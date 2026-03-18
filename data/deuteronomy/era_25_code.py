"""
era_25_code.py — The Deuteronomic Code (Deuteronomy 12-18)

The specific stipulations of the covenant: centralized worship, the test of
prophets, dietary laws, the sabbatical year, festivals, courts, kingship
law, priestly portions, and the Prophet like Moses. This is the legal core
of the suzerainty treaty.
"""

CHAPTERS = [
    {
        "id": "deut-12",
        "ref": "Deuteronomy 12",
        "chapter_num": 12,
        "title": "Centralized Worship — The Place YHWH Will Choose",
        "era": "code",
        "type": "chapter",
        "themes": ["HOLY", "LAW", "NAME", "DC", "NATIONS"],

        "synopsis": "Deuteronomy 12 is the first and most foundational law in the Deuteronomic Code: "
                    "all worship must occur at 'the place that the LORD your God will choose out of "
                    "all your tribes to put his name and make his habitation there' (12:5). This "
                    "centralization command is revolutionary — it counters the entire religious "
                    "structure of the ANE, where every city had its own shrine to its patron deity. "
                    "In the divine council framework, each allotted 'el had a local dwelling place "
                    "in the territory assigned to that 'el's nation. YHWH's command to centralize "
                    "worship asserts something radical: he is not a local deity confined to one "
                    "shrine but a universal God who CHOOSES where his presence will dwell. The "
                    "chapter begins by commanding the total destruction of Canaanite worship sites "
                    "— high places, pillars, Asherim poles, carved and metal images (12:2-4). Israel "
                    "must 'not worship the LORD your God in that way' (12:4) — God's worship cannot "
                    "be syncretized with Canaanite forms. The practical implications are far-reaching: "
                    "sacrificial slaughter can only occur at the central sanctuary, though non-sacred "
                    "slaughter for food is permitted locally (12:15-16). The chapter closes with a "
                    "horrifying description of Canaanite worship: 'they even burn their sons and "
                    "their daughters in the fire to their gods' (12:31) — child sacrifice as the "
                    "ultimate abomination that necessitates the centralization command.",

        "key_verse": {
            "ref": "Deuteronomy 12:5",
            "text": "But you shall seek the place that the LORD your God will choose out of all your tribes to put his name and make his habitation there. There you shall go.",
            "translation": "ESV"
        },

        "hebrew_terms": ["maqom", "shem", "shikno", "bamot", "matstsevah", "asherah", "olah", "zevach", "dam"],

        "hebrew_glossary": {
            "maqom": "Place (the unnamed 'place YHWH will choose' — Deuteronomy never names it, preserving the anticipation; it would be identified as Jerusalem in 2 Samuel 24 and 1 Kings 8)",
            "shem": "Name (YHWH 'puts his name' at the chosen place — in ANE theology, a deity's name represented the deity's presence and authority; Deuteronomy's 'name theology' asserts divine presence without divine limitation)",
            "bamot": "High places (hilltop shrines used in Canaanite worship — each served the allotted 'el of that locale; Israel must destroy them all and centralize worship at one place)",
            "matstsevah": "Standing stone / pillar (possibly phallic symbols associated with Canaanite fertility worship — part of the worship infrastructure of the allotted 'elohim)",
            "asherah": "Asherah pole (a sacred wooden pole or living tree associated with the Canaanite goddess Asherah, El's consort in Ugaritic mythology — represents the feminine divine in Canaanite religion)"
        },

        "ane_backdrop": "Centralized worship was unusual in the ANE. Most cultures had multiple shrines, "
                        "each associated with a local deity or a local manifestation of a major deity. "
                        "The Canaanite 'high places' (bamot) were hilltop shrines, often equipped with "
                        "standing stones (matstsevot), sacred poles (asherim), and altars. These served "
                        "the allotted 'elohim of each locale. Deuteronomy's centralization command — "
                        "one God, one place — is a deliberate theological statement: YHWH is not "
                        "distributed across the landscape like Baal or Asherah. His name-theology "
                        "('the place to put his name') draws on ANE concepts of divine name as "
                        "representative presence. In Mesopotamia, placing a deity's name on a "
                        "building signified ownership and presence. YHWH places his 'name' at the "
                        "chosen site — his presence dwells there, though he transcends any physical "
                        "location. Child sacrifice (12:31) is well-attested in the worship of Molech "
                        "at Canaanite tophet sites, confirmed archaeologically at Carthage and Pozo "
                        "Moro.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 4.8.5",
                "summary": "Josephus interprets the centralization command as requiring all "
                           "sacrifice to occur in Jerusalem alone, reflecting post-Josianic practice.",
                "relevance": "Shows how the general 'place God will choose' was concretized as "
                             "Jerusalem in Second Temple interpretation."
            },
            {
                "source": "4QMMT (Halakhic Letter)",
                "summary": "The Qumran sectarian letter that disputes with the Jerusalem priesthood "
                           "over proper worship practice at the central sanctuary.",
                "relevance": "Demonstrates that Deut 12's centralization was accepted by all parties — "
                             "the dispute was over WHO controlled the central sanctuary, not WHETHER "
                             "one was needed.",
                "canon": False
            },
            {
                "source": "Samaritan Pentateuch — Deut 12:5",
                "summary": "The SP reads 'the place God has chosen' (past tense) rather than 'will "
                           "choose' (future), identifying it as Mount Gerizim.",
                "relevance": "Illustrates the Jewish-Samaritan split over the location of the central "
                             "sanctuary — both communities accepted Deut 12's centralization principle."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 8:29", "note": "Solomon's prayer: 'My name shall be there' — identifying Jerusalem's temple as the Deut 12 'place'", "type": "ot"},
            {"ref": "2 Kings 22-23", "note": "Josiah's reform: destroying high places and centralizing worship in Jerusalem — direct fulfillment of Deut 12", "type": "ot"},
            {"ref": "John 4:20-24", "note": "Jesus to the Samaritan woman: 'Neither on this mountain nor in Jerusalem will you worship... true worshipers will worship in spirit and truth' — transcending the Deut 12 localization", "type": "nt"},
            {"ref": "2 Chronicles 7:12", "note": "God to Solomon: 'I have chosen this place for myself as a house of sacrifice'", "type": "ot"},
            {"ref": "Leviticus 18:21", "note": "Prohibition of child sacrifice to Molech — the practice Deut 12:31 condemns", "type": "ot"},
            {"ref": "Hebrews 13:10-14", "note": "'We have an altar from which those who serve the tent have no right to eat... let us go to him outside the camp' — the centralized worship transcended in Christ", "type": "nt"}
        ],

        "divine_council_note": "The centralization command of Deuteronomy 12 is a direct assertion of "
                               "YHWH's universal sovereignty against the territorial religion of the "
                               "allotted 'elohim. In the divine council worldview, each nation's allotted "
                               "'el had a local shrine — Chemosh in Moab, Dagon in Philistia, Marduk in "
                               "Babylon. These territorial 'elohim were worshipped at their assigned "
                               "locations. YHWH breaks this pattern by declaring that HE will choose "
                               "the location — worship is not tied to a geographic feature (mountain, "
                               "spring, grove) but to divine election. This foreshadows the ultimate "
                               "transcendence of all sacred geography in the New Covenant: Jesus tells "
                               "the Samaritan woman that worship will not be localized at all (John "
                               "4:21-24). The destruction of Canaanite worship sites (12:2-3) is the "
                               "dismantling of the allotted 'elohim's territorial infrastructure — "
                               "spiritual warfare expressed through physical demolition.",

        "sections": [
            {
                "heading": "Destroy All Canaanite Worship Sites (12:1-4)",
                "body": "Moses opens the specific stipulations with a comprehensive demolition order: "
                        "'You shall surely destroy all the places where the nations whom you shall "
                        "dispossess served their gods, on the high mountains and on the hills and "
                        "under every green tree. You shall tear down their altars and dash in pieces "
                        "their pillars and burn their Asherim with fire. You shall chop down the "
                        "carved images of their gods and destroy their name out of that place' "
                        "(12:2-3). Every element of Canaanite worship infrastructure must be "
                        "obliterated: the bamot (high places), matstsevot (standing stones — "
                        "possibly phallic symbols associated with fertility rites), asherim "
                        "(wooden poles or trees sacred to the goddess Asherah), and carved images. "
                        "The phrase 'destroy their name (shem) out of that place' is contrasted with "
                        "YHWH's command to 'put his name' at the chosen place (12:5). The names of "
                        "the allotted 'elohim must be erased; YHWH's name will replace them. The "
                        "decisive prohibition follows: 'You shall not worship the LORD your God in "
                        "that way' (12:4). The forms of Canaanite worship are not transferable to "
                        "YHWH — Israel cannot simply relabel the high places and keep worshipping as "
                        "the Canaanites did."
            },
            {
                "heading": "The Place God Will Choose — Name Theology (12:5-14)",
                "body": "The positive command: 'But you shall seek the place that the LORD your God "
                        "will choose out of all your tribes to put his name (shemo) and make his "
                        "habitation (shikno) there' (12:5). The 'name' theology (shem theology) is "
                        "distinctive to Deuteronomy. Rather than saying God dwells at the chosen site, "
                        "Deuteronomy says God puts his NAME there — a sophisticated theological "
                        "move that asserts divine presence without divine limitation. God's shem "
                        "represents him, makes him accessible, and claims the space as his own, "
                        "while God himself transcends any physical location. All burnt offerings, "
                        "sacrifices, tithes, contributions, votive offerings, and freewill offerings "
                        "must be brought to this single location (12:6). There, Israel will eat "
                        "'before the LORD your God' and 'rejoice in all that you put your hand to, "
                        "you and your households' (12:7). Worship is communal and joyful — not grim "
                        "obligation but celebration in God's presence. The refrain 'the place the "
                        "LORD your God will choose' appears over 20 times in Deuteronomy, always "
                        "without naming a specific site. The place will eventually be identified as "
                        "Jerusalem (2 Sam 24; 1 Kings 8), but Deuteronomy preserves the forward-looking "
                        "anticipation."
            },
            {
                "heading": "Sacred vs. Secular Slaughter (12:15-28)",
                "body": "Centralization creates a practical problem: if all sacrifice must occur at "
                        "one location, how do people far from the central sanctuary eat meat? Moses' "
                        "solution: 'However, you may slaughter and eat meat within any of your towns, "
                        "as much as you desire, according to the blessing of the LORD your God that "
                        "he has given you. The unclean and the clean may eat of it, as of the gazelle "
                        "and as of the deer' (12:15). Non-sacred slaughter for food is permitted "
                        "anywhere — the key distinction is between sacrificial slaughter (which must "
                        "occur at the central sanctuary) and ordinary slaughter for consumption (which "
                        "is unrestricted). The one prohibition: 'Only you shall not eat the blood. "
                        "You shall pour it out on the earth like water' (12:16). The blood prohibition "
                        "is absolute — blood represents life (nefesh) and belongs to God alone (Gen "
                        "9:4; Lev 17:11). This distinction between sacred and secular slaughter was "
                        "a significant development from the earlier system where all slaughter was "
                        "sacrificial (Lev 17:3-7). Deuteronomy adapts the legal code to the "
                        "practical reality of centralized worship in a large territory."
            },
            {
                "heading": "The Abomination of Child Sacrifice (12:29-32)",
                "body": "The chapter closes with the gravest warning: 'When the LORD your God cuts "
                        "off before you the nations whom you go in to dispossess, and you dispossess "
                        "them and dwell in their land, take care that you be not ensnared to follow "
                        "them... Do not inquire about their gods, saying, \"How did these nations serve "
                        "their gods? — that I also may do the same\"' (12:29-30). The curiosity itself "
                        "is dangerous. Then the reason: 'For every abominable thing that the LORD "
                        "hates they have done for their gods, for they even burn their sons and their "
                        "daughters in the fire to their gods' (12:31). Child sacrifice — attested "
                        "archaeologically at Carthaginian tophet sites and condemned throughout the "
                        "prophets (Jer 7:31; 19:5; Ezek 16:20-21) — is the ultimate perversion of "
                        "worship. It represents the logical endpoint of worshipping the allotted "
                        "'elohim: the beings to whom the nations were given have degraded those "
                        "nations to the point of sacrificing their own children. YHWH's response is "
                        "absolute: 'Everything that I command you, you shall be careful to do. You "
                        "shall not add to it or take from it' (12:32). The covenant terms are fixed."
            }
        ]
    },

    {
        "id": "deut-13",
        "ref": "Deuteronomy 13",
        "chapter_num": 13,
        "title": "The Test of Prophets — Guarding Against Spiritual Seduction",
        "era": "code",
        "type": "chapter",
        "themes": ["LAW", "SPIRIT", "DC"],

        "synopsis": "Deuteronomy 13 addresses the gravest internal threat to covenant loyalty: false "
                    "prophets and seducers who urge Israel to worship other gods. Three scenarios are "
                    "treated with escalating severity. First, a prophet who performs genuine signs and "
                    "wonders but uses them to redirect worship to other 'elohim (13:1-5) — he must be "
                    "executed, because God is testing Israel's loyalty. Second, a close family member "
                    "who secretly entices you to serve other gods (13:6-11) — even a beloved spouse or "
                    "child must be put to death, with you casting the first stone. Third, an entire "
                    "city that has gone after other gods (13:12-18) — the city must be devoted to "
                    "destruction (cherem), its inhabitants killed, its spoil burned, and the city never "
                    "rebuilt. The severity reflects the covenant stakes: apostasy is treason against "
                    "the Great King, and treason in a suzerainty treaty always carried the death "
                    "penalty. The chapter is also a remarkable acknowledgment that false prophets can "
                    "perform real supernatural acts — the test is not 'does the miracle happen?' but "
                    "'where does the prophet direct worship?' This presupposes the divine council "
                    "worldview: supernatural power is not exclusively YHWH's; the allotted 'elohim "
                    "can empower their prophets too.",

        "key_verse": {
            "ref": "Deuteronomy 13:3-4",
            "text": "You shall not listen to the words of that prophet or that dreamer of dreams. For the LORD your God is testing you, to know whether you love the LORD your God with all your heart and with all your soul. You shall walk after the LORD your God and fear him and keep his commandments and obey his voice, and you shall serve him and hold fast to him.",
            "translation": "ESV"
        },

        "hebrew_terms": ["navi", "cholem_chalom", "ot", "mofet", "nasah", "meisit", "cherem", "dibbek"],

        "hebrew_glossary": {
            "navi": "Prophet (one who speaks for God — the term may come from an Akkadian root meaning 'to call'; in the divine council framework, the true prophet has access to YHWH's council, while the false prophet speaks from unauthorized spiritual sources)",
            "ot": "Sign (a supernatural event intended to validate a prophet's message — critically, Deut 13 says the sign can be REAL yet the prophet FALSE; the test is not 'does the miracle happen?' but 'does the prophet direct worship to YHWH?')",
            "mofet": "Wonder / portent (a miraculous demonstration — paired with 'ot to describe supernatural credentials; even genuine wonders can come from non-YHWH sources in the divine council worldview)",
            "nasah": "Test / prove (God allows false prophets to test Israel's loyalty — the testing is deliberate: 'the LORD your God is testing you, to know whether you love the LORD your God with all your heart')",
            "bnei_beliyaal": "Sons of worthlessness / sons of Belial (the perpetrators of apostasy in 13:13 — later Jewish tradition personified Belial as a demonic figure; the term marks covenant rebels as spiritually aligned with chaos and opposition to YHWH)",
            "cherem": "Devoted destruction (applied in 13:15-16 to an entire apostate city — the most extreme covenant sanction: a spiritual cancer surgically removed to protect the nation's covenant with YHWH)"
        },

        "ane_backdrop": "The phenomenon of prophets who perform signs in the name of rival deities is "
                        "well-attested in the ANE. The Mari letters (18th century BC) contain reports "
                        "of ecstatic prophets (muhhum, apilum) who delivered oracles on behalf of "
                        "various deities, sometimes accompanied by signs. The Egyptian Admonitions of "
                        "Ipuwer describe social chaos partly caused by false prophetic activity. In "
                        "the Baal Cycle, the prophets of Baal perform ecstatic rituals to invoke "
                        "their deity. Deuteronomy 13's acknowledgment that false prophets can work "
                        "real signs parallels the Egyptian magicians' ability to replicate some of "
                        "Moses' signs (Exod 7:11-12, 22; 8:7). The execution of apostate cities "
                        "(cherem) parallels the treatment of rebellious vassal cities in Hittite "
                        "treaties, where refusal to honor the treaty was punished by total destruction.",

        "second_temple": [
            {
                "source": "11QTemple (Temple Scroll) 54:8-18",
                "summary": "The Temple Scroll expands the false prophet legislation of Deut 13, "
                           "adding details about investigation procedures and execution methods.",
                "relevance": "Shows that Qumran took the false prophet threat with absolute "
                             "seriousness and expanded the legal framework to address new scenarios.",
                "canon": False
            },
            {
                "source": "Mishnah Sanhedrin 7:10",
                "summary": "The Mishnah discusses the legal procedures for trying a mesit "
                           "(seducer/enticer) who leads others to idolatry.",
                "relevance": "Demonstrates that the Deut 13 categories (prophet, family enticer, "
                             "apostate city) remained active in rabbinic legal discussion."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 18:20-40", "note": "Elijah's contest with the prophets of Baal — the false prophets of a rival 'el", "type": "ot"},
            {"ref": "Matthew 7:15-23", "note": "Jesus warns of false prophets who prophesy in his name but are not known by him", "type": "nt"},
            {"ref": "Matthew 24:24", "note": "'False christs and false prophets will arise and perform great signs and wonders' — echoing Deut 13:1-2", "type": "nt"},
            {"ref": "2 Thessalonians 2:9", "note": "The lawless one comes 'with all power and false signs and wonders' — Deut 13 in eschatological form", "type": "nt"},
            {"ref": "1 John 4:1", "note": "'Test the spirits to see whether they are from God, for many false prophets have gone out into the world'", "type": "nt"},
            {"ref": "Jeremiah 23:9-32", "note": "Jeremiah's sustained polemic against false prophets who speak 'visions of their own minds'", "type": "ot"}
        ],

        "divine_council_note": "Deuteronomy 13 explicitly acknowledges that false prophets can "
                               "perform real signs and wonders (13:1-2). This is a crucial divine "
                               "council datum: supernatural power is not limited to YHWH. The allotted "
                               "'elohim — the 'sons of God' who received the nations in 32:8-9 — can "
                               "empower their prophets to perform genuine supernatural acts. The test "
                               "is not 'can the prophet work miracles?' but 'does the prophet direct "
                               "worship to YHWH?' God himself allows this testing 'to know whether you "
                               "love the LORD your God with all your heart' (13:3). This means the "
                               "divine council worldview has practical implications for discernment: "
                               "supernatural power alone does not validate a spiritual claim. Only "
                               "fidelity to YHWH validates a prophet. This principle carries directly "
                               "into the NT: even the Antichrist will perform signs and wonders (2 Thess "
                               "2:9; Rev 13:13-14), but the test remains the same — does the miracle-worker "
                               "confess Jesus Christ as Lord (1 John 4:1-3)?",

        "sections": [
            {
                "heading": "The False Prophet Who Works Signs (13:1-5)",
                "body": "The first scenario: 'If a prophet or a dreamer of dreams arises among you "
                        "and gives you a sign or a wonder, and the sign or wonder that he tells you "
                        "comes to pass, and if he says, \"Let us go after other gods... and let us "
                        "serve them,\" you shall not listen' (13:1-3). The sign comes true — the "
                        "miracle is real. But the direction of worship is wrong. This is the "
                        "foundational principle of prophetic discernment: theological fidelity "
                        "trumps miraculous credentials. God's reason for allowing this: 'the LORD "
                        "your God is testing (nasah) you, to know whether you love the LORD your God "
                        "with all your heart and with all your soul' (13:3). The test is the same as "
                        "the wilderness testing (8:2) — will Israel choose loyalty to YHWH over the "
                        "impressive display of a rival 'el's power? The penalty is death: 'that "
                        "prophet or that dreamer of dreams shall be put to death, because he has "
                        "taught rebellion against the LORD your God' (13:5). The charge is not false "
                        "prophecy per se but treason — 'rebellion' (sarah) against the covenant King."
            },
            {
                "heading": "The Secret Enticer — Even Family (13:6-11)",
                "body": "The second scenario is intimate and agonizing: 'If your brother, the son of "
                        "your mother, or your son or your daughter or the wife you embrace or your "
                        "friend who is as your own soul entices you secretly, saying, \"Let us go and "
                        "serve other gods\"... you shall not yield to him or listen to him, nor shall "
                        "your eye pity him, nor shall you spare him, nor shall you conceal him. But "
                        "you shall kill him. Your hand shall be first against him to put him to death' "
                        "(13:6-9). The list is deliberately comprehensive — brother, son, daughter, "
                        "wife, closest friend. No human relationship is above covenant loyalty. The "
                        "requirement that 'your hand shall be first' makes the judgment personal — "
                        "you cannot outsource this. The 'gods that you have not known, neither you "
                        "nor your fathers' (13:6) distinguishes these from the allotted 'elohim of "
                        "4:19-20 — these may be new spiritual claimants, previously unknown entities. "
                        "The purpose of the public execution: 'So all Israel shall hear and fear and "
                        "never again do any such wickedness' (13:11). Deterrence through severity — "
                        "the suzerainty treaty's enforcement mechanism."
            },
            {
                "heading": "The Apostate City — Total Destruction (13:12-18)",
                "body": "The third scenario is collective: 'If you hear in one of your cities... that "
                        "certain worthless fellows (b'nei veliyya'al) have gone out among you and "
                        "have drawn away the inhabitants of their city, saying, \"Let us go and serve "
                        "other gods\"...' (13:12-13). The term b'nei veliyya'al ('sons of worthlessness' "
                        "or 'sons of Belial') becomes a technical designation for covenant rebels in "
                        "later biblical literature. The procedure: first, 'inquire and make search and "
                        "ask diligently' (13:14) — investigation is required before judgment. If "
                        "confirmed: 'you shall surely strike the inhabitants of that city with the "
                        "edge of the sword, devoting it to destruction (cherem), all who are in it "
                        "and its cattle' (13:15). The spoil must be gathered and burned publicly, and "
                        "'it shall be a heap forever. It shall not be built again' (13:16). The city "
                        "becomes a permanent monument to the consequences of collective apostasy. The "
                        "purpose: 'that the LORD may turn from the fierceness of his anger and show "
                        "you mercy and have compassion on you and multiply you' (13:17). The cherem "
                        "of one city protects the nation — surgical removal of a spiritual cancer."
            }
        ]
    },

    {
        "id": "deut-14",
        "ref": "Deuteronomy 14",
        "chapter_num": 14,
        "title": "Holy Identity — Dietary Laws and the Tithe",
        "era": "code",
        "type": "chapter",
        "themes": ["HOLY", "LAW"],

        "synopsis": "Deuteronomy 14 grounds Israel's distinctive practices in their identity as God's "
                    "children and holy people. The chapter opens: 'You are the sons (banim) of the "
                    "LORD your God' (14:1) — familial language that establishes the theological basis "
                    "for everything that follows. Because Israel belongs to God as children to a "
                    "father, they must not engage in pagan mourning rituals (cutting themselves, "
                    "shaving the head for the dead, 14:1). Because they are 'a people holy to the "
                    "LORD' and his 'treasured possession' (14:2), they observe dietary distinctions "
                    "that set them apart from the nations. The clean/unclean animal lists (14:3-21) "
                    "largely parallel Leviticus 11 with minor variations. The principle is not "
                    "hygiene but holiness — Israel eats differently because Israel IS different. "
                    "The chapter then addresses the tithe system (14:22-29): a tenth of all produce "
                    "is to be consumed before YHWH at the central sanctuary in a communal celebration "
                    "(14:23-26). Every third year, the tithe is stored locally for the Levite, the "
                    "sojourner, the fatherless, and the widow (14:28-29). The tithe is simultaneously "
                    "worship (eating before YHWH), education ('that you may learn to fear the LORD'), "
                    "and social justice (provision for the vulnerable).",

        "key_verse": {
            "ref": "Deuteronomy 14:1-2",
            "text": "You are the sons of the LORD your God. You shall not cut yourselves or make any baldness on your foreheads for the dead. For you are a people holy to the LORD your God, and the LORD has chosen you to be a people for his treasured possession, out of all the peoples who are on the face of the earth.",
            "translation": "ESV"
        },

        "hebrew_terms": ["banim", "am_qadosh", "segullah", "tahor", "tamei", "ma'aser", "maakhal", "geulah"],

        "hebrew_glossary": {
            "banim": "Sons / children (Israel is called 'sons of the LORD your God' in 14:1 — a divine council term: in 32:8 the nations are allotted to the 'sons of God' (divine council members), but here ISRAEL is called God's sons; this places Israel in the divine council family structure)",
            "am_qadosh": "Holy people (a people set apart, belonging to God — holiness in Hebrew means separation for divine use, not moral perfection; Israel is holy because God chose them, not because they earned it)",
            "segullah": "Treasured possession (a king's personal, private treasure — the Akkadian cognate sikkiltum refers to royal private property; Israel is YHWH's personal treasure among all nations)",
            "tahor": "Clean / pure (ritually fit for contact with the holy — the dietary clean/unclean distinction creates a daily, embodied reminder that Israel is different from the nations)",
            "tamei": "Unclean / impure (ritually unfit for sacred contact — not inherently sinful, but requiring purification before approaching the holy; the system reinforces the boundary between common and sacred)",
            "maaser": "Tithe / tenth (a tenth of agricultural produce devoted to YHWH — in Deut 14, the tithe is consumed communally at the central sanctuary as a joyful celebration, not merely a tax)"
        },

        "ane_backdrop": "Self-laceration and shaving as mourning practices are well-attested in the "
                        "ANE. Ugaritic texts describe the god El cutting himself in mourning for Baal: "
                        "'He cuts his skin with a stone, with a razor he cuts his cheek and chin.' "
                        "These practices were associated with communion with the dead and possibly "
                        "with the cult of the dead (ancestor worship). Deuteronomy prohibits them "
                        "because Israel's identity is defined by their relationship with YHWH, not "
                        "with the dead. The dietary laws have been variously explained: symbolic "
                        "(Mary Douglas — categories reflect creation order), hygienic (Maimonides), "
                        "anti-pagan (avoiding animals associated with foreign cult), and boundary-marking "
                        "(creating a distinct Israelite identity). The ANE background suggests that "
                        "many of the prohibited animals were associated with the worship of particular "
                        "deities — the pig with Canaanite chthonic cults, the eagle with solar deities.",

        "second_temple": [
            {
                "source": "Letter of Aristeas 128-171",
                "summary": "Aristeas provides an allegorical interpretation of the dietary laws, "
                           "arguing that they teach moral virtues: predatory birds teach against "
                           "violence, ruminants teach about meditation on Torah.",
                "relevance": "Shows how Hellenistic Judaism rationalized the dietary laws for a "
                             "Greek-speaking audience while maintaining their observance."
            },
            {
                "source": "4QMMT (Halakhic Letter) B 13-17",
                "summary": "Addresses specific dietary and purity questions that divided the "
                           "Qumran community from the Jerusalem priesthood.",
                "relevance": "Demonstrates that the interpretation of Deut 14's dietary laws was "
                             "a matter of sectarian dispute in the Second Temple period.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Leviticus 11:1-47", "note": "The parallel clean/unclean animal list — Deut 14 draws on and slightly modifies Leviticus 11", "type": "ot"},
            {"ref": "Acts 10:9-16", "note": "Peter's vision: 'What God has made clean, do not call common' — the dietary laws transcended in the new covenant", "type": "nt"},
            {"ref": "Mark 7:14-23", "note": "Jesus: 'There is nothing outside a person that by going into him can defile him' — declaring all foods clean", "type": "nt"},
            {"ref": "Romans 14:14-17", "note": "Paul: 'Nothing is unclean in itself... the kingdom of God is not a matter of eating and drinking'", "type": "nt"},
            {"ref": "1 Corinthians 8:7-13", "note": "The conscience-based approach to food offered to idols — the NT resolution of the Deut 14 principle", "type": "nt"},
            {"ref": "Malachi 3:8-10", "note": "'Will a man rob God? Yet you are robbing me... in your tithes and contributions' — the tithe system Deut 14 establishes", "type": "ot"}
        ],

        "divine_council_note": "The opening declaration 'You are the sons (banim) of the LORD your God' "
                               "(14:1) is striking in the divine council context. In Deuteronomy 32:8 "
                               "(DSS), the nations are allotted to the 'sons of God' (b'nei 'elohim) — "
                               "divine council members. Here, ISRAEL is called 'sons of God' — a "
                               "designation that places Israel in a unique position within the divine "
                               "council framework. Israel is not merely YHWH's vassal nation; Israel is "
                               "his family. This son-language has enormous christological implications: "
                               "Christ is THE Son of God (unique divine council member), and through him, "
                               "believers become 'sons of God' (Gal 3:26; Rom 8:14-17) — recovering the "
                               "Deuteronomic identity at a cosmic level. The dietary laws and mourning "
                               "prohibitions mark Israel as distinct from the nations governed by the "
                               "allotted 'elohim — behavioral boundaries that reinforce spiritual "
                               "identity.",

        "sections": [
            {
                "heading": "Sons of God — Mourning Practices Forbidden (14:1-2)",
                "body": "The chapter opens with identity before ethics: 'You are the sons (banim) of "
                        "the LORD your God' (14:1). Identity precedes behavior — what you ARE determines "
                        "what you DO. Two mourning practices are forbidden: cutting oneself (hitgoded, "
                        "self-laceration) and shaving the forehead for the dead (14:1b). Both were "
                        "associated with pagan mourning rites that involved communion with the dead "
                        "and the gods of the underworld. In Ugaritic literature, even the gods engaged "
                        "in self-laceration during mourning. Israel must mourn differently because "
                        "Israel belongs to YHWH, not to the spirits of the dead or the chthonic "
                        "deities. The theological basis is restated: 'For you are a people holy to "
                        "the LORD your God, and the LORD has chosen you to be a people for his "
                        "treasured possession (am segullah)' (14:2). Holiness (qedushah) means "
                        "separation — not monastic withdrawal but distinctive identity within the "
                        "world of nations."
            },
            {
                "heading": "Clean and Unclean Animals (14:3-21)",
                "body": "The dietary laws classify animals into clean (permitted for consumption) and "
                        "unclean (forbidden). Land animals must both chew the cud AND have split hooves "
                        "(14:6). The exceptions that fail one criterion are listed: the camel, hare, "
                        "and rock badger chew the cud but lack split hooves; the pig has split hooves "
                        "but does not chew the cud (14:7-8). Water creatures must have fins AND scales "
                        "(14:9-10). Forbidden birds are listed individually — mostly raptors and "
                        "scavengers (14:11-18). Winged insects are generally forbidden except those "
                        "that hop (14:19-20). 'You shall not eat anything that has died naturally' "
                        "(14:21a) — the prohibition against eating carrion maintains the blood "
                        "prohibition (the blood was not properly drained). The final dietary rule: "
                        "'You shall not boil a young goat in its mother's milk' (14:21b). This "
                        "prohibition, found three times in the Torah (Exod 23:19; 34:26; Deut 14:21), "
                        "may reflect a Canaanite fertility ritual (though the alleged Ugaritic parallel "
                        "is now disputed). It became the basis for the rabbinic separation of meat and "
                        "dairy in kosher law."
            },
            {
                "heading": "The Festival Tithe — Eating Before YHWH (14:22-27)",
                "body": "The tithe command follows the dietary laws, linking what Israel eats to how "
                        "Israel worships: 'You shall tithe all the yield of your seed that comes from "
                        "the field year by year. And you shall eat the tithe of your grain, of your "
                        "wine, and of your oil, and the firstborn of your herd and flock, before the "
                        "LORD your God, in the place that he will choose, to make his name dwell there' "
                        "(14:22-23). This tithe is consumed by the worshipper's household at the "
                        "central sanctuary — it is a communal feast in God's presence. If the journey "
                        "is too long, the tithe may be converted to money, and the money used to buy "
                        "'whatever you desire — oxen or sheep or wine or strong drink' (14:26). The "
                        "mention of 'strong drink' (shekar) confirms this as a joyful celebration, "
                        "not ascetic obligation. The Levite must not be neglected: 'he has no portion "
                        "or inheritance with you' (14:27) — because YHWH is the Levite's inheritance."
            },
            {
                "heading": "The Third-Year Tithe — Social Justice (14:28-29)",
                "body": "Every third year, the tithe is stored locally rather than taken to the central "
                        "sanctuary: 'The Levite, because he has no portion or inheritance with you, and "
                        "the sojourner, the fatherless, and the widow, who are within your towns, shall "
                        "come and eat and be filled, that the LORD your God may bless you' (14:29). "
                        "The four vulnerable categories — Levite, sojourner (ger), fatherless (yatom), "
                        "and widow (almanah) — form a standard Deuteronomic formula for those without "
                        "economic security. The third-year tithe is Deuteronomy's social safety net, "
                        "funded by the covenant community's agricultural surplus. This is not charity "
                        "but covenantal obligation — care for the vulnerable is as much a treaty "
                        "stipulation as centralized worship or exclusive loyalty."
            }
        ]
    },

    {
        "id": "deut-15",
        "ref": "Deuteronomy 15",
        "chapter_num": 15,
        "title": "Release and Generosity — The Sabbatical Year and the Open Hand",
        "era": "code",
        "type": "chapter",
        "themes": ["LAW", "LAND", "TYPE", "LOVE"],

        "synopsis": "Deuteronomy 15 legislates economic generosity as a covenant requirement. Every "
                    "seventh year, debts must be released (shemittah) — a radical economic reset that "
                    "prevents permanent debt bondage (15:1-6). Moses directly addresses the human "
                    "resistance to this law: 'Take care lest there be an unworthy thought in your "
                    "heart... \"The seventh year, the year of release is near,\" and your eye look "
                    "grudgingly on your poor brother, and you give him nothing' (15:9). The command "
                    "to open-handedness is emphatic: 'You shall open wide your hand to your brother, "
                    "to the needy and to the poor, in your land' (15:11). Hebrew slaves must be "
                    "released in the seventh year with generous provision — 'You shall furnish him "
                    "liberally out of your flock, your threshing floor, and your winepress' (15:14). "
                    "The theological motivation is the exodus: 'You shall remember that you were a "
                    "slave in the land of Egypt, and the LORD your God redeemed you' (15:15). Israel "
                    "must treat others as God treated them. The chapter closes with the firstborn "
                    "animal law: every firstborn male is consecrated to YHWH and eaten at the "
                    "central sanctuary (15:19-23).",

        "key_verse": {
            "ref": "Deuteronomy 15:11",
            "text": "For there will never cease to be poor in the land. Therefore I command you, 'You shall open wide your hand to your brother, to the needy and to the poor, in your land.'",
            "translation": "ESV"
        },

        "hebrew_terms": ["shemittah", "eved", "chofshi", "ani", "evyon", "berakhah", "bekhor", "patoach_tiftach"],

        "hebrew_glossary": {
            "shemittah": "Release / letting go (the sabbatical year debt cancellation — every seventh year, debts between Israelites are released; the word comes from the root shamat, 'to let drop'; a radical economic reset with no parallel in ANE law codes)",
            "eved": "Servant / slave (a Hebrew who sells himself into service due to poverty — Deuteronomy limits servitude to six years and requires generous provision upon release; the exodus motivation transforms master-slave relations: 'remember that you were a slave in Egypt')",
            "chofshi": "Free / liberated (the status of a released servant — YHWH's character as liberator means Israel must practice liberation; the God who freed them from Egypt commands them to free their own servants)",
            "evyon": "Poor / needy (the economically vulnerable in the covenant community — Deuteronomy does not idealize poverty but commands generous response: 'you shall open wide your hand to your brother, to the needy and to the poor')",
            "patoach_tiftach": "You shall surely open (the emphatic Hebrew construction: infinitive absolute + finite verb — 'opening you shall open' your hand; the doubled form intensifies the command, making generosity non-negotiable)"
        },

        "ane_backdrop": "Debt release and manumission were known in the ANE. Mesopotamian kings "
                        "proclaimed 'andurarum' (liberty) decrees that cancelled debts and freed debt "
                        "slaves — attested from Hammurabi (18th century BC) onward. These were "
                        "typically royal proclamations at the beginning of a reign or at moments of "
                        "crisis. Deuteronomy systematizes what was an occasional royal act into a "
                        "regular seven-year cycle — democratizing economic justice. The generosity "
                        "provisions go beyond anything in ANE law codes, which typically regulated "
                        "debt and slavery but did not command generosity of spirit.",

        "second_temple": [
            {
                "source": "Hillel's Prozbul (1st century BC)",
                "summary": "The rabbi Hillel created a legal mechanism to allow loans to continue "
                           "past the sabbatical year, acknowledging that Deut 15's debt release was "
                           "causing lenders to stop lending.",
                "relevance": "Shows both the ongoing authority of Deut 15 in Jewish law and the "
                             "practical difficulty of implementing radical debt release in a "
                             "commercial economy."
            },
            {
                "source": "4Q159 (Ordinances)",
                "summary": "A Qumran legal text that discusses debt release practices, likely "
                           "reflecting community application of Deut 15.",
                "relevance": "Confirms that the sabbatical year was observed at Qumran as part of "
                             "their Torah-observant community life.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Leviticus 25:1-55", "note": "The Jubilee legislation — the 50th-year super-sabbatical that extends Deut 15's principles", "type": "ot"},
            {"ref": "Matthew 26:11", "note": "Jesus: 'The poor you always have with you' — quoting Deut 15:11", "type": "nt"},
            {"ref": "Luke 4:18-19", "note": "Jesus' Nazareth manifesto: 'to proclaim liberty to the captives... the year of the Lord's favor' — Jubilee/sabbatical fulfillment", "type": "nt"},
            {"ref": "Philemon 1:15-16", "note": "Paul sends the slave Onesimus back 'no longer as a bondservant but... as a beloved brother' — the spirit of Deut 15", "type": "nt"},
            {"ref": "Nehemiah 5:1-13", "note": "Nehemiah enforces debt release according to Deuteronomic principles", "type": "ot"},
            {"ref": "Jeremiah 34:8-22", "note": "Zedekiah proclaimed liberty for Hebrew slaves then revoked it — violating Deut 15 with catastrophic consequences", "type": "ot"}
        ],

        "divine_council_note": "The sabbatical year legislation in Deuteronomy 15 reflects YHWH's "
                               "character as a God who liberates — the same character that distinguished "
                               "him from the allotted 'elohim of the nations. While the gods of Mesopotamia "
                               "created humans as slave labor (Atrahasis), YHWH redeemed slaves (the "
                               "exodus) and commands that slavery itself be limited and ultimately resolved. "
                               "The open-hand ethic (15:7-11) reflects the character of the God who judges "
                               "the 'elohim in Psalm 82 precisely for their failure to defend the poor "
                               "and needy (Ps 82:3-4). Israel's economic justice is meant to model what "
                               "the allotted 'elohim failed to provide for their nations.",

        "sections": [
            {
                "heading": "The Sabbatical Year Debt Release (15:1-6)",
                "body": "At the end of every seven years you shall grant a release (shemittah). Every "
                        "creditor shall release what he has lent to his neighbor' (15:1-2). The scope "
                        "is defined: this applies to fellow Israelites, not foreigners (15:3) — a "
                        "distinction that reflects the covenant community's internal obligations. "
                        "Moses adds the ideal vision: 'there will be no poor among you' (15:4) if "
                        "Israel fully obeys — followed by the realistic acknowledgment: 'there will "
                        "never cease to be poor in the land' (15:11). This tension between the ideal "
                        "and the real is characteristic of Deuteronomy's theology: the law envisions "
                        "what SHOULD be while addressing what IS."
            },
            {
                "heading": "Generous Lending Despite the Coming Release (15:7-11)",
                "body": "Moses anticipates the calculation that would undermine the law: 'If among you, "
                        "one of your brothers should become poor... you shall not harden your heart or "
                        "shut your hand against your poor brother, but you shall open your hand to him "
                        "and lend him sufficient for his need' (15:7-8). The specific temptation: 'Take "
                        "care lest there be an unworthy thought (devar beliyya'al) in your heart and "
                        "you say, \"The seventh year, the year of release is near,\" and your eye look "
                        "grudgingly on your poor brother' (15:9). The phrase devar beliyya'al ('worthless "
                        "thought') uses the same beliyya'al that described the seducers in 13:13. "
                        "Refusing to lend near the sabbatical year is classified with apostasy — it is "
                        "a 'Belial thought.' The corrective: 'You shall give to him freely, and your "
                        "heart shall not be grudging when you give to him' (15:10). Generosity must be "
                        "internal, not merely external."
            },
            {
                "heading": "Release of Hebrew Servants (15:12-18)",
                "body": "A Hebrew who sells himself into service must be released in the seventh year — "
                        "and not empty-handed: 'You shall furnish him liberally out of your flock, your "
                        "threshing floor, and your winepress. As the LORD your God has blessed you, "
                        "you shall give to him' (15:14). The motivation: 'You shall remember that you "
                        "were a slave in Egypt, and the LORD your God redeemed you; therefore I command "
                        "you this today' (15:15). Israel's treatment of slaves must mirror God's "
                        "treatment of Israel — liberation with provision. If the servant chooses to "
                        "stay permanently, the ceremony of piercing the ear with an awl against the "
                        "door (15:17) marks lifelong voluntary service. This is the background for "
                        "Psalm 40:6 ('My ears you have opened/pierced') and its application to Christ "
                        "in Hebrews 10:5-7."
            },
            {
                "heading": "Firstborn Animals (15:19-23)",
                "body": "Every firstborn male of herd and flock is consecrated to YHWH: 'You shall do "
                        "no work with the firstborn of your herd, nor shear the firstborn of your "
                        "flock' (15:19). They are eaten 'before the LORD your God, in the place that "
                        "the LORD will choose' (15:20). If the animal is blemished, it is eaten locally "
                        "but not sacrificed (15:21-22). The blood prohibition is restated: 'Only you "
                        "shall not eat its blood; you shall pour it out on the ground like water' "
                        "(15:23). The firstborn principle — the first belongs to God — extends the "
                        "theological logic of the tithe: God's claim comes first."
            }
        ]
    },

    {
        "id": "deut-16",
        "ref": "Deuteronomy 16",
        "chapter_num": 16,
        "title": "The Three Pilgrimage Festivals and the Pursuit of Justice",
        "era": "code",
        "type": "chapter",
        "themes": ["TYPE", "LAW", "REMEMBER", "BLOOD"],

        "synopsis": "Deuteronomy 16 prescribes the three annual pilgrimage festivals: Passover/ "
                    "Unleavened Bread (16:1-8), the Feast of Weeks/Shavuot (16:9-12), and the "
                    "Feast of Booths/Sukkot (16:13-17). Each festival requires Israel to appear "
                    "'before the LORD your God at the place that he will choose' (16:16), reinforcing "
                    "the centralization command of chapter 12. Each festival commemorates God's saving "
                    "acts and agricultural provision: Passover remembers the exodus, Weeks celebrates "
                    "the grain harvest (later associated with the giving of the Torah at Sinai), and "
                    "Booths celebrates the ingathering and the wilderness sojourn. The chapter closes "
                    "with the appointment of judges and the famous justice command: 'Justice, justice "
                    "shall you pursue (tsedek tsedek tirdof)' (16:20) — the doubling emphasizing "
                    "intensity and urgency. The festivals and the justice system are placed together "
                    "because both are expressions of covenant life: worship and justice are inseparable "
                    "in Deuteronomy's theology.",

        "key_verse": {
            "ref": "Deuteronomy 16:20",
            "text": "Justice, and only justice, you shall follow, that you may live and inherit the land that the LORD your God is giving you.",
            "translation": "ESV"
        },

        "hebrew_terms": ["pesach", "matzot", "shavuot", "sukkot", "chag", "tsedek", "shofet", "aliyah_laregel"],

        "hebrew_glossary": {
            "pesach": "Passover (from the verb pasach, 'to pass over' or 'to protect' — commemorating YHWH's protection of Israelite firstborn while striking Egypt's; the lamb's blood on the doorposts marked those under YHWH's protection vs. those under Egypt's gods' jurisdiction)",
            "matzot": "Unleavened bread (bread made without yeast, 'the bread of affliction' — eaten for seven days after Passover to remember the haste of the exodus; leaven later became a metaphor for corruption, Matt 16:6)",
            "shavuot": "Feast of Weeks / Pentecost (seven weeks after the grain harvest begins — later associated with the giving of Torah at Sinai; the Holy Spirit was poured out on this feast day in Acts 2, connecting Torah-giving with Spirit-giving)",
            "sukkot": "Feast of Booths / Tabernacles (the autumn harvest festival where Israel dwells in temporary shelters — remembering the wilderness wandering; the most joyful of the three pilgrimage festivals)",
            "tsedek": "Justice / righteousness (the famous doubled command: tsedek tsedek tirdof, 'justice, justice you shall pursue' — the repetition emphasizes that justice is not optional but must be actively hunted down; it will not happen passively)",
            "aliyah_laregel": "Pilgrimage (literally 'going up on foot' — the three annual journeys to the central sanctuary; every male was required to appear before YHWH and 'not appear empty-handed')"
        },

        "ane_backdrop": "Pilgrimage festivals were common in ANE religions. The Babylonian Akitu "
                        "(New Year) festival required the Marduk statue to be processed through "
                        "Babylon to the temple. Egyptian festivals involved processions of the god's "
                        "barque from temple to temple. Israel's festivals are distinctive in their "
                        "historical-commemorative character: they remember specific saving events "
                        "(exodus, wilderness, harvest), not mythological cycles. The spring festival "
                        "(Passover) coincides with barley harvest; the early summer festival (Weeks) "
                        "with wheat harvest; the autumn festival (Booths) with the grape and olive "
                        "ingathering. This agricultural calendar parallels the Gezer Calendar "
                        "(10th century BC) and reflects the agrarian rhythm of ancient Israel.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 17.9.3",
                "summary": "Josephus describes the massive pilgrimage crowds at Passover in "
                           "Jerusalem, estimating millions of attendees.",
                "relevance": "Shows how Deut 16's pilgrimage command was implemented on a massive "
                             "scale at the Jerusalem temple in the late Second Temple period."
            },
            {
                "source": "Jubilees 49:1-22",
                "summary": "Jubilees provides detailed regulations for Passover observance, "
                           "insisting it must be celebrated at the sanctuary.",
                "relevance": "Confirms the centralization requirement for Passover specifically, "
                             "as prescribed in Deut 16:2."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 12:1-28", "note": "The original Passover legislation — Deut 16 adapts it for centralized worship", "type": "ot"},
            {"ref": "Acts 2:1-4", "note": "Pentecost (Feast of Weeks/Shavuot) — the Holy Spirit descends on the pilgrimage festival, fulfilling Deut 16's Weeks celebration", "type": "nt"},
            {"ref": "John 7:37-39", "note": "Jesus' proclamation at the Feast of Booths: 'If anyone thirsts, let him come to me and drink'", "type": "nt"},
            {"ref": "1 Corinthians 5:7", "note": "'Christ, our Passover lamb, has been sacrificed' — christological fulfillment of Deut 16's Passover", "type": "nt"},
            {"ref": "Amos 5:21-24", "note": "'Let justice roll down like waters' — the prophetic demand that worship (festivals) and justice (16:18-20) be united", "type": "ot"},
            {"ref": "Isaiah 1:13-17", "note": "God rejects festivals without justice — the inseparability Deut 16 establishes", "type": "ot"}
        ],

        "divine_council_note": "The three pilgrimage festivals are acts of covenant renewal that "
                               "reinforce Israel's unique relationship with YHWH against the claims "
                               "of the allotted 'elohim. The surrounding nations had their own festival "
                               "calendars honoring their patron deities (Baal's autumnal enthronement "
                               "festival in Ugarit, Marduk's Akitu in Babylon). Israel's festivals "
                               "deliberately counter these: Passover celebrates liberation from Egypt "
                               "(whose gods YHWH defeated — Exod 12:12, 'against all the gods of Egypt "
                               "I will execute judgments'), Weeks celebrates YHWH's agricultural "
                               "provision (displacing Baal's claim as fertility god), and Booths "
                               "remembers God's wilderness care (proving YHWH sustains his people "
                               "even outside any allotted 'el's territory). Pentecost in Acts 2 "
                               "reverses the Deuteronomy 32 allotment: representatives of 'every "
                               "nation under heaven' (Acts 2:5) receive the Spirit at the Weeks "
                               "festival — the nations are being reclaimed from their allotted 'elohim.",

        "sections": [
            {
                "heading": "Passover and Unleavened Bread (16:1-8)",
                "body": "The Passover must be observed 'in the month of Abib, for in the month of "
                        "Abib the LORD your God brought you out of Egypt by night' (16:1). The "
                        "sacrifice must be offered 'at the place that the LORD will choose, to make "
                        "his name dwell there' (16:2) — centralizing what was originally a household "
                        "celebration (Exod 12). Seven days of unleavened bread follow, with a solemn "
                        "assembly on the seventh day (16:8). The unleavened bread is 'the bread of "
                        "affliction — for you came out of Egypt in haste' (16:3). The haste motif "
                        "connects to the urgency of the exodus — there was no time for bread to rise."
            },
            {
                "heading": "Feast of Weeks / Shavuot (16:9-12)",
                "body": "Seven weeks after the sickle is first put to the standing grain, Israel "
                        "celebrates the wheat harvest (16:9). The offering is a freewill contribution "
                        "'in proportion to the blessing that the LORD your God has given you' (16:10). "
                        "The celebration is communal and inclusive: 'you and your son and your daughter, "
                        "your male servant and your female servant, the Levite, the sojourner, the "
                        "fatherless, and the widow' (16:11). Everyone participates; no one is excluded. "
                        "The exodus memory again: 'You shall remember that you were a slave in Egypt' "
                        "(16:12). Gratitude for harvest + memory of slavery = generosity to the "
                        "vulnerable."
            },
            {
                "heading": "Feast of Booths / Sukkot (16:13-17)",
                "body": "The seven-day autumn festival celebrates the final ingathering: 'after you "
                        "have gathered in your grain and your wine' (16:13). The inclusivity formula "
                        "repeats (16:14). 'You shall be altogether joyful' (16:15) — Sukkot is the "
                        "most joyful of the festivals. The summary rule for all three pilgrimage "
                        "festivals: 'Three times a year all your males shall appear before the LORD "
                        "your God at the place that he will choose... They shall not appear before "
                        "the LORD empty-handed. Every man shall give as he is able, according to the "
                        "blessing of the LORD your God that he has given you' (16:16-17). Worship "
                        "requires offering — not as payment but as proportional response to grace."
            },
            {
                "heading": "Justice, Justice You Shall Pursue (16:18-22)",
                "body": "Judges and officers are to be appointed 'in all your towns that the LORD your "
                        "God is giving you, according to your tribes, and they shall judge the people "
                        "with righteous judgment' (16:18). The standards: 'You shall not pervert "
                        "justice. You shall not show partiality, and you shall not accept a bribe' "
                        "(16:19). Then the memorable commandment: 'Justice, justice (tsedek tsedek) "
                        "you shall pursue (tirdof), that you may live and inherit the land' (16:20). "
                        "The doubling of tsedek is emphatic — 'justice and nothing but justice.' The "
                        "verb tirdof ('pursue, chase') implies active effort. Justice does not happen "
                        "passively; it must be hunted down. The section concludes with a prohibition "
                        "of Asherah poles and pillars beside YHWH's altar (16:21-22) — pairing "
                        "justice with pure worship, because both are covenant requirements."
            }
        ]
    },

    {
        "id": "deut-17",
        "ref": "Deuteronomy 17",
        "chapter_num": 17,
        "title": "Courts, the King, and the Torah — Limiting Human Power",
        "era": "code",
        "type": "chapter",
        "themes": ["KING", "LAW", "COV"],

        "synopsis": "Deuteronomy 17 addresses governance: the central court (17:8-13) and the kingship "
                    "law (17:14-20). Difficult legal cases beyond the local courts' competence must be "
                    "brought to the central sanctuary, where the Levitical priests and the judge will "
                    "render a binding verdict (17:8-12). Refusal to accept the central court's ruling "
                    "is punishable by death (17:12) — maintaining the authority of the covenant's "
                    "judicial system. The kingship law (17:14-20) is unique in the ancient world: no "
                    "other ANE legal code limits the king's power. The king must be chosen by YHWH "
                    "(17:15), must be an Israelite (not a foreigner), must not multiply horses (military "
                    "power), must not multiply wives (political alliances), must not multiply silver "
                    "and gold (economic power), and — most remarkably — must write a personal copy of "
                    "this Torah and 'read in it all the days of his life, that he may learn to fear "
                    "the LORD his God' (17:18-19). The king is not above the law; he is the law's most "
                    "diligent student. This law envisions a constitutional monarchy where Torah is the "
                    "constitution and YHWH is the true King.",

        "key_verse": {
            "ref": "Deuteronomy 17:18-19",
            "text": "And when he sits on the throne of his kingdom, he shall write for himself in a book a copy of this law, approved by the Levitical priests. And it shall be with him, and he shall read in it all the days of his life, that he may learn to fear the LORD his God by keeping all the words of this law and these statutes.",
            "translation": "ESV"
        },

        "hebrew_terms": ["melekh", "mishneh_hatorah", "kohen", "shofet", "hofea", "ra'ah", "miqrev_achekha"],

        "hebrew_glossary": {
            "melekh": "King (the human ruler under Torah — uniquely in the ANE, Deuteronomy's king is NOT the source of law but its most devoted student; YHWH is the true King, the human melekh is a vice-regent under covenant)",
            "mishneh_hatorah": "Copy of this law / second law (the king's personal copy of the Torah that he must write by hand and read daily — the LXX translated this as deuteronomion, 'second law,' giving the book its English name)",
            "kohen": "Priest (a member of the tribe of Levi set apart for sanctuary service — the Levitical priests serve as the guardians and teachers of Torah; the central court's authority rests with them alongside the judge)",
            "miqrev_achekha": "From among your brothers (the king must be a fellow Israelite — not a foreigner, because a foreign king would serve a foreign 'el; the king must remain within YHWH's covenant jurisdiction)"
        },

        "ane_backdrop": "Deuteronomy 17's kingship law has no parallel in ANE literature. Mesopotamian "
                        "kings claimed divine appointment and sometimes divine descent. Egyptian "
                        "pharaohs were considered gods incarnate. No known ANE legal text restricts "
                        "the king's military, marital, or economic power. The closest parallel is the "
                        "Mesopotamian 'mirror for princes' genre (naru literature), which advised kings "
                        "on just rule but lacked legal force. Deuteronomy's king is under the Torah — "
                        "he is not the source of law but its most devoted subject. The term mishneh "
                        "hatorah ('copy of this law,' 17:18) is the origin of the LXX title "
                        "'Deuteronomium' (second law). The king's hand-written copy parallels the "
                        "treaty-deposit requirement in ANE diplomacy: both suzerain and vassal kept "
                        "copies of the treaty.",

        "second_temple": [
            {
                "source": "11QTemple (Temple Scroll) 56-59",
                "summary": "The Temple Scroll significantly expands the kingship law, adding "
                           "detailed regulations about the king's council, army, and war conduct.",
                "relevance": "Shows that Qumran saw the Deut 17 kingship law as foundational and "
                             "sought to develop it into a comprehensive royal constitution.",
                "canon": False
            },
            {
                "source": "Josephus, Antiquities 4.8.17",
                "summary": "Josephus presents the kingship law as a model of just governance, "
                           "emphasizing the king's obligation to obey the priests' Torah instruction.",
                "relevance": "Illustrates Second Temple understanding of the king as Torah-subject "
                             "rather than Torah-source."
            }
        ],

        "cross_refs": [
            {"ref": "1 Samuel 8:10-18", "note": "Samuel warns of the king's abuses — the very things Deut 17 prohibits", "type": "ot"},
            {"ref": "1 Kings 10:26-11:8", "note": "Solomon violates every provision of the kingship law: horses, wives, gold", "type": "ot"},
            {"ref": "2 Kings 22:8-13", "note": "Josiah discovers 'the Book of the Law' and reforms — the rediscovery of Deut 17's Torah-centered kingship", "type": "ot"},
            {"ref": "John 18:36", "note": "Jesus: 'My kingdom is not of this world' — transcending the Deut 17 kingship", "type": "nt"},
            {"ref": "Psalm 72:1-14", "note": "The ideal king 'judges the poor... delivers the needy' — the Deut 17 vision poeticized", "type": "ot"}
        ],

        "divine_council_note": "The kingship law in Deuteronomy 17 has significant divine council "
                               "implications. In the ANE, the king was typically the earthly representative "
                               "of the patron deity — in some cases, the deity's 'image' on earth (cf. "
                               "the imago dei concept in Gen 1:26-27). Deuteronomy radically constrains "
                               "the king's pretensions: he is not God's equal but God's student. YHWH "
                               "is the true King of Israel; the human king is merely a vice-regent "
                               "under Torah. The requirement that the king must be 'from among your "
                               "brothers' (17:15) — not a foreigner — reflects the covenant principle "
                               "that Israel's governance must remain under YHWH's direct rule, not under "
                               "the authority of a foreign king who would be a devotee of one of the "
                               "allotted 'elohim. Solomon's foreign wives brought the worship of their "
                               "gods (1 Kings 11:4-8) — exactly what the kingship law was designed to "
                               "prevent.",

        "sections": [
            {
                "heading": "Capital Cases and Evidence Standards (17:1-7)",
                "body": "Blemished sacrifices are forbidden: 'You shall not sacrifice to the LORD your "
                        "God an ox or a sheep in which is a blemish, any defect whatever, for that is "
                        "an abomination to the LORD' (17:1). Then the procedure for capital apostasy: "
                        "if someone worships other gods, the sun, moon, or host of heaven (17:3 — "
                        "the very beings allotted to the nations in 4:19), they must be stoned at the "
                        "city gate. But evidence must be rigorous: 'On the evidence of two witnesses "
                        "or of three witnesses the one who is to die shall be put to death; a person "
                        "shall not be put to death on the evidence of one witness' (17:6). The witnesses "
                        "must cast the first stones (17:7), personally attesting their testimony. This "
                        "two-witness rule becomes foundational in both Jewish and Christian legal "
                        "tradition (Matt 18:16; 2 Cor 13:1)."
            },
            {
                "heading": "The Central Court (17:8-13)",
                "body": "Cases too difficult for local courts — 'between one kind of bloodshed and "
                        "another, one kind of legal right and another, or one kind of assault and "
                        "another' (17:8) — are appealed to the central sanctuary. The Levitical "
                        "priests and the sitting judge issue a binding verdict: 'You shall do "
                        "according to what they declare to you' (17:10). Refusal to accept the "
                        "ruling is capital: 'The man who acts presumptuously by not obeying the "
                        "priest... or the judge, that man shall die' (17:12). This is not judicial "
                        "tyranny but covenant order — the central court represents YHWH's authority, "
                        "and defying it is defying the suzerain himself."
            },
            {
                "heading": "The Kingship Law — Torah-Limited Monarchy (17:14-20)",
                "body": "Moses anticipates the monarchy: 'When you come to the land... and you say, "
                        "\"I will set a king over me, like all the nations that are around me\"' (17:14). "
                        "The desire to be 'like the nations' is the very impulse Deuteronomy resists — "
                        "the nations have their allotted 'elohim; Israel has YHWH. Yet God permits a "
                        "king, with restrictions: (1) God must choose him (17:15a). (2) He must be a "
                        "fellow Israelite (17:15b). (3) He must not multiply horses — i.e., build "
                        "a chariot army like Egypt (17:16). (4) He must not multiply wives — i.e., "
                        "make foreign marriage alliances (17:17a). (5) He must not multiply silver "
                        "and gold excessively (17:17b). (6) He must write a personal copy of this "
                        "Torah and read it daily (17:18-19). The purpose: 'that his heart may not be "
                        "lifted up above his brothers' (17:20). Solomon violated every single one of "
                        "these restrictions. The ideal king is not a warrior-emperor but a Torah-student "
                        "whose power is limited by covenant."
            }
        ]
    },

    {
        "id": "deut-18",
        "ref": "Deuteronomy 18",
        "chapter_num": 18,
        "title": "The Prophet Like Moses — Priestly Portions and True Prophecy",
        "era": "code",
        "type": "chapter",
        "themes": ["PRIEST", "SEED", "SPIRIT", "TYPE"],

        "synopsis": "Deuteronomy 18 addresses two critical institutions: the priesthood and the "
                    "prophetic office. The Levites' inheritance is YHWH himself (18:1-2), and they "
                    "receive specific portions from the people's sacrifices (18:3-5). Moses then "
                    "delivers one of the most comprehensive prohibitions of occult practices in the "
                    "Bible: child sacrifice, divination, fortune-telling, sorcery, charming, mediums, "
                    "necromancers, and inquiring of the dead (18:9-14). These are 'abominations' that "
                    "caused God to drive out the Canaanite nations. In their place, God promises to "
                    "raise up 'a prophet like me from among you, from your brothers' (18:15). This "
                    "is one of the most important messianic prophecies in the Torah — cited by Peter "
                    "(Acts 3:22-23) and Stephen (Acts 7:37) as fulfilled in Jesus. The prophet will "
                    "receive God's words directly and speak them to the people, continuing the "
                    "mediatorial role established at Horeb (18:16-19). The chapter closes with the "
                    "test for true vs. false prophets: if the prophet speaks in YHWH's name and the "
                    "word does not come to pass, 'that is a word that the LORD has not spoken' "
                    "(18:22). Combined with Deut 13's test (loyalty direction), this gives Israel "
                    "two criteria for prophetic discernment: theological fidelity AND predictive "
                    "fulfillment.",

        "key_verse": {
            "ref": "Deuteronomy 18:15",
            "text": "The LORD your God will raise up for you a prophet like me from among you, from your brothers — it is to him you shall listen.",
            "translation": "ESV"
        },

        "hebrew_terms": ["navi", "levi", "kohen", "nachalah", "qesem", "anan", "nachash", "kashaph", "ov", "yidoni", "doresh_el_hametim"],

        "hebrew_glossary": {
            "navi": "Prophet (one who speaks God's words — from a root meaning 'to call, to announce'; the prophet is YHWH's authorized spokesperson, replacing all unauthorized methods of accessing the spiritual realm)",
            "qesem": "Divination (accessing hidden knowledge through forbidden techniques — casting lots, reading animal entrails (extispicy), observing bird flights; these were standard ANE practices for consulting the gods)",
            "anan": "Fortune-telling / cloud-reading (a Canaanite omen-interpretation practice — attempting to read divine messages from natural phenomena outside YHWH's authorized channels)",
            "nachash": "Sorcery / omen-reading (from the same root as nachash, 'serpent' — spell-casting and incantation; the connection to the serpent of Genesis 3 is not accidental; accessing spiritual power through the nachash rather than through YHWH)",
            "kashaph": "Sorcerer / witch (one who uses potions, spells, or rituals to manipulate spiritual forces — the practice of bending the spiritual realm to human will rather than submitting to YHWH's will)",
            "ov": "Medium / spiritist (one who communicates with the dead through a 'pit spirit' — the ob is the familiar spirit that supposedly speaks from the ground; Saul's consultation of the medium at Endor (1 Sam 28) is the classic biblical violation of this prohibition)",
            "yidoni": "Necromancer / knowing one (one who claims to have a 'familiar spirit' that gives secret knowledge — the yidoni accessed the spirit realm through the dead, bypassing YHWH entirely)",
            "doresh_el_hametim": "One who inquires of the dead (the most explicit prohibition — seeking guidance or power from deceased humans; this was widespread in the ANE and is the practice Isaiah condemns: 'Should they inquire of the dead on behalf of the living?' — Isa 8:19)"
        },

        "ane_backdrop": "The occult practices listed in 18:10-11 correspond to well-documented ANE "
                        "divinatory methods. Qesem (divination) was practiced through casting lots, "
                        "reading entrails (extispicy), and observing bird flights (augury). Me'onen "
                        "(fortune-telling or cloud-reading) was associated with Canaanite omen "
                        "interpretation. Menachesh (sorcery) involved spell-casting and incantation. "
                        "Ov (medium/spiritist) and yidoni (necromancer) involved communicating with "
                        "the dead — the 'pit' spirits known in Hittite and Mesopotamian literature. "
                        "These practices were the standard means by which ANE cultures accessed the "
                        "spiritual realm. Israel's prohibition is total — not because the supernatural "
                        "realm doesn't exist, but because Israel must access it exclusively through "
                        "YHWH's appointed prophet, not through the methods of the allotted 'elohim's "
                        "religious systems.",

        "second_temple": [
            {
                "source": "4QTestimonia (4Q175)",
                "summary": "A Qumran collection of messianic proof-texts that begins with Deut "
                           "18:18-19 as the prophecy of the coming prophet.",
                "relevance": "Proves that the Qumran community read Deut 18:15-19 as a prophecy "
                             "of a specific eschatological figure — the 'Prophet' — distinct from "
                             "the Messiah and the priestly Messiah."
            },
            {
                "source": "John 1:21, 6:14, 7:40",
                "summary": "The crowd asks John the Baptist 'Are you the Prophet?' and identifies "
                           "Jesus as 'the Prophet who is to come into the world.'",
                "relevance": "Shows that the expectation of 'the Prophet like Moses' was alive in "
                             "the 1st century and was applied to both John the Baptist and Jesus."
            },
            {
                "source": "Acts 3:22-23; 7:37",
                "summary": "Peter and Stephen both quote Deut 18:15-19 and apply it to Jesus.",
                "relevance": "The definitive NT identification of Jesus as the Prophet like Moses — "
                             "the one who speaks God's words with divine authority and demands "
                             "absolute obedience."
            }
        ],

        "cross_refs": [
            {"ref": "Acts 3:22-23", "note": "Peter: 'Moses said, \"The Lord God will raise up for you a prophet like me...\"' — applied to Jesus", "type": "nt"},
            {"ref": "Acts 7:37", "note": "Stephen: 'This is the Moses who said to the Israelites, \"God will raise up for you a prophet like me\"'", "type": "nt"},
            {"ref": "John 1:21, 45; 6:14; 7:40", "note": "The 'Prophet' expectation applied to Jesus in the Fourth Gospel", "type": "nt"},
            {"ref": "1 Samuel 28:3-20", "note": "Saul consults the medium at Endor — directly violating Deut 18:10-12", "type": "ot"},
            {"ref": "Isaiah 8:19-20", "note": "'Should they inquire of the dead on behalf of the living? To the teaching and to the testimony!' — echoing Deut 18", "type": "ot"},
            {"ref": "Hebrews 1:1-2", "note": "'God spoke by the prophets... in these last days he has spoken to us by his Son' — the Prophet like Moses is THE Son", "type": "nt"},
            {"ref": "John 5:46", "note": "Jesus: 'If you believed Moses, you would believe me, for he wrote of me' — Deut 18:15 as one of those writings", "type": "nt"},
            {"ref": "Deuteronomy 4:19-20", "note": "The divine council context for 18:9-14: the occult practices are the communication methods used by the nations' allotted 'elohim; Israel must not use them because YHWH provides his prophet instead", "type": "ot"},
            {"ref": "Deuteronomy 32:17", "note": "The shedim (demons) Israel sacrificed to — the spiritual entities behind the occult practices forbidden in 18:9-14", "type": "ot"},
            {"ref": "Galatians 5:19-21", "note": "Paul lists 'sorcery' (pharmakeia) among the works of the flesh — the NT continuation of the Deut 18 prohibition", "type": "nt"},
            {"ref": "Revelation 21:8", "note": "'Sorcerers' listed among those excluded from the new Jerusalem — the Deut 18 prohibition carried into eschatological judgment", "type": "nt"}
        ],

        "divine_council_note": "Deuteronomy 18 is critical for the divine council worldview in two "
                               "ways. First, the occult prohibition (18:9-14) forbids Israel from "
                               "accessing the spiritual realm through the methods used by the nations "
                               "governed by allotted 'elohim (divine council members assigned to the "
                               "nations in 4:19 and 32:8). Divination (qesem — reading entrails, "
                               "casting lots), fortune-telling (anan — interpreting omens from clouds "
                               "or natural signs), sorcery (nachash — spell-casting, from the same root "
                               "as 'serpent'), necromancy (doresh el hametim — consulting the dead) — "
                               "ALL of these were the standard communication channels between the nations "
                               "and their patron spirits. They were the 'technology' by which the allotted "
                               "'elohim communicated with their nations. Israel must not use these channels "
                               "because YHWH has provided a completely different access point to the "
                               "spiritual realm: the prophet. The contrast is absolute: the nations access "
                               "the spiritual realm through divination, mediums, and the dead; Israel "
                               "accesses God through his living prophet. The nine forbidden practices are "
                               "not listed because they 'don't work' — they are forbidden precisely "
                               "because they DO access spiritual entities, but those entities are not YHWH. "
                               "They are the shedim (demons, 32:17) and the allotted 'elohim who govern "
                               "the nations — beings whose authority Israel must not recognize. "
                               "Second, the 'Prophet like Moses' promise (18:15-19) is deeply messianic "
                               "and has divine council implications. Moses was the mediator between YHWH "
                               "and Israel at Sinai — he stood in the divine council's presence (Exod "
                               "24:9-11) and transmitted God's words to the people. The future Prophet "
                               "will do the same, but at a cosmic level: Jesus, the Prophet like Moses, "
                               "stands in the divine council (the heavenly throne room of Revelation 4-5) "
                               "and declares God's ultimate word to all nations — not just Israel. The "
                               "'Prophet like Moses' will undo the allotment of Deuteronomy 32 by bringing "
                               "all nations under YHWH's direct authority through the gospel.",

        "sections": [
            {
                "heading": "The Levites' Inheritance Is YHWH (18:1-8)",
                "body": "The Levites and the whole tribe of Levi 'shall have no portion or inheritance "
                        "with Israel. They shall eat the LORD's food offerings as their inheritance' "
                        "(18:1). Their provision comes from the sacrificial system: the shoulder, the "
                        "two cheeks, and the stomach of sacrificed animals (18:3), plus the firstfruits "
                        "of grain, wine, oil, and wool (18:4). The reason: 'The LORD is their "
                        "inheritance, as he promised them' (18:2). The Levites embody the principle "
                        "that Israel as a whole should exhibit: dependence on YHWH rather than on "
                        "territorial possession. A Levite who migrates to the central sanctuary from "
                        "any town may serve there and receive equal portions (18:6-8). This provision "
                        "ensures that all Levites, not just those born near the central sanctuary, "
                        "have access to their priestly vocation."
            },
            {
                "heading": "The Abominable Practices — Comprehensive Occult Prohibition (18:9-14)",
                "body": "Moses delivers the most comprehensive prohibition of occult practices in the "
                        "Torah: 'When you come into the land... you shall not learn to follow the "
                        "abominable practices of those nations. There shall not be found among you "
                        "anyone who burns his son or his daughter as an offering, anyone who practices "
                        "divination (qosem qesamim) or tells fortunes (me'onen) or interprets omens "
                        "(menachesh) or a sorcerer (mekhashsheph), or a charmer (chover chaver) or a "
                        "medium (sho'el ov) or a necromancer (yidoni) or one who inquires of the dead "
                        "(doresh el hametim)' (18:9-11). Nine categories are listed — likely intended "
                        "as comprehensive. 'For whoever does these things is an abomination to the "
                        "LORD. And because of these abominations the LORD your God is driving them out "
                        "before you' (18:12). The Canaanites' use of these practices is part of the "
                        "reason for their dispossession. The contrast: 'You shall be blameless (tamim) "
                        "before the LORD your God' (18:13). Tamim means complete, whole, having "
                        "integrity — wholly committed to YHWH without spiritual adultery through "
                        "occult practices."
            },
            {
                "heading": "The Prophet Like Moses (18:15-19)",
                "body": "In place of divination and necromancy, YHWH promises a prophetic mediator: "
                        "'The LORD your God will raise up for you a prophet like me from among you, "
                        "from your brothers — it is to him you shall listen' (18:15). The promise is "
                        "both collective (the prophetic office) and singular (a specific future "
                        "Prophet). The people asked for this at Horeb: 'Let me not hear again the "
                        "voice of the LORD my God or see this great fire any more, lest I die' (18:16). "
                        "God's response: 'They are right in what they have spoken. I will raise up for "
                        "them a prophet like you from among their brothers. And I will put my words in "
                        "his mouth, and he shall speak to them all that I command him' (18:17-18). "
                        "'I will put my words in his mouth' is the definition of true prophecy — divine "
                        "words transmitted through human speech. The consequence of ignoring this "
                        "Prophet: 'Whoever will not listen to my words that he shall speak in my name, "
                        "I myself will require it of him' (18:19). Peter in Acts 3:22-23 adds: 'And it "
                        "shall be that every soul who does not listen to that prophet shall be destroyed "
                        "from the people.' The stakes are absolute. The Qumran community expected this "
                        "Prophet as a distinct eschatological figure (4QTestimonia). Jesus claimed the "
                        "role: 'If you believed Moses, you would believe me, for he wrote of me' "
                        "(John 5:46)."
            },
            {
                "heading": "True and False Prophecy — The Fulfillment Test (18:20-22)",
                "body": "Two categories of false prophets are identified: (1) a prophet who speaks "
                        "'in the name of other gods' — this is the Deut 13 scenario, treason against "
                        "YHWH (18:20a); (2) a prophet who presumes to speak 'a word in my name that "
                        "I have not commanded him to speak' — unauthorized use of YHWH's name (18:20b). "
                        "Both must die. The discernment criterion: 'when a prophet speaks in the name "
                        "of the LORD, if the word does not come to pass or come true, that is a word "
                        "that the LORD has not spoken; the prophet has spoken it presumptuously. You "
                        "need not be afraid of him' (18:22). Combined with chapter 13's loyalty test, "
                        "Israel now has two criteria for prophetic evaluation: (a) Does the prophet "
                        "direct worship to YHWH? (Deut 13) (b) Does the prophet's word come true? "
                        "(Deut 18). Both must be satisfied. A prophet who works miracles but leads to "
                        "other 'elohim is false (ch. 13). A prophet who claims YHWH's authority but "
                        "whose predictions fail is false (ch. 18). Only the prophet who passes both "
                        "tests speaks for YHWH."
            }
        ]
    }
]
