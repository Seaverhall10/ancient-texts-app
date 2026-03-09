"""
era_40_covenant_farewell.py -- Covenant & Farewell (Joshua 22-24)

The final section of Joshua addresses the unity of the covenant community (the
Transjordan altar controversy), Joshua's farewell warning against apostasy, and
the great covenant renewal at Shechem -- "choose this day whom you will serve."
The divine council language of Joshua 24 explicitly acknowledges the existence
of other gods while demanding exclusive loyalty to YHWH.
"""

CHAPTERS = [
    {
        "id": "josh-22",
        "ref": "Joshua 22",
        "chapter_num": 22,
        "title": "The Transjordan Altar -- Crisis of Unity and the Witness Stone",
        "era": "covenant_farewell",
        "type": "chapter",

        "synopsis": "With the conquest complete, Joshua dismisses the Transjordan tribes (Reuben, "
                    "Gad, half-Manasseh) to their eastern inheritance, charging them to 'take great "
                    "care to observe the commandment and the law that Moses the servant of the LORD "
                    "commanded you, to love the LORD your God, and to walk in all his ways' (22:5). "
                    "They depart blessed and laden with spoil. But when they reach the Jordan, they "
                    "build 'an altar of great size' (22:10) on the western bank. The nine and a half "
                    "western tribes interpret this as apostasy -- a rival sanctuary to the tabernacle "
                    "at Shiloh -- and prepare for civil war. Phinehas son of Eleazar leads a "
                    "delegation with ten chiefs (one per western tribe) to confront the eastern "
                    "tribes: 'What is this breach of faith (ma'al) that you have committed against "
                    "the God of Israel?' (22:16). They invoke the Baal-peor incident (Num 25) and "
                    "the Achan episode (Josh 7) as precedents for corporate guilt. The eastern "
                    "tribes explain: the altar is not for sacrifice but for witness (ed) -- a "
                    "memorial to future generations that the Transjordan tribes also belong to YHWH, "
                    "lest the western tribes' descendants say 'You have no portion in the LORD' "
                    "(22:25). The explanation satisfies Phinehas and the delegation: 'Today we know "
                    "that the LORD is in our midst, because you have not committed this breach of "
                    "faith against the LORD' (22:31). The altar is named 'Witness' (Ed) -- 'a "
                    "witness between us that the LORD is God' (22:34).",

        "key_verse": {
            "ref": "Joshua 22:22",
            "text": "The Mighty One, God, the LORD! The Mighty One, God, the LORD! He knows; and let Israel itself know! If it was in rebellion or in breach of faith against the LORD, do not spare us today.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "mizbeach (altar -- the structure that triggers the crisis)",
            "ed (witness -- the name given to the altar, testifying to covenant unity)",
            "ma'al (breach of faith/trespass -- the accusation against the eastern tribes)",
            "chelqah (portion/share -- the Transjordan tribes' concern about being excluded)",
            "El Elohim YHWH (The Mighty One, God, the LORD -- the triple divine name invoked by the eastern tribes)",
            "qehillah (assembly/congregation -- the gathered covenant community that nearly goes to war)",
            "pinehas (Phinehas -- the zealous priest, son of Eleazar, who leads the investigation)"
        ],

        "ane_backdrop": "The altar controversy reflects ANE concerns about cultic centralization "
                        "and the legitimacy of religious sites. In Mesopotamia, unauthorized shrines "
                        "were viewed as political and religious threats: the Assyrian kings "
                        "systematically destroyed rival sanctuaries to centralize worship. In Egypt, "
                        "Akhenaten's attempt to centralize worship at Amarna was both a religious "
                        "and political revolution. The Israelite principle of cultic centralization "
                        "(Deut 12:5-14, 'the place YHWH will choose') made any alternative altar "
                        "potentially subversive. The eastern tribes' defense -- that the altar is "
                        "a 'witness' (ed), not a place of sacrifice -- draws on the ANE practice "
                        "of memorial stones and witness structures. Standing stones (masseboth) "
                        "functioned as covenant witnesses throughout the Levant. The triple divine "
                        "name invoked by the eastern tribes (El Elohim YHWH, 22:22) is an "
                        "extraordinary oath formula: they invoke the divine name three times to "
                        "protest their innocence.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities V.1.25-26",
                "summary": "Josephus recounts the altar controversy and emphasizes the near-civil "
                           "war, treating it as evidence of Israel's zeal for cultic purity.",
                "relevance": "Josephus shows that Second Temple readers understood the altar crisis "
                             "as a test case for the balance between cultic zeal and covenant unity."
            },
            {
                "source": "Philo, Special Laws I.67-68",
                "summary": "Philo discusses the principle of centralized worship and its rationale: "
                           "preventing the fragmentation of the community through multiple shrines.",
                "relevance": "Philo's treatment reflects the ongoing concern about cultic unity "
                             "that the Joshua 22 narrative first dramatizes."
            },
            {
                "source": "Mishnah Zevachim 14:4-8",
                "summary": "The Mishnah discusses the periods when sacrificial worship was permitted "
                           "on local altars vs. centralized at one location, referencing the history "
                           "from Gilgal through Shiloh to Jerusalem.",
                "relevance": "Rabbinic law treated the centralization question as having evolved "
                             "through stages -- the Joshua 22 controversy belongs to the period "
                             "when Shiloh was THE central sanctuary."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 12:5-14", "note": "The centralization command: 'the place that the LORD your God will choose' -- the basis for the western tribes' alarm", "type": "ot"},
            {"ref": "Numbers 25:1-9", "note": "The Baal-peor incident cited by the delegation as precedent for corporate guilt from apostasy", "type": "ot"},
            {"ref": "Joshua 7:1-26", "note": "The Achan episode cited as precedent: 'Did not Achan... commit a breach of faith... and wrath fell upon all the congregation?'", "type": "ot"},
            {"ref": "Numbers 32:1-33", "note": "The original agreement with the Transjordan tribes -- the obligation they have now fulfilled", "type": "ot"},
            {"ref": "Judges 20:1-48", "note": "The civil war against Benjamin -- the near-war of Josh 22 foreshadows the actual civil war in Judges", "type": "ot"},
            {"ref": "Ephesians 4:3-6", "note": "'Eager to maintain the unity of the Spirit in the bond of peace... one Lord, one faith, one baptism' -- the NT equivalent of the Josh 22 unity concern", "type": "nt"},
            {"ref": "Genesis 31:44-52", "note": "Jacob and Laban's heap of witness (gal'ed) -- the same 'witness' concept applied to a covenant marker", "type": "ot"}
        ],

        "divine_council_note": "The altar controversy reveals the tension inherent in the divine "
                               "council worldview: YHWH is worshipped at one central sanctuary (the "
                               "tabernacle at Shiloh), but his sovereignty extends over all territory, "
                               "including the Transjordan. The western tribes fear that an eastern "
                               "altar means the eastern tribes are establishing an alternative divine "
                               "jurisdiction -- serving a different deity or at least worshipping YHWH "
                               "outside his authorized location. In the Deuteronomy 32 framework, the "
                               "Transjordan territories were originally allotted to other spiritual "
                               "powers (Chemosh for Moab, Milcom for Ammon). By building an altar "
                               "there, the eastern tribes could be seen as reverting to the pre-"
                               "conquest spiritual order. Their defense is that the altar is a witness "
                               "to YHWH's lordship over both sides of the Jordan -- a declaration that "
                               "the cosmic boundary between YHWH's territory and the territory of other "
                               "elohim does NOT run along the Jordan. YHWH's sovereignty extends "
                               "everywhere his people live. The triple divine name -- 'El Elohim YHWH' "
                               "(22:22) -- may reflect the divine council hierarchy: El (the supreme "
                               "God), Elohim (the divine category), and YHWH (the specific personal "
                               "name). The eastern tribes invoke the full majesty of YHWH's identity "
                               "to protest their innocence.",

        "sections": [
            {
                "heading": "Dismissal of the Eastern Tribes (22:1-9)",
                "body": "Joshua summons the Transjordan tribes and formally releases them from "
                        "their military obligation: 'You have kept all that Moses the servant of "
                        "the LORD commanded you and have obeyed my voice in all that I have "
                        "commanded you. You have not forsaken your brothers these many days, down "
                        "to this day, but have been careful to keep the charge of the LORD your God' "
                        "(22:2-3). Their faithfulness during the entire conquest -- fighting for their "
                        "brothers' inheritance before returning to their own -- is formally recognized. "
                        "Joshua's charge for the future echoes the Shema: 'Take great care to observe "
                        "the commandment and the law that Moses the servant of the LORD commanded you, "
                        "to love the LORD your God, and to walk in all his ways and to keep his "
                        "commandments and to cling to him and to serve him with all your heart and "
                        "with all your soul' (22:5). The five verbs -- observe, love, walk, keep, "
                        "cling -- are a concentrated Deuteronomic vocabulary of covenant faithfulness. "
                        "Joshua blesses them and sends them away with great wealth: 'with much "
                        "livestock, with silver, gold, bronze, and iron, and with much clothing. "
                        "Divide the spoil of your enemies with your brothers' (22:8). They depart "
                        "for their Transjordan inheritance."
            },
            {
                "heading": "The Altar That Almost Caused Civil War (22:10-20)",
                "body": "The crisis erupts without warning: 'When they came to the region of the "
                        "Jordan that is in the land of Canaan, the people of Reuben and the people "
                        "of Gad and the half-tribe of Manasseh built there an altar by the Jordan, "
                        "an altar of imposing size' (22:10). The western tribes hear of it and "
                        "immediately mobilize for war: 'the whole assembly of the people of Israel "
                        "gathered at Shiloh to make war against them' (22:12). The reaction is "
                        "extreme but theologically grounded: Deuteronomy 13:12-16 commands the "
                        "destruction of any Israelite city that apostatizes. If the eastern tribes "
                        "have built a rival sanctuary, the covenant demands a military response. "
                        "Before attacking, they send a diplomatic delegation: Phinehas son of "
                        "Eleazar (whose zealous action at Baal-peor had stopped the plague, Num "
                        "25:7-13) and ten tribal chiefs. Phinehas confronts the eastern tribes: "
                        "'What is this breach of faith that you have committed against the God of "
                        "Israel in turning away this day from following the LORD by building "
                        "yourselves an altar this day in rebellion against the LORD?' (22:16). "
                        "He invokes the precedents: Baal-peor's plague (Num 25) and Achan's sin "
                        "(Josh 7) -- both cases where one group's sin brought judgment on all "
                        "Israel. He even offers a radical solution: 'If the land of your possession "
                        "is unclean, cross over into the LORD's land where the LORD's tabernacle "
                        "stands, and take for yourselves a possession among us' (22:19). Better to "
                        "share the western territory than to rebel against YHWH."
            },
            {
                "heading": "The Defense: A Witness, Not a Sacrifice (22:21-29)",
                "body": "The eastern tribes respond with the most passionate oath in the book: 'The "
                        "Mighty One, God, the LORD! The Mighty One, God, the LORD! He knows!' "
                        "(22:22). The triple divine name -- El Elohim YHWH -- is invoked twice for "
                        "emphasis, a solemn oath formula of extraordinary gravity. They invoke YHWH "
                        "as the omniscient witness: 'He knows; and let Israel itself know! If it "
                        "was in rebellion or in breach of faith against the LORD, do not spare us "
                        "today' (22:22). They self-imprecate: if we are guilty, may God destroy us. "
                        "Their explanation reveals the real concern: 'In time to come your children "
                        "might say to our children, What have you to do with the LORD, the God of "
                        "Israel? For the LORD has made the Jordan a boundary between us and you. "
                        "You have no portion (cheleq) in the LORD' (22:24-25). Their fear is not "
                        "that YHWH will forget them but that the western tribes' descendants will "
                        "exclude them. The Jordan could become a theological boundary -- separating "
                        "YHWH's 'real' people from those on the other side. The altar is built as "
                        "a 'witness between us and you, and between our generations after us, that "
                        "we do perform the service of the LORD in his presence' (22:27). It is not "
                        "for burnt offerings or sacrifice but for testimony: visible proof that the "
                        "eastern tribes belong to YHWH's covenant community."
            },
            {
                "heading": "Resolution: The Altar of Witness (22:30-34)",
                "body": "Phinehas and the delegation hear the explanation 'and it was good in their "
                        "eyes' (22:30). Phinehas declares: 'Today we know that the LORD is in our "
                        "midst (beqirbeinu), because you have not committed this breach of faith "
                        "against the LORD. Now you have delivered the people of Israel from the hand "
                        "of the LORD' (22:31). The phrase 'delivered from the hand of the LORD' is "
                        "striking: corporate punishment was averted because the eastern tribes were "
                        "innocent. The delegation returns to the western tribes with the good news, "
                        "and 'the people of Israel blessed God and spoke no more of making war "
                        "against them to destroy the land' (22:33). The eastern tribes name the "
                        "altar Ed ('Witness'): 'For it is a witness between us that the LORD is "
                        "God' (22:34). The crisis resolves peacefully, but the underlying tension -- "
                        "the geographic and spiritual unity of a people divided by a river -- will "
                        "persist throughout Israel's history. The episode teaches that zeal for "
                        "YHWH's honor must be balanced by careful investigation before action, "
                        "and that covenant unity transcends geography. The Jordan is not a "
                        "theological boundary. YHWH's people on both sides of the river belong "
                        "equally to his covenant."
            }
        ]
    },

    {
        "id": "josh-23",
        "ref": "Joshua 23",
        "chapter_num": 23,
        "title": "Joshua's Farewell Warning -- The Danger of the Remaining Nations",
        "era": "covenant_farewell",
        "type": "chapter",

        "synopsis": "Many years after the conquest, Joshua -- now 'old and advanced in years' -- "
                    "summons all Israel for his farewell address. He reminds them of YHWH's "
                    "faithfulness: 'You have seen all that the LORD your God has done to all "
                    "these nations for your sake, for it is the LORD your God who has fought for "
                    "you' (23:3). He assures them that YHWH will continue to drive out the "
                    "remaining nations 'until they have perished from before you' (23:5). The "
                    "condition is covenant faithfulness: 'Be very strong to keep and to do all "
                    "that is written in the Book of the Law of Moses' (23:6). The core warning "
                    "is against intermarriage and religious syncretism with the nations that "
                    "remain among them. 'For if you turn back and cling to the remnant of these "
                    "nations remaining among you and make marriages with them, know for certain "
                    "that the LORD your God will no longer drive out these nations before you, but "
                    "they shall be a snare and a trap for you' (23:12-13). The speech is structured "
                    "as a covenant lawsuit: YHWH has kept his side of the covenant (23:14), and "
                    "Israel must keep theirs. The consequences of failure are devastating: 'Just as "
                    "every good word that YHWH has spoken to you has been fulfilled, so YHWH will "
                    "bring upon you every evil word, until he has destroyed you from off this good "
                    "land' (23:15). The same God who fulfills promises of blessing will fulfill "
                    "threats of curse.",

        "key_verse": {
            "ref": "Joshua 23:14",
            "text": "And now I am about to go the way of all the earth, and you know in your hearts and souls, all of you, that not one word has failed of all the good things that the LORD your God promised concerning you. All have come to pass for you; not one of them has failed.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "davaq (to cling/cleave -- used both for clinging to YHWH and for dangerous attachment to the nations)",
            "chatanim (intermarriage -- the specific danger Joshua warns against)",
            "moqesh (snare -- the nations as traps for Israel's faith)",
            "pach (trap -- parallel to moqesh, the danger of syncretism)",
            "shot (whip/scourge -- the remaining nations as instruments of divine discipline)",
            "tseninim (thorns -- the nations as painful irritants in Israel's eyes)",
            "aved (to perish -- the ultimate consequence of covenant violation)"
        ],

        "ane_backdrop": "Farewell addresses by aging leaders were a recognized genre in the ANE. "
                        "Egyptian 'Instructions' literature (Instruction of Ptahhotep, Instruction "
                        "of Amenemhet) records the final teachings of wise men to their successors. "
                        "Hittite royal testaments (Testament of Hattusili I, ~1650 BC) include the "
                        "dying king's warnings to his successors about loyalty to the gods and "
                        "the treaty obligations. Moses' farewell in Deuteronomy follows this pattern, "
                        "and Joshua's farewell continues it. The warning against intermarriage "
                        "reflects the ANE reality that marriage alliances carried religious "
                        "obligations: marrying into a foreign household meant accepting that "
                        "household's gods. The Amarna Letters reveal how marriage alliances "
                        "between Canaanite city-states created religious as well as political "
                        "obligations.",

        "second_temple": [
            {
                "source": "Ezra 9-10",
                "summary": "Ezra's prayer and the covenant to divorce foreign wives directly "
                           "invoke the Joshua 23 warning about intermarriage leading to apostasy.",
                "relevance": "The post-exilic community treated Joshua 23 as prophetically fulfilled: "
                             "intermarriage had indeed led to the apostasy that caused the exile."
            },
            {
                "source": "Nehemiah 13:23-27",
                "summary": "Nehemiah confronts intermarriage and cites Solomon as a cautionary "
                           "example: 'Did not Solomon king of Israel sin on account of such women?'",
                "relevance": "The trajectory Joshua 23 warns about -- intermarriage leading to "
                             "apostasy -- was traced through Solomon's fall as the definitive "
                             "historical vindication of Joshua's warning."
            },
            {
                "source": "Jubilees 30:7-17",
                "summary": "Jubilees strongly prohibits intermarriage, treating it as a capital "
                           "offense that brings defilement on the entire community.",
                "relevance": "The Jubilees tradition radicalized the Joshua 23 warning, treating "
                             "intermarriage as one of the gravest possible covenant violations."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 7:1-4", "note": "Moses' prohibition against intermarriage with the seven nations -- the foundation for Joshua's warning", "type": "ot"},
            {"ref": "Judges 2:1-5, 10-13", "note": "The immediate fulfillment of Joshua's warning: Israel fails to drive out the nations and serves Baal", "type": "ot"},
            {"ref": "1 Kings 11:1-8", "note": "Solomon's foreign wives turn his heart to other gods -- the climactic fulfillment of the intermarriage warning", "type": "ot"},
            {"ref": "Joshua 21:45", "note": "'Not one word has failed' -- the same fulfillment language Joshua uses in his farewell (23:14)", "type": "ot"},
            {"ref": "2 Peter 2:20-22", "note": "'If, after they have escaped the defilements of the world through the knowledge of our Lord... they are again entangled' -- the NT version of the apostasy warning", "type": "nt"},
            {"ref": "Hebrews 3:12-14", "note": "'Take care, brothers, lest there be in any of you an evil, unbelieving heart, leading you to fall away from the living God' -- echoing Joshua's warning", "type": "nt"}
        ],

        "divine_council_note": "Joshua's farewell address is rooted in the divine council worldview. "
                               "The 'remaining nations' are not merely political entities but spiritual "
                               "jurisdictions governed by the elohim allotted to them under Deuteronomy "
                               "32:8. Intermarrying with these nations does not merely create cultural "
                               "complications -- it entangles Israel with the spiritual powers that "
                               "govern those nations. When Joshua warns that the remaining nations will "
                               "become 'a snare and a trap, a whip on your sides and thorns in your "
                               "eyes' (23:13), he is describing the spiritual consequences of engaging "
                               "with the allotted elohim's domains. The key theological affirmation is "
                               "23:14: 'not one word has failed of all the good things that YHWH your "
                               "God promised.' YHWH has kept the covenant. The question is whether "
                               "Israel will. The ominous parallel follows: 'just as all the good things "
                               "that YHWH has spoken have come to pass, so YHWH will bring upon you "
                               "all the evil things' (23:15). The same faithfulness that guarantees "
                               "blessing guarantees curse. YHWH's word never fails -- for good or "
                               "for ill.",

        "sections": [
            {
                "heading": "YHWH's Past Faithfulness (23:1-8)",
                "body": "Joshua's farewell opens with a review of YHWH's mighty acts: 'You have "
                        "seen all that the LORD your God has done to all these nations for your "
                        "sake, for it is the LORD your God who has fought for you' (23:3). The "
                        "attribution is total -- every victory was YHWH's. Joshua reminds them of "
                        "the allotment: 'I have allotted to you as an inheritance for your tribes "
                        "those nations that remain, along with all the nations that I have already "
                        "cut off, from the Jordan to the Great Sea in the west' (23:4). Even the "
                        "unconquered nations are allotted to Israel by divine decree -- their "
                        "eventual dispossession is guaranteed: 'The LORD your God will push them "
                        "back before you and drive them out of your sight. And you shall possess "
                        "their land, just as the LORD your God promised you' (23:5). The condition: "
                        "'Be very strong to keep and to do all that is written in the Book of the "
                        "Law of Moses, turning aside from it neither to the right hand nor to the "
                        "left, that you may not mix with these nations remaining among you or make "
                        "mention of the names of their gods or swear by them or serve them or bow "
                        "down to them, but you shall cling to the LORD your God just as you have "
                        "done to this day' (23:6-8). The prohibition against even mentioning the "
                        "names of other gods reflects the divine council reality: these are real "
                        "spiritual beings whose names carry power. To invoke them is to acknowledge "
                        "their jurisdiction."
            },
            {
                "heading": "The Warning Against Apostasy (23:9-16)",
                "body": "Joshua's tone shifts from encouragement to warning: 'For if you turn back "
                        "and cling to the remnant of these nations remaining among you and make "
                        "marriages with them, so that you associate with them and they with you, "
                        "know for certain that the LORD your God will no longer drive out these "
                        "nations before you' (23:12-13). Intermarriage is the gateway to apostasy "
                        "because it creates family obligations to foreign gods. The metaphors for "
                        "the remaining nations intensify: 'they shall be a snare (moqesh) and a "
                        "trap (pach) for you, a whip (shot) on your sides and thorns (tseninim) "
                        "in your eyes' (23:13). Four images of pain and captivity -- the nations "
                        "that Israel fails to drive out will become instruments of Israel's own "
                        "suffering. The consequence of continued apostasy: 'you shall perish from "
                        "off this good land that the LORD your God has given you' (23:13, 16). The "
                        "land that was given can be taken away. Possession is conditional on "
                        "faithfulness. Joshua's final words echo the covenant curse tradition of "
                        "Deuteronomy 28: 'if you transgress the covenant of the LORD your God, "
                        "which he commanded you, and go and serve other gods and bow down to them... "
                        "the anger of the LORD will be kindled against you, and you shall perish "
                        "quickly from off the good land that he has given to you' (23:16). The "
                        "book of Judges will record the immediate beginning of this trajectory. "
                        "The Deuteronomistic History through 2 Kings will trace it to its "
                        "devastating conclusion in exile."
            }
        ]
    },

    {
        "id": "josh-24",
        "ref": "Joshua 24",
        "chapter_num": 24,
        "title": "The Covenant at Shechem -- 'Choose This Day Whom You Will Serve'",
        "era": "covenant_farewell",
        "type": "chapter",

        "synopsis": "Joshua assembles all Israel at Shechem -- the site where Abraham first received "
                    "the land promise (Gen 12:6-7), where Jacob buried his family's foreign gods "
                    "(Gen 35:4), and where Joshua previously renewed the covenant (Josh 8:30-35). "
                    "YHWH speaks in the first person through Joshua, recounting the entire salvation "
                    "history from Abraham through the conquest. The speech begins with explicit "
                    "divine council language: 'Long ago, your fathers lived beyond the Euphrates, "
                    "Terah, the father of Abraham and of Nahor; and they served other gods' (24:2). "
                    "YHWH took Abraham from 'beyond the River,' led Israel through Egypt, the "
                    "wilderness, and the conquest. The climax is the most famous verse in Joshua: "
                    "'Choose this day whom you will serve, whether the gods your fathers served in "
                    "the region beyond the River, or the gods of the Amorites in whose land you "
                    "dwell. But as for me and my house, we will serve the LORD' (24:15). The people "
                    "affirm three times that they will serve YHWH alone. Joshua warns them: 'You "
                    "are not able to serve the LORD, for he is a holy God. He is a jealous God' "
                    "(24:19). The covenant is ratified. Joshua writes the covenant words in the "
                    "Book of the Law, sets up a great stone under the terebinth tree at Shechem "
                    "as a witness, and sends the people to their inheritances. Joshua dies at 110 "
                    "years old. The book closes with the burial of Joseph's bones at Shechem -- "
                    "fulfilling the oath of Genesis 50:25 -- and the death and burial of Eleazar "
                    "the priest.",

        "key_verse": {
            "ref": "Joshua 24:15",
            "text": "And if it is evil in your eyes to serve the LORD, choose this day whom you will serve, whether the gods your fathers served in the region beyond the River, or the gods of the Amorites in whose land you dwell. But as for me and my house, we will serve the LORD.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "bachar (to choose -- the covenant demand for a conscious decision)",
            "avad (to serve/worship -- the verb applied to both YHWH and other gods)",
            "elohim acherim (other gods -- the Hebrew Bible uses <em>elohim</em> as a broad category meaning 'divine beings' or 'spiritual beings,' not exclusively the one true God; the 'other gods' here are real spiritual entities in the divine council framework, not mere idols, though their worship is forbidden because YHWH alone is the supreme God and Israel's covenant lord)",
            "ever hanahar (beyond the River -- Mesopotamia, where Abraham's family served other gods)",
            "qanna (jealous -- YHWH's exclusive covenant claim on Israel's loyalty)",
            "berit (covenant -- the formal agreement ratified at Shechem)",
            "massevah (stone pillar -- the witness stone set up under the terebinth)",
            "elah (terebinth/oak -- the sacred tree at Shechem, associated with divine presence)"
        ],

        "ane_backdrop": "The Shechem covenant follows the structure of ANE suzerainty treaties (agreements between a powerful 'suzerain' or overlord and a weaker 'vassal' or subject king; see the Reader's Guide in Era 1 for the full explanation of this treaty form): "
                        "(1) Preamble: YHWH identifies himself (24:2a). (2) Historical prologue: "
                        "the recounting of YHWH's saving acts from Abraham to the conquest (24:2b-13). "
                        "(3) Stipulations: serve YHWH alone (24:14-15). (4) Witness: the stone "
                        "pillar (24:26-27). (5) Deposit: the covenant written in the Book of the "
                        "Law of God (24:26). This structure matches the Hittite suzerainty treaties "
                        "of the Late Bronze Age (14th-13th century BC), supporting an early date "
                        "for the covenant form. Shechem itself was a major Bronze Age cult center "
                        "with a massive migdal-temple (fortress temple) dating to the Middle Bronze "
                        "Age. The 'terebinth' (or 'oak') at Shechem has a long patriarchal "
                        "association (Gen 12:6, 'the oak of Moreh'; Gen 35:4, where Jacob buried "
                        "the foreign gods). The practice of setting up a witness stone at a covenant "
                        "site is attested throughout the ANE.",

        "second_temple": [
            {
                "source": "Sirach (Ecclesiasticus) 46:1-10",
                "summary": "Sirach's praise of Joshua culminates in the covenant renewal: Joshua "
                           "as the man who secured Israel's allegiance to YHWH before his death.",
                "relevance": "Sirach treats the Shechem covenant as the crowning achievement of "
                             "Joshua's career -- not the military victories but the spiritual commitment."
            },
            {
                "source": "Pseudo-Philo, Biblical Antiquities 21:1-6",
                "summary": "Pseudo-Philo expands Joshua's farewell with additional warnings and "
                           "prophecies about Israel's future apostasy.",
                "relevance": "The Second Temple expansion reflects awareness that Joshua's warning "
                             "was prophetically fulfilled -- Israel did serve other gods."
            },
            {
                "source": "Testament of Joshua (unpublished fragments)",
                "summary": "Testamentary literature attributed to Joshua, following the pattern of "
                           "farewell addresses by dying patriarchs.",
                "relevance": "The testament genre built on Joshua 24 demonstrates the importance "
                             "of 'last words' in Second Temple literary tradition."
            },
            {
                "source": "Josephus, Antiquities V.1.29",
                "summary": "Josephus describes Joshua's farewell speech and death, noting his age "
                           "of 110 and the enduring impact of his leadership.",
                "relevance": "Josephus treats the Shechem covenant as Joshua's definitive legacy: "
                             "binding Israel to YHWH through a final, solemn oath."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 12:6-7", "note": "Abraham at Shechem receiving the land promise -- the covenant location is the same", "type": "ot"},
            {"ref": "Genesis 35:2-4", "note": "Jacob commands his household to put away foreign gods and buries them at Shechem -- the same demand Joshua makes", "type": "ot"},
            {"ref": "Genesis 50:25", "note": "Joseph's oath: 'God will surely visit you, and you shall carry up my bones from here' -- fulfilled in Josh 24:32", "type": "ot"},
            {"ref": "Deuteronomy 30:15-20", "note": "'I have set before you today life and death, blessing and curse. Therefore choose life' -- the Deuteronomic precedent for Josh 24:15", "type": "ot"},
            {"ref": "Judges 2:6-15", "note": "After Joshua's death, Israel served other gods -- the immediate failure of the Shechem commitment", "type": "ot"},
            {"ref": "1 Kings 18:21", "note": "Elijah: 'How long will you go limping between two different opinions?' -- the same choice Joshua demanded at Shechem", "type": "ot"},
            {"ref": "John 4:20-24", "note": "The Samaritan woman at Shechem: 'Our fathers worshiped on this mountain' -- the covenant site still theologically active in Jesus' day", "type": "nt"},
            {"ref": "Acts 7:16", "note": "Stephen references the burial of the patriarchs at Shechem -- connecting the Joshua 24 conclusion to salvation history", "type": "nt"},
            {"ref": "Revelation 3:15-16", "note": "'I wish that you were either cold or hot' -- Christ's demand for decision echoes Joshua's 'choose this day'", "type": "nt"}
        ],

        "divine_council_note": "Joshua 24 contains the most explicit divine council language in the "
                               "book. The opening verse establishes the polytheistic background of "
                               "Israel's ancestry: 'Your fathers lived beyond the Euphrates... and "
                               "they served other gods' (24:2). The 'other gods' (elohim acherim) "
                               "are not fictional -- they are the spiritual beings who governed "
                               "Mesopotamia under the Deuteronomy 32:8-9 allotment. Terah, Abraham's "
                               "father, served these elohim. YHWH 'took' (laqach) Abraham out of that "
                               "spiritual jurisdiction and brought him into a direct relationship. "
                               "The choice Joshua presents (24:15) names three categories of elohim: "
                               "(1) 'The gods your fathers served beyond the River' -- the Mesopotamian "
                               "deities (Marduk, Sin, Ishtar, Enlil). (2) 'The gods of the Amorites "
                               "in whose land you dwell' -- the Canaanite deities (Baal, Asherah, Mot, "
                               "Anat). (3) YHWH -- the Most High who chose Israel as his own portion. "
                               "The choice is not between YHWH and nothing; it is between YHWH and "
                               "real spiritual beings who claim authority over nations and territories. "
                               "Joshua does not deny that these gods exist -- he demands that Israel "
                               "reject their authority and serve YHWH exclusively. This is what scholars "
                               "call <em>monolatry</em> (from Greek <em>monos</em>, 'one,' and <em>latreia</em>, "
                               "'worship' -- the exclusive worship of one God without necessarily denying "
                               "the existence of other spiritual beings; distinct from monotheism, which "
                               "denies the existence of any other gods entirely): not the denial of other "
                               "elohim but the exclusive worship of the Most High. Joshua's warning that YHWH is 'a jealous God' (el "
                               "qanna, 24:19) uses covenant jealousy language: YHWH will not share "
                               "Israel's worship with the elohim of the nations. The stone witness "
                               "under the terebinth (24:26-27) -- 'it has heard all the words of "
                               "the LORD that he spoke to us' -- functions as a permanent covenant "
                               "witness, like the heavens and earth Moses invoked in Deuteronomy 30:19. "
                               "The entire scene is a divine council commitment ceremony: Israel "
                               "formally chooses YHWH over all other elohim, and a stone witness "
                               "records the choice for eternity.",

        "sections": [
            {
                "heading": "YHWH's First-Person Salvation History (24:1-13)",
                "body": "Joshua gathers all Israel at Shechem -- elders, heads, judges, and officers "
                        "-- and they 'presented themselves before God' (24:1). The phrase 'before "
                        "God' (lifnei ha'elohim) indicates the presence of the ark and the formal "
                        "cultic setting. YHWH then speaks in the first person through Joshua -- a "
                        "prophetic oracle in which God recounts his own mighty acts. 'Thus says the "
                        "LORD, the God of Israel: Long ago, your fathers lived beyond the Euphrates, "
                        "Terah, the father of Abraham and of Nahor; and they served other gods' "
                        "(24:2). The confession is stunning in its honesty: Israel's patriarchal "
                        "family was pagan. They served the elohim of Mesopotamia. YHWH himself "
                        "intervened: 'Then I took your father Abraham from beyond the River and led "
                        "him through all the land of Canaan, and made his offspring many' (24:3). "
                        "The verb 'took' (laqach) implies extraction from one spiritual jurisdiction "
                        "to another -- YHWH pulled Abraham out of the territory of Mesopotamia's "
                        "gods and brought him into his own domain. The oracle continues through "
                        "Isaac, Jacob, Esau, Moses and Aaron, the plagues on Egypt, the Red Sea, "
                        "the wilderness, Balaam, the Jordan crossing, Jericho, and the conquest of "
                        "the Amorites, Perizzites, Canaanites, Hittites, Girgashites, Hivites, and "
                        "Jebusites. The climax: 'I gave you a land on which you had not labored and "
                        "cities that you had not built, and you dwell in them. You eat the fruit of "
                        "vineyards and olive orchards that you did not plant' (24:13). Everything "
                        "Israel has -- land, cities, orchards -- is a gift. The historical prologue "
                        "establishes the Great King's case for loyalty: I did all this for you; "
                        "therefore serve me."
            },
            {
                "heading": "The Choice: YHWH or the Other Gods (24:14-18)",
                "body": "The stipulation follows the historical prologue: 'Now therefore fear the "
                        "LORD and serve him in sincerity and in faithfulness. Put away the gods that "
                        "your fathers served beyond the River and in Egypt, and serve the LORD' "
                        "(24:14). The command to 'put away' (hasiru) foreign gods implies that some "
                        "Israelites still possess them -- idolatrous objects brought from Egypt or "
                        "acquired from the Canaanites. Jacob had to issue the same command at this "
                        "same location (Gen 35:2-4). Then comes the most famous verse in Joshua: "
                        "'And if it is evil in your eyes to serve the LORD, choose this day whom "
                        "you will serve, whether the gods your fathers served in the region beyond "
                        "the River, or the gods of the Amorites in whose land you dwell. But as "
                        "for me and my house, we will serve the LORD' (24:15). The choice is "
                        "presented as genuine: Israel is not coerced but confronted with a decision. "
                        "The three options -- Mesopotamian gods, Canaanite gods, or YHWH -- represent "
                        "the real spiritual alternatives available in the ANE world. Joshua does not "
                        "say these other gods do not exist; he says he and his household have already "
                        "decided. The people respond: 'Far be it from us that we should forsake the "
                        "LORD to serve other gods, for it is the LORD our God who brought us and our "
                        "fathers up from the land of Egypt' (24:16-17). They affirm YHWH three "
                        "times (24:18, 21, 24), each affirmation more emphatic than the last."
            },
            {
                "heading": "Joshua's Shocking Warning (24:19-24)",
                "body": "Joshua's response to the people's affirmation is unexpected and disturbing: "
                        "'You are not able to serve the LORD, for he is a holy God. He is a jealous "
                        "God; he will not forgive your transgressions or your sins' (24:19). This is "
                        "not reverse psychology but sober theology: Joshua knows what Israel will do. "
                        "He knows they will serve other gods. He wants the commitment to be made "
                        "with full understanding of the consequences. YHWH is 'holy' (qadosh) -- "
                        "utterly separate from everything profane, and his holiness cannot coexist "
                        "with idolatry. He is 'jealous' (qanna) -- his covenant demands exclusive "
                        "loyalty, and violation provokes his wrath. 'If you forsake the LORD and "
                        "serve foreign gods, then he will turn and do you harm and consume you, "
                        "after having done you good' (24:20). The warning is absolute: the God who "
                        "blessed can also destroy. The people insist: 'No, but we will serve the "
                        "LORD' (24:21). Joshua makes them witnesses against themselves: 'You are "
                        "witnesses against yourselves that you have chosen the LORD, to serve him.' "
                        "They confirm: 'We are witnesses' (24:22). Joshua demands action: 'Then put "
                        "away the foreign gods that are among you, and incline your heart to the "
                        "LORD, the God of Israel' (24:23). The people affirm a final time: 'The "
                        "LORD our God we will serve, and his voice we will obey' (24:24). The "
                        "threefold affirmation is formal and binding -- a covenant commitment "
                        "witnessed by the entire assembly."
            },
            {
                "heading": "The Covenant Ratified and Joshua's Death (24:25-33)",
                "body": "Joshua makes a covenant (berit) with the people that day and sets up "
                        "'statutes and rules' (choq umishpat) at Shechem (24:25). He writes the "
                        "covenant words 'in the Book of the Law of God' (sefer torat elohim) -- "
                        "adding to the sacred written text (24:26). He takes a great stone and sets "
                        "it up under the terebinth (elah) that was 'in the sanctuary (miqdash) of "
                        "the LORD' at Shechem. The stone becomes a witness: 'Behold, this stone "
                        "shall be a witness against us, for it has heard all the words of the LORD "
                        "that he spoke to us. Therefore it shall be a witness against you, lest you "
                        "deal falsely with your God' (24:27). The personification of the stone -- "
                        "'it has heard' -- echoes the witness function of heavens and earth in "
                        "Deuteronomy 30:19 and 31:28. The covenant concluded, Joshua sends the "
                        "people to their inheritances. 'After these things Joshua the son of Nun, "
                        "the servant of the LORD, died, being 110 years old' (24:29). He is finally "
                        "given the title 'servant of YHWH' (eved YHWH) -- the honor Moses held, "
                        "now transferred at death. He is buried in Timnath-serah, his inheritance. "
                        "A crucial epitaph: 'Israel served the LORD all the days of Joshua, and all "
                        "the days of the elders who outlived Joshua and had known all the work that "
                        "the LORD did for Israel' (24:31). Faithfulness lasted one generation. The "
                        "book of Judges will reveal how quickly the covenant was broken. Finally, "
                        "'The bones of Joseph, which the people of Israel brought up from Egypt, "
                        "were buried at Shechem, in the piece of land that Jacob bought from the "
                        "sons of Hamor' (24:32). Joseph's 400-year-old oath (Gen 50:25; Exod 13:19) "
                        "is fulfilled. The promises of Genesis are complete. And Eleazar son of "
                        "Aaron dies and is buried in the hill country of Ephraim (24:33). The "
                        "book ends with three burials: Joshua, Joseph, and Eleazar -- the commander, "
                        "the patriarch, and the priest. The conquest generation is passing. What "
                        "comes next depends on whether the Shechem covenant holds."
            }
        ]
    }
]
