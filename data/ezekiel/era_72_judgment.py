"""
era_72_judgment.py -- Judgment Oracles (Ezekiel 12-24)

The central judgment section of Ezekiel: symbolic acts, parables, allegories,
and disputations that build the case for Jerusalem's destruction. The extended
allegories of chapters 16 and 23 (Jerusalem as an unfaithful wife) are among
the most graphic in scripture. The theology of individual responsibility
(chapter 18) represents a major development: "The soul who sins shall die.
The son shall not suffer for the iniquity of the father." The section climaxes
with the death of Ezekiel's wife (24:15-27) on the very day the siege of
Jerusalem begins -- the prophet is forbidden to mourn, just as the people will
be too stunned to mourn when the temple falls.
"""

CHAPTERS = [
    {
        "id": "ezek-12-15",
        "ref": "Ezekiel 12-15",
        "chapter_num": 12,
        "title": "Sign Acts and False Prophets",
        "era": "ezekiel_judgment",
        "type": "chapter",
        "themes": ["EXILE", "RIV"],

        "synopsis": "Chapter 12: Ezekiel enacts the exile -- packing his belongings and digging through "
                    "the wall at night 'as an exile's baggage' (12:4). This specifically prefigures "
                    "Zedekiah's attempted escape (12:12-13; cf. 2 Kings 25:4-7). Chapter 13: YHWH "
                    "condemns the false prophets who 'prophesy out of their own hearts' (13:2) and "
                    "the women who 'sew magic bands upon all wrists' (13:18) -- practicing sorcery in "
                    "YHWH's name. Chapter 14: Even if Noah, Daniel, and Job were in the land, 'they "
                    "would deliver but their own lives by their righteousness' (14:14) -- no intercessor "
                    "can avert the judgment. Chapter 15: Jerusalem is a useless vine -- good for nothing "
                    "but burning.",

        "key_verse": {
            "ref": "Ezekiel 14:14",
            "text": "Even if these three men, Noah, Daniel, and Job, were in it, they would deliver but their own lives by their righteousness, declares the Lord GOD.",
            "translation": "ESV"
        },

        "original_terms": [
            "golah (exile/exiles -- the condition Ezekiel enacts and the community he addresses)",
            "nevi'ei sheqer (false prophets -- those who prophesy from their own imagination, without council access)",
            "tafal (whitewash -- the false prophets' covering of weak walls with plaster, hiding structural failure)",
            "tsedaqah (righteousness -- even the righteousness of the most famous intercessors cannot save the land)"
        ],

        "ane_backdrop": "The practice of prophets and diviners giving favorable oracles for payment was "
                        "widespread in the ANE. The Mari prophets sometimes delivered optimistic messages "
                        "to secure royal favor. Ezekiel's condemnation of false prophets (chapter 13) "
                        "targets this precise dynamic: those who 'whitewash' (tafal) with false peace "
                        "oracles. The magical bands and veils of 13:18-21 suggest a form of sympathetic "
                        "magic -- possibly binding or loosing spiritual forces for hire.",

        "second_temple": [
            {
                "source": "Matthew 7:15",
                "summary": "Jesus warns of 'false prophets who come in sheep's clothing but "
                           "inwardly are ravenous wolves.'",
                "relevance": "Jesus' false-prophet warnings build on the Ezekielian tradition of "
                             "prophets who speak 'peace' without divine authorization."
            }
        ],

        "cross_refs": [
            {"ref": "2 Kings 25:4-7", "note": "Zedekiah's escape and capture -- the historical fulfillment of Ezekiel's sign act (12:12-13)", "type": "ot"},
            {"ref": "Jeremiah 23:16-22", "note": "Jeremiah's parallel condemnation of false prophets -- they have not stood in the council", "type": "ot"},
            {"ref": "Genesis 6-9; Job 1-2", "note": "Noah and Job as exemplary righteous men (14:14) -- yet even they cannot save the land", "type": "ot"},
            {"ref": "Matthew 7:15", "note": "Jesus' false prophet warnings in the Ezekielian tradition", "type": "nt"}
        ],

        "divine_council_note": "The false prophets of chapter 13 have not received their message from the "
                               "divine council: they 'prophesy out of their own hearts (libbam)' (13:2) and "
                               "'follow their own spirit (ruach) and have seen nothing' (13:3). This echoes "
                               "Jeremiah 23:18-22: they have not stood in the sod of YHWH. Their 'whitewash' "
                               "(tafal) covers structural failure with superficial plaster. The invocation "
                               "of Noah, Daniel, and Job (14:14) is significant: these are the greatest "
                               "intercessors in biblical tradition, yet even their righteousness is insufficient "
                               "to change the council's decree. The judgment is irrevocable.",

        "sections": [
            {
                "heading": "Exile Enacted and Zedekiah's Flight Prefigured (12:1-28)",
                "body": "Ezekiel is commanded to 'prepare for yourself an exile's baggage (kelei golah) "
                        "and go into exile by day in their sight' (12:3). At evening, he digs through the "
                        "wall and carries his baggage 'in the dark' with face covered (12:6-7). YHWH "
                        "interprets: 'This oracle concerns the prince (nasi) in Jerusalem' -- Zedekiah "
                        "will attempt to flee 'in the dark' through a breach in the wall, but 'I will "
                        "spread my net over him, and he shall be taken in my snare' (12:13). He will be "
                        "brought to Babylon 'but he shall not see it' (12:13) -- because his eyes will "
                        "be put out. The specificity of the prediction is remarkable."
            },
            {
                "heading": "False Prophets and Sorcery Condemned (13:1-23)",
                "body": "'Woe to the foolish prophets who follow their own spirit and have seen nothing!' "
                        "(13:3). They are 'like jackals among ruins' (13:4) -- scavengers who profit "
                        "from destruction rather than preventing it. Their oracles are 'whitewash' (tafal): "
                        "'when the people build a wall, these prophets smear it with whitewash' (13:10). "
                        "The wall will collapse: 'I will make a stormy wind break out in my wrath... "
                        "and the wall shall fall' (13:13-14). The false prophetesses 'sew magic bands "
                        "(kesatot) upon all wrists and make veils (mispachot) for the heads of persons "
                        "of every stature, in the hunt for souls' (13:18). These practices are magical "
                        "manipulation -- 'putting to death souls who should not die and keeping alive "
                        "souls who should not live' (13:19)."
            },
            {
                "heading": "Noah, Daniel, and Job Cannot Save (14:1-23)",
                "body": "Elders come to inquire of YHWH, but YHWH sees their hearts: 'These men have "
                        "taken their idols into their hearts (gilluleihem el-libbam)' (14:3). YHWH will "
                        "not be inquired of by idolaters. Then the hypothetical: if a land sins against "
                        "YHWH, 'even if these three men, Noah, Daniel, and Job, were in it, they would "
                        "deliver but their own lives (nafshom) by their righteousness' (14:14). The "
                        "invocation of the three most famous righteous men underscores the finality of "
                        "the decree. YHWH sends his 'four disastrous acts of judgment' (arba shephatai "
                        "hara'ot): sword, famine, wild beasts, pestilence (14:21) -- the four horsemen "
                        "of the covenant curses (cf. Lev 26:22-26)."
            }
        ]
    },

    {
        "id": "ezek-16-18",
        "ref": "Ezekiel 16, 18",
        "chapter_num": 16,
        "title": "Jerusalem's Story and Individual Responsibility",
        "era": "ezekiel_judgment",
        "type": "chapter",
        "themes": ["COV", "RIV", "WOMEN", "BLOOD"],

        "synopsis": "Chapter 16 is the longest chapter in Ezekiel and one of the most graphic in "
                    "scripture: an extended allegory of Jerusalem as an abandoned infant whom YHWH "
                    "found, raised, adorned, and married -- only to have her become an adulterous "
                    "wife who 'played the whore' with every passing nation (16:15). 'You trusted in "
                    "your beauty and played the whore because of your renown' (16:15). Yet the chapter "
                    "ends with restoration: 'I will establish my covenant with you, and you shall know "
                    "that I am YHWH' (16:62). Chapter 18 addresses individual moral responsibility: "
                    "'The soul who sins shall die' (18:4, 20) -- challenging the exilic proverb 'The "
                    "fathers have eaten sour grapes, and the children's teeth are set on edge' (18:2). "
                    "Each generation is responsible for its own actions.",

        "key_verse": {
            "ref": "Ezekiel 18:4",
            "text": "Behold, all souls are mine; the soul of the father as well as the soul of the son is mine: the soul who sins shall die.",
            "translation": "ESV"
        },

        "original_terms": [
            "zanah (to commit adultery/prostitution -- the governing metaphor for Jerusalem's infidelity in chapter 16)",
            "nefesh (soul/life -- the subject of the individual responsibility declaration in chapter 18)",
            "tsedaqah (righteousness -- demonstrated by just behavior: feeding the hungry, clothing the naked, lending without interest)",
            "teshuvah (repentance/return -- 'Turn and live!' 18:32)"
        ],

        "ane_backdrop": "The foundling-wife allegory draws on ANE legal traditions regarding adoption, "
                        "marriage, and adultery. Mesopotamian law codes (Hammurabi, Middle Assyrian Laws) "
                        "specified severe penalties for adultery. The description of Jerusalem's foreign "
                        "alliances as 'prostitution' reflects the ANE treaty-making vocabulary where "
                        "covenant-making involved quasi-marital commitment to the suzerain. The concept "
                        "of corporate vs. individual responsibility was debated throughout the ANE -- "
                        "Ezekiel's emphasis on individual responsibility represents a significant "
                        "theological development.",

        "second_temple": [
            {
                "source": "Romans 6:23",
                "summary": "'The wages of sin is death' echoes Ezekiel 18:4 ('the soul who sins "
                           "shall die').",
                "relevance": "Paul's foundational statement on sin and death draws on Ezekiel's "
                             "theology of individual moral responsibility."
            },
            {
                "source": "Ezekiel 18:23, 32",
                "summary": "'Have I any pleasure in the death of the wicked?... Turn back and live!'",
                "relevance": "YHWH's desire for repentance rather than death anticipates the NT "
                             "emphasis on divine mercy (2 Peter 3:9)."
            }
        ],

        "cross_refs": [
            {"ref": "Hosea 1-3", "note": "Hosea's marriage allegory -- the same unfaithful-wife theology as Ezekiel 16", "type": "ot"},
            {"ref": "Jeremiah 2-3", "note": "Jeremiah's covenant lawsuit using the adultery metaphor -- parallel to Ezekiel 16", "type": "ot"},
            {"ref": "Romans 6:23", "note": "'The wages of sin is death' -- the NT echo of Ezekiel 18:4", "type": "nt"},
            {"ref": "2 Peter 3:9", "note": "God 'not wishing that any should perish' -- the NT development of Ezekiel 18:23, 32", "type": "nt"},
            {"ref": "Deuteronomy 24:16", "note": "'Fathers shall not be put to death because of their children' -- Torah basis for Ezekiel 18", "type": "ot"}
        ],

        "divine_council_note": "The individual responsibility theology of chapter 18 has divine council "
                               "implications. The council's judgment is not arbitrary or inherited -- each "
                               "person stands before YHWH on their own merits. 'All souls are mine' (18:4) "
                               "asserts YHWH's direct jurisdiction over every individual. The invitation "
                               "'Turn back and live!' (18:32) reveals the council's heart: YHWH 'takes no "
                               "pleasure in the death of the wicked' (18:23). The council decrees judgment "
                               "because of sin, not because of desire for destruction.",

        "sections": [
            {
                "heading": "The Foundling-Wife Allegory (16:1-34)",
                "body": "YHWH tells Jerusalem's story as a parable. Origin: 'Your origin and your birth "
                        "are of the land of the Canaanites. Your father was an Amorite and your mother "
                        "a Hittite' (16:3). At birth: 'Your navel cord was not cut, nor were you washed "
                        "with water to cleanse you... you were cast out on the open field, for you were "
                        "abhorred, on the day that you were born' (16:4-5). YHWH found her: 'I passed "
                        "by you and saw you wallowing in your blood... I said to you in your blood, \"Live!\"' "
                        "(16:6). He raised her, and when she was of age: 'I spread the corner of my "
                        "garment over you and covered your nakedness; I made my vow to you and entered "
                        "into a covenant with you' (16:8). He adorned her with gold, silver, fine linen, "
                        "embroidered cloth (16:10-13). 'And your renown went forth among the nations "
                        "because of your beauty' (16:14). But: 'You trusted in your beauty and played "
                        "the whore because of your renown, and you lavished your whorings on any "
                        "passerby' (16:15)."
            },
            {
                "heading": "Worse Than Sodom and Samaria (16:44-63)",
                "body": "The allegory reaches its climax: Jerusalem is worse than her 'sisters' Sodom "
                        "and Samaria. 'Your elder sister is Samaria... and your younger sister is Sodom' "
                        "(16:46). Sodom's sin: 'She and her daughters had pride, excess of food, and "
                        "prosperous ease, but did not aid the poor and needy' (16:49). Jerusalem's sins "
                        "exceed both. Yet YHWH promises restoration: 'I will restore their fortunes, "
                        "the fortunes of Sodom... and the fortunes of Samaria... and I will restore your "
                        "own fortunes in their midst' (16:53). The covenant will be re-established: "
                        "'I will establish my everlasting covenant (berit olam) with you' (16:60). 'Then "
                        "you will remember your ways and be ashamed' (16:61)."
            },
            {
                "heading": "The Soul Who Sins Shall Die (18:1-32)",
                "body": "Chapter 18 challenges the exile's bitter proverb: 'The fathers have eaten sour "
                        "grapes (boser), and the children's teeth are set on edge (tiqhenah)' (18:2) -- "
                        "the complaint that the exile generation is being punished for their ancestors' "
                        "sins. YHWH's counter: 'Behold, all souls are mine (kol ha-nefashot li hennah)' "
                        "(18:4). Three cases: (1) A righteous father lives (18:5-9); (2) His violent son "
                        "dies (18:10-13); (3) The violent son's righteous grandson lives (18:14-17). 'The "
                        "son shall not suffer for the iniquity of the father... The righteousness of "
                        "the righteous shall be upon himself, and the wickedness of the wicked shall be "
                        "upon himself' (18:20). The wicked who repents will live; the righteous who sins "
                        "will die (18:21-24). The climactic appeal: 'Have I any pleasure in the death of "
                        "the wicked, declares the Lord GOD, and not rather that he should turn from his "
                        "way and live?' (18:23). 'Repent and turn from all your transgressions... make "
                        "yourselves a new heart (lev chadash) and a new spirit (ruach chadashah)! Why "
                        "will you die, O house of Israel? For I have no pleasure in the death of anyone' "
                        "(18:31-32)."
            }
        ]
    },

    {
        "id": "ezek-24",
        "ref": "Ezekiel 24",
        "chapter_num": 24,
        "title": "The Pot, the Siege, and the Prophet's Silent Grief",
        "era": "ezekiel_judgment",
        "type": "chapter",
        "themes": ["EXILE", "HOLY"],

        "synopsis": "The climax of the judgment section, set on 'the very day' the siege of Jerusalem "
                    "begins (24:1-2). The rusty pot parable (24:3-14) pictures Jerusalem as a cooking "
                    "pot encrusted with blood-rust that cannot be cleaned -- judgment by fire is the "
                    "only remedy. Then the most personal sign act: YHWH tells Ezekiel 'I am about to "
                    "take the delight of your eyes (machmad einekha) away from you at a stroke' (24:16). "
                    "Ezekiel's wife dies that evening. He is forbidden to mourn: 'Sigh, but not aloud; "
                    "make no mourning for the dead' (24:17). When the people ask why, the answer: when "
                    "the temple ('the delight of your eyes') is destroyed, they will be too stunned to "
                    "mourn. Ezekiel's personal loss becomes a prophetic sign for the nation's loss.",

        "key_verse": {
            "ref": "Ezekiel 24:21",
            "text": "Say to the house of Israel, Thus says the Lord GOD: Behold, I will profane my sanctuary, the pride of your power, the delight of your eyes, and the yearning of your soul.",
            "translation": "ESV"
        },

        "original_terms": [
            "machmad einayim (delight of the eyes -- both Ezekiel's wife and the temple; the most precious possession)",
            "chel'ah (rust/encrustation -- the bloodguilt that cannot be scoured from Jerusalem's 'pot')",
            "challel (to profane -- YHWH himself will profane/desecrate his own sanctuary through judgment)",
            "ot (sign -- Ezekiel himself is the sign to Israel, his grief a prophecy of their grief)"
        ],

        "ane_backdrop": "The cooking-pot metaphor was used in Mesopotamian curse literature to describe "
                        "cities under divine judgment. The prohibition of mourning rites is particularly "
                        "striking: in the ANE, mourning was elaborately ritualized (tearing garments, "
                        "covering the head, wailing, eating the 'bread of mourning'). For Ezekiel to "
                        "suppress all mourning is a radical disruption of social convention, designed to "
                        "provoke questioning and deliver the prophetic message.",

        "second_temple": [
            {
                "source": "Luke 19:41-44",
                "summary": "Jesus weeps over Jerusalem: 'If you, even you, had known... the things "
                           "that make for peace! But now they are hidden from your eyes.'",
                "relevance": "Jesus weeps where Ezekiel was forbidden to weep -- the later prophet "
                             "expresses the grief the earlier prophet had to suppress."
            }
        ],

        "cross_refs": [
            {"ref": "Jeremiah 39:1-2", "note": "The fall of Jerusalem -- the event Ezekiel 24 prophetically anticipates", "type": "ot"},
            {"ref": "Luke 19:41-44", "note": "Jesus weeps over Jerusalem, knowing the destruction Ezekiel foresaw", "type": "nt"},
            {"ref": "2 Kings 25:1", "note": "The siege begins -- 'in the ninth year... in the tenth month' matching Ezekiel 24:1", "type": "ot"},
            {"ref": "Lamentations 2:1-7", "note": "The aftermath of what Ezekiel 24 predicts -- YHWH profanes his own sanctuary", "type": "ot"}
        ],

        "divine_council_note": "The statement 'I will profane my sanctuary' (24:21) is extraordinary -- YHWH "
                               "himself will desecrate his own holy place. This is the divine council's most "
                               "radical act of judgment: not merely allowing the temple's destruction but "
                               "actively profaning it. The council's holiness demands either obedience or "
                               "judgment; when the people choose defilement, YHWH chooses destruction. "
                               "Ezekiel's forbidden mourning embodies the council's decree: the time for "
                               "lament has passed. Only stunned silence is appropriate before the magnitude "
                               "of what the council has decreed.",

        "sections": [
            {
                "heading": "The Rusted Pot -- Jerusalem's Bloodguilt (24:1-14)",
                "body": "'In the ninth year, in the tenth month, on the tenth day of the month, the "
                        "word of YHWH came to me: \"Son of man, write down the name of this day, this "
                        "very day (etsem ha-yom hazzeh). The king of Babylon has laid siege to Jerusalem "
                        "this very day\"' (24:1-2). Ezekiel receives real-time revelation about events "
                        "happening hundreds of miles away. The parable of the pot: 'Set on the pot (sir); "
                        "set it on... put in it the pieces of meat, all the good pieces' (24:3-4). But "
                        "the pot has 'rust' (chel'ah) -- bloodguilt that has corroded into the metal. "
                        "'Woe to the bloody city (ir ha-damim), to the pot whose rust (chel'atah) is in "
                        "it, and whose rust has not gone out of it!' (24:6). The rust cannot be removed "
                        "by scrubbing; only fire will purge it: 'heap on the logs, kindle the fire... "
                        "then set it empty upon the coals, that it may become hot, and its copper may "
                        "burn, that its uncleanness (tum'atah) may be melted in it, its rust consumed' "
                        "(24:10-11)."
            },
            {
                "heading": "The Death of Ezekiel's Wife (24:15-27)",
                "body": "The most devastating personal oracle: 'Son of man, behold, I am about to take "
                        "the delight of your eyes (machmad einekha) away from you at a stroke' (24:16). "
                        "YHWH commands: 'yet you shall not mourn or weep, nor shall your tears run down. "
                        "Sigh (he'aneq), but not aloud (dom); make no mourning for the dead. Bind on "
                        "your turban, put your shoes on your feet; do not cover your upper lip, and do "
                        "not eat the bread of men (lechem anashim)' (24:17). 'So I spoke to the people "
                        "in the morning, and at evening my wife died' (24:18). The prophet obeys. The "
                        "people ask: 'Will you not tell us what these things mean for us?' (24:19). "
                        "The interpretation: 'I will profane my sanctuary (miqdashi), the pride of your "
                        "power (ge'on uzzekhem), the delight of your eyes (machmad einekhem)' (24:21). "
                        "Just as Ezekiel could not mourn his wife, they will not mourn the temple: 'You "
                        "shall not mourn or weep, but you shall rot away in your iniquities and groan "
                        "to one another' (24:23). The day news of Jerusalem's fall arrives, Ezekiel's "
                        "mouth will be opened and his muteness ended (24:26-27)."
            }
        ]
    }
]
