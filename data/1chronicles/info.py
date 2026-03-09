"""
info.py -- 1 Chronicles (Divrei HaYamim Aleph): Scholarly Text Introduction

This file provides the "front page" for 1 Chronicles in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

1 Chronicles retells Israel's history from Adam to David with a priestly,
temple-centered theological lens. Its genealogical prologue (chs. 1-9) is
the most extensive in the Bible, and its portrait of David focuses almost
exclusively on his role as temple preparer and worship organizer. Notably,
1 Chronicles 21:1 introduces "Satan" (ha-satan) standing against Israel --
a divine council adversary figure whose role must be read alongside the
parallel account in 2 Samuel 24:1 where YHWH himself incites David.
"""

TEXT_INFO = {
    "text_id": "1chronicles",
    "display_name": "1 Chronicles (Divrei HaYamim)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "1 Chronicles is universally recognized as canonical scripture by Jewish, "
                  "Catholic, Orthodox, and Protestant traditions. In the Hebrew Bible, "
                  "1-2 Chronicles (originally a single book called Divrei HaYamim, 'The Words "
                  "of the Days') is placed at the very end of the Ketuvim (Writings), making "
                  "it the final book of the Hebrew canon. This placement is theologically "
                  "significant: the Hebrew Bible ends with Cyrus's decree to rebuild the "
                  "temple (2 Chr 36:23), pointing forward to restoration. In the Septuagint "
                  "and Christian Old Testament, Chronicles is placed after Kings as a supplement "
                  "to the historical narrative. The Greek title 'Paraleipomena' ('Things Left "
                  "Out') reflects the ancient view that Chronicles supplements Kings with "
                  "additional material. No mainstream tradition has questioned its canonicity."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Jewish tradition (Talmud Bava Batra 15a) attributes Chronicles to Ezra "
                       "the scribe. The book shares significant vocabulary, themes, and theological "
                       "emphasis with Ezra-Nehemiah: concern for temple worship, Levitical genealogies, "
                       "liturgical practices, and the restoration community. The genealogies in "
                       "1 Chronicles 1-9 show the same meticulous attention to priestly and Levitical "
                       "lineages that characterizes Ezra's work.",

        "scholarly_debate": "Modern scholarship generally identifies the author as 'the Chronicler' -- "
                           "a post-exilic Levitical writer (or school) working in Jerusalem, probably "
                           "associated with the temple. The question of whether the Chronicler is the "
                           "same person as the author of Ezra-Nehemiah has been debated extensively. "
                           "Japhet (1968) and Williamson (1977) argued against common authorship based "
                           "on theological and linguistic differences, while others (Freedman, Cross) "
                           "maintained the traditional connection. The Chronicler drew on multiple "
                           "sources: Samuel-Kings (extensively), genealogical records, temple archives, "
                           "and possibly independent prophetic sources now lost (the Chronicler cites "
                           "'the Chronicles of Samuel the Seer,' 'the Chronicles of Nathan the Prophet,' "
                           "and 'the Chronicles of Gad the Seer' in 1 Chr 29:29).",

        "bottom_line": "Whether written by Ezra or by another post-exilic Levitical author, "
                       "1 Chronicles is a theologically purposeful retelling of Israel's history "
                       "that centers the story on the temple, the Davidic covenant, and the worship "
                       "of YHWH. It is not a neutral historical chronicle but a priestly interpretation "
                       "of history designed to anchor the post-exilic community in the continuity of "
                       "God's purposes from creation to the restoration."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "~450-400 BC (early post-exilic period, associated with Ezra's reforms)",
        "critical_range": "Most scholars date the final form of Chronicles to the late 5th or "
                         "4th century BC. The genealogies in 1 Chronicles 3:17-24 extend at least "
                         "six generations beyond Zerubbabel (who returned from exile ~538 BC), "
                         "suggesting a date no earlier than ~400 BC. Some scholars push the date "
                         "into the early Hellenistic period (~350-300 BC) based on linguistic "
                         "features and possible awareness of Greek administrative terms. The "
                         "Chronicler's sources, however, include genuinely ancient material -- "
                         "the genealogies likely preserve pre-exilic records, and the parallel "
                         "passages with Samuel-Kings demonstrate dependence on pre-exilic texts.",
        "evidence": "The latest datable reference in 1 Chronicles is the genealogy of "
                    "Zerubbabel's descendants (3:17-24), which extends several generations "
                    "beyond the initial return from exile. The Persian loanword daric (darkmon, "
                    "1 Chr 29:7) confirms a Persian-period or later date of composition. The "
                    "theological emphasis on the temple, Levitical worship, and the continuity "
                    "of the Davidic line all fit the concerns of the post-exilic community "
                    "in Jerusalem. The oldest manuscript fragments come from the Dead Sea Scrolls "
                    "(4QChr, ~50 BC), though these are small and fragmentary."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The post-exilic Jewish community in Jerusalem -- specifically those "
                            "who had returned from Babylon and were rebuilding their identity around "
                            "the Second Temple. This community needed to know: Are we still God's "
                            "people? Does the Davidic covenant still hold? Is our temple legitimate? "
                            "Do we stand in continuity with pre-exilic Israel? Chronicles answers "
                            "all of these questions with a resounding yes.",

        "purpose": "1 Chronicles serves three primary purposes: (1) IDENTITY -- the genealogies "
                   "(chs. 1-9) connect the post-exilic community to Adam, Abraham, and David, "
                   "establishing unbroken continuity; (2) TEMPLE LEGITIMACY -- David's extensive "
                   "preparations for the temple (chs. 22-29) establish that the temple worship "
                   "system is not a human invention but divinely authorized through the Davidic "
                   "covenant; (3) WORSHIP AS MISSION -- the Chronicler's David is primarily a "
                   "worship leader, not a warrior-king. His greatest achievements are organizing "
                   "the Levitical singers, appointing gatekeepers, and preparing materials for "
                   "the temple. The post-exilic community is being told: your calling is worship.",

        "theological_intent": "The Chronicler deliberately omits David's adultery with Bathsheba, "
                             "Absalom's rebellion, and most of the court intrigues of Samuel-Kings. "
                             "This is not dishonesty but theological selectivity: the Chronicler is "
                             "not writing biography but liturgical history. He presents David as the "
                             "ideal king whose primary vocation was preparing for God's dwelling "
                             "place among his people. This Davidic portrait points forward to the "
                             "ultimate son of David who will build the true temple (2 Sam 7:12-14; "
                             "John 2:19-21)."
    },

    # -- ORIGINAL LANGUAGE ------------------------------------------------------
    "language": {
        "original": "Late Biblical Hebrew",
        "script": "Aramaic square script (the standard script of the post-exilic period)",
        "linguistic_notes": "The Hebrew of Chronicles is distinctly post-exilic, showing features "
                           "characteristic of Late Biblical Hebrew (LBH): increased use of Aramaic "
                           "loanwords, Persian administrative terms (daric/darkmon for a gold coin, "
                           "1 Chr 29:7), changes in verbal syntax (increased use of the participle "
                           "for present tense), and vocabulary shifts from Classical Biblical Hebrew. "
                           "Robert Polzin's landmark study (1976) demonstrated systematic linguistic "
                           "differences between Chronicles and its Vorlage in Samuel-Kings, confirming "
                           "that the Chronicler updated archaic language for his audience. The genealogies "
                           "preserve some archaic name forms that may reflect genuinely ancient sources.",
        "grammar_match": "The language of Chronicles is consistent with other post-exilic biblical "
                        "texts (Ezra, Nehemiah, Esther, late Psalms) and with what we know of "
                        "late 5th/4th century Hebrew from inscriptions and the Dead Sea Scrolls."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------------
    "scripture_alignment": {
        "verdict": "1 Chronicles IS scripture -- it is the priestly lens through which Israel's "
                   "history is retold for the worshipping community.",
        "nt_usage": "The New Testament draws heavily on Chronicles' theology even when not quoting "
                    "it directly. Matthew's genealogy of Jesus (Matt 1:1-17) follows the Chronicler's "
                    "method of tracing messianic lineage through the Davidic line. The Davidic "
                    "covenant promise ('I will be to him a father, and he shall be to me a son,' "
                    "1 Chr 17:13) is quoted in Hebrews 1:5 as fulfilled in Christ. Jesus' cleansing "
                    "of the temple (Matt 21:12-13) presupposes the Chronicler's theology that the "
                    "temple is YHWH's chosen dwelling place. The early church's emphasis on worship, "
                    "music, and liturgy owes much to the Chronicler's portrait of Davidic worship.",
        "internal_consistency": "1 Chronicles parallels large sections of 2 Samuel but with significant "
                               "theological reinterpretation. Where 2 Samuel tells David's story as "
                               "political-military history, Chronicles retells it as liturgical-covenantal "
                               "history. The differences are not contradictions but complementary "
                               "perspectives -- the same events viewed through different theological lenses. "
                               "The genealogies connect to Genesis, the temple preparations connect to "
                               "Exodus (tabernacle), and the Davidic covenant connects to the prophetic "
                               "hope of an eternal kingdom."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragment 4QChr (~50 BC), preserving small portions of "
                    "the text. This is the only known Qumran manuscript of Chronicles, suggesting "
                    "the book may have had limited circulation at Qumran -- possibly because the "
                    "Qumran community, being anti-temple establishment, had less interest in the "
                    "Chronicler's pro-temple theology.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. Chronicles is well-preserved in the MT tradition."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC translation",
             "note": "The Greek Paraleipomena. The LXX of Chronicles generally follows the MT "
                     "closely but has some variant readings in the genealogies and numerical data."},
            {"name": "Vulgate", "date": "~400 AD (Jerome)",
             "note": "Jerome translated Chronicles from the Hebrew, noting its importance for "
                     "understanding Israelite genealogy and temple practice."},
            {"name": "Dead Sea Scrolls", "date": "4QChr, ~50 BC",
             "note": "Only one small fragment survives from Qumran, making Chronicles the least "
                     "attested OT book at Qumran."}
        ],
        "reliability": "The text of 1 Chronicles is well-preserved. Because large sections parallel "
                       "Samuel-Kings, textual critics can cross-check readings. In some cases, "
                       "Chronicles preserves a better reading than the MT of Samuel (which has "
                       "known textual difficulties, especially in 1-2 Samuel)."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------------
    "historical_context": {
        "setting": "1 Chronicles covers from Adam (in genealogy) through the death of David "
                   "(~970 BC). The narrative proper (chs. 10-29) covers David's reign: "
                   "approximately 1010-970 BC. However, the book was WRITTEN in the post-exilic "
                   "period (~450-350 BC) for a community living under Persian rule. The gap "
                   "between the events described and the date of composition is crucial for "
                   "understanding the Chronicler's purpose: he is interpreting the past to "
                   "address the present.",

        "geography": "The geographical focus of 1 Chronicles is Jerusalem and its environs, "
                     "especially the threshing floor of Ornan/Araunah the Jebusite (1 Chr 21:15-22:1), "
                     "which David purchases as the future temple site. The genealogies range across "
                     "the entire ancient Near East (Mesopotamia, Canaan, Edom, Moab), tracing "
                     "Israel's connections to the wider world of nations.",

        "historical_connections": "The post-exilic setting places the Chronicler in Persian-period "
                                 "Yehud (the Persian province of Judah), a small community centered "
                                 "on Jerusalem and the rebuilt Second Temple (completed 516 BC). The "
                                 "community was led by priests and Levites rather than kings, which "
                                 "explains the Chronicler's emphasis on Levitical worship over royal "
                                 "politics. The Persian policy of supporting local religious institutions "
                                 "(attested in the Cyrus Cylinder and other texts) provided the political "
                                 "framework within which the temple community flourished."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "moderate",
        "summary": "1 Chronicles contains one of the most theologically significant divine council "
                   "references in the Old Testament: 1 Chronicles 21:1 -- 'Then Satan stood against "
                   "Israel and incited David to number Israel.' This must be read alongside its "
                   "parallel in 2 Samuel 24:1: 'The anger of the LORD was kindled against Israel, "
                   "and he incited David.' The same event is attributed to YHWH in Samuel and to "
                   "'Satan' (ha-satan, the adversary) in Chronicles. This is not a contradiction "
                   "but a revelation of divine council mechanics: YHWH's sovereign decree is executed "
                   "through a council member -- the adversary (cf. Job 1-2, where the satan operates "
                   "within the council under YHWH's permission; Zechariah 3:1-2, where the satan "
                   "accuses Joshua the high priest before the Angel of YHWH). The Chronicler, writing "
                   "later than the author of Samuel, makes explicit what was implicit: when YHWH "
                   "'incites,' he does so through the agency of a divine council member who functions "
                   "as an adversary/accuser. This is a window into how the divine council operates "
                   "-- God's sovereignty is mediated through his council agents.\n\n"
                   "Additionally, the temple theology pervading 1 Chronicles has divine council "
                   "dimensions. The temple is the earthly counterpart to YHWH's heavenly throne room "
                   "where the council meets. The Levitical singers, gatekeepers, and priests mirror "
                   "the heavenly worship described in Isaiah 6 and Revelation 4-5. David's organization "
                   "of temple worship is patterned after 'the plan (tavnit) that he had by the Spirit' "
                   "(1 Chr 28:12) -- the same language used for the tabernacle pattern shown to Moses "
                   "on the mountain (Exod 25:9, 40), suggesting a heavenly blueprint.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 3 (the satan as divine council prosecutor)",
            "Supernatural, chapter 14 (Satan's role in the divine council)",
            "Angels (2018), discussion of the satan figure in Job, Zechariah, and Chronicles",
            "The Naked Bible Podcast, episodes on 1 Chronicles 21 and the divine council adversary"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "Chronicles vs. Samuel-Kings: Two Perspectives, One History",
            "body": "If you read Chronicles alongside Samuel-Kings, you will notice the Chronicler "
                    "omits, adds, and reshapes material freely. David's adultery with Bathsheba is "
                    "absent. Absalom's rebellion is absent. The northern kingdom barely appears. "
                    "These omissions are not errors or cover-ups -- they reflect the Chronicler's "
                    "theological purpose. He is writing temple history, not royal biography. Both "
                    "accounts are inspired and authoritative; they simply emphasize different aspects "
                    "of the same events."
        },
        {
            "type": "interpretation",
            "title": "The Satan of 1 Chronicles 21",
            "body": "1 Chronicles 21:1 is one of only three Old Testament passages that use 'Satan' "
                    "(without the definite article in Hebrew) as a proper name or title for a "
                    "specific being. In Job 1-2 and Zechariah 3, the figure appears as 'the satan' "
                    "(ha-satan, with the article) -- 'the adversary,' a role within the divine "
                    "council. In 1 Chronicles 21:1, the article is absent, which some scholars "
                    "read as a shift toward understanding Satan as a specific entity rather than "
                    "merely a role. This text is a crucial data point in tracing the development "
                    "of Israel's understanding of the divine council adversary."
        },
        {
            "type": "scholarship",
            "title": "The Genealogies Are Not Filler",
            "body": "Modern readers often skip 1 Chronicles 1-9 as tedious lists. For the original "
                    "audience, these genealogies were identity documents. They answered the question: "
                    "Who are we? The post-exilic community needed to establish that they were the "
                    "legitimate heirs of Abraham, David, and the Levitical priesthood. The genealogies "
                    "are the Chronicler's theological argument that God's covenant purposes have not "
                    "been broken by exile. Every name is a link in the chain of faithfulness."
        }
    ]
}
