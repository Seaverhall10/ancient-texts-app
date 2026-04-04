"""
era_columns.py — The Genesis Apocryphon (1QapGen / 1Q20)

The Genesis Apocryphon is an Aramaic scroll discovered in Cave 1 at Qumran,
one of the original seven Dead Sea Scrolls purchased by E.L. Sukenik and
Mar Athanasius Yeshue Samuel in 1947-1948. It was the last of the seven
to be unrolled (1956, by James Biberkraut under Nahman Avigad and Yigael
Yadin's direction) due to its severe deterioration. The scroll preserves
a retelling of Genesis in first-person Aramaic narrative, expanding the
biblical text with haggadic material, dialogue, and geographic detail.

Only columns II through XXII survive in readable condition, with many
columns (especially VI-XVIII) extremely fragmentary. The preserved text
covers three narrative cycles:

  II-V     — Lamech's narrative: suspicion about Noah's birth, Bitenosh's
             oath, consultation with Methuselah and Enoch
  VI-XVII  — Noah narrative (very fragmentary): the Flood, sacrifice,
             covenant, division of the earth among Noah's sons
  XIX-XXII — Abraham cycle: entry into Canaan, sojourn in Egypt, Sarah
             before Pharaoh, Lot's separation, war of the kings,
             Melchizedek

The scroll is written in a literary Aramaic closely related to the
language of Daniel, the Targumim, and the other Aramaic scrolls from
Qumran. Its date of composition is debated: paleography suggests the
manuscript was copied in the late 1st century BC or early 1st century AD,
but the composition may be earlier (2nd-1st century BC). The text is
significant for several reasons: it demonstrates how Second Temple Jews
rewrote and expanded biblical narrative; it preserves the Watcher tradition
in a form independent of 1 Enoch; and it contains the oldest known
extended Aramaic prose narrative outside the biblical Aramaic of
Daniel and Ezra.

Editio princeps: N. Avigad and Y. Yadin, A Genesis Apocryphon (1956).
Major editions: J.A. Fitzmyer, The Genesis Apocryphon of Qumran Cave I
(1st ed. 1966, 2nd ed. 1971, 3rd ed. 2004). D. Machiela, The Dead Sea
Genesis Apocryphon: A New Text and Translation with Introduction and
Special Treatment of Columns 13-17 (STDJ 79, 2009).
"""

