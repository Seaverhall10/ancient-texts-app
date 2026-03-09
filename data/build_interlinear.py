"""
build_interlinear.py — Download OSHB Genesis XML + Strong's Hebrew dictionary,
parse word-by-word interlinear data, and generate interlinear.py.

Data sources:
  - Open Scriptures Hebrew Bible (morphhb): CC BY 4.0
    https://github.com/openscriptures/morphhb
  - Strong's Hebrew Dictionary (openscriptures): CC BY 4.0
    https://github.com/openscriptures/strongs

Usage:
  python data/build_interlinear.py                 # All 50 chapters
  python data/build_interlinear.py --chapters 1-2  # Just chapters 1 and 2
  python data/build_interlinear.py --chapters 1,3  # Chapters 1 and 3
"""

import os
import sys
import json
import re
import argparse
import xml.etree.ElementTree as ET
from urllib.request import urlretrieve, urlopen
from urllib.error import URLError

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(BASE, "sources")

STRONGS_URL = "https://raw.githubusercontent.com/openscriptures/strongs/master/hebrew/strongs-hebrew-dictionary.js"
STRONGS_FILE = os.path.join(SOURCES, "strongs-hebrew-dictionary.js")

# Multi-book support: OSHB XML URLs and output files
BOOK_CONFIG = {
    "genesis": {
        "osis_prefix": "Gen",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Gen.xml",
        "xml_file": os.path.join(SOURCES, "Gen.xml"),
        "output": os.path.join(BASE, "interlinear.py"),
        "var_name": "INTERLINEAR",
        "total_chapters": 50,
        "display_name": "Genesis",
    },
    "exodus": {
        "osis_prefix": "Exod",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Exod.xml",
        "xml_file": os.path.join(SOURCES, "Exod.xml"),
        "output": os.path.join(BASE, "interlinear_exodus.py"),
        "var_name": "INTERLINEAR_EXODUS",
        "total_chapters": 40,
        "display_name": "Exodus",
    },
    "leviticus": {
        "osis_prefix": "Lev",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Lev.xml",
        "xml_file": os.path.join(SOURCES, "Lev.xml"),
        "output": os.path.join(BASE, "interlinear_leviticus.py"),
        "var_name": "INTERLINEAR_LEVITICUS",
        "total_chapters": 27,
        "display_name": "Leviticus",
    },
    "numbers": {
        "osis_prefix": "Num",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Num.xml",
        "xml_file": os.path.join(SOURCES, "Num.xml"),
        "output": os.path.join(BASE, "interlinear_numbers.py"),
        "var_name": "INTERLINEAR_NUMBERS",
        "total_chapters": 36,
        "display_name": "Numbers",
    },
    "deuteronomy": {
        "osis_prefix": "Deut",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Deut.xml",
        "xml_file": os.path.join(SOURCES, "Deut.xml"),
        "output": os.path.join(BASE, "interlinear_deuteronomy.py"),
        "var_name": "INTERLINEAR_DEUTERONOMY",
        "total_chapters": 34,
        "display_name": "Deuteronomy",
    },
    "joshua": {
        "osis_prefix": "Josh",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Josh.xml",
        "xml_file": os.path.join(SOURCES, "Josh.xml"),
        "output": os.path.join(BASE, "interlinear_joshua.py"),
        "var_name": "INTERLINEAR_JOSHUA",
        "total_chapters": 24,
        "display_name": "Joshua",
    },
    "judges": {
        "osis_prefix": "Judg",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Judg.xml",
        "xml_file": os.path.join(SOURCES, "Judg.xml"),
        "output": os.path.join(BASE, "interlinear_judges.py"),
        "var_name": "INTERLINEAR_JUDGES",
        "total_chapters": 21,
        "display_name": "Judges",
    },
    "ruth": {
        "osis_prefix": "Ruth",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Ruth.xml",
        "xml_file": os.path.join(SOURCES, "Ruth.xml"),
        "output": os.path.join(BASE, "interlinear_ruth.py"),
        "var_name": "INTERLINEAR_RUTH",
        "total_chapters": 4,
        "display_name": "Ruth",
    },
    "1samuel": {
        "osis_prefix": "1Sam",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/1Sam.xml",
        "xml_file": os.path.join(SOURCES, "1Sam.xml"),
        "output": os.path.join(BASE, "interlinear_1samuel.py"),
        "var_name": "INTERLINEAR_1SAMUEL",
        "total_chapters": 31,
        "display_name": "1 Samuel",
    },
    "2samuel": {
        "osis_prefix": "2Sam",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/2Sam.xml",
        "xml_file": os.path.join(SOURCES, "2Sam.xml"),
        "output": os.path.join(BASE, "interlinear_2samuel.py"),
        "var_name": "INTERLINEAR_2SAMUEL",
        "total_chapters": 24,
        "display_name": "2 Samuel",
    },
    "1kings": {
        "osis_prefix": "1Kgs",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/1Kgs.xml",
        "xml_file": os.path.join(SOURCES, "1Kgs.xml"),
        "output": os.path.join(BASE, "interlinear_1kings.py"),
        "var_name": "INTERLINEAR_1KINGS",
        "total_chapters": 22,
        "display_name": "1 Kings",
    },
    "2kings": {
        "osis_prefix": "2Kgs",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/2Kgs.xml",
        "xml_file": os.path.join(SOURCES, "2Kgs.xml"),
        "output": os.path.join(BASE, "interlinear_2kings.py"),
        "var_name": "INTERLINEAR_2KINGS",
        "total_chapters": 25,
        "display_name": "2 Kings",
    },
    "psalms": {
        "osis_prefix": "Ps",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Ps.xml",
        "xml_file": os.path.join(SOURCES, "Ps.xml"),
        "output": os.path.join(BASE, "interlinear_psalms.py"),
        "var_name": "INTERLINEAR_PSALMS",
        "total_chapters": 150,
        "display_name": "Psalms",
    },
    "isaiah": {
        "osis_prefix": "Isa",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Isa.xml",
        "xml_file": os.path.join(SOURCES, "Isa.xml"),
        "output": os.path.join(BASE, "interlinear_isaiah.py"),
        "var_name": "INTERLINEAR_ISAIAH",
        "total_chapters": 66,
        "display_name": "Isaiah",
    },
    "daniel": {
        "osis_prefix": "Dan",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Dan.xml",
        "xml_file": os.path.join(SOURCES, "Dan.xml"),
        "output": os.path.join(BASE, "interlinear_daniel.py"),
        "var_name": "INTERLINEAR_DANIEL",
        "total_chapters": 12,
        "display_name": "Daniel",
    },
    # === NEW 24 OT BOOKS (Batch 1: Small, Batch 2: Medium, Batch 3: Large) ===
    "obadiah": {
        "osis_prefix": "Obad",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Obad.xml",
        "xml_file": os.path.join(SOURCES, "Obad.xml"),
        "output": os.path.join(BASE, "interlinear_obadiah.py"),
        "var_name": "INTERLINEAR_OBADIAH",
        "total_chapters": 1,
        "display_name": "Obadiah",
    },
    "haggai": {
        "osis_prefix": "Hag",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Hag.xml",
        "xml_file": os.path.join(SOURCES, "Hag.xml"),
        "output": os.path.join(BASE, "interlinear_haggai.py"),
        "var_name": "INTERLINEAR_HAGGAI",
        "total_chapters": 2,
        "display_name": "Haggai",
    },
    "jonah": {
        "osis_prefix": "Jonah",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Jonah.xml",
        "xml_file": os.path.join(SOURCES, "Jonah.xml"),
        "output": os.path.join(BASE, "interlinear_jonah.py"),
        "var_name": "INTERLINEAR_JONAH",
        "total_chapters": 4,
        "display_name": "Jonah",
    },
    "nahum": {
        "osis_prefix": "Nah",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Nah.xml",
        "xml_file": os.path.join(SOURCES, "Nah.xml"),
        "output": os.path.join(BASE, "interlinear_nahum.py"),
        "var_name": "INTERLINEAR_NAHUM",
        "total_chapters": 3,
        "display_name": "Nahum",
    },
    "malachi": {
        "osis_prefix": "Mal",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Mal.xml",
        "xml_file": os.path.join(SOURCES, "Mal.xml"),
        "output": os.path.join(BASE, "interlinear_malachi.py"),
        "var_name": "INTERLINEAR_MALACHI",
        "total_chapters": 4,
        "display_name": "Malachi",
    },
    "zephaniah": {
        "osis_prefix": "Zeph",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Zeph.xml",
        "xml_file": os.path.join(SOURCES, "Zeph.xml"),
        "output": os.path.join(BASE, "interlinear_zephaniah.py"),
        "var_name": "INTERLINEAR_ZEPHANIAH",
        "total_chapters": 3,
        "display_name": "Zephaniah",
    },
    "habakkuk": {
        "osis_prefix": "Hab",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Hab.xml",
        "xml_file": os.path.join(SOURCES, "Hab.xml"),
        "output": os.path.join(BASE, "interlinear_habakkuk.py"),
        "var_name": "INTERLINEAR_HABAKKUK",
        "total_chapters": 3,
        "display_name": "Habakkuk",
    },
    "joel": {
        "osis_prefix": "Joel",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Joel.xml",
        "xml_file": os.path.join(SOURCES, "Joel.xml"),
        "output": os.path.join(BASE, "interlinear_joel.py"),
        "var_name": "INTERLINEAR_JOEL",
        "total_chapters": 3,
        "display_name": "Joel",
    },
    "lamentations": {
        "osis_prefix": "Lam",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Lam.xml",
        "xml_file": os.path.join(SOURCES, "Lam.xml"),
        "output": os.path.join(BASE, "interlinear_lamentations.py"),
        "var_name": "INTERLINEAR_LAMENTATIONS",
        "total_chapters": 5,
        "display_name": "Lamentations",
    },
    "songofsolomon": {
        "osis_prefix": "Song",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Song.xml",
        "xml_file": os.path.join(SOURCES, "Song.xml"),
        "output": os.path.join(BASE, "interlinear_songofsolomon.py"),
        "var_name": "INTERLINEAR_SONGOFSOLOMON",
        "total_chapters": 8,
        "display_name": "Song of Solomon",
    },
    "esther": {
        "osis_prefix": "Esth",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Esth.xml",
        "xml_file": os.path.join(SOURCES, "Esth.xml"),
        "output": os.path.join(BASE, "interlinear_esther.py"),
        "var_name": "INTERLINEAR_ESTHER",
        "total_chapters": 10,
        "display_name": "Esther",
    },
    "ecclesiastes": {
        "osis_prefix": "Eccl",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Eccl.xml",
        "xml_file": os.path.join(SOURCES, "Eccl.xml"),
        "output": os.path.join(BASE, "interlinear_ecclesiastes.py"),
        "var_name": "INTERLINEAR_ECCLESIASTES",
        "total_chapters": 12,
        "display_name": "Ecclesiastes",
    },
    "hosea": {
        "osis_prefix": "Hos",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Hos.xml",
        "xml_file": os.path.join(SOURCES, "Hos.xml"),
        "output": os.path.join(BASE, "interlinear_hosea.py"),
        "var_name": "INTERLINEAR_HOSEA",
        "total_chapters": 14,
        "display_name": "Hosea",
    },
    "micah": {
        "osis_prefix": "Mic",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Mic.xml",
        "xml_file": os.path.join(SOURCES, "Mic.xml"),
        "output": os.path.join(BASE, "interlinear_micah.py"),
        "var_name": "INTERLINEAR_MICAH",
        "total_chapters": 7,
        "display_name": "Micah",
    },
    "amos": {
        "osis_prefix": "Amos",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Amos.xml",
        "xml_file": os.path.join(SOURCES, "Amos.xml"),
        "output": os.path.join(BASE, "interlinear_amos.py"),
        "var_name": "INTERLINEAR_AMOS",
        "total_chapters": 9,
        "display_name": "Amos",
    },
    "zechariah": {
        "osis_prefix": "Zech",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Zech.xml",
        "xml_file": os.path.join(SOURCES, "Zech.xml"),
        "output": os.path.join(BASE, "interlinear_zechariah.py"),
        "var_name": "INTERLINEAR_ZECHARIAH",
        "total_chapters": 14,
        "display_name": "Zechariah",
    },
    "nehemiah": {
        "osis_prefix": "Neh",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Neh.xml",
        "xml_file": os.path.join(SOURCES, "Neh.xml"),
        "output": os.path.join(BASE, "interlinear_nehemiah.py"),
        "var_name": "INTERLINEAR_NEHEMIAH",
        "total_chapters": 13,
        "display_name": "Nehemiah",
    },
    "ezra": {
        "osis_prefix": "Ezra",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Ezra.xml",
        "xml_file": os.path.join(SOURCES, "Ezra.xml"),
        "output": os.path.join(BASE, "interlinear_ezra.py"),
        "var_name": "INTERLINEAR_EZRA",
        "total_chapters": 10,
        "display_name": "Ezra",
    },
    "proverbs": {
        "osis_prefix": "Prov",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Prov.xml",
        "xml_file": os.path.join(SOURCES, "Prov.xml"),
        "output": os.path.join(BASE, "interlinear_proverbs.py"),
        "var_name": "INTERLINEAR_PROVERBS",
        "total_chapters": 31,
        "display_name": "Proverbs",
    },
    "1chronicles": {
        "osis_prefix": "1Chr",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/1Chr.xml",
        "xml_file": os.path.join(SOURCES, "1Chr.xml"),
        "output": os.path.join(BASE, "interlinear_1chronicles.py"),
        "var_name": "INTERLINEAR_1CHRONICLES",
        "total_chapters": 29,
        "display_name": "1 Chronicles",
    },
    "2chronicles": {
        "osis_prefix": "2Chr",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/2Chr.xml",
        "xml_file": os.path.join(SOURCES, "2Chr.xml"),
        "output": os.path.join(BASE, "interlinear_2chronicles.py"),
        "var_name": "INTERLINEAR_2CHRONICLES",
        "total_chapters": 36,
        "display_name": "2 Chronicles",
    },
    "job": {
        "osis_prefix": "Job",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Job.xml",
        "xml_file": os.path.join(SOURCES, "Job.xml"),
        "output": os.path.join(BASE, "interlinear_job.py"),
        "var_name": "INTERLINEAR_JOB",
        "total_chapters": 42,
        "display_name": "Job",
    },
    "ezekiel": {
        "osis_prefix": "Ezek",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Ezek.xml",
        "xml_file": os.path.join(SOURCES, "Ezek.xml"),
        "output": os.path.join(BASE, "interlinear_ezekiel.py"),
        "var_name": "INTERLINEAR_EZEKIEL",
        "total_chapters": 48,
        "display_name": "Ezekiel",
    },
    "jeremiah": {
        "osis_prefix": "Jer",
        "url": "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/Jer.xml",
        "xml_file": os.path.join(SOURCES, "Jer.xml"),
        "output": os.path.join(BASE, "interlinear_jeremiah.py"),
        "var_name": "INTERLINEAR_JEREMIAH",
        "total_chapters": 52,
        "display_name": "Jeremiah",
    },
}

