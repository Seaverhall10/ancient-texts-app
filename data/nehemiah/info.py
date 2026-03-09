"""
info.py -- Nehemiah: Scholarly Text Introduction

This file provides the "front page" for Nehemiah in the Ancient Texts Library.
Nehemiah narrates the rebuilding of Jerusalem's walls and the renewal of the
covenant under Nehemiah the governor and Ezra the priest-scribe. It is a
book of practical faith: prayer, planning, and perseverance in the face of
opposition. The great public reading of the Torah (ch. 8) and the covenant
renewal ceremony (chs. 9-10) represent the birth of Torah-centered Judaism
as a community identity.
"""

TEXT_INFO = {
    "text_id": "nehemiah",
    "display_name": "Nehemiah",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "Nehemiah is universally canonical. Originally part of a single Ezra-Nehemiah "
                  "book in the Hebrew tradition (Talmud Bava Batra 15a), it was separated in "
                  "Christian manuscripts from the 3rd century onward. In the Hebrew Bible it "
                  "is placed among the Ketuvim, near Chronicles. The 'Nehemiah memoir' sections "
                  "(first-person accounts) give it a unique autobiographical character among "
                  "biblical books."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Nehemiah son of Hacaliah, cupbearer to King Artaxerxes I of Persia, who "
                       "served as governor of Judah. The first-person 'Nehemiah memoir' sections "
                       "(1:1-7:5; 12:27-13:31) are widely accepted as Nehemiah's own composition. "
                       "The Talmud (Bava Batra 15a) credits Nehemiah with completing the work "
                       "Ezra began.",

        "scholarly_debate": "The Nehemiah memoir is among the most historically credible first-person "
                           "accounts in the Hebrew Bible. Its vivid detail, personal emotion, and "
                           "self-serving appeals to God ('Remember me, O my God, for good,' 13:31) "
                           "have the hallmarks of authentic autobiography. The third-person sections "
                           "(chs. 8-10, the Ezra-Torah reading material) may have been inserted by "
                           "an editor combining the Ezra and Nehemiah traditions. The relationship "
                           "between the Nehemiah memoir, the Ezra memoir, and the editorial framework "
                           "continues to be debated.",

        "bottom_line": "The core of Nehemiah is an authentic memoir by a Jewish governor in "
                       "Persian-period Judah, supplemented by lists, prayers, and narrative "
                       "sections from the Ezra-Nehemiah editorial tradition. It provides a "
                       "uniquely personal window into the challenges of rebuilding a covenant "
                       "community."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events span ~445-430 BC. Nehemiah arrives in Jerusalem in the "
                       "twentieth year of Artaxerxes I (445 BC, Neh 2:1) and serves as governor "
                       "for twelve years (5:14). He returns to Persia and then comes back for a "
                       "second term (13:6-7).",
        "critical_range": "The events are firmly dated by the reference to Artaxerxes I (465-424 BC). "
                         "The Nehemiah memoir was likely written during or shortly after Nehemiah's "
                         "governorship. The final compilation of the book may date to the late 5th "
                         "or 4th century BC.",
        "evidence": "The Elephantine Papyri (408 BC) mention 'Sanballat, governor of Samaria' -- "
                    "the same Sanballat who opposes Nehemiah (2:10, 4:1). The papyri also mention "
                    "'Johanan the high priest' (Neh 12:22). These external confirmations anchor "
                    "Nehemiah firmly in the mid-5th century BC."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The post-exilic Jewish community in Jerusalem and the diaspora, "
                            "particularly those who needed encouragement that the physical and "
                            "spiritual rebuilding of Judah was possible despite opposition.",

        "purpose": "Nehemiah serves multiple purposes: (1) documenting the wall rebuilding as "
                   "evidence of YHWH's faithfulness and the community's resilience; (2) establishing "
                   "Torah as the community's constitution through the public reading ceremony (ch. 8); "
                   "(3) recording the covenant renewal that bound the community to specific obligations "
                   "(ch. 10); (4) providing a model of faithful leadership that combines prayer with "
                   "practical action.",

        "theological_intent": "Nehemiah's theology is profoundly practical: pray AND plan, trust God "
                             "AND post guards, confess sin AND make commitments. The wall is not merely "
                             "a military fortification but a statement of identity: we are a distinct "
                             "people, set apart for YHWH, with defined boundaries. The public Torah "
                             "reading (ch. 8) marks the moment when the written Word becomes the "
                             "community's central authority -- the birth of the 'People of the Book.'"
    },

    # -- ORIGINAL LANGUAGE ------------------------------------------------------
    "language": {
        "original": "Hebrew (with some Aramaic in quoted documents)",
        "script": "Aramaic square script",
        "linguistic_notes": "Nehemiah is written primarily in Late Biblical Hebrew, with Aramaic "
                           "influence consistent with the Persian period. The Nehemiah memoir sections "
                           "have a distinctive personal style -- direct, urgent, emotional -- that "
                           "differs from the more formal list-and-document style of the editorial "
                           "framework. Persian loanwords (tirshatha for 'governor,' 8:9; pardes for "
                           "'park/garden,' 2:8) confirm the Persian-period setting.",
        "grammar_match": "Consistent with Late Biblical Hebrew and other Persian-period texts."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Nehemiah IS scripture -- it documents the rebuilding of God's community and "
                   "the establishment of Torah as the community's constitution.",
        "nt_usage": "The New Testament does not directly quote Nehemiah but stands on its legacy. "
                    "The synagogue system implied in Nehemiah 8 (public Torah reading with "
                    "interpretation) is the same system Jesus and Paul use to teach. The wall "
                    "of Jerusalem that Nehemiah rebuilt is the wall Jesus entered for his "
                    "triumphal entry and from which the temple he cleansed was visible.",
        "internal_consistency": "Nehemiah connects to Ezra (the Ezra-Torah reading in ch. 8 bridges "
                               "both books), to the prophets (Haggai, Zechariah, and Malachi address "
                               "the same post-exilic community), and to Chronicles (the genealogies "
                               "and Levitical organization)."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------------
    "manuscripts": {
        "earliest": "No Nehemiah manuscripts have been found at Qumran -- it is one of the few "
                    "OT books entirely absent from the Dead Sea Scrolls. This may be coincidence "
                    "or may reflect Qumran's lack of interest in the Jerusalem establishment "
                    "Nehemiah represents.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text of Nehemiah."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC",
             "note": "Part of 'Esdras B' in the LXX. Generally follows the MT."},
            {"name": "Vulgate", "date": "~400 AD (Jerome)",
             "note": "Jerome translated from the Hebrew; treated Nehemiah as 'Second Ezra.'"}
        ],
        "reliability": "The text is well-preserved. The absence from Qumran means we lack "
                       "pre-Masoretic Hebrew evidence, but the LXX confirms the MT's general reliability."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------------
    "historical_context": {
        "setting": "Mid-5th century BC, the Persian province of Yehud (Judah) under Artaxerxes I. "
                   "Jerusalem is partially inhabited but unwalled -- vulnerable and demoralized.",

        "geography": "Jerusalem is the focus: its walls, gates (at least 10 named in ch. 3), and "
                     "the temple precinct. The surrounding region includes Samaria (Sanballat's "
                     "base), Ammon (Tobiah's territory), and the Arabian desert (Geshem's domain). "
                     "The Persian capital Susa (1:1) is where Nehemiah begins his story.",

        "historical_connections": "The Elephantine Papyri confirm Sanballat as governor of Samaria "
                                 "and provide independent evidence of the political dynamics described "
                                 "in Nehemiah. The Wadi Daliyeh papyri from the Samarian caves provide "
                                 "additional evidence for Persian-period administration. Archaeological "
                                 "excavations in Jerusalem have identified potential remains of Nehemiah's "
                                 "wall in the City of David area."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "low",
        "summary": "Nehemiah does not contain explicit divine council content but operates within "
                   "its framework. Nehemiah's prayers assume YHWH's sovereign governance of all "
                   "rulers and events. His statement that 'the God of heaven will make us prosper' "
                   "(2:20) reflects confidence in divine council governance. The opposition of "
                   "Sanballat, Tobiah, and Geshem -- each representing a different neighboring "
                   "people -- may reflect the territorial spiritual dynamics of Deuteronomy 32:8-9: "
                   "the nations surrounding Israel are under the governance of divine beings allotted "
                   "at Babel, and their human rulers oppose YHWH's reclamation of his own territory. "
                   "The wall rebuilding is, in this framework, the reassertion of YHWH's territorial "
                   "claim against rival spiritual jurisdictions.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 27 (post-exilic restoration and divine geography)",
            "Supernatural, chapter 17 (the cosmic implications of rebuilding Zion)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "Nehemiah's Leadership Style",
            "body": "Nehemiah is one of the most practically-minded leaders in the Bible. He prays "
                    "AND plans. He fasts AND surveys the walls at night. He trusts God AND posts "
                    "armed guards. He confesses sin AND organizes labor crews. Modern readers who "
                    "divide faith from action, prayer from planning, can learn much from Nehemiah's "
                    "integration of spiritual dependence and practical wisdom."
        },
        {
            "type": "interpretation",
            "title": "The Separation Question",
            "body": "Like Ezra, Nehemiah enforces separation from surrounding peoples (13:23-27). "
                    "The concern is covenantal, not racial: the peoples of the land practiced "
                    "idolatry, and intermarriage historically led Israel into the same practices. "
                    "Nehemiah cites Solomon explicitly: 'Did not Solomon king of Israel sin on "
                    "account of such women?... foreign women made even him to sin' (13:26). The "
                    "post-exilic community is fragile and cannot survive another cycle of "
                    "syncretism and exile."
        }
    ]
}
