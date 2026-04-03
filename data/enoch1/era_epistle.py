"""
era_epistle.py — Epistle of Enoch (1 Enoch 91-108)

The Epistle of Enoch is the final major section of the Enochic corpus. It
contains Enoch's farewell exhortation to his children, the Apocalypse of
Weeks (a periodized history of the world in ten "weeks"), woe-oracles
against the wealthy and oppressive sinners, and concluding exhortations
about the fate of the righteous and wicked after death.

The most important sub-unit is the Apocalypse of Weeks (91:12-17 + 93:1-10),
which divides all of history into ten "weeks" (epochs). The text's order
is disrupted in the Ethiopic tradition: the eighth through tenth weeks
(91:12-17) appear AFTER the first through seventh (93:1-10), but the
Aramaic fragments from Qumran (4Q212) preserve the correct order with
all ten weeks in sequence.

Aramaic fragments: 4Q212 (4QEn-g) preserves portions of the Apocalypse
of Weeks and the Epistle. 4Q204 (4QEn-c) may also contain Epistle
material. The Epistle is generally dated to the 2nd century BC, though
the Apocalypse of Weeks may be slightly earlier.

Chapters 106-108 (the Birth of Noah appendix) are considered a later
addition by most scholars, possibly from a separate "Book of Noah" that
circulated independently.

Translation references: R.H. Charles (1912), G.W.E. Nickelsburg &
J.C. VanderKam (Hermeneia, 2012), L. Stuckenbruck (2007).
"""

