"""
era_mark_servant.py -- Mark 1-16: The Servant King Who Conquers Through Suffering

Mark's entire Gospel is a single, relentless narrative arc from baptism to empty
tomb. There are no birth narratives, no genealogy, no Sermon on the Mount -- Mark
plunges immediately into the action: "The beginning of the gospel of Jesus Christ,
the Son of God" (1:1). The first half (1-8) reveals Jesus' power through exorcisms,
healings, and nature miracles while the messianic secret conceals his identity.
Peter's confession at Caesarea Philippi (8:29) is the turning point: from there,
Jesus turns toward Jerusalem and the cross. The second half (8-16) reveals that
the Son of God must suffer, die, and rise. The Transfiguration, the passion, and
the empty tomb form the climax of a Gospel that redefines power as service,
conquest as sacrifice, and divine glory as a crucified king.
"""

CHAPTERS = [
    {
        "id": "mark-1",
        "ref": "Mark 1",
        "chapter_num": 1,
        "title": "The Beginning -- Baptism, Temptation, and the First Exorcism",
        "era": "mark_servant",
        "type": "study",

        "synopsis": "Mark begins without a birth narrative or genealogy: 'The beginning of the gospel "
                    "(euangelion) of Jesus Christ, the Son of God' (1:1). The word euangelion ('good "
                    "news') was used in the Roman world for imperial proclamations -- the birth of an "
                    "emperor, a military victory, the accession of a new ruler. Mark co-opts the term: "
                    "the true good news is not Caesar's but God's. John the Baptist appears as the "
                    "Isaianic voice preparing 'the way of the Lord' (1:2-3). Jesus is baptized, the "
                    "heavens are 'torn open' (schizomenous, 1:10 -- a violent rupture, not a gentle "
                    "opening), the Spirit descends, and the Father declares: 'You are my beloved Son; "
                    "with you I am well pleased' (1:11). The Spirit immediately 'drives' (ekballei, "
                    "1:12 -- the same verb used for casting out demons) Jesus into the wilderness for "
                    "40 days of temptation. Mark's account is compressed: 'He was with the wild animals, "
                    "and the angels were ministering to him' (1:13) -- a picture of the new Adam at "
                    "peace with creation, served by divine council members. Jesus begins his ministry "
                    "proclaiming: 'The time is fulfilled (peplerotai), and the kingdom of God is at hand "
                    "(engiken); repent and believe in the gospel' (1:15). His first miracle is an "
                    "exorcism in the Capernaum synagogue -- the demon cries 'I know who you are -- the "
                    "Holy One of God!' (1:24). Jesus silences it and casts it out. The crowd is "
                    "astonished: 'What is this? A new teaching with authority (exousia)! He commands "
                    "even the unclean spirits, and they obey him' (1:27).",

        "key_verse": {
            "ref": "Mark 1:15",
            "text": "The time is fulfilled, and the kingdom of God is at hand; repent and believe in the gospel.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "euangelion (gospel / good news -- imperial proclamation language co-opted for God's kingdom; the announcement that YHWH is king)",
            "schizo (to tear / to rip -- the heavens are 'torn open' at the baptism (1:10) and the Temple veil is 'torn' at the death (15:38); same verb, forming an inclusio)",
            "pneuma akatharton (unclean spirit -- a hostile spiritual being that oppresses humans; 'unclean' because it belongs to the realm opposed to God's holiness)",
            "ho hagios tou theou (the Holy One of God -- the demon's recognition of Jesus' divine identity; a divine council designation)",
            "exousia (authority -- Jesus' teaching and exorcisms are characterized by authority that surpasses the scribes; divine council authority operating on earth)",
            "euthys (immediately -- Mark's signature word, appearing over 40 times; creates a sense of relentless urgency and divine momentum)"
        ],

        "ane_backdrop": "Mark's opening citation combines Malachi 3:1 ('I send my messenger before your "
                        "face') and Isaiah 40:3 ('Prepare the way of the Lord'). In Isaiah 40, the 'way "
                        "of the Lord' is YHWH's return from exile -- God himself coming back to his "
                        "people through the wilderness. Mark identifies Jesus' coming as the fulfillment "
                        "of YHWH's promised return. The 'tearing open' of the heavens (1:10) echoes "
                        "Isaiah 64:1: 'Oh that you would rend (qara) the heavens and come down!' The "
                        "violent rupture of the barrier between heaven and earth signals that the divine "
                        "council is intervening in the human realm. The 40-day temptation recapitulates "
                        "Israel's 40-year wilderness testing and Moses' 40 days on Sinai. Jesus being "
                        "'with the wild animals' (1:13) evokes the Edenic picture of the first human in "
                        "harmony with creation before the Fall, as well as the eschatological vision of "
                        "Isaiah 11:6-9 where the wolf dwells with the lamb. The angels ministering to him "
                        "are divine council members attending the Son after his victory over the adversary.",

        "second_temple": [
            {
                "source": "Testament of Levi 18:10-12 (2nd century BC - 1st century AD)",
                "summary": "A messianic priest will open the gates of paradise, remove the threatening "
                           "sword, and give the saints access to the tree of life. 'Beliar shall be bound "
                           "by him, and he shall grant to his children the authority to trample on wicked "
                           "spirits.'",
                "relevance": "Parallels Mark's presentation of Jesus as the one who binds the strong man "
                             "and gives authority over unclean spirits to his followers (3:15; 6:7)."
            },
            {
                "source": "1QS 3:13-4:26 (Community Rule -- Two Spirits Treatise)",
                "summary": "The Qumran Community Rule describes the cosmic conflict between the Spirit "
                           "of Truth and the Spirit of Falsehood, with all humanity divided between them. "
                           "God has appointed a time when evil will be destroyed.",
                "relevance": "Provides the Second Temple context for Mark's dualistic presentation: the "
                             "Spirit (1:10, 12) versus the unclean spirits (1:23, 26), light versus "
                             "darkness, the kingdom of God versus Satan's domain."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 40:3", "note": "'A voice cries: In the wilderness prepare the way of the LORD' -- the opening citation identifying Jesus' coming as YHWH's return", "type": "ot"},
            {"ref": "Isaiah 64:1", "note": "'Oh that you would rend the heavens and come down!' -- the prayer answered when the heavens are 'torn open' at Jesus' baptism", "type": "ot"},
            {"ref": "Psalm 2:7", "note": "'You are my Son' -- echoed in the baptismal voice (1:11), identifying Jesus as the enthroned king of Psalm 2", "type": "ot"},
            {"ref": "Isaiah 42:1", "note": "'My chosen, in whom my soul delights' -- echoed in 'with you I am well pleased,' identifying Jesus as the Servant", "type": "ot"},
            {"ref": "Genesis 1:2", "note": "The Spirit hovering over the waters -- the Spirit descending at Jesus' baptism signals a new creation", "type": "ot"},
            {"ref": "Matthew 3:13-4:11", "note": "Matthew's expanded parallel: three specific temptations with Deuteronomy responses; Mark's compressed account emphasizes the wild animals and angels", "type": "nt"},
            {"ref": "Luke 4:31-37", "note": "Luke's parallel to the Capernaum exorcism -- nearly identical, confirming Mark as the source", "type": "nt"}
        ],

        "divine_council_note": "Mark 1 is a divine council invasion narrative. The heavens are 'torn "
                               "open' (schizomenous, 1:10) -- not gently parted but violently ripped, "
                               "as if the barrier between the heavenly council chamber and the earth has "
                               "been breached by force. Through this rupture, the Spirit descends on Jesus "
                               "and the Father's voice speaks the enthronement decree from Psalm 2:7 and "
                               "the Servant commissioning from Isaiah 42:1. The same Spirit then 'drives' "
                               "(ekballei) Jesus into the wilderness to confront the adversary -- using "
                               "the same verb Mark uses for exorcism. The wilderness encounter with Satan "
                               "is the first battle in the cosmic war; the angels ministering afterward "
                               "are divine council members attending the victorious Son. The first public "
                               "miracle is not a healing but an exorcism (1:21-28): the demon in the "
                               "synagogue identifies Jesus as 'the Holy One of God' (ho hagios tou theou) "
                               "-- a title used in the OT for YHWH himself and for his consecrated "
                               "servants. The demon's knowledge comes from the spiritual realm: it "
                               "recognizes a member of the divine council who has entered the earthly "
                               "domain to wage war. 'Have you come to destroy us?' (1:24) -- the demon "
                               "knows the eschatological judgment has begun. Jesus silences it ('Be quiet!' "
                               "-- phimotheti, literally 'be muzzled') and expels it. The cosmic war has "
                               "begun, and the Son of God is winning.",

        "sections": [
            {
                "heading": "The Way Prepared: Baptism and Temptation (1:1-15)",
                "body": "Mark opens with a declaration: 'The beginning (arche) of the gospel (euangelion) "
                        "of Jesus Christ (Christos), the Son of God (huios theou)' (1:1). Every word is "
                        "loaded: arche echoes Genesis 1:1 ('In the beginning'); euangelion is the Roman "
                        "imperial term for a proclamation of good news (a new emperor, a victory); "
                        "Christos is the Greek translation of Meshiach; 'Son of God' is the title from "
                        "Psalm 2:7 that establishes the king's divine relationship. John the Baptist "
                        "appears in the wilderness (1:4), baptizing for repentance. Jesus comes from "
                        "Nazareth and is baptized in the Jordan. 'And when he came up out of the water, "
                        "immediately (euthys) he saw the heavens being torn open (schizomenous) and the "
                        "Spirit descending on him like a dove' (1:10). The voice declares: 'You are my "
                        "beloved Son (su ei ho huios mou ho agapetos); with you I am well pleased' (1:11). "
                        "Note: Mark's voice speaks to Jesus ('You are...'), while Matthew's speaks about "
                        "him ('This is...'). The Spirit then 'drives' (ekballei) him into the wilderness "
                        "for 40 days of testing with Satan. Mark's account is spare: 'he was with the "
                        "wild animals, and the angels were ministering to him' (1:13). After John's "
                        "arrest, Jesus proclaims: 'The time is fulfilled (peplerotai ho kairos), and "
                        "the kingdom of God is at hand (engiken he basileia tou theou); repent and "
                        "believe in the gospel' (1:15)."
            },
            {
                "heading": "The First Exorcism: Authority Revealed (1:16-45)",
                "body": "Jesus calls four fishermen -- Simon, Andrew, James, and John -- 'and immediately "
                        "(euthys) they left their nets and followed him' (1:18, 20). In the Capernaum "
                        "synagogue, 'immediately (euthys) there was in their synagogue a man with an "
                        "unclean spirit' (1:23). The demon cries out: 'What have you to do with us (ti "
                        "hemin kai soi), Jesus of Nazareth? Have you come to destroy us (elthes apolesai "
                        "hemas)? I know who you are (oida se tis ei) -- the Holy One of God (ho hagios "
                        "tou theou)!' (1:24). The plural 'us' suggests the demon speaks for the entire "
                        "spiritual opposition -- 'Have you come to destroy us?' is a question about the "
                        "eschatological judgment of all rebellious spirits. The recognition formula ('I "
                        "know who you are') is a defensive maneuver: in ancient magical practice, knowing "
                        "someone's name or identity gave power over them. The demon tries to use Jesus' "
                        "identity as a weapon. Jesus refuses the gambit: 'Be silent (phimotheti, 'be "
                        "muzzled'), and come out of him!' (1:25). The spirit convulses the man and exits "
                        "'with a loud cry' (1:26). The crowd is amazed: 'A new teaching with authority! "
                        "He commands even the unclean spirits, and they obey him' (1:27). That evening, "
                        "he heals Peter's mother-in-law and 'the whole city was gathered together at the "
                        "door' (1:33). He heals many and casts out many demons, and 'would not permit the "
                        "demons to speak, because they knew him' (1:34) -- the messianic secret enforced."
            }
        ]
    },

    {
        "id": "mark-2-5",
        "ref": "Mark 2-5",
        "chapter_num": 2,
        "title": "Conflict, Parables, and Power Over Demons, Sea, and Death",
        "era": "mark_servant",
        "type": "study",

        "synopsis": "Mark 2-5 escalates both the conflict and the revelation. Five controversy stories "
                    "(2:1-3:6) establish opposition: Jesus claims authority to forgive sins (2:1-12), "
                    "eats with sinners (2:13-17), doesn't fast (2:18-22), breaks Sabbath tradition "
                    "(2:23-28), and heals on the Sabbath (3:1-6). The Pharisees and Herodians begin "
                    "plotting his destruction (3:6). Jesus appoints the Twelve (3:13-19), faces the "
                    "Beelzebul accusation (3:22-30 -- the strong man parable), teaches in parables "
                    "(4:1-34), and then demonstrates his authority in four dramatic miracles: stilling "
                    "the storm (4:35-41), exorcising Legion (5:1-20), healing the hemorrhaging woman "
                    "(5:25-34), and raising Jairus' daughter from the dead (5:21-24, 35-43). Each "
                    "miracle reveals a new domain under Jesus' authority: nature, demons, disease, "
                    "and death.",

        "key_verse": {
            "ref": "Mark 3:27",
            "text": "But no one can enter a strong man's house and plunder his goods, unless he first binds the strong man. Then indeed he may plunder his house.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "exousia (authority -- Jesus' authority to forgive sins (2:10), over the Sabbath (2:28), and over demons, nature, disease, and death)",
            "ischuros (strong man -- Satan as the fortified ruler whose house Jesus is plundering; the core of Mark's cosmic warfare theology)",
            "Legeon (Legion -- 'for we are many' (5:9); the name evokes the Roman military unit; demonic occupation parallels political occupation)",
            "Talitha koum (Aramaic: 'Little girl, arise' -- Jesus' command to the dead girl; preserved in the original language for its power and intimacy)",
            "parabole (parable -- Jesus teaches the crowds in parables (4:2), revealing the kingdom's secrets to insiders while hiding them from outsiders (4:11-12))",
            "huios tou theou tou hypsistou (Son of the Most High God -- Legion's title for Jesus (5:7); 'Most High' (hypsistos/elyon) is the divine council title for YHWH)"
        ],

        "ane_backdrop": "The stilling of the storm (4:35-41) draws on the ANE divine warrior's mastery "
                        "of chaotic waters: Baal defeats Yam (Sea) in the Ugaritic texts; Marduk defeats "
                        "Tiamat in the Enuma Elish; YHWH rebukes the sea in Psalm 104:7; 106:9; and "
                        "Job 38:8-11. Jesus' command 'Peace! Be still!' (4:39) uses the same language as "
                        "his exorcism commands -- he rebukes (epetimesen, 4:39) the wind, treating the "
                        "storm as a hostile spiritual force. The Gerasene demoniac (5:1-20) lives 'among "
                        "the tombs' (5:3) -- the realm of the dead and unclean -- in Gentile territory "
                        "(the Decapolis, indicated by the pig herd). The demons' request not to be sent "
                        "'out of the country' (5:10) reflects the territorial jurisdiction of spiritual "
                        "powers in the Deuteronomy 32 worldview.",

        "second_temple": [
            {
                "source": "1 Enoch 15:8-12",
                "summary": "The spirits of the dead giants (offspring of the Watchers and human women) "
                           "become evil spirits on earth: 'They shall be called evil spirits... they "
                           "shall destroy without incurring judgment... until the day of the great "
                           "consummation.'",
                "relevance": "The Enochic tradition provides the Second Temple framework for understanding "
                             "demons as distinct from fallen angels: demons are the disembodied spirits of "
                             "the Nephilim, which is why they seek to inhabit human bodies (as Legion does)."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 107:23-32", "note": "'He made the storm be still, and the waves of the sea were hushed' -- YHWH's power over the sea; Jesus exercises this same authority", "type": "ot"},
            {"ref": "Job 38:8-11", "note": "'Who shut in the sea with doors... and said, \"Here shall your proud waves be stayed\"?' -- divine authority over chaotic waters", "type": "ot"},
            {"ref": "Isaiah 65:1-4", "note": "People 'who sit in tombs and spend the night in secret places, who eat pig's flesh' -- the Gerasene demoniac's condition echoes Isaiah's description of apostasy", "type": "ot"},
            {"ref": "Matthew 8:28-34", "note": "Matthew's parallel: two demoniacs (Mark has one), briefer account, less dialogue with the demons", "type": "nt"},
            {"ref": "Luke 8:26-39", "note": "Luke's parallel: closely follows Mark but smooths some details; the healed man wants to follow Jesus but is sent home as a missionary", "type": "nt"},
            {"ref": "1 Enoch 15:8-12", "note": "The disembodied spirits of the Nephilim become demons on earth -- the Enochic tradition behind Mark's demonology", "type": "noncanonical"}
        ],

        "divine_council_note": "Mark 3:27 -- the strong man parable -- is the interpretive key to the "
                               "entire Gospel. Satan is the 'strong man' (ischuros) who has fortified his "
                               "'house' -- the domain of the nations and peoples under the authority of the "
                               "rebellious elohim. Jesus has come to 'bind' (desai) the strong man and "
                               "'plunder' (diarpasai) his house -- every exorcism, every healing, every "
                               "act of liberation is plunder taken from the enemy. The Gerasene demoniac "
                               "(5:1-20) is the supreme example: a man in Gentile territory, living among "
                               "the dead, possessed by 'Legion' (a demonic army), and completely under "
                               "the enemy's control. Jesus liberates him with a word. The demons' request "
                               "to stay 'in the country' (5:10) reflects the Deuteronomy 32 territorial "
                               "framework: they want to remain in their assigned region. Their title for "
                               "Jesus -- 'Son of the Most High God' (huios tou theou tou hypsistou, 5:7) "
                               "-- is a divine council designation: 'Most High' (hypsistos/elyon) is the "
                               "title of the supreme God of the council (Deut 32:8, 'When the Most High "
                               "gave to the nations their inheritance'). The demons know exactly who they "
                               "are facing: the Son of the God who presides over all the elohim. Their "
                               "entry into the pigs and the pigs' rush into the sea is a picture of chaos "
                               "returning to chaos -- the unclean spirits entering unclean animals and "
                               "both being swallowed by the sea (the domain of primordial chaos). The "
                               "stilling of the storm uses the same authority: Jesus 'rebukes' "
                               "(epetimesen) the wind and commands the sea 'Be muzzled!' (pephimoso -- "
                               "the same verb used to silence the demon in 1:25). Nature's chaos and "
                               "demonic oppression are dealt with by the same authority.",

        "sections": [
            {
                "heading": "Five Controversies and the Beelzebul Accusation (2:1 - 3:35)",
                "body": "Five conflict stories establish the pattern of opposition that will lead to "
                        "the cross. Jesus heals a paralytic and claims 'The Son of Man has authority "
                        "(exousia) on earth to forgive sins' (2:10) -- a prerogative that belongs to "
                        "God alone. He eats with tax collectors and sinners (2:15-17). He is asked why "
                        "his disciples don't fast; he responds with the new wine/old wineskins teaching "
                        "(2:21-22) -- the kingdom cannot be contained in old forms. He defends his "
                        "disciples plucking grain on the Sabbath with 'The Son of Man is lord even of "
                        "the Sabbath' (2:28). He heals a man with a withered hand on the Sabbath (3:1-5), "
                        "provoking the Pharisees and Herodians to plot 'how to destroy him' (3:6). Jesus "
                        "appoints the Twelve 'to be with him and to be sent out to preach and have "
                        "authority to cast out demons' (3:14-15). Scribes from Jerusalem accuse him of "
                        "casting out demons by Beelzebul (3:22). Jesus responds with the strong man "
                        "parable (3:27): Satan is being bound, his house is being plundered. Blasphemy "
                        "against the Holy Spirit -- attributing the Spirit's work to Satan -- is the "
                        "eternal sin (3:28-29)."
            },
            {
                "heading": "Parables, the Storm, and Legion (4:1 - 5:20)",
                "body": "Jesus teaches in parables by the sea (4:1-34): the Sower (4:3-20), the lamp "
                        "under a basket (4:21-25), the seed growing secretly (4:26-29, unique to Mark), "
                        "and the mustard seed (4:30-32). The parables reveal 'the secret (mysterion) of "
                        "the kingdom of God' (4:11) -- the kingdom is hidden, growing, and certain of "
                        "its harvest. Then three demonstrations of authority: (1) The storm stilling "
                        "(4:35-41): Jesus sleeps in the stern while the storm rages. Awakened, he "
                        "rebukes the wind and commands the sea: 'Peace! Be still!' (Siopa, pephimoso -- "
                        "'Silence! Be muzzled!'). The disciples are terrified: 'Who then is this, that "
                        "even the wind and the sea obey him?' (4:41). (2) The Gerasene demoniac (5:1-20): "
                        "In Gentile territory, a man 'with an unclean spirit' lives among the tombs, "
                        "cuts himself with stones, and cannot be chained. The spirit declares: 'What "
                        "have you to do with me, Jesus, Son of the Most High God? I adjure you by God, "
                        "do not torment me' (5:7). The demon's name is 'Legion, for we are many' (5:9). "
                        "Jesus sends them into pigs (about 2,000), which rush into the sea (5:13). The "
                        "healed man is told: 'Go home to your friends and tell them how much the Lord "
                        "has done for you' (5:19) -- no secrecy here; in Gentile territory, the message "
                        "can be proclaimed."
            },
            {
                "heading": "The Hemorrhaging Woman and Jairus' Daughter (5:21-43)",
                "body": "Two interlocked stories -- a narrative 'sandwich' (intercalation), Mark's "
                        "favorite literary technique. Jairus, a synagogue ruler, begs Jesus to heal his "
                        "dying daughter (5:22-24). On the way, a woman 'who had suffered from a discharge "
                        "of blood for twelve years' (5:25) touches Jesus' garment. She has spent all she "
                        "had on physicians and 'was no better but rather grew worse' (5:26). She touches "
                        "his cloak and is immediately healed. Jesus feels 'power (dynamin) had gone out "
                        "from him' (5:30). He identifies her: 'Daughter, your faith (pistis) has made you "
                        "well; go in peace' (5:34). Meanwhile, word comes that Jairus' daughter has died. "
                        "Jesus says: 'Do not fear, only believe (pisteuon)' (5:36). At the house, he "
                        "takes the girl's hand and says 'Talitha koum' -- preserved in Aramaic: 'Little "
                        "girl, I say to you, arise' (5:41). She rises immediately. 'And they were "
                        "immediately overcome with amazement' (5:42). He commands secrecy (5:43). The two "
                        "stories contrast: the woman has been suffering for 12 years; the girl is 12 "
                        "years old. Both are female, both are ritually unclean (bleeding and death), "
                        "and both are restored by Jesus' power and the response of faith."
            }
        ]
    },

    {
        "id": "mark-6-8",
        "ref": "Mark 6-8:21",
        "chapter_num": 3,
        "title": "Feeding Miracles, Gentile Ministry, and the Bread of Life",
        "era": "mark_servant",
        "type": "study",

        "synopsis": "Mark 6-8 expands the kingdom's reach beyond Israel into Gentile territory while "
                    "deepening the blindness motif. Jesus is rejected at Nazareth: 'A prophet is not "
                    "without honor, except in his hometown' (6:4). He sends the Twelve on a mission "
                    "with authority over unclean spirits (6:7). John the Baptist is executed (6:14-29). "
                    "Jesus feeds 5,000 Jews (6:30-44), walks on the water (6:45-52), and heals in "
                    "Gennesaret. He confronts Pharisaic tradition on purity (7:1-23), declaring 'all "
                    "foods clean' (7:19) -- breaking the barrier between Jew and Gentile. He heals the "
                    "Syrophoenician woman's daughter (7:24-30) and a deaf-mute in the Decapolis "
                    "(7:31-37), then feeds 4,000 in Gentile territory (8:1-10). The two feedings are "
                    "parallel: one for Jews (12 baskets, the 12 tribes), one for Gentiles (7 baskets, "
                    "the completeness of the nations). Jesus warns against 'the leaven of the Pharisees "
                    "and the leaven of Herod' (8:15), and the disciples still don't understand (8:17-21).",

        "key_verse": {
            "ref": "Mark 7:37",
            "text": "And they were astonished beyond measure, saying, 'He has done all things well. He even makes the deaf hear and the mute speak.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Ephphatha (Aramaic: 'Be opened' -- Jesus' command to the deaf-mute (7:34); preserved in the original language; the opening of ears and tongue in Gentile territory)",
            "koinos (common / unclean -- the Pharisaic purity concern; Jesus declares that defilement comes from the heart, not from food (7:15-23))",
            "artos (bread -- the central symbol of the feeding miracles; 'bread' is mentioned 20+ times in 6:30-8:21, creating a 'bread section')",
            "dynamis (power/miracle -- 'he could do no mighty work (dynamin) there' in Nazareth (6:5); not inability but the connection between faith and the kingdom's operation)",
            "porosis (hardness -- 'their hearts were hardened' (6:52; 8:17); the disciples' incomprehension despite witnessing the miracles)"
        ],

        "ane_backdrop": "The feeding miracles echo the manna in the wilderness (Exod 16), Elisha's "
                        "multiplication of loaves (2 Kings 4:42-44), and the messianic banquet "
                        "prophecies (Isa 25:6-8). Jesus walking on the sea (6:45-52) is a theophany: "
                        "YHWH alone 'tramples the waves of the sea' (Job 9:8). The phrase 'he meant "
                        "to pass by them' (6:48) uses the same language as YHWH 'passing by' Moses on "
                        "Sinai (Exod 33:19-22) and Elijah on Horeb (1 Kings 19:11) -- a divine self-"
                        "revelation. The declaration 'all foods clean' (7:19) demolishes the Jewish-"
                        "Gentile purity boundary that had separated Israel from the nations since Sinai. "
                        "In the Deuteronomy 32 framework, this is explosive: if the food laws no longer "
                        "separate Israel from the nations, the barrier between YHWH's people and the "
                        "nations under the other elohim is being dismantled.",

        "second_temple": [
            {
                "source": "2 Baruch 29:5-8 (late 1st century AD)",
                "summary": "In the messianic age, 'the earth shall yield its fruit ten-thousand-fold "
                           "and on each vine there shall be a thousand branches... The treasury of "
                           "manna shall again descend from on high.'",
                "relevance": "The expectation that the Messiah's age would feature miraculous abundance "
                             "of food -- exactly what the feeding miracles demonstrate."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 16", "note": "The manna in the wilderness -- the feeding miracles present Jesus as the one who provides bread from God, surpassing Moses", "type": "ot"},
            {"ref": "2 Kings 4:42-44", "note": "Elisha feeds 100 with 20 loaves and has some left over -- Jesus feeds thousands with less and has more left over", "type": "ot"},
            {"ref": "Job 9:8", "note": "'He alone stretches out the heavens and treads on the waves of the sea' -- YHWH's exclusive prerogative, exercised by Jesus", "type": "ot"},
            {"ref": "Isaiah 35:5-6", "note": "'The ears of the deaf will be unstopped; the tongue of the mute will shout for joy' -- fulfilled in the healing of the deaf-mute (7:31-37)", "type": "ot"},
            {"ref": "Acts 10:9-16", "note": "Peter's vision declaring all foods clean -- the theological revolution Jesus initiated in Mark 7:19 continued in the apostolic mission", "type": "nt"},
            {"ref": "Matthew 14:13 - 16:12", "note": "Matthew's expanded parallel: same sequence of feedings, walking on water, and bread discussions", "type": "nt"}
        ],

        "divine_council_note": "The two feeding miracles form a deliberate parallel that reveals the "
                               "scope of the kingdom's provision. The feeding of the 5,000 (6:30-44) "
                               "occurs in Jewish territory: 12 baskets of leftovers, symbolizing the 12 "
                               "tribes of Israel. The feeding of the 4,000 (8:1-10) occurs in Gentile "
                               "territory (the Decapolis): 7 baskets of leftovers, with 7 as the number "
                               "of completeness, symbolizing the fullness of the nations. Together they "
                               "declare: the Messiah feeds both Israel and the nations -- the Deuteronomy "
                               "32 division is being overcome. Jesus' walking on the sea (6:45-52) is a "
                               "divine council self-revelation: in the OT, treading on the waves is "
                               "exclusively YHWH's prerogative (Job 9:8; Hab 3:15; Ps 77:19). Jesus' "
                               "words 'Take heart; it is I' (6:50) use the Greek ego eimi -- potentially "
                               "the divine self-identification 'I AM' (cf. Exod 3:14 LXX). The "
                               "Syrophoenician woman's healing (7:24-30) is crucial: a Gentile woman's "
                               "faith secures deliverance for her demon-oppressed daughter. This is the "
                               "kingdom crossing into the territory of the nations -- plundering the "
                               "strong man's house in Gentile land. Jesus' declaration that 'all foods "
                               "are clean' (7:19) dismantles the purity boundary that separated Israel "
                               "from the nations -- preparing for the Great Commission's universal scope.",

        "sections": [
            {
                "heading": "Nazareth Rejection, the Twelve Sent, and John's Death (6:1-29)",
                "body": "At Nazareth, Jesus' hometown, the people take offense: 'Is not this the "
                        "carpenter, the son of Mary?' (6:3). Their unbelief limits his work: 'he could "
                        "do no mighty work there' (6:5) -- not inability but the connection between "
                        "faith and the kingdom's operation. He sends the Twelve in pairs with authority "
                        "over unclean spirits (6:7), instructing them to travel light and preach "
                        "repentance. The mission report is interrupted by the flashback to John the "
                        "Baptist's execution (6:14-29) -- a dark story of Herod's guilt, Herodias' "
                        "revenge, Salome's dance, and a head on a platter. The kingdom's forerunner "
                        "is murdered by the powers of this age -- foreshadowing what will happen to "
                        "the King himself."
            },
            {
                "heading": "Two Feedings and the Breach of Purity (6:30 - 8:21)",
                "body": "The feeding of the 5,000 (6:30-44): five loaves, two fish, 12 baskets "
                        "remaining. Jesus walks on the sea (6:45-52): 'He meant to pass by them' -- "
                        "theophanic 'passing by' language. 'Take heart; it is I (ego eimi). Do not be "
                        "afraid' (6:50). The controversy over purity (7:1-23) leads to Jesus' "
                        "revolutionary declaration: 'There is nothing outside a person that by going "
                        "into him can defile him' (7:15). Mark adds: '(Thus he declared all foods "
                        "clean)' (7:19). In Tyre, the Syrophoenician woman persists despite Jesus' "
                        "initial reply about the children's bread (7:27-28), and her daughter is healed. "
                        "In the Decapolis, Jesus heals a deaf-mute with 'Ephphatha' (7:34) -- fulfilling "
                        "Isaiah 35:5-6 in Gentile territory. The feeding of the 4,000 (8:1-10) in "
                        "Gentile territory: seven loaves, seven baskets remaining. Jesus warns against "
                        "'the leaven of the Pharisees and of Herod' (8:15). The disciples are confused; "
                        "Jesus questions: 'Do you not yet understand (oupō noeite)?' (8:21). Despite "
                        "two feedings, they remain blind."
            }
        ]
    },

    {
        "id": "mark-8-10",
        "ref": "Mark 8:22 - 10:52",
        "chapter_num": 4,
        "title": "Peter's Confession, the Transfiguration, and the Way to the Cross",
        "era": "mark_servant",
        "type": "study",

        "synopsis": "This central section of Mark is framed by two healings of blind men (8:22-26; "
                    "10:46-52) -- a literary inclusio symbolizing the gradual opening of the disciples' "
                    "eyes. At Caesarea Philippi, Peter confesses 'You are the Christ' (8:29), but "
                    "immediately stumbles at the passion prediction: 'Get behind me, Satan!' (8:33). "
                    "Three times Jesus predicts his death and resurrection (8:31; 9:31; 10:33-34), and "
                    "three times the disciples misunderstand: Peter rebukes him, the Twelve argue about "
                    "greatness, and James and John request thrones. After each misunderstanding, Jesus "
                    "teaches the way of suffering discipleship. The Transfiguration (9:2-8) is the "
                    "theological center: Jesus' divine glory is revealed on the mountain, with Moses "
                    "and Elijah as witnesses, and the Father's voice commands 'Listen to him.' This "
                    "section teaches: the path to glory passes through suffering -- for the Messiah "
                    "and for all who follow him.",

        "key_verse": {
            "ref": "Mark 9:7",
            "text": "And a cloud overshadowed them, and a voice came out of the cloud, 'This is my beloved Son; listen to him.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Christos (Christ/Anointed One -- Peter's confession at Caesarea Philippi: 'You are the Christ' (8:29); the messianic identity finally named by a human)",
            "metamorphoo (transfigured -- Jesus' form is changed to reveal his divine glory; the inner reality made visible)",
            "lytron (ransom -- 'the Son of Man came to give his life as a ransom for many' (10:45); the liberation price paid to free captives from bondage)",
            "ho pais (the servant/child -- greatness in the kingdom is measured by becoming servant (diakonos) and slave (doulos) of all)",
            "dei (it is necessary -- 'the Son of Man must (dei) suffer many things' (8:31); divine necessity, the council's predetermined plan)"
        ],

        "ane_backdrop": "The Transfiguration combines multiple ANE and OT theophanic elements: the "
                        "radiant garments recall the divine glory visible on sacred mountains (Sinai, "
                        "Exod 24:15-17; 34:29-30); the cloud is the shekinah, the visible manifestation "
                        "of YHWH's presence (Exod 40:34-35; 1 Kings 8:10-11); the divine voice from the "
                        "cloud parallels the Sinai revelation. Mount Hermon, the likely location, was "
                        "in the ANE world the northern cosmic mountain -- the equivalent of Mount Zaphon "
                        "in Ugaritic mythology, where the gods assembled. The Transfiguration on Hermon "
                        "is YHWH's Son revealed in glory on the mountain the Watchers had claimed -- a "
                        "divine reclamation of rebel territory.",

        "second_temple": [
            {
                "source": "1 Enoch 6:1-6",
                "summary": "The Watchers descend on Mount Hermon and swear their oath of rebellion. "
                           "Hermon is explicitly named as the site of the cosmic transgression.",
                "relevance": "If the Transfiguration occurs on Hermon (the 'high mountain' near "
                             "Caesarea Philippi), it is a direct counterclaim: the Son of God's glory "
                             "revealed on the very mountain the Watchers defiled."
            },
            {
                "source": "2 Peter 1:16-18",
                "summary": "Peter reflects on the Transfiguration: 'We were eyewitnesses of his "
                           "majesty. For when he received honor and glory from God the Father, and "
                           "the voice was borne to him by the Majestic Glory...'",
                "relevance": "Peter's testimony confirms the Transfiguration's significance as a "
                             "genuine divine encounter, not merely a vision or literary creation."
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 7:13-14", "note": "The Son of Man receives all authority -- the background to Mark's 'Son of Man must suffer' predictions; suffering precedes enthronement", "type": "ot"},
            {"ref": "Isaiah 53:10-12", "note": "The Servant gives himself as a guilt offering and bears the sins of many -- the background to 'a ransom for many' (10:45)", "type": "ot"},
            {"ref": "Exodus 34:29-30", "note": "Moses' shining face after meeting YHWH on Sinai -- the Transfiguration surpasses this: Jesus does not reflect glory but radiates his own", "type": "ot"},
            {"ref": "Deuteronomy 18:15", "note": "'A prophet like me [Moses]... you shall listen to him' -- echoed in the command 'Listen to him' (9:7)", "type": "ot"},
            {"ref": "Matthew 16:13 - 17:13", "note": "Matthew's expanded parallel: Peter's confession includes 'Son of the living God,' the rock/keys saying, and the Transfiguration", "type": "nt"},
            {"ref": "Philippians 2:5-11", "note": "The Christ hymn: the pattern of humiliation leading to exaltation that Mark's central section embodies", "type": "nt"}
        ],

        "divine_council_note": "The central section of Mark reveals the divine council's plan in its "
                               "most paradoxical form: the Son of God must suffer. The word 'must' (dei, "
                               "8:31) indicates divine necessity -- not mere historical probability but the "
                               "decreed plan of the heavenly council. Peter's attempt to prevent the "
                               "suffering earns the title 'Satan' (8:33) because opposing the cross means "
                               "opposing the council's plan -- it is literally the adversary's strategy to "
                               "prevent the redemption. The Transfiguration (9:2-8) is the supreme divine "
                               "council theophany in Mark: on the mountain (likely Hermon, the Watchers' "
                               "mountain), Jesus radiates divine glory in the presence of Moses and "
                               "Elijah -- the Law and the Prophets as council witnesses. The cloud "
                               "(nephele) is the shekinah, the visible manifestation of YHWH's presence. "
                               "The voice from the cloud repeats the Psalm 2:7/Isaiah 42:1 declaration "
                               "from the baptism ('This is my beloved Son') and adds the Deuteronomy "
                               "18:15 command ('listen to him'). The three passion predictions (8:31; "
                               "9:31; 10:33-34) reveal the divine council's script: the Son of Man will "
                               "be delivered (paradidotai, present passive -- 'is being handed over,' "
                               "9:31, suggesting an ongoing divine action), killed, and after three days "
                               "rise. The ransom saying (10:45) provides the theological interpretation: "
                               "the Son of Man's death is a lytron (ransom) that liberates 'many' from "
                               "bondage to sin, death, and the hostile powers. This is the price of "
                               "reclaiming the nations from the strong man's house.",

        "sections": [
            {
                "heading": "Peter's Confession and the First Passion Prediction (8:22-9:1)",
                "body": "The section opens with the two-stage healing of a blind man at Bethsaida "
                        "(8:22-26) -- first partial sight ('I see people, but they look like trees'), "
                        "then full sight. This symbolizes the disciples' partial understanding that is "
                        "about to be both opened and challenged. At Caesarea Philippi, Peter confesses: "
                        "'You are the Christ' (8:29). Jesus commands secrecy (8:30) and immediately "
                        "begins the first passion prediction: 'The Son of Man must (dei) suffer many "
                        "things and be rejected by the elders and the chief priests and the scribes and "
                        "be killed, and after three days rise again' (8:31). Peter rebukes him (8:32). "
                        "Jesus rebukes Peter: 'Get behind me, Satan! For you are not setting your mind "
                        "on the things of God, but on the things of man' (8:33). Then: 'If anyone would "
                        "come after me, let him deny himself and take up his cross and follow me. For "
                        "whoever would save his life will lose it, but whoever loses his life for my "
                        "sake and the gospel's will save it' (8:34-35)."
            },
            {
                "heading": "The Transfiguration and the Way Down (9:2-50)",
                "body": "Six days later, Jesus takes Peter, James, and John up 'a high mountain' (9:2). "
                        "'And he was transfigured (metemorphothe) before them, and his clothes became "
                        "radiant, intensely white, as no one on earth could bleach them' (9:2-3). Elijah "
                        "and Moses appear, talking with Jesus (9:4). Peter, terrified, offers to build "
                        "three tabernacles (9:5). A cloud overshadows them, and the voice speaks: 'This "
                        "is my beloved Son; listen to him (akouete autou)' (9:7). 'And suddenly, looking "
                        "around, they no longer saw anyone with them but Jesus only (Iesoun monon)' (9:8). "
                        "Coming down the mountain, Jesus commands silence 'until the Son of Man had risen "
                        "from the dead' (9:9). The second passion prediction follows (9:31): 'The Son of "
                        "Man is being delivered (paradidotai) into the hands of men, and they will kill "
                        "him. And when he is killed, after three days he will rise.' The disciples argue "
                        "about who is the greatest (9:34). Jesus takes a child: 'Whoever receives one "
                        "such child in my name receives me, and whoever receives me, receives not me "
                        "but him who sent me' (9:37)."
            },
            {
                "heading": "The Journey to Jerusalem: Suffering and Service (10:1-52)",
                "body": "Jesus teaches on divorce (10:2-12), blesses children (10:13-16), and encounters "
                        "the rich man who asks about eternal life (10:17-22). 'How difficult it will be "
                        "for those who have wealth to enter the kingdom of God!' (10:23). The third "
                        "passion prediction is the most detailed: 'The Son of Man will be delivered over "
                        "to the chief priests and the scribes, and they will condemn him to death and "
                        "deliver him over to the Gentiles. And they will mock him and spit on him, and "
                        "flog him and kill him. And after three days he will rise' (10:33-34). James and "
                        "John request the seats at Jesus' right and left (10:35-37). Jesus asks: 'Can "
                        "you drink the cup that I drink?' (10:38). He teaches: 'Whoever would be great "
                        "among you must be your servant (diakonos), and whoever would be first among you "
                        "must be slave (doulos) of all. For even the Son of Man came not to be served "
                        "but to serve, and to give his life as a ransom (lytron) for many (anti pollon)' "
                        "(10:43-45). The section closes with Bartimaeus, the blind beggar who cries out "
                        "'Son of David, have mercy on me!' (10:47), receives his sight, and follows "
                        "Jesus 'on the way' (en te hodo, 10:52) -- the way to the cross."
            }
        ]
    },

    {
        "id": "mark-11-13",
        "ref": "Mark 11-13",
        "chapter_num": 5,
        "title": "Jerusalem Conflicts and the Olivet Discourse",
        "era": "mark_servant",
        "type": "study",

        "synopsis": "Jesus enters Jerusalem riding a colt (11:1-11), cleanses the Temple (11:15-19), "
                    "and engages in a series of confrontations with the religious authorities. The fig "
                    "tree incident (11:12-14, 20-25) -- cursed and withered -- frames the Temple "
                    "cleansing as a prophetic sign of judgment. Controversies follow: the question of "
                    "authority (11:27-33), the parable of the tenants (12:1-12), paying taxes to Caesar "
                    "(12:13-17), the resurrection debate (12:18-27), the greatest commandment (12:28-34), "
                    "and the Psalm 110 question: 'David himself calls him Lord. So how is he his son?' "
                    "(12:35-37). Chapter 13 -- the Olivet Discourse -- reveals the end: the Temple's "
                    "destruction, cosmic upheaval, the shaking of the heavenly powers, and the Son of "
                    "Man coming in clouds 'with great power and glory' to send his angels and gather "
                    "the elect (13:26-27).",

        "key_verse": {
            "ref": "Mark 13:26-27",
            "text": "And then they will see the Son of Man coming in clouds with great power and glory. And then he will send out the angels and gather his elect from the four winds, from the ends of the earth to the ends of heaven.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "hai dynameis en tois ouranois (the powers in the heavens -- the spiritual forces governing the cosmos; their shaking signals the collapse of the old order (13:25))",
            "ho huios tou anthropou (the Son of Man -- from Daniel 7:13; the human-divine figure who comes in the clouds with divine authority)",
            "eklektous (elect / chosen ones -- those chosen by God; gathered by the angels at the Son of Man's coming from the four winds)",
            "kyrios (Lord -- David's 'Lord' in Psalm 110:1; the title that proves the Messiah is more than David's descendant)",
            "Abba (Father -- Jesus' intimate address for God in Gethsemane (14:36); Aramaic term of familial intimacy used in prayer)"
        ],

        "ane_backdrop": "The parable of the tenants (12:1-12) draws on Isaiah 5's vineyard song -- a "
                        "well-known judgment oracle in which Israel is YHWH's vineyard that produces "
                        "wild grapes. Mark's version adds the dimension of the owner sending servants "
                        "(the prophets) and finally his beloved son (12:6). The tenants kill the son, "
                        "hoping to seize the inheritance. The Olivet Discourse's cosmic sign language -- "
                        "darkened sun, falling stars, shaking heavens -- draws on the prophetic tradition "
                        "of theophanic judgment (Isa 13:10; Joel 2:31; Amos 8:9). The 'stars falling "
                        "from heaven' (13:25) in the ANE framework refers to the displacement of "
                        "spiritual powers: celestial bodies were associated with divine beings (Deut "
                        "4:19; Dan 8:10; Judg 5:20), and their 'falling' represents the collapse of "
                        "the spiritual order that governs the nations.",

        "second_temple": [
            {
                "source": "1 Enoch 62-63 (Parables of Enoch)",
                "summary": "The Son of Man sits on his throne of glory, and the kings and mighty ones "
                           "of the earth are judged before him. They beg for mercy but are handed over "
                           "to the angels of punishment.",
                "relevance": "The closest non-canonical parallel to Mark 13:26-27 -- the Son of Man "
                             "coming in glory with angelic attendants to judge and gather."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 110:1", "note": "'The LORD said to my Lord: Sit at my right hand' -- quoted by Jesus (12:36) to demonstrate the Messiah's divine identity", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "'One like a son of man, coming with the clouds of heaven' -- the foundational text for the Son of Man's coming (13:26)", "type": "ot"},
            {"ref": "Isaiah 5:1-7", "note": "The vineyard song -- the background to the parable of the tenants (12:1-12)", "type": "ot"},
            {"ref": "Isaiah 13:10; 34:4", "note": "Cosmic judgment language: darkened sun, falling stars -- used in the Olivet Discourse (13:24-25)", "type": "ot"},
            {"ref": "Deuteronomy 6:4-5", "note": "The Shema: 'Hear, O Israel: The LORD our God, the LORD is one. You shall love the LORD your God with all your heart' -- quoted as the greatest commandment (12:29-30)", "type": "ot"},
            {"ref": "Matthew 24-25", "note": "Matthew's expanded Olivet Discourse -- adds the sheep/goats judgment (25:31-46) and several parables of readiness", "type": "nt"}
        ],

        "divine_council_note": "Mark 13 is the most explicitly divine council eschatological text in "
                               "this Gospel. The 'powers in the heavens' (hai dynameis hai en tois "
                               "ouranois, 13:25) that are 'shaken' are the spiritual forces governing the "
                               "cosmos -- the same powers Paul identifies as 'rulers and authorities in the "
                               "heavenly places' (Eph 3:10; 6:12). Their shaking signals the collapse of "
                               "the Deuteronomy 32 order: the nations governed by the rebellious elohim "
                               "are being reclaimed. The Son of Man 'coming in clouds with great power and "
                               "glory' (13:26) is the Daniel 7:13-14 scene: the human-divine figure "
                               "approaches the Ancient of Days and receives universal dominion. He 'sends "
                               "out the angels (tous angelous)' (13:27) -- divine council members executing "
                               "his commands -- to 'gather his elect from the four winds.' The Psalm 110 "
                               "question (12:35-37) is equally important: how can David's descendant be "
                               "David's Lord? The answer requires the divine council framework: the Messiah "
                               "is both human (David's seed) and divine (seated at YHWH's right hand in the "
                               "heavenly council). Mark's audience knows the answer that the scribes cannot "
                               "give: Jesus is the one who sits at God's right hand, above all the elohim.",

        "sections": [
            {
                "heading": "The Entry, the Temple, and the Controversies (11:1 - 12:44)",
                "body": "Jesus enters Jerusalem on a colt (11:1-11), fulfilling Zechariah 9:9. He "
                        "curses a fig tree with no fruit (11:12-14) -- a prophetic sign. He cleanses "
                        "the Temple: 'Is it not written, \"My house shall be called a house of prayer "
                        "for all the nations (pasin tois ethnesin)\"? But you have made it a den of "
                        "robbers' (11:17, combining Isa 56:7 and Jer 7:11). The inclusion of 'all the "
                        "nations' is significant: the Temple was supposed to be a place where the "
                        "nations could encounter YHWH -- the reversal of Babel -- but the merchants "
                        "have prevented it. The fig tree is found withered (11:20-21). The controversies "
                        "escalate: the parable of the tenants (12:1-12) ends with 'The stone that the "
                        "builders rejected has become the cornerstone' (12:10, Ps 118:22). 'Render to "
                        "Caesar the things that are Caesar's, and to God the things that are God's' "
                        "(12:17). The greatest commandments: love God and love neighbor (12:29-31). Then "
                        "the Psalm 110 question: 'David himself calls him Lord. So how is he his son?' "
                        "(12:37). The widow's two coins close the chapter (12:41-44) -- true giving "
                        "contrasted with the hollow religion of the scribes."
            },
            {
                "heading": "The Olivet Discourse: Cosmic Signs and the Son of Man (13:1-37)",
                "body": "Leaving the Temple, Jesus predicts its destruction: 'There will not be left "
                        "here one stone upon another' (13:2). On the Mount of Olives, Peter, James, "
                        "John, and Andrew ask privately: 'When will these things be?' (13:4). Jesus "
                        "warns of false messiahs, wars, earthquakes, and famines -- 'the beginning of "
                        "the birth pains' (13:8). They will be delivered to councils and beaten in "
                        "synagogues (13:9). 'The gospel must first be proclaimed to all nations (panta "
                        "ta ethne)' (13:10) -- the mission to the nations is eschatologically necessary. "
                        "The 'abomination of desolation' will stand where it ought not (13:14, from "
                        "Daniel 9:27). Then cosmic upheaval: 'the sun will be darkened, and the moon "
                        "will not give its light, and the stars will be falling from heaven, and the "
                        "powers in the heavens will be shaken' (13:24-25). 'And then they will see the "
                        "Son of Man coming in clouds with great power and glory. And then he will send "
                        "out the angels and gather his elect from the four winds, from the ends of the "
                        "earth to the ends of heaven' (13:26-27). 'But concerning that day or that hour, "
                        "no one knows, not even the angels in heaven, nor the Son, but only the Father' "
                        "(13:32). The discourse ends: 'What I say to you I say to all: Stay awake' "
                        "(13:37)."
            }
        ]
    },

    {
        "id": "mark-14-16",
        "ref": "Mark 14-16",
        "chapter_num": 6,
        "title": "The Passion and the Empty Tomb",
        "era": "mark_servant",
        "type": "study",

        "synopsis": "Mark's passion narrative is the most raw and unflinching of the four Gospels. "
                    "Jesus is anointed at Bethany (14:3-9), celebrates the Last Supper and institutes "
                    "the covenant meal (14:22-25), prays in Gethsemane with anguished honesty ('Abba, "
                    "Father, all things are possible for you. Remove this cup from me. Yet not what I "
                    "will, but what you will,' 14:36), is betrayed by Judas, abandoned by all the "
                    "disciples, denied three times by Peter, tried before the Sanhedrin (where he makes "
                    "the definitive 'I AM' declaration, 14:62), delivered to Pilate, mocked, scourged, "
                    "and crucified. From the cross he cries the desolate words of Psalm 22:1: 'Eloi, "
                    "Eloi, lema sabachthani?' (15:34). At his death, the Temple veil is torn in two "
                    "(15:38) -- the same verb (schizo) used for the heavens 'torn open' at the baptism "
                    "(1:10), forming a literary inclusio: what was opened at the beginning is torn at "
                    "the end. The centurion -- a Gentile -- confesses: 'Truly this man was the Son of "
                    "God!' (15:39). The women discover the empty tomb and the angel's message: 'He has "
                    "risen; he is not here' (16:6). Mark's original ending: 'they said nothing to "
                    "anyone, for they were afraid (ephobounto gar)' (16:8).",

        "key_verse": {
            "ref": "Mark 15:38-39",
            "text": "And the curtain of the temple was torn in two, from top to bottom. And when the centurion, who stood facing him, saw that in this way he breathed his last, he said, 'Truly this man was the Son of God!'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ego eimi (I AM -- Jesus' answer at the trial: 'Are you the Christ?' 'I am' (14:62); potentially the divine self-identification of Exodus 3:14)",
            "Abba (Father -- Aramaic intimate address; Jesus' prayer in Gethsemane (14:36); the familial relationship with God that grounds his obedience)",
            "diatheke (covenant -- 'This is my blood of the covenant, which is poured out for many' (14:24); the new covenant ratified by the Messiah's death)",
            "schizo (tear -- the veil is 'torn' (eschisthe, 15:38) at the cross, matching the heavens 'torn open' (schizomenous, 1:10) at the baptism; an inclusio of revelation)",
            "Eloi, Eloi, lema sabachthani (My God, my God, why have you forsaken me -- Psalm 22:1 in Aramaic; the cry of dereliction that is also a cry of faith)"
        ],

        "ane_backdrop": "The passion narrative resonates with the ANE motif of the righteous sufferer "
                        "who is vindicated by the deity. The individual lament psalms (esp. Psalm 22, "
                        "69, 88) provide the literary and theological framework. The tearing of the "
                        "Temple veil connects to ANE temple theology: the veil separated the sacred "
                        "space (the Holy of Holies, the earthly counterpart of the divine council "
                        "chamber) from the profane world. Its tearing at Jesus' death signals that "
                        "the barrier between God and humanity has been permanently removed. The cosmic "
                        "darkness during the crucifixion (15:33) echoes the plague of darkness in "
                        "Egypt (Exod 10:21-23) and the prophetic judgment tradition (Amos 8:9). The "
                        "centurion's confession -- a Roman soldier acknowledging the crucified man as "
                        "'Son of God' -- is the ultimate irony: the title claimed by Caesar belongs "
                        "to the one Caesar's empire has just executed.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 2:12-20; 5:1-7",
                "summary": "The wicked test the righteous man who claims to be God's son (2:13, 16, 18). "
                           "After his death, they are shocked to find him among the sons of God (5:5): "
                           "'We fools counted his life madness and his end to be without honor. Behold, "
                           "how he is counted among the sons of God!'",
                "relevance": "A striking parallel to Mark's passion: the righteous Son of God is "
                             "tested by suffering and mockery, then vindicated -- and the Gentile "
                             "centurion recognizes what the mockers could not."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 22", "note": "The passion psalm: 'My God, my God, why have you forsaken me?' (v.1, quoted at 15:34); mockery (v.7-8), piercing (v.16), lots for garments (v.18)", "type": "ot"},
            {"ref": "Isaiah 53:7, 12", "note": "'Like a lamb led to the slaughter, he opened not his mouth... he bore the sin of many' -- the Suffering Servant fulfilled in the passion", "type": "ot"},
            {"ref": "Daniel 7:13", "note": "'Coming with the clouds of heaven' -- quoted at the trial (14:62); the Son of Man's divine identity confessed before the Sanhedrin", "type": "ot"},
            {"ref": "Psalm 110:1", "note": "'Seated at the right hand of Power' -- quoted at the trial (14:62); the divine council enthronement claimed at the moment of greatest humiliation", "type": "ot"},
            {"ref": "Zechariah 13:7", "note": "'Strike the shepherd, and the sheep will be scattered' -- quoted by Jesus about the disciples' abandonment (14:27)", "type": "ot"},
            {"ref": "Exodus 24:8", "note": "'The blood of the covenant' -- echoed in the Last Supper: 'This is my blood of the covenant' (14:24)", "type": "ot"},
            {"ref": "Matthew 26-28", "note": "Matthew's parallel: adds Judas' death, Pilate's wife's dream, the guard at the tomb, and the Great Commission", "type": "nt"},
            {"ref": "Luke 22-24", "note": "Luke's parallel: adds the Emmaus road narrative, Jesus' appearance to the disciples, and the promise of the Spirit", "type": "nt"}
        ],

        "divine_council_note": "The passion narrative is the climax of Mark's divine council theology. "
                               "At the trial, the high priest asks: 'Are you the Christ, the Son of the "
                               "Blessed?' (14:61). Jesus answers: 'I am (ego eimi), and you will see the "
                               "Son of Man seated at the right hand of Power (ek dexion tes dynameos) and "
                               "coming with the clouds of heaven (meta ton nephelon tou ouranou)' (14:62). "
                               "This is the most explicit divine council claim in the Gospel: ego eimi "
                               "(the possible divine self-identification), Psalm 110:1 (seated at YHWH's "
                               "right hand in the heavenly council), and Daniel 7:13 (the Son of Man "
                               "coming on clouds -- a divine prerogative). The high priest tears his "
                               "garments and declares blasphemy (14:63-64) -- he understands exactly what "
                               "Jesus is claiming. The tearing of the Temple veil (15:38) is the second "
                               "use of the verb schizo in Mark (the first: the heavens 'torn open' at "
                               "baptism, 1:10). This forms an inclusio: at the baptism, heaven is torn "
                               "open to reveal the Son; at the death, the Temple veil is torn to open "
                               "access to God. The barrier between the divine council chamber (the Holy "
                               "of Holies, YHWH's earthly throne room) and humanity has been permanently "
                               "breached by the death of the Son. The centurion's confession -- 'Truly "
                               "this man was the Son of God (huios theou)' (15:39) -- is the theological "
                               "climax of the Gospel. The title declared at the baptism (1:11), "
                               "acknowledged by demons (3:11; 5:7), revealed at the Transfiguration (9:7), "
                               "and claimed at the trial (14:62) is finally spoken by a human being -- and "
                               "that human is a Gentile, standing at the cross. The messianic secret is "
                               "fully revealed: the Son of God is recognized not in a display of power "
                               "but at the moment of death. The empty tomb (16:1-8) vindicates the claim: "
                               "death cannot hold the Son of God. 'He has risen; he is not here' (16:6).",

        "sections": [
            {
                "heading": "The Last Supper, Gethsemane, and Arrest (14:1-52)",
                "body": "The chief priests plot to kill Jesus 'by stealth' (14:1). At Bethany, a woman "
                        "anoints him with pure nard (14:3-9): 'She has done a beautiful thing to me... "
                        "she has anointed my body beforehand for burial' (14:6, 8). Judas agrees to "
                        "betray him (14:10-11). At the Passover meal, Jesus institutes the Lord's "
                        "Supper: 'Take; this is my body' (14:22). 'This is my blood of the covenant "
                        "(to haima mou tes diathekes), which is poured out for many' (14:24). 'Truly, "
                        "I say to you, I will not drink again of the fruit of the vine until that day "
                        "when I drink it new in the kingdom of God' (14:25) -- the messianic banquet "
                        "awaits. In Gethsemane, Jesus prays with devastating honesty: 'Abba, Father, "
                        "all things are possible for you. Remove this cup from me. Yet not what I will, "
                        "but what you will' (14:36). The disciples sleep. Judas arrives. A young man "
                        "flees naked (14:51-52, unique to Mark -- possibly the author himself?). 'And "
                        "they all left him and fled' (14:50)."
            },
            {
                "heading": "Trial, Crucifixion, Death, and the Empty Tomb (14:53 - 16:8)",
                "body": "Before the Sanhedrin, false witnesses fail to agree (14:56-59). The high "
                        "priest asks: 'Are you the Christ, the Son of the Blessed?' Jesus answers: "
                        "'I am (ego eimi). And you will see the Son of Man seated at the right hand "
                        "of Power and coming with the clouds of heaven' (14:62). The charge: blasphemy "
                        "(14:64). Peter denies Jesus three times and weeps (14:66-72). Pilate asks: "
                        "'Are you the King of the Jews?' Jesus: 'You have said so' (15:2). The crowd "
                        "chooses Barabbas (15:6-15). Soldiers mock Jesus with a purple robe and crown "
                        "of thorns: 'Hail, King of the Jews!' (15:18). He is crucified at the third "
                        "hour (9 AM, 15:25). The inscription: 'The King of the Jews' (15:26). At the "
                        "sixth hour, darkness covers the land (15:33). At the ninth hour: 'Eloi, Eloi, "
                        "lema sabachthani?' (15:34). Jesus cries out and breathes his last (15:37). "
                        "The Temple veil is torn from top to bottom (15:38). The centurion confesses: "
                        "'Truly this man was the Son of God!' (15:39). Joseph of Arimathea buries "
                        "Jesus (15:42-47). On the first day of the week, the women find the stone "
                        "rolled away and a young man in a white robe: 'Do not be alarmed. You seek "
                        "Jesus of Nazareth, who was crucified. He has risen; he is not here' (16:6). "
                        "'Go, tell his disciples and Peter that he is going before you to Galilee' "
                        "(16:7). 'And they went out and fled from the tomb, for trembling and "
                        "astonishment had seized them, and they said nothing to anyone, for they "
                        "were afraid' (16:8). Mark's Gospel ends in fear and silence -- and the reader "
                        "must decide: will you go to Galilee and find the risen Lord?"
            }
        ]
    }
]
