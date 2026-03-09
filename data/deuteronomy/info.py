"""
info.py — Deuteronomy: Scholarly Text Introduction

This file provides the "front page" for Deuteronomy in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Deuteronomy is THE most important book in the Old Testament for the divine
council worldview. Deuteronomy 32:8-9 is the Rosetta Stone of the entire
supernatural worldview of the Bible.
"""

TEXT_INFO = {
    "text_id": "deuteronomy",
    "display_name": "Deuteronomy (Devarim)",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical — Old Testament / Torah",
        "detail": "Deuteronomy is the fifth and final book of the Torah (Pentateuch), "
                  "universally recognized as canonical scripture by Jewish, Catholic, "
                  "Orthodox, and Protestant traditions. It is the most frequently quoted "
                  "Old Testament book in the New Testament — Jesus cited it more than any "
                  "other book during his temptation (Matt 4:1-11), drawing all three "
                  "responses from Deuteronomy 6-8. The Shema (Deut 6:4-5) is the central "
                  "confession of Judaism and was affirmed by Jesus as the greatest "
                  "commandment (Mark 12:29-30). No mainstream tradition has ever questioned "
                  "its canonical status. In Jewish liturgical practice, Deuteronomy holds "
                  "a uniquely elevated position: the Shema is recited twice daily and is "
                  "inscribed in every mezuzah and tefillin."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "Moses, as affirmed by the book's own claims (Deut 1:1, 5; 31:9, 22, 24), "
                       "Jewish tradition (Talmud Bava Batra 14b-15a), Jesus (Matt 19:7-8; "
                       "Mark 10:3-5; John 5:46-47), and the New Testament (Acts 3:22 citing "
                       "Deut 18:15; Heb 10:28-30 citing Deut 32:35-36). The Talmud records "
                       "that Moses wrote the Torah through Deuteronomy 34:5 ('So Moses the "
                       "servant of the LORD died there'), and Joshua wrote the final eight "
                       "verses describing Moses' death and burial. Deuteronomy presents "
                       "itself as three farewell addresses delivered by Moses on the plains "
                       "of Moab before the conquest of Canaan.",

        "scholarly_debate": "Deuteronomy has been the most debated book in Pentateuchal criticism "
                           "since W.M.L. de Wette (1805) proposed that it was the 'Book of the "
                           "Law' discovered in the temple during Josiah's reform (2 Kings 22-23, "
                           "~621 BC). The Documentary Hypothesis identifies it as the 'D' source, "
                           "composed in the 7th century BC to support centralized worship in "
                           "Jerusalem. More recent scholarship distinguishes between the 'D' "
                           "source proper and a broader 'Deuteronomistic History' (DtrH) that "
                           "extends through Joshua-Kings (Martin Noth, 1943). Conservative "
                           "scholars (Meredith Kline, Kenneth Kitchen, Eugene Merrill) note "
                           "that Deuteronomy's treaty structure closely parallels 2nd millennium "
                           "BC Hittite suzerainty treaties (Preamble, Historical Prologue, "
                           "Stipulations, Blessings/Curses, Witnesses, Deposit) rather than the "
                           "1st millennium Neo-Assyrian treaty form (which lacks the historical "
                           "prologue). This structural argument places the core of Deuteronomy "
                           "in the Late Bronze Age, consistent with Mosaic authorship. The "
                           "discovery of the Esarhaddon vassal treaties (672 BC) complicated "
                           "this picture by showing that Deut 28's curses parallel Neo-Assyrian "
                           "curse formulas, though Kitchen argues these reflect a common ANE "
                           "tradition, not direct borrowing.",

        "bottom_line": "The treaty-structure argument for an early (2nd millennium BC) date "
                       "remains powerful, and the book's self-presentation as Mosaic addresses "
                       "is coherent. Whether Moses delivered these speeches substantially as "
                       "they stand, or whether an authentic Mosaic core was expanded and edited "
                       "over centuries, Deuteronomy is a carefully structured covenant document "
                       "with deep roots in the ancient Near Eastern treaty tradition. The "
                       "theological content — YHWH's exclusive sovereignty, the allotment of "
                       "nations to lesser 'elohim, Israel's unique election, and the covenant "
                       "blessings-and-curses framework — is consistent from beginning to end "
                       "and represents a unified theological vision."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "~1406 BC (end of the wilderness wandering, delivered on the plains "
                       "of Moab just before Moses' death and the conquest of Canaan)",
        "critical_range": "The core traditions may go back to the Mosaic period (13th-15th "
                         "century BC), with the text reaching its final form sometime between "
                         "the 8th century BC (Hezekian reform) and the late 7th century BC "
                         "(Josianic reform, ~621 BC). Some scholars posit a post-exilic "
                         "redaction layer (~550-450 BC) that added the framework and "
                         "connected Deuteronomy to the Deuteronomistic History. The Song of "
                         "Moses (Deut 32) is widely regarded as one of the oldest poems in "
                         "the Bible, with archaic linguistic features predating the monarchy.",
        "evidence": "Key evidence includes: (1) The Hittite suzerainty treaty form (14th-13th "
                    "century BC) matches Deuteronomy's structure far better than 1st millennium "
                    "treaties, supporting an early date for the covenant framework. (2) The "
                    "curses in Deut 28 have parallels to both 2nd millennium Hittite treaties "
                    "and the 7th century BC Esarhaddon vassal treaties, making curse-formula "
                    "dating ambiguous. (3) Linguistic analysis of the Song of Moses (Deut 32) "
                    "identifies archaic morphology and vocabulary consistent with pre-monarchic "
                    "Hebrew poetry. (4) The Dead Sea Scrolls preserve significant Deuteronomy "
                    "manuscripts (4QDeut^a-n, ~250-50 BC), with 4QDeut^j (4Q37) reading 'sons "
                    "of God' (b'nei 'elohim) at 32:8 where the MT has 'sons of Israel' — "
                    "widely regarded as the older reading. (5) The centralization command "
                    "(Deut 12) fits the Josianic reform context but could also reflect an "
                    "original Mosaic principle applied later."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Israel — the second generation standing on the plains of Moab, "
                            "about to cross the Jordan and enter the Promised Land. Their parents "
                            "perished in the wilderness. Moses is about to die. This is his final "
                            "charge to the covenant community: remember who YHWH is, remember what "
                            "he did, and commit to exclusive loyalty when you enter a land full of "
                            "other nations and their gods.",

        "purpose": "Deuteronomy's overarching purpose is covenant renewal. It answers: Why must "
                   "Israel serve YHWH alone? Because he is the Most High (Elyon) who chose Israel "
                   "out of all the nations he allotted to the other 'elohim (Deut 32:8-9). Because "
                   "he redeemed them from Egypt. Because he sustained them in the wilderness. "
                   "The book functions as a suzerainty treaty between the Great King (YHWH) and "
                   "his vassal nation (Israel): it recounts the history of the relationship "
                   "(chapters 1-4), states the terms of the covenant (chapters 5-26), and "
                   "declares the consequences of obedience and rebellion (chapters 27-34). "
                   "It is simultaneously a legal document, a theological treatise, a covenant "
                   "renewal liturgy, and a farewell address.",

        "theological_intent": "Deuteronomy makes the most explicit theological claim in the entire "
                             "Old Testament about the relationship between YHWH and the nations' gods. "
                             "Other 'elohim exist (4:19-20, 29:26, 32:8-9, 32:17, 32:43), but YHWH is "
                             "incomparably supreme. Israel's obligation is not to deny these beings exist "
                             "but to refuse to serve them, because YHWH — not they — redeemed Israel. "
                             "The Shema (6:4) is not an ontological statement about monotheism; it is "
                             "a covenant loyalty oath: 'YHWH is OUR God, YHWH alone.' This makes "
                             "Deuteronomy the charter document for what scholars call 'monolatry' or "
                             "'Yahwistic exclusivism' within a divine council framework."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) → Aramaic square script (post-exilic, "
                  "which is what modern Hebrew uses)",
        "linguistic_notes": "Deuteronomy's prose style is distinctive and recognizable — a "
                           "flowing, hortatory, sermonic Hebrew characterized by long subordinate "
                           "clauses, repetitive phrasing, and emotional rhetorical appeal. Key "
                           "vocabulary clusters mark the book: 'hear/obey' (shema), 'love' (ahav), "
                           "'keep/guard' (shamar), 'heart' (lev/levav), 'choose' (bachar), 'place "
                           "where YHWH will choose to set his name' (Deut 12:5). The Song of Moses "
                           "(Deut 32) is written in archaic Hebrew poetry with pre-monarchic "
                           "linguistic features: archaic pronominal suffixes (-mo instead of -am), "
                           "rare vocabulary shared with Ugaritic, and grammatical forms consistent "
                           "with the earliest stratum of Hebrew verse (comparable to Judges 5 and "
                           "Exodus 15). The Blessing of Moses (Deut 33) similarly preserves archaic "
                           "poetic features. The prose sections show affinities with both early and "
                           "late Hebrew, consistent with an early core that underwent editorial "
                           "updating.",
        "grammar_match": "Deuteronomy's sermonic prose style is unique within the Pentateuch but "
                        "has parallels in later biblical literature influenced by the Deuteronomic "
                        "tradition (Joshua-Kings, Jeremiah). The treaty-form structure is "
                        "consistent with 2nd millennium ANE diplomatic Hebrew/Akkadian conventions. "
                        "The archaic poetry (Deut 32-33) is among the oldest datable Hebrew in "
                        "the Bible, with linguistic features that cannot have been artificially "
                        "created in a later period."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "Deuteronomy IS scripture — it is the covenant charter of Israel and the most "
                   "quoted OT book in the New Testament.",
        "nt_usage": "Deuteronomy is quoted or alluded to approximately 200 times in the New "
                    "Testament, more than any other OT book except Psalms and Isaiah. Jesus quotes "
                    "it three times against Satan (Matt 4:4 → Deut 8:3; Matt 4:7 → Deut 6:16; "
                    "Matt 4:10 → Deut 6:13), identifies the Shema as the greatest commandment "
                    "(Mark 12:29-30 → Deut 6:4-5), and cites it on divorce (Matt 19:7 → Deut 24:1). "
                    "Paul quotes Deuteronomy extensively: the 'word is near you' passage (Rom 10:6-8 "
                    "→ Deut 30:12-14), the Song of Moses (Rom 15:10 → Deut 32:43; Rom 12:19 → "
                    "Deut 32:35), and the curse of hanging on a tree (Gal 3:13 → Deut 21:23). "
                    "Hebrews 1:6 quotes Deut 32:43 (LXX/DSS) to establish Christ's supremacy over "
                    "the angels: 'Let all God's angels worship him.' Acts 3:22-23 and 7:37 identify "
                    "Jesus as the 'Prophet like Moses' of Deut 18:15-19.",
        "internal_consistency": "Deuteronomy's themes — exclusive loyalty to YHWH, covenant "
                               "faithfulness, the centrality of the Promised Land, blessings for "
                               "obedience and curses for disobedience — run through the entire "
                               "Deuteronomistic History (Joshua through Kings) and are echoed in the "
                               "prophets (especially Jeremiah, who shows strong Deuteronomic influence). "
                               "The divine council worldview of Deut 32:8-9 is consistent with "
                               "Daniel 10 (territorial princes), Psalm 82 (God judging the 'elohim), "
                               "and 1 Kings 22 (the heavenly council). The New Testament resolves "
                               "Deuteronomy's tensions: the 'new covenant' of Jeremiah 31 (anticipated "
                               "by Deut 30:6, the circumcision of the heart) is fulfilled in Christ, "
                               "and the territorial allotment of nations to lesser 'elohim is reversed "
                               "at Pentecost (Acts 2), where representatives of all nations receive "
                               "the Spirit — the Great Commission reverses the Deuteronomy 32 allotment."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: Deuteronomy is the most frequently attested "
                    "biblical book at Qumran, with 33 manuscripts (4QDeut^a through 4QDeut^q, "
                    "plus manuscripts from other caves). The most important is 4QDeut^j (4Q37), "
                    "dating to approximately 150-50 BC, which reads 'sons of God' (b'nei 'elohim) "
                    "at Deuteronomy 32:8 — the reading that transforms our understanding of the "
                    "entire divine council worldview. 4QDeut^q (4Q44) preserves a version of "
                    "Deuteronomy 32:43 with additional lines commanding the 'elohim to worship "
                    "YHWH, matching the LXX reading.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text behind most English translations. At Deut 32:8, "
                     "the MT reads 'sons of Israel' (b'nei yisra'el) — a theological alteration "
                     "from the original 'sons of God,' likely made to avoid the implication that "
                     "other divine beings received national allotments."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "Greek translation that reads 'angels of God' (angelon theou) at Deut 32:8, "
                     "independently confirming the 'sons of God' reading against the MT's 'sons "
                     "of Israel.' The LXX Deut 32:43 is significantly longer than the MT, "
                     "including 'Rejoice, O heavens, with him, and let all the sons of God worship "
                     "him' — quoted in Hebrews 1:6."},
            {"name": "Samaritan Pentateuch (SP)", "date": "Pre-2nd century BC tradition",
             "note": "Independent Hebrew text preserved by the Samaritan community. Contains "
                     "significant expansions, particularly the 'tenth commandment' requiring "
                     "an altar on Mount Gerizim (inserted after Exod 20:17 and Deut 5:21). "
                     "The SP reads 'sons of Israel' at 32:8, agreeing with the MT against the "
                     "DSS/LXX — possibly reflecting the same theological correction."},
            {"name": "Dead Sea Scrolls", "date": "~250 BC - 68 AD",
             "note": "33 manuscripts — more than any other biblical book at Qumran. Key readings: "
                     "4QDeut^j has 'sons of God' at 32:8 (older than MT/SP 'sons of Israel'); "
                     "4QDeut^q has the longer version of 32:43 with 'elohim worshipping YHWH. "
                     "Multiple phylactery texts from Qumran contain the Shema (Deut 6:4-9), "
                     "confirming its centrality in Second Temple worship."},
            {"name": "Targumim", "date": "1st century BC onward",
             "note": "Targum Onkelos renders Deut 32:8 as 'according to the number of the "
                     "children of Israel' (following MT). Targum Pseudo-Jonathan, however, reads "
                     "'according to the number of the seventy angels, princes of the nations' — "
                     "preserving the divine council interpretation even while using the MT text. "
                     "This shows that the 'sons of God' reading was known in Jewish interpretive "
                     "tradition regardless of which Hebrew text was used."}
        ],
        "reliability": "Deuteronomy is the best-attested biblical book in the Dead Sea Scrolls "
                       "corpus. The textual tradition is remarkably stable for the vast majority "
                       "of the book. The critical textual issues are concentrated in chapter 32, "
                       "where the DSS and LXX preserve older readings at 32:8 ('sons of God') and "
                       "32:43 (expanded doxology) that have profound theological implications. "
                       "The MT's alteration of 'sons of God' to 'sons of Israel' at 32:8 is now "
                       "recognized by the majority of textual scholars (including those who produced "
                       "the ESV, NRSV, and NJB) as a secondary, theologically motivated change. "
                       "This makes the DSS reading of Deut 32:8 one of the most consequential "
                       "textual variants in the entire Old Testament."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "Deuteronomy is set on the plains of Moab, east of the Jordan River, in the "
                   "final month of Moses' life (~1406 BC by traditional chronology, or the 13th "
                   "century BC by the late-date exodus model). The first generation that left Egypt "
                   "has perished in the wilderness; the second generation stands ready to cross into "
                   "Canaan. Moses cannot enter the land himself (Num 20:12), so he delivers three "
                   "farewell speeches, renewing the covenant, commissioning Joshua as his successor, "
                   "and composing the Song of Moses (chapter 32) as a prophetic witness.",

        "geography": "The plains of Moab overlook the Jordan Valley and Jericho across the river. "
                     "Moses ascends Mount Nebo (Pisgah) to view the Promised Land before his death. "
                     "Key geographic references include: the Arabah (rift valley), the Transjordan "
                     "kingdoms already conquered (Sihon of Heshbon, Og of Bashan), the cities of "
                     "refuge east of the Jordan (Bezer, Ramoth-gilead, Golan), and the land 'from "
                     "Dan to Beer-sheba' that Israel will inherit. The 'place YHWH will choose' "
                     "(Deut 12:5) — later identified as Jerusalem — is deliberately unnamed, "
                     "preserving the forward-looking orientation of Moses' speech.",

        "historical_connections": "Deuteronomy's treaty structure parallels the Hittite suzerainty "
                                 "treaties of the Late Bronze Age (14th-13th century BC), particularly "
                                 "the treaties of Suppiluliuma I and Mursili II. Key elements: the "
                                 "Great King identifies himself (Deut 1:1-5), recounts the history of "
                                 "his benevolence to the vassal (Deut 1-3), states the stipulations of "
                                 "the treaty (Deut 5-26), lists blessings for compliance and curses for "
                                 "violation (Deut 27-28), names witnesses (heaven and earth, Deut 30:19; "
                                 "the Song of Moses, Deut 31:19), and deposits the treaty document "
                                 "(Deut 31:26, in the ark of the covenant). Meredith Kline's 'Treaty "
                                 "of the Great King' (1963) demonstrated these parallels in detail. The "
                                 "Esarhaddon vassal treaties (672 BC) show continuity with the curse "
                                 "tradition but lack the historical prologue that characterizes both "
                                 "Hittite treaties and Deuteronomy."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "critical",
        "summary": "Deuteronomy contains THE foundational text for the entire divine council "
                   "worldview: Deuteronomy 32:8-9. In the Dead Sea Scrolls reading (4QDeut^j), "
                   "confirmed independently by the LXX, this passage reads: 'When the Most High "
                   "(Elyon) gave to the nations their inheritance, when he divided mankind, he "
                   "fixed the borders of the peoples according to the number of the sons of God "
                   "(b'nei 'elohim). But the LORD's (YHWH's) portion is his people, Jacob his "
                   "allotted heritage.' This reveals a cosmic political reality: after the Babel "
                   "event (Gen 11), God allotted the nations of the world to members of his "
                   "divine council — the 'sons of God' — while keeping Israel for himself. "
                   "This is the Rosetta Stone of the supernatural worldview of the Bible. "
                   "\n\n"
                   "Additional key passages: "
                   "(1) Deut 4:19-20 — God allotted the sun, moon, stars, and 'all the host of "
                   "heaven' to the other nations, but took Israel out of Egypt for himself. "
                   "'Host of heaven' is a divine council term (1 Kings 22:19). "
                   "(2) Deut 29:26 — Israel served 'gods that were allotted to them,' using the "
                   "same allotment language as 32:8-9. "
                   "(3) Deut 32:17 — Israel sacrificed to shedim (demons), to gods ('elohim) they "
                   "had not known, to new gods that had come recently. This distinguishes between "
                   "the allotted 'elohim of 32:8 and the shedim — the council members who rule "
                   "nations vs. the lesser spiritual rebels. "
                   "(4) Deut 32:43 (DSS/LXX) — 'Rejoice with him, O heavens; bow down to him, "
                   "all gods ('elohim)' — a command for the divine council to worship YHWH, "
                   "quoted in Hebrews 1:6 as fulfilled when Christ is enthroned. "
                   "(5) Deut 18:15-19 — The Prophet like Moses, fulfilled in Christ (Acts 3:22), "
                   "who will restore the divine council order. "
                   "\n\n"
                   "Michael Heiser considered Deuteronomy 32:8-9 the single most important "
                   "passage in the Old Testament for understanding the spiritual worldview of "
                   "the biblical writers. Without it, Psalm 82, Daniel 10, and the Great "
                   "Commission cannot be properly understood.",

        "key_heiser_refs": [
            "The Unseen Realm, chapters 13-16 (Deuteronomy 32 worldview — the core argument)",
            "Supernatural, chapters 10-13 (the Deuteronomy 32 worldview for lay readers)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 2-3 (shedim in Deut 32:17)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 4-6 (sons of God in Deut 32:8)",
            "The Naked Bible Podcast, episodes 94-97 (Deuteronomy 32 deep dive)",
            "The Naked Bible Podcast, episode 109 (Deuteronomy 4:19-20 and cosmic geography)",
            "'Deuteronomy 32:8 and the Sons of God' — Bibliotheca Sacra 158 (2001): 52-74 (Heiser's academic article)"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "Moses' Farewell — The Weight of Last Words",
            "body": "Deuteronomy is structured as Moses' farewell addresses to Israel. Ancient "
                    "Near Eastern literature treated 'last words' with supreme gravity — they "
                    "carried prophetic and legal force (cf. Jacob's blessings in Genesis 49, "
                    "Joshua's farewell in Joshua 23-24). Moses knows he will die on this mountain. "
                    "Every word is chosen with the urgency of a man who will not get another chance "
                    "to speak. Read Deuteronomy with that weight. This is not legal bureaucracy — "
                    "it is a dying father pleading with his children to remain faithful."
        },
        {
            "type": "scholarship",
            "title": "The Treaty Structure Debate",
            "body": "The form of Deuteronomy is one of the most important debates in OT scholarship. "
                    "If it matches the 2nd millennium Hittite treaty form (as Kline, Kitchen, and "
                    "Merrill argue), this strongly supports an early date and Mosaic authorship. If "
                    "it instead reflects 1st millennium Neo-Assyrian treaty forms (as Weinfeld and "
                    "others argue), this supports the Josianic date. The evidence is genuinely "
                    "complex — Deuteronomy has features of both. This study presents the structural "
                    "parallels honestly and lets the reader evaluate the evidence."
        },
        {
            "type": "interpretation",
            "title": "The Deuteronomy 32:8 Textual Issue",
            "body": "The single most theologically significant textual variant in the entire Old "
                    "Testament is at Deuteronomy 32:8. The Dead Sea Scrolls (4QDeut^j) read 'sons "
                    "of God' (b'nei 'elohim). The Septuagint independently reads 'angels of God.' "
                    "The Masoretic Text reads 'sons of Israel.' Nearly all modern critical scholars "
                    "— and most evangelical textual scholars — regard the DSS/LXX reading as original "
                    "and the MT reading as a later theological correction designed to remove the "
                    "implication that God allotted nations to divine beings. The ESV footnotes this "
                    "reading. The NRSV, NJB, and NET Bible adopt it in the main text. This reading "
                    "is the foundation of the divine council worldview presented in this study."
        },
        {
            "type": "theology",
            "title": "Monolatry, Not Monotheism",
            "body": "Modern readers often bring a post-Enlightenment monotheism to Deuteronomy that "
                    "doesn't fit the text. Deuteronomy does not deny that other 'elohim exist — it "
                    "explicitly affirms their existence (4:19-20, 29:26, 32:8, 32:17, 32:43). What "
                    "it demands is exclusive worship of YHWH. The Shema ('YHWH our God, YHWH is one') "
                    "is a loyalty declaration, not an ontological claim about the non-existence of "
                    "other spiritual beings. This is 'monolatry' — the worship of one God while "
                    "acknowledging the existence of others. It is also the consistent position of "
                    "the entire Bible: the NT affirms 'principalities and powers' (Eph 6:12), "
                    "'thrones and dominions' (Col 1:16), and 'the ruler of this world' (John 12:31) "
                    "while insisting on the supremacy of the one God. Deuteronomy established this "
                    "framework."
        }
    ]
}
