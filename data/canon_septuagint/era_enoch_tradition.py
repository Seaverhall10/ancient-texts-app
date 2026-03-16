"""
era_enoch_tradition.py -- 1 Enoch: The Book They Couldn't Kill (Chapters 1-2)

Suppressed by rabbinic authorities at Yavneh. Sidelined by Jerome's Vulgate.
Forgotten in Western Christianity for over a millennium. Rediscovered in
Ethiopia in the 18th century. Confirmed by the Dead Sea Scrolls in the 20th.
Quoted as prophecy in the canonical New Testament.

1 Enoch survived every attempt to bury it -- and the discovery of its Aramaic
fragments at Qumran proved it was never the marginal curiosity its critics
claimed. It was core literature for the community closest to Jesus and his
apostles. Its divine council framework is precisely the worldview the NT
authors assumed their readers understood. This era examines the five books
of 1 Enoch and establishes a principled three-tier framework for reading
non-canonical texts.

Two chapters covering:
  1. The five books of 1 Enoch -- structure, content, DSS status
  2. The three-tier framework for reading non-canonical texts
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: THE FIVE BOOKS OF 1 ENOCH
    # =========================================================================
    {
        "id": "enoch-tradition-1",
        "ref": "Jude 14-15; 1 Enoch 1:9; 1 Enoch 14:18-23; Daniel 7:9-14",
        "chapter_num": 1,
        "title": "The Five Books of 1 Enoch \u2014 Structure and Content",
        "era": "enoch_tradition",
        "type": "chapter",

        "synopsis": "1 Enoch is not a single text but a collection of five originally "
                    "independent works compiled into one. The Book of the Watchers "
                    "(chapters 1-36) is the core, recording the descent of 200 Watchers "
                    "on Mount Hermon and the corruption that followed. The Parables of "
                    "Enoch (37-71) present the most developed pre-Christian Son of Man "
                    "theology. The Book of Astronomy (72-82) establishes the 364-day "
                    "solar calendar. The Book of Dreams (83-90) encodes all of human "
                    "history in symbolic vision. The Epistle of Enoch (91-108) delivers "
                    "ethical teaching and eschatological hope. The Dead Sea Scrolls "
                    "confirmed Aramaic fragments of all sections except the Parables -- "
                    "making 1 Enoch among the most widely attested non-canonical texts "
                    "in ancient Judaism.",

        "key_verse": {
            "ref": "Jude 14-15",
            "text": "It was also about these that Enoch, the seventh from Adam, "
                    "prophesied, saying, \u2018Behold, the Lord comes with ten thousands "
                    "of his holy ones, to execute judgment on all.\u2019",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u12C8\u1295\u1326\u122D (Watcher / \u02BFir)",
                "meaning": "From Aramaic \u02BFir (\u05E2\u05D9\u05E8), meaning 'watcher, wakeful one.' "
                           "Designates the angelic beings who descend on Mount Hermon in "
                           "1 Enoch 6. The term appears in Daniel 4:13, 17, 23 in the "
                           "canonical text: 'a watcher, a holy one, came down from heaven.' "
                           "Daniel uses the same Aramaic word the Enochic tradition uses, "
                           "confirming shared vocabulary between the canonical and "
                           "non-canonical traditions."
            },
            {
                "term": "\u05E9\u05B6\u05C1\u05DE\u05B4\u05D9\u05D7\u05B2\u05D6\u05B8\u05D4 (Shemihazah)",
                "meaning": "'My name has seen' or 'the name sees.' The leader of the 200 "
                           "Watchers who make a pact on Mount Hermon to descend and take "
                           "human wives (1 Enoch 6:3). His name implies that he acts with "
                           "full knowledge of the divine prohibition he is violating -- "
                           "this is not ignorance but rebellion."
            },
            {
                "term": "\u05E2\u05B2\u05D6\u05B0\u05D0\u05D6\u05B5\u05DC (Azazel)",
                "meaning": "The Watcher who teaches forbidden knowledge: metallurgy for "
                           "weapons, cosmetics for seduction, and sorcery (1 Enoch 8:1-2). "
                           "Azazel is bound hand and foot and cast into darkness until the "
                           "Day of Judgment (1 Enoch 10:4-6). He is the Azazel of Leviticus "
                           "16 -- the scapegoat ritual sends Israel's sins to the being "
                           "responsible for introducing that corruption. Without 1 Enoch, "
                           "Leviticus 16 has no explanation for who Azazel is."
            },
            {
                "term": "\u05d1\u05b7\u05bc\u05e8 \u05d0\u05b1\u05e0\u05b8\u05e9\u05c1 (bar enash)",
                "meaning": "'Son of Man' -- the Aramaic title used in the Parables of "
                           "Enoch (1 Enoch 37-71) for a pre-existent, messianic figure "
                           "named before creation and presented before the Ancient of "
                           "Days. The same title Jesus uses for himself throughout the "
                           "Gospels. When Jesus says 'You will see the Son of Man coming "
                           "with the clouds' (Mark 14:62), his audience knew both Daniel "
                           "7 and the Enochic Son of Man tradition."
            },
            {
                "term": "\u05D7\u05B6\u05E8\u05B0\u05DE\u05D5\u05B9\u05DF (Hermon)",
                "meaning": "The mountain where the 200 Watchers descend and make their "
                           "pact (1 Enoch 6:6). The name is connected to the Hebrew "
                           "root cherem (devoted to destruction, banned). According to "
                           "1 Enoch, the Watchers called the mountain 'Hermon because "
                           "they swore and bound themselves by mutual imprecations' -- "
                           "a wordplay on the Hebrew root. Mount Hermon sits at the "
                           "northern boundary of Israel, and in Jesus' time it was the "
                           "location of the pagan sanctuary at Caesarea Philippi."
            }
        ],

        "ane_backdrop": "The Watchers narrative of 1 Enoch has deep parallels in "
                        "Mesopotamian tradition. The apkallu -- seven antediluvian sages "
                        "who brought knowledge from the gods to humans -- mirror the "
                        "Watchers who bring forbidden knowledge. But there is a critical "
                        "difference: in Mesopotamian tradition, the apkallu are benefactors; "
                        "in the Enochic tradition, the Watchers are criminals. The knowledge "
                        "they bring -- weapons, cosmetics, sorcery -- corrupts rather than "
                        "civilizes. The Gilgamesh epic describes a partially divine hero "
                        "(two-thirds god, one-third human) whose superhuman status reflects "
                        "the Nephilim pattern. The Book of Giants from Qumran actually names "
                        "Gilgamesh as one of the post-Flood Nephilim. These are not "
                        "coincidental parallels -- they are corrupted memories of the same "
                        "events, seen through different cultural lenses. 1 Enoch provides "
                        "the theological framework the Mesopotamian traditions lack.",

        "second_temple": [
            {
                "source": "1 Enoch 14:18-23 (Throne Vision)",
                "summary": "According to 1 Enoch, Enoch sees the heavenly throne room: "
                           "walls of crystal, a floor of crystal, a ceiling of stars and "
                           "lightning, cherubim surrounding the throne, rivers of fire "
                           "flowing beneath it, and the Great Glory seated upon a throne "
                           "of crystal with wheels. Ten thousand times ten thousand stood "
                           "before Him, and every word from His mouth was fire.",
                "relevance": "This throne vision uses vocabulary identical to Ezekiel 1, "
                             "Daniel 7, and Revelation 4-5. Four texts spanning 700 years "
                             "describe the same place with the same imagery. 1 Enoch 14 is "
                             "part of the continuous throne-room tradition that the canonical "
                             "texts participate in."
            },
            {
                "source": "1 Enoch 15:8-10 (Origin of Demons)",
                "summary": "According to 1 Enoch, the spirits of the Nephilim giants "
                           "after their death become evil spirits on the earth: 'the "
                           "spirits of the giants shall be like clouds, which shall "
                           "oppress, corrupt, fall, contend, and bruise upon the earth.' "
                           "They are disembodied, wandering, seeking re-embodiment.",
                "relevance": "The canonical text mentions demons constantly but never "
                             "explains their origin. 1 Enoch fills this gap: demons are "
                             "the disembodied spirits of dead Nephilim. This explains "
                             "why demons seek embodiment (Mark 5:12), why they differ "
                             "from imprisoned fallen angels, and why they beg not to be "
                             "sent to the Abyss (Luke 8:31)."
            },
            {
                "source": "1 Enoch 48:2-3 (Pre-existent Son of Man)",
                "summary": "According to 1 Enoch, 'at that hour, that son of man was "
                           "named in the presence of the Lord of Spirits... before the "
                           "sun and the signs were created, before the stars of heaven "
                           "were made, his name was named before the Lord of Spirits.' "
                           "The Son of Man is pre-existent, named before creation.",
                "relevance": "When Jesus says 'You will see the Son of Man coming with "
                             "the clouds' before the Sanhedrin (Mark 14:62), the high "
                             "priest tears his robes. The audience knew both Daniel 7 "
                             "and the Enochic Son of Man tradition. The full weight of "
                             "both traditions landed simultaneously -- Jesus was claiming "
                             "to be the pre-existent divine figure, not merely a human "
                             "messiah."
            }
        ],

        "cross_refs": [
            {"ref": "Jude 14-15", "note": "Direct quotation of 1 Enoch 1:9, identified as 'prophecy.' The canonical endorsement that establishes 1 Enoch's authority as background material.", "type": "nt"},
            {"ref": "Jude 6", "note": "The angels who 'left their proper dwelling' (oiketerion) -- the Watchers of 1 Enoch who abandoned heaven for human women.", "type": "nt"},
            {"ref": "2 Peter 2:4", "note": "'Cast them into Tartarus' -- the imprisonment of the Watchers using uniquely Enochic vocabulary.", "type": "nt"},
            {"ref": "Daniel 4:13, 17", "note": "'A watcher, a holy one, came down from heaven' -- the canonical text uses the same Aramaic term ('ir) that 1 Enoch uses for the angelic Watchers.", "type": "ot"},
            {"ref": "Daniel 7:9-14", "note": "The Ancient of Days, the throne of fire, the Son of Man coming with clouds -- the same throne-room tradition that 1 Enoch 14 describes in parallel detail.", "type": "ot"},
            {"ref": "Ezekiel 1:26-28", "note": "The throne vision with crystal, fire, and the appearance of the Glory of YHWH -- shares vocabulary and imagery with 1 Enoch 14.", "type": "ot"},
            {"ref": "Revelation 4:2-6", "note": "The heavenly throne room with crystal, fire, and twenty-four elders -- the latest canonical expression of the throne tradition that includes 1 Enoch 14.", "type": "nt"},
            {"ref": "Leviticus 16:8-10", "note": "The scapegoat sent 'to Azazel' -- a specific Watcher named in 1 Enoch 8:1-2 and 10:4-6. The Day of Atonement sends Israel's sins back to their originator.", "type": "ot"},
            {"ref": "Mark 14:62", "note": "Jesus' Son of Man declaration before the Sanhedrin -- the audience knew both Daniel 7 and the Enochic Son of Man tradition. The high priest's torn robes were recognition, not confusion.", "type": "nt"},
            {"ref": "1 Enoch 1:9", "note": "The source text for Jude 14-15. Confirmed by Aramaic fragments at Qumran. Part of the Book of the Watchers section.", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "1 Enoch is the single most important non-canonical text for "
                               "understanding the divine council framework. It provides: "
                               "(1) the Watchers narrative -- 200 divine beings who rebel by "
                               "descending on Mount Hermon (Genesis 6:1-4 expanded), (2) the "
                               "origin of demons -- disembodied Nephilim spirits (1 Enoch "
                               "15:8-10), (3) the throne-room vision that parallels Ezekiel 1, "
                               "Daniel 7, and Revelation 4 (1 Enoch 14), (4) the pre-existent "
                               "Son of Man who is named before creation and presented before "
                               "the Ancient of Days (1 Enoch 48), (5) the Azazel identification "
                               "that explains Leviticus 16, and (6) the four-archangel "
                               "structure (Michael, Uriel, Raphael, Gabriel) that the canonical "
                               "text assumes but never fully explains. The NT authors assumed "
                               "their readers knew this material. Recovering it is not adding "
                               "to Scripture -- it is recovering the background knowledge "
                               "Scripture was written against.",

        "sections": [
            {
                "heading": "Book of the Watchers (1 Enoch 1\u201336) \u2014 The Core Narrative",
                "body": "The Book of the Watchers is the foundation of the entire Enochic "
                        "tradition and the source of the passage Jude quotes as prophecy. "
                        "According to 1 Enoch 6, two hundred angelic beings called Watchers "
                        "make a pact on Mount Hermon to descend and take human wives. "
                        "Shemihazah leads them. They produce the Nephilim -- giant hybrid "
                        "offspring who consume the produce of humanity and then devour "
                        "humans themselves. Azazel teaches forbidden knowledge: metallurgy "
                        "for weapons, cosmetics for seduction, sorcery, and astrology. "
                        "The corruption becomes total. Four archangels -- Michael, Uriel, "
                        "Raphael, Gabriel -- bring the cry of the devastated earth before "
                        "God's throne. God commands judgment: Azazel is bound and cast "
                        "into darkness. The Watchers are imprisoned until the final "
                        "judgment. The Flood cleanses the earth. Enoch serves as both "
                        "intercessor (the Watchers ask him to petition God on their "
                        "behalf -- and fail) and cosmic tour guide, traveling through "
                        "the heavens and the corners of the earth. The DSS confirmed "
                        "multiple Aramaic manuscripts of this section, making it among "
                        "the most widely attested texts at Qumran."
            },
            {
                "heading": "Parables of Enoch (1 Enoch 37\u201371) \u2014 The Son of Man",
                "body": "The Parables (also called the Similitudes) contain the most "
                        "theologically developed messianic material in all of Second "
                        "Temple literature. According to 1 Enoch 46, the Son of Man "
                        "appears before the Ancient of Days -- identical to Daniel "
                        "7:13 -- with a face 'full of graciousness, like one of the "
                        "holy angels.' According to 1 Enoch 48:2-3, he was 'named in "
                        "the presence of the Lord of Spirits before the sun and the "
                        "signs were created, before the stars of heaven were made.' "
                        "Pre-existent. Named before creation. Presented before God. "
                        "According to 1 Enoch 62, kings and rulers fall on their faces "
                        "before the Son of Man and plead for mercy -- and are denied. "
                        "This is the tradition Jesus invokes at his trial (Mark 14:62). "
                        "The critical note: the Parables are the ONLY section of 1 "
                        "Enoch not confirmed by the DSS. No Aramaic fragments were found "
                        "at Qumran. This has led scholars to debate whether the Parables "
                        "are pre-Christian or a later composition. The majority view now "
                        "dates them to the late 1st century BC, but the textual "
                        "uncertainty is real and must be acknowledged honestly."
            },
            {
                "heading": "Astronomy, Dreams, and Epistle (1 Enoch 72\u2013108)",
                "body": "The Book of Astronomy (chapters 72-82) presents the 364-day solar "
                        "calendar in meticulous detail. This calendar -- 52 weeks of exactly "
                        "7 days, divided into four seasons of 91 days each -- was used by "
                        "the Qumran community and put them on different feast days than the "
                        "Jerusalem temple, which followed a lunar calendar. The calendar "
                        "dispute was one of the primary reasons the Qumran community "
                        "separated from the temple establishment. DSS Aramaic fragments "
                        "of this section are confirmed. The Book of Dreams (chapters 83-90) "
                        "contains the Animal Apocalypse -- all of human history from Adam "
                        "through the Maccabean period told through animals. Israel are "
                        "sheep; angels are men; predator nations are wild beasts. The "
                        "seventy 'shepherds' appointed over Israel correspond to the "
                        "seventy nations of Genesis 10 and the seventy divine beings of "
                        "Deuteronomy 32:8. DSS fragments confirmed. The Epistle of Enoch "
                        "(chapters 91-108) contains ethical exhortation, woes against the "
                        "wicked, and the Apocalypse of Weeks -- human history schematized "
                        "into ten 'weeks' from Enoch to the new creation. DSS fragments "
                        "confirmed for this section as well."
            },
            {
                "heading": "What 1 Enoch Illuminates in the Canonical Text",
                "body": "Without 1 Enoch, several canonical passages are opaque. "
                        "Leviticus 16 sends the scapegoat 'to Azazel' -- but who is "
                        "Azazel? According to 1 Enoch 8:1-2 and 10:4-6, Azazel is a "
                        "specific Watcher who taught forbidden knowledge and was bound "
                        "in darkness. The scapegoat ritual sends Israel's sins back to "
                        "the being responsible for introducing that corruption -- one "
                        "of the most precise theological moments in the Torah. The "
                        "canonical text mentions demons but never explains their origin. "
                        "According to 1 Enoch 15:8-10, demons are the disembodied "
                        "spirits of dead Nephilim. This explains why they seek "
                        "embodiment (the Gadarene demoniac, Mark 5), why they differ "
                        "from imprisoned fallen angels, and why they beg Jesus not to "
                        "send them to the Abyss (Luke 8:31) -- they know their fathers "
                        "are already imprisoned there. 1 Corinthians 11:10 -- 'a wife "
                        "ought to have authority on her head, because of the angels' -- "
                        "makes immediate sense against the Watcher background: angelic "
                        "beings are present, and the Watcher precedent established the "
                        "danger. The canonical text assumes the Enochic framework. "
                        "Recovering it is hearing what Scripture assumed you already knew."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: THE THREE-TIER FRAMEWORK
    # =========================================================================
    {
        "id": "enoch-tradition-2",
        "ref": "1 John 4:1-2; Jude 14-15; 2 Timothy 3:16",
        "chapter_num": 2,
        "title": "The Three-Tier Framework \u2014 How to Read Non-Canonical Texts",
        "era": "enoch_tradition",
        "type": "chapter",

        "synopsis": "Not all ancient texts are equal -- but the binary of 'canonical' "
                    "versus 'irrelevant' is too blunt. A principled framework requires "
                    "three tiers. Tier 1: Canonical texts (the 66-book Bible) are "
                    "authoritative and primary. Tier 2: DSS-confirmed, NT-quoted texts "
                    "like 1 Enoch are highly valuable background material that the "
                    "canonical writers assumed their audiences knew. Tier 3: Other "
                    "ancient texts (4 Ezra, Sibylline Oracles) illuminate the cultural "
                    "and theological world of Scripture. The governing rule: 'According "
                    "to 1 Enoch...' -- never 'the Bible says' for non-canonical material. "
                    "And always lead with the canonical connection before the Enochic "
                    "content. Let the canonical endorsement carry the weight.",

        "key_verse": {
            "ref": "1 John 4:1",
            "text": "Beloved, do not believe every spirit, but test the spirits to "
                    "see whether they are from God, for many false prophets have gone "
                    "out into the world.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03b4\u03bf\u03ba\u03b9\u03bc\u03ac\u03b6\u03b5\u03c4\u03b5 (dokimazete)",
                "meaning": "'Test, examine, prove.' John's imperative in 1 John 4:1 -- "
                           "believers are commanded to test, not simply accept or reject. "
                           "Applied to non-canonical texts, this means neither uncritical "
                           "acceptance nor blanket dismissal. The test criteria are given: "
                           "does it confess Jesus Christ come in the flesh? Does it align "
                           "with the character of God revealed across the canonical text?"
            },
            {
                "term": "\u03ba\u03ae\u03c1\u03c5\u03b3\u03bc\u03b1 (kerygma)",
                "meaning": "Proclamation, preaching. The core apostolic proclamation about "
                           "Christ. The three-tier framework is built around the kerygma: "
                           "canonical texts proclaim it directly (Tier 1), NT-quoted texts "
                           "provide the assumed background (Tier 2), and other ancient texts "
                           "illuminate the cultural context of the proclamation (Tier 3)."
            },
            {
                "term": "\u05e4\u05b8\u05e8\u05b8\u05e9\u05c1 (parash)",
                "meaning": "To distinguish, separate, interpret. The Hebrew concept of "
                           "making distinctions -- the very first act of creation in "
                           "Genesis 1 is God separating light from darkness. The three-tier "
                           "framework applies the same principle: distinguish between "
                           "levels of authority without erasing the texts that illuminate "
                           "the canonical text."
            }
        ],

        "ane_backdrop": "Ancient Near Eastern libraries and scribal traditions maintained "
                        "their own hierarchies of textual authority. Mesopotamian temples "
                        "had sacred texts used in rituals (highest authority), scribal "
                        "training texts (educational authority), and literary works "
                        "(cultural value). Egyptian temple libraries distinguished between "
                        "sacred funerary texts (the Book of the Dead was required for "
                        "passage to the afterlife) and wisdom literature (valuable but not "
                        "ritually necessary). The concept of tiered textual authority was "
                        "not invented by modern scholars -- it was embedded in the ancient "
                        "world's approach to its own literature. The three-tier framework "
                        "for biblical and extra-biblical texts follows this ancient pattern "
                        "while applying distinctly biblical criteria.",

        "second_temple": [
            {
                "source": "4 Ezra 14:44-46 (the 94 Books)",
                "summary": "According to 4 Ezra, Ezra was divinely inspired to dictate "
                           "94 books: 24 were made public (the standard Hebrew canon) and "
                           "70 were kept for 'the wise among your people, for in them is "
                           "the spring of understanding, the fountain of wisdom, and the "
                           "river of knowledge.'",
                "relevance": "4 Ezra's framework directly anticipates the three-tier model. "
                             "The 24 public books are Tier 1 -- universally accessible "
                             "Scripture. The 70 hidden books are valuable wisdom preserved "
                             "for those willing to seek deeper. The text does not dismiss "
                             "the hidden books -- it calls them 'the fountain of wisdom.' "
                             "This is not a modern apologetic. It is an ancient Jewish "
                             "understanding that authoritative literature extends beyond "
                             "the public canon."
            },
            {
                "source": "Jude's method (Jude 9, 14-15)",
                "summary": "Jude quotes 1 Enoch 1:9 as prophecy (vv. 14-15) and alludes "
                           "to the Assumption of Moses regarding Michael's dispute with "
                           "the devil over Moses' body (v. 9). He uses non-canonical "
                           "material without adding it to the canon -- the same approach "
                           "the three-tier framework takes.",
                "relevance": "Jude models the principled use of non-canonical texts. He "
                             "treats them as authoritative background, not as Scripture "
                             "equal to the Torah or Prophets. He does not explain or "
                             "defend his sources -- he assumes his readers know them. "
                             "This is exactly the Tier 2 relationship: highly valuable, "
                             "assumed as known, but not elevated to canonical status."
            }
        ],

        "cross_refs": [
            {"ref": "1 John 4:1-2", "note": "'Test the spirits to see whether they are from God' -- the biblical command that governs how we evaluate all texts, canonical and non-canonical.", "type": "nt"},
            {"ref": "2 Timothy 3:16", "note": "'All Scripture is breathed out by God' -- establishes the principle of divine origin as the criterion, not human committee vote.", "type": "nt"},
            {"ref": "Jude 14-15", "note": "Jude quotes 1 Enoch as prophecy -- demonstrating that a canonical writer can use non-canonical material authoritatively without canonizing it.", "type": "nt"},
            {"ref": "Jude 9", "note": "Jude alludes to the Assumption of Moses regarding Michael's dispute over Moses' body -- a second non-canonical source used by a canonical writer.", "type": "nt"},
            {"ref": "Acts 17:28", "note": "Paul quotes the pagan poet Aratus ('In him we live and move and have our being') -- demonstrating that truth can be found in non-biblical sources.", "type": "nt"},
            {"ref": "Titus 1:12", "note": "Paul quotes the Cretan poet Epimenides and calls him a 'prophet' -- applying prophetic language to a pagan writer whose statement happens to be true.", "type": "nt"},
            {"ref": "1 Enoch 1:9", "note": "The source text for Jude 14-15. Aramaic fragments confirmed at Qumran. Part of the Book of the Watchers -- the most widely attested section.", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "The three-tier framework is essential for divine council "
                               "theology because the canonical text assumes knowledge that "
                               "only Tier 2 texts provide. Genesis 6:1-4 describes the 'sons "
                               "of God' taking human wives in four verses. 1 Enoch 6-16 "
                               "provides the full narrative. Leviticus 16 sends the scapegoat "
                               "'to Azazel' without explanation. 1 Enoch 8-10 identifies "
                               "Azazel and explains the ritual's logic. The canonical text "
                               "mentions demons without explaining their origin. 1 Enoch "
                               "15:8-10 provides the answer. Without Tier 2 texts, the divine "
                               "council framework has gaps that the canonical text itself "
                               "never fills. This is not because Scripture is insufficient -- "
                               "it is because Scripture was written for an audience that already "
                               "knew this material.",

        "sections": [
            {
                "heading": "Tier 1 \u2014 The Canonical Text (Always Primary)",
                "body": "The 66-book biblical canon is always the primary authority. "
                        "When Scripture speaks, the discussion begins and ends there. "
                        "'All Scripture is breathed out by God' (2 Timothy 3:16) -- the "
                        "canonical texts derive their authority from divine origin, not "
                        "from human selection. No non-canonical text can override, "
                        "contradict, or supplement the canonical text in a way that "
                        "changes its meaning. Evidence classification: [A] direct "
                        "Scripture. Language convention: 'The Bible says...' or 'The "
                        "text says...' This tier is non-negotiable and forms the "
                        "foundation on which everything else rests. The Tier 1 "
                        "principle also means that when evaluating Tier 2 and Tier 3 "
                        "texts, the canonical text is the measuring rod. If a non-canonical "
                        "text contradicts the canon, the canon wins. If a non-canonical "
                        "text illuminates the canon without contradiction, it is valuable. "
                        "The test of 1 John 4:1-2 applies: does it confess Yahweh as "
                        "sovereign? Does it present the Messiah? Is it consistent with "
                        "the character of God? Does it lead toward God or away from Him? "
                        "These are the criteria -- not institutional tradition, not "
                        "historical accident, not political convenience."
            },
            {
                "heading": "Tier 2 \u2014 DSS-Confirmed, NT-Quoted (Highly Valuable)",
                "body": "Tier 2 texts are non-canonical texts that meet two crucial "
                        "criteria: they are confirmed by the Dead Sea Scrolls (proving "
                        "they were authoritative in the Second Temple period), and they "
                        "are quoted or drawn upon by canonical NT writers (proving the "
                        "apostles treated them as authoritative background). The primary "
                        "Tier 2 texts are: 1 Enoch (Book of the Watchers especially -- "
                        "quoted by Jude, drawn on by Peter, confirmed at Qumran in "
                        "multiple copies), Jubilees (confirmed at Qumran in multiple "
                        "copies, in the Ethiopian canon, fills gaps in Genesis-Exodus), "
                        "and the Book of Giants (confirmed at Qumran in ten manuscripts "
                        "across four caves, part of the Enochic tradition). Evidence "
                        "classification: [C] ancient parallels, but highest confidence "
                        "within that tier. Language convention: 'According to 1 Enoch...' "
                        "or 'According to Jubilees...' -- never 'the Bible says.' These "
                        "texts are not Scripture. They are the background knowledge that "
                        "Scripture was written against -- and recovering them is essential "
                        "for understanding what the canonical writers meant."
            },
            {
                "heading": "Tier 3 \u2014 Ancient Illumination (Valuable Context)",
                "body": "Tier 3 texts are ancient writings that illuminate the theological "
                        "and cultural world of Scripture without meeting the full Tier 2 "
                        "criteria. They may not be confirmed at Qumran, or may not be "
                        "directly quoted in the NT, but they preserve traditions that "
                        "help reconstruct the worldview of the biblical authors and their "
                        "audiences. Primary Tier 3 texts include: 4 Ezra (2 Esdras) -- a "
                        "Jewish apocalypse from c. 100 AD with the most developed non-"
                        "canonical eschatological sequence and intermediate state theology. "
                        "The Sibylline Oracles -- Jewish prophetic poetry in Greek that "
                        "preserves new creation imagery consistent with Isaiah 65 and "
                        "Revelation 21-22. The Assumption of Moses -- alluded to by "
                        "Jude 9 regarding Michael's dispute over Moses' body. The Life "
                        "of Adam and Eve -- expanded Eden narratives. Evidence "
                        "classification: [C] ancient parallels, lower confidence. Language "
                        "convention: 'The tradition preserved in 4 Ezra suggests...' or "
                        "'An ancient Jewish text describes...' Tier 3 texts are never "
                        "treated as authoritative in the same sense as Tier 1 or Tier 2 -- "
                        "but dismissing them is as much an error as elevating them."
            },
            {
                "heading": "The Governing Principle \u2014 How the NT Writers Did It",
                "body": "The three-tier framework is not a modern invention. It is the "
                        "method the NT writers themselves practiced. Jude quoted 1 Enoch "
                        "without canonizing it. Peter drew on the Watchers tradition "
                        "without adding 1 Enoch to the Torah. The author of Hebrews "
                        "quoted a line from LXX Deuteronomy 32:43 that the MT does not "
                        "contain -- using a textual tradition broader than the standard "
                        "Hebrew Bible. Paul quoted the pagan poet Aratus in Acts 17:28 "
                        "and called Epimenides a 'prophet' in Titus 1:12 -- finding "
                        "truth in non-biblical sources without canonizing them. These "
                        "writers used available traditions to illuminate the canonical "
                        "text. They did not add to Scripture. They did not treat non-"
                        "canonical material as equal to the Torah. But they used it, "
                        "assumed their readers knew it, and built arguments on shared "
                        "knowledge. That is exactly what the three-tier framework does. "
                        "It recovers the background knowledge Scripture was written "
                        "against. The test of 1 John 4:1 applies at every tier: test "
                        "the spirits. And when you test 1 Enoch honestly -- does it "
                        "confess Yahweh? Does it present the Messiah? Does it lead "
                        "toward God? -- the answer at every point is yes."
            }
        ]
    }
]
