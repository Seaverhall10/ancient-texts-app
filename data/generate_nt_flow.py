"""
generate_nt_flow.py — NT Flow Translation Generator

Uses the Claude API (SCRIBE key) to generate verse-by-verse formal equivalence
English translations for New Testament books, matching the OT flow file format.

Output: data/flow/flow_{book}.py with FLOW_{BOOK} and NOTES_{BOOK} dicts

Usage:
    python data/generate_nt_flow.py --book philemon
    python data/generate_nt_flow.py --book 2john
    python data/generate_nt_flow.py --all
    python data/generate_nt_flow.py --all --start-from galatians
"""

import os
import sys
import json
import time
import argparse
import importlib.util
import re

# Windows UTF-8 console fix
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Project root
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from agents.config import SCRIBE_API_KEY

# === Book Registry (shortest to longest) ===
NT_BOOKS_ORDERED = [
    ('2john',           '2JOHN',           '2 John'),
    ('3john',           '3JOHN',           '3 John'),
    ('philemon',        'PHILEMON',         'Philemon'),
    ('jude',            'JUDE',             'Jude'),
    ('titus',           'TITUS',            'Titus'),
    ('2thessalonians',  '2THESSALONIANS',   '2 Thessalonians'),
    ('2peter',          '2PETER',           '2 Peter'),
    ('2timothy',        '2TIMOTHY',         '2 Timothy'),
    ('1thessalonians',  '1THESSALONIANS',   '1 Thessalonians'),
    ('colossians',      'COLOSSIANS',       'Colossians'),
    ('philippians',     'PHILIPPIANS',      'Philippians'),
    ('1john',           '1JOHN',            '1 John'),
    ('1peter',          '1PETER',           '1 Peter'),
    ('james',           'JAMES',            'James'),
    ('1timothy',        '1TIMOTHY',         '1 Timothy'),
    ('galatians',       'GALATIANS',        'Galatians'),
    ('ephesians',       'EPHESIANS',        'Ephesians'),
    ('hebrews',         'HEBREWS',          'Hebrews'),
    ('2corinthians',    '2CORINTHIANS',     '2 Corinthians'),
    ('romans',          'ROMANS',           'Romans'),
    ('1corinthians',    '1CORINTHIANS',     '1 Corinthians'),
    ('revelation',      'REVELATION',       'Revelation'),
    ('mark',            'MARK',             'Mark'),
    ('matthew',         'MATTHEW',          'Matthew'),
    ('acts',            'ACTS',             'Acts'),
    ('luke',            'LUKE',             'Luke'),
    ('john',            'JOHN',             'John'),
]

NT_BOOK_MAP = {b[0]: b for b in NT_BOOKS_ORDERED}

FLOW_DIR = os.path.join(ROOT, 'data', 'flow')
DATA_DIR  = os.path.join(ROOT, 'data')


def load_interlinear(book_id):
    """Load NT interlinear data for a book."""
    fp = os.path.join(DATA_DIR, f'interlinear_nt_{book_id}.py')
    if not os.path.exists(fp):
        print(f'ERROR: {fp} not found')
        return None
    spec = importlib.util.spec_from_file_location('il', fp)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    var_suffix = NT_BOOK_MAP[book_id][1]
    return getattr(mod, f'INTERLINEAR_NT_{var_suffix}', None)


def build_chapter_context(chapter_data, ch_num, book_name):
    """Build a human-readable verse-by-verse context string from interlinear data."""
    lines = []
    verses = chapter_data.get('verses', [])
    for v in verses:
        vnum = v['num']
        words = v.get('words', [])
        # Build gloss line
        glosses  = ' '.join(w.get('g', '') for w in words if w.get('g'))
        greek    = ' '.join(w.get('h', '') for w in words if w.get('h'))
        translit = ' '.join(w.get('t', '') for w in words if w.get('t'))
        lines.append(f'  v{vnum}:')
        lines.append(f'    Greek:  {greek}')
        lines.append(f'    Translit: {translit}')
        lines.append(f'    Glosses: {glosses}')
    return '\n'.join(lines)


