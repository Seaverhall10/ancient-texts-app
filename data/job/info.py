"""
info.py -- Job (Iyyov): Scholarly Text Introduction

This file provides the "front page" for Job in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Job is the premier divine council text in the Wisdom literature. The prologue
(chapters 1-2) provides the only narrative scene in the Hebrew Bible where
ha-Satan appears as a member of the divine council, presenting himself among
the bene ha-elohim ("sons of God") before YHWH's throne. The book addresses
the deepest question of theodicy -- why do the righteous suffer? -- and resolves
it not with philosophical argument but with theophany: YHWH speaks from the
whirlwind and reveals the cosmic scope of his governance, including his
mastery over Behemoth and Leviathan, chaos creatures that represent forces
beyond human control. Job is the Bible's most sustained engagement with the
problem of undeserved suffering, the operations of the divine council, and
the limits of human wisdom before the Creator.
"""

TEXT_INFO = {
    "text_id": "job",
    "display_name": "Job (Iyyov)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "Job is universally recognized as canonical scripture by all Jewish and Christian "
                  "traditions. In the Hebrew Bible it is placed in the Writings (Ketuvim), though its "
                  "exact position varies: the Talmud (Bava Batra 14b) places it after Psalms and before "
                  "Proverbs; the Leningrad Codex has the order Psalms-Job-Proverbs; the Aleppo Codex "
                  "reverses Job and Proverbs. In the Christian Old Testament, Job is placed among the "
                  "poetic books, usually after Esther and before Psalms. The New Testament alludes to Job "
                  "in several key passages: James 5:11 ('You have heard of the steadfastness of Job, and "
                  "you have seen the purpose of the Lord, how the Lord is compassionate and merciful'), "
                  "1 Corinthians 3:19 quotes Job 5:13 ('He catches the wise in their craftiness'), and "
                  "Romans 11:35 echoes Job 41:11 ('Who has given a gift to him that he might be repaid?'). "
                  "The book's canonical authority has never been questioned by any tradition."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud (Bava Batra 14b-15a) records a debate: one view attributes Job to "
                       "Moses, suggesting he wrote it during his forty years in Midian. Another tradition "
                       "holds that Job was written by Job himself or by an anonymous Israelite sage. Some "
                       "rabbis placed Job in the patriarchal period (before Moses), others in the time of "
                       "the judges, the exile, or the return. The diversity of rabbinic opinion itself "
                       "suggests that authorship was uncertain from very early. The book shows no "
                       "awareness of the Mosaic covenant, the Exodus, or Israelite history, which is "
                       "consistent with either a very early setting or deliberate literary universalism.",

        "scholarly_debate": "Modern scholarship generally treats Job as a composite work: an ancient prose "
                           "tale (the prologue, 1:1-2:13, and epilogue, 42:7-17) that may date to the "
                           "second millennium BC, into which a later poet inserted the dialogue cycles "
                           "(3:1-42:6) -- perhaps in the 7th-5th century BC. The Elihu speeches (32-37) "
                           "are widely regarded as a later addition because: (1) Elihu is not mentioned in "
                           "the prologue or epilogue; (2) his speeches interrupt the transition from Job's "
                           "final oath to YHWH's response; (3) his vocabulary and style differ from the "
                           "main dialogue. However, the theological role of Elihu as a transitional voice "
                           "between human wisdom and divine revelation has led some scholars (Andersen, "
                           "Hartley) to defend his speeches as integral. The language of Job is the most "
                           "difficult Hebrew in the Bible, with an extraordinarily high concentration of "
                           "hapax legomena (words that appear only once), Aramaisms, and possible Arabic "
                           "cognates -- consistent with a wisdom tradition rooted in the wider Semitic world.",

        "bottom_line": "Whether composed by a single genius or shaped through centuries of sapiential "
                       "tradition, Job as we have it is a masterwork of theological literature. The prose "
                       "frame sets the divine council stage; the poetic dialogues explore theodicy with "
                       "unparalleled depth; the theophany resolves the crisis not through explanation but "
                       "through encounter. The question of authorship does not diminish the theological "
                       "power of a book that dares to bring human suffering before the throne of God and "
                       "receives an answer that transcends rational categories."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The narrative setting places Job in the patriarchal era -- he is described as a "
                       "man of the East (qedem), measures wealth in livestock, serves as family priest, "
                       "and lives 140 years after his restoration. If Mosaic authorship is accepted, the "
                       "composition would date to ~1400 BC.",
        "critical_range": "The prose tale may preserve traditions from the second millennium BC (parallels "
                         "with Mesopotamian suffering-righteous texts from that era). The poetic dialogue "
                         "is typically dated to the 7th-5th century BC based on linguistic evidence and "
                         "thematic parallels with exilic/post-exilic wisdom theology. The Elihu speeches "
                         "may be a further addition from the 5th-4th century BC. Final compilation: "
                         "~500-300 BC.",
        "evidence": "Key evidence includes: (1) The name 'Job' (Iyyov) appears in second-millennium "
                    "Egyptian Execration Texts and Amarna Letters, confirming the antiquity of the "
                    "tradition. (2) Ezekiel 14:14, 20 names Job alongside Noah and Daniel as exemplary "
                    "righteous figures, indicating that the Job tradition was well established by the "
                    "6th century BC. (3) The Dead Sea Scrolls preserve fragments of Job in Hebrew "
                    "(4QJob^a, 2Q15) and an Aramaic Targum of Job (11QtgJob, 4QtgJob) -- the oldest "
                    "known Targum of any biblical book, dating to ~150-50 BC. (4) The Septuagint (LXX) "
                    "of Job is about one-sixth shorter than the MT, omitting passages throughout the "
                    "dialogues, which may reflect either an earlier Hebrew Vorlage or deliberate "
                    "abridgment. (5) The Testament of Job (1st century BC - 1st century AD) is an "
                    "expanded retelling that emphasizes Job's endurance and connects his story to "
                    "apocalyptic themes."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The wise -- the sages, scribes, and theologians of ancient Israel and the "
                            "broader Semitic world. Job is wisdom literature in its most radical form: "
                            "it challenges the very foundations of conventional wisdom (the retribution "
                            "principle: the righteous prosper, the wicked suffer) that Proverbs and "
                            "Deuteronomy seem to affirm. The setting in 'the land of Uz' (not Israel) "
                            "and the absence of Israelite covenant theology give the book a universal "
                            "scope: this is not about Israel's covenant relationship but about the "
                            "fundamental human relationship with God.",

        "purpose": "Job addresses the most devastating theological question: Why do the righteous "
                   "suffer if God is just? The three friends (Eliphaz, Bildad, Zophar) represent "
                   "conventional wisdom: suffering implies sin; repent and be restored. Job refuses "
                   "this answer because he knows it is false in his case. Elihu introduces the idea "
                   "of suffering as discipline. But the book's answer comes only in the theophany "
                   "(chapters 38-41): YHWH does not explain Job's suffering. Instead, he reveals the "
                   "staggering complexity of the cosmos he governs -- including the divine council, the "
                   "foundations of the earth, the wild animals, and the chaos monsters Behemoth and "
                   "Leviathan. The implicit answer: the universe operates on a scale that transcends "
                   "human moral accounting. Trust is demanded, not explanation.",

        "theological_intent": "Job's deepest theological contribution is its insistence that the "
                             "relationship between God and humanity cannot be reduced to a transactional "
                             "formula. The retribution principle is true in general but cannot be applied "
                             "as a diagnostic tool to individual cases. The divine council scene (1-2) "
                             "reveals that Job's suffering has a purpose Job cannot see -- it is part of "
                             "a cosmic drama involving the adversary's challenge to the genuineness of "
                             "human faithfulness. The theophany reveals that God's governance encompasses "
                             "realities far beyond human comprehension. Job's final response -- 'I had "
                             "heard of you by the hearing of the ear, but now my eye sees you' (42:5) -- "
                             "is the resolution: not answers, but encounter."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew (with the most difficult and archaic Hebrew in the entire Bible)",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "Job's Hebrew is the most challenging in the Bible. The book contains over "
                           "100 hapax legomena (words found nowhere else in scripture), an extraordinarily "
                           "high proportion for any biblical text. Many terms have cognates in Arabic, "
                           "Aramaic, and Akkadian but not elsewhere in Hebrew, suggesting the author drew "
                           "from a broad Semitic lexical range. The Aramaisms are particularly concentrated "
                           "in the Elihu speeches (32-37), which some scholars see as evidence of a "
                           "different author and others attribute to the character's non-Israelite origin. "
                           "The poetic sections employ sophisticated literary techniques: extended metaphor, "
                           "irony, legal language (the riv motif), hymnic praise, and nature poetry. The "
                           "divine speeches (38-41) represent some of the most majestic Hebrew poetry "
                           "ever composed, with vivid imagery of the cosmos, the wild animals, and the "
                           "chaos creatures Behemoth and Leviathan.",
        "grammar_match": "The prose frame (1:1-2:13; 42:7-17) uses straightforward narrative Hebrew "
                        "consistent with classical biblical prose. The poetic dialogue (3:1-42:6) uses "
                        "dense, archaic, and often obscure poetic Hebrew that has generated more textual "
                        "uncertainty than perhaps any other biblical book. Many verses remain genuinely "
                        "uncertain in meaning despite centuries of scholarship."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Job IS scripture -- the Bible's supreme exploration of theodicy, divine sovereignty, "
                   "and the divine council's operations in the unseen realm.",
        "nt_usage": "The New Testament draws on Job at several key points. James 5:11 holds up Job as "
                    "the paradigm of patient endurance. 1 Corinthians 3:19 quotes Job 5:13 ('He catches "
                    "the wise in their craftiness') -- Eliphaz's words, ironically, are quoted as "
                    "scripture even though Job challenges much of what Eliphaz says. Romans 11:35 echoes "
                    "Job 41:11 in Paul's doxology about God's unsearchable ways. The broader theology of "
                    "Job -- that innocent suffering can have transcendent purpose, that God's ways exceed "
                    "human comprehension, that vindication comes after suffering -- prepares the way for "
                    "the cross. Jesus, the truly righteous sufferer, experiences what Job experienced in "
                    "type: abandonment, false accusation, cosmic struggle, and ultimate vindication.",
        "internal_consistency": "Job connects to the divine council theology of Psalm 82, 89, and "
                               "1 Kings 22 through its portrayal of the bene ha-elohim gathered before "
                               "YHWH. The creation theology of chapters 38-39 parallels Genesis 1-2, "
                               "Psalm 104, and Proverbs 8. The chaos monster traditions (Leviathan, "
                               "Behemoth, Rahab) connect to Psalm 74:13-14, Isaiah 27:1, and "
                               "Revelation 12-13. Job's cry for a mediator (9:33; 16:19; 19:25) "
                               "anticipates the New Testament's answer in Christ."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments from Qumran: 4QJob^a (4Q99), 4QJob^b (4Q100), and "
                    "2Q15, dating to the 1st century BC. The Aramaic Targum of Job from Qumran "
                    "(11QtgJob, 4QtgJob) is the oldest known Targum of any biblical book, dating to "
                    "~150-50 BC, demonstrating that Job was being translated and interpreted in Aramaic "
                    "well before the common era.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. Job's MT is challenging due to its difficult vocabulary "
                     "and uncertain text in many passages."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The LXX of Job is approximately one-sixth shorter than the MT, omitting lines "
                     "and passages throughout the dialogues. The shorter text may reflect an earlier "
                     "Hebrew Vorlage or deliberate Greek abridgment. Origen's Hexapla marked the "
                     "additions from Theodotion to fill the gaps."},
            {"name": "Aramaic Targum (11QtgJob)", "date": "~150-50 BC",
             "note": "The oldest Targum of any biblical book. Preserves portions of Job 17-42 in "
                     "Aramaic with interpretive expansions. Demonstrates that Job was being studied "
                     "and translated in the Second Temple period."},
            {"name": "Peshitta (Syriac)", "date": "2nd-3rd century AD",
             "note": "The Syriac translation sometimes clarifies obscure Hebrew passages and preserves "
                     "interpretive traditions from the Aramaic-speaking Jewish community."},
            {"name": "Vulgate (Latin)", "date": "Jerome, ~405 AD",
             "note": "Jerome translated Job directly from the Hebrew and noted its extraordinary "
                     "difficulty. His translation of Job 19:25-26 ('I know that my Redeemer lives') "
                     "became foundational for Christian liturgy and theology."}
        ],
        "reliability": "Job's text is the most uncertain of any biblical book due to its difficult "
                       "vocabulary and the significant divergence between the MT and LXX. However, the "
                       "narrative framework (prologue and epilogue), the theophany speeches, and the "
                       "key theological passages (1:21; 13:15; 19:25-27; 42:5-6) are stable across all "
                       "witnesses. The Qumran Targum confirms that the book was being actively studied "
                       "and translated in the Second Temple period."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Job is set 'in the land of Uz' (1:1) -- a region associated with Edom, southeast "
                   "of Israel (cf. Lamentations 4:21, 'O daughter of Edom, you who dwell in the land "
                   "of Uz'). The setting is deliberately non-Israelite: Job is a righteous Gentile, "
                   "his friends come from Edomite and Arabian regions (Teman, Shuah, Naamah, Buz), "
                   "and the religious practices described (family sacrifice, no Temple or priesthood) "
                   "are pre-Mosaic. The patriarchal setting -- great wealth in livestock, longevity of "
                   "140 additional years, family-based religion -- places the narrative in the second "
                   "millennium BC, whether or not the composition is later.",

        "geography": "The 'land of Uz' is most likely in the territory of Edom/northern Arabia. "
                     "Eliphaz comes from Teman (a city or region in Edom, cf. Obadiah 9). Bildad is "
                     "from Shuah (associated with Abraham's son Shuah through Keturah, Gen 25:2, "
                     "possibly in the Syrian desert). Zophar is from Naamah (location uncertain). "
                     "Elihu is from Buz (associated with Nahor's son Buz, Gen 22:21, in Aramean "
                     "territory). The Sabeans (1:15) and Chaldeans (1:17) who attack Job's property "
                     "are known raiders from southern Arabia and Mesopotamia respectively.",

        "historical_connections": "The suffering-righteous-person genre is well attested in the ANE. "
                                 "The Sumerian 'Man and His God' (~2000 BC) tells of a pious man who "
                                 "suffers and is eventually restored. The Babylonian 'Ludlul Bel Nemeqi' "
                                 "('I Will Praise the Lord of Wisdom,' ~1700 BC) describes a nobleman's "
                                 "suffering, confusion about divine justice, and eventual restoration by "
                                 "Marduk. The 'Babylonian Theodicy' (~1000 BC) is an acrostic dialogue "
                                 "between a sufferer and a friend, debating divine justice in a format "
                                 "remarkably similar to Job's dialogue structure. These parallels show that "
                                 "Job participates in a widespread ANE wisdom tradition, while surpassing "
                                 "all parallels in theological depth, literary sophistication, and the "
                                 "radicality of its divine council framework."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Job contains the most explicit divine council narrative in the Hebrew Bible. The "
                   "prologue (chapters 1-2) places the reader in the heavenly throne room where YHWH "
                   "presides over the assembled bene ha-elohim ('sons of God') -- the divine council "
                   "of spiritual beings who serve as YHWH's royal court."
                   "\n\n"
                   "THE DIVINE COUNCIL SCENE (Job 1:6-12; 2:1-6): 'Now there was a day when the sons "
                   "of God (bene ha-elohim) came to present themselves before YHWH, and ha-Satan (the "
                   "Adversary) also came among them' (1:6). This is the divine council in session: the "
                   "bene ha-elohim are the same class of beings mentioned in Genesis 6:1-4 (where they "
                   "descend to take human wives) and in Deuteronomy 32:8 (where they are allotted the "
                   "nations). They 'present themselves' (hityatsev) before YHWH -- a technical term for "
                   "appearing before a superior in a formal assembly (cf. 1 Kings 22:19, where Micaiah "
                   "sees 'all the host of heaven standing beside YHWH on his right hand and on his "
                   "left'). Ha-Satan is not yet the personal name 'Satan' of later tradition but a "
                   "title with the definite article: 'the adversary' or 'the accuser' -- a prosecutorial "
                   "role within the divine council. He challenges the genuineness of Job's faithfulness: "
                   "'Does Job fear God for nothing?' (1:9). The implication: human loyalty to God is "
                   "merely transactional. YHWH permits the test, establishing boundaries: 'Behold, all "
                   "that he has is in your hand. Only against him do not stretch out your hand' (1:12). "
                   "The second council scene (2:1-6) escalates: 'Behold, he is in your hand; only spare "
                   "his life' (2:6). The entire book's drama is framed by this divine council "
                   "deliberation that Job never sees and never learns about."
                   "\n\n"
                   "THE MORNING STARS AND SONS OF GOD (Job 38:4-7): In the theophany, YHWH asks Job: "
                   "'Where were you when I laid the foundation of the earth?... when the morning stars "
                   "(kokhve voqer) sang together and all the sons of God (bene elohim) shouted for joy?' "
                   "(38:4, 7). This confirms the divine council's existence at creation itself. The "
                   "'morning stars' is a parallel term for the bene elohim -- celestial beings who "
                   "witnessed and celebrated the creation of the earth. The same imagery appears in "
                   "Isaiah 14:12 (Helel ben Shachar, 'Day Star, son of Dawn') for the rebellious divine "
                   "being. Job 38:7 establishes that the divine council predates the physical cosmos."
                   "\n\n"
                   "BEHEMOTH AND LEVIATHAN (Job 40:15-41:34): YHWH's descriptions of Behemoth and "
                   "Leviathan transcend any natural animal. Leviathan breathes fire (41:18-21), cannot "
                   "be captured by any human means (41:1-11), and is called 'king over all the sons of "
                   "pride' (41:34). In the ANE context, Leviathan (Ugaritic: Litanu) is the chaos "
                   "serpent defeated by Baal in the Baal Cycle. Isaiah 27:1 prophesies that 'YHWH will "
                   "punish Leviathan the fleeing serpent, Leviathan the twisting serpent, and he will "
                   "slay the dragon that is in the sea.' Psalm 74:14 recounts how God 'crushed the "
                   "heads of Leviathan.' In the divine council framework, these chaos creatures "
                   "represent the spiritual forces of chaos that only YHWH can master. Job is told: "
                   "you cannot even handle Leviathan -- how can you challenge the God who controls him?",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 2-3 (the divine council -- Job 1-2 as the paradigmatic scene)",
            "The Unseen Realm, chapter 8 (ha-Satan's role in the divine council)",
            "The Unseen Realm, chapter 10-11 (the bene ha-elohim of Genesis 6 and Job 1-2)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 2-3 (ha-Satan as accuser)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 2-3 (the bene elohim)",
            "The Naked Bible Podcast, episodes on Job and the divine council",
            "Supernatural, chapter 3 (the divine council framework -- Job as key example)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Divine Council Prologue -- What Job Never Knew",
            "body": "The reader of Job knows something Job never learns: the reason for his suffering. "
                    "The prologue (1:1-2:13) reveals a scene in the divine council where ha-Satan "
                    "challenges the genuineness of Job's faithfulness. YHWH permits the test. But this "
                    "information is never communicated to Job -- not in the dialogues, not in the "
                    "theophany, not in the epilogue. Job goes to his grave without knowing why he "
                    "suffered. This narrative strategy is theologically profound: the reader sees the "
                    "cosmic purpose; Job must trust without seeing. The application to every sufferer "
                    "is clear: there may be purposes in your suffering that operate in the unseen "
                    "realm, purposes you will never be told in this life. The demand is trust, not "
                    "explanation."
        },
        {
            "type": "interpretation",
            "title": "Ha-Satan in Job -- Not Yet the Devil",
            "body": "The figure in Job 1-2 is ha-Satan -- 'the adversary' with the definite article, "
                    "indicating a title/role, not a personal name. He appears as a member of the divine "
                    "council, not as a fallen rebel. His role is prosecutorial: he tests the genuineness "
                    "of human loyalty to God. This is a different portrait than the Satan of later "
                    "Christian theology (informed by Isaiah 14, Ezekiel 28, Revelation 12). In the "
                    "development of the biblical tradition, ha-Satan evolves from a divine council "
                    "functionary (Job, Zechariah 3) to a cosmic adversary (1 Chronicles 21:1, where "
                    "the article is dropped, and the name becomes personal). The New Testament "
                    "synthesizes these strands into the figure of the Devil. Michael Heiser argues "
                    "that the Job portrayal is the earliest stratum: a member of the council with a "
                    "specific adversarial function, operating under YHWH's authority and within YHWH's "
                    "boundaries."
        },
        {
            "type": "context",
            "title": "Job's Redeemer -- The Goel of 19:25-27",
            "body": "Job 19:25-27 is one of the most famous and debated passages in the book: 'For I "
                    "know that my Redeemer (goeli) lives, and at the last he will stand upon the earth. "
                    "And after my skin has been thus destroyed, yet in my flesh I shall see God, whom "
                    "I shall see for myself, and my eyes shall behold, and not another.' The goel is "
                    "the kinsman-redeemer -- the family member obligated to advocate for the vulnerable "
                    "(Ruth 3-4, Leviticus 25:25). Job identifies this goel as someone who will vindicate "
                    "him after death, standing on the earth (or 'on the dust') at 'the last' (acharon). "
                    "Christian interpretation has consistently seen this as a prophetic anticipation of "
                    "Christ as the living Redeemer who will raise the dead on the last day. The Hebrew "
                    "text is genuinely difficult, and the precise meaning of 'in my flesh I shall see "
                    "God' is debated, but the passage's orientation toward post-mortem vindication is "
                    "remarkable for a text that elsewhere shows limited hope beyond death (cf. 14:10-12)."
        },
        {
            "type": "scholarship",
            "title": "The Elihu Problem -- Intruder or Theologian?",
            "body": "The Elihu speeches (chapters 32-37) are the most debated section of Job from a "
                    "literary-critical perspective. Arguments for later addition: Elihu is absent from "
                    "the prologue and epilogue, his speeches interrupt the flow from Job's final oath "
                    "(chapter 31) to YHWH's response (chapter 38), and his language shows more "
                    "Aramaisms than the main dialogues. Arguments for original composition: Elihu's "
                    "theology of suffering as divine discipline (33:14-30) bridges between the friends' "
                    "rigid retribution theology and YHWH's transcendent answer, his anger at all four "
                    "previous speakers is dramatically appropriate, and his storm language (36:26-37:24) "
                    "sets the stage for YHWH's whirlwind appearance. Whether original or added, Elihu "
                    "serves a canonical function: he shows that even the best human theology ('God uses "
                    "suffering to teach') falls short of the divine perspective that only the theophany "
                    "can provide."
        }
    ]
}
