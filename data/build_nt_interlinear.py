"""
build_nt_interlinear.py — Build Greek NT interlinear data from MorphGNT + Strong's Greek.

Data sources:
  - MorphGNT SBLGNT: https://github.com/morphgnt/sblgnt (CC-BY-SA 3.0)
  - Strong's Greek Dictionary (openscriptures): CC BY 4.0
    https://github.com/openscriptures/strongs

MorphGNT columns (space-separated):
  bookchapterverse  POS  parse  text  word  normalized  lemma
  e.g.: 010101 N- ----NSF- Βίβλος Βίβλος βίβλος βίβλος

Output: data/interlinear_nt_{book}.py with INTERLINEAR_NT_{BOOK} dict
Format (parallel to Hebrew interlinear):
  { chapter: { "verses": [ { "num": v, "words": [
      {"h": greek_text, "t": translit, "s": "G1234", "g": gloss, "m": morphology, "l": lemma}
  ] } ] } }

Usage:
  python data/build_nt_interlinear.py                         # All 27 NT books
  python data/build_nt_interlinear.py --book matthew          # Single book
  python data/build_nt_interlinear.py --book matthew,john     # Multiple books
"""

import os
import sys
import json
import re
import argparse
import unicodedata
from urllib.request import urlretrieve, urlopen
from urllib.error import URLError

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(BASE, "sources")

STRONGS_GREEK_URL = "https://raw.githubusercontent.com/openscriptures/strongs/master/greek/strongs-greek-dictionary.js"
STRONGS_GREEK_FILE = os.path.join(SOURCES, "strongs-greek-dictionary.js")

MORPHGNT_BASE_URL = "https://raw.githubusercontent.com/morphgnt/sblgnt/master/"

