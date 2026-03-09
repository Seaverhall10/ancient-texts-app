"""
info.py -- 3 John: Scholarly Text Introduction

A personal letter from "the Elder" to Gaius about church authority and the
traveling missionary system. Gaius faithfully receives missionaries; Diotrephes
rejects them and exalts himself. A study in how authority should function in the
community of God -- mirroring heavenly authority, not grasping for power.
"""

TEXT_INFO = {
    "text_id": "3john",
    "display_name": "3 John",

    # -- CANONICAL STATUS ------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament General Epistle",
        "detail": "Third John is canonical in all Christian traditions -- Catholic, Orthodox, and "
                  "Protestant. Like 2 John, it was initially among the 'disputed' (antilegomena) "
                  "books listed by Eusebius (Ecclesiastical History 3.25.3), primarily because of "
                  "its brevity and the ambiguity of its author. However, it appears in the "
                  "Muratorian Fragment (~170 AD) and was included in the definitive canonical lists "
                  "of the 4th century (Athanasius, Hippo, Carthage). Its personal, occasional "
                  "nature actually argues for authenticity -- there is no reason to forge a brief "
                  "personal note about a church dispute."
    },

    # -- AUTHORSHIP ------------------------------------------------------
    "authorship": {
        "traditional": "The author identifies himself as 'the Elder' (ho presbyteros, verse 1) -- "
                       "the same self-designation as 2 John. Early church tradition identified this "
                       "Elder with the apostle John, son of Zebedee. The personal tone, the use of "
                       "proper names (Gaius, Diotrephes, Demetrius), and the specific situational "
                       "details mark this as a genuine personal letter, not a theological treatise.",

        "scholarly_debate": "The authorship question is identical to 2 John: is 'the Elder' the "
                           "apostle John or a distinct figure within the Johannine community? The "
                           "vocabulary and style are consistent with 1-2 John and the Fourth Gospel. "
                           "The key difference from 1 John is the deeply personal and administrative "
                           "nature of the letter -- this is not theology but church management. The "
                           "Elder has authority to commend (Gaius, Demetrius) and censure (Diotrephes), "
                           "suggesting a recognized leadership position. Some scholars note that the "
                           "Elder's authority appears to be challenged by Diotrephes, which might be "
                           "more consistent with a non-apostolic Elder (one could more easily defy a "
                           "community leader than an apostle).",

        "bottom_line": "The same 'Elder' who wrote 1-2 John, writing a personal letter to a "
                       "trusted friend (Gaius) about a leadership crisis involving Diotrephes. "
                       "The letter is transparently genuine -- its personal details and specific "
                       "situation make forgery implausible."
    },

    # -- DATE ------------------------------------------------------------
    "date": {
        "traditional": "Contemporary with 1-2 John, during the apostle John's residence in Ephesus.",
        "critical_range": "Approximately AD 90-95. The letter addresses the same network of Johannine "
                         "communities as 2 John, though the specific issue is different (authority and "
                         "hospitality rather than doctrinal testing). It may have been sent at or near "
                         "the same time as 2 John, dealing with a related but distinct problem in a "
                         "different house church.",
        "evidence": "The letter's situation -- traveling missionaries, house church hospitality, "
                    "authority disputes -- fits the late first-century church. The vocabulary and "
                    "style place it within the Johannine corpus. Some scholars have suggested that "
                    "3 John was written before 1-2 John, when the schism was a leadership dispute "
                    "rather than a full doctrinal crisis, but this is speculative."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------
    "audience": {
        "original_audience": "Gaius -- a specific individual within the Johannine community network. "
                            "The name Gaius was extremely common in the Roman world (it appears three "
                            "other times in the NT: Acts 19:29; 20:4; Romans 16:23; 1 Corinthians "
                            "1:14). There is no reason to identify this Gaius with any of the others. "
                            "The letter's warm tone ('beloved,' used four times) indicates a close "
                            "personal relationship between the Elder and Gaius.",

        "purpose": "Third John addresses a leadership crisis in the Johannine community. The letter "
                   "has three parts:\n\n"
                   "1. COMMENDATION OF GAIUS (verses 1-8): Gaius is praised for faithfully receiving "
                   "and supporting traveling missionaries sent by the Elder, even though they are "
                   "'strangers' to his community. This is the hospitality system working correctly.\n\n"
                   "2. CONDEMNATION OF DIOTREPHES (verses 9-10): Diotrephes 'loves to be first' "
                   "(philoproteuon) among the community. He refuses to receive the Elder's messengers, "
                   "slanders the Elder, and expels from the church anyone who does welcome the "
                   "missionaries. This is the hospitality system weaponized for personal power.\n\n"
                   "3. COMMENDATION OF DEMETRIUS (verses 11-12): Demetrius is vouched for by 'everyone, "
                   "and by the truth itself.' He may be the letter carrier or a missionary whom Gaius "
                   "is being asked to receive.",

        "theological_intent": "Third John is about authority in the church and how it should function. "
                             "Diotrephes represents self-exalting authority -- 'loving to be first' -- "
                             "which is the pattern of the rebellious elohim (seeking their own glory "
                             "rather than serving God's purposes). Gaius represents servant-authority -- "
                             "faithfully supporting God's work even at personal cost. The letter "
                             "implicitly asks: whose model of authority reflects the heavenly pattern?"
    },

    # -- ORIGINAL LANGUAGE -----------------------------------------------
    "language": {
        "original": "Greek. Koine Greek of the late first century.",
        "script": "Greek uncial script in the earliest manuscripts.",
        "linguistic_notes": "Third John is the most personal and least theological of the Johannine "
                           "epistles. Its vocabulary includes unique terms: philoproteuon ('loving to "
                           "be first,' verse 9, a hapax legomenon -- it appears nowhere else in the "
                           "New Testament or the Septuagint), phluaron ('talking nonsense/slandering,' "
                           "verse 10), and epidechomai ('receive/welcome,' verses 9-10). Despite these "
                           "unique terms, the letter's core vocabulary remains Johannine: aletheia "
                           "(truth), agapetos (beloved), martyrein (to testify/bear witness), and the "
                           "characteristic Johannine contrast between good/evil and truth/falsehood.",
        "grammar_match": "Consistent with late first-century Koine Greek. The letter's style is direct, "
                        "personal, and administrative -- quite different from the homiletical style of "
                        "1 John but consistent with a genuine personal letter."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------
    "scripture_alignment": {
        "verdict": "Canonical New Testament epistle. Fully authoritative Christian scripture. Its "
                   "value lies in what it reveals about early church structure and the ethics of "
                   "leadership.",

        "where_it_aligns": [
            "The commendation of hospitality to missionaries aligns with Jesus' sending instructions "
            "(Matthew 10:11-14; Luke 10:5-12) and Paul's teaching on supporting gospel workers "
            "(1 Corinthians 9:14; 3 John 7-8).",
            "The condemnation of Diotrephes's self-exalting leadership aligns with Jesus' teaching "
            "that greatness in the kingdom means service (Mark 10:42-45; John 13:12-17).",
            "The principle 'do not imitate evil but imitate good' (verse 11) echoes Paul's "
            "'be imitators of God' (Ephesians 5:1) and the consistent NT theme that character "
            "reveals spiritual allegiance.",
            "The letter's emphasis on truth (aletheia, appearing 6 times in 15 verses) is "
            "quintessentially Johannine (John 14:6; 17:17; 1 John 3:18-19)."
        ],

        "where_it_diverges": [],

        "reader_guidance": "Third John is a window into the real, messy, human dynamics of early "
                          "church life. Read it for its practical wisdom about leadership, hospitality, "
                          "and authority -- and for what it reveals about the Johannine community's "
                          "structure. Pair with 2 John (which shows the other side of the hospitality "
                          "question: whom NOT to receive) for a complete picture."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------
    "manuscripts": {
        "earliest": "The earliest witnesses are the great 4th-century uncials. No papyrus fragment "
                    "of 3 John has been identified with certainty, though some fragmentary papyri "
                    "may contain portions.",
        "major_witnesses": [
            {"name": "Codex Sinaiticus (Aleph)", "date": "4th century AD",
             "note": "Complete text of 3 John within the Catholic Epistles collection."},
            {"name": "Codex Vaticanus (B)", "date": "4th century AD",
             "note": "Complete text. Agrees closely with Sinaiticus."},
            {"name": "Codex Alexandrinus (A)", "date": "5th century AD",
             "note": "Complete text. Confirms the reading of the earlier uncials."}
        ],
        "reliability": "The text of 3 John is remarkably stable across the manuscript tradition. "
                       "Its brevity and personal nature mean there are few significant variants. "
                       "No major textual disputes affect interpretation."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------
    "historical_context": {
        "setting": "Third John reveals the inner workings of the early church's missionary support "
                   "system. Traveling teachers ('brothers,' verse 3) went out 'for the sake of the "
                   "Name, accepting nothing from the Gentiles' (verse 7). They depended entirely on "
                   "the hospitality of house churches. Gaius supported this system faithfully; "
                   "Diotrephes weaponized it for personal control. The conflict between Gaius and "
                   "Diotrephes reflects a broader tension in the early church between charismatic "
                   "authority (the Elder, traveling missionaries) and local institutional authority "
                   "(a leader like Diotrephes who controls access to the congregation).",

        "geography": "The letter implies at least three locations: the Elder's base, Gaius's community, "
                     "and Diotrephes's community (which may or may not be the same as Gaius's). All are "
                     "within the Johannine network of house churches in Asia Minor, likely in the region "
                     "around Ephesus. The traveling distance was short enough that the Elder plans to "
                     "visit 'soon' (verse 14).",

        "historical_connections": "Third John provides unique evidence for several aspects of early "
                                 "church life: (1) The itinerant missionary system and its dependence on "
                                 "local hospitality. (2) The transition from charismatic to institutional "
                                 "authority structures. (3) The real possibility of power abuse in house "
                                 "church leadership. (4) The practice of letter-writing as pastoral "
                                 "oversight. The Didache (11-13) addresses the same system from a different "
                                 "angle, providing tests for genuine vs. fraudulent traveling prophets. "
                                 "Paul's letters similarly reflect his dependence on and gratitude for "
                                 "hospitality networks (Romans 16; Philemon)."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------
    "divine_council": {
        "relevance": "moderate",
        "summary": "Third John's divine council relevance centers on the theology of authority. "
                   "Diotrephes 'loves to be first' (philoproteuon) -- and this single Greek word "
                   "captures the essence of the rebellious elohim's sin.\n\n"
                   "Key connections:\n\n"
                   "(1) PHILOPROTEUON -- LOVING TO BE FIRST (verse 9): This compound word appears "
                   "nowhere else in the entire Greek Bible. It describes someone who grasps for "
                   "preeminence, who insists on being the center of authority. In the divine council "
                   "framework, this is THE sin of the rebellious spiritual powers: the Watchers who "
                   "crossed boundaries God set for them (Genesis 6:1-4; 1 Enoch 6-16), the 'gods' "
                   "of Psalm 82 who ruled unjustly, the 'prince of this world' who exalts himself "
                   "against God's authority. Diotrephes enacts in the church the same pattern of "
                   "self-exaltation that characterizes the rebellious elohim. He does not serve the "
                   "community -- he dominates it.\n\n"
                   "(2) AUTHORITY AS SERVICE VS. AUTHORITY AS DOMINION: Gaius represents the pattern "
                   "of faithful authority -- serving God's purposes by supporting missionaries, even "
                   "at personal cost. Diotrephes represents corrupted authority -- using his position "
                   "to exclude others and consolidate power. This mirrors the contrast between loyal "
                   "divine council members (who execute God's will as servants) and rebellious ones "
                   "(who seek their own glory). Jesus explicitly contrasted these two models: 'The "
                   "rulers of the Gentiles lord it over them... It shall not be so among you' "
                   "(Mark 10:42-43). Authority in God's kingdom mirrors heavenly authority: it "
                   "serves; it does not grasp.\n\n"
                   "(3) TRUTH AS COSMIC ALIGNMENT: The word 'truth' (aletheia) appears 6 times in "
                   "15 verses. Walking 'in truth' (verse 3-4) means aligning with reality as God "
                   "defines it -- participating in the divine governance structure rather than "
                   "constructing an alternative based on self-interest.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 12 (the sin of the Watchers: crossing boundaries)",
            "The Unseen Realm, chapter 4 (Psalm 82: gods who abuse their authority are judged)",
            "Supernatural, chapter 7 (how spiritual rebellion mirrors earthly power abuse)",
            "The Naked Bible Podcast, episodes on authority in the divine council"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "Who Are Gaius and Diotrephes?",
            "body": "Gaius and Diotrephes are otherwise unknown -- they appear only in this letter. "
                    "Gaius was a common Roman name (three other men named Gaius appear in the NT), "
                    "and there is no reason to connect this Gaius with any of them. He was apparently "
                    "a prosperous believer who could afford to host traveling missionaries -- "
                    "hospitality in the ancient world required financial resources (food, lodging, "
                    "provisions for the journey). Diotrephes was a local church leader with enough "
                    "authority to refuse entry to missionaries and expel members who welcomed them. "
                    "His title or office is not specified -- the text says only that he 'loves to be "
                    "first.' Some scholars see him as an early example of the 'monarchical bishop' "
                    "pattern (a single leader governing a local church), which was emerging in the "
                    "late first and early second centuries (see Ignatius of Antioch's letters, ~110 AD). "
                    "Demetrius, commended in verse 12, may be the letter carrier or a missionary "
                    "whom the Elder is asking Gaius to receive."
        },
        {
            "type": "interpretation",
            "title": "The Traveling Missionary System",
            "body": "Third John opens a window into how the gospel spread in the first century. "
                    "There were no church buildings, no denominational structures, no budgets for "
                    "missionary salaries. Traveling teachers went out 'for the sake of the Name, "
                    "accepting nothing from the Gentiles' (verse 7) -- they refused payment from "
                    "non-believers to maintain the integrity of their message. Instead, they depended "
                    "entirely on the hospitality of fellow believers in house churches. This created "
                    "a network of mutual dependence: missionaries needed hosts, and hosts benefited "
                    "from the teaching and encouragement of the missionaries. The Elder says those "
                    "who support such workers 'become fellow workers for the truth' (verse 8) -- "
                    "even staying home, Gaius participates in the mission by providing material "
                    "support. This system was beautiful but fragile. It worked when people like Gaius "
                    "were generous and when people like the Elder provided quality control. It broke "
                    "down when people like Diotrephes weaponized hospitality for personal power, or "
                    "when false teachers exploited the system to spread error (the problem 2 John "
                    "addresses). Together, 2 John and 3 John show both sides of the hospitality coin: "
                    "whom to receive (faithful missionaries) and whom to refuse (deniers of the "
                    "Incarnation)."
        }
    ]
}
