"""
info.py — Judges (Shoftim): Scholarly Text Introduction

This file provides the "front page" for Judges in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Judges is the darkest book in the Former Prophets — a spiraling descent into
moral chaos, idolatry, and inter-tribal violence that demonstrates what happens
when Israel abandons YHWH and serves the territorial deities allotted to the
nations under the Deuteronomy 32 framework. The refrain "everyone did what was
right in his own eyes" (17:6; 21:25) is not merely a statement about social
disorder — it is a theological verdict: Israel has exchanged YHWH, the Most
High, for the gods of the surrounding nations, and the result is catastrophic.
"""

TEXT_INFO = {
    "text_id": "judges",
    "display_name": "Judges (Shoftim)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Former Prophets",
        "detail": "Judges is the second book of the Former Prophets (Nevi'im Rishonim) in the "
                  "Hebrew Bible and the seventh book of the Christian Old Testament. It is universally "
                  "recognized as canonical by Jewish, Catholic, Orthodox, and Protestant traditions. "
                  "In the Jewish ordering, Judges follows Joshua as the continuation of the prophetic "
                  "history, narrating the period between the conquest and the monarchy. The Talmud "
                  "(Bava Batra 14b-15a) attributes its authorship to Samuel. The book is quoted and "
                  "alluded to throughout the New Testament: Hebrews 11:32-34 celebrates the faith of "
                  "Gideon, Barak, Samson, and Jephthah; the Magnificat (Luke 1:46-55) echoes the Song "
                  "of Deborah (Judges 5); and Paul cites the period of the judges in his Antioch "
                  "sermon (Acts 13:20). The angel of YHWH, who appears repeatedly in Judges (2:1-4; "
                  "6:11-24; 13:2-23), was identified by patristic interpreters as a pre-incarnate "
                  "appearance of Christ. No mainstream tradition has ever questioned the canonical "
                  "status of Judges, though its graphic depictions of violence, apostasy, and moral "
                  "degradation have always required careful interpretive handling."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud (Bava Batra 14b-15a) states: 'Samuel wrote the book that bears "
                       "his name, Judges, and Ruth.' This attribution makes theological sense: Samuel "
                       "was the last judge and the prophet who anointed the first king, standing at "
                       "the hinge between the two eras. As the one who oversaw the transition from "
                       "judgeship to monarchy, Samuel would have had both the authority and the "
                       "perspective to compile the stories of the judges into a coherent theological "
                       "narrative. The repeated refrain 'In those days there was no king in Israel' "
                       "(17:6; 18:1; 19:1; 21:25) implies an author writing after the monarchy was "
                       "established — consistent with Samuel's timeframe. The detailed knowledge of "
                       "tribal territories, local sanctuaries, and regional traditions suggests access "
                       "to old sources close to the events described.",

        "scholarly_debate": "Modern scholarship places Judges within the Deuteronomistic History (DtrH), "
                           "the narrative arc from Deuteronomy through 2 Kings attributed by Martin Noth "
                           "(1943) to a single exilic author/editor. The cyclical framework of Judges "
                           "(apostasy -> oppression -> cry to YHWH -> deliverer raised -> rest -> "
                           "apostasy again) is understood as Deuteronomistic theological structuring of "
                           "older, independent hero traditions. The 'major judges' (Othniel, Ehud, Deborah, "
                           "Gideon, Jephthah, Samson) have full narrative cycles, while the 'minor judges' "
                           "(Shamgar, Tola, Jair, Ibzan, Elon, Abdon) appear in bare chronological notices. "
                           "Frank Moore Cross's double-redaction theory sees a pre-exilic edition (Dtr1) "
                           "under Josiah that emphasized covenant loyalty, and an exilic edition (Dtr2) "
                           "that added the hopeless tone of chapters 17-21. The Song of Deborah (Judges 5) "
                           "is widely regarded as one of the oldest pieces of Hebrew poetry in the Bible, "
                           "dating to the 12th-11th century BC on linguistic grounds. Scholars like Frank "
                           "Moore Cross and David Noel Freedman have demonstrated its archaic verbal forms, "
                           "orthography, and vocabulary are consistent with early Iron Age Hebrew.",

        "bottom_line": "The book contains genuinely ancient traditions — tribal hero stories, the Song of "
                       "Deborah, etiological narratives, and geographic details — that have been woven "
                       "into a Deuteronomistic theological framework. Whether Samuel compiled the first "
                       "edition or a later Deuteronomistic editor shaped the material, the source traditions "
                       "are rooted in the pre-monarchic period. The theological framework is not imposed "
                       "artificially but reflects the actual pattern of Israel's spiritual history during "
                       "this era: the 'gods of the peoples around them' (2:12) were real spiritual entities "
                       "in the Deuteronomy 32 worldview, and serving them had real consequences."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "~1380-1050 BC for the events described (from the death of Joshua to the rise "
                       "of Samuel), with the book composed by Samuel around ~1050-1020 BC. Judges 11:26 "
                       "states that Israel had occupied the Transjordan for 300 years by Jephthah's time, "
                       "which fits the early exodus chronology (~1446 BC).",
        "critical_range": "The events described span the Iron Age I period (~1200-1050 BC by the late "
                         "chronology). The final form of the book is typically dated to the exilic period "
                         "within the DtrH framework (~550 BC), with possible pre-exilic editions under "
                         "Josiah (~620 BC). However, the source traditions are much older: the Song of "
                         "Deborah (Judges 5) is dated by virtually all scholars to the 12th-11th century "
                         "BC, making it one of the oldest extended texts in the Hebrew Bible. The tribal "
                         "geography reflects pre-monarchic conditions, and the reference to the Jebusites "
                         "still holding Jerusalem (1:21) points to a pre-Davidic source.",
        "evidence": "Key evidence includes: (1) The Song of Deborah (Judges 5) contains archaic Hebrew "
                    "features — early verbal morphology, paleo-Hebrew spelling conventions, and vocabulary "
                    "parallels with Ugaritic — that place it in the 12th-11th century BC. (2) The tribal "
                    "roster in Judges 5 omits Judah, Simeon, Levi, Gad, and Manasseh (listing 'Machir' "
                    "instead), reflecting a pre-monarchic tribal configuration. (3) The Philistine presence "
                    "in the Samson narratives (chapters 13-16) fits the early 11th century BC, after the "
                    "Sea Peoples' settlement on the coastal plain (~1175 BC). (4) Archaeological evidence "
                    "from Iron Age I sites in the central highlands shows small, unwalled settlements with "
                    "four-room houses and collar-rim storage jars — consistent with the decentralized "
                    "tribal society described in Judges. (5) The Merneptah Stele (~1208 BC) confirms "
                    "Israel as an entity in Canaan during the period of the judges. (6) Dead Sea Scrolls "
                    "fragments of Judges (1QJudg, 4QJudg^a) date to ~50 BC-50 AD and generally align "
                    "with the Masoretic Text."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Israel — particularly the generation living under the early monarchy who "
                            "needed to understand why the pre-monarchic period was so chaotic and why "
                            "kingship was necessary (or, alternatively, why it was dangerous). The refrain "
                            "'there was no king in Israel' can be read as either pro-monarchic (things were "
                            "bad because there was no king) or anti-monarchic (things were bad, but a human "
                            "king is not the solution — YHWH is the true king). For the exilic audience of "
                            "the DtrH, Judges explained how the pattern of apostasy and judgment that "
                            "eventually led to exile was already present from the very beginning of life "
                            "in the land.",

        "purpose": "Judges demonstrates the catastrophic consequences of Israel serving the gods of the "
                   "nations — the territorial deities allotted under the Deuteronomy 32:8-9 framework. "
                   "Each cycle of apostasy involves Israel worshiping specific regional deities: the Baals "
                   "and Asheroth (2:13; 3:7), the gods of Aram, Sidon, Moab, Ammon, and the Philistines "
                   "(10:6). These are not fictional entities in the biblical worldview — they are the "
                   "'sons of God' (bene elohim) who were given authority over the nations at Babel and "
                   "who have corrupted their rule. When Israel serves them, Israel comes under their "
                   "authority and YHWH's protection is withdrawn. The judges are raised up not as permanent "
                   "rulers but as charismatic deliverers empowered by 'the Spirit of YHWH' (3:10; 6:34; "
                   "11:29; 13:25; 14:6, 19; 15:14) — a divine council bestowal that demonstrates YHWH's "
                   "continued sovereignty even during apostasy.",

        "theological_intent": "The book's structure is deliberately designed to show a downward spiral. "
                             "The first judge (Othniel) is a model deliverer; the last (Samson) is a "
                             "morally compromised figure who accomplishes YHWH's purposes almost accidentally. "
                             "The appendix (chapters 17-21) depicts the total collapse of Israelite society "
                             "into idolatry (the Danite migration and Micah's idol), sexual violence (the "
                             "Levite's concubine at Gibeah), and civil war (the near-extermination of "
                             "Benjamin). The Gibeah narrative deliberately echoes the Sodom story (Genesis 19), "
                             "signaling that Israel has become as corrupt as the nations YHWH judged. The "
                             "theological trajectory is clear: without faithful leadership and covenant "
                             "loyalty, Israel devolves into the very abominations that brought judgment "
                             "on the Canaanites."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "Judges contains some of the most linguistically diverse material in the "
                           "Hebrew Bible. The Song of Deborah (chapter 5) preserves archaic Hebrew with "
                           "features shared with Ugaritic: early verbal morphology, the use of the "
                           "independent pronoun as a copula, rare vocabulary (prazot for 'open villages,' "
                           "shagar for 'unleash'), and poetic parallelism that matches Late Bronze Age "
                           "Canaanite verse conventions. The prose narratives use standard Biblical Hebrew "
                           "narrative style (wayyiqtol chains) but include distinctive dialect markers: "
                           "the Gileadites' 'Shibboleth' test (12:5-6) is the earliest recorded example "
                           "of dialectal variation being used as a linguistic identifier. The Jotham fable "
                           "(9:7-15) is a rare example of ancient Israelite political satire in verse. "
                           "The Samson riddles (14:14, 18) represent wisdom-contest tradition. The "
                           "Deuteronomistic framework passages (2:6-3:6; the cycle introductions) use "
                           "the characteristic Dtr vocabulary: 'did evil in the eyes of YHWH,' 'served "
                           "the Baals,' 'the anger of YHWH burned against Israel.'",
        "grammar_match": "The linguistic register shifts dramatically between the archaic poetry of "
                        "Judges 5, the vivid narrative prose of the hero stories, the formulaic Dtr "
                        "framework, and the raw, disturbing narration of chapters 17-21. This diversity "
                        "reflects the book's composite origin: ancient oral traditions (the Song of "
                        "Deborah), tribal hero narratives (Ehud, Gideon, Jephthah, Samson), and editorial "
                        "framework (the cycle pattern) are woven together into a single theological "
                        "narrative. The terse, shocking prose of the Gibeah narrative (chapter 19) is "
                        "widely regarded as a masterpiece of biblical narrative art."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Judges IS scripture — the theological center of the Deuteronomistic History's "
                   "warning about covenant unfaithfulness and its consequences.",
        "nt_usage": "Hebrews 11:32-34 names four judges — Gideon, Barak, Samson, and Jephthah — among "
                    "the heroes of faith 'who through faith conquered kingdoms, administered justice, "
                    "and gained what was promised.' This is striking because three of these four are "
                    "deeply flawed characters, underscoring the Hebrews author's point that faith, not "
                    "moral perfection, is the key. Paul references the period of the judges in Acts "
                    "13:20: 'After this God gave them judges until the time of Samuel the prophet.' The "
                    "Magnificat (Luke 1:46-55) echoes the Song of Deborah (Judges 5), both celebrating "
                    "YHWH's reversal of power structures on behalf of the lowly. The angel of YHWH's "
                    "appearances in Judges (6:11-24; 13:2-23) were consistently identified by patristic "
                    "interpreters as Christophanies, particularly the appearance to Manoah and his wife "
                    "(13:18) where the angel declares his name 'Wonderful' (peli) — the same word used "
                    "in Isaiah 9:6 for the messianic child. James's warning against 'friendship with "
                    "the world' (James 4:4) echoes the Judges pattern of Israel's spiritual adultery.",
        "internal_consistency": "Judges picks up exactly where Joshua leaves off — the death of Joshua "
                               "(Judges 1:1; cf. Josh 24:29-31) and the incomplete conquest (Judges 1; "
                               "cf. Josh 13:1-7; 15:63; 16:10; 17:12-13). The theological framework of "
                               "Deuteronomy 7:1-5 (do not intermarry with the nations, do not serve their "
                               "gods) is systematically violated in Judges. The warning of Joshua 23:12-13 "
                               "(if you intermarry and serve their gods, they will become 'snares and traps "
                               "for you') is fulfilled in Judges 2:3. The Anakim remnant at Gaza, Gath, and "
                               "Ashdod (Josh 11:22) connects directly to the Philistine giant tradition that "
                               "will produce Goliath in 1 Samuel 17. The Danite migration (Judges 18) "
                               "explains the anomalous northern territory of Dan referenced in later texts."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: 1QJudg (1Q6) and 4QJudg^a (4Q49) and 4QJudg^b "
                    "(4Q50), dating to approximately 50 BC-50 AD. These fragments cover portions of "
                    "chapters 6, 8-12, and 19-21. The text generally aligns with the Masoretic tradition, "
                    "though with minor orthographic variations.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. The MT of Judges is generally well-preserved. "
                     "The most significant internal textual issue is the relationship between "
                     "the prose account of Deborah's victory (chapter 4) and the poetic account "
                     "(chapter 5), which differ in several details — evidence that both traditions "
                     "circulated independently before being placed side by side."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The LXX of Judges exists in two major recensions: the A-text (Codex "
                     "Alexandrinus) and the B-text (Codex Vaticanus), which differ significantly "
                     "from each other. The B-text is generally closer to the MT, while the A-text "
                     "shows a more expansive tradition. The relationship between these recensions "
                     "has been extensively studied by Walter Bodine and Natalio Fernández Marcos."},
            {"name": "Dead Sea Scrolls", "date": "~50 BC-50 AD",
             "note": "Three manuscripts preserve fragments of Judges. The text is generally "
                     "proto-Masoretic, supporting the stability of the Hebrew transmission."},
            {"name": "Targum Jonathan", "date": "1st-3rd century AD tradition",
             "note": "The Aramaic translation interprets theologically sensitive passages. At "
                     "Judges 5:4-5 (YHWH's march from Seir), the Targum softens the theophanic "
                     "imagery, and at 13:18, the angel's 'wonderful' name is rendered interpretively "
                     "to avoid direct identification with YHWH."}
        ],
        "reliability": "The text of Judges is well-attested across the major witnesses. The most "
                       "significant textual question is the dual-recension LXX tradition, which "
                       "suggests that the Greek text circulated in two distinct forms. However, the "
                       "theological content — the cycle of apostasy and deliverance, the divine "
                       "warrior narratives, the angel of YHWH appearances — is stable across all "
                       "witnesses. The Song of Deborah (chapter 5) is particularly well-preserved, "
                       "perhaps because its archaic language discouraged scribal modification."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Judges covers the Iron Age I period (~1200-1050 BC), one of the most turbulent "
                   "eras in ancient Near Eastern history. The Late Bronze Age Collapse (~1200-1150 BC) "
                   "destroyed the Hittite Empire, weakened Egypt's control over Canaan, disrupted "
                   "Mycenaean civilization, and brought the Sea Peoples (including the Philistines) to "
                   "the southern Levantine coast. Israel was a loose confederation of tribes in the "
                   "central highlands, without centralized government, standing army, or permanent "
                   "capital. The surrounding peoples — Moabites, Ammonites, Midianites, Amalekites, "
                   "Philistines — posed constant military threats. The Canaanite city-states continued "
                   "to exist in the lowlands and valleys (Judges 1:19, 27-35), and their religious "
                   "culture exerted constant pressure on Israelite worship.",

        "geography": "The judges operated in localized regions rather than over all Israel. Ehud "
                     "delivered Benjamin from Moab in the Jordan Valley. Deborah and Barak fought "
                     "in the Jezreel Valley against Hazor's coalition. Gideon operated in the hill "
                     "country of Manasseh against the Midianites who raided from the Transjordan. "
                     "Jephthah fought in Gilead against Ammon. Samson operated in the Shephelah "
                     "(lowland foothills) bordering Philistine territory. The Danite migration "
                     "(chapter 18) moved from the central coastal area to the far north at Laish "
                     "(later Dan). This geographic fragmentation reflects the pre-monarchic tribal "
                     "structure and the absence of centralized authority.",

        "historical_connections": "The Philistine oppression described in Judges 13-16 corresponds to "
                                 "the historical settlement of the Sea Peoples on the southern coastal "
                                 "plain after ~1175 BC. Archaeological evidence from Philistine sites "
                                 "(Ekron, Ashdod, Ashkelon, Gath, Gaza) shows Aegean-style pottery, "
                                 "architecture, and religious practices that distinguish them from "
                                 "indigenous Canaanites — consistent with the Bible's portrayal of them "
                                 "as foreign invaders. The Midianite camel-borne raids (Judges 6) "
                                 "represent one of the earliest references to the use of domesticated "
                                 "camels in warfare. The societal conditions described in Judges match "
                                 "the archaeological picture of Iron Age I: small, unwalled settlements, "
                                 "decentralized social organization, limited metallurgy (cf. 1 Sam 13:19-22), "
                                 "and a subsistence agricultural economy."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "major",
        "summary": "Judges is the Deuteronomy 32 worldview in action — the book demonstrates what "
                   "happens when Israel serves the territorial deities that YHWH allotted to the "
                   "nations. The 'gods' of the surrounding peoples are not dismissed as nonexistent "
                   "but treated as real spiritual entities whose worship brings Israel under their "
                   "corrupting authority and removes YHWH's protective presence."
                   "\n\n"
                   "The angel of YHWH (mal'akh YHWH) plays a central role in Judges as the visible "
                   "YHWH — the second power in heaven who mediates between the divine council and "
                   "Israel. Key appearances include: (1) Judges 2:1-4 — the angel ascends from Gilgal "
                   "to Bochim and pronounces covenant judgment, speaking in the first person as YHWH "
                   "('I brought you up out of Egypt... I said I will never break my covenant with you'). "
                   "This is not a created angel relaying a message — this is the visible YHWH "
                   "pronouncing judgment directly. (2) Judges 6:11-24 — the angel appears to Gideon "
                   "and is explicitly identified as YHWH (6:14, 'YHWH turned to him and said...'; "
                   "6:16, 'YHWH said to him, I will be with you'). When Gideon realizes he has seen "
                   "the angel of YHWH 'face to face,' he fears death (6:22-23) — because seeing YHWH "
                   "means death (Exod 33:20). (3) Judges 13:2-23 — the angel appears to Manoah's wife "
                   "and then to Manoah, announcing Samson's birth. The angel declares his name is 'Wonderful' "
                   "(peli, 13:18), ascends in the flame of the altar (13:20), and is identified as 'God' "
                   "(elohim, 13:22) by Manoah. This is the same 'Wonderful' of Isaiah 9:6."
                   "\n\n"
                   "The Anakim remnant is a critical thread connecting Judges to the Nephilim tradition. "
                   "Joshua 11:21-22 records that the Anakim were cut off from the hill country but "
                   "survived in Gaza, Gath, and Ashdod — Philistine cities. The Philistine giants "
                   "encountered later (Goliath of Gath in 1 Sam 17; the Rephaim warriors in 2 Sam "
                   "21:15-22) descend from this surviving Anakim population. The judges' wars against "
                   "the Philistines are thus part of the ongoing campaign against the Nephilim remnant "
                   "— the biological legacy of the Watchers' rebellion (Gen 6:1-4; 1 Enoch 6-16)."
                   "\n\n"
                   "The Spirit of YHWH (ruakh YHWH) that empowers the judges is a divine council gift: "
                   "the Spirit 'came upon' Othniel (3:10), 'clothed' Gideon (6:34, literally 'the Spirit "
                   "of YHWH wore Gideon like a garment'), 'rushed upon' Jephthah (11:29), and repeatedly "
                   "'rushed upon' Samson (13:25; 14:6, 19; 15:14). This empowerment comes from the "
                   "heavenly council and is task-specific: it is given for deliverance, not for ongoing "
                   "governance. When the Spirit departs, the judge's power departs (cf. Samson in 16:20, "
                   "'He did not know that YHWH had departed from him').",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 17-18 (territorial spirits and the conquest/judges period)",
            "The Unseen Realm, chapter 13-16 (Deuteronomy 32 worldview — the gods of the nations)",
            "Supernatural, chapter 15 (the gods Israel served in Judges)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 7-8 (the angel of YHWH in Judges)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 4-5 (Nephilim remnant and the Philistine giants)",
            "The Naked Bible Podcast, episodes 103-108 (Judges and the divine council)",
            "The Naked Bible Podcast, episode 120 (the angel of YHWH as the visible YHWH)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "The Cycle of Apostasy and the Gods of the Nations",
            "body": "The cyclical pattern of Judges (apostasy -> oppression -> cry -> deliverance -> "
                    "rest -> apostasy) is not merely a literary device — it reflects the Deuteronomy 32 "
                    "worldview in which the gods of the nations are real spiritual beings who actively "
                    "compete for Israel's worship. Each cycle names specific deities: the Baals (the "
                    "storm god of Canaan, equivalent to Hadad), the Asheroth (the consort goddess), "
                    "the gods of Aram, Sidon, Moab, Ammon, and the Philistines (10:6). When Israel "
                    "serves these gods, they come under the spiritual authority of the nations those "
                    "gods rule — which is why the oppressors correspond to the gods served. The cycle "
                    "is a lived-out demonstration of the choice Joshua presented at Shechem: 'Choose "
                    "this day whom you will serve' (Josh 24:15). Israel chose the gods of the nations, "
                    "and the nations' power over them was the consequence."
        },
        {
            "type": "interpretation",
            "title": "The Angel of YHWH — The Visible God of Judges",
            "body": "The angel of YHWH in Judges is the most theologically significant figure in the "
                    "book. In each appearance, the text oscillates between calling him 'the angel of "
                    "YHWH' and simply 'YHWH' — the same pattern seen in the burning bush (Exod 3) and "
                    "the Hagar encounter (Gen 16). This is the 'two YHWHs' phenomenon identified by "
                    "Michael Heiser and the early church fathers: the invisible YHWH (the Father) and "
                    "the visible YHWH (the Word/Son) are both fully YHWH but personally distinct. The "
                    "angel's self-identification as 'Wonderful' (peli) in Judges 13:18 connects directly "
                    "to the messianic prophecy of Isaiah 9:6 ('His name shall be called Wonderful'). "
                    "Manoah's fear of death upon seeing this figure (13:22) confirms that this is a "
                    "genuine theophany — an encounter with YHWH himself — not merely an angelic messenger."
        },
        {
            "type": "theology",
            "title": "The Downward Spiral — Israel Becomes Like Sodom",
            "body": "Judges is deliberately structured to show progressive moral deterioration. The early "
                    "judges (Othniel, Ehud) are presented positively. The middle judges show increasing "
                    "ambiguity: Gideon destroys the Baal altar but makes an ephod that becomes an idol "
                    "(8:27); Jephthah makes a rash vow with devastating consequences (11:30-40). Samson "
                    "is empowered by the Spirit but driven by lust and vengeance. The appendix (chapters "
                    "17-21) presents total societal collapse: the Danite idolatry narrative and the Gibeah "
                    "atrocity. The Gibeah story (chapter 19) deliberately echoes Sodom (Genesis 19) — the "
                    "same mob violence, the same sexual depravity, the same offering of women to the crowd. "
                    "The theological message is devastating: Israel, the covenant people chosen to replace "
                    "the corrupt nations, has become indistinguishable from Sodom. The very sins that "
                    "brought divine judgment on Canaan are now being committed by Israel in Canaan. This "
                    "is the ultimate indictment of serving the gods of the nations — you become like them."
        },
        {
            "type": "scholarship",
            "title": "The Song of Deborah — Earliest Hebrew Poetry",
            "body": "Judges 5, the Song of Deborah, is widely regarded as one of the oldest extended "
                    "texts in the Hebrew Bible. Its archaic linguistic features, divine warrior imagery, "
                    "and theophanic language make it a critical text for understanding early Israelite "
                    "theology. The song opens with a theophany: 'YHWH, when you went out from Seir, "
                    "when you marched from the region of Edom, the earth trembled and the heavens "
                    "dropped, yes, the clouds dropped water. The mountains quaked before YHWH, even "
                    "Sinai, before YHWH, the God of Israel' (5:4-5). This is divine council language: "
                    "YHWH marches from his mountain sanctuary with his heavenly army. The stars fight "
                    "from heaven (5:20) — the astral host as YHWH's cosmic warriors. The cursing of "
                    "Meroz (5:23, 'Curse Meroz, said the angel of YHWH') suggests a town that refused "
                    "to join YHWH's holy war, cursed by a divine council decree."
        }
    ]
}
