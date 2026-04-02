"""
era_3john_leadership.py -- 3 John: Kingdom Leadership and the Sin of Preeminence

Two chapters examining the character paradigms of 3 John:
(1) Gaius and Demetrius as models of faithful kingdom leadership.
(2) Diotrephes as the embodiment of divine council rebellion in church form.

ERA_ID: 3john_leadership
"""

ERA_ID = "3john_leadership"

CHAPTERS = [
    # ================================================================
    # CHAPTER 1: Gaius, Demetrius, and the Character Test
    # ================================================================
    {
        "id": "3john-leadership-01",
        "ref": "3 John 1-8, 11-12",
        "chapter_num": 2,
        "title": "Gaius, Demetrius, and the Character Test",
        "era": "3john_leadership",
        "type": "study",
        "themes": ["KING", "HOLY", "NATIONS"],

        "synopsis": (
            "Third John presents three men as paradigms of kingdom leadership. Gaius "
            "receives missionaries at personal cost, supporting strangers for the sake of the Name "
            "(vv. 5-8). Demetrius has 'received a good testimony from everyone, and from the truth "
            "itself' (v. 12) — triple-witness commendation. Together they embody what Jesus described "
            "in Matthew 25:21: 'Well done, good and faithful servant.' The character test for leadership "
            "in the divine council's economy is not gifting, eloquence, or institutional authority — it "
            "is faithfulness in service, hospitality toward the mission, and a reputation established "
            "by converging testimony. These men represent the pattern of the loyal council member: one "
            "who executes the sovereign's will without grasping for personal power. They are 'fellow "
            "workers for the truth' (synergoi tē alētheia, v. 8) — participants in the divine mission "
            "through ordinary acts of generosity and integrity."
        ),

        "key_verse": {
            "ref": "3 John 11",
            "text": "Beloved, do not imitate evil but imitate good. Whoever does good is from God; whoever does evil has not seen God.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "martyreō (Greek: martyreō)",
                "transliteration": "martyreō",
                "meaning": (
                    "To testify, bear witness, give evidence. Used throughout the letter for the "
                    "testimony borne about people's character. The brothers 'testified to your truth' "
                    "(v. 3 — about Gaius). Demetrius has 'received a good testimony from everyone' "
                    "(v. 12). In the Johannine framework, martyria (testimony/witness) is how truth "
                    "is established. A person's character is known not by self-promotion but by the "
                    "converging witness of the community, the truth itself, and the apostolic leadership. "
                    "This triple-witness pattern echoes Deuteronomy 19:15 ('on the evidence of two or "
                    "three witnesses') and the threefold witness of 1 John 5:7-8."
                )
            },
            {
                "term": "alētheia (Greek: alētheia)",
                "transliteration": "alētheia",
                "meaning": (
                    "Truth, reality, what accords with fact. Appears six times in 15 verses — the "
                    "densest concentration of 'truth' per word in the NT. Gaius 'walks in truth' (v. 3). "
                    "The missionaries go out 'for the sake of the Name' (v. 7). Supporters become 'fellow "
                    "workers FOR the truth' (v. 8). Demetrius is commended 'by the truth itself' (v. 12). "
                    "In the Johannine community, alētheia is not mere factual accuracy but the reality of "
                    "God's character and governance — how things actually are in the divine order. Walking "
                    "in truth means living aligned with cosmic reality."
                )
            },
            {
                "term": "synergoi (Greek: synergoi)",
                "transliteration": "synergoi",
                "meaning": (
                    "Fellow workers, co-laborers. From syn ('together') + ergon ('work'). By supporting "
                    "missionaries materially, Gaius becomes a synergos — a genuine co-worker in the "
                    "mission. He does not need to travel to participate in the gospel's advance. His "
                    "hospitality IS his mission work. This term elevates material support from charity "
                    "to partnership: the one who gives and the one who goes are equally participants "
                    "in the work."
                )
            },
            {
                "term": "kalos poieō (Greek: kalos poieō)",
                "transliteration": "kalos poieō",
                "meaning": (
                    "To do well, to do rightly, to do a fine/noble thing. Used in v. 6: 'You will do "
                    "well (kalos poiēseis) to send them on their journey in a manner worthy of God.' "
                    "Kalos means not just 'good' in a moral sense but 'beautiful, noble, admirable.' "
                    "Hospitality done 'worthily of God' (axios tou theou) is kalos — it is a beautiful "
                    "act that reflects God's own generosity. The verb reappears in v. 11: 'whoever does "
                    "good (agathopoiōn) is from God' — the origin determines the quality of the action."
                )
            },
            {
                "term": "axios tou theou (Greek: axios tou theou)",
                "transliteration": "axios tou theou",
                "meaning": (
                    "In a manner worthy of God. The standard for hospitality is not social convention "
                    "but divine character. To send missionaries on their way 'worthy of God' means "
                    "with the generosity, thoroughness, and joy that reflect God's own nature. The "
                    "standard is not 'adequate' or 'sufficient' but 'godlike.' This phrase transforms "
                    "hospitality from a social obligation into an act of imitatio Dei — imitation of God."
                )
            }
        ],

        "ane_backdrop": (
            "In the ancient Mediterranean world, honor and shame were the primary social "
            "currencies. A person's reputation (timē) was established through public testimony — "
            "what others said about you in the community. Letters of recommendation were crucial "
            "for traveling teachers (cf. 2 Corinthians 3:1) because they established a person's "
            "character through the witness of trusted community members. Demetrius's triple "
            "testimony (from everyone, from the truth, from the Elder) follows this pattern "
            "perfectly. The ancient church adopted the legal principle of multiple witnesses "
            "(Deuteronomy 19:15) for character assessment: no single testimony was sufficient; "
            "converging witnesses established reliability."
        ),

        "second_temple": [
            {
                "source": "1 Timothy 3:1-7",
                "summary": "Paul's elder qualifications: 'above reproach, the husband of one wife, "
                           "sober-minded, self-controlled, respectable, hospitable, able to teach, not "
                           "a drunkard, not violent but gentle, not quarrelsome, not a lover of money... "
                           "He must be well thought of by outsiders.'",
                "relevance": "The elder qualifications in the Pastoral Epistles provide the checklist "
                            "that Gaius and Demetrius embody: hospitality, good reputation, gentleness, "
                            "and faithfulness. Diotrephes fails virtually every criterion.",
                "canon": "canonical"
            },
            {
                "source": "Titus 1:5-9",
                "summary": "Paul instructs Titus to appoint elders who are 'above reproach... hospitable, "
                           "a lover of good, self-controlled, upright, holy, and disciplined.'",
                "relevance": "The qualifications center on character, not charisma. The 'lover of good' "
                            "(philagathon) stands in direct contrast to Diotrephes as the 'lover of "
                            "preeminence' (philoproteuōn). Love of good vs. love of power.",
                "canon": "canonical"
            }
        ],

        "cross_refs": [
            {"ref": "1 Timothy 3:1-7", "note": "Elder qualifications: 'above reproach, hospitable, "
             "well thought of by outsiders' — the checklist Gaius and Demetrius exemplify", "type": "nt"},
            {"ref": "Titus 1:5-9", "note": "Elders must be 'hospitable, a lover of good' (philagathon) "
             "— the opposite of Diotrephes's philoproteuōn (lover of preeminence)", "type": "nt"},
            {"ref": "Matthew 25:21", "note": "'Well done, good and faithful servant. You have been "
             "faithful over a little; I will set you over much' — the commendation Gaius and Demetrius "
             "model: faithfulness in ordinary service", "type": "nt"},
            {"ref": "Hebrews 13:2", "note": "'Do not neglect to show hospitality to strangers, for "
             "thereby some have entertained angels unawares' — hospitality to strangers as Gaius practices", "type": "nt"},
            {"ref": "Philippians 2:3-4", "note": "'Do nothing from selfish ambition or conceit, but "
             "in humility count others more significant than yourselves' — the servant-leadership pattern", "type": "nt"},
            {"ref": "Psalm 15:1-5", "note": "'O LORD, who shall sojourn in your tent? Who shall dwell "
             "on your holy hill? He who walks blamelessly and does what is right' — the character test "
             "for dwelling in God's presence", "type": "ot"}
        ],

        "divine_council_note": (
            "Gaius and Demetrius represent the pattern of the loyal divine council member: "
            "one who executes the sovereign's will without grasping for personal glory. In the "
            "council framework, faithful elohim carry out their assigned roles — they do not "
            "compete for higher positions or refuse to serve when the mission requires it. The "
            "'character test' of 3 John is ultimately a reflection of the character test applied "
            "to the divine council itself. The Watchers failed: they abandoned their assigned "
            "domain (Jude 6). The 'gods' of Psalm 82 failed: they judged unjustly and showed "
            "partiality. Diotrephes fails the same test in the church. But Gaius passes: he "
            "serves strangers at personal cost, asks nothing in return, and receives commendation "
            "from the apostolic authority. Demetrius passes: his testimony comes from three "
            "converging sources — the community, the truth, and the Elder. The pattern of "
            "faithful divine council membership is faithfulness, not fame; service, not "
            "self-promotion; testimony from others, not self-declaration."
        ),

        "sections": [
            {
                "title": "Gaius: The Model of Faithful Service (vv. 1-8)",
                "verses": "3 John 1-8",
                "content": (
                    "The Elder's love for Gaius is unmistakable: 'the beloved Gaius, whom I love "
                    "in truth' (v. 1). Four times in fifteen verses, Gaius is called 'beloved' "
                    "(agapētos) — the highest relational term in the Johannine vocabulary. The "
                    "Elder's prayer reveals Gaius's situation: 'I pray that all may go well with "
                    "you and that you may be in good health, as it goes well with your soul' (v. 2). "
                    "His spiritual health outpaces his physical circumstances.\n\n"
                    "Gaius's distinguishing characteristic is hospitality to strangers: 'It is a "
                    "faithful thing you do in all your efforts for these brothers, strangers as they "
                    "are' (v. 5). The word 'strangers' (xenoi) is significant — Gaius does not "
                    "restrict his generosity to people he knows. He supports missionaries on the "
                    "basis of their mission, not personal relationship. This is covenantal generosity "
                    "— giving because of shared allegiance to the King, not because of social "
                    "networking.\n\n"
                    "The missionaries go out 'for the sake of the Name, accepting nothing from the "
                    "Gentiles' (v. 7). Their refusal of outside funding creates a practical necessity: "
                    "the believing community must support them. By doing so, Gaius becomes a 'fellow "
                    "worker for the truth' (synergos tē alētheia, v. 8). <em>His hospitality is not "
                    "merely kindness — it is mission participation. He advances the truth by funding "
                    "its messengers.</em>"
                ),
                "key_terms": [
                    {"term": "agapētos (beloved)", "definition": "Used four times for Gaius — the "
                     "highest relational term, signaling deep personal affection and covenantal bond."},
                    {"term": "xenoi (strangers)", "definition": "Missionaries unknown to Gaius "
                     "personally. His hospitality extends beyond social circles to anyone sent for "
                     "the Name's sake."},
                    {"term": "synergoi tē alētheia (fellow workers for the truth)", "definition": "By "
                     "providing material support, local believers become co-laborers in the mission."}
                ]
            },
            {
                "title": "Demetrius: The Triple Witness (vv. 11-12)",
                "verses": "3 John 11-12",
                "content": (
                    "'Beloved, do not imitate evil but imitate good. Whoever does good is from God; "
                    "whoever does evil has not seen God' (v. 11). This verse is the theological pivot "
                    "between the Diotrephes warning and the Demetrius commendation. The Christian "
                    "life is fundamentally imitative (mimeomai): we are called to follow patterns "
                    "(Eph 5:1, 1 Cor 11:1). The question is which pattern: Diotrephes (self-exaltation) "
                    "or Gaius/Demetrius (faithful service)?\n\n"
                    "Demetrius receives the strongest character endorsement in the letter: 'Demetrius "
                    "has received a good testimony from everyone, and from the truth itself. We also "
                    "add our testimony, and you know that our testimony is true' (v. 12). Three "
                    "witnesses converge: (1) <strong>Everyone</strong> — the universal testimony of "
                    "the community. (2) <strong>The truth itself</strong> — his life aligns with "
                    "reality; the way he lives testifies to the truth independent of anyone's "
                    "opinion. (3) <strong>The Elder</strong> — apostolic authority adds personal "
                    "endorsement.\n\n"
                    "This triple witness echoes the legal standard of Deuteronomy 19:15 ('on the "
                    "evidence of two or three witnesses') and the three witnesses of 1 John 5:7-8. "
                    "Demetrius may be the letter carrier or a missionary whom the Elder is "
                    "commending to Gaius's hospitality. Either way, his character has been tested "
                    "and validated from every angle. <em>In the divine council framework, character "
                    "is established by testimony, not self-declaration. The faithful council member "
                    "is known by the witness of others, not by his own claims.</em>"
                ),
                "key_terms": [
                    {"term": "mimeomai (to imitate)", "definition": "The Christian life as pattern-"
                     "following: imitate God (Eph 5:1), imitate Christ (1 Cor 11:1), imitate faithful "
                     "leaders (Heb 13:7)."},
                    {"term": "martyria (testimony/witness)", "definition": "Character is established "
                     "by converging witnesses. Demetrius receives triple testimony — the strongest "
                     "possible endorsement in the Johannine community."},
                    {"term": "ek tou theou (from God)", "definition": "Origin determines character. "
                     "Doing good reveals divine origin; doing evil reveals alienation from God."}
                ]
            }
        ]
    },
    # ================================================================
    # CHAPTER 2: Diotrephes and the Love of Preeminence
    # ================================================================
    {
        "id": "3john-leadership-02",
        "ref": "3 John 9-11",
        "chapter_num": 3,
        "title": "Diotrephes and the Love of Preeminence",
        "era": "3john_leadership",
        "type": "study",
        "themes": ["REBEL", "DC", "KING"],

        "synopsis": (
            "Diotrephes is described with a single devastating word that appears nowhere else in "
            "the entire Greek Bible: philoproteuōn — 'loving to be first' (v. 9). This hapax "
            "legomenon was coined or selected to capture the specific pathology of ecclesiastical "
            "power abuse. Diotrephes does not merely hold authority — he loves authority. He does "
            "not merely lead — he grasps for preeminence. His actions form a pattern of total "
            "power consolidation: he rejects the Elder's authority (v. 9), slanders the Elder "
            "with malicious nonsense (v. 10), refuses to welcome missionaries (v. 10), and expels "
            "anyone who dares to practice hospitality (v. 10). In the divine council framework, "
            "this is the pattern of the rebellious elohim: the Watchers who abandoned their "
            "assigned domain, the 'gods' of Psalm 82 who abused their delegated authority, the "
            "nachash who grasped for 'being like the Most High' (Isa 14:14). Diotrephes enacts "
            "in a local church what the rebellious spiritual powers enacted on the cosmic stage: "
            "authority corrupted by self-love, service replaced by dominance, the mission "
            "subordinated to personal power."
        ),

        "key_verse": {
            "ref": "3 John 9-10",
            "text": "I have written something to the church, but Diotrephes, who likes to put himself first, does not acknowledge our authority. So if I come, I will bring up what he is doing, talking wicked nonsense against us. And not content with that, he refuses to welcome the brothers, and also stops those who want to and puts them out of the church.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "philoproteuō (Greek: philoproteuō)",
                "transliteration": "philoproteuō",
                "meaning": (
                    "To love being first, to desire preeminence. A compound from phileō ('to love') + "
                    "proteuō ('to be first, to hold first place'). This word is a NT hapax legomenon — "
                    "it appears ONLY in 3 John 9, nowhere else in the entire Greek Bible (NT or LXX). "
                    "Its uniqueness is itself significant: John reached for a word that existed nowhere "
                    "in the scriptural vocabulary to capture Diotrephes's specific sin. The compound "
                    "structure is damning: the problem is not that Diotrephes holds a position of "
                    "leadership (proteuō is used positively for Christ in Col 1:18: 'that in everything "
                    "he might be preeminent'). The problem is that he LOVES it (phileō). His affection "
                    "is directed not toward God or the community but toward his own primacy."
                )
            },
            {
                "term": "ekballō ek tēs ekklēsias (Greek: ekballō ek tēs ekklēsias)",
                "transliteration": "ekballō ek tēs ekklēsias",
                "meaning": (
                    "To cast out of the assembly, to expel from the church. Diotrephes 'puts them out "
                    "of the church' (v. 10) — he excommunicates anyone who practices hospitality to "
                    "the Elder's missionaries. This weaponizes church discipline: the mechanism designed "
                    "to protect the community from sin (Matt 18:17, 1 Cor 5:13) is used to punish "
                    "faithfulness. The verb ekballō is strong — the same word used for casting out "
                    "demons (Mark 1:34). Diotrephes casts out the faithful as though they were the "
                    "unclean."
                )
            },
            {
                "term": "ponēros (Greek: ponēros)",
                "transliteration": "ponēros",
                "meaning": (
                    "Evil, wicked, malicious. Diotrephes's words against the Elder are 'wicked "
                    "nonsense' (logois ponērois phlyrōn, v. 10). The adjective ponēros is the same "
                    "word used throughout the Johannine writings for 'the evil one' (ho ponēros, "
                    "1 John 2:13-14, 3:12, 5:18-19). When Diotrephes speaks 'wicked words,' he "
                    "participates in the vocabulary and character of the evil one himself. His "
                    "slander is not merely interpersonal conflict — it aligns him with the cosmic "
                    "adversary."
                )
            },
            {
                "term": "phlyrareō (Greek: phlyrareō)",
                "transliteration": "phlyrareō",
                "meaning": (
                    "To babble, to talk nonsense, to bring false charges. Used in v. 10 for "
                    "Diotrephes's verbal attacks against the Elder. The word implies not just "
                    "disagreement but baseless, malicious verbal assault — empty words designed "
                    "to destroy reputation. It is related to phlyaros ('babbling, gossip') in "
                    "1 Timothy 5:13. Diotrephes does not engage the Elder's arguments — he "
                    "character-assassinates him through nonsensical slander."
                )
            },
            {
                "term": "epidechomai (Greek: epidechomai)",
                "transliteration": "epidechomai",
                "meaning": (
                    "To receive, welcome, accept. Used twice: 'Diotrephes does not receive us' "
                    "(v. 9) and 'he refuses to welcome the brothers' (v. 10). The prefix epi- "
                    "intensifies: this is not passive neglect but active, deliberate refusal. "
                    "Diotrephes turns the hospitality gate into a power mechanism — controlling "
                    "access to the community as a means of controlling the community itself."
                )
            }
        ],

        "ane_backdrop": (
            "Power concentration in religious leadership was a recognized problem in the ancient "
            "world. The Qumran community (Dead Sea Scrolls) had strict authority structures "
            "precisely to prevent individuals from seizing unilateral control. The 'Teacher of "
            "Righteousness' at Qumran operated within a council structure, not as a sole "
            "authority. Greek political philosophy (Aristotle, Politics) distinguished between "
            "legitimate authority (exercised for the community's benefit) and tyranny (authority "
            "exercised for the ruler's benefit). Diotrephes represents the tyrannical model: "
            "authority that serves the leader rather than the community. In Jewish tradition, "
            "Korah's rebellion (Numbers 16) was the paradigmatic example of unauthorized power-"
            "grasping — and Korah's fate (the earth swallowing him alive) served as a permanent "
            "warning against those who challenged divinely-appointed authority structures."
        ),

        "second_temple": [
            {
                "source": "Numbers 16 (Korah's Rebellion)",
                "summary": "Korah gathered 250 leaders and challenged Moses and Aaron: 'You have "
                           "gone too far! For all in the congregation are holy, every one of them, "
                           "and the LORD is among them. Why then do you exalt yourselves above the "
                           "assembly of the LORD?' The earth opened and swallowed them.",
                "relevance": "Korah used egalitarian language ('all are holy') to mask personal "
                            "ambition — exactly what Diotrephes does. Both men position themselves "
                            "as champions of the community while actually seeking their own power. "
                            "Jude 11 calls this pattern 'Korah's rebellion.'",
                "canon": "canonical"
            },
            {
                "source": "Isaiah 14:13-14",
                "summary": "'I will ascend to heaven... I will set my throne on high... I will "
                           "make myself like the Most High.'",
                "relevance": "Whether referring to the king of Babylon or the rebellious divine "
                            "being behind him, the 'I will' declarations capture the core sin: "
                            "self-exaltation to the place that belongs to God. Diotrephes's "
                            "philoproteuōn is the ecclesiastical version of 'I will make myself "
                            "like the Most High.'",
                "canon": "canonical"
            },
            {
                "source": "Ezekiel 34:1-10 (Indictment of Israel's Shepherds)",
                "summary": "'Ah, shepherds of Israel who have been feeding yourselves! Should not "
                           "shepherds feed the sheep? You eat the fat, you clothe yourselves with "
                           "the wool, you slaughter the fat ones, but you do not feed the sheep.'",
                "relevance": "God's indictment of Israel's leaders who exploit rather than serve "
                            "their flock. Diotrephes follows this pattern: using his position to "
                            "feed himself (love of preeminence) while scattering the sheep (expelling "
                            "faithful members).",
                "canon": "canonical"
            }
        ],

        "cross_refs": [
            {"ref": "3 John 9-10", "note": "The primary text: Diotrephes loves preeminence, rejects "
             "apostolic authority, slanders the Elder, blocks missionaries, and expels dissenters", "type": "nt"},
            {"ref": "Mark 10:42-45", "note": "'Whoever would be great among you must be your servant, "
             "and whoever would be first among you must be slave of all. For even the Son of Man came "
             "not to be served but to serve' — the direct rebuke to philoproteuōn", "type": "nt"},
            {"ref": "Revelation 2-3", "note": "Christ's letters to seven churches address leadership "
             "failures: Ephesus (abandoned first love), Pergamum (tolerated false teaching), Thyatira "
             "(allowed Jezebel), Sardis (dead reputation), Laodicea (lukewarm self-sufficiency)", "type": "nt"},
            {"ref": "Ezekiel 34:1-10", "note": "'Shepherds of Israel who feed themselves' — the OT "
             "indictment of leaders who exploit their flock instead of serving it", "type": "ot"},
            {"ref": "Philippians 2:5-8", "note": "Christ 'did not count equality with God a thing to "
             "be grasped, but emptied himself, taking the form of a servant' — the anti-Diotrephes: "
             "one who had every right to primacy but chose servanthood", "type": "nt"},
            {"ref": "1 Peter 5:1-4", "note": "'Shepherd the flock of God... not domineering over "
             "those in your charge, but being examples to the flock' — Peter's direct prohibition "
             "of the Diotrephes pattern", "type": "nt"},
            {"ref": "Numbers 16:1-35", "note": "Korah's rebellion — the OT paradigm for unauthorized "
             "power-grasping that Diotrephes replicates in the church", "type": "ot"}
        ],

        "divine_council_note": (
            "Diotrephes embodies the sin that defines every rebellious member of the divine "
            "council: the love of preeminence. The Watchers were not content with their heavenly "
            "station — they descended to take what was not theirs (Gen 6:1-4, 1 Enoch 6-16, "
            "Jude 6). The 'gods' of Psalm 82 used their delegated authority over the nations "
            "for self-aggrandizement rather than justice. The nachash in Eden grasped for 'being "
            "like the Most High' (Isa 14:14) — philoproteuōn in its cosmic form.\n\n"
            "Diotrephes replicates this pattern at the local church level. He rejects the "
            "Elder's authority (rejecting the chain of command, as the Watchers rejected theirs). "
            "He slanders the Elder (speaking 'wicked words,' aligning with ho ponēros). He "
            "blocks the missionaries (preventing the divine mission from advancing). He expels "
            "the faithful (punishing those who obey God rather than him). Every action mirrors "
            "the rebellious divine council pattern: authority turned inward, mission subordinated "
            "to power, the community weaponized for the leader's benefit.\n\n"
            "Christ's declaration in Mark 10:42-45 is the divine antidote: 'Whoever would be "
            "first among you must be slave of all.' The one who had legitimate claim to cosmic "
            "preeminence (Col 1:18) chose servanthood (Phil 2:5-8). Diotrephes, who has no "
            "legitimate claim to preeminence, grasps for it. The contrast could not be sharper. "
            "In the divine council's economy, authority flows downward through service; in the "
            "rebellious pattern, it is hoarded upward through domination."
        ),

        "sections": [
            {
                "title": "Philoproteuōn: The Hapax Legomenon of Self-Exaltation (v. 9)",
                "verses": "3 John 9",
                "content": (
                    "'I have written something to the church, but Diotrephes, who loves to be first "
                    "among them, does not acknowledge our authority' (v. 9). The word "
                    "<strong>philoproteuōn</strong> appears nowhere else in the Greek Bible — not in "
                    "the NT, not in the LXX. John reached for a word that had never been used in "
                    "Scripture to capture this particular sin.\n\n"
                    "The compound is surgical: phileō ('to love, to have affection for') + proteuō "
                    "('to be first, to hold preeminence'). The problem is not leadership itself. "
                    "Christ holds legitimate preeminence: 'that in everything he might be preeminent' "
                    "(proteuōn, Col 1:18). The problem is LOVING preeminence — having one's deepest "
                    "affection directed not toward God or the community but toward one's own primacy.\n\n"
                    "Diotrephes 'does not acknowledge' (ouk epidechetai) the Elder's authority. "
                    "The verb epidechomai means 'to receive, welcome, accept.' Diotrephes actively "
                    "refuses to recognize the apostolic chain of authority. He has made himself "
                    "the final authority in his congregation, accountable to no one. <em>This is "
                    "the structural sin of the rebellious elohim: claiming autonomous authority "
                    "in a system designed for delegated service.</em>"
                ),
                "key_terms": [
                    {"term": "philoproteuōn", "definition": "A hapax legomenon — appears only here "
                     "in the entire Greek Bible. 'Loving to be first.' The sin is not holding "
                     "authority but loving authority for its own sake."},
                    {"term": "ouk epidechetai", "definition": "Does not receive/acknowledge. Active "
                     "refusal of apostolic authority — not ignorance but deliberate rejection."}
                ]
            },
            {
                "title": "The Four Actions of Ecclesiastical Tyranny (v. 10)",
                "verses": "3 John 10",
                "content": (
                    "'So if I come, I will bring up what he is doing' (v. 10a). The Elder announces "
                    "pastoral accountability — Diotrephes may dominate locally, but he cannot escape "
                    "the Elder's authority when the Elder arrives in person. Then the four actions:\n\n"
                    "<strong>1. Slander</strong>: 'talking wicked nonsense against us' (logois "
                    "ponērois phlyrōn). The word phlyrōn means 'babbling, bringing false charges.' "
                    "The adjective ponēros ('wicked') connects Diotrephes's speech to 'the evil one' "
                    "(ho ponēros). His words are not just wrong — they are aligned with cosmic evil.\n\n"
                    "<strong>2. Rejection</strong>: 'he refuses to welcome the brothers' (ouk "
                    "epidechetai tous adelphous). He blocks the missionaries from entering his "
                    "congregation, cutting off the community from apostolic connection.\n\n"
                    "<strong>3. Obstruction</strong>: 'stops those who want to' (tous boulomenous "
                    "kōlyei). He prevents OTHER members from practicing hospitality. The tyranny "
                    "extends beyond his own actions to controlling the actions of others.\n\n"
                    "<strong>4. Expulsion</strong>: 'puts them out of the church' (ek tēs ekklēsias "
                    "ekballei). He excommunicates the faithful. The mechanism designed to protect the "
                    "community from sin is weaponized to punish obedience.\n\n"
                    "<em>Together, these four actions constitute total power consolidation: control "
                    "the narrative (slander), control access (rejection), control behavior "
                    "(obstruction), and punish dissent (expulsion). This is the complete toolkit "
                    "of authoritarian leadership — and it mirrors the cosmic pattern of the "
                    "rebellious powers who control nations through deception, exclusion, and fear.</em>"
                ),
                "key_terms": [
                    {"term": "logois ponērois phlyrōn", "definition": "Talking wicked nonsense — "
                     "malicious, baseless slander. The word ponēros connects to 'the evil one.'"},
                    {"term": "kōlyei (stops/prevents)", "definition": "Active obstruction of others' "
                     "faithfulness. Diotrephes does not merely refuse hospitality himself — he "
                     "prevents others from practicing it."},
                    {"term": "ekballei ek tēs ekklēsias", "definition": "Casts out of the assembly. "
                     "The same verb used for casting out demons — Diotrephes casts out the faithful "
                     "as though they were the unclean."}
                ]
            },
            {
                "title": "Imitate Good, Not Evil: The Binary Choice (v. 11)",
                "verses": "3 John 11",
                "content": (
                    "'Beloved, do not imitate evil but imitate good. Whoever does good is from God; "
                    "whoever does evil has not seen God' (v. 11). This single verse is the theological "
                    "summary of the entire letter. It presents a binary: two patterns, two origins, "
                    "two destinations.\n\n"
                    "The verb mimeomai ('to imitate') means to follow a pattern, to model one's "
                    "behavior on an exemplar. Gaius and Demetrius provide the pattern of good — "
                    "faithful service, hospitality, truth-walking. Diotrephes provides the pattern "
                    "of evil — self-exaltation, slander, exclusion.\n\n"
                    "The criterion is origin: 'whoever does good is FROM GOD' (ek tou theou estin). "
                    "The one who practices the servant-authority pattern reveals their divine origin. "
                    "'Whoever does evil has NOT SEEN GOD' (ouch heōraken ton theon). Diotrephes, "
                    "for all his ecclesiastical power, has never truly encountered the God whose "
                    "authority is exercised through service. <em>If he had seen God, he would not "
                    "grasp for preeminence — because the God he would have seen is the one who "
                    "emptied himself and took the form of a servant (Phil 2:7).</em>\n\n"
                    "The Johannine 'family test' (1 John 3:10) applies: children of God are known "
                    "by their actions. Those who imitate good reveal their divine parentage. Those "
                    "who imitate evil reveal that they belong to a different family entirely — the "
                    "family of the rebellious powers who have never submitted to God's servant-"
                    "authority model."
                ),
                "key_terms": [
                    {"term": "mimeomai (to imitate)", "definition": "To follow a pattern. The "
                     "Christian life is defined by which model you copy: Gaius or Diotrephes."},
                    {"term": "ek tou theou (from God)", "definition": "Origin determines character. "
                     "Good actions reveal divine origin; evil actions reveal alienation from God."},
                    {"term": "ouch heōraken ton theon (has not seen God)", "definition": "The one "
                     "who practices evil has never encountered the true God. Encountering God "
                     "transforms — if Diotrephes had seen God, he would serve, not dominate."}
                ]
            }
        ]
    }
]
