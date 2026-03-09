"""
era_01_creation.py — Creation Week (Genesis 1-2)
"""

CHAPTERS = [
    {
        "id": "gen-1",
        "ref": "Genesis 1",
        "chapter_num": 1,
        "title": "In the Beginning \u2014 Creation Week",
        "era": "creation",
        "type": "chapter",

        "synopsis": "Genesis 1 presents God's systematic ordering of the cosmos in six days, moving from chaos (tohu vavohu) to a fully furnished, inhabited world. The structure is deliberate: Days 1\u20133 create realms (light, sky/sea, land), Days 4\u20136 fill those realms with rulers (luminaries, birds/fish, animals/humans). Humanity is created as the climactic act \u2014 image-bearers commissioned to extend God's ordered rule across the earth. The chapter is simultaneously a polemic against Ancient Near Eastern creation myths, asserting that the God of Israel alone is Creator and that celestial bodies are mere objects, not deities.",

        "key_verse": {
            "ref": "Genesis 1:1",
            "text": "In the beginning God created the heavens and the earth.",
            "translation": "ESV"
        },

        "hebrew_terms": ["bara", "asah", "elohim", "elohim_plural", "yom", "tohu_vavohu", "ruach", "tselem", "demut", "adam", "nefesh", "radah", "kabash"],

        "ane_backdrop": "Genesis 1 enters a world already saturated with creation stories. In Mesopotamia, the Enuma Elish describes Marduk slaying the chaos dragon Tiamat and fashioning the world from her corpse. In Egypt, Atum speaks the world into existence from the primordial waters (Nun). Genesis quietly but firmly subverts these narratives: there is no theogony (God has no origin story), no theomachy (no battle to create), and no divine rivalry. The sun and moon \u2014 worshipped as gods throughout the ANE \u2014 are demoted to functional objects ('the greater light,' 'the lesser light') without even being named. Creation is effortless: God speaks, and it is so. The seven-day structure parallels temple inauguration texts (cf. Gudea's temple dedication), suggesting that the cosmos itself is God's temple, with humanity as its priestly caretakers.",

        "second_temple": [
            {
                "source": "Jubilees 2:1\u201316",
                "summary": "Jubilees provides an angelic account of creation week, specifying that angels were created on Day 1 alongside the heavens. It lists 22 categories of created things and emphasizes the Sabbath as cosmically ordained.",
                "relevance": "Fills in a gap Genesis leaves open: when were the angels created? Jubilees answers Day 1, aligning with the divine council reading of 'Let us make' in Genesis 1:26."
            },
            {
                "source": "1 Enoch 69:16\u201325",
                "summary": "The angel Kasbeel (Biqa) is said to have revealed the oath by which creation was established \u2014 the hidden name/power that holds the cosmos together.",
                "relevance": "Reflects Second Temple speculation about the mechanism of creation. God's spoken word (fiat creation) was understood as carrying binding, covenantal force."
            },
            {
                "source": "4Q504 (Words of the Luminaries)",
                "summary": "A liturgical prayer cycle from Qumran that recounts God's creation of Adam, his placement in Eden, and the glory bestowed upon humanity at creation. The Wednesday prayer recounts creation in detail.",
                "relevance": "Demonstrates that the Qumran community used Genesis 1\u20132 creation theology in daily liturgical worship, treating the creation account as the foundation for praise and covenant identity.",
                "canon": False
            },
            {
                "source": "4Q303\u2013305 (Meditation on Creation)",
                "summary": "Fragmentary Qumran texts contemplating the order and purpose of creation. The preserved portions meditate on the arrangement of created things and God's wisdom displayed in the natural order.",
                "relevance": "Shows that creation theology was a subject of sustained intellectual and devotional reflection at Qumran, not merely narrative retelling but philosophical contemplation of God's creative design.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "John 1:1\u20133", "note": "The Logos (Word) as the agent of creation: 'All things were made through him'", "type": "nt"},
            {"ref": "Colossians 1:15\u201317", "note": "Christ as the image of the invisible God, firstborn over all creation", "type": "nt"},
            {"ref": "Hebrews 11:3", "note": "By faith we understand the worlds were framed by God's word", "type": "nt"},
            {"ref": "Psalm 33:6, 9", "note": "By the word of YHWH the heavens were made; He spoke and it was done", "type": "ot"},
            {"ref": "Psalm 104:1\u201330", "note": "Creation hymn paralleling Genesis 1's sequence", "type": "ot"},
            {"ref": "Job 38:4\u20137", "note": "God asks Job where he was when the morning stars sang at creation \u2014 divine council witness", "type": "ot"},
            {"ref": "Isaiah 45:18", "note": "God did not create the earth tohu \u2014 he formed it to be inhabited", "type": "ot"},
            {"ref": "Enuma Elish I\u2013IV", "note": "Marduk defeats Tiamat, creates from her body; Genesis subverts this narrative", "type": "ane"},
            {"ref": "Egyptian Memphite Theology", "note": "Ptah creates by speaking \u2014 parallels to fiat creation", "type": "ane"},
            {"ref": "4Q252 I.1\u20136", "type": "dss", "note": "Commentary on Genesis A reinterprets creation days within Qumran's 364-day solar calendar framework, recalculating the temporal structure of Genesis 1"},
            {"ref": "11Q5 (Psalms Scroll) \u2014 Psalm 154", "type": "dss", "note": "Praises God as Creator of all things; creation theology expressed in liturgical poetry preserved at Qumran"},
            {"ref": "4Q422 (Paraphrase of Genesis and Exodus)", "type": "dss", "note": "Retelling of the creation narrative that paraphrases and expands Genesis 1\u20132, reflecting Qumran's engagement with the creation tradition"}
        ],

        "divine_council_note": "Genesis 1:26 \u2014 'Let US make man in OUR image' \u2014 is the most debated plural in the Bible. Options: (1) Trinity (Christian reading), (2) plural of majesty (grammatically unsupported in Hebrew), (3) God addressing the divine council (Psalm 82, Job 38:7, 1 Kings 22:19\u201322). Michael Heiser argues for option 3: God announces his plan to the assembled council, just as a king might announce a decree to his court. Humans are made in God's image (not the council's), but the council witnesses and participates in the deliberation. This reading is supported by the shift from plural ('let us make') to singular ('so God created') \u2014 God alone does the creating, but the council is the audience.",

        "sections": [
            {
                "heading": "Day 1 \u2014 Light and Darkness (1:1\u20135)",
                "body": "The chapter opens with the most famous sentence in literature: 'In the beginning, God created the heavens and the earth.' The Hebrew bereshit can be translated as an absolute statement ('In the beginning God created...') or as a temporal clause ('When God began to create...'). Either way, verse 2 describes the pre-creation state: tohu vavohu (formless and void), darkness over the deep (tehom \u2014 cognate with Tiamat), and the ruach elohim hovering over the waters. God's first creative act is speech: 'Let there be light.' This light is not solar (the sun comes on Day 4) but primordial \u2014 the fundamental ordering principle that separates the chaos-darkness. God names the light 'Day' and the darkness 'Night,' establishing the day-night cycle and demonstrating sovereignty through the act of naming."
            },
            {
                "heading": "Day 2 \u2014 The Expanse (1:6\u20138)",
                "body": "God creates the raqia ('expanse' or 'firmament') to separate the waters above from the waters below. In ANE cosmology, this is a solid dome holding back the cosmic ocean. Genesis uses this shared conceptual vocabulary without necessarily endorsing its physics \u2014 the point is theological: God masters and divides the chaotic waters. Notably, Day 2 is the only day without the refrain 'and God saw that it was good,' which later Jewish interpreters attributed to the separation (division without resolution) being incomplete until Day 3."
            },
            {
                "heading": "Day 3 \u2014 Land and Vegetation (1:9\u201313)",
                "body": "The waters below gather to reveal dry land. God names them 'Earth' (erets) and 'Seas' (yammim). Then the earth brings forth vegetation: seed-bearing plants and fruit trees. The phrase 'according to its kind' (lemin) establishes categorical order in the biological world. Day 3 receives a double 'it was good' \u2014 one for the land, one for the vegetation \u2014 completing the resolution left open from Day 2. The land-from-water motif reverses the chaos of the deep."
            },
            {
                "heading": "Day 4 \u2014 Sun, Moon, Stars (1:14\u201319)",
                "body": "The luminaries are created as functional markers: for signs, seasons, days, and years. Genesis pointedly refuses to name them 'Shamash' (sun god) or 'Sin' (moon god) \u2014 they are simply 'the greater light' and 'the lesser light.' In every surrounding culture, the sun and moon were primary deities. Genesis reduces them to created objects, servants of the calendar. The stars are mentioned almost as an afterthought: 'He made the stars also.' This is devastating polemic \u2014 the astral deities of Babylon and Egypt are demoted to a subordinate clause."
            },
            {
                "heading": "Day 5 \u2014 Sea Creatures and Birds (1:20\u201323)",
                "body": "God fills the water and sky realms created on Day 2. The 'great sea creatures' (tanninim gedolim) uses a word associated with chaos monsters in other OT passages (Isa 27:1, Psalm 74:13). Here they are simply created things \u2014 Leviathan is God's pet, not his rival. This is the first use of bara since verse 1, perhaps because animate life represents a genuinely new category of existence. God blesses the creatures: 'Be fruitful and multiply' \u2014 the first blessing."
            },
            {
                "heading": "Day 6 \u2014 Animals and Humanity (1:24\u201331)",
                "body": "Land animals appear first, followed by the climactic creation of humanity. The shift to divine deliberation ('Let us make') signals the gravity of this act. Humans are created betselem elohim ('in the image of God') \u2014 a phrase with no parallel in ANE literature applied to common humanity. In Mesopotamia, only the king was the image of the god. Genesis democratizes this: every human, male and female, bears the divine image. The dominion mandate (radah and kabash) commissions humanity as God's viceroys, responsible for stewarding creation. Bara appears three times in verse 27, emphasizing the uniqueness of this creative act."
            },
            {
                "heading": "Day 7 \u2014 The Sabbath Rest (2:1\u20133)",
                "body": "God 'rests' (shabat) \u2014 not from exhaustion but from completion. The seventh day is blessed and made holy (qadash), set apart from the other six. In ANE temple inauguration texts, the deity rests in the completed temple. Genesis 1's seven-day structure mirrors this pattern: the cosmos is God's temple, and his rest signifies that he has taken up residence. The number seven (sheva) is related to the word for oath/covenant (shevuah), lending the Sabbath a covenantal dimension. No 'evening and morning' formula closes Day 7 \u2014 the rest is ongoing."
            }
        ]
    },

    {
        "id": "ane-creation-backdrop",
        "ref": "Historical Context",
        "chapter_num": None,
        "title": "ANE Creation Accounts \u2014 The World Genesis Entered",
        "era": "creation",
        "type": "historical_insert",

        "synopsis": "Genesis 1\u20132 did not emerge in a vacuum. Israel's neighbors had well-developed creation traditions that shaped the conceptual vocabulary and literary conventions Genesis both uses and subverts. Understanding these accounts illuminates what Genesis is arguing and why.",

        "key_verse": None,
        "hebrew_terms": [],
        "ane_backdrop": None,
        "second_temple": [],

        "cross_refs": [
            {"ref": "Enuma Elish (Babylon, ~1100 BC)", "note": "Marduk defeats Tiamat, creates world from her body, humans from blood of slain god Kingu", "type": "ane"},
            {"ref": "Atrahasis Epic (Babylon, ~1700 BC)", "note": "Humans created from clay mixed with divine blood to relieve gods of labor; flood sent when humans become too noisy", "type": "ane"},
            {"ref": "Memphis Creation Text (Egypt)", "note": "Ptah conceives creation in his heart and speaks it into existence \u2014 closest ANE parallel to Genesis fiat creation", "type": "ane"},
            {"ref": "Baal Cycle (Ugarit, ~1400 BC)", "note": "Baal battles Yam (Sea) and Mot (Death); storm-god vs. chaos motif paralleled in Psalms", "type": "ane"},
            {"ref": "1QHa (Hodayot/Thanksgiving Hymns)", "type": "dss", "note": "Creation theology pervades these hymns; the speaker praises God as the one who established the cosmos and assigned all things their purpose from before creation"}
        ],

        "divine_council_note": None,

        "sections": [
            {
                "heading": "Enuma Elish \u2014 The Babylonian Creation Epic",
                "body": "The Enuma Elish ('When on High') is a seven-tablet poem recited at the Babylonian New Year festival. It begins with the mingling of Apsu (fresh water) and Tiamat (salt water) producing the first gods. After a generational conflict, the young warrior-god Marduk agrees to fight the chaos dragon Tiamat in exchange for supremacy over the pantheon. He slays Tiamat, splits her body in two: one half becomes the sky, the other the earth. Humans are created from the blood of Kingu (Tiamat's general) to serve the gods as slave laborers. The parallels with Genesis are structural (watery chaos, separation of waters, six stages of creation, rest) but the theology is opposite. In Genesis: one God, no origin story, no battle, creation by speech, humans as dignified image-bearers, rest as celebration rather than divine fatigue."
            },
            {
                "heading": "Atrahasis \u2014 Creation, Overpopulation, and Flood",
                "body": "The Atrahasis Epic provides the fullest ANE narrative arc from creation through flood. The lesser gods (Igigi) revolt against the labor imposed by the greater gods (Anunnaki). The solution: create humans from clay mixed with the blood of a slain god to take over the work. When human population grows and the 'noise' (perhaps rebellion or simply overbreeding) disturbs the gods, they send plague, famine, and finally a flood. One wise man (Atrahasis) is warned and builds a boat. This is the closest ANE parallel to the Genesis 1\u201311 narrative arc, and the flood portion closely parallels Genesis 6\u20139."
            },
            {
                "heading": "What Genesis Is Doing Differently",
                "body": "Genesis shares vocabulary and narrative structure with these traditions but makes radical theological claims. (1) Monotheism: no theogony, no pantheon rivalry. (2) Creation by speech: no battle, no struggle, no divine blood required. (3) Human dignity: image-bearers, not slave laborers. (4) Moral order: judgment comes from ethical violation (sin), not divine irritation (noise). (5) Covenant: God enters into binding relationship with creation and with specific humans. (6) De-divinization of nature: sun, moon, sea, storms are created things, not gods. Genesis is not merely telling a story \u2014 it is making an argument about the nature of God, humanity, and the cosmos."
            },
            {
                "heading": "Sources and Further Reading",
                "body": "Primary texts: ANET (Ancient Near Eastern Texts, Pritchard ed.), COS (Context of Scripture, Hallo & Younger eds.). Key studies: John Walton, 'The Lost World of Genesis One' (2009); Michael Heiser, 'The Unseen Realm' (2015); Bruce Waltke, 'Genesis: A Commentary' (2001). For Enuma Elish: Stephanie Dalley, 'Myths from Mesopotamia' (Oxford, 2000)."
            }
        ]
    },

    {
        "id": "gen-2",
        "ref": "Genesis 2",
        "chapter_num": 2,
        "title": "The Garden of Eden \u2014 God's Temple-Garden",
        "era": "creation",
        "type": "chapter",

        "synopsis": "Genesis 2 zooms in from the cosmic panorama of chapter 1 to focus on humanity's creation and vocation. The man is formed from the dust of the ground (adamah), placed in a garden-sanctuary (gan-Eden), and given the priestly task of 'working and keeping' it \u2014 the same Hebrew pair later used for Levitical service. The woman is built from the man's side as his ezer kenegdo (corresponding helper). Eden is presented as the intersection of heaven and earth: rivers flow out from it, precious stones adorn it, and God walks within it. This is not a second creation account contradicting chapter 1, but a complementary narrative that develops the human story in detail.",

        "key_verse": {
            "ref": "Genesis 2:7",
            "text": "Then the LORD God formed the man of dust from the ground and breathed into his nostrils the breath of life, and the man became a living creature.",
            "translation": "ESV"
        },

        "hebrew_terms": ["yhwh", "adam", "adamah", "gan", "ezer_kenegdo", "nefesh", "ets_haddaat", "ets_hachayyim", "ruach"],

        "ane_backdrop": "The Eden narrative draws on widespread ANE motifs: the sacred garden, the tree of life, the divine craftsman molding humans from clay, and the four rivers marking the center of the world. In Mesopotamian literature, the garden of the gods (particularly Dilmun in Sumerian tradition) is a paradise of abundance. The Gilgamesh Epic features a quest for the plant of immortality, which is ultimately lost to a serpent. Ezekiel 28:12\u201319 describes Eden as a 'garden of God' on a holy mountain, adorned with precious stones \u2014 language that merges garden and temple imagery. The 'working and keeping' (abad and shamar) of Genesis 2:15 is the same word pair used for Levitical priestly service (Numbers 3:7\u20138), indicating that Adam's role was inherently sacral.",

        "second_temple": [
            {
                "source": "Jubilees 3:1\u201335",
                "summary": "Jubilees specifies that Adam was created on Day 6 in the land of Elda (outside Eden), then brought into the garden after 40 days. Eve was created after 80 days. The garden is described as the 'Holy of Holies' of the earth.",
                "relevance": "Jubilees makes explicit what Genesis implies: Eden = temple. Adam enters the garden the way a priest enters the sanctuary, after a period of purification."
            },
            {
                "source": "1 Enoch 24\u201325",
                "summary": "Enoch sees the tree of life on a holy mountain, surrounded by fragrant trees. The archangel Michael explains that after the great judgment, the righteous will eat from this tree and live forever.",
                "relevance": "Connects the tree of life in Eden to eschatological hope. What was lost in Genesis 3 will be restored at the end of the age (cf. Revelation 22:2)."
            },
            {
                "source": "4Q504 (Words of the Luminaries) frag. 8",
                "summary": "A Qumran liturgical text that describes Adam's original state in Eden: 'You fashioned Adam our father in the likeness of your glory; the breath of life you breathed into his nostril, and intelligence and knowledge you gave him.' Adam is depicted as having been clothed in divine glory before the Fall.",
                "relevance": "Provides the DSS witness to the 'glory of Adam' tradition \u2014 the belief that Adam possessed a luminous, glory-filled state in Eden that was lost through sin and will be restored to the righteous. This tradition shaped Qumran's self-understanding as a community seeking to recover Adamic glory.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Ezekiel 28:12\u201319", "note": "Eden as the garden of God on the holy mountain, with guardian cherub and precious stones", "type": "ot"},
            {"ref": "Ezekiel 47:1\u201312", "note": "River flowing from the eschatological temple, trees of life on its banks", "type": "ot"},
            {"ref": "Revelation 22:1\u20135", "note": "River of life and tree of life restored in the New Jerusalem", "type": "nt"},
            {"ref": "1 Corinthians 15:45\u201349", "note": "Adam as the first man (natural), Christ as the last Adam (spiritual)", "type": "nt"},
            {"ref": "2 Corinthians 11:3", "note": "Paul references Eve's deception in Eden as a warning", "type": "nt"},
            {"ref": "Numbers 3:7\u20138", "note": "Levites 'keep charge' (shamar) of the tabernacle \u2014 same priestly language as Gen 2:15", "type": "ot"},
            {"ref": "Epic of Gilgamesh XI", "note": "Utnapishtim's garden, plant of immortality stolen by serpent", "type": "ane"},
            {"ref": "4Q504 (Words of the Luminaries) frag. 8", "type": "dss", "note": "Recounts Adam's glory in Eden before the Fall \u2014 'You fashioned Adam our father in the likeness of your glory' \u2014 the most explicit DSS reference to Edenic splendor"},
            {"ref": "4Q252 col. I", "type": "dss", "note": "Commentary on Genesis A includes comments bearing on the Eden narrative and its chronological framework within the Qumran calendar"}
        ],

        "divine_council_note": "Genesis 2 introduces YHWH Elohim (the LORD God) \u2014 combining the personal covenant name with the title used of the divine council head. The garden setting evokes a divine council meeting place: Ezekiel 28:13\u201314 places an anointed cherub 'in Eden, the garden of God' on 'the holy mountain of God,' walking among 'stones of fire.' This connects Eden to the heavenly throne room, with cherubim as its guardians. When Adam is placed in the garden to 'work and keep' (abad/shamar) it, he is given a quasi-priestly role in God's earthly throne room \u2014 maintaining the sacred space where heaven meets earth.",

        "sections": [
            {
                "heading": "YHWH Elohim \u2014 The Combined Name (2:4\u20137)",
                "body": "Genesis 2:4 marks a transition with the toledot formula ('these are the generations of...'), which structures the entire book of Genesis. The name shifts from Elohim (chapter 1) to YHWH Elohim. Source critics attributed this to different authors (J and P sources), but the combined name serves a theological purpose: the transcendent Creator God (Elohim) is also the personal, relational covenant God (YHWH). The account zooms in: before any plant had grown (because there was no rain and no human to work the ground), YHWH Elohim forms the man from the adamah (ground). The wordplay adam/adamah is foundational \u2014 humanity is tied to the earth, drawn from it and destined to return to it."
            },
            {
                "heading": "The Breath of Life (2:7)",
                "body": "God forms (yatsar \u2014 the potter's verb) the man from dust and breathes (naphach) into his nostrils the breath of life (nishmat chayyim). The man becomes a living being (nefesh chayyah). This is intimate, hands-on creation \u2014 very different from the majestic speech-acts of chapter 1. The nefesh is not a separable 'soul' imprisoned in a body (Greek dualism) but the whole person animated by God's breath. When the breath departs, the nefesh ceases. The same phrase nefesh chayyah was used of animals in Genesis 1:20\u201324 \u2014 humans share creatureliness with animals but are uniquely formed by God's own hands and breath."
            },
            {
                "heading": "The Garden and Its Geography (2:8\u201314)",
                "body": "God plants a garden 'in Eden, in the east.' Eden (from Sumerian edin, 'plain/steppe,' or Hebrew eden, 'delight') is a region; the garden is within it. Four rivers flow from Eden: Pishon (near Havilah, with gold, bdellium, and onyx), Gihon (near Cush), Tigris (east of Asshur), and Euphrates. The geography is semi-mythological: two rivers are identifiable (Tigris, Euphrates), two are not. The garden sits at the cosmic center where waters originate \u2014 a motif shared with Ezekiel's temple vision (Ezek 47). The precious stones (gold, bdellium, onyx) anticipate the materials of the tabernacle and high priest's garments, reinforcing the Eden-as-temple reading."
            },
            {
                "heading": "The Two Trees (2:9, 15\u201317)",
                "body": "Two trees occupy the center of the garden: the tree of life (ets hachayyim) and the tree of the knowledge of good and evil (ets haddaat tov vara). The tree of life grants ongoing life; access to it will be blocked after the Fall (Gen 3:22\u201324). The tree of knowledge is the subject of the single prohibition: 'You shall not eat of it, for in the day you eat of it you shall surely die' (mot tamut \u2014 'dying you shall die'). 'Knowledge of good and evil' is debated: (a) moral discernment, (b) experiential knowledge (knowing by doing), (c) a merism for all knowledge, or (d) the authority to determine right and wrong independently of God. Options (c) and (d) are most likely \u2014 seizing autonomous moral authority is the essence of the temptation in chapter 3."
            },
            {
                "heading": "Adam's Priestly Vocation (2:15)",
                "body": "YHWH Elohim places the man in the garden to 'work it and keep it' (le'ovdah uleshomrah). These verbs \u2014 abad ('to serve/work') and shamar ('to keep/guard') \u2014 appear together elsewhere only in priestly contexts. Numbers 3:7\u20138 uses the same pair for the Levites' duty in the tabernacle. The man is not merely a gardener but a priestly guardian of sacred space. His job is to maintain the holiness of the garden-temple, to tend God's earthly dwelling. This priestly role will be violated in chapter 3 when he fails to guard the garden against the intruder."
            },
            {
                "heading": "Naming the Animals (2:18\u201320)",
                "body": "God declares 'It is not good for the man to be alone' \u2014 the first 'not good' in a creation declared 'very good.' To demonstrate this, God brings every animal to the man for naming. In the ANE, naming implies authority and understanding: the man perceives each creature's nature and assigns it a name (shem). But among all the animals, no suitable counterpart (ezer kenegdo) is found. The naming parade serves to reveal the man's need: he is qualitatively different from the animal kingdom and requires a partner who corresponds to him."
            },
            {
                "heading": "The Creation of Woman (2:21\u201325)",
                "body": "God causes a deep sleep (tardemah) to fall on the man and builds (banah) the woman from his side (tsela \u2014 traditionally 'rib,' but the word means 'side' or 'panel' elsewhere, as in the side of the tabernacle). The man's response is the first human speech and the first poem in the Bible: 'This at last is bone of my bones and flesh of my flesh; she shall be called Woman (ishah), for she was taken out of Man (ish).' The wordplay ish/ishah expresses correspondence and equality. The narrator adds: 'Therefore a man shall leave his father and mother and hold fast to his wife, and they shall become one flesh.' The chapter closes with primal innocence: 'they were both naked (arummim) and were not ashamed' \u2014 a wordplay that sets up chapter 3, where the serpent is described as 'crafty' (arum)."
            }
        ]
    }
]
