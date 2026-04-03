"""
fetch_kjv_apocrypha.py -- Fetch deuterocanonical texts from kingjamesbibleonline.org
and convert to flow file format.

Usage:
  python tools/fetch_kjv_apocrypha.py 1-Maccabees 16
  python tools/fetch_kjv_apocrypha.py 2-Maccabees 15
  python tools/fetch_kjv_apocrypha.py Wisdom-of-Solomon 19
  python tools/fetch_kjv_apocrypha.py Baruch 5
  python tools/fetch_kjv_apocrypha.py 2-Esdras 16
  python tools/fetch_kjv_apocrypha.py all

Output: data/flow/flow_{text_id}.py

Source: King James Bible Online (KJV Apocrypha — public domain)
HTML pattern: <p><a href="..."><span class="versehover">N </span>verse text</a></p>
"""
import os
import sys
import re
import time
import urllib.request
import html

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOW_DIR = os.path.join(BASE_DIR, "data", "flow")

BASE_URL = "https://www.kingjamesbibleonline.org"

TEXTS = {
    "1-Maccabees": {
        "text_id": "1maccabees",
        "name": "1 Maccabees",
        "chapters": 16,
        "language": "greek",
        "doc": (
            "First Maccabees covers the Jewish revolt against Seleucid oppression\n"
            "(175-134 BC), from Antiochus IV's desecration of the Temple through\n"
            "Judas Maccabeus' victories to the establishment of the Hasmonean dynasty\n"
            "under Simon. Originally composed in Hebrew (now lost), surviving in Greek.\n"
            "A primary historical source for the Hanukkah story and Second Temple politics.\n"
        ),
        "source": "KJV Apocrypha (public domain), via kingjamesbibleonline.org",
    },
    "2-Maccabees": {
        "text_id": "2maccabees",
        "name": "2 Maccabees",
        "chapters": 15,
        "language": "greek",
        "doc": (
            "An abridgment of Jason of Cyrene's five-volume work covering the\n"
            "Maccabean revolt (180-161 BC). More theological than 1 Maccabees:\n"
            "explicit resurrection theology (7:9, 12:43-45), angelic intervention,\n"
            "creation ex nihilo (7:28), and prayers for the dead. The martyrdom\n"
            "of the mother and seven sons (ch. 7) profoundly influenced Jewish\n"
            "and Christian martyrology.\n"
        ),
        "source": "KJV Apocrypha (public domain), via kingjamesbibleonline.org",
    },
    "Wisdom-of-Solomon": {
        "text_id": "wisdom_of_solomon",
        "name": "Wisdom of Solomon",
        "chapters": 19,
        "language": "greek",
        "doc": (
            "A Jewish wisdom text composed in Greek (1st c. BC - 1st c. AD),\n"
            "likely in Alexandria. Attributed to Solomon but written centuries later.\n"
            "Significant for NT theology: Wisdom 2:12-20 parallels the Suffering\n"
            "Servant and is echoed in the mocking at the cross. Wisdom 7:22-8:1\n"
            "describes divine Wisdom in terms echoed by John 1 and Colossians 1.\n"
            "Canonical in Catholic and Orthodox traditions.\n"
        ),
        "source": "KJV Apocrypha (public domain), via kingjamesbibleonline.org",
    },
    "Baruch": {
        "text_id": "baruch",
        "name": "Baruch",
        "chapters": 5,
        "language": "hebrew",
        "doc": (
            "Attributed to Baruch ben Neriah, Jeremiah's scribe. Written as a\n"
            "letter from Babylonian exiles to Jerusalem. Includes a confession\n"
            "of sin (1:15-3:8), a wisdom poem identifying Torah with divine\n"
            "Wisdom (3:9-4:4), and a poem of consolation (4:5-5:9).\n"
            "The identification of Wisdom with Torah (3:37-4:1) parallels\n"
            "Sirach 24 and anticipates rabbinic theology.\n"
        ),
        "source": "KJV Apocrypha (public domain), via kingjamesbibleonline.org",
    },
    "2-Esdras": {
        "text_id": "4ezra",
        "name": "4 Ezra (2 Esdras)",
        "chapters": 16,
        "language": "latin",
        "doc": (
            "A Jewish apocalypse (core: ch. 3-14) with Christian additions\n"
            "(ch. 1-2 = 5 Ezra, ch. 15-16 = 6 Ezra). The Jewish core dates\n"
            "to c. 100 AD, written in response to the Temple's destruction.\n"
            "Ezra debates with the angel Uriel about theodicy, receives seven\n"
            "visions including the eagle vision (Rome) and the Son of Man.\n"
            "Profound influence on Christian eschatology and the concept of\n"
            "the 'messianic woes.' Survives primarily in Latin.\n"
        ),
        "source": "KJV Apocrypha (public domain), via kingjamesbibleonline.org",
    },
}


