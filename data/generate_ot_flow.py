"""
generate_ot_flow.py — OT Flow Translation Generator

Uses the Claude API (SCRIBE key) to generate verse-by-verse formal equivalence
English translations for Old Testament books that don't have interlinear data.

Output: data/flow/flow_{book}.py with FLOW_{BOOK} and NOTES_{BOOK} dicts

Usage:
    python data/generate_ot_flow.py --book jeremiah
    python data/generate_ot_flow.py --all
    python data/generate_ot_flow.py --all --start-from hosea
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

# === OT Book Registry (24 missing books, ordered shortest to longest) ===
OT_BOOKS_ORDERED = [
    # (book_id, VAR_SUFFIX, display_name, chapter_count)
    ('obadiah',       'OBADIAH',       'Obadiah',          1),
    ('lamentations',  'LAMENTATIONS',  'Lamentations',     5),
    ('haggai',        'HAGGAI',        'Haggai',           2),
    ('jonah',         'JONAH',         'Jonah',            4),
    ('nahum',         'NAHUM',         'Nahum',            3),
    ('malachi',       'MALACHI',       'Malachi',          4),
    ('habakkuk',      'HABAKKUK',      'Habakkuk',         3),
    ('zephaniah',     'ZEPHANIAH',     'Zephaniah',        3),
    ('joel',          'JOEL',          'Joel',             3),
    ('songofsolomon', 'SONGOFSOLOMON', 'Song of Solomon',  8),
    ('hosea',         'HOSEA',         'Hosea',           14),
    ('amos',          'AMOS',          'Amos',             9),
    ('micah',         'MICAH',         'Micah',            7),
    ('zechariah',     'ZECHARIAH',     'Zechariah',       14),
    ('ecclesiastes',  'ECCLESIASTES',  'Ecclesiastes',    12),
    ('esther',        'ESTHER',        'Esther',          10),
    ('ezra',          'EZRA',          'Ezra',            10),
    ('nehemiah',      'NEHEMIAH',      'Nehemiah',        13),
    ('proverbs',      'PROVERBS',      'Proverbs',        31),
    ('1chronicles',   '1CHRONICLES',   '1 Chronicles',    29),
    ('2chronicles',   '2CHRONICLES',   '2 Chronicles',    36),
    ('job',           'JOB',           'Job',             42),
    ('ezekiel',       'EZEKIEL',       'Ezekiel',        48),
    ('jeremiah',      'JEREMIAH',      'Jeremiah',        52),
]

OT_BOOK_MAP = {b[0]: b for b in OT_BOOKS_ORDERED}

FLOW_DIR = os.path.join(ROOT, 'data', 'flow')
DATA_DIR = os.path.join(ROOT, 'data')

# Standard verse counts per chapter for each OT book (from the Masoretic Text)
VERSE_COUNTS = {
    'obadiah':       {1: 21},
    'lamentations':  {1: 22, 2: 22, 3: 66, 4: 22, 5: 22},
    'haggai':        {1: 15, 2: 23},
    'jonah':         {1: 17, 2: 10, 3: 10, 4: 11},
    'nahum':         {1: 15, 2: 13, 3: 19},
    'malachi':       {1: 14, 2: 17, 3: 18, 4: 6},
    'habakkuk':      {1: 17, 2: 20, 3: 19},
    'zephaniah':     {1: 18, 2: 15, 3: 20},
    'joel':          {1: 20, 2: 32, 3: 21},
    'songofsolomon': {1: 17, 2: 17, 3: 11, 4: 16, 5: 16, 6: 13, 7: 13, 8: 14},
    'hosea':         {1: 11, 2: 23, 3: 5, 4: 19, 5: 15, 6: 11, 7: 16, 8: 14, 9: 17, 10: 15, 11: 12, 12: 14, 13: 16, 14: 9},
    'amos':          {1: 15, 2: 16, 3: 15, 4: 13, 5: 27, 6: 14, 7: 17, 8: 14, 9: 15},
    'micah':         {1: 16, 2: 13, 3: 12, 4: 13, 5: 15, 6: 16, 7: 20},
    'zechariah':     {1: 21, 2: 13, 3: 10, 4: 14, 5: 11, 6: 15, 7: 14, 8: 23, 9: 17, 10: 12, 11: 17, 12: 14, 13: 9, 14: 21},
    'ecclesiastes':  {1: 18, 2: 26, 3: 22, 4: 16, 5: 20, 6: 12, 7: 29, 8: 17, 9: 18, 10: 20, 11: 10, 12: 14},
    'esther':        {1: 22, 2: 23, 3: 15, 4: 17, 5: 14, 6: 14, 7: 10, 8: 17, 9: 32, 10: 3},
    'ezra':          {1: 11, 2: 70, 3: 13, 4: 24, 5: 17, 6: 22, 7: 28, 8: 36, 9: 15, 10: 44},
    'nehemiah':      {1: 11, 2: 20, 3: 32, 4: 23, 5: 19, 6: 19, 7: 73, 8: 18, 9: 38, 10: 39, 11: 36, 12: 47, 13: 31},
    'proverbs':      {1: 33, 2: 22, 3: 35, 4: 27, 5: 23, 6: 35, 7: 27, 8: 36, 9: 18, 10: 32, 11: 31, 12: 28, 13: 25, 14: 35, 15: 33, 16: 33, 17: 28, 18: 24, 19: 29, 20: 30, 21: 31, 22: 29, 23: 35, 24: 34, 25: 28, 26: 28, 27: 27, 28: 28, 29: 27, 30: 33, 31: 31},
    '1chronicles':   {1: 54, 2: 55, 3: 24, 4: 43, 5: 26, 6: 81, 7: 40, 8: 40, 9: 44, 10: 14, 11: 47, 12: 40, 13: 14, 14: 17, 15: 29, 16: 43, 17: 27, 18: 17, 19: 19, 20: 8, 21: 30, 22: 19, 23: 32, 24: 31, 25: 31, 26: 32, 27: 34, 28: 21, 29: 30},
    '2chronicles':   {1: 17, 2: 18, 3: 17, 4: 22, 5: 14, 6: 42, 7: 22, 8: 18, 9: 31, 10: 19, 11: 23, 12: 16, 13: 22, 14: 15, 15: 19, 16: 14, 17: 19, 18: 34, 19: 11, 20: 37, 21: 20, 22: 12, 23: 21, 24: 27, 25: 28, 26: 23, 27: 9, 28: 27, 29: 36, 30: 27, 31: 21, 32: 33, 33: 25, 34: 33, 35: 27, 36: 23},
    'job':           {1: 22, 2: 13, 3: 26, 4: 21, 5: 27, 6: 30, 7: 21, 8: 22, 9: 35, 10: 22, 11: 20, 12: 25, 13: 28, 14: 22, 15: 35, 16: 22, 17: 16, 18: 21, 19: 29, 20: 29, 21: 34, 22: 30, 23: 17, 24: 25, 25: 6, 26: 14, 27: 23, 28: 28, 29: 25, 30: 31, 31: 40, 32: 22, 33: 33, 34: 37, 35: 16, 36: 33, 37: 24, 38: 41, 39: 30, 40: 24, 41: 34, 42: 17},
    'ezekiel':       {1: 28, 2: 10, 3: 27, 4: 17, 5: 17, 6: 14, 7: 27, 8: 18, 9: 11, 10: 22, 11: 25, 12: 28, 13: 23, 14: 23, 15: 8, 16: 63, 17: 24, 18: 32, 19: 14, 20: 49, 21: 32, 22: 31, 23: 49, 24: 27, 25: 17, 26: 21, 27: 36, 28: 26, 29: 21, 30: 26, 31: 18, 32: 32, 33: 33, 34: 31, 35: 15, 36: 38, 37: 28, 38: 23, 39: 29, 40: 49, 41: 26, 42: 20, 43: 27, 44: 31, 45: 25, 46: 24, 47: 23, 48: 35},
    'jeremiah':      {1: 19, 2: 37, 3: 25, 4: 31, 5: 31, 6: 30, 7: 34, 8: 22, 9: 26, 10: 25, 11: 23, 12: 17, 13: 27, 14: 22, 15: 21, 16: 21, 17: 27, 18: 23, 19: 15, 20: 18, 21: 14, 22: 30, 23: 40, 24: 10, 25: 38, 26: 24, 27: 22, 28: 17, 29: 32, 30: 24, 31: 40, 32: 44, 33: 26, 34: 22, 35: 19, 36: 32, 37: 21, 38: 28, 39: 18, 40: 16, 41: 18, 42: 22, 43: 13, 44: 30, 45: 5, 46: 28, 47: 7, 48: 47, 49: 39, 50: 46, 51: 64, 52: 34},
}


TRANSLATION_GUIDELINES = """TRANSLATION RULES (non-negotiable):
1. Formal equivalence — word-for-word literal, not dynamic paraphrase.
2. YHWH = always translate as "YHWH" (NOT "the LORD" or "LORD"). This is a study Bible that preserves the divine name.
3. Jesus IS the promised Messiah and King — translate messianic passages accordingly.
4. Preserve Hebrew word order flavor where English allows it.
5. For unique Hebrew terms (hesed, shalom, ruach, etc.), put the transliteration in parentheses on first use.
6. Avoid modern paraphrase language. Keep a dignified, slightly elevated register.
7. The divine council is real — translate Psalm 82/Deut 32 related language accordingly.
8. Use ESV as your baseline but make it more literal and include Hebrew term parentheticals.
9. Do NOT abbreviate or summarize — every verse must be complete.
10. Genealogies and lists: translate fully, don't skip names."""

