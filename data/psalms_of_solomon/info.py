"""
info.py — Psalms of Solomon: Scholarly Text Introduction

First-century BC psalms with significant messianic expectations,
providing crucial background for understanding Jewish hopes
at the time of Jesus.
"""

TEXT_INFO = {
    "text_id": "psalms_of_solomon",
    "display_name": "Psalms of Solomon",
    "full_title": "The Psalms of Solomon",

    "canonical_status": {
        "status": "non-canonical",
        "label": "Pseudepigraphic (not in any major canon)",
        "detail": "The Psalms of Solomon are not included in the Jewish, Protestant, "
                  "Catholic, or Eastern Orthodox canons. They appear in some early "
                  "Christian manuscript lists and were included in the 5th century "
                  "Codex Alexandrinus table of contents (though the text itself is "
                  "missing from the manuscript). They are classified as Old Testament "
                  "pseudepigrapha."
    },

    "authorship": {
        "traditional": "The collection is attributed to King Solomon, but this is "
                       "pseudepigraphic attribution — a common Second Temple practice.",
        "scholarly_debate": "The psalms were composed by one or more Pharisaic authors "
                           "in Jerusalem. The anti-Hasmonean polemic and the response to "
                           "Pompey's conquest of Jerusalem (63 BC) are clear historical "
                           "markers. The theological perspective — emphasis on God's "
                           "righteousness, free will, and resurrection — aligns with "
                           "Pharisaic theology as described by Josephus.",
        "bottom_line": "Anonymous Pharisaic authors writing in Jerusalem during and after "
                       "Pompey's conquest (63 BC), using Solomon's name to give their "
                       "prayers prophetic authority."
    },

    "date": {
        "traditional": "Attributed to Solomon's era (10th century BC).",
        "critical_range": "~80-30 BC. Psalms of Solomon 2 and 17 respond directly to "
                         "Pompey's conquest of Jerusalem (63 BC) and his death in Egypt "
                         "(48 BC). The collection was likely compiled over several decades.",
        "evidence": "The historical references are precise: a foreign conqueror from the "
                    "west (Pompey) who profaned the Temple, followed by his death in Egypt. "
                    "These events date Psalm 2 to after 48 BC. The anti-Hasmonean polemic "
                    "throughout places the collection in the 1st century BC."
    },

    "audience": {
        "original_audience": "Pharisaic communities in Jerusalem who opposed the Hasmonean "
                            "dynasty's combination of royal and priestly offices and mourned "
                            "the Roman conquest as divine judgment.",
        "purpose": "The Psalms of Solomon express a community's theological response to "
                   "political crisis. They interpret the Hasmonean corruption and Roman "
                   "conquest as God's judgment on Israel's sins, while looking forward "
                   "to a righteous Davidic Messiah who will purge Jerusalem and establish "
                   "God's kingdom.",
        "theological_intent": "Psalm 17 contains the most detailed pre-Christian description "
                             "of the expected Davidic Messiah. He will be a human king "
                             "empowered by the Holy Spirit who will drive out foreign rulers, "
                             "purify Jerusalem, gather the scattered tribes, and rule with "
                             "righteousness. This is the messianic expectation Jesus both "
                             "fulfilled and subverted."
    },

    "language": {
        "original": "Hebrew (probable). The surviving text is in Greek and Syriac, but "
                    "the Greek shows clear Semitisms suggesting translation from Hebrew.",
        "script": "Greek (surviving manuscripts), likely translated from a Hebrew original.",
        "linguistic_notes": "The Greek text is heavily Semitic in syntax and vocabulary, "
                           "strongly suggesting a Hebrew Vorlage. The poetic structure "
                           "follows Hebrew psalm conventions (parallelism, acrostic hints)."
    },

    "manuscripts": {
        "earliest": "Greek manuscripts from the medieval period.",
        "major_witnesses": [
            {"name": "Greek manuscripts", "date": "10th-16th century AD",
             "note": "About a dozen Greek manuscripts preserve the text. No ancient "
                     "manuscripts survive."},
            {"name": "Syriac manuscripts", "date": "Medieval",
             "note": "Syriac translation provides a secondary witness, useful for "
                     "textual criticism."},
            {"name": "Codex Alexandrinus (table of contents)", "date": "5th century AD",
             "note": "Listed in the table of contents but the actual text is missing "
                     "from the manuscript — confirming early Christian awareness."}
        ],
        "reliability": "The manuscript tradition is relatively late, with no ancient "
                       "copies surviving. However, the internal historical references "
                       "confirm the 1st century BC date, and the Greek/Syriac traditions "
                       "generally agree, suggesting a reliable transmission."
    },

    "historical_context": {
        "setting": "Jerusalem during the tumultuous 1st century BC: the corrupt late "
                   "Hasmonean dynasty, the Roman conquest under Pompey (63 BC), and "
                   "the beginning of Roman domination of Judea.",
        "geography": "Jerusalem-centered. The psalms focus on the Temple, the holy city, "
                     "and the land of Israel. The foreign conqueror comes 'from the end "
                     "of the earth' (Rome) and profanes the Temple.",
        "historical_connections": "These psalms are the closest pre-Christian parallel to "
                                 "the messianic expectations that shaped Jesus' ministry. "
                                 "Psalm 17's Davidic Messiah who rules with righteousness "
                                 "and the Holy Spirit provides essential context for "
                                 "understanding why the crowds expected a conquering king "
                                 "and why Jesus redefined messiahship through suffering."
    },

    "reader_notes": [
        {
            "type": "authority",
            "title": "Not Scripture — But Essential for Understanding Jesus",
            "body": "The Psalms of Solomon are not canonical in any tradition. However, "
                    "they provide the most detailed window into 1st century BC Jewish "
                    "messianic expectations. When Jesus entered Jerusalem and the crowds "
                    "cried 'Hosanna to the Son of David,' they were expecting the kind "
                    "of Messiah described in Psalm of Solomon 17. Understanding what they "
                    "expected illuminates what Jesus actually came to do."
        },
        {
            "type": "context",
            "title": "Pharisaic Theology in Action",
            "body": "These psalms provide a rare firsthand window into Pharisaic theology: "
                    "emphasis on God's righteousness, human free will, bodily resurrection, "
                    "and trust in divine providence even amid political disaster. This is "
                    "the theological world Paul grew up in before his encounter with Christ."
        }
    ]
}
