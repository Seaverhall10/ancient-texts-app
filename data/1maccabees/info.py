"""
info.py — 1 Maccabees: Scholarly Text Introduction

Historical account of the Maccabean revolt and Hasmonean dynasty,
written in biblical style echoing Joshua and Judges.
"""

TEXT_INFO = {
    "text_id": "1maccabees",
    "display_name": "1 Maccabees",
    "full_title": "The First Book of the Maccabees",

    "canonical_status": {
        "status": "deuterocanonical",
        "label": "Deuterocanonical (Catholic & Orthodox canon; not in Protestant canon)",
        "detail": "1 Maccabees is included in the Catholic and Eastern Orthodox Old Testament "
                  "canons but excluded from the Protestant canon. Written originally in Hebrew "
                  "(now lost), it survives in the Greek Septuagint. Josephus relied heavily on "
                  "1 Maccabees as a historical source for his Antiquities (Books 12-13), "
                  "treating it as reliable history. The Hebrew original is attested by Jerome "
                  "and confirmed by pervasive Hebraisms in the Greek text."
    },

    "authorship": {
        "traditional": "Anonymous. The text provides no internal claim of authorship.",
        "scholarly_debate": "The author was almost certainly a Palestinian Jew and a supporter "
                           "of the Hasmonean dynasty. The narrative style deliberately echoes "
                           "the biblical historical books — Joshua, Judges, Samuel, and Kings — "
                           "presenting the Maccabees as divinely appointed deliverers in the "
                           "pattern of the Judges. The author had access to official Hasmonean "
                           "records, Seleucid diplomatic documents, and possibly temple archives.",
        "bottom_line": "An anonymous Jewish author writing in a deliberately biblical style, "
                       "likely connected to the Hasmonean court, composing a theological "
                       "history that legitimizes the Maccabee family as God's chosen instruments."
    },

    "date": {
        "traditional": "c. 104 BC, shortly after the death of John Hyrcanus I.",
        "critical_range": "140-100 BC. The narrative concludes with the accession of John "
                         "Hyrcanus (16:23-24) and refers to a chronicle of his high priesthood, "
                         "suggesting composition after his death (104 BC). The author shows no "
                         "awareness of the Roman conquest of Judea (63 BC), providing a firm "
                         "terminus ante quem.",
        "evidence": "The concluding formula (16:23-24) mirrors the formulaic endings of Kings, "
                    "implying the author wrote after Hyrcanus' reign ended. The generally "
                    "positive view of Rome (ch. 8) would be unlikely after Pompey's conquest. "
                    "The detailed knowledge of Seleucid diplomacy and chronology points to "
                    "access to near-contemporary records."
    },

    "audience": {
        "original_audience": "Palestinian Jews, particularly those who supported or needed to "
                            "be persuaded of the legitimacy of the Hasmonean dynasty.",
        "purpose": "To present the Maccabean revolt as a divinely guided deliverance parallel "
                   "to the great deliverances in Israel's history (Exodus, Conquest, Judges). "
                   "The text legitimizes Hasmonean rule by showing God working through Mattathias "
                   "and his sons — especially Judas, Jonathan, and Simon — to rescue Israel "
                   "from Seleucid oppression and rededicate the Temple.",
        "theological_intent": "God acts through faithful human warriors who refuse to compromise "
                             "with paganism. Unlike 2 Maccabees, divine intervention is subtle — "
                             "no angels or miracles, just faithful fighters whom God empowers."
    },

    "language": {
        "original": "Hebrew (now lost). The Hebrew original is attested by Jerome, who saw "
                    "a Hebrew copy, and confirmed by the heavily Semitic syntax of the Greek "
                    "translation.",
        "script": "The surviving text is in Greek (Septuagint). The translation is often "
                  "woodenly literal, preserving Hebrew idioms, paratactic sentence structure, "
                  "and even Hebrew poetic forms.",
        "linguistic_notes": "Characteristic Hebraisms include 'and it came to pass' (kai egeneto), "
                           "the use of 'heaven' as a circumlocution for God (the author avoids "
                           "the divine name throughout), and warfare vocabulary drawn directly "
                           "from the Hebrew Bible's battle narratives."
    },

    "manuscripts": {
        "earliest": "Greek Septuagint manuscripts from the 4th-5th century AD.",
        "major_witnesses": [
            {"name": "Codex Sinaiticus", "date": "4th century AD",
             "note": "Contains 1 Maccabees in the Old Testament section."},
            {"name": "Codex Alexandrinus", "date": "5th century AD",
             "note": "Complete text of 1 Maccabees."},
            {"name": "Codex Venetus", "date": "8th century AD",
             "note": "Important minuscule manuscript for the Maccabean books."},
            {"name": "Latin Vulgate", "date": "4th century AD (translation)",
             "note": "Jerome's Latin translation, though he noted the text was not in the Hebrew canon."}
        ],
        "reliability": "No Hebrew fragments survive. The Greek text is well preserved across "
                       "multiple manuscript families. The Lucianic recension provides an important "
                       "secondary witness. Josephus' paraphrase in Antiquities 12-13 serves as "
                       "an independent check on the Greek text."
    },

    "historical_context": {
        "setting": "The narrative covers approximately 175-134 BC: from the Seleucid persecution "
                   "under Antiochus IV Epiphanes through the establishment of the Hasmonean "
                   "dynasty under Simon and John Hyrcanus. Key events include the desecration "
                   "of the Temple (167 BC), the Maccabean revolt, the Temple rededication "
                   "(164 BC, the origin of Hanukkah), and the consolidation of Jewish independence.",
        "geography": "Centered on Judea, Jerusalem, and the surrounding regions. Military "
                     "campaigns extend to Galilee, Transjordan, Idumea, and the coastal plain. "
                     "Diplomatic missions reach Rome and Sparta.",
        "historical_connections": "1 Maccabees is considered one of the most reliable historical "
                                 "sources for the Maccabean period, comparable in quality to "
                                 "Thucydides' approach to history. It preserves copies of official "
                                 "documents (letters, decrees, treaties) that scholars generally "
                                 "regard as authentic or based on authentic originals. The book "
                                 "provides essential background for understanding Hanukkah, the "
                                 "Pharisee-Sadducee divide, and the political world Jesus entered."
    },

    "reader_notes": [
        {
            "type": "authority",
            "title": "Historical Reliability",
            "body": "1 Maccabees is considered one of the most reliable historical sources "
                    "for the second century BC in Jewish history. Its detailed chronology "
                    "(using the Seleucid era dating system), preserved documents, and sober "
                    "narrative style make it invaluable for reconstructing the Maccabean period. "
                    "Read it as serious history written with theological purpose."
        },
        {
            "type": "context",
            "title": "Hanukkah Origins",
            "body": "Chapter 4 describes the purification and rededication of the Temple after "
                    "its desecration by Antiochus IV — the event commemorated by Hanukkah. "
                    "Notably, 1 Maccabees does not mention the miracle of oil (that tradition "
                    "appears later in the Talmud, b. Shabbat 21b). The original emphasis was "
                    "on military deliverance and Temple restoration."
        },
        {
            "type": "tradition",
            "title": "Hebrew Warriors",
            "body": "The author deliberately patterns the Maccabees after biblical warriors. "
                    "Judas Maccabeus is compared to a lion (3:4), echoing Judah in Genesis 49:9. "
                    "Battle prayers echo David's confrontation with Goliath. The entire narrative "
                    "is structured to show that the same God who delivered Israel through Joshua "
                    "and the Judges is delivering them again through the Hasmoneans."
        }
    ]
}
