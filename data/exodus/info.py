"""
info.py — Exodus (Shemot): Scholarly Text Introduction

This file provides the "front page" for Exodus in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?
"""

TEXT_INFO = {
    "text_id": "exodus",
    "display_name": "Exodus (Shemot)",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical — Old Testament / Torah",
        "detail": "Exodus is universally recognized as canonical scripture by Jewish, "
                  "Catholic, Orthodox, and Protestant traditions. It is the second of "
                  "the five books of the Torah (Pentateuch) and the narrative hinge of "
                  "the entire Old Testament — the event by which God constitutes Israel "
                  "as his covenant people. The exodus event is the most frequently "
                  "referenced historical act of God in the Hebrew Bible, cited in the "
                  "Psalms, the Prophets, and the New Testament as the paradigmatic act "
                  "of divine redemption. No mainstream tradition has ever questioned "
                  "its canonical status."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "Moses, as affirmed by Jewish tradition (Talmud Bava Batra 14b), "
                       "the text itself (Exodus 17:14, 24:4, 34:27 — 'Then the LORD said to "
                       "Moses, Write this'), Jesus (Mark 7:10, 12:26 — 'in the book of Moses'), "
                       "and the New Testament authors (Romans 9:15, Hebrews 8:5). The Torah is "
                       "consistently called 'the Book of Moses' in the OT and NT, and Exodus is "
                       "the book where Moses is most personally present as narrator-participant.",

        "scholarly_debate": "Critical scholarship applies the same Documentary Hypothesis framework "
                           "used for Genesis. The Yahwist (J) source is identified in the plague "
                           "narrative and wilderness stories. The Elohist (E) source is seen in "
                           "the Horeb traditions and certain Moses narratives. The Priestly (P) "
                           "source is identified in the tabernacle instructions (chs. 25-31, "
                           "35-40), genealogies, and ritual legislation. The Deuteronomist (D) "
                           "is considered largely absent from Exodus itself but shapes how Exodus "
                           "is received in Deuteronomy. More recent approaches (Childs, Durham, "
                           "Dozeman) focus on the final form and literary unity of the text rather "
                           "than hypothetical source reconstruction. Some scholars (Kitchen, "
                           "Hoffmeier, Provan) argue for substantial Mosaic-era composition based "
                           "on Egyptian loanwords, authentic local details, and the archaic poetry "
                           "of the Song of the Sea (Exodus 15), which linguistically dates to the "
                           "late 2nd millennium BC.",

        "bottom_line": "The Song of the Sea (Exodus 15) is widely regarded — even by critical "
                       "scholars — as among the oldest poetry in the Hebrew Bible, possibly "
                       "contemporary with the events it describes. The prose narrative may reflect "
                       "Mosaic-era traditions shaped and edited over centuries, or it may be "
                       "substantially Mosaic with minor editorial updates. Either way, Exodus as "
                       "we have it is a theologically coherent narrative that Israel staked its "
                       "entire identity on. The question of compositional history does not diminish "
                       "the text's claim to record real divine action in real history."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "~1446-1406 BC (Mosaic period). This date is derived from 1 Kings 6:1, "
                       "which places the exodus 480 years before Solomon began building the "
                       "Temple (~966 BC), yielding an exodus date of ~1446 BC. This corresponds "
                       "to the late 18th Dynasty in Egypt (reign of Thutmose III or Amenhotep II).",
        "critical_range": "The dating of the exodus is one of the most debated questions in "
                         "biblical scholarship. Two major positions exist:\n\n"
                         "EARLY DATE (~1446 BC): Based on 1 Kings 6:1 taken literally, supported "
                         "by the Amarna Letters (which describe Canaan in upheaval ~1400-1350 BC, "
                         "potentially matching the conquest), the destruction layer at Jericho "
                         "(Kenyon's City IV, debated), and the Merneptah Stele (1208 BC) which "
                         "presupposes Israel is already established in Canaan.\n\n"
                         "LATE DATE (~1260-1250 BC): Based on Exodus 1:11's mention of the store "
                         "city 'Rameses' (likely Pi-Ramesses, built under Ramesses II, 1279-1213 BC), "
                         "destruction layers at Hazor and other Canaanite cities in the late 13th "
                         "century, and the argument that the 480 years in 1 Kings 6:1 is symbolic "
                         "(12 generations x 40 years).\n\n"
                         "Some scholars (Lemche, Thompson, Finkelstein) argue the exodus as described "
                         "never occurred, while others (Hoffmeier, Kitchen) marshal extensive "
                         "archaeological and Egyptian evidence supporting a historical core to the "
                         "narrative, even if the precise date remains disputed.",
        "evidence": "Egyptian evidence: The Merneptah Stele (1208 BC) mentions 'Israel' as a "
                    "people in Canaan — the earliest extra-biblical reference. Papyrus Anastasi V "
                    "describes Shasu nomads crossing the Egyptian border. The Brooklyn Papyrus "
                    "(1740 BC) lists Semitic slaves with names matching biblical patterns (Shiphrah "
                    "appears as a slave name). The Ipuwer Papyrus describes catastrophes in Egypt "
                    "that some have compared to the plagues (though most Egyptologists date it "
                    "earlier and consider the parallel incidental). The oldest manuscript fragments "
                    "of Exodus come from the Dead Sea Scrolls (4QExod-a through 4QpaleoExod-m, "
                    "~250-100 BC)."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Israel — the covenant community receiving its foundational identity "
                            "narrative. If Mosaic, the immediate audience is the generation that "
                            "experienced the exodus and stood at Sinai. If later, the audience is "
                            "Israel in every era needing to remember who redeemed them, what covenant "
                            "binds them, and whose presence dwells among them. Exodus is the text "
                            "that transforms a group of slaves into a nation with a God, a law, and "
                            "a mission.",

        "purpose": "Exodus answers the questions: Who is YHWH? Why should Israel worship him and "
                   "no other? What does it mean to be God's people? The book has three great "
                   "movements: (1) Liberation — God hears the cry of the oppressed and acts with "
                   "sovereign power to free them (chs. 1-15); (2) Covenant — God brings Israel "
                   "to Sinai and establishes a binding relationship with terms, obligations, and "
                   "promises (chs. 19-24); (3) Presence — God commands the building of the "
                   "tabernacle so that he can dwell among his people (chs. 25-40). The climax "
                   "of Exodus is not the Red Sea crossing — it is the glory of YHWH filling the "
                   "tabernacle (40:34-38). The point of deliverance is not merely escape from "
                   "slavery; it is that God might dwell with his people. This is the trajectory "
                   "that runs through the entire Bible to Revelation 21:3 — 'Behold, the dwelling "
                   "place of God is with man.'",

        "theological_intent": "Exodus is theological polemic against Egypt's gods and worldview. "
                             "The plagues are not random catastrophes — they are systematic "
                             "dismantlings of the Egyptian pantheon: the Nile turning to blood "
                             "targets Hapi (Nile god), darkness targets Ra (sun god), the death of "
                             "the firstborn targets Pharaoh himself as a 'son of Ra.' Exodus 12:12 "
                             "makes this explicit: 'Against all the gods of Egypt I will execute "
                             "judgments.' The golden calf episode (ch. 32) is not random idolatry — "
                             "it is Israel reverting to Egyptian religious practice (the Apis bull) "
                             "the moment Moses is absent. The tabernacle is not merely a tent — it "
                             "is a microcosm of creation, heaven on earth, the reversal of Eden's "
                             "exile. Every detail is theologically loaded."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic, "
                  "which is what modern Hebrew uses). The Dead Sea Scrolls include both: "
                  "4QpaleoExod-m is written in Paleo-Hebrew script, while other Exodus "
                  "manuscripts use the square script.",
        "linguistic_notes": "Exodus contains both prose narrative and some of the most archaic "
                           "poetry in the Hebrew Bible. The Song of the Sea (Exodus 15:1-18) is "
                           "considered by scholars across the spectrum (Cross, Freedman, Robertson) "
                           "to exhibit linguistic features consistent with late 2nd millennium BC "
                           "Hebrew: archaic verbal forms, early morphological patterns, and "
                           "vocabulary shared with Ugaritic poetry. Egyptian loanwords appear "
                           "throughout the text — 'ark' (tebah, from Egyptian dbt), the name "
                           "'Moses' (moshe, likely from Egyptian ms meaning 'born of'), 'Goshen,' "
                           "'Pithom,' 'Rameses' — indicating genuine contact with Egyptian language "
                           "and culture. The legal material (chs. 21-23, the 'Book of the Covenant') "
                           "shares structural and linguistic features with other ancient Near Eastern "
                           "law codes (Laws of Hammurabi, Hittite laws).",
        "grammar_match": "The Hebrew of Exodus is consistent with the Torah corpus and with what "
                        "we know of Iron Age Hebrew from inscriptions. The legal prose of the "
                        "Book of the Covenant matches ancient Near Eastern casuistic law style "
                        "('if a man does X, then Y'). The tabernacle instructions use a "
                        "specialized technical vocabulary that has parallels in both Egyptian "
                        "architectural texts and Mesopotamian temple-building accounts."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "Exodus IS scripture — it is the event on which the entire Old Testament "
                   "covenant relationship is built, and the typological foundation for New "
                   "Testament salvation theology.",
        "nt_usage": "The New Testament treats the exodus as the defining act of God in the Old "
                    "Testament and the primary type for understanding what Jesus accomplished. "
                    "Jesus IS the Passover lamb (1 Corinthians 5:7, John 1:29, 1 Peter 1:19). "
                    "The Last Supper IS a Passover meal reinterpreted around Jesus' death "
                    "(Matthew 26:17-29, Luke 22:14-20). Jesus' transfiguration conversation with "
                    "Moses and Elijah is about his 'exodus' (Luke 9:31, using the Greek word "
                    "exodos). Paul explicitly maps the exodus onto the Christian life: crossing "
                    "the Red Sea = baptism, manna = spiritual food, the rock = Christ "
                    "(1 Corinthians 10:1-4). Hebrews builds its entire argument on the "
                    "superiority of Christ's priesthood and sacrifice over the tabernacle system "
                    "established in Exodus. Revelation's plagues echo the Egyptian plagues, and "
                    "the 'song of Moses and the Lamb' (Revelation 15:3) explicitly connects "
                    "the exodus to final redemption.",
        "internal_consistency": "Exodus picks up directly from Genesis 50 (Israel in Egypt, "
                               "the promise that God will bring them out) and establishes the "
                               "covenant framework that governs the rest of the Torah (Leviticus, "
                               "Numbers, Deuteronomy). The prophets constantly invoke the exodus as "
                               "the basis of God's relationship with Israel (Hosea 11:1, Jeremiah "
                               "2:6, Ezekiel 20:5-10, Micah 6:4). Isaiah envisions the future "
                               "restoration as a 'new exodus' (Isaiah 43:16-21, 51:9-11). The "
                               "exodus is the thread that stitches the entire Old Testament together."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments from Qumran, including 4QExod-a through "
                    "4QExod-c and the notable 4QpaleoExod-m (written in Paleo-Hebrew script, "
                    "~250-100 BC). 4QpaleoExod-m is particularly significant because it is an "
                    "extensive manuscript that aligns closely with the Samaritan Pentateuch "
                    "tradition, proving that the SP readings are ancient and not late inventions.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text behind most English translations. For Exodus, "
                     "the MT is generally well-preserved and stable."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The Greek translation preserves important variant readings. In the "
                     "tabernacle chapters (35-40), the LXX has a significantly different "
                     "arrangement and shorter text than the MT, suggesting either a different "
                     "Hebrew Vorlage or editorial revision in the Greek tradition."},
            {"name": "Samaritan Pentateuch (SP)", "date": "Pre-2nd century BC tradition",
             "note": "Preserves readings that sometimes agree with the LXX against the MT. "
                     "In Exodus, the SP adds harmonizing expansions (e.g., inserting plague "
                     "fulfillment notices) and the Gerizim commandment in the Decalogue. "
                     "4QpaleoExod-m confirms that many SP readings are ancient."},
            {"name": "Dead Sea Scrolls", "date": "~250 BC - 68 AD",
             "note": "Multiple manuscripts of Exodus from Qumran. They attest a fluid text "
                     "tradition in the Second Temple period — some scrolls align with MT, some "
                     "with SP, some with LXX, proving that no single text type yet dominated."},
            {"name": "Targumim", "date": "1st century BC onward",
             "note": "Aramaic translations/paraphrases (Targum Onkelos, Targum Pseudo-Jonathan, "
                     "Fragment Targum). The Targumim are especially rich for Exodus, adding "
                     "interpretive expansions that reveal how the plagues, the Red Sea crossing, "
                     "and the Sinai theophany were understood in the synagogue."}
        ],
        "reliability": "Exodus is exceptionally well-attested across multiple text traditions. "
                       "The MT, LXX, SP, and DSS agree on the narrative content and major "
                       "theological claims. The most significant textual issue is the tabernacle "
                       "section (chs. 35-40), where the LXX order differs from the MT, and the "
                       "Decalogue (ch. 20), where the SP adds the Gerizim commandment. No major "
                       "theological doctrine depends on a textual variant in Exodus."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "Exodus spans from Israel's enslavement in Egypt through the construction of "
                   "the tabernacle at Sinai. By traditional chronology, this covers ~1526-1445 BC "
                   "(early date) or ~1300-1240 BC (late date). The setting is the Nile Delta region "
                   "of Egypt (Goshen, Pithom, Rameses/Pi-Ramesses), the wilderness of the Sinai "
                   "Peninsula, and Mount Sinai/Horeb. The Egyptian backdrop is the New Kingdom — "
                   "the most powerful period of Egyptian imperial history, when Pharaoh commanded "
                   "massive building projects using conscript and slave labor.",

        "geography": "The action moves from Goshen (northeastern Nile Delta) through the 'Reed Sea' "
                     "(yam suph — the precise location is debated: Gulf of Suez, Gulf of Aqaba, "
                     "the Bitter Lakes, or the northern Sinai coast) into the wilderness of Sinai. "
                     "Key sites: Goshen -> Succoth -> Etham -> the sea crossing -> Marah -> Elim -> "
                     "Wilderness of Sin -> Rephidim -> Sinai/Horeb. The location of Mount Sinai "
                     "itself is debated: traditional site = Jebel Musa in southern Sinai Peninsula, "
                     "alternatives include Jebel al-Lawz in northwest Saudi Arabia and Har Karkom "
                     "in the Negev. Midian, where Moses fled to and met God at the burning bush, is "
                     "in the northwestern Arabian Peninsula.",

        "historical_connections": "Egyptian records do not directly mention the exodus — which is "
                                 "unsurprising, as Egyptian royal inscriptions never recorded "
                                 "military defeats or slave revolts. However, multiple Egyptian "
                                 "texts illuminate the world of Exodus: the Brooklyn Papyrus lists "
                                 "Asiatic (Semitic) slaves with names like those in Exodus. Papyrus "
                                 "Anastasi records border officials monitoring Shasu nomads crossing "
                                 "between Egypt and Sinai. The Merneptah Stele (1208 BC) confirms "
                                 "Israel's existence in Canaan by the late 13th century. The Leiden "
                                 "Papyrus 348 mentions 'Apiru (possibly related to 'Hebrew') forced "
                                 "laborers. The Elephantine Papyri (5th century BC) show a Jewish "
                                 "community in Egypt that celebrated Passover, confirming the deep "
                                 "antiquity of the exodus tradition."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "high",
        "summary": "Exodus is deeply significant for the divine council worldview, though the "
                   "connections are often missed by readers unfamiliar with the framework. Key "
                   "elements:\n\n"
                   "THE PLAGUES AS COSMIC WARFARE: Exodus 12:12 declares, 'Against all the gods "
                   "of Egypt I will execute judgments — I am YHWH.' In the divine council "
                   "framework (Deuteronomy 32:8-9, Psalm 82), the gods of the nations are real "
                   "spiritual beings — rebellious members of God's council who were assigned to "
                   "the nations at Babel. The plagues are not merely natural disasters — they are "
                   "YHWH dismantling the spiritual powers behind Egypt's pantheon. Numbers 33:4 "
                   "confirms: 'On their gods the LORD executed judgments.'\n\n"
                   "THE DESTROYER (MASHCHIT): In Exodus 12:23, the agent of the tenth plague is "
                   "called 'the destroyer' — a figure distinct from YHWH himself ('YHWH will pass "
                   "over the door and will not allow the destroyer to enter'). Heiser connects "
                   "this to the mal'ak (angelic agent) tradition and the 'death angel' motif. "
                   "This is a divine council member executing God's decree.\n\n"
                   "SINAI AS DIVINE COUNCIL ASSEMBLY: Deuteronomy 33:2 says YHWH came from Sinai "
                   "'with ten thousands of holy ones' — the divine council accompanied God to the "
                   "covenant ceremony. Psalm 68:17 describes God's chariots as 'twice ten thousand, "
                   "thousands upon thousands' at Sinai. Acts 7:53 and Galatians 3:19 reference the "
                   "law being 'delivered by angels.' The Sinai theophany is a divine council event — "
                   "the heavenly assembly descending to meet Israel.\n\n"
                   "THE HARDENING OF PHARAOH: Heiser reads the hardening of Pharaoh's heart within "
                   "the divine council decision-making framework — God's decree executed through the "
                   "spiritual realm, consistent with the pattern in 1 Kings 22:19-23 (the lying "
                   "spirit sent by the council) and Job 1-2 (the satan acting within council "
                   "permission).\n\n"
                   "THE TABERNACLE AS COSMIC MOUNTAIN: The tabernacle is structured as a heaven-earth "
                   "meeting point — the Holy of Holies corresponds to God's throne room (the council "
                   "chamber), the cherubim on the ark are council throne-guardians (cf. Ezekiel 1, 10), "
                   "and the entire structure is a portable Eden, the place where God dwells with his "
                   "people as he once walked in the garden.",

        "key_heiser_refs": [
            "The Unseen Realm, chapters 15-18 (exodus, Sinai, divine council assembly)",
            "Supernatural, chapter 10 (the cosmic significance of the exodus)",
            "The Naked Bible Podcast, episodes on Exodus (plagues as divine warfare, Sinai theophany)",
            "Angels (2018), discussion of the destroyer and angelic mediation of the law",
            "Demons (2020), the gods of Egypt as territorial spirits under judgment"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "The Exodus Dating Debate",
            "body": "The date of the exodus is one of the most contested issues in biblical "
                    "archaeology. The early date (~1446 BC, 18th Dynasty) and late date (~1260 BC, "
                    "19th Dynasty/Ramesses II) both have serious scholarly defenders. The early "
                    "date takes 1 Kings 6:1 at face value and points to the Amarna Letters and "
                    "Jericho's destruction. The late date points to the name 'Rameses' in Exodus "
                    "1:11 and 13th-century destruction layers in Canaan. A third position holds "
                    "that the exodus is theological narrative without a specific historical anchor. "
                    "This study presents all views honestly. The theological message of Exodus does "
                    "not depend on resolving the archaeological debate — but the biblical text "
                    "clearly presents the exodus as a real event in real history."
        },
        {
            "type": "interpretation",
            "title": "The Genre of the Plague Narrative",
            "body": "Were the plagues 'natural' phenomena heightened by divine timing, or "
                    "wholly supernatural events? Were there exactly ten, or is the ten-plague "
                    "structure a literary arrangement? Did they happen in rapid succession or "
                    "over months? These questions have occupied scholars for centuries. The text "
                    "itself does not provide a naturalistic explanation — it attributes every "
                    "plague directly to YHWH's word spoken through Moses. The literary structure "
                    "(three cycles of three plagues plus the climactic tenth) suggests careful "
                    "theological composition, whether or not it also records precise chronological "
                    "history. The plagues are narrated as cosmic warfare — YHWH vs. Pharaoh and "
                    "his gods — and should be read in that framework first."
        },
        {
            "type": "scholarship",
            "title": "Exodus and Egyptian Records",
            "body": "The absence of the exodus from Egyptian records is frequently cited as "
                    "evidence against its historicity. This argument has less force than it "
                    "appears. Egyptian royal inscriptions are propaganda — they NEVER record "
                    "defeats, humiliations, or slave revolts. The Berlin Pedestal, the Merneptah "
                    "Stele, and the Elephantine texts all place Israel in the broader Egyptian "
                    "world exactly where the Bible places them. Semitic slaves with biblical-type "
                    "names are attested in Egypt in exactly the right periods. The question is not "
                    "whether Semitic peoples were enslaved in Egypt (they demonstrably were) but "
                    "whether the specific events of Exodus occurred as described. Honest scholarship "
                    "holds this as an open question, not a settled one."
        }
    ]
}
