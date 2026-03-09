#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════
Agent Crawl — Report Generator
═══════════════════════════════════════════════════════════════
Reads JSON result files from tests/crawl/results/ and generates:
  - Markdown report (.md)
  - HTML report (.html)
  - Console summary

Usage:
    python tests/crawl/report.py                     # Latest results
    python tests/crawl/report.py crawl_2026-03-09.json  # Specific file
"""

import os
import sys
import json
import html as html_mod
from datetime import datetime

RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')

SUITE_LABELS = {
    'smoke': '1. Smoke',
    'navigation': '2. Navigation',
    'overlays': '3. Overlays',
    'interlinear': '4. Interlinear',
    'search': '5. Search',
    'content': '6. Content',
    'mobile': '7. Mobile',
    'performance': '8. Performance',
}


def load_results(filename=None):
    """Load the latest or specified result file."""
    if filename:
        filepath = os.path.join(RESULTS_DIR, filename)
    else:
        # Find latest
        files = sorted([f for f in os.listdir(RESULTS_DIR) if f.endswith('.json')])
        if not files:
            print("No result files found in", RESULTS_DIR)
            sys.exit(1)
        filepath = os.path.join(RESULTS_DIR, files[-1])
        filename = files[-1]

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Normalize — could be a list of tests or a dict with metadata
    if isinstance(data, list):
        tests = data
        metadata = {}
    elif isinstance(data, dict):
        tests = data.get('tests', data.get('results', []))
        metadata = {k: v for k, v in data.items() if k not in ('tests', 'results')}
    else:
        tests = []
        metadata = {}

    return tests, metadata, filename


def compute_stats(tests):
    """Compute per-suite and overall statistics."""
    suites = {}
    for t in tests:
        suite = t.get('suite', 'unknown')
        if suite not in suites:
            suites[suite] = {'pass': 0, 'fail': 0, 'warn': 0, 'tests': []}
        status = t.get('status', 'UNKNOWN').upper()
        if status == 'PASS':
            suites[suite]['pass'] += 1
        elif status == 'FAIL':
            suites[suite]['fail'] += 1
        elif status == 'WARN':
            suites[suite]['warn'] += 1
        suites[suite]['tests'].append(t)

    total_pass = sum(s['pass'] for s in suites.values())
    total_fail = sum(s['fail'] for s in suites.values())
    total_warn = sum(s['warn'] for s in suites.values())
    total = len(tests)

    return suites, total, total_pass, total_fail, total_warn


def generate_console(tests, metadata):
    """Print console summary."""
    suites, total, total_pass, total_fail, total_warn = compute_stats(tests)
    pct = (total_pass / total * 100) if total > 0 else 0
    ts = metadata.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    print()
    print("=" * 55)
    print(f"  AGENT CRAWL REPORT — {ts}")
    print("=" * 55)
    print()
    print(f"  TOTAL: {total_pass}/{total} PASS ({pct:.1f}%) | {total_fail} FAIL | {total_warn} WARN")
    print()
    print(f"  {'Suite':<20s} {'Pass':>5s} {'Fail':>5s} {'Warn':>5s}")
    print(f"  {'-'*20} {'-'*5} {'-'*5} {'-'*5}")

    for suite_key in ['smoke', 'navigation', 'overlays', 'interlinear',
                      'search', 'content', 'mobile', 'performance']:
        label = SUITE_LABELS.get(suite_key, suite_key)
        s = suites.get(suite_key, {'pass': 0, 'fail': 0, 'warn': 0})
        print(f"  {label:<20s} {s['pass']:>5d} {s['fail']:>5d} {s['warn']:>5d}")

    # Failures
    failures = [t for t in tests if t.get('status', '').upper() == 'FAIL']
    if failures:
        print()
        print("  FAILURES:")
        for t in failures:
            tid = t.get('id', '?')
            name = t.get('name', '?')
            err = t.get('error', t.get('notes', 'no details'))
            print(f"    {tid:6s} {name} — {err}")

    # Warnings
    warnings = [t for t in tests if t.get('status', '').upper() == 'WARN']
    if warnings:
        print()
        print("  WARNINGS:")
        for t in warnings:
            tid = t.get('id', '?')
            name = t.get('name', '?')
            note = t.get('notes', 'no details')
            print(f"    {tid:6s} {name} — {note}")

    print()


def generate_markdown(tests, metadata, filename):
    """Generate Markdown report."""
    suites, total, total_pass, total_fail, total_warn = compute_stats(tests)
    pct = (total_pass / total * 100) if total > 0 else 0
    ts = metadata.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    lines = []
    lines.append(f"# Agent Crawl Report — {ts}")
    lines.append("")
    lines.append(f"**Total: {total_pass}/{total} PASS ({pct:.1f}%) | {total_fail} FAIL | {total_warn} WARN**")
    lines.append("")

    # Summary table
    lines.append("| Suite | Pass | Fail | Warn |")
    lines.append("|-------|------|------|------|")
    for suite_key in ['smoke', 'navigation', 'overlays', 'interlinear',
                      'search', 'content', 'mobile', 'performance']:
        label = SUITE_LABELS.get(suite_key, suite_key)
        s = suites.get(suite_key, {'pass': 0, 'fail': 0, 'warn': 0})
        lines.append(f"| {label} | {s['pass']} | {s['fail']} | {s['warn']} |")
    lines.append("")

    # Failures
    failures = [t for t in tests if t.get('status', '').upper() == 'FAIL']
    if failures:
        lines.append("## Failures")
        lines.append("")
        for t in failures:
            lines.append(f"### {t.get('id', '?')} — {t.get('name', '?')}")
            lines.append(f"- **Error:** {t.get('error', t.get('notes', 'no details'))}")
            if t.get('expected'):
                lines.append(f"- **Expected:** {t['expected']}")
            if t.get('actual'):
                lines.append(f"- **Actual:** {t['actual']}")
            if t.get('console_errors'):
                lines.append(f"- **Console errors:** {', '.join(t['console_errors'])}")
            lines.append("")

    # Warnings
    warnings = [t for t in tests if t.get('status', '').upper() == 'WARN']
    if warnings:
        lines.append("## Warnings")
        lines.append("")
        for t in warnings:
            lines.append(f"- **{t.get('id', '?')} {t.get('name', '?')}** — {t.get('notes', 'no details')}")
        lines.append("")

    # Per-suite detail
    lines.append("## Detailed Results")
    lines.append("")
    for suite_key in ['smoke', 'navigation', 'overlays', 'interlinear',
                      'search', 'content', 'mobile', 'performance']:
        if suite_key not in suites:
            continue
        label = SUITE_LABELS.get(suite_key, suite_key)
        s = suites[suite_key]
        lines.append(f"### {label}")
        lines.append("")
        lines.append("| ID | Test | Status | Notes |")
        lines.append("|-----|------|--------|-------|")
        for t in s['tests']:
            status = t.get('status', '?')
            icon = {'PASS': 'PASS', 'FAIL': 'FAIL', 'WARN': 'WARN'}.get(status, status)
            notes = t.get('notes', '')[:80]
            lines.append(f"| {t.get('id', '?')} | {t.get('name', '?')} | {icon} | {notes} |")
        lines.append("")

    md_content = '\n'.join(lines)
    md_path = os.path.join(RESULTS_DIR, filename.replace('.json', '.md'))
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"  Markdown report: {md_path}")
    return md_path


def generate_html(tests, metadata, filename):
    """Generate HTML report with styling."""
    suites, total, total_pass, total_fail, total_warn = compute_stats(tests)
    pct = (total_pass / total * 100) if total > 0 else 0
    ts = metadata.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    status_colors = {
        'PASS': '#2ea043',
        'FAIL': '#e05540',
        'WARN': '#d29922',
    }

    rows_html = ""
    for suite_key in ['smoke', 'navigation', 'overlays', 'interlinear',
                      'search', 'content', 'mobile', 'performance']:
        if suite_key not in suites:
            continue
        label = SUITE_LABELS.get(suite_key, suite_key)
        s = suites[suite_key]
        for t in s['tests']:
            status = t.get('status', '?').upper()
            color = status_colors.get(status, '#888')
            notes = html_mod.escape(t.get('notes', '')[:100])
            error = html_mod.escape(t.get('error', ''))
            display_note = error if error else notes
            rows_html += f"""
            <tr>
                <td>{html_mod.escape(str(t.get('id', '?')))}</td>
                <td>{html_mod.escape(str(t.get('name', '?')))}</td>
                <td>{html_mod.escape(str(t.get('suite', '?')))}</td>
                <td style="color:{color};font-weight:bold">{status}</td>
                <td>{display_note}</td>
            </tr>"""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Agent Crawl Report — {ts}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         background: #0c0e14; color: #e8e6e3; padding: 2rem; }}
  h1 {{ color: #c9a84c; margin-bottom: 0.5rem; }}
  .summary {{ font-size: 1.2rem; margin-bottom: 2rem; color: #a8a49e; }}
  .pass {{ color: #2ea043; }}
  .fail {{ color: #e05540; }}
  .warn {{ color: #d29922; }}
  table {{ width: 100%; border-collapse: collapse; margin-bottom: 2rem; }}
  th {{ background: #1a1d27; color: #c9a84c; padding: 0.6rem 1rem; text-align: left;
       border-bottom: 2px solid #c9a84c; }}
  td {{ padding: 0.5rem 1rem; border-bottom: 1px solid #2a2d37; }}
  tr:hover {{ background: #1a1d27; }}
  .stats {{ display: flex; gap: 2rem; margin-bottom: 2rem; }}
  .stat {{ background: #1a1d27; padding: 1rem 1.5rem; border-radius: 8px; text-align: center; }}
  .stat-num {{ font-size: 2rem; font-weight: bold; }}
  .stat-label {{ font-size: 0.85rem; color: #a8a49e; }}
</style>
</head>
<body>
  <h1>Agent Crawl Report</h1>
  <p class="summary">{ts} — {total} tests executed</p>

  <div class="stats">
    <div class="stat">
      <div class="stat-num pass">{total_pass}</div>
      <div class="stat-label">PASSED</div>
    </div>
    <div class="stat">
      <div class="stat-num fail">{total_fail}</div>
      <div class="stat-label">FAILED</div>
    </div>
    <div class="stat">
      <div class="stat-num warn">{total_warn}</div>
      <div class="stat-label">WARNINGS</div>
    </div>
    <div class="stat">
      <div class="stat-num" style="color:#c9a84c">{pct:.0f}%</div>
      <div class="stat-label">PASS RATE</div>
    </div>
  </div>

  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Test</th>
        <th>Suite</th>
        <th>Status</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>

  <p style="color:#666;font-size:0.8rem;margin-top:2rem;">
    Generated by Agent Crawl — Ancient Texts Study App
  </p>
</body>
</html>"""

    html_path = os.path.join(RESULTS_DIR, filename.replace('.json', '.html'))
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"  HTML report:     {html_path}")
    return html_path


def generate_report(filename=None):
    """Generate all report formats."""
    tests, metadata, fname = load_results(filename)

    print("\n" + "=" * 55)
    print("  GENERATING REPORTS")
    print("=" * 55)

    generate_console(tests, metadata)
    generate_markdown(tests, metadata, fname)
    generate_html(tests, metadata, fname)

    print("\n  Done!")


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else None
    generate_report(fname)
