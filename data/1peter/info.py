"""
info.py -- 1 Peter: Scholarly Text Introduction

Peter writes to "elect exiles" scattered through Asia Minor. Contains one of the
most important divine council passages in the NT: Christ "went and proclaimed to
the spirits in prison" (3:19) -- the imprisoned Watchers of Genesis 6 -- and is
now "at the right hand of God, with angels, authorities, and powers having been
subjected to him" (3:22). The letter frames Christian suffering as participation
in Christ's suffering and cosmic victory.
"""

TEXT_INFO = {
    "text_id": "1peter",
    "display_name": "1 Peter",

    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / General Epistles",
        "detail": "1 Peter was universally accepted in the early church. Polycarp, Irenaeus, and Clement of "
                  "Alexandria all cite it. It appears in every ancient canon list. Its canonicity has never "
                  "been seriously disputed."
    },

    "authorship": {
        "traditional": "Simon Peter, the apostle, writing from 'Babylon' (5:13 -- likely a cipher for Rome) "
                       "'through Silvanus' (5:12 -- Silas, Paul's former companion, who may have served as "
                       "secretary and polished the Greek).",
        "scholarly_debate": "The excellent Greek style has led some scholars to question whether a Galilean "
                           "fisherman could write at this level. Defenses include: (1) Silvanus as amanuensis "
                           "could explain the polished Greek; (2) bilingualism was common in first-century "
                           "Galilee; (3) Peter had 30+ years of ministry in Greek-speaking contexts by this time.",
        "bottom_line": "Petrine authorship is accepted, likely with significant secretarial assistance from "
                       "Silvanus. The theology is consistent with the Peter of Acts and the Gospels."
    },

    "date": {
        "traditional": "62-64 AD, from Rome, before or during Nero's persecution.",
        "critical_range": "62-64 AD if Petrine; 80-90 AD if pseudonymous.",
        "evidence": "The letter addresses persecution that seems to be social ostracism and legal harassment "
                    "(not yet systematic state persecution), consistent with the early 60s AD. Peter was "
                    "martyred in Rome under Nero, traditionally dated c. 64-67 AD."
    },

    "audience": {
        "original_audience": "'The elect exiles of the Dispersion in Pontus, Galatia, Cappadocia, Asia, and "
                            "Bithynia' (1:1) -- Christians scattered across the Roman provinces of Asia Minor "
                            "(modern Turkey). The audience appears to be predominantly Gentile converts "
                            "(1:14, 18; 2:10; 4:3-4).",
        "purpose": "To encourage Christians facing suffering and social marginalization: their suffering is "
                   "temporary, their inheritance is imperishable, and their Lord has already triumphed over "
                   "all hostile powers.",
        "theological_intent": "The letter frames Christian identity through Israel's titles ('elect,' 'exiles,' "
                             "'royal priesthood,' 'holy nation') and grounds ethical behavior in Christ's "
                             "example of suffering followed by vindication. The cosmic scope is breathtaking: "
                             "Christ's victory extends not only to the living and dead but to the imprisoned "
                             "spiritual beings (3:19) and the subjugated cosmic powers (3:22)."
    },

    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Key terms: parepidemos (exile/sojourner -- 1:1; 2:11), eklektos (elect/chosen), "
                           "basileion hierateuma (royal priesthood -- 2:9), kerysso (to proclaim/herald -- "
                           "3:19, Christ's proclamation to the spirits), pneumasin en phylake (spirits in "
                           "prison -- 3:19), hypotasso (to subject/subordinate -- 3:22, powers subjected to "
                           "Christ), antidikos (adversary -- 5:8, the devil as opponent).",
        "grammar_match": "Polished, literary Greek with extensive OT quotation and imagery. Among the best "
                        "Greek in the NT, likely reflecting Silvanus's secretarial skill."
    },

    "scripture_alignment": {
        "verdict": "1 Peter is saturated with OT quotation and allusion, particularly from Isaiah (quoted "
                   "7+ times) and the Psalms. The letter reinterprets Israel's identity titles for the church.",
        "nt_usage": "Major OT citations: Isa 40:6-8 (1:24-25), Isa 28:16/Ps 118:22/Isa 8:14 (2:6-8), "
                    "Exod 19:5-6 (2:9), Isa 53:4-9 (2:22-25), Ps 34:12-16 (3:10-12), Prov 11:31 (4:18), "
                    "Prov 3:34 (5:5).",
        "internal_consistency": "Connects to 2 Peter (same author claims), Jude (parallel material on fallen "
                               "angels), Acts (Peter's sermons), and Paul's letters (Silvanus connection)."
    },

    "manuscripts": {
        "earliest": "P72 (3rd-4th century) -- contains 1 Peter complete.",
        "major_witnesses": [
            {"name": "P72", "date": "c. 300 AD", "note": "Complete text of 1 Peter (and 2 Peter, Jude)."},
            {"name": "Codex Vaticanus", "date": "c. 325-350 AD", "note": "Complete text."},
            {"name": "Codex Sinaiticus", "date": "c. 330-360 AD", "note": "Complete text."},
            {"name": "Codex Alexandrinus", "date": "c. 400-440 AD", "note": "Complete text."}
        ],
        "reliability": "Very well-preserved. P72 is one of the earliest complete NT manuscripts of any book."
    },

    "historical_context": {
        "setting": "Peter writes from 'Babylon' (5:13), almost certainly a cipher for Rome (as in Rev 14:8; "
                   "17:5; 18:2). The recipients face social ostracism and harassment for their faith.",
        "geography": "The five provinces listed (Pontus, Galatia, Cappadocia, Asia, Bithynia) cover most of "
                     "Asia Minor. The letter may have been carried by Silvanus along a circular route through "
                     "these provinces.",
        "historical_connections": "The suffering described (malignment, social exclusion, potential legal "
                                 "trouble) fits the period before Nero's systematic persecution. Christians "
                                 "were increasingly seen as socially deviant for refusing to participate in "
                                 "pagan religious and social practices."
    },

    "divine_council": {
        "relevance": "very high",
        "summary": "1 Peter contains one of the most significant divine council passages in the entire NT: "
                   "3:18-22. Christ, after being 'put to death in the flesh but made alive in the spirit,' "
                   "'went and proclaimed (ekeryksen) to the spirits in prison (pneumasin en phylake), because "
                   "they formerly did not obey, when God's patience waited in the days of Noah' (3:19-20). "
                   "These 'spirits' are the imprisoned Watchers of Genesis 6:1-4 / 1 Enoch 6-16 -- the fallen "
                   "sons of God who violated the cosmic boundary between heaven and earth. Christ's 'proclamation' "
                   "is a victory announcement: the plan they tried to corrupt has succeeded. He then ascended and "
                   "is 'at the right hand of God, with angels, authorities, and powers having been subjected to "
                   "him' (3:22). The entire hostile hierarchy of the divine council is now under Christ's "
                   "authority. Additionally, 1:12 notes that 'angels long to look into' the salvation revealed "
                   "to believers -- the faithful members of the council are fascinated by the unfolding plan. "
                   "And 5:8, 'Your adversary the devil prowls around like a roaring lion, seeking someone to "
                   "devour,' places believers in active spiritual warfare with the chief rebel.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 31 (Christ's proclamation to the imprisoned Watchers)",
            "The Unseen Realm, chapter 32 (the subjugation of cosmic powers at the ascension)",
            "Supernatural, chapter 13 (the spirits in prison and the Watcher tradition)",
            "The Naked Bible Podcast, episodes 148-150 (1 Peter 3:18-22 deep dive)"
        ]
    },

    "reader_notes": [
        {
            "type": "theology",
            "title": "The Spirits in Prison -- Christ's Victory Announcement to the Watchers",
            "body": "1 Peter 3:18-20 is one of the most debated passages in the NT. Christ 'went and proclaimed "
                    "(ekeryksen) to the spirits in prison (pneumasin en phylake), because they formerly did not "
                    "obey, when God's patience waited in the days of Noah.' Three questions must be answered: "
                    "(1) WHO are the spirits? The word pneuma ('spirit') is almost never used for dead humans "
                    "in the NT without qualification (e.g., 'spirits of the righteous,' Heb 12:23). The "
                    "identification 'spirits in prison' who 'did not obey in the days of Noah' points to the "
                    "Watchers tradition of 1 Enoch 6-16 and Genesis 6:1-4 -- the 'sons of God' (bene elohim) "
                    "who violated the cosmic boundary. 2 Peter 2:4 explicitly places these angels in 'chains "
                    "of darkness' (Tartarus), and Jude 6 describes angels who 'left their proper dwelling.' "
                    "(2) WHAT did Christ proclaim? The verb is kerysso (to herald/proclaim), not euangelizo (to "
                    "preach good news). Christ did not offer them salvation -- he announced his victory. The "
                    "plan they tried to corrupt by contaminating the human bloodline has succeeded: the Seed "
                    "of the woman (Gen 3:15) has come, died, risen, and conquered. (3) WHEN did this happen? "
                    "Most likely between Christ's death and resurrection (or at the ascension), when he passed "
                    "through the spiritual realm to announce his triumph over every hostile power."
        },
        {
            "type": "theology",
            "title": "Angels, Authorities, and Powers Subjected to Christ",
            "body": "1 Peter 3:22 declares that Christ 'has gone into heaven and is at the right hand of God, "
                    "with angels and authorities and powers having been subjected to him.' This is the cosmic "
                    "enthronement: the resurrected and ascended Christ now rules over the entire hierarchy of "
                    "spiritual beings. 'Angels' (angeloi), 'authorities' (exousiai), and 'powers' (dynameis) "
                    "are the standard NT terms for the ranks of the divine council (cf. Eph 1:21; Col 1:16; "
                    "Rom 8:38). The passive participle 'having been subjected' (hypotagenton) indicates this is "
                    "a completed reality: the subjugation has already happened at the ascension. This does not "
                    "mean the hostile powers have ceased to operate (5:8, the devil still prowls), but that "
                    "their authority has been broken and their ultimate defeat is certain."
        },
        {
            "type": "context",
            "title": "Elect Exiles -- Israel's Identity Transferred to the Church",
            "body": "Peter addresses his readers as 'elect exiles of the Dispersion' (1:1) and later calls them "
                    "'a chosen race, a royal priesthood, a holy nation, a people for his own possession' (2:9, "
                    "quoting Exod 19:5-6). These are Israel's covenant titles, now applied to a predominantly "
                    "Gentile audience. 'Once you were not a people, but now you are God's people' (2:10, quoting "
                    "Hosea 2:23). This transfer of identity is a divine council event: the nations that were "
                    "disinherited at Babel (Deut 32:8-9) and placed under the authority of the 'sons of God' "
                    "are now being reclaimed through the gospel. The 'elect exiles' are people drawn from the "
                    "disinherited nations, now incorporated into God's own people. They are 'exiles' because "
                    "they live in territories still under the influence of the hostile powers, awaiting the "
                    "completion of the reclamation at Christ's return."
        }
    ]
}
