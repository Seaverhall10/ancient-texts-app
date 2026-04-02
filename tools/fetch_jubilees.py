"""
fetch_jubilees.py -- Fetch Book of Jubilees from Sefaria API (R.H. Charles translation)
and convert to flow file format.

Usage: python tools/fetch_jubilees.py
Output: data/flow/flow_jubilees.py
"""
import os
import sys
import json
import time
import re
import urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "flow", "flow_jubilees.py")
BASE_URL = "https://www.sefaria.org/api/texts/Book_of_Jubilees.{ch}?context=0"


def fetch_chapter(ch_num):
    """Fetch a single chapter from Sefaria API."""
    url = BASE_URL.format(ch=ch_num)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        verses = data.get('text', [])
        if isinstance(verses, list):
            return verses
    except Exception as e:
        print(f"  Ch {ch_num} failed: {e}")
    return []


def clean_verse(text):
    """Clean HTML and normalize verse text."""
    if not text or not isinstance(text, str):
        return ''
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove A.M. annotations inline
    text = text.replace('(A.M. = Anno Mundi) ', '')
    text = text.replace('(A.M. = Anno Mundi)', '')
    return text


def main():
    print("Fetching Book of Jubilees from Sefaria API...")
    print("Source: R.H. Charles translation (public domain)\n")

    chapters = {}
    total_verses = 0

    for ch in range(1, 51):
        verses_raw = fetch_chapter(ch)
        if not verses_raw:
            print(f"  Ch {ch}: EMPTY (skipping)")
            continue

        verses = {}
        for i, v_text in enumerate(verses_raw):
            cleaned = clean_verse(v_text)
            if cleaned:
                verses[i + 1] = cleaned

        if verses:
            chapters[ch] = verses
            total_verses += len(verses)
            print(f"  Ch {ch}: {len(verses)} verses")
        else:
            print(f"  Ch {ch}: no valid verses")

        # Rate limit: be polite to the API
        time.sleep(0.3)

    print(f"\nTotal: {len(chapters)} chapters, {total_verses} verses")

    if len(chapters) < 40:
        print("ERROR: Too few chapters retrieved. Aborting.")
        sys.exit(1)

    # Write flow file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Flow translations for Book of Jubilees (chapters 1-50) -- complete text.\n')
        f.write('R.H. Charles translation (public domain), sourced via Sefaria API.\n')
        f.write('\n')
        f.write('Also known as "The Little Genesis," Jubilees retells Genesis and Exodus\n')
        f.write('through the angel of the presence dictating to Moses on Mount Sinai.\n')
        f.write('Key distinctive elements: the 364-day solar calendar, jubilee dating\n')
        f.write('system (49-year cycles), named women in genealogies, expanded Watcher\n')
        f.write('tradition, Mastema as adversary figure, and detailed halakhic rulings.\n')
        f.write('\n')
        f.write("The text survives complete only in Ge'ez (Ethiopic), with fragments\n")
        f.write('found at Qumran (4Q216-228, 11Q12) confirming its antiquity (2nd c. BC).\n')
        f.write('Jubilees was authoritative at Qumran and remains canonical in the\n')
        f.write('Ethiopian Orthodox Church.\n')
        f.write('\n')
        f.write(f'Chapters: {len(chapters)} | Verses: {total_verses}\n')
        f.write('"""\n\n')

        f.write('FLOW_JUBILEES = {\n')
        for ch_num in sorted(chapters.keys()):
            vv = chapters[ch_num]
            f.write(f'    {ch_num}: {{  # Chapter {ch_num}\n')
            for v_num in sorted(vv.keys()):
                # Escape single quotes in verse text
                text = vv[v_num].replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v_num}: '{text}',\n")
            f.write('    },\n')
        f.write('}\n\n')
        f.write('NOTES_JUBILEES = {}\n')

    print(f"\nWritten: {OUTPUT_FILE}")
    print(f"File size: {os.path.getsize(OUTPUT_FILE):,} bytes")


if __name__ == "__main__":
    main()
