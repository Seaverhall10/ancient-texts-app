"""
Add all 24 missing OT books to manifest.json.
Run once, then delete this script.
"""
import json, os

MANIFEST_PATH = os.path.join(os.path.dirname(__file__), "manifest.json")

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = json.load(f)

existing_text_ids = {t["id"] for t in manifest["texts"]}
existing_era_ids = {e["id"] for e in manifest["eras"]}

# ── 24 New OT Text Entries ─────────────────────────────────
NEW_TEXTS = [
    # Wisdom Literature
    {"id": "job", "name": "Job", "category": "ot", "language": "hebrew", "chapters": 42, "color": "#8a6d4a", "data_dir": "job", "interlinear": None, "description": "Suffering, the divine council, cosmic justice, and YHWH's theophany from the whirlwind"},
    {"id": "proverbs", "name": "Proverbs", "category": "ot", "language": "hebrew", "chapters": 31, "color": "#6a8a4a", "data_dir": "proverbs", "interlinear": None, "description": "Wisdom personified, fear of YHWH, and practical instruction for covenant life"},
    {"id": "ecclesiastes", "name": "Ecclesiastes", "category": "ot", "language": "hebrew", "chapters": 12, "color": "#7a7a5a", "data_dir": "ecclesiastes", "interlinear": None, "description": "Life under the sun — hebel, wisdom's limits, and the fear of God as the whole duty of man"},
    {"id": "songofsolomon", "name": "Song of Solomon", "category": "ot", "language": "hebrew", "chapters": 8, "color": "#8a5070", "data_dir": "songofsolomon", "interlinear": None, "description": "Love poetry celebrating covenant love between beloved and lover — read as both literal and typological"},

    # Major Prophets (missing)
    {"id": "jeremiah", "name": "Jeremiah", "category": "ot", "language": "hebrew", "chapters": 52, "color": "#8a4a4a", "data_dir": "jeremiah", "interlinear": None, "description": "The weeping prophet — judgment on Judah, the new covenant promise, and the fall of Jerusalem"},
    {"id": "ezekiel", "name": "Ezekiel", "category": "ot", "language": "hebrew", "chapters": 48, "color": "#4a6a8a", "data_dir": "ezekiel", "interlinear": None, "description": "Throne visions, cherubim, the divine glory departing and returning, and the new temple"},
    {"id": "lamentations", "name": "Lamentations", "category": "ot", "language": "hebrew", "chapters": 5, "color": "#7a4a5a", "data_dir": "lamentations", "interlinear": None, "description": "Acrostic poems of grief over Jerusalem's fall — covenant curses fulfilled, hope in YHWH's faithfulness"},

    # History
    {"id": "1chronicles", "name": "1 Chronicles", "category": "ot", "language": "hebrew", "chapters": 29, "color": "#5a6a80", "data_dir": "1chronicles", "interlinear": None, "description": "Israel's genealogies and David's reign — temple preparations and the Davidic covenant"},
    {"id": "2chronicles", "name": "2 Chronicles", "category": "ot", "language": "hebrew", "chapters": 36, "color": "#506a7a", "data_dir": "2chronicles", "interlinear": None, "description": "Solomon's temple, the divided kingdom, reform and apostasy, exile and the decree of Cyrus"},
    {"id": "ezra", "name": "Ezra", "category": "ot", "language": "hebrew", "chapters": 10, "color": "#6a7a5a", "data_dir": "ezra", "interlinear": None, "description": "Return from Babylon, temple rebuilding, and covenant renewal under Persian rule"},
    {"id": "nehemiah", "name": "Nehemiah", "category": "ot", "language": "hebrew", "chapters": 13, "color": "#5a7a6a", "data_dir": "nehemiah", "interlinear": None, "description": "Rebuilding Jerusalem's walls, Ezra's Torah reading, and covenant renewal in the restored community"},
    {"id": "esther", "name": "Esther", "category": "ot", "language": "hebrew", "chapters": 10, "color": "#8a5a7a", "data_dir": "esther", "interlinear": None, "description": "Divine providence in the Persian court — Haman's plot, Esther's courage, and the feast of Purim"},

    # Minor Prophets
    {"id": "hosea", "name": "Hosea", "category": "ot", "language": "hebrew", "chapters": 14, "color": "#a0504a", "data_dir": "hosea", "interlinear": None, "description": "Covenant unfaithfulness as spiritual adultery — judgment, exile, and promised restoration"},
    {"id": "joel", "name": "Joel", "category": "ot", "language": "hebrew", "chapters": 3, "color": "#5a6a8a", "data_dir": "joel", "interlinear": None, "description": "The Day of YHWH — locust plague, call to repentance, and the outpouring of the Spirit"},
    {"id": "amos", "name": "Amos", "category": "ot", "language": "hebrew", "chapters": 9, "color": "#6a5a3a", "data_dir": "amos", "interlinear": None, "description": "Social justice, divine judgment on the nations, and cosmic visions of Israel's fate"},
    {"id": "obadiah", "name": "Obadiah", "category": "ot", "language": "hebrew", "chapters": 1, "color": "#7a6a5a", "data_dir": "obadiah", "interlinear": None, "description": "Oracle against Edom — judgment on Esau's descendants and the Day of YHWH"},
    {"id": "jonah", "name": "Jonah", "category": "ot", "language": "hebrew", "chapters": 4, "color": "#4a7a7a", "data_dir": "jonah", "interlinear": None, "description": "The reluctant prophet — divine mercy extended beyond Israel to Nineveh"},
    {"id": "micah", "name": "Micah", "category": "ot", "language": "hebrew", "chapters": 7, "color": "#8a5a6a", "data_dir": "micah", "interlinear": None, "description": "Justice, the Bethlehem prophecy, covenant lawsuit, and hope for the remnant"},
    {"id": "nahum", "name": "Nahum", "category": "ot", "language": "hebrew", "chapters": 3, "color": "#7a4a3a", "data_dir": "nahum", "interlinear": None, "description": "The fall of Nineveh — YHWH as divine warrior executing judgment on Assyria"},
    {"id": "habakkuk", "name": "Habakkuk", "category": "ot", "language": "hebrew", "chapters": 3, "color": "#5a7a5a", "data_dir": "habakkuk", "interlinear": None, "description": "Theodicy dialogue with YHWH — 'the righteous shall live by faith' and the divine warrior theophany"},
    {"id": "zephaniah", "name": "Zephaniah", "category": "ot", "language": "hebrew", "chapters": 3, "color": "#6a5a7a", "data_dir": "zephaniah", "interlinear": None, "description": "The great Day of YHWH — cosmic judgment, purification, and the humble remnant"},
    {"id": "haggai", "name": "Haggai", "category": "ot", "language": "hebrew", "chapters": 2, "color": "#8a7a4a", "data_dir": "haggai", "interlinear": None, "description": "Rebuilding the temple — the glory of the latter house will surpass the former"},
    {"id": "zechariah", "name": "Zechariah", "category": "ot", "language": "hebrew", "chapters": 14, "color": "#4a6a6a", "data_dir": "zechariah", "interlinear": None, "description": "Night visions, the divine council, messianic prophecy, and the pierced one of Zechariah 12"},
    {"id": "malachi", "name": "Malachi", "category": "ot", "language": "hebrew", "chapters": 4, "color": "#7a5a4a", "data_dir": "malachi", "interlinear": None, "description": "Covenant faithfulness, the coming messenger, tithes, and the Elijah prophecy"},
]

