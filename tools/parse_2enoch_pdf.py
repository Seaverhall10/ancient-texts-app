"""
parse_2enoch_pdf.py -- Extract 2 Enoch (Morfill/Charles 1896) from PDF.
"""
import os
import sys
import re
import PyPDF2

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PDF_PATH = os.path.join(os.path.dirname(__file__), "2enoch_morfill.pdf")
OUTPUT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "flow", "flow_2enoch.py")


def main():
    print("Parsing 2 Enoch PDF...")

    with open(PDF_PATH, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        full_text = ""
        for p in reader.pages:
            t = p.extract_text() or ""
            full_text += t + "\n"

    print(f"  Extracted: {len(full_text):,} chars")

    chapters = {}
    current_ch = 0
    current_v = 0
    buffer = ""

    for line in full_text.split("\n"):
        line = line.strip()
        if not line:
            continue

        ch_match = re.match(r'^Chapter\s+(\d+)\s*[,.]?\s*$', line)
        if ch_match:
            if buffer and current_ch > 0 and current_v > 0:
                if current_ch not in chapters:
                    chapters[current_ch] = {}
                chapters[current_ch][current_v] = re.sub(r'\s+', ' ', buffer).strip()
                buffer = ""
            current_ch = int(ch_match.group(1))
            current_v = 0
            if current_ch not in chapters:
                chapters[current_ch] = {}
            continue

        if current_ch == 0:
            continue

        # Skip header lines
        if '2 (Slavonic) Enoch' in line:
            continue
        if '(English translation' in line:
            continue

        v_match = re.match(r'^(\d+)\s+(.+)', line)
        if v_match:
            candidate_v = int(v_match.group(1))
            if candidate_v <= current_v + 5 and candidate_v > 0:
                if buffer and current_v > 0:
                    chapters[current_ch][current_v] = re.sub(r'\s+', ' ', buffer).strip()
                current_v = candidate_v
                buffer = v_match.group(2)
                continue

        if buffer:
            buffer += " " + line
        elif current_v > 0:
            buffer = line

    # Save last
    if buffer and current_ch > 0 and current_v > 0:
        chapters[current_ch][current_v] = re.sub(r'\s+', ' ', buffer).strip()

    total = sum(len(v) for v in chapters.values())
    print(f"  Chapters: {len(chapters)}, Verses: {total}")

    for ch in sorted(chapters.keys()):
        print(f"    Ch {ch}: {len(chapters[ch])} verses")

    # Write flow file
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Flow translations for 2 Enoch (Slavonic Enoch / Book of the Secrets of Enoch).\n')
        f.write('W.R. Morfill translation, edited by R.H. Charles (1896, public domain).\n')
        f.write('\n')
        f.write('Also known as the Book of the Secrets of Enoch. Enoch is taken through\n')
        f.write('the seven heavens, sees the fallen Watchers imprisoned, the righteous\n')
        f.write('in paradise, and the terrible punishments of sinners. He receives\n')
        f.write('revelations about creation, the calendar, and the end times, then\n')
        f.write('returns to earth to instruct his sons before his final translation.\n')
        f.write('Survives only in Old Slavonic manuscripts (shorter recension A used).\n')
        f.write('\n')
        f.write(f'Chapters: {len(chapters)} | Verses: {total}\n')
        f.write('"""\n\n')

        f.write('FLOW_2ENOCH = {\n')
        for ch_num in sorted(chapters.keys()):
            vv = chapters[ch_num]
            f.write(f'    {ch_num}: {{  # Chapter {ch_num}\n')
            for v_num in sorted(vv.keys()):
                text = vv[v_num].replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v_num}: '{text}',\n")
            f.write('    },\n')
        f.write('}\n\n')
        f.write('NOTES_2ENOCH = {}\n')

    print(f"\n  Written: {OUTPUT}")
    print(f"  File size: {os.path.getsize(OUTPUT):,} bytes")


if __name__ == "__main__":
    main()
