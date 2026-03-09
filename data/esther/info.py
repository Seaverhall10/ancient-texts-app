"""
info.py -- Esther: Scholarly Text Introduction

This file provides the "front page" for Esther in the Ancient Texts Library.
Esther is unique among biblical books: God is never mentioned by name. Yet
divine providence saturates every page. The "coincidences" that save the
Jewish people from Haman's genocide are so precisely orchestrated that the
invisible hand of YHWH is more evident in its absence than in explicit
reference. Esther provides the origin story of Purim and explores Jewish
identity, divine hiddenness, and the survival of God's people in diaspora.
"""

TEXT_INFO = {
    "text_id": "esther",
    "display_name": "Esther",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim) / Megillot",
        "detail": "Esther is canonical in Jewish, Catholic, Orthodox, and Protestant traditions, "
                  "though its canonicity was debated more than most books. The Talmud (Megillah 7a) "
                  "records debates about whether Esther 'defiles the hands' (i.e., is sacred). In "
                  "the Hebrew Bible, Esther is one of the Five Megillot (scrolls) read at festivals -- "
                  "Esther is read at Purim. Notably, no fragment of Esther has been found among the "
                  "Dead Sea Scrolls -- the only OT book entirely absent from Qumran. This may reflect "
                  "the Qumran community's non-observance of Purim or their discomfort with a book that "
                  "never mentions God. Martin Luther expressed discomfort with Esther ('I wish it did "
                  "not exist'), but it has remained firmly canonical. The Catholic and Orthodox canons "
                  "include the 'Additions to Esther' (Greek Esther), which add prayers, dream visions, "
                  "and explicit references to God. Protestants treat these additions as Apocrypha."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Unknown. The Talmud (Bava Batra 15a) attributes Esther to the Men of the "
                       "Great Assembly (Anshei Knesset HaGedolah). Some traditions attribute it to "
                       "Mordecai himself, based on 9:20 ('Mordecai recorded these things'). The "
                       "author displays intimate knowledge of Persian court customs, architecture, "
                       "and administration, suggesting either personal experience or excellent sources.",

        "scholarly_debate": "The date and historicity of Esther are debated. The book describes events "
                           "in the reign of Ahasuerus (Xerxes I, 486-465 BC), but no Persian source "
                           "mentions Esther, Mordecai, or Haman. Some scholars read Esther as historical "
                           "narrative set in the Persian court; others as historical fiction or novella "
                           "with a historical setting. The book's knowledge of Persian customs (the postal "
                           "system, the king's gate, the irrevocability of royal decrees, court protocol) "
                           "is remarkably accurate, suggesting either a Persian-period author or excellent "
                           "access to Persian-period sources. The name 'Mordecai' may connect to the "
                           "Babylonian god Marduk, and 'Esther' to Ishtar -- leading some scholars to "
                           "propose mythological origins, though this remains speculative.",

        "bottom_line": "Whether strictly historical or historically-grounded literary art, Esther is "
                       "a masterpiece of narrative theology that demonstrates divine providence without "
                       "ever naming God. Its theology of hiddenness -- that God works behind the scenes "
                       "of apparently secular events -- is profoundly sophisticated."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events are set in the reign of Ahasuerus/Xerxes I (486-465 BC), "
                       "specifically years 3-12 of his reign (~483-474 BC).",
        "critical_range": "The composition date is debated: estimates range from the late Persian "
                         "period (~400-330 BC) to the early Hellenistic period (~330-200 BC). The "
                         "Hebrew of Esther contains Persian loanwords (dat for 'law,' pardes for "
                         "'garden,' pitgam for 'decree') and Late Biblical Hebrew features, consistent "
                         "with a late Persian or early Hellenistic date. The absence from Qumran "
                         "suggests it may have achieved wide acceptance later than other books.",
        "evidence": "Linguistic features, accurate knowledge of Persian customs and administration, "
                    "and the setting in Susa (the winter capital of the Persian Empire) all point to "
                    "a Persian-period origin for the traditions, even if the final literary form is "
                    "somewhat later."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Diaspora Jews living under foreign rule, facing the constant threat "
                            "of antisemitic persecution. Esther answers the question: Can God protect "
                            "his people even when they are scattered, powerless, and living far from "
                            "the temple?",

        "purpose": "Esther serves multiple purposes: (1) providing the origin story and authorization "
                   "for the Feast of Purim (9:20-32); (2) demonstrating that divine providence "
                   "operates even when God is not visibly present; (3) encouraging diaspora Jews "
                   "that their survival is not accidental but providential; (4) exploring the "
                   "theology of Jewish identity -- what does it mean to be God's people when you "
                   "live in Susa rather than Jerusalem?",

        "theological_intent": "The absence of God's name is not a deficiency but a deliberate "
                             "literary strategy. The book demonstrates that YHWH's sovereignty does "
                             "not require visibility. The 'coincidences' are so numerous and precise -- "
                             "Esther becoming queen, Mordecai overhearing the assassination plot, "
                             "the king's insomnia on the right night, Haman entering at the right "
                             "moment -- that the reader is forced to see the invisible hand of God "
                             "orchestrating every detail. Esther teaches that God is most present when "
                             "he seems most absent."
    },

    # -- ORIGINAL LANGUAGE ------------------------------------------------------
    "language": {
        "original": "Late Biblical Hebrew",
        "script": "Aramaic square script",
        "linguistic_notes": "Esther contains more Persian loanwords than any other OT book: dat "
                           "(law/decree), pardes (garden/park), pitgam (edict/decree), genaz (treasury), "
                           "ahashdarpan (satrap). The Hebrew style is vivid, fast-paced, and richly "
                           "detailed -- more literary than the historical prose of Kings or Chronicles. "
                           "The LBH features (syntax, vocabulary) are consistent with Persian-period "
                           "composition. The Additions to Esther (Greek) were composed in Greek and "
                           "have a different literary character from the Hebrew original.",
        "grammar_match": "Consistent with other Late Biblical Hebrew texts, especially Ezra-Nehemiah "
                        "and late Psalms."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Esther IS scripture -- it demonstrates YHWH's providence over his people even "
                   "in exile, even when unnamed.",
        "nt_usage": "Esther is not directly quoted in the New Testament, but its theology of "
                    "providence deeply influences NT thought. Jesus' teaching that God feeds the "
                    "birds and clothes the lilies (Matt 6:26-30) presupposes the same invisible "
                    "providence Esther demonstrates. Paul's confidence that 'in all things God "
                    "works for the good of those who love him' (Rom 8:28) is Esther's theology "
                    "stated explicitly.",
        "internal_consistency": "Esther connects to the broader biblical narrative through the "
                               "Agagite identity of Haman (3:1) -- descended from Agag, king of the "
                               "Amalekites, Israel's ancient enemy (1 Sam 15). The Esther-Haman "
                               "conflict is the latest chapter in the Amalekite war that began in "
                               "Exodus 17 and continued through Saul's failure in 1 Samuel 15."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------------
    "manuscripts": {
        "earliest": "No Hebrew manuscripts of Esther have been found at Qumran -- it is the "
                    "only OT book entirely absent from the Dead Sea Scrolls.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. The MT of Esther does not mention God at all."},
            {"name": "Septuagint (LXX) with Additions", "date": "~2nd-1st century BC",
             "note": "The Greek Esther includes six 'Additions' (A-F): Mordecai's dream, royal "
                     "edicts in full text, prayers of Mordecai and Esther, and Mordecai's "
                     "interpretation of his dream. These additions explicitly mention God and add "
                     "over 100 verses to the book."},
            {"name": "Alpha Text (AT)", "date": "An alternative Greek recension",
             "note": "A shorter Greek version with significant differences from both the MT and "
                     "the standard LXX, attesting a fluid textual tradition."},
            {"name": "Targum Sheni", "date": "6th-7th century AD",
             "note": "An elaborate Aramaic expansion of Esther with extensive midrashic additions, "
                     "showing the rich interpretive tradition surrounding the book."}
        ],
        "reliability": "The Hebrew MT and Greek LXX represent significantly different editions of "
                       "the Esther story. The textual situation is more complex than for most OT "
                       "books. The absence from Qumran means we have no pre-Masoretic Hebrew evidence."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------------
    "historical_context": {
        "setting": "The Persian Empire during the reign of Ahasuerus (Xerxes I, 486-465 BC), "
                   "specifically the winter capital of Susa (Shushan). The events span years 3-12 "
                   "of Xerxes' reign (~483-474 BC).",

        "geography": "Susa (modern Shush, Iran) is the primary setting. The palace complex "
                     "described in Esther -- inner court, outer court, the king's garden, the "
                     "harem -- matches archaeological discoveries at Susa. French excavations at "
                     "Susa (1884-1886 under Dieulafoy, and later) uncovered the apadana (audience "
                     "hall) with columns matching Esther's descriptions.",

        "historical_connections": "Xerxes I is well-attested in Greek and Persian sources. "
                                 "Herodotus describes his lavish feasts (consistent with Esther 1), "
                                 "his anger and impulsiveness (consistent with Esther's portrait), "
                                 "and his 'queen Amestris' (whom some identify with either Vashti "
                                 "or Esther, though this remains debated). The Persepolis Treasury "
                                 "Tablets mention a 'Marduka' (Mordecai?) as an accountant at Susa "
                                 "during Xerxes' reign, though the identification is uncertain."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "low-moderate (implicit rather than explicit)",
        "summary": "Esther never mentions God, angels, or the divine council. Yet its theology of "
                   "providence is a powerful implicit testimony to divine council governance. The "
                   "perfectly orchestrated 'coincidences' that save the Jewish people -- Esther's "
                   "elevation to queen, Mordecai's discovery of the assassination plot, the king's "
                   "insomnia at the exact right moment -- display the invisible hand of YHWH working "
                   "through seemingly natural events. This is how the divine council normally "
                   "operates: not through visible miracles but through the quiet orchestration of "
                   "circumstances. Mordecai's famous statement to Esther -- 'Who knows whether you "
                   "have not come to the kingdom for such a time as this?' (4:14) -- is the "
                   "theology of providence stated as a question. Additionally, Haman's identity "
                   "as an 'Agagite' (3:1) connects the conflict to the ancient war between YHWH "
                   "and Amalek (Exod 17:14-16; Deut 25:17-19; 1 Sam 15). In the divine council "
                   "framework, Amalek represents persistent opposition to YHWH's purposes -- the "
                   "human agents of cosmic rebellion.",

        "key_heiser_refs": [
            "Supernatural, chapter 20 (providence and the hiddenness of God)",
            "The Unseen Realm, chapter 27 (diaspora theology and divine governance of the nations)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "The Absence of God's Name",
            "body": "Esther is the only book of the Hebrew Bible that never mentions God by name. "
                    "This has bothered readers for millennia -- Luther wished it did not exist, the "
                    "Qumran community apparently ignored it, and the Greek translators added extensive "
                    "prayers and divine references. But the absence is the point. Esther shows that "
                    "God does not need to be named to be present. His fingerprints are everywhere -- "
                    "in the timing, the 'coincidences,' the reversals. Some have noted that the "
                    "divine name YHWH appears as an acrostic in four key verses in the Hebrew text "
                    "(1:20, 5:4, 5:13, 7:7), hidden in the first or last letters of consecutive "
                    "words. Whether intentional or coincidental, the symbolism is fitting: God's "
                    "name is hidden in the text just as God's hand is hidden in the story."
        },
        {
            "type": "interpretation",
            "title": "Violence and Vengeance in Esther",
            "body": "The killing of 75,000 enemies (9:16) and the hanging of Haman's ten sons "
                    "trouble modern readers. Context matters: the decree Haman secured authorized "
                    "the complete annihilation of every Jew in the Persian Empire (3:13). The "
                    "counter-decree does not command the Jews to attack but to 'defend their lives' "
                    "(8:11). The violence is defensive, not aggressive, and is set within a world "
                    "where genocide was a real threat. The narrative also emphasizes that the Jews "
                    "'laid no hand on the plunder' (9:10, 15, 16) -- they did not profit from the "
                    "killing. Read within its ancient context, Esther presents the survival of a "
                    "threatened people, not gratuitous violence."
        }
    ]
}
