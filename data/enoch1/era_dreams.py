"""
era_dreams.py — Book of Dream Visions (1 Enoch 83-90)

The Book of Dream Visions contains two vision-dreams that Enoch recounts
to his son Methuselah. The first (83-84) is a brief vision of the coming
Flood and Enoch's prayer for the preservation of a remnant. The second
(85-90) is the Animal Apocalypse — one of the most remarkable allegorical
texts in Second Temple Judaism, retelling all of biblical history from
Adam to the eschatological future through animal symbolism.

Aramaic fragments: 4Q204 (4QEn-c) preserves portions of the Animal
Apocalypse (corresponding to 1 Enoch 89). 4Q207 (4QEn-f) contains
fragments from the Book of Dream Visions. The text was composed in the
Maccabean period (c. 164-160 BC), as the Animal Apocalypse's historical
survey extends to the Maccabean revolt (the "great horn" of 90:9).

The Animal Apocalypse's code:
  White bulls    = patriarchs (Adam, Seth, Noah, Shem, Abraham, Isaac)
  Black/brown    = Ham, rejected lines
  Sheep/rams     = Israel / faithful Jews
  Wolves/lions   = oppressing nations (Egyptians, Babylonians, etc.)
  Stars/angels   = Watchers who fell
  Shepherds      = the 70 angelic shepherds of the nations
  Great horn     = Judas Maccabeus

Translation references: R.H. Charles (1912), P. Tiller (1993),
G.W.E. Nickelsburg & J.C. VanderKam (Hermeneia, 2012).
"""

