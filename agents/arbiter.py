"""
THE ARBITER — Quality Audit Agent

Checks content for theological accuracy, formatting consistency,
cross-reference integrity, and canonical labeling correctness.

Usage:
    python agents/arbiter.py --audit-all
    python agents/arbiter.py --file data/enoch1/era_watchers.py
    python agents/arbiter.py --text 1enoch
"""
import os
import sys
import re
import json
import argparse
import importlib.util
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.config import (
    ARBITER_API_KEY, ARBITER_MODEL, ARBITER_TEMPERATURE,
    DATA_DIR, MANIFEST_PATH, REPORTS_DIR,
    THEOLOGICAL_GUIDELINES, AUDIT_LEVELS, MAX_TOKENS_ARBITER
)


def get_client():
    """Create Anthropic client with ARBITER's own API key."""
    if not ARBITER_API_KEY:
        print("ERROR: Set ARBITER_API_KEY in agents/config.py or environment")
        sys.exit(1)
    from anthropic import Anthropic
    return Anthropic(api_key=ARBITER_API_KEY)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_glossary():
    gpath = os.path.join(DATA_DIR, "glossary.py")
    if os.path.exists(gpath):
        mod = load_module("glossary", gpath)
        return getattr(mod, "GLOSSARY", {})
    return {}


# ══════════════════════════════════════════════════════════
# LOCAL AUDIT RULES (no API needed)
# ══════════════════════════════════════════════════════════

def audit_chapter_structure(ch, era_id, findings):
    """Check that a chapter has all required fields."""
    ch_type = ch.get("type", "chapter")
    # ref/key_verse are legitimately None for historical_insert and ane_backdrop types
    nullable_for_inserts = {"ref", "key_verse"}
    is_insert = ch_type in ("historical_insert", "ane_backdrop", "insert")

    required = ["id", "ref", "title", "era", "type", "synopsis"]
    for field in required:
        if field not in ch or not ch[field]:
            if is_insert and field in nullable_for_inserts:
                continue  # OK for inserts to have None ref/key_verse
            findings.append({
                "level": "CRITICAL",
                "chapter": ch.get("id", "UNKNOWN"),
                "era": era_id,
                "rule": "missing_field",
                "message": f"Missing required field: {field}"
            })

    # Key verse structure
    if ch.get("key_verse"):
        kv = ch["key_verse"]
        for kf in ["ref", "text", "translation"]:
            if kf not in kv or not kv[kf]:
                findings.append({
                    "level": "WARNING",
                    "chapter": ch.get("id"),
                    "era": era_id,
                    "rule": "incomplete_key_verse",
                    "message": f"Key verse missing field: {kf}"
                })

    # Cross-ref types
    for xr in ch.get("cross_refs", []):
        if isinstance(xr, str):
            continue  # Thematic texts use bare string cross-refs; skip type check
        if xr.get("type") not in ("ot", "nt", "ane", "dss", "pseudepigrapha", "thematic"):
            findings.append({
                "level": "WARNING",
                "chapter": ch.get("id"),
                "era": era_id,
                "rule": "invalid_xref_type",
                "message": f"Cross-ref '{xr.get('ref')}' has invalid type: {xr.get('type')}"
            })

    # Thin section check
    sections = ch.get("sections", [])
    if len(sections) < 2 and ch.get("type") == "chapter":
        findings.append({
            "level": "WARNING",
            "chapter": ch.get("id"),
            "era": era_id,
            "rule": "thin_content",
            "message": f"Only {len(sections)} section(s) — consider expanding"
        })


def audit_glossary_refs(ch, glossary_keys, findings):
    """Check that hebrew_terms reference existing glossary entries."""
    for term_key in ch.get("hebrew_terms", []):
        if not isinstance(term_key, str):
            continue
        if term_key not in glossary_keys:
            findings.append({
                "level": "WARNING",
                "chapter": ch.get("id"),
                "era": ch.get("era"),
                "rule": "missing_glossary_entry",
                "message": f"Hebrew term '{term_key}' not found in glossary.py"
            })


