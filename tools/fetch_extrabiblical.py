"""
fetch_extrabiblical.py -- Fetch extra-biblical texts from Sefaria API
and convert to flow file format.

Usage:
  python tools/fetch_extrabiblical.py jubilees
  python tools/fetch_extrabiblical.py tobit
  python tools/fetch_extrabiblical.py all

Output: data/flow/flow_{text_id}.py
"""
import os
import sys
import json
import time
import re
import urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

FLOW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "flow")

# Sefaria text name -> our text_id, display name, chapters, docstring
TEXTS = {
    "jubilees": {
        "sefaria": "Book_of_Jubilees",
        "chapters": 50,
        "name": "Book of Jubilees",
        "doc": (
            'Also known as "The Little Genesis," Jubilees retells Genesis and Exodus\n'
            'through the angel of the presence dictating to Moses on Mount Sinai.\n'
            'Key distinctive elements: the 364-day solar calendar, jubilee dating\n'
            'system (49-year cycles), named women in genealogies, expanded Watcher\n'
            'tradition, Mastema as adversary figure, and detailed halakhic rulings.\n'
            '\n'
            "The text survives complete only in Ge'ez (Ethiopic), with fragments\n"
            'found at Qumran (4Q216-228, 11Q12) confirming its antiquity (2nd c. BC).\n'
        ),
        "source": "R.H. Charles translation (public domain), via Sefaria API",
    },
    "tobit": {
        "sefaria": "Tobit",
        "chapters": 14,
        "name": "Book of Tobit",
        "doc": (
            'A narrative set during the Assyrian exile about Tobit of Naphtali and\n'
            'his son Tobias. Themes: angelic mediation (Raphael), demonology (Asmodeus),\n'
            'prayer, almsgiving, and divine providence. Found at Qumran in both\n'
            'Aramaic (4Q196-199) and Hebrew (4Q200), confirming pre-Christian origin.\n'
        ),
        "source": "Brenton LXX / Charles APOT (public domain), via Sefaria API",
    },
    "wisdom_of_solomon": {
        "sefaria": "Wisdom_of_Solomon",
        "chapters": 19,
        "name": "Wisdom of Solomon",
        "doc": (
            'A Jewish wisdom text composed in Greek (1st c. BC - 1st c. AD), likely\n'
            'in Alexandria. Attributed to Solomon but written centuries later.\n'
            'Significant for NT theology: Wisdom 2:12-20 parallels the Suffering\n'
            'Servant and is echoed in the mocking at the cross. Wisdom 7:22-8:1\n'
            'describes divine Wisdom in terms echoed by John 1 and Colossians 1.\n'
            'Canonical in Catholic and Orthodox traditions.\n'
        ),
        "source": "Brenton LXX (public domain), via Sefaria API",
    },
    "sirach": {
        "sefaria": "Ben_Sira",
        "chapters": 51,
        "name": "Sirach (Ecclesiasticus / Ben Sira)",
        "doc": (
            'Written by Yeshua ben Eleazar ben Sira (c. 180 BC), translated into\n'
            'Greek by his grandson (c. 132 BC). The most extensive wisdom text of\n'
            'the Second Temple period. The "Praise of the Fathers" (ch. 44-50)\n'
            'surveys Israel\'s heroes. Hebrew fragments found at Qumran and Masada.\n'
            'Canonical in Catholic and Orthodox traditions. Cited by early church\n'
            'fathers as Scripture.\n'
        ),
        "source": "Brenton LXX / Sefaria (public domain)",
    },
    "judith": {
        "sefaria": "Judith",
        "chapters": 16,
        "name": "Book of Judith",
        "doc": (
            'A narrative of Jewish heroine Judith who saves her city from the\n'
            'Assyrian general Holofernes. Themes: divine deliverance through\n'
            'unexpected agents, faith vs military power, women as instruments\n'
            'of salvation. Canonical in Catholic and Orthodox traditions.\n'
        ),
        "source": "Brenton LXX (public domain), via Sefaria API",
    },
    "psalms_of_solomon": {
        "sefaria": "Psalms_of_Solomon",
        "chapters": 18,
        "name": "Psalms of Solomon",
        "doc": (
            "A collection of 18 psalms composed in the 1st century BC, likely in\n"
            "response to Pompey's conquest of Jerusalem (63 BC). Contains significant\n"
            "messianic expectations (Ps Sol 17-18) describing a Davidic king who will\n"
            "purge Jerusalem and rule the nations. Important background for NT\n"
            "messianic theology.\n"
        ),
        "source": "R.H. Charles APOT (public domain), via Sefaria API",
    },
}


def fetch_chapter(sefaria_name, ch_num):
    """Fetch a single chapter from Sefaria API."""
    url = f"https://www.sefaria.org/api/texts/{sefaria_name}.{ch_num}?context=0"
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
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace('(A.M. = Anno Mundi) ', '').replace('(A.M. = Anno Mundi)', '')
    return text


def fetch_text(text_id):
    """Fetch all chapters of a text and write the flow file."""
    if text_id not in TEXTS:
        print(f"Unknown text: {text_id}")
        print(f"Available: {', '.join(TEXTS.keys())}")
        return False

    cfg = TEXTS[text_id]
    output_file = os.path.join(FLOW_DIR, f"flow_{text_id}.py")
    var_name = text_id.upper()

    print(f"\nFetching {cfg['name']} from Sefaria API...")
    print(f"  Sefaria name: {cfg['sefaria']}")
    print(f"  Expected chapters: {cfg['chapters']}")
    print(f"  Source: {cfg['source']}\n")

    chapters = {}
    total_verses = 0

    for ch in range(1, cfg['chapters'] + 1):
        verses_raw = fetch_chapter(cfg['sefaria'], ch)
        if not verses_raw:
            print(f"  Ch {ch}: EMPTY")
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

        time.sleep(0.3)

    print(f"\n  Total: {len(chapters)} chapters, {total_verses} verses")

    if len(chapters) < cfg['chapters'] * 0.8:
        print(f"  WARNING: Only got {len(chapters)}/{cfg['chapters']} chapters")

    if not chapters:
        print("  ERROR: No chapters retrieved. Aborting.")
        return False

    # Write flow file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'"""\nFlow translations for {cfg["name"]} -- complete text.\n')
        f.write(f'{cfg["source"]}.\n\n')
        f.write(cfg['doc'])
        f.write(f'\nChapters: {len(chapters)} | Verses: {total_verses}\n')
        f.write('"""\n\n')

        f.write(f'FLOW_{var_name} = {{\n')
        for ch_num in sorted(chapters.keys()):
            vv = chapters[ch_num]
            f.write(f'    {ch_num}: {{  # Chapter {ch_num}\n')
            for v_num in sorted(vv.keys()):
                text = vv[v_num].replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v_num}: '{text}',\n")
            f.write('    },\n')
        f.write('}\n\n')
        f.write(f'NOTES_{var_name} = {{}}\n')

    print(f"\n  Written: {output_file}")
    print(f"  File size: {os.path.getsize(output_file):,} bytes")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/fetch_extrabiblical.py <text_id|all>")
        print(f"Available: {', '.join(TEXTS.keys())}")
        sys.exit(1)

    target = sys.argv[1].lower()

    if target == 'all':
        for tid in TEXTS:
            fetch_text(tid)
    else:
        if not fetch_text(target):
            sys.exit(1)


if __name__ == "__main__":
    main()
