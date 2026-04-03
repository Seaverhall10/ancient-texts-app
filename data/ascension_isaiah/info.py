"""
info.py — Ascension of Isaiah: Scholarly Text Introduction

A composite Jewish-Christian apocalypse preserving Isaiah's martyrdom tradition
and one of the earliest Christian accounts of Christ's secret descent through
the heavens — a unique window into first-century cosmology and Christology.
"""

TEXT_INFO = {
    "text_id": "ascension_isaiah",
    "display_name": "Ascension of Isaiah",
    "full_title": "The Ascension of Isaiah",

    "canonical_status": {
        "status": "pseudepigrapha",
        "label": "Pseudepigrapha (canonical in Ethiopian Orthodox Church)",
        "detail": "The Ascension of Isaiah is a composite work with two distinct sections. "
                  "The Martyrdom of Isaiah (chapters 1-5) is a Jewish text, possibly from the "
                  "2nd century BC, preserving the tradition that Isaiah was sawn in half under "
                  "King Manasseh — the event referenced in Hebrews 11:37. The Vision of Isaiah "
                  "(chapters 6-11) is a Christian composition describing Isaiah's heavenly ascent "
                  "through seven heavens and a vision of Christ's incarnation. The complete work "
                  "is canonical in the Ethiopian Orthodox Church. This edition contains the Vision "
                  "section. Early church fathers including Justin Martyr, Tertullian, and Origen "
                  "knew and referenced the text."
    },

    "authorship": {
        "traditional": "The text presents itself as a prophetic vision received by Isaiah son of "
                       "Amoz during the reign of King Hezekiah, with the martyrdom occurring under "
                       "Manasseh.",
        "scholarly_debate": "The Martyrdom section (ch. 1-5) is Jewish, possibly dating to the "
                           "2nd century BC, and may have circulated independently before being "
                           "combined with the Vision. The Vision section (ch. 6-11) is Christian, "
                           "written by an anonymous author in the late 1st or early 2nd century AD. "
                           "Some scholars argue for a date as early as the 60s AD based on the "
                           "Beloved's descent narrative and the absence of developed Gnostic "
                           "features. A third component, the 'Testament of Hezekiah' (3:13-4:22), "
                           "may be a separate Christian apocalypse inserted into the Martyrdom.",
        "bottom_line": "Anonymous composition in stages. The Jewish Martyrdom tradition is pre-Christian. "
                       "The Christian Vision represents very early Christological reflection, possibly "
                       "from the late first century AD, making it one of the oldest surviving accounts "
                       "of Christ's heavenly origin and incarnation outside the New Testament."
    },

    "date": {
        "traditional": "Set during the reigns of Hezekiah and Manasseh, 8th-7th century BC.",
        "critical_range": "Martyrdom of Isaiah (ch. 1-5): 2nd century BC, possibly earlier. "
                         "Vision of Isaiah (ch. 6-11): late 1st century AD, with some scholars "
                         "arguing for the 60s AD based on internal evidence. Testament of Hezekiah "
                         "(3:13-4:22): late 1st or early 2nd century AD. Final compilation: "
                         "2nd century AD.",
        "evidence": "The Martyrdom's tradition is ancient — the Jewish legend of Isaiah's death by "
                    "sawing was known to the author of Hebrews (11:37) and is referenced in "
                    "rabbinic literature (Yevamot 49b). The Vision's Christology — Christ as a "
                    "pre-existent figure descending secretly through angelic realms — reflects a "
                    "stage of theological development consistent with the late first century. The "
                    "Trinitarian formula in 8:18 (Father, Beloved, Holy Spirit worshipped together) "
                    "is remarkably early and lacks the later precision of Nicene theology."
    },

    "audience": {
        "original_audience": "Early Christian communities interested in heavenly ascent traditions, "
                            "angelic hierarchies, and the cosmic dimensions of Christ's work. The "
                            "Martyrdom section originally addressed a Jewish audience familiar with "
                            "prophetic persecution traditions.",
        "purpose": "The Vision provides a cosmic narrative of salvation: Isaiah ascends through "
                   "seven heavens, witnesses the worship in each level, and sees the Beloved "
                   "descend in disguise through hostile angelic territories to accomplish the "
                   "incarnation, crucifixion, resurrection, and ascension. The purpose is to "
                   "reveal the heavenly reality behind the earthly events of the gospel.",
        "theological_intent": "Christ's incarnation is a divine invasion conducted in secrecy — "
                             "the Beloved takes on the form of each heaven's inhabitants as he "
                             "descends, so that even the angels do not recognize him. This motif "
                             "emphasizes the hiddenness of God's plan and echoes Paul's statement "
                             "that the rulers of this age did not understand God's wisdom, for if "
                             "they had, they would not have crucified the Lord of glory (1 Cor 2:8)."
    },

    "language": {
        "original": "The original language was likely Greek for the Christian sections. The Jewish "
                    "Martyrdom may have had a Hebrew or Aramaic original. The full text is best "
                    "preserved in Ge'ez (Ethiopic).",
        "script": "The most complete text survives in Ethiopic manuscripts. Partial witnesses "
                  "exist in Latin (a palimpsest with about two-thirds of the text), Slavonic "
                  "(Old Church Slavonic version), and Coptic fragments. No complete Greek "
                  "manuscript survives, though Greek was almost certainly the language of "
                  "composition for the Vision.",
        "linguistic_notes": "The Ethiopic text is the scholarly standard for the full work, but "
                           "must be checked against the Latin and Slavonic where they overlap. "
                           "The Latin palimpsest is particularly valuable because it represents "
                           "an independent early translation from the Greek. The loss of the Greek "
                           "original means that some textual decisions depend on retroversion — "
                           "guessing the Greek behind the Ethiopic, a process that involves "
                           "unavoidable uncertainty."
    },

    "manuscripts": {
        "earliest": "Ethiopic manuscripts (most complete). Latin palimpsest fragments. "
                    "Slavonic version. Coptic fragments.",
        "major_witnesses": [
            {"name": "Ethiopic manuscripts", "date": "15th-18th century AD",
             "note": "The only complete witnesses to the full text. Multiple manuscripts "
                     "allow comparison and correction of scribal errors."},
            {"name": "Latin palimpsest (Codex Lat. 1)", "date": "5th-6th century AD",
             "note": "Contains roughly two-thirds of the text. One of the earliest witnesses, "
                     "translated independently from the Greek."},
            {"name": "Slavonic version", "date": "medieval",
             "note": "Old Church Slavonic translation, providing an independent witness for "
                     "portions of the text."},
            {"name": "Coptic fragments", "date": "5th-6th century AD",
             "note": "Small fragments from Upper Egypt, confirming the text's circulation "
                     "in Egyptian Christianity."},
            {"name": "Greek papyrus fragment (P.Amherst 1)", "date": "5th-6th century AD",
             "note": "A small Greek fragment, one of the few surviving pieces of the original "
                     "language tradition."}
        ],
        "reliability": "The Ethiopic text is generally reliable but stands as a translation of a "
                       "translation (Greek to Ethiopic, possibly via Arabic for some manuscripts). "
                       "The Latin palimpsest, though incomplete, provides crucial early evidence. "
                       "Where the Ethiopic, Latin, and Slavonic agree, the text is considered "
                       "secure. Where they diverge, editorial judgment is required. The absence "
                       "of a complete Greek manuscript is the single greatest limitation."
    },

    "historical_context": {
        "setting": "The Martyrdom is set during the reign of Manasseh, when Isaiah and a group "
                   "of prophets flee to the wilderness to escape persecution. The false prophet "
                   "Belkira (associated with Beliar/Satan) accuses Isaiah, leading to his execution "
                   "by sawing. The Vision is set during Hezekiah's reign — Isaiah falls into a "
                   "trance and ascends through seven heavens guided by an angel.",
        "geography": "The earthly setting is Jerusalem and the Judean wilderness. The heavenly "
                     "setting — seven layered heavens with increasing glory — reflects the "
                     "cosmological framework common in Second Temple Judaism and early Christianity. "
                     "Each heaven has its own angelic inhabitants, throne, and worship.",
        "historical_connections": "The seven-heaven cosmology influenced later Jewish merkabah "
                                 "mysticism and Gnostic systems. The Beloved's secret descent — "
                                 "disguising himself to pass through each heaven unrecognized — is "
                                 "a unique Christological motif that echoes Philippians 2:6-8 (Christ "
                                 "emptying himself and taking the form of a servant) but develops it "
                                 "into a full cosmic narrative. The tradition that Isaiah was sawn in "
                                 "half is referenced in Hebrews 11:37 and became a standard element "
                                 "of Jewish and Christian martyrology. The Trinitarian worship scene "
                                 "in the seventh heaven (8:18) — Father, Beloved, and Holy Spirit "
                                 "worshipped together — is one of the earliest witnesses to Trinitarian "
                                 "devotional practice outside the New Testament."
    },

    "reader_notes": [
        {
            "type": "deeper_reading",
            "title": "Christ's Secret Descent",
            "body": "The Vision's most striking feature is the Beloved's descent through the seven "
                    "heavens in disguise. At each level he transforms his appearance to match the "
                    "angels of that heaven, so that none recognize him. Only when he reaches the "
                    "earth — taking on human form, being crucified, and rising again — is his true "
                    "identity revealed. This motif is not found in the New Testament but resonates "
                    "deeply with Philippians 2:6-8 (the kenosis hymn) and 1 Corinthians 2:8 (the "
                    "rulers of this age not recognizing God's wisdom). It represents an early "
                    "Christian theological imagination working out the cosmic implications of the "
                    "incarnation — God entering enemy territory undetected to accomplish redemption."
        },
        {
            "type": "context",
            "title": "Seven Heavens Cosmology",
            "body": "The detailed seven-heaven framework in the Ascension — with each level containing "
                    "thrones, angelic hierarchies, and progressively greater glory — became enormously "
                    "influential in later tradition. It connects backward to 1 Enoch's heavenly "
                    "journeys and forward to the merkabah (chariot) mysticism of rabbinic Judaism, "
                    "the Gnostic pleroma systems, and Paul's reference to being caught up to the "
                    "'third heaven' in 2 Corinthians 12:2. The number seven draws on ancient Near "
                    "Eastern cosmological traditions (compare the seven gates of the Mesopotamian "
                    "underworld in Ishtar's Descent) reframed within Jewish monotheism."
        },
        {
            "type": "authority",
            "title": "Isaiah Sawn in Half",
            "body": "The Martyrdom section preserves the ancient Jewish tradition that the prophet "
                    "Isaiah was executed by being sawn in half with a wooden saw during the reign "
                    "of Manasseh. This tradition is almost certainly behind the reference in Hebrews "
                    "11:37 to those who 'were sawn in two' — a detail that makes little sense without "
                    "knowledge of this specific martyrdom account. The tradition also appears in "
                    "the Babylonian Talmud (Yevamot 49b) and in early church fathers. The Ascension "
                    "of Isaiah is the earliest surviving narrative of this event and provides the "
                    "interpretive background for one of the New Testament's most dramatic statements "
                    "about the cost of faithfulness."
        }
    ]
}
