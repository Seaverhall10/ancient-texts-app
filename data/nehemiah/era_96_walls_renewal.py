"""
era_96_walls_renewal.py -- Walls Rising (Nehemiah 1-7)

Nehemiah, a cupbearer turned governor, rebuilds Jerusalem's walls in 52 days
against fierce opposition. The wall is both physical defense and theological
statement: YHWH's people have defined boundaries, an established identity,
and a God who keeps his promises. From Nehemiah's prayer in Susa through the
armed construction crews to the enemies' recognition that 'this work was
accomplished with the help of our God,' this era covers the rebuilding project
from start to completion.
"""

CHAPTERS = [
    {
        "id": "neh-1-4",
        "ref": "Nehemiah 1-4",
        "chapter_num": 1,
        "title": "The Cupbearer's Prayer and the Wall Begins: Faith and Opposition",
        "era": "walls_renewal",
        "type": "chapter",
        "themes": ["COV", "LAND", "PROV", "NATIONS"],

        "synopsis": "Nehemiah, cupbearer to King Artaxerxes I in Susa, receives devastating news: "
                    "'The remnant there in the province who had survived the exile is in great trouble "
                    "and shame. The wall of Jerusalem is broken down, and its gates are destroyed by "
                    "fire' (1:3). His response is immediate: weeping, mourning, fasting, and prayer. "
                    "Nehemiah's prayer (1:5-11) is a model of covenant reasoning: he confesses Israel's "
                    "sin, appeals to YHWH's promises to Moses (Deut 30:1-5), and asks for favor before "
                    "the king. When the opportunity comes, Nehemiah requests leave to rebuild. Artaxerxes "
                    "grants permission and provides letters of safe passage and timber from the royal "
                    "forest. Nehemiah arrives in Jerusalem, secretly surveys the ruined walls at night "
                    "(2:11-16), and rallies the people: 'You see the trouble we are in... Come, let us "
                    "build the wall of Jerusalem' (2:17). The people respond: 'Let us rise up and build!' "
                    "(2:18). But opposition comes immediately from Sanballat the Horonite, Tobiah the "
                    "Ammonite, and Geshem the Arab, who mock and threaten. Chapter 3 records the "
                    "organized effort: each family, guild, and district takes responsibility for a section "
                    "of wall. Chapter 4 intensifies the conflict as enemies plot attack, and Nehemiah "
                    "arms the workers: 'those who carried burdens were loaded in such a way that each "
                    "labored on the work with one hand and held his weapon with the other' (4:17).",

        "key_verse": {
            "ref": "Nehemiah 2:18",
            "text": "And I told them of the hand of my God that had been upon me for good, and also of the words that the king had spoken to me. And they said, 'Let us rise up and build.' So they strengthened their hands for the good work.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "mashqeh (cupbearer -- Nehemiah's position; not merely a servant but a trusted royal advisor who tested the king's wine for poison; a position of extreme trust and influence)",
            "yad-elohay hatovah (the hand of my God for good -- Nehemiah's recurring testimony; divine providence expressed as God's active hand directing events)",
            "chomah (wall -- the physical wall of Jerusalem, but theologically a symbol of identity, protection, and divine commitment to Zion)",
            "charaq shinnayim (gnashing teeth -- the enemies' frustrated rage at the wall's progress; opposition intensifies as God's work advances)"
        ],

        "ane_backdrop": "City walls in the ancient Near East were more than military fortifications -- "
                        "they were statements of identity and legitimacy. An unwalled city was not a city "
                        "at all in ANE terms; it was a village, a settlement without legal standing. "
                        "Jerusalem without walls was a theological scandal: YHWH's chosen city reduced "
                        "to a ruin. Rebuilding the wall reestablished Jerusalem's status as a legitimate "
                        "provincial capital. The opposition from Sanballat (governor of Samaria), Tobiah "
                        "(Ammonite official), and Geshem (Arab leader) reflects the political reality: "
                        "a fortified Jerusalem threatened their regional influence. The Elephantine Papyri "
                        "confirm Sanballat's historical existence and his position as a powerful regional "
                        "figure.",

        "second_temple": [
            {
                "source": "Sirach (Ben Sira) 49:13",
                "summary": "Ben Sira praises Nehemiah: 'The memory of Nehemiah also is lasting; he "
                           "raised up for us the walls that had fallen, and set up the gates and bars "
                           "and rebuilt our ruined houses.'",
                "relevance": "The Second Temple community remembered Nehemiah primarily as the wall "
                             "builder -- the practical leader who restored Jerusalem's physical integrity."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 30:1-5", "note": "Moses' prophecy of restoration after exile -- the promise Nehemiah appeals to in his prayer (1:8-9)", "type": "ot"},
            {"ref": "Psalm 51:18", "note": "'Do good to Zion in your good pleasure; build up the walls of Jerusalem' -- the psalmist's prayer fulfilled in Nehemiah's work", "type": "ot"},
            {"ref": "Psalm 147:2", "note": "'The LORD builds up Jerusalem; he gathers the outcasts of Israel' -- the theological framework for Nehemiah's mission", "type": "ot"},
            {"ref": "Isaiah 49:16", "note": "'I have engraved you on the palms of my hands; your walls are continually before me' -- YHWH's commitment to Jerusalem's walls", "type": "ot"},
            {"ref": "Isaiah 62:6-7", "note": "'On your walls, O Jerusalem, I have set watchmen' -- the restored wall as a sign of God's renewed attention to Zion", "type": "ot"},
            {"ref": "Revelation 21:12-14", "note": "The new Jerusalem has walls with twelve gates and twelve foundations -- the eschatological fulfillment of what Nehemiah rebuilt", "type": "nt"}
        ],

        "divine_council_note": "Nehemiah's repeated references to 'the hand of my God' (2:8, 18) being upon "
                               "him for good describe divine council protection in action. The 'hand of God' "
                               "in the Hebrew Bible is the visible expression of YHWH's invisible governance -- "
                               "the council's will manifested in historical events. The opposition from "
                               "Sanballat, Tobiah, and Geshem -- representing Samaria, Ammon, and Arabia "
                               "respectively -- may reflect the Deuteronomy 32 framework: these nations are "
                               "under the governance of allotted divine beings, and their opposition to "
                               "Jerusalem's restoration is the earthly expression of spiritual resistance "
                               "to YHWH's reclamation of his territory and people.",

        "sections": [
            {
                "heading": "Bad News in Susa and the Cupbearer's Prayer (Neh 1:1-11)",
                "body": "Nehemiah receives the report from his brother Hanani about Jerusalem's desolation "
                        "in the month of Kislev (November-December), 445 BC. His response is not immediate "
                        "action but sustained prayer and fasting 'for days' (1:4). His prayer (1:5-11) is a "
                        "masterclass in covenant reasoning: (1) He addresses YHWH as the covenant-keeping God "
                        "(1:5). (2) He confesses Israel's sins honestly, including his own family's (1:6-7). "
                        "(3) He quotes YHWH's own promise back to him: 'Remember the word that you commanded "
                        "your servant Moses: If you are unfaithful, I will scatter you among the peoples, "
                        "but if you return to me and keep my commandments and do them, though your outcasts "
                        "are in the uttermost parts of heaven, from there I will gather them and bring them "
                        "to the place that I have chosen, to make my name dwell there' (1:8-9, paraphrasing "
                        "Deut 30:1-5). (4) He asks for success 'today' -- the day he will speak to the king "
                        "(1:11). Prayer does not replace planning; it precedes and empowers it."
            },
            {
                "heading": "Before the King and the Night Survey (Neh 2:1-20)",
                "body": "Four months after hearing the news (Nisan/March-April), Nehemiah serves wine to "
                        "Artaxerxes. The king notices his sadness: 'Why is your face sad, seeing you are "
                        "not sick? This is nothing but sadness of the heart' (2:2). Nehemiah is 'very much "
                        "afraid' (2:2) -- showing sadness in the king's presence could be interpreted as "
                        "disloyalty. He explains about Jerusalem. The king asks: 'What are you requesting?' "
                        "Nehemiah's immediate response: 'So I prayed to the God of heaven' (2:4) -- a quick, "
                        "silent prayer before answering. This is Nehemiah's pattern throughout: pray in the "
                        "moment, then act. He requests leave, letters of safe passage, and timber from the "
                        "royal forest. 'The king granted me what I asked, for the good hand of my God was "
                        "upon me' (2:8). Arriving in Jerusalem, he secretly surveys the ruins by night "
                        "(2:12-16), assessing the damage before going public. Only then does he rally the "
                        "people: 'Let us rise up and build!' (2:18)."
            },
            {
                "heading": "All Hands on the Wall: Community Effort (Neh 3:1-32)",
                "body": "Chapter 3 is a detailed record of who rebuilt which section of the wall. The high "
                        "priest Eliashib and his fellow priests rebuild the Sheep Gate (3:1). Goldsmiths, "
                        "perfumers, district rulers, merchants, and even daughters of officials participate "
                        "(3:8, 12, 31-32). The only exception: 'The Tekoites repaired, but their nobles "
                        "would not stoop to serve their Lord' (3:5) -- a note of shame. This chapter is not "
                        "boring administrative record-keeping; it is a theological statement about communal "
                        "responsibility. Everyone has a section of wall. Everyone contributes. The wall is "
                        "not built by a contractor but by a community. The post-exilic community learns "
                        "that the work of God requires the participation of all God's people."
            },
            {
                "heading": "Building with a Sword: Opposition Intensifies (Neh 4:1-23)",
                "body": "Sanballat mocks: 'What are these feeble Jews doing?... Will they revive the stones "
                        "out of the heaps of rubbish, and burned ones at that?' (4:2). Tobiah adds: 'If a fox "
                        "goes up on what they are building, he will break down their stone wall!' (4:3). "
                        "Nehemiah's response is prayer: 'Hear, O our God, for we are despised' (4:4). When "
                        "mockery escalates to conspiracy ('they all plotted together to come and fight against "
                        "Jerusalem,' 4:8), Nehemiah responds with both prayer AND practical measures: 'We "
                        "prayed to our God and set a guard as a protection against them day and night' (4:9). "
                        "Workers carry loads with one hand and hold weapons with the other (4:17). A trumpeter "
                        "stands ready to sound the alarm. Nehemiah declares: 'Do not be afraid of them. "
                        "Remember the Lord, who is great and awesome, and fight for your brothers, your sons, "
                        "your daughters, your wives, and your homes' (4:14). The integration of faith and "
                        "action is total: remember the Lord AND fight."
            }
        ]
    },

    {
        "id": "neh-5-7",
        "ref": "Nehemiah 5-7",
        "chapter_num": 2,
        "title": "Economic Justice, Intrigue, and the Wall Completed in 52 Days",
        "era": "walls_renewal",
        "type": "chapter",
        "themes": ["LAW", "PROV", "NATIONS", "REVERSAL"],

        "synopsis": "The wall rebuilding faces internal as well as external challenges. Chapter 5 "
                    "reveals economic exploitation: wealthy Jews are charging their poorer kinsmen "
                    "interest and seizing their lands as collateral, driving families into debt slavery. "
                    "Nehemiah is furious: 'I was very angry when I heard their outcry and these words' "
                    "(5:6). He confronts the nobles and officials, abolishes the exploitative practices, "
                    "and sets the example himself by refusing the governor's food allowance for twelve "
                    "years (5:14-18). Chapter 6 records escalating intrigue: Sanballat and Tobiah try "
                    "to lure Nehemiah to a meeting (to assassinate him), hire a false prophet to "
                    "frighten him into the temple (to discredit him), and send intimidating letters. "
                    "Nehemiah sees through every plot: 'Should such a man as I run away? And what "
                    "man such as I could go into the temple and live? I will not go in' (6:11). The "
                    "wall is completed in 52 days (6:15). 'When all our enemies heard of it... they "
                    "perceived that this work had been accomplished with the help of our God' (6:16).",

        "key_verse": {
            "ref": "Nehemiah 6:15-16",
            "text": "So the wall was finished on the twenty-fifth day of the month Elul, in fifty-two days. And when all our enemies heard of it, all the nations around us were afraid and fell greatly in their own esteem, for they perceived that this work had been accomplished with the help of our God.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "neshek (interest/usury -- the practice Nehemiah abolishes; Torah prohibited charging interest to fellow Israelites, Exod 22:25, Lev 25:36-37)",
            "yir'ah (fear/reverence -- 'I did not do so, because of the fear of God' (5:15); Nehemiah's moral compass; the fear of God prevents exploitation)",
            "na'asu melacha (they accomplished the work -- the completion formula; the work is attributed both to the people's effort and to God's help)"
        ],

        "ane_backdrop": "Debt slavery was widespread in the ancient Near East and was periodically "
                        "addressed through royal 'misharum' (justice/equity) decrees that cancelled debts "
                        "and freed debt slaves. The Babylonian king Hammurabi's Code regulated interest "
                        "rates. Nehemiah's economic reform (ch. 5) functions as a covenant-based misharum: "
                        "he applies Torah's prohibition on Israelite-to-Israelite interest (Exod 22:25, "
                        "Lev 25:36-37) to correct economic injustice. The 52-day construction timeline is "
                        "remarkably short but plausible: the wall was being REPAIRED (using existing "
                        "foundations and fallen stones), not built from scratch, and the entire community "
                        "was mobilized.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 11.159-183",
                "summary": "Josephus retells Nehemiah's mission, confirming the opposition from Sanballat "
                           "and adding details about the political dynamics of the period.",
                "relevance": "Josephus provides independent confirmation of the historical setting and "
                             "political tensions described in Nehemiah."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 22:25", "note": "'If you lend money to any of my people with you who is poor, you shall not be like a moneylender to him, and you shall not exact interest from him' -- the Torah basis for Nehemiah's economic reform", "type": "ot"},
            {"ref": "Leviticus 25:35-37", "note": "The Sabbatical/Jubilee prohibition on charging interest to fellow Israelites -- the law Nehemiah enforces", "type": "ot"},
            {"ref": "Deuteronomy 23:19-20", "note": "No interest to brothers; interest permitted to foreigners -- the distinction Nehemiah applies", "type": "ot"},
            {"ref": "James 5:1-6", "note": "James condemns the rich who defraud laborers -- the same economic justice Nehemiah championed", "type": "nt"},
            {"ref": "Psalm 127:1", "note": "'Unless the LORD builds the house, those who build it labor in vain' -- the theology behind the enemies' recognition that 'this work was accomplished with the help of our God' (6:16)", "type": "nt"}
        ],

        "divine_council_note": "The enemies' recognition that the wall was completed 'with the help of our "
                               "God' (6:16) is a testimony from outside Israel to divine council governance. "
                               "The surrounding nations -- under the spiritual governance of allotted divine "
                               "beings (Deut 32:8-9) -- perceive that a power greater than human effort has "
                               "accomplished this work. Their fear is not merely political but spiritual: they "
                               "recognize the hand of Israel's God in the 52-day construction.",

        "sections": [
            {
                "heading": "Economic Justice: Nehemiah Confronts the Nobles (Neh 5:1-19)",
                "body": "Internal crisis erupts: 'There was a great outcry of the people and of their wives "
                        "against their Jewish brothers' (5:1). Some are mortgaging their fields and houses to "
                        "buy grain during famine (5:3). Others are borrowing money to pay the king's tax and "
                        "losing their children to debt slavery (5:5). Nehemiah is 'very angry' (5:6) and "
                        "confronts the nobles publicly: 'The thing that you are doing is not good. Ought you "
                        "not to walk in the fear of our God to prevent the taunts of the nations our enemies?' "
                        "(5:9). He demands: return the fields, vineyards, olive orchards, houses, and interest "
                        "(5:11). The nobles agree. Nehemiah then models servant leadership: for twelve years "
                        "as governor, he refuses the food allowance his predecessors demanded (5:14-15). "
                        "'Instead, I devoted myself to the work on this wall' (5:16). His prayer: 'Remember "
                        "for my good, O my God, all that I have done for this people' (5:19)."
            },
            {
                "heading": "Plots, Intrigues, and Nehemiah's Discernment (Neh 6:1-14)",
                "body": "Sanballat and Geshem invite Nehemiah to a meeting at Ono ('come and let us meet "
                        "together,' 6:2). Nehemiah sees the trap: 'They intended to do me harm' (6:2). His "
                        "reply: 'I am doing a great work and I cannot come down. Why should the work stop "
                        "while I leave it and come down to you?' (6:3). They send the invitation FOUR times; "
                        "he refuses four times. Then Sanballat sends an open letter accusing Nehemiah of "
                        "planning rebellion and setting himself up as king (6:6-7). Nehemiah denies it and "
                        "prays: 'Now, O God, strengthen my hands' (6:9). The final plot: Shemaiah, a hired "
                        "false prophet, urges Nehemiah to hide in the temple for safety. Nehemiah's response "
                        "reveals his discernment: 'Should such a man as I run away?... I perceived that God "
                        "had not sent him' (6:11-12). He recognizes false prophecy by its fruit: it produces "
                        "fear and flight, not faith and courage."
            },
            {
                "heading": "The Wall Completed: 52 Days That Changed Everything (Neh 6:15-7:73)",
                "body": "The wall is finished on Elul 25 (September-October) -- 52 days after construction "
                        "began (6:15). The theological significance of this speed is not lost on anyone: "
                        "'When all our enemies heard of it, all the nations around us were afraid and fell "
                        "greatly in their own esteem, for they perceived that this work had been accomplished "
                        "with the help of our God' (6:16). Even Israel's enemies recognize divine assistance. "
                        "Chapter 7 records the organization of the completed city: gatekeepers, singers, and "
                        "Levites are appointed (7:1). Nehemiah finds 'the book of the genealogy of those who "
                        "came up at the first' (7:5) -- the same census as Ezra 2. The wall defines a "
                        "community; the genealogy defines who belongs. Both are statements of identity: we "
                        "are a people with boundaries, with history, with a God who has brought us this far."
            }
        ]
    }
]
