"""
era_46b_kinsman.py -- The Kinsman-Redeemer (Ruth 3-4)

The climax and resolution of the Ruth narrative. At the threshing floor Ruth
asks Boaz to spread his 'wing' (kanaf) over her -- the same word he used when
praying that YHWH would shelter her under his wings (2:12). Boaz becomes the
human fulfillment of his own prayer. At the city gate he outmaneuvers the
nearer kinsman-redeemer, redeems Elimelech's land, marries Ruth, and raises
up an heir for the dead. YHWH gives Ruth conception, and she bears Obed --
grandfather of David. The go'el theology of these chapters points toward the
ultimate kinsman-redeemer: one who will take on human flesh to redeem those in
bondage, pay the price no one else would pay, and restore the inheritance that
was lost. The genealogy closing the book (Perez to David) reveals that YHWH's
messianic strategy runs through unlikely, boundary-crossing unions that no
human planner would have designed.
"""

CHAPTERS = [
    {
        "id": "ruth-3",
        "ref": "Ruth 3",
        "chapter_num": 1,
        "title": "The Threshing Floor -- Wings of Redemption",
        "era": "kinsman_redeemer",
        "type": "chapter",
        "themes": ["COV", "TYPE", "WOMEN", "SEED"],

        "synopsis": "Naomi devises a plan to secure Ruth's future. She instructs Ruth to wash, anoint "
                    "herself, and go down to the threshing floor where Boaz will be winnowing barley "
                    "that night. Ruth is to wait until Boaz has eaten and drunk and lain down, then "
                    "uncover his feet (margelot) and lie down. The scene is charged with vulnerability "
                    "and trust. Ruth obeys perfectly. At midnight Boaz awakes startled to find a woman "
                    "at his feet. 'Who are you?' he asks. Ruth answers: 'I am Ruth, your servant "
                    "(amah). Spread your wing (kanaf) over your servant, for you are a go'el' (3:9). "
                    "The word kanaf ('wing/corner of garment') echoes Boaz's own prayer in 2:12 -- that "
                    "YHWH would shelter Ruth under his wings. Now Ruth asks Boaz to be the human "
                    "fulfillment of his own prayer. To spread the kanaf was a marriage proposal and an "
                    "act of protection (cf. Ezek 16:8). Boaz is deeply moved: 'May you be blessed by "
                    "YHWH, my daughter. You have made this last kindness (hesed) greater than the first "
                    "in that you have not gone after young men, whether poor or rich' (3:10). But there "
                    "is a complication: a nearer kinsman-redeemer exists who has prior legal claim. Boaz "
                    "promises to resolve the matter at the gate. He sends Ruth home before dawn with "
                    "six measures of barley. Naomi declares: 'Wait, my daughter, until you learn how "
                    "the matter falls. For the man will not rest but will settle the matter today' (3:18).",

        "key_verse": {
            "ref": "Ruth 3:9",
            "text": "He said, 'Who are you?' And she answered, 'I am Ruth, your servant. Spread your wings over your servant, for you are a redeemer.'",
            "translation": "ESV"
        },

        "original_terms": [
            "kanaf (wing/corner of garment -- marriage covering; same word as YHWH's 'wings' in 2:12)",
            "go'el (kinsman-redeemer -- the one obligated to redeem a relative's land and line)",
            "amah (female servant/handmaid -- Ruth's self-designation; humbler than shifchah)",
            "margelot (place of the feet -- the area Ruth uncovers; debated in interpretation)",
            "goren (threshing floor -- an open-air site for separating grain from chaff)",
            "hesed (covenant loyalty -- Boaz praises Ruth's second act of hesed as greater than the first)"
        ],

        "ane_backdrop": "Threshing floors in ancient Israel were typically elevated, flat areas outside "
                        "the village where grain was tossed into the wind to separate the kernels from "
                        "the chaff. They were also places of legal and religious significance: Araunah's "
                        "threshing floor became the Temple site (2 Sam 24:18-25), and threshing floors "
                        "appear in prophetic imagery (Hos 9:1; Mic 4:12). Winnowing occurred in the "
                        "evening when the breeze was strongest. Workers often slept at the threshing "
                        "floor to guard the grain from theft. The act of 'spreading the kanaf' (corner "
                        "of the garment) over a woman was an established marriage gesture in the ANE. "
                        "Ezekiel 16:8 uses the same imagery for YHWH's covenant with Israel: 'I spread "
                        "my wing (kanaf) over you and covered your nakedness; I made my vow to you and "
                        "entered into a covenant with you.' The threshing floor scene is carefully "
                        "narrated to maintain the honor of both Ruth and Boaz: nothing improper occurs, "
                        "and Boaz's first concern is the proper legal process.",

        "second_temple": [
            {
                "source": "Ruth Rabbah 7:1",
                "summary": "The midrash praises Boaz's self-control and righteousness: though a woman "
                           "lay at his feet, he mastered his inclination and swore by YHWH to act "
                           "honorably through the legal process.",
                "relevance": "Rabbinic tradition emphasized Boaz as a model of righteous restraint -- "
                             "a man who channeled desire into proper covenantal action."
            },
            {
                "source": "Ezekiel 16:8",
                "summary": "'I spread my wing (kanaf) over you and covered your nakedness; I pledged "
                           "my oath to you and entered into a covenant with you, declares the Lord GOD, "
                           "and you became mine.'",
                "relevance": "YHWH's marriage covenant with Israel uses identical kanaf language -- "
                             "Boaz's act toward Ruth mirrors YHWH's act toward his people."
            },
            {
                "source": "Targum Ruth 3:9",
                "summary": "The Targum renders Ruth's request as: 'Let your name be called upon your "
                           "handmaid to take me as wife, because you are a redeemer.' It clarifies the "
                           "marriage proposal dimension of the kanaf request.",
                "relevance": "The Targum makes explicit what the Hebrew narrative conveys through "
                             "metaphor: the spreading of the kanaf is a marriage covenant act, "
                             "paralleling YHWH's covenant with Israel."
            }
        ],

        "cross_refs": [
            {"ref": "Ezekiel 16:8", "note": "'I spread my wing (kanaf) over you' -- YHWH's covenant marriage with Israel, same gesture Ruth requests from Boaz", "type": "ot"},
            {"ref": "Ruth 2:12", "note": "Boaz prayed YHWH would shelter Ruth under his 'wings' (kenafayim) -- now Ruth asks Boaz himself to be those wings", "type": "ot"},
            {"ref": "Deuteronomy 25:5-10", "note": "The levirate marriage law -- the legal background for the go'el obligation", "type": "ot"},
            {"ref": "Leviticus 25:23-28", "note": "The go'el institution: redeeming a relative's sold land", "type": "ot"},
            {"ref": "Galatians 4:4-5", "note": "'God sent forth his Son... to redeem those under the law' -- Christ as the ultimate go'el", "type": "nt"},
            {"ref": "Hosea 2:19-20", "note": "'I will betroth you to me forever; I will betroth you to me in righteousness and justice, in hesed and mercy' -- the divine marriage of redemption", "type": "nt"}
        ],

        "divine_council_note": "The threshing floor scene carries typological weight in the divine "
                               "council framework. Boaz as go'el is a type of YHWH's redemptive action: "
                               "just as Boaz spreads his 'wing' over a vulnerable foreign woman to bring "
                               "her into the covenant household, YHWH spreads his 'wings' over those who "
                               "defect from the jurisdiction of other 'elohim and seek refuge under his "
                               "sovereignty. The go'el institution itself reflects the divine character: "
                               "YHWH is Israel's ultimate go'el (Isa 41:14; 43:14; 44:6, 24), the kinsman "
                               "who redeems his people from bondage, restores their inheritance, and "
                               "avenges their blood. Every human go'el in Israel is a shadow of the "
                               "divine go'el. That the go'el in Ruth is acting on behalf of a Moabite "
                               "woman makes the typology even more striking: the redeemer's scope is "
                               "not limited to ethnic Israel.",

        "sections": [
            {
                "heading": "Naomi's Plan (Ruth 3:1-5)",
                "body": "Naomi takes the initiative: 'My daughter, should I not seek rest (manoach) for "
                        "you, that it may be well with you?' (3:1). The word manoach ('rest, security') "
                        "echoes 1:9, where Naomi prayed that each daughter-in-law would find 'rest in "
                        "the house of her husband.' Marriage provides manoach -- the security of "
                        "belonging to a household. Naomi identifies Boaz as the target and outlines a "
                        "specific plan: wash and anoint yourself, put on your cloak, go down to the "
                        "threshing floor, wait until he has finished eating and drinking and lies down, "
                        "then uncover his feet and lie down. 'He will tell you what to do' (3:4). The "
                        "instructions are precise and carry cultural weight: the washing and anointing "
                        "prepare Ruth as a bride (cf. Ezek 16:9-10), and the threshing floor at night "
                        "is a socially daring location. Ruth's obedience is total: 'All that you say I "
                        "will do' (3:5) -- echoing Israel's covenant response at Sinai (Exod 19:8)."
            },
            {
                "heading": "Midnight at the Threshing Floor (Ruth 3:6-13)",
                "body": "Ruth does everything Naomi instructed. Boaz eats and drinks, 'and his heart "
                        "was merry' (3:7) -- he has celebrated a good harvest. He lies down at the end "
                        "of the grain heap. Ruth comes softly, uncovers his feet (margelot), and lies "
                        "down. 'At midnight the man was startled and turned over, and behold, a woman "
                        "lay at his feet!' (3:8). The tension is exquisite. 'Who are you?' he asks. "
                        "Ruth's response is a masterful fusion of humility and boldness: 'I am Ruth, "
                        "your amah. Spread your kanaf over your amah, for you are a go'el' (3:9). She "
                        "identifies herself, places herself under his authority (amah), invokes the "
                        "marriage gesture (kanaf), and claims the legal right (go'el) -- all in one "
                        "sentence. Boaz responds with blessing and admiration: her second act of hesed "
                        "(choosing him rather than a younger man) exceeds her first (clinging to Naomi). "
                        "He affirms her character: 'All my fellow townsmen know that you are a woman of "
                        "worth (eshet chayil)' (3:11) -- the same designation as the Proverbs 31 woman. "
                        "But there is a legal complication: 'There is a redeemer (go'el) nearer than I' "
                        "(3:12). Boaz will not act outside the law. He swears by YHWH to resolve the "
                        "matter: 'If he will redeem you, good; let him do it. But if he is not willing, "
                        "as YHWH lives, I will redeem you' (3:13)."
            },
            {
                "heading": "Dawn Departure and Naomi's Confidence (Ruth 3:14-18)",
                "body": "Ruth lies at Boaz's feet until before dawn, then rises 'before one could "
                        "recognize another' (3:14). Boaz is protective of her reputation: 'Let it not "
                        "be known that the woman came to the threshing floor' (3:14). He fills her "
                        "cloak with six measures of barley -- a tangible pledge of his intent and a "
                        "provision for Naomi. Ruth returns home and reports everything. Naomi's final "
                        "word is confidence: 'Wait, my daughter, until you learn how the matter falls. "
                        "For the man will not rest but will settle the matter today' (3:18). The verb "
                        "'rest' (shaqat) echoes the 'rest' (manoach) Naomi seeks for Ruth: Boaz will "
                        "not rest until Ruth has rest. The chapter stands as a turning point: the "
                        "emptiness of chapter 1 is about to be filled, the bitterness reversed, the "
                        "dead line of Elimelech about to be resurrected through the go'el."
            }
        ]
    },

    {
        "id": "ruth-4",
        "ref": "Ruth 4",
        "chapter_num": 2,
        "title": "Gate Redemption, Marriage, and the Genealogy of David",
        "era": "kinsman_redeemer",
        "type": "chapter",
        "themes": ["SEED", "TYPE", "COV", "WOMEN", "KING"],

        "synopsis": "Boaz goes to the city gate -- the legal and judicial center of Israelite towns -- "
                    "and seats himself. When the nearer kinsman-redeemer passes by, Boaz calls him "
                    "('Turn aside, friend,' using the Hebrew peloni almoni, 'so-and-so,' deliberately "
                    "unnamed) and assembles ten elders as witnesses. Boaz presents the case: Naomi is "
                    "selling (or has sold) the parcel of land belonging to Elimelech. The nearer go'el "
                    "agrees to redeem the land -- but when Boaz adds that the redemption includes "
                    "marrying Ruth the Moabitess 'to perpetuate the name of the dead in his inheritance' "
                    "(4:5), the go'el withdraws: 'I cannot redeem it for myself, lest I impair my own "
                    "inheritance' (4:6). The marriage obligation is the cost he will not pay. He removes "
                    "his sandal and gives it to Boaz -- the legal transfer ceremony (cf. Deut 25:9-10). "
                    "Boaz declares before the elders and all the people: 'I have bought from the hand of "
                    "Naomi all that belonged to Elimelech and all that belonged to Chilion and Mahlon. "
                    "Also Ruth the Moabite, the widow of Mahlon, I have bought to be my wife, to "
                    "perpetuate the name of the dead in his inheritance' (4:9-10). The people and elders "
                    "bless the union, invoking Rachel, Leah, Perez, and Tamar -- matriarchs and a "
                    "precedent for the go'el-born child. YHWH gives Ruth conception, and she bears a "
                    "son. The women of Bethlehem declare to Naomi: 'A son has been born to Naomi!' -- "
                    "crediting the child to the woman who called herself empty. Naomi takes the child to "
                    "her bosom as nurse. They name him Obed ('servant'). The book closes with a "
                    "genealogy: Perez -- Hezron -- Ram -- Amminadab -- Nahshon -- Salmon -- Boaz -- "
                    "Obed -- Jesse -- David. Ruth the Moabitess is the great-grandmother of King David.",

        "key_verse": {
            "ref": "Ruth 4:14-15",
            "text": "Then the women said to Naomi, 'Blessed be the LORD, who has not left you this day without a redeemer, and may his name be renowned in Israel! He shall be to you a restorer of life and a nourisher of your old age, for your daughter-in-law who loves you, who is more to you than seven sons, has given birth to him.'",
            "translation": "ESV"
        },

        "original_terms": [
            "sha'ar (gate -- the legal court of the Israelite city)",
            "peloni almoni (so-and-so -- the anonymous nearer go'el, deliberately unnamed)",
            "ga'al (to redeem -- the verb form of go'el; to buy back, to act as kinsman-redeemer)",
            "na'al (sandal -- the legal instrument of transfer in the go'el ceremony)",
            "qanah (to acquire/buy -- Boaz's legal declaration of redemption)",
            "Obed (servant -- the son of Ruth and Boaz, grandfather of David)",
            "toldot (generations/genealogy -- the closing genealogy that links Ruth to David)"
        ],

        "ane_backdrop": "The city gate served as the courthouse of the Israelite town. Legal "
                        "transactions, judicial hearings, and business deals took place 'in the gate' "
                        "(cf. Gen 23:10-18, Abraham's purchase of Machpelah; Deut 21:19; 22:15). The "
                        "ten elders as witnesses parallel ANE legal practice requiring specified "
                        "witnesses for binding transactions. The sandal ceremony (4:7-8) is a variation "
                        "of the halitsah ritual of Deuteronomy 25:9-10, where the widow removes the "
                        "refusing kinsman's sandal as a mark of shame. Here the transfer is voluntary "
                        "and mutual -- the nearer go'el removes his own sandal and gives it to Boaz, "
                        "symbolizing the transfer of the right to 'walk on' (inherit) the property. "
                        "Sandal-transfer as property conveyance is attested in Nuzi texts (~1500 BC), "
                        "where land sales were symbolized by the seller lifting his foot from the "
                        "property and the buyer placing his foot on it. The Perez-Tamar reference "
                        "(4:12) is significant: Perez was born through a levirate-like arrangement "
                        "when Tamar, disguised as a prostitute, conceived by her father-in-law Judah "
                        "(Gen 38). The parallel is deliberate: irregular unions within the go'el "
                        "framework produce the messianic line.",

        "second_temple": [
            {
                "source": "Ruth Rabbah 8:1",
                "summary": "The midrash identifies the unnamed go'el as Tob (from 4:1, reading peloni "
                           "as his actual name) and interprets his refusal as cowardice: he feared the "
                           "stigma of marrying a Moabitess.",
                "relevance": "The unnamed go'el's anonymity is his legacy: he refused redemption and "
                             "was forgotten. Boaz accepted it and entered the genealogy of David."
            },
            {
                "source": "Babylonian Talmud, Bava Batra 91a",
                "summary": "The Talmud identifies Boaz with the judge Ibzan of Bethlehem (Judg 12:8-10) "
                           "and records traditions about his age and the timing of his marriage to Ruth.",
                "relevance": "The rabbinic identification of Boaz as a judge reinforces his status as "
                             "a leader in Israel -- not merely a wealthy landowner but a man of judicial "
                             "authority."
            },
            {
                "source": "Luke 3:32",
                "summary": "Luke's genealogy of Jesus traces through Boaz, Obed, Jesse, David -- "
                           "confirming the Ruth genealogy as the messianic backbone.",
                "relevance": "Both Matthew and Luke preserve the Ruth-to-David line as essential to "
                             "the Messianic pedigree."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 25:5-10", "note": "The levirate marriage law and the halitsah (sandal-removal) ceremony -- the legal framework for Ruth 4", "type": "ot"},
            {"ref": "Genesis 38:1-30", "note": "Tamar and Judah -- the Perez birth through a levirate-like arrangement, explicitly referenced in Ruth 4:12", "type": "ot"},
            {"ref": "Genesis 23:10-18", "note": "Abraham's gate-purchase of Machpelah -- the same legal setting as Boaz's redemption", "type": "ot"},
            {"ref": "Isaiah 41:14; 43:14; 44:6", "note": "YHWH as Israel's go'el (Redeemer) -- the divine kinsman who buys back his people", "type": "ot"},
            {"ref": "Matthew 1:5-6", "note": "'Boaz the father of Obed by Ruth... Jesse the father of David the king' -- the genealogy that Ruth's story enables", "type": "nt"},
            {"ref": "Revelation 5:9", "note": "'You ransomed (redeemed) people for God from every tribe and language and people and nation' -- the ultimate go'el act", "type": "nt"},
            {"ref": "1 Peter 1:18-19", "note": "'You were ransomed... with the precious blood of Christ' -- Christ as the kinsman-redeemer who pays the ultimate price", "type": "nt"}
        ],

        "divine_council_note": "The genealogy closing Ruth (4:18-22) is the theological climax of the "
                               "book. From Perez (born of Tamar's irregular union with Judah) through "
                               "Boaz (who redeems a Moabite widow) to David -- the entire line runs "
                               "through unlikely, boundary-crossing unions that no human planner would "
                               "have designed. The messianic line includes a Canaanite woman who disguised "
                               "herself as a prostitute (Tamar), a Canaanite prostitute who sheltered "
                               "spies (Rahab, per Matt 1:5), and a Moabite widow who defected from "
                               "Chemosh (Ruth). YHWH's redemptive strategy in the divine council "
                               "framework is not to maintain ethnic purity but to incorporate the nations "
                               "into his own nachalah. The go'el theology of Ruth points toward the "
                               "ultimate kinsman-redeemer: one who will take on human flesh (become "
                               "kinsman) to redeem those in bondage, pay the price no one else would "
                               "pay, and restore the inheritance that was lost. Boaz is a type of Christ "
                               "not merely in function but in willingness: he redeems when the nearer "
                               "kinsman refuses, bearing the cost others calculated as too high.",

        "sections": [
            {
                "heading": "The Gate Proceedings (Ruth 4:1-6)",
                "body": "Boaz goes up to the gate and sits down -- assuming the posture of a judge or "
                        "legal petitioner. The nearer kinsman passes by (providence again), and Boaz "
                        "calls him: 'Turn aside, peloni almoni' -- literally 'so-and-so,' a deliberately "
                        "anonymous designation. This man will refuse redemption, and his name is "
                        "consequently erased from the narrative. The irony is severe: the very act "
                        "meant to 'perpetuate the name' of the dead is refused by a man whose own name "
                        "is not perpetuated. Boaz assembles ten elders as witnesses (the minimum for a "
                        "legal quorum in later rabbinic tradition) and presents the case. He begins with "
                        "the land: 'Naomi, who has come back from the country of Moab, is selling the "
                        "parcel of land that belonged to our relative Elimelech' (4:3). The nearer go'el "
                        "agrees: 'I will redeem it' (4:4). Then Boaz introduces the complication: 'The "
                        "day you buy the field from the hand of Naomi, you also acquire Ruth the Moabite, "
                        "the widow of the dead, in order to perpetuate the name of the dead in his "
                        "inheritance' (4:5). The go'el reverses immediately: 'I cannot redeem it for "
                        "myself, lest I impair (shachat) my own inheritance' (4:6). The marriage to a "
                        "Moabitess and the obligation to produce an heir who would inherit the redeemed "
                        "land (thereby removing it from his own estate) is a cost he will not bear."
            },
            {
                "heading": "The Sandal Transfer and Boaz's Declaration (Ruth 4:7-12)",
                "body": "The narrator explains the legal custom: 'Now this was the custom in former times "
                        "in Israel concerning redeeming and exchanging: to confirm a transaction, the one "
                        "drew off his sandal and gave it to the other, and this was the manner of "
                        "attesting in Israel' (4:7). The parenthetical note suggests this custom was "
                        "already archaic by the time of writing. The nearer go'el removes his sandal "
                        "and gives it to Boaz -- the transfer of rights is complete. Boaz then makes "
                        "a formal legal declaration before the elders and all the people: 'You are "
                        "witnesses this day that I have bought from the hand of Naomi all that belonged "
                        "to Elimelech and all that belonged to Chilion and to Mahlon. Also Ruth the "
                        "Moabite, the widow of Mahlon, I have bought to be my wife, to perpetuate the "
                        "name of the dead in his inheritance, that the name of the dead may not be cut "
                        "off from among his brothers and from the gate of his native place' (4:9-10). "
                        "The elders respond with a blessing that invokes the matriarchs: 'May YHWH make "
                        "the woman who is coming into your house like Rachel and Leah, who together "
                        "built up the house of Israel' (4:11). They also invoke Perez: 'May your house "
                        "be like the house of Perez, whom Tamar bore to Judah' (4:12). The Perez "
                        "reference connects the irregular levirate union of Judah-Tamar to the "
                        "go'el union of Boaz-Ruth -- both producing the messianic line through unlikely "
                        "means."
            },
            {
                "heading": "Birth of Obed and the Davidic Genealogy (Ruth 4:13-22)",
                "body": "Boaz takes Ruth as his wife. 'And YHWH gave her conception, and she bore a son' "
                        "(4:13). The explicit statement that 'YHWH gave her conception' is theologically "
                        "deliberate: this birth is YHWH's doing, as every child in the messianic line is "
                        "ultimately YHWH's provision. The women of Bethlehem bless Naomi: 'Blessed be "
                        "YHWH, who has not left you this day without a go'el, and may his name be "
                        "renowned in Israel! He shall be to you a restorer of life (meshiv nefesh) and "
                        "a nourisher of your old age' (4:14-15). Then comes the stunning declaration: "
                        "'Your daughter-in-law who loves you, who is more to you than seven sons, has "
                        "given birth to him' (4:15). Seven sons is the idealized number of offspring "
                        "(cf. 1 Sam 2:5); Ruth surpasses even that ideal. Naomi takes the child to her "
                        "bosom, and the neighbor women name him: 'A son has been born to Naomi!' They "
                        "call him Obed ('servant/worshiper'). The genealogy closes the book: Perez "
                        "fathered Hezron, Hezron fathered Ram, Ram fathered Amminadab, Amminadab "
                        "fathered Nahshon, Nahshon fathered Salmon, Salmon fathered Boaz, Boaz fathered "
                        "Obed, Obed fathered Jesse, and Jesse fathered David (4:18-22). Ten generations "
                        "from Perez to David -- the number of completeness. The book of Ruth, set in "
                        "the dark age of the judges, ends with the name of the king. Naomi's emptiness "
                        "has been filled. The dead line of Elimelech has been resurrected. The Moabite "
                        "woman has entered the genealogy of the Messiah."
            }
        ]
    }
]
