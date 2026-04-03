"""
era_lxx_mt.py -- Two Text Traditions: LXX vs Masoretic (Chapters 1-2)

Most English-speaking Christians assume their Old Testament is a direct
translation from "the original Hebrew." The reality is more complex and
more interesting. The Septuagint -- the Greek translation made by Jewish
scholars in Alexandria between 250-150 BC -- was the Bible Jesus' followers
actually used. When Paul quotes the Old Testament in Romans, he quotes the
LXX. When the author of Hebrews builds his argument in chapter 1, he quotes
a line from Deuteronomy 32:43 that exists only in the LXX -- not in the
Masoretic Text that underlies most Protestant Bibles.

The Masoretic Text, standardized by Jewish scribes between 600-1000 AD, is
careful and largely faithful work. But it was finalized centuries after the
Dead Sea Scrolls were copied, and in key passages -- especially those
touching the divine council -- it contains alterations. Understanding both
traditions is essential for anyone who takes Scripture seriously.

Two chapters covering:
  1. The Septuagint (LXX) -- the Bible the apostles quoted
  2. The Masoretic Text (MT) -- the later standardization and its key variants
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: THE SEPTUAGINT (LXX)
    # =========================================================================
    {
        "id": "lxx-mt-1",
        "ref": "Hebrews 1:6; Deuteronomy 32:43 LXX; Acts 2:17-21",
        "chapter_num": 1,
        "title": "The Septuagint \u2014 The Bible the Apostles Used",
        "era": "lxx_mt",
        "type": "chapter",

        "synopsis": "The Septuagint (LXX) is the Greek translation of the Hebrew "
                    "scriptures produced by Jewish scholars in Alexandria, Egypt between "
                    "roughly 250 and 150 BC. Named after the tradition of seventy (or "
                    "seventy-two) translators, it became the Bible of the Jewish diaspora "
                    "and then the Bible of the early church. When NT writers quote the "
                    "Old Testament -- approximately 300 direct quotations -- the majority "
                    "follow the LXX wording, not the later Hebrew Masoretic Text. This is "
                    "not a footnote in textual history. It is the foundation of how the "
                    "apostles read, preached, and wrote Scripture.",

        "key_verse": {
            "ref": "Hebrews 1:6",
            "text": "And again, when he brings the firstborn into the world, he says, "
                    "\u2018Let all God\u2019s angels worship him.\u2019",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03c3\u03b5\u03c0\u03c4\u03c5\u03b1\u03b3\u03b9\u03bd\u03c4\u03b1 (Septuaginta)",
                "meaning": "Latin for 'seventy,' referring to the tradition that seventy "
                           "(or seventy-two) Jewish scholars translated the Torah into "
                           "Greek in Alexandria. The Roman numeral LXX became the standard "
                           "abbreviation. Originally only the Torah was translated (c. 250 BC), "
                           "with the Prophets and Writings following over the next century."
            },
            {
                "term": "\u03b4\u03b9\u03b1\u03c3\u03c0\u03bf\u03c1\u03ac (diaspora)",
                "meaning": "Dispersion, scattering. The Jewish communities living outside "
                           "the land of Israel, especially in Alexandria, which had the "
                           "largest Jewish population in the ancient world. Most diaspora "
                           "Jews had lost fluent Hebrew and needed Scripture in Greek -- "
                           "the common language of the Mediterranean following Alexander "
                           "the Great's conquests."
            },
            {
                "term": "\u03c0\u03c1\u03bf\u03c3\u03ba\u03c5\u03bd\u03b5\u03c9 (proskyneo)",
                "meaning": "To worship, bow down before, do obeisance. Used in the LXX "
                           "Deuteronomy 32:43 in the line 'Let all God's angels worship "
                           "him' -- the exact line quoted in Hebrews 1:6 to establish "
                           "Christ's superiority over angels. This line does not appear "
                           "in the Masoretic Text at all."
            },
            {
                "term": "\u05ea\u05b7\u05bc\u05e8\u05b0\u05d2\u05bc\u05d5\u05bc\u05dd (Targum)",
                "meaning": "Aramaic paraphrase-translations of the Hebrew Bible, produced "
                           "for synagogue audiences who spoke Aramaic rather than Hebrew. "
                           "The Targums often preserve interpretive traditions that predate "
                           "the Masoretic standardization and sometimes agree with the LXX "
                           "against the MT."
            }
        ],

        "ane_backdrop": "The translation of the Hebrew scriptures into Greek was part of "
                        "a massive cultural project in Ptolemaic Alexandria. The famous "
                        "Library of Alexandria, founded c. 283 BC, was the ancient world's "
                        "greatest repository of knowledge. The Letter of Aristeas (2nd "
                        "century BC) describes how Ptolemy II Philadelphus commissioned "
                        "the translation for the royal library. While the letter's details "
                        "are legendary, its core claim -- that Jewish scholars produced a "
                        "Greek Torah in Alexandria in the 3rd century BC -- is historically "
                        "sound. This was not a casual undertaking. Greek-speaking Judaism "
                        "in Alexandria produced Philo, the Wisdom of Solomon, and some of "
                        "the most sophisticated biblical interpretation of the ancient world. "
                        "The LXX emerged from a community that took its Scriptures with "
                        "absolute seriousness.",

        "second_temple": [
            {
                "source": "Letter of Aristeas (2nd century BC)",
                "summary": "According to the Letter of Aristeas, Ptolemy II Philadelphus "
                           "of Egypt commissioned seventy-two Jewish elders to translate "
                           "the Torah into Greek for the Library of Alexandria. The scholars "
                           "completed the work in exactly seventy-two days. While the account "
                           "is embellished, it attests to the high status the LXX held in "
                           "the Jewish community.",
                "relevance": "The story reflects the ancient Jewish conviction that the LXX "
                             "was not a loose paraphrase but a divinely guided translation. "
                             "Philo of Alexandria went further, claiming the translators "
                             "worked independently yet produced identical results -- a "
                             "tradition reflecting deep reverence for the Greek text."
            },
            {
                "source": "Philo of Alexandria (c. 20 BC \u2013 AD 50)",
                "summary": "Philo treated the LXX as fully authoritative Scripture, "
                           "building his entire philosophical-theological framework on "
                           "the Greek text. He saw no tension between the Greek translation "
                           "and the Hebrew original -- in his view, both were expressions "
                           "of the same divine word.",
                "relevance": "Philo demonstrates that educated, devout Jews before and "
                             "during the NT period regarded the LXX as fully scriptural. "
                             "The apostles' use of the LXX was not unusual -- it was the "
                             "standard practice of Greek-speaking Judaism."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 1:6", "note": "Quotes LXX Deuteronomy 32:43 -- 'Let all God's angels worship him' -- a line absent from the Masoretic Text. The NT argument for Christ's supremacy over angels depends on a text the standard Protestant OT does not contain.", "type": "nt"},
            {"ref": "Acts 2:17-21", "note": "Peter at Pentecost quotes Joel 2:28-32 following the LXX text, not the Hebrew. The sermon that launches the ekklesia era uses the Greek Old Testament.", "type": "nt"},
            {"ref": "Romans 3:10-18", "note": "Paul's catena of OT quotations in Romans 3 follows the LXX text throughout, including slight variations from the Hebrew that are theologically significant.", "type": "nt"},
            {"ref": "Matthew 1:23", "note": "Matthew quotes Isaiah 7:14 using the LXX's parthenos (virgin) rather than the Hebrew 'almah (young woman), a translation choice that shapes Christian understanding of the virgin birth.", "type": "nt"},
            {"ref": "Deuteronomy 32:43 LXX", "note": "The LXX preserves a longer version of the Song of Moses including 'Rejoice, O heavens, with him, and let all the sons of God worship him' -- the source text for Hebrews 1:6.", "type": "ot"},
            {"ref": "Isaiah 7:14", "note": "Hebrew 'almah (young woman of marriageable age) translated as parthenos (virgin) in the LXX -- a legitimate translation that the NT authors followed.", "type": "ot"}
        ],

        "divine_council_note": "The LXX's significance for divine council theology cannot be "
                               "overstated. In Deuteronomy 32:8, where the MT reads 'sons of "
                               "Israel,' the LXX reads 'angels of God' (angelon theou) -- a "
                               "Greek rendering of the Hebrew 'sons of God' (b\u0115n\u00ea \u02be\u0115l\u014dh\u00eem) "
                               "that the Dead Sea Scrolls later confirmed as original. The LXX "
                               "preserves the divine council worldview that the MT obscured. "
                               "Similarly, the expanded Deuteronomy 32:43 in the LXX -- with "
                               "its reference to the 'sons of God' worshipping -- provides the "
                               "text that Hebrews 1:6 quotes to place Christ above all divine "
                               "council members. The Bible the apostles used was more explicit "
                               "about the heavenly court than the one most Protestants read today.",

        "sections": [
            {
                "heading": "What the Septuagint Is \u2014 And Why It Was Made",
                "body": "Alexandria, Egypt in the 3rd century BC was home to the largest "
                        "Jewish community outside the land of Israel. Following Alexander "
                        "the Great's conquests, Greek had become the lingua franca of the "
                        "Mediterranean world. Most Jews in Alexandria spoke Greek as their "
                        "primary language. They needed the Scriptures in the language they "
                        "actually spoke. The translation began with the Torah -- the five "
                        "books of Moses -- around 250 BC, and the Prophets and Writings "
                        "were translated over the following century. The result was not a "
                        "rough paraphrase but a careful, verse-by-verse translation that "
                        "sometimes preserves readings older than what survived in the later "
                        "Hebrew manuscript tradition. The Septuagint became so widely used "
                        "that by the 1st century AD, it was simply 'the Scriptures' for "
                        "Greek-speaking Jews and the entire early ekklesia. When Paul writes "
                        "to ekklesias in Rome, Corinth, or Ephesus and quotes the Old "
                        "Testament, he is quoting the LXX -- because that is the text "
                        "his readers knew."
            },
            {
                "heading": "The Bible Jesus' Followers Used",
                "body": "This is the detail that changes everything for most believers: "
                        "the New Testament overwhelmingly quotes the LXX, not the Hebrew "
                        "text that underlies modern Protestant Bibles. Estimates vary, but "
                        "scholars consistently find that approximately 80% of Old Testament "
                        "quotations in the NT follow the LXX wording rather than the "
                        "Hebrew. This is not because the NT authors were careless about "
                        "the original language. It is because the LXX was the standard "
                        "Scripture of the Greek-speaking world in which Christianity was "
                        "born and spread. When the author of Hebrews builds his argument "
                        "for Christ's superiority over angels in chapter 1, he quotes "
                        "Deuteronomy 32:43 from the LXX -- 'Let all God's angels worship "
                        "him.' This line does not exist in the Masoretic Text. The canonical "
                        "NT argument depends on a text that the standard Protestant OT does "
                        "not contain. When Peter preaches at Pentecost (Acts 2:17-21), he "
                        "quotes Joel 2:28-32 from the LXX. The sermon that launches the "
                        "church age uses the Greek Old Testament. This is not a minor "
                        "bibliographic curiosity -- it is a fundamental reality about the "
                        "Bible the apostles actually read and preached."
            },
            {
                "heading": "Where the LXX and MT Diverge \u2014 And Why It Matters",
                "body": "In many places the LXX and the later Hebrew Masoretic Text agree "
                        "closely -- the Masoretes did careful work. But in certain key "
                        "passages, the texts diverge in ways that carry enormous theological "
                        "weight. Deuteronomy 32:8 is the clearest case: the MT reads 'sons "
                        "of Israel,' but the LXX reads 'angels of God' -- a Greek rendering "
                        "of the Hebrew 'b\u0115n\u00ea \u02be\u0115l\u014dh\u00eem' (sons of God). The Dead Sea Scrolls "
                        "confirmed the LXX as preserving the older reading. Deuteronomy "
                        "32:43 is equally significant: the LXX contains an expanded version "
                        "that includes 'let all the sons of God worship him' -- the exact "
                        "line the author of Hebrews quotes in 1:6. The MT has a shorter "
                        "version without this line. Again, the DSS (4QDeut) preserves a "
                        "text closer to the LXX than the MT. These are not minor textual "
                        "curiosities. They directly affect how we understand the divine "
                        "council, the relationship between Yahweh and the other elohim, "
                        "and the Christological argument of Hebrews. The LXX preserved "
                        "what the later Hebrew tradition altered."
            },
            {
                "heading": "The LXX as Textual Witness \u2014 Not Just Translation",
                "body": "A common misconception is that the LXX is simply a 'translation' "
                        "of the same Hebrew text that became the MT. The Dead Sea Scrolls "
                        "shattered this assumption. The DSS revealed that in the centuries "
                        "before the Masoretic standardization, multiple Hebrew text "
                        "traditions existed simultaneously. The LXX translators were not "
                        "translating loosely from the proto-MT -- in many cases they were "
                        "translating accurately from a different and older Hebrew manuscript "
                        "tradition. The book of Jeremiah in the LXX is about one-eighth "
                        "shorter than the MT version and has chapters in a different order. "
                        "DSS fragments of Jeremiah (4QJer-b) confirm that the shorter "
                        "LXX version reflects an older Hebrew text. Similarly, 1 Samuel "
                        "17-18 in the LXX differs substantially from the MT, and DSS "
                        "evidence supports the LXX tradition. The LXX is not a secondary "
                        "source to be corrected against the MT. It is an independent "
                        "witness to Hebrew text traditions that in some cases are older "
                        "and more original than what the Masoretes preserved. For serious "
                        "biblical study, both must be on the table."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: THE MASORETIC TEXT (MT)
    # =========================================================================
    {
        "id": "lxx-mt-2",
        "ref": "Deuteronomy 32:8-9; Genesis 3:15; Hebrews 1:6",
        "chapter_num": 2,
        "title": "The Masoretic Text \u2014 The Later Standardization",
        "era": "lxx_mt",
        "type": "chapter",

        "synopsis": "The Masoretic Text (MT) is the Hebrew text standardized by Jewish "
                    "scholars called the Masoretes between the 7th and 10th centuries AD. "
                    "It became the basis for almost all Protestant Old Testament "
                    "translations -- KJV, ESV, NIV, NASB. The Masoretes did careful, "
                    "largely faithful work. But they were working 600-1000 years after "
                    "the original texts, after the destruction of the temple, after the "
                    "rabbinic restructuring of Judaism. In key passages -- especially "
                    "those touching the divine council -- the MT contains readings that "
                    "the Dead Sea Scrolls proved to be later alterations.",

        "key_verse": {
            "ref": "Deuteronomy 32:8",
            "text": "When the Most High gave to the nations their inheritance, when he "
                    "divided mankind, he fixed the borders of the peoples according to "
                    "the number of the sons of God.",
            "translation": "ESV (following DSS/LXX reading)"
        },

        "hebrew_terms": [
            {
                "term": "\u05de\u05b8\u05e1\u05d5\u05b9\u05e8\u05b8\u05d4 (Masorah)",
                "meaning": "Tradition, transmission. The Masoretes were Jewish scribes "
                           "who preserved and transmitted the Hebrew biblical text, adding "
                           "vowel points, accent marks, and marginal notes (masorah) to a "
                           "consonantal text. Their work spanned roughly 600-1000 AD, "
                           "centered in Tiberias and Babylon. The Ben Asher family of "
                           "Tiberias produced the most influential Masoretic codices."
            },
            {
                "term": "\u05d1\u05bc\u05b0\u05e0\u05b5\u05d9 \u05d9\u05b4\u05e9\u05b0\u05c2\u05e8\u05b8\u05d0\u05b5\u05dc (b\u0115n\u00ea yisr\u0101\u02be\u0113l)",
                "meaning": "'Sons of Israel' -- the MT reading of Deuteronomy 32:8. The "
                           "Dead Sea Scrolls (4QDeut-j) and the LXX both preserve 'b\u0115n\u00ea "
                           "\u02be\u0115l\u014dh\u00eem' (sons of God) instead. The MT reading makes no "
                           "contextual sense: Yahweh divided nations according to the number "
                           "of Israel's sons -- but the nations were divided before Israel "
                           "existed. The original reading, 'sons of God,' refers to divine "
                           "council members assigned to govern the nations."
            },
            {
                "term": "\u05d4\u05d5\u05bc\u05d0 (hu\u2019)",
                "meaning": "He (masculine pronoun). In Genesis 3:15, the Hebrew uses the "
                           "masculine pronoun hu\u2019: 'HE shall bruise your head.' Jerome's "
                           "Latin Vulgate rendered this as ipsa (she), creating the "
                           "foundation for over a millennium of Marian theology in Western "
                           "Christianity. The Hebrew is clear: the Seed who crushes the "
                           "serpent is masculine -- pointing to an individual male descendant."
            },
            {
                "term": "\u05d0\u05b1\u05dc\u05b9\u05d4\u05b4\u05d9\u05dd (elohim)",
                "meaning": "A morphologically plural noun that can refer to the God of "
                           "Israel, divine council members, or spiritual beings generally. "
                           "Jerome's Vulgate systematically flattened elohim vocabulary, "
                           "rendering divine council language as singular Deus and removing "
                           "the council framework from Latin Christianity for over a "
                           "thousand years."
            }
        ],

        "ane_backdrop": "The Masoretic standardization was not conducted in a vacuum. After "
                        "the destruction of the Second Temple in 70 AD, rabbinic Judaism "
                        "underwent a massive restructuring. The rabbis at Yavneh (c. 90 AD) "
                        "began the process of standardizing the Hebrew canon, preferring "
                        "texts in Hebrew over Greek, and excluding works associated with "
                        "sectarian or Christian communities. The criteria were partly "
                        "linguistic (must be in Hebrew), partly temporal (must not post-date "
                        "Ezra), and partly theological. The divine council framework that "
                        "Second Temple Judaism had embraced was increasingly uncomfortable "
                        "for a rabbinic movement defining itself against Christianity's "
                        "Christological claims. The 'sons of God' in Deuteronomy 32:8 "
                        "became 'sons of Israel' -- a reading that eliminated the divine "
                        "council from the foundational text of YHWH's governance of nations.",

        "second_temple": [
            {
                "source": "Yavneh/Jamnia Council (c. 90 AD)",
                "summary": "After the destruction of the temple, Jewish leaders gathered "
                           "at Yavneh to restructure Judaism around Torah study and "
                           "synagogue worship rather than temple sacrifice. Part of this "
                           "process involved standardizing which books were sacred and "
                           "which Hebrew textual traditions were authoritative.",
                "relevance": "The Yavneh decisions were shaped by post-temple concerns, "
                             "including the need to distinguish Jewish Scripture from texts "
                             "being adopted by Christians. This context helps explain why "
                             "certain readings were altered and certain books (like 1 Enoch) "
                             "were excluded from the emerging rabbinic canon."
            },
            {
                "source": "Jerome's Vulgate (382-405 AD)",
                "summary": "Jerome was commissioned by Pope Damasus I to produce a standard "
                           "Latin Bible. He chose to translate the OT from the Hebrew "
                           "Jamnia canon rather than the LXX, calling his approach Hebraica "
                           "veritas ('Hebrew truth'). But Jerome's own translation choices "
                           "introduced new theological problems -- including the ipsa "
                           "('she') pronoun in Genesis 3:15.",
                "relevance": "Jerome's choice of the Hebrew over the Greek ensured that "
                             "Western Christianity would read the MT tradition -- with its "
                             "altered divine council readings -- for over a thousand years. "
                             "The LXX readings that the NT authors actually quoted were "
                             "effectively sidelined in the Western church."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9", "note": "The textual crux: MT 'sons of Israel' vs. DSS/LXX 'sons of God.' The entire Deuteronomy 32 worldview -- nations assigned to divine beings, Israel kept by Yahweh -- depends on which reading is original. The DSS settles it: 'sons of God.'", "type": "ot"},
            {"ref": "Deuteronomy 32:43", "note": "LXX preserves 'Let all God's angels worship him,' quoted in Hebrews 1:6. The MT version lacks this line entirely. A canonical NT Christological argument depends on a text the MT does not contain.", "type": "ot"},
            {"ref": "Genesis 3:15", "note": "Hebrew hu' (he) vs. Jerome's ipsa (she). The Hebrew clearly uses the masculine pronoun, pointing to a single male descendant who will crush the serpent. Jerome's feminine rendering shaped Marian theology for 1,200 years.", "type": "ot"},
            {"ref": "Hebrews 1:6", "note": "Quotes LXX Deuteronomy 32:43 to argue Christ's supremacy over angels. The author of Hebrews used the LXX -- the NT's Christological argument requires the Greek OT, not the Hebrew MT.", "type": "nt"},
            {"ref": "Psalm 82:1", "note": "MT preserves 'God stands in the divine council; in the midst of the gods he holds judgment.' Even the MT retained this divine council text, though its implications were increasingly minimized in rabbinic interpretation.", "type": "ot"},
            {"ref": "Hebrews 7:13-14", "note": "Jesus is from the tribe of Judah, not Levi -- His priesthood is Melchizedekian, not Levitical. The LXX/DSS tradition of Psalm 110 and 11QMelchizedek illuminates this framework.", "type": "nt"}
        ],

        "divine_council_note": "The Masoretic Text's alteration of Deuteronomy 32:8 from "
                               "'sons of God' to 'sons of Israel' is the single most "
                               "consequential textual variant for divine council theology. "
                               "With the original reading, Deuteronomy 32:8-9 describes "
                               "Yahweh dividing the nations among divine beings (the b\u0115n\u00ea "
                               "\u02be\u0115l\u014dh\u00eem) while keeping Israel as His own inheritance. "
                               "This is the foundation of the divine council worldview: "
                               "the nations are under the governance of lesser divine "
                               "beings who have become corrupt (Psalm 82), and Yahweh's "
                               "plan to reclaim all nations runs through Israel and "
                               "culminates in Christ. With the MT reading, 'sons of Israel,' "
                               "the entire framework collapses into a circular reference. "
                               "The DSS confirmed the original reading and restored the "
                               "worldview the biblical authors actually held.",

        "sections": [
            {
                "heading": "What the Masoretes Did \u2014 And When They Did It",
                "body": "The Masoretes were Jewish scribal families -- primarily the Ben "
                        "Asher and Ben Naphtali families of Tiberias -- who worked between "
                        "approximately 600 and 1000 AD to standardize the Hebrew biblical "
                        "text. Their most significant contribution was adding vowel points "
                        "(niqqud) and cantillation marks (te'amim) to the consonantal "
                        "Hebrew text, which had been written without vowels for centuries. "
                        "This was enormously important work -- without vowels, Hebrew "
                        "words can often be read multiple ways, and the Masoretes fixed "
                        "the reading tradition that had been passed down orally. They also "
                        "added marginal notes tracking unusual spellings, counting letters "
                        "and words to prevent copying errors. Their care and precision is "
                        "not in question. What is in question is whether the consonantal "
                        "text they received in the 7th century AD was identical in every "
                        "respect to the text that existed before the 1st century. The "
                        "Dead Sea Scrolls proved it was not."
            },
            {
                "heading": "Deuteronomy 32:8 \u2014 The Variant That Changes Everything",
                "body": "The MT of Deuteronomy 32:8 reads: 'When the Most High gave to "
                        "the nations their inheritance, when he divided mankind, he fixed "
                        "the borders of the peoples according to the number of the sons "
                        "of Israel.' But the LXX reads 'angels of God' (angelon theou), "
                        "and the Dead Sea Scrolls fragment 4QDeut-j reads 'b\u0115n\u00ea \u02be\u0115l\u014dh\u00eem' "
                        "-- 'sons of God.' The DSS fragment predates the MT by over a "
                        "thousand years. The LXX was translating from a Hebrew text that "
                        "read 'sons of God,' not 'sons of Israel.' The contextual argument "
                        "is decisive: in the MT reading, God divides nations according to "
                        "the number of Israel's sons. But this event occurs at Babel "
                        "(Genesis 10-11), before Israel exists. Jacob has not yet been "
                        "born. The 'sons of Israel' reading is an anachronism. The "
                        "original reading -- 'sons of God' -- makes perfect sense: "
                        "Yahweh divided the nations among divine council members, allotting "
                        "each nation to a divine being (compare Daniel 10:13, 10:20-21), "
                        "while keeping Israel as His own portion (Deuteronomy 32:9). This "
                        "is the Deuteronomy 32 worldview that undergirds the entire divine "
                        "council framework."
            },
            {
                "heading": "Genesis 3:15 and Jerome\u2019s Pronoun \u2014 He or She?",
                "body": "The Hebrew text of Genesis 3:15 uses the masculine pronoun hu\u2019 "
                        "(\u05d4\u05d5\u05bc\u05d0): 'HE shall bruise your head, and you shall bruise HIS "
                        "heel.' The subject is the zera\u2019 (seed) of the woman -- a singular "
                        "masculine noun pointing to an individual male descendant. Jerome, "
                        "translating into Latin around 390 AD, rendered this as ipsa "
                        "conteret caput tuum -- 'SHE shall crush your head.' Whether this "
                        "was a deliberate theological choice or a manuscript variant Jerome "
                        "was following, the result shaped Western theology for over a "
                        "millennium. The 'she' reading became the foundation of Marian "
                        "theology -- the idea that Mary, not merely her son, would crush "
                        "the serpent. Catholic art for centuries depicted Mary standing on "
                        "a serpent's head. The Hebrew is clear: the Seed is masculine, "
                        "singular, and individual. Paul confirms this in Galatians 3:16: "
                        "the promise is to one Seed, 'who is Christ.' The protoevangelium "
                        "points to Jesus, not Mary. Jerome's pronoun change -- whatever "
                        "its origin -- demonstrates how a single translation choice can "
                        "redirect centuries of theology."
            },
            {
                "heading": "Hebrews 1:6 \u2014 The NT Quote the MT Cannot Explain",
                "body": "The author of Hebrews, building his argument for Christ's "
                        "superiority over angels, quotes Deuteronomy 32:43: 'Let all "
                        "God's angels worship him' (Hebrews 1:6). There is one problem: "
                        "this line does not exist in the Masoretic Text. Open any "
                        "Protestant Bible to Deuteronomy 32:43 and look for it -- it is "
                        "not there. The line exists in the LXX and is confirmed by the "
                        "Dead Sea Scrolls (4QDeut). The canonical New Testament quotes "
                        "with full authority a line from the Old Testament that the "
                        "standard Hebrew text does not contain. This is not a problem "
                        "to be explained away. It is evidence that the LXX preserves "
                        "readings that are older and more original than the MT in "
                        "certain passages. The author of Hebrews was not quoting a "
                        "corrupt text -- he was quoting a text that the later Masoretic "
                        "tradition had shortened. For anyone who takes the NT as Scripture, "
                        "the implications are unavoidable: the LXX is not a secondary "
                        "source. In this case, it is the source the inspired NT author "
                        "treated as authoritative, and the MT is the tradition that "
                        "lacks the original reading."
            }
        ]
    }
]
