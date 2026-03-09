"""
info.py — Leviticus (Vayikra): Scholarly Text Introduction

This file provides the "front page" for Leviticus in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?
"""

TEXT_INFO = {
    "text_id": "leviticus",
    "display_name": "Leviticus (Vayikra)",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical — Old Testament / Torah",
        "detail": "Leviticus is universally recognized as canonical scripture by "
                  "Jewish, Catholic, Orthodox, and Protestant traditions. It is "
                  "the third book of the Torah (Pentateuch) and the physical center "
                  "of the five books of Moses. In Jewish tradition, it was the first "
                  "book taught to children (Leviticus Rabbah 7:3), precisely because "
                  "it deals with purity and sacrifice — themes considered foundational "
                  "to covenant life. Its canonical status has never been questioned "
                  "by any mainstream tradition."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "Moses, as affirmed by Jewish tradition (Talmud Bava Batra 14b-15a), "
                       "Jesus (Mark 1:44, referencing Lev 14:2-32), and the New Testament "
                       "authors. Leviticus consistently attributes its legislation to divine "
                       "speech mediated through Moses: 'The LORD spoke to Moses' occurs over "
                       "30 times in the book. The setting is Sinai (Lev 7:38, 25:1, 26:46, "
                       "27:34), placing the composition within the wilderness period.",

        "scholarly_debate": "Critical scholarship assigns the bulk of Leviticus to the Priestly "
                           "source (P), with chapters 17-26 identified as a distinct 'Holiness "
                           "Code' (H), first recognized by August Klostermann in 1877. "
                           "Wellhausen dated P to the exilic/post-exilic period (~550-450 BC), "
                           "arguing it was the latest Pentateuchal source. However, Yehezkel "
                           "Kaufmann and Jacob Milgrom challenged this, arguing that many "
                           "Levitical laws reflect pre-exilic, even pre-monarchic, practices. "
                           "Milgrom's magisterial three-volume Anchor Bible commentary (1991-2001) "
                           "makes the case that P is earlier than D (Deuteronomy) and reflects "
                           "genuinely ancient priestly tradition. Israel Knohl ('The Sanctuary of "
                           "Silence,' 1995) distinguishes P (Priestly Torah, older and more "
                           "austere) from H (Holiness School, later and more sermonic). More "
                           "recent scholars (Christophe Nihan, Jeffrey Stackert) see H as a "
                           "redactional layer that shaped the final form of the Pentateuch.",

        "bottom_line": "Whether the legislation originated with Moses at Sinai or represents "
                       "priestly traditions codified over centuries, Leviticus preserves "
                       "Israel's most systematic theology of holiness, sacrifice, and sacred "
                       "space. The debate about dating does not diminish the text's theological "
                       "weight — these are the instructions that defined what it meant for "
                       "Israel to live in the presence of a holy God."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "~1446-1406 BC (Mosaic period, during the year at Sinai between "
                       "Exodus 19 and Numbers 10)",
        "critical_range": "The sacrificial legislation may preserve traditions from the "
                         "pre-monarchic period (1200-1000 BC), with the Holiness Code (H) "
                         "possibly dating to the late monarchy (7th century BC) and the final "
                         "Priestly redaction occurring in the exilic or early post-exilic "
                         "period (~550-450 BC). Milgrom argues that many P laws must predate "
                         "Deuteronomy because D presupposes and modifies them. Comparative "
                         "evidence from Hittite, Mesopotamian, and Ugaritic ritual texts "
                         "shows that the sacrificial system described in Leviticus 1-7 has "
                         "deep roots in Bronze Age cult practice.",
        "evidence": "The sacrificial terminology and ritual procedures in Leviticus find "
                    "close parallels in Ugaritic texts from Ras Shamra (14th-12th century BC): "
                    "the shelamim (peace offering) corresponds to Ugaritic shlmm, the olah "
                    "(burnt offering) to Ugaritic srp, and the specific burnt portions "
                    "(fat, kidneys, liver caudate lobe) match Akkadian extispicy texts. "
                    "The Holiness Code's ethical framework parallels but differs from the "
                    "Laws of Hammurabi and Middle Assyrian Laws. The earliest physical "
                    "manuscript evidence comes from the Dead Sea Scrolls (4QLev-a through "
                    "4QLev-g, 11QpaleoLev, ~250-50 BC)."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Israel — specifically the priests (sons of Aaron) who would "
                            "administer the sacrificial system, and the broader covenant "
                            "community that needed to understand the demands of living in "
                            "proximity to YHWH's holy presence in the tabernacle. If Mosaic, "
                            "the audience is the wilderness generation being trained for "
                            "tabernacle worship. If later, the audience is a community "
                            "seeking to maintain cultic and ethical holiness.",

        "purpose": "Leviticus answers the question that Exodus left open: God has come "
                   "to dwell among his people in the tabernacle (Exodus 40:34-35), but "
                   "how can a holy God live among sinful humans without destroying them? "
                   "Leviticus provides the answer: through sacrifice (chs. 1-7), ordained "
                   "priesthood (chs. 8-10), purity regulations (chs. 11-15), annual "
                   "atonement (ch. 16), blood sanctity (ch. 17), the Holiness Code "
                   "(chs. 18-22), the sacred calendar (ch. 23), and covenant blessings "
                   "and curses (ch. 26). The central command is 'Be holy, for I the LORD "
                   "your God am holy' (Lev 19:2).",

        "theological_intent": "Leviticus is the cosmic architecture of holiness — the "
                             "systematic theology of how the rupture between God and "
                             "humanity (Genesis 3) is managed until it can be fully healed. "
                             "Every offering addresses the fracture between the holy and "
                             "the profane. The sacrificial system is not primitive blood "
                             "magic — it is a divinely ordained mechanism for maintaining "
                             "the intersection of heaven and earth that the tabernacle "
                             "represents. The distinction between clean/unclean, holy/common "
                             "is a pedagogical framework teaching Israel to discern between "
                             "the categories of existence: life and death, order and chaos, "
                             "the way of YHWH and the way of the nations."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) → Aramaic square script (post-exilic)",
        "linguistic_notes": "Leviticus contains highly specialized priestly vocabulary "
                           "that has no parallel elsewhere in the Hebrew Bible: technical "
                           "terms for sacrifice (olah, minchah, shelamim, chattat, asham), "
                           "ritual procedures (semikah — hand-laying, zerikah — blood "
                           "sprinkling, haqtarah — burning on the altar), and purity "
                           "states (tamei, tahor, qadosh). The syntax is predominantly "
                           "casuistic legal prose ('If a person does X, then Y shall be "
                           "done'), characteristic of ANE law codes. The Holiness Code "
                           "(chs. 17-26) shifts to a more hortatory, sermonic style with "
                           "the recurring motivational clause 'I am the LORD your God.' "
                           "11QpaleoLev, written in paleo-Hebrew script, suggests the "
                           "text was transmitted in archaic script traditions even in the "
                           "Second Temple period.",
        "grammar_match": "The Hebrew of Leviticus is consistent with other Torah books "
                        "and with priestly inscriptions from the Iron Age. The sacrificial "
                        "terminology has direct cognates in Ugaritic ritual texts (KTU 1.40, "
                        "1.109, 1.148), confirming deep linguistic roots in Northwest "
                        "Semitic cultic tradition."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "Leviticus IS scripture — it is the theological center of the Torah "
                   "and the foundation of all biblical theology of atonement and holiness.",
        "nt_usage": "The New Testament is saturated with Levitical theology. The entire "
                    "argument of Hebrews depends on the Levitical sacrificial system as "
                    "the 'shadow' of heavenly realities (Heb 8:5, 9:1-10:18). Jesus' "
                    "identification as 'the Lamb of God who takes away the sin of the "
                    "world' (John 1:29) draws on the tamid (daily burnt offering) and "
                    "the Passover lamb, both governed by Levitical law. Paul's doctrine "
                    "of propitiation (hilasterion, Rom 3:25) directly references the "
                    "kapporet (mercy seat/atonement cover) of Leviticus 16. Jesus cites "
                    "Leviticus 19:18 ('Love your neighbor as yourself') as the second "
                    "greatest commandment (Matt 22:39). Peter quotes Leviticus 19:2 in "
                    "1 Peter 1:16. The language of 'clean' and 'unclean' pervades the "
                    "Gospels and Acts.",
        "internal_consistency": "Leviticus bridges Exodus and Numbers seamlessly. The "
                               "tabernacle completed at the end of Exodus (ch. 40) is now "
                               "operational. The priesthood consecrated in Leviticus 8-9 "
                               "serves through Numbers. The purity laws of Leviticus 11-15 "
                               "are presupposed throughout the rest of the Torah and the "
                               "historical books. The festival calendar of Leviticus 23 is "
                               "referenced in every subsequent biblical discussion of Israel's "
                               "worship cycle. Leviticus 26 provides the covenant curses that "
                               "the prophets invoke when Israel disobeys."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments (4QLev-a through 4QLev-g, 11QpaleoLev, "
                    "~250-50 BC) preserve substantial portions of Leviticus. 11QpaleoLev "
                    "is written in the archaic paleo-Hebrew script and contains Leviticus "
                    "4-27, making it one of the most complete Torah manuscripts from Qumran.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. Leviticus in MT is remarkably stable — "
                     "the textual variants between MT and other witnesses are fewer than "
                     "in any other Torah book."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The Greek translation generally follows the Hebrew closely in "
                     "Leviticus, with minor expansions and clarifications of ritual "
                     "procedures. LXX Leviticus is important for understanding how "
                     "sacrificial terminology was rendered for the Greek-speaking world."},
            {"name": "Samaritan Pentateuch (SP)", "date": "Pre-2nd century BC tradition",
             "note": "The Samaritan text of Leviticus closely parallels MT with minor "
                     "orthographic and grammatical differences. The sacrificial legislation "
                     "is virtually identical, suggesting very early stabilization of this "
                     "material."},
            {"name": "Dead Sea Scrolls", "date": "~250 BC - 68 AD",
             "note": "Multiple manuscripts: 4QLev-a (proto-MT), 4QLev-b, 4QLev-d, "
                     "and notably 11QpaleoLev (paleo-Hebrew script, Lev 4-27). The "
                     "DSS texts align closely with MT, confirming early textual "
                     "stabilization of the priestly material."},
            {"name": "Targumim", "date": "1st century BC onward",
             "note": "Targum Onkelos renders Leviticus fairly literally. Targum "
                     "Pseudo-Jonathan adds expansive interpretive material, including "
                     "angelological traditions about the Azazel goat (Lev 16) and "
                     "identifications of purity laws with specific historical events."}
        ],
        "reliability": "Leviticus is among the best-attested books of the Hebrew Bible. "
                       "The ritual and legal content was preserved with exceptional "
                       "precision across all textual traditions, likely because priestly "
                       "communities treated it as operational instructions that could not "
                       "be altered. No significant theological variant exists between "
                       "MT, LXX, SP, and DSS witnesses."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "Leviticus is set entirely at Mount Sinai, during the year-long "
                   "encampment between Exodus 19 and Numbers 10. The legislation is "
                   "presented as direct divine speech from the newly erected tabernacle "
                   "(Lev 1:1). The narrative sections (chs. 8-10, 16, 24:10-23) take "
                   "place in the tabernacle court. The book covers only about one month "
                   "of narrative time but contains the most concentrated body of "
                   "legislation in the Torah.",

        "geography": "The action is entirely at Sinai — the mountain of God where the "
                     "covenant was ratified. The tabernacle is the focal point: its "
                     "altar, laver, Holy Place, and Most Holy Place structure all of "
                     "Leviticus. The 'camp' (machaneh) and the space 'outside the camp' "
                     "are critical spatial categories — the movement between them "
                     "represents transitions between holiness, normalcy, and impurity.",

        "historical_connections": "The sacrificial system in Leviticus has deep parallels "
                                 "in ANE cultic practice. Ugaritic ritual texts (KTU 1.40, "
                                 "1.109, 1.148) describe offerings using cognate terminology: "
                                 "shlmm (peace offerings), srp (burnt offerings), dbh "
                                 "(communion sacrifice). Hittite instructions for temple "
                                 "officials parallel Levitical priestly regulations. The "
                                 "Mesopotamian bit rimki ('bath house') purification ritual "
                                 "and the namburbi (apotropaic rites) parallel the Levitical "
                                 "purification procedures. Egyptian mortuary and temple texts "
                                 "show elaborate purity requirements for priests that parallel "
                                 "Leviticus 21-22. The 'scapegoat' ritual of Leviticus 16 "
                                 "has a striking parallel in Hittite texts where a goat "
                                 "carries away plague to enemy territory."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "high",
        "summary": "Leviticus is critical to the divine council worldview in ways often "
                   "overlooked. The central passage is Leviticus 16:8-10, 20-22: the "
                   "scapegoat sent 'to Azazel' (la'azazel) in the wilderness. In the "
                   "divine council framework, Azazel is not merely a geographical term "
                   "or an adjective meaning 'scapegoat' — it is a personal name. "
                   "1 Enoch 10:4-8 identifies Azazel as a fallen Watcher imprisoned in "
                   "the desert wilderness, the being who taught humanity forbidden "
                   "knowledge (metalworking, cosmetics, weapons of war — 1 Enoch 8:1-2). "
                   "The Day of Atonement ritual symbolically returns sin to the being "
                   "who introduced illicit knowledge to humanity. This is cosmic justice: "
                   "the corruption Azazel seeded is sent back to him. Additionally, the "
                   "blood prohibition of Leviticus 17:10-14 connects to the Watcher "
                   "tradition — the Watchers taught humans to consume blood (1 Enoch 7:5), "
                   "and YHWH explicitly forbids it because 'the life (nephesh) of the "
                   "flesh is in the blood.' The Holiness Code's prohibition of practices "
                   "'the nations do' (Lev 18:3, 24-30; 20:23) echoes the Deuteronomy "
                   "32:8-9 framework: the nations were allotted to lesser 'elohim who "
                   "corrupted them; Israel must not follow their ways. The priestly "
                   "ministry in the tabernacle is the earthly counterpart to the "
                   "heavenly council — the priests serve in a 'copy and shadow' of "
                   "the heavenly throne room (Heb 8:5).",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 25 (Azazel and the Day of Atonement)",
            "Reversing Hermon, chapters 2-3 (1 Enoch Watcher tradition and Azazel)",
            "The Naked Bible Podcast, Episode 95 (Leviticus 16 and Azazel)",
            "Demons, chapter 4 (Azazel as a real entity in Israelite theology)"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "Leviticus Is Not Boring — It Is Cosmic Architecture",
            "body": "Modern readers often skip Leviticus or treat it as an obsolete "
                    "manual of ancient rituals. This is a catastrophic misreading. "
                    "Leviticus is the theological center of the Torah — the manual for "
                    "how heaven and earth interface. Every regulation addresses the "
                    "fundamental problem of the biblical narrative: how can a holy God "
                    "dwell among an unholy people? The sacrificial system, the purity "
                    "laws, the priestly ordination, the Day of Atonement — all of it "
                    "is the solution to the rupture introduced in Genesis 3. Without "
                    "Leviticus, you cannot understand the Cross."
        },
        {
            "type": "scholarship",
            "title": "The P vs. H Debate",
            "body": "Scholars distinguish between the Priestly Torah (P, chs. 1-16) "
                    "and the Holiness Code (H, chs. 17-26), based on differences in "
                    "style, vocabulary, and theological emphasis. P is technical and "
                    "ritual-focused; H is hortatory and motivational. Jacob Milgrom "
                    "argued P is earlier; Israel Knohl reversed this. The relationship "
                    "between P and H remains one of the most debated questions in "
                    "Pentateuchal scholarship. This study presents Leviticus as a "
                    "unified theological work while noting the scholarly distinctions."
        },
        {
            "type": "interpretation",
            "title": "Sacrifice and the Modern Reader",
            "body": "The sacrificial system can seem alien or repugnant to modern "
                    "sensibilities. Three interpretive keys help: (1) Sacrifice is "
                    "the language of the ancient world — God meets Israel where they "
                    "are, using the vocabulary they already understand. (2) The blood "
                    "is not payment to an angry God but the means of purification — "
                    "Milgrom demonstrates that sin is treated as a physical pollutant "
                    "that contaminates the sanctuary, and blood is the ritual detergent. "
                    "(3) The entire system points forward — Hebrews 10:1-4 explicitly "
                    "says animal blood cannot ultimately remove sin; the system is a "
                    "'shadow' pointing to a greater reality."
        }
    ]
}
