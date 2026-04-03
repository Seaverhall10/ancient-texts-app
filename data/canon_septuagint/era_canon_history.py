"""
era_canon_history.py -- How We Got Our Bible (Chapters 1-2)

The 66-book Protestant canon was not handed down from heaven on golden
plates. It was a historical process involving human decisions, theological
debates, political pressures, and in some cases motivated reasoning. That
statement is not an attack on Scripture -- it is taking history seriously.

Understanding how the canon was formed does not undermine its authority.
It actually strengthens it. The books that made it into the canon did so
because they bore the marks of divine origin across centuries of use in
communities of faith. And the books that fell out -- 1 Enoch, Jubilees,
the Book of Giants -- fell out for reasons that had far more to do with
politics and institutional control than with theology.

Two chapters covering:
  1. Canon as historical process -- Jerome, Trent, and the Ethiopian tradition
  2. What fell out and why -- 1 Enoch, Jubilees, and the politics of exclusion
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: CANON AS HISTORICAL PROCESS
    # =========================================================================
    {
        "id": "canon-history-1",
        "ref": "2 Timothy 3:16; Luke 24:44; Jude 14-15",
        "chapter_num": 1,
        "title": "Canon as Historical Process \u2014 From Scrolls to Your Bible",
        "era": "canon_history",
        "type": "chapter",

        "synopsis": "The biblical canon -- the list of books recognized as Scripture -- "
                    "was not decided by a single council, a single vote, or a single "
                    "emperor. It emerged through centuries of use, debate, and recognition "
                    "across scattered communities of faith. The Old Testament canon was "
                    "shaped by the Jewish council at Yavneh (c. 90 AD), Jerome's Vulgate "
                    "translation (382-405 AD), and the Council of Trent (1546 AD). The "
                    "New Testament canon was substantially settled by the mid-2nd century "
                    "through organic church usage, with the first complete list matching "
                    "the modern NT appearing in Athanasius's 39th Festal Letter in 367 AD. "
                    "Meanwhile, the Ethiopian Orthodox Church -- one of the oldest "
                    "continuous Christian traditions -- has included 1 Enoch and Jubilees "
                    "in their 81-book canon for 1,700 years.",

        "key_verse": {
            "ref": "2 Timothy 3:16",
            "text": "All Scripture is breathed out by God and profitable for teaching, "
                    "for reproof, for correction, and for training in righteousness.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03b8\u03b5\u03cc\u03c0\u03bd\u03b5\u03c5\u03c3\u03c4\u03bf\u03c2 (theopneustos)",
                "meaning": "'God-breathed' -- Paul's term in 2 Timothy 3:16 for the nature "
                           "of Scripture. The word describes the origin of the text, not a "
                           "human process of selecting texts. The canon question is: which "
                           "texts bear this character? Paul's statement establishes the "
                           "principle, but does not provide the list."
            },
            {
                "term": "Hebraica veritas",
                "meaning": "Latin: 'Hebrew truth.' Jerome's phrase for his conviction that "
                           "the Old Testament should be translated from the Hebrew text "
                           "rather than the LXX. This led him to follow the shorter Jamnia "
                           "canon (excluding 1 Enoch, Jubilees, and the deuterocanonical "
                           "books), creating the framework that Protestantism would later "
                           "adopt. Ironically, Jerome's 'Hebrew truth' was the MT tradition "
                           "that the DSS would later prove was not always the oldest reading."
            },
            {
                "term": "\u05e7\u05b8\u05e0\u05d5\u05b9\u05df (qanon) / \u03ba\u03b1\u03bd\u03ce\u03bd (kanon)",
                "meaning": "Reed, measuring rod, standard. The word 'canon' derives from "
                           "the Greek kanon (ultimately from Hebrew qaneh), meaning a "
                           "standard of measurement. Applied to Scripture, it designates "
                           "the list of books recognized as measuring up to the standard "
                           "of divine authority. The metaphor is revealing: the books are "
                           "measured against a standard, not voted into existence."
            },
            {
                "term": "\u12a8\u1290\u1291 (Henok)",
                "meaning": "Enoch in Ge'ez (Ethiopic). The Ethiopian Orthodox Church calls "
                           "the book 'Mets'hafe Henok' (Book of Enoch) and has included "
                           "it in their biblical canon continuously since the 4th century. "
                           "Their canon of 81 books represents an unbroken Christian "
                           "tradition independent of both Roman and Reformation decisions."
            }
        ],

        "ane_backdrop": "Canon formation was not unique to Judaism and Christianity. "
                        "Ancient civilizations routinely maintained lists of authoritative "
                        "texts. Egyptian temple libraries had prescribed lists of sacred "
                        "writings. Mesopotamian scribal schools had standard collections "
                        "of literary texts for training and reference. The Babylonian "
                        "Epic of Gilgamesh itself went through a 'canonical' process -- "
                        "the Standard Babylonian version compiled by Sin-leqi-unninni "
                        "became the authoritative edition. What distinguishes the biblical "
                        "canon process is the theological claim: these are not merely "
                        "important human writings but 'God-breathed' (theopneustos) "
                        "texts that derive their authority from divine origin rather "
                        "than human selection. The human process of recognizing them did "
                        "not create their authority -- it identified authority that was "
                        "already present.",

        "second_temple": [
            {
                "source": "Athanasius, 39th Festal Letter (367 AD)",
                "summary": "The first document listing exactly the 27 New Testament books "
                           "as canonical. Athanasius, Bishop of Alexandria, also specified "
                           "the Old Testament canon but included the deuterocanonical books "
                           "as suitable for instruction, creating a distinction between "
                           "'canonical' and 'read in churches' that would shape later debate.",
                "relevance": "Athanasius's list demonstrates that the NT canon was not "
                             "settled until over 300 years after the last book was written. "
                             "The process was organic, not dictated. Even after Athanasius, "
                             "debate continued -- Revelation, Hebrews, and Jude were "
                             "questioned in some circles for centuries."
            },
            {
                "source": "Council of Trent (1546 AD)",
                "summary": "The Roman Catholic council that formally and dogmatically "
                           "defined the Catholic canon, including the deuterocanonical "
                           "books (Tobit, Judith, Wisdom, Sirach, Baruch, 1-2 Maccabees). "
                           "This was a direct response to the Protestant Reformation, which "
                           "had gone back to the shorter Hebrew canon.",
                "relevance": "Both the Protestant and Catholic canons as currently defined "
                             "were shaped by the 16th-century dispute between them. Neither "
                             "is a pure transmission from the apostolic era. Trent made the "
                             "Catholic canon legally binding; the Reformation enshrined "
                             "Jerome's shorter Hebrew canon in Protestant Bibles."
            }
        ],

        "cross_refs": [
            {"ref": "2 Timothy 3:16", "note": "'All Scripture is breathed out by God' -- establishes the divine origin of Scripture but does not specify which books constitute Scripture.", "type": "nt"},
            {"ref": "Luke 24:44", "note": "Jesus refers to 'the Law of Moses and the Prophets and the Psalms' -- a tripartite division already recognized. But the boundaries of each section were still debated.", "type": "nt"},
            {"ref": "2 Peter 3:15-16", "note": "Peter recognizes Paul's letters as 'Scripture' during the apostolic period -- canon recognition was already happening before any council formalized it.", "type": "nt"},
            {"ref": "Jude 3", "note": "'The faith once for all delivered to the saints' -- implies a fixed deposit of authoritative teaching that the community is responsible to guard.", "type": "nt"},
            {"ref": "Jude 14-15", "note": "Jude quotes 1 Enoch 1:9 as 'prophecy' and identifies Enoch by name. A canonical NT writer treats a non-canonical text as prophetic -- demonstrating that canon boundaries were not drawn where modern Protestants assume.", "type": "nt"},
            {"ref": "Acts 8:26-40", "note": "The Ethiopian eunuch baptized by Philip -- the origin tradition of the Ethiopian Orthodox Church, which has maintained the broadest Christian canon (81 books) for 1,700 years.", "type": "nt"}
        ],

        "divine_council_note": "The canon formation process has direct implications for "
                               "divine council theology. The texts most explicitly teaching "
                               "the divine council framework -- 1 Enoch, Jubilees, the Book "
                               "of Giants -- were precisely the texts excluded from the "
                               "Protestant canon. This is not coincidence. As post-temple "
                               "Judaism moved away from the divine council worldview (partly "
                               "in reaction to Christian Christological claims), and as Western "
                               "Christianity absorbed Platonic philosophy that replaced the "
                               "divine council with abstract monotheism, the texts that most "
                               "clearly articulated the council framework became uncomfortable. "
                               "The Ethiopian Orthodox Church, which never adopted either the "
                               "Platonic framework or Jerome's canon decisions, preserved "
                               "these texts without interruption.",

        "sections": [
            {
                "heading": "The Old Testament Canon \u2014 From Torah to Yavneh",
                "body": "The Torah -- the five books of Moses -- was the first section "
                        "of Scripture to achieve near-universal acceptance. By the time "
                        "of the Samaritans' split (c. 4th century BC), the Torah was "
                        "already authoritative for all Israelite communities. The Prophets "
                        "and Writings were accepted progressively over centuries, with "
                        "debate continuing into the 1st century AD about books like "
                        "Ecclesiastes, Song of Solomon, and Esther. After the destruction "
                        "of the Second Temple in 70 AD, the Jewish council at Yavneh "
                        "(Jamnia, c. 90 AD) moved to standardize the Hebrew canon. Their "
                        "criteria were partly linguistic (must be in Hebrew, not Greek), "
                        "partly temporal (must not post-date Ezra), and partly motivated "
                        "by the need to distinguish Jewish Scripture from texts being "
                        "adopted by the growing Christian movement. This excluded 1 Enoch, "
                        "Jubilees, and other texts that the Qumran community had treated as "
                        "authoritative. The Yavneh canon became the basis for the Protestant "
                        "Old Testament 1,500 years later. But between Yavneh and the "
                        "Reformation, most Christians -- including Augustine, the councils "
                        "of Hippo and Carthage, and the entire Eastern Orthodox tradition "
                        "-- used a broader OT canon based on the LXX."
            },
            {
                "heading": "Jerome\u2019s Choice \u2014 Hebrew Over Greek",
                "body": "In 382 AD, Pope Damasus I commissioned the scholar Jerome to "
                        "produce a standard Latin Bible. Jerome's decision at this moment "
                        "would shape Western Christianity for over a thousand years. "
                        "Against the prevailing practice of the church -- which had used "
                        "the LXX-based Old Testament since the apostolic era -- Jerome "
                        "chose to translate from the Hebrew. He called this Hebraica "
                        "veritas: 'Hebrew truth.' His reasoning was that the original "
                        "language must be primary. But Jerome's 'original Hebrew' was "
                        "the post-Yavneh text tradition -- a shorter canon with readings "
                        "that had already been altered in key divine council passages. "
                        "Jerome's translation choices compounded the problem. He rendered "
                        "the masculine pronoun in Genesis 3:15 as feminine (ipsa -- 'she'). "
                        "He systematically flattened elohim vocabulary, translating divine "
                        "council language as singular Deus. He removed the council framework "
                        "from Latin Christianity. His Vulgate became the dominant Bible in "
                        "the West for over a millennium, and when the Protestant Reformers "
                        "chose the Hebrew canon over the LXX canon, they were unwittingly "
                        "following Jerome's earlier decision."
            },
            {
                "heading": "Trent, Luther, and the Modern Canon",
                "body": "Martin Luther, in his German Bible translation (1534), followed "
                        "Jerome's canon of the Hebrew-only books for the OT, relegating "
                        "the deuterocanonical books to an appendix labeled 'useful and good "
                        "to read but not equal to Holy Scripture.' He also questioned "
                        "Hebrews, James, Jude, and Revelation, placing them at the end "
                        "of his NT in a separate section. The Council of Trent (1546), "
                        "convened in direct response to the Reformation, formally and "
                        "dogmatically defined the Catholic canon for the first time, "
                        "including the deuterocanonical books as fully canonical. Both "
                        "the Protestant and Catholic canons as they exist today were "
                        "shaped by the 16th-century conflict between them. The Protestant "
                        "canon follows the Yavneh/Jamnia Hebrew tradition mediated through "
                        "Jerome. The Catholic canon includes the broader LXX-based "
                        "tradition ratified against Protestant objections. Neither "
                        "represents a pure, unmediated transmission from the apostolic "
                        "era. The canon was a historical process -- not an oracle. That "
                        "does not make it less authoritative, but it demands honesty about "
                        "how we got it."
            },
            {
                "heading": "The Ethiopian Orthodox Tradition \u2014 81 Books",
                "body": "One of the oldest continuous Christian traditions in the world "
                        "traces its roots to the Ethiopian eunuch baptized by Philip in "
                        "Acts 8. The Ethiopian Orthodox Tewahedo Church never accepted "
                        "Jerome's canon decisions or Trent's authority. Their canon of 81 "
                        "books includes 1 Enoch (Mets'hafe Henok), Jubilees (Kufale), and "
                        "other texts that Western Christianity excluded. They did not add "
                        "these books as an afterthought -- they simply never removed them. "
                        "While the Western church debated what to include and exclude, "
                        "Ethiopia quietly preserved a broader canon that maintained the "
                        "Watchers tradition, the divine council framework, and the solar "
                        "calendar theology of Jubilees without interruption. The existence "
                        "of the Ethiopian canon does not prove that 1 Enoch is canonical in "
                        "the same sense as Isaiah. But it demonstrates that the exclusion "
                        "of 1 Enoch from the Western canon was a particular historical "
                        "decision, not a universal Christian judgment. An unbroken Christian "
                        "tradition going back to the apostolic era considers 1 Enoch "
                        "Scripture. That fact should give pause to anyone who dismisses "
                        "it as 'non-biblical.'"
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: WHAT FELL OUT AND WHY
    # =========================================================================
    {
        "id": "canon-history-2",
        "ref": "Jude 14-15; 1 Enoch 1:9; 2 Peter 2:4",
        "chapter_num": 2,
        "title": "What Fell Out and Why \u2014 The Politics of Exclusion",
        "era": "canon_history",
        "type": "chapter",

        "synopsis": "Several texts that the Qumran community treated as authoritative, "
                    "that the NT authors quoted or drew upon, and that the Ethiopian "
                    "Orthodox Church has preserved for 1,700 years were excluded from "
                    "the Protestant and Catholic canons. The reasons were not primarily "
                    "theological. 1 Enoch was quoted by Jude as prophecy, confirmed by "
                    "the DSS, and passes every theological test applied to canonical "
                    "texts. Jubilees was found in more copies at Qumran than some "
                    "canonical books. The Book of Giants provides essential background "
                    "for understanding the Nephilim. These texts failed politics, "
                    "not theology.",

        "key_verse": {
            "ref": "Jude 14-15",
            "text": "It was also about these that Enoch, the seventh from Adam, "
                    "prophesied, saying, \u2018Behold, the Lord comes with ten thousands "
                    "of his holy ones, to execute judgment on all.\u2019",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03c0\u03c1\u03bf\u03b5\u03c6\u03ae\u03c4\u03b5\u03c5\u03c3\u03b5\u03bd (epropheteusen)",
                "meaning": "'Prophesied' -- the Greek verb Jude uses to describe Enoch's "
                           "words from 1 Enoch 1:9. This is the standard word for prophetic "
                           "utterance in the NT. Jude does not say Enoch 'wrote,' 'suggested,' "
                           "or 'guessed.' He says Enoch prophesied. Prophecy in the biblical "
                           "framework means a human speaking the words of God."
            },
            {
                "term": "\u05d8\u05b7\u05e8\u05d8\u05b0\u05e8\u05d5\u05b9\u05e1 (Tartaros)",
                "meaning": "The Greek mythological underworld prison for rebellious divine "
                           "beings. Peter uses this word -- nowhere else in the NT -- in "
                           "2 Peter 2:4: God 'cast them into Tartarus.' Peter reaches for "
                           "a Greek term his readers would recognize to describe the real "
                           "event behind the mythology: the imprisonment of the Watchers "
                           "that 1 Enoch records in detail."
            },
            {
                "term": "\u05d0\u05b2\u05e4\u05d5\u05b9\u05e7\u05b0\u05e8\u05d9\u05e4\u05b4\u05d9 (apokryphi)",
                "meaning": "'Hidden, concealed.' The term 'apocrypha' originally meant "
                           "'hidden writings' -- not 'false writings.' 4 Ezra 14:44-46 "
                           "describes Ezra restoring 94 books: 24 public (the Hebrew canon) "
                           "and 70 hidden (reserved for the wise). The category of 'hidden "
                           "but valuable' is ancient -- not a modern invention."
            }
        ],

        "ane_backdrop": "The exclusion of certain texts from the canon was not a uniquely "
                        "Jewish or Christian phenomenon. Ancient scribal cultures routinely "
                        "made decisions about which texts to preserve, copy, and promote. "
                        "Mesopotamian libraries had standard texts and secondary texts. "
                        "Egyptian temple schools had prescribed curricula and supplementary "
                        "reading. The process always involved human judgment about value, "
                        "relevance, and authority. What makes the biblical canon process "
                        "distinctive is the theological claim undergirding it: these "
                        "decisions were guided by divine providence even though they were "
                        "made by human beings. The question is whether that providential "
                        "guidance extended only to inclusion (protecting the canonical "
                        "texts) or also to exclusion (removing genuinely valuable texts). "
                        "The evidence suggests the latter: the excluded texts preserve "
                        "theological content that the canonical writers assumed their "
                        "readers knew.",

        "second_temple": [
            {
                "source": "4 Ezra 14:44-46",
                "summary": "According to 4 Ezra, Ezra was inspired to dictate 94 books: "
                           "24 were made public (the Hebrew canon) and 70 were reserved "
                           "'for the wise among your people.' The text explicitly envisions "
                           "a category of valuable, inspired writings that are not part of "
                           "the public canon.",
                "relevance": "4 Ezra's framework -- public canon plus hidden treasure -- "
                             "provides a Second Temple precedent for treating non-canonical "
                             "texts as valuable without equating them with the public "
                             "scriptures. This is essentially the three-tier framework: "
                             "canonical, highly authoritative, illuminating."
            },
            {
                "source": "Tertullian, On the Apparel of Women 1.3 (c. 200 AD)",
                "summary": "Tertullian acknowledges that 1 Enoch is not universally "
                           "accepted in the canon but defends its value: it was preserved "
                           "through the Flood (either by Noah or by divine restoration), "
                           "and Jude's quotation in the NT gives it prophetic status.",
                "relevance": "Even in the early church, 1 Enoch occupied a unique position: "
                             "not fully canonical for all communities, but defended by "
                             "significant church fathers as prophetic and valuable. Its "
                             "exclusion was not unanimous or swift."
            }
        ],

        "cross_refs": [
            {"ref": "Jude 14-15", "note": "Direct quotation of 1 Enoch 1:9, called 'prophecy.' Enoch identified by name as 'the seventh from Adam.' A canonical NT writer treats 1 Enoch as prophetic speech.", "type": "nt"},
            {"ref": "Jude 6", "note": "'Angels who did not stay within their own position of authority but left their proper dwelling' -- the Watchers narrative from 1 Enoch, assumed as known background.", "type": "nt"},
            {"ref": "2 Peter 2:4", "note": "'God cast them into Tartarus' -- tartaroo appears only here in the entire NT. Peter uses the Greek mythological prison for divine rebels to describe the Watchers' imprisonment.", "type": "nt"},
            {"ref": "1 Enoch 1:9", "note": "The source text Jude quotes: 'Behold, he comes with ten thousand of his holy ones, to execute judgment upon all.' Aramaic fragments confirmed at Qumran.", "type": "pseudepigrapha"},
            {"ref": "Hebrews 11:5", "note": "'By faith Enoch was taken up so that he should not see death' -- the canonical affirmation of the Enoch tradition, consistent with 1 Enoch's heavenly journey narrative.", "type": "nt"},
            {"ref": "1 Corinthians 11:10", "note": "'A wife ought to have a symbol of authority on her head, because of the angels' -- makes immediate sense against the Watcher tradition: angelic beings are present and the Watcher precedent established the danger.", "type": "nt"}
        ],

        "divine_council_note": "The texts excluded from the Western canon are precisely the "
                               "texts that most explicitly teach the divine council framework. "
                               "1 Enoch provides the Watchers narrative, the origin of demons, "
                               "and the throne-room vision. Jubilees provides the Mastema "
                               "framework and the national angel assignments. The Book of "
                               "Giants names the Nephilim and records their judgment. As "
                               "Western Christianity moved toward the Platonic-influenced "
                               "framework of abstract monotheism -- in which spiritual beings "
                               "are either metaphors or minor footnotes -- the texts that "
                               "described a robust, populated heavenly realm became "
                               "theologically inconvenient. Their exclusion from the canon "
                               "was not accidental. Recovering these texts is essential for "
                               "recovering the worldview the biblical authors actually held.",

        "sections": [
            {
                "heading": "1 Enoch \u2014 The Case for Its Authority",
                "body": "No non-canonical text has stronger credentials than 1 Enoch. "
                        "Jude 14-15 directly quotes 1 Enoch 1:9 and calls it 'prophecy.' "
                        "The Greek word epropheteusen is the standard term for prophetic "
                        "speech -- Jude treats Enoch's words as the words of a prophet "
                        "speaking on behalf of God. Jude does not explain who Enoch is "
                        "or what book he is quoting -- he assumes his readers know. "
                        "2 Peter 2:4 uses the uniquely Enochic term 'Tartarus' for the "
                        "prison of the fallen Watchers. Hebrews 11:5 affirms the Enoch "
                        "tradition. The Dead Sea Scrolls preserved multiple copies in "
                        "Aramaic, confirming it was core literature at Qumran. The "
                        "Ethiopian Orthodox Church has included it in their canon for "
                        "1,700 years without interruption. When you apply the standard "
                        "tests of canonicity -- does it confess Yahweh as sovereign? "
                        "Does it present the Messiah? Is it consistent with the character "
                        "of God? Does it lead toward God or away from Him? -- 1 Enoch "
                        "passes on every count. It failed a political test at Yavneh "
                        "(associated with Christians) and an institutional test in the "
                        "Western church (its divine council framework was incompatible "
                        "with post-Platonic theology). It never failed a theological test."
            },
            {
                "heading": "Jubilees and the Book of Giants \u2014 The Qumran Evidence",
                "body": "Jubilees (the 'Little Genesis') was found in more copies at "
                        "Qumran than several canonical books. The DSS community treated "
                        "it as authoritative -- their solar calendar, their festival "
                        "schedule, and their theological framework drew heavily from "
                        "Jubilees. The Ethiopian Orthodox and Eritrean Orthodox churches "
                        "include it in their canon. Its retelling of Genesis through "
                        "Exodus 14 provides the Mastema framework (the figure who "
                        "commands the remaining free evil spirits after the Flood), "
                        "explicit national angel assignments (confirming Deuteronomy "
                        "32:8), and a precise jubilee-cycle calendar. The Book of "
                        "Giants was found in ten manuscripts across four Qumran caves. "
                        "It names the Nephilim individually -- Ohyah, Hahyah, Mahaway -- "
                        "and records their dream visions of coming judgment. It is part "
                        "of the Enochic tradition that Jude and Peter drew upon. Neither "
                        "Jubilees nor the Book of Giants contradicts the canonical text. "
                        "Both illuminate it. Their presence at Qumran in multiple copies "
                        "demonstrates they were not fringe documents but core library "
                        "holdings for the most devout Jewish community of the Second "
                        "Temple period."
            },
            {
                "heading": "Why They Were Excluded \u2014 Politics, Not Theology",
                "body": "The exclusion of 1 Enoch, Jubilees, and the Book of Giants from "
                        "the Western canon was driven by identifiable historical forces, "
                        "not theological evaluation. At Yavneh (c. 90 AD), the rabbinic "
                        "council excluded texts that were not in Hebrew (1 Enoch's "
                        "surviving complete text was in Ge'ez), that were associated "
                        "with Christian communities, or that post-dated Ezra. The "
                        "Aramaic fragments from Qumran prove 1 Enoch predates many "
                        "canonical books, but the rabbis at Yavneh did not have the DSS. "
                        "Their decision was based on the manuscripts available to them "
                        "and the institutional pressures they faced. In the Western "
                        "church, Jerome's preference for the Hebrew canon over the LXX "
                        "canon meant that texts not in the Yavneh list were demoted. "
                        "By the 4th century, the divine council framework of 1 Enoch was "
                        "increasingly out of step with the Platonic-influenced theology "
                        "that had come to dominate Alexandria and Rome. A text describing "
                        "divine beings who marry human women, produce hybrid offspring, "
                        "and corrupt human civilization was theologically embarrassing "
                        "to a church that had redefined spiritual beings as disembodied "
                        "abstractions. The exclusion protected institutional theology, "
                        "not biblical integrity."
            },
            {
                "heading": "Recognition vs. Creation \u2014 An Honest Framework",
                "body": "The ekklesia did not create the canon -- it recognized it. The "
                        "books of the Bible were authoritative from the moment of their "
                        "composition because they were 'breathed out by God' (2 Timothy "
                        "3:16). The human process of canon formation was the messy, "
                        "centuries-long work of recognizing what God had already done. "
                        "But honesty demands a follow-up question: if the process was "
                        "one of human recognition, is it possible the humans got some "
                        "decisions wrong? The Ethiopian Orthodox answer is yes -- they "
                        "recognized 1 Enoch and Jubilees as canonical, and they have "
                        "the older tradition. Luther questioned Hebrews, James, Jude, "
                        "and Revelation -- suggesting even the NT list was not self-"
                        "evident. The solution is not to abandon the canon or add books "
                        "arbitrarily. It is to develop a principled framework: canonical "
                        "texts are authoritative (Tier 1). DSS-confirmed, NT-quoted "
                        "texts like 1 Enoch are highly valuable (Tier 2). Other ancient "
                        "texts illuminate the world of Scripture (Tier 3). This framework "
                        "takes both the canon and its history seriously -- refusing to "
                        "treat the 66-book list as if it fell from heaven while also "
                        "maintaining the distinction between Scripture and other writings."
            }
        ]
    }
]