# NT book configuration
# morphgnt_file: filename in the morphgnt repo
# internal_num: NT book number (1-27) as used inside morphgnt data files
# var_suffix: ALLCAPS for var name INTERLINEAR_NT_{var_suffix}
# output: filename in data/
NT_BOOK_CONFIG = {
    "matthew":        {"morphgnt_file": "61-Mt-morphgnt.txt",  "internal_num":  1, "chapters": 28, "var_suffix": "MATTHEW",        "display": "Matthew"},
    "mark":           {"morphgnt_file": "62-Mk-morphgnt.txt",  "internal_num":  2, "chapters": 16, "var_suffix": "MARK",           "display": "Mark"},
    "luke":           {"morphgnt_file": "63-Lk-morphgnt.txt",  "internal_num":  3, "chapters": 24, "var_suffix": "LUKE",           "display": "Luke"},
    "john":           {"morphgnt_file": "64-Jn-morphgnt.txt",  "internal_num":  4, "chapters": 21, "var_suffix": "JOHN",           "display": "John"},
    "acts":           {"morphgnt_file": "65-Ac-morphgnt.txt",  "internal_num":  5, "chapters": 28, "var_suffix": "ACTS",           "display": "Acts"},
    "romans":         {"morphgnt_file": "66-Ro-morphgnt.txt",  "internal_num":  6, "chapters": 16, "var_suffix": "ROMANS",         "display": "Romans"},
    "1corinthians":   {"morphgnt_file": "67-1Co-morphgnt.txt", "internal_num":  7, "chapters": 16, "var_suffix": "1CORINTHIANS",   "display": "1 Corinthians"},
    "2corinthians":   {"morphgnt_file": "68-2Co-morphgnt.txt", "internal_num":  8, "chapters": 13, "var_suffix": "2CORINTHIANS",   "display": "2 Corinthians"},
    "galatians":      {"morphgnt_file": "69-Ga-morphgnt.txt",  "internal_num":  9, "chapters":  6, "var_suffix": "GALATIANS",      "display": "Galatians"},
    "ephesians":      {"morphgnt_file": "70-Eph-morphgnt.txt", "internal_num": 10, "chapters":  6, "var_suffix": "EPHESIANS",      "display": "Ephesians"},
    "philippians":    {"morphgnt_file": "71-Php-morphgnt.txt", "internal_num": 11, "chapters":  4, "var_suffix": "PHILIPPIANS",    "display": "Philippians"},
    "colossians":     {"morphgnt_file": "72-Col-morphgnt.txt", "internal_num": 12, "chapters":  4, "var_suffix": "COLOSSIANS",     "display": "Colossians"},
    "1thessalonians": {"morphgnt_file": "73-1Th-morphgnt.txt", "internal_num": 13, "chapters":  5, "var_suffix": "1THESSALONIANS", "display": "1 Thessalonians"},
    "2thessalonians": {"morphgnt_file": "74-2Th-morphgnt.txt", "internal_num": 14, "chapters":  3, "var_suffix": "2THESSALONIANS", "display": "2 Thessalonians"},
    "1timothy":       {"morphgnt_file": "75-1Ti-morphgnt.txt", "internal_num": 15, "chapters":  6, "var_suffix": "1TIMOTHY",       "display": "1 Timothy"},
    "2timothy":       {"morphgnt_file": "76-2Ti-morphgnt.txt", "internal_num": 16, "chapters":  4, "var_suffix": "2TIMOTHY",       "display": "2 Timothy"},
    "titus":          {"morphgnt_file": "77-Tit-morphgnt.txt", "internal_num": 17, "chapters":  3, "var_suffix": "TITUS",          "display": "Titus"},
    "philemon":       {"morphgnt_file": "78-Phm-morphgnt.txt", "internal_num": 18, "chapters":  1, "var_suffix": "PHILEMON",       "display": "Philemon"},
    "hebrews":        {"morphgnt_file": "79-Heb-morphgnt.txt", "internal_num": 19, "chapters": 13, "var_suffix": "HEBREWS",        "display": "Hebrews"},
    "james":          {"morphgnt_file": "80-Jas-morphgnt.txt", "internal_num": 20, "chapters":  5, "var_suffix": "JAMES",          "display": "James"},
    "1peter":         {"morphgnt_file": "81-1Pe-morphgnt.txt", "internal_num": 21, "chapters":  5, "var_suffix": "1PETER",         "display": "1 Peter"},
    "2peter":         {"morphgnt_file": "82-2Pe-morphgnt.txt", "internal_num": 22, "chapters":  3, "var_suffix": "2PETER",         "display": "2 Peter"},
    "1john":          {"morphgnt_file": "83-1Jn-morphgnt.txt", "internal_num": 23, "chapters":  5, "var_suffix": "1JOHN",          "display": "1 John"},
    "2john":          {"morphgnt_file": "84-2Jn-morphgnt.txt", "internal_num": 24, "chapters":  1, "var_suffix": "2JOHN",          "display": "2 John"},
    "3john":          {"morphgnt_file": "85-3Jn-morphgnt.txt", "internal_num": 25, "chapters":  1, "var_suffix": "3JOHN",          "display": "3 John"},
    "jude":           {"morphgnt_file": "86-Jud-morphgnt.txt", "internal_num": 26, "chapters":  1, "var_suffix": "JUDE",           "display": "Jude"},
    "revelation":     {"morphgnt_file": "87-Re-morphgnt.txt",  "internal_num": 27, "chapters": 22, "var_suffix": "REVELATION",     "display": "Revelation"},
}


# ── Greek Morphology Decoder ─────────────────────────────────────
POS_NAMES = {
    "A-": "adjective", "C-": "conjunction", "D-": "adverb",
    "I-": "interjection", "N-": "noun", "P-": "preposition",
    "RA": "article", "RD": "demonstrative", "RI": "interrogative",
    "RP": "personal pronoun", "RR": "relative pronoun",
    "V-": "verb", "X-": "particle",
}

TENSE = {"P": "present", "I": "imperfect", "F": "future", "A": "aorist", "X": "perfect", "Y": "pluperfect"}
VOICE = {"A": "active", "M": "middle", "P": "passive"}
MOOD  = {"I": "indicative", "D": "imperative", "S": "subjunctive", "O": "optative", "N": "infinitive", "P": "participle"}
CASE  = {"N": "nominative", "G": "genitive", "D": "dative", "A": "accusative"}
NUMBER = {"S": "singular", "P": "plural"}
GENDER = {"M": "masculine", "F": "feminine", "N": "neuter"}
DEGREE = {"C": "comparative", "S": "superlative"}
PERSON = {"1": "1st", "2": "2nd", "3": "3rd"}


