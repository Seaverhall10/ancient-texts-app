"""
parse_jasher_pdf.py -- Extract Book of Jasher from PDF and convert to flow file.
Requires: pip install PyPDF2
"""
import os
import sys
import re
import PyPDF2

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PDF_PATH = os.path.join(os.path.dirname(__file__), "jasher.pdf")
OUTPUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "flow", "flow_jasher.py")


def main():
    print("Parsing Jasher PDF...")

    with open(PDF_PATH, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        print(f"  Pages: {len(reader.pages)}")

        # Extract all text from page 35 onward (where ch 1 starts)
        full_text = ""
        for i in range(35, len(reader.pages)):
            page_text = reader.pages[i].extract_text()
            if page_text:
                full_text += page_text + "\n"

    print(f"  Extracted: {len(full_text):,} chars")

    # Parse into chapters and verses
    chapters = {}
    current_ch = 0
    current_verse = 0

    # Split by lines
    lines = full_text.split('\n')
    buffer = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Detect chapter header: "Jasher Chapter N" or "CHAPTER N"
        ch_match = re.match(r'(?:Jasher\s+)?Chapter\s+(\d+)', line, re.IGNORECASE)
        if ch_match:
            # Save buffered verse
            if buffer and current_ch > 0 and current_verse > 0:
                if current_ch not in chapters:
                    chapters[current_ch] = {}
                chapters[current_ch][current_verse] = buffer.strip()
                buffer = ""

            current_ch = int(ch_match.group(1))
            current_verse = 0
            if current_ch not in chapters:
                chapters[current_ch] = {}
            continue

        if current_ch == 0:
            continue

        # Skip known non-content lines
        if line.startswith('THE BOOK OF JASHER'):
            continue
        if re.match(r'^THIS IS THE BOOK', line):
            continue
        if re.match(r'^UPON THE EARTH', line):
            continue
        if re.match(r'^MADE HEAVEN', line):
            continue

        # Detect verse: "N. text" or "N.text"
        v_match = re.match(r'^(\d+)\.\s*(.+)', line)
        if v_match:
            # Save previous verse
            if buffer and current_verse > 0:
                chapters[current_ch][current_verse] = buffer.strip()

            current_verse = int(v_match.group(1))
            buffer = v_match.group(2)
        else:
            # Continuation line
            if buffer:
                buffer += " " + line
            elif current_verse > 0:
                buffer = line

    # Save last verse
    if buffer and current_ch > 0 and current_verse > 0:
        chapters[current_ch][current_verse] = buffer.strip()

    # Clean up verses
    for ch in chapters:
        for v in chapters[ch]:
            text = chapters[ch][v]
            text = re.sub(r'\s+', ' ', text).strip()
            chapters[ch][v] = text

    total_verses = sum(len(v) for v in chapters.values())
    print(f"  Chapters: {len(chapters)}, Verses: {total_verses}")

    # Show chapter breakdown
    for ch in sorted(chapters.keys()):
        n = len(chapters[ch])
        if n > 0:
            print(f"    Ch {ch}: {n} verses")

    # Write flow file
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Flow translations for Book of Jasher (chapters 1-91) -- complete text.\n')
        f.write('1840 English translation (public domain), extracted from PDF.\n')
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
                f.write(f"        {v_num}: '{text}',\n")
            f.write('    },\n')
        f.write('}\n\n')
        f.write('NOTES_JASHER = {}\n')

    print(f"\n  Written: {OUTPUT}")
    print(f"  File size: {os.path.getsize(OUTPUT):,} bytes")


if __name__ == "__main__":
    main()
