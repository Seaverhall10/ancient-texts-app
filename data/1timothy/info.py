"""
info.py -- 1 Timothy: Scholarly Text Introduction

Paul's first letter to his protege Timothy, left in Ephesus to combat false
teaching and establish church order. For the divine council framework, key
passages include: the "mystery of godliness" which was "seen by angels" (3:16)
-- the divine council witnessing Christ's incarnation and vindication -- and the
warning about "doctrines of demons" (4:1) in the last days.
"""

TEXT_INFO = {
    "text_id": "1timothy",
    "display_name": "1 Timothy",

    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Pastoral Epistles",
        "detail": "1 Timothy is part of the Pastoral Epistles (1 Tim, 2 Tim, Titus). Attributed to Paul "
                  "by all ancient witnesses. Pauline authorship is debated among modern scholars due to "
                  "vocabulary, style, and theological emphasis differences from the undisputed letters, "
                  "but the traditional attribution remains defensible."
    },

    "authorship": {
        "traditional": "Paul the Apostle, writing to Timothy in Ephesus after Paul's release from his "
                       "first Roman imprisonment (Acts 28). Timothy was Paul's closest associate, called "
                       "'my true child in the faith' (1:2).",
        "scholarly_debate": "The Pastoral Epistles are among the most disputed in the Pauline corpus. "
                           "Arguments against Pauline authorship include: (1) 306 words not found elsewhere "
                           "in Paul; (2) organizational structure implies later development; (3) the false "
                           "teaching described may reflect second-century Gnosticism. Arguments for Pauline "
                           "authorship include: (1) vocabulary differences are expected when addressing "
                           "different topics (church order vs. theology); (2) Paul used a secretary/amanuensis "
                           "who may have influenced style; (3) the personal details fit no known pseudonymous "
                           "setting; (4) early attestation (Polycarp, Irenaeus, Muratorian Canon).",
        "bottom_line": "Pauline authorship is accepted here. The personal details, theological content, "
                       "and early attestation support genuine Pauline origin, possibly with significant "
                       "secretarial freedom."
    },

    "date": {
        "traditional": "62-65 AD, between Paul's first and second Roman imprisonments.",
        "critical_range": "62-65 AD if Pauline; 80-100 AD if pseudonymous.",
        "evidence": "The letter presupposes Paul's release from the imprisonment of Acts 28 and further "
                    "travels not recorded in Acts. This 'second career' hypothesis fits the evidence of "
                    "the Pastoral Epistles."
    },

    "audience": {
        "original_audience": "Timothy, Paul's young associate, stationed in Ephesus to combat false "
                            "teaching and organize the church.",
        "purpose": "Paul writes to (1) charge Timothy to oppose false teachers who promote 'myths and "
                   "endless genealogies' (1:3-4); (2) provide instructions for church worship and "
                   "leadership (chs. 2-3); (3) warn about 'doctrines of demons' in the last times (4:1); "
                   "(4) give pastoral counsel for various groups (widows, elders, slaves, rich).",
        "theological_intent": "The letter is concerned with 'sound doctrine' (hygiainos didaskalia) as "
                             "the antidote to demonic deception. The church is 'the pillar and buttress "
                             "of the truth' (3:15), and its leaders must be above reproach."
    },

    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Key terms: hygiainos didaskalia (sound/healthy doctrine), eusebeia (godliness/ "
                           "piety), mysterion tes eusebeias (mystery of godliness), didaskaliais daimoniōn "
                           "(doctrines/teachings of demons), episkopos (overseer/bishop), diakonos (deacon/ "
                           "servant), presbyteros (elder).",
        "grammar_match": "The Pastorals use more formal, administrative Greek than the undisputed letters, "
                        "reflecting the institutional concerns of the correspondence."
    },

    "scripture_alignment": {
        "verdict": "1 Timothy provides essential NT teaching on church governance, the mystery of "
                   "godliness, and the demonic origin of false doctrine.",
        "nt_usage": "Paul quotes Deuteronomy 25:4 (5:18) and Luke 10:7 (5:18, calling it 'Scripture' -- "
                    "one of the earliest attestations of a Gospel's scriptural authority).",
        "internal_consistency": "The Pastorals connect to Acts (Paul's travel itinerary), Ephesians "
                               "(church governance), and 2 Timothy (Paul's final letter)."
    },

    "manuscripts": {
        "earliest": "Codex Sinaiticus (c. 330-360 AD). P46 does NOT contain the Pastorals, which may "
                    "indicate they circulated separately from the main Pauline collection.",
        "major_witnesses": [
            {"name": "Codex Sinaiticus", "date": "c. 330-360 AD", "note": "Complete text."},
            {"name": "Codex Alexandrinus", "date": "c. 400-440 AD", "note": "Complete text."},
            {"name": "Codex Ephraemi", "date": "c. 450 AD", "note": "Fragmentary."}
        ],
        "reliability": "Well-preserved with minimal significant variants."
    },

    "historical_context": {
        "setting": "Ephesus, the leading city of the Roman province of Asia. Timothy was tasked with "
                   "establishing order in a church beset by false teachers.",
        "geography": "Ephesus was a major port city on the western coast of Asia Minor, famous for the "
                     "temple of Artemis (one of the Seven Wonders) and a significant center of early "
                     "Christianity (Acts 19).",
        "historical_connections": "The false teaching in Ephesus may reflect early forms of the 'Gnostic' "
                                 "tendency: 'myths and genealogies' (1:4), 'what is falsely called knowledge "
                                 "(gnosis)' (6:20), ascetic practices (4:3), and disputes about the law (1:7)."
    },

    "divine_council": {
        "relevance": "moderate",
        "summary": "Two passages are significant: (1) The 'mystery of godliness' (mysterion tes eusebeias, "
                   "3:16) is a creedal hymn that includes 'seen by angels' (ophthe angelois) -- the divine "
                   "council witnessed Christ's incarnation and vindication. This is the heavenly court taking "
                   "note of the most significant event in cosmic history. (2) 'In later times some will "
                   "depart from the faith by devoting themselves to deceitful spirits and doctrines of "
                   "demons (didaskaliais daimoniōn)' (4:1) -- false teaching has a spiritual source. The "
                   "cosmic conflict operates through intellectual deception: demonic beings promote "
                   "doctrines that lead people away from truth.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 35 (the mystery of godliness and angelic witnesses)",
            "Supernatural, chapter 19 (doctrines of demons and spiritual warfare)",
            "The Naked Bible Podcast, episode 207 (1 Tim 3:16 and the divine council)"
        ]
    },

    "reader_notes": [
        {
            "type": "theology",
            "title": "Seen by Angels -- The Council Witnesses",
            "body": "The creedal hymn of 3:16 says Christ was 'manifested in the flesh, vindicated by the "
                    "Spirit, seen by angels (ophthe angelois), proclaimed among the nations, believed on in "
                    "the world, taken up in glory.' The phrase 'seen by angels' places the Christ event in a "
                    "cosmic context: the members of the divine council witnessed the incarnation, death, "
                    "resurrection, and ascension. This connects to 1 Peter 1:12 ('things into which angels "
                    "long to look') and Ephesians 3:10 ('the manifold wisdom of God might now be made known "
                    "to the rulers and authorities in the heavenly places through the church'). The gospel is "
                    "not merely a human story but a cosmic event observed by the entire heavenly court."
        },
        {
            "type": "interpretation",
            "title": "Doctrines of Demons -- Spiritual Source of False Teaching",
            "body": "Paul warns that 'in later times some will depart from the faith by devoting themselves "
                    "to deceitful spirits and doctrines of demons' (4:1). The false teaching includes "
                    "'forbidding marriage and requiring abstinence from foods that God created to be received "
                    "with thanksgiving' (4:3). This ascetic teaching is attributed not to human error but to "
                    "demonic origin: 'deceitful spirits' (pneumasin planois) and 'demons' (daimoniōn) are "
                    "the source. In the divine council framework, false doctrine is a weapon of the cosmic "
                    "rebellion: the hostile spiritual powers promote teachings that distort God's creation "
                    "order and lead people away from truth."
        },
        {
            "type": "context",
            "title": "Why Was Timothy in Ephesus? -- The False Teaching Crisis",
            "body": "1 Timothy only makes sense when you understand the situation Timothy was dropped "
                    "into. Ephesus was a major city of the Roman province of Asia, home to the temple "
                    "of Artemis (one of the Seven Wonders of the ancient world) and a hotbed of religious "
                    "syncretism. Paul had spent over two years there on his third missionary journey (Acts "
                    "19:8-10), during which time 'all the residents of Asia heard the word of the Lord.' "
                    "But Paul had also warned the Ephesian elders that 'fierce wolves will come in among "
                    "you, not sparing the flock, and from among your own selves will arise men speaking "
                    "twisted things, to draw away the disciples after them' (Acts 20:29-30). By the time "
                    "of 1 Timothy, that warning had come true. The false teachers promoted 'myths and "
                    "endless genealogies' (1:4), claimed to be 'teachers of the law' without understanding "
                    "it (1:7), and advanced speculative theology that Paul calls 'what is falsely called "
                    "knowledge' (gnosis, 6:20). The specific nature of the heresy is debated -- it may "
                    "reflect early Gnostic tendencies, Jewish-mystical speculation about angelic hierarchies "
                    "and cosmic genealogies, or a combination. Timothy's task was not merely administrative: "
                    "he was holding the line against a spiritual assault on the church's doctrinal integrity."
        },
        {
            "type": "theology",
            "title": "The Mystery of Godliness -- A Divine Council Hymn?",
            "body": "The creedal fragment in 3:16 is one of the most compressed theological statements in "
                    "the New Testament. Paul introduces it with 'Great indeed, we confess, is the mystery "
                    "of godliness (mysterion tes eusebeias),' and then quotes what appears to be an early "
                    "Christian hymn: 'He was manifested in the flesh, vindicated by the Spirit, seen by "
                    "angels, proclaimed among the nations, believed on in the world, taken up in glory.' "
                    "The six lines move in three pairs that alternate between the earthly and the heavenly "
                    "realms: flesh/Spirit, angels/nations, world/glory. This rhythmic oscillation reflects "
                    "a cosmic perspective: the Christ event reverberates simultaneously in both the visible "
                    "and invisible worlds. The phrase 'seen by angels' (ophthe angelois) is particularly "
                    "significant for the divine council framework. The verb ophthe is the same word used "
                    "for Christ's resurrection appearances (1 Cor 15:5-8, 'he appeared to Cephas... then "
                    "to the twelve'). The divine council members -- angels, principalities, powers -- "
                    "witnessed the incarnation, death, resurrection, and ascension. They are not passive "
                    "bystanders: Ephesians 3:10 says that 'through the church the manifold wisdom of God "
                    "might now be made known to the rulers and authorities in the heavenly places.' The "
                    "gospel is a cosmic announcement that reaches every tier of the spiritual hierarchy."
        },
        {
            "type": "scholarship",
            "title": "The Pastoral Epistles Debate -- Why Scholars Question Authorship",
            "body": "The question of whether Paul actually wrote 1 Timothy (and 2 Timothy and Titus) is "
                    "one of the most significant authorship debates in New Testament scholarship. A non-"
                    "seminary reader encountering this for the first time should understand what is at stake "
                    "and why scholars disagree. The case against Pauline authorship rests on several "
                    "observations: (1) The Pastorals contain 306 words not found in Paul's undisputed letters "
                    "(Romans, 1-2 Corinthians, Galatians, Philippians, 1 Thessalonians, Philemon). (2) The "
                    "church organization described (bishops, deacons, elders with defined qualifications) "
                    "seems more developed than what Paul describes in his earlier letters. (3) The false "
                    "teaching combated resembles second-century Gnosticism more than first-century problems. "
                    "(4) The 'deposit' language (1:18; 6:20, 'guard the deposit') suggests a period of "
                    "preserving received tradition rather than the dynamic apostolic ministry of Paul's "
                    "earlier career. The case FOR Pauline authorship counters: (1) Vocabulary differences "
                    "are expected when writing about different subjects to different recipients. (2) Paul "
                    "typically used a secretary (amanuensis) whose own style influenced the Greek. (3) The "
                    "personal details (1:3, leaving Timothy at Ephesus; 5:23, drink a little wine for your "
                    "stomach) would be inexplicable in a pseudonymous letter. (4) Early church attestation "
                    "is unanimous. This study accepts Pauline authorship while acknowledging the debate "
                    "honestly."
        },
        {
            "type": "warning",
            "title": "Reading 1 Timothy in Cultural Context -- What Is Universal, What Is Situational?",
            "body": "1 Timothy contains some of the most debated passages in the NT regarding church "
                    "practice: instructions about women's roles (2:9-15), qualifications for overseers "
                    "and deacons (3:1-13), treatment of widows (5:3-16), and attitudes toward slavery "
                    "(6:1-2). These passages have been the source of intense disagreement across "
                    "Christian traditions. A responsible reader must distinguish between the theological "
                    "principles Paul is applying and the specific cultural forms through which he applies "
                    "them. The theological principle behind the leadership qualifications, for example, is "
                    "that church leaders must be morally above reproach and doctrinally sound -- a timeless "
                    "standard. The specific cultural form (e.g., 'husband of one wife,' 3:2) reflects "
                    "first-century household structures that looked different from modern Western families. "
                    "Similarly, the instruction about women (2:11-12) is interpreted differently by "
                    "complementarians (who see it as a permanent created-order principle) and egalitarians "
                    "(who see it as addressing a specific Ephesian situation involving unqualified women "
                    "teachers influenced by the false doctrine). Regardless of your interpretive tradition, "
                    "the key is to read 1 Timothy as a pastoral letter addressing a real crisis -- not as "
                    "an abstract rulebook dropped from the sky."
        }
    ]
}
