"""
THE ARCHITECT — Builder, Organizer, Status Tracker

Runs builds, monitors structure, detects gaps, tracks progress,
and maintains the project status dashboard.

Usage:
    python agents/architect.py --build
    python agents/architect.py --status
    python agents/architect.py --check
"""
import os
import sys
import json
import argparse
import subprocess
import importlib.util
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.config import (
    DATA_DIR, MANIFEST_PATH, BUILD_SCRIPT, OUTPUT_DIR,
    REPORTS_DIR, PROJECT_ROOT
)


def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_build():
    """Execute build.py and report results."""
    print("[architect] Running build...")
    result = subprocess.run(
        [sys.executable, BUILD_SCRIPT],
        capture_output=True, text=True, cwd=PROJECT_ROOT
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"BUILD FAILED:\n{result.stderr}")
        return False
    return True


def check_structure():
    """Validate project structure — find orphans and missing files."""
    manifest = load_manifest()
    findings = []

    # Check all manifest eras have data
    for era in manifest["eras"]:
        if era.get("content_type") == "html_fragment":
            # Check HTML fragments exist
            fragments = era.get("fragments", [])
            for frag in fragments:
                fpath = os.path.join(DATA_DIR, "heavenly_court", "chapters", frag["file"])
                if not os.path.exists(fpath):
                    findings.append(f"MISSING: {frag['file']} (era: {era['id']})")
        else:
            data_file = era.get("data_file")
            if not data_file:
                continue
            text_id = era.get("text")
            text_def = next((t for t in manifest["texts"] if t["id"] == text_id), None)
            if not text_def:
                findings.append(f"ORPHAN ERA: {era['id']} references unknown text '{text_id}'")
                continue

            data_dir = text_def.get("data_dir", text_id)
            path = os.path.join(DATA_DIR, data_dir, data_file + ".py")
            if not os.path.exists(path):
                path = os.path.join(DATA_DIR, data_file + ".py")
            if not os.path.exists(path):
                findings.append(f"MISSING DATA: {data_file}.py (era: {era['id']})")

    # Check for orphan .py files not referenced by any era
    referenced_files = set()
    for era in manifest["eras"]:
        df = era.get("data_file")
        if df:
            referenced_files.add(df + ".py")

    for root, dirs, files in os.walk(DATA_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f.startswith("era_") and f.endswith(".py"):
                if f not in referenced_files:
                    relpath = os.path.relpath(os.path.join(root, f), DATA_DIR)
                    findings.append(f"ORPHAN FILE: {relpath} (not in manifest)")

    # Check info.py files
    for text_def in manifest["texts"]:
        data_dir = text_def.get("data_dir", text_def["id"])
        info_path = os.path.join(DATA_DIR, data_dir, "info.py")
        if not os.path.exists(info_path):
            findings.append(f"MISSING INFO: {data_dir}/info.py (text: {text_def['name']})")

    return findings


def generate_status():
    """Generate a comprehensive project status report."""
    manifest = load_manifest()

    # Count chapters per text
    text_stats = {}
    for text_def in manifest["texts"]:
        text_id = text_def["id"]
        eras = [e for e in manifest["eras"] if e.get("text") == text_id]
        total_chapters = 0
        total_inserts = 0
        has_data = 0

        for era in eras:
            if era.get("content_type") == "html_fragment":
                frags = era.get("fragments", [])
                total_chapters += len(frags)
                # Check if files exist
                for frag in frags:
                    fpath = os.path.join(DATA_DIR, "heavenly_court", "chapters", frag["file"])
                    if os.path.exists(fpath):
                        has_data += 1
            else:
                data_file = era.get("data_file")
                if not data_file:
                    continue
                data_dir = text_def.get("data_dir", text_id)
                path = os.path.join(DATA_DIR, data_dir, data_file + ".py")
                if not os.path.exists(path):
                    path = os.path.join(DATA_DIR, data_file + ".py")
                if os.path.exists(path):
                    try:
                        mod = load_module(data_file, path)
                        chapters = getattr(mod, "CHAPTERS", [])
                        ch_count = sum(1 for c in chapters if c.get("type") == "chapter")
                        ins_count = sum(1 for c in chapters if c.get("type") == "historical_insert")
                        total_chapters += ch_count
                        total_inserts += ins_count
                        has_data += 1
                    except Exception:
                        pass

        # Check info.py
        data_dir = text_def.get("data_dir", text_id)
        has_info = os.path.exists(os.path.join(DATA_DIR, data_dir, "info.py"))

        text_stats[text_id] = {
            "name": text_def["name"],
            "category": text_def["category"],
            "eras": len(eras),
            "eras_with_data": has_data,
            "chapters": total_chapters,
            "inserts": total_inserts,
            "has_info": has_info,
            "content_type": text_def.get("content_type", "python_data")
        }

    # Check output
    output_exists = os.path.exists(os.path.join(OUTPUT_DIR, "AncientTextsStudy.html"))
    if output_exists:
        output_size = os.path.getsize(os.path.join(OUTPUT_DIR, "AncientTextsStudy.html"))
    else:
        output_size = 0

    # Glossary count
    gpath = os.path.join(DATA_DIR, "glossary.py")
    glossary_count = 0
    if os.path.exists(gpath):
        try:
            mod = load_module("glossary", gpath)
            glossary_count = len(getattr(mod, "GLOSSARY", {}))
        except Exception:
            pass

    return text_stats, output_exists, output_size, glossary_count


def print_status():
    """Print formatted status report."""
    text_stats, output_exists, output_size, glossary_count = generate_status()

    print(f"\n{'='*70}")
    print(f"  THE ARCHITECT \u2014 Project Status")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}\n")

    # Output status
    if output_exists:
        print(f"  Build: [OK] AncientTextsStudy.html ({output_size/1024:.1f} KB)")
    else:
        print(f"  Build: [X] No output file (run --build)")

    print(f"  Glossary: {glossary_count} terms")
    print()

    # Text table
    total_ch = 0
    print(f"  {'Text':<28} {'Category':<14} {'Eras':>5} {'Chap':>6} {'Info':>6} {'Type':<12}")
    print(f"  {'-'*26}  {'-'*12}  {'-'*5} {'-'*6} {'-'*6} {'-'*12}")

    for tid, stats in text_stats.items():
        info_mark = "[OK]" if stats["has_info"] else "[X]"
        content_type = "fragment" if stats["content_type"] == "html_fragment" else "data"
        print(f"  {stats['name']:<28} {stats['category']:<14} {stats['eras']:>5} {stats['chapters']:>6} {info_mark:>6} {content_type:<12}")
        total_ch += stats["chapters"]

    print(f"\n  Total: {len(text_stats)} texts, {sum(s['eras'] for s in text_stats.values())} eras, {total_ch} chapters")

    # Structure check
    findings = check_structure()
    if findings:
        print(f"\n  [!] Structure Issues ({len(findings)}):")
        for f in findings[:10]:
            print(f"    - {f}")
        if len(findings) > 10:
            print(f"    ... and {len(findings) - 10} more")
    else:
        print(f"\n  [OK] No structural issues found")

    print(f"\n{'='*70}")


