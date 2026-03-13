"""
info.py — The Biblical Canon: Scholarly Text Introduction

How did we get our Bible? An honest examination of how the 66-book Protestant
canon was recognized, the formation process from Torah to New Testament,
and the differences between Christian traditions (Protestant, Catholic,
Orthodox, Ethiopian).
"""

TEXT_INFO = {
    "text_id": "canon_scripture",
    "display_name": "The Biblical Canon",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "thematic_study",
        "label": "Thematic Study — Canon Formation",
        "detail": "This is not a primary text but a study resource examining how the "
                  "biblical canon was formed. It covers the Old Testament canon (Torah "
                  "through Writings), the New Testament canon (apostolic writings through "
                  "the 4th-century lists), the Dead Sea Scrolls' impact on textual "
                  "criticism, and the differences between Protestant (66 books), Catholic "
                  "(73 books), Orthodox (76+ books), and Ethiopian (81 books) canons. "
                  "All Scripture quotations use the ESV unless otherwise noted."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "This study text was compiled from scholarly sources examining the "
                       "historical process of canon formation. It does not represent a "
                       "single author's viewpoint but synthesizes the evidence from "
                       "multiple traditions and scholarly perspectives.",

        "scholarly_debate": "Canon formation is one of the most studied topics in biblical "
                           "scholarship. Key scholars include F.F. Bruce (The Canon of Scripture, "
                           "1988), Bruce Metzger (The Canon of the New Testament, 1987), Lee "
                           "Martin McDonald (The Biblical Canon, 2007), and Michael Kruger "
                           "(Canon Revisited, 2012). The fundamental debate is between the "
                           "'intrinsic model' (the books were authoritative from the moment of "
                           "composition because of their divine origin) and the 'community model' "
                           "(the books became authoritative through community recognition over "
                           "time). This study presents the evidence and argues that the process "
                           "was one of recognition, not creation — the church did not make these "
                           "books authoritative; it recognized the authority they already possessed.",

        "bottom_line": "The biblical canon was not decided by a single council or emperor. It "
                       "emerged through centuries of usage, theological testing, and community "
                       "recognition. The 27 New Testament books were already functioning as "
                       "Scripture in the earliest churches long before any council formalized "
                       "the list."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "The canon formation process spans roughly 1,400 years: from Moses "
                       "and the Torah (c. 1400-1200 BC) to the final recognition of the "
                       "New Testament canon (4th century AD).",
        "critical_range": "Torah composition: 13th-5th century BC (traditional to critical "
                         "range). Prophets and Writings: 8th-2nd century BC. New Testament: "
                         "c. AD 49-95. Canon lists: Muratorian Fragment (c. AD 170), "
                         "Athanasius's 39th Festal Letter (AD 367), Councils of Hippo (393) "
                         "and Carthage (397).",
        "evidence": "The earliest evidence for a fixed Torah collection is the Samaritan "
                    "Pentateuch (diverging c. 4th century BC). The Dead Sea Scrolls "
                    "(c. 250 BC - AD 68) attest to a fluid textual situation for many "
                    "books. The Septuagint (3rd-1st century BC) included additional books "
                    "not in the later Hebrew canon. Jesus and the apostles quoted from "
                    "both the Hebrew and Greek traditions."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Students and researchers seeking to understand how and why the "
                            "Bible contains the books it does. This study is designed for "
                            "believers who want honest answers to hard questions about canon "
                            "formation without losing confidence in Scripture's divine authority.",

        "purpose": "To equip believers with historically grounded knowledge about how the "
                   "biblical canon was formed, so they can answer common objections ('The "
                   "Bible was decided by Constantine,' 'The church arbitrarily chose which "
                   "books to include,' 'The Gnostic gospels were suppressed') with facts "
                   "rather than assumptions.",

        "theological_intent": "The canon was recognized, not invented. God preserved His word "
                             "through a messy, human process — and that process is itself "
                             "evidence of providential guidance. The books that made it into "
                             "the canon did so because they bore the marks of apostolic "
                             "authority, theological consistency, and widespread church usage "
                             "from the earliest period."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "The Old Testament was written primarily in Hebrew, with Aramaic "
                    "portions in Daniel (2:4b-7:28) and Ezra (4:8-6:18, 7:12-26). The "
                    "New Testament was written in Koine Greek.",
        "script": "Hebrew square script (OT), Aramaic square script (portions), Greek "
                  "uncial and minuscule manuscripts (NT).",
        "linguistic_notes": "The Septuagint (LXX) translation into Greek (3rd-1st century "
                           "BC) was the Bible of the early church and is quoted extensively "
                           "in the New Testament. The Masoretic Text (MT) represents the "
                           "Hebrew tradition standardized by Jewish scribes (c. 7th-10th "
                           "century AD). The Dead Sea Scrolls revealed that the textual "
                           "situation before the MT standardization was more diverse than "
                           "previously thought — some scrolls align with the MT, others "
                           "with the LXX, and others with neither.",
        "grammar_match": "Multiple original languages across 1,400+ years of composition, "
                        "yet remarkable theological coherence — itself an argument for "
                        "divine superintendence of the canon."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "This study is built entirely on Scripture and aims to illuminate how "
                   "Scripture's own witness to itself informs canon formation.",

        "where_it_aligns": [
            "2 Timothy 3:16 — 'All Scripture is breathed out by God' establishes the "
            "principle that canonical books derive authority from divine origin, not "
            "human decision",
            "2 Peter 3:15-16 — Peter recognizes Paul's letters as 'Scripture' during "
            "the apostolic period, showing canon recognition was already happening",
            "Luke 24:44 — Jesus references 'the Law of Moses, the Prophets, and the "
            "Psalms' as a tripartite canon already recognized in His time",
            "Jude 3 — 'the faith once for all delivered to the saints' implies a fixed "
            "deposit of authoritative teaching",
            "Deuteronomy 4:2 — 'You shall not add to the word that I command you, nor "
            "take from it' establishes the principle of a closed canon"
        ],

        "where_it_diverges": [],

        "reader_guidance": "This study examines the human side of a divine process. God "
                          "breathed out Scripture; humans recognized it over time. Both "
                          "realities are true, and understanding the human process should "
                          "strengthen, not weaken, confidence in the divine product."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "Dead Sea Scrolls (c. 250 BC - AD 68) for the Old Testament; "
                    "Papyrus P52 (c. AD 125) for the New Testament — a fragment of "
                    "John 18, the earliest known NT manuscript.",
        "major_witnesses": [
            {"name": "Dead Sea Scrolls", "date": "c. 250 BC - AD 68",
             "note": "Over 900 manuscripts including every OT book except Esther. "
                     "Revolutionized understanding of the pre-Masoretic text."},
            {"name": "Codex Sinaiticus", "date": "c. AD 350",
             "note": "Complete NT plus portions of OT including the Deuterocanonical "
                     "books. Discovered at St. Catherine's Monastery, Sinai."},
            {"name": "Codex Vaticanus", "date": "c. AD 325-350",
             "note": "Nearly complete Bible including Deuterocanonical books. Held "
                     "in the Vatican Library."},
            {"name": "Muratorian Fragment", "date": "c. AD 170",
             "note": "Earliest known canon list. Lists most NT books and explicitly "
                     "rejects certain texts (Shepherd of Hermas for public reading)."}
        ],
        "reliability": "The biblical text is the best-attested ancient document in history. "
                       "Over 5,800 Greek NT manuscripts, 10,000+ Latin manuscripts, and "
                       "thousands in other languages. The textual variants that exist affect "
                       "no essential Christian doctrine."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "Canon formation occurred within the broader context of Second Temple "
                   "Judaism (for the OT) and early Christianity (for the NT). The process "
                   "was shaped by persecution, theological controversy, and the practical "
                   "needs of worshipping communities.",

        "geography": "Palestine (OT formation), the Mediterranean world (NT composition "
                     "and collection), Alexandria (Septuagint translation), Rome, Carthage, "
                     "Hippo (Western canon councils), Constantinople, Ethiopia (Eastern "
                     "canon traditions).",

        "historical_connections": "The destruction of the Second Temple in AD 70 accelerated "
                                 "OT canon fixation in Judaism (Council of Jamnia/Yavneh, "
                                 "c. AD 90). Roman persecution of Christians (especially "
                                 "Diocletian's order to surrender sacred books in AD 303) "
                                 "forced the church to decide which books were worth dying "
                                 "for — a powerful criterion for canonicity."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "moderate",
        "summary": "The canon formation process has significant implications for divine "
                   "council theology. The Dead Sea Scrolls preserved the original reading "
                   "of Deuteronomy 32:8 ('sons of God' rather than 'sons of Israel'), "
                   "which is foundational to the Heiser framework. The Masoretic Text's "
                   "alteration of this verse represents a theological correction that "
                   "obscured the divine council worldview — and the DSS discovery reversed "
                   "that obscuring. Similarly, the Ethiopian canon's inclusion of 1 Enoch "
                   "preserves the Watchers tradition that illuminates Genesis 6:1-4 and "
                   "the origin of the Nephilim. Canon differences between traditions often "
                   "correlate with how comfortable each tradition is with the supernatural "
                   "worldview of Second Temple Judaism.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 2 (Deuteronomy 32 worldview as canon framework)",
            "Reversing Hermon, introduction (why 1 Enoch matters for NT interpretation)",
            "Supernatural, chapter 3 (the biblical worldview vs. modern assumptions)"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "Constantine Did Not Choose the Bible",
            "body": "One of the most persistent myths about the Bible is that Emperor "
                    "Constantine decided which books to include at the Council of Nicaea "
                    "(AD 325). This is historically false. Nicaea addressed the Arian "
                    "controversy (the nature of Christ), not the biblical canon. The "
                    "canon was already substantially settled by the mid-2nd century "
                    "through organic church usage, and the first complete list matching "
                    "the modern NT canon came from Athanasius in AD 367 — over 40 years "
                    "after Nicaea. Dan Brown's The Da Vinci Code popularized this myth, "
                    "but no serious historian supports it."
        },
        {
            "type": "theology",
            "title": "Canon Differences Are Not a Crisis",
            "body": "The fact that Protestant, Catholic, Orthodox, and Ethiopian canons "
                    "differ in the number of books can feel unsettling. But the core canon "
                    "— the 39 OT books and 27 NT books — is shared by all major Christian "
                    "traditions. The disagreements concern the Deuterocanonical/Apocryphal "
                    "books (Tobit, Judith, Wisdom, Sirach, Baruch, 1-2 Maccabees, and "
                    "additions to Esther and Daniel). These books are valuable for historical "
                    "context but do not introduce doctrines that contradict the shared canon. "
                    "The Ethiopian tradition's inclusion of 1 Enoch and Jubilees preserves "
                    "Second Temple traditions that illuminate the canonical text."
        },
        {
            "type": "interpretation",
            "title": "Recognition vs. Creation",
            "body": "The church did not create the canon — it recognized it. This distinction "
                    "matters enormously. The books of the Bible were authoritative from the "
                    "moment of their composition because they were 'breathed out by God' "
                    "(2 Tim 3:16). The centuries-long process of canon formation was the "
                    "human side of recognizing what God had already done. The criteria used "
                    "by the early church (apostolic authorship or connection, theological "
                    "consistency, widespread usage, spiritual power) were tools for "
                    "identifying divine authority, not for conferring it."
        }
    ]
}
