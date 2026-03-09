"""
era_psalms_book3.py -- Psalms 73-89 (Book III): Asaph and Korah Collections

Book III is the DIVINE COUNCIL book of the Psalter. It contains the two most
explicit divine council texts in the Hebrew Bible's poetic literature: Psalm 82,
where God stands in the divine assembly and renders judgment against the corrupt
elohim who have failed to govern the nations justly, and Psalm 89, which
presents the heavenly council scene where YHWH's incomparability among the
"sons of God" (bene elim) is celebrated. Book III opens with the Asaphite
collection (Pss 73-83) and closes with the Korahite collection (Pss 84-88)
plus the Ethanite psalm (89). The Asaphite psalms are characterized by
historical recitals (Ps 78), cosmic battle mythology (Ps 74 -- Leviathan),
and the divine council judgment scene (Ps 82). Book III is framed by crisis:
it begins with the theodicy of Psalm 73 ("Why do the wicked prosper?") and
ends with the devastating lament of Psalm 89 ("Where is your steadfast love
of old?"). The Davidic covenant appears to have failed -- and the divine
council must answer for the state of the world.
"""

CHAPTERS = [
    {
        "id": "ps-73-74",
        "ref": "Psalms 73-74",
        "chapter_num": 1,
        "title": "Theodicy and Leviathan -- The Crisis of Faith and the Cosmic Battle",
        "era": "psalms_book3",
        "type": "chapter",

        "synopsis": "Book III opens with two psalms of crisis. Psalm 73, an Asaphite wisdom psalm, "
                    "confronts the prosperity of the wicked: 'My feet had almost stumbled... for I "
                    "was envious of the arrogant when I saw the prosperity of the wicked' (73:2-3). "
                    "The resolution comes in the sanctuary: 'I went into the sanctuary of God; then "
                    "I discerned their end' (73:17). The wicked are on slippery ground, destined for "
                    "destruction, while the psalmist possesses YHWH himself: 'Whom have I in heaven "
                    "but you? And there is nothing on earth that I desire besides you' (73:25). "
                    "Psalm 74 is a communal lament over the destruction of the temple: 'O God, why "
                    "do you cast us off forever?' (74:1). The enemies have 'set up their signs for "
                    "signs' (74:4) -- pagan symbols in the sacred space. The psalmist appeals to "
                    "YHWH's cosmic warrior identity: 'You divided the sea (yam) by your might; you "
                    "broke the heads of the sea monsters (tanninim) on the waters. You crushed the "
                    "heads of Leviathan (livyatan)' (74:13-14). The destruction of the temple is a "
                    "cosmic crisis requiring a cosmic response -- YHWH must defeat the chaos monster "
                    "once more.",

        "key_verse": {
            "ref": "Psalm 74:13-14",
            "text": "You divided the sea by your might; you broke the heads of the sea monsters on the waters. You crushed the heads of Leviathan; you gave him as food for the creatures of the wilderness.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Asaph (a Levitical musician and seer -- head of one of the three Levitical music guilds)",
            "tanninim (sea monsters/dragons -- the cosmic chaos creatures defeated by YHWH at creation)",
            "livyatan (Leviathan -- the multi-headed chaos sea dragon; cognate with Ugaritic Litanu/Lotan)",
            "yam (sea -- both the physical ocean and the personified chaos force; cognate with Ugaritic Yam)",
            "miqadash (sanctuary -- the holy place destroyed by the enemy; YHWH's earthly throne room)",
            "moed (meeting place/appointed time -- 'they burned all the meeting places of God in the land,' 74:8)",
            "ot (sign -- 'we do not see our signs,' 74:9; the absence of prophetic communication)"
        ],

        "ane_backdrop": "The Leviathan passage in Psalm 74:13-14 is one of the most direct parallels "
                        "between Israelite and Canaanite mythology in the Bible. In the Ugaritic Baal "
                        "Cycle (KTU 1.5.I.1-3), the god Mot describes how Baal 'struck Lotan (ltn), "
                        "the fleeing serpent, finished off the twisting serpent, the tyrant with seven "
                        "heads.' The parallels with Psalm 74 and Isaiah 27:1 are virtually exact: "
                        "Leviathan (livyatan) = Lotan (ltn); 'fleeing serpent' (nachash bariach, Isa "
                        "27:1) = 'fleeing serpent' (btn brh, KTU 1.5.I.1); 'twisting serpent' (nachash "
                        "'aqallaton) = 'twisting serpent' (btn 'qltn). The multi-headed feature ('heads "
                        "of Leviathan,' 74:14) matches the 'seven heads' of Ugaritic Lotan. But where "
                        "the Ugaritic texts attribute the victory to Baal, Israel's psalmist attributes "
                        "it to YHWH -- the true cosmic warrior who defeats chaos.",

        "second_temple": [
            {
                "source": "4 Ezra 6:49-52",
                "summary": "The apocalypse describes the creation of Leviathan and Behemoth on the "
                           "fifth day, preserved for the eschatological banquet.",
                "relevance": "Second Temple tradition preserved the cosmic monster traditions of Ps 74 "
                             "and developed them into eschatological expectations."
            },
            {
                "source": "Revelation 13:1",
                "summary": "'I saw a beast rising out of the sea, with ten horns and seven heads' -- "
                           "the sea beast of Revelation draws on the Leviathan tradition.",
                "relevance": "John's Apocalypse continues the Psalm 74 tradition: the chaos monster "
                             "rises from the sea and is ultimately defeated by the divine warrior."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 27:1", "note": "'In that day YHWH with his hard and great and strong sword will punish Leviathan the fleeing serpent, Leviathan the twisting serpent, and he will slay the dragon that is in the sea'", "type": "ot"},
            {"ref": "Job 41:1-34", "note": "YHWH's extended description of Leviathan -- the creature no human can tame but YHWH controls", "type": "ot"},
            {"ref": "Psalm 89:10", "note": "'You crushed Rahab like a carcass; you scattered your enemies with your mighty arm' -- the parallel chaos-monster victory in the same book", "type": "ot"},
            {"ref": "Revelation 13:1; 17:3", "note": "The seven-headed beast from the sea -- the eschatological Leviathan tradition", "type": "nt"},
            {"ref": "Genesis 1:21", "note": "'God created the great sea creatures (tanninim)' -- YHWH is creator, not rival, of the tanninim", "type": "ot"},
            {"ref": "Psalm 104:26", "note": "'There is Leviathan, which you formed to play in it' -- Leviathan as YHWH's plaything, not his adversary", "type": "ot"}
        ],

        "divine_council_note": "Psalm 74 invokes the cosmic battle tradition to protest the destruction "
                               "of the temple. The logic is profound: if YHWH defeated the chaos monsters "
                               "at creation (74:13-14), established day and night, summer and winter "
                               "(74:16-17), then why does he tolerate the destruction of his own "
                               "sanctuary? The temple was the cosmic center -- the place where YHWH's "
                               "heavenly throne room intersected with the earth. Its destruction is not "
                               "merely a political catastrophe but a cosmic one: it suggests that chaos "
                               "has won, that Leviathan has risen again. The lament 'we do not see our "
                               "signs; there is no longer any prophet, and there is none among us who "
                               "knows how long' (74:9) describes a divine council communication "
                               "breakdown -- the prophetic channel through which YHWH spoke to Israel "
                               "has gone silent. The signs (otot) that marked YHWH's presence and "
                               "purpose have been replaced by the enemy's signs (74:4). The psalmist's "
                               "appeal to the Leviathan victory is a plea for YHWH to re-engage the "
                               "cosmic battle: as he defeated chaos at the beginning, let him defeat "
                               "the chaos that has engulfed his people now. Psalm 73's resolution -- "
                               "'I went into the sanctuary of God; then I discerned their end' (73:17) "
                               "-- suggests that the sanctuary is the place where the divine council's "
                               "perspective becomes available to the human worshipper. In the sanctuary, "
                               "one sees as God sees.",

        "sections": [
            {
                "heading": "Who Is Asaph? The Prophetic Musician Behind Book III",
                "body": "Eleven psalms in Book III (Psalms 73-83) bear the superscription "
                        "<em>le'Asaph</em> ('of Asaph' or 'belonging to the Asaphite collection'). "
                        "Asaph was one of three Levitical musicians David appointed over the "
                        "worship of the Tabernacle (1 Chronicles 6:39; 16:4-5). The other two "
                        "were Heman and Ethan (also called Jeduthun). Together, these three men "
                        "and their descendants formed the three guilds of Temple musicians -- "
                        "the worship leaders of Israel for centuries.<br><br>"
                        "What makes Asaph distinctive is that he is called a <strong>seer</strong> "
                        "(<em>choze</em>) in 2 Chronicles 29:30 -- a title for a prophet. This "
                        "means Asaph was not merely a musician but a prophetic figure whose "
                        "compositions carried divine authority. The Asaphite psalms reflect this "
                        "prophetic character: they engage with history (Ps 78), cosmic battle "
                        "(Ps 74), and the divine council (Ps 82) in ways that go beyond personal "
                        "devotion to declare YHWH's sovereign purposes. Like the Sons of Korah, "
                        "the 'Sons of Asaph' refers to a guild of musicians descended from the "
                        "original Asaph who continued composing and performing psalms in his "
                        "tradition for generations."
            },
            {
                "heading": "Historical Context: 'The Temple in Ruins' -- Which Destruction?",
                "body": "Psalm 74 describes the destruction of the Temple in graphic detail: "
                        "'Your foes have roared in the midst of your meeting place... they set "
                        "your sanctuary on fire; they profaned the dwelling place of your name "
                        "to the ground' (74:4, 7). Readers may ask: which destruction is this?"
                        "<br><br>"
                        "Israel's Temple was destroyed twice in history: first by the "
                        "<strong>Babylonians under Nebuchadnezzar in 586 BC</strong>, and "
                        "second by the <strong>Romans under Titus in 70 AD</strong>. Psalm 74 "
                        "most likely refers to the Babylonian destruction -- the event that "
                        "ended the kingdom of Judah and sent the people into <strong>the Exile</strong> "
                        "(also called <strong>the Babylonian Captivity</strong>).<br><br>"
                        "To understand why this was so devastating, readers need the larger "
                        "historical context: After King Solomon's death (c. 930 BC), the united "
                        "kingdom of Israel split into two: the <strong>northern kingdom</strong> "
                        "(called 'Israel' or 'Ephraim,' with its capital at Samaria) and the "
                        "<strong>southern kingdom</strong> (called 'Judah,' with its capital at "
                        "Jerusalem). This event is known as <strong>the Divided Kingdom</strong>. "
                        "The northern kingdom was conquered and scattered by Assyria in 722 BC "
                        "(the 'ten lost tribes'). The southern kingdom survived another 136 years "
                        "until Babylon conquered it in 586 BC, destroying Solomon's Temple and "
                        "deporting the population to Babylon.<br><br>"
                        "<strong>The Exile</strong> lasted approximately 70 years (586-516 BC). "
                        "It was the defining trauma of Israel's national and spiritual history. "
                        "The Temple -- the place where YHWH had put his name, the intersection "
                        "of heaven and earth -- was a heap of rubble. The Davidic monarchy was "
                        "ended. The question that dominates Book III of the Psalter is born from "
                        "this crisis: if YHWH promised David an eternal throne, and the throne "
                        "lies in ruins, has YHWH broken his covenant? <strong>The Return</strong> "
                        "from exile began under the Persian king Cyrus (538 BC), who allowed "
                        "the Jews to go back to Jerusalem and rebuild the Temple (the Second "
                        "Temple, completed 516 BC). But the restored community lived under "
                        "foreign rule -- Persian, then Greek, then Roman -- and the Davidic king "
                        "never returned to the throne. The psalms of Book III capture the anguish "
                        "of that unanswered promise."
            },
            {
                "heading": "Psalm 73: The Sanctuary Revelation (73:1-28)",
                "body": "'Truly God is good to Israel, to those who are pure in heart' (73:1). "
                        "This thesis statement is immediately challenged by experience: 'But as "
                        "for me, my feet had almost stumbled... for I was envious of the arrogant "
                        "when I saw the prosperity (shalom) of the wicked' (73:2-3). The wicked "
                        "are described with devastating accuracy: they have no pangs in their "
                        "death, their bodies are sleek (73:4); 'pride is their necklace; violence "
                        "covers them as a garment' (73:6); 'they set their mouths against the "
                        "heavens' (73:9). The crisis deepens: 'All in vain have I kept my heart "
                        "clean' (73:13). The turning point is the sanctuary: 'When I thought how "
                        "to understand this, it seemed to me a wearisome task, until (ad) I went "
                        "into the sanctuary of God (miqdeshei-El); then I discerned their end' "
                        "(73:16-17). In the sanctuary -- YHWH's earthly throne room -- the "
                        "psalmist receives the divine council's perspective. The wicked are on "
                        "'slippery places' (chalaqot) set by God (73:18); they are 'like a dream "
                        "when one awakes' (73:20). The psalm culminates in ecstatic devotion: "
                        "'Whom have I in heaven but you? And there is nothing on earth that I "
                        "desire besides you. My flesh and my heart may fail, but God is the "
                        "strength of my heart and my portion (chelqi) forever' (73:25-26)."
            },
            {
                "heading": "Psalm 74: Leviathan and the Temple in Ruins (74:1-23)",
                "body": "'O God, why do you cast us off forever? Why does your anger smoke against "
                        "the sheep of your pasture?' (74:1). The temple has been destroyed: 'Your "
                        "foes have roared in the midst of your meeting place (moed); they set up "
                        "their signs for signs' (74:4). The axe-work of destruction is described "
                        "in painful detail: 'They hacked all the carved wood (pitucheiha) with "
                        "hatchets and hammers. They set your sanctuary on fire; they profaned "
                        "the dwelling place of your name to the ground' (74:6-7). The prophetic "
                        "silence is devastating: 'We do not see our signs (ototeinu); there is "
                        "no longer any prophet (navi), and there is none among us who knows how "
                        "long' (74:9). The appeal turns to creation mythology: 'Yet God my King is "
                        "from of old, working salvation in the midst of the earth. You divided "
                        "the sea (yam) by your might; you broke the heads of the sea monsters "
                        "(tanninim) on the waters. You crushed the heads of Leviathan; you gave "
                        "him as food for the creatures of the wilderness' (74:12-14). The "
                        "crushing of Leviathan's multiple heads parallels the seven-headed Lotan "
                        "of Ugaritic mythology -- but YHWH, not Baal, is the victor. The psalmist "
                        "then appeals to YHWH's sovereignty over all creation: 'Yours is the day, "
                        "yours also the night; you have established the heavenly lights and the "
                        "sun. You have fixed all the boundaries of the earth; you have made summer "
                        "and winter' (74:16-17). The God who set the boundaries of creation "
                        "must now enforce the boundaries of his covenant."
            }
        ]
    },

    {
        "id": "ps-78",
        "ref": "Psalm 78",
        "chapter_num": 2,
        "title": "The Great Historical Recital -- Israel's Failure and YHWH's Faithfulness",
        "era": "psalms_book3",
        "type": "chapter",

        "synopsis": "Psalm 78 is the longest Asaphite psalm and one of the great historical recitals "
                    "of the Psalter. It traces Israel's history from the exodus through the "
                    "wilderness to the election of David and Zion, with an unflinching account of "
                    "Israel's repeated rebellion and YHWH's corresponding faithfulness. The psalm "
                    "opens as a wisdom instruction: 'I will open my mouth in a parable (mashal); "
                    "I will utter dark sayings (chidot) from of old' (78:2 -- quoted in Matt 13:35). "
                    "The 'dark sayings' are the hidden pattern of Israel's history: rebellion, "
                    "judgment, mercy, rebellion again. The plagues of Egypt, the wilderness "
                    "provisions (manna, quail, water from the rock), the conquest, and the tribal "
                    "failures are all recounted. The theological climax is YHWH's choice of Judah "
                    "over Ephraim, Zion over Shiloh, and David as the shepherd-king: 'He chose "
                    "David his servant and took him from the sheepfolds' (78:70).",

        "key_verse": {
            "ref": "Psalm 78:2",
            "text": "I will open my mouth in a parable; I will utter dark sayings from of old.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "mashal (parable/proverb -- a wisdom discourse that reveals hidden meaning in familiar events)",
            "chidot (dark sayings/riddles -- enigmatic truths that require discernment to understand)",
            "pelei (wonders/marvels -- the miraculous acts of YHWH that Israel repeatedly forgot)",
            "Ephrayim (Ephraim -- the northern tribe that failed; representative of Israel's apostasy)",
            "Shiloh (the pre-Jerusalem sanctuary that YHWH abandoned because of Israel's sin)",
            "mishkan (tabernacle/dwelling -- the tent of meeting at Shiloh, later at Zion)",
            "ro'eh (shepherd -- David as the shepherd-king, caring for Israel as his flock)"
        ],

        "ane_backdrop": "Historical recitals are a feature of ANE treaty literature. The Hittite "
                        "suzerainty treaties include a 'historical prologue' that recounts the "
                        "suzerain's past benefits to the vassal, establishing the basis for the "
                        "vassal's obligation. Psalm 78 functions as Israel's historical prologue: "
                        "YHWH's mighty acts on behalf of Israel establish the basis for obedience. "
                        "The pattern of rebellion-judgment-mercy parallels the Mesopotamian genre "
                        "of 'city laments' where the destruction of a city is attributed to divine "
                        "anger provoked by human sin, followed by restoration.",

        "second_temple": [
            {
                "source": "Matthew 13:35",
                "summary": "Matthew quotes Psalm 78:2 as fulfilled in Jesus' teaching in parables: "
                           "'I will open my mouth in parables; I will utter what has been hidden "
                           "since the foundation of the world.'",
                "relevance": "The evangelists understood Jesus' parabolic teaching as the fulfillment "
                             "of the Asaphite wisdom tradition -- the hidden pattern of God's purposes "
                             "revealed through story."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 13:35", "note": "Jesus fulfills Ps 78:2 by speaking in parables -- uttering things hidden from the foundation of the world", "type": "nt"},
            {"ref": "1 Samuel 4:1-11", "note": "The capture of the ark at Shiloh -- the event Ps 78:60-61 references: 'He forsook his dwelling at Shiloh'", "type": "ot"},
            {"ref": "Jeremiah 7:12-14", "note": "Jeremiah warns the temple will share Shiloh's fate -- the same warning embedded in Ps 78", "type": "ot"},
            {"ref": "1 Corinthians 10:1-11", "note": "Paul recounts the wilderness failures as 'examples for us' -- the same pedagogical use of history as Ps 78", "type": "nt"},
            {"ref": "2 Samuel 7:8", "note": "'I took you from the pasture, from following the sheep' -- YHWH's election of David, echoed in 78:70", "type": "ot"},
            {"ref": "Nehemiah 9:5-38", "note": "The post-exilic historical recital prayer -- the same genre as Ps 78", "type": "ot"}
        ],

        "divine_council_note": "Psalm 78 reveals the divine council's governance of Israel's history "
                               "through the pattern of rebellion, judgment, and restoration. YHWH does "
                               "not abandon his people even when they test him repeatedly in the "
                               "wilderness: 'Yet he, being compassionate, atoned for their iniquity and "
                               "did not destroy them; he restrained his anger often and did not stir up "
                               "all his wrath. He remembered that they were but flesh, a wind (ruach) "
                               "that passes and comes not again' (78:38-39). The divine council's mercy "
                               "overrides its justice. The abandonment of Shiloh (78:60) is a council "
                               "decision: YHWH 'forsook his dwelling (mishkan) at Shiloh, the tent "
                               "where he dwelt among mankind. He delivered his power (uz) to captivity, "
                               "his glory (tiferet) to the hand of the foe' (78:60-61). The ark -- "
                               "YHWH's throne -- was given over to the Philistines. But the council's "
                               "purpose was not abandonment but redirection: 'He chose the tribe of "
                               "Judah, Mount Zion, which he loves' (78:68). The transfer from Ephraim/ "
                               "Shiloh to Judah/Zion is a divine council realignment -- YHWH relocates "
                               "his earthly throne from the failed northern sanctuary to the chosen "
                               "southern mountain. David is then selected as the human regent: 'He "
                               "chose David his servant and took him from the sheepfolds... to shepherd "
                               "Jacob his people, Israel his inheritance (nachalatoh)' (78:70-71).",

        "sections": [
            {
                "heading": "The Wisdom Framework and the Exodus Wonders (78:1-31)",
                "body": "The psalm opens as a wisdom instruction: 'Give ear, O my people, to my "
                        "teaching (torati); incline your ears to the words of my mouth' (78:1). "
                        "The purpose is intergenerational transmission: 'We will not hide them "
                        "from their children, but tell to the coming generation the glorious "
                        "deeds of YHWH, and his might, and the wonders that he has done' (78:4). "
                        "The historical recital begins with the plagues of Egypt: 'He turned "
                        "their rivers to blood... sent swarms of flies... gave their crops to "
                        "the destroying locust' (78:44-46). The exodus follows: 'He divided the "
                        "sea and let them pass through it, and made the waters stand like a heap "
                        "(ned)' (78:13). In the wilderness, YHWH provided abundantly: 'He split "
                        "rocks in the wilderness and gave them drink... He commanded the skies "
                        "above and opened the doors of heaven, and he rained down on them manna "
                        "to eat and gave them the grain of heaven' (78:15, 23-24). Yet even amid "
                        "miracle provision, 'they sinned still more against him, rebelling against "
                        "the Most High (Elyon) in the desert' (78:17). The title Elyon -- the "
                        "divine council designation of YHWH as supreme God -- is used deliberately: "
                        "Israel's rebellion is not merely against a national deity but against the "
                        "cosmic sovereign. YHWH's anger blazed, yet he continued to provide."
            },
            {
                "heading": "From Shiloh to Zion -- The Divine Relocation (78:56-72)",
                "body": "The psalm reaches its climactic section with the failure of the northern "
                        "sanctuary: 'Yet they tested and rebelled against the Most High God (Elohim "
                        "Elyon) and did not keep his testimonies, but turned away and acted "
                        "treacherously like their fathers' (78:56-57). They 'provoked him to anger "
                        "with their high places; they moved him to jealousy with their idols' "
                        "(78:58). YHWH's response is devastating: 'He forsook his dwelling at "
                        "Shiloh (mishkan Shiloh), the tent where he dwelt among mankind. He "
                        "delivered his power (uzo) to captivity, his glory (tifareto) to the hand "
                        "of the foe' (78:60-61). The 'power' and 'glory' are references to the "
                        "ark of the covenant. The ark's capture by the Philistines (1 Sam 4) was "
                        "the loss of YHWH's visible throne from Israel. Then the turn: 'Then the "
                        "Lord awoke as from sleep, like a strong man shouting because of wine. "
                        "And he put his adversaries to rout' (78:65-66). YHWH chose a new center: "
                        "'He rejected the tent of Joseph; he did not choose the tribe of Ephraim, "
                        "but he chose the tribe of Judah, Mount Zion, which he loves' (78:67-68). "
                        "'He chose David his servant (avdo) and took him from the sheepfolds; from "
                        "following the nursing ewes he brought him to shepherd Jacob his people, "
                        "Israel his inheritance (nachalato). With upright heart he shepherded "
                        "them and guided them with his skillful hand' (78:70-72)."
            }
        ]
    },

    {
        "id": "ps-82",
        "ref": "Psalm 82",
        "chapter_num": 3,
        "title": "The Divine Council Judgment -- God Stands Among the Gods",
        "era": "psalms_book3",
        "type": "chapter",

        "synopsis": "Psalm 82 is THE divine council text of the Old Testament -- the passage where "
                    "the veil between heaven and earth is drawn back and the reader witnesses YHWH "
                    "standing in the divine assembly, pronouncing judgment on the corrupt elohim "
                    "who have failed to govern the nations with justice. 'God (Elohim) has taken "
                    "his place in the divine council (adat-El); in the midst of the gods (elohim) "
                    "he holds judgment' (82:1). The accused gods are charged with injustice: 'How "
                    "long will you judge unjustly and show partiality to the wicked?' (82:2). They "
                    "were given authority over the nations (the Deuteronomy 32:8 allotment), but "
                    "they have failed. YHWH's sentence is devastating: 'I said, You are gods (elohim "
                    "attem), sons of the Most High (bene Elyon), all of you; nevertheless, like men "
                    "(ke'adam) you shall die, and fall like any prince (sarim)' (82:6-7). The psalm "
                    "closes with a plea that echoes the eschatological hope of the entire Bible: "
                    "'Arise, O God (Elohim), judge the earth! For you shall inherit all the "
                    "nations!' (82:8).",

        "key_verse": {
            "ref": "Psalm 82:1, 6-7",
            "text": "God has taken his place in the divine council; in the midst of the gods he holds judgment. ... I said, 'You are gods, sons of the Most High, all of you; nevertheless, like men you shall die, and fall like any prince.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "adat-El (congregation/assembly of God -- the divine council; the heavenly court where YHWH presides)",
            "elohim (gods -- used for both the presiding God and the subordinate divine beings being judged)",
            "bene Elyon (sons of the Most High -- the divine council members; the same class as bene elohim)",
            "nitsav (to stand/take one's place -- YHWH rises to pronounce judgment; a courtroom posture)",
            "shaphat (to judge -- YHWH's judicial function in the council; the charge against the corrupt gods)",
            "ke'adam (like men/like Adam -- the sentence of mortality imposed on the divine beings)",
            "sarim (princes/rulers -- the gods will fall like human rulers; possibly 'angelic princes')",
            "nachal (to inherit -- YHWH will inherit all nations, reversing the Deut 32 allotment)"
        ],

        "ane_backdrop": "The divine council is a thoroughly attested ANE concept. In Ugaritic texts, "
                        "the 'assembly of the sons of El' (phr bn 'ilm) or the 'council of El' (dt "
                        "'ilm) meets to deliberate cosmic affairs. El, the head of the Canaanite "
                        "pantheon, presides over a council of deities who govern various domains. In "
                        "Mesopotamia, the assembly of the great gods (puhur ilani rabuti) makes "
                        "decisions about creation, the flood, and the fate of humanity. The Enuma "
                        "Elish describes the assembly of gods deliberating Marduk's elevation as "
                        "supreme deity. In every case, the council has a supreme deity who presides "
                        "and subordinate deities who serve. Psalm 82 adopts this framework entirely "
                        "but with a radical Israelite twist: the subordinate elohim have FAILED in "
                        "their assigned governance, and YHWH -- the true supreme deity -- sentences "
                        "them to mortality. In the ANE parallels, gods do not die (with rare "
                        "exceptions like the Ugaritic Mot and Baal cycle). Psalm 82's sentence of "
                        "death on divine beings is theologically revolutionary: it strips the gods "
                        "of the one attribute that distinguishes them from humans -- immortality.",

        "second_temple": [
            {
                "source": "John 10:34-36",
                "summary": "Jesus quotes Psalm 82:6 in his defense against the charge of blasphemy: "
                           "'Is it not written in your Law, I said, you are gods? If he called them "
                           "gods to whom the word of God came -- and Scripture cannot be broken -- "
                           "do you say of him whom the Father consecrated and sent into the world, "
                           "You are blaspheming, because I said, I am the Son of God?'",
                "relevance": "Jesus' argument is a fortiori: if the elohim of Psalm 82 could be "
                             "called 'gods' by divine decree, how much more can the one whom the "
                             "Father sent claim divine sonship? The passage presupposes the divine "
                             "council reading of Psalm 82."
            },
            {
                "source": "11QMelchizedek (11Q13)",
                "summary": "This Qumran text interprets Psalm 82:1-2 as referring to Melchizedek's "
                           "role as the eschatological judge of Belial and the spirits of his lot. "
                           "The 'elohim' of 82:1 who presides is identified as Melchizedek; the "
                           "'elohim' being judged are the fallen angels.",
                "relevance": "The Dead Sea Scrolls community read Psalm 82 as describing a future "
                             "cosmic judgment scene where a divine figure (Melchizedek) judges the "
                             "rebellious spiritual powers -- confirming the supernatural reading of "
                             "the 'elohim' and anticipating the eschatological reversal of 82:8."
            },
            {
                "source": "Targum on Psalm 82:1",
                "summary": "The Targum renders the verse: 'God, in the assembly of the righteous "
                           "who are mighty in Torah, the divine presence (shekhinta) of God judges.' "
                           "This reading identifies the 'gods' as human judges.",
                "relevance": "The Targumic tradition reflects the later rabbinic tendency to "
                             "de-supernaturalize the 'elohim' -- a reading that conflicts with the "
                             "Qumran evidence and the ANE divine council background."
            },
            {
                "source": "Jubilees 15:31-32",
                "summary": "Jubilees describes how God appointed spirits (angels) to rule over "
                           "the nations, 'but over Israel he did not appoint any angel or spirit, "
                           "for he alone is their ruler.'",
                "relevance": "Jubilees preserves the Deuteronomy 32:8 / Psalm 82 tradition: the "
                             "nations were placed under angelic governance, while Israel remained "
                             "under YHWH's direct authority."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9", "note": "'When the Most High (Elyon) gave to the nations their inheritance... he fixed the borders of the peoples according to the number of the sons of God (bene elohim). But YHWH's portion is his people' -- the allotment Psalm 82 presupposes", "type": "ot"},
            {"ref": "John 10:34-36", "note": "Jesus quotes Ps 82:6 ('I said, you are gods') to defend his claim to divine sonship -- a fortiori argument from the divine council", "type": "nt"},
            {"ref": "Daniel 10:13, 20-21", "note": "The 'prince of Persia' and 'prince of Greece' -- territorial spiritual rulers corresponding to the elohim of Ps 82", "type": "ot"},
            {"ref": "1 Kings 22:19-23", "note": "Micaiah's vision of the divine council in session -- YHWH enthroned with the host of heaven, deliberating", "type": "ot"},
            {"ref": "Psalm 89:5-7", "note": "'Who in the skies can be compared to YHWH? Who among the sons of God (bene elim) is like YHWH? A God greatly to be feared in the council of the holy ones' -- the companion divine council text", "type": "ot"},
            {"ref": "Isaiah 24:21-22", "note": "'On that day YHWH will punish the host of heaven, in heaven, and the kings of the earth, on the earth. They will be gathered together as prisoners' -- the eschatological fulfillment of Ps 82's judgment", "type": "ot"},
            {"ref": "1 Corinthians 6:3", "note": "'Do you not know that we are to judge angels?' -- the saints participating in the judgment of the corrupt spiritual powers", "type": "nt"},
            {"ref": "Ephesians 6:12", "note": "'We do not wrestle against flesh and blood, but against rulers, against authorities, against cosmic powers' -- the NT identification of the Ps 82 elohim as hostile spiritual forces", "type": "nt"},
            {"ref": "Psalm 58:1-2", "note": "'Do you indeed decree what is right, you gods (elim)? Do you judge the children of man uprightly?' -- a parallel indictment of unjust divine beings", "type": "ot"},
            {"ref": "Genesis 11:1-9", "note": "The Babel dispersion -- the event that led to the Deut 32:8 allotment that Ps 82 revisits", "type": "ot"},
            {"ref": "Isaiah 34:4", "note": "'All the host of heaven shall rot away' -- the most extreme fulfillment of Ps 82:7 ('you shall die like men'): the divine council members are not merely judged but dissolved", "type": "ot"},
            {"ref": "Colossians 2:15", "note": "'He disarmed the rulers and authorities and put them to open shame, triumphing over them in him' -- Christ executes the Psalm 82 verdict on the cross", "type": "nt"},
            {"ref": "1 Enoch 10:4-6, 11-14", "note": "YHWH commands the binding of Azazel and the Watchers -- the Enochic tradition elaborates the imprisonment of the elohim judged in Ps 82", "type": "dss"}
        ],

        "divine_council_note": "Psalm 82 is the single most important divine council text in the "
                               "Hebrew Bible. Its theology unfolds in four movements: (1) THE SETTING: "
                               "'God (Elohim) has taken his place (nitsav) in the divine council "
                               "(adat-El); in the midst of the gods (elohim) he holds judgment "
                               "(yishpot)' (82:1). The supreme God stands -- the judicial posture of "
                               "one rising to pronounce verdict -- in the assembly of the subordinate "
                               "gods. The word adat-El means 'assembly/congregation of God' and is the "
                               "Israelite equivalent of the Ugaritic phr bn 'ilm ('assembly of the sons "
                               "of El'). (2) THE INDICTMENT: 'How long will you judge unjustly and show "
                               "partiality to the wicked?' (82:2). The gods were given authority over "
                               "the nations (Deut 32:8), but they have used that authority to promote "
                               "injustice. The charges continue: 'Give justice to the weak and the "
                               "fatherless; maintain the right of the afflicted and the destitute. "
                               "Rescue the weak and the needy; deliver them from the hand of the wicked' "
                               "(82:3-4). The gods were supposed to govern the nations according to "
                               "YHWH's justice, but they allowed (or promoted) oppression. (3) THE "
                               "DIAGNOSIS: 'They have neither knowledge nor understanding, they walk "
                               "about in darkness; all the foundations of the earth are shaken' (82:5). "
                               "The gods' failure is cognitive and moral -- they lack the knowledge "
                               "(da'at) and understanding (binah) that YHWH possesses. And their failure "
                               "has cosmic consequences: the very foundations (mosdei) of the earth are "
                               "destabilized. When the governing spiritual powers are corrupt, the "
                               "created order itself trembles. (4) THE SENTENCE: 'I said (ani amarti), "
                               "You are gods (elohim attem), sons of the Most High (bene Elyon), all "
                               "of you; nevertheless (akhen), like men (ke'adam) you shall die, and "
                               "fall like any prince (ke'achad hasarim)' (82:6-7). The sentence is "
                               "mortality -- the one thing that separated elohim from adam is removed. "
                               "The gods who governed like tyrants will die like tyrants. The word "
                               "ke'adam may also echo 'like Adam' -- as Adam fell from his position in "
                               "Eden through disobedience, so the gods will fall from their position in "
                               "the council. The final plea of 82:8 is the eschatological cry of the "
                               "faithful: 'Arise (qumah), O God, judge (shafta) the earth! For you "
                               "shall inherit (tinchal) all the nations!' The verb nachal ('to inherit') "
                               "is the reversal of Deuteronomy 32:8-9: YHWH will no longer delegate "
                               "governance of the nations to subordinate elohim. He will take back "
                               "direct authority over all nations, not just Israel. This is the "
                               "theological foundation for the Great Commission, the ingathering of "
                               "the Gentiles, and the universal reign of YHWH's Messiah.",

        "sections": [
            {
                "heading": "The Council Convenes: God Stands Among the Gods (82:1)",
                "body": "'Elohim nitsav ba'adat-El; beqerev elohim yishpot' -- 'God has taken his "
                        "place in the divine council; in the midst of the gods he holds judgment' "
                        "(82:1). This single verse is the most compressed divine council scene in "
                        "Scripture. The first Elohim is the supreme God -- YHWH, the Most High -- "
                        "who 'stands' (nitsav) in the assembly. The verb nitsav in a judicial "
                        "context indicates one who rises to deliver a verdict (cf. Isa 3:13: 'YHWH "
                        "has taken his place to contend; he stands to judge peoples'). The adat-El "
                        "is the 'assembly of God' -- the divine council where the elohim gather "
                        "before YHWH's throne. The second elohim (lowercase in intent) refers to "
                        "the members of this assembly -- the subordinate divine beings who have "
                        "been given authority over the nations. The word elohim in Hebrew is not "
                        "a title reserved for YHWH alone; it is a nature term meaning 'divine "
                        "being, inhabitant of the spiritual realm.' All members of the council "
                        "are elohim by nature; YHWH is unique among them as the Most High, the "
                        "uncreated creator, the sovereign over all other elohim. The scene is a "
                        "courtroom: YHWH is both the presiding judge and the plaintiff. The "
                        "defendants are the gods of the nations."
            },
            {
                "heading": "The Indictment: Cosmic Injustice (82:2-5)",
                "body": "'How long (ad-matai) will you judge unjustly (tishpetu-avel) and show "
                        "partiality (pene resha'im tis'u) to the wicked?' (82:2). The phrase "
                        "'ad-matai' ('how long?') implies that this injustice has been ongoing "
                        "for an extended period -- the gods have been failing in their governance "
                        "since the Deuteronomy 32:8 allotment. The specific charges follow: "
                        "'Give justice (shiftu) to the weak (dal) and the fatherless (yatom); "
                        "maintain the right (hatsdiku) of the afflicted (ani) and the destitute "
                        "(rash). Rescue the weak and the needy (evyon); deliver them from the "
                        "hand of the wicked' (82:3-4). These are the same categories of "
                        "vulnerable people that YHWH himself champions throughout the OT (Exod "
                        "22:22-24; Deut 10:17-19; Ps 68:5). The gods were supposed to ensure "
                        "justice for these groups within the nations they governed. Instead, they "
                        "allowed -- or enabled -- the wicked to oppress them. The diagnosis is "
                        "devastating: 'They have neither knowledge (yad'u) nor understanding "
                        "(yavinu), they walk about in darkness (bachasheikhah yithalakhu); all "
                        "the foundations of the earth are shaken (yimmotu kol mosdei erets)' "
                        "(82:5). The darkness is moral and spiritual blindness. The shaking of "
                        "the earth's foundations is the cosmic consequence of the council's "
                        "corruption: when the spiritual governors are unjust, the physical "
                        "creation destabilizes. The connection between spiritual governance "
                        "and cosmic order is fundamental to biblical theology."
            },
            {
                "heading": "The Sentence: Gods Shall Die Like Men (82:6-7)",
                "body": "'I said (ani amarti), You are gods (elohim attem), sons of the Most "
                        "High (bene Elyon), all of you (kullekhem)' (82:6). The 'I said' is "
                        "YHWH's own declaration -- he is the one who originally designated these "
                        "beings as elohim and bene Elyon. The titles are real, not metaphorical: "
                        "these are genuine divine beings, members of the heavenly council, sons "
                        "of the Most High by nature or appointment. The title 'bene Elyon' "
                        "connects directly to Deuteronomy 32:8-9, where the 'Most High' (Elyon) "
                        "allotted the nations according to the number of the 'sons of God' (bene "
                        "elohim, in the DSS/LXX reading). These are the same beings. But the "
                        "sentence follows with devastating force: 'Nevertheless (akhen), like "
                        "men (ke'adam) you shall die (temutun), and fall like any prince "
                        "(ke'achad hasarim tippolu)' (82:7). The word akhen is an adversative "
                        "particle that introduces a sharp contrast: despite your divine status, "
                        "you will experience the one thing that was supposed to be impossible "
                        "for elohim -- death. The phrase ke'adam ('like men' or 'like Adam') "
                        "strips them of their distinguishing attribute. The gods will die as "
                        "humans die. The phrase ke'achad hasarim ('like any prince') may mean "
                        "'like one of the [human] princes' or 'like one of the [angelic] "
                        "princes' -- both readings reinforce the judgment. This is the only "
                        "passage in the Hebrew Bible where divine beings are sentenced to "
                        "death by the supreme God. It is the theological precursor to the "
                        "eschatological judgment of spiritual powers in Isaiah 24:21-22, "
                        "Daniel 10, and Revelation 20."
            },
            {
                "heading": "The Eschatological Cry: Arise, O God! (82:8)",
                "body": "'Arise (qumah), O God (Elohim), judge (shaftah) the earth (ha'arets)! "
                        "For you shall inherit (tinchal) all the nations (kol-haggoyim)!' (82:8). "
                        "This single verse is the Psalter's most concentrated eschatological "
                        "statement. The verb qumah ('arise') is the same verb used for YHWH "
                        "arising against his enemies in Psalm 68:1 and Numbers 10:35 -- the "
                        "divine warrior rising to act. The verb shaftah ('judge') means not "
                        "merely to render verdict but to set things right -- to govern with "
                        "justice, to restore order. The critical verb is tinchal ('you shall "
                        "inherit'). Under the Deuteronomy 32:8-9 dispensation, YHWH inherited "
                        "only Israel (Jacob) as his nachalah while the other nations were "
                        "allotted to the sons of God. Psalm 82:8 prays for the reversal of "
                        "this arrangement: YHWH will inherit ALL the nations. The corrupt "
                        "elohim will be stripped of their authority, and YHWH will take direct "
                        "governance over every people. This is the Old Testament foundation for "
                        "the New Testament's proclamation that in Christ, the nations are being "
                        "reclaimed from hostile spiritual powers. Colossians 2:15 describes "
                        "Christ 'disarming the rulers and authorities and putting them to open "
                        "shame, by triumphing over them' -- the execution of the Psalm 82 "
                        "sentence. The Great Commission (Matt 28:18-20) is the practical "
                        "outworking of Psalm 82:8: 'All authority in heaven and on earth has "
                        "been given to me. Go therefore and make disciples of all nations.' "
                        "YHWH is inheriting the nations through his Son."
            }
        ]
    },

    {
        "id": "ps-83",
        "ref": "Psalm 83",
        "chapter_num": 4,
        "title": "The Conspiracy of Nations -- Territorial Spirits and Earthly Proxies",
        "era": "psalms_book3",
        "type": "chapter",

        "synopsis": "Psalm 83 is the final Asaphite psalm and describes a conspiracy of nations "
                    "seeking to annihilate Israel: 'They say, Come, let us wipe them out as a "
                    "nation; let the name of Israel be remembered no more!' (83:4). The conspiracy "
                    "includes ten peoples: Edom, the Ishmaelites, Moab, the Hagrites, Gebal, Ammon, "
                    "Amalek, Philistia, Tyre, and Assyria. The psalm appeals for divine intervention "
                    "by recalling past victories (Sisera, Jabin, Midian) and asks YHWH to treat "
                    "the conspirators 'as you did to Midian, as to Sisera and Jabin at the river "
                    "Kishon' (83:9). The purpose of the requested judgment is not mere national "
                    "survival but theological witness: 'Let them know that you alone, whose name "
                    "is YHWH, are the Most High (Elyon) over all the earth' (83:18).",

        "key_verse": {
            "ref": "Psalm 83:18",
            "text": "Let them know that you alone, whose name is the LORD, are the Most High over all the earth.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "sod (secret counsel/conspiracy -- the nations take counsel together against YHWH's people)",
            "berit (covenant -- the nations 'make a covenant together,' 83:5; an anti-YHWH alliance)",
            "Elyon (Most High -- YHWH's supreme title, claiming authority over all other gods and nations)",
            "galgal (whirling dust/tumbleweed -- 'make them like the galgal,' 83:13; chaff before the wind)",
            "tsaphun (your treasured/hidden ones -- Israel as YHWH's hidden treasure; 83:3)"
        ],

        "ane_backdrop": "Coalition warfare against a common enemy is well documented in the ANE. "
                        "The Battle of Qarqar (853 BC) saw a coalition of twelve kings, including "
                        "Ahab of Israel and Ben-Hadad of Damascus, against Shalmaneser III of "
                        "Assyria. The ten-nation conspiracy of Psalm 83 may reflect a specific "
                        "historical coalition or a composite of recurring threats. The prayer for "
                        "cosmic judgment -- 'as fire consumes the forest, as the flame sets the "
                        "mountains ablaze' (83:14) -- reflects the divine warrior's typical "
                        "weapons: fire, storm, and wind.",

        "second_temple": [
            {
                "source": "1 Maccabees 5:1-8",
                "summary": "The nations surrounding Judea conspire against the Maccabean Jews -- "
                           "Edom, Ammon, and others -- in a scenario that echoes Psalm 83's "
                           "coalition.",
                "relevance": "The Psalm 83 pattern of multi-national conspiracy against Israel "
                             "recurred throughout Second Temple history."
            }
        ],

        "cross_refs": [
            {"ref": "Judges 4-5", "note": "The victory over Sisera and Jabin at Kishon -- the historical precedent Ps 83:9 invokes", "type": "ot"},
            {"ref": "Judges 7-8", "note": "Gideon's victory over Midian, Oreb, Zeeb, Zebah, Zalmunna -- referenced in 83:9-11", "type": "ot"},
            {"ref": "Ezekiel 38-39", "note": "Gog's coalition of nations against Israel in the latter days -- the eschatological version of Ps 83", "type": "ot"},
            {"ref": "Revelation 20:7-9", "note": "'Gog and Magog, to gather them for battle' -- the final conspiracy of nations against God's people", "type": "nt"},
            {"ref": "Psalm 2:1-3", "note": "'Why do the nations rage?... against YHWH and his Anointed' -- the same conspiracy pattern", "type": "ot"},
            {"ref": "Genesis 16:12; 25:18", "note": "Ishmael's hostility -- the Ishmaelites are among the Ps 83 conspirators", "type": "ot"}
        ],

        "divine_council_note": "Psalm 83 describes the earthly manifestation of spiritual opposition "
                               "to YHWH's purposes. The ten-nation conspiracy is not merely a political "
                               "alliance; it is an attempt to destroy YHWH's covenant people -- the one "
                               "nation he kept for himself when the others were allotted to the sons of "
                               "God (Deut 32:8-9). The conspirators explicitly target YHWH's nachalah: "
                               "'They say, Let us take possession of the pastures of God (ne'ot Elohim)' "
                               "(83:12). The 'pastures of God' are the promised land -- YHWH's own "
                               "territory. The conspiracy is thus an assault on YHWH's territorial "
                               "sovereignty. In the divine council framework, the nations that surround "
                               "Israel are governed by the elohim of Psalm 82 -- the territorial gods "
                               "who were allotted governance and subsequently corrupted it. The "
                               "conspiracy of their earthly peoples reflects the hostility of their "
                               "spiritual rulers. The prayer for YHWH's intervention (83:9-17) is a plea "
                               "for the cosmic sovereign to overrule the territorial powers. The "
                               "climactic verse (83:18) makes the theological stakes explicit: 'Let "
                               "them know that you alone, whose name is YHWH, are the Most High (Elyon) "
                               "over all the earth.' The title Elyon -- the supreme God above all other "
                               "elohim -- asserts YHWH's right to overrule the corrupt gods and their "
                               "human proxies.",

        "sections": [
            {
                "heading": "The Conspiracy Against YHWH's People (83:1-8)",
                "body": "'O God, do not keep silence; do not hold your peace or be still, O God (El)!' "
                        "(83:1). The urgency is palpable -- divine silence in the face of existential "
                        "threat. 'For behold, your enemies make an uproar; those who hate you have "
                        "raised their heads. They lay crafty plans against your people; they conspire "
                        "against your treasured ones (tsephunekha)' (83:2-3). The word tsephunekha "
                        "('your treasured/hidden ones') echoes the concept of Israel as YHWH's "
                        "segullah (treasured possession, Exod 19:5; Deut 7:6). The conspiracy's "
                        "aim: 'Come, let us wipe them out as a nation; let the name of Israel be "
                        "remembered no more!' (83:4). The goal is genocide -- the erasure of Israel's "
                        "very name. The ten conspirators are listed (83:6-8): Edom, Ishmaelites, "
                        "Moab, Hagrites, Gebal, Ammon, Amalek, Philistia, Tyre, and Assyria. "
                        "'Even Assyria has joined them; they are the strong arm (zero'a) of the "
                        "children of Lot' (83:8). The coalition ranges from local tribal enemies "
                        "to imperial superpowers."
            },
            {
                "heading": "The Prayer for Judgment and the Most High's Vindication (83:9-18)",
                "body": "The psalmist appeals to YHWH's track record: 'Do to them as you did to "
                        "Midian, as to Sisera and Jabin at the river Kishon... Make their nobles "
                        "like Oreb and Zeeb, all their princes like Zebah and Zalmunna' (83:9-11). "
                        "These are all cases where YHWH defeated overwhelming odds through divine "
                        "intervention, not military superiority. The judgment language escalates: "
                        "'O my God, make them like whirling dust (galgal), like chaff before the "
                        "wind. As fire consumes the forest, as the flame sets the mountains "
                        "ablaze, so may you pursue them with your tempest and terrify them with "
                        "your hurricane!' (83:13-15). The storm theophany imagery connects to "
                        "Psalm 29 -- YHWH's voice in the storm scattering his enemies. The "
                        "purpose of judgment is not mere vengeance but revelation: 'Fill their "
                        "faces with shame, that they may seek your name, O YHWH... Let them know "
                        "that you alone (levadkha), whose name is YHWH, are the Most High (Elyon) "
                        "over all the earth (al kol-ha'arets)' (83:16, 18). The goal is that the "
                        "nations -- currently under the governance of corrupt elohim -- will come "
                        "to acknowledge YHWH as the one true supreme God. This connects directly "
                        "to the eschatological cry of Psalm 82:8: YHWH inheriting all the nations."
            }
        ]
    },

    {
        "id": "ps-89",
        "ref": "Psalm 89",
        "chapter_num": 5,
        "title": "The Council of the Holy Ones -- YHWH's Incomparability and the Davidic Crisis",
        "era": "psalms_book3",
        "type": "chapter",

        "synopsis": "Psalm 89 is the theological capstone of Book III and the second great divine "
                    "council text of the Psalter (alongside Ps 82). An Ethanite maskil, it opens "
                    "with a celebration of YHWH's chesed (steadfast love) and faithfulness, then "
                    "presents a divine council scene of extraordinary detail: 'Let the heavens "
                    "praise your wonders, O YHWH, your faithfulness in the assembly of the holy "
                    "ones (qehal qedoshim)! For who in the skies (shachaq) can be compared to "
                    "YHWH? Who among the sons of God (bene elim) is like YHWH, a God greatly to "
                    "be feared in the council of the holy ones (sod qedoshim), and awesome above "
                    "all who are around him?' (89:5-7). The psalm then recounts the Davidic "
                    "covenant in its most exalted form (89:19-37), only to collapse into devastating "
                    "lament: 'But you have cast off and rejected; you are full of wrath against "
                    "your anointed' (89:38). The crown has been defiled, the throne shattered. "
                    "Book III ends with the unanswered question: 'Lord, where is your steadfast "
                    "love of old, which by your faithfulness you swore to David?' (89:49).",

        "key_verse": {
            "ref": "Psalm 89:6-7",
            "text": "For who in the skies can be compared to the LORD? Who among the heavenly beings is like the LORD, a God greatly to be feared in the council of the holy ones, and awesome above all who are around him?",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "qehal qedoshim (assembly of the holy ones -- the divine council gathered in worship)",
            "bene elim (sons of God/sons of the mighty -- the divine council members; same phrase as Ps 29:1)",
            "sod qedoshim (council/counsel of the holy ones -- the deliberative assembly of divine beings)",
            "shachaq (the skies/clouds -- the heavenly realm where the elohim dwell)",
            "Rahab (the chaos sea monster -- 'You crushed Rahab like a carcass,' 89:10; cf. Isa 51:9)",
            "chesed (steadfast love/loyal love -- the covenant faithfulness YHWH pledged to David; appears 7 times)",
            "nezer (crown/consecration -- the crown defiled and cast to the ground in 89:39)",
            "mashiach (anointed one -- 'your anointed' in 89:38, 51; the Davidic king in crisis)"
        ],

        "ane_backdrop": "The divine council scene of Psalm 89:5-7 has close parallels in Ugaritic "
                        "literature. The 'assembly of the sons of El' (phr bn 'ilm) is the standard "
                        "designation for the divine council in the Baal Cycle. The question 'Who among "
                        "the bene elim is like YHWH?' echoes the incomparability formula found in "
                        "Mesopotamian hymns: Marduk is praised as 'the one among the gods who has no "
                        "equal.' But in the Israelite formulation, the incomparability is not merely "
                        "of degree but of kind: YHWH is not the greatest god among equals but the "
                        "unique sovereign whose power and faithfulness no other council member can "
                        "approach. The Rahab reference (89:10) connects to the Canaanite chaos-combat "
                        "mythology: as Baal defeated Yam/Lotan, YHWH crushed Rahab -- but YHWH's "
                        "victory is more comprehensive. The Davidic covenant section (89:19-37) "
                        "parallels ANE royal grant treaties where a suzerain grants an eternal dynasty "
                        "to a loyal vassal.",

        "second_temple": [
            {
                "source": "4QWords of the Luminaries (4Q504)",
                "summary": "A Qumran liturgical text that references the divine council and echoes "
                           "the language of Psalm 89, praising YHWH's incomparability among the "
                           "holy ones.",
                "relevance": "The Dead Sea Scrolls community continued to use the divine council "
                             "language of Psalm 89 in their worship, confirming its centrality."
            },
            {
                "source": "Luke 1:32-33",
                "summary": "Gabriel's announcement to Mary: 'He will be great and will be called "
                           "the Son of the Most High (huios Hupsistou). And the Lord God will give "
                           "to him the throne of his father David, and he will reign over the "
                           "house of Jacob forever.'",
                "relevance": "Gabriel's announcement directly answers the lament of Psalm 89: the "
                             "Davidic throne that seemed destroyed will be restored in Jesus, the "
                             "'Son of the Most High' -- the title connecting him to the bene Elyon "
                             "of the divine council."
            },
            {
                "source": "Acts 2:30-31",
                "summary": "Peter at Pentecost argues that David, 'being a prophet and knowing "
                           "that God had sworn with an oath to him that he would set one of his "
                           "descendants on his throne,' spoke of Christ's resurrection.",
                "relevance": "Peter reads the Davidic covenant of Psalm 89 as fulfilled in the "
                             "resurrection of Jesus -- the anointed one who, unlike 89:38-45, is "
                             "not cast off but exalted."
            }
        ],

        "cross_refs": [
            {"ref": "2 Samuel 7:8-16", "note": "The Davidic covenant -- the historical foundation for Psalm 89's celebration of YHWH's oath to David", "type": "ot"},
            {"ref": "Psalm 82:1, 6", "note": "The divine council scene and the 'sons of the Most High' -- the companion text to Ps 89's council of the holy ones", "type": "ot"},
            {"ref": "Isaiah 51:9-10", "note": "'Was it not you who cut Rahab in pieces, who pierced the dragon?' -- the chaos-combat parallel to Ps 89:10", "type": "ot"},
            {"ref": "Job 1:6; 2:1", "note": "'The sons of God (bene ha'elohim) came to present themselves before YHWH' -- the divine council scene in narrative form", "type": "ot"},
            {"ref": "Job 15:8", "note": "'Have you listened in the council of God (sod Eloah)?' -- the sod language of Ps 89:7", "type": "ot"},
            {"ref": "Luke 1:32-33", "note": "Gabriel announces the restoration of David's throne in Jesus -- answering the lament of Ps 89:38-51", "type": "nt"},
            {"ref": "Daniel 7:9-14", "note": "The heavenly court scene where the Son of Man receives eternal dominion -- the eschatological answer to Ps 89's crisis", "type": "ot"},
            {"ref": "Psalm 29:1", "note": "'Ascribe to YHWH, O bene elim' -- the same divine council designation as 89:6", "type": "ot"},
            {"ref": "Revelation 5:11-14", "note": "The heavenly court worshipping the Lamb -- the eschatological council scene that fulfills Ps 89's qehal qedoshim", "type": "nt"},
            {"ref": "Jeremiah 23:18, 22", "note": "'Who has stood in the council (sod) of YHWH to see and to hear his word?' -- the prophetic access to the divine council", "type": "ot"},
            {"ref": "Isaiah 6:1-8", "note": "Isaiah's throne-room vision -- the same divine council worship scene as Ps 89:5-7, with YHWH 'high and lifted up' and the holy ones crying 'Holy!'", "type": "ot"},
            {"ref": "Daniel 7:9-14", "note": "The Ancient of Days on his throne with the heavenly court -- the same council scene as 89:5-7, now including the Son of Man's enthronement", "type": "ot"},
            {"ref": "Hebrews 1:5-13", "note": "The author applies the Davidic covenant promises ('You are my Son,' 'I will be to him a Father') to Christ -- the Ps 89 covenant fulfilled in the divine Son", "type": "nt"},
            {"ref": "Luke 1:32-33", "note": "'The Lord God will give to him the throne of his father David, and he will reign over the house of Jacob forever' -- Gabriel declaring the Ps 89 covenant fulfilled in Jesus", "type": "nt"},
            {"ref": "Acts 2:30-31", "note": "Peter at Pentecost: David 'foresaw and spoke about the resurrection of the Christ' -- the Ps 89 covenant of 'forever' requires resurrection", "type": "nt"}
        ],

        "divine_council_note": "Psalm 89 is the most detailed divine council scene in the Psalter and "
                               "one of the most important in the entire Hebrew Bible. Three key features: "
                               "(1) THE COUNCIL IN WORSHIP: 'Let the heavens praise your wonders, O YHWH, "
                               "your faithfulness in the assembly of the holy ones (qehal qedoshim)' "
                               "(89:5). The qehal qedoshim is the congregation of holy beings -- the "
                               "divine council assembled for worship. This is the heavenly liturgy that "
                               "Psalm 29:1-2 commanded. (2) YHWH'S INCOMPARABILITY: 'For who in the skies "
                               "(shachaq) can be compared to YHWH? Who among the sons of God (bene elim) "
                               "is like YHWH?' (89:6). The question is rhetorical: NO ONE in the council "
                               "can match YHWH. The bene elim are real divine beings -- the same class as "
                               "the bene elohim of Job 1:6; 38:7, the bene Elyon of Psalm 82:6, and the "
                               "bene elim of Psalm 29:1. They are powerful, they are glorious, but they "
                               "are not comparable to YHWH. (3) THE COUNCIL'S FEAR: 'A God greatly to be "
                               "feared in the council of the holy ones (sod qedoshim rabbah), and awesome "
                               "(nora) above all who are around him (sevivav)' (89:7). The word sod means "
                               "both 'council' (the assembly) and 'counsel' (the deliberation). YHWH is "
                               "'feared' (na'arats) -- not merely respected but genuinely terrifying to "
                               "the divine beings who surround him. Even the holy ones -- the loyal members "
                               "of the council -- stand in awe. The psalm then moves to YHWH's cosmic "
                               "victories (89:9-13) -- ruling the raging sea, crushing Rahab, creating "
                               "heaven and earth -- before presenting the Davidic covenant as YHWH's "
                               "supreme earthly act (89:19-37). The devastating lament that follows "
                               "(89:38-51) does not negate the council theology; rather, it appeals to "
                               "it. The psalmist is asking the cosmic sovereign, who sits enthroned above "
                               "the holy ones and whose faithfulness the council celebrates, why the "
                               "earthly representative of that faithfulness -- the Davidic king -- has "
                               "been abandoned. The tension between the exalted council scene and the "
                               "devastated earthly reality is the theological crisis of Book III. The "
                               "answer will come in Book IV: 'YHWH reigns!' (Pss 93-99).",

        "sections": [
            {
                "heading": "Who Is Ethan the Ezrahite? And What Is a Maskil?",
                "body": "Psalm 89 is attributed to <strong>Ethan the Ezrahite</strong> and "
                        "labeled a <em>maskil</em> (an instructional or wisdom psalm). Ethan "
                        "was one of the three master musicians David appointed for Temple "
                        "worship, alongside Asaph and Heman (1 Chronicles 15:17, 19). He is "
                        "also identified in 1 Kings 4:31 as a man of legendary wisdom -- "
                        "Solomon was said to be wiser 'than Ethan the Ezrahite.' The term "
                        "'Ezrahite' may indicate membership in a pre-Israelite wisdom family "
                        "or may be a variant of 'Zerahite' (a descendant of Zerah, from the "
                        "tribe of Judah). Like the Asaphite and Korahite attributions, 'Ethan "
                        "the Ezrahite' likely designates a musical tradition rather than "
                        "requiring that Ethan personally wrote every word -- his descendants "
                        "and students composed in his tradition.<br><br>"
                        "The <em>maskil</em> designation is significant for Psalm 89: this "
                        "psalm is meant to <em>instruct</em>. Its teaching purpose explains "
                        "the dramatic structure -- it presents the glorious Davidic covenant "
                        "in its fullest form, then forces the reader to confront the devastating "
                        "reality that the covenant appears to have failed. The maskil intends "
                        "the reader to wrestle with this tension, not resolve it cheaply."
            },
            {
                "heading": "The Assembly of the Holy Ones (89:1-8)",
                "body": "'I will sing of the steadfast love (chesed) of YHWH, forever; with my "
                        "mouth I will make known your faithfulness (emunah) to all generations' "
                        "(89:1). Chesed and emunah are the twin pillars of the psalm -- YHWH's "
                        "covenant loyalty and his reliability. The heavenly scene opens in verse "
                        "5: 'Let the heavens praise your wonders, O YHWH, your faithfulness in "
                        "the assembly of the holy ones (qehal qedoshim)!' The qehal qedoshim is "
                        "the divine council in its worshipping function -- the angelic beings "
                        "gathered to praise YHWH's deeds. Verse 6 poses the rhetorical question: "
                        "'For who in the skies (bashachaq) can be compared (ya'arakh) to YHWH? "
                        "Who among the sons of God (bene elim) is like (yidmeh) YHWH?' The word "
                        "shachaq ('skies') locates the comparison in the heavenly realm -- this "
                        "is not about earthly kings but about celestial beings. The bene elim "
                        "('sons of God' or 'sons of the mighty') are the same divine beings "
                        "addressed in Psalm 29:1. None of them can be 'compared' (ya'arakh, "
                        "literally 'arranged alongside') or 'likened' (yidmeh) to YHWH. Verse 7 "
                        "intensifies: 'A God greatly to be feared (na'arats) in the council of "
                        "the holy ones (sod qedoshim rabbah), and awesome (nora) above all who "
                        "are around him (al kol sevivav).' The sod is the intimate council -- "
                        "the inner circle of divine deliberation (cf. Jer 23:18). Even in this "
                        "most exalted company, YHWH inspires dread. The 'all who are around him' "
                        "are the council members who encircle his throne."
            },
            {
                "heading": "Cosmic Victory and the Davidic Covenant (89:9-37)",
                "body": "The psalm moves from the council to YHWH's cosmic acts: 'You rule the "
                        "raging of the sea; when its waves rise, you still them. You crushed "
                        "Rahab (rahab) like a carcass (chalal); you scattered your enemies with "
                        "your mighty arm' (89:9-10). Rahab is the chaos sea monster (cf. Ps "
                        "74:13-14; Isa 51:9; Job 26:12) -- YHWH's sovereignty over chaos proves "
                        "his incomparability. 'The heavens are yours; the earth also is yours; "
                        "the world and all that is in it, you have founded them. The north "
                        "(tsaphon) and the south (yamin), you have created them' (89:11-12). "
                        "Tsaphon -- Baal's mountain -- is YHWH's creation, not his rival. The "
                        "Davidic covenant section begins at verse 19: 'You said, I have made a "
                        "covenant with my chosen one; I have sworn to David my servant: I will "
                        "establish your offspring forever, and build your throne for all "
                        "generations' (89:3-4, reiterated in 89:19-37). The covenant promises "
                        "are absolute: 'I will not violate my covenant or alter the word that "
                        "went forth from my lips. Once for all I have sworn by my holiness; I "
                        "will not lie to David. His offspring shall endure forever, his throne "
                        "as long as the sun before me' (89:34-36). These are irrevocable "
                        "promises, sworn by YHWH's own holiness."
            },
            {
                "heading": "The Devastating Lament: Where Is Your Chesed? (89:38-52)",
                "body": "'But you have cast off (zanachta) and rejected (vatim'as); you are "
                        "full of wrath against your anointed (meshichekha)' (89:38). The contrast "
                        "with the exalted covenant promises is shattering. 'You have renounced "
                        "the covenant of your servant; you have defiled his crown (nizro) in the "
                        "dust' (89:39). The crown -- the symbol of YHWH's covenant gift -- lies "
                        "in the dirt. 'You have breached all his walls; you have laid his "
                        "strongholds in ruins' (89:40). Every defensive fortification has been "
                        "dismantled by YHWH's own hand. 'You have exalted the right hand of his "
                        "foes; you have made all his enemies rejoice' (89:42). YHWH is actively "
                        "working against his own anointed. The lament reaches its anguished "
                        "climax: 'How long, O YHWH? Will you hide yourself forever? How long "
                        "will your wrath burn like fire?... Lord, where is your steadfast love "
                        "(chesed) of old, which by your faithfulness (emunah) you swore to David?' "
                        "(89:46, 49). The psalm began with chesed and emunah; it ends by demanding "
                        "them back. The closing verse: 'Blessed be YHWH forever! Amen and Amen' "
                        "(89:52) -- the Book III doxology, spoken through tears. The crisis is "
                        "unresolved. Book IV must answer the question that Book III has raised: "
                        "if the Davidic covenant has failed, what remains?"
            }
        ]
    },

    {
        "id": "ps-book3-synthesis",
        "ref": "Psalms 73-89",
        "chapter_num": 6,
        "title": "Book III Synthesis: The Divine Council Crisis and the Judgment of the Gods",
        "era": "psalms_book3",
        "type": "chapter",

        "synopsis": "Book III of the Psalter is the divine council book -- the section where the "
                    "cosmic governance of YHWH through subordinate spiritual beings is most "
                    "explicitly addressed, questioned, and judged. The book opens with theodicy "
                    "(Ps 73: why do the wicked prosper?), moves through cosmic battle (Ps 74: "
                    "YHWH vs. Leviathan), historical recital (Ps 78: Israel's failures and YHWH's "
                    "redirections), the divine council judgment scene (Ps 82: the gods sentenced "
                    "to death), the conspiracy of nations (Ps 83: the territorial spirits' earthly "
                    "proxies), and the council of the holy ones with its Davidic crisis (Ps 89). "
                    "The overall arc is devastating: the divine council system appears to be "
                    "broken. The gods govern unjustly (82), the nations conspire (83), and the "
                    "Davidic anointed is cast off (89). Book III ends in darkness. But the "
                    "darkness is theological, not nihilistic -- it demands a divine response.",

        "key_verse": {
            "ref": "Psalm 82:8",
            "text": "Arise, O God, judge the earth! For you shall inherit all the nations!",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "adat-El (assembly of God -- the divine council of Ps 82)",
            "sod qedoshim (council of holy ones -- the divine council of Ps 89)",
            "bene Elyon (sons of the Most High -- the divine council members sentenced in Ps 82)",
            "bene elim (sons of God -- the council members declared incomparable to YHWH in Ps 89)",
            "chesed (steadfast love -- the covenant virtue whose apparent absence drives Book III's crisis)",
            "mashiach (anointed one -- the Davidic king whose rejection closes Book III)"
        ],

        "ane_backdrop": "Book III represents the most sustained engagement with ANE divine council "
                        "theology in the Bible. The Asaphite and Korahite guilds, as temple musicians "
                        "and prophetic seers (Asaph is called a 'seer' in 2 Chr 29:30), had deep "
                        "familiarity with the cosmic mythology of Israel's neighbors and deployed "
                        "it to articulate Israel's unique theology: YHWH is not merely the chief "
                        "god among peers but the incomparable sovereign who judges the other gods "
                        "and sentences them to mortality.",

        "second_temple": [
            {
                "source": "Colossians 2:15",
                "summary": "'He disarmed the rulers and authorities and put them to open shame, "
                           "by triumphing over them in him [the cross].'",
                "relevance": "The NT sees the cross as the execution of the Psalm 82 sentence: "
                             "Christ's death and resurrection strip the hostile spiritual powers "
                             "of their authority over the nations."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9", "note": "The foundational text for the divine council allotment that Book III addresses, judges, and reverses", "type": "ot"},
            {"ref": "Colossians 2:15", "note": "Christ disarming the rulers and authorities -- the NT fulfillment of Psalm 82's judgment", "type": "nt"},
            {"ref": "Ephesians 1:20-22", "note": "Christ seated 'far above all rule and authority and power and dominion' -- the exaltation that answers Ps 89's crisis", "type": "nt"},
            {"ref": "Daniel 7:9-14", "note": "The heavenly court convenes, the Ancient of Days sits, the Son of Man receives the kingdom -- the answer to Book III", "type": "ot"},
            {"ref": "Revelation 4-5", "note": "The heavenly throne room scene where the Lamb receives authority -- the eschatological council session", "type": "nt"}
        ],

        "divine_council_note": "Book III is the interpretive key to the Psalter's divine council "
                               "theology. Its contribution is threefold: (1) THE COUNCIL IS CORRUPT. "
                               "Psalm 82 reveals that the elohim entrusted with governing the nations "
                               "have failed -- they judge unjustly, they favor the wicked, they walk "
                               "in darkness. The foundations of the earth tremble because of their "
                               "corruption. (2) THE COUNCIL IS JUDGED. YHWH rises in the assembly and "
                               "sentences the gods to mortality: 'like men you shall die.' The divine "
                               "beings who were supposed to reflect YHWH's justice will instead share "
                               "humanity's fate. (3) THE COUNCIL'S SYSTEM WILL BE REPLACED. Psalm 82:8 "
                               "cries for YHWH to inherit all the nations directly -- no more mediation "
                               "through subordinate gods. Psalm 89 adds a complementary crisis: not "
                               "only have the gods failed, but the Davidic king -- YHWH's human regent "
                               "-- appears to have been abandoned. The council system is broken from "
                               "both sides: the spiritual rulers are corrupt, and the earthly ruler is "
                               "cast off. The only solution is for YHWH himself to act. Book IV will "
                               "answer with the enthronement psalms: 'YHWH reigns!' (93-99). Book V "
                               "will answer with the Melchizedek psalm: 'Sit at my right hand' (110). "
                               "But Book III leaves the reader in the dark, waiting for the divine "
                               "warrior to arise.",

        "sections": [
            {
                "heading": "Understanding 'Chesed' (Hesed) -- The Word That Holds the Psalter Together",
                "body": "The Hebrew word <strong>chesed</strong> (<em>pronounced KHEH-sed</em>; "
                        "sometimes transliterated as 'hesed') is arguably the most important "
                        "theological word in the Psalter. It appears over 120 times in the Psalms "
                        "and is variously translated as 'steadfast love,' 'lovingkindness,' "
                        "'faithful love,' 'covenant loyalty,' or 'mercy.' No single English word "
                        "captures it.<br><br>"
                        "Chesed is the quality of faithful, committed love that endures regardless "
                        "of circumstances. It is not a feeling but a covenant commitment -- the "
                        "kind of love that remains loyal even when the other party fails. When the "
                        "Psalms say 'his chesed endures forever' (Pss 100:5; 106:1; 107:1; 118:1-4; "
                        "136), they are declaring that YHWH's covenant commitment to his people is "
                        "permanent, unbreakable, and unaffected by human unfaithfulness.<br><br>"
                        "Book III's crisis is fundamentally a chesed crisis. Psalm 89 opens by "
                        "celebrating YHWH's chesed (89:1) and closes by demanding to know where "
                        "it went: 'Lord, where is your chesed of old, which by your faithfulness "
                        "you swore to David?' (89:49). The entire arc of Book III -- from theodicy "
                        "to exile to the judgment of the gods -- is driven by the question: is "
                        "YHWH's chesed still operative? The Psalter's ultimate answer is yes, but "
                        "the path to that answer runs through the darkness of Book III."
            },
            {
                "heading": "What Are Imprecatory Psalms?",
                "body": "Psalm 83 contains language that many modern readers find disturbing: "
                        "'O my God, make them like whirling dust... as fire consumes the forest, "
                        "as the flame sets the mountains ablaze, so may you pursue them with your "
                        "tempest' (83:13-15). This kind of prayer -- calling down divine judgment "
                        "on enemies -- is called an <strong>imprecatory psalm</strong> (from the "
                        "Latin <em>imprecari</em>, 'to invoke evil upon').<br><br>"
                        "Imprecatory psalms (also found in Pss 35, 58, 69, 109, 137, and portions "
                        "of many others) are among the most misunderstood sections of the Psalter. "
                        "Readers often wonder: how can prayers for the destruction of enemies be "
                        "included in Scripture?<br><br>"
                        "Several points help readers engage these psalms honestly:<br>"
                        "(1) <strong>They are prayers, not actions</strong>. The psalmist brings "
                        "rage and desire for justice to God rather than taking vengeance personally. "
                        "The imprecation is an act of trust: 'Vengeance is mine, I will repay, "
                        "says the Lord' (Deut 32:35; Rom 12:19).<br>"
                        "(2) <strong>The 'enemies' are often cosmic, not merely personal</strong>. "
                        "In the divine council framework, the nations that conspire against YHWH's "
                        "people (Ps 83) are proxies for hostile spiritual powers. The prayer for "
                        "their destruction is a prayer against evil itself.<br>"
                        "(3) <strong>The goal is often repentance, not annihilation</strong>. "
                        "Psalm 83 ends not with the destruction of the enemies but with the hope "
                        "that 'they may seek your name, O YHWH' (83:16) and 'know that you alone "
                        "are the Most High over all the earth' (83:18).<br>"
                        "(4) <strong>They are emotionally honest</strong>. The Psalter does not "
                        "sanitize human experience. It gives voice to grief, rage, and the cry "
                        "for justice that every victim of oppression knows. To exclude these "
                        "prayers would be to exclude the suffering from worship."
            },
            {
                "heading": "The Structural Arc: From Theodicy to Crisis",
                "body": "Book III's structural movement is from individual theodicy (Ps 73) to "
                        "national crisis (Ps 89), with the divine council as the hinge. Psalm 73 "
                        "asks why the individual wicked prosper; the answer is found in the "
                        "sanctuary. Psalm 74 asks why the temple is destroyed; the answer is "
                        "sought in the cosmic battle tradition. Psalm 78 recounts the historical "
                        "pattern of rebellion and divine faithfulness. Psalm 82 moves to the "
                        "cosmic level: the gods themselves are the problem. Psalm 83 shows the "
                        "earthly manifestation of the cosmic problem: the nations conspire "
                        "against YHWH's people. And Psalm 89 brings the crisis to its most acute "
                        "form: the Davidic covenant, sworn by YHWH's own holiness, appears to "
                        "have been broken. The five-book structure of the Psalter means Book III "
                        "corresponds roughly to Leviticus in the Torah -- the book of holiness "
                        "and the priesthood. Fittingly, Book III is dominated by the Levitical "
                        "guilds (Asaph and Korah) and concerns itself with the holy assembly "
                        "(the divine council) and the maintenance of cosmic holiness (the "
                        "judgment of the corrupt gods). The doxology of 89:52 -- 'Blessed be "
                        "YHWH forever! Amen and Amen' -- is the most paradoxical of the five "
                        "book-ending doxologies: it praises YHWH in the midst of YHWH's apparent "
                        "faithlessness. It is faith without sight -- the essence of the Psalter's "
                        "theology."
            }
        ]
    }
]
