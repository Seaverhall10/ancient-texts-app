"""
info.py -- 1 Corinthians: Scholarly Text Introduction

Paul's longest and most varied letter, written to a fractured church in Corinth
around 53-55 AD. The letter addresses everything from factionalism and sexual
immorality to spiritual gifts and the resurrection. For the divine council
framework, 1 Corinthians is critical: Paul speaks of "rulers of this age" who
crucified Christ unknowingly (2:6-8), saints who will judge angels (6:2-3),
sacrifices offered to demons/daimonia (10:20), head coverings "because of the
angels" (11:10), and Christ destroying every rule, authority, and power at
the end (15:24-28). This letter reveals how the early church understood its
cosmic role in the war against the hostile spiritual powers.
"""

TEXT_INFO = {
    "text_id": "1corinthians",
    "display_name": "1 Corinthians",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Pauline Epistles",
        "detail": "1 Corinthians is universally accepted as an authentic letter of the Apostle Paul. "
                  "It is attested by Clement of Rome (1 Clement, c. 96 AD), who explicitly references "
                  "this letter to the Corinthians. Ignatius, Polycarp, and the Muratorian Canon all "
                  "affirm its Pauline authorship. No serious scholar, conservative or critical, has "
                  "ever disputed that Paul wrote 1 Corinthians. It is one of the 'undisputed Paulines' "
                  "alongside Romans, 2 Corinthians, Galatians, Philippians, 1 Thessalonians, and "
                  "Philemon. The letter is quoted or alluded to by virtually every major early church "
                  "father. Its canonical status was never questioned."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Paul the Apostle, writing from Ephesus during his third missionary journey "
                       "(Acts 19:1-20:1). Paul identifies himself and Sosthenes as co-senders (1:1). "
                       "He mentions his plans to visit Corinth via Macedonia (16:5-9) and states that "
                       "he will remain in Ephesus until Pentecost (16:8). He references sending Timothy "
                       "ahead (4:17; 16:10) and notes that 'the household of Chloe' informed him of the "
                       "Corinthian divisions (1:11). He also responds to a letter the Corinthians sent "
                       "him (7:1, 'Now concerning the matters about which you wrote').",

        "scholarly_debate": "There is virtually no debate about Pauline authorship. The only scholarly "
                           "discussion concerns the letter's unity: some scholars (e.g., Walter Schmithals) "
                           "have proposed that 1 Corinthians is a composite of two or more letters stitched "
                           "together, based on apparent topic shifts and the reference to a 'previous letter' "
                           "in 5:9. However, most scholars (Gordon Fee, Anthony Thiselton, Raymond Collins) "
                           "defend the letter's integrity, noting that ancient letters frequently addressed "
                           "multiple topics and that Paul's rhetorical structure accounts for the transitions.",

        "bottom_line": "Paul wrote 1 Corinthians from Ephesus around 53-55 AD, addressing specific "
                       "problems reported to him by Chloe's household and questions the Corinthians had "
                       "sent in a letter. This is one of the most securely attributed documents in the "
                       "entire New Testament."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Written from Ephesus during Paul's third missionary journey, approximately "
                       "53-55 AD. Acts 18:1-18 records Paul's initial 18-month stay in Corinth, and "
                       "1 Corinthians was written during the subsequent Ephesian ministry (Acts 19).",
        "critical_range": "The date is remarkably secure: 53-55 AD. The Gallio inscription from Delphi "
                         "fixes Paul's appearance before Gallio in Corinth (Acts 18:12-17) to approximately "
                         "51-52 AD. Paul left Corinth shortly after, traveled to Ephesus, and wrote "
                         "1 Corinthians from there within a few years. This places the letter firmly in "
                         "the mid-50s, making it one of the earliest NT documents.",
        "evidence": "Key evidence includes: (1) The Gallio inscription (SIG 801D) dates Gallio's "
                    "proconsulship to 51-52 AD, anchoring Paul's Corinthian chronology. (2) Paul's "
                    "reference to remaining in Ephesus 'until Pentecost' (16:8) implies a spring "
                    "composition. (3) The collection for Jerusalem (16:1-4) corresponds to the project "
                    "Paul describes in Romans 15:25-28 and 2 Corinthians 8-9. (4) The letter presupposes "
                    "the Corinthian church has been established long enough for factions, lawsuits, and "
                    "doctrinal disputes to develop -- consistent with 2-3 years after Paul's founding visit."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The church at Corinth -- a mixed community of Jewish and Gentile converts "
                            "in one of the most cosmopolitan cities of the Roman Empire. Ancient Corinth "
                            "was a Roman colony refounded by Julius Caesar in 44 BC, located on the narrow "
                            "isthmus connecting mainland Greece and the Peloponnese. It was a commercial "
                            "hub with two ports (Lechaion on the west, Cenchreae on the east), a center "
                            "for the Isthmian Games, and notorious for its sexual permissiveness. The "
                            "temple of Aphrodite on the Acrocorinth was a symbol of the city's moral "
                            "landscape. The congregation included people of diverse social status: wealthy "
                            "patrons like Gaius (Rom 16:23), lower-class laborers, and slaves.",

        "purpose": "Paul wrote to address multiple crises: (1) Factionalism -- groups claiming allegiance "
                   "to Paul, Apollos, Cephas, or Christ (1:10-17). (2) Sexual immorality -- including "
                   "a man living with his father's wife (5:1-13). (3) Lawsuits among believers (6:1-11). "
                   "(4) Questions about marriage and celibacy (ch. 7). (5) Idol food and temple meals "
                   "(chs. 8-10). (6) Head coverings and worship order (11:2-16). (7) Abuse of the Lord's "
                   "Supper (11:17-34). (8) Spiritual gifts and their proper use (chs. 12-14). (9) Denial "
                   "of bodily resurrection (ch. 15). (10) The collection for Jerusalem (ch. 16).",

        "theological_intent": "Beneath the diverse topics, Paul's overarching argument is that the "
                             "Corinthians have failed to grasp the cross as the governing paradigm for "
                             "all of life. The 'wisdom of this age' (sophia tou aionos toutou) exalts "
                             "human power, eloquence, and social status, but God's wisdom operates through "
                             "apparent weakness (1:18-2:16). The 'rulers of this age' (archontes tou aionos "
                             "toutou) who crucified the Lord of glory did so because they could not "
                             "comprehend the wisdom of God hidden in a mystery (2:7-8). Paul's ethic is "
                             "cruciform: the cross reshapes how believers relate to power, sexuality, "
                             "worship, spiritual gifts, and even death itself."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script (earliest manuscripts)",
        "linguistic_notes": "Paul's Greek in 1 Corinthians is vigorous, rhetorically sophisticated, and "
                           "at times deliberately unpolished. He uses diatribe style (imagined interlocutors, "
                           "rhetorical questions), Stoic-Cynic argumentative patterns, and repeated use of "
                           "the formula 'peri de' ('now concerning,' 7:1, 25; 8:1; 12:1; 16:1, 12) to "
                           "transition between topics the Corinthians raised. Key Greek terms include: "
                           "sophia (wisdom), dynamis (power), pneumatikos (spiritual/spiritual person), "
                           "psychikos (natural/soulish person), sarx (flesh), soma (body), charisma "
                           "(grace-gift), agape (love, ch. 13), and the critical christological title "
                           "Kyrios (Lord). Paul's use of archontes tou aionos toutou (rulers of this age, "
                           "2:6, 8) is a key phrase for divine council studies, debated as referring to "
                           "either human rulers, spiritual powers, or both.",
        "grammar_match": "Paul's syntax can be dense and parenthetical, with long sentences that pile up "
                        "subordinate clauses (e.g., 1:26-31). He occasionally breaks grammatical structure "
                        "in passionate outbursts. His rhetorical questions are frequent and pointed: 'Do "
                        "you not know?' (ouk oidate) appears ten times (3:16; 5:6; 6:2, 3, 9, 15, 16, 19; "
                        "9:13, 24). The letter shows evidence of Pauline dictation with possible scribal "
                        "assistance (16:21, 'I, Paul, write this greeting with my own hand')."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "1 Corinthians is apostolic scripture that profoundly shapes NT theology on the "
                   "resurrection (ch. 15), spiritual gifts (chs. 12-14), the Lord's Supper (11:23-26), "
                   "love (ch. 13), and the cosmic scope of Christ's victory over all powers (15:24-28).",
        "nt_usage": "1 Corinthians contains the earliest written account of the Lord's Supper tradition "
                    "(11:23-26, 'I received from the Lord what I also delivered to you') and the earliest "
                    "written testimony of the resurrection appearances (15:3-8). Paul quotes or alludes to "
                    "the Old Testament frequently: Isaiah 29:14 (1:19), Isaiah 64:4 (2:9), Psalm 94:11 "
                    "(3:20), Deuteronomy 25:4 (9:9), Isaiah 22:13 (15:32), Hosea 13:14 (15:55), Genesis "
                    "2:24 (6:16), Exodus 32:6 (10:7). He also cites an early creedal formula in 15:3-5 "
                    "that predates his letter by at least 20 years.",
        "internal_consistency": "The letter coheres with Acts 18 (founding of the Corinthian church), "
                               "Romans 16:23 (Gaius and Erastus in Corinth), and 2 Corinthians (Paul's "
                               "follow-up). The theological themes -- cruciform wisdom, bodily resurrection, "
                               "the body of Christ, and the defeat of cosmic powers -- connect seamlessly to "
                               "Paul's other letters, especially Romans 8:38-39, Colossians 2:15, and "
                               "Ephesians 1:20-23."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "P46 (Chester Beatty Papyrus II, c. 175-225 AD) contains 1 Corinthians with minor "
                    "lacunae. P15 (3rd century) preserves fragments of chapters 7-8. P11 (7th century) "
                    "covers portions of chapters 1-7.",
        "major_witnesses": [
            {"name": "P46", "date": "c. 175-225 AD",
             "note": "The earliest substantial witness to 1 Corinthians. Part of a codex containing "
                     "most of Paul's letters. Some readings differ from later manuscripts but the "
                     "text is largely stable."},
            {"name": "Codex Sinaiticus (Aleph)", "date": "c. 330-360 AD",
             "note": "Complete text of 1 Corinthians. One of the most important uncial manuscripts."},
            {"name": "Codex Vaticanus (B)", "date": "c. 300-325 AD",
             "note": "Complete text. Generally considered the most reliable single manuscript."},
            {"name": "Codex Alexandrinus (A)", "date": "c. 400-440 AD",
             "note": "Complete text with minor variants. Represents the Byzantine text tradition."}
        ],
        "reliability": "The text of 1 Corinthians is well-attested and stable. The most significant "
                       "textual variant is the placement of 14:34-35 (women keeping silent in church), "
                       "which some manuscripts (D, F, G) relocate to after 14:40, leading some scholars "
                       "to suggest it is a later interpolation. The majority of scholars retain the verses "
                       "in their traditional position while debating their interpretation."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Roman Corinth was refounded as a Roman colony (Colonia Laus Iulia Corinthiensis) by "
                   "Julius Caesar in 44 BC after being destroyed by the Roman general Lucius Mummius in "
                   "146 BC. By Paul's time, it was the capital of the Roman province of Achaia, governed "
                   "by a proconsul. The city sat on the narrow Corinthian isthmus, controlling east-west "
                   "trade routes. Its population was diverse: Roman freedmen, Greek-speaking residents, "
                   "Jews (Acts 18:4 mentions a synagogue), and immigrants from across the Mediterranean.",

        "geography": "Corinth controlled two ports: Lechaion (Gulf of Corinth, western) and Cenchreae "
                     "(Saronic Gulf, eastern). Ships were dragged across the diolkos (stone trackway) "
                     "to avoid the dangerous voyage around the Peloponnese. The Acrocorinth, a massive "
                     "limestone hill (575m), towered over the city and held the temple of Aphrodite. "
                     "The city's agora, temples, and shops have been extensively excavated.",

        "historical_connections": "The Gallio inscription (discovered at Delphi, 1905) dates Gallio's "
                                 "proconsulship to 51-52 AD, providing the most precise chronological "
                                 "anchor for Paul's ministry. The Erastus inscription found in Corinth "
                                 "('Erastus, in return for his aedileship, laid this pavement at his own "
                                 "expense') may refer to the Erastus mentioned by Paul in Romans 16:23 "
                                 "as the city's oikonomos (treasurer/manager). The Isthmian Games, held "
                                 "near Corinth every two years, provide context for Paul's athletic "
                                 "metaphors (9:24-27)."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "high",
        "summary": "1 Corinthians is one of the most important NT letters for divine council theology. "
                   "Paul explicitly references spiritual powers and their role in the crucifixion, the "
                   "future judgment of angels by believers, sacrifices to demons, angelic observation of "
                   "worship, and Christ's final destruction of all cosmic powers."
                   "\n\n"
                   "The 'rulers of this age' (archontes tou aionos toutou, 2:6-8) who crucified the Lord "
                   "of glory are best understood as including both human and spiritual powers. The term "
                   "archontes can refer to human rulers (as in Rom 13:3), but Paul's language of 'this age' "
                   "(aion houtos) and 'a wisdom not of this age' (2:6) suggests a cosmic dimension. Michael "
                   "Heiser argues these are the same hostile spiritual powers who rule the nations under the "
                   "Deuteronomy 32 allotment -- they orchestrated the crucifixion not understanding that it "
                   "would be the very means of their defeat. Had they known God's secret wisdom, 'they would "
                   "not have crucified the Lord of glory' (2:8)."
                   "\n\n"
                   "The statement that believers 'will judge angels' (6:2-3) is a direct reversal of the "
                   "divine council hierarchy. In Psalm 82, God judges the corrupt elohim; Paul declares "
                   "that redeemed humanity will participate in that judgment. This fulfills the original "
                   "design: humans, made as God's imagers (Gen 1:26-28), will ultimately be elevated above "
                   "the angelic beings who rebelled."
                   "\n\n"
                   "Paul's identification of pagan sacrifice as sacrifice 'to demons' (daimonia, 10:20) "
                   "draws directly on Deuteronomy 32:17 (LXX: daimoniois, 'to demons'). The territorial "
                   "gods of the nations are real spiritual beings, and worship directed to them empowers "
                   "the demonic realm. Paul does not deny the reality of these beings but denies their "
                   "legitimacy as objects of worship."
                   "\n\n"
                   "The head covering instruction 'because of the angels' (11:10) reflects the Watcher "
                   "tradition: the awareness that angels observe human worship and that the boundary between "
                   "human and angelic must be maintained. Whether this references the Watcher story directly "
                   "(Gen 6:1-4; 1 Enoch 6-16) or the broader concept of angelic observation of the "
                   "worshipping community, Paul assumes his audience knows the tradition."
                   "\n\n"
                   "The climax comes in 15:24-28: Christ 'destroys every rule (arche) and every authority "
                   "(exousia) and power (dynamis).' The same vocabulary used for spiritual powers in "
                   "Ephesians 6:12 and Colossians 2:15 appears here in the eschatological destruction "
                   "sequence. The last enemy is death itself (15:26). Christ's reign continues until every "
                   "hostile power is placed under his feet -- language drawn from Psalm 110:1, the divine "
                   "council enthronement psalm. Then the Son himself submits to the Father, 'that God may "
                   "be all in all' (15:28).",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 35 (rulers of this age and the crucifixion)",
            "The Unseen Realm, chapter 37 (judging angels -- Psalm 82 reversal)",
            "The Unseen Realm, chapter 14 (Deuteronomy 32:17 -- sacrifices to demons)",
            "Supernatural, chapter 20 (the cosmic scope of Christ's victory)",
            "Angels: What the Bible Really Says, ch. 12 (because of the angels -- 1 Cor 11:10)",
            "The Naked Bible Podcast, episode 117 (1 Cor 2:6-8 and the archontes)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Archontes -- Human Rulers or Spiritual Powers?",
            "body": "The identity of the 'rulers of this age' (archontes tou aionos toutou) in 2:6-8 is "
                    "one of the most debated questions in Pauline studies. Three positions exist: (1) Human "
                    "rulers only -- Pontius Pilate, Herod, the Jewish Sanhedrin, etc. This reads archontes "
                    "in its common political sense (cf. Acts 4:26, citing Psalm 2). (2) Spiritual powers "
                    "only -- the demonic beings behind the political powers, who manipulated human agents "
                    "to crucify Christ. This interpretation was dominant among the early church fathers "
                    "(Origen, Marcion, the Ascension of Isaiah). (3) Both -- a 'dual reference' in which "
                    "Paul intentionally uses language that encompasses both human and spiritual powers, "
                    "recognizing that in the ancient worldview, political authority and spiritual authority "
                    "were inseparable. Heiser and most divine council scholars favor option 3: the spiritual "
                    "powers who govern the nations (Deut 32:8-9; Dan 10:13, 20-21; Ps 82) acted through "
                    "human rulers to crucify Christ. The phrase 'Lord of glory' (2:8) is a divine title "
                    "(cf. 1 Enoch 22:14; 25:3; 27:3-5; Psalm 24:7-10), making the archontes' ignorance "
                    "all the more profound: they killed their own sovereign."
        },
        {
            "type": "context",
            "title": "Because of the Angels -- The Watcher Connection",
            "body": "Paul's instruction that women should have 'authority' (exousia) on their heads 'because "
                    "of the angels' (dia tous angelous, 11:10) has puzzled interpreters for centuries. The "
                    "most likely background is the Second Temple Watcher tradition. In 1 Enoch 6-16, the "
                    "Watchers (a class of angels) were drawn to human women by their beauty and 'fell' by "
                    "crossing the boundary between divine and human realms (Gen 6:1-4). Paul's concern is "
                    "boundary maintenance in worship: the worshipping assembly is a space where heaven and "
                    "earth overlap, where angels are present (cf. Qumran's War Scroll, which requires "
                    "purity 'because the holy angels are in your midst'). The head covering serves as a "
                    "marker of proper order -- not subordination but identity and boundary. Whether Paul "
                    "feared literal angelic temptation or used the tradition symbolically to reinforce "
                    "worship propriety, the Watcher tradition is the key to unlocking this verse."
        },
        {
            "type": "interpretation",
            "title": "Judging Angels -- The Great Reversal",
            "body": "Paul's almost offhand remark that believers 'will judge angels' (6:2-3) is extraordinary. "
                    "In Psalm 82, YHWH judges the corrupt members of his divine council -- the elohim who "
                    "failed to govern the nations justly. Paul announces that redeemed humans will participate "
                    "in this judgment. This is the ultimate reversal of the cosmic hierarchy: humans, who "
                    "were made 'a little lower than the elohim' (Psalm 8:5), who were placed under angelic "
                    "beings in the Deuteronomy 32 allotment, will ultimately judge those same beings. The "
                    "theological logic runs: if believers are united to Christ (who is exalted above all "
                    "powers, Eph 1:20-23), they share in his authority. Paul uses this cosmic reality to "
                    "shame the Corinthians for taking petty disputes to pagan courts: 'If you are going to "
                    "judge angels, can you not handle trivial matters?'"
        },
        {
            "type": "scholarship",
            "title": "The Resurrection and Cosmic Powers (1 Cor 15)",
            "body": "1 Corinthians 15 is the most sustained argument for bodily resurrection in the entire "
                    "Bible. Some Corinthians were denying the future resurrection of the body (15:12), likely "
                    "influenced by Greek dualism that disdained the physical. Paul responds with an argument "
                    "that moves from historical testimony (15:1-11) to logical necessity (15:12-19) to cosmic "
                    "scope (15:20-28) to the nature of the resurrection body (15:35-58). The divine council "
                    "dimension appears in 15:24-28: Christ's resurrection initiates a process that will "
                    "culminate in the destruction of 'every rule (arche) and every authority (exousia) and "
                    "power (dynamis).' These are the same cosmic powers Paul references throughout his "
                    "letters (Rom 8:38; Eph 1:21; 3:10; 6:12; Col 1:16; 2:15). The final enemy, death "
                    "itself, is personified as a power to be destroyed. Paul quotes Psalm 110:1 ('he must "
                    "reign until he has put all his enemies under his feet') -- the divine council "
                    "enthronement psalm -- and Psalm 8:6 ('he has put all things under his feet'), linking "
                    "the resurrection to the original human mandate to rule creation."
        }
    ]
}
