"""
era_68_confessions.py -- Confessions & Conflict (Jeremiah 11-25)

The heart of Jeremiah's personal struggle: the five "confessions" or laments
(11:18-12:6; 15:10-21; 17:14-18; 18:18-23; 20:7-18) reveal the prophet's
anguish at his divine calling. Jeremiah accuses YHWH of deception: "O YHWH,
you have deceived me (pittitani), and I was deceived (va'eppat)" (20:7).
He curses the day of his birth (20:14-18), echoing Job. These are not
failures of faith but the raw material of prophetic existence -- the cost
of bearing YHWH's word to a hostile audience. Interspersed are symbolic
actions (the linen belt, the potter's house), confrontations with false
prophets, and the pivotal 70 years prophecy (25:11-12) that becomes the
basis for Daniel's 70 weeks.
"""

CHAPTERS = [
    {
        "id": "jer-11-12",
        "ref": "Jeremiah 11-12",
        "chapter_num": 11,
        "title": "The Broken Covenant and the First Confession",
        "era": "jeremiah_confessions",
        "type": "chapter",
        "themes": ["COV", "RIV", "SPIRIT"],

        "synopsis": "Chapter 11 announces that Judah has broken the Sinai covenant: 'Cursed be the man "
                    "who does not hear the words of this covenant that I commanded your fathers when I "
                    "brought them out of the land of Egypt' (11:3-4). The covenant curses of Deuteronomy "
                    "28 are now activated. A conspiracy against Jeremiah by the men of Anathoth, his own "
                    "hometown, triggers the first confession (11:18-12:6). Jeremiah demands to know why "
                    "the wicked prosper: 'Why does the way of the wicked prosper? Why do all who are "
                    "treacherous thrive?' (12:1). YHWH's response is not comfort but challenge: 'If you "
                    "have raced with men on foot, and they have wearied you, how will you compete with "
                    "horses?' (12:5). The trials will only intensify.",

        "key_verse": {
            "ref": "Jeremiah 12:5",
            "text": "If you have raced with men on foot, and they have wearied you, how will you compete with horses? And if in a safe land you are so trusting, what will you do in the thicket of the Jordan?",
            "translation": "ESV"
        },

        "original_terms": [
            "berit (covenant -- the Sinai covenant whose terms Judah has violated)",
            "arur (cursed -- the covenant curses of Deuteronomy 28 activated by disobedience)",
            "tsaddiq (righteous -- Jeremiah's claim of innocence before YHWH in the lament)",
            "mishpat (justice/judgment -- Jeremiah brings his case before YHWH as the righteous judge)"
        ],

        "ane_backdrop": "The prophetic lament tradition has parallels in Mesopotamian literature. "
                        "The Sumerian 'Man and His God' and the Babylonian 'Ludlul bel nemeqi' "
                        "('I Will Praise the Lord of Wisdom') feature righteous sufferers who "
                        "complain to their gods about undeserved suffering. However, Jeremiah's "
                        "confessions are unique in their directness -- he argues with YHWH, "
                        "accuses him, and demands justice. The prophetic freedom to challenge "
                        "the deity is unparalleled in ANE religious literature.",

        "second_temple": [
            {
                "source": "Habakkuk 1:2-4, 13",
                "summary": "Habakkuk's complaint parallels Jeremiah's: 'Why do you idly look at "
                           "traitors and remain silent when the wicked swallows up the man more "
                           "righteous than he?'",
                "relevance": "The prophetic lament tradition flows from Jeremiah through Habakkuk "
                             "to the Psalms of complaint -- righteous sufferers demanding divine justice."
            },
            {
                "source": "Romans 9:19-21",
                "summary": "Paul's potter/clay metaphor (drawing on Jer 18 and Isa 29:16; 45:9) "
                           "addresses the same theodicy question Jeremiah raises.",
                "relevance": "The NT engages Jeremiah's theodicy through Paul's theology of divine "
                             "sovereignty over vessels of mercy and wrath."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 28:15-68", "note": "The covenant curses that Jeremiah 11 activates -- the theological framework for the exile", "type": "ot"},
            {"ref": "Habakkuk 1:2-4", "note": "Habakkuk's parallel complaint about divine justice", "type": "ot"},
            {"ref": "Job 21:7-15", "note": "Job's question about the prosperity of the wicked -- the same theodicy as Jer 12:1", "type": "ot"},
            {"ref": "Psalm 73:1-17", "note": "Asaph's struggle with the prosperity of the wicked -- resolved in the sanctuary", "type": "ot"},
            {"ref": "Hebrews 12:1-3", "note": "'Running the race' -- the endurance theme YHWH demands of Jeremiah (12:5)", "type": "nt"}
        ],

        "divine_council_note": "Jeremiah's first confession (11:18-12:6) represents the prophet bringing "
                               "his case before the divine council. The language is forensic: 'You, O YHWH "
                               "of hosts, who judges righteously (shophet tsedeq), who tests the heart and "
                               "the mind (bochen kelayot valev)' (11:20). Jeremiah appeals to YHWH as the "
                               "divine judge of the council, asking him to render a verdict against the "
                               "wicked conspirators. YHWH's response ('if you have raced with men on foot, "
                               "how will you compete with horses?') reframes the situation: the prophet's "
                               "mission requires endurance beyond what he currently imagines.",

        "sections": [
            {
                "heading": "The Covenant Is Broken (11:1-17)",
                "body": "YHWH sends Jeremiah to proclaim the covenant: 'Hear the words of this covenant, "
                        "and speak to the men of Judah and the inhabitants of Jerusalem' (11:2). The "
                        "reference is to the Sinai covenant -- specifically the Deuteronomic formulation "
                        "with its blessings and curses. 'Cursed (arur) be the man who does not hear the "
                        "words of this covenant' (11:3). Israel has violated the covenant from the "
                        "beginning: 'They did not obey or incline their ear, but everyone walked in the "
                        "stubbornness of his evil heart (sherirut lev)' (11:8). The phrase 'stubbornness "
                        "of heart' (sherirut lev) is a distinctive Jeremianic expression, occurring 8 "
                        "times in the book. A conspiracy (qesher) has been found among the people (11:9) "
                        "-- they have returned to the sins of their fathers. YHWH therefore brings upon "
                        "them 'disaster (ra'ah) that they cannot escape' (11:11)."
            },
            {
                "heading": "The First Confession: Why Do the Wicked Prosper? (11:18-12:6)",
                "body": "YHWH reveals a plot against Jeremiah's life: 'I was like a gentle lamb (keves "
                        "aluf) led to the slaughter. I did not know it was against me they devised "
                        "schemes' (11:19). The men of Anathoth, Jeremiah's own village, plan to kill him "
                        "and 'cut him off from the land of the living' (11:19). Jeremiah responds with "
                        "the first of his five confessions: 'Righteous are you (tsaddiq attah), O YHWH, "
                        "when I bring my case (riv) before you; yet I would plead my case (mishpatim) "
                        "with you. Why does the way of the wicked prosper (darakh resha'im tsalekhah)? "
                        "Why do all who are treacherous thrive?' (12:1). This is theodicy in its rawest "
                        "form. YHWH's answer is not an explanation but a challenge: 'If you have raced "
                        "with men on foot, and they have wearied you, how will you compete with horses "
                        "(susim)? And if in a safe land (erets shalom) you are so trusting, what will "
                        "you do in the thicket of the Jordan (ga'on ha-yarden)?' (12:5). The coming "
                        "trials will be far worse than anything Jeremiah has yet experienced."
            },
            {
                "heading": "YHWH's Own Lament (12:7-17)",
                "body": "Remarkably, YHWH himself laments: 'I have forsaken my house (azavti et-beiti); I "
                        "have abandoned my heritage (natashti et-nachalati); I have given the beloved of "
                        "my soul (yedidut nafshi) into the hands of her enemies' (12:7). The language is "
                        "heartbreaking: YHWH calls Israel the 'beloved of my soul' even as he gives her "
                        "over to judgment. 'My heritage has become to me like a lion in the forest; she "
                        "has lifted up her voice against me; therefore I hate her' (12:8) -- the 'hate' "
                        "is not emotional rejection but covenantal language for breaking the relationship. "
                        "Yet even here, restoration is promised: 'After I have plucked them up, I will "
                        "again have compassion on them, and I will bring them again each to his heritage "
                        "and each to his land' (12:15)."
            }
        ]
    },

    {
        "id": "jer-15-20",
        "ref": "Jeremiah 15-20",
        "chapter_num": 15,
        "title": "The Prophet's Confessions -- Anguish and Endurance",
        "era": "jeremiah_confessions",
        "type": "chapter",
        "themes": ["SPIRIT", "RIV"],

        "synopsis": "Chapters 15-20 contain Jeremiah's most agonized confessions -- the deep interior "
                    "monologue of a prophet who loves his people but must pronounce their doom. The "
                    "second confession (15:10-21): 'Woe is me, my mother, that you bore me, a man of "
                    "strife and contention to the whole land!' (15:10). The third (17:14-18): 'Heal me, "
                    "O YHWH, and I shall be healed.' The fourth (18:18-23): Jeremiah's enemies plot against "
                    "him; he prays for their destruction. The fifth and most devastating (20:7-18): 'O "
                    "YHWH, you have deceived me (pittitani), and I was deceived' (20:7), culminating in "
                    "the curse on his birthday (20:14-18). Interspersed are the symbolic acts: the potter's "
                    "house (18:1-12), the broken flask (19:1-13), and the confrontation with Pashhur the "
                    "priest (20:1-6).",

        "key_verse": {
            "ref": "Jeremiah 20:9",
            "text": "If I say, 'I will not mention him, or speak any more in his name,' there is in my heart as it were a burning fire shut up in my bones, and I am weary with holding it in, and I cannot.",
            "translation": "ESV"
        },

        "original_terms": [
            "pittah (to deceive/seduce/entice -- Jeremiah's accusation that YHWH has 'seduced' him into the prophetic office)",
            "yotser (potter -- YHWH as the divine potter who shapes nations, from Jer 18)",
            "esh (fire -- the burning compulsion of YHWH's word within Jeremiah's bones)",
            "magor missaviv (terror on every side -- the name Jeremiah gives Pashhur, 20:3)"
        ],

        "ane_backdrop": "The potter metaphor (chapter 18) draws on widespread ANE imagery. In Egypt, the "
                        "ram-headed god Khnum was depicted forming humans on a potter's wheel. In "
                        "Mesopotamia, the creation of humanity involved shaping clay. Jeremiah's innovation "
                        "is applying the potter imagery not to creation but to national destiny: YHWH "
                        "reshapes nations as a potter reshapes clay on the wheel. The prophet's psychological "
                        "struggle has no real ANE parallel -- the intensity of Jeremiah's argument with "
                        "God exceeds anything in Mesopotamian or Egyptian prophetic literature.",

        "second_temple": [
            {
                "source": "Romans 9:19-24",
                "summary": "Paul develops Jeremiah's potter metaphor (Jer 18) into his theology of "
                           "divine sovereignty: 'Has the potter no right over the clay?'",
                "relevance": "Paul's most controversial theological argument draws directly on "
                             "Jeremiah's potter's house vision."
            },
            {
                "source": "2 Timothy 2:20-21",
                "summary": "Paul extends the potter/vessel metaphor: vessels of honor and dishonor "
                           "in a great house.",
                "relevance": "The Jeremianic potter imagery permeates NT theology of divine "
                             "sovereignty and human vessels."
            }
        ],

        "cross_refs": [
            {"ref": "Job 3:1-26", "note": "Job curses the day of his birth -- Jeremiah 20:14-18 echoes the same anguished tradition", "type": "ot"},
            {"ref": "Romans 9:19-24", "note": "Paul's potter/clay theology draws on Jeremiah 18", "type": "nt"},
            {"ref": "Isaiah 45:9", "note": "'Does the clay say to the potter, \"What are you making?\"' -- the same potter sovereignty", "type": "ot"},
            {"ref": "1 Kings 22:19-23", "note": "YHWH sends a 'deceiving spirit' -- relevant to Jeremiah's accusation that YHWH 'deceived' him (20:7)", "type": "ot"},
            {"ref": "2 Corinthians 4:7-12", "note": "'Treasure in jars of clay' -- the fragile vessel carrying the divine word, as Jeremiah experienced", "type": "nt"}
        ],

        "divine_council_note": "Jeremiah 20:7 ('You have deceived me') uses the verb pittah, which appears "
                               "in 1 Kings 22:20-22 where YHWH asks the council 'Who will entice (yefateh) "
                               "Ahab?' and a spirit volunteers to be a 'deceiving spirit.' Jeremiah uses "
                               "the same root to accuse YHWH of 'seducing' him into the prophetic office -- "
                               "the divine council has drawn him into a role that brings nothing but suffering. "
                               "Yet the fire in his bones (20:9) prevents him from quitting: YHWH's word is "
                               "a compulsion that cannot be suppressed. The potter's house vision (18:1-12) "
                               "also has council implications: the divine potter has sovereign authority over "
                               "nations, reshaping them according to the council's decree.",

        "sections": [
            {
                "heading": "The Second and Third Confessions (15:10-21; 17:14-18)",
                "body": "'Woe is me (oy-li), my mother, that you bore me, a man of strife (ish riv) "
                        "and contention (ish madon) to the whole land!' (15:10). Jeremiah's second "
                        "confession voices the isolation of the prophetic calling: everyone hates him. "
                        "Yet he recalls his initial joy: 'Your words were found, and I ate them, and "
                        "your words became to me a joy (sason) and the delight (simchah) of my heart' "
                        "(15:16). YHWH's response is a renewed commission: 'If you return (tashuv), I "
                        "will restore you... if you utter what is precious (yaqar) and not what is "
                        "worthless (zolel), you shall be as my mouth (kefi)' (15:19). The prophet is "
                        "to be YHWH's mouth -- the council's spokesman. The third confession (17:14-18) "
                        "is a prayer for healing and vindication: 'Heal me, O YHWH, and I shall be healed "
                        "(refa'eni va'erafe); save me, and I shall be saved (hoshi'eni ve'ivvashea)' (17:14)."
            },
            {
                "heading": "The Potter's House (18:1-12)",
                "body": "YHWH sends Jeremiah to the potter's workshop for a living parable: 'The vessel "
                        "he was making of clay was spoiled (nishchat) in the potter's hand, and he "
                        "reworked it into another vessel (keli acher), as it seemed good (yashar) to the "
                        "potter to do' (18:4). The interpretation: 'O house of Israel, can I not do with "
                        "you as this potter has done?... Behold, like the clay in the potter's hand, "
                        "so are you in my hand, O house of Israel' (18:6). But the sovereignty is not "
                        "arbitrary -- it is responsive: 'If at any time I declare concerning a nation or "
                        "a kingdom, that I will pluck up and break down and destroy it, and if that "
                        "nation... turns from its evil, I will relent of the disaster that I intended "
                        "to do to it' (18:7-8). The potter is sovereign but not capricious; judgment "
                        "can be averted by repentance."
            },
            {
                "heading": "The Fifth Confession: You Have Deceived Me (20:7-18)",
                "body": "The most agonized passage in the prophets: 'O YHWH, you have deceived me "
                        "(pittitani), and I was deceived (va'eppat); you are stronger than I (chazaqta "
                        "mimmeni), and you have prevailed (va'tukhal)' (20:7). The verb pittah means "
                        "'to seduce, entice, deceive' -- Jeremiah accuses YHWH of luring him into an "
                        "impossible calling. He has become a laughingstock: 'I have become a laughingstock "
                        "all the day; everyone mocks me' (20:7). He tries to stop prophesying, but 'there "
                        "is in my heart as it were a burning fire (esh bo'eret) shut up in my bones, and "
                        "I am weary with holding it in, and I cannot' (20:9). The word of YHWH is a "
                        "compulsion he cannot resist. The passage swings between despair and trust: 'YHWH "
                        "is with me as a dread warrior (gibbor arits)' (20:11) -- then immediately plunges "
                        "back: 'Cursed be the day on which I was born! The day when my mother bore me, "
                        "let it not be blessed!' (20:14). This echoes Job 3:1-26 but is spoken not by a "
                        "suffering innocent but by a prophet who knows exactly why he suffers -- and "
                        "suffers anyway."
            },
            {
                "heading": "The Fourth Confession and the Broken Flask (18:18-19:15)",
                "body": "Jeremiah's enemies conspire: 'Come, let us make plots against Jeremiah, for the "
                        "law (torah) shall not perish from the priest, nor counsel (etsah) from the wise, "
                        "nor the word (davar) from the prophet' (18:18) -- they believe the official "
                        "religious establishment can function without Jeremiah. His fourth confession "
                        "responds with imprecatory prayer: 'Give heed to me, O YHWH, and listen to the "
                        "voice of my adversaries... Let their children be given over to famine' (18:19-21). "
                        "Then YHWH commands the symbolic act of the broken flask (baqbuq): Jeremiah takes "
                        "an earthenware flask to the Valley of Hinnom and smashes it before the elders: "
                        "'So will I break this people and this city, as one breaks a potter's vessel, so "
                        "that it can never be mended' (19:11). The flask, unlike the clay on the wheel, "
                        "is already hardened -- it can only be shattered, not reshaped. The time for "
                        "repentance has passed."
            }
        ]
    },

    {
        "id": "jer-23",
        "ref": "Jeremiah 23",
        "chapter_num": 23,
        "title": "The Righteous Branch and the Council of YHWH",
        "era": "jeremiah_confessions",
        "type": "chapter",
        "themes": ["SEED", "KING", "DC", "NAME"],

        "synopsis": "Chapter 23 is the theological summit of Jeremiah -- containing both the messianic "
                    "Branch prophecy (23:5-6) and the definitive statement on divine council access "
                    "(23:18-22). The chapter opens with judgment on the 'shepherds who destroy and "
                    "scatter the sheep of my pasture' (23:1) -- the failed kings of Judah. Against "
                    "them, YHWH promises: 'I will raise up for David a righteous Branch (tsemach "
                    "tsaddiq), and he shall reign as king and deal wisely... And this is the name by "
                    "which he will be called: YHWH is our righteousness (YHWH Tsidqenu)' (23:5-6). "
                    "The second half targets false prophets, with the decisive criterion: 'Who has "
                    "stood in the council (sod) of YHWH to see and to hear his word?' (23:18).",

        "key_verse": {
            "ref": "Jeremiah 23:5-6",
            "text": "Behold, the days are coming, declares the LORD, when I will raise up for David a righteous Branch, and he shall reign as king and deal wisely, and shall execute justice and righteousness in the land. In his days Judah will be saved, and Israel will dwell securely. And this is the name by which he will be called: 'The LORD is our righteousness.'",
            "translation": "ESV"
        },

        "original_terms": [
            "tsemach tsaddiq (righteous Branch -- the messianic title, from the root tsemach 'to sprout')",
            "YHWH Tsidqenu (YHWH is our righteousness -- the name of the messianic king, bearing the divine name)",
            "sod YHWH (council of YHWH -- the heavenly assembly where YHWH deliberates with his host)",
            "ro'im (shepherds -- a common ANE metaphor for kings; here, the failed kings of Judah)",
            "navi sheqer (false prophet -- one who prophesies without standing in the divine council)"
        ],

        "ane_backdrop": "The 'shepherd' metaphor for kingship was universal in the ANE. Mesopotamian "
                        "kings bore the title 'faithful shepherd' (re'u kenu). The 'Branch' (tsemach) "
                        "imagery draws on the ANE motif of the 'righteous shoot' from the royal tree -- "
                        "a new king from the established dynasty. The concept of the divine council "
                        "(sod/puhru) is well-attested in Mesopotamian and Ugaritic literature: the "
                        "Ugaritic texts describe El presiding over the 'assembly of the gods' (phr ilm), "
                        "and Mesopotamian texts describe the council of the Anunnaki making cosmic "
                        "decisions. Jeremiah's innovation is making council access the criterion for "
                        "prophetic authenticity.",

        "second_temple": [
            {
                "source": "Zechariah 3:8; 6:12",
                "summary": "Zechariah develops the 'Branch' (tsemach) title for the coming messianic "
                           "figure: 'Behold, the man whose name is the Branch.'",
                "relevance": "The post-exilic prophet Zechariah picks up Jeremiah's Branch theology "
                             "and applies it to the eschatological priest-king."
            },
            {
                "source": "Luke 1:78",
                "summary": "Zechariah (John's father) prophesies that the 'sunrise (anatole) shall "
                           "visit us from on high' -- anatole is the LXX translation of tsemach (Branch).",
                "relevance": "The NT identifies Jesus as the fulfillment of the Branch prophecy -- the "
                             "righteous scion of David who bears YHWH's name."
            },
            {
                "source": "4Q174 (Florilegium)",
                "summary": "The Qumran text interprets the 'Branch of David' as the eschatological "
                           "messiah who will arise with the Interpreter of the Torah.",
                "relevance": "The Dead Sea Scrolls community expected a Davidic Branch figure, drawing "
                             "directly on Jeremiah 23:5 and Zechariah 3:8."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 11:1-5", "note": "A shoot (choter) from the stump of Jesse -- parallel messianic Branch imagery", "type": "ot"},
            {"ref": "Zechariah 3:8; 6:12", "note": "The Branch (tsemach) developed as a messianic title in post-exilic prophecy", "type": "ot"},
            {"ref": "1 Kings 22:19-23", "note": "Micaiah sees the divine council deliberating -- the paradigmatic example of the sod YHWH", "type": "ot"},
            {"ref": "Luke 1:78", "note": "The 'sunrise' (anatole/tsemach) from on high -- the Branch has come in Jesus", "type": "nt"},
            {"ref": "Amos 3:7", "note": "'YHWH does nothing without revealing his secret (sod) to his servants the prophets'", "type": "ot"}
        ],

        "divine_council_note": "Jeremiah 23:18-22 is the most explicit statement in scripture about the "
                               "divine council's role in prophetic authentication. The question 'Who has "
                               "stood in the council (sod) of YHWH to see and to hear his word?' (23:18) "
                               "is rhetorical -- the false prophets have NOT stood in the council. They "
                               "prophesy 'visions of their own minds (chazon libbam), not from the mouth "
                               "of YHWH' (23:16). True prophecy requires being admitted to YHWH's heavenly "
                               "assembly, hearing the divine deliberation, and faithfully transmitting the "
                               "council's decree. This connects to the call narratives of Isaiah (chapter 6, "
                               "where Isaiah stands in the council and hears 'Whom shall I send?'), Micaiah "
                               "(1 Kings 22, where he sees YHWH on his throne with the heavenly host), and "
                               "Amos 3:7 ('YHWH does nothing without revealing his sod to his servants the "
                               "prophets'). The Branch prophecy (23:5-6) is also a council decree: YHWH "
                               "announces that he will 'raise up' a messianic king who bears YHWH's own "
                               "name (YHWH Tsidqenu). The Messiah, in the divine council framework, is the "
                               "council's appointed king -- carrying YHWH's authority and identity.",

        "sections": [
            {
                "heading": "Woe to the Shepherds -- Failed Kings (23:1-4)",
                "body": "'Woe (hoi) to the shepherds (ro'im) who destroy and scatter the sheep of my "
                        "pasture!' declares YHWH (23:1). The 'shepherds' are the kings of Judah who have "
                        "failed their royal calling. YHWH pronounces judgment: 'You have scattered my "
                        "flock and have driven them away, and you have not attended to them. Behold, I "
                        "will attend to you (poqed aleikhem) for your evil deeds' (23:2). The wordplay "
                        "on paqad (attend/visit/punish) is pointed: you did not 'attend' to the sheep, "
                        "so I will 'attend' to you -- in judgment. But YHWH himself will gather the "
                        "remnant: 'I will gather the remnant of my flock out of all the countries where "
                        "I have driven them, and I will bring them back to their fold' (23:3). He will "
                        "set over them 'shepherds who will care for them' (23:4) -- the faithful leaders "
                        "of the restoration."
            },
            {
                "heading": "The Righteous Branch -- YHWH Is Our Righteousness (23:5-8)",
                "body": "The messianic promise: 'Behold, the days are coming, declares YHWH, when I will "
                        "raise up for David a righteous Branch (tsemach tsaddiq), and he shall reign as "
                        "king (malakh melek) and deal wisely (hiskil), and shall execute justice (mishpat) "
                        "and righteousness (tsedaqah) in the land' (23:5). The Branch is from David's line "
                        "but transcends any historical Davidic king. His name is the most staggering claim "
                        "in the book: 'And this is the name by which he will be called: YHWH Tsidqenu -- "
                        "YHWH is our righteousness' (23:6). The messianic king bears the divine name YHWH "
                        "as part of his own name. In the divine council framework, this places the Messiah "
                        "within the identity of God himself -- not merely an anointed human but one who "
                        "carries YHWH's name and exercises YHWH's righteousness. The salvation this king "
                        "brings will be so great that 'they shall no longer say, \"As YHWH lives who "
                        "brought up the people of Israel out of the land of Egypt,\" but \"As YHWH lives "
                        "who brought up... the offspring of the house of Israel out of the north country\"' "
                        "(23:7-8) -- the new exodus will eclipse the first."
            },
            {
                "heading": "Who Has Stood in the Council of YHWH? (23:9-22)",
                "body": "The section on false prophets opens with Jeremiah's anguish: 'My heart is broken "
                        "within me; all my bones shake. I am like a drunken man... because of YHWH and "
                        "because of his holy words' (23:9). The false prophets prophesy by Baal (23:13), "
                        "commit adultery, and 'walk in lies' (23:14). They say to those who despise YHWH: "
                        "'It shall be well with you (shalom yihyeh lakhem)' -- the perennial message of "
                        "false prophecy: peace without repentance. Then the decisive criterion: 'For who "
                        "has stood (amad) in the council (sod) of YHWH to see (ra'ah) and to hear (shama) "
                        "his word (davar)? Who has paid attention (hiqshiv) to his word and listened?' "
                        "(23:18). The four verbs -- stood, saw, heard, listened -- describe the prophet's "
                        "participation in the divine assembly. False prophets have not been there. 'But if "
                        "they had stood in my council (be-sodi), then they would have proclaimed my words "
                        "to my people, and they would have turned them from their evil way' (23:22). "
                        "Council access produces genuine prophetic speech; genuine prophetic speech "
                        "produces repentance."
            },
            {
                "heading": "The Burden of YHWH (23:23-40)",
                "body": "YHWH is not a local deity: 'Am I a God at hand (meqarov), declares YHWH, and not "
                        "a God far off (merachoq)? Can a man hide himself in secret places so that I "
                        "cannot see him? Do I not fill heaven and earth?' (23:23-24). YHWH's omnipresence "
                        "means the false prophets cannot hide their lies. He condemns those who steal his "
                        "words 'each from his neighbor' (23:30) -- false prophets who plagiarize genuine "
                        "oracles and add their own fabrications. The final word concerns the 'burden' "
                        "(massa) of YHWH: the people mockingly ask 'What is the burden of YHWH?' and "
                        "YHWH responds: 'You are the burden (massa), and I will cast you off' (23:33, "
                        "with a wordplay on 'burden' and 'cast off'). The prophetic word is not a toy "
                        "to be handled lightly; it is the decree of the divine council, and those who "
                        "trivialize it will be judged."
            }
        ]
    },

    {
        "id": "jer-25",
        "ref": "Jeremiah 25",
        "chapter_num": 25,
        "title": "The 70 Years and the Cup of Wrath",
        "era": "jeremiah_confessions",
        "type": "chapter",
        "themes": ["NATIONS", "EXILE", "DC"],

        "synopsis": "Chapter 25 is the hinge of the entire book, containing two pivotal prophecies: "
                    "the 70 years of Babylonian exile (25:11-12) and the cup of YHWH's wrath poured "
                    "out on all nations (25:15-29). For 23 years Jeremiah has prophesied without result "
                    "(25:3). Now YHWH announces that Nebuchadnezzar is 'my servant' (avdi, 25:9) -- a "
                    "title normally reserved for Israel, Moses, or David. The Babylonian king is YHWH's "
                    "chosen instrument of judgment. The exile will last 70 years (25:11-12), after which "
                    "YHWH will punish Babylon. Then all nations must drink from YHWH's cup of wrath: "
                    "'Drink, be drunk and vomit, fall and rise no more, because of the sword that I "
                    "am sending among you' (25:27).",

        "key_verse": {
            "ref": "Jeremiah 25:11-12",
            "text": "This whole land shall become a ruin and a waste, and these nations shall serve the king of Babylon seventy years. Then after seventy years are completed, I will punish the king of Babylon and that nation, the land of the Chaldeans, for their iniquity, declares the LORD.",
            "translation": "ESV"
        },

        "original_terms": [
            "avdi (my servant -- the astonishing title YHWH gives to Nebuchadnezzar as his instrument of judgment)",
            "shiv'im shanah (seventy years -- the decreed duration of the Babylonian exile)",
            "kos ha-yayin ha-chemah (cup of the wine of wrath -- YHWH's judgment portrayed as forced intoxication)",
            "cherev (sword -- the instrument of divine judgment sent among the nations)"
        ],

        "ane_backdrop": "The concept of a divinely decreed period of exile or punishment is attested in "
                        "ANE literature. The Esarhaddon succession treaty specifies penalties lasting "
                        "generations. The 'seventy years' may reflect the conventional lifespan (Ps 90:10) "
                        "or a typological number for a complete period of judgment. The 'cup of wrath' "
                        "metaphor is found in Mesopotamian curse literature and in Ugaritic texts where "
                        "gods force enemies to drink from a poisoned cup. YHWH's use of Nebuchadnezzar "
                        "as 'my servant' reflects the ANE practice of divine patronage -- gods claimed "
                        "foreign kings as their agents (the Cyrus Cylinder records Marduk choosing Cyrus).",

        "second_temple": [
            {
                "source": "Daniel 9:2, 24-27",
                "summary": "Daniel reads Jeremiah's 70 years prophecy and receives the revelation of "
                           "the 70 'weeks' (490 years) -- a reinterpretation of Jeremiah's chronology.",
                "relevance": "Jeremiah 25:11-12 is the textual basis for Daniel's 70 weeks prophecy, "
                             "the most important messianic chronology in the Old Testament."
            },
            {
                "source": "2 Chronicles 36:21",
                "summary": "The Chronicler interprets the exile as fulfilling Jeremiah's 70 years: "
                           "'to fulfill the word of YHWH by the mouth of Jeremiah.'",
                "relevance": "The canonical interpretation confirms Jeremiah's 70 years as divinely "
                             "decreed and historically fulfilled."
            },
            {
                "source": "Revelation 14:10; 16:19",
                "summary": "The 'cup of wrath' imagery reappears in Revelation: 'he also will drink "
                           "the wine of God's wrath, poured full strength into the cup of his anger.'",
                "relevance": "The eschatological cup of wrath in Revelation draws directly on "
                             "Jeremiah's vision of all nations drinking YHWH's judgment."
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 9:2, 24-27", "note": "Daniel's 70 weeks are built on Jeremiah's 70 years -- the messianic chronology", "type": "ot"},
            {"ref": "2 Chronicles 36:21", "note": "The exile fulfills Jeremiah's 70 years prophecy", "type": "ot"},
            {"ref": "Isaiah 44:28-45:1", "note": "YHWH calls Cyrus 'my shepherd' and 'his anointed' -- the same pattern of using foreign rulers", "type": "ot"},
            {"ref": "Revelation 14:10; 16:19", "note": "The cup of God's wrath -- eschatological fulfillment of Jeremiah's imagery", "type": "nt"},
            {"ref": "Matthew 26:39", "note": "Jesus prays 'let this cup pass from me' -- the cup of wrath he drinks on behalf of the nations", "type": "nt"}
        ],

        "divine_council_note": "The 70 years prophecy and the cup of wrath are both divine council decrees. "
                               "The designation of Nebuchadnezzar as 'my servant' (25:9) means the Babylonian "
                               "king is acting under YHWH's commission -- he is an instrument of the council's "
                               "judgment. The 70-year duration is the council's determined sentence. The cup of "
                               "wrath (25:15-29) is poured out on all nations -- beginning with Jerusalem and "
                               "extending to every kingdom on earth, ending with Babylon itself. The universality "
                               "of the judgment reflects the divine council's authority over all nations and "
                               "their patron deities. 'Sheshach' (25:26, a cipher for 'Babel') 'shall drink "
                               "after them' -- even YHWH's chosen instrument of judgment will itself be judged.",

        "sections": [
            {
                "heading": "Twenty-Three Years of Rejected Prophecy (25:1-7)",
                "body": "The chapter opens with a chronological marker: 'the word that came to Jeremiah "
                        "concerning all the people of Judah, in the fourth year of Jehoiakim... the first "
                        "year of Nebuchadnezzar king of Babylon' (25:1) -- 605 BC, the year Nebuchadnezzar "
                        "defeated Egypt at Carchemish and became the dominant power. 'For twenty-three years "
                        "(esrim ve-shalosh shanah), from the thirteenth year of Josiah... to this day, the "
                        "word of YHWH has come to me, and I have spoken persistently to you, but you have "
                        "not listened' (25:3). YHWH also 'persistently sent all his servants the prophets' "
                        "(25:4) -- the phrase 'rising early and sending' (hashkem veshalocah) is a "
                        "distinctive Jeremianic expression for YHWH's relentless prophetic outreach."
            },
            {
                "heading": "Nebuchadnezzar My Servant -- The 70 Years (25:8-14)",
                "body": "The sentence: 'Behold, I will send for all the tribes of the north, declares "
                        "YHWH, and for Nebuchadnezzar the king of Babylon, my servant (avdi), and I "
                        "will bring them against this land and its inhabitants' (25:9). The title 'my "
                        "servant' for a pagan king is shocking -- it places Nebuchadnezzar in the same "
                        "category as Moses (Deut 34:5) and David (2 Sam 7:5). YHWH will use Babylon to "
                        "judge Judah, then judge Babylon: 'This whole land shall become a ruin and a "
                        "waste, and these nations shall serve the king of Babylon seventy years (shiv'im "
                        "shanah). Then after seventy years are completed, I will punish the king of "
                        "Babylon and that nation' (25:11-12). The 70-year period (roughly 605-539 BC, "
                        "or 586-516 BC depending on the calculation) becomes the basis for Daniel's "
                        "reinterpretation in the 70 weeks prophecy (Dan 9:24-27)."
            },
            {
                "heading": "The Cup of Wrath for All Nations (25:15-38)",
                "body": "YHWH commands Jeremiah: 'Take from my hand this cup of the wine of wrath (kos "
                        "yayin ha-chemah hazzeh), and make all the nations to whom I send you drink it' "
                        "(25:15). The list begins with 'Jerusalem and the cities of Judah' (25:18) -- "
                        "judgment begins with the household of God. It extends to Egypt, Uz, Philistia, "
                        "Edom, Moab, Ammon, Tyre, Sidon, Dedan, Tema, Buz, Arabia, Zimri, Elam, Media, "
                        "and all the kingdoms of the earth (25:19-26). Finally: 'And after them the king "
                        "of Sheshach (Babel) shall drink' (25:26). 'Sheshach' is an atbash cipher for "
                        "'Babel' -- the letters are reversed in the Hebrew alphabet. If any nation "
                        "refuses the cup: 'You must drink! For behold, I begin to work disaster at the "
                        "city that is called by my name, and shall you go unpunished?' (25:29). The "
                        "universal scope -- every nation, every kingdom -- reveals the divine council's "
                        "comprehensive authority over all peoples and their patron powers."
            }
        ]
    }
]
