"""
info.py -- Ephesians: Scholarly Text Introduction

This file provides the "front page" for Ephesians in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Ephesians is THE cosmic church epistle of the New Testament. It maps the
church's identity and mission against the backdrop of the divine council
worldview more explicitly than any other Pauline letter. Christ is seated
"far above all rule and authority and power and dominion" (1:21) -- language
drawn directly from the hierarchy of spiritual beings in Second Temple
Judaism. The "prince of the power of the air" (2:2) identifies Satan as
the territorial ruler over the present age. The church's cosmic vocation
is stated in 3:10: "through the church the manifold wisdom of God might
now be made known to the rulers and authorities in the heavenly places."
And the climactic passage on spiritual warfare (6:10-18) names the enemy
explicitly: "rulers, authorities, cosmic powers over this present darkness,
spiritual forces of evil in the heavenly places." No other epistle so
thoroughly integrates ecclesiology (the doctrine of the church) with
the divine council framework.
"""

TEXT_INFO = {
    "text_id": "ephesians",
    "display_name": "Ephesians",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Pauline Epistles",
        "detail": "Ephesians is universally canonical across all Christian traditions -- Roman Catholic, "
                  "Eastern Orthodox, and Protestant. It appears in every ancient canon list: the Muratorian "
                  "Fragment (c. 170 AD), Marcion's Apostolikon (c. 140 AD, where it was titled 'Laodiceans'), "
                  "Irenaeus (c. 180 AD, who quotes it extensively), Clement of Alexandria, Tertullian, and "
                  "Origen. The letter was deeply influential in early Christian theology: Ignatius of Antioch "
                  "(c. 110 AD) appears to allude to Ephesians in his own letter to the Ephesians, and "
                  "Polycarp's letter to the Philippians (c. 120 AD) echoes Ephesians 4:26. The epistle's "
                  "influence on subsequent Christian thought is immeasurable -- its vision of the church as "
                  "the body of Christ (1:22-23; 4:15-16), the household codes (5:21-6:9), the armor of God "
                  "(6:10-18), and its cosmic Christology (1:20-23) have shaped ecclesiology, ethics, "
                  "spirituality, and theology from the patristic era to the present. John Calvin called "
                  "Ephesians his favorite epistle. John Chrysostom's homilies on Ephesians remain among the "
                  "finest patristic commentaries. The letter is read liturgically across all major traditions."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The letter identifies its author as 'Paul, an apostle of Christ Jesus by the will of "
                       "God' (1:1) and describes himself as 'a prisoner for Christ Jesus' (3:1; 4:1; 6:20), "
                       "consistent with Paul's Roman imprisonment (c. 60-62 AD). The early church universally "
                       "attributed Ephesians to Paul without dispute. Irenaeus, Clement of Alexandria, "
                       "Tertullian, and Origen all quote Ephesians as Pauline. The letter's theology is "
                       "continuous with Romans, Colossians, and 1 Corinthians -- cosmic Christology, "
                       "justification by grace through faith, Jew-Gentile unity, and the body of Christ "
                       "metaphor. Paul's authorship was unquestioned for eighteen centuries.",

        "scholarly_debate": "Since F. C. Baur and the Tubingen school (mid-19th century), Pauline authorship "
                           "has been debated. Arguments against Pauline authorship include: (1) Vocabulary -- "
                           "Ephesians contains 40 words not found elsewhere in Paul (hapax legomena), and some "
                           "common Pauline terms are used differently. (2) Style -- the Greek sentences are "
                           "unusually long and complex, even for Paul (1:3-14 is a single sentence in Greek, "
                           "202 words). (3) Relationship to Colossians -- approximately one-third of Colossians "
                           "reappears in Ephesians, yet reworked and expanded, suggesting a later author used "
                           "Colossians as a source. (4) Theology -- some argue Ephesians presents a more "
                           "developed ecclesiology (the universal church rather than local congregations) and "
                           "a realized eschatology (believers already 'seated in the heavenly places,' 2:6) "
                           "that differs from Paul's earlier letters. Arguments FOR Pauline authorship include: "
                           "(1) The early church never questioned it. (2) An amanuensis (secretary) could "
                           "account for stylistic differences -- Paul used secretaries (Rom 16:22). (3) The "
                           "theology, while developed, is continuous with Paul's thought. (4) The relationship "
                           "to Colossians is better explained by Paul writing both letters around the same time "
                           "from the same imprisonment. (5) A pseudonymous author would likely have included "
                           "more personal details, not fewer.",

        "bottom_line": "The traditional view remains defensible: Paul wrote Ephesians during his Roman "
                       "imprisonment (c. 60-62 AD), possibly as a circular letter to multiple churches in "
                       "the province of Asia (which would explain its general tone and the absence of personal "
                       "greetings). Whether written by Paul directly or by a close associate under his "
                       "authority, the letter's theological content is authentically Pauline and represents "
                       "the fullest expression of Paul's cosmic ecclesiology -- the church as the body of "
                       "Christ, seated in the heavenly places, making known God's wisdom to the spiritual "
                       "powers."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "c. 60-62 AD, during Paul's first Roman imprisonment (Acts 28:30-31). The letter "
                       "was likely written around the same time as Colossians and Philemon, carried by "
                       "Tychicus (Eph 6:21; Col 4:7) to the churches of Asia Minor.",
        "critical_range": "If Pauline: c. 60-62 AD. If pseudonymous: c. 80-100 AD, written by a Pauline "
                         "disciple in Asia Minor who had access to Colossians and other Pauline letters. "
                         "Most scholars who reject Pauline authorship date it to the 80s AD, during the "
                         "period when Paul's letters were being collected and his legacy was being interpreted "
                         "for a new generation.",
        "evidence": "Key evidence includes: (1) The letter's self-identification as from a prisoner (3:1; "
                    "4:1; 6:20), consistent with Paul's Roman imprisonment. (2) The close relationship with "
                    "Colossians, which most scholars date to c. 60-62 AD. (3) Tychicus is named as the "
                    "letter carrier in both Ephesians 6:21 and Colossians 4:7. (4) The earliest external "
                    "attestation comes from Ignatius (c. 110 AD), establishing a terminus ante quem. "
                    "(5) The absence of 'in Ephesus' (en Epheso) in 1:1 in the earliest manuscripts "
                    "(P46, Sinaiticus, Vaticanus) suggests it may have been a circular letter, with the "
                    "destination added later -- consistent with Marcion's title 'To the Laodiceans' (cf. "
                    "Col 4:16, where Paul mentions a letter to Laodicea that should be shared)."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The letter is addressed to 'the saints who are in Ephesus and are faithful "
                            "in Christ Jesus' (1:1), but the earliest manuscripts omit 'in Ephesus,' "
                            "suggesting it was a circular letter to multiple churches in the Roman province "
                            "of Asia (modern western Turkey). Ephesus was the capital of the province, the "
                            "site of the great temple of Artemis (one of the Seven Wonders), and a major "
                            "center of Greco-Roman religion, magic, and the imperial cult. Paul had spent "
                            "three years in Ephesus (Acts 19-20), making it his longest ministry in any city. "
                            "The audience was predominantly Gentile (2:11-12; 3:1; 4:17), though the letter's "
                            "theology is deeply rooted in Jewish categories -- the divine council, the "
                            "commonwealth of Israel, the covenants of promise.",

        "purpose": "Ephesians has no specific crisis or heresy to address (unlike Galatians or Colossians). "
                   "Instead, it is a theological meditation on the nature, identity, and cosmic calling of "
                   "the church. Its purposes include: (1) Declaring the cosmic scope of God's plan in Christ "
                   "-- to unite all things in heaven and on earth under one head (1:10). (2) Establishing "
                   "the church's identity as the body of Christ, seated in the heavenly places, with a "
                   "mission that extends to the spiritual powers (3:10). (3) Celebrating the Jew-Gentile "
                   "unity accomplished by Christ, who has broken down the 'dividing wall of hostility' "
                   "(2:14). (4) Exhorting believers to walk worthy of their calling in unity, holiness, "
                   "and love (4:1-6:9). (5) Equipping believers for spiritual warfare against the cosmic "
                   "powers that oppose God's purposes (6:10-20).",

        "theological_intent": "Ephesians provides the fullest New Testament articulation of the church's "
                             "cosmic identity and mission within the divine council framework. The letter "
                             "answers three questions: (1) WHERE is Christ? -- seated at God's right hand "
                             "'far above all rule and authority and power and dominion' (1:20-21), the "
                             "position of supreme authority in the divine council, fulfilling Psalm 110:1. "
                             "(2) WHERE is the church? -- 'raised up with him and seated with him in the "
                             "heavenly places in Christ Jesus' (2:6), sharing Christ's exalted position above "
                             "the powers. (3) WHAT is the church's mission? -- to 'make known to the rulers "
                             "and authorities in the heavenly places the manifold wisdom of God' (3:10). The "
                             "church is not merely a human institution but a cosmic proclamation to the "
                             "spiritual powers that God's plan of redemption has succeeded. This is the "
                             "reversal of the Deuteronomy 32 worldview: the nations, once scattered among "
                             "the gods at Babel, are now being gathered into one body in Christ."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script (majuscule) in the earliest manuscripts",
        "linguistic_notes": "Ephesians contains some of the most elevated and complex Greek in the New "
                           "Testament. The opening blessing (1:3-14) is a single sentence of 202 words in "
                           "Greek -- one of the longest sentences in ancient literature. The style is "
                           "liturgical and hymnic, with long chains of relative clauses, prepositional "
                           "phrases, and participial constructions that build on each other in cascading "
                           "layers. Key theological vocabulary includes: <strong>en tois epouraniois</strong> "
                           "('in the heavenly places' -- 1:3, 20; 2:6; 3:10; 6:12), a distinctive phrase "
                           "appearing 5 times in Ephesians and nowhere else in Paul; <strong>mysterion</strong> "
                           "('mystery' -- 1:9; 3:3, 4, 9; 5:32; 6:19), the hidden plan of God now revealed; "
                           "<strong>oikonomia</strong> ('plan/administration' -- 1:10; 3:2, 9), God's cosmic "
                           "household management; <strong>plerooma</strong> ('fullness' -- 1:23; 3:19; 4:13), "
                           "the totality of divine presence filling all things; and the extensive spiritual "
                           "warfare vocabulary of 6:10-18 drawn from Roman military terminology: "
                           "<strong>panoplia</strong> (full armor), <strong>thureos</strong> (shield), "
                           "<strong>perikephalaia</strong> (helmet), <strong>machaira</strong> (sword).",
        "grammar_match": "The Greek of Ephesians is characterized by its paratactic style -- clauses linked "
                        "by kai (and), relative pronouns, and participial phrases rather than tight logical "
                        "argumentation. This creates a prose style that reads more like prayer or hymn than "
                        "argument. The density of prepositional phrases ('in Christ,' 'in him,' 'in the "
                        "heavenly places,' 'according to the working of his power') establishes a spatial "
                        "theology: believers exist 'in Christ' who exists 'in the heavenly places' where "
                        "the spiritual powers also operate. The phrase 'in Christ' (en Christo) and its "
                        "variants appear approximately 35 times in the letter, making it the most "
                        "'in-Christ' concentrated letter in the Pauline corpus."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Ephesians IS scripture -- universally canonical, deeply rooted in Old Testament "
                   "theology, and the fullest expression of the church's cosmic identity in Christ.",
        "nt_usage": "Ephesians draws extensively from the Old Testament: Psalm 68:18 is quoted in 4:8 "
                    "('When he ascended on high he led a host of captives, and he gave gifts to men'); "
                    "Psalm 110:1 underlies the enthronement language of 1:20; Genesis 2:24 is quoted in "
                    "5:31 ('the two shall become one flesh') and applied to Christ and the church; Isaiah "
                    "57:19 and 52:7 are echoed in 2:17 ('he came and preached peace to you who were far "
                    "off and peace to those who were near'); Deuteronomy 32:8-9 underlies the entire "
                    "framework of territorial spiritual powers; the armor of God in 6:14-17 draws from "
                    "Isaiah 11:5 (belt of righteousness), Isaiah 59:17 (breastplate of righteousness, "
                    "helmet of salvation), and Isaiah 52:7 (feet fitted with the gospel of peace). "
                    "The letter also has deep connections with Colossians, sharing approximately one-third "
                    "of its content, and with Romans (justification by grace through faith) and "
                    "1 Corinthians (body of Christ ecclesiology).",
        "internal_consistency": "Ephesians is deeply consistent with the broader Pauline corpus while "
                               "developing Paul's thought to its cosmic climax. The justification by grace "
                               "through faith of Romans 3-4 is restated in Ephesians 2:8-9. The body of "
                               "Christ metaphor of 1 Corinthians 12 is expanded into a cosmic ecclesiology in "
                               "Ephesians 1:22-23 and 4:15-16. The Jew-Gentile unity theme of Romans 9-11 and "
                               "Galatians 3 reaches its fullest expression in Ephesians 2:11-22. The spiritual "
                               "warfare theme implied in 2 Corinthians 10:3-5 and Romans 8:38-39 is developed "
                               "into the detailed cosmic warfare of Ephesians 6:10-18. The 'principalities and "
                               "powers' (archai kai exousiai) of Colossians 1:16; 2:15 are placed into the "
                               "cosmic drama of Ephesians 1:21; 3:10; 6:12. Ephesians is Paul's synthesis -- "
                               "the cosmic capstone of his theology."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "The earliest manuscript witness is P46 (Chester Beatty Papyrus II), dated c. 200 AD, "
                    "which contains Ephesians among the Pauline letters. Notably, P46 lacks the words "
                    "'in Ephesus' in 1:1, reading simply 'to the saints who are [blank] and faithful in "
                    "Christ Jesus.' This textual evidence supports the circular letter hypothesis.",
        "major_witnesses": [
            {"name": "P46 (Chester Beatty II)", "date": "c. 200 AD",
             "note": "The earliest witness to Ephesians. Lacks 'in Ephesus' in 1:1, reading 'to the "
                     "saints who are... and faithful.' Contains the complete text of Ephesians within a "
                     "codex of Pauline letters."},
            {"name": "Codex Sinaiticus (Aleph)", "date": "c. 350 AD",
             "note": "Also lacks 'in Ephesus' in 1:1 in the original hand. The complete text is well-"
                     "preserved and largely agrees with the critical text."},
            {"name": "Codex Vaticanus (B)", "date": "c. 325 AD",
             "note": "Similarly lacks 'in Ephesus' in the original text, though a later corrector added "
                     "it. This is the most important early uncial for the Pauline corpus."},
            {"name": "Codex Alexandrinus (A)", "date": "c. 400 AD",
             "note": "Includes 'in Ephesus' in 1:1. The text is of high quality and represents the "
                     "Byzantine text-type for the Pauline letters."}
        ],
        "reliability": "The text of Ephesians is extremely well-preserved. There are no major textual "
                       "variants that affect theological content. The most significant variant is the "
                       "presence or absence of 'in Ephesus' (en Epheso) in 1:1, which affects the letter's "
                       "destination but not its theology. The earliest and best manuscripts (P46, Sinaiticus, "
                       "Vaticanus) lack the phrase, strongly suggesting it was a circular letter. Marcion's "
                       "identification of the letter as 'To the Laodiceans' (c. 140 AD) confirms that the "
                       "destination was debated from very early. The theological content -- cosmic Christology, "
                       "ecclesiology, and spiritual warfare -- is stable across all witnesses."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Ephesians was written during Paul's imprisonment, most likely in Rome (c. 60-62 AD), "
                   "though Caesarea (c. 58-60 AD) has also been proposed. The city of Ephesus was the "
                   "preeminent metropolis of the Roman province of Asia -- a city of approximately 250,000 "
                   "people, home to the temple of Artemis (Diana), one of the Seven Wonders of the Ancient "
                   "World. Ephesus was a center of magic and occult practices: Acts 19:18-19 records that "
                   "converts burned 50,000 pieces of silver worth of magical scrolls. The city was also a "
                   "center of the imperial cult, with temples dedicated to Augustus and the Roman Senate. "
                   "Paul's three-year ministry in Ephesus (Acts 19-20) was marked by exorcisms, "
                   "confrontation with magical practitioners, and the riot of the silversmiths whose "
                   "Artemis idol business was threatened by the gospel.",

        "geography": "The letter's geography is primarily cosmic rather than terrestrial. The key spatial "
                     "concept is 'the heavenly places' (ta epourania) -- the realm where Christ is "
                     "enthroned (1:20), where believers are seated (2:6), where the spiritual powers "
                     "operate (3:10; 6:12), and where every spiritual blessing resides (1:3). This is "
                     "not 'heaven' in the popular sense of a distant paradise, but the spiritual dimension "
                     "of reality that intersects with the visible world. The 'air' (aer) in 2:2 is the "
                     "atmospheric realm -- the zone between earth and the highest heaven where, in Second "
                     "Temple cosmology, hostile spiritual powers exercised influence. The temple imagery "
                     "of 2:19-22 (the church as a 'holy temple in the Lord') evokes both the Jerusalem "
                     "Temple and the cosmic temple theology of the ancient Near East.",

        "historical_connections": "Ephesians connects to several major historical realities: (1) The "
                                 "Jew-Gentile divide was the defining social and theological issue of the "
                                 "early church. The 'dividing wall of hostility' (2:14) likely alludes to "
                                 "the physical barrier in Herod's Temple that separated the Court of the "
                                 "Gentiles from the inner courts, with inscriptions warning Gentiles that "
                                 "trespass meant death (two such inscriptions have been discovered "
                                 "archaeologically). (2) The 'mystery' language (1:9; 3:3-9) connects to "
                                 "both the apocalyptic mysteries of Daniel and 1 Enoch (hidden divine plans "
                                 "now revealed) and the Greco-Roman mystery religions that flourished in "
                                 "Ephesus and Asia Minor. (3) The household codes (5:21-6:9) engage the "
                                 "Greco-Roman household management tradition (Aristotelian oikonomia) while "
                                 "radically transforming it with mutual submission in Christ. (4) The armor "
                                 "of God (6:10-18) uses Roman legionary equipment as its imagery, appropriate "
                                 "for a letter written by a man chained to Roman soldiers (6:20)."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Ephesians is the New Testament's most explicit and sustained engagement with the "
                   "divine council worldview. The letter operates entirely within the framework of cosmic "
                   "spiritual powers, placing the church's identity and mission within the context of "
                   "the heavenly hierarchy."
                   "\n\n"
                   "CHRIST ABOVE THE COUNCIL (1:20-23): God 'raised him from the dead and seated him "
                   "at his right hand in the heavenly places, far above all rule (arche) and authority "
                   "(exousia) and power (dynamis) and dominion (kyriotes), and above every name that is "
                   "named, not only in this age but also in the one to come. And he put all things under "
                   "his feet and gave him as head over all things to the church, which is his body, the "
                   "fullness of him who fills all in all.' The four terms -- arche, exousia, dynamis, "
                   "kyriotes -- correspond to the hierarchy of spiritual beings in Second Temple Judaism. "
                   "These are the members of the divine council, the territorial rulers of the nations, "
                   "the cosmic powers that govern the spiritual dimension. Christ is seated ABOVE them "
                   "all, fulfilling Psalm 110:1 ('Sit at my right hand') and Psalm 8:6 ('all things "
                   "under his feet'). This is the enthronement of the Messiah as head of the divine "
                   "council."
                   "\n\n"
                   "THE PRINCE OF THE POWER OF THE AIR (2:1-3): Before conversion, believers 'walked "
                   "according to the course of this world (aion), according to the prince (archon) of "
                   "the power (exousia) of the air (aer), the spirit that is now at work in the sons "
                   "of disobedience.' This identifies Satan as the chief of the rebellious spiritual "
                   "powers -- not merely a tempter but a territorial ruler with administrative authority "
                   "over a domain. The 'air' (aer) in ancient cosmology was the sublunar realm between "
                   "earth and the highest heaven -- the zone of demonic activity in Second Temple thought "
                   "(cf. Testament of Benjamin 3:4; Ascension of Isaiah 7:9-12). The 'sons of disobedience' "
                   "are those under the archon's jurisdiction -- humanity in its unredeemed state, governed "
                   "by the rebellious council member who rules 'this present age.'"
                   "\n\n"
                   "THE CHURCH'S COSMIC MISSION (3:10): 'so that through the church the manifold wisdom "
                   "(polypoikilos sophia) of God might now be made known to the rulers and authorities "
                   "(archai kai exousiai) in the heavenly places.' This is THE defining verse for the "
                   "church's cosmic identity. The church -- composed of Jews and Gentiles united in one "
                   "body -- is God's demonstration to the spiritual powers that the Deuteronomy 32 division "
                   "of the nations has been reversed. The 'manifold wisdom' (polypoikilos -- 'many-colored,' "
                   "'many-faceted,' used of embroidered cloth) suggests the stunning complexity and beauty "
                   "of God's plan as it unfolds before the watching powers. The divine council members who "
                   "governed the nations now see the nations being reclaimed into one body under one head. "
                   "The church is not just saved FROM the powers; it is God's message TO the powers."
                   "\n\n"
                   "SPIRITUAL WARFARE (6:10-18): 'Put on the whole armor of God, that you may be able to "
                   "stand against the schemes (methodeia) of the devil. For we do not wrestle against "
                   "flesh and blood, but against the rulers (archas), against the authorities (exousias), "
                   "against the cosmic powers (kosmokratoras) over this present darkness, against the "
                   "spiritual forces of evil in the heavenly places (epouraniois).' This is the most "
                   "explicit spiritual warfare passage in the New Testament. The terminology maps directly "
                   "to the divine council hierarchy: archai (ruling powers), exousiai (authorities), "
                   "kosmokratores (world-rulers -- a term used in Greco-Roman astrology for planetary "
                   "deities that govern human destiny). The warfare is 'in the heavenly places' -- the "
                   "same realm where Christ is enthroned (1:20) and where believers are seated (2:6). "
                   "The armor of God draws from Isaiah's description of YHWH as divine warrior "
                   "(Isa 59:17; 11:5), suggesting that believers participate in YHWH's own battle against "
                   "the rebellious powers.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 30-31 (principalities and powers in Paul)",
            "The Unseen Realm, chapter 35-36 (spiritual warfare and the divine council)",
            "The Unseen Realm, chapter 13-14 (Deuteronomy 32 worldview — the backdrop of Eph 2-3)",
            "Supernatural, chapter 12-13 (the church and the powers)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 14-16 (NT spiritual powers)",
            "The Naked Bible Podcast, episode 42 (Ephesians 6:10-18 — cosmic warfare)",
            "The Naked Bible Podcast, episode 134 (principalities and powers)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 6-7 (archons and exousiai)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "En tois Epouraniois -- 'In the Heavenly Places'",
            "body": "The phrase <strong>en tois epouraniois</strong> (Greek: <em>en tois epouraniois</em>, "
                    "'in the heavenly places' or 'in the heavenly realms') appears 5 times in Ephesians "
                    "(1:3, 20; 2:6; 3:10; 6:12) and nowhere else in Paul's letters. It is the spatial key to "
                    "the entire letter. This is NOT 'heaven' in the sense of God's exclusive dwelling or the "
                    "final destination of the righteous. It is the <strong>spiritual dimension of reality</strong> "
                    "-- the realm where Christ is enthroned (1:20), where spiritual blessings exist (1:3), "
                    "where believers are already seated in Christ (2:6), where the principalities and powers "
                    "operate (3:10), and where spiritual warfare takes place (6:12).<br><br>"
                    "In the divine council framework, <em>ta epourania</em> is the realm of the council itself "
                    "-- the cosmic dimension where YHWH sits enthroned and the elohim (spiritual beings) carry "
                    "out their functions, whether faithful or rebellious. Ephesians presents this realm as the "
                    "primary theater of the gospel drama: Christ has been exalted there, believers have been "
                    "seated there, and the church's mission is directed there. The fact that both Christ AND "
                    "the hostile powers occupy the 'heavenly places' is not a contradiction but reflects the "
                    "Second Temple understanding that the spiritual realm contains multiple tiers -- Christ is "
                    "'far above' (hyperano) the powers, not merely alongside them."
        },
        {
            "type": "theology",
            "title": "Predestination in Ephesians 1 -- What Paul Actually Says",
            "body": "Ephesians 1:3-14 contains the most concentrated predestination language in the New "
                    "Testament: 'he chose us in him before the foundation of the world' (1:4), 'he "
                    "predestined us for adoption' (1:5), 'predestined according to the purpose of him who "
                    "works all things according to the counsel of his will' (1:11). This passage has been "
                    "the center of fierce theological debate for centuries.<br><br>"
                    "<strong>The Calvinist reading</strong> emphasizes God's sovereign unconditional election: "
                    "God chose specific individuals for salvation before they existed, apart from any foreseen "
                    "faith or merit. The language of 'before the foundation of the world' and 'according to "
                    "the counsel of his will' stresses divine initiative and sovereignty.<br><br>"
                    "<strong>The Arminian reading</strong> emphasizes that the choosing is 'in him' (en auto) "
                    "-- the election is corporate rather than individual. God predestined a PLAN (that those "
                    "in Christ would be holy and adopted) rather than predestining specific individuals. Faith "
                    "is the means by which individuals enter the chosen community.<br><br>"
                    "<strong>The divine council reading</strong> (Heiser's approach) places predestination in "
                    "the context of God's cosmic plan against the powers: God's predetermined plan was to "
                    "unite all things in Christ (1:10), reclaiming the nations scattered at Babel. The "
                    "'counsel of his will' (boulen tou thelematos, 1:11) echoes the council deliberation "
                    "language of the Old Testament (cf. Isa 46:10; Ps 33:11). The predestination is of "
                    "God's PLAN to redeem through Christ, not a debate about individual vs. corporate "
                    "election. The emphasis falls on the certainty and cosmic scope of God's purposes, not "
                    "on the mechanics of individual salvation."
        },
        {
            "type": "interpretation",
            "title": "The Mystery (Mysterion) -- Not a Secret but a Revelation",
            "body": "The word <strong>mysterion</strong> (Greek: <em>mysterion</em>) appears 6 times in "
                    "Ephesians (1:9; 3:3, 4, 9; 5:32; 6:19) -- more than in any other Pauline letter. In "
                    "popular English, 'mystery' suggests something unknown or unknowable. In Pauline "
                    "theology, it means the exact opposite: a <strong>mysterion</strong> is something that "
                    "<em>was</em> hidden but has <em>now</em> been revealed.<br><br>"
                    "The specific content of the mystery in Ephesians is stated in 3:6: 'that the Gentiles "
                    "are fellow heirs, members of the same body, and partakers of the promise in Christ "
                    "Jesus through the gospel.' The mystery is the Jew-Gentile union in one body -- the "
                    "reversal of the Deuteronomy 32 division of the nations. What was hidden in past ages "
                    "(3:5, 9) has now been revealed to the apostles and prophets by the Spirit. This "
                    "mystery has cosmic scope: it encompasses God's plan 'to unite all things in him, "
                    "things in heaven and things on earth' (1:10).<br><br>"
                    "The background of <em>mysterion</em> is twofold: (1) The apocalyptic tradition of "
                    "Daniel (Dan 2:18-19, 27-30, 47; cf. 1 Enoch 103:2; 104:10-12), where razin/mysteria "
                    "are divine secrets about the future revealed to the wise. (2) The Greco-Roman mystery "
                    "religions (Eleusinian, Dionysian, Isiac), where initiates received secret knowledge. "
                    "Paul subverts the mystery religion concept: in Christ, the mystery is not reserved for "
                    "elite initiates but proclaimed openly to all nations (6:19-20)."
        },
        {
            "type": "context",
            "title": "The Armor of God -- Isaiah's Divine Warrior Meets the Roman Legionary",
            "body": "The famous 'armor of God' passage (6:10-18) is often read as a purely devotional "
                    "metaphor, but its roots are in the divine warrior tradition of the Old Testament. Paul "
                    "does not invent the armor imagery -- he adapts it from Isaiah, where YHWH himself is "
                    "the warrior:<br><br>"
                    "<strong>Isaiah 59:17</strong>: 'He put on righteousness as a breastplate, and a helmet "
                    "of salvation on his head; he put on garments of vengeance for clothing, and wrapped "
                    "himself in zeal as a cloak.'<br>"
                    "<strong>Isaiah 11:5</strong>: 'Righteousness shall be the belt of his waist, and "
                    "faithfulness the belt of his loins.'<br>"
                    "<strong>Isaiah 52:7</strong>: 'How beautiful upon the mountains are the feet of him "
                    "who brings good news, who publishes peace.'<br><br>"
                    "Paul takes the armor that YHWH wears as the divine warrior and gives it to believers. "
                    "The theological implication is staggering: the church participates in YHWH's own cosmic "
                    "battle against the rebellious powers. The armor is not merely defensive -- it is the "
                    "equipment of the divine warrior himself, shared with his people. Each piece corresponds "
                    "to a divine attribute (truth, righteousness, peace, faith, salvation) and the one "
                    "offensive weapon is 'the sword of the Spirit, which is the word of God' (6:17) -- the "
                    "machaira tou pneumatos, the short thrusting sword of the Roman infantryman, here "
                    "identified with the rhema theou (the spoken word of God)."
        },
        {
            "type": "language",
            "title": "Key Greek Terms in Ephesians",
            "body": "<strong>arche</strong> (<em>arche</em>, plural <em>archai</em>) -- 'ruler, principality, "
                    "beginning.' In Ephesians 1:21; 3:10; 6:12, this refers to high-ranking spiritual powers "
                    "-- the chiefs of the divine council's hierarchy. These are the 'ruling powers' placed "
                    "over territories and domains.<br><br>"
                    "<strong>exousia</strong> (<em>exousia</em>, plural <em>exousiai</em>) -- 'authority, "
                    "power.' Paired with arche throughout Ephesians (1:21; 2:2; 3:10; 6:12), these are "
                    "spiritual beings who exercise delegated authority. The 'prince of the exousia of the "
                    "air' (2:2) is Satan, the chief of this category.<br><br>"
                    "<strong>kosmokrator</strong> (<em>kosmokrator</em>, plural <em>kosmokratores</em>) -- "
                    "'world-ruler.' Only in Eph 6:12 in the NT. In Greco-Roman astrology, kosmokratores "
                    "were planetary deities who governed human fate. Paul co-opts the term for the hostile "
                    "spiritual powers -- the 'cosmic powers over this present darkness.' This term connects "
                    "the divine council framework to the Greco-Roman world's own awareness of spiritual "
                    "powers governing human affairs.<br><br>"
                    "<strong>polypoikilos</strong> (<em>polypoikilos</em>) -- 'manifold, many-colored, "
                    "variegated.' Only in Eph 3:10 in the NT. Used of embroidered cloth or flowers of "
                    "diverse colors. The 'manifold wisdom of God' displayed through the church is not "
                    "monochrome but dazzlingly complex -- a tapestry of grace visible to the watching "
                    "powers.<br><br>"
                    "<strong>anakephalaioo</strong> (<em>anakephalaioo</em>) -- 'to sum up, to unite under "
                    "one head.' In Eph 1:10, God's plan is 'to unite all things in him' -- literally, to "
                    "'re-head' all of creation under Christ. This is the reversal of Babel: the nations "
                    "divided and placed under separate heads (the sons of God, Deut 32:8) are now being "
                    "gathered under one head, Christ."
        },
        {
            "type": "scholarship",
            "title": "Ephesians and Colossians -- Twin Letters?",
            "body": "Ephesians and Colossians share approximately one-third of their content, with "
                    "extensive verbal parallels: the cosmic Christ hymn (Col 1:15-20 / Eph 1:20-23), "
                    "the alienation-reconciliation pattern (Col 1:21-22 / Eph 2:1-10), the mystery "
                    "revealed (Col 1:26-27 / Eph 3:3-6), the household codes (Col 3:18-4:1 / Eph "
                    "5:21-6:9), and Tychicus as letter carrier (Col 4:7 / Eph 6:21).<br><br>"
                    "Three explanations have been proposed: (1) <strong>Paul wrote both simultaneously</strong> "
                    "from Rome, addressing similar themes to different audiences -- Colossians to a specific "
                    "church facing a specific heresy, Ephesians as a more general theological meditation on "
                    "the same themes for wider circulation. This is the traditional view. (2) <strong>A "
                    "disciple used Colossians as a source</strong> to compose Ephesians after Paul's death, "
                    "expanding and developing Paul's thought for a new generation. (3) <strong>Both letters "
                    "draw on common liturgical and catechetical material</strong> from Pauline churches.<br><br>"
                    "The key theological difference: Colossians emphasizes Christ's supremacy over the powers "
                    "(the powers are 'disarmed' and 'triumphed over,' Col 2:15), while Ephesians emphasizes "
                    "the <em>church's role</em> in the cosmic drama -- the church makes known God's wisdom "
                    "TO the powers (3:10). Colossians is Christological; Ephesians is ecclesiological. "
                    "Together, they present the complete picture: Christ's victory over the powers AND the "
                    "church's participation in proclaiming that victory."
        }
    ]
}
