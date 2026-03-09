"""
info.py -- Proverbs (Mishlei): Scholarly Text Introduction

This file provides the "front page" for Proverbs in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Proverbs is the foundational wisdom text of the Hebrew Bible -- the practical
companion to Job's theodicy and Ecclesiastes' existential probing. Its most
theologically significant contribution is the personification of Wisdom (Hokhmah)
as a divine figure present at creation (8:22-31), calling from the gates of the
city (1:20-21; 8:1-3), and offering life to all who heed her voice. In the
divine council framework, Lady Wisdom is the mediating agent between YHWH's
cosmic governance and human life on earth. The book also establishes the
foundational axiom of all wisdom theology: "The fear of YHWH is the beginning
of knowledge" (1:7) -- true wisdom begins not with investigation but with
reverence before the Creator and his council.
"""

TEXT_INFO = {
    "text_id": "proverbs",
    "display_name": "Proverbs (Mishlei)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "Proverbs is universally recognized as canonical by all Jewish and Christian traditions. "
                  "In the Hebrew Bible it is placed in the Writings (Ketuvim), typically after Psalms and "
                  "Job (or between them, depending on the tradition). In the Christian Old Testament, it "
                  "follows Psalms in the poetic/wisdom section. The New Testament draws heavily on Proverbs: "
                  "Romans 12:20 quotes Proverbs 25:21-22 ('if your enemy is hungry, feed him'); Hebrews "
                  "12:5-6 quotes Proverbs 3:11-12 ('the Lord disciplines the one he loves'); James 4:6 and "
                  "1 Peter 5:5 both quote Proverbs 3:34 ('God opposes the proud but gives grace to the "
                  "humble'); and the Wisdom christology of John 1:1-3, Colossians 1:15-17, and 1 Corinthians "
                  "1:24, 30 draws on the personified Wisdom of Proverbs 8. Jesus himself frequently taught "
                  "in proverbial form (mashal), standing in the wisdom tradition Proverbs represents."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The superscriptions attribute the bulk of Proverbs to Solomon: 'The proverbs of "
                       "Solomon, son of David, king of Israel' (1:1); 'The proverbs of Solomon' (10:1); "
                       "'These also are proverbs of Solomon which the men of Hezekiah king of Judah copied "
                       "out' (25:1). Additional sections are attributed to 'the wise' (22:17; 24:23), "
                       "'Agur son of Jakeh' (30:1), and 'King Lemuel' (31:1). 1 Kings 4:32 states that "
                       "Solomon 'spoke 3,000 proverbs,' of which the current book preserves a curated "
                       "selection. The 'men of Hezekiah' reference (25:1) indicates an editorial process "
                       "extending at least to the 8th-7th century BC.",

        "scholarly_debate": "Critical scholarship recognizes Proverbs as a multi-author, multi-period "
                           "anthology compiled over centuries. The literary structure suggests identifiable "
                           "collections: (1) chapters 1-9, the 'prologue' with extended discourses on Wisdom "
                           "and Folly, often dated to the post-exilic period due to theological sophistication; "
                           "(2) 10:1-22:16, the main Solomonic collection of individual two-line proverbs; "
                           "(3) 22:17-24:22, the 'Words of the Wise,' closely paralleling the Egyptian "
                           "'Instruction of Amenemope' (~1200 BC); (4) 24:23-34, more sayings of the wise; "
                           "(5) 25-29, the Hezekiah collection of Solomonic proverbs; (6) 30, the words of "
                           "Agur; (7) 31:1-9, the words of Lemuel; (8) 31:10-31, the acrostic poem on the "
                           "valiant woman. Solomonic authorship of the core collections (10-22:16; 25-29) is "
                           "widely accepted even by critical scholars, though the final compilation is dated "
                           "to the post-exilic period (~5th-4th century BC).",

        "bottom_line": "Proverbs is the product of Israel's wisdom tradition, anchored in Solomon's court "
                       "but enriched by centuries of sage reflection, international wisdom exchange, and "
                       "theological development. The attribution to Solomon is not merely honorific -- it "
                       "identifies the book with the wisdom tradition he inaugurated and that continued "
                       "under royal patronage. The final form is a carefully structured anthology that "
                       "moves from theological foundation (1-9) through practical application (10-29) to "
                       "portrait of the ideal (30-31)."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Solomon's reign (~970-930 BC) for the core material, with the Hezekiah collection "
                       "edited ~700 BC and final compilation during or after the exile (~6th-5th century BC).",
        "critical_range": "Individual proverbs may originate from the 10th century BC (Solomonic court). "
                         "The 'Words of the Wise' (22:17-24:22) reflect contact with the Egyptian "
                         "'Instruction of Amenemope' (~1200 BC), suggesting awareness of international "
                         "wisdom traditions. Chapters 1-9 are often dated to the post-exilic period "
                         "(5th-4th century BC) due to their developed theology of personified Wisdom. "
                         "Final compilation: ~450-300 BC.",
        "evidence": "Key evidence includes: (1) The 'men of Hezekiah' superscription (25:1) provides an "
                    "internal date for part of the editorial process (~700 BC). (2) The close parallel "
                    "between Proverbs 22:17-23:11 and the Egyptian 'Instruction of Amenemope' demonstrates "
                    "international wisdom exchange. (3) Dead Sea Scrolls fragments (4QProverbs^a, 4QProverbs^b) "
                    "date to the 1st century BC and generally align with the MT. (4) The Septuagint of "
                    "Proverbs differs significantly in arrangement from the MT -- particularly in chapters "
                    "24-31, where the order of collections is rearranged -- suggesting the book's arrangement "
                    "was not fully fixed when the LXX translation was made (~2nd century BC). (5) Ben Sira "
                    "(Sirach, ~180 BC) extensively draws on and develops Proverbs' themes, confirming the "
                    "book's authority by the early 2nd century BC."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Multiple audiences are addressed. Chapters 1-9 address 'my son' (beni) -- "
                            "a young man being initiated into the wisdom tradition, either a royal student "
                            "in the court school or a son receiving parental instruction. The proverb "
                            "collections (10-29) address the broader community of the wise. The Lemuel "
                            "oracle (31:1-9) is a queen mother's instruction to her royal son. The "
                            "valiant woman poem (31:10-31) may address a young man seeking a wife or "
                            "celebrate wisdom personified as the ideal partner.",

        "purpose": "Proverbs teaches the art of living well before God -- the practical application of "
                   "covenant theology to everyday decisions. Its purpose is stated explicitly in the "
                   "prologue: 'To know wisdom and instruction, to understand words of insight, to "
                   "receive instruction in wise dealing, in righteousness, justice, and equity; to give "
                   "prudence to the simple, knowledge and discretion to the youth' (1:2-4). The book "
                   "insists that wisdom is not abstract philosophy but skill for living: moral, social, "
                   "economic, relational, and theological competence.",

        "theological_intent": "Proverbs makes a radical theological claim: the God who created the cosmos "
                             "has embedded wisdom into the fabric of reality, and human beings can access "
                             "that wisdom through reverence ('the fear of YHWH') and diligent observation. "
                             "The personification of Wisdom in chapters 1-9 elevates this claim to cosmic "
                             "proportions: Wisdom was present at creation (8:22-31), was YHWH's 'craftsman' "
                             "(or 'daily delight,' 8:30), and now calls to humanity from every corner of the "
                             "city. To reject Wisdom is to reject the ordering principle of the universe "
                             "itself. The New Testament identifies this personified Wisdom with Christ "
                             "(1 Corinthians 1:24, 30; Colossians 1:15-17; John 1:1-3)."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "Proverbs employs the full range of Hebrew poetic devices: synonymous "
                           "parallelism ('A wise son makes a glad father / but a foolish son is a sorrow "
                           "to his mother,' 10:1), antithetical parallelism ('Treasures gained by wickedness "
                           "do not profit / but righteousness delivers from death,' 10:2), and synthetic "
                           "parallelism. The Hebrew term 'mashal' (proverb) literally means a comparison "
                           "or similitude -- wisdom by analogy. The book's vocabulary is rich in moral "
                           "terminology: hokhmah (wisdom), binah (understanding), musar (discipline/ "
                           "instruction), da'at (knowledge), tushiyyah (sound wisdom), mezimmah "
                           "(discretion), ormah (prudence). The 'Words of Agur' (chapter 30) contain "
                           "some of the most enigmatic Hebrew in the Bible, including possible Aramaisms "
                           "or North Arabian linguistic features. The Proverbs 31 acrostic uses each "
                           "successive letter of the Hebrew alphabet to structure its portrait of the "
                           "valiant woman.",
        "grammar_match": "The proverb collections (10-29) use primarily two-line (distich) proverbs "
                        "with tight, balanced parallelism -- the most concentrated expression of Hebrew "
                        "poetic wisdom. The discourses (1-9) use longer, flowing speeches with extended "
                        "metaphors and personification. The numerical sayings in chapter 30 ('Three "
                        "things... four...') represent a distinct literary sub-genre attested elsewhere in "
                        "the ANE."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Proverbs IS scripture -- the practical wisdom companion to the Torah, prophets, and "
                   "psalms, and the source of the Wisdom christology the New Testament develops.",
        "nt_usage": "The New Testament draws on Proverbs extensively. Direct quotations include: "
                    "Proverbs 3:11-12 in Hebrews 12:5-6 (divine discipline); Proverbs 3:34 in James 4:6 "
                    "and 1 Peter 5:5 ('God opposes the proud but gives grace to the humble'); Proverbs "
                    "25:21-22 in Romans 12:20 (feeding your enemy); Proverbs 26:11 in 2 Peter 2:22 ('a "
                    "dog returns to its vomit'). Beyond direct quotation, the Wisdom christology of the "
                    "New Testament is built on Proverbs 8: John 1:1-3 (the Logos who was 'in the "
                    "beginning' with God and through whom 'all things were made') mirrors Wisdom's "
                    "presence at creation in Proverbs 8:22-31. Colossians 1:15-17 (Christ as 'the "
                    "firstborn of all creation' through whom 'all things were created') develops the "
                    "same theme. 1 Corinthians 1:24, 30 directly identifies Christ as 'the wisdom of "
                    "God.'",
        "internal_consistency": "Proverbs is deeply connected to the rest of the Hebrew Bible. Its "
                               "creation theology (8:22-31) presupposes Genesis 1-2. Its retribution "
                               "principle ('the righteous prosper, the wicked perish') is the same "
                               "theology Deuteronomy articulates, that Job challenges, and that "
                               "Ecclesiastes qualifies. The 'fear of YHWH' axiom (1:7; 9:10; 15:33) "
                               "connects to Deuteronomy's covenant theology. The personification of "
                               "Wisdom anticipates the prophetic Servant and the Johannine Logos."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: 4QProverbs^a (4Q102) and 4QProverbs^b (4Q103), "
                    "dating to the 1st century BC. These fragments cover portions of chapters 1-2 "
                    "and 14-15 and generally align with the MT.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. Proverbs' MT is generally well-preserved, though some "
                     "individual verses are textually uncertain due to the compressed poetic style."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC translation",
             "note": "The LXX of Proverbs is one of the most freely translated books in the Greek "
                     "Bible. The order of sections in chapters 24-31 differs significantly from the MT: "
                     "the collections are rearranged, suggesting the book's arrangement was still fluid "
                     "when the translation was made. The LXX also adds several proverbs not found in "
                     "the MT and omits others."},
            {"name": "Peshitta (Syriac)", "date": "2nd-3rd century AD",
             "note": "The Syriac translation generally follows the MT arrangement and provides "
                     "useful variants for textually difficult passages."},
            {"name": "Vulgate (Latin)", "date": "Jerome, ~405 AD",
             "note": "Jerome's translation from the Hebrew. His rendering of Proverbs 8:22 -- "
                     "'The Lord possessed me (possedit me) at the beginning of his work' -- became "
                     "central to the Arian controversy about whether Christ (identified with Wisdom) "
                     "was created or eternal."}
        ],
        "reliability": "Proverbs is well-attested in the major witnesses, though the LXX's different "
                       "arrangement of the later collections shows that the book's final structure was "
                       "not universally fixed until relatively late. Individual proverbs are generally "
                       "stable across traditions. The theologically crucial passages -- the personification "
                       "of Wisdom (1-9), the 'fear of YHWH' sayings, and the creation poem (8:22-31) -- "
                       "are textually secure."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Proverbs is rooted in the royal court of Jerusalem, particularly the Solomonic era "
                   "(10th century BC). Solomon's court was a center of international wisdom exchange: "
                   "1 Kings 4:30-31 claims his wisdom 'surpassed the wisdom of all the people of the "
                   "east and all the wisdom of Egypt.' The 'men of Hezekiah' (25:1) locate a second "
                   "editorial stage in the late 8th century BC, when Hezekiah's scribes compiled and "
                   "transmitted Solomonic traditions. The final compilation probably occurred in the "
                   "post-exilic period, when Israel's sages gathered and organized the accumulated "
                   "wisdom traditions.",

        "geography": "Proverbs' setting is urban rather than pastoral -- the city gate (1:21; 8:3; "
                     "31:23), the marketplace, the house, and the road. The international wisdom "
                     "connections extend to Egypt (the Amenemope parallel), Arabia (Agur and Lemuel "
                     "may be Arabian sages), and Mesopotamia (shared wisdom motifs).",

        "historical_connections": "The parallel between Proverbs 22:17-23:11 and the Egyptian 'Instruction "
                                 "of Amenemope' (~1200 BC) is the most striking external connection. "
                                 "Amenemope's 'thirty sayings' correspond to the 'thirty sayings' of "
                                 "Proverbs 22:20 (emending 'excellent things' to 'thirty'). Both texts "
                                 "address similar topics in similar order: honest weights, respect for "
                                 "boundaries, care for the poor, avoidance of the hot-tempered. Whether "
                                 "Proverbs borrows from Amenemope, both draw from a common ANE wisdom pool, "
                                 "or Amenemope borrows from an earlier Israelite source is debated. The "
                                 "Babylonian 'Counsels of Wisdom' and the Sumerian 'Instructions of Shuruppak' "
                                 "provide additional parallels, confirming that Israel's wisdom literature "
                                 "participated in a broad ANE intellectual tradition."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "high",
        "summary": "Proverbs' divine council significance centers on the personification of Wisdom "
                   "(Hokhmah) in chapters 1-9, particularly the creation poem of 8:22-31."
                   "\n\n"
                   "WISDOM AT CREATION (Proverbs 8:22-31): 'YHWH possessed me (qanani) at the "
                   "beginning of his work, the first of his acts of old. Ages ago I was set up "
                   "(nissakhti), at the first, before the beginning of the earth... When he established "
                   "the heavens, I was there; when he drew a circle on the face of the deep... then I "
                   "was beside him, like a master workman (amon); and I was daily his delight, rejoicing "
                   "before him always, rejoicing in his inhabited world and delighting in the children "
                   "of man' (8:22-23, 27, 30-31). The verb 'qanani' can mean 'created me,' 'possessed "
                   "me,' or 'acquired me' -- the ambiguity was central to the Arian controversy (4th "
                   "century AD) about whether Christ-Wisdom was created or eternally begotten. The term "
                   "'amon' is equally debated: 'master workman' (Wisdom as God's architect), 'nursling' "
                   "(Wisdom as God's child), or 'constantly' (Wisdom as God's constant companion). In "
                   "the divine council framework, Wisdom is YHWH's own attribute personified as a "
                   "figure who participates in the council's creative work and then calls to humanity "
                   "to embrace the order that was built into creation."
                   "\n\n"
                   "WISDOM AS DIVINE COUNCIL MEDIATOR: Lady Wisdom stands at the crossroads and city "
                   "gates (1:20-21; 8:1-3; 9:1-6), calling to humanity. She offers 'life' (8:35), "
                   "'favor from YHWH' (8:35), knowledge, and understanding. She is not merely a "
                   "teacher but a cosmic figure: 'By me kings reign, and rulers decree what is just; "
                   "by me princes rule, and nobles, all who govern justly' (8:15-16). In the "
                   "Deuteronomy 32 framework, the nations are governed by divine council members "
                   "allotted by YHWH. Wisdom claims authority over this governance structure. She "
                   "mediates between YHWH's cosmic order and human society. The contrast with Woman "
                   "Folly (9:13-18) represents the choice between YHWH's order and the chaos of "
                   "rebellion."
                   "\n\n"
                   "CHRISTOLOGICAL DEVELOPMENT: The New Testament identifies the personified Wisdom "
                   "of Proverbs 8 with Christ. John 1:1-3 echoes Proverbs 8:22-31: the Logos was "
                   "'in the beginning' with God and 'all things were made through him.' Colossians "
                   "1:15-17 mirrors the creation language: Christ is 'the firstborn of all creation' "
                   "and 'in him all things hold together.' 1 Corinthians 1:24, 30 directly calls "
                   "Christ 'the wisdom of God.' This identification means that the Wisdom calling "
                   "from the gates in Proverbs is a pre-incarnate revelation of the Son -- the divine "
                   "council member who was with YHWH at creation and through whom all things were made.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 4-5 (the 'two powers in heaven' -- Wisdom/Logos theology)",
            "The Unseen Realm, chapter 27-28 (the Wisdom-Christ connection)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 4 (Wisdom as a divine attribute personified)",
            "The Naked Bible Podcast, episodes on Proverbs 8 and Wisdom christology"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "Proverbs 8:22-31 -- Wisdom at Creation and the Christ Connection",
            "body": "Proverbs 8:22-31 is one of the most theologically consequential passages in the "
                    "Old Testament. The personified Wisdom describes her presence with YHWH before and "
                    "during creation. The early church fathers identified this Wisdom with the pre-incarnate "
                    "Christ (the Logos of John 1), but the Arian heresy (4th century) used the verb 'qanani' "
                    "('created/possessed me,' 8:22) to argue that Christ was a created being. The Council "
                    "of Nicaea (325 AD) and subsequent councils affirmed that the Wisdom of Proverbs 8 is "
                    "the eternally begotten Son, not a created intermediary. In the divine council framework, "
                    "Wisdom is YHWH's own creative intelligence personified -- the agent through whom the "
                    "cosmos was ordered and who now calls humanity to participate in that order."
        },
        {
            "type": "interpretation",
            "title": "Proverbs and the Retribution Principle",
            "body": "Proverbs generally teaches that righteousness leads to prosperity and wickedness to "
                    "ruin. This 'retribution principle' is stated repeatedly: 'The righteous is delivered "
                    "from trouble, and the wicked walks into it instead' (11:8). But Proverbs presents "
                    "this as a general principle, not an ironclad law. The book itself acknowledges "
                    "exceptions ('A rich man's wealth is his strong city,' 10:15 -- wealth provides "
                    "security regardless of moral character). Job and Ecclesiastes exist precisely to "
                    "qualify the retribution principle: Job shows it fails in individual cases; "
                    "Ecclesiastes shows it fails to account for life's absurdity. Reading Proverbs in "
                    "isolation from Job and Ecclesiastes produces dangerous oversimplification."
        },
        {
            "type": "context",
            "title": "The Valiant Woman of Proverbs 31",
            "body": "Proverbs 31:10-31 is the famous acrostic poem about the 'eshet chayil' -- literally "
                    "'woman of strength/valor.' The same word 'chayil' describes warriors (2 Samuel "
                    "23:20) and Ruth (Ruth 3:11). This is not a poem about domesticity but about "
                    "competence, strength, and wisdom in action. The woman manages a household economy, "
                    "trades in real estate (31:16), runs a textile business (31:24), provides for the "
                    "poor (31:20), and speaks with wisdom (31:26). Many scholars see the poem as a "
                    "literary portrait of Lady Wisdom herself -- the personified Wisdom of chapters 1-9 "
                    "incarnated in a real human life. The book thus ends where it began: with Wisdom "
                    "calling out, now embodied in a woman whose 'fear of YHWH' (31:30) fulfills the "
                    "axiom of 1:7."
        }
    ]
}
