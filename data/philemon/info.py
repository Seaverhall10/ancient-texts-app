"""
info.py -- Philemon: Scholarly Text Introduction

Paul's shortest letter, written from prison to Philemon about his runaway slave
Onesimus who has become a Christian. A masterpiece of persuasion that subverts
the Roman institution of slavery from within by the logic of the gospel:
"no longer as a bondservant but more than a bondservant, as a beloved brother" (v.16).
"""

TEXT_INFO = {
    "text_id": "philemon",
    "display_name": "Philemon",

    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Pauline Epistles",
        "detail": "Philemon is virtually undisputed as authentically Pauline. Its brevity, personal nature, "
                  "and lack of significant theological controversy make it one of the least contested letters "
                  "in the Pauline corpus."
    },

    "authorship": {
        "traditional": "Paul the Apostle, writing from prison (v.1, 9-10, 13, 23) to Philemon, a wealthy "
                       "Christian in Colossae. Timothy is co-sender (v.1).",
        "scholarly_debate": "Almost universally accepted as genuinely Pauline. The personal, concrete details "
                           "and the situation described are difficult to explain as pseudonymous fiction.",
        "bottom_line": "Pauline authorship is undisputed. The letter is a window into Paul's pastoral practice "
                       "and social ethics."
    },

    "date": {
        "traditional": "60-62 AD, during Paul's first Roman imprisonment (same period as Colossians, "
                       "Ephesians, and Philippians).",
        "critical_range": "60-62 AD. The connection to Colossians (Onesimus appears in Col 4:9) confirms "
                         "the dating.",
        "evidence": "Paul is a prisoner (v.1, 9, 13, 23). The letter was likely carried with Colossians "
                    "by Onesimus and Tychicus (Col 4:7-9)."
    },

    "audience": {
        "original_audience": "Philemon, a wealthy Christian in Colossae (or possibly Laodicea), and the "
                            "church that meets in his house (v.2). Also addressed: Apphia (possibly "
                            "Philemon's wife) and Archippus (possibly his son or the church's minister).",
        "purpose": "To persuade Philemon to receive back his runaway slave Onesimus, now a Christian "
                   "convert, 'no longer as a bondservant but more than a bondservant, as a beloved brother' "
                   "(v.16). Paul subtly but powerfully undermines the institution of slavery by redefining "
                   "the master-slave relationship through the gospel.",
        "theological_intent": "The letter demonstrates the social implications of the gospel: in Christ, "
                             "all human hierarchies are relativized. Philemon is asked to act 'of your own "
                             "free will' (v.14), not by apostolic command -- the gospel transforms from "
                             "within, not by external force."
    },

    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Key terms: adelphos agapetos (beloved brother -- v.16), koinonia (partnership/ "
                           "fellowship -- v.6, 17), onaimen (I want benefit -- v.20, a play on the name "
                           "Onesimus which means 'useful/profitable'), achreston/euchreston (useless/useful "
                           "-- v.11, another wordplay on Onesimus's name), parrhesia (boldness/confidence -- "
                           "v.8).",
        "grammar_match": "Personal, warm, and rhetorically sophisticated despite its brevity. Paul employs "
                        "classical rhetorical techniques: ethos (v.8-9), pathos (v.10-12), logos (v.15-17)."
    },

    "scripture_alignment": {
        "verdict": "Philemon demonstrates the practical outworking of Paul's theological principle that "
                   "'there is neither slave nor free... for you are all one in Christ Jesus' (Gal 3:28).",
        "nt_usage": "No direct OT quotations, but the theology of reconciliation (2 Cor 5:18-20) and "
                    "the new creation (2 Cor 5:17) are applied to a concrete social situation.",
        "internal_consistency": "Closely connected to Colossians (same companions mentioned: Onesimus, "
                               "Epaphras, Mark, Aristarchus, Demas, Luke). Onesimus appears in Col 4:9 as "
                               "'one of you' -- confirming the Colossian setting."
    },

    "manuscripts": {
        "earliest": "Codex Sinaiticus (c. 330-360 AD). P87 (3rd century) preserves fragments of vv. 13-15, 24-25.",
        "major_witnesses": [
            {"name": "P87", "date": "c. 250 AD", "note": "Earliest witness; fragments of vv. 13-15, 24-25."},
            {"name": "Codex Sinaiticus", "date": "c. 330-360 AD", "note": "Complete text."},
            {"name": "Codex Alexandrinus", "date": "c. 400-440 AD", "note": "Complete text."}
        ],
        "reliability": "Very well-preserved. No significant textual variants."
    },

    "historical_context": {
        "setting": "Paul is in prison (probably Rome, c. 60-62 AD). Onesimus, a slave belonging to "
                   "Philemon in Colossae, has apparently run away and somehow come into contact with Paul. "
                   "Paul has led Onesimus to faith in Christ.",
        "geography": "Colossae was a small city in the Lycus Valley of Phrygia (western Asia Minor), near "
                     "Laodicea and Hierapolis. By Paul's time it was declining in importance.",
        "historical_connections": "Roman slavery was a complex institution. A fugitive slave (fugitivus) "
                                 "could face severe punishment including branding, beating, or death. By "
                                 "sending Onesimus back with this letter, Paul navigates Roman law while "
                                 "subverting the institution from within. Some scholars suggest Onesimus may "
                                 "not have 'run away' but deliberately sought Paul as a mediator (amicus "
                                 "domini -- a friend of the master who could intercede), which was a legal "
                                 "option for slaves in Roman law."
    },

    "divine_council": {
        "relevance": "low",
        "summary": "Philemon's divine council connections are indirect but theologically significant. The "
                   "letter demonstrates the gospel's power to transform earthly hierarchies: the 'brother' "
                   "relationship in Christ supersedes the master-slave relationship. In the divine council "
                   "framework, this reflects the new-creation reality: the cosmic reconciliation accomplished "
                   "by Christ (Col 1:20, 'reconciling to himself all things, whether on earth or in heaven') "
                   "has social consequences. When Paul says 'if he has wronged you at all, or owes you "
                   "anything, charge that to my account' (v.18), he models Christ's substitutionary work -- "
                   "taking another's debt upon himself.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 37 (the new creation and reversal of the Fall's consequences)"
        ]
    },

    "reader_notes": [
        {
            "type": "theology",
            "title": "Paul's Rhetorical Masterpiece -- Persuasion Without Command",
            "body": "Philemon is a case study in apostolic persuasion. Paul could 'command' Philemon to do what "
                    "is right (v.8) but chooses to 'appeal' (parakaleo, v.9-10) instead. He calls himself 'Paul, "
                    "an old man and now a prisoner also for Christ Jesus' (v.9) -- evoking sympathy. He calls "
                    "Onesimus 'my child... whose father I became in my imprisonment' (v.10) -- evoking paternal "
                    "love. He plays on Onesimus's name: 'Formerly he was useless (achrestos) to you, but now "
                    "he is indeed useful (euchrestos) to you and to me' (v.11) -- the name 'Onesimus' means "
                    "'useful/profitable.' He sends Onesimus back as 'my very heart' (v.12). He offers to pay "
                    "any debt (v.18-19) while subtly reminding Philemon: 'you owe me even your own self' (v.19). "
                    "The public address (to Philemon AND the church) ensures social accountability. Every move "
                    "is calculated to make refusal impossible while preserving Philemon's free agency."
        },
        {
            "type": "context",
            "title": "Slavery and the Gospel -- Subversion from Within",
            "body": "Paul does not directly attack the institution of slavery in Philemon, which has troubled "
                    "modern readers. But the logic of the letter is deeply subversive: Paul asks Philemon to "
                    "receive Onesimus 'no longer as a bondservant but more than a bondservant, as a beloved "
                    "brother -- especially to me, but how much more to you, both in the flesh and in the Lord' "
                    "(v.16). The phrase 'both in the flesh and in the Lord' means the brother-relationship is "
                    "not merely spiritual but extends to the earthly/social realm. Paul asks Philemon to "
                    "receive Onesimus 'as you would receive me' (v.17) -- that is, as an apostle. The "
                    "theological principle (Gal 3:28, 'neither slave nor free... all one in Christ') is being "
                    "applied to a concrete case. The seed planted here would eventually destroy the institution "
                    "it was planted within."
        }
    ]
}
