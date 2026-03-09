"""
era_64.py -- Solomonic Proverbs: The Main Collection (Proverbs 10-22:16)

The heart of the book: 375 individual two-line proverbs attributed to Solomon.
These are not systematic theology but wisdom observation -- the accumulated
insights of careful living before God. The dominant form is antithetical
parallelism: righteous vs. wicked, wise vs. foolish, diligent vs. lazy.
The retribution principle is the general framework (righteousness leads to
life, wickedness to death), but individual proverbs acknowledge the complexity
of real life. Key themes: speech, wealth, family, justice, the king, and
the sovereignty of YHWH over all human plans.
"""

CHAPTERS = [
    {
        "id": "prov-10-12",
        "ref": "Proverbs 10-12",
        "chapter_num": 10,
        "title": "The Righteous and the Wicked -- Antithetical Wisdom",
        "era": "64",
        "type": "chapter",

        "synopsis": "Chapters 10-12 are dominated by antithetical parallelism: the first line states a "
                    "truth about the righteous or wise, the second line states the contrasting truth about "
                    "the wicked or foolish. 'The memory of the righteous is a blessing, but the name of "
                    "the wicked will rot' (10:7). These chapters establish the moral framework of the "
                    "entire collection. Key themes emerge: the power of speech ('The mouth of the "
                    "righteous is a fountain of life, but the mouth of the wicked conceals violence,' "
                    "10:11), the value of diligence ('A slack hand causes poverty, but the hand of the "
                    "diligent makes rich,' 10:4), and YHWH's sovereign oversight ('The eyes of YHWH are "
                    "in every place, keeping watch on the evil and the good'). The proverbs do not argue "
                    "for the retribution principle -- they observe it as the general pattern of creation's "
                    "moral order.",

        "key_verse": {
            "ref": "Proverbs 10:27",
            "text": "The fear of the LORD prolongs life, but the years of the wicked will be short.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tsaddiq (righteous -- the person aligned with God's moral order)",
            "rasha (wicked -- the person who violates God's moral order)",
            "peh (mouth -- the instrument of speech, either fountain of life or well of violence)",
            "charutz (diligent -- the industrious person whom wisdom commends)"
        ],

        "ane_backdrop": "The two-line antithetical proverb form is attested in Egyptian and Mesopotamian "
                        "wisdom literature. The Egyptian 'Instruction of Ptahhotep' and 'Instruction of "
                        "Amenemope' use similar contrastive structures. The Mesopotamian 'Counsels of "
                        "Wisdom' also contrast wise and foolish behavior. However, Proverbs' consistent "
                        "theological grounding -- 'the fear of YHWH' as the organizing principle -- "
                        "distinguishes it from the more pragmatic orientation of most ANE wisdom texts.",

        "second_temple": [
            {
                "source": "Sirach 5:1-6:4",
                "summary": "Ben Sira develops similar antithetical wisdom: warnings about wealth, "
                           "speech, and the contrast between faithful and unfaithful friends.",
                "relevance": "Shows the continuation of the Proverbs wisdom tradition into the "
                             "Second Temple period with similar form and content."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 12:36-37", "note": "'By your words you will be justified, and by your words you will be condemned' -- Jesus affirms the speech theology of Proverbs", "type": "nt"},
            {"ref": "James 3:1-12", "note": "The tongue as fire and fountain -- James develops Proverbs' extensive speech ethics", "type": "nt"},
            {"ref": "Psalm 1:1-6", "note": "The righteous/wicked contrast -- the psalm that introduces the Psalter uses the same framework", "type": "ot"},
            {"ref": "Galatians 6:7-9", "note": "'Whatever one sows, that will he also reap' -- the retribution principle stated in agricultural terms", "type": "nt"}
        ],

        "divine_council_note": "Proverbs 10-12 describe YHWH's active governance of the moral order: "
                               "'The eyes of YHWH are in every place, keeping watch on the evil and the "
                               "good' (15:3 -- anticipated here). 'YHWH does not let the righteous go "
                               "hungry, but he thwarts the craving of the wicked' (10:3). This is the "
                               "retribution principle as divine council administration: YHWH actively "
                               "manages the moral outcomes of human choices. The proverbs present this "
                               "as the normal operation of creation's moral fabric, woven by the Wisdom "
                               "who was present at creation (8:22-31).",

        "sections": [
            {
                "heading": "The Wise Son and the Foolish Son (10:1-16)",
                "body": "The collection opens: 'A wise son makes a glad father, but a foolish son is "
                        "a sorrow to his mother' (10:1). This domestic starting point roots cosmic "
                        "wisdom in family relationships. The proverbs then range across speech, wealth, "
                        "and moral character, always in antithetical form: 'Treasures gained by wickedness "
                        "do not profit, but righteousness delivers from death' (10:2); 'Whoever walks in "
                        "integrity walks securely, but he who makes his ways crooked will be found out' "
                        "(10:9). The density is remarkable -- each verse is a self-contained wisdom unit "
                        "that rewards extended meditation."
            },
            {
                "heading": "Speech, Wealth, and Community (10:17-11:31)",
                "body": "The power of speech dominates: 'When words are many, transgression is not lacking, "
                        "but whoever restrains his lips is prudent' (10:19). Wealth is complex: 'A rich "
                        "man's wealth is his strong city; the poverty of the poor is their ruin' (10:15) -- "
                        "an observation, not necessarily an endorsement. The community dimension emerges: "
                        "'Where there is no guidance, a people falls, but in an abundance of counselors "
                        "there is safety' (11:14). The retribution principle is stated with confidence: "
                        "'The righteous is delivered from trouble, and the wicked walks into it instead' "
                        "(11:8). Yet 11:24 adds nuance: 'One gives freely, yet grows all the richer; "
                        "another withholds what he should give, and only suffers want' -- generosity, "
                        "paradoxically, enriches."
            },
            {
                "heading": "The Character of the Righteous (12:1-28)",
                "body": "Chapter 12 develops the character portrait of the wise person. 'Whoever loves "
                        "discipline loves knowledge, but he who hates reproof is stupid' (12:1). The "
                        "righteous person is characterized by truthfulness ('Lying lips are an abomination "
                        "to YHWH, but those who act faithfully are his delight,' 12:22), diligence ('The "
                        "hand of the diligent will rule, while the slothful will be put to forced labor,' "
                        "12:24), and emotional restraint ('A prudent man conceals knowledge, but the heart "
                        "of fools proclaims folly,' 12:23). The chapter concludes: 'In the path of "
                        "righteousness is life, and in its pathway there is no death' (12:28)."
            }
        ]
    },

    {
        "id": "prov-13-15",
        "ref": "Proverbs 13-15",
        "chapter_num": 13,
        "title": "YHWH's Oversight, Wealth, and the Tongue",
        "era": "64",
        "type": "chapter",

        "synopsis": "Chapters 13-15 continue the antithetical proverb collection with increasing "
                    "theological depth. 'Hope deferred makes the heart sick, but a desire fulfilled is "
                    "a tree of life' (13:12). The 'tree of life' allusion connects practical wisdom to "
                    "Eden's eschatological promise. Chapter 14 introduces a key epistemological insight: "
                    "'There is a way that seems right to a man, but its end is the way to death' (14:12). "
                    "Human moral intuition is unreliable without the fear of YHWH. Chapter 15 features "
                    "some of the most frequently quoted proverbs: 'A soft answer turns away wrath, but a "
                    "harsh word stirs up anger' (15:1); 'The eyes of YHWH are in every place, keeping "
                    "watch on the evil and the good' (15:3); 'Better is a little with the fear of YHWH "
                    "than great treasure and trouble with it' (15:16).",

        "key_verse": {
            "ref": "Proverbs 15:3",
            "text": "The eyes of the LORD are in every place, keeping watch on the evil and the good.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ets chayyim (tree of life -- the Eden motif reappearing in wisdom, applied to desire fulfilled, 13:12)",
            "toeivat YHWH (abomination to YHWH -- actions that YHWH finds detestable, a strong ethical category)",
            "ratson YHWH (delight/favor of YHWH -- what pleases God, the positive counterpart to abomination)",
            "marpe (healing -- the healing power of gentle speech, 15:4)"
        ],

        "ane_backdrop": "The concept of divine surveillance ('the eyes of YHWH in every place,' 15:3) "
                        "is paralleled in Egyptian theology where the sun-god Re sees all things, and in "
                        "Mesopotamian texts where Shamash (the sun-god of justice) sees every deed. "
                        "Proverbs monotheizes this concept: it is YHWH alone who watches all.",

        "second_temple": [
            {
                "source": "Sirach 15:11-20",
                "summary": "Ben Sira insists that God does not command sin: 'Do not say, \"It was "
                           "the Lord's doing that I fell away.\" He has not done what he detests.'",
                "relevance": "Engages with the theological tension between YHWH's sovereignty "
                             "(Proverbs 15:3) and human moral responsibility."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 4:13", "note": "'No creature is hidden from his sight, but all are naked and exposed to the eyes of him to whom we must give account' -- the NT develops Proverbs 15:3", "type": "nt"},
            {"ref": "Genesis 2:9", "note": "The tree of life in Eden -- Proverbs 13:12 and 15:4 use the same motif for wisdom's blessings", "type": "ot"},
            {"ref": "Romans 12:18", "note": "'If possible, so far as it depends on you, live peaceably with all' -- the soft-answer wisdom of 15:1", "type": "nt"},
            {"ref": "Proverbs 14:12", "note": "'There is a way that seems right to a man' -- repeated verbatim in 16:25, emphasizing this critical warning", "type": "ot"}
        ],

        "divine_council_note": "Proverbs 15:3 -- 'The eyes of YHWH are in every place, keeping watch "
                               "on the evil and the good' -- presents YHWH as the omniscient sovereign "
                               "who monitors all human conduct. In the divine council framework, this "
                               "surveillance is exercised through YHWH's own omniscience and through the "
                               "agency of his council members. Proverbs 15:11 adds: 'Sheol and Abaddon "
                               "lie open before YHWH; how much more the hearts of the children of man!' "
                               "Even the underworld cannot hide from YHWH's gaze. This undergirds the "
                               "moral confidence of the entire proverb collection: justice is administered "
                               "by an all-seeing God.",

        "sections": [
            {
                "heading": "Wealth, Speech, and the Tree of Life (13:1-25)",
                "body": "Chapter 13 continues the antithetical pattern with gems of observation: 'Wealth "
                        "gained hastily will dwindle, but whoever gathers little by little will increase "
                        "it' (13:11). The tree of life motif appears: 'Hope deferred makes the heart sick, "
                        "but a desire fulfilled is a tree of life' (13:12). The 'tree of life' (ets "
                        "chayyim) connects practical wisdom to Eden's cosmic promise -- wisdom offers in "
                        "partial form what humanity lost through the fall. Speech remains central: 'Whoever "
                        "guards his mouth preserves his life; he who opens wide his lips comes to ruin' "
                        "(13:3)."
            },
            {
                "heading": "The Way That Seems Right (14:1-35)",
                "body": "Chapter 14 contains one of the most sobering warnings in the book: 'There is a "
                        "way that seems right to a man, but its end is the way to death' (14:12). Human "
                        "moral intuition is not trustworthy without the corrective of wisdom and the fear "
                        "of YHWH. The chapter also contains social-justice proverbs: 'Whoever oppresses "
                        "a poor man insults his Maker, but he who is generous to the needy honors him' "
                        "(14:31). The Creator-creature relationship grounds social ethics: the poor bear "
                        "God's image, and their mistreatment is an insult to their Maker."
            },
            {
                "heading": "The Eyes of YHWH and the Gentle Tongue (15:1-33)",
                "body": "Chapter 15 is among the richest in the collection. The opening proverb -- 'A "
                        "soft answer turns away wrath, but a harsh word stirs up anger' (15:1) -- is "
                        "matched by the theological assertion: 'The eyes of YHWH are in every place, "
                        "keeping watch on the evil and the good' (15:3). The 'better than' proverbs "
                        "appear: 'Better is a little with the fear of YHWH than great treasure and "
                        "trouble with it' (15:16); 'Better is a dinner of herbs where love is than a "
                        "fattened ox and hatred with it' (15:17). These qualify the retribution principle: "
                        "material prosperity is not the ultimate good. The chapter concludes with another "
                        "wisdom axiom: 'The fear of YHWH is instruction in wisdom, and humility comes "
                        "before honor' (15:33)."
            }
        ]
    },

    {
        "id": "prov-16-19",
        "ref": "Proverbs 16-19",
        "chapter_num": 16,
        "title": "YHWH's Sovereignty and the King's Justice",
        "era": "64",
        "type": "chapter",

        "synopsis": "Chapters 16-19 are the theological core of the Solomonic collection. Chapter 16 "
                    "opens with a cluster of YHWH-proverbs that assert divine sovereignty over all human "
                    "plans: 'The plans of the heart belong to man, but the answer of the tongue is from "
                    "YHWH' (16:1); 'The lot is cast into the lap, but its every decision is from YHWH' "
                    "(16:33). The king appears as YHWH's representative: 'Inspired decisions are on the "
                    "lips of a king; his mouth does not sin in judgment' (16:10). Pride -- the fundamental "
                    "vice -- is addressed: 'Pride goes before destruction, and a haughty spirit before a "
                    "fall' (16:18). Friendship, speech, and the complexity of justice continue as themes: "
                    "'A friend loves at all times, and a brother is born for adversity' (17:17); 'Even a "
                    "fool who keeps silent is considered wise' (17:28).",

        "key_verse": {
            "ref": "Proverbs 16:33",
            "text": "The lot is cast into the lap, but its every decision is from the LORD.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "lev (heart -- the seat of human planning, which YHWH ultimately overrules, 16:1, 9)",
            "gaavah (pride -- the root sin that Proverbs identifies as the path to destruction, 16:18)",
            "goral (lot -- the casting of lots, whose every outcome YHWH determines, 16:33)",
            "qesem (divination/inspired decision -- the king's role as channel of divine justice, 16:10)"
        ],

        "ane_backdrop": "The concept of the king as the channel of divine justice is central to ANE royal "
                        "ideology. The Mesopotamian king was the 'shepherd' appointed by the gods to "
                        "maintain cosmic order (misharu). The Egyptian pharaoh embodied Ma'at (cosmic "
                        "order). Proverbs' royal proverbs reflect this tradition: the king's lips carry "
                        "'inspired decisions' (qesem, 16:10), suggesting oracular authority. The casting "
                        "of lots (16:33) was used in both Israelite and ANE decision-making as a means "
                        "of determining the divine will (cf. the Urim and Thummim, Leviticus 8:8).",

        "second_temple": [
            {
                "source": "Sirach 33:7-15",
                "summary": "Ben Sira develops the theme of divine sovereignty: 'Good is the opposite "
                           "of evil, and life the opposite of death... Look upon all the works of the "
                           "Most High; they come in pairs, one the opposite of the other.'",
                "relevance": "Develops Proverbs' antithetical wisdom into a broader theological "
                             "framework of divine ordering of opposites."
            }
        ],

        "cross_refs": [
            {"ref": "James 4:13-16", "note": "'You do not know what tomorrow will bring' -- James echoes 16:1, 9 on human planning and divine sovereignty", "type": "nt"},
            {"ref": "Acts 1:26", "note": "The apostles cast lots to choose Matthias -- the practice affirmed in 16:33 as under YHWH's control", "type": "nt"},
            {"ref": "1 Peter 5:5-6", "note": "'God opposes the proud but gives grace to the humble' (quoting Prov 3:34) -- the anti-pride theme of 16:18", "type": "nt"},
            {"ref": "Romans 13:1-4", "note": "Governing authority as God's servant for justice -- developing the royal proverbs' theology", "type": "nt"}
        ],

        "divine_council_note": "The YHWH-proverbs of chapter 16 present the most concentrated statement "
                               "of divine sovereignty in the wisdom literature. 'The plans of the heart "
                               "belong to man, but the answer of the tongue is from YHWH' (16:1). 'YHWH "
                               "has made everything for its purpose, even the wicked for the day of "
                               "trouble' (16:4). 'The lot is cast into the lap, but its every decision is "
                               "from YHWH' (16:33). This is the divine council worldview applied to "
                               "everyday life: nothing escapes YHWH's governance. Even seemingly random "
                               "events (the casting of lots) are under divine control. The king who "
                               "governs justly participates in the divine council's administration of "
                               "justice on earth.",

        "sections": [
            {
                "heading": "YHWH's Sovereignty Over Human Plans (16:1-33)",
                "body": "Chapter 16 opens with a stunning cluster of YHWH-proverbs: 'The plans of the "
                        "heart belong to man, but the answer of the tongue is from YHWH' (16:1). 'Commit "
                        "your work to YHWH, and your plans will be established' (16:3). 'YHWH has made "
                        "everything for its purpose, even the wicked for the day of trouble' (16:4). 'The "
                        "heart of man plans his way, but YHWH establishes his steps' (16:9). This is "
                        "sovereignty theology in proverbial form: human initiative is real but operates "
                        "within divine governance. The famous 16:18 warns: 'Pride goes before destruction, "
                        "and a haughty spirit before a fall.' The chapter closes with the lot proverb "
                        "(16:33), establishing that even randomness is divinely directed."
            },
            {
                "heading": "Friendship, Conflict, and the Fool (17:1-18:24)",
                "body": "These chapters explore social relationships with penetrating insight. 'Better is "
                        "a dry morsel with quiet than a house full of feasting with strife' (17:1). 'A "
                        "friend loves at all times, and a brother is born for adversity' (17:17). The fool "
                        "is diagnosed: 'A rebuke goes deeper into a man of understanding than a hundred "
                        "blows into a fool' (17:10); 'Even a fool who keeps silent is considered wise; "
                        "when he closes his lips, he is deemed intelligent' (17:28). Chapter 18 adds: "
                        "'A man who isolates himself seeks his own desire; he breaks out against all "
                        "sound judgment' (18:1). The chapter culminates: 'The name of YHWH is a strong "
                        "tower; the righteous man runs into it and is safe' (18:10)."
            },
            {
                "heading": "Poverty, Justice, and Domestic Life (19:1-29)",
                "body": "Chapter 19 addresses poverty with sympathy and complexity: 'Better is a poor "
                        "person who walks in his integrity than one who is crooked in speech and is a "
                        "fool' (19:1). Poverty attracts neither friends nor favor: 'Wealth brings many "
                        "new friends, but a poor man is deserted by his friend' (19:4). Social justice "
                        "is grounded theologically: 'Whoever is generous to the poor lends to YHWH, and "
                        "he will repay him for his deed' (19:17). The family proverbs are vivid: 'A "
                        "foolish son is ruin to his father, and a wife's quarreling is a continual "
                        "dripping of rain' (19:13). Discipline of children is advocated: 'Discipline "
                        "your son, for there is hope; do not set your heart on putting him to death' "
                        "(19:18)."
            }
        ]
    },

    {
        "id": "prov-20-22a",
        "ref": "Proverbs 20-22:16",
        "chapter_num": 20,
        "title": "The Close of the Solomonic Collection",
        "era": "64",
        "type": "chapter",

        "synopsis": "The Solomonic collection concludes with proverbs on kingship, justice, and the "
                    "heart. 'The king's heart is a stream of water in the hand of YHWH; he turns it "
                    "wherever he will' (21:1) -- even royal power is under divine sovereignty. 'Every "
                    "way of a man is right in his own eyes, but YHWH weighs the heart' (21:2) -- human "
                    "self-assessment is unreliable. 'To do righteousness and justice is more acceptable "
                    "to YHWH than sacrifice' (21:3) -- echoing the prophetic critique of empty ritual "
                    "(Isaiah 1:11-17; Micah 6:6-8). The section closes with 22:1-16, including: 'A good "
                    "name is to be chosen rather than great riches, and favor is better than silver or "
                    "gold' (22:1); 'Train up a child in the way he should go; even when he is old he "
                    "will not depart from it' (22:6).",

        "key_verse": {
            "ref": "Proverbs 21:1",
            "text": "The king's heart is a stream of water in the hand of the LORD; he turns it wherever he will.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "palge mayim (streams of water -- the irrigation-channel metaphor for YHWH directing the king's will)",
            "taqan (to weigh/test -- YHWH's evaluation of the heart, beyond human self-assessment, 21:2)",
            "shem tov (good name -- reputation and character as more valuable than wealth, 22:1)",
            "chanakh (to train/dedicate -- the education of the child in wisdom's path, 22:6)"
        ],

        "ane_backdrop": "The irrigation metaphor of 21:1 ('the king's heart is a stream of water in "
                        "YHWH's hand') draws on the agricultural reality of ancient irrigation: channels "
                        "were directed by the farmer to water specific fields. The image presents even "
                        "the most powerful human (the king) as a channel YHWH directs at will. The "
                        "preference for justice over sacrifice (21:3) echoes a theme found across the "
                        "prophetic tradition and in Egyptian wisdom (the Instruction of Merikare: "
                        "'More acceptable is the character of one upright of heart than the ox of the "
                        "evildoer').",

        "second_temple": [
            {
                "source": "Sirach 7:1-36",
                "summary": "A collection of ethical instructions covering speech, friendship, family, "
                           "and worship -- developing the same themes as Proverbs 20-22:16.",
                "relevance": "Demonstrates the ongoing vitality of the proverbial wisdom tradition "
                             "into the Hellenistic period."
            }
        ],

        "cross_refs": [
            {"ref": "Ezra 1:1", "note": "'YHWH stirred up the spirit of Cyrus king of Persia' -- the historical illustration of 21:1", "type": "ot"},
            {"ref": "1 Samuel 15:22", "note": "'To obey is better than sacrifice' -- the prophetic parallel to 21:3", "type": "ot"},
            {"ref": "Mark 12:38-44", "note": "The widow's mite -- Jesus values the heart over the amount, as 21:2-3 implies", "type": "nt"},
            {"ref": "Ephesians 6:4", "note": "'Bring them up in the discipline and instruction of the Lord' -- the NT form of 22:6", "type": "nt"}
        ],

        "divine_council_note": "Proverbs 21:1 is one of the strongest sovereignty statements in the "
                               "wisdom literature: 'The king's heart is a stream of water in the hand of "
                               "YHWH; he turns it wherever he will.' In the divine council framework, this "
                               "means that even human political power operates under YHWH's sovereign "
                               "direction. The kings of the earth may rage (Psalm 2:1-2), but their hearts "
                               "are channels YHWH directs. Proverbs 21:30 makes the point absolute: 'No "
                               "wisdom, no understanding, no counsel can avail against YHWH.' No human plan "
                               "and no spiritual strategy can override the divine council's sovereign.",

        "sections": [
            {
                "heading": "Wine, the King, and Divine Sovereignty (20:1-30)",
                "body": "Chapter 20 opens: 'Wine is a mocker, strong drink a brawler, and whoever is "
                        "led astray by it is not wise' (20:1). The king's authority is emphasized: 'The "
                        "terror of a king is like the growling of a lion; whoever provokes him to anger "
                        "forfeits his life' (20:2). Human self-knowledge is limited: 'Who can say, \"I "
                        "have made my heart pure; I am clean from my sin\"?' (20:9). The chapter contains "
                        "practical commercial ethics: 'Unequal weights and unequal measures are both alike "
                        "an abomination to YHWH' (20:10, 23). YHWH's oversight is comprehensive: 'The "
                        "spirit (neshamah) of man is the lamp of YHWH, searching all his innermost parts' "
                        "(20:27)."
            },
            {
                "heading": "The King's Heart and Justice Over Sacrifice (21:1-31)",
                "body": "Chapter 21 opens with the sovereignty-of-the-king proverb (21:1) and the "
                        "heart-weighing proverb (21:2), establishing YHWH's absolute authority over all "
                        "human power and self-assessment. The prophetic wisdom tradition emerges: 'To do "
                        "righteousness and justice is more acceptable to YHWH than sacrifice' (21:3). "
                        "The chapter diagnoses various forms of folly: the proud (21:4, 24), the lazy "
                        "(21:25-26), the violent (21:7), and the contentious wife (21:9, 19). The "
                        "conclusion is absolute: 'The horse is made ready for the day of battle, but "
                        "the victory belongs to YHWH' (21:31)."
            },
            {
                "heading": "A Good Name, the Child, and the Close (22:1-16)",
                "body": "The final section of the Solomonic collection contains some of the most beloved "
                        "proverbs. 'A good name is to be chosen rather than great riches, and favor is "
                        "better than silver or gold' (22:1). 'The rich and the poor meet together; YHWH "
                        "is the Maker of them all' (22:2) -- social-economic equality grounded in creation "
                        "theology. 'Train up a child in the way he should go; even when he is old he will "
                        "not depart from it' (22:6) -- the foundational education proverb (though 'the "
                        "way he should go' may mean 'according to his own way/nature,' i.e., personalized "
                        "education). The collection closes at 22:16 with a warning: 'Whoever oppresses "
                        "the poor to increase his own wealth, or gives to the rich, will only come to "
                        "poverty.'"
            }
        ]
    }
]
