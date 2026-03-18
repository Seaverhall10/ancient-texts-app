"""
era_66.py -- Under the Sun: The Search Begins (Ecclesiastes 1-6)

The first half of Ecclesiastes establishes Qoheleth's thesis and conducts the
great experiment. The argument spirals: Qoheleth raises a theme, probes it,
qualifies it, and returns to it later with deeper insight. The chapters here
cover the thesis and royal experiment (1-2), the times poem and divine
sovereignty (3-4), and wisdom for worship and wealth (5-6). By the end of
chapter 6, Qoheleth has tested wisdom, pleasure, work, and wealth -- all are
hebel. Yet within the hebel, God gives enjoyment as a gift (2:24; 3:12-13;
5:18-20). The second half of the book (era_66b_fear_god) pushes toward the
limits of wisdom and the final verdict: fear God.
"""

CHAPTERS = [
    {
        "id": "eccl-1-2",
        "ref": "Ecclesiastes 1-2",
        "chapter_num": 1,
        "title": "The Thesis and the Royal Experiment",
        "era": "66",
        "type": "chapter",
        "themes": ["PROV", "DC"],

        "synopsis": "Qoheleth opens with the thesis that will govern the entire book: 'Vanity of "
                    "vanities (havel havalim), says the Preacher, vanity of vanities! All is vanity "
                    "(hebel)' (1:2). The Hebrew superlative -- 'hebel of hebels' -- is the strongest "
                    "possible statement: everything is utterly vapor. The poem on cyclical nature "
                    "(1:4-11) establishes the frame: generations come and go, the sun rises and sets, "
                    "the wind circuits the earth, the rivers run to the sea but the sea is not full. "
                    "'There is nothing new under the sun' (1:9). Qoheleth then adopts the Solomonic "
                    "persona: 'I the Preacher have been king over Israel in Jerusalem' (1:12). He "
                    "conducts a royal experiment, testing wisdom (1:13-18), pleasure (2:1-11), and "
                    "work (2:12-23) to determine what is 'good for the children of man to do under "
                    "heaven' (2:3). His verdict: wisdom exceeds folly (2:13) but cannot prevent death "
                    "(2:14-16); pleasure is hebel (2:1); work is futile because its fruits pass to "
                    "others (2:18-23). The chapter closes with the first of seven 'enjoyment passages': "
                    "'There is nothing better for a person than that he should eat and drink and find "
                    "enjoyment in his toil. This also, I saw, is from the hand of God' (2:24).",

        "key_verse": {
            "ref": "Ecclesiastes 1:2",
            "text": "Vanity of vanities, says the Preacher, vanity of vanities! All is vanity.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "hebel (vapor/breath/vanity -- the key word of the book, appearing 38 times; transience, futility, absurdity)",
            "tachath hashamesh (under the sun -- the frame for Qoheleth's investigation: earthly, human-level observation)",
            "yitron (profit/gain -- the economic metaphor: what lasting advantage does life produce? Answer: none)",
            "ra'yon ruach (striving after wind/shepherding wind -- the futility of human effort to grasp the ungraspable)",
            "inyan (business/task -- the toil God has given humanity, which is simultaneously burden and gift)"
        ],

        "ane_backdrop": "The cyclical nature poem (1:4-11) has close parallels in Mesopotamian literature. "
                        "The Gilgamesh Epic's reflection on the permanence of nature versus the transience "
                        "of human life is the closest ANE parallel: 'Only the gods live forever under the "
                        "sun. As for mankind, numbered are their days.' The alewife Siduri's counsel to "
                        "Gilgamesh -- 'Fill your belly. Day and night make merry. Let days be full of "
                        "joy... This is the task of mankind' -- remarkably parallels Qoheleth's enjoyment "
                        "passages. The Egyptian 'Harper's Songs' from Middle Kingdom tomb paintings "
                        "similarly urge enjoyment in the face of death: 'Make holiday! Do not weary of "
                        "it!' The Babylonian 'Dialogue of Pessimism' (~1000 BC) debates the value of "
                        "various human activities with a comparable skeptical tone.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 2:1-9",
                "summary": "The wicked reason: 'Our life is short and sorrowful, and there is no "
                           "remedy when a man comes to his end... Come therefore, let us enjoy the "
                           "good things that exist.'",
                "relevance": "Wisdom of Solomon puts Qoheleth-like language in the mouths of the "
                             "wicked, then refutes it with the promise of immortality (3:1-9). This "
                             "shows the later tradition's anxiety about Ecclesiastes' apparent hedonism."
            },
            {
                "source": "4QQoh^a (4Q109)",
                "summary": "A Dead Sea Scrolls fragment preserving portions of Ecclesiastes 5-7, "
                           "dating to ~175-150 BC.",
                "relevance": "The oldest manuscript evidence for Ecclesiastes, confirming the book "
                             "existed in its current form by the mid-2nd century BC."
            }
        ],

        "cross_refs": [
            {"ref": "Romans 8:20", "note": "'The creation was subjected to futility (mataiotes)' -- Paul uses the LXX's word for 'hebel' in a cosmic scope", "type": "nt"},
            {"ref": "James 4:14", "note": "'You are a mist that appears for a little time and then vanishes' -- the hebel of human life", "type": "nt"},
            {"ref": "Psalm 39:5-6", "note": "'You have made my days a few handbreadths, and my lifetime is as nothing before you. Surely all mankind stands as a mere breath (hebel)'", "type": "ot"},
            {"ref": "Matthew 6:19-21", "note": "'Do not lay up for yourselves treasures on earth' -- Jesus addresses the futility of earthly accumulation that Qoheleth documents", "type": "nt"},
            {"ref": "Luke 12:13-21", "note": "The parable of the rich fool -- accumulating wealth for oneself and not being 'rich toward God'", "type": "nt"}
        ],

        "divine_council_note": "Qoheleth's investigation is deliberately limited to what can be observed "
                               "'under the sun' (1:3, 9, 14). This framing is theologically significant: "
                               "the divine council operates above the sun, and its governance cannot be "
                               "discerned from the earthly vantage point. The hebel Qoheleth observes -- "
                               "the apparent meaninglessness of the retribution principle's failures -- is "
                               "not the whole picture but only the human-visible portion. The 'eternity in "
                               "the heart' (3:11) hints at a reality beyond the sun that would resolve "
                               "what Qoheleth cannot.",

        "sections": [
            {
                "heading": "The Thesis: All Is Hebel (1:1-11)",
                "body": "The opening verse identifies the speaker: 'The words of the Qoheleth, the son "
                        "of David, king in Jerusalem' (1:1). The thesis follows immediately: 'Havel "
                        "havalim, says the Qoheleth, havel havalim! All is hebel' (1:2). The superlative "
                        "construction ('hebel of hebels') is the strongest form in Hebrew -- compare 'Song "
                        "of Songs' (the supreme song), 'Holy of Holies' (the most holy place). Then the "
                        "nature poem: 'A generation goes, and a generation comes, but the earth remains "
                        "forever' (1:4). The sun, wind, and rivers all cycle endlessly. 'There is nothing "
                        "new under the sun' (1:9) -- and even if something appears new, it has been "
                        "forgotten from a previous age (1:10-11). The frame is set: human life is "
                        "embedded in an endlessly repetitive cosmos that absorbs every achievement."
            },
            {
                "heading": "The Experiment: Wisdom, Pleasure, and Work (1:12-2:23)",
                "body": "Qoheleth adopts the Solomonic persona and conducts three experiments. First, "
                        "wisdom: 'I applied my heart to seek and to search out by wisdom all that is "
                        "done under heaven. It is an unhappy business (inyan ra) that God has given to "
                        "the children of man to be busy with' (1:13). The verdict: 'In much wisdom is "
                        "much vexation, and he who increases knowledge increases sorrow' (1:18). Second, "
                        "pleasure: 'I said in my heart, \"Come now, I will test you with pleasure; enjoy "
                        "yourself\"' (2:1). He built houses, planted vineyards, made gardens and parks, "
                        "acquired servants, amassed silver and gold, hired singers (2:4-8). 'And whatever "
                        "my eyes desired I did not keep from them' (2:10). The verdict: 'Then I considered "
                        "all that my hands had done... and behold, all was hebel and a striving after "
                        "wind' (2:11). Third, work: even wise work is futile because the worker must "
                        "leave its fruits to 'a man who did not toil for it' (2:21)."
            },
            {
                "heading": "The First Enjoyment Passage (2:24-26)",
                "body": "After demolishing every human foundation for meaning, Qoheleth offers the first "
                        "positive counsel: 'There is nothing better for a person than that he should eat "
                        "and drink and find enjoyment in his toil. This also, I saw, is from the hand of "
                        "God' (2:24). The enjoyment is not a solution to the hebel but a gift within it. "
                        "God gives 'wisdom and knowledge and joy' to the one 'who pleases him' (2:26), "
                        "but even this distinction seems arbitrary to Qoheleth -- it is 'also hebel and "
                        "a striving after wind' (2:26). The paradox is essential: the gifts are real but "
                        "the giver's distribution is inscrutable."
            }
        ]
    },

    {
        "id": "eccl-3-4",
        "ref": "Ecclesiastes 3-4",
        "chapter_num": 3,
        "title": "The Times Poem and the Eternity in the Heart",
        "era": "66",
        "type": "chapter",
        "themes": ["PROV", "DC", "SPIRIT"],

        "synopsis": "Chapter 3 contains the most famous poem in Ecclesiastes: 'For everything there is "
                    "a season, and a time for every matter under heaven: a time to be born, and a time to "
                    "die' (3:1-2). The fourteen pairs of opposites (3:2-8) encompass the full range of "
                    "human experience. Qoheleth's theological reflection follows: 'He has made everything "
                    "beautiful in its time. Also, he has put eternity (olam) into man's heart, yet so "
                    "that he cannot find out what God has done from the beginning to the end' (3:11). "
                    "This is Qoheleth's most profound theological statement: God has embedded a sense "
                    "of transcendence in the human soul but withholds the ability to comprehend the "
                    "divine plan. Chapter 3 also addresses justice: 'In the place of justice, even "
                    "there was wickedness' (3:16). Qoheleth affirms that 'God will judge the righteous "
                    "and the wicked' (3:17) but then pushes further: are humans really different from "
                    "animals? 'Who knows whether the spirit of man goes upward and the spirit of the "
                    "beast goes down into the earth?' (3:21). Chapter 4 examines oppression (4:1-3), "
                    "rivalry (4:4-6), loneliness (4:7-12), and political futility (4:13-16).",

        "key_verse": {
            "ref": "Ecclesiastes 3:11",
            "text": "He has made everything beautiful in its time. Also, he has put eternity into man's heart, yet so that he cannot find out what God has done from the beginning to the end.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "et (time/appointed time -- the right moment for each activity, divinely determined)",
            "olam (eternity/the world/long duration -- placed in the human heart but remaining incomprehensible)",
            "yapheh (beautiful/fitting -- everything is appropriate in its divinely appointed time)",
            "chevel (cord/companionship -- 'a threefold cord is not quickly broken,' 4:12)"
        ],

        "ane_backdrop": "The concept of divinely appointed times is paralleled in Mesopotamian omen "
                        "literature and the belief that the gods control the 'destinies' (shimtu) of "
                        "all things. The Egyptian concept of Ma'at includes the idea that everything "
                        "has its proper time and place within the cosmic order. The contrast between "
                        "human and animal death (3:19-21) echoes the Gilgamesh Epic's preoccupation "
                        "with mortality: Gilgamesh learns that immortality belongs to the gods alone.",

        "second_temple": [
            {
                "source": "Sirach 39:16-35",
                "summary": "'All the works of the Lord are good, and he will supply every need in "
                           "its time. No one can say, \"This is not as good as that.\"'",
                "relevance": "Ben Sira's more optimistic response to Ecclesiastes 3:11 -- affirming "
                             "divine timing without Qoheleth's existential anxiety about human "
                             "inability to comprehend it."
            },
            {
                "source": "1QS (Rule of the Community) III:13-IV:26",
                "summary": "The Qumran community believed in divinely appointed 'times' and 'seasons' "
                           "for all things, including the eschatological 'time of visitation.'",
                "relevance": "Shows how the concept of divinely appointed times developed into a "
                             "full eschatological framework in Second Temple Judaism."
            }
        ],

        "cross_refs": [
            {"ref": "Acts 17:26-27", "note": "God 'determined allotted periods and the boundaries of their dwelling place, that they should seek God' -- divine timing with the purpose Qoheleth glimpses", "type": "nt"},
            {"ref": "2 Peter 3:8", "note": "'With the Lord one day is as a thousand years' -- divine time transcends human perception, as Qoheleth sensed", "type": "nt"},
            {"ref": "Genesis 3:22-24", "note": "The tree of life guarded after the fall -- the eternity in the heart (3:11) denied access by sin", "type": "ot"},
            {"ref": "Romans 8:19-22", "note": "Creation groaning -- the cosmic 'hebel' that Ecclesiastes observes at the personal level", "type": "nt"},
            {"ref": "Psalm 90:2-6", "note": "'From everlasting to everlasting you are God... a thousand years in your sight are but as yesterday' -- the divine perspective Qoheleth cannot access", "type": "ot"}
        ],

        "divine_council_note": "Ecclesiastes 3:11 is theologically pivotal for the divine council "
                               "framework. God has placed 'olam' (eternity, the world, long duration) "
                               "in the human heart -- a capacity for transcendence, an awareness that "
                               "there is more than what meets the eye -- 'yet so that he cannot find out "
                               "what God has done from the beginning to the end.' Humans sense the unseen "
                               "realm but cannot penetrate it. This is the 'under the sun' limitation: "
                               "the divine council's operations, the unseen spiritual governance, the "
                               "cosmic purposes behind suffering and injustice -- all of this exists but "
                               "remains hidden from earthly observation. The fear of God (3:14) is the "
                               "appropriate response to this cognitive boundary.",

        "sections": [
            {
                "heading": "The Times Poem: A Time for Everything (3:1-8)",
                "body": "The poem is structured as fourteen pairs of opposites: 'A time to be born, and "
                        "a time to die; a time to plant, and a time to pluck up what is planted; a time "
                        "to kill, and a time to heal; a time to break down, and a time to build up; a "
                        "time to weep, and a time to laugh; a time to mourn, and a time to dance' (3:2-4). "
                        "The list encompasses the full range of human experience -- creation and "
                        "destruction, joy and grief, intimacy and distance, speech and silence, war and "
                        "peace. The poetic structure implies that all these opposites are divinely "
                        "appointed: there is a 'time' (et) for each, suggesting sovereign ordering "
                        "rather than random chaos."
            },
            {
                "heading": "Eternity in the Heart (3:9-15)",
                "body": "Qoheleth asks: 'What gain (yitron) has the worker from his toil?' (3:9). The "
                        "answer comes in the theological masterpiece of verse 11: 'He has made everything "
                        "beautiful in its time. Also, he has put eternity (olam) into man's heart, yet so "
                        "that he cannot find out what God has done from the beginning to the end.' Three "
                        "truths: (1) God's ordering is 'beautiful' (yapheh) -- there is aesthetic and "
                        "moral rightness to the divine plan. (2) Humans have an awareness of transcendence "
                        "-- the capacity to sense the eternal. (3) But human cognition cannot grasp the "
                        "full scope of God's work. The result: 'I perceived that whatever God does endures "
                        "forever; nothing can be added to it, nor anything taken from it. God has done it, "
                        "so that people fear before him' (3:14). The fear of God arises from the encounter "
                        "with divine incomprehensibility."
            },
            {
                "heading": "Justice, Death, and the Human-Animal Question (3:16-4:16)",
                "body": "Qoheleth observes injustice: 'In the place of justice, even there was "
                        "wickedness' (3:16). He affirms that God will judge (3:17) but then raises the "
                        "most provocative question in the book: 'I said in my heart with regard to the "
                        "children of man that God is testing them that they may see that they themselves "
                        "are but beasts. For what happens to the children of man and what happens to the "
                        "beasts is the same; as one dies, so dies the other... All go to one place. All "
                        "are from the dust, and to dust all return' (3:18-20). From the 'under the sun' "
                        "perspective, there is no observable difference between human and animal death. "
                        "'Who knows whether the spirit of man goes upward and the spirit of the beast "
                        "goes down into the earth?' (3:21). Chapter 4 examines oppression (4:1-3 -- the "
                        "dead are happier than the living), rivalry (4:4), and loneliness versus "
                        "companionship: 'Two are better than one... a threefold cord is not quickly "
                        "broken' (4:9-12)."
            }
        ]
    },

    {
        "id": "eccl-5-6",
        "ref": "Ecclesiastes 5-6",
        "chapter_num": 5,
        "title": "Worship, Wealth, and the Gift of Enjoyment",
        "era": "66",
        "type": "chapter",
        "themes": ["PROV", "HOLY"],

        "synopsis": "Chapter 5 opens with a rare imperative section on proper worship: 'Guard your steps "
                    "when you go to the house of God. To draw near to listen is better than to offer the "
                    "sacrifice of fools' (5:1). Vows must be fulfilled (5:4-5), and words before God "
                    "should be few (5:2). The chapter then examines wealth: 'He who loves money will not "
                    "be satisfied with money, nor he who loves wealth with his income; this also is hebel' "
                    "(5:10). The laborer's sleep is sweet regardless of how much he eats, but the rich "
                    "man's abundance will not let him sleep (5:12). Wealth can be lost in a bad venture, "
                    "and the owner departs 'naked as he came' (5:13-16). The third enjoyment passage "
                    "follows: 'Behold, what I have seen to be good and fitting is to eat and drink and "
                    "find enjoyment in all the toil with which one toils under the sun' (5:18). Chapter "
                    "6 presents the dark side: a man to whom God gives wealth but not the ability to "
                    "enjoy it (6:1-2) -- 'a grievous evil.'",

        "key_verse": {
            "ref": "Ecclesiastes 5:1-2",
            "text": "Guard your steps when you go to the house of God. To draw near to listen is better than to offer the sacrifice of fools, for they do not know that they are doing evil. Be not rash with your mouth, nor let your heart be hasty to utter a word before God, for God is in heaven and you are on earth. Therefore let your words be few.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "bet ha-elohim (house of God -- the Temple, approached with reverent caution)",
            "neder (vow -- a binding commitment before God that must not be made rashly)",
            "amal (toil/labor -- the daily work that can be either burden or gift depending on perspective)",
            "chelqo (his portion -- the share God assigns to each person, to be received with gratitude)"
        ],

        "ane_backdrop": "The warning about rash speech before God (5:1-7) echoes Egyptian and Mesopotamian "
                        "temple instruction. The Egyptian 'Instruction of Ani' warns: 'Be not of many "
                        "words in the god's house; the god hates much speaking.' The Babylonian temple "
                        "entrance instructions similarly counsel reverence and brevity. Qoheleth's reason "
                        "is distinctively theological: 'God is in heaven and you are on earth' (5:2) -- "
                        "the infinite qualitative difference between Creator and creature demands humility.",

        "second_temple": [
            {
                "source": "Sirach 7:14",
                "summary": "'Do not babble in the assembly of the elders, and do not repeat yourself "
                           "when you pray.'",
                "relevance": "Ben Sira develops the Qoheleth-like counsel of brevity in prayer, "
                             "applying it to both worship and communal assembly."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 6:7-8", "note": "'Do not heap up empty phrases as the Gentiles do' -- Jesus echoes 5:2 on brevity before God", "type": "nt"},
            {"ref": "1 Timothy 6:6-10", "note": "'The love of money is a root of all kinds of evils' -- developing Qoheleth's wealth critique", "type": "nt"},
            {"ref": "Job 1:21", "note": "'Naked I came from my mother's womb, and naked shall I return' -- the same observation as 5:15", "type": "ot"},
            {"ref": "Luke 12:15-21", "note": "The rich fool: 'a man's life does not consist in the abundance of his possessions' -- the parable of 5:10-17", "type": "nt"}
        ],

        "divine_council_note": "Ecclesiastes 5:2 contains a critical theological assertion: 'God is in "
                               "heaven and you are on earth. Therefore let your words be few.' This is "
                               "the 'under the sun' / 'above the sun' distinction made explicit. God's "
                               "realm is heaven -- the throne room of the divine council. The human realm "
                               "is earth. The gap between them demands reverent caution. This is the same "
                               "theological instinct that produced the theophany in Job: YHWH speaks from "
                               "above, and humans respond in humility and silence.",

        "sections": [
            {
                "heading": "Reverence in Worship (5:1-7)",
                "body": "Qoheleth's worship counsel is rare in the wisdom literature for its directness: "
                        "'Guard your steps when you go to the house of God' (5:1). The 'sacrifice of "
                        "fools' is worship offered without understanding or reverence. Speech before God "
                        "should be sparse: 'Be not rash with your mouth, nor let your heart be hasty to "
                        "utter a word before God, for God is in heaven and you are on earth' (5:2). Vows "
                        "are serious: 'When you vow a vow to God, do not delay paying it, for he has no "
                        "pleasure in fools. Pay what you vow. It is better that you should not vow than "
                        "that you should vow and not pay' (5:4-5). The section concludes: 'God is the one "
                        "you must fear' (5:7)."
            },
            {
                "heading": "The Futility of Wealth (5:8-6:12)",
                "body": "Qoheleth observes systemic injustice: 'If you see in a province the oppression "
                        "of the poor... do not be amazed at the matter, for the high official is watched "
                        "by a higher, and there are yet higher ones over them' (5:8). The bureaucratic "
                        "chain of exploitation is noted without surprise. Wealth itself is empty: 'He "
                        "who loves money will not be satisfied with money' (5:10). The rich man's curse: "
                        "'Sweet is the sleep of a laborer... but the full stomach of the rich will not "
                        "let him sleep' (5:12). The enjoyment passage follows: 'Behold, what I have seen "
                        "to be good and fitting is to eat and drink and find enjoyment' (5:18). This is "
                        "a person's 'portion' (chelqo) -- not a solution to the hebel but God's gift "
                        "within it. Chapter 6 presents the horror of having wealth without the ability "
                        "to enjoy it (6:1-6) -- a man with everything who cannot partake. 'A stillborn "
                        "child is better off than he' (6:3)."
            }
        ]
    }
]
