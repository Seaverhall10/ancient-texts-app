"""
info.py -- 1 Thessalonians: Scholarly Text Introduction

Likely the earliest surviving Pauline letter (c. 49-51 AD), written to a young
church enduring persecution. Paul addresses the Thessalonians' anxiety about
believers who have died before Christ's return. The key divine council elements:
the archangel's call at Christ's descent (4:16), the day of the Lord coming
like a thief (5:2), and the cosmic transformation at the parousia.
"""

TEXT_INFO = {
    "text_id": "1thessalonians",
    "display_name": "1 Thessalonians",

    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Pauline Epistles",
        "detail": "1 Thessalonians is universally accepted as an authentic Pauline letter and may be "
                  "the earliest document in the NT. It is one of the undisputed Paulines, attested by "
                  "Irenaeus, Clement of Alexandria, and the Muratorian Canon."
    },

    "authorship": {
        "traditional": "Paul, Silvanus, and Timothy (1:1). Written from Corinth after Timothy returned "
                       "with good news from Thessalonica (3:6; cf. Acts 18:5).",
        "scholarly_debate": "No serious scholar disputes Pauline authorship. The only debate is whether "
                           "the 'anti-Jewish' polemic in 2:14-16 is a later interpolation; most scholars "
                           "retain it as Pauline, though the rhetoric is unusually harsh.",
        "bottom_line": "Paul wrote 1 Thessalonians from Corinth around 49-51 AD, making it likely the "
                       "earliest surviving Christian document."
    },

    "date": {
        "traditional": "49-51 AD, during Paul's second missionary journey, written from Corinth.",
        "critical_range": "49-51 AD. The Gallio inscription anchors Paul's Corinthian stay to 51-52 AD; "
                         "1 Thessalonians was likely written early in that period.",
        "evidence": "Paul had recently been in Thessalonica (Acts 17:1-9) and left under duress. Timothy "
                    "was sent back and has just returned (3:1-6). The letter reflects a very young church."
    },

    "audience": {
        "original_audience": "The church at Thessalonica, a major city on the Via Egnatia in the Roman "
                            "province of Macedonia (modern Thessaloniki, Greece). The congregation was "
                            "predominantly Gentile (1:9, 'you turned to God from idols').",
        "purpose": "Paul writes to (1) encourage the persecuted believers; (2) defend his ministry "
                   "against accusations of exploitation; (3) address anxiety about deceased believers -- "
                   "will they miss the parousia?; (4) urge holy living in preparation for the day of "
                   "the Lord.",
        "theological_intent": "The letter is dominated by eschatology: the parousia (coming) of Christ, "
                             "the resurrection of the dead, the archangel's call, and the day of the Lord. "
                             "Paul assures the Thessalonians that the dead in Christ will rise first."
    },

    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Key terms: parousia (coming/arrival/presence), koimaomai (to fall asleep -- "
                           "euphemism for death), archangelos (archangel -- only here and Jude 9 in NT), "
                           "salpinx theou (trumpet of God), hemera Kyriou (day of the Lord), harpazo (to "
                           "snatch/catch up -- source of 'rapture' concept).",
        "grammar_match": "Paul's Greek in 1 Thessalonians is warm and pastoral, with frequent terms "
                        "of endearment and emotional disclosure."
    },

    "scripture_alignment": {
        "verdict": "1 Thessalonians provides the earliest written teaching on the parousia, the "
                   "resurrection of believers, and the day of the Lord.",
        "nt_usage": "Paul draws on Jesus's own eschatological teaching (cf. Matt 24:30-31; John 5:28-29). "
                    "The 'day of the Lord' language comes from the OT prophetic tradition (Joel 2:1-2; "
                    "Amos 5:18-20; Zephaniah 1:14-18).",
        "internal_consistency": "The eschatology of 1 Thessalonians coheres with 1 Corinthians 15, "
                               "Philippians 3:20-21, and Romans 8:18-25."
    },

    "manuscripts": {
        "earliest": "P46 (c. 175-225 AD) contains 1 Thessalonians. P30 (3rd century) has fragments.",
        "major_witnesses": [
            {"name": "P46", "date": "c. 175-225 AD", "note": "Earliest substantial witness."},
            {"name": "Codex Sinaiticus", "date": "c. 330-360 AD", "note": "Complete text."},
            {"name": "Codex Vaticanus", "date": "c. 300-325 AD", "note": "Complete text."},
            {"name": "Codex Alexandrinus", "date": "c. 400-440 AD", "note": "Complete text."}
        ],
        "reliability": "Well-preserved with no major textual disputes."
    },

    "historical_context": {
        "setting": "Thessalonica was the capital of the Roman province of Macedonia, situated on the Via "
                   "Egnatia. It was a free city with its own politarchs (city officials, cf. Acts 17:6).",
        "geography": "Located at the head of the Thermaic Gulf in northern Greece. A major commercial "
                     "and administrative center.",
        "historical_connections": "Paul, Silas, and Timothy founded the church during the second missionary "
                                 "journey (Acts 17:1-9). They were forced to leave after accusations of "
                                 "proclaiming 'another king, Jesus' (Acts 17:7)."
    },

    "divine_council": {
        "relevance": "moderate",
        "summary": "1 Thessalonians contributes to divine council theology primarily through its "
                   "eschatology. The descent of the Lord 'with a cry of command, with the voice of an "
                   "archangel, and with the sound of the trumpet of God' (4:16) places the parousia in "
                   "a cosmic context. The archangel (archangelos -- likely Michael, cf. Dan 10:13, 21; "
                   "12:1; Jude 9) is a chief member of the divine council. The 'trumpet of God' echoes "
                   "the Sinai theophany (Exod 19:16, 19) and the eschatological trumpet traditions "
                   "(1 Cor 15:52; Matt 24:31). The 'day of the Lord' (hemera Kyriou, 5:2) is the OT "
                   "yom YHWH -- the day of divine judgment that the prophets warned about, now "
                   "reinterpreted as the day of Christ's return.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 38 (the parousia and the cosmic transformation)",
            "Angels: What the Bible Really Says, ch. 8 (Michael the archangel)",
            "The Naked Bible Podcast, episode 69 (the day of the Lord)"
        ]
    },

    "reader_notes": [
        {
            "type": "theology",
            "title": "The Archangel's Voice -- Michael at the Parousia",
            "body": "The 'voice of an archangel' (phone archangelou, 4:16) is significant. The term "
                    "'archangel' appears only here and in Jude 9 (where Michael is the archangel who "
                    "contends with the devil over Moses' body). In Daniel 10:13, 21 and 12:1, Michael is "
                    "'the great prince who has charge of your people' -- Israel's angelic guardian in the "
                    "divine council. At the end times, 'Michael shall arise' (Dan 12:1). Paul's parousia "
                    "scene includes this archangelic figure: Christ descends from heaven, the archangel "
                    "cries out, God's trumpet sounds, and the dead in Christ rise. This is a divine "
                    "council assembly scene -- the cosmic court convenes for the final act."
        },
        {
            "type": "context",
            "title": "The Dead in Christ -- Why Were They Worried?",
            "body": "The Thessalonians were distressed about believers who had died (4:13). Why? Because "
                    "Paul had taught them to expect Christ's imminent return, and they assumed the dead "
                    "would miss it. Paul reassures them: the dead in Christ will rise FIRST (4:16), then "
                    "the living will be 'caught up together with them in the clouds to meet the Lord in "
                    "the air' (4:17). The verb harpazo ('caught up/snatched') implies sudden, powerful "
                    "divine action. The phrase 'to meet' (eis apantesin) is a technical term for a civic "
                    "reception: when an emperor or dignitary approached a city, citizens went OUT to meet "
                    "him and escort him IN. The imagery is not believers flying away from earth but going "
                    "out to meet the descending Lord and accompanying him back."
        }
    ]
}
