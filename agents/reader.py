"""
THE READER — Content Quality Agent

Reads the app's content as a human student would and generates feedback:
  - student mode: curiosity-driven reading, flags unclear/thin/missing content
  - theologian mode: checks theological consistency across all content
  - crossref mode: validates every cross-reference in era files
  - qa mode: structural validation — manifest, verse counts, file integrity

Usage:
    python agents/reader.py --mode student --text genesis
    python agents/reader.py --mode student --text matthew
    python agents/reader.py --mode theologian --text all
    python agents/reader.py --mode crossref --text isaiah
    python agents/reader.py --mode qa
    python agents/reader.py --mode qa --verbose
"""

import os
import sys
import json
import argparse
import importlib.util
import re
import time
from datetime import datetime

# Windows UTF-8 fix
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from agents.config import (
    ARBITER_API_KEY, ARBITER_MODEL, SCRIBE_API_KEY, SCRIBE_MODEL,
    DATA_DIR, MANIFEST_PATH, REPORTS_DIR, THEOLOGICAL_GUIDELINES
)

# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_client(api_key):
    from anthropic import Anthropic
    return Anthropic(api_key=api_key)


def load_manifest():
    with open(MANIFEST_PATH, encoding='utf-8') as f:
        return json.load(f)


def get_text_data_dir(text_id, manifest):
    """Get actual data directory for a text (respects data_dir override in manifest)."""
    t = next((x for x in manifest.get('texts', []) if x['id'] == text_id), None)
    data_dir_name = t.get('data_dir', text_id) if t else text_id
    return os.path.join(DATA_DIR, data_dir_name)


def load_era_file(text_id, data_file, manifest=None):
    """Load a single era file and return its CHAPTERS list."""
    if manifest:
        text_dir = get_text_data_dir(text_id, manifest)
    else:
        text_dir = os.path.join(DATA_DIR, text_id)
    candidates = [
        os.path.join(text_dir, data_file + '.py'),
        os.path.join(DATA_DIR, data_file + '.py'),
    ]
    for path in candidates:
        if os.path.exists(path):
            spec = importlib.util.spec_from_file_location('era_' + data_file, path)
            mod  = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return getattr(mod, 'CHAPTERS', [])
    return []