# Default to genesis for backwards compatibility
OUTPUT = BOOK_CONFIG["genesis"]["output"]

# OSIS XML namespace (bibletechnologies.net, NOT biblesociety.org)
NS = "http://www.bibletechnologies.net/2003/OSIS/namespace"


# ── Morphology Decoder ──────────────────────────────────────────
MORPH_PARTS_OF_SPEECH = {
    "A": "adjective", "C": "conjunction", "D": "adverb",
    "N": "noun", "P": "pronoun", "R": "preposition",
    "S": "suffix", "T": "particle", "V": "verb",
}

MORPH_VERB_STEMS = {
    "q": "qal", "N": "niphal", "p": "piel", "P": "pual",
    "h": "hiphil", "H": "hophal", "t": "hithpael",
    "o": "polel", "O": "polal", "r": "hithpolel",
    "m": "poel", "M": "poal", "k": "palel", "K": "pulal",
    "Q": "qal passive", "l": "pilpel", "L": "polpal",
    "f": "hithpalpel", "D": "nithpael", "j": "pealal",
    "i": "pilel", "u": "hothpaal", "c": "tiphil",
    "v": "hishtaphel", "w": "nithpalel", "y": "nithpoel",
    "z": "nithpael",
}

MORPH_VERB_TYPES = {
    "p": "perfect", "q": "sequential perfect",
    "i": "imperfect", "w": "sequential imperfect",
    "h": "cohortative", "j": "jussive",
    "v": "imperative", "r": "participle active",
    "s": "participle passive", "a": "infinitive absolute",
    "c": "infinitive construct",
}

