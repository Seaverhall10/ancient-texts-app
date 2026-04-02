"""
info.py — Sirach (Ben Sira): Scholarly Text Introduction

The most extensive wisdom text from the Second Temple period,
with significant manuscript evidence including the Cairo Genizah
Hebrew fragments and Dead Sea Scrolls.
"""

TEXT_INFO = {
    "text_id": "sirach",
    "display_name": "Sirach (Ben Sira)",
    "full_title": "The Wisdom of Jesus Son of Sirach (Ecclesiasticus)",

    "canonical_status": {
        "status": "deuterocanonical",
        "label": "Deuterocanonical (Catholic & Orthodox canon; not in Protestant canon)",
        "detail": "Sirach is included in the Catholic and Eastern Orthodox canons. It was "
                  "widely used in the early church (hence its Latin title 'Ecclesiasticus' — "
                  "'the church book'). The rabbis excluded it from the Hebrew canon despite "
                  "its popularity, partly because the author was known and too recent to be "
                  "considered prophetic. Fragments were found at Qumran (2Q18) and Masada, "
                  "and extensive Hebrew manuscripts were recovered from the Cairo Genizah."
    },

    "authorship": {
        "traditional": "The text identifies its author as 'Jesus son of Eleazar son of Sira' "
                       "(Sirach 50:27), a Jerusalem sage and scribe. His grandson translated "
                       "the work from Hebrew into Greek in Egypt after 132 BC, providing a "
                       "rare dated colophon in the prologue.",
        "scholarly_debate": "This is one of the few Second Temple texts with a known, named "
                           "author. Ben Sira was a professional scribe and teacher who ran "
                           "a school (bet midrash) in Jerusalem. The grandson's prologue "
                           "provides reliable information about the translation and date.",
        "bottom_line": "Yeshua ben Eleazar ben Sira, a Jerusalem wisdom teacher writing "
                       "around 180 BC — one of the rare cases where we know the actual "
                       "author of a Second Temple Jewish text."
    },

    "date": {
        "traditional": "The grandson's prologue states he came to Egypt 'in the thirty-eighth "
                       "year of King Euergetes' (= Ptolemy VIII, so 132 BC) and translated "
                       "his grandfather's work. This places the original composition around "
                       "180-175 BC.",
        "critical_range": "~180-175 BC. The praise of the high priest Simon II (Sirach 50:1-21) "
                         "suggests the author witnessed Simon's ministry but wrote after his "
                         "death (~196 BC). The text shows no awareness of the Maccabean crisis "
                         "(167 BC), confirming composition before that watershed event.",
        "evidence": "The grandson's dated prologue is the strongest evidence. The historical "
                    "references (praise of Simon II, no mention of Antiochus IV) confirm "
                    "the pre-Maccabean date."
    },

    "audience": {
        "original_audience": "Young Jewish men training for scribal and administrative careers "
                            "in early 2nd century BC Jerusalem, during a period of increasing "
                            "Hellenistic cultural pressure.",
        "purpose": "Ben Sira sought to demonstrate that Jewish wisdom was superior to Greek "
                   "philosophy and that Torah observance was the true path to wisdom. The "
                   "famous 'Praise of the Fathers' (chapters 44-50) presents Israel's heroes "
                   "as exemplars of wisdom embodied in action.",
        "theological_intent": "Sirach identifies Torah with cosmic Wisdom (chapter 24) — "
                             "Wisdom came down from heaven and 'pitched her tent' in Israel. "
                             "This Torah-Wisdom identification became foundational for later "
                             "Jewish theology and provides crucial background for John 1 "
                             "(the Word 'tabernacled' among us)."
    },

    "language": {
        "original": "Hebrew. Ben Sira wrote in Hebrew; his grandson translated into Greek. "
                    "About two-thirds of the Hebrew text has been recovered.",
        "script": "Hebrew (original), translated into Greek by the author's grandson "
                  "after 132 BC.",
        "linguistic_notes": "The Hebrew is late biblical Hebrew with features transitioning "
                           "toward Mishnaic Hebrew. The Cairo Genizah manuscripts (discovered "
                           "1896) preserve about 68% of the Hebrew text. Additional fragments "
                           "were found at Qumran and Masada."
    },

    "manuscripts": {
        "earliest": "Fragments from Qumran (2Q18) and Masada, dating to the 1st century BC.",
        "major_witnesses": [
            {"name": "Cairo Genizah manuscripts (MSS A-F)", "date": "11th-12th century AD",
             "note": "Six medieval Hebrew manuscripts preserving about two-thirds of the text. "
                     "Despite their late date, they preserve a text close to the original."},
            {"name": "2Q18 (Qumran)", "date": "1st century BC",
             "note": "Small Hebrew fragments from Qumran Cave 2."},
            {"name": "Masada scroll", "date": "1st century BC",
             "note": "Hebrew fragments of Sirach 39:27-44:17 found at Masada."},
            {"name": "Greek (LXX tradition)", "date": "4th-5th century AD",
             "note": "The grandson's translation preserved in major uncial manuscripts."}
        ],
        "reliability": "The combination of Qumran, Masada, Genizah, and Greek witnesses "
                       "provides excellent textual evidence. Where Hebrew and Greek can be "
                       "compared, the grandson's translation is generally faithful but "
                       "sometimes interpretive."
    },

    "historical_context": {
        "setting": "Jerusalem in the early 2nd century BC, during the transition from "
                   "Ptolemaic to Seleucid control of Palestine. Ben Sira wrote during "
                   "a period of relative peace before the Maccabean crisis, but Hellenistic "
                   "cultural pressure was already a major concern.",
        "geography": "Jerusalem, where Ben Sira ran his school. The grandson translated "
                     "the text in Alexandria, Egypt, after emigrating there.",
        "historical_connections": "Sirach is the last major wisdom text before the Maccabean "
                                 "revolt. It captures Jewish intellectual life at a critical "
                                 "moment — the calm before the storm of Antiochus IV's "
                                 "persecution. The 'Praise of the Fathers' (chs. 44-50) "
                                 "provided a model for later lists of faithful heroes "
                                 "(cf. Hebrews 11)."
    },

    "reader_notes": [
        {
            "type": "authority",
            "title": "Deuterocanonical but Historically Invaluable",
            "body": "Sirach is the most extensive window into mainstream Jewish thought "
                    "in the early 2nd century BC. Its identification of Torah with Wisdom "
                    "(chapter 24) is essential background for understanding John 1 and "
                    "Colossians 1. The rabbis cited Ben Sira frequently despite excluding "
                    "his book from the canon."
        },
        {
            "type": "context",
            "title": "A Known Author in an Anonymous World",
            "body": "Ben Sira is one of the very few Second Temple authors we can name "
                    "with confidence. His grandson's prologue gives us a rare dated "
                    "reference point (132 BC) and a firsthand account of the translation "
                    "process. This makes Sirach uniquely valuable for reconstructing "
                    "the intellectual world of pre-Maccabean Judaism."
        }
    ]
}
