"""
info.py -- 2 John: Scholarly Text Introduction

The shortest book in the New Testament (13 verses), written by "the Elder" to
an "elect lady" (likely a house church), warning against hosting false teachers
who deny the Incarnation. A letter about boundaries: hospitality to deceivers
means participation in cosmic rebellion.
"""

TEXT_INFO = {
    "text_id": "2john",
    "display_name": "2 John",

    # -- CANONICAL STATUS ------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament General Epistle",
        "detail": "Second John is canonical in all Christian traditions -- Catholic, Orthodox, and "
                  "Protestant. Its acceptance was slower than 1 John due to its brevity and its "
                  "ambiguous author designation ('the Elder'). Eusebius listed it among the "
                  "'disputed' (antilegomena) books, noting that 'not all consider them genuine' "
                  "(Ecclesiastical History 3.25.3). However, it appears in the Muratorian Fragment "
                  "(~170 AD), was cited by Irenaeus (Against Heresies 1.16.3), and was included "
                  "in the canonical lists of Athanasius (367 AD) and the councils of Hippo (393) "
                  "and Carthage (397). By the 4th century its place in the canon was secure."
    },

    # -- AUTHORSHIP ------------------------------------------------------
    "authorship": {
        "traditional": "The author identifies himself as 'the Elder' (ho presbyteros, verse 1). "
                       "Early church tradition identified this Elder with the apostle John, son of "
                       "Zebedee, following the same attribution as 1 John and the Gospel of John. "
                       "Irenaeus explicitly quotes 2 John 7-8 and attributes it to 'John, the "
                       "disciple of the Lord' (Against Heresies 1.16.3).",

        "scholarly_debate": "The self-designation 'the Elder' is the author's only identification. "
                           "This title could refer to the apostle John in his old age, or it could "
                           "indicate a distinct figure -- 'John the Elder' -- mentioned by Papias "
                           "as reported in Eusebius (Ecclesiastical History 3.39.4). The vocabulary, "
                           "theology, and style are unmistakably from the same hand as 1 John and "
                           "closely related to the Gospel of John. Most scholars treat 2 John, 3 John, "
                           "and 1 John as products of the same author or at minimum the same Johannine "
                           "school. The brevity of 2 John (fitting on a single papyrus sheet) and its "
                           "specific, occasional nature make it unlikely to be a forgery -- there is no "
                           "reason to forge a letter this short and this situational.",

        "bottom_line": "The author is 'the Elder' -- the same authoritative figure behind 1 John "
                       "and 3 John, writing from within the Johannine community. Whether this is the "
                       "apostle John or a close associate, the letter carries the same theological "
                       "authority and addresses the same crisis of proto-Gnostic false teaching."
    },

    # -- DATE ------------------------------------------------------------
    "date": {
        "traditional": "Placed late in the apostle John's life, during his residence in Ephesus, "
                       "roughly contemporary with 1 John.",
        "critical_range": "Approximately AD 90-95, contemporary with or slightly after 1 John. "
                         "The same crisis -- false teachers denying the Incarnation -- is addressed "
                         "in both letters, suggesting they were written close together in time.",
        "evidence": "The theological vocabulary and concerns are identical to 1 John, placing them "
                    "in the same historical moment. The letter presupposes the same schism ('many "
                    "deceivers have gone out into the world,' verse 7) and the same christological "
                    "test ('those who do not confess the coming of Jesus Christ in the flesh'). "
                    "The brevity and specific occasion suggest a real letter sent to a real community "
                    "during an active crisis, not a literary composition after the fact."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------
    "audience": {
        "original_audience": "The letter is addressed to 'the elect lady and her children' (eklekte "
                            "kyria, verse 1). This is almost certainly a metaphor for a house church "
                            "and its members, not a literal woman named Kyria. The personification of "
                            "a community as a woman is well-attested in both Old and New Testament "
                            "usage (Israel as bride/wife of YHWH; the church as bride of Christ; 'she "
                            "who is in Babylon' in 1 Peter 5:13). The 'children' are the church members. "
                            "The 'elect sister' in verse 13 is another house church -- the one from "
                            "which the Elder writes.",

        "purpose": "Second John has one central purpose: to warn the house church NOT to receive "
                   "traveling teachers who deny that Jesus Christ came in the flesh. In the early "
                   "church, traveling missionaries depended on the hospitality of house churches for "
                   "lodging, food, and a platform to teach (see 3 John for the positive side of this "
                   "system). The Elder warns that extending hospitality to false teachers makes the "
                   "host church complicit in their 'evil works' (ponera erga, verse 11). This is not "
                   "inhospitality -- it is discernment. In the divine council framework, providing a "
                   "platform for teaching that denies the Incarnation means aiding the 'spirit of the "
                   "antichrist' (1 John 4:3) in its work.",

        "theological_intent": "Second John applies the christological test of 1 John 4:2-3 to the "
                             "practical question of church hospitality. Theology has consequences for "
                             "practice. If the Incarnation is the mechanism by which God invaded enemy "
                             "territory, then denying the Incarnation is siding with the enemy -- and "
                             "helping those who deny it is joining their side in the cosmic conflict."
    },

    # -- ORIGINAL LANGUAGE -----------------------------------------------
    "language": {
        "original": "Greek. Koine Greek of the late first century.",
        "script": "Greek uncial script in the earliest manuscripts.",
        "linguistic_notes": "The vocabulary is pure Johannine: aletheia (truth, 5 times in 13 verses), "
                           "agape (love), entole (commandment), plane/planos (error/deceiver), "
                           "antichristos (antichrist). The letter is extremely concise, fitting on a "
                           "single sheet of papyrus (the author notes he has 'much to write' but prefers "
                           "to speak 'face to face,' verse 12). The style is more clearly epistolary than "
                           "1 John, with a standard greeting (verses 1-3) and closing (verses 12-13).",
        "grammar_match": "Consistent with late first-century Koine Greek and the Johannine literary "
                        "tradition. The brevity makes detailed stylistic analysis difficult, but every "
                        "linguistic feature aligns with the Johannine corpus."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------
    "scripture_alignment": {
        "verdict": "Canonical New Testament epistle. Fully authoritative Christian scripture, applying "
                   "the theology of the Gospel of John and 1 John to a specific pastoral situation.",

        "where_it_aligns": [
            "The christological test -- confessing Jesus Christ 'coming in the flesh' (verse 7) -- "
            "repeats the criterion of 1 John 4:2-3 and presupposes John 1:14 ('the Word became flesh').",
            "The love commandment ('that we love one another,' verse 5) echoes John 13:34 and "
            "1 John 3:11, 23.",
            "The warning against false teachers aligns with Jesus' warnings (Matthew 7:15; 24:11, 24), "
            "Paul's warnings (Acts 20:29-30; 2 Timothy 4:3-4), and Peter's warnings (2 Peter 2:1).",
            "The concept that hospitality to false teachers constitutes participation in their 'evil "
            "works' (verse 11) parallels Paul's warning about partnership with darkness "
            "(2 Corinthians 6:14)."
        ],

        "where_it_diverges": [],

        "reader_guidance": "Second John is a short, focused application of Johannine theology to a "
                          "specific practical problem. Read it alongside 1 John (which provides the "
                          "full theological framework) and 3 John (which shows the positive side of "
                          "the hospitality question)."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------
    "manuscripts": {
        "earliest": "The earliest papyrus witness is P9 (if it covers 2 John; this is debated). The "
                    "major uncials Codex Sinaiticus, Codex Vaticanus, and Codex Alexandrinus all "
                    "contain 2 John. The letter's brevity means it is often preserved as part of a "
                    "collection of the Catholic Epistles rather than independently.",
        "major_witnesses": [
            {"name": "Codex Sinaiticus (Aleph)", "date": "4th century AD",
             "note": "Complete text of 2 John within the Catholic Epistles collection."},
            {"name": "Codex Vaticanus (B)", "date": "4th century AD",
             "note": "Complete text. The two great 4th-century uncials agree closely on 2 John."},
            {"name": "Codex Alexandrinus (A)", "date": "5th century AD",
             "note": "Complete text. Important confirming witness."}
        ],
        "reliability": "The text of 2 John is stable across the manuscript tradition. Its brevity "
                       "means there are few opportunities for significant variation. No major textual "
                       "disputes affect the letter's meaning."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------
    "historical_context": {
        "setting": "The same Johannine community crisis as 1 John, but 2 John addresses a specific "
                   "practical dimension: how should house churches handle traveling teachers who "
                   "promote the secessionist theology? The early church depended on a network of "
                   "house churches that provided hospitality to itinerant missionaries. This system "
                   "was essential for the spread of the gospel (see Romans 16:1-2; 3 John 5-8) but "
                   "also created a vulnerability: false teachers could exploit the hospitality network "
                   "to spread their message. Second John addresses this vulnerability.",

        "geography": "The 'elect lady' is likely a house church in the network of Johannine communities "
                     "in Asia Minor, possibly in the region around Ephesus. The Elder writes from another "
                     "community ('the children of your elect sister greet you,' verse 13). The letter's "
                     "existence demonstrates that the Johannine community was not a single congregation "
                     "but a network of house churches spread across a geographical region.",

        "historical_connections": "Second John provides invaluable evidence for how the early church "
                                 "functioned at the practical level: house churches, traveling teachers, "
                                 "the hospitality network, and the challenge of maintaining doctrinal "
                                 "standards across a decentralized movement. The Didache (a roughly "
                                 "contemporary church manual, ~AD 80-100) addresses the same practical "
                                 "problem: how to distinguish genuine traveling prophets from frauds "
                                 "(Didache 11-13). The letter also shows that early Christian communities "
                                 "exercised doctrinal discipline -- they had the authority and the "
                                 "responsibility to refuse hospitality to teachers whose message was "
                                 "deemed contrary to the apostolic tradition."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------
    "divine_council": {
        "relevance": "moderate",
        "summary": "Second John is brief but its divine council implications are significant. The core "
                   "theological claim: hospitality to false teachers constitutes participation in their "
                   "'evil works' (ponera erga, verse 11). In the divine council framework, this means "
                   "that providing a platform for teaching that denies the Incarnation is not a neutral "
                   "act -- it is choosing sides in the cosmic war.\n\n"
                   "Key connections:\n\n"
                   "(1) THE DECEIVER AND ANTICHRIST (verse 7): 'Many deceivers have gone out into the "
                   "world, those who do not confess the coming of Jesus Christ in the flesh. Such a one "
                   "is the deceiver and the antichrist.' The language of 'going out into the world' "
                   "parallels the Watchers 'leaving their proper dwelling' (Jude 6) and the spirits "
                   "operating in the human realm. The 'deceiver' (planos) is animated by the 'spirit of "
                   "the antichrist' (1 John 4:3) -- a hostile spiritual power working through human agents.\n\n"
                   "(2) PARTICIPATION IN EVIL WORKS (verse 11): 'Whoever greets him participates in his "
                   "evil works.' The Greek koinonei ('participates,' 'shares in') implies genuine "
                   "partnership, not mere social contact. In the cosmic war framework, this means that "
                   "hospitality to agents of the antichrist spirit makes the host an ally of that spirit. "
                   "This is the same logic as Paul's warning about eating at the table of demons "
                   "(1 Corinthians 10:20-21) -- spiritual allegiance has real consequences.\n\n"
                   "(3) TRUTH AS COSMIC REALITY: The word 'truth' (aletheia) appears 5 times in 13 "
                   "verses. Truth is not a human opinion -- it is the reality of God's governance, the "
                   "way things actually are in the divine council. Walking 'in truth' means aligning "
                   "with God's administration; the 'deceiver' represents the counter-administration of "
                   "the evil one.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 37 (the cosmic war and the Incarnation as divine invasion)",
            "Supernatural, chapter 15 (spiritual warfare through false teaching)",
            "The Naked Bible Podcast, episodes on the Johannine epistles and antichrist"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "Who Is the 'Elect Lady'?",
            "body": "The greeting 'to the elect lady and her children' (verse 1) has been debated for "
                    "centuries. Some early interpreters took it as a literal woman named Kyria (the "
                    "Greek word for 'lady') or Eklekte (the Greek for 'elect'). But the overwhelming "
                    "consensus of modern scholarship is that 'the elect lady' is a house church "
                    "personified as a woman, and 'her children' are its members. This interpretation "
                    "is supported by the letter's closing: 'The children of your elect sister greet "
                    "you' (verse 13), which makes much more sense as one church greeting another than "
                    "as a literal family reference. The personification of communities as women is "
                    "standard biblical imagery (Jerusalem as daughter Zion, the church as the bride "
                    "of Christ)."
        },
        {
            "type": "interpretation",
            "title": "Why Is Hospitality So Important?",
            "body": "Modern readers may wonder why the Elder makes such a big deal about not hosting "
                    "certain teachers. The answer lies in how the early church functioned. There were "
                    "no church buildings until the 3rd century -- believers met in private homes. "
                    "Traveling missionaries depended entirely on the hospitality of house churches for "
                    "lodging, food, and a platform to teach. To 'receive' (lambanein) a teacher meant "
                    "to welcome them into your home, provide for their needs, and give them an audience. "
                    "It was an endorsement. The Elder's prohibition is not about being rude to strangers "
                    "-- it is about refusing to provide institutional support and a teaching platform to "
                    "those who deny the Incarnation. In modern terms: it is the difference between "
                    "being kind to someone and inviting them to preach from your pulpit. The stakes are "
                    "cosmic: the teaching in question denies the very mechanism by which God entered the "
                    "world to defeat the powers of darkness."
        }
    ]
}