def decode_greek_morphology(pos_code, parse_code):
    """Decode MorphGNT POS + 8-char parse code to human-readable string.
    Parse code: person tense voice mood case number gender degree
    Dashes = not applicable."""
    pos = POS_NAMES.get(pos_code, pos_code.strip("-").lower())
    if not parse_code or parse_code == "--------":
        return pos

    p = parse_code  # 8 chars
    parts = [pos]

    if pos_code == "V-":
        # Verb: person tense voice mood case number gender
        if p[0] != "-": parts.append(PERSON.get(p[0], ""))
        if p[1] != "-": parts.append(TENSE.get(p[1], ""))
        if p[2] != "-": parts.append(VOICE.get(p[2], ""))
        if p[3] != "-": parts.append(MOOD.get(p[3], ""))
        if p[4] != "-": parts.append(CASE.get(p[4], ""))
        if p[5] != "-": parts.append(NUMBER.get(p[5], ""))
        if p[6] != "-": parts.append(GENDER.get(p[6], ""))
    elif pos_code in ("N-", "A-", "RA", "RD", "RI", "RP", "RR"):
        # Nominal: case number gender
        if p[4] != "-": parts.append(CASE.get(p[4], ""))
        if p[5] != "-": parts.append(NUMBER.get(p[5], ""))
        if p[6] != "-": parts.append(GENDER.get(p[6], ""))
        if p[7] != "-": parts.append(DEGREE.get(p[7], ""))

    return " ".join(x for x in parts if x)


# ── Transliteration ──────────────────────────────────────────────
def strip_greek_diacritics(text):
    """Remove accents/breathing marks from Greek for approximate matching."""
    nfkd = unicodedata.normalize("NFD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


# ── Strong's Greek Loader ────────────────────────────────────────
def load_strongs_greek(path):
    """Load openscriptures Strong's Greek dictionary JS and return {Gnum: {...}}."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()

    idx = raw.find("{")
    if idx < 0:
        return {}
    end_match = re.search(r"\};\s*(?:module\.exports|$)", raw[idx:])
    json_str = raw[idx:idx + end_match.start() + 1] if end_match else raw[idx:].rstrip().rstrip(";")
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        json_str = re.sub(r",\s*([}\]])", r"\1", json_str)
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            return {}

    strongs = {}
    lemma_index = {}  # normalized_lemma -> G-number

    for key, entry in data.items():
        num = key.upper()
        if not num.startswith("G"):
            continue
        try:
            short = "G" + str(int(num[1:]))
        except ValueError:
            short = num

        record = {
            "num": short,
            "lemma": entry.get("lemma", ""),
            "translit": entry.get("translit", entry.get("pronounce", "")),
            "gloss": entry.get("kjv_def", ""),
            "def": entry.get("strongs_def", ""),
        }
        strongs[short] = record
        strongs[num] = record

        # Build lemma → G-number index
        lemma = entry.get("lemma", "")
        if lemma:
            stripped = strip_greek_diacritics(lemma.lower())
            if stripped not in lemma_index:
                lemma_index[stripped] = short

    return strongs, lemma_index


def lookup_strongs_by_lemma(lemma, strongs, lemma_index):
    """Try to find Strong's G-number for a given Greek lemma."""
    if not lemma:
        return None
    # Exact match after stripping diacritics
    stripped = strip_greek_diacritics(lemma.lower())
    gnum = lemma_index.get(stripped)
    if gnum:
        return gnum
    # Try just the bare letters (remove all non-letter chars)
    bare = "".join(c for c in stripped if c.isalpha())
    for key, val in lemma_index.items():
        if "".join(c for c in key if c.isalpha()) == bare:
            return val
    return None


def get_gloss(gnum, strongs):
    """Get a short English gloss from Strong's number."""
    if not gnum:
        return ""
    entry = strongs.get(gnum)
    if not entry:
        return ""
    kjv = entry.get("gloss", "")
    if kjv:
        kjv = re.sub(r"\{[^}]+\}", "", kjv)
        parts = [p.strip().rstrip(".") for p in re.split(r"[,;]", kjv)]
        for p in parts:
            p = re.sub(r"\[idiom\]\s*", "", p).strip()
            p = re.sub(r"\([^)]*\)", "", p).strip()
            if p and len(p) <= 30 and not p.startswith("["):
                return p
    sdef = entry.get("def", "")
    if sdef:
        cleaned = re.sub(r"\{[^}]+\}", "", sdef)
        cleaned = re.sub(r"\([^)]*\)", "", cleaned).strip()
        first = cleaned.split(";")[0].split(",")[0].strip()
        if first:
            return first[:30]
    return ""


def get_translit(gnum, strongs):
    """Get transliteration from Strong's."""
    if not gnum:
        return ""
    entry = strongs.get(gnum)
    return entry.get("translit", "") if entry else ""


# ── MorphGNT Parser ──────────────────────────────────────────────
def parse_morphgnt(txt_path, internal_num, strongs, lemma_index):
    """Parse a MorphGNT .txt file and return interlinear data dict."""
    result = {}

    with open(txt_path, encoding="utf-8") as f:
        lines = f.readlines()

    book_prefix = f"{internal_num:02d}"

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) < 7:
            continue

        ref = parts[0]  # e.g. "010101"
        if not ref.startswith(book_prefix):
            continue

        pos_code = parts[1]      # e.g. "N-"
        parse_code = parts[2]    # e.g. "----NSF-"
        text_word = parts[3]     # word as it appears (with accents + punctuation)
        lemma = parts[6] if len(parts) >= 7 else parts[5]

        # Parse chapter + verse from ref
        ref_digits = ref[len(book_prefix):]  # remaining after book prefix
        if len(ref_digits) < 4:
            continue
        chapter_num = int(ref_digits[:2])
        verse_num = int(ref_digits[2:4])

        # Strip trailing punctuation from text_word for display
        greek = text_word.rstrip(".,;:!?·")

        # Look up Strong's G-number from lemma
        gnum = lookup_strongs_by_lemma(lemma, strongs, lemma_index)

        # Get gloss and transliteration
        gloss = get_gloss(gnum, strongs)
        translit = get_translit(gnum, strongs)

        # Decode morphology
        morph = decode_greek_morphology(pos_code, parse_code)

        # Build word entry
        # Use "h" for script text (matches Hebrew convention — same rendering slot)
        # Use "g" for gloss (matches Hebrew "g" = English gloss)
        word_entry = {"h": greek}
        if translit:
            word_entry["t"] = translit
        if gnum:
            word_entry["s"] = gnum
        if gloss:
            word_entry["g"] = gloss
        if morph:
            word_entry["m"] = morph
        # Include lemma for reference
        if lemma and lemma != greek:
            word_entry["l"] = lemma

        # Store in result
        if chapter_num not in result:
            result[chapter_num] = {"verses": []}

        verses = result[chapter_num]["verses"]
        if not verses or verses[-1]["num"] != verse_num:
            verses.append({"num": verse_num, "words": []})
        verses[-1]["words"].append(word_entry)

    return result