def save_status_report():
    """Save status report to markdown file."""
    text_stats, output_exists, output_size, glossary_count = generate_status()
    findings = check_structure()

    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, f"status_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# THE ARCHITECT \u2014 Project Status\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write(f"## Build\n\n")
        if output_exists:
            f.write(f"- Output: AncientTextsStudy.html ({output_size/1024:.1f} KB)\n")
        else:
            f.write(f"- Output: NOT BUILT\n")
        f.write(f"- Glossary: {glossary_count} terms\n\n")

        f.write(f"## Texts\n\n")
        f.write(f"| Text | Category | Eras | Chapters | Info | Type |\n")
        f.write(f"|------|----------|------|----------|------|------|\n")
        for tid, s in text_stats.items():
            info_mark = "[OK]" if s["has_info"] else "[X]"
            f.write(f"| {s['name']} | {s['category']} | {s['eras']} | {s['chapters']} | {info_mark} | {s['content_type']} |\n")

        if findings:
            f.write(f"\n## Issues ({len(findings)})\n\n")
            for finding in findings:
                f.write(f"- {finding}\n")

    print(f"[architect] Status report: {report_path}")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="THE ARCHITECT \u2014 Builder & Status Tracker")
    parser.add_argument("--build", action="store_true", help="Run build.py")
    parser.add_argument("--status", action="store_true", help="Print project status")
    parser.add_argument("--check", action="store_true", help="Check structure for issues")
    parser.add_argument("--report", action="store_true", help="Save status report to file")
    args = parser.parse_args()

    if args.build:
        success = run_build()
        if success:
            print_status()
        sys.exit(0 if success else 1)

    elif args.status:
        print_status()

    elif args.check:
        findings = check_structure()
        if findings:
            print(f"\nFound {len(findings)} issues:")
            for f in findings:
                print(f"  - {f}")
        else:
            print("[OK] No issues found")

    elif args.report:
        save_status_report()
        print_status()

    else:
        print("Usage:")
        print("  python agents/architect.py --build    # Build the app")
        print("  python agents/architect.py --status   # Show project status")
        print("  python agents/architect.py --check    # Check for structural issues")
        print("  python agents/architect.py --report   # Save status report")


if __name__ == "__main__":
    main()