def fetch_chapter(book_url_name, chapter_num):
    """Fetch a single chapter from kingjamesbibleonline.org."""
    url = f"{BASE_URL}/{book_url_name}-Chapter-{chapter_num}/"
    print(f"  Fetching {url} ...", end=" ", flush=True)

    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"ERROR: {e}")
        return {}

    verses = {}

    # Primary pattern: <span class='versehover'>N </span> followed by verse text inside <a>
    # Site uses single quotes in attributes
    pattern = r"<span[^>]*class=['\"]versehover['\"][^>]*>\s*(\d+)\s*</span>\s*(.*?)</a>"
    matches = re.findall(pattern, raw, re.DOTALL)

    if matches:
        for v_str, v_text in matches:
            v_num = int(v_str)
            # Clean HTML tags and entities
            text = re.sub(r'<[^>]+>', '', v_text).strip()
            text = html.unescape(text)
            # Normalize whitespace
            text = re.sub(r'\s+', ' ', text).strip()
            if text:
                verses[v_num] = text

    if not verses:
        # Fallback: try broader pattern
        pattern2 = r"class=['\"]versehover['\"][^>]*>\s*(\d+)\s*</span>([^<]+)"
        matches2 = re.findall(pattern2, raw)
        for v_str, v_text in matches2:
            v_num = int(v_str)
            text = html.unescape(v_text.strip())
            text = re.sub(r'\s+', ' ', text).strip()
            if text:
                verses[v_num] = text

    print(f"{len(verses)} verses")
    return verses


def write_flow_file(text_info, all_chapters):
    """Write a flow file in standard format."""
    text_id = text_info["text_id"]
    var_name = f"FLOW_{text_id.upper()}"
    out_path = os.path.join(FLOW_DIR, f"flow_{text_id}.py")

    total_verses = sum(len(ch) for ch in all_chapters.values())
    total_chapters = len(all_chapters)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f'"""\n')
        f.write(f'Flow translations for {text_info["name"]} -- complete text.\n')
        f.write(f'{text_info["source"]}.\n\n')
        f.write(f'{text_info["doc"]}\n')
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
    return total_chapters, total_verses


def fetch_book(book_url_name):
    """Fetch all chapters of a book and write the flow file."""
    if book_url_name not in TEXTS:
        print(f"Unknown book: {book_url_name}")
        print(f"Available: {', '.join(TEXTS.keys())}")
        return

    info = TEXTS[book_url_name]
    print(f"\n=== Fetching {info['name']} ({info['chapters']} chapters) ===")

    all_chapters = {}
    for ch in range(1, info["chapters"] + 1):
        verses = fetch_chapter(book_url_name, ch)
        if verses:
            all_chapters[ch] = verses
        time.sleep(0.5)  # polite delay

    if all_chapters:
        write_flow_file(info, all_chapters)
    else:
        print(f"  WARNING: No verses fetched for {info['name']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_kjv_apocrypha.py <book-name|all> [chapters]")
        print(f"Available books: {', '.join(TEXTS.keys())}")
        sys.exit(1)

    book = sys.argv[1]

    if book == "all":
        for book_name in TEXTS:
            fetch_book(book_name)
            time.sleep(1)
    else:
        if len(sys.argv) >= 3:
            # Override chapter count if provided
            TEXTS[book]["chapters"] = int(sys.argv[2])
        fetch_book(book)


if __name__ == "__main__":
    main()
