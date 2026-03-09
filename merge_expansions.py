"""
merge_expansions.py -- Merge SCRIBE-generated chapter expansions into era_parables.py

Reads the 13 thin chapters' expansions from .py and .log files in agents/reports/,
parses them as Python dicts, and replaces the corresponding thin chapters in
data/enoch1/era_parables.py with the expanded versions.

Strategy for parsing:
    The SCRIBE-generated files contain Python dict literals, but some string
    values contain unescaped double quotes (e.g., biblical quotations with
    nested "..." inside "..." strings). Standard ast.literal_eval fails on
    these. We use a two-pass approach:
      1. First try ast.literal_eval (works for well-formed files)
      2. If that fails, preprocess the text line-by-line to escape inner quotes
         in ALL string values, not just known keys

Usage:
    python merge_expansions.py
"""

import os
import sys
import ast
import re
import json
import shutil
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent
ERA_FILE = BASE / "data" / "enoch1" / "era_parables.py"
REPORTS_DIR = BASE / "agents" / "reports"

# The 13 thin chapter IDs to expand
THIN_IDS = [
    "1en-52", "1en-53", "1en-54", "1en-55", "1en-56", "1en-57",
    "1en-58", "1en-59", "1en-64", "1en-65", "1en-66", "1en-68", "1en-70",
]

# Mapping: chapter_id -> preferred source file (second-run .py files are preferred)
PY_SOURCES = {
    "1en-55": "scribe_expansion_task_004.py",
    "1en-56": "scribe_expansion_task_005.py",
    "1en-57": "scribe_expansion_task_006.py",
    "1en-64": "scribe_expansion_task_009.py",
    "1en-65": "scribe_expansion_task_010.py",
    "1en-68": "scribe_expansion_task_012.py",
    "1en-70": "scribe_expansion_task_013.py",
}

# These 6 only exist in first-run .log files:
LOG_SOURCES = {
    "1en-52": "scribe_20260219_075610.log",
    "1en-53": "scribe_20260219_075833.log",
    "1en-54": "scribe_20260219_080042.log",
    "1en-58": "scribe_20260219_080825.log",
    "1en-59": "scribe_20260219_081020.log",
    "1en-66": "scribe_20260219_081711.log",
}


def fix_all_string_values(text):
    """Fix unescaped double quotes inside ALL double-quoted string values.

    This processes the text line by line. For each line that contains a
    key-value pair where the value is a double-quoted string, it finds the
    value boundaries and escapes any inner double quotes.

    Works for patterns like:
        "key": "value with "nested quotes" inside",
        "key": "value with 'single quotes' inside",  (no change needed)

    The trick: for each line, we identify where the value string starts
    (after "key": ") and where it ends (the last " before optional comma).
    Everything between those two quotes gets inner " escaped.
    """
    lines = text.split("\n")
    fixed_lines = []

    for line in lines:
        fixed_lines.append(fix_line_quotes(line))

    return "\n".join(fixed_lines)


def fix_line_quotes(line):
    """Fix unescaped double quotes in a single line's string value.

    Handles patterns like:
        "key": "text with "inner" quotes",
        {"ref": "...", "note": "text with "inner" quotes", "type": "ot"},
    """
    stripped = line.strip()

    # Skip empty lines, comments, lines that are just structural
    if not stripped or stripped.startswith('#'):
        return line
    if stripped in ('{', '}', '},', '{},', '[', ']', '],'):
        return line

    # For lines that have string values, we need to identify each
    # "key": "value" pair and fix inner quotes in the value.
    # We'll do this by processing the line character by character.

    result = []
    i = 0
    n = len(line)

    while i < n:
        # Look for a key-value pattern: "key": "value..."
        # First, find a quoted key followed by colon
        if line[i] == '"':
            # Read the key
            key_start = i
            i += 1
            while i < n and line[i] != '"':
                if line[i] == '\\':
                    i += 1  # skip escaped char
                i += 1
            if i >= n:
                # Malformed, just append rest
                result.append(line[key_start:])
                break
            i += 1  # past closing "
            key_end = i
            result.append(line[key_start:key_end])

            # Skip whitespace and colon
            while i < n and line[i] in ' \t':
                result.append(line[i])
                i += 1

            if i < n and line[i] == ':':
                result.append(':')
                i += 1

                # Skip whitespace
                while i < n and line[i] in ' \t':
                    result.append(line[i])
                    i += 1

                # Now check what the value is
                if i < n and line[i] == '"':
                    # String value! Find its true end and escape inner quotes.
                    fixed_value, new_i = fix_string_value(line, i)
                    result.append(fixed_value)
                    i = new_i
                else:
                    # Not a string value (number, bool, list, dict, etc.)
                    # Just pass through
                    continue
            else:
                # Not a key-value pair, continue
                continue
        else:
            result.append(line[i])
            i += 1

    return "".join(result)


