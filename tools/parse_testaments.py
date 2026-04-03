"""
parse_testaments.py -- Parse Testaments of the Twelve Patriarchs from
earlychristianwritings.com HTML into flow file format.

Each testament becomes one chapter. Verses are numbered sequentially
within each testament (combining all internal chapters).

Usage:
  python tools/parse_testaments.py
"""
import os
import sys
import re
import html as html_mod

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOW_DIR = os.path.join(BASE_DIR, "data", "flow")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")

# The 12 patriarchs in order
PATRIARCHS = [
    "Reuben", "Simeon", "Levi", "Judah", "Issachar", "Zebulun",
    "Dan", "Naphtali", "Gad", "Asher", "Joseph", "Benjamin",
]


def strip_html(text):
    """Remove HTML tags and decode entities."""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html_mod.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def parse_testaments():
    """Parse all 12 testaments from the HTML file."""
    html_path = os.path.join(TOOLS_DIR, "testaments_raw.html")
    with open(html_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    all_chapters = {}

    for ch_idx, patriarch in enumerate(PATRIARCHS, 1):
        # Find this testament's section
        # Pattern: "TESTAMENT OF REUBEN" or "REUBEN, THE FIRST-BORN SON"
        pat_name = patriarch.upper()
        start_idx = raw.find(pat_name)
        if start_idx == -1:
            print(f"  WARNING: Could not find Testament of {patriarch}")
            continue

        # Find end: start of next testament or end of document
        end_idx = len(raw)
        if ch_idx < len(PATRIARCHS):
            next_pat = PATRIARCHS[ch_idx].upper()
            # Search for the next patriarch's testament header
            # Look for the pattern more carefully
            search_from = start_idx + 100
            next_idx = raw.find(next_pat, search_from)
            if next_idx > -1:
                # Back up to find the preceding section break
                end_idx = next_idx

        section_html = raw[start_idx:end_idx]
        section_text = strip_html(section_html)

        # Extract verses: they're marked by inline numbers
        # Pattern: bold chapter numbers <B>1</B> then verse numbers inline
        # In the plaintext, verses appear as: "1 text 2 text 3 text"
        # Chapter breaks within a testament: the bold numbers reset verse counting

        # Simple approach: find all numbers followed by text
        # Split on verse numbers that appear after sentence endings
        verses = {}
        verse_counter = 1

        # Remove the title/header portion
        # Find where actual verse text starts (after "1 1 The copy" or similar)
        first_verse = re.search(r'\b1\s+1\s+', section_text)
        if first_verse:
            section_text = section_text[first_verse.start():]

        # Split by numbers that start a new verse
        # Verses are marked by numbers after sentence-ending punctuation
        # or at the start of bold chapter markers
        parts = re.split(r'(?<=[.!?"\u2019])\s+(\d{1,2})\s+(?=[A-Z])', section_text)

        # Process parts
        if parts[0].strip():
            # First part - may contain chapter number + verse 1
            first_text = parts[0].strip()
            # Remove leading chapter/verse numbers like "1 1"
            first_text = re.sub(r'^\d+\s+\d+\s+', '', first_text)
            if not first_text:
                first_text = re.sub(r'^\d+\s+', '', parts[0].strip())
            if first_text and len(first_text) > 10:
                verses[verse_counter] = first_text
                verse_counter += 1

        i = 1
        while i < len(parts) - 1:
            v_num_str = parts[i]
            v_text = parts[i + 1].strip() if i + 1 < len(parts) else ""
            if v_text and len(v_text) > 5:
                # Clean up: remove internal chapter markers (bold numbers)
                v_text = re.sub(r'^\d+\s+', '', v_text)  # Remove leading chapter nums
                verses[verse_counter] = v_text
                verse_counter += 1
            i += 2

        if verses:
            all_chapters[ch_idx] = verses
            print(f"  Testament of {patriarch} (ch {ch_idx}): {len(verses)} verses")
        else:
            print(f"  WARNING: No verses found for Testament of {patriarch}")

    return all_chapters


def write_flow_file(all_chapters):
    """Write the flow file."""
    out_path = os.path.join(FLOW_DIR, "flow_testaments_12.py")
    total_verses = sum(len(ch) for ch in all_chapters.values())
    total_chapters = len(all_chapters)

    patriarch_list = ", ".join(PATRIARCHS)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f'"""\n')
        f.write(f'Flow translations for Testaments of the Twelve Patriarchs -- complete text.\n')
        f.write(f'R.H. Charles translation (1908, public domain) via earlychristianwritings.com.\n\n')
        f.write(f'Each of the twelve sons of Jacob gives a deathbed testament to his\n')
        f.write(f'descendants, confessing sins, teaching virtues, and prophesying the\n')
        f.write(f'future. Major themes: the Two Ways (virtue vs. vice), messianic\n')
        f.write(f'expectations (Messiah from Levi and Judah), and spiritual warfare.\n')
        f.write(f'Significant for NT background: the Two Ways doctrine (Didache),\n')
        f.write(f'virtue/vice catalogs (Pauline epistles), and Levi-Judah messianism.\n')
        f.write(f'Composite text with Jewish core and possible Christian interpolations.\n\n')
        f.write(f'Patriarchs: {patriarch_list}\n')
        f.write(f'Each patriarch = one chapter. Verses numbered sequentially within.\n\n')
        f.write(f'Chapters: {total_chapters} | Verses: {total_verses}\n')
        f.write(f'"""\n\n')
        f.write(f'FLOW_TESTAMENTS_12 = {{\n')

        for ch_num in sorted(all_chapters.keys()):
            patriarch = PATRIARCHS[ch_num - 1] if ch_num <= len(PATRIARCHS) else f"Ch{ch_num}"
            ch_verses = all_chapters[ch_num]
            f.write(f'    {ch_num}: {{  # Testament of {patriarch}\n')
            for v_num in sorted(ch_verses.keys()):
                v_text = ch_verses[v_num].replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v_num}: '{v_text}',\n")
            f.write(f'    }},\n')

        f.write(f'}}\n')

    print(f"\n  -> Wrote {out_path} ({total_chapters} testaments, {total_verses} verses)")


def main():
    print("=== Parsing Testaments of the Twelve Patriarchs ===")
    chapters = parse_testaments()
    if chapters:
        write_flow_file(chapters)
    else:
        print("ERROR: No chapters parsed!")


if __name__ == "__main__":
    main()