def audit_transliteration(ch, findings):
    """Check for inconsistent transliterations."""
    text = json.dumps(ch, ensure_ascii=False)
    bad_forms = {
        "Semjaza": "Shemihazah",
        "Shemyaza": "Shemihazah",
        "Semyaz": "Shemihazah",
        "bene elohim": "b'nei 'elohim",
        "Bene Elohim": "b'nei 'elohim",
    }
    for bad, good in bad_forms.items():
        if bad in text:
            findings.append({
                "level": "WARNING",
                "chapter": ch.get("id"),
                "era": ch.get("era"),
                "rule": "inconsistent_transliteration",
                "message": f"Found '{bad}' — should be '{good}'"
            })


def audit_canonical_language(ch, era_text_id, non_canonical_texts, findings):
    """Check for inappropriate canonical language in non-canonical texts."""
    if era_text_id not in non_canonical_texts:
        return
    text = json.dumps(ch, ensure_ascii=False).lower()
    bad_phrases = ["the bible says", "scripture tells us", "god's word says", "biblical text states"]
    for phrase in bad_phrases:
        if phrase in text:
            findings.append({
                "level": "CRITICAL",
                "chapter": ch.get("id"),
                "era": ch.get("era"),
                "rule": "canonical_language_violation",
                "message": f"Non-canonical text uses canonical language: '{phrase}'"
            })


def audit_html_fragments(fragments_dir, findings):
    """Audit THC HTML fragment files."""
    if not os.path.isdir(fragments_dir):
        return

    for fname in os.listdir(fragments_dir):
        if not fname.endswith(".html"):
            continue
        fpath = os.path.join(fragments_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for unclosed tags (basic)
        for tag in ["article", "div", "section"]:
            opens = len(re.findall(f"<{tag}[\\s>]", content))
            closes = len(re.findall(f"</{tag}>", content))
            if opens != closes:
                findings.append({
                    "level": "WARNING",
                    "chapter": fname,
                    "era": "heavenly_court",
                    "rule": "unclosed_html_tag",
                    "message": f"Tag <{tag}>: {opens} opens vs {closes} closes"
                })


def run_local_audit():
    """Run all local (non-API) audit rules."""
    manifest = load_manifest()
    glossary = load_glossary()
    glossary_keys = set(glossary.keys())
    findings = []

    non_canonical = {"1enoch", "giants", "jubilees", "jasher", "genesis_apocryphon", "dss_sectarian"}

    # Audit Python data files
    for era in manifest["eras"]:
        if era.get("content_type") == "html_fragment":
            continue  # Skip THC eras for data audit

        text_id = era.get("text")
        text_def = next((t for t in manifest["texts"] if t["id"] == text_id), None)
        if not text_def:
            continue

        data_dir = text_def.get("data_dir", text_id)
        data_file = os.path.join(DATA_DIR, data_dir, era.get("data_file", "") + ".py")
        if not os.path.exists(data_file):
            data_file = os.path.join(DATA_DIR, era.get("data_file", "") + ".py")
        if not os.path.exists(data_file):
            findings.append({
                "level": "WARNING",
                "chapter": "-",
                "era": era["id"],
                "rule": "missing_data_file",
                "message": f"Data file not found: {era.get('data_file')}.py"
            })
            continue

        mod = load_module(era.get("data_file", ""), data_file)
        chapters = getattr(mod, "CHAPTERS", [])

        for ch in chapters:
            audit_chapter_structure(ch, era["id"], findings)
            audit_glossary_refs(ch, glossary_keys, findings)
            audit_transliteration(ch, findings)
            audit_canonical_language(ch, text_id, non_canonical, findings)

    # Audit THC HTML fragments
    hc_dir = os.path.join(DATA_DIR, "heavenly_court", "chapters")
    audit_html_fragments(hc_dir, findings)

    return findings


def run_ai_audit(file_path):
    """Run AI-powered deep audit on a specific file."""
    client = get_client()

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Truncate if very large
    if len(content) > 30000:
        content = content[:30000] + "\n\n... (truncated) ..."

    system_prompt = f"""You are THE ARBITER — a theological accuracy auditor.

{THEOLOGICAL_GUIDELINES}

Audit the following content for:
1. CRITICAL: Wrong canonical status, scripture misquote, theological error
2. WARNING: Missing cross-reference, inconsistent transliteration, thin section
3. INFO: Style inconsistency, formatting nit

Output a JSON array of findings:
[{{"level": "CRITICAL|WARNING|INFO", "location": "...", "rule": "...", "message": "..."}}]

Be thorough but fair. Only flag genuine issues."""

    response = client.messages.create(
        model=ARBITER_MODEL,
        max_tokens=MAX_TOKENS_ARBITER,
        temperature=ARBITER_TEMPERATURE,
        system=system_prompt,
        messages=[
            {"role": "user", "content": f"Audit this file ({os.path.basename(file_path)}):\n\n{content}"}
        ]
    )

    result_text = response.content[0].text
    usage = getattr(response, 'usage', None)
    # Extract JSON from response
    try:
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0]
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0]
        return json.loads(result_text), usage
    except (json.JSONDecodeError, IndexError):
        return [{"level": "INFO", "location": file_path, "rule": "parse_error",
                 "message": f"Could not parse AI audit response: {result_text[:200]}"}], usage


