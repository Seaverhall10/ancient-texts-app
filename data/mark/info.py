"""
info.py -- Mark (Kata Markon): Scholarly Text Introduction

This file provides the "front page" for Mark in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Mark is the Gospel of urgent action -- the shortest, most fast-paced, and
most visceral of the four Gospels. Written with breathless urgency (the
word euthys, "immediately," appears over 40 times), Mark presents Jesus as
the powerful Son of God whose true identity is hidden under the "messianic
secret" until it is revealed at the cross. Through its divine council lens,
Mark shows Jesus as the divine warrior who has come to bind the strong man
(Satan), plunder his kingdom through exorcisms and healings, and inaugurate
the reign of God. The demons recognize him immediately ("I know who you
are -- the Holy One of God!" Mark 1:24), while the human characters
struggle to understand. The Transfiguration reveals his divine glory on
the mountain; the centurion at the cross confesses his divine identity.
Mark's theology is one of revelation through suffering: the Son of God
must suffer, die, and rise, and his followers must take up their crosses
and follow the same path.
"""

TEXT_INFO = {
    "text_id": "mark",
    "display_name": "Mark (Kata Markon)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Gospels",
        "detail": "Mark is the second Gospel in the New Testament canon and has been recognized as "
                  "canonical scripture from the earliest period of the church. It appears in all "
                  "ancient canonical lists: the Muratorian Canon (~170 AD), Irenaeus' four-Gospel "
                  "canon (Against Heresies 3.11.8, ~180 AD), the Cheltenham Canon (~360 AD), "
                  "Athanasius' 39th Festal Letter (367 AD), and the councils of Hippo (393) and "
                  "Carthage (397). In the early church, Mark was the least cited Gospel -- "
                  "overshadowed by Matthew's comprehensive teaching and John's theological depth. "
                  "Augustine called Mark a 'follower and abbreviator' of Matthew (De Consensu "
                  "Evangelistarum 1.2.4). This changed dramatically in the 19th century when "
                  "scholars recognized Mark as most likely the earliest Gospel, the source behind "
                  "Matthew and Luke. Since then, Mark has moved from the margins to the center of "
                  "Gospel scholarship."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "John Mark, a companion of both Peter and Paul. Papias of Hierapolis (~110 AD), "
                       "quoted by Eusebius (Hist. Eccl. 3.39.15), gives the earliest testimony: 'Mark, "
                       "having become Peter's interpreter (hermeneutes), wrote down accurately, though "
                       "not in order, everything that he remembered of the things said or done by the "
                       "Lord. For he neither heard the Lord nor followed him, but afterward, as I said, "
                       "he followed Peter, who adapted his teaching to the needs of the moment.' "
                       "Irenaeus (Against Heresies 3.1.1) affirms: 'After their departure [Peter and "
                       "Paul's death], Mark, the disciple and interpreter of Peter, did also hand down "
                       "to us in writing what had been preached by Peter.' The Anti-Marcionite Prologue "
                       "(~160-180 AD) and Clement of Alexandria (in Eusebius, Hist. Eccl. 6.14.6) "
                       "support the Peter-Mark connection. John Mark appears in Acts 12:12, 25; 13:5, "
                       "13; 15:37-39 (Paul's companion who left the first missionary journey), "
                       "Colossians 4:10 (Barnabas' cousin), 2 Timothy 4:11 ('Get Mark and bring him "
                       "with you, for he is useful to me for ministry'), Philemon 24, and 1 Peter 5:13 "
                       "('She who is at Babylon... sends you greetings, and so does Mark, my son').",

        "scholarly_debate": "Most scholars accept that the author was likely a second-generation "
                           "Christian named Mark, possibly the John Mark of Acts, writing on the basis "
                           "of Petrine tradition. The Peter-Mark connection is widely regarded as "
                           "plausible but not certain. Some scholars note that the Gospel shows limited "
                           "knowledge of Palestinian geography (e.g., the route through Sidon to the "
                           "Sea of Galilee in 7:31 is geographically roundabout), suggesting the "
                           "author may have been from outside Palestine. Others argue the geographical "
                           "difficulties are exaggerated or reflect ancient travel routes. The Gospel's "
                           "Latinisms (kenturion for centurion, 15:39; spekoulator for executioner, "
                           "6:27; quadrans for coin, 12:42) have been used to support a Roman origin, "
                           "though Latinisms were common throughout the empire.",

        "bottom_line": "Mark's Gospel, whether by the John Mark of Acts or another early Christian "
                       "named Mark, represents the earliest written narrative of Jesus' ministry. Its "
                       "connection to Petrine tradition is supported by the earliest external evidence "
                       "and is consistent with the Gospel's content: vivid eyewitness details, Peter's "
                       "prominent but unflattering portrayal, and the raw emotional intensity of the "
                       "narrative. The text gives us the closest thing we have to a rapid-fire, "
                       "street-level account of Jesus' war against the powers of darkness."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Ancient tradition places Mark's composition in Rome during or shortly after "
                       "Peter's ministry there. Irenaeus says Mark wrote 'after the departure (exodon) "
                       "of Peter and Paul' -- most likely after their martyrdom under Nero (~64-67 AD). "
                       "Clement of Alexandria, however, says Mark wrote while Peter was still alive.",
        "critical_range": "Most scholars date Mark to ~65-70 AD. The upper boundary is set by the "
                         "Olivet Discourse (Mark 13): some argue it reflects knowledge of the Jewish "
                         "War (66-70 AD) and the Temple's imminent destruction, while others note that "
                         "the discourse lacks the specificity you would expect from a post-70 writer "
                         "(no mention of fire, which was how the Temple was actually destroyed). The "
                         "lower boundary is set by the need for sufficient time for oral tradition to "
                         "develop and for an audience that needs the Gospel's explanations of Jewish "
                         "customs (7:3-4) and Aramaic words (5:41; 7:34; 15:34). Most scholars place "
                         "composition in Rome, during or just after the Neronian persecution (64 AD), "
                         "or in Syria.",
        "evidence": "Key evidence includes: (1) Papias' testimony (~110 AD) linking Mark to Peter's "
                    "preaching. (2) The Gospel's use by Matthew and Luke (if the Two-Source Hypothesis "
                    "is correct), requiring a date early enough for both to access it. (3) The Latinisms "
                    "and explanations of Jewish customs suggesting a Gentile audience, consistent with "
                    "Rome. (4) The theme of persecution and suffering, consistent with the Neronian "
                    "period. (5) P45 (Chester Beatty Papyrus I), dated to the 3rd century, is the "
                    "earliest substantial papyrus of Mark. (6) Codex Sinaiticus and Vaticanus (4th "
                    "century) contain the full text, ending at 16:8 (the shorter ending)."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "A predominantly Gentile Christian community, most likely in Rome, facing "
                            "persecution or the threat of persecution. This is indicated by: (1) Mark's "
                            "explanations of Jewish customs (7:3-4, the washing of hands; 14:12, Passover "
                            "explanation; 15:42, day of Preparation). (2) Translation of Aramaic phrases "
                            "(5:41, 'Talitha koum'; 7:34, 'Ephphatha'; 15:34, 'Eloi, Eloi, lema "
                            "sabachthani'). (3) The use of Latin loanwords. (4) The emphasis on "
                            "suffering discipleship -- 'If anyone would come after me, let him deny "
                            "himself and take up his cross and follow me' (8:34) -- which speaks directly "
                            "to a community facing martyrdom.",

        "purpose": "Mark writes to present Jesus as the powerful Son of God whose divine authority is "
                   "revealed paradoxically through suffering and death. The Gospel moves relentlessly "
                   "toward the cross, revealing that true messiahship involves not conquest but sacrifice. "
                   "For a community under persecution, this message is existentially urgent: the path of "
                   "the disciple follows the path of the master. Mark's narrative theology answers the "
                   "question: if Jesus is the all-powerful Son of God, why does he suffer? And why "
                   "must his followers suffer?",

        "theological_intent": "Mark's central theological motif is the 'messianic secret' -- Jesus "
                             "repeatedly commands demons, disciples, and healed people not to reveal his "
                             "identity (1:25, 34, 44; 3:12; 5:43; 7:36; 8:26, 30; 9:9). This is not a "
                             "literary device but a theological statement: Jesus' true identity cannot be "
                             "understood apart from the cross. The demons know who he is ('the Holy One of "
                             "God,' 1:24; 'the Son of God,' 3:11; 'Son of the Most High God,' 5:7), but "
                             "premature revelation without the cross leads to a triumphalist misunderstanding. "
                             "The secret is lifted only at the Transfiguration (for three disciples, 9:2-8), "
                             "at the trial ('I am,' 14:62), and at the cross, where the centurion -- a "
                             "Gentile -- makes the definitive confession: 'Truly this man was the Son of "
                             "God' (15:39). The divine council implications are profound: the Son of God's "
                             "identity is revealed not in a display of raw power but at the moment of "
                             "ultimate vulnerability."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek",
        "script": "Greek uncial script",
        "linguistic_notes": "Mark's Greek is the simplest and most colloquial of the four Gospels. His "
                           "style is characterized by parataxis (sentences connected by kai, 'and,' "
                           "rather than subordinate clauses), the historic present tense (151 times -- "
                           "vivid, as if narrating events happening right now), frequent use of euthys "
                           "('immediately,' over 40 times), and diminutive forms (korasion, 'little "
                           "girl'; paidiou, 'little child'; kunarion, 'little dog'). The effect is "
                           "breathless urgency -- events tumble forward at breakneck speed. Mark "
                           "preserves Aramaic words and translates them for his audience: 'Boanerges, "
                           "that is, Sons of Thunder' (3:17); 'Talitha koum, which means, Little girl, "
                           "I say to you, arise' (5:41); 'Ephphatha, that is, Be opened' (7:34); 'Abba, "
                           "Father' (14:36); 'Eloi, Eloi, lema sabachthani, which means, My God, my "
                           "God, why have you forsaken me?' (15:34). These Aramaic preservations likely "
                           "reflect the oral tradition behind the Gospel, possibly Peter's own words "
                           "as remembered by Mark.",
        "grammar_match": "Mark's grammar was considered rough even in antiquity, which is partly why "
                        "Matthew and Luke smoothed many of Mark's constructions when incorporating his "
                        "material. But the roughness is part of the power: Mark's Gospel reads like an "
                        "urgent, breathless eyewitness account, not a polished literary composition. "
                        "The vivid details -- Jesus sleeping on a cushion in the stern (4:38), looking "
                        "around in anger (3:5), being moved with compassion (1:41) or indignation "
                        "(10:14) -- create an intimate, almost cinematic portrait of Jesus."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Mark IS scripture -- the earliest narrative Gospel, foundational to the NT witness.",
        "nt_usage": "Mark contains fewer direct OT quotations than Matthew but weaves OT allusions "
                    "throughout the narrative. The Gospel opens with a composite quotation combining "
                    "Malachi 3:1 ('Behold, I send my messenger before your face') and Isaiah 40:3 "
                    "('The voice of one crying in the wilderness: Prepare the way of the Lord') -- "
                    "attributed to 'Isaiah the prophet' (1:2-3). Key OT references include: the "
                    "baptismal voice combining Psalm 2:7 and Isaiah 42:1 (1:11), the hardening "
                    "language of Isaiah 6:9-10 applied to the parables (4:12), the feeding miracles "
                    "evoking Exodus 16 and 2 Kings 4 (6:30-44; 8:1-10), the Transfiguration evoking "
                    "Sinai (9:2-8), Psalm 118:22-23 quoted in the parable of the tenants (12:10-11), "
                    "Daniel 7:13 in the Son of Man sayings (13:26; 14:62), Psalm 22 from the cross "
                    "(15:34), and Zechariah 13:7 on the scattering of the disciples (14:27).",
        "internal_consistency": "Mark's use of the OT is more allusive than Matthew's explicit "
                               "fulfillment formula but equally deliberate. The opening citation of Isaiah "
                               "40:3 frames the entire Gospel as the story of YHWH's return -- the God "
                               "who promised through Isaiah to come back to his people is now coming in "
                               "the person of Jesus. The exodus motif runs throughout: Jesus passes through "
                               "the waters (baptism), enters the wilderness (temptation), feeds the people "
                               "in the wilderness (feeding miracles), and crosses the sea (lake crossings). "
                               "The 'way' (hodos) motif -- anticipated in the opening citation ('prepare "
                               "the way of the Lord') -- structures the central section (8:22-10:52) as a "
                               "journey on 'the way' to Jerusalem and the cross."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "P45 (Chester Beatty Papyrus I), dating to the 3rd century, is the earliest "
                    "substantial manuscript of Mark, containing portions of chapters 4-12. The major "
                    "uncial codices (Sinaiticus, Vaticanus, Alexandrinus, Bezae) contain Mark in full, "
                    "though the ending is a major text-critical issue.",
        "major_witnesses": [
            {"name": "Codex Sinaiticus (Aleph)", "date": "4th century AD",
             "note": "Ends Mark at 16:8 ('for they were afraid'). The longer ending (16:9-20) is "
                     "absent. This is one of the strongest witnesses for the shorter ending."},
            {"name": "Codex Vaticanus (B)", "date": "4th century AD",
             "note": "Also ends Mark at 16:8. The scribe left a blank column after 16:8, possibly "
                     "aware of a longer ending but choosing not to include it."},
            {"name": "Codex Alexandrinus (A)", "date": "5th century AD",
             "note": "Contains the longer ending (16:9-20)."},
            {"name": "Codex Bezae (D)", "date": "5th century AD",
             "note": "Contains the longer ending, with some unique variants."}
        ],
        "reliability": "The text of Mark is well-preserved, with one major text-critical issue: the "
                       "ending. Mark 16:9-20 (the 'Longer Ending') is absent from the two best and "
                       "earliest manuscripts (Sinaiticus and Vaticanus), and the early church fathers "
                       "Clement of Alexandria and Origen show no knowledge of it. Eusebius and Jerome "
                       "note that the passage is absent from most manuscripts known to them. The "
                       "vocabulary, style, and theology of 16:9-20 differ from the rest of Mark. Most "
                       "scholars conclude that Mark originally ended at 16:8: 'And they went out and "
                       "fled from the tomb, for trembling and astonishment had seized them, and they "
                       "said nothing to anyone, for they were afraid (ephobounto gar).' This abrupt "
                       "ending -- in the middle of a sentence, ending with 'for' (gar) -- is either "
                       "the original ending (intentionally abrupt, forcing the reader to respond) or "
                       "the result of the original ending being lost. The Longer Ending was added later "
                       "to provide resurrection appearances. It is canonical in the sense that it has "
                       "been part of the received text for centuries, but it was not written by Mark."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Mark's Gospel was most likely written in Rome during or just after the Neronian "
                   "persecution (64-67 AD). After the Great Fire of Rome (July 64 AD), Nero blamed "
                   "Christians and subjected them to horrific punishments: they were covered in animal "
                   "skins and torn apart by dogs, crucified, or set on fire to illuminate Nero's "
                   "gardens (Tacitus, Annals 15.44). Tradition holds that both Peter and Paul were "
                   "martyred during this persecution. Mark's Gospel, with its relentless emphasis on "
                   "suffering, the cost of discipleship, and the paradox of a crucified Messiah, "
                   "speaks directly to a community that has watched its leaders die and wonders what "
                   "faithfulness looks like in the face of state violence.",

        "geography": "The Gospel's narrative geography moves from the Judean wilderness (baptism, 1:4-9), "
                     "to Galilee (the center of Jesus' ministry, 1:14 - 9:50), with excursions into "
                     "Gentile territory (the Gerasene/Gadarene region, 5:1-20; Tyre and Sidon, 7:24-31; "
                     "the Decapolis, 7:31-37; Caesarea Philippi, 8:27), then the journey to Jerusalem "
                     "(10:1-52), and finally Jerusalem itself (11:1 - 16:8). The movements into Gentile "
                     "territory are theologically significant: Jesus' power extends beyond Israel into the "
                     "domain of the nations -- the territory of the other elohim.",

        "historical_connections": "Mark's Gospel connects to: (1) The ministry of John the Baptist in "
                                 "the Judean wilderness, connected to the Qumran community's eschatological "
                                 "expectations. (2) The political situation under Herod Antipas (executed "
                                 "John the Baptist, 6:14-29) and the Roman occupation. (3) The Jewish "
                                 "sectarian landscape: Pharisees, Sadducees, Herodians, and scribes all "
                                 "appear as opponents. (4) The Neronian persecution in Rome, the likely "
                                 "context for the Gospel's composition. (5) The approaching Jewish War "
                                 "(66-70 AD), which the Olivet Discourse (chapter 13) anticipates."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "significant",
        "summary": "Mark presents Jesus as the divine warrior who invades Satan's territory, binds the "
                   "strong man, and begins reclaiming the cosmos for YHWH. The exorcism narratives are "
                   "not sideshows but the main event -- they are the evidence that the kingdom of God "
                   "has arrived."
                   "\n\n"
                   "BINDING THE STRONG MAN (Mark 3:27): After the Beelzebul accusation, Jesus declares: "
                   "'No one can enter a strong man's house and plunder his goods, unless he first binds "
                   "the strong man. Then indeed he may plunder his house.' Satan is the strong man. His "
                   "'house' is the domain he controls -- the nations and peoples held under the authority "
                   "of the rebellious elohim. Jesus has come to bind him and liberate the captives. Every "
                   "exorcism is an act of plundering -- taking back what the enemy has stolen."
                   "\n\n"
                   "LEGION (Mark 5:1-20): The Gerasene demoniac is possessed by a spirit that identifies "
                   "itself as 'Legion, for we are many' (5:9). A Roman legion was 5,000-6,000 soldiers "
                   "-- the name is both literal (many demons) and political (the demonic occupation "
                   "mirrors the Roman occupation). The demons beg not to be sent 'out of the country' "
                   "(5:10) -- they want to remain in their territory, reflecting the Deuteronomy 32 "
                   "worldview of territorial spiritual jurisdiction. They are sent into pigs (unclean "
                   "animals) that rush into the sea (the realm of chaos). The liberated man becomes "
                   "the first Gentile missionary: 'Go home to your friends and tell them how much the "
                   "Lord has done for you' (5:19)."
                   "\n\n"
                   "THE TRANSFIGURATION (Mark 9:2-8): On a high mountain (likely Hermon), Jesus is "
                   "transfigured: 'his clothes became radiant, intensely white' (9:3). Moses and Elijah "
                   "appear. The voice from the cloud declares: 'This is my beloved Son; listen to him' "
                   "(9:7). In the divine council framework, this is a heavenly council session on earth: "
                   "the Son is identified by the Father in the presence of two witnesses (the Law and "
                   "the Prophets), and the command to 'listen to him' establishes his authority above "
                   "Moses and Elijah -- above the old covenant entirely."
                   "\n\n"
                   "COSMIC SIGNS AND ANGELIC GATHERING (Mark 13:24-27): At the end of the age, 'the "
                   "sun will be darkened, and the moon will not give its light, and the stars will be "
                   "falling from heaven, and the powers in the heavens will be shaken' (13:24-25). "
                   "'The powers' (hai dynameis) are the spiritual forces governing the cosmos -- their "
                   "shaking signals the collapse of the old order. The Son of Man comes in clouds 'with "
                   "great power and glory' and sends 'his angels' to 'gather his elect from the four "
                   "winds' (13:26-27). The divine council executes the Son of Man's will.",

        "key_heiser_refs": [
            "The Unseen Realm, ch. 24-26 (the kingdom of God as reclamation of the nations)",
            "The Unseen Realm, ch. 33 (the binding of the strong man and the plundering of his house)",
            "Demons, ch. 4-6 (exorcism and the kingdom of God in Mark)",
            "Supernatural, ch. 10-12 (Jesus and the war against the powers)",
            "The Naked Bible Podcast, ep. 94-95 (the Gerasene demoniac and spiritual geography)",
            "The Naked Bible Podcast, ep. 173 (Psalm 110, the divine Son, and the Transfiguration)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Messianic Secret -- Why Does Jesus Hide His Identity?",
            "body": "One of the most striking features of Mark's Gospel is Jesus' repeated command to "
                    "keep his identity secret. He silences demons who identify him (1:25, 34; 3:11-12), "
                    "instructs healed people not to tell anyone (1:44; 5:43; 7:36; 8:26), and commands "
                    "the disciples not to reveal his messiahship (8:30; 9:9). This pattern, identified "
                    "by William Wrede in 1901, is called the <strong>messianic secret</strong>. Why would "
                    "the Son of God hide his identity?<br><br>"
                    "Several explanations have been proposed: (1) <strong>Historical</strong>: Jesus wanted "
                    "to avoid premature arrest by Roman authorities who would see a messianic claim as "
                    "political insurrection. (2) <strong>Theological</strong>: Jesus' identity cannot be "
                    "properly understood apart from the cross. A messiah who is merely powerful is a "
                    "triumphalist distortion. The secret is lifted progressively: at the Transfiguration "
                    "(9:2-8, for three disciples), at the trial (14:62, publicly), and at the cross, where "
                    "the centurion makes the full confession (15:39). Only when you see the crucified "
                    "Messiah do you understand who Jesus truly is. (3) <strong>Divine council</strong>: "
                    "the demons know Jesus' identity because they are spiritual beings with access to "
                    "heavenly knowledge ('the Holy One of God,' 1:24; 'the Son of God,' 3:11; 'Son of "
                    "the Most High God,' 5:7). They recognize the Son's authority immediately. But their "
                    "knowledge is premature disclosure -- the revelation must come through the path of "
                    "suffering, not through demonic testimony. The irony is powerful: the spiritual "
                    "beings understand what the human characters cannot."
        },
        {
            "type": "context",
            "title": "The Ending of Mark -- Where Does It Really End?",
            "body": "Mark's ending is the most significant text-critical problem in the New Testament. The "
                    "two best and earliest manuscripts (Codex Sinaiticus and Codex Vaticanus, both 4th "
                    "century) end at 16:8: 'And they went out and fled from the tomb, for trembling and "
                    "astonishment had seized them, and they said nothing to anyone, for they were afraid.' "
                    "The Longer Ending (16:9-20) -- containing resurrection appearances, the Great "
                    "Commission, snake handling, and the ascension -- was added later by a different "
                    "author. The evidence is strong: (a) absent from the best manuscripts; (b) early "
                    "church fathers (Clement, Origen) show no knowledge of it; (c) Eusebius and Jerome "
                    "note its absence from most manuscripts; (d) the vocabulary and style differ markedly "
                    "from the rest of Mark; (e) 16:9 introduces Mary Magdalene as if for the first time, "
                    "though she appeared in 15:40, 47 and 16:1.<br><br>"
                    "So did Mark intend to end at 16:8? Three views: (1) <strong>Yes -- the abrupt ending "
                    "is intentional</strong>. Mark ends with fear and silence, forcing the reader to "
                    "respond: Will you be afraid, or will you go and tell? The empty tomb and the angel's "
                    "message ('He is risen, he is not here,' 16:6) are the proclamation; the reader must "
                    "complete the story with faith. (2) <strong>No -- the original ending was lost</strong>. "
                    "The final leaf of Mark's scroll was damaged or torn off, and the text we have is "
                    "incomplete. (3) <strong>No -- Mark was interrupted</strong> (by arrest, death, or "
                    "other circumstances) and never finished. Most modern scholars favor option 1 or 2."
        },
        {
            "type": "interpretation",
            "title": "Exorcism in Mark -- The Kingdom's Front Line",
            "body": "Mark contains more exorcism accounts than any other Gospel, and they are not "
                    "incidental stories but the primary evidence of the kingdom's arrival. Mark's first "
                    "recorded miracle is an exorcism (1:21-28), and exorcisms dominate the early chapters. "
                    "The pattern is consistent: (1) the demon recognizes Jesus ('I know who you are -- "
                    "the Holy One of God!' 1:24), (2) Jesus commands silence (the messianic secret), and "
                    "(3) Jesus expels the demon with authoritative command. The demons' recognition is "
                    "theologically crucial: they are spiritual beings who know the identity of the divine "
                    "Son from the heavenly realm. They fear him because they know the judgment is coming. "
                    "The exorcisms demonstrate that Jesus is not merely a teacher or healer but the divine "
                    "warrior who has entered enemy territory to dismantle Satan's kingdom. Mark 3:27 makes "
                    "this explicit: Jesus is binding the strong man and plundering his house. Every "
                    "exorcism is an act of liberation -- a captive freed from the enemy's jurisdiction "
                    "and transferred to the kingdom of God."
        },
        {
            "type": "scholarship",
            "title": "Markan Priority -- Why Most Scholars Think Mark Was Written First",
            "body": "Since Karl Lachmann (1835), most NT scholars have held that Mark was the first "
                    "Gospel written, and that Matthew and Luke independently used Mark as a source. "
                    "The evidence includes: (1) <strong>Content overlap</strong>: About 90% of Mark's "
                    "content appears in Matthew, and about 50% in Luke. This is most easily explained if "
                    "Mark was the source. (2) <strong>Order agreement</strong>: When Matthew and Luke "
                    "differ from Mark's order, they never agree with each other against Mark. Mark's "
                    "order is the constant. (3) <strong>Improvement of style</strong>: Matthew and Luke "
                    "consistently smooth Mark's rough Greek, clarify his ambiguities, and soften his "
                    "harsh portrayals (e.g., Mark 6:5, 'he could do no mighty work,' becomes Matt 13:58, "
                    "'he did not do many mighty works'). This is easier to explain as improvement of a "
                    "source than as deliberate roughening. (4) <strong>The harder reading</strong>: Mark "
                    "often has the more difficult reading, which Matthew and Luke soften. This follows "
                    "the text-critical principle that the harder reading is more likely original. "
                    "Markan priority is not universally accepted -- the Griesbach Hypothesis (Matthean "
                    "priority) and the Augustinian Hypothesis have defenders -- but it remains the "
                    "dominant scholarly position."
        }
    ]
}
