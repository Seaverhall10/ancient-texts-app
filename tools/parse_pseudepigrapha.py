"""
parse_pseudepigrapha.py -- Parse Ascension of Isaiah and Letter of Aristeas
from pseudepigrapha.com HTML into flow file format.

Usage:
  python tools/parse_pseudepigrapha.py ascension
  python tools/parse_pseudepigrapha.py aristeas
  python tools/parse_pseudepigrapha.py all
"""
import os
import sys
import re
import html as html_mod

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOW_DIR = os.path.join(BASE_DIR, "data", "flow")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")


def strip_html(text):
    """Remove HTML tags and decode entities."""
    text = re.sub(r'<[^>]+>', '', text)
    text = html_mod.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def parse_ascension():
    """Parse Ascension of Isaiah (chapters 6-11) from HTML."""
    html_path = os.path.join(TOOLS_DIR, "ascension_raw.html")
    with open(html_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Extract body text
    body_match = re.search(r'<body[^>]*>(.*?)</body>', raw, re.DOTALL | re.IGNORECASE)
    if not body_match:
        body_match = re.search(r'<BODY[^>]*>(.*?)</BODY>', raw, re.DOTALL)
    text = strip_html(body_match.group(1) if body_match else raw)

    # Find chapters 6-11
    chapters = {}
    # Split by chapter markers: "6." "7." etc. at start of sentence
    # The text uses patterns like "7. The vision which Isaiah saw"
    chapter_splits = re.split(r'(?:^|\s)(\d{1,2})\.\s+(?=[A-Z])', text)

    # Parse chapter splits
    current_ch = None
    current_text = ""

    for i, part in enumerate(chapter_splits):
        if re.match(r'^\d{1,2}$', part.strip()):
            ch_num = int(part.strip())
            if 6 <= ch_num <= 11:
                if current_ch is not None:
                    chapters[current_ch] = current_text
                current_ch = ch_num
                current_text = ""
        elif current_ch is not None:
            current_text += part

    if current_ch is not None:
        chapters[current_ch] = current_text

    # Now parse verses within each chapter
    all_chapters = {}
    for ch_num, ch_text in chapters.items():
        verses = {}
        # First verse is the chapter opening (no number prefix)
        # Subsequent verses start with a number: "2And he sat" or "2 And he sat"
        parts = re.split(r'(?<=[.?!"\u2019\u201d])\s*(\d{1,2})(?=[A-Z]|\s+[A-Z])', ch_text)

        # First part is verse 1
        if parts[0].strip():
            verses[1] = parts[0].strip()

        # Rest are verse_num, verse_text pairs
        i = 1
        while i < len(parts) - 1:
            v_num = int(parts[i])
            v_text = parts[i + 1].strip() if i + 1 < len(parts) else ""
            if v_text:
                verses[v_num] = v_text
            i += 2

        if verses:
            all_chapters[ch_num] = verses
            print(f"  Chapter {ch_num}: {len(verses)} verses")

    return all_chapters


def parse_aristeas():
    """Parse Letter of Aristeas from HTML. Continuous numbered paragraphs 1-322."""
    html_path = os.path.join(TOOLS_DIR, "aristeas_raw.html")
    with open(html_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Extract body text
    body_match = re.search(r'<body[^>]*>(.*?)</body>', raw, re.DOTALL | re.IGNORECASE)
    if not body_match:
        body_match = re.search(r'<BODY[^>]*>(.*?)</BODY>', raw, re.DOTALL)
    text = strip_html(body_match.group(1) if body_match else raw)

    # Remove header info (title, editor, etc.)
    # Find where paragraph 1 starts: "SINCE I have collected"
    start = text.find('SINCE I have collected')
    if start == -1:
        start = 0
    text = text[start:]

    # Split into numbered paragraphs
    # Pattern: number at start or after sentence end
    parts = re.split(r'(?:^|\s)(\d{1,3})\s+(?=[A-Z])', text)

    paragraphs = {}
    # First part before any number is paragraph 1 (starts with "SINCE")
    if parts[0].strip():
        paragraphs[1] = parts[0].strip()

    i = 1
    while i < len(parts) - 1:
        try:
            p_num = int(parts[i])
            p_text = parts[i + 1].strip()
            if p_text and p_num > 0:
                paragraphs[p_num] = p_text
        except ValueError:
            pass
        i += 2

    print(f"  Found {len(paragraphs)} paragraphs")

    # Group into chapters of ~30 paragraphs each for our system
    # Thematic groupings based on content:
    # Ch 1: 1-50 (Introduction, context, embassy proposal)
    # Ch 2: 51-100 (Gifts, journey preparations)
    # Ch 3: 101-150 (Description of Jerusalem, Temple)
    # Ch 4: 151-200 (Banquet questions part 1)
    # Ch 5: 201-250 (Banquet questions part 2)
    # Ch 6: 251-300 (Banquet questions part 3, translation work)
    # Ch 7: 301-322 (Translation completion, conclusion)
    chapter_ranges = [
        (1, 1, 50),
        (2, 51, 100),
        (3, 101, 150),
        (4, 151, 200),
        (5, 201, 250),
        (6, 251, 300),
        (7, 301, 350),  # Will naturally end at max paragraph
    ]

    all_chapters = {}
    for ch_num, start_p, end_p in chapter_ranges:
        ch_verses = {}
        v_counter = 1
        for p_num in range(start_p, end_p + 1):
            if p_num in paragraphs:
                ch_verses[v_counter] = paragraphs[p_num]
                v_counter += 1
        if ch_verses:
            all_chapters[ch_num] = ch_verses
            print(f"  Chapter {ch_num} (para {start_p}-{end_p}): {len(ch_verses)} verses")

    return all_chapters


def write_flow_file(text_id, name, doc, source, all_chapters):
    """Write a flow file."""
    var_name = f"FLOW_{text_id.upper()}"
    out_path = os.path.join(FLOW_DIR, f"flow_{text_id}.py")

    total_verses = sum(len(ch) for ch in all_chapters.values())
    total_chapters = len(all_chapters)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f'"""\n')
        f.write(f'Flow translations for {name} -- complete text.\n')
        f.write(f'{source}.\n\n')
        f.write(f'{doc}\n')
        f.write(f'Chapters: {total_chapters} | Verses: {total_verses}\n')
        f.write(f'"""\n\n')
        f.write(f'{var_name} = {{\n')

        for ch_num in sorted(all_chapters.keys()):
            ch_verses = all_chapters[ch_num]
            f.write(f'    {ch_num}: {{  # Chapter {ch_num}\n')
            for v_num in sorted(ch_verses.keys()):
                v_text = ch_verses[v_num].replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v_num}: '{v_text}',\n")
            f.write(f'    }},\n')

        f.write(f'}}\n')

    print(f"  -> Wrote {out_path} ({total_chapters} chapters, {total_verses} verses)")


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_pseudepigrapha.py <ascension|aristeas|all>")
        sys.exit(1)

    target = sys.argv[1]

    if target in ("ascension", "all"):
        print("\n=== Parsing Ascension of Isaiah ===")
        chapters = parse_ascension()
        if chapters:
            write_flow_file(
                "ascension_isaiah",
                "Ascension of Isaiah",
                "An apocalyptic text in which Isaiah is taken on a tour through\n"
                "the seven heavens, witnessing the divine council, the Beloved's\n"
                "descent, and the incarnation. The Vision (ch. 6-11) describes\n"
                "Christ's descent through the heavens in disguise and his\n"
                "crucifixion, resurrection, and ascension. Contains early\n"
                "Trinitarian imagery (the Lord, the Beloved, and the Angel of\n"
                "the Holy Spirit). Composite work: Martyrdom (ch. 1-5) + Vision\n"
                "(ch. 6-11). This edition contains the Vision portion.\n",
                "M.A. Knibb translation, from Charlesworth OTP vol. 2 (public domain text via pseudepigrapha.com)",
                chapters,
            )

    if target in ("aristeas", "all"):
        print("\n=== Parsing Letter of Aristeas ===")
        chapters = parse_aristeas()
        if chapters:
            write_flow_file(
                "letter_aristeas",
                "Letter of Aristeas",
                "A Hellenistic Jewish text (c. 2nd century BC) describing how the\n"
                "Torah was translated into Greek (the Septuagint/LXX). Written as\n"
                "a letter from Aristeas, a courtier of Ptolemy II Philadelphus,\n"
                "to his brother Philocrates. Includes descriptions of Jerusalem,\n"
                "the Temple, and extended philosophical dialogues at royal banquets.\n"
                "Key for understanding how Diaspora Jews viewed their scriptures\n"
                "and their relationship with Hellenistic culture.\n",
                "R.H. Charles edition (1913, public domain) via pseudepigrapha.com",
                chapters,
            )


if __name__ == "__main__":
    main()
