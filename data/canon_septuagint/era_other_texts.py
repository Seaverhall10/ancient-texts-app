"""
era_other_texts.py -- Jubilees, Book of Giants, and Beyond (Chapters 1-2)

Beyond 1 Enoch, the ancient Jewish world produced texts that illuminate the
canonical Scriptures in ways most modern readers have never encountered. The
Book of Jubilees -- found at Qumran in more copies than some canonical books
-- retells Genesis through Exodus with a precise calendar, an expanded
Watchers narrative, and the Mastema framework that explains how evil spirits
operate under divine permission. The Book of Giants names the Nephilim
individually and records their dream visions of the coming Flood judgment.
4 Ezra preserves the most developed Second Temple eschatological sequence
outside Revelation.

These texts are not Scripture. But they are the literature that the community
closest to Jesus and his apostles treated as authoritative. Understanding
them is not optional for serious biblical study.

Two chapters covering:
  1. Jubilees and the Book of Giants -- Qumran's core library holdings
  2. 4 Ezra and beyond -- the broader Second Temple literary world
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: JUBILEES AND THE BOOK OF GIANTS
    # =========================================================================
    {
        "id": "other-texts-1",
        "ref": "Genesis 6:1-4; Leviticus 25:8-12; Deuteronomy 32:8-9",
        "chapter_num": 1,
        "title": "Jubilees and the Book of Giants \u2014 Qumran\u2019s Core Library",
        "era": "other_texts",
        "type": "chapter",

        "synopsis": "Jubilees and the Book of Giants were not fringe documents at Qumran "
                    "-- they were core library holdings, found in multiple copies across "
                    "multiple caves. Jubilees ('Little Genesis') retells Genesis through "
                    "Exodus 14 within a precise 49-year jubilee cycle, adds the Mastema "
                    "framework for understanding evil spirits, and confirms the "
                    "Deuteronomy 32:8 national angel assignment. The Book of Giants names "
                    "the Nephilim (Ohyah, Hahyah, Mahaway), records their dream visions "
                    "of coming judgment, and contains a reference to Gilgamesh that "
                    "connects Mesopotamian epic to the biblical Nephilim tradition. Both "
                    "texts illuminate the canonical narrative without contradicting it.",

        "key_verse": {
            "ref": "Genesis 6:4",
            "text": "The Nephilim were on the earth in those days, and also afterward, "
                    "when the sons of God came in to the daughters of man and they "
                    "bore children to them. These were the mighty men who were of old, "
                    "the men of renown.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05d9\u05d5\u05b9\u05d1\u05b5\u05dc (yovel)",
                "meaning": "Jubilee -- a period of 49 years (seven cycles of seven years) "
                           "culminating in the 50th year of release (Leviticus 25:8-12). "
                           "The book of Jubilees organizes all of Genesis through Exodus "
                           "14 within this calendar framework, counting history in jubilee "
                           "periods from creation. The Qumran community used this calendar "
                           "system alongside the 364-day solar calendar."
            },
            {
                "term": "\u05de\u05b7\u05e9\u05b0\u05c2\u05d8\u05b5\u05de\u05b8\u05d4 (Mastema)",
                "meaning": "'Hostility, animosity.' According to Jubilees, Mastema is the "
                           "prince of evil spirits who petitions Yahweh after the Flood "
                           "to retain one-tenth of the Nephilim spirits free while "
                           "nine-tenths are imprisoned (Jubilees 10:8-9). He operates "
                           "under divine permission -- closely related to the hassatan "
                           "prosecutorial role in Job 1-2. Mastema is not the ultimate "
                           "adversary but the figure who leads the free evil spirits."
            },
            {
                "term": "\u05E0\u05B0\u05E4\u05B4\u05D9\u05DC\u05B4\u05D9\u05DD (Nephilim)",
                "meaning": "From the root naphal ('to fall') -- the offspring of the "
                           "unions between the 'sons of God' and human women in Genesis "
                           "6:4. The Book of Giants names them individually: Ohyah and "
                           "Hahyah (sons of Shemihazah), Mahaway (son of Barakel). They "
                           "are not anonymous monsters but named individuals whose specific "
                           "sins and judgments are documented."
            },
            {
                "term": "\u05d2\u05b4\u05bc\u05d1\u05bc\u05d5\u05b9\u05e8 (gibbor)",
                "meaning": "Mighty one, warrior, hero. The term used for Nimrod in "
                           "Genesis 10:8-9: 'the first on earth to be a gibbor.' The "
                           "Book of Giants contains an Aramaic reference to Gilgamesh "
                           "(glgmysh in 4Q530), connecting the Mesopotamian epic hero "
                           "to the post-Flood Nephilim pattern. Gilgamesh/Nimrod as the "
                           "first post-Flood figure carrying the Nephilim lineage."
            }
        ],

        "ane_backdrop": "The Mesopotamian literary tradition provides striking parallels "
                        "to both Jubilees and the Book of Giants. The Sumerian King List "
                        "records pre-Flood kings who ruled for impossibly long periods, "
                        "followed by a great flood, then post-Flood kings with normal "
                        "lifespans -- the same pattern as Genesis 5 through Genesis 11. "
                        "The Gilgamesh Epic features a hero who is two-thirds divine and "
                        "one-third human -- the Nephilim pattern of divine-human hybrid "
                        "offspring. The Book of Giants' Aramaic reference to Gilgamesh "
                        "(4Q530) explicitly connects these traditions: Gilgamesh is not "
                        "a Mesopotamian fiction but a corrupted memory of a real post-Flood "
                        "Nephilim figure. The apkallu tradition -- seven antediluvian "
                        "sages who brought knowledge from the gods -- mirrors 1 Enoch's "
                        "Watchers who bring forbidden knowledge, but with the moral "
                        "valuation reversed: the Mesopotamian tradition celebrates what "
                        "the Enochic tradition condemns.",

        "second_temple": [
            {
                "source": "Jubilees 10:8-9 (Mastema's Petition)",
                "summary": "According to Jubilees, after the Flood, Mastema petitions "
                           "God to retain one-tenth of the evil spirits (disembodied "
                           "Nephilim) free to operate on earth, while nine-tenths are "
                           "imprisoned. God grants this request. The prince of evil "
                           "spirits thus operates under divine permission -- he has "
                           "authority over a constrained number of demons.",
                "relevance": "This framework is theologically significant: if only "
                             "one-tenth of the total Nephilim spirits remain free, the "
                             "number of demons currently active is constrained. The rest "
                             "are imprisoned. Mastema's role parallels the hassatan of "
                             "Job 1-2 -- a prosecutor who operates under divine "
                             "permission, not an independent power."
            },
            {
                "source": "Jubilees 15:31-32 (National Angels)",
                "summary": "According to Jubilees, God 'set spirits over the nations "
                           "to lead them astray from him' but over Israel He set no "
                           "angel or spirit as ruler -- He Himself governs Israel "
                           "directly. This confirms the Deuteronomy 32:8-9 framework.",
                "relevance": "Jubilees independently confirms that Second Temple Judaism "
                             "understood the Deuteronomy 32 worldview: nations assigned "
                             "to divine beings, Israel directly under Yahweh. The LXX, "
                             "DSS, Jubilees, and Sirach all agree on this reading."
            },
            {
                "source": "Book of Giants, 4Q530 (Gilgamesh Reference)",
                "summary": "An Aramaic fragment from Qumran contains the name 'glgmysh' "
                           "-- identified by scholars as Gilgamesh of Mesopotamian epic "
                           "fame. In the Book of Giants, Gilgamesh appears as one of the "
                           "post-Flood Nephilim, directly connecting the Mesopotamian "
                           "hero tradition to the biblical Nephilim narrative.",
                "relevance": "This reference confirms the Nimrod-Gilgamesh connection. "
                             "Genesis 10:8 calls Nimrod 'the first gibbor on earth after "
                             "the Flood.' The Book of Giants identifies Gilgamesh as a "
                             "Nephilim figure. The Mesopotamian epic hero and the biblical "
                             "Nimrod are different cultural memories of the same phenomenon "
                             "-- post-Flood Nephilim lineage."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 6:1-4", "note": "The canonical account of the 'sons of God' and the Nephilim -- four verses that 1 Enoch, Jubilees, and the Book of Giants all expand and illuminate.", "type": "ot"},
            {"ref": "Genesis 10:8-9", "note": "Nimrod as 'the first gibbor on earth' after the Flood -- the Book of Giants' Gilgamesh reference connects this to the Nephilim pattern.", "type": "ot"},
            {"ref": "Leviticus 25:8-12", "note": "The jubilee cycle -- 49 years plus the 50th year of release. Jubilees organizes all of Genesis-Exodus within this framework.", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "Jubilees 15:31-32 independently confirms the 'sons of God' reading: nations assigned to spirits, Israel directly under Yahweh.", "type": "ot"},
            {"ref": "Job 1:6-12", "note": "The hassatan operating under divine permission -- the same framework as Mastema in Jubilees, who petitions God and receives authorized limits.", "type": "ot"},
            {"ref": "Mark 5:12-13", "note": "The Gadarene demons beg to be sent into pigs rather than face disembodiment -- consistent with 1 Enoch 15:8-10's description of demons as disembodied Nephilim spirits seeking re-embodiment.", "type": "nt"},
            {"ref": "Luke 8:31", "note": "The demons beg Jesus 'not to command them to depart into the abyss' -- they know their Watcher fathers are imprisoned there and fear the same fate.", "type": "nt"},
            {"ref": "Jubilees 10:8-9", "note": "According to Jubilees, Mastema retains 1/10 of the Nephilim spirits free while 9/10 are imprisoned -- constraining the active demonic population.", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "Jubilees and the Book of Giants fill critical gaps in the "
                               "divine council framework. Jubilees provides: (1) explicit "
                               "confirmation of the Deuteronomy 32:8 national angel "
                               "assignment, (2) the Mastema framework explaining how evil "
                               "spirits operate under divine permission with constrained "
                               "numbers, (3) the expanded Watchers narrative consistent with "
                               "1 Enoch. The Book of Giants provides: (1) named Nephilim "
                               "individuals with documented sins and judgments, (2) dream "
                               "visions connecting Eden typology to Flood judgment, (3) the "
                               "Gilgamesh-Nephilim connection that links Mesopotamian epic "
                               "to biblical narrative. Together these texts demonstrate that "
                               "the divine council was not a fringe idea but the standard "
                               "theological framework of Second Temple Judaism.",

        "sections": [
            {
                "heading": "Jubilees \u2014 The Little Genesis That Reframes Everything",
                "body": "Jubilees retells Genesis through Exodus 14 within a precise "
                        "jubilee cycle framework -- counting history from creation in "
                        "49-year periods. Written approximately 160-150 BC, with Aramaic "
                        "and Hebrew fragments confirmed at Qumran, Jubilees is canonical "
                        "in the Ethiopian Orthodox and Eritrean Orthodox traditions. Its "
                        "content does not contradict the canonical text -- it expands it "
                        "with material that fills gaps the canonical text leaves open. "
                        "The 364-day solar calendar in Jubilees (the same calendar as "
                        "1 Enoch's Astronomy Book) placed the Qumran community on "
                        "different feast days than the Jerusalem temple, which followed "
                        "a lunar calendar. This calendar dispute was one of the primary "
                        "reasons the Qumran community separated from the temple "
                        "establishment. The Watchers narrative in Jubilees is consistent "
                        "with 1 Enoch but adds detail: the role of Mastema, the precise "
                        "number of retained evil spirits, the connection to national "
                        "angel assignments. The fact that Jubilees was found at Qumran "
                        "in more copies than some canonical books tells us something "
                        "crucial about its status in Second Temple Judaism."
            },
            {
                "heading": "Mastema \u2014 The Prosecutor Under Permission",
                "body": "One of Jubilees' most important contributions to the theological "
                        "framework is the figure of Mastema -- the prince of evil spirits "
                        "who operates under divine permission. According to Jubilees "
                        "10:8-9, after the Flood, when the angel Raphael is binding all "
                        "the evil spirits, Mastema petitions Yahweh: let me retain "
                        "one-tenth of them free to operate on earth. God grants this "
                        "request. The implications are profound. First, the number of "
                        "demons currently active is constrained -- nine-tenths of the "
                        "Nephilim spirits are imprisoned. Second, Mastema operates under "
                        "divine permission, not independent authority -- exactly parallel "
                        "to the hassatan in Job 1-2, who must ask permission before "
                        "afflicting Job. Third, the retained spirits serve a function "
                        "under God's sovereign plan -- they test, they tempt, but they "
                        "are leashed. According to Jubilees, Mastema is later identified "
                        "as the one who tried to kill Moses (Jubilees 48:2-3, parallel "
                        "to Exodus 4:24-26) and who hardened Pharaoh's heart. He is a "
                        "prosecutorial figure operating within the boundaries God sets -- "
                        "not an equal and opposite power."
            },
            {
                "heading": "The Book of Giants \u2014 Named Nephilim and Dream Visions",
                "body": "The Book of Giants, preserved in ten Aramaic manuscripts across "
                        "four Qumran caves (Caves 1, 2, 4, 6), is closely related to "
                        "1 Enoch and provides unique material found nowhere else. It "
                        "names eight Nephilim individually: Ohyah and Hahyah (sons of "
                        "Shemihazah), Mahaway (son of Barakel), and others. These are "
                        "not anonymous monsters -- they are named individuals whose "
                        "specific sins and judgments are recorded. The dream visions are "
                        "especially significant. According to the Book of Giants, Ohyah "
                        "dreams of a garden with 200 trees (the 200 Watchers) submerged "
                        "in water and fire -- dual-element judgment that deliberately "
                        "evokes Eden typology. Hahyah dreams of a great tablet lowered "
                        "from heaven -- the heavenly book of life -- immersed in water. "
                        "Three names survive on the tablet: Noah and two sons. The "
                        "Nephilim see their names erased from the heavenly record. The "
                        "irony is sharp: Mahaway, himself a Nephilim, is sent as "
                        "messenger to Enoch to interpret the dreams. A being produced by "
                        "the angelic violation of boundaries must consult the one human "
                        "who crossed in the other direction -- taken to heaven without "
                        "death -- to understand what the divine council has decreed."
            },
            {
                "heading": "The Gilgamesh Connection \u2014 Mesopotamia Meets Genesis",
                "body": "Among the most startling details in the Book of Giants is the "
                        "Aramaic reference in 4Q530 to 'glgmysh' -- identified by "
                        "scholars as Gilgamesh, the hero of the Mesopotamian epic. "
                        "In the Gilgamesh Epic, the hero is described as two-thirds "
                        "divine and one-third human -- the Nephilim pattern of divine-"
                        "human hybrid offspring. He is a king of extraordinary strength "
                        "and stature who seeks immortality after watching his companion "
                        "Enkidu die. In the Book of Giants, Gilgamesh appears not as a "
                        "cultural hero but as one of the post-Flood Nephilim -- part of "
                        "the lineage Genesis 6:4 says existed 'also afterward.' This "
                        "connects directly to Genesis 10:8-9, where Nimrod is called "
                        "'the first gibbor on earth' after the Flood. The Gilgamesh of "
                        "Mesopotamian fame and the Nimrod of Genesis are different cultural "
                        "memories of the same phenomenon: post-Flood figures carrying the "
                        "Nephilim pattern. The pagan mythologies are not fiction -- they "
                        "are corrupted memories of real events involving real beings. "
                        "The Book of Giants provides the interpretive key that connects "
                        "Mesopotamian epic tradition to the biblical narrative. The "
                        "ANE parallels confirm rather than undermine the biblical account."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: 4 EZRA AND BEYOND
    # =========================================================================
    {
        "id": "other-texts-2",
        "ref": "Revelation 21:1-4; 4 Ezra 7:26-44; Isaiah 65:17-25",
        "chapter_num": 2,
        "title": "4 Ezra, and the Wider Second Temple Library",
        "era": "other_texts",
        "type": "chapter",

        "synopsis": "Beyond the Tier 2 texts of 1 Enoch, Jubilees, and the Book of "
                    "Giants, the wider Second Temple literary world preserves traditions "
                    "that illuminate the canonical text from multiple angles. 4 Ezra "
                    "(2 Esdras) provides the most complete non-canonical eschatological "
                    "sequence, including the intermediate state, the messianic reign, "
                    "and the final judgment. The Sibylline Oracles preserve new creation "
                    "imagery consistent with Isaiah 65 and Revelation 21-22. 4 Ezra's "
                    "account of Ezra restoring 94 books -- 24 public and 70 hidden -- "
                    "provides an ancient Jewish framework for understanding why some "
                    "texts are canonical and others are preserved 'for the wise.' These "
                    "are Tier 3 texts: illuminating, consistent with the canon, but not "
                    "carrying the weight of DSS-confirmed and NT-quoted Tier 2 material.",

        "key_verse": {
            "ref": "Revelation 21:1",
            "text": "Then I saw a new heaven and a new earth, for the first heaven "
                    "and the first earth had passed away, and the sea was no more.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05E2\u05D5\u05B9\u05DC\u05B8\u05DD \u05D4\u05B7\u05D1\u05BC\u05B8\u05D0 (\u2018olam habba\u2019)",
                "meaning": "'The age to come' -- the Hebrew eschatological concept of the "
                           "future age that follows the present evil age. 4 Ezra develops "
                           "this concept in extraordinary detail: a temporary messianic "
                           "kingdom followed by universal death, silence, resurrection, "
                           "and final judgment. The two-age framework underlies all NT "
                           "eschatology."
            },
            {
                "term": "\u05E9\u05B0\u05C1\u05D0\u05D5\u05B9\u05DC (She'ol)",
                "meaning": "The abode of the dead in Hebrew cosmology -- not 'hell' in "
                           "the later Christian sense but the holding place of all the "
                           "dead awaiting resurrection. 4 Ezra 7:75-101 describes the "
                           "intermediate state in She'ol with more detail than any "
                           "canonical text: the righteous in restful 'chambers' and "
                           "the wicked in restless torment, both awaiting final judgment."
            },
            {
                "term": "\u05D0\u05B6\u05E8\u05B6\u05E5 \u05D7\u05B2\u05D3\u05B8\u05E9\u05B8\u05C1\u05D4 (\u2019erets chadashah)",
                "meaning": "'New earth' -- the Hebrew concept from Isaiah 65:17 ('I create "
                           "new heavens and a new earth') that Revelation 21:1 picks up. "
                           "4 Ezra and the Sibylline Oracles both describe this renewed "
                           "creation in physical, material terms: trees bearing fruit, "
                           "illness banished, death hidden. Not an ethereal 'heaven' but "
                           "a restored, physical creation."
            },
            {
                "term": "\u05D7\u05B8\u05DB\u05B8\u05DD (chakam)",
                "meaning": "'Wise one.' 4 Ezra 14:46 reserves the 70 hidden books 'for "
                           "the wise among your people, for in them is the spring of "
                           "understanding, the fountain of wisdom.' The Hebrew wisdom "
                           "tradition always distinguished between public instruction "
                           "(Torah) and deeper knowledge available to those who seek it "
                           "(compare Proverbs 25:2: 'It is the glory of God to conceal "
                           "a matter; the glory of kings to search it out')."
            }
        ],

        "ane_backdrop": "Eschatological literature was not unique to Judaism. Egyptian "
                        "funerary texts described post-mortem judgment and the fate of "
                        "the soul in the afterlife. Zoroastrian eschatology included a "
                        "final battle between good and evil, bodily resurrection, and "
                        "a renewed creation -- predating most Jewish apocalyptic by "
                        "centuries and likely influencing it during the Persian period. "
                        "Greek philosophical tradition debated the soul's immortality "
                        "(Plato's Phaedo) and the cyclical renewal of the cosmos (Stoic "
                        "ekpyrosis). What distinguishes the Jewish eschatological tradition "
                        "-- expressed in Daniel, 4 Ezra, and Revelation -- is its linear, "
                        "purposeful framework: history is moving toward a specific divine "
                        "goal, not cycling endlessly. The Messiah arrives, judges the "
                        "living and the dead, and establishes an eternal kingdom on a "
                        "renewed earth. This is not borrowed mythology -- it is the "
                        "logical conclusion of the divine council worldview.",

        "second_temple": [
            {
                "source": "4 Ezra 7:26-44 (Eschatological Sequence)",
                "summary": "According to 4 Ezra, the eschatological sequence is: the "
                           "Messiah is revealed with 'those who are with him'; a temporary "
                           "messianic reign of 400 years; then death -- even the Messiah "
                           "dies; seven days of primordial silence; universal resurrection; "
                           "the Most High appears on the judgment seat; the pit of torment "
                           "and the place of rest are revealed as the two final destinations.",
                "relevance": "This sequence closely parallels Revelation's structure: "
                             "Christ's reign (Rev 20:4-6), followed by final judgment "
                             "(Rev 20:11-15), followed by the new creation (Rev 21-22). "
                             "4 Ezra and Revelation are not copying each other -- they are "
                             "drawing on the same eschatological tradition from different "
                             "vantage points. 4 Ezra illuminates what Revelation compresses."
            },
            {
                "source": "4 Ezra 7:75-101 (The Intermediate State)",
                "summary": "According to 4 Ezra, after death, the souls of the righteous "
                           "enter 'chambers' where they rest, knowing the reward prepared "
                           "but not yet receiving it. The souls of the wicked are in "
                           "restless chambers, tormented by knowledge of what awaits them. "
                           "This is the intermediate state -- after death but before "
                           "resurrection.",
                "relevance": "The canonical text is sparse on the intermediate state. "
                             "4 Ezra fills this gap with the most developed ancient "
                             "Jewish treatment of what happens between death and "
                             "resurrection. It aligns with the canonical framework of "
                             "Sheol as a holding place (not final destination) while "
                             "adding detail the canonical texts do not provide."
            },
            {
                "source": "4 Ezra 14:44-46 (The 94 Books)",
                "summary": "According to 4 Ezra, Ezra was divinely inspired to dictate "
                           "94 books: 24 were made public and 70 were reserved 'for the "
                           "wise among your people.' The 24 public books correspond to "
                           "the standard Hebrew canon. The 70 hidden books represent a "
                           "category of valuable, inspired literature beyond the public "
                           "canon.",
                "relevance": "This is the ancient Jewish precedent for the concept that "
                             "valuable, even divinely inspired literature exists beyond "
                             "the public canon. 'Non-canonical' does not mean 'non-valuable.' "
                             "The 70 hidden books are called 'the spring of understanding, "
                             "the fountain of wisdom, and the river of knowledge.'"
            }
        ],

        "cross_refs": [
            {"ref": "Revelation 21:1-4", "note": "'A new heaven and a new earth... no more death, neither shall there be mourning, nor crying, nor pain anymore' -- the canonical new creation vision that 4 Ezra and the Sibylline Oracles describe in parallel detail.", "type": "nt"},
            {"ref": "Isaiah 65:17-25", "note": "'I create new heavens and a new earth; and the former things shall not be remembered' -- the OT foundation for the new creation hope that 4 Ezra and Revelation both develop.", "type": "ot"},
            {"ref": "Revelation 20:4-6", "note": "The thousand-year reign of Christ with resurrected saints -- parallel to 4 Ezra's temporary messianic kingdom. Same tradition, different temporal details.", "type": "nt"},
            {"ref": "Revelation 20:11-15", "note": "The great white throne judgment -- 4 Ezra 7:33-44 describes the same event: the Most High on the judgment seat, the pit of torment and the place of rest revealed.", "type": "nt"},
            {"ref": "Luke 16:19-31", "note": "The parable of the rich man and Lazarus describes the intermediate state: 'Abraham's bosom' (comfort) and a place of torment, separated by a chasm -- consistent with 4 Ezra's 'chambers.'", "type": "nt"},
            {"ref": "Proverbs 25:2", "note": "'It is the glory of God to conceal a matter; the glory of kings to search it out' -- the wisdom principle behind 4 Ezra's 70 hidden books reserved 'for the wise.'", "type": "ot"},
            {"ref": "4 Ezra 14:44-46", "note": "According to 4 Ezra, Ezra restored 94 books: 24 public (the canon) and 70 hidden ('the fountain of wisdom'). An ancient framework for non-canonical texts as valuable wisdom.", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "The Tier 3 texts illuminate the cosmic scope of the divine "
                               "council narrative's resolution. 4 Ezra's eschatological "
                               "sequence describes the Messiah appearing, the corrupt powers "
                               "being judged, and creation being renewed -- the completion of "
                               "the divine council story arc. The Sibylline Oracles describe "
                               "the new age as one of extraordinary physical fruitfulness "
                               "under the direct rule of the divine king -- the fulfillment "
                               "of Psalm 82:8 where Yahweh inherits all the nations. Even "
                               "these Tier 3 texts assume the divine council framework: the "
                               "present age is under the governance of corrupt spiritual "
                               "powers, the Messiah comes to displace them, and the new age "
                               "is characterized by God's direct rule over all nations -- "
                               "the reversal of Deuteronomy 32:8's original assignment.",

        "sections": [
            {
                "heading": "4 Ezra \u2014 The Eschatology That Parallels Revelation",
                "body": "4 Ezra (also known as 2 Esdras chapters 3-14) is a Jewish "
                        "apocalypse written approximately 100 AD -- roughly contemporary "
                        "with the book of Revelation. It is in the Catholic deuterocanon "
                        "and the Ethiopian Orthodox canon, though not in the Protestant "
                        "or Jewish canon. Its eschatological content represents some of "
                        "the most sophisticated Second Temple Jewish thinking about the "
                        "end times. According to 4 Ezra 7:26-44, the sequence is: the "
                        "Messiah is revealed with those who accompany him, followed by "
                        "a temporary messianic reign, then universal death and seven "
                        "days of primordial silence, then universal resurrection, then "
                        "the Most High appearing on the judgment seat with the pit of "
                        "torment and the place of rest as the two final destinations. "
                        "This is not identical to Revelation's sequence, but it draws "
                        "from the same tradition. 4 Ezra and Revelation are not copying "
                        "each other -- they are two windows into the same eschatological "
                        "framework that Second Temple Judaism and early Christianity shared."
            },
            {
                "heading": "The Intermediate State \u2014 What Happens Between Death and Resurrection",
                "body": "The canonical text is remarkably sparse on what happens between "
                        "individual death and the final resurrection. She'ol in the OT is "
                        "described as a shadowy holding place. Jesus' parable of the rich "
                        "man and Lazarus (Luke 16:19-31) provides imagery of comfort and "
                        "torment separated by a chasm. Paul speaks of 'departing and being "
                        "with Christ' (Philippians 1:23) but does not elaborate. 4 Ezra "
                        "7:75-101 provides the most developed ancient Jewish treatment of "
                        "this question. According to 4 Ezra, after death the souls of the "
                        "righteous enter 'chambers' where they rest in seven orders of "
                        "joy -- they know the reward that awaits them but do not yet "
                        "receive it. The souls of the wicked enter chambers of restless "
                        "torment -- they know what awaits them and cannot escape. Both "
                        "groups await the final resurrection and judgment. This framework "
                        "is consistent with the canonical data: death is not the final "
                        "state, resurrection is coming, and the intermediate period "
                        "involves conscious existence in either rest or distress. 4 Ezra "
                        "fills a gap the canonical text leaves deliberately open."
            },
            {
                "heading": "The 94 Books \u2014 An Ancient Framework for Non-Canonical Literature",
                "body": "One of 4 Ezra's most provocative passages comes near the end "
                        "of the book. According to 4 Ezra 14:44-46, Ezra was divinely "
                        "inspired to dictate 94 books. Of these, 24 were made public -- "
                        "corresponding to the standard Hebrew canon (the same 39 books "
                        "as the Protestant OT, counted differently). But 70 were "
                        "reserved: 'for the wise among your people, for in them is the "
                        "spring of understanding, the fountain of wisdom, and the river "
                        "of knowledge.' This is an ancient Jewish framework that directly "
                        "addresses the non-canonical text question. The 24 public books "
                        "are Tier 1 -- universally accessible, universally authoritative. "
                        "The 70 hidden books are valuable wisdom preserved for those "
                        "willing to seek deeper. They are not dismissed as false or "
                        "dangerous -- they are called 'the fountain of wisdom.' This "
                        "is not an argument for adding books to the canon. It is an "
                        "argument against dismissing non-canonical texts as worthless. "
                        "The ancient Jewish tradition itself recognized a category of "
                        "valuable, even divinely inspired literature that exists beyond "
                        "the public canon. The three-tier framework is not a modern "
                        "invention -- it has ancient roots."
            },
            {
                "heading": "Why Non-Canonical Does Not Mean Non-Valuable",
                "body": "The fundamental error in most discussions of non-canonical texts "
                        "is the assumption that 'not in the canon' means 'not worth "
                        "reading.' This is a category error. The canon is the list of "
                        "texts recognized as bearing supreme divine authority for faith "
                        "and practice. It is not the list of all texts that are true or "
                        "illuminating. Paul quoted pagan poets (Acts 17:28, Titus 1:12). "
                        "Jude quoted 1 Enoch (Jude 14-15). The author of Hebrews quoted "
                        "a text from the LXX absent in the MT (Hebrews 1:6). The NT "
                        "writers demonstrate that truth exists beyond the formal canon. "
                        "The Dead Sea Scrolls proved that the community closest to Jesus "
                        "read 1 Enoch, Jubilees, and the Book of Giants alongside Isaiah "
                        "and Deuteronomy. The Ethiopian Orthodox Church has included "
                        "these texts in their canon for 1,700 years. The question is not "
                        "whether these texts are interesting. The question is what "
                        "relationship they bear to the canonical text -- and the answer, "
                        "demonstrated by the NT writers themselves, is that they provide "
                        "the background knowledge Scripture was written against. "
                        "Recovering them is not adding to Scripture. It is recovering "
                        "what the original audiences already knew."
            }
        ]
    }
]
