"""
info.py -- 1 John: Scholarly Text Introduction

The first epistle of John, written by "the Elder" from the Johannine community,
combats proto-Gnostic secessionists who denied the Incarnation. A masterpiece of
light/darkness dualism, divine council warfare at the theological level, and the
insistence that love is the definitive test of authentic faith.
"""

TEXT_INFO = {
    "text_id": "1john",
    "display_name": "1 John",

    # -- CANONICAL STATUS ------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament General Epistle",
        "detail": "First John is canonical in all Christian traditions -- Catholic, Orthodox, "
                  "and Protestant. It was accepted early and without serious dispute, partly "
                  "because of its close theological and linguistic relationship to the Gospel "
                  "of John. Eusebius listed it among the 'acknowledged' (homologoumena) books. "
                  "It appears in the Muratorian Fragment (~170 AD) and was quoted by Polycarp, "
                  "Papias, and Irenaeus in the 2nd century. Its authority was never seriously "
                  "challenged in the patristic period."
    },

    # -- AUTHORSHIP ------------------------------------------------------
    "authorship": {
        "traditional": "The letter does not name its author, but early church tradition unanimously "
                       "attributed it to the apostle John, son of Zebedee, one of the Twelve and "
                       "the 'beloved disciple' of the Fourth Gospel. The author speaks with pastoral "
                       "authority, addresses the recipients as 'my little children' (teknia mou), "
                       "and claims to be an eyewitness of Jesus: 'that which we have heard, which "
                       "we have seen with our eyes, which we looked upon and have touched with our "
                       "hands' (1:1). Irenaeus (Against Heresies 3.16.5, 8) explicitly attributes "
                       "the letter to 'John, the disciple of the Lord.'",

        "scholarly_debate": "Modern scholarship recognizes that the author identifies himself only as "
                           "'the Elder' (ho presbyteros) in 2 John and 3 John, and does not name "
                           "himself at all in 1 John. The vocabulary, style, and theology of all "
                           "three Johannine epistles are closely related to the Gospel of John, leading "
                           "most scholars to place them within the same 'Johannine community.' Whether "
                           "the author is the apostle John himself, a disciple of the apostle, or an "
                           "elder within a community that preserved the apostle's teaching is debated. "
                           "Eusebius (Ecclesiastical History 3.39.4) distinguished between 'John the "
                           "apostle' and 'John the Elder' based on a passage in Papias, and some "
                           "scholars assign the epistles to this second John. Raymond Brown's magisterial "
                           "commentary (1982) argued that the epistles were written by a leader of the "
                           "Johannine community who was not the evangelist but shared his theological "
                           "tradition. The linguistic overlap with the Gospel is extensive: light/darkness, "
                           "truth/falsehood, abiding/remaining, the Paraclete, love commandment, the "
                           "world's hatred. Whatever the precise identity, the author wrote from within "
                           "the same theological circle that produced the Fourth Gospel.",

        "bottom_line": "The author is 'the Elder' -- a figure of recognized authority within the "
                       "Johannine community. Whether this is the apostle John himself or a close "
                       "disciple writing in the apostolic tradition, the letter carries the theological "
                       "DNA of the Gospel of John and addresses a specific crisis: false teachers who "
                       "have left the community and denied that Jesus Christ came in the flesh."
    },

    # -- DATE ------------------------------------------------------------
    "date": {
        "traditional": "Early church fathers placed 1 John late in the apostle's life, during his "
                       "residence in Ephesus. Irenaeus reports that John lived until the reign of "
                       "Trajan (98-117 AD), suggesting a date in the 90s AD.",
        "critical_range": "Most scholars date 1 John to approximately AD 90-95. The letter appears "
                         "to have been written AFTER the Gospel of John (it presupposes the Gospel's "
                         "theology and sometimes responds to misinterpretations of it) and addresses "
                         "a schism that has already occurred: 'They went out from us, but they were "
                         "not of us' (2:19). The proto-Gnostic tendencies the letter combats -- "
                         "denial of the Incarnation, moral indifferentism, claims to special knowledge "
                         "-- fit the late first century, when early forms of what would become "
                         "second-century Gnosticism were emerging.",
        "evidence": "Internal evidence points to a late first-century date: (1) The theological "
                    "vocabulary presupposes the developed Johannine tradition of the Fourth Gospel. "
                    "(2) The 'antichrists' and false teachers described fit the proto-Gnostic movements "
                    "known from the late first century. (3) The letter addresses a church community "
                    "in its second or third generation ('I write to you, fathers... young men... "
                    "children,' 2:12-14). (4) Polycarp of Smyrna (writing ~110-140 AD) appears to "
                    "quote 1 John 4:2-3 in his Epistle to the Philippians (7.1), providing a "
                    "terminus ad quem."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------
    "audience": {
        "original_audience": "The Johannine community -- a network of house churches likely based in "
                            "Ephesus and the surrounding region of Asia Minor. This community had "
                            "recently experienced a painful schism: a group of teachers had departed "
                            "from the community ('they went out from us,' 2:19) and were now spreading "
                            "teachings that the Elder considers fatally wrong. The remaining members "
                            "were shaken, uncertain about who was right, and in need of reassurance.",

        "purpose": "First John was written to accomplish three interlocking goals:\n\n"
                   "1. DOCTRINAL: To combat the false teaching of the secessionists, who denied "
                   "that Jesus Christ 'came in the flesh' (4:2). These teachers apparently "
                   "acknowledged Jesus as a divine being but denied the reality or salvific "
                   "significance of his physical incarnation, suffering, and death. This is "
                   "proto-Docetism -- the earliest form of the Gnostic heresy that would plague "
                   "the church for centuries.\n\n"
                   "2. ETHICAL: To insist that genuine knowledge of God necessarily produces "
                   "righteous living and brotherly love. The secessionists may have claimed "
                   "spiritual enlightenment while dismissing ethical behavior as irrelevant. "
                   "John's response: 'Whoever says I know him but does not keep his "
                   "commandments is a liar' (2:4). Love is not optional ornamentation -- it is "
                   "the definitive evidence that someone has passed from death to life (3:14).\n\n"
                   "3. PASTORAL: To reassure the faithful community that they are genuinely saved, "
                   "genuinely know God, and genuinely possess eternal life. The word 'know' "
                   "(ginosko/oida) appears over 30 times. The letter's stated purpose: 'I write "
                   "these things to you who believe in the name of the Son of God, that you may "
                   "know that you have eternal life' (5:13).",

        "theological_intent": "First John articulates a theology where orthodoxy and orthopraxy are "
                             "inseparable. Right belief about who Jesus is (the Christ come in the flesh) "
                             "and right behavior (love for the brothers) are two sides of the same coin. "
                             "You cannot have one without the other. The Incarnation is not merely a "
                             "doctrinal proposition to affirm -- it is the mechanism by which God entered "
                             "the human realm to destroy the works of the devil (3:8). To deny the "
                             "Incarnation is to deny God's invasion of enemy territory."
    },

    # -- ORIGINAL LANGUAGE -----------------------------------------------
    "language": {
        "original": "Greek. First John was composed in Koine Greek, the common Greek of the "
                    "Hellenistic world and the Roman Empire.",
        "script": "Greek uncial script in the earliest manuscripts.",
        "linguistic_notes": "The Greek of 1 John is simple, repetitive, and powerful -- short sentences, "
                           "heavy use of parallelism and antithesis (light/darkness, truth/lie, love/hate, "
                           "God/world). The vocabulary is remarkably close to the Gospel of John: both use "
                           "logos, zoe, phos, aletheia, agape, menein, kosmos, and parakleitos. Some "
                           "scholars have noted slight differences (1 John uses hilasmos for 'propitiation' "
                           "and chrisma for 'anointing,' terms absent from the Gospel), but the overall "
                           "linguistic profile is unmistakably Johannine. The Semitic flavor of the Greek "
                           "(paratactic sentence structure, conditional constructions) may reflect a writer "
                           "whose first language was Aramaic or Hebrew.",
        "grammar_match": "The Greek is consistent with late first-century Koine, specifically the "
                        "Johannine literary tradition. The style is more homiletical than epistolary -- "
                        "1 John lacks the standard letter opening (sender, recipient, greeting) and "
                        "reads more like a pastoral sermon or theological tract."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------
    "scripture_alignment": {
        "verdict": "Canonical New Testament epistle. First John is fully authoritative Christian "
                   "scripture, continuous with the theology of the Gospel of John and the broader "
                   "New Testament witness.",

        "where_it_aligns": [
            "The Incarnation theology ('the Word became flesh,' John 1:14) is presupposed and "
            "defended: Jesus Christ 'came in the flesh' (4:2) and 'came by water and blood' (5:6).",
            "The light/darkness dualism directly extends the Gospel of John (John 1:5, 3:19-21, "
            "8:12, 12:35-36) and parallels the Dead Sea Scrolls' Two Spirits doctrine (1QS III-IV), "
            "showing a shared Second Temple Jewish framework.",
            "The love commandment ('love one another,' 3:11, 23; 4:7, 11-12) is the central ethical "
            "demand of the Fourth Gospel (John 13:34-35, 15:12, 17).",
            "The identification of Jesus as the 'propitiation for our sins' (hilasmos, 2:2; 4:10) "
            "aligns with Paul's theology of atonement (Romans 3:25) and the Levitical system of "
            "sacrifice for sin.",
            "The 'Spirit of truth' and 'spirit of error' (4:6) use the exact terminology of the "
            "Qumran Two Spirits doctrine (1QS III.18-19), confirming shared theological vocabulary.",
            "'The whole world lies in the power of the evil one' (5:19) affirms the Deuteronomy 32 "
            "worldview: the nations are under the dominion of rebellious spiritual powers, and only "
            "those 'born of God' are delivered from this dominion."
        ],

        "where_it_diverges": [],

        "reader_guidance": "First John is canonical scripture and does not diverge from the biblical "
                          "witness. Its theological framework -- cosmic dualism under divine sovereignty, "
                          "the Incarnation as God's definitive intervention, love as the evidence of "
                          "regeneration -- is the theological heart of the New Testament. Read it as the "
                          "pastoral application of the theology proclaimed in the Gospel of John."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------
    "manuscripts": {
        "earliest": "The earliest manuscript witnesses include P9 (Papyrus Oxyrhynchus 402, 3rd century, "
                    "containing 1 John 4:11-12, 14-17) and the major 4th-century uncials Codex Sinaiticus "
                    "and Codex Vaticanus. The letter is also attested in early versions (Latin, Syriac, "
                    "Coptic) from the 3rd-4th centuries.",
        "major_witnesses": [
            {"name": "P9 (P.Oxy. 402)", "date": "3rd century AD",
             "note": "Papyrus fragment containing 1 John 4:11-12, 14-17. One of the earliest "
                     "witnesses to the text."},
            {"name": "Codex Sinaiticus (Aleph)", "date": "4th century AD",
             "note": "Complete text of 1 John. One of the two most important uncial manuscripts "
                     "for the entire New Testament."},
            {"name": "Codex Vaticanus (B)", "date": "4th century AD",
             "note": "Complete text of 1 John. The other pillar of New Testament textual criticism."},
            {"name": "Codex Alexandrinus (A)", "date": "5th century AD",
             "note": "Complete text. Important witness for the Catholic Epistles."}
        ],
        "reliability": "The text of 1 John is well-attested and stable across the manuscript tradition, "
                       "with one major exception: the Comma Johanneum (1 John 5:7-8). The longer reading, "
                       "which explicitly mentions 'the Father, the Word, and the Holy Spirit, and these "
                       "three are one,' is found only in late Latin manuscripts (earliest: 5th-6th century) "
                       "and is absent from ALL Greek manuscripts before the 14th century. It is universally "
                       "recognized by modern textual scholars as a later addition, not part of the original "
                       "text. Apart from this famous interpolation, the text of 1 John is remarkably stable."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------
    "historical_context": {
        "setting": "First John was written in the context of a community crisis. A group of teachers "
                   "had separated from the Johannine community ('they went out from us,' 2:19) and "
                   "were promoting a version of the faith that denied the significance of Jesus' "
                   "physical incarnation. This schism likely occurred in the churches of Asia Minor "
                   "(centered on Ephesus) in the last decade of the first century. The secessionists "
                   "may have drawn on early forms of the philosophical dualism between spirit and "
                   "matter that would later characterize full-blown Gnosticism: if the material world "
                   "is evil or illusory, then God could not truly have taken on flesh, and bodily "
                   "behavior is spiritually irrelevant.",

        "geography": "The Johannine community is traditionally located in Ephesus, the major city of "
                     "the Roman province of Asia (western Asia Minor, modern Turkey). Ephesus was a "
                     "cosmopolitan center of commerce, religion, and philosophy. The city hosted the "
                     "temple of Artemis (one of the Seven Wonders), a significant Jewish community, "
                     "and early Pauline churches (Acts 19; Ephesians; Revelation 2:1-7). The Johannine "
                     "community coexisted alongside these other Christian and Jewish communities. By "
                     "the 90s AD, Ephesus was a hotbed of competing theological claims.",

        "historical_connections": "First John provides critical evidence for the diversity and conflict "
                                 "within early Christianity. The schism it describes shows that even within "
                                 "a single community, fundamental disagreements about Christology could lead "
                                 "to division. The proto-Gnostic tendencies of the secessionists anticipate "
                                 "the major Gnostic systems of the 2nd century (Cerinthus, Valentinus, "
                                 "Basilides). Irenaeus (Against Heresies 3.3.4) specifically connects the "
                                 "apostle John with opposition to Cerinthus in Ephesus, which aligns with "
                                 "the anti-Docetic polemic of 1 John. The letter thus sits at the hinge "
                                 "point between the apostolic age and the patristic period, when the church "
                                 "would spend centuries defining orthodox Christology against Gnostic "
                                 "alternatives."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------
    "divine_council": {
        "relevance": "high",
        "summary": "First John is divine council warfare at the theological level. The entire letter "
                   "operates within the Deuteronomy 32 worldview: 'the whole world lies in the power "
                   "of the evil one' (5:19) -- the nations and their systems are under the dominion of "
                   "rebellious spiritual powers. Against this backdrop, the Incarnation is God's "
                   "definitive invasion of enemy territory: 'The reason the Son of God appeared was to "
                   "destroy the works of the devil' (3:8). This is not metaphor -- it is the theological "
                   "claim that the Second Person of the divine council took on human flesh to undo what "
                   "the rebellious elohim had done.\n\n"
                   "Key divine council connections:\n\n"
                   "(1) 'TEST THE SPIRITS' (4:1-6): John commands believers to 'test the spirits to see "
                   "whether they are from God.' This presupposes the Two Spirits framework of Qumran "
                   "(1QS III-IV) and the broader Second Temple understanding that spiritual beings stand "
                   "behind human teachings. The 'spirit of the antichrist' (4:3) and the 'spirit of truth "
                   "vs. spirit of error' (4:6) are not abstractions -- they are the operational influence "
                   "of rival members of the spiritual realm. False teaching is not merely human error; it "
                   "is the work of hostile spiritual powers.\n\n"
                   "(2) 'CHILDREN OF GOD VS. CHILDREN OF THE DEVIL' (3:10): This language echoes the "
                   "Qumran division between 'sons of light' and 'sons of darkness.' Humanity is divided "
                   "into two families based on which spiritual authority they belong to. The children of "
                   "God are those born of God (begotten from above); the children of the devil are those "
                   "who practice sin and belong to the evil one's domain.\n\n"
                   "(3) THE ANTICHRIST (2:18, 22; 4:3): The 'antichrist' is not merely a future political "
                   "figure but a present spiritual reality -- the spirit that denies the Incarnation. In "
                   "the divine council framework, this is the ultimate rebellion: denying that the Most "
                   "High God entered the human realm in flesh. The Incarnation is precisely what the "
                   "hostile powers cannot tolerate, because it is the mechanism of their defeat.\n\n"
                   "(4) LIGHT/DARKNESS DUALISM (1:5-7; 2:8-11): 'God is light, and in him is no darkness "
                   "at all.' This absolute dualism parallels the Dead Sea Scrolls' Two Spirits theology "
                   "and the Johannine Gospel's sustained light/darkness imagery. The darkness is not merely "
                   "ignorance -- it is the domain controlled by the 'evil one' (5:19), the rebellious "
                   "spiritual power who holds the world in his grip.\n\n"
                   "(5) 'THE WHOLE WORLD LIES IN THE EVIL ONE' (5:19): This is the Deuteronomy 32:8-9 "
                   "worldview stated in its starkest New Testament form. The world -- its systems, its "
                   "powers, its ideologies -- is under the administration of the hostile spiritual being. "
                   "Only those 'born of God' have been extracted from this dominion. The Incarnation, "
                   "death, and resurrection of Jesus are the mechanism of this extraction.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 35 (the 'prince of this world' and hostile spiritual powers "
            "in John's writings)",
            "The Unseen Realm, chapter 37 (the cosmic war and the purpose of the Incarnation)",
            "Supernatural, chapters 14-15 (spiritual warfare in the New Testament)",
            "Reversing Hermon, chapter 5 (how the NT authors understood the cosmic conflict)",
            "The Naked Bible Podcast, episodes on 1 John and the 'spirit of antichrist'"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "What Is the 'Antichrist'?",
            "body": "The word 'antichrist' (antichristos) appears in the New Testament ONLY in 1 John "
                    "and 2 John (1 John 2:18, 22; 4:3; 2 John 7). John uses it in two senses: (1) a "
                    "future eschatological figure ('you have heard that antichrist is coming,' 2:18), "
                    "and (2) a present reality already active in the world through false teachers who "
                    "deny the Incarnation ('many antichrists have come,' 2:18; 'every spirit that does "
                    "not confess Jesus is not from God; this is the spirit of the antichrist,' 4:3). "
                    "The popular image of a single future Antichrist figure is drawn more from Daniel, "
                    "2 Thessalonians 2, and Revelation 13 than from John's epistles. For John, the "
                    "'antichrist' is primarily a theological category: any teaching that denies Jesus "
                    "Christ came in the flesh is animated by the 'spirit of the antichrist.' The "
                    "antichrist is not coming -- the antichrist is already here, wherever the Incarnation "
                    "is denied."
        },
        {
            "type": "interpretation",
            "title": "Testing the Spirits: Discernment as Spiritual Warfare",
            "body": "When John commands 'test the spirits' (4:1), he is not speaking metaphorically. "
                    "In the Second Temple Jewish worldview that John shares with the Dead Sea Scrolls, "
                    "spiritual beings (the 'spirit of truth' and the 'spirit of error,' 4:6) actively "
                    "influence human thought, teaching, and behavior. False teaching is not merely bad "
                    "theology -- it is the operational influence of hostile spiritual powers working "
                    "through human agents. The test John provides is christological: 'Every spirit that "
                    "confesses that Jesus Christ has come in the flesh is from God, and every spirit "
                    "that does not confess Jesus is not from God' (4:2-3). The Incarnation is the "
                    "dividing line because it is the event the hostile powers most desperately oppose. "
                    "If Jesus did not come in the flesh, the invasion of enemy territory never happened, "
                    "and the 'works of the devil' (3:8) remain undefeated."
        },
        {
            "type": "scholarship",
            "title": "The Johannine Schism",
            "body": "Raymond Brown's landmark study 'The Community of the Beloved Disciple' (1979) and "
                    "his Anchor Bible commentary on the Johannine Epistles (1982) reconstructed the "
                    "crisis behind 1 John. Brown argued that the secessionists who 'went out from us' "
                    "(2:19) were not outsiders but members of the Johannine community who had taken the "
                    "Gospel of John's high Christology in a direction the Elder considered heretical. "
                    "The Gospel's emphasis on Jesus as the pre-existent Word (John 1:1), the divine 'I "
                    "Am' (John 8:58), and the one who came 'from above' (John 3:31) could be read as "
                    "minimizing Jesus' genuine humanity. The secessionists apparently did exactly this: "
                    "they affirmed Jesus' divinity but denied the salvific significance of his human "
                    "flesh, suffering, and death. First John's insistence that Jesus came 'in the flesh' "
                    "(4:2), 'by water and blood' (5:6), and that his blood 'cleanses us from all sin' "
                    "(1:7) is a direct counter to this proto-Docetic reading of the Gospel. The irony: "
                    "the same Gospel that proclaimed 'the Word became flesh' (John 1:14) was being used "
                    "to deny the significance of that very flesh."
        }
    ]
}
