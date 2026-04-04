"""
era_catholic_authority.py -- Chapters 1-3 of the Catholicism Research Lens

Chapter 1: Peter and the Rock -- Matt 16:18 Exegesis
Chapter 2: Mary -- From Theotokos to Mediatrix
Chapter 3: Purgatory & Prayers for the Dead

Approach: Present the Catholic position in its strongest form first, then
examine it against the biblical witness with Hebrew/Greek/Latin evidence.
Fair representation is a prerequisite for honest engagement -- strawman
arguments convince no one. If the biblical position is true, it should
be able to handle the strongest version of the opposing view.

Evidence tiers throughout:
  [A] Direct Scripture -- what the text actually says in Hebrew/Greek/Latin
  [B] Valid inference -- from Greek/Hebrew analysis, patristic evidence,
      historical context, manuscript tradition
  [C] Ancient parallels -- Church Father citations, conciliar documents,
      Second Temple Judaism, Hellenistic philosophy

Theological framework: Bible = authoritative foundation (Law #1).
Hebrew/Greek priority (Law #2). Non-biblical sources framed as "Catholic
tradition teaches..." never "the Bible says" (Law #5). Ekklesia =
governing assembly, not institutional church (Law #22). Afterlife =
Sheol to bodily resurrection to new earth, not souls ascending to
heaven (Law #23). Truth with good delivery (Law #30).

Sources: ESV (Scripture), Catechism of the Catholic Church (CCC),
Denzinger (Enchiridion Symbolorum), Ludwig Ott (Fundamentals of Catholic
Dogma), Oscar Cullmann (Peter: Disciple, Apostle, Martyr), D.A. Carson
(Matthew commentary, EBC), Michael S. Heiser (The Unseen Realm),
Jaroslav Pelikan (The Christian Tradition, vols. 1-3), Joseph Ratzinger
(Introduction to Christianity), N.T. Wright (The Resurrection of the
Son of God), Craig Keener (IVP Bible Background Commentary).
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: PETER AND THE ROCK -- MATT 16:18 EXEGESIS
    # =========================================================================
    {
        "id": "catholic-peter-rock",
        "ref": "Matt 16:18, 1 Cor 10:4, 1 Pet 2:4-8, Isa 22:22",
        "chapter_num": 1,
        "title": "Peter and the Rock \u2014 Matt 16:18 Exegesis",
        "era": "catholic_authority",
        "type": "chapter",

        "synopsis": (
            "Matthew 16:18 is the single most important verse in the "
            "Catholic case for papal primacy. Jesus says to Simon: 'You "
            "are Petros, and on this petra I will build my ekklesia.' "
            "Catholic theology reads this as the appointment of Peter as "
            "the foundation of the visible institution, with successors "
            "inheriting his authority through apostolic succession. The "
            "argument is strengthened by the Aramaic layer: Jesus almost "
            "certainly spoke Aramaic, where the word Kepha functions for "
            "both the name and the noun with no gender distinction. The "
            "Catholic reading has genuine patristic support -- but the "
            "Fathers are far from unanimous, and the Greek text preserves "
            "a distinction that Matthew clearly intended. The question is "
            "not whether Peter held a significant role among the apostles "
            "(he did), but whether Matthew 16:18 establishes an office of "
            "papal primacy transmissible across centuries through Roman "
            "bishops. That claim requires exegetical, historical, and "
            "theological evidence that the text itself does not supply."
        ),

        "key_verse": {
            "ref": "Matthew 16:18",
            "text": (
                "And I tell you, you are Peter, and on this rock I "
                "will build my church, and the gates of hell shall "
                "not prevail against it."
            ),
            "translation": "ESV"
        },

        # NOTE: These are Greek/Aramaic terms — field name is a known schema limitation
        "original_terms": [
            {
                "term": "\u03a0\u03ad\u03c4\u03c1\u03bf\u03c2 Petros (petros)",
                "meaning": (
                    "Greek masculine noun: a stone, a piece of rock, "
                    "a detached fragment. Used in the New Testament "
                    "exclusively as Simon's name. In classical and "
                    "Koine Greek, petros typically denotes a movable "
                    "stone or boulder -- distinct from petra, which "
                    "denotes bedrock or a massive rock formation. "
                    "Matthew, writing in Greek, chose to maintain "
                    "this distinction rather than using petra for both. "
                    "If Matthew intended Peter himself to be the "
                    "bedrock, he could have written 'you are Petra' "
                    "-- but the masculine name form required petros."
                )
            },
            {
                "term": "\u03c0\u03ad\u03c4\u03c1\u03b1 petra (petra)",
                "meaning": (
                    "Greek feminine noun: bedrock, cliff face, massive "
                    "rock formation. In the LXX, petra translates the "
                    "Hebrew tsur (\u05e6\u05d5\u05e8), a term applied to Yahweh "
                    "as the Rock of Israel (Deut 32:4, 2 Sam 22:2, "
                    "Ps 18:2). Paul explicitly identifies Christ as "
                    "the petra: 'they drank from the spiritual Rock "
                    "that followed them, and the Rock was Christ' "
                    "(1 Cor 10:4). Peter himself identifies Christ "
                    "as the foundational stone (1 Pet 2:4-8), never "
                    "claiming this identity for himself."
                )
            },
            {
                "term": "\u05db\u05b5\u05bc\u05d9\u05e4\u05b8\u05d0 Kepha (k\u0113p\u0304\u0101\u02be)",
                "meaning": (
                    "Aramaic: 'rock, crag.' The name Jesus gave Simon "
                    "(John 1:42, rendered Cephas in Greek transliteration). "
                    "In Aramaic, kepha functions for both the proper name "
                    "and the common noun without a gender distinction. "
                    "Catholic scholars argue this eliminates the petros/"
                    "petra distinction as a Greek artifact. This is a "
                    "legitimate linguistic point -- but it does not settle "
                    "the interpretive question, because Matthew chose to "
                    "write in Greek and preserved the distinction. If the "
                    "Aramaic identity were the whole point, Matthew could "
                    "have simply transliterated Kephas for both."
                )
            },
            {
                "term": "\u1f10\u03ba\u03ba\u03bb\u03b7\u03c3\u03af\u03b1 ekklesia (ekkl\u0113sia)",
                "meaning": (
                    "Greek: 'assembly, called-out gathering.' In the LXX "
                    "it translates Hebrew qahal (\u05e7\u05b8\u05d4\u05b8\u05dc), the assembly "
                    "of Israel gathered for covenantal purposes (Deut "
                    "9:10, 1 Kings 8:14). Ekklesia in the Greco-Roman "
                    "world was a governing assembly with legislative "
                    "authority -- not a religious institution. Jesus' use "
                    "in Matt 16:18 echoes the qahal of Israel: a covenant "
                    "community with governing authority, not an "
                    "institutional hierarchy with a monarchical head. "
                    "The translation 'church' imports centuries of "
                    "institutional development back into the 1st century."
                )
            }
        ],

        "ane_backdrop": (
            "In the ancient Near East, 'rock' language carried deep "
            "covenantal resonance. Yahweh is called tsur (Rock) throughout "
            "the Hebrew Bible (Deut 32:4, 15, 18, 30-31; 1 Sam 2:2; "
            "2 Sam 22:2-3, 32, 47; Ps 18:2, 31, 46; Isa 26:4; 44:8). "
            "This is not decorative metaphor -- it is covenant identity "
            "language. Yahweh is the unshakeable foundation. Isaiah 28:16 "
            "prophesies a tested cornerstone laid in Zion. Psalm 118:22 "
            "speaks of the stone rejected by the builders becoming the "
            "cornerstone. Jesus applies Psalm 118:22 to himself (Matt "
            "21:42). Peter applies it to Christ (1 Pet 2:4-8). Paul "
            "identifies Christ as the petra (1 Cor 10:4) and the "
            "foundation (1 Cor 3:11). The entire Old Testament rock/"
            "foundation tradition points to Yahweh and to the Messiah -- "
            "never to a human successor. Reading Matt 16:18 as establishing "
            "Peter as the bedrock foundation requires overriding this "
            "entire Hebrew theological tradition."
        ),

        "second_temple": [
            {
                "source": "Qumran Community Rule (1QS V-VI), c. 100 BC",
                "summary": (
                    "The Qumran community organized itself around a council "
                    "of twelve laymen and three priests, functioning as a "
                    "governing assembly with binding authority. This "
                    "structure parallels the twelve apostles without any "
                    "single monarchical head exercising supreme authority."
                ),
                "relevance": (
                    "[C] Jewish precedent for a governing council model "
                    "of leadership without a papal-style singular head. "
                    "The earliest Christian communities followed a similar "
                    "pattern: plural elders (Acts 14:23, 20:17; Titus 1:5), "
                    "not a single supreme bishop."
                )
            },
            {
                "source": "Clement of Rome, 1 Clement 5-6, c. 96 AD",
                "summary": (
                    "Clement writes from the Roman congregation to Corinth, "
                    "mentioning Peter and Paul together as exemplary "
                    "martyrs. Notably, Clement does not invoke Petrine "
                    "primacy or papal authority to settle the Corinthian "
                    "dispute. He appeals to apostolic teaching, not to "
                    "Roman jurisdictional supremacy."
                ),
                "relevance": (
                    "[B] The earliest document from the Roman church does "
                    "not claim the authority that later papal theology "
                    "would attribute to Rome. Clement's letter is pastoral "
                    "and collegial, not jurisdictional. If papal primacy "
                    "was understood from the beginning, this letter is "
                    "difficult to explain."
                )
            },
            {
                "source": "Cyprian of Carthage, De Unitate Ecclesiae, c. 251 AD",
                "summary": (
                    "Cyprian affirms Peter's primacy of honor but explicitly "
                    "denies that the Roman bishop holds jurisdictional "
                    "authority over other bishops. He clashed with Pope "
                    "Stephen I over rebaptism, refusing to submit to Roman "
                    "authority. Cyprian is paradoxically cited by both "
                    "Catholic and Protestant scholars."
                ),
                "relevance": (
                    "[B] A major 3rd-century bishop who affirmed Peter's "
                    "symbolic priority but denied Roman jurisdictional "
                    "supremacy -- demonstrating that papal authority as "
                    "later defined was not the universal understanding "
                    "of the early church."
                )
            }
        ],

        "cross_refs": [
            {
                "ref": "1 Corinthians 10:4",
                "note": (
                    "[A] Paul identifies Christ as the petra: 'the Rock "
                    "was Christ.' Paul uses the same Greek word (petra) "
                    "that Matthew uses in 16:18. If Paul understood Peter "
                    "as the petra-foundation, he contradicts himself here."
                ),
                "type": "nt"
            },
            {
                "ref": "1 Peter 2:4-8",
                "note": (
                    "[A] Peter himself identifies Christ as the living "
                    "stone, the cornerstone, the rock of stumbling. Peter "
                    "never claims the rock identity for himself -- he "
                    "explicitly assigns it to Christ."
                ),
                "type": "nt"
            },
            {
                "ref": "Galatians 2:11",
                "note": (
                    "[A] Paul rebukes Peter 'to his face, because he stood "
                    "condemned' over the Antioch incident. This public "
                    "correction of Peter by a fellow apostle is "
                    "incompatible with Peter holding supreme jurisdictional "
                    "authority. No Catholic would rebuke the Pope publicly "
                    "on a matter of doctrine and record it as legitimate."
                ),
                "type": "nt"
            },
            {
                "ref": "Acts 15:13-21",
                "note": (
                    "[A] At the Jerusalem Council, James -- not Peter -- "
                    "renders the final decision: 'Therefore my judgment "
                    "is...' James exercises the authoritative role. Peter "
                    "speaks (Acts 15:7-11), but James presides and decides."
                ),
                "type": "nt"
            },
            {
                "ref": "Isaiah 22:22",
                "note": (
                    "[B] The 'key of the house of David' given to Eliakim. "
                    "Catholic scholars connect this to the keys given to "
                    "Peter (Matt 16:19) as evidence of a transferable "
                    "office. However, Eliakim's authority was stewardship "
                    "under the king, not independent sovereignty -- and "
                    "Revelation 3:7 applies the Isaiah 22:22 key language "
                    "to Christ, not to any human successor."
                ),
                "type": "ot"
            },
            {
                "ref": "1 Corinthians 3:11",
                "note": (
                    "[A] 'No one can lay a foundation other than that "
                    "which is laid, which is Jesus Christ.' Paul is "
                    "explicit: Christ is the sole foundation. This "
                    "directly addresses whether any human figure -- "
                    "including Peter -- can serve as the foundational "
                    "rock of the ekklesia."
                ),
                "type": "nt"
            }
        ],

        "divine_council_note": (
            "The divine council framework illuminates why ekklesia "
            "language matters so much in Matt 16:18. Ekklesia is not a "
            "religious institution -- it is a governing assembly with "
            "cosmic jurisdiction. Paul states that the purpose of the "
            "ekklesia is to make known God's wisdom 'to the rulers and "
            "authorities in the heavenly places' (Eph 3:10). Believers "
            "will judge angels (1 Cor 6:3). The ekklesia is the new "
            "council -- humanity restored to the divine council role that "
            "was corrupted at Babel when the nations were allotted to the "
            "sons of God (Deut 32:8-9, LXX/DSS). Pentecost reverses "
            "Babel (Acts 2). The ekklesia's authority derives from Christ, "
            "the petra, the Rock of Israel -- not from a human succession "
            "line. The question is not whether Peter held a special role "
            "(he did -- he preached at Pentecost, opened the door to the "
            "Gentiles at Cornelius' house). The question is whether his "
            "role was an inheritable office or a unique apostolic function "
            "in salvation history. The divine council framework places "
            "authority in Christ as the head, with the ekklesia as his "
            "governing body -- not in a papal monarchy that has no "
            "precedent in the Hebrew Scriptures."
        ),

        "sections": [
            {
                "heading": "The Catholic Case at Its Strongest",
                "body": (
                    "Catholic scholarship presents a coherent argument. "
                    "Jesus renames Simon as Kepha (Aramaic: 'rock'), "
                    "echoing God's renaming of Abram to Abraham at a "
                    "covenantal turning point (Gen 17:5). In Aramaic, "
                    "there is no distinction between the name and the "
                    "noun -- Kepha means rock, and Kepha is the name. "
                    "The petros/petra distinction, Catholic scholars "
                    "argue, is simply a Greek gender accommodation: "
                    "Matthew could not give Simon a feminine name (petra) "
                    "in Greek, so he used the masculine form (petros) "
                    "for the name while preserving petra for the predicate. "
                    "The argument has weight. Oscar Cullmann, a Protestant "
                    "scholar, conceded in his 1953 study that Peter "
                    "himself is the rock in Matthew's immediate context. "
                    "Joseph Ratzinger (later Benedict XVI) argued that "
                    "the renaming of Simon establishes a new identity "
                    "and a new function -- Peter becomes the living "
                    "foundation stone. The keys of the kingdom (Matt "
                    "16:19) and the power to bind and loose reinforce "
                    "the picture of delegated authority. Catholic theology "
                    "then connects this to Isaiah 22:22, where Eliakim "
                    "receives the key of the house of David as a "
                    "steward -- an office that outlives the individual "
                    "holder. This is a serious exegetical argument and "
                    "deserves serious engagement."
                )
            },
            {
                "heading": "The Greek Text -- What Matthew Actually Wrote",
                "body": (
                    "Matthew wrote in Greek, and his Greek preserves a "
                    "distinction. The text reads: su ei Petros, kai epi "
                    "tautei tei petrai oikodomeso mou ten ekklesian... "
                    "[kai pulai hadou ou katischusousin autes omitted]. "
                    "'You are Petros [masculine, a stone], and upon this "
                    "petra [feminine, bedrock] I will build my ekklesia.' "
                    "If Matthew intended to say 'you are the rock and on "
                    "you I will build,' the simplest Greek construction "
                    "would be 'you are Petros and on you (epi soi) I will "
                    "build.' Instead, Matthew shifts from the masculine "
                    "petros to the feminine petra with the demonstrative "
                    "tautei ('this'). The shift is deliberate. D.A. "
                    "Carson, in the Expositor's Bible Commentary, notes "
                    "that while petros and petra had largely merged in "
                    "Koine Greek, Matthew's decision to use both forms "
                    "in the same sentence signals an intentional wordplay "
                    "with a distinction. The petra is Peter's confession -- "
                    "'You are the Christ, the Son of the living God' (Matt "
                    "16:16) -- not Peter himself. Jesus builds his ekklesia "
                    "on the bedrock confession of his identity as the "
                    "Messiah and the divine Son."
                )
            },
            {
                "heading": "The Church Fathers -- Not Unanimous",
                "body": (
                    "Catholic apologists often claim patristic consensus "
                    "for Peter as the rock. The actual record is far more "
                    "diverse. [B] Of the major Fathers who commented on "
                    "Matt 16:18, the interpretations fall into at least "
                    "three categories. First, the rock is Peter himself "
                    "(Tertullian in some passages, some readings of "
                    "Chrysostom). Second, the rock is Peter's confession "
                    "of faith (Chrysostom in Homily 54 on Matthew, "
                    "Hilary of Poitiers, Ambrose in some passages). "
                    "Third, the rock is Christ himself (Augustine in "
                    "his Retractations 1.21 -- written in Latin, using "
                    "ecclesia, not the Greek ekklesia -- revisited his "
                    "earlier interpretation, acknowledging that 'the "
                    "rock' could refer to Christ rather than Peter, "
                    "though he did not definitively retract the Petrine "
                    "reading. The nuance of his self-correction has "
                    "been debated by scholars on both sides). Chrysostom, frequently cited "
                    "by Catholics, actually wrote in Homily 54: 'Upon "
                    "this rock -- that is, on the faith of his "
                    "confession.' Augustine's self-correction is "
                    "particularly significant because he is one of the "
                    "most authoritative Western Fathers. The patristic "
                    "evidence does not support the claim that the early "
                    "church universally understood Peter as the rock-"
                    "foundation of a papal institution."
                )
            },
            {
                "heading": "Peter in His Own Letters",
                "body": (
                    "[A] The most telling evidence comes from Peter "
                    "himself. In 1 Peter 2:4-8, Peter writes about "
                    "Christ as the 'living stone' (lithon zonta), the "
                    "'cornerstone' (akrogoniaion), and the 'rock of "
                    "stumbling' (petra skandalou). Peter applies the "
                    "rock/stone language entirely to Christ. He never "
                    "claims the petra identity for himself. He never "
                    "references Matt 16:18 or the keys. He identifies "
                    "himself as 'a fellow elder' (sympresbyteros, 1 Pet "
                    "5:1) -- not as supreme shepherd, not as vicar of "
                    "Christ, not as head of the ekklesia. He instructs "
                    "elders to shepherd willingly, 'not domineering over "
                    "those in your charge' (1 Pet 5:3). The language of "
                    "1 Peter is radically incompatible with papal claims. "
                    "If Peter understood himself as the rock-foundation "
                    "with supreme authority and transmissible jurisdiction, "
                    "his own letters contain no trace of this self-"
                    "understanding."
                )
            },
            {
                "heading": "The Keys and the Kingdom -- What Was Given",
                "body": (
                    "[A] The keys of the kingdom (Matt 16:19) are real "
                    "authority -- this is not disputed. The question is "
                    "what kind of authority and whether it was exclusive "
                    "to Peter. The power to 'bind and loose' was a "
                    "recognized rabbinic concept. The Aramaic equivalents "
                    "-- asar (\u05d0\u05b2\u05e1\u05b7\u05e8, to bind) and shara (\u05e9\u05c1\u05b0\u05e8\u05b8\u05d0, to loose) -- "
                    "reflect the rabbinic authority to declare what is "
                    "forbidden and permitted. The Hebrew equivalents are "
                    "asar and hitir (\u05d4\u05b4\u05ea\u05bc\u05b4\u05d9\u05e8). The authority to declare "
                    "what is permitted and forbidden under Torah. Jesus "
                    "gives this same authority to all the disciples in "
                    "Matt 18:18: 'Truly, I say to you, whatever you bind "
                    "on earth shall be bound in heaven.' The binding and "
                    "loosing authority is not unique to Peter -- it belongs "
                    "to the apostolic community as a whole. The keys "
                    "imagery from Isaiah 22:22 describes stewardship under "
                    "the king, not independent sovereignty. And Revelation "
                    "3:7 applies the key of David to Christ: 'The words "
                    "of the holy one, the true one, who has the key of "
                    "David, who opens and no one will shut, who shuts "
                    "and no one opens.' The keys belong ultimately to "
                    "Christ. Peter exercised them in opening the door "
                    "of the gospel -- to Jews at Pentecost (Acts 2) and "
                    "to Gentiles at Cornelius' house (Acts 10). This is "
                    "a unique apostolic function, not a transferable "
                    "papal office."
                )
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: MARY -- FROM THEOTOKOS TO MEDIATRIX
    # =========================================================================
    {
        "id": "catholic-mariology",
        "ref": "Luke 1:46-55, John 2:3-5, 1 Tim 2:5, Matt 13:55-56",
        "chapter_num": 2,
        "title": "Mary \u2014 From Theotokos to Mediatrix",
        "era": "catholic_authority",
        "type": "chapter",

        "synopsis": (
            "Catholic Mariology represents one of the most significant "
            "theological developments in Christian history -- a trajectory "
            "that moves from the biblical portrait of Mary (a faithful "
            "Jewish woman, chosen as the mother of the Messiah, who "
            "identifies herself as a servant needing a savior) to a "
            "doctrinal edifice that includes sinless conception, perpetual "
            "virginity, bodily assumption into heaven, and co-redemptrix/"
            "mediatrix status. The question is not whether Mary deserves "
            "honor (she does -- Luke 1:48, 'all generations will call me "
            "blessed'). The question is whether the Catholic doctrinal "
            "development reflects what Scripture teaches or whether it "
            "represents a theological trajectory that departed from the "
            "biblical witness under the influence of late antique devotional "
            "culture, Hellenistic religious patterns, and the doctrinal "
            "authority claims of the papal magisterium. Two of the four "
            "major Marian dogmas -- the Immaculate Conception (1854) and "
            "the Assumption (1950) -- were defined as infallible dogma "
            "more than 1,800 years after Mary's life, without any "
            "scriptural basis and against the objections of significant "
            "Catholic theologians, including Thomas Aquinas on the "
            "Immaculate Conception."
        ),

        "key_verse": {
            "ref": "1 Timothy 2:5",
            "text": (
                "For there is one God, and there is one mediator "
                "between God and men, the man Christ Jesus."
            ),
            "translation": "ESV"
        },

        # NOTE: These are Greek/Aramaic terms — field name is a known schema limitation
        "original_terms": [
            {
                "term": "\u0398\u03b5\u03bf\u03c4\u03cc\u03ba\u03bf\u03c2 Theotokos (theotokos)",
                "meaning": (
                    "Greek: 'God-bearer, Mother of God.' Formally "
                    "affirmed at the Council of Ephesus (431 AD) against "
                    "Nestorius, who preferred Christotokos ('Christ-"
                    "bearer'). The term was primarily a Christological "
                    "statement -- affirming the unity of Christ's person "
                    "(the one born of Mary is truly God) -- not a Marian "
                    "one. Theotokos is defensible as Christology. The "
                    "problem arises when a Christological title becomes "
                    "the foundation for an independent Marian theological "
                    "trajectory that Scripture does not support."
                )
            },
            {
                "term": "\u03bc\u03b5\u03c3\u03af\u03c4\u03b7\u03c2 mesites (mesit\u0113s)",
                "meaning": (
                    "Greek: 'mediator, go-between.' Paul uses this term "
                    "in 1 Tim 2:5 with the numeral heis ('one'): heis "
                    "mesites theou kai anthropon. One mediator between "
                    "God and men. The grammar is emphatic -- heis is "
                    "placed first for emphasis. Catholic theology "
                    "distinguishes between Christ's unique mediation and "
                    "Mary's 'subordinate mediation,' but Paul's language "
                    "does not create tiers of mediation. Heis mesites "
                    "means one mediator."
                )
            },
            {
                "term": "\u03b4\u03bf\u03cd\u03bb\u03b7 doule (doul\u0113)",
                "meaning": (
                    "Greek: 'female servant, bondservant.' Mary's self-"
                    "identification in Luke 1:38: 'Behold, I am the "
                    "doule of the Lord.' And in the Magnificat (Luke "
                    "1:48): 'He has looked on the humble estate of his "
                    "doule.' Mary identifies herself as a servant -- "
                    "not as a co-redemptrix, not as a mediatrix, not "
                    "as queen of heaven. Her self-understanding, "
                    "preserved in Luke's Gospel, is radically different "
                    "from the titles later Catholic theology assigned "
                    "to her."
                )
            },
            {
                "term": "\u03c3\u03c9\u03c4\u03ae\u03c1 soter (sot\u0113r)",
                "meaning": (
                    "Greek: 'savior, deliverer.' Mary's Magnificat "
                    "declares: 'my spirit rejoices in God my soter' "
                    "(Luke 1:47). Mary rejoices in God as her savior. "
                    "If Mary was conceived without original sin (the "
                    "Immaculate Conception), in what sense does she need "
                    "a savior? Catholic theology answers with 'preservative "
                    "redemption' -- God saved Mary by preventing sin "
                    "rather than forgiving it. This is a theological "
                    "construction without any scriptural basis. Mary's "
                    "own words place her among those who need salvation."
                )
            }
        ],

        "ane_backdrop": (
            "The ancient Near Eastern and Greco-Roman world was saturated "
            "with goddess veneration. Isis in Egypt, Artemis/Diana in "
            "Ephesus (Acts 19:28), Inanna/Ishtar in Mesopotamia, Asherah "
            "in Canaan -- all functioned as divine mother figures, "
            "intercessors, and queen-of-heaven archetypes. The Hebrew "
            "prophets explicitly condemned the worship of the 'queen of "
            "heaven' (Jer 7:18; 44:17-25) -- likely Asherah or Ishtar. "
            "This is not to say Catholic Mariology consciously borrowed "
            "from paganism. But the cultural soil in which Marian devotion "
            "grew -- the Mediterranean world of the 3rd-5th centuries -- "
            "was ground that had been cultivated for millennia by goddess "
            "veneration. When the Council of Ephesus (431 AD) affirmed "
            "Theotokos, it met in a city whose primary cult had been "
            "the worship of Artemis. The transition from Artemis of the "
            "Ephesians to Mary the Theotokos in the same city, within "
            "the same cultural matrix, is historically documented. The "
            "Protoevangelium of James (mid-2nd century), the earliest "
            "source for Mary's perpetual virginity and her own miraculous "
            "birth, draws heavily on Hellenistic hagiographic conventions "
            "rather than on any apostolic tradition."
        ),

        "second_temple": [
            {
                "source": "Protoevangelium of James, c. 150 AD",
                "summary": (
                    "An apocryphal infancy gospel that narrates Mary's "
                    "miraculous birth, childhood in the Temple, perpetual "
                    "virginity (including a midwife's physical examination "
                    "after Jesus' birth), and Joseph as an elderly widower "
                    "with children from a previous marriage. This text is "
                    "the earliest source for most Marian traditions that "
                    "later became Catholic dogma."
                ),
                "relevance": (
                    "[C] The Protoevangelium of James, rejected as "
                    "apocryphal by Jerome and excluded from all canons, "
                    "is the seedbed of Marian doctrinal development. "
                    "Perpetual virginity, Mary's temple childhood, the "
                    "brothers of Jesus as step-brothers -- all trace to "
                    "this 2nd-century text, not to apostolic teaching."
                )
            },
            {
                "source": "Council of Ephesus, 431 AD",
                "summary": (
                    "Ecumenical council that affirmed Mary as Theotokos "
                    "against Nestorius. The council was primarily "
                    "Christological -- defending the unity of Christ's "
                    "divine and human natures -- but its Marian "
                    "implications became the foundation for later "
                    "doctrinal development."
                ),
                "relevance": (
                    "[B] Theotokos as a Christological affirmation is "
                    "defensible -- the child born of Mary is truly God "
                    "incarnate. The problem is the doctrinal trajectory "
                    "that followed: from Theotokos (God-bearer) to "
                    "Aeiparthenos (ever-virgin) to Immaculate Conception "
                    "to Assumption to Mediatrix -- each step moving "
                    "further from the biblical text."
                )
            },
            {
                "source": "Thomas Aquinas, Summa Theologiae III, q. 27, 13th century",
                "summary": (
                    "Aquinas -- the most authoritative Catholic theologian "
                    "-- argued against the Immaculate Conception. He held "
                    "that Mary was sanctified in the womb but after "
                    "conception, not at conception, because otherwise she "
                    "would not have needed redemption by Christ. Pius IX "
                    "overruled Aquinas in 1854."
                ),
                "relevance": (
                    "[B] When the Catholic Church's greatest theologian "
                    "argued against a doctrine that was later defined as "
                    "infallible dogma, it demonstrates that the Immaculate "
                    "Conception was not part of the received tradition. "
                    "Papal authority, not theological consensus or "
                    "scriptural evidence, was the basis for the definition."
                )
            }
        ],

        "cross_refs": [
            {
                "ref": "Luke 1:46-55",
                "note": (
                    "[A] The Magnificat. Mary declares God as 'my savior' "
                    "(soter, v. 47), placing herself among those who need "
                    "salvation. She praises God for regarding 'the humble "
                    "estate of his servant' (doule). Mary's self-portrait "
                    "is one of humble dependence, not exalted co-redemption."
                ),
                "type": "nt"
            },
            {
                "ref": "Matthew 13:55-56",
                "note": (
                    "[A] 'Is not this the carpenter's son? Is not his "
                    "mother called Mary? And are not his brothers James "
                    "and Joseph and Simon and Judas? And are not all his "
                    "sisters with us?' The Greek adelphoi (brothers) is "
                    "the standard term for biological siblings. Catholic "
                    "tradition argues these are cousins (Jerome) or step-"
                    "brothers (Protoevangelium of James), but adelphoi "
                    "in Greek means brothers unless context demands "
                    "otherwise."
                ),
                "type": "nt"
            },
            {
                "ref": "John 2:3-5",
                "note": (
                    "[A] The wedding at Cana. Catholic theology sees Mary "
                    "as intercessor -- she brings the need to Jesus. But "
                    "Jesus' response is telling: 'Woman, what does this "
                    "have to do with me?' (ti emoi kai soi, gynai). The "
                    "address is respectful but distancing. Mary's final "
                    "recorded instruction points away from herself: 'Do "
                    "whatever he tells you' (John 2:5)."
                ),
                "type": "nt"
            },
            {
                "ref": "Jeremiah 7:18",
                "note": (
                    "[A] 'The children gather wood, the fathers kindle "
                    "fire, and the women knead dough, to make cakes for "
                    "the queen of heaven.' Yahweh condemns the worship "
                    "of the queen of heaven through Jeremiah. The title "
                    "'Queen of Heaven' (Regina Caeli) is applied to Mary "
                    "in Catholic devotion. The Old Testament context of "
                    "this title is condemnation, not commendation."
                ),
                "type": "ot"
            },
            {
                "ref": "1 Timothy 2:5",
                "note": (
                    "[A] 'One mediator between God and men, the man "
                    "Christ Jesus.' Paul uses heis (one) emphatically. "
                    "The doctrine of Mary as Mediatrix (mediatrix "
                    "omnium gratiarum) directly contradicts Paul's "
                    "categorical statement. Catholic theology posits "
                    "'subordinate mediation,' but Paul's language "
                    "admits no tiers. The Greek anthropon "
                    "(\u1f00\u03bd\u03b8\u03c1\u03ce\u03c0\u03c9\u03bd, 'man/human being') emphasizes "
                    "that the mediator shares our nature -- not that "
                    "mediation is limited to males."
                ),
                "type": "nt"
            },
            {
                "ref": "Luke 11:27-28",
                "note": (
                    "[A] A woman cries out, 'Blessed is the womb that "
                    "bore you!' Jesus redirects: 'Blessed rather are "
                    "those who hear the word of God and keep it.' Jesus "
                    "himself deflects biological-maternal veneration "
                    "toward obedience to God's word."
                ),
                "type": "nt"
            }
        ],

        "divine_council_note": (
            "The divine council framework clarifies why the Mediatrix "
            "doctrine is theologically problematic beyond just 1 Tim 2:5. "
            "In the Hebrew Bible, access to the divine council -- the "
            "heavenly throne room -- is mediated by Yahweh alone. The "
            "prophets who stood in the council (sod, \u05e1\u05d5\u05d3) did so by "
            "Yahweh's direct invitation (Jer 23:18, 22; Amos 3:7; "
            "1 Kings 22:19-23). No angelic being, no human figure, no "
            "heavenly intermediary grants access independently. The New "
            "Testament presents Christ as the one who opens the way into "
            "the heavenly holy of holies (Heb 10:19-20, 'by the new and "
            "living way that he opened for us through the curtain'). "
            "Hebrews 4:14-16 states that believers can 'draw near to the "
            "throne of grace' directly through Christ as high priest. "
            "Inserting a secondary mediator between believers and Christ "
            "undermines the entire new covenant framework -- the tearing "
            "of the temple veil (Matt 27:51) signified direct access to "
            "God through Christ, not a new intermediary hierarchy."
        ),

        "sections": [
            {
                "heading": "What Scripture Actually Says About Mary",
                "body": (
                    "[A] The biblical portrait of Mary is remarkable and "
                    "beautiful -- but it is not what Catholic theology "
                    "has made of it. Mary is chosen by God for the most "
                    "significant human role in salvation history: bearing "
                    "the incarnate Son. Her faith response to the angel "
                    "is exemplary: 'Behold, I am the servant (doule) of "
                    "the Lord; let it be to me according to your word' "
                    "(Luke 1:38). The Magnificat (Luke 1:46-55) reveals "
                    "a woman steeped in the Hebrew Scriptures -- her song "
                    "echoes Hannah's prayer (1 Sam 2:1-10), the language "
                    "of the Psalms, and the prophetic hope of Israel. She "
                    "calls God 'my savior' (Luke 1:47). She identifies "
                    "as God's humble servant. She is present at the cross "
                    "(John 19:25-27). She is in the upper room at Pentecost "
                    "(Acts 1:14). After Acts 1:14, Mary disappears from "
                    "the New Testament narrative entirely. Paul never "
                    "mentions her. Peter never mentions her. John mentions "
                    "her only in his Gospel, not in his epistles. The "
                    "apostolic witness treats Mary with honor but does "
                    "not elevate her to a doctrinal or devotional role "
                    "beyond what Luke records."
                )
            },
            {
                "heading": "The Immaculate Conception -- 1854",
                "body": (
                    "The doctrine that Mary was conceived without original "
                    "sin was defined as infallible dogma by Pope Pius IX "
                    "in the bull Ineffabilis Deus (1854). [B] This was not "
                    "a recovery of ancient teaching -- it was a resolution "
                    "of a centuries-long debate that Catholic theology's "
                    "greatest minds had rejected. Thomas Aquinas argued "
                    "against the Immaculate Conception in the 13th century, "
                    "holding that if Mary never contracted original sin, "
                    "she would not need Christ's redemption, violating the "
                    "universality of salvation through Christ (Rom 3:23, "
                    "'all have sinned'; Rom 5:12, 'death spread to all "
                    "men because all sinned'). Bernard of Clairvaux, one "
                    "of the most devoted Marian theologians of the Middle "
                    "Ages, also opposed the doctrine. The Franciscan-"
                    "Dominican debate over the Immaculate Conception "
                    "lasted centuries before papal authority settled it "
                    "by fiat. The concept of 'preservative redemption' -- "
                    "that God saved Mary by preventing sin rather than "
                    "forgiving it -- is a theological construction without "
                    "any scriptural warrant. Mary's own words ('God my "
                    "savior,' Luke 1:47) do not distinguish between types "
                    "of salvation."
                )
            },
            {
                "heading": "The Assumption -- 1950",
                "body": (
                    "The doctrine that Mary was bodily assumed into heaven "
                    "was defined as infallible dogma by Pope Pius XII in "
                    "Munificentissimus Deus (1950). [B] This is the most "
                    "recent infallible papal definition and the one with "
                    "the least historical foundation. There is no mention "
                    "of Mary's death, burial, or assumption in any New "
                    "Testament text. The earliest traditions about Mary's "
                    "departure (the Dormition narratives) date to the 5th-"
                    "6th centuries and are legendary in character. There "
                    "is no early Christian veneration of Mary's tomb -- "
                    "which is remarkable, since the early church preserved "
                    "traditions about the burial places of apostles and "
                    "martyrs. The silence is significant but not conclusive. "
                    "What is conclusive is that the biblical afterlife "
                    "framework does not support the Assumption as defined. "
                    "The biblical pattern is death, then Sheol/the "
                    "intermediate state, then bodily resurrection at "
                    "Christ's return (1 Cor 15:22-23, 'each in his own "
                    "order: Christ the firstfruits, then at his coming "
                    "those who belong to Christ'). Christ is 'the "
                    "firstfruits of those who have fallen asleep' (1 Cor "
                    "15:20). If Mary was bodily assumed before the general "
                    "resurrection, she precedes the order Paul establishes. "
                    "The Assumption imports the Platonic soul-body "
                    "framework into Christian eschatology -- souls "
                    "ascending to heaven rather than awaiting bodily "
                    "resurrection on the renewed earth. The Assumption's "
                    "framing -- Mary taken 'body and soul into heavenly "
                    "glory' -- raises the afterlife question: the biblical "
                    "framework is Sheol \u2192 bodily resurrection \u2192 new earth "
                    "(1 Cor 15:20-23, where Christ is 'the firstfruits "
                    "of those who have fallen asleep'). If Christ is the "
                    "firstfruits of bodily resurrection, Mary's assumed "
                    "bodily glorification would precede the general "
                    "resurrection -- a theological tension the dogma "
                    "does not resolve."
                )
            },
            {
                "heading": "The Brothers of Jesus -- Adelphoi",
                "body": (
                    "[A] Matthew 13:55-56 names four brothers of Jesus -- "
                    "James, Joseph, Simon, Judas -- and mentions sisters "
                    "(plural). The Greek adelphoi is the standard word "
                    "for biological brothers. Catholic scholarship offers "
                    "two alternatives. Jerome's view (4th century): "
                    "adelphoi means cousins (anepsioi in Greek). But "
                    "Matthew had the word anepsioi available (Paul uses "
                    "it in Col 4:10 for Barnabas as Mark's cousin) and "
                    "chose adelphoi instead. The Protoevangelium of James' "
                    "view (2nd century): these are Joseph's children from "
                    "a prior marriage, making them step-brothers. This "
                    "tradition has no scriptural support and derives "
                    "entirely from an apocryphal text. Luke 2:7 calls "
                    "Jesus Mary's 'firstborn' (prototokos) son -- a term "
                    "that implies subsequent children. If Jesus were Mary's "
                    "only child, Luke could have written monogenes ('only-"
                    "born,' the term he uses for Jesus as God's Son in "
                    "John 3:16, traditionally attributed to the same "
                    "author). The natural reading of the Greek text, "
                    "without the pressure of the perpetual virginity "
                    "doctrine, is that Mary had other children after Jesus."
                )
            }
        ]
    },

    # =========================================================================
    # CHAPTER 3: PURGATORY & PRAYERS FOR THE DEAD
    # =========================================================================
    {
        "id": "catholic-purgatory",
        "ref": "1 Cor 3:12-15, Heb 9:27, 2 Macc 12:43-45, Luke 16:19-31",
        "chapter_num": 3,
        "title": "Purgatory & Prayers for the Dead",
        "era": "catholic_authority",
        "type": "chapter",

        "synopsis": (
            "Purgatory is the Catholic doctrine that the souls of those "
            "who die in God's grace but are not yet fully purified undergo "
            "a process of purification after death before entering heaven "
            "(CCC 1030-1032). The doctrine was formally defined at the "
            "Council of Florence (1439) and reaffirmed at Trent (1563). "
            "Catholic scholarship marshals several texts in its defense: "
            "2 Maccabees 12:43-45 (prayers and sacrifice for the dead), "
            "1 Corinthians 3:12-15 (works tested by fire, the person "
            "saved 'yet so as through fire'), and Matthew 12:32 (sin "
            "not forgiven 'in this age or the age to come,' possibly "
            "implying post-mortem forgiveness of some sins). These texts "
            "deserve careful examination on their own terms. But the "
            "doctrine of purgatory depends on a philosophical framework "
            "that is foreign to biblical thought: the Platonic soul-body "
            "dualism that entered Christian theology through Alexandrian "
            "influence. The Hebrew concept of afterlife is Sheol, then "
            "bodily resurrection, then new creation -- not disembodied "
            "souls undergoing purification in an intermediate realm. "
            "Purgatory is a solution to a problem that biblical "
            "anthropology does not create."
        ),

        "key_verse": {
            "ref": "Hebrews 9:27",
            "text": (
                "And just as it is appointed for man to die once, "
                "and after that comes judgment."
            ),
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "\u05e9\u05c1\u05b0\u05d0\u05d5\u05b9\u05dc Sheol (sh\u0115\u02be\u014dl)",
                "meaning": (
                    "Hebrew: the realm of the dead, the underworld. In "
                    "the Hebrew Bible, all the dead go to Sheol (Gen "
                    "37:35; Ps 89:48; Eccl 9:10). Sheol is not purgatory "
                    "-- it is not a place of purification or moral "
                    "refinement. It is the abode of the dead awaiting "
                    "resurrection. The Old Testament afterlife is "
                    "death, then Sheol, then bodily resurrection (Dan "
                    "12:2; Isa 26:19; Ezek 37:1-14). There is no "
                    "intermediate purification stage in the Hebrew "
                    "framework."
                )
            },
            {
                "term": "\u03c0\u03c5\u03c1\u03cc\u03c9 pyroo (pyro\u014d)",
                "meaning": (
                    "Greek verb: 'to burn, to test by fire.' Used in "
                    "1 Cor 3:13-15 for the testing of works (ergon). "
                    "Paul says each person's work will be tested by fire "
                    "(to ergon... to pyr dokimasei). The fire tests the "
                    "work (ergon), not the soul (psyche). The person "
                    "is saved (sothesetai); the work may be burned. "
                    "Catholic theology reads this as the purification "
                    "of the person; Paul's Greek says it is the "
                    "evaluation of the work."
                )
            },
            {
                "term": "purgatorium (Latin)",
                "meaning": (
                    "Latin: 'place of purging.' The word purgatorium "
                    "does not appear in any biblical text in any language "
                    "-- Hebrew, Aramaic, Greek, or Latin. It entered "
                    "Christian theological vocabulary through the Latin "
                    "Fathers, particularly Gregory the Great (6th century) "
                    "and was formalized as doctrine in the medieval period. "
                    "The concept depends on the Latin theological tradition, "
                    "not on biblical exegesis."
                )
            },
            {
                "term": "\u03ba\u03c1\u03af\u03c3\u03b9\u03c2 krisis (krisis)",
                "meaning": (
                    "Greek: 'judgment, decision, separation.' Hebrews "
                    "9:27 states the sequence: death (apothanein), then "
                    "judgment (krisis). The author of Hebrews presents "
                    "a two-step sequence -- death, then judgment -- with "
                    "no intermediate purification stage. The krisis "
                    "follows death directly. Purgatory requires inserting "
                    "a third step between death and judgment that the "
                    "biblical text does not contain."
                )
            }
        ],

        "ane_backdrop": (
            "The concept of post-mortem purification has deep roots in "
            "Greco-Roman philosophy, not in Hebrew thought. Plato's Phaedo "
            "and Republic describe the soul's journey after death through "
            "stages of purification. Virgil's Aeneid (Book 6) presents "
            "souls being purged of earthly stains in the underworld before "
            "ascending. Origen of Alexandria (3rd century), deeply "
            "influenced by Platonism, developed the idea of purifying "
            "fire after death (De Principiis II.10.4-6). Augustine refined "
            "the concept, distinguishing between mortal and venial sins and "
            "suggesting that some purification might occur after death "
            "(Enchiridion 69). Gregory the Great (6th century) developed "
            "the doctrine further, including specific stories of souls "
            "appearing to the living requesting prayers. The trajectory "
            "is clear: Platonic philosophy provided the soul-body dualism; "
            "Alexandrian Christianity baptized it; Augustine and Gregory "
            "systematized it; Florence and Trent defined it. The Hebrew "
            "Scriptures know nothing of disembodied souls undergoing "
            "moral refinement. The Hebrew afterlife hope is bodily "
            "resurrection on a renewed earth (Isa 65:17-25; Dan 12:2; "
            "Ezek 37:1-14) -- not the escape of the soul from the body "
            "through progressive purification."
        ),

        "second_temple": [
            {
                "source": "2 Maccabees 12:43-45, c. 124 BC",
                "summary": (
                    "Judas Maccabeus sends money to Jerusalem for a sin "
                    "offering on behalf of soldiers who died wearing "
                    "pagan amulets. The text states he acted 'that they "
                    "might be delivered from their sin' and made "
                    "'atonement for the dead.' This is the strongest "
                    "Catholic proof text for prayers for the dead."
                ),
                "relevance": (
                    "[C] 2 Maccabees is deuterocanonical -- accepted by "
                    "Catholic and Orthodox traditions but not by the "
                    "Jewish or Protestant canons. Even within Catholic "
                    "tradition, deuterocanonical books hold a secondary "
                    "status. More significantly, the soldiers in question "
                    "died in idolatry (wearing amulets of Jamnia's gods). "
                    "Judas' action may reflect 2nd-century BC Jewish piety "
                    "without establishing a doctrinal norm for post-mortem "
                    "purification."
                )
            },
            {
                "source": "Augustine, Enchiridion 69, c. 421 AD",
                "summary": (
                    "Augustine suggested that some believers might undergo "
                    "a purifying fire after death, distinguishing between "
                    "those who build with gold and silver (whose works "
                    "survive) and those who build with wood and straw "
                    "(whose works are burned, though they are saved). "
                    "Augustine was tentative, not dogmatic."
                ),
                "relevance": (
                    "[B] Augustine's influence on Western theology was "
                    "immense, but his tentative suggestions became the "
                    "basis for dogmatic definitions centuries later. "
                    "Augustine himself was deeply shaped by his earlier "
                    "Platonism (Confessions VII), and his afterlife "
                    "theology reflects the Platonic soul-body framework "
                    "rather than the Hebrew resurrection hope."
                )
            },
            {
                "source": "Gregory the Great, Dialogues IV, c. 593 AD",
                "summary": (
                    "Gregory collected stories of souls appearing to the "
                    "living, requesting Masses and prayers to hasten their "
                    "release from purgatorial suffering. His Dialogues "
                    "became enormously influential in shaping medieval "
                    "piety and the popular understanding of purgatory."
                ),
                "relevance": (
                    "[C] Gregory's stories are hagiographic literature, "
                    "not exegetical arguments. The purgatory doctrine "
                    "became embedded in Western Christianity through "
                    "pastoral storytelling and liturgical practice before "
                    "it was defined as dogma. The development was cultural "
                    "and devotional, not exegetical."
                )
            }
        ],

        "cross_refs": [
            {
                "ref": "1 Corinthians 3:12-15",
                "note": (
                    "[A] The primary Catholic proof text for purgatory. "
                    "Paul describes building on the foundation with gold, "
                    "silver, precious stones, wood, hay, straw. Fire "
                    "tests each one's work (ergon). 'If the work is "
                    "burned up, he will suffer loss, though he himself "
                    "will be saved, but only as through fire.' The fire "
                    "tests works, not souls. The person is already saved. "
                    "Paul is discussing ministry evaluation at the "
                    "judgment seat, not post-mortem soul purification."
                ),
                "type": "nt"
            },
            {
                "ref": "Hebrews 9:27-28",
                "note": (
                    "[A] 'It is appointed for man to die once, and after "
                    "that comes judgment.' The author presents a two-step "
                    "sequence: death then judgment. No intermediate "
                    "purification. Verse 28 completes the parallel: "
                    "'Christ, having been offered once to bear the sins "
                    "of many.' The once-for-all nature of Christ's "
                    "sacrifice leaves no remainder for post-mortem "
                    "purification to address."
                ),
                "type": "nt"
            },
            {
                "ref": "Luke 16:19-31",
                "note": (
                    "[A] The parable of the rich man and Lazarus. "
                    "Abraham's bosom and Hades are separated by a 'great "
                    "chasm' (chasma mega) that 'has been fixed' (esteriktai, "
                    "perfect passive: permanently established). No one "
                    "can cross from one side to the other. The geography "
                    "of the afterlife in Jesus' teaching includes a fixed "
                    "separation, not a permeable purification zone."
                ),
                "type": "nt"
            },
            {
                "ref": "Matthew 12:32",
                "note": (
                    "[B] 'Whoever speaks against the Holy Spirit will "
                    "not be forgiven, either in this age or in the age "
                    "to come.' Catholic theology reads 'age to come' "
                    "as implying some sins can be forgiven after death. "
                    "But Jesus' point is the absolute unforgiveness of "
                    "blasphemy against the Spirit -- the phrase 'neither "
                    "in this age nor the next' is an emphatic negation "
                    "(a Semitic idiom meaning 'never'), not a positive "
                    "statement about post-mortem forgiveness."
                ),
                "type": "nt"
            },
            {
                "ref": "Daniel 12:2",
                "note": (
                    "[A] 'Many of those who sleep in the dust of the "
                    "earth shall awake, some to everlasting life, and "
                    "some to shame and everlasting contempt.' The Hebrew "
                    "afterlife hope: sleep in the dust (not conscious "
                    "purification), then awakening to either life or "
                    "judgment. Two outcomes, no intermediate purification."
                ),
                "type": "ot"
            },
            {
                "ref": "2 Corinthians 5:8",
                "note": (
                    "[B] 'To be absent from the body is to be present "
                    "with the Lord.' Paul's expectation for the believer "
                    "after death is immediate presence with Christ -- "
                    "not a detour through purification. If purgatory "
                    "intervenes between death and Christ's presence, "
                    "Paul's confidence is misplaced."
                ),
                "type": "nt"
            },
            {
                "ref": "Isaiah 65:17-25",
                "note": (
                    "[A] The new heavens and new earth -- the Hebrew "
                    "prophetic hope. The afterlife destination in Hebrew "
                    "thought is not an ethereal heaven for disembodied "
                    "souls but a renewed physical creation. Purgatory "
                    "belongs to the Platonic framework of soul-escape, "
                    "not to the Hebrew framework of creation-renewal."
                ),
                "type": "ot"
            }
        ],

        "divine_council_note": (
            "The divine council framework places the afterlife in its "
            "proper biblical context. When humans die, they enter Sheol -- "
            "the realm of the dead (Hebrew: rephaim, 'the shades,' Isa "
            "14:9, 26:14). The dead in Sheol are not undergoing moral "
            "refinement; they are awaiting resurrection. The Old Testament "
            "hope is that God will not abandon the righteous to Sheol "
            "permanently (Ps 16:10, 'you will not abandon my soul to "
            "Sheol, or let your holy one see corruption' -- Peter applies "
            "this to Christ's resurrection in Acts 2:27-31). The "
            "resurrection hope is physical: 'Your dead shall live; their "
            "bodies shall rise' (Isa 26:19). Ezekiel 37 envisions dry "
            "bones receiving flesh and breath -- bodily resurrection on "
            "a renewed earth, not disembodied souls ascending through "
            "purification chambers. The divine council operates in the "
            "heavenly realm, and the resurrected ekklesia will join that "
            "governance (1 Cor 6:3, 'Do you not know that we are to "
            "judge angels?'). The path from death to that cosmic role "
            "runs through resurrection, not through purgatory. The "
            "Platonic infiltration that makes purgatory conceivable -- "
            "the idea that the soul is the real person and the body is "
            "a temporary shell -- entered Christian theology through "
            "Alexandrian influence (Clement of Alexandria, Origen) and "
            "represents a fundamental departure from Hebrew anthropology, "
            "where the whole person (basar, nephesh, ruach -- flesh, "
            "being, breath) is a unity destined for resurrection."
        ),

        "sections": [
            {
                "heading": "The Catholic Case -- Presented Fairly",
                "body": (
                    "Catholic theology presents purgatory as a necessary "
                    "implication of God's holiness and human imperfection. "
                    "The argument runs: nothing impure can enter God's "
                    "presence (Rev 21:27). Most believers die imperfectly "
                    "sanctified -- still carrying the effects of venial "
                    "sins, still attached to worldly things, still "
                    "incompletely conformed to Christ. Therefore, a "
                    "process of final purification is needed. The "
                    "Catechism states: 'All who die in God's grace and "
                    "friendship, but still imperfectly purified, are "
                    "indeed assured of their eternal salvation; but after "
                    "death they undergo purification, so as to achieve "
                    "the holiness necessary to enter the joy of heaven' "
                    "(CCC 1030). According to Catholic tradition, 2 "
                    "Maccabees 12:43-45 establishes the practice of "
                    "praying for the dead. According to one Catholic "
                    "reading, 1 Cor 3:12-15 describes the purifying "
                    "fire. Matt 12:32, in this view, implies that some "
                    "sins can be forgiven in 'the age to come.' The "
                    "argument is internally coherent within the Catholic "
                    "system. The question is whether that system reflects "
                    "what Scripture teaches."
                )
            },
            {
                "heading": "1 Corinthians 3:12-15 -- What the Fire Tests",
                "body": (
                    "[A] Paul's metaphor in 1 Corinthians 3 is about "
                    "ministry, not about post-mortem purification. The "
                    "context is critical. Paul is addressing factions in "
                    "Corinth (1 Cor 3:4, 'When one says I follow Paul and "
                    "another I follow Apollos'). He describes himself and "
                    "Apollos as fellow workers building on a foundation. "
                    "'No one can lay a foundation other than that which is "
                    "laid, which is Jesus Christ' (3:11). Then he describes "
                    "building materials: gold, silver, precious stones "
                    "versus wood, hay, straw. 'The Day' (hemera, referring "
                    "to the Day of the Lord, the eschatological judgment) "
                    "will reveal each one's work (ergon). The fire tests "
                    "the work. 'If the work is burned up, he will suffer "
                    "loss, though he himself will be saved, but only as "
                    "through fire.' The Greek is precise: the fire tests "
                    "to ergon (the work), not ten psychen (the soul). The "
                    "person (autos) is saved (sothesetai, future passive). "
                    "This is a metaphor for escaping a burning building "
                    "with nothing but your life -- not a description of "
                    "the soul being purified through suffering."
                )
            },
            {
                "heading": "The Deuterocanonical Question -- 2 Maccabees",
                "body": (
                    "[C] 2 Maccabees 12:43-45 is the only ancient text "
                    "that directly describes making atonement for the dead. "
                    "The context: soldiers in Judas Maccabeus' army died "
                    "wearing pagan amulets dedicated to the idols of "
                    "Jamnia. Judas collected money and sent it to Jerusalem "
                    "for a sin offering. The text commends this as an "
                    "expression of belief in resurrection. Several issues "
                    "complicate its use as a proof text. First, 2 Maccabees "
                    "is deuterocanonical -- part of the Catholic and "
                    "Orthodox canons but not the Jewish or Protestant "
                    "canons. The Jewish community that produced it did not "
                    "ultimately include it in their Scriptures. Second, "
                    "the soldiers died in the specific sin of idolatry -- "
                    "not in a state of imperfect sanctification. Third, "
                    "the practice Judas describes (sending money for "
                    "temple sacrifice) is tied to the Second Temple "
                    "sacrificial system that ended in 70 AD. Fourth, "
                    "even Catholic theology does not teach that purgatory "
                    "applies to those who die in mortal sin (idolatry "
                    "qualifies). The text describes a specific 2nd-century "
                    "BC practice, not a universal doctrine of post-mortem "
                    "purification."
                )
            },
            {
                "heading": "The Platonic Infiltration",
                "body": (
                    "[B] The deeper question is not whether specific "
                    "proof texts support purgatory but whether the entire "
                    "conceptual framework is biblical. Purgatory requires "
                    "several philosophical assumptions: (1) the soul "
                    "separates from the body at death and continues in "
                    "conscious existence; (2) the soul can undergo moral "
                    "improvement without the body; (3) suffering purifies "
                    "the soul of moral stain; (4) temporal punishment "
                    "remains after guilt is forgiven. None of these "
                    "assumptions derive from Hebrew thought. They derive "
                    "from Platonic philosophy -- specifically the Phaedo "
                    "and Republic, where the soul's journey after death "
                    "involves stages of purification. Clement of "
                    "Alexandria (c. 150-215 AD) and Origen (c. 184-253 "
                    "AD) were the first Christian theologians to develop "
                    "a detailed post-mortem purification theology, and "
                    "both were steeped in Platonic philosophy. Origen's "
                    "concept of apokatastasis (universal restoration "
                    "through purifying fire) was later condemned, but "
                    "the basic framework -- disembodied souls undergoing "
                    "moral refinement -- survived in modified form as "
                    "purgatory. Hebrew anthropology is holistic: the "
                    "human person is basar (flesh), nephesh (living being), "
                    "and ruach (breath/spirit) as a unity. The hope is "
                    "not the soul's escape from the body but the "
                    "resurrection of the whole person into a renewed "
                    "creation."
                )
            },
            {
                "heading": "Hebrews 9:27 and the Biblical Afterlife Sequence",
                "body": (
                    "[A] The author of Hebrews states the afterlife "
                    "sequence with stark simplicity: 'It is appointed for "
                    "man to die once, and after that comes judgment' "
                    "(Heb 9:27). Two steps. Death, then judgment. No "
                    "intermediate stage. The verse continues with a "
                    "Christological parallel: 'so Christ, having been "
                    "offered once to bear the sins of many, will appear "
                    "a second time, not to deal with sin but to save "
                    "those who are eagerly waiting for him' (9:28). "
                    "Christ's sacrifice is once-for-all (hapax, the "
                    "characteristic term of Hebrews: 7:27, 9:12, 9:26, "
                    "10:10). If Christ's single offering has 'perfected "
                    "for all time those who are being sanctified' (Heb "
                    "10:14), there is no remainder of sin or impurity "
                    "for purgatory to address. The entire argument of "
                    "Hebrews moves in the opposite direction from "
                    "purgatory: Christ's work is complete, the sacrifice "
                    "is final, the purification is accomplished, and "
                    "believers have 'confidence to enter the holy places "
                    "by the blood of Jesus' (Heb 10:19) -- directly, "
                    "without an intermediate stage of purification."
                )
            }
        ]
    },
]