TRANSLATION_GUIDELINES = """TRANSLATION RULES (non-negotiable):
1. Formal equivalence — word-for-word literal, not dynamic paraphrase.
2. NEVER use "LORD" for Greek "Kyrios" — use "Lord" (Greek has no YHWH distinction to preserve; in NT Kyrios = Lord).
3. Jesus IS the promised Messiah and King of everything — translate accordingly.
4. "Christ" = Christos = Anointed One — keep "Christ" (do not substitute "Messiah" unless noting both).
5. Preserve Greek word order flavor where English allows it.
6. Quoted OT passages in NT must match LXX flavor (slightly formal/archaic).
7. For hapax legomena or unusual Greek, note it in the study note.
8. Avoid modern paraphrase language. Keep a dignified, slightly elevated register.
9. Use "you" (plural when Greek is plural, e.g., "you all" only in notes, not the translation).
10. Translate "elohim" concept words (theos, theios, pneuma) consistently throughout."""

NOTE_GUIDELINES = """STUDY NOTE RULES:
- Notes use category prefixes: GREEK:, TYPOLOGY:, HISTORICAL:, THEOLOGICAL:, DIVINE_COUNCIL:, STRUCTURE:
- GREEK notes: explain key Greek terms (cite Strong's if known), word origins, nuances
- TYPOLOGY notes: OT echoes, fulfillment patterns, Christ typology
- HISTORICAL notes: Roman-era context, Second Temple Judaism, geography
- THEOLOGICAL notes: doctrinal significance, divine council implications
- Notes for key verses only (10-30% of verses, prioritize theologically dense ones)
- Keep notes concise but substantive (2-5 sentences each)
- Cross-reference format: (Matt 5:17), (Ps 22:1), (Eph 1:10)"""


