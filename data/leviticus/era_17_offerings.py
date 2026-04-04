"""
era_17_offerings.py — The Sacrificial System (Leviticus 1-7)

The five major offerings form the grammar of Israel's worship: burnt offering (olah,
'that which ascends' — totally consumed by fire), grain offering (minchah, 'gift/tribute'
— the non-blood offering of flour and oil), peace offering (shelamim, from shalom,
'wholeness' — the shared communion meal), sin offering (chattat, 'purification offering'
— cleanses the sanctuary of sin's pollution), and guilt offering (asham, 'reparation
offering' — addresses the debt sin creates, requiring restitution). Each addresses a
different dimension of the God-human relationship — consecration, gratitude, fellowship,
purification, and restitution.
"""

CHAPTERS = [
    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 1 — THE BURNT OFFERING (OLAH)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-1",
        "ref": "Leviticus 1",
        "chapter_num": 1,
        "title": "The Burnt Offering — Total Consecration",
        "era": "offerings",
        "type": "chapter",
        "themes": ["BLOOD", "HOLY", "PRIEST", "TYPE"],

        "synopsis": (
            "Leviticus 1 opens with YHWH calling to Moses from the Tent of Meeting — the "
            "first divine speech from the newly completed tabernacle. The book begins not "
            "with narrative but with instruction (torah), establishing that the purpose of "
            "the tabernacle is not merely God's residence but the operational center of "
            "Israel's worship. The burnt offering (olah, from the root 'to ascend') is "
            "presented first because it represents the most fundamental act of worship: "
            "total consecration. The entire animal is consumed on the altar — nothing is "
            "kept for the worshiper or the priest (except the hide, 7:8). Three tiers of "
            "animals are permitted: a bull from the herd (the costliest), a male sheep or "
            "goat from the flock, or turtledoves/young pigeons (the offering of the poor). "
            "This graduated system ensures that no Israelite is excluded from worship by "
            "poverty. The ritual sequence — presentation, hand-laying (semikah), slaughter, "
            "blood manipulation, dismemberment, washing, and burning — is described with "
            "precise, almost clinical detail. The hand-laying is critical: the worshiper "
            "presses both hands on the animal's head, symbolically transferring identity "
            "so that the animal's total consumption represents the worshiper's total "
            "surrender to YHWH. The offering produces a 'pleasing aroma' (reach nichoach) "
            "to YHWH — not because God needs food (Ps 50:12-13), but because the act of "
            "willing self-surrender delights him. The olah is the offering of devotion: "
            "when nothing is demanded, everything is given."
        ),

        "key_verse": {
            "ref": "Leviticus 1:3-4",
            "text": "If his offering is a burnt offering from the herd, he shall offer a male without blemish. He shall bring it to the entrance of the tent of meeting, that he may be accepted before the LORD. He shall lay his hand on the head of the burnt offering, and it shall be accepted for him to make atonement for him.",
            "translation": "ESV"
        },

        "original_terms": [
            "olah", "korban", "tamim", "semikah", "dam", "mizbeach",
            "reach_nichoach", "kaphar", "ohel_moed", "esh"
            # Key glosses: korban = 'offering' (from qarab, 'to draw near');
            # tamim = 'without blemish/perfect'; semikah = 'hand-laying' (ritual
            # identification); dam = 'blood'; mizbeach = 'altar' (from zabach, 'to
            # slaughter'); reach nichoach = 'pleasing/restful aroma'; kaphar = 'to
            # atone/purge/cover'; ohel moed = 'tent of meeting'; esh = 'fire'
        ],

        "ane_backdrop": (
            "Burnt offerings were universal in the ancient Near East. Ugaritic texts "
            "(KTU 1.40, 1.109, 1.148) describe srp offerings (cognate with Hebrew saraph, "
            "'to burn') offered to El, Baal, and other deities. Mesopotamian temple "
            "rituals included the niqqu (regular burnt offering) presented to the gods' "
            "statues as daily food — the gods were thought to literally consume the smoke. "
            "The Egyptian ritual of 'the morning meal' involved burning offerings before "
            "the cult image in the temple. Leviticus subverts the ANE feeding-the-gods "
            "theology: YHWH does not eat (Psalm 50:12-13), and the pleasing aroma is "
            "a metaphor for divine acceptance, not divine hunger. The graduated tiering "
            "of animals (bull > sheep/goat > birds) has parallels in Punic sacrificial "
            "tariffs from Marseilles and Carthage, which specify which animals are "
            "acceptable and what portions go to the priests."
        ),

        "second_temple": [
            {
                "source": "Jubilees 6:1-3",
                "summary": "Noah offers a burnt offering after the flood, described in "
                           "language drawn from Leviticus 1. Jubilees places the origin "
                           "of the sacrificial system before Sinai, with the patriarchs.",
                "relevance": "Shows that Second Temple tradition understood the burnt "
                             "offering as a primordial institution, not merely a Sinaitic "
                             "innovation — Noah, Abraham, and Jacob all offered olot."
            },
            {
                "source": "Philo, De Specialibus Legibus I.198-211",
                "summary": "Philo allegorizes the burnt offering as the soul's complete "
                           "surrender to God. The fire represents divine reason consuming "
                           "the passions. The unblemished animal represents moral perfection.",
                "relevance": "Demonstrates Hellenistic Jewish interpretation that sought "
                             "philosophical meaning beneath the ritual — a precursor to "
                             "the Christian reading of sacrifice as spiritual transformation."
            },
            {
                "source": "Mishnah Zevachim 1-5",
                "summary": "Detailed rabbinic elaboration of the burnt offering procedure: "
                           "the layout of the altar, the method of slaughter, the blood "
                           "application, and the circumstances that invalidate the offering.",
                "relevance": "Preserves the oral tradition of how the Levitical system was "
                             "actually practiced in the Second Temple — filling in details "
                             "that Leviticus 1 leaves unspecified."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 10:1-10", "note": "The burnt offerings of the old covenant are 'shadows' — Christ's body offered 'once for all' is the reality they anticipated", "type": "nt"},
            {"ref": "Romans 12:1", "note": "Paul urges believers to present their bodies as 'living sacrifices' — the olah principle of total consecration spiritualized", "type": "nt"},
            {"ref": "Genesis 22:2-13", "note": "Abraham's near-sacrifice of Isaac is called an olah — the ultimate test of total surrender to YHWH", "type": "ot"},
            {"ref": "1 Kings 18:38", "note": "Elijah's burnt offering on Carmel consumed by fire from heaven — YHWH accepting the olah in dramatic fashion", "type": "ot"},
            {"ref": "Psalm 51:16-19", "note": "David recognizes that God desires a broken spirit over mere burnt offerings — the inward reality the ritual signifies", "type": "ot"},
            {"ref": "Ephesians 5:2", "note": "Christ 'gave himself up for us, a fragrant offering and sacrifice to God' — the reach nichoach language fulfilled", "type": "nt"},
            {"ref": "Isaiah 1:11-17", "note": "YHWH rejects burnt offerings offered without justice — the offering without the heart is meaningless", "type": "ot"},
            {"ref": "Hebrews 10:4", "note": "'It is impossible for the blood of bulls and goats to take away sins' — the olah system was always pointing beyond itself to the ultimate offering", "type": "nt"},
            {"ref": "Hebrews 13:15-16", "note": "'Through him let us continually offer up a sacrifice of praise' — the tamid (perpetual burnt offering) principle transformed into perpetual worship", "type": "nt"}
        ],

        "divine_council_note": (
            "The burnt offering addresses the fundamental problem created by the "
            "cosmic rebellion: the rupture between the holy divine realm and the "
            "profane human world. When Adam was expelled from Eden (the earthly "
            "council chamber), the pathway to God's presence was blocked. The olah "
            "is the restoration of that pathway — total surrender ascending as smoke "
            "to the heavenly throne room. The 'pleasing aroma' (reach nichoach) "
            "language connects to the divine council context: Genesis 8:21 uses the "
            "same phrase when Noah's post-flood offering reaches YHWH, prompting "
            "the covenant promise. The offering mediates between the earthly and "
            "heavenly realms, the tabernacle being the point where the two worlds "
            "intersect. The sacrificial system exists because the tabernacle is where "
            "heaven and earth overlap — it is an embassy of the divine council on "
            "earth. Without the offerings maintaining this sacred space, the overlap "
            "collapses and God's presence withdraws (Ezekiel 10). The entire system "
            "is grace: YHWH provides the means to remain in his presence."
        ),

        "sections": [
            {
                "title": "The Call from the Tent of Meeting (1:1-2)",
                "content": (
                    "Leviticus begins with the Hebrew word vayikra ('and he called'), "
                    "giving the book its Hebrew name. YHWH calls to Moses from the Tent "
                    "of Meeting (ohel moed). This is a significant shift from Exodus, "
                    "where God spoke from the mountaintop amid thunder and fire. Now "
                    "God speaks from within the tabernacle — he has moved in. The "
                    "tabernacle is operational, and the first order of business is "
                    "establishing the system by which Israel will approach their holy "
                    "God. The word korban ('offering,' from the root qarab, 'to draw "
                    "near') reveals the purpose of sacrifice: it is the means of "
                    "approach. In a world fractured by sin, one does not simply walk "
                    "into God's presence. The offering creates the pathway."
                )
            },
            {
                "title": "The Bull Offering — Full Ritual Sequence (1:3-9)",
                "content": (
                    "The most detailed description comes with the bull, the costliest "
                    "offering. The sequence is: (1) Select a male without blemish (tamim). "
                    "(2) Bring it to the entrance of the Tent of Meeting — not just "
                    "anywhere, but the designated place of encounter. (3) Lay a hand "
                    "(samak) on its head. The Hebrew semikah implies firm pressing, not "
                    "a light touch — it is an act of identification. (4) Slaughter the "
                    "bull 'before the LORD' — the worshiper kills the animal, not the "
                    "priest. This is significant: the cost is borne personally. (5) The "
                    "priests (sons of Aaron) collect the blood and throw (zaraq) it "
                    "against the sides of the altar — blood manipulation is exclusively "
                    "priestly. (6) The animal is flayed, cut into pieces, washed (entrails "
                    "and legs), and arranged on the altar fire. (7) The entire animal "
                    "ascends as an ishsheh, a 'fire offering,' producing a reach nichoach "
                    "('aroma of rest/satisfaction') to YHWH."
                )
            },
            {
                "title": "The Flock Offering — Sheep and Goats (1:10-13)",
                "content": (
                    "The procedure for small livestock parallels the bull but is less "
                    "costly. The animal must be male and without blemish. It is slaughtered "
                    "'on the north side of the altar before the LORD.' The specification of "
                    "the north side has generated significant discussion. Some scholars "
                    "note that north is the direction of divine encounter in Canaanite "
                    "mythology — Mount Zaphon, Baal's holy mountain, lies to the north. "
                    "Isaiah 14:13 associates the 'far reaches of the north' with the "
                    "divine council meeting place. The north-side specification may subtly "
                    "orient the sacrifice toward the heavenly realm. The blood is thrown "
                    "against the altar, the animal is dismembered, washed, and burned "
                    "entirely. The same 'pleasing aroma' formula concludes the section."
                )
            },
            {
                "title": "The Bird Offering — Provision for the Poor (1:14-17)",
                "content": (
                    "The turtledove or young pigeon offering ensures that even the poorest "
                    "Israelite can bring an olah. The procedure differs: the priest (not "
                    "the worshiper) performs the slaughter by wringing off the head. The "
                    "crop and feathers are removed and thrown beside the altar on the ash "
                    "heap to the east. The bird is torn open by its wings but not divided. "
                    "This is the offering Mary and Joseph bring at Jesus' dedication in "
                    "Luke 2:24, marking the holy family's poverty. The graduated system "
                    "reveals a God who calibrates the cost of worship to the means of the "
                    "worshiper — what matters is not the monetary value but the heart of "
                    "total surrender. The reach nichoach from a pigeon is the same as the "
                    "reach nichoach from a bull."
                )
            },
            {
                "title": "Atonement and the Logic of Substitution (1:4)",
                "content": (
                    "Verse 4 states that the burnt offering 'shall be accepted for him "
                    "to make atonement (kaphar) for him.' The verb kaphar is central to "
                    "Levitical theology. Its root meaning is debated: 'to cover' (from "
                    "Arabic kafara), 'to wipe/purge' (from Akkadian kuppuru), or 'to "
                    "ransom' (from Hebrew kopher). Milgrom argues convincingly for the "
                    "purgation meaning: sin pollutes the sanctuary, and the blood of "
                    "sacrifice is the ritual detergent that cleanses the contamination. "
                    "The atonement here is not merely juridical (a legal transaction) but "
                    "ontological — it addresses the real, quasi-physical effect of sin on "
                    "sacred space. The hand-laying creates identification between worshiper "
                    "and animal, so that the animal's death and total consumption represents "
                    "the worshiper's consecration. This is not mere symbolism; in the "
                    "Israelite worldview, ritual acts have real efficacy within the "
                    "divinely established system."
                )
            },
            {
                "title": "The Tamid — Daily Burnt Offering in Practice",
                "content": (
                    "Though described more fully in Exodus 29:38-42 and Numbers 28:1-8, "
                    "the daily burnt offering (tamid) is the application of Leviticus 1 "
                    "in perpetual practice. Two lambs were offered each day — one at "
                    "morning, one at twilight — maintaining the continuous 'pleasing aroma' "
                    "before YHWH. This was the heartbeat of the tabernacle (and later "
                    "temple) worship. When Daniel 8:11-13 and 11:31 prophesy the "
                    "'abomination of desolation,' it involves the cessation of the tamid — "
                    "the stopping of the daily burnt offering is the supreme desecration "
                    "because it severs the continuous connection between Israel and YHWH. "
                    "Jesus dies at the ninth hour (3 PM, Matt 27:46), the time of the "
                    "evening tamid — the ultimate burnt offering coincides with the daily "
                    "burnt offering. Hebrews 7:27 draws the contrast: Christ 'does not "
                    "need daily, like those high priests, to offer sacrifices' — his "
                    "single offering replaces the perpetual cycle."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 2 — THE GRAIN OFFERING (MINCHAH)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-2",
        "ref": "Leviticus 2",
        "chapter_num": 2,
        "title": "The Grain Offering — Tribute from the Land",
        "era": "offerings",
        "type": "chapter",
        "themes": ["BLOOD", "HOLY", "PRIEST"],

        "synopsis": (
            "Leviticus 2 introduces the grain offering (minchah), the only major offering "
            "that involves no animal blood. The minchah is presented in four forms: raw "
            "fine flour with oil and frankincense, oven-baked cakes or wafers, griddle-cooked "
            "cakes, or pan-cooked grain. A memorial portion (azkarah) is burned on the altar, "
            "and the remainder goes to the priests — it is 'most holy' (qodesh qodashim). "
            "The offering must never include leaven (chametz) or honey (devash), but must "
            "always include salt — the 'salt of the covenant' (melach berit). The minchah "
            "represents the fruit of human labor presented back to God: grain that was sown, "
            "cultivated, harvested, processed, and prepared. It acknowledges that the land "
            "and its produce belong to YHWH and that Israel is a tenant on God's soil. The "
            "word minchah itself means 'gift' or 'tribute' — the same word used for the "
            "tribute a vassal brings to a king (Gen 32:13, Judg 3:15). In offering minchah, "
            "the worshiper acknowledges YHWH as sovereign lord and oneself as dependent "
            "beneficiary. The prohibition of leaven and honey likely relates to their "
            "association with fermentation and decomposition — processes linked to corruption "
            "and thus incompatible with what is presented to the holy God. Salt, by contrast, "
            "preserves and purifies, symbolizing the enduring nature of the covenant bond."
        ),

        "key_verse": {
            "ref": "Leviticus 2:13",
            "text": "You shall season all your grain offerings with salt. You shall not let the salt of the covenant with your God be missing from your grain offering. With all your offerings you shall offer salt.",
            "translation": "ESV"
        },

        "original_terms": [
            "minchah", "solet", "levonah", "azkarah", "chametz",
            "devash", "melach_berit", "qodesh_qodashim", "shemen"
            # Key glosses: minchah = 'gift/tribute'; solet = 'fine flour';
            # levonah = 'frankincense'; azkarah = 'memorial portion' (the part
            # burned on the altar as a representative of the whole); chametz =
            # 'leaven/yeast'; devash = 'honey' (includes fruit syrup);
            # melach berit = 'salt of the covenant'; qodesh qodashim = 'most
            # holy' (restricted to priestly consumption); shemen = 'oil'
        ],

        "ane_backdrop": (
            "Grain offerings were standard throughout the ancient Near East. Mesopotamian "
            "temple inventories (such as the Ur III administrative texts) meticulously "
            "record grain, oil, and flour presented to the gods. Egyptian temple offering "
            "lists depict tables laden with bread, cakes, and grain alongside meat. The "
            "concept of the 'divine meal' — presenting food to the deity — was universal. "
            "Ugaritic texts describe minhatu offerings alongside animal sacrifice. The "
            "requirement of salt has ANE parallels: salt covenants are attested in "
            "Neo-Babylonian and Assyrian treaty texts, where sharing salt symbolizes an "
            "unbreakable bond. The prohibition of leaven finds a partial parallel in "
            "Greek and Roman religious practice, where unleavened bread (azuma) was "
            "sometimes prescribed for sacred contexts."
        ),

        "second_temple": [
            {
                "source": "Philo, De Specialibus Legibus I.271-275",
                "summary": "Philo interprets the grain offering as representing the "
                           "simplest form of worship — the person too poor for an animal "
                           "offering brings what the land provides.",
                "relevance": "Highlights the egalitarian principle: even the humblest "
                             "offering of flour is 'most holy' in God's estimation."
            },
            {
                "source": "Mishnah Menachot 1-6",
                "summary": "Elaborate rabbinic discussion of the grain offering types, "
                           "required quantities, and disqualifying procedures.",
                "relevance": "Preserves the practical details of grain offering practice "
                             "in the Second Temple, including the 'handful' technique for "
                             "the azkarah portion."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 4:3-5", "note": "Cain's offering of 'fruit of the ground' — the first minchah, rejected not for its type but for Cain's heart", "type": "ot"},
            {"ref": "1 Kings 18:36", "note": "Elijah calls on YHWH 'at the time of the offering of the minchah' — the grain offering marked the afternoon hour of prayer", "type": "ot"},
            {"ref": "Mark 9:49-50", "note": "Jesus says 'everyone will be salted with fire' — possible allusion to the salt of the covenant and altar fire", "type": "nt"},
            {"ref": "Matthew 5:13", "note": "'You are the salt of the earth' — disciples as covenant-salt preserving the world", "type": "nt"},
            {"ref": "1 Corinthians 5:6-8", "note": "Paul uses leaven as a metaphor for sin — 'cleanse out the old leaven' — drawing on Levitical symbolism", "type": "nt"},
            {"ref": "Malachi 1:11", "note": "A pure minchah will be offered among the nations — eschatological universalization of the grain offering", "type": "ot"}
        ],

        "divine_council_note": (
            "The grain offering may seem distant from divine council theology, but the "
            "'salt of the covenant' language (melach berit) connects it to the broader "
            "covenant framework. The covenant between YHWH and Israel is unique precisely "
            "because YHWH chose Israel as his own portion (Deut 32:8-9) while allotting "
            "the other nations to lesser elohim. The salt covenant seals this exclusive "
            "relationship. The minchah as tribute acknowledges YHWH's sovereignty — the "
            "same sovereignty the divine council recognizes in Psalm 82:8 when God is "
            "called to 'arise' and 'judge the earth' because the lesser gods have failed."
        ),

        "sections": [
            {
                "title": "Raw Flour Offering (2:1-3)",
                "content": (
                    "The simplest form: fine flour (solet) with oil poured on it and "
                    "frankincense placed upon it. The worshiper brings it to the priests, "
                    "and the priest takes a 'handful' (qomets) as the memorial portion "
                    "(azkarah) and burns it on the altar. The remainder belongs to Aaron "
                    "and his sons — it is qodesh qodashim ('most holy'), which means it "
                    "can only be eaten by priests in a holy place. The azkarah ('memorial') "
                    "is the portion that ascends to YHWH as a representative of the whole, "
                    "much as the olah ascends entirely. The frankincense (levonah) produces "
                    "the aromatic smoke; it is entirely burned, none going to the priests. "
                    "The combination of flour, oil, and frankincense represents the basic "
                    "sustenance of life presented back to the Life-giver."
                )
            },
            {
                "title": "Baked, Griddled, and Pan-Cooked Offerings (2:4-10)",
                "content": (
                    "Three prepared forms are described: (1) Oven-baked unleavened cakes "
                    "of fine flour mixed with oil, or unleavened wafers smeared with oil. "
                    "(2) Griddle-cooked cakes of fine flour with oil, broken into pieces "
                    "with oil poured over them. (3) Pan-cooked grain in fine flour with "
                    "oil. In each case, the memorial portion is burned and the rest is "
                    "priestly food. The diversity of preparation methods accommodates "
                    "different cooking technologies and cultural practices. The common "
                    "elements — fine flour, oil, absence of leaven — ensure consistency "
                    "of meaning regardless of form. The pouring of oil echoes anointing "
                    "rituals, sanctifying the grain as it is sanctified for presentation."
                )
            },
            {
                "title": "The Prohibition of Leaven and Honey (2:11-12)",
                "content": (
                    "No grain offering burned on the altar may contain leaven (se'or) or "
                    "honey (devash — which may include fruit syrup). Both can be brought "
                    "as firstfruit offerings (terumah) but may not ascend on the altar. "
                    "The prohibition is likely related to fermentation: leaven causes dough "
                    "to puff up and eventually decay; honey ferments into alcohol. Both "
                    "represent processes of corruption and decomposition — the opposite of "
                    "the purity required for what enters God's presence. In later Jewish "
                    "and Christian symbolism, leaven consistently represents sin, pride, "
                    "or corruption (Matt 16:6, 1 Cor 5:6-8). The altar receives only what "
                    "is uncorrupted, whole, and pure."
                )
            },
            {
                "title": "The Salt of the Covenant (2:13)",
                "content": (
                    "Every grain offering — indeed, every offering — must include salt. "
                    "The phrase 'salt of the covenant of your God' (melach berit elohekha) "
                    "introduces a concept found also in Numbers 18:19 and 2 Chronicles 13:5: "
                    "an enduring, inviolable covenant sealed with salt. Salt preserves "
                    "against decay, purifies water, and was used in ANE treaty ceremonies "
                    "as a symbol of permanent obligation. In contrast to leaven (which "
                    "corrupts), salt preserves. The salt covenant expresses the permanent "
                    "nature of YHWH's commitment to Israel and Israel's obligation to "
                    "YHWH. Every offering, by including salt, is a covenant renewal — a "
                    "reaffirmation of the bond between God and his people."
                )
            },
            {
                "title": "The Firstfruits Offering (2:14-16)",
                "content": (
                    "The grain offering of firstfruits (bikkurim) uses freshly roasted "
                    "grain — ears of new grain parched with fire, processed from fresh "
                    "ears. Oil and frankincense are added. The memorial portion is burned. "
                    "This offering marks the beginning of the harvest season and "
                    "acknowledges that the first and best belongs to YHWH. The firstfruits "
                    "principle runs throughout Scripture: Abel offered 'the firstborn of "
                    "his flock' (Gen 4:4); Israel itself is called 'the firstfruits of "
                    "his harvest' (Jer 2:3); Christ is 'the firstfruits of those who have "
                    "fallen asleep' (1 Cor 15:20). What is offered first sanctifies what "
                    "follows — the part represents and consecrates the whole."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 3 — THE PEACE OFFERING (SHELAMIM)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-3",
        "ref": "Leviticus 3",
        "chapter_num": 3,
        "title": "The Peace Offering — Communion at God's Table",
        "era": "offerings",
        "type": "chapter",
        "themes": ["BLOOD", "HOLY", "COV"],

        "synopsis": (
            "Leviticus 3 describes the peace offering (zebach shelamim), the most communal "
            "of the five major sacrifices. Unlike the burnt offering (entirely consumed) or "
            "the sin offering (priestly food), the peace offering is shared between God "
            "(the fat and blood), the priest (the breast and right thigh, per 7:31-34), "
            "and the worshiper's family (the remaining meat). It is a covenant meal — "
            "eating together in God's presence, a celebration of restored fellowship. The "
            "name shelamim derives from shalom ('peace/wholeness/completion'), indicating "
            "that this offering is brought when the relationship between God and worshiper "
            "is whole and healthy. It is the offering of joy, gratitude, and fellowship. "
            "Three types of animals are permitted: cattle (male or female), sheep, or goats. "
            "The offering may be male or female (unlike the olah, which requires males only), "
            "perhaps because it represents relationship rather than total consecration. The "
            "ritual involves the standard sequence of presentation, hand-laying, slaughter, "
            "and blood manipulation. The distinctive element is the fat: all internal fat "
            "(suet covering the entrails, fat on the kidneys, the caudate lobe of the liver) "
            "is burned on the altar as 'food for the fire offering' (lechem ishsheh). The "
            "fat is YHWH's portion — it represents the choicest, richest part. An absolute "
            "prohibition follows: 'You shall eat neither fat nor blood' (3:17) — a perpetual "
            "statute across all generations and dwellings. This prohibition elevates the "
            "peace offering above mere feasting: even in celebration, Israel must honor the "
            "sacred boundaries between human consumption and what belongs exclusively to God."
        ),

        "key_verse": {
            "ref": "Leviticus 3:16-17",
            "text": "And the priest shall burn them on the altar as a food offering with a pleasing aroma. All fat is the LORD's. It shall be a statute forever throughout your generations, in all your dwelling places, that you eat neither fat nor blood.",
            "translation": "ESV"
        },

        "original_terms": [
            "shelamim", "shalom", "zebach", "chelev", "dam",
            "klayot", "yoteret", "lechem_ishsheh", "semikah", "zaraq"
            # Key glosses: shelamim = 'peace/fellowship offering' (from shalom,
            # 'wholeness'); zebach = 'slaughter-sacrifice'; chelev = 'suet fat'
            # (the internal fat reserved for God); klayot = 'kidneys'; yoteret =
            # 'caudate lobe of the liver'; lechem ishsheh = 'food of the fire
            # offering' (God's portion); zaraq = 'to throw/splash' (blood against
            # the altar sides)
        ],

        "ane_backdrop": (
            "Communion sacrifices — meals shared between deity, priest, and worshiper — "
            "were widespread in the ANE. Ugaritic texts describe the dbh (slaughter/sacrifice, "
            "cognate with Hebrew zebach) as a communal feast in honor of the gods. The shlmm "
            "offering at Ugarit directly parallels the Hebrew shelamim, both linguistically "
            "and functionally. Mesopotamian kispu rituals involved feeding both gods and "
            "ancestors. Greek thysia sacrifices divided the animal between gods (thigh bones "
            "wrapped in fat, burned), priests, and participants — strikingly similar to the "
            "Levitical division. The key difference in Leviticus is the absolute prohibition "
            "of fat and blood consumption. In other ANE traditions, the worshiper ate "
            "whatever the god and priest did not claim. Israel's restriction elevates the "
            "theological significance: some things belong to God alone."
        ),

        "second_temple": [
            {
                "source": "Jubilees 21:7-10",
                "summary": "Abraham instructs Isaac on proper sacrifice, including the "
                           "peace offering procedure and the prohibition of consuming "
                           "blood, connecting it to the Noahic covenant (Gen 9:4).",
                "relevance": "Demonstrates that the blood prohibition was understood as "
                             "predating Sinai, rooted in the universal Noahic covenant — "
                             "binding on all humanity, not just Israel."
            },
            {
                "source": "1 Enoch 7:5",
                "summary": "The Watchers and their giant offspring 'began to sin against "
                           "birds, and beasts, and reptiles, and fish, and to devour one "
                           "another's flesh, and drink the blood.'",
                "relevance": "The consumption of blood is explicitly linked to the Watcher "
                             "rebellion. The Levitical blood prohibition may be understood "
                             "as reversing the corruption the Watchers introduced — forbidding "
                             "what the fallen ones taught."
            },
            {
                "source": "Mishnah Zevachim 5:6-8",
                "summary": "Detailed classification of peace offering subtypes: todah "
                           "(thanksgiving), neder (vow), nedavah (freewill). Each has "
                           "different time limits for consumption.",
                "relevance": "The Mishnah preserves the practical liturgical calendar of "
                             "peace offering consumption that governed Second Temple worship."
            }
        ],

        "cross_refs": [
            {"ref": "1 Corinthians 10:16-21", "note": "Paul describes the Lord's Supper as a covenant meal — 'participation in the body/blood of Christ' — the peace offering fulfilled", "type": "nt"},
            {"ref": "Exodus 24:9-11", "note": "The elders of Israel eat and drink in God's presence on Sinai — the archetypal peace offering meal", "type": "ot"},
            {"ref": "Deuteronomy 12:6-7", "note": "Instructions to bring peace offerings and 'eat before the LORD your God and rejoice' — the shelamim as worship-celebration", "type": "ot"},
            {"ref": "Luke 15:23-24", "note": "The fatted calf slaughtered for the prodigal son's return echoes the peace offering — a feast of restored relationship", "type": "nt"},
            {"ref": "Revelation 19:9", "note": "'Blessed are those invited to the marriage supper of the Lamb' — the eschatological peace offering", "type": "nt"},
            {"ref": "Acts 15:28-29", "note": "The Jerusalem Council retains the blood prohibition for Gentile believers — Leviticus 3:17 extended beyond Israel", "type": "nt"},
            {"ref": "Psalm 22:26", "note": "'The afflicted shall eat and be satisfied' — eschatological fulfillment of the peace offering meal", "type": "ot"}
        ],

        "divine_council_note": (
            "The peace offering is a covenant meal in God's presence — an earthly echo "
            "of the heavenly banquet. Exodus 24:9-11 shows the original pattern: Moses, "
            "Aaron, Nadab, Abihu, and seventy elders ascend Sinai and 'beheld God, and "
            "ate and drank.' They ate a covenant meal in the divine council's meeting "
            "place. The peace offering replicates this experience at the tabernacle. The "
            "fat and blood prohibition connects to the divine realm: these belong to "
            "YHWH because they represent life (blood) and the choicest substance (fat). "
            "The Watcher tradition in 1 Enoch associates blood consumption with the "
            "corruption of the created order — what the fallen ones introduced, YHWH "
            "categorically forbids."
        ),

        "sections": [
            {
                "title": "The Cattle Offering (3:1-5)",
                "content": (
                    "Male or female cattle may be offered — the first time females are "
                    "permitted, distinguishing the shelamim from the olah. The animal "
                    "must be without blemish (tamim). The worshiper lays hands on its "
                    "head at the entrance of the Tent of Meeting and slaughters it. The "
                    "priests throw the blood against the sides of the altar. Then the "
                    "fat is removed: all the fat covering the entrails, the fat on the "
                    "kidneys, and the caudate lobe of the liver. These are burned on "
                    "the altar 'on top of the burnt offering' — the peace offering rests "
                    "on the foundation of the burnt offering, suggesting that communion "
                    "with God (shelamim) presupposes consecration to God (olah)."
                )
            },
            {
                "title": "The Sheep Offering (3:6-11)",
                "content": (
                    "The sheep offering follows the same pattern but adds a distinctive "
                    "element: the fat tail (alyah). The breed of sheep common in the "
                    "ancient Near East — the fat-tailed sheep (Ovis laticaudata) — has "
                    "an enormous tail that can weigh 10-15 pounds, consisting almost "
                    "entirely of fat. This tail, 'removed close to the backbone,' is "
                    "added to the fat portions burned on the altar. The specificity "
                    "of this detail reflects intimate knowledge of the actual animals "
                    "used in sacrifice and argues against a purely theoretical or "
                    "late-invented text. The entire fat portion is called 'food of the "
                    "fire offering to the LORD' (lechem ishsheh la-YHWH) — 'food' "
                    "(lechem) is not literal but indicates the offering's role as the "
                    "divine portion of the shared meal."
                )
            },
            {
                "title": "The Goat Offering (3:12-16a)",
                "content": (
                    "The goat offering completes the triad. It follows the same sequence "
                    "as the cattle offering (no fat tail to account for). The fat "
                    "portions are identical: entrails fat, kidney fat, and liver lobe. "
                    "All are burned on the altar. The repeated precision of the fat "
                    "portions across all three animal types emphasizes that this is not "
                    "arbitrary — the internal fat is consistently sacred. The fat "
                    "represents the richest, most concentrated substance of the animal, "
                    "and offering it to YHWH acknowledges that the best belongs to God. "
                    "This principle extends beyond sacrifice: the firstfruits, the "
                    "firstborn, the tithe — the 'first and best' always goes to YHWH."
                )
            },
            {
                "title": "The Perpetual Prohibition: Fat and Blood (3:16b-17)",
                "content": (
                    "The chapter concludes with an absolute, universal prohibition: "
                    "'All fat is the LORD's. It shall be a statute forever throughout "
                    "your generations, in all your dwelling places, that you eat neither "
                    "fat nor blood.' This is emphatic — 'forever,' 'throughout your "
                    "generations,' 'in all your dwelling places.' The fat prohibition "
                    "refers specifically to the suet fat (chelev) of sacrificial animals, "
                    "not all animal fat in general. The blood prohibition is absolute "
                    "and will be elaborated in Leviticus 17:10-14 with its theological "
                    "rationale: 'the life (nephesh) of the flesh is in the blood.' "
                    "Together, these prohibitions create a permanent boundary between "
                    "human consumption and divine prerogative. Even in the context of "
                    "joyful feasting and communion, Israel remembers that some things "
                    "are reserved for God alone."
                )
            },
            {
                "title": "The Theology of Communion Sacrifice",
                "content": (
                    "The peace offering is unique among the five major sacrifices because "
                    "it is the only one that is truly shared: God receives the fat and "
                    "blood, the priest receives designated portions (breast and right "
                    "thigh, specified in 7:31-34), and the worshiper's family eats the "
                    "rest in a festive meal. This three-way sharing makes the peace "
                    "offering a covenant meal — an act of table fellowship between God, "
                    "his appointed mediators, and his people. Eating together in the "
                    "ancient world was a binding act of solidarity and trust. The peace "
                    "offering is the ritual expression of shalom — not merely the absence "
                    "of conflict but the presence of wholeness, harmony, and right "
                    "relationship. It is the sacrifice of celebration, offered when all "
                    "is well. The Last Supper and the Eucharist/Lord's Supper are the "
                    "New Covenant fulfillment of this principle: a meal shared in "
                    "God's presence, sealing the covenant bond."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 4 — THE SIN OFFERING (CHATTAT)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-4",
        "ref": "Leviticus 4",
        "chapter_num": 4,
        "title": "The Sin Offering — Purification of the Sanctuary",
        "era": "offerings",
        "type": "chapter",
        "themes": ["BLOOD", "HOLY", "PRIEST", "TYPE"],

        "synopsis": (
            "Leviticus 4 introduces the sin offering (chattat), the first offering "
            "explicitly designed to address sin. The Hebrew word chattat is related to "
            "the root chata' ('to miss the mark/sin'), but Milgrom argues it should be "
            "translated 'purification offering' because its primary function is not to "
            "punish the sinner but to purge the sanctuary of the pollution that sin generates. "
            "In Milgrom's revolutionary reading, sin is understood as a miasma — a real, "
            "quasi-physical contaminant that settles on the sanctuary, progressively "
            "defiling it. Unaddressed sin accumulates, eventually driving God's presence "
            "out of the tabernacle (as it does in Ezekiel 10). The chattat is the 'ritual "
            "detergent' that cleanses this contamination. The chapter structures the sin "
            "offering by social rank: the anointed priest (4:3-12), the whole congregation "
            "(4:13-21), a leader/chieftain (4:22-26), and a common person (4:27-35). The "
            "higher the rank of the sinner, the deeper the pollution penetrates into the "
            "sanctuary, and the more elaborate the blood ritual required to purge it. When "
            "the high priest sins, blood must be sprinkled seven times before the inner veil "
            "and applied to the horns of the incense altar — the pollution reaches the Holy "
            "Place. When a commoner sins, blood is applied only to the horns of the burnt "
            "offering altar in the outer court. This graduated system reveals a sophisticated "
            "theology of corporate responsibility: the leader's sin pollutes more deeply "
            "because it affects more people and carries greater covenantal weight. The "
            "offering addresses only inadvertent sin (bishgagah) — 'high-handed' (intentional, "
            "defiant) sin has no sacrifice (Numbers 15:30-31) and requires direct divine "
            "intervention or punishment."
        ),

        "key_verse": {
            "ref": "Leviticus 4:2",
            "text": "Speak to the people of Israel, saying, If anyone sins unintentionally in any of the LORD's commandments about things not to be done, and does any one of them...",
            "translation": "ESV"
        },

        "original_terms": [
            "chattat", "chata", "bishgagah", "kohen_mashiach", "parokhet",
            "qetoret", "kapporet", "qeren", "nasi", "nefesh"
            # Key glosses: chattat = 'purification/sin offering'; chata = 'to miss
            # the mark/sin'; bishgagah = 'inadvertently/unintentionally'; kohen
            # mashiach = 'anointed priest' (the high priest); parokhet = 'veil/
            # curtain' (separating Holy Place from Most Holy Place); qetoret =
            # 'incense'; kapporet = 'mercy seat/atonement cover' (on the ark);
            # qeren = 'horn' (of the altar); nasi = 'chieftain/leader';
            # nefesh = 'soul/life-force/self'
        ],

        "ane_backdrop": (
            "Purification rituals were common across the ANE. Mesopotamian namburbi "
            "rituals aimed to avert the consequences of ominous events — a form of "
            "'undoing' the effect of transgression. The Babylonian sharpu incantation "
            "series addresses sin through ritualized confession and symbolic burning. "
            "Hittite royal substitution rituals (the 'eviction of evil') involve "
            "transferring impurity to an animal or object and sending it away. The "
            "Egyptian 'Execration Texts' inscribed names of enemies on pots that were "
            "then smashed — symbolic destruction of impurity. Leviticus shares the "
            "logic of ritual purification with these traditions but locates the source "
            "of impurity specifically in covenant violation (sin) rather than ominous "
            "portents. The unique contribution of Leviticus 4 is the graduated blood "
            "manipulation: nowhere else in the ANE is the depth of ritual purification "
            "calibrated to the social status of the offender."
        ),

        "second_temple": [
            {
                "source": "4QMMT (Miqsat Ma'ase Ha-Torah)",
                "summary": "This Qumran halakhic letter debates the correct procedures "
                           "for sin offerings and purity, indicating that the interpretation "
                           "of Leviticus 4 was a live sectarian issue.",
                "relevance": "Shows that the chattat procedures were not merely historical "
                             "but actively debated in the Second Temple period — different "
                             "communities had competing interpretations of how to purify "
                             "the sanctuary correctly."
            },
            {
                "source": "Philo, De Specialibus Legibus I.226-238",
                "summary": "Philo explains the sin offering as addressing 'involuntary "
                           "offenses' and emphasizes that the different animals required "
                           "for different social ranks reflect the principle that greater "
                           "privilege entails greater responsibility.",
                "relevance": "Provides the Hellenistic Jewish philosophical interpretation "
                             "of the graduated system — moral responsibility scales with "
                             "social position."
            },
            {
                "source": "Josephus, Antiquities III.9.3",
                "summary": "Josephus describes the sin offering procedure for a "
                           "first-century audience, emphasizing its expiatory function "
                           "and the role of priestly blood manipulation.",
                "relevance": "Eyewitness-era account of how the chattat was understood "
                             "and practiced in the late Second Temple period."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 9:11-14", "note": "Christ enters the true Holy Place with his own blood, achieving purification that animal blood could only shadow", "type": "nt"},
            {"ref": "Romans 8:3", "note": "God sent his Son 'in the likeness of sinful flesh and for sin (peri hamartias — a sin offering)' — the chattat language applied to Christ", "type": "nt"},
            {"ref": "2 Corinthians 5:21", "note": "God 'made him to be sin (hamartia)' — Christ became the chattat, the purification offering itself", "type": "nt"},
            {"ref": "Numbers 15:30-31", "note": "High-handed sin has no sacrifice — it must be 'cut off,' revealing the limits of the sacrificial system", "type": "ot"},
            {"ref": "Hebrews 10:26-27", "note": "Echoes Numbers 15:30 — 'if we go on sinning deliberately, there no longer remains a sacrifice for sins'", "type": "nt"},
            {"ref": "Ezekiel 10:18-19", "note": "God's glory departs the temple due to accumulated impurity — the consequence of unaddressed sin that the chattat was designed to prevent", "type": "ot"},
            {"ref": "1 John 1:7", "note": "'The blood of Jesus his Son cleanses us from all sin' — the ultimate purification offering", "type": "nt"}
        ],

        "divine_council_note": (
            "The sin offering directly addresses the pollution that threatens to drive "
            "God's presence from the tabernacle. In the divine council framework, the "
            "tabernacle is the earthly copy of the heavenly throne room — the place where "
            "YHWH sits enthroned among his council (Isa 6:1-3, Heb 8:5). When sin "
            "pollutes the earthly sanctuary, it disrupts the heaven-earth interface. "
            "The chattat maintains the connection between realms. Ezekiel's vision of "
            "God's glory departing (Ezek 10) shows what happens when purification fails: "
            "the divine presence evacuates, leaving the temple as mere architecture. The "
            "graduated system — deeper pollution from higher-ranking sinners — reflects "
            "the council principle that authority bears cosmic weight."
        ),

        "sections": [
            {
                "title": "The Anointed Priest's Sin Offering (4:3-12)",
                "content": (
                    "When the anointed priest (kohen ha-mashiach) sins, he brings guilt "
                    "on the people (4:3) — his sin is not private but corporate. He must "
                    "offer a bull without blemish. The blood ritual is the most elaborate: "
                    "the priest dips his finger in the blood and sprinkles it seven times "
                    "before the veil (parokhet) of the Holy Place, then applies blood to "
                    "the horns of the incense altar inside the Holy Place. The remaining "
                    "blood is poured at the base of the burnt offering altar. The seven "
                    "sprinklings before the veil indicate that the priest's sin penetrates "
                    "to the boundary of the Most Holy Place. The bull's fat is burned on "
                    "the altar, but the rest of the animal is carried 'outside the camp' "
                    "to a clean place and burned entirely. The priest cannot eat his own "
                    "sin offering — he is both offerer and offender."
                )
            },
            {
                "title": "The Congregation's Sin Offering (4:13-21)",
                "content": (
                    "When the whole congregation sins inadvertently — a communal failure — "
                    "the same procedure applies as for the high priest: a bull, seven "
                    "sprinklings before the veil, blood on the incense altar horns. The "
                    "elders of the congregation lay their hands on the bull's head, "
                    "representing the entire community. This corporate sin offering "
                    "recognizes that communities, not just individuals, bear guilt. The "
                    "inadvertent nature ('the thing is hidden from the eyes of the "
                    "assembly,' 4:13) suggests structural sin — systemic failures that "
                    "no individual chose but all participated in. The ritual is identical "
                    "to the priest's because the congregation's collective standing before "
                    "God is analogous to the priest's individual standing."
                )
            },
            {
                "title": "The Leader's Sin Offering (4:22-26)",
                "content": (
                    "When a leader (nasi) sins, the blood ritual is less intense: blood "
                    "is applied to the horns of the burnt offering altar (outer court), "
                    "not the incense altar (Holy Place), and there is no sprinkling before "
                    "the veil. The animal is a male goat. The leader's sin pollutes the "
                    "outer court rather than the inner sanctuary. The remaining blood is "
                    "poured at the base of the altar. The fat portions are burned as in "
                    "the peace offering. The priest eats the meat. The nasi occupies a "
                    "middle position — more consequential than a commoner, less than the "
                    "priest who enters God's immediate presence."
                )
            },
            {
                "title": "The Common Person's Sin Offering (4:27-35)",
                "content": (
                    "The ordinary Israelite brings a female goat or female lamb. The blood "
                    "ritual is the simplest: blood on the horns of the burnt offering altar "
                    "and the rest poured at its base. No sprinkling before the veil, no "
                    "access to the inner sanctuary. The fat is burned, the priest eats the "
                    "meat. Two animals are offered as options, accommodating different "
                    "economic circumstances. The commoner's sin affects the outermost zone "
                    "of holiness. The graduated system teaches a profound lesson: sin always "
                    "pollutes, but the degree of pollution scales with the covenant "
                    "responsibility of the sinner. Greater proximity to God means greater "
                    "consequence for failure."
                )
            },
            {
                "title": "Milgrom's Purification Theology",
                "content": (
                    "Jacob Milgrom's interpretation of the chattat revolutionized Levitical "
                    "studies. He argued that the blood is not applied 'for' the sinner "
                    "(substitution) but 'on' the sanctuary (purification). Sin generates "
                    "a miasma that adheres to sacred objects. The blood — as the vehicle "
                    "of life (nephesh) — is the most potent purifying agent. When applied "
                    "to the altar and sanctuary, it absorbs and neutralizes the pollution. "
                    "This explains why the blood goes to different places depending on the "
                    "sinner's rank: more consequential sin penetrates deeper into the "
                    "sanctuary and requires deeper purification. The Day of Atonement "
                    "(Leviticus 16) is the annual 'deep clean' that purges accumulated "
                    "pollution from the entire sanctuary, including the Most Holy Place "
                    "where the ark sits — the holiest point on earth."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 5 — THE GUILT OFFERING (ASHAM)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-5",
        "ref": "Leviticus 5",
        "chapter_num": 5,
        "title": "The Guilt Offering — Restitution and Sacred Trespass",
        "era": "offerings",
        "type": "chapter",
        "themes": ["BLOOD", "HOLY", "LAW"],

        "synopsis": (
            "Leviticus 5 transitions from the sin offering to the guilt offering (asham), "
            "addressing cases where sin involves measurable trespass against God's holy "
            "things or against a neighbor. The chapter begins (5:1-13) with supplementary "
            "cases for the chattat — situations involving failure to testify, touching "
            "unclean things, or rash oaths — before transitioning to the asham proper "
            "(5:14-19). The asham differs from the chattat in a critical way: it requires "
            "restitution (5:16). Where the chattat purifies the sanctuary from sin's "
            "pollution, the asham addresses the economic or relational damage that sin "
            "causes. If someone inadvertently misuses ('commits a breach of faith,' ma'al) "
            "holy things — eating consecrated food, using dedicated property, failing to "
            "pay tithes — they must bring a ram as a guilt offering AND repay what was "
            "taken plus one-fifth (20%) as a penalty. The asham thus has a forensic, "
            "compensatory dimension absent from the chattat. It presupposes that sin is "
            "not merely a spiritual stain but a concrete violation that creates a debt. "
            "The ram must be valued in silver shekels according to the sanctuary standard, "
            "introducing a monetary calculus into the sacrificial system. This chapter "
            "also provides the poorest worshipers with alternatives: if someone cannot "
            "afford a lamb, they may bring two turtledoves or two young pigeons; if even "
            "that is beyond their means, a tenth of an ephah of fine flour suffices (5:11). "
            "This remarkable provision ensures that no one is excluded from atonement by "
            "poverty — the God of Israel meets every person at their economic reality."
        ),

        "key_verse": {
            "ref": "Leviticus 5:16",
            "text": "He shall also make restitution for what he has done amiss in the holy thing and shall add a fifth to it and give it to the priest. And the priest shall make atonement for him with the ram of the guilt offering, and he shall be forgiven.",
            "translation": "ESV"
        },

        "original_terms": [
            "asham", "maal", "shegagah", "tor", "yonah",
            "chamishit", "sheqel_haqqodesh", "kaphar", "salach", "nefesh"
            # Key glosses: asham = 'guilt/reparation offering' (requires restitution
            # plus 20% penalty); maal = 'breach of faith/sacrilege' (trespass against
            # holy things); tor = 'turtledove'; yonah = 'pigeon'; chamishit = 'one-
            # fifth' (the 20% penalty surcharge); sheqel haqqodesh = 'sanctuary shekel'
            # (the standard weight for sacred valuations); salach = 'to forgive'
        ],

        "ane_backdrop": (
            "The concept of sacrilege — trespass against sacred property — was treated "
            "with extreme severity throughout the ANE. Mesopotamian texts describe severe "
            "punishments for those who violated temple property or mishandled sacred objects. "
            "The Hittite Instructions for Temple Officials prescribe penalties for priests "
            "who eat sacred food improperly or allow contamination of temple goods. The "
            "Levitical asham is notable for its combination of ritual sacrifice and "
            "economic restitution — a dual remedy addressing both the spiritual and "
            "material dimensions of trespass. The 20% penalty surcharge (one-fifth added "
            "to the restitution) has parallels in Mesopotamian legal codes where "
            "misappropriation of temple goods requires repayment with substantial penalties. "
            "The Laws of Eshnunna and the Code of Hammurabi prescribe restitution for "
            "property violations, though typically at higher penalty rates (double to "
            "thirtyfold)."
        ),

        "second_temple": [
            {
                "source": "11QTemple (Temple Scroll) 35-36",
                "summary": "The Temple Scroll at Qumran expands the guilt offering "
                           "regulations, specifying additional categories of sacred "
                           "trespass requiring the asham.",
                "relevance": "Shows that the Qumran community took sacrilege against "
                             "holy things with utmost seriousness and developed expanded "
                             "halakhah around the asham."
            },
            {
                "source": "Mishnah Keritot 1:1-2",
                "summary": "Lists 36 transgressions punishable by 'cutting off' (karet) "
                           "from which the chattat/asham provides remedy when committed "
                           "inadvertently.",
                "relevance": "Systematizes the relationship between sin severity and "
                             "sacrificial remedy in the rabbinic tradition."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 53:10", "note": "The Servant's life is made an asham (guilt offering) — the most explicitly sacrificial verse about the Suffering Servant", "type": "ot"},
            {"ref": "1 Peter 2:24", "note": "'He himself bore our sins in his body on the tree' — Christ as the asham, bearing the debt of trespass", "type": "nt"},
            {"ref": "Numbers 5:5-8", "note": "Expands the restitution principle: if the wronged party has died, restitution goes to the nearest kinsman or to the priest", "type": "ot"},
            {"ref": "Luke 19:8", "note": "Zacchaeus voluntarily restores fourfold — exceeding the asham's one-fifth penalty", "type": "nt"},
            {"ref": "Ezra 10:19", "note": "The returning exiles offer a ram as a guilt offering for marrying foreign women — the asham applied to covenant breach", "type": "ot"},
            {"ref": "Hebrews 9:28", "note": "Christ 'offered once to bear the sins of many' — the once-for-all asham", "type": "nt"}
        ],

        "divine_council_note": (
            "Isaiah 53:10 is the pivotal divine council connection: YHWH makes his "
            "Servant's life an asham — a guilt offering. The Servant bears not just "
            "sin's pollution (chattat) but sin's debt (asham). In the divine council "
            "framework, the rebellion of the Watchers and the resulting corruption "
            "created not only spiritual contamination but a cosmic debt — the violation "
            "of sacred boundaries between heaven and earth. The asham principle teaches "
            "that such violations require both purification AND restitution. The ultimate "
            "asham — the Servant's life — addresses both dimensions simultaneously."
        ),

        "sections": [
            {
                "title": "Supplementary Sin Offering Cases (5:1-6)",
                "content": (
                    "Four situations require a chattat: (1) Failing to testify when one "
                    "has witnessed something and is publicly adjured — silence in the "
                    "face of injustice incurs guilt. (2) Touching an unclean carcass "
                    "(animal, livestock, or swarming thing) without realizing it. "
                    "(3) Touching human uncleanness of any kind unknowingly. "
                    "(4) Making a rash oath — swearing thoughtlessly to do something "
                    "good or bad and then forgetting it. In each case, when the person "
                    "'realizes his guilt' (ve-ashem), they must confess and bring a "
                    "female lamb or goat as a sin offering. The common thread is "
                    "inadvertence followed by realization — the moral conscience catching "
                    "up with the action. Confession (vidui) is required, making this "
                    "the first explicit demand for verbal acknowledgment of sin."
                )
            },
            {
                "title": "The Sliding Scale — Provision for the Poor (5:7-13)",
                "content": (
                    "If the worshiper 'cannot afford a lamb' (lo tasig yado), they may "
                    "bring two turtledoves or two young pigeons — one as a sin offering, "
                    "one as a burnt offering. The sin offering bird is killed by wringing "
                    "its neck (not severing the head), and its blood is sprinkled on the "
                    "side of the altar. If even birds are beyond reach, a tenth of an ephah "
                    "of fine flour suffices — no oil, no frankincense (to distinguish it "
                    "from the minchah). A handful is burned as a memorial portion. This "
                    "is extraordinary: a bloodless sin offering. The principle that 'the "
                    "life is in the blood' (17:11) is overridden by the principle of "
                    "access — God will not let poverty prevent atonement. The flour sin "
                    "offering demonstrates that the efficacy of sacrifice is not in the "
                    "material but in the divine acceptance."
                )
            },
            {
                "title": "Trespass Against Holy Things (5:14-16)",
                "content": (
                    "The asham proper begins: 'If anyone commits a breach of faith (ma'al) "
                    "and sins unintentionally in any of the holy things of the LORD.' "
                    "Sacred trespass (ma'al) involves misusing what has been consecrated — "
                    "eating priestly portions, using dedicated property, withholding tithes. "
                    "The remedy has two parts: (1) A ram valued in silver shekels by the "
                    "sanctuary standard as a guilt offering. (2) Full restitution of what "
                    "was misused, plus one-fifth (20%) added as penalty. The dual remedy "
                    "— sacrifice plus restitution — teaches that sin against God's holy "
                    "things requires both spiritual repair (the ram) and material repair "
                    "(the payment). You cannot merely apologize; you must make it right."
                )
            },
            {
                "title": "The Uncertain Guilt Offering (5:17-19)",
                "content": (
                    "A remarkable provision: if someone 'does any of the things that by "
                    "the LORD's commandments ought not to be done' but 'does not know it,' "
                    "they still 'bear their iniquity.' Even suspected sin requires an asham "
                    "ram. This addresses the anxiety of the scrupulous conscience — the "
                    "person who suspects they may have sinned but cannot be certain. The "
                    "offering provides resolution and assurance. Milgrom calls this the "
                    "'asham of doubt' — it covers the gray zone between known innocence "
                    "and known guilt. The fact that God provides a mechanism for uncertain "
                    "guilt reveals pastoral sensitivity: the sacrificial system is not a "
                    "cold legal code but a provision for real human psychology."
                )
            },
            {
                "title": "The Asham and Isaiah's Suffering Servant",
                "content": (
                    "The most theologically significant use of asham outside Leviticus is "
                    "Isaiah 53:10: 'When his soul makes an offering for guilt (asham).' "
                    "The Suffering Servant's life is explicitly identified as a guilt "
                    "offering — not a burnt offering (devotion), not a sin offering "
                    "(purification), but specifically an asham (restitution). This means "
                    "the Servant's death addresses not just the moral contamination of sin "
                    "but the debt sin creates. The asham requires payment with penalty — "
                    "the Servant pays not just what is owed but more than what is owed. "
                    "The New Testament authors build on this: Christ 'bore our sins' "
                    "(1 Pet 2:24), was 'made sin' (2 Cor 5:21), and 'gave himself as a "
                    "ransom' (1 Tim 2:6) — all asham language."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 6 — PERPETUAL FIRE AND PRIESTLY PROCEDURES
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-6",
        "ref": "Leviticus 6",
        "chapter_num": 6,
        "title": "Perpetual Fire — Instructions for the Priests",
        "era": "offerings",
        "type": "chapter",
        "themes": ["BLOOD", "PRIEST", "HOLY", "LAW"],

        "synopsis": (
            "Leviticus 6 shifts from the worshiper's perspective to the priest's. Chapters "
            "1-5 described what the Israelite brings and does; chapter 6 (beginning at 6:8 "
            "in Hebrew verse numbering) describes how the priest handles each offering. The "
            "chapter begins with a crucial addition to the asham legislation (6:1-7 in English): "
            "cases of sin against a neighbor — lying about a deposit, robbery, oppression, "
            "finding lost property and lying about it, or swearing falsely. These are "
            "deliberate sins, not inadvertent ones, yet they receive an asham provision. "
            "The catch: full restitution plus one-fifth must be paid FIRST, on the day the "
            "guilt offering is brought. This is remarkable — Leviticus generally restricts "
            "sacrifice to inadvertent sin, but these interpersonal crimes receive atonement "
            "through restitution plus sacrifice. The principle: sin against a neighbor IS "
            "sin against YHWH (ma'al ba-YHWH, 6:2). The chapter then provides priestly "
            "instructions for the burnt offering (the perpetual altar fire must never go "
            "out), the grain offering (the memorial portion procedure and priestly "
            "consumption rules), the high priest's daily grain offering (a half-ephah of "
            "fine flour, morning and evening, entirely burned), and the sin offering "
            "(cooked and eaten by priests in the court of the Tent of Meeting, with strict "
            "holiness contagion rules — whatever touches the meat becomes holy, blood "
            "splashed on garments must be washed in a holy place, and the earthenware "
            "vessel must be broken while bronze vessels are scoured). The 'holiness "
            "contagion' concept is extraordinary: holiness is treated as transmissible, "
            "spreading from the sacrificial meat to whatever contacts it."
        ),

        "key_verse": {
            "ref": "Leviticus 6:12-13",
            "text": "The fire on the altar shall be kept burning on it; it shall not go out. The priest shall burn wood on it every morning, and he shall arrange the burnt offering on it and shall burn on it the fat of the peace offerings. Fire shall be kept burning on the altar continually; it shall not go out.",
            "translation": "ESV"
        },

        "original_terms": [
            "esh_tamid", "maal", "gazal", "asham", "minchah",
            "kohen_gadol", "qodesh_qodashim", "chattat", "chavitin"
            # Key glosses: esh tamid = 'perpetual fire' (the altar fire that must
            # never go out — divine in origin, Lev 9:24); gazal = 'robbery/seizure';
            # kohen gadol = 'high priest'; chavitin = 'griddle cakes' (the high
            # priest's personal daily grain offering)
        ],

        "ane_backdrop": (
            "Perpetual sacred fires were maintained in temples throughout the ANE. The "
            "Zoroastrian tradition maintained eternal fires in fire temples (atash bahram), "
            "and while this tradition postdates Leviticus in its developed form, the concept "
            "of sacred fire as a symbol of divine presence is ancient. Mesopotamian temples "
            "maintained fires for incense and offering. The Roman Vestal Virgins maintained "
            "an eternal flame in the Temple of Vesta — the fire's extinction was considered "
            "a national catastrophe. The Levitical perpetual fire serves a practical purpose "
            "(the altar must always be ready to receive offerings) and a theological one "
            "(God's presence and Israel's worship never cease). The priestly instructions "
            "for handling sacrificial meat parallel Hittite instructions for temple "
            "officials, which similarly regulate how sacred food is prepared, consumed, "
            "and disposed of."
        ),

        "second_temple": [
            {
                "source": "2 Maccabees 1:18-36",
                "summary": "Claims the altar fire, hidden by priests before the exile, "
                           "was miraculously restored under Nehemiah — the perpetual fire "
                           "survived even the destruction of Solomon's temple.",
                "relevance": "Demonstrates how seriously the perpetual fire was taken: "
                             "its continuity was considered essential to legitimate worship."
            },
            {
                "source": "Mishnah Tamid 1-2",
                "summary": "Describes the daily procedures for maintaining the altar fire, "
                           "the arrangement of wood, and the morning clearing of ashes "
                           "in the Second Temple.",
                "relevance": "Preserves the operational reality of the perpetual fire — "
                             "priests slept in the temple precincts to ensure the fire "
                             "never went out."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 5:23-24", "note": "Jesus says to reconcile with your brother BEFORE bringing your offering — echoing Lev 6:1-7's principle that interpersonal restitution precedes sacrifice", "type": "nt"},
            {"ref": "Mark 9:49", "note": "'Everyone will be salted with fire' — fire and salt, the perpetual altar elements, applied to discipleship", "type": "nt"},
            {"ref": "Hebrews 12:29", "note": "'Our God is a consuming fire' — the perpetual altar fire as a theophanic symbol", "type": "nt"},
            {"ref": "1 Thessalonians 5:17", "note": "'Pray without ceasing' — the perpetual fire principle applied to Christian devotion", "type": "nt"},
            {"ref": "Isaiah 33:14", "note": "'Who among us can dwell with the consuming fire?' — the altar fire as the intersection of holiness and judgment", "type": "ot"},
            {"ref": "2 Chronicles 7:1", "note": "Fire from heaven consumes Solomon's inaugural offerings — divine origin of the altar fire", "type": "ot"}
        ],

        "divine_council_note": (
            "The perpetual fire on the altar represents the continuous connection between "
            "the earthly sanctuary and the heavenly throne room. In Ezekiel 1:4, 13, the "
            "divine throne is surrounded by fire; in Isaiah 6:6, a seraph brings a burning "
            "coal from the heavenly altar to purify Isaiah's lips. The altar fire is the "
            "earthly manifestation of the heavenly fire — the point of intersection between "
            "the two realms. Nadab and Abihu will be consumed for offering 'strange fire' "
            "(Lev 10:1-2), demonstrating that this connection is not symbolic but lethally "
            "real. The fire that mediates between heaven and earth cannot be trifled with."
        ),

        "sections": [
            {
                "title": "The Asham for Interpersonal Sin (6:1-7)",
                "content": (
                    "This section expands the guilt offering to cover deliberate sins against "
                    "neighbors: deceiving about a deposit or pledge, robbery, oppression, "
                    "finding lost property and lying, or false oaths. These are willful acts, "
                    "not inadvertent mistakes — yet they receive sacrificial remedy. The key: "
                    "restitution must come first. The offender must restore the stolen property "
                    "in full, add one-fifth as penalty, and deliver it 'on the day he realizes "
                    "his guilt.' Only then does the ram offering effect atonement. The sequence "
                    "matters: restoration before ritual. Jesus echoes this in Matthew 5:23-24: "
                    "'First be reconciled to your brother, and then come and offer your gift.' "
                    "Sin against a neighbor is called ma'al ba-YHWH — 'breach of faith against "
                    "the LORD' — because violating a covenant member violates the covenant Lord."
                )
            },
            {
                "title": "The Burnt Offering — Perpetual Fire (6:8-13)",
                "content": (
                    "The priest's instructions for the olah: it burns on the altar 'all night "
                    "until the morning,' and the fire must be kept burning. Each morning, the "
                    "priest dons his linen garments, clears the ashes (deshen) beside the "
                    "altar, changes to other garments, and carries the ashes to a 'clean place' "
                    "outside the camp. Fresh wood is laid every morning. The fire 'shall not go "
                    "out' is repeated twice for emphasis (6:12, 13). This perpetual fire has "
                    "divine origin — Leviticus 9:24 records fire 'from before the LORD' "
                    "consuming the inaugural offerings. The priest's daily routine maintains "
                    "what God initiated. The ash removal procedure — changing garments for the "
                    "task — shows that even mundane maintenance work in the sanctuary requires "
                    "attention to holiness protocols."
                )
            },
            {
                "title": "The Grain Offering — Priestly Instructions (6:14-18)",
                "content": (
                    "The priests' handling of the minchah: they present it before the LORD "
                    "at the front of the altar. A handful (with frankincense) is burned as "
                    "the memorial portion (azkarah). The remainder is eaten by Aaron and "
                    "his sons as unleavened cakes in the court of the Tent of Meeting. It "
                    "is qodesh qodashim — 'most holy' — and everything that touches it "
                    "becomes holy. This 'holiness contagion' concept (the transmissibility "
                    "of holiness) is remarkable: holiness is not merely a spiritual quality "
                    "but a powerful, almost physical force that spreads through contact. "
                    "This parallels the impurity contagion system but in reverse — both "
                    "holiness and impurity are 'catching.' Only authorized priests may "
                    "eat the most holy food."
                )
            },
            {
                "title": "The High Priest's Daily Grain Offering (6:19-23)",
                "content": (
                    "Aaron and his sons offer a perpetual grain offering (minchah tamid): "
                    "a tenth of an ephah of fine flour, half in the morning and half in "
                    "the evening, prepared as 'well-mixed cakes' (chavitin) on a griddle. "
                    "This offering is entirely burned — none goes to the priest. The high "
                    "priest's personal minchah complements the people's tamid sacrifices. "
                    "Every sin offering offered by a priest must likewise be entirely "
                    "burned — the priest cannot eat his own purification, just as a doctor "
                    "cannot prescribe for himself in certain contexts. This daily priestly "
                    "offering maintained the priest's personal consecration, acknowledging "
                    "that the mediator needs mediation."
                )
            },
            {
                "title": "The Sin Offering — Holiness Contagion (6:24-30)",
                "content": (
                    "Priestly instructions for the chattat: it must be slaughtered in the "
                    "same place as the burnt offering — 'before the LORD.' The priest who "
                    "offers it shall eat it in the court of the Tent of Meeting. Strict "
                    "holiness contagion rules follow: whatever touches the meat becomes "
                    "holy; if blood splashes on a garment, it must be washed in a holy "
                    "place; earthenware vessels in which it is cooked must be broken "
                    "(because pottery absorbs the holiness and cannot be purged), but "
                    "bronze vessels may be scoured and rinsed. Only male priests may eat "
                    "it. However, any sin offering whose blood is brought into the Tent "
                    "of Meeting (the inner sanctum purification — for the high priest's "
                    "or congregation's sin) must not be eaten but burned entirely. The "
                    "deeper the purification reaches, the more dangerous the offering "
                    "becomes — holiness intensifies as one approaches the divine center."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 7 — COMPLETION OF OFFERING INSTRUCTIONS
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-7",
        "ref": "Leviticus 7",
        "chapter_num": 7,
        "title": "Completing the Torah of Offerings — Priestly Portions and Final Laws",
        "era": "offerings",
        "type": "chapter",
        "themes": ["BLOOD", "PRIEST", "HOLY", "LAW"],

        "synopsis": (
            "Leviticus 7 completes the sacrificial instruction section that began in chapter 1, "
            "providing final priestly regulations for the guilt offering, the peace offering "
            "subtypes, and the assignment of priestly portions. The chapter covers the guilt "
            "offering procedures (7:1-10), the three types of peace offerings — thanksgiving "
            "(todah), vow (neder), and freewill (nedavah) — with their differing time limits "
            "for consumption (7:11-21), the absolute prohibition of fat and blood (7:22-27), "
            "and the 'wave offering' (tenufah) of the priest's portions — the breast and "
            "right thigh (7:28-36). The chapter closes with a colophon summarizing all the "
            "offerings described since chapter 1: 'This is the law (torah) of the burnt "
            "offering, the grain offering, the sin offering, the guilt offering, the "
            "ordination offering, and the peace offering, which the LORD commanded Moses at "
            "Mount Sinai' (7:37-38). The peace offering subtypes are theologically rich. The "
            "todah (thanksgiving) must be eaten the same day — joy cannot be hoarded or "
            "stored. The neder (vow) and nedavah (freewill) may extend to the second day but "
            "no further — by the third day, the meat becomes piggul ('an abomination') and "
            "anyone who eats it will be 'cut off' (karet). This severe penalty for eating "
            "stale offering-meat may seem disproportionate, but it enforces the temporal "
            "boundary of the sacred: the holiness of the offering has a shelf life, and "
            "treating expired sacred food as still valid is a fundamental category error. "
            "The prohibition against eating while in a state of uncleanness is equally severe "
            "— bringing impurity into contact with the most holy creates a dangerous collision "
            "of incompatible forces."
        ),

        "key_verse": {
            "ref": "Leviticus 7:37-38",
            "text": "This is the law of the burnt offering, of the grain offering, of the sin offering, of the guilt offering, of the ordination offering, and of the peace offering, which the LORD commanded Moses on Mount Sinai, on the day that he commanded the people of Israel to bring their offerings to the LORD, in the wilderness of Sinai.",
            "translation": "ESV"
        },

        "original_terms": [
            "torah", "todah", "neder", "nedavah", "piggul",
            "karet", "tenufah", "chazeh", "shoq", "chelev"
            # Key glosses: torah = 'instruction/law' (not merely 'law' but
            # 'teaching/direction'); todah = 'thanksgiving offering' (brought in
            # response to divine deliverance); neder = 'vow offering'; nedavah =
            # 'freewill offering'; piggul = 'abomination/loathsome' (sacred meat
            # kept past its time limit); karet = 'cutting off' (the most severe
            # penalty — excommunication or divine death); tenufah = 'wave/elevation
            # offering'; chazeh = 'breast' (priestly portion); shoq = 'thigh'
            # (priestly portion)
        ],

        "ane_backdrop": (
            "The division of sacrificial meat between deity, priest, and worshiper is "
            "attested across the ANE. Punic sacrificial tariffs from Marseilles and "
            "Carthage (CIS I.165) meticulously specify which portions go to the priests, "
            "which to the offerer, and which are entirely burned. The time limits for "
            "consumption find parallels in practical wisdom about meat spoilage in a hot "
            "climate, but the theological overlay — piggul, karet — elevates this beyond "
            "mere hygiene. Ugaritic texts describe royal feasts following temple sacrifices "
            "that parallel the todah celebration. The wave offering (tenufah) may correspond "
            "to the 'elevation offering' attested in Egyptian temple ritual, where priests "
            "present portions before the deity's image before consuming them."
        ),

        "second_temple": [
            {
                "source": "Mishnah Zevachim 5-6",
                "summary": "Classifies the offerings by their degree of holiness (qodshei "
                           "qodashim vs. qodashim qallim) and specifies the exact locations, "
                           "times, and personnel for eating each type.",
                "relevance": "Systematizes the Levitical regulations into the rabbinic "
                             "holiness taxonomy that governed Second Temple practice."
            },
            {
                "source": "Psalm 50:14, 23",
                "summary": "'Offer to God a sacrifice of thanksgiving (todah)... the one "
                           "who offers thanksgiving (todah) honors me' — God elevates the "
                           "todah above other sacrifices.",
                "relevance": "In post-exilic Jewish thought, the todah was increasingly "
                             "understood as the supreme sacrifice — the one that would "
                             "persist in the messianic age when sin offerings were no "
                             "longer needed."
            },
            {
                "source": "Jubilees 21:12-16",
                "summary": "Abraham's instructions to Isaac about proper sacrifice include "
                           "strict warnings about timing — offerings must be eaten promptly.",
                "relevance": "Confirms that the time-limit regulations were taken seriously "
                             "in Second Temple interpretation, not as mere ritual technicality "
                             "but as fundamental to proper worship."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 13:15", "note": "'Through him let us continually offer up a sacrifice of praise (todah) to God' — the todah as the abiding sacrifice", "type": "nt"},
            {"ref": "Psalm 116:17", "note": "'I will offer to you the sacrifice of thanksgiving (todah) and call on the name of the LORD' — todah paired with prayer", "type": "ot"},
            {"ref": "1 Corinthians 10:18", "note": "'Consider the people of Israel: are not those who eat the sacrifices participants in the altar?' — the communion principle of the shelamim", "type": "nt"},
            {"ref": "Leviticus 19:7-8", "note": "Reiterates the piggul prohibition — eating peace offering meat on the third day profanes what is holy", "type": "ot"},
            {"ref": "1 Samuel 2:12-17", "note": "Eli's sons violate the priestly portion regulations — seizing raw meat before the fat is burned, a sin 'very great before the LORD'", "type": "ot"},
            {"ref": "Malachi 1:7-8", "note": "The priests offer polluted food on the altar — blemished animals that violate the tamim requirement", "type": "ot"},
            {"ref": "John 6:53-56", "note": "'Unless you eat the flesh of the Son of Man and drink his blood' — the peace offering communion reframed in Christ", "type": "nt"}
        ],

        "divine_council_note": (
            "The colophon in 7:37-38 frames the entire sacrificial system as divine "
            "legislation — 'which the LORD commanded Moses at Mount Sinai.' This is not "
            "human invention but heavenly instruction. The tabernacle is built according "
            "to a 'pattern' (tavnit) shown on the mountain (Exod 25:9), and the "
            "sacrificial procedures are likewise revealed, not devised. Hebrews 8:5 makes "
            "this explicit: the priests serve 'a copy and shadow of the heavenly things.' "
            "The earthly sacrificial system mirrors the heavenly reality — the altar on "
            "earth corresponds to the altar in heaven (Rev 6:9-11). The priestly portions "
            "and communion meals are the earthly counterpart of the heavenly feast."
        ),

        "sections": [
            {
                "title": "The Guilt Offering — Priestly Procedure (7:1-10)",
                "content": (
                    "The asham is killed in the same place as the burnt offering. Its blood "
                    "is thrown against the sides of the altar. All the fat — the fat tail, "
                    "the fat covering the entrails, the kidneys and their fat, the liver "
                    "lobe — is burned on the altar. The meat is 'most holy' (qodesh qodashim) "
                    "and is eaten by the priests in a holy place. The same law governs the "
                    "sin offering and guilt offering regarding priestly consumption. "
                    "Additionally, the priest who offers any burnt offering keeps its hide. "
                    "Every grain offering — baked, griddled, or raw — belongs to all the "
                    "sons of Aaron equally. This equitable distribution ensures that all "
                    "priests benefit from the sacrificial system, not just those who happen "
                    "to officiate on a given day."
                )
            },
            {
                "title": "The Todah — Thanksgiving Peace Offering (7:11-15)",
                "content": (
                    "The todah (thanksgiving offering) is a subtype of the shelamim. It is "
                    "brought in response to a specific act of divine deliverance — rescue "
                    "from illness, danger, or distress (cf. Psalm 107). Alongside the "
                    "animal, the worshiper brings unleavened cakes mixed with oil, "
                    "unleavened wafers smeared with oil, cakes of fine flour mixed with oil, "
                    "AND loaves of leavened bread. The presence of leavened bread is remarkable "
                    "— it is prohibited on the altar (2:11) but permitted at the thanksgiving "
                    "meal. One loaf from each batch is set apart as a 'contribution' (terumah) "
                    "for the priest. The rest is eaten by the worshiper's family that same "
                    "day — nothing may remain until morning. The todah is the offering of "
                    "immediate, overflowing gratitude."
                )
            },
            {
                "title": "Vow and Freewill Offerings (7:16-18)",
                "content": (
                    "The neder (vow offering) and nedavah (freewill offering) are the other "
                    "two peace offering subtypes. The vow offering fulfills a promise made "
                    "to God — typically 'If you do X, I will offer a sacrifice.' The freewill "
                    "offering is pure generosity — no obligation, no response, just spontaneous "
                    "worship. Both may be eaten for two days (day of offering plus the next "
                    "day) — longer than the todah but not unlimited. On the third day, any "
                    "remaining meat becomes piggul ('abomination/loathsome thing') and must "
                    "be burned. Anyone who eats it 'shall bear his iniquity' — the penalty "
                    "is karet ('cutting off'), the most severe punishment in the Levitical "
                    "system. The sacred has a temporal limit; holiness is not indefinitely "
                    "storable."
                )
            },
            {
                "title": "Uncleanness and the Sacred Meal (7:19-21)",
                "content": (
                    "Meat that touches anything unclean must be burned — it cannot be eaten. "
                    "Conversely, any person who is clean may eat the peace offering meat. But "
                    "anyone who eats the peace offering while in a state of uncleanness "
                    "'shall be cut off from his people.' This collision of the sacred (holy "
                    "meat) and the impure (unclean person) is catastrophically dangerous — it "
                    "creates a short circuit between holiness and impurity that threatens "
                    "the entire system. The severity of the penalty reflects the cosmic "
                    "stakes: the peace offering is communion with God, and approaching God "
                    "while bearing impurity is an ontological violation."
                )
            },
            {
                "title": "The Fat and Blood Prohibition Restated (7:22-27)",
                "content": (
                    "The prohibition from 3:17 is restated with additional specificity and "
                    "the karet penalty: anyone who eats the chelev (suet fat) of ox, sheep, "
                    "or goat shall be cut off. The fat of an animal that dies naturally or "
                    "is torn by beasts may be used for other purposes but not eaten. Anyone "
                    "who eats blood of any animal shall be cut off. The blood prohibition "
                    "applies universally — not just in sacrificial contexts but in all "
                    "eating. The repetition and severity underscore that fat and blood belong "
                    "to YHWH alone. These are covenant boundary markers: every time an "
                    "Israelite refrains from eating fat or blood, they affirm YHWH's "
                    "sovereignty over life and sustenance."
                )
            },
            {
                "title": "The Wave Offering and Priestly Portions (7:28-38)",
                "content": (
                    "The worshiper personally presents (tenufah, 'wave/elevation offering') "
                    "the fat and the breast before the LORD. The priest burns the fat on the "
                    "altar; the breast goes to Aaron and his sons as their portion. The right "
                    "thigh (shoq ha-yamin) is given as a 'contribution' (terumah) to the "
                    "officiating priest. These priestly portions — the breast and right thigh "
                    "— are their 'perpetual due' from the people of Israel (7:34). This is "
                    "how the priests are fed: they live from the altar (cf. 1 Cor 9:13). The "
                    "chapter closes with the comprehensive colophon: 'This is the torah of "
                    "the burnt offering, the grain offering, the sin offering, the guilt "
                    "offering, the ordination offering, and the peace offering.' Torah here "
                    "means 'instruction' — the sacrificial system is divine pedagogy, "
                    "teaching Israel the grammar of approaching God."
                )
            }
        ]
    }
]