NOTE_GUIDELINES = """STUDY NOTE RULES:
- Notes use category prefixes: HEBREW:, TYPOLOGY:, HISTORICAL:, THEOLOGICAL:, DIVINE_COUNCIL:, STRUCTURE:
- HEBREW notes: explain key Hebrew terms (cite Strong's if known), word origins, nuances
- TYPOLOGY notes: Christ typology, NT fulfillment patterns
- HISTORICAL notes: ANE context, archaeological parallels, geography
- THEOLOGICAL notes: doctrinal significance, covenantal themes
- DIVINE_COUNCIL notes: heavenly assembly references, spiritual warfare, territorial spirits
- Notes for key verses only (10-30% of verses, prioritize theologically dense ones)
- Keep notes concise but substantive (2-5 sentences each)
- Cross-reference format: (Matt 5:17), (Ps 82:1), (Eph 1:10)"""


def call_claude_for_chapter(client, book_name, ch_num, verse_count, total_chapters, book_intro=''):
    """Call Claude API to generate translations + notes for one OT chapter."""

    system = f"""You are THE SCRIBE — a theological linguist generating formal equivalence translations of the Hebrew Old Testament for a study Bible app. You have deep knowledge of Biblical Hebrew, Aramaic, the Masoretic Text, Second Temple Judaism, and divine council theology.

{TRANSLATION_GUIDELINES}

{NOTE_GUIDELINES}"""

    prompt = f"""Generate a verse-by-verse translation of {book_name} chapter {ch_num} (of {total_chapters}) for our Ancient Texts Study App.

This chapter has {verse_count} verses (verses 1 through {verse_count}).

{book_intro}

OUTPUT FORMAT — respond with ONLY valid Python dict literals, NO imports, NO variable names, NO markdown code blocks. Just the raw dict structures:

TRANSLATIONS (dict mapping verse_num int to English translation string):
{{
    1: 'Translation of verse 1...',
    2: 'Translation of verse 2...',
    ...{verse_count}: 'Translation of last verse...'
}}

NOTES (dict mapping verse_num int to note string, only for significant verses):
{{
    1: 'HEBREW: explanation...',
    3: 'TYPOLOGY: explanation...',
    ...
}}

Important:
- Return EXACTLY two dicts separated by a blank line
- First dict: ALL {verse_count} verses, every verse number from 1 to {verse_count}
- Second dict: notes for 10-30% of verses (theologically significant ones)
- Use single-quoted strings. Escape internal single quotes with backslash: it\\'s
- NO newlines inside strings
- Make translations accurate, literal, dignified
- Translate from the Hebrew Masoretic Text
- Use YHWH for the divine name (tetragrammaton)"""

    response = client.messages.create(
        model='claude-sonnet-4-6',
        max_tokens=8000,
        system=system,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.content[0].text


def parse_two_dicts(raw_text):
    """Parse Claude's output: two Python dict literals."""
    raw = re.sub(r'```python\s*', '', raw_text)
    raw = re.sub(r'```\s*', '', raw)
    raw = raw.strip()

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
    data_dir = book_id
    # Check manifest for data_dir
    manifest_path = os.path.join(ROOT, 'manifest.json')
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                text = f.read()
            text = text.replace("\u201c", '"').replace("\u201d", '"')
            text = text.replace("\u2018", "'").replace("\u2019", "'")
            text = text.replace("\u00e2\u20ac\u201c", "\u2014")
            text = text.replace("\u00e2\u20ac\u201d", "\u2014")
            manifest = json.loads(text)
            for t in manifest.get('texts', []):
                if t['id'] == book_id:
                    data_dir = t.get('data_dir', book_id)
                    break
        except Exception:
            pass

    info_path = os.path.join(DATA_DIR, data_dir, 'info.py')
    if not os.path.exists(info_path):
        return ''
    try:
        spec = importlib.util.spec_from_file_location('info', info_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        info = getattr(mod, 'TEXT_INFO', {})
        desc = info.get('description', '')
        if not desc:
            # Try canonical_status detail
            cs = info.get('canonical_status', {})
            desc = cs.get('detail', '')
        if desc and len(desc) > 600:
            desc = desc[:600] + '...'
        return f'BOOK CONTEXT ({book_name}): {desc}' if desc else ''
    except Exception as e:
        print(f'  Warning: could not load info.py: {e}')
        return ''


def _write_flow_file(out_path, book_id, var_suffix, book_name, all_translations, all_notes, total_verses):
    """Write the flow file in the standard format."""
    os.makedirs(FLOW_DIR, exist_ok=True)

    total_notes = sum(len(n) for n in all_notes.values())

    lines = []
    lines.append('"""')
    lines.append(f'Flow translations for {book_name} — accurate, literal English renderings.')
    lines.append(f'Every verse of all chapters. Formal equivalence style.')
    lines.append(f'YHWH = the divine name (tetragrammaton). Original translation from the Hebrew Masoretic Text.')
    lines.append(f'Jesus Christ IS the promised Messiah and King of everything.')
    lines.append(f'Generated by generate_ot_flow.py using Claude Sonnet.')
    lines.append(f'Verses: {total_verses} | Notes: {total_notes}')
    lines.append('"""')
    lines.append('')
    lines.append(f'FLOW_{var_suffix} = {{')

    for ch_num in sorted(all_translations.keys()):
        translations = all_translations[ch_num]
        lines.append(f'    {ch_num}: {{  # Chapter {ch_num}')
        for v_num in sorted(translations.keys()):
            text = translations[v_num]
            text = text.replace('\r', '').replace('\n', ' ')
            text = text.replace('\\', '\\\\').replace("'", "\\'")
            lines.append(f"        {v_num}: '{text}',")
        lines.append('    },')

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
        lines.append('    },')

    lines.append('}')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def generate_flow_for_book(book_id, force=False):
    """Generate flow translations for a complete OT book."""
    if book_id not in OT_BOOK_MAP:
        print(f'ERROR: Unknown book: {book_id}')
        print(f'Available: {", ".join(OT_BOOK_MAP.keys())}')
        return False

    _, var_suffix, book_name, total_chapters = OT_BOOK_MAP[book_id]
    out_path = os.path.join(FLOW_DIR, f'flow_{book_id}.py')

    if os.path.exists(out_path) and not force:
        print(f'SKIP: {out_path} already exists (use --force to overwrite)')
        return True

    verse_counts = VERSE_COUNTS.get(book_id, {})
    if not verse_counts:
        print(f'ERROR: No verse counts defined for {book_id}')
        return False

    print(f'\n{"="*60}')
    print(f'GENERATING: {book_name} ({book_id})')
    total_verses = sum(verse_counts.values())
    print(f'Chapters: {total_chapters}, Verses: {total_verses}')
    print(f'{"="*60}')

    # Load book context
    book_intro = get_book_intro(book_id, book_name)

    # Claude client
    from anthropic import Anthropic
    client = Anthropic(api_key=SCRIBE_API_KEY)

    all_translations = {}
    all_notes = {}

    for ch_num in sorted(verse_counts.keys()):
        vc = verse_counts[ch_num]
        print(f'  Chapter {ch_num}/{total_chapters} ({vc} verses)...', end=' ', flush=True)

        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                raw = call_claude_for_chapter(client, book_name, ch_num, vc, total_chapters, book_intro)
                translations, notes = parse_two_dicts(raw)

                # Validate: all verses present
                expected = set(range(1, vc + 1))
                got = set(translations.keys())
                missing = expected - got
                if missing:
                    print(f'\n    WARNING: Missing verses {sorted(missing)} in chapter {ch_num}')

                all_translations[ch_num] = translations
                all_notes[ch_num] = notes
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
                    all_notes[ch_num] = {}

        # Small pause between chapters
        if ch_num < max(verse_counts.keys()):
            time.sleep(0.5)

    # Write output
    _write_flow_file(out_path, book_id, var_suffix, book_name, all_translations, all_notes, total_verses)
    print(f'\nWritten: {out_path}')

    # Validate
    ok, msg = validate_flow_file(out_path)
    if ok:
        print(f'Validated: {msg}')
    else:
        print(f'VALIDATION FAILED: {msg}')
    return True


def validate_flow_file(path):
    """Quick validation."""
    try:
        spec = importlib.util.spec_from_file_location('flow_check', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        flow_vars = [v for v in dir(mod) if v.startswith('FLOW_')]
        if not flow_vars:
            return False, 'No FLOW_ variable found'
        flow = getattr(mod, flow_vars[0])
        total_verses = sum(len(ch) for ch in flow.values())
        notes_vars = [v for v in dir(mod) if v.startswith('NOTES_')]
        total_notes = 0
        if notes_vars:
            notes = getattr(mod, notes_vars[0])
            total_notes = sum(len(ch) for ch in notes.values())
        return True, f'{total_verses} verses, {total_notes} notes'
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser(description='Generate OT flow translations using Claude API')
    parser.add_argument('--book', type=str, help='Book ID (e.g., jeremiah, hosea)')
    parser.add_argument('--all', action='store_true', help='Generate all 24 OT books')
    parser.add_argument('--start-from', type=str, help='When using --all, start from this book ID')
    parser.add_argument('--force', action='store_true', help='Overwrite existing files')
    parser.add_argument('--validate', type=str, help='Validate an existing flow file')
    args = parser.parse_args()

    if args.validate:
        ok, msg = validate_flow_file(args.validate)
        print(f'{"OK" if ok else "FAIL"}: {msg}')
        return

    if args.book:
        generate_flow_for_book(args.book, force=args.force)
    elif args.all:
        start = False if args.start_from else True
        for book_id, _, book_name, _ in OT_BOOKS_ORDERED:
            if not start:
                if book_id == args.start_from:
                    start = True
                else:
                    continue
            print(f'\n--- Starting {book_name} ---')
            generate_flow_for_book(book_id, force=args.force)
        print('\n\nALL DONE!')
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
