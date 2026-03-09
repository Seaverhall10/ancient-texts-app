"""
info.py -- Acts (Praxeis Apostolon): Scholarly Text Introduction

This file provides the "front page" for Acts in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Acts is Volume 2 of Luke's two-part work -- the sequel to the Gospel of
Luke, tracing the expansion of the gospel from Jerusalem to Rome. Through
its divine council lens, Acts is the book of Babel reversal. At Pentecost
(Acts 2), the Holy Spirit descends and the apostles speak in the languages
of "every nation under heaven" (2:5) -- the nations divided at Babel are
now united by the Spirit. Stephen's speech (Acts 7) retells Israel's
history as a divine council narrative. Paul's Areopagus speech (Acts 17)
directly addresses the Deuteronomy 32 worldview: God "made from one man
every nation... having determined allotted periods and the boundaries of
their dwelling place" (17:26). The book traces the gospel's advance from
Jewish Jerusalem to Gentile Rome, overcoming every spiritual, ethnic, and
geographic barrier -- the Deuteronomy 32 disinheritance being reversed,
nation by nation, through the power of the Spirit.
"""

TEXT_INFO = {
    "text_id": "acts",
    "display_name": "Acts (Praxeis Apostolon)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / History",
        "detail": "Acts is the only book of NT history and has been recognized as canonical from the "
                  "earliest period. It appears in the Muratorian Canon (~170 AD), Irenaeus' writings "
                  "(Against Heresies, ~180 AD), and every subsequent canonical list. Acts is "
                  "indispensable to the NT canon because it provides the historical bridge between the "
                  "Gospels and the Epistles: without Acts, we would not know how the church was "
                  "founded, how the gospel spread from Jerusalem to Rome, or how Paul became an "
                  "apostle. It is the only canonical account of Pentecost, the Jerusalem council, "
                  "Paul's conversion, and the Gentile mission. Some Marcionites excluded Acts because "
                  "it portrayed Paul as compatible with the Jerusalem apostles, which contradicted "
                  "Marcion's anti-Jewish theology. The church's response was to affirm Acts as "
                  "authoritative witness to the unity of Jewish and Gentile Christianity."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Luke, the author of the Third Gospel, as indicated by the prologue's direct "
                       "address to Theophilus (1:1, 'In the first book, O Theophilus, I dealt with all "
                       "that Jesus began to do and teach'). The same external witnesses who identify "
                       "Luke as the Gospel's author -- the Muratorian Canon, Irenaeus, the Anti-"
                       "Marcionite Prologue -- attribute Acts to him as well. The 'we-passages' "
                       "(16:10-17; 20:5-15; 21:1-18; 27:1-28:16) use first-person plural, strongly "
                       "suggesting the author was present during those events.",

        "scholarly_debate": "The Lukan authorship of Acts is debated along the same lines as the "
                           "Gospel (see the Luke info.py). Additional issues for Acts include: (1) "
                           "Differences between Acts' portrayal of Paul and Paul's self-portrait in "
                           "his letters (e.g., the Jerusalem council in Acts 15 vs. Galatians 2; "
                           "Paul's relationship with the Jerusalem apostles). (2) Whether the 'we-"
                           "passages' represent a genuine travel diary or a literary convention. (3) "
                           "Historical difficulties: the relationship between Acts 5:36-37 and "
                           "Josephus' accounts of Theudas and Judas the Galilean. Most scholars "
                           "accept that the author of Acts is the same person who wrote the Third "
                           "Gospel, whether or not he is the Luke of Paul's letters.",

        "bottom_line": "Acts is the second volume of Luke-Acts, written by the same author as the "
                       "Third Gospel. Whether he is the Luke of Colossians 4:14 or another early "
                       "Christian writer, he produced the most important historical narrative of the "
                       "early church -- tracing the gospel's advance from a small Jewish movement in "
                       "Jerusalem to a world-spanning faith reaching the capital of the Roman Empire."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "If Acts was written before Paul's trial in Rome, as the abrupt ending (28:30-31) "
                       "may suggest, it would date to ~62-63 AD. This is supported by: (1) No mention "
                       "of Paul's death. (2) No mention of the fall of Jerusalem (70 AD). (3) No "
                       "mention of the Neronian persecution (64 AD). (4) The positive portrayal of "
                       "Roman officials, consistent with a pre-Neronian date.",
        "critical_range": "Most critical scholars date Acts to ~80-90 AD, following the Gospel of Luke "
                         "(also dated ~80-85 AD). The argument: if Luke used Mark (~65-70 AD) and Acts "
                         "was written after Luke, then Acts dates to the 80s or later. The abrupt "
                         "ending may be a literary choice: Luke's narrative goal is to trace the gospel "
                         "from Jerusalem to Rome (1:8), and once Paul reaches Rome and preaches there "
                         "'with all boldness and without hindrance' (28:31), the narrative is complete.",
        "evidence": "Key evidence includes: (1) The prologue's reference to 'the first book' (1:1), "
                    "linking Acts to the Gospel of Luke. (2) The 'we-passages' suggesting eyewitness "
                    "participation. (3) The abrupt ending at Rome -- either because the author was "
                    "writing in real time or because Rome was the literary destination. (4) The earliest "
                    "manuscript: P45 (Chester Beatty Papyrus I, 3rd century), P29 (3rd century, "
                    "containing Acts 26:7-8, 20), and P48 (3rd century). The major codices (Sinaiticus, "
                    "Vaticanus, Alexandrinus, Bezae) all contain Acts."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Theophilus (1:1) and the same educated Gentile Christian audience as the "
                            "Gospel of Luke. Acts serves multiple functions for this audience: (1) "
                            "Historical: providing an authoritative account of the church's founding and "
                            "expansion. (2) Apologetic: demonstrating that Christianity is not a dangerous "
                            "new movement but the legitimate continuation of Israel's ancient faith, and "
                            "that Roman officials repeatedly found Christians innocent of wrongdoing. (3) "
                            "Theological: showing that the Gentile mission was not a departure from God's "
                            "plan but its fulfillment -- the Spirit himself directed the inclusion of "
                            "Gentiles. (4) Ecclesiological: modeling church life, governance, and mission "
                            "for subsequent generations.",

        "purpose": "Acts traces the fulfillment of Jesus' commission in 1:8: 'You will be my witnesses "
                   "in Jerusalem and in all Judea and Samaria, and to the end of the earth.' The "
                   "narrative follows this geographic expansion: Jerusalem (chapters 1-7), Judea and "
                   "Samaria (chapters 8-12), and the ends of the earth (chapters 13-28). Luke "
                   "demonstrates that every expansion of the gospel was directed by the Holy Spirit: "
                   "Pentecost (2:1-4), the Samaritan mission (8:14-17), the conversion of Cornelius "
                   "(10:44-48), the Antioch mission (13:1-3), and Paul's Macedonian vision (16:9-10). "
                   "The inclusion of Gentiles is not a human innovation but a divine initiative.",

        "theological_intent": "Acts' deepest theological claim is that the risen Jesus, through the Holy "
                             "Spirit, is actively directing the reclamation of the nations. The Spirit is "
                             "the primary actor: poured out at Pentecost (2:1-4), guiding Philip to the "
                             "Ethiopian (8:29), falling on Cornelius' household (10:44), setting apart Paul "
                             "and Barnabas (13:2), forbidding entry into Asia and directing toward Macedonia "
                             "(16:6-10). The gospel's advance is not merely a human missionary enterprise "
                             "but the divine council's program of Babel reversal, powered by the Spirit "
                             "and directed by the risen Lord."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Acts displays the same linguistic range as the Gospel of Luke -- from "
                           "polished literary Greek in the speeches to more colloquial narrative style "
                           "in the action sequences. The speeches in Acts are theologically crafted "
                           "compositions: Peter's Pentecost sermon (2:14-36), Stephen's speech (7:2-53), "
                           "Paul's Areopagus address (17:22-31), and Paul's defense speeches (22:1-21; "
                           "24:10-21; 26:1-29) represent different rhetorical styles suited to different "
                           "audiences (Jews, Hellenistic Jews, pagan philosophers, Roman officials). "
                           "Whether these are verbatim transcripts, summaries, or Luke's literary "
                           "compositions based on traditional material is debated. The 'we-passages' show "
                           "a shift to first-person plural that is stylistically consistent with the rest "
                           "of Acts, suggesting a single author who was sometimes present at the events.",
        "grammar_match": "Acts' Greek is more varied than the Gospel's, reflecting the diversity of "
                        "settings and audiences. The narrative sections use standard Koine storytelling "
                        "conventions. The speeches show awareness of classical rhetorical forms: Peter's "
                        "sermons follow Jewish homiletical patterns (gezerah shawah -- linking texts by "
                        "shared vocabulary), while Paul's Areopagus speech employs Stoic philosophical "
                        "language familiar to a Greek audience."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Acts IS scripture -- the canonical history of the early church and the narrative "
                   "demonstration that the OT promises are being fulfilled in the Gentile mission.",
        "nt_usage": "Acts is saturated with OT quotations and allusions, particularly in the speeches. "
                    "Peter's Pentecost sermon quotes Joel 2:28-32 (the Spirit poured out on all flesh) "
                    "and Psalms 16 and 110 (the resurrection and ascension, 2:17-36). Stephen's speech "
                    "(chapter 7) retells Israel's history from Abraham to Solomon. James quotes Amos "
                    "9:11-12 at the Jerusalem council (15:16-18) to justify the Gentile mission. Paul "
                    "quotes Psalm 2:7 (13:33), Isaiah 55:3 (13:34), Psalm 16:10 (13:35), Isaiah "
                    "49:6 (13:47), and Habakkuk 1:5 (13:41) in his preaching. The pattern is "
                    "consistent: the OT predicted the Messiah's suffering, resurrection, and the "
                    "inclusion of the Gentiles, and these predictions are now being fulfilled.",
        "internal_consistency": "Acts demonstrates remarkable internal consistency with the Gospel of "
                               "Luke: the prologue connects directly to the Gospel's ending, the ascension "
                               "account bridges the two volumes, the themes of Spirit-empowerment, "
                               "prayer, joy, and universal mission continue seamlessly. Acts also "
                               "connects to Paul's letters at multiple points: the Jerusalem council "
                               "(Acts 15 // Gal 2), Paul's missionary journeys (confirmed by letter "
                               "destinations), and Paul's imprisonment in Rome (Phil 1:12-14)."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "P45 (Chester Beatty Papyrus I), dating to the 3rd century, contains portions of "
                    "Acts. P29 (3rd century) contains Acts 26:7-8, 20. P48 (3rd century) contains "
                    "Acts 23:11-17, 25-29. The major codices all contain Acts in full.",
        "major_witnesses": [
            {"name": "Codex Sinaiticus (Aleph)", "date": "4th century AD",
             "note": "Contains Acts in full. Represents the Alexandrian text type."},
            {"name": "Codex Vaticanus (B)", "date": "4th century AD",
             "note": "Contains Acts in full. Generally considered the best manuscript for Acts."},
            {"name": "Codex Bezae (D)", "date": "5th century AD",
             "note": "Contains a significantly different text of Acts -- about 10% longer than the "
                     "Alexandrian text, with many additions, paraphrases, and unique readings. The "
                     "'Western text' of Acts is the most significant textual variation in the NT."},
            {"name": "Codex Alexandrinus (A)", "date": "5th century AD",
             "note": "Contains Acts in full. An important witness to the Byzantine text type."}
        ],
        "reliability": "Acts has a uniquely complex textual history. Two distinct text forms exist: "
                       "(1) The Alexandrian text (Sinaiticus, Vaticanus, P45, P75) -- shorter and "
                       "generally considered closer to the original. (2) The Western text (Codex "
                       "Bezae, Old Latin, some Syriac) -- about 10% longer, with many additions "
                       "including extra details about the Spirit's guidance, stronger anti-Jewish "
                       "language, and expanded narrative. Scholarly debate continues over whether the "
                       "Western text represents: (a) an early revision by the author himself (a second "
                       "edition), (b) an early scribal expansion, or (c) a separate textual tradition "
                       "with some authentic readings. Most modern translations follow the Alexandrian "
                       "text, noting significant Western variants."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Acts spans approximately 30 years of church history, from the ascension of Jesus "
                   "(~30 AD) to Paul's imprisonment in Rome (~60-62 AD). The historical context "
                   "includes: (1) The Roman Empire under Tiberius, Caligula, Claudius, and Nero. "
                   "(2) The Jewish world before the destruction of Jerusalem: the Temple still "
                   "standing, the Sanhedrin still functioning, multiple Jewish parties (Pharisees, "
                   "Sadducees, Essenes) still active. (3) The emergence of Christianity as a distinct "
                   "movement: initially a Jewish sect, then increasingly Gentile, eventually reaching "
                   "the heart of the Roman Empire. (4) Key historical events: Claudius' expulsion of "
                   "Jews from Rome (~49 AD, Acts 18:2), the proconsulship of Gallio in Corinth "
                   "(~51-52 AD, Acts 18:12), and the procuratorship of Felix and Festus in Judea.",

        "geography": "Acts follows the geographic expansion outlined in 1:8: Jerusalem (chapters 1-7), "
                     "Judea and Samaria (chapters 8-12), and 'the end of the earth' (chapters 13-28). "
                     "The narrative spans the eastern Mediterranean: Jerusalem, Judea, Samaria, "
                     "Antioch of Syria, Cyprus, Asia Minor (modern Turkey), Macedonia and Achaia "
                     "(modern Greece), and finally Rome. Paul's missionary journeys cover thousands "
                     "of miles by land and sea. The geographic movement from Jerusalem to Rome is "
                     "theologically significant: the gospel moves from the center of the Jewish world "
                     "to the center of the Gentile world.",

        "historical_connections": "Acts connects to numerous datable events: (1) Herod Agrippa I's "
                                 "death in 44 AD (Acts 12:20-23, confirmed by Josephus, Ant. 19.343-350). "
                                 "(2) The famine under Claudius (~46-48 AD, Acts 11:28). (3) Claudius' "
                                 "expulsion edict (~49 AD, Acts 18:2, confirmed by Suetonius, Claudius 25.4). "
                                 "(4) Gallio's proconsulship in Corinth (~51-52 AD, Acts 18:12, confirmed by "
                                 "the Gallio Inscription from Delphi). (5) Felix and Festus as procurators "
                                 "of Judea (~52-60 AD, Acts 23-26). These synchronizations make Acts one of "
                                 "the most historically anchored books in the NT."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Acts is the book of Babel reversal -- the narrative of how the disinherited nations "
                   "are being reclaimed for YHWH through the Spirit-empowered proclamation of the risen "
                   "Jesus. Every major event in Acts has divine council significance."
                   "\n\n"
                   "PENTECOST AS BABEL REVERSAL (Acts 2:1-11): The Spirit descends on the gathered "
                   "disciples, and they speak in the languages of 'every nation under heaven' (2:5). "
                   "The list of nations in 2:9-11 represents the full scope of the known world. At "
                   "Babel (Gen 11), YHWH confused the languages and scattered the nations; at Pentecost, "
                   "the Spirit gives the languages and gathers the nations. The same Greek verbs used "
                   "in the LXX of Deuteronomy 32:8 (the allotment of nations) appear in Acts 2. Peter's "
                   "sermon quotes Joel 2:28-32: 'I will pour out my Spirit on all flesh' -- the Spirit "
                   "is no longer confined to Israel but is poured out on the nations."
                   "\n\n"
                   "STEPHEN'S DIVINE COUNCIL HISTORY (Acts 7:2-53): Stephen retells Israel's history "
                   "as a story of persistent rebellion: Abraham's call (7:2-8), Joseph's betrayal by "
                   "his brothers (7:9-16), Moses rejected by Israel twice (7:23-29, 35-43), and the "
                   "golden calf (7:39-41). Critically, Stephen quotes Amos 5:25-27 about Israel "
                   "worshiping 'the host of heaven' (te stratia tou ouranou, 7:42) -- the celestial "
                   "powers that Deuteronomy 4:19 says were 'allotted' to the nations. Israel adopted "
                   "the worship of the nations' gods, reversing its unique status."
                   "\n\n"
                   "PAUL'S AREOPAGUS SPEECH (Acts 17:22-31): Paul declares that God 'made from one man "
                   "every nation of mankind to live on all the face of the earth, having determined "
                   "allotted periods (prostetagmenous kairous) and the boundaries of their dwelling "
                   "place (horothesias tes katoikias auton)' (17:26). This is a direct echo of "
                   "Deuteronomy 32:8: God determined the nations' boundaries and allotted periods. "
                   "The purpose: 'that they should seek God' (17:27). The nations were not abandoned "
                   "-- they were given space and time to seek the true God. 'The times of ignorance "
                   "God overlooked, but now he commands all people everywhere to repent' (17:30). The "
                   "era of Deuteronomy 32 governance is over; the era of direct reclamation has begun."
                   "\n\n"
                   "FROM SATAN'S POWER TO GOD (Acts 26:18): Paul describes his commission from the "
                   "risen Jesus: 'to open their eyes, so that they may turn from darkness to light "
                   "and from the power (exousias) of Satan to God.' This summarizes the entire "
                   "narrative of Acts: the nations are being transferred from Satan's jurisdiction "
                   "to God's kingdom. Every conversion, every church planted, every nation reached "
                   "is a territory reclaimed from the hostile powers.",

        "key_heiser_refs": [
            "The Unseen Realm, ch. 30-34 (Pentecost, the Gentile mission, and the reversal of Babel)",
            "The Unseen Realm, ch. 13-14 (Deuteronomy 32 worldview -- the framework for Acts 17:26-27)",
            "Supernatural, ch. 14-16 (the Spirit and the mission to the nations)",
            "Demons, ch. 10-12 (spiritual warfare in Acts -- exorcisms, opposition, the powers)",
            "The Naked Bible Podcast, ep. 101-103 (Acts 2 -- Pentecost as Babel reversal)",
            "The Naked Bible Podcast, ep. 115 (Acts 17 -- Paul's Areopagus speech and Deut 32)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "Pentecost as Babel Reversal -- The Most Important Event in Acts",
            "body": "Pentecost (Acts 2) is not merely the birthday of the church or the first occurrence "
                    "of speaking in tongues -- it is the <strong>reversal of Babel</strong>, the undoing "
                    "of the Deuteronomy 32 disinheritance of the nations. At Babel (Gen 11), YHWH "
                    "confused the languages and scattered the nations. According to Deuteronomy 32:8-9, "
                    "he then allotted those nations to the sons of God (the bene elohim), keeping Israel "
                    "as his own portion. At Pentecost, the Spirit descends and the apostles speak in the "
                    "languages of 'every nation under heaven' (2:5). The confusion of Babel is reversed: "
                    "where the nations were divided by language, they are now united by the Spirit. The "
                    "list of nations in 2:9-11 -- Parthians, Medes, Elamites, Mesopotamians, Judeans, "
                    "Cappadocians, Pontians, Asians, Phrygians, Pamphylians, Egyptians, Libyans, "
                    "Romans, Cretans, and Arabians -- represents the full scope of the known world. "
                    "Peter's quotation of Joel 2:28 ('I will pour out my Spirit on <em>all flesh</em>') "
                    "declares that the Spirit is no longer restricted to Israel but is available to the "
                    "nations. The 3,000 who respond (2:41) are 'from every nation' -- the firstfruits "
                    "of the Babel reversal. This is the program announced in the Great Commission "
                    "(Matt 28:19, 'all nations'; Luke 24:47, 'all nations') and empowered at Pentecost."
        },
        {
            "type": "interpretation",
            "title": "Acts 17:26-27 -- Paul Quotes the Deuteronomy 32 Worldview to Pagans",
            "body": "Paul's Areopagus speech in Athens (17:22-31) is one of the most theologically "
                    "significant speeches in Acts, because Paul addresses <em>pagans</em> using the "
                    "Deuteronomy 32 worldview. He declares that God 'made from one man every nation of "
                    "mankind to live on all the face of the earth, having determined allotted periods "
                    "(prostetagmenous kairous) and the boundaries of their dwelling place (horothesias "
                    "tes katoikias auton)' (17:26). This language directly echoes Deuteronomy 32:8 (LXX): "
                    "'When the Most High divided the nations, when he separated the sons of Adam, he "
                    "fixed the boundaries (horia) of the nations.' Paul is telling the Athenians that "
                    "their existence as a nation, their geographical placement, and their historical "
                    "epochs were all determined by the one true God -- the God they worship 'as unknown' "
                    "(17:23). The purpose of this arrangement: 'that they should seek God, and perhaps "
                    "feel their way toward him and find him' (17:27). Even the Deuteronomy 32 "
                    "disinheritance was not abandonment but a temporary measure with a redemptive "
                    "purpose. Now 'the times of ignorance God overlooked, but now he commands all "
                    "people everywhere to repent, because he has fixed a day on which he will judge "
                    "the world in righteousness by a man whom he has appointed' (17:30-31). The era "
                    "of governance by territorial elohim is ending; the era of direct divine claim on "
                    "all nations through the risen Jesus has begun."
        },
        {
            "type": "context",
            "title": "Stephen's Speech -- The Longest Speech in Acts and Its Divine Council Theology",
            "body": "Stephen's speech (7:2-53) is the longest in Acts and one of the most theologically "
                    "dense passages in the NT. Stephen retells Israel's history from Abraham to Solomon, "
                    "but with a pointed emphasis: Israel repeatedly rejected God's chosen agents. "
                    "Joseph's brothers sold him into slavery (7:9). Moses was rejected twice -- first "
                    "by the Israelite who asked 'Who made you a ruler and a judge?' (7:27, 35), and "
                    "again through the golden calf (7:39-41). The divine council dimension emerges in "
                    "7:42-43, where Stephen quotes Amos 5:25-27: 'You took up the tent of Moloch and "
                    "the star of your god Rephan, the images that you made to worship.' Israel adopted "
                    "the worship of the 'host of heaven' (stratia tou ouranou, 7:42) -- the very "
                    "celestial powers that Deuteronomy 4:19 says YHWH 'allotted to all the peoples "
                    "under the whole heaven.' Israel was supposed to be separate from the nations' "
                    "gods; instead, it worshiped them. Stephen's climactic accusation: 'You who "
                    "received the law as delivered by angels (eis diatagas angelon) and did not keep "
                    "it' (7:53) -- the Torah was mediated by angels (a tradition found in Deut 33:2 "
                    "LXX; Gal 3:19; Heb 2:2), and Israel violated even this angelically delivered law."
        },
        {
            "type": "scholarship",
            "title": "The 'We-Passages' -- Was Luke There?",
            "body": "At four points in Acts, the narrative suddenly shifts from third person ('they') to "
                    "first person plural ('we'): 16:10-17 (Troas to Philippi), 20:5-15 (Philippi to "
                    "Miletus), 21:1-18 (Miletus to Jerusalem), and 27:1-28:16 (the sea voyage to Rome). "
                    "Three main explanations exist: (1) <strong>Eyewitness presence</strong>: the author "
                    "was personally present during these events and signals this by switching to 'we.' "
                    "This is the traditional view and the most natural reading. (2) <strong>Incorporated "
                    "source</strong>: the author used a travel diary (perhaps his own, perhaps someone "
                    "else's) and forgot to or chose not to change the pronouns. (3) <strong>Literary "
                    "convention</strong>: ancient sea-voyage narratives sometimes used first-person "
                    "plural for vividness (though this claim is disputed). Most scholars favor option 1 "
                    "or a combination of 1 and 2: the author was present during the 'we' sections and "
                    "may have kept notes that were incorporated into the final narrative. If so, this "
                    "places the author with Paul on the second and third missionary journeys and the "
                    "journey to Rome -- consistent with the traditional identification as Luke."
        }
    ]
}
