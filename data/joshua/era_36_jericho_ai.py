"""
era_36_jericho_ai.py -- Jericho & Ai (Joshua 6-8)

The first two military engagements of the conquest reveal the theology of holy
war: Jericho falls through liturgical obedience and divine power (not siege
engineering), while Ai becomes a catastrophic lesson in covenant violation.
Achan's sin breaks the herem, and YHWH's anger falls on the entire community.
After purging the violation, Israel conquers Ai by ambush and renews the
covenant at Shechem between Ebal and Gerizim.
"""

CHAPTERS = [
    {
        "id": "josh-6",
        "ref": "Joshua 6",
        "chapter_num": 6,
        "title": "The Fall of Jericho -- Cosmic Warfare Through Liturgy",
        "era": "jericho_ai",
        "type": "chapter",

        "synopsis": "Jericho is shut up tight -- 'none went out, and none came in' (6:1). YHWH "
                    "gives Joshua the battle plan: this is not a conventional siege but a liturgical "
                    "ritual. For six days, armed men march around the city once daily, followed by "
                    "seven priests blowing seven ram's horn trumpets (shofarot), followed by the ark "
                    "of the covenant. On the seventh day, they march around seven times. At the long "
                    "blast of the trumpets, all the people shout (teru'ah -- the war cry), and the "
                    "walls collapse. The entire city is placed under herem -- 'devoted to the LORD "
                    "for destruction' (6:17). Everything that breathes is killed; only metals (gold, "
                    "silver, bronze, iron) go into YHWH's treasury. Rahab and her household are "
                    "spared because of the oath. Joshua pronounces a curse on anyone who rebuilds "
                    "Jericho: 'At the cost of his firstborn shall he lay its foundation, and at the "
                    "cost of his youngest son shall he set up its gates' (6:26) -- a curse fulfilled "
                    "in 1 Kings 16:34. The seven-day ritual with seven priests, seven trumpets, and "
                    "seven circuits saturates the narrative with the number of divine completion. "
                    "Jericho falls not by human military power but by YHWH's direct intervention "
                    "through a worship procession. The ark -- YHWH's throne -- is the true siege "
                    "weapon. The walls of the first Canaanite city fall before the presence of the "
                    "divine King.",

        "key_verse": {
            "ref": "Joshua 6:20",
            "text": "So the people shouted, and the trumpets were blown. As soon as the people heard the sound of the trumpet, the people shouted a great shout, and the wall fell down flat, so that the people went up into the city, every man straight before him, and they captured the city.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "cherem (devoted destruction -- a difficult but important concept: everything placed under cherem is totally dedicated to YHWH and cannot be taken as plunder. Persons are killed, objects are either destroyed or placed in YHWH's treasury. This is not ordinary warfare but an act of sacred judgment. The practice was not unique to Israel -- the Moabite Stone (Mesha Stele, ~840 BC) records King Mesha of Moab devoting Israelite cities to his god Chemosh using identical language. In the biblical context, herem is reserved for the specific Canaanite populations whose sin had reached a critical threshold (cf. Genesis 15:16, where God tells Abraham that 'the iniquity of the Amorites is not yet complete'). It was never intended as a permanent policy for all warfare.)",
            "shofar (ram's horn trumpet -- the instrument of divine warfare and worship; its blast announced God's presence and his intervention in battle)",
            "teru'ah (war cry/shout -- the battle cry that triggers divine intervention)",
            "aron YHWH (ark of YHWH -- the portable divine throne that leads the procession; the gold-overlaid chest containing the covenant tablets, topped by the mercy seat and two cherubim)",
            "sovev (to go around/encircle -- the ritual circling of the city)",
            "qelalah (curse -- the imprecation Joshua places on Jericho's rebuilder)",
            "sheva (seven -- the number of divine completion saturating the narrative)"
        ],

        "ane_backdrop": "Siege warfare was the primary method of conquering fortified cities in "
                        "the Late Bronze and Iron Ages. Typical siege tactics included battering "
                        "rams, siege ramps, undermining walls, and prolonged blockade. Egyptian "
                        "reliefs (Ramesses II at Dapur, ~1269 BC) and Assyrian reliefs (Sennacherib "
                        "at Lachish, ~701 BC) depict elaborate siege operations. The Jericho "
                        "narrative deliberately subverts all of this: no rams, no ramps, no "
                        "undermining. The city falls through a ritual procession. This is not "
                        "military technology but liturgical warfare. The practice of carrying divine "
                        "standards or cult objects in military processions was common in the ANE: "
                        "Egyptian armies carried images of Amun-Re before the troops, and Assyrian "
                        "armies carried the divine standards of Ashur. Israel's version places the "
                        "ark -- not an image but the throne of the imageless God -- at the center "
                        "of the formation. The herem (devoted destruction) parallels the Moabite "
                        "cherem attested in the Mesha Stele (~840 BC): King Mesha of Moab devoted "
                        "Israelite cities to his god Chemosh in identical language. The practice "
                        "was a recognized form of sacred warfare throughout the ancient Near East.",

        "second_temple": [
            {
                "source": "Hebrews 11:30",
                "summary": "'By faith the walls of Jericho fell down after they had been "
                           "encircled for seven days.'",
                "relevance": "Hebrews identifies the Jericho victory as an act of faith, not "
                             "military skill -- the same theological reading the text itself presents."
            },
            {
                "source": "Josephus, Antiquities V.1.5-6",
                "summary": "Josephus describes the fall of Jericho in detail, attributing the "
                           "wall collapse to divine intervention and comparing it to other "
                           "miraculous deliverances in Israel's history.",
                "relevance": "Josephus treats the Jericho narrative as historical fact, not "
                             "mythology, reflecting standard Second Temple interpretation."
            },
            {
                "source": "1 Maccabees 2:55",
                "summary": "Mattathias cites Joshua as an example of faithful zeal: 'Joshua, "
                           "because he fulfilled the command, became a judge in Israel.'",
                "relevance": "The Maccabean resistance movement drew on the Joshua tradition "
                             "for inspiration -- a new conquest of the Promised Land."
            },
            {
                "source": "4QJosh^a (4Q47)",
                "summary": "The Dead Sea Scrolls Joshua manuscript preserves portions of chapter "
                           "6, with minor variations from the MT.",
                "relevance": "The Qumran text confirms the stability of the Jericho narrative "
                             "in the manuscript tradition."
            }
        ],

        "cross_refs": [
            {"ref": "Leviticus 27:28-29", "note": "The cherem legislation: 'Every devoted thing is most holy to the LORD' -- the theological basis for the Jericho herem", "type": "ot"},
            {"ref": "Deuteronomy 7:1-5", "note": "The command to destroy the seven Canaanite nations and their religious infrastructure", "type": "ot"},
            {"ref": "Deuteronomy 20:16-18", "note": "'You shall save alive nothing that breathes' -- the specific herem command for Canaanite cities", "type": "ot"},
            {"ref": "1 Kings 16:34", "note": "Hiel of Bethel rebuilds Jericho at the cost of his firstborn and youngest son -- Joshua's curse fulfilled", "type": "ot"},
            {"ref": "Hebrews 11:30", "note": "By faith the walls of Jericho fell -- the NT interprets the event as faith-driven", "type": "nt"},
            {"ref": "2 Corinthians 10:4", "note": "'The weapons of our warfare are not of the flesh but have divine power to destroy strongholds' -- spiritual warfare echoing the Jericho pattern", "type": "nt"},
            {"ref": "Revelation 8:2, 6", "note": "Seven angels with seven trumpets -- the Jericho seven-trumpet motif in eschatological judgment", "type": "nt"},
            {"ref": "Psalm 47:1-5", "note": "'God has gone up with a shout (teru'ah), the LORD with the sound of a trumpet' -- YHWH as the divine warrior of the Jericho narrative", "type": "ot"}
        ],

        "divine_council_note": "The fall of Jericho is cosmic warfare conducted through liturgy. "
                               "The seven-day ritual with seven priests, seven trumpets, and seven "
                               "circuits invokes the number of divine completion -- creation was "
                               "completed in seven days, and Jericho is un-created in seven days. "
                               "The ark of the covenant -- YHWH's throne -- is the true weapon. Its "
                               "presence in the procession means YHWH himself is besieging the city. "
                               "The shofar blast connects to the theophany tradition: God descends "
                               "with a trumpet blast at Sinai (Exod 19:16, 19), and the trumpet will "
                               "sound at the final theophany (1 Thess 4:16; Rev 8-11). The teru'ah "
                               "(war cry/shout) is the battle cry of the divine warrior and his army "
                               "(Psalm 47:5; Zeph 3:17). The herem transforms the city into a sacred "
                               "offering -- everything is given to YHWH, either by destruction (living "
                               "things) or by treasury deposit (metals). In the divine council "
                               "framework, the herem targets the territory and populations under "
                               "the spiritual authority of Jericho's gods. YHWH is not merely "
                               "conquering a city; he is dismantling a spiritual jurisdiction. The "
                               "walls fall by divine power to demonstrate that no human or spiritual "
                               "fortification can withstand the approach of the divine King.",

        "sections": [
            {
                "heading": "The Divine Battle Plan (6:1-7)",
                "body": "Jericho is in lockdown: 'shut up inside and outside because of the people "
                        "of Israel. None went out, and none came in' (6:1). The city is sealed like "
                        "a tomb -- the residents have heard of the Jordan miracle and are paralyzed "
                        "with terror. YHWH's instructions to Joshua are specific and counterintuitive: "
                        "'See, I have given Jericho into your hand, with its king and mighty men of "
                        "valor' (6:2). Again the prophetic perfect: 'I have given' -- the outcome "
                        "is decided before the first circuit begins. The plan: all the fighting men "
                        "march around the city once per day for six days. Seven priests carry seven "
                        "ram's horn trumpets (shofarot yovelim) before the ark. On the seventh day, "
                        "they march around seven times, the priests blow a long blast, and the "
                        "people shout. 'The wall of the city will fall down flat (tachteyha), and "
                        "the people shall go up, everyone straight before him' (6:5). The word "
                        "tachteyha means 'underneath itself' or 'in its place' -- the wall collapses "
                        "vertically, creating a ramp of rubble that soldiers can climb straight up. "
                        "The seven-day structure mirrors the creation week: God created the world in "
                        "six days and rested on the seventh. At Jericho, God un-creates a city in "
                        "seven days -- the herem is a reversal of creation, a return to chaos for "
                        "the territory of the enemy gods. The rams' horns (yovel) connect to the "
                        "Jubilee (yovel) -- the year of release and restoration (Lev 25). Jericho's "
                        "destruction is Israel's liberation."
            },
            {
                "heading": "The Seven-Day Procession (6:8-16)",
                "body": "Joshua organizes the procession: armed men in front, then seven priests "
                        "blowing trumpets, then the ark, then the rear guard (6:8-9). The silence "
                        "is imposed: 'You shall not shout or make your voice heard, neither shall "
                        "any word go out of your mouth, until the day I tell you to shout. Then you "
                        "shall shout' (6:10). The silence for six days intensifies the drama -- an "
                        "entire nation marching in disciplined silence around a terrified city, with "
                        "only the haunting drone of seven rams' horns breaking the stillness. The "
                        "psychological impact on Jericho's defenders must have been extraordinary: "
                        "no battle cries, no siege operations, no negotiations -- just silent "
                        "marching and the sound of horns, day after day, while the golden ark of "
                        "an invisible God passes beneath the walls. The procession follows the same "
                        "pattern for six days: one circuit, return to camp. On the seventh day, they "
                        "rise 'at the dawn of day' (6:15) -- the first light of the seventh day, "
                        "the day of completion. They march around seven times. On the seventh circuit, "
                        "Joshua commands: 'Shout, for the LORD has given you the city!' (6:16). He "
                        "specifies the herem: the city and all in it are 'devoted to the LORD for "
                        "destruction' (cherem la'YHWH). Only Rahab and her household are excepted. "
                        "Only metals go to YHWH's treasury. The herem is total and non-negotiable."
            },
            {
                "heading": "The Walls Fall and the Herem Is Executed (6:17-25)",
                "body": "The trumpets blast, the people shout, and 'the wall fell down flat (tachteyha)' "
                        "(6:20). The archaeological evidence from Jericho has been hotly debated: "
                        "Kathleen Kenyon's excavations (1952-1958) found massive destruction evidence "
                        "but dated it to ~1550 BC (too early for either exodus chronology). Bryant "
                        "Wood's re-analysis (1990) of Kenyon's pottery data argued for a ~1400 BC "
                        "destruction, consistent with the early date. The debate continues, but the "
                        "text's description of walls collapsing outward and downward, creating "
                        "rubble ramps, is archaeologically distinctive. The herem is executed: "
                        "'Then they devoted all in the city to destruction (cherem), both men and "
                        "women, young and old, oxen, sheep, and donkeys, with the edge of the "
                        "sword' (6:21). The comprehensiveness is deliberate -- this is a total "
                        "offering to YHWH, not selective plunder. Gold, silver, bronze, and iron "
                        "vessels go into YHWH's treasury (6:19). Joshua sends the two spies to "
                        "retrieve Rahab and her family: 'they brought out Rahab and her father "
                        "and mother and brothers and all who belonged to her... and they set them "
                        "outside the camp of Israel' (6:23). Rahab is placed 'outside the camp' "
                        "initially -- she is a Canaanite who has not yet been formally incorporated "
                        "into Israel. But the narrative adds: 'she has lived in Israel to this day' "
                        "(6:25) -- she was absorbed into the covenant community, eventually marrying "
                        "Salmon and becoming an ancestor of David and Jesus (Matt 1:5). The city is "
                        "burned. Rahab's faith saves her; Jericho's resistance destroys it."
            },
            {
                "heading": "Joshua's Curse on Jericho (6:26-27)",
                "body": "Joshua pronounces a solemn oath: 'Cursed before the LORD be the man who "
                        "rises up and rebuilds this city, Jericho. At the cost of his firstborn "
                        "shall he lay its foundation, and at the cost of his youngest son shall he "
                        "set up its gates' (6:26). This is not merely a military prohibition but a "
                        "sacred imprecation: the rebuilder will lose his firstborn when the foundation "
                        "is laid and his youngest when the gates are erected. The fulfillment comes "
                        "centuries later in 1 Kings 16:34: 'In his days Hiel of Bethel built Jericho. "
                        "He laid its foundation at the cost of Abiram his firstborn, and set up its "
                        "gates at the cost of his youngest son Segub, according to the word of the "
                        "LORD, which he spoke by Joshua the son of Nun.' The curse treats Jericho as "
                        "permanently devoted territory -- like the herem itself, the city belongs to "
                        "YHWH and cannot be reclaimed for human use. Rebuilding it is an act of "
                        "sacrilege that invokes covenant curses. The chapter concludes: 'So the LORD "
                        "was with Joshua, and his fame was in all the land' (6:27). YHWH's promise "
                        "of Joshua 1:5 is being fulfilled. The divine warrior fights, and his general "
                        "receives the credit -- but both the narrator and the reader know where the "
                        "power comes from."
            }
        ]
    },

    {
        "id": "josh-7",
        "ref": "Joshua 7",
        "chapter_num": 7,
        "title": "Achan's Sin -- When the Herem Is Broken",
        "era": "jericho_ai",
        "type": "chapter",

        "synopsis": "After the triumph at Jericho, disaster strikes. Achan son of Carmi, of the "
                    "tribe of Judah, has taken devoted items (cherem) from Jericho -- a cloak from "
                    "Shinar, 200 shekels of silver, and a bar of gold -- hiding them under his tent. "
                    "YHWH's anger burns against all Israel (7:1), not just Achan. When Joshua sends "
                    "3,000 men against the small city of Ai, they are routed, and 36 Israelites die. "
                    "Joshua tears his clothes, falls before the ark, and laments: 'Why did you ever "
                    "bring this people over the Jordan?' (7:7). YHWH's response is blunt: 'Israel has "
                    "sinned... they have taken some of the devoted things... they have stolen... they "
                    "have lied... they have put them among their own belongings' (7:11). Corporate "
                    "guilt contaminates the entire community. A lot-casting process narrows the guilt "
                    "from tribe (Judah) to clan (Zerahites) to household (Zabdi) to individual "
                    "(Achan). Achan confesses: 'I saw... I coveted... I took' -- the language "
                    "deliberately echoing Eve's sin in Genesis 3:6 ('saw that it was good, took, "
                    "ate'). Achan and his entire household, along with the stolen goods, are stoned "
                    "and burned in the Valley of Achor ('Valley of Trouble'). 'Then the LORD turned "
                    "from his burning anger' (7:26). The Achan episode establishes that the herem is "
                    "not optional -- breaking it brings corporate disaster.",

        "key_verse": {
            "ref": "Joshua 7:11",
            "text": "Israel has sinned; they have transgressed my covenant that I commanded them; they have taken some of the devoted things; they have stolen and lied and put them among their own belongings.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ma'al (trespass/unfaithfulness -- sacrilege against YHWH's sacred property)",
            "cherem (devoted things -- the sacred property Achan stole from YHWH)",
            "chamad (to covet/desire -- the same verb used in the tenth commandment)",
            "goral (lot -- the device used to identify the guilty party)",
            "achor (trouble -- the valley named for the 'troubling' of Israel)",
            "charon af (burning anger -- YHWH's wrath kindled by covenant violation)",
            "avar brit (to transgress the covenant -- crossing the boundary of YHWH's commands)"
        ],

        "ane_backdrop": "The concept of corporate guilt -- an entire community suffering for one "
                        "member's violation -- was fundamental to ANE treaty relationships. Hittite "
                        "suzerainty treaties specify that the vassal population collectively bears "
                        "responsibility for violations by individuals. The Esarhaddon vassal treaties "
                        "impose curses on entire populations for the disloyalty of any member. The "
                        "Moabite Stone records Mesha's dedication of entire Israelite cities to "
                        "Chemosh -- the parallel cherem practice confirms that violation of devoted "
                        "property was universally understood as sacrilege. Lot-casting for divine "
                        "determination was common throughout the ANE: Mesopotamian texts describe "
                        "the puru (lot) as a means of divine communication, and the practice is "
                        "attested in Hittite, Egyptian, and Ugaritic contexts. The lot does not "
                        "function by chance but by divine direction -- 'The lot is cast into the "
                        "lap, but its every decision is from the LORD' (Prov 16:33).",

        "second_temple": [
            {
                "source": "Jubilees 20:6-7",
                "summary": "Jubilees warns against coveting devoted things, drawing on the Achan "
                           "narrative as a cautionary example of the consequences of sacrilege.",
                "relevance": "The Jubilees tradition treats the Achan episode as paradigmatic: any "
                             "violation of sacred property triggers corporate consequences."
            },
            {
                "source": "4 Maccabees 2:19-20",
                "summary": "The author cites Achan's desire as an example of the passions "
                           "overwhelming reason, arguing that Torah-disciplined reason can "
                           "overcome such temptations.",
                "relevance": "The Hellenistic Jewish reading reframes Achan's sin in philosophical "
                             "terms -- the failure of rational self-control before desire."
            },
            {
                "source": "Mishnah Sanhedrin 6:2",
                "summary": "The Mishnah discusses the stoning procedure referenced in the Achan "
                           "narrative, establishing it as the paradigmatic case for community execution.",
                "relevance": "Rabbinic law treated the Achan episode as a foundational case in "
                             "criminal jurisprudence -- the model for how a community deals with "
                             "a member who endangers the whole."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 3:6", "note": "'The woman saw that the tree was good... she took... she ate' -- Achan's 'I saw, I coveted, I took' mirrors Eve's sin pattern", "type": "ot"},
            {"ref": "Deuteronomy 7:25-26", "note": "'You shall not covet the silver or the gold that is on them or take it for yourselves' -- the exact prohibition Achan violates", "type": "ot"},
            {"ref": "Acts 5:1-11", "note": "Ananias and Sapphira withhold from the community and die -- the Achan pattern in the New Testament church", "type": "nt"},
            {"ref": "1 Corinthians 5:6", "note": "'A little leaven leavens the whole lump' -- the corporate guilt principle of Joshua 7 applied to church discipline", "type": "nt"},
            {"ref": "1 Chronicles 2:7", "note": "Achan called 'Achar, the troubler of Israel, who broke faith in the matter of the devoted thing'", "type": "ot"},
            {"ref": "Hosea 2:15", "note": "'The Valley of Achor shall become a door of hope' -- the curse site becomes a redemption site in prophetic vision", "type": "ot"},
            {"ref": "Proverbs 16:33", "note": "'The lot is cast into the lap, but its every decision is from the LORD' -- the theology behind the lot-casting in Josh 7", "type": "ot"}
        ],

        "divine_council_note": "Achan's sin is a cosmic violation, not merely a legal infraction. "
                               "The cherem transforms conquered property into YHWH's sacred treasury. "
                               "Taking from the cherem is theft from God himself -- a breach of the "
                               "boundary between the human and divine realms. In the divine council "
                               "framework, the herem is the mechanism by which YHWH reclaims territory "
                               "from the spiritual powers that held it. The devoted property belongs "
                               "to the divine realm; removing it from that realm and bringing it into "
                               "the human realm (under Achan's tent) is an act of cosmic trespass "
                               "comparable to the Watchers crossing the boundary between heaven and "
                               "earth in Genesis 6:1-4. The corporate consequences -- all Israel suffers "
                               "for one man's violation -- reflect the corporate nature of the covenant: "
                               "Israel is YHWH's vassal nation, collectively bound by the treaty terms. "
                               "When one member violates the treaty, the suzerain's anger falls on the "
                               "whole vassal state. The lot-casting process is a divine council judicial "
                               "procedure: YHWH himself directs the lots to identify the guilty party, "
                               "functioning as the cosmic judge who sees what is hidden.",

        "sections": [
            {
                "heading": "The Trespass and the Defeat at Ai (7:1-5)",
                "body": "The chapter opens with a devastating summary: 'But the people of Israel "
                        "broke faith (ma'al) in regard to the devoted things (cherem)' (7:1). The "
                        "verb ma'al means 'to act treacherously, to commit sacrilege' -- it "
                        "specifically denotes violation of sacred trust. The narrator names the "
                        "guilty party immediately (Achan son of Carmi, son of Zabdi, son of Zerah, "
                        "of the tribe of Judah), but the text says 'the people of Israel' committed "
                        "the trespass and 'the anger of YHWH burned against the people of Israel.' "
                        "Corporate identity precedes individual guilt. Joshua, unaware of the violation, "
                        "sends men to reconnoiter Ai ('the ruin'), a small city near Bethel. The spies "
                        "report confidently: 'Do not have all the people go up, but let about two or "
                        "three thousand men go up... for they are few' (7:3). The overconfidence after "
                        "Jericho is palpable -- and fatal. 'About 3,000 men' go up, and 'the men of "
                        "Ai struck down about 36 men of them and chased them before the gate as far "
                        "as Shebarim' (7:5). The reversal is total: Israel, who was just told that "
                        "no one could stand before them (1:5), is now fleeing before a minor city. "
                        "'The hearts of the people melted (yimmasu) and became as water' (7:5) -- "
                        "the same verb (masas) used for the Canaanites' melting hearts in 2:11 and "
                        "5:1. The condition has reversed: now it is Israel's heart that melts."
            },
            {
                "heading": "Joshua's Lament and YHWH's Diagnosis (7:6-15)",
                "body": "Joshua tears his clothes, falls before the ark, and throws dust on his "
                        "head -- traditional mourning gestures. His lament echoes the wilderness "
                        "generation's complaint: 'Alas, O Lord GOD, why have you brought this "
                        "people over the Jordan at all, to give us into the hands of the Amorites, "
                        "to destroy us? Would that we had been content to dwell beyond the Jordan!' "
                        "(7:7). This is dangerously close to the murmuring of Numbers 14:2-3. YHWH's "
                        "response is abrupt: 'Get up! Why have you fallen on your face?' (7:10). The "
                        "rebuke is sharp -- this is not a time for mourning but for action. YHWH "
                        "diagnoses the problem with surgical precision: 'Israel has sinned; they have "
                        "transgressed my covenant (avru et briti) that I commanded them; they have "
                        "taken some of the devoted things; they have stolen and lied and put them "
                        "among their own belongings' (7:11). Five verbs of violation: sinned, "
                        "transgressed, taken, stolen, lied. The consequence: 'I will be with you no "
                        "more, unless you destroy the devoted things from among you' (7:12). The "
                        "most terrifying possible statement: YHWH's presence -- the very thing that "
                        "makes Israel invincible -- is withdrawn. Without God's presence, Israel is "
                        "just another small tribal group. YHWH commands a sanctification process "
                        "and a lot-casting procedure for the next day: tribe by tribe, clan by clan, "
                        "household by household, man by man, until the guilty party is identified."
            },
            {
                "heading": "The Lot Falls on Achan (7:16-21)",
                "body": "The lot-casting unfolds with agonizing precision. 'Judah was taken' (7:16) -- "
                        "the royal tribe, the tribe of future kings, carries the guilty member. 'The "
                        "clan of the Zerahites was taken' -- then 'the household of Zabdi was taken' "
                        "-- then 'Achan the son of Carmi' was taken (7:17-18). The narrowing process "
                        "-- from 600,000 men to one -- is a judicial procedure directed by YHWH "
                        "himself. Joshua confronts Achan: 'My son, give glory to the LORD God of "
                        "Israel and give praise to him. And tell me now what you have done; do not "
                        "hide it from me' (7:19). The phrase 'give glory to God' is a demand for "
                        "truthful confession -- the same formula used in John 9:24. Achan confesses: "
                        "'Truly I have sinned against the LORD God of Israel, and this is what I "
                        "did: when I saw among the spoil a beautiful cloak from Shinar, and 200 "
                        "shekels of silver, and a bar of gold weighing 50 shekels, then I coveted "
                        "(chamad) them and took them' (7:20-21). The confession follows the sin "
                        "pattern of Genesis 3:6: I saw, I desired, I took. The cloak 'from Shinar' "
                        "(Babylonia) is a luxury item -- the allure of foreign wealth and culture "
                        "that will plague Israel throughout its history. The items are hidden 'in "
                        "the earth inside my tent' (7:21) -- buried like a corpse, concealed from "
                        "human eyes but not from YHWH's."
            },
            {
                "heading": "Judgment in the Valley of Achor (7:22-26)",
                "body": "Messengers retrieve the stolen items from Achan's tent, confirm the "
                        "confession, and spread the evidence 'before YHWH' (7:23) -- a judicial "
                        "display before the divine judge. Joshua and all Israel take Achan, the "
                        "devoted items, his sons, daughters, oxen, donkeys, sheep, tent, and all "
                        "his possessions to the Valley of Achor. Joshua pronounces judgment: 'Why "
                        "did you bring trouble on us? The LORD brings trouble on you today' (7:25). "
                        "The wordplay on 'akar ('to trouble') and 'Achor' ('trouble') names the "
                        "valley after the event. 'And all Israel stoned him with stones. They "
                        "burned them with fire and stoned them with stones' (7:25). The inclusion "
                        "of Achan's family in the punishment has troubled interpreters. The "
                        "Deuteronomic principle 'fathers shall not be put to death because of their "
                        "children' (Deut 24:16) seems violated. Possible explanations: (1) The "
                        "family knew and conspired in hiding the goods. (2) The cherem violation "
                        "contaminated everything Achan possessed. (3) The narrative reflects the "
                        "corporate solidarity of household identity in ancient Israel. The text does "
                        "not explain -- it reports. A great heap of stones is raised over the site "
                        "'to this day.' 'Then the LORD turned from his burning anger' (7:26). The "
                        "purging of the violation restores YHWH's presence and Israel's effectiveness. "
                        "Hosea 2:15 will later prophesy that 'the Valley of Achor shall become a door "
                        "of hope' -- the place of judgment will become a place of restoration."
            }
        ]
    },

    {
        "id": "josh-8",
        "ref": "Joshua 8",
        "chapter_num": 8,
        "title": "The Conquest of Ai and Covenant Renewal at Shechem",
        "era": "jericho_ai",
        "type": "chapter",

        "synopsis": "With Achan's sin purged, YHWH commands a second assault on Ai: 'Do not fear "
                    "and do not be dismayed... See, I have given into your hand the king of Ai, and "
                    "his people, his city, and his land' (8:1). This time the entire army goes -- "
                    "30,000 men -- and YHWH authorizes taking spoil and livestock (unlike Jericho's "
                    "total herem). Joshua sets an ambush behind the city. His strategy: the main "
                    "force feigns a frontal attack and then retreats, drawing Ai's defenders out of "
                    "the city in pursuit. The ambush force enters the undefended city and sets it "
                    "ablaze. When Ai's soldiers turn back and see their city burning, they are caught "
                    "between the two Israelite forces and destroyed. The king of Ai is captured, "
                    "hanged on a tree (a post-mortem humiliation, not execution by hanging), and "
                    "buried under a stone heap at the city gate. The second half of the chapter "
                    "shifts abruptly to covenant renewal: Joshua builds an altar on Mount Ebal, "
                    "offers sacrifices, writes the law of Moses on plastered stones, and reads 'all "
                    "the words of the law, the blessing and the curse' (8:34) before the assembled "
                    "nation stationed between Mount Ebal and Mount Gerizim -- fulfilling Moses' "
                    "command in Deuteronomy 27:1-8. The juxtaposition of military conquest and "
                    "covenant ceremony is theologically deliberate: victory belongs to YHWH, and "
                    "Israel's response is worship and recommitment to Torah.",

        "key_verse": {
            "ref": "Joshua 8:1",
            "text": "And the LORD said to Joshua, 'Do not fear and do not be dismayed. Take all the fighting men with you, and arise, go up to Ai. See, I have given into your hand the king of Ai, and his people, his city, and his land.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "orev (ambush -- the military tactic YHWH authorizes for Ai)",
            "shalal (spoil/plunder -- permitted at Ai, unlike Jericho's total herem)",
            "talah (to hang -- post-mortem display of the defeated king)",
            "mizbeach (altar -- the altar Joshua builds on Mount Ebal)",
            "avanim shelemot (unhewn stones -- whole stones, not cut with iron tools)",
            "mishneh torah (copy of the law -- the law written on plastered stones)",
            "berakah uqelalah (blessing and curse -- the covenant consequences read at Shechem)"
        ],

        "ane_backdrop": "The ambush tactic is one of the oldest military strategies in the "
                        "ancient Near East. Egyptian military texts from the New Kingdom describe "
                        "feigned retreats used to draw defenders out of fortified positions. The "
                        "practice of hanging defeated kings after death (not as a method of execution "
                        "but as a public display) is attested in Egyptian campaign accounts: pharaohs "
                        "displayed the bodies of defeated enemies on the walls of their cities. "
                        "Deuteronomy 21:22-23 legislates this practice and requires the body to be "
                        "taken down before nightfall ('a hanged man is cursed by God'). The covenant "
                        "ceremony at Shechem between Ebal and Gerizim corresponds to the ceremony "
                        "commanded in Deuteronomy 27. Writing law on plastered stones was a standard "
                        "ANE practice: the Laws of Hammurabi were inscribed on a basalt stele, and "
                        "Egyptian royal inscriptions on plastered surfaces are well-attested. The "
                        "Ebal/Gerizim valley is a natural amphitheater that amplifies sound remarkably "
                        "-- acoustic tests confirm that a speaker in the valley can be heard clearly "
                        "by thousands on the opposing slopes.",

        "second_temple": [
            {
                "source": "4QJosh^a (4Q47)",
                "summary": "The Dead Sea Scrolls Joshua manuscript places the altar-building "
                           "ceremony (8:30-35) after Joshua 5:1 rather than after the Ai conquest. "
                           "This may preserve an older arrangement of the narrative.",
                "relevance": "The textual tradition preserves evidence of alternative narrative "
                             "sequences, suggesting the Shechem ceremony may originally have been "
                             "positioned earlier in the book."
            },
            {
                "source": "Josephus, Antiquities V.1.12-14",
                "summary": "Josephus describes the ambush at Ai in detail, treating it as "
                           "conventional military history, and the Ebal/Gerizim ceremony as a "
                           "solemn covenant renewal.",
                "relevance": "Josephus presents the Ai conquest as historical military strategy "
                             "blessed by divine support -- not pure miracle, unlike Jericho."
            },
            {
                "source": "Mishnah Sotah 7:5",
                "summary": "The Mishnah discusses the Ebal/Gerizim ceremony in detail, debating "
                           "which tribes stood on which mountain and how the blessings and curses "
                           "were pronounced.",
                "relevance": "Rabbinic tradition treated the Shechem ceremony as a foundational "
                             "covenant event, second only to Sinai in significance."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 27:1-8", "note": "Moses' command to build an altar on Mount Ebal and write the law on plastered stones -- fulfilled in Josh 8:30-35", "type": "ot"},
            {"ref": "Deuteronomy 11:29-30", "note": "'You shall set the blessing on Mount Gerizim and the curse on Mount Ebal' -- the framework for the Josh 8 ceremony", "type": "ot"},
            {"ref": "Deuteronomy 21:22-23", "note": "The hanged body must be buried before nightfall -- the law Joshua follows with the king of Ai", "type": "ot"},
            {"ref": "Galatians 3:13", "note": "'Christ redeemed us from the curse of the law by becoming a curse for us -- for it is written, Cursed is everyone who is hanged on a tree' -- Paul connects Deut 21:23 to the cross", "type": "nt"},
            {"ref": "Judges 9:6-7", "note": "Abimelech's coronation at Shechem and Jotham's fable from Mount Gerizim -- the same location as Joshua's covenant ceremony", "type": "ot"},
            {"ref": "John 4:20-24", "note": "The Samaritan woman at the well: 'Our fathers worshiped on this mountain' (Gerizim) -- the Shechem covenant site still contested in Jesus' day", "type": "nt"}
        ],

        "divine_council_note": "The Ai narrative reveals the conditional nature of divine warrior "
                               "support: when the covenant is intact, YHWH fights for Israel; when "
                               "it is violated (Achan), YHWH withdraws. The restoration of victory at "
                               "Ai demonstrates that YHWH's anger, once the violation is purged, does "
                               "not permanently abandon his people. The ambush strategy -- unlike "
                               "Jericho's liturgical warfare -- involves human military planning "
                               "authorized by God. This is important theologically: the divine warrior "
                               "works through both miracle (Jericho) and strategy (Ai). The covenant "
                               "ceremony at Shechem between Ebal and Gerizim is a public declaration "
                               "of YHWH's sovereignty over the land. Writing the Torah on stones in "
                               "the heart of Canaan is a territorial claim: YHWH's law is now inscribed "
                               "on Canaanite territory, replacing the religious and legal authority of "
                               "Canaan's gods. The blessings and curses read from the mountains are "
                               "covenant treaty sanctions -- the divine suzerain declaring the consequences "
                               "of loyalty and rebellion in the hearing of heaven and earth (Deut 30:19). "
                               "The hanging of Ai's king on a tree (8:29) and his removal before sundown "
                               "fulfills Deuteronomy 21:22-23 and foreshadows the theological significance "
                               "Paul will draw from that law (Gal 3:13) -- the cursed one hanging on "
                               "the tree.",

        "sections": [
            {
                "heading": "YHWH's Encouragement and the Ambush Plan (8:1-9)",
                "body": "After the purging of Achan, YHWH speaks to Joshua with the same language "
                        "as the original commission: 'Do not fear and do not be dismayed' (8:1; cf. "
                        "1:9). Fear and dismay are the enemies of faith, and the Ai defeat had "
                        "produced both. YHWH reassures with the prophetic perfect: 'I have given "
                        "into your hand the king of Ai.' This time, however, the strategy involves "
                        "human military planning: Joshua selects 30,000 warriors for a nighttime "
                        "ambush deployment west of the city, between Ai and Bethel. He instructs "
                        "them: 'Do not go very far from the city, but all of you remain ready' (8:4). "
                        "The main force will approach Ai from the front, engage the defenders, and "
                        "then feign retreat. When Ai's forces pursue, the ambush will enter the "
                        "undefended city and set it ablaze. The plan requires coordination, discipline, "
                        "and trust -- military virtues that Israel lacked in the first assault when "
                        "overconfidence replaced dependence on YHWH. The difference between the first "
                        "and second Ai assaults is not merely tactical but theological: the first "
                        "was attempted without YHWH's presence (withdrawn due to the cherem violation); "
                        "the second is commanded by YHWH himself. Human strategy succeeds when it "
                        "operates within the framework of divine authorization."
            },
            {
                "heading": "The Battle: Feigned Retreat and Ambush (8:10-23)",
                "body": "Joshua deploys the ambush force by night. In the morning, he leads the "
                        "main force openly toward Ai, camping 'on the north side of Ai, with a "
                        "valley between him and Ai' (8:11). The king of Ai sees the Israelite force "
                        "and comes out to engage. Joshua's feigned retreat works perfectly: 'They "
                        "fled in the direction of the wilderness' (8:15). All the men of Ai pursue, "
                        "'not a man was left in Ai or Bethel who did not go out after Israel. They "
                        "left the city open and pursued Israel' (8:17). The emptied city is "
                        "defenseless. YHWH commands Joshua: 'Stretch out the javelin (kidon) that "
                        "is in your hand toward Ai, for I will give it into your hand' (8:18). The "
                        "extended javelin is a signal to the ambush force but also a symbolic act: "
                        "like Moses' staff over the Red Sea (Exod 14:16) or his hands raised at "
                        "Rephidim (Exod 17:11-12), the commander's outstretched weapon channels "
                        "divine power. The ambush enters the city and sets it on fire. When Ai's "
                        "soldiers look back and see smoke rising from their city, they are trapped: "
                        "'the men of Ai had no power to flee this way or that' (8:20). The Israelite "
                        "forces close from both sides, and 'all who fell that day, both men and "
                        "women, were 12,000, all the people of Ai' (8:25). The king is taken alive."
            },
            {
                "heading": "The Defeat of the King and the Taking of Spoil (8:24-29)",
                "body": "After the battle, Joshua executes the herem on Ai's population -- but this "
                        "time YHWH has authorized Israel to keep the livestock and spoil (8:2, 27). "
                        "The difference between Jericho (total herem -- no spoil) and Ai (selective "
                        "herem -- spoil permitted) underscores that YHWH sets the terms. The herem "
                        "is not a universal, inflexible rule but a divine command specific to each "
                        "situation. Achan's sin was not merely greed but presumption: he decided for "
                        "himself what to take, rather than waiting for YHWH's instruction. At Ai, "
                        "the same kind of goods Achan stole are freely given -- had he waited, he "
                        "could have taken legitimately. The king of Ai is hanged on a tree (talah "
                        "al ha'ets) -- post-mortem display, not execution by hanging. Joshua "
                        "carefully follows Deuteronomy 21:23: 'at sunset Joshua commanded, and "
                        "they took his body down from the tree and threw it at the entrance of the "
                        "gate of the city and raised over it a great heap of stones, which stands "
                        "to this day' (8:29). The stone heap over the king's body parallels the "
                        "stone heap over Achan in the Valley of Achor -- both are memorial warnings. "
                        "Ai itself is left 'a heap of ruins forever' (8:28) -- the meaning of its "
                        "name ('the ruin') becomes its destiny."
            },
            {
                "heading": "Covenant Renewal at Ebal and Gerizim (8:30-35)",
                "body": "The chapter shifts from battlefield to sacred mountain. 'Then Joshua built "
                        "an altar to the LORD, the God of Israel, on Mount Ebal, just as Moses the "
                        "servant of the LORD had commanded the people of Israel' (8:30-31). The altar "
                        "is built of 'unhewn stones, upon which no man has wielded an iron tool' "
                        "(8:31) -- following the instruction of Exodus 20:25 and Deuteronomy 27:5-6. "
                        "Iron tools would 'profane' (chalal) the stones; the altar must be natural "
                        "creation, untouched by human technology, because it represents the "
                        "intersection of heaven and earth. Burnt offerings and peace offerings are "
                        "sacrificed. Joshua writes 'a copy of the law of Moses' (mishneh torat "
                        "Mosheh) on plastered stones (8:32). The entire nation assembles: half on "
                        "the slopes of Mount Gerizim (the blessing mountain), half on Mount Ebal "
                        "(the curse mountain), with the ark and priests in the valley between them. "
                        "Joshua reads 'all the words of the law, the blessing and the curse, "
                        "according to all that is written in the Book of the Law' (8:34). The "
                        "reading includes 'every word that Moses commanded' -- nothing omitted. "
                        "'There was not a word of all that Moses commanded that Joshua did not read "
                        "before all the assembly of Israel, and the women, and the little ones, and "
                        "the sojourners who lived among them' (8:35). Women, children, and foreign "
                        "residents are explicitly included -- the covenant community is not limited "
                        "to adult Israelite males. This ceremony plants YHWH's Torah in the heart "
                        "of Canaan, transforming the land from pagan territory into covenant space."
            }
        ]
    }
]
