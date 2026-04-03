"""
era_catholic_sacraments.py -- Sacraments, Saints & Authority (Chapters 4-6)

Research Lens: Catholicism -- examining Catholic distinctive doctrines against
the biblical text. This era covers the Eucharist (transubstantiation), the
intercession of saints and veneration of relics, and papal infallibility.

Each chapter presents the Catholic case in its strongest form -- drawing from
councils, the Catechism, and the church fathers -- before responding with
Greek, Hebrew, and historical evidence. The goal is not polemic but honest
examination: what does the text actually say?

Three chapters covering:
  4. The Eucharist -- transubstantiation, "This is my body," the four views
  5. Saints, Relics, and Intercession -- veneration vs. worship, Heb 12:1
  6. Papal Infallibility -- Vatican I (1870), ex cathedra, Peter's fallibility

Evidence tiers:
  [A] Direct Scripture -- the text says what it says
  [B] Valid inference -- reasonable conclusions from scriptural data
  [C] Historical parallel -- documented events and patristic testimony

Theological framework: divine council worldview, ESV baseline translation,
formal equivalence preference. Non-canonical and patristic sources are
cited as historical evidence, never as Scripture.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 4: THE EUCHARIST -- TRANSUBSTANTIATION
    # =========================================================================
    {
        "id": "catholic-eucharist",
        "ref": "Matthew 26:26-28; John 6:48-63; 1 Corinthians 11:23-26; Luke 22:19-20",
        "chapter_num": 4,
        "title": "The Eucharist \u2014 Transubstantiation",
        "era": "catholic_sacraments",
        "type": "chapter",

        "synopsis": "When Jesus said 'This is my body,' did He mean that the bread "
                    "literally becomes His flesh? Catholic theology says yes -- the "
                    "Fourth Lateran Council (1215) formally defined transubstantiation "
                    "using Aristotelian categories of substance and accidents. The "
                    "early witness is strong: Ignatius of Antioch (Epistle to the "
                    "Smyrnaeans 7:1, c. 110 AD) called the Eucharist 'the flesh of "
                    "our Savior Jesus Christ,' and Justin Martyr (First Apology 66, "
                    "c. 155 AD) described the bread and wine as 'the flesh and blood "
                    "of that Jesus who was made flesh.' But the Greek of "
                    "John 6:63 complicates the literal reading: 'It is the Spirit "
                    "who gives life; the flesh profits nothing.' Jesus used metaphor "
                    "constantly -- 'I am the door,' 'I am the vine' -- and Paul "
                    "frames the Lord's Supper as memorial proclamation: 'you proclaim "
                    "the Lord's death until He comes' (1 Cor 11:26). The real question "
                    "is whether a 13th-century Aristotelian philosophical framework "
                    "should be imposed on a 1st-century Jewish Passover meal.",

        "key_verse": {
            "ref": "1 Corinthians 11:26",
            "text": "For as often as you eat this bread and drink the cup, you "
                    "proclaim the Lord's death until he comes.",
            "translation": "ESV"
        },

        # NOTE: These are Greek/Latin terms — field name is a known schema limitation
        "hebrew_terms": [
            {
                "term": "\u03c4\u03bf\u1fe6\u03c4\u03cc \u1f10\u03c3\u03c4\u03b9\u03bd \u03c4\u1f78 \u03c3\u1ff6\u03bc\u03ac \u03bc\u03bf\u03c5 (touto estin to soma mou)",
                "meaning": "This is my body. The Catholic case rests heavily on "
                           "estin -- IS, not 'represents' or 'symbolizes.' Greek "
                           "estin (from eimi, 'to be') is the standard copulative "
                           "verb. The argument: Jesus said IS, full stop. This is "
                           "the strongest point in the Catholic arsenal, and it "
                           "deserves honest engagement. However, estin functions "
                           "as a metaphorical copula throughout the NT: 'I am the "
                           "door' (ego eimi he thyra, John 10:9), 'I am the vine' "
                           "(ego eimi he ampelos, John 15:1), 'the seven stars ARE "
                           "the angels' (Rev 1:20). In each case, estin means "
                           "'represents' or 'signifies,' not literal identity. The "
                           "verb itself cannot settle the debate. Context must. [A]"
            },
            {
                "term": "\u1f00\u03bd\u03ac\u03bc\u03bd\u03b7\u03c3\u03b9\u03c2 (anamnesis)",
                "meaning": "Remembrance, memorial, active recollection. From ana "
                           "(again) + mimnesko (to remember). Luke 22:19: 'Do this "
                           "in remembrance (anamnesis) of me.' Paul repeats it in "
                           "1 Corinthians 11:24-25. The word carries rich Passover "
                           "resonance -- the Passover seder is itself an anamnesis, "
                           "a ritual re-presentation of the Exodus. The Passover "
                           "lamb is not literally re-sacrificed at each seder; it "
                           "is memorialized. Jesus, instituting the Supper during "
                           "Passover, is placing His death within this memorial "
                           "framework. Anamnesis is more than bare mental recall -- "
                           "it is participatory commemoration -- but it is NOT the "
                           "same as ontological re-creation of Christ's body. [A]"
            },
            {
                "term": "\u03ba\u03b1\u03c4\u03b1\u03b3\u03b3\u03ad\u03bb\u03bb\u03b5\u03c4\u03b5 (katangellette)",
                "meaning": "You proclaim, you announce publicly. From kata (down, "
                           "intensifier) + angello (to announce). 1 Corinthians "
                           "11:26: 'You proclaim the Lord's death until He comes.' "
                           "Paul defines the Supper's purpose as proclamation -- "
                           "heralding the Lord's death with eschatological hope "
                           "('until He comes'). The verb is communicative, not "
                           "sacrificial. The Supper announces; it does not re-offer "
                           "what was offered once for all (ephapax, Hebrews 7:27). [A]"
            },
            {
                "term": "transsubstantiatio (Latin)",
                "meaning": "Transubstantiation. A Latin theological term formalized "
                           "at the Fourth Lateran Council (1215) and reaffirmed at "
                           "Trent (1551). Built on Aristotelian metaphysics: every "
                           "object has 'substance' (what it truly IS) and 'accidents' "
                           "(what it appears to be -- taste, color, texture). In "
                           "transubstantiation, the substance of bread becomes the "
                           "substance of Christ's body, while the accidents remain "
                           "bread-like. The philosophical framework is Aristotle's "
                           "Categories, transmitted through Boethius and Aquinas. "
                           "The question: should a Greek philosophical distinction "
                           "from the 4th century BC, systematized by a 13th-century "
                           "Dominican friar, define what Jesus meant at a Jewish "
                           "Passover meal in 30 AD? [C]"
            },
            {
                "term": "\u1f10\u03c6\u03ac\u03c0\u03b1\u03be (ephapax)",
                "meaning": "Once for all, once and for all time. Hebrews 7:27, "
                           "9:12, 10:10. The author of Hebrews insists that "
                           "Christ's sacrifice was ephapax -- a single, unrepeatable, "
                           "eternally sufficient offering. Catholic theology holds "
                           "the Mass is not a 're-sacrifice' but a 're-presentation' "
                           "of the one sacrifice. The distinction is subtle but "
                           "important. However, Hebrews 10:12 says Christ 'offered "
                           "for all time a single sacrifice for sins' and then 'sat "
                           "down' -- the seated posture signals completion. A priest "
                           "stands to offer; Christ sits because the offering is "
                           "finished. [A]"
            }
        ],

        "ane_backdrop": "In the ancient Near East, sacred meals were central to "
                        "covenant-making and worship. The Mesopotamian 'meal of the "
                        "gods' (naptanu) placed food before the deity's image; the "
                        "food was consumed by priests as representatives. Egyptian "
                        "temple meals served a similar function -- the offering was "
                        "presented to the god, then 'reverted' to the priests and "
                        "worshippers. In every ANE context, the sacred meal created "
                        "communion between the human and divine realms. Israel's "
                        "Passover meal (Exodus 12) functioned within this pattern "
                        "but with a crucial difference: no food became the deity. "
                        "The lamb was a memorial sacrifice, its blood marking "
                        "deliverance, not divine substance. When Jesus institutes "
                        "the Lord's Supper during Passover, He is working within "
                        "a Jewish memorial framework, not an ANE transformation "
                        "framework. The bread does not become God; it remembers "
                        "what God has done.",

        "second_temple": [
            {
                "source": "Passover Haggadah (Mishnah Pesachim 10)",
                "summary": "The Passover liturgy includes the declaration: 'This "
                           "is the bread of affliction which our fathers ate in "
                           "the land of Egypt.' No participant in the seder "
                           "understood this to mean the matzah literally became "
                           "the bread eaten in Egypt. It was anamnesis -- "
                           "participatory remembrance.",
                "relevance": "Jesus used identical Passover meal language ('This is "
                             "my body') within a Jewish ritual context where 'this "
                             "is' was universally understood as memorial identification, "
                             "not ontological transformation. His disciples, all Jews "
                             "reared on Passover, would have heard 'This is my body' "
                             "as they heard 'This is the bread of affliction' -- as "
                             "covenantal memorial, not metaphysical change."
            },
            {
                "source": "Philo, On the Special Laws 2.148-149",
                "summary": "Philo of Alexandria interprets the Passover as primarily "
                           "a 'crossing over' (pascha from diabasis) -- a memorial "
                           "of divine deliverance. The physical elements point beyond "
                           "themselves to spiritual realities.",
                "relevance": "Alexandrian Jewish interpretation contemporary with the "
                             "NT consistently read Passover elements symbolically -- "
                             "the bread and wine signified theological truths without "
                             "becoming something ontologically different. This is the "
                             "interpretive world in which Jesus and Paul operated."
            },
            {
                "source": "Didache 9-10 (c. 50-120 AD)",
                "summary": "The earliest Christian liturgical text outside the NT "
                           "provides prayers for the Eucharist that focus on "
                           "thanksgiving, unity, and eschatological gathering -- "
                           "'Maranatha' (Our Lord, come!) -- without any language "
                           "of substance change.",
                "relevance": "The Didache, likely contemporary with some NT writings, "
                             "treats the Eucharist as a meal of thanksgiving and "
                             "eschatological hope. The absence of transformation "
                             "language in the earliest liturgy suggests the doctrine "
                             "developed later, not that it was always there."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 26:26-28", "note": "'This is my body... this is my blood of the covenant' -- the institution narrative. Catholic strongest proof text. The question is whether estin ('is') functions literally or as metaphorical identification, as it does throughout Jesus' 'I am' statements [A]", "type": "nt"},
            {"ref": "John 6:48-58", "note": "'Whoever feeds on my flesh and drinks my blood has eternal life' -- Catholic case for real presence. Note: many disciples left after this (6:66), suggesting shocking literalism. But v. 63 provides the interpretive key [A]", "type": "nt"},
            {"ref": "John 6:63", "note": "'It is the Spirit who gives life; the flesh profits nothing. The words that I have spoken to you are spirit and life' -- Jesus' own interpretive gloss on the 'eat my flesh' discourse. The flesh-eating language is spiritual, not material [A]", "type": "nt"},
            {"ref": "1 Corinthians 11:23-26", "note": "Paul's account of the Lord's Supper: 'Do this in remembrance (anamnesis) of me... you proclaim the Lord's death until He comes.' Memorial + eschatological hope -- not sacrifice + substance change [A]", "type": "nt"},
            {"ref": "Hebrews 7:27", "note": "Christ 'does not need daily, like those high priests, to offer sacrifices... He did this once for all (ephapax)' -- the single, unrepeatable sacrifice directly challenges any re-offering in the Mass [A]", "type": "nt"},
            {"ref": "Hebrews 10:10-12", "note": "'We have been sanctified through the offering of the body of Jesus Christ once for all... He sat down at the right hand of God' -- the seated posture signals finished sacrifice. Priests stand to offer; Christ sits because it is done [A]", "type": "nt"},
            {"ref": "John 10:9", "note": "'I am the door' -- Jesus uses estin metaphorically. He is not a literal door. Same verb, same construction as 'This is my body' [A]", "type": "nt"},
            {"ref": "John 15:1", "note": "'I am the true vine' -- another metaphorical use of eimi/estin. Pattern: Jesus consistently uses 'I am' language figuratively to communicate spiritual reality [A]", "type": "nt"},
            {"ref": "Exodus 12:1-14", "note": "The Passover institution: the lamb is sacrificed, the blood applied, the meal eaten. The annual Passover is memorial re-enactment, not literal re-creation of the original event -- the pattern Jesus fulfills [A]", "type": "ot"},
            {"ref": "Luke 22:19-20", "note": "'Do this in remembrance of me... This cup that is poured out for you is the new covenant in my blood' -- 'the new covenant IN my blood,' not 'this cup IS my blood.' The cup represents the covenant, sealed by blood already shed [A]", "type": "nt"},
            {"ref": "Matthew 26:28", "note": "Matthew 26:28 and Mark 14:24 use stronger language -- 'this IS my blood of the covenant.' The Catholic case is strongest here. The biblical response: the 'is' (estin) functions identically to 'I am the door' (John 10:9) and 'I am the vine' (John 15:1) -- metaphorical identification, not ontological transformation. The question is whether estin demands literal or figurative reading, and Jesus' own clarification in John 6:63 ('the flesh profits nothing') tips the balance [A]", "type": "nt"}
        ],

        "divine_council_note": "In the divine council framework, YHWH alone possesses "
                               "the power to create, transform, and sustain being. The "
                               "council members -- even the highest -- do not share "
                               "this creative ontological authority. The claim that a "
                               "human priest, by speaking words of institution, causes "
                               "the substance of bread to become the literal body of "
                               "Christ places an extraordinary creative power in human "
                               "hands. In the biblical pattern, God acts; humans "
                               "receive. The Passover lamb was not transformed into "
                               "YHWH by priestly words -- it was received as a memorial "
                               "of what YHWH had already done. The Lord's Supper "
                               "follows this pattern: we proclaim what Christ has "
                               "accomplished, we do not re-create His sacrifice.",

        "sections": [
            {
                "heading": "The Catholic Case: Strongest Form",
                "body": "'This is my body' -- touto estin to soma mou. Jesus said IS. "
                        "Not 'represents,' not 'symbolizes,' not 'reminds you of.' "
                        "IS. [A] That is the starting point, and it deserves honest "
                        "weight. Catholic theology argues that the plain meaning of "
                        "Jesus' words demands real, substantial presence. John 6 "
                        "intensifies the claim: 'Unless you eat the flesh of the "
                        "Son of Man and drink His blood, you have no life in you' "
                        "(6:53). The Greek verb shifts from phago (to eat) to trogo "
                        "(to gnaw, to munch) in verse 54 -- Jesus escalates, not "
                        "retreats, into physical language. When disciples grumble, "
                        "He does not soften it. Many leave (6:66), and He lets them "
                        "go. The early witness supports the Catholic reading. "
                        "Ignatius of Antioch (c. 110 AD) wrote in his Epistle "
                        "to the Smyrnaeans 7:1 that certain heretics 'abstain "
                        "from the Eucharist and prayer, because they do not "
                        "confess that the Eucharist is the flesh of our Savior "
                        "Jesus Christ.' [C] Justin Martyr (c. 155 AD) wrote in "
                        "his First Apology 66: 'The food which has been made the "
                        "Eucharist is the flesh and blood of that Jesus who was "
                        "made flesh.' [C] These are not late medieval additions -- "
                        "they are first- and second-century voices. The Catholic "
                        "argument is not without weight."
            },
            {
                "heading": "John 6:63 -- The Verse Catholics Must Address",
                "body": "After the most intense 'eat my flesh' discourse in all of "
                        "Scripture (John 6:48-58), Jesus provides His own "
                        "interpretive key: 'It is the Spirit who gives life; the "
                        "flesh (sarx) profits nothing. The words that I have spoken "
                        "to you are spirit and life' (6:63). [A] This verse is the "
                        "most significant challenge to a strictly literal reading "
                        "of the flesh-eating language. Jesus explicitly contrasts "
                        "sarx (flesh, physical matter) with pneuma (Spirit, the "
                        "life-giving reality). He says His words are spirit and "
                        "life -- meaning the discourse is operating on a spiritual "
                        "plane, not a material one. The flesh, taken literally, "
                        "'profits nothing.' Catholic interpreters argue that 6:63 "
                        "refers to merely human understanding ('the flesh' as "
                        "fleshly thinking), not to Christ's flesh in the Eucharist. "
                        "This is a possible reading, but it requires importing a "
                        "distinction Jesus does not make. In the immediate context, "
                        "'the flesh profits nothing' most naturally reads as Jesus' "
                        "clarification that the flesh-eating language is spiritual "
                        "metaphor -- the same pattern He uses with 'living water' "
                        "(John 4:10-14) and 'bread from heaven' (John 6:32-35), "
                        "where physical imagery conveys spiritual reality. [B]"
            },
            {
                "heading": "Aristotle in the Upper Room",
                "body": "The doctrine of transubstantiation was formally defined "
                        "at the Fourth Lateran Council (1215) and refined at the "
                        "Council of Trent (1551). [C] The philosophical engine is "
                        "Aristotelian: every object possesses 'substance' (what it "
                        "truly IS -- its essence) and 'accidents' (what it appears "
                        "to be -- color, taste, texture, weight). In "
                        "transubstantiation, at the words of consecration, the "
                        "substance of bread becomes the substance of Christ's body "
                        "while the accidents remain unchanged. You see bread, taste "
                        "bread, measure bread -- but it is no longer bread. Thomas "
                        "Aquinas (1225-1274) gave this doctrine its definitive "
                        "philosophical articulation in the Summa Theologiae (III, "
                        "qq. 73-78), drawing on Aristotle's Metaphysics. The "
                        "historical problem: Aristotelian metaphysics was not "
                        "available to the first-century church. It entered Western "
                        "theology through Boethius (6th century), the Arab "
                        "philosophers (11th-12th century), and reached its Christian "
                        "synthesis in Aquinas. The apostles at the Last Supper had "
                        "no category of 'substance versus accidents.' They had "
                        "Passover. They had anamnesis. They had covenant meal. "
                        "Imposing a 13th-century Aristotelian grid on a 1st-century "
                        "Jewish meal is a philosophical choice, not a biblical "
                        "requirement. [C]"
            },
            {
                "heading": "The Four Views -- Honest Comparison",
                "body": "Christians have held at least four major positions on the "
                        "Lord's Supper. Catholic (transubstantiation): the bread "
                        "and wine literally become Christ's body and blood in "
                        "substance, retaining only the appearances of bread and "
                        "wine. Lutheran (real presence / 'in, with, and under'): "
                        "Christ is truly, really present in the elements, but the "
                        "bread remains bread -- Lutherans rejected Aristotelian "
                        "substance metaphysics while affirming real presence. "
                        "Reformed (spiritual presence): Christ is truly present "
                        "in the Supper, but spiritually, not physically -- the "
                        "Spirit lifts the believer to Christ rather than bringing "
                        "Christ down into the bread. Calvin called the Supper a "
                        "'spiritual banquet.' Memorial (Zwingli): the Supper is "
                        "primarily an act of remembrance and proclamation -- 'do "
                        "this in remembrance of me' -- the elements represent, "
                        "they do not become or contain. [C] Each position has "
                        "biblical warrant. The Catholic view takes 'This is my "
                        "body' at maximum literalness. The memorial view takes "
                        "'do this in remembrance' and 'the flesh profits nothing' "
                        "at maximum weight. The Reformed position attempts to honor "
                        "both: real spiritual presence without Aristotelian metaphysics. "
                        "What is clear: Paul defines the Supper's function as "
                        "proclamation with eschatological hope -- 'you proclaim "
                        "the Lord's death until He comes' (1 Cor 11:26). [A] "
                        "The Supper points backward to the cross and forward to "
                        "the return. It is covenantal, communal, and anticipatory."
            },
            {
                "heading": "Once for All -- Hebrews and the Finished Sacrifice",
                "body": "The book of Hebrews builds an extended argument that "
                        "Christ's sacrifice is ephapax -- once for all, never to "
                        "be repeated. 'He has no need, like those high priests, to "
                        "offer sacrifices daily... He did this once for all when He "
                        "offered up Himself' (7:27). 'We have been sanctified "
                        "through the offering of the body of Jesus Christ once for "
                        "all' (10:10). Then the decisive image: 'When Christ had "
                        "offered for all time a single sacrifice for sins, He sat "
                        "down at the right hand of God' (10:12). [A] In the "
                        "Levitical system, the priest never sat down -- there were "
                        "no chairs in the tabernacle because the work was never "
                        "finished. Christ sits because His offering is complete. "
                        "Catholic theology insists the Mass is not a 're-sacrifice' "
                        "but a 're-presentation' -- making present again the one "
                        "sacrifice of Calvary. The distinction is carefully drawn "
                        "in the Catechism (CCC 1366-1367). But Hebrews does not "
                        "envision even a 're-presentation.' The sacrifice is "
                        "finished. The priest is seated. The veil is torn. Access "
                        "is direct. The Lord's Supper proclaims what was "
                        "accomplished; it does not re-present what needs no "
                        "presenting again. [B]"
            }
        ]
    },

    # =========================================================================
    # CHAPTER 5: SAINTS, RELICS, AND INTERCESSION
    # =========================================================================
    {
        "id": "catholic-saints-intercession",
        "ref": "Hebrews 4:16; 1 Timothy 2:5; Hebrews 12:1; Revelation 5:8; Deuteronomy 18:10-12",
        "chapter_num": 5,
        "title": "Saints, Relics, and Intercession",
        "era": "catholic_sacraments",
        "type": "chapter",

        "synopsis": "If the saints are alive in Christ and aware of earthly events, "
                    "does it make sense to ask them to intercede? Catholic theology "
                    "distinguishes veneration (dulia) from worship (latria) and "
                    "points to the 'great cloud of witnesses' (Hebrews 12:1) and "
                    "the prayers of the saints in Revelation 5:8 and 8:3-4. The "
                    "early church honored its martyrs from the second century "
                    "onward, and the practice has deep roots. But the biblical "
                    "response is equally clear: Hebrews 4:16 invites believers to "
                    "'draw near to the throne of grace' directly, 1 Timothy 2:5 "
                    "names 'one mediator between God and men,' and Deuteronomy "
                    "18:10-12 forbids consulting the dead. The historical "
                    "development tells a story: early commemoration of martyrs "
                    "gradually absorbed Greco-Roman hero cult and ancestor "
                    "veneration patterns, becoming something the apostolic church "
                    "would not have recognized.",

        "key_verse": {
            "ref": "Hebrews 4:16",
            "text": "Let us then with confidence draw near to the throne of "
                    "grace, that we may receive mercy and find grace to help "
                    "in time of need.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u03b4\u03bf\u03c5\u03bb\u03af\u03b1 / \u03bb\u03b1\u03c4\u03c1\u03b5\u03af\u03b1 (doulia / latreia)",
                "meaning": "Veneration/service vs. worship. Catholic theology "
                           "distinguishes latria (\u03bb\u03b1\u03c4\u03c1\u03b5\u03af\u03b1, worship -- due to "
                           "God alone) from doulia (\u03b4\u03bf\u03c5\u03bb\u03af\u03b1, veneration -- "
                           "given to saints). Hyperdulia (special veneration) is "
                           "reserved for Mary. Note: douleia (\u03b4\u03bf\u03c5\u03bb\u03b5\u03af\u03b1) means "
                           "bondage/slavery (Romans 8:21) -- a different word from "
                           "doulia (\u03b4\u03bf\u03c5\u03bb\u03af\u03b1), the Catholic theological term for "
                           "veneration/service. The distinction is real in Greek, "
                           "though critics argue the practical difference is often "
                           "invisible to ordinary believers. When they kneel before "
                           "statues, light candles, and petition the dead for help, "
                           "the line between honoring and worshipping blurs. [B]"
            },
            {
                "term": "\u03bc\u03b5\u03c3\u03af\u03c4\u03b7\u03c2 (mesites)",
                "meaning": "Mediator, go-between, one who stands in the middle. "
                           "1 Timothy 2:5: 'There is one God, and there is one "
                           "mediator (mesites) between God and men, the man Christ "
                           "Jesus.' The word is singular and emphatic: heis mesites "
                           "-- ONE mediator. Catholic theology responds that asking "
                           "saints to pray is no different from asking a living "
                           "friend to pray -- it does not violate Christ's unique "
                           "mediation. The counter-question: where does the NT "
                           "instruct believers to ask the dead to pray for them? "
                           "The practice of asking living believers to pray is "
                           "biblical (James 5:16). The practice of petitioning "
                           "the dead to pray has no NT precedent. [A]"
            },
            {
                "term": "\u03bd\u03ad\u03ba\u03c5\u03c2 / \u03b4\u03c1\u03ac\u03c9 (nekros / drao) \u2014 consulting the dead",
                "meaning": "Deuteronomy 18:10-12 (LXX) forbids one who 'inquires "
                           "of the dead' (eperotao tous nekrous). The Hebrew "
                           "original uses doresh el ha-metim -- 'one who seeks the "
                           "dead.' Catholic theology argues that asking a saint to "
                           "intercede is not 'consulting the dead' in the sense of "
                           "necromancy (divination). The distinction has some merit: "
                           "necromancy seeks hidden knowledge from the dead; "
                           "intercession asks the dead to pray to God. But the "
                           "underlying principle stands: the living are not "
                           "instructed to direct communication to the dead. "
                           "Hebrews directs all prayer traffic to the throne of "
                           "grace through Christ, not through the departed. [A]"
            },
            {
                "term": "\u03c0\u03b1\u03c1\u03c1\u03b7\u03c3\u03af\u03b1 (parrhesia)",
                "meaning": "Boldness, confidence, freedom of speech. Hebrews "
                           "4:16: 'Let us draw near with confidence (parrhesia).' "
                           "Also Hebrews 10:19: 'We have confidence (parrhesia) to "
                           "enter the holy places by the blood of Jesus.' The word "
                           "describes the freedom of a citizen to speak openly in "
                           "the assembly. Every believer has parrhesia -- direct, "
                           "unmediated, bold access to the throne of God through "
                           "Christ's blood. No saint, no priest, no intermediary "
                           "is needed. The veil is torn (Matthew 27:51). Access "
                           "is open. [A]"
            },
            {
                "term": "\u03bd\u03ad\u03c6\u03bf\u03c2 \u03bc\u03b1\u03c1\u03c4\u03cd\u03c1\u03c9\u03bd (nephos martyron)",
                "meaning": "Cloud of witnesses. Hebrews 12:1: 'Since we are "
                           "surrounded by so great a cloud of witnesses (nephos "
                           "martyron).' Catholic theology reads this as the saints "
                           "actively watching and participating in the lives of "
                           "believers. But martyron here means 'witnesses' in the "
                           "sense of testimony-givers, not spectators. The heroes "
                           "of Hebrews 11 are witnesses TO FAITH -- their lives "
                           "testify to faithfulness. The metaphor is courtroom or "
                           "athletic: they have run their race, and their example "
                           "surrounds us. The text does not say they hear our "
                           "prayers or intercede for us. It says their testimony "
                           "encourages us to run. [B]"
            }
        ],

        "ane_backdrop": "The ancient Near East was saturated with ancestor veneration "
                        "and hero cult. Mesopotamian cultures maintained the kispu "
                        "ritual -- regular offerings of food and drink to the dead "
                        "to sustain them in the underworld and gain their benevolent "
                        "influence. The Greek hero cult venerated exceptional "
                        "mortals -- warriors, founders, benefactors -- at their "
                        "tombs, offering libations and prayers in exchange for "
                        "protection and favor. Roman ancestor worship (cultus "
                        "maiorum) honored the household dead and sought their "
                        "ongoing patronage. Israel was explicitly forbidden from "
                        "these practices: 'There shall not be found among you "
                        "anyone who... inquires of the dead' (Deuteronomy 18:11). "
                        "The early church emerged into a Greco-Roman world where "
                        "honoring the dead at their tombs was normal religion. The "
                        "transition from commemorating martyrs to venerating saints "
                        "and seeking their intercession followed cultural patterns "
                        "that Scripture had specifically prohibited in Israel.",

        "second_temple": [
            {
                "source": "2 Maccabees 15:12-16 (Deuterocanonical)",
                "summary": "Judas Maccabeus has a vision of the deceased high priest "
                           "Onias and the prophet Jeremiah interceding for Israel. "
                           "Jeremiah 'stretched out his right hand and gave to Judas "
                           "a golden sword.' Catholic theology cites this as "
                           "scriptural evidence for the intercession of the dead.",
                "relevance": "This is the Catholic strongest proof text for saintly "
                             "intercession. It comes from the deuterocanonical books "
                             "(Protestants: Apocrypha). The passage describes a "
                             "dream/vision, not a normative teaching. Even within "
                             "Catholic canon, the literary genre (apocalyptic "
                             "vision) should temper how much doctrinal weight the "
                             "passage bears. 2 Maccabees never instructs readers "
                             "to pray to the dead; it reports a vision."
            },
            {
                "source": "Testament of Abraham (1st-2nd century AD)",
                "summary": "Abraham is shown the judgment of souls and intercedes "
                           "for the living before God. The righteous dead are "
                           "portrayed as having awareness of and influence on "
                           "earthly affairs.",
                "relevance": "Second Temple literature occasionally portrays the "
                             "righteous dead as having heavenly awareness, but "
                             "these texts are pseudepigraphal -- they tell us what "
                             "some Jews imagined, not what Scripture teaches. The "
                             "canonical Hebrew Bible consistently directs prayer "
                             "to YHWH alone: 'You shall worship the Lord your God "
                             "and him only shall you serve' (Deut 6:13, quoted by "
                             "Jesus in Matthew 4:10)."
            },
            {
                "source": "Tobit 12:12 (Deuterocanonical)",
                "summary": "The angel Raphael tells Tobit: 'When you and Sarah "
                           "prayed, it was I who brought your prayer before the "
                           "Holy One.' Angels present human prayers to God.",
                "relevance": "Revelation 5:8 and 8:3-4 also depict heavenly beings "
                             "presenting prayers before God's throne. But the "
                             "direction is crucial: human prayers go UP to God "
                             "through angelic presentation. The saints and angels "
                             "are carriers, not recipients. Catholic practice "
                             "inverts this by directing prayers TO saints, asking "
                             "them to petition God -- a direction of prayer the "
                             "biblical texts never model."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 4:16", "note": "'Let us draw near with confidence to the throne of grace' -- direct access to God through Christ. No saint, no intermediary, no go-between needed. The 'us' is every believer [A]", "type": "nt"},
            {"ref": "1 Timothy 2:5", "note": "'One mediator between God and men, the man Christ Jesus' -- heis mesites, emphatically singular. Every additional mediating layer diminishes this exclusivity [A]", "type": "nt"},
            {"ref": "Hebrews 12:1", "note": "'Great cloud of witnesses' -- witnesses in the sense of testimony-givers (Heb 11 heroes), not heavenly spectators hearing prayers. The text encourages us by their example, not their intercession [B]", "type": "nt"},
            {"ref": "Revelation 5:8", "note": "Elders hold 'golden bowls full of incense, which are the prayers of the saints.' Catholic proof text for heavenly intercession. But the saints here are praying TO God (the Lamb), and the bowls PRESENT prayers -- the text does not instruct us to direct prayers to the elders [B]", "type": "nt"},
            {"ref": "Revelation 8:3-4", "note": "An angel offers incense 'with the prayers of all the saints' before God. Again, prayers go UP to God. The angel is a courier, not a recipient. No human is instructed to pray to the angel [B]", "type": "nt"},
            {"ref": "Deuteronomy 18:10-12", "note": "'There shall not be found among you... anyone who inquires of the dead.' The Hebrew doresh el ha-metim -- seeking the dead -- is explicitly forbidden. Whether for divination or intercession, directing communication to the dead is outside the biblical pattern [A]", "type": "ot"},
            {"ref": "Matthew 27:51", "note": "'The curtain of the temple was torn in two, from top to bottom' -- God Himself removes the barrier. Access to the Holy of Holies is now direct for every believer. Adding intermediaries re-erects what God tore down [A]", "type": "nt"},
            {"ref": "Hebrews 10:19-22", "note": "'We have confidence to enter the holy places by the blood of Jesus... let us draw near' -- the entire argument of Hebrews is that Christ's priesthood makes all other priestly mediation obsolete [A]", "type": "nt"},
            {"ref": "James 5:16", "note": "'Pray for one another' -- the NT pattern for intercessory prayer is among the LIVING. The command is mutual, horizontal, and among those present. It is not directed to the dead [A]", "type": "nt"},
            {"ref": "Philippians 1:23", "note": "Paul's desire to 'depart and be with Christ' -- Catholic proof text that the dead are alive and conscious with Christ. Valid point: the righteous dead are with Christ. But being with Christ does not mean they hear or mediate earthly prayers [B]", "type": "nt"}
        ],

        "divine_council_note": "The divine council model is directly relevant here. In "
                               "the heavenly court, there are indeed beings who serve "
                               "before God's throne -- the seraphim of Isaiah 6, the "
                               "24 elders of Revelation, the angelic hosts. Revelation "
                               "5:8 and 8:3-4 show heavenly figures handling the prayers "
                               "of the saints. But the consistent pattern is critical: "
                               "all worship, all petition, all prayer goes to God. The "
                               "council members serve; they do not receive worship or "
                               "direct petition. When John falls before an angel in "
                               "Revelation 22:8-9, the angel immediately says: 'You "
                               "must not do that! Worship God.' The divine council "
                               "framework actually undermines saint intercession: if "
                               "even angels refuse to receive directed honor, how much "
                               "less should deceased humans receive it?",

        "sections": [
            {
                "heading": "The Catholic Case: Strongest Form",
                "body": "Catholic theology makes a careful, layered argument for the "
                        "intercession of saints. First, the saints are alive -- Paul "
                        "desires to 'depart and be with Christ' (Phil 1:23), and "
                        "the God of Abraham is 'not God of the dead, but of the "
                        "living' (Mark 12:27). [A] Second, the saints are aware: "
                        "Hebrews 12:1 describes a 'great cloud of witnesses' "
                        "surrounding the living church. Revelation 6:9-10 shows "
                        "martyrs under the altar who cry out, 'How long, Sovereign "
                        "Lord?' -- they are conscious and concerned about earthly "
                        "events. [A] Third, the saints intercede: Revelation 5:8 "
                        "shows elders holding bowls of incense 'which are the "
                        "prayers of the saints,' and Revelation 8:3-4 shows an "
                        "angel offering incense with the prayers of all the saints "
                        "before God's throne. [B] Fourth, asking others to pray is "
                        "biblical: 'Pray for one another' (James 5:16). If we ask "
                        "living friends to pray, why not the saints who are more "
                        "alive in Christ than we are? The distinction between "
                        "veneration (dulia) and worship (latria) ensures that honor "
                        "given to saints does not cross into idolatry. This argument "
                        "is coherent and has 1,500 years of theological development "
                        "behind it."
            },
            {
                "heading": "Direct Access -- The Veil Is Torn",
                "body": "The entire argument of Hebrews is that Christ's priesthood "
                        "makes all other mediating structures obsolete. 'We have "
                        "confidence (parrhesia) to enter the holy places by the "
                        "blood of Jesus, by the new and living way that He opened "
                        "for us through the curtain' (Hebrews 10:19-20). [A] The "
                        "curtain is torn (Matthew 27:51). The barrier between the "
                        "worshipper and God's presence is removed. 'Let us draw "
                        "near with confidence to the throne of grace' (4:16). [A] "
                        "The 'us' is not priests, not saints, not a special class "
                        "-- it is every believer. First Timothy 2:5 is equally "
                        "direct: 'There is one God, and there is one mediator "
                        "(mesites) between God and men, the man Christ Jesus.' [A] "
                        "One mediator. Not one primary mediator with secondary "
                        "mediators assisting. Heis -- one. The biblical model of "
                        "prayer is radically simple: any believer, at any time, "
                        "through Christ alone, directly to the Father. 'When you "
                        "pray, go into your room and shut the door and pray to "
                        "your Father who is in secret' (Matthew 6:6). [A] Adding "
                        "saintly intermediaries does not enhance this access -- "
                        "it undermines the sufficiency of what Christ's blood "
                        "accomplished. If the veil is torn, why build new curtains?"
            },
            {
                "heading": "The Historical Development: From Martyrs to Mediators",
                "body": "The development from honoring martyrs to petitioning saints "
                        "spans roughly 300 years and follows a traceable arc. [C] "
                        "Phase one (2nd century): the early church commemorated its "
                        "martyrs at their tombs on the anniversary of their death "
                        "(their 'heavenly birthday'). The Martyrdom of Polycarp "
                        "(c. 155 AD) distinguishes clearly: 'We worship Christ as "
                        "the Son of God, but the martyrs we love as disciples and "
                        "imitators of the Lord.' Commemoration, not petition. Phase "
                        "two (3rd-4th century): veneration of relics intensified. "
                        "Bones, clothing, and objects associated with martyrs were "
                        "collected, enshrined, and believed to carry spiritual "
                        "power. The parallel to pagan relic culture is unmistakable "
                        "-- Roman families preserved the genius (spirit) of ancestors "
                        "through relics and household shrines. Phase three (5th "
                        "century onward): formal intercession theology developed. "
                        "Augustine wrote cautiously about praying 'at' the memorials "
                        "of martyrs (not 'to' them initially), but the practice "
                        "expanded rapidly as the Roman Empire's conversion brought "
                        "millions of former pagans into the church -- carrying their "
                        "patron-client religious instincts with them. The saint "
                        "replaced the household deity. The relic replaced the "
                        "ancestor shrine. The patron saint replaced the local "
                        "protector spirit. [C]"
            },
            {
                "heading": "Dulia vs. Latria -- Can the Line Hold?",
                "body": "The Catholic distinction between dulia (veneration) and "
                        "latria (worship) is theologically precise on paper. Latria "
                        "belongs to God alone. Dulia is the honor given to saints. "
                        "Hyperdulia is the special honor reserved for Mary. In "
                        "theological treatises, the categories are clean. [C] In "
                        "practice, the line has not held. Popular Catholic piety "
                        "throughout history has included: kneeling before statues of "
                        "saints, lighting candles to saints, praying novenas (nine "
                        "days of sustained petition) to saints, wearing medals of "
                        "saints for protection, attributing miraculous powers to "
                        "saints' relics and images, and making pilgrimages to saints' "
                        "shrines to receive healings and blessings. The behavioral "
                        "pattern is indistinguishable from what the pagans did at "
                        "the shrines of their heroes and household gods. The Catholic "
                        "Catechism (CCC 2132) acknowledges the need for careful "
                        "instruction to prevent the honor from becoming worship. "
                        "But the very need for that instruction proves the danger "
                        "is real, persistent, and not merely theoretical. When a "
                        "grandmother in Mexico kneels before a statue of the "
                        "Virgin, lights a candle, weeps, and begs for healing -- "
                        "the theological distinction between dulia and latria is "
                        "not operative in her heart. [B]"
            },
            {
                "heading": "Deuteronomy 18 -- The Prohibition",
                "body": "The Torah is explicit: 'There shall not be found among you "
                        "anyone who burns his son or his daughter as an offering, "
                        "anyone who practices divination or tells fortunes or "
                        "interprets omens, or a sorcerer or a charmer or a medium "
                        "or a necromancer or one who inquires of the dead' "
                        "(Deuteronomy 18:10-11). [A] The Hebrew doresh el ha-metim "
                        "-- 'one who seeks the dead' -- covers any practice of "
                        "directing communication to deceased persons. Catholic "
                        "theology distinguishes necromancy (seeking hidden knowledge "
                        "from the dead) from intercession (asking the dead to pray "
                        "to God). The distinction has some logical force -- but "
                        "the Deuteronomy text draws the prohibition broadly. The "
                        "issue is not the KIND of communication but the DIRECTION: "
                        "toward the dead. When Saul consulted Samuel's shade at "
                        "Endor (1 Samuel 28), the text treats it as a grave sin "
                        "regardless of Saul's motive. The principle: the living "
                        "are to direct their words to the living God, not to the "
                        "departed. The New Testament continues this trajectory: "
                        "every prayer instruction in the NT is directed to the "
                        "Father through the Son in the Spirit. Not once does any "
                        "apostle instruct believers to pray to a deceased saint. "
                        "The silence is deafening. Catholics counter with Luke "
                        "20:38 -- 'He is not God of the dead but of the living, "
                        "for all live to him.' If the saints are alive to God, "
                        "asking for their prayers is not necromancy but "
                        "communication within the body of Christ. The biblical "
                        "response: being alive to God does not establish a "
                        "communication channel -- Hebrews 4:16 still directs "
                        "prayer to God through Christ, not through intermediate "
                        "saints. [A]"
            }
        ]
    },

    # =========================================================================
    # CHAPTER 6: PAPAL INFALLIBILITY (1870)
    # =========================================================================
    {
        "id": "catholic-papal-infallibility",
        "ref": "Matthew 16:23; Luke 22:54-62; Galatians 2:11; Acts 15:13-21; Ephesians 2:20",
        "chapter_num": 6,
        "title": "Papal Infallibility (1870)",
        "era": "catholic_sacraments",
        "type": "chapter",

        "synopsis": "Papal infallibility is narrower than most people think. Vatican I "
                    "(Pastor Aeternus, 1870) declared that the pope is infallible "
                    "ONLY when speaking ex cathedra (from the chair of Peter), on "
                    "matters of faith and morals, with the explicit intention of "
                    "binding the whole ekklesia. It has been formally invoked only "
                    "twice: the Immaculate Conception (1854, retroactively covered) "
                    "and the Assumption of Mary (1950). The political context is "
                    "revealing -- Vatican I was held during Italian unification, as "
                    "the Papal States were being conquered. Temporal power was ending, "
                    "so spiritual power was elevated. The biblical response is "
                    "devastating: Peter himself was fallible in the extreme -- "
                    "rebuked by Jesus ('Get behind me, Satan'), denied Christ three "
                    "times, and was publicly corrected by Paul. James, not Peter, "
                    "led the Jerusalem Council. And the ekklesia was built on 'the "
                    "apostles and prophets' (plural), with Christ alone as "
                    "cornerstone.",

        "key_verse": {
            "ref": "Galatians 2:11",
            "text": "But when Cephas came to Antioch, I opposed him to his face, "
                    "because he stood condemned.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "ex cathedra (Latin)",
                "meaning": "From the chair. The technical term for papal infallible "
                           "pronouncements. Cathedra (chair, seat of authority) gives "
                           "us 'cathedral' -- the church where the bishop's chair "
                           "sits. The doctrine claims that when the pope speaks from "
                           "this seat of authority, on defined matters of faith and "
                           "morals, intending to bind the whole church, the Holy "
                           "Spirit preserves him from error. The claim is carefully "
                           "limited: it does not mean the pope is sinless (impeccable) "
                           "or always right. It means that under these specific "
                           "conditions, his doctrinal definitions are protected from "
                           "error. The question: where does Scripture grant any human "
                           "being this charism? [C]"
            },
            {
                "term": "\u1f10\u03ba\u03ba\u03bb\u03b7\u03c3\u03af\u03b1 (ekklesia)",
                "meaning": "Assembly, governing body of called-out ones. NOT an "
                           "institutional hierarchy with a single human head. The "
                           "Greek ekklesia was the citizen assembly, where decisions "
                           "were made collectively. The LXX uses ekklesia to translate "
                           "Hebrew qahal -- the covenant assembly of Israel gathered "
                           "before YHWH. When Jesus says 'I will build my ekklesia' "
                           "(Matthew 16:18), He is not describing a monarchy. He is "
                           "describing an assembly under His own direct headship "
                           "(Ephesians 1:22, Colossians 1:18). Papal infallibility "
                           "effectively places one man as the definitive voice of the "
                           "ekklesia -- but the ekklesia answers to Christ, not to "
                           "any earthly vicar. [B]"
            },
            {
                "term": "\u03b8\u03b5\u03bc\u03ad\u03bb\u03b9\u03bf\u03c2 (themelios)",
                "meaning": "Foundation. Ephesians 2:20: the ekklesia is 'built on the "
                           "foundation (themelios) of the apostles and prophets, "
                           "Christ Jesus himself being the cornerstone.' Two things: "
                           "the foundation is PLURAL -- apostles and prophets, not "
                           "one man. And the cornerstone is Christ, not Peter. The "
                           "architectural metaphor distributes authority across the "
                           "apostolic witness and locates the structural center in "
                           "Christ alone. A building with one cornerstone and one "
                           "infallible human foundation stone has two competing "
                           "structural centers. [A]"
            },
            {
                "term": "\u1f51\u03c0\u03ac\u03b3\u03b5 \u1f40\u03c0\u03af\u03c3\u03c9 \u03bc\u03bf\u03c5, \u03a3\u03b1\u03c4\u03b1\u03bd\u1fb6 (hypage opiso mou, Satana)",
                "meaning": "'Get behind me, Satan!' -- Jesus' rebuke to Peter in "
                           "Matthew 16:23, immediately after the 'rock' declaration "
                           "in 16:18. Jesus identifies Peter as speaking for the "
                           "adversary (Satanas) because Peter opposes the divine "
                           "plan of the cross. The same man declared 'blessed' in "
                           "v. 17 is called 'Satan' in v. 23. If papal infallibility "
                           "were operative, this sequence is inexplicable. Peter is "
                           "not merely mistaken -- he is rebuked as a mouthpiece of "
                           "the enemy. Five verses after the 'rock,' the rock "
                           "stumbles catastrophically. [A]"
            },
            {
                "term": "\u03ba\u03b1\u03c4\u03b5\u03b3\u03bd\u03c9\u03c3\u03bc\u03ad\u03bd\u03bf\u03c2 (kategnōsmenos)",
                "meaning": "Stood condemned, was clearly wrong, was self-condemned. "
                           "Galatians 2:11: Paul opposed Cephas 'because he stood "
                           "condemned (kategnōsmenos).' The perfect passive participle "
                           "indicates Peter's guilt was already established -- his "
                           "actions had condemned him before Paul even spoke. Peter "
                           "withdrew from eating with Gentiles under pressure from "
                           "the circumcision party, contradicting the gospel of grace. "
                           "Paul's public rebuke of the 'first pope' on a matter of "
                           "faith and practice is the single most embarrassing text "
                           "for papal infallibility. [A]"
            },
            {
                "term": "\u03ba\u03c1\u03af\u03bd\u03c9 (krino)",
                "meaning": "I judge, I decide, I render a verdict. Acts 15:19: James "
                           "says 'Therefore my judgment (krino) is that we should not "
                           "trouble the Gentiles.' At the Jerusalem Council -- the "
                           "first and most important doctrinal council of the church "
                           "-- it is James who delivers the authoritative verdict, "
                           "not Peter. Peter speaks (vv. 7-11), but James decides "
                           "(v. 19) and the decree goes out under his formulation "
                           "(vv. 20-21). If Peter held papal primacy, James' role is "
                           "inexplicable. [A]"
            }
        ],

        "ane_backdrop": "In the ancient Near East, the concept of a single human "
                        "figure wielding infallible religious authority was alien to "
                        "Israel's structure. Israel's governance was distributed: "
                        "prophets spoke for YHWH, priests administered the cult, "
                        "kings ruled civilly, and elders judged locally. No single "
                        "office combined all authority. When kings attempted to "
                        "seize priestly prerogatives (Uzziah in 2 Chronicles "
                        "26:16-21), they were struck down. When priests attempted "
                        "prophetic authority, they were corrected (Amaziah vs. Amos "
                        "in Amos 7:10-17). The concentration of religious authority "
                        "in a single figure follows the pattern of Mesopotamian "
                        "priest-kings and Egyptian pharaohs, not the pattern of "
                        "Israel. The divine council model -- where YHWH presides "
                        "over a plurality of subordinate authorities (Psalm 82, "
                        "1 Kings 22) -- is inherently anti-monarchical in its "
                        "ecclesiology. Authority is distributed under one supreme "
                        "head: YHWH, not any human being.",

        "second_temple": [
            {
                "source": "Qumran Community Rule (1QS 5-6)",
                "summary": "The Dead Sea community was governed by a council of "
                           "twelve men and three priests, with collective decision-"
                           "making. The 'Teacher of Righteousness' held high "
                           "authority but was not infallible -- his interpretations "
                           "could be tested against the Torah.",
                "relevance": "The most rigorous Jewish community contemporary with "
                             "Jesus operated on collective authority, not papal "
                             "monarchy. Even their most revered leader was "
                             "subordinate to the text. The apostolic church inherited "
                             "this pattern: collective authority (the Twelve, the "
                             "elders, the council) under the authority of Scripture "
                             "and the Spirit."
            },
            {
                "source": "Josephus, Antiquities 20.197-203",
                "summary": "Josephus describes the succession and authority of the "
                           "high priests in Second Temple Judaism. High priests held "
                           "enormous authority, but none was considered infallible. "
                           "They could be removed, replaced, and were frequently "
                           "corrupt -- Josephus documents their failings freely.",
                "relevance": "Even the highest religious office in Judaism -- the high "
                             "priesthood -- never carried a charism of infallibility. "
                             "The high priest could err, and history shows that many "
                             "did, catastrophically. Caiaphas, the reigning high "
                             "priest, condemned Jesus to death. The office did not "
                             "guarantee truth."
            },
            {
                "source": "Mishnah Sanhedrin 1:6",
                "summary": "The Great Sanhedrin of 71 members decided matters of "
                           "law through majority vote. Dissenting opinions were "
                           "recorded. No single member held veto or infallible "
                           "authority.",
                "relevance": "The highest Jewish judicial body operated on collective "
                             "deliberation and majority decision, with recorded "
                             "dissent. This is the governance model the apostles "
                             "knew. The Jerusalem Council of Acts 15 follows this "
                             "pattern: discussion, testimony, collective judgment -- "
                             "not papal decree."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 16:23", "note": "'Get behind me, Satan!' -- Jesus rebukes Peter as a mouthpiece of the adversary, five verses after 'on this rock.' If Peter held infallible teaching authority, this rebuke is inexplicable [A]", "type": "nt"},
            {"ref": "Luke 22:54-62", "note": "Peter denies Jesus three times. Not a minor lapse -- a public, repeated, oath-accompanied denial of Christ under pressure. The 'first pope' failed the most basic test of faithfulness [A]", "type": "nt"},
            {"ref": "Galatians 2:11-14", "note": "Paul opposes Peter 'to his face because he stood condemned' on a matter of faith and practice (table fellowship with Gentiles). The 'first pope' publicly corrected by an apostle [A]", "type": "nt"},
            {"ref": "Acts 15:13-21", "note": "James, not Peter, delivers the authoritative judgment at the Jerusalem Council: 'my judgment is...' The decree follows James' formulation. If papal primacy existed, James' leadership role makes no sense [A]", "type": "nt"},
            {"ref": "Ephesians 2:20", "note": "'Built on the foundation of the apostles and prophets' -- PLURAL. 'Christ Jesus himself being the cornerstone' -- singular. Authority is distributed across the apostolic witness with Christ alone as structural center [A]", "type": "nt"},
            {"ref": "Colossians 1:18", "note": "'He is the head of the body, the church' -- Christ is the head. Not the pope, not Peter, not any vicar. The headship language is exclusive to Christ in the NT [A]", "type": "nt"},
            {"ref": "1 Peter 5:1-3", "note": "Peter calls himself 'fellow elder' (sympresbyteros) and warns against 'domineering over those in your charge.' His self-understanding directly contradicts papal monarchy [A]", "type": "nt"},
            {"ref": "Acts 8:14", "note": "'The apostles at Jerusalem sent Peter and John to Samaria' -- Peter is SENT BY the apostolic body. A strange dynamic if he is their supreme head [A]", "type": "nt"},
            {"ref": "Acts 11:1-18", "note": "Peter must defend his visit to Cornelius before 'the apostles and the brothers.' He is called to account by his peers -- impossible if he held supreme jurisdiction [A]", "type": "nt"},
            {"ref": "2 Chronicles 26:16-21", "note": "King Uzziah enters the temple to burn incense -- seizing priestly prerogatives -- and is struck with leprosy. The principle: no single office concentrates all religious authority. God enforces the distribution [A]", "type": "ot"}
        ],

        "divine_council_note": "The divine council framework is the strongest argument "
                               "against papal infallibility. In the heavenly court, "
                               "YHWH alone presides with supreme, unchallengeable "
                               "authority (Psalm 82:1, 1 Kings 22:19-23). The council "
                               "members -- even the highest -- are subordinate, "
                               "accountable, and capable of error (Psalm 82:2-7). "
                               "Authority flows from the top down; no council member "
                               "can claim infallible teaching authority independent "
                               "of YHWH's word. The earthly ekklesia mirrors this "
                               "pattern: Christ is the head (Ephesians 1:22), the "
                               "apostles are the foundation (Ephesians 2:20, plural), "
                               "and every leader is accountable to the community and "
                               "to Scripture. Placing one man in a seat of infallible "
                               "authority replicates the error of the fallen elohim "
                               "in Psalm 82 -- claiming a prerogative that belongs to "
                               "God alone. The council model distributes authority "
                               "under one supreme head. Papal infallibility "
                               "concentrates it in a human being.",

        "sections": [
            {
                "heading": "What Infallibility Actually Claims",
                "body": "The doctrine is narrower than its critics -- and many of its "
                        "adherents -- realize. Vatican I (Pastor Aeternus, July 18, "
                        "1870) defined: the Roman Pontiff, when he speaks ex cathedra "
                        "(from the chair of Peter) -- that is, when in the exercise "
                        "of his office as shepherd and teacher of all Christians, "
                        "by virtue of his supreme apostolic authority, he defines "
                        "a doctrine concerning faith or morals to be held by the "
                        "whole Church -- possesses, by the divine assistance "
                        "promised to him in blessed Peter, that infallibility which "
                        "the divine Redeemer willed His Church to enjoy in defining "
                        "doctrine. [C] Four conditions must all be met: (1) speaking "
                        "as pope, not as private theologian; (2) defining a doctrine "
                        "of faith or morals; (3) intending to bind the entire church; "
                        "(4) invoking the full weight of apostolic authority. Has it "
                        "been formally invoked? Only twice: the Immaculate Conception "
                        "of Mary (Pius IX, 1854 -- retroactively covered by the 1870 "
                        "definition) and the Assumption of Mary (Pius XII, 1950). The "
                        "rarity of invocation is itself significant -- the church has "
                        "managed for 2,000 years with infallibility formally deployed "
                        "on exactly two occasions, both concerning Mariology."
            },
            {
                "heading": "The Political Context: Why 1870?",
                "body": "Timing matters. Vatican I convened on December 8, 1869, "
                        "during the final phase of Italian unification (the "
                        "Risorgimento). Piedmont-Sardinia had been conquering the "
                        "Italian peninsula for a decade. The Papal States -- the "
                        "pope's temporal domain since the 8th century -- were being "
                        "swallowed. Rome itself would fall on September 20, 1870, "
                        "just two months after the infallibility definition. [C] "
                        "As temporal power collapsed, spiritual power was elevated. "
                        "The pope was losing his army, his territory, and his "
                        "political sovereignty. Infallibility compensated: what was "
                        "lost in earthly authority was gained in spiritual authority. "
                        "This does not mean the doctrine was invented cynically -- "
                        "the theological roots go back centuries. But the timing is "
                        "not coincidental. The council was cut short by the Franco-"
                        "Prussian War and the fall of Rome. Many bishops with "
                        "reservations about infallibility left before the final "
                        "vote. The minority opposition (including many of the most "
                        "distinguished theologians) was effectively silenced by "
                        "events rather than persuaded by arguments. The doctrine "
                        "passed 533 to 2, but the vote count obscures the real "
                        "theological debate. [C]"
            },
            {
                "heading": "Peter's Fallibility -- The Biblical Record",
                "body": "If papal infallibility is grounded in Peter's unique role, "
                        "the New Testament portrait of Peter is profoundly "
                        "inconvenient. In Matthew 16:23 -- five verses after the "
                        "'rock' declaration -- Jesus says to Peter: 'Get behind me, "
                        "Satan! You are a hindrance (skandalon) to me. For you are "
                        "not setting your mind on the things of God, but on the "
                        "things of man.' [A] Peter is not merely wrong; he is "
                        "identified as Satan's mouthpiece. In Luke 22:54-62, Peter "
                        "denies Jesus three times -- the last with an oath. This "
                        "is not a minor lapse; it is a public, repeated denial of "
                        "Christ under pressure. [A] In Galatians 2:11-14, Paul "
                        "writes: 'When Cephas came to Antioch, I opposed him to "
                        "his face, because he stood condemned (kategnōsmenos).' "
                        "Peter withdrew from eating with Gentile believers under "
                        "pressure from the circumcision party -- a direct betrayal "
                        "of the gospel of grace. Paul corrected him publicly. [A] "
                        "Catholic theology responds that infallibility does not "
                        "mean impeccability (sinlessness) or personal inerrancy in "
                        "every statement. Fair enough. But the pattern is striking: "
                        "the man claimed as the first infallible pope was rebuked "
                        "as Satan, denied Christ, and 'stood condemned' on a matter "
                        "of faith and practice. The charism was not evident in Peter."
            },
            {
                "heading": "James, Not Peter, Led the Jerusalem Council",
                "body": "Acts 15 records the Jerusalem Council -- the first and most "
                        "important doctrinal council of the church, addressing "
                        "whether Gentile converts must keep the Mosaic law. Peter "
                        "speaks (vv. 7-11), giving important testimony about his "
                        "experience with Cornelius. Paul and Barnabas share their "
                        "missionary experiences (v. 12). But it is James who "
                        "delivers the authoritative judgment: 'Therefore my judgment "
                        "(ego krino) is that we should not trouble those of the "
                        "Gentiles who turn to God' (v. 19). [A] The verb krino -- "
                        "'I judge, I decide' -- carries judicial weight. James "
                        "renders the verdict. The decree that goes out follows "
                        "James' formulation (vv. 20-21, 28-29). If Peter held papal "
                        "primacy and supreme teaching authority, why does James -- "
                        "not Peter -- deliver the binding decision? Why does the "
                        "council letter not reference Peter's authority? Catholic "
                        "scholars argue that Peter laid the theological groundwork "
                        "and James merely summarized. But the text gives the "
                        "decisive verb (krino) and the decisive formulation to "
                        "James. Luke, writing under inspiration, chose to present "
                        "James as the one who decided. If Peter's primacy were the "
                        "operative reality, Luke's presentation is misleading. [A]"
            },
            {
                "heading": "The Apostolic Pattern: Plural Foundation",
                "body": "The New Testament consistently describes apostolic authority "
                        "as collective, not monarchical. Ephesians 2:20: 'built on "
                        "the foundation of the apostles and prophets, Christ Jesus "
                        "Himself being the cornerstone.' [A] The foundation is plural "
                        "-- apostles AND prophets. The cornerstone is singular -- "
                        "Christ alone. No single apostle holds the structural center. "
                        "Colossians 1:18: 'He is the head of the body, the church.' "
                        "[A] Christ is the head. The Greek kephale (head) is applied "
                        "to Christ, never to Peter, never to any bishop, in the "
                        "entire New Testament. Revelation 21:14: the wall of the "
                        "New Jerusalem has 'twelve foundations, and on them were the "
                        "twelve names of the twelve apostles of the Lamb.' [A] "
                        "Twelve foundations. Not one foundation with eleven "
                        "subordinates. Peter is named among the twelve, but the "
                        "eschatological vision gives him no special structural "
                        "prominence. First Peter 5:1-3 provides Peter's own self-"
                        "understanding: 'fellow elder' (sympresbyteros), not supreme "
                        "pontiff. He warns against 'domineering over those in your "
                        "charge.' [A] The Greek katakyrieuo (to lord it over) is "
                        "the same word Jesus used in Mark 10:42: 'Those who are "
                        "considered rulers of the Gentiles lord it over them.' The "
                        "pattern is clear: authority in the ekklesia is distributed, "
                        "accountable, and subordinate to Christ alone."
            }
        ]
    }
]
