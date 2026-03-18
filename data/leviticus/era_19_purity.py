"""
era_19_purity.py — Purity and Impurity Laws (Leviticus 11-15)

The purity system is not about hygiene — it is about the taxonomy of life and death.
Clean (tahor, 'pure/ritually fit') and unclean (tamei, 'ritually impure/contaminated')
form a symbolic map of the cosmos: what is whole, ordered, and life-giving belongs in
God's realm; what is associated with decay, death, and boundary-crossing is incompatible
with the holy (qodesh). These are not moral judgments but cosmic categories separating
the realm of life (God's domain) from the realm of death (the domain of chaos and the
powers opposed to God).
"""

CHAPTERS = [
    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 11 — CLEAN AND UNCLEAN ANIMALS
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-11",
        "ref": "Leviticus 11",
        "chapter_num": 11,
        "title": "Clean and Unclean Animals — The Dietary Laws",
        "era": "purity",
        "type": "chapter",
        "themes": ["HOLY", "LAW"],

        "synopsis": (
            "Leviticus 11 presents the foundational dietary laws (kashrut) that will define "
            "Israel's eating practices for millennia. The system classifies animals into clean "
            "(tahor — permitted for eating) and unclean (tamei — forbidden). For land animals: "
            "split hoof AND chews the cud (ruminants) are clean; animals with only one trait "
            "(camel, rock badger, hare, pig) are specifically named as unclean. For water "
            "creatures: fins AND scales are clean; everything else (shellfish, eels, catfish) "
            "is 'detestable' (sheqets). For birds: a list of forbidden species (mostly "
            "raptors, scavengers, and carrion-eaters) is given rather than a positive rule. "
            "For insects: most are unclean, but locusts, crickets, and grasshoppers (with "
            "jointed legs for hopping) are permitted. Swarming things (sherets) on the ground "
            "are categorically unclean. Contact with carcasses of unclean animals transmits "
            "impurity until evening. The chapter concludes with the theological rationale: "
            "'For I am the LORD your God. Consecrate yourselves therefore, and be holy, for "
            "I am holy... I am the LORD who brought you up out of the land of Egypt to be "
            "your God. You shall therefore be holy, for I am holy' (11:44-45). The dietary "
            "laws are NOT primarily about health — they are about holiness. They create a "
            "daily, embodied practice of discernment: every meal requires Israel to distinguish "
            "between permitted and forbidden, training the covenant community to make "
            "distinctions in every area of life. The specific criteria likely reflect symbolic "
            "categories: clean animals are those that perfectly fit their domain (land animals "
            "that walk properly on split hooves AND process food properly by chewing cud; "
            "water creatures that swim properly with fins and scales). Animals that blur "
            "categories or cross boundaries are unclean — a principle that resonates with "
            "the broader Levitical concern for order, wholeness, and boundary integrity."
        ),

        "key_verse": {
            "ref": "Leviticus 11:44-45",
            "text": "For I am the LORD your God. Consecrate yourselves therefore, and be holy, for I am holy. You shall not defile yourselves with any swarming thing that crawls on the ground. For I am the LORD who brought you up out of the land of Egypt to be your God. You shall therefore be holy, for I am holy.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tahor", "tamei", "sheqets", "parsah", "gerah",
            "sherets", "qadosh", "nefesh", "tame", "maqor"
            # Key glosses: tahor = 'clean/pure' (ritually fit to approach God);
            # tamei = 'unclean/impure' (ritually unfit — not sinful, but
            # incompatible with the sacred); sheqets = 'detestable/abomination'
            # (stronger than tamei — objects of revulsion); parsah = 'hoof'
            # (split hoof = one criterion for clean land animals); gerah =
            # 'cud' (chewing cud = the other criterion); sherets = 'swarming
            # thing' (small creatures that teem); qadosh = 'holy/set apart'
        ],

        "ane_backdrop": (
            "Dietary restrictions are attested in several ANE cultures, though none approach "
            "the systematization of Leviticus 11. Egyptian priests had extensive dietary "
            "prohibitions: Herodotus reports they avoided beans, pork, and certain fish. "
            "Mesopotamian omen texts associate certain animals with favorable or unfavorable "
            "portents, creating de facto avoidance of some species. The pig prohibition has "
            "deep roots: while pigs were sacrificed in Mesopotamian and Hittite contexts, "
            "they were associated with disease and impurity in multiple cultures. The uniquely "
            "Israelite contribution is the systematic classification based on observable "
            "physical criteria (hoof, cud, fins, scales) rather than mythological association "
            "or priestly preference. Mary Douglas's influential analysis ('Purity and Danger,' "
            "1966) argues that the dietary laws classify animals by their conformity to the "
            "ideal type of their domain — animals that 'fit' their category are clean; those "
            "that blur boundaries are not."
        ),

        "second_temple": [
            {
                "source": "Letter of Aristeas 142-169",
                "summary": "This Hellenistic Jewish text allegorizes the dietary laws: "
                           "ruminants represent meditation on God's law; split hooves "
                           "represent discernment between good and evil.",
                "relevance": "Shows how Hellenistic Judaism reinterpreted the dietary laws "
                             "philosophically while still observing them literally — the "
                             "allegorical and literal coexisted."
            },
            {
                "source": "1 Maccabees 1:47-48, 62-63",
                "summary": "Antiochus IV forces Jews to sacrifice pigs and eat unclean "
                           "food. Many 'chose to die rather than to be defiled by food' — "
                           "the dietary laws become a martyrdom issue.",
                "relevance": "Demonstrates that by the 2nd century BC, the dietary laws "
                             "were central to Jewish identity — worth dying for."
            },
            {
                "source": "11QTemple (Temple Scroll) 48:1-7",
                "summary": "The Temple Scroll provides expanded purity regulations for "
                           "animals, including additional restrictions beyond Leviticus 11.",
                "relevance": "Shows that Qumran intensified the purity laws — the "
                             "community saw itself as even more stringent than the "
                             "Torah required."
            }
        ],

        "cross_refs": [
            {"ref": "Mark 7:14-23", "note": "Jesus declares all foods clean — 'it is not what goes into a person that defiles, but what comes out' — internalizing the purity principle", "type": "nt"},
            {"ref": "Acts 10:9-16", "note": "Peter's vision of the sheet with unclean animals — 'What God has made clean, do not call common' — the dietary laws as a symbol of Gentile inclusion", "type": "nt"},
            {"ref": "Romans 14:14", "note": "Paul: 'Nothing is unclean in itself' — the new covenant transformation of Levitical categories", "type": "nt"},
            {"ref": "Deuteronomy 14:3-21", "note": "The parallel dietary code in Deuteronomy — largely identical to Leviticus 11 but in a different literary context", "type": "ot"},
            {"ref": "Genesis 7:2-3", "note": "Clean/unclean animal distinction exists before Sinai — Noah takes seven pairs of clean and two of unclean", "type": "ot"},
            {"ref": "Daniel 1:8", "note": "Daniel resolves 'not to defile himself with the king's food' — dietary obedience as resistance to empire", "type": "ot"},
            {"ref": "Isaiah 66:17", "note": "Judgment on those who eat 'pig's flesh and the abomination and mice' — the dietary laws in prophetic eschatology", "type": "ot"},
            {"ref": "Hebrews 9:9-10", "note": "The old covenant's 'regulations for the body — food and drink and various washings' were 'imposed until the time of reformation' — the dietary laws as temporary pedagogy pointing to Christ", "type": "nt"},
            {"ref": "1 Peter 1:15-16", "note": "'As he who called you is holy, be holy in all your conduct' — quoting the Lev 11:44-45 command, now applied to moral rather than dietary holiness", "type": "nt"},
            {"ref": "Colossians 2:16-17", "note": "'Let no one pass judgment on you in questions of food and drink... these are a shadow of the things to come, but the substance belongs to Christ'", "type": "nt"}
        ],

        "divine_council_note": (
            "The dietary laws create a visible marker distinguishing Israel from the "
            "nations. In the Deuteronomy 32:8-9 framework, the nations were allotted to "
            "lesser elohim (the bene elohim, 'sons of God' — divine council members) "
            "who corrupted them; Israel was kept for YHWH as his nachalah ('inheritance/ "
            "personal portion'). The dietary laws are a daily, embodied enactment of "
            "this distinction: Israel does not eat as the nations eat because Israel "
            "does not belong to the gods of the nations. Every meal is an act of "
            "covenant allegiance — a thrice-daily declaration of 'YHWH is my God, not "
            "the elohim of the nations.' The Holiness Code will make this explicit: "
            "'You shall not walk in the customs of the nation that I am driving out "
            "before you' (Lev 20:23). The clean/unclean animal distinction also maps "
            "onto the cosmic life/death boundary: clean animals are associated with "
            "the ordered, life-giving domain (God's realm); unclean animals are "
            "associated with death, predation, and boundary-crossing (the chaotic "
            "realm opposed to God's order). The dietary laws are the most basic, "
            "most frequent practice of covenantal separation — and of choosing life "
            "over death (Deut 30:19)."
        ),

        "sections": [
            {
                "title": "Land Animals (11:1-8)",
                "content": (
                    "The criteria for clean land animals are twofold: the animal must have a "
                    "completely split hoof (parsah shosa'at) AND chew the cud (ma'alat gerah). "
                    "Both conditions must be met. Four animals that meet only one criterion "
                    "are named: the camel (chews cud but does not split the hoof), the rock "
                    "badger/hyrax (chews cud but no split hoof), the hare (same), and the "
                    "pig (splits the hoof but does not chew cud). The pig is singled out as "
                    "particularly deceptive — it 'shows' the right external feature (split "
                    "hoof) but lacks the internal one (cud-chewing). Later Jewish tradition "
                    "made the pig a symbol of hypocrisy: clean on the outside, unclean within. "
                    "The criteria effectively limit clean animals to domesticated ruminants: "
                    "cattle, sheep, goats, and wild equivalents like deer and gazelle."
                )
            },
            {
                "title": "Water Creatures (11:9-12)",
                "content": (
                    "Everything in water that has fins AND scales is clean. Everything else — "
                    "shellfish, crustaceans, eels, catfish, rays — is sheqets ('detestable'). "
                    "The language is emphatic: 'they are detestable to you... you shall "
                    "detest their carcasses.' Fins and scales are the markers of proper "
                    "aquatic locomotion — creatures that swim 'properly' in their domain. "
                    "Bottom-dwellers, filter-feeders, and creatures that lack the defining "
                    "features of their habitat are excluded. This aligns with Mary Douglas's "
                    "taxonomic interpretation: clean animals perfectly fit the ideal type of "
                    "their domain. The practical effect excludes all shellfish — a significant "
                    "dietary limitation in the ancient Near East where coastal communities "
                    "relied heavily on shellfish."
                )
            },
            {
                "title": "Birds and Flying Insects (11:13-23)",
                "content": (
                    "Rather than positive criteria, a list of forbidden birds is given: "
                    "eagle, bearded vulture, black vulture, kite, falcon, ravens, ostrich, "
                    "nighthawk, sea gull, hawk, little owl, cormorant, short-eared owl, "
                    "barn owl, tawny owl, carrion vulture, stork, heron, hoopoe, and bat. "
                    "The common thread: these are predators, scavengers, and carrion-eaters — "
                    "birds associated with death. Clean birds (by implication) are seed-eaters "
                    "and domesticated poultry. Among flying insects, those with jointed legs "
                    "for hopping are clean: locusts, crickets, grasshoppers. All other "
                    "winged insects with four feet (swarming insects) are detestable. The "
                    "locust exception is practically important — locusts were a significant "
                    "protein source in the ANE and the wilderness (cf. John the Baptist, "
                    "Matt 3:4)."
                )
            },
            {
                "title": "Carcass Contamination (11:24-40)",
                "content": (
                    "Contact with the carcass of an unclean animal transmits impurity until "
                    "evening. Whoever carries a carcass must wash their clothes and is unclean "
                    "until evening. Animals that walk on paws (cats, dogs, bears) are unclean. "
                    "Among swarming things, specific creatures are named: weasel, mouse, "
                    "great lizard, gecko, monitor lizard, sand lizard, chameleon. If any of "
                    "these die and fall on an object — earthenware vessel, oven, stove, "
                    "water cistern — the object becomes unclean. Earthenware must be broken "
                    "(it absorbs impurity); a spring or cistern remains clean (running water "
                    "purifies). Seed grain remains clean unless water has been put on it. "
                    "If a clean animal dies naturally, whoever touches or eats the carcass "
                    "becomes unclean until evening. The detailed regulations reveal a "
                    "comprehensive system managing the inevitable contacts between Israel "
                    "and impurity in daily life."
                )
            },
            {
                "title": "The Theological Rationale (11:41-47)",
                "content": (
                    "The chapter climaxes with the foundational command: 'Be holy, for I am "
                    "holy' (qedoshim tihyu ki qadosh ani). This phrase — repeated in 19:2 "
                    "and echoed in 1 Peter 1:16 — is the hermeneutical key to the entire "
                    "purity system. The dietary laws are not arbitrary taboos or health codes "
                    "but training in holiness — the daily, embodied practice of discernment "
                    "between what is fitting and what is not. The concluding verse states the "
                    "purpose explicitly: 'to make a distinction between the unclean and the "
                    "clean, and between the living creature that may be eaten and the living "
                    "creature that may not be eaten' (11:47). Learning to discern at the "
                    "table trains Israel to discern in every domain: worship, relationships, "
                    "ethics, and covenant faithfulness."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 12 — PURIFICATION AFTER CHILDBIRTH
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-12",
        "ref": "Leviticus 12",
        "chapter_num": 12,
        "title": "Childbirth and Purification — The Mystery of Blood and Life",
        "era": "purity",
        "type": "chapter",
        "themes": ["HOLY", "BLOOD", "PRIEST"],

        "synopsis": (
            "Leviticus 12 is one of the shortest chapters in Leviticus but raises some of "
            "the most profound theological questions. After giving birth to a son, a woman "
            "is ceremonially impure for seven days (as during menstruation), then remains "
            "in a state of 'blood purification' (demei toharah) for thirty-three additional "
            "days — a total of forty days. For a daughter, the periods are doubled: fourteen "
            "days of impurity and sixty-six days of blood purification — a total of eighty "
            "days. During the purification period, the woman must not touch any holy thing "
            "or enter the sanctuary. At the end, she brings a yearling lamb for a burnt "
            "offering and a pigeon or turtledove for a sin offering; if she cannot afford a "
            "lamb, two turtledoves or pigeons suffice. The priest makes atonement, and she "
            "is clean. The impurity is NOT because childbirth is sinful — it is because it "
            "involves blood, and blood belongs to God (17:11). The discharge of blood associated "
            "with birth creates a state of ritual impurity because the life-substance has "
            "left the body. The distinction between male and female birth periods is debated. "
            "Some scholars link it to the eight-day circumcision of boys (which begins the "
            "purification process), while others connect it to ancient physiology that "
            "believed female births involved more blood loss. Milgrom argues that the "
            "doubling reflects a purely formal symmetry in the priestly system. The bird "
            "offering for the poor is what Mary brings in Luke 2:24, marking the holy "
            "family's humble economic status."
        ),

        "key_verse": {
            "ref": "Leviticus 12:7-8",
            "text": "And he shall offer it before the LORD and make atonement for her. Then she shall be clean from the flow of her blood. This is the law for her who bears a child, either male or female. And if she cannot afford a lamb, then she shall take two turtledoves or two young pigeons, one for a burnt offering and the other for a sin offering. And the priest shall make atonement for her, and she shall be clean.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "yoledet", "niddah", "demei_toharah", "milah",
            "chattat", "olah", "kaphar", "tahor", "tamei"
            # Key glosses: yoledet = 'woman who gives birth'; niddah =
            # 'menstrual impurity/separation'; demei toharah = 'blood of
            # purification' (the liminal period between impurity and full
            # cleanness); milah = 'circumcision' (on the eighth day);
            # kaphar = 'to atone/purge'
        ],

        "ane_backdrop": (
            "Postpartum purification periods are widespread in the ANE and across cultures "
            "globally. Egyptian medical papyri (Ebers Papyrus, ~1550 BC) prescribe fourteen-day "
            "seclusion periods after childbirth. Mesopotamian texts describe postpartum "
            "impurity periods during which the woman is restricted from temple access. Hittite "
            "laws prescribe purification rituals for women after birth. Greek culture "
            "recognized a period of 'pollution' (miasma) associated with birth (and death). "
            "The widespread nature of postpartum purification across unrelated cultures "
            "suggests a deep-rooted human intuition that the transition of bringing new life "
            "into the world — involving blood, vulnerability, and liminal states — requires "
            "ritual management. Leviticus is distinctive in providing a clear timeframe and a "
            "sacrificial mechanism for restoration."
        ),

        "second_temple": [
            {
                "source": "Luke 2:22-24",
                "summary": "Mary and Joseph bring Jesus to the temple for the purification "
                           "prescribed in Leviticus 12, offering 'a pair of turtledoves or "
                           "two young pigeons' — the offering of the poor.",
                "relevance": "The most direct NT application of Leviticus 12 — Jesus' family "
                             "observes the Torah faithfully, and their poverty-level offering "
                             "connects the Messiah to the poorest in Israel."
            },
            {
                "source": "Mishnah Niddah 3-4",
                "summary": "Extensive rabbinic discussion of the postpartum impurity periods, "
                           "including cases of miscarriage, multiple births, and uncertain "
                           "timing.",
                "relevance": "Shows the practical halakhic elaboration of Leviticus 12 in "
                             "Second Temple and rabbinic practice — the brief chapter generated "
                             "extensive legal discussion."
            }
        ],

        "cross_refs": [
            {"ref": "Luke 2:22-24", "note": "Mary's purification offering — two birds, the provision for the poor", "type": "nt"},
            {"ref": "Genesis 17:12", "note": "Circumcision on the eighth day — the male birth period aligns with the circumcision timeline", "type": "ot"},
            {"ref": "Psalm 51:5", "note": "'In sin did my mother conceive me' — sometimes (mis)applied to Leviticus 12 but actually about universal sinfulness, not birth impurity", "type": "ot"},
            {"ref": "Galatians 4:4", "note": "Christ 'born of woman, born under the law' — Jesus enters the world subject to the Levitical purity system", "type": "nt"},
            {"ref": "John 3:6", "note": "'That which is born of the flesh is flesh' — the flesh/spirit distinction echoes the clean/unclean boundary", "type": "nt"},
            {"ref": "Hebrews 10:22", "note": "'Let us draw near with a true heart in full assurance of faith, with our hearts sprinkled clean from an evil conscience and our bodies washed with pure water' — the Lev 12 purification washing and sprinkling language applied to new covenant believers who now have permanent access to God's presence", "type": "nt"}
        ],

        "divine_council_note": (
            "The purification after childbirth connects to the broader theme of blood "
            "as the sacred life-substance. In the divine council framework, life (nephesh) "
            "belongs to YHWH — he breathed it into humanity at creation (Gen 2:7). Blood, "
            "as the carrier of nephesh (Lev 17:11), is sacred and must be returned to God "
            "through the altar. The postpartum blood discharge represents nephesh-substance "
            "leaving the body outside the altar system — hence the impurity. The purification "
            "offering restores the proper order: the blood of the sacrifice on the altar "
            "'covers' the blood that was shed outside the sacred framework."
        ),

        "sections": [
            {
                "title": "The Male Birth Period (12:1-4)",
                "content": (
                    "After bearing a son, the woman is tamei (unclean) for seven days — "
                    "'as at the time of her menstruation' (ke-yemei niddat devotah). On the "
                    "eighth day, the son is circumcised. Then for thirty-three more days she "
                    "remains in the 'blood of purification' (demei toharah) — a liminal state "
                    "between impurity and full cleanness. During this period she may not touch "
                    "any holy thing or enter the sanctuary, but she is not fully tamei. The "
                    "seven-day initial period plus circumcision on day eight mirrors the "
                    "seven-day creation plus the eighth-day inauguration pattern. The forty-day "
                    "total resonates with other biblical forties: the flood (40 days), Moses on "
                    "Sinai (40 days), the wilderness (40 years), Jesus in the desert (40 days)."
                )
            },
            {
                "title": "The Female Birth Period (12:5)",
                "content": (
                    "For a daughter, the impurity period is doubled: fourteen days of initial "
                    "impurity and sixty-six days of blood purification — eighty days total. "
                    "The reason for the doubling is debated and no scholarly consensus exists. "
                    "Options include: (1) The absence of circumcision — the male birth has "
                    "circumcision as a purificatory milestone that the female birth lacks. "
                    "(2) Ancient medical belief that female births involved greater blood loss. "
                    "(3) Formal symmetry in the priestly numerical system. (4) The daughter "
                    "carries future reproductive potential, doubling the blood-association. "
                    "What is clear: the text does NOT assign negative value to daughters — the "
                    "same sacrifice cleanses both, and the woman's status is fully restored "
                    "in both cases."
                )
            },
            {
                "title": "The Purification Offerings (12:6-8)",
                "content": (
                    "At the completion of the purification period (whether 40 or 80 days), "
                    "the woman brings two offerings: a yearling lamb for a burnt offering "
                    "(olah — consecration) and a pigeon or turtledove for a sin offering "
                    "(chattat — purification). If she cannot afford a lamb, two birds suffice — "
                    "one for each offering. The priest makes atonement (kaphar) for her, "
                    "and she is declared clean (tahor). The chattat here is not for moral "
                    "sin but for ritual impurity — childbirth is not sinful, but the blood "
                    "discharge creates a state incompatible with approaching the sanctuary. "
                    "The sacrifice restores access. Mary's offering of birds in Luke 2:24 "
                    "places the incarnation among the poor of Israel — the Messiah enters "
                    "through the lowest economic tier of the Levitical system."
                )
            },
            {
                "title": "Blood, Life, and the Sacred Boundary",
                "content": (
                    "The unifying principle of Leviticus 12 is blood as the substance of "
                    "life. Every blood discharge — menstruation, postpartum, injury — creates "
                    "impurity because nephesh (life-force) is leaving the body outside the "
                    "controlled, sacred context of the altar. The altar is the only place "
                    "where blood-shedding is sanctioned and sanctified. When blood leaves "
                    "the body in any other context, it represents a rupture in the life-order "
                    "that must be ritually addressed. This is not primitive superstition "
                    "but a coherent theological anthropology: life belongs to God, blood "
                    "carries life, and the uncontrolled loss of blood represents a temporary "
                    "disruption in the God-human relationship that sacrifice repairs."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 13 — SKIN DISEASES: DIAGNOSIS
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-13",
        "ref": "Leviticus 13",
        "chapter_num": 13,
        "title": "Tsara'at — The Priest as Diagnostic Authority",
        "era": "purity",
        "type": "chapter",
        "themes": ["HOLY", "PRIEST", "LAW"],

        "synopsis": (
            "Leviticus 13 is the longest chapter in Leviticus (59 verses), providing "
            "exhaustive diagnostic criteria for tsara'at — a term traditionally translated "
            "'leprosy' but almost certainly NOT Hansen's disease (Mycobacterium leprae). "
            "The Hebrew tsara'at refers to a range of skin conditions (and even afflictions "
            "of garments and houses, as chapter 14 will address) characterized by surface "
            "discoloration, scaling, and hair changes. The priest functions as the diagnostic "
            "authority — not a doctor treating disease but a ritual expert determining "
            "purity status. The affected person is brought to the priest, who examines the "
            "skin condition and makes one of three determinations: clean (tahor), unclean "
            "(tamei), or quarantined for seven days of observation (with potential re-examination "
            "and a second seven-day period). The diagnostic criteria are remarkably precise: "
            "depth of the affliction relative to surrounding skin, hair color changes (white "
            "hair in the affected area is a sign of deep infection), spreading versus stable "
            "conditions, raw flesh, and the presence of white discoloration. A person "
            "diagnosed as tamei must live outside the camp, wear torn clothes, let their hair "
            "hang loose, cover their upper lip, and cry 'Unclean, unclean!' (tamei, tamei) "
            "when anyone approaches. This is devastating social isolation. The chapter also "
            "covers tsara'at in garments — woolens, linens, and leather can develop a "
            "'greenish or reddish disease' that must be examined, quarantined, washed, and "
            "potentially burned. The theological significance is profound: tsara'at represents "
            "death encroaching on the living — the skin, the body's boundary, is breaking "
            "down. The afflicted person is treated as a walking death — expelled from the "
            "community of the living, mourning as if for themselves."
        ),

        "key_verse": {
            "ref": "Leviticus 13:45-46",
            "text": "The leprous person who has the disease shall wear torn clothes and let the hair of his head hang loose, and he shall cover his upper lip and cry out, 'Unclean, unclean.' He shall remain unclean as long as he has the disease. He is unclean. He shall live alone. His dwelling shall be outside the camp.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tsaraat", "nega", "baheret", "se'et", "sapachat",
            "kohen", "hesger", "tamei", "tahor", "michyah"
            # Key glosses: tsara'at = 'skin disease/affliction' (NOT Hansen's
            # disease/leprosy — a range of surface conditions indicating death
            # encroaching on the living); nega = 'affliction/mark/plague spot';
            # baheret = 'bright/white spot'; se'et = 'swelling/elevation';
            # sapachat = 'scab/rash'; kohen = 'priest' (serves as diagnostic
            # authority, not doctor — classifies purity status); hesger =
            # 'quarantine/isolation' (7-day observation period);
            # michyah = 'raw/living flesh' (exposed tissue in a lesion)
        ],

        "ane_backdrop": (
            "Skin diseases generated significant anxiety in the ANE. Mesopotamian diagnostic "
            "texts (particularly the Sakikku series, 'Treatise on Medical Diagnosis and "
            "Prognosis') describe various skin conditions with prognoses ranging from "
            "'he will recover' to 'the hand of a ghost.' The Mesopotamian texts treat skin "
            "disease as potentially caused by divine anger or demonic attack. Egyptian medical "
            "papyri (Ebers Papyrus) describe treatments for skin conditions including salves "
            "and incantations. The distinctly Levitical approach treats tsara'at not as a "
            "medical condition requiring treatment but as a ritual condition requiring "
            "priestly diagnosis. The priest does not heal — he classifies. Healing comes "
            "from God alone (cf. Num 12:13, 2 Kings 5:7). The isolation of the afflicted "
            "person has parallels in Hittite texts where individuals affected by plague are "
            "removed from the community to prevent the spread of impurity."
        ),

        "second_temple": [
            {
                "source": "4Q266 (Damascus Document) 9:1-10",
                "summary": "The Qumran community's halakhah on tsara'at diagnosis, "
                           "following Leviticus 13 but with expanded requirements for "
                           "the examining priest's expertise.",
                "relevance": "Shows that tsara'at regulations were actively applied at "
                             "Qumran — not merely theoretical but operational purity law."
            },
            {
                "source": "Mishnah Negaim 1-14",
                "summary": "The most extensive rabbinic treatment of tsara'at: 14 chapters "
                           "detailing every possible diagnostic scenario, measurement, and "
                           "priestly procedure.",
                "relevance": "Preserves the oral tradition of how the Leviticus 13-14 "
                             "regulations were interpreted and (theoretically) applied "
                             "after the destruction of the temple."
            },
            {
                "source": "2 Kings 5:1-14 (Naaman)",
                "summary": "The Aramean general Naaman is healed of tsara'at by washing "
                           "in the Jordan at Elisha's command — healing belongs to YHWH.",
                "relevance": "Illustrates that tsara'at was understood as a condition "
                             "only God could heal, not doctors or priests."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 8:1-4", "note": "Jesus touches a leper and heals him, then commands 'go show yourself to the priest and offer the gift Moses commanded' — Leviticus 13-14 procedure", "type": "nt"},
            {"ref": "Luke 17:11-19", "note": "Jesus heals ten lepers and sends them to the priests — the Levitical diagnostic system still operative in the 1st century", "type": "nt"},
            {"ref": "Numbers 12:10-15", "note": "Miriam is struck with tsara'at for challenging Moses — tsara'at as divine judgment", "type": "ot"},
            {"ref": "2 Kings 5:27", "note": "Gehazi receives Naaman's tsara'at as judgment for greed — the affliction transmitted as punishment", "type": "ot"},
            {"ref": "2 Chronicles 26:19-21", "note": "King Uzziah is struck with tsara'at for burning incense in the temple — unauthorized priestly function", "type": "ot"},
            {"ref": "Mark 1:40-45", "note": "Jesus is 'moved with compassion' toward the leper — divine mercy toward what the purity system excludes", "type": "nt"},
            {"ref": "Hebrews 4:15", "note": "Christ is 'one who in every respect has been tempted as we are, yet without sin' — where the Levitical priest could only diagnose and classify impurity, Christ enters human brokenness while remaining uncontaminated, reversing the purity flow", "type": "nt"},
            {"ref": "Hebrews 7:26", "note": "Christ is 'holy, innocent, unstained, separated from sinners' — the high priest who needs no quarantine or examination because he is inherently tahor (pure)", "type": "nt"}
        ],

        "divine_council_note": (
            "Tsara'at is associated with divine judgment in several biblical narratives: "
            "Miriam for rebellion, Gehazi for greed, Uzziah for usurping priestly authority. "
            "In the divine council framework, the affliction represents the withdrawal of "
            "divine life-force from the body — death encroaching on the living. The person "
            "becomes a visible symbol of the separation from God that sin produces. The "
            "exclusion 'outside the camp' mirrors the expulsion from Eden: separated from "
            "the community of the living, separated from the sanctuary, crying 'unclean' "
            "as a warning. Jesus' healings of lepers reverse this — he restores what the "
            "cosmic rupture of sin had taken away."
        ),

        "sections": [
            {
                "title": "Initial Examination Criteria (13:1-8)",
                "content": (
                    "When a person develops a skin condition — a swelling (se'et), a scab "
                    "(sapachat), or a bright spot (baheret) — they are brought to Aaron or "
                    "one of his sons. The priest examines the nega ('affliction/mark'). Key "
                    "indicators of tsara'at: the affliction appears deeper than the surrounding "
                    "skin, and the hair in the affected area has turned white. If both are "
                    "present, the diagnosis is tamei. If the condition is ambiguous — no deeper "
                    "than skin surface, no white hair — the person is quarantined (hesger) for "
                    "seven days and re-examined. If it has not spread, another seven days. If "
                    "after fourteen days it has faded and not spread, the person is declared "
                    "clean and washes their clothes. The careful, patient diagnostic procedure "
                    "protects against hasty judgment — no one is declared unclean without "
                    "thorough examination."
                )
            },
            {
                "title": "Chronic and Spreading Conditions (13:9-28)",
                "content": (
                    "Multiple scenarios are addressed: chronic tsara'at with white swelling "
                    "and raw flesh is immediately tamei — no quarantine needed. Paradoxically, "
                    "if tsara'at covers the ENTIRE body from head to foot with white, the "
                    "person is declared CLEAN (13:12-13). This seems counterintuitive but "
                    "follows the system's logic: the condition has stabilized, the whole skin "
                    "is uniform, and the process is complete. Active spreading is the danger "
                    "sign, not extent. Burns that develop suspicious white or reddish-white "
                    "spots require the same examination protocol. Scalp and beard conditions "
                    "follow parallel procedures. The meticulous detail — dozens of specific "
                    "diagnostic scenarios — reflects the gravity of the diagnosis: declaring "
                    "someone tamei means social death, so the priest must be exhaustively "
                    "thorough."
                )
            },
            {
                "title": "Hair and Scalp Conditions (13:29-44)",
                "content": (
                    "Conditions on the head or beard require additional criteria: yellow thin "
                    "hair (not white, but yellow), depth below the skin, and spreading are "
                    "the indicators. Baldness (gareach for back-of-head, gibeach for forehead) "
                    "by itself is explicitly NOT tsara'at — the text protects bald men from "
                    "false diagnosis. Only if reddish-white afflictions appear on the bald "
                    "area does the tsara'at diagnosis apply. The specificity of these "
                    "provisions shows pastoral concern: the system is designed to be as "
                    "narrow as possible in declaring impurity, protecting individuals from "
                    "unnecessary exclusion."
                )
            },
            {
                "title": "The Social Death of the Metsora (13:45-46)",
                "content": (
                    "The diagnosed individual (metsora) must adopt the outward signs of "
                    "mourning: torn clothes, loose/disheveled hair, covered upper lip. They "
                    "must cry tamei, tamei ('unclean, unclean') to warn others of their "
                    "status. They must live alone, outside the camp. These are the rituals "
                    "of death mourning applied to a living person — the metsora is socially "
                    "dead, symbolically deceased. The covered lip prevents breath (the ruach, "
                    "life-breath) from contaminating others. The exclusion from the camp "
                    "mirrors the exclusion from Eden. This is the most severe form of "
                    "impurity in the Levitical system — long-term, visible, isolating."
                )
            },
            {
                "title": "Tsara'at in Garments (13:47-59)",
                "content": (
                    "Remarkably, tsara'at can affect not just skin but garments — woolens, "
                    "linens, or leather. A 'greenish or reddish' discoloration (possibly "
                    "mold or fungal growth) is examined by the priest, quarantined for seven "
                    "days, and re-examined. If it has spread, the garment is burned — it is "
                    "'a persistent tsara'at' (tsara'at mam'eret). If it has not spread, it "
                    "is washed and re-quarantined. If the mark has faded, the affected area "
                    "is torn out; if it reappears, the whole garment is burned. The extension "
                    "of tsara'at to inanimate objects shows that impurity is not merely about "
                    "biological disease but about the broader incursion of death and decay "
                    "into the created order. The material world itself can be afflicted — "
                    "the consequences of the cosmic rupture extend beyond human bodies to "
                    "the fabric of daily life."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 14 — CLEANSING FROM TSARA'AT
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-14",
        "ref": "Leviticus 14",
        "chapter_num": 14,
        "title": "Cleansing the Leper — Resurrection Ritual",
        "era": "purity",
        "type": "chapter",
        "themes": ["HOLY", "PRIEST", "BLOOD", "TYPE"],

        "synopsis": (
            "Leviticus 14 describes the elaborate purification ritual for a person healed "
            "of tsara'at — a ritual so complex and symbolically rich that it functions as a "
            "resurrection ceremony. The person was socially dead (Lev 13:45-46); now they are "
            "being brought back to life. The ritual occurs in two stages: (1) An initial "
            "ceremony outside the camp involving two live clean birds, cedarwood, scarlet "
            "yarn, and hyssop. One bird is killed over running water in an earthenware vessel; "
            "the living bird, the wood, yarn, and hyssop are dipped in the blood-water mixture "
            "and sprinkled on the healed person seven times. Then the living bird is released "
            "into the open field — carrying the impurity away. The person shaves all hair, "
            "washes clothes, bathes, and may re-enter the camp (but not their tent) for seven "
            "days. (2) On the eighth day, a guilt offering ram, a sin offering lamb, and a "
            "burnt offering lamb are brought to the Tent of Meeting. The priest takes blood "
            "from the guilt offering ram and applies it to the person's right ear lobe, right "
            "thumb, and right big toe — the exact same application as the priestly ordination "
            "in chapter 8. Then oil is applied to the same three points and sprinkled before "
            "the LORD. The parallel to the ordination ritual is deliberate: the healed leper "
            "is being re-ordained to the human community, re-consecrated for life among God's "
            "people. The two-bird ritual has an unmistakable parallel to the two-goat ritual "
            "of the Day of Atonement (chapter 16): one killed, one released alive, carrying "
            "impurity into the wilderness. The chapter also addresses tsara'at in houses — "
            "greenish or reddish spots in the walls of a house, requiring priestly examination, "
            "quarantine, stone removal, replastering, and potentially total demolition."
        ),

        "key_verse": {
            "ref": "Leviticus 14:7",
            "text": "And he shall sprinkle it seven times on him who is to be cleansed of the leprous disease. Then he shall pronounce him clean and shall let the living bird go into the open field.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tohorat_hametsora", "tsipporim", "erez", "shani",
            "ezov", "mayim_chayyim", "asham", "shemen", "log"
            # Key glosses: tohorat ha-metsora = 'purification of the afflicted
            # person'; tsipporim = 'birds' (two live clean birds for the
            # purification ritual); erez = 'cedarwood' (durability, fragrance);
            # shani = 'scarlet yarn' (the color of blood/life); ezov = 'hyssop'
            # (small plant used for sprinkling — purification symbol, cf. Ps 51:7);
            # mayim chayyim = 'living/running water' (spring water, not stagnant
            # — life overcoming death); asham = 'guilt/reparation offering';
            # log = a liquid measure (~0.3 liters) of oil
        ],

        "ane_backdrop": (
            "Purification rituals involving birds are attested in the Hittite ritual tradition. "
            "The Hittite 'ritual of Ashella against plague' involves sending a bird carrying "
            "disease away into the wilderness — strikingly similar to the living bird released "
            "in Leviticus 14:7. Mesopotamian purification rituals (namburbi) similarly involve "
            "transferring impurity to an animal or object that is then removed. The cedar, "
            "hyssop, and scarlet combination appears to be uniquely Israelite — cedar (durability "
            "and fragrance), hyssop (purification, used in the Passover blood application, "
            "Exod 12:22), and scarlet yarn (the color of blood/life) together create a "
            "multi-sensory purification symbol. The running water (mayim chayyim, 'living "
            "water') over which the bird is slaughtered represents life overcoming death — "
            "the impurity of the 'dead' condition is washed away by living water."
        ),

        "second_temple": [
            {
                "source": "Mishnah Negaim 14:1-13",
                "summary": "Detailed rabbinic elaboration of the purification ceremony: "
                           "the species of birds, the length of cedar, the method of "
                           "sprinkling, and the integration of the two stages.",
                "relevance": "Preserves the oral tradition of how the ritual was (or would "
                             "be) performed, filling gaps in the biblical text."
            },
            {
                "source": "4Q274 (Purification Rules A)",
                "summary": "Qumran text describing purity regulations including provisions "
                           "for the metsora's reintegration into the community.",
                "relevance": "Shows the Qumran community maintained the tsara'at purification "
                             "framework as part of their rigorous purity practice."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 8:2-4", "note": "Jesus heals a leper and sends him to the priest 'for a testimony to them' — the Lev 14 ritual as messianic proof", "type": "nt"},
            {"ref": "Mark 1:44", "note": "'Offer for your cleansing what Moses commanded' — Jesus validates the Leviticus 14 procedure", "type": "nt"},
            {"ref": "Psalm 51:7", "note": "'Purge me with hyssop, and I shall be clean' — the hyssop of Leviticus 14 as a symbol of spiritual purification", "type": "ot"},
            {"ref": "John 7:38", "note": "'Rivers of living water will flow' — mayim chayyim language applied to the Spirit", "type": "nt"},
            {"ref": "Hebrews 9:19-22", "note": "Moses sprinkled blood with hyssop and scarlet wool — the Levitical purification elements in the covenant inauguration", "type": "nt"},
            {"ref": "Numbers 19:6", "note": "Cedar, hyssop, and scarlet yarn in the red heifer purification — the same combination for death-contamination purification", "type": "ot"},
            {"ref": "Hebrews 9:13-14", "note": "'If the blood of goats and bulls... sanctify for the purification of the flesh, how much more will the blood of Christ purify our conscience' — the Lev 14 purification ritual as shadow of Christ's cleansing power", "type": "nt"},
            {"ref": "Hebrews 13:11-13", "note": "'The bodies of those animals whose blood is brought into the holy places by the high priest as a sin offering are burned outside the camp. So Jesus also suffered outside the gate' — the outside-the-camp pattern of Lev 14 fulfilled in the crucifixion", "type": "nt"}
        ],

        "divine_council_note": (
            "The two-bird ritual in Leviticus 14 is a miniature version of the two-goat "
            "ritual in Leviticus 16 — one killed, one released. In the Day of Atonement, "
            "the released goat goes 'to Azazel' — into the wilderness, to the domain of "
            "the fallen Watcher. In Leviticus 14, the released bird carries the impurity "
            "into 'the open field' (pene hasadeh) — the wild, uncultivated space that "
            "represents the realm outside God's ordered domain. The symmetry is deliberate: "
            "both rituals send impurity away from God's presence into the chaotic, "
            "unconsecrated space. The ordination-parallel blood application (ear, thumb, "
            "toe) re-consecrates the healed person as an image-bearer in the community — "
            "restoring them to the priestly vocation of all Israel."
        ),

        "sections": [
            {
                "title": "The Two-Bird Ceremony Outside the Camp (14:1-7)",
                "content": (
                    "The healed person is examined by the priest OUTSIDE the camp — the "
                    "priest goes to the impure person, not the other way around. If healing "
                    "is confirmed, two live clean birds, cedarwood, scarlet yarn, and hyssop "
                    "are brought. One bird is slaughtered over running water (mayim chayyim) "
                    "in an earthenware vessel. The living bird, cedar, scarlet, and hyssop "
                    "are dipped in the blood-water mixture. The healed person is sprinkled "
                    "seven times. The priest pronounces them clean. The living bird is "
                    "released. This ritual is rich with symbolism: the killed bird represents "
                    "the 'death' the person has been in; the released bird represents new "
                    "life; the blood in running water combines death (blood) with life (living "
                    "water); the seven sprinklings mark complete purification. The bird "
                    "flying free is a visual parable of liberation from death."
                )
            },
            {
                "title": "The Seven-Day Transition (14:8-9)",
                "content": (
                    "The healed person shaves all body hair, washes clothes, bathes in water, "
                    "and may re-enter the camp. But they must remain outside their tent for "
                    "seven more days. On the seventh day, they shave again — all hair: head, "
                    "beard, eyebrows, all body hair — wash, and bathe. The complete hair "
                    "removal represents the shedding of the old 'dead' identity — like a "
                    "newborn, the person is hairless, fresh, starting over. The seven-day "
                    "period echoes creation and ordination. The person is being re-made, "
                    "re-born into the community. The transition from outside the camp "
                    "(socially dead) to inside the camp but outside the tent (liminal) to "
                    "full reintegration on the eighth day mirrors the movement from chaos "
                    "to order in Genesis 1."
                )
            },
            {
                "title": "The Eighth-Day Offerings (14:10-20)",
                "content": (
                    "On the eighth day: two male lambs without blemish, one ewe lamb, three-tenths "
                    "of an ephah of fine flour mixed with oil, and one log of oil. The guilt "
                    "offering (asham) lamb is presented with the log of oil as a wave offering. "
                    "The lamb is slaughtered, and its blood is applied to the person's right "
                    "ear lobe, right thumb, and right big toe — EXACTLY the ordination ritual "
                    "of Leviticus 8:23-24. The priest then takes oil, sprinkles it seven times "
                    "before the LORD, and applies it to the same three points: ear, thumb, toe — "
                    "on top of the blood. The remaining oil is poured on the person's head. "
                    "Then the sin offering and burnt offering are presented. The asham (guilt "
                    "offering) comes first because the impurity represents a 'trespass' "
                    "against the sacred order that requires restitution. The ordination-parallel "
                    "is the theological climax: the healed person is being re-inducted into "
                    "the priestly community of Israel."
                )
            },
            {
                "title": "Provision for the Poor (14:21-32)",
                "content": (
                    "If the healed person 'is poor and cannot afford so much,' the offerings "
                    "are scaled down: one male lamb for the guilt offering (the asham cannot "
                    "be substituted — it is essential to the re-consecration), one-tenth ephah "
                    "of flour, the log of oil, and two turtledoves or pigeons for the sin "
                    "and burnt offerings. The ritual procedure is identical — blood on ear, "
                    "thumb, toe; oil on the same points. The asham blood application cannot "
                    "be omitted regardless of economic status — the re-ordination is "
                    "non-negotiable. This sliding scale ensures that no healed person is "
                    "prevented from rejoining the community by poverty."
                )
            },
            {
                "title": "Tsara'at in Houses (14:33-53)",
                "content": (
                    "When Israel enters Canaan (note the future orientation — this law "
                    "anticipates settlement), houses may develop tsara'at: greenish or "
                    "reddish spots in the walls. The procedure parallels the skin diagnosis: "
                    "the house is emptied, the priest examines, quarantines for seven days, "
                    "re-examines. If it has spread, the affected stones are removed and "
                    "replaced, the house is replastered. If the affliction returns, the "
                    "entire house is demolished — torn down and its materials carried "
                    "outside the city to an unclean place. If the replastering succeeds, "
                    "the house is cleansed with the same two-bird ceremony used for "
                    "persons. The extension of tsara'at to architecture reinforces the "
                    "principle that impurity is not merely biological but cosmological — "
                    "the physical world itself participates in the clean/unclean system. "
                    "The land of Canaan, polluted by the practices of its previous "
                    "inhabitants, requires purification at every level."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 15 — BODILY DISCHARGES
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-15",
        "ref": "Leviticus 15",
        "chapter_num": 15,
        "title": "Bodily Discharges — The Taxonomy of Life Leaving the Body",
        "era": "purity",
        "type": "chapter",
        "themes": ["HOLY", "LAW"],

        "synopsis": (
            "Leviticus 15 addresses the ritual impurity caused by genital discharges — male "
            "and female, abnormal and normal. The chapter is structured symmetrically: "
            "abnormal male discharge (15:1-15), normal male discharge/seminal emission "
            "(15:16-18), normal female discharge/menstruation (15:19-24), and abnormal female "
            "discharge (15:25-30). The principle unifying all four cases is consistent: any "
            "discharge from the reproductive organs creates ritual impurity. Abnormal "
            "discharges (chronic male discharge, prolonged female bleeding) require "
            "seven-day purification after cessation plus sacrificial offerings (two "
            "turtledoves or pigeons — one sin offering, one burnt offering). Normal "
            "discharges (seminal emission, menstruation) create shorter impurity periods "
            "(until evening for seminal emission, seven days for menstruation) with no "
            "sacrifice required. The chapter emphasizes contagion: everything the impure "
            "person sits on, lies on, or touches transmits secondary impurity. Anyone who "
            "touches them or their bedding/seat must wash and is impure until evening. "
            "Sexual intercourse during menstruation makes the man unclean for seven days. "
            "The concluding verse states the purpose: 'Thus you shall keep the people of "
            "Israel separate from their uncleanness, lest they die in their uncleanness by "
            "defiling my tabernacle that is in their midst' (15:31). This is the key: the "
            "purity system protects the tabernacle. Accumulated impurity that reaches the "
            "sanctuary drives God's presence away (Ezek 10). The purity regulations are a "
            "buffer zone — they manage the inevitable impurities of human bodily existence "
            "so that the sacred center is not overwhelmed."
        ),

        "key_verse": {
            "ref": "Leviticus 15:31",
            "text": "Thus you shall keep the people of Israel separate from their uncleanness, lest they die in their uncleanness by defiling my tabernacle that is in their midst.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "zav", "zov", "shikevat_zera", "niddah",
            "tamei", "tahor", "mishkav", "moshav", "kaphar"
            # Key glosses: zav = 'a man with an abnormal genital discharge';
            # zov = 'the discharge itself' (chronic/pathological); shikevat
            # zera = 'seminal emission'; niddah = 'menstrual impurity/separation'
            # (from nadad, 'to separate/remove'); mishkav = 'bed/lying place'
            # (transmits secondary impurity from the zav/niddah); moshav =
            # 'seat/sitting place' (likewise transmits impurity)
        ],

        "ane_backdrop": (
            "Menstrual and discharge impurity is attested across ANE cultures. Mesopotamian "
            "texts describe the 'woman in her impurity' as restricted from temple access. "
            "Hittite laws regulate sexual contact during menstruation. Egyptian priestly "
            "purity requirements included restrictions related to bodily discharges. "
            "Zoroastrian purity laws (Vendidad) have elaborate menstrual impurity regulations "
            "with seclusion requirements. The Levitical system is distinctive in its "
            "symmetry (male and female discharges receive parallel treatment), its graduated "
            "severity (abnormal > normal), and its theological rationale (protecting the "
            "tabernacle rather than attributing demonic causation). The system does NOT "
            "treat female impurity as inherently worse than male — both require purification, "
            "and the structures are parallel."
        ),

        "second_temple": [
            {
                "source": "4Q274 (Purification Rules A)",
                "summary": "Qumran regulations expanding on Leviticus 15, including "
                           "specific distances the impure must maintain from the pure "
                           "and from sacred objects.",
                "relevance": "Demonstrates that Qumran intensified the discharge impurity "
                             "regulations — the community's rigorous purity practice went "
                             "beyond the biblical requirements."
            },
            {
                "source": "Mishnah Zavim and Niddah",
                "summary": "Two entire Mishnaic tractates devoted to the Leviticus 15 "
                           "regulations — Zavim for abnormal male discharge, Niddah for "
                           "female menstrual impurity.",
                "relevance": "The extent of rabbinic elaboration shows how central "
                             "discharge impurity was to Jewish practice — these tractates "
                             "remain operative in Orthodox Judaism today."
            },
            {
                "source": "11QTemple 45:7-18",
                "summary": "The Temple Scroll expands the menstrual and discharge purity "
                           "zones within the ideal temple city.",
                "relevance": "Shows the Qumran community's vision of the holy city "
                             "organized around concentric purity zones radiating from "
                             "the sanctuary."
            }
        ],

        "cross_refs": [
            {"ref": "Mark 5:25-34", "note": "The woman with the twelve-year blood flow touches Jesus and is healed — a Leviticus 15:25-30 case, and Jesus is NOT made unclean by the contact", "type": "nt"},
            {"ref": "Matthew 9:20-22", "note": "Parallel to Mark 5 — the hemorrhaging woman's faith makes her well, overcoming the impurity barrier", "type": "nt"},
            {"ref": "Leviticus 18:19", "note": "The Holiness Code prohibits sexual intercourse during menstruation — extending the Lev 15 impurity to moral law", "type": "ot"},
            {"ref": "Ezekiel 36:17", "note": "Israel's behavior is 'like the uncleanness of a woman in her menstrual impurity' — niddah as a metaphor for national sin", "type": "ot"},
            {"ref": "Revelation 21:27", "note": "'Nothing unclean will ever enter' the New Jerusalem — the purity principle perfected in eschatology", "type": "nt"},
            {"ref": "Ezekiel 22:10", "note": "Those who 'humble women in their menstrual impurity' are condemned — violation of niddah boundaries as moral failure", "type": "ot"},
            {"ref": "Hebrews 9:13-14", "note": "'If the blood of goats and bulls, and the sprinkling of defiled persons with the ashes of a heifer, sanctify for the purification of the flesh, how much more will the blood of Christ... purify our conscience' — the Lev 15 purification system was effective for external/ritual impurity; Christ's blood purifies the interior person", "type": "nt"},
            {"ref": "Hebrews 10:19-22", "note": "Believers now enter God's presence directly 'by the blood of Jesus' with 'bodies washed with pure water' — the Lev 15 concern (impurity defiling the tabernacle) is resolved permanently because Christ's sacrifice has cleansed the true sanctuary once for all", "type": "nt"}
        ],

        "divine_council_note": (
            "The concluding verse (15:31) provides the cosmic rationale: uncleanness that "
            "reaches the tabernacle causes death because it defiles the place where YHWH "
            "dwells — the earthly extension of the heavenly throne room. The purity system "
            "is a protective perimeter around the divine-human interface. In Ezekiel 10, "
            "the accumulated impurity of Israel drives the kavod (glory) of YHWH out of "
            "the temple — the divine council vacates the earthly meeting place. The "
            "discharge regulations ensure this never happens by managing the inevitable "
            "impurities of embodied human life. The Day of Atonement (Lev 16) is the "
            "annual purge that cleanses whatever has slipped through — the ultimate "
            "safeguard against the departure of the divine presence."
        ),

        "sections": [
            {
                "title": "Abnormal Male Discharge (15:1-15)",
                "content": (
                    "A man with an abnormal genital discharge (zav) — chronic or pathological — "
                    "becomes tamei and transmits impurity broadly: his bed, his seat, anything "
                    "he lies or sits on, anyone who touches him or his bedding, anyone he "
                    "spits on, any saddle he rides. Everyone who contacts these things must "
                    "wash clothes, bathe, and is unclean until evening. Earthenware vessels "
                    "he touches must be broken; wooden vessels must be rinsed. Seven days "
                    "after the discharge ceases, he washes clothes, bathes in running water "
                    "(mayim chayyim — living water), and on the eighth day brings two "
                    "turtledoves or pigeons: one sin offering, one burnt offering. The priest "
                    "makes atonement. The running water requirement (not just any water) "
                    "connects purification to life — living water symbolizes the life-force "
                    "that overcomes the death-association of the discharge."
                )
            },
            {
                "title": "Normal Male Emission (15:16-18)",
                "content": (
                    "A seminal emission (shikevat zera) makes the man unclean until evening. "
                    "He must bathe his whole body in water. Any garment or leather that has "
                    "semen on it must be washed and is unclean until evening. If a man lies "
                    "with a woman (consensual intercourse), both are unclean until evening "
                    "and both must bathe. No sacrifice is required — this is a minor, "
                    "temporary impurity. The brevity and simplicity of this section contrasts "
                    "with the abnormal discharge regulations, showing the graduated system: "
                    "normal biological functions create minimal impurity. Sexual intercourse "
                    "is NOT sinful — but the emission of reproductive fluid creates a "
                    "temporary ritual state because the life-producing substances have "
                    "been released."
                )
            },
            {
                "title": "Normal Female Menstruation (15:19-24)",
                "content": (
                    "A woman in her menstrual period (niddah) is tamei for seven days. "
                    "Whoever touches her is unclean until evening. Everything she lies or "
                    "sits on becomes unclean. Anyone who touches her bed or seat must wash "
                    "clothes, bathe, and is unclean until evening. If a man lies with her "
                    "during menstruation, he is unclean for seven days and his bed becomes "
                    "unclean. No sacrifice is required at the end of the seven days. The "
                    "menstrual impurity is structurally parallel to the normal male emission "
                    "but longer in duration, reflecting the longer biological process. The "
                    "system treats menstruation as a natural, regular event that creates "
                    "manageable impurity — not as a moral failing or punishment."
                )
            },
            {
                "title": "Abnormal Female Discharge (15:25-30)",
                "content": (
                    "A woman with an abnormal discharge — either prolonged menstruation or "
                    "non-menstrual bleeding — is tamei for the entire duration plus seven "
                    "days after it ceases. The impurity rules parallel the abnormal male "
                    "discharge (zav): her bed, seat, and contacts transmit impurity. After "
                    "cessation, she counts seven days, and on the eighth day brings two "
                    "turtledoves or pigeons for sin offering and burnt offering. The woman "
                    "with the twelve-year blood flow in Mark 5:25-34 has been in this state "
                    "for over a decade — perpetually tamei, unable to enter the temple, "
                    "excluded from normal social contact. When she touches Jesus' garment "
                    "and is healed, the theological significance is immense: Jesus is not "
                    "defiled by her impurity; instead, his holiness overwhelms her impurity. "
                    "Holiness proves more contagious than uncleanness."
                )
            },
            {
                "title": "The Purpose Statement (15:31-33)",
                "content": (
                    "The concluding verses provide the rationale for the entire purity system "
                    "of chapters 11-15: 'You shall keep the people of Israel separate from "
                    "their uncleanness, LEST THEY DIE in their uncleanness by defiling my "
                    "tabernacle that is in their midst.' This is not metaphorical. The "
                    "tabernacle is the intersection of heaven and earth — God's holy presence "
                    "literally dwells there. Impurity that contacts the holy creates a lethal "
                    "reaction (cf. Nadab and Abihu, Uzzah). The entire system of Leviticus "
                    "11-15 — dietary laws, postpartum purification, tsara'at regulations, "
                    "discharge impurity — serves one ultimate purpose: protecting the people "
                    "from dying by keeping their impurity from reaching God's dwelling. This "
                    "prepares for chapter 16: the Day of Atonement is the annual purification "
                    "of the sanctuary itself, cleansing it of all the accumulated impurity "
                    "that the daily management could not fully prevent."
                )
            }
        ]
    }
]
