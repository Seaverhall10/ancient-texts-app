"""
era_69_new_covenant.py -- New Covenant & Fall of Jerusalem (Jeremiah 26-39)

The central section of Jeremiah contains the most important prophetic text in
the Old Testament: the New Covenant oracle of 31:31-34. This section also
narrates the political conflicts leading to Jerusalem's fall, the burning of
Jeremiah's scroll by Jehoiakim, the imprisonment of Jeremiah under Zedekiah,
and the actual fall of Jerusalem in 586 BC. The "Book of Consolation"
(chapters 30-33) is the theological heart of the entire book -- judgment is
not the final word. Beyond destruction lies restoration, a new covenant, and
a new relationship between YHWH and his people.
"""

CHAPTERS = [
    {
        "id": "jer-26-29",
        "ref": "Jeremiah 26-29",
        "chapter_num": 26,
        "title": "Trial, Yoke, and the Letter to the Exiles",
        "era": "jeremiah_new_covenant",
        "type": "chapter",
        "themes": ["EXILE", "RIV"],

        "synopsis": "These chapters narrate Jeremiah's escalating conflicts with the religious and "
                    "political establishment. Chapter 26 recounts his trial for the temple sermon -- "
                    "the priests and prophets demand his death, but Jeremiah is saved by the elders who "
                    "cite the precedent of Micah of Moresheth (26:18-19). Chapter 27 features the "
                    "symbolic yoke: Jeremiah wears a wooden yoke to proclaim that all nations must "
                    "'serve the king of Babylon' (27:6). Chapter 28 narrates the confrontation with "
                    "the false prophet Hananiah, who breaks Jeremiah's yoke and prophesies return within "
                    "two years. YHWH replaces the wooden yoke with iron: 'I have put upon the neck of "
                    "all these nations an iron yoke' (28:14). Chapter 29 is Jeremiah's letter to the "
                    "exiles in Babylon: 'Seek the welfare (shalom) of the city where I have sent you "
                    "into exile, and pray to YHWH on its behalf' (29:7), and the promise: 'When seventy "
                    "years are completed for Babylon, I will visit you... For I know the plans I have "
                    "for you... plans for welfare (shalom) and not for evil, to give you a future and "
                    "a hope' (29:10-11).",

        "key_verse": {
            "ref": "Jeremiah 29:11",
            "text": "For I know the plans I have for you, declares the LORD, plans for welfare and not for evil, to give you a future and a hope.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ol (yoke -- the symbol of servitude to Babylon, YHWH's decreed instrument)",
            "shalom (welfare/peace -- what the exiles should seek for Babylon, and what YHWH plans for Israel)",
            "makhashavot (plans/thoughts -- YHWH's deliberate, purposeful intentions for Israel's future)",
            "tiqvah (hope -- the expectation of a positive future beyond the exile)"
        ],

        "ane_backdrop": "The yoke symbolism was common in ANE political discourse. Assyrian and "
                        "Babylonian kings described conquered peoples as 'bearing the yoke.' Breaking "
                        "the yoke symbolized rebellion. Jeremiah's counsel to accept the Babylonian yoke "
                        "was political treason by contemporary standards -- equivalent to urging surrender "
                        "to the enemy. The letter to the exiles (chapter 29) represents an innovative "
                        "theological response to exile: rather than awaiting immediate deliverance, the "
                        "community should settle, build, plant, and 'seek the welfare of the city' -- "
                        "a theology of faithful presence in diaspora.",

        "second_temple": [
            {
                "source": "1 Peter 2:11-12",
                "summary": "Peter addresses Christians as 'sojourners and exiles' who should maintain "
                           "good conduct among the nations -- the same exilic theology as Jeremiah 29.",
                "relevance": "The NT church's self-understanding as 'exiles' draws on Jeremiah's "
                             "theology of faithful presence in a foreign land."
            },
            {
                "source": "Jeremiah 29:13 in Matthew 7:7",
                "summary": "'You will seek me and find me, when you seek me with all your heart' "
                           "echoes in Jesus' 'seek and you will find.'",
                "relevance": "Jesus' invitation to seek God draws on Jeremiah's promise to the exiles."
            }
        ],

        "cross_refs": [
            {"ref": "Micah 3:12", "note": "Micah prophesied Jerusalem's destruction -- the precedent that saved Jeremiah's life (26:18)", "type": "ot"},
            {"ref": "1 Peter 2:11-12", "note": "Christians as 'sojourners and exiles' -- the NT application of Jeremianic exile theology", "type": "nt"},
            {"ref": "Deuteronomy 18:20-22", "note": "The test of a true prophet -- applied when Hananiah dies as Jeremiah predicted (28:16-17)", "type": "ot"},
            {"ref": "Matthew 7:7", "note": "'Seek and you will find' echoes Jeremiah 29:13", "type": "nt"}
        ],

        "divine_council_note": "The confrontation with Hananiah (chapter 28) is a contest between true and "
                               "false divine council access. Hananiah claims YHWH has 'broken the yoke of "
                               "Babylon' (28:2) -- but he has not stood in the council. Jeremiah initially "
                               "says 'Amen! May YHWH do so' (28:6), genuinely hoping Hananiah is right. But "
                               "the council's word comes through Jeremiah: the wooden yoke becomes iron, and "
                               "Hananiah will die within the year (28:16). Hananiah dies in the seventh month "
                               "(28:17) -- the divine council's verdict is executed. The letter to the exiles "
                               "(chapter 29) is also a council decree: the exile has a divinely determined "
                               "duration (70 years) and purpose (restoration).",

        "sections": [
            {
                "heading": "Jeremiah's Trial at the Temple (26:1-24)",
                "body": "After the temple sermon, 'the priests and the prophets and all the people laid "
                        "hold of him, saying, \"You shall die!\"' (26:8). The charge: 'This man deserves "
                        "the sentence of death, because he has prophesied against this city' (26:11). "
                        "Jeremiah's defense is simple: 'YHWH sent me to prophesy against this house and "
                        "this city all the words that you have heard. Now therefore amend your ways and "
                        "your deeds, and obey the voice of YHWH your God' (26:12-13). The elders intervene "
                        "with a precedent: 'Micah of Moresheth prophesied in the days of Hezekiah king "
                        "of Judah... Did Hezekiah king of Judah and all Judah put him to death? Did he "
                        "not fear YHWH and entreat the favor of YHWH?' (26:18-19). The precedent saves "
                        "Jeremiah -- but the text notes that another prophet, Uriah, was not so fortunate: "
                        "Jehoiakim had him extradited from Egypt and executed (26:20-23)."
            },
            {
                "heading": "The Yoke and the False Prophet Hananiah (27-28)",
                "body": "YHWH commands Jeremiah to make 'yoke-bars and thongs (motot)' and wear them "
                        "(27:2), symbolizing submission to Babylon. The message to all surrounding nations: "
                        "'I have given all these lands into the hand of Nebuchadnezzar the king of Babylon, "
                        "my servant' (27:6). Any nation that 'will not serve the king of Babylon... I will "
                        "punish' (27:8). The false prophet Hananiah responds by breaking the yoke off "
                        "Jeremiah's neck: 'Thus says YHWH: Even so will I break the yoke of "
                        "Nebuchadnezzar king of Babylon from the neck of all the nations within two years' "
                        "(28:11). YHWH's counter-response through Jeremiah: 'You have broken wooden bars, "
                        "but you have made in their place bars of iron' (28:13). Resistance to YHWH's "
                        "decree makes the judgment worse. 'This very year you shall die, because you have "
                        "uttered rebellion against YHWH' (28:16). Hananiah dies two months later (28:17)."
            },
            {
                "heading": "The Letter to the Exiles (29:1-23)",
                "body": "Jeremiah sends a letter to the exiles in Babylon with revolutionary counsel: "
                        "'Build houses and live in them; plant gardens and eat their produce. Take wives "
                        "and have sons and daughters... multiply there, and do not decrease' (29:5-6). "
                        "Most remarkably: 'Seek the welfare (shalom) of the city where I have sent you "
                        "into exile, and pray to YHWH on its behalf, for in its welfare (shalom) you "
                        "will find your welfare' (29:7). This is exile theology: YHWH's people can "
                        "flourish in a foreign land. The false prophets in Babylon who promise quick "
                        "return are liars. YHWH's actual promise: 'When seventy years are completed for "
                        "Babylon, I will visit you and I will fulfill to you my promise and bring you "
                        "back to this place' (29:10). Then the beloved verse: 'For I know the plans "
                        "(makhashavot) I have for you, declares YHWH, plans for welfare (shalom) and "
                        "not for evil (ra'ah), to give you a future (acharit) and a hope (tiqvah)' "
                        "(29:11). 'You will seek me and find me, when you seek me with all your heart "
                        "(bekhol-levavkhem)' (29:13)."
            }
        ]
    },

    {
        "id": "jer-31",
        "ref": "Jeremiah 31",
        "chapter_num": 31,
        "title": "The New Covenant -- Torah Written on the Heart",
        "era": "jeremiah_new_covenant",
        "type": "chapter",
        "themes": ["COV", "SEED", "REVERSAL", "LOVE", "SPIRIT"],

        "synopsis": "Jeremiah 31 is the theological summit of the entire Old Testament prophetic corpus. "
                    "It contains the New Covenant oracle (31:31-34) -- the only place in the Hebrew Bible "
                    "where the phrase berit chadashah ('new covenant') appears. YHWH declares that the "
                    "Sinai covenant has been broken and that he will make a qualitatively new covenant "
                    "with Israel: 'I will put my law within them (beqirbam), and I will write it on "
                    "their hearts (al-libbam)' (31:33). The chapter also contains Rachel's weeping "
                    "(31:15), the promise of return, and YHWH's eternal love: 'I have loved you with an "
                    "everlasting love (ahavat olam); therefore I have continued my faithfulness (chesed) "
                    "to you' (31:3).",

        "key_verse": {
            "ref": "Jeremiah 31:31-33",
            "text": "Behold, the days are coming, declares the LORD, when I will make a new covenant with the house of Israel and the house of Judah, not like the covenant that I made with their fathers on the day when I took them by the hand to bring them out of the land of Egypt, my covenant that they broke, though I was their husband, declares the LORD. For this is the covenant that I will make with the house of Israel after those days, declares the LORD: I will put my law within them, and I will write it on their hearts. And I will be their God, and they shall be my people.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "berit chadashah (new covenant -- the only occurrence of this exact phrase in the Hebrew Bible)",
            "torah (law/instruction -- what YHWH will write on the heart in the New Covenant)",
            "lev (heart -- the seat of will, intellect, and decision in Hebrew anthropology; the location of the internalized Torah)",
            "ahavat olam (everlasting love -- YHWH's eternal, covenant-faithful love for Israel)",
            "chesed (steadfast love/faithfulness -- the ongoing expression of ahavat olam)",
            "yada (know -- direct, personal knowledge of YHWH available to all in the New Covenant)"
        ],

        "ane_backdrop": "Covenant renewal was common in the ANE -- Hittite and Assyrian treaties were "
                        "periodically renewed or updated. However, Jeremiah's New Covenant is not merely "
                        "a renewal but something qualitatively different: the Torah is internalized, "
                        "written on the heart rather than on stone or parchment. No ANE parallel exists "
                        "for this concept. The nearest analogy is the Egyptian concept of Ma'at (cosmic "
                        "order) dwelling in the heart of the wise, but even this lacks the covenantal "
                        "framework and the promise of universal knowledge of the deity.",

        "second_temple": [
            {
                "source": "Hebrews 8:8-12",
                "summary": "The author of Hebrews quotes Jeremiah 31:31-34 in full -- the longest "
                           "OT quotation in the NT -- to argue that Jesus mediates a 'better covenant.'",
                "relevance": "The entire argument of Hebrews depends on Jeremiah's New Covenant -- "
                             "the old covenant is 'obsolete' (Heb 8:13) because the new has come in Christ."
            },
            {
                "source": "Luke 22:20 / 1 Corinthians 11:25",
                "summary": "Jesus at the Last Supper: 'This cup is the new covenant (kaine diatheke) "
                           "in my blood.' Paul transmits the same tradition.",
                "relevance": "Jesus explicitly identifies his sacrificial death as the inauguration of "
                             "Jeremiah's New Covenant -- the blood that establishes the berit chadashah."
            },
            {
                "source": "2 Corinthians 3:3-6",
                "summary": "Paul describes believers as 'a letter from Christ... written not with ink "
                           "but with the Spirit of the living God, not on tablets of stone but on "
                           "tablets of human hearts.'",
                "relevance": "Paul's Spirit-vs-letter theology is a direct development of Jeremiah's "
                             "New Covenant promise: the Torah written on hearts by the Spirit."
            },
            {
                "source": "Matthew 2:17-18",
                "summary": "Matthew cites Jeremiah 31:15 ('Rachel weeping for her children') in "
                           "connection with Herod's slaughter of the innocents.",
                "relevance": "The NT reads Rachel's weeping as fulfilled in the suffering that attends "
                             "the Messiah's coming -- grief that precedes ultimate redemption."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 8:8-12", "note": "The full quotation of Jer 31:31-34 -- the longest OT quote in the NT", "type": "nt"},
            {"ref": "Luke 22:20", "note": "Jesus identifies his blood as the New Covenant of Jeremiah 31", "type": "nt"},
            {"ref": "2 Corinthians 3:3-6", "note": "Paul's theology of Torah written on hearts by the Spirit", "type": "nt"},
            {"ref": "Ezekiel 36:26-27", "note": "'A new heart and a new spirit' -- Ezekiel's parallel to the New Covenant", "type": "ot"},
            {"ref": "Deuteronomy 30:6", "note": "YHWH will 'circumcise your heart' -- the Torah's own anticipation of internalized obedience", "type": "ot"},
            {"ref": "Matthew 2:17-18", "note": "Rachel weeping (Jer 31:15) fulfilled at the slaughter of the innocents", "type": "nt"}
        ],

        "divine_council_note": "The New Covenant oracle is a divine council decree of the highest order. "
                               "The formula 'Behold, the days are coming, declares YHWH' (hinneh yamim "
                               "ba'im ne'um YHWH) is the solemn announcement of a council decision. The "
                               "New Covenant addresses the fundamental problem identified throughout the "
                               "prophets: Israel's inability to keep the Torah because of a defective heart. "
                               "The council's solution is not a new law but a new heart -- the same Torah, "
                               "but written internally rather than externally. The result: 'they shall all "
                               "know me, from the least of them to the greatest' (31:34) -- universal, "
                               "direct knowledge of YHWH, bypassing the mediation of priest and prophet. "
                               "In the divine council framework, this means every covenant member becomes "
                               "a participant in the knowledge of YHWH that was previously reserved for "
                               "prophets who stood in the sod.",

        "sections": [
            {
                "heading": "Everlasting Love and Rachel's Weeping (31:1-22)",
                "body": "The chapter opens with restoration promise: 'I have loved you with an everlasting "
                        "love (ahavat olam ahavtikh); therefore I have continued my faithfulness (chesed) "
                        "to you' (31:3). Israel will be rebuilt: 'Again you shall adorn yourself with "
                        "tambourines and shall go forth in the dance of the merrymakers' (31:4). But "
                        "restoration passes through grief: 'A voice is heard in Ramah, lamentation and "
                        "bitter weeping. Rachel is weeping for her children; she refuses to be comforted "
                        "for her children, because they are no more' (31:15). Rachel, the mother of "
                        "Joseph and Benjamin, weeps from her tomb at Ramah as the exiles pass by. YHWH "
                        "responds: 'Keep your voice from weeping... there is hope for your future (tiqvah "
                        "le-acharitikh)... your children shall come back to their own country' (31:16-17). "
                        "The mysterious closing: 'YHWH has created a new thing on the earth: a woman "
                        "encircles (tesovev) a man' (31:22) -- an enigmatic statement that has puzzled "
                        "interpreters for millennia."
            },
            {
                "heading": "The New Covenant -- Berit Chadashah (31:31-34)",
                "body": "The single most important prophetic oracle in the Old Testament: 'Behold, the "
                        "days are coming (hinneh yamim ba'im), declares YHWH, when I will make (karati) "
                        "a new covenant (berit chadashah) with the house of Israel and the house of Judah' "
                        "(31:31). The newness is specified: 'Not like the covenant that I made with their "
                        "fathers on the day when I took them by the hand to bring them out of the land of "
                        "Egypt, my covenant that they broke (heferu), though I was their husband (ba'al), "
                        "declares YHWH' (31:32). The Sinai covenant was not defective -- Israel was. The "
                        "new covenant's distinctive: 'I will put my law within them (natati et-torati "
                        "beqirbam), and I will write it on their hearts (ve-al-libbam ekhtavenah). And "
                        "I will be their God, and they shall be my people' (31:33). Three transformations: "
                        "(1) Internalization -- Torah moves from external tablets to the inner person; "
                        "(2) Universal knowledge -- 'they shall all know me, from the least (miqetannam) "
                        "to the greatest (ve-ad-gedolam)' (31:34); (3) Definitive forgiveness -- 'I will "
                        "forgive their iniquity (avon), and I will remember their sin (chatta'at) no more' "
                        "(31:34). This is what Jesus inaugurated at the Last Supper: 'This cup is the new "
                        "covenant in my blood' (Luke 22:20)."
            },
            {
                "heading": "The Permanence of Israel and the New Jerusalem (31:35-40)",
                "body": "YHWH guarantees the New Covenant with the most permanent things in creation: "
                        "'If this fixed order (chuqqot) departs from before me, declares YHWH, then the "
                        "offspring (zera) of Israel shall cease from being a nation before me forever' "
                        "(31:36). The sun, moon, and stars serve as witnesses -- if they fail, then Israel "
                        "will fail. Since they never fail, Israel is eternally secure. The chapter closes "
                        "with a vision of the rebuilt Jerusalem: 'The city shall be rebuilt for YHWH from "
                        "the Tower of Hananel to the Corner Gate' (31:38). Even the Valley of Hinnom (the "
                        "place of child sacrifice and defilement) 'shall be sacred (qodesh) to YHWH. It "
                        "shall not be plucked up or overthrown anymore forever' (31:40). The geography "
                        "of judgment becomes the geography of holiness."
            }
        ]
    },

    {
        "id": "jer-36-39",
        "ref": "Jeremiah 36-39",
        "chapter_num": 36,
        "title": "The Burning Scroll and the Fall of Jerusalem",
        "era": "jeremiah_new_covenant",
        "type": "chapter",
        "themes": ["EXILE", "KING"],

        "synopsis": "Chapters 36-39 narrate the final crisis. Chapter 36: Jeremiah dictates his oracles "
                    "to Baruch, who reads them in the temple. King Jehoiakim hears the scroll read and "
                    "cuts it apart with a knife, burning each column as it is read (36:23) -- a breathtaking "
                    "act of defiance against YHWH's word. Jeremiah re-dictates the scroll 'with many "
                    "similar words added' (36:32). Chapters 37-38: Under Zedekiah, Jeremiah is arrested, "
                    "beaten, and thrown into a muddy cistern to die. The Ethiopian eunuch Ebed-melech "
                    "rescues him (38:7-13). Chapter 39: Jerusalem falls to Nebuchadnezzar in the eleventh "
                    "year of Zedekiah (586 BC). Zedekiah is captured, his sons are killed before his eyes, "
                    "and he is blinded -- the last thing he sees is his dynasty's end. The temple and city "
                    "are burned. Jeremiah is released and given his freedom.",

        "key_verse": {
            "ref": "Jeremiah 36:23",
            "text": "As Jehudi read three or four columns, the king would cut them off with a knife and throw them into the fire in the fire pot, until the entire scroll was consumed in the fire that was in the fire pot.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "megillah (scroll -- the physical medium of YHWH's written word, burned by Jehoiakim)",
            "ta'ar sofer (scribe's knife -- the tool Jehoiakim used to cut YHWH's word; ironic reversal of the scribe's pen)",
            "bor (cistern -- the waterless pit where Jeremiah is thrown to die, a symbol of Sheol)",
            "Eved-melekh (servant of the king -- the Ethiopian eunuch who rescues Jeremiah, a Gentile showing more faith than Israel)"
        ],

        "ane_backdrop": "The destruction of prophetic or divine texts was considered an extreme act in the "
                        "ANE. Mesopotamian literary tradition held that destroying inscribed tablets was an "
                        "affront to the gods who authorized them. Jehoiakim's column-by-column burning of "
                        "Jeremiah's scroll is an act of deliberate sacrilege -- not merely political "
                        "censorship but rejection of the divine word itself. The Babylonian siege and "
                        "destruction of Jerusalem in 586 BC is confirmed by the Babylonian Chronicle, "
                        "the archaeological destruction layer in Jerusalem excavations, and the Lachish "
                        "Letters.",

        "second_temple": [
            {
                "source": "Acts 8:27-39",
                "summary": "The Ethiopian eunuch reading Isaiah on the road to Gaza echoes Ebed-melech, "
                           "the Ethiopian who saved Jeremiah -- Gentiles receptive to YHWH's word.",
                "relevance": "The parallel between the two Ethiopian figures suggests a typological "
                             "pattern: Gentiles who honor the prophetic word when Israel rejects it."
            },
            {
                "source": "2 Kings 25:1-21",
                "summary": "The parallel account of Jerusalem's fall, closely matching Jeremiah 39 "
                           "and the expanded account in Jeremiah 52.",
                "relevance": "Multiple canonical witnesses confirm the historical reality of the "
                             "fall of Jerusalem and its theological interpretation."
            }
        ],

        "cross_refs": [
            {"ref": "2 Kings 25:1-21", "note": "The parallel account of Jerusalem's fall", "type": "ot"},
            {"ref": "2 Chronicles 36:15-21", "note": "The Chronicler's interpretation of the fall as covenant judgment", "type": "ot"},
            {"ref": "Lamentations 1-5", "note": "The poetic response to the destruction Jeremiah 39 narrates", "type": "ot"},
            {"ref": "Ezekiel 24:15-27", "note": "Ezekiel learns of Jerusalem's fall in Babylon -- the exile perspective", "type": "ot"},
            {"ref": "Acts 8:27-39", "note": "The Ethiopian eunuch -- typological parallel to Ebed-melech the Ethiopian", "type": "nt"}
        ],

        "divine_council_note": "Jehoiakim's burning of the scroll (chapter 36) is an attempt to nullify "
                               "the divine council's decree by destroying its written record. It fails "
                               "completely: Jeremiah re-dictates the scroll 'with many similar words added' "
                               "(36:32) -- the word of the council cannot be destroyed. The fall of Jerusalem "
                               "(chapter 39) is the execution of the council's judgment, decreed throughout "
                               "the book. Yet even in the destruction, YHWH preserves his prophet and the "
                               "faithful Gentile Ebed-melech (39:15-18) -- the council's judgment is not "
                               "indiscriminate. Nebuchadnezzar's order to 'look after' Jeremiah (39:11-12) "
                               "is ironic: the pagan king treats the prophet better than his own people did.",

        "sections": [
            {
                "heading": "The Burning of the Scroll (36:1-32)",
                "body": "In the fourth year of Jehoiakim (605 BC), YHWH commands Jeremiah: 'Take a scroll "
                        "(megillah) and write on it all the words that I have spoken to you... Perhaps "
                        "the house of Judah will hear... and everyone will turn from his evil way, and I "
                        "will forgive their iniquity' (36:2-3). Baruch the scribe writes at Jeremiah's "
                        "dictation and reads the scroll publicly in the temple (36:10). Officials hear and "
                        "tremble (36:16), but King Jehoiakim's response is chilling: 'As Jehudi read three "
                        "or four columns (delathot), the king would cut them off with a scribe's knife "
                        "(ta'ar hasofer) and throw them into the fire... until the entire scroll was "
                        "consumed' (36:23). The narrator adds the devastating detail: 'Yet neither the "
                        "king nor any of his servants who heard all these words was afraid (pachad), "
                        "nor did they tear their garments' (36:24). Compare this to Josiah, who tore his "
                        "garments when the Torah was read (2 Kings 22:11). YHWH's response: Jeremiah "
                        "re-dictates the entire scroll 'and many similar words were added' (36:32)."
            },
            {
                "heading": "Jeremiah in the Cistern (37-38)",
                "body": "Under Zedekiah, Jeremiah continues to prophesy surrender to Babylon and is "
                        "arrested for 'deserting to the Chaldeans' (37:13). He is beaten and imprisoned "
                        "(37:15-16). Zedekiah secretly consults him: 'Is there any word from YHWH?' "
                        "Jeremiah replies: 'There is... You shall be given into the hand of the king "
                        "of Babylon' (37:17). The officials then throw Jeremiah into 'the cistern (bor) "
                        "of Malkijah... and they let Jeremiah down by ropes. And there was no water in "
                        "the cistern, but only mud (tit), and Jeremiah sank in the mud' (38:6). Left to "
                        "die. But Ebed-melech the Ethiopian (Kushi) -- a foreigner, a eunuch, a court "
                        "official -- intercedes with the king and rescues Jeremiah with old rags and "
                        "worn-out clothes lowered by ropes (38:11-13). A Gentile saves the prophet when "
                        "Israel tried to kill him."
            },
            {
                "heading": "The Fall of Jerusalem (39:1-18)",
                "body": "In the ninth year of Zedekiah, 'Nebuchadnezzar king of Babylon and all his "
                        "army came against Jerusalem and besieged it' (39:1). In the eleventh year, "
                        "'the city was broken into' (39:2). Zedekiah flees by night but is captured "
                        "'in the plains of Jericho' (39:5). 'The king of Babylon slaughtered the sons "
                        "of Zedekiah at Riblah before his eyes, and the king of Babylon slaughtered all "
                        "the nobles of Judah. He put out the eyes of Zedekiah and bound him in chains' "
                        "(39:6-7). The last thing Zedekiah sees is the death of his sons -- the end of "
                        "the Davidic line as a reigning dynasty. 'The Chaldeans burned the king's house "
                        "and the houses of the people, and broke down the walls of Jerusalem' (39:8). "
                        "But Nebuzaradan the captain of the guard releases Jeremiah: 'Take him, look "
                        "after him well, and do him no harm' (39:12). The pagan commander shows more "
                        "respect for the prophet than the kings of Judah did."
            }
        ]
    }
]