# ── Output Generator ─────────────────────────────────────────────
def generate_interlinear_py(data, output_path, var_name, book_name):
    """Write Greek interlinear Python file."""
    sorted_chapters = sorted(data.keys())

    lines = [
        '"""',
        f'Auto-generated interlinear Greek-English data for {book_name}.',
        '',
        'Source: MorphGNT SBLGNT (https://github.com/morphgnt/sblgnt) — CC-BY-SA 3.0',
        '        Strong\'s Greek Dictionary (openscriptures) — CC-BY 4.0',
        '',
        'Generated by build_nt_interlinear.py',
        '',
        'Keys:  h = Greek text (with accents) — same slot as Hebrew "h"',
        '       t = transliteration',
        '       s = Strong\'s G-number',
        '       g = English gloss — same slot as Hebrew "g"',
        '       m = morphology',
        '       l = lexical lemma',
        '"""',
        '',
        f'{var_name} = {{',
    ]

    total_words = 0
    total_verses = 0

    for ch_num in sorted_chapters:
        ch_data = data[ch_num]
        verses = ch_data["verses"]
        total_verses += len(verses)

        lines.append(f'    {ch_num}: {{')
        lines.append(f'        "verses": [')

        for verse in verses:
            lines.append(f'            {{')
            lines.append(f'                "num": {verse["num"]},')
            lines.append(f'                "words": [')

            for word in verse["words"]:
                total_words += 1
                word_json = json.dumps(word, ensure_ascii=False)
                lines.append(f'                    {word_json},')

            lines.append(f'                ]')
            lines.append(f'            }},')

        lines.append(f'        ]')
        lines.append(f'    }},')

    lines.append('}')
    lines.append('')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(sorted_chapters), total_verses, total_words