# ── New Era Entries ────────────────────────────────────────
NEW_ERAS = [
    # Job (eras 60-62)
    {"id": "job_prologue", "text": "job", "name": "Prologue & Dialogues", "chapters": "Job 1\u201314", "color": "#8a6d4a", "icon": "I", "data_file": "era_60_prologue", "themes": ["Divine council scene", "Satan as accuser", "Suffering of the righteous", "First dialogue cycle"]},
    {"id": "job_dialogues", "text": "job", "name": "Dialogues & Elihu", "chapters": "Job 15\u201337", "color": "#8a6d4a", "icon": "II", "data_file": "era_61_dialogues", "themes": ["Second and third cycles", "Wisdom hymn (ch 28)", "Elihu speeches", "Theodicy"]},
    {"id": "job_theophany", "text": "job", "name": "Theophany & Restoration", "chapters": "Job 38\u201342", "color": "#8a6d4a", "icon": "III", "data_file": "era_62_theophany", "themes": ["YHWH speaks from whirlwind", "Cosmic interrogation", "Leviathan and Behemoth", "Restoration"]},

    # Proverbs (eras 63-65)
    {"id": "prov_royal", "text": "proverbs", "name": "Royal Wisdom", "chapters": "Proverbs 1\u20139", "color": "#6a8a4a", "icon": "I", "data_file": "era_63_royal_wisdom", "themes": ["Wisdom personified", "Woman Wisdom vs Woman Folly", "Fear of YHWH", "Parental instruction"]},
    {"id": "prov_solomonic", "text": "proverbs", "name": "Solomonic Proverbs", "chapters": "Proverbs 10\u201322:16", "color": "#6a8a4a", "icon": "II", "data_file": "era_64_solomonic", "themes": ["Antithetic parallelism", "Righteous vs wicked", "Speech ethics", "Wealth and poverty"]},
    {"id": "prov_collections", "text": "proverbs", "name": "Collections & Conclusion", "chapters": "Proverbs 22:17\u201331", "color": "#6a8a4a", "icon": "III", "data_file": "era_65_collections", "themes": ["Words of the Wise", "Agur's oracle", "King Lemuel", "Proverbs 31 woman"]},

    # Ecclesiastes (era 66)
    {"id": "eccl_under_sun", "text": "ecclesiastes", "name": "Under the Sun", "chapters": "Ecclesiastes 1\u201312", "color": "#7a7a5a", "icon": "I", "data_file": "era_66_under_the_sun", "themes": ["Hebel (vapor/vanity)", "Life under the sun", "Wisdom's limits", "Fear God and keep commandments"]},

    # Jeremiah (eras 67-70)
    {"id": "jer_call", "text": "jeremiah", "name": "Call & Early Oracles", "chapters": "Jeremiah 1\u201310", "color": "#8a4a4a", "icon": "I", "data_file": "era_67_call", "themes": ["Prophetic commission", "Temple sermon", "Idolatry indictment", "Broken covenant"]},
    {"id": "jer_confessions", "text": "jeremiah", "name": "Confessions & Conflict", "chapters": "Jeremiah 11\u201325", "color": "#8a4a4a", "icon": "II", "data_file": "era_68_confessions", "themes": ["Jeremiah's laments", "False prophets", "Seventy years prophecy", "Cup of wrath"]},
    {"id": "jer_new_covenant", "text": "jeremiah", "name": "New Covenant & Fall", "chapters": "Jeremiah 26\u201339", "color": "#8a4a4a", "icon": "III", "data_file": "era_69_new_covenant", "themes": ["New covenant (31:31-34)", "Temple sermon trial", "Siege of Jerusalem", "Fall of the city"]},
    {"id": "jer_aftermath", "text": "jeremiah", "name": "Aftermath & Oracles", "chapters": "Jeremiah 40\u201352", "color": "#8a4a4a", "icon": "IV", "data_file": "era_70_aftermath", "themes": ["Gedaliah assassination", "Flight to Egypt", "Oracles against nations", "Fall of Babylon"]},

    # Ezekiel (eras 71-74)
    {"id": "ezek_throne", "text": "ezekiel", "name": "Call & Throne Vision", "chapters": "Ezekiel 1\u201311", "color": "#4a6a8a", "icon": "I", "data_file": "era_71_throne", "themes": ["Merkabah throne chariot", "Cherubim vision", "Prophetic commission", "Glory departing temple"]},
    {"id": "ezek_judgment", "text": "ezekiel", "name": "Judgment Oracles", "chapters": "Ezekiel 12\u201324", "color": "#4a6a8a", "icon": "II", "data_file": "era_72_judgment", "themes": ["Symbolic acts", "False prophets", "Allegories of Jerusalem", "Covenant unfaithfulness"]},
    {"id": "ezek_nations", "text": "ezekiel", "name": "Against the Nations", "chapters": "Ezekiel 25\u201332", "color": "#4a6a8a", "icon": "III", "data_file": "era_73_nations", "themes": ["Prince of Tyre (ch 28)", "Fallen guardian cherub", "Egypt oracles", "Cosmic warfare"]},
    {"id": "ezek_restoration", "text": "ezekiel", "name": "Restoration & Temple", "chapters": "Ezekiel 33\u201348", "color": "#4a6a8a", "icon": "IV", "data_file": "era_74_restoration", "themes": ["Valley of dry bones", "Gog and Magog", "New temple vision", "River of life"]},

    # Lamentations (era 75)
    {"id": "lam_weeping", "text": "lamentations", "name": "Weeping Over Zion", "chapters": "Lamentations 1\u20135", "color": "#7a4a5a", "icon": "I", "data_file": "era_75_weeping", "themes": ["Acrostic poetry", "Daughter Zion personified", "Covenant curses fulfilled", "Hope in YHWH's faithfulness"]},

    # Hosea (eras 76-77)
    {"id": "hosea_marriage", "text": "hosea", "name": "Marriage & Judgment", "chapters": "Hosea 1\u20137", "color": "#a0504a", "icon": "I", "data_file": "era_76_marriage", "themes": ["Gomer marriage", "Covenant adultery", "Lo-Ammi (Not My People)", "Divine love"]},
    {"id": "hosea_restoration", "text": "hosea", "name": "Judgment & Restoration", "chapters": "Hosea 8\u201314", "color": "#a0504a", "icon": "II", "data_file": "era_77_restoration", "themes": ["Reaping the whirlwind", "YHWH's compassion", "Return to covenant", "Resurrection hope"]},

    # Joel (era 78)
    {"id": "joel_day", "text": "joel", "name": "The Day of YHWH", "chapters": "Joel 1\u20133", "color": "#5a6a8a", "icon": "I", "data_file": "era_78_day_of_yhwh", "themes": ["Locust plague", "Call to repentance", "Spirit outpouring", "Valley of decision"]},

    # Amos (era 79)
    {"id": "amos_justice", "text": "amos", "name": "Justice & Judgment", "chapters": "Amos 1\u20139", "color": "#6a5a3a", "icon": "I", "data_file": "era_79_justice", "themes": ["Oracles against nations", "Social justice", "Five visions", "Fallen booth of David"]},

    # Obadiah (era 80)
    {"id": "obad_edom", "text": "obadiah", "name": "Edom's Judgment", "chapters": "Obadiah 1", "color": "#7a6a5a", "icon": "I", "data_file": "era_80_edom", "themes": ["Jacob vs Esau", "Edom's pride", "Day of YHWH", "Kingdom belongs to YHWH"]},

    # Jonah (era 81)
    {"id": "jonah_mercy", "text": "jonah", "name": "The Reluctant Prophet", "chapters": "Jonah 1\u20134", "color": "#4a7a7a", "icon": "I", "data_file": "era_81_mercy", "themes": ["Flight from YHWH", "Great fish", "Nineveh repents", "Divine mercy to nations"]},

    # Micah (era 82)
    {"id": "micah_justice", "text": "micah", "name": "Justice & Hope", "chapters": "Micah 1\u20137", "color": "#8a5a6a", "icon": "I", "data_file": "era_82_justice", "themes": ["Covenant lawsuit", "Bethlehem prophecy (5:2)", "Do justice, love mercy", "Shepherd of the remnant"]},

    # Nahum (era 83)
    {"id": "nahum_nineveh", "text": "nahum", "name": "Fall of Nineveh", "chapters": "Nahum 1\u20133", "color": "#7a4a3a", "icon": "I", "data_file": "era_83_nineveh", "themes": ["Divine warrior hymn", "YHWH's jealousy", "Nineveh's destruction", "Cosmic judgment"]},

    # Habakkuk (era 84)
    {"id": "hab_dialogue", "text": "habakkuk", "name": "Faith in Crisis", "chapters": "Habakkuk 1\u20133", "color": "#5a7a5a", "icon": "I", "data_file": "era_84_dialogue", "themes": ["Theodicy dialogue", "Righteous shall live by faith", "Woe oracles", "Divine warrior theophany"]},

    # Zephaniah (era 85)
    {"id": "zeph_day", "text": "zephaniah", "name": "The Great Day", "chapters": "Zephaniah 1\u20133", "color": "#6a5a7a", "icon": "I", "data_file": "era_85_great_day", "themes": ["Cosmic de-creation", "Day of YHWH's wrath", "Humble remnant", "YHWH rejoices over Zion"]},

    # Haggai (era 86)
    {"id": "haggai_temple", "text": "haggai", "name": "Rebuild the Temple", "chapters": "Haggai 1\u20132", "color": "#8a7a4a", "icon": "I", "data_file": "era_86_temple", "themes": ["Temple rebuilding call", "Glory of latter house", "Zerubbabel as signet", "Shaking of nations"]},

    # Zechariah (eras 87-88)
    {"id": "zech_visions", "text": "zechariah", "name": "Night Visions", "chapters": "Zechariah 1\u20138", "color": "#4a6a6a", "icon": "I", "data_file": "era_87_visions", "themes": ["Eight night visions", "Divine council (ch 3)", "Satan rebuked", "Branch/priest-king"]},
    {"id": "zech_oracle", "text": "zechariah", "name": "Messianic Oracles", "chapters": "Zechariah 9\u201314", "color": "#4a6a6a", "icon": "II", "data_file": "era_88_oracle", "themes": ["Humble king on donkey", "Shepherd struck", "Pierced one (12:10)", "Living waters from Jerusalem"]},

    # Malachi (era 89)
    {"id": "mal_covenant", "text": "malachi", "name": "Covenant Faithfulness", "chapters": "Malachi 1\u20134", "color": "#7a5a4a", "icon": "I", "data_file": "era_89_covenant", "themes": ["Polluted offerings", "Covenant of marriage", "Messenger of the covenant", "Elijah before the Day"]},

    # 1 Chronicles (eras 90-91)
    {"id": "1chr_genealogies", "text": "1chronicles", "name": "Genealogies & David's Rise", "chapters": "1 Chronicles 1\u201316", "color": "#5a6a80", "icon": "I", "data_file": "era_90_genealogies", "themes": ["Genealogical prologue", "David's kingdom established", "Ark to Jerusalem", "Levitical worship"]},
    {"id": "1chr_temple", "text": "1chronicles", "name": "David's Kingdom & Temple Plans", "chapters": "1 Chronicles 17\u201329", "color": "#5a6a80", "icon": "II", "data_file": "era_91_temple_plans", "themes": ["Davidic covenant", "Satan and the census", "Temple preparations", "Solomon's charge"]},

    # 2 Chronicles (eras 92-94)
    {"id": "2chr_solomon", "text": "2chronicles", "name": "Solomon's Glory", "chapters": "2 Chronicles 1\u20139", "color": "#506a7a", "icon": "I", "data_file": "era_92_solomon", "themes": ["Temple construction", "Dedication prayer", "YHWH's glory fills temple", "Queen of Sheba"]},
    {"id": "2chr_divided", "text": "2chronicles", "name": "Divided Kingdom", "chapters": "2 Chronicles 10\u201328", "color": "#506a7a", "icon": "II", "data_file": "era_93_divided", "themes": ["Rehoboam's folly", "Asa and Jehoshaphat", "Micaiah's vision (ch 18)", "Reform and apostasy"]},
    {"id": "2chr_exile", "text": "2chronicles", "name": "Final Kings & Exile", "chapters": "2 Chronicles 29\u201336", "color": "#506a7a", "icon": "III", "data_file": "era_94_exile", "themes": ["Hezekiah's reform", "Josiah's renewal", "Fall of Jerusalem", "Cyrus decree"]},

    # Ezra (era 95)
    {"id": "ezra_return", "text": "ezra", "name": "Return & Rebuilding", "chapters": "Ezra 1\u201310", "color": "#6a7a5a", "icon": "I", "data_file": "era_95_return", "themes": ["Cyrus decree", "Temple foundation", "Opposition and completion", "Mixed marriages crisis"]},

    # Nehemiah (era 96)
    {"id": "neh_walls", "text": "nehemiah", "name": "Walls & Renewal", "chapters": "Nehemiah 1\u201313", "color": "#5a7a6a", "icon": "I", "data_file": "era_96_walls", "themes": ["Nehemiah's prayer", "Wall rebuilding", "Torah reading (Ezra)", "Covenant renewal"]},

    # Esther (era 97)
    {"id": "esther_providence", "text": "esther", "name": "For Such a Time", "chapters": "Esther 1\u201310", "color": "#8a5a7a", "icon": "I", "data_file": "era_97_providence", "themes": ["Vashti's refusal", "Esther chosen", "Haman's plot", "Purim established"]},

    # Song of Solomon (era 98)
    {"id": "song_beloved", "text": "songofsolomon", "name": "The Beloved", "chapters": "Song of Solomon 1\u20138", "color": "#8a5070", "icon": "I", "data_file": "era_98_beloved", "themes": ["Love poetry", "Covenant love", "Garden imagery", "Typological reading"]},
]

# ── Insert into manifest ──────────────────────────────────
added_texts = 0
added_eras = 0

for t in NEW_TEXTS:
    if t["id"] not in existing_text_ids:
        manifest["texts"].append(t)
        added_texts += 1
    else:
        print(f"  SKIP text {t['id']} (already exists)")

for e in NEW_ERAS:
    if e["id"] not in existing_era_ids:
        manifest["eras"].append(e)
        added_eras += 1
    else:
        print(f"  SKIP era {e['id']} (already exists)")

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"\nDone! Added {added_texts} texts and {added_eras} eras to manifest.json")
print(f"Total texts: {len(manifest['texts'])}")
print(f"Total eras: {len(manifest['eras'])}")