MORPH_PERSON = {"1": "1st", "2": "2nd", "3": "3rd"}
MORPH_GENDER = {"m": "masc", "f": "fem", "b": "both", "c": "common"}
MORPH_NUMBER = {"s": "sing", "p": "plur", "d": "dual"}
MORPH_STATE = {"a": "absolute", "c": "construct", "d": "determined"}


def decode_morphology(morph_code):
    """Decode OSHB morphology code (e.g., 'HVqp3ms') into human-readable string."""
    if not morph_code:
        return ""

    # Strip language prefix (H = Hebrew, A = Aramaic)
    code = morph_code
    lang = ""
    if code and code[0] in ("H", "A"):
        lang = code[0]
        code = code[1:]

    if not code:
        return ""

    # Handle compound forms with "/"
    if "/" in morph_code:
        parts = morph_code.split("/")
        return " + ".join(decode_morphology(p) for p in parts)

    pos_char = code[0]
    pos = MORPH_PARTS_OF_SPEECH.get(pos_char, pos_char)
    rest = code[1:]

    if pos_char == "V" and len(rest) >= 2:
        stem = MORPH_VERB_STEMS.get(rest[0], rest[0])
        vtype = MORPH_VERB_TYPES.get(rest[1], rest[1])
        parts = [f"verb {stem} {vtype}"]

        r = rest[2:]
        if len(r) >= 1:
            parts.append(MORPH_PERSON.get(r[0], ""))
        if len(r) >= 2:
            parts.append(MORPH_GENDER.get(r[1], ""))
        if len(r) >= 3:
            parts.append(MORPH_NUMBER.get(r[2], ""))
        return " ".join(p for p in parts if p)

    elif pos_char == "N" and rest:
        parts = [pos]
        if len(rest) >= 1:
            parts.append(MORPH_GENDER.get(rest[0], ""))
        if len(rest) >= 2:
            parts.append(MORPH_NUMBER.get(rest[1], ""))
        if len(rest) >= 3:
            parts.append(MORPH_STATE.get(rest[2], ""))
        return " ".join(p for p in parts if p)

    elif pos_char == "A" and rest:
        parts = ["adj"]
        if len(rest) >= 1:
            parts.append(MORPH_GENDER.get(rest[0], ""))
        if len(rest) >= 2:
            parts.append(MORPH_NUMBER.get(rest[1], ""))
        if len(rest) >= 3:
            parts.append(MORPH_STATE.get(rest[2], ""))
        return " ".join(p for p in parts if p)

    elif pos_char == "P" and rest:
        parts = ["pronoun"]
        if len(rest) >= 1:
            parts.append(MORPH_PERSON.get(rest[0], ""))
        if len(rest) >= 2:
            parts.append(MORPH_GENDER.get(rest[0], ""))
        if len(rest) >= 3:
            parts.append(MORPH_NUMBER.get(rest[0], ""))
        return " ".join(p for p in parts if p)

    elif pos_char in ("R", "C", "D", "T"):
        return pos

    elif pos_char == "S":
        parts = ["suffix"]
        if len(rest) >= 1:
            parts.append(MORPH_PERSON.get(rest[0], ""))
        if len(rest) >= 2:
            parts.append(MORPH_GENDER.get(rest[1], ""))
        if len(rest) >= 3:
            parts.append(MORPH_NUMBER.get(rest[2], ""))
        return " ".join(p for p in parts if p)

    return pos


