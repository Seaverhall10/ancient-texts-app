"""
fetch_jasher.py -- Fetch Book of Jasher from CCEL (1840 translation, public domain)
and convert to flow file format.

Usage: python tools/fetch_jasher.py
"""
import os
import sys
import re
import time
import urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "flow", "flow_jasher.py")
BASE_URL = "https://www.ccel.org/a/anonymous/jasher/{ch}.htm"


def fetch_chapter(ch_num):
    """Fetch and parse a single Jasher chapter from CCEL."""
    url = BASE_URL.format(ch=ch_num)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"  Ch {ch_num} fetch failed: {e}")
        return {}

    # Remove HTML tags but preserve line breaks
    text = re.sub(r'<br\s*/?>', '\n', html, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&quot;', '"').replace('&#39;', "'").replace('&nbsp;', ' ')

    # Parse verses: look for patterns like "1. text" or just numbered paragraphs
    verses = {}
    lines = text.split('\n')
    current_verse = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Skip navigation, headers, chapter titles
        if re.match(r'^Jasher Chapter', line, re.IGNORECASE):
            continue
        if re.match(r'^THE BOOK OF JASHER', line, re.IGNORECASE):
            continue
        if re.match(r'^\d+\s*\|\s*\d+', line):  # navigation links
            continue
        if len(line) < 10 and not re.match(r'^\d+', line):
            continue

        # Try to match verse number at start
        v_match = re.match(r'^(\d+)\.\s*(.+)', line)
        if not v_match:
            v_match = re.match(r'^(\d+)\s+([A-Z].+)', line)

        if v_match:
            v_num = int(v_match.group(1))
            v_text = v_match.group(2).strip()
            current_verse = v_num
            verses[v_num] = v_text
        elif current_verse > 0 and line and not line.startswith('Chapter'):
            # Continuation of previous verse
            if current_verse in verses:
                verses[current_verse] += ' ' + line

    return verses


def main():
    print("Fetching Book of Jasher from CCEL...")
    print("Source: 1840 English translation (public domain)\n")

    chapters = {}
    total_verses = 0

    for ch in range(1, 92):
        verses = fetch_chapter(ch)
        if verses:
            chapters[ch] = verses
            total_verses += len(verses)
            print(f"  Ch {ch}: {len(verses)} verses")
        else:
            print(f"  Ch {ch}: EMPTY")
        time.sleep(0.3)

    print(f"\nTotal: {len(chapters)} chapters, {total_verses} verses")

    if not chapters:
        print("ERROR: No chapters retrieved.")
        sys.exit(1)

    # Write flow file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Flow translations for Book of Jasher (chapters 1-91) -- complete text.\n')
        f.write('1840 English translation (public domain), sourced from CCEL.\n')
        f.write('\n')
        f.write('Also known as Sefer HaYashar ("Book of the Upright"), referenced in\n')
        f.write('Joshua 10:13 and 2 Samuel 1:18. This 1840 translation claims to derive\n')
        f.write('from a Hebrew manuscript but its provenance is debated. Regardless of\n')
        f.write('origin, it preserves traditions that parallel and expand Genesis through\n')
        f.write('Joshua with details found nowhere else: named wives of patriarchs,\n')
        f.write('expanded wars, detailed chronologies, and the youth of Abraham.\n')
        f.write('\n')
        f.write(f'Chapters: {len(chapters)} | Verses: {total_verses}\n')
        f.write('"""\n\n')

        f.write('FLOW_JASHER = {\n')
        for ch_num in sorted(chapters.keys()):
            vv = chapters[ch_num]
            f.write(f'    {ch_num}: {{  # Chapter {ch_num}\n')
            for v_num in sorted(vv.keys()):
                text = vv[v_num].replace("\\", "\\\\").replace("'", "\\'")
                # Clean up any remaining artifacts
                text = re.sub(r'\s+', ' ', text).strip()
                f.write(f"        {v_num}: '{text}',\n")
            f.write('    },\n')
        f.write('}\n\n')
        f.write('NOTES_JASHER = {}\n')

    print(f"\nWritten: {OUTPUT_FILE}")
    print(f"File size: {os.path.getsize(OUTPUT_FILE):,} bytes")


if __name__ == "__main__":
    main()
