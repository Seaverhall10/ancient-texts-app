"""
info.py -- Romans: Scholarly Text Introduction

This file provides the "front page" for Romans in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Romans is THE cosmic gospel of the New Testament. It is Paul's most
systematic and comprehensive theological statement, tracing the arc of
redemption from universal human guilt (1:18-3:20), through justification
by faith (3:21-5:21), into union with Christ in death and resurrection
(6:1-8:39), through the mystery of Israel and the nations (9:1-11:36),
and into the practical life of the redeemed community (12:1-16:27).

The divine council framework pervades the letter: the nations "given over"
by God (1:24, 26, 28) echo the Deuteronomy 32:8-9 allotment of the nations
to the sons of God. Creation groans for liberation (8:18-25) -- the entire
cosmos awaits the reversal of the cosmic rebellion. Neither "angels, nor
rulers, nor things present, nor things to come, nor powers" (8:38-39)
can separate believers from God's love -- Paul names the council members
and declares them powerless. The olive tree allegory (11:17-24) depicts
the reunification of Israel and the nations under one root. And the
closing promise -- "the God of peace will soon crush Satan under your
feet" (16:20) -- is the fulfillment of Genesis 3:15, the protoevangelium.
"""

TEXT_INFO = {
    "text_id": "romans",
    "display_name": "Romans",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Pauline Epistles",
        "detail": "Romans is universally canonical across all Christian traditions -- Roman Catholic, "
                  "Eastern Orthodox, and Protestant. It has been considered the most important theological "
                  "document in the New Testament from the earliest centuries. Every major reform and "
                  "revival in Christian history has been catalyzed by Romans: Augustine's conversion in "
                  "the garden (387 AD) was triggered by reading Romans 13:13-14. Martin Luther's "
                  "Reformation (1517) was born from his study of Romans 1:17 ('the righteous shall live "
                  "by faith'). John Wesley's Aldersgate experience (1738), which launched the Methodist "
                  "movement, came while listening to Luther's preface to Romans. Karl Barth's commentary "
                  "on Romans (1919) inaugurated neo-orthodox theology and changed 20th-century "
                  "Christianity. The letter appears in every ancient canon list: the Muratorian Fragment "
                  "(c. 170 AD), Marcion's Apostolikon (c. 140 AD), Irenaeus (c. 180 AD), and all "
                  "subsequent witnesses. Chrysostom had Romans read to him every week. Calvin considered "
                  "it 'the most important piece in the New Testament' and 'a door and a gateway into the "
                  "whole of Scripture.' Luther called it 'the most important part of the New Testament and "
                  "the very purest Gospel.'"
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Paul identifies himself as the author (1:1) and provides extensive biographical "
                       "detail: his apostleship to the Gentiles (1:5; 11:13; 15:15-19), his planned "
                       "itinerary (15:22-29 -- delivering the collection to Jerusalem, then visiting Rome "
                       "en route to Spain), and his personal greetings to over 25 named individuals in "
                       "chapter 16. Tertius, Paul's amanuensis (secretary), identifies himself in 16:22: "
                       "'I, Tertius, who wrote this letter, greet you in the Lord.' Pauline authorship of "
                       "Romans has never been seriously questioned by any scholar -- it is the undisputed "
                       "cornerstone of the Pauline corpus.",

        "scholarly_debate": "The authorship of Romans itself is not debated. However, two textual issues are "
                           "discussed: (1) Chapter 16 -- some scholars have argued that Romans 16, with its "
                           "extensive list of greetings, was originally a separate letter to Ephesus (where Paul "
                           "had spent three years and would know many people) rather than to Rome (which he had "
                           "not visited). However, the manuscript evidence overwhelmingly supports chapter 16 as "
                           "original to Romans. The list of names in Rome is explained by the mobility of the "
                           "early church. (2) The doxology of 16:25-27 -- in some manuscripts (P46), this "
                           "doxology appears after 15:33, and in others after 14:23, suggesting textual fluidity "
                           "at the letter's end. Some scholars attribute this to Marcion's shortened version of "
                           "Romans (14 chapters).",

        "bottom_line": "Paul wrote Romans from Corinth (cf. the commendation of Phoebe from Cenchreae, "
                       "16:1) during his third missionary journey, c. 56-58 AD, dictating to Tertius. It is "
                       "the most carefully composed of Paul's letters -- not a response to a crisis (like "
                       "Galatians or Corinthians) but a systematic presentation of his gospel, written as he "
                       "prepared to visit Rome for the first time and to seek support for his mission to Spain."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "c. 56-58 AD, written from Corinth during Paul's three-month stay in Greece "
                       "(Acts 20:2-3) on his third missionary journey, before his final journey to "
                       "Jerusalem with the collection for the saints (Rom 15:25-28).",
        "critical_range": "The virtually unanimous scholarly consensus dates Romans to c. 55-58 AD. The "
                         "letter's mention of the collection for Jerusalem (15:25-28), Paul's plan to visit "
                         "Rome and then Spain (15:23-24), and the commendation of Phoebe from Cenchreae "
                         "(the eastern port of Corinth, 16:1) all point to composition during the Corinthian "
                         "stay of Acts 20:2-3.",
        "evidence": "Key evidence includes: (1) The synchronism with Acts 20:2-3 (Paul's three months in "
                    "Greece). (2) The collection for Jerusalem (Rom 15:25-28; cf. 1 Cor 16:1-4; 2 Cor 8-9; "
                    "Acts 24:17). (3) Phoebe from Cenchreae (16:1) as the likely letter carrier, placing "
                    "composition near Corinth. (4) Gaius (16:23), identified with the Gaius of Corinth "
                    "(1 Cor 1:14). (5) Erastus, the city treasurer (16:23), possibly identified with the "
                    "Erastus named in a Latin inscription found at Corinth: 'Erastus, in return for his "
                    "aedileship, laid this pavement at his own expense.' (6) The theological relationship "
                    "with Galatians (written earlier from Antioch or Ephesus) -- Romans develops and "
                    "systematizes the justification-by-faith argument of Galatians in a more irenic tone."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The letter is addressed 'to all those in Rome who are loved by God and called "
                            "to be saints' (1:7). The Roman church was not founded by Paul -- it likely arose "
                            "from Jewish believers returning from Jerusalem after Pentecost (Acts 2:10 lists "
                            "'visitors from Rome, both Jews and proselytes'). The church was originally Jewish "
                            "but became predominantly Gentile after the Emperor Claudius expelled Jews from "
                            "Rome in 49 AD (Acts 18:2; Suetonius, Claudius 25.4). When Jews returned after "
                            "Claudius's death (54 AD), the church was now majority Gentile, creating the "
                            "Jew-Gentile tension that pervades the letter (especially chapters 9-11 and 14-15). "
                            "The Roman church met in multiple house churches (16:5, 14, 15), not a single "
                            "congregation, adding to the diversity and potential for division.",

        "purpose": "Romans serves multiple purposes: (1) Self-introduction -- Paul is preparing to visit "
                   "Rome for the first time and presents his gospel so they will support his Spanish mission "
                   "(15:22-24). (2) Theological exposition -- a comprehensive statement of his understanding "
                   "of the gospel, addressing the universal human predicament (1:18-3:20), justification by "
                   "faith (3:21-5:21), sanctification and freedom from sin (6:1-8:39), Israel's place in "
                   "God's plan (9:1-11:36), and practical Christian living (12:1-15:13). (3) Pastoral "
                   "mediation -- addressing the tension between Jewish and Gentile believers over Torah "
                   "observance, food laws, and holy days (14:1-15:13). (4) Theological apologetic -- defending "
                   "his gospel against Jewish objections: if justification is by faith, what advantage does "
                   "Israel have? Has God's word failed? Is faith a license for sin? These questions structure "
                   "much of the argument.",

        "theological_intent": "Romans presents the most comprehensive soteriology (doctrine of salvation) in "
                             "the New Testament, set within the cosmic framework of the Deuteronomy 32 "
                             "worldview. The letter traces a cosmic arc: (1) The problem is universal -- all "
                             "humanity, both Gentile and Jew, stands guilty before God (1:18-3:20). The "
                             "Gentiles were 'given over' (paredoken, 1:24, 26, 28) -- language echoing "
                             "Deuteronomy 32:8-9, where God allotted the nations to the sons of God. (2) The "
                             "solution is the righteousness of God revealed in Christ's death (3:21-26) -- "
                             "a propitiation (hilasterion) that satisfies divine justice and demonstrates "
                             "divine love simultaneously. (3) The scope is cosmic -- creation itself groans "
                             "for liberation (8:18-25), and neither angels nor rulers nor powers can separate "
                             "from God's love (8:38-39). (4) The mystery of Israel's hardening and the "
                             "Gentiles' inclusion (9-11) is the Deuteronomy 32 drama played out in history, "
                             "ending in the merciful inclusion of 'all Israel' (11:26). (5) The practical "
                             "life of the redeemed community (12-16) is the new humanity living under "
                             "Christ's lordship, awaiting the final crushing of Satan (16:20)."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script (majuscule) in the earliest manuscripts",
        "linguistic_notes": "Romans represents the highest level of rhetorical sophistication in the Pauline "
                           "corpus. Paul employs the diatribe style -- an ancient rhetorical technique "
                           "involving imaginary objections and dialogical engagement with an interlocutor "
                           "(2:1-5, 17-24; 3:1-9, 27-31; 6:1-2, 15; 7:7, 13; 9:14, 19-21; 11:1, 11, 19). "
                           "The style reflects Hellenistic philosophical discourse (Epictetus, Seneca) "
                           "adapted for theological argumentation. Key theological vocabulary includes: "
                           "<strong>dikaiosyne theou</strong> ('the righteousness of God' -- the central "
                           "theme; 1:17; 3:21-22), <strong>hilasterion</strong> ('propitiation/mercy seat' "
                           "-- 3:25; the kapporet of the Day of Atonement applied to Christ), "
                           "<strong>sarx</strong> ('flesh' -- the dominant anthropological term for human "
                           "existence in its weakness and opposition to God), <strong>pneuma</strong> "
                           "('Spirit' -- the divine power enabling new life; chapters 8), "
                           "<strong>nomos</strong> ('law' -- used in multiple senses: Torah, moral principle, "
                           "inner principle; the most complex term in the letter), and "
                           "<strong>mysterion</strong> ('mystery' -- 11:25; 16:25; the hidden plan now "
                           "revealed). The Greek of Romans is dense, logically structured, and marked by "
                           "chains of argument (gar... gar... gar -- 'for... for... for') that build "
                           "cumulative cases.",
        "grammar_match": "Romans is characterized by its logical connectives and argumentative structure. "
                        "The word 'therefore' (oun/dio/ara) appears frequently (3:20, 28; 5:1, 12, 18; "
                        "6:4, 12; 8:1, 12; 9:16, 18; 12:1), marking the major transitions of the argument. "
                        "The diatribe questions ('What shall we say then?' -- ti oun eroumen, 3:5; 4:1; "
                        "6:1; 7:7; 8:31; 9:14, 30) create a dialogical rhythm. The letter moves between "
                        "theological exposition and emotional outburst: the measured logic of chapters 1-4 "
                        "gives way to the exuberant celebration of 8:31-39 ('If God is for us, who can be "
                        "against us?') and the anguished lament of 9:1-3 ('I have great sorrow and "
                        "unceasing anguish in my heart'). The doxologies (8:31-39; 11:33-36; 16:25-27) "
                        "punctuate the argument with worship, breaking the logical chain to praise the "
                        "God whose ways transcend human comprehension."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Romans IS scripture -- the most theologically influential letter in the New Testament "
                   "and the systematic foundation of Christian soteriology.",
        "nt_usage": "Romans quotes the Old Testament more extensively and more systematically than any other "
                    "New Testament document. Paul cites over 60 Old Testament passages, drawing from the "
                    "Torah, Prophets, and Writings. Key quotations include: Habakkuk 2:4 ('the righteous "
                    "shall live by faith,' 1:17 -- the thesis verse), Genesis 15:6 ('Abraham believed God, "
                    "and it was counted to him as righteousness,' 4:3 -- the proof of justification by "
                    "faith), Psalm 32:1-2 (David's testimony of forgiveness, 4:7-8), Psalm 51:4 (God "
                    "justified in his words, 3:4), Isaiah 52:5 ('God's name is blasphemed among the nations,' "
                    "2:24), Psalm 44:22 ('For your sake we are being killed,' 8:36), Isaiah 28:16/Joel 2:32 "
                    "('everyone who calls on the name of the Lord will be saved,' 10:11-13), Isaiah 59:20-21 "
                    "('the Deliverer will come from Zion,' 11:26-27), Deuteronomy 32:35 ('Vengeance is mine,' "
                    "12:19), and Psalm 69:9 ('the reproaches of those who reproach you fell on me,' 15:3). "
                    "Romans 9-11 is essentially a sustained midrash on Deuteronomy 32 and its implications.",
        "internal_consistency": "Romans is deeply consistent with the rest of the Pauline corpus and the "
                               "broader New Testament. The justification-by-faith argument (3:21-4:25) "
                               "develops and systematizes the case Paul made more polemically in Galatians "
                               "2:15-3:29. The Adam-Christ typology (5:12-21) connects to the christological "
                               "hymns of Philippians 2:6-11 and Colossians 1:15-20. The Spirit and adoption "
                               "theology (8:1-17) parallels Galatians 4:4-7. The Israel-and-the-nations "
                               "theology (9-11) addresses the same questions raised in Galatians but with "
                               "more nuance and hope. The practical ethics (12:1-15:13) parallel Ephesians "
                               "4-6 and Colossians 3. The eschatological hope (8:18-25) connects to "
                               "1 Corinthians 15 and 1 Thessalonians 4-5. Romans is Paul's systematic "
                               "synthesis, weaving together themes developed across his entire ministry."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "The earliest manuscript witness is P46 (Chester Beatty Papyrus II), dated c. 200 AD, "
                    "which contains most of Romans (with some lacunae). The doxology of 16:25-27 appears "
                    "after 15:33 in P46, reflecting the textual fluidity at the letter's end.",
        "major_witnesses": [
            {"name": "P46 (Chester Beatty II)", "date": "c. 200 AD",
             "note": "The earliest substantial witness to Romans. Places the doxology (16:25-27) after "
                     "15:33. Contains most of the letter with some damage at the end."},
            {"name": "P26", "date": "c. 600 AD",
             "note": "Fragment containing Romans 1:1-16. Confirms the standard text of the letter's opening."},
            {"name": "Codex Sinaiticus (Aleph)", "date": "c. 350 AD",
             "note": "Complete text of Romans. Places the doxology at 16:25-27 (its standard position). "
                     "One of the two most important uncial manuscripts for the Pauline letters."},
            {"name": "Codex Vaticanus (B)", "date": "c. 325 AD",
             "note": "Complete text of Romans. Places the doxology at 16:25-27. The most important "
                     "early manuscript for the entire New Testament."},
            {"name": "Codex Alexandrinus (A)", "date": "c. 400 AD",
             "note": "Contains the doxology in both locations (after 14:23 and after 16:25), reflecting "
                     "the textual complexity of the letter's ending."}
        ],
        "reliability": "The text of Romans is exceptionally well-preserved. There are no major textual "
                       "variants that affect theological content. The main textual issue is the location "
                       "of the doxology (16:25-27) -- it appears at different places in different manuscripts, "
                       "suggesting that some versions of Romans circulated without chapters 15-16 (possibly "
                       "Marcion's edition). A few manuscripts omit 'in Rome' (en Rome) from 1:7 and 1:15, "
                       "possibly reflecting a version intended for general circulation. The theological "
                       "content -- justification by faith, the Adam-Christ typology, the Spirit's work, "
                       "Israel's mystery -- is stable across all witnesses."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Romans was written from Corinth (c. 56-58 AD) during Paul's third missionary journey, "
                   "at a pivotal moment in his ministry. He had completed his mission in the eastern "
                   "Mediterranean ('from Jerusalem and all the way around to Illyricum I have fulfilled "
                   "the ministry of the gospel of Christ,' 15:19) and was about to carry the collection "
                   "for the poor in Jerusalem (15:25-28) before setting out for Rome and Spain -- the "
                   "western frontier of the known world. The letter reflects both confidence (the eastern "
                   "mission is complete) and anxiety (Paul fears danger in Jerusalem, 15:31).",

        "geography": "The letter's geographical scope is the entire Mediterranean world: from Jerusalem "
                     "(15:19, 25) to Illyricum (15:19, modern Albania/Croatia), Rome (1:7, 15), and "
                     "Spain (15:24, 28). This reflects Paul's understanding of his apostolic mandate: he "
                     "is the apostle to the Gentile nations (1:5; 11:13; 15:16), tasked with completing "
                     "the reversal of the Deuteronomy 32 scattering by bringing the gospel to the ends "
                     "of the earth. Theologically, the letter operates with a cosmic geography: 'all the "
                     "world' (holos ho kosmos, 3:19) stands guilty before God, and 'the whole creation' "
                     "(pasa he ktisis, 8:22) groans for redemption. The olive tree of chapter 11 maps "
                     "the spiritual geography: Israel is the root, the Gentiles are wild branches grafted "
                     "in, and the whole tree will eventually be restored.",

        "historical_connections": "Romans connects to several major historical realities: (1) The Claudius "
                                 "expulsion (49 AD, Acts 18:2; Suetonius, Claudius 25.4) -- Claudius "
                                 "expelled Jews from Rome due to disturbances 'at the instigation of "
                                 "Chrestus' (possibly Christ/Christos), which left the Roman church "
                                 "predominantly Gentile and created the Jew-Gentile tensions Paul addresses. "
                                 "(2) The Jerusalem collection (15:25-28; cf. 2 Cor 8-9; Acts 24:17) -- "
                                 "the offering from Gentile churches for the Jewish saints in Jerusalem, "
                                 "which Paul understood as a tangible expression of the Jew-Gentile unity "
                                 "he proclaims theologically. (3) The Erastus inscription at Corinth -- a "
                                 "paving stone inscribed 'Erastus, in return for his aedileship, laid this "
                                 "pavement at his own expense,' possibly identifying the Erastus of 16:23 "
                                 "as a known public official, providing archaeological confirmation of a "
                                 "person named in Romans."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Romans provides the most systematic theological treatment of the cosmic situation "
                   "that the divine council framework describes: the nations given over to false worship, "
                   "the cosmic scope of redemption, the inability of the spiritual powers to separate "
                   "from God's love, and the final crushing of Satan."
                   "\n\n"
                   "THE NATIONS GIVEN OVER (1:18-32): Paul describes the downward spiral of Gentile "
                   "humanity in language that echoes Deuteronomy 32:8-9. God 'gave them over' (paredoken, "
                   "repeated three times: 1:24, 26, 28) -- the same verb used for divine judicial "
                   "abandonment. In the Deuteronomy 32 worldview, when the nations rebelled at Babel, "
                   "God disinherited them and allotted them to the sons of God (bene elohim) as their "
                   "spiritual overlords. The result was the nations' descent into idolatry -- worshiping "
                   "the creation rather than the Creator. Romans 1:18-32 describes this descent: they "
                   "'exchanged the glory of the immortal God for images resembling mortal man and birds "
                   "and animals and creeping things' (1:23), and God 'gave them over' to the consequences. "
                   "The threefold 'giving over' (to impurity, 1:24; to dishonorable passions, 1:26; to a "
                   "debased mind, 1:28) traces the progressive abandonment of the nations to the "
                   "governance of the rebellious sons of God."
                   "\n\n"
                   "CREATION GROANING (8:18-25): The cosmic scope of redemption extends beyond humanity: "
                   "'the creation itself will be set free from its bondage to corruption (phthora) and "
                   "obtain the freedom of the glory of the children of God' (8:21). The whole created "
                   "order has been 'subjected to futility (mataiotes)' (8:20) -- not voluntarily but by "
                   "divine decree, awaiting liberation. This is the cosmic dimension of the Fall: not just "
                   "human sin but the entire creation subjected to the consequences of the cosmic "
                   "rebellion, groaning for the day when the sons of God (the redeemed humanity) are "
                   "revealed and the cosmos is set free."
                   "\n\n"
                   "THE POWERS POWERLESS (8:38-39): 'For I am sure that neither death, nor life, nor "
                   "angels (angeloi), nor rulers (archai), nor things present, nor things to come, nor "
                   "powers (dynameis), nor height, nor depth, nor anything else in all creation, will "
                   "be able to separate us from the love of God in Christ Jesus our Lord.' Paul names "
                   "the members of the divine council hierarchy -- angels, rulers, powers -- and declares "
                   "them impotent against God's love. The 'height' (hypsoma) and 'depth' (bathos) may "
                   "refer to astrological terms for celestial positions, extending the claim to the "
                   "entire cosmic domain of spiritual influence."
                   "\n\n"
                   "SATAN CRUSHED (16:20): 'The God of peace will soon crush Satan under your feet.' "
                   "This stunning one-verse promise combines Genesis 3:15 (the seed of the woman crushing "
                   "the serpent's head) with Psalm 110 (enemies as a footstool) and applies it to the "
                   "church: it is YOUR feet under which Satan will be crushed. The chief of the rebellious "
                   "council members meets his end through the new humanity in Christ.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 13-14 (Deuteronomy 32 worldview -- the nations given over, the background of Rom 1)",
            "The Unseen Realm, chapter 30-31 (principalities and powers in Paul -- Rom 8:38-39)",
            "The Unseen Realm, chapter 35-36 (the cosmic scope of redemption -- Rom 8:18-25)",
            "Supernatural, chapter 10-11 (the nations given over and the gospel's reversal)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 8-9 (Satan's defeat, Rom 16:20)",
            "The Naked Bible Podcast, episode 93 (Romans 1 and the Deuteronomy 32 worldview)",
            "The Naked Bible Podcast, episode 115 (Romans 8:38-39 -- powers that cannot separate)",
            "The Naked Bible Podcast, episode 195 (Romans 9-11 and Israel's mystery)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "Justification by Faith -- What Paul Actually Means",
            "body": "The word <strong>dikaiosyne</strong> (Greek: <em>dikaiosyne</em>, 'righteousness' or "
                    "'justice') is the most important theological term in Romans, appearing over 30 times. "
                    "The phrase <strong>dikaiosyne theou</strong> ('the righteousness of God,' 1:17; 3:21-22) "
                    "has been interpreted in three major ways:<br><br>"
                    "<strong>(1) An attribute of God</strong> -- God's own moral righteousness or justice. "
                    "This was the medieval Catholic understanding and is part of the truth.<br>"
                    "<strong>(2) A gift from God</strong> -- the righteous status that God grants to those "
                    "who believe. This was Luther's breakthrough reading and the foundation of Protestant "
                    "soteriology. When Paul says 'the righteous shall live by faith' (1:17, quoting Hab 2:4), "
                    "he means that right standing with God comes through faith, not through works of the law.<br>"
                    "<strong>(3) God's covenant faithfulness</strong> -- the New Perspective on Paul (E. P. "
                    "Sanders, James Dunn, N. T. Wright) argues that dikaiosyne theou is God's faithful "
                    "commitment to his covenant promises, demonstrated in the saving act of Christ. God is "
                    "'righteous' because he keeps his promise to Abraham, rescues his people, and puts the "
                    "world right.<br><br>"
                    "All three dimensions are present in Romans. The 'righteousness of God' is BOTH God's "
                    "character (his justice, 3:25-26) AND his gift (the righteous status he confers on "
                    "believers, 3:22) AND his covenant faithfulness (his keeping of the Abrahamic promise, "
                    "4:13-16). The term is rich enough to encompass all three."
        },
        {
            "type": "theology",
            "title": "Propitiation (Hilasterion) -- The Mercy Seat and the Cross",
            "body": "Romans 3:25 describes Christ as the one 'whom God put forward as a propitiation "
                    "(<strong>hilasterion</strong>) by his blood, to be received by faith.' The word "
                    "<em>hilasterion</em> is enormously significant because it is the same word used in the "
                    "LXX (Greek Old Testament) for the <strong>kapporet</strong> -- the 'mercy seat' or "
                    "'atonement cover' on top of the Ark of the Covenant (Exod 25:17-22; Lev 16:2, 13-15). "
                    "On the Day of Atonement (Yom Kippur), the high priest sprinkled blood on the kapporet "
                    "to atone for Israel's sins.<br><br>"
                    "Paul is making a stunning claim: <strong>Christ himself is the new mercy seat.</strong> "
                    "The place where God's wrath and God's mercy meet -- where judgment and grace intersect -- "
                    "is no longer a golden lid in the Holy of Holies but the crucified body of Jesus. God "
                    "'put him forward' (proetheto -- publicly displayed, like the mercy seat was displayed to "
                    "Israel on Yom Kippur) as the place of atonement. The blood that was sprinkled on the "
                    "kapporet is now Christ's own blood. The high priest who entered the Holy of Holies is "
                    "now Christ himself (cf. Hebrews 9:11-14).<br><br>"
                    "Two theological issues are at stake: (1) <strong>Propitiation vs. expiation</strong>: "
                    "Propitiation means turning away God's wrath (satisfying divine justice). Expiation means "
                    "cleansing sin (removing guilt). The hilasterion does BOTH: it satisfies God's righteous "
                    "judgment (3:25-26, 'so that he might be just') AND it cleanses sin ('the one who justifies "
                    "the one who has faith in Jesus'). (2) <strong>Public display</strong>: unlike the kapporet, "
                    "which was hidden behind the veil and seen only by the high priest once a year, Christ was "
                    "'put forward publicly' -- the atonement is open, visible, and accessible to all."
        },
        {
            "type": "theology",
            "title": "The Flesh (Sarx) -- Not Your Body, Your Orientation",
            "body": "The word <strong>sarx</strong> (Greek: <em>sarx</em>, 'flesh') appears over 25 times "
                    "in Romans and is Paul's most misunderstood term. In popular Christian usage, 'the flesh' "
                    "is often equated with the physical body, especially physical desires. This is NOT what "
                    "Paul means.<br><br>"
                    "<em>Sarx</em> in Romans has several senses: (1) <strong>Physical human existence</strong> "
                    "(neutral): 'according to the flesh' (kata sarka) can simply mean 'in terms of physical "
                    "descent' (1:3 -- Christ descended from David 'according to the flesh'; 4:1 -- Abraham "
                    "'our forefather according to the flesh'; 9:3 -- Paul's kinsmen 'according to the flesh'). "
                    "(2) <strong>Human weakness and mortality</strong> (slightly negative): humanity in its "
                    "creaturely limitation, unable to achieve what God requires (8:3 -- 'what the law could not "
                    "do, weakened by the flesh'). (3) <strong>The whole person oriented against God</strong> "
                    "(deeply negative): this is the primary theological sense. 'Those who live according to "
                    "the flesh set their minds on the things of the flesh' (8:5). 'To set the mind on the "
                    "flesh is death' (8:6). 'Those who are in the flesh cannot please God' (8:8). In this "
                    "sense, <em>sarx</em> is the entire human being -- body, mind, emotions, will -- oriented "
                    "toward self and sin, operating in the sphere of the old Adam, under the archon's influence. "
                    "The opposite of <em>sarx</em> is not 'soul' or 'spirit' (as in Greek philosophy) but "
                    "<strong>pneuma</strong> (Spirit) -- the divine power that reorients the whole person "
                    "toward God.<br><br>"
                    "The crucial distinction: Paul is NOT a dualist who hates the physical body. The body will "
                    "be REDEEMED (8:23 -- 'the redemption of our bodies'), not escaped. Sarx is not the body "
                    "but the orientation -- the default human setting of self-reliance, self-determination, "
                    "and resistance to God."
        },
        {
            "type": "interpretation",
            "title": "Romans 9-11 -- Predestination, Israel, and the Olive Tree",
            "body": "Romans 9-11 is the most debated section of the letter. Three major questions:<br><br>"
                    "<strong>(1) Predestination (9:6-29)</strong>: Paul cites Jacob and Esau ('I loved Jacob "
                    "but I hated Esau,' 9:13), Pharaoh ('I raised you up for this very purpose,' 9:17), and "
                    "the potter and clay metaphor (9:20-21) to establish God's sovereign freedom in election. "
                    "Calvinists read this as individual predestination to salvation or damnation. Arminians "
                    "argue Paul is discussing God's historical purposes for nations (Israel/Edom), not "
                    "individual eternal destinies. The New Perspective argues Paul is explaining how God's "
                    "covenant faithfulness operates: God's word has not failed (9:6) because the true 'Israel' "
                    "was always defined by promise, not ethnicity.<br><br>"
                    "<strong>(2) Israel's hardening (11:7-10, 25)</strong>: 'A partial hardening has come upon "
                    "Israel, until the fullness of the Gentiles has come in' (11:25). Israel's temporary "
                    "hardening serves a cosmic purpose: it creates space for the Gentile mission, which in "
                    "turn will provoke Israel to jealousy and salvation. The hardening is PARTIAL (not total) "
                    "and TEMPORARY (until the fullness of the Gentiles comes in).<br><br>"
                    "<strong>(3) 'All Israel will be saved' (11:26)</strong>: What does 'all Israel' mean? "
                    "Three views: (a) Ethnic Israel -- all Jews will eventually be saved through Christ. "
                    "(b) The elect of Israel -- the true remnant throughout history. (c) The whole people of "
                    "God -- both Jews and Gentiles as the true Israel. The olive tree metaphor (11:17-24) "
                    "shows that Israel is the root, Gentile believers are grafted in, broken branches can be "
                    "re-grafted, and God's purpose is the salvation of the whole tree.<br><br>"
                    "In the divine council framework, Romans 9-11 is the Deuteronomy 32 worldview reversed: "
                    "the nations, once disinherited and given to the sons of God, are now being grafted into "
                    "Israel's olive tree. Israel, YHWH's own portion, has experienced temporary hardening to "
                    "make room for the nations' return. The end result is the reunification of all nations "
                    "under the one God -- the eschatological reversal of Babel."
        },
        {
            "type": "context",
            "title": "Romans 7 -- Who Is Speaking? Paul, Adam, or Israel?",
            "body": "Romans 7:7-25 ('I do not do the good I want to do, but the evil I do not want to do -- "
                    "this I keep on doing,' 7:19) is one of the most personally resonant and theologically "
                    "debated passages in the Bible. Three major interpretations:<br><br>"
                    "<strong>(1) Paul's present Christian experience</strong> -- Augustine (later), Luther, "
                    "Calvin, and most Reformed theology read Romans 7 as Paul describing the ongoing struggle "
                    "of the believer. Even the regenerate Christian experiences internal conflict between the "
                    "desire to obey God and the power of remaining sin.<br>"
                    "<strong>(2) Paul's pre-Christian experience</strong> -- The early church fathers (Origen, "
                    "early Augustine, Chrysostom), Wesley, and many contemporary scholars argue that Romans 7 "
                    "describes life under the law WITHOUT the Spirit -- the unregenerate person who knows what "
                    "is right but lacks the power to do it. Romans 8 then provides the answer: 'There is "
                    "therefore now no condemnation for those who are in Christ Jesus' (8:1).<br>"
                    "<strong>(3) Israel personified through Adam</strong> -- N. T. Wright and others argue "
                    "that the 'I' is not autobiographical but rhetorical: Paul speaks as Adam/Israel receiving "
                    "the commandment ('you shall not covet,' 7:7, the tenth commandment), finding that the "
                    "commandment intended for life brings death (7:10). This reading connects Romans 7 to the "
                    "Adam-Christ typology of Romans 5.<br><br>"
                    "The passage is best understood as a retrospective description from the Christian "
                    "standpoint: Paul looks back at life under the law and sees its inability to deliver from "
                    "sin's power. The 'wretched man' cry (7:24) is resolved not by human effort but by divine "
                    "intervention: 'Thanks be to God through Jesus Christ our Lord!' (7:25)."
        },
        {
            "type": "language",
            "title": "Key Greek Terms in Romans",
            "body": "<strong>dikaiosyne</strong> (<em>dikaiosyne</em>) -- 'righteousness/justice.' The central "
                    "theological term. Used over 30 times. Encompasses God's character, God's gift, and God's "
                    "covenant faithfulness.<br><br>"
                    "<strong>hilasterion</strong> (<em>hilasterion</em>) -- 'propitiation/mercy seat.' 3:25. "
                    "The LXX term for the kapporet on the Ark of the Covenant. Christ as the new place of "
                    "atonement where God's wrath and mercy meet.<br><br>"
                    "<strong>paradidomi</strong> (<em>paradidomi</em>) -- 'to give over/hand over.' 1:24, 26, "
                    "28. The threefold divine judicial abandonment of the nations -- echoing the Deut 32 "
                    "allotment. Also used for Christ being 'given over' for us (4:25; 8:32) -- the same verb "
                    "for judgment becomes the verb of salvation.<br><br>"
                    "<strong>nomos</strong> (<em>nomos</em>) -- 'law.' The most complex term in Romans, used "
                    "in at least four senses: (1) the Torah/Mosaic law (2:12-13; 3:19-21), (2) a general "
                    "principle (3:27 -- 'the law of faith'; 7:21 -- 'I find this law'), (3) the 'law of sin "
                    "and death' (8:2) -- sin's enslaving power, (4) the 'law of the Spirit of life' (8:2) -- "
                    "the Spirit's liberating power. Context determines which sense Paul intends.<br><br>"
                    "<strong>sarx</strong> (<em>sarx</em>) -- 'flesh.' NOT the physical body. The whole person "
                    "oriented against God, under the old Adam's influence. Opposed to <em>pneuma</em> (Spirit), "
                    "not to 'soul.'<br><br>"
                    "<strong>hyiothesia</strong> (<em>hyiothesia</em>) -- 'adoption as sons.' 8:15, 23; 9:4. "
                    "A legal term from Roman adoption law, where the adopted son received full inheritance "
                    "rights, a new name, and a new family identity. Applied to believers' status in God's "
                    "family and to Israel's prior status as God's adopted people."
        }
    ]
}