# ── Strong's Dictionary Loader ──────────────────────────────────
def load_strongs(path):
    """Load the Strong's Hebrew dictionary JS file and extract definitions."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Format: var strongsHebrewDictionary = {"H1":{...}, ...};\n\nmodule.exports = ...
    # Find the JSON object between first { and the matching };
    idx = raw.find("{")
    if idx < 0:
        print("  WARNING: Could not find JSON start in Strong's dictionary")
        return {}

    # Find the end: "};" followed by module.exports or EOF
    end_match = re.search(r"\};\s*(?:module\.exports|$)", raw[idx:])
    if end_match:
        json_str = raw[idx:idx + end_match.start() + 1]  # include closing }
    else:
        json_str = raw[idx:].rstrip().rstrip(";").rstrip()

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"  WARNING: JSON parse failed at position {e.pos}: {e.msg}")
        # Try a more aggressive cleanup
        json_str = re.sub(r",\s*([}\]])", r"\1", json_str)
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e2:
            print(f"  WARNING: Retry also failed: {e2}")
            return {}

    strongs = {}
    for key, entry in data.items():
        # Normalize key format: "H0001" -> "H1"
        num = key.upper()
        if num.startswith("H"):
            try:
                short = "H" + str(int(num[1:]))
            except ValueError:
                short = num
        else:
            short = num

        strongs[short] = {
            "lemma": entry.get("lemma", ""),
            "translit": entry.get("translit", entry.get("pronounce", "")),
            "gloss": entry.get("kjv_def", entry.get("strongs_def", "")),
            "def": entry.get("strongs_def", ""),
        }
        # Also store with zero-padded key
        strongs[num] = strongs[short]

    return strongs


def _lookup_entry(strongs_dict, strongs_num):
    """Look up a Strong's entry by number, handling normalization."""
    if not strongs_num:
        return None
    entry = strongs_dict.get(strongs_num)
    if not entry and strongs_num.startswith("H"):
        try:
            entry = strongs_dict.get("H" + str(int(strongs_num[1:])))
        except ValueError:
            pass
    return entry


