"""
review_content.py -- Council Review Pipeline

Runs the 5 council agents to review specified texts:
  Phase 1 (Local):  Structural checks (free, no API)
  Phase 2 (AI):     Deep theological + accuracy review (~$0.75)
  Phase 3 (AI):     Student readability review (~$0.15, --full only)
  Phase 4 (Report): Compiled markdown report

Usage:
    python agents/review_content.py --texts canon_scripture church_history zionism_israel
    python agents/review_content.py --all-new --full
    python agents/review_content.py --texts canon_scripture --local-only
    python agents/review_content.py --texts X --phase 2
"""
import os
import sys
import json
import argparse
import time
import subprocess
import importlib.util
from datetime import datetime

# Windows UTF-8 fix
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Add project root to path
AGENTS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(AGENTS_DIR)
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, AGENTS_DIR)

from config import (REPORTS_DIR, MANIFEST_PATH, DATA_DIR,
                    SONNET_INPUT_COST, SONNET_OUTPUT_COST)


# ============================================================================
#  Utility helpers
# ============================================================================

def banner(text, char="=", width=68):
    """Print a bordered banner line."""
    border = char * width
    print(f"\n{border}")
    print(f"  {text}")
    print(border)


def phase_header(num, title):
    """Print a phase header with box-drawing characters."""
    print(f"\n  {'='*60}")
    print(f"  Phase {num}: {title}")
    print(f"  {'='*60}")


def progress(current, total, label):
    """Print a progress indicator."""
    pct = int(current / total * 100) if total else 0
    bar_len = 30
    filled = int(bar_len * current / total) if total else 0
    bar = "#" * filled + "-" * (bar_len - filled)
    print(f"    [{bar}] {current}/{total} ({pct}%) {label}")


def cost_estimate(input_tokens, output_tokens):
    """Calculate estimated API cost from token counts."""
    input_cost = (input_tokens / 1_000_000) * SONNET_INPUT_COST
    output_cost = (output_tokens / 1_000_000) * SONNET_OUTPUT_COST
    return input_cost + output_cost


