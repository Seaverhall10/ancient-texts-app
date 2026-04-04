"""
era_nephilim_story.py -- The Nephilim Narrative (Chapters 1-4)

A continuous narrative tracing the Nephilim thread through Scripture,
from the boundary violation of Genesis 6 through the giant clans in
the land, Joshua's systematic campaign, and David's confrontation
with Goliath of Gath. Each chapter uses three evidence tiers:

  [A] Direct Scripture (ESV) -- what the text plainly says
  [B] Hebrew analysis + valid inference -- what the original language reveals
  [C] 1 Enoch, DSS, ANE parallels -- the wider ancient context

This is the SECOND rebellion narrative (Hermon/Watchers, Genesis 6:1-4),
distinct from the FIRST rebellion (Eden/Nachash, Genesis 3) and the
THIRD rebellion (Babel/territorial allotment, Deuteronomy 32:8-9).
The three rebellions are independent events with independent actors,
though Genesis 3:15 provides the thematic thread connecting God's
response to all three.

Theological framework: Divine council theology. The 'sons of God' in
Genesis 6 are members of the heavenly council who violated their
appointed boundary, producing hybrid offspring. The Nephilim and their
post-Flood descendants (Anakim, Rephaim, etc.) represent the physical
legacy of that rebellion. Their elimination is not genocide but targeted
removal of a corrupted bloodline that threatened the messianic seed.

Sources: ESV (all Scripture), Michael S. Heiser (The Unseen Realm,
Reversing Hermon), Nickelsburg (1 Enoch Hermeneia commentary),
Archie T. Wright (The Origin of Evil Spirits), Amar Annus
(On the Origin of Watchers).
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: THE BOUNDARY VIOLATION -- Genesis 6:1-4
    # =========================================================================
    {
        "id": "nephilim-story-boundary",
        "ref": "Genesis 6:1-4",
        "chapter_num": 1,
        "title": "The Boundary Violation \u2014 Genesis 6:1\u20134",
        "era": "nephilim_story",
        "type": "chapter",

        "synopsis": "Something happened before the Flood that was so catastrophic "
                    "God decided to destroy all flesh on the earth. Genesis 6:1-4 "
                    "describes it in four verses that have generated more debate "
                    "than almost any other passage in the Old Testament: the "
                    "'sons of God' saw the 'daughters of man,' took wives from "
                    "among them, and produced the Nephilim \u2014 the mighty men of "
                    "old, men of renown. The question is not what the text says. "
                    "The question is whether we will let it say what it says.",

        "key_verse": {
            "ref": "Genesis 6:4",
            "text": "The Nephilim were on the earth in those days, and also "
                    "afterward, when the sons of God came in to the daughters "
                    "of man and they bore children to them. These were the "
                    "mighty men who were of old, the men of renown.",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "bene ha\u2019elohim",
                "hebrew": "\u05d1\u05b0\u05e0\u05b5\u05d9 \u05d4\u05b8\u05d0\u05b1\u05dc\u05b9\u05d4\u05b4\u05d9\u05dd",
                "meaning": "'Sons of God' \u2014 divine/heavenly beings. This exact "
                           "phrase appears in Job 1:6, 2:1, and 38:7, where it "
                           "unambiguously refers to members of God's heavenly "
                           "council. No instance in the Hebrew Bible uses this "
                           "phrase for human beings.",
                "verse": "Genesis 6:2"
            },
            {
                "term": "nephilim",
                "hebrew": "\u05e0\u05b0\u05e4\u05b4\u05dc\u05b4\u05d9\u05dd",
                "meaning": "The name is often connected to the root naphal "
                           "(\u05e0\u05b8\u05e4\u05b7\u05dc, 'to fall'), though the precise derivation is "
                           "debated \u2014 the expected passive form would be nephulim, "
                           "not nephilim. Whether it means 'fallen ones,' 'those "
                           "who fall upon' (warriors), or derives from a separate "
                           "root remains uncertain. What is clear: the LXX "
                           "translators understood them as gigantes.",
                "verse": "Genesis 6:4"
            },
            {
                "term": "gibborim",
                "hebrew": "\u05d2\u05b4\u05bc\u05d1\u05b9\u05bc\u05e8\u05b4\u05d9\u05dd",
                "meaning": "'Mighty ones,' 'warriors.' From gabar (\u05d2\u05b8\u05d1\u05b7\u05e8), 'to be "
                           "strong, to prevail.' The Nephilim are gibborim \u2014 "
                           "mighty warriors of superhuman power. The word implies "
                           "physical dominance far beyond ordinary men.",
                "verse": "Genesis 6:4"
            },
            {
                "term": "naphal",
                "hebrew": "\u05e0\u05b8\u05e4\u05b7\u05dc",
                "meaning": "'To fall, to fall down, to lie.' The verbal root behind "
                           "nephilim. Used throughout the Hebrew Bible for falling "
                           "from a height, falling in battle, or being cast down "
                           "from a position of honor.",
                "verse": "Genesis 6:4"
            }
        ],

        "ane_backdrop": "The motif of divine beings mating with human women is not "
                        "unique to Genesis. Greek mythology preserves accounts of the "
                        "Titans, semi-divine offspring of Ouranos (Heaven) and Gaia "
                        "(Earth), who were imprisoned beneath the earth after warring "
                        "against the Olympian gods. Mesopotamian traditions describe "
                        "the apkallu \u2014 antediluvian sages sent by the gods to civilize "
                        "humanity \u2014 who in some traditions transgress their mandate and "
                        "are punished. Amar Annus has demonstrated that the Watcher "
                        "tradition in 1 Enoch draws on Mesopotamian apkallu traditions "
                        "but inverts the valuation: where Mesopotamia celebrates the "
                        "apkallu as culture-bringers, the Enochic tradition condemns "
                        "the Watchers for the same acts.",

        "second_temple": [
            {
                "source": "1 Enoch 6:1-7:6 (Book of the Watchers)",
                "summary": "According to 1 Enoch, 200 Watchers led by Shemihazah "
                           "descended on Mount Hermon and swore a mutual oath to "
                           "take human wives. They taught forbidden knowledge: "
                           "Azazel taught metalwork and cosmetics; others taught "
                           "sorcery, astrology, and root-cutting.",
                "relevance": "Provides the most detailed Second Temple expansion of "
                             "Genesis 6:1-4, preserved in 11 Aramaic copies at Qumran."
            },
            {
                "source": "Jude 14-15",
                "summary": "The New Testament epistle of Jude directly quotes 1 Enoch "
                           "1:9 as prophecy, attributing it to 'Enoch, the seventh "
                           "from Adam.' This is the only explicit quotation of a "
                           "non-canonical text as prophetic in the New Testament. "
                           "This demonstrates 1 Enoch's high authority in the "
                           "apostolic period, though it does not confer canonical "
                           "status on the entire book.",
                "relevance": "Demonstrates that at least one NT author considered "
                             "the Enochic Watcher tradition authoritative enough to "
                             "cite as genuine prophecy."
            },
            {
                "source": "2 Peter 2:4-5",
                "summary": "Peter writes that 'God did not spare angels when they "
                           "sinned, but cast them into Tartarus (tartarosas) and "
                           "committed them to chains of gloomy darkness.' The Greek "
                           "word tartarosas appears nowhere else in the NT.",
                "relevance": "Peter uses a term from Greek cosmology for the prison "
                             "of the Titans \u2014 directly linking the imprisoned angels "
                             "to the Watcher/Titan tradition."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 6:1-4", "note": "The boundary violation itself \u2014 sons of God take daughters of man", "type": "ot"},
            {"ref": "Genesis 6:5-7", "note": "God's response: total destruction of all flesh via the Flood", "type": "ot"},
            {"ref": "Job 1:6", "note": "bene ha\u2019elohim present themselves before YHWH \u2014 identical phrase", "type": "ot"},
            {"ref": "Job 2:1", "note": "bene ha\u2019elohim again in the divine council scene", "type": "ot"},
            {"ref": "Job 38:7", "note": "bene elohim shouted for joy at creation \u2014 they existed before the earth", "type": "ot"},
            {"ref": "Jude 6", "note": "Angels who did not stay within their own domain, kept in eternal chains", "type": "nt"},
            {"ref": "Jude 14-15", "note": "Direct quotation of 1 Enoch 1:9 as prophecy of Enoch", "type": "nt"},
            {"ref": "2 Peter 2:4-5", "note": "Angels who sinned cast into Tartarus \u2014 a Greek term for the Titan prison", "type": "nt"},
            {"ref": "1 Enoch 6-16", "note": "According to 1 Enoch, 200 Watchers descended on Mount Hermon and swore an oath", "type": "pseudepigrapha"},
            {"ref": "4Q201-202 (Dead Sea Scrolls)", "note": "Aramaic fragments of 1 Enoch from Qumran, confirming the antiquity of the Watcher tradition", "type": "dss"}
        ],

        "divine_council_note": "Genesis 6:1-4 describes a rebellion WITHIN the divine "
                               "council. The bene ha\u2019elohim are council members \u2014 the "
                               "same category of beings who present themselves before "
                               "YHWH in Job 1-2 and who shouted at creation in Job 38:7. "
                               "Their sin was a boundary violation: leaving their proper "
                               "domain (Jude 6) to take what was not appointed to them. "
                               "This is the SECOND of three independent rebellions \u2014 "
                               "distinct from Eden (Nachash) and Babel (Deut 32:8). Each "
                               "involves different actors, different sins, and different "
                               "divine responses.",

        "sections": [
            # --- TIER A: CANON ONLY ---
            {
                "heading": "What Your Bible Actually Says",
                "tier": "a",
                "body": "[A] Read Genesis 6:1-4 slowly. 'When man began to multiply "
                        "on the face of the land and daughters were born to them, "
                        "the sons of God saw that the daughters of man were attractive. "
                        "And they took as their wives any they chose' (ESV). The text "
                        "does not hedge. The 'sons of God' <em>saw</em> and <em>took</em> "
                        "\u2014 the same language of desire and seizure. The result: the "
                        "Nephilim, described as 'the mighty men who were of old, the "
                        "men of renown.' These are not obscure figures. They are "
                        "famous. Ancient. Powerful. The text presents them as a known "
                        "category \u2014 the original audience did not need the Nephilim "
                        "explained to them. Four verses. No commentary. No softening. "
                        "This is what your Bible says happened before the Flood."
            },
            {
                "heading": "The Flood Response",
                "tier": "a",
                "body": "[A] The very next verses deliver God's verdict: 'The LORD saw "
                        "that the wickedness of man was great in the earth, and that "
                        "every intention of the thoughts of his heart was only evil "
                        "continually. And the LORD regretted that he had made man on "
                        "the earth, and it grieved him to his heart. So the LORD said, "
                        "\"I will blot out man whom I have created from the face of the "
                        "land\"' (Genesis 6:5-7, ESV). The response is total \u2014 the "
                        "destruction of all flesh. Ask yourself: if Genesis 6:1-4 "
                        "describes nothing more than intermarriage between two human "
                        "lines (the Sethite interpretation), why does God respond by "
                        "destroying <em>every living thing</em>? Intermarriage between "
                        "human groups does not warrant the annihilation of all land "
                        "animals. Something far more catastrophic than a social boundary "
                        "violation has occurred. The punishment must fit the crime \u2014 "
                        "and the punishment here is extinction-level."
            },
            # --- TIER B: HEBREW ANALYSIS ---
            {
                "heading": "What the Hebrew Reveals",
                "tier": "b",
                "body": "[B] The phrase bene ha\u2019elohim (\u05d1\u05b0\u05e0\u05b5\u05d9 \u05d4\u05b8\u05d0\u05b1\u05dc\u05b9\u05d4\u05b4\u05d9\u05dd) means 'sons of "
                        "God' \u2014 and it is not ambiguous. Every other occurrence of "
                        "this exact phrase in the Hebrew Bible refers to heavenly "
                        "beings. Job 1:6: the bene ha\u2019elohim present themselves "
                        "before YHWH in the divine council. Job 2:1: the same scene "
                        "repeated. Job 38:7: the bene elohim (short form) shouted "
                        "for joy when God laid the earth's foundation \u2014 they were "
                        "present <em>before the earth existed</em>. The word nephilim "
                        "(\u05e0\u05b0\u05e4\u05b4\u05dc\u05b4\u05d9\u05dd) derives from naphal (\u05e0\u05b8\u05e4\u05b7\u05dc), 'to fall.' They "
                        "are the fallen ones. The gibborim (\u05d2\u05b4\u05bc\u05d1\u05b9\u05bc\u05e8\u05b4\u05d9\u05dd) are 'mighty "
                        "warriors' \u2014 a word used elsewhere for exceptional military "
                        "power. The Sethite interpretation \u2014 that bene ha\u2019elohim "
                        "means 'descendants of Seth' \u2014 was absent from the dominant "
                        "Jewish and early Christian tradition until Julius "
                        "Africanus proposed it around 225 AD \u2014 some scholars "
                        "trace proto-Sethite readings to Philo of Alexandria "
                        "(1st century), though Philo's reading is more "
                        "allegorical than the later patristic Sethite view. For the first two centuries of the church, "
                        "the supernatural reading was universal."
            },
            {
                "heading": "The Question the Text Forces",
                "tier": "b",
                "body": "[B] If bene ha\u2019elohim means divine beings in Job 1:6, "
                        "divine beings in Job 2:1, and divine beings in Job 38:7, "
                        "on what basis does it suddenly mean 'Seth's descendants' "
                        "in Genesis 6:2? The burden of proof is entirely on the "
                        "Sethite view. Consider what the Sethite reading requires "
                        "you to accept: that the Hebrew phrase bene ha\u2019elohim, which "
                        "everywhere else in the Hebrew Bible means heavenly beings, "
                        "here alone means pious human men; that intermarriage between "
                        "two human lines produces giants (nephilim/gibborim); that "
                        "God's response to this human social problem is the total "
                        "annihilation of all land-based life; and that the New "
                        "Testament references in Jude 6-7 and 2 Peter 2:4 to angels "
                        "who 'did not stay within their own position of authority' "
                        "and who were imprisoned refer to something other than what "
                        "Genesis 6 describes. The Sethite view was introduced in the "
                        "third century AD by writers influenced by Platonic dualism, "
                        "who found the idea of spirit-matter interaction philosophically "
                        "objectionable. It is a philosophical objection, not an "
                        "exegetical one."
            },
            # --- TIER C: FULL PICTURE ---
            {
                "heading": "The Complete Story",
                "tier": "c",
                "body": "[C] According to 1 Enoch 6-16, what Genesis compresses into "
                        "four verses was a coordinated rebellion. Two hundred members "
                        "of the heavenly host \u2014 called Watchers (Aramaic: irin) \u2014 "
                        "descended on Mount Hermon under the leadership of Shemihazah. "
                        "They swore a binding oath (the name 'Hermon' is related to "
                        "the Hebrew cherem, 'oath/ban'). They took human wives and "
                        "produced the Nephilim, who according to 1 Enoch 7:2-5 were "
                        "giants who consumed the produce of the earth and then turned "
                        "to consuming humans themselves. A second Watcher leader, "
                        "Azazel, taught forbidden arts: metalwork for weapons, "
                        "cosmetics, sorcery, astrology. The corruption became total. "
                        "God sent the archangels to imprison the Watchers and destroy "
                        "the Nephilim. Jude 14-15 quotes 1 Enoch 1:9 as genuine "
                        "prophecy of 'Enoch, the seventh from Adam.' Eleven Aramaic "
                        "copies of 1 Enoch were found at Qumran among the Dead Sea "
                        "Scrolls \u2014 more copies than some biblical books. The early "
                        "church fathers (Justin Martyr, Irenaeus, Clement of "
                        "Alexandria, Tertullian) all affirmed the supernatural "
                        "reading of Genesis 6."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: GIANTS IN THE LAND -- Numbers 13, Deuteronomy 2-3
    # =========================================================================
    {
        "id": "nephilim-story-giants-land",
        "ref": "Numbers 13:28-33; Deuteronomy 2:10-21; 3:11",
        "chapter_num": 2,
        "title": "Giants in the Land \u2014 Numbers 13, Deuteronomy 2\u20133",
        "era": "nephilim_story",
        "type": "chapter",

        "synopsis": "The Flood was supposed to end the Nephilim. It did not. When "
                    "Israel's spies entered Canaan, they came back terrified: 'We "
                    "saw the Nephilim (the sons of Anak, who come from the "
                    "Nephilim).' Moses then catalogs the giant clans inhabiting "
                    "the Promised Land with the precision of an intelligence report "
                    "\u2014 Rephaim, Emim, Zamzummim, Anakim. These were not metaphors. "
                    "They had names, territories, and a king with an iron bed over "
                    "thirteen feet long (~13.5 feet).",

        "key_verse": {
            "ref": "Numbers 13:33",
            "text": "And there we saw the Nephilim (the sons of Anak, who come "
                    "from the Nephilim), and we seemed to ourselves like "
                    "grasshoppers, and so we seemed to them.",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "rephaim",
                "hebrew": "\u05e8\u05b0\u05e4\u05b8\u05d0\u05b4\u05d9\u05dd",
                "meaning": "The overarching category for all giant clans. The word "
                           "carries a devastating double meaning: in the land of the "
                           "living, Rephaim are giant warriors of terrifying stature; "
                           "in Sheol, the same word means 'shades' or 'the dead' "
                           "(Isaiah 14:9, 26:14). The Hebrew language itself links "
                           "these beings to death even while they walk the earth.",
                "verse": "Deuteronomy 2:11, 20"
            },
            {
                "term": "anakim",
                "hebrew": "\u05e2\u05b2\u05e0\u05b8\u05e7\u05b4\u05d9\u05dd",
                "meaning": "From anak (\u05e2\u05b2\u05e0\u05b8\u05e7), possibly meaning 'long-necked' or "
                           "'giant.' The Anakim are the specific giant clan occupying "
                           "Hebron and the hill country of Judah. Numbers 13:33 "
                           "explicitly connects them to the Nephilim: 'the sons of "
                           "Anak, who come from the Nephilim.'",
                "verse": "Numbers 13:33"
            },
            {
                "term": "emim",
                "hebrew": "\u05d0\u05b5\u05d9\u05de\u05b4\u05d9\u05dd",
                "meaning": "'Terrifying ones' \u2014 the Moabite name for the Rephaim who "
                           "once occupied their territory. The name itself is a "
                           "testimony to the horror these beings inspired. 'Counted "
                           "as Rephaim' (Deuteronomy 2:11).",
                "verse": "Deuteronomy 2:10-11"
            },
            {
                "term": "zamzummim",
                "hebrew": "\u05d6\u05b7\u05de\u05b0\u05d6\u05bb\u05de\u05b4\u05bc\u05d9\u05dd",
                "meaning": "'Mumblers' or 'plotters' \u2014 the Ammonite name for the "
                           "Rephaim. Like the Emim, they were 'great and many, and "
                           "tall as the Anakim' (Deuteronomy 2:20-21). YHWH "
                           "destroyed them before the Ammonites.",
                "verse": "Deuteronomy 2:20"
            }
        ],

        "ane_backdrop": "The Ugaritic rpum texts (KTU 1.20-22) from Ras Shamra describe "
                        "the Rephaim as powerful warrior-spirits who ride chariots and "
                        "attend divine feasts. The Ditanu/Didanu clan name, associated "
                        "with the rpum in Ugaritic literature, also appears in "
                        "Mesopotamian king lists as ancestral founders. The biblical "
                        "giants are not an Israelite invention \u2014 they are part of a "
                        "widely recognized ANE category of semi-divine beings whose "
                        "existence was taken for granted across the ancient world.",

        "second_temple": [
            {
                "source": "1 Enoch 15:8-10",
                "summary": "According to 1 Enoch, when the Nephilim died, their "
                           "spirits were released as evil spirits upon the earth. "
                           "Because they originated from both heavenly and earthly "
                           "parents, their spirits belong fully to neither realm "
                           "and wander the earth as demons.",
                "relevance": "Provides the dominant Second Temple explanation for "
                             "the origin of demons \u2014 they are the disembodied spirits "
                             "of dead Nephilim."
            },
            {
                "source": "Book of Giants (4Q530-532)",
                "summary": "Fragments from Qumran describe the Nephilim giants "
                           "receiving dreams of their coming destruction and "
                           "seeking Enoch's intercession on their behalf.",
                "relevance": "Confirms that the Nephilim tradition was actively "
                             "expanded at Qumran, with the giants portrayed as "
                             "sentient beings aware of their doom."
            },
            {
                "source": "Jubilees 7:21-25",
                "summary": "According to Jubilees, the giants turned against one "
                           "another and 'devoured one another,' and after their "
                           "destruction their spirits continued to lead astray "
                           "the children of Noah.",
                "relevance": "Another Second Temple witness connecting post-Flood "
                             "demonic activity to the pre-Flood Nephilim."
            }
        ],

        "cross_refs": [
            {"ref": "Numbers 13:28-33", "note": "The spies' report: Nephilim (sons of Anak) in Canaan, Israel as 'grasshoppers'", "type": "ot"},
            {"ref": "Deuteronomy 2:10-11", "note": "Emim formerly in Moab, 'counted as Rephaim, tall as the Anakim'", "type": "ot"},
            {"ref": "Deuteronomy 2:20-21", "note": "Zamzummim formerly in Ammon, destroyed by YHWH, 'tall as the Anakim'", "type": "ot"},
            {"ref": "Deuteronomy 3:11", "note": "Og king of Bashan, last of the Rephaim \u2014 his bed was 9 cubits long (~13.5 feet)", "type": "ot"},
            {"ref": "Genesis 14:5", "note": "Rephaim, Emim, and Zuzim (Zamzummim) mentioned in Abraham's era \u2014 already in the land", "type": "ot"},
            {"ref": "Isaiah 14:9", "note": "Rephaim stirred up in Sheol \u2014 same word, now meaning 'shades of the dead'", "type": "ot"},
            {"ref": "Isaiah 26:14", "note": "'The dead (Rephaim) will not live, the shades will not rise'", "type": "ot"},
            {"ref": "1 Enoch 15:8-10", "note": "According to 1 Enoch, the spirits of dead Nephilim became demons on earth", "type": "pseudepigrapha"},
            {"ref": "4Q530-532 (Book of Giants)", "note": "Qumran fragments describing the Nephilim's dreams of destruction", "type": "dss"}
        ],

        "divine_council_note": "The post-Flood presence of Nephilim descendants in "
                               "Canaan \u2014 the very land God promised to Abraham \u2014 is not "
                               "coincidental in the divine council framework. These giant "
                               "clans occupied the territory that YHWH reserved for His "
                               "own allotment (Deuteronomy 32:8-9, DSS/LXX: 'according "
                               "to the number of the sons of God'). Israel's inheritance "
                               "was strategically infested with the physical legacy of "
                               "the Watcher rebellion. The Conquest will be a direct "
                               "confrontation between YHWH's people and the corrupted "
                               "seed of the second rebellion.",

        "sections": [
            # --- TIER A: CANON ONLY ---
            {
                "heading": "The Spies' Report",
                "tier": "a",
                "body": "[A] Forty years after the Exodus, Moses sends twelve spies "
                        "into Canaan. They return with a split verdict: the land "
                        "flows with milk and honey, but 'the people who dwell in "
                        "the land are strong, and the cities are fortified and very "
                        "large. And besides, we saw the descendants of Anak there' "
                        "(Numbers 13:28, ESV). Then the bombshell: 'And there we saw "
                        "the Nephilim (the sons of Anak, who come from the Nephilim), "
                        "and we seemed to ourselves like grasshoppers, and so we "
                        "seemed to them' (13:33). Stop. The Flood was supposed to "
                        "destroy 'all flesh' (Genesis 6:13). Yet here, centuries "
                        "later, the spies identify these beings by name \u2014 Nephilim "
                        "\u2014 and trace their lineage: the sons of Anak 'come from' "
                        "the Nephilim. The parenthetical is an editorial note making "
                        "the connection explicit. Whatever the Nephilim were before "
                        "the Flood, their descendants are in the Promised Land."
            },
            {
                "heading": "Moses Catalogs the Giants",
                "tier": "a",
                "body": "[A] Deuteronomy 2-3 reads like a military intelligence "
                        "briefing. Moses catalogs the giant populations with the "
                        "specificity of a field report: the Emim in Moab, 'a people "
                        "great and many, and tall as the Anakim' (2:10); the "
                        "Zamzummim in Ammon, also 'great and many, and tall as the "
                        "Anakim' (2:20-21); and in Bashan, King Og \u2014 'the remnant of "
                        "the Rephaim' \u2014 whose iron bed was 'nine cubits in length "
                        "and four cubits in breadth' (3:11). That is roughly 13.5 "
                        "feet long and 6 feet wide. These are not metaphors. Moses "
                        "is recording specific nations with specific territories, "
                        "specific names in multiple languages (Rephaim in Hebrew, "
                        "Emim in Moabite, Zamzummim in Ammonite), and at least one "
                        "specific artifact \u2014 Og's bed, which could still be seen "
                        "in Rabbah. The text wants you to know these beings were real "
                        "and recently present."
            },
            # --- TIER B: HEBREW ANALYSIS ---
            {
                "heading": "The Giant Taxonomy",
                "tier": "b",
                "body": "[B] The Hebrew reveals something the English conceals. The "
                        "word rephaim (\u05e8\u05b0\u05e4\u05b8\u05d0\u05b4\u05d9\u05dd) carries a devastating dual meaning. "
                        "In the Pentateuch and Joshua, the Rephaim are a race of "
                        "giants \u2014 the overarching category under which Anakim, Emim, "
                        "and Zamzummim are all classified ('counted as Rephaim,' "
                        "Deuteronomy 2:11, 20). But in the poetic and prophetic "
                        "literature, the identical word means 'the dead' or 'shades' "
                        "who inhabit Sheol. Isaiah 14:9: 'Sheol beneath is stirred "
                        "up to meet you when you come; it rouses the Rephaim to "
                        "greet you.' Isaiah 26:14: 'They are dead, they will not "
                        "live; they are Rephaim, they will not arise.' The Hebrew "
                        "language itself connects these giant clans to the realm "
                        "of death. Anak (\u05e2\u05b2\u05e0\u05b8\u05e7) likely means 'long-necked' or 'giant,' "
                        "and the Anakim are always presented as a sub-clan: 'sons "
                        "of Anak, who come from the Nephilim.' The taxonomy is "
                        "precise. The linguistic connections are intentional."
            },
            # --- TIER C: FULL PICTURE ---
            {
                "heading": "Why Were They Still There?",
                "tier": "c",
                "body": "[C] The post-Flood presence of Nephilim raises one of the "
                        "most debated questions in biblical scholarship: how did "
                        "Nephilim survive the Flood? Three proposals have been "
                        "advanced. First, a second incursion \u2014 Genesis 6:4 says "
                        "the Nephilim were on the earth 'in those days, and also "
                        "afterward,' which some read as indicating additional "
                        "boundary violations after the Flood. Second, genetic "
                        "survival through Noah's daughters-in-law, who were not "
                        "of Noah's own bloodline ('Noah was a righteous man, "
                        "blameless in his generation,' Genesis 6:9 \u2014 where "
                        "'blameless,' tamim, can mean 'complete' or 'unblemished'). "
                        "Third, 'Nephilim' as a category term applied to any "
                        "offspring of divine-human union. According to 1 Enoch "
                        "15:8-10, the disembodied spirits of dead Nephilim became "
                        "evil spirits upon the earth: 'But now the giants who are "
                        "born from the spirits and the flesh shall be called evil "
                        "spirits upon the earth.' The Flood killed their bodies. "
                        "According to 1 Enoch, the spirits remain."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 3: JOSHUA'S CAMPAIGN -- Joshua 11:21-22
    # =========================================================================
    {
        "id": "nephilim-story-joshua-campaign",
        "ref": "Joshua 11:21-22; 14:12-15; 15:13-14",
        "chapter_num": 3,
        "title": "Joshua's Campaign \u2014 Joshua 11:21\u201322",
        "era": "nephilim_story",
        "type": "chapter",

        "synopsis": "Joshua did not conquer Canaan at random. The text reveals a "
                    "systematic campaign to eliminate the Anakim \u2014 the giant clan "
                    "descended from the Nephilim \u2014 from every stronghold in the "
                    "hill country. Joshua cleared them from Hebron, from Debir, "
                    "from Anab, from all the hill country of Judah and Israel. "
                    "But three Philistine cities were left untouched: Gaza, Gath, "
                    "and Ashdod. The giants survived there. Gath will matter in "
                    "the next chapter.",

        "key_verse": {
            "ref": "Joshua 11:21-22",
            "text": "And Joshua came at that time and cut off the Anakim from "
                    "the hill country, from Hebron, from Debir, from Anab, and "
                    "from all the hill country of Judah, and from all the hill "
                    "country of Israel. Joshua devoted them to destruction with "
                    "their cities. There was none of the Anakim left in the land "
                    "of the people of Israel. Only in Gaza, in Gath, and in "
                    "Ashdod did some remain.",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "cherem",
                "hebrew": "\u05d7\u05b5\u05e8\u05b6\u05dd",
                "meaning": "'The ban' \u2014 total destruction devoted to YHWH. Everything "
                           "under the cherem belongs irrevocably to God and must be "
                           "completely destroyed. This is not standard warfare. It is "
                           "sacred elimination. The same root (ch-r-m) connects to "
                           "Mount Hermon (\u05d7\u05e8\u05de\u05d5\u05df), where according to 1 Enoch the "
                           "Watchers swore their oath. The place of the oath and the "
                           "judgment of the oath share a linguistic root.",
                "verse": "Joshua 11:21"
            },
            {
                "term": "anakim",
                "hebrew": "\u05e2\u05b2\u05e0\u05b8\u05e7\u05b4\u05d9\u05dd",
                "meaning": "The giant clan Joshua specifically targeted. Descended "
                           "from Anak son of Arba. Arba was 'the greatest man among "
                           "the Anakim' (Joshua 14:15). Hebron was originally named "
                           "Kiriath-arba \u2014 'City of Arba' \u2014 a giant's city that "
                           "Israel would reclaim.",
                "verse": "Joshua 11:21"
            },
            {
                "term": "Arba",
                "hebrew": "\u05d0\u05b7\u05e8\u05b0\u05d1\u05b7\u05bc\u05e2",
                "meaning": "The patriarch of the Anakim. His name means 'four,' "
                           "possibly indicating a fourfold nature or a clan of "
                           "four. Joshua 14:15 calls him 'the greatest man among "
                           "the Anakim.' Hebron bore his name (Kiriath-arba) until "
                           "Israel reclaimed it.",
                "verse": "Joshua 14:15"
            },
            {
                "term": "karat",
                "hebrew": "\u05db\u05b8\u05bc\u05e8\u05b7\u05ea",
                "meaning": "'To cut off, to eliminate.' The verb used for Joshua's "
                           "campaign against the Anakim. Not merely 'to defeat' but "
                           "'to cut off' \u2014 a word used for covenant-cutting and for "
                           "complete removal. The Anakim were not just conquered; "
                           "they were excised.",
                "verse": "Joshua 11:21"
            }
        ],

        "ane_backdrop": "The practice of total warfare dedicated to a deity (cherem "
                        "in Hebrew, equivalent concepts in the Moabite Mesha Stele "
                        "where King Mesha describes devoting Israelite towns to his "
                        "god Chemosh) was known across the ancient Near East. The "
                        "Mesha Stele (c. 840 BC) uses nearly identical language to "
                        "describe Moab's cherem against Israel as the Bible uses for "
                        "Israel's cherem against the Canaanite giants. The concept "
                        "was not unique to Israel, but the theological rationale was: "
                        "Israel's cherem targeted specific populations connected to "
                        "the Nephilim legacy.",

        "second_temple": [
            {
                "source": "Jubilees 29:9-11",
                "summary": "According to Jubilees, the giant clans occupying "
                           "Canaan are explicitly connected to the antediluvian "
                           "Nephilim, maintaining the link between the pre-Flood "
                           "rebellion and post-Flood conquest.",
                "relevance": "Confirms the Second Temple understanding that the "
                             "Conquest was not merely political but part of the "
                             "ongoing war against the Watcher legacy."
            },
            {
                "source": "Wisdom of Solomon 14:6",
                "summary": "References the 'proud giants' who perished in the "
                           "Flood, maintaining the connection between the "
                           "antediluvian Nephilim and divine judgment.",
                "relevance": "Another witness to the widespread Second Temple "
                             "understanding of the giants as targets of divine "
                             "judgment."
            }
        ],

        "cross_refs": [
            {"ref": "Joshua 11:21-22", "note": "Joshua cuts off the Anakim from the hill country; remnant survives in Gaza, Gath, Ashdod", "type": "ot"},
            {"ref": "Joshua 14:12-15", "note": "Caleb requests Hebron and drives out the three sons of Anak: Sheshai, Ahiman, Talmai", "type": "ot"},
            {"ref": "Joshua 15:13-14", "note": "Caleb took Hebron (Kiriath-arba) and drove out the three Anakim sons", "type": "ot"},
            {"ref": "Numbers 13:22", "note": "The spies saw Ahiman, Sheshai, and Talmai, descendants of Anak, at Hebron", "type": "ot"},
            {"ref": "Deuteronomy 9:1-2", "note": "'Who can stand before the sons of Anak?' \u2014 Israel's fear before the campaign", "type": "ot"},
            {"ref": "Genesis 3:15", "note": "The protoevangelium \u2014 seed of the woman vs. seed of the serpent, the war behind the war", "type": "ot"},
            {"ref": "1 Enoch 10:11-12", "note": "According to 1 Enoch, God commanded the destruction of the Watchers' offspring", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "Joshua's campaign against the Anakim is, in the divine "
                               "council framework, the continuation of a cosmic war. "
                               "The cherem (\u05d7\u05b5\u05e8\u05b6\u05dd) applied to the Anakim is not ordinary "
                               "warfare \u2014 it is sacred destruction mandated by YHWH against "
                               "the physical legacy of rebel council members. The fact "
                               "that Joshua systematically targeted Anakim territory and "
                               "that the text carefully notes where survivors remained "
                               "(Gaza, Gath, Ashdod) shows this was a strategic operation "
                               "with a specific objective: eliminate the corrupted "
                               "bloodline. The incomplete elimination will have "
                               "consequences \u2014 Gath produces Goliath.",

        "sections": [
            # --- TIER A: CANON ONLY ---
            {
                "heading": "The Anakim Campaign",
                "tier": "a",
                "body": "[A] Joshua 11:21-22 summarizes an entire military campaign "
                        "in two verses: 'And Joshua came at that time and cut off "
                        "the Anakim from the hill country, from Hebron, from Debir, "
                        "from Anab, and from all the hill country of Judah, and "
                        "from all the hill country of Israel. Joshua devoted them "
                        "to destruction with their cities. There was none of the "
                        "Anakim left in the land of the people of Israel. Only in "
                        "Gaza, in Gath, and in Ashdod did some remain' (ESV). Note "
                        "the language: Joshua 'cut off' the Anakim. He 'devoted them "
                        "to destruction' \u2014 the cherem, the sacred ban. This was not "
                        "ordinary conquest. It was targeted elimination of a specific "
                        "population that God mandated for complete removal. And the "
                        "text carefully notes where the job was left incomplete."
            },
            {
                "heading": "Three Philistine Cities",
                "tier": "a",
                "body": "[A] The three cities where Anakim survived \u2014 Gaza, Gath, "
                        "and Ashdod \u2014 are all Philistine cities. The Philistines "
                        "were sea peoples who settled the coastal plain, and their "
                        "territory became a refuge for the giant remnant. The text "
                        "notes this detail with the precision of an unfinished "
                        "mission report: the hill country is clear, but the coast "
                        "is not. Gath in particular will become the most significant "
                        "of these three cities. It is from Gath that a champion "
                        "will emerge, four centuries later, to challenge the armies "
                        "of the living God. The Bible is connecting dots across "
                        "hundreds of years. The reader is expected to remember: "
                        "the Anakim survived in Gath."
            },
            # --- TIER B: HEBREW ANALYSIS ---
            {
                "heading": "Cherem Warfare \u2014 The Ban",
                "tier": "b",
                "body": "[B] The Hebrew word cherem (\u05d7\u05b5\u05e8\u05b6\u05dd) governs Joshua's campaign "
                        "against the Anakim. It means 'devoted to destruction' \u2014 "
                        "everything under the ban belongs irrevocably to YHWH and "
                        "must be completely annihilated. No plunder. No survivors. "
                        "No negotiation. This was not standard ANE warfare where "
                        "conquest meant subjugation, tribute, and absorption. "
                        "Cherem was sacred elimination. But notice the linguistic "
                        "connection that most readers miss: the root ch-r-m (\u05d7\u05e8\u05dd) "
                        "is shared with Mount Hermon (\u05d7\u05e8\u05de\u05d5\u05df), where according to "
                        "1 Enoch 6:6 the Watchers swore their oath of rebellion. "
                        "The place-name Hermon derives from 'oath' or 'devoted "
                        "thing.' The same linguistic root that names the site of "
                        "the Watchers' transgression now governs the judgment "
                        "against their offspring. The oath and its consequence "
                        "share a single Hebrew root."
            },
            {
                "heading": "The Strategic Pattern",
                "tier": "b",
                "body": "[B] Map Joshua's campaign geographically and a pattern "
                        "emerges. He begins in the hill country \u2014 the interior "
                        "highlands where the Anakim were concentrated. Hebron "
                        "first: this was Kiriath-arba, 'City of Arba,' the "
                        "ancestral capital of the Anakim. Arba was 'the greatest "
                        "man among the Anakim' (Joshua 14:15). Three sons of Anak "
                        "held the city: Sheshai, Ahiman, and Talmai (Numbers 13:22; "
                        "Joshua 15:14). Joshua and Caleb took the capital, then "
                        "Debir, then Anab, then the entire hill country of Judah "
                        "and Israel. The campaign radiated outward from the Anakim "
                        "stronghold, pushing the remnant toward the coastal plain "
                        "\u2014 Philistine territory where Israel's mandate did not yet "
                        "extend. This was not random warfare. It was systematic "
                        "clearance of Nephilim-descended populations from the "
                        "territory YHWH had reserved for His people."
            },
            # --- TIER C: FULL PICTURE ---
            {
                "heading": "The Cosmic Background",
                "tier": "c",
                "body": "[C] In the divine council framework, cherem warfare against "
                        "the Anakim connects to the seed war announced in Genesis "
                        "3:15. The 'seed of the woman' \u2014 the messianic line running "
                        "through Seth, Noah, Shem, Abraham, Judah, and David \u2014 must "
                        "be preserved. The Nephilim-descended giant clans occupying "
                        "the Promised Land represent a physical threat to that line. "
                        "According to the broader Second Temple understanding, these "
                        "clans were the legacy of the Watcher rebellion described in "
                        "1 Enoch 6-16. Their elimination was part of God's program "
                        "to secure the territory and the bloodline through which the "
                        "'seed of the woman' would come. The three Philistine cities "
                        "where Anakim remained (Gaza, Gath, Ashdod) become future "
                        "battlegrounds precisely because the cherem was incomplete "
                        "there. The Nephilim narrative is not a subplot \u2014 it is the "
                        "physical dimension of a cosmic war that stretches from "
                        "Genesis 3:15 to the cross."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 4: DAVID VS GOLIATH -- 1 Samuel 17
    # =========================================================================
    {
        "id": "nephilim-story-david-goliath",
        "ref": "1 Samuel 17",
        "chapter_num": 4,
        "title": "David vs. Goliath \u2014 1 Samuel 17",
        "era": "nephilim_story",
        "type": "chapter",

        "synopsis": "Everyone knows the story. Almost no one reads it correctly. "
                    "Goliath is not a random tall Philistine. He is from Gath \u2014 "
                    "one of the three cities where the Anakim remnant survived "
                    "after Joshua's campaign (Joshua 11:22). He stands over nine "
                    "feet tall, wears armor that weighs more than an average man, "
                    "and challenges the armies of the living God for forty days. "
                    "David's response invokes not just courage but a specific "
                    "divine title: YHWH Tsevaot, the LORD of the heavenly armies. "
                    "A shepherd boy calls on the divine council against the last "
                    "son of the Watchers' legacy.",

        "key_verse": {
            "ref": "1 Samuel 17:45",
            "text": "Then David said to the Philistine, \u201cYou come to me with a "
                    "sword and with a spear and with a javelin, but I come to "
                    "you in the name of the LORD of hosts, the God of the "
                    "armies of Israel, whom you have defied.\u201d",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "YHWH Tsevaot",
                "hebrew": "\u05d9\u05d4\u05d5\u05d4 \u05e6\u05b0\u05d1\u05b8\u05d0\u05d5\u05b9\u05ea",
                "meaning": "'LORD of Hosts' or 'LORD of Armies.' The tsevaot "
                           "(\u05e6\u05b0\u05d1\u05b8\u05d0\u05d5\u05b9\u05ea) are the heavenly host \u2014 the loyal members of "
                           "God's divine council in their military capacity. This "
                           "is not a generic title for God's power. It specifically "
                           "invokes the heavenly army against an earthly enemy. "
                           "David is not fighting alone; he is calling in the "
                           "divine military.",
                "verse": "1 Samuel 17:45"
            },
            {
                "term": "ish habbenayim",
                "hebrew": "\u05d0\u05b4\u05d9\u05e9\u05c1 \u05d4\u05b7\u05d1\u05b5\u05bc\u05e0\u05b7\u05d9\u05b4\u05dd",
                "meaning": "'Man of the between' \u2014 the term used for Goliath's "
                           "role as champion. He stands in the space between the "
                           "two armies. The word implies a representative combatant "
                           "whose fight decides the outcome for both sides. In "
                           "ANE warfare, such champions often had cultic or "
                           "semi-divine status.",
                "verse": "1 Samuel 17:4"
            },
            {
                "term": "golyat",
                "hebrew": "\u05d2\u05b8\u05bc\u05dc\u05b0\u05d9\u05b8\u05ea",
                "meaning": "Goliath. The name may derive from a root meaning 'to "
                           "exile' or 'to uncover.' Some scholars connect it to "
                           "the Anatolian/Lydian name Alyattes or the Indo-European "
                           "root *wal- (ruler). Whatever the etymology, Goliath "
                           "is identified as being 'of Gath' \u2014 the city where "
                           "the Anakim survived (Joshua 11:22).",
                "verse": "1 Samuel 17:4"
            },
            {
                "term": "chazaq",
                "hebrew": "\u05d7\u05b8\u05d6\u05b7\u05e7",
                "meaning": "'To be strong, to prevail, to overpower.' David "
                           "'prevailed' (vayechezaq) over the Philistine with "
                           "a sling and a stone (1 Samuel 17:50). The same root "
                           "is used for God strengthening His servants \u2014 the "
                           "victory is divine enablement, not human power.",
                "verse": "1 Samuel 17:50"
            }
        ],

        "ane_backdrop": "Representative combat between champions was a recognized "
                        "practice in the ancient Near East and the broader Mediterranean "
                        "world. The Iliad's duel between Achilles and Hector follows "
                        "the same pattern: a champion from each side determines the "
                        "outcome. In ANE royal ideology, the king or champion often "
                        "embodied divine power \u2014 Goliath's challenge to Israel is "
                        "implicitly a challenge from the Philistine gods (Dagon) to "
                        "YHWH. David's response makes this explicit: he comes not in "
                        "his own name but in the name of YHWH Tsevaot.",

        "second_temple": [
            {
                "source": "2 Samuel 21:15-22",
                "summary": "Four additional Philistine giants are killed by David's "
                           "men: Ishbi-benob, Saph, the brother of Goliath (Lahmi, "
                           "per 1 Chronicles 20:5), and a giant with six fingers on "
                           "each hand and six toes on each foot. All four are 'born "
                           "to the giant in Gath.'",
                "relevance": "Confirms that Goliath was not unique \u2014 Gath produced "
                             "multiple giants. The polydactyly (extra fingers/toes) "
                             "suggests genetic anomaly consistent with hybrid origin."
            },
            {
                "source": "Sirach 47:4-5",
                "summary": "According to Sirach (Ecclesiasticus), David 'in his "
                           "youth slew a giant and took away the people's disgrace, "
                           "when he whirled the stone in the sling and struck down "
                           "the boasting Goliath.'",
                "relevance": "Second Temple reception of the David-Goliath encounter, "
                             "preserving the tradition that Goliath was a 'giant' "
                             "in the technical sense."
            },
            {
                "source": "Targum Pseudo-Jonathan on 1 Samuel 17:4",
                "summary": "The Aramaic targum identifies Goliath as descended from "
                           "the giant clans, connecting him to the broader Nephilim "
                           "tradition.",
                "relevance": "Demonstrates that later Jewish interpretation maintained "
                             "the connection between Goliath and the antediluvian "
                             "giant tradition."
            }
        ],

        "cross_refs": [
            {"ref": "1 Samuel 17:4", "note": "Goliath of Gath, six cubits and a span (~9 feet 9 inches), full armor description", "type": "ot"},
            {"ref": "1 Samuel 17:45", "note": "David invokes YHWH Tsevaot \u2014 the LORD of the heavenly armies", "type": "ot"},
            {"ref": "1 Samuel 17:50-51", "note": "David prevails with sling and stone, then beheads Goliath with his own sword", "type": "ot"},
            {"ref": "Joshua 11:22", "note": "Anakim remained 'only in Gaza, in Gath, and in Ashdod' \u2014 Goliath is FROM Gath", "type": "ot"},
            {"ref": "2 Samuel 21:15-22", "note": "Four more giants from Gath killed by David's men \u2014 Gath was a giant stronghold", "type": "ot"},
            {"ref": "1 Chronicles 20:4-8", "note": "Parallel account: giants of Gath killed, including one with six fingers per hand", "type": "ot"},
            {"ref": "Genesis 3:15", "note": "Seed of the woman shall crush the serpent's head \u2014 David crushing the giant's head echoes the pattern", "type": "ot"},
            {"ref": "Psalm 82:1", "note": "God stands in the divine assembly \u2014 the council whose army David invokes with 'YHWH Tsevaot'", "type": "ot"},
            {"ref": "Colossians 2:15", "note": "Christ disarming rulers and authorities \u2014 the ultimate defeat of the powers behind the giants", "type": "nt"}
        ],

        "divine_council_note": "David's invocation of YHWH Tsevaot (\u05d9\u05d4\u05d5\u05d4 \u05e6\u05b0\u05d1\u05b8\u05d0\u05d5\u05b9\u05ea) is "
                               "not a devotional exclamation \u2014 it is a battlefield "
                               "identification of his commanding officer. The tsevaot "
                               "are the heavenly host in military formation: the loyal "
                               "members of God's divine council arrayed for war. A "
                               "shepherd boy with a sling invokes the heavenly army "
                               "against a descendant of the beings who violated the "
                               "boundary between heaven and earth. Goliath represents "
                               "physical armor, human military power, the legacy of "
                               "the second rebellion. David represents the seed line \u2014 "
                               "the messianic ancestry through which the ultimate "
                               "serpent-crusher will come. The giant falls. The head "
                               "is taken. The pattern of Genesis 3:15 echoes forward.",

        "sections": [
            # --- TIER A: CANON ONLY ---
            {
                "heading": "The Champion of Gath",
                "tier": "a",
                "body": "[A] 'And there came out from the camp of the Philistines "
                        "a champion named Goliath of Gath, whose height was six "
                        "cubits and a span' (1 Samuel 17:4, ESV). That is roughly "
                        "nine feet nine inches. His coat of mail weighed five "
                        "thousand shekels of bronze \u2014 approximately 125 pounds. The "
                        "head of his spear alone weighed six hundred shekels of iron "
                        "\u2014 about 15 pounds. A shield-bearer walked before him. For "
                        "forty days, morning and evening, this giant stood between "
                        "the armies and issued his challenge: 'Choose a man for "
                        "yourselves, and let him come down to me. If he is able to "
                        "fight with me and kill me, then we will be your servants' "
                        "(17:8-9). Saul and all Israel 'were dismayed and greatly "
                        "afraid' (17:11). For forty days, nobody moved."
            },
            {
                "heading": "In the Name of the LORD of Hosts",
                "tier": "a",
                "body": "[A] David's answer to Goliath is the theological center of "
                        "the story: 'You come to me with a sword and with a spear "
                        "and with a javelin, but I come to you in the name of the "
                        "LORD of hosts, the God of the armies of Israel, whom you "
                        "have defied' (1 Samuel 17:45, ESV). David then runs toward "
                        "Goliath, slings a stone that sinks into the giant's "
                        "forehead, and Goliath falls face down to the earth. David "
                        "takes Goliath's own sword and cuts off his head (17:51). "
                        "The Philistines flee. The victory is total. Note the "
                        "sequence: David declares the divine name, the stone strikes "
                        "the head, the giant falls on his face, and the head is "
                        "severed. David does not claim personal courage or skill. He "
                        "claims a Name."
            },
            # --- TIER B: HEBREW ANALYSIS ---
            {
                "heading": "YHWH Tsevaot \u2014 The Divine Army",
                "tier": "b",
                "body": "[B] The name David invokes is YHWH Tsevaot (\u05d9\u05d4\u05d5\u05d4 \u05e6\u05b0\u05d1\u05b8\u05d0\u05d5\u05b9\u05ea), "
                        "translated 'LORD of Hosts' or 'LORD of Armies.' This is "
                        "not a generic title. The tsevaot (\u05e6\u05b0\u05d1\u05b8\u05d0\u05d5\u05b9\u05ea) in divine "
                        "council theology refers to the heavenly host \u2014 the loyal "
                        "members of God's council in their military capacity. When "
                        "Joshua met the 'commander of the army of YHWH' (Joshua "
                        "5:14), he encountered the visible leader of this heavenly "
                        "force. When Elisha prayed that his servant's eyes would be "
                        "opened, the servant saw 'horses and chariots of fire all "
                        "around' (2 Kings 6:17) \u2014 the tsevaot in visible form. "
                        "David, standing before a nine-foot descendant of the "
                        "Watchers' offspring, does not call on his own strength. "
                        "He calls on the divine army \u2014 the loyal council members "
                        "who did <em>not</em> rebel, arrayed against the physical "
                        "legacy of those who did."
            },
            {
                "heading": "From Gath \u2014 The Last Giant City",
                "tier": "b",
                "body": "[B] The text identifies Goliath as being 'of Gath' "
                        "(1 Samuel 17:4). This is not incidental geographic detail. "
                        "Joshua 11:22 told us precisely where the Anakim survived "
                        "after Joshua's campaign: 'Only in Gaza, in Gath, and in "
                        "Ashdod did some remain.' Goliath is from the city where "
                        "the Nephilim remnant was explicitly noted as surviving. He "
                        "is not a random tall man. He is a product of the unfinished "
                        "cherem \u2014 the incomplete ban that left Anakim alive in "
                        "Philistine territory. Furthermore, 2 Samuel 21:15-22 "
                        "records <em>four more giants</em> from Gath, including one "
                        "with six fingers on each hand and six toes on each foot "
                        "(21:20). Gath was not a city that happened to produce one "
                        "large man. It was a giant stronghold \u2014 the last refuge "
                        "of the Anakim that Joshua's campaign failed to reach. The "
                        "Bible connects these dots deliberately across hundreds of "
                        "pages. The question is whether we are reading carefully "
                        "enough to follow the thread."
            },
            # --- TIER C: FULL PICTURE ---
            {
                "heading": "The Genesis 3:15 Echo",
                "tier": "c",
                "body": "[C] David's beheading of Goliath echoes the language of "
                        "Genesis 3:15 \u2014 the protoevangelium, where God declares "
                        "that the seed of the woman will 'crush' (shuph) the head "
                        "of the serpent. David, an ancestor of Christ and a carrier "
                        "of the messianic seed, strikes the head of a giant "
                        "descended from the beings who violated the boundary between "
                        "heaven and earth. The head falls. But theological precision "
                        "matters: the Nephilim are the legacy of the SECOND rebellion "
                        "(Hermon/Watchers, Genesis 6:1-4), not the FIRST (Eden/"
                        "Nachash, Genesis 3). The three rebellions \u2014 Eden, Hermon, "
                        "Babel \u2014 are independent events with independent actors. "
                        "David's victory echoes Genesis 3:15 typologically: the "
                        "seed of the woman crushing the head of a cosmic enemy. But "
                        "it does not collapse the three rebellions into a single "
                        "chain. The echo is thematic, not genealogical. Both involve "
                        "a human agent empowered by God defeating a representative "
                        "of cosmic evil. The ultimate fulfillment awaits David's "
                        "greater Son, who will disarm 'the rulers and authorities' "
                        "entirely (Colossians 2:15)."
            }
        ]
    }
]

# ── Append Chapters 5-7 ──────────────────────────────────────
import os as _os, importlib.util as _ilu
_here = _os.path.dirname(_os.path.abspath(__file__))
_spec = _ilu.spec_from_file_location("ch57", _os.path.join(_here, "chapters_5_7.py"))
_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
for _ch in _mod.CHAPTERS_5_7:
    for _sec in _ch.get("sections", []):
        if "tier" in _sec:
            _sec["tier"] = _sec["tier"].lower()
CHAPTERS.extend(_mod.CHAPTERS_5_7)
del _os, _ilu, _here, _spec, _mod, _ch, _sec
