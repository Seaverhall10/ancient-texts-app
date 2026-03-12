"""
era_46_ruth.py -- The Book of Ruth (Ruth 1-2)

A Moabite widow clings to her Israelite mother-in-law, gleans in the fields
of Bethlehem, and encounters a kinsman-redeemer (go'el) named Boaz. These
opening chapters are a masterpiece of hesed theology: covenant loyalty enacted
between a foreigner and the covenant people. Ruth demonstrates that YHWH's
redemptive purposes transcend ethnic boundaries -- a Moabite woman who
abandons Chemosh's jurisdiction and pledges fealty to YHWH is guided by
hidden providence to the precise field where redemption waits.
"""

CHAPTERS = [
    {
        "id": "ruth-1",
        "ref": "Ruth 1",
        "chapter_num": 1,
        "title": "Naomi's Bitter Return and Ruth's Covenant Oath",
        "era": "ruth",
        "type": "chapter",

        "synopsis": "During the period of the judges, famine drives Elimelech of Bethlehem to sojourn "
                    "in Moab with his wife Naomi and sons Mahlon and Chilion. Elimelech dies. The sons "
                    "marry Moabite women -- Orpah and Ruth -- and after ten years both sons also die, "
                    "leaving three childless widows. Naomi hears that YHWH has visited his people with "
                    "bread (lechem -- wordplay on Bethlehem, 'house of bread') and decides to return. "
                    "She urges her daughters-in-law to go back to their mothers' houses and their gods. "
                    "Orpah kisses Naomi and departs, but Ruth clings (davaq) to her -- the same verb "
                    "used for a man leaving father and mother and 'clinging' to his wife (Gen 2:24). "
                    "Ruth delivers one of the most celebrated oaths in Scripture: 'Where you go I will "
                    "go, and where you lodge I will lodge. Your people shall be my people, and your God "
                    "my God. Where you die I will die, and there will I be buried. May YHWH do so to "
                    "me and more also if anything but death parts me from you' (1:16-17). This is not "
                    "sentimental devotion but a covenant oath with a self-imprecation clause. Ruth "
                    "abandons Chemosh, the god of Moab, and binds herself to YHWH. Naomi returns to "
                    "Bethlehem at the beginning of barley harvest and declares: 'Do not call me Naomi "
                    "(Pleasant); call me Mara (Bitter), for Shaddai has dealt very bitterly with me' "
                    "(1:20). She left full and returned empty -- a theological complaint against the "
                    "Almighty that the narrative will systematically reverse.",

        "key_verse": {
            "ref": "Ruth 1:16-17",
            "text": "But Ruth said, 'Do not urge me to leave you or to return from following you. For where you go I will go, and where you lodge I will lodge. Your people shall be my people, and your God my God. Where you die I will die, and there will I be buried. May the LORD do so to me and more also if anything but death parts me from you.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "davaq (to cling/cleave -- the marriage verb of Gen 2:24, now Ruth's loyalty to Naomi)",
            "hesed (covenant loyalty/lovingkindness -- the controlling theme of the entire book)",
            "go'el (kinsman-redeemer -- introduced here, fulfilled in chapters 3-4)",
            "Mara (bitter -- Naomi's self-designation reflecting theological anguish)",
            "Shaddai (the Almighty -- the patriarchal divine name Naomi invokes in complaint)",
            "lechem (bread -- embedded in Beth-lechem, 'house of bread,' now restored after famine)",
            "shub (to return -- used twelve times in this chapter; the key verb of repentance)"
        ],

        "ane_backdrop": "Moab, east of the Dead Sea, was Israel's perennial neighbor-adversary. The "
                        "Moabites descended from Lot through incest (Gen 19:30-38), and Deuteronomy "
                        "23:3-6 prohibited Moabites from entering the assembly of YHWH 'to the tenth "
                        "generation.' The national deity Chemosh demanded loyalty from Moabites as YHWH "
                        "demanded loyalty from Israel -- the Mesha Stele (Moabite Stone, ~840 BC) shows "
                        "Moab's king describing Chemosh in terms nearly identical to how Israel described "
                        "YHWH: granting land, delivering from enemies, demanding devotion. Ruth's oath "
                        "to Naomi ('your God my God') is a deliberate defection from Chemosh's domain "
                        "to YHWH's -- a border-crossing in the divine council territorial map. Widows "
                        "without sons in the ANE were among the most vulnerable people: no male "
                        "protector, no inheritance rights, no economic security. The book's tension is "
                        "built on this social reality: three widows with no sons is a triple catastrophe "
                        "in the ancient world.",

        "second_temple": [
            {
                "source": "Targum Ruth 1:16",
                "summary": "The Targum expands Ruth's oath into an explicit conversion confession: "
                           "'Your people I desire to be joined to... the customs of your people I desire "
                           "to observe.' It transforms a relational oath into a halakhic conversion.",
                "relevance": "Shows how rabbinic Judaism read Ruth as the paradigmatic convert (ger "
                             "tsedek) -- the righteous proselyte who abandons paganism for Torah."
            },
            {
                "source": "Ruth Rabbah 2:22",
                "summary": "The midrash interprets Orpah's departure as a return to idolatry and claims "
                           "she became the ancestress of Goliath, while Ruth became the ancestress of "
                           "David -- setting up the David-Goliath conflict as a family feud.",
                "relevance": "This tradition creates a typological contrast: the Moabite woman who left "
                             "YHWH produced giants; the Moabite woman who clung to YHWH produced kings."
            },
            {
                "source": "Matthew 1:5",
                "summary": "Matthew includes Ruth in the genealogy of Jesus: 'Boaz the father of Obed "
                           "by Ruth, and Obed the father of Jesse, and Jesse the father of David.'",
                "relevance": "Ruth's inclusion in the Messianic genealogy demonstrates that God's "
                             "redemptive plan deliberately incorporates Gentile outsiders into the "
                             "covenant line -- foreshadowing the universal scope of the gospel."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 2:24", "note": "'A man shall leave his father and mother and cling (davaq) to his wife' -- Ruth 'clings' to Naomi with the same covenant verb", "type": "ot"},
            {"ref": "Deuteronomy 23:3-6", "note": "Moabites excluded from YHWH's assembly -- Ruth's story shows grace transcending this exclusion", "type": "ot"},
            {"ref": "Genesis 19:30-38", "note": "Moab's origin through Lot's incest -- Ruth reverses the shame of that origin", "type": "ot"},
            {"ref": "Judges 21:25", "note": "'Everyone did what was right in his own eyes' -- Ruth is set in this period but models covenant faithfulness", "type": "ot"},
            {"ref": "Matthew 1:5", "note": "Ruth in the genealogy of Jesus -- Moabite woman in the Messianic line", "type": "nt"},
            {"ref": "Ephesians 2:12-13", "note": "'You who once were far off have been brought near' -- Ruth as a type of Gentile inclusion", "type": "nt"},
            {"ref": "Isaiah 56:3-8", "note": "Foreigners who join themselves to YHWH will be gathered -- Ruth's story anticipates this promise", "type": "ot"}
        ],

        "divine_council_note": "Ruth's oath is a territorial defection in the divine council framework. "
                               "Under the Deuteronomy 32:8-9 allotment, Moab was governed by Chemosh, a "
                               "member of the 'elohim assigned to that nation. When Ruth declares 'your "
                               "God my God,' she is leaving Chemosh's jurisdiction and entering YHWH's. "
                               "This is not merely a personal religious preference but a cosmic border "
                               "crossing. She abandons her allotted deity and pledges fealty to the Most "
                               "High -- the God who kept Israel as his own nachalah (inheritance). That "
                               "YHWH accepts a Moabite woman into his covenant people, and not merely "
                               "accepts but places her in the Davidic-Messianic line, demonstrates that "
                               "his redemptive purposes are not confined to ethnic Israel. The divine "
                               "council allotment of nations to lesser 'elohim was never the final word: "
                               "YHWH's plan was always to reclaim all nations. Ruth is the firstfruit of "
                               "that reclamation.",

        "sections": [
            {
                "heading": "Famine, Moab, and Death (Ruth 1:1-5)",
                "body": "The opening sets the story in the period of the judges -- Israel's darkest era "
                        "of cyclical apostasy and oppression. Famine in Bethlehem ('house of bread') is "
                        "bitterly ironic: the place named for abundance has no food. Elimelech ('my God "
                        "is king') takes his family to Moab, the land of Chemosh. The names are laden "
                        "with theological significance: Mahlon ('sickness') and Chilion ('destruction') "
                        "bear names that foreshadow their fate. Both die in Moab, leaving Naomi with "
                        "two Moabite daughters-in-law and no male heir. The narrator compresses ten "
                        "years of life into five verses -- the emphasis is not on the sojourn but on "
                        "the loss. Three deaths produce three widows, and the Israelite family line of "
                        "Elimelech stands at extinction. The theological question the book will answer "
                        "is whether YHWH can bring life from this death, fullness from this emptiness."
            },
            {
                "heading": "Naomi's Urging and Ruth's Oath (Ruth 1:6-18)",
                "body": "Naomi hears that 'YHWH had visited (paqad) his people and given them bread' "
                        "(1:6). The verb paqad carries strong covenant overtones -- YHWH 'visits' his "
                        "people to intervene, whether in judgment or salvation (cf. Gen 50:24; Exod "
                        "3:16). She sets out to return, and her daughters-in-law go with her. On the "
                        "road, Naomi urges them to turn back: 'Go, return each of you to her mother's "
                        "house. May YHWH deal kindly (hesed) with you, as you have dealt with the dead "
                        "and with me' (1:8). She invokes hesed -- covenant loyalty -- and blesses them. "
                        "She argues that she has no more sons to provide husbands (invoking the levirate "
                        "custom of Deut 25:5-10), and that YHWH's hand has gone out against her. Orpah "
                        "kisses Naomi and departs -- back to her people and her gods (1:15). But Ruth "
                        "'clung' (davaq) to Naomi. Her oath (1:16-17) contains six commitments: shared "
                        "journey, shared lodging, shared people, shared God, shared death, shared burial. "
                        "The self-imprecation ('May YHWH do so to me and more also') invokes YHWH -- "
                        "not Chemosh -- as the guarantor of her oath. Ruth has crossed over. She has "
                        "chosen YHWH, chosen Israel, chosen Naomi. The narrator records: 'When Naomi "
                        "saw that she was determined to go with her, she said no more' (1:18)."
            },
            {
                "heading": "Return to Bethlehem: Empty and Bitter (Ruth 1:19-22)",
                "body": "The two women arrive in Bethlehem, and 'the whole town was stirred because of "
                        "them' (1:19). Naomi's return after a decade in Moab causes a commotion. The "
                        "women of the town ask, 'Is this Naomi?' She responds with a theological "
                        "complaint: 'Do not call me Naomi (na'omi, 'Pleasant'); call me Mara (mara, "
                        "'Bitter'), for Shaddai has dealt very bitterly with me. I went away full, and "
                        "YHWH has brought me back empty. Why call me Naomi, when YHWH has testified "
                        "against me and Shaddai has brought calamity upon me?' (1:20-21). She uses the "
                        "divine name Shaddai ('the Almighty') -- the patriarchal name associated with "
                        "promises of fruitfulness (Gen 17:1; 28:3; 35:11). The irony is sharp: the God "
                        "of fruitfulness has made her barren. She left 'full' (with husband and sons) "
                        "and returns 'empty' (reiqam). Yet standing beside her is Ruth -- whom Naomi "
                        "does not count as fullness. The narrative will demonstrate that Ruth is the "
                        "very instrument through which YHWH will fill Naomi again. The chapter closes "
                        "with a chronological note: they arrive at the beginning of barley harvest, "
                        "which is spring (March-April), the season of Passover and new beginnings."
            }
        ]
    },

    {
        "id": "ruth-2",
        "ref": "Ruth 2",
        "chapter_num": 2,
        "title": "Gleaning in the Field of Boaz -- Providence and Hesed",
        "era": "ruth",
        "type": "chapter",

        "synopsis": "Ruth goes out to glean in the fields -- the Levitical provision that allowed the "
                    "poor, widows, orphans, and foreigners to gather leftover grain behind the reapers "
                    "(Lev 19:9-10; 23:22; Deut 24:19-22). She 'happens' (miqreh) to come to the field "
                    "of Boaz, a gibbor chayil ('mighty man of valor/wealth') from the clan of Elimelech. "
                    "The narrator's use of 'happens' is deliberate irony: what looks like chance is "
                    "YHWH's hidden providence directing Ruth to the precise field where redemption waits. "
                    "Boaz notices Ruth, asks about her, and is told of her loyalty to Naomi. He speaks "
                    "over her: 'May YHWH repay you for what you have done, and a full reward be given "
                    "you by YHWH, the God of Israel, under whose wings (kenafayim) you have come to "
                    "take refuge' (2:12). The 'wings' metaphor will recur at the threshing floor (3:9), "
                    "where Ruth asks Boaz to spread his 'wing' (kanaf) over her -- the same word. Boaz "
                    "becomes the human agent of the divine refuge he invoked. He instructs Ruth to stay "
                    "in his fields, gives her food, and secretly orders his young men to pull grain from "
                    "the bundles for her. She returns to Naomi with an ephah of barley (~30 pounds). "
                    "When Naomi learns it is Boaz's field, she exclaims: 'May he be blessed by YHWH, "
                    "whose hesed has not forsaken the living or the dead!' (2:20). She reveals that Boaz "
                    "is 'one of our go'elim' -- a kinsman-redeemer who has the legal right to redeem "
                    "Elimelech's property and family line.",

        "key_verse": {
            "ref": "Ruth 2:12",
            "text": "The LORD repay you for what you have done, and a full reward be given you by the LORD, the God of Israel, under whose wings you have come to take refuge!",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "laqat (to glean -- the right of the poor to gather leftover grain; Lev 19:9-10)",
            "miqreh (chance/happening -- the narrator's ironic word for divine providence)",
            "gibbor chayil (mighty man of valor/wealth -- Boaz's social and military status)",
            "kenafayim (wings -- God's protective covering; same word as the 'corner' of a garment)",
            "go'el (kinsman-redeemer -- one who has legal right and obligation to redeem a relative)",
            "ephah (a dry measure, ~22 liters / ~30 lbs -- an extraordinary amount for one day's gleaning)",
            "na'arot (young women -- Boaz's female servants among whom Ruth should stay for safety)"
        ],

        "ane_backdrop": "Gleaning laws (Lev 19:9-10; 23:22; Deut 24:19-22) were distinctive to "
                        "Israelite social legislation. While ANE law codes (Hammurabi, Eshnunna) "
                        "addressed property rights extensively, none mandated that landowners leave "
                        "portions of the harvest for the poor. The gleaning laws institutionalized "
                        "YHWH's concern for the vulnerable: the widow, the orphan, and the ger "
                        "(resident alien/sojourner). Ruth qualifies on all counts -- she is a widow, "
                        "childless, and a foreigner. The harvest setting is significant: the barley "
                        "harvest (April-May) was the first grain harvest of the year, followed by "
                        "wheat harvest (May-June). Ruth's gleaning spans both seasons (2:23). The "
                        "amount she gathers -- an ephah -- is extraordinary, indicating either her "
                        "exceptional diligence or Boaz's deliberate generosity (likely both). An "
                        "average gleaner might gather a fraction of that amount. Boaz's provision "
                        "far exceeds the legal minimum.",

        "second_temple": [
            {
                "source": "Ruth Rabbah 5:4",
                "summary": "The midrash reads 'her chance chanced upon' (miqreh) as a theological "
                           "statement: 'Rabbi Joshua said: She found her prepared portion (matzah "
                           "mikhrah shelucha).' What appears as chance is divine orchestration.",
                "relevance": "Rabbinic tradition recognized the irony of 'chance' language in a book "
                             "saturated with YHWH's hidden providence."
            },
            {
                "source": "Targum Ruth 2:12",
                "summary": "The Targum expands Boaz's blessing to specify that Ruth will receive her "
                           "reward 'in the world to come' (alma de'atey) -- eschatologizing the promise.",
                "relevance": "Second Temple interpretation pushed the 'full reward' beyond earthly "
                             "blessing to eschatological hope -- a righteous Gentile convert receiving "
                             "eternal reward."
            }
        ],

        "cross_refs": [
            {"ref": "Leviticus 19:9-10", "note": "The gleaning law: 'You shall leave them for the poor and the sojourner' -- the legal foundation for Ruth's sustenance", "type": "ot"},
            {"ref": "Deuteronomy 24:19-22", "note": "Gleaning provisions for the widow, orphan, and sojourner -- Ruth is all three", "type": "ot"},
            {"ref": "Psalm 91:4", "note": "'He will cover you with his pinions, and under his wings (kenafayim) you will find refuge' -- the same metaphor Boaz uses for Ruth", "type": "ot"},
            {"ref": "Psalm 36:7", "note": "'The children of mankind take refuge in the shadow of your wings' -- YHWH's wings as divine protection", "type": "ot"},
            {"ref": "Proverbs 31:10", "note": "'An excellent wife (eshet chayil) who can find?' -- Ruth is called eshet chayil in 3:11, matching Boaz as gibbor chayil", "type": "ot"},
            {"ref": "Matthew 6:26", "note": "'Your heavenly Father feeds them' -- the same providential care Boaz extends to Ruth as YHWH's agent", "type": "nt"}
        ],

        "divine_council_note": "The 'wings' (kenafayim) under which Ruth has taken refuge (2:12) are "
                               "the wings of YHWH himself -- the same wings described in the Psalms as "
                               "the divine covering that protects those who trust in him (Ps 36:7; 57:1; "
                               "91:4). In the divine council imagery, YHWH's throne is associated with "
                               "winged cherubim (Exod 25:20; 1 Kgs 8:6-7), and his 'wings' represent "
                               "both sovereign power and protective care. That a Moabite woman -- from a "
                               "nation under Chemosh's jurisdiction -- has come to shelter under YHWH's "
                               "wings is a divine council transfer of allegiance. YHWH has accepted her "
                               "defection from Chemosh's domain. The providence that guides Ruth to Boaz's "
                               "field is YHWH operating behind the scenes without dramatic theophany or "
                               "prophetic oracle. The book of Ruth is unique in its depiction of divine "
                               "action through ordinary providence: no miracles, no angels, no audible "
                               "voice -- only the quiet sovereignty that arranges 'chance' encounters in "
                               "barley fields.",

        "sections": [
            {
                "heading": "Ruth Goes to Glean (Ruth 2:1-3)",
                "body": "The narrator introduces Boaz before Ruth encounters him: 'Now Naomi had a "
                        "relative of her husband's, a worthy man (gibbor chayil) of the clan of "
                        "Elimelech, whose name was Boaz' (2:1). The designation gibbor chayil can "
                        "mean 'mighty warrior,' 'man of wealth,' or 'man of standing' -- Boaz is all "
                        "three. His name may derive from bo'az, 'in him is strength.' Ruth takes the "
                        "initiative: 'Let me go to the field and glean among the ears of grain after "
                        "him in whose sight I shall find favor (chen)' (2:2). The word chen ('grace, "
                        "favor') will become a thematic keyword (2:2, 10, 13). Ruth goes out and "
                        "'happened to come to the part of the field belonging to Boaz' (2:3). The "
                        "Hebrew is emphatic: vayyiqer miqreha -- 'her chance chanced upon' -- a "
                        "deliberately awkward construction that signals the narrator's awareness that "
                        "this is not chance at all. The reader is meant to see YHWH's hand in what "
                        "appears random. Providence wears the mask of coincidence."
            },
            {
                "heading": "Boaz Notices Ruth (Ruth 2:4-13)",
                "body": "Boaz arrives from Bethlehem and greets his reapers: 'YHWH be with you!' They "
                        "answer: 'YHWH bless you!' (2:4). This exchange reveals Boaz's character and "
                        "the spiritual health of his household -- YHWH's name is on their lips as a "
                        "natural greeting, not a formula. Boaz notices Ruth and asks his foreman: "
                        "'Whose young woman is this?' (2:5). The foreman identifies her as 'the Moabite "
                        "young woman who came back with Naomi from the country of Moab' (2:6) and "
                        "reports her request to glean and her extraordinary diligence: 'She has been on "
                        "her feet from early morning until now, except for a short rest' (2:7). Boaz "
                        "addresses Ruth directly with remarkable generosity: 'Do not go to glean in "
                        "another field... keep close to my young women' (2:8). He has commanded his "
                        "young men not to touch her and given her access to his water jars. Ruth falls "
                        "on her face in astonishment: 'Why have I found favor in your eyes, that you "
                        "should take notice of me, since I am a foreigner (nokriyyah)?' (2:10). The "
                        "word nokriyyah is stronger than ger (resident alien) -- it means 'foreign "
                        "woman,' one with no claim on Israelite kindness. Boaz's response reveals that "
                        "he already knows Ruth's story: 'All that you have done for your mother-in-law "
                        "since the death of your husband has been fully told to me, and how you left "
                        "your father and mother and your native land and came to a people that you did "
                        "not know before' (2:11). He then pronounces the blessing of YHWH's wings."
            },
            {
                "heading": "Boaz's Generosity and Naomi's Hope (Ruth 2:14-23)",
                "body": "At mealtime Boaz invites Ruth to eat with his workers: 'Come here and eat some "
                        "bread and dip your morsel in the wine vinegar (chomets)' (2:14). She is seated "
                        "beside the reapers -- an extraordinary social elevation for a Moabite gleaner. "
                        "He passes her roasted grain (qali), and she eats until satisfied with leftovers "
                        "remaining. When she rises to glean, Boaz secretly instructs his young men: "
                        "'Let her glean even among the sheaves, and do not reproach her. And also pull "
                        "out some from the bundles for her and leave it for her to glean' (2:15-16). "
                        "His provision far exceeds the legal requirement: the gleaning law only required "
                        "leaving the corners and dropped grain; Boaz orders deliberate waste to increase "
                        "her gathering. Ruth works until evening and beats out what she has gleaned: "
                        "'about an ephah of barley' (2:17) -- roughly 30 pounds, an astonishing amount. "
                        "She brings it to Naomi along with leftover food from lunch. When Naomi asks "
                        "where she gleaned, Ruth reveals: 'The man's name with whom I worked today is "
                        "Boaz' (2:19). Naomi's response is electrifying: 'May he be blessed by YHWH, "
                        "whose hesed has not forsaken the living or the dead!' She adds: 'The man is a "
                        "close relative of ours, one of our go'elim (kinsman-redeemers)' (2:20). The "
                        "legal mechanism for Naomi's redemption has been identified."
            }
        ]
    }
]
