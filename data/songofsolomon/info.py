"""
info.py -- Song of Solomon (Shir HaShirim): Scholarly Text Introduction

This file provides the "front page" for Song of Solomon in the Ancient Texts Library.
The Song of Solomon (Song of Songs) is the Bible's great love poem -- a
celebration of romantic and erotic love between a man and a woman, read by
Jewish and Christian tradition as an allegory of the covenant love between
God and his people. Its explicit language, its absence of overt theology,
and its literary brilliance make it one of the most debated and beautiful
books in the canon. Rabbi Akiva declared: "All the ages are not worth the
day on which the Song of Songs was given to Israel."
"""

TEXT_INFO = {
    "text_id": "songofsolomon",
    "display_name": "Song of Solomon (Shir HaShirim)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim) / Megillot",
        "detail": "Song of Solomon is canonical in Jewish, Catholic, Orthodox, and Protestant "
                  "traditions. In the Hebrew Bible, it is the first of the Five Megillot and is "
                  "read at Passover. Its canonicity was debated in the late first century AD -- "
                  "the Mishnah (Yadayim 3:5) records the debate at Yavneh/Jamnia. Rabbi Akiva's "
                  "passionate defense settled the question: 'The whole world is not worth the day "
                  "on which the Song of Songs was given to Israel, for all the Writings are holy, "
                  "but the Song of Songs is the Holy of Holies.' The allegorical interpretation "
                  "(God's love for Israel, Christ's love for the church) was the primary reason "
                  "for its acceptance and has dominated reception history. The literal reading "
                  "(human love poetry) has always existed alongside the allegorical and has "
                  "gained prominence in modern scholarship."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Solomon, based on the superscription 'The Song of Songs, which is Solomon's' "
                       "(1:1). Solomon is mentioned by name seven times in the book (1:1, 5; 3:7, 9, "
                       "11; 8:11, 12). 1 Kings 4:32 attributes 1,005 songs to Solomon. Jewish tradition "
                       "assigns Song of Songs to Solomon's youth, Proverbs to his maturity, and "
                       "Ecclesiastes to his old age.",

        "scholarly_debate": "The Hebrew phrase lish'lomoh (1:1) can mean 'Solomon's' (authorship), 'for "
                           "Solomon' (dedication), or 'about Solomon' (subject). Linguistic analysis "
                           "reveals Late Biblical Hebrew features (Aramaisms, possible Greek or Persian "
                           "loanwords) that some scholars attribute to a post-exilic date rather than "
                           "Solomon's era. Others argue these features reflect northern Israelite dialect "
                           "rather than late date. The book's unity is debated: is it a single poem, a "
                           "collection of love lyrics, or a liturgical drama? The literary quality is "
                           "consistently high throughout, suggesting either a single brilliant author or "
                           "a carefully edited collection.",

        "bottom_line": "Whether authored by Solomon, dedicated to him, or composed in the Solomonic "
                       "literary tradition, Song of Songs is a masterwork of Hebrew love poetry that "
                       "has been read, sung, and cherished for nearly three millennia. Its place in "
                       "the canon reflects the conviction that human love -- at its best -- reflects "
                       "divine love."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "~970-930 BC (Solomon's reign, 10th century BC)",
        "critical_range": "Estimates range from the 10th century (Solomonic period) to the 3rd century "
                         "BC (Hellenistic period). The Aramaisms and possible late vocabulary suggest a "
                         "post-exilic date to many scholars, but the love poetry itself may preserve "
                         "genuinely ancient traditions. The references to Tirzah (6:4, the early capital "
                         "of the northern kingdom) suggest a pre-722 BC tradition, even if the final "
                         "form is later. The most common scholarly dating is 5th-3rd century BC.",
        "evidence": "The linguistic evidence is debated. Aramaisms could reflect late date or "
                    "northern Israelite dialect. The mention of Tirzah alongside Jerusalem (6:4) "
                    "suggests a period before Tirzah was eclipsed by Samaria (~880 BC). The "
                    "botanical and geographical references (Lebanon, Sharon, En-gedi, Carmel) "
                    "span the entire land of Israel and suggest intimate knowledge of its landscape."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The original setting is debated: was the Song composed for wedding "
                            "celebrations, court entertainment, wisdom instruction, or liturgical "
                            "use? Its inclusion in the Megillot (festival scrolls) and its reading "
                            "at Passover suggest a liturgical context from an early period.",

        "purpose": "The Song celebrates human love and sexuality as good, beautiful, and divinely "
                   "given. In a canonical context, it affirms that the body is not evil, that "
                   "desire is not sin, and that mutual love between a man and a woman reflects "
                   "something of God's own nature. The allegorical tradition adds a second layer: "
                   "the passionate love described between the lovers is an image of the passionate "
                   "love between YHWH and Israel, between Christ and his church.",

        "theological_intent": "The Song answers an unspoken question: Does God care about human love? "
                             "The answer is an emphatic yes. Love is 'strong as death' (8:6), and its "
                             "flame is shalhevet-yah -- a 'flame of the LORD' (8:6, the only possible "
                             "divine name reference in the book). By placing a love poem in the canon, "
                             "Israel declares that human romance and physical love are not worldly "
                             "distractions from the spiritual life but genuine reflections of divine "
                             "reality. The God who IS love (1 John 4:8) made human beings capable of "
                             "love, and the Song celebrates that capacity at its most intense."
    },

    # -- ORIGINAL LANGUAGE ------------------------------------------------------
    "language": {
        "original": "Hebrew (with possible northern dialect features)",
        "script": "Aramaic square script (in extant manuscripts)",
        "linguistic_notes": "The Hebrew of Song of Songs is unique in the OT. It contains rare "
                           "vocabulary found nowhere else in the Bible (hapax legomena), extensive "
                           "nature imagery, and grammatical features that may reflect northern "
                           "Israelite dialect rather than standard Judahite Hebrew. The word "
                           "shalhevet-yah (8:6, 'flame of Yah/the LORD') is the only possible "
                           "divine name in the book -- and even this is debated (some read it as "
                           "simply 'a mighty flame' using the divine name as a superlative). The "
                           "poetry is rich in metaphor, simile, and sensory imagery -- taste, touch, "
                           "smell, sight -- making it the most embodied text in the Hebrew Bible.",
        "grammar_match": "The language has features consistent with both early and late Hebrew, "
                        "contributing to the dating debate. Some Aramaisms may reflect northern "
                        "dialect rather than chronological lateness."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Song of Solomon IS scripture -- it is the canonical celebration of human love "
                   "as a reflection of divine love, and the typological portrait of covenant "
                   "relationship between God and his people.",
        "nt_usage": "The New Testament does not directly quote Song of Solomon but draws heavily "
                    "on its imagery. Paul's extended analogy of Christ and the church as bride and "
                    "groom (Ephesians 5:25-32) reflects the allegorical reading of the Song. The "
                    "parable of the ten virgins (Matt 25:1-13) uses wedding imagery rooted in the "
                    "Song's world. Revelation's 'bride of the Lamb' (Rev 19:7-8; 21:2, 9) is the "
                    "eschatological fulfillment of the love relationship the Song celebrates.",
        "internal_consistency": "The Song connects to Genesis 2:23-25 (the first love poem: 'This "
                               "at last is bone of my bones'), to the prophets' marriage metaphor "
                               "(Hosea 2, Isaiah 54, Ezekiel 16 -- YHWH as Israel's husband), and "
                               "to Proverbs 5:18-19 (rejoicing in the wife of your youth). The Song "
                               "is the positive counterpart to the prophets' lament over Israel's "
                               "'adultery' with other gods."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: 4QCant-a and 4QCant-b (~50 BC-50 AD), "
                    "preserving portions of the text consistent with the MT.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text."},
            {"name": "Septuagint (LXX)", "date": "~2nd century BC",
             "note": "The Greek Asma Asmaton ('Song of Songs'). Follows the MT closely."},
            {"name": "Dead Sea Scrolls", "date": "4QCant-a, 4QCant-b, ~50 BC-50 AD",
             "note": "Fragments consistent with the MT tradition, confirming the text's stability."},
            {"name": "Vulgate", "date": "~400 AD (Jerome)",
             "note": "Jerome translated from the Hebrew. His commentary reflects the allegorical "
                     "tradition: Christ and the church."}
        ],
        "reliability": "The text is well-preserved and consistent across witnesses."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------------
    "historical_context": {
        "setting": "The Song is not set in a specific historical moment but in the landscape of "
                   "love: vineyards, gardens, orchards, mountains, and chambers. Geographic "
                   "references span the entire land of Israel: Lebanon, Hermon, Carmel, Sharon, "
                   "En-gedi, Jerusalem, Tirzah.",

        "geography": "The landscape is lush and pastoral: vineyards (1:6, 8:11-12), gardens "
                     "(4:12-16, 6:2), mountains of spice (8:14), the tower of David (4:4), "
                     "the pools of Heshbon (7:4), the cedars of Lebanon (5:15). The lovers move "
                     "through a world bursting with natural beauty -- the Song is the most "
                     "ecologically rich book in the Bible.",

        "historical_connections": "Love poetry was a major genre in the ancient Near East. "
                                 "Egyptian love songs from the New Kingdom (Chester Beatty Papyrus, "
                                 "Papyrus Harris 500, ~1300-1100 BC) share many features with "
                                 "the Song: the 'brother/sister' address, nature imagery, longing for "
                                 "the absent beloved, and celebration of physical beauty. Sumerian "
                                 "sacred marriage texts (Dumuzi-Inanna poetry) celebrate the union of "
                                 "king and goddess, which some scholars compare to the Song's royal "
                                 "imagery. The Song's uniqueness lies in its mutuality: both lovers "
                                 "speak, both desire, both are valued."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "low",
        "summary": "Song of Solomon does not contain divine council content in the direct sense. "
                   "However, the allegorical reading connects it to the broader theology of "
                   "covenant relationship. If the Song typologically represents YHWH's love for "
                   "Israel and Christ's love for the church, then it speaks to the ultimate "
                   "purpose of the divine council's work: restoring the relationship between God "
                   "and humanity that was broken in Eden. The garden imagery throughout the Song "
                   "(4:12-16, 5:1, 6:2, 8:13) echoes the Garden of Eden -- the original place "
                   "where God walked with humanity. The Song may be read as a vision of Eden "
                   "restored: the barriers broken, the lovers reunited, the garden flourishing. "
                   "The phrase shalhevet-yah ('flame of the LORD,' 8:6) -- if it contains the "
                   "divine name -- identifies the love celebrated in the Song as divine in origin: "
                   "love comes from God, and its most intense expressions reflect his nature.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 6 (Eden as the divine council meeting place; the Song's garden imagery)",
            "Supernatural, chapter 7 (the restoration of divine-human relationship)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "interpretation",
            "title": "Literal, Allegorical, or Both?",
            "body": "Throughout history, Song of Solomon has been read three ways: (1) LITERAL -- "
                    "it celebrates human romantic and sexual love as a God-given good. (2) ALLEGORICAL -- "
                    "in Jewish tradition, it represents YHWH's love for Israel; in Christian tradition, "
                    "Christ's love for the church (or the individual soul). (3) TYPOLOGICAL -- it is "
                    "genuinely about human love AND that human love genuinely reflects divine love. The "
                    "typological reading holds both together: the Song is not 'really' about God and "
                    "'merely' about human love, nor 'merely' about human love with no divine dimension. "
                    "Human love at its best IS an image of divine love. This study honors both dimensions."
        },
        {
            "type": "context",
            "title": "Why at Passover?",
            "body": "Jewish tradition reads Song of Solomon at Passover because the exodus is "
                    "understood as the 'courtship' between YHWH and Israel: 'I will take you to be "
                    "my people, and I will be your God' (Exod 6:7). The covenant at Sinai is the "
                    "'wedding,' and the tabernacle is the 'home' where God and Israel dwell together. "
                    "Reading the Song at Passover connects the most intimate human experience (love) "
                    "to the most foundational divine act (redemption). God redeems because he loves; "
                    "the Song celebrates the love that motivates the redemption."
        },
        {
            "type": "scholarship",
            "title": "The Song and ANE Love Poetry",
            "body": "Song of Solomon shares features with Egyptian, Sumerian, and Mesopotamian love "
                    "poetry but transcends them in one crucial way: mutuality. In most ANE love "
                    "poetry, the woman is an object of male desire. In the Song, the woman speaks "
                    "more than the man. She initiates, she seeks, she desires, she celebrates her "
                    "own body without shame. 'I am dark but lovely' (1:5) -- she names her own "
                    "beauty. 'My beloved is mine and I am his' (2:16) -- the relationship is "
                    "mutual and reciprocal. This mutuality is revolutionary in its ancient context "
                    "and reflects the theology of Genesis 2: man and woman created together in "
                    "God's image, united in complementary love."
        }
    ]
}
