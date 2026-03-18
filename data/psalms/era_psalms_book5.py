"""
era_psalms_book5.py -- Psalms 107-150 (Book V): Return, Praise, and Consummation

Book V is the Psalter's finale -- the resolution of the five-book arc that
began with Torah meditation (Ps 1), traced the rise and crisis of the Davidic
covenant (Books I-III), and answered with YHWH's eternal kingship (Book IV).
Book V moves toward consummation: the post-exilic psalms of return (Ps 107),
the Songs of Ascents (Pss 120-134) that trace the pilgrim's journey to
Jerusalem, the great Torah meditation of Psalm 119, the royal-messianic
psalms that renew the Davidic hope (Pss 110, 118, 132), and the final
Hallelujah chorus (Pss 146-150) that crescendos into the command for
everything that has breath to praise YHWH. The divine council theme reaches
its climax: Psalm 110 installs the Messiah at YHWH's right hand as priest-
king after the order of Melchizedek, Psalm 148 summons the entire heavenly
host to worship, and the final Hallelujah psalms envision the cosmic praise
that is the divine council's ultimate purpose. The Psalter ends not with
lament but with praise -- the consummation toward which all creation moves.
"""

CHAPTERS = [
    {
        "id": "ps-107-120-134",
        "ref": "Psalms 107, 120-134",
        "chapter_num": 1,
        "title": "Psalms of Return and the Songs of Ascents -- Post-Exilic Hope and Pilgrimage",
        "era": "psalms_book5",
        "type": "chapter",
        "themes": ["EXILE", "REVERSAL", "LAND", "REMEMBER"],

        "synopsis": "Psalm 107 opens Book V with a post-exilic celebration of YHWH's deliverance: 'Oh "
                    "give thanks to YHWH, for he is good, for his steadfast love (chesed) endures forever! "
                    "Let the redeemed (ge'ulei) of YHWH say so, whom he has redeemed from trouble and "
                    "gathered in from the lands, from the east and from the west, from the north and from "
                    "the south' (107:1-3). The four-fold gathering from every direction answers the prayer "
                    "of Psalm 106:47 ('gather us from among the nations') and signals that the exile is "
                    "ending. The psalm traces four types of distress -- wandering in the wilderness, "
                    "imprisonment, sickness, and storm at sea -- each resolved by the same refrain: 'Then "
                    "they cried to YHWH in their trouble, and he delivered them from their distress' "
                    "(107:6, 13, 19, 28). The Songs of Ascents (Psalms 120-134) form a distinct subcollection "
                    "-- fifteen psalms sung by pilgrims ascending to Jerusalem for the annual festivals. They "
                    "trace the journey from distress in a foreign land ('Woe to me, that I sojourn in "
                    "Meshech,' 120:5) through the joyful approach to Jerusalem ('I was glad when they said "
                    "to me, Let us go to the house of YHWH!' 122:1) to the final blessing from Zion "
                    "('May YHWH bless you from Zion, he who made heaven and earth!' 134:3). The journey "
                    "is both geographical and spiritual: approaching the earthly Temple is approaching the "
                    "replica of the heavenly council chamber.",

        "key_verse": {
            "ref": "Psalm 122:1",
            "text": "I was glad when they said to me, 'Let us go to the house of the LORD!'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ge'ulei YHWH (the redeemed of YHWH -- those brought back from exile; the covenant people restored)",
            "chesed (steadfast love/covenant loyalty -- the refrain of Ps 107; YHWH's faithfulness that outlasts exile)",
            "shir hamma'alot (song of ascents/song of the steps -- the superscription of Pss 120-134; pilgrim songs for going up to Jerusalem)",
            "ma'alah (ascent/going up -- pilgrimage to Jerusalem; both physical elevation and spiritual approach to YHWH's presence)",
            "Tsiyyon (Zion -- the destination of pilgrimage; the holy mountain where YHWH dwells; the earthly counterpart of the heavenly throne)",
            "shalom Yerushalaim (peace of Jerusalem -- the pilgrim's prayer in Ps 122:6; peace for the city where YHWH's name dwells)",
            "gar (to sojourn -- the pilgrim as temporary resident in a foreign land; longing for home in YHWH's presence)"
        ],

        "ane_backdrop": "Pilgrimage to central sanctuaries was common in the ANE. The great temples of "
                        "Mesopotamia (Marduk's Esagila in Babylon, Enlil's Ekur in Nippur) drew pilgrims "
                        "from surrounding regions. The Egyptian temple at Karnak was a pilgrimage "
                        "destination for centuries. The Israelite pilgrimage festival system (Passover, "
                        "Weeks, Tabernacles -- Deut 16:16) was distinctive in requiring attendance by all "
                        "males three times per year at the central sanctuary. The Songs of Ascents reflect "
                        "a post-exilic context where pilgrimage to Jerusalem has been restored but the "
                        "community lives with the memory of exile and the reality of foreign domination. "
                        "The physical ascent to Jerusalem (which sits at ~2,500 feet elevation) made the "
                        "pilgrimage a literal 'going up' -- the verb 'alah ('to go up, ascend') is "
                        "technical vocabulary for traveling to Jerusalem. The fifteen Songs of Ascents may "
                        "correspond to the fifteen steps between the Court of Women and the Court of Israel "
                        "in the Second Temple, where the Levites sang (Mishnah, Middot 2:5; Sukkah 5:4).",

        "second_temple": [
            {
                "source": "Mishnah Sukkah 5:4",
                "summary": "The Mishnah records that Levites stood on the fifteen steps leading from the "
                           "Court of Israel to the Court of Women and sang the fifteen Songs of Ascents "
                           "during the Sukkot water-drawing ceremony.",
                "relevance": "This liturgical tradition connects the Songs of Ascents to the Second Temple's "
                             "architecture and worship -- the psalms were sung on the physical steps of the "
                             "Temple itself."
            },
            {
                "source": "Ezra 1:1-4; 2:1-70",
                "summary": "Ezra records the return from exile under Cyrus's decree, including the "
                           "restoration of the Temple vessels and the list of returnees.",
                "relevance": "Psalm 107's celebration of gathering 'from the lands' finds its historical "
                             "fulfillment in the return under Cyrus -- the 'redeemed of YHWH' coming home."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 106:47", "note": "'Save us, O YHWH our God, and gather us from among the nations' -- the prayer that Ps 107 answers", "type": "ot"},
            {"ref": "Deuteronomy 16:16", "note": "'Three times a year all your males shall appear before YHWH your God at the place that he will choose' -- the pilgrimage command behind the Songs of Ascents", "type": "ot"},
            {"ref": "Ezra 1:1-4", "note": "Cyrus's decree allowing the return from exile -- the historical context of Ps 107", "type": "ot"},
            {"ref": "Isaiah 35:10", "note": "'And the ransomed of YHWH shall return and come to Zion with singing' -- the prophetic vision that Ps 107 and the Songs of Ascents celebrate", "type": "ot"},
            {"ref": "Hebrews 12:22", "note": "'You have come to Mount Zion and to the city of the living God, the heavenly Jerusalem, and to innumerable angels in festal gathering' -- the spiritual reality behind the physical pilgrimage", "type": "nt"},
            {"ref": "John 7:37-38", "note": "Jesus cries out at the Feast of Tabernacles (when the Songs of Ascents were sung): 'If anyone thirsts, let him come to me and drink'", "type": "nt"}
        ],

        "divine_council_note": "The Songs of Ascents represent the pilgrim's approach to the earthly "
                               "replica of the divine council chamber. Jerusalem's Temple was understood as "
                               "the terrestrial counterpart of YHWH's heavenly throne room (cf. Exod 25:9, "
                               "40 -- the tabernacle built according to the 'pattern' (tavnit) shown on "
                               "the mountain). To ascend to the Temple was to approach the place where heaven "
                               "and earth intersect -- where YHWH's presence 'dwells' among his people as it "
                               "'dwells' among his heavenly council. Psalm 121:1-2 captures this: 'I lift up "
                               "my eyes to the mountains -- from where does my help come? My help comes from "
                               "YHWH, who made heaven and earth.' The mountains are not the source of help "
                               "(as in Canaanite high-place worship) but the direction in which one looks "
                               "toward YHWH. Psalm 123:1 intensifies: 'To you I lift up my eyes, O you who "
                               "are enthroned in the heavens!' The pilgrimage destination is ultimately "
                               "heavenly, not earthly. Psalm 134 -- the final Song of Ascents -- commands the "
                               "Temple servants to 'bless YHWH' and promises: 'May YHWH bless you from Zion, "
                               "he who made heaven and earth!' (134:3). The blessing flows from Zion because "
                               "Zion is where the divine council's authority touches the earth. The phrase "
                               "'who made heaven and earth' (oseh shamayim va'arets) recurs throughout the "
                               "Songs of Ascents (121:2; 124:8; 134:3) -- a confession that the God of the "
                               "pilgrimage is not a local deity but the Creator of all, the Most High who "
                               "presides over every spiritual power.",

        "sections": [
            {
                "heading": "What Are the 'Songs of Ascents' and Why Are They Called That?",
                "body": "Psalms 120-134 each bear the superscription <em>Shir Hamma'alot</em> -- "
                        "'A Song of Ascents' (or 'A Song of Steps'). This collection of fifteen "
                        "short psalms forms one of the most beloved subcollections in the Psalter, "
                        "but the title raises an immediate question: why 'ascents'?<br><br>"
                        "The word <em>ma'alah</em> means 'a going up, an ascent, a step.' Three "
                        "main explanations have been proposed:<br><br>"
                        "<strong>(1) Pilgrimage psalms</strong>: These were sung by pilgrims "
                        "traveling 'up' to Jerusalem for the three annual festivals (Passover, "
                        "Weeks, and Tabernacles). In Hebrew, one always 'goes up' (<em>'alah</em>) "
                        "to Jerusalem, regardless of one's starting point, because Jerusalem sits "
                        "on a hill (about 2,500 feet elevation) and because it is the spiritual "
                        "center of the land. The psalms trace the journey: from distress in a "
                        "foreign land (Ps 120) to the joyful arrival at Jerusalem (Ps 122) to the "
                        "final blessing in the Temple (Ps 134).<br><br>"
                        "<strong>(2) Temple steps</strong>: The Mishnah (Middot 2:5; Sukkah 5:4) "
                        "records that the Levites stood on the fifteen steps between the Court of "
                        "Women and the Court of Israel in the Second Temple and sang these fifteen "
                        "psalms during the water-drawing ceremony at the Feast of Tabernacles. One "
                        "psalm per step.<br><br>"
                        "<strong>(3) Graduated structure</strong>: Many of these psalms use a "
                        "literary technique called 'step parallelism' or 'staircase parallelism,' "
                        "where a key word from the end of one line is picked up at the beginning "
                        "of the next, creating a climbing effect. Example from Psalm 121: 'He will "
                        "not let your foot be moved; he who <em>keeps</em> you will not slumber. "
                        "Behold, he who <em>keeps</em> Israel will neither slumber nor sleep' "
                        "(121:3-4).<br><br>"
                        "These explanations are not mutually exclusive. The Songs of Ascents were "
                        "likely pilgrimage songs that were also used liturgically in the Temple, "
                        "and their literary structure mirrors the upward movement their content "
                        "describes."
            },
            {
                "heading": "The Exile and the Return: Historical Context for Book V",
                "body": "Book V opens with Psalm 107's celebration of YHWH gathering his people "
                        "'from the lands, from the east and from the west, from the north and "
                        "from the south' (107:2-3). To understand the joy of this psalm, readers "
                        "must understand what had been lost.<br><br>"
                        "In 586 BC, the Babylonian Empire under King Nebuchadnezzar conquered "
                        "Jerusalem, destroyed Solomon's Temple, and deported much of the population "
                        "to Babylon (modern Iraq). This event -- <strong>the Exile</strong> (also "
                        "called <strong>the Babylonian Captivity</strong>) -- was the greatest "
                        "catastrophe in Israel's history. The three pillars of Israel's identity "
                        "were destroyed simultaneously: the <em>land</em> (conquered), the "
                        "<em>Temple</em> (burned), and the <em>Davidic monarchy</em> (ended). "
                        "Psalm 137 captures the anguish: 'By the waters of Babylon, there we sat "
                        "down and wept, when we remembered Zion.'<br><br>"
                        "Approximately 70 years later (538 BC), the Persian King Cyrus conquered "
                        "Babylon and issued a decree allowing the Jews to return to Jerusalem and "
                        "rebuild their Temple (Ezra 1:1-4). This event -- <strong>the Return</strong> "
                        "(or <em>the Restoration</em>) -- began a new chapter in Israel's story, "
                        "but it was bittersweet. The Second Temple was completed in 516 BC, but it "
                        "was far less glorious than Solomon's original (Ezra 3:12 -- the old men "
                        "wept when they saw it). No Davidic king returned to the throne. The "
                        "nation lived under foreign rule -- first Persian, then Greek, then Roman "
                        "-- for the rest of the Old Testament period and beyond.<br><br>"
                        "Book V of the Psalms reflects this post-exilic context: gratitude for "
                        "the return (Ps 107), pilgrimage to the restored Jerusalem (Pss 120-134), "
                        "renewed hope in the Davidic covenant (Pss 110, 132), and a deepened "
                        "understanding that YHWH's ultimate purposes transcend any earthly kingdom."
            },
            {
                "heading": "Psalm 107: Gathered from the Lands -- The Redeemed Return",
                "body": "'Oh give thanks (hodu) to YHWH, for he is good (tov), for his steadfast love "
                        "(chesed) endures forever (le'olam)!' (107:1). This opening echoes the great "
                        "thanksgiving formula (cf. Ps 106:1; 1 Chr 16:34) but now with a new context: "
                        "'Let the redeemed (ge'ulei) of YHWH say so, whom he has redeemed from trouble "
                        "and gathered in (qibbetsam) from the lands (me'aratsot), from the east and from "
                        "the west, from the north and from the south (yam, lit. 'sea')' (107:2-3). The "
                        "four-directional gathering signals the ingathering from exile -- the scattered "
                        "people returning from every direction. The psalm then presents four vignettes of "
                        "distress and deliverance, each ending with the refrain: 'Let them thank YHWH "
                        "for his steadfast love, for his wondrous works to the children of man!' "
                        "(107:8, 15, 21, 31). The wanderers in the desert found no city (107:4-9). The "
                        "prisoners sat in darkness and chains (107:10-16). The sick drew near the gates "
                        "of death (107:17-22). The sailors were tossed by storms (107:23-32). Each group "
                        "cries to YHWH and is delivered. The closing meditation: 'He turns rivers into "
                        "a desert... he turns a desert into pools of water' (107:33-35). YHWH transforms "
                        "landscapes and situations. 'Whoever is wise (chakham), let him attend to these "
                        "things; let them consider the steadfast love (chasdei) of YHWH' (107:43)."
            },
            {
                "heading": "Songs of Ascents (Psalms 120-134): The Pilgrim's Journey to Zion",
                "body": "The fifteen Songs of Ascents trace a spiritual journey from alienation to "
                        "blessing. Psalm 120 begins in distress: 'In my distress I called to YHWH, and "
                        "he answered me' (120:1). The psalmist laments living 'among the tents of Kedar' "
                        "and sojourning 'in Meshech' (120:5) -- far from YHWH's presence. Psalm 121 "
                        "marks the turning toward Jerusalem: 'I lift up my eyes to the mountains "
                        "(haharim)' (121:1). The four-fold repetition of shamar ('to keep, guard') "
                        "in 121:3-8 assures the pilgrim of YHWH's protection on the journey: 'He will "
                        "not let your foot be moved; he who keeps you will not slumber' (121:3). Psalm "
                        "122 arrives at Jerusalem: 'I was glad (samachti) when they said to me, Let us "
                        "go to the house of YHWH! Our feet have been standing within your gates, O "
                        "Jerusalem!' (122:1-2). The prayer for peace: 'Pray for the peace (shalom) of "
                        "Jerusalem! May they be secure who love you!' (122:6). The middle psalms address "
                        "the pilgrim's condition: dependence on YHWH (123), deliverance from enemies "
                        "(124), security of the righteous (125), joy of restoration (126 -- 'When YHWH "
                        "restored the fortunes of Zion, we were like those who dream,' 126:1), the "
                        "futility of effort without YHWH (127 -- 'Unless YHWH builds the house, those "
                        "who build it labor in vain,' 127:1), the blessings of fearing YHWH (128), "
                        "Israel's sufferings overcome (129), waiting for YHWH from the depths (130 -- "
                        "'Out of the depths I cry to you, O YHWH!' 130:1), humble trust (131), and the "
                        "Davidic covenant at Zion (132). Psalm 133 celebrates the unity of the gathered "
                        "community: 'Behold, how good and pleasant it is when brothers dwell in unity "
                        "(yachad)!' (133:1). Psalm 134 closes the collection with the night-watch blessing: "
                        "'Come, bless YHWH, all you servants of YHWH, who stand by night in the house of "
                        "YHWH!' (134:1). The journey is complete: from exile to Zion, from distress to "
                        "worship, from the tents of Kedar to the house of YHWH."
            }
        ]
    },

    {
        "id": "ps-110-118-132",
        "ref": "Psalms 110, 118, 132",
        "chapter_num": 2,
        "title": "Royal and Messianic Psalms -- Melchizedek, the Rejected Stone, and the Davidic Covenant",
        "era": "psalms_book5",
        "type": "chapter",
        "themes": ["KING", "PRIEST", "DC", "SEED", "COV"],

        "synopsis": "Book V contains three of the most theologically significant royal-messianic psalms in "
                    "the Psalter. Psalm 110 is the most quoted Old Testament verse in the New Testament: "
                    "'YHWH says to my Lord (adoni): Sit at my right hand, until I make your enemies your "
                    "footstool' (110:1). David writes of a figure he calls 'my Lord' who is invited to "
                    "share YHWH's throne and declared 'a priest forever after the order of Melchizedek' "
                    "(110:4) -- combining kingship and priesthood in a way the Mosaic covenant kept separate. "
                    "Psalm 118, the climax of the Egyptian Hallel (Pss 113-118), contains the rejected-stone "
                    "prophecy: 'The stone that the builders rejected has become the cornerstone (rosh "
                    "pinnah). This is YHWH's doing; it is marvelous in our eyes' (118:22-23). Jesus applies "
                    "this directly to himself (Matt 21:42). Psalm 132 renews the Davidic covenant promise "
                    "at Zion: 'YHWH swore to David a sure oath from which he will not turn back: One of "
                    "the sons of your body I will set on your throne' (132:11). Together, these three psalms "
                    "establish the messianic program: a priest-king at YHWH's right hand, rejected by human "
                    "builders but chosen by YHWH, enthroned on Zion in fulfillment of the Davidic covenant.",

        "key_verse": {
            "ref": "Psalm 110:1, 4",
            "text": "The LORD says to my Lord: 'Sit at my right hand, until I make your enemies your footstool.' ... The LORD has sworn and will not change his mind, 'You are a priest forever after the order of Melchizedek.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ne'um YHWH la'adoni (oracle of YHWH to my lord -- the divine decree installing a figure at YHWH's right hand; the most important messianic formula in the OT)",
            "shev limini (sit at my right hand -- the position of supreme authority; sharing YHWH's throne in the divine council)",
            "kohen le'olam al-divrati Malkhi-Tsedeq (a priest forever after the order of Melchizedek -- a non-Levitical, eternal priesthood combining royal and priestly functions)",
            "even ma'asu habonim (the stone the builders rejected -- the foundation stone chosen by YHWH, rejected by human builders; applied to Christ)",
            "rosh pinnah (cornerstone/capstone -- the chief stone of the building; the one upon which the entire structure depends)",
            "nishba YHWH (YHWH has sworn -- the irrevocable oath confirming the Davidic covenant at Zion)",
            "menuchah (resting place -- YHWH's rest at Zion; the place where his presence permanently dwells)"
        ],

        "ane_backdrop": "The concept of a figure seated at the deity's right hand has deep ANE roots. "
                        "Egyptian pharaohs were depicted seated at the right hand of Amun or Horus, "
                        "signifying divine authorization. In Ugaritic texts, favored deities or kings "
                        "occupied positions of honor at El's right hand in the divine council. Psalm 110's "
                        "Melchizedek reference reaches back to Genesis 14:18-20 and the ancient Canaanite "
                        "tradition of a priest-king at Salem (Jerusalem). Melchizedek's name means 'my "
                        "king is righteousness' (or 'king of righteousness' in Hebrews 7:2) -- a title "
                        "connected to the pre-Israelite worship of El Elyon at Jerusalem. The institution "
                        "of the 'cornerstone' (rosh pinnah, Ps 118:22) is architecturally significant: "
                        "the cornerstone was the first stone laid, determining the alignment of the entire "
                        "building. Mesopotamian temple inscriptions describe the selection and laying of "
                        "foundation stones with elaborate ritual -- the cornerstone was sacred. Psalm 132's "
                        "connection of the Davidic covenant to Zion reflects the theological claim that "
                        "YHWH chose both a dynasty and a location -- the king and the mountain together "
                        "constitute YHWH's earthly governance.",

        "second_temple": [
            {
                "source": "Matthew 22:41-46",
                "summary": "Jesus asks the Pharisees: 'If David calls him Lord, how is he his son?' -- "
                           "using Psalm 110:1 to demonstrate that the Messiah is not merely David's "
                           "descendant but his Lord, a divine figure who shares YHWH's throne.",
                "relevance": "Jesus' use of Psalm 110 is the most direct argument for the Messiah's "
                             "divinity in the Synoptic Gospels. The puzzle is intentional: only a figure "
                             "who is both David's descendant (human) and David's Lord (divine) resolves it."
            },
            {
                "source": "Hebrews 5:5-10; 7:1-28",
                "summary": "The author of Hebrews builds the entire christological argument about Jesus' "
                           "priesthood on Psalm 110:4: 'You are a priest forever, after the order of "
                           "Melchizedek.' The Melchizedek priesthood supersedes the Levitical order.",
                "relevance": "Hebrews demonstrates that Psalm 110's Melchizedek priesthood requires a "
                             "figure who transcends the Levitical system -- one whose priesthood is eternal, "
                             "not hereditary, and whose single sacrifice is permanently effective."
            },
            {
                "source": "Acts 4:11; 1 Peter 2:4-7",
                "summary": "Peter identifies Jesus as the 'stone that the builders rejected' from "
                           "Psalm 118:22: 'This Jesus is the stone that was rejected by you, the builders, "
                           "which has become the cornerstone.'",
                "relevance": "The rejected-stone motif becomes central to early Christian theology: the "
                             "one whom the religious establishment rejected is the one YHWH chose as the "
                             "foundation of the new temple -- the messianic community."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 14:18-20", "note": "Melchizedek, king of Salem and priest of God Most High, blesses Abraham -- the original Melchizedek figure behind Ps 110:4", "type": "ot"},
            {"ref": "Matthew 22:41-46", "note": "Jesus uses Ps 110:1 to demonstrate the Messiah's divinity: 'If David calls him Lord, how is he his son?'", "type": "nt"},
            {"ref": "Acts 2:34-35", "note": "Peter at Pentecost: 'David did not ascend into the heavens, but he himself says, The Lord said to my Lord, Sit at my right hand'", "type": "nt"},
            {"ref": "Hebrews 5:6; 7:1-28", "note": "The Melchizedek priesthood of Christ -- eternal, non-Levitical, superior to Aaron", "type": "nt"},
            {"ref": "Matthew 21:42", "note": "Jesus quotes Ps 118:22-23: 'The stone that the builders rejected has become the cornerstone'", "type": "nt"},
            {"ref": "2 Samuel 7:12-16", "note": "The Davidic covenant that Ps 132 renews: 'Your throne shall be established forever'", "type": "ot"},
            {"ref": "1 Corinthians 15:25", "note": "'For he must reign until he has put all his enemies under his feet' -- echoing Ps 110:1", "type": "nt"},
            {"ref": "Ephesians 1:20", "note": "God 'seated him at his right hand in the heavenly places' -- the fulfillment of Ps 110:1 in Christ's ascension", "type": "nt"},
            {"ref": "Isaiah 52:13", "note": "'My servant shall be high (yarum) and lifted up (venissa) and exalted (vegavah me'od)' -- the Suffering Servant elevated to the throne-room position of Ps 110:1", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "The Son of Man brought before the Ancient of Days to receive dominion -- the divine council enthronement that Ps 110:1 declares as YHWH's decree", "type": "ot"},
            {"ref": "Psalm 2:6-7", "note": "'I have set my King on Zion... You are my Son' -- the royal installation psalm that Ps 110 intensifies with throne-sharing and eternal priesthood", "type": "ot"},
            {"ref": "Zechariah 6:12-13", "note": "'He shall sit and rule on his throne. And he shall be a priest on his throne' -- the priest-king figure of Ps 110:4 echoed in Zechariah's Branch", "type": "ot"},
            {"ref": "Revelation 3:21", "note": "'The one who conquers, I will grant him to sit with me on my throne, as I also conquered and sat down with my Father on his throne' -- the Ps 110:1 enthronement extended to believers", "type": "nt"},
            {"ref": "Hebrews 1:3, 13", "note": "'He sat down at the right hand of the Majesty on high... To which of the angels has he ever said, Sit at my right hand?' -- the author's argument that Ps 110:1 places Christ above all angels", "type": "nt"},
            {"ref": "Isaiah 63:1-6", "note": "YHWH treading the winepress alone -- the divine warrior who has no helpers, whose victory Ps 110:5-6 describes: 'He will shatter kings on the day of his wrath'", "type": "ot"}
        ],

        "divine_council_note": "Psalm 110 is THE divine council psalm -- the most explicit text in the "
                               "Psalter for the installation of a figure at YHWH's right hand in the "
                               "heavenly throne room. 'YHWH says to my Lord (ne'um YHWH la'adoni): Sit at "
                               "my right hand (shev limini)' (110:1). The ne'um ('oracle, decree') is "
                               "technical vocabulary for a divine pronouncement -- the same word used for "
                               "prophetic oracles throughout the Old Testament. YHWH issues a formal decree "
                               "to a figure David calls 'my Lord' -- someone superior to the king himself. "
                               "The invitation to 'sit at my right hand' is an invitation to share the "
                               "divine throne -- the supreme position in the divine council. No angel is "
                               "ever offered this position (Hebrews 1:13: 'To which of the angels has he "
                               "ever said, Sit at my right hand?'). This figure is unique in the council "
                               "-- he occupies a position above the angels, at YHWH's side, and rules until "
                               "all enemies become his footstool. The 'enemies' include the hostile spiritual "
                               "powers of the Deuteronomy 32 worldview -- the rebellious elohim and their "
                               "earthly agents. Psalm 110:4 adds the priesthood: 'You are a priest forever "
                               "after the order of Melchizedek.' This combines royal authority (sitting on "
                               "the throne) with priestly mediation (interceding between God and humanity) "
                               "in a single figure -- something the Mosaic law strictly separated (only "
                               "Levites could be priests, only Judahites could be kings). The Melchizedek "
                               "order predates and supersedes the Levitical order. The figure at YHWH's "
                               "right hand is the ultimate mediator between the divine council and humanity "
                               "-- the priest-king who bridges heaven and earth. Psalm 118's rejected stone "
                               "adds another dimension: the one YHWH chooses is the one humans reject. The "
                               "divine council's choice and human judgment are inverted. Psalm 132 grounds "
                               "the messianic hope in Zion: 'YHWH has chosen Zion; he has desired it for "
                               "his dwelling place. This is my resting place (menuchati) forever; here I "
                               "will dwell, for I have desired it' (132:13-14). Zion is where YHWH's "
                               "council authority touches the earth, and the Davidic king is the council's "
                               "earthly representative enthroned there.",

        "sections": [
            {
                "heading": "Key Hebrew Concepts: Tsedeq, Mishpat, and Shalom",
                "body": "Three Hebrew words appear repeatedly in the royal and messianic psalms "
                        "and are essential for understanding what kind of king the Psalter envisions:"
                        "<br><br>"
                        "<strong>Tsedeq / Tsedaqah</strong> (<em>righteousness</em>): This is not "
                        "merely moral goodness but 'right order' -- things being as they should be "
                        "according to YHWH's design. A righteous king establishes tsedeq by "
                        "aligning his kingdom with YHWH's cosmic order. When Psalm 132 says YHWH "
                        "will 'clothe her priests with righteousness' (132:9), it means they will "
                        "function as YHWH designed them to.<br><br>"
                        "<strong>Mishpat</strong> (<em>justice / judgment</em>): While tsedeq is "
                        "the standard, mishpat is the act of applying that standard -- rendering "
                        "just decisions, defending the weak, and correcting what is wrong. Psalm "
                        "72:1-2 asks God to give the king both: 'Give the king your justice "
                        "(mishpat), O God, and your righteousness (tsidqah) to the royal son.'<br><br>"
                        "<strong>Shalom</strong> (<em>peace</em>): This is not merely the absence "
                        "of war but comprehensive well-being -- wholeness, prosperity, harmony, "
                        "and right relationships at every level. When tsedeq and mishpat are "
                        "established, shalom is the result. Psalm 122:6 commands: 'Pray for the "
                        "peace (shalom) of Jerusalem.' The messianic hope is a kingdom where "
                        "these three -- righteousness, justice, and peace -- are perfectly realized."
            },
            {
                "heading": "Psalm 110: The Priest-King at YHWH's Right Hand",
                "body": "'A Psalm of David. The LORD says to my Lord (ne'um YHWH la'adoni): Sit at my "
                        "right hand (shev limini), until I make your enemies your footstool (hadom "
                        "leraglekha)' (110:1). David, under divine inspiration, reports a decree from "
                        "YHWH to a figure David calls 'my Lord' (adoni). The puzzle Jesus poses to the "
                        "Pharisees (Matt 22:44) rests on this: if the Messiah is merely David's descendant, "
                        "why does David call him 'Lord'? The answer requires a figure who is both human "
                        "(David's seed) and divine (David's Lord). 'YHWH sends forth from Zion your "
                        "mighty scepter. Rule in the midst of your enemies!' (110:2). The authority "
                        "proceeds from Zion -- the cosmic mountain, the meeting point of heaven and earth. "
                        "'Your people will offer themselves freely on the day of your power, in holy "
                        "garments; from the womb of the morning, the dew of your youth will be yours' "
                        "(110:3 -- a notoriously difficult verse, perhaps describing the Messiah's army "
                        "or his supernatural origin). Then the second decree: 'YHWH has sworn (nishba) "
                        "and will not change his mind (velo yinnachem): You are a priest (kohen) forever "
                        "(le'olam) after the order of Melchizedek (al-divrati Malkhi-Tsedeq)' (110:4). "
                        "The oath is irrevocable. The priesthood is eternal. The order is not Levitical "
                        "but Melchizedekian -- reaching back behind the Mosaic covenant to Genesis 14, "
                        "to the priest-king of Salem who blessed Abraham. 'The Lord is at your right "
                        "hand; he will shatter kings on the day of his wrath' (110:5). The Messiah "
                        "exercises divine warrior judgment. The psalm ends with a cryptic image: 'He "
                        "will drink from the brook by the way; therefore he will lift up his head' "
                        "(110:7) -- the victorious king refreshed by the water of YHWH's provision."
            },
            {
                "heading": "Psalm 118: The Rejected Stone and the Gate of Righteousness",
                "body": "Psalm 118 is the climax of the Egyptian Hallel (Pss 113-118), sung at Passover "
                        "-- the 'hymn' (hymnos) that Jesus and his disciples sang after the Last Supper "
                        "(Matt 26:30). The psalm begins with the thanksgiving formula: 'Oh give thanks "
                        "to YHWH, for he is good; for his steadfast love (chesed) endures forever!' "
                        "(118:1). It traces a personal deliverance: 'Out of my distress I called on "
                        "YHWH; YHWH answered me and set me free' (118:5). The confession of faith: 'It "
                        "is better to take refuge in YHWH than to trust in man. It is better to take "
                        "refuge in YHWH than to trust in princes' (118:8-9). The nations surrounded the "
                        "psalmist 'like bees... but in the name of YHWH I cut them off!' (118:12). Then "
                        "the approach to the Temple: 'Open to me the gates of righteousness (sha'arei "
                        "tsedeq), that I may enter through them and give thanks to YHWH. This is the "
                        "gate of YHWH; the righteous shall enter through it' (118:19-20). The messianic "
                        "climax: 'The stone (even) that the builders (habonim) rejected (ma'asu) has "
                        "become the cornerstone (rosh pinnah). This is YHWH's doing; it is marvelous in "
                        "our eyes' (118:22-23). Jesus applies this directly to himself: the religious "
                        "leaders (the 'builders') reject him, but YHWH makes him the foundation of the "
                        "new Temple (Matt 21:42; Acts 4:11; 1 Pet 2:7). The processional cry: 'Blessed "
                        "is he who comes in the name of YHWH! (barukh habba beshem YHWH)' (118:26) -- "
                        "the words the crowd shouted at Jesus' triumphal entry (Matt 21:9) and the words "
                        "Jesus says Jerusalem will speak when it finally recognizes him (Matt 23:39)."
            },
            {
                "heading": "Psalm 132: The Davidic Covenant Renewed at Zion",
                "body": "Psalm 132 is the last of the Songs of Ascents and the only royal psalm in the "
                        "collection. It renews the Davidic covenant in connection with Zion -- the place "
                        "where the ark found its permanent home. David's vow: 'I will not enter my house "
                        "or get into my bed, I will not give sleep to my eyes or slumber to my eyelids, "
                        "until I find a place (maqom) for YHWH, a dwelling place (mishkanot) for the "
                        "Mighty One of Jacob (Avir Ya'aqov)' (132:3-5). The ark is brought to Zion: 'Let "
                        "us go to his dwelling place; let us worship at his footstool!' (132:7). The "
                        "footstool (hadom raglav) is the ark of the covenant -- the earthly replica of "
                        "YHWH's heavenly throne. YHWH's response: 'YHWH swore (nishba) to David a sure "
                        "oath from which he will not turn back (lo yashuv): One of the sons of your body "
                        "(mipri vitnekha) I will set on your throne' (132:11). The oath is irrevocable: "
                        "the Davidic line will reign. The condition: 'If your sons keep my covenant and "
                        "my testimonies that I shall teach them, their sons also forever shall sit on "
                        "your throne' (132:12). Then YHWH's choice of Zion: 'YHWH has chosen Zion; he "
                        "has desired it for his dwelling place (moshav): This is my resting place "
                        "(menuchati) forever (la'ad); here I will dwell (eshev), for I have desired it' "
                        "(132:13-14). The double election -- of David and of Zion -- anchors the messianic "
                        "hope: 'There I will make a horn to sprout (atsmiyach qeren) for David; I have "
                        "prepared a lamp (ner) for my anointed (limshichi)' (132:17). The sprouting horn "
                        "is the messianic heir; the lamp is the enduring Davidic dynasty that will never "
                        "be extinguished."
            }
        ]
    },

    {
        "id": "ps-113-118-146-150",
        "ref": "Psalms 113-118, 146-150",
        "chapter_num": 3,
        "title": "The Hallel and Hallelujah Psalms -- Pure Praise and Cosmic Worship",
        "era": "psalms_book5",
        "type": "chapter",
        "themes": ["DC", "GLORY", "KING", "REVERSAL"],

        "synopsis": "The Hallel psalms (113-118, the 'Egyptian Hallel') and the final Hallelujah psalms "
                    "(146-150) form the Psalter's praise framework in Book V. The Egyptian Hallel was sung "
                    "at Passover, Weeks, Tabernacles, and Hanukkah -- it is the 'hymn' (hymnos) Jesus and "
                    "his disciples sang after the Last Supper (Matt 26:30). Psalm 113 opens with 'Praise "
                    "YAH! (halelu-Yah!)' and celebrates YHWH who 'raises the poor from the dust and lifts "
                    "the needy from the ash heap' (113:7). Psalm 114 recounts the Exodus with cosmic "
                    "imagery: 'The sea looked and fled; Jordan turned back' (114:3). Psalm 115 contrasts "
                    "the living YHWH with dead idols. Psalm 116 is personal thanksgiving for deliverance "
                    "from death. Psalm 117 -- the shortest chapter in the Bible -- commands 'all nations' "
                    "and 'all peoples' to praise YHWH. The final five Hallelujah psalms (146-150) build to "
                    "the Psalter's crescendo. Each opens and closes with 'Hallelujah!' The scope expands "
                    "from personal trust (146) to Zion's restoration (147) to cosmic praise (148) to the "
                    "warrior praise of Israel (149) to the ultimate command: 'Let everything that has "
                    "breath (neshamah) praise YHWH! Hallelujah!' (150:6). The Psalter ends not with "
                    "lament, not with theology, but with praise -- the purpose for which the council and "
                    "creation exist.",

        "key_verse": {
            "ref": "Psalm 150:6",
            "text": "Let everything that has breath praise the LORD! Praise the LORD!",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "halelu-Yah (Praise YAH! -- the shortened form of YHWH; the battle cry of worship that opens and closes the final psalms)",
            "Hallel (praise -- the name for the Pss 113-118 collection; the liturgical praise sung at the great festivals)",
            "neshamah (breath -- 'everything that has breath' in 150:6; the gift of life that obligates praise; cf. Gen 2:7, the breath YHWH gave to humanity)",
            "tehillah (praise -- from the same root as Tehillim, the Hebrew name for the Psalms; the entire Psalter culminates in this)",
            "kol-ha'ammim (all peoples -- the universal scope of praise in Ps 117; every nation commanded to praise YHWH)",
            "tof (tambourine/timbrel -- the instruments of praise in Ps 150; embodied, physical worship)",
            "shir chadash (new song -- the fresh praise called for in Ps 149:1; not repetition but continual newness)"
        ],

        "ane_backdrop": "Festival hymnody was central to ANE worship. The Babylonian akitu festival "
                        "included the chanting of the Enuma Elish, and Egyptian festivals featured "
                        "professional temple singers performing hymns to the gods. The Israelite Hallel "
                        "was distinctive in its participatory nature: the entire congregation sang the "
                        "refrains, not just professional Levitical musicians. The Passover Hallel "
                        "specifically was divided: Psalms 113-114 were sung before the meal, Psalms "
                        "115-118 after (Mishnah Pesachim 10:5-7). This means Jesus sang Psalm 118 -- "
                        "including 'The stone the builders rejected has become the cornerstone' and "
                        "'Blessed is he who comes in the name of YHWH' -- immediately before walking "
                        "to Gethsemane. The use of percussion, wind, and stringed instruments in Psalm "
                        "150 reflects archaeological evidence of Israelite musical culture: lyres, "
                        "harps, cymbals, and percussion have been found at multiple Israelite sites. "
                        "The universalism of Psalms 117 and 148 -- commanding all nations and all "
                        "creation to praise -- stands in contrast to most ANE hymnody, which addressed "
                        "specific national or local deities.",

        "second_temple": [
            {
                "source": "Matthew 26:30",
                "summary": "'And when they had sung a hymn (hymnesantes), they went out to the Mount "
                           "of Olives.' The 'hymn' was the second half of the Hallel (Pss 115-118).",
                "relevance": "Jesus sang the Hallel psalms -- including the rejected cornerstone and "
                             "'Blessed is he who comes in the name of YHWH' -- knowing he was about to "
                             "fulfill them. The Passover liturgy became the soundtrack of the Passion."
            },
            {
                "source": "Revelation 19:1-6",
                "summary": "'After this I heard what seemed to be the loud voice of a great multitude "
                           "in heaven, crying out, Hallelujah! Salvation and glory and power belong to "
                           "our God... Hallelujah! For the Lord our God the Almighty reigns!'",
                "relevance": "The 'Hallelujah' of Revelation 19 is the heavenly fulfillment of the "
                             "Psalter's Hallelujah chorus -- the divine council and the redeemed joining "
                             "in the cosmic praise that Psalms 146-150 anticipate."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 26:30", "note": "Jesus and the disciples sing the Hallel after the Last Supper -- Pss 115-118 as the soundtrack to Gethsemane", "type": "nt"},
            {"ref": "Romans 15:11", "note": "Paul quotes Ps 117:1: 'Praise the Lord, all you Gentiles, and let all the peoples extol him' -- the universal scope of worship", "type": "nt"},
            {"ref": "Revelation 19:1-6", "note": "The four-fold 'Hallelujah' of Revelation -- the heavenly fulfillment of the Psalter's praise", "type": "nt"},
            {"ref": "Exodus 15:1-21", "note": "The Song of the Sea -- the original 'hallelujah' after the Exodus that Ps 114 recapitulates", "type": "ot"},
            {"ref": "1 Chronicles 16:36", "note": "'Blessed be YHWH, the God of Israel, from everlasting to everlasting! Then all the people said, Amen! and praised YHWH' -- the doxology pattern the Hallel psalms follow", "type": "ot"},
            {"ref": "Revelation 5:11-14", "note": "'Worthy is the Lamb' -- every creature in heaven, on earth, under the earth, and in the sea joins in praise, fulfilling Ps 150:6", "type": "nt"}
        ],

        "divine_council_note": "The final Hallelujah psalms (146-150) represent the Psalter's vision of "
                               "the divine council in full worship mode. Psalm 148 is the critical text: "
                               "'Praise YHWH from the heavens (min-hashamayim); praise him in the heights "
                               "(bammeromim)! Praise him, all his angels (malakhav); praise him, all his "
                               "hosts (tseva'ov)! Praise him, sun and moon; praise him, all you shining "
                               "stars!' (148:1-3). The command to praise begins in the heavenly realm -- "
                               "the divine council itself is summoned to worship. The 'angels' (malakhim) "
                               "and 'hosts' (tseva'ot) are the council members; the sun, moon, and stars "
                               "are the astral beings that Manasseh wrongly worshipped but whose proper "
                               "function is to praise their Creator. 'Praise him, you highest heavens "
                               "(shemei hashamayim), and you waters above the heavens!' (148:4). Even the "
                               "cosmic architecture -- the heavens above the heavens, the primordial waters "
                               "-- is summoned to praise. 'Let them praise the name of YHWH! For he "
                               "commanded and they were created (nivra'u). And he established them forever "
                               "and ever; he gave a decree (choq) and it shall not pass away' (148:5-6). "
                               "The council members exist because YHWH commanded them into being. Their "
                               "existence is his decree. Psalm 148 then moves from heaven to earth: sea "
                               "creatures, fire and hail, snow and mist, mountains and hills, trees and "
                               "animals, kings and peoples, young and old -- all are commanded to praise. "
                               "The scope is total: the entire created order, from the highest angel to the "
                               "humblest creature, exists to praise YHWH. Psalm 150 brings the crescendo: "
                               "praise with trumpet, lute, harp, tambourine, strings, pipe, and cymbals. "
                               "'Let everything that has breath (kol haneshamah) praise YHWH! Hallelujah!' "
                               "(150:6). The neshamah is the breath of life given at creation (Gen 2:7). "
                               "Every being that received YHWH's breath owes him praise. The Psalter's final "
                               "word is not theology or lament but the purest imperative: praise. This is "
                               "the divine council's purpose. This is creation's purpose. This is the purpose "
                               "of the entire Psalter -- and of the redeemed community that sings it.",

        "sections": [
            {
                "heading": "Understanding 'Hallelujah' and 'Hallel' -- The Hebrew Behind the World's Most Famous Word",
                "body": "<strong>Hallelujah</strong> (<em>halelu-Yah</em>) is arguably the most "
                        "widely recognized Hebrew word on earth. It has been borrowed into virtually "
                        "every language and appears in worship music from Africa to Asia to the "
                        "Americas. But what does it actually mean?<br><br>"
                        "The word is a compound of two parts:<br>"
                        "<strong>Hallelu</strong> -- the imperative plural of the verb <em>hallal</em>, "
                        "meaning 'praise!' Specifically, <em>hallal</em> means to praise with "
                        "exuberant, vocal, public celebration -- not quiet meditation but loud, "
                        "joyful declaration. The imperative plural means this is a command to a "
                        "group: 'All of you -- praise!'<br>"
                        "<strong>Yah</strong> -- the shortened form of YHWH (<em>Yahweh</em>), "
                        "God's personal, covenantal name revealed to Moses at the burning bush "
                        "(Exodus 3:14-15). <em>Yah</em> is the most intimate form of the divine "
                        "name.<br><br>"
                        "So <strong>Hallelujah means: 'All of you -- praise YHWH!'</strong><br><br>"
                        "The related term <strong>Hallel</strong> (from the same root <em>hallal</em>) "
                        "means simply 'praise' and is used as a title for specific collections of "
                        "praise psalms in Jewish worship:<br>"
                        "- <strong>The Egyptian Hallel</strong> (Psalms 113-118): Sung at Passover, "
                        "Pentecost (Weeks/Shavuot), Tabernacles (Sukkot), and Hanukkah. At "
                        "Passover, Psalms 113-114 were sung before the meal and Psalms 115-118 "
                        "after. This is the 'hymn' (<em>hymnos</em>) that Jesus and his disciples "
                        "sang after the Last Supper (Matthew 26:30).<br>"
                        "- <strong>The Great Hallel</strong>: Usually identified as Psalm 136, with "
                        "its 26-fold refrain 'for his steadfast love endures forever.' Some "
                        "traditions extend it to Psalms 120-136.<br>"
                        "- <strong>The Final Hallel</strong> (Psalms 146-150): The five-psalm "
                        "doxological crescendo that closes the Psalter, each psalm framed by "
                        "Hallelujah.<br><br>"
                        "The Hebrew title of the entire Book of Psalms is <strong>Tehillim</strong> "
                        "-- 'Praises' (the plural of <em>tehillah</em>, from the same root as "
                        "<em>hallal</em>). The Psalter's Hebrew name tells us its identity: it is, "
                        "at its core, a book of praise -- and Hallelujah is its defining cry."
            },
            {
                "heading": "The Egyptian Hallel (Psalms 113-118): Festival Praise",
                "body": "The Egyptian Hallel is so named because Psalm 114 recounts the Exodus. Psalm "
                        "113 opens with the triple call: 'Praise YAH! (halelu-Yah!) Praise, O servants "
                        "of YHWH, praise the name of YHWH!' (113:1). YHWH is praised for his "
                        "transcendence ('He is high above all nations, and his glory above the heavens,' "
                        "113:4) and his condescension ('He raises the poor from the dust and lifts the "
                        "needy from the ash heap,' 113:7). Psalm 114 is a cosmic Exodus poem: 'When "
                        "Israel went out from Egypt... the sea looked (ra'ah) and fled (vayyanos); "
                        "Jordan turned back (yissov le'achor). The mountains skipped (raqedu) like "
                        "rams, the hills like lambs' (114:1, 3-4). Creation itself responds to YHWH's "
                        "redemptive presence. Psalm 115 contrasts YHWH with idols: 'Their idols are "
                        "silver and gold, the work of human hands. They have mouths, but do not speak; "
                        "eyes, but do not see' (115:4-5). Psalm 116 is personal thanksgiving: 'I love "
                        "YHWH, because he has heard my voice and my pleas for mercy' (116:1). 'Precious "
                        "(yaqar) in the sight of YHWH is the death of his saints (chasidav)' (116:15). "
                        "Psalm 117 -- just two verses, the shortest chapter in the Bible -- commands "
                        "universal praise: 'Praise YHWH, all nations (kol-goyim)! Extol him, all "
                        "peoples (kol-ha'ummim)!' (117:1). Paul quotes this in Romans 15:11 as proof "
                        "that the Gentiles were always intended to praise YHWH. Psalm 118 -- the Hallel "
                        "climax -- is treated separately under the messianic psalms."
            },
            {
                "heading": "The Final Hallelujah (Psalms 146-150): Everything That Has Breath",
                "body": "The final five psalms form a doxological crescendo. Each opens and closes with "
                        "'Hallelujah!' Psalm 146 is personal: 'Praise YHWH, O my soul! I will praise "
                        "YHWH as long as I live' (146:1-2). 'Put not your trust in princes (nedivim), "
                        "in a son of man (ben-adam), in whom there is no salvation (teshu'ah)' (146:3). "
                        "YHWH alone can be trusted -- he 'executes justice for the oppressed, gives food "
                        "to the hungry, sets the prisoners free, opens the eyes of the blind' (146:7-8). "
                        "Psalm 147 celebrates YHWH's restoration of Jerusalem: 'YHWH builds up Jerusalem; "
                        "he gathers the outcasts of Israel. He heals the brokenhearted (nishberei lev) "
                        "and binds up their wounds' (147:2-3). He 'determines the number of the stars "
                        "(kokhavim); he gives to all of them their names' (147:4) -- the same God who "
                        "counts the stars counts the tears of his people. Psalm 148 summons the entire "
                        "cosmos -- angels, hosts, sun, moon, stars, heavens, waters, sea creatures, "
                        "weather, mountains, trees, animals, kings, peoples, young, old -- to praise "
                        "YHWH. Psalm 149 gives Israel a 'new song' (shir chadash) and 'a two-edged "
                        "sword in their hands, to execute vengeance on the nations' (149:6-7) -- the "
                        "eschatological judgment where YHWH's people participate in his victory. Psalm "
                        "150 is the final crescendo: 'Praise God in his sanctuary (beqodsho); praise "
                        "him in his mighty heavens (birqia uzzo)!' (150:1). The sanctuary and the "
                        "heavens are joined -- earthly and heavenly worship unite. Every instrument is "
                        "deployed: trumpet (shofar), lute (nevel), harp (kinnor), tambourine (tof), "
                        "strings (minnim), pipe (ugav), and cymbals (tseltsellim, 150:3-5). The final "
                        "command: 'Let everything that has breath (kol haneshamah) praise YHWH! "
                        "Hallelujah!' (150:6). The Psalter ends with its purpose revealed: all breath, "
                        "all life, all creation exists to praise the God who made it. Hallelujah."
            }
        ]
    },

    {
        "id": "ps-119",
        "ref": "Psalm 119",
        "chapter_num": 4,
        "title": "Torah Psalm 119 -- The Longest Chapter: 176 Verses on God's Word",
        "era": "psalms_book5",
        "type": "chapter",
        "themes": ["LAW", "LOVE", "PROV"],

        "synopsis": "Psalm 119 is the longest chapter in the Bible -- 176 verses divided into 22 sections "
                    "of 8 verses each, one section for each letter of the Hebrew alphabet. It is the most "
                    "elaborate acrostic in scripture: every verse in a section begins with the same Hebrew "
                    "letter (aleph through tav). The psalm is a sustained meditation on YHWH's Torah (law, "
                    "instruction, word) using eight synonyms that rotate throughout: torah (law), edah "
                    "(testimony), piqqudim (precepts), chuqqim (statutes), mitsvah (commandment), mishpat "
                    "(judgment/ordinance), dabar (word), and imrah (saying/promise). The psalmist is not "
                    "celebrating legalism but expressing the delight of one who loves YHWH's revelation: "
                    "'Oh how I love your law! (torah) It is my meditation all the day' (119:97). 'Your "
                    "word is a lamp (ner) to my feet and a light (or) to my path' (119:105). The psalm "
                    "contains some of the most beloved devotional verses in scripture while sustaining an "
                    "astonishing literary feat across 176 verses. It is both a monument to the Torah and "
                    "a deeply personal prayer of one who depends on YHWH's word for survival.",

        "key_verse": {
            "ref": "Psalm 119:105",
            "text": "Your word is a lamp to my feet and a light to my path.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "torah (law/instruction -- the comprehensive term for YHWH's revealed will; not mere legislation but divine teaching)",
            "edah/edot (testimony/testimonies -- YHWH's covenant stipulations that testify to his character and demands)",
            "piqqudim (precepts -- YHWH's appointed charges; specific instructions requiring careful attention)",
            "chuqqim (statutes -- engraved, permanent decrees; laws carved in stone, unalterable)",
            "mitsvah/mitsvot (commandment/commandments -- direct orders from YHWH requiring obedience)",
            "mishpatim (judgments/ordinances -- YHWH's rulings and legal decisions; the case law of the covenant)",
            "dabar (word -- YHWH's spoken revelation; both the Torah text and the living divine speech)",
            "imrah (saying/promise -- YHWH's utterance; often emphasizing the promissory aspect of divine speech)"
        ],

        "ane_backdrop": "Acrostic compositions were known in the ANE but nothing approaches the scale of "
                        "Psalm 119. The Babylonian 'Theodicy' (c. 1000 BC) is an acrostic poem of 27 "
                        "stanzas, each beginning with successive cuneiform signs spelling the author's name "
                        "and title. Egyptian wisdom texts celebrated the 'Teaching' (sbayt) of the gods, "
                        "and Mesopotamian hymns praised the decrees (parsu) of the divine assembly. But the "
                        "Israelite Torah is distinctive: it is not hidden wisdom accessible only to priests "
                        "or scribes but public revelation given to the entire nation. The eight synonyms for "
                        "Torah in Psalm 119 may reflect the Mesopotamian practice of using multiple terms "
                        "for divine decrees (simtu, parsu, usurtu, etc.), but the psalmist personalizes "
                        "them: YHWH's law is 'my delight' (sha'ashu'ai, 119:24), 'my counselors' (119:24), "
                        "'my song' (119:54). The ANE parallel literature produces awe before divine law; "
                        "Psalm 119 produces intimacy -- the psalmist loves YHWH's word because through it "
                        "he knows YHWH himself.",

        "second_temple": [
            {
                "source": "Sirach 24:23",
                "summary": "Ben Sira identifies Wisdom with the Torah: 'All this is the book of the "
                           "covenant of the Most High God, the law that Moses commanded us.'",
                "relevance": "The Second Temple identification of Wisdom with Torah echoes Psalm 119's "
                             "celebration of Torah as the source of all understanding, delight, and life -- "
                             "not merely legal code but divine wisdom incarnate in text."
            },
            {
                "source": "Matthew 5:17-18",
                "summary": "Jesus declares: 'Do not think that I have come to abolish the Law or the "
                           "Prophets; I have not come to abolish them but to fulfill them. For truly, "
                           "I say to you, until heaven and earth pass away, not an iota, not a dot, will "
                           "pass from the Law.'",
                "relevance": "Jesus' affirmation of the Torah's permanence echoes Psalm 119's theology: "
                             "'Forever, O YHWH, your word is firmly fixed in the heavens' (119:89). The "
                             "Torah endures because it reflects the eternal character of its Author."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 1:1-2", "note": "'Blessed is the man... whose delight is in the law of YHWH, and on his law he meditates day and night' -- the Torah meditation that Ps 119 sustains for 176 verses", "type": "ot"},
            {"ref": "Psalm 19:7-11", "note": "'The law of YHWH is perfect, reviving the soul... More to be desired are they than gold' -- the shorter Torah psalm that Ps 119 expands into a magnum opus", "type": "ot"},
            {"ref": "Joshua 1:8", "note": "'This Book of the Law shall not depart from your mouth, but you shall meditate on it day and night' -- the command Ps 119 obeys", "type": "ot"},
            {"ref": "Matthew 5:17-18", "note": "Jesus affirms the Torah's permanence -- 'not an iota, not a dot, will pass from the Law'", "type": "nt"},
            {"ref": "Romans 7:22", "note": "'For I delight in the law of God, in my inner being' -- Paul echoes Ps 119:97", "type": "nt"},
            {"ref": "2 Timothy 3:16-17", "note": "'All Scripture is breathed out by God and profitable for teaching' -- the doctrine of Scripture that Ps 119 celebrates devotionally", "type": "nt"}
        ],

        "divine_council_note": "Psalm 119 connects to the divine council through its theology of YHWH's "
                               "word as heavenly decree. 'Forever, O YHWH, your word (dabar) is firmly "
                               "fixed (nitsav) in the heavens (bashamayim)' (119:89). The word is not "
                               "merely written on scrolls but 'established' (nitsav -- the same root used "
                               "for standing in the divine assembly, cf. 1 Kgs 22:19) in the heavens "
                               "themselves. YHWH's Torah has its origin in the heavenly throne room and "
                               "its permanence in the divine decree. 'Your faithfulness endures to all "
                               "generations; you have established the earth, and it stands fast' (119:90) "
                               "-- the same word that created and sustains the physical world is the Torah "
                               "given to Israel. The psalmist's love for Torah is therefore love for the "
                               "divine council's revealed will: 'Your testimonies are wonderful (pela'ot); "
                               "therefore my soul keeps them' (119:129). The pela'ot ('wonders') are the "
                               "same term used for YHWH's mighty acts in history and creation. Torah is "
                               "wondrous because it reveals the mind of the council's presiding King. 'The "
                               "unfolding (petach) of your words gives light (ya'ir); it gives understanding "
                               "(mevin) to the simple (peta'im)' (119:130). The 'opening' of YHWH's word "
                               "is revelation -- the divine council's decrees made accessible to humans. "
                               "The 22-section acrostic structure (aleph through tav, the first and last "
                               "letters of the Hebrew alphabet) suggests completeness: YHWH's word covers "
                               "everything from beginning to end, from aleph to tav -- or as Revelation "
                               "1:8 would later express it in Greek, from Alpha to Omega.",

        "sections": [
            {
                "heading": "What Is an Acrostic Psalm? Psalm 119 as the Supreme Example",
                "body": "An <strong>acrostic</strong> is a literary form in which the first letter "
                        "of each line (or section) follows a predetermined pattern -- typically "
                        "the order of the alphabet. Several psalms use this form (Pss 9-10, 25, "
                        "34, 37, 111, 112, 145), but Psalm 119 is the most elaborate acrostic in "
                        "the entire Bible.<br><br>"
                        "The Hebrew alphabet has 22 letters: aleph, bet, gimel, dalet, he, vav, "
                        "zayin, chet, tet, yod, kaf, lamed, mem, nun, samekh, ayin, pe, tsade, "
                        "qof, resh, shin, and tav. Psalm 119 devotes <strong>eight verses to "
                        "each letter</strong>, for a total of 176 verses (22 x 8). Within each "
                        "eight-verse section, every verse begins with the same Hebrew letter. So "
                        "verses 1-8 all begin with aleph, verses 9-16 all begin with bet, and so "
                        "on through the entire alphabet.<br><br>"
                        "This structure is invisible in English translation (since Hebrew and "
                        "English alphabets differ), which is why many English Bibles print the "
                        "Hebrew letter name at the start of each section (ALEPH, BETH, GIMEL, etc.) "
                        "to help readers see the pattern.<br><br>"
                        "The acrostic form accomplishes several things: (1) It aided memorization -- "
                        "knowing which letter comes next helped singers remember the text. (2) It "
                        "expressed <strong>completeness</strong> -- running from aleph to tav (the "
                        "first and last letters of the Hebrew alphabet) symbolically covers "
                        "everything from A to Z. The psalmist is saying: YHWH's Torah encompasses "
                        "the totality of existence. (3) It demonstrated extraordinary literary "
                        "skill -- sustaining a coherent theological meditation across 176 verses "
                        "while obeying a rigid alphabetic constraint is a feat of poetic mastery "
                        "unparalleled in the ancient world."
            },
            {
                "heading": "The Acrostic Structure and the Eight Synonyms (119:1-48, selected)",
                "body": "The psalm opens with the Aleph section: 'Blessed (ashrei) are those whose way "
                        "is blameless (temimei-darekh), who walk in the law (torah) of YHWH! Blessed "
                        "are those who keep his testimonies (edotav), who seek him with their whole "
                        "heart (bekhol-lev)' (119:1-2). The eight Torah synonyms appear immediately: "
                        "torah, edot, derakhim (ways), piqqudim, chuqqim, mitsvot, mishpatim, and "
                        "devarim. Each section rotates through these terms while meditating on a "
                        "different facet of the psalmist's relationship to YHWH's word. The Beth "
                        "section asks: 'How can a young man keep his way pure (yezakkeh)? By guarding "
                        "it according to your word (dabar)' (119:9). 'I have stored up your word "
                        "(imrah) in my heart (libbi), that I might not sin against you' (119:11). The "
                        "Gimel section prays: 'Open my eyes (gal einai), that I may behold wondrous "
                        "things (nifla'ot) out of your law (toratekha)' (119:18). The Daleth section "
                        "confesses: 'My soul clings (davqah) to the dust; give me life (chayyeni) "
                        "according to your word' (119:25). The He section pleads: 'Teach me (horeni), "
                        "O YHWH, the way of your statutes; and I will keep it to the end (eqev)' "
                        "(119:33). The Vav section trusts: 'I shall walk in a wide place (varechavah), "
                        "for I have sought your precepts' (119:45). Through every letter, the psalmist "
                        "returns to the same theme: YHWH's word is life, light, freedom, delight, and "
                        "the only foundation for faithful living."
            },
            {
                "heading": "The Heart of the Psalm: Delight, Dependence, and Eternity (119:89-176, selected)",
                "body": "The Lamed section reaches the theological summit: 'Forever (le'olam), O YHWH, "
                        "your word (devarekha) is firmly fixed (nitsav) in the heavens (bashamayim)' "
                        "(119:89). YHWH's word is not earthly in origin; it is established in the "
                        "heavenly realm -- decreed in the council and permanent as the cosmos. 'Your "
                        "faithfulness (emunatekha) endures to all generations; you have established the "
                        "earth, and it stands fast' (119:90). The same word that holds the earth in "
                        "place is the Torah the psalmist meditates on. The Mem section is the most "
                        "personal: 'Oh how I love your law (toratekha)! It is my meditation (sichati) "
                        "all the day' (119:97). 'How sweet are your words (imratekha) to my taste "
                        "(lechikki), sweeter than honey (midevash) to my mouth!' (119:103). The Nun "
                        "section contains the most famous verse: 'Your word (devarekha) is a lamp (ner) "
                        "to my feet and a light (or) to my path' (119:105). The Ayin section confesses "
                        "servanthood: 'I am your servant (avdekha); give me understanding (havineni), "
                        "that I may know your testimonies' (119:125). The Tsade section declares: "
                        "'Righteous (tsaddiq) are you, O YHWH, and right (yashar) are your rules "
                        "(mishpatekha)' (119:137). The Shin section cries: 'My lips will pour forth "
                        "praise (tehillah), for you teach me your statutes' (119:171). The final Tav "
                        "section closes with a humble confession: 'I have gone astray like a lost "
                        "sheep (kesh ovad); seek your servant (avdekha), for I do not forget your "
                        "commandments (mitsvotekha)' (119:176). The psalm ends not with triumphant "
                        "mastery of the law but with the confession of a wandering sheep who depends "
                        "entirely on YHWH to seek him out -- a fitting bridge to the Good Shepherd "
                        "who leaves the ninety-nine to find the one (Luke 15:4)."
            }
        ]
    },

    {
        "id": "ps-139",
        "ref": "Psalm 139",
        "chapter_num": 5,
        "title": "Psalm 139 -- The Inescapable God: Omniscience, Omnipresence, and the Womb",
        "era": "psalms_book5",
        "type": "chapter",
        "themes": ["DC", "SPIRIT", "GLORY"],

        "synopsis": "Psalm 139 is one of the most profound theological poems in scripture -- a meditation "
                    "on YHWH's exhaustive knowledge, inescapable presence, and intimate creative power. "
                    "David opens with the realization that YHWH knows him completely: 'O YHWH, you have "
                    "searched me (chaqartani) and known me (vatted'a)! You know when I sit down and when "
                    "I rise up; you discern my thoughts from afar' (139:1-2). He explores YHWH's presence "
                    "in the most extreme locations: 'Where shall I go from your Spirit (ruchakha)? Or "
                    "where shall I flee from your presence (panekha)? If I ascend to heaven (shamayim), "
                    "you are there! If I make my bed in Sheol (she'ol), you are there!' (139:7-8). He "
                    "marvels at YHWH's creative work in the womb: 'For you formed my inward parts "
                    "(khilyotai); you knitted me together (tesukkeni) in my mother's womb. I praise you, "
                    "for I am fearfully and wonderfully made (nora'ot nifle'ti). Wonderful are your "
                    "works; my soul knows it very well' (139:13-14). YHWH's knowledge extends even to "
                    "the unformed embryo: 'Your eyes saw my unformed substance (golmi); in your book "
                    "were written, every one of them, the days that were formed for me, when as yet there "
                    "were none of them' (139:16). The psalm closes with a prayer for divine examination: "
                    "'Search me, O God, and know my heart! Try me and know my thoughts! And see if there "
                    "be any grievous way in me, and lead me in the way everlasting (derekh olam)!' "
                    "(139:23-24).",

        "key_verse": {
            "ref": "Psalm 139:13-14",
            "text": "For you formed my inward parts; you knitted me together in my mother's womb. I praise you, for I am fearfully and wonderfully made. Wonderful are your works; my soul knows it very well.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "chaqar (to search/probe -- YHWH's exhaustive examination of the human person; he knows everything about us)",
            "ruach (Spirit -- YHWH's Spirit from which no one can flee; the omnipresent divine presence)",
            "panim (face/presence -- YHWH's face from which no one can hide; the personal aspect of divine omnipresence)",
            "khilyot (inward parts/kidneys -- the seat of emotion and conscience in Hebrew anthropology; YHWH formed even these)",
            "sakak (to knit together/weave -- the creative act of forming a human being in the womb; intimate, artisanal craftsmanship)",
            "nora'ot nifle'ti (fearfully and wonderfully made -- lit. 'I am awesome-ly, wonderfully made'; the human person as a divine masterwork)",
            "golem (unformed substance/embryo -- the only biblical use of this word; the not-yet-formed life that YHWH already knows)",
            "derekh olam (the way everlasting -- the path of eternal life; the ultimate destination of the examined life)"
        ],

        "ane_backdrop": "The concept of an all-knowing, all-present deity was rare in ANE religion. Most "
                        "ANE gods were territorial -- Marduk in Babylon, Ashur in Assyria, Baal in Canaan "
                        "-- and their knowledge and power were limited to their domains. The Egyptian 'Hymn "
                        "to Amun-Re' attributes broad knowledge to the sun god, but within the framework "
                        "of his daily journey across the sky. The Babylonian Shamash (sun god), as the god "
                        "of justice, was credited with seeing all human deeds during daylight, but darkness "
                        "limited his vision. Psalm 139 radically transcends these limitations: YHWH's "
                        "knowledge is not limited to daylight ('even the darkness is not dark to you; the "
                        "night is bright as the day,' 139:12), his presence is not limited to any territory "
                        "(heaven, Sheol, the far side of the sea -- he is everywhere), and his creative "
                        "involvement extends to the womb itself. The word golem (139:16), used nowhere else "
                        "in the Bible, means 'unformed mass, embryo' -- YHWH knows and plans even before "
                        "a human being takes shape. Later Jewish tradition (the Talmud, medieval folklore) "
                        "would develop the golem concept into the idea of an artificial being brought to "
                        "life, but in Psalm 139 it refers to the natural embryo in YHWH's creative process.",

        "second_temple": [
            {
                "source": "Romans 8:38-39",
                "summary": "Paul writes: 'Neither death nor life, nor angels nor rulers, nor things present "
                           "nor things to come, nor powers, nor height nor depth, nor anything else in all "
                           "creation, will be able to separate us from the love of God.'",
                "relevance": "Paul's comprehensive list of powers that cannot separate the believer from "
                             "God echoes Psalm 139's exploration of every domain -- heaven, Sheol, the "
                             "uttermost sea -- where YHWH's presence is inescapable. What Psalm 139 "
                             "discovers as theological truth, Romans 8 applies as pastoral assurance."
            },
            {
                "source": "Acts 17:27-28",
                "summary": "Paul at Athens: 'He is actually not far from each one of us, for in him we "
                           "live and move and have our being.'",
                "relevance": "Paul's Mars Hill declaration is the Psalm 139 theology applied to a Gentile "
                             "audience: YHWH is not far from anyone because his presence permeates all "
                             "creation."
            }
        ],

        "cross_refs": [
            {"ref": "Jeremiah 23:23-24", "note": "'Am I a God at hand, declares YHWH, and not a God far away? ... Do I not fill heaven and earth?' -- the prophetic statement of Ps 139's theology", "type": "ot"},
            {"ref": "Romans 8:38-39", "note": "Nothing in all creation can separate from God's love -- the NT application of Ps 139's omnipresence", "type": "nt"},
            {"ref": "Acts 17:27-28", "note": "'In him we live and move and have our being' -- Paul's Athenian sermon echoing Ps 139", "type": "nt"},
            {"ref": "Job 10:8-12", "note": "'Your hands fashioned and made me... You clothed me with skin and flesh, and knit me together with bones and sinews' -- Job's parallel to Ps 139:13-16", "type": "ot"},
            {"ref": "Jeremiah 1:5", "note": "'Before I formed you in the womb I knew you, and before you were born I consecrated you' -- YHWH's prenatal knowledge paralleling Ps 139:13-16", "type": "ot"},
            {"ref": "Matthew 10:30", "note": "'Even the hairs of your head are all numbered' -- Jesus' statement of the exhaustive divine knowledge Ps 139 celebrates", "type": "nt"},
            {"ref": "Hebrews 4:13", "note": "'No creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account' -- the divine scrutiny of Ps 139:1-4", "type": "nt"}
        ],

        "divine_council_note": "Psalm 139 reveals the attributes that distinguish YHWH from every other "
                               "member of the divine council. The elohim of Psalm 82 -- the sons of God "
                               "allotted over the nations -- are territorial and limited in knowledge. They "
                               "govern their assigned domains but their authority has boundaries. YHWH, by "
                               "contrast, is inescapable: 'Where shall I go from your Spirit? Or where shall "
                               "I flee from your presence?' (139:7). The answer: nowhere. Not heaven (the "
                               "council's own meeting place), not Sheol (the realm of the dead, where the "
                               "rephaim dwell), not the wings of the morning (the far eastern horizon), not "
                               "the uttermost parts of the sea (the far west). YHWH's presence fills every "
                               "domain -- including the domains allotted to other elohim. This is the "
                               "theological foundation for the Deuteronomy 32:8-9 hierarchy: YHWH is not "
                               "one god among equals. He is the God who fills all space, knows all thoughts, "
                               "and creates all life. The other elohim exist within his omnipresence. The "
                               "creative act described in 139:13-16 is distinctly YHWH's: 'You formed my "
                               "inward parts; you knitted me together in my mother's womb.' The creation of "
                               "individual human beings is not delegated to subordinate powers but is YHWH's "
                               "personal, intimate work. He knows the golem (unformed substance) before it "
                               "takes shape. He writes the days in his book before they exist. This level of "
                               "knowledge and creative involvement is unique to the council's presiding King. "
                               "The imprecatory section (139:19-22 -- 'Oh that you would slay the wicked, O "
                               "God!') is the psalmist's alignment with the council's purposes: hatred of evil "
                               "flows from intimate knowledge of the Holy One. The closing prayer (139:23-24) "
                               "invites the same searching knowledge that opened the psalm: 'Search me, O God, "
                               "and know my heart!' The one who cannot escape YHWH's gaze chooses to submit to "
                               "it, asking to be led in 'the way everlasting' (derekh olam) -- the eternal path "
                               "that leads from the divine council's scrutiny to the divine council's blessing.",

        "sections": [
            {
                "heading": "The Imprecatory Section: Honest Prayer or Troubling Rage? (139:19-22)",
                "body": "Readers of Psalm 139 are often startled when the psalm's tone shifts "
                        "abruptly from tender wonder to fierce hostility: 'Oh that you would slay "
                        "the wicked, O God! O men of blood, depart from me!' (139:19). 'Do I not "
                        "hate those who hate you, O YHWH?... I count them my enemies' (139:21-22). "
                        "How does this prayer for the death of enemies fit within a psalm about "
                        "God's intimate, loving knowledge?<br><br>"
                        "These verses are an example of <strong>imprecatory prayer</strong> -- "
                        "prayer that calls down divine judgment on the wicked (from the Latin "
                        "<em>imprecari</em>, 'to invoke evil upon'). Imprecatory passages appear "
                        "throughout the Psalter (Pss 35, 58, 69, 83, 109, 137), and they raise "
                        "genuine questions for readers. Several observations help:<br><br>"
                        "<strong>First</strong>, the imprecation flows directly from the theology. "
                        "If YHWH's intimate knowledge of the psalmist (139:1-16) means he is "
                        "perfectly good and perfectly just, then the wicked who oppose him are "
                        "opposing ultimate goodness. The psalmist's hatred of the wicked is not "
                        "personal grudge but moral alignment with YHWH's own character.<br><br>"
                        "<strong>Second</strong>, the psalmist does not take action himself. He "
                        "prays for God to act: 'Oh that <em>you</em> would slay the wicked.' "
                        "This is the surrender of vengeance to the one qualified to execute it "
                        "justly.<br><br>"
                        "<strong>Third</strong>, notice what immediately follows the imprecation: "
                        "'Search me, O God, and know my heart! ... And see if there be any grievous "
                        "way in me' (139:23-24). The psalmist who has just expressed hatred for "
                        "evil turns the searchlight on himself. He asks YHWH to examine <em>him</em> "
                        "for wickedness. This is not self-righteous fury but humble, vulnerable "
                        "honesty: 'I hate evil -- and I know I might harbor it myself. Search me.'"
            },
            {
                "heading": "The Inescapable Knowledge and Presence (139:1-12)",
                "body": "'O YHWH, you have searched me (chaqartani) and known me (vatted'a)!' (139:1). "
                        "The verb chaqar means to probe, explore, search out thoroughly -- the same word "
                        "used for mining precious metals from deep in the earth (Job 28:3). YHWH's "
                        "knowledge of the psalmist is that thorough. 'You know when I sit down and when "
                        "I rise up; you discern (banta) my thoughts (re'i) from afar' (139:2). YHWH "
                        "reads thoughts at a distance -- no proximity is needed. 'You search out "
                        "(zerita) my path and my lying down, and are acquainted (hiskanta) with all my "
                        "ways' (139:3). 'Even before a word is on my tongue, behold, O YHWH, you know "
                        "it altogether (kullahh)' (139:4). YHWH knows what we will say before we say it. "
                        "'You hem me in (tsartani), behind and before, and lay your hand upon me' "
                        "(139:5). The divine knowledge is not distant surveillance but intimate embrace. "
                        "'Such knowledge is too wonderful (peli'ah) for me; it is high (nisgavah); I "
                        "cannot attain it' (139:6). The psalmist is overwhelmed. Then the exploration "
                        "of omnipresence: 'Where shall I go from your Spirit (ruchakha)? Or where shall "
                        "I flee from your presence (panekha)?' (139:7). Heaven? 'You are there.' Sheol? "
                        "'You are there.' The wings of the morning? 'Even there your hand shall lead me, "
                        "and your right hand shall hold me' (139:10). Darkness? 'Even the darkness is "
                        "not dark to you; the night is bright as the day, for darkness is as light with "
                        "you' (139:12). There is no place, no time, no condition where YHWH is absent."
            },
            {
                "heading": "The Creator in the Womb and the Way Everlasting (139:13-24)",
                "body": "'For you formed (qanita) my inward parts (khilyotai); you knitted me together "
                        "(tesukkeni) in my mother's womb (beten immi)' (139:13). The verb qanah can mean "
                        "'to create, to acquire, to form' -- the same verb used of YHWH in Genesis 14:19 "
                        "(Melchizedek's blessing: 'maker of heaven and earth'). The verb sakak means 'to "
                        "weave, to knit, to intertwine' -- the image of YHWH as a weaver, personally "
                        "crafting each human being. 'I praise you (odekha), for I am fearfully and "
                        "wonderfully made (nora'ot nifle'ti)' (139:14). The adverb nora'ot ('fearfully, "
                        "awesomely') derives from yare ('to fear') -- the same root as the 'fear of YHWH.' "
                        "The human being is awe-inspiring because the Creator is awe-inspiring. 'My frame "
                        "(otsmi) was not hidden from you, when I was being made in secret (basater), "
                        "intricately woven (ruqqamti) in the depths of the earth (betachtiyyot arets)' "
                        "(139:15). The 'depths of the earth' is metaphorical for the hiddenness of the "
                        "womb -- the unseen place where YHWH creates. The verb ruqqam ('to embroider, to "
                        "weave in color') suggests that YHWH creates with the artistry of a master "
                        "embroiderer. 'Your eyes saw my unformed substance (golmi); in your book (sifrekha) "
                        "were written, every one of them, the days (yamim) that were formed for me, when "
                        "as yet there were none of them' (139:16). YHWH writes the days of a life before "
                        "the life begins. The 'book' (sefer) is the divine register -- the heavenly record "
                        "of each person's appointed days. After the imprecatory appeal (139:19-22), the "
                        "psalm closes with extraordinary vulnerability: 'Search me (choqreni), O God, and "
                        "know my heart (levavi)! Try me (bechaneni) and know my thoughts (sar'appai)! And "
                        "see if there be any grievous way (derekh-otsev) in me, and lead me (uncheneni) in "
                        "the way everlasting (derekh olam)!' (139:23-24). The psalmist who began by "
                        "declaring YHWH's searching knowledge now invites it. The God who knows everything "
                        "is asked to lead in the derekh olam -- the eternal way, the path that leads "
                        "beyond death into the everlasting presence of the one from whom there is no escape "
                        "and no desire to escape."
            }
        ]
    }
]
