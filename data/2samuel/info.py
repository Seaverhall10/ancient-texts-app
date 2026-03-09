"""
info.py — 2 Samuel (Shemu'el Bet): Scholarly Text Introduction

This file provides the "front page" for 2 Samuel in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

2 Samuel contains the theological apex of the Old Testament — the Davidic
covenant of 2 Samuel 7, where YHWH promises David an eternal throne, an
everlasting dynasty, and a "son" who will reign forever. This is the covenant
that creates the messianic expectation: every subsequent generation looks for
the Son of David who will fulfill YHWH's promise. The book also records
David's encounters with the Rephaim in Jerusalem, his purchase of the
threshing floor where the Temple will stand, and the mysterious tension
between YHWH and Satan in the census narrative — key intersections of the
visible and invisible realms.
"""

TEXT_INFO = {
    "text_id": "2samuel",
    "display_name": "2 Samuel (Shemu'el Bet)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Former Prophets",
        "detail": "2 Samuel is the fourth book of the Former Prophets (Nevi'im Rishonim) in the "
                  "Hebrew Bible and the tenth book of the Christian Old Testament. Originally part "
                  "of a single 'Samuel' scroll, it was divided by the LXX translators. The Talmud "
                  "(Bava Batra 14b-15a) attributes authorship to Samuel, Gad, and Nathan (cf. "
                  "1 Chr 29:29). 2 Samuel is extensively quoted in the New Testament: the Davidic "
                  "covenant (2 Sam 7:12-16) is the foundation of messianic expectation fulfilled in "
                  "Christ (Luke 1:32-33; Acts 2:29-36; 13:22-23, 34; Rom 1:3; 2 Tim 2:8; Heb 1:5); "
                  "David's 'last words' (2 Sam 23:1-7) are considered messianic prophecy; and David's "
                  "purchase of the threshing floor (2 Sam 24) establishes the site of Solomon's Temple "
                  "and, later, the Temple where Jesus taught. No tradition has questioned its canonical "
                  "status."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud attributes the book to Samuel, Gad the seer, and Nathan the prophet "
                       "(Bava Batra 14b-15a; 1 Chr 29:29). Since Samuel died in 1 Samuel 25, Gad and "
                       "Nathan are credited with the material covering David's reign. Both were active "
                       "during David's kingship: Nathan delivered the Davidic covenant oracle (2 Sam 7), "
                       "confronted David over the Bathsheba affair (2 Sam 12), and supported Solomon's "
                       "succession (1 Kings 1). Gad advised David during his fugitive years (1 Sam 22:5) "
                       "and delivered the oracle concerning the census plague (2 Sam 24:11-14). These "
                       "prophets had firsthand knowledge of the events and theological authority to "
                       "interpret them.",

        "scholarly_debate": "The core of 2 Samuel is widely recognized as containing some of the oldest "
                           "and finest prose in the Hebrew Bible. Leonhard Rost (1926) identified the "
                           "'Succession Narrative' or 'Court History of David' (2 Sam 9-20; 1 Kings 1-2) "
                           "as an independent source, possibly by an eyewitness to David's court. This "
                           "source is characterized by realistic characterization, psychological depth, "
                           "restrained divine intervention (God works through human actions rather than "
                           "miracles), and unflinching honesty about David's failures. Some scholars "
                           "(Gerhard von Rad) saw it as an early example of historical writing; others "
                           "(John Van Seters) place it later. The Davidic covenant oracle (2 Sam 7) is "
                           "analyzed by Cross as having Dtr1 (pro-Davidic, pre-exilic) and Dtr2 (exilic, "
                           "conditional elements) layers. The 'appendix' (2 Sam 21-24) is generally seen "
                           "as a collection of independent traditions arranged in a chiastic structure "
                           "(A-B-C-C'-B'-A') and inserted before the Succession Narrative's conclusion.",

        "bottom_line": "2 Samuel draws on sources very close to the events — possibly including "
                       "eyewitness court narratives by figures like Nathan and Gad. The Succession "
                       "Narrative is widely acknowledged as one of the earliest and most sophisticated "
                       "pieces of prose writing in the ancient world. Whether composed in the 10th century "
                       "BC (close to the events) or later, the material reflects intimate knowledge of "
                       "David's court, his family dynamics, and the political intrigues of the early "
                       "monarchy. The Deuteronomistic editorial framework is lighter in 2 Samuel than in "
                       "Judges or Kings, allowing the underlying sources to speak more directly."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events span approximately 1010-970 BC, covering David's entire reign. "
                       "Composition by Gad and Nathan would place the writing within the late 10th "
                       "century BC, with possible compilation shortly after David's death.",
        "critical_range": "The events cover David's reign (~1010-970 BC). The Succession Narrative "
                         "is often dated to the Solomonic era (~970-930 BC) as an early piece of "
                         "Israelite historiography. The Davidic covenant oracle (2 Sam 7) may have "
                         "an original core from the 10th century with Deuteronomistic editing in the "
                         "7th-6th century BC. The appendix material (chapters 21-24) preserves "
                         "independent traditions of varying age. The final DtrH editing is typically "
                         "placed in the exilic period (~550 BC).",
        "evidence": "Key evidence includes: (1) The 4QSam^a scroll from Qumran provides the best "
                    "manuscript evidence, often preserving superior readings to the MT (as with 1 Samuel). "
                    "(2) The 'House of David' inscription from Tel Dan (~840 BC) — the earliest extra-"
                    "biblical reference to the Davidic dynasty — confirms David as the founder of a "
                    "royal house within 150 years of his reign. (3) The Mesha Stele (~840 BC) may also "
                    "reference the 'House of David' (the reading is debated). (4) The political and "
                    "administrative details in 2 Samuel (David's cabinet in 8:15-18 and 20:23-26, "
                    "the census in chapter 24) reflect authentic Iron Age IIA institutions. (5) The "
                    "description of Jerusalem's pre-Davidic fortifications and water systems (5:6-8) "
                    "matches archaeological evidence from the City of David excavations."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Israel — particularly the Davidic court and the people who needed to "
                            "understand the legitimacy and theology of the Davidic dynasty. The book "
                            "addresses both the glory of David's reign (the covenant, the conquests, the "
                            "establishment of Jerusalem) and its devastating failures (Bathsheba, Amnon, "
                            "Absalom's rebellion), providing a brutally honest portrait that legitimizes "
                            "the dynasty not by whitewashing David but by showing YHWH's sovereign grace "
                            "working through a deeply flawed instrument.",

        "purpose": "2 Samuel has two primary theological purposes: (1) To establish the Davidic covenant "
                   "as the centerpiece of YHWH's redemptive plan — the promise of an eternal throne, an "
                   "everlasting dynasty, and a 'son' with a unique father-son relationship to YHWH "
                   "(7:12-16). This covenant does not cancel the Mosaic covenant but builds upon it, "
                   "creating a new channel through which YHWH's purposes for Israel and the world will "
                   "be fulfilled. (2) To demonstrate the consequences of sin even for the chosen king — "
                   "David's adultery with Bathsheba and murder of Uriah bring devastating judgment "
                   "('the sword shall never depart from your house,' 12:10), yet YHWH does not revoke "
                   "the covenant. Grace and judgment coexist in David's story.",

        "theological_intent": "The Davidic covenant (2 Sam 7) is the theological heart of the book and "
                             "one of the most important passages in the entire Bible. YHWH's promise to "
                             "David includes: (a) a great name (7:9); (b) a place for Israel (7:10); "
                             "(c) rest from enemies (7:11); (d) a dynasty — 'your house and your kingdom "
                             "shall be made sure forever before me; your throne shall be established "
                             "forever' (7:16); (e) a father-son relationship with David's offspring — "
                             "'I will be to him a father, and he shall be to me a son' (7:14). This "
                             "father-son language becomes the foundation of messianic christology: Jesus "
                             "is the 'Son of God' not merely in a general sense but as the fulfillment "
                             "of the Davidic covenant promise. Hebrews 1:5 explicitly applies 2 Sam 7:14 "
                             "to Christ."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "2 Samuel contains some of the finest narrative prose in the Hebrew Bible. "
                           "The Succession Narrative (chapters 9-20) is characterized by understated, "
                           "psychologically penetrating narration — the narrator reports actions and "
                           "dialogue but rarely comments on motives, leaving the reader to infer the "
                           "characters' inner states. David's lament over Saul and Jonathan (1:19-27) "
                           "is among the greatest Hebrew poetry: 'How the mighty have fallen!' (1:19, 25, "
                           "27). David's 'Last Words' (23:1-7) use archaic poetic language with possible "
                           "northern dialectal features. The Song of David (chapter 22, paralleled in "
                           "Psalm 18) is a royal psalm with divine warrior theophanic imagery. The MT "
                           "text of 2 Samuel, like 1 Samuel, shows corruption in places, and the "
                           "4QSam^a scroll and LXX often preserve better readings.",
        "grammar_match": "The prose style shifts between several registers: the formal covenant oracle "
                        "of chapter 7 (Deuteronomistic), the terse military reports of chapters 8 and "
                        "10-12, the psychologically rich Succession Narrative (chapters 9-20), the "
                        "archaic poetry of the laments and psalms (chapters 1, 22, 23), and the "
                        "administrative lists (8:15-18; 20:23-26; 23:8-39). This diversity reflects "
                        "multiple source types unified by editorial vision."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "2 Samuel IS scripture — the book that establishes the Davidic covenant, the "
                   "theological foundation of messianic expectation and New Testament christology.",
        "nt_usage": "The Davidic covenant (2 Sam 7:12-16) is the single most quoted/alluded-to Old "
                    "Testament passage in the New Testament's christological arguments. Gabriel's "
                    "annunciation to Mary directly echoes it: 'The Lord God will give to him the throne "
                    "of his father David, and he will reign over the house of Jacob forever, and of his "
                    "kingdom there will be no end' (Luke 1:32-33; cf. 2 Sam 7:12-16). Peter's Pentecost "
                    "sermon argues that David spoke prophetically about the Messiah's resurrection "
                    "(Acts 2:29-36). Paul opens Romans by declaring Jesus 'descended from David according "
                    "to the flesh' (Rom 1:3; cf. 2 Tim 2:8). Hebrews 1:5 applies the father-son "
                    "language of 2 Sam 7:14 directly to Christ. Jesus repeatedly uses and accepts the "
                    "title 'Son of David' (Matt 1:1; 9:27; 12:23; 15:22; 20:30-31; 21:9, 15; 22:42-45).",
        "internal_consistency": "2 Samuel fulfills 1 Samuel's trajectory and establishes the foundation "
                               "for Kings. David's anointing (1 Sam 16:13) leads to his enthronement "
                               "(2 Sam 2:4; 5:3). The promise to Abraham of land, nation, and blessing "
                               "(Gen 12:1-3) finds partial fulfillment in David's empire (2 Sam 8). The "
                               "census and the threshing floor purchase (2 Sam 24; cf. 1 Chr 21) "
                               "establish the Temple site, connecting to Solomon's building in 1 Kings 6. "
                               "The Rephaim encounters (2 Sam 5:18-25; 21:15-22) continue the Nephilim "
                               "war from Joshua and Judges."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls: 4QSam^a (4Q51) is the primary witness, preserving large "
                    "sections of both 1 and 2 Samuel. For 2 Samuel, it covers portions of chapters "
                    "2-24 with significant gaps. As with 1 Samuel, 4QSam^a frequently agrees with "
                    "the LXX against the MT and sometimes preserves superior readings.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The MT of 2 Samuel is better preserved than 1 Samuel but still shows corruption "
                     "in places. The parallel passage in 1 Chronicles is sometimes used to correct "
                     "difficult MT readings (e.g., 2 Sam 24:1 vs. 1 Chr 21:1 on the census's divine "
                     "instigation)."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The LXX of 2 Samuel provides important textual corrections. The 'Lucianic' or "
                     "'Antiochene' text of Samuel-Kings is particularly valuable, preserving readings "
                     "confirmed by 4QSam^a that were lost from the MT."},
            {"name": "Dead Sea Scrolls (4QSam^a)", "date": "~50 BC",
             "note": "Critical for establishing the earliest recoverable text. Frank Moore Cross "
                     "demonstrated that the LXX Vorlage was a text closely related to 4QSam^a."},
            {"name": "1 Chronicles parallel", "date": "Post-exilic composition, ~400 BC",
             "note": "1 Chronicles 11-29 parallels much of 2 Samuel, sometimes with significant "
                     "theological interpretive differences. The most famous is 2 Sam 24:1 ('YHWH "
                     "incited David') vs. 1 Chr 21:1 ('Satan incited David')."}
        ],
        "reliability": "The textual situation for 2 Samuel mirrors 1 Samuel: the MT has suffered "
                       "corruption but the major theological content is stable. The 4QSam^a scroll "
                       "and LXX are essential for recovering the best text. The Davidic covenant "
                       "oracle (chapter 7) is remarkably stable across all witnesses — the passage "
                       "that matters most theologically is the best preserved."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "2 Samuel covers David's reign (~1010-970 BC), the Iron Age IIA period. David "
                   "established Jerusalem as his capital by capturing the Jebusite fortress (~1003 BC), "
                   "created a small empire stretching from the border of Egypt to the Euphrates, and "
                   "organized the administrative, military, and religious institutions of the monarchy. "
                   "This was a window of opportunity: the great powers (Egypt, Assyria, Babylon) were "
                   "in decline or preoccupied, allowing a small Levantine state to expand.",

        "geography": "Key locations include: Hebron (David's first capital, where he reigned over Judah "
                     "for seven years), Jerusalem/Zion (captured from the Jebusites and made the new "
                     "capital — a stroke of political genius, as it belonged to no tribe), the Valley "
                     "of Rephaim (southwest of Jerusalem, where David defeated the Philistines twice), "
                     "Rabbah (modern Amman, capital of Ammon, besieged during the Bathsheba affair), "
                     "the threshing floor of Araunah/Ornan on Mount Moriah (where the Temple would be "
                     "built). The 'forest of Ephraim' (18:6) is the site of Absalom's defeat.",

        "historical_connections": "The Tel Dan Inscription (~840 BC) references the 'House of David' "
                                 "(bytdwd), providing the earliest extra-biblical confirmation of the "
                                 "Davidic dynasty. The Mesha Stele (~840 BC) may also reference David's "
                                 "house. Archaeological work in the City of David (Eilat Mazar's excavations) "
                                 "has uncovered a 'Large Stone Structure' that some identify with David's "
                                 "palace, though this identification is debated. The description of David's "
                                 "administrative structure (2 Sam 8:15-18; 20:23-26) parallels known Egyptian "
                                 "and Canaanite bureaucratic models, suggesting Israelite state formation "
                                 "followed established Near Eastern patterns."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "major",
        "summary": "2 Samuel contains four key divine council themes: the Davidic covenant, the Rephaim "
                   "encounters, the census-incitement problem, and the threshing floor as cosmic mountain."
                   "\n\n"
                   "THE DAVIDIC COVENANT (2 Sam 7:12-16): YHWH's promise to David establishes a "
                   "unique divine-human relationship: 'I will be to him a father, and he shall be "
                   "to me a son' (7:14). This is divine council adoption language — the Davidic king "
                   "is installed as YHWH's son, his viceroy on earth, his human representative in "
                   "the council. Psalm 2:7 ('You are my son; today I have begotten you') and Psalm "
                   "89:26-27 ('He shall cry to me, \"You are my Father\"... I will make him the "
                   "firstborn, the highest of the kings of the earth') develop this adoption theology. "
                   "The Davidic king sits at YHWH's right hand (Psalm 110:1), participates in the "
                   "divine council as its human member, and exercises YHWH's authority on earth. The "
                   "promise of an 'eternal' throne points beyond any single human king to the ultimate "
                   "Son of David — the messianic figure who is both David's son and David's Lord "
                   "(Matt 22:41-46; Psalm 110:1)."
                   "\n\n"
                   "THE REPHAIM IN JERUSALEM (2 Sam 5:18-25; 21:15-22): The Valley of Rephaim "
                   "(emeq repha'im) southwest of Jerusalem is named for the giant clan — the Rephaim, "
                   "who are connected to the Nephilim tradition. David fights the Philistines there "
                   "twice, and both times YHWH provides supernatural direction (5:23-24, 'When you "
                   "hear the sound of marching in the tops of the balsam trees, then rouse yourself, "
                   "for then YHWH has gone out before you to strike down the army of the Philistines'). "
                   "The 'sound of marching' in the treetops is the invisible army of YHWH — the "
                   "divine council's heavenly host going to war. In 2 Sam 21:15-22, David's warriors "
                   "kill four Rephaim warriors from Gath, described as 'descendants of the giants' "
                   "(yelidei harafah). These are the last Nephilim remnant — the final cleanup of the "
                   "bloodline that began in Genesis 6:1-4."
                   "\n\n"
                   "THE CENSUS PROBLEM (2 Sam 24:1 vs. 1 Chr 21:1): 2 Samuel 24:1 states 'the anger "
                   "of YHWH was kindled against Israel, and he incited David' to take a census. "
                   "1 Chronicles 21:1, describing the same event, says 'Satan stood against Israel "
                   "and incited David.' This is one of the most important divine council texts: both "
                   "statements are true because Satan (the adversary, the accuser) operates within "
                   "YHWH's sovereign permission. The pattern is identical to Job 1-2, where Satan "
                   "acts against Job but only with YHWH's authorization. In the divine council "
                   "framework, the 'satan' (adversary) is a member of YHWH's council who functions "
                   "as a prosecuting attorney — he accuses and tests, but only within limits set by "
                   "YHWH. The Chronicler's naming of Satan makes explicit what was implicit in the "
                   "Samuel narrative."
                   "\n\n"
                   "THE THRESHING FLOOR AND THE COSMIC MOUNTAIN (2 Sam 24:18-25): David purchases "
                   "the threshing floor of Araunah the Jebusite on Mount Moriah — the site where "
                   "Solomon will build the Temple (2 Chr 3:1) and where, according to Jewish tradition, "
                   "Abraham bound Isaac (Gen 22:2). The threshing floor is a liminal space in the "
                   "ancient Near East — a flat, elevated, open-air surface associated with divine "
                   "encounters (cf. Ruth 3, the threshing floor scene; 1 Kings 22:10, the kings on "
                   "their threshing floor at the gate of Samaria). David's altar on this site, where "
                   "the destroying angel's plague is stopped, establishes the location of YHWH's "
                   "earthly dwelling — the cosmic mountain where heaven and earth meet.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 24-25 (the Davidic covenant and the divine council son)",
            "The Unseen Realm, chapter 18-19 (Rephaim and the Nephilim remnant cleanup)",
            "The Unseen Realm, chapter 4-5 (the 'two powers in heaven' — YHWH and YHWH's son)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 2-3 (Satan as divine council member)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 8-9 (the destroying angel)",
            "The Naked Bible Podcast, episodes 113-118 (2 Samuel and the divine council)",
            "The Naked Bible Podcast, episode 45 (the divine council scene of Job 1-2 — parallels the census problem)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Davidic Covenant — The Most Important Promise After Abraham",
            "body": "The Davidic covenant (2 Sam 7:12-16) is the theological hinge of the Old Testament. "
                    "Everything before it prepares for it (the Abrahamic promise of blessing, the Mosaic "
                    "covenant, the conquest and settlement); everything after it looks back to it (the "
                    "prophets, the psalms, the exile as the apparent failure of the promise, and the New "
                    "Testament's proclamation that Jesus fulfills it). The promise has three dimensions: "
                    "(1) dynastic — David will always have a descendant on the throne; (2) filial — the "
                    "king will have a unique father-son relationship with YHWH; (3) eternal — the throne "
                    "will be established 'forever' (olam). The conditional element (7:14b, 'When he "
                    "commits iniquity, I will discipline him') explains the exile: the covenant is not "
                    "broken but the dynasty is disciplined. The unconditional element ('my steadfast love "
                    "will not depart from him,' 7:15) guarantees ultimate fulfillment. Jesus is the "
                    "resolution: the Son of David who is also the Son of God, the eternal king whose "
                    "throne will never be shaken."
        },
        {
            "type": "interpretation",
            "title": "YHWH or Satan? The Census Incitement",
            "body": "The tension between 2 Samuel 24:1 ('YHWH incited David') and 1 Chronicles 21:1 "
                    "('Satan incited David') is not a contradiction but a complementary pair that reveals "
                    "the divine council's operations. The principle of primary and secondary causation is "
                    "at work: YHWH permits the satan (adversary) to act as the immediate agent, while "
                    "YHWH remains the ultimate sovereign authority. This is exactly the pattern in Job "
                    "1-2: YHWH gives Satan permission to test Job, so both 'YHWH gave and YHWH has taken "
                    "away' (Job 1:21) and 'Satan struck Job' (Job 2:7) are true simultaneously. The "
                    "divine council operates under YHWH's authority — rebel members can only act within "
                    "the limits YHWH permits. The Chronicler's explicit naming of Satan reflects a later "
                    "development in Israel's understanding of the divine council's internal dynamics, "
                    "influenced by the exile's encounter with Zoroastrian dualism and the fuller "
                    "revelation of the satan figure in Job and Zechariah 3."
        },
        {
            "type": "context",
            "title": "The Rephaim Warriors — Last of the Nephilim",
            "body": "2 Samuel 21:15-22 records the deaths of four Rephaim warriors from Gath at the "
                    "hands of David's elite soldiers: Ishbi-benob (who had a spear weighing 300 "
                    "shekels of bronze), Saph/Sippai, the unnamed brother of Goliath (whose spear "
                    "'shaft was like a weaver's beam'), and a man of extraordinary stature with six "
                    "fingers on each hand and six toes on each foot. All four are called yelidei "
                    "harafah — 'descendants of the giant' (or 'of the Raphah'). The polydactyly "
                    "(extra digits) is particularly significant: it may indicate genetic anomalies "
                    "associated with the Nephilim bloodline, or it may simply mark these individuals "
                    "as 'other' — physically distinct in ways that the biblical authors associated "
                    "with the cursed giant lineage. The systematic killing of these four warriors, "
                    "combined with David's earlier victory over Goliath (1 Sam 17), effectively ends "
                    "the Nephilim remnant in Canaan — a campaign that began with Joshua's attack on "
                    "the Anakim (Josh 11:21-22) and reaches its completion under David."
        },
        {
            "type": "scholarship",
            "title": "The Tel Dan Inscription — David Confirmed",
            "body": "The Tel Dan Inscription, discovered in 1993-1994 at the site of ancient Dan in "
                    "northern Israel, is a fragmentary Aramaic stele erected by an Aramean king (likely "
                    "Hazael of Damascus, ~840 BC) commemorating his victories over Israel and Judah. "
                    "The critical phrase is 'bytdwd' — 'House of David' — which constitutes the earliest "
                    "extra-biblical reference to David and his dynasty. Before this discovery, some "
                    "minimalist scholars had argued that David was a legendary figure rather than a "
                    "historical king. The inscription confirms that within ~150 years of David's reign, "
                    "his name was recognized by a foreign power as the founder of the Judahite royal "
                    "house. The Mesha Stele (~840 BC) may also contain a reference to the 'House of "
                    "David' in a damaged line, though the reading is debated. These inscriptions provide "
                    "important external corroboration for the historical core of 2 Samuel."
        }
    ]
}
