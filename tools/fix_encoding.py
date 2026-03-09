"""Fix encoding issues in manifest.json and reconcile era entries."""
import json
import os
import glob

MANIFEST = "manifest.json"

# Read as raw bytes
with open(MANIFEST, "rb") as f:
    raw = f.read()

# Check for double-encoded UTF-8 (common mojibake pattern)
# em-dash U+2014 in proper UTF-8 = e2 80 94
# If double-encoded through latin-1: c3 a2 c2 80 c2 94
# But we see "a\xcc\x82\xe2\x82\xac\xe2\x80\x9c" or similar patterns

# Strategy: decode as utf-8, then fix known problem patterns
text = raw.decode("utf-8", errors="replace")

# The problem: some em-dashes got double-encoded
# Pattern: â€" (which is bytes c3 a2 c2 80 c2 94 in double-encoded UTF-8)
# or the Read tool showed â€" which means the bytes are actually
# the proper em-dash U+2014 but rendered through a wrong codepage
# Let me try a different approach: fix the mojibake

# Try to detect if the file has BOM or encoding markers
print(f"File size: {len(raw)} bytes")
print(f"First 3 bytes: {raw[:3].hex()}")

# Check for the mojibake pattern for em-dash
# "â€"" as UTF-8 bytes is: c3 a2 c2 80 e2 80 93 (for en-dash)
# or c3 a2 c2 80 e2 80 94 (for em-dash)
# But actually the most common double-encoding of U+2014 through cp1252->UTF-8 gives:
# U+2014 -> cp1252 byte 0x97 -> UTF-8 encodes 0x97 as... wait

# Let me just check what pattern appears before " rebellion"
idx = text.find("rebellion, Nephilim")
if idx > 0:
    snippet = text[idx-20:idx+5]
    print(f"Around 'rebellion': {repr(snippet)}")
    # Also check the raw bytes
    ridx = raw.find(b"rebellion, Nephilim")
    print(f"Raw bytes before rebellion: {raw[ridx-10:ridx].hex(' ')}")

# Count replacement characters
print(f"Replacement chars (U+FFFD): {text.count(chr(0xFFFD))}")

# The real issue might be simpler: let me try to find all smart/curly quotes
# that are used as JSON delimiters (not inside strings)
import re

# Find all non-ASCII quote-like characters
for i, ch in enumerate(text):
    if ch in "\u201c\u201d\u201e\u201f\u2018\u2019\u201a\u201b":
        context = text[max(0,i-30):i+30]
        print(f"Smart quote at pos {i}: {repr(ch)} context: {repr(context[:60])}")
        if i > 100:
            break  # Just show first few

# Simpler approach: just replace ALL non-ASCII quote chars with ASCII equivalents
# and also fix the mojibake em-dashes
fixed = text
fixed = fixed.replace("\u201c", '"')
fixed = fixed.replace("\u201d", '"')
fixed = fixed.replace("\u2018", "'")
fixed = fixed.replace("\u2019", "'")

# Now check if there are unmatched quotes after the replacement
# by trying to parse
try:
    data = json.loads(fixed)
    print(f"\nParsed successfully: {len(data['texts'])} texts, {len(data['eras'])} eras")
