"""
info.py -- 2 Chronicles (Divrei HaYamim Bet): Scholarly Text Introduction

This file provides the "front page" for 2 Chronicles in the Ancient Texts Library.
2 Chronicles covers from Solomon's reign through the Babylonian exile and ends
with the decree of Cyrus. The book contains one of the most explicit divine council
scenes in the Old Testament: Micaiah's vision of YHWH's throne room in 2 Chronicles
18:18-22, where YHWH asks "Who will entice Ahab?" and a spirit volunteers to be a
lying spirit in the mouths of the prophets. Temple theology dominates throughout:
the glory of YHWH filling Solomon's temple, the reforms of Hezekiah and Josiah,
and the theological explanations for exile and the hope of return.
"""

TEXT_INFO = {
    "text_id": "2chronicles",
    "display_name": "2 Chronicles (Divrei HaYamim)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "2 Chronicles is the second half of a single work (Divrei HaYamim) that was "
                  "divided into two books by the Septuagint translators. In the Hebrew Bible, "
                  "Chronicles stands as the final book of the canon -- the Hebrew Bible ends "
                  "with 2 Chronicles 36:23, Cyrus's decree: 'The LORD, the God of heaven, has "
                  "given me all the kingdoms of the earth, and he has charged me to build him "
                  "a house at Jerusalem, which is in Judah. Whoever is among you of all his "
                  "people, may the LORD his God be with him. Let him go up.' The Hebrew canon "
                  "thus ends with an open invitation to return and rebuild -- a message of hope. "
                  "In the Christian Old Testament, Chronicles is placed among the historical "
                  "books. Its canonicity has never been questioned by any tradition."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Attributed to Ezra the scribe by Jewish tradition (Talmud Bava Batra 15a). "
                       "The overlap between the ending of 2 Chronicles (36:22-23) and the beginning "
                       "of Ezra (1:1-3) has been cited as evidence of common authorship. The "
                       "Chronicler's intimate knowledge of temple worship, Levitical organization, "
                       "and priestly genealogies suggests a writer deeply embedded in the Second "
                       "Temple establishment.",

        "scholarly_debate": "The question of whether the Chronicler authored Ezra-Nehemiah remains "
                           "debated. Japhet and Williamson argued against unified authorship, noting "
                           "differences in theology (Chronicles is more inclusive toward the north; "
                           "Ezra-Nehemiah emphasizes separation) and language. The overlap in 2 Chr "
                           "36:22-23 // Ezra 1:1-3 may simply be a literary link, not proof of "
                           "common authorship. The Chronicler draws on extensive sources, citing over "
                           "20 by name: 'the Book of the Kings of Israel and Judah' (2 Chr 35:27), "
                           "'the Chronicles of the Kings of Judah and Israel' (16:11), and individual "
                           "prophetic writings attributed to Isaiah (26:22), Iddo (13:22), and Shemaiah "
                           "(12:15). These may be independent documents or different names for the same "
                           "composite source.",

        "bottom_line": "The Chronicler is a theologically sophisticated writer -- likely a Levitical "
                       "priest or temple scribe in post-exilic Jerusalem -- who retells Israel's "
                       "monarchic history with a singular focus: the temple, worship, and the "
                       "faithfulness or unfaithfulness of kings measured by their devotion to YHWH's "
                       "house. 2 Chronicles is not a supplement to Kings but an independent "
                       "theological interpretation of the same period."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "~450-400 BC (early post-exilic period, associated with Ezra's era)",
        "critical_range": "Same dating considerations as 1 Chronicles: the genealogies extending "
                         "beyond Zerubbabel and Persian-period vocabulary suggest a date in the "
                         "late 5th or 4th century BC. The Chronicler's awareness of Persian "
                         "administrative structures and his positive view of Cyrus (36:22-23) fit "
                         "the Persian period. Some scholars push the date into the early Hellenistic "
                         "period (~350-300 BC).",
        "evidence": "The mention of darics (1 Chr 29:7), the genealogies extending multiple "
                    "generations beyond Zerubbabel, and linguistic features of Late Biblical "
                    "Hebrew all point to the late Persian or early Hellenistic period. The "
                    "theological concerns -- legitimacy of the Second Temple, continuity of "
                    "Davidic hope, proper Levitical worship -- are quintessentially post-exilic."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The post-exilic community centered on the Second Temple in Jerusalem. "
                            "These were people living under Persian rule, without a Davidic king on "
                            "the throne, asking whether God's promises still held. 2 Chronicles "
                            "addresses their concerns by showing that temple faithfulness brings "
                            "blessing and temple unfaithfulness brings judgment -- and that even "
                            "after judgment, God provides a way back.",

        "purpose": "2 Chronicles presents the monarchic period as a sustained argument about "
                   "faithfulness. Every king is evaluated by a single criterion: did he seek "
                   "YHWH and maintain proper temple worship? Those who did (Solomon, Jehoshaphat, "
                   "Hezekiah, Josiah) prospered. Those who did not (Rehoboam initially, Ahaz, "
                   "Manasseh initially) suffered. The theological formula is explicit: 'If you "
                   "seek him, he will be found by you, but if you forsake him, he will forsake "
                   "you' (15:2). This is not simplistic retribution theology but covenantal "
                   "logic: faithfulness to YHWH's covenant brings covenant blessing.",

        "theological_intent": "The Chronicler writes to anchor the post-exilic community in three "
                             "certainties: (1) the temple is YHWH's chosen dwelling place -- the glory "
                             "that filled Solomon's temple (5:13-14) validates the Second Temple; "
                             "(2) the Davidic covenant endures -- even in exile, the line persists; "
                             "(3) repentance always opens a door back to God. The most quoted verse "
                             "in 2 Chronicles -- 7:14 -- captures this theology: 'If my people who are "
                             "called by my name humble themselves, and pray and seek my face and turn "
                             "from their wicked ways, then I will hear from heaven and will forgive their "
                             "sin and heal their land.'"
    },

    # -- ORIGINAL LANGUAGE ------------------------------------------------------
    "language": {
        "original": "Late Biblical Hebrew",
        "script": "Aramaic square script (post-exilic standard)",
        "linguistic_notes": "2 Chronicles displays the same Late Biblical Hebrew features as "
                           "1 Chronicles: Aramaic influence, Persian loanwords, and syntactic "
                           "developments characteristic of the post-exilic period. The Chronicler "
                           "systematically updates archaic language from his Samuel-Kings sources, "
                           "providing an invaluable window into how Hebrew evolved from the pre-exilic "
                           "to post-exilic periods. Scholars like Avi Hurvitz and Robert Polzin have "
                           "used the Chronicler's linguistic modifications as key evidence for dating "
                           "Late Biblical Hebrew.",
        "grammar_match": "Consistent with other Late Biblical Hebrew texts: Ezra, Nehemiah, Esther, "
                        "and late Psalms. The language is accessible to a post-exilic audience while "
                        "maintaining continuity with the earlier literary tradition."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------------
    "scripture_alignment": {
        "verdict": "2 Chronicles IS scripture -- it provides the priestly-theological interpretation "
                   "of Israel's monarchic period and the definitive biblical theology of temple worship.",
        "nt_usage": "Jesus quotes 2 Chronicles 24:20-22 (the murder of Zechariah the priest) in "
                    "Matthew 23:35 and Luke 11:51: 'from the blood of righteous Abel to the blood of "
                    "Zechariah.' Since Abel is the first martyr in Genesis (the first book of the "
                    "Hebrew canon) and Zechariah the last martyr recorded in 2 Chronicles (the last "
                    "book of the Hebrew canon), Jesus is encompassing the entire Old Testament witness. "
                    "The temple theology of 2 Chronicles undergirds the New Testament's understanding "
                    "of Jesus as the true temple (John 2:19-21), the church as God's temple "
                    "(1 Cor 3:16-17), and the heavenly temple (Hebrews 8-10). The Chronicler's "
                    "principle that God inhabits the praises of his people (2 Chr 5:13-14) becomes "
                    "foundational for New Testament worship theology.",
        "internal_consistency": "2 Chronicles parallels 1 Kings - 2 Kings extensively but with "
                               "significant additions, omissions, and theological reframing. The "
                               "differences serve the Chronicler's purposes and are not contradictions. "
                               "Both Kings and Chronicles are inspired presentations of the same history "
                               "from complementary theological perspectives."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragment 4QChr (~50 BC), preserving small portions. "
                    "As with 1 Chronicles, the Qumran evidence is minimal.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. 2 Chronicles is well-preserved in the MT."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC translation",
             "note": "The Greek 'Paraleipomena B.' Generally follows the MT with some variant "
                     "readings, particularly in numerical data and royal speeches."},
            {"name": "Vulgate", "date": "~400 AD (Jerome)",
             "note": "Jerome's Latin translation, based on the Hebrew."},
            {"name": "Dead Sea Scrolls", "date": "4QChr, ~50 BC",
             "note": "Minimal representation at Qumran."}
        ],
        "reliability": "The text of 2 Chronicles is well-preserved. Cross-checking with the "
                       "parallel passages in 1-2 Kings provides additional textual security."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------------
    "historical_context": {
        "setting": "2 Chronicles covers from Solomon's accession (~970 BC) through the "
                   "Babylonian exile (586 BC) to Cyrus's decree (538 BC) -- over 400 years "
                   "of Judean monarchic history. The narrative focuses almost exclusively on "
                   "the southern kingdom (Judah), with the northern kingdom mentioned only when "
                   "it intersects with Judah's story. The composition date is post-exilic "
                   "(~450-350 BC).",

        "geography": "Jerusalem and the temple dominate the geographical focus. Important sites "
                     "include: Mount Moriah (the temple mount, 2 Chr 3:1), the Valley of "
                     "Beracah (Jehoshaphat's victory, 20:26), Lachish (where Amaziah fled, "
                     "25:27), and the major cult sites that reforming kings destroyed (Hezekiah "
                     "and Josiah's reforms).",

        "historical_connections": "The events of 2 Chronicles are corroborated by multiple "
                                 "extra-biblical sources: Shishak's invasion (2 Chr 12) is recorded "
                                 "on the Bubastite Portal at Karnak; Sennacherib's siege of Jerusalem "
                                 "(2 Chr 32) is described in the Taylor Prism; the Babylonian "
                                 "destruction of Jerusalem (2 Chr 36) is documented in the Babylonian "
                                 "Chronicles; and Cyrus's decree (2 Chr 36:22-23) aligns with the "
                                 "Cyrus Cylinder's policy of restoring displaced peoples and their gods."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "high",
        "summary": "2 Chronicles contains one of the most explicit divine council scenes in the "
                   "entire Old Testament: 2 Chronicles 18:18-22 (= 1 Kings 22:19-23). The prophet "
                   "Micaiah describes a vision of YHWH seated on his throne 'with all the host of "
                   "heaven (kol-tseva hashamayim) standing on his right hand and on his left' (18:18). "
                   "YHWH asks: 'Who will entice Ahab the king of Israel, that he may go up and fall "
                   "at Ramoth-gilead?' (18:19). Various spirits offer suggestions. Then 'a spirit came "
                   "forward and stood before the LORD, saying, I will entice him... I will go out "
                   "and will be a lying spirit in the mouth of all his prophets' (18:20-21). YHWH "
                   "says: 'You are to entice him, and you shall succeed; go out and do so' (18:21). "
                   "This scene reveals: (1) YHWH presides over a heavenly court; (2) the court includes "
                   "diverse spiritual beings (the 'host of heaven'); (3) these beings participate in "
                   "deliberation; (4) a specific spirit volunteers for a mission; (5) YHWH authorizes "
                   "the mission; (6) the spirit executes it by operating through human agents (false "
                   "prophets). This is the divine council in action -- a deliberative body under YHWH's "
                   "sovereignty.\n\n"
                   "Additionally, the temple theology pervading 2 Chronicles has divine council "
                   "significance. When the glory of YHWH fills Solomon's temple (5:13-14) -- 'so that "
                   "the priests could not stand to minister because of the cloud, for the glory of "
                   "the LORD filled the house of God' -- this is the divine presence descending from "
                   "the council chamber to dwell among humans. The temple is heaven on earth.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 2 (the divine council -- Micaiah's vision as primary text)",
            "Supernatural, chapter 4 (the divine assembly and its members)",
            "The Naked Bible Podcast, episodes on 1 Kings 22 / 2 Chronicles 18 (the lying spirit)",
            "Angels (2018), discussion of the host of heaven as divine council members"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "The Chronicler's Theological History",
            "body": "2 Chronicles is not 'Kings retold' -- it is an independent theological "
                    "interpretation of the same period. The Chronicler adds material not found "
                    "in Kings (Jehoshaphat's judicial reform, Hezekiah's Passover, Manasseh's "
                    "repentance) and omits material found in Kings (most northern kingdom history). "
                    "Reading Chronicles as a flawed copy of Kings misses the point entirely. The "
                    "Chronicler has a different audience, different purpose, and different "
                    "theological emphasis. Both are inspired; both are authoritative; they serve "
                    "different functions in the canon."
        },
        {
            "type": "interpretation",
            "title": "Micaiah's Vision: The Divine Council in Action",
            "body": "2 Chronicles 18:18-22 is one of the most important passages in the Bible "
                    "for understanding how God governs the spiritual realm. A lying spirit is "
                    "sent by God to deceive Ahab's prophets. This raises difficult questions "
                    "about God and deception, but the text is clear: YHWH is sovereign over all "
                    "spirits, including those who deceive. The lying spirit operates only with "
                    "divine authorization and for divine purposes. This is not God lying but "
                    "God using all agents -- including deceptive ones -- to accomplish his "
                    "righteous judgment against a wicked king."
        },
        {
            "type": "scholarship",
            "title": "The Numbers in Chronicles",
            "body": "2 Chronicles frequently records larger numbers than the parallel accounts "
                    "in Kings: larger armies, more offerings, greater wealth. Three explanations "
                    "are offered: (1) the Chronicler had access to different, possibly more "
                    "complete source material; (2) the numbers involve a different counting "
                    "system (the Hebrew word eleph can mean 'thousand' or 'military unit/clan,' "
                    "which significantly affects interpretation); (3) the numbers are typological "
                    "and rhetorical, following ANE conventions of royal aggrandizement. In any "
                    "case, the theological point of the numbers -- God's abundant provision for "
                    "those who seek him -- is clear regardless of how one resolves the arithmetic."
        }
    ]
}
