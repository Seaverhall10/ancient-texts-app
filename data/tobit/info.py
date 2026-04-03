"""
info.py — Tobit: Scholarly Text Introduction

Second Temple narrative featuring angelology and demonology,
preserved in the Dead Sea Scrolls and deuterocanonical collections.
"""

TEXT_INFO = {
    "text_id": "tobit",
    "display_name": "Tobit",
    "full_title": "The Book of Tobit",

    "canonical_status": {
        "status": "deuterocanonical",
        "label": "Deuterocanonical (Catholic & Orthodox canon; not in Protestant canon)",
        "detail": "Tobit is included in the Catholic and Eastern Orthodox Old Testament canons "
                  "but excluded from the Protestant canon. Jerome included it in the Vulgate "
                  "but noted it was not part of the Hebrew canon. Fragments in Aramaic and "
                  "Hebrew were discovered among the Dead Sea Scrolls (4Q196-200), confirming "
                  "its antiquity and Jewish origin."
    },

    "authorship": {
        "traditional": "The text presents itself as the memoir of Tobit, a pious Israelite "
                       "from the tribe of Naphtali deported to Nineveh after the Assyrian "
                       "conquest of the northern kingdom.",
        "scholarly_debate": "Universally regarded as a work of historical fiction composed "
                           "during the Second Temple period. The author is unknown. The "
                           "narrative combines wisdom instruction, prayer, and angelology "
                           "within a diaspora setting.",
        "bottom_line": "An anonymous Jewish author writing during the Persian or early "
                       "Hellenistic period, using the Assyrian exile as a narrative backdrop "
                       "to teach about faithfulness, prayer, and divine providence."
    },

    "date": {
        "traditional": "Set during the Assyrian exile (8th-7th century BC).",
        "critical_range": "Composed ~200 BC, possibly earlier. The Aramaic and Hebrew "
                         "fragments at Qumran (4Q196-200) date to ~100 BC, establishing "
                         "a firm terminus ante quem.",
        "evidence": "The Dead Sea Scrolls preserve four Aramaic manuscripts and one "
                    "Hebrew manuscript of Tobit. The Aramaic version appears to be the "
                    "original language. The theological vocabulary and concerns align "
                    "with 3rd-2nd century BC Jewish literature."
    },

    "audience": {
        "original_audience": "Jews living in the diaspora or under foreign rule, facing "
                            "questions about maintaining faithfulness away from the Temple.",
        "purpose": "Tobit teaches that God rewards faithfulness even in exile. It addresses "
                   "proper burial of the dead, almsgiving, endogamy (marriage within the "
                   "community), and trust in divine providence. The angel Raphael and the "
                   "demon Asmodeus provide a window into Second Temple angelology and "
                   "demonology.",
        "theological_intent": "Demonstrates God's active care for the righteous through "
                             "angelic intervention, even when circumstances appear hopeless."
    },

    "language": {
        "original": "Aramaic (primary) with one Hebrew manuscript also found at Qumran. "
                    "The Aramaic is likely the original language.",
        "script": "Aramaic square script (Qumran fragments), translated into Greek "
                  "(two major recensions: short GI and long GII).",
        "linguistic_notes": "The longer Greek recension (GII, Sinaiticus) is generally "
                           "considered closer to the Semitic original. The shorter "
                           "recension (GI, Vaticanus/Alexandrinus) appears to be an "
                           "abridgment."
    },

    "manuscripts": {
        "earliest": "Aramaic and Hebrew fragments from Qumran Cave 4 (4Q196-200), "
                    "dating to ~100 BC.",
        "major_witnesses": [
            {"name": "4Q196-199 (Aramaic)", "date": "~100 BC",
             "note": "Four Aramaic manuscripts from Qumran preserving portions of Tobit."},
            {"name": "4Q200 (Hebrew)", "date": "~100 BC",
             "note": "One Hebrew manuscript from Qumran."},
            {"name": "Codex Sinaiticus (GII)", "date": "4th century AD",
             "note": "Longer Greek recension, generally preferred by scholars."},
            {"name": "Codex Vaticanus / Alexandrinus (GI)", "date": "4th-5th century AD",
             "note": "Shorter Greek recension."}
        ],
        "reliability": "The Qumran fragments confirm the Semitic origin and support the "
                       "longer Greek recension (GII) as closer to the original."
    },

    "historical_context": {
        "setting": "Set in Nineveh during the Assyrian exile (8th-7th century BC), but "
                   "composed during the Second Temple period. The story reflects diaspora "
                   "concerns: maintaining Jewish identity, proper worship, and trust in "
                   "God far from the Temple.",
        "geography": "The narrative moves between Nineveh (Tobit's location) and Ecbatana "
                     "in Media (where Sarah lives). Tobias journeys with the angel Raphael "
                     "along the Tigris River.",
        "historical_connections": "Tobit provides important evidence for Second Temple "
                                 "Jewish beliefs about angels (Raphael as one of seven "
                                 "archangels) and demons (Asmodeus). These traditions "
                                 "illuminate the angelology and demonology presupposed "
                                 "by the New Testament authors."
    },

    "reader_notes": [
        {
            "type": "authority",
            "title": "Deuterocanonical Status",
            "body": "Tobit is deuterocanonical (included in Catholic and Orthodox canons "
                    "but not in the Protestant or Jewish canons). This app treats it as "
                    "valuable Second Temple literature, not as canonical Scripture. Its "
                    "angelology and demonology provide important context for understanding "
                    "the New Testament supernatural worldview."
        },
        {
            "type": "context",
            "title": "Raphael and Asmodeus",
            "body": "Tobit is one of the earliest Jewish texts naming specific angels "
                    "(Raphael) and demons (Asmodeus). According to Tobit 12:15, Raphael "
                    "identifies himself as 'one of the seven holy angels who present the "
                    "prayers of the saints,' a tradition echoed in Revelation 8:2. "
                    "Asmodeus becomes a significant figure in later Jewish demonology."
        }
    ]
}