except json.JSONDecodeError as e:
    print(f"\nStill broken at line {e.lineno}, col {e.colno}")
    lines = fixed.split("\n")
    print(f"Problem line: {repr(lines[e.lineno-1][:200])}")

    # The em-dash problem: the sequence "â€"" contains \u201c which is a left
    # double quote. When we replace it with ", it breaks the JSON string.
    # Solution: we need to handle em-dash mojibake BEFORE quote replacement.

    # The â in â€" is U+00E2, the € is... actually in the file,
    # "â€"" could be the double-encoded em-dash
    # Original UTF-8 em-dash: bytes e2 80 94
    # If those bytes are treated as cp1252: â (e2) € (80) " (94) -> "â€""
    # Then encoded back to UTF-8: c3 a2 e2 82 ac e2 80 9c

    # So the fix is: find the pattern and replace with actual em-dash
    text2 = raw.decode("utf-8", errors="replace")

    # Try decoding as cp1252 then re-encoding properly... this is tricky
    # Let's try a different approach: use chardet or just brute force it

    # Actually, the simplest fix: read as latin-1, then encode to utf-8
    # the bytes that should be utf-8
    print("\nTrying alternative: fix double-encoding")

    # The pattern "\u00e2\u20ac\u201c" or "\u00e2\u20ac\u0094" is double-encoded em-dash
    fixed2 = text
    # â€" (â=\u00e2, €=\u20ac, "=\u201c) -> this is em-dash double-encoded via cp1252
    fixed2 = fixed2.replace("\u00e2\u20ac\u201c", "\u2014")  # em-dash
    fixed2 = fixed2.replace("\u00e2\u20ac\u201d", "\u2014")  # alt em-dash
    fixed2 = fixed2.replace("\u00e2\u20ac\u2122", "'")  # apostrophe mojibake
    fixed2 = fixed2.replace("\u00e2\u20ac\u0099", "'")  # alt apostrophe

    # Now do the smart quote replacement
    fixed2 = fixed2.replace("\u201c", '"')
    fixed2 = fixed2.replace("\u201d", '"')
    fixed2 = fixed2.replace("\u2018", "'")
    fixed2 = fixed2.replace("\u2019", "'")

    try:
        data = json.loads(fixed2)
        print(f"Fixed! {len(data['texts'])} texts, {len(data['eras'])} eras")
        fixed = fixed2
    except json.JSONDecodeError as e2:
        print(f"Still broken: line {e2.lineno}, col {e2.colno}")
        lines2 = fixed2.split("\n")
        print(f"Line: {repr(lines2[e2.lineno-1][:200])}")

if "data" in dir():
    # Now reconcile era data_file entries
    actual_files = {}
    for text_entry in data["texts"]:
        text_id = text_entry["id"]
        data_dir = text_entry.get("data_dir", text_id)
        dir_path = os.path.join("data", data_dir)
        if os.path.isdir(dir_path):
            era_files = glob.glob(os.path.join(dir_path, "era_*.py"))
            actual_files[text_id] = [
                os.path.splitext(os.path.basename(f))[0] for f in era_files
            ]
        else:
            actual_files[text_id] = []

    fixes = 0
    missing_list = []
    for era in data["eras"]:
        text_id = era["text"]
        if "data_file" not in era:
            # html_fragment eras (heavenly_court) don't have data_file
            continue
        manifest_df = era["data_file"]
        disk_files = actual_files.get(text_id, [])
        if manifest_df in disk_files:
            continue
        parts = manifest_df.split("_")
        if len(parts) >= 2:
            era_num = parts[1]
            matches = [f for f in disk_files if f.startswith(f"era_{era_num}_") or f == f"era_{era_num}"]
            if len(matches) == 1:
                old = manifest_df
                era["data_file"] = matches[0]
                print(f"  FIX: {text_id} | {old} -> {matches[0]}")
                fixes += 1
            elif len(matches) == 0:
                missing_list.append((text_id, manifest_df))
            else:
                print(f"  AMBIGUOUS: {text_id} | {manifest_df} -> {matches}")

    # Remove duplicates
    seen = set()
    dupes = []
    for i, era in enumerate(data["eras"]):
        if "data_file" not in era:
            continue
        key = (era["text"], era["data_file"])
        if key in seen:
            dupes.append(i)
        seen.add(key)
    for i in reversed(dupes):
        removed = data["eras"].pop(i)
        print(f"  DUPE REMOVED: {removed['text']}/{removed['data_file']}")

    print(f"\n=== Summary ===")
    print(f"  Fixes: {fixes}")
    print(f"  Dupes removed: {len(dupes)}")
    print(f"  Missing: {len(missing_list)}")
    for t, f in missing_list:
        print(f"    {t}/{f}")

    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\nManifest saved: {len(data['texts'])} texts, {len(data['eras'])} eras")
