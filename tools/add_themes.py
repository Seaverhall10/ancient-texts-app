"""
add_themes.py - Add "themes" field to chapter dicts in Wisdom & Prophet era files.
Inserts themes after the "type" field line.
"""
import re
import os

BASE = r"C:\Users\User\Desktop\ANCIENT_TEXTS Study App"

# Map: file path (relative to BASE) -> list of (chapter_id, themes) tuples
THEME_MAP = {
    # ═══════════════════════════════════════════════════════════════
    # JOB
    # ═══════════════════════════════════════════════════════════════
    "data/job/era_60.py": [
        ("job-1",     ["DC", "REBEL", "PROV"]),
        ("job-2",     ["DC", "REBEL", "PROV"]),
        ("job-3",     ["SPIRIT"]),
        ("job-4-5",   ["DC", "SPIRIT"]),
        ("job-6-7",   ["SPIRIT"]),
        ("job-8-10",  ["DC", "PROV", "SPIRIT"]),
        ("job-12-14", ["DC", "PROV", "SPIRIT"]),
    ],
    "data/job/era_61.py": [
        ("job-15-17", ["PROV", "SPIRIT"]),
        ("job-18-19", ["SEED", "REVERSAL", "SPIRIT"]),
        ("job-20-21", ["PROV", "SPIRIT"]),
        ("job-22-28", ["PROV", "SPIRIT", "DC"]),
        ("job-29-31", ["LAW", "PROV", "SPIRIT"]),
        ("job-32-37", ["DC", "SPIRIT", "PROV"]),
    ],
    "data/job/era_62.py": [
        ("job-38-39", ["DC", "GLORY", "PROV", "SPIRIT"]),
        ("job-40-41", ["DC", "GLORY", "REBEL", "SPIRIT"]),
        ("job-42",    ["DC", "REVERSAL", "PROV", "PRIEST"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # PSALMS
    # ═══════════════════════════════════════════════════════════════
    "data/psalms/era_psalms_book1.py": [
        ("ps-1-2",         ["SEED", "KING", "DC", "LAW", "NATIONS"]),
        ("ps-8",           ["DC", "GLORY", "KING"]),
        ("ps-16-22",       ["SEED", "PRIEST", "SPIRIT", "BLOOD", "TYPE"]),
        ("ps-23-24",       ["KING", "HOLY", "GLORY"]),
        ("ps-29",          ["DC", "GLORY", "KING"]),
        ("ps-33-34",       ["DC", "PROV"]),
        ("ps-book1-themes",["KING", "SEED", "DC"]),
    ],
    "data/psalms/era_psalms_book2.py": [
        ("ps-42-43",  ["EXILE", "HOLY", "SPIRIT"]),
        ("ps-45",     ["KING", "SEED", "LOVE", "WOMEN"]),
        ("ps-46-48",  ["KING", "DC", "LAND", "HOLY"]),
        ("ps-68",     ["DC", "GLORY", "KING", "NATIONS"]),
        ("ps-72",     ["KING", "SEED", "NATIONS", "PROV"]),
    ],
    "data/psalms/era_psalms_book3.py": [
        ("ps-73-74",          ["DC", "PROV", "REBEL"]),
        ("ps-78",             ["REMEMBER", "COV", "REBEL"]),
        ("ps-82",             ["DC", "NATIONS", "RIV"]),
        ("ps-83",             ["DC", "NATIONS"]),
        ("ps-89",             ["DC", "COV", "SEED", "KING"]),
        ("ps-book3-synthesis",["DC", "NATIONS", "RIV", "KING"]),
    ],
    "data/psalms/era_psalms_book4.py": [
        ("ps-90-91",   ["PROV", "SPIRIT", "DC"]),
        ("ps-93-99",   ["KING", "DC", "GLORY", "HOLY", "NATIONS"]),
        ("ps-104",     ["DC", "GLORY", "SPIRIT"]),
        ("ps-106",     ["COV", "REMEMBER", "REBEL"]),
    ],
    "data/psalms/era_psalms_book5.py": [
        ("ps-107-120-134",   ["EXILE", "REVERSAL", "LAND", "REMEMBER"]),
        ("ps-110-118-132",   ["KING", "PRIEST", "DC", "SEED", "COV"]),
        ("ps-113-118-146-150",["DC", "GLORY", "KING", "REVERSAL"]),
        ("ps-119",           ["LAW", "LOVE", "PROV"]),
        ("ps-139",           ["DC", "SPIRIT", "GLORY"]),
    ],
    "data/psalms/era_psalms_cosmic.py": [
        ("ps-29-cosmic",  ["DC", "GLORY", "KING"]),
        ("ps-68-cosmic",  ["DC", "GLORY", "KING", "NATIONS"]),
        ("ps-82-cosmic",  ["DC", "NATIONS", "RIV", "REBEL"]),
        ("ps-89-cosmic",  ["DC", "COV", "SEED", "KING"]),
        ("ps-110-cosmic", ["DC", "KING", "PRIEST", "SEED"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # PROVERBS
    # ═══════════════════════════════════════════════════════════════
    "data/proverbs/era_63.py": [
        ("prov-1",   ["PROV", "DC", "SPIRIT"]),
        ("prov-2-4", ["PROV", "LAW"]),
        ("prov-5-7", ["PROV", "WOMEN", "LOVE"]),
        ("prov-8-9", ["PROV", "DC", "SEED", "GLORY"]),
    ],
    "data/proverbs/era_64.py": [
        ("prov-10-12",  ["PROV", "LAW"]),
        ("prov-13-15",  ["PROV", "LAW"]),
        ("prov-16-19",  ["PROV", "KING", "DC"]),
        ("prov-20-22a", ["PROV", "KING", "DC"]),
    ],
    "data/proverbs/era_65.py": [
        ("prov-22b-24", ["PROV", "RIV", "LAW"]),
        ("prov-25-29",  ["PROV", "KING", "LOVE"]),
        ("prov-30-31",  ["PROV", "DC", "WOMEN", "SEED"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # ECCLESIASTES
    # ═══════════════════════════════════════════════════════════════
    "data/ecclesiastes/era_66.py": [
        ("eccl-1-2", ["PROV", "DC"]),
        ("eccl-3-4", ["PROV", "DC", "SPIRIT"]),
        ("eccl-5-6", ["PROV", "HOLY"]),
    ],
    "data/ecclesiastes/era_66b_fear_god.py": [
        ("eccl-7-8",   ["PROV", "DC"]),
        ("eccl-9-10",  ["PROV"]),
        ("eccl-11-12", ["PROV", "REMEMBER", "LAW"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # SONG OF SOLOMON
    # ═══════════════════════════════════════════════════════════════
    "data/songofsolomon/era_98_the_beloved.py": [
        ("song-1-2", ["LOVE", "WOMEN", "TYPE"]),
        ("song-3-5", ["LOVE", "WOMEN", "HOLY", "TYPE"]),
    ],
    "data/songofsolomon/era_98b_love_strong_as_death.py": [
        ("song-6-8", ["LOVE", "WOMEN", "COV", "NAME"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # ISAIAH
    # ═══════════════════════════════════════════════════════════════
    "data/isaiah/era_isaiah_judgment.py": [
        ("isa-1",  ["RIV", "COV", "BLOOD", "HOLY"]),
        ("isa-6",  ["DC", "HOLY", "GLORY", "SPIRIT"]),
        ("isa-7",  ["SEED", "KING", "COV"]),
        ("isa-9",  ["SEED", "KING", "DC", "NAME"]),
        ("isa-11", ["SEED", "KING", "SPIRIT", "LAND", "REMNANT"]),
        ("isa-12", ["NAME", "REVERSAL"]),
    ],
    "data/isaiah/era_isaiah_nations.py": [
        ("isa-13-14", ["DC", "REBEL", "NATIONS", "KING"]),
        ("isa-19",    ["NATIONS", "REVERSAL"]),
        ("isa-24-25", ["DC", "NATIONS", "REVERSAL", "GLORY"]),
        ("isa-17",    ["NATIONS", "REMNANT"]),
    ],
    "data/isaiah/era_isaiah_woe.py": [
        ("isa-28",    ["SEED", "COV", "DC"]),
        ("isa-36-37", ["DC", "KING", "GLORY"]),
        ("isa-29",    ["SPIRIT", "REVERSAL"]),
        ("isa-34",    ["DC", "NATIONS", "BLOOD"]),
        ("isa-35",    ["REVERSAL", "LAND", "HOLY"]),
    ],
    "data/isaiah/era_isaiah_comfort.py": [
        ("isa-40",    ["DC", "GLORY", "SPIRIT", "REVERSAL"]),
        ("isa-42",    ["SEED", "SPIRIT", "COV", "NATIONS"]),
        ("isa-45",    ["DC", "KING", "NATIONS", "NAME"]),
        ("isa-49",    ["SEED", "COV", "NATIONS", "REMNANT"]),
        ("isa-50",    ["SEED", "SPIRIT"]),
        ("isa-52-53", ["SEED", "BLOOD", "TYPE", "PRIEST", "REVERSAL"]),
        ("isa-55",    ["COV", "SEED", "LOVE"]),
    ],
    "data/isaiah/era_isaiah_servant.py": [
        ("isa-servant-1", ["SEED", "SPIRIT", "NATIONS", "COV"]),
        ("isa-servant-2", ["SEED", "COV", "NATIONS", "REMNANT"]),
        ("isa-servant-3", ["SEED", "SPIRIT"]),
        ("isa-servant-4", ["SEED", "BLOOD", "TYPE", "PRIEST", "REVERSAL"]),
        ("isa-servant-5", ["SEED", "COV", "NATIONS", "REVERSAL"]),
    ],
    "data/isaiah/era_isaiah_new.py": [
        ("isa-56-57", ["COV", "HOLY", "NATIONS"]),
        ("isa-58-59", ["RIV", "BLOOD", "SPIRIT"]),
        ("isa-60-62", ["GLORY", "SEED", "REVERSAL", "LAND"]),
        ("isa-63-64", ["BLOOD", "REMEMBER", "RIV"]),
        ("isa-65-66", ["LAND", "REVERSAL", "GLORY", "HOLY"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # JEREMIAH
    # ═══════════════════════════════════════════════════════════════
    "data/jeremiah/era_67_call_early.py": [
        ("jer-1",    ["SPIRIT", "DC", "NATIONS"]),
        ("jer-2-3",  ["COV", "RIV", "LOVE"]),
        ("jer-7",    ["HOLY", "RIV", "LAW"]),
        ("jer-4-6",  ["RIV", "EXILE"]),
        ("jer-8-10", ["RIV", "PROV"]),
    ],
    "data/jeremiah/era_68_confessions.py": [
        ("jer-11-12", ["COV", "RIV", "SPIRIT"]),
        ("jer-15-20", ["SPIRIT", "RIV"]),
        ("jer-23",    ["SEED", "KING", "DC", "NAME"]),
        ("jer-25",    ["NATIONS", "EXILE", "DC"]),
    ],
    "data/jeremiah/era_69_new_covenant.py": [
        ("jer-26-29", ["EXILE", "RIV"]),
        ("jer-31",    ["COV", "SEED", "REVERSAL", "LOVE", "SPIRIT"]),
        ("jer-36-39", ["EXILE", "KING"]),
    ],
    "data/jeremiah/era_70_aftermath.py": [
        ("jer-40-44", ["EXILE", "REMNANT"]),
        ("jer-46-51", ["NATIONS", "DC"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # LAMENTATIONS
    # ═══════════════════════════════════════════════════════════════
    "data/lamentations/era_75.py": [
        ("lam-1", ["EXILE", "RIV", "HOLY"]),
        ("lam-2", ["EXILE", "RIV", "GLORY"]),
        ("lam-3", ["EXILE", "COV", "LOVE", "REMEMBER"]),
    ],
    "data/lamentations/era_75b_prayer.py": [
        ("lam-4", ["EXILE", "BLOOD", "KING"]),
        ("lam-5", ["EXILE", "REMEMBER", "COV"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # EZEKIEL
    # ═══════════════════════════════════════════════════════════════
    "data/ezekiel/era_71_throne_vision.py": [
        ("ezek-1",    ["DC", "GLORY", "SPIRIT"]),
        ("ezek-2-5",  ["DC", "SPIRIT", "RIV"]),
        ("ezek-8-11", ["GLORY", "HOLY", "DC", "REBEL"]),
    ],
    "data/ezekiel/era_72_judgment.py": [
        ("ezek-12-15", ["EXILE", "RIV"]),
        ("ezek-16-18", ["COV", "RIV", "WOMEN", "BLOOD"]),
        ("ezek-24",    ["EXILE", "HOLY"]),
    ],
    "data/ezekiel/era_73_nations.py": [
        ("ezek-25-27", ["NATIONS", "DC"]),
        ("ezek-28",    ["DC", "REBEL", "KING"]),
        ("ezek-29-32", ["NATIONS", "DC"]),
    ],
    "data/ezekiel/era_74_restoration.py": [
        ("ezek-33-34", ["SEED", "KING", "REMNANT"]),
        ("ezek-36-37", ["SPIRIT", "COV", "LAND", "REVERSAL"]),
        ("ezek-40-48", ["HOLY", "GLORY", "PRIEST", "LAND"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # DANIEL
    # ═══════════════════════════════════════════════════════════════
    "data/daniel/era_daniel_court.py": [
        ("dan-1-2", ["DREAM", "KING", "DC", "NATIONS"]),
        ("dan-3",   ["KING", "HOLY", "NAME"]),
        ("dan-4-5", ["DREAM", "KING", "DC", "NATIONS"]),
        ("dan-6",   ["DC", "KING"]),
    ],
    "data/daniel/era_daniel_visions.py": [
        ("dan-7",     ["DC", "KING", "SEED", "NATIONS", "DREAM"]),
        ("dan-8",     ["DC", "NATIONS", "DREAM"]),
        ("dan-9",     ["COV", "SEED", "BLOOD", "HOLY"]),
        ("dan-10-12", ["DC", "NATIONS", "DREAM", "SPIRIT", "GLORY"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # HOSEA (individual chapter IDs)
    # ═══════════════════════════════════════════════════════════════
    "data/hosea/era_76_hosea_marriage.py": [
        ("hosea-1", ["COV", "LOVE", "WOMEN", "SEED", "TYPE"]),
        ("hosea-2", ["COV", "LOVE", "WOMEN", "LAND", "REVERSAL"]),
        ("hosea-3", ["COV", "LOVE", "WOMEN", "TYPE"]),
        ("hosea-4", ["RIV", "COV", "PRIEST"]),
        ("hosea-5", ["RIV", "COV"]),
        ("hosea-6", ["COV", "RIV", "LOVE"]),
        ("hosea-7", ["RIV", "REBEL"]),
    ],
    "data/hosea/era_77_hosea_judgment.py": [
        ("hosea-8",  ["COV", "RIV", "REBEL"]),
        ("hosea-9",  ["EXILE", "RIV"]),
        ("hosea-10", ["RIV", "REBEL"]),
        ("hosea-11", ["LOVE", "SEED", "REVERSAL"]),
        ("hosea-12", ["COV", "REMEMBER"]),
        ("hosea-13", ["REBEL", "SEED"]),
        ("hosea-14", ["LOVE", "REVERSAL", "REMNANT"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # JOEL
    # ═══════════════════════════════════════════════════════════════
    "data/joel/era_78_joel_day.py": [
        ("joel-1", ["RIV", "LAND", "HOLY"]),
        ("joel-2", ["DC", "NATIONS", "REVERSAL"]),
    ],
    "data/joel/era_78b_spirit.py": [
        ("joel-2b", ["SPIRIT", "REVERSAL", "DC"]),
        ("joel-3",  ["NATIONS", "DC", "RIV"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # AMOS
    # ═══════════════════════════════════════════════════════════════
    "data/amos/era_79_amos_justice.py": [
        ("amos-1",   ["RIV", "NATIONS", "COV"]),
        ("amos-3-4", ["RIV", "DC", "HOLY"]),
    ],
    "data/amos/era_79b_visions_hope.py": [
        ("amos-5-6", ["RIV", "HOLY"]),
        ("amos-7-9", ["DC", "RIV", "SEED", "REMNANT", "LAND", "REVERSAL"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # OBADIAH
    # ═══════════════════════════════════════════════════════════════
    "data/obadiah/era_80_obadiah.py": [
        ("obadiah-1", ["NATIONS", "RIV", "LAND"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # JONAH
    # ═══════════════════════════════════════════════════════════════
    "data/jonah/era_81_jonah.py": [
        ("jonah-1", ["NATIONS", "SPIRIT", "TYPE"]),
        ("jonah-2", ["SPIRIT", "TYPE"]),
    ],
    "data/jonah/era_81b_nineveh.py": [
        ("jonah-3", ["NATIONS", "REVERSAL"]),
        ("jonah-4", ["NATIONS", "LOVE"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # MICAH
    # ═══════════════════════════════════════════════════════════════
    "data/micah/era_82_micah.py": [
        ("micah-1-3", ["RIV", "EXILE", "DC"]),
        ("micah-4-5", ["SEED", "KING", "NATIONS", "REMNANT"]),
    ],
    "data/micah/era_82b_covenant_mercy.py": [
        ("micah-6-7", ["RIV", "COV", "LOVE", "REMNANT"]),
    ],
    "data/micah/era_micah_riv.py": [
        ("micah-riv-1",        ["RIV", "COV", "DC"]),
        ("micah-riv-2",        ["RIV", "SEED", "KING"]),
        ("micah-riv-3",        ["RIV", "COV", "LOVE", "REMNANT"]),
        ("micah-riv-insert-1", ["SEED", "KING", "NATIONS"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # NAHUM
    # ═══════════════════════════════════════════════════════════════
    "data/nahum/era_83_nahum.py": [
        ("nahum-1", ["DC", "NATIONS", "GLORY"]),
        ("nahum-2", ["NATIONS", "DC", "RIV"]),
    ],
    "data/nahum/era_83b_fall.py": [
        ("nahum-3", ["NATIONS", "DC", "RIV"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # HABAKKUK
    # ═══════════════════════════════════════════════════════════════
    "data/habakkuk/era_84_habakkuk.py": [
        ("habakkuk-1", ["RIV", "DC", "PROV"]),
        ("habakkuk-2", ["RIV", "DC", "NATIONS"]),
    ],
    "data/habakkuk/era_84b_theophany.py": [
        ("habakkuk-3", ["DC", "GLORY", "SPIRIT"]),
    ],
    "data/habakkuk/era_habakkuk_theodicy.py": [
        ("habakkuk-theodicy-1", ["RIV", "DC", "PROV"]),
        ("habakkuk-theodicy-2", ["RIV", "DC", "NATIONS"]),
        ("habakkuk-theodicy-3", ["DC", "GLORY", "SPIRIT"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # ZEPHANIAH
    # ═══════════════════════════════════════════════════════════════
    "data/zephaniah/era_85_zephaniah.py": [
        ("zephaniah-1", ["DC", "NATIONS", "RIV"]),
        ("zephaniah-2", ["NATIONS", "RIV"]),
    ],
    "data/zephaniah/era_85b_remnant.py": [
        ("zephaniah-3", ["REMNANT", "REVERSAL", "LOVE", "KING"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # HAGGAI
    # ═══════════════════════════════════════════════════════════════
    "data/haggai/era_86_haggai.py": [
        ("haggai-1", ["HOLY", "GLORY", "SPIRIT"]),
        ("haggai-2", ["GLORY", "SEED", "COV"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # ZECHARIAH (individual chapter IDs)
    # ═══════════════════════════════════════════════════════════════
    "data/zechariah/era_87_zechariah_visions.py": [
        ("zechariah-1",   ["DC", "SPIRIT", "NATIONS"]),
        ("zechariah-2",   ["DC", "GLORY", "LAND"]),
        ("zechariah-3",   ["DC", "PRIEST", "SEED"]),
        ("zechariah-4",   ["DC", "SPIRIT", "SEED"]),
        ("zechariah-5-6", ["DC", "SPIRIT"]),
        ("zechariah-7-8", ["COV", "REMNANT", "NATIONS"]),
    ],
    "data/zechariah/era_88_zechariah_messianic.py": [
        ("zechariah-9-10",  ["SEED", "KING", "NATIONS"]),
        ("zechariah-11",    ["SEED", "BLOOD", "COV"]),
        ("zechariah-12-13", ["SEED", "BLOOD", "SPIRIT", "DC"]),
        ("zechariah-14",    ["KING", "DC", "NATIONS", "HOLY"]),
    ],
    "data/zechariah/era_zechariah_council.py": [
        ("zechariah-council-1", ["DC", "PRIEST", "SEED"]),
        ("zechariah-council-2", ["DC", "KING", "PRIEST", "SEED"]),
        ("zechariah-council-3", ["DC", "SPIRIT", "SEED"]),
    ],

    # ═══════════════════════════════════════════════════════════════
    # MALACHI
    # ═══════════════════════════════════════════════════════════════
    "data/malachi/era_89_malachi.py": [
        ("malachi-1", ["COV", "RIV", "PRIEST", "LOVE"]),
        ("malachi-2", ["COV", "RIV", "PRIEST"]),
    ],
    "data/malachi/era_89b_messenger.py": [
        ("malachi-3", ["COV", "PRIEST", "SEED", "RIV", "HOLY"]),
        ("malachi-4", ["COV", "SEED", "REVERSAL"]),
    ],
}


def add_themes_to_file(rel_path, chapter_themes):
    """Add themes field after "type" field in each matching chapter dict."""
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        print(f"  WARNING: File not found: {full_path}")
        return False

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if themes already exist
    if '"themes"' in content:
        print(f"  SKIP (already has themes): {rel_path}")
        return True

    # Build a lookup from chapter_id -> themes list
    theme_lookup = {cid: themes for cid, themes in chapter_themes}

    modified = False
    lines = content.split("\n")
    new_lines = []
    current_id = None
    i = 0
    while i < len(lines):
        line = lines[i]

        # Track current chapter ID
        id_match = re.search(r'"id":\s*"([^"]+)"', line)
        if id_match:
            current_id = id_match.group(1)

        # Find "type": "chapter" lines and insert themes after
        type_match = re.search(r'^(\s*)"type":\s*"chapter"', line)
        if type_match and current_id and current_id in theme_lookup:
            indent = type_match.group(1)
            themes = theme_lookup[current_id]
            themes_str = ", ".join(f'"{t}"' for t in themes)
            # Add the type line
            new_lines.append(line)
            # Add themes line after
            new_lines.append(f'{indent}"themes": [{themes_str}],')
            modified = True
            i += 1
            continue

        new_lines.append(line)
        i += 1

    if modified:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        count = sum(1 for cid in theme_lookup if cid in [c for c, _ in chapter_themes])
        print(f"  OK: {rel_path} ({len(chapter_themes)} chapters)")
    else:
        print(f"  NO CHANGES: {rel_path}")

    return modified


def main():
    total_files = 0
    total_chapters = 0
    for rel_path, chapter_themes in sorted(THEME_MAP.items()):
        print(f"Processing {rel_path}...")
        add_themes_to_file(rel_path, chapter_themes)
        total_files += 1
        total_chapters += len(chapter_themes)
    print(f"\nDone. Processed {total_files} files, {total_chapters} chapters.")


if __name__ == "__main__":
    main()