CHAPTERS = [
    # =========================================================================
    # ENOCH'S EXHORTATION (1 Enoch 91-93)
    # =========================================================================
    {
        "id": "1en-91-93",
        "ref": "1 Enoch 91-93",
        "chapter_num": 91,
        "title": "The Apocalypse of Weeks — Ten Epochs of History",
        "era": "epistle",
        "type": "chapter",

        "synopsis": "The Apocalypse of Weeks is a compressed history of the world "
                    "divided into ten symbolic 'weeks' (epochs). The first seven "
                    "weeks cover history from Enoch's birth through the Second Temple "
                    "period; the final three project into the eschatological future. "
                    "The Aramaic fragments from Qumran (4Q212) preserve the correct "
                    "sequence: 93:1-10 (weeks 1-7) followed by 91:12-17 (weeks 8-10). "
                    "In the Ethiopic tradition, the order is inverted — 91:12-17 "
                    "precedes 93:1-10 — due to a displacement in the manuscript "
                    "tradition. This periodized view of history is foundational for "
                    "apocalyptic temporal schemes from Daniel to Revelation.",

        "key_verse": {
            "ref": "1 Enoch 93:1-3",
            "text": "And Enoch began to recount from the books and said: 'I was "
                    "born the seventh in the first week, while judgement and "
                    "righteousness still endured. And after me there shall arise in "
                    "the second week great wickedness, and deceit shall have sprung "
                    "up; and in it there shall be the first end. And in it a man "
                    "shall be saved; and after it is ended unrighteousness shall "
                    "grow up, and a law shall be made for the sinners.'",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "mishpat",
            "tsedaqah",
            "olam",
            "tsaddiq",
            "berit",
            "mashiach",
        ],

        "ane_backdrop": "The periodization of history into numbered epochs is a "
                        "widespread ANE and Second Temple convention. The Mesopotamian "
                        "tradition of dividing history into pre-flood and post-flood "
                        "eras (in the Sumerian King List) represents an early form. "
                        "The Zoroastrian concept of world-epochs (the four ages of "
                        "3,000 years each) may have influenced Jewish apocalyptic "
                        "periodization during the Persian period. The Hesiodic "
                        "tradition of declining world-ages (gold, silver, bronze, "
                        "iron) provides a Greek parallel. The 'week' as a unit of "
                        "historical periodization draws on the sabbatical principle: "
                        "seven days, seven years (the sabbatical year), seven sevens "
                        "(the jubilee). Daniel 9's 'seventy weeks of years' represents "
                        "the canonical biblical version of this periodization technique.",

        "second_temple": [
            {
                "source": "Daniel 9:24-27",
                "summary": "Seventy weeks of years are decreed for Israel: seven weeks "
                           "for the rebuilding of Jerusalem, sixty-two weeks until an "
                           "anointed one, and a final week of tribulation.",
                "relevance": "Daniel 9's 'weeks of years' scheme and the Apocalypse of "
                             "Weeks share the same periodization technique. Both divide "
                             "history into numbered units of 'weeks' with different "
                             "character. Both reach their climax in eschatological "
                             "judgment. The question of which text influenced the other "
                             "is debated; they may draw on a common apocalyptic tradition.",
                "canon": False
            },
            {
                "source": "Jubilees 1:4-29",
                "summary": "God reveals to Moses on Sinai the entire sweep of history "
                           "divided into jubilee periods (49-year cycles), from "
                           "creation to the eschatological restoration.",
                "relevance": "Jubilees' periodization by jubilees and the Apocalypse of "
                             "Weeks' periodization by weeks represent two versions of "
                             "the same tradition: history has a divinely predetermined "
                             "structure, and the end can be calculated from the "
                             "pattern.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 9:24-27", "note": "The seventy weeks of years — the canonical parallel to the Apocalypse of Weeks' ten-epoch periodization of history", "type": "ot"},
            {"ref": "Daniel 2:31-45", "note": "The four-metal statue representing successive world empires — Daniel's periodized history that parallels the Apocalypse of Weeks' epoch scheme", "type": "ot"},
            {"ref": "Genesis 5:21-24", "note": "Enoch, the seventh from Adam — the Apocalypse of Weeks begins with 'I was born the seventh in the first week,' connecting Enoch's genealogical position to cosmic chronology", "type": "ot"},
            {"ref": "Matthew 24:3-14", "note": "Jesus' periodized overview of the end times (wars, famines, persecutions, the abomination, the gospel preached to all nations, then the end) follows the same structure as apocalyptic epoch schemes", "type": "nt"},
            {"ref": "Revelation 2-3", "note": "Seven churches representing seven ages or conditions — the number seven structuring a historical/ecclesial progression, as in the Apocalypse of Weeks", "type": "nt"},
            {"ref": "4Q212 (4QEn-g)", "type": "dss", "note": "Aramaic fragments preserving the Apocalypse of Weeks in its correct order (all ten weeks in sequence), correcting the disorder in the Ethiopic manuscript tradition. Paleographic date: 1st century BC."},
            {"ref": "4Q180-181 (Ages of Creation)", "type": "dss", "note": "Qumran periodization text that divides history into predetermined epochs, using a scheme related to the Apocalypse of Weeks' framework"},
            {"ref": "Hebrews 11:1-40", "note": "The 'hall of faith' surveys salvation history through exemplary figures from Abel to the prophets — a different literary form (catalog vs. periodization) covering similar ground", "type": "nt"}
        ],

        "divine_council_note": "The Apocalypse of Weeks presupposes that history's "
                               "structure is a divine council decree. The ten epochs "
                               "are not arbitrary divisions but foreordained periods "
                               "inscribed on the heavenly tablets (cf. 1 Enoch 81). "
                               "Enoch has read the tablets and can therefore 'recount "
                               "from the books' the entire sweep of history. The "
                               "transition points between weeks — the Flood (week 2), "
                               "Abraham's election (week 3), Sinai (week 4), the Temple "
                               "(week 5), the exile (week 6), the rise of the elect "
                               "(week 7) — are all council-directed events. The "
                               "eschatological weeks (8-10) describe the council's "
                               "final actions: judgment of the Watchers, renewal of "
                               "creation, and the eternal age.",

        "sections": [
            {
                "heading": "The First Seven Weeks — From Enoch to the Second Temple (93:1-10)",
                "body": "The Apocalypse of Weeks begins with Enoch's self-placement: "
                        "'I was born the seventh in the first week, while judgement "
                        "and righteousness still endured' (93:1). The first week is "
                        "the primordial era from creation to Enoch — characterized by "
                        "righteousness. The second week brings 'great wickedness' and "
                        "the Flood: 'a man shall be saved' (Noah) and 'after it is "
                        "ended unrighteousness shall grow up' (93:4). The third week "
                        "sees the election of Abraham: 'a man shall be elected as the "
                        "plant of righteous judgement, and his posterity shall become "
                        "the plant of righteousness for evermore' (93:5). The fourth "
                        "week: 'visions of the holy and righteous' and 'a law for all "
                        "generations' — the Sinai revelation (93:6). The fifth week "
                        "brings the Temple: 'a house of glory and dominion shall be "
                        "built for ever' (93:7). The sixth week: 'all who live in it "
                        "shall be blinded, and the hearts of all of them shall godlessly "
                        "forsake wisdom' — the period of apostasy before the exile. "
                        "'A man shall ascend' (Elijah, 93:8). The Temple is burned. The "
                        "seventh week is the corrupt period of the Second Temple: 'an "
                        "apostate generation shall arise, and many shall be its deeds, "
                        "and all its deeds shall be apostate. And at its close shall be "
                        "elected the elect righteous of the eternal plant of "
                        "righteousness' (93:9-10). This 'elect righteous' likely "
                        "refers to the Enochic movement itself — the community that "
                        "the author belongs to."
            },
            {
                "heading": "The Eighth Through Tenth Weeks — Eschatological Future (91:12-17)",
                "body": "The final three weeks project into the author's eschatological "
                        "future. The eighth week is the 'week of righteousness': 'a "
                        "sword shall be given to it that a righteous judgement may be "
                        "executed on the oppressors, and sinners shall be delivered "
                        "into the hands of the righteous' (91:12). The righteous "
                        "acquire houses (security), and 'the house of the Great King "
                        "shall be built in glory for evermore' (91:13) — the "
                        "eschatological Temple. The ninth week: 'the righteous "
                        "judgement shall be revealed to the whole world, and all the "
                        "works of the godless shall vanish from all the earth, and the "
                        "world shall be written down for destruction' (91:14). "
                        "Universal judgment extends to the entire world, not just "
                        "Israel. The tenth week: 'the eternal judgement shall be "
                        "executed on the Watchers... the first heaven shall depart and "
                        "pass away, and a new heaven shall appear' (91:15-16). The "
                        "judgment of the Watchers — deferred since chapters 10-16 — "
                        "finally reaches its consummation. The old creation is replaced "
                        "by a new one: 'all the powers of the heavens shall give "
                        "sevenfold light' (91:16). After the tenth week, 'there shall "
                        "be many weeks without number for ever, and all shall be in "
                        "goodness and righteousness' (91:17). Time itself is "
                        "transformed: the numbered epochs give way to an innumerable "
                        "eternity."
            },
            {
                "heading": "Enoch's Charge to His Children (91:1-11)",
                "body": "The Apocalypse of Weeks is embedded within a broader "
                        "exhortation. Chapter 91 opens with Enoch's summons: 'And "
                        "now, my son Methuselah, call to me all thy brothers and "
                        "gather together to me all the sons of thy mother' (91:1). "
                        "Enoch addresses his family as a patriarch imparting final "
                        "wisdom — a literary form that echoes Jacob's blessing "
                        "(Genesis 49), Moses' farewell (Deuteronomy 33), and will "
                        "recur in the Testaments of the Twelve Patriarchs. His "
                        "message is dual: encouragement for the righteous ('Walk in "
                        "the paths of righteousness, and walk not in the paths of "
                        "wickedness,' 91:4) and warning about the coming judgment. "
                        "'Woe to those who build unrighteousness and oppression and "
                        "lay deceit as a foundation; for they shall be suddenly "
                        "overthrown' (91:7). The exhortation establishes the ethical "
                        "framework within which the Apocalypse of Weeks should be "
                        "read: the periodization of history is not mere intellectual "
                        "curiosity but a call to faithfulness. Knowing that God has "
                        "predetermined the epochs — including the epoch of judgment — "
                        "should motivate the hearer to 'walk in the paths of "
                        "righteousness.'"
            }
        ]
    },

    # =========================================================================
    # THE APOCALYPSE OF WEEKS — DETAILED ANALYSIS (1 Enoch 93:1-10 + 91:12-17)
    # =========================================================================
    {
        "id": "1en-apoc-weeks-detail",
        "ref": "1 Enoch 93:1-10 + 91:12-17",
        "chapter_num": 93,
        "title": "The Ten Weeks Decoded — A Map of All History",
        "era": "epistle",
        "type": "chapter",

        "synopsis": "The Apocalypse of Weeks deserves detailed treatment beyond the "
                    "overview in the previous chapter. This passage divides all of "
                    "history into ten \'weeks\' (epochs) of unspecified duration, each "
                    "characterized by a defining event or condition. The first seven "
                    "weeks survey past history from Enoch to the author\'s present; the "
                    "final three project into the eschatological future. The Aramaic "
                    "fragments from Qumran (4Q212) preserve the correct order of all "
                    "ten weeks in sequence, correcting the displacement in the Ethiopic "
                    "manuscripts. Each week contains a theological assessment of its "
                    "era, creating a comprehensive theology of history: creation is "
                    "good, sin corrupts progressively, judgment intervenes repeatedly, "
                    "and the elect are preserved through every catastrophe.",

        "key_verse": {
            "ref": "1 Enoch 93:10 + 91:12",
            "text": "And at the close of the seventh week shall be elected the elect "
                    "righteous of the eternal plant of righteousness, to receive "
                    "sevenfold instruction concerning all His creation... In the "
                    "eighth week a sword shall be given to the righteous that a "
                    "righteous judgment may be executed on the oppressors.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "mishpat",
            "tsedaqah",
            "olam",
            "qodesh",
            "berit",
            "mabbul",
        ],

        "ane_backdrop": "Historical periodization schemes are attested across the ANE. "
                        "The Hesiodic tradition (Works and Days, c. 700 BC) divides "
                        "human history into five declining ages: gold, silver, bronze, "
                        "heroic, and iron. The Zoroastrian tradition divides cosmic "
                        "history into four periods of 3,000 years each. The Babylonian "
                        "Dynasties Chronicle periodizes Mesopotamian history by ruling "
                        "houses. The distinctive feature of the Apocalypse of Weeks is "
                        "its combination of periodization with predestination: the "
                        "epochs are not merely described but decreed — their content "
                        "was inscribed on the heavenly tablets before creation. History "
                        "unfolds according to plan, not by chance.",

        "second_temple": [
            {
                "source": "11Q13 (11QMelchizedek)",
                "summary": "A Qumran text that calculates the eschatological Jubilee "
                           "using a ten-Jubilee scheme, at the end of which Melchizedek "
                           "will execute judgment on Belial and the spirits of his lot.",
                "relevance": "11QMelchizedek\'s ten-Jubilee scheme may be directly "
                             "influenced by the Apocalypse of Weeks\' ten-week scheme. "
                             "Both divide history into ten major periods culminating in "
                             "eschatological judgment, and both place the current community "
                             "at the critical juncture before the final period.",
                "canon": False
            },
            {
                "source": "2 Baruch 53-74 (Apocalypse of the Cloud Vision)",
                "summary": "A post-70 AD Jewish apocalypse that divides history into "
                           "alternating periods of \'bright waters\' (righteous eras) and "
                           "\'dark waters\' (wicked eras), from Adam to the Messiah.",
                "relevance": "2 Baruch independently develops a periodized history scheme "
                             "that echoes the Apocalypse of Weeks\' alternation between "
                             "righteousness and apostasy, showing the persistence of this "
                             "apocalyptic technique into the late 1st century AD.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 9:24-27", "note": "Seventy weeks of years decreed — the canonical parallel to the Apocalypse of Weeks, both using \'weeks\' as units of historical periodization culminating in eschatological resolution", "type": "ot"},
            {"ref": "Daniel 2:31-45", "note": "The four-metal statue representing successive empires — a complementary periodization scheme that maps history through declining metal quality rather than numbered weeks", "type": "ot"},
            {"ref": "Leviticus 25:8-12", "note": "The Jubilee cycle (7 x 7 + 1 years) — the sabbatical-Jubilee mathematics underlying both the Apocalypse of Weeks and Daniel\'s seventy weeks", "type": "ot"},
            {"ref": "4Q212 (4QEn-g)", "type": "dss", "note": "Aramaic fragments preserving the Apocalypse of Weeks in correct order (all ten weeks in sequence), correcting the Ethiopic manuscript displacement"},
            {"ref": "4Q180-181 (Ages of Creation)", "type": "dss", "note": "Qumran text periodizing history into predetermined epochs with explicit reference to the Watcher rebellion — a related periodization tradition"},
            {"ref": "11Q13 (11QMelchizedek)", "type": "dss", "note": "Qumran eschatological text using a ten-Jubilee calculation possibly derived from the Apocalypse of Weeks\' ten-period scheme"},
            {"ref": "Galatians 4:4", "note": "\'When the fullness of time had come, God sent his Son\' — the NT conviction that the Messiah arrives at the divinely appointed moment in the predetermined schedule", "type": "nt"},
            {"ref": "Ephesians 1:10", "note": "A plan for the fullness of time, to unite all things in Christ — Pauline eschatology shaped by the apocalyptic conviction that history has a predetermined structure and climax", "type": "nt"}
        ],

        "divine_council_note": "The Apocalypse of Weeks is a summary of the heavenly "
                               "tablets — the council\'s master plan for history. Enoch "
                               "can \'recount from the books\' (93:1) because he has read "
                               "the tablets that record all future events. Each week\'s "
                               "transition represents a council decision point: the Flood "
                               "in week 2 (a council judgment), Abraham\'s election in week "
                               "3 (a council appointment), Sinai in week 4 (council "
                               "legislation), the Temple in week 5 (council dwelling), and "
                               "so on. The final three weeks describe the council\'s "
                               "culminating actions: arming the righteous (week 8), "
                               "worldwide judgment (week 9), and the judgment of the "
                               "Watchers and cosmic renewal (week 10). History\'s meaning "
                               "is the council\'s plan being executed.",

        "sections": [
            {
                "heading": "Weeks 1-4: From Creation to Sinai",
                "body": "Week 1 is the primordial era from creation to Enoch, "
                        "characterized by \'judgment and righteousness\' (93:1). The world "
                        "in its original state is good. Enoch identifies himself as \'born "
                        "the seventh in the first week\' — linking his genealogical "
                        "position (seventh from Adam, Gen 5) to cosmic chronology. Week "
                        "2 brings the Flood: \'great wickedness\' arises, and \'a man shall "
                        "be saved\' (Noah, 93:4). The Flood is both judgment and "
                        "preservation — the pattern for all subsequent divine intervention. "
                        "Week 3 sees Abraham\'s election: \'a man shall be elected as the "
                        "plant of righteous judgment, and his posterity shall become the "
                        "plant of righteousness for evermore\' (93:5). The \'plant\' "
                        "metaphor is significant — it recurs in the Community Rule (1QS "
                        "8:5; 11:8) as the Qumran community\'s self-designation, suggesting "
                        "they understood themselves as the eschatological flowering of "
                        "Abraham\'s seed. Week 4 is Sinai: \'a law for all generations\' "
                        "and \'visions of the holy and righteous\' (93:6). The Law and "
                        "prophetic vision are given together, and an \'enclosure\' "
                        "(the Tabernacle/Promised Land) is established."
            },
            {
                "heading": "Weeks 5-7: Temple, Exile, and the Elect",
                "body": "Week 5 is the monarchic period: \'a house of glory and dominion "
                        "shall be built for ever\' (93:7) — Solomon\'s Temple. The word "
                        "\'for ever\' is ironic, since the Temple will be destroyed in the "
                        "next week. Week 6 is the period of apostasy and exile: \'all who "
                        "live in it shall be blinded, and the hearts of all of them shall "
                        "godlessly forsake wisdom\' (93:8). \'A man shall ascend\' (Elijah), "
                        "and the Temple is burned. The \'blindness\' of week 6 echoes the "
                        "Animal Apocalypse\'s \'blinded sheep\' (89:28) — Israel cannot see "
                        "because they have abandoned wisdom (Torah). Week 7 is the "
                        "author\'s own era — the Second Temple period: \'an apostate "
                        "generation shall arise, and many shall be its deeds, and all its "
                        "deeds shall be apostate\' (93:9). The Second Temple establishment "
                        "is comprehensively condemned. But at the close of week 7, \'the "
                        "elect righteous of the eternal plant of righteousness\' are chosen "
                        "(93:10) — the Enochic movement itself, the community that has "
                        "preserved true wisdom while the broader nation apostasized. This "
                        "self-placement at the hinge of history is a powerful rhetorical "
                        "move: the reader is living at the transition from corruption to "
                        "vindication."
            },
            {
                "heading": "Weeks 8-10: Eschatological Future",
                "body": "The final three weeks project into the future with escalating "
                        "cosmic transformation. Week 8 is the \'week of righteousness\': "
                        "a sword is given to the righteous for judgment on oppressors, "
                        "and the eschatological Temple (\'the house of the Great King\') "
                        "is built \'in glory for evermore\' (91:12-13). Week 9 extends "
                        "judgment universally: \'the righteous judgment shall be revealed "
                        "to the whole world\' and \'the world shall be written down for "
                        "destruction\' (91:14). Judgment is no longer limited to Israel "
                        "but encompasses all nations — a universalism that anticipates "
                        "the NT\'s cosmic eschatology. Week 10 is the consummation: \'the "
                        "eternal judgment shall be executed on the Watchers\' (91:15). The "
                        "Watchers who were bound in 1 Enoch 10 are finally judged "
                        "permanently. \'The first heaven shall depart and pass away, and "
                        "a new heaven shall appear\' (91:16). The old creation is replaced. "
                        "\'All the powers of the heavens shall give sevenfold light\' — "
                        "the renewed cosmos radiates intensified divine glory. After the "
                        "tenth week: \'there shall be many weeks without number for ever, "
                        "and all shall be in goodness and righteousness\' (91:17). Counted "
                        "time (history) gives way to uncounted eternity."
            }
        ]
    },

    # =========================================================================
    # THE TWO WAYS — RIGHTEOUS AND SINNERS (1 Enoch 91, 94, 101-105)
    # =========================================================================
    {
        "id": "1en-two-ways",
        "ref": "1 Enoch 91, 94, 101-105",
        "chapter_num": 101,
        "title": "The Two Ways — Righteous and Sinners in Enochic Theology",
        "era": "epistle",
        "type": "chapter",

        "synopsis": "Woven throughout the Epistle of Enoch is a sustained \'two ways\' "
                    "theology that sharply divides humanity into two groups: the righteous "
                    "and the sinners. This division is not merely moral but cosmic — it "
                    "reflects the predetermined categories inscribed on the heavenly "
                    "tablets. The righteous walk in light, will inherit eternal joy, and "
                    "will become companions of the heavenly host. The sinners walk in "
                    "darkness, will face eternal judgment, and their names will be erased "
                    "from the divine record. This two-ways framework connects the Epistle "
                    "to the Deuteronomic tradition (Deut 30:15-20), the Wisdom tradition "
                    "(Psalm 1, Proverbs 4:18-19), and the Qumran community\'s dualistic "
                    "theology (1QS 3:13 - 4:26). It also provides crucial background for "
                    "Jesus\' two-ways teaching (Matthew 7:13-14) and the Didache\'s "
                    "\'Two Ways\' catechesis.",

        "key_verse": {
            "ref": "1 Enoch 91:3-4",
            "text": "Walk not in the paths of wickedness, nor in the paths of death, "
                    "and draw not nigh to them, lest ye be destroyed. But seek and "
                    "choose for yourselves righteousness and an elect life.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "tsaddiq",
            "tsedaqah",
            "mishpat",
            "sheol",
            "nefesh",
            "olam",
        ],

        "ane_backdrop": "The \'two ways\' or \'two paths\' motif is one of the oldest "
                        "moral frameworks in world literature. Egyptian wisdom texts "
                        "(the Instruction of Amenemope, c. 1300 BC) distinguish the \'hot "
                        "man\' (the impulsive sinner) from the \'silent man\' (the wise "
                        "righteous person). Mesopotamian wisdom literature (the Counsels "
                        "of Wisdom, the Shurpu incantation series) similarly distinguishes "
                        "between paths of righteousness and wickedness. The Zoroastrian "
                        "tradition\'s dualism between Ahura Mazda and Angra Mainyu may "
                        "have influenced the sharpened form of this dualism in Second "
                        "Temple Judaism. The Epistle\'s two-ways theology reflects the "
                        "intensification of this ancient framework under the pressure of "
                        "persecution: when faithfulness costs everything, the line between "
                        "righteous and wicked becomes absolute.",

        "second_temple": [
            {
                "source": "1QS 3:13 - 4:26 (Community Rule, The Two Spirits Treatise)",
                "summary": "God created two spirits — the Prince of Lights and the Angel "
                           "of Darkness — who govern two lots of humanity. The sons of "
                           "righteousness walk in light; the sons of perversity walk in "
                           "darkness. At the appointed end, God will destroy falsehood.",
                "relevance": "The Qumran Two Spirits Treatise develops the Epistle\'s "
                             "two-ways theology into a full cosmic dualism with angelic "
                             "leaders on each side. Both texts share the conviction that "
                             "the division between righteous and wicked is predetermined "
                             "and will be resolved at the eschatological judgment.",
                "canon": False
            },
            {
                "source": "Didache 1-6 (The Two Ways)",
                "summary": "The earliest Christian catechetical text opens with: \'There "
                           "are two ways, one of life and one of death, and there is a "
                           "great difference between the two ways.\' It then elaborates "
                           "the moral content of each path.",
                "relevance": "The Didache\'s \'Two Ways\' catechesis draws on the same "
                             "tradition as the Epistle of Enoch and Deuteronomy 30. The "
                             "early church adopted this framework directly from Second "
                             "Temple Judaism for its own moral instruction.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 30:15-20", "note": "I set before you today life and death, blessing and curse. Choose life — the foundational OT \'two ways\' text that the Epistle of Enoch develops", "type": "ot"},
            {"ref": "Psalm 1:1-6", "note": "The righteous man walks not in the counsel of the wicked... the way of the wicked will perish — the Wisdom tradition\'s definitive \'two ways\' formulation", "type": "ot"},
            {"ref": "Proverbs 4:18-19", "note": "The path of the righteous is like the light of dawn; the way of the wicked is like deep darkness — the light/darkness imagery that the Epistle shares", "type": "ot"},
            {"ref": "Matthew 7:13-14", "note": "Enter by the narrow gate... the gate is wide and the way is easy that leads to destruction — Jesus\' two-ways teaching drawing on the same tradition as the Epistle", "type": "nt"},
            {"ref": "John 3:19-21", "note": "Light has come into the world, and people loved the darkness rather than the light — Johannine dualism shaped by the two-ways tradition", "type": "nt"},
            {"ref": "Romans 6:16-23", "note": "Slaves of sin leading to death, or slaves of righteousness leading to eternal life — Paul\'s two-ways formulation in soteriological terms", "type": "nt"},
            {"ref": "1 John 1:5-7", "note": "God is light and in him is no darkness at all; if we walk in the light... — Johannine light/darkness dualism inheriting the Enochic two-ways framework", "type": "nt"}
        ],

        "divine_council_note": "The Epistle\'s two-ways theology is grounded in the "
                               "divine council\'s predetermined categories. The names of "
                               "the righteous are written before the Great One (104:1); "
                               "the deeds of the sinners are recorded for judgment (98:7-8). "
                               "The division is not a human assessment but a heavenly one. "
                               "The \'elect life\' that Enoch urges his children to choose "
                               "(91:4) is the life inscribed on the heavenly tablets as the "
                               "destiny of the righteous. This creates a tension between "
                               "predestination and exhortation that recurs in Paul (cf. "
                               "Romans 8:28-30 with Philippians 2:12): the elect are "
                               "predetermined, yet they must \'choose\' the path of "
                               "righteousness. The council has written the outcome, but "
                               "the individual must walk in it.",

        "sections": [
            {
                "heading": "Enoch\'s Charge — Choose Righteousness (91:1-11)",
                "body": "The Epistle opens with Enoch summoning his children for a final "
                        "exhortation. \'Walk not in the paths of wickedness, nor in the "
                        "paths of death, and draw not nigh to them, lest ye be destroyed. "
                        "But seek and choose for yourselves righteousness and an elect "
                        "life\' (91:3-4). The vocabulary is Deuteronomic: \'choose\' echoes "
                        "Moses\' command in Deuteronomy 30:19 (\'Choose life\'). The \'elect "
                        "life\' (Ge\'ez: heyaw xeruy) is a life characterized by election — "
                        "chosen by God and chosen by the individual. Enoch warns that "
                        "wickedness will come: \'Woe to those who build unrighteousness "
                        "and oppression and lay deceit as a foundation; for they shall be "
                        "suddenly overthrown\' (91:7). But his primary tone is encouraging: "
                        "\'Fear ye not, ye righteous\' (91:3, anticipating the same "
                        "assurance in 96:3, 104:6). The righteous should not be "
                        "intimidated by the sinners\' apparent prosperity. The heavenly "
                        "tablets record both their faithfulness and the sinners\' doom."
            },
            {
                "heading": "The Tablets of Heaven and Predestined Paths (103:1 - 104:8)",
                "body": "The tablets of heaven function as the ultimate guarantor of the "
                        "two-ways distinction. \'I have read the heavenly tablets, and "
                        "have seen the holy ones, and have found written therein and "
                        "inscribed regarding them\' (103:2). The righteous\' destiny is "
                        "not uncertain — it is recorded in the divine archive. \'Your "
                        "names are written before the glory of the Great One\' (104:1). "
                        "This is not abstract predestination but personal inscription: "
                        "each name is individually recorded. Conversely, the sinners\' "
                        "deeds are also recorded: \'All your sin is written down every "
                        "day\' (98:7). The recording angels maintain both records "
                        "simultaneously. The heavenly tablets thus contain both a book "
                        "of life (the names of the righteous) and a book of deeds (the "
                        "sins of the wicked), corresponding to the \'books\' opened at "
                        "judgment in Daniel 7:10 and Revelation 20:12. The practical "
                        "implication for the persecuted righteous is profound: nothing "
                        "is forgotten. Every act of faithfulness under persecution, "
                        "every refusal to compromise, is inscribed in heaven."
            },
            {
                "heading": "The Social Dimension — Justice as Two-Ways Marker",
                "body": "The Epistle\'s two-ways theology has a distinctive social "
                        "dimension that sets it apart from purely individual moral "
                        "teaching. The \'sinners\' are repeatedly identified by their "
                        "social behavior: they build houses through oppression (94:7), "
                        "trust in riches (96:4), write lying records (98:15), and "
                        "exploit the poor (97:8-10). The \'righteous\' are identified by "
                        "their suffering: they are persecuted, impoverished, and mocked "
                        "(103:9-15). The two ways are thus not just moral paths but "
                        "social positions: the oppressor class and the oppressed class. "
                        "This social reading of the two-ways tradition profoundly "
                        "influenced the NT. Jesus\' Beatitudes (Matt 5:3-12) identify "
                        "the righteous with the poor, mourning, and persecuted. James "
                        "5:1-6 condemns the rich who have exploited workers. Luke 6:20-26 "
                        "pairs blessings for the poor with woes against the rich. The "
                        "Epistle of Enoch is a critical link in the chain from "
                        "Deuteronomic two-ways theology to the NT\'s social justice "
                        "ethic."
            }
        ]
    },

    # =========================================================================
    # COSMIC WITNESS AND SOCIAL JUSTICE (1 Enoch 97-100)
    # =========================================================================
    {
        "id": "1en-97-100",
        "ref": "1 Enoch 97-100",
        "chapter_num": 97,
        "title": "Cosmic Witnesses and Social Justice — Creation Testifies Against the Sinners",
        "era": "epistle",
        "type": "chapter",

        "synopsis": "Chapters 97-100 intensify the Epistle\'s woe-oracles with a "
                    "remarkable innovation: creation itself will serve as a witness "
                    "against the sinners at the final judgment. The earth, the heavens, "
                    "the sun, moon, and stars will testify to the injustice they have "
                    "observed. This cosmic witness tradition draws on Deuteronomy 30:19 "
                    "(heaven and earth as witnesses) and Isaiah 1:2 (\'Hear, O heavens, "
                    "and give ear, O earth\') but develops it into a comprehensive "
                    "forensic theology: every element of creation records the sinners\' "
                    "deeds and will present evidence at the eschatological trial. The "
                    "section also contains the Epistle\'s sharpest social justice "
                    "rhetoric, condemning the exploitation of workers, false weights "
                    "and measures, and the corruption of scribal traditions.",

        "key_verse": {
            "ref": "1 Enoch 100:10-11",
            "text": "And now, know ye that from the angels He will inquire as to your "
                    "deeds in heaven, from the sun and from the moon and from the "
                    "stars in reference to your sins, because upon the earth ye "
                    "execute judgement on the righteous.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "shamayim",
            "mishpat",
            "tsedaqah",
            "berit",
            "malak_yhwh",
        ],

        "ane_backdrop": "The concept of creation as a moral witness has roots in "
                        "Mesopotamian and Egyptian traditions. In Egyptian judgment "
                        "scenes, the heart of the deceased is weighed against Ma\'at "
                        "(truth/cosmic order) — the created order itself serves as the "
                        "standard of judgment. The Hittite treaties invoke mountains, "
                        "rivers, heaven, and earth as witnesses to covenant obligations, "
                        "a practice reflected in the Deuteronomic tradition. The Epistle "
                        "of Enoch combines these traditions into a distinctly apocalyptic "
                        "framework: creation does not merely symbolize justice but "
                        "actively records and testifies.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 1:6-8",
                "summary": "God is witness of the innermost feelings and a true observer "
                           "of the heart; the Spirit of the Lord has filled the world and "
                           "holds all things together, and nothing said in secret escapes "
                           "notice.",
                "relevance": "Wisdom of Solomon shares the Epistle\'s conviction that "
                             "nothing escapes divine observation, but frames it in terms "
                             "of God\'s Spirit filling creation rather than creation itself "
                             "recording and testifying.",
                "canon": False
            },
            {
                "source": "4Q416-418 (4QInstruction / Musar leMevin)",
                "summary": "A Qumran wisdom text instructing the poor to study the "
                           "\'mystery of existence\' (raz nihyeh) and trust that "
                           "eschatological judgment will vindicate them against their "
                           "exploiters.",
                "relevance": "Like the Epistle, 4QInstruction addresses an economically "
                             "marginalized community and assures them of eschatological "
                             "reversal. Both texts combine wisdom instruction with "
                             "apocalyptic hope.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 30:19", "note": "I call heaven and earth to witness against you today — the foundational OT text for creation as covenant witness, which the Epistle develops into cosmic testimony at the final judgment", "type": "ot"},
            {"ref": "Isaiah 1:2", "note": "Hear, O heavens, and give ear, O earth — the prophetic invocation of creation as witness to Israel\'s unfaithfulness", "type": "ot"},
            {"ref": "Deuteronomy 25:13-16", "note": "You shall not have two kinds of weights in your bag — the Torah\'s condemnation of false weights that the Epistle echoes in its attack on economic corruption", "type": "ot"},
            {"ref": "Amos 8:4-6", "note": "You who trample on the needy and bring the poor to ruin, making the ephah small and the shekel great, dealing deceitfully with false balances — prophetic social justice rhetoric that the Epistle continues", "type": "ot"},
            {"ref": "Romans 8:19-22", "note": "The creation waits with eager longing... the whole creation has been groaning together — Paul\'s vision of creation\'s involvement in the drama of salvation echoes the Epistle\'s cosmic witness", "type": "nt"},
            {"ref": "Romans 1:18-20", "note": "God\'s invisible attributes have been clearly perceived in the things that have been made, so they are without excuse — creation as witness to divine truth, leaving sinners without defense", "type": "nt"},
            {"ref": "James 5:1-6", "note": "The wages of the laborers you kept back by fraud are crying out, and the cries have reached the ears of the Lord of hosts — the closest NT parallel to the Epistle\'s cosmic witness and social justice themes", "type": "nt"},
            {"ref": "Revelation 6:9-10", "note": "The souls under the altar crying \'How long?\' — the righteous dead demanding vindication, as in the Epistle\'s assurance that their testimony is recorded in heaven", "type": "nt"}
        ],

        "divine_council_note": "The cosmic witness theology of the Epistle extends the "
                               "divine council\'s surveillance to all of creation. The sun, "
                               "moon, and stars are not merely obedient luminaries (as in "
                               "the Astronomical Book) but also observers who record human "
                               "behavior and will testify at the final trial. This means "
                               "the council\'s intelligence network is total: not only the "
                               "recording angels (1 Enoch 89:61, 100:10) but the elements "
                               "themselves gather evidence. No act of injustice occurs "
                               "without a cosmic witness. The forensic theology is complete: "
                               "witnesses (creation), records (heavenly tablets), a judge "
                               "(the Most High), a court (the divine council), and a "
                               "verdict (eschatological judgment).",

        "sections": [
            {
                "heading": "Creation as Forensic Witness (97:6 - 100:11)",
                "body": "The cosmic witness theme reaches its fullest expression in "
                        "the Epistle. \'The stars of heaven shall testify against you; "
                        "for you have committed blasphemy against the Great and Holy One\' "
                        "(97:6, paraphrased from the broader context). \'And now, know ye "
                        "that from the angels He will inquire as to your deeds in heaven, "
                        "from the sun and from the moon and from the stars in reference "
                        "to your sins, because upon the earth ye execute judgment on the "
                        "righteous\' (100:10). The sun has watched every act of oppression. "
                        "The moon has observed every injustice done under cover of "
                        "darkness. The stars have recorded every blasphemous word. These "
                        "celestial bodies are not passive objects but angelic agents "
                        "(recall that stars in 1 Enoch are often identified with angels). "
                        "They constitute an army of witnesses whose testimony will be "
                        "irrefutable at the final trial. The forensic language is "
                        "deliberate: this is a court scene, and creation is the "
                        "prosecution\'s witness pool. Deuteronomy 30:19\'s invocation "
                        "of heaven and earth as witnesses is here expanded to encompass "
                        "every celestial body, every natural phenomenon, and every "
                        "element of the created order."
            },
            {
                "heading": "Economic Injustice as Cosmic Sin (97:8 - 99:2)",
                "body": "The Epistle\'s social justice accusations are specific and "
                        "concrete, not merely rhetorical. The sinners \'build their houses "
                        "with the toil of others\' (99:13, paraphrased) — using corvee "
                        "labor or debt slavery to construct estates. They accumulate "
                        "gold and silver through unjust means (97:8-10). They use false "
                        "weights and measures to cheat in trade (implied in the broader "
                        "economic critique). They \'write lying and godless words\' (98:15) "
                        "— possibly producing false legal documents or corrupted scribal "
                        "texts. The economic specificity suggests a real social context: "
                        "Hellenistic-era Judea, where Greek mercantile practices and "
                        "Seleucid taxation created sharp inequalities between a "
                        "landowning elite and an impoverished peasantry. The Epistle\'s "
                        "audience appears to be the latter — the poor faithful who see "
                        "the wicked prosper and wonder if God has noticed. The answer is "
                        "emphatic: God has noticed, creation has recorded it, and "
                        "judgment is coming."
            },
            {
                "heading": "The Sinners\' False Security (99:3-16)",
                "body": "Chapter 99 contains an extended indictment of the sinners\' "
                        "false confidence. They worship idols: \'Woe to you who worship "
                        "stones, and grave images of gold and silver and wood\' (99:7). "
                        "They trust in false teachings: \'Woe to you who acquire silver "
                        "and gold in unrighteousness and say: \"We have become rich... "
                        "and have acquired everything we desired\"\' (99:13). The self-"
                        "congratulatory speech of the sinners echoes Deuteronomy 8:17 "
                        "(\'My power and the might of my hand have gotten me this "
                        "wealth\'). Their security is an illusion because the cosmic "
                        "record tells a different story. The contrast between appearances "
                        "and reality is the Epistle\'s core concern: on earth, the "
                        "sinners appear to prosper and the righteous appear to fail. "
                        "In heaven, the tablets show the opposite — the righteous are "
                        "inscribed for glory and the sinners for destruction. The "
                        "Epistle urges its audience to live by the heavenly record, "
                        "not by earthly appearances. This same appeal to the heavenly "
                        "perspective over the earthly would later characterize Paul\'s "
                        "letters (2 Cor 4:16-18: \'We look not to the things that are "
                        "seen but to the things that are unseen\')."
            }
        ]
    },

    # =========================================================================
    # THE WOE ORACLES (1 Enoch 94-100)
    # =========================================================================
    {
        "id": "1en-94-100",
        "ref": "1 Enoch 94-100",
        "chapter_num": 94,
        "title": "Woe to the Sinners — Wealth, Oppression, and Coming Judgment",
        "era": "epistle",
        "type": "chapter",

        "synopsis": "Chapters 94-100 contain a series of woe-oracles addressed to the "
                    "wealthy and powerful who oppress the righteous. The language is "
                    "fiery prophetic rhetoric modeled on the OT prophetic woe-oracles "
                    "(Isaiah 5, Amos 6, Habakkuk 2). The sinners are indicted for "
                    "building fine houses through exploitation, accumulating gold and "
                    "silver through injustice, writing lying records to pervert "
                    "truth, and persecuting the righteous. The response is a series "
                    "of woe-pronouncements promising eschatological reversal: the "
                    "oppressors will face judgment, and the righteous poor will be "
                    "vindicated. The social critique is among the sharpest in Second "
                    "Temple literature, anticipating the Magnificat (Luke 1:46-55) "
                    "and James 5:1-6.",

        "key_verse": {
            "ref": "1 Enoch 96:4-5",
            "text": "Woe to you, ye rich, for ye have trusted in your riches, and "
                    "from your riches shall ye depart, because ye have not remembered "
                    "the Most High in the days of your riches. Ye have committed "
                    "blasphemy and unrighteousness, and have become ready for the "
                    "day of slaughter, and the day of darkness and the day of the "
                    "great judgement.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "mishpat",
            "tsedaqah",
            "arar",
            "goy",
            "sheol",
            "yom_yhwh",
        ],

        "ane_backdrop": "The prophetic 'woe' (Hebrew hoy) oracle is a distinctively "
                        "Israelite literary form with no close ANE parallel in its "
                        "specific structure, though Mesopotamian wisdom literature "
                        "contains analogous denunciations of the unjust rich. The "
                        "social critique of chapters 94-100 reflects the economic "
                        "inequalities of the Hellenistic period, when Greek "
                        "mercantile practices and taxation systems exacerbated "
                        "disparities between a wealthy elite and the agrarian poor. "
                        "The concentration of land ownership in the hands of few, "
                        "the exploitation of debt servitude, and the corruption of "
                        "legal systems are recurrent themes in both 1 Enoch and in "
                        "contemporary Hellenistic protest literature.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 2:10-20",
                "summary": "The wicked plan to oppress the righteous poor man, test "
                           "him with insult and torture, and condemn him to a shameful "
                           "death — confident that their power makes them right.",
                "relevance": "Wisdom of Solomon independently describes the same "
                             "dynamic as 1 Enoch 94-100: wealthy sinners persecuting "
                             "the righteous and facing eschatological reversal. Both "
                             "texts address the theodicy problem of why the wicked "
                             "prosper and the righteous suffer.",
                "canon": False
            },
            {
                "source": "4Q416-418 (4QInstruction / Musar leMevin)",
                "summary": "A Qumran wisdom text that addresses the poor and tells "
                           "them to study the 'mystery of existence' (raz nihyeh) "
                           "rather than pursue wealth. Eschatological judgment will "
                           "vindicate them.",
                "relevance": "Like 1 Enoch 94-100, 4QInstruction addresses an "
                             "economically marginalized audience and assures them "
                             "that divine judgment will reverse current inequalities.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 5:8-23", "note": "A series of six woe-oracles against those who accumulate houses and land, pursue drunkenness, call evil good, and accept bribes — the prophetic model for 1 Enoch 94-100", "type": "ot"},
            {"ref": "Amos 6:1-7", "note": "Woe to those at ease in Zion, who lie on beds of ivory and eat lambs from the flock — prophetic indictment of luxury amid injustice", "type": "ot"},
            {"ref": "Habakkuk 2:6-20", "note": "Five woe-oracles against the plunderer, the unjust builder, the violent, the drunkard, and the idolater — the closest OT structural parallel to 1 Enoch's woe series", "type": "ot"},
            {"ref": "Luke 6:24-26", "note": "Woe to you who are rich, who are full now, who laugh now — Jesus' woe-oracles in the Sermon on the Plain echo 1 Enoch's eschatological reversal of wealth and poverty", "type": "nt"},
            {"ref": "James 5:1-6", "note": "Come now, you rich, weep and howl for the miseries that are coming upon you. Your riches have rotted — the most direct NT parallel to 1 Enoch 96-97's denunciation of the wealthy oppressors", "type": "nt"},
            {"ref": "Luke 1:46-55", "note": "The Magnificat: He has filled the hungry with good things and sent the rich away empty — Mary's song articulates the eschatological reversal that 1 Enoch 94-100 proclaims", "type": "nt"},
            {"ref": "Matthew 23:13-36", "note": "Jesus' seven woe-oracles against the scribes and Pharisees — the same literary form as 1 Enoch's woes, applied to religious rather than economic corruption", "type": "nt"},
            {"ref": "Revelation 18:1-24", "note": "The fall of Babylon the Great, the lament of merchants and kings over her destruction — the Apocalypse's woe against the wealthy system echoes 1 Enoch's anti-wealth rhetoric", "type": "nt"}
        ],

        "divine_council_note": "The woe-oracles of chapters 94-100 derive their "
                               "authority from Enoch's position as a council insider. "
                               "He can pronounce judgment on the sinners because he has "
                               "read the heavenly tablets (81:1-4) and knows the "
                               "predetermined fate of both righteous and wicked. The "
                               "woe-oracle form itself originates in the council: the "
                               "prophet who has 'stood in the council of the LORD' "
                               "(Jer 23:18) pronounces the council's verdict on the "
                               "earth. Enoch's woes are not personal opinions but "
                               "authorized declarations of the divine court's sentence.",

        "sections": [
            {
                "heading": "Woe to the Wealthy Oppressors (94:6 - 96:8)",
                "body": "The woe-oracles begin with a sharp indictment: 'Woe to those "
                        "who build their houses with sin; for from all their "
                        "foundations shall they be overthrown, and by the sword shall "
                        "they fall' (94:7). The 'houses built with sin' are literal "
                        "estates constructed through exploitation of the poor — a "
                        "direct echo of Isaiah 5:8 ('Woe to those who join house to "
                        "house, who add field to field'). The wealth indictment "
                        "intensifies: 'Woe to you, ye rich, for ye have trusted in "
                        "your riches, and from your riches shall ye depart, because "
                        "ye have not remembered the Most High in the days of your "
                        "riches' (96:4). The sin is not wealth per se but trust in "
                        "wealth combined with forgetting God — the same dynamic Jesus "
                        "describes in the parable of the Rich Fool (Luke 12:16-21). "
                        "The indictment extends to intellectual dishonesty: 'Woe to "
                        "you who write lying and godless words; for they write their "
                        "lies that men may hear them and act godlessly towards their "
                        "neighbour' (98:15). This may target rival scribal groups who "
                        "produce texts the Enochic community considers false — "
                        "possibly calendrical texts promoting the lunar calendar or "
                        "interpretive traditions that deny the Watcher reading of "
                        "Genesis 6."
            },
            {
                "heading": "The Cry of the Righteous and Cosmic Witness (97:1 - 99:16)",
                "body": "The woe-oracles include assurance to the suffering righteous. "
                        "'Fear ye not, ye that have suffered; for healing shall be "
                        "your portion, and a bright light shall enlighten you, and "
                        "the voice of rest ye shall hear from heaven' (96:3). The "
                        "contrast is stark: 'Woe to you, ye sinners, for your riches "
                        "make you appear like the righteous, but your hearts convict "
                        "you of being sinners' (96:4). External prosperity masks "
                        "internal corruption. Chapter 97 describes cosmic testimony: "
                        "the earth itself, the luminaries, and the elements will "
                        "testify against the sinners at the judgment. 'The stars of "
                        "heaven shall testify against you; for you have committed "
                        "blasphemy against the Great and Holy One' (97:6). This cosmic "
                        "witness tradition recurs in Deuteronomy 30:19 ('I call heaven "
                        "and earth to witness against you'), Isaiah 1:2 ('Hear, O "
                        "heavens, and give ear, O earth'), and Romans 8:22 ('the whole "
                        "creation groans'). Chapter 99 includes a remarkable passage "
                        "about false worship: 'Woe to you who worship stones, and "
                        "grave images of gold and silver and wood' (99:7). The idolatry "
                        "critique places the Epistle firmly in the prophetic tradition "
                        "of Isaiah 44:9-20 and Psalm 115:4-8."
            },
            {
                "heading": "The Day of Judgment — Sinners' Terror and the Righteous' Vindication (100:1-13)",
                "body": "Chapter 100 describes the day of judgment in terms that "
                        "anticipate the NT's eschatological language. 'In those days "
                        "the angels shall descend into the secret places and gather "
                        "together into one place all those who brought down sin... "
                        "the Most High will arise on that day of judgement to execute "
                        "great judgement amongst sinners' (100:4). The judgment is "
                        "cosmic in scope: 'And all the idols of the heathen shall be "
                        "abandoned, and the temples burned with fire, and they shall "
                        "remove them from the whole earth, and they (the heathen) "
                        "shall be cast into the judgement of fire, and shall perish "
                        "in wrath and in the severe judgement for ever' (100:9). "
                        "Alongside this judgment stands vindication: 'And the "
                        "righteous one shall arise from sleep, and wisdom shall arise "
                        "and be given unto them' (91:10, in context). The language of "
                        "'arising from sleep' echoes Daniel 12:2 ('many of those who "
                        "sleep in the dust of the earth shall awake') and anticipates "
                        "1 Thessalonians 4:14-16 ('the dead in Christ will rise'). "
                        "The woe section ends with the assurance that God has not "
                        "forgotten the suffering of the righteous: 'I know this "
                        "mystery... the angels record your righteousness before the "
                        "glory of the Great One' (100:10, 104:1). Every act of "
                        "faithfulness is inscribed in the heavenly record."
            }
        ]
    },

    # =========================================================================
    # HISTORICAL INSERT: THE APOCALYPSE OF WEEKS AND DANIEL'S SEVENTY WEEKS
    # =========================================================================
    {
        "id": "insert-apocalypse-weeks-daniel",
        "ref": "Historical Context",
        "chapter_num": None,
        "title": "The Apocalypse of Weeks and Daniel's Seventy Weeks — Two Schemas of Predetermined History",
        "era": "epistle",
        "type": "historical_insert",

        "synopsis": "The Apocalypse of Weeks (1 Enoch 93:1-10 + 91:12-17) and "
                    "Daniel's Seventy Weeks (Daniel 9:24-27) are the two most "
                    "important chronological schemas in Second Temple Judaism. "
                    "Both divide history into 'weeks,' both were composed during "
                    "or near the Maccabean crisis, and both climax with "
                    "eschatological judgment. Yet they differ in structure, scope, "
                    "and emphasis. Understanding their relationship illuminates "
                    "how Jewish apocalypticists used periodized history to make "
                    "sense of suffering and affirm divine sovereignty. "
                    "Revelation's seven-fold structures (seven churches, seals, "
                    "trumpets, bowls) continue this tradition of schematized "
                    "sacred history.",

        "key_verse": {
            "ref": "Daniel 9:24",
            "text": "Seventy weeks are decreed about your people and your holy city, to finish the transgression, to put an end to sin, and to atone for iniquity, to bring in everlasting righteousness, to seal both vision and prophet, and to anoint a most holy place.",
            "translation": "ESV"
        },
        "hebrew_terms": [
            "mishpat",
            "olam",
            "mashiach",
            "berit",
            "tsaddiq",
        ],
        "ane_backdrop": None,
        "second_temple": [],

        "cross_refs": [
            {"ref": "Daniel 9:24-27", "type": "ot", "note": "Seventy weeks (490 years) decreed: 7 weeks to rebuild Jerusalem, 62 weeks to the anointed one, 1 final week of tribulation. The canonical week-schema for Israel's future."},
            {"ref": "Leviticus 25:8-12", "type": "ot", "note": "Seven sabbaths of years (7 x 7 = 49 years), then the Jubilee. The Jubilee cycle provides the mathematical basis for both Daniel's seventy weeks and the Apocalypse of Weeks."},
            {"ref": "2 Chronicles 36:21", "type": "ot", "note": "The exile lasted seventy years to fulfill Sabbath rest for the land — the starting point for Daniel's reinterpretation of Jeremiah's seventy years as seventy weeks of years."},
            {"ref": "Jeremiah 25:11-12", "type": "ot", "note": "These nations shall serve the king of Babylon seventy years — the prophecy that Daniel reinterprets in terms of weeks and that the Apocalypse of Weeks schematizes differently."},
            {"ref": "Revelation 2-3", "type": "nt", "note": "The seven churches of Asia — Revelation's seven-fold structure continues the tradition of schematized periods, possibly drawing on both Enochic and Danielic models."},
            {"ref": "Matthew 18:22", "type": "nt", "note": "Not seven times but seventy-seven times (or seventy times seven) — Jesus using the 'seventy weeks' numerical tradition to redefine the scope of forgiveness."},
            {"ref": "Galatians 4:4", "type": "nt", "note": "When the fullness of time had come, God sent his Son — the NT conviction that the Messiah arrived at the appointed moment in the predetermined schedule, the theological legacy of both week-schemas."},
            {"ref": "4Q212 (4QEn-g)", "type": "dss", "note": "Aramaic fragments of the Apocalypse of Weeks from Qumran, confirming its pre-Christian date and its circulation alongside Daniel in the same community."}
        ],

        "divine_council_note": "Both the Apocalypse of Weeks and Daniel's Seventy "
                               "Weeks presuppose that the divine council has "
                               "predetermined history according to a numerical schema. "
                               "In Daniel 9, the angel Gabriel reveals the decree; "
                               "in the Apocalypse of Weeks, Enoch reads the schedule "
                               "from the heavenly tablets. Both texts present history "
                               "as a council document — minutes of a meeting that "
                               "took place before creation, now disclosed to the "
                               "elect for their encouragement.",

        "sections": [
            {
                "heading": "Structural Comparison",
                "body": "The Apocalypse of Weeks divides all history into <b>ten "
                        "undefined periods</b> ('weeks') from Enoch to the new "
                        "creation. Daniel's schema divides a specific portion of "
                        "Israel's future into <b>seventy weeks of seven years each</b> "
                        "(490 years) from the decree to rebuild Jerusalem to the "
                        "eschaton. The Apocalypse of Weeks is broader in scope "
                        "(all history from creation) but vaguer in duration (no "
                        "year counts). Daniel is narrower in scope (from the exile "
                        "forward) but more numerically precise. Both use the 'week' "
                        "as the fundamental unit, reflecting the Sabbath/Jubilee "
                        "theology of Leviticus 25: time is structured in sevens, "
                        "and the culmination of a series of sevens brings liberation "
                        "(Jubilee) or judgment. The ten-week structure of the "
                        "Apocalypse of Weeks may derive from the ten-generation "
                        "genealogies of Genesis 5 and 11, while Daniel's seventy "
                        "weeks reinterprets Jeremiah's seventy years (Jeremiah "
                        "25:11-12) by multiplying by seven."
            },
            {
                "heading": "Corresponding Events and Divergences",
                "body": "Several pivotal events appear in both schemas, though "
                        "placed differently. Both treat the destruction of the "
                        "Temple as a critical turning point: in the Apocalypse of "
                        "Weeks, the Temple is burned in Week 6; in Daniel, the "
                        "sanctuary is destroyed by the forces of the 'prince who "
                        "is to come' (9:26). Both culminate in an eschatological "
                        "resolution: the Apocalypse of Weeks ends with new heavens "
                        "and eternal judgment in Week 10; Daniel ends with the "
                        "cessation of sacrifice, the abomination of desolation, "
                        "and the 'decreed end' poured out on the desolator (9:27). "
                        "Both were composed in response to the Maccabean crisis "
                        "(c. 167-164 BC), and both place their audience at the "
                        "critical juncture just before divine intervention: the "
                        "Apocalypse of Weeks locates the elect at the end of Week 7 "
                        "(about to enter Week 8's vindication), and Daniel locates "
                        "the faithful in the midst of the final half-week of "
                        "tribulation. The rhetorical function is identical: 'You "
                        "are HERE on the divine schedule, and deliverance is "
                        "imminent.' Where they diverge is telling: the Apocalypse "
                        "of Weeks is more interested in the community of the elect "
                        "(the 'plant of righteousness'), while Daniel focuses on "
                        "the anointed figure and the temple cult."
            },
            {
                "heading": "Legacy in Jewish and Christian Interpretation",
                "body": "Both schemas profoundly influenced subsequent apocalyptic "
                        "thinking. Daniel's seventy weeks became the most calculated "
                        "messianic prophecy in Judaism, with rabbinic, Christian, "
                        "and sectarian interpreters attempting to decode its precise "
                        "chronology. The Apocalypse of Weeks influenced the Qumran "
                        "community's own periodization texts (4Q180-181, 11Q13 "
                        "Melchizedek) and may have contributed to the ten-Jubilee "
                        "schema of 11QMelchizedek, which envisions eschatological "
                        "liberation at the end of ten Jubilee periods. In the NT, "
                        "the conviction that Jesus appeared at 'the fullness of time' "
                        "(Galatians 4:4) reflects the same theological framework: "
                        "history has been divided into predetermined periods, and the "
                        "Messiah arrives at exactly the right moment in the schedule. "
                        "Revelation's structure of sevens (seven seals, trumpets, "
                        "bowls, churches) continues the tradition of schematized "
                        "judgment periods that both the Apocalypse of Weeks and "
                        "Daniel's seventy weeks established. Matthew's woe oracles "
                        "(23:13-36) and the letters to the seven churches (Revelation "
                        "2-3) both reflect communities that understood themselves as "
                        "living at a critical juncture in the divine schedule — the "
                        "same self-understanding that the Apocalypse of Weeks "
                        "cultivated for its original audience."
            }
        ]
    },

    # =========================================================================
    # AFTERLIFE AND EXHORTATION (1 Enoch 102-105)
    # =========================================================================
    {
        "id": "1en-102-105",
        "ref": "1 Enoch 102-105",
        "chapter_num": 102,
        "title": "The Fate of the Righteous Dead — Hope Beyond Death",
        "era": "epistle",
        "type": "chapter",

        "synopsis": "Chapters 102-105 address the most urgent question facing the "
                    "persecuted righteous: what happens after death? The sinners "
                    "mock the righteous, saying, 'As we die, so die the righteous "
                    "— what benefit do they get for their deeds?' (102:6-8). Enoch's "
                    "answer is emphatic: the spirits of the righteous dead live on, "
                    "their names are written before the Great One, and they will "
                    "experience joy, honor, and light. The wicked dead, by contrast, "
                    "descend to Sheol where 'great darkness' awaits them. This "
                    "section is one of the most developed afterlife theologies in "
                    "Second Temple literature, bridging the gap between the shadowy "
                    "Sheol of the older OT texts and the fully articulated "
                    "heaven/hell theology of the NT.",

        "key_verse": {
            "ref": "1 Enoch 103:3-4",
            "text": "Now I know this mystery, that sinners will alter and pervert "
                    "the words of righteousness in many ways, and will speak "
                    "wicked words, and lie, and practice great deceits... But "
                    "fear not, ye righteous, when ye see the sinners growing "
                    "strong and prospering in their ways: be not companions with "
                    "them, but keep afar from their violence; for ye shall become "
                    "companions of the hosts of heaven.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "sheol",
            "nefesh",
            "tsaddiq",
            "mishpat",
            "olam",
            "ruach",
        ],

        "ane_backdrop": "The question of post-mortem justice — why the righteous "
                        "suffer in life and what happens after death — is one of the "
                        "oldest theological problems in the ANE. The Mesopotamian "
                        "Descent of Ishtar and the Gilgamesh Epic depict the underworld "
                        "as a shadowy, undifferentiated realm. Egyptian religion, by "
                        "contrast, developed a rich afterlife theology with judgment "
                        "before Osiris, the weighing of the heart against Ma'at "
                        "(truth), and differentiated post-mortem fates. The Epistle of "
                        "Enoch's afterlife theology falls between these poles: more "
                        "differentiated than the older Israelite Sheol (cf. Eccles "
                        "9:10) but not yet as architecturally detailed as 1 Enoch 22's "
                        "four-compartment geography.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 3:1-9",
                "summary": "The souls of the righteous are in the hand of God, and "
                           "no torment will ever touch them. In the eyes of the "
                           "foolish they seemed to have died... but they are at peace. "
                           "They will govern nations and the Lord will reign over them.",
                "relevance": "Wisdom of Solomon independently develops the same "
                             "response to the same problem as 1 Enoch 102-104: the "
                             "righteous appear to die like everyone else, but their "
                             "souls are safe with God, and eschatological vindication "
                             "awaits them.",
                "canon": False
            },
            {
                "source": "2 Maccabees 7:9-14",
                "summary": "The seven martyred brothers declare their confidence in "
                           "resurrection: 'The King of the universe will raise us up "
                           "to an everlasting renewal of life, because we have died "
                           "for his laws.'",
                "relevance": "2 Maccabees shows that by the 2nd century BC, belief in "
                             "bodily resurrection as vindication of the martyred "
                             "righteous was a live option in Jewish theology — the same "
                             "confidence that pervades 1 Enoch 102-104.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Ecclesiastes 9:2-10", "note": "The same fate befalls the righteous and the wicked; the dead know nothing — the skeptical position that the Epistle of Enoch directly refutes", "type": "ot"},
            {"ref": "Daniel 12:2-3", "note": "Many who sleep in the dust shall awake, some to everlasting life, some to shame — the canonical resurrection hope that the Epistle develops", "type": "ot"},
            {"ref": "Matthew 5:11-12", "note": "Blessed are you when others revile you and persecute you... for great is your reward in heaven — Jesus' promise to the persecuted echoes 1 Enoch's assurance to suffering righteous", "type": "nt"},
            {"ref": "Luke 16:19-31", "note": "The rich man and Lazarus — differentiated afterlife fates for the wealthy wicked and the poor righteous, presupposing the theology of 1 Enoch 102-104", "type": "nt"},
            {"ref": "Revelation 6:9-11", "note": "The souls of the slain under the altar crying out 'How long, O Lord?' — the righteous dead demanding vindication, as in 1 Enoch's righteous dead whose testimonies are recorded in heaven", "type": "nt"},
            {"ref": "Philippians 1:21-23", "note": "To depart and be with Christ is far better — Paul's confidence about the intermediate state echoes the Enochic assurance that the righteous dead are in God's care", "type": "nt"},
            {"ref": "2 Corinthians 5:1-8", "note": "We would rather be away from the body and at home with the Lord — Pauline afterlife hope shaped by the Second Temple tradition of conscious post-mortem existence", "type": "nt"},
            {"ref": "4Q212 (4QEn-g)", "type": "dss", "note": "Aramaic fragments of the Epistle of Enoch, preserving portions of the woe-oracles and exhortation sections, confirming the text's pre-Christian date"}
        ],

        "divine_council_note": "The afterlife theology of the Epistle rests on the "
                               "divine council's record-keeping. The names of the "
                               "righteous are 'written before the glory of the Great "
                               "One' (104:1) — inscribed in the heavenly registry that "
                               "the council maintains. The recording angels note every "
                               "act of righteousness and every act of oppression. Death "
                               "does not erase the record; the council's books persist "
                               "beyond mortal life. This is the theological basis for "
                               "post-mortem vindication: the divine court has the "
                               "evidence, and the verdict will eventually be rendered. "
                               "The righteous dead can 'hope' (103:3-4) precisely "
                               "because the council's archives guarantee that nothing "
                               "is lost.",

        "sections": [
            {
                "heading": "The Sinners' Taunt — 'We Die Alike' (102:1-11)",
                "body": "Chapter 102 opens with a cosmic-judgment scene — 'the heaven "
                        "of heavens shall quake and tremble, and those who are in "
                        "the high heavens shall be smitten' (102:1) — before turning "
                        "to the core problem: the sinners' mockery of the righteous "
                        "dead. 'And they said unto the righteous: \"As we die, so die "
                        "the righteous, and what benefit do they reap for their deeds? "
                        "Behold, even as we, so do they die in grief and darkness, "
                        "and what have they more than we? From henceforth we are "
                        "equal\"' (102:6-8). This is the Epicurean objection: if death "
                        "is the same for all, then righteousness is pointless. It is "
                        "the voice of Ecclesiastes 9:2 radicalized into a taunt. "
                        "Enoch's response is direct: 'I tell you: their spirits of "
                        "those who have died in righteousness shall live and rejoice, "
                        "and their spirits shall not perish, nor their memorial from "
                        "before the face of the Great One' (103:4). The afterlife is "
                        "not the same for all. The righteous dead live on in the "
                        "presence of the Great One (God), while the wicked descend "
                        "to darkness. This passage is foundational for the NT's "
                        "confidence in differentiated post-mortem existence."
            },
            {
                "heading": "Companions of the Hosts of Heaven (103:1 - 104:6)",
                "body": "Enoch assures the righteous that their post-mortem state "
                        "will be one of honor and companionship with the angels. 'Ye "
                        "shall become companions of the hosts of heaven' (104:6). The "
                        "righteous dead do not merely survive; they are elevated to "
                        "the company of the divine council. They will 'shine as the "
                        "lights of heaven' (104:2) — language drawn from Daniel 12:3 "
                        "('those who are wise shall shine like the brightness of the "
                        "sky') and anticipating Matthew 13:43 ('the righteous will "
                        "shine like the sun in the kingdom of their Father'). The "
                        "transformation is ontological: mortal humans become like "
                        "celestial beings. This is not merely a metaphor for reward "
                        "but a description of actual transformation — the same "
                        "tradition that Paul develops in 1 Corinthians 15:41-44 "
                        "('star differs from star in glory... so also is the "
                        "resurrection of the dead'). Chapter 104 adds: 'I know "
                        "another mystery, that books shall be given to the righteous "
                        "and the wise to become a cause of joy and uprightness' "
                        "(104:12). The 'books' are the Enochic writings themselves — "
                        "the text is self-referentially legitimizing its own "
                        "transmission. The Epistle of Enoch claims that its own "
                        "composition is part of the divine plan for the consolation "
                        "of the righteous."
            },
            {
                "heading": "The Heavenly Record and the Assurance of Justice (104:7 - 105:2)",
                "body": "The Epistle's assurance of post-mortem justice rests on the "
                        "certainty of divine record-keeping. 'Fear ye not, ye "
                        "righteous; for when ye see the sinners growing strong, and "
                        "prospering in their ways, be not companions with them, but "
                        "keep afar from their violence; for ye shall become companions "
                        "of the hosts of heaven' (104:6). The righteous should not be "
                        "envious or despairing but patient, because the divine court "
                        "has kept meticulous records: 'And now I know that the sinners "
                        "will alter and pervert the words of righteousness' (103:3) — "
                        "but it does not matter, because the heavenly tablets preserve "
                        "the truth regardless of what humans do with texts on earth. "
                        "Chapter 105 contains what some scholars identify as a "
                        "fragment of the 'Book of Noah': 'In those days, saith the "
                        "Lord, they shall call and testify to the children of earth "
                        "concerning their wisdom: show it unto them, for ye are their "
                        "guides' (105:1). The righteous are not merely passive "
                        "recipients of vindication but active witnesses whose "
                        "testimony will be heard. The Epistle ends where it began: "
                        "with the confidence that the divine court's verdict, though "
                        "delayed, is certain, and that the books of heaven — including "
                        "the text the reader now holds — are the guarantee."
            }
        ]
    },

    # =========================================================================
    # APPENDIX: BIRTH OF NOAH (1 Enoch 106-108)
    # =========================================================================
    {
        "id": "1en-106-108",
        "ref": "1 Enoch 106-108",
        "chapter_num": 106,
        "title": "The Birth of Noah — A Child of Light",
        "era": "epistle",
        "type": "chapter",

        "synopsis": "The final chapters of 1 Enoch form an appendix describing the "
                    "miraculous birth of Noah. When Lamech's wife bears a child, the "
                    "baby has extraordinary features: his flesh is white as snow and "
                    "red as a rose, his hair is white as wool, and his eyes illuminate "
                    "the entire house like the sun. Lamech is terrified and suspects "
                    "the child is the offspring of a Watcher. He sends Methuselah to "
                    "Enoch (who is already in paradise) to inquire. Enoch reassures "
                    "them: Noah is legitimate, not a Watcher's child, and is destined "
                    "to survive the coming Flood. The passage is likely drawn from "
                    "a 'Book of Noah' that circulated independently. Chapter 108 "
                    "provides a final exhortation about the contrasting fates of "
                    "the righteous and wicked.",

        "key_verse": {
            "ref": "1 Enoch 106:2-3",
            "text": "And his body was white as snow and red as the blooming of a "
                    "rose, and the hair of his head and his long locks were white "
                    "as wool, and his eyes beautiful. And when he opened his eyes, "
                    "he lighted up the whole house like the sun, and the whole "
                    "house was very bright.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "mabbul",
            "tebah",
            "nephilim",
            "tsaddiq",
            "berit",
            "kavod",
        ],

        "ane_backdrop": "The motif of a miraculous or divinely marked birth is "
                        "widespread in the ANE. Sargon of Akkad's birth legend "
                        "describes his mother placing him in a reed basket on the "
                        "river (paralleling Moses). The Egyptian Westcar Papyrus "
                        "describes the miraculous births of the first three kings of "
                        "the Fifth Dynasty. The luminous qualities of baby Noah — "
                        "shining like the sun, white as snow — echo the 'divine "
                        "radiance' (Akkadian melammu) that marks gods and divinized "
                        "kings in Mesopotamian tradition. In the Israelite tradition, "
                        "Moses' face shines after encountering God (Exodus 34:29-35). "
                        "Noah's birth luminosity thus signals divine favor and "
                        "special destiny.",

        "second_temple": [
            {
                "source": "1QapGen (Genesis Apocryphon) col. II-V",
                "summary": "The Qumran Genesis Apocryphon preserves a parallel account "
                           "of Noah's miraculous birth. Lamech suspects his wife "
                           "Bitenosh of having been intimate with a Watcher. She swears "
                           "her innocence. Lamech goes to his father Methuselah, who "
                           "goes to Enoch at 'the ends of the earth.'",
                "relevance": "The Genesis Apocryphon demonstrates that the Noah birth "
                             "narrative was a widely circulating tradition, not unique "
                             "to 1 Enoch 106-107. The Qumran version adds significant "
                             "detail, including Bitenosh's emphatic denial and the "
                             "emotional dynamics between Lamech and his wife.",
                "canon": False
            },
            {
                "source": "Jubilees 4:28",
                "summary": "A brief reference to Noah: 'He was perfect in all his "
                           "ways in his generations, and was found righteous and "
                           "perfect' — language echoing Genesis 6:9.",
                "relevance": "Jubilees does not preserve the miraculous birth tradition "
                             "but affirms Noah's exceptional righteousness, the "
                             "theological claim that underlies 1 Enoch 106's birth "
                             "narrative.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 5:28-29", "note": "Lamech names his son Noah, saying 'Out of the ground that the LORD has cursed, this one shall bring us relief' — 1 Enoch 106 expands this brief notice into a full miraculous birth narrative", "type": "ot"},
            {"ref": "Genesis 6:9", "note": "Noah was a righteous man, blameless in his generation; Noah walked with God — the canonical characterization that 1 Enoch 106's luminous birth seeks to explain", "type": "ot"},
            {"ref": "Daniel 7:9", "note": "The Ancient of Days whose hair is 'white like wool' — Noah's white-wool hair in 106:2 echoes the Ancient of Days, implying an association between the child and the divine", "type": "ot"},
            {"ref": "Revelation 1:14", "note": "His head and his hair were white, like white wool, like snow — the risen Christ described in terms that echo both Daniel 7:9 and the infant Noah of 1 Enoch 106", "type": "nt"},
            {"ref": "Matthew 17:2", "note": "His face shone like the sun — the transfigured Christ displaying the same luminous qualities as the infant Noah, signaling divine presence", "type": "nt"},
            {"ref": "1QapGen col. II-V (Genesis Apocryphon)", "type": "dss", "note": "The Qumran Aramaic parallel to 1 Enoch 106-107, preserving a more detailed version of the Noah birth narrative with Lamech's suspicion and Bitenosh's defense"},
            {"ref": "4Q534-536 (Birth of Noah / Elect of God)", "type": "dss", "note": "Additional Qumran fragments describing the birth of a miraculous child, sometimes identified with Noah, whose physical characteristics include marks on the body and exceptional wisdom"},
            {"ref": "Luke 1:13-17, 26-38", "note": "The angelic announcements of the births of John and Jesus — the NT's miraculous birth narratives follow the same literary pattern as 1 Enoch 106: divine child, parental anxiety, angelic reassurance", "type": "nt"}
        ],

        "divine_council_note": "Noah's luminous birth suggests a child who is already "
                               "marked by the divine council for a special role. His "
                               "appearance — white as snow, bright as the sun, hair like "
                               "wool — uses the visual vocabulary of theophany. He looks "
                               "like an angel or a divine being, which is precisely why "
                               "Lamech suspects Watcher paternity. But Enoch's "
                               "reassurance means that the luminosity is not a sign of "
                               "angelic descent but of divine election: God has marked "
                               "this child for the cosmic role of preserving humanity "
                               "through the Flood. The council's plan is written on "
                               "the heavenly tablets, and Noah's very body testifies "
                               "to it.",

        "sections": [
            {
                "heading": "The Luminous Child and Lamech's Fear (106:1-7)",
                "body": "Methuselah takes a wife for his son Lamech, and she conceives "
                        "and bears 'a son whose flesh was white as snow and red as the "
                        "blooming of a rose, and the hair of his head and his long "
                        "locks were white as wool, and his eyes beautiful. And when "
                        "he opened his eyes, he lighted up the whole house like the "
                        "sun' (106:2). The child immediately stands up in the hands "
                        "of the midwife and speaks to the Lord of righteousness (106:3). "
                        "Lamech is terrified: 'I have begotten a strange son, diverse "
                        "from and unlike man, and resembling the sons of the God of "
                        "heaven; and his nature is different and he is not like us' "
                        "(106:5-6). Lamech's fear is specifically that his wife has "
                        "been impregnated by a Watcher — the Watcher descent is "
                        "recent history in this narrative, and the trauma of chapters "
                        "6-11 is fresh. The description of Noah's luminous body "
                        "deliberately echoes the description of the divine throne in "
                        "1 Enoch 14 (crystal, fire, brightness) and anticipates the "
                        "description of the Ancient of Days in Daniel 7:9 (hair white "
                        "as wool). The child is not a Nephilim but he is marked by "
                        "the divine presence in ways that mirror both angelic and "
                        "divine attributes."
            },
            {
                "heading": "Methuselah's Journey and Enoch's Reassurance (106:8 - 107:3)",
                "body": "Lamech sends his father Methuselah to Enoch, who dwells 'at "
                        "the ends of the earth' in the company of the angels (106:8). "
                        "The geography is significant: Enoch is not dead but translated "
                        "(Genesis 5:24), living in the cosmic periphery that he "
                        "traversed in chapters 17-36. Methuselah makes the journey "
                        "and recounts Lamech's fears. Enoch's response draws on his "
                        "knowledge of the heavenly tablets: he confirms that Noah is "
                        "Lamech's legitimate son, not a Watcher's offspring. He then "
                        "prophesies: 'A great destruction is coming upon the whole "
                        "earth, and there is to be a deluge... And this son who has "
                        "been born unto you shall be left on the earth, and his three "
                        "children shall be saved' (106:15-18). The name 'Noah' is given "
                        "prophetically: 'Call his name Noah; for he shall be left to "
                        "you, and he and his sons shall be saved from the destruction' "
                        "(107:3). The name is connected to nacham (comfort/rest) as in "
                        "Genesis 5:29. The entire episode functions as a bridge between "
                        "the Enoch tradition and the Noah tradition, establishing "
                        "continuity between the two great pre-flood patriarchs."
            },
            {
                "heading": "The Final Exhortation — Fire and Light (108:1-15)",
                "body": "Chapter 108 concludes the entire 1 Enoch corpus with a final "
                        "statement about the contrasting fates of sinners and "
                        "righteous. It begins with a superscription: 'Another book "
                        "which Enoch wrote for his son Methuselah and for those who "
                        "will come after him' (108:1). The chapter describes a place "
                        "of fire where the spirits of sinners are confined: 'chaotic "
                        "and horrible' with 'fire burning, blazing, and falling on "
                        "every side' (108:3-5). In contrast, the righteous are "
                        "promised: 'Be hopeful; for aforetime ye were put to shame "
                        "through all kinds of evil and afflictions; but now ye shall "
                        "shine as the lights of heaven, ye shall shine and ye shall "
                        "be seen, and the portals of heaven shall be opened to you' "
                        "(108:11-12). The luminous transformation of the righteous "
                        "echoes Daniel 12:3 and anticipates Matthew 13:43. The portals "
                        "of heaven opening recalls the gates Enoch traversed in his "
                        "cosmic journeys — now accessible to all the righteous. The "
                        "final verse describes these righteous ones as those 'who love "
                        "God and loved neither gold nor silver nor any of the good "
                        "things which are in the world, but gave over their bodies to "
                        "suffering' (108:8). The Epistle's social critique reaches its "
                        "conclusion: the righteous are identified by their rejection "
                        "of wealth and their willingness to suffer — the same "
                        "identification that Jesus makes in the Beatitudes (Matt "
                        "5:3-12) and that James makes in his epistle (James 1:12, "
                        "2:5). The book of 1 Enoch ends where it began: with the "
                        "promise that the righteous will share in the glory that "
                        "Enoch himself entered when God 'took him.'"
            }
        ]
    }
]
