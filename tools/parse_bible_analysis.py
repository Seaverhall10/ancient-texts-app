"""
parse_bible_analysis.py — Convert bible_study_reference.html book cards
into a structured Python data file (data/bible_analysis.py).

One-time conversion tool. Reads the HTML, extracts filter bar, section
headers, and 70 book cards into a clean data structure.

Usage: python tools/parse_bible_analysis.py
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(BASE_DIR, "docs", "bible_study_reference.html")
OUT_PATH = os.path.join(BASE_DIR, "data", "bible_analysis.py")


def parse():
    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Extract lines 228-558 (0-indexed: 227-557)
    chunk = ''.join(lines[227:558])

    # ── 1. Parse filters ──
    filters = []
    for m in re.finditer(r"toggleFilter\('([A-Z]+)'\)\">(.*?)</button>", chunk):
        code, label = m.group(1), m.group(2)
        if code != 'all':
            filters.append({"code": code, "label": label})
    print(f"  Filters: {len(filters)}")

    # ── 2. Parse section headers ──
    sections = []
    for m in re.finditer(r'<h2 class="section-header"[^>]*id="([^"]*)"[^>]*>(.*?)</h2>', chunk):
        sections.append({"id": m.group(1), "title": m.group(2)})
    print(f"  Sections: {len(sections)}")

    # ── 3. Parse book cards ──
    books = extract_cards_line_by_line(lines[227:558])

    print(f"  Books: {len(books)}")
    return filters, sections, books


def extract_cards_line_by_line(lines):
    """Most reliable: walk lines, find card boundaries."""
    chunk = ''.join(lines)
    books = []
    current_section = None

    # Find all section headers
    for m in re.finditer(r'<h2 class="section-header"[^>]*id="([^"]*)"', chunk):
        pass  # just checking they exist

    # Split by book-card divs
    # Find start positions of each card
    card_starts = [(m.start(), m) for m in re.finditer(
        r'<div class="book-card" id="([^"]*)" data-themes="([^"]*)">', chunk
    )]
    section_positions = [(m.start(), m.group(1)) for m in re.finditer(
        r'<h2 class="section-header"[^>]*id="([^"]*)"', chunk
    )]

    # Build section map
    all_positions = [(pos, 'section', sid) for pos, sid in section_positions]
    all_positions += [(pos, 'card', m) for pos, m in card_starts]
    all_positions.sort(key=lambda x: x[0])

    current_section = None
    for idx, (pos, ptype, data) in enumerate(all_positions):
        if ptype == 'section':
            current_section = data
            continue

        # It's a card
        card_match = data
        card_id = card_match.group(1)
        card_themes = card_match.group(2)

        # Find card end — next card or section start, or end of chunk
        card_start = pos
        card_end = len(chunk)
        for next_pos, _, _ in all_positions[idx + 1:]:
            card_end = next_pos
            break

        card_html = chunk[card_start:card_end]

        # Extract header
        header_m = re.search(r'<h3>(.*?)</h3>', card_html)
        title = header_m.group(1) if header_m else card_id

        meta_m = re.search(r'<span class="meta">(.*?)</span>', card_html, re.DOTALL)
        meta_html = meta_m.group(1) if meta_m else ''

        # Extract body
        body_m = re.search(r'<div class="book-body">(.*?)</div>\s*</div>\s*$', card_html, re.DOTALL)
        if not body_m:
            body_m = re.search(r'<div class="book-body">(.*)', card_html, re.DOTALL)
        body_html = body_m.group(1).strip() if body_m else ''
        # Clean trailing </div> tags
        body_html = re.sub(r'\s*</div>\s*</div>\s*$', '', body_html).strip()

        book = {
            "id": card_id,
            "section": current_section,
            "title": title,
            "themes": card_themes,
            "meta_html": meta_html,
            "body_html": body_html,
        }
        parse_meta(book)
        books.append(book)

    return books


def parse_meta(book):
    """Extract era_count, chapters, grade from meta_html."""
    meta = book.get("meta_html", "")
    # Clean HTML
    meta_text = re.sub(r'<[^>]+>', '', meta).strip()
    book["meta_text"] = meta_text

    # Try to extract structured fields
    era_m = re.search(r'(\d+)\s+era\s+files?', meta_text)
    ch_m = re.search(r'(\d+)\s+chapters?', meta_text)
    grade_m = re.search(r'Grade:\s*([A-F][+-]?)', meta_text)

    if era_m:
        book["era_count"] = int(era_m.group(1))
    if ch_m:
        book["chapters"] = int(ch_m.group(1))
    if grade_m:
        book["grade"] = grade_m.group(1)

    # Remove meta_html (we have meta_text and structured fields)
    del book["meta_html"]


def write_output(filters, sections, books):
    """Write data/bible_analysis.py."""
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('bible_analysis.py — Structured data for the Bible Analysis tab.\n')
        f.write(f'Contains {len(books)} book entries across {len(sections)} sections.\n')
        f.write('Parsed from docs/bible_study_reference.html.\n')
        f.write('"""\n\n')

        # Filters
        f.write('THEME_FILTERS = [\n')
        for filt in filters:
            f.write(f'    {{"code": {repr(filt["code"])}, "label": {repr(filt["label"])}}},\n')
        f.write(']\n\n')

        # Sections
        f.write('BOOK_SECTIONS = [\n')
        for sec in sections:
            f.write(f'    {{"id": {repr(sec["id"])}, "title": {repr(sec["title"])}}},\n')
        f.write(']\n\n')

        # Books
        f.write('BOOK_ENTRIES = [\n')
        for book in books:
            f.write('    {\n')
            f.write(f'        "id": {repr(book["id"])},\n')
            f.write(f'        "section": {repr(book["section"])},\n')
            f.write(f'        "title": {repr(book["title"])},\n')
            f.write(f'        "themes": {repr(book["themes"])},\n')
            if "era_count" in book:
                f.write(f'        "era_count": {book["era_count"]},\n')
            if "chapters" in book:
                f.write(f'        "chapters": {book["chapters"]},\n')
            if "grade" in book:
                f.write(f'        "grade": {repr(book["grade"])},\n')
            f.write(f'        "meta_text": {repr(book["meta_text"])},\n')
            # Write body_html as a triple-quoted string for readability
            body = book["body_html"]
            # Escape any triple quotes in the body
            body_escaped = body.replace('\\', '\\\\').replace("'''", "\\'\\'\\'" )
            f.write(f"        \"body_html\": '''{body_escaped}''',\n")
            f.write('    },\n')
        f.write(']\n\n')

        # Top-level export
        f.write('BIBLE_ANALYSIS = {\n')
        f.write('    "filters": THEME_FILTERS,\n')
        f.write('    "sections": BOOK_SECTIONS,\n')
        f.write('    "books": BOOK_ENTRIES,\n')
        f.write('}\n')

    print(f"  -> Wrote {OUT_PATH}")
    print(f"     {len(filters)} filters, {len(sections)} sections, {len(books)} books")


def main():
    print("=== Parsing Bible Analysis from HTML ===")
    filters, sections, books = parse()
    if books:
        write_output(filters, sections, books)
    else:
        print("ERROR: No books extracted!")
        sys.exit(1)


if __name__ == "__main__":
    main()