def get_strongs_gloss(strongs_dict, strongs_num):
    """Get a clean, short English gloss from Strong's number.
    Strategy: try strongs_def first (accurate), fall back to kjv_def (concise).
    Target: <=25 chars for clean interlinear display."""
    entry = _lookup_entry(strongs_dict, strongs_num)
    if not entry:
        return ""

    # Try strongs_def first — more accurate primary meaning
    sdef = entry.get("def", "")
    if sdef:
        # Remove cross-references {H1234}
        cleaned = re.sub(r"\{[^}]+\}", "", sdef)
        # Strip leading parenthetical qualifiers like "(absolutely)"
        cleaned = re.sub(r"^\s*\([^)]*\)\s*", "", cleaned)
        if not cleaned.strip():
            cleaned = sdef
        # Take text before first semicolon
        first_clause = cleaned.split(";")[0].strip()
        # Remove remaining parentheticals
        first_clause = re.sub(r"\s*\([^)]*\)", "", first_clause).strip()
        # Take before first comma for short gloss
        short = first_clause.split(",")[0].strip()
        if short and len(short) <= 30:
            return short

    # Fallback: kjv_def — often has the best single-word translations
    kjv = entry.get("gloss", "")
    if kjv:
        kjv = re.sub(r"\{[^}]+\}", "", kjv)
        # Split on comma/semicolon/period and filter
        parts = [p.strip().rstrip(".") for p in re.split(r"[,;]", kjv)]
        for p in parts:
            # Skip [idiom] markers, empty parts, and parenthetical-only parts
            p = re.sub(r"\[idiom\]\s*", "", p).strip()
            p = re.sub(r"\([^)]*\)", "", p).strip()
            if p and len(p) <= 25 and not p.startswith("["):
                return p

    # Last resort: full strongs_def truncated
    if sdef:
        cleaned = re.sub(r"\{[^}]+\}", "", sdef)
        cleaned = re.sub(r"\([^)]*\)", "", cleaned).strip()
        first = cleaned.split(";")[0].split(",")[0].strip()
        if first:
            return first[:25]

    return ""


