"""
era_77_hosea_judgment.py -- Hosea 8-14: Judgment, Exile, and Restoration

The final section of Hosea escalates the judgment oracles against Israel while
simultaneously revealing YHWH's deepest emotions: anguish over his rebellious
son, the lion's roar that calls the children home, and the promise that Israel
will blossom like the lily when YHWH heals their apostasy. Chapter 11's portrayal
of YHWH as a heartbroken father is among the most theologically significant
passages in the prophetic literature.
"""

CHAPTERS = [
    {
        "id": "hosea-8",
        "ref": "Hosea 8",
        "chapter_num": 8,
        "title": "Sowing the Wind, Reaping the Whirlwind",
        "era": "hosea_judgment",
        "type": "chapter",

        "synopsis": "The alarm sounds: 'Set the trumpet to your lips! One like a vulture is over the house "
                    "of YHWH, because they have transgressed my covenant and rebelled against my law' (8:1). "
                    "Israel cries 'My God, we know you!' but YHWH rejects their hollow profession. The core "
                    "indictment: they have made kings without YHWH's approval, made idols from silver and gold, "
                    "and the calf of Samaria will be broken to pieces. The most memorable phrase in the chapter "
                    "encapsulates the entire prophetic message: 'They sow the wind, and they shall reap the "
                    "whirlwind' (8:7). Israel's sacrifices are rejected: 'They offer me sacrifices of flesh "
                    "and eat them, but YHWH does not accept them' (8:13). The chapter closes with a devastating "
                    "irony: 'Israel has forgotten his Maker and built palaces, and Judah has multiplied "
                    "fortified cities; so I will send a fire upon his cities' (8:14).",

        "key_verse": {
            "ref": "Hosea 8:7",
            "text": "For they sow the wind, and they shall reap the whirlwind. The standing grain has no heads; it shall yield no flour; if it were to yield, strangers would devour it.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ruach (wind -- they sow wind; insubstantial, empty)",
            "sufah (whirlwind/storm -- they reap destruction far greater than what they sowed)",
            "egel Shomeron (calf of Samaria -- the golden calf worship at Bethel and Dan)",
            "berit (covenant -- 'they have transgressed my covenant,' the fundamental charge)"
        ],

        "ane_backdrop": "The 'calf of Samaria' (8:5-6) refers to the golden calves set up by Jeroboam I at "
                        "Bethel and Dan (1 Kings 12:28-29). These were likely intended as pedestals for YHWH's "
                        "invisible presence (similar to the cherubim in the Jerusalem Temple), but popular "
                        "worship conflated the image with the deity -- a violation of the second commandment. "
                        "Bull iconography was widespread in ancient Near Eastern religion, associated with "
                        "El and Baal.",

        "second_temple": [
            {
                "source": "Galatians 6:7-8",
                "summary": "Paul echoes Hosea's sowing/reaping principle: 'Whatever one sows, that will he "
                           "also reap. For the one who sows to his own flesh will reap corruption.'",
                "relevance": "The sowing/reaping principle is a cosmic moral law that operates at both "
                             "national (Hosea) and individual (Paul) levels."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 12:28-29", "note": "Jeroboam's golden calves at Bethel and Dan -- the origin of the calf worship Hosea condemns", "type": "ot"},
            {"ref": "Galatians 6:7-8", "note": "'Whatever one sows, that will he also reap' -- Hosea's principle universalized", "type": "nt"},
            {"ref": "Hosea 10:12-13", "note": "The sowing/reaping metaphor extended: 'You have plowed iniquity, reaped injustice'", "type": "ot"}
        ],

        "divine_council_note": "Israel's idolatry is not merely bad religion but cosmic treason. The golden "
                               "calf represents worship of a created divine being (or a syncretistic confusion "
                               "of YHWH with Baal/El imagery) rather than the uncreated Creator. In the divine "
                               "council framework, YHWH sits enthroned above all other elohim. To worship the "
                               "calf is to dethrone YHWH and elevate a subordinate -- or a fabrication -- to "
                               "the supreme position.",

        "sections": [
            {
                "heading": "The Alarm and the Hollow Cry (8:1-3)",
                "body": "The trumpet sounds: the vulture of judgment circles the house of YHWH. Israel "
                        "cries 'My God, we know you!' but their actions contradict their words. Knowledge "
                        "of God requires obedience, not merely verbal profession."
            },
            {
                "heading": "Kings and Calves: Unauthorized Authority (8:4-6)",
                "body": "Israel has set up kings and princes without YHWH's sanction, and made idols from "
                        "silver and gold. The calf of Samaria provokes YHWH's anger: 'A craftsman made it; "
                        "it is not God.' The idol will be smashed to splinters."
            },
            {
                "heading": "Sowing Wind, Reaping Whirlwind (8:7-10)",
                "body": "The proverb that encapsulates Israel's folly: they invest in worthlessness and "
                        "receive destruction. Israel has become like a useless vessel among the nations, "
                        "going to Assyria 'like a wild donkey wandering alone.' They hire allies among the "
                        "nations, but YHWH will gather them for judgment."
            },
            {
                "heading": "Rejected Sacrifices (8:11-14)",
                "body": "Israel multiplies altars -- not for YHWH but 'for sinning.' Their sacrifices are "
                        "mere meat meals: 'YHWH does not accept them.' Israel has forgotten its Maker and "
                        "built palaces; Judah has fortified cities. Both trust in human construction rather "
                        "than divine protection. Fire will consume them."
            }
        ]
    },

    {
        "id": "hosea-9",
        "ref": "Hosea 9",
        "chapter_num": 9,
        "title": "No Rejoicing -- Exile Among the Nations",
        "era": "hosea_judgment",
        "type": "chapter",

        "synopsis": "Hosea announces that Israel's harvest festivals are over: 'Rejoice not, O Israel! "
                    "Exult not like the peoples; for you have played the whore, forsaking your God' (9:1). "
                    "The agricultural blessings will cease, and Israel will return to 'Egypt' (a metaphor for "
                    "exile, though Assyria is the actual destination) and eat unclean food among the nations. "
                    "The prophet himself is mocked: 'The prophet is a fool! The man of the spirit is mad!' "
                    "(9:7). Hosea recalls Israel's beginnings at Baal-peor (Num 25), where they first "
                    "prostituted themselves to foreign gods, and Gilgal, where the rot of the monarchy began. "
                    "The chapter's most chilling image concerns the loss of children: 'Give them, O YHWH -- "
                    "what will you give? Give them a miscarrying womb and dry breasts' (9:14). Ephraim's "
                    "glory will 'fly away like a bird -- no birth, no pregnancy, no conception' (9:11).",

        "key_verse": {
            "ref": "Hosea 9:7",
            "text": "The days of punishment have come; the days of recompense have come; Israel shall know it. The prophet is a fool! The man of the spirit is mad! Because of your great iniquity and great hatred.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "paqad (visitation/punishment -- YHWH 'visits' Israel in judgment)",
            "Baal-peor (the site of Israel's first mass apostasy through sexual idolatry, Num 25)",
            "nabi (prophet -- the people mock the prophet as a fool)",
            "Gilgal (the site associated with the beginning of the monarchy and its corruption)"
        ],

        "ane_backdrop": "Harvest festivals in the ancient Near East were religious occasions dedicated to the "
                        "deity credited with agricultural fertility. Israel's participation in Canaanite-style "
                        "harvest celebrations -- attributing the crop to Baal -- is what Hosea condemns. The "
                        "exile 'to Egypt' (9:3, 6) is symbolic: Egypt represents the state of bondage before "
                        "YHWH's redemption. Returning to 'Egypt' means returning to pre-exodus slavery.",

        "second_temple": [
            {
                "source": "Luke 23:29",
                "summary": "Jesus echoes Hosea's language: 'Blessed are the barren and the wombs that never "
                           "bore and the breasts that never nursed!'",
                "relevance": "Jesus applies Hosea's barrenness-as-judgment imagery to Jerusalem's coming "
                             "destruction in 70 AD."
            }
        ],

        "cross_refs": [
            {"ref": "Numbers 25:1-9", "note": "Baal-peor -- Israel's first mass sexual-idolatrous apostasy, recalled by Hosea", "type": "ot"},
            {"ref": "1 Samuel 11:14-15", "note": "Gilgal as the site of Saul's kingship confirmation", "type": "ot"},
            {"ref": "Luke 23:29", "note": "Jesus echoes the barrenness judgment language of Hosea 9", "type": "nt"}
        ],

        "divine_council_note": "Israel's exile 'among the nations' is a return to the spiritual geography "
                               "of the Deuteronomy 32 allotment. Outside the land of Israel -- YHWH's "
                               "territory -- the people will be under the spiritual jurisdiction of the gods "
                               "of the nations. Eating 'unclean food in Assyria' (9:3) is both a dietary and "
                               "a spiritual contamination: in foreign lands, Israel is cut off from YHWH's "
                               "Temple, YHWH's sacrificial system, and YHWH's direct governance.",

        "sections": [
            {
                "heading": "Harvest Joy Ended (9:1-6)",
                "body": "Israel's festivals are over. The threshing floor and wine vat will fail them. "
                        "They will not remain in YHWH's land but will be scattered -- to Assyria, to "
                        "Egypt. Their silver treasures will be inherited by nettles and thorns."
            },
            {
                "heading": "The Mocked Prophet (9:7-9)",
                "body": "The people call the prophet a fool and a madman. Hosea responds: this contempt "
                        "for the prophetic word is itself evidence of Israel's great iniquity. The prophet "
                        "is the watchman over Ephraim -- but traps are set in all his paths."
            },
            {
                "heading": "Baal-peor and Barrenness (9:10-17)",
                "body": "YHWH recalls finding Israel 'like grapes in the wilderness' -- fresh, delightful. "
                        "But at Baal-peor they consecrated themselves to Baal and became detestable. Now "
                        "Ephraim's glory will vanish: no birth, no pregnancy, no conception. Even if they "
                        "bring up children, YHWH will bereave them. The prayer of 9:14 is agonizing: the "
                        "prophet asks YHWH for miscarriage and barrenness as mercy -- better to have no "
                        "children than to raise them for slaughter."
            }
        ]
    },

    {
        "id": "hosea-10",
        "ref": "Hosea 10",
        "chapter_num": 10,
        "title": "The Luxuriant Vine and the Plowed Fallow Ground",
        "era": "hosea_judgment",
        "type": "chapter",

        "synopsis": "Israel is a 'luxuriant vine that yields its fruit' -- but the more fruit it produced, "
                    "the more altars it built; the more the land prospered, the more sacred pillars it erected "
                    "(10:1). Prosperity led not to gratitude but to idolatry. The calf of Beth-aven (Bethel, "
                    "renamed 'house of wickedness') will be carried off to Assyria as tribute: 'Samaria's "
                    "king shall perish like a twig on the face of the waters' (10:7). The high places of Aven "
                    "will be destroyed, and the people will cry to the mountains and hills, 'Cover us!' and "
                    "'Fall on us!' (10:8). The chapter contains a powerful agricultural call to repentance: "
                    "'Sow for yourselves righteousness; reap steadfast love; break up your fallow ground, for "
                    "it is the time to seek YHWH' (10:12). But Israel has plowed iniquity, reaped injustice, "
                    "and eaten the fruit of lies (10:13).",

        "key_verse": {
            "ref": "Hosea 10:12",
            "text": "Sow for yourselves righteousness; reap steadfast love; break up your fallow ground, for it is the time to seek the LORD, that he may come and rain righteousness upon you.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "gefen (vine -- Israel as luxuriant vine, cf. Isa 5, Ps 80, John 15)",
            "nir (fallow ground -- unplowed land that needs breaking up; metaphor for hardened hearts)",
            "tsedaqah (righteousness -- what Israel should sow instead of iniquity)"
        ],

        "ane_backdrop": "The 'calf of Beth-aven' being carried off as tribute reflects the ancient practice "
                        "of victorious armies carrying captured idols as war spoils (cf. 1 Sam 5:1-2, the "
                        "Philistines capturing the Ark; Isa 46:1-2, Bel and Nebo carried off). The irony is "
                        "sharp: the god Israel worshiped cannot even protect itself.",

        "second_temple": [
            {
                "source": "Luke 23:30",
                "summary": "Jesus quotes Hosea 10:8 on the way to the cross: 'Then they will begin to say "
                           "to the mountains, \"Fall on us,\" and to the hills, \"Cover us.\"'",
                "relevance": "Jesus applies Hosea's judgment language to the coming destruction of Jerusalem "
                             "-- the same pattern of judgment for covenant unfaithfulness."
            },
            {
                "source": "Revelation 6:16",
                "summary": "At the opening of the sixth seal, the earth's inhabitants cry to the mountains "
                           "and rocks, 'Fall on us and hide us.'",
                "relevance": "John's apocalyptic vision extends Hosea's imagery to the final cosmic judgment."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 5:1-7", "note": "Isaiah's Song of the Vineyard -- another vine metaphor for Israel's unfaithfulness", "type": "ot"},
            {"ref": "Luke 23:30", "note": "Jesus quotes Hosea 10:8 on the way to Calvary", "type": "nt"},
            {"ref": "Revelation 6:16", "note": "The cry 'Fall on us, hide us' at the cosmic judgment", "type": "nt"},
            {"ref": "John 15:1-8", "note": "Jesus as the true vine -- the fulfillment of Israel's calling", "type": "nt"}
        ],

        "divine_council_note": "The capture and deportation of the Samarian calf-idol exposes the impotence "
                               "of the false gods. In the divine council framework, the Baals and golden calves "
                               "represent either corrupted divine beings or human fabrications -- neither can "
                               "save. Only YHWH, the Most High who presides over the council (Ps 82:1), has "
                               "actual power. The call to 'sow righteousness' (10:12) is a call to realign "
                               "with YHWH's governance rather than the corrupt rule of the allotted gods.",

        "sections": [
            {
                "heading": "Prosperity and Idolatry (10:1-4)",
                "body": "The vine metaphor reveals the paradox: the more YHWH blessed Israel, the more "
                        "they invested in idolatry. Prosperity became the fuel for apostasy. Their heart "
                        "is 'false' (chalaq, smooth/divided) -- they try to serve both YHWH and the Baals."
            },
            {
                "heading": "The Calf Carried Off (10:5-8)",
                "body": "The golden calf will be deported to Assyria as tribute. Samaria's king will "
                        "perish like a twig swept away on water. The high places will be overgrown, and "
                        "the people will cry for the mountains to fall on them -- language Jesus and John "
                        "will both repurpose for eschatological judgment."
            },
            {
                "heading": "Sow Righteousness, Break the Fallow Ground (10:9-15)",
                "body": "Despite the judgment, YHWH issues a call to repentance through agricultural "
                        "metaphor: sow righteousness, reap hesed, break up hardened ground, seek YHWH. "
                        "But the diagnosis follows immediately: Israel has sowed iniquity, reaped "
                        "injustice, and trusted in military power rather than YHWH."
            }
        ]
    },

    {
        "id": "hosea-11",
        "ref": "Hosea 11",
        "chapter_num": 11,
        "title": "The Heartbroken Father -- YHWH's Anguished Love",
        "era": "hosea_judgment",
        "type": "chapter",

        "synopsis": "Chapter 11 is the emotional and theological summit of Hosea. The marriage metaphor "
                    "gives way to the father-son metaphor: 'When Israel was a child, I loved him, and out of "
                    "Egypt I called my son' (11:1). YHWH recalls teaching Ephraim to walk, carrying them in "
                    "his arms, healing them, leading them 'with cords of kindness, with the bands of love' "
                    "(11:4). 'I bent down to them and fed them' (11:4) -- the image of a parent stooping to "
                    "feed a toddler. But Israel turned away, and now judgment must come: 'The sword shall rage "
                    "against their cities' (11:6). Then comes the most extraordinary reversal in the prophetic "
                    "literature: 'How can I give you up, O Ephraim? How can I hand you over, O Israel? ... My "
                    "heart recoils within me; my compassion grows warm and tender. I will not execute my "
                    "burning anger; I will not again destroy Ephraim; for I am God and not a man, the Holy One "
                    "in your midst, and I will not come in wrath' (11:8-9). YHWH's holiness, paradoxically, "
                    "becomes the ground of mercy rather than judgment.",

        "key_verse": {
            "ref": "Hosea 11:8-9",
            "text": "How can I give you up, O Ephraim? How can I hand you over, O Israel? How can I make you like Admah? How can I treat you like Zeboiim? My heart recoils within me; my compassion grows warm and tender. I will not execute my burning anger; I will not again destroy Ephraim; for I am God, and not a man, the Holy One in your midst, and I will not come in wrath.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "na'ar (child/youth -- Israel as YHWH's beloved child)",
            "ahavah (love -- 'I loved him,' divine parental love)",
            "rachamim (compassion -- 'my compassion grows warm and tender,' womb-love, visceral)",
            "nehpak (recoils/overturns -- YHWH's heart overturns within him; the verb used for Sodom's overthrow)",
            "qadosh (Holy One -- 'the Holy One in your midst'; holiness becomes the ground of mercy)"
        ],

        "ane_backdrop": "Admah and Zeboiim (11:8) were cities of the plain destroyed alongside Sodom and "
                        "Gomorrah (Gen 14:2, 8; 19:24-25; Deut 29:23). By invoking them, YHWH is asking: "
                        "'How can I do to you what I did to Sodom?' The verb nehpak ('recoils/overturns') is "
                        "the same verb used for the 'overthrow' (mahpekah) of Sodom (Gen 19:25). YHWH's "
                        "heart is 'overthrown' -- the destruction he plans for Israel is redirected inward, "
                        "as divine compassion overthrows divine wrath.",

        "second_temple": [
            {
                "source": "Matthew 2:15",
                "summary": "Matthew applies Hosea 11:1 to Jesus' return from Egypt: 'Out of Egypt I called "
                           "my son.'",
                "relevance": "Matthew sees Jesus as the true Israel -- the faithful Son who recapitulates "
                             "Israel's history and fulfills what Israel failed to fulfill. The Son called out "
                             "of Egypt is both Israel and the Messiah."
            },
            {
                "source": "Luke 15:11-32",
                "summary": "The Parable of the Prodigal Son echoes Hosea 11's father-child dynamic: a father "
                           "who watches his child leave, suffers, and runs to embrace the returning child.",
                "relevance": "Jesus' parable is the narrative dramatization of Hosea 11's theology: the "
                             "father's love that persists through the child's rebellion."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 4:22", "note": "'Israel is my firstborn son' -- the sonship YHWH claims in Hosea 11:1", "type": "ot"},
            {"ref": "Genesis 19:24-25", "note": "Sodom, Admah, Zeboiim destroyed -- YHWH's heart 'recoils' from doing the same to Israel", "type": "ot"},
            {"ref": "Matthew 2:15", "note": "Jesus as the true Son called out of Egypt -- Hosea 11:1 fulfilled typologically", "type": "nt"},
            {"ref": "Luke 15:11-32", "note": "The Prodigal Son -- the narrative version of Hosea 11's heartbroken father", "type": "nt"},
            {"ref": "Romans 9:25-26", "note": "Paul applies Hosea's restoration promise to Gentile inclusion", "type": "nt"}
        ],

        "divine_council_note": "Hosea 11:1 -- 'Out of Egypt I called my son' -- is foundational to both "
                               "divine council theology and christology. Israel as YHWH's 'son' echoes the "
                               "bene elohim ('sons of God') language of the divine council. Israel was YHWH's "
                               "firstborn (Exod 4:22), called to be his image-bearing nation on earth as the "
                               "divine council serves him in heaven. When Matthew applies this to Jesus, the "
                               "full divine council significance emerges: Jesus is both the faithful Son of "
                               "God (the true Israel) and the divine Son of God (the council member who shares "
                               "YHWH's throne). He recapitulates Israel's journey and succeeds where Israel "
                               "failed. The declaration 'I am God and not a man' (11:9) distinguishes YHWH "
                               "from the lesser elohim: only the Most High can transform wrath into mercy "
                               "through his own holiness.",

        "sections": [
            {
                "heading": "The Father's Memory (11:1-4)",
                "body": "YHWH recalls Israel's infancy: teaching Ephraim to walk, carrying them in his "
                        "arms, leading them with cords of love. The imagery is achingly tender -- a parent "
                        "stooping to feed a child, holding a toddler's hands as they take first steps. "
                        "'But they did not know that I healed them' (11:3) -- the tragedy of unrecognized love."
            },
            {
                "heading": "The Sentence That Cannot Stand (11:5-7)",
                "body": "Judgment is pronounced: they shall return to 'Egypt' (exile), the sword shall "
                        "rage against their cities. 'My people are bent on turning away from me' (11:7). "
                        "The judgment is deserved, the evidence overwhelming."
            },
            {
                "heading": "The Divine Reversal (11:8-9)",
                "body": "Then YHWH speaks the words that shatter the judicial proceeding: 'How can I give "
                        "you up?' His heart is 'overthrown' within him -- the same verb used for Sodom's "
                        "destruction. The destruction meant for Israel detonates inside YHWH's own heart. "
                        "'I am God and not a man' -- divine holiness, paradoxically, becomes the ground "
                        "not of judgment but of mercy. A human betrayed spouse would destroy; God absorbs "
                        "the cost himself."
            },
            {
                "heading": "The Lion's Roar of Restoration (11:10-11)",
                "body": "YHWH will roar like a lion -- not to devour but to call his children home. 'They "
                        "shall come trembling like birds from Egypt, and like doves from the land of Assyria, "
                        "and I will return them to their homes' (11:11). The exile is not the end. The "
                        "scattered will be gathered."
            }
        ]
    },

    {
        "id": "hosea-12",
        "ref": "Hosea 12",
        "chapter_num": 12,
        "title": "Jacob's Legacy -- Wrestling with God and Man",
        "era": "hosea_judgment",
        "type": "chapter",

        "synopsis": "Hosea reaches back to the patriarchal narratives to indict Israel through its ancestor "
                    "Jacob. 'Ephraim feeds on the wind and pursues the east wind all day long; they multiply "
                    "falsehood and violence' (12:1). Then the prophet recalls Jacob's history: 'In the womb "
                    "he took his brother by the heel, and in his manhood he strove with God. He strove with "
                    "the angel and prevailed; he wept and sought his favor' (12:3-4). The reference to Jacob "
                    "wrestling with the angel (Gen 32:22-32) and meeting God at Bethel (Gen 28:10-22; 35:1-15) "
                    "serves a dual purpose: it recalls that Israel's very identity was forged through encounter "
                    "with God, and it indicts the present generation for their failure to seek God as Jacob did. "
                    "YHWH declares: 'I am YHWH your God from the land of Egypt; I will again make you dwell "
                    "in tents, as in the days of the appointed feast' (12:9).",

        "key_verse": {
            "ref": "Hosea 12:6",
            "text": "So you, by the help of your God, return, hold fast to love and justice, and wait continually for your God.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "aqav (to take by the heel/supplant -- wordplay on Jacob's name and character)",
            "sarah (to strive/contend -- Jacob 'strove' with God; the root of 'Israel')",
            "mal'ak (angel/messenger -- the divine being Jacob wrestled at Peniel)"
        ],

        "ane_backdrop": "The patriarchal narratives were foundational identity texts for Israel. By recalling "
                        "Jacob's story, Hosea invokes the entire tradition of divine election, wrestling with "
                        "God, and covenant promise -- and contrasts it with the present generation's abandonment "
                        "of that heritage.",

        "second_temple": [
            {
                "source": "Genesis 32:22-32",
                "summary": "Jacob's wrestling with the divine being at Peniel -- the encounter that renamed "
                           "him 'Israel' (one who strives with God).",
                "relevance": "Hosea uses this narrative to call Israel back to its identity: a people who "
                             "wrestle with God rather than ignore him."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 25:26", "note": "Jacob grabs Esau's heel at birth -- the character trait Hosea references", "type": "ot"},
            {"ref": "Genesis 32:22-32", "note": "Jacob wrestles with God at Peniel -- the identity-forging encounter", "type": "ot"},
            {"ref": "Genesis 28:10-22", "note": "Jacob's dream at Bethel -- 'YHWH, the God of hosts, YHWH is his memorial name'", "type": "ot"}
        ],

        "divine_council_note": "Hosea 12:4 states Jacob 'strove with the angel' -- the divine being at "
                               "Peniel whom Genesis 32:30 identifies as 'God face to face.' This is a "
                               "theophanic encounter with a member of the divine council -- likely the Angel "
                               "of YHWH, the visible manifestation of YHWH himself. In the divine council "
                               "framework, this is the 'second power in heaven' -- the divine mediator who "
                               "appears to the patriarchs. Israel's very name derives from this divine "
                               "council encounter.",

        "sections": [
            {
                "heading": "Ephraim's Wind-Chasing (12:1-2)",
                "body": "Israel pursues worthless alliances with Assyria and Egypt, making treaties while "
                        "exporting olive oil. They chase the east wind -- the hot desert wind (sirocco) "
                        "that brings devastation, not life."
            },
            {
                "heading": "Jacob's Story as Mirror (12:3-6)",
                "body": "Hosea recounts Jacob's history to mirror Israel's present: grasping, striving, "
                        "weeping. But Jacob sought God's favor and encountered him at Bethel. The call: "
                        "'Return to your God, hold fast to hesed and justice, and wait continually for "
                        "your God' (12:6)."
            },
            {
                "heading": "The Merchant and the Prophet (12:7-14)",
                "body": "Ephraim is called a 'merchant' (kena'an -- literally 'Canaan'!) with dishonest "
                        "scales. They have become Canaanites in practice. YHWH reminds them: 'I am YHWH "
                        "your God from the land of Egypt.' By a prophet (Moses), YHWH brought Israel "
                        "out of Egypt; by a prophet (Hosea), he preserves them now."
            }
        ]
    },

    {
        "id": "hosea-13",
        "ref": "Hosea 13",
        "chapter_num": 13,
        "title": "Death and Sheol -- The Final Judgment",
        "era": "hosea_judgment",
        "type": "chapter",

        "synopsis": "The darkest chapter in Hosea depicts the totality of divine judgment. Ephraim once spoke "
                    "with authority, but 'he incurred guilt through Baal and died' (13:1). The present "
                    "generation multiplies sin, making idols from silver -- 'kiss the calves!' (13:2). YHWH "
                    "recalls that he was Israel's God 'from the land of Egypt; you know no God but me, and "
                    "besides me there is no savior' (13:4). The devastating metaphor cascade: YHWH becomes "
                    "lion, leopard, bear robbed of her cubs -- tearing Israel open. 'Where is your king, to "
                    "save you in all your cities?' (13:10). Then the passage Paul will cite: 'Shall I ransom "
                    "them from the power of Sheol? Shall I redeem them from Death? O Death, where are your "
                    "plagues? O Sheol, where is your sting?' (13:14). In context, this is a taunt: YHWH "
                    "summons Death and Sheol against Israel. But Paul reads it christologically as a victory "
                    "cry -- death's sting is defeated through Christ's resurrection.",

        "key_verse": {
            "ref": "Hosea 13:14",
            "text": "I shall ransom them from the power of Sheol; I shall redeem them from Death. O Death, where are your plagues? O Sheol, where is your sting? Compassion is hidden from my eyes.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Sheol (the realm of the dead -- the underworld, the grave)",
            "mavet (Death -- personified as a power; in Canaanite mythology, Mot was the god of death)",
            "padah (ransom/redeem -- YHWH's capacity to buy back from Death itself)",
            "nocham (compassion/relenting -- 'compassion is hidden from my eyes'; YHWH will not relent)"
        ],

        "ane_backdrop": "The personification of Death (Mot) connects to Canaanite mythology, where Mot was "
                        "a divine being who swallowed Baal and held him in the underworld. In the divine "
                        "council framework, Death/Sheol is a hostile power -- not a place but a spiritual "
                        "entity that holds the dead. YHWH's claim to 'ransom from Sheol' asserts his "
                        "authority over even Death itself.",

        "second_temple": [
            {
                "source": "1 Corinthians 15:55",
                "summary": "Paul cites Hosea 13:14 as a victory cry at the resurrection: 'O death, where "
                           "is your victory? O death, where is your sting?'",
                "relevance": "Paul transforms Hosea's judgment taunt into a resurrection triumph -- what was "
                             "threatened against Israel becomes achieved for all believers through Christ."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 25:8", "note": "'He will swallow up death forever' -- the cosmic defeat of Mot/Death", "type": "ot"},
            {"ref": "1 Corinthians 15:54-57", "note": "Paul's resurrection hymn quoting Hosea 13:14 and Isaiah 25:8", "type": "nt"},
            {"ref": "Revelation 20:14", "note": "'Then Death and Hades were thrown into the lake of fire' -- the final defeat", "type": "nt"}
        ],

        "divine_council_note": "The personification of Death (Mot) and Sheol as powers with 'plagues' and "
                               "'sting' connects to the divine council cosmology. In the Ugaritic texts, Mot "
                               "is a divine being who swallows Baal. In the biblical framework, Death is a "
                               "hostile spiritual force that YHWH alone can overcome. Hosea 13:14 -- whether "
                               "read as judgment taunt or redemption promise -- asserts YHWH's sovereignty "
                               "over Death itself. Paul's christological reading reveals the ultimate "
                               "fulfillment: through Christ's resurrection, YHWH has ransomed his people from "
                               "Sheol and defeated Death as a cosmic power (Heb 2:14-15).",

        "sections": [
            {
                "heading": "Ephraim's Fatal Idolatry (13:1-3)",
                "body": "Once authoritative, Ephraim 'died' when he embraced Baal. Now they compound the "
                        "sin: silver idols, human craftsmanship, calf-kissing. They will vanish like "
                        "morning mist, chaff, and smoke -- the most ephemeral things in nature."
            },
            {
                "heading": "YHWH the Predator (13:4-8)",
                "body": "YHWH was Israel's God from Egypt, their only savior. He fed them in the "
                        "wilderness, and when they were satisfied, their hearts became proud. Now YHWH "
                        "becomes the predator: lion, leopard, bear robbed of her cubs. The divine "
                        "protector becomes the divine destroyer."
            },
            {
                "heading": "Death and Sheol Summoned (13:9-16)",
                "body": "Israel's king cannot save them. YHWH summons Death and Sheol against his people. "
                        "The east wind (Assyria) will blow, springs will dry up, and Samaria will bear "
                        "her guilt. The chapter ends with horrific images of conquest -- the ancient "
                        "reality of what happened when cities fell to invading armies."
            }
        ]
    },

    {
        "id": "hosea-14",
        "ref": "Hosea 14",
        "chapter_num": 14,
        "title": "Return to YHWH -- The Healing of Apostasy",
        "era": "hosea_judgment",
        "type": "chapter",

        "synopsis": "After thirteen chapters of accusation, metaphor, judgment, and anguished love, Hosea "
                    "closes with one of the most beautiful restoration passages in the prophetic literature. "
                    "'Return, O Israel, to YHWH your God, for you have stumbled because of your iniquity. "
                    "Take with you words and return to YHWH; say to him, \"Take away all iniquity; accept what "
                    "is good, and we will pay with bulls the vows of our lips\"' (14:1-2). Israel must "
                    "explicitly renounce the false saviors: 'Assyria shall not save us; we will not ride on "
                    "horses; and we will say no more, \"Our God,\" to the work of our hands' (14:3). YHWH's "
                    "response is pure grace: 'I will heal their apostasy; I will love them freely, for my "
                    "anger has turned from them' (14:4). The botanical imagery of restoration is lush: YHWH "
                    "will be like dew to Israel; Israel will blossom like the lily, take root like the trees "
                    "of Lebanon, and give forth fragrance like a garden. The book closes with a wisdom "
                    "admonition: 'Whoever is wise, let him understand these things... the ways of YHWH are "
                    "right, and the upright walk in them, but transgressors stumble in them' (14:9).",

        "key_verse": {
            "ref": "Hosea 14:4",
            "text": "I will heal their apostasy; I will love them freely, for my anger has turned from them.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "shub (return/repent -- the key verb of the entire book, here finally enacted genuinely)",
            "rapha (to heal -- 'I will heal their apostasy'; only YHWH can heal the sickness of unfaithfulness)",
            "nedavah (freely/voluntarily -- 'I will love them freely'; YHWH's love is uncaused, unearned)",
            "tal (dew -- YHWH as dew to Israel; life-giving moisture in an arid land)"
        ],

        "ane_backdrop": "The botanical restoration imagery (lily, Lebanon cedar, olive, grain, vine) reverses "
                        "the agricultural curses of the earlier chapters. In the ancient Near East, a "
                        "flourishing garden was the ultimate image of divine blessing and cosmic order. "
                        "The 'dew' metaphor is particularly powerful in the semi-arid Levant, where morning "
                        "dew was essential for summer agriculture.",

        "second_temple": [
            {
                "source": "Ezekiel 37:1-14",
                "summary": "Ezekiel's valley of dry bones -- national resurrection/restoration that "
                           "develops Hosea's healing-of-apostasy promise.",
                "relevance": "Both Hosea and Ezekiel envision YHWH restoring a dead nation to life through "
                             "the sheer power of divine love and divine Spirit."
            },
            {
                "source": "Romans 11:26-27",
                "summary": "Paul: 'And in this way all Israel will be saved... the Deliverer will come "
                           "from Zion, he will banish ungodliness from Jacob.'",
                "relevance": "Paul sees the ultimate fulfillment of Hosea's restoration promise in Israel's "
                             "eschatological salvation."
            }
        ],

        "cross_refs": [
            {"ref": "Jeremiah 3:22", "note": "'Return, O faithless children; I will heal your faithlessness' -- echoing Hosea 14:4", "type": "ot"},
            {"ref": "Ezekiel 37:1-14", "note": "The valley of dry bones -- national restoration/resurrection", "type": "ot"},
            {"ref": "Romans 11:26-27", "note": "Israel's eschatological salvation -- ultimate fulfillment of Hosea's promise", "type": "nt"},
            {"ref": "Song of Solomon 2:1-2", "note": "'I am a lily of the valleys' -- the same bloom imagery of restoration", "type": "ot"}
        ],

        "divine_council_note": "YHWH's declaration 'I will heal their apostasy; I will love them freely' "
                               "(14:4) is the divine council resolution to the cosmic drama. Israel's apostasy "
                               "-- their defection to the Baals, the corrupted sons of God -- is healed not by "
                               "Israel's effort but by YHWH's sovereign love. The renunciation of false saviors "
                               "(Assyria, horses, handmade gods) is a renunciation of the entire rival "
                               "spiritual system. The botanical imagery of restoration (lily, cedar, vine) "
                               "recalls Eden -- the garden where YHWH dwelt with humanity before the rebellions. "
                               "Hosea's final vision is an Edenic restoration: YHWH as the dew of life, Israel "
                               "as the flourishing garden, the hostile spiritual powers removed.",

        "sections": [
            {
                "heading": "The Call to Return (14:1-3)",
                "body": "Israel is given the very words to say: 'Take away all iniquity; accept what is "
                        "good.' They must renounce Assyria (political salvation), horses (military power), "
                        "and handmade gods (idolatry). The confession explicitly identifies the three "
                        "false saviors Israel has pursued throughout the book. 'In you the orphan finds "
                        "mercy' -- the most vulnerable find compassion in YHWH alone."
            },
            {
                "heading": "YHWH's Healing Love (14:4-7)",
                "body": "YHWH's response exceeds the request. He heals apostasy, loves freely, and "
                        "becomes the source of new life. The dew imagery is profound: in the Levant, "
                        "morning dew is the difference between life and death for summer crops. YHWH "
                        "himself becomes the invisible, life-sustaining moisture. Israel will blossom "
                        "like the lily, take root like Lebanon's cedars, spread like an olive tree."
            },
            {
                "heading": "The Wisdom Epilogue (14:8-9)",
                "body": "The book closes with a divine declaration ('I am like an evergreen cypress; "
                        "from me comes your fruit') and a wisdom admonition. 'The ways of YHWH are right' "
                        "-- the upright walk in them, transgressors stumble. This epilogue frames the "
                        "entire book as wisdom instruction: learn from Israel's catastrophe."
            }
        ]
    }
]
