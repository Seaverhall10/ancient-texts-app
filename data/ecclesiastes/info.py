"""
info.py -- Ecclesiastes (Qoheleth): Scholarly Text Introduction

This file provides the "front page" for Ecclesiastes in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Ecclesiastes is the most radical book in the Hebrew Bible -- a sustained
philosophical meditation on the meaning of life "under the sun" (tachath
hashamesh). Its author, Qoheleth ("the Assembler/Preacher"), relentlessly
probes the limits of human wisdom, pleasure, wealth, and achievement, finding
everything "hebel" -- vapor, breath, meaningless in the sense of transient and
ungraspable. The book's signature phrase "vanity of vanities, all is vanity"
(1:2) frames the entire argument. Yet Ecclesiastes is not nihilistic: its
repeated counsel is to fear God, enjoy the simple gifts he provides (food,
drink, companionship, work), and accept that human beings cannot comprehend
God's ways. The book qualifies and limits the confidence of Proverbs'
retribution principle, showing that the moral universe is more opaque than
conventional wisdom allows.
"""

TEXT_INFO = {
    "text_id": "ecclesiastes",
    "display_name": "Ecclesiastes (Qoheleth)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "Ecclesiastes is canonical in all Jewish and Christian traditions, though its "
                  "canonicity was debated in rabbinic discussions. The Mishnah (Yadayim 3:5) records a "
                  "dispute about whether Ecclesiastes 'defiles the hands' (the rabbinic idiom for "
                  "canonical authority), with the school of Shammai opposing and the school of Hillel "
                  "affirming. The Talmud (Shabbat 30b) records that 'the sages wished to hide the book "
                  "of Ecclesiastes because its words contradict one another' and because some statements "
                  "seemed to encourage hedonism. Its inclusion was secured because it begins and ends "
                  "with the fear of God (1:1 -- Solomon, who feared God; 12:13 -- 'Fear God and keep "
                  "his commandments'). Ecclesiastes is one of the five Megillot (scrolls) read at "
                  "Jewish festivals -- it is read during Sukkot (Feast of Tabernacles), the harvest "
                  "festival of joy, which the rabbis connected to Qoheleth's theme of enjoying God's "
                  "gifts. The New Testament does not directly quote Ecclesiastes but echoes its themes "
                  "extensively: Romans 8:20 ('the creation was subjected to futility/mataiotes') uses "
                  "the same Greek word the LXX uses for 'hebel.'"
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Solomon, based on the superscription: 'The words of the Preacher (Qoheleth), "
                       "the son of David, king in Jerusalem' (1:1). The autobiographical sections "
                       "describe unparalleled royal wealth, wisdom, building projects, and access to "
                       "pleasure (1:12-2:11) -- fitting Solomon's historical profile (1 Kings 3-10). "
                       "Rabbinic tradition (Bava Batra 15a) states that 'Hezekiah and his associates "
                       "wrote... Proverbs, Song of Songs, and Ecclesiastes,' meaning they compiled and "
                       "edited Solomon's words. Jewish tradition also associated the book with Solomon's "
                       "old age -- the reflections of a man who had experienced everything and found "
                       "it wanting.",

        "scholarly_debate": "Most critical scholars date Ecclesiastes to the post-exilic period, "
                           "specifically the 3rd century BC, based on: (1) linguistic evidence -- the "
                           "Hebrew of Ecclesiastes contains late features (Aramaisms, Persian loanwords, "
                           "and syntax patterns consistent with late biblical or early Mishnaic Hebrew); "
                           "(2) philosophical parallels with Hellenistic thought, particularly Epicureanism "
                           "and early Stoicism; (3) the social context of disillusionment that fits the "
                           "Ptolemaic period in Palestine. The Solomonic persona is understood as a literary "
                           "device (royal fiction) -- a later sage speaks through the mouth of Israel's "
                           "wisest king to demonstrate that even unlimited wisdom, wealth, and pleasure "
                           "cannot satisfy the human soul. Some scholars (Fredericks, Longman) argue for "
                           "an earlier date based on linguistic analysis that challenges the late-dating "
                           "consensus.",

        "bottom_line": "Whether Solomon wrote Ecclesiastes in his old age or a later sage adopted the "
                       "Solomonic voice to explore the limits of human achievement, the book's theological "
                       "contribution is the same: it exposes the 'hebel' (vapor) of all human pursuits "
                       "apart from the fear of God. The Solomonic persona is not deceptive but literary -- "
                       "the wisest and wealthiest king in history is the perfect test case for whether "
                       "earthly accomplishment can provide ultimate meaning. The answer is no."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Late in Solomon's reign (~940-930 BC), reflecting the wisdom and disillusionment "
                       "of his later years.",
        "critical_range": "Most scholars date the book to the 3rd century BC (~250-200 BC), during the "
                         "Ptolemaic period when Palestine was under Egyptian control. The epilogue "
                         "(12:9-14) may be a later editorial addition framing the book for orthodox "
                         "reception.",
        "evidence": "Key evidence includes: (1) The language of Ecclesiastes is the latest Hebrew in "
                    "the Old Testament -- more Aramaisms and late grammatical features than any other "
                    "biblical book except possibly Esther and Daniel. (2) The Persian loanword 'pardes' "
                    "(garden/park, 2:5) suggests post-exilic composition. (3) Dead Sea Scrolls fragments "
                    "(4QQoh^a, 4Q109) date to ~175-150 BC, providing a terminus ante quem (the book "
                    "must have been written before this date). (4) The earliest reliable attestation is "
                    "the Qumran fragment, placing composition before ~175 BC. (5) The book shows no "
                    "clear awareness of the Maccabean crisis (167-164 BC), which some take as evidence "
                    "for a pre-Maccabean date. (6) Ben Sira (~180 BC) may allude to Ecclesiastes themes "
                    "without directly quoting it."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The wise -- sages, students of wisdom, and anyone seeking meaning in a "
                            "world that does not conform to neat theological categories. If the Solomonic "
                            "persona is a literary device, the audience is specifically those who trust too "
                            "much in human wisdom and achievement. If written in the Ptolemaic period, the "
                            "audience includes Jews facing Hellenistic philosophy's competing claims about "
                            "the good life.",

        "purpose": "Ecclesiastes demolishes all false foundations for meaning: wisdom (1:12-18), "
                   "pleasure (2:1-11), work (2:18-23), wealth (5:10-17), and even justice (8:14). "
                   "Everything 'under the sun' (tachath hashamesh) is 'hebel' -- vapor, breath, "
                   "ephemeral, ungraspable. But this is not nihilism. The repeated positive counsel is: "
                   "'There is nothing better for a person than that he should eat and drink and find "
                   "enjoyment in his toil. This also, I saw, is from the hand of God' (2:24; cf. 3:12-13; "
                   "5:18-20; 8:15; 9:7-10). The gifts of ordinary life -- food, drink, companionship, "
                   "work -- are God's gifts to be received with gratitude. The conclusion (12:13) anchors "
                   "everything: 'Fear God and keep his commandments, for this is the whole duty of man.'",

        "theological_intent": "Ecclesiastes serves as the necessary corrective to an oversimplified "
                             "reading of Proverbs. If Proverbs teaches the retribution principle (the "
                             "righteous prosper, the wicked suffer), Ecclesiastes qualifies it: 'There "
                             "are righteous people who get what the actions of the wicked deserve, and "
                             "there are wicked people who get what the actions of the righteous deserve' "
                             "(8:14). The three wisdom books form a dialogue: Proverbs establishes the "
                             "general principle, Job challenges it through the experience of innocent "
                             "suffering, and Ecclesiastes observes that the principle fails to account "
                             "for life's radical unpredictability. Together they teach a mature wisdom: "
                             "trust God's general patterns while accepting that his specific governance "
                             "often exceeds human comprehension."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew (the latest Hebrew in the Old Testament)",
        "script": "Aramaic square script (post-exilic standard)",
        "linguistic_notes": "Ecclesiastes' Hebrew is distinctive: it contains more Aramaisms than any "
                           "other biblical book, uses late syntactic features (the relative pronoun she- "
                           "instead of asher, the suffix -i for first person in several forms), and "
                           "includes the Persian loanword 'pardes' (garden/park, 2:5). The verbal system "
                           "shows features transitional between biblical and Mishnaic Hebrew. The style "
                           "is characterized by repetition, rhetorical questions, and the refrain 'hebel' "
                           "(appearing 38 times in 12 chapters). The word 'hebel' literally means 'breath' "
                           "or 'vapor' -- something that exists momentarily and then vanishes. Its precise "
                           "connotation varies by context: futile, fleeting, absurd, incomprehensible, or "
                           "ironic. The term 'under the sun' (tachath hashamesh) appears 29 times as the "
                           "defining frame for Qoheleth's observations: this is about life from the human "
                           "perspective, limited to what can be seen and experienced in the earthly realm.",
        "grammar_match": "The prose style is repetitive and meditative rather than narrative or "
                        "proverbial. Qoheleth circles back to themes, restates and qualifies, and builds "
                        "his argument through accumulation rather than linear progression. This style has "
                        "been compared to philosophical discourse -- a kind of stream-of-consciousness "
                        "wisdom meditation."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Ecclesiastes IS scripture -- the Bible's most radical internal critique of "
                   "oversimplified theology, and the necessary companion to Proverbs and Job in the "
                   "wisdom dialogue.",
        "nt_usage": "The New Testament does not directly quote Ecclesiastes but echoes its themes "
                    "extensively. Romans 8:20 -- 'the creation was subjected to futility (mataiotes)' -- "
                    "uses the same Greek word the LXX uses to translate 'hebel.' Paul's context is "
                    "cosmic: the entire creation shares in the 'hebel' that Qoheleth observed, awaiting "
                    "liberation through Christ. Jesus' teaching about storing up treasures on earth "
                    "(Matthew 6:19-21) echoes Ecclesiastes 2:18-23 (toiling for wealth that passes to "
                    "others). The rich fool of Luke 12:13-21 embodies Ecclesiastes' warning about "
                    "accumulation without wisdom. James 4:14 ('What is your life? For you are a mist "
                    "that appears for a little time and then vanishes') could be a direct allusion to "
                    "'hebel.'",
        "internal_consistency": "Ecclesiastes stands in creative tension with Proverbs' retribution "
                               "theology but does not contradict it. Proverbs presents the general "
                               "pattern; Ecclesiastes documents the exceptions. Together with Job, the "
                               "three wisdom books form a complete theology: general principles (Proverbs), "
                               "the challenge of innocent suffering (Job), and the opacity of divine "
                               "governance (Ecclesiastes), all resolved in the fear of God."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: 4QQoh^a (4Q109), dating to ~175-150 BC. This is one "
                    "of the earliest biblical manuscripts from Qumran and provides an important "
                    "terminus ante quem for the book's composition.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. Ecclesiastes' MT is relatively well-preserved, "
                     "though some passages are textually uncertain due to the compressed, "
                     "allusive style."},
            {"name": "Septuagint (LXX)", "date": "2nd-1st century BC translation",
             "note": "The LXX of Ecclesiastes is remarkably literal -- one of the most 'wooden' "
                     "translations in the Greek Bible, following Hebrew word order and idiom closely. "
                     "This suggests the translator treated the text with extreme reverence. The key "
                     "translation is 'mataiotes' (futility/vanity) for 'hebel,' which influenced "
                     "the Latin 'vanitas' and all subsequent translations."},
            {"name": "Aquila's Greek Translation", "date": "~130 AD",
             "note": "The hyper-literal Greek translation by Aquila may have been influenced by "
                     "an earlier similarly literal translation tradition, possibly the same one "
                     "behind the LXX Ecclesiastes."},
            {"name": "Vulgate (Latin)", "date": "Jerome, ~405 AD",
             "note": "Jerome's 'vanitas vanitatum, omnia vanitas' is one of the most famous "
                     "phrases in Western literature. His translation shaped the reception of "
                     "Ecclesiastes for a millennium."}
        ],
        "reliability": "Ecclesiastes is well-attested for a book of its size. The Qumran fragment "
                       "confirms the early existence of the text in a form close to the MT. The LXX's "
                       "wooden literalism preserves a reliable witness to the Hebrew Vorlage. The "
                       "theologically crucial passages -- the 'hebel' framework, the enjoyment counsel, "
                       "the conclusion (12:13-14) -- are stable across all witnesses."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "If Solomonic, the setting is the united monarchy in Jerusalem (~950 BC). If "
                   "post-exilic (the majority scholarly view), the setting is Ptolemaic Palestine "
                   "(~250-200 BC), when Judea was a small province under Egyptian control. The social "
                   "context of the Ptolemaic period -- heavy taxation, limited social mobility, exposure "
                   "to Hellenistic philosophy, and the experience of life under foreign rule -- provides "
                   "a plausible background for Qoheleth's observations about injustice, the futility of "
                   "toil, and the unpredictability of fortune.",

        "geography": "Jerusalem is the implied setting (1:1, 'king in Jerusalem'). The references to "
                     "the Temple (5:1-7) and the city (10:16-17) suggest an urban, cosmopolitan "
                     "environment. The commercial observations (11:1-6, casting bread upon the waters) "
                     "reflect a society engaged in trade.",

        "historical_connections": "Ecclesiastes has been compared to several ANE texts: (1) The Gilgamesh "
                                 "Epic's advice to Gilgamesh from the alewife Siduri ('Fill your belly. "
                                 "Day and night make merry... dance and play') closely parallels "
                                 "Qoheleth's enjoyment counsel. (2) The Egyptian 'Harper's Songs' (Middle "
                                 "Kingdom) similarly urge the enjoyment of life in the face of death. (3) "
                                 "Hellenistic philosophy -- Epicurean emphasis on moderate pleasure and "
                                 "Stoic acceptance of fate -- offers thematic parallels, though direct "
                                 "literary dependence is unproven. (4) The 'Dialogue of Pessimism' "
                                 "(Babylonian, ~1000 BC) debates the value of various human activities "
                                 "with a similar skeptical tone."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "moderate",
        "summary": "Ecclesiastes does not contain explicit divine council scenes, but its theology "
                   "operates within the divine council framework in important ways."
                   "\n\n"
                   "THE HIDDENNESS OF GOD'S GOVERNANCE: Qoheleth's central complaint is that human "
                   "beings cannot discern God's ways: 'He has made everything beautiful in its time. "
                   "Also, he has put eternity (olam) into man's heart, yet so that he cannot find out "
                   "what God has done from the beginning to the end' (3:11). God has embedded a sense "
                   "of transcendence ('eternity') in the human heart but withholds the ability to "
                   "comprehend the divine plan. In the divine council framework, this is the 'glory "
                   "of God to conceal things' (Proverbs 25:2) -- YHWH's governance includes dimensions "
                   "hidden from human view. The divine council operates with purposes that mortals "
                   "'under the sun' cannot see."
                   "\n\n"
                   "THE FEAR OF GOD: Despite his skepticism about human wisdom's ability to discern "
                   "God's ways, Qoheleth consistently affirms the fear of God: 'I perceived that "
                   "whatever God does endures forever; nothing can be added to it, nor anything taken "
                   "from it. God has done it, so that people fear before him' (3:14). 'Fear God and "
                   "keep his commandments, for this is the whole duty of man. For God will bring every "
                   "deed into judgment, with every secret thing, whether good or evil' (12:13-14). "
                   "The fear of God -- the same posture Proverbs and Job commend -- is the anchor "
                   "amid the hebel. In the divine council worldview, the appropriate response to "
                   "YHWH's inscrutable governance is reverent trust, not despair."
                   "\n\n"
                   "JUDGMENT AND ACCOUNTABILITY: Qoheleth affirms that God will judge: 'I said in "
                   "my heart, God will judge the righteous and the wicked, for there is a time for "
                   "every matter and for every work' (3:17). The apparent absence of justice 'under "
                   "the sun' does not mean the absence of justice altogether. The divine council "
                   "framework locates ultimate justice in God's eschatological act -- a judgment that "
                   "operates beyond the visible realm of human experience.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 36-37 (the hiddenness of God's governance and eschatological judgment)",
            "Supernatural, chapter 15 (the 'already/not yet' of divine justice -- relevant to Qoheleth's observations)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "Hebel -- The Key Word and Its Many Meanings",
            "body": "The word 'hebel' (traditionally translated 'vanity') appears 38 times in "
                    "Ecclesiastes -- more than in the rest of the Old Testament combined. Its literal "
                    "meaning is 'breath' or 'vapor' (the name Abel, 'Hevel,' is the same word). The "
                    "metaphor captures something that exists momentarily and then vanishes -- like "
                    "breath on a cold day. But 'hebel' does not always mean the same thing in "
                    "Ecclesiastes. In some contexts it means 'fleeting' (life is short), in others "
                    "'futile' (effort produces no lasting result), in others 'absurd' (life does not "
                    "conform to moral expectations), and in others 'incomprehensible' (God's ways "
                    "cannot be figured out). The translation 'vanity' (from the Vulgate's 'vanitas') "
                    "captures some but not all of these senses. 'Meaningless' (NIV 1984) is too "
                    "nihilistic. 'Vapor' or 'breath' preserves the metaphorical richness."
        },
        {
            "type": "interpretation",
            "title": "Under the Sun -- The Limits of Qoheleth's Perspective",
            "body": "The phrase 'under the sun' (tachath hashamesh) appears 29 times and defines the "
                    "scope of Qoheleth's investigation. He is examining life from the human vantage "
                    "point -- what can be observed, experienced, and reasoned about within the earthly "
                    "realm. This is crucial for interpretation: Qoheleth is not claiming that life has "
                    "no ultimate meaning, but that meaning cannot be established from the 'under the "
                    "sun' perspective alone. The fear of God (12:13) points beyond the sun to the God "
                    "who governs from above it. The New Testament's revelation of resurrection, "
                    "judgment, and eternal life answers the questions Qoheleth raises but cannot resolve "
                    "from his earthly vantage point."
        },
        {
            "type": "context",
            "title": "Ecclesiastes and the Wisdom Dialogue",
            "body": "Ecclesiastes should not be read in isolation. It is the third voice in a wisdom "
                    "dialogue that includes Proverbs and Job. Proverbs teaches the general retribution "
                    "principle: wisdom leads to life, folly to death. Job challenges the principle when "
                    "the righteous suffer. Ecclesiastes observes that the principle fails to account for "
                    "life's radical unpredictability: 'The race is not to the swift, nor the battle to "
                    "the strong, nor bread to the wise, nor riches to the intelligent, nor favor to "
                    "those with knowledge, but time and chance happen to them all' (9:11). Together, "
                    "the three books teach that God's governance is real, generally follows discernible "
                    "patterns, but ultimately operates beyond the reach of human wisdom. The appropriate "
                    "response is not cynicism but reverent trust: 'Fear God and keep his commandments.'"
        }
    ]
}