def load_flow_file(text_id):
    """Load a flow translation file, return (flow_dict, notes_dict) or (None, None)."""
    flow_path = os.path.join(DATA_DIR, 'flow', f'flow_{text_id}.py')
    if not os.path.exists(flow_path):
        return None, None
    spec = importlib.util.spec_from_file_location('flow_' + text_id, flow_path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    flow_var  = next((v for v in dir(mod) if v.startswith('FLOW_')), None)
    notes_var = next((v for v in dir(mod) if v.startswith('NOTES_')), None)
    flow  = getattr(mod, flow_var,  None) if flow_var  else None
    notes = getattr(mod, notes_var, None) if notes_var else None
    return flow, notes


def get_texts_for_target(target, manifest):
    """Resolve --text argument to a list of text_ids."""
    if target == 'all':
        return [t['id'] for t in manifest['texts']]
    if target in ('ot', 'oldtestament'):
        return [t['id'] for t in manifest['texts'] if t.get('category') == 'ot']
    if target in ('nt', 'newtestament'):
        return [t['id'] for t in manifest['texts'] if t.get('category') == 'nt']
    return [target]


def write_report(mode, content, text_id='all'):
    """Save a report file and print it."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M')
    fname = f'reader_{mode}_{text_id}_{ts}.md'
    fpath = os.path.join(REPORTS_DIR, fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(content)
    print(f'\n--- Report saved: {fpath} ---')
    return fpath


# ─── Mode: Student ────────────────────────────────────────────────────────────

STUDENT_SYSTEM = """You are a curious, intelligent theology student reading ancient scripture and commentary for the first time. You are engaged, ask real questions, and notice when explanations are thin, unclear, or missing.

Your task: read the provided study chapter content and give honest, constructive feedback:

1. UNDERSTANDING CHECK — what concepts were explained well?
2. CONFUSION POINTS — what was unclear, jargon-heavy, or assumed too much prior knowledge?
3. MISSING EXPLANATIONS — what did you expect to find that wasn't there?
4. THIN SECTIONS — where did the content feel rushed or underdeveloped?
5. STANDOUT MOMENTS — what was genuinely illuminating or moving?
6. IMPROVEMENT SUGGESTIONS — specific, actionable additions/changes (cite section headings)

Format as markdown. Be specific — quote from the text when criticizing or praising.
Focus on whether a motivated non-expert could understand and be enriched by this content."""


def run_student_mode(text_id, manifest):
    """Read a text's content as a student and generate feedback."""
    client = get_client(ARBITER_API_KEY)
    text_def = next((t for t in manifest['texts'] if t['id'] == text_id), None)
    if not text_def:
        print(f'ERROR: Text {text_id} not found in manifest')
        return

    text_name = text_def.get('name', text_id)
    eras = [e for e in manifest.get('eras', []) if e.get('text') == text_id]

    print(f'\n{"="*60}')
    print(f'READER (Student Mode): {text_name}')
    print(f'{"="*60}')
    print(f'Eras to read: {len(eras)}')

    all_feedback = []
    for era in eras:
        data_file = era.get('data_file', '')
        if not data_file:
            continue
        chapters = load_era_file(text_id, data_file)
        if not chapters:
            print(f'  SKIP {data_file}: no chapters')
            continue

        # Build a summary of the content for Claude to read
        content_summary = []
        for ch in chapters[:6]:  # Cap at 6 chapters per era to control token use
            sections = ch.get('sections', [])
            section_text = '\n'.join(
                f'### {s.get("heading","")}\n{re.sub("<[^>]+>", "", s.get("body","")[:800])}'
                for s in sections[:3]
            )
            content_summary.append(f"""
## {ch.get("ref","?")} — {ch.get("title","")}
{ch.get("synopsis","")}

Key verse: {ch.get("key_verse",{}).get("ref","")} — {ch.get("key_verse",{}).get("text","")}

ANE Context: {ch.get("ane_backdrop","")[:400]}

{section_text}
""")

        era_content = '\n'.join(content_summary)
        era_name = era.get('name', data_file)

        print(f'  Reading: {era_name} ({len(chapters)} chapters)...', end=' ', flush=True)

        response = client.messages.create(
            model=ARBITER_MODEL,
            max_tokens=2000,
            system=STUDENT_SYSTEM,
            messages=[{
                'role': 'user',
                'content': f'Please read this study content for "{text_name} — {era_name}" and give your feedback as a student:\n\n{era_content}'
            }]
        )
        feedback = response.content[0].text
        all_feedback.append(f'# {text_name} — {era_name}\n\n{feedback}')
        print('done')

    # Check flow translations too
    flow, notes = load_flow_file(text_id)
    if flow:
        total_verses = sum(len(ch) for ch in flow.values())
        total_notes  = sum(len(n) for n in (notes or {}).values())
        # Sample a few verses for student feedback
        sample_verses = []
        for ch_num in sorted(flow.keys())[:3]:
            for v_num in sorted(flow[ch_num].keys())[:5]:
                sample_verses.append(f'{ch_num}:{v_num} — {flow[ch_num][v_num]}')
        sample = '\n'.join(sample_verses[:15])

        print(f'  Reading flow translation ({total_verses}v, {total_notes} notes)...', end=' ', flush=True)
        response = client.messages.create(
            model=ARBITER_MODEL,
            max_tokens=1000,
            system=STUDENT_SYSTEM,
            messages=[{
                'role': 'user',
                'content': f'Read this sample of the flow translation for {text_name} and evaluate: Is it literal yet readable? Does it sound like Scripture? Any verses that seem off or need a note?\n\n{sample}\n\n(Total: {total_verses} verses, {total_notes} study notes in the full file)'
            }]
        )
        all_feedback.append(f'# {text_name} — Flow Translation Review\n\n{response.content[0].text}')
        print('done')

    report = f'# READER REPORT: {text_name} (Student Mode)\n*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}*\n\n'
    report += '\n\n---\n\n'.join(all_feedback)
    write_report('student', report, text_id)


# ─── Mode: Theologian ─────────────────────────────────────────────────────────

THEOLOGIAN_SYSTEM = f"""You are THE ARBITER — a rigorous theological reviewer for the Ancient Texts Study App.

{THEOLOGICAL_GUIDELINES}

Your task: Read the provided content and check for:
1. CANONICAL STATUS ERRORS — is a non-canonical text presented as authoritative Scripture?
2. CHRISTOLOGICAL CONSISTENCY — is Christ presented as THE promised Messiah throughout?
3. DIVINE COUNCIL INTEGRITY — are elohim/council beings treated as real spiritual beings?
4. TRANSLATION FIDELITY — do flow translations match formal equivalence principles?
5. SETHITE CONTAMINATION — any hint that Genesis 6 "sons of God" are humans?
6. THEOLOGICAL GAPS — passages that NEED a divine council or Christological note but lack one

Output:
- CRITICAL issues (wrong canonical status, scripture misquote) — must fix
- WARNING issues (thin note, missed cross-reference) — should fix
- COMMENDATIONS — what's theologically strong

Format as markdown with severity levels."""


def run_theologian_mode(text_ids, manifest, all_eras=False, return_data=False):
    """Run theological consistency check across texts.

    Args:
        all_eras: If True, check ALL eras per text (not just first). More thorough but more API calls.
        return_data: If True, return (issues_list, total_usage) instead of writing report.
    """
    client = get_client(ARBITER_API_KEY)

    print(f'\n{"="*60}')
    print(f'READER (Theologian Mode): {len(text_ids)} texts' + (' — ALL ERAS' if all_eras else ''))
    print(f'{"="*60}')

    all_issues = []
    total_usage = {"input_tokens": 0, "output_tokens": 0}
    for text_id in text_ids:
        text_def = next((t for t in manifest['texts'] if t['id'] == text_id), None)
        if not text_def:
            continue
        text_name = text_def.get('name', text_id)
        eras = [e for e in manifest.get('eras', []) if e.get('text') == text_id]
        if not eras:
            continue

        eras_to_check = eras if all_eras else [eras[0]]

        for era in eras_to_check:
            chapters = load_era_file(text_id, era.get('data_file', ''))
            if not chapters:
                continue

            # Sample content from first chapter
            ch = chapters[0]
            sections = ch.get('sections', [])
            body_text = ' '.join(re.sub('<[^>]+>', '', s.get('body','')[:600]) for s in sections[:2])

            era_label = era.get('name', era.get('id', ''))
            print(f'  Auditing: {text_name} / {era_label}...', end=' ', flush=True)
            response = client.messages.create(
                model=ARBITER_MODEL,
                max_tokens=1500,
                system=THEOLOGIAN_SYSTEM,
                messages=[{
                    'role': 'user',
                    'content': f'Audit this content from {text_name} — {era_label} ({text_def.get("category","?").upper()}):\n\nREF: {ch.get("ref","?")} — {ch.get("title","")}\nSYNOPSIS: {ch.get("synopsis","")}\nCROSS-REFS: {json.dumps(ch.get("cross_refs",[]))}\nCONTENT: {body_text}'
                }]
            )
            result = response.content[0].text
            all_issues.append(f'## {text_name} — {era_label}\n\n{result}')
            if hasattr(response, 'usage') and response.usage:
                total_usage["input_tokens"] += response.usage.input_tokens
                total_usage["output_tokens"] += response.usage.output_tokens
            print('done')
            time.sleep(1)  # Rate limiting between eras

    if return_data:
        return all_issues, total_usage

    report = f'# THEOLOGICAL AUDIT REPORT\n*{datetime.now().strftime("%Y-%m-%d %H:%M")} — {len(text_ids)} texts reviewed' + (' (all eras)' if all_eras else '') + '*\n\n'
    report += '\n\n---\n\n'.join(all_issues)
    write_report('theologian', report, 'multi')


# ─── Mode: Cross-Reference Validator ─────────────────────────────────────────

# Valid book abbreviations for quick checks
VALID_OT_BOOKS = {
    'Gen','Exod','Lev','Num','Deut','Josh','Judg','Ruth',
    '1Sam','2Sam','1Kgs','2Kgs','1Chr','2Chr','Ezra','Neh','Esth',
    'Job','Ps','Prov','Eccl','Song','Isa','Jer','Lam','Ezek','Dan',
    'Hos','Joel','Amos','Obad','Jonah','Mic','Nah','Hab','Zeph','Hag','Zech','Mal'
}
VALID_NT_BOOKS = {
    'Matt','Mark','Luke','John','Acts','Rom','1Cor','2Cor','Gal','Eph',
    'Phil','Col','1Thess','2Thess','1Tim','2Tim','Titus','Phlm',
    'Heb','Jas','1Pet','2Pet','1John','2John','3John','Jude','Rev'
}
ALL_VALID_BOOKS = VALID_OT_BOOKS | VALID_NT_BOOKS

CROSSREF_PATTERN = re.compile(
    r'\b(1|2|3)?'
    r'(Gen|Exod|Lev|Num|Deut|Josh|Judg|Ruth|Sam|Kgs|Chr|Ezra|Neh|Esth|'
    r'Job|Ps|Prov|Eccl|Song|Isa|Jer|Lam|Ezek|Dan|Hos|Joel|Amos|Obad|'
    r'Jonah|Mic|Nah|Hab|Zeph|Hag|Zech|Mal|'
    r'Matt|Mark|Luke|John|Acts|Rom|Cor|Gal|Eph|Phil|Col|Thess|Tim|Titus|Phlm|'
    r'Heb|Jas|Pet|Rev)'
    r'\.?\s*\d+:\d+(?:-\d+)?',
    re.IGNORECASE
)


def run_crossref_mode(text_ids, manifest, verbose=False):
    """Scan all cross-references in era files and report suspicious/malformed ones."""
    print(f'\n{"="*60}')
    print(f'READER (Cross-Ref Mode): scanning {len(text_ids)} texts')
    print(f'{"="*60}')

    issues = []
    good_count = 0
    bad_count  = 0

    for text_id in text_ids:
        text_def = next((t for t in manifest['texts'] if t['id'] == text_id), None)
        if not text_def:
            continue
        text_name = text_def.get('name', text_id)
        eras = [e for e in manifest.get('eras', []) if e.get('text') == text_id]

        for era in eras:
            chapters = load_era_file(text_id, era.get('data_file', ''))
            for ch in chapters:
                refs = ch.get('cross_refs', [])
                for ref_entry in refs:
                    ref_str = ref_entry.get('ref', '')
                    note    = ref_entry.get('note', '')
                    # Basic format check: should match "Book ch:v"
                    if not CROSSREF_PATTERN.search(ref_str):
                        bad_count += 1
                        issues.append({
                            'severity': 'WARNING',
                            'text': text_name,
                            'chapter': ch.get('ref', ''),
                            'ref': ref_str,
                            'note': note[:80],
                            'problem': 'Format does not match expected Book ch:v pattern'
                        })
                    else:
                        good_count += 1
                        if verbose:
                            print(f'  OK: {ref_str}')

                # Also scan section bodies for inline refs
                for section in ch.get('sections', []):
                    body = section.get('body', '')
                    found = CROSSREF_PATTERN.findall(body)

    # Enoch/pseudepigrapha refs that get cited as Scripture
    pseudo_refs = re.compile(r'\b1\s*En(?:och)?\s*\d+', re.IGNORECASE)

    report_lines = [
        f'# CROSS-REFERENCE VALIDATION REPORT',
        f'*{datetime.now().strftime("%Y-%m-%d %H:%M")}*\n',
        f'**Valid refs**: {good_count} | **Issues**: {bad_count}\n',
        '## Issues Found\n'
    ]

    if not issues:
        report_lines.append('No cross-reference format issues found.')
    else:
        for iss in issues:
            report_lines.append(
                f'- **[{iss["severity"]}]** `{iss["text"]}` | `{iss["chapter"]}` | '
                f'Ref: `{iss["ref"]}` → {iss["problem"]}'
            )

    report = '\n'.join(report_lines)
    write_report('crossref', report, 'all')


# ─── Mode: QA (Structural) ───────────────────────────────────────────────────

def run_qa_mode(manifest, verbose=False):
    """Structural quality assurance — all manifest refs resolve, verse counts match, etc."""
    print(f'\n{"="*60}')
    print('READER (QA Mode): Structural Validation')
    print(f'{"="*60}')

    issues   = []
    warnings = []
    passed   = []

    texts = manifest.get('texts', [])
    eras  = manifest.get('eras', [])

    # 1. Every text in manifest has a category
    for t in texts:
        if not t.get('category'):
            issues.append(f'TEXT {t["id"]}: missing category')
        else:
            passed.append(f'TEXT {t["id"]}: category={t["category"]}')

    # 2. Every era references a valid text
    text_ids = {t['id'] for t in texts}
    for e in eras:
        if e.get('text') not in text_ids:
            issues.append(f'ERA {e["id"]}: text="{e.get("text")}" not in manifest texts')
        text_def3 = next((t for t in texts if t['id'] == e.get('text','')), None)
        if not e.get('data_file') and (not text_def3 or text_def3.get('content_type') != 'html_fragment'):
            warnings.append(f'ERA {e["id"]}: missing data_file field')

    # 3. Every era data_file exists on disk
    for e in eras:
        data_file = e.get('data_file', '')
        if not data_file:
            continue
        text_id   = e.get('text', '')
        text_def2 = next((t for t in texts if t['id'] == text_id), None)
        data_dir_name = text_def2.get('data_dir', text_id) if text_def2 else text_id
        text_dir  = os.path.join(DATA_DIR, data_dir_name)
        candidates = [
            os.path.join(text_dir, data_file + '.py'),
            os.path.join(DATA_DIR, data_file + '.py'),
        ]
        found = any(os.path.exists(p) for p in candidates)
        if not found:
            issues.append(f'ERA {e["id"]}: data_file "{data_file}.py" NOT FOUND on disk')
        else:
            passed.append(f'ERA {e["id"]}: file OK')

    # 4. Every text in manifest has at least 1 era
    era_texts = {e.get('text') for e in eras}
    for t in texts:
        if t['id'] not in era_texts:
            warnings.append(f'TEXT {t["id"]}: 0 era entries in manifest')

    # 5. Flow files: check verse count vs interlinear
    flow_dir = os.path.join(DATA_DIR, 'flow')
    if os.path.isdir(flow_dir):
        flow_files = [f for f in os.listdir(flow_dir)
                      if f.startswith('flow_') and f.endswith('.py') and f.count('_') == 1]
        for ff in sorted(flow_files):
            book_id = ff.replace('flow_', '').replace('.py', '')
            fpath   = os.path.join(flow_dir, ff)
            try:
                spec = importlib.util.spec_from_file_location('fl', fpath)
                mod  = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                flow_var = next((v for v in dir(mod) if v.startswith('FLOW_')), None)
                if not flow_var:
                    issues.append(f'FLOW {ff}: no FLOW_ variable')
                    continue
                flow = getattr(mod, flow_var)
                total_v = sum(len(ch) for ch in flow.values())
                if total_v == 0:
                    issues.append(f'FLOW {ff}: 0 verses — empty file')
                else:
                    passed.append(f'FLOW {ff}: {total_v} verses OK')
            except Exception as ex:
                issues.append(f'FLOW {ff}: PARSE ERROR — {ex}')

    # 6. Check interlinear files in manifest are present
    for t in texts:
        il_key = t.get('interlinear', '')
        if il_key:
            book_id = t['id']
            # Genesis uses flat interlinear.py (not interlinear_genesis.py)
            candidates = [
                os.path.join(DATA_DIR, f'interlinear_{book_id}.py'),
                os.path.join(DATA_DIR, f'interlinear_nt_{book_id}.py'),
                os.path.join(DATA_DIR, 'interlinear.py'),  # genesis special case
            ]
            found = any(os.path.exists(p) for p in candidates)
            if not found:
                issues.append(f'INTERLINEAR {book_id}: manifest says {il_key} but no file found')
            else:
                passed.append(f'INTERLINEAR {book_id}: file OK')

    # Summary report
    report = [
        '# QA STRUCTURAL VALIDATION REPORT',
        f'*{datetime.now().strftime("%Y-%m-%d %H:%M")}*\n',
        f'**PASS**: {len(passed)} | **WARN**: {len(warnings)} | **FAIL**: {len(issues)}\n',
    ]

    if issues:
        report.append('## CRITICAL ISSUES\n')
        for iss in issues:
            report.append(f'- ❌ {iss}')

    if warnings:
        report.append('\n## WARNINGS\n')
        for w in warnings:
            report.append(f'- ⚠️ {w}')

    if verbose:
        report.append('\n## PASSED CHECKS\n')
        for p in passed[:50]:
            report.append(f'- ✅ {p}')
        if len(passed) > 50:
            report.append(f'- ... and {len(passed)-50} more')

    report_text = '\n'.join(report)
    write_report('qa', report_text, 'structural')

    # Print quick summary
    print(f'\nRESULT: {len(issues)} critical | {len(warnings)} warnings | {len(passed)} passed')
    if issues:
        print('\nCRITICAL ISSUES:')
        for iss in issues[:10]:
            print(f'  ❌ {iss}')
    if warnings:
        print('\nWARNINGS:')
        for w in warnings[:10]:
            print(f'  ⚠️ {w}')


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='THE READER — Content Quality Agent for Ancient Texts Study App'
    )
    parser.add_argument('--mode', choices=['student', 'theologian', 'crossref', 'qa'],
                        default='qa', help='Reading mode')
    parser.add_argument('--text', default='all',
                        help='Text ID (e.g. genesis, matthew, nt, ot, all)')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--all-eras', action='store_true',
                        help='Theologian mode: check ALL eras per text (not just first)')
    args = parser.parse_args()

    manifest  = load_manifest()
    text_ids  = get_texts_for_target(args.text, manifest)

    if args.mode == 'qa':
        run_qa_mode(manifest, verbose=args.verbose)
    elif args.mode == 'student':
        for text_id in text_ids:
            run_student_mode(text_id, manifest)
    elif args.mode == 'theologian':
        run_theologian_mode(text_ids, manifest, all_eras=args.all_eras)
    elif args.mode == 'crossref':
        run_crossref_mode(text_ids, manifest, verbose=args.verbose)


if __name__ == '__main__':
    main()
