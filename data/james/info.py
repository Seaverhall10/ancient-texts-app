"""
info.py -- James: Scholarly Text Introduction

The letter of James, the brother of Jesus, to "the twelve tribes in the
Dispersion." A fiercely practical letter: faith without works is dead (2:26),
the tongue is a fire (3:6), demons believe and shudder (2:19), and the wisdom
from above is contrasted with wisdom that is "earthly, unspiritual, demonic" (3:15).
"""

TEXT_INFO = {
    "text_id": "james",
    "display_name": "James",

    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / General Epistles",
        "detail": "James was debated in antiquity (Eusebius listed it among the 'disputed' books), and Luther "
                  "famously called it an 'epistle of straw.' However, it was accepted at the councils of "
                  "Hippo (393) and Carthage (397) and has been part of the NT canon ever since. Its inclusion "
                  "is fully warranted: James does not contradict Paul but addresses a different problem (dead "
                  "orthodoxy vs. legalism)."
    },

    "authorship": {
        "traditional": "James, the brother of Jesus (Matt 13:55; Mark 6:3; Gal 1:19), who became the leader "
                       "of the Jerusalem church (Acts 15:13; 21:18; Gal 2:9). He was not one of the Twelve "
                       "but became an apostle after the resurrection (1 Cor 15:7).",
        "scholarly_debate": "Some scholars argue the letter is pseudonymous, pointing to its excellent Greek "
                           "(could a Galilean write this well?) and apparent tension with Paul on faith and "
                           "works. Others defend James's authorship: bilingualism was common in Galilee, the "
                           "theology reflects a very early, pre-Pauline stage of Christianity, and the letter "
                           "contains no hint of the post-70 AD situation.",
        "bottom_line": "James the brother of Jesus is accepted as the author. The letter may be one of the "
                       "earliest NT documents, possibly predating Paul's letters."
    },

    "date": {
        "traditional": "45-49 AD, possibly the earliest NT document, written before the Jerusalem Council (Acts 15).",
        "critical_range": "45-49 AD if by James (before his martyrdom in 62 AD); 80-100 AD if pseudonymous.",
        "evidence": "The letter shows no awareness of the Pauline controversy over faith and works (suggesting "
                    "it predates Paul's letters), no mention of the Jerusalem Council, and a very Jewish-Christian "
                    "perspective. James was martyred in 62 AD (Josephus, Antiquities 20.9.1)."
    },

    "audience": {
        "original_audience": "'The twelve tribes in the Dispersion' (1:1) -- Jewish Christians scattered "
                            "outside Palestine, possibly after the persecution of Acts 8:1.",
        "purpose": "To exhort scattered Jewish Christians to live out their faith through practical obedience: "
                   "enduring trials (1:2-4), controlling the tongue (3:1-12), caring for the poor (2:1-7), and "
                   "producing 'works' that demonstrate genuine faith (2:14-26).",
        "theological_intent": "James's central concern is that faith must produce visible results. 'Faith by "
                             "itself, if it does not have works, is dead' (2:17). This does not contradict "
                             "Paul's justification by faith: Paul argues against earning salvation by law-keeping; "
                             "James argues against a dead faith that produces no transformation. Both agree that "
                             "genuine faith transforms behavior."
    },

    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Key terms: pistis (faith -- used 16x, always as active trust, not mere intellectual "
                           "assent), erga (works -- practical deeds of obedience), peirasmos (trial/testing), "
                           "dipsychos (double-minded -- literally 'double-souled,' unique to James in the NT "
                           "[1:8; 4:8]), sophia anothen (wisdom from above), epigeios, psychike, daimoniodes "
                           "(earthly, unspiritual/soulish, demonic -- three-level taxonomy of false wisdom [3:15]).",
        "grammar_match": "James's Greek is among the best in the NT: polished, rhetorical, with extensive use "
                        "of vivid metaphors (mirror, sea waves, fire, horse bits, ship rudders, spring waters)."
    },

    "scripture_alignment": {
        "verdict": "James is deeply rooted in the OT wisdom tradition (Proverbs, Sirach) and in the teaching "
                   "of Jesus (especially the Sermon on the Mount). Over 50 parallels to Jesus's teaching have "
                   "been identified.",
        "nt_usage": "James quotes or alludes to: Gen 15:6 (2:23, Abraham believed God), Gen 22 (2:21, the "
                    "offering of Isaac), Josh 2 (2:25, Rahab), Prov 3:34 (4:6, God opposes the proud), "
                    "Lev 19:18 (2:8, 'love your neighbor').",
        "internal_consistency": "James shares vocabulary and themes with 1 Peter and the Sermon on the Mount. "
                               "The faith-works teaching complements (not contradicts) Romans 3-4 and "
                               "Galatians 2-3."
    },

    "manuscripts": {
        "earliest": "P20 (3rd century, fragments of 2:19-3:9), P23 (3rd century, fragments of 1:10-12, 15-18).",
        "major_witnesses": [
            {"name": "P20", "date": "c. 250 AD", "note": "Fragments of 2:19-3:9."},
            {"name": "P23", "date": "c. 250 AD", "note": "Fragments of 1:10-12, 15-18."},
            {"name": "Codex Sinaiticus", "date": "c. 330-360 AD", "note": "Complete text."},
            {"name": "Codex Vaticanus", "date": "c. 325-350 AD", "note": "Complete text."}
        ],
        "reliability": "Well-preserved with few significant variants."
    },

    "historical_context": {
        "setting": "Jerusalem, where James led the church. The recipients are Jewish Christians scattered "
                   "throughout the Mediterranean world.",
        "geography": "The Dispersion (diaspora) refers to Jewish communities outside Palestine. James "
                     "addresses a network of house churches throughout the Roman Empire.",
        "historical_connections": "James the Just was known for his piety even among non-Christian Jews. "
                                 "Josephus records his execution by stoning in 62 AD under the high priest "
                                 "Ananus (Antiquities 20.9.1). Hegesippus (c. 180 AD) records that James was "
                                 "known as 'the Just' and spent so much time in prayer that 'his knees became "
                                 "hard like those of a camel.'"
    },

    "divine_council": {
        "relevance": "moderate",
        "summary": "James contains two significant divine council connections: (1) 'You believe that God is "
                   "one; you do well. Even the demons believe -- and shudder!' (2:19). The demons (daimonia) "
                   "are members of the fallen heavenly host who recognize God's sovereignty but rebel against "
                   "it; mere belief without obedience is demonic faith. (2) 'The wisdom from above is first "
                   "pure, then peaceable... but the wisdom that does not come down from above is earthly, "
                   "unspiritual (psychike), demonic (daimoniodes)' (3:15-17). James presents a three-level "
                   "taxonomy of false wisdom: earthly (human), unspiritual (soulish, lacking the Spirit), "
                   "and demonic (originating from hostile spiritual beings). This parallels Paul's 'doctrines "
                   "of demons' (1 Tim 4:1) -- false wisdom has a spiritual source.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 35 (demonic influence on human thought and culture)",
            "Supernatural, chapter 19 (the demonic dimension of false teaching)"
        ]
    },

    "reader_notes": [
        {
            "type": "theology",
            "title": "Faith and Works -- James vs. Paul?",
            "body": "The apparent contradiction between James ('a person is justified by works and not by faith "
                    "alone,' 2:24) and Paul ('a person is justified by faith apart from works of the law,' "
                    "Rom 3:28) has troubled readers since Luther. The resolution lies in recognizing they address "
                    "different problems with different definitions: Paul's 'works' are 'works of the law' (Torah "
                    "observance as a means of earning righteousness); James's 'works' are 'deeds of mercy and "
                    "obedience' that demonstrate living faith. Paul's 'faith' is genuine trust in Christ; James's "
                    "target is 'faith' as mere intellectual assent ('the demons believe,' 2:19). Both agree: "
                    "genuine faith in Christ produces transformed behavior. Paul says: 'faith working through love' "
                    "(Gal 5:6); James says: 'faith apart from works is dead' (2:26). The 'contradiction' evaporates "
                    "when you see they are standing back-to-back, fighting different enemies."
        },
        {
            "type": "interpretation",
            "title": "Earthly, Unspiritual, Demonic -- The Three-Level Taxonomy of False Wisdom",
            "body": "James 3:15 presents a remarkable taxonomy of wisdom that does not come 'from above.' It is: "
                    "(1) epigeios (earthly) -- rooted in the fallen world system, limited to human perspective; "
                    "(2) psychike (unspiritual/soulish) -- from psyche, the 'soul' or natural life; it operates "
                    "without the Holy Spirit's illumination; the same word Paul uses in 1 Cor 2:14 ('the natural "
                    "person does not accept the things of the Spirit of God'); (3) daimoniodes (demonic) -- "
                    "originating from demons; the deepest source of false wisdom is not human error but demonic "
                    "influence. This three-level descent (earthly -> soulish -> demonic) reveals that what appears "
                    "as merely 'worldly' thinking may have a spiritual source. The 'wisdom from above' (3:17) is "
                    "contrasted as 'pure, peaceable, gentle, open to reason, full of mercy and good fruits, "
                    "impartial and sincere.' The test of wisdom's source is its fruit."
        }
    ]
}
