"""
era_62.py -- Theophany & Restoration (Job 38-42)

The climax of the book. YHWH speaks from the whirlwind -- not to explain
Job's suffering but to reveal the staggering scope of cosmic governance.
Two divine speeches: the first (38-39) tours the cosmos from creation
foundations to wild animals; the second (40-41) confronts Job with Behemoth
and Leviathan, chaos creatures that only God can master. Job repents -- not
of sin but of speaking beyond his knowledge. The epilogue vindicates Job
against the friends and restores him double.
"""

CHAPTERS = [
    {
        "id": "job-38-39",
        "ref": "Job 38-39",
        "chapter_num": 38,
        "title": "YHWH's First Speech -- The Cosmic Tour",
        "era": "62",
        "type": "chapter",
        "themes": ["DC", "GLORY", "PROV", "SPIRIT"],

        "synopsis": "YHWH answers Job 'out of the whirlwind' (38:1) -- the storm Elihu described has "
                    "arrived, and it carries God's voice. YHWH's response is not what anyone expected: "
                    "no explanation of Job's suffering, no verdict on the friends' theology, no "
                    "acknowledgment of ha-Satan's challenge. Instead, YHWH takes Job on a tour of the "
                    "cosmos, asking questions Job cannot answer. 'Where were you when I laid the "
                    "foundation of the earth?' (38:4). 'Who determined its measurements?' (38:5). "
                    "'When the morning stars sang together and all the sons of God shouted for joy?' "
                    "(38:7). The questions sweep through creation: the sea, the dawn, the storehouses "
                    "of snow and hail, the constellations, the clouds, the lions, the mountain goats, "
                    "the wild donkey, the ostrich, the war horse, the hawk, the eagle. The implicit "
                    "argument: the universe operates on a scale of complexity that human moral "
                    "categories cannot contain. YHWH governs a cosmos Job cannot even begin to "
                    "comprehend.",

        "key_verse": {
            "ref": "Job 38:4, 7",
            "text": "Where were you when I laid the foundation of the earth?... when the morning stars sang together and all the sons of God shouted for joy?",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "seara (whirlwind/tempest -- the medium of YHWH's theophanic appearance)",
            "kokhve voqer (morning stars -- celestial beings who witnessed creation, parallel to bene elohim)",
            "bene elohim (sons of God -- the divine council present at creation)",
            "mazzarot (constellations -- possibly the Zodiac signs, showing YHWH's governance of the celestial order)",
            "chokhmah (wisdom -- placed in the ibis and rooster as evidence of divine design in nature, 38:36)"
        ],

        "ane_backdrop": "YHWH's first speech draws on the same cosmic imagery found in ANE creation "
                        "texts but subordinates all of it to the sole Creator. The 'foundations of the "
                        "earth' (38:4) and 'cornerstone' (38:6) use architectural language common in "
                        "Mesopotamian temple-building texts, where the earth is God's temple. The 'sea' "
                        "being confined behind doors (38:8-11) echoes the Enuma Elish's division of "
                        "Tiamat's waters but without any combat -- YHWH simply sets boundaries. The "
                        "constellations (38:31-33) -- Pleiades, Orion, Mazzaroth, the Bear -- were "
                        "significant in Babylonian astral religion, but here they are merely objects "
                        "of YHWH's governance. The wild animal catalogue (38:39-39:30) is unique in "
                        "ANE literature: no other text uses the diversity of creation as an argument "
                        "for divine sovereignty.",

        "second_temple": [
            {
                "source": "4Q303-305 (Meditation on Creation from Qumran)",
                "summary": "Fragmentary texts contemplating the order and purpose of creation, "
                           "meditating on God's wisdom displayed in the natural order.",
                "relevance": "Shows that the Qumran community engaged in the same kind of "
                             "creation-theology contemplation that YHWH's speech models."
            },
            {
                "source": "Sirach 42:15-43:33",
                "summary": "A creation hymn praising God's works: the sun, moon, stars, rainbow, "
                           "snow, lightning, and sea. 'We could say more but could never say enough; "
                           "let the final word be: He is the all' (43:27).",
                "relevance": "The closest Second Temple parallel to YHWH's creation tour in "
                             "Job 38-39, expressing the same theme of divine grandeur beyond "
                             "human comprehension."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 104:1-35", "note": "The great creation psalm -- celebrates the same cosmic phenomena YHWH catalogues in Job 38-39", "type": "ot"},
            {"ref": "Proverbs 8:22-31", "note": "Wisdom present at creation when God 'marked out the foundations of the earth' -- the same scene as Job 38:4-7", "type": "ot"},
            {"ref": "Genesis 1:1-2:3", "note": "The creation narrative YHWH's speech presupposes and expands upon", "type": "ot"},
            {"ref": "Romans 11:33-36", "note": "'Oh, the depth of the riches and wisdom and knowledge of God! How unsearchable his judgments!' -- Paul's doxology echoes YHWH's point in Job 38", "type": "nt"},
            {"ref": "Isaiah 40:12-31", "note": "'Who has measured the waters in the hollow of his hand?' -- the same rhetorical strategy as YHWH's questions", "type": "ot"}
        ],

        "divine_council_note": "Job 38:7 is one of the most important divine council verses in the Bible: "
                               "'When the morning stars (kokhve voqer) sang together and all the sons of God "
                               "(bene elohim) shouted for joy.' The parallelism identifies the 'morning "
                               "stars' with the 'sons of God' -- both are terms for divine council members. "
                               "They witnessed creation and celebrated it with music and praise. This "
                               "establishes that the divine council existed before the physical cosmos -- "
                               "they are not products of creation but witnesses to it. The same bene "
                               "elohim who appeared in the divine council scene of Job 1:6 were present "
                               "when YHWH laid the foundations of the earth. YHWH's question to Job -- "
                               "'Where were you?' -- implicitly contrasts Job's absence with the council's "
                               "presence. Job was not there; the council was.",

        "sections": [
            {
                "heading": "YHWH Appears from the Whirlwind (38:1-3)",
                "body": "The theophany opens with majestic simplicity: 'Then YHWH answered Job out of the "
                        "whirlwind (seara)' (38:1). The seara is the classic vehicle of divine appearance: "
                        "YHWH approaches in storm power (cf. Nahum 1:3; Ezekiel 1:4; Psalm 18:7-15). The "
                        "first words are a challenge: 'Who is this that darkens counsel by words without "
                        "knowledge?' (38:2). YHWH acknowledges that Job has been speaking ('words') but "
                        "declares they lack knowledge. The demand: 'Dress for action like a man; I will "
                        "question you, and you make it known to me' (38:3). The Hebrew 'gird up your "
                        "loins' (ezor na kechallatsekha) is the language of preparation for battle or "
                        "difficult labor. God will ask the questions; Job must answer."
            },
            {
                "heading": "Creation's Foundations and the Sons of God (38:4-11)",
                "body": "YHWH begins with the earth's creation: 'Where were you when I laid the foundation "
                        "of the earth? Tell me, if you have understanding. Who determined its measurements?' "
                        "(38:4-5). The architectural metaphors -- foundations, measurements, bases, "
                        "cornerstone -- depict creation as temple construction (cf. Isaiah 28:16). Then the "
                        "stunning divine council reference: 'When the morning stars sang together and all "
                        "the sons of God shouted for joy' (38:7). Creation was a cosmic celebration "
                        "attended by the heavenly assembly. The sea's birth is described as YHWH wrapping "
                        "it in swaddling cloths and setting its limits: 'Thus far shall you come, and no "
                        "farther, and here shall your proud waves be stayed' (38:11). The sea -- symbol "
                        "of chaos in ANE mythology -- is merely an infant God contains."
            },
            {
                "heading": "The Tour of Cosmic Phenomena (38:12-38)",
                "body": "YHWH's questions sweep through the cosmos. Has Job commanded the dawn (38:12)? "
                        "Has he entered the springs of the sea or walked the recesses of the deep (38:16)? "
                        "Have the gates of death been revealed to him (38:17)? Can he bind the chains of "
                        "the Pleiades or loose the cords of Orion (38:31)? Can he 'lead forth the "
                        "Mazzaroth (constellations) in their season' (38:32)? Each question reveals "
                        "another dimension of cosmic governance that operates entirely without human "
                        "input or comprehension. The storehouses of snow and hail are reserved 'for the "
                        "time of trouble, for the day of battle and war' (38:22-23) -- even weather has "
                        "military purpose in God's administration."
            },
            {
                "heading": "The Wild Animal Catalogue (38:39-39:30)",
                "body": "YHWH transitions from inanimate creation to the animal kingdom, but these are "
                        "specifically wild animals -- creatures that serve no human purpose and operate "
                        "entirely outside human control. Who provides for the lions (38:39-40)? Who feeds "
                        "the ravens (38:41)? When do the mountain goats give birth (39:1)? The wild donkey "
                        "(39:5-8) was given freedom by God -- 'I have given the wild donkey the steppe for "
                        "his home.' The ostrich 'leaves her eggs to the earth' and 'deals cruelly with "
                        "her young' (39:13-16), yet God designed her that way. The war horse (39:19-25) "
                        "charges into battle without fear. The hawk and eagle soar at God's command "
                        "(39:26-30). The point is profound: God's governance includes creatures and systems "
                        "that have nothing to do with human moral categories. The universe is not designed "
                        "around human experience."
            }
        ]
    },

    {
        "id": "job-40-41",
        "ref": "Job 40-41",
        "chapter_num": 40,
        "title": "YHWH's Second Speech -- Behemoth and Leviathan",
        "era": "62",
        "type": "chapter",
        "themes": ["DC", "GLORY", "REBEL", "SPIRIT"],

        "synopsis": "After Job's brief response ('I lay my hand on my mouth,' 40:4), YHWH speaks again "
                    "from the whirlwind with an even more direct challenge: 'Will you even put me in the "
                    "wrong? Will you condemn me that you may be in the right? Have you an arm like God, "
                    "and can you thunder with a voice like his?' (40:8-9). YHWH then introduces two "
                    "creatures: Behemoth (40:15-24) and Leviathan (41:1-34). Behemoth is a land creature "
                    "of immense power: 'He eats grass like an ox... his bones are tubes of bronze, his "
                    "limbs like bars of iron' (40:15, 18). Leviathan is a sea creature that breathes fire, "
                    "cannot be captured, and is 'king over all the sons of pride' (41:34). These are not "
                    "merely large animals -- their descriptions transcend any natural creature. They "
                    "represent the forces of chaos that only YHWH can master. The implicit argument: Job "
                    "cannot handle Leviathan; how can he challenge Leviathan's master?",

        "key_verse": {
            "ref": "Job 41:10-11",
            "text": "No one is so fierce that he dares to stir him up. Who then is he who can stand before me? Who has first given to me, that I should repay him? Whatever is under the whole heaven is mine.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "behemoth (intensive plural of behemah/beast -- the supreme land creature, possibly supernatural)",
            "Leviathan (livyatan -- the chaos sea serpent, cognate with Ugaritic Litanu)",
            "tannin (sea monster/dragon -- related to Leviathan in the ANE chaos-monster tradition)",
            "malkhut (kingship -- Leviathan is 'king over all the sons of pride,' a cosmic sovereign of chaos)"
        ],

        "ane_backdrop": "Leviathan (livyatan) is cognate with the Ugaritic Litanu, the seven-headed chaos "
                        "serpent that Baal defeats in the Baal Cycle: 'When you smote Litanu the fleeing "
                        "serpent, made an end of the twisted serpent, the tyrant with seven heads' (KTU "
                        "1.5 I:1-3). Isaiah 27:1 uses nearly identical language: 'YHWH will punish "
                        "Leviathan the fleeing serpent, Leviathan the twisting serpent.' Psalm 74:13-14 "
                        "recounts how God 'crushed the heads of Leviathan.' In Job 41, YHWH does not "
                        "describe defeating Leviathan but rather controlling him -- the creature exists "
                        "under YHWH's sovereign governance. Behemoth may correspond to the 'Bull of "
                        "Heaven' in the Gilgamesh Epic or other ANE land-monster traditions. Together, "
                        "Behemoth (land) and Leviathan (sea) represent the totality of chaotic power "
                        "that only God can manage.",

        "second_temple": [
            {
                "source": "1 Enoch 60:7-10, 24",
                "summary": "Behemoth and Leviathan are described as primordial creatures separated on "
                           "the fifth day of creation: Leviathan dwelling in the sea and Behemoth in "
                           "an invisible desert east of Eden. They will be food for the righteous at "
                           "the eschatological banquet.",
                "relevance": "1 Enoch's tradition interprets Behemoth and Leviathan as literal "
                             "supernatural creatures with eschatological significance, preserving the "
                             "cosmic reading that Job 40-41 suggests."
            },
            {
                "source": "4 Ezra 6:49-52",
                "summary": "On the fifth day, God created Behemoth and Leviathan and separated them "
                           "because the world could not hold them together.",
                "relevance": "Confirms the Second Temple tradition of Behemoth and Leviathan as "
                             "primordial creatures of cosmic significance."
            },
            {
                "source": "2 Baruch 29:4",
                "summary": "Behemoth and Leviathan will be food for the messianic banquet: 'Behemoth "
                           "shall be revealed from his place and Leviathan shall ascend from the sea, "
                           "those two great monsters which I created on the fifth day of creation.'",
                "relevance": "The eschatological defeat and consumption of the chaos creatures "
                             "represents the ultimate triumph of God's order over chaos."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 74:13-14", "note": "'You crushed the heads of Leviathan; you gave him as food for the creatures of the wilderness' -- YHWH's past defeat of the chaos monster", "type": "ot"},
            {"ref": "Isaiah 27:1", "note": "'YHWH will punish Leviathan the fleeing serpent... and he will slay the dragon that is in the sea' -- the eschatological destruction", "type": "ot"},
            {"ref": "Revelation 12:7-9", "note": "The great dragon cast down -- the NT's final engagement with the chaos monster tradition", "type": "nt"},
            {"ref": "Revelation 13:1-2", "note": "The beast from the sea -- Leviathan imagery in John's apocalyptic vision", "type": "nt"},
            {"ref": "Romans 11:35", "note": "Paul quotes Job 41:11: 'Who has first given to me, that I should repay him?'", "type": "nt"}
        ],

        "divine_council_note": "YHWH's second speech is the ultimate divine council demonstration. The "
                               "question is: who governs the forces of chaos? Leviathan breathes fire "
                               "(41:18-21), his scales are impenetrable shields (41:15-17), and 'on earth "
                               "there is not his like, a creature without fear' (41:33). He is 'king over "
                               "all the sons of pride' (41:34) -- a title that positions Leviathan as the "
                               "sovereign of the chaotic realm, the antithesis of YHWH's ordered creation. "
                               "The point: if Job cannot tame Leviathan, he cannot challenge the One who "
                               "controls Leviathan. In the divine council framework, these chaos creatures "
                               "represent the spiritual forces of disorder that only YHWH can govern. The "
                               "Revelation 12-13 fulfillment shows these forces ultimately defeated through "
                               "Christ's victory.",

        "sections": [
            {
                "heading": "Job's First Response and YHWH's Challenge (40:1-14)",
                "body": "Job's initial response is brief and humble: 'Behold, I am of small account; "
                        "what shall I answer you? I lay my hand on my mouth. I have spoken once, and I "
                        "will not answer; twice, but I will proceed no further' (40:4-5). The hand on the "
                        "mouth is the gesture of submission and silence. But YHWH is not finished. The "
                        "second speech opens with a more direct challenge: 'Will you even put me in the "
                        "wrong? Will you condemn me that you may be in the right?' (40:8). YHWH does not "
                        "deny that Job has suffered unjustly -- the issue is whether Job can run the "
                        "universe better. 'Have you an arm like God, and can you thunder with a voice like "
                        "his?' (40:9). The challenge: if Job can govern the cosmos and humble the proud "
                        "(40:11-13), then 'I also will acknowledge to you that your own right hand can "
                        "save you' (40:14)."
            },
            {
                "heading": "Behemoth: The Supreme Land Creature (40:15-24)",
                "body": "YHWH introduces Behemoth: 'Behold, Behemoth, which I made as I made you' (40:15). "
                        "The description transcends any natural animal: 'His bones are tubes of bronze, "
                        "his limbs like bars of iron. He is the first of the works of God' (40:18-19). "
                        "The phrase 'first of the works of God' (reshit darke el) echoes the language used "
                        "of Wisdom in Proverbs 8:22 ('YHWH possessed me at the beginning of his work'). "
                        "Behemoth is primordial -- among the first things God made. He dwells under the "
                        "lotus plants, in the marshes (40:21-22), and even when 'the river rages... he is "
                        "confident' (40:23). Whether this is a hippopotamus, a dinosaur, or a mythological "
                        "creature, the theological point is clear: God made this being, and only God can "
                        "approach it with a sword (40:19)."
            },
            {
                "heading": "Leviathan: King Over All the Sons of Pride (41:1-34)",
                "body": "YHWH's Leviathan passage is the longest sustained description of a single "
                        "creature in the Bible. Can Job draw out Leviathan with a fishhook? (41:1). Will "
                        "Leviathan make a covenant with Job? (41:4). Can he be made a pet? (41:5). The "
                        "answer to every question is no. The description escalates: his sneezings flash "
                        "forth light (41:18), out of his mouth go flaming torches and sparks of fire "
                        "(41:19), smoke pours from his nostrils (41:20), and his breath kindles coals "
                        "(41:21). His underbelly is 'like sharp potsherds' (41:30), and he makes the deep "
                        "boil like a pot (41:31). The climax: 'On earth there is not his like, a creature "
                        "without fear. He sees everything that is high; he is king over all the sons of "
                        "pride' (41:33-34). No natural animal breathes fire or reigns over 'the sons of "
                        "pride.' Leviathan is a cosmic entity -- the chaos force that only YHWH governs."
            }
        ]
    },

    {
        "id": "job-42",
        "ref": "Job 42",
        "chapter_num": 42,
        "title": "Job's Repentance and Restoration",
        "era": "62",
        "type": "chapter",
        "themes": ["DC", "REVERSAL", "PROV", "PRIEST"],

        "synopsis": "Job responds to YHWH with words that have been debated for millennia: 'I had heard "
                    "of you by the hearing of the ear, but now my eye sees you; therefore I despise "
                    "myself, and repent in dust and ashes' (42:5-6). Job does not repent of sin (the "
                    "book has established his innocence) but of speaking beyond his knowledge about "
                    "cosmic governance. The encounter -- seeing God -- is the answer. Then YHWH turns "
                    "to the friends: 'My anger burns against you... for you have not spoken of me what "
                    "is right, as my servant Job has' (42:7). The friends who defended God's justice are "
                    "condemned; Job who challenged God is vindicated. YHWH instructs the friends to bring "
                    "burnt offerings and have Job pray for them. The epilogue restores Job double: "
                    "14,000 sheep, 6,000 camels, 1,000 yoke of oxen, 1,000 female donkeys, seven sons, "
                    "and three daughters. He lives 140 more years. But the prologue's question is "
                    "answered: Job feared God for nothing. His faithfulness was genuine.",

        "key_verse": {
            "ref": "Job 42:5-6",
            "text": "I had heard of you by the hearing of the ear, but now my eye sees you; therefore I despise myself, and repent in dust and ashes.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "nacham (to repent/relent/comfort -- Job's response after seeing God, debated in meaning)",
            "ra (evil/calamity -- what YHWH brought upon Job, acknowledged in 42:11)",
            "eved (servant -- YHWH calls Job 'my servant' four times in 42:7-8, the title of highest honor)",
            "mishne (double -- Job receives double restoration, echoing Isaiah 40:2 and 61:7)"
        ],

        "ane_backdrop": "The double restoration motif has parallels in ANE literature. The Babylonian "
                        "'Ludlul Bel Nemeqi' ends with full restoration of the sufferer by Marduk. The "
                        "practice of intercessory sacrifice (Job praying for his friends, 42:8-10) is "
                        "attested in both Mesopotamian and Israelite tradition. The restoration of wealth "
                        "and family represents the ANE ideal of divine blessing. But Job's restoration is "
                        "not merely material -- it is covenantal vindication. YHWH publicly declares that "
                        "Job spoke rightly and the friends did not.",

        "second_temple": [
            {
                "source": "LXX addition to Job 42:17",
                "summary": "The Septuagint adds: 'It is written that he will rise again with those "
                           "whom the Lord raises up.' Also identifies Job with Jobab of Genesis 36:33 "
                           "and provides genealogical information.",
                "relevance": "The LXX resurrection addition shows that by the Hellenistic period, "
                             "Job's story was being read through a resurrection lens -- his vindication "
                             "extends beyond this life."
            },
            {
                "source": "Testament of Job 46-53",
                "summary": "Job's three daughters receive heavenly girdles that enable them to speak "
                           "in angelic languages and see heavenly visions. Job himself ascends to "
                           "heaven in a chariot.",
                "relevance": "The Testament transforms Job's restoration into an apocalyptic event, "
                             "with his daughters becoming prophetic figures and Job himself entering "
                             "the heavenly realm."
            },
            {
                "source": "James 5:11",
                "summary": "'You have heard of the steadfastness (hypomone) of Job, and you have seen "
                           "the purpose (telos) of the Lord, how the Lord is compassionate and merciful.'",
                "relevance": "James interprets Job's story as a model of endurance that reveals God's "
                             "ultimate compassion -- the canonical NT reading of Job's resolution."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 40:2", "note": "'She has received from YHWH's hand double for all her sins' -- the double-restoration principle Job exemplifies", "type": "ot"},
            {"ref": "Isaiah 61:7", "note": "'Instead of your shame there shall be a double portion' -- the eschatological promise of double restoration", "type": "ot"},
            {"ref": "James 5:11", "note": "The 'purpose of the Lord' revealed in Job's story -- compassion and mercy through suffering", "type": "nt"},
            {"ref": "Ezekiel 14:14, 20", "note": "Job named alongside Noah and Daniel as exemplary righteous -- confirming his canonical reputation", "type": "ot"},
            {"ref": "Matthew 5:45", "note": "God 'makes his sun rise on the evil and on the good' -- the universal governance YHWH's speech reveals", "type": "nt"}
        ],

        "divine_council_note": "The epilogue completes the divine council narrative arc. Ha-Satan "
                               "challenged the genuineness of Job's faithfulness (1:9). YHWH permitted "
                               "the test. Job endured -- imperfectly (he demanded answers he had no right "
                               "to demand) but genuinely (he never cursed God). YHWH's verdict vindicates "
                               "Job against the friends: 'You have not spoken of me what is right, as my "
                               "servant Job has' (42:7). The irony is remarkable: the friends who defended "
                               "God's justice are condemned; Job who accused God of injustice is commended. "
                               "Why? Because Job engaged honestly with a God he experienced as absent, "
                               "while the friends reduced God to a formula. YHWH calls Job 'my servant' "
                               "(avdi) four times in 42:7-8 -- the divine council title of highest honor, "
                               "shared with Moses, David, and the Suffering Servant of Isaiah. The "
                               "restoration is not retribution theology vindicated but grace: God "
                               "restores what he was not obligated to restore.",

        "sections": [
            {
                "heading": "Job's Final Response: Seeing God (42:1-6)",
                "body": "Job's response to YHWH's speeches is the theological resolution of the book. "
                        "'I know that you can do all things, and that no purpose of yours can be thwarted' "
                        "(42:2). He quotes YHWH's own challenge back: 'Who is this that hides counsel "
                        "without knowledge?' and confesses: 'Therefore I have uttered what I did not "
                        "understand, things too wonderful for me, which I did not know' (42:3). Then the "
                        "pivotal statement: 'I had heard of you by the hearing of the ear, but now my eye "
                        "sees you' (42:5). The shift from hearsay to encounter is the resolution. Job's "
                        "suffering is not explained, but Job's God has been revealed. Verse 6 is debated: "
                        "'Therefore I despise myself (emas) and repent (nachamti) in dust and ashes.' "
                        "The verb 'nacham' can mean repent, relent, or be comforted. Some scholars render "
                        "it: 'I retract [my case] and am comforted in dust and ashes.' Job does not "
                        "repent of sin but of presuming to judge cosmic governance from a human vantage."
            },
            {
                "heading": "YHWH Vindicates Job Against the Friends (42:7-9)",
                "body": "YHWH's judgment on the friends is striking: 'My anger burns against you and "
                        "against your two friends, for you have not spoken of me what is right (nekhonah), "
                        "as my servant Job has' (42:7). This is stated twice for emphasis (42:7, 8). The "
                        "friends who defended God's justice by insisting that Job must have sinned are "
                        "condemned. Job who accused God of injustice is commended. The resolution: honest "
                        "engagement with God -- even angry, confused, demanding engagement -- is preferable "
                        "to theological systems that sacrifice truth for tidiness. YHWH instructs the "
                        "friends to bring seven bulls and seven rams as burnt offerings, and Job will pray "
                        "for them (42:8). Job, the accused, becomes the intercessor -- a priestly role "
                        "that anticipates Christ's intercession for those who wronged him."
            },
            {
                "heading": "Double Restoration (42:10-17)",
                "body": "YHWH restores Job's fortunes 'when he had prayed for his friends' (42:10) -- "
                        "the restoration is triggered by Job's intercession, not by his repentance (he had "
                        "nothing to repent of). The restoration is precisely double: 14,000 sheep (originally "
                        "7,000), 6,000 camels (3,000), 1,000 yoke of oxen (500), 1,000 female donkeys (500). "
                        "His children are replaced: seven sons and three daughters. The daughters -- Jemimah "
                        "('dove'), Keziah ('cinnamon'), and Keren-happuch ('horn of eye-paint') -- are named "
                        "(the sons are not), given an inheritance alongside their brothers (extraordinary in "
                        "ancient society), and described as the most beautiful women in all the land (42:15). "
                        "Job lives 140 more years (double the standard seventy) and sees four generations. "
                        "He dies 'old and full of days' (42:17). The answer to ha-Satan's challenge is "
                        "definitive: Job feared God for nothing. Grace, not transaction, is the foundation "
                        "of genuine faith."
            }
        ]
    }
]
