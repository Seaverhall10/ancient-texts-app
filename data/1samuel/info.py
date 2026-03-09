"""
info.py — 1 Samuel (Shemu'el Aleph): Scholarly Text Introduction

This file provides the "front page" for 1 Samuel in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

1 Samuel is the hinge book of the Old Testament — the transition from the
chaotic judges period to the monarchy that will produce the Davidic covenant,
the temple, and ultimately the Messiah. It contains some of the most vivid
divine council encounters in scripture: the Ark of the Covenant overpowering
Dagon in the Philistine temple, the medium at Endor summoning Samuel's spirit,
and David's defeat of Goliath — the Nephilim remnant warrior from Gath. The
book is saturated with the question of authority: Who will rule Israel? A
faithless priest (Eli)? A compromised king (Saul)? A man after God's own
heart (David)?
"""

TEXT_INFO = {
    "text_id": "1samuel",
    "display_name": "1 Samuel (Shemu'el Aleph)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Former Prophets",
        "detail": "1 Samuel is the third book of the Former Prophets (Nevi'im Rishonim) in the "
                  "Hebrew Bible and the ninth book of the Christian Old Testament. In the Hebrew "
                  "Bible, 1 and 2 Samuel were originally a single book called 'Samuel' (Shemu'el), "
                  "divided into two by the Septuagint translators (who titled them '1-2 Kingdoms' or "
                  "'1-2 Reigns,' with 1-2 Kings being '3-4 Kingdoms'). The Talmud (Bava Batra 14b-15a) "
                  "states: 'Samuel wrote the book that bears his name.' Since Samuel dies in 1 Samuel 25, "
                  "the Talmud adds that Gad the seer and Nathan the prophet completed the work (cf. "
                  "1 Chr 29:29). The book is extensively quoted and alluded to in the New Testament: "
                  "Hannah's prayer (1 Sam 2:1-10) is the model for the Magnificat (Luke 1:46-55); "
                  "David's eating of the showbread (1 Sam 21:1-6) is cited by Jesus (Matt 12:3-4; "
                  "Mark 2:25-26; Luke 6:3-4); Paul's Antioch sermon references Samuel, Saul, and "
                  "David (Acts 13:20-22). No tradition has questioned the canonical status of 1 Samuel."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud (Bava Batra 14b-15a) attributes authorship to Samuel himself for the "
                       "portions covering events during his lifetime, with Gad and Nathan completing the "
                       "narrative after Samuel's death. This is supported by 1 Chronicles 29:29: 'Now "
                       "the acts of King David, from first to last, are written in the Chronicles of "
                       "Samuel the seer, and in the Chronicles of Nathan the prophet, and in the "
                       "Chronicles of Gad the seer.' This suggests that multiple prophetic sources were "
                       "used to compile the book, each associated with a specific prophetic author. "
                       "Samuel's prophetic authority, his role in anointing both Saul and David, and "
                       "his position as the last judge and first great prophet of the monarchy make him "
                       "the natural author of the core narrative.",

        "scholarly_debate": "Modern scholarship places 1-2 Samuel within the Deuteronomistic History, "
                           "though the relationship is more complex than for other DtrH books. The "
                           "material in 1 Samuel appears to draw on several independent sources: (1) The "
                           "Ark Narrative (1 Sam 4:1-7:1) — a self-contained account of the Ark's capture "
                           "and return that may predate the DtrH. (2) The Rise of David narrative (1 Sam "
                           "16-2 Sam 5) — a continuous, vivid account of David's ascent to power, possibly "
                           "written by a court historian. (3) The Samuel-Saul traditions — prophetic "
                           "narratives about Samuel's call, Saul's anointing and rejection. P. Kyle "
                           "McCarter's Anchor Bible commentary (1980, 1984) provides the definitive "
                           "critical analysis, identifying multiple sources woven into the DtrH framework. "
                           "The presence of apparent 'doublets' (two accounts of Saul's anointing, two "
                           "accounts of David sparing Saul) has been interpreted as either dual sources "
                           "or complementary episodes. The text of 1 Samuel is notably more corrupt than "
                           "other books — the 4QSam^a Dead Sea Scroll often agrees with the LXX against "
                           "the MT, suggesting the MT suffered more transmission damage here.",

        "bottom_line": "The book draws on genuinely early sources — the Ark Narrative, prophetic traditions "
                       "about Samuel and Saul, and court narratives about David's rise — compiled and "
                       "edited within the Deuteronomistic framework. Whether Samuel, Gad, and Nathan wrote "
                       "the original sources or later editors compiled them, the material has deep roots "
                       "in the 11th-10th century BC. The theological vision is consistent with the broader "
                       "DtrH: YHWH is sovereign over Israel's political history, and kingship is valid only "
                       "when the king submits to YHWH's prophetic word."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events span approximately 1100-1010 BC, from Samuel's birth to just before "
                       "David's reign. Composition by Samuel, Gad, and Nathan would place the writing "
                       "within the 11th-10th century BC.",
        "critical_range": "The events described span the late 11th century to ~1010 BC. The final form "
                         "is dated to the exilic period within the DtrH (~550 BC), but the sources are "
                         "much earlier: the Ark Narrative is often dated to the 10th century BC, and the "
                         "Rise of David narrative is considered one of the oldest extended prose texts "
                         "in the Bible, possibly from the early Solomonic period. The 4QSam^a scroll "
                         "from Qumran (~50 BC) preserves a text that is often superior to the MT, "
                         "suggesting the MT of 1 Samuel suffered significant textual damage in "
                         "transmission.",
        "evidence": "Key evidence includes: (1) The 4QSam^a (4Q51) manuscript from Qumran is the "
                    "longest Samuel manuscript from the Dead Sea Scrolls and frequently agrees with "
                    "the LXX against the MT, indicating a Hebrew Vorlage for the LXX that differs "
                    "from the proto-MT. Some readings are clearly superior (e.g., 4QSam^a preserves "
                    "a paragraph before 1 Sam 11 about Nahash's atrocities against the Gadites, "
                    "which explains the context for Jabesh-Gilead's plea). (2) The Philistine "
                    "cultural details — Dagon worship, the lords (seranim) of the five cities, "
                    "military technology (iron weapons, chariots) — match archaeological evidence from "
                    "Iron Age I Philistine sites. (3) The description of pre-monarchic Israelite "
                    "society (no standing army, tribal muster system, local shrines at Ramah, Shiloh, "
                    "Nob, Gilgal) fits the archaeological picture of Iron Age I. (4) David's interactions "
                    "with the Philistines, Moabites, and other peoples reflect known Iron Age I "
                    "geopolitical conditions."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Israel — particularly those who needed to understand the legitimacy of "
                            "David's kingship and why Saul's dynasty was rejected. The book functions "
                            "as a political theology: David is the chosen king, anointed by YHWH's "
                            "prophet, and his rise to power — despite Saul's persecution — demonstrates "
                            "YHWH's sovereignty over Israel's political future. For the exilic audience "
                            "of the DtrH, 1 Samuel established the foundational principles of Israelite "
                            "kingship: the king rules under YHWH's authority, mediated through the "
                            "prophetic word, and rejection of that authority leads to rejection of the "
                            "king.",

        "purpose": "1 Samuel traces the transition from the judges to the monarchy through three "
                   "figures — Samuel, Saul, and David — each representing a different model of "
                   "leadership. Samuel is the ideal prophet-judge: faithful, obedient, intercessory. "
                   "Saul is the failed king: chosen by YHWH but destroyed by disobedience, jealousy, "
                   "and resort to forbidden spiritual practices. David is the chosen king: a flawed "
                   "but repentant man who trusts YHWH rather than his own strength. The book makes "
                   "clear that the monarchy is both a concession to Israel's demand ('Give us a king "
                   "like the nations,' 8:5) and YHWH's sovereign choice to establish a dynasty through "
                   "which the Messiah will come.",

        "theological_intent": "The book's deepest theological concern is the relationship between "
                             "divine sovereignty and human kingship. YHWH is the true king of Israel; "
                             "the human king is his viceroy, ruling under YHWH's authority as mediated "
                             "through the prophetic word. When Saul usurps priestly prerogatives (13:8-14) "
                             "and disobeys the herem command against Amalek (15:1-35), he violates the "
                             "fundamental principle of theocratic kingship. Samuel's rebuke — 'to obey "
                             "is better than sacrifice' (15:22) — establishes the prophetic critique of "
                             "kingship that will run through the entire Deuteronomistic History. David's "
                             "anointing 'in the midst of his brothers' (16:13) and the Spirit of YHWH "
                             "rushing upon him represent the divine council's investiture of YHWH's "
                             "chosen ruler."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "1 Samuel's Hebrew is narrative prose of the highest quality, but the MT "
                           "text has suffered more corruption than most biblical books. Numerous passages "
                           "are textually difficult: 1 Sam 13:1 ('Saul was [?] years old when he began "
                           "to reign') has a missing numeral in the MT; 14:41 is garbled in the MT but "
                           "preserved more fully in the LXX (revealing the Urim and Thummim procedure). "
                           "The 4QSam^a scroll has demonstrated that many 'difficult' MT readings are "
                           "textual corruptions with better readings preserved in the LXX tradition. "
                           "Hannah's prayer (2:1-10) is early Hebrew poetry with archaic features. The "
                           "narrative style alternates between vivid, psychologically rich storytelling "
                           "(the David-Saul relationship, the David-Jonathan friendship) and formal "
                           "prophetic speech (Samuel's oracles). The Philistine vocabulary — seranim "
                           "(lords), kova (helmet), shiryon (coat of mail) — includes loanwords from "
                           "Aegean/Anatolian languages consistent with the Philistines' Sea Peoples origin.",
        "grammar_match": "The narrative prose of 1 Samuel is distinguished by its psychological depth "
                        "and dramatic irony. The narrator uses dialogue, interior monologue, and "
                        "contrasting scenes to create complex characterization rarely matched in ancient "
                        "literature. The Hebrew employs standard narrative tense (wayyiqtol) for event "
                        "sequence but varies sentence structure to signal shifts in perspective and "
                        "emotional tone. Robert Alter has described the David narrative as the first "
                        "great work of prose fiction in Western literature — though the qualifying "
                        "word 'fiction' is contested by those who affirm its historical basis."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "1 Samuel IS scripture — the foundational narrative of the Davidic monarchy "
                   "and the prophetic theology of kingship under YHWH.",
        "nt_usage": "1 Samuel is extensively quoted and alluded to in the New Testament. Jesus cites "
                    "David's eating of the showbread at Nob (1 Sam 21:1-6) to justify his disciples' "
                    "Sabbath gleaning (Matt 12:3-4; Mark 2:25-26; Luke 6:3-4). Paul's Antioch sermon "
                    "quotes YHWH's rejection of Saul and selection of David: 'I have found David son of "
                    "Jesse, a man after my own heart, who will do all my will' (Acts 13:22, combining "
                    "1 Sam 13:14 and Psalm 89:20). Hannah's prayer (1 Sam 2:1-10), which celebrates "
                    "YHWH's reversal of human power structures, is the clear model for Mary's Magnificat "
                    "(Luke 1:46-55). The theology of divine election — YHWH choosing the youngest, "
                    "least expected son (16:1-13) — anticipates the pattern of 1 Corinthians 1:27 "
                    "('God chose the foolish things of the world to shame the wise'). David as the "
                    "anointed (mashiakh) of YHWH becomes the foundational category for understanding "
                    "Jesus as the Christ (Christos = Messiah = anointed one).",
        "internal_consistency": "1 Samuel bridges Judges and 2 Samuel seamlessly. The decline of the "
                               "priesthood (Eli's corrupt sons, 2:12-17) continues the pattern of "
                               "institutional failure in Judges. Samuel's call narrative (chapter 3) "
                               "echoes Moses' call. The Philistine threat intensifies from Judges "
                               "(Samson) through 1 Samuel (Saul and David). The Anakim remnant at "
                               "Gaza, Gath, and Ashdod (Josh 11:22) explains Goliath's presence at "
                               "Gath. The Davidic covenant anticipated in 1 Samuel 16 is formally "
                               "established in 2 Samuel 7. The reference to the 'Book of Jashar' "
                               "(2 Sam 1:18) connects to the same lost collection cited in Joshua 10:13."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls: Three manuscripts of Samuel have been identified at Qumran — "
                    "4QSam^a (4Q51), 4QSam^b (4Q52), and 4QSam^c (4Q53). The most important is "
                    "4QSam^a, which is one of the largest biblical manuscripts from Qumran and frequently "
                    "preserves superior readings to the MT. Frank Moore Cross's work on 4QSam^a "
                    "demonstrated that the LXX was translated from a Hebrew Vorlage closely resembling "
                    "this scroll, not from the proto-MT tradition.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The MT of Samuel is more corrupt than any other biblical book. Numerous passages "
                     "have missing words, garbled syntax, or unintelligible readings. The most famous "
                     "problem is 1 Sam 13:1 (Saul's missing age). The MT tradition for Samuel likely "
                     "suffered from a damaged archetype early in transmission."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The LXX of Samuel often preserves superior readings to the MT, supported by "
                     "4QSam^a. Key examples: 1 Sam 1:22 (LXX adds detail about Hannah's vow), "
                     "1 Sam 10:27-11:1 (LXX/4QSam^a preserve the Nahash expansion), 1 Sam 14:41 "
                     "(LXX preserves the full Urim/Thummim oracle procedure). The LXX 'Lucianic' "
                     "recension (proto-Lucianic text) is particularly important for Samuel."},
            {"name": "Dead Sea Scrolls (4QSam^a)", "date": "~50 BC",
             "note": "The most important DSS manuscript for Samuel. Contains large portions of both "
                     "1 and 2 Samuel. Frequently agrees with LXX against MT. Cross argued it represents "
                     "the Old Palestinian text type from which the LXX was translated."},
            {"name": "Targum Jonathan", "date": "1st-3rd century AD tradition",
             "note": "The Aramaic translation interprets theological difficulties. At 1 Sam 28 (Endor), "
                     "the Targum identifies Samuel's appearance as genuine but frames it within "
                     "acceptable theological categories."}
        ],
        "reliability": "1 Samuel presents the most complex textual situation of any Old Testament book. "
                       "The MT has suffered significant corruption, and critical scholarship (McCarter, "
                       "Cross, Tov) regularly corrects the MT using the LXX and 4QSam^a. However, the "
                       "major narrative content and theological themes are stable across all witnesses. "
                       "The textual issues primarily affect details within episodes, not the overall "
                       "structure or theological message of the book."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "1 Samuel spans the late 11th century BC, from Samuel's birth (~1100 BC) to the "
                   "eve of David's reign (~1010 BC). This is the Iron Age I / Iron Age IIA transition, "
                   "a period when Israel moved from a decentralized tribal confederation to a centralized "
                   "monarchy. The Philistines were the dominant military power on the coastal plain, "
                   "with superior iron weapons technology (1 Sam 13:19-22 describes their monopoly on "
                   "ironworking). The Shiloh sanctuary was destroyed — probably by the Philistines after "
                   "the battle of Aphek (1 Sam 4) — an event confirmed by archaeology (destruction layers "
                   "at Shiloh dating to ~1050 BC) and referenced in Jeremiah 7:12-14 and 26:6.",

        "geography": "The narrative ranges across the central hill country of Benjamin and Judah. Key "
                     "locations include: Shiloh (the tabernacle sanctuary, destroyed after the Ark's "
                     "capture), Ramah (Samuel's home and prophetic headquarters), Gibeah (Saul's "
                     "capital, identified with Tell el-Ful ~5 km north of Jerusalem), Bethlehem "
                     "(David's hometown), the Elah Valley (the site of the Goliath encounter), Nob "
                     "(the priestly city massacred by Saul), En-Gedi and the Wilderness of Ziph "
                     "(David's hiding places), Ziklag (the Philistine town given to David by Achish "
                     "of Gath), and Endor (where Saul consulted the medium).",

        "historical_connections": "The Philistine settlement is confirmed by archaeology: excavations at "
                                 "Ekron (Tel Miqne), Ashkelon, Ashdod, and Gath reveal Aegean-style "
                                 "pottery, architecture, and cultural practices consistent with Sea Peoples "
                                 "origin. The iron monopoly described in 1 Sam 13:19-22 is consistent with "
                                 "early Iron Age metallurgical evidence. The transition from tribal "
                                 "confederation to monarchy mirrors broader patterns in the ancient Near "
                                 "East during this period. The Ammonite threat (1 Sam 11) is consistent "
                                 "with known Iron Age Transjordanian politics."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "major",
        "summary": "1 Samuel contains three of the most dramatic divine council encounters in the "
                   "Old Testament: the Ark's victory over Dagon, David's defeat of Goliath, and "
                   "the necromancy at Endor. Each episode operates at the intersection of the "
                   "visible and invisible realms."
                   "\n\n"
                   "THE ARK AND DAGON (1 Sam 5:1-5): When the Philistines capture the Ark of the "
                   "Covenant and place it in Dagon's temple at Ashdod, Dagon's statue is found "
                   "prostrate before the Ark — then found the next morning with head and hands "
                   "severed on the threshold. This is not merely an idol falling over; it is a "
                   "divine council power encounter. The Ark is YHWH's throne — his footstool on "
                   "earth (1 Chr 28:2; Ps 99:5; 132:7-8), the meeting point between the visible "
                   "and invisible realms, flanked by the cherubim (the divine council throne-"
                   "guardians). Dagon is the patron deity of the Philistines — a real spiritual "
                   "entity in the Deuteronomy 32 framework. The Ark's presence in Dagon's temple "
                   "is a clash between YHWH and a rival elohim, and YHWH wins decisively. The "
                   "plagues that follow (tumors and mice, 5:6-12) echo the Egyptian plagues — "
                   "YHWH judging the gods of the nation (cf. Exod 12:12)."
                   "\n\n"
                   "DAVID AND GOLIATH (1 Sam 17): Goliath of Gath is explicitly identified as a "
                   "giant — his height (six cubits and a span, ~9.5 feet in the MT; four cubits "
                   "and a span, ~6.5 feet in 4QSam^a and the LXX) and his city of origin (Gath, "
                   "one of the three cities where the Anakim survived per Josh 11:22) connect him "
                   "directly to the Nephilim remnant. The Anakim were 'of the Nephilim' (Num 13:33), "
                   "the offspring of the Watchers' illicit union with human women (Gen 6:1-4; "
                   "1 Enoch 6-16). David's battle with Goliath is not just a military contest — "
                   "it is the continuation of the cosmic war against the Nephilim bloodline that "
                   "began with the Flood, continued through the conquest (Josh 11:21-22), and will "
                   "not be fully resolved until the eschatological judgment. David's declaration "
                   "that the battle 'belongs to YHWH' (17:47) and his fight 'in the name of YHWH "
                   "of hosts (tseva'ot), the God of the armies of Israel' (17:45) are divine "
                   "council warfare language — YHWH fights through his human agent against the "
                   "seed of the rebellious Watchers."
                   "\n\n"
                   "THE MEDIUM AT ENDOR (1 Sam 28:3-25): Saul, abandoned by YHWH ('YHWH did not "
                   "answer him, either by dreams, or by Urim, or by prophets,' 28:6), consults a "
                   "medium (ba'alat ob, literally 'mistress of a spirit/pit') to summon Samuel's "
                   "ghost. The passage is extraordinary: the medium sees 'an elohim coming up out "
                   "of the earth' (28:13) — using the word elohim for a deceased human spirit, "
                   "confirming that the term refers to a resident of the spiritual realm, not "
                   "exclusively to God. Samuel actually appears and delivers a genuine prophetic "
                   "oracle (28:16-19) that comes true the next day. The text does not present this "
                   "as a demonic deception but as a genuine, terrifying encounter with the dead — "
                   "one that is forbidden precisely because the spiritual realm is real and dangerous. "
                   "The Endor episode is critical evidence for the biblical understanding of the "
                   "afterlife and the spiritual nature of the departed.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 18-19 (the Nephilim remnant and David's giant-killing)",
            "The Unseen Realm, chapter 7 (elohim as a term for spiritual beings, including the dead at Endor)",
            "Supernatural, chapter 15-16 (Goliath and the Nephilim connection)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 5 (the Rephaim, Anakim, and Nephilim bloodline)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 2 (elohim as 'residents of the spiritual realm')",
            "The Naked Bible Podcast, episode 56 (the Endor necromancy and the elohim of 1 Sam 28)",
            "The Naked Bible Podcast, episodes 109-112 (1 Samuel and the divine council)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "interpretation",
            "title": "Goliath and the Nephilim Remnant",
            "body": "Goliath is not merely a tall Philistine soldier — he is the biological descendant "
                    "of the Anakim, who are 'of the Nephilim' (Num 13:33). Joshua 11:21-22 records that "
                    "the Anakim were cut off from the hill country but survived in three Philistine cities: "
                    "Gaza, Gath, and Ashdod. Goliath is from Gath. His extraordinary size, his association "
                    "with a family of giants (2 Sam 21:15-22 records four additional Rephaim warriors from "
                    "Gath, including one with six fingers on each hand and six toes on each foot), and his "
                    "defiance of YHWH's army all mark him as the seed of the Watchers' rebellion. David's "
                    "victory over Goliath is thus a typological act: the anointed of YHWH (mashiakh) defeats "
                    "the offspring of the rebel sons of God. This pattern — the anointed seed defeating "
                    "the serpent's seed — traces back to Genesis 3:15 and forward to Christ's victory "
                    "over the powers of darkness (Col 2:15; Heb 2:14-15)."
        },
        {
            "type": "theology",
            "title": "The Endor Necromancy — What Did Saul Really See?",
            "body": "The medium at Endor episode (1 Sam 28) is one of the most debated passages in the "
                    "Old Testament. Three main interpretations exist: (1) The traditional reading: Samuel "
                    "actually appeared — God permitted it as a final prophetic word of judgment on Saul. "
                    "This is supported by the text's straightforward narration and the accuracy of "
                    "Samuel's prophecy. (2) The demonic deception view: a demonic spirit impersonated "
                    "Samuel. This protects against the implication that necromancy 'works,' but conflicts "
                    "with the text's own language (the narrator calls the figure 'Samuel,' not 'a spirit' "
                    "or 'a demon'). (3) The divine exception view: YHWH sovereignly brought Samuel up as "
                    "an unrepeatable act of judgment, terrifying even the medium herself (28:12, she "
                    "screams when she sees him, suggesting this was not her normal experience). The most "
                    "significant detail is the medium's description: she sees 'an elohim coming up out "
                    "of the earth' (28:13). The word elohim here refers to a deceased human spirit — "
                    "confirming Michael Heiser's point that elohim is a 'place of residence' term (the "
                    "spiritual realm), not an ontological term meaning only 'God.' The dead are elohim "
                    "because they are now residents of the spiritual world."
        },
        {
            "type": "context",
            "title": "The Ark as YHWH's Throne — Divine Council Power",
            "body": "The Ark of the Covenant is not a magical box — it is YHWH's throne-footstool, the "
                    "meeting point between the heavenly and earthly realms. YHWH is described as 'enthroned "
                    "above the cherubim' (1 Sam 4:4; 2 Sam 6:2) — the cherubim on the Ark's cover "
                    "(kapporet) are the throne-guardians of the divine council, the same beings who "
                    "guard Eden's entrance (Gen 3:24) and surround YHWH's throne in Ezekiel 1 and 10. "
                    "When the Ark enters Dagon's temple, it is not two objects sharing space — it is two "
                    "thrones in one room, and only one can stand. YHWH's throne overpowers Dagon's. The "
                    "Philistines' decision to return the Ark with guilt offerings (gold tumors and gold "
                    "mice, 6:4-5) mirrors ancient Near Eastern practices of appeasing an offended deity "
                    "— they recognize the Ark's power as genuine divine power. The subsequent disaster "
                    "at Beth-Shemesh (6:19-21, the men struck down for looking into the Ark) reinforces "
                    "the lethal holiness of YHWH's presence — the divine council throne is not to be "
                    "treated casually by any human, Israelite or Philistine."
        },
        {
            "type": "scholarship",
            "title": "The Textual Problem of 1 Samuel",
            "body": "1 Samuel presents the most significant textual challenges of any Old Testament book. "
                    "The Masoretic Text has suffered notable corruption, and the Dead Sea Scrolls (especially "
                    "4QSam^a) have revolutionized our understanding of the book's textual history. Key "
                    "examples: (1) 1 Sam 10:27-11:1 — 4QSam^a preserves an entire paragraph about Nahash "
                    "the Ammonite gouging out the right eyes of the Gadites and Reubenites, which provides "
                    "essential context for chapter 11 and was lost from the MT. Josephus (Antiquities "
                    "6.68-71) knew this tradition. (2) Goliath's height — the MT gives 'six cubits and a "
                    "span' (~9.5 feet) while 4QSam^a and the LXX give 'four cubits and a span' (~6.5 feet). "
                    "Many scholars regard the shorter reading as original, with the MT inflated by "
                    "transmission. (3) 1 Sam 14:41 — the MT is garbled, but the LXX preserves the full "
                    "Urim and Thummim oracle procedure. These examples demonstrate why textual criticism "
                    "of 1 Samuel requires consulting the LXX and DSS alongside the MT."
        }
    ]
}
