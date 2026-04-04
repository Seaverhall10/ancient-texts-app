"""
era_isaiah_woe.py -- Woe Oracles, the Cornerstone, and Hezekiah's Crisis (Isaiah 28-39)

The third major section of Isaiah contains a series of hoi (woe) oracles against
Ephraim and Judah (28-33), followed by eschatological judgment and restoration
(34-35), and concluding with the historical narrative of Hezekiah's confrontation
with Sennacherib of Assyria (36-39). Key theological moments include the precious
cornerstone laid in Zion (28:16), the sealed scroll and the reversal of blindness
(29), the warning against trusting Egypt instead of YHWH (30-31), and the dramatic
deliverance of Jerusalem by the angel of YHWH who strikes down 185,000 Assyrians
in a single night (37:36). This section serves as the bridge between First Isaiah
(1-39) and Second Isaiah (40-55), with the Babylonian exile foreshadowed in
Hezekiah's encounter with the envoys of Merodach-baladan (39).
"""

CHAPTERS = [
    {
        "id": "isa-28",
        "ref": "Isaiah 28",
        "chapter_num": 28,
        "title": "The Cornerstone in Zion and the Covenant with Death",
        "era": "isaiah_woe",
        "type": "chapter",
        "themes": ["SEED", "COV", "DC"],

        "synopsis": "The first woe oracle targets Ephraim (northern Israel), whose leaders are 'drunkards' "
                    "with 'fading flowers' (28:1). Judgment comes as a 'tempest of hail, a destroying storm, "
                    "like a tempest of mighty, overflowing waters' (28:2) -- the Assyrian invasion described "
                    "in chaos-water language. The oracle then pivots to Jerusalem, where priests and prophets "
                    "'reel with strong drink... they err in vision (re'ut) and stumble in judgment (peliliyyah)' "
                    "(28:7). The religious leadership is blind and drunk -- the very organs of divine "
                    "communication are compromised. Judah's leaders have made a 'covenant with death' (berit "
                    "et-mavet) and an 'agreement with Sheol' (chozeh et-she'ol) (28:15), believing their "
                    "political alliances will protect them from the 'overwhelming scourge.' YHWH responds "
                    "with the cornerstone oracle: 'Behold, I am the one who has laid as a foundation in "
                    "Zion, a stone (even), a tested stone (even bochan), a precious cornerstone (pinnat "
                    "yiqrat) of a sure foundation (musad mussad): whoever believes (ha-ma'amin) will not be "
                    "in haste (lo yachish)' (28:16). Justice (mishpat) will be the measuring line and "
                    "righteousness (tsedaqah) the plumb line. Hail will sweep away the refuge of lies, and "
                    "the covenant with death will be annulled (28:17-18). YHWH's 'strange work' (ma'aseh "
                    "zar) and 'alien deed' (avodah nokhriyyah) -- bringing judgment on his own people -- "
                    "will be accomplished (28:21).",

        "key_verse": {
            "ref": "Isaiah 28:16",
            "text": "Therefore thus says the Lord GOD, 'Behold, I am the one who has laid as a foundation in Zion, a stone, a tested stone, a precious cornerstone, of a sure foundation: Whoever believes will not be in haste.'",
            "translation": "ESV"
        },

        "original_terms": [
            "even bochan (tested stone -- a foundation stone that has been proven reliable)",
            "pinnat yiqrat (precious cornerstone -- the stone that anchors and aligns the entire building)",
            "musad mussad (sure/established foundation -- doubled for emphasis, absolutely certain)",
            "ha-ma'amin (the one who believes/trusts -- from the root aman, same as 'amen')",
            "berit et-mavet (covenant with death -- a deal with the powers of destruction)",
            "hoi (woe -- the prophetic interjection introducing judgment oracles)",
            "ma'aseh zar (strange work -- YHWH's judgment on his own people, contrary to his nature)"
        ],

        "ane_backdrop": "Cornerstones in ANE construction were ritually significant. Mesopotamian "
                        "foundation deposits included inscribed stones placed at the corners of temples "
                        "and palaces, often with prayers to the gods for the building's stability. The "
                        "cornerstone determined the alignment of the entire structure -- a misplaced "
                        "cornerstone produced a crooked building. The Egyptian concept of ma'at "
                        "(justice/cosmic order) as the foundation of civilization parallels the Isaianic "
                        "image of mishpat and tsedaqah as the measuring line and plumb line of YHWH's "
                        "new construction in Zion.",

        "second_temple": [
            {
                "source": "1QS (Rule of the Community) VIII.7-8",
                "summary": "The Qumran community identified itself as the 'precious cornerstone' of "
                           "Isaiah 28:16, describing their council as a 'tested wall, a precious "
                           "cornerstone, whose foundations will not be shaken.'",
                "relevance": "The Dead Sea Scrolls community corporately identified with the cornerstone -- "
                             "they believed they were the new foundation YHWH was laying in Zion."
            },
            {
                "source": "1 Peter 2:4-8",
                "summary": "Peter quotes Isaiah 28:16 (with Psalm 118:22 and Isaiah 8:14) to identify "
                           "Jesus as the living cornerstone: 'Whoever believes in him will not be put "
                           "to shame.'",
                "relevance": "The New Testament applies the cornerstone directly to Christ -- he is the "
                             "tested, precious foundation stone on which the new temple (the church) is built."
            },
            {
                "source": "Romans 9:33; 10:11",
                "summary": "Paul combines Isaiah 28:16 and 8:14: 'Behold, I am laying in Zion a stone "
                           "of stumbling... but whoever believes in him will not be put to shame.'",
                "relevance": "Paul reads the cornerstone christologically -- Christ is both the foundation "
                             "for those who believe and the stumbling stone for those who refuse."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 118:22", "note": "'The stone the builders rejected has become the cornerstone' -- the same cornerstone tradition", "type": "ot"},
            {"ref": "Daniel 2:34-35, 44-45", "note": "The stone 'cut without hands' that smashes the image and fills the earth -- the divine cornerstone as cosmic kingdom", "type": "ot"},
            {"ref": "Matthew 21:42-44", "note": "Jesus quotes Psalm 118:22 and alludes to Daniel 2 -- he is the rejected cornerstone and the crushing stone", "type": "nt"},
            {"ref": "1 Peter 2:4-8", "note": "Christ as the living cornerstone of Isaiah 28:16 -- believers as living stones built upon him", "type": "nt"},
            {"ref": "Ephesians 2:20", "note": "Christ Jesus as the cornerstone of the apostolic foundation", "type": "nt"},
            {"ref": "Romans 9:33", "note": "Paul's Christological reading of the Zion cornerstone", "type": "nt"}
        ],

        "divine_council_note": "The cornerstone oracle of 28:16 is a divine council decree -- YHWH himself "
                               "('I am the one who has laid') places the foundation stone. The covenant with "
                               "death (28:15) that Judah's leaders have made represents an attempt to align "
                               "themselves with the powers of the underworld -- Death (Mavet) and Sheol are "
                               "personified as treaty partners, recalling the Canaanite god Mot (Death) who "
                               "opposes Baal in the Ugaritic texts. YHWH's counter-action is to lay a "
                               "different foundation: not an alliance with death but a stone of faith. The "
                               "measuring line of mishpat and the plumb line of tsedaqah (28:17) are the "
                               "divine council's standards -- the same justice demanded in Psalm 82:3-4, "
                               "where the elohim are commanded to 'give justice to the weak' and 'rescue "
                               "the needy.' The 'strange work' (ma'aseh zar) of 28:21 acknowledges that "
                               "judgment on his own people is not YHWH's preferred action -- it is 'alien' "
                               "to his nature, but the council has decreed it because the covenant has been "
                               "violated.",

        "sections": [
            {
                "heading": "Woe to Ephraim's Drunkards and Judah's Blind Leaders (28:1-13)",
                "body": "'Woe (hoi) to the proud crown (ateret ge'ut) of the drunkards of Ephraim' (28:1). "
                        "The oracle begins with Samaria, the capital of northern Israel, described as a "
                        "'fading flower' (tsits novel) crowning a 'rich valley' -- beautiful but decaying. "
                        "YHWH's judgment comes as a 'mighty and strong one' (chazaq ve'ammits) -- the "
                        "Assyrian invasion -- 'like a tempest of hail (zeram barad), a destroying storm, "
                        "like a tempest of mighty, overflowing waters' (28:2). The chaos-water language "
                        "describes Assyria as an instrument of divine de-creation. The oracle then shifts "
                        "to Jerusalem (28:7-13), where the religious elite are equally compromised: "
                        "'These also reel with wine and stagger with strong drink; the priest and the "
                        "prophet reel with strong drink, they are swallowed by wine' (28:7). The verb "
                        "'swallowed' (navu'u) creates a grim wordplay: the navi (prophet) is navu'u "
                        "(swallowed/confused). Their tables are covered with 'filthy vomit, without a "
                        "clean place' (28:8) -- the graphic imagery is deliberate: the prophetic and "
                        "priestly offices are defiled beyond recognition."
            },
            {
                "heading": "The Precious Cornerstone vs. the Covenant with Death (28:14-22)",
                "body": "Judah's leaders have made a 'covenant with death (berit et-mavet)' (28:15) -- "
                        "likely a reference to political alliances with Egypt or Assyria, described as "
                        "deals with the personified powers of destruction. They believe 'the overwhelming "
                        "scourge (shot shotef) will not reach us, for we have made lies (kazav) our "
                        "refuge and falsehood (sheqer) our hiding place' (28:15). Against this fortress "
                        "of lies, YHWH lays a true foundation: 'Behold, I am the one who has laid "
                        "(yissad) as a foundation in Zion, a stone (even), a tested stone (even bochan), "
                        "a precious cornerstone (pinnat yiqrat) of a sure foundation: whoever believes "
                        "(ha-ma'amin) will not be in haste (yachish)' (28:16). The stone is tested "
                        "(bochan) -- it has been proven reliable under pressure. It is precious (yiqrat) "
                        "-- of supreme value. It is a cornerstone (pinnah) -- the stone that determines "
                        "the alignment of every other stone. 'Whoever believes' -- the response required "
                        "is trust (aman), the same root as 'amen' and the same faith demanded of Ahaz "
                        "in 7:9. 'Will not be in haste (yachish)' -- the believer will not panic or "
                        "flee. Then judgment: 'I will make justice (mishpat) the measuring line and "
                        "righteousness (tsedaqah) the plumb line; and hail will sweep away the refuge "
                        "of lies' (28:17). The covenant with death 'will be annulled (kuppar)' (28:18) "
                        "-- using the same verb kaphar (atone/cover/annul) from the sacrificial system."
            }
        ]
    },

    {
        "id": "isa-36-37",
        "ref": "Isaiah 36-37",
        "chapter_num": 36,
        "title": "Sennacherib's Siege and the Angel's Deliverance",
        "era": "isaiah_woe",
        "type": "chapter",
        "themes": ["DC", "KING", "GLORY"],

        "synopsis": "In the fourteenth year of King Hezekiah (~701 BC), Sennacherib king of Assyria "
                    "invades Judah and captures its fortified cities. He sends the Rabshakeh (chief "
                    "cupbearer, a high-ranking Assyrian official) to Jerusalem with a massive army. "
                    "The Rabshakeh stands at the very location where Isaiah had confronted Ahaz decades "
                    "earlier -- the conduit of the upper pool (36:2; cf. 7:3) -- and delivers a "
                    "theological ultimatum. His speech is a masterpiece of psychological and theological "
                    "warfare: 'On whom do you now trust?' (36:5). He mocks trust in Egypt ('that "
                    "broken reed,' 36:6), trust in YHWH ('Has not Hezekiah removed his high places and "
                    "altars?' 36:7 -- misrepresenting Hezekiah's reform as an insult to YHWH), and "
                    "Judah's military capacity (36:8-9). His ultimate blasphemy: 'Has any of the gods "
                    "of the nations ever delivered his land out of the hand of the king of Assyria?' "
                    "(36:18). He equates YHWH with the gods of defeated nations -- Hamath, Arpad, "
                    "Sepharvaim, Samaria (36:19-20). Hezekiah tears his clothes, enters the temple, "
                    "and sends word to Isaiah. Isaiah responds: 'Do not be afraid... Thus says YHWH "
                    "concerning the king of Assyria: He shall not come into this city' (37:6, 33). "
                    "Hezekiah prays directly to YHWH, addressing him as 'YHWH tseva'ot, God of Israel, "
                    "who is enthroned above the cherubim' (37:16) -- a divine council title emphasizing "
                    "YHWH's throne. The climax: 'And the angel of YHWH (malakh YHWH) went out and "
                    "struck down 185,000 in the camp of the Assyrians' (37:36). The divine warrior "
                    "deploys a single agent and annihilates an empire's army overnight.",

        "key_verse": {
            "ref": "Isaiah 37:36",
            "text": "And the angel of the LORD went out and struck down 185,000 in the camp of the Assyrians. And when people arose early in the morning, behold, these were all dead bodies.",
            "translation": "ESV"
        },

        "original_terms": [
            "Rabshakeh (chief cupbearer -- the title of the Assyrian official, not a personal name)",
            "malakh YHWH (angel/messenger of YHWH -- the divine agent who strikes the Assyrian camp)",
            "yoshev hakeruvim (enthroned above the cherubim -- YHWH's throne room title)",
            "YHWH tseva'ot (YHWH of hosts -- the divine warrior commanding heaven's armies)",
            "qana (zeal/jealousy -- YHWH's passionate defense of his name and city)",
            "she'erit (remnant -- the survivors who will take root and bear fruit)"
        ],

        "ane_backdrop": "Sennacherib's own account of the 701 BC campaign survives on the Taylor Prism "
                        "and the Annals inscriptions. He claims to have captured 46 of Judah's fortified "
                        "cities and besieged Hezekiah 'like a bird in a cage' in Jerusalem. Notably, "
                        "Sennacherib never claims to have captured Jerusalem -- a significant omission in "
                        "Assyrian royal inscriptions, which typically exaggerate victories. The Rabshakeh's "
                        "speech follows known Assyrian psychological warfare tactics: challenge the enemy's "
                        "trust in allies, mock their gods, and offer terms of surrender. The Lachish "
                        "reliefs from Sennacherib's palace at Nineveh graphically depict the siege and "
                        "fall of Lachish -- Judah's second city -- confirming the historical devastation "
                        "of the campaign even while Jerusalem survived.",

        "second_temple": [
            {
                "source": "Sirach (Ecclesiasticus) 48:18-21",
                "summary": "Ben Sira celebrates Hezekiah's faith: 'Sennacherib sent the Rabshakeh... "
                           "he stretched out his hand against Zion... Then their hearts and hands "
                           "trembled... And they called upon the Lord who is merciful... and an angel "
                           "struck the camp of the Assyrians and wiped them out.'",
                "relevance": "Sirach preserves the tradition of the angelic deliverance as one of "
                             "Israel's greatest moments of divine intervention."
            },
            {
                "source": "2 Kings 18:13-19:37",
                "summary": "The parallel account in Kings provides additional details, including "
                           "Hezekiah's payment of tribute (not mentioned in Isaiah's version) and "
                           "the full text of both the Rabshakeh's speech and Hezekiah's prayer.",
                "relevance": "The Kings account confirms the historicity of the event and provides "
                             "the broader narrative context of Hezekiah's reign."
            },
            {
                "source": "Josephus, Antiquities X.1.1-5",
                "summary": "Josephus recounts the Sennacherib crisis in detail and adds the note "
                           "that 'a pestilential disease' arose in the Assyrian camp, citing "
                           "Herodotus' account of mice gnawing Sennacherib's bowstrings.",
                "relevance": "Josephus attempts to harmonize the biblical account of the angel's "
                             "strike with naturalistic explanations circulating in his era."
            }
        ],

        "cross_refs": [
            {"ref": "2 Kings 18:13-19:37", "note": "The parallel account of Sennacherib's invasion, nearly identical to Isaiah 36-37", "type": "ot"},
            {"ref": "2 Chronicles 32:1-23", "note": "The Chronicler's account emphasizing Hezekiah's faith and the divine intervention", "type": "ot"},
            {"ref": "Isaiah 7:3", "note": "Isaiah met Ahaz at the same conduit of the upper pool -- the Rabshakeh now stands where the Immanuel sign was given", "type": "ot"},
            {"ref": "Isaiah 10:5-19", "note": "Assyria as the rod of YHWH's anger -- the tool that exceeded its commission and is now judged", "type": "ot"},
            {"ref": "Exodus 12:23, 29", "note": "The destroyer (mashchit) striking Egypt's firstborn -- the angel of YHWH at the Assyrian camp echoes the Passover plague", "type": "ot"},
            {"ref": "2 Samuel 24:16", "note": "The destroying angel stretching his hand over Jerusalem -- stayed by YHWH's mercy", "type": "ot"},
            {"ref": "Psalm 46:4-7", "note": "'God is in the midst of her; she shall not be moved. God will help her when morning dawns' -- the Zion theology fulfilled in 701 BC", "type": "ot"}
        ],

        "divine_council_note": "The Sennacherib crisis is a divine council confrontation. The Rabshakeh's "
                               "speech frames the conflict as a contest between YHWH and the gods of the "
                               "nations: 'Has any of the gods of the nations delivered his land out of my "
                               "hand? Who among all the gods of these lands have delivered their lands out of "
                               "my hand, that YHWH should deliver Jerusalem out of my hand?' (36:18, 20). "
                               "The Rabshakeh places YHWH in the same category as Hamath's god, Arpad's god, "
                               "Samaria's god -- all defeated. Hezekiah's prayer directly counters this by "
                               "invoking YHWH's divine council title: 'O YHWH tseva'ot, God of Israel, who "
                               "is enthroned above the cherubim (yoshev hakeruvim), you are the God, you "
                               "alone (levaddekha), of all the kingdoms of the earth; you have made heaven "
                               "and earth' (37:16). The prayer distinguishes YHWH from the defeated gods: "
                               "'they were not gods (elohim), but the work of men's hands, wood and stone' "
                               "(37:19). The nations' gods are not real elohim at all. YHWH's response "
                               "through Isaiah confirms his divine council supremacy: 'Whom have you mocked "
                               "and reviled? Against whom have you raised your voice and lifted your eyes to "
                               "the height? Against the Holy One of Israel!' (37:23). The deployment of the "
                               "malakh YHWH (angel of YHWH) to destroy 185,000 soldiers in a single night "
                               "is the divine council's military response: one heavenly agent is sufficient "
                               "to annihilate the greatest army on earth.",

        "sections": [
            {
                "heading": "The Rabshakeh's Theological Warfare (36:1-22)",
                "body": "The Rabshakeh stands at the conduit of the upper pool on the highway to the "
                        "Washer's Field (36:2) -- the exact spot where Isaiah confronted Ahaz with the "
                        "Immanuel sign decades earlier (7:3). The geographical echo is deliberate: where "
                        "Ahaz refused to trust YHWH and turned to Assyria, now Assyria stands at the same "
                        "spot demanding submission. The Rabshakeh's speech systematically dismantles every "
                        "source of Judah's confidence. Trust in Egypt? 'That broken reed of a staff, which "
                        "will pierce the hand of any man who leans on it' (36:6). Trust in YHWH? 'Has not "
                        "Hezekiah himself removed his high places and altars?' (36:7) -- a distortion of "
                        "Hezekiah's reform, spinning the removal of idolatrous sites as an insult to YHWH. "
                        "Military strength? 'Come, make a wager with my master: I will give you two "
                        "thousand horses, if you are able to set riders on them' (36:8) -- Judah cannot "
                        "even field cavalry. The Rabshakeh then claims divine authorization: 'Have I come "
                        "up against this land to destroy it without YHWH? YHWH said to me, Go up against "
                        "this land and destroy it' (36:10). This is psychologically devastating: the "
                        "Assyrian claims YHWH is on his side. Hezekiah's officials beg the Rabshakeh to "
                        "speak in Aramaic rather than Hebrew so the people on the walls cannot understand "
                        "(36:11), but the Rabshakeh deliberately shouts in Hebrew to the common soldiers, "
                        "promising deportation to 'a land like your own land' (36:17)."
            },
            {
                "heading": "Hezekiah's Prayer and Isaiah's Oracle (37:1-35)",
                "body": "Hezekiah responds with the actions of a faithful king: he tears his clothes, "
                        "covers himself with sackcloth, enters the house of YHWH, and sends to Isaiah "
                        "(37:1-2). Isaiah's initial response: 'Do not be afraid... YHWH will put a "
                        "spirit (ruach) in him, so that he shall hear a rumor and return to his own "
                        "land, and I will cause him to fall by the sword in his own land' (37:6-7). When "
                        "Sennacherib sends a second threatening letter, Hezekiah takes it into the temple "
                        "and 'spread it before YHWH' (37:14) -- physically placing the threat before "
                        "YHWH's throne. His prayer is theologically precise: 'O YHWH tseva'ot, God of "
                        "Israel, yoshev hakeruvim (enthroned above the cherubim), you are the God, you "
                        "alone, of all the kingdoms of the earth' (37:16). He acknowledges that the "
                        "Assyrians have indeed destroyed other nations and their gods -- 'for they were "
                        "not elohim but the work of men's hands' (37:19). The prayer stakes everything "
                        "on YHWH's uniqueness: if YHWH is truly God, he will act. Isaiah delivers YHWH's "
                        "oracle against Sennacherib: 'The virgin daughter of Zion despises you, she "
                        "scorns you' (37:22). YHWH recounts his sovereign control over Sennacherib's "
                        "movements: 'Because you have raged against me... I will put my hook in your "
                        "nose and my bit in your lips, and I will turn you back on the way by which "
                        "you came' (37:29). The promise to Hezekiah: a sign of agricultural recovery, "
                        "and the assurance that 'the zeal (qin'at) of YHWH tseva'ot will do this' "
                        "(37:32) -- the same guarantee as the messianic oracle of 9:7."
            },
            {
                "heading": "The Angel Strikes: 185,000 Dead in a Single Night (37:36-38)",
                "body": "'And the malakh YHWH (angel/messenger of YHWH) went out and struck down (vayakkeh) "
                        "185,000 in the camp of the Assyrians. And when people arose early in the morning, "
                        "behold, these were all dead bodies (pegharim metim)' (37:36). The terse narration "
                        "is staggering in its understatement: one agent, one night, 185,000 dead. The "
                        "malakh YHWH is the divine council's executive agent -- the same figure who "
                        "struck Egypt's firstborn on Passover night (Exod 12:23, 29), who stood with "
                        "drawn sword before Balaam (Num 22:23), and who appeared as the Commander of "
                        "YHWH's army before Joshua (Josh 5:13-15). The destruction recalls the tenth "
                        "plague of the exodus: as the destroyer struck the firstborn of Egypt overnight, "
                        "so the angel of YHWH strikes the Assyrian army overnight. Sennacherib 'departed "
                        "and went home and lived at Nineveh' (37:37). The chapter closes with the "
                        "assassination of Sennacherib by his own sons while worshiping in the house of "
                        "Nisroch his god (37:38) -- the god who could not protect the king from judgment "
                        "in his own temple. YHWH's word through Isaiah is fulfilled completely: "
                        "Sennacherib returns home and falls by the sword in his own land."
            }
        ]
    },

    {
        "id": "isa-29",
        "ref": "Isaiah 29",
        "chapter_num": 29,
        "title": "The Sealed Book, Spiritual Blindness, and Future Reversal",
        "era": "isaiah_woe",
        "type": "chapter",
        "themes": ["SPIRIT", "REVERSAL"],

        "synopsis": "Isaiah pronounces woe upon 'Ariel' (ari'el) -- Jerusalem, the 'lion of God' or "
                    "'altar hearth of God.' YHWH will besiege his own city: 'I will distress Ariel, "
                    "and there shall be moaning and lamentation, and she shall be to me like an altar "
                    "hearth (ari'el)' (29:2). Yet the besieging nations will vanish 'like a dream, a "
                    "vision of the night' (29:7). Isaiah then describes the spiritual blindness of his "
                    "generation: 'For YHWH has poured out upon you a spirit of deep sleep (ruach "
                    "tardemah), and has closed your eyes (the prophets), and covered your heads (the "
                    "seers)' (29:10). The entire prophetic vision has become like a sealed scroll (sepher "
                    "ha-chatum): the literate say 'I cannot read it, for it is sealed,' and the "
                    "illiterate say 'I cannot read' (29:11-12). Worship has become mere formalism: "
                    "'This people draw near with their mouth and honor me with their lips, while their "
                    "hearts are far from me, and their fear of me is a commandment taught by men (mitsvat "
                    "anashim melummadah)' (29:13). Yet reversal is promised: 'In that day the deaf shall "
                    "hear the words of a book, and out of their gloom and darkness the eyes of the "
                    "blind shall see' (29:18). The meek (anavim) will obtain fresh joy in YHWH.",

        "key_verse": {
            "ref": "Isaiah 29:13",
            "text": "And the Lord said: 'Because this people draw near with their mouth and honor me with their lips, while their hearts are far from me, and their fear of me is a commandment taught by men.'",
            "translation": "ESV"
        },

        "original_terms": [
            "Ariel (lion of God / altar hearth -- a double-meaning name for Jerusalem)",
            "ruach tardemah (spirit of deep sleep -- the same supernatural sleep as Adam's in Gen 2:21)",
            "sepher ha-chatum (sealed scroll -- the prophetic word inaccessible due to spiritual blindness)",
            "mitsvat anashim melummadah (commandment of men, learned by rote -- religion as human tradition)",
            "anavim (meek/humble/afflicted -- the poor who will receive joy in the reversal)"
        ],

        "ane_backdrop": "The sealed scroll motif has parallels in Mesopotamian practice where important "
                        "documents were enclosed in clay envelopes and sealed, accessible only to "
                        "authorized readers. The concept of divine-imposed blindness appears in "
                        "Mesopotamian omen literature, where the gods could 'close the eyes' of a "
                        "diviner, preventing him from reading the omens correctly. The 'Ariel' title "
                        "for Jerusalem may connect to the Moabite Stone (Mesha Stele, line 12), which "
                        "mentions the 'ariel of David' -- possibly an altar or sacred object taken "
                        "from Israelite territory.",

        "second_temple": [
            {
                "source": "Matthew 15:7-9; Mark 7:6-7",
                "summary": "Jesus quotes Isaiah 29:13 against the Pharisees: 'This people honors me "
                           "with their lips, but their heart is far from me; in vain do they worship "
                           "me, teaching as doctrines the commandments of men.'",
                "relevance": "Jesus applies the Isaiah critique of formalistic religion directly to "
                             "the religious leadership of his own day."
            },
            {
                "source": "Romans 11:8",
                "summary": "Paul quotes Isaiah 29:10: 'God gave them a spirit of stupor, eyes that "
                           "would not see and ears that would not hear, down to this very day.'",
                "relevance": "Paul applies the judicial blindness of Isaiah 29 to Israel's rejection "
                             "of the Messiah -- the same spiritual torpor continues."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 6:9-10", "note": "The judicial hardening commission -- the blindness described in 29:9-12 is the fulfillment of 6:9-10", "type": "ot"},
            {"ref": "Matthew 15:7-9", "note": "Jesus quoting 29:13 against lip-service religion", "type": "nt"},
            {"ref": "Romans 11:8", "note": "Paul quoting 29:10 regarding Israel's spiritual sleep", "type": "nt"},
            {"ref": "Daniel 12:4, 9", "note": "'Seal the book until the time of the end' -- Daniel's sealed scroll echoes Isaiah's sealed scroll", "type": "ot"},
            {"ref": "Revelation 5:1-5", "note": "The scroll sealed with seven seals that only the Lamb can open -- the ultimate unsealing", "type": "nt"},
            {"ref": "Isaiah 35:5-6", "note": "The blind see and the deaf hear -- the reversal promised in 29:18 elaborated in 35", "type": "ot"}
        ],

        "divine_council_note": "The 'spirit of deep sleep' (ruach tardemah) of 29:10 is a divine council "
                               "action. YHWH himself closes the eyes of the prophets and seers -- the very "
                               "people who are supposed to have access to the council's deliberations (cf. "
                               "Jer 23:18, 22). When the prophetic office is blinded by divine decree, "
                               "the entire nation loses access to heavenly counsel. The sealed scroll "
                               "(29:11) represents the divine word made inaccessible -- not because the "
                               "words are absent but because the capacity to understand has been judicially "
                               "removed. This is the fulfillment of the commission in 6:9-10: 'hearing but "
                               "not understanding.' Yet the divine council also decrees reversal: 'the "
                               "deaf shall hear the words of a book, and... the eyes of the blind shall "
                               "see' (29:18). The same council that imposed the blindness will remove it.",

        "sections": [
            {
                "heading": "Woe to Ariel: Jerusalem Besieged and Delivered (29:1-8)",
                "body": "'Woe to Ariel, Ariel, the city where David encamped!' (29:1). The name Ariel "
                        "carries two meanings: ari-El ('lion of God') and ari'el ('altar hearth') -- "
                        "Jerusalem is both the fierce guardian of YHWH's presence and the place of "
                        "sacrifice. YHWH will besiege his own city: 'I will encamp against you all "
                        "around' (29:3). Yet the besieging nations will be scattered: 'The multitude of "
                        "all the nations that fight against Ariel... shall be like a dream, a vision of "
                        "the night' (29:7). They will vanish like the hunger that remains after a "
                        "dreaming man awakens (29:8) -- the siege will dissolve as if it never happened."
            },
            {
                "heading": "The Sealed Scroll and Lip-Service Religion (29:9-14)",
                "body": "'Astonish yourselves and be astonished; blind yourselves and be blind! Be drunk, "
                        "but not with wine; stagger, but not with strong drink!' (29:9). The blindness "
                        "is spiritual, not physical. 'YHWH has poured out upon you a ruach tardemah "
                        "(spirit of deep sleep)' (29:10) -- the tardemah is the same supernatural sleep "
                        "that fell on Adam (Gen 2:21) and Abraham (Gen 15:12). It is a divinely imposed "
                        "state of unconsciousness. The vision has become 'like the words of a sealed "
                        "scroll (sepher he-chatum)' (29:11). Both the educated and uneducated are unable "
                        "to read it -- the impediment is not literacy but spiritual capacity. Then the "
                        "devastating diagnosis: 'this people draw near with their mouth and honor me "
                        "with their lips, while their hearts are far from me, and their fear (yir'ah) of "
                        "me is a commandment taught by men (mitsvat anashim melummadah)' (29:13). Religion "
                        "has become human tradition, not divine encounter. YHWH's response: 'I will again "
                        "do wonderful things (lehaphli) with this people, with wonder upon wonder; and the "
                        "wisdom of their wise shall perish' (29:14)."
            },
            {
                "heading": "Reversal: The Deaf Hear, the Blind See (29:17-24)",
                "body": "The judgment is not final: 'Is it not yet a very little while until Lebanon shall "
                        "be turned into a fruitful field, and the fruitful field shall be regarded as a "
                        "forest?' (29:17). The reversal encompasses nature and humanity: 'In that day the "
                        "deaf shall hear the words of a scroll (sepher), and out of their gloom (ophel) "
                        "and darkness (choshek) the eyes of the blind shall see' (29:18). The sealed "
                        "scroll of 29:11 will be unsealed. The meek (anavim) will rejoice in YHWH, the "
                        "poor (evyonim) will exult in the Holy One of Israel (29:19). Those who err in "
                        "spirit (to'ei ruach) will come to understanding (binah), and those who murmur "
                        "will accept instruction (leqach) (29:24). The God who sealed the book will "
                        "unseal it; the God who blinded the eyes will open them."
            }
        ]
    },

    {
        "id": "isa-34",
        "ref": "Isaiah 34",
        "chapter_num": 34,
        "title": "The Host of Heaven Dissolved: Cosmic Judgment on the Nations and Their Gods",
        "era": "isaiah_woe",
        "type": "chapter",
        "themes": ["DC", "NATIONS", "BLOOD"],

        "synopsis": "Isaiah 34 is one of the most terrifying cosmic judgment passages in all of Scripture. It "
                    "opens with a summons to the entire creation: 'Draw near, O nations (goyim), to hear, and "
                    "give attention, O peoples (le'ummim)! Let the earth hear (tishma ha'arets), and all that "
                    "fills it (melo'ah); the world (tevel), and all that comes from it' (34:1). The summons is "
                    "universal -- every nation, every creature, the entire cosmos is called to witness what "
                    "follows. YHWH's fury falls on all nations: 'For YHWH is enraged (qetseph) against all "
                    "the nations (kol-haggoyim), and furious (chemah) against all their host (kol-tseva'am); "
                    "he has devoted them to destruction (hecherimam), has given them over to slaughter (letevach)' "
                    "(34:2). The verb herim ('to devote to destruction') is the cherem vocabulary of holy war -- "
                    "the total consecration of the enemy to YHWH. Then the cosmic unmaking: 'All the host "
                    "of heaven (kol-tseva hashamayim) shall rot away (yimmaqu), and the skies (shamayim) "
                    "roll up like a scroll (venigollu kasseper); all their host (kol-tseva'am) shall fall "
                    "(yibbol), as leaves fall (kinevol aleh) from the vine, like leaves falling from the "
                    "fig tree' (34:4). The 'host of heaven' (tseva hashamayim) are the divine council members "
                    "allotted to the nations (Deut 32:8-9) -- the same beings condemned in Psalm 82, the same "
                    "'princes' who resist Gabriel in Daniel 10:13, 20. Their 'rotting away' (yimmaqu -- "
                    "literally 'to dissolve, to melt, to putrefy') is a de-creation event: the spiritual "
                    "powers behind the nations are unmade. The heavens rolling up like a scroll reverses "
                    "the creation of the firmament in Genesis 1:6-8 -- the cosmos is being uncreated. "
                    "YHWH's sword (cherev) appears in heaven: 'For my sword (charbi) has drunk its fill "
                    "in the heavens (bashamayim); behold, it descends for judgment upon Edom (al-Edom)' "
                    "(34:5). The sword strikes first in heaven (against the spiritual powers) and then "
                    "descends to earth (against Edom, representing all hostile nations). The remainder of "
                    "the chapter describes Edom's devastation in gruesome detail: slaughter like a sacrifice "
                    "(34:6-7), streams turned to pitch and soil to sulfur (34:9-10), the land inhabited by "
                    "wild animals and chaos creatures (34:11-15). The chapter closes with an appeal to YHWH's "
                    "book: 'Seek and read from the book (sepher) of YHWH: Not one of these shall be missing' "
                    "(34:16).",

        "key_verse": {
            "ref": "Isaiah 34:4",
            "text": "All the host of heaven shall rot away, and the skies roll up like a scroll. All their host shall fall, as leaves fall from the vine, like leaves falling from the fig tree.",
            "translation": "ESV"
        },

        "original_terms": [
            "tseva hashamayim (host of heaven -- the divine council members assigned to govern the nations; the spiritual powers behind earthly kingdoms. This is NOT a reference to stars as physical objects but to the spiritual beings associated with the stars -- the 'sons of God' of Deut 32:8, the elohim of Psalm 82, the 'princes' of Daniel 10)",
            "yimmaqu (shall rot away/dissolve -- from the root maqaq, meaning to waste away, putrefy, decompose; used of flesh rotting (Zech 14:12) and of enemies melting in terror (Ps 38:5). Applied to the host of heaven, it describes their total dissolution -- they are unmade, decomposed back into non-existence)",
            "venigollu kasseper (rolled up like a scroll -- the heavens are treated as a written document that can be rolled shut; the cosmic order 'closed' by divine decree)",
            "cherem (devoted to destruction -- the holy war term for total consecration of the enemy to YHWH; nothing is spared, nothing is taken as spoil. When YHWH places the nations under cherem, it means his patience with their rebellion is exhausted)",
            "charbi (my sword -- YHWH's personal weapon, not a human instrument; the same divine sword of Deut 32:41-42, where YHWH says 'I will make my arrows drunk with blood, and my sword shall devour flesh')",
            "yibbol (shall fall/wither -- the same verb used for leaves falling from a tree; the host of heaven falls like autumn foliage, stripped of vitality)",
            "tohu vavohu (chaos and void -- 34:11 uses both tohu and vohu to describe Edom's devastation, the same words as Genesis 1:2; judgment is de-creation, a return to primordial chaos)"
        ],

        "ane_backdrop": "The concept of cosmic warfare in which both divine beings and human nations are judged "
                        "simultaneously is attested in ANE apocalyptic imagery but nowhere with the scope of "
                        "Isaiah 34. In the Ugaritic Baal Cycle, Baal defeats the sea god Yam and the death "
                        "god Mot, but the conflict is among the gods -- humanity is peripheral. In the "
                        "Babylonian Enuma Elish, Marduk defeats Tiamat and her host of monsters, using their "
                        "bodies to build the cosmos. Isaiah 34 reverses the creation pattern: instead of the "
                        "defeated host being used to build, the existing cosmic order is being dismantled. "
                        "The heavens rolling up like a scroll has no direct ANE parallel -- it assumes a "
                        "cosmos that can be 'written' and 'unwritten' by divine decree, reflecting the "
                        "biblical understanding of creation as speech-act (Ps 33:6). The devastation of "
                        "Edom (34:5-17) uses sacrificial language: the slaughter is described as a 'sacrifice' "
                        "(zevach) and a 'great slaughter' (tevach gadol) in Bozrah (34:6), recalling the "
                        "ritual killing of sacrificial animals. The nations' destruction is presented as a "
                        "cosmic offering to YHWH -- the inverse of worship.",

        "second_temple": [
            {
                "source": "Revelation 6:13-14",
                "summary": "'The stars of the sky fell to the earth as the fig tree sheds its winter fruit "
                           "when shaken by a gale. The sky vanished like a scroll that is being rolled up.'",
                "relevance": "John directly echoes Isaiah 34:4 -- the stars falling like figs and the sky "
                             "rolling up like a scroll. The 'stars' in Revelation's symbolic framework are "
                             "spiritual beings (cf. Rev 12:4, where the dragon sweeps a third of the stars "
                             "from heaven). The host of heaven's dissolution becomes a sign of the end."
            },
            {
                "source": "2 Peter 3:10-12",
                "summary": "'The heavens will pass away with a roar, and the heavenly bodies (stoicheia) will "
                           "be burned up and dissolved... the heavens will be set on fire and dissolved.'",
                "relevance": "Peter's description of cosmic dissolution echoes Isaiah 34:4. The Greek stoicheia "
                             "('elements/heavenly bodies') was used in Paul's letters (Gal 4:3, 9; Col 2:8, 20) "
                             "to refer to spiritual powers governing the old age -- the 'host of heaven' of "
                             "Isaiah 34 reinterpreted through Pauline spiritual-warfare theology."
            },
            {
                "source": "1 Enoch 18:13-16; 21:1-6",
                "summary": "Enoch sees 'stars that had transgressed the commandment of God' bound in a "
                           "terrible place of punishment, awaiting the great day of judgment.",
                "relevance": "The Enochic tradition interprets the 'host of heaven' as rebellious angelic "
                             "beings whose punishment is described in imagery parallel to Isaiah 34's "
                             "dissolution -- the stars that fall are divine beings who fell from their stations."
            },
            {
                "source": "Matthew 24:29",
                "summary": "Jesus says: 'The sun will be darkened, and the moon will not give its light, "
                           "and the stars will fall from heaven, and the powers (dynameis) of the heavens "
                           "will be shaken.'",
                "relevance": "Jesus' Olivet Discourse echoes Isaiah 34:4 explicitly. The 'powers of the "
                             "heavens' (dynameis ton ouranon) are the host of heaven -- the spiritual powers "
                             "that will be 'shaken' (saleuthesontai) at his return."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 24:21-22", "note": "'YHWH will punish the host of heaven in heaven' -- the parallel cosmic judgment text in the Isaiah Apocalypse; 34:4 intensifies 24:21 from punishment to dissolution", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The original allotment of nations to the sons of God -- Isaiah 34 is the judgment day for those allotted beings", "type": "ot"},
            {"ref": "Psalm 82:6-7", "note": "'You shall die like men, and fall like any prince' -- the divine council members who will 'fall' as Isaiah 34:4 describes", "type": "ot"},
            {"ref": "Daniel 10:13, 20", "note": "The Prince of Persia and Prince of Greece -- territorial spirits who are the 'host of heaven' facing judgment in Isaiah 34", "type": "ot"},
            {"ref": "Revelation 6:13-14", "note": "Stars falling like figs and the sky rolling up like a scroll -- John's direct citation of Isaiah 34:4", "type": "nt"},
            {"ref": "Matthew 24:29", "note": "Jesus quoting Isaiah 34:4 -- the 'powers of the heavens' shaken at his return", "type": "nt"},
            {"ref": "2 Peter 3:10-12", "note": "The heavens dissolved by fire -- Peter's eschatological reading of Isaiah 34's cosmic unmaking", "type": "nt"},
            {"ref": "Ephesians 6:12", "note": "'Cosmic powers over this present darkness' -- the same host of heaven that Isaiah 34 promises to dissolve", "type": "nt"},
            {"ref": "Colossians 2:15", "note": "Christ 'disarming the rulers and authorities' -- the cross as the beginning of the host of heaven's defeat", "type": "nt"},
            {"ref": "Isaiah 63:1-6", "note": "YHWH's judgment on Edom (Bozrah) -- the same geographical focus as 34:5-6, forming an inclusio around Second Isaiah", "type": "ot"},
            {"ref": "Deuteronomy 32:41-42", "note": "'I will make my sword devour flesh' -- YHWH's personal sword that appears in Isaiah 34:5", "type": "ot"},
            {"ref": "Genesis 1:2, 6-8", "note": "The tohu of pre-creation and the firmament -- Isaiah 34 reverses both: land returns to tohu, heavens roll up", "type": "ot"},
            {"ref": "1 Enoch 18:13-16", "note": "Stars that transgressed bound for judgment -- the Enochic expansion of the 'host of heaven' punishment tradition", "type": "dss"},
            {"ref": "Jude 6, 13", "note": "Angels who abandoned their proper dwelling kept in eternal chains -- 'wandering stars for whom the gloom of utter darkness has been reserved forever'", "type": "nt"}
        ],

        "divine_council_note": "Isaiah 34 is the most violent and comprehensive divine council judgment text in "
                               "the prophets. The simultaneous judgment of the nations and their spiritual "
                               "patrons -- 'all the nations... all their host' (34:2) and 'all the host of "
                               "heaven' (34:4) -- reveals that the Deuteronomy 32:8-9 allotment was never meant "
                               "to be permanent. The sons of God were given governance of the nations as a "
                               "stewardship. Psalm 82:2-4 shows that they failed: they judged unjustly, showed "
                               "partiality to the wicked, and neglected the weak. Isaiah 24:21-22 announces "
                               "their imprisonment. Isaiah 34:4 goes further: they do not merely lose their "
                               "positions -- they dissolve. The verb maqaq ('to rot away, putrefy') is applied "
                               "to beings who were once 'stars' in the council (cf. Job 38:7, where the 'morning "
                               "stars sang together' at creation). Their dissolution is the reversal of their "
                               "creation: as YHWH spoke them into being, so he now speaks them out of being. "
                               "The heavens rolling up like a scroll is the unwriting of the cosmic order: the "
                               "firmament of Genesis 1:6-8 is treated as a document that YHWH can close. The "
                               "descent of YHWH's sword from heaven to earth (34:5) follows the same pattern as "
                               "the judgment in 24:21-22: the spiritual realm is judged first, then the earthly. "
                               "The sword 'drinks its fill in heaven' before it falls on Edom -- the cosmic "
                               "powers are dealt with before their human clients. This passage is foundational "
                               "for the entire New Testament theology of cosmic spiritual warfare: Paul's "
                               "'rulers and authorities' (Eph 6:12; Col 2:15), Peter's dissolved heavens "
                               "(2 Pet 3:10-12), and Jesus' 'powers of the heavens shaken' (Matt 24:29) all "
                               "draw on Isaiah 34:4's vision of the divine council's rebellious members being "
                               "unmade. The passage also connects to Christ's victory: Colossians 2:15 declares "
                               "that on the cross, Christ 'disarmed the rulers and authorities and put them "
                               "to open shame, triumphing over them' -- the dissolution of the host of heaven "
                               "begins at Calvary and will be consummated at Christ's return.",

        "sections": [
            {
                "heading": "The Universal Summons and the Cherem of the Nations (34:1-3)",
                "body": "'Draw near (qirvu), O nations (goyim), to hear, and give attention (haqshivu), O "
                        "peoples (le'ummim)! Let the earth hear (tishma ha'arets), and all that fills it; "
                        "the world (tevel), and all that comes from it' (34:1). The summons is comprehensive: "
                        "nations, peoples, the earth itself, and everything in it. The entire created order "
                        "is called to witness YHWH's judgment. 'For YHWH is enraged (qetseph la-YHWH) "
                        "against all the nations (kol-haggoyim), and furious (chemah) against all their "
                        "host (kol-tseva'am)' (34:2a). The word tseva'am ('their host') is ambiguous and "
                        "pregnant with meaning: it can refer to the nations' armies, but in context with "
                        "the 'host of heaven' in 34:4, it creates a deliberate parallel -- the nations' "
                        "earthly host and the heavenly host are both under judgment. 'He has devoted them "
                        "to destruction (hecherimam), has given them over to slaughter (letevach natanum)' "
                        "(34:2b). The cherem is the total ban of holy war -- Jericho was placed under cherem "
                        "(Josh 6:17-21), and now the nations themselves receive the same treatment. 'Their "
                        "slain (challeleihem) shall be cast out (yushlikhu), and the stench (bo'sham) of "
                        "their corpses shall rise; the mountains shall flow (venamassu) with their blood' "
                        "(34:3). The mountains flowing with blood is apocalyptic hyperbole expressing the "
                        "totality of the destruction."
            },
            {
                "heading": "The Host of Heaven Dissolved: Cosmic De-Creation (34:4-5)",
                "body": "'All the host of heaven (kol-tseva hashamayim) shall rot away (yimmaqu)' (34:4a). "
                        "The tseva hashamayim are the divine beings assigned to govern the nations -- the "
                        "'sons of God' (benei elohim) of Deuteronomy 32:8 (LXX/DSS), the elohim condemned "
                        "in Psalm 82, the 'princes' (sarim) of Persia and Greece in Daniel 10. Their "
                        "'rotting' (maqaq) is not mere defeat but decomposition -- they are unmade, returned "
                        "to non-existence. This is the ultimate consequence of the verdict in Psalm 82:7: "
                        "'You shall die like men (ke-adam) and fall like any prince (ke-achad hasarim).' "
                        "Isaiah 34:4 describes what that death looks like: dissolution. 'And the skies "
                        "(shamayim) roll up (venigollu) like a scroll (kasseper)' (34:4b). The heavens "
                        "themselves -- the firmament (raqia) of Genesis 1:6-8, the expanse that separates "
                        "the waters above from the waters below -- are treated as a written document that "
                        "YHWH can roll shut. The cosmos is a scroll YHWH has written, and he can unwrite it. "
                        "'All their host shall fall (yibbol kol-tseva'am), as leaves fall (kinevol aleh) "
                        "from the vine (migeppen), like leaves falling from the fig tree (kimmolet "
                        "mite'enah)' (34:4c). The host of heaven falling like autumn leaves is a devastating "
                        "image: the once-glorious divine beings, the 'stars' who sang at creation (Job 38:7), "
                        "now wither and drop like dead vegetation. The vine and fig tree are symbols of "
                        "covenant blessing in the OT (1 Kgs 4:25; Mic 4:4) -- their withered leaves signal "
                        "the end of the old covenant order between YHWH and the nations' gods. 'For my sword "
                        "(charbi) has drunk its fill (rivvetah) in the heavens (bashamayim); behold, it "
                        "descends (teired) for judgment (lemishpat) upon Edom' (34:5). YHWH's sword operates "
                        "in two realms: it strikes first in heaven (against the spiritual powers) and then "
                        "descends to earth (against Edom). The sequence is theologically critical: the "
                        "spiritual powers must be dealt with before their earthly manifestations can be "
                        "judged. This two-stage pattern (heavenly judgment preceding earthly judgment) "
                        "reappears in Daniel 10 (the prince of Persia defeated before Persia falls), in "
                        "Colossians 2:15 (Christ disarming rulers before the gospel goes to the nations), "
                        "and in Revelation 12 (Satan expelled from heaven before the earthly persecution)."
            },
            {
                "heading": "Edom's Devastation: De-Creation in Detail (34:5-17)",
                "body": "Edom becomes the representative of all hostile nations. 'For YHWH has a sacrifice "
                        "(zevach) in Bozrah and a great slaughter (tevach gadol) in the land of Edom' (34:6). "
                        "The slaughter is described in sacrificial terms -- the nations' judgment is presented "
                        "as a cosmic offering. 'Wild oxen (re'emim) shall fall with them, and young steers "
                        "(parim) with the mighty bulls (abbirim). Their land shall drink its fill (rivvetah) "
                        "of blood, and their soil shall be gorged (yedushshan) with fat' (34:7). The language "
                        "mirrors sacrificial liturgy: blood poured out and fat consumed, but here the sacrifice "
                        "is the nation itself. 'For YHWH has a day of vengeance (yom naqam), a year of "
                        "recompense (shillumim) for the cause (riv) of Zion' (34:8). The judgment is not "
                        "arbitrary but forensic: YHWH has a legal case (riv) on behalf of Zion. The "
                        "desolation becomes total: 'Its streams (nechalehah) shall be turned into pitch "
                        "(zepheth), and its soil into sulfur (gophrith); its land shall become burning "
                        "pitch' (34:9) -- Sodom-and-Gomorrah language (cf. Gen 19:24). 'Night and day "
                        "(laylah veyomam) it shall not be quenched (lo tikhbeh); its smoke shall go up "
                        "forever (le'olam)' (34:10). The ever-burning, ever-smoking ruin anticipates the "
                        "Gehenna imagery of 66:24. The land returns to primordial chaos: YHWH stretches out "
                        "'the measuring line of tohu (chaos) and the plumb stones of vohu (void)' over it "
                        "(34:11) -- the same tohu vavohu of Genesis 1:2. Creation is being reversed. The "
                        "chapter closes with YHWH's guarantee: 'Seek and read from the book (sepher) of "
                        "YHWH: Not one of these shall be missing (lo ne'derah); none shall be without her "
                        "mate (re'utah). For my mouth has commanded, and his Spirit (rucho) has gathered "
                        "them' (34:16). The 'book of YHWH' is the divine council's written decree -- YHWH's "
                        "judgments are recorded and will be fulfilled to the letter."
            }
        ]
    },

    {
        "id": "isa-35",
        "ref": "Isaiah 35",
        "chapter_num": 35,
        "title": "The Ransomed Return: Highway of Holiness",
        "era": "isaiah_woe",
        "type": "chapter",
        "themes": ["REVERSAL", "LAND", "HOLY"],

        "synopsis": "Isaiah 35 is a dazzling vision of restoration that serves as the theological "
                    "bridge between First Isaiah (1-39) and Second Isaiah (40-55). The wilderness "
                    "blooms: 'The wilderness and the dry land shall be glad; the desert shall rejoice "
                    "and blossom like the crocus' (35:1). Nature itself participates in the redemption: "
                    "'They shall see the glory (kavod) of YHWH, the majesty (hadar) of our God' (35:2). "
                    "The prophet calls for courage: 'Strengthen the weak hands, and make firm the "
                    "feeble knees. Say to those who have an anxious heart, Be strong; fear not! Behold, "
                    "your God (Eloheikhem) will come with vengeance (naqam), with the recompense of God "
                    "(gemul elohim). He will come and save you' (35:3-4). Then the healing: 'The eyes "
                    "of the blind shall be opened, and the ears of the deaf unstopped. Then shall the "
                    "lame man leap like a deer, and the tongue of the mute sing for joy' (35:5-6). "
                    "Waters break forth in the wilderness, and a 'Highway of Holiness' (mesillah "
                    "vedarek derekh haqqodesh) will be raised: 'The unclean shall not pass over it... "
                    "No lion shall be there... but the redeemed shall walk there. And the ransomed of "
                    "YHWH (peduyyei YHWH) shall return and come to Zion with singing' (35:8-10).",

        "key_verse": {
            "ref": "Isaiah 35:5-6",
            "text": "Then the eyes of the blind shall be opened, and the ears of the deaf unstopped; then shall the lame man leap like a deer, and the tongue of the mute sing for joy.",
            "translation": "ESV"
        },

        "original_terms": [
            "mesillah (highway -- a raised road, prepared and graded for easy travel)",
            "derekh haqqodesh (Way of Holiness -- the sacred road for the redeemed)",
            "peduyyei YHWH (the ransomed of YHWH -- those redeemed by God's purchase-price)",
            "naqam (vengeance -- not vindictiveness but righteous retribution that restores justice)",
            "simchat olam (everlasting joy -- the permanent gladness of the redeemed)"
        ],

        "ane_backdrop": "Royal highways were major infrastructure projects in the ANE. The Persian "
                        "Royal Road (5th c. BC) stretched over 1,600 miles. Assyrian and Babylonian "
                        "kings built processional highways for religious festivals -- the Processional "
                        "Way (Ai-ibur-shabu) in Babylon was decorated with glazed-brick lions and used "
                        "for the Akitu (New Year) festival procession. Isaiah's Highway of Holiness "
                        "transforms the ANE processional way into a pilgrimage road for the redeemed, "
                        "leading not to a pagan temple but to Zion.",

        "second_temple": [
            {
                "source": "Matthew 11:4-5",
                "summary": "Jesus tells John the Baptist's disciples: 'The blind receive their sight "
                           "and the lame walk, lepers are cleansed and the deaf hear, and the dead "
                           "are raised up.'",
                "relevance": "Jesus points to his miracles as evidence that Isaiah 35:5-6 is being "
                             "fulfilled -- the messianic age has dawned."
            },
            {
                "source": "Luke 7:22",
                "summary": "Luke's parallel: Jesus cites Isaiah 35 and 61 as the evidence of his "
                           "messianic identity.",
                "relevance": "The healing miracles of Jesus are presented as the Isaiah 35 restoration "
                             "in action."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 40:3-5", "note": "'A highway for our God in the wilderness' -- the same highway motif opening Second Isaiah", "type": "ot"},
            {"ref": "Isaiah 29:18", "note": "The deaf hearing and the blind seeing -- the reversal promised in 29 is elaborated in 35", "type": "ot"},
            {"ref": "Matthew 11:4-5", "note": "Jesus' miracles as evidence of Isaiah 35's fulfillment", "type": "nt"},
            {"ref": "Revelation 21:1-4", "note": "The new creation where 'death shall be no more, neither shall there be mourning' -- the Isaiah 35 vision consummated", "type": "nt"},
            {"ref": "Isaiah 51:11", "note": "'The ransomed of YHWH shall return and come to Zion with singing' -- nearly identical to 35:10", "type": "ot"}
        ],

        "divine_council_note": "Isaiah 35 envisions the divine warrior's return to Zion with his "
                               "redeemed people. The language of 'vengeance' (naqam) and 'recompense' "
                               "(gemul) in 35:4 describes YHWH as the council's enforcer, executing "
                               "judgment against oppressors and liberating his people. The Highway of "
                               "Holiness (35:8) is the route of the new exodus -- the path on which YHWH "
                               "leads his ransomed people (peduyyei YHWH) home. The healing of the blind, "
                               "deaf, lame, and mute (35:5-6) reverses the judicial blindness decreed in "
                               "6:9-10 and 29:10-12. The council that imposed the affliction now removes "
                               "it. The final verse (35:10) describes the redeemed arriving in Zion with "
                               "'everlasting joy (simchat olam) upon their heads, and sorrow and sighing "
                               "shall flee away' -- the permanent state of the redeemed in the presence "
                               "of the Holy One.",

        "sections": [
            {
                "heading": "The Wilderness Blooms and the Healing Comes (35:1-6)",
                "body": "'The wilderness (midbar) and the dry land (tsiyyah) shall be glad; the desert "
                        "(aravah) shall rejoice and blossom like the crocus (chavatstselet)' (35:1). "
                        "The three terms for arid landscape -- midbar, tsiyyah, aravah -- represent the "
                        "totality of desolation now transformed. 'They shall see the glory of YHWH, "
                        "the majesty of our God' (35:2). Creation responds to the presence of the divine "
                        "warrior. The call to courage (35:3-4) echoes the commissioning language of "
                        "Joshua 1: 'Be strong (chizqu), fear not (al-tira'u).' The God who comes is "
                        "both judge and savior: 'He will come with naqam (vengeance), with the gemul "
                        "(recompense) of God. He will come and save you (yoshia'khem)' (35:4). Then the "
                        "cascade of healing: 'The eyes of the blind shall be opened (tipaqachnah), and "
                        "the ears of the deaf unstopped (tippatachnah). Then shall the lame man leap like "
                        "a deer, and the tongue of the mute sing for joy (terannein)' (35:5-6a). "
                        "Waters break forth in the wilderness, streams in the desert (35:6b)."
            },
            {
                "heading": "The Highway of Holiness and the Ransomed Return (35:7-10)",
                "body": "'And a highway (mesillah) shall be there, and a way (derekh), and it shall be "
                        "called the Way of Holiness (derekh haqqodesh); the unclean shall not pass over "
                        "it' (35:8). The highway is ritually pure -- set apart for the redeemed. No "
                        "predator will threaten: 'No lion shall be there, nor shall any ravenous beast "
                        "come up on it' (35:9) -- recalling the Edenic animal peace of 11:6-9. 'But the "
                        "redeemed (ge'ulim) shall walk there' (35:9). 'And the ransomed of YHWH "
                        "(peduyyei YHWH) shall return and come to Zion with singing (rinnah), with "
                        "everlasting joy (simchat olam) upon their heads; they shall obtain gladness and "
                        "joy, and sorrow (yagon) and sighing (anachah) shall flee away' (35:10). The "
                        "verbs are triumphant: return, come, sing, obtain. The nouns are permanent: "
                        "everlasting joy, gladness. The negations are final: sorrow and sighing flee. "
                        "This is not a temporary reprieve but the permanent state of the redeemed."
            }
        ]
    }
]
