"""
era_matt_sermon.py -- The Sermon on the Mount Deep Dive (Matthew 5-7)

The most important discourse in human history deserves granular study.
Jesus ascends "the mountain" -- evoking Moses on Sinai -- and delivers
the charter of the kingdom of heaven. The Beatitudes redefine blessedness,
the antitheses radicalize Torah, the Lord's Prayer encodes divine council
theology, and the two builders demand a response. Every verse carries
weight that rewards close reading with original language analysis.
"""

CHAPTERS = [
    {
        "id": "matt-beatitudes",
        "ref": "Matthew 5:1-16",
        "chapter_num": 1,
        "title": "The Beatitudes and the Light of the World",
        "era": "matt_sermon",
        "type": "study",
        "themes": ["DC", "TYPE", "HOLY", "KING", "SPIRIT"],

        "synopsis": "Jesus ascends the mountain and sits -- the posture of a king on his throne and a "
                    "rabbi teaching with authority. The eight Beatitudes (makarioi, 5:3-12) describe not "
                    "moral achievements but the surprising recipients of God's kingdom. 'Blessed are the "
                    "poor in spirit' (ptochoi to pneumati) -- those who know their spiritual bankruptcy -- "
                    "'for theirs IS the kingdom of heaven' (present tense: the kingdom belongs to them now). "
                    "The mourners will be comforted (paraklethesontai, from parakaleo -- the same root as "
                    "parakletos, the title Jesus will give the Holy Spirit in John 14-16). The meek (praeis "
                    "-- not weak but disciplined, like a warhorse under rein) inherit the earth (quoting "
                    "Psalm 37:11). Those who hunger and thirst for righteousness will be 'filled' "
                    "(chortasthesontai -- the same verb used for feeding the 5,000 and 4,000). The merciful "
                    "receive mercy (the lex talionis reversed). The pure in heart 'see God' (opsontai ton "
                    "theon) -- a vision previously reserved for Moses, Isaiah, and Ezekiel. The peacemakers "
                    "are called 'sons of God' (huioi theou) -- a divine council title: they share the "
                    "family identity of the Most High. Jesus then defines his community's mission: 'You "
                    "are the salt of the earth' (5:13) and 'the light of the world' (5:14). A city set on "
                    "a hill cannot be hidden. The kingdom community is not a private club but a public "
                    "witness before the nations.",

        "key_verse": {
            "ref": "Matthew 5:3",
            "text": "Blessed are the poor in spirit, for theirs is the kingdom of heaven.",
            "translation": "ESV"
        },

        "original_terms": [
            "makarioi (blessed -- from makar; equivalent to Hebrew ashre in Psalm 1:1; not emotional happiness but divine favor, the state of flourishing under God's rule)",
            "ptochoi to pneumati (poor in spirit -- ptochos means 'beggar-poor,' totally dependent; spiritual poverty = knowing one's desperate need for God)",
            "praeis (meek/gentle -- from praus; a controlled strength, like a trained war horse; LXX of Psalm 37:11 uses this word for Hebrew anawim, the humble faithful)",
            "huioi theou (sons of God -- bene elohim; a divine council title applied to peacemakers; those who make peace share the Father's nature and identity)",
            "halas (salt -- preservative and covenant symbol; 'salt of the covenant' in Lev 2:13; Num 18:19; a community that loses its saltiness loses its covenant identity)",
            "phos tou kosmou (light of the world -- Israel was called to be 'a light to the nations' (Isa 42:6, 49:6); Jesus transfers this Servant mandate to his followers)"
        ],

        "ane_backdrop": "The Beatitudes invert conventional ancient values. In Greco-Roman culture, the 'blessed' "
                        "(makarios) were the gods and the wealthy -- those beyond suffering. Jesus declares the "
                        "opposite: the destitute, grieving, and persecuted are blessed. This inversion parallels "
                        "the Egyptian Instruction literature's occasional recognition that the humble prosper "
                        "(Instruction of Amenemope), but goes further: blessedness is not eventual prosperity but "
                        "present participation in God's kingdom. The 'city on a hill' (5:14) evokes both Jerusalem "
                        "(Psalm 48:2, 'Mount Zion... the city of the great King') and the ANE concept of the cosmic "
                        "mountain where the gods dwell. The community itself becomes the sacred mountain -- the "
                        "dwelling place of God's presence among humanity.",

        "second_temple": [
            {
                "source": "4Q525 (4QBeatitudes)",
                "summary": "A fragmentary Qumran text containing beatitudes: 'Blessed is he who speaks truth "
                           "with a pure heart and does not slander with his tongue.' The form predates Jesus.",
                "relevance": "Shows that the beatitude literary form was alive in Second Temple Judaism. "
                             "Jesus transforms a wisdom genre into a kingdom manifesto."
            },
            {
                "source": "Sirach 25:7-11",
                "summary": "A list of nine beatitudes: 'Happy is the one who lives with a sensible wife... "
                           "happy the one who finds a friend.' Conventional wisdom blessings.",
                "relevance": "Contrasts sharply with Jesus' beatitudes. Sirach blesses the comfortable; "
                             "Jesus blesses the broken. The kingdom inverts earthly categories."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 37:11", "note": "'The meek shall inherit the land' -- Jesus quotes this directly in the third beatitude", "type": "ot"},
            {"ref": "Isaiah 61:1-3", "note": "Good news to the poor, comfort for mourners -- Jesus' beatitudes echo the Isaianic Servant's mission", "type": "ot"},
            {"ref": "Isaiah 42:6", "note": "'I will make you as a light for the nations' -- the Servant's mission transferred to Jesus' disciples as 'light of the world'", "type": "ot"},
            {"ref": "Psalm 24:3-4", "note": "'Who shall ascend the hill of the LORD?... He who has clean hands and a pure heart' -- background for 'blessed are the pure in heart'", "type": "ot"},
            {"ref": "Luke 6:20-26", "note": "Luke's parallel: 'Blessed are you who are poor' (not 'poor in spirit') plus four woes against the rich", "type": "nt"},
            {"ref": "Revelation 21:4", "note": "'He will wipe away every tear' -- the ultimate fulfillment of 'blessed are those who mourn, for they shall be comforted'", "type": "nt"}
        ],

        "divine_council_note": "The Beatitudes are a divine council manifesto. 'Sons of God' (huioi theou, 5:9) "
                               "is the title of the divine council members in the OT (Job 1:6, 2:1; Psalm 29:1; "
                               "82:6). Jesus applies this title to human peacemakers -- those who embody the Father's "
                               "character participate in his family identity. The 'light of the world' language "
                               "(5:14) echoes Isaiah's Servant Songs, where the Servant is 'a light for the nations' "
                               "(42:6, 49:6). The community of Jesus becomes the visible representation of YHWH's "
                               "rule on earth -- the outpost of the heavenly council's authority in the domain of "
                               "the hostile powers.",

        "sections": [
            {
                "heading": "The Eight Beatitudes: Kingdom Citizens (5:3-12)",
                "body": "The Beatitudes follow a careful literary structure. The first and eighth share the same "
                        "reward ('theirs is the kingdom of heaven,' 5:3, 10), forming an inclusio. The first "
                        "four describe conditions of need (poverty, grief, meekness, hunger); the second four "
                        "describe qualities of character (mercy, purity, peacemaking, endurance). Together they "
                        "portray a community that is simultaneously broken and beautiful. The verb 'blessed' "
                        "(makarioi) is plural -- this is corporate, not individual. The kingdom belongs to a "
                        "people, not isolated saints. The final beatitude breaks the pattern with second-person "
                        "direct address: 'Blessed are YOU when others revile you and persecute you' (5:11) -- "
                        "Jesus speaks directly to his disciples, making the beatitudes personal."
            },
            {
                "heading": "Salt and Light: The Community's Mission (5:13-16)",
                "body": "Salt preserves, purifies, and flavors. In the ancient world, salt was also a covenant "
                        "symbol: 'the salt of the covenant' (Leviticus 2:13; Numbers 18:19; 2 Chronicles 13:5). "
                        "A community that loses its covenant identity is 'no longer good for anything except to "
                        "be thrown out and trampled under people's feet' (5:13). Light exposes and reveals. A "
                        "city on a hill -- unmistakable and unavoidable. 'Let your light shine before others, "
                        "so that they may see your good works and give glory to your Father who is in heaven' "
                        "(5:16). The mission is public witness that leads to the glorification of God."
            }
        ]
    },

    {
        "id": "matt-antitheses",
        "ref": "Matthew 5:17-48",
        "chapter_num": 2,
        "title": "The Six Antitheses: I Say to You",
        "era": "matt_sermon",
        "type": "study",
        "themes": ["TYPE", "DC", "LAW", "COV", "WOMEN"],

        "synopsis": "Jesus first establishes his relationship to Torah: 'Do not think that I have come to "
                    "abolish the Law or the Prophets; I have not come to abolish them but to fulfill (plerosai) "
                    "them' (5:17). Not one iota or dot will pass away until all is accomplished (5:18). Then six "
                    "antitheses demonstrate what 'fulfillment' means in practice. Each follows the formula: 'You "
                    "have heard that it was said (errethei)... but I say to you (ego de lego hymin).' The pattern "
                    "is unprecedented: no rabbi claimed authority to reinterpret Torah on his own authority. The "
                    "antitheses move from the sixth commandment (murder → anger, 5:21-26) through the seventh "
                    "(adultery → lust, 5:27-30) to divorce (5:31-32), oaths (5:33-37), retaliation (5:38-42), "
                    "and finally enemy-love (5:43-48). The trajectory is clear: from external compliance to "
                    "internal transformation, from minimum obligation to maximum love. The climax is staggering: "
                    "'You therefore must be perfect (teleioi), as your heavenly Father is perfect (teleios)' "
                    "(5:48). The divine standard is not human achievement but divine character.",

        "key_verse": {
            "ref": "Matthew 5:44-45",
            "text": "But I say to you, Love your enemies and pray for those who persecute you, so that you may be sons of your Father who is in heaven. For he makes his sun rise on the evil and on the good, and sends rain on the just and on the unjust.",
            "translation": "ESV"
        },

        "original_terms": [
            "pleroo (to fulfill -- not to replace but to fill up to its fullest meaning; Jesus reveals what Torah was always pointing toward)",
            "ego de lego hymin (but I say to you -- the unprecedented formula of authority; no scribe says 'I say' but rather 'Rabbi X said'; Jesus speaks on his own divine authority)",
            "raka (Aramaic: empty one, worthless -- a contemptuous dismissal of someone's value; Jesus equates verbal dehumanization with murder)",
            "porneia (sexual immorality -- the exception clause in 5:32; broader than adultery, encompassing the range of sexual violations in Lev 18)",
            "antistenai to ponero (resist the evil one -- 5:39; the verb means 'stand against in battle'; Jesus forbids violent resistance, not passive acceptance of injustice)",
            "teleios (perfect/complete -- from telos, 'end/goal'; not sinless perfection but wholeness, maturity, reaching the intended goal of covenant faithfulness)"
        ],

        "ane_backdrop": "The antitheses have no parallel in rabbinic literature. The closest analogy is Moses "
                        "receiving Torah directly from God on Sinai. Jesus' formula 'I say to you' implies an "
                        "authority that equals or surpasses the original Lawgiver. In rabbinic tradition, "
                        "interpretation was always attributed to earlier authorities (halakhic chain of tradition). "
                        "Jesus breaks this chain entirely -- he speaks as one with direct, unmediated authority. "
                        "The command to love enemies (5:44) contrasts with the ethos of the ancient world, where "
                        "honor demanded retaliation. The Greco-Roman world celebrated virtues of courage in "
                        "battle and just revenge. The Qumran community explicitly commanded love of 'sons of "
                        "light' and hatred of 'sons of darkness' (1QS 1:9-10). Jesus' ethic transcends both.",

        "second_temple": [
            {
                "source": "1QS 1:9-10 (Community Rule)",
                "summary": "'To love all the sons of light... and to hate all the sons of darkness.' The "
                           "Qumran ethic of love within the community and hostility toward outsiders.",
                "relevance": "Direct foil to Jesus' command to love enemies. Even the most devout Jewish "
                             "community of the period did not reach the ethical standard Jesus demands."
            },
            {
                "source": "Letter of Aristeas 207",
                "summary": "Asks 'What is the teaching of wisdom?' Answer: 'As you wish that no evil should "
                           "befall you, but to be a partaker of all good things, so you should act on the "
                           "same principle towards your subjects.' A precursor to the Golden Rule.",
                "relevance": "Shows that reciprocal ethics existed in Hellenistic Judaism, but Jesus goes beyond "
                             "reciprocity to unilateral love of enemies."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 20:13-17", "note": "The Decalogue commands -- murder, adultery, false witness -- that Jesus intensifies from action to intention", "type": "ot"},
            {"ref": "Deuteronomy 24:1-4", "note": "Moses' divorce provision that Jesus restricts: Moses 'permitted' divorce due to hardness of heart (Matt 19:8)", "type": "ot"},
            {"ref": "Leviticus 19:18", "note": "'Love your neighbor as yourself' -- Jesus extends this beyond 'neighbor' to include enemies", "type": "ot"},
            {"ref": "Romans 12:17-21", "note": "'Do not repay anyone evil for evil... overcome evil with good' -- Paul's application of Jesus' anti-retaliation ethic", "type": "nt"},
            {"ref": "1 Peter 3:9", "note": "'Do not repay evil for evil or reviling for reviling, but on the contrary, bless' -- Peter echoes the Sermon's enemy-love", "type": "nt"}
        ],

        "divine_council_note": "Jesus' authority in the antitheses raises the question: who has the right to "
                               "reinterpret the Torah that YHWH himself gave to Moses? Only YHWH himself -- or one "
                               "who shares YHWH's authority. The formula 'I say to you' (ego de lego hymin) is an "
                               "implicit divine claim. Moses received Torah from God; Jesus delivers Torah as God. "
                               "This is consistent with the two-powers-in-heaven theology: the visible YHWH figure "
                               "(the Angel of YHWH, the Word, the Son) who spoke Torah on Sinai now speaks it again "
                               "on this new mountain, not through a mediator but directly. The climactic command "
                               "'Be perfect as your Father is perfect' (5:48) is a call to imitate the divine "
                               "character -- to live as true 'sons of God' who reflect their Father's nature.",

        "sections": [
            {
                "heading": "Murder, Anger, and Reconciliation (5:21-26)",
                "body": "The first antithesis escalates the sixth commandment from the act of murder to "
                        "the heart of anger. 'Everyone who is angry with his brother will be liable to "
                        "judgment' (5:22). Three escalating insults and their consequences: anger = judgment "
                        "(krisis), 'Raka' (Aramaic: worthless) = the council (synedrion), 'fool' (moros) = "
                        "the gehenna of fire. The practical application is radical: if you are offering your "
                        "gift at the altar and remember that your brother has something against you, 'leave "
                        "your gift there before the altar and go. First be reconciled to your brother' "
                        "(5:24). Reconciliation takes priority over worship. God refuses offerings from an "
                        "unreconciled heart."
            },
            {
                "heading": "Adultery, Lust, and Radical Surgery (5:27-30)",
                "body": "'Everyone who looks at a woman with lustful intent (pros to epithymesai) has already "
                        "committed adultery with her in his heart' (5:28). The verb epithymeo is the LXX "
                        "word for 'covet' in the tenth commandment (Exodus 20:17). Jesus connects the seventh "
                        "and tenth commandments: coveting IS the root of adultery. The remedy is hyperbolic "
                        "but makes a real point: 'If your right eye causes you to sin, tear it out' (5:29). "
                        "Better to lose a member than lose the whole person to gehenna. The language is not "
                        "literal self-mutilation but radical moral surgery -- cutting off whatever leads to sin."
            },
            {
                "heading": "Retaliation Refused, Enemies Loved (5:38-48)",
                "body": "'You have heard that it was said, \"An eye for an eye and a tooth for a tooth.\" But "
                        "I say to you, Do not resist the one who is evil (me antistenai to ponero)' (5:38-39). "
                        "The lex talionis (Exodus 21:24) was originally a limit on revenge -- no more than "
                        "proportional justice. Jesus goes further: no retaliation at all. Turn the cheek, give "
                        "the cloak, walk the extra mile. Then the climax: 'Love your enemies and pray for "
                        "those who persecute you' (5:44). The reason is theological, not sentimental: 'so that "
                        "you may be sons (huioi) of your Father who is in heaven' (5:45). God's love is "
                        "indiscriminate -- sun and rain on good and evil alike. The standard is not human "
                        "reciprocity but divine generosity. 'Be perfect (teleioi) as your Father is perfect' "
                        "(5:48). Luke's parallel has 'Be merciful (oiktirmones)' (Luke 6:36) -- mercy and "
                        "perfection are two faces of the same divine character."
            }
        ]
    },

    {
        "id": "matt-prayer-trust",
        "ref": "Matthew 6:1-34",
        "chapter_num": 3,
        "title": "The Lord's Prayer, Fasting, and the Father's Provision",
        "era": "matt_sermon",
        "type": "study",
        "themes": ["DC", "HOLY", "PROV", "KING", "REBEL"],

        "synopsis": "Chapter 6 moves from external ethics to internal devotion. Jesus addresses three pillars "
                    "of Jewish piety -- giving (tsedaqah), prayer (tefillah), and fasting (tsom) -- and "
                    "transforms each from public performance into hidden communion with the Father. The central "
                    "section is the Lord's Prayer (6:9-13), the most prayed text in human history and a "
                    "theological masterpiece in 57 Greek words. Each petition encodes divine council theology: "
                    "'Our Father in heaven' addresses the Most High, enthroned above the heavenly assembly. "
                    "'Hallowed be your name' declares YHWH's supremacy over all spiritual powers. 'Your kingdom "
                    "come, your will be done on earth as it is in heaven' prays for the heavenly council's rule "
                    "to extend to the earthly realm. 'Give us this day our daily bread' (ton arton ton epiousion "
                    "-- a word so rare it appears nowhere else in Greek literature) trusts the Creator's "
                    "provision. 'Forgive us our debts as we forgive our debtors' makes divine forgiveness "
                    "conditional on human forgiveness. 'Lead us not into temptation but deliver us from the "
                    "evil one' (tou ponerou) is a prayer for protection in cosmic warfare. The chapter "
                    "concludes with Jesus' most extended teaching on anxiety (6:25-34): birds, lilies, and "
                    "the Gentiles who chase after material things. The remedy: 'Seek first the kingdom of "
                    "God and his righteousness, and all these things will be added to you' (6:33).",

        "key_verse": {
            "ref": "Matthew 6:9-10",
            "text": "Pray then like this: 'Our Father in heaven, hallowed be your name. Your kingdom come, your will be done, on earth as it is in heaven.'",
            "translation": "ESV"
        },

        "original_terms": [
            "Pater hemon ho en tois ouranois (Our Father in heaven -- Avinu shebashamayim; YHWH as cosmic Father, enthroned in the heavenly realm above the council)",
            "hagiastheto to onoma sou (hallowed be your name -- from hagiazo; the divine Name set apart as supremely holy; a declaration of YHWH's incomparability)",
            "arton epiousion (daily bread -- epiousion appears NOWHERE else in Greek literature; possibly 'bread for the coming day' or 'bread of existence'; a complete mystery word)",
            "opheilemata (debts -- not merely sins but genuine debts/obligations; the economic metaphor: sin creates a debt to God that only forgiveness can cancel)",
            "peirasmon (temptation/testing -- from peirazo; can mean either enticement to sin or trial/testing; the prayer asks God not to lead into the kind of test that overwhelms)",
            "tou ponerou (the evil one -- can be neuter 'evil' or masculine 'the evil one'; most likely personal: the adversary, Satan, the chief enemy of God's people)",
            "mammonas (mammon -- Aramaic for wealth/possessions; 6:24 personifies it as a rival deity: 'You cannot serve God and mammon')"
        ],

        "ane_backdrop": "Jewish prayer traditions in the Second Temple period included fixed prayers such as "
                        "the Amidah (Eighteen Benedictions) and the Kaddish. The Lord's Prayer shares language "
                        "with the Kaddish: 'May his great name be hallowed... may he establish his kingdom' "
                        "(Kaddish) parallels 'hallowed be your name, your kingdom come.' The concern with "
                        "daily bread echoes the manna tradition (Exodus 16): God provides one day at a time, "
                        "training Israel to trust. The anxiety discourse (6:25-34) has parallels in Stoic "
                        "philosophy (Epictetus' teaching on providential care) but differs fundamentally: "
                        "Stoic calm comes from resignation to fate; Jesus' peace comes from trust in a "
                        "personal Father who knows his children's needs.",

        "second_temple": [
            {
                "source": "Kaddish Prayer (earliest form ~1st century)",
                "summary": "'Magnified and sanctified be his great name... may he establish his kingdom in "
                           "your lifetime and in your days.' The liturgical prayer closest to the Lord's Prayer.",
                "relevance": "Demonstrates shared prayer language between Jesus and Jewish liturgy. The Lord's "
                             "Prayer is thoroughly Jewish while being uniquely Christological."
            },
            {
                "source": "Didache 8:2-3 (~90-100 AD)",
                "summary": "Instructs Christians to pray the Lord's Prayer three times daily, as an "
                           "alternative to the Jewish practice of praying the Amidah three times daily.",
                "relevance": "Shows the Lord's Prayer functioning as the core Christian prayer within a "
                             "generation of Jesus' death."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 16:4-5", "note": "Manna: God provides daily bread one day at a time, teaching trust and dependence", "type": "ot"},
            {"ref": "Psalm 103:13", "note": "'As a father shows compassion to his children, so the LORD shows compassion to those who fear him'", "type": "ot"},
            {"ref": "Luke 11:1-4", "note": "Luke's shorter version of the Lord's Prayer, given in response to 'Lord, teach us to pray'", "type": "nt"},
            {"ref": "Philippians 4:6-7", "note": "'Do not be anxious about anything, but in everything by prayer... the peace of God will guard your hearts'", "type": "nt"},
            {"ref": "1 Peter 5:7", "note": "'Cast all your anxieties on him, because he cares for you' -- the apostolic application of Matt 6:25-34", "type": "nt"}
        ],

        "divine_council_note": "The Lord's Prayer is a divine council document. 'Our Father in heaven' -- the "
                               "Most High God, enthroned above the heavenly assembly. 'Hallowed be your name' "
                               "-- YHWH's name is supreme over all names, including the names of the rebellious "
                               "elohim who rule the nations (Deut 32:8-9). 'Your kingdom come, your will be done "
                               "on earth as it is in heaven' -- the heavenly council's governance extending to "
                               "the earthly realm, displacing the corrupt territorial spirits. 'Deliver us from "
                               "the evil one' -- protection from the adversary (ha-satan) who opposes God's "
                               "purposes. The Lord's Prayer is a concentrated cosmic warfare prayer disguised as "
                               "simple devotion. The personification of mammon (6:24) may reflect the Jewish "
                               "tradition of spiritual powers behind material forces -- wealth as a rival god "
                               "demanding allegiance.",

        "sections": [
            {
                "heading": "Secret Devotion: Giving, Praying, Fasting (6:1-18)",
                "body": "Jesus addresses three pillars of Jewish piety (tsedaqah, tefillah, tsom) with the "
                        "same principle: do not practice your righteousness before others 'to be seen by them' "
                        "(6:1). The hypocrites (hypokritai -- literally 'stage actors') sound trumpets when "
                        "they give (6:2), pray on street corners (6:5), and disfigure their faces when fasting "
                        "(6:16). They 'have received their reward' (apechousin -- a commercial term meaning "
                        "'paid in full'). The alternative: give in secret (6:3-4), pray in the inner room "
                        "(tameion, 6:6), and fast with a washed face (6:17). 'Your Father who sees in secret "
                        "will reward you' (6:4, 6, 18). The three-fold repetition emphasizes: the audience "
                        "that matters is God alone."
            },
            {
                "heading": "The Lord's Prayer: Seven Petitions (6:9-13)",
                "body": "The prayer divides into two halves. The first three petitions are God-ward: hallowed "
                        "be your name, your kingdom come, your will be done. The second four are human-ward: "
                        "daily bread, debt forgiveness, temptation protection, evil deliverance. The structure "
                        "mirrors the Decalogue: duties toward God first, then duties toward self and neighbor. "
                        "'Epiousion' (daily) is the most mysterious word in the NT -- it appears nowhere "
                        "else in all of Greek literature. Origen noted it was not found in any Greek writer "
                        "or common speech. It may mean 'for the coming day' (epi + ousia) or 'supersubstantial' "
                        "(above physical sustenance). The forgiveness petition is the only one Jesus expands "
                        "(6:14-15): 'If you forgive others their trespasses, your heavenly Father will also "
                        "forgive you, but if you do not forgive others their trespasses, neither will your "
                        "Father forgive your trespasses.' Divine mercy flows through human mercy."
            },
            {
                "heading": "Do Not Be Anxious: Creation Theology (6:25-34)",
                "body": "'Therefore I tell you, do not be anxious (merimnate) about your life' (6:25). The "
                        "argument moves from lesser to greater: if God feeds the birds (6:26), clothes the "
                        "lilies with glory surpassing Solomon (6:28-29), and adorns the grass of the field "
                        "(6:30), how much more will he care for his children? The rebuke is gentle: 'O you of "
                        "little faith (oligopistoi)' (6:30). Anxiety is a faith problem, not an intelligence "
                        "problem. The Gentiles (ta ethne) seek after all these things (6:32) -- nations "
                        "without a covenant Father are right to be anxious. But you have a Father who knows "
                        "your needs. The solution: 'Seek first the kingdom of God and his righteousness, "
                        "and all these things will be added to you' (6:33). Kingdom priority produces "
                        "provision. 'Each day has enough trouble of its own' (6:34) -- live in daily "
                        "dependence, like Israel gathering manna one day at a time."
            }
        ]
    },

    {
        "id": "matt-two-ways",
        "ref": "Matthew 7:1-29",
        "chapter_num": 4,
        "title": "The Narrow Gate and the Two Builders",
        "era": "matt_sermon",
        "type": "study",
        "themes": ["KING", "DC", "HOLY", "NAME", "RIV"],

        "synopsis": "Chapter 7 closes the Sermon with urgent warnings and a decisive call. 'Judge not, that "
                    "you be not judged' (7:1) -- not a prohibition against moral discernment but against "
                    "hypocritical condemnation. The log-and-speck parable (7:3-5) exposes the blindness of "
                    "those who criticize others while ignoring their own failures. 'Do not give dogs what is "
                    "holy, and do not throw your pearls before pigs' (7:6) -- discernment IS required, just not "
                    "hypocrisy. The prayer promises follow: 'Ask, and it will be given to you; seek, and you "
                    "will find; knock, and it will be opened to you' (7:7). If human fathers give good gifts, "
                    "'how much more will your Father who is in heaven give good things to those who ask him!' "
                    "(7:11). The Golden Rule summarizes the entire ethical teaching: 'Whatever you wish that "
                    "others would do to you, do also to them, for this is the Law and the Prophets' (7:12). "
                    "Then three warnings: the narrow gate (few find it, 7:13-14), false prophets (wolves in "
                    "sheep's clothing, known by their fruit, 7:15-20), and the terrifying declaration: 'Not "
                    "everyone who says to me, \"Lord, Lord,\" will enter the kingdom of heaven, but the one who "
                    "does the will of my Father' (7:21). Even miracle workers may hear 'I never knew you; "
                    "depart from me, you workers of lawlessness (anomias)' (7:23). The Sermon's final parable "
                    "-- the wise and foolish builders -- demands decision: build on Jesus' words (rock) or "
                    "reject them (sand). The crowds respond with astonishment: 'he was teaching them as one "
                    "who had authority (exousia), and not as their scribes' (7:29).",

        "key_verse": {
            "ref": "Matthew 7:24-25",
            "text": "Everyone then who hears these words of mine and does them will be like a wise man who built his house on the rock. And the rain fell, and the floods came, and the winds blew and beat on that house, but it did not fall, because it had been founded on the rock.",
            "translation": "ESV"
        },

        "original_terms": [
            "krinete (judge -- from krino; the word covers a range from 'evaluate' to 'condemn'; Jesus forbids condemnatory judgment, not moral discernment)",
            "stene pyle (narrow gate -- the kingdom entrance is constrained; few find it because it requires self-denial, not self-promotion)",
            "anomia (lawlessness -- from a + nomos, 'without Torah'; those who claim Jesus' name but reject his teaching; lawlessness = life without divine order)",
            "exousia (authority -- not merely rhetorical skill but inherent, delegated divine authority; the authority of one who IS the Torah-giver, not merely its interpreter)",
            "petra (rock -- bedrock, foundation; the same word used for Peter's renaming (16:18); here it is Jesus' words themselves that form the unshakeable foundation)",
            "phronimos (wise/prudent -- from phroneo; the wise builder has practical wisdom that acts on what is heard; wisdom = obedience, foolishness = hearing without doing)"
        ],

        "ane_backdrop": "The 'Two Ways' tradition -- a choice between the path of life and the path of death -- "
                        "is one of the oldest ethical frameworks in the ancient world. It appears in Deuteronomy "
                        "30:19 ('I have set before you life and death, blessing and curse'), the Egyptian 'Two "
                        "Ways of Life' papyrus, and the Didache's opening ('There are two ways, one of life "
                        "and one of death'). Jesus' two builders parable transforms this tradition: the choice "
                        "is not merely between ethical paths but between building one's entire life on Jesus' "
                        "words or on anything else. The storm imagery (rain, floods, winds) recalls cosmic "
                        "judgment language from the prophets (Isaiah 28:15-18, where YHWH's 'overwhelming "
                        "scourge' sweeps away those who trust in lies).",

        "second_temple": [
            {
                "source": "Didache 1:1",
                "summary": "'There are two ways, one of life and one of death, and there is a great "
                           "difference between these two ways.' The opening of the earliest Christian manual.",
                "relevance": "The Two Ways tradition that frames the Didache directly echoes the Sermon's "
                             "narrow/wide gate teaching and the two builders conclusion."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 30:15-20", "note": "'I have set before you life and death, blessing and curse. Therefore choose life' -- the OT Two Ways framework behind the Sermon's conclusion", "type": "ot"},
            {"ref": "Isaiah 28:16-17", "note": "'Behold, I am the one who has laid as a foundation in Zion a stone, a tested stone, a precious cornerstone, of a sure foundation' -- the rock on which to build", "type": "ot"},
            {"ref": "Psalm 1:1-6", "note": "The two ways: the righteous who delight in Torah vs. the wicked who are like chaff -- the Psalter opens where the Sermon closes", "type": "ot"},
            {"ref": "James 1:22-25", "note": "'Be doers of the word, and not hearers only, deceiving yourselves' -- James' application of the two builders principle", "type": "nt"},
            {"ref": "Luke 6:46-49", "note": "Luke's parallel: 'Why do you call me Lord, Lord, and not do what I tell you?' with the house built on the ground vs. rock", "type": "nt"}
        ],

        "divine_council_note": "The authority (exousia) that astonishes the crowds (7:28-29) is not merely "
                               "rhetorical power but divine council authority. The scribes derived their authority "
                               "from the chain of tradition -- 'Rabbi X said in the name of Rabbi Y.' Jesus "
                               "derives his authority from himself, from his identity as the divine Son who IS "
                               "the Word of God. When he says 'I never knew you' (7:23), he claims the prerogative "
                               "of final judgment -- a function belonging to God alone. The 'workers of lawlessness' "
                               "(ergazomenoi ten anomian, 7:23) may include those who invoke Jesus' name for "
                               "spiritual warfare ('cast out demons in your name,' 7:22) without genuine "
                               "submission to his authority. The warning is severe: supernatural manifestations "
                               "do not prove divine approval. The only proof is fruit -- character that reflects "
                               "the Father's nature.",

        "sections": [
            {
                "heading": "The Log and the Speck: Judging with Integrity (7:1-6)",
                "body": "The famous 'judge not' is the most misquoted verse in Scripture. Jesus does not forbid "
                        "discernment -- he immediately demands it ('do not give dogs what is holy,' 7:6). What "
                        "he forbids is hypocritical, self-righteous condemnation. The image is absurd: a person "
                        "with a construction beam (dokos) in their eye offering to remove a splinter (karphos) "
                        "from their brother's eye. 'First take the log out of your own eye, and then you will "
                        "see clearly to take the speck out of your brother's eye' (7:5). Self-examination "
                        "precedes correction of others."
            },
            {
                "heading": "Ask, Seek, Knock: The Father's Generosity (7:7-12)",
                "body": "Three imperatives (present tense, implying ongoing action): keep asking, keep seeking, "
                        "keep knocking. The Father's response is reliable: 'For everyone who asks receives' "
                        "(7:8). The analogy: no human father gives a stone instead of bread or a serpent instead "
                        "of fish (7:9-10). If evil (poneroi) humans know how to give good gifts, 'how much more "
                        "will your Father who is in heaven give good things to those who ask him!' (7:11). "
                        "Luke's parallel specifies: the Father gives 'the Holy Spirit to those who ask him' "
                        "(Luke 11:13). The Golden Rule (7:12) summarizes: 'This is the Law and the Prophets' "
                        "-- the entire ethical tradition distilled into one principle."
            },
            {
                "heading": "Lord, Lord: The Danger of Empty Profession (7:21-29)",
                "body": "'Not everyone who says to me, \"Lord, Lord,\" will enter the kingdom' (7:21). The "
                        "warning targets people who use Jesus' name but reject his authority. They prophesy, "
                        "cast out demons, and do mighty works 'in your name' (7:22) -- spectacular spiritual "
                        "ministry without genuine submission. Jesus' response: 'I never knew you; depart "
                        "from me, you workers of lawlessness' (7:23). The verb 'knew' (egnon, from ginosko) "
                        "is covenantal knowledge -- YHWH's intimate, elective knowledge. These miracle workers "
                        "were never truly known by Jesus despite their public ministry. The Sermon then "
                        "concludes with the most decisive parable: two builders, one storm, opposite outcomes. "
                        "'The rain fell, and the floods came, and the winds blew' (7:25, 27) -- identical "
                        "storms hit both houses. The only difference is the foundation."
            }
        ]
    },

    {
        "id": "matt-sermon-synthesis",
        "ref": "Matthew 5-7 (Synthesis)",
        "chapter_num": 5,
        "title": "The Sermon as Kingdom Charter: From Sinai to the New Mountain",
        "era": "matt_sermon",
        "type": "study",
        "themes": ["KING", "LAW", "COV", "DC", "TYPE"],

        "synopsis": "The Sermon on the Mount is not merely ethical teaching -- it is the charter of a new "
                    "kingdom and the revelation of a new Moses. Matthew structures his Gospel around five "
                    "great discourses (chs. 5-7, 10, 13, 18, 24-25), paralleling the five books of Moses. "
                    "The Sermon is the first and foundational discourse -- the kingdom's Torah. Its structure "
                    "is chiastic: the Beatitudes (A) and the Two Builders (A') frame the teaching, the "
                    "antitheses (B) and the warnings (B') mirror each other, and the Lord's Prayer stands "
                    "at the center (C). The theological logic moves from identity (who are the kingdom's "
                    "citizens? -- Beatitudes) through ethics (how do they live? -- antitheses, chapter 6) "
                    "to destiny (what happens to them? -- chapter 7). The Sermon assumes that the kingdom "
                    "has already arrived in Jesus' person and that his followers are already living under "
                    "its rule, even while the old age continues. The tension between 'already' and 'not yet' "
                    "pervades every paragraph: the kingdom IS theirs (5:3), but they still face persecution "
                    "(5:10); the Father WILL provide (6:33), but anxiety is a daily battle (6:34); the house "
                    "WILL stand (7:25), but the storm is coming. The Sermon ends with 'authority' (exousia) -- "
                    "the crowds recognize that Jesus speaks not as a scribe repeating tradition but as one "
                    "who possesses inherent, divine authority over Torah, ethics, and destiny.",

        "key_verse": {
            "ref": "Matthew 7:28-29",
            "text": "And when Jesus finished these sayings, the crowds were astonished at his teaching, for he was teaching them as one who had authority, and not as their scribes.",
            "translation": "ESV"
        },

        "original_terms": [
            "exousia (authority -- the word that closes the Sermon; Jesus possesses divine authority that surpasses all human teaching tradition)",
            "basileia (kingdom -- the governing concept: the Sermon describes life under God's rule, not merely ethical principles for a fallen world)",
            "dikaiosyne (righteousness -- appears 7 times in the Sermon; not forensic imputation but lived covenant faithfulness that exceeds the Pharisees' (5:20))",
            "nomos kai prophetas (the Law and the Prophets -- Jesus claims to fulfill (5:17) and summarize (7:12) the entire Hebrew Scripture in his teaching)"
        ],

        "ane_backdrop": "Matthew's five-discourse structure deliberately parallels the Pentateuch. Just as Moses "
                        "delivered five books of Torah, Jesus delivers five great speeches. This 'new Torah' "
                        "pattern positions Jesus as the new and greater Moses -- the prophet 'like Moses' "
                        "promised in Deuteronomy 18:15-18. The mountain setting (5:1) recalls Sinai, where "
                        "YHWH gave the first Torah. But there is a crucial difference: at Sinai, the people "
                        "stayed at the base while Moses ascended alone. On this mountain, Jesus invites the "
                        "crowds up with him. The barrier between God and people is being removed. The Sermon's "
                        "ethical vision has no true parallel in the ancient world. Neither Greek philosophy "
                        "(which celebrated justice and moderation) nor Jewish wisdom literature (which taught "
                        "prudent living) demanded love of enemies as a foundational ethic.",

        "second_temple": [
            {
                "source": "Targum Pseudo-Jonathan on Deuteronomy 18:15",
                "summary": "'A prophet from among you, from your brothers, like me, the Lord your God will "
                           "raise up for you; to him you shall hearken.'",
                "relevance": "The expectation of a new Moses who would deliver new Torah was alive in Jesus' day. "
                             "The Sermon fulfills this expectation while surpassing it: Jesus does not merely "
                             "transmit Torah but speaks with the authority of the Torah-giver himself."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 18:15-18", "note": "The prophet like Moses who will speak God's words -- Jesus as the new and greater Moses delivering new Torah from a new mountain", "type": "ot"},
            {"ref": "Exodus 19:16-20", "note": "The Sinai theophany -- God descending on the mountain to give Torah; Jesus ascends the mountain to deliver the kingdom's Torah", "type": "ot"},
            {"ref": "2 Corinthians 3:7-18", "note": "Paul contrasts the ministry of Moses (glory that faded) with the ministry of the Spirit (glory that increases) -- the new covenant surpasses Sinai", "type": "nt"},
            {"ref": "Hebrews 12:18-24", "note": "'You have not come to a mountain that can be touched... but you have come to Mount Zion' -- the Sermon's mountain is the heavenly Zion", "type": "nt"}
        ],

        "divine_council_note": "The Sermon's theological logic can only be understood through the lens of divine "
                               "council theology. Jesus speaks as the unique Son of the Father (5:45, 48; 6:9; "
                               "7:11, 21) -- not one Son among many but THE Son who shares the Father's authority. "
                               "He commands obedience to his own words as the criterion for eternal destiny (7:24-27). "
                               "He claims the right to reject those who invoke his name but practice lawlessness "
                               "(7:22-23). He speaks 'not as the scribes' (7:29) because he IS the divine Word "
                               "that gave Torah in the first place. The Sermon is not a human teacher offering "
                               "ethical advice -- it is the visible YHWH, the Son, delivering the constitution "
                               "of the kingdom that has come to reclaim the earth from the hostile powers.",

        "sections": [
            {
                "heading": "Five Discourses, Five Books: The New Moses Pattern",
                "body": "Matthew structures his Gospel around five great discourses, each ending with a "
                        "transitional formula ('When Jesus finished these sayings,' 7:28; 11:1; 13:53; "
                        "19:1; 26:1). This five-fold pattern parallels the Pentateuch. Discourse 1 (Sermon "
                        "on the Mount, chs. 5-7) = kingdom ethics. Discourse 2 (Missionary Discourse, ch. 10) "
                        "= kingdom mission. Discourse 3 (Parables Discourse, ch. 13) = kingdom mystery. "
                        "Discourse 4 (Community Discourse, ch. 18) = kingdom relationships. Discourse 5 "
                        "(Olivet Discourse, chs. 24-25) = kingdom consummation. Together they form the "
                        "'new Torah' -- Jesus' comprehensive teaching on life in the kingdom of heaven."
            },
            {
                "heading": "Already and Not Yet: The Kingdom Tension",
                "body": "The Sermon assumes the kingdom is present ('theirs IS the kingdom,' 5:3, 10) while "
                        "acknowledging it is not yet complete ('your kingdom COME,' 6:10). Citizens live "
                        "between the inauguration (Jesus' ministry) and the consummation (his return). This "
                        "'already/not yet' tension explains why the Sermon's ethic feels simultaneously "
                        "possible and impossible: possible because the Spirit empowers kingdom living, "
                        "impossible because the old age resists at every point. The Sermon is not a code "
                        "for earning salvation but a description of life empowered by grace under the rule "
                        "of the returning King."
            }
        ]
    }
]
