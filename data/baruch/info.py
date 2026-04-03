"""
info.py — Baruch: Scholarly Text Introduction

Composite deuterocanonical text attributed to Jeremiah's scribe,
combining confession, wisdom poetry, and prophetic encouragement.
"""

TEXT_INFO = {
    "text_id": "baruch",
    "display_name": "Baruch",
    "full_title": "The Book of Baruch",

    "canonical_status": {
        "status": "deuterocanonical",
        "label": "Deuterocanonical (Catholic & Orthodox canon; not in Protestant canon)",
        "detail": "Baruch is included in the Catholic and Eastern Orthodox Old Testament canons "
                  "but excluded from the Protestant canon. It is attributed to Baruch ben Neriah, "
                  "the scribe and companion of Jeremiah (Jer 32:12, 36:4). Chapter 6, the "
                  "'Letter of Jeremiah,' is sometimes counted as a separate work in Orthodox "
                  "traditions. The book was transmitted as part of the Jeremiah collection in "
                  "the Septuagint."
    },

    "authorship": {
        "traditional": "Attributed to Baruch ben Neriah, Jeremiah's faithful scribe, writing "
                       "from Babylon after the destruction of Jerusalem (1:1-2).",
        "scholarly_debate": "Universally regarded as pseudepigraphical — written under Baruch's "
                           "name by later authors. The book is composite, with at least three or "
                           "four distinct sections by different hands: (1) a historical introduction "
                           "(1:1-14), (2) a confession of sins heavily dependent on Daniel 9 and "
                           "Jeremiah (1:15-3:8), (3) a wisdom poem identifying Torah with cosmic "
                           "Wisdom (3:9-4:4), and (4) a prophetic poem of encouragement echoing "
                           "Isaiah 40-66 (4:5-5:9). The seams between these sections are visible "
                           "in shifts of style, theology, and likely original language.",
        "bottom_line": "A composite pseudepigraphical work by multiple anonymous Jewish authors "
                       "writing under the authority of Jeremiah's scribe to encourage faithfulness "
                       "during periods of foreign domination."
    },

    "date": {
        "traditional": "Set during the Babylonian exile, shortly after the destruction of the "
                       "First Temple (586 BC).",
        "critical_range": "Composite dating: the sections range from the 3rd to 1st century BC. "
                         "The confession section (1:15-3:8) may date to c. 164 BC, given its "
                         "close parallels with Daniel 9. The wisdom poem (3:9-4:4) reflects "
                         "Hellenistic-era wisdom traditions. The final encouragement section "
                         "(4:5-5:9) shares language with the Psalms of Solomon (1st century BC).",
        "evidence": "The dependence on Daniel 9 (which itself dates to c. 165 BC) provides "
                    "a terminus post quem for the confession. The identification of Torah with "
                    "Wisdom parallels Sirach 24 (c. 180 BC). The lack of any reference to the "
                    "Maccabean revolt or Hasmonean dynasty suggests the authors were not engaged "
                    "with those events, or wrote before or apart from that context."
    },

    "audience": {
        "original_audience": "Jews living under foreign rule — whether in the diaspora or in "
                            "Judea under Hellenistic domination. The exile setting serves as a "
                            "transparent analogy for ongoing subjugation.",
        "purpose": "To encourage faithfulness during foreign domination by (1) modeling "
                   "penitential prayer as the path to restoration, (2) identifying Torah "
                   "obedience with true Wisdom, and (3) promising that God will gather the "
                   "scattered and restore Jerusalem. The composite structure addresses the "
                   "community's need for confession, instruction, and hope.",
        "theological_intent": "Israel's suffering is the consequence of abandoning Torah, but "
                             "God remains faithful to the covenant. Wisdom is not a Greek "
                             "philosophical abstraction — it is Torah, given uniquely to Israel. "
                             "The path from exile to restoration runs through repentance."
    },

    "language": {
        "original": "Probably Hebrew for the introduction and confession (1:1-3:8), given "
                    "the Semitic syntax and vocabulary paralleling Jeremiah and Daniel. The "
                    "wisdom poem and encouragement sections (3:9-5:9) were likely composed "
                    "in Greek, showing sophisticated Greek poetic forms.",
        "script": "Only the Greek text survives. No Hebrew fragments are known from Qumran "
                  "or elsewhere.",
        "linguistic_notes": "The shift from Semitic translation Greek in the first half to "
                           "more fluent literary Greek in the second half is one of the strongest "
                           "arguments for composite authorship. The confession section mirrors "
                           "the syntax of Jeremiah and Daniel almost verbatim in places."
    },

    "manuscripts": {
        "earliest": "Greek Septuagint manuscripts from the 4th-5th century AD.",
        "major_witnesses": [
            {"name": "Codex Vaticanus", "date": "4th century AD",
             "note": "Contains Baruch within the Jeremiah collection."},
            {"name": "Codex Alexandrinus", "date": "5th century AD",
             "note": "Contains Baruch following Lamentations."},
            {"name": "Codex Marchalianus", "date": "6th century AD",
             "note": "Important prophetic manuscript including Baruch."},
            {"name": "Syriac Peshitta", "date": "various",
             "note": "Syriac translation preserving an independent textual tradition."}
        ],
        "reliability": "No Hebrew or Aramaic fragments survive. The Greek text is relatively "
                       "stable across manuscripts. The main textual question is the relationship "
                       "of chapter 6 (Letter of Jeremiah) to the rest of the book — some "
                       "manuscript traditions separate them."
    },

    "historical_context": {
        "setting": "Ostensibly set in Babylon during the exile (1:1-2), but the composite "
                   "text reflects Second Temple conditions across several centuries. The "
                   "confession mirrors the penitential theology of the post-exilic community. "
                   "The wisdom poem engages with Hellenistic philosophical claims about the "
                   "nature of wisdom, insisting that true wisdom is Torah — not Greek philosophy.",
        "geography": "The narrative frame is set in Babylon, with Jerusalem as the focus of "
                     "longing and promised restoration. The wisdom poem surveys the nations "
                     "(Canaan, Teman, Merran) who sought wisdom but failed to find it.",
        "historical_connections": "Baruch's identification of Torah with divine Wisdom (3:37-4:1) "
                                 "is a revolutionary theological move that parallels Sirach 24 and "
                                 "anticipates the Johannine identification of Logos with Torah and "
                                 "Christ (John 1:1-14). The confession prayer tradition (drawn from "
                                 "Daniel 9, Nehemiah 9, Ezra 9) represents a major stream of Second "
                                 "Temple piety that shaped synagogue liturgy."
    },

    "reader_notes": [
        {
            "type": "context",
            "title": "Torah as Wisdom",
            "body": "Baruch 3:37-4:1 makes the revolutionary identification of cosmic Wisdom "
                    "with Torah. While the nations grope after wisdom through philosophy and "
                    "speculation, God has given Wisdom to Israel in the form of the commandments. "
                    "This parallels Sirach 24 and stands behind the later Rabbinic concept of "
                    "Torah as God's pre-existent blueprint for creation. Early Christians would "
                    "reinterpret this Wisdom-Torah identification christologically (John 1, "
                    "Colossians 1:15-20)."
        },
        {
            "type": "authority",
            "title": "Composite Text",
            "body": "Scholars identify at least three to four distinct sections by different "
                    "authors stitched together under Baruch's name: a historical frame (1:1-14), "
                    "a penitential confession (1:15-3:8), a wisdom poem (3:9-4:4), and a "
                    "prophetic encouragement (4:5-5:9). Each section has its own style, "
                    "theological emphasis, and probably original language. Reading Baruch means "
                    "reading an anthology, not a unified composition."
        }
    ]
}
