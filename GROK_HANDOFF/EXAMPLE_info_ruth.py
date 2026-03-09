"""
info.py — Ruth: Scholarly Text Introduction

This file provides the "front page" for Ruth in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Ruth is a masterpiece of narrative theology — a four-chapter story that
carries the weight of the entire messianic lineage. Set during the period
of the judges, it stands in deliberate contrast to the moral chaos of that
era: where Judges ends with rape, idolatry, and civil war, Ruth presents
covenant loyalty (hesed), kinsman-redemption (go'el), and the quiet
providence of YHWH working through ordinary faithfulness. The book's
placement in the canon — between Judges and Samuel in the LXX/Christian
ordering, or among the Writings (Ketuvim) in the Hebrew Bible — reflects
its dual function as both a historical bridge and a theological gem.
"""

TEXT_INFO = {
    "text_id": "ruth",
    "display_name": "Ruth",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim) or Historical Books",
        "detail": "Ruth is universally recognized as canonical by Jewish, Catholic, Orthodox, and "
                  "Protestant traditions. In the Hebrew Bible, Ruth is placed among the Writings "
                  "(Ketuvim), specifically in the Five Megillot (Scrolls), and is read liturgically "
                  "during the Feast of Weeks (Shavuot) because of its harvest setting and its "
                  "connection to the giving of the Torah (Ruth's acceptance of YHWH parallels "
                  "Israel's acceptance of the covenant). In the Septuagint and Christian Old Testament, "
                  "Ruth is placed after Judges and before 1 Samuel, creating a chronological sequence "
                  "that highlights its setting 'in the days when the judges ruled' (1:1). The Talmud "
                  "(Bava Batra 14b-15a) attributes its authorship to Samuel. Ruth is cited in the "
                  "New Testament in the genealogy of Jesus (Matthew 1:5), where Ruth the Moabitess "
                  "appears as one of four women named in the lineage of Christ — alongside Tamar, "
                  "Rahab, and Bathsheba ('the wife of Uriah') — each of whom represents an unexpected "
                  "or scandalous element in the messianic line. No tradition has ever questioned "
                  "Ruth's canonical status."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud (Bava Batra 14b-15a) attributes Ruth to Samuel, which is plausible "
                       "given that the book culminates in the genealogy of David (4:17-22) and Samuel "
                       "was the prophet who anointed David. Samuel would have had both the knowledge "
                       "and the theological motivation to record the origins of the Davidic line. The "
                       "intimate knowledge of Bethlehem's customs, the legal proceedings at the city "
                       "gate, and the details of the harvest suggest familiarity with Judahite culture "
                       "and traditions. The mention of the 'former custom in Israel' regarding sandal "
                       "removal (4:7) implies the author writes from a time when this practice was "
                       "no longer current, consistent with a monarchic-era perspective.",

        "scholarly_debate": "Critical scholarship is divided on dating. Some scholars (Edward Campbell, "
                           "Robert Hubbard) argue for a pre-exilic date, noting the book's familiarity "
                           "with harvest customs, legal procedures, and the absence of late linguistic "
                           "features. Others (Jack Sasson) argue for a post-exilic date, suggesting Ruth "
                           "was composed as a counter-narrative to Ezra-Nehemiah's prohibition of foreign "
                           "marriages — showing that David's own great-grandmother was a Moabitess. The "
                           "linguistic evidence is ambiguous: the Hebrew of Ruth is elegant and relatively "
                           "simple, without clearly late features, but the explanatory note about the "
                           "sandal custom (4:7) suggests some historical distance from the events. A "
                           "growing consensus favors a monarchic composition (10th-8th century BC) that "
                           "may have been lightly edited in the post-exilic period.",

        "bottom_line": "Ruth was likely composed during the early monarchy, possibly by Samuel or a "
                       "court scribe with access to Davidic family traditions. The genealogical "
                       "conclusion (4:17-22) — which traces the line from Perez to David — indicates "
                       "that the Davidic connection is the book's raison d'etre. Whether pre-exilic or "
                       "post-exilic in final form, the story preserves authentic pre-monarchic customs "
                       "and legal practices that an author could not have invented from a later period."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events are set 'in the days when the judges ruled' (1:1), placing the "
                       "narrative in the period ~1200-1050 BC. The composition is attributed to "
                       "Samuel (~1050-1020 BC), writing to establish David's lineage.",
        "critical_range": "The events are set during the judges period (Iron Age I, ~1200-1050 BC). "
                         "Composition dates range widely: (1) Pre-exilic, possibly as early as the "
                         "10th century BC (the Solomonic 'enlightenment' when court scribes allegedly "
                         "compiled wisdom literature and historical narratives); (2) 8th-7th century BC "
                         "(pre-exilic but after the customs required explanation); (3) Post-exilic, "
                         "5th-4th century BC (as a response to the Ezra-Nehemiah marriage reforms). "
                         "The genealogy ending at David (not Solomon or later) argues against a very "
                         "late date.",
        "evidence": "Key evidence includes: (1) The explanatory note about the sandal custom (4:7) "
                    "implies historical distance from the events, ruling out a composition during the "
                    "judges period itself. (2) The legal procedure at the city gate (4:1-12) reflects "
                    "authentic ancient Israelite jurisprudence paralleled in Deuteronomy 25:5-10 "
                    "(levirate marriage) and attested in ancient Near Eastern texts. (3) The genealogy "
                    "of David (4:17-22) terminates at David, not Solomon, suggesting composition before "
                    "the divided monarchy or deliberate focus on David's origins. (4) The Hebrew style "
                    "is polished, narrative prose without clearly late features. (5) Ruth is not found "
                    "among the Dead Sea Scrolls (no fragments have been identified from Qumran), which "
                    "is not necessarily significant given the fragmentary survival of the scrolls, but "
                    "it means we lack the earliest manuscript evidence available for other books. "
                    "(6) The Moabite setting connects to known archaeological data about Moab in the "
                    "Iron Age I period."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Israel — particularly those interested in the origins of the Davidic "
                            "dynasty and the theology of YHWH's providential care for the faithful. "
                            "The book would have been especially meaningful to audiences familiar with "
                            "the period of the judges: against the backdrop of national apostasy and "
                            "moral collapse, Ruth demonstrates that YHWH's covenant purposes continued "
                            "to advance through individual faithfulness. For the post-exilic community, "
                            "Ruth affirmed that YHWH's grace extended to non-Israelites who embraced "
                            "the covenant — a message with profound implications for the inclusion of "
                            "Gentiles in the people of God.",

        "purpose": "Ruth serves multiple theological purposes simultaneously: (1) It establishes the "
                   "Davidic genealogy, tracing David's ancestry through Boaz and Ruth to Perez (the "
                   "son of Judah and Tamar), grounding the messianic line in both Judahite ancestry "
                   "and Moabite inclusion. (2) It illustrates the go'el (kinsman-redeemer) institution, "
                   "which becomes the primary biblical metaphor for YHWH's redemptive work and, "
                   "ultimately, for Christ's redemptive role. (3) It demonstrates hesed (covenant "
                   "loyalty, faithful love) as the defining virtue of the covenant community — Boaz, "
                   "Ruth, and Naomi all exhibit hesed in ways that contrast sharply with the moral "
                   "chaos of Judges. (4) It affirms YHWH's providence: the 'coincidence' of Ruth "
                   "gleaning in Boaz's field (2:3) is a narrative signal that YHWH orchestrates "
                   "events without visible supernatural intervention.",

        "theological_intent": "The go'el theology of Ruth is one of the richest typological veins in "
                             "the Old Testament. The kinsman-redeemer (go'el) must be a blood relative "
                             "who has the right, the resources, and the willingness to redeem. Boaz "
                             "fulfills all three: he is of the clan of Elimelech (right), he is a "
                             "'worthy man' (ish gibbor hayil, 2:1) with means (resources), and he "
                             "chooses to redeem despite the cost (willingness). The nearer kinsman who "
                             "declines (4:6) highlights that redemption requires not just legal standing "
                             "but personal commitment. This points directly to Christ: fully human (blood "
                             "relative of humanity through the incarnation), infinitely resourceful "
                             "(divine power), and willing to bear the cost of redemption (the cross). "
                             "The threshing floor scene (chapter 3), where Ruth 'uncovers his feet' and "
                             "lies at Boaz's feet, is loaded with covenant symbolism: the spreading of "
                             "the garment (3:9, 'spread your wings over your servant') echoes YHWH's "
                             "covenant with Israel (Ezek 16:8) and Ruth's own words about coming under "
                             "YHWH's 'wings' (2:12)."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "Ruth's Hebrew is among the most elegant prose in the Bible — polished, "
                           "restrained, and rich in wordplay. The narrative uses a limited vocabulary "
                           "with great precision, creating meaning through repetition and variation: "
                           "the root g-'-l (redeem) appears 23 times, shuv (return) 12 times, and "
                           "hesed (covenant loyalty) at key structural points (1:8; 2:20; 3:10). "
                           "Ruth's famous declaration (1:16-17) is a masterpiece of Hebrew rhetoric: "
                           "seven parallel clauses building to a covenant oath. The legal language at "
                           "the city gate (4:1-12) uses precise technical terminology: go'el (kinsman-"
                           "redeemer), qanah (acquire/purchase), and the symbolic shoe removal "
                           "(halitzah) ceremony. The name 'Ruth' (rut) may derive from the root r-w-h "
                           "(to water, to saturate) or from re'ut (friendship/companionship). 'Boaz' "
                           "(bo'az) means 'in him is strength,' and 'Naomi' means 'pleasant' — her "
                           "name-change to 'Mara' (bitter, 1:20) marks the narrative's emotional nadir.",
        "grammar_match": "Ruth's prose style is characterized by dialogue-heavy narration with minimal "
                        "authorial commentary. The narrator rarely tells the reader what to think; "
                        "instead, meaning emerges from the characters' words and actions. The "
                        "wayyiqtol narrative chain is used sparingly compared to other biblical "
                        "narratives, giving Ruth a slower, more contemplative pace. The book's "
                        "linguistic features are consistent with classical Biblical Hebrew (10th-8th "
                        "century BC) without the late features (Aramaisms, Persian loanwords) that "
                        "characterize post-exilic texts, though this is debated."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Ruth IS scripture — a genealogical and theological foundation stone of the "
                   "messianic line, placed by providence at the hinge between the judges and the "
                   "monarchy.",
        "nt_usage": "Ruth appears in the genealogy of Jesus in Matthew 1:5: 'Boaz fathered Obed by "
                    "Ruth, and Obed fathered Jesse, and Jesse fathered David the king.' Ruth is one "
                    "of four women named in Matthew's genealogy — alongside Tamar (Gen 38), Rahab "
                    "(Josh 2), and Bathsheba (2 Sam 11) — each representing an unexpected, scandalous, "
                    "or non-Israelite element in the messianic line. The theological point is profound: "
                    "the Messiah's ancestry includes a Canaanite prostitute, a Moabitess, and an "
                    "adulteress, demonstrating that God's redemptive purposes transcend ethnic boundaries "
                    "and human moral failure. The go'el typology of Ruth is fulfilled in Christ, who is "
                    "called the Redeemer (lutron/lutrosis in Mark 10:45; Luke 1:68; 2:38; Heb 9:12). "
                    "Paul's teaching that Christ has 'redeemed' (exagorazo) believers from the curse of "
                    "the law (Gal 3:13; 4:5) draws on the same kinsman-redeemer concept.",
        "internal_consistency": "Ruth connects seamlessly to the broader biblical narrative. The Moabite "
                               "origin of Ruth links to Genesis 19:30-38 (Moab descended from Lot through "
                               "incest after Sodom's destruction) — yet from this ignoble origin, YHWH "
                               "brings forth the Davidic line. The Perez genealogy (4:18-22) connects to "
                               "Genesis 38 (Judah and Tamar), creating a pattern of unlikely and scandal-"
                               "marked ancestors in the messianic line. The levirate marriage customs "
                               "correspond to Deuteronomy 25:5-10. The harvest setting connects to the "
                               "gleaning laws of Leviticus 19:9-10 and 23:22, which Ruth exploits. The "
                               "Davidic genealogy at the conclusion bridges directly to 1 Samuel's account "
                               "of David's rise."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "No Dead Sea Scrolls fragments of Ruth have been positively identified, making the "
                    "earliest witnesses the Septuagint (LXX) translation (3rd-2nd century BC) and the "
                    "Masoretic Text tradition. The absence from Qumran is likely accidental — the book "
                    "is short (only 85 verses) and the survival of specific scrolls is random.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. Ruth's MT is well-preserved with minimal textual "
                     "difficulties. The most significant textual question is the Qere-Ketiv at 3:3-4 "
                     "and 3:15 (masculine/feminine pronoun variations that may reflect dialectal or "
                     "scribal differences). The text is remarkably stable."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The Greek Ruth closely follows the Hebrew, with minor expansions for clarity. "
                     "The LXX places Ruth after Judges, creating the chronological sequence that "
                     "most Christian Bibles follow. The translation is literal and straightforward, "
                     "indicating a Hebrew Vorlage very close to the MT."},
            {"name": "Targum Ruth", "date": "Variable, 1st-7th century AD traditions",
             "note": "The Aramaic Targum of Ruth is highly expansive, adding extensive midrashic "
                     "material. It identifies Boaz as a judge and adds theological explanations "
                     "throughout, reflecting later Jewish interpretive traditions."},
            {"name": "Syriac Peshitta", "date": "2nd-3rd century AD",
             "note": "The Syriac translation follows the Hebrew closely with minor interpretive "
                     "adjustments. It supports the MT text tradition."}
        ],
        "reliability": "The text of Ruth is exceptionally well-preserved. There are virtually no "
                       "significant textual variants that affect the meaning of the book. The main "
                       "textual discussions involve minor pronoun variations and the exact reading of "
                       "some proper names. The theological content — the go'el redemption, the hesed "
                       "theme, and the Davidic genealogy — is completely stable across all witnesses."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Ruth is set 'in the days when the judges ruled' (1:1), placing it in the Iron Age I "
                   "period (~1200-1050 BC) in the town of Bethlehem in Judah and in the country of Moab "
                   "(modern-day Jordan, east of the Dead Sea). The famine that drives Elimelech's family "
                   "to Moab is consistent with the recurring agricultural crises of this period, when "
                   "the semi-arid climate of the Judean highlands made subsistence farming precarious. "
                   "Bethlehem ('House of Bread') is ironically empty of bread, forcing the family to "
                   "seek sustenance in Moab — a nation with whom Israel had a complex and often hostile "
                   "relationship (cf. Judges 3:12-30, the Moabite oppression under Eglon).",

        "geography": "The story moves between two locations: Moab (the high plateau east of the Dead Sea, "
                     "modern Jordan) and Bethlehem (a small agricultural town ~8 km south of Jerusalem in "
                     "the Judean hill country). The 'road back from the country of Moab' (1:7) would have "
                     "descended from the Moabite plateau, crossed the Jordan near Jericho, and climbed "
                     "westward into the Judean hills to Bethlehem. The harvest scenes (chapters 2-3) take "
                     "place in the fields and threshing floors around Bethlehem — the same area where "
                     "David would later tend sheep (1 Sam 16:11) and where, a millennium later, Jesus "
                     "would be born (Luke 2:4-7).",

        "historical_connections": "The Moabite connection is theologically loaded. Moab was descended from "
                                 "Lot through his incestuous encounter with his elder daughter after the "
                                 "destruction of Sodom (Gen 19:30-37). Deuteronomy 23:3-6 prohibits "
                                 "Moabites from entering 'the assembly of YHWH' for ten generations. "
                                 "Yet Ruth the Moabitess not only enters the assembly but becomes the "
                                 "great-grandmother of David and an ancestor of the Messiah. This tension "
                                 "between legal exclusion and gracious inclusion is central to the book's "
                                 "theology. The Mesha Stele (Moabite Stone, ~840 BC) provides the most "
                                 "detailed extra-biblical account of Moabite culture and religion, including "
                                 "the worship of Chemosh — the national deity of Moab (cf. 1 Kings 11:7, 33). "
                                 "Ruth's declaration 'your God will be my God' (1:16) represents a conscious "
                                 "rejection of Chemosh in favor of YHWH."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "moderate",
        "summary": "Ruth's divine council connections are subtle but theologically profound. The book "
                   "operates in the register of providence rather than theophany — YHWH works behind "
                   "the scenes through human faithfulness rather than through visible supernatural "
                   "intervention. But the divine council framework illuminates the story at several "
                   "key points."
                   "\n\n"
                   "The go'el (kinsman-redeemer) concept is the book's primary contribution to divine "
                   "council theology. In the Hebrew Bible, YHWH himself is called Israel's Go'el "
                   "(Exod 6:6; 15:13; Isa 41:14; 43:14; 44:6, 24; 47:4; 48:17; 49:7, 26; 54:5, 8; "
                   "59:20; 60:16; 63:16). The go'el must be a kinsman who has the right to redeem, "
                   "the power to redeem, and the will to redeem. Boaz fulfills all three qualifications, "
                   "making him a type of the ultimate Go'el — the divine-human Redeemer who is both "
                   "kinsman (through incarnation) and God (with infinite power to redeem). This typology "
                   "is foundational to the New Testament's atonement theology."
                   "\n\n"
                   "The Moabite dimension connects to the Deuteronomy 32 worldview: Moab was allotted "
                   "to Chemosh (cf. Judges 11:24, where Jephthah acknowledges Chemosh as Moab's god; "
                   "1 Kings 11:7, 33 where Solomon builds high places for Chemosh). Ruth's conversion "
                   "— 'your people shall be my people, and your God my God' (1:16) — is a territorial "
                   "transfer: she leaves the spiritual jurisdiction of Chemosh and places herself under "
                   "YHWH's authority. In the Deuteronomy 32 framework, this is an act of cosmic "
                   "defection from one divine patron to another. It anticipates the eschatological "
                   "ingathering of the nations prophesied in Isaiah 2:2-4, Psalm 87, and ultimately "
                   "fulfilled in the Great Commission (Matt 28:18-20)."
                   "\n\n"
                   "The city gate proceedings (4:1-12) have divine council echoes. The gate was the "
                   "place of legal judgment in ancient Israel, and the elders who sit there function "
                   "as an earthly mirror of the divine council: they witness, adjudicate, and pronounce "
                   "binding decisions. The blessing they pronounce over Ruth (4:11-12) — invoking Rachel, "
                   "Leah, and the house of Perez — is a prophetic declaration that connects Ruth's "
                   "story to the foundational promises of Israel's history. The Davidic genealogy that "
                   "closes the book (4:17-22) places Ruth's story in the messianic trajectory that "
                   "culminates in the 'Son of David' who will rule as YHWH's viceroy on earth — the "
                   "human member of the divine council who sits at YHWH's right hand (Psalm 110:1).",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 24 (the kinsman-redeemer and the Messiah)",
            "The Unseen Realm, chapter 13-16 (Deuteronomy 32 worldview — Chemosh and the allotted gods)",
            "Supernatural, chapter 19 (Gentile inclusion in the messianic program)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 3 (the divine council and earthly mirrors)",
            "The Naked Bible Podcast, episode 132 (Ruth and the go'el typology)",
            "The Naked Bible Podcast, episode 47 (Deuteronomy 32 and the gods of the nations)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Go'el — From Boaz to Christ",
            "body": "The kinsman-redeemer (go'el) institution is the theological heart of Ruth and one "
                    "of the most important typological connections in the Old Testament. The go'el had "
                    "specific legal responsibilities: (1) redeem a relative's property that had been "
                    "sold due to poverty (Lev 25:25); (2) redeem a relative from debt-slavery (Lev "
                    "25:47-49); (3) avenge the blood of a murdered relative (Num 35:19-21); (4) marry "
                    "a deceased relative's widow to preserve the family line (Deut 25:5-10, the levirate "
                    "obligation, which Boaz extends through the go'el institution). In Ruth, Boaz "
                    "redeems Naomi's land, takes Ruth as his wife, and raises up an heir (Obed) for "
                    "the dead. This three-fold redemption — property, person, and progeny — prefigures "
                    "Christ's comprehensive redemption: he redeems the inheritance (the land/creation), "
                    "the person (from the slavery of sin), and secures eternal progeny (the children "
                    "of God). The anonymous nearer kinsman who refuses to redeem (4:6) represents the "
                    "law — it has the right but not the willingness or the capacity to fully redeem. "
                    "Only the willing, able kinsman can accomplish redemption."
        },
        {
            "type": "context",
            "title": "Ruth the Moabitess — Grace Beyond the Law",
            "body": "Deuteronomy 23:3 states: 'No Ammonite or Moabite may enter the assembly of YHWH. "
                    "Even to the tenth generation, none of them may enter the assembly of YHWH forever.' "
                    "Yet Ruth the Moabitess not only enters the assembly but becomes the great-grandmother "
                    "of David and an ancestor of Jesus. How is this reconciled? Several explanations have "
                    "been offered: (1) Rabbinic tradition (Talmud Yevamot 76b) argues the prohibition "
                    "applied only to Moabite men, not women. (2) Ruth's conversion ('your God will be "
                    "my God') effectively transfers her from Moabite to Israelite status. (3) The "
                    "prohibition refers to national/political membership, not individual inclusion "
                    "through marriage and conversion. (4) YHWH's sovereign grace overrides the legal "
                    "restriction — the same grace that includes Rahab the Canaanite and Tamar the "
                    "daughter-in-law of Judah in the messianic line. In the divine council framework, "
                    "Ruth's inclusion signals that YHWH's redemptive plan ultimately transcends the "
                    "national allotment of Deuteronomy 32 — the nations allotted to other gods will "
                    "eventually be reclaimed through the Messiah."
        },
        {
            "type": "interpretation",
            "title": "The Threshing Floor — Covenant, Not Scandal",
            "body": "The threshing floor scene (Ruth 3) is one of the most debated passages in the "
                    "book. Naomi instructs Ruth to wash, anoint, and dress, then go to the threshing "
                    "floor at night, uncover Boaz's 'feet,' and lie down. The Hebrew word for 'feet' "
                    "(margelot) is sometimes used as a euphemism (cf. Isa 7:20; Judges 3:24), leading "
                    "some to read sexual overtones. However, the narrative is better understood as a "
                    "covenant proposal: Ruth asks Boaz to 'spread your wing (kanaf) over your servant' "
                    "(3:9) — the same language used for YHWH's covenant protection in Ezekiel 16:8 and "
                    "Ruth 2:12. The threshing floor was also a place of legal and religious significance "
                    "in Israel (cf. 2 Sam 24:18-25, the threshing floor of Araunah where the Temple "
                    "would be built). Ruth is not seducing Boaz; she is invoking her legal right to "
                    "redemption and asking Boaz to act as go'el. Boaz's response — 'you have not gone "
                    "after young men, whether poor or rich' (3:10) — confirms that her action is "
                    "understood as hesed (covenant loyalty), not impropriety."
        },
        {
            "type": "scholarship",
            "title": "The Davidic Genealogy and Messianic Purpose",
            "body": "The genealogy of Ruth 4:17-22 — Perez, Hezron, Ram, Amminadab, Nahshon, Salmon, "
                    "Boaz, Obed, Jesse, David — is not an afterthought but the theological destination "
                    "of the entire narrative. Everything in Ruth leads to David: the famine, the "
                    "journey to Moab, Ruth's loyalty, Boaz's redemption, and the birth of Obed all "
                    "serve YHWH's purpose of establishing the Davidic line through which the Messiah "
                    "will come. The genealogy connects to Genesis 38 (Perez, son of Judah and Tamar) "
                    "at the beginning and to Matthew 1:1-17 at the end. The pattern of unexpected, "
                    "scandal-marked, and non-Israelite women in the messianic line — Tamar (Canaanite, "
                    "disguised as a prostitute), Rahab (Canaanite prostitute), Ruth (Moabitess), "
                    "Bathsheba (taken in adultery) — declares that YHWH's redemptive purposes work "
                    "through human brokenness and across ethnic boundaries. The Messiah's genealogy "
                    "is itself a gospel: no ancestry is too compromised, no origin too foreign, for "
                    "YHWH's grace to transform into the lineage of the King of kings."
        }
    ]
}