CHAPTERS = [
    # =========================================================================
    # HISTORICAL INSERT: DISCOVERY AND PHYSICAL CONDITION
    # =========================================================================
    {
        "id": "insert-apoc-discovery",
        "ref": "Historical Context",
        "chapter_num": None,
        "title": "The Genesis Apocryphon — Discovery, Unrolling, and Physical Condition",
        "era": "apocryphon_columns",
        "type": "historical_insert",

        "synopsis": "The Genesis Apocryphon (1Q20) is one of the original seven Dead "
                    "Sea Scrolls recovered from Cave 1 at Qumran in 1947. It was the "
                    "most badly deteriorated of the seven and the last to be opened, "
                    "remaining sealed for nearly a decade after its discovery. When "
                    "finally unrolled in 1956, large portions had fused together or "
                    "crumbled to dust. Its tortured physical history has shaped — and "
                    "limited — scholarship on the text ever since. Initially called "
                    "'the Lamech Scroll' from fragments of the outer surface, it was "
                    "only upon unrolling that its true scope — a first-person Aramaic "
                    "retelling of Genesis from Lamech through Abraham — became apparent.",

        "key_verse": {
            "ref": "Genesis 5:28-29",
            "text": "When Lamech had lived 182 years, he fathered a son and called his name Noah, saying, 'Out of the ground that the LORD has cursed, this one shall bring us relief from our work and from the painful toil of our hands.'",
            "translation": "ESV"
        },
        "original_terms": [],
        "ane_backdrop": None,
        "second_temple": [],

        "cross_refs": [
            {"ref": "1Q20 (1QapGen)", "type": "dss", "note": "The official Qumran designation for the Genesis Apocryphon. 1Q = Cave 1; 20 = the twentieth text catalogued from that cave. Also designated 1QapGen in older literature."},
            {"ref": "1QIsaiah-a (1QIsa-a)", "type": "dss", "note": "The Great Isaiah Scroll, another of the original seven Cave 1 scrolls. Its excellent preservation contrasts sharply with the Apocryphon's deterioration and illustrates the range of conditions in Cave 1."},
            {"ref": "1QS (Community Rule)", "type": "dss", "note": "Another of the original seven scrolls, acquired alongside the Apocryphon by Mar Athanasius Yeshue Samuel of St. Mark's Monastery."},
            {"ref": "Genesis 5-6", "type": "ot", "note": "The canonical text that columns II-V retell and expand, adding Lamech's suspicion, Bitenosh's oath, and the Enoch consultation — none of which appears in Genesis."},
            {"ref": "Genesis 12-14", "type": "ot", "note": "The canonical Abraham narratives retold in columns XIX-XXII with elaborate expansions: the dream-warning, the Beauty Hymn, the pestilential spirit, geographic surveys, and the Melchizedek encounter."},
            {"ref": "1 Enoch 106-107", "type": "pseudepigrapha", "note": "The 'Birth of Noah' appendix to 1 Enoch, which tells the same story of Lamech's fear about Noah's birth from a different literary perspective. The Genesis Apocryphon and 1 Enoch 106-107 likely draw on a common source."}
        ],

        "divine_council_note": "The Genesis Apocryphon's Lamech narrative presupposes "
                               "the Watcher theology of 1 Enoch as established fact. "
                               "Lamech's fear that his son was fathered by a Watcher is "
                               "intelligible only in a world where the descent of the "
                               "b'nei 'elohim and their interbreeding with human women is "
                               "common knowledge. The scroll thus witnesses to the "
                               "widespread acceptance of the divine council rebellion "
                               "tradition in Second Temple Judaism — it is not argued "
                               "or defended, merely assumed as the backdrop against "
                               "which family drama unfolds.",

        "sections": [
            {
                "heading": "Discovery and Acquisition (1947-1954)",
                "body": "In late 1946 or early 1947, three Bedouin shepherds of the "
                        "Ta'amireh tribe discovered a cache of scrolls in a cave above "
                        "Wadi Qumran on the northwestern shore of the Dead Sea. Seven "
                        "major scrolls were recovered from what came to be known as "
                        "Cave 1. Four were acquired by Mar Athanasius Yeshue Samuel, "
                        "the Syrian Orthodox Metropolitan of Jerusalem, including a "
                        "tightly rolled scroll that could not be identified. Three "
                        "others were purchased by Eleazar Lipa Sukenik of the Hebrew "
                        "University. The unidentified scroll in Samuel's possession — "
                        "which he initially called the 'Lamech Scroll' based on a "
                        "fragment that had broken off — was in appalling condition: "
                        "blackened, brittle, and fused into a solid mass in many "
                        "places. Multiple layers had adhered together, and the outer "
                        "columns had rotted away entirely. It was clearly Aramaic, but "
                        "no one could read it without unrolling it, and no one dared "
                        "attempt unrolling without risking total destruction. When "
                        "Samuel brought his four scrolls to the United States in 1949, "
                        "the Lamech Scroll remained sealed. After the Israeli government "
                        "purchased all four of Samuel's scrolls in 1954 (through an "
                        "intermediary responding to a Wall Street Journal advertisement), "
                        "the scroll was transferred to Jerusalem."
            },
            {
                "heading": "The Unrolling (1956)",
                "body": "In 1956, the conservator James Biberkraut undertook the "
                        "painstaking task of unrolling the scroll under the supervision "
                        "of Nahman Avigad and Yigael Yadin. The process was agonizingly "
                        "slow. Biberkraut used a combination of controlled humidity and "
                        "careful mechanical separation to peel apart the fused layers. "
                        "Large sections disintegrated during the process. Column I was "
                        "entirely lost. Columns II-V were recovered in readable "
                        "condition, though with significant lacunae. Columns VI-XVIII "
                        "were catastrophically damaged — in many columns only a few "
                        "words per line survived, and some columns were reduced to "
                        "scattered fragments. Columns XIX-XXII, from the inner portion "
                        "of the scroll, were the best preserved, yielding continuous "
                        "readable text. Avigad and Yadin published the editio princeps "
                        "in 1956, releasing columns II, XIX-XXII. The fragmentary "
                        "middle columns were published later by Fitzmyer (1966, 1971) "
                        "and comprehensively by Machiela (2009). Infrared photography "
                        "and later multispectral imaging have recovered additional "
                        "readings from the damaged columns, but large portions remain "
                        "irrecoverably lost."
            },
            {
                "heading": "Date, Language, and Literary Character",
                "body": "Paleographic analysis places the manuscript's copying in the "
                        "late 1st century BC or early 1st century AD (Herodian period). "
                        "The composition date is earlier, likely 2nd or 1st century BC, "
                        "based on linguistic features and the text's relationship to "
                        "other Second Temple literature. The Aramaic is literary and "
                        "polished, closely related to the language of Daniel 2-7 and "
                        "the Aramaic Levi Document. Key linguistic features include "
                        "the use of the emphatic state for definiteness, the ethpeel "
                        "reflexive conjugation, and vocabulary shared with the Targumim. "
                        "The Genesis Apocryphon belongs to the genre of 'Rewritten "
                        "Bible' (or 'Rewritten Scripture'), a category that includes "
                        "Jubilees, Pseudo-Philo's Biblical Antiquities, and Josephus's "
                        "Antiquities. These texts retell the biblical narrative with "
                        "expansions, harmonizations, and theological commentary woven "
                        "into the story itself. Unlike a commentary (pesher) that "
                        "quotes and then interprets, Rewritten Bible replaces the "
                        "biblical text with an expanded version that incorporates "
                        "interpretive traditions directly into the narrative flow. "
                        "The Apocryphon's distinctive feature is its use of first-person "
                        "narration: Lamech, Noah, and Abraham each tell their own "
                        "stories, transforming third-person Genesis into intimate "
                        "autobiography."
            }
        ]
    },

    # =========================================================================
    # COLUMN II: LAMECH'S FEAR
    # =========================================================================
    {
        "id": "apoc-col-2",
        "ref": "1QapGen Col. II",
        "chapter_num": 2,
        "title": "Lamech's Suspicion — Is Noah a Child of the Watchers?",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Column II opens with Lamech speaking in the first person. He "
                    "has just witnessed the birth of his son Noah, and the child's "
                    "extraordinary appearance fills him with dread. The baby's body "
                    "is white as snow and red as a rose, his hair white as wool, "
                    "and his eyes radiant. Lamech immediately suspects that the "
                    "child was not conceived by him but by one of the Watchers "
                    "(irin) or the Nephilim (nephilin). This is the earliest "
                    "known narrative that dramatizes a human father's terror at the "
                    "possibility that his wife has been impregnated by a divine being.",

        "key_verse": {
            "ref": "1QapGen II.1-2 (reconstructed)",
            "text": "Behold, I thought then within my heart that conception was "
                    "due to the Watchers and the Holy Ones... and to the Nephilim... "
                    "and my heart was troubled within me because of this child.",
            "translation": "Fitzmyer"
        },

        "original_terms": ["irin", "nephilin"],

        "ane_backdrop": "The motif of a hero's miraculous birth — accompanied by "
                        "extraordinary physical signs and parental anxiety — is "
                        "widespread in ancient Near Eastern and Mediterranean "
                        "literature. The births of Sargon of Akkad, Moses, and "
                        "later Perseus all feature elements of divine parentage, "
                        "unusual circumstances, and a father or authority figure's "
                        "fear. What distinguishes the Genesis Apocryphon is that the "
                        "'divine parentage' is not celebrated but dreaded: Lamech "
                        "fears that his son's father is a rebel angel, making Noah's "
                        "birth not a sign of divine favor but of cosmic contamination. "
                        "This inverts the typical ANE pattern and reflects the "
                        "distinctly Jewish horror at boundary-crossing between the "
                        "divine and human realms expressed in Genesis 6:1-4 and the "
                        "Watcher tradition.",

        "second_temple": [
            {
                "source": "1 Enoch 106:1-6",
                "summary": "The parallel account in the 'Birth of Noah' appendix to "
                           "1 Enoch describes the same scene: Noah's body is 'white as "
                           "snow and red as the blooming of a rose,' his hair 'white as "
                           "wool,' and when he opens his eyes the whole house glows. "
                           "Lamech is frightened and flees to Methuselah.",
                "relevance": "The verbal parallels between 1QapGen II and 1 Enoch 106 "
                             "are so close that both texts must depend on a common "
                             "source (possibly the lost Book of Noah). The Apocryphon "
                             "preserves a first-person Aramaic version; 1 Enoch 106 "
                             "preserves a third-person Ethiopic version. Together they "
                             "attest to a widely circulated Noah birth narrative in "
                             "Second Temple Judaism.",
                "canon": False
            },
            {
                "source": "Jubilees 4:28",
                "summary": "Jubilees notes that Lamech took a wife named Bitenosh "
                           "(also spelled Betenos), daughter of Baraki'el, providing "
                           "the genealogical framework assumed by the Apocryphon.",
                "relevance": "The name Bitenosh (Aramaic: 'daughter of man' or "
                             "'daughter of Enosh') is attested in both Jubilees and "
                             "the Apocryphon but not in canonical Genesis, indicating "
                             "a shared haggadic tradition about the wives of the "
                             "antediluvian patriarchs. Remarkably, Baraki'el also "
                             "appears in 1 Enoch 6:7 as one of the Watcher leaders, "
                             "adding a genealogical dimension to Lamech's anxiety.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 5:28-29", "type": "ot", "note": "The canonical account of Noah's birth: 'Lamech... fathered a son and called his name Noah, saying, This one shall comfort us.' No miraculous signs, no suspicion — the Apocryphon fills an enormous narrative gap."},
            {"ref": "Genesis 6:1-4", "type": "ot", "note": "The canonical backdrop: 'the sons of God saw that the daughters of man were attractive and took as their wives any they chose.' Lamech's fear in the Apocryphon is that this is exactly what happened to Bitenosh."},
            {"ref": "1 Enoch 106-107", "type": "pseudepigrapha", "note": "The parallel 'Birth of Noah' account: Lamech sees the miraculous child, flees to Methuselah, who consults Enoch. Enoch confirms Noah is Lamech's legitimate son and prophesies the coming Flood."},
            {"ref": "1 Enoch 6-11", "type": "pseudepigrapha", "note": "The Watcher descent narrative that provides the theological context for Lamech's fear. Without the tradition of angelic interbreeding in 1 Enoch 6-11, Lamech's suspicion makes no sense."},
            {"ref": "Revelation 1:14", "type": "nt", "note": "The glorified Christ is described with 'white hair, white like wool, like snow' — the same language used for the infant Noah. Whether deliberate allusion or shared apocalyptic vocabulary, the verbal overlap is striking."}
        ],

        "divine_council_note": "Column II is a domestic scene underwritten by cosmic "
                               "theology. Lamech's terror presupposes an entire worldview: "
                               "that members of the divine council (the Watchers/irin) "
                               "have violated their station by descending to earth and "
                               "fathering children with human women, that this "
                               "interbreeding produces beings of terrifying appearance, "
                               "and that any human husband might find himself unknowingly "
                               "raising a hybrid child. The text treats the Watcher "
                               "tradition not as a myth to be argued but as a lived "
                               "reality that causes genuine personal anguish. This is "
                               "the divine council rebellion as experienced from the "
                               "ground — not from Enoch's heavenly vantage point but "
                               "from the terrified perspective of an ordinary man.",

        "sections": [
            {
                "heading": "Noah's Miraculous Appearance (II.1-5)",
                "body": "The column begins mid-sentence (column I is entirely lost), "
                        "with Lamech recounting the birth of his son. The physical "
                        "description of the infant is extraordinary and alarming: his "
                        "body is white as snow (khiwar ki-talga) and red as a rose, "
                        "his hair is white as wool (amar), and his eyes are beautiful "
                        "and radiant. When Noah opens his eyes, the entire house is "
                        "illuminated as if by the sun. The same description appears in "
                        "1 Enoch 106:2, where the child's eyes are 'like the rays of "
                        "the sun' and his face 'glorious.' These are not merely "
                        "literary embellishments — they are signs of otherworldly "
                        "origin. In the Enochic worldview, luminosity is the hallmark "
                        "of heavenly beings (cf. the shining garments of the angels "
                        "in 1 Enoch 14:20, Daniel 10:6, and later the Transfiguration "
                        "in Matthew 17:2). A baby who glows is, to Lamech, evidence "
                        "that the child's father was not human."
            },
            {
                "heading": "Lamech's Accusation and Anguish (II.5-16)",
                "body": "Lamech's reaction is visceral. He does not celebrate the "
                        "birth but is seized with fear. The text uses the Aramaic "
                        "term dehilat (terror, dread) to describe his response. He "
                        "immediately suspects the Watchers (irin) and the Holy Ones "
                        "(qaddishin) — note the bitter irony that the rebel angels "
                        "retain the title 'holy ones' even in their transgression. "
                        "Lamech suspects that the Nephilim (nephilin) have had "
                        "intercourse with his wife Bitenosh. The Aramaic term "
                        "nephilin here is the same word that appears in the Aramaic "
                        "portions of 1 Enoch, establishing linguistic continuity "
                        "between the two texts. Lamech's heart is 'changed' "
                        "(eshtanni) within him — a term suggesting fundamental "
                        "disturbance, not merely worry. He is experiencing the "
                        "personal, familial dimension of the cosmic catastrophe "
                        "described in 1 Enoch 6-11. The Watcher rebellion is not "
                        "an abstract theological problem for Lamech; it is the "
                        "possible explanation for why his newborn son looks like "
                        "an angel."
            }
        ]
    },

    # =========================================================================
    # COLUMN III: BITENOSH'S OATH
    # =========================================================================
    {
        "id": "apoc-col-3",
        "ref": "1QapGen Col. III",
        "chapter_num": 3,
        "title": "Bitenosh's Oath of Innocence — The Wife's Defense",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Lamech confronts his wife Bitenosh (also spelled Bathenosh), "
                    "demanding to know whether the child was conceived by a Watcher. "
                    "Bitenosh swears a solemn oath of innocence, invoking 'the Most "
                    "High, the Lord, the Great One, the King of all the Ages' — a "
                    "remarkable string of divine titles. She insists that the seed "
                    "is Lamech's alone and recalls the specific occasion of "
                    "conception, appealing to his own memory of their intimacy. "
                    "This is one of the most remarkable scenes in all Second Temple "
                    "literature: a woman's voice defending her sexual fidelity in "
                    "first-person Aramaic speech.",

        "key_verse": {
            "ref": "1QapGen III.3-6 (reconstructed)",
            "text": "Then I, Bitenosh, your wife, swore to you by the Great Holy "
                    "One, the King of the hea[vens]... I swear to you that this "
                    "seed is from you, and this pregnancy is from you, and from "
                    "you is the planting of [this] fruit... and not from any "
                    "stranger or from any of the Watchers or from any of the "
                    "Sons of Heav[en].",
            "translation": "Fitzmyer"
        },

        "original_terms": ["irin", "bene_shemayin"],

        "ane_backdrop": "Bitenosh's oath of sexual fidelity has parallels in ancient "
                        "Near Eastern legal practice. The oath of purgation — where an "
                        "accused woman swears her innocence before the deity — is "
                        "attested in the Laws of Hammurabi (sections 131-132) and in "
                        "the biblical ordeal of the suspected adulteress (Numbers "
                        "5:11-31, the sotah ritual). In both ANE legal tradition and "
                        "Israelite law, a woman accused of infidelity could clear "
                        "herself through a sworn oath invoking divine witness. "
                        "Bitenosh's oath in the Apocryphon follows this legal form "
                        "precisely, but with a twist unique to the Watcher tradition: "
                        "the 'other man' she denies is not human but angelic. She "
                        "must swear not only that she did not commit adultery with "
                        "another man but that she was not violated by a Watcher or "
                        "one of the 'Sons of Heaven' (bene shemayin).",

        "second_temple": [
            {
                "source": "1 Enoch 106:4-7",
                "summary": "In the parallel account, Lamech goes to Methuselah and "
                           "says, 'I have begotten a strange son; he is not like a "
                           "human being, but resembles the children of the angels of "
                           "heaven.' There is no dialogue with the wife; the woman's "
                           "voice is absent from 1 Enoch 106.",
                "relevance": "The Apocryphon's inclusion of Bitenosh's direct speech "
                             "is a significant literary innovation over the 1 Enoch "
                             "parallel. By giving the wife a voice, the Apocryphon "
                             "humanizes the narrative and adds a dimension of marital "
                             "pathos entirely absent from 1 Enoch 106-107.",
                "canon": False
            },
            {
                "source": "Numbers 5:11-31 (Sotah)",
                "summary": "The priestly ritual for a wife suspected of adultery: "
                           "she drinks the 'bitter water' and swears an oath; if "
                           "guilty, her body will swell; if innocent, she is cleared.",
                "relevance": "Bitenosh's oath-scene adapts the structure of the sotah "
                             "ritual to a narrative context. The legal pattern (husband's "
                             "suspicion, wife's oath, divine adjudication) is preserved "
                             "but transformed: there is no priest, no bitter water, only "
                             "the woman's direct appeal to God and to her husband's "
                             "own knowledge.",
                "canon": True
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 6:1-2", "type": "ot", "note": "The sons of God 'took as their wives any they chose' — the canonical text that creates the possibility Lamech fears: that a Watcher chose Bitenosh."},
            {"ref": "Numbers 5:11-31", "type": "ot", "note": "The sotah ordeal for a wife suspected of adultery — the legal-ritual backdrop for Bitenosh's oath of purgation."},
            {"ref": "1 Enoch 106:4-7", "type": "pseudepigrapha", "note": "The parallel account in which Lamech describes Noah's appearance to Methuselah but never confronts his wife — Bitenosh has no voice in the Enochic version."},
            {"ref": "Jubilees 4:28", "type": "pseudepigrapha", "note": "Identifies Lamech's wife as Bitenosh daughter of Baraki'el, corroborating the Apocryphon's naming tradition."},
            {"ref": "Luke 1:34-35", "type": "nt", "note": "Mary's question to the angel Gabriel ('How will this be, since I am a virgin?') inverts the Bitenosh pattern: where Bitenosh denies divine conception, Mary learns she is experiencing it. Both scenes involve a woman confronting the possibility of supernatural pregnancy."}
        ],

        "divine_council_note": "The divine titles Bitenosh uses in her oath are "
                               "theologically loaded: 'the Most High' (illaya), "
                               "'the Lord' (mare), 'the Great One' (rabba), 'the "
                               "King of all the Ages' (malka di kol almaya). These "
                               "are titles of cosmic sovereignty that implicitly "
                               "contrast God's legitimate authority with the Watchers' "
                               "illegitimate transgression. By swearing before the "
                               "Most High God, Bitenosh appeals to the supreme "
                               "authority of the divine council — the very authority "
                               "the Watchers violated. Her oath is structurally a "
                               "petition to the council's presiding judge to vindicate "
                               "her innocence against the actions of his rebel "
                               "subordinates.",

        "sections": [
            {
                "heading": "The Confrontation (III.1-3)",
                "body": "Lamech brings his suspicion directly to Bitenosh. The "
                        "text is fragmentary at the transition from column II to "
                        "column III, but the sense is clear: Lamech demands to know "
                        "whether the child's father was human or angelic. The "
                        "directness of the confrontation is remarkable — Lamech does "
                        "not hint or test; he accuses. The scene presupposes that "
                        "Watcher visitation to human women was a known and feared "
                        "phenomenon, not a remote theoretical possibility. Lamech "
                        "does not need to explain to Bitenosh what a Watcher is or "
                        "why their involvement would be catastrophic. Both husband "
                        "and wife inhabit a world where the Watcher rebellion "
                        "described in 1 Enoch 6-11 is common knowledge."
            },
            {
                "heading": "Bitenosh's Oath and Appeal (III.3-8)",
                "body": "Bitenosh responds with a formal oath invoking the highest "
                        "divine authority. The Aramaic formula is solemn and "
                        "juridically precise: she swears by 'the Great Holy One, "
                        "the King of the heavens' that the seed is from Lamech and "
                        "not from 'any stranger or any of the Watchers or any of "
                        "the Sons of Heaven' (bene shemayin). The term bene "
                        "shemayin ('Sons of Heaven') is a variant of b'nei 'elohim "
                        "('Sons of God') and irin ('Watchers'), all referring to "
                        "the same class of heavenly beings. Bitenosh's use of "
                        "multiple terms for the potential angelic fathers — "
                        "'stranger' (nukhraya), 'Watchers' (irin), 'Sons of "
                        "Heaven' (bene shemayin) — is emphatic and exhaustive: "
                        "she denies every conceivable category of non-human "
                        "paternity. She then appeals to Lamech's own memory of "
                        "their sexual union, asking him to recall the pleasure "
                        "(hadwa) of their intimacy. This is an extraordinary "
                        "moment: a woman in an ancient Aramaic text defending "
                        "herself by invoking shared erotic memory as evidence. "
                        "Bitenosh does not merely deny; she provides proof — her "
                        "husband's own bodily knowledge of their union."
            },
            {
                "heading": "Lamech's Unresolved Doubt (III.9-end)",
                "body": "Despite Bitenosh's passionate oath, the text indicates "
                        "that Lamech remains troubled. His doubt is not resolved by "
                        "his wife's testimony; he will need patriarchal and "
                        "prophetic confirmation from Methuselah and ultimately Enoch. "
                        "This narrative detail is both psychologically realistic and "
                        "theologically significant. Psychologically, it captures the "
                        "corrosive nature of doubt: an oath, however sincere, cannot "
                        "always dispel suspicion. Theologically, it establishes that "
                        "the answer to the Watcher crisis cannot come from human "
                        "testimony alone — it requires revelation from Enoch, the "
                        "one human who has access to heavenly knowledge. The "
                        "epistemological hierarchy is clear: human witness (Bitenosh) "
                        "is insufficient; patriarchal authority (Methuselah) can "
                        "mediate; but only prophetic revelation (Enoch at the ends "
                        "of the earth) can definitively settle the question."
            }
        ]
    },

    # =========================================================================
    # COLUMNS IV-V: CONSULTATION WITH METHUSELAH AND ENOCH
    # =========================================================================
    {
        "id": "apoc-col-4-5",
        "ref": "1QapGen Col. IV-V",
        "chapter_num": 4,
        "title": "The Chain of Inquiry — Methuselah, Enoch, and the Confirmation of Noah",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Still troubled despite Bitenosh's oath, Lamech sends his father "
                    "Methuselah to consult Enoch, who dwells 'at the ends of the earth' "
                    "(presumably Parvaim/Paradise, cf. 1 Enoch 12-16). Methuselah "
                    "travels to Enoch and relays Lamech's fear. Enoch confirms that "
                    "Noah is indeed Lamech's legitimate son, not the offspring of a "
                    "Watcher. Enoch also prophesies the coming Flood and Noah's role "
                    "as the preserver of humanity. These columns are damaged but "
                    "their general content is recoverable from the preserved fragments "
                    "and the parallel in 1 Enoch 106-107.",

        "key_verse": {
            "ref": "1 Enoch 106:13 / 107:3 (parallel text)",
            "text": "I, Enoch, answered and said to him: 'The Lord will do a new "
                    "thing on the earth... this son who has been born to you is "
                    "righteous; and his name shall be called Noah, for he shall "
                    "be the remnant for you.'",
            "translation": "Charles"
        },

        "original_terms": [],

        "ane_backdrop": "The motif of a chain of inquiries — son to father to "
                        "grandfather to distant sage — reflects the ancient Near "
                        "Eastern understanding of knowledge as hierarchical and "
                        "mediated. In Mesopotamian literature, difficult questions "
                        "that cannot be resolved at one level are escalated through "
                        "a chain of increasingly authoritative figures until they "
                        "reach someone with direct access to divine knowledge. The "
                        "structure parallels the Mesopotamian ummanu (sage/scholar) "
                        "tradition, where antediluvian sages possessed knowledge "
                        "received directly from the gods. Enoch, dwelling at the "
                        "ends of the earth with direct access to heavenly secrets, "
                        "functions as the ultimate ummanu in the Jewish tradition.",

        "second_temple": [
            {
                "source": "1 Enoch 106:7-107:3",
                "summary": "The fullest parallel: Lamech tells Methuselah about "
                           "Noah's appearance; Methuselah journeys to 'the ends of "
                           "the earth' to consult Enoch; Enoch confirms Noah's "
                           "legitimacy and prophesies the Flood. Enoch also refers "
                           "to the Watcher descent and the subsequent corruption of "
                           "the earth as background to his prophecy.",
                "relevance": "1 Enoch 106-107 provides the most complete parallel "
                             "to the Apocryphon's columns IV-V. Since the Apocryphon's "
                             "text is very fragmentary here, the Enochic parallel is "
                             "essential for reconstructing the narrative arc.",
                "canon": False
            },
            {
                "source": "Jubilees 4:17-25",
                "summary": "Jubilees describes Enoch's sojourn in the Garden of Eden "
                           "after his translation, where he 'writes down the "
                           "condemnation and judgment of the world.' Enoch is "
                           "accessible to Methuselah because he has not died but "
                           "has been taken to a specific location.",
                "relevance": "Explains the geographical assumption of the Apocryphon: "
                             "Methuselah can travel to consult Enoch because Enoch "
                             "was translated to a place, not annihilated. The 'ends "
                             "of the earth' is a real destination in Second Temple "
                             "cosmography.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 5:21-27", "type": "ot", "note": "The genealogical chain — Enoch fathered Methuselah, who fathered Lamech, who fathered Noah. The Apocryphon follows this chain in reverse as an epistemic chain: Lamech asks Methuselah asks Enoch."},
            {"ref": "Genesis 5:24", "type": "ot", "note": "'Enoch walked with God, and he was not, for God took him' — the canonical basis for Enoch's availability at 'the ends of the earth' as a living source of divine knowledge."},
            {"ref": "1 Enoch 12:1-2", "type": "pseudepigrapha", "note": "Describes Enoch's translation and his dwelling among the Watchers/holy ones, establishing his location and his unique access to heavenly intelligence."},
            {"ref": "1 Enoch 106-107", "type": "pseudepigrapha", "note": "The parallel account of Methuselah's journey to Enoch and Enoch's confirmation of Noah's legitimacy."},
            {"ref": "Hebrews 11:5", "type": "nt", "note": "'By faith Enoch was taken up so that he should not see death, and he was not found, because God had taken him' — the NT echo of the Enoch translation tradition assumed by the Apocryphon."}
        ],

        "divine_council_note": "The epistemic chain in columns IV-V reveals a "
                               "hierarchy of knowledge that mirrors the hierarchy of "
                               "the divine council. Lamech, an ordinary human, cannot "
                               "resolve his doubt by human means. Methuselah, a "
                               "patriarch of great age, can serve as intermediary but "
                               "not as source. Only Enoch, the translated sage who has "
                               "stood in the divine council and witnessed the Watcher "
                               "judgment firsthand (1 Enoch 12-16), possesses the "
                               "authority to certify Noah's paternity. The answer to "
                               "a question caused by the council's rebels can only come "
                               "from someone who has access to the council's records. "
                               "This is apocalyptic epistemology: true knowledge about "
                               "the cosmic order comes not from human investigation but "
                               "from revelation mediated through a figure who has "
                               "penetrated the heavenly realm.",

        "sections": [
            {
                "heading": "Methuselah's Mission (IV.1-end)",
                "body": "Column IV is severely damaged, but the narrative trajectory "
                        "is recoverable: Lamech, unable to resolve his doubt through "
                        "Bitenosh's testimony, sends his father Methuselah to consult "
                        "Enoch. The geographic detail — Enoch dwelling at 'the ends "
                        "of the earth' — is consistent with the broader Enochic "
                        "tradition (1 Enoch 12:1-2; Jubilees 4:23), which places "
                        "the translated patriarch in a remote but accessible location, "
                        "sometimes identified with Paradise (Parvaim) or the Garden "
                        "of Righteousness. The journey itself is not described in "
                        "detail in the surviving fragments, but 1 Enoch 106:7 fills "
                        "the gap: Methuselah goes 'to the ends of the earth to "
                        "Enoch his father.' The journey motif serves a narrative "
                        "function (building suspense, showing the seriousness of "
                        "Lamech's concern) and a theological function (demonstrating "
                        "that resolution of the Watcher crisis requires ascending "
                        "to the highest available authority)."
            },
            {
                "heading": "Enoch's Confirmation and Prophecy (V.1-end)",
                "body": "Column V, also fragmentary, records Enoch's response. Based "
                        "on the parallel in 1 Enoch 106:13-107:3, Enoch confirms "
                        "three things: first, that Noah is genuinely Lamech's son "
                        "and not a Watcher's offspring; second, that the Watchers "
                        "have indeed corrupted the earth (explaining why Lamech's "
                        "suspicion was reasonable); and third, that God will bring "
                        "a devastating Flood to cleanse the earth, and Noah will be "
                        "the instrument of preservation. Enoch's prophecy links the "
                        "personal (Lamech's paternity question) to the cosmic (the "
                        "Flood judgment) in a single revelatory speech. The child "
                        "whose appearance caused Lamech's terror will in fact be "
                        "the savior of the human race. The irony is profound: the "
                        "very signs that made Lamech fear angelic paternity — Noah's "
                        "luminous, otherworldly appearance — are instead signs of "
                        "divine election. Noah looks different because he is different: "
                        "not contaminated but chosen."
            }
        ]
    },

    # =========================================================================
    # COLUMNS VI-X: NOAH AND THE FLOOD (FRAGMENTARY)
    # =========================================================================
    {
        "id": "apoc-col-6-10",
        "ref": "1QapGen Col. VI-X",
        "chapter_num": 6,
        "title": "The Flood and Its Aftermath — Noah's First-Person Account (Fragments)",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Columns VI-X are extremely fragmentary. The surviving words and "
                    "phrases indicate that Noah's first-person narrative continued "
                    "through the Flood and its aftermath. Identifiable elements "
                    "include references to the ark, the deluge, the receding of "
                    "waters, Noah's sacrifice, and the covenant. The narrative "
                    "appears to follow the Genesis account but with Aramaic "
                    "expansions, possibly including Noah's prayers and emotional "
                    "responses not found in the biblical text. Column VI may "
                    "contain material related to the Watcher judgment, serving as "
                    "a narrative bridge between the Lamech/birth cycle and the "
                    "Flood proper.",

        "key_verse": {
            "ref": "Genesis 8:1",
            "text": "But God remembered Noah and all the beasts and all the livestock that were with him in the ark. And God made a wind blow over the earth, and the waters subsided.",
            "translation": "ESV"
        },

        "original_terms": [],

        "ane_backdrop": "First-person Flood narratives are attested in Mesopotamian "
                        "literature. In Tablet XI of the Epic of Gilgamesh, "
                        "Utnapishtim narrates his experience of the Flood in the "
                        "first person to Gilgamesh. The Apocryphon's Noah performs "
                        "an analogous function: retelling the catastrophe from the "
                        "survivor's perspective. The shift from Genesis's third-person "
                        "omniscient narration to first-person testimony transforms "
                        "the Flood from a cosmic event observed from above into a "
                        "human experience lived from within. The Atrahasis Epic "
                        "similarly describes the Flood from the perspective of the "
                        "one saved, including his emotional response to the "
                        "destruction unfolding around him.",

        "second_temple": [
            {
                "source": "Jubilees 5-10",
                "summary": "Jubilees provides the most extensive Second Temple "
                           "retelling of the Flood, including the binding of the "
                           "Watcher spirits (Mastema retains one-tenth), Noah's "
                           "prayers, and the division of the earth.",
                "relevance": "Where the Apocryphon's columns are fragmentary, "
                             "Jubilees preserves a complete narrative that likely "
                             "drew on similar haggadic traditions. Comparison helps "
                             "fill gaps in the Apocryphon's lost text.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 6:9-9:17", "type": "ot", "note": "The canonical Flood narrative — the Apocryphon retells this entire sequence in Noah's first-person voice, transforming narrative into autobiography."},
            {"ref": "Genesis 8:20-22", "type": "ot", "note": "Noah's sacrifice after the Flood — fragments from columns VII-VIII appear to correspond to this scene, with the 'pleasing aroma' ascending to heaven."},
            {"ref": "Jubilees 5-10", "type": "pseudepigrapha", "note": "The Jubilees Flood account, including angelic binding and the Mastema negotiation, represents a parallel Rewritten Bible tradition."},
            {"ref": "4Q534-536 (4QNoah)", "type": "dss", "note": "Aramaic Noah fragments from Qumran Cave 4, possibly related to or drawn from the same source traditions as the Apocryphon's Noah sections."},
            {"ref": "1 Peter 3:20", "type": "nt", "note": "'God's patience waited in the days of Noah, while the ark was being prepared, in which a few, that is, eight persons, were brought safely through water' — the NT summary of the event Noah narrates in the Apocryphon."}
        ],

        "divine_council_note": "Though the fragments are sparse, the Flood narrative "
                               "in the Apocryphon almost certainly included reference "
                               "to the divine judgment on the Watchers, since this is "
                               "the theological cause of the Flood in the Enochic "
                               "tradition. The Flood is not merely God's response to "
                               "human sin (as in Genesis 6:5-7) but specifically God's "
                               "response to the Watcher contamination — the cleansing "
                               "of earth from the hybrid Nephilim and the knowledge "
                               "illicitly revealed by Azazel and his companions. In "
                               "1 Enoch 10, the archangels Michael, Gabriel, Raphael, "
                               "and Uriel are each commissioned by the council to "
                               "execute specific judgments — binding Watchers, warning "
                               "Noah, destroying Nephilim. The Apocryphon's Noah would "
                               "have experienced these council-dispatched interventions "
                               "from the receiving end.",

        "sections": [
            {
                "heading": "The State of the Text",
                "body": "Columns VI through X represent the most severely damaged "
                        "portion of the scroll. In many columns, only the beginnings "
                        "or ends of lines survive, with the middle sections entirely "
                        "lost. Machiela's 2009 edition provides the most comprehensive "
                        "treatment of these fragments, using multispectral imaging to "
                        "recover readings invisible to the naked eye. Even with these "
                        "advances, continuous translation is impossible for most of "
                        "columns VI-IX. Column X is somewhat better preserved, with "
                        "phrases relating to the recession of the Flood waters and "
                        "Noah's emergence from the ark. The fragmentary nature of these "
                        "columns is particularly frustrating because the Apocryphon's "
                        "first-person Noah narrative appears to have been extensive and "
                        "detailed, offering a perspective on the Flood unique among "
                        "surviving Second Temple texts."
            },
            {
                "heading": "Identifiable Themes and Vocabulary",
                "body": "Despite the damage, certain themes can be identified from "
                        "surviving vocabulary. Words related to water, destruction, "
                        "and judgment appear in columns VI-VII. Terminology associated "
                        "with sacrifice and covenant appears in columns VIII-IX. "
                        "Column X contains geographic and directional vocabulary "
                        "suggesting the description of post-Flood geography. The "
                        "presence of divine names and liturgical language in several "
                        "fragments suggests that Noah's prayers — absent from Genesis "
                        "but present in Jubilees 10 — were part of the Apocryphon's "
                        "narrative. The lost material almost certainly included "
                        "expanded versions of Genesis 8:20 (Noah's sacrifice), "
                        "Genesis 9:1-7 (the covenant), and possibly material "
                        "corresponding to the 'Book of Noah' traditions preserved "
                        "in 1 Enoch 65-69 and 106-107."
            }
        ]
    },

    # =========================================================================
    # COLUMNS XI-XVII: DIVISION OF THE EARTH
    # =========================================================================
    {
        "id": "apoc-col-11-17",
        "ref": "1QapGen Col. XI-XVII",
        "chapter_num": 11,
        "title": "The Division of the Earth Among Noah's Sons — Geographic Catalogue",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Columns XI-XVII, still fragmentary but somewhat better preserved "
                    "than VI-X, contain an elaborate geographic description of how "
                    "the earth was divided among Noah's three sons: Shem, Ham, and "
                    "Japheth. This section corresponds to Genesis 10 (the Table of "
                    "Nations) but expands it with detailed boundary descriptions, "
                    "using rivers, seas, and mountains as markers. The text assigns "
                    "specific territories with considerable geographic precision, "
                    "reflecting Hellenistic-era geographic knowledge. Machiela's "
                    "2009 edition provided major advances in reading these columns.",

        "key_verse": {
            "ref": "Genesis 10:32",
            "text": "These are the clans of the sons of Noah, according to their genealogies, in their nations, and from these the nations spread abroad on the earth after the flood.",
            "translation": "ESV"
        },

        "original_terms": [],

        "ane_backdrop": "The division of the earth among three figures has roots in "
                        "both Mesopotamian and Greek traditions. The Greek division "
                        "of the cosmos among Zeus, Poseidon, and Hades (Iliad "
                        "15.187-193) is a thematic parallel, though not a source. "
                        "More directly relevant are Hellenistic geographic texts "
                        "and ethnographic catalogues (e.g., Hecataeus of Miletus, "
                        "Eratosthenes) that divided the known world into continents "
                        "assigned to different peoples. The Apocryphon's geographic "
                        "descriptions reflect the Hellenistic synthesis of biblical "
                        "tradition with contemporary geographic knowledge, "
                        "demonstrating that Second Temple Jews engaged seriously "
                        "with the scientific geography of their era.",

        "second_temple": [
            {
                "source": "Jubilees 8:10-9:15",
                "summary": "Jubilees contains the most extensive parallel to the "
                           "Apocryphon's division of the earth, assigning Shem the "
                           "center of the earth (including the Garden of Eden and "
                           "Mount Sinai), Ham the south, and Japheth the north. "
                           "The boundaries are described with detailed geographic "
                           "markers.",
                "relevance": "The close verbal and conceptual parallels between "
                             "Jubilees 8-9 and the Apocryphon's columns XI-XVII "
                             "suggest either dependence on a common source (possibly "
                             "the lost Book of Noah) or direct literary relationship. "
                             "Machiela argues for a common source rather than direct "
                             "dependence.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 10:1-32", "type": "ot", "note": "The canonical Table of Nations listing the descendants of Shem, Ham, and Japheth — the Apocryphon transforms this genealogical list into a geographic narrative with territorial boundaries."},
            {"ref": "Genesis 9:18-27", "type": "ot", "note": "Noah's prophecy about his sons' destinies — the Apocryphon's geographic division gives concrete territorial content to Noah's blessings and curses."},
            {"ref": "Deuteronomy 32:8", "type": "ot", "note": "'When the Most High gave to the nations their inheritance, when he divided mankind, he fixed the borders of the peoples according to the number of the sons of God' (LXX/4QDeut-j) — the canonical theology of divinely ordained national boundaries that the Apocryphon narrativizes."},
            {"ref": "Jubilees 8:10-9:15", "type": "pseudepigrapha", "note": "The most detailed parallel to the Apocryphon's geographic division, with close verbal correspondences suggesting a common source tradition."},
            {"ref": "4Q534-536 (4QNoah)", "type": "dss", "note": "Additional Aramaic Noah material from Qumran that may overlap with or derive from the same traditions as the Apocryphon's geographic sections."}
        ],

        "divine_council_note": "The division of the earth among Noah's sons reflects "
                               "the broader Second Temple tradition that God (or his "
                               "council) assigned the nations to specific angelic "
                               "patrons. Deuteronomy 32:8 (LXX/4QDeut-j: 'according "
                               "to the number of the sons of God') establishes that "
                               "national territories were assigned by divine decree. "
                               "The Apocryphon's detailed geographic division, "
                               "administered by Noah under divine authority, provides "
                               "the narrative mechanism for this cosmic allocation. "
                               "Each son's territory implicitly comes under the "
                               "supervision of the divine being assigned to it by "
                               "the council.",

        "sections": [
            {
                "heading": "The Three-Part Division",
                "body": "The surviving text assigns Shem the central portion of the "
                        "earth, including the land that would become Israel, extending "
                        "from the Tina (Don?) river to the south. Ham receives the "
                        "southern lands, including Egypt and Africa. Japheth receives "
                        "the northern territories, including the lands around the "
                        "Mediterranean and extending into what is now Europe. The "
                        "boundaries are described using rivers, seas, and mountain "
                        "ranges as markers, reflecting a level of geographic knowledge "
                        "consistent with the Hellenistic period. The Mediterranean "
                        "Sea (called the 'Great Sea') features prominently as a "
                        "boundary marker. The Apocryphon's geography is compatible "
                        "with, but not identical to, the geographic scheme in "
                        "Jubilees 8-9, suggesting both drew on a common tradition "
                        "rather than one copying the other."
            },
            {
                "heading": "The Oath and Curse",
                "body": "The division of territories is accompanied by an oath — "
                        "each son swears not to encroach upon his brothers' "
                        "allotment. This oath element is also present in Jubilees "
                        "9:14-15, where a curse is pronounced on anyone who seizes "
                        "territory not assigned to him. The oath-bound territorial "
                        "division creates a cosmic charter for national boundaries: "
                        "the borders between peoples are not accidents of history "
                        "but divinely ordained allocations sealed by patriarchal "
                        "covenant. Any territorial aggression becomes, in this "
                        "framework, not merely a political act but a violation of "
                        "sacred covenant — a theme that resonated deeply in the "
                        "Hellenistic period when Jewish territory was contested by "
                        "competing empires."
            }
        ]
    },

    # =========================================================================
    # COLUMN XIX: ABRAHAM ENTERS CANAAN
    # =========================================================================
    {
        "id": "apoc-col-19",
        "ref": "1QapGen Col. XIX",
        "chapter_num": 19,
        "title": "Abraham Enters the Promised Land — First-Person Itinerary",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Column XIX marks the transition to the Abraham cycle, now told "
                    "in Abraham's first-person voice. Abraham (still called Abram) "
                    "describes his journey from Haran into Canaan, following the "
                    "route described in Genesis 12:4-9. He passes through the land "
                    "to Shechem, then to Bethel, building altars and calling on "
                    "God's name. The text is well preserved in the inner columns "
                    "and provides an expanded itinerary with geographic details "
                    "absent from Genesis. Abraham also describes a dream-vision "
                    "in which God promises him the land — the celebrated dream of "
                    "the cedar and the palm tree, in which he foresees the danger "
                    "awaiting him in Egypt.",

        "key_verse": {
            "ref": "1QapGen XIX.14-16 (dream sequence)",
            "text": "I saw in my dream a cedar tree and a palm tree... men came "
                    "and sought to cut down and uproot the cedar, and to leave "
                    "the palm tree alone. But the palm tree cried out and said, "
                    "'Do not cut down the cedar, for both of us are from one "
                    "root.' And the cedar was saved on account of the palm tree.",
            "translation": "Fitzmyer"
        },

        "original_terms": [],

        "ane_backdrop": "Abraham's itinerary through Canaan follows the major north-south "
                        "route known from both archaeological evidence and ancient "
                        "itinerary texts. The mention of Shechem, Bethel, and the "
                        "Negev corresponds to major sites along the central hill "
                        "country ridge route. The construction of altars at significant "
                        "locations reflects the ANE practice of marking territorial "
                        "claims and sacred sites with cultic installations. In "
                        "Mesopotamian royal inscriptions, a king's journey through "
                        "territory with altar-building signifies the establishment "
                        "of sovereignty under divine mandate. The dream of the cedar "
                        "and palm tree belongs to the ANE tradition of symbolic dreams "
                        "requiring interpretation — the same genre found in the "
                        "Joseph cycle (Genesis 37, 40-41), Daniel 2 and 4, and the "
                        "Qumran Book of Giants.",

        "second_temple": [
            {
                "source": "Jubilees 13:1-7",
                "summary": "Jubilees describes Abraham's journey into Canaan with "
                           "similar geographic detail, noting the altars at Shechem "
                           "and Bethel and adding that Abraham celebrated the Feast "
                           "of Tabernacles — an anachronistic detail reflecting "
                           "Jubilees' concern with halakhic observance.",
                "relevance": "Both the Apocryphon and Jubilees expand the itinerary "
                             "of Genesis 12 but with different theological emphases: "
                             "Jubilees adds legal observance; the Apocryphon adds "
                             "personal prayer and visionary experience.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 12:4-9", "type": "ot", "note": "The canonical account of Abram's entry into Canaan — the Apocryphon follows this sequence closely but expands it with first-person narration, prayers, dream-visions, and geographic detail."},
            {"ref": "Genesis 12:7", "type": "ot", "note": "'The LORD appeared to Abram and said, To your offspring I will give this land' — the Apocryphon expands this theophany into the dream of the cedar and palm tree."},
            {"ref": "Genesis 12:10", "type": "ot", "note": "'Now there was a famine in the land, so Abram went down to Egypt' — the Apocryphon uses the dream sequence to connect the Canaan entry to the Egypt sojourn with narrative causality."},
            {"ref": "Jubilees 13:1-7", "type": "pseudepigrapha", "note": "Parallel Rewritten Bible account of Abraham's Canaan itinerary, with halakhic additions absent from the Apocryphon."},
            {"ref": "Hebrews 11:8-10", "type": "nt", "note": "'By faith Abraham obeyed when he was called to go out to a place he was to receive as an inheritance' — the theological significance the NT assigns to Abraham's journey into Canaan."}
        ],

        "divine_council_note": "Abraham's dream-vision in column XIX places him in "
                               "the tradition of patriarchs who receive divine "
                               "communication through visionary experience. The cedar-"
                               "and-palm-tree dream functions as a divine council "
                               "communication: God reveals to Abraham through symbolic "
                               "imagery the danger that awaits in Egypt, enabling "
                               "Abraham to devise the sister-strategy. This positions "
                               "Abraham as a recipient of heavenly intelligence — not "
                               "Enoch's direct council access, but prophetic dreams "
                               "that carry the council's authority. The dream-warning "
                               "motif establishes that Abraham's subsequent actions in "
                               "Egypt (presenting Sarah as his sister) are not deception "
                               "born of cowardice but obedience to divinely revealed "
                               "strategy.",

        "sections": [
            {
                "heading": "The Journey from Haran (XIX.7-13)",
                "body": "Abraham narrates his departure from Haran in the first "
                        "person, describing the route south through Canaan. The "
                        "geographic detail exceeds what is found in Genesis 12: "
                        "the Apocryphon names specific stopping points and describes "
                        "the character of the land Abraham traverses. The text "
                        "emphasizes Abraham's cultic activity at each site — altar "
                        "building, sacrifice, and invocation of 'the God Most High' "
                        "(el illaya). This title, anticipating the Melchizedek "
                        "encounter in column XXII, identifies Abraham's God with "
                        "the supreme cosmic deity. The itinerary serves a dual "
                        "function: it recounts a historical journey and it maps "
                        "the sacred geography of the land, marking it as Abraham's "
                        "by divine right and cultic consecration."
            },
            {
                "heading": "The Dream of the Cedar and the Palm Tree (XIX.14-19)",
                "body": "At Bethel, Abraham receives a symbolic dream that "
                        "foreshadows the danger awaiting him in Egypt. He sees a "
                        "cedar tree and a palm tree growing together from one root. "
                        "Men come to cut down the cedar, but the palm tree cries out: "
                        "'Do not cut down the cedar, for both of us are from one "
                        "root!' The cedar is spared for the palm tree's sake. Abraham "
                        "interprets the dream: the cedar is himself, the palm tree "
                        "is Sarah, and the woodcutters are the Egyptians who will "
                        "seek to kill him in order to take his wife. The dream's "
                        "message is that Sarah will save Abraham's life by claiming "
                        "kinship with him — which leads to his decision to present "
                        "her as his sister. This dream is entirely absent from "
                        "Genesis 12, which presents Abraham's fear as rational "
                        "calculation. The Apocryphon elevates his strategy from "
                        "human prudence to prophetic obedience, resolving a moral "
                        "difficulty that troubled ancient interpreters: Abraham does "
                        "not lie about Sarah from cowardice but acts on divinely "
                        "communicated intelligence."
            },
            {
                "heading": "The Descent to Egypt (XIX.19-end)",
                "body": "Famine drives Abraham and Sarah into Egypt, following "
                        "Genesis 12:10. The Apocryphon adds Abraham's prayer for "
                        "protection as they enter the land — a detail absent from "
                        "Genesis, where Abraham simply acts. The prayer identifies "
                        "God as the sovereign who controls the affairs of nations "
                        "and can protect his servants even in the heart of Pharaoh's "
                        "kingdom. Abraham's emotional state is visible in a way "
                        "that Genesis's terse narrative does not permit: he is "
                        "afraid, prayerful, and reliant on the dream-warning he "
                        "has received. The transition to column XX sets the stage "
                        "for the most famous passage in the entire scroll: the "
                        "Beauty Hymn."
            }
        ]
    },

    # =========================================================================
    # COLUMN XX: SARAH'S BEAUTY AND PHARAOH
    # =========================================================================
    {
        "id": "apoc-col-20",
        "ref": "1QapGen Col. XX",
        "chapter_num": 20,
        "title": "The Beauty of Sarah — The Hymn Before Pharaoh and the Pestilential Spirit",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Column XX is the most celebrated section of the Genesis "
                    "Apocryphon. Egyptian nobles see Sarah and report her beauty "
                    "to Pharaoh in an elaborate hymn describing her physical "
                    "appearance in extraordinary detail — her face, her hair, "
                    "her eyes, her nose, her breasts, her hands, her fingers, "
                    "her legs. This is the most extensive physical description "
                    "of a woman in all known Second Temple literature. Pharaoh "
                    "takes Sarah into his household. Abraham weeps and prays. "
                    "God responds by sending a 'pestilential spirit' (ruha "
                    "makhashsha) that afflicts Pharaoh and his entire house for "
                    "two years, preventing him from approaching Sarah.",

        "key_verse": {
            "ref": "1QapGen XX.2-7",
            "text": "How beautiful the look of her face... and how fine is the "
                    "hair of her head, how fair indeed are her eyes and how "
                    "pleasing her nose and all the radiance of her face... how "
                    "beautiful her breast and how lovely all her whiteness. Her "
                    "arms goodly to look upon, and her hands how perfect... how "
                    "fair her palms and how long and fine all the fingers of "
                    "her hands. Her legs how beautiful and how without blemish "
                    "her thighs.",
            "translation": "Fitzmyer"
        },

        "original_terms": [],

        "ane_backdrop": "The detailed blazon (a head-to-toe description of a woman's "
                        "beauty) has parallels in both Mesopotamian and Egyptian love "
                        "poetry. The Egyptian love songs from Papyrus Harris 500 and "
                        "the Cairo Love Songs describe a woman's beauty part by part "
                        "in similar fashion. The Song of Songs (4:1-7, 7:1-9) is the "
                        "biblical example, using the wasf form (Arabic: 'description') "
                        "to praise the beloved's body from head to foot or foot to "
                        "head. The Apocryphon's description of Sarah follows the wasf "
                        "pattern with remarkable specificity, suggesting the author "
                        "was familiar with this poetic convention. The context, "
                        "however, transforms the genre: the beauty hymn is not a "
                        "love poem between partners but a report by courtiers to "
                        "their king, making it simultaneously a celebration of "
                        "beauty and an instrument of political danger.",

        "second_temple": [
            {
                "source": "Jubilees 13:11-13",
                "summary": "Jubilees covers the Egypt sojourn briefly, noting that "
                           "Pharaoh took Sarah and that Abraham wept. No beauty "
                           "description is provided.",
                "relevance": "The contrast with Jubilees is instructive: where Jubilees "
                             "compresses the episode, the Apocryphon massively expands "
                             "it. The two texts have opposite literary strategies for "
                             "the same biblical passage.",
                "canon": False
            },
            {
                "source": "Josephus, Antiquities I.162-168",
                "summary": "Josephus retells the Egypt episode noting Abraham's fear "
                           "of the Egyptians' 'mad passion for women.' He adds that "
                           "Abraham taught the Egyptians arithmetic and astronomy.",
                "relevance": "Josephus confirms a widespread Second Temple tradition "
                             "of expanding Abraham's time in Egypt but takes a "
                             "different direction — cultural exchange rather than "
                             "beauty poetry.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 12:10-20", "type": "ot", "note": "The canonical wife-sister episode — the Apocryphon transforms ten terse verses into an elaborate narrative with dream-warning, beauty hymn, pestilential spirit, exorcism, and detailed plague account."},
            {"ref": "Genesis 12:14-15", "type": "ot", "note": "'The Egyptians saw that the woman was very beautiful. And... Pharaoh's princes... praised her to Pharaoh' — the single adjective ('very beautiful') that the Apocryphon expands into a 25-line descriptive hymn."},
            {"ref": "Song of Songs 4:1-7; 7:1-9", "type": "ot", "note": "The canonical wasf (descriptive praise poem) — the literary form underlying the Apocryphon's Sarah beauty hymn."},
            {"ref": "1 Samuel 16:14", "type": "ot", "note": "'A harmful spirit from the LORD tormented Saul' — the closest biblical parallel to the Apocryphon's pestilential spirit (ruha makhashsha) sent against Pharaoh."},
            {"ref": "1 Kings 22:19-23", "type": "ot", "note": "God sends a lying spirit through the divine council — a canonical example of God using a spirit-agent as an instrument of judgment, paralleling the Apocryphon's mechanism."},
            {"ref": "Proverbs 31:30", "type": "ot", "note": "'Charm is deceitful, and beauty is vain, but a woman who fears the LORD is to be praised' — a canonical counterpoint to the Apocryphon's celebration of physical beauty."}
        ],

        "divine_council_note": "Column XX introduces two significant divine council "
                               "elements. First, the 'pestilential spirit' (ruha "
                               "makhashsha) sent against Pharaoh is a council-dispatched "
                               "agent. God does not personally afflict Pharaoh but "
                               "deploys a spiritual being to execute judgment — the same "
                               "pattern seen in 1 Kings 22:19-23, where God sends a "
                               "spirit through the council. This reflects the mature "
                               "Second Temple understanding of divine action as mediated "
                               "through spiritual intermediaries. Second, Abraham's role "
                               "as exorcist (laying hands on Pharaoh to expel the spirit "
                               "after Sarah is returned) positions him as a human agent "
                               "authorized to command council-dispatched spirits — a "
                               "remarkable degree of spiritual authority for a patriarch.",

        "sections": [
            {
                "heading": "The Beauty Hymn (XX.2-8)",
                "body": "When Pharaoh's courtiers see Sarah, they compose a report "
                        "of her beauty for the king. The courtier Harkenosh and two "
                        "companions deliver this report. The description proceeds "
                        "systematically from head to body: the look of her face, "
                        "the hair of her head, the fairness of her eyes, the "
                        "pleasing shape of her nose, the radiance of her countenance, "
                        "her breast, her whiteness of skin, her arms and hands, "
                        "the perfection of her fingers, her legs and thighs. The "
                        "Aramaic phrase mah shapir ('how beautiful') recurs as an "
                        "anaphoric refrain throughout, creating a liturgical cadence. "
                        "The description employs what classical rhetoric calls the "
                        "blazon or, in Arabic poetic tradition, the wasf — a "
                        "systematic praise of a woman's body part by part. The "
                        "hymn concludes with a summary: 'above all women she is "
                        "lovely, and her beauty surpasses them all.' The sexual "
                        "candor — breasts, thighs, whiteness of skin — is unusual "
                        "for Second Temple literature and indicates the author was "
                        "working within a love-poetry tradition rather than a "
                        "strictly theological genre. The beauty hymn functions "
                        "narratively as the catalyst for Pharaoh's desire and the "
                        "crisis that follows."
            },
            {
                "heading": "Sarah Taken and Abraham's Prayer (XX.8-16)",
                "body": "Pharaoh takes Sarah into his household. Abraham weeps and "
                        "prays to God for deliverance — elements absent from Genesis "
                        "12, where Abraham is notably silent during Sarah's captivity. "
                        "The Apocryphon's Abraham is emotionally engaged: his grief "
                        "is explicit, his prayer urgent. He asks God to send a "
                        "'chastising spirit' against Pharaoh to prevent him from "
                        "defiling Sarah. The text bridges a moral gap that troubled "
                        "ancient interpreters: how could Abraham allow his wife to be "
                        "taken without protest? The Apocryphon's answer is that he "
                        "did protest — not to Pharaoh (who would have killed him) but "
                        "to God (who could actually intervene). Abraham's prayer "
                        "initiates the divine response."
            },
            {
                "heading": "The Pestilential Spirit and Two Years of Affliction (XX.16-25)",
                "body": "God answers Abraham's prayer by sending a 'pestilential "
                        "spirit' (ruha makhashsha) upon Pharaoh and his entire "
                        "household. The spirit prevents Pharaoh from approaching "
                        "Sarah sexually — a detail that directly addresses a gap in "
                        "Genesis that troubled ancient readers: were the plagues "
                        "immediate enough to prevent consummation? The Apocryphon "
                        "answers unambiguously: the spirit struck immediately and "
                        "continuously, making approach impossible. The affliction "
                        "lasts two full years, during which Pharaoh's healers and "
                        "exorcists are unable to cure him. The two-year duration "
                        "suggests a longer Egyptian sojourn than Genesis implies and "
                        "heightens the dramatic tension. Finally, Lot (Abraham's "
                        "nephew) reveals to Pharaoh that Sarah is Abraham's wife. "
                        "Pharaoh returns Sarah. Abraham then lays hands on Pharaoh "
                        "and prays, and the spirit departs — Abraham functioning as "
                        "an exorcist, a role that connects him to the broader Second "
                        "Temple tradition of holy men who command spiritual forces "
                        "(cf. Josephus, Antiquities VIII.46-49, on Solomon as "
                        "exorcist). Pharaoh sends Abraham away with great wealth: "
                        "gold, silver, livestock, and garments — a preview of the "
                        "Exodus pattern where Israel will leave Egypt enriched "
                        "(Exodus 12:35-36)."
            }
        ]
    },

    # =========================================================================
    # HISTORICAL INSERT: SARAH'S BEAUTY IN ANCIENT NEAR EASTERN LITERATURE
    # =========================================================================
    {
        "id": "insert-apoc-sarah-beauty",
        "ref": "Literary Context",
        "chapter_num": None,
        "title": "Sarah's Beauty in Ancient Near Eastern and Second Temple Literature",
        "era": "apocryphon_columns",
        "type": "historical_insert",

        "synopsis": "The Genesis Apocryphon's elaborate description of Sarah's beauty "
                    "in column XX is the most extensive physical description of a "
                    "woman in all surviving Second Temple Jewish literature. It "
                    "participates in a literary tradition stretching from Sumerian "
                    "love poetry through the Song of Songs to rabbinic midrash. "
                    "Examining this tradition illuminates both the Apocryphon's "
                    "literary artistry and the cultural significance of Sarah's "
                    "beauty in Jewish memory.",

        "key_verse": {
            "ref": "Genesis 12:11",
            "text": "When he was about to enter Egypt, he said to Sarai his wife, 'I know that you are a woman beautiful in appearance.'",
            "translation": "ESV"
        },
        "original_terms": [],
        "ane_backdrop": None,
        "second_temple": [],

        "cross_refs": [
            {"ref": "Song of Songs 4:1-7; 7:1-9", "type": "ot", "note": "The canonical wasf poems — the primary biblical precedent for detailed physical description of a woman's beauty, part by part."},
            {"ref": "Genesis 12:11, 14", "type": "ot", "note": "'I know that you are a woman beautiful in appearance' / 'the Egyptians saw that the woman was very beautiful' — the canonical seed text that the Apocryphon expands into 25 lines."},
            {"ref": "Genesis 12:10-20; 20:1-18; 26:1-11", "type": "ot", "note": "The three wife-sister narratives in Genesis — a repeated pattern in which the matriarch's beauty creates danger for the patriarch in foreign lands."},
            {"ref": "Esther 2:7", "type": "ot", "note": "'The young woman had a beautiful figure and was lovely to look at' — another canonical note on a woman's beauty that later tradition expanded with elaborate physical descriptions."},
            {"ref": "Genesis Rabbah 40:4", "type": "rabbinic", "note": "Rabbinic midrash that Sarah was one of the four most beautiful women in the world (along with Rahab, Abigail, and Esther). The tradition of celebrating Sarah's beauty continued well beyond the Second Temple period."},
            {"ref": "Megillah 15a", "type": "rabbinic", "note": "The Talmudic tradition listing the four most beautiful women — Sarah, Rahab, Abigail, and Esther — continuing the line of reflection that the Apocryphon inaugurated."}
        ],

        "divine_council_note": "Sarah's beauty in the Apocryphon is not merely an "
                               "aesthetic observation but a theological datum. In the "
                               "narrative logic of Genesis 12 and its retellings, "
                               "Sarah's beauty is the mechanism through which God's "
                               "promise to Abraham is tested: the woman through whom "
                               "the covenant seed must come is endangered precisely "
                               "because of her desirability. God's intervention — "
                               "the plagues on Pharaoh, the pestilential spirit — "
                               "demonstrates that the divine plan cannot be derailed "
                               "by human (or royal) desire. The beauty hymn thus "
                               "functions within a providential framework: Sarah is "
                               "beautiful, and that beauty creates danger, and that "
                               "danger elicits divine rescue, which confirms the "
                               "inviolability of the Abrahamic covenant. The council "
                               "dispatches a spirit to enforce what the council has "
                               "decreed: that through Abraham all nations shall be "
                               "blessed.",

        "sections": [
            {
                "heading": "The Wasf Tradition in Ancient Near Eastern Poetry",
                "body": "The systematic physical description of a beloved's body — "
                        "known in Arabic poetic criticism as the wasf — is one of "
                        "the oldest literary forms in the ancient Near East. Sumerian "
                        "love poetry from the late 3rd millennium BC describes the "
                        "goddess Inanna's body in celebratory detail. Egyptian love "
                        "songs from the New Kingdom (Papyrus Harris 500, Papyrus "
                        "Chester Beatty I, the Cairo Love Songs) employ part-by-part "
                        "descriptions of the beloved's face, hair, eyes, arms, and "
                        "body. The Song of Songs contains two canonical wasf poems "
                        "(4:1-7 and 7:1-9), describing the woman from head to breast "
                        "and from feet to head respectively. What distinguishes the "
                        "Apocryphon's wasf from these poetic predecessors is its "
                        "narrative context: it is not a lover's praise but a "
                        "courtier's report. The beauty is being catalogued for a "
                        "king's consumption, transforming an intimate genre into an "
                        "instrument of political and sexual power. The woman being "
                        "described is not the speaker's beloved but another man's "
                        "wife, making the description simultaneously appreciative "
                        "and threatening."
            },
            {
                "heading": "Sarah's Beauty in Later Jewish Tradition",
                "body": "The tradition of Sarah's extraordinary beauty did not end "
                        "with the Apocryphon. The Talmud (Megillah 15a) lists Sarah "
                        "among the four most beautiful women in history (with Rahab, "
                        "Abigail, and Esther). Genesis Rabbah 40:4 elaborates on "
                        "Genesis 12:11, explaining that Abraham only became fully "
                        "aware of Sarah's beauty when they approached Egypt — a "
                        "midrashic explanation for the timing of his concern. "
                        "Targum Pseudo-Jonathan on Genesis 12:11 notes that Sarah's "
                        "beauty was undiminished despite the hardships of travel. "
                        "Josephus (Antiquities 1.162-163) describes Pharaoh's desire "
                        "for Sarah and God's intervention but omits the physical "
                        "description. The Apocryphon's wasf thus occupies a unique "
                        "position: it is the earliest and most detailed physical "
                        "description of Sarah, predating the rabbinic traditions by "
                        "centuries and providing the literary model — whether "
                        "directly or through shared oral tradition — for later "
                        "celebrations of the matriarch's beauty. It demonstrates "
                        "that Second Temple Judaism was not uniformly ascetic or "
                        "prudish about the human body: the Apocryphon's author "
                        "celebrates Sarah's physical beauty with evident literary "
                        "relish, seeing no contradiction between piety and "
                        "aesthetic appreciation."
            },
            {
                "heading": "Beauty, Danger, and Divine Protection",
                "body": "In all three wife-sister narratives (Genesis 12, 20, 26), "
                        "the matriarch's beauty creates a specific pattern: beauty "
                        "attracts foreign power, foreign power threatens the "
                        "patriarch, divine intervention rescues both patriarch and "
                        "matriarch. The Apocryphon intensifies every element of "
                        "this pattern. The beauty is described in extraordinary "
                        "detail (making Pharaoh's desire comprehensible). The "
                        "threat is heightened by the dream-warning (making the "
                        "danger premeditated and cosmic). The divine rescue is "
                        "elaborated with specific plagues and a spiritual agent "
                        "(making God's intervention dramatically visible). The "
                        "literary effect is to transform an already powerful "
                        "narrative into a fully realized dramatic episode. The "
                        "theological effect is to emphasize that God's covenant "
                        "with Abraham — which requires Sarah as the mother of the "
                        "promised seed — is defended by divine power against the "
                        "greatest earthly threat imaginable. The beauty that "
                        "endangered Sarah is thus ultimately a servant of "
                        "providence: it precipitates the crisis that demonstrates "
                        "God's faithfulness."
            }
        ]
    },

    # =========================================================================
    # COLUMN XXI: LOT'S SEPARATION AND ABRAHAM'S GEOGRAPHIC SURVEY
    # =========================================================================
    {
        "id": "apoc-col-21",
        "ref": "1QapGen Col. XXI",
        "chapter_num": 21,
        "title": "Abraham's Return, the Land Survey, and Lot's Departure",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Column XXI narrates Abraham's return from Egypt to Canaan, now "
                    "wealthy from Pharaoh's gifts. The column contains a remarkable "
                    "geographic survey in which Abraham ascends to a high point and "
                    "describes the promised land in all four directions — rivers, "
                    "mountains, boundaries — with a level of topographic detail "
                    "absent from Genesis 13. The column then describes the "
                    "separation of Abraham and Lot: their herds have grown too "
                    "large for the land to support both, and Abraham generously "
                    "allows Lot first choice. Lot chooses the Jordan valley and "
                    "settles near Sodom, setting the stage for the war of the "
                    "kings in column XXII.",

        "key_verse": {
            "ref": "1QapGen XXI.8-12 (geographic survey)",
            "text": "I went up to Ramat Hazor and I looked from this high place "
                    "to the south and to the north, to the east and to the west... "
                    "and I saw the land from the River of Egypt to Lebanon and "
                    "Senir, and from the Great Sea to Hauran... all this land "
                    "he would give to me and to my seed forever.",
            "translation": "Fitzmyer (adapted)"
        },

        "original_terms": [],

        "ane_backdrop": "The geographic survey from a high vantage point is a "
                        "well-attested ANE literary and royal motif. Mesopotamian "
                        "royal inscriptions describe kings ascending high places to "
                        "survey territories they have conquered or been granted. The "
                        "Moses survey from Mount Nebo (Deuteronomy 34:1-4) is the "
                        "closest biblical parallel: God shows Moses 'all the land — "
                        "Gilead as far as Dan, all Naphtali, Ephraim, Manasseh, "
                        "Judah as far as the western sea, the Negev, and the Jordan "
                        "plain.' The Apocryphon's Abraham performs the same visual "
                        "survey, mapping the promised land from a summit with "
                        "directional precision. The motif combines territorial "
                        "claim with divine sanction: what the patriarch sees, God "
                        "gives.",

        "second_temple": [
            {
                "source": "Jubilees 13:14-21",
                "summary": "Jubilees describes Abraham's return from Egypt and the "
                           "separation from Lot, adding that Lot's choice of Sodom "
                           "was driven by greed and proximity to Egyptian luxury.",
                "relevance": "Jubilees shares the basic narrative but moralizes Lot's "
                             "choice more explicitly than either Genesis or the "
                             "Apocryphon, reflecting Jubilees' ethical concerns.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 13:1-18", "type": "ot", "note": "The canonical account of Abraham's return from Egypt, separation from Lot, and God's land promise — the Apocryphon expands every element with first-person narration and geographic detail."},
            {"ref": "Genesis 13:14-17", "type": "ot", "note": "'Lift up your eyes and look from the place where you are, northward and southward and eastward and westward, for all the land that you see I will give to you' — the canonical command that the Apocryphon transforms into a detailed topographic survey."},
            {"ref": "Deuteronomy 34:1-4", "type": "ot", "note": "Moses' survey of the promised land from Mount Nebo — the closest structural parallel to Abraham's survey in the Apocryphon. Both patriarchs see the land from a summit; both receive a divine promise about the territory they behold."},
            {"ref": "Genesis 13:10-13", "type": "ot", "note": "Lot's choice of the Jordan valley, 'well watered everywhere like the garden of the LORD' — the fateful decision that leads to his entanglement with Sodom."},
            {"ref": "Jubilees 13:14-21", "type": "pseudepigrapha", "note": "Parallel account of the separation with moralized characterization of Lot's choice."}
        ],

        "divine_council_note": "The land survey in column XXI carries the authority "
                               "of a divine grant. When God tells Abraham to 'look' "
                               "in all four directions and declares 'all this land I "
                               "will give to you,' the visual survey functions as a "
                               "legal act: the patriarch is shown the title deed of a "
                               "territory allocated by the supreme council head. This "
                               "echoes the pattern in Deuteronomy 32:8-9, where God "
                               "allocated the nations' territories: Abraham's allotment "
                               "is the specific portion reserved for God's own people. "
                               "The geographic precision of the Apocryphon's survey — "
                               "naming rivers, mountains, seas — transforms the divine "
                               "promise from abstract blessing into a cadastral record "
                               "with measurable boundaries.",

        "sections": [
            {
                "heading": "Return from Egypt (XXI.1-7)",
                "body": "Abraham departs Egypt with the wealth Pharaoh has given him "
                        "and returns to Canaan, retracing his earlier route through "
                        "the Negev and back to Bethel. The Apocryphon notes his "
                        "prosperity — livestock, silver, gold — establishing that "
                        "God's protection in Egypt has resulted in material blessing. "
                        "This wealth, however, will create the problem that drives "
                        "the next narrative: the land cannot support both Abraham's "
                        "and Lot's expanded herds. The pattern of descent to Egypt, "
                        "divine protection, and return with wealth is a deliberate "
                        "foreshadowing of the Exodus: the patriarch's experience "
                        "prefigures the nation's future. The Apocryphon's first-person "
                        "narration makes Abraham conscious of God's faithfulness "
                        "throughout the ordeal."
            },
            {
                "heading": "The Four-Directional Survey (XXI.8-14)",
                "body": "Abraham ascends to a high point — identified by some scholars "
                        "with Ramat Hazor, the highest peak in the central highlands "
                        "— and looks out in all four directions. The survey is detailed: "
                        "to the south he sees as far as the River of Egypt (Wadi "
                        "el-Arish or the Nile); to the west, the Mediterranean (the "
                        "'Great Sea'); to the north, Lebanon and Senir (Anti-Lebanon); "
                        "to the east, the Jordan valley and Hauran. The geographic "
                        "knowledge is consistent with Hellenistic-period cartography "
                        "and corresponds broadly to the traditional biblical boundaries "
                        "of the promised land (cf. Numbers 34:1-12). The survey is "
                        "both literary and theological: it concretizes the divine "
                        "promise by mapping it onto real geography. Abraham does not "
                        "receive an abstract blessing but a specific territory with "
                        "identifiable boundaries."
            },
            {
                "heading": "The Separation from Lot (XXI.15-end)",
                "body": "The narrative follows Genesis 13:5-13: the herds of Abraham "
                        "and Lot have grown too large for the land. Quarrels arise "
                        "between their herdsmen. Abraham, in a display of magnanimity, "
                        "allows Lot to choose first. Lot looks toward the Jordan "
                        "valley, sees that it is 'well watered everywhere like the "
                        "garden of the LORD' (Genesis 13:10), and chooses it. He "
                        "settles near Sodom. The Apocryphon tells this from Abraham's "
                        "perspective, emphasizing his generosity and perhaps hinting "
                        "at his awareness that Lot's choice carries moral risk. "
                        "The separation is necessary for the next episode: with "
                        "Lot in the Jordan plain near Sodom, he will be caught up "
                        "in the war of the four kings against five, requiring "
                        "Abraham's military intervention in column XXII."
            }
        ]
    },

    # =========================================================================
    # COLUMN XXII: WAR OF THE KINGS AND MELCHIZEDEK
    # =========================================================================
    {
        "id": "apoc-col-22",
        "ref": "1QapGen Col. XXII",
        "chapter_num": 22,
        "title": "The War of the Kings, Lot's Rescue, and the Blessing of Melchizedek",
        "era": "apocryphon_columns",
        "type": "chapter",

        "synopsis": "Column XXII retells Genesis 14: the war of four kings against "
                    "five, the capture of Sodom and Lot, Abraham's military "
                    "expedition to rescue Lot, and the encounter with Melchizedek "
                    "king of Salem (Jerusalem). Abraham narrates his defeat of "
                    "Chedorlaomer's coalition, the recovery of Lot and the captives, "
                    "and Melchizedek's blessing. Abraham pays tithes to Melchizedek "
                    "and refuses the king of Sodom's offer of spoils. The column is "
                    "among the best preserved and provides important geographic and "
                    "narrative detail beyond what Genesis 14 supplies. Critically, "
                    "the Apocryphon explicitly identifies Salem with Jerusalem — "
                    "the earliest known explicit equation in a narrative text.",

        "key_verse": {
            "ref": "1QapGen XXII.14-17",
            "text": "And the king of Sodom came to meet me, and Melchizedek "
                    "the king of Salem — that is, the king of Jerusalem — "
                    "brought out food and drink for me and for all the men "
                    "who were with me. And he blessed me and said: 'Blessed "
                    "be Abram by the Most High God, Lord of heaven and earth. "
                    "And blessed be the Most High God who has delivered your "
                    "enemies into your hand.' And I gave him a tithe of all "
                    "the possessions of the king of Elam.",
            "translation": "Fitzmyer (adapted)"
        },

        "original_terms": [],

        "ane_backdrop": "Genesis 14 is one of the most debated chapters in the "
                        "Pentateuch, with scholars arguing over whether the war "
                        "of the four kings against five reflects genuine Late Bronze "
                        "Age or Middle Bronze Age political geography. The Apocryphon "
                        "adds geographic specificity to the campaign route, naming "
                        "locations that can in some cases be identified with known "
                        "sites. Melchizedek of Salem, described as 'priest of God "
                        "Most High' (kohen le-el illaya), represents the intersection "
                        "of Canaanite and Israelite religious traditions. 'God Most "
                        "High' (El Elyon) was a Canaanite divine title attested at "
                        "Ugarit and in Phoenician inscriptions. The Apocryphon's "
                        "explicit identification of Salem with Jerusalem (not stated "
                        "in Genesis 14 but assumed in Psalm 76:2) is an important "
                        "piece of interpretive evidence for how Second Temple Jews "
                        "understood this text. The title 'Lord of heaven and earth' "
                        "(mare shemayya we-ar'a) identifies Abraham's God as the "
                        "supreme deity of the cosmic order.",

        "second_temple": [
            {
                "source": "11QMelchizedek (11Q13)",
                "summary": "A Qumran text that elevates Melchizedek to a heavenly "
                           "figure who executes divine judgment in the eschatological "
                           "jubilee. He is called 'elohim' and presides over the "
                           "divine assembly, applying Psalm 82:1 directly to him.",
                "relevance": "The Apocryphon's portrayal of Melchizedek as a human "
                             "king-priest contrasts with 11QMelchizedek's angelic "
                             "Melchizedek, demonstrating the range of Second Temple "
                             "interpretive traditions about this figure. The two texts "
                             "from the same cave system present radically different "
                             "Melchizedeks.",
                "canon": False
            },
            {
                "source": "Hebrews 7:1-10",
                "summary": "The author of Hebrews interprets Melchizedek as a type "
                           "of Christ: 'without father or mother or genealogy, having "
                           "neither beginning of days nor end of life, but resembling "
                           "the Son of God, he continues a priest forever.'",
                "relevance": "Hebrews' christological reading of Melchizedek stands "
                             "in continuity with the speculative Second Temple "
                             "traditions about Melchizedek (including 11Q13) while "
                             "going further in identifying the figure with Christ's "
                             "priesthood. The Apocryphon provides the narrative "
                             "foundation for all subsequent Melchizedek interpretation.",
                "canon": True
            },
            {
                "source": "Jubilees 13:25-27",
                "summary": "Jubilees briefly notes Abraham's tithe to Melchizedek "
                           "and adds that this established the priestly tithe as a "
                           "perpetual ordinance.",
                "relevance": "Jubilees and the Apocryphon share the basic narrative "
                             "but with different theological emphases: Jubilees "
                             "focuses on halakhic precedent; the Apocryphon focuses "
                             "on narrative drama and geographic detail.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 14:1-24", "type": "ot", "note": "The canonical war of the kings, Lot's rescue, and the Melchizedek encounter — the Apocryphon retells the entire chapter in Abraham's first-person voice with geographic expansions."},
            {"ref": "Genesis 14:18-20", "type": "ot", "note": "The Melchizedek pericope: king of Salem, priest of God Most High, bread and wine, blessing, tithe — every element is preserved and expanded in the Apocryphon."},
            {"ref": "Psalm 76:2", "type": "ot", "note": "'His abode has been established in Salem, his dwelling place in Zion' — the canonical identification of Salem with Jerusalem that the Apocryphon makes explicit in narrative form."},
            {"ref": "Psalm 110:4", "type": "ot", "note": "'You are a priest forever after the order of Melchizedek' — the royal-priestly oracle that made Melchizedek a figure of enduring theological significance."},
            {"ref": "11QMelchizedek (11Q13)", "type": "dss", "note": "The Qumran text that elevates Melchizedek to an angelic judge who presides over the eschatological divine council — the furthest development of the Melchizedek tradition within Second Temple Judaism."},
            {"ref": "Hebrews 5:6-10; 7:1-28", "type": "nt", "note": "The most extensive NT treatment of Melchizedek: Jesus is 'a priest forever after the order of Melchizedek,' whose priesthood supersedes Aaron's. The entire argument depends on the Genesis 14 narrative the Apocryphon retells."}
        ],

        "divine_council_note": "The Melchizedek encounter in column XXII is a "
                               "pivotal moment for divine council theology. "
                               "Melchizedek is 'priest of God Most High' (kohen "
                               "le-el illaya), and his blessing of Abraham invokes "
                               "'the Most High God, Lord of heaven and earth' — "
                               "language that identifies Abraham's God as the supreme "
                               "ruler of the cosmic order. The title 'Lord of heaven "
                               "and earth' (mare shemayya we-ar'a) encompasses both "
                               "the divine council above and the human realm below. "
                               "When Abraham pays tithes to Melchizedek, he "
                               "acknowledges the priest-king's authority as "
                               "representative of this supreme God. The Qumran "
                               "community would later develop this tradition in a "
                               "dramatic direction, placing Melchizedek within the "
                               "divine council itself as the presiding judge of the "
                               "eschatological judgment (11Q13 applies Psalm 82:1 — "
                               "'God has taken his place in the divine council; in "
                               "the midst of the gods he holds judgment' — directly "
                               "to Melchizedek). Hebrews 7:3 pushes further, "
                               "describing Melchizedek as 'without father or mother "
                               "or genealogy' — language that echoes the eternal "
                               "existence of divine council members.",

        "sections": [
            {
                "heading": "The War and Lot's Capture (XXII.1-8)",
                "body": "Abraham narrates the war of Chedorlaomer and his allies "
                        "against the five cities of the Jordan plain (Sodom, "
                        "Gomorrah, Admah, Zeboiim, and Bela/Zoar). The Apocryphon "
                        "follows Genesis 14:1-12 but adds geographic specificity "
                        "to the campaign route, tracing the invaders' path through "
                        "Transjordan and the Arabah. When the coalition defeats "
                        "Sodom and carries off captives, Lot is among them. "
                        "Abraham learns of Lot's capture through an escapee (cf. "
                        "Genesis 14:13, 'one who had escaped came and told Abram'). "
                        "The first-person narration transforms the impersonal battle "
                        "account of Genesis into a personal crisis: this is Abraham's "
                        "nephew, the same Lot who accompanied him from Haran, who "
                        "chose the Jordan valley, and who revealed his identity to "
                        "Pharaoh in Egypt. The family relationship heightens the "
                        "dramatic stakes beyond what a third-person account conveys."
            },
            {
                "heading": "Abraham's Military Expedition (XXII.8-13)",
                "body": "Abraham musters his trained men — Genesis 14:14 gives the "
                        "number as 318 — and pursues the coalition northward as far "
                        "as Dan and beyond. The Apocryphon describes the night attack "
                        "and the rout of Chedorlaomer's forces with tactical detail. "
                        "Abraham recovers all the captives and possessions. The "
                        "military narrative is significant in Second Temple tradition: "
                        "it establishes Abraham not merely as a recipient of promises "
                        "but as a man of decisive action who could defeat a coalition "
                        "of four kings with a small personal force. This martial "
                        "portrait served as an inspiration for Jewish resistance in "
                        "the Hellenistic and Roman periods. The Apocryphon's first-person "
                        "narration makes the campaign vivid and personal: Abraham is "
                        "not a distant figure in a chronicle but a warrior recounting "
                        "his own night raid."
            },
            {
                "heading": "Melchizedek's Blessing and the Tithe (XXII.14-end)",
                "body": "After the victory, Abraham encounters Melchizedek, whom "
                        "the Apocryphon explicitly identifies as 'the king of "
                        "Salem — that is, the king of Jerusalem.' This gloss is "
                        "interpretively crucial: it is the earliest known explicit "
                        "identification of Melchizedek's Salem with Jerusalem in a "
                        "narrative text (Psalm 76:2 makes the equation in poetic "
                        "context). Melchizedek brings out food and drink (Genesis "
                        "14:18: 'bread and wine') and blesses Abraham with a formula "
                        "praising 'the Most High God, Lord of heaven and earth.' "
                        "Abraham responds by paying a tithe of all the recovered "
                        "spoils. He then refuses the king of Sodom's offer to keep "
                        "the remaining goods, declaring that he will take nothing "
                        "lest it be said that the king of Sodom made Abraham rich — "
                        "a statement of integrity and sole dependence on God's "
                        "provision. The scene ends with Abraham's return, bringing "
                        "the Apocryphon's preserved text to its close. Any additional "
                        "columns that may have followed — perhaps continuing through "
                        "Genesis 15 (the covenant of the pieces) — are lost."
            }
        ]
    }
]
