"""
era_riv_framework.py -- The Riv Pattern (Chapters 1-3)

The Hebrew prophets were not freelance spiritual commentators offering
inspirational reflections on life. They were royal messengers -- dispatched
from YHWH's heavenly court with a specific legal brief: prosecute Israel
for covenant violations. The riv (rib in some transliterations) is the
covenant lawsuit, a formal legal genre rooted in Ancient Near Eastern
suzerainty treaty practice. Every major and minor prophet operates within
this framework. Heaven and earth are summoned as witnesses. The charges
are read. The evidence is presented. The verdict is delivered. The sentence
is pronounced. This is not poetry -- it is litigation from the throne room.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: THE RIV PATTERN -- COVENANT LAWSUITS IN THE HEBREW BIBLE
    # =========================================================================
    {
        "id": "riv-01",
        "ref": "Deuteronomy 32:1; Isaiah 1:2-4; Micah 6:1-8; Hosea 4:1-3",
        "chapter_num": 1,
        "title": "The Riv Pattern \u2014 Covenant Lawsuits in the Hebrew Bible",
        "era": "riv_framework",
        "type": "chapter",

        "synopsis": "The riv (also transliterated rib) is the covenant lawsuit -- the foundational "
                    "genre of Hebrew prophecy that modern readers almost universally miss. The "
                    "pattern follows a precise legal structure borrowed from Ancient Near Eastern "
                    "suzerainty treaty enforcement: (1) summons of witnesses, typically heaven and "
                    "earth (Deut 4:26, 30:19, 32:1; Isa 1:2; Mic 6:1-2); (2) historical prologue "
                    "recounting YHWH's faithfulness; (3) indictment listing specific covenant "
                    "violations; (4) verdict of guilt; (5) sentence -- the curses from Deuteronomy "
                    "28. [A] Micah 6:1-8 provides the clearest single example: YHWH summons the "
                    "mountains as witnesses (6:1-2), recounts his saving acts from Egypt to Canaan "
                    "(6:3-5), rejects ritual substitutes for obedience (6:6-7), and delivers the "
                    "covenant demand: justice, mercy, and humble walk with God (6:8). [B] Once this "
                    "pattern is recognized, every prophetic book transforms from vague spiritual "
                    "poetry into a precise legal proceeding. The prophets are not inspired "
                    "commentators -- they are prosecuting attorneys dispatched from YHWH's court.",

        "key_verse": {
            "ref": "Micah 6:1-2",
            "text": "Hear what the LORD says: Arise, plead your case before the mountains, and let the hills hear your voice. Hear, you mountains, the indictment of the LORD, and you enduring foundations of the earth, for the LORD has an indictment against his people, and he will contend with Israel.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05e8\u05b4\u05d9\u05d1 (riv)",
                "meaning": "'Lawsuit, legal case, contention, dispute.' The root r-y-b means 'to conduct "
                           "a lawsuit, to lodge a legal complaint.' When YHWH has a riv with Israel "
                           "(Hos 4:1; Mic 6:2; Jer 2:9), he is not having a disagreement -- he is "
                           "filing a formal covenant lawsuit. The noun appears over 60 times in the "
                           "Hebrew Bible, frequently in prophetic contexts. In Micah 6:2, YHWH's riv "
                           "is directed against 'his people' (ammo) -- the covenant partner who has "
                           "violated the agreement. The legal precision matters: this is not divine "
                           "frustration but formal prosecution. The entire prophetic corpus is "
                           "structured around this legal action."
            },
            {
                "term": "\u05e2\u05b5\u05d3 (\u2018ed)",
                "meaning": "'Witness.' Heaven and earth are summoned as treaty witnesses in the riv "
                           "pattern (Deut 4:26, 30:19, 32:1; Isa 1:2). In ANE suzerainty treaties, "
                           "gods were invoked as witnesses to the covenant. Since YHWH has no peer "
                           "gods to invoke, he calls the cosmic order itself -- heaven, earth, "
                           "mountains, hills -- as permanent witnesses who were present when the "
                           "covenant was ratified at Sinai. These are not poetic flourishes but "
                           "legal formalities required by the treaty genre. The mountains and hills "
                           "in Micah 6:1-2 serve as the jury, not the audience."
            },
            {
                "term": "\u05de\u05b4\u05e9\u05b0\u05c1\u05e4\u05b8\u05bc\u05d8 (mishpat)",
                "meaning": "'Justice, judgment, legal decision, ordinance.' From the root sh-p-t ('to "
                           "judge'). Mishpat appears over 400 times in the Hebrew Bible and is the "
                           "central demand of the covenant. When Micah 6:8 says 'what does YHWH "
                           "require of you but to do mishpat,' this is not abstract ethics but "
                           "covenant obligation -- the specific standards of justice codified in the "
                           "Torah. The prophets prosecute Israel for failing mishpat: rigged courts, "
                           "exploitation of the poor, bribery, land theft. These are treaty "
                           "violations, not moral suggestions."
            },
            {
                "term": "\u05d4\u05b7\u05e2\u05b4\u05d9\u05d3\u05b9\u05ea\u05b4\u05d9 (ha\u2018idoti)",
                "meaning": "'I have caused to testify, I have warned.' From the root \u2018-w-d ('to "
                           "testify, to bear witness, to warn formally'). This is the legal "
                           "notification term. In Deuteronomy 4:26 and 30:19, Moses says 'I call "
                           "heaven and earth to witness (ha\u2018idoti) against you' -- a formal legal "
                           "deposition of testimony. The prophets continue this role: they are "
                           "delivering legal notice that the covenant has been violated and the "
                           "stipulated penalties are now in effect."
            }
        ],

        "ane_backdrop": "The riv pattern maps directly onto the enforcement mechanism of Ancient Near "
                       "Eastern suzerainty treaties. In the Hittite treaty tradition (c. 1400-1200 BC), "
                       "when a vassal violated a treaty, the great king would send a messenger with a "
                       "formal complaint listing: (1) the king's past benefits to the vassal, (2) the "
                       "specific violations committed, (3) the consequences stipulated in the treaty. "
                       "The Treaty of Tudhaliya IV with Kurunta of Tarhuntassa follows this exact "
                       "pattern. Assyrian treaties (particularly Esarhaddon's Vassal Treaties, 672 BC) "
                       "included curse lists strikingly parallel to Deuteronomy 28. The prophets "
                       "are operating within a well-known international legal genre that their audience "
                       "would have immediately recognized as formal treaty prosecution.",

        "second_temple": [
            {
                "source": "4QXIIa (Qumran Minor Prophets Scroll)",
                "summary": "The Book of the Twelve preserved as a single continuous scroll at Qumran, "
                           "supporting the reading of the minor prophets as one unified prosecution "
                           "document rather than twelve separate books.",
                "relevance": "If the Twelve function as a single work, their riv pattern forms a "
                            "progressive covenant lawsuit from Hosea's opening indictment through "
                            "Malachi's final summons."
            },
            {
                "source": "Sirach 49:10 (Ben Sira)",
                "summary": "Ben Sira treats the Twelve Prophets as a single group: 'May the bones of "
                           "the Twelve Prophets send forth new life from where they lie, for they "
                           "comforted the people of Jacob.'",
                "relevance": "Second Temple Judaism understood the minor prophets as a unified witness, "
                            "consistent with reading them as stages in a single covenant prosecution."
            },
            {
                "source": "1 Enoch 1:1-9 (non-canonical)",
                "summary": "1 Enoch opens with a prophetic prosecution pattern: Enoch delivers a verdict "
                           "against the Watchers using riv-like structure -- charges, evidence, and "
                           "sentence from the divine council.",
                "relevance": "The riv pattern extends beyond canonical prophets; 1 Enoch shows the same "
                            "prosecutorial framework applied to cosmic beings, not just Israel."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:1", "note": "Moses summons heaven and earth as covenant witnesses: 'Give ear, O heavens, and let me speak; and let the earth hear the words of my mouth' -- the template for all prophetic riv openings", "type": "ot"},
            {"ref": "Deuteronomy 4:26", "note": "'I call heaven and earth to witness against you today' -- Moses formally deposes cosmic witnesses against Israel, the legal foundation the prophets later invoke", "type": "ot"},
            {"ref": "Deuteronomy 30:19", "note": "'I call heaven and earth to witness against you today, that I have set before you life and death, blessing and curse' -- the covenant choice with cosmic witnesses", "type": "ot"},
            {"ref": "Isaiah 1:2-4", "note": "'Hear, O heavens, and give ear, O earth; for the LORD has spoken' -- Isaiah opens with the classic riv summons, then lists Israel's covenant violations", "type": "ot"},
            {"ref": "Hosea 4:1-3", "note": "'The LORD has an indictment (riv) against the inhabitants of the land. There is no faithfulness or steadfast love, and no knowledge of God in the land' -- Hosea names the riv explicitly", "type": "ot"},
            {"ref": "Jeremiah 2:9", "note": "'Therefore I still contend (riv) with you, declares the LORD, and with your children's children I will contend' -- the generational scope of YHWH's lawsuit", "type": "ot"},
            {"ref": "1 Enoch 1:1-9", "note": "According to 1 Enoch, the patriarch delivers a prophetic verdict against the Watchers using the same prosecution structure the later prophets use against Israel", "type": "pseudepigrapha"},
            {"ref": "KTU 1.2 (Baal Cycle)", "note": "In Ugaritic literature, the divine council functions as a court where cases are heard and verdicts delivered -- the same setting from which YHWH dispatches his prophets", "type": "ane"}
        ],

        "divine_council_note": "The riv is fundamentally a divine council action. The prophets do not "
                              "speak on their own authority -- they speak as envoys dispatched from YHWH's "
                              "heavenly court. When heaven and earth are summoned as witnesses (Deut 32:1; "
                              "Isa 1:2), the cosmic order itself becomes the jury in a case tried before "
                              "the divine assembly. Psalm 82 shows the divine council functioning as a "
                              "courtroom where God rises to judge: 'God (Elohim) has taken his place in "
                              "the divine council (adat-El); in the midst of the gods (elohim) he holds "
                              "judgment.' The riv is not a literary device -- it is the legal mechanism by "
                              "which the divine king enforces his covenant through his council and its "
                              "dispatched messengers.",

        "sections": [
            {
                "heading": "The Five-Part Structure of the Covenant Lawsuit",
                "body": "The riv follows a precise legal architecture that appears with remarkable consistency across the prophetic corpus. First, the summons: cosmic witnesses are called to hear the case. Deuteronomy 32:1 establishes the template -- 'Give ear, O heavens, and let me speak; and let the earth hear the words of my mouth.' Isaiah echoes it in 1:2: 'Hear, O heavens, and give ear, O earth.' Micah summons the mountains themselves as the jury (6:1-2). These are not poetic ornaments -- in ANE treaty law, witnesses must be present for legal proceedings to be valid. Second, the historical prologue: YHWH recounts his faithfulness. Micah 6:3-5 is the clearest example: 'O my people, what have I done to you? How have I wearied you? Answer me! For I brought you up from the land of Egypt and redeemed you from the house of slavery.' The great king reminds the vassal of past benefits before listing violations. Third, the indictment: specific covenant breaches are named. Hosea 4:1-2 reads like a legal charge sheet: 'There is no faithfulness or steadfast love, and no knowledge of God in the land; there is swearing, lying, murder, stealing, and committing adultery.' These map directly to the Decalogue -- the core stipulations of the Sinai treaty. Fourth, the verdict: guilt is declared. Fifth, the sentence: the curses of Deuteronomy 28 are invoked -- exile, famine, plague, military defeat. Every prophet operates within this structure."
            },
            {
                "heading": "Heaven and Earth as Covenant Witnesses",
                "body": "Why do the prophets keep summoning heaven and earth? It is not dramatic flair -- it is legal necessity. In Ancient Near Eastern suzerainty treaties, the gods of both parties were invoked as witnesses to guarantee enforcement. The Hittite treaties routinely ended with a list of divine witnesses: 'The thousand gods have now been called to assembly for witnessing.' When YHWH enters a covenant with Israel, he faces a unique legal situation: there are no peer gods to serve as witnesses. His solution is to invoke the permanent features of the created order itself. Deuteronomy 4:26 -- 'I call heaven and earth to witness against you today.' Deuteronomy 30:19 -- 'I call heaven and earth to witness against you today, that I have set before you life and death.' Deuteronomy 32:1 -- 'Give ear, O heavens, and let me speak; and let the earth hear the words of my mouth.' Heaven and earth were present at Sinai. They witnessed the covenant ratification. They heard the stipulations and the curses. When YHWH later sends prophets to prosecute Israel, those prophets summon the same witnesses who were present at the original treaty signing. Isaiah 1:2 opens with this summons because Isaiah is reopening a case that was filed at Sinai. The mountains in Micah 6:1-2 are not metaphors -- they are the oldest witnesses in the courtroom, and they have seen everything."
            },
            {
                "heading": "Prophets as Royal Messengers, Not Inspired Commentators",
                "body": "The modern tendency to treat prophets as inspired spiritual commentators -- people who had deep insights about God and shared them poetically -- fundamentally misunderstands the prophetic office. The Hebrew prophet (navi) is a royal messenger dispatched from the king's court with an official message. The phrase 'thus says YHWH' (ko amar YHWH) is not a piety formula -- it is the ANE messenger formula, identical in structure to 'thus says the great king' used in diplomatic correspondence throughout the ancient world. The Akkadian phrase umma shar rabbu ana means 'thus says the great king to...' -- the exact pattern used hundreds of times in the prophetic corpus. When Isaiah says 'thus says YHWH,' he is identifying himself as an authorized envoy delivering official communication from the sovereign. He has been to the throne room. He has received his commission. He speaks with delegated authority, not personal inspiration. Amos 3:7 makes this explicit: 'For the Lord YHWH does nothing without revealing his secret (sod) to his servants the prophets.' The word sod means both 'secret' and 'council' -- the prophet has been admitted to YHWH's privy council (sod YHWH, cf. Jer 23:18) and now relays what he heard there. Jeremiah 23:18-22 draws the sharpest line: a true prophet has stood in the council; a false one has not."
            },
            {
                "heading": "Micah 6:1-8 -- The Complete Riv in Eight Verses",
                "body": "Micah 6:1-8 is the single most complete and compact example of the riv pattern in the entire prophetic corpus, and it deserves close attention as the template for all the others. Verse 1: 'Hear what the LORD says: Arise, plead your case (riv) before the mountains, and let the hills hear your voice.' The word riv is used explicitly -- this is a lawsuit. The mountains are summoned as witnesses who have been standing since creation. Verse 2: 'Hear, you mountains, the indictment of the LORD.' The word 'indictment' (riv again) makes the legal register unmistakable. Verses 3-5: the historical prologue. 'O my people, what have I done to you? How have I wearied you? Answer me! For I brought you up from the land of Egypt and redeemed you from the house of slavery, and I sent before you Moses, Aaron, and Miriam.' YHWH recounts his covenant faithfulness -- the exodus, the leadership, the deliverance from Balaam's curse. This is the great king reminding the vassal of unmerited benefits. Verses 6-7: Israel offers ritual substitutes -- burnt offerings, calves, rams, oil, even the firstborn. These are attempts to buy off the prosecutor without addressing the actual covenant violations. Verse 8: the verdict and demand. 'He has told you, O man, what is good; and what does the LORD require of you but to do justice (mishpat), and to love kindness (chesed), and to walk humbly with your God?' This is not generic ethics -- mishpat and chesed are covenant terms. The demand is treaty compliance, not spiritual self-improvement."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: THE ROYAL MESSENGER PROTOCOL
    # =========================================================================
    {
        "id": "riv-02",
        "ref": "1 Kings 22:19-23; Isaiah 6:1-8; Amos 3:7; Jeremiah 23:18-22",
        "chapter_num": 2,
        "title": "The Royal Messenger Protocol \u2014 How the Divine Council Dispatches Prophets",
        "era": "riv_framework",
        "type": "chapter",

        "synopsis": "[A] The Hebrew prophets did not simply 'feel called' to speak -- they were "
                    "formally commissioned in YHWH's divine council. 1 Kings 22:19-23 provides the "
                    "clearest narrative: Micaiah ben Imlah sees YHWH seated on his throne with the "
                    "entire host of heaven standing on his right and left. YHWH asks the council 'Who "
                    "will persuade Ahab?' and a spirit volunteers, receiving explicit authorization "
                    "before being dispatched. Isaiah 6:1-8 shows the same commissioning: the prophet "
                    "sees YHWH's throne, hears the seraphim, is cleansed, and then responds to 'Whom "
                    "shall I send, and who will go for us?' -- the plural 'us' addressing the council. "
                    "[A] Amos 3:7 states the principle: 'The Lord YHWH does nothing without revealing "
                    "his sod (secret/council) to his servants the prophets.' [B] The word sod carries "
                    "both meanings -- the prophet is admitted to YHWH's privy council and receives "
                    "the council's secret deliberation. Jeremiah 23:18, 22 draws the line between "
                    "true and false prophets: 'Who among them has stood in the council (sod) of "
                    "YHWH?' False prophets have not been to the throne room.",

        "key_verse": {
            "ref": "1 Kings 22:19-20",
            "text": "I saw the LORD sitting on his throne, and all the host of heaven standing beside him on his right hand and on his left. And the LORD said, 'Who will entice Ahab, that he may go up and fall at Ramoth-gilead?'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05e1\u05d5\u05b9\u05d3 (sod)",
                "meaning": "'Secret, confidential council, intimate circle.' The word carries a dual "
                           "meaning that is essential for understanding prophecy: sod means both the "
                           "divine council itself (the assembly where YHWH deliberates) and the secret "
                           "deliberation that occurs there. When Amos 3:7 says YHWH reveals his sod "
                           "to the prophets, it means both 'he admits them to his council' and 'he "
                           "shares his confidential plans.' Jeremiah 23:18 uses it to distinguish "
                           "true from false prophets: 'Who among them has stood in the sod of YHWH "
                           "to see and to hear his word?' Standing in the sod is the authentication "
                           "of genuine prophetic calling."
            },
            {
                "term": "\u05e0\u05b8\u05d1\u05b4\u05d9\u05d0 (navi)",
                "meaning": "'Prophet, spokesperson, one who is called.' The etymology is debated: it "
                           "may derive from the Akkadian nabu ('to call, to announce') or from a "
                           "passive form ('one who is called'). In either case, the navi is not a "
                           "self-appointed commentator but one who has been called into service and "
                           "authorized to speak. The navi delivers the message he received in the "
                           "divine council -- he is a mouthpiece, not a source. Exodus 7:1 clarifies "
                           "the role: Aaron is Moses' navi, meaning Aaron speaks what Moses tells "
                           "him. The prophet speaks what YHWH tells him. The chain of authority runs "
                           "from the divine council through the prophet to the people."
            },
            {
                "term": "\u05db\u05bc\u05b9\u05d4 \u05d0\u05b8\u05de\u05b7\u05e8 \u05d9\u05b0\u05d4\u05d5\u05b8\u05d4 (ko amar YHWH)",
                "meaning": "'Thus says YHWH' -- the prophetic messenger formula. This is not a piety "
                           "marker or rhetorical device. It is the ANE royal messenger formula, "
                           "identical in structure to the Akkadian diplomatic phrase 'thus says the "
                           "great king.' In the Amarna Letters (14th century BC), envoys use this "
                           "exact formula to deliver messages from one king to another. When a prophet "
                           "says ko amar YHWH, he is identifying himself as an authorized envoy "
                           "delivering official communication from the divine sovereign. The formula "
                           "appears over 400 times in the prophetic books."
            },
            {
                "term": "\u05de\u05b4\u05d9 \u05d9\u05b5\u05dc\u05b5\u05da\u05b0 \u05dc\u05b8\u05e0\u05d5\u05bc (mi yelekh lanu)",
                "meaning": "'Who will go for us?' (Isaiah 6:8). The plural 'us' (lanu) is not a "
                           "royal 'we' or a Trinitarian proof-text in its original context -- it is "
                           "YHWH addressing his divine council. The question is posed to the heavenly "
                           "assembly: who among the council will carry this message? Isaiah volunteers: "
                           "'Here am I! Send me (sh'lacheni).' The verb shalach ('to send') is the "
                           "same root behind the noun shaliach ('sent one, emissary') -- the prophet "
                           "is commissioned as YHWH's authorized agent, a concept Paul later applies "
                           "to apostles (apostolos, Greek equivalent of shaliach)."
            }
        ],

        "ane_backdrop": "The royal messenger system was the backbone of Ancient Near Eastern diplomacy. "
                       "The Amarna Letters (c. 1350 BC) -- diplomatic correspondence between Egypt and "
                       "Canaan -- demonstrate the protocol: the messenger arrives, delivers the king's "
                       "words using the formula 'thus says the king,' and the message carries the "
                       "authority of the king himself. Disrespecting the messenger was disrespecting "
                       "the king. 2 Chronicles 36:16 applies this directly: Israel's fall came because "
                       "'they kept mocking the messengers of God, despising his words, and scoffing at "
                       "his prophets.' In Mesopotamian religion, the divine council (puhrum) was a "
                       "formal assembly where gods deliberated and dispatched agents. The Enuma Elish "
                       "describes the gods assembling in council to authorize Marduk's mission. YHWH's "
                       "council operates within this same institutional framework, though with absolute "
                       "divine sovereignty rather than democratic deliberation.",

        "second_temple": [
            {
                "source": "4Q385-389 (Pseudo-Ezekiel, Qumran)",
                "summary": "These fragments expand on Ezekiel's throne-chariot (merkavah) vision, "
                           "showing sustained Second Temple interest in the divine council's visible "
                           "manifestation and the prophet's access to YHWH's throne room.",
                "relevance": "The Qumran community understood the prophet's authority as rooted in "
                            "direct access to the divine council -- the same framework 1 Kings 22 "
                            "and Isaiah 6 present."
            },
            {
                "source": "1 Enoch 14:8-25 (non-canonical)",
                "summary": "1 Enoch describes the patriarch being brought before the divine throne "
                           "in extraordinary detail -- crystal walls, fiery floor, the Great Glory "
                           "seated on the throne. Enoch receives his commission to deliver judgment "
                           "to the Watchers directly from the council.",
                "relevance": "Enoch's throne-room commissioning follows the same pattern as Isaiah 6 "
                            "and 1 Kings 22: see the throne, receive the message, go deliver it. The "
                            "prophetic pattern extends beyond the canonical prophets."
            },
            {
                "source": "Targum Jonathan on Isaiah 6",
                "summary": "The Aramaic Targum interprets Isaiah's vision with expanded descriptions "
                           "of the seraphim and the divine court, reflecting the ongoing Jewish "
                           "tradition of merkavah (throne-chariot) interpretation.",
                "relevance": "Post-exilic Judaism continued to understand prophetic commissioning as "
                            "throne-room access, developing elaborate merkavah traditions around "
                            "the prophetic call narratives."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 22:19-23", "note": "Micaiah sees YHWH's council deliberating how to deal with Ahab -- the clearest narrative of divine council commissioning a prophetic mission", "type": "ot"},
            {"ref": "Isaiah 6:1-8", "note": "'Whom shall I send, and who will go for us?' -- Isaiah's commissioning in YHWH's throne room, responding to the council's call", "type": "ot"},
            {"ref": "Amos 3:7", "note": "'The Lord YHWH does nothing without revealing his sod to his servants the prophets' -- the prophet as privy council insider", "type": "ot"},
            {"ref": "Jeremiah 23:18", "note": "'For who among them has stood in the council (sod) of YHWH to see and to hear his word?' -- the test of true vs. false prophecy", "type": "ot"},
            {"ref": "Psalm 82:1", "note": "'God has taken his place in the divine council; in the midst of the gods he holds judgment' -- the council as courtroom", "type": "ot"},
            {"ref": "Job 1:6-12", "note": "The bene ha-elohim present themselves before YHWH and the satan appears among them -- a divine council session with a prosecutorial adversary", "type": "ot"},
            {"ref": "2 Chronicles 36:15-16", "note": "YHWH sends messengers persistently, but Israel mocks them -- rejecting the envoy is rejecting the king", "type": "ot"},
            {"ref": "Luke 11:49", "note": "'The Wisdom of God said, I will send them prophets and apostles' -- Jesus connects prophetic dispatch to divine authorization, extending it to the apostles", "type": "nt"},
            {"ref": "1 Enoch 14:8-25", "note": "According to 1 Enoch, Enoch is brought before YHWH's throne in vivid detail and commissioned to deliver judgment to the Watchers -- the same dispatch pattern", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "This chapter is the divine council chapter. The entire prophetic office is a "
                              "divine council function. The prophet does not speak from personal insight or "
                              "spiritual sensitivity -- he speaks because he has been admitted to YHWH's "
                              "heavenly court, heard the deliberation, and been authorized to deliver the "
                              "verdict. 1 Kings 22:19-23 is the most transparent account: Micaiah literally "
                              "sees YHWH on his throne with the host of heaven on his right and left. A "
                              "spirit steps forward, proposes a plan, and receives authorization: 'Go out "
                              "and do so.' This is not metaphor -- this is the institutional mechanism by "
                              "which prophecy functions. Isaiah 6 shows the same pattern: the prophet sees "
                              "the throne, is cleansed, and responds to the council's call. Jeremiah 23:18-22 "
                              "makes council access the very definition of prophetic legitimacy: if you have "
                              "not stood in the sod, you are not a prophet. Period.",

        "sections": [
            {
                "heading": "1 Kings 22:19-23 -- The Council Deliberates, the Prophet Reports",
                "body": "First Kings 22 provides the most transparent narrative of how the divine council actually operates. Ahab king of Israel wants to attack Ramoth-gilead and asks his 400 court prophets if he should go. They unanimously say yes. But Jehoshaphat king of Judah asks for a prophet of YHWH, and Micaiah ben Imlah is summoned -- a prophet Ahab hates 'because he never prophesies good concerning me, but evil.' Micaiah initially mimics the court prophets sarcastically, then delivers what he actually saw: 'I saw the LORD sitting on his throne, and all the host of heaven standing beside him on his right hand and on his left. And the LORD said, \"Who will entice Ahab, that he may go up and fall at Ramoth-gilead?\" And one said one thing, and another said another. Then a spirit came forward and stood before the LORD, saying, \"I will entice him.\" And the LORD said, \"By what means?\" And he said, \"I will go out, and will be a lying spirit in the mouth of all his prophets.\" And he said, \"You are to entice him, and you shall succeed; go out and do so.\"' The council deliberates. Multiple suggestions are offered. One spirit proposes a specific plan. YHWH evaluates it, approves it, and issues authorization. This is institutional process, not spontaneous inspiration. Micaiah reports what he witnessed in the council -- that is what makes him a true prophet."
            },
            {
                "heading": "Isaiah 6 -- Commissioned in the Throne Room",
                "body": "Isaiah's call narrative in chapter 6 is one of the most studied passages in the Hebrew Bible, but its divine council setting is often overlooked. 'In the year that King Uzziah died I saw the Lord sitting upon a throne, high and lifted up; and the train of his robe filled the temple.' The earthly king has died; Isaiah sees the true King. The seraphim (literally 'burning ones' -- the same category of serpentine divine beings as the nachash, see Numbers 21:6 where saraph and nachash appear together) attend the throne, crying 'Holy, holy, holy is the LORD of hosts.' Isaiah is undone -- 'Woe is me! For I am lost; for I am a man of unclean lips, and I dwell in the midst of a people of unclean lips; for my eyes have seen the King, the LORD of hosts!' A seraph cleanses his lips with a burning coal from the altar. Then comes the commissioning: 'And I heard the voice of the Lord saying, \"Whom shall I send, and who will go for us?\"' The shift from singular 'I' to plural 'us' is the divine council speaking. YHWH asks the assembly who will carry the message. Isaiah volunteers: 'Here am I! Send me.' He is then given his message -- and it is devastating: 'Go, and say to this people: Keep on hearing, but do not understand.' The prophet is dispatched with a verdict of judicial hardening. This is a courtroom sentencing, not a motivational speech."
            },
            {
                "heading": "Amos 3:7 and the Sod of YHWH",
                "body": "Amos 3:7 is the theological thesis statement of the prophetic office: 'For the Lord YHWH does nothing without revealing his sod to his servants the prophets.' The word sod is the key. It means both 'confidential council' (the assembly itself) and 'secret deliberation' (what happens there). Proverbs 3:32 uses sod for intimate friendship: 'the upright are in his sod' -- his inner circle. Psalm 25:14 parallels this: 'The sod of YHWH is for those who fear him.' The prophet is admitted to the inner circle where divine decisions are made before they are executed in the world. Amos himself was not a professional prophet -- 'I was no prophet, nor a prophet's son, but I was a herdsman' (7:14). Yet YHWH took him from the flock and said 'Go, prophesy to my people Israel' (7:15). The authorization does not come from training or lineage but from council access. Jeremiah 23:18 makes this the litmus test: 'For who among them has stood in the council (sod) of YHWH to see and to hear his word?' Verse 22 delivers the verdict on false prophets: 'But if they had stood in my council, then they would have proclaimed my words to my people, and they would have turned them from their evil way.' False prophets fail the test not because their theology is wrong but because they were never in the room."
            },
            {
                "heading": "The Messenger Formula -- 'Thus Says YHWH'",
                "body": "The phrase 'thus says YHWH' (ko amar YHWH) appears over 400 times in the prophetic books and is routinely treated as a piety formula -- a way prophets signal that they are about to say something spiritual. This is a fundamental misunderstanding. The phrase is the ANE royal messenger formula, and it functioned as diplomatic credentials. When an envoy arrived at a foreign court, he would announce 'thus says the great king' and then deliver the message verbatim. The envoy did not compose the message, interpret the message, or negotiate the message -- he delivered it. His authority derived entirely from the king who sent him. The Amarna Letters from 14th-century BC Egypt-Canaan correspondence use this formula hundreds of times: 'Thus says the king of Egypt to the king of...' The biblical prophets use the identical formula because they hold the identical role: they are envoys from the divine court delivering YHWH's official communication. When Elijah confronts Ahab, he says 'thus says YHWH' and delivers the verdict. When Isaiah addresses Hezekiah, he says 'thus says YHWH' and delivers the sentence. The formula means: what follows is not my opinion -- it is the King's word. Reject the messenger and you reject the King. Israel's ultimate catastrophe, according to 2 Chronicles 36:15-16, was precisely this: 'They kept mocking the messengers of God, despising his words, and scoffing at his prophets, until the wrath of the LORD rose against his people, until there was no remedy.'"
            }
        ]
    },

    # =========================================================================
    # CHAPTER 3: THE COVENANT AT SINAI
    # =========================================================================
    {
        "id": "riv-03",
        "ref": "Deuteronomy 28:1-68; Exodus 19:3-6; Deuteronomy 4:26; Leviticus 26:14-45",
        "chapter_num": 3,
        "title": "The Covenant at Sinai \u2014 What the Prophets Are Prosecuting",
        "era": "riv_framework",
        "type": "chapter",

        "synopsis": "[A] The prophets do not prosecute Israel for generic sinfulness -- they prosecute "
                    "specific violations of the Sinai covenant. This covenant follows the structure of "
                    "ANE suzerainty treaties: preamble identifying the great king (Exod 20:2a -- 'I am "
                    "YHWH your God'), historical prologue recounting past benefits (Exod 20:2b -- 'who "
                    "brought you out of the land of Egypt'), stipulations (the Decalogue and case law), "
                    "witnesses (heaven and earth, Deut 4:26), deposit and reading instructions (Deut "
                    "31:9-13), and blessings/curses (Deut 28, Lev 26). [C] The Hittite suzerainty "
                    "treaties of the 14th-13th centuries BC follow this identical six-part structure, "
                    "and the parallels are too precise to be coincidental. [A] Deuteronomy 28 is the "
                    "curse list that every prophet invokes: famine (28:23-24), plague (28:21-22), "
                    "military defeat (28:25), siege (28:52-57), exile (28:63-68). When Isaiah, "
                    "Jeremiah, Ezekiel, and the Twelve pronounce judgment, they are not inventing "
                    "penalties -- they are activating the pre-agreed consequences of treaty violation. "
                    "The prophet is the attorney; YHWH is plaintiff, judge, and king; and the penalty "
                    "schedule was signed at Sinai.",

        "key_verse": {
            "ref": "Deuteronomy 28:15",
            "text": "But if you will not obey the voice of the LORD your God or be careful to do all his commandments and his statutes that I command you today, then all these curses shall come upon you and overtake you.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05d1\u05b0\u05bc\u05e8\u05b4\u05d9\u05ea (berit)",
                "meaning": "'Covenant, treaty, pact.' The central legal concept of the Hebrew Bible. "
                           "A berit is not a casual agreement but a formally ratified, legally binding "
                           "commitment sealed with an oath and often with blood (cf. Genesis 15:9-17, "
                           "the covenant of the pieces). The Sinai berit follows the ANE suzerainty "
                           "treaty pattern precisely: the great king (YHWH) establishes terms with "
                           "the vassal (Israel), and both parties are bound by the stipulations. The "
                           "prophets prosecute violations of this specific legal instrument."
            },
            {
                "term": "\u05e7\u05b0\u05dc\u05b8\u05dc\u05b8\u05d4 (qelalah)",
                "meaning": "'Curse, imprecation.' From the root q-l-l ('to be light, to be trifling, "
                           "to curse'). Deuteronomy 28:15-68 contains the curse list of the Sinai "
                           "covenant -- 54 verses of escalating penalties for covenant violation. "
                           "These are not threats invented in the moment but pre-agreed penalties "
                           "formally accepted when Israel ratified the covenant (Deut 27:15-26, where "
                           "the people respond 'Amen' to each curse). The prophets do not invent "
                           "punishments -- they announce that the qelalah agreed upon at Sinai is "
                           "now being activated."
            },
            {
                "term": "\u05ea\u05bc\u05d5\u05b9\u05e8\u05b8\u05d4 (torah)",
                "meaning": "'Instruction, law, teaching.' From the root y-r-h ('to throw, to shoot, "
                           "to direct, to teach'). Torah is not merely 'law' in the Western legal "
                           "sense -- it is the covenant document itself: the terms, stipulations, "
                           "and instructions that define the relationship between YHWH and Israel. "
                           "Deuteronomy is structured as a covenant renewal document: preamble (1:1-5), "
                           "historical prologue (1:6-4:43), stipulations (5-26), blessings and curses "
                           "(27-28), witnesses and deposit (30-31). When the prophets accuse Israel of "
                           "abandoning the torah, they mean abandoning the covenant instrument."
            },
            {
                "term": "\u05de\u05b7\u05de\u05b0\u05dc\u05b8\u05db\u05b8\u05d4 (mamlakah)",
                "meaning": "'Kingdom, royal dominion.' Exodus 19:6 defines Israel's covenant identity: "
                           "'You shall be to me a kingdom of priests (mamlekhet kohanim) and a holy "
                           "nation (goy qadosh).' This is suzerainty language: YHWH is the great king, "
                           "Israel is his royal vassal entrusted with a priestly function among the "
                           "nations. The covenant is not just a moral code but a political constitution "
                           "establishing Israel's role in YHWH's cosmic administration. When Israel "
                           "violates the covenant, it is not just sin -- it is political rebellion "
                           "against the suzerain."
            }
        ],

        "ane_backdrop": "The parallels between the Sinai covenant and Hittite suzerainty treaties of the "
                       "14th-13th centuries BC are among the most significant discoveries in biblical "
                       "scholarship. George Mendenhall and Kenneth Kitchen independently demonstrated "
                       "that Deuteronomy follows the six-part Hittite treaty structure: (1) preamble "
                       "identifying the great king, (2) historical prologue of past benefits, (3) "
                       "stipulations, (4) deposit and reading provisions, (5) divine witnesses, (6) "
                       "blessings and curses. Later Assyrian treaties (7th century BC), like "
                       "Esarhaddon's Vassal Treaties, also contain curse lists with striking parallels "
                       "to Deuteronomy 28 -- diseases, famine, siege, exile. The question of dating "
                       "(Hittite-era or Assyrian-era) remains debated, but the treaty genre itself is "
                       "undeniable. The prophets operate as covenant enforcement agents within this "
                       "established international legal framework.",

        "second_temple": [
            {
                "source": "11QTemple (Temple Scroll, Qumran)",
                "summary": "The Temple Scroll rewrites Deuteronomy's covenant laws in first person as "
                           "YHWH's direct speech, treating the Sinai covenant as a living, expandable "
                           "legal document rather than a closed text.",
                "relevance": "The Qumran community saw the covenant as actively enforceable and "
                            "expandable -- the same view the prophets held when they prosecuted "
                            "violations centuries earlier."
            },
            {
                "source": "4QMMT (Miqsat Ma'ase Ha-Torah, Qumran)",
                "summary": "This halakhic letter from Qumran addresses specific Torah observances and "
                           "invokes blessings and curses language reminiscent of Deuteronomy 28-30, "
                           "showing ongoing Second Temple engagement with covenant prosecution.",
                "relevance": "Even in the Second Temple period, communities invoked the Deuteronomic "
                            "blessing/curse framework to prosecute perceived covenant violations -- "
                            "the same mechanism the prophets used."
            },
            {
                "source": "Jubilees 1:7-18",
                "summary": "Jubilees narrates YHWH warning Moses that Israel will forsake the covenant "
                           "and face the curses, then eventually return -- the same prosecution-to-"
                           "restoration pattern found in the canonical prophets.",
                "relevance": "The riv pattern of charge, sentence, and eventual restoration was "
                            "embedded in Second Temple retellings of the Sinai narrative."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 19:3-6", "note": "'You shall be to me a kingdom of priests and a holy nation' -- Israel's covenant identity as YHWH's vassal kingdom with priestly function", "type": "ot"},
            {"ref": "Exodus 20:1-17", "note": "The Decalogue as the core stipulations of the Sinai covenant -- the specific terms the prophets later prosecute violations of", "type": "ot"},
            {"ref": "Deuteronomy 28:1-68", "note": "The complete blessing and curse list of the Sinai covenant -- the penalty schedule that every prophet activates", "type": "ot"},
            {"ref": "Leviticus 26:14-45", "note": "The parallel curse list with escalating stages of punishment: illness, defeat, famine, wild beasts, siege, exile -- and the promise of eventual restoration", "type": "ot"},
            {"ref": "Deuteronomy 31:9-13", "note": "The covenant document deposited beside the Ark and read publicly every seven years -- treaty deposit and review provisions", "type": "ot"},
            {"ref": "Joshua 24:1-27", "note": "Covenant renewal at Shechem following the suzerainty treaty structure: historical prologue, stipulations, witnesses, deposit", "type": "ot"},
            {"ref": "Galatians 3:10-14", "note": "Paul cites Deuteronomy 27:26 -- 'Cursed be everyone who does not abide by all things written in the Book of the Law' -- and declares Christ became a curse to redeem from covenant curses", "type": "nt"},
            {"ref": "Hebrews 8:6-13", "note": "The new covenant is 'better' because it is enacted on 'better promises' -- the author reads the Sinai covenant through the prophetic lens of Jeremiah 31", "type": "nt"},
            {"ref": "4QMMT (Qumran)", "note": "The Qumran halakhic letter invokes Deuteronomic blessing/curse language to prosecute perceived covenant violations in the Second Temple period", "type": "dss"}
        ],

        "divine_council_note": "The Sinai covenant itself is a divine council event. Exodus 19:16-20 "
                              "describes the theophany at Sinai with fire, smoke, thunder, and the "
                              "mountain trembling -- the visible manifestation of YHWH's arrival with "
                              "his heavenly court. Deuteronomy 33:2 says 'The LORD came from Sinai... "
                              "he came from the ten thousands of holy ones' -- the 'holy ones' are "
                              "the members of the divine council who accompanied YHWH to the covenant "
                              "ratification. Acts 7:53 and Galatians 3:19 state that the law was "
                              "'delivered by angels' -- the council participated in the treaty process. "
                              "When the prophets later prosecute covenant violations, they are enforcing "
                              "an agreement that was witnessed and mediated by the divine council itself. "
                              "The council was present at the signing, and the council sends the "
                              "prosecutors when the terms are violated.",

        "sections": [
            {
                "heading": "The Suzerainty Treaty Pattern -- What Ancient Treaties Looked Like",
                "body": "In the ancient world, when a great king conquered or entered alliance with a lesser kingdom, the relationship was formalized in a suzerainty treaty. These were not agreements between equals -- they were imposed by a superior power on a subordinate, though often after an act of deliverance that created obligation. The Hittite treaties of the 14th-13th centuries BC follow a consistent six-part structure that biblical scholars have recognized in the Sinai covenant. First, the preamble: 'These are the words of the Sun, Suppiluliuma, the great king, the king of Hatti, the hero' -- identifying the suzerain by name and titles. Compare Exodus 20:2a: 'I am YHWH your God.' Second, the historical prologue: a recitation of what the great king has done for the vassal. Compare Exodus 20:2b: 'who brought you out of the land of Egypt, out of the house of slavery.' Third, stipulations: what the vassal must do and must not do. Compare the Decalogue and the Book of the Covenant (Exodus 20-23). Fourth, deposit and reading provisions: the treaty document is stored in the vassal's temple and read publicly at regular intervals. Compare Deuteronomy 31:9-13. Fifth, witnesses: typically the gods of both parties. Compare Deuteronomy 4:26 where heaven and earth serve as witnesses. Sixth, blessings for compliance and curses for violation. Compare Deuteronomy 28. The pattern is unmistakable."
            },
            {
                "heading": "Deuteronomy 28 -- The Curse List Every Prophet Quotes",
                "body": "Deuteronomy 28 is the single most important chapter for understanding the prophets, because it is the penalty schedule they enforce. The chapter begins with blessings for obedience (28:1-14) -- agricultural abundance, military victory, international prestige. Then comes the curse list (28:15-68), and its detail is staggering. Plague and disease (28:21-22): 'The LORD will strike you with wasting disease and with fever, inflammation and fiery heat.' Drought (28:23-24): 'The heavens over your head shall be bronze, and the earth under you shall be iron.' Military defeat (28:25): 'The LORD will cause you to be defeated before your enemies.' Madness (28:28): 'The LORD will strike you with madness and blindness and confusion of mind.' Siege (28:52-57): conditions so extreme that parents eat their own children. Exile (28:63-68): 'The LORD will scatter you among all peoples, from one end of the earth to the other.' When Isaiah announces destruction, when Jeremiah weeps over Jerusalem, when Ezekiel describes siege and exile -- they are not predicting based on political analysis. They are reading from the penalty schedule that Israel formally accepted at Sinai. The people said 'Amen' to every curse (Deuteronomy 27:15-26). The prophets are simply reminding them of what they agreed to."
            },
            {
                "heading": "The Prophet as Attorney -- YHWH as Plaintiff, Judge, and King",
                "body": "In a human legal system, the roles of plaintiff, judge, and prosecutor are separated to ensure fairness. In the covenant lawsuit, YHWH holds all three roles simultaneously -- and this is not a defect but a feature of divine sovereignty. YHWH is the plaintiff: he is the wronged party whose covenant partner has been unfaithful. The marriage metaphor in Hosea makes this visceral -- YHWH is the faithful husband whose wife has committed adultery with other gods. YHWH is the judge: he evaluates the evidence and renders the verdict. Psalm 82 shows him taking his seat in the divine council to judge. YHWH is the king: he is the suzerain whose vassal has rebelled, and he has the sovereign right to enforce the treaty. The prophet's role in this system is the attorney -- the prosecuting counsel who presents the case. He does not render the verdict (that is YHWH's role) or execute the sentence (that is delegated to agents, sometimes foreign nations like Assyria and Babylon, which Isaiah 10:5 calls 'the rod of my anger'). The prophet presents the charges, recites the evidence, and announces the sentence. This is why the prophets can weep over the very judgment they announce -- Jeremiah does not want Jerusalem destroyed, but his job is to deliver the court's ruling, not to change it."
            },
            {
                "heading": "Covenant Violation as Cosmic Treason",
                "body": "The prophets do not treat Israel's sins as mere moral failures -- they treat them as political rebellion against the cosmic sovereign. This is because the Sinai covenant is not just a moral code but a political constitution. Exodus 19:6 establishes Israel as 'a kingdom of priests and a holy nation' -- a vassal kingdom with a specific administrative function in YHWH's cosmic government. When Israel worships other gods, it is not just breaking a commandment -- it is committing treason by recognizing a rival sovereign. Jeremiah 2:11-13 captures the magnitude: 'Has a nation changed its gods, even though they are no gods? But my people have changed their glory for that which does not profit... they have forsaken me, the fountain of living waters, and hewed out cisterns for themselves, broken cisterns that can hold no water.' The double charge is devastating: treason (switching allegiance) and stupidity (switching to gods that do not even work). Ezekiel pushes further -- his graphic metaphors of Israel as an adulterous wife (ch. 16, 23) are covenant language: the berit between YHWH and Israel is a marriage covenant, and idolatry is adultery. This is why the penalty is so severe. This is not a disappointed teacher grading poorly -- this is a king executing the penalty clause for high treason, a husband responding to betrayal, a suzerain enforcing a treaty that the vassal voluntarily entered and then systematically violated."
            }
        ]
    }
]
