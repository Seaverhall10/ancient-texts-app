"""
info.py — Genesis: Scholarly Text Introduction

This file provides the "front page" for Genesis in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?
"""

TEXT_INFO = {
    "text_id": "genesis",
    "display_name": "Genesis (Bereshit)",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical — Old Testament / Torah",
        "detail": "Genesis is universally recognized as canonical scripture by "
                  "Jewish, Catholic, Orthodox, and Protestant traditions. It is "
                  "the first of the five books of the Torah (Pentateuch) and the "
                  "foundation of the entire biblical narrative. No mainstream "
                  "tradition has ever questioned its canonical status."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "Moses, as affirmed by Jewish tradition (Talmud Bava Batra 14b-15a), "
                       "Jesus (John 5:46-47, Mark 10:4-5), and the New Testament authors "
                       "(Luke 24:27, 44). The Torah is consistently called 'the Book of Moses' "
                       "throughout the OT (Joshua 8:31, 2 Kings 14:6, Nehemiah 13:1).",

        "scholarly_debate": "Since the 18th century, critical scholarship has proposed "
                           "that Genesis is a composite work drawing on multiple sources. "
                           "The Documentary Hypothesis (Wellhausen, 1878) identifies four "
                           "strands: J (Yahwist, ~950 BC), E (Elohist, ~850 BC), "
                           "D (Deuteronomist, ~620 BC), and P (Priestly, ~500 BC). "
                           "More recent scholarship (Rendtorff, Blum, Carr) has moved away "
                           "from neat source divisions toward models of supplementation and "
                           "redaction. Conservative scholars (Garrett, Sailhamer, Waltke) "
                           "maintain essential Mosaic authorship with later editorial updates "
                           "(e.g., Genesis 36:31 'before any king reigned over Israel' implies "
                           "a monarchic-era editor, and Genesis 14:14 uses 'Dan' — a name the "
                           "city didn't receive until Judges 18:29).",

        "bottom_line": "Whether Moses wrote the core text and later editors made minor "
                       "updates, or whether the final form reflects centuries of Israelite "
                       "literary tradition, Genesis as we have it is a carefully structured "
                       "theological work with a unified narrative arc. The question of "
                       "authorship does not determine the question of authority — the text "
                       "is what it is regardless of how it reached its final form."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "~1446-1406 BC (Mosaic period, during the wilderness wandering)",
        "critical_range": "The traditions in Genesis may reach back to the 2nd millennium BC "
                         "(patriarchal era), with the text reaching its final form sometime "
                         "between the 10th century BC (united monarchy) and the 5th century BC "
                         "(post-exilic period). The Priestly material is often dated to the "
                         "exilic/post-exilic period (~550-450 BC).",
        "evidence": "The patriarchal narratives reflect customs attested in 2nd millennium "
                    "Mesopotamian texts (Nuzi tablets, Mari letters): adoption practices, "
                    "wife-sister motifs, inheritance customs, treaty forms. This suggests "
                    "genuinely ancient traditions, even if the final literary composition "
                    "is later. The oldest physical manuscript fragments come from the Dead "
                    "Sea Scrolls (4Q1-4Q8, ~250-100 BC)."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Israel — specifically the covenant community receiving their "
                            "identity narrative. If Mosaic, the immediate audience is the "
                            "exodus generation preparing to enter Canaan. If later, the audience "
                            "is Israel needing to understand its origins, its God, and its "
                            "relationship to the surrounding nations.",

        "purpose": "Genesis answers the fundamental questions: Who is God? Who are we? "
                   "Why is the world broken? What is God doing about it? It establishes "
                   "that the God of Israel is the Creator of all things, that humanity bears "
                   "his image, that sin and rebellion (both human and spiritual) have corrupted "
                   "creation, and that God has chosen Abraham's family as the vehicle through "
                   "which he will restore what was lost. Every narrative drives toward the "
                   "Abrahamic covenant: 'In you all families of the earth shall be blessed' "
                   "(Genesis 12:3).",

        "theological_intent": "Genesis is not merely history — it is theological polemic. "
                             "It deliberately counters the worldviews of Egypt (where Israel was "
                             "enslaved) and Mesopotamia (where Israel's ancestors originated). "
                             "The sun is not a god — it's a lamp God made. The sea is not a "
                             "chaos deity — it's water God contained. Humanity is not created "
                             "as slave labor for the gods — humans are image-bearers commissioned "
                             "to rule. This is revolutionary theology in its ancient context."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) → Aramaic square script (post-exilic, "
                  "which is what modern Hebrew uses)",
        "linguistic_notes": "Genesis contains some of the oldest Hebrew prose in the Bible. "
                           "Linguistic features include: archaic verb forms, vocabulary shared "
                           "with Ugaritic and Akkadian, and grammatical constructions consistent "
                           "with early Northwest Semitic. The 'Song of Lamech' (4:23-24) and "
                           "the 'Blessing of Jacob' (49:1-27) are particularly archaic in their "
                           "poetry. Some Aramaisms appear (especially in later chapters), which "
                           "some scholars attribute to post-exilic editing and others to natural "
                           "bilingual influence in the patriarchal Aramean context.",
        "grammar_match": "The Hebrew of Genesis is consistent with other Torah books and with "
                        "what we know of Iron Age Hebrew from inscriptions (Gezer Calendar, "
                        "Siloam Inscription, Lachish Letters). The prose style matches the "
                        "conventions of ancient Near Eastern historical-theological narrative."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "Genesis IS scripture — it is the foundation on which all subsequent "
                   "revelation builds.",
        "nt_usage": "The New Testament quotes or alludes to Genesis over 200 times. Jesus "
                    "cites Genesis as authoritative on marriage (Matt 19:4-6 → Gen 1:27, 2:24), "
                    "on Abel's murder (Matt 23:35 → Gen 4), on Noah's flood (Matt 24:37-39 → "
                    "Gen 6-9), on Abraham (John 8:56 → Gen 12-22), and on Sodom (Luke 17:28-32 "
                    "→ Gen 19). Paul builds his entire theology of sin and redemption on Genesis "
                    "(Romans 5:12-21 → Gen 3; Galatians 3:8 → Gen 12:3). Hebrews 11 treats the "
                    "Genesis patriarchs as historical figures of faith.",
        "internal_consistency": "Genesis establishes themes that run through the entire Bible: "
                               "creation-fall-redemption, seed of the woman vs. seed of the serpent "
                               "(3:15), covenant promise, chosen line, exile and return, the presence "
                               "of God with his people. These threads are picked up in Exodus, "
                               "developed through the prophets, and resolved in the New Testament."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments (4Q1-4Q8, ~250-100 BC) preserve portions "
                    "of every chapter of Genesis. The oldest substantial manuscript is "
                    "4QGenesis-Exod^a (4Q1), dating to approximately 250-200 BC.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text behind most English translations (ESV, NASB, etc.)"},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "Greek translation made in Alexandria; has variant readings, especially "
                     "in genealogies (Genesis 5, 11) and in Genesis 4:8 (adds 'Let us go out to the field')"},
            {"name": "Samaritan Pentateuch (SP)", "date": "Pre-2nd century BC tradition",
             "note": "Independent Hebrew text tradition preserved by the Samaritan community; "
                     "differs in ~6000 places from MT, mostly minor, but significant in Deut 27 "
                     "(Mount Gerizim vs. Mount Ebal)"},
            {"name": "Dead Sea Scrolls", "date": "~250 BC - 68 AD",
             "note": "33+ fragments of Genesis from Qumran; some align with MT, some with LXX, "
                     "some with SP — proving the text was not yet standardized in the Second Temple period"},
            {"name": "Targumim", "date": "1st century BC onward",
             "note": "Aramaic translations/paraphrases (Targum Onkelos, Targum Pseudo-Jonathan) "
                     "that contain interpretive expansions revealing how Genesis was understood in "
                     "the synagogue"}
        ],
        "reliability": "Genesis is exceptionally well-attested. The MT, LXX, SP, and DSS all "
                       "substantially agree on the narrative content. Differences are primarily "
                       "in chronological numbers (the ages in Genesis 5 and 11 differ across "
                       "text traditions) and minor expansions. No major doctrine depends on a "
                       "textual variant."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "Genesis spans from creation to Israel's descent into Egypt (~1876 BC by "
                   "traditional chronology). The patriarchal narratives (chs. 12-50) are set "
                   "in the Middle Bronze Age (2000-1550 BC) in the Fertile Crescent: "
                   "Mesopotamia (Ur, Haran), Canaan (Shechem, Hebron, Beer-sheba, Bethel), "
                   "Egypt, and the Transjordan.",

        "geography": "The action moves from Mesopotamia (Eden, Babel) through Canaan "
                     "(Abraham's journeys, Jacob's travels) to Egypt (Joseph's story). "
                     "Key sites: Ur of the Chaldees → Haran → Shechem → Bethel → Hebron → "
                     "Beer-sheba → Egypt (Goshen). Mount Moriah (the binding of Isaac) is "
                     "identified with Jerusalem's Temple Mount in 2 Chronicles 3:1.",

        "historical_connections": "Patriarchal customs match 2nd millennium Mesopotamian "
                                 "texts: the Nuzi tablets attest adoption, surrogate motherhood, "
                                 "and inheritance practices parallel to Abraham-Sarah-Hagar. The "
                                 "Treaty of Kadesh and Hittite suzerainty treaties illuminate the "
                                 "covenant forms in Genesis 15 and 17. The Ebla tablets (2400 BC) "
                                 "mention cities and personal names consistent with the Genesis "
                                 "patriarchal world. The 'Beni Hasan' tomb painting (1900 BC, Egypt) "
                                 "depicts Semitic traders entering Egypt — the visual world of "
                                 "Abraham's journey to Egypt."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "high",
        "summary": "Genesis is foundational to the divine council worldview. Key passages: "
                   "Genesis 1:26 ('Let US make man in OUR image' — God addressing the council), "
                   "Genesis 3:5 and 3:22 ('knowing good and evil like US/one of US'), "
                   "Genesis 6:1-4 (b'nei 'elohim descending to take human wives — the Watchers), "
                   "Genesis 11:7 ('Let US go down and confuse their language'), "
                   "Genesis 18-19 (YHWH appearing with two angelic beings). "
                   "Michael Heiser argues that Genesis cannot be properly understood without "
                   "the divine council framework — it is the backdrop against which the entire "
                   "narrative operates. The 'sons of God' in Genesis 6 are divine council "
                   "members who rebelled, and the Table of Nations (Genesis 10) combined with "
                   "Deuteronomy 32:8-9 shows that God divided the nations among these beings, "
                   "keeping Israel for himself.",

        "key_heiser_refs": [
            "The Unseen Realm, chapters 1-14 (Genesis material)",
            "Supernatural, chapters 3-9",
            "Reversing Hermon, chapters 1-5 (Genesis 6 + 1 Enoch connection)",
            "The Naked Bible Podcast, episodes on Genesis 1-11 especially"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "Ancient Text, Modern Questions",
            "body": "Genesis was written in and for an ancient Near Eastern context. It answers "
                    "the questions its original audience was asking — Who made us? Why do we "
                    "suffer? Why is our God different from the gods of Egypt and Babylon? — not "
                    "the questions modern Western readers bring to it. Reading Genesis well means "
                    "learning to hear it in its own world before applying it to ours."
        },
        {
            "type": "scholarship",
            "title": "The Authorship Question",
            "body": "You will encounter scholars who confidently assign Genesis passages to "
                    "'J', 'E', or 'P' sources. You will also encounter scholars who defend "
                    "Mosaic authorship just as confidently. The evidence is genuinely complex. "
                    "This study presents the major views honestly without forcing a conclusion. "
                    "The authority and message of Genesis do not depend on resolving this debate."
        },
        {
            "type": "interpretation",
            "title": "Genesis 1-11 and Genre",
            "body": "The genre of Genesis 1-11 is debated: strict historical narrative, "
                    "theological history, polemic literature, or 'mytho-history' (real events "
                    "told through the literary conventions of the ancient world). Faithful "
                    "Christians hold different views on this. What is not debated is the "
                    "theological content: God is the sole Creator, humanity bears his image, "
                    "sin has cosmic consequences, and God has a plan to redeem."
        }
    ]
}