def call_claude_for_chapter(client, book_name, ch_num, chapter_data, total_chapters, book_intro=''):
    """Call Claude API to generate translations + notes for one chapter."""
    context = build_chapter_context(chapter_data, ch_num, book_name)
    verse_count = len(chapter_data.get('verses', []))

    system = f"""You are THE SCRIBE — a theological linguist generating formal equivalence translations of New Testament Greek for a study Bible app. You have deep knowledge of Koine Greek, Second Temple Judaism, and divine council theology.

{TRANSLATION_GUIDELINES}

{NOTE_GUIDELINES}"""

    prompt = f"""Generate a verse-by-verse translation of {book_name} chapter {ch_num} (of {total_chapters}) for our Ancient Texts Study App.

CHAPTER CONTEXT (Greek text with word-by-word glosses):
{context}

{book_intro}

OUTPUT FORMAT — respond with ONLY valid Python dict literals, NO imports, NO variable names, NO markdown code blocks. Just the raw dict structures:

TRANSLATIONS (dict mapping verse_num int → English translation string):
{{
    1: 'Translation of verse 1...',
    2: 'Translation of verse 2...',
    ...{verse_count}: 'Translation of last verse...'
}}

NOTES (dict mapping verse_num int → note string, only for significant verses):
{{
    1: 'GREEK: explanation...',
    3: 'TYPOLOGY: explanation...',
    ...
}}

Important:
- Return EXACTLY two dicts separated by a blank line
- First dict: ALL {verse_count} verses, every verse number from 1 to {verse_count}
- Second dict: notes for 10-30% of verses (theologically significant ones)
- Use single-quoted strings. Escape internal single quotes with backslash: it\\'s
- NO newlines inside strings
- Make translations accurate, literal, dignified"""

    response = client.messages.create(
        model='claude-opus-4-6',
        max_tokens=8000,
        system=system,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.content[0].text


def parse_two_dicts(raw_text):
    """
    Parse Claude's output: two Python dict literals.
    Returns (translations_dict, notes_dict).
    """
    # Strip markdown code fences if present
    raw = re.sub(r'```python\s*', '', raw_text)
    raw = re.sub(r'```\s*', '', raw)
    raw = raw.strip()

    # Find the two dicts by balanced brace matching
    dicts_found = []
    i = 0
    while i < len(raw) and len(dicts_found) < 2:
        if raw[i] == '{':
            depth = 0
            start = i
            j = i
            in_str = False
            str_char = None
            escape = False
            while j < len(raw):
                c = raw[j]
                if escape:
                    escape = False
                elif c == '\\':
                    escape = True
                elif in_str:
                    if c == str_char:
                        in_str = False
                elif c in ('"', "'"):
                    in_str = True
                    str_char = c
                elif c == '{':
                    depth += 1
                elif c == '}':
                    depth -= 1
                    if depth == 0:
                        dicts_found.append(raw[start:j+1])
                        i = j + 1
                        break
                j += 1
            else:
                break
        else:
            i += 1

    if len(dicts_found) < 2:
        raise ValueError(f'Could not find 2 dicts in output. Found {len(dicts_found)}. Raw:\n{raw[:500]}')

    translations = eval(dicts_found[0])
    notes = eval(dicts_found[1])
    return translations, notes


def get_book_intro(book_id, book_name):
    """Load book intro from info.py for context."""
    info_path = os.path.join(DATA_DIR, book_id, 'info.py')
    if not os.path.exists(info_path):
        return ''
    try:
        spec = importlib.util.spec_from_file_location('info', info_path)
        mod  = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        info = getattr(mod, 'INFO', {})
        overview = info.get('overview', '')
        if overview and len(overview) > 500:
            overview = overview[:500] + '...'
        return f'BOOK CONTEXT ({book_name}): {overview}' if overview else ''
    except Exception:
        return ''


def generate_flow_for_book(book_id, force=False):
    """Generate flow translations for a complete NT book."""
    if book_id not in NT_BOOK_MAP:
        print(f'ERROR: Unknown book: {book_id}')
        return False

    _, var_suffix, book_name = NT_BOOK_MAP[book_id]
    out_path = os.path.join(FLOW_DIR, f'flow_{book_id}.py')

    if os.path.exists(out_path) and not force:
        print(f'SKIP: {out_path} already exists (use --force to overwrite)')
        return True

    print(f'\n{"="*60}')
    print(f'GENERATING: {book_name} ({book_id})')
    print(f'{"="*60}')

    # Load interlinear data
    il_data = load_interlinear(book_id)
    if not il_data:
        return False

    total_chapters = len(il_data)
    total_verses   = sum(len(ch.get('verses', [])) for ch in il_data.values())
    print(f'Chapters: {total_chapters}, Verses: {total_verses}')

    # Load book context
    book_intro = get_book_intro(book_id, book_name)

    # Claude client
    from anthropic import Anthropic
    client = Anthropic(api_key=SCRIBE_API_KEY)

    # Accumulate translations + notes per chapter
    all_translations = {}  # {ch: {v: text}}
    all_notes        = {}  # {ch: {v: note}}

    for ch_num in sorted(il_data.keys()):
        chapter_data = il_data[ch_num]
        verse_count  = len(chapter_data.get('verses', []))
        print(f'  Chapter {ch_num}/{total_chapters} ({verse_count} verses)...', end=' ', flush=True)

        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                raw = call_claude_for_chapter(client, book_name, ch_num, chapter_data, total_chapters, book_intro)
                translations, notes = parse_two_dicts(raw)

                # Validate: all verses present
                expected = set(v['num'] for v in chapter_data.get('verses', []))
                got       = set(translations.keys())
                missing   = expected - got
                if missing:
                    print(f'\n    WARNING: Missing verses {sorted(missing)} in chapter {ch_num}')

                all_translations[ch_num] = translations
                all_notes[ch_num]        = notes
                print(f'OK ({len(translations)} verses, {len(notes)} notes)')
                break

            except Exception as e:
                print(f'\n    Attempt {attempt} failed: {e}')
                if attempt < max_retries:
                    print(f'    Retrying in 5s...')
                    time.sleep(5)
                else:
                    print(f'    GIVING UP on chapter {ch_num}')
                    all_translations[ch_num] = {}
                    all_notes[ch_num]        = {}

        # Small pause between chapters to avoid rate limiting
        if ch_num < max(il_data.keys()):
            time.sleep(1)

    # Write output file
    _write_flow_file(out_path, book_id, var_suffix, book_name, all_translations, all_notes, total_verses)
    print(f'\n✓ Written: {out_path}')
    return True


def _write_flow_file(out_path, book_id, var_suffix, book_name, all_translations, all_notes, total_verses):
    """Write the flow file in the standard format."""
    os.makedirs(FLOW_DIR, exist_ok=True)

    total_notes = sum(len(n) for n in all_notes.values())

    lines = []
    lines.append(f'"""')
    lines.append(f'Flow translations for {book_name} — accurate, literal English renderings.')
    lines.append(f'Every verse. Formal equivalence style. From the Greek New Testament (SBLGNT).')
    lines.append(f'Jesus Christ IS the promised Messiah and King of everything.')
    lines.append(f'Generated by generate_nt_flow.py using Claude Opus.')
    lines.append(f'Verses: {total_verses} | Notes: {total_notes}')
    lines.append(f'"""')
    lines.append('')
    lines.append(f'FLOW_{var_suffix} = {{')

    for ch_num in sorted(all_translations.keys()):
        translations = all_translations[ch_num]
        lines.append(f'    {ch_num}: {{  # Chapter {ch_num}')
        for v_num in sorted(translations.keys()):
            text = translations[v_num]
            # Sanitize: remove newlines, escape single quotes
            text = text.replace('\r', '').replace('\n', ' ')
            text = text.replace('\\', '\\\\').replace("'", "\\'")
            lines.append(f"        {v_num}: '{text}',")
        lines.append(f'    }},')

    lines.append('}')
    lines.append('')
    lines.append(f'NOTES_{var_suffix} = {{')

    for ch_num in sorted(all_notes.keys()):
        notes = all_notes[ch_num]
        if not notes:
            continue
        lines.append(f'    {ch_num}: {{')
        for v_num in sorted(notes.keys()):
            note = notes[v_num]
            note = note.replace('\r', '').replace('\n', ' ')
            note = note.replace('\\', '\\\\').replace("'", "\\'")
            lines.append(f"        {v_num}: '{note}',")
        lines.append(f'    }},')

    lines.append('}')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def validate_flow_file(path):
    """Quick validation: import file, check FLOW and NOTES vars exist and are non-empty."""
    try:
        spec = importlib.util.spec_from_file_location('flow_check', path)
        mod  = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        # Find FLOW_ and NOTES_ vars
        flow_vars  = [v for v in dir(mod) if v.startswith('FLOW_')]
        notes_vars = [v for v in dir(mod) if v.startswith('NOTES_')]
        if not flow_vars:
            return False, 'No FLOW_ variable found'
        flow = getattr(mod, flow_vars[0])
        total_verses = sum(len(ch) for ch in flow.values())
        if total_verses == 0:
            return False, 'FLOW is empty'
        return True, f'{total_verses} verses, {len(notes_vars)} notes vars'
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description='Generate NT flow translations using Claude API')
    parser.add_argument('--book', help='Book ID (e.g., philemon, matthew)')
    parser.add_argument('--all', action='store_true', help='Generate all 27 NT books')
    parser.add_argument('--start-from', help='When using --all, start from this book ID')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files')
    parser.add_argument('--validate', help='Validate an existing flow file')
    args = parser.parse_args()

    if args.validate:
        ok, msg = validate_flow_file(args.validate)
        print(f'{"PASS" if ok else "FAIL"}: {msg}')
        return

    if args.all:
        books = NT_BOOKS_ORDERED
        if args.start_from:
            start = args.start_from.lower()
            idx = next((i for i, b in enumerate(books) if b[0] == start), 0)
            books = books[idx:]
            print(f'Starting from: {books[0][2]} (position {idx+1}/27)')

        print(f'Generating flow translations for {len(books)} NT books...')
        success = 0
        for book_id, _, _ in books:
            ok = generate_flow_for_book(book_id, force=args.force)
            if ok:
                success += 1
            time.sleep(2)  # Pause between books

        print(f'\n{"="*60}')
        print(f'COMPLETE: {success}/{len(books)} books generated')

    elif args.book:
        generate_flow_for_book(args.book.lower(), force=args.force)

    else:
        parser.print_help()
        print('\nAvailable books (shortest to longest):')
        for book_id, _, name in NT_BOOKS_ORDERED:
            out = os.path.join(FLOW_DIR, f'flow_{book_id}.py')
            status = '✓' if os.path.exists(out) else '⬜'
            print(f'  {status} {book_id:20s} ({name})')


if __name__ == '__main__':
    main()
