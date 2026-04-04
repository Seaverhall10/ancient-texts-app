"""
era_48_saul_rise.py -- Israel Demands a King and Saul's Rise and Fall (1 Samuel 8-15)

Israel rejects YHWH's direct kingship and demands a human king 'like all the
nations.' YHWH grants the request as both concession and judgment. Saul, tall,
handsome, and from Benjamin -- the smallest tribe -- is anointed by Samuel,
receives the Spirit of YHWH, and wins early military victories. But his reign
unravels through two acts of disobedience: unauthorized sacrifice at Gilgal and
incomplete execution of the herem against Amalek. YHWH rejects Saul as king,
and the Spirit departs. This section establishes the theology of kingship in
Israel: the king rules under YHWH's authority, and obedience to the divine word
is the non-negotiable condition of legitimate rule.
"""

CHAPTERS = [
    {
        "id": "1sam-8",
        "ref": "1 Samuel 8",
        "chapter_num": 8,
        "title": "Israel Demands a King -- Rejecting YHWH's Kingship",
        "era": "saul_rise",
        "type": "chapter",
        "themes": ["KING", "DC", "NATIONS", "COV", "RIV"],

        "synopsis": "Samuel grows old and appoints his sons Joel and Abijah as judges, but they are "
                    "corrupt -- taking bribes and perverting justice (8:3). The elders of Israel gather "
                    "at Ramah and demand: 'Appoint for us a king to judge us like all the nations' "
                    "(8:5). Samuel is displeased, but YHWH tells him: 'Obey the voice of the people in "
                    "all that they say to you, for they have not rejected you, but they have rejected me "
                    "from being king over them' (8:7). This is the theological crux: Israel's demand for "
                    "a human king is a rejection of YHWH's direct theocratic rule. YHWH instructs Samuel "
                    "to warn them of the 'manner of the king' (mishpat hamelek) -- a catalog of royal "
                    "exactions: he will take their sons for his chariots and his fields, their daughters "
                    "for his perfumers and cooks, the best of their fields and vineyards, a tenth of "
                    "their grain and flocks, and their servants. 'You shall be his slaves. And in that "
                    "day you will cry out because of your king whom you have chosen for yourselves, but "
                    "YHWH will not answer you in that day' (8:17-18). The people refuse to listen: 'No! "
                    "But there shall be a king over us, that we also may be like all the nations, and "
                    "that our king may judge us and go out before us and fight our battles' (8:19-20). "
                    "The phrase 'like all the nations' is the theological indictment: Israel's calling "
                    "was to be unlike the nations (Deut 7:6; 14:2), set apart as YHWH's own people.",

        "key_verse": {
            "ref": "1 Samuel 8:7",
            "text": "And the LORD said to Samuel, 'Obey the voice of the people in all that they say to you, for they have not rejected you, but they have rejected me from being king over them.'",
            "translation": "ESV"
        },

        "original_terms": [
            "melek (king -- Hebrew melek is the standard ANE title for a sovereign ruler. Israel's demand for a melek replaces YHWH's direct theocratic rule with a human intermediary. The irony: YHWH IS their melek, but they want one they can see)",
            "mishpat hamelek (manner/right of the king -- lit. 'the judgment/custom of the king'; a catalog of what the king will take. This is not legislation but warning: here is what human kingship will cost you. Every item in the list came true under Solomon)",
            "ma'as (to reject -- the verb YHWH uses: 'they have rejected (ma'as) ME from being king over them.' The same verb will be used when YHWH rejects Saul (15:23, 26) -- a bitter symmetry: the people rejected YHWH; their king will be rejected by YHWH)",
            "goyim (nations -- 'like all the nations (goyim).' The goyim are the peoples allotted to the sons of God under Deuteronomy 32:8-9; Israel's calling was to be UNLIKE them, governed directly by YHWH rather than by a subordinate elohim through a human king)",
            "malak (to reign/be king -- YHWH has been Israel's malak, their reigning king, since the exodus. The demand for a human king is a structural demotion of YHWH from sovereign to background deity)",
            "ro'eh / navi (seer / prophet -- 1 Samuel 9:9 contains an important editorial note: 'formerly in Israel, when a man went to inquire of God, he said, Come, let us go to the ro'eh (seer), for today's navi (prophet) was formerly called a ro'eh (seer).' The ro'eh (from ra'ah, 'to see') emphasizes the prophet's ability to SEE what others cannot -- spiritual sight, visions, hidden knowledge. The navi (from an uncertain root, possibly 'to call' or 'to bubble up') emphasizes the prophet's role as SPEAKER -- one who proclaims YHWH's word. Samuel is called both: he sees the future (seer) and he speaks for YHWH (prophet). The shift in terminology reflects the evolution of the prophetic office from local visionary to public spokesman for the divine council)"
        ],

        "ane_backdrop": "Israel's demand for kingship mirrors the transition from tribal to monarchic "
                        "government attested across the ANE. City-states in Mesopotamia transitioned from "
                        "conciliar rule to kingship; the Sumerian King List narrates how 'kingship "
                        "descended from heaven' after the flood. In Canaan, the Amarna Letters (~1350 BC) "
                        "show petty kings governing city-states. Samuel's 'manner of the king' (8:11-18) "
                        "closely resembles descriptions of Canaanite kingship in Ugaritic texts: the king "
                        "levied conscription, taxed agricultural produce, and requisitioned labor. The "
                        "Deuteronomic law of the king (Deut 17:14-20) anticipated this request and placed "
                        "strict limits on the king: he must not multiply horses (military alliance with "
                        "Egypt), wives, or silver and gold, and he must write his own copy of the Torah. "
                        "Israel's request violates the spirit of Deuteronomy 17 by desiring a king 'like "
                        "all the nations' rather than the Torah-shaped king Deuteronomy prescribed.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities VI.3.3",
                "summary": "Josephus frames the elders' request as reasonable, noting their dissatisfaction "
                           "with Samuel's corrupt sons and the Philistine threat.",
                "relevance": "Josephus softens the theological critique, presenting the request as "
                             "political pragmatism rather than covenant betrayal."
            },
            {
                "source": "Deuteronomy 17:14-20",
                "summary": "Moses anticipated Israel's request for a king and legislated strict conditions: "
                           "the king must be chosen by YHWH, must be an Israelite, and must be governed by "
                           "the Torah.",
                "relevance": "The law of the king shows that monarchy was not inherently wrong -- the sin "
                             "was demanding a king 'like the nations' rather than accepting YHWH's model."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 17:14-20", "note": "The Torah's law of the king -- anticipated, limited, Torah-shaped", "type": "ot"},
            {"ref": "Judges 8:22-23", "note": "Gideon refused kingship: 'I will not rule over you... YHWH will rule over you' -- the theocratic ideal Israel now rejects", "type": "ot"},
            {"ref": "Judges 21:25", "note": "'Everyone did what was right in his own eyes' -- the chaos that made the demand for kingship understandable", "type": "ot"},
            {"ref": "Hosea 13:10-11", "note": "'Where now is your king, to save you?... I gave you a king in my anger, and I took him away in my wrath'", "type": "ot"},
            {"ref": "Acts 13:21", "note": "'They asked for a king, and God gave them Saul the son of Kish' -- the NT summary of this episode", "type": "nt"},
            {"ref": "Isaiah 33:22", "note": "'YHWH is our judge; YHWH is our lawgiver; YHWH is our king' -- the theocratic ideal Israel abandoned", "type": "ot"}
        ],

        "divine_council_note": "Israel's demand for a king 'like all the nations' (8:5, 20) is a divine "
                               "council category error. Under the Deuteronomy 32:8-9 framework, the nations "
                               "were allotted to the sons of God (bene 'elohim) as their rulers, while "
                               "Israel was YHWH's direct portion (nachalah). The nations had divine-human "
                               "kingship mediated through their allotted 'elohim; Israel had YHWH himself "
                               "as king. To demand a king 'like the nations' is to demand the governance "
                               "structure of the nations under their lesser 'elohim rather than the unique "
                               "theocratic structure of YHWH's own people. YHWH's response is both "
                               "concession and judgment: he grants a king but interprets the request as "
                               "rejection -- 'they have rejected me from being king over them' (8:7). The "
                               "monarchy will function within the covenant, but it will always exist in "
                               "tension with YHWH's direct kingship. The human king rules as YHWH's vassal, "
                               "not as a sovereign in his own right.",

        "sections": [
            {
                "heading": "Samuel's Corrupt Sons and the Elders' Demand (8:1-9)",
                "body": "Samuel's sons repeat the pattern of Eli's sons: they are appointed to positions "
                        "of authority but abuse them for personal gain. 'His sons did not walk in his "
                        "ways but turned aside after gain, took bribes, and perverted justice' (8:3). "
                        "The institutional failure of the judgeship provides the political pretext for "
                        "the kingship demand. The elders present two reasons: Samuel's age and his sons' "
                        "corruption. But their actual request reveals a deeper desire: 'a king to judge "
                        "us like all the nations' (8:5). The phrase 'like all the nations' (kekol "
                        "haggoyim) is the theological indictment. YHWH tells Samuel not to take it "
                        "personally: 'According to all the deeds that they have done, from the day I "
                        "brought them up out of Egypt even to this day, forsaking me and serving other "
                        "gods, so they are also doing to you' (8:8). The demand for a king is continuous "
                        "with the pattern of apostasy that has characterized Israel since the exodus."
            },
            {
                "heading": "The Manner of the King: Samuel's Warning (8:10-22)",
                "body": "Samuel delivers YHWH's warning in the form of the 'manner of the king' (mishpat "
                        "hamelek) -- a comprehensive list of royal exactions. The king will take their "
                        "sons for his chariots, horsemen, and runners (8:11); appoint commanders of "
                        "thousands and fifties (8:12); conscript laborers for plowing, reaping, and "
                        "weapon-making (8:12); take daughters as perfumers, cooks, and bakers (8:13); "
                        "confiscate the best fields, vineyards, and olive orchards for his courtiers "
                        "(8:14); tithe their grain and vintage for his officers (8:15); requisition "
                        "servants, donkeys, and flocks (8:16); and take a tenth of their flocks (8:17). "
                        "The climax: 'You shall be his slaves (avadim)' (8:17). The irony is devastating: "
                        "YHWH brought them out of Egypt to free them from slavery to Pharaoh; now they "
                        "are choosing a new form of servitude. 'And in that day you will cry out because "
                        "of your king whom you have chosen for yourselves, but YHWH will not answer you "
                        "in that day' (8:18). The people refuse the warning: 'No! But there shall be a "
                        "king over us' (8:19). YHWH tells Samuel to grant their request."
            }
        ]
    },

    {
        "id": "1sam-9-12",
        "ref": "1 Samuel 9-12",
        "chapter_num": 9,
        "title": "Saul Anointed, Spirit-Empowered, and Publicly Confirmed",
        "era": "saul_rise",
        "type": "chapter",
        "themes": ["KING", "SPIRIT", "COV"],

        "synopsis": "Saul son of Kish, of the tribe of Benjamin, is introduced: 'a handsome young man, "
                    "taller than any of the people from his shoulders upward' (9:2). His search for lost "
                    "donkeys brings him to Samuel, whom YHWH has already told: 'Tomorrow about this time "
                    "I will send to you a man from the land of Benjamin, and you shall anoint him to be "
                    "prince (nagid) over my people Israel' (9:16). Samuel anoints Saul privately and "
                    "gives him three signs to confirm the calling: he will meet men at Rachel's tomb, "
                    "then three men going to Bethel, and finally a band of prophets with musical "
                    "instruments. 'Then the Spirit of YHWH will rush upon you, and you will prophesy "
                    "with them, and you will be turned into another man' (10:6). All three signs occur. "
                    "Saul prophesies among the prophets, prompting the proverb: 'Is Saul also among the "
                    "prophets?' (10:11). At Mizpah, Samuel presents Saul by lot before all Israel -- "
                    "the lot falls on Benjamin, then on the family of Matri, then on Saul himself, who "
                    "is found hiding among the baggage (10:22). Samuel proclaims: 'Do you see him whom "
                    "YHWH has chosen? There is none like him among all the people' (10:24). Saul proves "
                    "himself militarily by rescuing Jabesh-gilead from the Ammonite Nahash (ch. 11), "
                    "and the kingship is renewed at Gilgal. Samuel delivers his farewell speech (ch. 12), "
                    "calling heaven and earth as witnesses and invoking thunder in the wheat harvest as a "
                    "sign that YHWH is displeased with the kingship request.",

        "key_verse": {
            "ref": "1 Samuel 10:6",
            "text": "Then the Spirit of the LORD will rush upon you, and you will prophesy with them and be turned into another man.",
            "translation": "ESV"
        },

        "original_terms": [
            "nagid (prince/leader/commander -- the title Samuel uses rather than melek, 'king.' YHWH remains the true king; Saul is appointed nagid, the military commander who serves under the divine king. This is Israel's unique contribution to political theology: the human ruler is always subordinate to the divine sovereign)",
            "mashiach (anointed one -- from mashach, 'to anoint with oil.' Saul is Israel's first mashiach (messiah/anointed king). The anointing oil signifies divine selection and empowerment: YHWH has chosen this person, and YHWH's spirit now rests on him. Every subsequent Israelite king was a mashiach, but the title eventually pointed forward to THE Mashiach -- the ultimate Anointed King whom David's line would produce)",
            "ruach YHWH (Spirit of YHWH -- the divine empowerment that rushes upon Saul. Hebrew ruach means 'wind, breath, spirit.' The ruach YHWH is YHWH's own executive power -- not a separate being but YHWH's active presence operating through a human agent. When the ruach comes upon someone, they are enabled to do what they could never do naturally: prophesy, fight with superhuman strength, lead with divine wisdom. The ruach is conditional and revocable -- it comes upon Saul here and departs from him in chapter 16)",
            "tsalach (to rush upon -- the Spirit's sudden, overwhelming seizure of a person; the same verb used for Samson's feats of strength)",
            "goral (lot -- the casting of lots (small stones, sticks, or similar objects) to determine YHWH's will. The process works by elimination: tribe, then clan, then individual. The underlying theology: 'The lot is cast into the lap, but its every decision is from YHWH' (Prov 16:33))",
            "nevi'im (prophets -- the band of prophesying ecstatics Saul joins after his anointing. These are not individual prophets like Samuel but a prophetic guild (benei haneviim, 'sons of the prophets') who prophesy with musical instruments. Ecstatic prophecy -- involving altered states, group chanting, and musical trance -- was one form of Israelite prophecy alongside the more structured 'word of YHWH' prophecy of figures like Samuel)"
        ],

        "ane_backdrop": "Royal anointing was practiced across the ANE. Egyptian pharaohs were anointed "
                        "with sacred oil during their coronation; Hittite kings were anointed as part of "
                        "the enthronement ritual. In Israel, anointing (mashach) set the king apart as "
                        "YHWH's chosen agent -- the 'messiah' (mashiach, 'anointed one'). The title nagid "
                        "('prince, commander') rather than melek ('king') may emphasize that YHWH remains "
                        "the true king and Saul is his military commander. The Spirit-empowerment pattern "
                        "connects Saul to the judges (Othniel, Gideon, Jephthah, Samson) who received the "
                        "Spirit for specific military tasks. The lot-casting at Mizpah follows the ANE "
                        "practice of sacred lots (Urim and Thummim in Israel) to determine the divine "
                        "will. The proverb 'Is Saul also among the prophets?' indicates surprise at a "
                        "non-prophetic figure exhibiting ecstatic prophetic behavior -- the Spirit's "
                        "power overrides social expectation.",

        "second_temple": [
            {
                "source": "Acts 13:21",
                "summary": "Paul summarizes: 'Then they asked for a king, and God gave them Saul the "
                           "son of Kish, a man of the tribe of Benjamin, for forty years.'",
                "relevance": "The New Testament treats Saul's reign as a divinely permitted but "
                             "ultimately inadequate kingship that prepared the way for David."
            },
            {
                "source": "Josephus, Antiquities VI.4.1",
                "summary": "Josephus emphasizes Saul's initial humility (hiding among the baggage) and "
                           "his physical impressiveness, portraying him as a reluctant king.",
                "relevance": "The reluctance motif is theologically significant: the best kings are those "
                             "who do not seek power -- a pattern David will also exhibit."
            }
        ],

        "cross_refs": [
            {"ref": "Judges 3:10; 6:34; 11:29; 14:6", "note": "The Spirit of YHWH upon the judges -- the same empowerment pattern now applied to Israel's first king", "type": "ot"},
            {"ref": "1 Samuel 16:13-14", "note": "The Spirit will depart from Saul and come upon David -- the transfer of divine empowerment", "type": "ot"},
            {"ref": "Acts 1:26", "note": "The apostles cast lots to choose Matthias -- the same lot-casting method used to identify Saul", "type": "nt"},
            {"ref": "Proverbs 16:33", "note": "'The lot is cast into the lap, but its every decision is from YHWH' -- the theology behind the Mizpah selection", "type": "ot"}
        ],

        "divine_council_note": "The 'Spirit of YHWH' (ruach YHWH) that rushes upon Saul (10:6, 10) is "
                               "the divine council's empowerment. The ruach is YHWH's executive power -- "
                               "the presence of the heavenly sovereign operating through a human agent. "
                               "When the Spirit 'rushes upon' (tsalach) Saul, he is 'turned into another "
                               "man' (10:6) -- a transformation that enables prophetic speech and military "
                               "prowess beyond natural capacity. This empowerment is conditional and "
                               "revocable: the Spirit that comes upon Saul in chapter 10 will depart from "
                               "him in chapter 16. In the divine council framework, the Spirit's presence "
                               "marks the legitimate ruler; the Spirit's departure marks the illegitimate "
                               "one. The title nagid ('commander, prince') rather than melek ('king') may "
                               "reflect the divine council hierarchy: YHWH is the melek, and the human "
                               "ruler is his nagid -- a military appointee serving under the cosmic king.",

        "sections": [
            {
                "heading": "Saul's Anointing and the Three Signs (9:1-10:16)",
                "body": "The narrative introduces Saul with careful detail: he is from the 'smallest of "
                        "the tribes of Israel' (Benjamin, 9:21), tall, handsome, and the son of a 'man "
                        "of wealth' (gibbor chayil, 9:1). His search for his father's lost donkeys "
                        "brings him providentially to Samuel at Zuph. YHWH has already revealed to "
                        "Samuel: 'About this time tomorrow I will send you a man from Benjamin, and you "
                        "shall anoint him to be nagid over my people Israel. He shall save my people "
                        "from the hand of the Philistines' (9:16). Samuel hosts Saul at a feast, gives "
                        "him the place of honor, and the next morning anoints him privately with a flask "
                        "of oil (10:1). The anointing is accompanied by three confirmatory signs, each "
                        "geographically specific: at Rachel's tomb (Benjamin's matriarch), at the oak of "
                        "Tabor, and at Gibeah of God (a Philistine garrison town). The third sign is the "
                        "most dramatic: Saul will meet a band of prophets descending from the high place "
                        "with instruments, and 'the Spirit of YHWH will rush upon you' (10:6). The verb "
                        "tsalach ('to rush, to fall upon powerfully') describes the Spirit's sudden, "
                        "overwhelming presence -- the same verb used for Samson's feats of strength "
                        "(Judg 14:6, 19; 15:14). All three signs are fulfilled. Saul prophesies among "
                        "the prophets, generating the proverb: 'Is Saul also among the prophets?' (10:11)."
            },
            {
                "heading": "Public Selection, Military Victory, and Samuel's Farewell (10:17-12:25)",
                "body": "At Mizpah, Samuel assembles Israel for the public identification of the king by "
                        "lot. The lot narrows from tribe (Benjamin) to clan (Matri) to individual (Saul), "
                        "but Saul is nowhere to be found. YHWH reveals: 'Behold, he has hidden himself "
                        "among the baggage' (10:22). The image is complex: humility or fear? The narrator "
                        "leaves it ambiguous. When Saul is brought forward, his physical stature is "
                        "emphasized: 'he was taller than any of the people from his shoulders upward' "
                        "(10:23). Some 'worthless fellows' (bene beliyya'al) despise him, but Saul holds "
                        "his peace. His first military test comes when Nahash the Ammonite besieges "
                        "Jabesh-gilead, demanding to gouge out every right eye as a condition of peace "
                        "(11:2). When the messengers reach Saul, 'the Spirit of God rushed upon Saul "
                        "when he heard these words, and his anger was greatly kindled' (11:6). He "
                        "musters Israel by cutting up a yoke of oxen and sending the pieces throughout "
                        "the land (echoing the Levite's act in Judges 19:29). Israel rallies 330,000 "
                        "strong and defeats the Ammonites. The kingship is 'renewed' at Gilgal with "
                        "sacrifices and rejoicing (11:14-15). Samuel's farewell speech (ch. 12) is a "
                        "covenant lawsuit: he calls YHWH and his anointed as witnesses to his own "
                        "integrity, recounts YHWH's saving acts from Egypt to the present, and warns "
                        "that both king and people must obey YHWH or face judgment. He invokes thunder "
                        "and rain during the wheat harvest -- a meteorological impossibility in Israel's "
                        "dry season -- as a sign that YHWH is displeased with the kingship request."
            }
        ]
    },

    {
        "id": "1sam-13-15",
        "ref": "1 Samuel 13-15",
        "chapter_num": 13,
        "title": "Saul's Disobedience and Rejection -- Obedience vs. Sacrifice",
        "era": "saul_rise",
        "type": "chapter",
        "themes": ["KING", "HOLY", "RIV", "BLOOD"],

        "synopsis": "Saul's reign deteriorates through two decisive acts of disobedience. First, at "
                    "Gilgal, facing a massive Philistine force while his troops desert, Saul grows "
                    "impatient waiting for Samuel and offers the burnt offering himself (13:8-9). Samuel "
                    "arrives and condemns him: 'You have done foolishly. You have not kept the command "
                    "of YHWH your God... Now your kingdom shall not continue. YHWH has sought out a man "
                    "after his own heart' (13:13-14). Jonathan, Saul's son, proves the military hero -- "
                    "attacking a Philistine garrison with only his armor-bearer, declaring: 'Nothing can "
                    "hinder YHWH from saving by many or by few' (14:6). YHWH sends panic on the "
                    "Philistines. But Saul's rash oath -- forbidding food under curse during battle -- "
                    "nearly kills Jonathan, who unknowingly eats honey (14:27). The people rescue "
                    "Jonathan. Second, YHWH through Samuel commands Saul to execute total herem "
                    "(devotion to destruction) against Amalek: 'Go and strike Amalek and devote to "
                    "destruction all that they have. Do not spare them' (15:3). Saul defeats the "
                    "Amalekites but spares King Agag and 'the best of the sheep and of the oxen' (15:9). "
                    "YHWH tells Samuel: 'I regret (nacham) that I have made Saul king, for he has turned "
                    "back from following me' (15:11). Samuel confronts Saul with the devastating oracle: "
                    "'Has YHWH as great delight in burnt offerings and sacrifices, as in obeying the "
                    "voice of YHWH? Behold, to obey is better than sacrifice, and to listen than the "
                    "fat of rams' (15:22). Saul is rejected. Samuel hews Agag in pieces before YHWH at "
                    "Gilgal. Samuel and Saul part, never to meet again.",

        "key_verse": {
            "ref": "1 Samuel 15:22-23",
            "text": "And Samuel said, 'Has the LORD as great delight in burnt offerings and sacrifices, as in obeying the voice of the LORD? Behold, to obey is better than sacrifice, and to listen than the fat of rams. For rebellion is as the sin of divination, and presumption is as iniquity and idolatry. Because you have rejected the word of the LORD, he has also rejected you from being king.'",
            "translation": "ESV"
        },

        "original_terms": [
            "herem (devotion to destruction / the ban -- a form of sacred warfare in which everything captured -- people, animals, possessions -- is 'devoted' to the deity and must be utterly destroyed. Nothing may be kept as personal spoil because the victory and its spoils belong entirely to YHWH. The concept is attested in the Mesha Stele, where Moab's king likewise 'devoted' captured cities to his god Chemosh. Saul's failure to execute the herem fully is treated not as mere disobedience but as sacrilege -- keeping what belongs to God)",
            "nacham (to regret/relent -- 'I regret (nacham) that I have made Saul king.' This is anthropopathic language (describing God in human emotional terms). It does not mean YHWH made a mistake but that YHWH genuinely grieves the outcome of Saul's choices. The tension is felt within the same chapter: 15:11 says YHWH 'regrets'; 15:29 says 'the Glory of Israel will not lie or nacham, for he is not a man that he should nacham.' The paradox is intentional: YHWH experiences something analogous to regret without being subject to fickleness)",
            "shama (to hear/obey -- 'to obey (shama) is better than sacrifice.' Hebrew shama means both 'to hear' and 'to obey' -- the idea being that truly hearing YHWH's voice results in obedience. You cannot 'hear' God and remain unchanged)",
            "qesem (divination -- Samuel equates rebellion with qesem, the occult practice of seeking hidden knowledge through forbidden techniques: casting lots with spirits, reading animal entrails, interpreting omens. The equation is deliberate: both rebellion and divination attempt to manipulate or bypass YHWH's declared will)",
            "ish kilvavo (man after his [God's] own heart -- the description of Saul's unnamed successor, David. 'After his heart' does not mean 'perfectly obedient' but 'aligned with YHWH's purposes' -- a king whose fundamental orientation is toward YHWH, even when he fails)",
            "Agag (the Amalekite king spared by Saul -- his name recurs centuries later in Esther, where Haman is identified as 'the Agagite' (Est 3:1). The implication: Saul's failure to execute YHWH's judgment against Amalek's royal line produced a descendant who nearly annihilated the Jewish people. Partial obedience has generational consequences)"
        ],

        "ane_backdrop": "The herem (ban) was a form of sacred warfare attested in the ANE. The Mesha "
                        "Stele records Moab's king devoting captured cities and populations to Chemosh "
                        "in language remarkably similar to Israelite herem texts. The concept: the spoils "
                        "of war belong to the deity, not the soldiers. To keep what is devoted to God "
                        "is sacrilege. Amalek had a specific historical enmity with Israel: they attacked "
                        "the weakest stragglers during the exodus (Exod 17:8-16; Deut 25:17-19). YHWH's "
                        "command to destroy Amalek (15:2-3) is the fulfillment of the oath in Exodus "
                        "17:14-16: 'YHWH will have war with Amalek from generation to generation.' Saul's "
                        "decision to spare Agag and the best livestock is presented as religious "
                        "rationalization: he claims the animals were saved 'to sacrifice to YHWH your "
                        "God' (15:21). Samuel's response cuts through the rationalization: obedience is "
                        "the primary demand, not cultic performance.",

        "second_temple": [
            {
                "source": "Sirach 46:19-20",
                "summary": "Ben Sira records that Samuel 'called upon the Mighty One' and 'bore witness "
                           "before YHWH and his anointed,' emphasizing Samuel's role as the covenant "
                           "enforcer who held kings accountable.",
                "relevance": "The prophet-over-king dynamic established by Samuel becomes the template "
                             "for all subsequent prophetic confrontation of royal power."
            },
            {
                "source": "Hosea 6:6",
                "summary": "'I desire steadfast love (hesed) and not sacrifice, the knowledge of God "
                           "rather than burnt offerings.'",
                "relevance": "Hosea's oracle echoes Samuel's principle: YHWH prioritizes covenant "
                             "obedience and relational loyalty over cultic performance."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 17:8-16", "note": "'YHWH will have war with Amalek from generation to generation' -- the oath Saul was commissioned to fulfill", "type": "ot"},
            {"ref": "Deuteronomy 25:17-19", "note": "'You shall blot out the memory of Amalek' -- the command Saul partially disobeyed", "type": "ot"},
            {"ref": "Hosea 6:6", "note": "'I desire mercy, not sacrifice' -- the prophetic principle Samuel establishes in 15:22", "type": "ot"},
            {"ref": "Matthew 9:13", "note": "Jesus quotes Hosea 6:6: 'Go and learn what this means: I desire mercy, not sacrifice'", "type": "nt"},
            {"ref": "Acts 13:22", "note": "'He raised up David... a man after my heart, who will do all my will' -- quoting 1 Sam 13:14", "type": "nt"},
            {"ref": "Micah 6:6-8", "note": "'What does YHWH require of you but to do justice, and to love hesed, and to walk humbly?' -- the obedience-over-sacrifice principle", "type": "ot"},
            {"ref": "Esther 3:1", "note": "'Haman the Agagite' -- a descendant of the Amalekite royal line Saul failed to destroy; consequences cascade", "type": "ot"}
        ],

        "divine_council_note": "Samuel's declaration that 'rebellion is as the sin of divination (qesem)' "
                               "(15:23) connects Saul's disobedience to the forbidden practices of the "
                               "nations. Divination (qesem) is the attempt to access supernatural "
                               "knowledge through illicit means -- consulting spirits, reading omens, "
                               "manipulating the divine realm. In the divine council framework, qesem is "
                               "the technology of the fallen 'elohim: Deuteronomy 18:9-14 lists divination "
                               "practices as the abominations of the nations whom YHWH is driving out. "
                               "Samuel equates Saul's disobedience with these practices because both share "
                               "the same root: the refusal to submit to YHWH's authority and the attempt "
                               "to control the outcome through unauthorized means. Saul's partial obedience "
                               "is total disobedience -- he has redefined YHWH's command according to his "
                               "own judgment, which is the essence of the original rebellion in Eden. "
                               "YHWH's 'regret' (nacham) over making Saul king (15:11, 35) is "
                               "anthropopathic language for the divine council's reassessment: the human "
                               "agent has failed, and a new agent must be appointed.",

        "sections": [
            {
                "heading": "Unauthorized Sacrifice at Gilgal (13:1-15)",
                "body": "Saul faces a crisis: the Philistines have amassed 30,000 chariots, 6,000 "
                        "horsemen, and innumerable infantry at Michmash (13:5). Saul's troops panic and "
                        "desert; he waits seven days at Gilgal for Samuel, as instructed (10:8). When "
                        "Samuel does not come at the expected time and the army is scattering, Saul takes "
                        "matters into his own hands: 'Bring the burnt offering here to me, and the peace "
                        "offerings. And he offered the burnt offering' (13:9). This is not merely "
                        "impatience but a usurpation of the priestly-prophetic role. Samuel arrives "
                        "immediately after and delivers the sentence: 'You have done foolishly. You have "
                        "not kept the command of YHWH your God, which he commanded you. For then YHWH "
                        "would have established your kingdom over Israel forever. But now your kingdom "
                        "shall not continue. YHWH has sought out a man after his own heart (ish kilvo), "
                        "and YHWH has commanded him to be prince (nagid) over his people' (13:13-14). "
                        "The phrase 'man after his own heart' is the first reference to David, though "
                        "unnamed. The kingdom is not immediately removed from Saul, but the dynastic "
                        "promise is revoked: Saul's house will not continue on the throne."
            },
            {
                "heading": "Jonathan's Faith and Saul's Rash Oath (14:1-52)",
                "body": "Jonathan and his armor-bearer attack a Philistine garrison at the pass of "
                        "Michmash: 'Come, let us go over to the garrison of these uncircumcised. It may "
                        "be that YHWH will work for us, for nothing can hinder YHWH from saving by many "
                        "or by few' (14:6). Jonathan's theology is the opposite of Saul's: he acts in "
                        "faith without requiring control of the outcome. YHWH sends an earthquake and "
                        "panic on the Philistines. Meanwhile Saul has bound the army with a rash oath: "
                        "'Cursed be the man who eats food until evening and until I am avenged on my "
                        "enemies' (14:24). Jonathan, not having heard the oath, eats wild honey and his "
                        "'eyes became bright' (14:27). When the lot reveals Jonathan as the oath-breaker, "
                        "Saul is ready to execute his own son: 'God do so to me and more also; you shall "
                        "surely die, Jonathan' (14:44). The people intervene: 'Shall Jonathan die, who "
                        "has worked this great salvation in Israel? Far from it!' (14:45). The irony is "
                        "sharp: the man of faith (Jonathan) is nearly killed by the man of control "
                        "(Saul). The chapter demonstrates the contrast between faith-driven courage "
                        "and fear-driven manipulation."
            },
            {
                "heading": "The Amalekite Herem and Saul's Rejection (15:1-35)",
                "body": "Samuel delivers YHWH's commission: 'Go and strike Amalek and devote to "
                        "destruction (herem) all that they have' (15:3). The command is total: men, "
                        "women, children, livestock -- everything. Saul defeats the Amalekites but "
                        "spares King Agag and 'the best of the sheep and of the oxen and of the fattened "
                        "calves and the lambs, and all that was good' (15:9). YHWH speaks to Samuel: 'I "
                        "regret (nacham) that I have made Saul king, for he has turned back from "
                        "following me and has not performed my commands' (15:11). Samuel confronts Saul, "
                        "who offers an astonishing defense: 'I have obeyed the voice of YHWH... but the "
                        "people took of the spoil... to sacrifice to YHWH your God at Gilgal' (15:20-21). "
                        "He simultaneously claims obedience and admits disobedience, then blames the "
                        "people, then rationalizes the sin as piety. Samuel's response is one of the "
                        "greatest prophetic oracles: 'Has YHWH as great delight in burnt offerings and "
                        "sacrifices, as in obeying the voice of YHWH? Behold, to obey is better than "
                        "sacrifice, and to listen than the fat of rams. For rebellion is as the sin of "
                        "divination (qesem), and presumption is as iniquity and idolatry (teraphim). "
                        "Because you have rejected the word of YHWH, he has also rejected you from being "
                        "king' (15:22-23). Saul begs forgiveness, grasps Samuel's robe and tears it. "
                        "Samuel seizes the moment: 'YHWH has torn the kingdom of Israel from you this "
                        "day and has given it to a neighbor of yours, who is better than you' (15:28). "
                        "Samuel hews Agag in pieces 'before YHWH at Gilgal' (15:33) -- executing the "
                        "herem the king refused. They never meet again."
            }
        ]
    }
]