def generate_report(findings, report_name="audit"):
    """Generate a markdown audit report."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(REPORTS_DIR, f"{report_name}_{timestamp}.md")

    critical = [f for f in findings if f.get("level") == "CRITICAL"]
    warnings = [f for f in findings if f.get("level") == "WARNING"]
    infos = [f for f in findings if f.get("level") == "INFO"]

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# THE ARBITER \u2014 Audit Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"| Level | Count |\n|-------|-------|\n")
        f.write(f"| CRITICAL | {len(critical)} |\n")
        f.write(f"| WARNING | {len(warnings)} |\n")
        f.write(f"| INFO | {len(infos)} |\n")
        f.write(f"| **Total** | **{len(findings)}** |\n\n")

        for level_name, level_findings in [("CRITICAL", critical), ("WARNING", warnings), ("INFO", infos)]:
            if level_findings:
                f.write(f"## {level_name}\n\n")
                for finding in level_findings:
                    ch = finding.get("chapter", finding.get("location", "?"))
                    f.write(f"- **[{finding.get('rule', '?')}]** `{ch}` \u2014 {finding.get('message', '')}\n")
                f.write("\n")

    print(f"[arbiter] Report saved: {report_path}")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="THE ARBITER \u2014 Quality Audit Agent")
    parser.add_argument("--audit-all", action="store_true", help="Run full local audit")
    parser.add_argument("--file", type=str, help="AI-audit a specific file")
    parser.add_argument("--text", type=str, help="Audit all eras for a text")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  THE ARBITER \u2014 Quality Audit")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    if args.audit_all:
        print("[arbiter] Running full local audit...")
        findings = run_local_audit()
        report = generate_report(findings, "full_audit")
        print(f"\n  Found {len(findings)} issues.")
        critical = sum(1 for f in findings if f["level"] == "CRITICAL")
        if critical > 0:
            print(f"  [!] {critical} CRITICAL issues require attention!")
        return findings

    elif args.file:
        print(f"[arbiter] AI audit of: {args.file}")
        findings, _usage = run_ai_audit(args.file)
        report = generate_report(findings, "ai_audit")
        return findings

    else:
        print("Usage:")
        print("  python agents/arbiter.py --audit-all        # Full local audit")
        print("  python agents/arbiter.py --file <path>      # AI audit one file")
        sys.exit(1)


if __name__ == "__main__":
    main()