def load_manifest():
    """Load the project manifest."""
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_module(name, path):
    """Dynamically load a Python module from file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ============================================================================
#  Text detection and resolution
# ============================================================================

def detect_new_texts():
    """Auto-detect recently added texts by scanning git log for new era files."""
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "--name-only", "-10"],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )
        new_dirs = set()
        for line in result.stdout.splitlines():
            if line.startswith("data/") and "/era_" in line and line.endswith(".py"):
                parts = line.split("/")
                if len(parts) >= 3:
                    new_dirs.add(parts[1])
        # Cross-reference with manifest
        manifest = load_manifest()
        valid = []
        for t in manifest["texts"]:
            dd = t.get("data_dir", t["id"])
            if dd in new_dirs:
                valid.append(t["id"])
        if valid:
            print(f"  Auto-detected {len(valid)} text(s) from recent commits:")
            for tid in valid:
                print(f"    - {tid}")
        else:
            print("  No new texts detected in recent git history.")
        return valid
    except Exception as e:
        print(f"  [!] Git detection failed: {e}")
        return []


def resolve_text_names(text_ids, manifest):
    """Return a dict mapping text_id -> display name."""
    names = {}
    for t in manifest.get("texts", []):
        if t["id"] in text_ids:
            names[t["id"]] = t.get("name", t["id"])
    return names


def resolve_era_files(text_ids, manifest):
    """Return list of (text_id, era_id, data_file, file_path) for target texts."""
    results = []
    for era in manifest.get("eras", []):
        if era.get("text") not in text_ids:
            continue
        if era.get("content_type") == "html_fragment":
            continue  # Skip HTML-fragment eras
        text_id = era["text"]
        data_file = era.get("data_file", "")
        if not data_file:
            continue
        text_def = next((t for t in manifest["texts"] if t["id"] == text_id), {})
        data_dir = text_def.get("data_dir", text_id)
        file_path = os.path.join(DATA_DIR, data_dir, f"{data_file}.py")
        if not os.path.exists(file_path):
            file_path = os.path.join(DATA_DIR, f"{data_file}.py")
        results.append((text_id, era.get("id", ""), data_file, file_path))
    return results


# ============================================================================
#  Phase 1 -- Structural checks (no API)
# ============================================================================

def run_phase1(text_ids, manifest):
    """Phase 1: Local structural checks. Returns a findings dict."""
    phase_header(1, "STRUCTURAL CHECKS (local, no API)")
    results = {
        "arbiter_findings": [],
        "qa_issues": [],
        "text_stats": {},
    }

    era_files = resolve_era_files(text_ids, manifest)
    target_era_ids = {ef[1] for ef in era_files}
    text_names = resolve_text_names(text_ids, manifest)

    # --- 1a. Arbiter local audit (filter to target eras) ---
    print("\n  [1a] Running Arbiter local audit...")
    try:
        from arbiter import run_local_audit
        all_findings = run_local_audit()
        # Filter to target eras only
        filtered = [f for f in all_findings if f.get("era") in target_era_ids]
        results["arbiter_findings"] = filtered
        crit = sum(1 for f in filtered if f.get("level") == "CRITICAL")
        warn = sum(1 for f in filtered if f.get("level") == "WARNING")
        info = sum(1 for f in filtered if f.get("level") == "INFO")
        print(f"       Arbiter findings for target texts: {len(filtered)}")
        print(f"       CRITICAL: {crit}  |  WARNING: {warn}  |  INFO: {info}")
    except Exception as e:
        print(f"       [!] Arbiter local audit error: {e}")

    # --- 1b. Verify era files exist ---
    print("\n  [1b] Verifying era data files...")
    missing_files = []
    for text_id, era_id, data_file, file_path in era_files:
        if not os.path.exists(file_path):
            missing_files.append((text_id, era_id, data_file, file_path))
            results["qa_issues"].append(
                f"MISSING FILE: {data_file}.py (era: {era_id}, text: {text_id})"
            )
    if missing_files:
        for _, era_id, data_file, _ in missing_files:
            print(f"       [X] Missing: {data_file}.py (era: {era_id})")
    else:
        print(f"       [OK] All {len(era_files)} era files found on disk.")

    # --- 1c. Check info.py existence ---
    print("\n  [1c] Checking info.py files...")
    for text_id in text_ids:
        text_def = next((t for t in manifest["texts"] if t["id"] == text_id), None)
        if not text_def:
            results["qa_issues"].append(f"TEXT NOT IN MANIFEST: {text_id}")
            print(f"       [X] {text_id}: not found in manifest!")
            continue
        data_dir = text_def.get("data_dir", text_id)
        info_path = os.path.join(DATA_DIR, data_dir, "info.py")
        if os.path.exists(info_path):
            print(f"       [OK] {data_dir}/info.py")
        else:
            print(f"       [X]  {data_dir}/info.py -- MISSING")
            results["qa_issues"].append(f"MISSING INFO: {data_dir}/info.py")

    # --- 1d. Count chapters, sections, cross-refs, hebrew_terms ---
    print("\n  [1d] Counting content depth per text...")
    print(f"\n       {'Text':<24} {'Eras':>5} {'Chap':>6} {'Sect':>6} {'XRefs':>7} {'Terms':>7}")
    print(f"       {'-'*22}  {'-'*5} {'-'*6} {'-'*6} {'-'*7} {'-'*7}")

    for text_id in text_ids:
        text_eras = [(tid, eid, df, fp) for tid, eid, df, fp in era_files if tid == text_id]
        total_chapters = 0
        total_sections = 0
        total_xrefs = 0
        total_terms = 0

        for _, era_id, data_file, file_path in text_eras:
            if not os.path.exists(file_path):
                continue
            try:
                mod = load_module(data_file, file_path)
                chapters = getattr(mod, "CHAPTERS", [])
                for ch in chapters:
                    total_chapters += 1
                    total_sections += len(ch.get("sections", []))
                    xrefs = ch.get("cross_refs", [])
                    total_xrefs += len(xrefs) if isinstance(xrefs, list) else 0
                    terms = ch.get("hebrew_terms", [])
                    total_terms += len(terms) if isinstance(terms, list) else 0
            except Exception as e:
                results["qa_issues"].append(
                    f"LOAD ERROR: {data_file}.py -- {e}"
                )

        display_name = text_names.get(text_id, text_id)[:24]
        results["text_stats"][text_id] = {
            "name": text_names.get(text_id, text_id),
            "eras": len(text_eras),
            "chapters": total_chapters,
            "sections": total_sections,
            "cross_refs": total_xrefs,
            "hebrew_terms": total_terms,
        }
        print(f"       {display_name:<24} {len(text_eras):>5} {total_chapters:>6} "
              f"{total_sections:>6} {total_xrefs:>7} {total_terms:>7}")

    # --- 1e. Lector term audit (filtered) ---
    print("\n  [1e] Checking glossary term references...")
    try:
        from lector import audit_term_references
        all_term_findings, unused_terms = audit_term_references()
        # Filter to target texts
        filtered_terms = [f for f in all_term_findings if f.get("text") in text_ids]
        if filtered_terms:
            print(f"       [!] {len(filtered_terms)} missing glossary entries for target texts")
            for tf in filtered_terms[:5]:
                print(f"           - '{tf['term']}' in {tf['chapter']} ({tf['text']})")
            if len(filtered_terms) > 5:
                print(f"           ... and {len(filtered_terms) - 5} more")
        else:
            print(f"       [OK] All glossary references resolve.")
        results["lector_term_findings"] = filtered_terms
    except Exception as e:
        print(f"       [!] Lector term audit error: {e}")
        results["lector_term_findings"] = []

    return results


# ============================================================================
#  Phase 2 -- AI Deep Review
# ============================================================================

def run_phase2(text_ids, manifest, era_files):
    """Phase 2: AI-powered theological and accuracy review. Returns findings + usage."""
    phase_header(2, "AI DEEP REVIEW (Arbiter + Reader)")
    results = {
        "arbiter_ai_findings": [],
        "theologian_issues": [],
        "total_tokens": {"input": 0, "output": 0},
        "api_calls": 0,
    }

    text_names = resolve_text_names(text_ids, manifest)

    # --- 2a. Arbiter AI audit on each era file ---
    print("\n  [2a] Arbiter AI audit on target era files...")
    target_eras = [(tid, eid, df, fp) for tid, eid, df, fp in era_files
                   if os.path.exists(fp)]

    if not target_eras:
        print("       No era files to audit.")
    else:
        try:
            from arbiter import run_ai_audit
        except ImportError as e:
            print(f"       [!] Cannot import arbiter.run_ai_audit: {e}")
            run_ai_audit = None

        if run_ai_audit:
            for i, (text_id, era_id, data_file, file_path) in enumerate(target_eras):
                label = f"{text_names.get(text_id, text_id)} / {era_id}"
                print(f"       [{i+1}/{len(target_eras)}] Auditing: {label}...", end=" ", flush=True)
                try:
                    findings, usage = run_ai_audit(file_path)
                    results["arbiter_ai_findings"].extend(findings)
                    results["api_calls"] += 1
                    if usage:
                        results["total_tokens"]["input"] += getattr(usage, "input_tokens", 0)
                        results["total_tokens"]["output"] += getattr(usage, "output_tokens", 0)
                    crit = sum(1 for f in findings if f.get("level") == "CRITICAL")
                    warn = sum(1 for f in findings if f.get("level") == "WARNING")
                    print(f"done ({crit}C / {warn}W / {len(findings) - crit - warn}I)")
                except Exception as e:
                    print(f"ERROR: {e}")
                    results["arbiter_ai_findings"].append({
                        "level": "INFO",
                        "location": file_path,
                        "rule": "api_error",
                        "message": f"AI audit failed: {e}"
                    })

                # Rate limit between API calls
                if i < len(target_eras) - 1:
                    time.sleep(2)

    # --- 2b. Reader theologian mode ---
    print("\n  [2b] Reader theologian review (all eras)...")
    try:
        from reader import run_theologian_mode
        issues, usage = run_theologian_mode(
            text_ids, manifest, all_eras=True, return_data=True
        )
        results["theologian_issues"] = issues
        results["api_calls"] += len(issues)  # Approximate: 1 call per era reviewed
        results["total_tokens"]["input"] += usage.get("input_tokens", 0)
        results["total_tokens"]["output"] += usage.get("output_tokens", 0)
        print(f"       Theologian review complete: {len(issues)} era(s) reviewed.")
    except Exception as e:
        print(f"       [!] Theologian mode error: {e}")

    # Summary
    total_cost = cost_estimate(
        results["total_tokens"]["input"],
        results["total_tokens"]["output"]
    )
    print(f"\n  Phase 2 Summary:")
    print(f"    API calls:     {results['api_calls']}")
    print(f"    Input tokens:  {results['total_tokens']['input']:,}")
    print(f"    Output tokens: {results['total_tokens']['output']:,}")
    print(f"    Est. cost:     ${total_cost:.4f}")

    return results


# ============================================================================
#  Phase 3 -- Readability (--full only)
# ============================================================================

def run_phase3(text_ids, manifest):
    """Phase 3: Student readability review. Returns feedback + usage."""
    phase_header(3, "READABILITY REVIEW (Reader student mode)")
    results = {
        "student_feedback": [],
        "total_tokens": {"input": 0, "output": 0},
        "api_calls": 0,
    }

    text_names = resolve_text_names(text_ids, manifest)

    try:
        from reader import run_student_mode
    except ImportError as e:
        print(f"  [!] Cannot import reader.run_student_mode: {e}")
        return results

    for i, text_id in enumerate(text_ids):
        label = text_names.get(text_id, text_id)
        print(f"\n  [{i+1}/{len(text_ids)}] Student review: {label}")
        try:
            run_student_mode(text_id, manifest)
            results["student_feedback"].append(text_id)
            results["api_calls"] += 1
        except Exception as e:
            print(f"  [!] Student mode error for {text_id}: {e}")

        # Rate limit between texts
        if i < len(text_ids) - 1:
            time.sleep(2)

    print(f"\n  Phase 3 Summary:")
    print(f"    Texts reviewed: {len(results['student_feedback'])}")
    print(f"    API calls:      {results['api_calls']}")

    return results


# ============================================================================
#  Phase 4 -- Report compilation
# ============================================================================

def compile_report(text_ids, manifest, phase1, phase2=None, phase3=None,
                   elapsed_seconds=0.0):
    """Phase 4: Compile all findings into a markdown report."""
    phase_header(4, "COMPILING REPORT")

    os.makedirs(REPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"council_review_{timestamp}.md"
    report_path = os.path.join(REPORTS_DIR, report_name)

    text_names = resolve_text_names(text_ids, manifest)
    texts_display = ", ".join(text_names.get(t, t) for t in text_ids)

    # Aggregate counts
    p1_arbiter_count = len(phase1.get("arbiter_findings", []))
    p1_qa_count = len(phase1.get("qa_issues", []))
    p1_lector_count = len(phase1.get("lector_term_findings", []))
    p1_total = p1_arbiter_count + p1_qa_count + p1_lector_count

    p2_arbiter_ai = len(phase2.get("arbiter_ai_findings", [])) if phase2 else 0
    p2_theologian = len(phase2.get("theologian_issues", [])) if phase2 else 0
    p2_tokens_in = phase2["total_tokens"]["input"] if phase2 else 0
    p2_tokens_out = phase2["total_tokens"]["output"] if phase2 else 0
    p2_calls = phase2.get("api_calls", 0) if phase2 else 0
    p2_cost = cost_estimate(p2_tokens_in, p2_tokens_out)

    p3_reviewed = len(phase3.get("student_feedback", [])) if phase3 else 0
    p3_calls = phase3.get("api_calls", 0) if phase3 else 0

    total_api_calls = p2_calls + p3_calls
    total_cost = p2_cost  # Phase 3 cost is hard to separate (reader writes its own report)

    with open(report_path, "w", encoding="utf-8") as f:
        # Title
        f.write(f"# Council Review Pipeline Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Texts Reviewed:** {texts_display}\n")
        f.write(f"**Duration:** {elapsed_seconds / 60:.1f} minutes\n\n")

        # Overview table
        f.write(f"## Overview\n\n")
        f.write(f"| Phase | Agent | Findings | API Calls | Tokens | Est. Cost |\n")
        f.write(f"|-------|-------|----------|-----------|--------|----------|\n")
        f.write(f"| 1 - Structural | Arbiter (local) | {p1_arbiter_count} | 0 | 0 | $0.00 |\n")
        f.write(f"| 1 - Structural | QA checks | {p1_qa_count} | 0 | 0 | $0.00 |\n")
        f.write(f"| 1 - Structural | Lector (terms) | {p1_lector_count} | 0 | 0 | $0.00 |\n")
        if phase2:
            f.write(f"| 2 - AI Deep | Arbiter (AI) | {p2_arbiter_ai} | "
                    f"{p2_calls - len(phase2.get('theologian_issues', []))} | "
                    f"-- | -- |\n")
            f.write(f"| 2 - AI Deep | Reader (theologian) | {p2_theologian} era(s) | "
                    f"{len(phase2.get('theologian_issues', []))} | "
                    f"{p2_tokens_in + p2_tokens_out:,} | ${p2_cost:.4f} |\n")
        if phase3:
            f.write(f"| 3 - Readability | Reader (student) | {p3_reviewed} text(s) | "
                    f"{p3_calls} | -- | -- |\n")
        f.write(f"| **Total** | | **{p1_total + p2_arbiter_ai}+** | "
                f"**{total_api_calls}** | **{p2_tokens_in + p2_tokens_out:,}** | "
                f"**${total_cost:.4f}** |\n\n")

        # Phase 1 details
        f.write(f"---\n\n## Phase 1: Structural Checks\n\n")

        # Content depth table
        f.write(f"### Content Depth\n\n")
        f.write(f"| Text | Eras | Chapters | Sections | Cross-Refs | Hebrew Terms |\n")
        f.write(f"|------|------|----------|----------|------------|-------------|\n")
        for text_id in text_ids:
            stats = phase1.get("text_stats", {}).get(text_id, {})
            f.write(f"| {stats.get('name', text_id)} | {stats.get('eras', 0)} | "
                    f"{stats.get('chapters', 0)} | {stats.get('sections', 0)} | "
                    f"{stats.get('cross_refs', 0)} | {stats.get('hebrew_terms', 0)} |\n")
        f.write("\n")

        # Arbiter local findings
        arbiter_findings = phase1.get("arbiter_findings", [])
        if arbiter_findings:
            f.write(f"### Arbiter Local Findings ({len(arbiter_findings)})\n\n")
            for finding in arbiter_findings:
                level = finding.get("level", "?")
                ch = finding.get("chapter", "?")
                era = finding.get("era", "?")
                rule = finding.get("rule", "?")
                msg = finding.get("message", "")
                f.write(f"- **[{level}]** `{ch}` (era: {era}) [{rule}] -- {msg}\n")
            f.write("\n")
        else:
            f.write(f"### Arbiter Local Findings\n\nNo issues found for target texts.\n\n")

        # QA issues
        qa_issues = phase1.get("qa_issues", [])
        if qa_issues:
            f.write(f"### QA Issues ({len(qa_issues)})\n\n")
            for issue in qa_issues:
                f.write(f"- {issue}\n")
            f.write("\n")

        # Lector term findings
        lector_findings = phase1.get("lector_term_findings", [])
        if lector_findings:
            f.write(f"### Missing Glossary Terms ({len(lector_findings)})\n\n")
            f.write(f"| Term Key | Chapter | Era | Text |\n")
            f.write(f"|----------|---------|-----|------|\n")
            for tf in lector_findings:
                f.write(f"| `{tf['term']}` | {tf['chapter']} | {tf['era']} | {tf['text']} |\n")
            f.write("\n")

        # Phase 2 details
        if phase2:
            f.write(f"---\n\n## Phase 2: AI Deep Review\n\n")

            ai_findings = phase2.get("arbiter_ai_findings", [])
            if ai_findings:
                f.write(f"### Arbiter AI Findings ({len(ai_findings)})\n\n")
                for finding in ai_findings:
                    level = finding.get("level", "?")
                    loc = finding.get("location", finding.get("chapter", "?"))
                    rule = finding.get("rule", "?")
                    msg = finding.get("message", "")
                    f.write(f"- **[{level}]** `{loc}` [{rule}] -- {msg}\n")
                f.write("\n")

            theo_issues = phase2.get("theologian_issues", [])
            if theo_issues:
                f.write(f"### Theologian Review ({len(theo_issues)} era(s))\n\n")
                for issue_text in theo_issues:
                    f.write(f"{issue_text}\n\n")

        # Phase 3 details
        if phase3 and phase3.get("student_feedback"):
            f.write(f"---\n\n## Phase 3: Readability Review\n\n")
            f.write(f"Student mode reports were generated for "
                    f"{len(phase3['student_feedback'])} text(s).\n")
            f.write(f"See individual `reader_student_*.md` files in `agents/reports/` "
                    f"for detailed feedback.\n\n")
            for text_id in phase3["student_feedback"]:
                name = text_names.get(text_id, text_id)
                f.write(f"- {name}\n")
            f.write("\n")

        # Footer
        f.write(f"---\n\n*Generated by Council Review Pipeline "
                f"({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})*\n")

    print(f"\n  Report saved: {report_path}")
    print(f"  Size: {os.path.getsize(report_path) / 1024:.1f} KB")
    return report_path


# ============================================================================
#  Main entry point
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Council Review Pipeline -- orchestrated review of new/updated content",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python agents/review_content.py --texts canon_scripture church_history
  python agents/review_content.py --all-new --full
  python agents/review_content.py --texts genesis --local-only
  python agents/review_content.py --texts canon_scripture --phase 2
"""
    )
    parser.add_argument("--texts", nargs="+", metavar="TEXT_ID",
                        help="One or more text IDs to review")
    parser.add_argument("--all-new", action="store_true",
                        help="Auto-detect recently added texts from git log")
    parser.add_argument("--local-only", action="store_true",
                        help="Phase 1 only -- structural checks, no API calls")
    parser.add_argument("--full", action="store_true",
                        help="All phases including Phase 3 readability (~extra $0.15)")
    parser.add_argument("--phase", type=int, choices=[1, 2, 3, 4],
                        help="Run only a specific phase (1-4)")
    args = parser.parse_args()

    start_time = time.time()

    # ── Banner ──
    banner("COUNCIL REVIEW PIPELINE", char="=")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Ancient Texts Study App")
    print(f"{'=' * 68}")

    # ── Resolve target texts ──
    if args.all_new:
        print("\n  Detecting new texts from git history...")
        text_ids = detect_new_texts()
        if not text_ids:
            print("\n  [!] No new texts detected. Use --texts to specify manually.")
            sys.exit(1)
    elif args.texts:
        text_ids = args.texts
    else:
        print("\n  ERROR: Specify --texts or --all-new")
        parser.print_help()
        sys.exit(1)

    manifest = load_manifest()

    # Validate text IDs against manifest
    valid_text_ids = {t["id"] for t in manifest.get("texts", [])}
    invalid = [t for t in text_ids if t not in valid_text_ids]
    if invalid:
        print(f"\n  [!] Unknown text IDs (not in manifest): {', '.join(invalid)}")
        print(f"      Available: {', '.join(sorted(valid_text_ids))}")
        sys.exit(1)

    text_names = resolve_text_names(text_ids, manifest)
    era_files = resolve_era_files(text_ids, manifest)

    print(f"\n  Target texts ({len(text_ids)}):")
    for tid in text_ids:
        era_count = sum(1 for ef in era_files if ef[0] == tid)
        print(f"    - {text_names.get(tid, tid)} ({era_count} era(s))")

    # Determine which phases to run
    if args.phase:
        run_phases = {args.phase}
    elif args.local_only:
        run_phases = {1, 4}
    elif args.full:
        run_phases = {1, 2, 3, 4}
    else:
        run_phases = {1, 2, 4}

    mode_label = "local-only" if args.local_only else ("full" if args.full else "standard")
    print(f"\n  Mode: {mode_label}")
    print(f"  Phases: {', '.join(str(p) for p in sorted(run_phases))}")

    if 2 in run_phases or 3 in run_phases:
        est = "$0.75" if 3 not in run_phases else "$0.90+"
        print(f"  Estimated API cost: ~{est}")

    # ── Execute phases ──
    phase1_results = None
    phase2_results = None
    phase3_results = None

    # Phase 1: Structural
    if 1 in run_phases:
        phase1_results = run_phase1(text_ids, manifest)
    else:
        # Minimal phase1 for the report
        phase1_results = {
            "arbiter_findings": [],
            "qa_issues": [],
            "text_stats": {},
            "lector_term_findings": [],
        }

    # Phase 2: AI Deep Review
    if 2 in run_phases:
        phase2_results = run_phase2(text_ids, manifest, era_files)

    # Phase 3: Readability
    if 3 in run_phases:
        phase3_results = run_phase3(text_ids, manifest)

    # Phase 4: Report
    elapsed = time.time() - start_time
    if 4 in run_phases:
        report_path = compile_report(
            text_ids, manifest,
            phase1_results,
            phase2_results,
            phase3_results,
            elapsed_seconds=elapsed,
        )
    else:
        report_path = None

    # ── Final summary ──
    elapsed = time.time() - start_time
    banner("REVIEW COMPLETE", char="=")
    print(f"  Duration:   {elapsed / 60:.1f} minutes ({elapsed:.0f}s)")
    print(f"  Texts:      {len(text_ids)}")
    print(f"  Era files:  {len(era_files)}")

    if phase1_results:
        p1_total = (len(phase1_results.get("arbiter_findings", []))
                    + len(phase1_results.get("qa_issues", []))
                    + len(phase1_results.get("lector_term_findings", [])))
        print(f"  Phase 1:    {p1_total} finding(s)")

    if phase2_results:
        p2_total = (len(phase2_results.get("arbiter_ai_findings", []))
                    + len(phase2_results.get("theologian_issues", [])))
        p2_cost = cost_estimate(
            phase2_results["total_tokens"]["input"],
            phase2_results["total_tokens"]["output"]
        )
        print(f"  Phase 2:    {p2_total} finding(s), "
              f"{phase2_results['api_calls']} API calls, ${p2_cost:.4f}")

    if phase3_results:
        print(f"  Phase 3:    {len(phase3_results.get('student_feedback', []))} text(s) reviewed")

    if report_path:
        print(f"  Report:     {report_path}")

    print(f"{'=' * 68}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