CHAPTERS = [
    # =========================================================================
    # THE FLOOD VISION (1 Enoch 83-84)
    # =========================================================================
    {
        "id": "1en-83-84",
        "ref": "1 Enoch 83-84",
        "chapter_num": 83,
        "title": "The First Dream Vision — Enoch Sees the Flood",
        "era": "dreams",
        "type": "chapter",

        "synopsis": "The Book of Dream Visions opens with a brief but powerful "
                    "vision-dream in which the young Enoch sees the earth swallowed "
                    "by a cosmic catastrophe. In the vision, the sky collapses and "
                    "the earth is swallowed into an abyss. Enoch wakes terrified and "
                    "interprets the vision as a prophecy of the coming Flood. He "
                    "falls on his face and prays an extended prayer of praise and "
                    "petition, asking God to preserve a righteous remnant on earth. "
                    "The prayer (ch. 84) is one of the finest liturgical compositions "
                    "in the Enochic corpus, praising God as sovereign over all "
                    "creation and begging him not to destroy the earth entirely.",

        "key_verse": {
            "ref": "1 Enoch 84:2-3",
            "text": "Blessed be Thou, O Lord, King, great and mighty in Thy "
                    "greatness, Lord of the whole creation of the heaven, King "
                    "of kings and God of the whole world... O God and Lord and "
                    "Great King, I implore and beseech Thee to fulfil my prayer, "
                    "to leave me a posterity on earth, and not destroy all the "
                    "flesh of man.",
            "translation": "Charles"
        },

        "original_terms": [
            "mabbul",
            "tehom",
            "shamayim",
            "tsaddiq",
            "mishpat",
            "kavod",
        ],

        "ane_backdrop": "Prophetic dreams and visions warning of catastrophe are a "
                        "standard ANE literary convention. In the Atrahasis epic, the "
                        "god Ea warns the flood hero through a dream or through the "
                        "wall of his reed hut. In the Gilgamesh Epic (Tablet XI), "
                        "Utnapishtim receives a similar warning. The Enochic "
                        "innovation is that the warning comes not to the flood hero "
                        "(Noah) but to his great-grandfather (Enoch), who sees the "
                        "catastrophe generations before it occurs. The prayer of "
                        "chapter 84 transforms the ANE flood-warning pattern from a "
                        "private escape plan into a cosmic liturgical appeal.",

        "second_temple": [
            {
                "source": "Jubilees 7:20-39",
                "summary": "Noah instructs his sons after the Flood, warning them "
                           "about the blood-consuming of the Watchers' offspring and "
                           "the violence that provoked the deluge.",
                "relevance": "Jubilees provides the post-Flood perspective that "
                             "complements 1 Enoch 83-84's pre-Flood warning: together "
                             "they frame the Flood narrative from both sides.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 6:5-13", "note": "God's assessment that the earth is corrupt and filled with violence, and his decision to destroy it — the judgment that Enoch's dream anticipates", "type": "ot"},
            {"ref": "Genesis 7:11", "note": "The fountains of the deep burst forth and the windows of heaven were opened — the de-creation event that Enoch sees as the sky collapsing and the earth swallowed", "type": "ot"},
            {"ref": "Genesis 8:21-22", "note": "God's promise never again to curse the ground or destroy every living creature — the answer to Enoch's prayer in chapter 84", "type": "ot"},
            {"ref": "2 Peter 3:5-7", "note": "The world was deluged with water and perished, and the present heavens and earth are stored up for fire — Peter's recapitulation of the Flood/judgment pattern that the Dream Visions narrate", "type": "nt"},
            {"ref": "Matthew 24:37-39", "note": "As were the days of Noah, so will be the coming of the Son of Man — Jesus uses the Flood as a type of eschatological judgment, the same typological framework underlying the Dream Visions", "type": "nt"},
            {"ref": "4Q207 (4QEn-f)", "type": "dss", "note": "Fragmentary Aramaic manuscript containing portions of the Book of Dream Visions, confirming its circulation at Qumran"}
        ],

        "divine_council_note": "Enoch's prayer in chapter 84 addresses God specifically "
                               "as the sovereign of the divine council: 'Lord of the "
                               "whole creation of the heaven, King of kings.' The "
                               "petition to preserve a remnant is an appeal within the "
                               "council's judicial proceedings — Enoch, already established "
                               "as a council participant (chapters 12-16), exercises his "
                               "standing to petition on behalf of humanity. This sets the "
                               "pattern for prophetic intercession: the prophet who has "
                               "been admitted to the council (cf. Jer 23:18) uses that "
                               "access to plead for his people.",

        "sections": [
            {
                "heading": "The Vision of Destruction (83:1-9)",
                "body": "Enoch tells Methuselah that 'before I took thy mother Edna, "
                        "I saw in a vision on my bed' a terrifying sight: 'the heaven "
                        "was thrown down and removed, and it fell to the earth... and "
                        "the earth was swallowed up in a great abyss' (83:3-4, Charles). "
                        "The imagery is of de-creation — the firmament collapsing and "
                        "the earth dissolving into the primordial deep (tehom). This "
                        "reverses the separations of Genesis 1:6-10, where God divided "
                        "the waters above from the waters below and gathered the waters "
                        "to reveal dry land. In Enoch's vision, those separations are "
                        "undone: heaven meets earth meets abyss. The young Enoch wakes "
                        "terrified and finds his grandfather Mahalalel, who interprets: "
                        "'A great destruction cometh on the earth, and the earth is "
                        "about to be destroyed' (83:7). This short vision establishes "
                        "the Flood as a de-creation event — not merely a natural "
                        "disaster but a cosmic unmaking that reverses the creative "
                        "acts of Genesis 1."
            },
            {
                "heading": "Enoch's Prayer for a Remnant (84:1-6)",
                "body": "Chapter 84 contains Enoch's prayer response — a liturgical "
                        "text of exceptional beauty. He begins with praise: 'Blessed "
                        "be Thou, O Lord, King, great and mighty in Thy greatness, "
                        "Lord of the whole creation of the heaven, King of kings and "
                        "God of the whole world. Thy power and kingship and greatness "
                        "abide for ever and ever, and throughout all generations Thy "
                        "dominion' (84:2). This hymnic opening establishes the "
                        "framework: God is praised as cosmic sovereign precisely when "
                        "the cosmos is about to be destroyed. The juxtaposition is "
                        "deliberate — even de-creation is under God's sovereign control. "
                        "Enoch's petition follows: 'I implore and beseech Thee to "
                        "fulfil my prayer, to leave me a posterity on earth, and not "
                        "destroy all the flesh of man, and make the earth without "
                        "inhabitant' (84:3). The plea for a 'posterity' (literally "
                        "'seed,' zera) echoes the zera promise of Genesis 3:15 and "
                        "the seed-line theology of Genesis 5. Enoch asks that the "
                        "line of promise not be severed by the Flood. The prayer "
                        "ends with a vision of the restored earth: 'And now, my "
                        "Lord and King, may it please Thee to establish the word of "
                        "my prayer... that the race of the righteous may never "
                        "fail' (84:6). This is prophetic intercession at its purest: "
                        "a seer who knows the judgment is coming pleading for mercy "
                        "within it."
            }
        ]
    },

    # =========================================================================
    # THE ANIMAL APOCALYPSE (1 Enoch 85-90)
    # =========================================================================
    {
        "id": "1en-85-87",
        "ref": "1 Enoch 85-87",
        "chapter_num": 85,
        "title": "The Animal Apocalypse — From Adam to the Watchers",
        "era": "dreams",
        "type": "chapter",

        "synopsis": "Chapters 85-87 open the Animal Apocalypse, a sweeping allegorical "
                    "retelling of all biblical history using animal symbolism. Adam is "
                    "a white bull, Eve a heifer, Cain and Abel are black and red "
                    "bullocks. The patriarchs are white bulls. In chapter 86, the "
                    "Watcher descent is portrayed as stars falling from heaven and "
                    "becoming bulls that mingle with the heifers (human women), "
                    "producing elephants, camels, and asses (the Nephilim). Chapter "
                    "87 introduces the four archangels as 'men' (the only figures "
                    "described in human form) who are commissioned from heaven to "
                    "deal with the crisis. The symbolic code transforms familiar "
                    "biblical narrative into an apocalyptic drama that would have "
                    "been immediately recognizable to Second Temple readers.",

        "key_verse": {
            "ref": "1 Enoch 86:1-3",
            "text": "And again I saw with mine eyes as I slept, and I saw the "
                    "heaven above, and behold a star fell from heaven, and it arose "
                    "and ate and pastured amongst those oxen. And after that I saw "
                    "the large and the black oxen, and behold they all changed "
                    "their stalls and pastures and their cattle, and began to "
                    "live with each other.",
            "translation": "Charles"
        },

        "original_terms": ["bene_elohim", "nephilim"],

        "ane_backdrop": "Animal symbolism for nations and rulers is widespread in the "
                        "ANE. Egyptian art depicts the pharaoh as a bull trampling "
                        "enemies. Mesopotamian texts use animal imagery for nations: "
                        "the lion for Babylon, the eagle for Assyria. Daniel's four "
                        "beasts (Daniel 7) represent successive empires. The Animal "
                        "Apocalypse extends this tradition into a comprehensive "
                        "allegorical system where every nation, patriarch, and "
                        "supernatural being is encoded in animal form. The closest "
                        "ANE parallel to the Animal Apocalypse's comprehensive "
                        "historical allegory is the Prophecy of Neferti and similar "
                        "Egyptian predictive texts that narrate past history as if "
                        "it were future prophecy.",

        "second_temple": [
            {
                "source": "Daniel 7:1-8",
                "summary": "Four great beasts emerge from the sea: a lion, a bear, "
                           "a leopard, and a terrifying fourth beast — nations "
                           "represented as animals, the same symbolic technique used "
                           "in the Animal Apocalypse.",
                "relevance": "Daniel 7 and the Animal Apocalypse share the technique "
                             "of encoding nations as animals, but the Animal Apocalypse "
                             "is far more comprehensive: it covers all of biblical "
                             "history, not just the eschatological empires.",
                "canon": False
            },
            {
                "source": "Testament of Joseph 19:3-8",
                "summary": "A vision of a lamb that defeats the beasts "
                           "(enemy nations). Animal symbolism for eschatological "
                           "conflict.",
                "relevance": "Shows that animal-allegory for salvation history was a "
                             "broader Second Temple literary technique, not unique to "
                             "the Animal Apocalypse.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 6:1-4", "note": "The Watcher descent and Nephilim — encoded in the Animal Apocalypse as stars falling from heaven and producing monstrous animal offspring (elephants, camels, asses)", "type": "ot"},
            {"ref": "Daniel 7:1-8", "note": "Four beasts representing nations — the same animal-symbolism technique that the Animal Apocalypse uses on a far larger scale", "type": "ot"},
            {"ref": "Daniel 8:3-8, 20-21", "note": "The ram (Media-Persia) and the goat (Greece) — Daniel's animal symbols for specific nations parallel the Animal Apocalypse's comprehensive system", "type": "ot"},
            {"ref": "Revelation 5:6", "note": "The Lamb standing as though slain — Revelation's central animal symbol, a Lamb representing the Messiah, follows the same tradition as the Animal Apocalypse's sheep/rams for Israel", "type": "nt"},
            {"ref": "Isaiah 14:12", "note": "How you are fallen from heaven, O Day Star — the fallen-star motif that the Animal Apocalypse applies to the Watchers (86:1)", "type": "ot"},
            {"ref": "4Q204 col. iv (4QEn-c)", "type": "dss", "note": "Aramaic fragments preserving portions of the Animal Apocalypse (corresponding to 1 Enoch 89), confirming this text circulated at Qumran"},
            {"ref": "Jude 13", "note": "Wandering stars for whom the gloom of utter darkness has been reserved forever — echoing the Animal Apocalypse's depiction of fallen stars (Watchers) cast into darkness", "type": "nt"}
        ],

        "divine_council_note": "The Animal Apocalypse's symbolic system reveals its "
                               "divine council theology through its choice of form: "
                               "all beings are encoded as animals EXCEPT the archangels "
                               "and God, who appear in human form. This inverts normal "
                               "expectation: humans are depicted as animals, while "
                               "divine beings appear as 'men.' The implication is that "
                               "true humanity — bearing the image of God — belongs to "
                               "the heavenly realm. Earthly beings are animalistic in "
                               "their nature and behavior; only the council members "
                               "appear in the form of the divine image.",

        "sections": [
            {
                "heading": "From Adam to the Flood — Bulls and Stars (85:1 - 86:6)",
                "body": "The second dream vision begins with Adam: 'a bull came forth "
                        "from the earth, and that bull was white' (85:3). The white "
                        "bull represents purity and divine favor. Eve is 'a heifer' "
                        "that comes forth alongside him. Their offspring: a black "
                        "bullock (Cain) and a red/white bullock (Abel). The black "
                        "bullock gores the red one (Cain murders Abel), and a white "
                        "bullock is born (Seth). The Sethite genealogy follows as "
                        "successive white bulls, maintaining the color symbolism of "
                        "purity. Then chapter 86 introduces the Watcher descent in "
                        "stunning visual language: 'A star fell from heaven' (86:1) — "
                        "the leader of the Watchers. Then 'many stars descended and "
                        "cast themselves down from heaven to that first star, and they "
                        "became bulls amongst those cattle and pastured with them "
                        "amongst them' (86:3). The stars-become-bulls mingling with "
                        "the heifers (human women) is the Genesis 6:1-4 narrative "
                        "in symbolic code. The offspring are grotesque: 'they began to "
                        "beget elephants, and great beasts, and asses' (86:4) — the "
                        "Nephilim rendered as monstrous animals that do not belong to "
                        "any natural category. The choice of elephants and camels "
                        "conveys their unnatural size and violence."
            },
            {
                "heading": "The Four Men from Heaven — Archangelic Intervention (87:1-4)",
                "body": "Chapter 87 introduces the divine response: 'I saw heaven "
                        "above, and four white men came out of that place... they "
                        "began to push those great ones, and to seize and take and "
                        "bind them all, and to cast them into an abyss of the earth' "
                        "(87:1-3, Charles). The 'four white men' are the four "
                        "archangels (Michael, Gabriel, Raphael, Uriel), and they "
                        "execute the judgment described in 1 Enoch 10. Only the "
                        "archangels appear in human form — every other figure in the "
                        "allegory is an animal. This is the Animal Apocalypse's most "
                        "significant symbolic choice: the divine council members alone "
                        "bear the form of humanity. They are 'men' in the truest "
                        "sense — bearing the image and authority of God. The earthly "
                        "beings, for all their importance in salvation history, are "
                        "rendered as creatures of instinct and earth. The archangels "
                        "seize one of the stars (Azazel), bind him, and cast him into "
                        "the abyss. They cause the giant offspring to destroy one "
                        "another. One of them (Uriel) approaches the 'white bull' "
                        "(Noah) to warn him of the Flood."
            },
            {
                "heading": "The Flood and the Preservation of Noah (88:1 - 89:1)",
                "body": "Chapter 88 describes the Flood in animal-apocalypse code: "
                        "'I saw the heaven of heavens, and a star that had fallen, and "
                        "they took it and threw it into an abyss... full of fire and "
                        "flaming and full of pillars of fire' (88:1, the imprisonment "
                        "of a Watcher leader). The other fallen stars are bound hand "
                        "and foot and 'cast into an abyss of the earth' (88:3). Then "
                        "one of the four men (Uriel) 'came to that white bull and "
                        "instructed him in a secret: he was born a bull and became a "
                        "man' (89:1) — Noah is transformed from animal to human form, "
                        "signifying his elevation to a quasi-angelic status. Noah "
                        "'built a vessel and dwelt therein; and three bulls dwelt with "
                        "him in that vessel' (89:1) — Shem, Ham, and Japheth. The "
                        "Flood is described as 'a great quantity of water fell down "
                        "from heaven' until 'all the earth was filled with water' "
                        "(89:2-3). After the Flood, Noah's status is confirmed by his "
                        "human form: he has been admitted to the company of the "
                        "'four men' — the divine council. This transformation from "
                        "bull to man echoes Genesis 6:9's 'Noah walked with God' — "
                        "the same phrase used for Enoch in Genesis 5:24."
            }
        ]
    },

    # =========================================================================
    # THE ANIMAL SYMBOLISM SYSTEM (1 Enoch 85-89)
    # =========================================================================
    {
        "id": "1en-animal-symbolism",
        "ref": "1 Enoch 85-89",
        "chapter_num": 88,
        "title": "The Zoomorphic Code — Who Is Which Animal?",
        "era": "dreams",
        "type": "chapter",

        "synopsis": "The Animal Apocalypse employs a remarkably consistent system of "
                    "animal symbolism that encodes every nation, patriarch, and spiritual "
                    "being in the biblical narrative. Understanding this code is essential "
                    "for reading the allegory. Israel\'s history is marked by a crucial "
                    "species transition: the patriarchs from Adam to Jacob are bulls "
                    "(autonomous, powerful), but from Jacob onward Israel becomes sheep "
                    "(vulnerable, dependent on a shepherd). The Gentile nations are wild "
                    "predators: wolves (Egypt), dogs (Philistia), lions (Babylon), "
                    "leopards (Assyria), ravens (Seleucids). The Watchers appear as "
                    "falling stars, the archangels as white men, and the Nephilim as "
                    "grotesque hybrid animals (elephants, camels, asses). Color carries "
                    "moral weight: white signals purity and divine favor, black signals "
                    "sin, red signals martyrdom or violence.",

        "key_verse": {
            "ref": "1 Enoch 89:12",
            "text": "And that bull which was born... begat twelve sheep. And those "
                    "twelve sheep grew, and they became very many flocks.",
            "translation": "Charles"
        },

        "original_terms": [
            "nephilim",
            "egregoroi",
            "bene_elohim",
            "gibborim",
            "malak_yhwh",
            "goy",
        ],

        "ane_backdrop": "Animal symbolism for nations and rulers is among the oldest "
                        "literary conventions in the ANE. Egyptian pharaohs were depicted "
                        "as bulls trampling enemies on battle palettes (the Narmer Palette, "
                        "c. 3100 BC). Mesopotamian boundary stones (kudurru) use animal "
                        "symbols for deities and kingdoms. The Sumerian literature refers "
                        "to kings as \'wild bull\' (am-si) as a title of power. The lion "
                        "was Babylon\'s signature animal (the Ishtar Gate featured rows of "
                        "lions). Persia was associated with the bull (cf. Daniel 8:3-4, "
                        "the ram). The Animal Apocalypse draws on this shared ANE "
                        "convention but creates a system far more comprehensive than any "
                        "single predecessor, encoding all of salvation history in a "
                        "unified zoomorphic framework.",

        "second_temple": [
            {
                "source": "Daniel 7:3-7 + 8:3-8, 20-21",
                "summary": "Daniel uses animal symbols for specific empires: the lion "
                           "(Babylon), bear (Media), leopard (Persia), terrifying beast "
                           "(Greece), ram (Media-Persia), and goat (Greece). Daniel 8 "
                           "even provides an angelic interpretation key.",
                "relevance": "Daniel and the Animal Apocalypse are roughly contemporary "
                             "(both from the Maccabean crisis) and share the technique of "
                             "encoding nations as animals. But Daniel\'s system is limited "
                             "to empires, while the Animal Apocalypse encodes ALL of "
                             "history — patriarchs, exodus, monarchy, exile, and eschaton.",
                "canon": False
            },
            {
                "source": "4 Ezra 11-12 (Eagle Vision)",
                "summary": "A later Jewish apocalypse (c. 100 AD) depicts Rome as a "
                           "twelve-winged, three-headed eagle rising from the sea, "
                           "confronted by a lion (the Messiah).",
                "relevance": "Shows that zoomorphic apocalyptic persisted well beyond "
                             "the Maccabean period. The eagle vision of 4 Ezra continues "
                             "the tradition that the Animal Apocalypse represents at an "
                             "earlier stage.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 49:9-27", "note": "Jacob\'s blessing assigns animal symbols to the tribes: Judah is a lion, Issachar a donkey, Dan a serpent, Naphtali a doe, Benjamin a wolf — the patriarchal tradition of zoomorphic tribal identity", "type": "ot"},
            {"ref": "Daniel 7:3-7", "note": "Four beasts from the sea representing four empires — the canonical parallel to the Animal Apocalypse\'s comprehensive zoomorphic system", "type": "ot"},
            {"ref": "Daniel 8:3-8, 20-21", "note": "The ram (Medo-Persia) and the goat (Greece) with angelic interpretation — the only canonical text that explicitly decodes its own animal symbolism", "type": "ot"},
            {"ref": "Ezekiel 34:1-31", "note": "Israel as sheep under negligent shepherds — the pastoral metaphor that the Animal Apocalypse adopts as its primary framework for Israel\'s history from Jacob onward", "type": "ot"},
            {"ref": "Psalm 80:1", "note": "Shepherd of Israel... you who lead Joseph like a flock — the OT \'God as shepherd of Israel\' tradition that the Animal Apocalypse renders as \'the Lord of the sheep\'", "type": "ot"},
            {"ref": "John 10:11-16", "note": "I am the good shepherd... I have other sheep not of this fold — Jesus employs the same sheep/shepherd metaphor that structures the entire Animal Apocalypse", "type": "nt"},
            {"ref": "Revelation 5:5-6", "note": "The Lion of Judah who is also the Lamb — Revelation combines two animal symbols into one messianic figure, continuing the zoomorphic tradition", "type": "nt"}
        ],

        "divine_council_note": "The Animal Apocalypse\'s most theologically significant "
                               "symbolic choice is that divine beings — God and the "
                               "archangels — appear in HUMAN form while humans appear as "
                               "animals. The \'Lord of the sheep\' is a man, the four "
                               "archangels are \'white men,\' and only Noah is elevated "
                               "from bull to man (89:1). This inversion reveals the "
                               "author\'s theology of the imago Dei: true \'humanity\' "
                               "(the image of God) belongs to the divine realm. Earthly "
                               "creatures, even the patriarchs and prophets, are rendered "
                               "as animals — beings of instinct, vulnerability, and "
                               "mortality. Only admission to the divine council confers "
                               "the \'human\' form that reflects the Creator\'s image.",

        "sections": [
            {
                "heading": "The Bull-to-Sheep Transition — A Theological Shift",
                "body": "The most important symbolic transition in the Animal Apocalypse "
                        "occurs at Jacob. The patriarchs from Adam through Isaac are white "
                        "bulls — powerful, autonomous creatures that represent the "
                        "pre-Israelite righteous line. Abraham is \'a white bull\' (89:10), "
                        "Isaac is \'a white bull\' (89:11). But Jacob \'begat twelve sheep\' "
                        "(89:12). The shift from bull to sheep is not a demotion but a "
                        "theological statement: Israel is a flock, not a herd. Bulls are "
                        "self-sufficient; sheep require a shepherd. The transformation "
                        "signals Israel\'s covenantal dependence on God — they cannot "
                        "survive without divine protection. This is the pastoral theology "
                        "of Psalm 23 (\'The LORD is my shepherd\') and Ezekiel 34 encoded "
                        "in allegorical form. The vulnerability of sheep also makes the "
                        "narrative of oppression viscerally powerful: wolves attacking "
                        "lambs is a more emotionally charged image than predators "
                        "attacking bulls."
            },
            {
                "heading": "The Predator Nations — A Bestiary of Oppression",
                "body": "Each oppressing nation receives a specific animal identity. "
                        "The Egyptians are wolves — the primary predators of the flock "
                        "during the exodus (89:13-17). The Philistines are dogs — "
                        "persistent, aggressive enemies in the Judges and early monarchic "
                        "period. The Edomites (Esau\'s descendants) are wild boars or "
                        "swine — animals associated with ritual impurity in Israelite "
                        "law (Lev 11:7). The Assyrians are leopards — swift, deadly "
                        "predators associated with the destruction of the northern "
                        "kingdom. The Babylonians are lions — the great beast that "
                        "destroys the Temple and scatters the flock, matching Daniel "
                        "7:4\'s identification of Babylon with the lion. The Seleucid "
                        "Greeks are ravens and kites — birds of prey that tear at the "
                        "sheep in the final period before divine intervention (90:2-4). "
                        "The choice of ravens for the Seleucids may reflect the "
                        "association of ravens with impurity (Lev 11:15) and with the "
                        "scavenging of corpses."
            },
            {
                "heading": "Color, Form, and Moral Status",
                "body": "Color in the Animal Apocalypse is never neutral. White "
                        "consistently signals divine favor, purity, and righteousness: "
                        "Adam is a white bull (85:3), the archangels are white men "
                        "(87:2), and the eschatological messiah is a white bull with "
                        "great horns (90:37). Black signals sin and deviation from the "
                        "righteous line: Cain is a black bullock (85:3), and the line "
                        "of Ham includes black cattle. Red appears with Abel (a red "
                        "bullock, 85:3) — suggesting blood and martyrdom — and with "
                        "certain Japhethite lines. The Nephilim receive the most "
                        "striking treatment: they are \'elephants, camels, and asses\' "
                        "(86:4) — creatures that belong to no single category, whose "
                        "monstrous size and unnatural grouping visually conveys the "
                        "ontological wrongness of the Watcher-human hybrid. These "
                        "animals are not native to the pastoral world of bulls and "
                        "sheep; they are foreign intrusions that disrupt the created "
                        "order, just as the Nephilim disrupt the boundary between "
                        "heaven and earth."
            }
        ]
    },

    # =========================================================================
    # THE 70 SHEPHERDS (1 Enoch 89:59 - 90:19)
    # =========================================================================
    {
        "id": "1en-70-shepherds",
        "ref": "1 Enoch 89:59 - 90:19",
        "chapter_num": 89,
        "title": "The Seventy Shepherds — Angelic Rulers of the Nations",
        "era": "dreams",
        "type": "chapter",

        "synopsis": "The most theologically dense passage in the Animal Apocalypse is the "
                    "appointment and judgment of the 70 angelic shepherds. After the "
                    "destruction of Solomon\'s Temple, God appoints 70 angelic beings to "
                    "manage Israel\'s punishment during and after the exile. Each shepherd "
                    "is given a specific quota of sheep (Israelites) that may be destroyed. "
                    "But the shepherds exceed their mandate — they destroy more than God "
                    "commanded. A recording angel keeps meticulous count of every excess "
                    "killing. The 70 shepherds are divided into four periods (12 + 23 + "
                    "23 + 12 = 70), corresponding to the Babylonian, Persian, Ptolemaic, "
                    "and Seleucid eras. This passage provides the most developed theology "
                    "of divine national administration in Second Temple literature, "
                    "building directly on the Deuteronomy 32:8 tradition that God assigned "
                    "the nations to divine beings.",

        "key_verse": {
            "ref": "1 Enoch 89:59-60",
            "text": "And He called seventy shepherds, and cast those sheep to them "
                    "that they might pasture them, and He spake to the shepherds and "
                    "to their companions: \'Let each individual of you pasture the "
                    "sheep henceforward, and everything that I shall command you "
                    "that do.\'",
            "translation": "Charles"
        },

        "original_terms": ["bene_elohim"],

        "ane_backdrop": "The concept of deities assigned to govern specific nations is "
                        "fundamental to ANE polytheism. Each Mesopotamian city had its "
                        "patron deity (Marduk for Babylon, Ashur for Assyria, Sin for "
                        "Ur), and the fortunes of the city were understood as reflecting "
                        "the standing of its god in the divine assembly. The Israelite "
                        "tradition of Deuteronomy 32:8-9 (reading with 4QDeut-j and LXX: "
                        "\'according to the number of the sons of God\') transforms this "
                        "polytheistic concept into a monotheistic framework: God assigns "
                        "the nations to subordinate divine beings but keeps Israel for "
                        "himself. The Animal Apocalypse\'s 70 shepherds develop this "
                        "tradition further: the number 70 corresponds to the 70 nations "
                        "of the Table of Nations (Genesis 10) and the 70 divine beings "
                        "who received national assignments.",

        "second_temple": [
            {
                "source": "Daniel 10:13, 20-21; 12:1",
                "summary": "The \'prince of Persia\' resists the angelic messenger for 21 "
                           "days; Michael is called \'your prince\' (Israel\'s guardian). "
                           "The \'prince of Greece\' is mentioned as a future adversary.",
                "relevance": "Daniel 10 is the closest canonical parallel to the 70 "
                             "shepherds: nations have angelic rulers, and conflicts between "
                             "nations reflect conflicts between their angelic patrons. "
                             "Daniel names specific national angels; the Animal Apocalypse "
                             "numbers them collectively as 70.",
                "canon": False
            },
            {
                "source": "Jubilees 15:31-32",
                "summary": "God created spirits to rule over all nations, but over Israel "
                           "he set no angel or spirit — \'he alone is their ruler.\'",
                "relevance": "Jubilees preserves the same Deuteronomy 32 tradition but "
                             "emphasizes that Israel\'s direct relationship with God means "
                             "the 70 shepherds of the Animal Apocalypse are an emergency "
                             "measure during punishment, not a permanent arrangement.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9 (LXX/4QDeut-j)", "note": "When the Most High divided the nations, he fixed their borders according to the number of the sons of God — the theological foundation for the 70 angelic shepherds assigned to govern the nations", "type": "ot"},
            {"ref": "Genesis 10:1-32", "note": "The Table of Nations listing 70 descendants of Noah\'s sons — the canonical basis for the number 70 as the total of nations and their corresponding angelic overseers", "type": "ot"},
            {"ref": "Daniel 10:13, 20-21", "note": "National angelic princes (Persia, Greece, Israel/Michael) — the canonical parallel to the Animal Apocalypse\'s angelic shepherds governing national affairs", "type": "ot"},
            {"ref": "Zechariah 1:15", "note": "I am angry with the nations that are at ease; I was only a little angry, but they furthered the disaster — exactly the problem with the 70 shepherds who exceed their punishment mandate", "type": "ot"},
            {"ref": "Isaiah 10:5-7", "note": "Assyria, the rod of my anger — God uses Assyria to punish Israel, but Assyria goes too far and will be judged. The same pattern governs the 70 shepherds", "type": "ot"},
            {"ref": "Ezekiel 34:1-10", "note": "Woe to the shepherds of Israel who feed themselves instead of the flock — the prophetic indictment of negligent shepherds that the Animal Apocalypse applies to angelic rulers", "type": "ot"},
            {"ref": "Luke 10:1", "note": "Jesus appoints 70 (or 72) others and sends them ahead — some scholars connect the number 70 to the nations tradition, suggesting Jesus is commissioning agents for ALL nations", "type": "nt"},
            {"ref": "Revelation 12:7-9", "note": "Michael and his angels fighting against the dragon — the eschatological angelic warfare that the Animal Apocalypse anticipates with Michael\'s role as Israel\'s defender", "type": "nt"}
        ],

        "divine_council_note": "The 70 shepherds passage is the most theologically "
                               "sophisticated treatment of the divine council\'s national "
                               "governance in all Second Temple literature. It addresses "
                               "three critical problems: (1) Why does God allow pagan "
                               "nations to oppress Israel? Answer: He appointed angelic "
                               "shepherds to administer measured punishment. (2) Why is "
                               "the punishment so excessive? Answer: The shepherds exceeded "
                               "their quotas. (3) Will the excess be addressed? Answer: "
                               "A recording angel has documented every violation, and the "
                               "shepherds will face judgment at the eschaton (90:22-25). "
                               "The divine council is not a perfect bureaucracy — its "
                               "members can fail, overreach, and be held accountable. This "
                               "is the Enochic answer to the problem of theodicy: God\'s "
                               "plan is just, but its execution by delegated agents can "
                               "be corrupted, and that corruption itself will be judged.",

        "sections": [
            {
                "heading": "The Appointment and the Quotas (89:59-64)",
                "body": "After the destruction of the First Temple (\'they forsook the "
                        "house of the Lord,\' 89:56), God appoints 70 angelic shepherds "
                        "to manage Israel\'s discipline. The commissioning speech is "
                        "remarkably precise: \'Let each individual of you pasture the "
                        "sheep henceforward, and everything that I shall command you "
                        "that do. And I will deliver them over unto you duly numbered, "
                        "and tell you which of them are to be destroyed, and them "
                        "destroy ye\' (89:59-60). God specifies exact quotas — the number "
                        "of sheep each shepherd may destroy is predetermined. This is "
                        "not random imperial violence but calibrated divine discipline. "
                        "Yet immediately the text notes: \'They destroyed more than I "
                        "commanded them\' (implicit in the recording angel\'s accounting, "
                        "89:61-64). A second angel is appointed to record every excess "
                        "killing: \'Write down every excess which the shepherds effect, "
                        "more than I have commanded them\' (89:61). This recording angel "
                        "creates the judicial evidence that will be used at the final "
                        "trial — the \'books\' opened in 90:20."
            },
            {
                "heading": "The Four Periods (89:65 - 90:5)",
                "body": "The 70 shepherds are divided into four groups operating in "
                        "four successive periods. Most scholars follow Charles\'s "
                        "division: (1) 12 shepherds in the Babylonian period (586-"
                        "538 BC); (2) 23 shepherds in the Persian period (538-333 BC); "
                        "(3) 23 shepherds in the Ptolemaic period (333-200 BC); (4) 12 "
                        "shepherds in the Seleucid period (200-164 BC). The uneven "
                        "distribution (12-23-23-12) is significant: the first and last "
                        "periods are shorter and more intense, while the middle periods "
                        "are longer. The total of 70 connects to multiple biblical "
                        "patterns: the 70 years of exile (Jeremiah 25:11-12), Daniel\'s "
                        "70 weeks (Daniel 9:24), and the 70 nations of Genesis 10. "
                        "The fourth period, corresponding to the Seleucid persecution, "
                        "is the author\'s own era — and the excess of the shepherds is "
                        "at its worst. The ravens and kites (Seleucid armies) attack "
                        "the sheep with unprecedented ferocity (90:2-4), and God\'s "
                        "wrath burns against the shepherds who permitted this excess."
            },
            {
                "heading": "The Theological Problem — Excessive Punishment",
                "body": "The 70 shepherds passage addresses one of the most agonizing "
                        "questions in Jewish theology: why did Israel\'s punishment "
                        "exceed what seemed proportionate? The exile was God\'s judgment "
                        "— the prophets said so explicitly (Isaiah, Jeremiah, Ezekiel). "
                        "But the suffering went far beyond anything the prophets "
                        "seemed to predict. The Babylonian destruction, the Persian "
                        "domination, the Ptolemaic exploitation, and especially the "
                        "Seleucid desecration — where was the proportionality? The "
                        "Animal Apocalypse answers: God\'s punishment was proportionate, "
                        "but the angelic administrators exceeded their mandates. The "
                        "excess was their sin, not God\'s. This answer preserves both "
                        "divine justice (God\'s original sentence was fair) and accounts "
                        "for disproportionate suffering (the agents went rogue). "
                        "Zechariah 1:15 makes the same point canonically: \'I was only "
                        "a little angry, but they furthered the disaster.\' The 70 "
                        "shepherds develop this single prophetic verse into a fully "
                        "elaborated theology of delegated judgment gone wrong."
            }
        ]
    },

    {
        "id": "1en-89-90",
        "ref": "1 Enoch 89-90",
        "chapter_num": 89,
        "title": "The Animal Apocalypse — From Abraham to the Maccabees",
        "era": "dreams",
        "type": "chapter",

        "synopsis": "Chapters 89-90 continue the Animal Apocalypse through the entire "
                    "sweep of biblical history: the patriarchs as white bulls, the "
                    "exodus from Egypt (sheep escaping wolves), the wilderness "
                    "wandering, the judges (rams with horns), the monarchy (the tower = "
                    "Solomon's Temple), the divided kingdom, the destruction of the "
                    "Temple, the exile (sheep scattered among wild beasts), and the "
                    "70 shepherds appointed to punish Israel. The allegory reaches "
                    "its climax with the Maccabean period: a 'great horn' (Judas "
                    "Maccabeus) grows on one of the sheep and fights against the "
                    "ravens (the Seleucids). The vision concludes with the eschaton: "
                    "a new Jerusalem, the conversion of the nations, and the birth "
                    "of a white bull with great horns — the Messiah.",

        "key_verse": {
            "ref": "1 Enoch 90:37-38",
            "text": "And I saw that a white bull was born, with large horns, and "
                    "all the beasts of the field and all the birds of the air "
                    "feared him and made petition to him at all times. And I saw "
                    "till all their generations were transformed, and they all "
                    "became white bulls.",
            "translation": "Charles"
        },

        "original_terms": [
            "bene_elohim",
            "goy",
            "malak_yhwh",
            "mishpat",
            "mashiach",
            "egregoroi",
        ],

        "ane_backdrop": "The concept of divinely appointed angelic overseers of "
                        "nations has deep roots in the ANE divine council tradition. "
                        "Deuteronomy 32:8-9 (reading with 4QDeut-j and the LXX: "
                        "'according to the number of the sons of God') assigns each "
                        "nation to a divine being, with YHWH taking Israel as his "
                        "own portion. The Animal Apocalypse's 70 shepherds develop "
                        "this tradition: after the exile, God appoints 70 angelic "
                        "shepherds to oversee Israel's punishment, but they exceed "
                        "their mandate and oppress the sheep excessively. The "
                        "number 70 corresponds to the 70 nations of the Table of "
                        "Nations (Genesis 10) and the 70 divine beings who receive "
                        "the nations in Deuteronomy 32.",

        "second_temple": [
            {
                "source": "Daniel 10:13, 20-21; 12:1",
                "summary": "The 'prince of Persia,' the 'prince of Greece,' and "
                           "Michael as Israel's prince — angelic beings assigned to "
                           "nations, matching the Animal Apocalypse's 70 shepherds.",
                "relevance": "Daniel's national angels are the canonical expression "
                             "of the same tradition that the Animal Apocalypse "
                             "develops: each nation has a divine overseer, and the "
                             "conflicts between nations reflect conflicts between "
                             "their angelic patrons.",
                "canon": False
            },
            {
                "source": "Jubilees 15:31-32",
                "summary": "God made spirits to rule over all nations but set no "
                           "spirit over Israel — he himself rules Israel directly.",
                "relevance": "Jubilees preserves the same tradition as the Animal "
                             "Apocalypse's 70 shepherds: the nations are under angelic "
                             "administration, but Israel's relationship to God is "
                             "direct. The 70 shepherds of the Animal Apocalypse are "
                             "thus an aberration — temporary appointees during Israel's "
                             "punishment, not permanent arrangements.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9", "note": "When the Most High divided the nations, he fixed their borders according to the number of the sons of God (b'nei 'elohim) — the theological basis for the 70 shepherds", "type": "ot"},
            {"ref": "Daniel 10:13, 20-21", "note": "National angelic princes (Persia, Greece, Israel/Michael) — the canonical parallel to the Animal Apocalypse's angelic shepherds of the nations", "type": "ot"},
            {"ref": "Ezekiel 34:1-10", "note": "God's indictment of Israel's shepherds who feed themselves instead of the flock — the background for the Animal Apocalypse's critique of the 70 shepherds who exceed their punishment mandate", "type": "ot"},
            {"ref": "Zechariah 1:15", "note": "I am angry with the nations that are at ease; I was only a little angry, but they furthered the disaster — exactly the problem with the 70 shepherds: they over-punish", "type": "ot"},
            {"ref": "Matthew 25:32", "note": "Before him will be gathered all the nations, and he will separate them — the eschatological judgment scene that culminates the Animal Apocalypse's sweep of history", "type": "nt"},
            {"ref": "Revelation 21:1-5", "note": "A new heaven and new earth, the new Jerusalem coming down from God — the eschatological renewal that the Animal Apocalypse anticipates with its 'new house' (the new Temple) in 90:28-29", "type": "nt"},
            {"ref": "4Q204 col. iv (4QEn-c)", "type": "dss", "note": "Aramaic fragments of the Animal Apocalypse corresponding to 1 Enoch 89, the historical survey section covering the patriarchs through the monarchy"},
            {"ref": "Psalm 74:1-2", "note": "Why does your anger smoke against the sheep of your pasture? Remember your congregation — the sheep imagery for Israel that the Animal Apocalypse adopts as its primary symbol", "type": "ot"},
            {"ref": "1 Maccabees 3:1-9", "note": "Judas Maccabeus rises to fight for Israel against the Seleucids — the historical figure behind the Animal Apocalypse's 'great horn' of 90:9", "type": "ot"}
        ],

        "divine_council_note": "The 70 shepherds of the Animal Apocalypse represent "
                               "the most developed theology of divine national "
                               "administration in Second Temple literature. God "
                               "appoints 70 angelic beings to manage the punishment "
                               "of Israel during and after the exile, allotting to each "
                               "a specific number of sheep that may be destroyed. But "
                               "the shepherds exceed their quotas: they destroy more "
                               "than God commanded. This excess becomes itself a crime "
                               "that will be judged at the eschaton (90:22-25). The "
                               "theological problem is the same as Zechariah 1:15 and "
                               "Isaiah 10:5-7: God uses the nations (and their angelic "
                               "patrons) as instruments of judgment, but they go beyond "
                               "their mandate and must themselves be judged. The divine "
                               "council is not a perfect bureaucracy: its members can "
                               "fail, exceed authority, and face consequences.",

        "sections": [
            {
                "heading": "Israel as Sheep — Exodus through Monarchy (89:10-50)",
                "body": "After the Flood and the patriarchal period (rendered as white "
                        "bulls), the allegory transitions at Jacob: 'that bull which "
                        "was born... begat twelve sheep' (89:12) — the twelve tribes. "
                        "The transformation from bulls to sheep marks a theological "
                        "shift: Israel's vulnerability and dependence on God increase. "
                        "The sheep descend to Egypt ('wolves began to pursue those "
                        "lambs,' 89:14). Moses is a sheep who is commissioned by "
                        "'the Lord of the sheep' (89:16). The Exodus is depicted as "
                        "the sheep fleeing from the wolves through a divided body of "
                        "water (89:24-25). The wilderness period features the sheep "
                        "'blinded' — they cannot see and wander (89:28, the golden "
                        "calf and wilderness rebellions). 'A man' (Moses) builds a "
                        "house for the Lord of the sheep (the Tabernacle, 89:36). "
                        "Judges are rams with horns who fight off the wild beasts "
                        "(89:42-49). Samuel and David appear as rams. The 'tower' is "
                        "constructed (Solomon's Temple, 89:50): 'they began to build, "
                        "and they placed a table before the tower, and all the bread "
                        "on it was polluted and not pure.' Even the first Temple's "
                        "bread of the Presence is not fully pure — a subtle critique "
                        "suggesting that Israel's worship was compromised from the "
                        "beginning."
            },
            {
                "heading": "The 70 Shepherds — Exile and the Second Temple (89:59 - 90:5)",
                "body": "After the destruction of Solomon's Temple ('they forsook the "
                        "house of the Lord and the tower,' 89:56), God appoints 70 "
                        "angelic shepherds to manage Israel's punishment. 'The Lord of "
                        "the sheep called seventy shepherds, and cast those sheep to "
                        "them that they might pasture them, and he said to the "
                        "shepherds and their companions: \"Let each individual of you "
                        "pasture the sheep henceforward, and everything that I shall "
                        "command you, that do. And I will deliver them over unto you "
                        "duly numbered, and tell you which of them are to be destroyed, "
                        "and them destroy ye\"' (89:59-60). The quotas are precise: "
                        "God specifies exactly how many sheep each shepherd may "
                        "destroy. But the shepherds exceed their mandate: 'They "
                        "destroyed more than I commanded them' (89:61, implicit). "
                        "A recording angel ('another angel,' possibly Enoch himself, "
                        "89:61) keeps account of every excess killing. The 70 "
                        "shepherds are divided into four periods (12 + 23 + 23 + 12), "
                        "which scholars have mapped onto historical epochs: the "
                        "Babylonian, Persian, Ptolemaic, and Seleucid periods. The "
                        "second Temple is built ('the sheep returned to and built "
                        "that house,' 89:72-73), but the bread on its table is also "
                        "'polluted and impure' — the Enochic critique of the Second "
                        "Temple establishment."
            },
            {
                "heading": "The Great Horn and the Eschaton (90:6-38)",
                "body": "The Animal Apocalypse reaches its historical present and "
                        "then projects into the eschatological future. Lambs with "
                        "opened eyes are born (the Enochic-Hasidic movement, 90:6): "
                        "'lambs were born by those white sheep, and they began to open "
                        "their eyes and to see.' The rams (leaders who resist the "
                        "oppressors) call to the sheep but the sheep 'did not hear' "
                        "(90:7). Ravens (Seleucids/Antiochus Epiphanes) attack the "
                        "sheep viciously. Then: 'a great horn sprouted on one of those "
                        "sheep' (90:9) — Judas Maccabeus. The great horn fights the "
                        "ravens and receives divine assistance. The eschatological "
                        "climax follows: God himself ('the Lord of the sheep') "
                        "descends in wrath (90:14-15). The sword is given to the "
                        "sheep (90:19). The abyss opens and the fallen stars "
                        "(Watchers) are cast in (90:24). The 70 shepherds are judged "
                        "for exceeding their mandates (90:25). The 'blinded sheep' "
                        "(faithless Israelites) are also cast in (90:26). The old "
                        "house (the corrupt Temple) is removed and a new house (the "
                        "eschatological Temple) is set up (90:28-29). The nations "
                        "come and worship. Finally, 'a white bull was born, with "
                        "large horns' (90:37) — the Messiah, depicted in the same "
                        "terms as Adam (85:3), indicating a return to the original "
                        "created order. All creatures are transformed into white "
                        "bulls: creation is restored to its pre-Fall purity."
            }
        ]
    },

    {
        "id": "1en-90-eschaton",
        "ref": "1 Enoch 90:20-42",
        "chapter_num": 90,
        "title": "The Final Judgment and the New Creation",
        "era": "dreams",
        "type": "chapter",

        "synopsis": "The climactic conclusion of the Animal Apocalypse describes the "
                    "final judgment in extraordinary detail. The Lord of the sheep "
                    "takes his judicial seat. Three categories of defendants are "
                    "brought before him: the fallen stars (Watchers), the 70 "
                    "shepherds who exceeded their mandate, and the blinded sheep "
                    "(faithless Israelites). All are cast into a fiery abyss. The "
                    "old Temple is folded up and a new, greater Temple replaces it. "
                    "Diaspora Jews return, Gentile nations submit, and a white bull "
                    "with great horns is born — the Messiah who restores creation to "
                    "its Edenic purity. All creatures become white bulls, and the "
                    "first white bull (Adam? the Messiah?) is exalted.",

        "key_verse": {
            "ref": "1 Enoch 90:28-29",
            "text": "And I saw till the Lord of the sheep brought a new house "
                    "greater and loftier than that first, and set it up in the place "
                    "of the first which had been folded up: all its pillars were new, "
                    "and its ornaments were new and larger than those of the first.",
            "translation": "Charles"
        },

        "original_terms": [
            "mishpat",
            "egregoroi",
            "mashiach",
            "qodesh",
            "goy",
            "olam",
            "sheol",
        ],

        "ane_backdrop": "The replacement of an old temple with a new, greater one is "
                        "a common ANE royal motif. Mesopotamian kings regularly "
                        "described their temple renovations as replacements of old, "
                        "inadequate structures with new, grander ones. The Enuma Elish "
                        "culminates in the construction of Marduk's temple, Esagila, "
                        "by the gods. Ezekiel's temple vision (chs. 40-48) describes "
                        "a radically new temple that replaces Solomon's. The Animal "
                        "Apocalypse's 'new house' draws on all these traditions: the "
                        "eschatological Temple is the fulfillment of both the ANE "
                        "temple-building tradition and the prophetic hope for a "
                        "restored sanctuary.",

        "second_temple": [
            {
                "source": "Revelation 21:1-22:5",
                "summary": "The new heaven and new earth with the new Jerusalem "
                           "descending from God, no temple because the Lord God and "
                           "the Lamb are its temple, the tree of life restored.",
                "relevance": "Revelation's new creation vision directly parallels the "
                             "Animal Apocalypse's conclusion: the old world is "
                             "replaced, the corrupt temple is removed, and a new, "
                             "greater divine dwelling takes its place. Revelation goes "
                             "further by eliminating the temple entirely — God's "
                             "presence fills the city.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 65:17-25", "note": "New heavens and new earth, no more weeping, the wolf and the lamb feeding together — the prophetic new creation that the Animal Apocalypse's ending embodies", "type": "ot"},
            {"ref": "Ezekiel 40-48", "note": "Ezekiel's eschatological temple vision — the prophetic background for the 'new house' of 90:28-29 that replaces the corrupt second Temple", "type": "ot"},
            {"ref": "Revelation 20:11-15", "note": "The great white throne judgment, books opened, the dead judged — the Apocalypse's judgment scene parallels the Animal Apocalypse's three-fold trial (Watchers, shepherds, blinded sheep)", "type": "nt"},
            {"ref": "Revelation 21:1-5", "note": "Behold, I am making all things new — the final transformation that corresponds to the Animal Apocalypse's vision of all creatures becoming white bulls", "type": "nt"},
            {"ref": "Daniel 7:9-10, 22, 26", "note": "The court sat in judgment, books were opened, dominion was given to the holy ones — the Danielic judgment scene that the Animal Apocalypse elaborates", "type": "ot"},
            {"ref": "Psalm 96:13", "note": "The LORD comes to judge the earth; he will judge the world in righteousness — the OT affirmation of cosmic judgment that the Animal Apocalypse dramatizes", "type": "ot"},
            {"ref": "Romans 8:19-23", "note": "The creation itself will be set free from its bondage to corruption — the Pauline vision of cosmic renewal that echoes the Animal Apocalypse's universal transformation", "type": "nt"}
        ],

        "divine_council_note": "The judgment scene in 90:20-27 is a formal divine "
                               "council trial with three categories of defendants: "
                               "(1) the fallen stars/Watchers — the original rebels; "
                               "(2) the 70 shepherds — angelic administrators who "
                               "exceeded their mandate; (3) the blinded sheep — "
                               "unfaithful members of God's own people. The judgment "
                               "is comprehensive: it addresses cosmic rebellion (the "
                               "Watchers), administrative corruption (the shepherds), "
                               "and human faithlessness (the blind sheep). The Lord "
                               "of the sheep presides personally — this is the final "
                               "assize when all delegated authority returns to the "
                               "supreme judge. The 'fiery abyss' to which they are "
                               "consigned is the same prison described in the Book of "
                               "the Watchers (1 Enoch 10, 18-19), now in its final "
                               "function as permanent punishment rather than temporary "
                               "holding.",

        "sections": [
            {
                "heading": "The Three-Fold Judgment (90:20-27)",
                "body": "The Lord of the sheep takes his judicial seat: 'I saw till a "
                        "throne was erected in the pleasant land, and the Lord of the "
                        "sheep sat himself thereon, and the other took the sealed books "
                        "and opened those books before the Lord of the sheep' (90:20). "
                        "The 'sealed books' are the records kept by the recording angel "
                        "since 89:61 — the detailed account of every excess committed "
                        "by the 70 shepherds. Three groups are tried in sequence. "
                        "First, the stars (Watchers): 'I saw till those seven white "
                        "ones (archangels) brought those stars and the first star "
                        "which had fallen, and they were all judged and found guilty, "
                        "and were cast into an abyss full of fire and flaming' "
                        "(90:24). Second, the 70 shepherds: 'I saw at that time how "
                        "a like abyss was opened in the midst of the earth, and they "
                        "brought those shepherds and cast them into that deep abyss' "
                        "(90:25). Third, the blinded sheep: 'the blinded sheep too "
                        "were judged and found guilty and were cast into that fiery "
                        "abyss' (90:26). The three categories represent cosmic evil "
                        "(Watchers), delegated abuse (shepherds), and willful "
                        "faithlessness (blind sheep). Judgment is proportional but "
                        "universal: no category escapes."
            },
            {
                "heading": "The New Temple and the Messianic Bull (90:28-38)",
                "body": "After the judgment, the old Temple is removed: 'I saw till "
                        "the Lord of the sheep brought a new house greater and "
                        "loftier than that first, and set it up in the place of the "
                        "first which had been folded up' (90:28-29). The 'folding up' "
                        "of the old house is a powerful image — the entire corrupt "
                        "Temple system is simply packed away like a tent, and a new, "
                        "greater structure replaces it. The diaspora sheep return: "
                        "'all the sheep were invited, and they came to that house, "
                        "and it could not contain them' (90:34) — the eschatological "
                        "regathering. The Gentile nations come and submit: 'all the "
                        "beasts of the field and all the birds of the air assembled "
                        "in that house, and the Lord of the sheep rejoiced with great "
                        "joy because they were all good' (90:33). Then the climactic "
                        "birth: 'a white bull was born, with large horns, and all "
                        "the beasts of the field and all the birds of the air feared "
                        "him and made petition to him at all times' (90:37). This "
                        "is the Messiah, and his white-bull form deliberately echoes "
                        "Adam's form in 85:3. The Messiah restores creation to its "
                        "Edenic state. Finally, 'all their generations were "
                        "transformed, and they all became white bulls' (90:38) — "
                        "universal restoration. Every creature returns to the original "
                        "created form. This is the Animal Apocalypse's version of "
                        "'Behold, I am making all things new' (Rev 21:5)."
            }
        ]
    },

    # =========================================================================
    # THE WHITE BULL MESSIAH AND THE MACCABEAN DATING (1 Enoch 90:6-42)
    # =========================================================================
    {
        "id": "1en-90-messiah-dating",
        "ref": "1 Enoch 90:6-42",
        "chapter_num": 90,
        "title": "The Great Horn, the White Bull, and the Maccabean Context",
        "era": "dreams",
        "type": "chapter",

        "synopsis": "The climactic section of the Animal Apocalypse contains two figures "
                    "of immense theological importance: the \'great horn\' (90:9), "
                    "universally identified as Judas Maccabeus, and the \'white bull with "
                    "large horns\' (90:37), the eschatological messiah. The great horn "
                    "provides the primary evidence for dating the Animal Apocalypse to "
                    "the Maccabean period (c. 164-160 BC). The white bull messiah "
                    "represents an Adamic restoration — a return to the original created "
                    "purity of Genesis 1-2. The relationship between these two figures "
                    "(historical deliverer and eschatological restorer) and their "
                    "connections to Daniel\'s \'one like a son of man\' (Dan 7:13) and "
                    "Revelation\'s Lamb (Rev 5:6) illuminate the diversity of Jewish "
                    "messianic expectation in the late Second Temple period.",

        "key_verse": {
            "ref": "1 Enoch 90:9, 37",
            "text": "And I saw till a great horn sprouted on one of those sheep, and "
                    "their eyes were opened... And I saw that a white bull was born, "
                    "with large horns, and all the beasts of the field and all the birds "
                    "of the air feared him and made petition to him at all times.",
            "translation": "Charles"
        },

        "original_terms": [
            "mashiach",
            "ben_adam",
            "goy",
            "gibborim",
            "mishpat",
            "olam",
        ],

        "ane_backdrop": "The horn as a symbol of power and authority is ubiquitous in "
                        "the ANE. Mesopotamian kings wore horned crowns to indicate "
                        "divine authority. The Ugaritic texts describe Baal as \'the "
                        "bull\' (tr) with horns. In Israelite tradition, the horn "
                        "symbolizes strength (1 Samuel 2:1, \'my horn is exalted in "
                        "the LORD\'), anointing (1 Samuel 16:1, the horn of oil), and "
                        "royal power (Psalm 132:17, \'I will make a horn to sprout for "
                        "David\'). The \'great horn\' of the Animal Apocalypse draws on "
                        "all these associations: Judas Maccabeus is a divinely empowered "
                        "warrior-king figure who rises from among the vulnerable sheep "
                        "to challenge the predatory ravens.",

        "second_temple": [
            {
                "source": "1 Maccabees 3:1-9",
                "summary": "Judas Maccabeus rises to lead the resistance: \'He extended "
                           "the glory of his people. Like a giant he put on his "
                           "breastplate; he armed himself with weapons of war and waged "
                           "battles, protecting the camp by his sword.\'",
                "relevance": "1 Maccabees provides the historical basis for the Animal "
                             "Apocalypse\'s \'great horn.\' The description of Judas as a "
                             "warrior who protects the camp and makes \'kings tremble\' "
                             "corresponds to the great horn that fights the ravens and "
                             "whose eyes are opened (divine empowerment).",
                "canon": False
            },
            {
                "source": "Daniel 7:13-14",
                "summary": "One like a son of man comes with the clouds of heaven, "
                           "is presented before the Ancient of Days, and receives "
                           "everlasting dominion over all nations.",
                "relevance": "Daniel\'s \'one like a son of man\' and the Animal "
                             "Apocalypse\'s white bull messiah are contemporary messianic "
                             "conceptions from the Maccabean crisis. Daniel\'s figure is "
                             "more clearly supernatural (coming on clouds); the Animal "
                             "Apocalypse\'s is more connected to Adamic restoration (a "
                             "bull, recalling Adam the first white bull).",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 7:13-14", "note": "The \'one like a son of man\' who receives dominion — a contemporary but distinct messianic conception from the same Maccabean crisis that produced the white bull messiah", "type": "ot"},
            {"ref": "Daniel 8:5-8", "note": "The goat with a \'conspicuous horn\' (Alexander the Great) — Daniel also uses the horn symbol for powerful leaders, but for a pagan king rather than a Jewish deliverer", "type": "ot"},
            {"ref": "1 Maccabees 3:1-9", "note": "The historical Judas Maccabeus who inspired the \'great horn\' of 90:9 — the warrior who rallied the faithful and challenged the Seleucid empire", "type": "ot"},
            {"ref": "Psalm 132:17", "note": "I will make a horn to sprout for David — the Davidic horn tradition that feeds both the \'great horn\' of 90:9 and the messianic white bull of 90:37", "type": "ot"},
            {"ref": "Isaiah 11:6-9", "note": "The wolf shall dwell with the lamb — the Isaianic peaceable kingdom that the Animal Apocalypse envisions when all creatures become white bulls (90:38)", "type": "ot"},
            {"ref": "Revelation 5:5-6", "note": "The Lion of Judah who is also the Lamb — Revelation\'s double animal symbol for the Messiah, combining the power imagery (lion) with the vulnerable imagery (lamb) that the Animal Apocalypse distributes across two figures (horn and bull)", "type": "nt"},
            {"ref": "Romans 8:19-22", "note": "The creation waits with eager longing for the revealing of the sons of God — Paul\'s cosmic restoration vision echoes the Animal Apocalypse\'s transformation of all creatures into white bulls", "type": "nt"},
            {"ref": "1 Corinthians 15:22-28", "note": "As in Adam all die, so in Christ all shall be made alive — the Adamic restoration that the white bull messiah (recalling Adam the first white bull) symbolizes", "type": "nt"}
        ],

        "divine_council_note": "The eschatological climax of the Animal Apocalypse is a "
                               "council event. God descends in wrath (90:14-15), the "
                               "judgment throne is erected (90:20), sealed books are opened "
                               "(90:20), and three categories of defendants are tried. The "
                               "\'great horn\' (Judas Maccabeus) fights with divine "
                               "assistance but is not the final agent of restoration — that "
                               "role belongs to the Lord of the sheep himself and to the "
                               "eschatological white bull. The distinction between the "
                               "historical deliverer (the horn) and the eschatological "
                               "restorer (the bull) maps onto a two-stage eschatology: "
                               "present liberation through human agency assisted by God, "
                               "followed by ultimate restoration through direct divine "
                               "intervention and a messianic figure who reverses the Fall "
                               "itself.",

        "sections": [
            {
                "heading": "The Great Horn — Judas Maccabeus (90:6-16)",
                "body": "The Maccabean revolt enters the allegory with dramatic force. "
                        "\'Lambs were born by those white sheep, and they began to open "
                        "their eyes and to see\' (90:6) — the Hasidim, the pious Jewish "
                        "movement that initially supported the Maccabees. The opened eyes "
                        "signal prophetic awareness: these lambs can see reality clearly "
                        "in contrast to the \'blinded\' sheep of earlier periods. Then: "
                        "\'a great horn sprouted on one of those sheep\' (90:9) — Judas "
                        "Maccabeus. The horn is a single, dramatic growth on an otherwise "
                        "ordinary sheep. Judas is not a bull (a patriarch) or a man (an "
                        "angel) but a sheep with extraordinary power — a commoner elevated "
                        "by divine empowerment. The great horn fights the ravens "
                        "(Seleucids) and cries out to the Lord of the sheep for help. "
                        "The Lord of the sheep responds: \'And the Lord of the sheep came "
                        "to them in wrath, and all who saw him fled, and they all fell "
                        "into his shadow\' (90:15). This divine intervention is the "
                        "theophanic climax — God himself enters the battlefield. But "
                        "critically, the narrative does not say the great horn achieves "
                        "final victory. Judas Maccabeus is a catalyst, not the conclusion."
            },
            {
                "heading": "The White Bull Messiah — Adamic Restoration (90:37-38)",
                "body": "After the judgment and the replacement of the old Temple with "
                        "a new one (90:28-29), the final eschatological event occurs: "
                        "\'a white bull was born, with large horns, and all the beasts "
                        "of the field and all the birds of the air feared him and made "
                        "petition to him at all times\' (90:37). The white bull "
                        "deliberately echoes Adam: \'a bull came forth from the earth, "
                        "and that bull was white\' (85:3). The messiah is thus an "
                        "eschatological Adam — a restoration of the original created "
                        "order. The \'large horns\' signal kingly authority (contrast "
                        "with Adam, who had no horns, just purity). This figure is not "
                        "merely a political deliverer but a cosmic restorer. Then the "
                        "most remarkable verse: \'I saw till all their generations were "
                        "transformed, and they all became white bulls\' (90:38). All "
                        "creatures — every nation, every species in the allegory — are "
                        "transformed into the Adamic form. This is universal restoration: "
                        "the distinctions between predator nations and prey nations are "
                        "abolished. Wolves become white bulls. Ravens become white bulls. "
                        "The zoomorphic diversity that encoded the violence of history "
                        "is resolved into the unity of the original creation."
            },
            {
                "heading": "Dating Evidence and Historical Context",
                "body": "The Maccabean dating of the Animal Apocalypse (c. 164-160 BC) "
                        "rests on several converging lines of evidence. First, the "
                        "historical allegory is transparent through the Maccabean period "
                        "but becomes vague and eschatological immediately after — the "
                        "author knows history up to Judas Maccabeus and then projects "
                        "into the future. Second, the great horn (Judas) is still "
                        "fighting when the divine intervention occurs — suggesting the "
                        "text was written during the revolt, not after its conclusion. "
                        "Third, there is no reference to the death of Judas Maccabeus "
                        "(160 BC) or to the Hasmonean dynasty that succeeded him. Fourth, "
                        "the Aramaic fragments from Qumran (4Q204) confirm pre-Christian "
                        "circulation. The dating places the Animal Apocalypse as roughly "
                        "contemporary with Daniel 7-12, and both texts respond to the "
                        "crisis of Antiochus IV Epiphanes\'s persecution of Judaism "
                        "(167-164 BC). Both use animal symbolism, both envision divine "
                        "intervention and judgment, and both promise eschatological "
                        "vindication. But where Daniel emphasizes a single transcendent "
                        "figure (the Son of Man), the Animal Apocalypse distributes "
                        "messianic functions across multiple figures and culminates in "
                        "universal transformation."
            }
        ]
    },

    # =========================================================================
    # HISTORICAL INSERT: THE ANIMAL APOCALYPSE AS ENCODED HISTORY
    # =========================================================================
    {
        "id": "insert-animal-apocalypse-key",
        "ref": "Historical Context",
        "chapter_num": None,
        "title": "The Animal Apocalypse Decoded — A Key to the Zoomorphic Allegory",
        "era": "dreams",
        "type": "historical_insert",

        "synopsis": "The Animal Apocalypse (1 Enoch 85-90) encodes the entirety "
                    "of biblical and post-biblical history through a system of "
                    "animal symbolism that is remarkably consistent and "
                    "decipherable. Understanding the key unlocks the allegory "
                    "and reveals the author's interpretation of history. The "
                    "system assigns species and colors to nations, classes of "
                    "people, and spiritual states. This insert provides the "
                    "complete interpretive guide and compares the Animal "
                    "Apocalypse's method with Daniel 7-8, which uses a similar "
                    "but more limited zoomorphic technique.",

        "key_verse": {
            "ref": "Daniel 7:3-4",
            "text": "And four great beasts came up out of the sea, different from one another. The first was like a lion and had eagles' wings.",
            "translation": "ESV"
        },
        "original_terms": [
            "nephilim",
            "egregoroi",
            "bene_elohim",
            "goy",
            "malak_yhwh",
            "mashiach",
        ],
        "ane_backdrop": None,
        "second_temple": [],

        "cross_refs": [
            {"ref": "Daniel 7:3-7", "type": "ot", "note": "Four beasts = four empires. Daniel's system is the closest canonical parallel to the Animal Apocalypse's method: animal species encode national/political identity."},
            {"ref": "Daniel 8:3-8, 20-21", "type": "ot", "note": "Ram = Media-Persia, goat = Greece — with explicit angelic interpretation. The only canonical text that provides its own key to animal symbolism."},
            {"ref": "Ezekiel 34:1-31", "type": "ot", "note": "Israel as a flock under shepherds (rulers) — the pastoral metaphor that the Animal Apocalypse adopts for all of Israel's history from Jacob onward."},
            {"ref": "Revelation 5:5-6", "type": "nt", "note": "The Lion of Judah = the Lamb who was slain. Revelation's animal symbolism continues the apocalyptic tradition that the Animal Apocalypse exemplifies."},
            {"ref": "Revelation 12-13", "type": "nt", "note": "The Dragon, the Beast from the sea, the Beast from the earth — Revelation's bestiary encodes political and spiritual powers as animals, continuing the tradition."},
            {"ref": "Matthew 25:31-33", "type": "nt", "note": "Separating sheep from goats at the eschatological judgment — animal symbolism in Jesus' teaching, possibly influenced by the Animal Apocalypse's sheep = righteous tradition."},
            {"ref": "Genesis 10:1-32", "type": "ot", "note": "The Table of Nations (70 nations) — the canonical basis for the 70 shepherds appointed over the nations in 1 Enoch 89:59."},
            {"ref": "Deuteronomy 32:8 (LXX/4QDeut-j)", "type": "ot", "note": "God fixed the nations' borders according to the number of the sons of God — the divine council theology behind the 70 shepherds."}
        ],

        "divine_council_note": "The Animal Apocalypse's symbolic system reflects a "
                               "thoroughgoing divine council theology. The two-tier "
                               "species division (animals = humans, men = angels) "
                               "maps directly onto the council structure: there is "
                               "a heavenly tier (the white men / the Lord of the "
                               "sheep) and an earthly tier (the cattle, sheep, beasts, "
                               "and birds). The 70 shepherds are council delegates "
                               "governing national affairs. The scribal angel recording "
                               "their actions is the court secretary maintaining "
                               "judicial records. The books opened at judgment are "
                               "the council's official proceedings.",

        "sections": [
            {
                "heading": "The Core Species Key",
                "body": "<b>WHITE BULLS</b> = the righteous patriarchal line "
                        "(Adam, Seth, Noah, Abraham, Isaac). White indicates "
                        "purity, righteousness, divine favor. Bulls represent "
                        "humans in the pre-Israelite period.<br><br>"
                        "<b>BLACK BULLS / CATTLE</b> = the line of Cain and Ham. "
                        "Black indicates sin, violence, or separation from the "
                        "righteous line.<br><br>"
                        "<b>RED CATTLE</b> = Abel (martyrdom/blood) and Japheth.<br><br>"
                        "<b>SHEEP (WHITE)</b> = Israel from Jacob onward. The "
                        "transition from bull to sheep at Jacob marks Israel's "
                        "emergence as a distinct covenantal people, a flock under "
                        "God as shepherd.<br><br>"
                        "<b>RAMS</b> = Israel's leaders (judges, kings, notable "
                        "figures like Moses, Samuel, David, Solomon).<br><br>"
                        "<b>LAMBS</b> = young reformers, specifically the Hasidim "
                        "and Maccabean movement in the late period.<br><br>"
                        "<b>MEN (WHITE)</b> = angels, divine beings. The four "
                        "white men are the archangels (Michael, Gabriel, Raphael, "
                        "Uriel). The Lord of the sheep is God himself.<br><br>"
                        "<b>STARS</b> = angels in their heavenly state. Fallen "
                        "stars = the Watchers who descended to earth."
            },
            {
                "heading": "The Gentile Nations Key",
                "body": "<b>WOLVES</b> = Egyptians. The primary predators of the "
                        "flock during the Exodus period.<br><br>"
                        "<b>DOGS</b> = Philistines. Persistent enemies during the "
                        "Judges and early monarchic period.<br><br>"
                        "<b>WILD BOARS / SWINE</b> = Edomites / Esau's "
                        "descendants. Esau himself is a boar.<br><br>"
                        "<b>FOXES</b> = Ammonites. Cunning, smaller-scale "
                        "enemies in the Judges period.<br><br>"
                        "<b>LIONS</b> = Babylonians. The great predator that "
                        "destroys the Temple and scatters the flock (cf. Daniel "
                        "7:4, Babylon as a lion).<br><br>"
                        "<b>LEOPARDS</b> = Assyrians. Associated with the "
                        "destruction of the northern kingdom.<br><br>"
                        "<b>EAGLES / VULTURES</b> = various imperial powers "
                        "(interpretations vary: Rome, Ptolemaic Egypt).<br><br>"
                        "<b>RAVENS</b> = Seleucid Greeks (Antiochus Epiphanes "
                        "and his forces). The ravens and kites attack the sheep "
                        "in the period immediately preceding divine intervention "
                        "— the Maccabean crisis.<br><br>"
                        "<b>KITES / HAWKS</b> = allied forces of the Seleucid "
                        "empire.<br><br>"
                        "<b>ELEPHANTS, CAMELS, ASSES</b> = Nephilim. Hybrid "
                        "monstrosities born from the Watcher-human unions, "
                        "representing creatures that belong to no natural "
                        "category."
            },
            {
                "heading": "The Animal Apocalypse and Daniel Compared",
                "body": "The Animal Apocalypse and Daniel 7-8 are roughly "
                        "contemporary compositions (both datable to the Maccabean "
                        "crisis, c. 167-164 BC) that use animal symbolism to "
                        "encode history, and both climax with divine judgment and "
                        "the establishment of God's kingdom. Yet they differ "
                        "significantly in scope and method. Daniel's beasts "
                        "represent empires in sequence (Babylon, Media, Persia, "
                        "Greece), while the Animal Apocalypse assigns species to "
                        "individual nations and traces ALL of history from Adam "
                        "to the eschaton. Daniel's vision focuses on the period "
                        "of gentile dominion; the Animal Apocalypse encompasses "
                        "the entire biblical narrative. Daniel introduces the "
                        "'one like a son of man' who receives dominion; the "
                        "Animal Apocalypse introduces the white bull with great "
                        "horns who restores the Adamic condition. Both figures "
                        "are messianic, but Daniel's is more clearly supernatural "
                        "(coming with the clouds of heaven), while the Animal "
                        "Apocalypse's is more clearly connected to the Davidic "
                        "line (a bull, i.e., a human, with royal authority). "
                        "Together, the two texts represent the full flowering "
                        "of Jewish apocalyptic animal symbolism, a tradition "
                        "that would profoundly influence Revelation's imagery "
                        "of the Lamb, the Beast, and the Dragon."
            }
        ]
    }
]
