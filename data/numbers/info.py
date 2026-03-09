"""
info.py — Numbers (Bamidbar): Scholarly Text Introduction

This file provides the "front page" for Numbers in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?
"""

TEXT_INFO = {
    "text_id": "numbers",
    "display_name": "Numbers (Bamidbar)",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical — Old Testament / Torah",
        "detail": "Numbers is universally recognized as canonical scripture by "
                  "Jewish, Catholic, Orthodox, and Protestant traditions. It is "
                  "the fourth book of the Torah (Pentateuch), known in Hebrew as "
                  "Bamidbar ('In the Wilderness') from its opening word, and in "
                  "English as 'Numbers' from the Septuagint title Arithmoi, "
                  "referencing the two censuses (chapters 1 and 26) that frame "
                  "the book. Numbers bridges the legislation of Sinai (Leviticus) "
                  "and the covenant renewal on the Plains of Moab (Deuteronomy), "
                  "narrating the catastrophic failure of the exodus generation and "
                  "the rise of the next. Its canonical status has never been "
                  "questioned by any mainstream tradition."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "Moses, as affirmed by Jewish tradition (Talmud Bava Batra 14b-15a), "
                       "Jesus (John 3:14, referencing the bronze serpent of Num 21), and the "
                       "New Testament authors. Numbers attributes legislation directly to "
                       "Moses throughout ('The LORD spoke to Moses' occurs over 80 times). "
                       "Numbers 33:2 explicitly states that 'Moses wrote down their starting "
                       "places, stage by stage, by command of the LORD' — one of the clearest "
                       "internal claims of Mosaic authorship in the Torah. Numbers 12:3 "
                       "('Now the man Moses was very meek, more than all people who were on "
                       "the face of the earth') is frequently cited as evidence of non-Mosaic "
                       "authorship, though tradition responds that Moses wrote it by "
                       "divine dictation (Talmud Megillah 9a).",

        "scholarly_debate": "Critical scholarship identifies Numbers as a composite of "
                           "Priestly (P) and non-Priestly (J/E) material, with P providing "
                           "the structural framework (censuses, camp arrangement, priestly "
                           "legislation in chs. 1-10, 15, 17-19, 26-36) and J/E supplying "
                           "the narrative material (chs. 11-14, 16 partially, 20-25). The "
                           "Balaam oracles (chs. 22-24) are often considered among the oldest "
                           "poetry in the Hebrew Bible, possibly dating to the 12th-10th "
                           "century BC based on archaic linguistic features. The 'Book of the "
                           "Wars of the LORD' cited in Numbers 21:14 is a lost source that "
                           "confirms Numbers drew on earlier written traditions. More recent "
                           "scholarship (Levine, Milgrom, Achenbach) recognizes multiple "
                           "redactional layers, with the final form shaped by post-exilic "
                           "Priestly editors who integrated older narrative traditions into "
                           "a theological framework centered on holiness and camp order.",

        "bottom_line": "Numbers is a complex literary work that preserves genuinely ancient "
                       "traditions — the Balaam oracles, the travel itinerary, the Song of "
                       "the Well — within a theological framework that emphasizes the "
                       "consequences of rebellion against YHWH's appointed order. Whether "
                       "Moses wrote the core or later editors shaped the final form, the "
                       "book carries a unified message: the generation that saw God's "
                       "greatest miracles failed through unbelief, and only their children "
                       "would enter the promised land."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "~1406-1405 BC (the final year of the wilderness period, with "
                       "Moses compiling the narrative of the preceding 38 years before "
                       "his death on Mount Nebo)",
        "critical_range": "The traditions in Numbers span a wide chronological range. "
                         "The Balaam oracles (chs. 22-24) may date to the 12th-10th "
                         "century BC based on archaic poetic features (the use of 'el "
                         "rather than 'elohim, parallel structures matching Ugaritic "
                         "poetry). The travel itinerary (ch. 33) may preserve a genuinely "
                         "ancient document. The priestly legislation likely reflects "
                         "pre-exilic cultic practice, while the final redaction of the "
                         "book into its current form is typically dated to the exilic or "
                         "early post-exilic period (~550-450 BC).",
        "evidence": "The Deir Alla inscription (c. 840-760 BC), discovered in 1967 in "
                    "the Jordan Valley, mentions 'Balaam son of Beor' as a 'seer of the "
                    "gods' — an extraordinary extrabiblical confirmation of the Balaam "
                    "tradition in Numbers 22-24. The inscription describes Balaam receiving "
                    "a night vision from the divine council (the shaddayin/gods), closely "
                    "paralleling the biblical account. The earliest physical manuscript "
                    "fragments come from the Dead Sea Scrolls (4QNum-a, 4QNum-b, "
                    "~125-75 BC). The silver scrolls from Ketef Hinnom (c. 600 BC) "
                    "preserve the Priestly Blessing of Numbers 6:24-26, making this the "
                    "oldest known text of any biblical passage."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Israel — specifically the second generation preparing to "
                            "enter Canaan under Joshua. If Mosaic, the immediate audience "
                            "is the generation camped on the Plains of Moab who need to "
                            "learn from their parents' catastrophic failure. If later, the "
                            "audience is any generation of Israel tempted to rebel, murmur, "
                            "or abandon faith in YHWH's promises despite overwhelming "
                            "evidence of his power and faithfulness.",

        "purpose": "Numbers answers the devastating question: Why did the exodus generation "
                   "— the people who saw the plagues, crossed the sea, received the Torah, "
                   "and ate manna from heaven — die in the wilderness without reaching the "
                   "promised land? The answer is unbelief crystallized in rebellion. The "
                   "book serves as a warning narrative: God's patience is real but not "
                   "infinite. He will accomplish his purposes, but those who refuse to "
                   "trust him will be replaced by those who will. The second census (ch. 26) "
                   "makes this concrete — a new generation is counted, ready to inherit what "
                   "their parents forfeited.",

        "theological_intent": "Numbers is structured around two generations and two "
                             "censuses, with the hinge at chapters 13-14 (the spy narrative "
                             "and the forty-year sentence). The first generation (chs. 1-25) "
                             "is characterized by progressive rebellion: complaining about "
                             "food (ch. 11), challenging Moses' authority (ch. 12), refusing "
                             "to enter Canaan (chs. 13-14), challenging the priesthood "
                             "(ch. 16), water complaints (ch. 20), and sexual idolatry "
                             "(ch. 25). Each rebellion escalates in severity and consequence. "
                             "The second generation (chs. 26-36) receives inheritance "
                             "instructions, signaling hope. The theological arc is: "
                             "faithlessness leads to death in the wilderness; faith leads "
                             "to the promised land. This is why Hebrews 3-4 uses Numbers "
                             "as the primary warning text for the church."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) → Aramaic square script (post-exilic)",
        "linguistic_notes": "Numbers contains a striking range of literary forms: census "
                           "lists, itinerary records, legal casuistic prose, narrative, "
                           "archaic poetry (the Balaam oracles, the Song of the Well, the "
                           "fragments from the 'Book of the Wars of the LORD'), and "
                           "liturgical formulas (the Priestly Blessing). The Balaam oracles "
                           "(Num 23-24) display archaic features: the divine name Shaddai, "
                           "verb forms matching Ugaritic and early Hebrew poetry, and "
                           "parallelism structures characteristic of 12th-10th century BC "
                           "Canaanite verse. The prose sections contain both P-style "
                           "legislative language ('according to the command of the LORD "
                           "through Moses') and J/E-style narrative prose. The Song of "
                           "the Well (21:17-18) is a brief but extremely archaic poetic "
                           "fragment. The travel itinerary of chapter 33 uses a distinctive "
                           "formulaic style ('they set out from X and camped at Y') "
                           "paralleled in Egyptian military itineraries.",
        "grammar_match": "The Hebrew of Numbers is consistent with other Torah books. "
                        "The priestly sections match Levitical legislative style. The "
                        "narrative sections share the syntax and vocabulary of Exodus "
                        "and the J/E material in Genesis. The poetic sections (especially "
                        "the Balaam oracles) contain the most archaic Hebrew in the "
                        "Pentateuch, rivaling the Song of the Sea (Exodus 15) and the "
                        "Blessing of Moses (Deuteronomy 33)."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "Numbers IS scripture — it is the narrative backbone of the "
                   "wilderness period and an essential link between the Sinai covenant "
                   "and the Promised Land.",
        "nt_usage": "The New Testament draws heavily on Numbers. Jesus cites the bronze "
                    "serpent as a type of his crucifixion: 'As Moses lifted up the "
                    "serpent in the wilderness, so must the Son of Man be lifted up' "
                    "(John 3:14 → Num 21:8-9). Paul uses the wilderness rebellion as "
                    "a warning: 'These things happened to them as examples and were "
                    "written down for our instruction' (1 Cor 10:1-11 → Num 11, 14, "
                    "16, 21, 25). Hebrews 3-4 builds its entire argument about "
                    "perseverance on the Numbers 13-14 spy narrative: 'They were unable "
                    "to enter because of unbelief' (Heb 3:19). Jude cites Korah's "
                    "rebellion (Jude 11 → Num 16), Balaam's error (Jude 11 → Num 22-24), "
                    "and the wilderness murmurers (Jude 5 → Num 14). Peter references "
                    "Balaam's donkey (2 Peter 2:15-16 → Num 22). Revelation 2:14 "
                    "references 'the teaching of Balaam' (→ Num 25, 31:16).",
        "internal_consistency": "Numbers continues seamlessly from Leviticus (the "
                               "Sinai legislation) and sets up Deuteronomy (Moses' "
                               "farewell speeches on the Plains of Moab). The first "
                               "census (Num 1) follows the tabernacle consecration "
                               "(Lev 8-9). The camp arrangement (Num 2) implements the "
                               "holiness theology of Leviticus. The travel itinerary "
                               "(Num 33) corresponds to Exodus-Numbers waypoints. The "
                               "inheritance laws (Num 27, 36) prepare for the conquest "
                               "narrated in Joshua. The transition from Moses to Joshua "
                               "(Num 27:18-23) is confirmed in Deuteronomy 31 and "
                               "Joshua 1."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "The silver scrolls from Ketef Hinnom (KH1 and KH2, c. 600 BC) "
                    "preserve Numbers 6:24-26 (the Priestly Blessing) and represent "
                    "the oldest known text of any biblical passage — predating the "
                    "Dead Sea Scrolls by 400 years. 4QNum-a (~125-75 BC) is the most "
                    "substantial Qumran manuscript of Numbers.",
        "major_witnesses": [
            {"name": "Ketef Hinnom Silver Scrolls", "date": "c. 600 BC",
             "note": "Two tiny silver amulets bearing Numbers 6:24-26 (the Priestly "
                     "Blessing), discovered in 1979 in a burial cave near Jerusalem. "
                     "The oldest known text of any biblical passage, predating even "
                     "the earliest DSS by four centuries."},
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. Numbers in MT is generally well-preserved, "
                     "with some textual difficulties in the travel itinerary (ch. 33) "
                     "and the Balaam oracles."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The Greek translation of Numbers shows significant differences "
                     "from MT in several passages: the order of tribal offerings in "
                     "chapter 7 varies, and some census figures differ. LXX Numbers "
                     "is an important witness to a pre-Masoretic Hebrew text."},
            {"name": "Samaritan Pentateuch (SP)", "date": "Pre-2nd century BC tradition",
             "note": "The Samaritan text of Numbers contains its most significant "
                     "divergence from MT in the camp arrangement and census lists. SP "
                     "also adds Deuteronomy-style expansions in several places."},
            {"name": "Dead Sea Scrolls", "date": "~125 BC - 68 AD",
             "note": "4QNum-a (4Q27) is the primary witness, preserving portions of "
                     "Numbers 1-36. It sometimes agrees with SP against MT (especially "
                     "in expanded readings) and sometimes with LXX, demonstrating "
                     "textual plurality in the Second Temple period."},
            {"name": "Targumim", "date": "1st century BC onward",
             "note": "Targum Onkelos renders Numbers fairly literally. Targum "
                     "Pseudo-Jonathan adds extensive interpretive material, especially "
                     "in the Balaam oracles (identifying the 'star from Jacob' with "
                     "the Messiah) and the rebellion narratives."}
        ],
        "reliability": "Numbers is well-attested across all textual traditions. The "
                       "Ketef Hinnom scrolls provide extraordinary early evidence for "
                       "the Priestly Blessing. The DSS, LXX, SP, and MT substantially "
                       "agree on narrative content, with differences primarily in census "
                       "numbers and the order of lists. The theological message is "
                       "consistent across all witnesses."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "Numbers spans approximately 38 years, from the second year after "
                   "the exodus (Num 1:1, the second month of the second year) to the "
                   "fortieth year (Num 33:38, Aaron's death). The bulk of the narrative "
                   "covers the departure from Sinai (ch. 10), the catastrophic spy "
                   "mission (chs. 13-14), the subsequent 38 years of wandering (largely "
                   "summarized, not narrated), and the final approach to Canaan from "
                   "the east via the Transjordan (chs. 20-36).",

        "geography": "The action moves from Sinai northward to Kadesh-barnea (the "
                     "staging ground for the failed invasion, ch. 13), then through "
                     "38 years of wilderness wandering in the Negev and Arabah, and "
                     "finally east through Edom and Moab to the Plains of Moab opposite "
                     "Jericho (ch. 22-36). Key sites: Mount Sinai, Kibroth-hattaavah, "
                     "Hazeroth, Kadesh-barnea, the Arabah, Mount Hor (Aaron's death), "
                     "the King's Highway, the Arnon River, Heshbon, the Plains of Moab, "
                     "and Mount Nebo/Pisgah. The Transjordan territory (Gilead, Bashan) "
                     "becomes critical in chapters 32-36.",

        "historical_connections": "The Deir Alla inscription (c. 840-760 BC), discovered "
                                 "in the Jordan Valley, provides extrabiblical attestation "
                                 "of Balaam son of Beor as a seer associated with the divine "
                                 "council — a remarkable confirmation of the Numbers 22-24 "
                                 "tradition. Egyptian records from the reigns of Thutmose III, "
                                 "Amenhotep II, and Ramesses II describe military campaigns "
                                 "through the same Transjordan territory traversed in Numbers "
                                 "20-21. The Mesha Stele (c. 840 BC) references Israelite "
                                 "occupation of Transjordan lands first claimed in Numbers 21 "
                                 "and 32. The Amorite kingdoms of Sihon (Heshbon) and Og "
                                 "(Bashan), defeated in Numbers 21, left archaeological "
                                 "traces consistent with Late Bronze Age urbanization in the "
                                 "region."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "high",
        "summary": "Numbers contains some of the most vivid divine council material "
                   "in the Torah. Key passages: (1) The Camp Arrangement (Num 2) — "
                   "Israel's camp in a cross pattern around the tabernacle mirrors "
                   "the heavenly court, with God's throne at the center surrounded by "
                   "concentric rings of holy beings (Levites as the inner ring, tribes "
                   "as the outer). (2) The Priestly Blessing (Num 6:24-26) — invoking "
                   "YHWH's face/panim, the same kavod-presence that fills the divine "
                   "throne room. (3) The Nephilim Report (Num 13:33) — the ONLY other "
                   "OT use of 'Nephilim' besides Genesis 6:4; the Anakim are remnants "
                   "of the giant clans tied to the divine council rebellion. (4) Korah's "
                   "Rebellion (Num 16) — the earth opens to swallow rebels who challenge "
                   "the divinely established mediatorial order, a direct divine council "
                   "judgment. (5) The Bronze Serpent (Num 21:4-9) — YHWH sends seraphim "
                   "(nachash saraph, 'fiery serpents' — the same word used for the "
                   "throne beings of Isaiah 6), and Moses makes a nachash nechoshet "
                   "(bronze serpent/shining one); Jesus identifies this as a type of "
                   "his crucifixion (John 3:14), connecting it to the nachash of "
                   "Genesis 3. (6) Balaam (Num 22-24) — a pagan diviner with genuine "
                   "access to the divine realm; his donkey sees the Angel of YHWH "
                   "before he does; his Star Prophecy (24:17) is one of the most "
                   "important messianic texts, cited extensively at Qumran. (7) Baal-Peor "
                   "(Num 25) — Israel yokes itself to a territorial 'elohim of Moab, "
                   "the exact Deuteronomy 32:8 scenario of allotted gods seducing "
                   "Israel away from YHWH.",

        "key_heiser_refs": [
            "The Unseen Realm, chapters 14-15 (giant clans, Nephilim, the conquest)",
            "The Unseen Realm, chapter 23 (the nachash/seraphim/bronze serpent connection)",
            "The Unseen Realm, chapter 29 (Balaam and the divine council)",
            "Supernatural, chapters 10-12 (Nephilim and the giant clans in Canaan)",
            "Reversing Hermon, chapter 6 (Balaam and the Star Prophecy at Qumran)",
            "The Naked Bible Podcast, Episode 109 (Numbers 22-24, Balaam and divine access)"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "Numbers Is a Warning Narrative",
            "body": "Numbers is the most theologically sobering book of the Torah. "
                    "It records the greatest tragedy in Israel's history: the generation "
                    "that witnessed God's most spectacular miracles — the plagues, the "
                    "sea crossing, the fire on Sinai, the daily manna — collectively "
                    "refused to trust him and died in the wilderness. Hebrews 3:7-4:11 "
                    "uses this as the primary warning for the church: 'Today, if you "
                    "hear his voice, do not harden your hearts as in the rebellion.' "
                    "The book is not merely ancient history — it is a mirror held up "
                    "to every community of faith that has seen God work and is tempted "
                    "to stop trusting."
        },
        {
            "type": "scholarship",
            "title": "Structure and Unity",
            "body": "Numbers has long been considered the most disorganized book of the "
                    "Torah — a seemingly random collection of narratives, laws, and "
                    "lists. Dennis Olson's 'The Death of the Old and the Birth of the "
                    "New' (1985) revolutionized Numbers scholarship by identifying the "
                    "two censuses (chs. 1 and 26) as the structural skeleton: the first "
                    "census counts the exodus generation that will die, and the second "
                    "counts the new generation that will inherit. Everything between is "
                    "the story of how the first generation forfeited the promise. This "
                    "two-generation structure provides a coherent theological framework "
                    "for the entire book."
        },
        {
            "type": "interpretation",
            "title": "The Nephilim and the Giant Clans",
            "body": "Numbers 13:33 is the only use of 'Nephilim' in the OT outside "
                    "Genesis 6:4. The spies report that the Anakim in Canaan are "
                    "'from the Nephilim.' In the divine council framework (Heiser, "
                    "Unseen Realm chs. 14-15), the post-flood giant clans (Anakim, "
                    "Rephaim, Emim, Zamzummim) are remnants of the pre-flood Nephilim "
                    "tradition — the offspring of the divine-human union of Genesis 6. "
                    "Their presence in Canaan is not incidental: the land is occupied "
                    "by beings connected to the rebellious divine council members. The "
                    "conquest of Canaan (Joshua) is thus not merely political but "
                    "spiritual warfare — reclaiming territory held by the seed of the "
                    "serpent. The spies' fear of the Nephilim is both military cowardice "
                    "and theological failure: they forgot that YHWH, the Most High who "
                    "commands the divine council, had promised them the land."
        }
    ]
}
