"""
era_91_david_kingdom_temple.py -- David's Kingdom & Temple Plans (1 Chronicles 17-29)

The second half of 1 Chronicles centers on two interconnected themes: the
Davidic covenant (God's promise of an eternal dynasty, ch. 17) and David's
preparations for the temple (chs. 22-29). Between them stands the pivotal
chapter 21 -- David's census, where "Satan stood against Israel" -- one of
the most important divine council texts in the Old Testament. The Chronicler's
David is consumed by one desire: to build a house for God. When told he cannot
build it himself, he pours his entire kingdom's resources into preparing
materials, plans, and personnel for Solomon. David's final prayer (29:10-19)
is among the most theologically rich in the Old Testament: "Yours, O LORD,
is the greatness and the power and the glory and the victory and the majesty."
"""

CHAPTERS = [
    {
        "id": "1chr-17-20",
        "ref": "1 Chronicles 17-20",
        "chapter_num": 1,
        "title": "The Davidic Covenant and the Kingdom Secured",
        "era": "david_kingdom_temple",
        "type": "chapter",
        "themes": ["COV", "SEED", "KING", "DC"],

        "synopsis": "Chapter 17 is the theological heart of 1 Chronicles: the Davidic covenant. "
                    "David desires to build a 'house' (bayit, temple) for the Ark, but YHWH, through "
                    "Nathan the prophet, reverses the initiative: God will build David a 'house' "
                    "(bayit, dynasty). 'I will raise up your offspring after you, one of your own "
                    "sons, and I will establish his kingdom. He shall build me a house, and I will "
                    "establish his throne forever. I will be to him a father, and he shall be to me "
                    "a son' (17:11-13). The Chronicler's version of the covenant significantly omits "
                    "the warning clause found in 2 Samuel 7:14b ('When he commits iniquity, I will "
                    "discipline him') -- in Chronicles, the covenant is presented as unconditional "
                    "and permanent. David's response prayer (17:16-27) is a masterpiece of theological "
                    "humility: 'Who am I, O LORD God, and what is my house, that you have brought me "
                    "thus far?' Chapters 18-20 then narrate David's military campaigns -- the kingdom "
                    "is being secured so that Solomon can build in peace.",

        "key_verse": {
            "ref": "1 Chronicles 17:12-14",
            "text": "He shall build me a house, and I will establish his throne forever. I will be to him a father, and he shall be to me a son. I will not take my steadfast love from him, as I took it from him who was before you, but I will confirm him in my house and in my kingdom forever, and his throne shall be established forever.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "bayit (house -- the pivotal wordplay: David wants to build God a bayit (temple), but God will build David a bayit (dynasty))",
            "olam (forever/eternity -- the covenant promise: David's throne is established 'forever,' a term pointing beyond any human dynasty)",
            "chesed (steadfast love/covenant loyalty -- YHWH's unbreakable commitment to the Davidic line, even when individual kings fail)",
            "ben (son -- 'I will be to him a father, and he shall be to me a son'; the adoptive father-son relationship between YHWH and the Davidic king)"
        ],

        "ane_backdrop": "Royal grant covenants in the ancient Near East operated similarly to the "
                        "Davidic covenant: a great king bestowed an irrevocable gift (typically land "
                        "or dynasty) on a loyal servant. The Abdi-Heba grant and Neo-Assyrian royal "
                        "grants show this pattern. The YHWH-David covenant is a royal grant: God "
                        "unilaterally promises David an eternal dynasty. The father-son language "
                        "('I will be to him a father') echoes ANE adoption formulas used in royal "
                        "succession texts. In Egypt, Pharaoh was called 'son of Ra' -- the Davidic "
                        "covenant democratizes this concept but attributes sonship to YHWH, not a "
                        "nature deity.",

        "second_temple": [
            {
                "source": "4Q174 (4QFlorilegium)",
                "summary": "This Dead Sea Scroll text interprets 2 Samuel 7 (= 1 Chr 17) messianically, "
                           "identifying the 'son' as the future Branch of David who will arise in the "
                           "last days. It reads the covenant as pointing beyond Solomon to an eschatological "
                           "fulfillment.",
                "relevance": "Demonstrates that Second Temple Judaism read the Davidic covenant as a "
                             "messianic prophecy awaiting final fulfillment -- the same interpretation "
                             "the New Testament applies to Jesus."
            },
            {
                "source": "Psalms of Solomon 17:21-32",
                "summary": "A first-century BC prayer for the messianic son of David to arise and "
                           "purge Jerusalem of Gentile occupation, establishing God's kingdom forever.",
                "relevance": "Shows the living hope of the Davidic covenant in the Second Temple period: "
                             "the promise of 1 Chr 17 was not considered fulfilled by Solomon but awaited "
                             "a greater son."
            }
        ],

        "cross_refs": [
            {"ref": "2 Samuel 7:1-29", "note": "The parallel Davidic covenant account in Samuel -- Chronicles omits the discipline clause (2 Sam 7:14b)", "type": "ot"},
            {"ref": "Psalm 89:3-4, 19-37", "note": "The Davidic covenant celebrated in worship: 'I have made a covenant with my chosen one; I have sworn to David my servant'", "type": "ot"},
            {"ref": "Isaiah 9:6-7", "note": "The messianic king whose throne is established forever -- fulfillment of the 1 Chr 17 promise", "type": "ot"},
            {"ref": "Luke 1:32-33", "note": "Gabriel to Mary: 'The Lord God will give to him the throne of his father David, and he will reign over the house of Jacob forever' -- direct fulfillment of 1 Chr 17", "type": "nt"},
            {"ref": "Hebrews 1:5", "note": "'I will be to him a father, and he shall be to me a son' -- quoted as fulfilled in Jesus, the ultimate son of David", "type": "nt"},
            {"ref": "Revelation 22:16", "note": "'I, Jesus, am the root and the descendant of David' -- the Davidic dynasty reaches its eternal fulfillment", "type": "nt"}
        ],

        "divine_council_note": "The father-son language of the Davidic covenant ('I will be to him a "
                               "father, and he shall be to me a son,' 17:13) has profound divine council "
                               "implications. In the ANE, the king was considered a 'son of god' -- a member "
                               "of the divine realm, adopted into the family of the gods. Psalm 2:7 makes "
                               "this explicit: 'The LORD said to me, You are my Son; today I have begotten "
                               "you.' Psalm 82:6 reveals that the 'sons of God' (benei elyon) are divine "
                               "council members. The Davidic king is thus adopted into the divine council "
                               "as YHWH's vice-regent on earth -- the human member of the heavenly assembly "
                               "who rules on God's behalf. This is why the Davidic covenant points "
                               "ultimately to Jesus, the true Son of God who sits at the right hand of the "
                               "Father in the divine council (Psalm 110:1; Hebrews 1:3, 13).",

        "sections": [
            {
                "heading": "David's Desire and God's Reversal (1 Chr 17:1-15)",
                "body": "David is settled in his cedar palace while the Ark of God dwells 'under a tent' "
                        "(17:1). His impulse is noble: 'I dwell in a house of cedar, but the Ark of the "
                        "covenant of the LORD is under a tent' (17:1). Nathan initially approves, but YHWH "
                        "speaks to Nathan that night with a different plan. God's message begins with "
                        "a gentle rebuke: 'You shall not build me a house to dwell in' (17:4). YHWH then "
                        "recounts his own history with Israel: 'I have not lived in a house since the day "
                        "I brought up Israel to this day, but I have gone from tent to tent and from "
                        "dwelling to dwelling' (17:5). The reversal comes in 17:10: 'Moreover, I declare "
                        "to you that the LORD will build YOU a house.' David wanted to contain God in a "
                        "building; God responds by promising to establish David forever. The bayit wordplay "
                        "is the theological key: the house God builds is greater than any house David "
                        "could build."
            },
            {
                "heading": "David's Prayer: Theology as Worship (1 Chr 17:16-27)",
                "body": "David's response prayer is a model of theological humility. He sits 'before the "
                        "LORD' (17:16) -- literally before the Ark -- and speaks. 'Who am I, O LORD God, "
                        "and what is my house, that you have brought me thus far?' (17:16). David recognizes "
                        "the sheer grace of God's initiative: 'And this was a small thing in your eyes, O God. "
                        "You have also spoken of your servant's house for a great while to come' (17:17). He "
                        "grounds the promise in God's character, not his own merit: 'There is none like you, "
                        "O LORD, and there is no God besides you' (17:20). The prayer's climax declares God's "
                        "uniqueness among all beings: YHWH alone is God. The conclusion is a petition grounded "
                        "in promise: 'Now therefore, O LORD, let the word that you have spoken concerning your "
                        "servant and concerning his house be established forever, and do as you have spoken' "
                        "(17:23). David asks God to keep his own promise -- prayer as holding God to his word."
            },
            {
                "heading": "David's Wars: Securing the Kingdom for Solomon (1 Chr 18-20)",
                "body": "Chapters 18-20 survey David's military campaigns: defeating the Philistines, Moab, "
                        "Hadadezer of Zobah, and the Arameans (ch. 18); the Ammonite-Aramean war and the "
                        "siege of Rabbah (chs. 19-20); and battles against Philistine giants (20:4-8). The "
                        "Chronicler includes these campaigns for a specific reason: David is securing the "
                        "borders so that Solomon can build in peace. This is stated explicitly later: 'My "
                        "son Solomon... shall be a man of rest... for I will give peace and quiet to Israel "
                        "in his days' (22:9). The Chronicler's David is a warrior only because he must be -- "
                        "his heart is in worship, not warfare. Note what the Chronicler OMITS from this "
                        "period: the entire Bathsheba-Uriah episode (2 Sam 11-12), Amnon's rape of Tamar "
                        "(2 Sam 13), Absalom's rebellion (2 Sam 14-18), and Sheba's revolt (2 Sam 20). "
                        "These omissions are not dishonesty but theological selectivity: the Chronicler is "
                        "writing temple history, and David's personal sins do not serve that narrative."
            }
        ]
    },

    {
        "id": "1chr-21-22",
        "ref": "1 Chronicles 21-22",
        "chapter_num": 2,
        "title": "Satan, the Census, and the Temple Site: The Divine Council at Work",
        "era": "david_kingdom_temple",
        "type": "chapter",
        "themes": ["DC", "HOLY", "BLOOD", "PRIEST"],

        "synopsis": "1 Chronicles 21 is one of the most theologically rich chapters in the entire "
                    "Old Testament for understanding the divine council. 'Then Satan stood against "
                    "Israel and incited David to number Israel' (21:1). The parallel in 2 Samuel 24:1 "
                    "reads: 'The anger of the LORD was kindled against Israel, and he incited David.' "
                    "The same event is attributed to YHWH (in Samuel) and to Satan (in Chronicles). "
                    "This is not a contradiction but complementary perspectives on the same divine "
                    "council action: YHWH decrees the testing/judgment, and the adversary (ha-satan) "
                    "executes it -- precisely the pattern of Job 1-2. The census brings plague: YHWH "
                    "sends a destroying angel (mal'ak mashchit, 21:15) who stands 'between earth and "
                    "heaven, with a drawn sword in his hand stretched out over Jerusalem.' David sees "
                    "the angel and intercedes. YHWH commands David to build an altar on the threshing "
                    "floor of Ornan the Jebusite -- which becomes the site of Solomon's temple "
                    "(22:1: 'Here shall be the house of the LORD God'). The catastrophe of the "
                    "census becomes the foundation of the temple. Chapter 22 then records David's "
                    "preparations: massive quantities of gold, silver, bronze, iron, timber, and "
                    "stone, along with his charge to Solomon to build.",

        "key_verse": {
            "ref": "1 Chronicles 21:1",
            "text": "Then Satan stood against Israel and incited David to number Israel.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "satan (adversary/accuser -- in 1 Chr 21:1 without the definite article; a divine council member who functions as prosecutor/tester)",
            "vayyamod (and he stood -- the posture of a council member presenting himself before the throne, cf. Job 1:6 where the satan 'stood among' the sons of God)",
            "vayyaset (and he incited/moved -- the same verb used for YHWH in 2 Sam 24:1; the council's decree is attributed to both the sovereign and the agent)",
            "mal'ak mashchit (destroying angel -- the angelic executor of divine judgment, standing between heaven and earth with drawn sword)",
            "goren (threshing floor -- the location of the temple; threshing floors in the ANE were sacred spaces of divine-human encounter, cf. Ruth 3, Hosea 9:1)"
        ],

        "ane_backdrop": "The concept of a divine adversary within the heavenly court has parallels "
                        "in Mesopotamian literature. The Mesopotamian god Nergal functioned as a deity "
                        "of death and plague, dispatched from the assembly of the gods to bring "
                        "destruction. The destroying angel of 1 Chronicles 21 -- standing between "
                        "heaven and earth with a drawn sword, visible to David but commissioned by "
                        "YHWH -- operates as a divine council agent executing a council decree. The "
                        "threshing floor as a sacred site is well attested in the ANE: threshing floors "
                        "were often on elevated ground (for wind), associated with theophany, and "
                        "used as gathering places for legal and religious functions. The Ugaritic texts "
                        "describe El's council meeting on a mountain -- the same theological geography "
                        "as David's altar on the threshing floor that becomes the Temple Mount.",

        "second_temple": [
            {
                "source": "Jubilees 48:2-3",
                "summary": "Jubilees identifies the figure who opposed Moses in Egypt as 'Mastema' "
                           "(the 'hatred one'), a satan-like figure who operates within divine "
                           "permission to test and accuse.",
                "relevance": "The Mastema tradition in Jubilees represents the same theological "
                             "development as 1 Chronicles 21: attributing adversarial actions to a "
                             "specific divine council figure rather than directly to YHWH."
            },
            {
                "source": "Zechariah 3:1-2",
                "summary": "In Zechariah's vision, 'the satan' (ha-satan, with the article) stands "
                           "to accuse Joshua the high priest. 'The LORD rebuke you, O Satan!'",
                "relevance": "The closest canonical parallel to 1 Chr 21:1 -- the satan functioning "
                             "as a divine council accuser, operating in YHWH's presence and subject "
                             "to YHWH's authority."
            }
        ],

        "cross_refs": [
            {"ref": "2 Samuel 24:1-25", "note": "The parallel account: 'the anger of the LORD...he incited David' -- where Chronicles says 'Satan stood against Israel and incited David'", "type": "ot"},
            {"ref": "Job 1:6-12", "note": "The satan presents himself among the sons of God (divine council) and receives YHWH's permission to test Job -- the same council dynamic as 1 Chr 21", "type": "ot"},
            {"ref": "Zechariah 3:1-2", "note": "Ha-satan accusing Joshua the high priest -- the accuser role in the divine council", "type": "ot"},
            {"ref": "2 Chronicles 3:1", "note": "Solomon builds the temple 'on Mount Moriah... on the threshing floor of Ornan' -- connecting 1 Chr 21 to the temple", "type": "ot"},
            {"ref": "Genesis 22:2", "note": "Abraham was told to go to 'the land of Moriah' to offer Isaac -- the same mountain where David sees the angel and Solomon builds the temple", "type": "ot"},
            {"ref": "Revelation 12:10", "note": "Satan as 'the accuser of our brothers' -- the NT culmination of the adversary figure introduced in 1 Chr 21:1", "type": "nt"}
        ],

        "divine_council_note": "1 Chronicles 21 is a PRIMARY divine council text. The apparent contradiction "
                               "with 2 Samuel 24 is actually a revelation of how the council operates: YHWH's "
                               "sovereign decree (2 Sam 24:1: 'he incited David') is executed through a council "
                               "agent (1 Chr 21:1: 'Satan stood against Israel and incited David'). This is "
                               "precisely the pattern of Job 1-2: YHWH does not directly afflict Job but "
                               "permits the satan to do so within defined limits. The 'standing' (vayyamod) "
                               "of Satan is the posture of a council member presenting himself before the throne "
                               "(cf. Job 1:6, 2:1; 1 Kings 22:21 where a spirit 'came forward and stood before "
                               "the LORD'). The destroying angel (mal'ak mashchit, 21:15-16) is another council "
                               "agent -- this time a visible, sword-wielding being who stands 'between earth and "
                               "heaven,' occupying the liminal space between the divine and human realms. David "
                               "and the elders of Israel 'fell on their faces' before this being (21:16), the "
                               "appropriate response to encountering a member of the heavenly assembly. YHWH's "
                               "command to the angel -- 'It is enough; now stay your hand' (21:15) -- demonstrates "
                               "that council agents operate under YHWH's sovereign direction. The entire episode "
                               "reveals the layered agency of the divine council: YHWH decrees, the adversary "
                               "incites, the destroying angel executes, and the human king responds. Multiple "
                               "agents, one sovereign will.",

        "sections": [
            {
                "heading": "Satan Incites the Census (1 Chr 21:1-6)",
                "body": "The chapter opens with the most theologically loaded sentence in Chronicles: 'Then "
                        "Satan (satan) stood against Israel and incited David to number Israel' (21:1). In "
                        "the parallel text (2 Sam 24:1), 'the anger of the LORD was kindled against Israel, "
                        "and he incited David.' The Chronicler, writing later, makes explicit what was implicit: "
                        "YHWH's incitement operates through an intermediary -- the adversary. The absence of "
                        "the definite article (ha-) before satan in Hebrew has been debated: some read it as "
                        "a proper name ('Satan'), others as a title ('an adversary'). In either case, this is "
                        "a divine council member fulfilling the adversarial/accusing role seen in Job and "
                        "Zechariah. Joab objects to the census: 'Why should my lord require this? Why should "
                        "it be a cause of guilt for Israel?' (21:3). The census is wrong because it represents "
                        "reliance on human military strength rather than trust in YHWH (cf. Deut 17:16-17 -- "
                        "the king must not multiply his forces). David overrides Joab's objection. Note that "
                        "Joab omits Levi and Benjamin from the count (21:6) -- Levi because they are sacred "
                        "to God, Benjamin perhaps because the tabernacle at Gibeon was in Benjaminite territory."
            },
            {
                "heading": "The Destroying Angel Over Jerusalem (1 Chr 21:7-17)",
                "body": "The census displeases God, and David is offered three punishments through Gad the "
                        "seer: three years of famine, three months of enemy devastation, or three days of "
                        "plague with 'the angel of the LORD destroying throughout all the territory of Israel' "
                        "(21:12). David chooses the plague: 'Let me fall into the hand of the LORD, for his "
                        "mercy is very great, but do not let me fall into the hand of man' (21:13). The "
                        "theology is remarkable: David would rather face God's direct judgment than human "
                        "cruelty, because God is merciful even in wrath. Seventy thousand fall to the plague. "
                        "Then the climactic vision: 'David lifted his eyes and saw the angel of the LORD "
                        "standing between earth and heaven, and in his hand a drawn sword stretched out over "
                        "Jerusalem' (21:16). This is a divine council agent made visible -- a warrior-being "
                        "occupying the threshold between realms. David and the elders, 'clothed in sackcloth, "
                        "fell upon their faces' (21:16). David's intercession -- 'Was it not I who gave the "
                        "command to number the people? It is I who have sinned... but these sheep, what have "
                        "they done?' (21:17) -- is a model of substitutionary intercession."
            },
            {
                "heading": "The Threshing Floor of Ornan: Catastrophe Becomes Sacred Site (1 Chr 21:18-22:1)",
                "body": "The angel of the LORD commands Gad to tell David to build an altar on the threshing "
                        "floor of Ornan (Araunah in 2 Samuel) the Jebusite. David goes to Ornan, who 'turned "
                        "and saw the angel, and his four sons who were with him hid themselves' (21:20). David "
                        "insists on paying full price: 'I will not take for the LORD what is yours, nor offer "
                        "burnt offerings that cost me nothing' (21:24). He pays 600 shekels of gold. David "
                        "builds the altar, offers burnt offerings and peace offerings, 'and he called upon "
                        "the LORD, and the LORD answered him with fire from heaven upon the altar of burnt "
                        "offering' (21:26). Fire from heaven is the divine seal of approval (cf. Lev 9:24, "
                        "1 Kings 18:38). The angel sheathes his sword. Then comes the Chronicler's pivotal "
                        "declaration: 'Then David said, Here shall be the house of the LORD God and here the "
                        "altar of burnt offering for Israel' (22:1). The place of judgment becomes the place "
                        "of worship. The destroying angel's sword is stayed where the temple will rise. This "
                        "is the Chronicler's theology in a single verse: mercy triumphs over judgment, and "
                        "God's dwelling place is established precisely where his wrath was turned aside."
            },
            {
                "heading": "David Prepares for the Temple (1 Chr 22:2-19)",
                "body": "David cannot build the temple -- 'You have shed much blood and have waged great wars. "
                        "You shall not build a house to my name, because you have shed so much blood before me "
                        "on the earth' (22:8). But he can prepare. The list of materials is staggering: 100,000 "
                        "talents of gold, 1,000,000 talents of silver, 'bronze and iron beyond weighing,' and "
                        "timber and stone in abundance (22:14). Whether these numbers are literal or typological "
                        "(representing royal hyperbole common in ANE building inscriptions), the theological "
                        "point is clear: David gives everything he has for the temple. His charge to Solomon "
                        "contains the Chronicler's core theology: 'Now, my son, the LORD be with you, so that "
                        "you may succeed in building the house of the LORD your God, as he has spoken concerning "
                        "you. Only, may the LORD grant you discretion and understanding' (22:11-12). The charge "
                        "to 'be strong and courageous' (22:13) echoes YHWH's words to Joshua (Josh 1:6-9) -- "
                        "Solomon's temple building is portrayed as a new conquest."
            }
        ]
    },

    {
        "id": "1chr-23-29",
        "ref": "1 Chronicles 23-29",
        "chapter_num": 3,
        "title": "Temple Personnel and David's Final Acts: The Blueprint from Heaven",
        "era": "david_kingdom_temple",
        "type": "chapter",
        "themes": ["PRIEST", "HOLY", "SPIRIT", "DC", "KING"],

        "synopsis": "The closing section of 1 Chronicles (chs. 23-29) is almost entirely the "
                    "Chronicler's unique material -- it has no parallel in Samuel-Kings. David "
                    "organizes the entire temple personnel system: 24 divisions of Levites "
                    "(ch. 23), 24 courses of priests (ch. 24), temple musicians organized into "
                    "24 rotating groups under Asaph, Jeduthun, and Heman (ch. 25), gatekeepers "
                    "and treasurers (ch. 26), and military and civil administrators (ch. 27). "
                    "Chapter 28 reveals that David received the temple plan 'by the Spirit' -- "
                    "literally from the divine council chamber. Chapter 29 records the people's "
                    "generous contributions and David's final prayer, one of the most magnificent "
                    "in all of Scripture. The book ends with Solomon's anointing and David's death: "
                    "'Then David slept with his fathers and was buried in the city of David' "
                    "(29:28). The Chronicler's David dies as he lived -- not as a warrior or "
                    "politician, but as a worshipper who spent his last years preparing for the "
                    "house of God.",

        "key_verse": {
            "ref": "1 Chronicles 29:11",
            "text": "Yours, O LORD, is the greatness and the power and the glory and the victory and the majesty, for all that is in the heavens and in the earth is yours. Yours is the kingdom, O LORD, and you are exalted as head above all.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tavnit (pattern/plan -- the architectural blueprint David received 'by the Spirit' (28:12); the same word used for the tabernacle pattern shown to Moses on Sinai (Exod 25:9))",
            "ruach (spirit -- the Spirit who gave David the temple plan; the divine source of the architectural design)",
            "naba (to prophesy -- the musicians 'prophesied' with lyres, harps, and cymbals (25:1); worship as prophetic activity)",
            "nedavah (freewill offering -- the voluntary generosity of the people for the temple; worship expressed through giving)",
            "kisse (throne -- YHWH's throne (29:23: 'Solomon sat on the throne of the LORD'); the earthly throne mirrors the heavenly council throne)"
        ],

        "ane_backdrop": "ANE temple-building inscriptions consistently describe the god providing "
                        "the plan for his own temple. The Gudea Cylinders (Sumerian, ~2100 BC) "
                        "describe how the god Ningirsu showed King Gudea the temple blueprint in a "
                        "dream, including precise measurements. The Egyptian temple at Edfu records "
                        "that its plan 'fell from heaven.' The Chronicler's account of David receiving "
                        "the temple plan 'by the Spirit' (28:12) follows this ANE convention: the "
                        "true architect of YHWH's temple is YHWH himself. The human king merely "
                        "receives and transmits the heavenly design. The 24 priestly courses that "
                        "David establishes (ch. 24) are attested in later sources: the Qumran scrolls "
                        "reference the 24 courses, and Josephus confirms they were still operating in "
                        "the first century AD (Antiquities 7.365-366).",

        "second_temple": [
            {
                "source": "Hebrews 8:5",
                "summary": "The author of Hebrews cites the principle that Moses was shown a 'pattern' "
                           "(typos) for the tabernacle, and that the earthly sanctuary is a 'copy and "
                           "shadow of the heavenly things.'",
                "relevance": "The same heavenly-blueprint theology applies to David's temple plan: the "
                             "tavnit received 'by the Spirit' (1 Chr 28:12) is a pattern of the heavenly "
                             "reality -- the divine council's throne room."
            },
            {
                "source": "11QTemple (Temple Scroll)",
                "summary": "The longest Dead Sea Scroll describes an ideal temple with detailed "
                           "architectural specifications, presented as divine revelation to Moses.",
                "relevance": "Demonstrates that the Second Temple community continued the tradition of "
                             "divinely revealed temple plans, extending the 1 Chronicles 28 paradigm."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 25:9, 40", "note": "Moses shown the tavnit (pattern) for the tabernacle on Sinai -- the same concept applied to David's temple plan (1 Chr 28:12, 19)", "type": "ot"},
            {"ref": "1 Kings 2:10-12", "note": "The parallel account of David's death in Kings -- brief compared to the Chronicler's extended farewell in chs. 28-29", "type": "ot"},
            {"ref": "Revelation 4:1-11", "note": "The heavenly throne room with worship surrounding the throne -- the heavenly reality of which David's temple was the earthly copy", "type": "nt"},
            {"ref": "Matthew 6:13b", "note": "'For yours is the kingdom and the power and the glory forever' -- a doxology echoing David's prayer in 1 Chr 29:11 (this doxology appears in later manuscripts of Matthew)", "type": "nt"},
            {"ref": "Hebrews 8:1-5", "note": "Christ ministers in the 'true tent' in heaven -- the heavenly temple of which Solomon's was the shadow, built on David's divinely received plan", "type": "nt"},
            {"ref": "Ephesians 2:19-22", "note": "The church as God's temple 'built on the foundation of the apostles and prophets, Christ Jesus himself being the cornerstone' -- the ultimate temple David's preparations pointed toward", "type": "nt"}
        ],

        "divine_council_note": "1 Chronicles 28:12 states that David gave Solomon 'the plan of all that "
                               "he had in mind by the Spirit (baruach)' -- the temple blueprint came from "
                               "the divine council through the Spirit of God. The term tavnit (pattern/model) "
                               "is the same word used in Exodus 25:9 for the tabernacle pattern shown to "
                               "Moses on Sinai. In both cases, the earthly sanctuary is modeled on a heavenly "
                               "reality: YHWH's throne room where the divine council assembles. The temple's "
                               "architecture reflects the council chamber: the Holy of Holies with its "
                               "cherubim (28:18) mirrors the heavenly throne flanked by seraphim/cherubim "
                               "(Isa 6, Ezek 1, Rev 4). The 24 divisions of priests and singers echo the "
                               "heavenly worship host that perpetually surrounds YHWH's throne. David's final "
                               "prayer acknowledges that all authority and power belong to YHWH (29:11-12), "
                               "and Solomon 'sat on the throne of the LORD as king' (29:23) -- the earthly "
                               "throne explicitly identified as an extension of YHWH's heavenly throne. The "
                               "Davidic king rules as YHWH's regent in the council's terrestrial jurisdiction.",

        "sections": [
            {
                "heading": "Levitical Divisions: The Standing Army of Worship (1 Chr 23-24)",
                "body": "David organizes the 38,000 Levites (age 30+) into functional divisions: 24,000 "
                        "oversee temple work, 6,000 are officers and judges, 4,000 are gatekeepers, and "
                        "4,000 are musicians (23:3-5). The 24 priestly courses (ch. 24) are determined by "
                        "lot -- Eleazar's line receives 16 courses and Ithamar's line 8, reflecting their "
                        "relative size. The first course falls to Jehoiarib (24:7 -- significant because "
                        "the Maccabees later claimed descent from Jehoiarib). The eighth course falls to "
                        "Abijah (24:10) -- Luke 1:5 identifies Zechariah, the father of John the Baptist, "
                        "as belonging to this division. These organizational details, tedious to modern "
                        "readers, establish that temple worship is not haphazard but divinely ordered. "
                        "Every priest and Levite has an assigned role, time, and responsibility. The "
                        "post-exilic community, inheriting this system, knows its worship stands in "
                        "continuity with David's original design."
            },
            {
                "heading": "The Musicians Who Prophesied (1 Chr 25)",
                "body": "Chapter 25 describes the temple musicians under three family heads: Asaph, "
                        "Jeduthun, and Heman. The critical theological detail is in 25:1: they were "
                        "'set apart for the service... who prophesied (naba) with lyres, with harps, "
                        "and with cymbals.' Music in worship is not entertainment -- it is PROPHECY. "
                        "Asaph prophesied 'under the direction of the king' (25:2). Jeduthun prophesied "
                        "'with the lyre in thanksgiving and praise to the LORD' (25:3). Heman was 'the "
                        "king's seer' (25:5). The 288 musicians (25:7) were organized into 24 courses "
                        "by lot, each serving in rotation. The identification of music with prophecy is "
                        "profoundly important: when the temple musicians sang, they were not performing -- "
                        "they were mediating divine communication. The Psalms are not merely human poetry "
                        "directed upward but prophetic words channeled through inspired singers. This "
                        "explains why the Psalter includes so many predictive and messianic texts."
            },
            {
                "heading": "The Temple Blueprint: From the Divine Council to David's Hands (1 Chr 28)",
                "body": "David assembles all Israel's leaders for his farewell address. He explains why he "
                        "cannot build the temple ('I am a man of war and have shed blood,' 28:3) and "
                        "declares that YHWH chose Solomon: 'He said to me, It is Solomon your son who shall "
                        "build my house and my courts, for I have chosen him to be my son, and I will be "
                        "his father' (28:6). Then comes the transfer of the plan: 'All this he made clear to "
                        "me in writing from the hand of the LORD, all the work to be done according to the "
                        "plan (tavnit)' (28:19). David gives Solomon the plans for every component: the "
                        "vestibule, inner rooms, upper rooms, treasuries, priestly chambers, the altar, the "
                        "golden cherubim (28:11-18). The plan came 'by the Spirit' (baruach, 28:12) -- this "
                        "is not David's architectural creativity but heaven's own design transmitted through "
                        "the Spirit of God. The temple is not a human building but a copy of the heavenly "
                        "reality, just as the tabernacle was 'according to the pattern shown on the mountain' "
                        "(Exod 25:40)."
            },
            {
                "heading": "David's Final Prayer and Solomon's Enthronement (1 Chr 29)",
                "body": "The people respond to David's appeal with extravagant generosity: 5,000 talents of "
                        "gold, 10,000 talents of silver, 18,000 talents of bronze, 100,000 talents of iron "
                        "(29:7). David's prayer is the theological summit of 1 Chronicles: 'Yours, O LORD, "
                        "is the greatness and the power and the glory and the victory and the majesty, for "
                        "all that is in the heavens and in the earth is yours. Yours is the kingdom, O LORD, "
                        "and you are exalted as head above all' (29:11). This is a confession of cosmic "
                        "sovereignty: YHWH rules over all -- heavens and earth, divine and human realms. "
                        "David acknowledges that even his generous giving was from God: 'For all things come "
                        "from you, and of your own have we given you... all this abundance... comes from your "
                        "hand and is all your own' (29:14, 16). Solomon is anointed: 'Solomon sat on the "
                        "throne of the LORD as king' (29:23). Note: 'the throne of the LORD' -- not merely "
                        "David's throne. The Davidic throne is YHWH's own throne, earthly extension of the "
                        "heavenly council's rule."
            }
        ]
    }
]
