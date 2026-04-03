"""
info.py — 4 Ezra (2 Esdras): Scholarly Text Introduction

Jewish apocalypse written after the Temple's destruction (70 AD),
containing the most profound theodicy wrestling in Second Temple literature.
"""

TEXT_INFO = {
    "text_id": "4ezra",
    "display_name": "4 Ezra (2 Esdras)",
    "full_title": "Fourth Book of Ezra (Second Esdras)",

    "canonical_status": {
        "status": "pseudepigrapha",
        "label": "Pseudepigrapha in Protestant & Catholic traditions; canonical in Ethiopian Orthodox, Slavonic, and Armenian churches (KJV Apocrypha as 2 Esdras)",
        "detail": "4 Ezra occupies a complex canonical position. It is classified as pseudepigrapha "
                  "in Protestant and Catholic traditions, but holds canonical status in the Ethiopian "
                  "Orthodox Tewahedo Church (as 1 Esdras/Ezra Sutuel) and is preserved in the "
                  "Slavonic and Armenian biblical traditions. The Jewish core (chapters 3-14) "
                  "is widely studied as a major Second Temple apocalypse. Christian additions "
                  "bracket the Jewish text: 5 Ezra (chapters 1-2, c. 2nd century AD) and 6 Ezra "
                  "(chapters 15-16, c. 3rd century AD). The composite work entered the KJV "
                  "Apocrypha as 2 Esdras. It is canonical in the Ethiopian Orthodox, Slavonic, "
                  "and Armenian churches. The Clementine Vulgate included it as an appendix, "
                  "acknowledging its importance while distinguishing it from the canon proper."
    },

    "authorship": {
        "traditional": "The text presents itself as the visions and dialogues of Ezra the scribe, "
                       "set in Babylon thirty years after Jerusalem's destruction — ostensibly "
                       "586 BC but transparently referring to 70 AD.",
        "scholarly_debate": "The Jewish core (ch. 3-14) was written by an anonymous Jewish author "
                           "using Ezra as a pseudonymous voice to process the catastrophe of 70 AD. "
                           "The author was a sophisticated theologian deeply troubled by the problem "
                           "of theodicy. The Christian additions are by different, later hands: "
                           "5 Ezra (ch. 1-2) reinterprets the Jewish material in a supersessionist "
                           "direction, while 6 Ezra (ch. 15-16) is a Christian apocalyptic oracle "
                           "responding to later crises.",
        "bottom_line": "An anonymous Jewish author writing as Ezra, c. 100 AD, producing one of "
                       "the most theologically sophisticated apocalypses in Jewish literature. "
                       "The Christian additions (5 Ezra and 6 Ezra) are later editorial frames."
    },

    "date": {
        "traditional": "Set thirty years after Jerusalem's first destruction (3:1), ostensibly "
                       "c. 556 BC. Note: this is the fictional narrative frame — Ezra is set 30 "
                       "years after the fall of Jerusalem in 586 BC. The actual composition date "
                       "is c. 100 AD, written in response to the destruction of the Second Temple "
                       "in 70 AD (see critical_range below).",
        "critical_range": "Jewish core (ch. 3-14): c. 100 AD, approximately thirty years after "
                         "Rome destroyed the Second Temple in 70 AD — the 'thirty years' of 3:1 "
                         "is the author's actual timeframe. 5 Ezra (ch. 1-2): c. mid-2nd century AD. "
                         "6 Ezra (ch. 15-16): c. mid-3rd century AD.",
        "evidence": "The eagle vision (ch. 11-12) is a coded apocalyptic portrayal of Rome, "
                    "identifiable through its emperors. The emotional intensity of Ezra's "
                    "dialogues reflects genuine post-70 AD trauma. The parallel composition "
                    "with 2 Baruch (which addresses the same catastrophe) confirms the dating. "
                    "Both texts wrestle with how God's covenant people can suffer such devastation."
    },

    "audience": {
        "original_audience": "Jews grappling with the destruction of the Second Temple by Rome "
                            "in 70 AD. The crisis was not merely political — it struck at the "
                            "heart of covenant theology. If God chose Israel, why does he allow "
                            "pagan Rome to triumph?",
        "purpose": "To wrestle honestly with the problem of theodicy — why God permits the "
                   "suffering of his covenant people — and to arrive at a position of trust "
                   "despite unanswered questions. The seven visions move from anguished protest "
                   "to apocalyptic revelation to a commission to preserve sacred writings.",
        "theological_intent": "Human reason cannot fully comprehend God's justice; the age to "
                             "come will reveal what this age conceals. The righteous must endure "
                             "faithfully through the present evil age, trusting that God's purposes "
                             "will be vindicated in the messianic age and final judgment."
    },

    "language": {
        "original": "Hebrew or Aramaic (lost). The original Semitic text was translated into "
                    "Greek (mostly lost — only scattered fragments survive). The primary "
                    "surviving text is in Latin, translated from the Greek.",
        "script": "The Latin Vulgate manuscripts preserve the fullest text. Important versions "
                  "also survive in Syriac, Ethiopic, Georgian, Armenian, and two Arabic "
                  "recensions, all translated from the Greek at various stages.",
        "linguistic_notes": "The complex transmission chain (Semitic original → Greek → Latin "
                           "and other versions) makes textual criticism unusually challenging. "
                           "Scholars must compare across multiple language traditions to reconstruct "
                           "the likely original. The Syriac Peshitta preserves chapters 3-14 and "
                           "is particularly valuable as an independent witness from the Greek."
    },

    "manuscripts": {
        "earliest": "Latin manuscripts from the 9th century AD. Greek fragments. Syriac Peshitta.",
        "major_witnesses": [
            {"name": "Codex Sangermanensis", "date": "9th century AD",
             "note": "Latin manuscript, one of the earliest witnesses to the full text."},
            {"name": "Codex Ambianensis", "date": "9th century AD",
             "note": "Important Latin witness with variant readings."},
            {"name": "Syriac Peshitta", "date": "various",
             "note": "Preserves chapters 3-14 (the Jewish core), translated independently from Greek."},
            {"name": "Ethiopic version", "date": "various",
             "note": "Complete text in the Ethiopian Orthodox canon, preserving readings lost in Latin."},
            {"name": "Greek Oxyrhynchus fragment", "date": "4th century AD",
             "note": "Rare surviving fragment of the Greek text."}
        ],
        "reliability": "The original Semitic text is entirely lost. The Greek is mostly lost except "
                       "for fragments. The Latin is the primary witness but stands two translations "
                       "removed from the original. Cross-referencing Latin, Syriac, Ethiopic, and "
                       "other versions is essential for establishing the text. Despite this complexity, "
                       "the main lines of the text are reasonably secure."
    },

    "historical_context": {
        "setting": "Ostensibly Babylon after the first Temple's destruction, but transparently "
                   "addressing the aftermath of Rome's destruction of the Second Temple in 70 AD. "
                   "The 'thirty years' of 3:1 places the composition around 100 AD. The author "
                   "writes during a period of profound theological crisis for Judaism — the Temple, "
                   "the sacrificial system, and the visible signs of God's covenant presence are gone.",
        "geography": "Set in Babylon (coded for Rome). The visions occur in a field outside the "
                     "city, echoing Ezekiel's visionary setting. The eagle vision (ch. 11-12) "
                     "surveys the Roman Empire.",
        "historical_connections": "4 Ezra is a twin composition with 2 Baruch — both written in "
                                 "response to the 70 AD catastrophe, both using the first destruction "
                                 "as a cipher for the second, both wrestling with theodicy. The "
                                 "angel Uriel's dialogues with Ezra parallel Job's confrontation "
                                 "with God but in an apocalyptic register. The 'Son of Man' vision "
                                 "in chapter 13 (a pre-existent figure rising from the sea to destroy "
                                 "enemies) connects to Daniel 7 and 1 Enoch's Similitudes (1 Enoch 46), "
                                 "providing crucial evidence for pre-Christian messianic expectations."
    },

    "reader_notes": [
        {
            "type": "deeper_reading",
            "title": "Theodicy and Suffering",
            "body": "4 Ezra contains the most profound wrestling with divine justice in Second "
                    "Temple literature. Ezra's anguished questions — why did God create humans "
                    "with an evil inclination and then punish them? why does pagan Rome prosper "
                    "while covenant Israel suffers? — receive no easy answers. The angel Uriel "
                    "responds with counter-questions and apocalyptic visions rather than "
                    "philosophical explanations. The book's honesty about the limits of human "
                    "understanding makes it a powerful companion to Job and Ecclesiastes."
        },
        {
            "type": "context",
            "title": "Son of Man Vision",
            "body": "Chapter 13 presents a vision of a pre-existent figure ('something like the "
                    "figure of a man') rising from the sea, flying with the clouds, and destroying "
                    "enemies with the breath of his mouth. This is an independent development of "
                    "the 'Son of Man' tradition from Daniel 7:13-14, parallel to 1 Enoch's "
                    "Similitudes (ch. 37-71). Together with Daniel and 1 Enoch, 4 Ezra demonstrates "
                    "that the 'Son of Man' was an active messianic category in Jewish thought "
                    "before and contemporaneous with the New Testament authors."
        },
        {
            "type": "authority",
            "title": "Lost Original",
            "body": "The original Hebrew or Aramaic text of 4 Ezra is entirely lost. The Greek "
                    "translation is mostly lost except for fragments. We read primarily through "
                    "Latin, standing two translations removed from the original. This makes "
                    "textual criticism complex — every passage requires checking across Latin, "
                    "Syriac, Ethiopic, and other versions. Despite this, the theological power "
                    "of the text transcends its transmission difficulties."
        }
    ]
}
