"""
info.py -- Matthew (Kata Matthaion): Scholarly Text Introduction

This file provides the "front page" for Matthew in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Matthew is the Gospel of the Kingdom -- the most Jewish of the four Gospels,
written to demonstrate that Jesus of Nazareth is the promised Messiah, the
Son of David who fulfills all the Law and the Prophets. Through its divine
council lens, Matthew presents Jesus as the one to whom "all authority in
heaven and on earth" has been given (28:18) -- the Psalm 2 Son who inherits
the nations, the Daniel 7 Son of Man who receives dominion from the Ancient
of Days, the Immanuel ("God with us") who is YHWH's presence embodied on
earth. Matthew's Jesus confronts Satan's illegitimate claim over the nations
(4:8-9), announces that the kingdom of God has arrived to plunder the strong
man's house (12:28-29), declares that the gates of Hades will not prevail
against his assembly (16:18), and commissions his followers to disciple all
nations (28:19) -- the Great Commission as the reversal of Deuteronomy
32:8-9, reclaiming the disinherited nations for YHWH through his Son.
"""

TEXT_INFO = {
    "text_id": "matthew",
    "display_name": "Matthew (Kata Matthaion)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Gospels",
        "detail": "Matthew is the first book of the New Testament in all Christian canons and has "
                  "held that position since the earliest manuscript collections. It was the most "
                  "widely cited Gospel in the early church -- quoted more frequently than any other "
                  "Gospel by the Apostolic Fathers (Clement of Rome, Ignatius, Didache, Barnabas). "
                  "Its placement at the head of the NT canon was deliberate: Matthew bridges the "
                  "Old and New Testaments through its genealogy connecting Jesus to Abraham and "
                  "David, its extensive fulfillment quotations ('This was to fulfill what was spoken "
                  "by the prophet...'), and its presentation of Jesus as the new Moses who delivers "
                  "a new Torah from a new Sinai (the Sermon on the Mount). No Christian tradition "
                  "has ever questioned Matthew's canonical status. It was included in Marcion's "
                  "opponents' lists, the Muratorian Canon (~170 AD), Irenaeus' four-Gospel canon "
                  "(Against Heresies 3.11.8, ~180 AD), and every subsequent canonical list."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Matthew (Levi), the tax collector whom Jesus called from his toll booth "
                       "(Matt 9:9; 10:3). Papias of Hierapolis (~110 AD), quoted by Eusebius "
                       "(Hist. Eccl. 3.39.16), states: 'Matthew collected the oracles (ta logia) "
                       "in the Hebrew language, and each interpreted them as best he could.' "
                       "Irenaeus (Against Heresies 3.1.1, ~180 AD) affirms: 'Matthew also issued "
                       "a written Gospel among the Hebrews in their own dialect, while Peter and "
                       "Paul were preaching at Rome and laying the foundations of the Church.' "
                       "The church fathers unanimously attributed this Gospel to the apostle Matthew.",

        "scholarly_debate": "Modern scholarship widely holds that the Gospel of Matthew was not "
                           "written directly by the apostle Matthew but by an anonymous Jewish-Christian "
                           "author who drew upon the Gospel of Mark (about 90% of Mark appears in "
                           "Matthew, often verbatim in Greek) and a sayings source called Q (from "
                           "German Quelle, 'source') shared with Luke. This is the Two-Source "
                           "Hypothesis, the dominant model since the 19th century. The argument against "
                           "direct apostolic authorship: why would an eyewitness apostle copy extensively "
                           "from Mark, who was not an eyewitness? Papias' reference to ta logia 'in "
                           "the Hebrew language' may refer to a different composition (perhaps a "
                           "collection of Jesus' sayings or OT proof-texts) rather than the Greek Gospel "
                           "we have. Some scholars (Goodacre, 2002) reject Q entirely, arguing Matthew "
                           "used Mark alone and Luke used both Mark and Matthew (the Farrer Hypothesis). "
                           "Others (Hengel, France) defend Matthean authorship, arguing Papias is "
                           "reliable and the apostle may have composed an earlier Aramaic/Hebrew version "
                           "later expanded into the Greek Gospel. The Griesbach Hypothesis (championed "
                           "by Farmer) reverses the priority: Matthew was written first, Luke used "
                           "Matthew, and Mark abbreviated both.",

        "bottom_line": "The Gospel of Matthew, whether written by the apostle himself or by a "
                       "disciple within his circle drawing on apostolic tradition, is a masterful "
                       "theological composition by a deeply Jewish author steeped in the Hebrew "
                       "Scriptures. The author's expertise in Torah, his facility with rabbinic "
                       "argument patterns, and his concern for Jewish-Christian community issues "
                       "are evident throughout. The text is what it is regardless of authorship "
                       "debates -- the most comprehensive presentation of Jesus' teaching in the "
                       "New Testament."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Early church tradition places Matthew as the first Gospel written, "
                       "composed while the apostles were still in Jerusalem, perhaps as early "
                       "as the 40s-50s AD. If the apostle Matthew wrote it in Hebrew/Aramaic "
                       "first (as Papias and Irenaeus claim), the original could date to the "
                       "40s AD, with the Greek version following in the 50s-60s AD.",
        "critical_range": "Most critical scholars date Matthew to 80-90 AD, after the fall of "
                         "Jerusalem in 70 AD. Key arguments: (1) Matthew appears to use Mark, "
                         "which is itself dated to ~65-70 AD. (2) The parable of the wedding "
                         "banquet (Matt 22:7, 'The king sent his troops and destroyed those "
                         "murderers and burned their city') is widely read as a reference to "
                         "the Roman destruction of Jerusalem in 70 AD. (3) The developed "
                         "ecclesiology (Matt 16:18; 18:15-20) and concern with community "
                         "discipline suggest a later, more organized church. (4) The intense "
                         "polemic against the Pharisees (chapter 23) reflects post-70 tensions "
                         "between the emerging rabbinic movement and Jewish Christianity. Some "
                         "scholars (Robinson, Wenham) argue for a pre-70 date, noting that "
                         "Matt 22:7 could be prophetic language based on OT patterns rather "
                         "than a post-event description.",
        "evidence": "Key evidence includes: (1) Matthew's use of Mark (if Markan priority is "
                    "correct) sets a terminus post quem of ~65-70 AD. (2) The Didache (~90-100 "
                    "AD) quotes Matthew extensively, providing a terminus ante quem. (3) Ignatius "
                    "of Antioch (~110 AD) shows knowledge of Matthew. (4) The earliest manuscript "
                    "fragment is P104 (Papyrus Oxyrhynchus 4404), containing Matt 21:34-37, dated "
                    "to the late 2nd century. (5) P64+P67 (Magdalen Papyrus + Barcelona Papyrus), "
                    "containing portions of Matthew 3, 5, and 26, are dated to ~200 AD by most "
                    "papyrologists (Carsten Thiede's controversial redating to ~60 AD is not widely "
                    "accepted). (6) The Gospel's Sitz im Leben ('setting in life') points to a "
                    "Jewish-Christian community, likely in Antioch of Syria, processing its identity "
                    "in the aftermath of Jerusalem's destruction."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "A Jewish-Christian community, most likely in Antioch of Syria (the city "
                            "where believers were first called 'Christians,' Acts 11:26). This community "
                            "was navigating its dual identity: deeply rooted in Jewish tradition yet "
                            "following Jesus as Messiah. They faced pressure from the emerging rabbinic "
                            "movement (the Pharisaic party that reconstituted Judaism after 70 AD at "
                            "Yavneh/Jamnia) and needed a comprehensive account of Jesus' teaching to "
                            "ground their faith. Matthew's Gospel served as a catechetical manual -- a "
                            "structured presentation of Jesus' life and teaching for instruction, worship, "
                            "and apologetics within a community that still observed the Torah but understood "
                            "it through Jesus' authoritative interpretation.",

        "purpose": "Matthew writes to demonstrate that Jesus is the promised Messiah of Israel, the Son "
                   "of David and Son of Abraham (1:1), who fulfills the Hebrew Scriptures in every "
                   "dimension -- the Law (Sermon on the Mount), the Prophets (fulfillment quotations), "
                   "the Writings (Psalm 110 question, Psalm 22 passion), and the entire arc of salvation "
                   "history from Abraham to the eschaton. The Gospel has five major discourse blocks "
                   "(chapters 5-7, 10, 13, 18, 24-25), each ending with the formula 'When Jesus finished "
                   "these sayings...' -- possibly mirroring the five books of the Torah and presenting "
                   "Jesus as the new Moses who delivers the definitive Torah from the mountain.",

        "theological_intent": "Matthew's deepest theological claim is that in Jesus, the kingdom of heaven "
                             "(basileia ton ouranon -- Matthew's preferred term, equivalent to Mark and "
                             "Luke's 'kingdom of God') has invaded the present age. This is not merely a "
                             "political or social program but a cosmic event: the authority that Satan "
                             "offered Jesus over 'all the kingdoms of the world' (4:8) is the very authority "
                             "Jesus receives from the Father after the resurrection -- 'all authority in "
                             "heaven and on earth' (28:18). The kingdom advances through exorcism (12:28, "
                             "'if it is by the Spirit of God that I cast out demons, then the kingdom of "
                             "God has come upon you'), through the gathered community (16:18-19; 18:18-20), "
                             "and through the discipling of all nations (28:19) -- the Deuteronomy 32 "
                             "reversal enacted through the Great Commission."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek (with possible Aramaic/Hebrew Vorlage for some material)",
        "script": "Greek uncial script",
        "linguistic_notes": "Matthew's Greek is competent but heavily Semitic in character. The Gospel "
                           "contains numerous Hebraisms and Aramaisms: the phrase 'kingdom of heaven' "
                           "(basileia ton ouranon) reflects the Jewish reverential circumlocution for "
                           "'kingdom of God' (using 'heaven' as a substitute for the divine name). The "
                           "formula quotations ('This was to fulfill what the Lord had spoken by the "
                           "prophet...') follow a distinctive introductory pattern that differs from "
                           "Matthew's other OT citations, suggesting they may come from a pre-existing "
                           "collection of messianic proof-texts -- possibly Papias' ta logia. Matthew "
                           "preserves Aramaic words at key moments: 'Raka' (5:22, a term of contempt), "
                           "'Mammon' (6:24, wealth/possessions), 'Eli, Eli, lema sabachthani' (27:46, "
                           "'My God, my God, why have you forsaken me' -- quoting Psalm 22:1 in Aramaic). "
                           "The author demonstrates fluency in both the Hebrew (MT) and Greek (LXX) "
                           "texts of the Old Testament, sometimes citing one, sometimes the other, and "
                           "sometimes creating a mixed citation that draws on both.",
        "grammar_match": "Matthew's narrative style is more polished than Mark's but retains a Semitic "
                        "flavor distinct from Luke's literary Greek. The frequent use of 'then' (tote) "
                        "as a narrative connector (90 times in Matthew vs. 6 in Mark and 15 in Luke) is "
                        "characteristic. Matthew structures Jesus' teaching into five great discourses, "
                        "each introduced with narrative and concluded with the formula 'And when Jesus "
                        "finished...' (kai egeneto hote etelesen ho Iesous). This careful literary "
                        "architecture reflects a catechetical purpose -- the Gospel is designed for "
                        "teaching and memorization."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Matthew IS scripture -- the most extensively OT-connected Gospel, containing "
                   "over 60 direct OT quotations and hundreds of allusions.",
        "nt_usage": "Matthew contains more Old Testament quotations than any other Gospel. The "
                    "distinctive 'fulfillment quotations' (about 12-14, depending on counting) "
                    "explicitly claim that events in Jesus' life fulfill OT prophecy: the virgin "
                    "birth fulfills Isaiah 7:14 (Matt 1:22-23), the flight to Egypt fulfills "
                    "Hosea 11:1 (2:15), the massacre of the innocents fulfills Jeremiah 31:15 "
                    "(2:17-18), the Nazareth settlement fulfills 'what was spoken by the prophets' "
                    "(2:23), the Galilean ministry fulfills Isaiah 9:1-2 (4:14-16), Jesus' "
                    "healings fulfill Isaiah 53:4 (8:17), his parables fulfill Psalm 78:2 (13:35), "
                    "and the triumphal entry fulfills Zechariah 9:9 (21:4-5). Beyond the formula "
                    "quotations, Jesus himself cites or alludes to the OT constantly: Deuteronomy "
                    "in the temptation narrative (4:1-11), Psalm 110 in the question about David's "
                    "Lord (22:41-46), Daniel 7 in the Son of Man sayings throughout the Gospel, and "
                    "Psalm 22 from the cross (27:46).",
        "internal_consistency": "Matthew's use of the OT is sophisticated and theologically purposeful. "
                               "The genealogy (1:1-17) structures Israel's history into three sets of "
                               "14 generations (Abraham to David, David to exile, exile to Christ), "
                               "demonstrating that Jesus is the climax of salvation history. The Sermon on "
                               "the Mount (chapters 5-7) does not abolish the Torah but intensifies it -- "
                               "'You have heard that it was said... but I say to you' is not replacement "
                               "but authoritative interpretation by one greater than Moses. The five "
                               "discourse blocks may parallel the five books of Torah. Matthew's Jesus is "
                               "the embodiment of Israel's story: like Israel, he goes to Egypt (2:15), "
                               "passes through the waters (3:13-17), is tested in the wilderness for 40 "
                               "days (4:1-2), and delivers Torah from a mountain (5:1). Matthew reads the "
                               "entire OT as a christological narrative that finds its fulfillment in Jesus."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "The earliest manuscript evidence for Matthew includes P104 (Papyrus Oxyrhynchus "
                    "4404, containing Matt 21:34-37, dated late 2nd century), P64+P67 (Magdalen/"
                    "Barcelona Papyrus, containing portions of Matt 3, 5, 26, dated ~200 AD), and "
                    "P1 (Papyrus Oxyrhynchus 2, containing Matt 1:1-9, 12, 14-20, dated 3rd century). "
                    "The major uncial codices -- Sinaiticus (Aleph, 4th century), Vaticanus (B, 4th "
                    "century), Alexandrinus (A, 5th century), and Bezae (D, 5th century) -- all contain "
                    "Matthew as the first Gospel.",
        "major_witnesses": [
            {"name": "Papyrus P1 (P.Oxy. 2)", "date": "3rd century AD",
             "note": "One of the earliest papyrus fragments of Matthew, containing portions of "
                     "chapter 1. Found at Oxyrhynchus, Egypt."},
            {"name": "Codex Sinaiticus (Aleph)", "date": "4th century AD",
             "note": "The earliest complete NT manuscript. Contains the full text of Matthew. "
                     "Discovered by Tischendorf at St. Catherine's Monastery, Sinai (1844-1859)."},
            {"name": "Codex Vaticanus (B)", "date": "4th century AD",
             "note": "Generally considered the best overall NT manuscript. Contains Matthew in full. "
                     "Housed in the Vatican Library since at least the 15th century."},
            {"name": "Codex Bezae (D)", "date": "5th century AD",
             "note": "A bilingual Greek-Latin manuscript with many unique readings in Matthew, "
                     "sometimes called the 'Western text.' Important for text-critical study."}
        ],
        "reliability": "The text of Matthew is extremely well-attested. The major text-critical issues "
                       "include: (1) The ending of the Lord's Prayer -- 'For yours is the kingdom and "
                       "the power and the glory forever. Amen' (6:13b) is absent from the earliest and "
                       "best manuscripts (Sinaiticus, Vaticanus) and was likely a liturgical addition, "
                       "though it appears in many later manuscripts and the KJV. (2) Matt 16:2b-3 "
                       "(signs of the times) is absent from some important witnesses. (3) Matt 17:21 "
                       "(the fasting and prayer addition) is absent from the earliest manuscripts. (4) "
                       "Matt 18:11 ('For the Son of Man came to save the lost') is absent from the best "
                       "witnesses and was likely imported from Luke 19:10. Overall, the textual tradition "
                       "is stable, and no major theological point depends on a textual variant."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Matthew's Gospel was likely composed in the aftermath of the destruction of the "
                   "Jerusalem Temple in 70 AD, a catastrophic event that reshaped Judaism entirely. "
                   "With the Temple gone, the sacrificial system ended, the priesthood lost its "
                   "institutional base, and the Sadducees disappeared as a party. The Pharisaic movement, "
                   "led by Yohanan ben Zakkai at Yavneh (Jamnia), began reconstructing Judaism around "
                   "Torah study, synagogue worship, and rabbinic authority. Matthew's community -- Jewish "
                   "Christians who believed Jesus was the Messiah -- found themselves in increasing "
                   "tension with this emerging rabbinic Judaism. The heated polemic against the Pharisees "
                   "in chapter 23 ('Woe to you, scribes and Pharisees, hypocrites!') reflects this "
                   "intra-Jewish conflict. Matthew's Gospel argues that Jesus, not the rabbis, is the "
                   "authoritative interpreter of Torah.",

        "geography": "The Gospel's narrative moves through the geography of Israel: Bethlehem (birth, "
                     "chapters 1-2), Egypt (flight from Herod), Nazareth in Galilee (childhood, 2:23), "
                     "the Jordan River (baptism, 3:13-17), the Judean wilderness (temptation, 4:1-11), "
                     "Capernaum and the Sea of Galilee (the center of Jesus' ministry, 4:13-18:35), "
                     "Caesarea Philippi (Peter's confession, 16:13 -- at the base of Mount Hermon, "
                     "where 1 Enoch locates the descent of the Watchers), the Transfiguration mountain "
                     "(17:1-8), and finally Jerusalem (the passion, chapters 21-28). The Gospel's "
                     "composition is traditionally located in Antioch of Syria, a major city where "
                     "Jewish and Gentile Christians coexisted and where the Gospel's bilingual "
                     "(Jewish-Gentile) audience would make sense.",

        "historical_connections": "Matthew's Gospel connects to several major historical developments: "
                                 "(1) The Roman occupation of Judea under procurators (Pilate, 26-36 AD). "
                                 "(2) The Herodian dynasty: Herod the Great (the massacre of the innocents, "
                                 "2:16), Herod Antipas (the tetrarch who executed John the Baptist, 14:1-12). "
                                 "(3) The destruction of Jerusalem in 70 AD (reflected in 22:7 and the "
                                 "Olivet Discourse, chapters 24-25). (4) The emergence of the synagogue "
                                 "as the center of Jewish life (Matthew mentions synagogues 9 times, often "
                                 "with the phrase 'their synagogues,' suggesting the community has been "
                                 "expelled or is distancing itself). (5) The Gentile mission: Matthew's "
                                 "Gospel begins with Gentile Magi worshiping the king of the Jews (2:1-12) "
                                 "and ends with the commission to 'make disciples of all nations' (28:19)."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "significant",
        "summary": "Matthew presents Jesus as the one who defeats and displaces the rebellious "
                   "spiritual powers who have usurped authority over the nations. The divine council "
                   "framework illuminates virtually every major episode in the Gospel."
                   "\n\n"
                   "THE TEMPTATION (Matt 4:1-11): Satan offers Jesus 'all the kingdoms of the world "
                   "and their glory' (4:8). This is not a bluff -- Satan has this authority to offer. "
                   "In the Deuteronomy 32 worldview, the nations were allotted to the sons of God at "
                   "Babel, and these spiritual rulers have corrupted their governance. Satan, as the "
                   "chief adversary, exercises dominion over these territorial powers (cf. Luke 4:6, "
                   "'all this authority has been delivered to me'). Jesus refuses the shortcut: he will "
                   "reclaim the nations not by bowing to Satan but by going to the cross. Each of his "
                   "three responses quotes Deuteronomy (8:3, 6:16, 6:13) -- the very book that "
                   "established the Babel worldview."
                   "\n\n"
                   "THE KINGDOM HAS COME (Matt 12:22-29): When the Pharisees accuse Jesus of casting "
                   "out demons by Beelzebul (a variant of Baal-Zebub, 'lord of the flies,' or "
                   "Baal-Zebul, 'lord of the dwelling/high place' -- a deliberate degradation of a "
                   "Canaanite deity title applied to Satan), Jesus responds with a divine council "
                   "argument: 'If I cast out demons by the Spirit of God, then the kingdom of God "
                   "has come upon you (ephthasen eph hymas)' (12:28). The verb ephthasen is decisive "
                   "-- the kingdom has arrived, not merely approached. He then gives the parable of "
                   "binding the strong man (12:29): 'How can someone enter a strong man's house and "
                   "plunder his goods, unless he first binds the strong man?' Satan is the strong man. "
                   "His 'house' is the domain of the nations he controls. Jesus has come to bind him "
                   "and plunder his kingdom."
                   "\n\n"
                   "GATES OF HADES (Matt 16:18): At Caesarea Philippi -- a city at the base of Mount "
                   "Hermon associated with Pan worship and, in Jewish tradition (1 Enoch 6-7), the "
                   "site where the rebellious Watchers descended to corrupt humanity -- Jesus declares: "
                   "'On this rock I will build my church (ekklesia), and the gates of Hades will not "
                   "prevail against it' (16:18). 'Gates of Hades' is not merely a metaphor for death. "
                   "In the ancient worldview, gates are defensive structures: the gates of Hades are "
                   "the fortifications of the underworld powers. Jesus is not saying his church will "
                   "merely survive; he is saying it will be on the offensive, and the underworld's "
                   "defenses will crumble. The location at Hermon, where the Watchers fell, makes "
                   "this a cosmic declaration of war against the rebellious elohim."
                   "\n\n"
                   "PSALM 110 QUESTION (Matt 22:41-46): Jesus asks the Pharisees: 'If David calls him "
                   "Lord, how is he his son?' He quotes Psalm 110:1, where YHWH invites David's Lord "
                   "to sit at his right hand. This is the divine council session where the Messiah "
                   "is enthroned at YHWH's side -- the highest position in the heavenly assembly. "
                   "Jesus is identifying himself as the one who occupies the place at YHWH's right "
                   "hand, above all the elohim, above all angelic powers."
                   "\n\n"
                   "ALL AUTHORITY (Matt 28:18): The risen Jesus declares: 'All authority (pasa exousia) "
                   "in heaven and on earth has been given to me.' This is the Daniel 7:13-14 moment -- "
                   "the Son of Man receives all dominion from the Ancient of Days. It is also the "
                   "reversal of the temptation: Satan offered 'all the kingdoms of the world,' and "
                   "Jesus refused the shortcut. Now, through death and resurrection, he receives "
                   "'all authority' -- not from Satan, but from the Father. The Great Commission "
                   "that follows (28:19, 'Go therefore and make disciples of all nations') is the "
                   "Deuteronomy 32 reversal: the nations allotted to the sons of God at Babel are "
                   "now reclaimed for YHWH through the gospel proclaimed by the Son's followers.",

        "key_heiser_refs": [
            "The Unseen Realm, ch. 13-14 (Deuteronomy 32 worldview -- the nations allotted to the sons of God)",
            "The Unseen Realm, ch. 24-26 (the kingdom of God as reclamation of the nations)",
            "The Unseen Realm, ch. 33-34 (the Great Commission as Babel reversal)",
            "The Unseen Realm, ch. 4-5 (two powers in heaven -- Psalm 110 and the second YHWH figure)",
            "Supernatural, ch. 10-12 (Jesus and the war against the powers)",
            "Demons, ch. 4-6 (exorcism and the kingdom of God)",
            "The Naked Bible Podcast, ep. 109 (Psalm 89 and the divine council)",
            "The Naked Bible Podcast, ep. 173 (Psalm 110 and Melchizedek)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "The Synoptic Problem -- Why Do Matthew, Mark, and Luke Look So Similar?",
            "body": "Matthew, Mark, and Luke are called the 'Synoptic Gospels' (from Greek synoptikos, "
                    "'seen together') because they share a remarkably similar structure, sequence of "
                    "events, and often identical wording. The question of how they are related is called "
                    "the 'Synoptic Problem.' The dominant scholarly solution is the <strong>Two-Source "
                    "Hypothesis</strong>: Mark was written first, and Matthew and Luke independently used "
                    "Mark plus a second source called <strong>Q</strong> (from German Quelle, 'source') "
                    "-- a hypothetical collection of Jesus' sayings that no longer exists as an "
                    "independent document. This explains: (a) why about 90% of Mark appears in Matthew; "
                    "(b) why Matthew and Luke share about 235 verses not found in Mark (the Q material, "
                    "including the Lord's Prayer, the Beatitudes in their Lukan form, and many parables); "
                    "(c) why each Gospel also has unique material ('M' for Matthew-only material like the "
                    "Magi, the flight to Egypt, the Sermon on the Mount's full form; 'L' for Luke-only "
                    "material like the Prodigal Son, the Good Samaritan). Alternative theories exist: the "
                    "<strong>Augustinian Hypothesis</strong> (Matthew first, Mark abbreviated Matthew, "
                    "Luke used both); the <strong>Griesbach/Two-Gospel Hypothesis</strong> (Matthew first, "
                    "Luke used Matthew, Mark conflated both); the <strong>Farrer Hypothesis</strong> (Mark "
                    "first, Matthew used Mark, Luke used both Mark and Matthew -- no Q needed). None of "
                    "these theories is proven beyond doubt, but the Two-Source Hypothesis remains the "
                    "most widely accepted. The key insight for study: the differences between the Synoptics "
                    "are as theologically revealing as the similarities. When Matthew changes a Markan "
                    "passage, he does so for theological reasons -- pay attention to what he adds, omits, "
                    "or rearranges."
        },
        {
            "type": "theology",
            "title": "Kingdom of Heaven vs. Kingdom of God -- What's the Difference?",
            "body": "Matthew almost always uses 'kingdom of heaven' (basileia ton ouranon) where Mark and "
                    "Luke use 'kingdom of God' (basileia tou theou). Matthew uses 'kingdom of heaven' "
                    "about 32 times and 'kingdom of God' only 5 times. Why? This is <strong>not</strong> "
                    "a reference to a different kingdom or a different destination (heaven vs. earth). It "
                    "is a Jewish reverential practice called <strong>circumlocution</strong>: avoiding "
                    "direct use of God's name out of reverence. Just as Jews say 'HaShem' (The Name) "
                    "instead of pronouncing YHWH, Matthew's community substituted 'heaven' for 'God.' "
                    "The 'kingdom of heaven' is God's kingdom -- his reign, his authority, his rule "
                    "breaking into the present age. It is not about going to heaven when you die; it is "
                    "about heaven's authority coming to earth. When Jesus says 'the kingdom of heaven has "
                    "come near' (4:17), he means God's rule is invading the territory of the rebellious "
                    "powers. When he says 'the kingdom of heaven is like a mustard seed' (13:31), he "
                    "means God's reign starts small and grows to encompass everything. The kingdom is both "
                    "present (already invading through Jesus' ministry) and future (not yet fully "
                    "consummated until the Son of Man comes in glory, 25:31). This 'already/not yet' "
                    "tension is one of the most important theological frameworks in the NT."
        },
        {
            "type": "theology",
            "title": "Exorcism as Cosmic Warfare -- Why Demons Matter in Matthew",
            "body": "Modern Western readers often skip over exorcism accounts as embarrassing relics of "
                    "a pre-scientific worldview. This misses the entire theological point. In the divine "
                    "council framework, Jesus' exorcisms are not sideshows -- they are the central "
                    "evidence that the kingdom has arrived. When Jesus casts out demons, he is not "
                    "merely healing individuals; he is dismantling Satan's kingdom territory by territory, "
                    "person by person. Matthew 12:28 makes this explicit: 'If it is by the Spirit of God "
                    "that I cast out demons, then the kingdom of God has come upon you.' The exorcisms "
                    "prove the kingdom. They demonstrate that the 'strong man' (Satan) is being bound "
                    "(12:29) and his captives set free. The demons themselves recognize Jesus' authority: "
                    "in 8:29, the Gadarene demons cry out, 'What have you to do with us, Son of God? "
                    "Have you come here to torment us before the time?' -- they know the eschatological "
                    "judgment is coming and that Jesus has the authority to execute it. The 'time' they "
                    "reference is the final judgment of the rebellious elohim predicted in Psalm 82 and "
                    "Daniel 7. Every exorcism is a preview of that final judgment, a skirmish in the "
                    "cosmic war that the Son of Man came to win."
        },
        {
            "type": "interpretation",
            "title": "The Five Discourses -- Matthew's Torah Structure",
            "body": "Matthew organizes Jesus' teaching into five major discourse blocks, each concluded "
                    "with the formula 'When Jesus had finished these sayings...' (7:28; 11:1; 13:53; "
                    "19:1; 26:1). These are: (1) The <strong>Sermon on the Mount</strong> (chs. 5-7) -- "
                    "the 'Torah of the Kingdom,' covering righteousness, prayer, anxiety, and the two "
                    "ways. (2) The <strong>Mission Discourse</strong> (ch. 10) -- instructions for the "
                    "Twelve as they go out to announce the kingdom. (3) The <strong>Parables Discourse</strong> "
                    "(ch. 13) -- seven parables of the kingdom revealing its hidden, growing, costly, and "
                    "all-encompassing nature. (4) The <strong>Community Discourse</strong> (ch. 18) -- "
                    "instructions on humility, forgiveness, church discipline, and life together. (5) The "
                    "<strong>Eschatological Discourse</strong> (chs. 24-25) -- the Olivet Discourse on "
                    "the destruction of Jerusalem, the coming of the Son of Man, and the final judgment. "
                    "Many scholars see this five-part structure as deliberately echoing the five books of "
                    "the Torah (Pentateuch), presenting Jesus as the new Moses who delivers a new Torah. "
                    "Just as Moses delivered God's law from Mount Sinai, Jesus delivers the law of the "
                    "kingdom from the mountain (5:1). The parallel is not replacement but fulfillment: "
                    "'Do not think that I have come to abolish the Law or the Prophets; I have not come "
                    "to abolish them but to fulfill them' (5:17)."
        },
        {
            "type": "context",
            "title": "Caesarea Philippi and Mount Hermon -- The Geography of the Supernatural",
            "body": "When Matthew records Peter's confession and Jesus' declaration about the 'gates "
                    "of Hades' at Caesarea Philippi (16:13-20), the location is not incidental -- it "
                    "is theologically loaded. Caesarea Philippi sits at the base of <strong>Mount Hermon "
                    "</strong>, the highest peak in the region (9,232 feet). In 1 Enoch 6:6, Mount Hermon "
                    "is explicitly named as the place where the Watchers -- the rebellious sons of God "
                    "from Genesis 6:1-4 -- descended to earth, swore their oath of rebellion, and began "
                    "corrupting humanity. The name 'Hermon' (Hebrew: khermon) is related to the word "
                    "kherem ('devoted to destruction, banned, cursed'). The site was a center of "
                    "Pan worship in Jesus' day, with a cave shrine to Pan that was called 'the gates "
                    "of Hades' because it was believed to be an entrance to the underworld. Jesus "
                    "deliberately takes his disciples to this place -- the epicenter of cosmic rebellion "
                    "in Jewish tradition, the very spot where the Watchers fell -- and declares that he "
                    "will build his assembly and the gates of Hades will not stand against it. This is "
                    "a declaration of war at the enemy's front door. The Transfiguration (17:1-8) likely "
                    "takes place on Mount Hermon itself (the text says 'a high mountain' six days after "
                    "Caesarea Philippi), where Jesus is revealed in divine glory -- YHWH's presence on "
                    "the very mountain the Watchers had claimed."
        },
        {
            "type": "scholarship",
            "title": "The Great Commission as Babel Reversal",
            "body": "Matthew 28:18-20, the Great Commission, is the theological climax of the entire "
                    "Gospel and one of the most important passages in the Bible for understanding the "
                    "divine council narrative. Three elements converge: (1) 'All authority in heaven and "
                    "on earth has been given to me' -- Jesus claims the universal dominion that was "
                    "fractured at Babel when YHWH disinherited the nations and allotted them to the sons "
                    "of God (Deut 32:8-9). The authority Satan offered in 4:8-9 has now been legitimately "
                    "conferred by the Father through the resurrection. (2) 'Go therefore and make "
                    "disciples of all nations (panta ta ethne)' -- the very nations that were given over "
                    "to the sons of God are now being reclaimed. The word ethne is the same word used in "
                    "the LXX of Deuteronomy 32:8 for the nations that were divided. (3) 'Baptizing them "
                    "in the name of the Father and of the Son and of the Holy Spirit' -- the nations are "
                    "being transferred from the authority of the territorial elohim to the authority of "
                    "the triune God. The Great Commission is the program by which the Deuteronomy 32 "
                    "disinheritance is reversed: every nation, once under the governance of corrupt "
                    "spiritual powers, is invited into YHWH's family through the gospel of the Son. "
                    "This is why Matthew ends where it does -- not with the ascension (as Luke does) "
                    "but with the commission. The story is not over; the reclamation of the nations is "
                    "the ongoing work of the church until the Son of Man returns."
        }
    ]
}