def get_strongs_translit(strongs_dict, strongs_num):
    """Get transliteration from Strong's."""
    entry = _lookup_entry(strongs_dict, strongs_num)
    if not entry:
        return ""
    return entry.get("translit", "")


# ── OSHB XML Parser ─────────────────────────────────────────────
PREFIX_GLOSS = {
    "b": "in/with", "l": "to/for", "k": "as/like",
    "m": "from", "c": "and", "d": "the",
    "e": "which", "i": "not",
}


def parse_oshb_xml(xml_path, strongs_dict, osis_prefix="Gen", chapters_to_include=None):
    """Parse OSHB XML and extract word-by-word interlinear data."""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    result = {}
    w_tag = f"{{{NS}}}w"
    verse_tag = f"{{{NS}}}verse"
    prefix = osis_prefix + "."

    # Iterate all verse elements
    for elem in root.iter(verse_tag):
        osis_id = elem.get("osisID", "")
        if not osis_id.startswith(prefix):
            continue

        # Parse "Gen.1.1" or "Exod.1.1" -> chapter=N, verse=N
        parts = osis_id.split(".")
        if len(parts) < 3:
            continue

        try:
            chapter_num = int(parts[1])
            verse_num = int(parts[2])
        except ValueError:
            continue

        if chapters_to_include and chapter_num not in chapters_to_include:
            continue

        if chapter_num not in result:
            result[chapter_num] = {"verses": []}

        # Extract words from this verse
        words = []
        for w in elem.iter(w_tag):
            hebrew = w.text or ""
            # Also grab any child text (and tail of children)
            for child in w:
                if child.text:
                    hebrew += child.text
                if child.tail:
                    hebrew += child.tail

            # Remove morpheme boundary markers but keep the Hebrew text
            hebrew = hebrew.replace("/", "").strip()
            if not hebrew:
                continue

            lemma = w.get("lemma", "")
            morph = w.get("morph", "")

            # OSHB lemma format: "b/7225", "1254 a", "430", "c/d/776"
            # Prefix particles are single letters: b, l, k, m, c, d, e, i
            # Strong's numbers are plain digits (no "H" prefix)
            lemma_parts = re.split(r"[/ ]+", lemma.strip())

            strongs = ""
            prefix_particles = []
            for lp in lemma_parts:
                lp = lp.strip()
                if not lp:
                    continue
                if lp in PREFIX_GLOSS:
                    prefix_particles.append(PREFIX_GLOSS[lp])
                elif re.match(r"^\d+$", lp):
                    # This is a Strong's number
                    strongs = "H" + str(int(lp))
                # Skip sense disambiguators like "a", "b", "c" after numbers

            # Get transliteration and gloss from Strong's dict
            translit = get_strongs_translit(strongs_dict, strongs)
            gloss = get_strongs_gloss(strongs_dict, strongs)

            # Decode morphology (handle compound with "/" separators)
            morph_decoded = decode_morphology(morph)

            # Prepend prefix glosses
            if prefix_particles and gloss:
                gloss = " + ".join(prefix_particles) + " " + gloss
            elif prefix_particles and not gloss:
                gloss = " + ".join(prefix_particles)

            word_entry = {"h": hebrew}
            if translit:
                word_entry["t"] = translit
            if strongs:
                word_entry["s"] = strongs
            if gloss:
                word_entry["g"] = gloss
            if morph_decoded:
                word_entry["m"] = morph_decoded

            words.append(word_entry)

        if words:
            result[chapter_num]["verses"].append({
                "num": verse_num,
                "words": words,
            })

    return result