def fix_string_value(line, start):
    """Fix a double-quoted string value starting at position `start` in line.

    The string starts with " at position `start`. We need to find where it
    truly ends. The true end is the last " on the line before optional
    comma and optional whitespace, UNLESS there's a subsequent key-value pair
    on the same line (like in a compact dict).

    For inline dicts like:
        {"ref": "Job 38:22-35", "note": "...text with "quotes"...", "type": "ot"},

    We need to identify the boundaries of each string value within the line.

    Strategy: We know the string ends when we see ", followed by either:
        - end of line (optionally with whitespace)
        - comma + whitespace (possibly followed by another key or end bracket)
        - comma + closing brace/bracket

    We use a greedy approach: scan forward from the opening quote, and at
    each " we encounter, check if it looks like a string terminator by
    examining what follows.
    """
    i = start + 1  # past opening "
    n = len(line)
    content_chars = []

    while i < n:
        c = line[i]

        if c == '\\' and i + 1 < n:
            # Already escaped character - keep as-is
            content_chars.append(c)
            content_chars.append(line[i + 1])
            i += 2
            continue

        if c == '"':
            # Is this the end of the string? Check what follows.
            rest = line[i + 1:].lstrip()
            if (not rest or
                rest[0] == ',' or
                rest[0] == '}' or
                rest[0] == ']' or
                rest.startswith(': ') or
                rest.startswith(':')):
                # This is a genuine string terminator
                escaped_content = "".join(content_chars)
                return '"' + escaped_content + '"', i + 1
            else:
                # This is an inner quote that needs escaping
                content_chars.append('\\"')
                i += 1
                continue

        content_chars.append(c)
        i += 1

    # Reached end of line without finding closing quote
    escaped_content = "".join(content_chars)
    return '"' + escaped_content, i


