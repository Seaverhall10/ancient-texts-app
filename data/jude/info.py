"""
info.py -- Jude: Scholarly Text Introduction

The most divine-council-saturated book in the NT. In just 25 verses, Jude
references: the fallen Watchers in eternal chains (v.6), Michael the archangel
disputing with the devil over Moses's body (v.9), the way of Cain, Balaam's
error, and Korah's rebellion (v.11), and directly quotes 1 Enoch 1:9 (vv.14-15).
Jude assumes his readers know the Watcher tradition and Second Temple literature.
"""

TEXT_INFO = {
    "text_id": "jude",
    "display_name": "Jude",

    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / General Epistles",
        "detail": "Jude's canonicity was debated in the early church precisely because it quotes 1 Enoch "
                  "(vv. 14-15) and alludes to the Assumption of Moses (v. 9). Some church fathers (Didymus, "
                  "Clement of Alexandria) accepted it enthusiastically; others were cautious. It was affirmed "
                  "at Hippo (393) and Carthage (397). Its inclusion is fully warranted: Jude provides the "
                  "most explicit divine council theology in the NT epistles."
    },

    "authorship": {
        "traditional": "Jude (Judas), 'a servant of Jesus Christ and brother of James' (v.1). This James "
                       "is almost certainly James the Just, leader of the Jerusalem church (Gal 1:19; Acts "
                       "15:13), which makes Jude a brother of Jesus (Matt 13:55; Mark 6:3). Note that Jude "
                       "does NOT call himself a brother of Jesus but a 'servant' (doulos) -- an extraordinary "
                       "act of humility from someone who grew up with Jesus.",
        "scholarly_debate": "Some scholars consider Jude pseudonymous, arguing the Greek is too polished for "
                           "a Palestinian Jew and the reference to 'the apostles of our Lord Jesus Christ' "
                           "(v.17) implies a later generation. Others defend the authorship: bilingualism was "
                           "common in Galilee, and the reference to apostles does not require temporal distance.",
        "bottom_line": "Jude the brother of Jesus is accepted as the author. The letter's familiarity with "
                       "Second Temple traditions (1 Enoch, the Assumption of Moses) is consistent with a "
                       "Palestinian Jewish-Christian author."
    },

    "date": {
        "traditional": "65-80 AD.",
        "critical_range": "65-80 AD if by Jude; 80-100 AD if pseudonymous.",
        "evidence": "The letter's relationship to 2 Peter is debated: most scholars think 2 Peter used Jude "
                    "as a source (nearly all of Jude's content appears in 2 Peter 2). If so, Jude is earlier. "
                    "The urgency and brevity suggest an early response to a specific crisis."
    },

    "audience": {
        "original_audience": "'Those who are called, beloved in God the Father and kept for Jesus Christ' "
                            "(v.1) -- a general Christian audience, location unspecified.",
        "purpose": "Jude intended to write about 'our common salvation' but was compelled instead to 'appeal "
                   "to you to contend for the faith that was once for all delivered to the saints' (v.3). "
                   "False teachers have 'crept in unnoticed' (v.4) -- antinomians who pervert grace into "
                   "license for immorality and 'deny our only Master and Lord, Jesus Christ.'",
        "theological_intent": "The letter uses three OT examples (the Exodus generation, the angels/Watchers, "
                             "Sodom and Gomorrah) and three character types (Cain, Balaam, Korah) to warn "
                             "that judgment is certain for those who rebel against God's established order. "
                             "The divine council framework is assumed throughout."
    },

    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Key terms: epagonizomai (to contend earnestly -- v.3), pareisduno (to slip in "
                           "unnoticed -- v.4, the false teachers' infiltration tactic), arche (own domain/ "
                           "position of authority -- v.6, which the angels abandoned), doxas (glorious ones/ "
                           "angelic beings -- v.8, which the false teachers blaspheme), psychikoi (sensual/ "
                           "worldly-minded -- v.19, people 'devoid of the Spirit').",
        "grammar_match": "Vivid, urgent Greek with extensive use of triplets (three OT examples, three "
                        "character types, three doxological attributes). The style is compact and allusive, "
                        "assuming familiarity with Second Temple literature."
    },

    "scripture_alignment": {
        "verdict": "Jude is the most important NT epistle for divine council theology. It directly quotes "
                   "1 Enoch and alludes to the Assumption of Moses, treating both as authoritative traditions "
                   "about the spiritual world.",
        "nt_usage": "OT and Second Temple allusions: Exodus 14/Num 14 (v.5, the Exodus generation), Gen 6:1-4 / "
                    "1 Enoch 6-16 (v.6, the fallen angels), Gen 19 (v.7, Sodom and Gomorrah), Assumption of "
                    "Moses (v.9, Michael vs. the devil), Gen 4 (v.11, Cain), Num 22-24 (v.11, Balaam), "
                    "Num 16 (v.11, Korah), 1 Enoch 1:9 (vv.14-15, direct quotation).",
        "internal_consistency": "Nearly all of Jude appears in 2 Peter 2 (either Jude used 2 Peter, or "
                               "more likely, 2 Peter used Jude). The Watcher tradition connects to Gen 6:1-4, "
                               "1 Peter 3:19-20, and 2 Peter 2:4."
    },

    "manuscripts": {
        "earliest": "P72 (3rd-4th century) -- contains the complete text of Jude (along with 1-2 Peter).",
        "major_witnesses": [
            {"name": "P72", "date": "c. 300 AD", "note": "Complete text; earliest witness. Part of the Bodmer miscellaneous codex."},
            {"name": "P78", "date": "c. 300 AD", "note": "Fragments of vv. 4-5, 7-8."},
            {"name": "Codex Vaticanus", "date": "c. 325-350 AD", "note": "Complete text."},
            {"name": "Codex Sinaiticus", "date": "c. 330-360 AD", "note": "Complete text."}
        ],
        "reliability": "Well-preserved. No major textual variants."
    },

    "historical_context": {
        "setting": "Unknown location. The false teachers have infiltrated the community and are promoting "
                   "moral license while participating in the community's love feasts (v.12).",
        "geography": "Unspecified. The letter's Palestinian Jewish background suggests the author is connected "
                     "to the Jerusalem church, but the audience could be anywhere.",
        "historical_connections": "Jude's use of 1 Enoch and the Assumption of Moses demonstrates that these "
                                 "Second Temple texts were known and valued in early Christian communities. The "
                                 "Ethiopian Orthodox Church includes 1 Enoch in its canon, partly because of "
                                 "Jude's endorsement. The early church's debate about Jude's canonicity was "
                                 "largely driven by uncertainty about the status of these extra-canonical sources."
    },

    "divine_council": {
        "relevance": "very high",
        "summary": "Jude is the most divine-council-saturated book in the NT epistles. In just 25 verses: "
                   "(1) FALLEN WATCHERS (v.6): 'Angels who did not stay within their own position of "
                   "authority (arche) but left their proper dwelling (oiketerion)' are kept 'in eternal "
                   "chains under gloomy darkness until the judgment of the great day.' This is a direct "
                   "reference to the Watcher tradition of 1 Enoch 6-16 / Genesis 6:1-4. (2) MICHAEL VS. "
                   "SATAN (v.9): 'Michael the archangel, when he was disputing with the devil about the "
                   "body of Moses, did not presume to pronounce a blasphemous judgment, but said, \"The Lord "
                   "rebuke you.\"' This comes from the lost Assumption of Moses and depicts a divine council "
                   "confrontation between the chief loyal angel and the chief rebel. (3) THREE REBEL TYPES "
                   "(v.11): the way of Cain (murder), Balaam's error (prophetic corruption for profit), and "
                   "Korah's rebellion (challenging God's appointed authority) -- three patterns of cosmic "
                   "rebellion. (4) 1 ENOCH QUOTED (vv.14-15): 'Enoch, the seventh from Adam, prophesied, "
                   "saying, \"Behold, the Lord comes with ten thousands of his holy ones, to execute judgment "
                   "on all.\"' This is 1 Enoch 1:9, quoted as prophecy. The 'ten thousands of holy ones' are "
                   "the members of the divine council accompanying God in judgment.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 12 (the Watcher rebellion -- Genesis 6 and 1 Enoch)",
            "The Unseen Realm, chapter 14 (the imprisonment of the Watchers)",
            "Supernatural, chapter 7 (Michael and Satan -- the divine council confrontation)",
            "The Naked Bible Podcast, episodes 94-95 (Jude and the divine council)",
            "Reversing Hermon, chapters 1-3 (the Watcher tradition Jude depends on)"
        ]
    },

    "reader_notes": [
        {
            "type": "theology",
            "title": "The Watchers -- Angels Who Left Their Proper Dwelling",
            "body": "Jude 6 describes 'angels who did not stay within their own position of authority (arche) "
                    "but left their proper dwelling (oiketerion).' They are kept 'in eternal chains under gloomy "
                    "darkness until the judgment of the great day.' This is a direct reference to the Watcher "
                    "tradition: the 'sons of God' (bene elohim) of Genesis 6:1-4 who descended from heaven, "
                    "took human wives, and produced the Nephilim. The punishment matches 1 Enoch 10:4-6, 12 "
                    "exactly: the Watchers were bound in darkness. Jude's language is precise: they left their "
                    "'arche' (domain/beginning/position of authority) -- they abandoned their assigned station "
                    "in the divine council hierarchy. They left their 'oiketerion' (dwelling/habitation) -- "
                    "they departed from heaven itself. Both words emphasize boundary violation: these beings "
                    "crossed the line between the heavenly and earthly realms, a transgression so severe that "
                    "they were permanently imprisoned."
        },
        {
            "type": "context",
            "title": "Michael vs. the Devil -- The Archangel's Restraint",
            "body": "Jude 9 recounts: 'Michael the archangel, when he was disputing with the devil about the "
                    "body of Moses, did not presume to pronounce a blasphemous judgment, but said, \"The Lord "
                    "rebuke you.\"' This episode comes from a lost work called the Assumption of Moses (or "
                    "Testament of Moses). The point is not about Moses's body per se but about authority: "
                    "even Michael, the highest-ranking loyal angel in the divine council (Dan 10:13, 21; 12:1; "
                    "Rev 12:7), did not exercise independent authority against the devil. He deferred to God: "
                    "'The Lord rebuke you.' If the archangel himself refuses to pronounce judgment on his own "
                    "authority, how much more arrogant are the false teachers who 'blaspheme the glorious ones' "
                    "(v.8) -- mocking the angelic beings they do not understand? Michael's restraint models "
                    "proper authority: derived from God, not seized by the creature."
        },
        {
            "type": "interpretation",
            "title": "Jude Quotes 1 Enoch -- What Does This Mean?",
            "body": "Jude 14-15 directly quotes 1 Enoch 1:9: 'Enoch, the seventh from Adam, prophesied, "
                    "saying, \"Behold, the Lord comes with ten thousands of his holy ones, to execute judgment "
                    "on all.\"' Jude introduces this as 'prophecy' (proepheteusen). Does this make 1 Enoch "
                    "'Scripture'? Not necessarily -- Paul quotes pagan poets (Acts 17:28; Titus 1:12) without "
                    "canonizing them. But Jude does use the word 'prophesied,' which is a stronger claim than "
                    "mere citation. At minimum, Jude treats the 1 Enoch tradition as containing genuine, "
                    "authoritative information about the spiritual world. The 'ten thousands of his holy ones' "
                    "are the members of the divine council: God comes for judgment accompanied by his heavenly "
                    "army (cf. Deut 33:2; Dan 7:10; Zech 14:5; Matt 25:31). The Ethiopian Orthodox Church "
                    "includes 1 Enoch in its biblical canon, partly because of Jude's endorsement."
        }
    ]
}
