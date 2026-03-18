"""
era_70_aftermath.py -- Aftermath & Oracles Against the Nations (Jeremiah 40-52)

The final section of Jeremiah covers the chaotic aftermath of Jerusalem's fall
and the massive oracles against the nations. Gedaliah is appointed governor by
Babylon but is assassinated (chapter 41). Judean refugees flee to Egypt,
dragging Jeremiah with them against YHWH's explicit command (chapters 42-43).
In Egypt, Jeremiah delivers his final oracles (chapter 44). The Oracles Against
the Nations (chapters 46-51) climax with the longest and most devastating oracle
against Babylon (chapters 50-51). The book concludes with a historical appendix
(chapter 52) paralleling 2 Kings 25.
"""

CHAPTERS = [
    {
        "id": "jer-40-44",
        "ref": "Jeremiah 40-44",
        "chapter_num": 40,
        "title": "Gedaliah, Egypt, and the Last Oracles",
        "era": "jeremiah_aftermath",
        "type": "chapter",
        "themes": ["EXILE", "REMNANT"],

        "synopsis": "After Jerusalem's fall, Nebuchadnezzar appoints Gedaliah son of Ahikam as governor "
                    "over the remnant (40:7). Gedaliah establishes his seat at Mizpah and counsels the "
                    "people: 'Do not be afraid to serve the Chaldeans. Dwell in the land and serve the "
                    "king of Babylon, and it shall be well with you' (40:9). But Ishmael son of Nethaniah, "
                    "of royal blood, assassinates Gedaliah (41:2) -- destroying the last hope for peaceful "
                    "existence in the land. The remaining Judeans panic and consult Jeremiah about fleeing "
                    "to Egypt. He tells them clearly: 'Do not go to Egypt' (42:19). They go anyway, "
                    "taking Jeremiah with them (43:6-7). In Tahpanhes, Egypt, Jeremiah delivers his final "
                    "known oracles, including the indictment of Judean women who burn incense to the "
                    "'Queen of Heaven' (44:17-19).",

        "key_verse": {
            "ref": "Jeremiah 42:10-11",
            "text": "If you will remain in this land, then I will build you up and not pull you down; I will plant you and not pluck you up, for I relent of the disaster that I did to you. Do not fear the king of Babylon, of whom you are afraid. Do not fear him, declares the LORD, for I am with you, to save you and to deliver you from his hand.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Gedalyahu (Gedaliah -- 'YHWH is great'; the governor whose assassination doomed the remnant)",
            "Mitspa (Mizpah -- 'watchtower'; the administrative center after Jerusalem's destruction)",
            "melekhet ha-shamayim (Queen of Heaven -- the deity (likely Ishtar/Asherah) worshipped by Judean women in Egypt)",
            "Tachpanchess (Tahpanhes -- the Egyptian border city where the refugees settled)"
        ],

        "ane_backdrop": "The flight to Egypt after Gedaliah's assassination is deeply ironic: Israel's "
                        "story began with the exodus from Egypt; now, after the exile, the remnant returns "
                        "to Egypt -- reversing the foundational salvation event. The 'Queen of Heaven' "
                        "worship (44:17-19) reflects the widespread cult of Ishtar/Astarte throughout "
                        "the ANE. Archaeological evidence from Elephantine (a Jewish military colony in "
                        "Egypt, 5th century BC) shows that Judean communities in Egypt did worship "
                        "alongside YHWH a female deity called Anat-Yahu, confirming the syncretism "
                        "Jeremiah condemns.",

        "second_temple": [
            {
                "source": "Elephantine Papyri (5th century BC)",
                "summary": "Letters from the Jewish community at Elephantine in Egypt show Judean "
                           "settlers worshipping YHWH alongside a female consort deity.",
                "relevance": "Archaeological confirmation that the syncretism Jeremiah condemned "
                             "in Egypt (chapter 44) continued for generations among diaspora Jews."
            }
        ],

        "cross_refs": [
            {"ref": "2 Kings 25:22-26", "note": "The parallel account of Gedaliah's governorship and assassination", "type": "ot"},
            {"ref": "Deuteronomy 17:16", "note": "'You shall never return that way again' (to Egypt) -- the command the refugees violate", "type": "ot"},
            {"ref": "Hosea 11:5", "note": "'They shall return to Egypt' -- the prophetic warning fulfilled in Jeremiah 43", "type": "ot"},
            {"ref": "Isaiah 30:1-3", "note": "Isaiah's earlier warning against fleeing to Egypt for protection", "type": "ot"}
        ],

        "divine_council_note": "The flight to Egypt against YHWH's explicit command (42:19-43:7) represents "
                               "the ultimate rejection of the divine council's decree. The remnant asks for "
                               "YHWH's word through Jeremiah, promises to obey (42:5-6), then immediately "
                               "disobeys when the word is unfavorable. This pattern -- seeking the council's "
                               "guidance while predetermining the answer -- is the essence of false piety. "
                               "The worship of the Queen of Heaven in Egypt (44:17-19) completes the cycle: "
                               "the refugees have abandoned YHWH for the subordinate deities of the "
                               "council, returning to the exact apostasy that caused the exile.",

        "sections": [
            {
                "heading": "Gedaliah's Governorship and Assassination (40:1-41:18)",
                "body": "Nebuzaradan releases Jeremiah at Ramah and offers him a choice: come to Babylon "
                        "with honor, or stay in the land (40:4-5). Jeremiah chooses to stay with Gedaliah "
                        "at Mizpah. The new governor counsels submission: 'Dwell in the land and serve the "
                        "king of Babylon, and it shall be well with you' (40:9). Judean refugees return "
                        "from surrounding nations (40:11-12), and there is a brief window of hope. But "
                        "Ishmael son of Nethaniah, 'of the royal family' (41:1), assassinates Gedaliah -- "
                        "jealousy, nationalistic pride, and political ambition destroy the last chance for "
                        "a peaceful remnant. Ishmael also murders Babylonian soldiers and Judean pilgrims "
                        "(41:2-8). Johanan son of Kareah pursues Ishmael, who escapes to the Ammonites "
                        "(41:15). The remnant, now leaderless and terrified of Babylonian reprisals, turns "
                        "toward Egypt."
            },
            {
                "heading": "The Consultation and Disobedience (42:1-43:7)",
                "body": "The remaining community asks Jeremiah to inquire of YHWH: 'Whether it is good or "
                        "bad, we will obey the voice of YHWH our God' (42:6). After ten days, YHWH's word "
                        "comes: 'If you will remain in this land, then I will build you up and not pull "
                        "you down; I will plant you and not pluck you up' (42:10) -- the positive verbs "
                        "from Jeremiah's original commission (1:10) are now applied to the remnant. 'Do "
                        "not go to Egypt' (42:19). The response: 'Azariah... and Johanan... and all the "
                        "arrogant men said to Jeremiah, \"You are telling a lie\"' (43:2). They accuse "
                        "Baruch of manipulating Jeremiah -- anything to avoid the word they asked for. "
                        "'So they came into the land of Egypt... and they came to Tahpanhes' (43:7). "
                        "And they brought Jeremiah with them."
            },
            {
                "heading": "The Queen of Heaven and the End in Egypt (44:1-30)",
                "body": "Jeremiah's final recorded oracle confronts the Judeans in Egypt who have resumed "
                        "idolatry: the women respond with shocking defiance: 'We will do everything that "
                        "we have vowed, make offerings to the queen of heaven (melekhet ha-shamayim) and "
                        "pour out drink offerings to her, as we did... in the cities of Judah and in the "
                        "streets of Jerusalem. For then we had plenty of food, and prospered, and saw no "
                        "disaster' (44:17). They credit their prosperity to the pagan goddess, not to "
                        "YHWH. Jeremiah's retort: it was precisely this worship that brought the disaster "
                        "(44:22-23). YHWH's final word: 'Behold, I am watching over them for disaster "
                        "and not for good' (44:27) -- the language of 1:12 ('I am watching over my word'), "
                        "now applied to judgment rather than promise."
            }
        ]
    },

    {
        "id": "jer-46-51",
        "ref": "Jeremiah 46-51",
        "chapter_num": 46,
        "title": "Oracles Against the Nations -- The Cup Poured Out",
        "era": "jeremiah_aftermath",
        "type": "chapter",
        "themes": ["NATIONS", "DC"],

        "synopsis": "The Oracles Against the Nations (OAN) fulfill the universal cup of wrath from "
                    "chapter 25. Each nation that Jeremiah was commissioned to address (1:10, 'over "
                    "nations and kingdoms') now receives its divine sentence: Egypt (46), Philistia (47), "
                    "Moab (48), Ammon (49:1-6), Edom (49:7-22), Damascus (49:23-27), Kedar and Hazor "
                    "(49:28-33), Elam (49:34-39), and Babylon (50-51). The Babylon oracle is the longest "
                    "and most elaborate, declaring that YHWH will raise up a 'destroyer' against the "
                    "great empire: 'Bel is put to shame, Merodach is dismayed; her images are put to "
                    "shame, her idols are dismayed' (50:2). The patron deities of Babylon are defeated "
                    "in the spiritual realm even as Babylon falls in the earthly realm.",

        "key_verse": {
            "ref": "Jeremiah 50:2",
            "text": "Declare among the nations and proclaim, set up a banner and proclaim, conceal it not, and say: 'Babylon is taken, Bel is put to shame, Merodach is dismayed. Her images are put to shame, her idols are dismayed.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Bel (the chief Babylonian deity, equivalent to Marduk -- 'put to shame' by YHWH's judgment)",
            "Merodach (Marduk -- Babylon's patron god, whose cosmic claims are dismantled)",
            "mashchit (destroyer -- the agent YHWH sends against Babylon, echoing the Passover destroyer)",
            "paqad (visit/punish -- the verb of divine intervention, used for both judgment and salvation)"
        ],

        "ane_backdrop": "Oracles against the nations were a standard genre in ANE prophetic literature. "
                        "Egyptian Execration Texts (curses written on pottery and smashed) targeted enemy "
                        "nations. Neo-Assyrian prophets delivered oracles announcing divine judgment on "
                        "the empire's enemies. The innovation in Jeremiah's OAN is theological: the "
                        "judgment is not nationalistic propaganda but the divine council's verdict on all "
                        "nations -- including Israel. Babylon is judged last and most severely because "
                        "it exceeded its commission: YHWH sent Babylon to discipline Judah, but Babylon "
                        "showed no mercy (50:17; 51:34-35).",

        "second_temple": [
            {
                "source": "Revelation 18:1-24",
                "summary": "The fall of 'Babylon the Great' in Revelation draws heavily on Jeremiah "
                           "50-51: 'Fallen, fallen is Babylon the great!' (Rev 18:2; cf. Jer 51:8).",
                "relevance": "The book of Revelation explicitly models its Babylon judgment on "
                             "Jeremiah's oracles -- the eschatological Babylon is the fulfillment "
                             "of what Jeremiah prophesied against historical Babylon."
            },
            {
                "source": "Isaiah 13-14; 47",
                "summary": "Isaiah's Babylon oracles parallel Jeremiah's -- both describe divine "
                           "council judgment on the great empire.",
                "relevance": "Two prophets independently announce the same council verdict against "
                             "Babylon, confirming the decree's certainty."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 13-14; 47", "note": "Isaiah's parallel Babylon oracles -- the same council verdict from a different prophet", "type": "ot"},
            {"ref": "Revelation 18:1-24", "note": "'Fallen, fallen is Babylon' -- Revelation models eschatological Babylon on Jeremiah 50-51", "type": "nt"},
            {"ref": "Exodus 12:23", "note": "The 'destroyer' (mashchit) at the Passover -- the same agent sent against Babylon", "type": "ot"},
            {"ref": "Habakkuk 2:6-20", "note": "Habakkuk's woe oracles against the oppressor -- parallel to Jeremiah's judgment on Babylon", "type": "ot"},
            {"ref": "Daniel 5:1-31", "note": "The fall of Babylon to the Medes and Persians fulfills Jeremiah's oracle", "type": "ot"}
        ],

        "divine_council_note": "The Oracles Against the Nations represent the divine council's comprehensive "
                               "jurisdiction over all peoples and their patron deities. When Jeremiah "
                               "declares 'Bel is put to shame, Merodach is dismayed' (50:2), this is not "
                               "merely the fall of a nation but the defeat of its spiritual patron in the "
                               "heavenly realm. The Deuteronomy 32 framework is visible: each nation was "
                               "allotted to a member of the divine council, and now those nations and their "
                               "patron spirits are judged together. YHWH's authority extends to every "
                               "territory, every empire, every spiritual power. The OAN fulfill Jeremiah's "
                               "original commission: 'I appointed you a prophet to the nations (la-goyim)' "
                               "(1:5) -- his authority, derived from the divine council, was never limited "
                               "to Judah alone.",

        "sections": [
            {
                "heading": "Egypt and the Smaller Nations (46-49)",
                "body": "Egypt is addressed first (chapter 46), in connection with Nebuchadnezzar's "
                        "victory at Carchemish (605 BC): 'That day is the day of the Lord GOD of hosts, "
                        "a day of vengeance (yom neqamah)' (46:10). Even mighty Egypt cannot resist the "
                        "council's decree. Philistia (47) faces the 'waters rising out of the north' -- "
                        "the flood of Babylonian invasion. Moab (48) receives the longest oracle after "
                        "Babylon's: 'Moab has been at ease from his youth and has settled on his dregs... "
                        "and his taste remains unchanged' (48:11). Ammon (49:1-6): 'Has Israel no sons?... "
                        "Why then has Milcom dispossessed Gad?' -- the patron deity Milcom has overstepped "
                        "his allotted territory. Edom (49:7-22): 'The terror you inspire and the pride "
                        "of your heart have deceived you' -- Edom trusted in its mountain strongholds. "
                        "Damascus (49:23-27), Kedar and Hazor (49:28-33), Elam (49:34-39) -- each nation "
                        "receives its verdict. Several oracles end with a remarkable restoration promise: "
                        "'I will restore the fortunes of Moab/Ammon/Elam in the latter days' (48:47; "
                        "49:6, 39) -- even judged nations have a future in YHWH's plan."
            },
            {
                "heading": "The Fall of Babylon -- Bel and Merodach Destroyed (50-51)",
                "body": "The climactic oracle: two chapters (the longest OAN in the prophets) devoted to "
                        "Babylon's fall. 'Babylon is taken, Bel is put to shame (hoveish Bel), Merodach "
                        "is dismayed (chath Merodakh); her images are put to shame, her idols are "
                        "dismayed' (50:2). The spiritual dimension is primary: Bel/Marduk, the patron "
                        "deity who was supposed to protect Babylon, is defeated. 'A nation from the north "
                        "(tsafon)' will make Babylon desolate (50:3) -- the same 'north' language used for "
                        "Babylon's assault on Judah, now turned against Babylon itself. The reason for "
                        "Babylon's judgment: 'Israel is a hunted sheep driven away by lions. First the "
                        "king of Assyria devoured him, and now at last Nebuchadnezzar king of Babylon has "
                        "gnawed his bones' (50:17). Babylon exceeded its commission -- it was YHWH's "
                        "instrument of judgment but became an instrument of cruelty. 'YHWH has opened "
                        "his armory (otsaro) and brought out the weapons of his wrath (kelei za'amo)' "
                        "(50:25). The council's arsenal is deployed against its own former agent."
            },
            {
                "heading": "The Scroll Cast into the Euphrates (51:59-64) and the Historical Appendix (52)",
                "body": "The book's final prophetic act: Jeremiah sends a scroll of Babylon's doom with "
                        "Seraiah to Babylon. After reading it, Seraiah is to 'tie a stone to it and cast "
                        "it into the midst of the Euphrates, and say, \"Thus shall Babylon sink, to rise "
                        "no more\"' (51:63-64). The scroll's descent into the river symbolizes Babylon's "
                        "descent into oblivion. The narrative note: 'Thus far are the words of Jeremiah' "
                        "(51:64) -- everything after this is appendix. Chapter 52 parallels 2 Kings 25, "
                        "providing a historical confirmation of Jeremiah's prophecies: the siege, the "
                        "capture of Zedekiah, the destruction of the temple, the deportation, and finally "
                        "the hopeful note: Evil-merodach of Babylon releases Jehoiachin from prison and "
                        "'spoke kindly to him and gave him a seat above the seats of the kings who were "
                        "with him in Babylon' (52:32). The Davidic line survives in exile -- a seed of "
                        "hope for the messianic Branch."
            }
        ]
    }
]
