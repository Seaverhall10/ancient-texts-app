"""
era_35_commission.py -- Joshua's Commission & Entry (Joshua 1-5)

YHWH commissions Joshua as Moses' successor, the spies enter Jericho and
encounter Rahab, Israel crosses the Jordan on dry ground (a new exodus), and
the Commander of YHWH's army appears at Gilgal -- the most significant
theophany since the burning bush. This opening sequence establishes that the
conquest is a divine warrior operation: YHWH fights, Israel obeys.
"""

CHAPTERS = [
    {
        "id": "josh-1",
        "ref": "Joshua 1",
        "chapter_num": 1,
        "title": "The Divine Warrior Commissions His General",
        "era": "commission",
        "type": "chapter",
        "themes": ["COV", "LAND", "LAW"],

        "synopsis": "After Moses' death, YHWH speaks directly to Joshua son of Nun with a charge "
                    "that echoes the language of a suzerain commissioning his vassal commander: 'Be "
                    "strong and courageous' (repeated three times in 1:6, 7, 9). The land promise "
                    "is reaffirmed -- from the wilderness to Lebanon, from the Euphrates to the "
                    "Mediterranean (1:4), matching the Abrahamic boundaries of Genesis 15:18-21. "
                    "YHWH promises his personal presence: 'Just as I was with Moses, so I will be "
                    "with you. I will not leave you or forsake you' (1:5). The condition is "
                    "obedience to 'all the law that Moses my servant commanded you' -- Torah "
                    "meditation day and night (1:8). Joshua then commands the officers to prepare "
                    "provisions: in three days Israel will cross the Jordan. He reminds the "
                    "Transjordan tribes (Reuben, Gad, half-Manasseh) of their obligation to cross "
                    "over armed and fight with their brothers before returning to their inheritance "
                    "east of the Jordan. Their response affirms total loyalty: 'Whoever rebels "
                    "against your commandment and disobeys your words, whatever you command him, "
                    "shall be put to death' (1:18). The chapter establishes the theological "
                    "framework for the entire book: the conquest is YHWH's initiative, Joshua is "
                    "his commissioned agent, and success depends on covenant faithfulness.",

        "key_verse": {
            "ref": "Joshua 1:5",
            "text": "No man shall be able to stand before you all the days of your life. Just as I was with Moses, so I will be with you. I will not leave you or forsake you.",
            "translation": "ESV"
        },

        "original_terms": [
            "chazaq (be strong -- the same charge given to warriors before battle)",
            "amats (be courageous -- firm, resolute, unyielding)",
            "yehoshua (YHWH saves/delivers -- Joshua's name, identical to 'Jesus')",
            "eved YHWH (servant of YHWH -- the title Moses held, now transferring to Joshua)",
            "torah (law/instruction -- the covenant document Joshua must meditate on)",
            "nachalah (inheritance -- the land as YHWH's gift to Israel)",
            "hagah (to meditate/murmur -- audible recitation of Torah, day and night)"
        ],

        "ane_backdrop": "The commissioning of Joshua follows the pattern of ancient Near Eastern "
                        "royal succession texts \u2014 particularly the <em>suzerain-vassal</em> model "
                        "(where a great king, the 'suzerain,' commissions a subordinate ruler, the "
                        "'vassal,' to carry out his will). In Hittite royal instructions, the dying king "
                        "commissions his successor with specific charges, promises divine support, "
                        "and demands loyalty to the treaty obligations. The Egyptian 'Installation "
                        "of the Vizier' texts (Rekhmire tomb, ~1450 BC) describe the pharaoh "
                        "charging his chief officer with the administration of justice and the "
                        "execution of royal commands. The triple 'be strong and courageous' formula "
                        "parallels ANE royal encouragement oracles, where the deity or suzerain "
                        "assures the new leader of divine backing. The promise of invincibility "
                        "('no man shall stand before you') echoes Assyrian royal inscriptions "
                        "where the god Ashur guarantees military victory. The critical difference: "
                        "in Israel, the commissioning comes from YHWH directly, not through a "
                        "human king. Joshua is not inheriting a throne but receiving a military "
                        "command from the divine warrior himself.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities V.1.1-2",
                "summary": "Josephus recounts Joshua's commissioning with emphasis on his military "
                           "qualities: 'a man of great courage and magnanimity, bold in action, "
                           "sagacious in counsel, and of singular piety toward God.'",
                "relevance": "Shows how Second Temple Judaism understood Joshua as the ideal "
                             "military-religious leader -- a warrior-prophet who combined martial "
                             "skill with Torah devotion."
            },
            {
                "source": "Sirach (Ecclesiasticus) 46:1-6",
                "summary": "Ben Sira praises Joshua as 'the successor of Moses in prophesying, "
                           "who became, in accordance with his name, great for the saving of God's "
                           "elect.' He emphasizes Joshua's role in the conquest and the sun miracle.",
                "relevance": "Sirach explicitly connects Joshua's name to his function: Yehoshua = "
                             "'YHWH saves,' and his military victories are acts of divine salvation."
            },
            {
                "source": "4QTestimonia (4Q175)",
                "summary": "A Qumran text that collects messianic proof-texts, including "
                           "Deuteronomy 18:18-19 (the prophet like Moses) and the Blessing of "
                           "Moses on Levi. The Joshua/prophet-like-Moses connection was live in "
                           "Second Temple expectation.",
                "relevance": "The Qumran community connected the Joshua tradition to messianic "
                             "expectation: a new Joshua would arise to lead a new conquest, "
                             "reclaiming the land from its spiritual occupiers."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 31:1-8", "note": "Moses' commission of Joshua: 'Be strong and courageous... the LORD himself goes before you'", "type": "ot"},
            {"ref": "Deuteronomy 34:9", "note": "Joshua filled with the spirit of wisdom because Moses laid hands on him", "type": "ot"},
            {"ref": "Hebrews 13:5", "note": "'I will never leave you nor forsake you' -- quoting Josh 1:5 as a promise for all believers", "type": "nt"},
            {"ref": "Hebrews 4:8-11", "note": "'For if Joshua had given them rest, God would not have spoken of another day later on' -- Joshua's rest was incomplete", "type": "nt"},
            {"ref": "Psalm 1:1-3", "note": "The righteous man meditates on Torah day and night and prospers -- the same promise given to Joshua in 1:8", "type": "ot"},
            {"ref": "Genesis 15:18-21", "note": "The Abrahamic land promise that Joshua 1:4 restates: from the Euphrates to the Mediterranean", "type": "ot"},
            {"ref": "Acts 7:45", "note": "Stephen references Joshua (Iesous) bringing the tabernacle into the land", "type": "nt"},
            {"ref": "Ephesians 6:10", "note": "'Be strong in the Lord and in the strength of his might' -- echoing the commissioning language of Joshua 1", "type": "nt"}
        ],

        "divine_council_note": "The commissioning of Joshua is a divine warrior text. YHWH speaks "
                               "as the supreme commander deploying his field general. The language "
                               "of invincibility ('no man shall stand before you') is not merely "
                               "military encouragement but a divine decree: YHWH the Most High, who "
                               "commands the heavenly host, guarantees that the earthly conquest will "
                               "succeed because the heavenly conquest has already been decided. The "
                               "transfer of authority from Moses to Joshua mirrors the divine council "
                               "pattern of succession: as God raised up Moses to confront Pharaoh (an "
                               "agent of Egypt's gods), he now raises up Joshua to confront the "
                               "Canaanite kings (agents of Canaan's gods). The threefold 'be strong "
                               "and courageous' echoes the divine encouragement oracles found "
                               "throughout the prophets when God sends his agents against spiritual "
                               "opposition. Joshua is not merely a military commander -- he is YHWH's "
                               "representative in a cosmic conflict to reclaim the land allotted to "
                               "the sons of God under the Deuteronomy 32:8-9 dispensation.",

        "sections": [
            {
                "heading": "YHWH's Charge to Joshua (1:1-5)",
                "body": "The book opens with a transition of cosmic significance: 'After the death "
                        "of Moses the servant of YHWH, YHWH said to Joshua son of Nun, Moses' "
                        "assistant (mesharet)...' (1:1). The title eved YHWH ('servant of YHWH') "
                        "is the highest honorific in the Old Testament -- it designates one who "
                        "serves directly in the divine court (cf. David in Psalm 89:3, the Servant "
                        "of Isaiah 42-53, and the angelic servants of Psalm 103:21). Moses held this "
                        "title; Joshua will earn it only at his death (Josh 24:29). For now he is "
                        "mesharet -- 'minister, attendant, assistant' -- the term used for priests "
                        "serving in the tabernacle and for angels ministering before God (Psalm 104:4). "
                        "The commission is framed as a land grant: 'Every place that the sole of your "
                        "foot will tread upon I have given to you, as I promised Moses' (1:3). The "
                        "verb 'I have given' (natatti) is a prophetic perfect -- the action is so "
                        "certain in God's purposes that it is described as already accomplished. The "
                        "boundaries match the Abrahamic promise (Gen 15:18-21): the wilderness to "
                        "the south, Lebanon to the north, the Euphrates to the east, the "
                        "Mediterranean to the west. This is not incremental territory but the "
                        "full scope of YHWH's land grant to his people. The promise of presence "
                        "is the theological center: 'Just as I was with Moses, so I will be with "
                        "you' (1:5). The verb 'to be with' (hayah im) is covenant language -- "
                        "God's personal, ongoing, active accompaniment. What made Moses effective "
                        "was not his eloquence or military skill but YHWH's presence; the same "
                        "presence now transfers to Joshua."
            },
            {
                "heading": "The Condition of Torah Obedience (1:6-9)",
                "body": "YHWH's charge intensifies with three imperatives. The first 'be strong and "
                        "courageous' (chazaq ve'emats) in verse 6 relates to the conquest itself: "
                        "'for you shall cause this people to inherit the land.' The second (1:7) "
                        "shifts to Torah: 'Only be strong and very courageous, being careful to do "
                        "according to all the law (torah) that Moses my servant commanded you.' The "
                        "third (1:9) returns to the foundational promise: 'Have I not commanded you? "
                        "Be strong and courageous. Do not be frightened, and do not be dismayed, for "
                        "the LORD your God is with you wherever you go.' The middle charge is the "
                        "hinge: military courage requires Torah obedience. Joshua must not 'turn from "
                        "it to the right hand or to the left' (1:7) -- the same language Deuteronomy "
                        "uses for covenant faithfulness (Deut 5:32; 17:11, 20). The command to "
                        "'meditate on it day and night' (1:8) uses the verb hagah, which means "
                        "'to murmur, to recite audibly.' This is not silent contemplation but "
                        "continuous verbal engagement with the text -- a practice attested in ANE "
                        "scribal education where students memorized texts by constant recitation. "
                        "The promise attached to Torah meditation is remarkable: 'then you will make "
                        "your way prosperous, and then you will have good success' (1:8). The Hebrew "
                        "word for 'success' (sakal) means 'to act wisely, to understand, to prosper' "
                        "-- the same root used for the Suffering Servant who will 'deal wisely' "
                        "(Isaiah 52:13). Success in the conquest is redefined as Torah-shaped wisdom, "
                        "not military genius."
            },
            {
                "heading": "Joshua Commands the Officers (1:10-15)",
                "body": "Joshua immediately exercises his new authority: he commands the officers "
                        "(shoterim) to go through the camp and order the people to prepare provisions "
                        "(tsedah), 'for within three days you are to pass over this Jordan to go in "
                        "to take possession of the land that the LORD your God is giving you' (1:11). "
                        "The three-day preparation period is significant: it matches the three-day "
                        "preparation before the Sinai theophany (Exod 19:10-11, 15) and establishes "
                        "the crossing as a sacred event requiring ritual readiness. Joshua then "
                        "addresses the Transjordan tribes -- Reuben, Gad, and the half-tribe of "
                        "Manasseh -- reminding them of Moses' command: 'The LORD your God is giving "
                        "you rest and will give you this land' (1:13), but 'all your men of valor "
                        "shall pass over armed before your brothers' (1:14). They may have received "
                        "their inheritance, but the covenant community is indivisible: no tribe rests "
                        "while others fight. This principle -- solidarity within the covenant "
                        "community -- runs through the entire book and will surface dramatically in "
                        "the Transjordan altar controversy of chapter 22. The obligation of the "
                        "eastern tribes to fight for their western brothers models a theology of "
                        "mutual responsibility that transcends individual tribal interest."
            },
            {
                "heading": "The People's Response: Total Loyalty (1:16-18)",
                "body": "The Transjordan tribes respond with an oath of absolute loyalty: 'All that "
                        "you have commanded us we will do, and wherever you send us we will go. "
                        "Just as we obeyed Moses in all things, so we will obey you' (1:16-17). "
                        "They add a promise of divine accompaniment: 'Only may the LORD your God be "
                        "with you, as he was with Moses!' (1:17) -- recognizing that Joshua's "
                        "authority depends on YHWH's presence, not on Joshua himself. Their final "
                        "declaration is startling in its severity: 'Whoever rebels against your "
                        "commandment and disobeys your words, whatever you command him, shall be "
                        "put to death' (1:18). They impose the death penalty on covenant rebellion "
                        "against Joshua's authority -- a self-imprecation that mirrors the covenant "
                        "curse tradition of Deuteronomy 27-28. The chapter closes with their own "
                        "echo of YHWH's charge: 'Only be strong and courageous.' The same words "
                        "that God spoke to Joshua, the people now speak back to him. The effect is "
                        "a cascading chain of encouragement: YHWH strengthens Joshua, and Joshua's "
                        "people strengthen him in return. The contrast with the first generation at "
                        "Kadesh-barnea (Num 13-14) is deliberate and dramatic: where the parents "
                        "rebelled and refused to enter, the children pledge their lives to the "
                        "conquest. This is the second generation that Deuteronomy prepared."
            }
        ]
    },

    {
        "id": "josh-2",
        "ref": "Joshua 2",
        "chapter_num": 2,
        "title": "Rahab and the Spies -- Chaos Tamed by Faith",
        "era": "commission",
        "type": "chapter",
        "themes": ["WOMEN", "PROV", "SEED"],

        "synopsis": "Joshua sends two spies to reconnoiter Jericho. They enter the house of Rahab "
                    "(rahav), a prostitute (zonah) whose name is identical to the Hebrew word for "
                    "the cosmic chaos monster (rahab/rahav -- Isa 51:9; Ps 89:10; Job 26:12). This "
                    "wordplay is theologically loaded: the woman named 'Chaos' becomes the agent of "
                    "YHWH's order. Rahab hides the spies on her roof, lies to the king's messengers, "
                    "and confesses a remarkable theology: 'The LORD your God, he is God in the "
                    "heavens above and on the earth beneath' (2:11) -- a declaration of YHWH's "
                    "cosmic supremacy that echoes Deuteronomy 4:39. She reports that the Canaanites' "
                    "hearts have 'melted' (masas) at news of the Red Sea crossing and the defeat of "
                    "Sihon and Og. The psychological warfare described in Joshua 1 is confirmed: "
                    "YHWH's reputation has preceded his army. Rahab negotiates salvation for her "
                    "entire household by tying a scarlet cord (tikvat chut hashani) in her window "
                    "-- a sign that will mark her house for preservation when Jericho falls. The "
                    "spies swear an oath: anyone inside Rahab's house will live; anyone outside "
                    "will die. The scarlet cord has been compared to the Passover blood on the "
                    "doorposts (Exod 12:7, 13) -- a sign that protects from divine judgment. Rahab "
                    "the Canaanite prostitute becomes an ancestor of David and Jesus (Matt 1:5).",

        "key_verse": {
            "ref": "Joshua 2:11",
            "text": "And as soon as we heard it, our hearts melted, and there was no spirit left in any man because of you, for the LORD your God, he is God in the heavens above and on the earth beneath.",
            "translation": "ESV"
        },

        "original_terms": [
            "rahab/rahav (proud one/chaos monster -- the same name as the primordial sea dragon)",
            "zonah (prostitute -- also used metaphorically for spiritual unfaithfulness)",
            "masas (to melt -- the dissolution of courage; used for wax melting before fire)",
            "tikvah (cord/hope -- the scarlet cord; the same word means 'hope' in Hebrew)",
            "chesed (loyal love/kindness -- the covenant virtue Rahab asks for and receives)",
            "ot (sign -- the scarlet cord as a marker of salvation, parallel to Passover blood)",
            "meraglim (spies -- from regel, 'foot'; those who walk through the land)"
        ],

        "ane_backdrop": "Rahab's profession and her house's location on the city wall are "
                        "historically plausible. Casemate walls in Late Bronze Age Canaan (double "
                        "walls with rooms between them) are archaeologically attested, and the rooms "
                        "were often used as dwellings and storerooms. Prostitution was integrated "
                        "into ANE urban economies, and a prostitute's house near the gate would "
                        "be a natural intelligence-gathering location where foreigners could visit "
                        "without arousing suspicion. The flax drying on Rahab's roof (2:6) reflects "
                        "the spring harvest season and is consistent with the timing of the Jordan "
                        "crossing during the spring flood. The scarlet cord has parallels in "
                        "apotropaic (protective) practices throughout the ANE: Mesopotamian texts "
                        "describe colored cords tied to doorways to ward off demons. The name "
                        "'Rahab' connects to the mythological chaos monster: in Ugaritic texts, "
                        "the sea monster (Yam/Litanu) is defeated by Baal; in Israelite theology, "
                        "Rahab is the chaos dragon defeated by YHWH (Isa 51:9). A Canaanite woman "
                        "bearing this cosmic name who submits to YHWH is a powerful literary and "
                        "theological statement.",

        "second_temple": [
            {
                "source": "Hebrews 11:31",
                "summary": "Rahab is included in the 'hall of faith': 'By faith Rahab the "
                           "prostitute did not perish with those who were disobedient, because "
                           "she had given a friendly welcome to the spies.'",
                "relevance": "The New Testament celebrates Rahab's faith as exemplary -- a Canaanite "
                             "outsider who recognized YHWH's supremacy and acted on that recognition, "
                             "foreshadowing Gentile inclusion in the covenant."
            },
            {
                "source": "James 2:25",
                "summary": "'Was not also Rahab the prostitute justified by works when she "
                           "received the messengers and sent them out by another way?'",
                "relevance": "James uses Rahab as a case study for faith-working-through-action. "
                             "Her 'work' (hiding the spies) was the visible expression of her "
                             "invisible faith confession (2:11)."
            },
            {
                "source": "1 Clement 12:1-8",
                "summary": "Clement of Rome (~96 AD) praises Rahab for her faith and hospitality, "
                           "and identifies the scarlet cord as a type of redemption through Christ's "
                           "blood: 'They made clear that through the blood of the Lord redemption "
                           "would come to all who believe and hope in God.'",
                "relevance": "The earliest post-apostolic interpretation already connects the scarlet "
                             "cord to Christ's blood -- a typological reading that persisted throughout "
                             "patristic exegesis."
            },
            {
                "source": "Josephus, Antiquities V.1.2",
                "summary": "Josephus describes Rahab as an 'innkeeper' (pandokeutria) rather than "
                           "a prostitute, possibly to soften the narrative for his Greco-Roman "
                           "audience.",
                "relevance": "Josephus' euphemism reveals the discomfort some Second Temple readers "
                             "felt about a prostitute playing such a heroic role -- a tension the "
                             "biblical text embraces rather than avoids."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 51:9-10", "note": "'Was it not you who cut Rahab in pieces, who pierced the dragon?' -- YHWH defeating the chaos monster, the cosmic namesake of the Jericho prostitute", "type": "ot"},
            {"ref": "Psalm 89:10", "note": "'You crushed Rahab like a carcass; you scattered your enemies with your mighty arm' -- the chaos monster defeated by YHWH the divine warrior", "type": "ot"},
            {"ref": "Matthew 1:5", "note": "'Salmon the father of Boaz by Rahab' -- Rahab enters the genealogy of Jesus, a Canaanite woman in the Messianic line", "type": "nt"},
            {"ref": "Exodus 12:7, 13", "note": "Passover blood on the doorposts as the sign of protection -- parallels the scarlet cord on Rahab's window", "type": "ot"},
            {"ref": "Numbers 13:1-3, 25-33", "note": "The first spy mission from Kadesh-barnea that failed -- this mission succeeds because the spies return with faith, not fear", "type": "ot"},
            {"ref": "Hebrews 11:31", "note": "Rahab's faith celebrated in the hall of faith: she did not perish with the disobedient", "type": "nt"},
            {"ref": "Job 26:12-13", "note": "'By his power he stilled the sea; by his understanding he shattered Rahab' -- the cosmic chaos monster subdued by YHWH", "type": "ot"},
            {"ref": "Deuteronomy 4:39", "note": "'The LORD is God in heaven above and on the earth beneath' -- the exact confession Rahab makes in Josh 2:11", "type": "ot"}
        ],

        "divine_council_note": "Rahab's confession (2:11) is a divine council declaration: 'The "
                               "LORD your God, he is God in the heavens above and on the earth "
                               "beneath.' This is the language of cosmic supremacy -- YHWH rules both "
                               "the heavenly realm (where the 'elohim dwell) and the earthly realm "
                               "(where the nations they govern reside). A Canaanite woman making this "
                               "confession is extraordinary: she is acknowledging that YHWH is superior "
                               "to whatever gods Jericho serves. The name 'Rahab' (rahav) deepens the "
                               "significance. In Israelite cosmic mythology, Rahab is the chaos sea "
                               "monster that YHWH defeated at creation (Isa 51:9; Ps 89:10; Job 26:12). "
                               "A woman named 'Chaos' who submits to YHWH and is incorporated into "
                               "Israel is a narrative enactment of the chaos-to-order motif: YHWH does "
                               "not merely destroy chaos -- he redeems it. The scarlet cord functions "
                               "as an apotropaic sign (like the Passover blood) that marks Rahab's "
                               "house as protected territory within the condemned city. Just as YHWH's "
                               "judgment 'passed over' the blood-marked houses in Egypt, it will pass "
                               "over the cord-marked house in Jericho. The Canaanite woman named after "
                               "the chaos monster becomes an ancestor of the Messiah (Matt 1:5) -- "
                               "the ultimate transformation of chaos into redemptive order.",

        "sections": [
            {
                "heading": "The Spy Mission and Rahab's House (2:1-7)",
                "body": "Joshua sends two spies 'secretly' (cheresh) to 'view the land, especially "
                        "Jericho' (2:1). The secrecy contrasts with the very public failure of the "
                        "twelve spies at Kadesh-barnea (Num 13) -- Joshua has learned from history. "
                        "The spies enter Jericho and 'came into the house of a prostitute (ishah "
                        "zonah) whose name was Rahab, and lodged there' (2:1). The choice of lodging "
                        "is pragmatic: a prostitute's house was one of the few places where foreign "
                        "men could stay without raising immediate alarm. But the literary significance "
                        "transcends the pragmatic. The Hebrew word zonah (prostitute) is also the "
                        "word the prophets use for spiritual unfaithfulness -- Israel 'playing the "
                        "harlot' with other gods (Hosea 1-3; Ezekiel 16, 23). A literal zonah in "
                        "Canaan who turns to YHWH inverts the metaphor: where Israel will repeatedly "
                        "play the harlot with Canaanite gods, a Canaanite harlot proves more "
                        "faithful than the covenant people. The king of Jericho learns of the spies "
                        "and sends messengers to Rahab demanding she produce them. She hides them "
                        "among stalks of flax (pishtei ha'ets) drying on the roof -- a detail that "
                        "confirms the spring season (flax harvest in March-April) and Rahab's "
                        "involvement in the textile trade, which was common for women of her "
                        "profession. She lies to the king's messengers, sending them on a false "
                        "pursuit toward the Jordan fords."
            },
            {
                "heading": "Rahab's Confession of Faith (2:8-11)",
                "body": "After sending the king's men away, Rahab goes up to the roof and delivers "
                        "a theological confession that is among the most remarkable in the Old "
                        "Testament. She begins with intelligence: 'I know that the LORD has given "
                        "you the land, and that the fear of you has fallen upon us, and that all "
                        "the inhabitants of the land melt away before you' (2:9). The verb masas "
                        "('to melt') is the language of psychological collapse -- courage dissolving "
                        "like wax before fire (cf. Psalm 97:5, where mountains 'melt like wax before "
                        "the LORD'). She cites the evidence: 'For we have heard how the LORD dried "
                        "up the water of the Red Sea before you when you came out of Egypt, and "
                        "what you did to the two kings of the Amorites... Sihon and Og' (2:10). "
                        "Forty years after the exodus, YHWH's reputation still reverberates through "
                        "Canaan. Then comes the confession: 'For the LORD your God, he is God in "
                        "the heavens above and on the earth beneath' (2:11). This is the language "
                        "of Deuteronomy 4:39, the capstone of Moses' argument about YHWH's "
                        "incomparability. A Canaanite woman articulates the theology of the "
                        "Deuteronomic worldview -- YHWH's universal sovereignty over both the "
                        "heavenly and earthly realms. She has reached the conclusion that Israel's "
                        "parents at Kadesh-barnea refused to reach: YHWH is supreme, and resistance "
                        "is futile. The faith that the first generation lacked, a Canaanite "
                        "prostitute possesses."
            },
            {
                "heading": "The Covenant of the Scarlet Cord (2:12-21)",
                "body": "Rahab negotiates a covenant of protection: 'Now then, please swear to me "
                        "by the LORD that, as I have dealt kindly (chesed) with you, you also will "
                        "deal kindly with my father's house' (2:12). She uses the covenant term "
                        "chesed -- loyal love, faithfulness -- the word that defines YHWH's "
                        "relationship with Israel. She asks for a 'sure sign' (ot emet, 'sign of "
                        "truth') that her family will be spared. The spies agree: 'Our life for "
                        "yours! If you do not tell this business of ours, then when the LORD gives "
                        "us the land we will deal kindly and faithfully with you' (2:14). They "
                        "instruct her to tie a 'scarlet cord' (tikvat chut hashani) in the window "
                        "through which she lets them down (her house is built into the city wall). "
                        "The Hebrew word tikvah means both 'cord' and 'hope' -- Rahab's scarlet "
                        "cord is literally her 'scarlet hope.' The color scarlet (shani) links to "
                        "the Passover blood, the crimson sacrificial system, and the redemptive "
                        "bloodline that will run through her to David and to Jesus. The condition "
                        "is spatial: anyone inside Rahab's house when Jericho falls will live; "
                        "anyone outside will die. The house becomes a miniature ark of salvation "
                        "within the condemned city -- a space marked by the covenant sign where "
                        "divine judgment does not enter. The parallel to the Passover is exact: "
                        "the angel of death passed over the blood-marked houses in Egypt; the "
                        "herem will pass over the cord-marked house in Jericho."
            },
            {
                "heading": "The Spies' Report: The Land is Ours (2:22-24)",
                "body": "The spies hide in the hills for three days while the pursuit gives up, "
                        "then cross the Jordan and return to Joshua. Their report is the theological "
                        "antithesis of the first spies' report at Kadesh-barnea. Where the ten "
                        "unfaithful spies said, 'We are not able to go up against the people, for "
                        "they are stronger than we' (Num 13:31), these two say: 'Truly the LORD has "
                        "given all the land into our hands. And also, all the inhabitants of the "
                        "land melt away because of us' (2:24). The information is identical -- the "
                        "land is formidable and its inhabitants are powerful -- but the interpretation "
                        "is inverted. The same evidence that produced fear in the first generation "
                        "produces faith in the second. The difference is the Deuteronomy 32 "
                        "worldview: they know that YHWH has already decided the outcome. The "
                        "Canaanites' melting hearts confirm that YHWH's psychological warfare is "
                        "working. The divine warrior has gone ahead of his army. The stage is set "
                        "for the crossing."
            }
        ]
    },

    {
        "id": "josh-3",
        "ref": "Joshua 3",
        "chapter_num": 3,
        "title": "The Jordan Crossing -- Waters of Chaos Parted Again",
        "era": "commission",
        "type": "chapter",
        "themes": ["TYPE", "HOLY", "COV"],

        "synopsis": "Israel breaks camp at Shittim and moves to the Jordan's edge. The officers "
                    "instruct the people to follow the ark of the covenant at a distance of 2,000 "
                    "cubits (~3,000 feet), 'for you have not passed this way before' (3:4). Joshua "
                    "announces: 'Here is how you shall know that the living God (El Chai) is among "
                    "you and that he will without fail drive out from before you the Canaanites...' "
                    "(3:10). When the priests carrying the ark step into the Jordan -- at flood stage "
                    "during the spring harvest -- the waters stand up in a heap (ned) far upstream "
                    "at Adam (modern ed-Damiyeh), and the riverbed dries completely, allowing all "
                    "Israel to cross on dry ground (charavah). The crossing recapitulates the Red "
                    "Sea miracle with deliberate theological precision: the same God who parted the "
                    "sea to bring Israel out of Egypt now parts the river to bring Israel into "
                    "Canaan. The ark -- YHWH's throne -- leads the way, with the priests standing "
                    "in the middle of the dry riverbed until every last Israelite has crossed. The "
                    "crossing is the birth of a new nation in a new land, a second exodus that "
                    "completes the first. The water motif connects to the chaos tradition: YHWH's "
                    "sovereignty over water is his sovereignty over the cosmic forces that oppose "
                    "his purposes.",

        "key_verse": {
            "ref": "Joshua 3:10",
            "text": "And Joshua said, 'Here is how you shall know that the living God is among you and that he will without fail drive out from before you the Canaanites, the Hittites, the Hivites, the Perizzites, the Girgashites, the Amorites, and the Jebusites.'",
            "translation": "ESV"
        },

        "original_terms": [
            "aron habrit (ark of the covenant -- YHWH's portable throne)",
            "El Chai (the living God -- a divine title emphasizing YHWH's vitality vs. dead idols)",
            "ned (heap -- waters standing up; same word used at the Red Sea in Exod 15:8)",
            "charavah (dry ground -- the miraculous absence of water in the riverbed)",
            "kohanim (priests -- the carriers of the ark who lead the crossing)",
            "adam (the city upstream where the waters stopped -- wordplay on 'humanity/Adam')",
            "goy (nation -- all nations will know YHWH's power through this act)"
        ],

        "ane_backdrop": "River crossings were significant events in ANE military campaigns. "
                        "Assyrian royal inscriptions frequently describe crossing rivers as "
                        "demonstrations of divine favor: Ashurnasirpal II boasts of crossing the "
                        "Euphrates with the help of Ashur and Ishtar. Egyptian texts describe "
                        "Thutmose III's crossing of the Euphrates as aided by Amun-Re. The concept "
                        "of water as a cosmic boundary -- separating ordered territory from chaotic "
                        "wilderness -- is deeply rooted in Mesopotamian cosmology. In the Enuma Elish, "
                        "Marduk defeats Tiamat (the chaos sea) and creates the ordered world from "
                        "her body. In Canaanite mythology (Ugaritic texts), Baal defeats Yam (Sea) "
                        "to establish cosmic order. The Jordan crossing places YHWH in the role of "
                        "the cosmic warrior who conquers water-chaos: the river obeys his command, "
                        "opening a path through the boundary between wilderness and promised land. "
                        "The spring flood of the Jordan (3:15) makes the miracle more dramatic -- "
                        "at its most powerful, the river submits to YHWH's authority.",

        "second_temple": [
            {
                "source": "Psalm 114:3-5",
                "summary": "'The sea looked and fled; the Jordan turned back... What ails you, O "
                           "sea, that you flee? O Jordan, that you turn back?' -- a poetic "
                           "celebration that pairs the Red Sea and Jordan crossings as acts of "
                           "the same God.",
                "relevance": "Psalm 114 confirms that the Jordan crossing was understood as "
                             "theologically parallel to the Red Sea crossing -- both are acts of "
                             "YHWH's sovereignty over the waters of chaos."
            },
            {
                "source": "4QJosh^a (4Q47)",
                "summary": "The Dead Sea Scrolls Joshua manuscript preserves portions of chapters "
                           "3-4 with minor textual variations, confirming the stability of the "
                           "crossing narrative in the textual tradition.",
                "relevance": "The Qumran evidence shows the crossing narrative was transmitted with "
                             "care, reflecting its central theological importance."
            },
            {
                "source": "Josephus, Antiquities V.1.4",
                "summary": "Josephus describes the Jordan miracle and compares it to Alexander's "
                           "crossing of the Pamphylian Sea, suggesting divine intervention in both "
                           "cases.",
                "relevance": "Josephus' comparison shows how Second Temple authors used the crossing "
                             "as an apologetic tool -- YHWH's power exceeds even the legends attributed "
                             "to Alexander."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 14:21-22", "note": "The Red Sea parting -- the original crossing miracle that the Jordan crossing recapitulates", "type": "ot"},
            {"ref": "Exodus 15:8", "note": "'The floods stood up in a heap (ned)' -- the same Hebrew word used for the Jordan waters in Josh 3:13, 16", "type": "ot"},
            {"ref": "Psalm 114:1-8", "note": "The Red Sea and Jordan crossings celebrated together as cosmic events", "type": "ot"},
            {"ref": "2 Kings 2:8, 14", "note": "Elijah and Elisha part the Jordan -- prophetic succession echoing the Joshua crossing", "type": "ot"},
            {"ref": "Matthew 3:13-17", "note": "Jesus' baptism in the Jordan -- the new Joshua (Yehoshua/Yeshua) enters the water and the Spirit descends", "type": "nt"},
            {"ref": "Psalm 74:12-15", "note": "'You divided the sea by your might; you broke the heads of the sea monsters' -- YHWH's water-sovereignty as cosmic victory", "type": "ot"},
            {"ref": "Isaiah 43:2", "note": "'When you pass through the waters, I will be with you' -- the promise of divine presence at water crossings", "type": "ot"}
        ],

        "divine_council_note": "The Jordan crossing is a cosmic event, not merely a military one. "
                               "Water in ANE cosmology represents chaos -- the primordial force that "
                               "opposes divine order. YHWH's command over the Jordan is the same "
                               "authority he exercised at creation (Gen 1:6-10, separating the waters), "
                               "at the Red Sea (Exod 14), and in the defeat of the chaos monster "
                               "Rahab/Leviathan (Isa 51:9-10; Ps 74:12-15). The ark of the covenant "
                               "leads the crossing because it is YHWH's throne -- the divine King "
                               "himself enters the chaotic waters and subdues them. The priests stand "
                               "in the middle of the dry riverbed as YHWH's agents, holding open the "
                               "boundary between chaos and order while his people pass through. The "
                               "city where the waters stopped is named 'Adam' (3:16) -- whether "
                               "coincidence or literary design, the wordplay evokes the original Adam "
                               "and the original creation, suggesting that the conquest is a new "
                               "creation act: YHWH is bringing order to the land, reclaiming it from "
                               "the chaotic spiritual powers that have held it since the Deuteronomy "
                               "32:8-9 allotment went wrong.",

        "sections": [
            {
                "heading": "Preparation at the Jordan (3:1-6)",
                "body": "Israel moves from Shittim to the edge of the Jordan and camps for three "
                        "days. Shittim (full name Abel-shittim, 'meadow of acacias') is the last "
                        "campsite in the wilderness -- the place where Israel committed the sin of "
                        "Baal-peor (Num 25), where Balaam attempted to curse Israel (Num 22-24), "
                        "and where Moses delivered his farewell addresses (Deuteronomy). The three-day "
                        "wait (3:2) parallels the three-day preparation before Sinai (Exod 19:10-11), "
                        "establishing the crossing as a sacred event of similar magnitude. The officers "
                        "instruct the people to watch for the ark of the covenant carried by the "
                        "Levitical priests: 'When you see the ark of the covenant of the LORD your "
                        "God being carried by the Levitical priests, then you shall set out from your "
                        "place and follow it' (3:3). The 2,000-cubit distance between the people and "
                        "the ark serves both practical and theological purposes: practically, the "
                        "entire nation needs to see the ark to follow its route; theologically, the "
                        "distance maintains the graduated holiness that protects the people from the "
                        "dangerous presence of YHWH enthroned on the ark. Joshua commands: 'Consecrate "
                        "yourselves (hitqaddeshu), for tomorrow the LORD will do wonders among you' "
                        "(3:5). The verb hitqaddesh involves ritual washing and sexual abstinence -- "
                        "the same preparation required before Sinai. The crossing is a theophany."
            },
            {
                "heading": "The Ark Enters the Water (3:7-13)",
                "body": "YHWH speaks to Joshua: 'Today I will begin to exalt you in the sight of all "
                        "Israel, that they may know that, as I was with Moses, so I will be with you' "
                        "(3:7). The crossing serves as Joshua's authentication: as the Red Sea validated "
                        "Moses' authority, the Jordan will validate Joshua's. Joshua announces to the "
                        "people: 'Here is how you shall know that the living God (El Chai) is among "
                        "you' (3:10). The title 'El Chai' -- the living God -- contrasts YHWH with "
                        "the dead idols of Canaan and the inactive gods who cannot control nature. "
                        "YHWH is alive, present, and active. Joshua names seven nations to be driven "
                        "out: Canaanites, Hittites, Hivites, Perizzites, Girgashites, Amorites, and "
                        "Jebusites. Seven is the number of completeness -- the list signifies total "
                        "dispossession. The plan: 'When the soles of the feet of the priests bearing "
                        "the ark of the LORD, the Lord of all the earth (adon kol ha'arets), rest in "
                        "the waters of the Jordan, the waters of the Jordan shall be cut off' (3:13). "
                        "The title 'Lord of all the earth' is a divine council designation -- YHWH "
                        "is not merely Israel's national deity but the cosmic sovereign over all "
                        "territories and all nations. His authority extends over the Jordan because "
                        "his authority extends over everything."
            },
            {
                "heading": "The Miracle: Waters Stand Up (3:14-17)",
                "body": "The narrative slows to sacramental precision. 'The Jordan overflows all its "
                        "banks throughout the time of harvest' (3:15) -- the river is at maximum "
                        "flood stage. The spring snowmelt from Mount Hermon swells the Jordan to "
                        "a torrent in March-April, making this the most dangerous possible moment "
                        "to cross. Into this flood the priests walk with the ark. 'As soon as those "
                        "bearing the ark had come as far as the Jordan, and the feet of the priests "
                        "bearing the ark were dipped in the brink of the water... the waters coming "
                        "down from above stood and rose up in a heap (ned) very far away, at Adam' "
                        "(3:15-16). The word ned ('heap') is the identical term used in the Song of "
                        "the Sea for the Red Sea miracle: 'the floods stood upright as a heap' (Exod "
                        "15:8). The literary connection is deliberate: what YHWH did at the beginning "
                        "of the exodus, he now does at the end. The city named Adam is approximately "
                        "16 miles upstream -- the entire stretch of river below that point drains "
                        "completely. 'The people passed over opposite Jericho' (3:16) -- they crossed "
                        "at the exact point that faces their first military objective. The priests "
                        "'stood firmly on dry ground (charavah) in the midst of the Jordan' while "
                        "'all the nation finished passing over the Jordan' (3:17). The divine throne "
                        "stands in the middle of the conquered chaos, holding the waters apart, "
                        "while the people of God walk through on solid ground. It is creation and "
                        "exodus and conquest in a single act."
            }
        ]
    },

    {
        "id": "josh-4",
        "ref": "Joshua 4",
        "chapter_num": 4,
        "title": "Memorial Stones -- So That All Peoples May Know",
        "era": "commission",
        "type": "chapter",
        "themes": ["COV", "LAND", "NAME"],

        "synopsis": "After the crossing, YHWH commands Joshua to have twelve men -- one from each "
                    "tribe -- take twelve stones from the middle of the Jordan where the priests "
                    "stood and carry them to the camp at Gilgal. These stones will be a 'memorial' "
                    "(zikkaron) for future generations. When children ask 'What do these stones "
                    "mean?' (4:6, 21), the parents will recount the Jordan miracle. Joshua also "
                    "sets up twelve stones in the middle of the Jordan itself, at the place where "
                    "the priests' feet stood. The Transjordan tribes cross over armed, as commanded. "
                    "YHWH exalts Joshua in the sight of all Israel: 'they stood in awe of him just "
                    "as they had stood in awe of Moses, all the days of his life' (4:14). When the "
                    "priests carrying the ark come up from the Jordan, the waters return to flood "
                    "stage. The people camp at Gilgal, east of Jericho, and Joshua erects the twelve "
                    "stones there. The chapter's theological climax is the purpose statement: 'so "
                    "that all the peoples of the earth may know that the hand of the LORD is mighty, "
                    "that you may fear the LORD your God forever' (4:24). The memorial serves two "
                    "audiences: Israel (to remember and fear YHWH) and the nations (to know YHWH's "
                    "power). The twelve-stone memorial is covenant architecture -- a physical marker "
                    "of divine action that anchors memory in geography.",

        "key_verse": {
            "ref": "Joshua 4:23-24",
            "text": "For the LORD your God dried up the waters of the Jordan for you until you passed over, as the LORD your God did to the Red Sea, which he dried up for us until we passed over, so that all the peoples of the earth may know that the hand of the LORD is mighty, that you may fear the LORD your God forever.",
            "translation": "ESV"
        },

        "original_terms": [
            "zikkaron (memorial -- a physical marker designed to trigger covenant memory)",
            "avanim (stones -- the raw material of the memorial; twelve for twelve tribes)",
            "gilgal (rolling/circle -- the campsite named for the 'rolling away' of reproach)",
            "ot (sign -- the stones as a 'sign' of YHWH's faithfulness)",
            "yare (to fear/revere -- the response the memorial is designed to produce)",
            "yad YHWH (hand of YHWH -- the power and agency of God made visible)"
        ],

        "ane_backdrop": "Stone memorials (masseboth, standing stones) were ubiquitous in the "
                        "ancient Near East. They marked treaties, commemorated victories, identified "
                        "sacred sites, and served as boundary markers. The Kurkh Monolith of "
                        "Shalmaneser III (~853 BC) is a stone memorial recording military victories. "
                        "Egyptian pharaohs erected stelae throughout Canaan to mark their territorial "
                        "claims (the Beth-shean stelae of Seti I and Ramesses II). The practice of "
                        "taking stones from a conquered location and erecting them at a base camp "
                        "parallels the ANE practice of trophy display. The twelve-stone structure "
                        "reflects the twelve-tribe organization that is central to Israel's identity "
                        "-- each stone represents a tribe's participation in the divine miracle. The "
                        "catechetical function ('when your children ask...') is paralleled in the "
                        "Passover haggadah tradition (Exod 12:26-27) and reflects the ANE emphasis "
                        "on inter-generational memory transmission.",

        "second_temple": [
            {
                "source": "Mishnah Sotah 7:5",
                "summary": "The Mishnah records traditions about the Jordan crossing stones, "
                           "including their size and the inscriptions placed on them.",
                "relevance": "Demonstrates that the memorial stones tradition remained a subject "
                             "of active discussion in rabbinic Judaism."
            },
            {
                "source": "Josephus, Antiquities V.1.4",
                "summary": "Josephus describes the memorial stones at Gilgal and notes that they "
                           "were still visible in his day (1st century AD), serving as evidence "
                           "of the crossing miracle.",
                "relevance": "If Josephus' claim is accurate, the Gilgal stones persisted as a "
                             "physical monument for over a thousand years after the crossing."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 12:26-27", "note": "'When your children say to you, What do you mean by this service?' -- the Passover catechism parallels the Jordan stone catechism", "type": "ot"},
            {"ref": "Exodus 14:21-22", "note": "The Red Sea crossing explicitly compared to the Jordan crossing in 4:23", "type": "ot"},
            {"ref": "Genesis 28:18-22", "note": "Jacob's memorial stone at Bethel -- the tradition of stone memorials at sites of divine encounter", "type": "ot"},
            {"ref": "1 Samuel 7:12", "note": "Samuel sets up 'Ebenezer' (stone of help) after victory -- the same memorial stone tradition", "type": "ot"},
            {"ref": "Deuteronomy 6:20-25", "note": "'When your son asks you in time to come, What is the meaning of the testimonies...' -- the catechetical pattern Joshua 4 follows", "type": "ot"},
            {"ref": "1 Peter 2:4-5", "note": "'You yourselves like living stones are being built up as a spiritual house' -- believers as memorial stones of God's saving acts", "type": "nt"}
        ],

        "divine_council_note": "The purpose statement in 4:24 reveals the cosmic scope of the "
                               "Jordan memorial: 'so that ALL THE PEOPLES OF THE EARTH may know that "
                               "the hand of YHWH is mighty.' The memorial is not merely for Israel's "
                               "internal memory -- it is a declaration to the nations, a witness to "
                               "the peoples who have been allotted to other elohim (Deut 32:8-9) that "
                               "YHWH is the supreme power. The phrase 'hand of YHWH' (yad YHWH) is "
                               "anthropomorphic divine council language -- the same 'hand' that struck "
                               "Egypt (Exod 3:20), parted the Red Sea (Exod 14:31), and fought against "
                               "the wilderness generation (Deut 2:15). YHWH's 'hand' is his executive "
                               "power -- the agency by which the cosmic sovereign enacts his will in "
                               "the physical world. The twelve stones, one per tribe, collectively "
                               "represent YHWH's complete people -- his nachalah (inheritance) among "
                               "the nations, the portion he kept for himself when he allotted the "
                               "rest to the sons of God. The memorial at Gilgal says: YHWH has brought "
                               "his people home.",

        "sections": [
            {
                "heading": "The Twelve Stones from the Jordan (4:1-8)",
                "body": "As the nation finishes crossing, YHWH commands Joshua to select twelve "
                        "men, one from each tribe, and have them take twelve stones from the exact "
                        "spot in the middle of the Jordan where the priests' feet stood firm (4:3). "
                        "The specificity is important: these are not random stones but stones from "
                        "the place where YHWH's throne (the ark) held back the waters. They are "
                        "contact relics, saturated with the significance of the miracle. The stones "
                        "will serve as a zikkaron -- a 'memorial' -- a term used for the Passover "
                        "(Exod 12:14), the showbread (Lev 24:7), and the trumpet blasts (Num 10:10). "
                        "A zikkaron is not merely a reminder but a ritual anchor that makes a past "
                        "event present to future generations. When children ask 'What do these "
                        "stones mean to you?' (4:6), the parents will recount the miracle: 'The "
                        "waters of the Jordan were cut off before the ark of the covenant of the "
                        "LORD. When it passed over the Jordan, the waters of the Jordan were cut "
                        "off' (4:7). The catechetical structure -- child's question, parent's "
                        "answer -- mirrors the Passover haggadah and establishes a pattern of "
                        "liturgical memory that runs through Israelite worship. The twelve men "
                        "obey: they carry the stones to the campsite and lay them down there."
            },
            {
                "heading": "Stones in the River and the Armed Crossing (4:9-14)",
                "body": "Joshua also sets up twelve stones 'in the midst of the Jordan, in the "
                        "place where the feet of the priests bearing the ark of the covenant had "
                        "stood; and they are there to this day' (4:9). This second set of stones "
                        "is a submerged memorial -- invisible under normal water levels, known only "
                        "to those who remember the crossing. It is a hidden witness, a testimony "
                        "beneath the surface of the waters of chaos. The narrator's note 'to this "
                        "day' indicates the account was written while the stones were still known, "
                        "suggesting proximity to the events. The text emphasizes the military "
                        "character of the crossing: the Transjordan tribes -- 'about 40,000 ready "
                        "for war' (4:13) -- cross armed before the LORD 'for battle, to the "
                        "plains of Jericho.' This is not a refugee exodus but a military invasion "
                        "organized by the divine warrior. The result: 'On that day the LORD "
                        "exalted Joshua in the sight of all Israel, and they stood in awe of him, "
                        "just as they had stood in awe of Moses, all the days of his life' (4:14). "
                        "The Jordan crossing is to Joshua what the Red Sea was to Moses: the "
                        "authenticating miracle that establishes the leader's divine authority."
            },
            {
                "heading": "The Waters Return and the Camp at Gilgal (4:15-24)",
                "body": "YHWH commands the priests to come up from the Jordan. 'And when the "
                        "priests bearing the ark of the covenant of the LORD came up from the "
                        "midst of the Jordan, and the soles of the priests' feet were lifted up "
                        "on dry ground, the waters of the Jordan returned to their place and "
                        "overflowed all its banks, as before' (4:18). The waters return the "
                        "instant the ark leaves the riverbed -- YHWH's presence was the dam that "
                        "held back chaos. Without the divine throne in the water, the flood "
                        "resumes. The people camp at Gilgal on the eastern edge of Jericho on "
                        "the tenth day of the first month (4:19) -- exactly four days before "
                        "Passover (Exod 12:3), connecting the Jordan crossing to the exodus "
                        "liturgical calendar. Joshua sets up the twelve memorial stones at Gilgal "
                        "and delivers the purpose statement: 'So that all the peoples of the "
                        "earth may know that the hand of the LORD is mighty, that you may fear "
                        "the LORD your God forever' (4:24). The dual audience -- nations and Israel "
                        "-- reflects the dual function of YHWH's mighty acts: they demonstrate his "
                        "supremacy to the watching world and cultivate reverent fear in his own "
                        "people. Gilgal becomes the base camp for the conquest and will remain a "
                        "significant cult site throughout the period of the judges and early monarchy."
            }
        ]
    },

    {
        "id": "josh-5",
        "ref": "Joshua 5",
        "chapter_num": 5,
        "title": "Circumcision, Passover, and the Commander of YHWH's Army",
        "era": "commission",
        "type": "chapter",
        "themes": ["COV", "HOLY", "TYPE"],

        "synopsis": "Joshua 5 contains three episodes of extraordinary theological density. First, "
                    "the Canaanite and Amorite kings hear of the Jordan miracle and their hearts "
                    "'melt' (5:1) -- confirming Rahab's report and the divine warrior's psychological "
                    "campaign. Second, YHWH commands Joshua to circumcise the wilderness generation "
                    "at 'Gibeath-haaraloth' ('Hill of Foreskins'). The men born in the wilderness "
                    "had not been circumcised -- a forty-year lapse in the Abrahamic covenant sign "
                    "(Gen 17). YHWH declares: 'Today I have rolled away (galoti) the reproach of "
                    "Egypt from you' -- and the place is named Gilgal (from galal, 'to roll'). "
                    "Third, Israel celebrates the Passover at Gilgal on the fourteenth day of the "
                    "first month. The day after, they eat the produce of the land for the first "
                    "time, and the manna ceases. The wilderness provision ends because the land "
                    "provision begins. Fourth -- and most dramatic -- Joshua encounters a 'man' "
                    "standing with a drawn sword who identifies himself as the 'Commander (sar) of "
                    "the army (tseva) of YHWH' (5:14). Joshua falls on his face in worship and is "
                    "commanded to remove his sandals: 'the place where you are standing is holy' "
                    "(5:15) -- the exact words spoken to Moses at the burning bush (Exod 3:5). This "
                    "theophany is one of the most significant divine council encounters in the Old "
                    "Testament: the commander of heaven's army appears to Israel's commander on the "
                    "eve of the conquest.",

        "key_verse": {
            "ref": "Joshua 5:14-15",
            "text": "And he said, 'No; but I am the commander of the army of the LORD. Now I have come.' And Joshua fell on his face to the earth and worshiped and said to him, 'What does my lord say to his servant?' And the commander of the LORD's army said to Joshua, 'Take off your sandals from your feet, for the place where you are standing is holy.' And Joshua did so.",
            "translation": "ESV"
        },

        "original_terms": [
            "sar tseva YHWH (Commander of the army of YHWH -- a divine council title)",
            "milah (circumcision -- the Abrahamic covenant sign renewed)",
            "galal (to roll -- the etymology of Gilgal; rolling away reproach)",
            "cherpat mitsrayim (reproach of Egypt -- the shame removed by circumcision)",
            "pesach (Passover -- celebrated for the first time in the Promised Land)",
            "man (manna -- the wilderness provision that ceases when the land provides)",
            "qadosh (holy -- the ground made sacred by the divine presence)",
            "cherev shelufah (drawn sword -- the Commander's weapon, indicating war)"
        ],

        "ane_backdrop": "Circumcision was practiced in various ANE cultures, including Egypt "
                        "(attested in tomb reliefs from the Old Kingdom), where it was typically "
                        "a puberty or pre-marriage rite. The Israelite practice was distinctive in "
                        "two ways: it was performed on infants (the eighth day, Gen 17:12) and it "
                        "carried explicit covenant significance, marking the male body as belonging "
                        "to YHWH's covenant community. Flint knives for circumcision (5:2-3) reflect "
                        "an archaic practice preserved even after metal tools were available, "
                        "suggesting ritual conservatism. The appearance of a divine warrior with a "
                        "drawn sword has parallels in ANE throne-room scenes: the gods' champion "
                        "stands before the king with a weapon, signifying divine authorization for "
                        "warfare. In Ugaritic texts, the divine warrior goes before the human king "
                        "in battle. The 'Commander of YHWH's army' is the Israelite version of this "
                        "pattern: the heavenly general presents himself to the earthly general on "
                        "the eve of battle, signifying that the heavenly army will fight alongside "
                        "the earthly one.",

        "second_temple": [
            {
                "source": "Targum Jonathan on Joshua 5:14",
                "summary": "The Targum identifies the Commander as an 'angel' (malaka) rather "
                           "than leaving the figure's identity ambiguous. Some Targum manuscripts "
                           "identify him specifically as Michael, the prince of Israel (cf. "
                           "Daniel 10:21; 12:1).",
                "relevance": "The Targumic tradition reflects Second Temple concern about the "
                             "figure's identity: is this YHWH himself, the Angel of YHWH, or "
                             "a high-ranking angel? The identification with Michael connects the "
                             "passage to the territorial-prince theology of Daniel 10."
            },
            {
                "source": "Eusebius of Caesarea, Demonstration of the Gospel V.9",
                "summary": "Eusebius identifies the Commander as the pre-incarnate Logos (Christ), "
                           "arguing that no created angel would accept worship or declare ground "
                           "holy by his presence.",
                "relevance": "The patristic Christophany reading was influential in shaping Christian "
                             "interpretation: the Commander is the second power in heaven, the visible "
                             "YHWH who appeared to the patriarchs and prophets."
            },
            {
                "source": "Origen, Homilies on Joshua VI.2",
                "summary": "Origen interprets the Commander as Jesus Christ, and sees Joshua's "
                           "encounter as a type of the Christian's encounter with Christ as the "
                           "captain of salvation (Hebrews 2:10).",
                "relevance": "Origen's typological reading connects the Commander to the 'pioneer "
                             "of salvation' language in Hebrews, reinforcing the Joshua-Jesus typology."
            },
            {
                "source": "Jubilees 49:18-23",
                "summary": "Jubilees provides detailed Passover regulations, emphasizing that the "
                           "festival must be celebrated in the correct location and at the correct "
                           "time according to the 364-day calendar.",
                "relevance": "The Gilgal Passover (Josh 5:10) fulfilled the requirement that Passover "
                             "be celebrated 'in the place YHWH chooses' -- the first Passover in the "
                             "Promised Land."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 3:5", "note": "'Take off your sandals from your feet, for the place where you are standing is holy ground' -- identical command given to Moses, now given to Joshua", "type": "ot"},
            {"ref": "Genesis 17:10-14", "note": "The Abrahamic circumcision covenant that the wilderness generation had neglected", "type": "ot"},
            {"ref": "Daniel 10:13, 21; 12:1", "note": "Michael as the 'prince' (sar) of Israel -- a divine council figure parallel to the Commander of YHWH's army", "type": "ot"},
            {"ref": "Revelation 19:11-16", "note": "Christ on the white horse with a sword, leading the armies of heaven -- the ultimate fulfillment of the Commander image", "type": "nt"},
            {"ref": "Hebrews 2:10", "note": "Jesus as the 'pioneer (archegos) of salvation' -- the NT equivalent of the sar tseva YHWH", "type": "nt"},
            {"ref": "Exodus 12:1-14", "note": "The first Passover in Egypt -- now celebrated for the first time in the Promised Land at Gilgal", "type": "ot"},
            {"ref": "Exodus 16:35", "note": "'The people of Israel ate the manna forty years... until they came to the border of the land of Canaan' -- fulfilled in Josh 5:12", "type": "ot"},
            {"ref": "Numbers 22:23, 31", "note": "The angel of YHWH with a drawn sword before Balaam -- the same divine warrior figure before the conquest", "type": "ot"},
            {"ref": "Colossians 2:11-12", "note": "Spiritual circumcision in Christ -- the Gilgal circumcision as a type of baptismal renewal", "type": "nt"}
        ],

        "divine_council_note": "Joshua 5:13-15 is one of the most important divine council texts in "
                               "the Old Testament. The 'Commander of the army of YHWH' (sar tseva "
                               "YHWH) is a throne-room title: sar means 'prince, commander, chief "
                               "officer,' and tseva YHWH is 'the host/army of YHWH' -- the heavenly "
                               "army that YHWH commands from his throne (1 Kings 22:19; Isaiah 6:1-3). "
                               "This figure stands with a drawn sword (cherev shelufah), the posture of "
                               "a warrior ready for battle. When Joshua asks 'Are you for us, or for our "
                               "adversaries?' the answer is neither: 'No (lo); but I am the commander "
                               "of the army of YHWH. Now I have come.' The Commander does not serve "
                               "Israel's agenda; Israel serves the Commander's agenda. The heavenly army "
                               "has its own purpose: the conquest is YHWH's war, not Israel's. Joshua's "
                               "response -- falling on his face and calling the figure 'my lord (adoni)' "
                               "-- and the Commander's acceptance of this prostration (without rebuke, "
                               "unlike the angel in Revelation 19:10 and 22:8-9) indicate a figure of "
                               "supreme authority. The command to remove sandals because the ground is "
                               "holy is identical to Exodus 3:5, where YHWH himself appears in the "
                               "burning bush. The identity of the Commander is debated: (1) YHWH himself "
                               "in visible form (the Angel of YHWH / visible YHWH); (2) Michael the "
                               "archangel (the sar of Israel in Daniel 10:21; 12:1); or (3) a pre-"
                               "incarnate appearance of Christ (the dominant patristic view). In the "
                               "divine council framework, the most likely identification is the second "
                               "power in heaven -- the visible YHWH who leads the heavenly army and "
                               "serves as YHWH's executive agent in the physical world.",

        "sections": [
            {
                "heading": "The Melting of the Canaanite Kings (5:1)",
                "body": "The opening verse reports the psychological impact of the Jordan miracle: "
                        "'As soon as all the kings of the Amorites who were beyond the Jordan to "
                        "the west, and all the kings of the Canaanites who were by the sea, heard "
                        "that the LORD had dried up the waters of the Jordan for the people of "
                        "Israel until they had crossed over, their hearts melted and there was no "
                        "longer any spirit in them because of the people of Israel' (5:1). The verb "
                        "masas ('melted') is the same word Rahab used (2:11) -- her private "
                        "intelligence report is now publicly confirmed. The Canaanite political and "
                        "military leadership has been psychologically defeated before a single battle "
                        "is fought. The double designation -- 'kings of the Amorites' (inland) and "
                        "'kings of the Canaanites' (coastal) -- indicates that the terror is "
                        "universal. The divine warrior's advance campaign has succeeded: his "
                        "reputation has shattered enemy morale. Some manuscripts (including LXX "
                        "traditions) read 'we had crossed' rather than 'they had crossed,' which "
                        "would place the narrator among the crossing generation -- an eyewitness "
                        "touch. This verse provides the strategic context for what follows: this "
                        "is the perfect moment to halt and perform rituals (circumcision, Passover) "
                        "because the enemy is too demoralized to attack."
            },
            {
                "heading": "Circumcision at Gilgal: Renewing the Covenant Sign (5:2-9)",
                "body": "YHWH commands Joshua to 'make flint knives and circumcise the sons of "
                        "Israel a second time' (5:2). The phrase 'a second time' (shenit) means not "
                        "that individuals are re-circumcised but that the nation collectively renews "
                        "the practice after a forty-year lapse. The use of flint (tsur) rather than "
                        "metal knives is ritually conservative -- preserving the archaic form of a "
                        "practice that predated metallurgy. The explanation follows: 'All the people "
                        "who came out of Egypt, all the men of war, had died in the wilderness' "
                        "(5:4), and 'all the people who were born on the way in the wilderness after "
                        "they had come out of Egypt had not been circumcised' (5:5). An entire "
                        "generation grew up without the Abrahamic covenant sign. The theological "
                        "implication is sobering: during the wilderness wandering, Israel was "
                        "covenantally incomplete. The forty years of judgment (Num 14:33-34) were "
                        "also forty years of suspended covenant identity. Now, at the threshold "
                        "of the Promised Land, YHWH restores the sign. The location is named "
                        "'Gibeath-haaraloth' ('Hill of Foreskins') -- a graphic, almost shocking "
                        "name that preserves the visceral reality of the event. YHWH's declaration "
                        "is transformative: 'Today I have rolled away (galoti) the reproach of "
                        "Egypt from you' (5:9). The 'reproach of Egypt' (cherpat Mitsrayim) likely "
                        "refers to the shame of the slave identity -- uncircumcised, disobedient, "
                        "unfaithful. The rolling away of reproach is a new beginning: Israel enters "
                        "the land as a renewed, covenantally marked people."
            },
            {
                "heading": "Passover and the End of Manna (5:10-12)",
                "body": "Israel celebrates the Passover at Gilgal 'on the fourteenth day of the "
                        "month in the evening, on the plains of Jericho' (5:10). This is the first "
                        "Passover in the Promised Land -- the bookend to the first Passover in Egypt "
                        "(Exod 12). In Egypt, the Passover protected Israel from the destroyer; at "
                        "Gilgal, it celebrates deliverance completed. The meal that night marks a "
                        "transition: the exodus narrative, which began with a Passover in a foreign "
                        "land, now culminates with a Passover in YHWH's land. The next day, 'the "
                        "day after the Passover' (5:11), they eat the produce of the land for the "
                        "first time -- unleavened cakes and parched grain from the stored harvest "
                        "of Canaan. 'And the manna ceased the day after they ate of the produce of "
                        "the land. And there was no longer manna for the people of Israel, but they "
                        "ate of the fruit of the land of Canaan that year' (5:12). The cessation of "
                        "manna is both practical and theological. Practically, the supernatural food "
                        "is no longer needed because the natural provision of the land has begun. "
                        "Theologically, the wilderness is over. The period of testing, wandering, "
                        "and dependence on daily miracle has ended. God's provision now comes through "
                        "the land itself -- the 'land flowing with milk and honey' that Deuteronomy "
                        "described. But this too requires faith: the land provides because YHWH "
                        "gives the rain and the harvest (Deut 11:10-15)."
            },
            {
                "heading": "The Commander of YHWH's Army: Theophany at Jericho (5:13-15)",
                "body": "The chapter climaxes with one of the most dramatic <em>theophanies</em> "
                        "(visible appearances of God to human beings) in the Old Testament \u2014 and "
                        "many Christian interpreters identify it as a <em>Christophany</em>, a pre-incarnation "
                        "appearance of Christ (the Son of God appearing in visible form before his "
                        "birth as Jesus of Nazareth). "
                        "'When Joshua was by Jericho, he lifted up his eyes and looked, "
                        "and behold, a man was standing before him with his drawn sword in his hand' "
                        "(5:13). The scene is terse and cinematic: Joshua, alone (apparently "
                        "reconnoitering), encounters a warrior with a naked blade. His question is "
                        "tactical: 'Are you for us, or for our adversaries?' (5:13). The answer "
                        "shatters the binary: 'No (lo)' -- neither. The figure does not serve "
                        "Israel's military agenda. He has his own agenda: 'I am the Commander of "
                        "the army of YHWH. Now I have come.' The title sar tseva YHWH designates "
                        "the leader of the heavenly host -- the same 'host of heaven' (tseva "
                        "hashamayim) that stands at YHWH's right and left in the divine throne room "
                        "(1 Kings 22:19). This figure leads the angelic army that fights YHWH's "
                        "cosmic wars. His arrival means the heavenly army has deployed for the "
                        "conquest. Joshua's response is immediate: he falls on his face to the "
                        "earth and 'worships' (yishtachu -- the same word used for worship of God "
                        "throughout the OT). He asks: 'What does my lord (adoni) say to his servant "
                        "(eved)?' The Commander does not rebuke the prostration (contrast Revelation "
                        "19:10, where the angel refuses worship). Instead, he issues a command: "
                        "'Take off your sandals from your feet, for the place where you are standing "
                        "is holy (qadosh)' (5:15). These are the exact words of Exodus 3:5 -- the "
                        "burning bush, where YHWH himself appeared to Moses. The ground is holy "
                        "because the divine presence makes it holy. The chapter ends abruptly after "
                        "Joshua obeys -- the narrative continues seamlessly into the Jericho "
                        "instructions in chapter 6, suggesting that the Commander's battle plan "
                        "follows directly. The conquest of Jericho is the Commander's operation. "
                        "Joshua is his field officer. The heavenly army and the earthly army will "
                        "fight together."
            }
        ]
    }
]
