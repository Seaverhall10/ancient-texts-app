"""
info.py -- Luke (Kata Loukan): Scholarly Text Introduction

This file provides the "front page" for Luke in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Luke is the Gospel of the universal Savior -- the most literary, historically
grounded, and socially conscious of the four Gospels. Written by a Gentile
physician as Volume 1 of a two-volume work (Luke-Acts), it presents Jesus as
the fulfillment of Israel's story and the hope of all nations. Through its
divine council lens, Luke is the Gospel of cosmic reversal: Satan claims
authority over the nations (4:6), but Jesus has come to reclaim them. He
sends seventy-two disciples to the nations (echoing the seventy nations of
Genesis 10), sees "Satan fall like lightning from heaven" (10:18), and
interprets his entire mission as the fulfillment of "everything written
about me in the Law of Moses and the Prophets and the Psalms" (24:44).
Luke's Pentecost narrative in Acts 2 is the ultimate Babel reversal --
but that is Volume 2. Volume 1 establishes the foundation: the Son of God
has come to seek and save the lost, to release the captives, and to
inaugurate the jubilee of YHWH's favor.
"""

TEXT_INFO = {
    "text_id": "luke",
    "display_name": "Luke (Kata Loukan)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Gospels",
        "detail": "Luke is the third Gospel in the New Testament canon and has been recognized as "
                  "canonical scripture from the earliest period of the church. Together with Acts, "
                  "it constitutes the largest single-author contribution to the NT -- about 27% of "
                  "the total. Luke appears in all ancient canonical lists: the Muratorian Canon (~170 "
                  "AD), Irenaeus' four-Gospel canon (Against Heresies 3.1.1; 3.11.8), and every "
                  "subsequent list. Marcion (~140 AD) used an edited version of Luke as his sole "
                  "Gospel, which may actually confirm Luke's early prominence -- Marcion chose Luke "
                  "precisely because of its association with Paul. The church's response was not to "
                  "reject Luke but to reject Marcion's editing."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Luke, 'the beloved physician' (Col 4:14), a companion of Paul. The Muratorian "
                       "Canon (~170 AD) identifies the author: 'The third book of the Gospel: according "
                       "to Luke. This Luke was a physician. After the ascension of Christ, when Paul "
                       "had taken him with him as one zealous for correctness, he wrote it in his own "
                       "name from report.' Irenaeus (Against Heresies 3.1.1) affirms: 'Luke also, the "
                       "companion of Paul, recorded in a book the Gospel preached by him.' The Anti-"
                       "Marcionite Prologue (~160-180 AD) adds that Luke was from Antioch, was a "
                       "physician, was unmarried, wrote in Achaia, and died at age 84. The 'we-passages' "
                       "in Acts (16:10-17; 20:5-15; 21:1-18; 27:1-28:16) use first-person plural, "
                       "suggesting the author was present during those events. Paul mentions Luke in "
                       "Colossians 4:14 ('Luke the beloved physician greets you'), Philemon 24, and "
                       "2 Timothy 4:11 ('Only Luke is with me').",

        "scholarly_debate": "The Lukan authorship is more widely accepted among scholars than Matthean or "
                           "Johannine authorship, though it remains debated. Arguments for: (1) The "
                           "'we-passages' in Acts are most naturally read as an eyewitness travel diary. "
                           "(2) The prologue (Luke 1:1-4) claims careful research from eyewitnesses, "
                           "consistent with a companion of Paul who had access to early traditions. (3) "
                           "The medical vocabulary noted by Hobart (1882) and Cadbury (1920), while not "
                           "conclusive (educated non-physicians used similar language), is consistent. "
                           "Arguments against: (1) The theology of Luke-Acts differs from Paul's letters "
                           "in some respects (e.g., the portrayal of Paul in Acts vs. Paul's self-portrait "
                           "in Galatians). (2) The 'we-passages' could be a literary convention or "
                           "borrowed from a source. (3) Some scholars argue the author was not a physician "
                           "but simply an educated Greek writer.",

        "bottom_line": "The author of Luke-Acts was a skilled Greek writer, probably a Gentile "
                       "(or Hellenistic Jew), who had access to eyewitness traditions (1:2) and "
                       "possibly accompanied Paul on some journeys. Whether or not he is the Luke of "
                       "Paul's letters, his two-volume work is the most ambitious historical-theological "
                       "project in the NT -- tracing the story from the Jerusalem Temple (Luke 1) to "
                       "the heart of the Roman Empire (Acts 28)."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Some scholars date Luke to the early 60s AD, before Paul's trial in Rome, "
                       "arguing that Acts' abrupt ending (Paul under house arrest) makes most sense if "
                       "the outcome was not yet known. If Acts was written in the early 60s, Luke "
                       "(written first) would date to ~58-62 AD.",
        "critical_range": "Most critical scholars date Luke to ~80-85 AD. Key arguments: (1) Luke "
                         "appears to use Mark (~65-70 AD) as a source. (2) Luke 21:20 ('When you see "
                         "Jerusalem surrounded by armies, then know that its desolation has come near') "
                         "is more specific than Mark 13:14 about the siege of Jerusalem, suggesting "
                         "post-70 knowledge. (3) Luke 19:43-44 ('Your enemies will set up a barricade "
                         "around you and surround you and hem you in on every side. They will dash you "
                         "to the ground, you and your children within you, and they will not leave one "
                         "stone upon another in you') reads as a description of the Roman siege. (4) "
                         "The developed ecclesiology and concern with Gentile mission reflect a later "
                         "setting. Some scholars (Robinson, Hemer) argue strongly for a pre-70 date.",
        "evidence": "Key evidence includes: (1) Luke's use of Mark and Q (if the Two-Source Hypothesis "
                    "is correct). (2) The prologue's reference to 'many' previous accounts (1:1), "
                    "requiring time for multiple narratives to develop. (3) The earliest manuscript "
                    "evidence: P75 (Bodmer Papyrus XIV-XV), dated ~175-225 AD, contains extensive "
                    "portions of Luke and John. P4 (Paris Papyrus), containing portions of Luke 1-6, "
                    "is dated to the late 2nd or early 3rd century. (4) The major codices (Sinaiticus, "
                    "Vaticanus, Alexandrinus, Bezae) all contain Luke."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Theophilus (1:3, 'most excellent Theophilus') and, through him, educated "
                            "Gentile Christians and God-fearing Gentiles interested in the Christian "
                            "movement. The address 'most excellent' (kratiste) suggests a person of high "
                            "social standing -- a Roman official, a patron who funded the writing, or a "
                            "literary dedicatee (though 'Theophilus' means 'lover of God' and could be "
                            "symbolic). Luke writes for people who need 'certainty' (asphaleia, 1:4) "
                            "about the Christian teaching they have received. His audience is literate, "
                            "Greek-speaking, and familiar with the conventions of Hellenistic "
                            "historiography.",

        "purpose": "Luke writes to provide an 'orderly account' (1:3) of the events that 'have been "
                   "accomplished among us' -- the life, death, resurrection, and ascension of Jesus. "
                   "His purposes include: (1) Historical reliability: demonstrating that the Christian "
                   "faith is grounded in real events involving real people at specific times and places "
                   "(2:1-2, the census under Augustus and Quirinius). (2) Theological continuity: "
                   "showing that Jesus fulfills the promises made to Israel in the Hebrew Scriptures "
                   "and that the Gentile mission is the divinely intended next chapter. (3) Social "
                   "concern: highlighting Jesus' ministry to the poor, the marginalized, women, "
                   "Samaritans, tax collectors, and sinners. (4) Universal salvation: Jesus is the "
                   "Savior of all people, not just Israel -- 'a light for revelation to the Gentiles, "
                   "and for glory to your people Israel' (2:32).",

        "theological_intent": "Luke's deepest theological vision is of salvation history (Heilsgeschichte) "
                             "-- the story of God's saving activity from creation to consummation, centered "
                             "on Jesus. Luke divides history into epochs: the time of Israel (the OT, "
                             "culminating in John the Baptist), the time of Jesus (the Gospel), and the "
                             "time of the church (Acts). Jesus is presented as prophet, Savior, and Lord -- "
                             "the one anointed by the Spirit to proclaim good news to the poor and release "
                             "to the captives (4:18-19, quoting Isa 61:1-2). The divine council dimensions "
                             "of Luke's theology emerge in: Satan's claim to the nations (4:6), Jesus' "
                             "vision of Satan's fall (10:18), the Deuteronomy 32 worldview underlying the "
                             "mission of the 72 (10:1-20), and the comprehensive fulfillment claim of "
                             "24:44 ('everything written about me in the Law of Moses and the Prophets and "
                             "the Psalms must be fulfilled')."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek (the most literary Greek in the NT)",
        "script": "Greek uncial script",
        "linguistic_notes": "Luke writes the most polished Greek in the New Testament. His prologue "
                           "(1:1-4) is a single, perfectly constructed periodic sentence in classical "
                           "Greek style, modeled on Hellenistic historical prologues (cf. Josephus, "
                           "Against Apion 1.1; Thucydides 1.1). He then switches to Septuagintal "
                           "style for the birth narratives (chapters 1-2), deliberately imitating the "
                           "LXX's Greek to evoke the feel of the OT -- Hannah's prayer (1 Sam 2:1-10) "
                           "becomes the Magnificat (Luke 1:46-55), and the birth announcement of "
                           "Isaac or Samuel becomes the angelic announcements to Zechariah and Mary. "
                           "Luke preserves fewer Aramaic words than Mark (he often translates or omits "
                           "them), consistent with a Gentile author writing for a Gentile audience. "
                           "His vocabulary is the largest of any NT author (~800 words not found elsewhere "
                           "in the NT). The narrative style shifts between Septuagintal archaism (birth "
                           "narratives), vivid storytelling (the parables), and polished historical "
                           "prose (the passion and Acts).",
        "grammar_match": "Luke's grammar ranges from the classical perfection of the prologue to the "
                        "Semitic flavor of the birth hymns to the straightforward Koine of the "
                        "narrative sections. He uses a wider range of vocabulary and more complex "
                        "sentence structures than Matthew or Mark. His parables are among the most "
                        "masterfully told stories in ancient literature -- the Prodigal Son (15:11-32), "
                        "the Good Samaritan (10:25-37), and the Rich Man and Lazarus (16:19-31) are "
                        "literary achievements of the first order."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Luke IS scripture -- Volume 1 of the most comprehensive salvation history "
                   "narrative in the NT, grounding the faith in OT promises and historical events.",
        "nt_usage": "Luke contains about 25 direct OT quotations and hundreds of allusions. The birth "
                    "narratives (chapters 1-2) are saturated with OT echoes: the Magnificat (1:46-55) "
                    "draws on Hannah's prayer (1 Sam 2:1-10) and celebrates the reversal of the "
                    "powerful and lowly. The Benedictus (1:68-79) draws on the Davidic covenant "
                    "promises. Simeon's Nunc Dimittis (2:29-32) quotes Isaiah 42:6 and 49:6, "
                    "identifying Jesus as 'a light for revelation to the Gentiles.' The Nazareth "
                    "sermon (4:18-19) quotes Isaiah 61:1-2 as the programmatic statement of Jesus' "
                    "ministry. The Emmaus road scene (24:27) records Jesus explaining 'in all the "
                    "Scriptures the things concerning himself,' beginning with Moses and the Prophets. "
                    "The post-resurrection teaching (24:44) makes the comprehensive claim: 'everything "
                    "written about me in the Law of Moses and the Prophets and the Psalms must be "
                    "fulfilled.'",
        "internal_consistency": "Luke-Acts forms a unified theological narrative from the Jerusalem "
                               "Temple (Luke 1:5-25, Zechariah's vision) to Rome (Acts 28:30-31, Paul "
                               "preaching the kingdom). The promise-fulfillment pattern runs throughout: "
                               "what is promised in the birth narratives is fulfilled in the ministry, "
                               "death, and resurrection of Jesus, and what is commissioned in the "
                               "resurrection appearances (Luke 24:47-49) is accomplished in Acts. The "
                               "Spirit is the connecting thread: promised by the Father (Luke 24:49), "
                               "poured out at Pentecost (Acts 2:1-4), and empowering the mission to the "
                               "ends of the earth (Acts 1:8)."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "P75 (Bodmer Papyrus XIV-XV), dated ~175-225 AD, is one of the most important "
                    "NT manuscripts. It contains extensive portions of Luke and John and is remarkably "
                    "close to Codex Vaticanus, suggesting an early and reliable textual tradition. P4 "
                    "(Paris Papyrus) contains portions of Luke 1-6 and is dated to the late 2nd or "
                    "early 3rd century.",
        "major_witnesses": [
            {"name": "P75 (Bodmer Papyrus XIV-XV)", "date": "~175-225 AD",
             "note": "One of the earliest and most important NT manuscripts. Contains large portions "
                     "of Luke 3-24 and John. Text is very close to Codex Vaticanus."},
            {"name": "Codex Sinaiticus (Aleph)", "date": "4th century AD",
             "note": "Contains the full text of Luke. The earliest complete NT manuscript."},
            {"name": "Codex Vaticanus (B)", "date": "4th century AD",
             "note": "Generally considered the best overall NT manuscript. Contains Luke in full."},
            {"name": "Codex Bezae (D)", "date": "5th century AD",
             "note": "Contains a notably different text of Luke in many places, representing the "
                     "'Western text' tradition. Some scholars argue the Western text of Luke may "
                     "preserve earlier readings in certain passages."}
        ],
        "reliability": "The text of Luke is well-attested and generally stable. The most significant "
                       "text-critical issues include: (1) Luke 22:43-44 (the angel strengthening Jesus "
                       "and the bloody sweat in Gethsemane) -- absent from P75 and some early witnesses, "
                       "though present in Sinaiticus. (2) Luke 23:34 ('Father, forgive them, for they "
                       "know not what they do') -- absent from P75, Vaticanus, and other witnesses, "
                       "though widely attested elsewhere. (3) The Western text (Codex Bezae and Old "
                       "Latin) has numerous unique readings throughout Luke, some of which may preserve "
                       "earlier traditions."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Luke's Gospel is set against the backdrop of the Roman Empire at its height. "
                   "Luke is the most historically conscious of the Gospel writers, carefully "
                   "synchronizing Jesus' story with Roman and Jewish political history: the decree "
                   "of Caesar Augustus (2:1), the governorship of Quirinius in Syria (2:2), the "
                   "fifteenth year of Tiberius Caesar with Pontius Pilate as governor of Judea and "
                   "Herod as tetrarch of Galilee (3:1-2). This historical precision serves a "
                   "theological purpose: the salvation story is not myth but history, happening in "
                   "real time under real rulers. The Gospel was likely composed after 70 AD, when "
                   "the Christian movement was spreading throughout the Roman world and needed an "
                   "account that would commend itself to educated Gentile readers.",

        "geography": "Luke's geography is theologically structured. The Gospel begins and ends in "
                     "Jerusalem and the Temple (1:5-25; 24:50-53), forming an inclusio. The central "
                     "section (9:51-19:44) is the 'Travel Narrative' -- Jesus' journey from Galilee "
                     "to Jerusalem, the longest section unique to Luke, containing many of his most "
                     "famous parables. This journey is presented as a deliberate march toward the "
                     "cross: 'When the days drew near for him to be taken up, he set his face to go "
                     "to Jerusalem' (9:51). Acts then continues the geographical expansion: from "
                     "Jerusalem to Judea to Samaria to the ends of the earth (Acts 1:8).",

        "historical_connections": "Luke connects Jesus' story to: (1) Augustus' census (2:1-7), which "
                                 "brings Jesus to Bethlehem -- the universal Roman enrollment as the "
                                 "instrument of messianic prophecy fulfillment. (2) Herod the Great's "
                                 "reign and death. (3) Tiberius' reign, Pilate's governorship, and the "
                                 "Herodian tetrarchy (3:1-2). (4) The Temple establishment (Zechariah as "
                                 "priest, Simeon and Anna as Temple devotees). (5) The broader Roman world "
                                 "(the centurion's servant, 7:1-10; Pilate's atrocities, 13:1; Roman "
                                 "governance throughout Acts)."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "significant",
        "summary": "Luke provides some of the most explicit divine council content in the Gospels, "
                   "including Satan's claim of authority over the nations, Jesus' vision of Satan's "
                   "fall, the courtroom language of spiritual conflict, and the comprehensive "
                   "fulfillment of the Law, Prophets, and Psalms."
                   "\n\n"
                   "SATAN'S AUTHORITY OVER THE NATIONS (Luke 4:5-6): In Luke's version of the "
                   "temptation, Satan shows Jesus 'all the kingdoms of the world in a moment of time' "
                   "and says: 'To you I will give all this authority (exousia) and their glory, for "
                   "it has been delivered to me (emoi paradedotai), and I give it to whom I will' "
                   "(4:6). The critical phrase is 'it has been delivered to me' -- in the passive "
                   "voice, implying someone delivered it. In the Deuteronomy 32 worldview, God himself "
                   "allotted the nations to the sons of God at Babel (Deut 32:8-9). Satan claims this "
                   "allotted authority has been 'delivered' to him -- he exercises dominion over the "
                   "nations' territorial spirits. This is the most explicit statement of the Deut 32 "
                   "worldview in the Gospels."
                   "\n\n"
                   "SATAN FALLS LIKE LIGHTNING (Luke 10:17-20): The seventy-two return from their "
                   "mission rejoicing: 'Lord, even the demons are subject to us in your name!' (10:17). "
                   "Jesus responds: 'I saw Satan fall like lightning from heaven' (10:18). Then: "
                   "'Behold, I have given you authority (exousia) to tread on serpents and scorpions, "
                   "and over all the power (dynamin) of the enemy' (10:19). And the climax: 'Do not "
                   "rejoice in this, that the spirits are subject to you, but rejoice that your names "
                   "are written in heaven' (10:20). The mission of the 72 (or 70, depending on the "
                   "manuscript) likely echoes the 70 nations of Genesis 10 -- the nations divided at "
                   "Babel. Jesus sends envoys to reclaim the nations, and as they advance, he sees "
                   "Satan -- the chief of the territorial powers -- falling from his position of "
                   "heavenly authority."
                   "\n\n"
                   "SATAN DEMANDS TO SIFT PETER (Luke 22:31-32): Jesus warns: 'Simon, Simon, behold, "
                   "Satan demanded (exetesato) to have you, that he might sift you like wheat' (22:31). "
                   "The verb exetesato means 'demanded, asked for' -- courtroom language. This echoes "
                   "Job 1-2, where Satan appears before the divine council and demands permission to "
                   "test Job. The same council dynamic is operative: Satan functions as the accuser/ "
                   "prosecutor who petitions the divine court for permission to test the faithful. "
                   "Jesus has 'prayed for you that your faith may not fail' (22:32) -- the Son "
                   "intercedes before the council on Peter's behalf."
                   "\n\n"
                   "THE LAW, THE PROPHETS, AND THE PSALMS (Luke 24:44): The risen Jesus declares: "
                   "'These are my words that I spoke to you while I was still with you, that everything "
                   "written about me in the Law of Moses and the Prophets and the Psalms must be "
                   "fulfilled.' This three-part division matches the Hebrew Bible's structure (Torah, "
                   "Nevi'im, Ketuvim). The claim is comprehensive: the entire OT -- including the "
                   "divine council texts in the Psalms -- points to Jesus.",

        "key_heiser_refs": [
            "The Unseen Realm, ch. 13-14 (Deuteronomy 32 worldview -- Satan's claim over the nations in Luke 4:6)",
            "The Unseen Realm, ch. 24-26 (the mission of the 72 and the reclamation of the nations)",
            "The Unseen Realm, ch. 33 (Satan falling like lightning -- the cosmic war)",
            "Demons, ch. 7-8 (Satan as accuser in the divine council -- Luke 22:31)",
            "Supernatural, ch. 10-12 (the kingdom's advance against the powers)",
            "The Naked Bible Podcast, ep. 94 (Luke 10 and the mission to the nations)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "Luke 4:6 -- The Deuteronomy 32 Worldview Made Explicit",
            "body": "Luke's version of the temptation contains the most explicit statement of the "
                    "Deuteronomy 32 worldview in the Gospels. Satan shows Jesus the kingdoms and says: "
                    "'To you I will give all this authority and their glory, <strong>for it has been "
                    "delivered to me</strong> (emoi paradedotai), and I give it to whom I will' (4:6). "
                    "The passive voice ('has been delivered') implies a deliverer -- someone gave Satan "
                    "this authority. In the Deuteronomy 32:8-9 framework, when YHWH divided the nations "
                    "at Babel, he allotted them to 'the sons of God' (bene elohim). These spiritual "
                    "rulers over the nations were supposed to govern justly (Psalm 82:2-4) but instead "
                    "corrupted their rule. Satan, as the chief adversary, claims authority over this "
                    "network of territorial spirits. His offer to Jesus is genuine: he does have "
                    "authority to offer. But it is illegitimate authority -- stolen through rebellion, "
                    "not delegated by the Father. Jesus refuses the shortcut. He will reclaim the nations "
                    "through the cross and resurrection, receiving 'all authority in heaven and on earth' "
                    "(Matt 28:18) from the Father, not from Satan."
        },
        {
            "type": "theology",
            "title": "The Mission of the 72 -- Babel Reversal Begins",
            "body": "Luke 10:1 records Jesus sending out 72 (or 70, depending on the manuscript) "
                    "disciples 'two by two... into every town and place where he himself was about to "
                    "go.' The number is not arbitrary. Genesis 10 lists 70 nations descended from "
                    "Noah (72 in the LXX). At Babel (Gen 11), YHWH scattered these nations and, "
                    "according to Deuteronomy 32:8-9, allotted them to the sons of God. Jesus sending "
                    "72 envoys is a symbolic reversal of Babel: where YHWH scattered the nations and "
                    "assigned them to lesser elohim, Jesus now sends agents to reclaim them. The "
                    "mission's success prompts Jesus' vision: 'I saw Satan fall like lightning from "
                    "heaven' (10:18). As the 72 advance into the nations, Satan loses his position of "
                    "cosmic authority. The disciples' authority over 'serpents and scorpions, and over "
                    "all the power of the enemy' (10:19) is divine council language: the enemy's power "
                    "(dynamis) is being broken. But the greater reality: 'your names are written in "
                    "heaven' (10:20) -- they are registered in the divine council's book of life."
        },
        {
            "type": "context",
            "title": "Luke's Unique Parables -- The Stories No Other Gospel Tells",
            "body": "About 35% of Luke's Gospel is unique material found in no other Gospel. This 'L' "
                    "material includes some of the most beloved stories in all of scripture: the "
                    "<strong>Good Samaritan</strong> (10:25-37) -- a Samaritan (despised by Jews) shows "
                    "mercy when a priest and Levite do not, redefining 'neighbor' to include the ethnic "
                    "other. The <strong>Prodigal Son</strong> (15:11-32) -- a rebellious son squanders "
                    "his inheritance among the Gentiles, returns in shame, and is welcomed with "
                    "extravagant grace by the father, while the elder son (representing righteous "
                    "Israel) refuses to celebrate. The <strong>Rich Man and Lazarus</strong> (16:19-31) "
                    "-- reversal of fortunes after death; the rich man in Hades begs for relief while "
                    "Lazarus rests in Abraham's bosom. The <strong>Pharisee and the Tax Collector</strong> "
                    "(18:9-14) -- the self-righteous Pharisee goes home unjustified while the repentant "
                    "tax collector is declared righteous. The <strong>Zacchaeus story</strong> (19:1-10) "
                    "-- the chief tax collector who climbs a tree to see Jesus and receives salvation: "
                    "'The Son of Man came to seek and to save the lost' (19:10). These parables share a "
                    "common theme: God's grace reaches the unexpected, the undeserving, and the outsider. "
                    "In divine council terms, the boundaries of the kingdom extend beyond Israel to "
                    "encompass the nations -- the reversal of Babel that Pentecost will consummate."
        },
        {
            "type": "interpretation",
            "title": "Satan Demands to Sift Peter -- The Divine Council Courtroom",
            "body": "Luke 22:31-32 preserves a detail found in no other Gospel: 'Simon, Simon, behold, "
                    "Satan demanded (exetesato) to have you, that he might sift you like wheat. But I "
                    "have prayed for you that your faith may not fail.' The verb <em>exetesato</em> "
                    "(from exaiteo, 'to demand, to ask for') is courtroom language -- it describes a "
                    "formal petition before an authority. This is the divine council in session: Satan "
                    "appears before God (as in Job 1:6-12; 2:1-6) and demands permission to test "
                    "Peter. The satan's role in the divine council was originally that of the "
                    "prosecutor -- the 'accuser' (Hebrew: satan) who brings charges against the "
                    "faithful. In Job, he demands: 'Does Job fear God for nothing? Stretch out your "
                    "hand and touch all that he has, and he will curse you to your face' (Job 1:9-11). "
                    "In Zechariah 3:1, 'Satan standing at his right hand to accuse him.' In Luke 22, "
                    "the same dynamic is at work: Satan demands the right to test the disciples -- "
                    "specifically 'you' (plural: hymas), meaning all of them. Jesus' response is not "
                    "to prevent the testing but to pray that Peter's faith will survive it: 'When you "
                    "have turned again (epistrepsas), strengthen your brothers' (22:32). The testing "
                    "is permitted; the intercession ensures survival. This is how the divine council "
                    "operates: testing is real, but the Son's intercession sustains the faithful "
                    "through it."
        }
    ]
}