# ── Download Helper ──────────────────────────────────────────────
def download_file(url, dest, force=False):
    if not force and os.path.exists(dest):
        size = os.path.getsize(dest)
        print(f"  [cached] {os.path.basename(dest)} ({size:,} bytes)")
        return True
    print(f"  [download] {url}")
    try:
        urlretrieve(url, dest)
        size = os.path.getsize(dest)
        print(f"  [saved] {os.path.basename(dest)} ({size:,} bytes)")
        return True
    except (URLError, OSError) as e:
        print(f"  [ERROR] Download failed: {e}")
        return False


# ── Main ─────────────────────────────────────────────────────────
def main():
    import io
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    elif sys.stdout.encoding != "utf-8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    parser = argparse.ArgumentParser(description="Build NT Greek interlinear data")
    parser.add_argument("--book", type=str, default="all",
                        help="Book(s) to build: 'all', or comma-separated names like 'matthew,john'")
    parser.add_argument("--force-download", action="store_true",
                        help="Re-download source files even if cached")
    args = parser.parse_args()

    # Which books to build
    if args.book.lower() == "all":
        books_to_build = list(NT_BOOK_CONFIG.keys())
    else:
        books_to_build = [b.strip().lower() for b in args.book.split(",")]
        for b in books_to_build:
            if b not in NT_BOOK_CONFIG:
                print(f"ERROR: Unknown book '{b}'. Valid: {', '.join(NT_BOOK_CONFIG.keys())}")
                sys.exit(1)

    print("=" * 60)
    print("  NT GREEK INTERLINEAR BUILDER")
    print(f"  Books: {', '.join(books_to_build)}")
    print("=" * 60)

    os.makedirs(SOURCES, exist_ok=True)

    # Step 1: Download Strong's Greek dictionary
    print("\n[1/3] Downloading Strong's Greek dictionary...")
    if not download_file(STRONGS_GREEK_URL, STRONGS_GREEK_FILE, args.force_download):
        print("WARNING: Proceeding without Strong's dictionary — no G-numbers or glosses")
        strongs = {}
        lemma_index = {}
    else:
        print("[2/3] Loading Strong's Greek dictionary...")
        strongs, lemma_index = load_strongs_greek(STRONGS_GREEK_FILE)
        print(f"  {len(strongs)//2:,} entries, {len(lemma_index):,} lemma mappings")

    # Step 3: Build each book
    print("\n[3/3] Building books...")
    results = []

    for book_id in books_to_build:
        cfg = NT_BOOK_CONFIG[book_id]
        var_name = f"INTERLINEAR_NT_{cfg['var_suffix']}"
        output_path = os.path.join(BASE, f"interlinear_nt_{book_id}.py")
        morphgnt_url = MORPHGNT_BASE_URL + cfg["morphgnt_file"]
        morphgnt_local = os.path.join(SOURCES, cfg["morphgnt_file"])

        print(f"\n  --- {cfg['display']} ---")

        # Download MorphGNT file
        if not download_file(morphgnt_url, morphgnt_local, args.force_download):
            print(f"  SKIP: Could not download {cfg['morphgnt_file']}")
            continue

        # Parse
        data = parse_morphgnt(morphgnt_local, cfg["internal_num"], strongs, lemma_index)

        if not data:
            print(f"  WARNING: No data parsed for {cfg['display']}")
            continue

        # Generate output
        n_ch, n_v, n_w = generate_interlinear_py(data, output_path, var_name, cfg["display"])
        size = os.path.getsize(output_path)
        print(f"  {var_name}: {n_ch} chapters, {n_v} verses, {n_w:,} words ({size//1024} KB)")
        results.append((book_id, n_ch, n_v, n_w))

    print("\n" + "=" * 60)
    print("  COMPLETE")
    total_words = sum(r[3] for r in results)
    print(f"  {len(results)}/{len(books_to_build)} books built, {total_words:,} total Greek words")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Run: python build.py  (in project root)")
    print("  2. The NT Greek interlinear will appear in the reading pane")
    print("     for all 27 NT books alongside the study content.")


if __name__ == "__main__":
    main()
