"""
era_passion_night.py — The Night (Chapters 5-7)

The Last Supper, Gethsemane, the Trials. This is the heart of the
Passion narrative — the night everything changed. Jesus inaugurates
the new covenant in blood, absorbs the cup of divine wrath in an
olive press, and makes the claim that tears the high priest's robes:
the cloud-rider claim from Daniel 7:13.

Evidence tiers:
  [A] Canon Only — what the Gospels actually say
  [B] Canon + Inference — Hebrew/Greek analysis, covenant echoes, divine council
  [C] Full Picture — Second Temple sources, DSS, ANE parallels, Didache, Qumran meals
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 5: THE LAST SUPPER — COVENANT IN BLOOD
    # =========================================================================
    {
        "id": "passion-night-last-supper",
        "ref": "Luke 22:14-20, Ex 24:8, Jer 31:31-34",
        "chapter_num": 5,
        "title": "The Last Supper \u2014 Covenant in Blood",
        "era": "passion_night",
        "type": "chapter",

        "synopsis": "It is Thursday night. Jesus and the Twelve gather in an upper "
                    "room for the Passover meal \u2014 the annual remembrance of the night "
                    "God struck Egypt and passed over the blood-marked houses of Israel. "
                    "But this Passover is different. Jesus takes bread, blesses it, "
                    "breaks it, and says: 'This is my body, which is given for you.' "
                    "He takes the cup and says: 'This cup that is poured out for you "
                    "is the new covenant in my blood.' He is not improvising. He is "
                    "claiming to inaugurate what Jeremiah promised six centuries earlier "
                    "\u2014 the berit chadashah, the new covenant \u2014 and he is doing it at "
                    "a Passover table, binding the Exodus deliverance to what is about "
                    "to happen on a Roman cross.",

        "key_verse": {
            "ref": "Luke 22:20",
            "text": "And likewise the cup after they had eaten, saying, \u201cThis "
                    "cup that is poured out for you is the new covenant in my "
                    "blood.\u201d",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "anamn\u0113sis",
                "greek": "\u1f00\u03bd\u03ac\u03bc\u03bd\u03b7\u03c3\u03b9\u03c2",
                "meaning": "'Remembrance' \u2014 but not mere memory. The LXX uses "
                           "this same word for the memorial portion of the grain "
                           "offering (Leviticus 2:2), a living re-presentation "
                           "before God. When Jesus says 'do this in remembrance "
                           "of me,' he is using sacrificial vocabulary.",
                "verse": "Luke 22:19"
            },
            {
                "term": "diath\u0113k\u0113",
                "greek": "\u03b4\u03b9\u03b1\u03b8\u03ae\u03ba\u03b7",
                "meaning": "'Covenant' or 'testament.' The Greek word that "
                           "translates the Hebrew berit. In secular Greek it "
                           "means a last will and testament \u2014 which requires "
                           "the death of the one who made it (Hebrews 9:16-17). "
                           "Jesus uses a word that carries both covenant and "
                           "death-of-the-maker in a single term.",
                "verse": "Luke 22:20"
            },
            {
                "term": "paradid\u014dmi",
                "greek": "\u03c0\u03b1\u03c1\u03b1\u03b4\u03af\u03b4\u03c9\u03bc\u03b9",
                "meaning": "'To hand over, deliver, betray.' The same Greek verb "
                           "describes Judas betraying Jesus (Mark 14:10) and God "
                           "delivering his own Son (Romans 8:32). Same word, "
                           "opposite purposes \u2014 Judas hands Jesus over to death; "
                           "God hands Jesus over for salvation.",
                "verse": "Mark 14:10; Romans 8:32"
            },
            {
                "term": "berit chadashah",
                "hebrew": "\u05d1\u05b0\u05e8\u05b4\u05d9\u05ea \u05d7\u05b2\u05d3\u05b8\u05e9\u05c1\u05b8\u05d4",
                "meaning": "'New covenant.' The phrase Jeremiah 31:31 uses to "
                           "describe God's promise of a covenant written on the "
                           "heart, not on stone. Jesus claims THIS is what he is "
                           "inaugurating at the table.",
                "verse": "Jeremiah 31:31"
            },
            {
                "term": "pesach",
                "hebrew": "\u05e4\u05b6\u05bc\u05e1\u05b7\u05d7",
                "meaning": "'Passover.' From the verb meaning 'to pass over, "
                           "to spare.' The annual feast remembering the night "
                           "YHWH struck the firstborn of Egypt but passed over "
                           "every house marked with lamb's blood.",
                "verse": "Exodus 12:11"
            }
        ],

        "ane_backdrop": "Covenant-making in the ancient Near East was a blood ritual. "
                        "In the Mari texts and Hittite treaties, animals were slaughtered "
                        "and the parties walked between the pieces \u2014 a self-curse meaning "
                        "'may this be done to me if I break this covenant.' When God made "
                        "his covenant with Abraham (Genesis 15:9-17), HE ALONE walked "
                        "between the pieces as a smoking fire pot and flaming torch. The "
                        "entire cost of covenant-breaking fell on God. At the Last Supper, "
                        "that theological pattern reaches its climax: the covenant-maker "
                        "himself becomes the sacrifice that seals the covenant.",

        "second_temple": [
            {
                "source": "Exodus 24:3-8 (Sinai covenant ceremony)",
                "summary": "Moses took the blood of oxen and threw it on the people, "
                           "saying: 'Behold the blood of the covenant that the LORD "
                           "has made with you.' Jesus echoes this formula with "
                           "devastating precision \u2014 but replaces the animal's blood "
                           "with his own.",
                "relevance": "The direct Old Testament template for Jesus' words at "
                             "the Last Supper. Same vocabulary, radically different "
                             "mediator."
            },
            {
                "source": "Jeremiah 31:31-34",
                "summary": "Jeremiah's oracle of the new covenant: 'I will put my "
                           "law within them, and I will write it on their hearts.' "
                           "This covenant will not be like the Sinai covenant which "
                           "Israel broke.",
                "relevance": "The specific prophecy Jesus claims to fulfill when he "
                             "says 'the new covenant in my blood.' Six centuries of "
                             "prophetic expectation compressed into a single sentence "
                             "at a Passover table."
            },
            {
                "source": "1QS 6:4-5 (Community Rule, Qumran)",
                "summary": "According to the Qumran Community Rule, the community "
                           "held ritual meals where bread and wine were blessed by "
                           "the priest \u2014 a pattern that anticipates the messianic "
                           "banquet. The Dead Sea community saw their shared meals "
                           "as rehearsals for the age to come.",
                "relevance": "Shows that ritual meals with bread and wine in a "
                             "covenantal context were already part of the Jewish "
                             "theological landscape. Jesus transforms existing "
                             "practice, not inventing from nothing."
            }
        ],

        "cross_refs": [
            {"ref": "Luke 22:14-20", "note": "The Last Supper \u2014 new covenant inaugurated in Jesus' blood", "type": "nt"},
            {"ref": "Mark 14:22-25", "note": "Mark's account: 'This is my blood of the covenant, poured out for many'", "type": "nt"},
            {"ref": "1 Corinthians 11:23-26", "note": "Paul's account, the earliest written: 'as often as you eat this bread and drink the cup, you proclaim the Lord's death until he comes'", "type": "nt"},
            {"ref": "Exodus 12:1-13", "note": "The original Passover: unblemished lamb, blood on the doorposts, 'when I see the blood, I will pass over you'", "type": "ot"},
            {"ref": "Exodus 24:3-8", "note": "Moses throws the blood on the people: 'Behold the blood of the covenant' \u2014 the formula Jesus echoes", "type": "ot"},
            {"ref": "Jeremiah 31:31-34", "note": "The new covenant prophecy: 'I will write it on their hearts'", "type": "ot"},
            {"ref": "John 13:1-17", "note": "Jesus washes the disciples' feet \u2014 the priestly act of purification before the sacrifice", "type": "nt"},
            {"ref": "Hebrews 9:15-22", "note": "A diath\u0113k\u0113 (testament) requires the death of the one who made it", "type": "nt"},
            {"ref": "Exodus 12:46; John 19:36", "note": "Not a bone of the Passover lamb shall be broken \u2014 fulfilled at the cross", "type": "ot"},
            {"ref": "1QS 6:4-5 (Community Rule)", "note": "Qumran ritual meals with priestly blessing of bread and wine", "type": "dss"}
        ],

        "divine_council_note": "The Last Supper is a covenant inauguration ceremony \u2014 "
                               "and covenants in the biblical world are witnessed by the "
                               "divine council. When Moses read the Book of the Covenant "
                               "at Sinai, heaven watched. When Jesus inaugurates the new "
                               "covenant, the cosmic dimension is explicit: 'This cup is "
                               "the new covenant in my blood.' The footwashing (John 13) "
                               "reveals Jesus functioning as high priest before functioning "
                               "as sacrifice \u2014 a Melchizedekian priesthood in action, "
                               "operating outside the Levitical system entirely (he is from "
                               "Judah, not Levi). The powers that orchestrate his death do "
                               "not understand that they are fulfilling the covenant plan: "
                               "'None of the rulers of this age understood this' (1 Cor 2:8).",

        "sections": [
            # --- TIER A: CANON ONLY ---
            {
                "heading": "The Passover Table",
                "tier": "a",
                "body": "[A] It is the night of Passover. Jesus sends Peter and John "
                        "to prepare the meal (Luke 22:8). When the hour comes, he "
                        "reclines at table with the apostles and says: 'I have "
                        "earnestly desired to eat this Passover with you before I "
                        "suffer. For I tell you I will not eat it until it is "
                        "fulfilled in the kingdom of God' (Luke 22:15-16, ESV). He "
                        "takes bread, gives thanks, breaks it, and gives it to them: "
                        "'This is my body, which is given for you. Do this in "
                        "remembrance of me' (22:19). After supper he takes the cup: "
                        "'This cup that is poured out for you is the new covenant in "
                        "my blood' (22:20). In the same meal, he tells them: 'One of "
                        "you will betray me' (Mark 14:18). The table holds both "
                        "the covenant and the betrayal. The bread is broken. The "
                        "wine is poured. The Lamb identifies himself."
            },
            {
                "heading": "The Servant King",
                "tier": "a",
                "body": "[A] John's Gospel records what the Synoptics do not: before "
                        "the meal, Jesus rises from the table, lays aside his outer "
                        "garment, wraps a towel around his waist, pours water into "
                        "a basin, and begins to wash the disciples' feet (John "
                        "13:4-5). Peter protests: 'You shall never wash my feet.' "
                        "Jesus answers: 'If I do not wash you, you have no share "
                        "with me' (13:8). When he finishes, he says: 'I have given "
                        "you an example, that you also should do as I have done "
                        "to you. Truly, truly, I say to you, a servant is not "
                        "greater than his master' (13:15-16). The one who will be "
                        "hailed as King of kings performs the task of the lowest "
                        "household slave. He does it deliberately, knowing 'that "
                        "he had come from God and was going back to God' (13:3). "
                        "His authority is not diminished by the towel. It is "
                        "revealed by it."
            },
            # --- TIER B: HEBREW/GREEK ANALYSIS ---
            {
                "heading": "The Covenant Echoes",
                "tier": "b",
                "body": "[B] Jesus' words at the table are not spontaneous \u2014 they are "
                        "surgically precise echoes of Exodus 24. At Sinai, Moses "
                        "took the blood of the covenant sacrifice and threw it on "
                        "the people, saying: 'Behold the blood of the covenant that "
                        "the LORD has made with you' (Exodus 24:8, ESV). Jesus says: "
                        "'This is my blood of the covenant, which is poured out for "
                        "many' (Mark 14:24). The parallel is exact \u2014 except for one "
                        "devastating difference. In the Exodus ceremony, an animal "
                        "died. Here the covenant mediator himself IS the sacrifice. "
                        "The Passover lamb typology is precise: unblemished (Exodus "
                        "12:5), no bones broken (Exodus 12:46, fulfilled in John "
                        "19:36), blood applied for protection (Exodus 12:7). Paul "
                        "makes the identification explicit: 'Christ, our Passover "
                        "lamb, has been sacrificed' (1 Corinthians 5:7). Jesus does "
                        "not merely observe the Passover. He fulfills it."
            },
            {
                "heading": "Remembrance as Re-Presentation",
                "tier": "b",
                "body": "[B] 'Do this in remembrance (anamn\u0113sis) of me' (Luke 22:19). "
                        "English readers hear 'remembrance' and think nostalgia \u2014 "
                        "a mental exercise in recollection. The Greek anamn\u0113sis "
                        "(\u1f00\u03bd\u03ac\u03bc\u03bd\u03b7\u03c3\u03b9\u03c2) is not nostalgia. It is the same word the LXX "
                        "uses for the memorial portion of the grain offering "
                        "(Leviticus 2:2) \u2014 a portion brought before God as a LIVING "
                        "re-presentation, not a wistful looking back. The footwashing "
                        "reveals Jesus functioning in a priestly role: in the "
                        "Tabernacle, priests washed before entering service (Exodus "
                        "30:19-21). Jesus washes the disciples' feet before offering "
                        "himself as the sacrifice. He is high priest and lamb "
                        "simultaneously. This is the Melchizedekian priesthood in "
                        "action \u2014 he cannot be a Levitical priest (he is from Judah, "
                        "not Levi, Hebrews 7:13-14), but he functions as something "
                        "far greater: the eternal priest-king after the order of "
                        "Melchizedek (Psalm 110:4, Hebrews 5:6)."
            },
            # --- TIER C: FULL PICTURE ---
            {
                "heading": "The Betrayer and the Plan",
                "tier": "c",
                "body": "[C] Judas's betrayal uses the Greek paradid\u014dmi (\u03c0\u03b1\u03c1\u03b1\u03b4\u03af\u03b4\u03c9\u03bc\u03b9) "
                        "\u2014 'to hand over.' The same word appears in Romans 8:32: God "
                        "'did not spare his own Son but handed him over (pared\u014dken) "
                        "for us all.' Same verb. Same action. Opposite agents. Judas "
                        "hands Jesus to the authorities for thirty pieces of silver "
                        "(Matthew 26:15, fulfilling Zechariah 11:12-13). God hands "
                        "Jesus over as the definitive covenant sacrifice. According to "
                        "the Didache (c. 50-120 AD), one of the earliest post-apostolic "
                        "texts, eucharistic prayers preserved the same 'new covenant' "
                        "language: 'We thank you, our Father, for the holy vine of "
                        "David your servant, which you made known to us through Jesus "
                        "your servant' (Didache 9:2). According to the Community Rule "
                        "at Qumran (1QS 6:4-5), the Essene community held ritual "
                        "meals with priestly blessing of bread and wine \u2014 a practice "
                        "that prefigured the messianic banquet. Jesus transforms "
                        "existing Jewish liturgical practice into the inauguration "
                        "of a new covenant reality."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 6: GETHSEMANE — THE CUP AND THE COSMIC BATTLE
    # =========================================================================
    {
        "id": "passion-night-gethsemane",
        "ref": "Mark 14:32-42, Luke 22:39-46, Isa 51:17-22",
        "chapter_num": 6,
        "title": "Gethsemane \u2014 The Cup and the Cosmic Battle",
        "era": "passion_night",
        "type": "chapter",

        "synopsis": "After the meal, Jesus leads the disciples to the Garden of "
                    "Gethsemane \u2014 Gat Shmanim in Hebrew, 'the oil press.' At the "
                    "base of the Mount of Olives, in a garden named for the crushing "
                    "of olives, Jesus faces the full weight of what is coming. He "
                    "takes Peter, James, and John deeper into the garden and tells "
                    "them: 'My soul is very sorrowful, even to death' (Mark 14:34). "
                    "Then he falls on the ground and prays: 'Abba, Father, all "
                    "things are possible for you. Remove this cup from me. Yet not "
                    "what I will, but what you will' (Mark 14:36). This is not a "
                    "man afraid of pain. This is the only being in the cosmos who "
                    "fully comprehends what absorbing the wrath of an infinite God "
                    "means.",

        "key_verse": {
            "ref": "Mark 14:36",
            "text": "And he said, \u201cAbba, Father, all things are possible for "
                    "you. Remove this cup from me. Yet not what I will, but "
                    "what you will.\u201d",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "pot\u0113rion",
                "greek": "\u03c0\u03bf\u03c4\u03ae\u03c1\u03b9\u03bf\u03bd",
                "meaning": "'Cup.' In the prophets, THE cup is a fixed metaphor "
                           "for the cup of God's wrath \u2014 the full measure of "
                           "divine judgment against sin. Isaiah 51:17, Jeremiah "
                           "25:15, Psalm 75:8. Jesus is not asking to avoid "
                           "suffering in general. He is asking to be spared the "
                           "cup of divine wrath that the prophets describe.",
                "verse": "Mark 14:36"
            },
            {
                "term": "ag\u014dnia",
                "greek": "\u1f00\u03b3\u03c9\u03bd\u03af\u03b1",
                "meaning": "'Agony, intense struggle.' From ag\u014dn (a contest, "
                           "a fight). Luke uses this word to describe Jesus' "
                           "state in the garden \u2014 not passive suffering but "
                           "active combat. The word implies an opponent.",
                "verse": "Luke 22:44"
            },
            {
                "term": "exousia tou skotous",
                "greek": "\u1f10\u03be\u03bf\u03c5\u03c3\u03af\u03b1 \u03c4\u03bf\u1fe6 \u03c3\u03ba\u03cc\u03c4\u03bf\u03c5\u03c2",
                "meaning": "'Authority/power of darkness.' Jesus uses this phrase "
                           "in Luke 22:53 to name the cosmic force behind the "
                           "events of the night. This is not metaphorical \u2014 "
                           "exousia is the word Paul uses for the hostile "
                           "spiritual powers in Ephesians 6:12.",
                "verse": "Luke 22:53"
            },
            {
                "term": "dakka",
                "hebrew": "\u05d3\u05b7\u05bc\u05db\u05bc\u05b8\u05d0",
                "meaning": "'Crushed, broken to pieces.' Isaiah 53:5: 'He was "
                           "crushed for our iniquities.' The same crushing "
                           "action the oil press performs on olives \u2014 in a "
                           "garden named 'oil press,' the Servant is crushed.",
                "verse": "Isaiah 53:5"
            },
            {
                "term": "Gat Shmanim",
                "hebrew": "\u05d2\u05b7\u05bc\u05ea \u05e9\u05b0\u05c1\u05de\u05b8\u05e0\u05b4\u05d9\u05dd",
                "meaning": "'Oil press.' The name of the garden itself is "
                           "theological: olives are crushed to produce oil. "
                           "The location where Jesus agonizes is named for "
                           "the process that is happening to him.",
                "verse": "Mark 14:32"
            }
        ],

        "ane_backdrop": "Mountains in the ancient Near East were sites of divine "
                        "encounter \u2014 Sinai, Zion, Carmel, Hermon. The Mount of Olives "
                        "has its own theological weight in the Hebrew Bible: it is the "
                        "mountain from which Ezekiel watched the glory of YHWH depart "
                        "from the Temple (Ezekiel 11:23), and the mountain to which "
                        "Zechariah says YHWH will return and stand on the day of final "
                        "battle (Zechariah 14:4). Jesus prays at the base of this "
                        "mountain \u2014 the mountain of departure and return \u2014 on the night "
                        "that sets the return in motion.",

        "second_temple": [
            {
                "source": "Isaiah 51:17-22 (the cup of wrath)",
                "summary": "Isaiah describes Jerusalem as having drunk 'the cup "
                           "of staggering' from the hand of YHWH. The cup is "
                           "the bowl of God's wrath \u2014 and God promises to take "
                           "it from Jerusalem's hand and put it into the hand "
                           "of her tormentors.",
                "relevance": "Jesus asks for THIS cup to be removed. The prophetic "
                             "background makes his prayer intelligible: he is not "
                             "asking to avoid inconvenience but to be spared the "
                             "full concentrated wrath of God against all sin."
            },
            {
                "source": "Isaiah 53:5, 10 (the crushed Servant)",
                "summary": "The Servant of YHWH is 'crushed for our iniquities' "
                           "and 'it was the will of the LORD to crush him.' The "
                           "Hebrew dakka describes being broken to pieces.",
                "relevance": "The garden named 'oil press' and the Isaiah 53 "
                             "Servant who is 'crushed' converge at Gethsemane. "
                             "The location, the language, and the theology align."
            },
            {
                "source": "Testament of Levi 18:12 (Testaments of the Twelve Patriarchs)",
                "summary": "According to this Second Temple text, the eschatological "
                           "priest will 'bind Beliar' and give power to his "
                           "children to trample evil spirits. The language of "
                           "cosmic combat between the priestly figure and the "
                           "powers of darkness parallels the Gethsemane scene.",
                "relevance": "Shows that the expectation of a priestly figure "
                             "engaged in cosmic battle against evil powers was "
                             "part of the Second Temple theological landscape."
            }
        ],

        "cross_refs": [
            {"ref": "Mark 14:32-42", "note": "Gethsemane: 'Remove this cup from me. Yet not what I will, but what you will'", "type": "nt"},
            {"ref": "Luke 22:39-46", "note": "Luke adds the angel strengthening Jesus and the sweat like drops of blood", "type": "nt"},
            {"ref": "Matthew 26:36-46", "note": "Matthew's parallel: 'My Father, if it be possible, let this cup pass from me'", "type": "nt"},
            {"ref": "Isaiah 51:17-22", "note": "The cup of YHWH's wrath \u2014 Jerusalem drunk from 'the bowl, the cup of staggering'", "type": "ot"},
            {"ref": "Jeremiah 25:15-16", "note": "'Take from my hand this cup of the wine of wrath and make all the nations drink it'", "type": "ot"},
            {"ref": "Psalm 75:8", "note": "'In the hand of the LORD there is a cup with foaming wine, well mixed, and he pours out from it'", "type": "ot"},
            {"ref": "Isaiah 53:5, 10", "note": "'He was crushed for our iniquities' \u2014 dakka, broken to pieces in the oil press", "type": "ot"},
            {"ref": "Ezekiel 11:23", "note": "The glory of YHWH departed from Jerusalem and stood on the Mount of Olives", "type": "ot"},
            {"ref": "Zechariah 14:4", "note": "YHWH's feet will stand on the Mount of Olives on the day of final battle", "type": "ot"},
            {"ref": "Luke 22:53", "note": "'This is your hour, and the power (exousia) of darkness' \u2014 Jesus names the cosmic dimension", "type": "nt"},
            {"ref": "Ephesians 6:12", "note": "Paul names the same hostile exousiai: 'cosmic powers over this present darkness'", "type": "nt"},
            {"ref": "Hebrews 5:7", "note": "'In the days of his flesh, Jesus offered up prayers and supplications, with loud cries and tears'", "type": "nt"}
        ],

        "divine_council_note": "Gethsemane reveals the cosmic dimension of the Cross. "
                               "Jesus names it explicitly: 'This is your hour, and the "
                               "power (exousia) of darkness' (Luke 22:53). The hostile "
                               "spiritual powers \u2014 the same exousiai Paul describes in "
                               "Ephesians 6:12 and Colossians 2:15 \u2014 are orchestrating "
                               "the arrest and execution, believing they are destroying "
                               "the seed of the woman. An angel from heaven strengthens "
                               "Jesus (Luke 22:43) \u2014 a member of the loyal divine "
                               "council sent to sustain the incarnate Son in his agony. "
                               "The cosmic irony is total: the powers of darkness are "
                               "about to hand God exactly what he needs to defeat them. "
                               "'None of the rulers of this age understood this, for if "
                               "they had, they would not have crucified the Lord of "
                               "glory' (1 Corinthians 2:8).",

        "sections": [
            # --- TIER A: CANON ONLY ---
            {
                "heading": "The Oil Press",
                "tier": "a",
                "body": "[A] After the supper, Jesus goes out to the Mount of "
                        "Olives, 'as was his custom' (Luke 22:39). He enters a "
                        "place called Gethsemane \u2014 'oil press' \u2014 and tells his "
                        "disciples: 'Sit here while I pray' (Mark 14:32). He "
                        "takes Peter, James, and John deeper into the garden. "
                        "'And he began to be greatly distressed and troubled. "
                        "And he said to them, \"My soul is very sorrowful, even "
                        "to death. Remain here and watch\"' (Mark 14:33-34, ESV). "
                        "He goes a little farther, falls on the ground, and "
                        "prays: 'Abba, Father, all things are possible for you. "
                        "Remove this cup from me. Yet not what I will, but what "
                        "you will' (14:36). Three times he prays. Three times he "
                        "returns to find the disciples sleeping. 'The spirit "
                        "indeed is willing, but the flesh is weak' (14:38)."
            },
            {
                "heading": "The Sweat and the Angel",
                "tier": "a",
                "body": "[A] Luke alone records the intensity: 'And being in "
                        "agony he prayed more earnestly; and his sweat became "
                        "like great drops of blood falling down to the ground' "
                        "(Luke 22:44, ESV). And Luke alone records the help: "
                        "'And there appeared to him an angel from heaven, "
                        "strengthening him' (22:43). The one who commands "
                        "legions of angels (Matthew 26:53) receives strength "
                        "from a single one. He could summon twelve legions. "
                        "He does not. He submits. 'Not my will, but yours, "
                        "be done' (Luke 22:42). Then he rises, returns to the "
                        "disciples, and says: 'The hour has come. The Son of "
                        "Man is betrayed into the hands of sinners. Rise, let "
                        "us be going; see, my betrayer is at hand' (Mark "
                        "14:41-42). He walks toward the arrest, not away from it."
            },
            {
                "heading": "The Arrest \u2014 The Power of Darkness",
                "tier": "a",
                "body": "[A] While Jesus is still speaking, Judas arrives with a "
                        "crowd armed with swords and clubs, sent from the chief "
                        "priests, scribes, and elders (Mark 14:43). Judas has "
                        "given them a signal: 'The one I will kiss is the man. "
                        "Seize him and lead him away under guard' (Mark 14:44). "
                        "He steps forward, says 'Rabbi!' and kisses him (14:45). "
                        "Jesus answers: 'Judas, would you betray the Son of Man "
                        "with a kiss?' (Luke 22:48). One of those standing nearby "
                        "draws a sword and strikes the servant of the high priest, "
                        "cutting off his ear (Mark 14:47). Luke alone records what "
                        "happens next: 'No more of this!' Jesus says, and he "
                        "touches the servant's ear and heals him (Luke 22:51). In "
                        "the middle of his own arrest, he heals his enemy's "
                        "servant. Then he turns to the crowd: 'Have you come out "
                        "as against a robber, with swords and clubs to capture "
                        "me? Day after day I was with you in the temple teaching, "
                        "and you did not seize me' (Mark 14:48-49). And then the "
                        "line that names the true nature of the night: 'But this "
                        "is your hour, and the power of darkness' (Luke 22:53). "
                        "Exousia tou skotous \u2014 the authority of darkness. Jesus "
                        "does not say 'the chief priests are arresting me.' He "
                        "names the cosmic force operating behind them. The "
                        "disciples flee. All of them. And Jesus is led away alone "
                        "into the jurisdiction of the darkness he has just named."
            },
            # --- TIER B: HEBREW/GREEK ANALYSIS ---
            {
                "heading": "The Cup of Wrath",
                "tier": "b",
                "body": "[B] 'Remove this CUP from me.' The cup (pot\u0113rion, "
                        "\u03c0\u03bf\u03c4\u03ae\u03c1\u03b9\u03bf\u03bd) is not a generic metaphor for suffering. In "
                        "the prophets, the cup is THE CUP OF GOD'S WRATH. "
                        "Isaiah 51:17: 'Wake yourself, Jerusalem, you who have "
                        "drunk from the hand of the LORD the cup of his wrath, "
                        "who have drunk to the dregs the bowl, the cup of "
                        "staggering.' Jeremiah 25:15: 'Take from my hand this "
                        "cup of the wine of wrath, and make all the nations "
                        "drink it.' Psalm 75:8: 'In the hand of the LORD there "
                        "is a cup with foaming wine, well mixed, and he pours "
                        "out from it, and all the wicked of the earth shall "
                        "drain it down to the dregs.' Jesus is asking the "
                        "Father to remove THE CUP OF DIVINE WRATH AGAINST ALL "
                        "HUMAN SIN. This is not a man afraid of nails. This "
                        "is the only being who fully comprehends what it means "
                        "to absorb the wrath of an infinite God."
            },
            {
                "heading": "The Name and the Darkness",
                "tier": "b",
                "body": "[B] The Greek ag\u014dnia (\u1f00\u03b3\u03c9\u03bd\u03af\u03b1) in Luke 22:44 is not "
                        "passive suffering. It comes from ag\u014dn \u2014 a contest, "
                        "a struggle against an opponent. Jesus is fighting. "
                        "Against what? He tells us: 'This is your hour, and "
                        "the power (exousia, \u1f10\u03be\u03bf\u03c5\u03c3\u03af\u03b1) of darkness' (Luke "
                        "22:53). Exousia is the word Paul uses for the hostile "
                        "spiritual authorities in Ephesians 6:12: 'against the "
                        "cosmic powers (kosmokratoras) over this present "
                        "darkness, against the spiritual forces of evil in "
                        "the heavenly places.' Jesus names the dark powers "
                        "arrayed against him \u2014 and walks into their teeth. "
                        "The garden's name adds its own testimony: Gat "
                        "Shmanim means 'oil press.' Olives are crushed to "
                        "produce oil. Isaiah 53:5 says the Servant was "
                        "'crushed' (dakka, \u05d3\u05b7\u05bc\u05db\u05bc\u05b8\u05d0) for our iniquities. In a "
                        "garden named for crushing, the Servant is crushed."
            },
            # --- TIER C: FULL PICTURE ---
            {
                "heading": "The Mountain of Departure and Return",
                "tier": "c",
                "body": "[C] The Mount of Olives is not a neutral location. "
                        "Ezekiel 11:23 records that the glory of YHWH 'went "
                        "up from the midst of the city and stood on the "
                        "mountain that is on the east side of the city' \u2014 the "
                        "Mount of Olives. The glory departed from there. "
                        "Zechariah 14:4 prophesies that when YHWH returns for "
                        "the final battle, 'his feet shall stand on the Mount "
                        "of Olives.' The mountain of departure and return. "
                        "Jesus prays at its base on the night that sets the "
                        "return in motion. The angel who strengthens him "
                        "(Luke 22:43) fits the divine council framework: a "
                        "loyal member of the heavenly host sent to sustain "
                        "the incarnate Son at the lowest point of his earthly "
                        "mission. Even in his greatest agony, the council "
                        "does not abandon the Son. The cosmic irony is "
                        "devastating: the 'power of darkness' thinks it is "
                        "closing the trap. In reality, darkness is walking "
                        "into God's trap. 1 Corinthians 2:8 is the verdict: "
                        "'None of the rulers of this age understood this, "
                        "for if they had, they would not have crucified the "
                        "Lord of glory.'"
            }
        ]
    },

    # =========================================================================
    # CHAPTER 7: THE TRIALS — THE CLOUD-RIDER CLAIM
    # =========================================================================
    {
        "id": "passion-night-trials",
        "ref": "Mark 14:53-65, Matt 26:57-68, Luke 22:66-71, Dan 7:13-14, Ps 110:1",
        "chapter_num": 7,
        "title": "The Trials \u2014 The Cloud-Rider Claim",
        "era": "passion_night",
        "type": "chapter",

        "synopsis": "This is the chapter that changes everything. Jesus stands "
                    "before the Sanhedrin in the dead of night. False witnesses "
                    "contradict each other. The case is collapsing. The high priest "
                    "makes one final attempt: 'Are you the Christ, the Son of the "
                    "Blessed?' And Jesus answers with a sentence that detonates "
                    "the courtroom: 'I am, and you will see the Son of Man seated "
                    "at the right hand of Power, and coming with the clouds of "
                    "heaven' (Mark 14:62). The high priest tears his garments. "
                    "'What further witnesses do we need? You have heard his "
                    "blasphemy.' For two thousand years, people have assumed the "
                    "blasphemy was claiming to be the Messiah. It was not. The "
                    "blasphemy was claiming to be the cloud-rider of Daniel 7 \u2014 "
                    "a claim that, in the entire Hebrew Bible and all ancient Near "
                    "Eastern literature, belongs exclusively to God.",

        "key_verse": {
            "ref": "Mark 14:62",
            "text": "And Jesus said, \u201cI am, and you will see the Son of Man "
                    "seated at the right hand of Power, and coming with the "
                    "clouds of heaven.\u201d",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "eg\u014d eimi",
                "greek": "\u1f10\u03b3\u1f7c \u03b5\u1f30\u03bc\u03b9",
                "meaning": "'I am.' The Greek equivalent of the divine name "
                           "revealed at the burning bush: 'I AM WHO I AM' "
                           "(Exodus 3:14, LXX: eg\u014d eimi ho \u014dn). When Jesus "
                           "answers the high priest with ego eimi, he is not "
                           "merely saying 'yes.' He is invoking the Name.",
                "verse": "Mark 14:62"
            },
            {
                "term": "nephel\u0113",
                "greek": "\u03bd\u03b5\u03c6\u03ad\u03bb\u03b7",
                "meaning": "'Cloud.' In the Hebrew Bible and ANE literature, "
                           "cloud-riding is exclusively a divine prerogative. "
                           "YHWH rides clouds (Psalm 68:4, 104:3, Deuteronomy "
                           "33:26). Baal is called 'cloud-rider' in Ugaritic "
                           "texts. No human, no angel, no prophet ever rides "
                           "clouds. Only deities.",
                "verse": "Mark 14:62; Daniel 7:13"
            },
            {
                "term": "dynamis",
                "greek": "\u03b4\u03cd\u03bd\u03b1\u03bc\u03b9\u03c2",
                "meaning": "'Power.' A circumlocution for God himself. 'Seated "
                           "at the right hand of Power' means 'seated at the "
                           "right hand of God' \u2014 the co-regent position from "
                           "Psalm 110:1.",
                "verse": "Mark 14:62"
            },
            {
                "term": "blasph\u0113mia",
                "greek": "\u03b2\u03bb\u03b1\u03c3\u03c6\u03b7\u03bc\u03af\u03b1",
                "meaning": "'Blasphemy.' The high priest's charge. In Jewish "
                           "law, blasphemy was the ultimate offense \u2014 claiming "
                           "divine prerogatives or pronouncing the divine Name. "
                           "The garment-tearing was the prescribed response to "
                           "hearing blasphemy (Mishnah Sanhedrin 7:5).",
                "verse": "Mark 14:64"
            },
            {
                "term": "basileus",
                "greek": "\u03b2\u03b1\u03c3\u03b9\u03bb\u03b5\u03cd\u03c2",
                "meaning": "'King.' The charge before Pilate: 'King of the Jews' "
                           "(basileus t\u014dn Ioudai\u014dn). Pilate does not care about "
                           "theology. He cares about insurrection. The political "
                           "charge is true in a way neither the Sanhedrin nor "
                           "Pilate understands.",
                "verse": "Mark 15:2"
            }
        ],

        "ane_backdrop": "Cloud-riding as a divine attribute is one of the most "
                        "consistent motifs in the ancient Near East. In the Ugaritic "
                        "texts from Ras Shamra (c. 1400-1200 BC), Baal is called "
                        "'rider of the clouds' (rkb \u02bfrpt). The Hebrew Bible takes this "
                        "title and assigns it exclusively to YHWH: 'him who rides "
                        "through the deserts' (Psalm 68:4, using the same Semitic root "
                        "as the Ugaritic Baal epithet). Deuteronomy 33:26: 'There is "
                        "none like God, O Jeshurun, who rides through the heavens.' "
                        "Psalm 104:3: 'He makes the clouds his chariot.' In the entire "
                        "corpus of ANE literature, cloud-riding belongs to deities and "
                        "deities alone. When Jesus claims to come 'with the clouds of "
                        "heaven,' every person in that courtroom with a theological "
                        "education knows exactly what he is saying.",

        "second_temple": [
            {
                "source": "Daniel 7:13-14",
                "summary": "Daniel's vision: 'Behold, with the clouds of heaven there "
                           "came one like a son of man, and he came to the Ancient of "
                           "Days and was presented before him. And to him was given "
                           "dominion and glory and a kingdom, that all peoples, nations, "
                           "and languages should serve him.' This figure receives "
                           "universal authority from YHWH himself.",
                "relevance": "The direct source text for Jesus' claim. The 'one like "
                             "a son of man' rides clouds \u2014 a divine prerogative \u2014 and "
                             "receives worship from all nations. Jesus identifies "
                             "himself as this figure."
            },
            {
                "source": "1 Enoch 46-48 (Similitudes of Enoch)",
                "summary": "According to the Similitudes, the 'Son of Man' is a "
                           "pre-existent figure who sits on the throne of glory and "
                           "judges the kings and mighty ones of the earth. He is "
                           "called 'the Chosen One' and 'the Righteous One.'",
                "relevance": "Demonstrates that BEFORE Jesus, Jewish interpreters "
                             "read Daniel 7:13 as describing a divine or semi-divine "
                             "figure alongside YHWH \u2014 not merely a symbol for Israel."
            },
            {
                "source": "4Q246 ('Son of God' text, Dead Sea Scrolls)",
                "summary": "This Aramaic fragment from Qumran describes a figure "
                           "who will be called 'Son of God' and 'Son of the Most "
                           "High' and whose kingdom will be an everlasting kingdom.",
                "relevance": "Shows that the language the high priest uses \u2014 'Son "
                             "of the Blessed' \u2014 and the concept of a divine-level "
                             "messianic figure were already in play in pre-Christian "
                             "Jewish theology."
            },
            {
                "source": "Mishnah Sanhedrin 7:5 (codified c. 200 AD)",
                "summary": "According to the Mishnah, the prescribed response when "
                           "a judge heard blasphemy was to tear his garments. The "
                           "high priest's garment-tearing at Jesus' words is the "
                           "legally prescribed reaction to heard blasphemy.",
                "relevance": "Confirms that the high priest understood Jesus' claim "
                             "as blasphemy \u2014 not because he claimed to be the Messiah "
                             "(they were expecting one) but because he claimed divine "
                             "prerogatives: the Name, the throne, and the clouds."
            }
        ],

        "cross_refs": [
            {"ref": "Mark 14:53-65", "note": "The trial before the Sanhedrin: 'I am, and you will see the Son of Man coming with the clouds'", "type": "nt"},
            {"ref": "Matthew 26:57-68", "note": "Matthew's account: they spit in his face and strike him", "type": "nt"},
            {"ref": "Luke 22:66-71", "note": "Luke's account: 'If I tell you, you will not believe'", "type": "nt"},
            {"ref": "Daniel 7:13-14", "note": "The Son of Man comes with clouds and receives dominion over all nations", "type": "ot"},
            {"ref": "Psalm 110:1", "note": "'The LORD says to my Lord: Sit at my right hand' \u2014 the co-regent psalm Jesus invokes", "type": "ot"},
            {"ref": "Exodus 3:14", "note": "'I AM WHO I AM' \u2014 the divine name Jesus echoes with ego eimi", "type": "ot"},
            {"ref": "Psalm 68:4", "note": "'Rider in the deserts' \u2014 YHWH as cloud-rider, same Semitic root as Baal's Ugaritic title", "type": "ot"},
            {"ref": "Psalm 104:3", "note": "'He makes the clouds his chariot' \u2014 cloud-riding as divine prerogative", "type": "ot"},
            {"ref": "Deuteronomy 33:26", "note": "'There is none like God, who rides through the heavens'", "type": "ot"},
            {"ref": "1 Corinthians 2:8", "note": "'None of the rulers of this age understood this, for if they had, they would not have crucified the Lord of glory'", "type": "nt"},
            {"ref": "Mark 15:1-5", "note": "The trial before Pilate: 'Are you the King of the Jews?' \u2014 the political translation of a theological claim", "type": "nt"},
            {"ref": "1 Enoch 46-48", "note": "According to the Similitudes, the pre-existent Son of Man sits on the throne of glory", "type": "pseudepigrapha"},
            {"ref": "4Q246 (Dead Sea Scrolls)", "note": "The 'Son of God' text from Qumran: 'He shall be called Son of God and Son of the Most High'", "type": "dss"}
        ],

        "divine_council_note": "The trial before the Sanhedrin is the moment when Jesus "
                               "reveals his identity in divine council terms. He combines "
                               "three Old Testament texts in one sentence: (1) 'I AM' \u2014 "
                               "the divine name from Exodus 3:14. (2) 'Seated at the right "
                               "hand of Power' \u2014 Psalm 110:1, the co-regent position at "
                               "YHWH's right hand. (3) 'Coming with the clouds of heaven' "
                               "\u2014 Daniel 7:13, the cloud-rider who receives authority from "
                               "the Ancient of Days. Cloud-riding is exclusively divine. "
                               "The high priest understands instantly: this man claims to be "
                               "the divine figure from Daniel 7, seated at YHWH's right "
                               "hand, bearing the divine Name. The garment-tearing is not "
                               "theatrical rage. It is the legally prescribed response to "
                               "heard blasphemy. The 'two powers in heaven' tradition shows "
                               "this claim was not unprecedented in Jewish theology \u2014 but "
                               "the rabbis later shut this reading down precisely because "
                               "Christians used it for Jesus.",

        "sections": [
            # --- TIER A: CANON ONLY ---
            {
                "heading": "The Failed Case",
                "tier": "a",
                "body": "[A] They lead Jesus to the high priest. The chief priests "
                        "and the whole council seek testimony against him to put "
                        "him to death, 'but they found none. For many bore false "
                        "witness against him, but their testimony did not agree' "
                        "(Mark 14:55-56, ESV). Some claim he said he would "
                        "destroy the temple and rebuild it in three days, but "
                        "'even about this their testimony did not agree' (14:59). "
                        "The case is failing. They cannot produce two consistent "
                        "witnesses \u2014 the minimum required under Jewish law "
                        "(Deuteronomy 19:15). The high priest stands up and asks "
                        "Jesus directly: 'Have you no answer? What is it that "
                        "these men testify against you?' Jesus is silent. He "
                        "does not defend himself. Isaiah 53:7: 'He was oppressed "
                        "and he was afflicted, yet he opened not his mouth; like "
                        "a lamb that before its shearers is silent.' The Lamb "
                        "does not bleat."
            },
            {
                "heading": "The Question and the Answer",
                "tier": "a",
                "body": "[A] The high priest asks the direct question: 'Are you "
                        "the Christ, the Son of the Blessed?' (Mark 14:61). "
                        "Jesus answers: 'I am, and you will see the Son of Man "
                        "seated at the right hand of Power, and coming with the "
                        "clouds of heaven' (14:62, ESV). The reaction is "
                        "immediate and violent. The high priest tears his "
                        "garments: 'What further witnesses do we need? You have "
                        "heard his blasphemy. What is your decision?' And they "
                        "all condemn him as deserving death (14:63-64). They "
                        "spit on him. They blindfold him and strike him, saying: "
                        "'Prophesy!' The guards receive him with blows (14:65). "
                        "The one who spoke the universe into existence stands "
                        "blindfolded while men hit his face and mock his power. "
                        "Outside, Peter denies him three times before the "
                        "rooster crows \u2014 just as Jesus predicted (14:66-72). "
                        "The night is total."
            },
            # --- TIER B: HEBREW/GREEK ANALYSIS ---
            {
                "heading": "Why the High Priest Tore His Robes",
                "tier": "b",
                "body": "[B] This is the question almost no one asks: WHY was "
                        "it blasphemy? Claiming to be the Messiah was not "
                        "blasphemous \u2014 they were EXPECTING a Messiah. The high "
                        "priest tore his robes because of what Jesus actually "
                        "said. He combined THREE Old Testament texts into one "
                        "sentence. First: 'I AM' \u2014 ego eimi (\u1f10\u03b3\u1f7c \u03b5\u1f30\u03bc\u03b9), echoing "
                        "the divine name from Exodus 3:14 (the LXX: ego eimi "
                        "ho \u014dn). Second: 'seated at the right hand of Power' "
                        "\u2014 Psalm 110:1, the co-regent position at YHWH's right "
                        "hand. 'Power' (dynamis, \u03b4\u03cd\u03bd\u03b1\u03bc\u03b9\u03c2) is a circumlocution "
                        "for God \u2014 Jesus is claiming the seat BESIDE GOD. "
                        "Third: 'coming with the clouds of heaven' \u2014 Daniel "
                        "7:13. CLOUD-RIDING IS EXCLUSIVELY A DIVINE "
                        "PREROGATIVE. In the entire Hebrew Bible and all ANE "
                        "literature, only deities ride clouds. YHWH rides "
                        "clouds (Psalm 68:4, 104:3, Deuteronomy 33:26). No "
                        "human, no angel, no prophet EVER rides clouds. "
                        "Jesus claimed to be the cloud-rider of Daniel 7. "
                        "The high priest understood perfectly."
            },
            {
                "heading": "The Cloud-Rider and the Divine Name",
                "tier": "b",
                "body": "[B] Put the three claims together. Jesus says: I bear "
                        "the divine Name (ego eimi). I sit at God's right "
                        "hand (Psalm 110:1). I ride the clouds (Daniel 7:13). "
                        "This is not a messianic claim. This is a DIVINE claim. "
                        "In the Ugaritic texts from Ras Shamra, Baal is called "
                        "'rider of the clouds' (rkb \u02bfrpt) \u2014 it is his defining "
                        "title. The Hebrew Bible takes that title away from "
                        "Baal and gives it to YHWH alone: 'him who rides "
                        "through the deserts' in Psalm 68:4 uses the same "
                        "Semitic root. Cloud-riding is deity language. Period. "
                        "The high priest's garment-tearing was not emotional "
                        "outrage. It was the legally prescribed response to "
                        "heard blasphemy, codified later in Mishnah Sanhedrin "
                        "7:5. He understood: this man from Nazareth just "
                        "claimed to be GOD \u2014 the divine figure from Daniel 7 "
                        "who receives worship from all nations, seated at "
                        "YHWH's own right hand, bearing the Name that was "
                        "too holy to speak. THAT is the blasphemy."
            },
            # --- TIER C: FULL PICTURE ---
            {
                "heading": "The Two Powers Controversy",
                "tier": "c",
                "body": "[C] Here is what makes Jesus' claim even more "
                        "devastating: it was not unprecedented. Before Jesus, "
                        "multiple Jewish sources read Daniel 7:13 as describing "
                        "a second divine figure alongside YHWH. The Similitudes "
                        "of Enoch (1 Enoch 46-48) describe a pre-existent 'Son "
                        "of Man' who sits on the throne of glory, judges the "
                        "kings of the earth, and is worshiped. 4 Ezra's 'my "
                        "son' figure exercises divine authority. The Qumran "
                        "'Son of God' text (4Q246) describes a figure called "
                        "'Son of God' and 'Son of the Most High' whose kingdom "
                        "is everlasting. This reading \u2014 that Daniel 7:13 "
                        "describes a second divine person receiving authority "
                        "from the Ancient of Days \u2014 was a live option in "
                        "pre-Christian Judaism. By the second century AD, "
                        "the rabbis explicitly rejected it. The 'two powers "
                        "in heaven' became a heresy \u2014 precisely because "
                        "Christians used Daniel 7:13 for Jesus. Rabbi Akiva "
                        "initially entertained the 'two thrones' reading of "
                        "Daniel 7:9 before his colleagues shut it down. "
                        "Jesus' claim was the fulfillment of a trajectory "
                        "the rabbis later tried to close."
            },
            {
                "heading": "Before Pilate \u2014 The Political Translation",
                "tier": "c",
                "body": "[C] The Sanhedrin convicts on blasphemy but cannot "
                        "execute under Roman law. They need Pilate. So the "
                        "charge shifts from theological to political: 'We "
                        "found this man misleading our nation and forbidding "
                        "us to give tribute to Caesar, and saying that he "
                        "himself is Christ, a king' (Luke 23:2). Pilate asks: "
                        "'Are you the King of the Jews?' Jesus answers: 'You "
                        "have said so' (Mark 15:2). The title basileus t\u014dn "
                        "Ioudai\u014dn ('King of the Jews') is the political "
                        "translation of what Jesus claimed in the Sanhedrin. "
                        "Pilate does not care about cloud-riders or Daniel 7 "
                        "\u2014 he cares about insurrection against Rome. The irony "
                        "is total: the charge 'King of the Jews' will be "
                        "nailed to the cross in three languages (John 19:19-20) "
                        "\u2014 and it is the truest thing written that day, in a "
                        "way neither the Sanhedrin that formulated it nor the "
                        "governor who authorized it understands. The rulers of "
                        "this age do not understand what they are doing. They "
                        "never do (1 Corinthians 2:8)."
            }
        ]
    }
]
