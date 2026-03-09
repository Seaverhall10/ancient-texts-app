"""
info.py — Joshua (Yehoshua): Scholarly Text Introduction

This file provides the "front page" for Joshua in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Joshua is the bridge between the Torah and the Deuteronomistic History — the
book where the promises made to Abraham, renewed at Sinai, and reaffirmed on
the plains of Moab are finally (and partially) fulfilled. The conquest narrative
is drenched in divine warrior theology, divine council imagery, and the cosmic
implications of YHWH reclaiming territory from rival spiritual powers.
"""

TEXT_INFO = {
    "text_id": "joshua",
    "display_name": "Joshua (Yehoshua)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Former Prophets",
        "detail": "Joshua is the first book of the Former Prophets (Nevi'im Rishonim) in the "
                  "Hebrew Bible and the sixth book of the Christian Old Testament. It is universally "
                  "recognized as canonical by Jewish, Catholic, Orthodox, and Protestant traditions. "
                  "In the Jewish ordering, Joshua stands immediately after Deuteronomy as the opening "
                  "of the prophetic corpus, signaling that the conquest narrative is understood not "
                  "merely as history but as prophetic theology -- a declaration of what YHWH has done "
                  "and will do. The Talmud (Bava Batra 14b-15a) lists Joshua among the prophetic "
                  "writings and attributes its authorship to Joshua himself. The book is quoted or "
                  "alluded to throughout the Old and New Testaments: the fall of Jericho appears in "
                  "Hebrews 11:30, Rahab's faith is celebrated in Hebrews 11:31 and James 2:25, and "
                  "the concept of 'rest' (menukhah) that Joshua inaugurates becomes a central "
                  "theological category in Hebrews 3-4. Stephen's speech in Acts 7:45 references "
                  "Joshua bringing the tabernacle into the land. No mainstream tradition has ever "
                  "questioned Joshua's canonical status, though its ethical content -- particularly "
                  "the herem (devoted destruction) passages -- has generated intense theological "
                  "discussion from antiquity to the present."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Joshua son of Nun, Moses' successor and the commander of the conquest, as "
                       "affirmed by the Talmud (Bava Batra 14b-15a), which states: 'Joshua wrote "
                       "the book that bears his name and the last eight verses of the Torah' "
                       "(describing Moses' death). The book itself records Joshua writing in 'the "
                       "Book of the Law of God' (Josh 24:26) and contains first-person elements that "
                       "suggest eyewitness authorship (Josh 5:1, 'until we had crossed over,' in some "
                       "manuscripts). The narrative perspective of one who participated in the events "
                       "is evident throughout: detailed knowledge of military tactics, geographic "
                       "precision, and the emotional intensity of the Jericho and Ai accounts. The "
                       "Talmud notes that the account of Joshua's death (24:29-33) was written by "
                       "Eleazar the priest, and the notice of Eleazar's death (24:33) was written by "
                       "Phinehas. This chain of authorship connects the book directly to the "
                       "generation of the conquest.",

        "scholarly_debate": "Modern scholarship generally places Joshua within the Deuteronomistic "
                           "History (DtrH), the narrative arc from Deuteronomy through 2 Kings that "
                           "Martin Noth (1943) proposed was composed by a single author/editor (the "
                           "'Deuteronomist') during the exile (~550 BC). Noth argued that the "
                           "Deuteronomist used older sources -- conquest traditions, boundary lists, "
                           "city catalogues, and etiological narratives -- to construct a theological "
                           "history explaining why Israel lost the land. Frank Moore Cross (1973) "
                           "proposed a double redaction: a pre-exilic edition (Dtr1) during Josiah's "
                           "reign (~620 BC) that was optimistic about covenant renewal, and an exilic "
                           "edition (Dtr2) that added the themes of judgment and loss. Richard Nelson "
                           "and Thomas Romer have further refined these models. Conservative scholars "
                           "(Kenneth Kitchen, Richard Hess, David Howard) argue that the book's "
                           "geographic and administrative details reflect Late Bronze Age or early "
                           "Iron Age conditions rather than later editorial invention. The boundary "
                           "lists in Joshua 13-21 match known Late Bronze Age settlement patterns, "
                           "and the city lists include sites that were destroyed or abandoned before "
                           "the monarchy. The debate centers on whether Joshua is a substantially "
                           "contemporary account edited into the DtrH framework, or a largely late "
                           "composition using fragmentary earlier traditions.",

        "bottom_line": "The book contains a core of authentic conquest-era traditions -- military "
                       "narratives, geographic knowledge, and administrative lists -- that are best "
                       "explained by proximity to the events described. Whether Joshua son of Nun "
                       "wrote the bulk of the text or an early editor compiled eyewitness sources "
                       "shortly after the conquest, the material has deep roots in the Late Bronze "
                       "Age / early Iron Age transition. The Deuteronomistic framework (particularly "
                       "the theological speeches in chapters 1, 23, and 24) shows editorial shaping "
                       "consistent with the broader DtrH project, but this shaping does not require "
                       "inventing the underlying events. The theological vision is consistent: YHWH "
                       "the divine warrior fulfills his land promise through Joshua, and Israel's "
                       "continued possession depends on covenant faithfulness."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "~1406-1380 BC (the conquest and settlement of Canaan following Moses' death, "
                       "using the early exodus date based on 1 Kings 6:1, which places the exodus "
                       "at ~1446 BC and the conquest ~40 years later)",
        "critical_range": "The events described are typically dated to either the late 15th century BC "
                         "(early date, based on 1 Kings 6:1) or the late 13th century BC (late date, "
                         "based on archaeological evidence from the destruction of Hazor and the Merneptah "
                         "Stele of ~1208 BC, which mentions 'Israel' as an entity in Canaan). The book's "
                         "final form is usually dated to the 7th-6th century BC within the DtrH framework, "
                         "with possible post-exilic additions. However, the source materials -- boundary "
                         "lists, city catalogues, and conquest narratives -- may date to the 13th-11th "
                         "century BC. The reference to the Jebusites still holding Jerusalem (Josh 15:63) "
                         "points to a pre-Davidic date for that source (~1000 BC). The reference to Sidon "
                         "rather than Tyre as the great Phoenician city (Josh 11:8; 19:28) fits the Late "
                         "Bronze Age, when Sidon was dominant, rather than the Iron Age, when Tyre rose "
                         "to prominence.",
        "evidence": "Key evidence includes: (1) The Merneptah Stele (~1208 BC) places 'Israel' in Canaan "
                    "by the late 13th century, providing a terminus ante quem for the settlement. "
                    "(2) Archaeological destruction layers at Hazor (stratum XIII, ~1230 BC) correlate "
                    "with Josh 11:10-13. (3) The Amarna Letters (~1350-1330 BC) describe 'Habiru' "
                    "disrupting Canaanite city-states, which some scholars connect to the conquest "
                    "though the identification is disputed. (4) The boundary lists in Josh 13-21 "
                    "reflect settlement patterns consistent with the Late Bronze Age / Iron Age I "
                    "transition. (5) Dead Sea Scrolls fragments of Joshua (4QJosh^a, 4QJosh^b) date "
                    "to ~150-50 BC and show a text largely consistent with the MT, with some "
                    "interesting variations (4QJosh^a places the altar-building of Josh 8:30-35 "
                    "after Josh 5:1, which may preserve an older arrangement). (6) The absence of "
                    "any reference to the monarchy or the temple suggests the core traditions predate "
                    "those institutions."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Israel -- both the generation that conquered the land and all subsequent "
                            "generations who needed to understand why they possessed it and what was "
                            "required to keep it. Joshua answers the question that Deuteronomy raised: "
                            "Will the second generation succeed where the first failed? The answer is "
                            "a qualified yes -- they will enter the land and receive their inheritance, "
                            "but the seeds of future failure are already present (the Gibeonite deception, "
                            "the incomplete conquest, the Transjordan altar controversy). For the exilic "
                            "audience of the DtrH, Joshua provided both hope (God fulfills his promises) "
                            "and warning (possession requires obedience).",

        "purpose": "Joshua's overarching purpose is to demonstrate that YHWH is faithful to his covenant "
                   "promises. The land sworn to Abraham (Gen 15:18-21), legislated in Deuteronomy, and "
                   "reclaimed through holy war in Joshua is YHWH's gift -- not Israel's achievement. The "
                   "book makes this point repeatedly: 'Not one word has failed of all the good things that "
                   "the LORD your God promised concerning you. All have come to pass for you; not one of "
                   "them has failed' (Josh 23:14). But the gift is conditional on covenant loyalty. "
                   "Joshua's farewell speeches (chapters 23-24) warn that serving other gods will result "
                   "in losing the land -- the very trajectory that the Deuteronomistic History will trace "
                   "through Judges, Samuel, and Kings. Joshua thus functions as the hinge between promise "
                   "and possession, between the Torah's forward-looking hope and the Former Prophets' "
                   "backward-looking explanation of exile.",

        "theological_intent": "Joshua presents YHWH as the divine warrior who fights for Israel and against "
                             "the spiritual powers that have held Canaan. The conquest is not merely military "
                             "but cosmic: YHWH throws hailstones from heaven (10:11), commands the sun and "
                             "moon to stand still (10:12-14), and appears as the 'Commander of the army of "
                             "YHWH' (5:14) -- a divine council figure who leads the heavenly host into "
                             "battle alongside Israel's earthly army. The herem (devoted destruction) is "
                             "the most theologically challenging element: entire populations are 'devoted' "
                             "to YHWH, meaning totally destroyed as a sacred offering. In the divine council "
                             "framework, the herem targets the Nephilim remnant (the Anakim) and the "
                             "populations under the spiritual authority of the gods YHWH has judged "
                             "(Psalm 82). The allotment of the land (chapters 13-21) fulfills the "
                             "Deuteronomy 32:8-9 principle in reverse: as YHWH allotted the nations to "
                             "the sons of God, he now allots Canaan to the tribes of Israel -- his own "
                             "portion, reclaimed from the rebel elohim."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic, "
                  "which is what modern Hebrew uses)",
        "linguistic_notes": "Joshua's Hebrew reflects a mixture of early and late features, consistent "
                           "with an early core that was editorially updated. The conquest narratives "
                           "(chapters 1-12) contain archaic vocabulary and syntax: battle terminology, "
                           "geographic designations, and administrative language that match Late Bronze Age "
                           "usage. The boundary lists (chapters 13-21) use technical geographic terminology "
                           "with precise topographic markers (nahal for 'wadi,' gvul for 'border,' pelekh "
                           "for 'district') that are characteristic of ancient land-survey documents. The "
                           "theological speeches (chapters 1, 23, 24) show the distinctive Deuteronomistic "
                           "prose style: flowing hortatory sentences, repeated key vocabulary (shema, "
                           "shamar, ahav, davaq), and covenant-loyalty language. The Song of the Sun "
                           "(10:12-13) is quoted from the 'Book of Jashar' (Sefer HaYashar), a lost "
                           "collection of ancient Hebrew poetry also cited in 2 Samuel 1:18. The poetic "
                           "fragment in 10:12-13 uses archaic verbal forms consistent with early Israelite "
                           "verse. The name 'Joshua' (Yehoshua) means 'YHWH saves/delivers' -- the same "
                           "name as 'Jesus' (Iesous in Greek, from the Aramaic Yeshua), a connection the "
                           "early church exploited extensively (Hebrews 4:8).",
        "grammar_match": "The prose style of Joshua alternates between narrative-historical and "
                        "Deuteronomistic-homiletical registers. The battle narratives use terse, action-"
                        "oriented syntax (wayyiqtol chains describing rapid military events) while the "
                        "speeches use long, complex sentences with multiple subordinate clauses. The "
                        "boundary descriptions employ a distinctive survey-language register found nowhere "
                        "else in the Bible in such concentration. This linguistic diversity supports the "
                        "view that the book draws on multiple source types (military annals, geographic "
                        "surveys, covenant speeches) woven into a single theological narrative."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Joshua IS scripture -- it is the fulfillment narrative of the Torah's land "
                   "promise and the opening act of the prophetic history.",
        "nt_usage": "Joshua is cited and alluded to throughout the New Testament. Hebrews 11:30-31 "
                    "celebrates the faith that brought down Jericho's walls and saved Rahab. James 2:25 "
                    "holds up Rahab as an example of faith working through action. Hebrews 4:8 explicitly "
                    "names Joshua (Iesous) and argues that the 'rest' he gave Israel was incomplete -- "
                    "the true Sabbath rest remains for the people of God. Acts 7:45 references Joshua "
                    "bringing the tabernacle into the land. The typological connection between Joshua "
                    "(Yehoshua, 'YHWH saves') and Jesus (Yeshua/Iesous, same name) was deeply important "
                    "to the early church: as Joshua led Israel into the earthly Promised Land through "
                    "the Jordan, Jesus leads believers into the heavenly rest through baptism. The "
                    "Commander of YHWH's army (Josh 5:13-15) was widely identified by patristic "
                    "interpreters as a pre-incarnate appearance of Christ (a Christophany), given the "
                    "figure's acceptance of worship and his holy-ground declaration. Paul's language of "
                    "spiritual warfare (Eph 6:10-18, 2 Cor 10:3-5) draws on the divine warrior theology "
                    "that Joshua exemplifies.",
        "internal_consistency": "Joshua is the natural sequel to Deuteronomy. The commission of Joshua in "
                               "Deuteronomy 31:1-8 is fulfilled in Joshua 1:1-9. The Jordan crossing "
                               "(Josh 3-4) echoes the Red Sea crossing (Exod 14-15). The circumcision at "
                               "Gilgal (Josh 5:2-9) resolves the uncircumcised wilderness generation. The "
                               "covenant renewal at Shechem (Josh 24) corresponds to the Deuteronomic "
                               "covenant structure. The allotment of land fulfills the promises to the "
                               "patriarchs (Gen 12:7; 15:18-21; 26:3; 28:13-15). The Anakim of Joshua "
                               "11:21-22 connect directly to the Nephilim/giant tradition of Numbers 13:33 "
                               "and Deuteronomy 2-3. The herem legislation of Deuteronomy 7:1-5 and 20:16-18 "
                               "is implemented in Joshua 6-11. The cities of refuge commanded in "
                               "Deuteronomy 19:1-13 are established in Joshua 20. The Levitical cities "
                               "commanded in Numbers 35 are assigned in Joshua 21. The book closes the "
                               "Torah's open loops with remarkable thoroughness."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: Two manuscripts of Joshua have been identified at "
                    "Qumran -- 4QJosh^a (4Q47) and 4QJosh^b (4Q48), dating to approximately "
                    "150-50 BC. The most significant textual finding is in 4QJosh^a, which places "
                    "the altar-building episode of Joshua 8:30-35 after Joshua 5:1 rather than in "
                    "its MT position after the Ai narrative. This arrangement may preserve an older "
                    "textual tradition in which the Shechem covenant ceremony followed immediately "
                    "after the Jordan crossing, before the conquest began. The LXX (Septuagint) "
                    "also shows significant variations from the MT in Joshua, particularly in the "
                    "boundary lists and the conclusion of the book.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. The MT of Joshua is generally well-preserved, "
                     "though it differs from the LXX in several significant places: the order of "
                     "events in chapters 5-8, the length of some boundary descriptions, and "
                     "additional material at the end of the book."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The Greek Joshua is approximately 4-5% shorter than the MT, suggesting either "
                     "LXX abbreviation or MT expansion. Key differences: the LXX places Josh 8:30-35 "
                     "after 9:2 (different from both the MT and 4QJosh^a positions), and the LXX "
                     "adds a notice at the end of the book about Joshua placing the flint knives "
                     "from the Gilgal circumcision in his tomb -- a striking etiological detail "
                     "absent from the MT."},
            {"name": "Dead Sea Scrolls", "date": "~150-50 BC",
             "note": "4QJosh^a and 4QJosh^b preserve fragments of chapters 4-10 and 17. The most "
                     "important variant is the placement of the Shechem altar-building (8:30-35) "
                     "after 5:1 in 4QJosh^a, which may reflect the oldest arrangement of the "
                     "narrative. Both manuscripts generally align with the proto-MT tradition."},
            {"name": "Samaritan Joshua (Chronicon Samaritanum)", "date": "Medieval, based on older traditions",
             "note": "An Arabic chronicle used by the Samaritan community that contains a parallel "
                     "Joshua narrative with significant differences, particularly emphasizing Mount "
                     "Gerizim rather than Shiloh as the central sanctuary. While the chronicle is "
                     "medieval in its present form, it preserves traditions that may be very ancient."},
            {"name": "Targum Jonathan", "date": "1st-3rd century AD tradition",
             "note": "The Aramaic translation of Joshua that occasionally interprets theologically "
                     "significant passages. At Joshua 5:14, the Targum identifies the 'Commander of "
                     "YHWH's army' as an angel, consistent with the divine council reading but "
                     "avoiding the implication that the figure is YHWH himself."}
        ],
        "reliability": "The text of Joshua is well-preserved across the major witnesses. The most "
                       "significant textual issues involve the arrangement of material (particularly "
                       "the placement of 8:30-35 and the order of events in chapters 5-9) rather "
                       "than the content itself. The boundary lists show the most variation between "
                       "MT and LXX, likely because geographic lists were susceptible to updating as "
                       "place names changed. The theological content -- the divine warrior narratives, "
                       "the herem commands, the covenant speeches -- is remarkably stable across all "
                       "witnesses, indicating that these passages were treated with special care in "
                       "transmission."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Joshua is set in the land of Canaan during the Late Bronze Age / Iron Age I "
                   "transition (either ~1400-1350 BC by the early chronology or ~1230-1180 BC by the "
                   "late chronology). The Canaanite city-state system was in decline, weakened by "
                   "Egyptian imperial control, inter-city warfare, and the broader 'Bronze Age Collapse' "
                   "that destabilized the entire eastern Mediterranean. The land was organized as a "
                   "patchwork of independent city-states, each ruled by a petty king (melek) who was "
                   "nominally subject to Egypt. The Amarna Letters (~1350-1330 BC) reveal Canaanite "
                   "kings desperately appealing to Pharaoh for help against invaders and rivals. Joshua "
                   "describes a rapid military campaign that targeted key cities (Jericho, Ai, Hazor) "
                   "and defeated coalition armies, followed by a gradual process of settlement and "
                   "allotment.",

        "geography": "The conquest moves in three phases: (1) Central -- crossing the Jordan near "
                     "Jericho, then taking Ai and establishing a base at Gilgal; (2) Southern -- "
                     "defeating the five-king Amorite coalition at Gibeon and sweeping south through "
                     "Makkedah, Libnah, Lachish, Eglon, Hebron, and Debir; (3) Northern -- defeating "
                     "Jabin's coalition at the waters of Merom and burning Hazor. The allotment covers "
                     "the entire land from the Negev to Lebanon, from the Mediterranean to the Jordan "
                     "Rift Valley. Key geographic markers include Gilgal (the base camp), Shechem (the "
                     "covenant center between Ebal and Gerizim), Shiloh (where the tabernacle is set "
                     "up and allotments finalized), and the Jordan River (the boundary between east "
                     "and west tribes).",

        "historical_connections": "The Late Bronze Age Collapse (~1200-1150 BC) saw the simultaneous "
                                 "decline of the Hittite Empire, Egyptian imperial power in Canaan, "
                                 "Mycenaean civilization, and the Ugaritic kingdom. The Sea Peoples "
                                 "(including the Philistines) invaded the coastal regions. This power "
                                 "vacuum created conditions favorable for a new population entering the "
                                 "highlands. Archaeological surveys (Israel Finkelstein) show a dramatic "
                                 "increase in small hilltop settlements in the central highlands during "
                                 "Iron Age I (~1200-1000 BC), consistent with an influx of new population. "
                                 "The destruction of Hazor (stratum XIII) is well-attested archaeologically "
                                 "and correlates with Josh 11:10-13. Jericho's archaeology is more "
                                 "contested: Kathleen Kenyon dated the destruction to ~1550 BC (too early "
                                 "for either chronology), but Bryant Wood has argued for a ~1400 BC "
                                 "destruction based on ceramic analysis. The Merneptah Stele (~1208 BC) "
                                 "confirms 'Israel' as an established entity in Canaan by the late 13th "
                                 "century, providing an external anchor point."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "major",
        "summary": "Joshua contains several key divine council passages and themes that connect "
                   "directly to the Deuteronomy 32 worldview. The most explicit is the theophany "
                   "in Joshua 5:13-15, where Joshua encounters the 'Commander of the army of YHWH' "
                   "(sar tseva YHWH) -- a divine council figure who leads the heavenly host into "
                   "battle. This figure draws his sword (indicating martial purpose), identifies "
                   "himself as the leader of YHWH's celestial army, and commands Joshua to remove "
                   "his sandals because the ground is holy -- the same command given to Moses at "
                   "the burning bush (Exod 3:5). Whether this figure is YHWH himself, the Angel "
                   "of YHWH (the visible YHWH), or a high-ranking angel like Michael, the passage "
                   "establishes that the conquest is a joint operation between YHWH's heavenly army "
                   "and Israel's earthly army."
                   "\n\n"
                   "The cosmic warfare theme runs throughout: (1) The Jordan crossing (Josh 3-4) "
                   "recapitulates the Red Sea crossing -- YHWH controls the waters of chaos, "
                   "opening a path through the cosmic barrier. (2) The fall of Jericho (Josh 6) "
                   "is a seven-day liturgical ritual, not a military siege -- the walls fall by "
                   "divine power, not human engineering. (3) The sun standing still (Josh 10:12-14) "
                   "is the most dramatic divine warrior act in the book: YHWH commands the "
                   "heavenly bodies themselves to serve Israel's military needs. In the ANE "
                   "context, the sun (Shamash) and moon (Yarikh) were deities -- YHWH's command "
                   "over them demonstrates his absolute supremacy over the astral powers allotted "
                   "to the nations (Deut 4:19). (4) Hailstones from heaven (Josh 10:11) -- YHWH "
                   "fights with cosmic weapons. (5) The extermination of the Anakim (Josh 11:21-22) "
                   "-- the giant clans connected to the Nephilim (Num 13:33), the biological "
                   "legacy of the Watchers' rebellion (Gen 6:1-4; 1 Enoch 6-16)."
                   "\n\n"
                   "The allotment of the land (Josh 13-21) is the Deuteronomy 32:8-9 principle "
                   "in action: as YHWH allotted the other nations to the sons of God, he now "
                   "allots the Promised Land to the twelve tribes -- his own inheritance, reclaimed "
                   "from the spiritual powers that had held it. Rahab's name (rahab) is the same "
                   "word used for the cosmic chaos monster in Isaiah 51:9, Psalm 89:10, and "
                   "Job 26:12 -- a wordplay that may connect her story to the chaos-to-order "
                   "theme of the conquest. Joshua's covenant renewal at Shechem (Josh 24) uses "
                   "explicit divine council language: 'the gods your fathers served beyond the "
                   "River' and 'the gods of the Amorites in whose land you dwell' (24:15) -- "
                   "acknowledging the existence of other elohim while demanding exclusive loyalty "
                   "to YHWH.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 17 (the conquest as reclaiming divine council territory)",
            "The Unseen Realm, chapters 13-16 (Deuteronomy 32 worldview -- the theological foundation for Joshua)",
            "Supernatural, chapters 14-15 (the conquest and the Nephilim connection)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 7-8 (the Commander of YHWH's army)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 4-5 (giant clans and territorial spirits)",
            "The Naked Bible Podcast, episodes 98-102 (Joshua and the divine warrior)",
            "The Naked Bible Podcast, episode 118 (the Anakim and the Nephilim connection)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "The Conquest and the Herem -- The Hardest Question in the Old Testament",
            "body": "Joshua's conquest narratives include the herem -- the 'devoted destruction' of "
                    "entire Canaanite populations. This is the most ethically challenging material in "
                    "the Old Testament and has been debated from antiquity. Several interpretive "
                    "frameworks have been proposed: (1) The herem was limited in scope -- the book "
                    "itself indicates that the conquest was partial and many Canaanites survived "
                    "(Josh 15:63; 16:10; 17:12-13; Judges 1). The language of total destruction may "
                    "be hyperbolic conquest rhetoric, paralleled in the Mesha Stele and Egyptian "
                    "campaign accounts. (2) The herem targeted specific groups -- particularly the "
                    "Nephilim/Anakim remnant and populations corrupted by the 'abominations' named "
                    "in Deuteronomy 18:9-14. In the divine council framework, the herem cleanses the "
                    "land of the biological and spiritual legacy of the Watchers' rebellion. "
                    "(3) The herem is covenantal judgment -- God is the judge of all the earth "
                    "(Gen 18:25), and the Canaanites' destruction is presented as divine judgment "
                    "delayed 400 years (Gen 15:16). (4) The herem is unique to a specific moment in "
                    "redemptive history -- it is never generalized as a model for subsequent warfare. "
                    "This study presents the herem in its full ANE context without minimizing the "
                    "difficulty or avoiding the theological questions."
        },
        {
            "type": "scholarship",
            "title": "The Archaeology Debate",
            "body": "The historicity of Joshua's conquest is one of the most contested issues in "
                    "biblical archaeology. Three major models compete: (1) The 'Conquest Model' "
                    "(Albright, Yadin, Kitchen) argues for a rapid military campaign consistent with "
                    "Joshua's account, supported by destruction layers at Hazor, Lachish, and other "
                    "sites. (2) The 'Peaceful Infiltration Model' (Alt, Noth) proposes gradual "
                    "pastoral nomadic settlement rather than military conquest. (3) The 'Peasant "
                    "Revolt Model' (Mendenhall, Gottwald) suggests 'Israel' emerged from indigenous "
                    "Canaanite populations who revolted against the city-state system. Current "
                    "consensus leans toward a complex process involving some military action, some "
                    "peaceful settlement, and some cultural transformation -- which may actually fit "
                    "the biblical text better than a simplistic reading, since Joshua itself describes "
                    "incomplete conquest and ongoing Canaanite presence."
        },
        {
            "type": "interpretation",
            "title": "The Commander of YHWH's Army (Joshua 5:13-15)",
            "body": "The identity of the figure who appears to Joshua before Jericho is one of the "
                    "most important christological questions in the Old Testament. He is called 'the "
                    "Commander (sar) of the army (tseva) of YHWH,' draws a sword, and commands Joshua "
                    "to remove his sandals because the ground is holy. Patristic interpreters "
                    "(Eusebius, Origen, Theodoret) widely identified this figure as a pre-incarnate "
                    "appearance of Christ -- a Christophany -- because: (a) he receives Joshua's "
                    "prostration without rebuke (unlike the angel in Revelation 19:10 who refuses "
                    "worship), (b) he declares the ground holy by his presence (a divine prerogative), "
                    "and (c) the scene directly parallels the burning bush theophany where YHWH himself "
                    "appears. Other interpreters identify him as the Angel of YHWH (the visible YHWH "
                    "of the OT theophanies) or as Michael the archangel (the prince of Israel in "
                    "Daniel 10:21; 12:1). In the divine council framework, this figure is the second "
                    "power in heaven -- the visible YHWH who leads the heavenly army into battle."
        },
        {
            "type": "theology",
            "title": "Joshua and the Deuteronomy 32 Worldview",
            "body": "Joshua can only be properly understood within the Deuteronomy 32:8-9 cosmic "
                    "framework. When the Most High divided the nations and allotted them to the sons "
                    "of God, he kept Israel as his own portion. The conquest of Canaan is YHWH "
                    "reclaiming his allotted territory from the spiritual powers that had corrupted "
                    "it -- the gods of the Canaanites, the Anakim/Nephilim bloodline, and the "
                    "religious systems built around the worship of these beings. Every military "
                    "victory in Joshua is simultaneously a spiritual victory: the fall of Jericho "
                    "is a liturgical act of cosmic warfare; the sun standing still is YHWH "
                    "commanding the astral powers; the defeat of the Anakim is the cleanup of the "
                    "Watchers' rebellion. The allotment of land to the tribes reverses the Babel "
                    "allotment: the divided nations now yield territory to YHWH's united people. "
                    "The 'rest' (menukhah) that Joshua gives Israel (Josh 21:44; 23:1) is a foretaste "
                    "of the cosmic rest when all rebel elohim are judged and YHWH's reign is "
                    "unchallenged -- the rest that Hebrews 4:8-11 says Joshua could not fully provide."
        }
    ]
}