# ── Output Generator ────────────────────────────────────────────
def generate_interlinear_py(data, output_path, var_name="INTERLINEAR", book_name="Genesis"):
    """Generate interlinear Python file with the given constant name."""
    # Sort chapters
    sorted_chapters = sorted(data.keys())

    lines = [
        '"""',
        f'Auto-generated interlinear Hebrew-English data for {book_name}.',
        '',
        'Source: Open Scriptures Hebrew Bible (OSHB) — CC BY 4.0',
        '        Strong\'s Hebrew Dictionary — CC BY 4.0',
        '',
        'Generated by build_interlinear.py',
        '',
        'Keys:  h = Hebrew text (with vowel points)',
        '       t = transliteration',
        '       s = Strong\'s number',
        '       g = English gloss',
        '       m = morphology',
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
                # Build word dict as compact JSON
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


# ── Download Helpers ────────────────────────────────────────────
def download_file(url, dest):
    """Download a file if it doesn't already exist."""
    if os.path.exists(dest):
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


# ── CLI ─────────────────────────────────────────────────────────
def parse_chapters_arg(arg):
    """Parse chapter specification: '1-2', '1,3,5', '1-3,7', etc."""
    if not arg:
        return None  # All chapters

    chapters = set()
    for part in arg.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            for i in range(int(start), int(end) + 1):
                chapters.add(i)
        else:
            chapters.add(int(part))
    return chapters


def build_one_book(book_key, chapters=None, force_download=False, strongs_cache=None):
    """Build interlinear for a single book. Returns (chapters, verses, words) or None on failure."""
    book = BOOK_CONFIG[book_key]

    print("=" * 60)
    print(f"  INTERLINEAR DATA BUILDER — {book['display_name']}")
    if chapters:
        print(f"  Chapters: {sorted(chapters)}")
    else:
        print(f"  Chapters: ALL (1-{book['total_chapters']})")
    print("=" * 60)

    # Ensure sources directory
    os.makedirs(SOURCES, exist_ok=True)

    # Download sources
    print("\n[1/4] Downloading sources...")
    if force_download:
        for f in [book["xml_file"], STRONGS_FILE]:
            if os.path.exists(f):
                os.remove(f)

    if not download_file(book["url"], book["xml_file"]):
        print(f"FATAL: Cannot proceed without OSHB {book['display_name']} XML")
        return None

    if strongs_cache is not None:
        strongs = strongs_cache
    elif not download_file(STRONGS_URL, STRONGS_FILE):
        print("WARNING: Proceeding without Strong's dictionary (glosses will be empty)")
        strongs = {}
    else:
        print("\n[2/4] Loading Strong's dictionary...")
        strongs = load_strongs(STRONGS_FILE)
        print(f"  {len(strongs)} entries loaded")

    # Parse OSHB XML
    print(f"\n[3/4] Parsing OSHB {book['display_name']} XML...")
    data = parse_oshb_xml(book["xml_file"], strongs, book["osis_prefix"], chapters)

    # If we're doing a partial build and output already exists, merge
    output_path = book["output"]
    if chapters and os.path.exists(output_path):
        print(f"  Merging with existing {os.path.basename(output_path)}...")
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("interlinear", output_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            existing = getattr(mod, book["var_name"], {})
            existing.update(data)
            data = existing
        except Exception as e:
            print(f"  WARNING: Could not merge: {e}")

    # Generate output
    print(f"\n[4/4] Generating {os.path.basename(output_path)}...")
    n_chapters, n_verses, n_words = generate_interlinear_py(
        data, output_path, book["var_name"], book["display_name"]
    )

    file_size = os.path.getsize(output_path)
    print(f"\n{'=' * 60}")
    print(f"  BUILD SUCCESSFUL — {book['display_name']}")
    print(f"  Output: {output_path}")
    print(f"  Chapters: {n_chapters}")
    print(f"  Verses:   {n_verses}")
    print(f"  Words:    {n_words:,}")
    print(f"  Size:     {file_size:,} bytes ({file_size / 1024:.1f} KB)")
    print(f"{'=' * 60}")

    # Spot-check first chapter
    first_ch = min(data.keys()) if data else None
    if first_ch and data[first_ch]["verses"]:
        v1 = data[first_ch]["verses"][0]
        print(f"\n  Spot check — {book['display_name']} {first_ch}:{v1['num']}:")
        for w in v1["words"][:4]:
            h = w.get("h", "")
            g = w.get("g", "")
            s = w.get("s", "")
            print(f"    {h:>20s}  {g:<25s}  {s}")
        if len(v1["words"]) > 4:
            print(f"    ... ({len(v1['words'])} words total)")

    return n_chapters, n_verses, n_words


# Books that need interlinear (the 24 new ones)
NEW_OT_BOOKS = [
    "obadiah", "haggai", "jonah", "nahum", "malachi", "zephaniah",
    "habakkuk", "joel", "lamentations",  # Batch 1 — small
    "songofsolomon", "esther", "ecclesiastes", "hosea", "micah",
    "amos", "zechariah", "nehemiah", "ezra",  # Batch 2 — medium
    "proverbs", "1chronicles", "2chronicles", "job", "ezekiel", "jeremiah",  # Batch 3 — large
]

BATCH_1 = NEW_OT_BOOKS[:9]
BATCH_2 = NEW_OT_BOOKS[9:18]
BATCH_3 = NEW_OT_BOOKS[18:]


def main():
    # Ensure UTF-8 output on Windows
    import io
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    elif sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    parser = argparse.ArgumentParser(description="Build interlinear data from OSHB")
    parser.add_argument("--book", type=str, default=None,
                        choices=list(BOOK_CONFIG.keys()),
                        help="Single book to build")
    parser.add_argument("--all", action="store_true",
                        help="Build all 24 new OT books")
    parser.add_argument("--batch", type=int, choices=[1, 2, 3],
                        help="Build a specific batch: 1=small, 2=medium, 3=large")
    parser.add_argument("--chapters", type=str, default=None,
                        help="Chapter range: '1-2', '1,3,5', etc. (default: all)")
    parser.add_argument("--force-download", action="store_true",
                        help="Re-download source files even if cached")
    args = parser.parse_args()

    chapters = parse_chapters_arg(args.chapters)

    if args.all or args.batch:
        # Multi-book mode
        if args.batch == 1:
            books = BATCH_1
            label = "Batch 1 (Small Books)"
        elif args.batch == 2:
            books = BATCH_2
            label = "Batch 2 (Medium Books)"
        elif args.batch == 3:
            books = BATCH_3
            label = "Batch 3 (Large Books)"
        else:
            books = NEW_OT_BOOKS
            label = "All 24 New OT Books"

        print(f"\n{'#' * 60}")
        print(f"  BUILDING INTERLINEAR — {label}")
        print(f"  Books: {len(books)}")
        print(f"{'#' * 60}\n")

        # Pre-load Strong's dictionary once
        os.makedirs(SOURCES, exist_ok=True)
        download_file(STRONGS_URL, STRONGS_FILE)
        print("Loading Strong's dictionary...")
        strongs = load_strongs(STRONGS_FILE)
        print(f"  {len(strongs)} entries loaded\n")

        total_words = 0
        total_verses = 0
        results = []
        for i, bk in enumerate(books, 1):
            print(f"\n{'*' * 60}")
            print(f"  [{i}/{len(books)}] {BOOK_CONFIG[bk]['display_name']}")
            print(f"{'*' * 60}")
            result = build_one_book(bk, chapters, args.force_download, strongs_cache=strongs)
            if result:
                n_ch, n_v, n_w = result
                total_verses += n_v
                total_words += n_w
                results.append((bk, n_ch, n_v, n_w))
            else:
                results.append((bk, 0, 0, 0))

        print(f"\n\n{'#' * 60}")
        print(f"  COMPLETE — {label}")
        print(f"{'#' * 60}")
        for bk, n_ch, n_v, n_w in results:
            status = "OK" if n_w > 0 else "FAILED"
            print(f"  {BOOK_CONFIG[bk]['display_name']:20s}  {n_ch:3d} ch  {n_v:5d} vs  {n_w:7,d} words  [{status}]")
        print(f"  {'TOTAL':20s}  {'':3s}     {total_verses:5d} vs  {total_words:7,d} words")
        print(f"{'#' * 60}")

    elif args.book:
        build_one_book(args.book, chapters, args.force_download)
    else:
        # Default: build genesis for backwards compat
        build_one_book("genesis", chapters, args.force_download)


if __name__ == "__main__":
    main()
