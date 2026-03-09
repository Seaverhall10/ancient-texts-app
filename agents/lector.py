"""
THE LECTOR — Language & Glossary Specialist Agent

Generates glossary entries, interlinear word-by-word data,
and validates Hebrew/Greek/Aramaic terminology across the project.

Usage:
    python agents/lector.py --glossary "Generate terms for 1 Enoch Watchers section"
    python agents/lector.py --audit-terms   # Check all hebrew_terms refs exist in glossary
    python agents/lector.py --task-file agents/tasks/pending/task_xxx.json
"""
import os
import sys
import json
import argparse
import importlib.util
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.config import (
    LECTOR_API_KEY, LECTOR_MODEL, LECTOR_TEMPERATURE,
    DATA_DIR, MANIFEST_PATH, REPORTS_DIR,
    LECTOR_GUIDELINES, MAX_TOKENS_LECTOR
)


def get_client():
    """Create Anthropic client with LECTOR's own API key."""
    if not LECTOR_API_KEY:
        print("ERROR: Set LECTOR_API_KEY in agents/config.py or environment")
        sys.exit(1)
    from anthropic import Anthropic
    return Anthropic(api_key=LECTOR_API_KEY)


def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_glossary():
    gpath = os.path.join(DATA_DIR, "glossary.py")
    if os.path.exists(gpath):
        mod = load_module("glossary", gpath)
        return getattr(mod, "GLOSSARY", {})
    return {}


def audit_term_references():
    """Check that all hebrew_terms in chapter data reference existing glossary entries."""
    manifest = load_manifest()
    glossary = load_glossary()
    glossary_keys = set(glossary.keys())
    findings = []
    used_keys = set()

    for era in manifest["eras"]:
        if era.get("content_type") == "html_fragment":
            continue
        text_id = era.get("text")
        text_def = next((t for t in manifest["texts"] if t["id"] == text_id), None)
        if not text_def:
            continue

        data_dir = text_def.get("data_dir", text_id)
        data_file = era.get("data_file")
        if not data_file:
            continue

        path = os.path.join(DATA_DIR, data_dir, data_file + ".py")
        if not os.path.exists(path):
            path = os.path.join(DATA_DIR, data_file + ".py")
        if not os.path.exists(path):
            continue

        try:
            mod = load_module(data_file, path)
            chapters = getattr(mod, "CHAPTERS", [])
            for ch in chapters:
                for term_key in ch.get("hebrew_terms", []):
                    if isinstance(term_key, str):
                        used_keys.add(term_key)
                        if term_key not in glossary_keys:
                            findings.append({
                                "chapter": ch.get("id"),
                                "era": era["id"],
                                "term": term_key,
                                "text": text_id
                            })
        except Exception:
            pass

    # Find unused glossary entries
    unused = glossary_keys - used_keys
    return findings, unused


