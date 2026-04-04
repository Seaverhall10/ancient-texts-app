"""
era_98_the_beloved.py -- The Beloved (Song of Solomon 1-5)

The first movement of the Song of Songs: the opening voices of desire, mutual
praise between the lovers, the spring invitation to "arise, my love," the
night search through the city streets, the magnificent wedding procession of
Solomon, the locked garden metaphor, and the second night of absence. Song 1-2
establishes the lovers' voices and the garden/vineyard imagery; Song 3-5
intensifies the drama with the wasf (extended praise of the woman's beauty),
the garden invitation and consummation, and the raw anguish of love tested
by absence -- the beloved knocks, she hesitates, and he is gone.
"""

CHAPTERS = [
    {
        "id": "song-1-2",
        "ref": "Song of Solomon 1-2",
        "chapter_num": 1,
        "title": "The Beloved and the Lover: First Words of Desire",
        "era": "the_beloved",
        "type": "chapter",
        "themes": ["LOVE", "WOMEN", "TYPE"],

        "synopsis": "The Song opens with the woman's voice -- a striking literary choice in the "
                    "ancient world. 'Let him kiss me with the kisses of his mouth! For your love is "
                    "better than wine' (1:2). She introduces herself: 'I am very dark, but beautiful, "
                    "O daughters of Jerusalem, like the tents of Kedar, like the curtains of Solomon' "
                    "(1:5). She is sun-darkened from working in the vineyards (1:6), but she claims her "
                    "beauty without apology. The dialogue between the lovers begins: he calls her 'most "
                    "beautiful among women' (1:8); she compares him to an apple tree among wild trees "
                    "(2:3). The imagery moves through nature -- vineyards, gardens, mountains, gazelles -- "
                    "with the landscape of Israel as the backdrop for desire. The famous invitations "
                    "emerge: 'Arise, my love, my beautiful one, and come away, for behold, the winter "
                    "is past; the rain is over and gone. The flowers appear on the earth, the time of "
                    "singing has come' (2:10-12). The adjuration to the daughters of Jerusalem appears "
                    "for the first time: 'Do not stir up or awaken love until it pleases' (2:7) -- "
                    "a refrain that will recur, suggesting that love has its own timing and cannot "
                    "be forced.",

        "key_verse": {
            "ref": "Song of Solomon 2:16",
            "text": "My beloved is mine, and I am his; he grazes among the lilies.",
            "translation": "ESV"
        },

        "original_terms": [
            "dodi (my beloved -- the woman's word for her lover; from dod, 'beloved/uncle/love'; used 32 times in the Song; the same root as David, 'beloved')",
            "ra'yati (my darling/companion -- the man's word for his beloved; from ra'ah, 'companion/friend'; she is not merely desired but valued as a companion)",
            "shoshanah (lily/lotus -- the flower the beloved is compared to; 'a lily among brambles,' 2:2; a symbol of beauty flourishing in an unlikely place)",
            "tappuach (apple tree -- the lover compared to an apple tree among forest trees; rare, sweet, and sheltering among the common and wild)"
        ],

        "ane_backdrop": "Egyptian love poetry from the New Kingdom (~1300-1100 BC) provides the closest "
                        "parallels to Song of Solomon 1-2. The Chester Beatty Papyrus I contains love "
                        "songs with strikingly similar features: nature imagery, the woman initiating "
                        "dialogue, physical descriptions of the beloved, and the brother/sister address "
                        "(Song 4:9, 5:1). The Egyptian songs also feature adjurations ('I adjure you, "
                        "O daughters') and nature walks as settings for encounters. However, the Song's "
                        "theology -- that human love reflects divine love and belongs within the covenant "
                        "community's sacred literature -- has no Egyptian parallel. The Sumerian Dumuzi-Inanna "
                        "love lyrics celebrate the sacred marriage between king and goddess, but the Song "
                        "democratizes this: the lovers are not divine figures but ordinary people whose "
                        "love participates in something divine.",

        "second_temple": [
            {
                "source": "Mishnah Yadayim 3:5",
                "summary": "Rabbi Akiva declares: 'The whole world is not worth the day on which "
                           "the Song of Songs was given to Israel. All the Writings are holy, but "
                           "the Song of Songs is the Holy of Holies.'",
                "relevance": "Akiva's defense canonized the Song by framing it as the supreme "
                             "expression of divine-human love -- the 'Holy of Holies' of scripture."
            },
            {
                "source": "Targum to Song of Solomon",
                "summary": "The Aramaic Targum reads the entire Song allegorically as the history "
                           "of God's relationship with Israel: the exodus, Sinai, the temple, "
                           "exile, and restoration.",
                "relevance": "The Targum demonstrates that the allegorical reading was deeply "
                             "embedded in Jewish interpretation from an early period."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 2:23-25", "note": "The first love poem: 'This at last is bone of my bones' -- the Song celebrates the same Edenic mutuality and delight", "type": "ot"},
            {"ref": "Proverbs 5:18-19", "note": "'Rejoice in the wife of your youth, a lovely deer, a graceful doe' -- wisdom tradition affirming the goodness of marital love", "type": "ot"},
            {"ref": "Hosea 2:14-16", "note": "YHWH will 'allure' Israel and speak tenderly to her in the wilderness -- the prophetic love language that echoes the Song", "type": "ot"},
            {"ref": "Isaiah 5:1-7", "note": "The 'Song of the Vineyard' -- YHWH's vineyard imagery applied to his relationship with Israel", "type": "ot"},
            {"ref": "Ephesians 5:25-32", "note": "'Husbands, love your wives, as Christ loved the church' -- Paul's marriage theology rooted in the Song's tradition", "type": "nt"},
            {"ref": "Revelation 19:7-9", "note": "The marriage supper of the Lamb -- the eschatological fulfillment of the covenant love the Song celebrates", "type": "nt"}
        ],

        "divine_council_note": "The Song's garden imagery (1:6, 2:1-3, 2:11-13) echoes the Garden of Eden -- "
                               "the original place where God walked with humanity in unbroken relationship. "
                               "In the divine council framework, Eden was the meeting point between the "
                               "heavenly and earthly realms, the place where God's council intersected with "
                               "the human world. The Song's lovers seek each other in gardens, among flowers, "
                               "under trees -- reimagining Eden's intimacy after the fall. If the Song "
                               "typologically represents YHWH's love for his people, then its garden setting "
                               "points to the restoration of what was lost when humanity was expelled from "
                               "Eden: direct, unmediated, intimate communion with God.",

        "sections": [
            {
                "heading": "The Woman's Voice: 'Let Him Kiss Me' (Song 1:1-8)",
                "body": "The Song opens not with the man's desire but the woman's: 'Let him kiss me with "
                        "the kisses of his mouth! For your love (dodekha) is better than wine' (1:2). In "
                        "the ancient world, the woman speaking first is extraordinary -- most love poetry "
                        "presents the woman as the object of male gaze. Here, she is the subject of her own "
                        "desire. She describes herself without apology: 'I am very dark, but beautiful, O "
                        "daughters of Jerusalem, like the tents of Kedar, like the curtains of Solomon' "
                        "(1:5). The darkness comes from outdoor labor: 'My mother's sons were angry with me; "
                        "they made me keeper of the vineyards, but my own vineyard I have not kept!' (1:6). "
                        "'My own vineyard' is double-edged: she has tended others' vineyards but neglected "
                        "her own beauty/herself. She seeks her beloved: 'Tell me, you whom my soul loves, "
                        "where you pasture your flock' (1:7). The language 'you whom my soul loves' "
                        "(she-ahavah nafshi) anticipates covenant love language."
            },
            {
                "heading": "Mutual Praise: Beauty Reflected (Song 1:9-2:7)",
                "body": "The dialogue of mutual admiration begins. He calls her 'my love' (ra'yati), compares "
                        "her to 'a mare among Pharaoh's chariots' (1:9 -- an image of stunning beauty and "
                        "controlled power), and describes her ornaments (1:10-11). She responds: 'My beloved "
                        "is to me a sachet of myrrh that lies between my breasts... a cluster of henna "
                        "blossoms in the vineyards of En-gedi' (1:13-14). The imagery is sensory: fragrance, "
                        "taste, touch. The exchanges build: 'Behold, you are beautiful, my love' / 'Behold, "
                        "you are beautiful, my beloved' (1:15-16). She identifies herself as 'a rose of "
                        "Sharon, a lily of the valleys' (2:1) -- humble wildflowers, not cultivated garden "
                        "specimens. He responds: 'As a lily among brambles, so is my love among the young "
                        "women' (2:2). She returns: 'As an apple tree among the trees of the forest, so is "
                        "my beloved among the young men. With great delight I sat in his shadow, and his "
                        "fruit was sweet to my taste' (2:3). Then the first adjuration: 'I adjure you, O "
                        "daughters of Jerusalem... that you not stir up or awaken love until it pleases' "
                        "(2:7). Love must not be forced or rushed -- it awakens in its own time."
            },
            {
                "heading": "The Spring Invitation: 'Arise, My Love' (Song 2:8-17)",
                "body": "The woman hears her beloved approaching: 'The voice of my beloved! Behold, he "
                        "comes, leaping over the mountains, bounding over the hills. My beloved is like "
                        "a gazelle or a young stag' (2:8-9). The imagery of leaping and bounding conveys "
                        "urgent, joyful approach. He stands outside and calls: 'Arise, my love, my "
                        "beautiful one, and come away, for behold, the winter is past; the rain is over "
                        "and gone. The flowers appear on the earth, the time of singing has come, and "
                        "the voice of the turtledove is heard in our land. The fig tree ripens its figs, "
                        "and the vines are in blossom; they give forth fragrance. Arise, my love, my "
                        "beautiful one, and come away' (2:10-13). This is arguably the most beautiful "
                        "passage in the Hebrew Bible. Spring -- the season of renewal, of creation "
                        "emerging from death -- is the setting for love's invitation. The allusion to "
                        "Passover (spring, new life, departure from bondage) deepens if read allegorically: "
                        "God calls Israel out of the winter of slavery into the spring of covenant love. "
                        "The chapter closes with a verse that will recur as a refrain: 'My beloved is mine, "
                        "and I am his; he grazes among the lilies' (2:16). Mutual belonging: the essence "
                        "of covenant."
            }
        ]
    },

    {
        "id": "song-3-5",
        "ref": "Song of Solomon 3-5",
        "chapter_num": 2,
        "title": "Seeking, Finding, and the Wedding Procession",
        "era": "the_beloved",
        "type": "chapter",
        "themes": ["LOVE", "WOMEN", "HOLY", "TYPE"],

        "synopsis": "The middle section of the Song intensifies both desire and tension. The woman "
                    "searches for her beloved through the city streets at night -- 'I sought him, but "
                    "found him not' (3:1). She finds him and will not let go (3:4). A grand wedding "
                    "procession appears: 'What is that coming up from the wilderness like columns of "
                    "smoke, perfumed with myrrh and frankincense?' (3:6). Solomon's litter is described "
                    "in magnificent detail (3:7-10). Chapter 4 is the man's extended praise of the "
                    "woman's beauty (the wasf): 'You are altogether beautiful, my love; there is no "
                    "flaw in you' (4:7). The garden metaphor reaches its fullest expression: 'A garden "
                    "locked is my sister, my bride, a spring locked, a fountain sealed' (4:12). She "
                    "invites him: 'Let my beloved come to his garden' (4:16). He enters: 'I came to my "
                    "garden, my sister, my bride' (5:1). Then a second night search: the beloved knocks, "
                    "but she hesitates; when she opens, he is gone. She searches the city again, is "
                    "struck by the watchmen, and adjures the daughters of Jerusalem to tell her beloved "
                    "that she is 'sick with love' (5:8).",

        "key_verse": {
            "ref": "Song of Solomon 4:7",
            "text": "You are altogether beautiful, my love; there is no flaw in you.",
            "translation": "ESV"
        },

        "original_terms": [
            "kallah (bride -- used six times in 4:8-5:1; the marriage context of the love celebration)",
            "gan na'ul (locked garden -- the woman as an enclosed, exclusive garden; a metaphor for sexual purity and covenant exclusivity)",
            "ma'yan chatum (sealed fountain -- parallel to the locked garden; the beloved's intimacy is reserved for her lover alone)",
            "cholat ahavah (sick with love/lovesick -- the woman's self-description; love so intense it causes physical anguish)"
        ],

        "ane_backdrop": "The wasf (Arabic for 'description') -- an extended praise poem describing the "
                        "beloved's body from head to foot (or foot to head) -- is a common form in ancient "
                        "Near Eastern love poetry. Egyptian love songs use similar catalogues of beauty. The "
                        "'locked garden' imagery (4:12) connects to the ANE understanding of gardens as "
                        "sacred, enclosed spaces -- the Persian pardes (paradise) from which the English "
                        "'paradise' derives. In the Song, the woman IS the garden: her body is the enclosed, "
                        "fragrant space that the lover enters by invitation. The wedding procession (3:6-11) "
                        "with its columns of smoke, myrrh, and frankincense parallels the incense processions "
                        "described in Egyptian and Mesopotamian wedding and temple texts.",

        "second_temple": [
            {
                "source": "Origen, Commentary on Song of Songs (~240 AD)",
                "summary": "Origen's commentary is the foundational Christian allegorical reading: "
                           "the bride is the church or the individual soul, the groom is Christ, "
                           "the garden is paradise restored.",
                "relevance": "Origen's reading shaped Christian interpretation for over a millennium "
                             "and demonstrates the Song's capacity to bear multiple levels of meaning."
            }
        ],

        "cross_refs": [
            {"ref": "Ezekiel 16:8-14", "note": "YHWH describes his covenant with Israel in marriage terms: 'I made my vow to you and entered into a covenant with you... and you became mine'", "type": "ot"},
            {"ref": "Isaiah 62:4-5", "note": "'As the bridegroom rejoices over the bride, so shall your God rejoice over you' -- the prophetic marriage metaphor the Song embodies", "type": "ot"},
            {"ref": "Psalm 45:10-15", "note": "The royal wedding psalm: the bride presented in gold-woven robes -- the same world of royal wedding celebration as Song 3:6-11", "type": "ot"},
            {"ref": "2 Corinthians 11:2", "note": "Paul: 'I betrothed you to one husband, to present you as a pure virgin to Christ' -- the locked garden theology applied to the church", "type": "nt"},
            {"ref": "Revelation 21:2", "note": "The new Jerusalem 'prepared as a bride adorned for her husband' -- the ultimate wedding the Song anticipates", "type": "nt"}
        ],

        "divine_council_note": "The garden imagery of Song 4:12-5:1 carries profound theological weight. The "
                               "'locked garden' (gan na'ul) is a miniature Eden: a place of beauty, fragrance, "
                               "fruit, and intimate encounter. In the divine council framework, Eden was the "
                               "place where heaven and earth intersected -- where God's council touched the "
                               "human world. The Song's garden is both a woman's body and a theological space: "
                               "the lovers' union in the garden reverses the expulsion from Eden. The 'friends' "
                               "invited to eat and drink (5:1b) may echo the divine council's participation in "
                               "the joy of union -- a heavenly feast celebrating restored relationship. If the "
                               "Song is typological, then the garden represents the new creation where God and "
                               "humanity are reunited in love.",

        "sections": [
            {
                "heading": "The Night Search and the Wedding Procession (Song 3:1-11)",
                "body": "The woman searches the city at night: 'On my bed by night I sought him whom my soul "
                        "loves; I sought him, but found him not. I will rise now and go about the city, in "
                        "the streets and in the squares; I will seek him whom my soul loves' (3:1-2). The "
                        "watchmen find her but cannot help. Then: 'Scarcely had I passed them when I found "
                        "him whom my soul loves. I held him, and would not let him go' (3:4). The scene "
                        "shifts to a magnificent procession: 'What is that coming up from the wilderness like "
                        "columns of smoke, perfumed with myrrh and frankincense?' (3:6). Solomon's litter "
                        "appears: 60 mighty men as guard, cedar wood, silver pillars, gold seat, purple "
                        "upholstery 'lovingly inlaid by the daughters of Jerusalem' (3:10). The daughters "
                        "of Zion are called to witness: 'Go out... and look upon King Solomon, with the "
                        "crown with which his mother crowned him on the day of his wedding, on the day of "
                        "the gladness of his heart' (3:11). Whether this is Solomon's actual wedding or a "
                        "poetic evocation of the marriage celebration, the point is the same: love's "
                        "consummation deserves the most magnificent setting imaginable."
            },
            {
                "heading": "The Garden of Delight: The Wasf and the Invitation (Song 4:1-5:1)",
                "body": "Chapter 4 contains the man's extended praise of the woman's beauty (the wasf). "
                        "The imagery moves from her eyes ('doves behind your veil,' 4:1) through her hair, "
                        "teeth, lips, cheeks, neck, and breasts (4:1-5). Each comparison draws from the "
                        "natural world: 'Your hair is like a flock of goats leaping down the slopes of "
                        "Gilead. Your teeth are like a flock of shorn ewes' (4:1-2). To modern ears these "
                        "comparisons seem odd; in the ancient world, they celebrate vitality, health, and "
                        "the beauty of the created order. The wasf climaxes with a declaration: 'You are "
                        "altogether beautiful, my love; there is no flaw in you' (4:7). Then the garden "
                        "metaphor: 'A garden locked is my sister, my bride, a spring locked, a fountain "
                        "sealed... a garden fountain, a well of living water, and flowing streams from "
                        "Lebanon' (4:12, 15). The woman is an enclosed garden -- her intimacy is exclusive, "
                        "reserved, precious. She responds with the invitation: 'Awake, O north wind, and "
                        "come, O south wind! Blow upon my garden, let its spices flow out. Let my beloved "
                        "come to his garden, and eat its choicest fruits' (4:16). He responds: 'I came to "
                        "my garden, my sister, my bride; I gathered my myrrh with my spice' (5:1)."
            },
            {
                "heading": "The Second Night Search: Love Tested by Absence (Song 5:2-8)",
                "body": "A second night scene unfolds: 'I slept, but my heart was awake. A sound! My beloved "
                        "is knocking. Open to me, my sister, my love, my dove, my perfect one, for my head "
                        "is wet with dew, my locks with the drops of the night' (5:2). He knocks; she "
                        "hesitates: 'I had put off my garment; how could I put it on? I had bathed my feet; "
                        "how could I soil them?' (5:3). When she finally opens, he is gone: 'I opened to my "
                        "beloved, but my beloved had turned and gone. My soul failed me when he spoke. I "
                        "sought him, but found him not; I called him, but he gave no answer' (5:6). She "
                        "searches the city and is struck by the watchmen (5:7) -- love's journey is not "
                        "always safe. She adjures the daughters of Jerusalem: 'If you find my beloved, "
                        "tell him I am sick with love' (5:8). The hesitation and absence create the most "
                        "emotionally raw section of the Song: love denied is love intensified. Read "
                        "allegorically, this represents the experience of divine absence -- the 'dark night "
                        "of the soul' when the Beloved seems to withdraw, and the lover must seek with "
                        "renewed urgency."
            }
        ]
    }
]
