#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════
Agent Crawl — Orchestrator
═══════════════════════════════════════════════════════════════
Builds desktop + mobile, verifies outputs, and prints
instructions for Claude to execute each test suite.

Usage:
    python tests/crawl/run_crawl.py              # Full crawl prep
    python tests/crawl/run_crawl.py --build      # Build only
    python tests/crawl/run_crawl.py --report     # Generate report from results
    python tests/crawl/run_crawl.py --status     # Show results summary
"""

import os
import sys
import json
import subprocess
import argparse
from datetime import datetime

# Add project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.dirname(__file__))

from config import (
    BUILD_SCRIPT, BUILD_MOBILE_SCRIPT, DESKTOP_HTML, MOBILE_DIR, MOBILE_INDEX,
    OUTPUT_DIR, SUITES_DIR, PROMPTS_DIR, RESULTS_DIR, SUITE_ORDER,
    DESKTOP_PORT, MOBILE_PORT, DESKTOP_URL, MOBILE_URL
)


def build_targets():
    """Build desktop and mobile targets."""
    print("\n" + "=" * 60)
    print("  BUILDING TARGETS")
    print("=" * 60)

    # Desktop dev build
    print("\n[1/3] Building desktop (dev)...")
    result = subprocess.run(
        [sys.executable, BUILD_SCRIPT],
        cwd=PROJECT_ROOT,
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  FAILED: {result.stderr[:500]}")
        return False
    print(f"  OK — {os.path.basename(DESKTOP_HTML)}")

    # Desktop release build
    print("\n[2/3] Building desktop (release)...")
    result = subprocess.run(
        [sys.executable, BUILD_SCRIPT, '--release'],
        cwd=PROJECT_ROOT,
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  FAILED: {result.stderr[:500]}")
        return False
    print("  OK — Release build")

    # Mobile build
    print("\n[3/3] Building mobile PWA...")
    result = subprocess.run(
        [sys.executable, BUILD_MOBILE_SCRIPT],
        cwd=PROJECT_ROOT,
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  FAILED: {result.stderr[:500]}")
        return False
    print(f"  OK — {os.path.basename(MOBILE_DIR)}/")

    # Verify outputs
    print("\n  Verifying outputs...")
    checks = [
        (DESKTOP_HTML, "Desktop HTML"),
        (MOBILE_INDEX, "Mobile index.html"),
    ]
    all_ok = True
    for path, label in checks:
        if os.path.exists(path):
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"    {label}: {size_mb:.1f} MB")
        else:
            print(f"    {label}: MISSING!")
            all_ok = False

    return all_ok


def list_suites():
    """List all test suites and their test counts."""
    print("\n" + "=" * 60)
    print("  TEST SUITES")
    print("=" * 60)

    total_tests = 0
    for suite_name in SUITE_ORDER:
        suite_path = os.path.join(SUITES_DIR, f"{suite_name}.json")
        if os.path.exists(suite_path):
            with open(suite_path, 'r', encoding='utf-8') as f:
                suite = json.load(f)
            count = len(suite.get('tests', []))
            total_tests += count
            desc = suite.get('description', '')
            print(f"  {suite_name:25s}  {count:3d} tests  — {desc}")
        else:
            print(f"  {suite_name:25s}  MISSING!")

    print(f"\n  TOTAL: {total_tests} tests across {len(SUITE_ORDER)} suites")
    return total_tests


def print_crawl_instructions():
    """Print instructions for Claude to execute the crawl."""
    print("\n" + "=" * 60)
    print("  AGENT CRAWL INSTRUCTIONS")
    print("=" * 60)

    print(f"""
To execute the agent crawl, follow these steps in Claude:

1. START SERVERS
   - Desktop: Use preview_start with a launch.json config serving
     {os.path.relpath(OUTPUT_DIR, PROJECT_ROOT)} on port {DESKTOP_PORT}
   - Mobile: Serve {os.path.relpath(MOBILE_DIR, PROJECT_ROOT)} on port {MOBILE_PORT}

2. EXECUTE SUITES (in order)
   For each suite, launch a Task agent with:
   - The prompt from tests/crawl/prompts/agent_<suite>.md
   - The test definitions from tests/crawl/suites/<suite>.json
   - Server URLs: Desktop={DESKTOP_URL}, Mobile={MOBILE_URL}

   Suite execution order:
""")

    for i, suite_name in enumerate(SUITE_ORDER, 1):
        prompt_file = os.path.join(PROMPTS_DIR, f"agent_{suite_name[3:]}.md")
        suite_file = os.path.join(SUITES_DIR, f"{suite_name}.json")
        prompt_exists = os.path.exists(prompt_file)
        suite_exists = os.path.exists(suite_file)
        status = "OK" if (prompt_exists and suite_exists) else "MISSING FILES"
        print(f"   {i}. {suite_name} [{status}]")

    print(f"""
3. SAVE RESULTS
   Each agent should return JSON results.
   Save combined results to:
     tests/crawl/results/crawl_<timestamp>.json

4. GENERATE REPORT
   Run: python tests/crawl/report.py
   Or:  python tests/crawl/run_crawl.py --report
""")


def show_status():
    """Show summary of existing results."""
    print("\n" + "=" * 60)
    print("  CRAWL RESULTS")
    print("=" * 60)

    if not os.path.exists(RESULTS_DIR):
        print("\n  No results directory found.")
        return

    result_files = sorted([f for f in os.listdir(RESULTS_DIR) if f.endswith('.json')])
    if not result_files:
        print("\n  No result files found.")
        return

    for rf in result_files:
        filepath = os.path.join(RESULTS_DIR, rf)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            tests = data
        elif isinstance(data, dict):
            tests = data.get('tests', data.get('results', []))
        else:
            continue

        total = len(tests)
        passed = sum(1 for t in tests if t.get('status') == 'PASS')
        failed = sum(1 for t in tests if t.get('status') == 'FAIL')
        warned = sum(1 for t in tests if t.get('status') == 'WARN')

        print(f"\n  {rf}")
        print(f"    {passed}/{total} PASS | {failed} FAIL | {warned} WARN")

        if failed > 0:
            print("    Failures:")
            for t in tests:
                if t.get('status') == 'FAIL':
                    print(f"      {t.get('id', '?')} {t.get('name', '?')} — {t.get('error', t.get('notes', 'no details'))}")


def main():
    parser = argparse.ArgumentParser(description='Agent Crawl Orchestrator')
    parser.add_argument('--build', action='store_true', help='Build targets only')
    parser.add_argument('--report', action='store_true', help='Generate report from results')
    parser.add_argument('--status', action='store_true', help='Show results summary')
    args = parser.parse_args()

    if args.report:
        # Import and run report generator
        try:
            from report import generate_report
            generate_report()
        except ImportError:
            print("Error: report.py not found or has errors")
            sys.exit(1)
        return

    if args.status:
        show_status()
        return

    if args.build:
        success = build_targets()
        sys.exit(0 if success else 1)

    # Full flow: build + list + instructions
    print("\n" + "=" * 60)
    print("  ANCIENT TEXTS STUDY APP — AGENT CRAWL")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    success = build_targets()
    if not success:
        print("\n  BUILD FAILED — fix errors before running crawl")
        sys.exit(1)

    list_suites()
    print_crawl_instructions()


if __name__ == '__main__':
    main()