def generate_glossary_entries(task_description):
    """Use AI to generate new glossary entries."""
    client = get_client()
    glossary = load_glossary()

    existing_keys = list(glossary.keys())

    system_prompt = f"""You are THE LECTOR -- a language specialist for the Ancient Texts Study app.

Your role: Generate scholarly glossary entries for Hebrew, Aramaic, Greek, and Ge'ez terms.

{LECTOR_GUIDELINES}

EXISTING GLOSSARY KEYS (do NOT duplicate these):
{', '.join(existing_keys)}

OUTPUT FORMAT:
Return ONLY a valid Python dictionary literal (no variable assignment, no imports).
Each key is a term slug, each value follows the glossary entry format above.
Example:
{{
    "new_term": {{
        "hebrew": "Unicode",
        "transliteration": "...",
        "strongs": "H1234",
        "gloss": "short meaning",
        "definition": "Full definition...",
        "language": "hebrew",
        "chapters_used": ["gen-1"]
    }}
}}
"""

    print(f"[lector] Generating glossary entries...")
    print(f"[lector] Task: {task_description}")

    response = client.messages.create(
        model=LECTOR_MODEL,
        max_tokens=MAX_TOKENS_LECTOR,
        temperature=LECTOR_TEMPERATURE,
        system=system_prompt,
        messages=[
            {"role": "user", "content": task_description}
        ]
    )

    result_text = response.content[0].text

    # Extract Python dict from response
    try:
        if "```python" in result_text:
            result_text = result_text.split("```python")[1].split("```")[0]
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0]

        # Try to parse as Python dict
        new_entries = eval(result_text.strip())
        if not isinstance(new_entries, dict):
            raise ValueError("Response is not a dictionary")
        return new_entries, response.usage
    except Exception as e:
        print(f"[lector] ERROR parsing response: {e}")
        # Save raw response for debugging
        log_path = os.path.join(REPORTS_DIR, f"lector_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        os.makedirs(REPORTS_DIR, exist_ok=True)
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(result_text)
        print(f"[lector] Raw response saved to: {log_path}")
        return {}, response.usage


def merge_glossary_entries(new_entries):
    """Merge new entries into glossary.py."""
    glossary = load_glossary()
    added = 0
    skipped = 0

    for key, entry in new_entries.items():
        if key in glossary:
            # Extend chapters_used if new chapters found
            existing_chapters = set(glossary[key].get("chapters_used", []))
            new_chapters = set(entry.get("chapters_used", []))
            if new_chapters - existing_chapters:
                glossary[key]["chapters_used"] = sorted(existing_chapters | new_chapters)
                print(f"  [+] Extended chapters_used for '{key}'")
            else:
                skipped += 1
        else:
            glossary[key] = entry
            added += 1
            print(f"  [+] Added new term: '{key}'")

    # Write back
    gpath = os.path.join(DATA_DIR, "glossary.py")
    with open(gpath, "w", encoding="utf-8") as f:
        f.write('"""\nglossary.py -- Multi-language term glossary for Ancient Texts Library.\n')
        f.write('Each entry is keyed by a slug used in chapter data files.\n')
        f.write('Supports Hebrew, Aramaic, Greek, and Ge\'ez terms.\n')
        f.write('The \'language\' field enables filtering in the glossary UI.\n"""\n\n')
        f.write('GLOSSARY = ')
        # Pretty print with proper Unicode
        f.write(json.dumps(glossary, indent=4, ensure_ascii=False))
        f.write('\n')

    print(f"\n[lector] Glossary updated: {added} added, {skipped} skipped")
    return added, skipped


def generate_report(findings, unused, new_count=0):
    """Generate a term audit report."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(REPORTS_DIR, f"lector_audit_{timestamp}.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# THE LECTOR -- Term Audit Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Count |\n|--------|-------|\n")
        f.write(f"| Missing glossary entries | {len(findings)} |\n")
        f.write(f"| Unused glossary entries | {len(unused)} |\n")
        f.write(f"| New entries generated | {new_count} |\n\n")

        if findings:
            f.write(f"## Missing Terms\n\n")
            f.write(f"| Term Key | Chapter | Era | Text |\n")
            f.write(f"|----------|---------|-----|------|\n")
            for finding in findings:
                f.write(f"| `{finding['term']}` | {finding['chapter']} | {finding['era']} | {finding['text']} |\n")

        if unused:
            f.write(f"\n## Unused Glossary Entries\n\n")
            for key in sorted(unused):
                f.write(f"- `{key}`\n")

    print(f"[lector] Report saved: {report_path}")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="THE LECTOR -- Language Specialist")
    parser.add_argument("--glossary", type=str, help="Generate glossary entries (AI)")
    parser.add_argument("--audit-terms", action="store_true", help="Audit term references")
    parser.add_argument("--task-file", type=str, help="Process a task file")
    parser.add_argument("--merge", action="store_true", help="Merge generated entries into glossary.py")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  THE LECTOR -- Language Specialist")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    if args.audit_terms:
        print("[lector] Auditing term references...")
        findings, unused = audit_term_references()
        report = generate_report(findings, unused)
        print(f"\n  Missing terms: {len(findings)}")
        print(f"  Unused terms: {len(unused)}")
        if findings:
            print(f"\n  Sample missing terms:")
            for f in findings[:10]:
                print(f"    - '{f['term']}' in {f['chapter']} ({f['text']})")

    elif args.glossary:
        new_entries, usage = generate_glossary_entries(args.glossary)
        print(f"[lector] Generated {len(new_entries)} entries")
        print(f"[lector] Tokens: {usage.input_tokens} in / {usage.output_tokens} out")
        if new_entries and args.merge:
            merge_glossary_entries(new_entries)
        elif new_entries:
            print("[lector] Use --merge flag to write entries to glossary.py")
            print("[lector] Preview:")
            for key in list(new_entries.keys())[:5]:
                print(f"  {key}: {new_entries[key].get('gloss', '?')}")

    elif args.task_file:
        with open(args.task_file, "r", encoding="utf-8") as f:
            task = json.load(f)
        desc = task.get("description", "")
        new_entries, usage = generate_glossary_entries(desc)
        if new_entries:
            merge_glossary_entries(new_entries)

    else:
        print("Usage:")
        print("  python agents/lector.py --audit-terms              # Audit all term references")
        print("  python agents/lector.py --glossary 'Generate...'   # AI-generate terms")
        print("  python agents/lector.py --glossary '...' --merge   # Generate and merge")


if __name__ == "__main__":
    main()
