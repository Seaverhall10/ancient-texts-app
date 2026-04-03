"""
era_hebrews_council.py -- Hebrews: The Divine Council Lens

Hebrews is constructed entirely around a single cosmic argument: the Son
occupies a position in the divine council hierarchy that no angel, prophet,
or priest has ever held. The letter does not merely quote the Old Testament
-- it quotes the divine council's own charter texts (Psalms 2, 8, 45, 102,
110; Deuteronomy 32:43 LXX/DSS) and reads them as a cumulative legal brief
establishing the Son's supremacy above every tier of the heavenly
administration. This era examines Hebrews through the full council lens:
the DSS/LXX variant at 1:6, the angelic mediation of Torah, the tabernacle
as a copy of the divine throne room, the heavenly assembly of Hebrews 12,
and the ekklesia's current participation in that assembly.

Five chapters (four study + one historical insert) covering the council
architecture of Hebrews from multiple angles -- the Son's rank above the
council members, the inferiority of angelic-mediated Torah, the heavenly
sanctuary as the council chamber, the cosmic shaking that removes corrupt
heavenly powers, and the continuous Melchizedekian tradition that connects
the DSS and the NT.
"""

CHAPTERS = [
    # ------------------------------------------------------------------
    # CHAPTER 1: THE SON ABOVE ALL -- HEBREWS 1:1-14
    # ------------------------------------------------------------------
    {
        "id": "heb-council-1",
        "ref": "Hebrews 1:1-14",
        "chapter_num": 1,
        "title": "The Son Above All -- The Council Commanded to Worship",
        "era": "hebrews_council",
        "type": "chapter",
        "themes": ["DC", "KING", "LAW", "SEED", "TYPE"],

        "synopsis": (
            "Hebrews 1 opens with a seven-claim christological declaration and then "
            "deploys a catena of seven Old Testament quotations to prove a single "
            "point: the Son occupies a position within the divine council hierarchy "
            "that no angel has ever held. [A] The climactic citation in 1:6 -- 'Let "
            "all God's angels worship him' -- quotes Deuteronomy 32:43 in the LXX "
            "and DSS (4QDeuteronomyq) reading, a text the Masoretic tradition does "
            "not contain, proving the author worked from the same textual tradition "
            "as Qumran. [B] The catena is structured as a legal brief before the "
            "divine council itself, systematically establishing that the Son holds "
            "the supreme position -- heir, creator, radiance of glory, seated at "
            "the right hand, worshiped by the whole council. [C] The ANE pattern of "
            "a divine figure elevated above the council assembly finds its "
            "theological fulfillment here, but with a crucial difference: the Son "
            "is not a rival to the Father but his exact imprint (charakter) sharing "
            "his very substance (hypostasis)."
        ),

        "key_verse": {
            "ref": "Hebrews 1:6",
            "text": "And again, when he brings the firstborn into the world, he says, 'Let all God's angels worship him.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "apaugasma (radiance/effulgence -- 1:3; the Son is the outshining of divine glory, not a reflected light but the emission of the source itself; used only here in the NT)",
            "charakter (exact imprint -- 1:3; the stamp pressed into wax that carries the precise impression of the seal; the Son bears the precise impression of God's hypostasis)",
            "hypostasis (substance/underlying reality -- 1:3; the foundational ontological reality of God's being; the Son is the charakter of this hypostasis, not a copy of a copy)",
            "kreitton (superior/better -- 1:4; a key word repeated 13 times in Hebrews; the Son is kreitton than the angels -- categorically and ontologically, not merely functionally)",
            "klēronomos (heir -- 1:2; appointed heir of panta, 'all things' -- the entire created order, visible and invisible, including every angelic dominion and territorial assignment)",
            "diaphoroteron (more excellent -- 1:4; comparative of diaphoros; the name the Son has inherited is in a different category of excellence from any angelic name)",
            "bene elohim (sons of God -- the divine council members of OT usage; Deut 32:8, Job 1-2, Ps 82; Heb 1 uses this tradition to establish the Son's superiority over this entire class)",
            "leitourgika pneumata (ministering spirits -- 1:14; the council members' role is service, not sovereignty; they are sent to serve for those who inherit salvation)",
            "kathizō (to sit down -- 1:3; the posture of completed work and sovereign authority; the Son 'sat down' at the right hand -- no angel has ever been invited to sit)",
            "prototokos (firstborn -- 1:6; used in the command 'when he brings the firstborn into the world'; cosmic rank title, not merely birth order -- cf. Ps 89:27; Col 1:15)"
        ],

        "ane_backdrop": (
            "The divine assembly and the question of rank within it pervades ancient "
            "Near Eastern literature. In the Ugaritic texts, El presides over the "
            "assembly of the gods (phr ilm / 'dt ilm), and the critical question is "
            "always: who holds the highest position? Baal's enthronement above the "
            "council after defeating Yam and Mot follows a pattern of cosmic combat "
            "and subsequent exaltation to the head of the assembly. In the Enuma "
            "Elish, the Babylonian council (Anunnaki) grants Marduk supreme authority "
            "after he defeats Tiamat: 'Among the great gods, his rank be foremost' "
            "(Tablet VI). The Egyptian Ennead debated divine supremacy; Pharaoh was "
            "the earthly representative of the heavenly council's highest member. "
            "In all these traditions the fundamental question is: to whom does "
            "worship belong within the assembly? The answer was always 'the one who "
            "sits at the head.' Hebrews 1 answers this question with the full weight "
            "of Israel's scriptures: the Son sits at the right hand, and the entire "
            "council -- every bene elohim, every cosmic power -- is commanded to "
            "worship him. This is not monotheistic denial of the council's existence "
            "but monotheistic declaration of the Son's supreme position within it."
        ),

        "second_temple": [
            {
                "source": "4QDeuteronomyq (4QDeutq) -- Deuteronomy 32:43 DSS Reading",
                "summary": (
                    "The Dead Sea Scrolls fragment 4QDeutq preserves the longer reading "
                    "of Deuteronomy 32:43: 'Praise him, O heavens, bow down to him, all "
                    "you divine beings (bene elohim); for he will avenge the blood of his "
                    "sons... Rejoice with him, O heavens; worship him, all you gods.' "
                    "This reading corresponds to the LXX and is the text quoted in "
                    "Hebrews 1:6, entirely absent from the Masoretic text."
                ),
                "relevance": (
                    "The author of Hebrews was not quoting a mistranslation or an "
                    "obscure variant -- he was working from the same textual tradition "
                    "as the Qumran community. 4QDeutq confirms this is an authentic "
                    "ancient reading of Deut 32. The command for the divine council "
                    "to worship the Son is grounded in a text the Qumran scribes "
                    "preserved, and Hebrews deploys it as the christological climax "
                    "of the Deuteronomy 32 worldview."
                )
            },
            {
                "source": "1 Enoch 61:10-12; 69:26-29 -- The Chosen One Enthroned",
                "summary": (
                    "The Parables of Enoch describe the Chosen One / Son of Man seated "
                    "on the throne of glory, before whom every angel and heavenly power "
                    "falls prostrate. The angelic hosts, the seraphim, the cherubim, "
                    "the ophannim -- the entire council structure -- worship him. "
                    "'And all those who dwell on the earth shall fall and worship before "
                    "him, and they will glorify and bless and celebrate with song the "
                    "Lord of Spirits' (1 En 48:5)."
                ),
                "relevance": (
                    "According to 1 Enoch, the pattern of the entire divine council "
                    "worshiping a figure at the head of the assembly was already present "
                    "in Second Temple Jewish tradition. Hebrews 1:6 grounds this pattern "
                    "in the Deuteronomy 32 charter text rather than apocalyptic vision, "
                    "giving it canonical authority while resonating with the same cosmic "
                    "framework the Enoch tradition developed."
                )
            },
            {
                "source": "Philo of Alexandria, On the Confusion of Tongues 146-147",
                "summary": (
                    "Philo describes the Logos as God's 'firstborn son' (prototokos "
                    "huios), 'the image of God' (eikon theou), and the mediator between "
                    "God and creation. The Logos is neither unbegotten like God nor "
                    "merely created, but the first and highest of God's works, through "
                    "whom all other things were made."
                ),
                "relevance": (
                    "Philo provides a pre-Christian Jewish framework for a divine "
                    "mediator figure who is God's agent in creation and governance. "
                    "Hebrews 1:2-3 uses similar vocabulary (apaugasma, charakter, "
                    "prototokos, agent of creation) but makes a claim Philo does not: "
                    "the Son shares God's own hypostasis and is worshiped by the "
                    "entire council. This is not Logos theology -- it is divine "
                    "council enthronement."
                )
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:43 (LXX/DSS)", "note": "The source of Heb 1:6 -- 'Let all God's angels worship him'; present in 4QDeutq and LXX but absent from MT, confirming the author's textual tradition", "type": "dss"},
            {"ref": "Psalm 110:1", "note": "'Sit at my right hand until I make your enemies a footstool' -- quoted in Heb 1:13; the right-hand invitation never extended to any angel", "type": "ot"},
            {"ref": "Psalm 2:7", "note": "'You are my Son; today I have begotten you' -- the enthronement decree quoted in Heb 1:5; the unique filial identity that distinguishes the Son from the bene elohim", "type": "ot"},
            {"ref": "Psalm 45:6-7", "note": "'Your throne, O God, is forever' -- quoted in Heb 1:8-9; the Son is addressed as theos by God himself, a 'two powers in heaven' formulation", "type": "ot"},
            {"ref": "Psalm 104:4", "note": "'He makes his angels winds, his ministers a flame of fire' -- quoted Heb 1:7; the council members are created servants, not sovereigns", "type": "ot"},
            {"ref": "Psalm 102:25-27", "note": "Creation language addressed to YHWH in the original psalm applied to the Son in Heb 1:10-12; the Son is the creator, the council is created", "type": "ot"},
            {"ref": "Deuteronomy 32:8", "note": "The Deuteronomy 32 worldview: bene elohim assigned to the nations at Babel; Heb 1:6 commands these same beings to worship the Son", "type": "ot"},
            {"ref": "Colossians 1:15-17", "note": "Paul's parallel cosmic-Christology: Son as image of God, firstborn of all creation, through whom all things including thrones, dominions, rulers, and authorities were created", "type": "nt"},
            {"ref": "Philippians 2:9-11", "note": "'The name that is above every name, that at the name of Jesus every knee should bow, in heaven and on earth and under the earth' -- the worship of the entire cosmic hierarchy", "type": "nt"},
            {"ref": "1 Enoch 61:10-12", "note": "According to 1 Enoch, the enthroned Son of Man receives worship from all angelic orders -- cherubim, seraphim, ophannim; Heb 1:6 grounds this in Deut 32:43", "type": "pseudepigrapha"}
        ],

        "divine_council_note": (
            "Hebrews 1 is structured as a legal brief presented before the divine "
            "council itself. The author takes seven OT texts that describe the "
            "council's charter, operations, and hierarchy, and reads them as "
            "cumulative testimony establishing the Son's supreme rank. This is "
            "not poetic hyperbole -- it is jurisprudence. The seven quotations "
            "establish seven distinct legal points: (1) unique filial identity "
            "(Ps 2:7 / 2 Sam 7:14 -- no angel was ever called 'my Son'); (2) the "
            "command for total council worship (Deut 32:43 LXX/DSS -- the entire "
            "bene elohim class must bow); (3) the nature of angelic existence as "
            "created servants rather than sovereigns (Ps 104:4); (4) direct divine "
            "address to the Son as God (Ps 45:6-7 -- theos applied to the Son by "
            "God); (5) the Son as creator, outlasting all created things including "
            "the council itself (Ps 102:25-27); (6) the right-hand invitation "
            "never extended to any angel (Ps 110:1 -- 'to which of the angels "
            "has he ever said...'); and (7) the redefinition of the council members "
            "as ministering spirits in service of the redeemed (1:14). "
            "\n\n"
            "The DSS connection at 1:6 is critical for the council lens. The "
            "author cites the Deut 32:43 reading that contains 'let all the divine "
            "beings worship him' -- the very text confirmed by 4QDeutq at Qumran. "
            "This means the author was operating within the same tradition as the "
            "Qumran community, which read Deuteronomy 32 as a cosmic charter "
            "document describing the bene elohim's assignment to the nations and "
            "their eventual judgment. Hebrews 1:6 takes this charter text and "
            "declares its climax: the same divine beings allotted the nations "
            "at Babel must now prostrate before YHWH's firstborn. The Deut 32 "
            "worldview -- rebellion, judgment, and redemption through the Son -- "
            "runs as a continuous thread from Genesis to Revelation, and Hebrews "
            "1 is its christological summit."
        ),

        "sections": [
            {
                "heading": "The Shift from Partial to Complete: Speaking Through the Son (1:1-2a)",
                "body": (
                    "The opening of Hebrews is a single Greek sentence -- one of the "
                    "most architecturally sophisticated sentences in the NT -- and it "
                    "begins by contrasting two modes of divine speech. 'Long ago, at "
                    "many times (polumeros) and in many ways (polutropos), God spoke "
                    "to our fathers by the prophets.' The alliteration is deliberate: "
                    "God's former speech was polu- -- many-fold in both frequency and "
                    "form. Dreams, visions, law, narrative, poetry, prophecy -- each "
                    "prophet received one portion, one thread of the tapestry. Jeremiah "
                    "23:18,22 describe the prophet as one who has 'stood in the council "
                    "(sod) of the LORD' and heard what YHWH declared. The prophet was "
                    "a messenger from the assembly, reporting what he had witnessed."
                    "\n\n"
                    "'But in these last days (ep' eschatou ton hemeron) he has spoken "
                    "to us en huio -- in a Son.' The phrase 'in a Son' is not 'through "
                    "a son' (dia): the Son is not a channel of revelation but its "
                    "embodiment. The prophets stood in the council and reported; the "
                    "Son sits at the council's right hand and speaks from it. The "
                    "fragmentary, multi-modal revelation has given way to one complete, "
                    "definitive word. And this word is a person."
                )
            },
            {
                "heading": "Seven Claims and the Son's Position in the Council (1:2b-4)",
                "body": (
                    "Before citing a single OT text, the author states seven christological "
                    "claims in one sentence, each addressing the Son's rank in the "
                    "divine council: (1) Heir of all things (klēronomos panton) -- "
                    "the Son inherits the entire created order, visible and invisible. "
                    "(2) Agent of creation -- if council members are created and the "
                    "Son created them, his ontological rank is categorically different. "
                    "(3) Radiance of the glory (apaugasma tes doxes) -- not lit by "
                    "divine glory from outside; he IS the outshining of it. (4) Exact "
                    "imprint of his nature (charakter tes hypostaseos autou) -- the "
                    "precise impression of God's own substance, not a copy. (5) Upholds "
                    "the universe by the word of his power -- ongoing cosmic governance. "
                    "(6) Made purification for sins -- the priestly act that precedes "
                    "(7) sitting down at the right hand -- the throne position no angel "
                    "has ever occupied. The seven claims build inexorably to this final "
                    "image: the Son seated, work complete, supreme in the council."
                )
            },
            {
                "heading": "The DSS Variant That Changes Everything: Deuteronomy 32:43 (1:6)",
                "body": (
                    "The catena of OT quotations in 1:5-14 reaches its most dramatic "
                    "moment at verse 6: 'Let all God's angels worship him.' This quote "
                    "does not appear in the Masoretic Text of Deuteronomy 32:43. The "
                    "MT reads: 'Rejoice, O nations, with his people' -- no angels, no "
                    "worship command. But the Septuagint and Dead Sea Scrolls diverge. "
                    "The DSS fragment 4QDeuteronomyq (4QDeutq) preserves the longer "
                    "reading: 'Bow down to him, all you divine beings (bene elohim).' "
                    "The LXX reads: 'Let all the sons of God worship him.' Text-critical "
                    "analysis indicates the MT may have shortened the text. The author "
                    "of Hebrews worked from the tradition that 4QDeutq and the LXX "
                    "preserve -- the same tradition the Qumran community studied."
                    "\n\n"
                    "This is one of the clearest NT citations of a DSS/LXX variant "
                    "diverging from the MT, and it is not incidental -- it is the "
                    "entire point. The command is issued to the bene elohim, the same "
                    "beings allotted the nations at Babel (Deut 32:8, also DSS/LXX). "
                    "The Deuteronomy 32 worldview finds its christological climax here: "
                    "every member of the divine council must prostrate before YHWH's "
                    "firstborn. The Babel assignment is overturned by the worship "
                    "command."
                )
            },
            {
                "heading": "Never Invited to Sit: The Right-Hand Question (1:13-14)",
                "body": (
                    "The catena closes with a rhetorical question: 'To which of "
                    "the angels has he ever said, Sit at my right hand?' (1:13, "
                    "Ps 110:1). The answer is universal: not one. In the divine "
                    "council, YHWH's throne is unshared. The seraphim of Isaiah 6 "
                    "stand above it; the cherubim flank the ark; the beings of "
                    "Revelation 4 surround it. No created being sits at YHWH's "
                    "right hand -- yet this is the exact invitation the Father "
                    "extends to the Son. Psalm 110:1 is the most cited OT text "
                    "in the NT, and after six prior citations establishing "
                    "superiority, this final one places the Son at the apex "
                    "of all cosmic governance."
                    "\n\n"
                    "Verse 14 redefines the council members entirely: 'Are they "
                    "not all ministering spirits (leitourgika pneumata) sent out "
                    "to serve for the sake of those who are to inherit salvation?' "
                    "Council members are not rivals -- they are servants of the "
                    "redemptive mission. Their glory is real (winds and flames of "
                    "fire, v.7), but it is the glory of servants, not sovereigns."
                )
            },
            {
                "heading": "Why the Catena Is a Legal Brief",
                "body": (
                    "The seven OT quotations in 1:5-14 are deployed with legal "
                    "precision as a catena -- a chain of linked citations. Each link "
                    "answers a specific question: Does the Son hold unique filial "
                    "identity (Ps 2:7, 2 Sam 7:14)? Does the divine council worship "
                    "him (Deut 32:43 DSS/LXX)? What is angelic existence (Ps 104:4)? "
                    "Is the Son divine (Ps 45:6-7)? Is he the creator (Ps 102:25-27)? "
                    "Has he received the supreme governance position (Ps 110:1)? "
                    "Each answer is drawn from the council's own charter texts -- "
                    "from inside the tradition, not imposed from without. The author "
                    "is not making a novel claim; he is reading the divine council "
                    "literature and showing that, read correctly, it has always "
                    "pointed to the Son's enthronement above it."
                    "\n\n"
                    "The genre resonates with the riv (covenant lawsuit) tradition: "
                    "YHWH summons witnesses and presents evidence before the divine "
                    "assembly (Isa 1:2; Mic 6:1-2; Ps 50:1-6). Hebrews 1 is a riv "
                    "against the claim that angelic mediators of the old covenant "
                    "stand equal to the Son. The verdict in verse 4: the Son is "
                    "kreitton (superior) to angels as his name is diaphoroteron "
                    "(more excellent) -- categorically, not merely comparatively."
                )
            }
        ]
    },

    # ------------------------------------------------------------------
    # CHAPTER 2: THE TORAH THROUGH ANGELS -- HEBREWS 2:1-9
    # ------------------------------------------------------------------
    {
        "id": "heb-council-2",
        "ref": "Hebrews 2:1-9",
        "chapter_num": 2,
        "title": "The Torah Through Angels -- Why Angelic Mediation Is Inferior",
        "era": "hebrews_council",
        "type": "chapter",
        "themes": ["DC", "REBEL", "KING", "COV", "TYPE"],

        "synopsis": (
            "Hebrews 2 addresses the consequence of the Son's superiority for "
            "covenant theology: if the Torah was delivered through angelic mediators, "
            "and if the Son is superior to all angels, then a covenant mediated "
            "directly through the Son must be superior to the Mosaic covenant. "
            "[A] Hebrews 2:2 explicitly states that 'the message declared by angels "
            "proved to be reliable,' confirmed by Acts 7:53 (Stephen's speech) and "
            "Galatians 3:19 ('the law was put in place through angels by an "
            "intermediary'). This is not polemical -- the angelic mediation was "
            "designed, reliable, and authoritative. [B] The logic of Hebrews' "
            "argument requires it: you do not replace a lower mediator with a "
            "higher one unless the higher is genuinely superior, and you do not "
            "abandon a reliable system unless a more-than-reliable one has arrived. "
            "[C] The temporary descent of the Son below the angels (v.9 -- 'for a "
            "little while lower than the angels') makes his exaltation above them "
            "all the more theologically dramatic."
        ),

        "key_verse": {
            "ref": "Hebrews 2:2",
            "text": "For since the message declared by angels proved to be reliable, and every transgression or disobedience received a just retribution...",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "di' angelon (through angels -- 2:2; the Mosaic Torah was 'declared through angels'; this is not heterodox -- Acts 7:53, Gal 3:19, Deut 33:2 LXX all confirm this tradition)",
            "bebaios (reliable/firm -- 2:2; the angelic-mediated word was bebaios -- solid, legally binding, dependable; the author is not dismissing the Torah but affirming its authority before showing what surpasses it)",
            "bebaiōsis (confirmation/validation -- the word-group appears at 6:16 for oaths that confirm covenants; the angelic mediation produced a legally confirmed covenant)",
            "mesites (mediator -- the concept underlying Heb 2:2; Gal 3:19 uses mesites explicitly; Moses is the human mediator, angels are the divine tier of the same mediation structure)",
            "huiou (son -- 2:6; when the author quotes Psalm 8:4 'what is man... the son of man,' he immediately identifies Jesus as the fulfillment of this psalm in v.9)",
            "elattoo (made lower -- 2:7,9; from elachistos 'least/smallest'; the Son was made 'a little lower (brachy ti) than the angels'; this is the incarnational descent below the council level)",
            "doxa kai time (glory and honor -- 2:7,9; the Son is now crowned with glory and honor because of his death; the descent below the council leads to the exaltation above it)",
            "aionos mellousa (the world to come -- 2:5; it was not to angels that God subjected the coming age; the ekklesia's cosmic assignment, not the council's, governs the new creation)",
            "katargeō (to nullify/destroy -- 2:14; through death the Son 'destroyed' the one who has the power of death -- another council-level figure, the Adversary)",
            "archegos (pioneer/founder -- 2:10; the Son as the archegos of salvation; he goes first, blazing the path through death and resurrection that the many sons will follow)"
        ],

        "ane_backdrop": (
            "The concept of divine intermediaries delivering cosmic decrees to "
            "humanity was standard in the ancient Near East. In Mesopotamia, the "
            "personal god (ilu) served as an individual's divine advocate and "
            "message-bearer between the cosmic gods and humanity. The Akkadian "
            "term for a divine messenger was malaku (cognate to Hebrew malak, "
            "'angel/messenger'), and these figures populated the divine assembly "
            "as the administrative arm of the divine council's decisions. In "
            "Ugaritic texts, El dispatches divine messengers (mlak) to deliver "
            "his decrees to humans and lesser deities. The pattern -- supreme "
            "deity governs through a council, council acts through messengers, "
            "messengers deliver authoritative decrees to humanity -- is the "
            "standard divine governance model across the ANE. Israel's law-at-"
            "Sinai tradition fits this pattern exactly: YHWH decrees, the angelic "
            "council mediates, Moses receives. Hebrews 2 does not dispute the "
            "pattern; it says a new mediatorial structure has superseded it "
            "because the mediator is now not an angelic council member but "
            "the divine Son who created the council."
        ),

        "second_temple": [
            {
                "source": "Josephus, Antiquities 15.136 -- The Law Through Angels",
                "summary": (
                    "Josephus writes that 'we have learned the noblest of our "
                    "doctrines and the holiest of our laws through angels sent "
                    "from God.' This is consistent attestation of the angelic "
                    "mediation of Torah in Second Temple Judaism outside of "
                    "the NT -- a non-polemical, straightforward statement that "
                    "the law came through divine messengers."
                ),
                "relevance": (
                    "The tradition of angelic Torah mediation was not controversial "
                    "in Second Temple Judaism -- it was simply assumed. Hebrews 2:2 "
                    "is not making an unusual claim when it calls the Mosaic "
                    "covenant 'the message declared by angels.' It is citing "
                    "a well-established framework and then arguing from within "
                    "it: if even the angelic-mediated word was this binding and "
                    "reliable, how much more accountable are those who neglect "
                    "the word mediated by the Son himself?"
                )
            },
            {
                "source": "Acts 7:38,53 -- Stephen's Speech on Angelic Mediation",
                "summary": (
                    "Stephen's speech before the Sanhedrin explicitly states that "
                    "Moses 'received living oracles to give to us' (7:38) and that "
                    "the people 'received the law as delivered by angels and did "
                    "not keep it' (7:53). This is the same tradition Hebrews draws "
                    "on, coming from a different NT author confirming its widespread "
                    "acceptance in the early church."
                ),
                "relevance": (
                    "Acts 7:53 and Hebrews 2:2 are independent witnesses to the "
                    "same tradition: the Torah came through angelic mediation. "
                    "This tradition is also reflected in Galatians 3:19 (Paul) "
                    "and Deuteronomy 33:2 (LXX) which mentions 'angels with him' "
                    "at Sinai. The convergence of multiple independent witnesses "
                    "from different authors and contexts confirms this was not "
                    "a fringe interpretation."
                )
            },
            {
                "source": "1 Enoch 89:36-38 -- Angels Overseeing the Nations",
                "summary": (
                    "According to 1 Enoch, the nations are assigned to angelic "
                    "shepherds who both govern and are accountable for their "
                    "flocks. The seventy angelic shepherds of the nations parallel "
                    "the Deuteronomy 32:8 tradition and suggest an active "
                    "angelic administrative tier between God and humanity."
                ),
                "relevance": (
                    "According to 1 Enoch, the divine council's administrative "
                    "role extended beyond Torah mediation to ongoing national "
                    "governance. This supports the Hebrews argument: if angels "
                    "mediated the old covenant structure (Torah + national "
                    "governance), then a covenant mediated by the Son who created "
                    "the angels and stands above them represents a fundamental "
                    "upgrade in the redemptive order, not merely a refinement."
                )
            }
        ],

        "cross_refs": [
            {"ref": "Galatians 3:19", "note": "'The law was put in place through angels by an intermediary' -- Paul's direct confirmation of the angelic mediation of Torah; the intermediary is Moses, the angels are the divine tier", "type": "nt"},
            {"ref": "Acts 7:53", "note": "Stephen: 'you who received the law as delivered by angels' -- independent NT confirmation of the same tradition Hebrews 2:2 draws on", "type": "nt"},
            {"ref": "Deuteronomy 33:2 (LXX)", "note": "The LXX reads 'at his right hand angels were with him' at the Sinai theophany -- the tradition that angels were present and active in the law-giving", "type": "ot"},
            {"ref": "Psalm 8:4-6", "note": "Quoted in Heb 2:6-8: 'what is man... you made him a little lower than the angels, crowned him with glory and honor' -- the Son fulfills this psalm through incarnation and exaltation", "type": "ot"},
            {"ref": "Hebrews 2:14-15", "note": "The Son shared flesh and blood to 'destroy (katargeo) the one who has the power of death, that is, the devil' -- the cosmic warfare dimension of the incarnation", "type": "nt"},
            {"ref": "Colossians 2:14-15", "note": "'Disarming the rulers and authorities' through the cross -- Paul's parallel to Hebrews' argument that the Son's work reconfigures the divine council hierarchy", "type": "nt"},
            {"ref": "Hebrews 2:5", "note": "'It was not to angels that God subjected the world to come' -- the coming age is placed under the Son and the sons, not the divine council members", "type": "nt"},
            {"ref": "1 Peter 1:12", "note": "Angels 'longing to look' into the salvation announced through the prophets -- the divine council members themselves do not fully comprehend the redemptive plan entrusted to the ekklesia", "type": "nt"}
        ],

        "divine_council_note": (
            "Hebrews 2 makes an argument that is invisible unless the divine "
            "council framework is operative. The logic runs: (1) The Mosaic "
            "covenant was mediated through angelic council members. (2) Even "
            "this angelic-mediated covenant was so reliable and binding that "
            "every violation received just punishment. (3) The Son is superior "
            "to every angel (established in chapter 1). (4) Therefore, a "
            "covenant mediated through the Son is superior to the Mosaic "
            "covenant by the same ratio that the Son is superior to the angels. "
            "(5) Neglecting this greater covenant brings greater accountability. "
            "This argument only works if the divine council hierarchy is real: "
            "if there is no genuine angelic mediation of Torah, the comparison "
            "collapses. The angelic council members' role in the old covenant "
            "was not a theological embarrassment to be minimized -- it was the "
            "very thing that made the argument for the new covenant compelling."
            "\n\n"
            "Verse 5 introduces the cosmic governance dimension of the ekklesia: "
            "'it was not to angels that God subjected the world to come (ten "
            "oikoumenen ten mellousan).' The divine council managed the present "
            "age -- the Deuteronomy 32 assignment of nations to the bene elohim. "
            "But the coming age -- the new creation, the world to come -- is "
            "not assigned to the council. It is assigned to the Son and through "
            "him to the sons (v.10). This is the cosmic scope of 1 Corinthians "
            "6:3 ('do you not know that we are to judge angels?') and Ephesians "
            "3:10 ('through the church the manifold wisdom of God might now be "
            "made known to the rulers and authorities in the heavenly places'). "
            "The ekklesia is not simply a gathering for worship -- it is the "
            "governing body of the coming age, the replacement administrative "
            "structure that supersedes the old Deut 32 assignment."
        ),

        "sections": [
            {
                "heading": "The Angelic Mediation of Torah: Not a Fringe Idea (2:1-2)",
                "body": (
                    "Hebrews 2 opens with a warning from the logic of chapter 1: "
                    "'For since the message declared by angels proved to be reliable "
                    "(bebaios), and every transgression or disobedience received a "
                    "just retribution...' (2:2). The argument is a fortiori -- lesser "
                    "to greater. It only works if the angelic mediation of Torah is "
                    "real and not diminished. The author is not embarrassed by the "
                    "tradition; he weaponizes it. That angelic-mediated word was "
                    "bebaios -- firm, legally binding. Its reliability produced "
                    "accountability: every transgression received just punishment."
                    "\n\n"
                    "The tradition is confirmed at multiple independent points: "
                    "Galatians 3:19 ('the law was put in place through angels'), "
                    "Acts 7:53 ('you received the law as delivered by angels'), "
                    "Deuteronomy 33:2 LXX ('angels were with him' at Sinai), and "
                    "Josephus (Antiquities 15.136). The Second Temple world broadly "
                    "understood Sinai Torah as mediated through divine council "
                    "members. Hebrews 2:2 is not introducing novel theology -- it "
                    "is citing an established framework as the premise for an "
                    "argument about what superseded it."
                )
            },
            {
                "heading": "The Son Beneath the Council -- and Then Above It (2:5-9)",
                "body": (
                    "Verses 5-9 deploy Psalm 8:4-6 with precision. The psalm asks: "
                    "'You made him for a little while lower than the angels (brachy "
                    "ti par' angelous); you have crowned him with glory and honor, "
                    "putting everything in subjection under his feet.' The phrase "
                    "brachy ti -- 'a little lower' or 'for a little while lower' -- "
                    "is deliberately ambiguous. Hebrews seizes both meanings. The "
                    "Son was made lower than the angels in the incarnation -- he "
                    "entered the human domain that sits below the divine council "
                    "tier in the cosmic hierarchy -- 'for a little while,' the "
                    "brief period of his earthly life and death."
                    "\n\n"
                    "Verse 9 applies this: 'But we see him who for a little while "
                    "was made lower than the angels, namely Jesus, crowned with "
                    "glory and honor because of the suffering of death.' The "
                    "descent is not a defeat -- it is the mechanism of the "
                    "exaltation. He goes below the council, enters death, destroys "
                    "it from the inside (v.14), and rises to the position above "
                    "every name (Phil 2:9-11). The movement is down and then up "
                    "-- but 'up' means above the level from which he descended, "
                    "not merely a return."
                )
            },
            {
                "heading": "The World to Come Is Not for Angels (2:5)",
                "body": (
                    "One verse carries enormous weight: 'It was not to angels that "
                    "God subjected the world to come (ten oikoumenen ten mellousan)' "
                    "(2:5). The present age was assigned to the bene elohim at Babel "
                    "(Deut 32:8) -- nations under divine overseers, Israel remaining "
                    "YHWH's direct inheritance. That is the Deuteronomy 32 worldview: "
                    "angelic council members administering the nations in varying "
                    "degrees of faithfulness and rebellion."
                    "\n\n"
                    "But the coming age -- the new creation, the kingdom that cannot "
                    "be shaken (12:28) -- is not assigned to the council. It is "
                    "assigned to the Son and the sons through him (2:10: 'bringing "
                    "many sons to glory'). The old arrangement (nations under angelic "
                    "oversight) gives way to the new (creation under the Son and the "
                    "sons). The ekklesia is not merely a spiritual gathering -- it is "
                    "the administrative body of the age to come, already partially "
                    "installed by the Son's enthronement."
                )
            },
            {
                "heading": "Destroying the One with Power Over Death (2:14-15)",
                "body": (
                    "The cosmic warfare dimension: 'Through death he might destroy "
                    "(katargeo) him who has the power of death, that is, the devil, "
                    "and deliver all those who through fear of death were subject "
                    "to lifelong slavery' (2:14-15). Katargeo means to render "
                    "inoperative, to disarm -- not annihilation. The devil "
                    "(diabolos -- the Adversary) appears in Job 1-2 as a divine "
                    "council member who accuses the saints before God. His primary "
                    "weapon is death: he holds humanity in the fear of it and uses "
                    "that fear to maintain control."
                    "\n\n"
                    "The Son's strategy: enter the zone the Adversary controls -- "
                    "flesh and blood, mortality, death itself -- and dismantle it "
                    "from within. By undergoing death and rising, he renders "
                    "inoperative the Adversary's primary weapon. Colossians 2:14-15 "
                    "confirms: 'disarming the rulers and authorities and putting "
                    "them to open shame, by triumphing over them.' The cross is "
                    "a divine council event -- the Son confronts the rebellious "
                    "members on their own ground and defeats them."
                )
            }
        ]
    },

    # ------------------------------------------------------------------
    # CHAPTER 3: THE TABERNACLE AS COUNCIL THRONE ROOM -- HEBREWS 8-9
    # ------------------------------------------------------------------
    {
        "id": "heb-council-3",
        "ref": "Hebrews 8:1-9:28",
        "chapter_num": 3,
        "title": "The Tabernacle as Council Throne Room -- The Copy and the Real",
        "era": "hebrews_council",
        "type": "chapter",
        "themes": ["DC", "TYPE", "BLOOD", "PRIEST", "REBEL"],

        "synopsis": (
            "Hebrews 8-9 develops the tabernacle typology with a claim that only "
            "makes sense in the divine council framework: the earthly sanctuary "
            "is a 'copy and shadow of the heavenly things' (8:5). [A] The heavenly "
            "original that the tabernacle copies is the divine throne room -- the "
            "council chamber of Ezekiel 1, Daniel 7, 1 Enoch 14, and Revelation "
            "4 -- the same throne room described with nearly identical vocabulary "
            "across 700 years of tradition. [B] The cherubim on the ark are not "
            "decorative; they represent the divine council members flanking "
            "YHWH's throne (Ezek 10), and the Holy of Holies is the earthly "
            "representation of the council's inner chamber. [A] Hebrews 9:23-24 "
            "states that 'the heavenly things themselves' needed purification "
            "through better sacrifices -- an extraordinary claim that Christ's "
            "work addressed not only human sin but the defilement of the "
            "heavenly realm itself -- with Christ's entry into heaven being "
            "entry into the real divine council throne room."
        ),

        "key_verse": {
            "ref": "Hebrews 8:5",
            "text": "They serve a copy and shadow of the heavenly things. For when Moses was about to erect the tent, he was instructed by God, saying, 'See that you make everything according to the pattern that was shown you on the mountain.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "antitypon (copy/antitype -- 9:24; the earthly sanctuary is the antitypon -- the corresponding copy -- of the true heavenly original; typology in Hebrews is always historical, not allegorical)",
            "typos (pattern -- 8:5; Moses was shown the typos on the mountain; the earthly tabernacle was constructed according to a heavenly blueprint, implying the heavenly original exists)",
            "skia (shadow -- 8:5; 10:1; the Mosaic system is a skia -- a shadow cast by the heavenly substance; a shadow implies a solid object producing it)",
            "eikōn (image/true form -- 10:1; the law has a shadow of good things to come, not the eikon itself; Hebrews here distinguishes three levels: shadow, image, reality)",
            "ouranios (heavenly -- 8:5; ta epourania = 'the heavenly things'; the sanctuary is in the heavens, where the divine council throne room is located in all four major vision texts)",
            "hagion (sanctuary/holy place -- 9:24; Christ entered not the earthly hagion but the true one -- heaven itself -- 'now to appear in the presence of God on our behalf')",
            "katharizo (to purify/cleanse -- 9:23; the heavenly things themselves (ta epourania) needed katharizo; the defilement of the heavenly realm by cosmic rebellion required cosmic purification)",
            "ephapax (once for all -- 9:12; Christ offered himself ephapax -- a single unrepeatable act of sacrifice; the Levitical repetition was the shadow; the ephapax is the substance)",
            "mesites (mediator -- 9:15; 12:24; Christ is the mesites of a new covenant; a mediator requires two parties and an issue requiring resolution; the issue is cosmic, not merely legal)",
            "aiōnion lytrōsin (eternal redemption -- 9:12; not temporary atonement requiring annual repetition but eternal -- aionion -- liberation; the scope matches the cosmic scale of the problem)"
        ],

        "ane_backdrop": (
            "The concept of the earthly temple as a replica of the heavenly palace "
            "was universal in the ancient Near East. The Akkadian term for a temple "
            "was bitu (house), and the cosmic house of the gods was the model after "
            "which earthly temples were designed. In the Enuma Elish, after Marduk's "
            "victory, the gods build Esagila -- 'the house whose head is raised on "
            "high' -- as the earthly counterpart to Marduk's heavenly palace. The "
            "Ugaritic texts describe El's dwelling at 'the source of the two rivers, "
            "in the midst of the fountains of the two deeps' -- a cosmic mountain "
            "sanctuary that earthly temples reproduced in miniature. Egyptian temples "
            "were called 'the horizon of heaven' and oriented to align with cosmic "
            "realities. In all these traditions, the earthly sanctuary was understood "
            "not as a human construction honoring a deity but as the designated "
            "meeting point between the heavenly and earthly realms -- a portal "
            "where the cosmic throne room and the human world intersected. Israel's "
            "tabernacle / temple stands in this same tradition, but with a crucial "
            "distinction: the heavenly original is not the palace of one god among "
            "many but the throne room of the creator who transcends the council."
        ),

        "second_temple": [
            {
                "source": "1 Enoch 14:8-25 -- Enoch's Vision of the Heavenly Throne Room",
                "summary": (
                    "According to 1 Enoch, Enoch is taken in vision to the heavenly "
                    "throne room, which he describes in terms nearly identical to "
                    "Ezekiel 1 and Daniel 7: a house of crystal, a floor of fire, "
                    "a second inner house greater than the first, a throne of fire "
                    "with 'wheels like the shining sun,' and the Great Glory seated "
                    "on the throne, too bright to look upon. Angels approach but "
                    "cannot enter the inner house; only Enoch is invited to draw "
                    "near."
                ),
                "relevance": (
                    "According to 1 Enoch, the heavenly throne room is the original "
                    "of which the tabernacle's two-chamber structure (outer court + "
                    "Holy of Holies) is a copy. The same pattern -- outer accessible "
                    "space, inner chamber of the divine presence, only the designated "
                    "priest entering the inner sanctum -- appears in both the earthly "
                    "sanctuary and 1 Enoch's heavenly vision. Hebrews 8:5 draws on "
                    "this tradition when it calls the tabernacle 'a copy and shadow "
                    "of the heavenly things.'"
                )
            },
            {
                "source": "Songs of the Sabbath Sacrifice (4Q400-407) -- The Heavenly Sanctuary",
                "summary": (
                    "The Qumran Songs of the Sabbath Sacrifice describe the heavenly "
                    "sanctuary in elaborate detail: the 'holy of holies' in heaven, "
                    "the angelic priests who minister there, the 'living divine "
                    "chariots' (merkabah), and the structure of the heavenly council "
                    "throne room. The earthly Sabbath liturgy was understood as "
                    "participation in the heavenly worship that never ceases."
                ),
                "relevance": (
                    "The Qumran community understood the earthly sanctuary as "
                    "a copy of the heavenly one, and their liturgy as genuine "
                    "participation in the heavenly council's worship. This is "
                    "the same framework Hebrews 8 deploys when it calls the "
                    "tabernacle a 'shadow of the heavenly things' and Hebrews "
                    "12:22-24 develops when it describes the ekklesia's access "
                    "to the 'innumerable angels in festal gathering.'"
                )
            },
            {
                "source": "Ezekiel 1 / Daniel 7:9-14 -- The Four-Text Continuous Tradition",
                "summary": (
                    "Ezekiel 1 (the merkabah / divine chariot throne vision), Daniel "
                    "7:9-14 (the Ancient of Days on a throne of fire, the Son of Man "
                    "approaching), 1 Enoch 14 (Enoch's heavenly throne room), and "
                    "Revelation 4-5 (the throne room with four living creatures and "
                    "twenty-four elders) all describe the same heavenly reality "
                    "using the same vocabulary over a span of 700 years: fire, "
                    "glory, living creatures, wheels, the enthroned divine figure, "
                    "and the assembly before the throne."
                ),
                "relevance": (
                    "The heavenly things that the tabernacle copies is not "
                    "a vague Platonic 'ideal realm' -- it is this specific "
                    "throne room, described consistently across four major "
                    "texts. Hebrews 8:5 and 9:23-24 presuppose this "
                    "tradition. Christ's entry into heaven (9:24) is entry "
                    "into the real version of this specific room, and "
                    "his appearance 'in the presence of God on our behalf' "
                    "is his appearance before the enthroned Father in "
                    "the divine council throne room."
                )
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 25:40", "note": "'See that you make everything according to the pattern (tabnit) shown you on the mountain' -- quoted in Heb 8:5; the heavenly original already existed when Moses received the pattern", "type": "ot"},
            {"ref": "Ezekiel 1:4-28", "note": "The merkabah vision: the divine throne room with four living creatures, wheels, fire, and the divine glory -- the heavenly original of which the tabernacle is the copy", "type": "ot"},
            {"ref": "Daniel 7:9-10", "note": "The Ancient of Days on a throne of fire with the river of fire and ten thousand times ten thousand standing before him -- the council throne room in Daniel's vision", "type": "ot"},
            {"ref": "Revelation 4:2-11", "note": "John's throne room vision: twenty-four elders, four living creatures, the sea of glass, fire -- the same continuous tradition across all four texts", "type": "nt"},
            {"ref": "1 Enoch 14:8-25", "note": "According to 1 Enoch, Enoch's vision of the heavenly throne room in two-chamber structure matching the tabernacle's outer/inner design confirms the copy-and-original relationship", "type": "pseudepigrapha"},
            {"ref": "Hebrews 9:23", "note": "'It was necessary for the copies of the heavenly things to be purified with these rites, but the heavenly things themselves with better sacrifices' -- the heavenly realm itself required purification through Christ's work", "type": "nt"},
            {"ref": "Hebrews 9:24", "note": "'Christ has entered... into heaven itself, now to appear in the presence of God on our behalf' -- the ascension as entrance into the real divine council throne room", "type": "nt"},
            {"ref": "Colossians 1:20", "note": "'Through him to reconcile to himself all things, whether on earth or in heaven' -- Paul's parallel: the reconciliation scope is cosmic, including the heavenly realm", "type": "nt"}
        ],

        "divine_council_note": (
            "The divine council framework is not a lens imposed on Hebrews 8-9 "
            "from outside -- it is the explicit content of the argument. The "
            "tabernacle was built according to a 'pattern shown on the mountain' "
            "(8:5, quoting Exod 25:40). That pattern is the heavenly throne room "
            "-- the council chamber described across Ezekiel 1, Daniel 7, 1 Enoch "
            "14, and Revelation 4. The two-chamber structure (outer court for "
            "the priests, Holy of Holies for the high priest once a year) "
            "replicates the two-chamber structure of the heavenly throne room "
            "(outer courts where angels gather, inner chamber where the divine "
            "glory dwells). The cherubim on the ark are not decorative; they "
            "represent the divine council members -- the living creatures -- who "
            "flank YHWH's throne (Ezek 10:1-22)."
            "\n\n"
            "Hebrews 9:23 makes an extraordinary claim that only the council "
            "framework can absorb: the heavenly things themselves (ta epourania "
            "auta) needed purification with better sacrifices. If the heavenly "
            "throne room is purely pristine and untouched, why does it need "
            "purification? The answer is the cosmic defilement caused by "
            "the rebellion of the divine council members -- the Watchers of "
            "Genesis 6, the corrupt bene elohim of Psalm 82, the accuser of "
            "Job 1-2. The heavenly realm was contaminated by the rebellion "
            "of its own members. Christ's once-for-all sacrifice (9:12) "
            "purified not only human conscience (9:14) but the heavenly "
            "sanctuary itself -- the divine council chamber -- restoring "
            "the throne room to its proper order under the Son."
        ),

        "sections": [
            {
                "heading": "The Copy and the Heavenly Original (8:1-5)",
                "body": (
                    "Hebrews 8 opens: 'We have such a high priest, one who is seated "
                    "at the right hand of the throne of the Majesty in heaven, a "
                    "minister in the holy places, in the true tent that the Lord "
                    "set up, not man' (8:1-2). The contrast is direct: earthly "
                    "priests serve a man-made tent; Christ serves the Lord-made "
                    "original. Verse 5 cites Exodus 25:40: 'See that you make "
                    "everything according to the pattern (typos) shown you on "
                    "the mountain.' The typos implies a prior original that "
                    "existed and could be shown -- not an abstract concept "
                    "but a reality Moses was shown and then reproduced."
                    "\n\n"
                    "The heavenly throne room of Ezekiel 1, Daniel 7, 1 Enoch 14, "
                    "and Revelation 4 is this original. These four texts describe "
                    "the same heavenly reality with the same vocabulary across 700 "
                    "years: fire, the divine throne, living creatures (cherubim), "
                    "the assembly of thousands. The tabernacle was Moses' portable "
                    "rendering of this cosmic throne room -- fabric and acacia wood "
                    "and gold standing in for fire and glory and the council "
                    "assembly. The earthly Holy of Holies is the council's inner "
                    "chamber in miniature."
                )
            },
            {
                "heading": "The Cherubim: Council Members Flanking the Throne (9:1-5)",
                "body": (
                    "The sanctuary description in 9:1-5 is not architectural catalog "
                    "-- it is theological statement. The author notes the ark covered "
                    "by 'the cherubim of glory overshadowing the mercy seat' (9:5). "
                    "These cherubim are not decorative. In Ezekiel 10, the cherubim "
                    "are identified as the same living creatures of Ezekiel 1 -- the "
                    "divine council members flanking YHWH's throne, driving the "
                    "divine chariot. In Genesis 3:24, cherubim guard the tree of "
                    "life. In Ezekiel 28:14-16, the guardian cherub is the highest "
                    "council member whose fall occasions Satan's rebellion."
                    "\n\n"
                    "The cherubim on the ark represent the council members flanking "
                    "YHWH's actual throne. The mercy seat (hilasterion) between "
                    "them is the earthly representation of the divine throne -- the "
                    "place where YHWH appears and atonement is applied. When the "
                    "High Priest entered the Holy of Holies on Yom Kippur, he was "
                    "performing an earthly action corresponding to a heavenly "
                    "reality: approaching the divine throne flanked by the council, "
                    "making the annual atonement. Hebrews says Christ has done this "
                    "once for all in the real throne room."
                )
            },
            {
                "heading": "Purifying the Heavenly Things (9:23-24)",
                "body": (
                    "The most often overlooked statement in Hebrews 8-9 is 9:23: "
                    "'The heavenly things themselves (ta epourania auta) needed "
                    "better sacrifices.' The logic: the earthly copies needed "
                    "purification, therefore the heavenly originals also needed "
                    "purification -- but with better sacrifices than animal blood. "
                    "What does the heavenly throne room need purified from? The "
                    "divine council framework answers: the defilement caused by "
                    "the rebellion of the council members themselves."
                    "\n\n"
                    "The Watchers' corruption of humanity (Gen 6; 1 En 6-16), "
                    "the corrupt bene elohim condemned in Psalm 82, the Adversary's "
                    "accusations before the divine throne (Job 1-2) -- these are "
                    "cosmic defilements that contaminated the heavenly realm. The "
                    "Day of Atonement (Lev 16) in Second Temple tradition addressed "
                    "not merely Israel's sins but the Azazel dimension -- sins "
                    "returned to the imprisoned Watcher who originated them. "
                    "Christ's better sacrifice addressed the heavenly defilement "
                    "at its source, purifying the council's own throne room for "
                    "the new covenant access Hebrews 12:22-24 declares."
                )
            },
            {
                "heading": "Entering Heaven Itself (9:24-28)",
                "body": (
                    "Hebrews 9:24 states the conclusion of the tabernacle argument: "
                    "'For Christ has entered, not into holy places made with hands, "
                    "which are copies of the true things, but into heaven itself, "
                    "now to appear in the presence of God on our behalf.' The "
                    "ascension is not a disappearance -- it is an entry. Christ "
                    "entered the real divine council throne room, the heavenly "
                    "original of which the tabernacle was the copy, and now "
                    "appears (emphanisthenai) before God on behalf of his people."
                    "\n\n"
                    "The word emphanisthenai means to appear before, to present "
                    "oneself to -- the same word used for the Levitical high "
                    "priest appearing before YHWH in the Holy of Holies. But "
                    "where the earthly high priest appeared annually with animal "
                    "blood and then exited, Christ appeared once (ephapax -- v.26) "
                    "with his own blood and remains. He is perpetually present "
                    "in the divine throne room, permanently interceding (7:25 -- "
                    "'he always lives to make intercession for them'). The "
                    "ekklesia's access to God is access to the throne room of "
                    "the divine council, the same throne room Ezekiel saw, that "
                    "Daniel saw, that John saw -- and Christ is perpetually "
                    "present there as the mediator of the new covenant."
                )
            }
        ]
    },

    # ------------------------------------------------------------------
    # CHAPTER 4: THE HEAVENLY ASSEMBLY -- HEBREWS 12:18-29
    # ------------------------------------------------------------------
    {
        "id": "heb-council-4",
        "ref": "Hebrews 12:18-29",
        "chapter_num": 4,
        "title": "The Heavenly Assembly -- The Ekklesia Already There",
        "era": "hebrews_council",
        "type": "chapter",
        "themes": ["DC", "KING", "BLOOD", "HOLY", "LAW"],

        "synopsis": (
            "Hebrews 12:22-24 provides the most explicit NT description of the "
            "divine council assembly in session: Mount Zion, the heavenly Jerusalem, "
            "innumerable angels in festal gathering (panegyris), the ekklesia of "
            "the firstborn enrolled in heaven, God the judge of all, the spirits "
            "of the righteous made perfect, and Jesus the mediator. [A] The "
            "ekklesia is not headed toward this assembly -- it has already 'come "
            "to' it (proselelythate -- perfect tense, completed action). [B] The "
            "term ekklesia here carries its full political weight: the governing "
            "assembly of citizens, the body with authority to act -- not a "
            "religious gathering but a governing council. [A] Verses 25-29 then "
            "announce the cosmic shaking that removes everything not of the "
            "kingdom, including the corrupt heavenly powers, quoting Haggai 2:6 "
            "in connection with Isaiah 24:21-22's simultaneous judgment of "
            "heavenly and earthly powers."
        ),

        "key_verse": {
            "ref": "Hebrews 12:22-23",
            "text": "But you have come to Mount Zion and to the city of the living God, the heavenly Jerusalem, and to innumerable angels in festal gathering, and to the assembly of the firstborn who are enrolled in heaven...",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "proselelythate (you have come -- 12:22; perfect indicative, completed action; the ekklesia has already arrived at the heavenly assembly -- not 'you will come' but 'you have come'; present spiritual reality)",
            "panegyris (festal assembly/celebration -- 12:22; a Greek term for a great public gathering, a festival of the whole people; the angelic gathering at Mount Zion is a celebration, not a military muster)",
            "ekklesia (governing assembly -- 12:23; the term for the Greek democratic assembly of citizens with authority to act; here applied to the assembly of the firstborn enrolled in heaven)",
            "prototokos (firstborn -- 12:23; tes ekklesias prototokōn -- the assembly of the firstborn; first-born = highest rank, cosmic title; the ekklesia shares the Son's firstborn status)",
            "apographo (enrolled/registered -- 12:23; apographomenon en ouranois -- enrolled in the heavens; a civic registration term -- the ekklesia members are registered citizens of the heavenly city)",
            "Sion (Zion -- 12:22; the cosmic mountain, the dwelling of the divine council in OT theology; Ps 48, Ps 76, Isa 24-27; not merely Jerusalem but the throne-mountain of YHWH)",
            "seismos (shaking -- 12:26-27; the cosmic shaking that removes everything not of the kingdom; both earth and heaven are shaken to remove the unstable -- including corrupt heavenly powers)",
            "basileian asaleutan (unshakeable kingdom -- 12:28; in contrast to everything shaken and removed; the ekklesia receives the kingdom that cannot be shaken -- the new creation order)",
            "kriten theon panton (God the judge of all -- 12:23; one of the titles in the heavenly assembly description; God's presence in the assembly is as universal judge, consistent with Ps 82 and Dan 7)",
            "pneumata dikaion teteleiomenon (spirits of the righteous made perfect -- 12:23; the redeemed dead who are already present in the heavenly assembly; the cloud of witnesses of 12:1 now in the throne room itself)"
        ],

        "ane_backdrop": (
            "The divine assembly on the cosmic mountain was a central motif across "
            "the ancient Near East. In Ugaritic mythology, El's assembly met on "
            "Mount Lel ('Mount of the Night') or at 'the mount of assembly' "
            "(har mo'ed -- the same phrase in Isaiah 14:13 where the rebel "
            "Helel / Lucifer aspires to 'sit on the mount of assembly in the "
            "far reaches of the north'). The Mesopotamian divine assembly "
            "convened in the great hall of the gods, with Marduk presiding from "
            "the ziggurat-mountain. Egypt's divine council met in Heliopolis, "
            "the 'house of the sun,' identified with the primordial mound. In "
            "all cases, the cosmic mountain is the meeting point of heaven and "
            "earth, the place where divine governance decisions are made and "
            "decrees are issued to the human world. Israel's Zion theology "
            "participates in this pattern (Psalms 46-48, 76; Isaiah 2:2-4; "
            "Micah 4:1-4) but transforms it: Zion is not one cosmic mountain "
            "among many but the unique dwelling of the creator-God, the place "
            "from which his law goes out to all nations. Hebrews 12:22 "
            "declares the ekklesia has already arrived at this assembly."
        ),

        "second_temple": [
            {
                "source": "Book of Giants (4Q530) -- Heavenly Enrollment and Tablets",
                "summary": (
                    "The Dead Sea Scrolls Book of Giants describes heavenly tablets "
                    "on which names and deeds are recorded before the divine council. "
                    "The concept of enrollment in a heavenly book of citizens parallels "
                    "the Hebrews 12:23 description of the ekklesia as 'enrolled in "
                    "heaven' (apographomenon en ouranois). Daniel 12:1 also speaks "
                    "of 'everyone whose name shall be found written in the book.'"
                ),
                "relevance": (
                    "The concept of heavenly civic enrollment -- being a registered "
                    "citizen of the divine council's city -- was alive in Second "
                    "Temple Judaism. Hebrews 12:23's apographomenon en ouranois "
                    "is not metaphorical: it draws on the tradition of the heavenly "
                    "book of the living in which the names of the redeemed are "
                    "recorded before the divine assembly. The ekklesia are "
                    "enrolled citizens of the heavenly city, not merely "
                    "spiritual sojourners."
                )
            },
            {
                "source": "Songs of the Sabbath Sacrifice (4Q400-407) -- Participating in Heavenly Worship",
                "summary": (
                    "The Qumran Sabbath Songs describe the earthly community's "
                    "worship as genuine participation in the ongoing worship of "
                    "the heavenly assembly. The community believed that during "
                    "their Sabbath liturgy they were co-worshiping with the angelic "
                    "council in the heavenly sanctuary -- the 'innumerable angels "
                    "in festal gathering' that Hebrews 12:22 describes."
                ),
                "relevance": (
                    "The Qumran community had developed a theology of present "
                    "heavenly participation through liturgy that closely parallels "
                    "Hebrews 12:22-24. Both communities -- Qumran and the Hebrews "
                    "recipients -- understood their earthly gathering as the "
                    "visible counterpart of an invisible heavenly assembly. "
                    "Hebrews 12 makes the same claim but grounds the access not "
                    "in Levitical purity but in the blood of Jesus (v.24)."
                )
            },
            {
                "source": "Isaiah 24:21-22 -- Simultaneous Judgment of Heaven and Earth",
                "summary": (
                    "Isaiah's cosmic judgment text states: 'On that day the LORD "
                    "will punish the host of heaven, in heaven, and the kings of "
                    "the earth, on the earth. They will be gathered together as "
                    "prisoners in a pit; they will be shut up in a prison, and "
                    "after many days they will be punished' (Isa 24:21-22). The "
                    "'host of heaven' refers to the divine council members who "
                    "have been corrupt -- judged simultaneously with the earthly "
                    "kings they corrupted."
                ),
                "relevance": (
                    "Hebrews 12:26-27 quotes Haggai 2:6 about the shaking of "
                    "heaven and earth in the context of the heavenly assembly. "
                    "Isaiah 24:21-22 provides the content of that shaking: the "
                    "corrupt heavenly powers are judged alongside the earthly "
                    "powers they governed. The 'removing of what is shaken' "
                    "(Heb 12:27) includes the corrupt elements of the divine "
                    "council -- the unshakeable kingdom that remains is the "
                    "one governed by the Son and the sons."
                )
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 12:22-24", "note": "The full heavenly assembly description: Mount Zion, heavenly Jerusalem, angels in festal gathering, the ekklesia enrolled in heaven, God the judge, spirits of the righteous, Jesus the mediator", "type": "nt"},
            {"ref": "Psalm 82:1", "note": "'God has taken his place in the divine council; in the midst of the gods he holds judgment' -- the Ps 82 judgment on the corrupt bene elohim is in view in Heb 12:23's 'God the judge of all'", "type": "ot"},
            {"ref": "Isaiah 24:21-22", "note": "'The LORD will punish the host of heaven, in heaven, and the kings of the earth, on the earth' -- the simultaneous judgment of heavenly and earthly powers; connected to Heb 12:26-27's cosmic shaking", "type": "ot"},
            {"ref": "Haggai 2:6", "note": "'Yet once more I will shake not only the earth but also the heavens' -- quoted in Heb 12:26; the shaking removes everything not of the kingdom, including corrupt heavenly powers", "type": "ot"},
            {"ref": "Daniel 7:10", "note": "'A thousand thousands served him, and ten thousand times ten thousand stood before him; the court sat in judgment' -- the divine council in judicial session, corresponding to Heb 12:23's assembly", "type": "ot"},
            {"ref": "Revelation 21:2", "note": "'The holy city, new Jerusalem, coming down out of heaven from God' -- the same heavenly Jerusalem of Heb 12:22, the city the ekklesia has already 'come to' in the present", "type": "nt"},
            {"ref": "Ephesians 3:10", "note": "'Through the church the manifold wisdom of God might now be made known to the rulers and authorities in the heavenly places' -- the ekklesia's present role in the cosmic governance structure", "type": "nt"},
            {"ref": "1 Corinthians 6:3", "note": "'Do you not know that we are to judge angels?' -- the ekklesia's cosmic juridical assignment, consistent with Heb 12:23's governance assembly language", "type": "nt"},
            {"ref": "Isaiah 14:13", "note": "The rebel aspires to 'sit on the mount of assembly (har mo'ed) in the far reaches of the north' -- the same cosmic mountain assembly the ekklesia has already legitimately entered through Christ", "type": "ot"}
        ],

        "divine_council_note": (
            "Hebrews 12:22-24 is the most explicit NT description of the divine "
            "council assembly as the present spiritual reality of the ekklesia. "
            "The passage is not a prophecy about where believers will go -- it "
            "is a declaration about where they already are. Proselelythate is "
            "perfect tense: completed action with present results. The ekklesia "
            "has come (and remains present) at the heavenly assembly. The seven "
            "elements of the assembly are listed in order: the cosmic mountain "
            "throne (Zion), the celestial city (heavenly Jerusalem), the loyal "
            "council members in celebration (innumerable angels in panegyris), "
            "the human governance assembly (ekklesia of the firstborn, enrolled "
            "as citizens), the divine judge (God the judge of all), the "
            "redeemed dead (spirits of the righteous made perfect), and the "
            "mediator (Jesus, the mediator of a new covenant)."
            "\n\n"
            "The term ekklesia in verse 23 carries its full weight. In Greek "
            "political usage, the ekklesia was the governing assembly of free "
            "male citizens who made binding decisions for the polis. When Paul "
            "uses it in Ephesians 3:10 -- 'through the church the manifold "
            "wisdom of God might now be made known to the rulers and authorities "
            "in the heavenly places' -- and when he asks in 1 Corinthians 6:3 "
            "'do you not know that we are to judge angels?' -- he is drawing on "
            "the same concept Hebrews 12:23 makes explicit: the ekklesia is "
            "the governing assembly of the new covenant, already enrolled in "
            "the heavenly city, already participating in the council's "
            "deliberations, already positioned for the cosmic governance "
            "role that the coming age will fully manifest."
            "\n\n"
            "Verses 25-29 introduce the final shaking of the cosmic structure: "
            "everything that can be shaken will be removed, and 'what cannot "
            "be shaken will remain' (12:27). This shaking removes not only "
            "earthly institutions but the corrupt elements of the divine "
            "council itself -- the heavens as well as the earth (v.26). "
            "Isaiah 24:21-22 is the OT parallel: on that day, the host of "
            "heaven is punished in heaven simultaneously with the kings of "
            "the earth. The prophecy matrix entry P055 -- 'The LORD Punishes "
            "the Powers in the Heavens' -- is partially fulfilled; its full "
            "realization is what Hebrews 12:26-28 anticipates."
        ),

        "sections": [
            {
                "heading": "You Have Already Come: Present Access to the Heavenly Assembly (12:18-22)",
                "body": (
                    "Hebrews 12 constructs a deliberate contrast between Sinai and "
                    "Zion. The Sinai account is terrifying: tangible fire, darkness, "
                    "gloom, tempest, the blast of a trumpet, a voice whose words "
                    "made the hearers beg that no further message be spoken, and "
                    "the command that even an animal touching the mountain should "
                    "be stoned (12:18-21). Moses himself said, 'I tremble with "
                    "fear' (12:21, quoting Deut 9:19). This was the old covenant "
                    "mountain -- awe-inspiring, yes, but ultimately unapproachable. "
                    "The divine presence was there, but access was limited by the "
                    "angelic-mediated covenant structure."
                    "\n\n"
                    "'But you have come to Mount Zion' (12:22). The word proselelythate "
                    "is perfect tense -- 'you have come and are present.' This is not "
                    "future hope; it is current reality. The ekklesia has arrived at "
                    "a different mountain: not the earthly Sinai but the cosmic "
                    "Zion, the throne-mountain of the divine council. Psalm 48 "
                    "celebrates Zion as 'the city of the great King... the joy "
                    "of all the earth.' Isaiah 2:2-4 sees all nations streaming "
                    "to Zion for Torah. The believers addressed by Hebrews are "
                    "not approaching this mountain -- they are already there, "
                    "by virtue of Christ's work as mediator of the new covenant."
                )
            },
            {
                "heading": "Seven Elements of the Heavenly Assembly (12:22-24)",
                "body": (
                    "The author lists seven elements of the heavenly assembly in "
                    "12:22-24 with the precision of someone mapping a real "
                    "geography: (1) Mount Zion -- the cosmic throne-mountain, "
                    "YHWH's dwelling, the divine council's meeting place. "
                    "(2) The city of the living God, the heavenly Jerusalem -- "
                    "the polis of which the ekklesia are enrolled citizens "
                    "(apographomenon -- registered in the civic rolls). (3) "
                    "Innumerable angels in festal gathering (panegyris) -- "
                    "the loyal divine council members in celebration; panegyris "
                    "is a festival, not a military assembly; the loyal council "
                    "is in worship, not in dread. (4) The assembly (ekklesia) "
                    "of the firstborn enrolled in heaven -- the human governing "
                    "assembly, bearing the firstborn title (prototokos) that "
                    "signals cosmic rank and authority. (5) God, the judge of "
                    "all -- present in the assembly as the universal judge; "
                    "this is Psalm 82's 'God has taken his place in the "
                    "divine council' fulfilled eschatologically. (6) The "
                    "spirits of the righteous made perfect -- the redeemed "
                    "dead, present in the assembly. (7) Jesus, the mediator "
                    "of a new covenant -- the one through whom access to "
                    "this entire assembly is granted."
                )
            },
            {
                "heading": "Enrolled in Heaven: The Ekklesia's Civic Status (12:23)",
                "body": (
                    "The term apographomenon en ouranois -- 'enrolled in the "
                    "heavens' -- is a civic registration term. In the Greco-Roman "
                    "world, apographo was the word for the census, for citizen "
                    "registration, for enrollment on the official rolls of a "
                    "city-state. Luke 2:1 uses the same root for the census "
                    "that brought Joseph and Mary to Bethlehem. To be enrolled "
                    "in heaven is to be a registered citizen of the heavenly "
                    "city, with all the rights and responsibilities of citizenship "
                    "in that polis. Philippians 3:20 draws on the same concept: "
                    "'our citizenship (politeuma) is in heaven.' This is not "
                    "sentimental -- it is constitutional."
                    "\n\n"
                    "The heavenly enrollment connects to the tradition of the "
                    "heavenly book seen in Exodus 32:32-33 (Moses asks to be "
                    "blotted from God's book), Psalm 69:28 ('let them be "
                    "blotted out of the book of the living'), Daniel 12:1 "
                    "('everyone whose name shall be found written in the book'), "
                    "and Revelation 21:27 ('only those who are written in the "
                    "Lamb's book of life'). The Book of Giants (4Q530) from "
                    "Qumran also references heavenly tablets of enrollment. The "
                    "ekklesia's names are in that book -- they are registered "
                    "citizens of the council's governing city."
                )
            },
            {
                "heading": "The Cosmic Shaking and What Cannot Be Shaken (12:25-29)",
                "body": (
                    "Hebrews 12:25-29 is framed in cosmic governance terms: 'For "
                    "if they did not escape when they refused him who warned them "
                    "on earth (Sinai), much less will we escape if we reject him "
                    "who warns from heaven.' The a fortiori argument of chapter 2 "
                    "returns: angelic-mediation had consequences; the Son's "
                    "direct word has greater ones."
                    "\n\n"
                    "Then the cosmic announcement: 'Yet once more I will shake "
                    "not only the earth but also the heavens' (12:26, Haggai 2:6). "
                    "This shaking removes the current cosmic governance structure. "
                    "Isaiah 24:21-22 identifies what is shaken: 'the host of "
                    "heaven, in heaven' -- the corrupt divine council members, "
                    "judged simultaneously with the earthly kings they corrupted. "
                    "The judgment is simultaneous: heaven and earth fall together. "
                    "What remains is the unshakeable kingdom (basileian asaleutan, "
                    "12:28) -- the governance order of the Son and the sons. This "
                    "is the kingdom the ekklesia already participates in through "
                    "their enrollment in the heavenly assembly."
                )
            }
        ]
    },

    # ------------------------------------------------------------------
    # CHAPTER 5: HISTORICAL INSERT -- FROM ANGELS TO THE SON
    # ------------------------------------------------------------------
    {
        "id": "heb-council-insert-1",
        "ref": "Historical Context",
        "chapter_num": None,
        "title": "Historical Insert: From Angels to the Son -- Why the Mediator Matters",
        "era": "hebrews_council",
        "type": "historical_insert",
        "themes": ["DC", "PRIEST", "COV", "TYPE", "SEED"],

        "synopsis": (
            "The entire argument of Hebrews rests on a real hierarchy: Torah "
            "came through angelic council members (real, reliable, authoritative), "
            "and the new covenant comes through the Son who created the council. "
            "This insert traces the thread from Deuteronomy 32's assignment of "
            "nations to divine council members, through the Qumran 11QMelchizedek "
            "text that shows Second Temple Judaism already wrestling with the "
            "need for a superior heavenly mediator, to Hebrews' identification "
            "of Jesus as the one who holds that position. The tradition is not "
            "Hebrews' invention -- it was already present in the DSS and the "
            "Enoch literature. Hebrews identifies the person."
        ),

        "key_verse": {
            "ref": "Hebrews 7:16-17",
            "text": "who has become a priest, not on the basis of a legal requirement concerning bodily descent, but by the power of an indestructible life. For it is witnessed of him, 'You are a priest forever, after the order of Melchizedek.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "mēsitēs (mediator -- Heb 8:6; 9:15; 12:24; from mesos 'middle' + a verb of action; a mediator stands between two parties and facilitates their relationship; the question Hebrews answers is: which mediator has sufficient standing?)",
            "Melchizedek (malki-tsedeq -- 'king of righteousness' or 'my king is righteousness'; Heb 7:2 parses the name; also 'king of Salem' = 'king of peace'; priest-king who predates the Levitical system)",
            "engyos (guarantor -- Heb 7:22; used only here in the NT; Christ is the personal guarantee of the better covenant; his indestructible life is staked on its fulfillment)",
            "akatalutos (indestructible -- Heb 7:16; the basis of Christ's priesthood; not biological descent but 'the power of an indestructible life'; the council argument requires a mediator who cannot die)",
            "teleios (perfect/complete/mature -- Heb 7:11; the perfection the Levitical priesthood could not achieve; the Son was 'made perfect through suffering' (Heb 2:10), qualifying him as the mediator the covenant required)",
            "11QMelchizedek (the DSS text that identifies Melchizedek as a heavenly elohim figure executing Psalm 82 judgment; bridges the Hebrews 7 argument and the divine council framework directly)",
            "bene elohim (sons of God -- the divine council members; the beings who mediated Torah; the beings the Son is superior to; the beings commanded to worship him in Deut 32:43 DSS/LXX)",
            "rosh ha-shanah (the coming Day of Atonement -- Lev 16; Yom Kippur; the annual re-enactment of the cosmic purification that Christ's single offering accomplished permanently; Heb 9:6-14)",
            "Azazel (the specific imprisoned Watcher to whom the scapegoat was sent -- Lev 16:8-26; the sins were sent back to their originator; the Day of Atonement had a cosmic council dimension)",
            "sha'ar (gate/assembly-point -- in ANE tradition, the gate was the place of civic assembly and judgment; the heavenly council assembled at the gate; the ekklesia's assembly is at the gate of the heavenly city)"
        ],

        "ane_backdrop": None,

        "second_temple": [
            {
                "source": "11QMelchizedek (11Q13) -- The Heavenly Mediator Tradition at Qumran",
                "summary": (
                    "The Dead Sea Scrolls text 11QMelchizedek presents Melchizedek "
                    "as a heavenly divine being (elohim) who presides over the "
                    "eschatological Day of Atonement, executing the Psalm 82 "
                    "judgment on the corrupt bene elohim. He is 'the god' (ha-elohim) "
                    "of Psalm 82:1 who stands to judge in the divine council. He "
                    "proclaims the year of the LORD's favor, releases captives, and "
                    "atones for the sins of the righteous. The text quotes Isaiah "
                    "52:7 ('how beautiful upon the mountains are the feet of him "
                    "who brings good news') and applies it to Melchizedek."
                ),
                "relevance": (
                    "The Qumran community was already developing a theology of a "
                    "heavenly mediator figure -- distinct from YHWH but of divine "
                    "council rank (elohim-level) -- who would execute final "
                    "judgment on the corrupt council members and redeem the "
                    "righteous. This is the exact theological need Hebrews "
                    "addresses when it presents Jesus as the Melchizedekian "
                    "high priest. Without 11QMelchizedek, Hebrews 7 is profound "
                    "but partial; with it, the argument gains its full cosmic "
                    "weight. The author of Hebrews was writing to a community "
                    "that understood this tradition and needed to hear that "
                    "the figure the DSS tradition anticipated had arrived."
                )
            },
            {
                "source": "Galatians 3:19-20; Acts 7:53 -- The Angelic Mediation Framework in NT",
                "summary": (
                    "Both Paul (Galatians 3:19: 'the law was put in place through "
                    "angels by an intermediary') and Stephen (Acts 7:53: 'you "
                    "received the law as delivered by angels') independently "
                    "confirm the tradition of angelic Torah mediation in the "
                    "early church. This tradition was not controversial -- "
                    "it was assumed. The question was what it meant for "
                    "the new covenant."
                ),
                "relevance": (
                    "The Hebrews argument requires the angelic mediation tradition "
                    "to be real, accepted, and authoritative. If the Torah did "
                    "not come through angels, the comparison in 2:2-3 collapses. "
                    "The multiple independent NT witnesses confirm the tradition "
                    "was widespread and that the author of Hebrews was not "
                    "introducing novel theology but drawing on a shared "
                    "framework to make a new case: the Son is greater than "
                    "the angels who gave the law, therefore his covenant "
                    "is greater than the covenant they mediated."
                )
            },
            {
                "source": "1 Enoch 10:4-6 -- Azazel's Imprisonment and the Day of Atonement",
                "summary": (
                    "According to 1 Enoch, Azazel is bound by Raphael and cast "
                    "into the desert pit of Dudael, there to remain until the "
                    "day of judgment. The Leviticus 16 scapegoat ritual -- "
                    "sending the sins of Israel into the wilderness to Azazel "
                    "(16:8-26) -- is, in this tradition, returning the sins "
                    "to their originator, the imprisoned Watcher whose "
                    "corruption of humanity they represent."
                ),
                "relevance": (
                    "According to 1 Enoch, the Day of Atonement's Azazel ritual "
                    "had a divine council dimension: the cosmic source of the "
                    "corruption (a specific Watcher) was being held accountable "
                    "through the liturgical return of humanity's sins to him. "
                    "Hebrews 9-10's treatment of the Day of Atonement, the "
                    "heavenly tabernacle, and Christ's once-for-all sacrifice "
                    "addresses this same cosmic dimension. Christ's blood "
                    "purified the heavenly sanctuary (9:23) -- the council "
                    "chamber where the rebellion originated -- as well as "
                    "human conscience (9:14)."
                )
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 7:16", "note": "Jesus qualified not by biological descent but by 'the power of an indestructible life' -- the Melchizedekian priesthood requires a priest who cannot die, unlike any Levitical or angelic mediator", "type": "nt"},
            {"ref": "Hebrews 7:25", "note": "'He always lives to make intercession for them' -- the perpetual priestly mediation in the heavenly throne room; the council mediator is permanently present", "type": "nt"},
            {"ref": "11QMelchizedek (11Q13)", "note": "The DSS Melchizedek executes Psalm 82 judgment on corrupt divine council members in the eschatological Day of Atonement; Hebrews identifies Jesus as this figure", "type": "dss"},
            {"ref": "Psalm 82:1-8", "note": "'God stands in the divine council; among the gods he holds judgment... I said you are gods, sons of the Most High... but you shall die like men' -- the council judgment the 11QMelchizedek figure executes", "type": "ot"},
            {"ref": "Leviticus 16:8-26", "note": "The Azazel scapegoat ritual: sins sent to the imprisoned Watcher in the wilderness; the Day of Atonement had a cosmic/council dimension beyond its liturgical surface", "type": "ot"},
            {"ref": "1 Enoch 10:4-6", "note": "According to 1 Enoch, Azazel's imprisonment and the return of his sins through the scapegoat ritual gave the Day of Atonement its cosmic warfare context", "type": "pseudepigrapha"},
            {"ref": "Deuteronomy 32:8-9", "note": "'When the Most High gave to the nations their inheritance... he fixed the borders according to the number of the sons of God' (DSS/LXX) -- the cosmic assignment that Hebrews 1:6's worship command reverses", "type": "dss"},
            {"ref": "Isaiah 52:7", "note": "Quoted in 11QMelchizedek and applied to the heavenly mediator bringing good news -- the same connection Hebrews makes between the Melchizedekian priest-king and the new covenant proclamation", "type": "ot"},
            {"ref": "1 Corinthians 6:3", "note": "The ekklesia's assignment to judge angels -- the governing role that Hebrews 12:23 establishes through the enrollment language and that 11QMelchizedek anticipates through the council-judgment framework", "type": "nt"},
            {"ref": "Ephesians 1:21", "note": "Christ seated 'far above all rule and authority and power and dominion, and above every name that is named, not only in this age but also in the one to come' -- the full cosmic hierarchy the Hebrews argument establishes", "type": "nt"}
        ],

        "divine_council_note": (
            "The historical insert brings together the threads that the four "
            "study chapters lay out: the Son is above the council (ch.1), "
            "the angelic mediation of Torah was real and reliable (ch.2), "
            "the tabernacle is the earthly copy of the council throne room "
            "(ch.3), and the ekklesia is already enrolled in the heavenly "
            "council assembly (ch.4). The question this insert addresses is: "
            "what prepared the way for Hebrews to make this argument? The "
            "answer is 11QMelchizedek."
            "\n\n"
            "The Qumran community, working from the same DSS text tradition "
            "that Hebrews cites at 1:6 (Deut 32:43, 4QDeutq) and at 1:8-9 "
            "(various OT texts), developed a theology of a heavenly Melchizedek "
            "figure who would execute the Psalm 82 judgment on the corrupt "
            "divine council members and inaugurate the final Day of Atonement. "
            "He was not YHWH, but he was elohim-level -- a divine council "
            "member of supreme rank who would adjudicate the council's "
            "rebellion. The author of Hebrews writes to recipients who knew "
            "this tradition and answers the question the tradition left open: "
            "who is this Melchizedek? The answer is the Jesus who was "
            "qualified not by Levitical descent or angelic rank but by "
            "'the power of an indestructible life' (7:16) -- the one who "
            "underwent death and came out the other side, qualifying him "
            "as the eternal priest of the real Day of Atonement, the "
            "purifier of both human conscience and the heavenly sanctuary "
            "itself."
        ),

        "sections": [
            {
                "heading": "The Problem the Old System Could Not Solve",
                "body": (
                    "Hebrews 10:1 states the problem plainly: 'The law has but a "
                    "shadow (skian) of the good things to come; it can never, by "
                    "the same sacrifices offered every year, make perfect those "
                    "who draw near.' The annual repetition was the evidence of "
                    "its limitation: if the atonement had worked permanently, "
                    "the repetition would have stopped (10:2). The high priest "
                    "entered once a year and exited. The people remained outside. "
                    "The council throne room was represented but not entered."
                    "\n\n"
                    "But the problem ran deeper than liturgical repetition. The "
                    "cosmic source of the contamination -- the rebellion of the "
                    "divine council members, the Genesis 6 corruption, the ongoing "
                    "accusations of the Adversary in the council chamber -- was "
                    "not addressed by animal blood. The heavenly sanctuary itself "
                    "(ta epourania, Heb 9:23) needed purification. The problem "
                    "required a mediator who could operate at the council level, "
                    "address the defilement at its source, and permanently purify "
                    "both the human side and the heavenly side of the covenant."
                )
            },
            {
                "heading": "What 11QMelchizedek Reveals",
                "body": (
                    "11QMelchizedek (11Q13) is the most important Second Temple "
                    "background text for Hebrews 7. It presents Melchizedek as "
                    "a heavenly divine being -- an elohim -- who presides over "
                    "the final cosmic Day of Atonement. He is 'the god (ha-elohim) "
                    "of Psalm 82:1 who stands in the divine council to judge.' He "
                    "proclaims liberty to captives, releases debt-slaves of Belial, "
                    "and executes judgment on the corrupt council members. The text "
                    "quotes Isaiah 52:7 and applies it to this heavenly Melchizedek "
                    "-- the one bringing the good news of the final atonement."
                    "\n\n"
                    "Without 11QMelchizedek, Hebrews 7 is a profound priesthood "
                    "argument from Genesis 14. With it, Hebrews 7 is the "
                    "identification of the figure the Qumran community anticipated. "
                    "The author says: you know the tradition of the heavenly "
                    "Melchizedek who would judge the council's rebellion. That "
                    "figure is Jesus. He is qualified not by angelic rank but "
                    "by indestructible life -- he went through death and came "
                    "back, which no Levitical priest or divine council member "
                    "can do. His priesthood does not end."
                )
            },
            {
                "heading": "The Same Textual Tradition: Hebrews and Qumran",
                "body": (
                    "Hebrews' OT citations cluster in the same texts Qumran "
                    "intensively studied. The Deuteronomy 32 worldview (4QDeutq, "
                    "bene elohim in 32:8 and worship command in 32:43) appears "
                    "in Hebrews 1:6. The Psalm 82 council judgment framework "
                    "appears in the 11QMelchizedek context Hebrews 7 presupposes. "
                    "The heavenly tabernacle of the Songs of Sabbath Sacrifice "
                    "(4Q400-407) corresponds to Hebrews 8:5's 'copy and shadow.' "
                    "The Azazel dimension of the Day of Atonement connects to "
                    "1 Enoch 10:4-6, preserved by Qumran."
                    "\n\n"
                    "The author of Hebrews was not writing from a tradition "
                    "foreign to Second Temple Judaism -- he wrote from inside "
                    "the same textual world as Qumran and concluded: the "
                    "heavenly mediator your tradition anticipated has come. "
                    "The Torah through angels was real. The heavenly tabernacle "
                    "is real. The council assembly is real. The Melchizedekian "
                    "priest-king who would judge the corrupt bene elohim -- real. "
                    "His name is Jesus. His blood has purified the heavenly "
                    "sanctuary. You have come to his assembly."
                )
            },
            {
                "heading": "The Ekklesia's Cosmic Inheritance",
                "body": (
                    "The divine council argument ends not with the Son alone "
                    "but with the sons. Hebrews 2:10 calls the Son 'the archegos "
                    "of their salvation, bringing many sons to glory.' His "
                    "exaltation above the council (ch.1), entry below it in the "
                    "incarnation (ch.2), permanent ministry in the throne room "
                    "(ch.3), and the ekklesia's enrollment in the assembly (ch.4) "
                    "form one argument: the Son did all of this to bring sons "
                    "into the same position."
                    "\n\n"
                    "First Corinthians 6:3 ('we are to judge angels') and "
                    "Ephesians 3:10 ('through the church the manifold wisdom of "
                    "God might now be made known to the rulers and authorities "
                    "in the heavenly places') articulate what Hebrews argues from "
                    "the council framework. The ekklesia is the governing assembly "
                    "of the coming age -- enrolled in the heavenly city, present "
                    "at the throne room through Christ, destined for a governance "
                    "role that surpasses the old angelic-mediated order. Do not "
                    "drift back to the shadow when the substance has arrived."
                )
            }
        ]
    }
]
