"""
info.py — Judith: Scholarly Text Introduction

A dramatic narrative of Jewish resistance and faith,
set against the backdrop of imperial aggression.
"""

TEXT_INFO = {
    "text_id": "judith",
    "display_name": "Judith",
    "full_title": "The Book of Judith",

    "canonical_status": {
        "status": "deuterocanonical",
        "label": "Deuterocanonical (Catholic & Orthodox canon; not in Protestant canon)",
        "detail": "Judith is included in the Catholic and Eastern Orthodox Old Testament "
                  "canons but excluded from the Protestant canon. Jerome translated it "
                  "for the Vulgate but noted it was not in the Hebrew canon. No Hebrew "
                  "or Aramaic manuscripts have survived from antiquity, though Jerome "
                  "claimed to have worked from an Aramaic text."
    },

    "authorship": {
        "traditional": "The author is unknown. The text does not claim authorship by any "
                       "biblical figure.",
        "scholarly_debate": "The book is widely regarded as a historical novella rather "
                           "than a historical account. The deliberate historical "
                           "anachronisms (Nebuchadnezzar called 'king of the Assyrians') "
                           "suggest the author was not confused but was using history "
                           "typologically — combining multiple periods of threat into one "
                           "archetypal story of divine deliverance.",
        "bottom_line": "An anonymous Jewish author, likely writing in Palestine during "
                       "the 2nd century BC, crafted a theological narrative about faith "
                       "and courage in the face of imperial power."
    },

    "date": {
        "traditional": "Set during the reign of Nebuchadnezzar (though anachronistically "
                       "placed in Nineveh as 'king of the Assyrians').",
        "critical_range": "Composed ~150-100 BC during the Hasmonean period. The themes "
                         "of Jewish resistance to foreign oppression fit the post-Maccabean "
                         "context well.",
        "evidence": "Linguistic analysis of the Greek text, the post-exilic theological "
                    "vocabulary, and the Hasmonean-era concerns about purity and resistance "
                    "all point to a 2nd century BC composition."
    },

    "audience": {
        "original_audience": "Palestinian Jews during the Hasmonean period, facing ongoing "
                            "questions about resistance to foreign powers and faithfulness "
                            "to Torah.",
        "purpose": "Judith demonstrates that God delivers Israel through unexpected means — "
                   "in this case, through a woman's faith, wisdom, and courage. The story "
                   "emphasizes prayer, fasting, and obedience to Torah as the true weapons "
                   "against oppression.",
        "theological_intent": "God uses the weak to shame the strong. Judith's victory "
                             "over Holofernes echoes Jael's defeat of Sisera (Judges 4-5) "
                             "and David's defeat of Goliath — a recurring biblical pattern."
    },

    "language": {
        "original": "Likely composed in Hebrew, though the original is lost. Jerome "
                    "mentioned working from an Aramaic text. The surviving text is in Greek.",
        "script": "Greek (LXX tradition). No Semitic manuscripts survive.",
        "linguistic_notes": "The Greek text shows clear Semitisms (Hebrew idioms translated "
                           "into Greek), strongly suggesting a Semitic original. The style "
                           "is literary and polished."
    },

    "manuscripts": {
        "earliest": "Greek manuscripts in the Septuagint tradition.",
        "major_witnesses": [
            {"name": "Codex Vaticanus", "date": "4th century AD",
             "note": "Primary Greek witness for Judith."},
            {"name": "Codex Sinaiticus", "date": "4th century AD",
             "note": "Another early Greek witness."},
            {"name": "Codex Alexandrinus", "date": "5th century AD",
             "note": "Greek uncial manuscript."},
            {"name": "Vulgate (Jerome)", "date": "4th century AD",
             "note": "Jerome's Latin translation, reportedly from an Aramaic source."}
        ],
        "reliability": "The Greek text is well-preserved in the major LXX manuscripts. "
                       "Without a Semitic Vorlage for comparison, textual criticism relies "
                       "on the Greek manuscript tradition and versional evidence."
    },

    "historical_context": {
        "setting": "The narrative is set during a fictional Assyrian campaign led by "
                   "Holofernes against Judea. The deliberate anachronisms place this "
                   "in an idealized rather than historical setting.",
        "geography": "Centered on the fictional town of Bethulia (possibly modeled on "
                     "a real town in the Samarian hills) under siege by the Assyrian army. "
                     "The geography of the campaign follows plausible routes through "
                     "the ancient Near East.",
        "historical_connections": "Judith likely reflects the Hasmonean experience of "
                                 "resisting Seleucid oppression. The emphasis on Torah "
                                 "observance, dietary laws, and prayer mirrors Hasmonean-era "
                                 "concerns. The heroine archetype connects to Deborah, Jael, "
                                 "and Esther."
    },

    "reader_notes": [
        {
            "type": "authority",
            "title": "Deuterocanonical Status",
            "body": "Judith is not canonical Scripture — it should never be cited as "
                    "'the Bible says.' It is included in Catholic and Orthodox canons but "
                    "not in the Protestant or Jewish canons. The deliberate historical "
                    "anachronisms mark it as theological narrative rather than historical "
                    "chronicle. Read it as powerful theological storytelling that "
                    "illuminates the faith and courage valued in Second Temple Judaism."
        },
        {
            "type": "context",
            "title": "The Judith Archetype",
            "body": "Judith stands in a biblical tradition of women who deliver Israel: "
                    "Deborah and Jael (Judges 4-5), Esther, the wise woman of Abel "
                    "(2 Samuel 20). Her story teaches that God's power works through "
                    "faithfulness, not military might."
        }
    ]
}