def extract_raw_text_from_py(filepath):
    """Extract the raw dict text from a .py expansion file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.search(r'""".*?"""', text, re.DOTALL)
    if match:
        text = text[match.end():]
    return text.strip()


def extract_raw_text_from_log(filepath):
    """Extract the raw dict text from a .log expansion file."""
    text = filepath.read_text(encoding="utf-8")
    sep_idx = text.find("=" * 20)
    if sep_idx == -1:
        raise ValueError(f"No separator found in {filepath}")
    after_sep = text[sep_idx:]
    newline_idx = after_sep.find("\n")
    if newline_idx != -1:
        after_sep = after_sep[newline_idx:]
    return after_sep.strip()


def find_matching_brace(text, start):
    """Find the matching closing brace for the opening brace at `start`.

    Uses simple depth counting (not string-aware, but used as a rough
    boundary finder).
    """
    depth = 0
    for i in range(start, len(text)):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return i
    return -1


def parse_dict_text(text):
    """Parse a Python dict literal from text, with robust handling of
    unescaped quotes and other common issues."""

    # Find the outermost { ... }
    start = text.find("{")
    if start == -1:
        raise ValueError("No opening brace found in text")

    end = find_matching_brace(text, start)
    if end == -1:
        raise ValueError("No matching closing brace found")

    dict_text = text[start:end + 1]

    # Attempt 1: Try ast.literal_eval directly
    try:
        result = ast.literal_eval(dict_text)
        if isinstance(result, dict):
            return result
    except (ValueError, SyntaxError):
        pass

    # Attempt 2: Fix unescaped quotes line by line
    fixed = fix_all_string_values(dict_text)

    try:
        result = ast.literal_eval(fixed)
        if isinstance(result, dict):
            return result
    except (ValueError, SyntaxError) as e:
        # Show context around the error for debugging
        if hasattr(e, 'lineno') and e.lineno:
            fixed_lines = fixed.split("\n")
            ln = e.lineno
            context_start = max(0, ln - 3)
            context_end = min(len(fixed_lines), ln + 2)
            print(f"    Parse error at line {ln}:")
            for ci in range(context_start, context_end):
                marker = ">>>" if ci == ln - 1 else "   "
                print(f"    {marker} {ci+1}: {fixed_lines[ci][:150]}")
        pass

    # Attempt 3: JSON approach
    json_text = fixed
    json_text = re.sub(r'\bNone\b', 'null', json_text)
    json_text = re.sub(r'\bTrue\b', 'true', json_text)
    json_text = re.sub(r'\bFalse\b', 'false', json_text)
    json_text = re.sub(r',(\s*[}\]])', r'\1', json_text)

    try:
        result = json.loads(json_text)
        if isinstance(result, dict):
            return result
    except json.JSONDecodeError as e:
        pass

    raise ValueError(f"All parse attempts failed for text starting with: {dict_text[:200]}")


def extract_dict_from_py(filepath):
    """Extract the chapter dict from a .py expansion file."""
    text = extract_raw_text_from_py(filepath)
    return parse_dict_text(text)


def extract_dict_from_log(filepath):
    """Extract the chapter dict from a .log expansion file."""
    text = extract_raw_text_from_log(filepath)
    return parse_dict_text(text)


def format_value(value, indent=8):
    """Format a Python value for writing into the CHAPTERS list."""
    if value is None:
        return "None"
    elif isinstance(value, bool):
        return "True" if value else "False"
    elif isinstance(value, str):
        return repr(value)
    elif isinstance(value, (int, float)):
        return repr(value)
    elif isinstance(value, list):
        return format_list(value, indent)
    elif isinstance(value, dict):
        return format_dict(value, indent)
    else:
        return repr(value)


def format_list(lst, indent=8):
    """Format a list value."""
    if not lst:
        return "[]"

    indent_str = " " * indent
    inner_indent = " " * (indent + 4)

    # List of simple strings on one line
    if all(isinstance(item, str) for item in lst):
        items = [repr(item) for item in lst]
        one_line = "[" + ", ".join(items) + "]"
        if len(one_line) + indent < 100:
            return one_line

    # Multi-line list
    lines = ["["]
    for item in lst:
        formatted = format_value(item, indent + 4)
        lines.append(f"{inner_indent}{formatted},")
    lines.append(f"{indent_str}]")
    return "\n".join(lines)


def format_dict(d, indent=8):
    """Format a dict value."""
    if not d:
        return "{}"

    indent_str = " " * indent
    inner_indent = " " * (indent + 4)

    # Simple one-liner dicts (cross_ref entries, key_verse, etc.)
    if len(d) <= 4 and all(isinstance(v, (str, int, bool, type(None))) for v in d.values()):
        items = []
        for k, v in d.items():
            items.append(f"{repr(k)}: {format_value(v, 0)}")
        one_line = "{" + ", ".join(items) + "}"
        if len(one_line) + indent < 100:
            return one_line

    # Multi-line dict
    lines = ["{"]
    for k, v in d.items():
        formatted = format_value(v, indent + 4)
        lines.append(f"{inner_indent}{repr(k)}: {formatted},")
    lines.append(f"{indent_str}" + "}")
    return "\n".join(lines)


def format_chapter_dict(chapter, indent=4):
    """Format a complete chapter dict for insertion into the CHAPTERS list."""
    indent_str = " " * indent
    inner_indent = " " * (indent + 4)

    lines = [f"{indent_str}" + "{"]

    key_order = [
        "id", "ref", "chapter_num", "title", "era", "type",
        "synopsis", "key_verse", "hebrew_terms", "ane_backdrop",
        "second_temple", "cross_refs", "divine_council_note", "sections"
    ]

    written_keys = set()
    for key in key_order:
        if key in chapter:
            val = chapter[key]
            formatted = format_value(val, indent + 4)
            lines.append(f"")
            lines.append(f"{inner_indent}{repr(key)}: {formatted},")
            written_keys.add(key)

    for key in chapter:
        if key not in written_keys:
            val = chapter[key]
            formatted = format_value(val, indent + 4)
            lines.append(f"")
            lines.append(f"{inner_indent}{repr(key)}: {formatted},")

    lines.append(f"{indent_str}" + "}")
    return "\n".join(lines)


def load_expansion(chapter_id):
    """Load the expanded chapter dict for a given chapter ID."""

    # Prefer .py files (second run)
    if chapter_id in PY_SOURCES:
        filepath = REPORTS_DIR / PY_SOURCES[chapter_id]
        if filepath.exists():
            print(f"  [{chapter_id}] Loading from {PY_SOURCES[chapter_id]}")
            return extract_dict_from_py(filepath)

    # Fall back to .log files (first run)
    if chapter_id in LOG_SOURCES:
        filepath = REPORTS_DIR / LOG_SOURCES[chapter_id]
        if filepath.exists():
            print(f"  [{chapter_id}] Loading from {LOG_SOURCES[chapter_id]}")
            return extract_dict_from_log(filepath)

    raise FileNotFoundError(f"No expansion file found for {chapter_id}")


def main():
    print("=" * 60)
    print("  MERGE SCRIBE EXPANSIONS INTO era_parables.py")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # -- Restore from backup if previous run modified the file --
    backup_path = ERA_FILE.with_suffix(".py.bak")
    if backup_path.exists():
        print(f"\n[0] Restoring from backup ...")
        shutil.copy2(backup_path, ERA_FILE)

    # -- Step 1: Read --
    print(f"\n[1] Reading {ERA_FILE} ...")
    source_text = ERA_FILE.read_text(encoding="utf-8")
    orig_line_count = source_text.count("\n")
    print(f"    {orig_line_count} lines")

    # -- Step 2: Parse existing CHAPTERS --
    print("\n[2] Parsing CHAPTERS list ...")

    doc_match = re.match(r'(""".*?""")\s*\n', source_text, re.DOTALL)
    if not doc_match:
        print("ERROR: Could not find module docstring")
        sys.exit(1)
    docstring = doc_match.group(1)

    chapters_match = re.search(r'CHAPTERS\s*=\s*\[', source_text)
    if not chapters_match:
        print("ERROR: Could not find CHAPTERS = [")
        sys.exit(1)

    list_start = source_text.find("[", chapters_match.start())

    # Find matching ] with string awareness
    depth = 0
    in_str = False
    str_char = None
    esc = False
    list_end = -1
    for i in range(list_start, len(source_text)):
        c = source_text[i]
        if esc:
            esc = False
            continue
        if c == '\\' and in_str:
            esc = True
            continue
        if not in_str:
            if c == '"':
                in_str = True
                str_char = '"'
                continue
            elif c == "'":
                in_str = True
                str_char = "'"
                continue
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    list_end = i
                    break
        else:
            if c == str_char:
                in_str = False
                str_char = None

    if list_end == -1:
        print("ERROR: Could not find end of CHAPTERS list")
        sys.exit(1)

    chapters_text = source_text[list_start:list_end + 1]

    try:
        chapters = ast.literal_eval(chapters_text)
    except (ValueError, SyntaxError) as e:
        print(f"ERROR: Could not parse CHAPTERS: {e}")
        sys.exit(1)

    print(f"    {len(chapters)} entries in CHAPTERS")

    thin_found = []
    for ch in chapters:
        if ch.get("id") in THIN_IDS:
            sections = ch.get("sections", [])
            thin_found.append((ch["id"], ch.get("title", "?"), len(sections)))

    print(f"    {len(thin_found)} thin chapters found:")
    for cid, title, nsec in thin_found:
        print(f"      {cid}: {title} ({nsec} section(s))")

    # -- Step 3: Load expansions --
    print(f"\n[3] Loading {len(THIN_IDS)} expansions ...")
    expansions = {}
    for chapter_id in THIN_IDS:
        try:
            expanded = load_expansion(chapter_id)
            sections = expanded.get("sections", [])
            if len(sections) > 20:
                print(f"       -> WARNING: {len(sections)} sections (seems wrong, skipping)")
                continue
            print(f"       -> {len(sections)} sections")
            expansions[chapter_id] = expanded
        except Exception as e:
            print(f"  ERROR loading {chapter_id}: {e}")

    print(f"    Successfully loaded {len(expansions)}/{len(THIN_IDS)} expansions")

    if not expansions:
        print("ERROR: No expansions loaded, aborting")
        sys.exit(1)

    # -- Step 4: Merge --
    print(f"\n[4] Merging ...")
    merged_count = 0
    for i, ch in enumerate(chapters):
        cid = ch.get("id")
        if cid in expansions:
            expanded = expansions[cid]

            if "chapter_num" not in expanded and "chapter_num" in ch:
                expanded["chapter_num"] = ch["chapter_num"]
            if "era" not in expanded:
                expanded["era"] = ch.get("era", "parables")
            if "type" not in expanded:
                expanded["type"] = ch.get("type", "chapter")

            old_sections = len(ch.get("sections", []))
            new_sections = len(expanded.get("sections", []))

            chapters[i] = expanded
            merged_count += 1
            print(f"    {cid}: {old_sections} -> {new_sections} sections")

    print(f"    Merged {merged_count} chapters")

    # -- Step 5: Reconstruct file --
    print(f"\n[5] Reconstructing era_parables.py ...")

    # Extract section comments from original
    section_comments = {}
    orig_lines = source_text.split("\n")
    for i, line in enumerate(orig_lines):
        if '"id":' in line:
            comment_block = []
            for j in range(max(0, i - 5), i):
                stripped = orig_lines[j].strip()
                if stripped.startswith("#"):
                    comment_block.append(orig_lines[j])
            if comment_block:
                id_match = re.search(r'"id":\s*"([^"]+)"', line)
                if id_match:
                    section_comments[id_match.group(1)] = "\n".join(comment_block)

    output_lines = [docstring, "", "CHAPTERS = ["]

    for idx, ch in enumerate(chapters):
        cid = ch.get("id", "")
        if cid in section_comments:
            output_lines.append(section_comments[cid])
        formatted = format_chapter_dict(ch, indent=4)
        output_lines.append(formatted + ",")
        output_lines.append("")

    output_lines.append("]")
    output_lines.append("")

    new_content = "\n".join(output_lines)

    # -- Step 6: Validate --
    print(f"\n[6] Validating ...")
    try:
        compile(new_content, "era_parables.py", "exec")
        print("    Syntax OK")
    except SyntaxError as e:
        print(f"    SYNTAX ERROR: {e}")
        draft_path = ERA_FILE.parent / "era_parables_MERGED_DRAFT.py"
        draft_path.write_text(new_content, encoding="utf-8")
        print(f"    Draft saved to {draft_path}")
        sys.exit(1)

    try:
        exec_globals = {}
        exec(new_content, exec_globals)
        loaded_chapters = exec_globals.get("CHAPTERS", [])
        print(f"    Data OK: {len(loaded_chapters)} entries loaded")

        for ch in loaded_chapters:
            if ch.get("id") in expansions:
                nsec = len(ch.get("sections", []))
                if nsec <= 1:
                    print(f"    WARNING: {ch['id']} still has only {nsec} section(s)!")
    except Exception as e:
        print(f"    DATA ERROR: {e}")
        draft_path = ERA_FILE.parent / "era_parables_MERGED_DRAFT.py"
        draft_path.write_text(new_content, encoding="utf-8")
        print(f"    Draft saved to {draft_path}")
        sys.exit(1)

    # -- Step 7: Write --
    print(f"\n[7] Writing ...")

    if not backup_path.exists():
        shutil.copy2(ERA_FILE, backup_path)
        print(f"    Backup: {backup_path}")

    ERA_FILE.write_text(new_content, encoding="utf-8")
    new_line_count = new_content.count("\n")
    print(f"    Written: {ERA_FILE}")
    print(f"    Lines: {orig_line_count} -> {new_line_count}")

    # -- Summary --
    print(f"\n{'=' * 60}")
    print(f"  MERGE COMPLETE")
    print(f"  Chapters expanded: {merged_count}")
    print(f"  File: {orig_line_count} -> {new_line_count} lines")
    print()
    print(f"  Expansion details:")
    for ch in loaded_chapters:
        cid = ch.get("id", "")
        if cid in expansions:
            nsec = len(ch.get("sections", []))
            print(f"    {cid}: {nsec} sections")
    print(f"{'=' * 60}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
