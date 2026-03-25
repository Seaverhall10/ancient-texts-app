"""
era_luke_journey.py -- Luke 9:51-19:27: The Travel Narrative (Journey to Jerusalem)

Luke's Travel Narrative is the longest unique section in his Gospel, spanning
nearly ten chapters of material found almost entirely in Luke alone. The
narrative begins with the ominous statement that Jesus "set his face to go
to Jerusalem" (9:51) -- the Greek analempsis (taking up) signals his coming
death and ascension. The journey structure is literary rather than strictly
geographical: Jesus moves steadily toward Jerusalem, the city that "kills
the prophets" (13:34), while teaching, healing, and telling the parables
that have become Christianity's most beloved stories. The Good Samaritan,
the Prodigal Son, the Rich Man and Lazarus, the Pharisee and the Tax
Collector -- all appear only in Luke, all within this travel section. The
theological center is Luke 15: three parables of the lost (sheep, coin,
son) that reveal the heart of God as a seeking, rejoicing Father who
recovers what was lost. The journey ends as Jesus enters Jericho, finds
Zacchaeus, and declares: "The Son of Man came to seek and to save the lost"
(19:10) -- the thesis statement of the entire Travel Narrative.
"""

CHAPTERS = [
    {
        "id": "luke-journey-01",
        "ref": "Luke 9:51-10:42",
        "chapter_num": 1,
        "title": "The Road to Jerusalem Begins -- Rejection, Mission, and Mercy",
        "era": "luke_journey",
        "type": "study",
        "themes": ["NATIONS", "DC", "LOVE", "KING", "COV"],

        "synopsis": "The Travel Narrative opens with one of the most dramatic statements in the "
                    "Gospels: 'When the days drew near for him to be taken up (analempsis), he set "
                    "his face (to prosopon esterisen) to go to Jerusalem' (9:51). The language is "
                    "Isaianic -- 'I have set my face like a flint' (Isa 50:7) -- identifying Jesus "
                    "with the Suffering Servant who advances toward suffering without flinching. [A] "
                    "Samaritans reject him because 'his face was set toward Jerusalem' (9:53) -- the "
                    "ancient Samaritan-Jewish rift over the proper worship site (Gerizim vs. Zion). "
                    "James and John want to call fire from heaven (9:54), echoing Elijah (2 Kings "
                    "1:10-12), but Jesus rebukes them -- the kingdom advances by mercy, not "
                    "destruction. [B] The cost of discipleship is laid bare: 'Foxes have holes, and "
                    "birds of the air have nests, but the Son of Man has nowhere to lay his head' "
                    "(9:58). Jesus then sends out seventy-two (10:1-20), a number echoing the "
                    "seventy nations of Genesis 10 and the seventy elders of Exodus 24:1. [B] Their "
                    "return triggers Jesus' exultant cry: 'I saw Satan fall like lightning from heaven' "
                    "(10:18) -- the kingdom mission is dismantling the adversary's authority. The "
                    "Good Samaritan (10:25-37) shatters ethnic and religious boundaries: the hero is "
                    "the despised outsider, and the command is 'Go, and do likewise' (10:37). [A] "
                    "Mary and Martha (10:38-42) close the unit: 'Mary has chosen the good portion "
                    "(agathen merida), which will not be taken away from her' (10:42).",

        "key_verse": {
            "ref": "Luke 10:18",
            "text": "And he said to them, 'I saw Satan fall like lightning from heaven.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "analempsis (taking up -- used only here in the NT (9:51); refers to Jesus' entire departure: death, resurrection, and ascension as a single divine event)",
            "to prosopon esterisen (he set his face -- a Semitism from Isa 50:7; resolute determination toward the cross; the Servant's unflinching advance)",
            "ergatas (workers / laborers -- 'The harvest is plentiful, but the laborers (ergatai) are few' (10:2); kingdom mission language for those sent into hostile territory)",
            "exousia (authority -- 'I have given you authority (exousian) to tread on serpents and scorpions' (10:19); delegated divine power over hostile spiritual forces)",
            "plesion (neighbor -- the lawyer's question 'Who is my neighbor (plesion)?' (10:29); Jesus redefines it from ethnic category to ethical action)",
            "splanchnistheis (moved with compassion -- the Samaritan was 'moved with compassion' (10:33); visceral, gut-level mercy; the same verb used for Jesus' own compassion)",
            "agathen merida (the good portion -- Mary's choice to sit at Jesus' feet (10:42); the language of inheritance and covenant blessing)"
        ],

        "ane_backdrop": "The Samaritan rejection (9:52-53) reflects centuries of hostility between "
                        "Jews and Samaritans rooted in the Assyrian resettlement of 722 BC (2 Kings "
                        "17:24-41) and the rival temple on Mount Gerizim. In the ANE, sacred geography "
                        "determined loyalty: your god's mountain was your identity. The Samaritans "
                        "worshiped at Gerizim; the Jews at Zion. Jesus' face 'set toward Jerusalem' "
                        "was a theological provocation. The sending of the seventy-two echoes the ANE "
                        "practice of royal envoys sent ahead of a king's arrival to prepare cities for "
                        "his coming. The number seventy (or seventy-two) corresponds to the Table of "
                        "Nations (Gen 10), which in Second Temple tradition represented the total number "
                        "of the world's peoples allotted to the bene elohim at Babel (Deut 32:8). The "
                        "Good Samaritan parable subverts the purity system: the priest and Levite avoid "
                        "the wounded man likely to avoid corpse contamination (Num 19:11-13), while the "
                        "Samaritan -- himself ritually 'unclean' to a Jewish audience -- acts with the "
                        "compassion that the Torah demands (Lev 19:18).",

        "second_temple": [
            {
                "source": "Targum Pseudo-Jonathan on Genesis 10",
                "summary": "The Targum expands the Table of Nations to enumerate seventy peoples "
                           "descended from Noah's sons, each allotted a language and territory at "
                           "Babel -- a tradition reflected in the LXX of Deut 32:8.",
                "relevance": "The seventy-two sent by Jesus (10:1) mirror the seventy nations: the "
                             "mission to 'every town and place where he himself was about to go' (10:1) "
                             "foreshadows the gospel's expansion to all peoples, reversing the Babel "
                             "judgment."
            },
            {
                "source": "Testament of Levi 18:12",
                "summary": "'And Beliar shall be bound by him, and he shall give power to his "
                           "children to tread upon the evil spirits.' A messianic prophecy of "
                           "authority over demonic forces.",
                "relevance": "Jesus' declaration that he gives his disciples 'authority to tread on "
                             "serpents and scorpions, and over all the power of the enemy' (10:19) "
                             "echoes this Second Temple expectation of the Messiah's defeat of Beliar "
                             "and delegation of spiritual authority."
            },
            {
                "source": "4Q372 (4QNarrative and Poetic Composition)",
                "summary": "A Qumran text lamenting the Samaritan schism and praying for God to "
                           "restore the northern tribes, acknowledging the long history of enmity "
                           "between Judah and the Samaritans.",
                "relevance": "Provides the sectarian backdrop for Jesus' radical inclusion of "
                             "Samaritans: while Qumran lamented the division, Jesus makes a Samaritan "
                             "the hero of his most famous parable."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 50:7", "note": "'I have set my face like a flint, and I know that I shall not be put to shame' -- the Suffering Servant text behind Jesus' resolve toward Jerusalem (9:51)", "type": "ot"},
            {"ref": "Genesis 10:1-32", "note": "The Table of Nations: seventy peoples from Noah's sons -- the theological background for the seventy-two sent out (10:1)", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God at Babel -- the seventy-two disciples reclaim territory from the hostile elohim assigned to the nations", "type": "ot"},
            {"ref": "2 Kings 1:10-12", "note": "Elijah calls fire from heaven on the king's soldiers -- James and John want the same, but Jesus rebukes the impulse (9:54-55)", "type": "ot"},
            {"ref": "Leviticus 19:18", "note": "'You shall love your neighbor as yourself' -- the commandment the lawyer quotes (10:27) that the Good Samaritan fulfills", "type": "ot"},
            {"ref": "Revelation 12:7-9", "note": "Satan cast from heaven -- connects to Jesus' vision: 'I saw Satan fall like lightning from heaven' (10:18); the kingdom mission inaugurates the cosmic defeat", "type": "nt"}
        ],

        "divine_council_note": "This section is saturated with divine council conflict. Jesus' exultant cry -- "
                               "'I saw Satan fall like lightning from heaven' (10:18) -- is a throne-room "
                               "vision: the chief adversary's authority is being dismantled as the seventy-two "
                               "preach and cast out demons. The number seventy-two itself is a divine council "
                               "number -- it corresponds to the nations allotted to the bene elohim at Babel "
                               "(Deut 32:8, LXX/DSS). Jesus is sending his agents to reclaim the very "
                               "territories that were placed under rebellious spiritual rulers. The authority "
                               "(exousia) Jesus delegates -- 'to tread on serpents and scorpions, and over all "
                               "the power of the enemy' (10:19) -- is authority over the hostile spiritual "
                               "hierarchy. 'Serpents and scorpions' are not merely physical dangers but echo "
                               "the nachash of Eden and the demonic forces associated with the wilderness "
                               "(cf. Deut 8:15; Isa 14:29). The seventy-two report that 'even the demons are "
                               "subject to us in your name' (10:17) -- the territorial spirits assigned to "
                               "the nations are losing ground as Jesus' emissaries advance. Yet Jesus redirects "
                               "their joy: 'Do not rejoice in this, that the spirits are subject to you, but "
                               "rejoice that your names are written in heaven' (10:20) -- their ultimate "
                               "identity is their citizenship in the heavenly assembly, not their combat "
                               "victories.",

        "sections": [
            {
                "heading": "Setting His Face: Rejection and the Cost of Discipleship (9:51-62)",
                "body": "The Travel Narrative opens with theological gravity: 'When the days drew near "
                        "for him to be taken up (analempsis), he set his face to go to Jerusalem' (9:51). "
                        "The word analempsis appears only here in the entire New Testament -- it encompasses "
                        "Jesus' death, resurrection, and ascension as a single divine event. 'Set his face' "
                        "(to prosopon esterisen) is a Semitism drawn from Isaiah 50:7, where the Suffering "
                        "Servant declares, 'I have set my face like a flint.' Jesus is not merely traveling; "
                        "he is advancing into the jaws of death with prophetic resolve. The Samaritans "
                        "reject him because 'his face was set toward Jerusalem' (9:53) -- the rival temple "
                        "at Gerizim makes Zion a point of offense. James and John react with Elijah-like "
                        "fury: 'Lord, do you want us to tell fire to come down from heaven and consume them?' "
                        "(9:54). But Jesus rebukes them -- the kingdom of God does not advance by destroying "
                        "enemies but by loving them. Three would-be followers approach, and each receives a "
                        "searing response: the Son of Man has no home (9:58), the dead must bury the dead "
                        "(9:60), no one who looks back is fit for the kingdom (9:62). The cost of following "
                        "Jesus on this road is everything."
            },
            {
                "heading": "The Seventy-Two: Mission to the Nations and Satan's Fall (10:1-24)",
                "body": "Jesus appoints seventy-two and sends them ahead 'into every town and place where "
                        "he himself was about to go' (10:1). The number is theologically loaded: Genesis 10 "
                        "lists seventy (LXX: seventy-two) nations descended from Noah. In the Deuteronomy 32 "
                        "worldview, these nations were assigned to the bene elohim at Babel. Jesus is now "
                        "sending his agents to reclaim those very territories. He warns them: 'I am sending "
                        "you out as lambs in the midst of wolves' (10:3) -- the mission is into hostile "
                        "spiritual territory. The instructions are urgent: no purse, no bag, no sandals, no "
                        "greetings on the road (10:4). When they return rejoicing that 'even the demons are "
                        "subject to us in your name' (10:17), Jesus responds with a cosmic revelation: 'I "
                        "saw Satan fall like lightning from heaven' (10:18). This is not a reference to a "
                        "past event but a prophetic vision of what the mission accomplishes -- the adversary's "
                        "authority structure is collapsing. Jesus grants them authority 'over all the power "
                        "of the enemy' (10:19) and then pivots: 'Do not rejoice in this, that the spirits "
                        "are subject to you, but rejoice that your names are written in heaven' (10:20). "
                        "Identity precedes assignment. Jesus then erupts in prayer: 'I thank you, Father, "
                        "Lord of heaven and earth, that you have hidden these things from the wise and "
                        "understanding and revealed them to little children' (10:21)."
            },
            {
                "heading": "The Good Samaritan: Redefining the Neighbor (10:25-37)",
                "body": "A lawyer stands up to test Jesus: 'Teacher, what shall I do to inherit eternal "
                        "life?' (10:25). Jesus turns the question back: 'What is written in the Law? How "
                        "do you read it?' (10:26). The lawyer answers correctly -- love God with all your "
                        "heart, and love your neighbor as yourself (10:27, quoting Deut 6:5 and Lev 19:18). "
                        "But then he tries to limit the command: 'And who is my neighbor (plesion)?' (10:29). "
                        "Jesus responds with a parable that demolishes every ethnic and religious boundary. "
                        "A man lies beaten on the Jericho road. A priest passes by on the other side -- "
                        "likely avoiding corpse contamination under Numbers 19. A Levite does the same. "
                        "Then 'a Samaritan, as he journeyed, came to where he was, and when he saw him, "
                        "he had compassion (splanchnistheis)' (10:33). The verb splanchnistheis is visceral "
                        "-- gut-level mercy, the same word used for Jesus' own compassion (Luke 7:13). The "
                        "Samaritan binds wounds, pours oil and wine, carries the man to an inn, pays for "
                        "his care, and promises to return. Jesus reverses the question: 'Which of these "
                        "three, do you think, proved to be a neighbor?' (10:36). The answer is inescapable: "
                        "'The one who showed him mercy' (10:37). 'Go, and do likewise.' The neighbor is not "
                        "defined by ethnicity but by action."
            },
            {
                "heading": "Mary and Martha: The Good Portion (10:38-42)",
                "body": "The Travel Narrative's opening unit closes with a domestic scene that carries "
                        "profound theological weight. Jesus enters a village, and 'a woman named Martha "
                        "welcomed him into her house' (10:38). Martha is 'distracted with much serving "
                        "(diakonian)' (10:40), while Mary 'sat at the Lord's feet and listened to his "
                        "teaching (logon)' (10:39). 'Sitting at the feet' of a teacher is the posture of "
                        "a disciple -- a role typically reserved for men in first-century Judaism. [B] By "
                        "presenting Mary in this posture without correction, Luke affirms women as full "
                        "participants in discipleship and Torah learning. Martha's complaint -- 'Lord, do "
                        "you not care that my sister has left me to serve alone?' (10:40) -- is not about "
                        "laziness but about priority. Jesus' response is gentle but firm: 'Martha, Martha, "
                        "you are anxious (merimnao) and troubled about many things, but one thing is "
                        "necessary. Mary has chosen the good portion (agathen merida), which will not be "
                        "taken away from her' (10:41-42). The word merida (portion) carries covenantal "
                        "overtones -- it is the language of inheritance, the share of the land or blessing "
                        "that God assigns. [B] The 'good portion' is the word of the Lord himself. In a "
                        "section about mission, cost, and compassion, Luke ends with the reminder that "
                        "all action flows from attentive presence at the feet of Jesus."
            }
        ]
    },

    {
        "id": "luke-journey-02",
        "ref": "Luke 11:1-13:21",
        "chapter_num": 2,
        "title": "Prayer and the Kingdom -- The Lord's Prayer, Warnings, and True Treasure",
        "era": "luke_journey",
        "type": "study",
        "themes": ["KING", "DC", "HOLY", "REBEL", "COV"],

        "synopsis": "This section opens with the disciples asking Jesus to teach them to pray (11:1) -- "
                    "a request unique to Luke. Jesus gives the Lord's Prayer in its shorter Lukan form: "
                    "'Father (Pater), hallowed be your name. Your kingdom come' (11:2). The prayer is "
                    "followed by parables of persistence: the friend at midnight (11:5-8) and the "
                    "assurance that the Father gives the Holy Spirit to those who ask (11:13). [A] "
                    "When Jesus casts out a demon, opponents accuse him of working 'by Beelzebul, the "
                    "prince of demons' (11:15). Jesus' response is devastating: 'If I cast out demons "
                    "by the finger of God (daktylō tou theou), then the kingdom of God has come upon "
                    "you' (11:20) -- 'finger of God' echoes Exodus 8:19, linking exorcism to the "
                    "Exodus liberation. [A] He pronounces woes on the Pharisees and lawyers (11:37-52): "
                    "they tithe mint and rue but neglect justice and the love of God. [B] The teaching "
                    "turns to fearless confession: 'Do not fear those who kill the body... Fear him "
                    "who, after he has killed, has authority to cast into Gehenna' (12:4-5). The Rich "
                    "Fool parable (12:13-21) exposes the idolatry of accumulation: 'Fool! This night "
                    "your soul (psyche) is required of you' (12:20). The section closes with mustard "
                    "seed and leaven (13:18-21) -- the kingdom starts invisible but transforms everything.",

        "key_verse": {
            "ref": "Luke 11:20",
            "text": "But if it is by the finger of God that I cast out demons, then the kingdom of God has come upon you.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Pater (Father -- Luke's version of the Lord's Prayer opens with the bare vocative 'Father' (11:2), more intimate than Matthew's 'Our Father in heaven'; the Aramaic Abba behind it)",
            "daktylō tou theou (finger of God -- 'by the finger of God I cast out demons' (11:20); echoes Exod 8:19 where Pharaoh's magicians recognize God's power; Jesus is the new Moses)",
            "Beelzeboul (Beelzebul / lord of the flies -- a derisive name for Satan as 'prince of demons' (11:15); from Ba'al Zebub of 2 Kings 1:2, the Philistine deity of Ekron)",
            "aphron (fool -- 'Fool! This night your soul is required of you' (12:20); not intellectual stupidity but moral blindness; the opposite of the wise person who stores treasure with God)",
            "pleonexia (covetousness / greed -- 'Be on your guard against all covetousness (pleonexia)' (12:15); the root desire behind the Rich Fool's accumulation)",
            "Gehenna (Valley of Hinnom -- the place of final judgment (12:5); originally the valley south of Jerusalem where child sacrifice occurred (2 Kings 23:10; Jer 7:31))",
            "zyme (leaven -- 'like leaven that a woman hid in three measures of flour' (13:21); the kingdom's hidden, pervasive, transformative power)"
        ],

        "ane_backdrop": "The Beelzebul controversy draws on the ANE understanding of hierarchical "
                        "demonic kingdoms. In Mesopotamian and Canaanite thought, evil spirits operated "
                        "under a chief -- the 'prince of demons' charge assumes a structured spiritual "
                        "hierarchy. Jesus' response engages this framework directly: 'If Satan also is "
                        "divided against himself, how will his kingdom stand?' (11:18). The 'finger of "
                        "God' (daktylō tou theou, 11:20) is a direct Exodus allusion -- the Egyptian "
                        "magicians used this phrase when they could no longer replicate Moses' signs "
                        "(Exod 8:19). Jesus' exorcisms are new-Exodus events: the liberation of Israel "
                        "from Pharaoh now replayed as the liberation of individuals from demonic "
                        "bondage. The Rich Fool parable resonates with ANE wisdom traditions: Egyptian "
                        "Instruction of Amenemope warns against storing grain while neglecting the gods; "
                        "Qoheleth similarly declares accumulation without God is hebel (vanity). The "
                        "mustard seed and leaven parables draw on common agrarian imagery but subvert "
                        "expectations -- the kingdom does not arrive with military fanfare but with the "
                        "quiet, unstoppable power of growth.",

        "second_temple": [
            {
                "source": "Testament of Solomon 3:1-6",
                "summary": "Solomon interrogates demons and learns their hierarchical structure -- "
                           "each demon reports to a prince and has a specific domain of affliction. "
                           "Solomon binds them by divine authority.",
                "relevance": "Provides the Second Temple context for the Beelzebul accusation: "
                             "demons were understood to operate in hierarchies under ruling princes. "
                             "Jesus' authority over this hierarchy is what provokes the charge."
            },
            {
                "source": "1 Enoch 15:8-10",
                "summary": "'The spirits of the giants afflict, oppress, destroy, attack, do battle, "
                           "and work destruction on the earth... evil spirits shall they be called.' "
                           "The giants' disembodied spirits become the demons that plague humanity.",
                "relevance": "The 1 Enoch framework identifies demons as disembodied Nephilim spirits -- "
                             "the strong man's house (11:21-22) that Jesus plunders is this demonic "
                             "occupation of human lives, rooted in the Watcher rebellion."
            },
            {
                "source": "Sirach 11:18-19",
                "summary": "'One becomes rich through diligence and self-denial, and the reward "
                           "allotted to him is this: when he says \"I have found rest, now I shall "
                           "feast on my goods!\" he does not know how long it will be until he "
                           "leaves them to others and dies.'",
                "relevance": "A near-exact parallel to the Rich Fool parable (12:16-21), showing "
                             "that Jesus draws on established Jewish wisdom tradition while giving "
                             "it eschatological urgency."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 8:19", "note": "'The magicians said to Pharaoh, \"This is the finger of God\"' -- Jesus applies the Exodus phrase to his exorcisms, identifying them as the same divine power that defeated Egypt", "type": "ot"},
            {"ref": "Isaiah 49:24-25", "note": "'Can the prey be taken from the mighty, or the captives of a tyrant be rescued?' -- the strong man metaphor (11:21-22); Jesus is the one who binds the tyrant and rescues the captives", "type": "ot"},
            {"ref": "2 Kings 1:2-3", "note": "Ahaziah sends to inquire of Baal-zebub, god of Ekron -- the origin of the Beelzebul name used by Jesus' opponents", "type": "ot"},
            {"ref": "Matthew 6:9-13", "note": "Matthew's Lord's Prayer -- longer form with additional petitions; Luke's shorter version emphasizes the intimacy of 'Father' and the kingdom's coming", "type": "nt"},
            {"ref": "1 Enoch 15:8-12", "note": "The origin of demons as disembodied Nephilim spirits -- the theological framework for understanding the demonic hierarchy Jesus confronts", "type": "pseudepigrapha"},
            {"ref": "Ecclesiastes 2:18-21", "note": "'I hated all my toil... because I must leave it to the man who will come after me' -- the same futility the Rich Fool discovers too late", "type": "ot"}
        ],

        "divine_council_note": "The Beelzebul controversy (11:14-23) is the most explicit clash between "
                               "Jesus and the demonic hierarchy in the Travel Narrative. The accusation "
                               "that Jesus works 'by Beelzebul, the prince of demons' (11:15) assumes the "
                               "divine council framework: there is a structured spiritual hierarchy with a "
                               "ruling prince. Jesus does not deny the hierarchy's existence -- he engages "
                               "it directly: 'Every kingdom divided against itself is laid waste' (11:17). "
                               "His counter-claim is devastating: 'If it is by the finger of God that I cast "
                               "out demons, then the kingdom of God has come upon you' (11:20). The 'finger "
                               "of God' was the phrase Egypt's magicians used when they recognized a power "
                               "greater than their own gods (Exod 8:19). Jesus is saying: what YHWH did to "
                               "the gods of Egypt, I am doing to the demonic princes now. The strong man "
                               "parable (11:21-22) pictures the demonic occupation of territory: a 'strong "
                               "man, fully armed, guards his own palace.' But 'when one stronger than he "
                               "attacks him and overcomes him, he takes away his armor in which he trusted "
                               "and divides his spoil.' Jesus is the stronger one who plunders the enemy's "
                               "domain -- the Christus Victor motif at the heart of the Gospel.",

        "sections": [
            {
                "heading": "Teach Us to Pray: The Lord's Prayer and the Generous Father (11:1-13)",
                "body": "Luke alone records the disciples' request: 'Lord, teach us to pray, as John "
                        "taught his disciples' (11:1). Jesus responds with a prayer that is shorter than "
                        "Matthew's version but equally profound. 'Father' (Pater) -- no qualifier, no "
                        "distance, just the raw intimacy of address. 'Hallowed be your name' -- the "
                        "divine name is to be honored as holy. 'Your kingdom come' -- the eschatological "
                        "petition for God's reign to fully arrive. 'Give us each day our daily bread "
                        "(ton arton hemon ton epiousion)' -- the mysterious word epiousios (found nowhere "
                        "else in Greek literature) may mean 'for the coming day' or 'supersubstantial,' "
                        "linking daily provision to the manna of the wilderness (Exod 16). 'Forgive us our "
                        "sins, for we ourselves forgive everyone who is indebted to us' -- forgiveness "
                        "given is forgiveness received. 'Lead us not into temptation (peirasmon)' -- not "
                        "that God tempts, but a plea for protection from the eschatological trial (cf. "
                        "Rev 3:10). Jesus follows with the parable of the friend at midnight (11:5-8): "
                        "persistence in prayer is honored. The climax: 'If you then, who are evil, know "
                        "how to give good gifts to your children, how much more will the heavenly Father "
                        "give the Holy Spirit to those who ask him!' (11:13). Where Matthew says 'good "
                        "things,' Luke says 'Holy Spirit' -- the ultimate gift of prayer is God himself."
            },
            {
                "heading": "The Beelzebul Controversy and the Finger of God (11:14-36)",
                "body": "Jesus casts out a mute demon, and the crowd is divided. Some accuse: 'He casts "
                        "out demons by Beelzebul, the prince of demons' (11:15). Others demand a sign from "
                        "heaven (11:16). Jesus exposes the logical absurdity: 'Every kingdom divided against "
                        "itself is laid waste' (11:17). If Satan casts out Satan, his kingdom is finished. "
                        "Then the decisive claim: 'But if it is by the finger of God (daktylō tou theou) "
                        "that I cast out demons, then the kingdom of God has come upon you (ephthasen eph "
                        "hymas)' (11:20). The verb ephthasen is aggressive -- the kingdom has not merely "
                        "drawn near but has arrived, crashed into the present. The 'finger of God' places "
                        "Jesus' exorcisms in the Exodus narrative: the same power that broke Pharaoh's "
                        "magicians now breaks the demonic strongholds. The strong man parable follows "
                        "(11:21-22): the enemy guards his palace until 'one stronger than he attacks him.' "
                        "Jesus is the stronger one who has entered the strong man's house, bound him, and "
                        "is now plundering his goods -- liberating those held captive by demonic oppression. "
                        "The sign of Jonah (11:29-32) is the only sign this generation will receive: 'For "
                        "as Jonah became a sign to the people of Nineveh, so will the Son of Man be to this "
                        "generation' (11:30). The greater-than-Jonah, the greater-than-Solomon is here."
            },
            {
                "heading": "Woes, Warnings, and Fearless Confession (11:37-12:12)",
                "body": "At a Pharisee's dinner, Jesus does not wash before the meal (11:38) -- not from "
                        "negligence but as a prophetic act. What follows is a devastating series of woes. "
                        "To the Pharisees: 'You tithe mint and rue and every herb, and neglect justice and "
                        "the love of God' (11:42). 'You are like unmarked graves (mnēmeia adēla), and "
                        "people walk over them without knowing it' (11:44) -- contact with a grave causes "
                        "ritual impurity (Num 19:16), so the accusation is withering: the Pharisees are "
                        "sources of defilement while appearing clean. To the lawyers: 'You load people with "
                        "burdens hard to bear, and you yourselves do not touch the burdens with one of your "
                        "fingers' (11:46). 'You have taken away the key of knowledge. You did not enter "
                        "yourselves, and you hindered those who were entering' (11:52). The tone shifts to "
                        "encouragement for the disciples: 'Do not fear those who kill the body, and after "
                        "that have nothing more that they can do' (12:4). The real threat is spiritual: "
                        "'Fear him who, after he has killed, has authority to cast into Gehenna' (12:5). "
                        "Yet the Father's care is intimate: 'Even the hairs of your head are all numbered. "
                        "Fear not; you are of more value than many sparrows' (12:7). Those who confess the "
                        "Son of Man before men will be acknowledged before the angels of God (12:8)."
            },
            {
                "heading": "The Rich Fool and the Kingdom's Hidden Growth (12:13-13:21)",
                "body": "A man asks Jesus to divide an inheritance -- a common rabbinic request. Jesus "
                        "refuses and warns: 'Take care, and be on your guard against all covetousness "
                        "(pleonexia), for one's life does not consist in the abundance of his possessions' "
                        "(12:15). The Rich Fool parable follows: a man's land produces abundantly. He plans "
                        "bigger barns, declares, 'Soul (psyche), you have ample goods laid up for many "
                        "years; relax, eat, drink, be merry' (12:19). God's verdict: 'Fool (aphron)! This "
                        "night your soul is required (apaitousin) of you' (12:20). The passive apaitousin "
                        "may imply angelic agents who come to collect -- a Second Temple motif of death "
                        "angels. [C] Jesus draws the lesson: 'So is the one who lays up treasure for "
                        "himself and is not rich toward God' (12:21). The teaching expands: do not be "
                        "anxious about food or clothing (12:22-34). 'Fear not, little flock (mikron "
                        "poimnion), for it is your Father's good pleasure to give you the kingdom' (12:32) "
                        "-- the kingdom is a gift, not a conquest. The section concludes with two parables "
                        "of the kingdom's nature: the mustard seed, tiny but growing into a tree where "
                        "birds nest (13:18-19), and leaven, hidden in flour but transforming the whole "
                        "lump (13:20-21). The kingdom starts small, works invisibly, and cannot be stopped."
            }
        ]
    },

    {
        "id": "luke-journey-03",
        "ref": "Luke 13:22-16:31",
        "chapter_num": 3,
        "title": "Parables of Grace -- The Lost, the Found, and the Great Reversal",
        "era": "luke_journey",
        "type": "study",
        "themes": ["LOVE", "COV", "KING", "NATIONS", "TYPE"],

        "synopsis": "This is the theological heart of Luke's Travel Narrative. The narrow door (13:22-30) "
                    "warns that many who expect entry will be excluded, while people 'from east and west, "
                    "and from north and south' will recline at the kingdom feast -- the nations streaming "
                    "in while insiders are locked out. [A] Jesus laments over Jerusalem: 'O Jerusalem, "
                    "Jerusalem, the city that kills the prophets and stones those who are sent to it! "
                    "How often would I have gathered your children together as a hen gathers her brood "
                    "under her wings, and you were not willing!' (13:34). Chapter 14 contains the great "
                    "banquet parable (14:15-24) where invited guests make excuses and the host sends "
                    "servants to bring in 'the poor and crippled and blind and lame' (14:21). [A] Then "
                    "comes Luke 15 -- the theological centerpiece of the entire Gospel. Three parables "
                    "of the lost: the shepherd who leaves ninety-nine to find one sheep (15:3-7), the "
                    "woman who sweeps the house to find one coin (15:8-10), and the father who runs to "
                    "embrace the returning prodigal (15:11-32). 'There will be more joy in heaven over "
                    "one sinner who repents than over ninety-nine righteous persons who need no "
                    "repentance' (15:7). [A] The elder brother's resentment (15:25-32) mirrors the "
                    "Pharisees' grumbling that triggered the parables (15:1-2). Chapter 16 shifts to "
                    "wealth: the shrewd manager (16:1-13) and the Rich Man and Lazarus (16:19-31), where "
                    "the reversal is total: the beggar is comforted in Abraham's bosom, the rich man "
                    "torments in Hades.",

        "key_verse": {
            "ref": "Luke 15:20",
            "text": "And he arose and came to his father. But while he was still a long way off, his father saw him and felt compassion, and ran and embraced him and kissed him.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "splanchnistheis (moved with compassion -- the father 'felt compassion' (splanchnistheis) for the prodigal (15:20); the same visceral, gut-level mercy; this is the heart of God)",
            "ousia (property / substance -- the prodigal asks for 'the share of property (ousia) that falls to me' (15:12); he demands his inheritance while his father is still alive -- a social death wish)",
            "stole ten proten (the best robe -- the father commands 'bring quickly the best robe (stolen ten proten)' (15:22); the robe of honor, the ring of authority, the sandals of sonship -- full restoration)",
            "apollymi (to lose / destroy / perish -- the key verb linking all three parables: the lost (apollymi) sheep, lost coin, lost son; the Father's mission is to recover what apollymi claims)",
            "kolpos Abraam (Abraham's bosom -- where Lazarus rests after death (16:22); the place of comfort and covenant blessing in Jewish afterlife tradition; the righteous dead at rest with the patriarch)",
            "Hades (the grave / realm of the dead -- where the rich man suffers (16:23); not the final Gehenna but the intermediate state; Luke preserves the OT Sheol concept in Greek dress)",
            "metanoia (repentance / change of mind -- 'there will be joy in heaven over one sinner who repents (metanoia)' (15:7); not mere regret but a total reorientation toward God)"
        ],

        "ane_backdrop": "The Prodigal Son parable operates within the ANE cultural framework of "
                        "patriarchal honor. For a son to demand his inheritance while the father "
                        "lives is to wish him dead -- a devastating social insult in the honor-shame "
                        "culture of the ancient Near East. The father's response violates every "
                        "expectation: he does not disown the son, does not demand public penance, "
                        "but runs to him -- an act considered undignified for an elderly patriarch "
                        "in Mediterranean culture, since it required him to hitch up his robes and "
                        "expose his legs. The robe, ring, and sandals are symbols of full restoration: "
                        "the robe marks him as an honored guest, the ring conveys authority to act in "
                        "the father's name, and sandals distinguish him from a slave (who went barefoot). "
                        "The elder brother's refusal to enter the banquet (15:28) would have been a "
                        "public shaming of the father in honor-shame culture -- his grievance, however "
                        "justified, should have been raised privately. The Rich Man and Lazarus draws "
                        "on Egyptian and Jewish afterlife traditions: the reversal of fortunes after "
                        "death was a common motif in Egyptian tales of the journey to the underworld "
                        "and in Jewish apocalyptic literature (1 Enoch 22).",

        "second_temple": [
            {
                "source": "1 Enoch 22:1-14",
                "summary": "Enoch sees the hollow places where the spirits of the dead are separated "
                           "into compartments: the righteous in a place with a spring of water and light, "
                           "the wicked in darkness and torment, awaiting the great judgment day.",
                "relevance": "Provides the conceptual framework for the Rich Man and Lazarus parable: "
                             "separated compartments in the afterlife, a great chasm (16:26), the righteous "
                             "comforted and the wicked in torment -- Luke draws on the 1 Enoch afterlife "
                             "geography."
            },
            {
                "source": "Psalms of Solomon 5:2-4",
                "summary": "'For if I am hungry, I will cry out to you, O God, and you will give to me. "
                           "You feed the birds and the fish... You provide for the lowly... When the "
                           "righteous are in need, they endure, and in your mercy they will be saved.'",
                "relevance": "The piety of dependence on God for daily provision -- the theological "
                             "backdrop for Lazarus, whose name means 'God helps,' contrasted with the "
                             "rich man who feasted sumptuously while ignoring the beggar at his gate."
            },
            {
                "source": "4Q525 (4QBeatitudes)",
                "summary": "A wisdom text from Qumran that pronounces blessings on the righteous "
                           "poor and those who seek wisdom -- 'Blessed is the one who speaks truth "
                           "with a pure heart and does not slander with his tongue.'",
                "relevance": "The Qumran beatitude tradition resonates with the reversal theme: the "
                             "blessed are not the wealthy and powerful but the humble and faithful, "
                             "the same reversal that plays out in the Prodigal Son and Lazarus."
            }
        ],

        "cross_refs": [
            {"ref": "Ezekiel 34:11-16", "note": "'I myself will search for my sheep, and will seek them out... I will seek the lost, and I will bring back the strayed' -- the shepherd imagery behind the parable of the lost sheep", "type": "ot"},
            {"ref": "Isaiah 25:6-8", "note": "'On this mountain the LORD of hosts will make for all peoples a feast of rich food' -- the eschatological banquet where people come from all directions (13:29)", "type": "ot"},
            {"ref": "Zephaniah 1:7; 3:17", "note": "YHWH's judgment feast and his rejoicing over his people -- the joy in heaven over one sinner who repents (15:7, 10) echoes the divine joy of Zeph 3:17", "type": "ot"},
            {"ref": "2 Samuel 14:33", "note": "David kisses Absalom -- an imperfect OT parallel to the father's embrace of the prodigal; the father's love absorbs the son's rebellion", "type": "ot"},
            {"ref": "1 Enoch 22:1-14", "note": "The afterlife compartments: the righteous in light, the wicked in darkness -- the conceptual background for the Rich Man and Lazarus (16:19-31)", "type": "pseudepigrapha"},
            {"ref": "Matthew 18:12-14", "note": "Matthew's version of the lost sheep parable -- set in the context of children; Luke sets it in the context of tax collectors and sinners (15:1-2)", "type": "nt"}
        ],

        "divine_council_note": "The narrow door teaching (13:22-30) reveals that the kingdom feast will "
                               "include people 'from east and west, and from north and south' (13:29) -- "
                               "a direct reversal of the Deuteronomy 32 allotment where the nations were "
                               "given to lesser elohim. The nations are streaming back to the table of "
                               "YHWH, the Most High, reclaimed from the governance of the rebellious sons "
                               "of God. Jesus' lament over Jerusalem (13:34) reveals the tragedy: God's "
                               "own inheritance (Israel, Deut 32:9) rejects the very one who would gather "
                               "them. The Prodigal Son parable, while primarily about personal repentance, "
                               "carries a cosmic echo: the son who departs to a 'far country' (choran "
                               "makran, 15:13) and lives among pigs (the ultimate symbol of Gentile "
                               "uncleanness) mirrors Israel's exile among the nations -- the covenant "
                               "people scattered among the territories of the hostile elohim. The father "
                               "who runs to the returning son is YHWH reclaiming his own from the far "
                               "country. The Rich Man and Lazarus (16:19-31) presupposes the divine council "
                               "afterlife geography familiar from 1 Enoch 22: compartmentalized Sheol, "
                               "a great chasm, the righteous comforted while the wicked suffer. Abraham "
                               "presides over the righteous side -- as the covenant patriarch, he is the "
                               "host of those who trusted God's promises.",

        "sections": [
            {
                "heading": "The Narrow Door and the Lament Over Jerusalem (13:22-35)",
                "body": "Someone asks: 'Lord, will those who are saved be few?' (13:23). Jesus does not "
                        "answer with a number but with an urgent command: 'Strive (agōnizesthe -- the "
                        "verb of athletic struggle) to enter through the narrow door. For many, I tell "
                        "you, will seek to enter and will not be able' (13:24). The imagery is "
                        "eschatological: the master of the house will shut the door, and those outside "
                        "will knock and plead, 'Lord, open to us' (13:25). His answer is chilling: 'I "
                        "do not know where you come from. Depart from me, all you workers of "
                        "unrighteousness!' (13:27). Yet the shock is the reversal that follows: 'People "
                        "will come from east and west, and from north and south, and recline at table in "
                        "the kingdom of God. And behold, some are last who will be first, and some are "
                        "first who will be last' (13:29-30). The nations -- those under the governance "
                        "of the rebellious elohim since Babel -- will feast at Abraham's table, while "
                        "those who assumed their place was secure will be cast out. Jesus is warned that "
                        "Herod wants to kill him (13:31). His reply: 'Go and tell that fox' (13:32) -- "
                        "a calculated insult; in Jewish tradition, the fox is the insignificant animal. "
                        "Then the lament: 'O Jerusalem, Jerusalem, the city that kills the prophets' "
                        "(13:34). The image of the hen gathering her brood is maternal, tender, grieving."
            },
            {
                "heading": "The Great Banquet and the Cost of Discipleship (14:1-35)",
                "body": "At a Pharisee's Sabbath dinner (14:1), Jesus heals a man with dropsy and "
                        "silences critics: 'Which of you, having a son or an ox that has fallen into "
                        "a well on a Sabbath day, will not immediately pull him out?' (14:5). He observes "
                        "guests choosing places of honor and teaches: 'Everyone who exalts himself will "
                        "be humbled, and he who humbles himself will be exalted' (14:11) -- the great "
                        "reversal principle. The parable of the great banquet (14:15-24) is the "
                        "centerpiece: a man prepares a feast and sends invitations. But all the invited "
                        "guests make excuses -- a field to see, oxen to examine, a wife newly married. "
                        "The host sends servants to bring in 'the poor and crippled and blind and lame' "
                        "(14:21) from the streets, and then from 'the highways and hedges' (14:23). The "
                        "first group represents the outcasts of Israel; the second, the Gentiles beyond "
                        "the city walls. 'None of those men who were invited shall taste my banquet' "
                        "(14:24). The application to Jesus' ministry is transparent: the religious "
                        "establishment declines the kingdom invitation, and God fills his table with "
                        "those they despise. Jesus then lays out the cost of discipleship in its "
                        "starkest terms: 'If anyone comes to me and does not hate his own father and "
                        "mother and wife and children... he cannot be my disciple' (14:26). The Semitic "
                        "idiom of 'hate' means to love less by comparison -- total allegiance to Jesus "
                        "must exceed every other loyalty."
            },
            {
                "heading": "The Lost Sheep, Lost Coin, and the Prodigal Son (15:1-32)",
                "body": "Luke 15 is the theological summit of the Travel Narrative. The setting is "
                        "crucial: 'Now the tax collectors and sinners were all drawing near to hear him. "
                        "And the Pharisees and the scribes grumbled, saying, \"This man receives sinners "
                        "and eats with them\"' (15:1-2). The three parables that follow are Jesus' "
                        "defense of his scandalous table fellowship. A shepherd with a hundred sheep loses "
                        "one and 'goes after the one that is lost, until he finds it' (15:4). A woman "
                        "with ten silver coins loses one and sweeps the house until she finds it. In both "
                        "cases, recovery triggers communal celebration: 'there will be more joy in heaven "
                        "over one sinner who repents' (15:7). Then comes the parable of the prodigal son "
                        "(15:11-32) -- more accurately, the parable of the gracious father. The younger "
                        "son demands his share of the ousia (inheritance), squanders it in a far country, "
                        "and hits bottom feeding pigs. He comes to himself (eis heauton de elthon, 15:17) "
                        "and rehearses a speech of repentance. But the father sees him 'while he was still "
                        "a long way off' (15:20) -- the father has been watching, waiting, longing. He "
                        "runs, embraces, kisses. Robe, ring, sandals, fattened calf. The elder brother "
                        "refuses to enter the party and accuses the father of injustice (15:29-30). The "
                        "father's reply: 'It was fitting to celebrate... for this your brother was dead, "
                        "and is alive; he was lost, and is found' (15:32)."
            },
            {
                "heading": "The Shrewd Manager, Lazarus, and the Great Reversal (16:1-31)",
                "body": "The parable of the shrewd manager (16:1-13) is among the most debated in the "
                        "Gospels. A manager about to be fired reduces his master's debtors' bills -- and "
                        "the master commends him for his shrewdness (phronimos). The point is not that "
                        "dishonesty is virtuous but that 'the sons of this age are more shrewd in dealing "
                        "with their own generation than the sons of light' (16:8). Kingdom people should "
                        "be at least as strategic with eternal resources as worldly people are with "
                        "temporal ones. The conclusion is absolute: 'You cannot serve God and money "
                        "(mamona)' (16:13). The Pharisees, 'who were lovers of money (philargyroi), heard "
                        "all these things, and they ridiculed him' (16:14). The Rich Man and Lazarus "
                        "(16:19-31) completes the reversal. The rich man feasts in purple and fine linen; "
                        "Lazarus lies at his gate, covered with sores, longing for scraps. Both die. "
                        "Lazarus is carried by angels to Abraham's bosom (kolpos Abraam, 16:22). The "
                        "rich man is in Hades, in torment. He begs Abraham to send Lazarus to cool his "
                        "tongue -- still treating the beggar as a servant. Abraham's answer is final: "
                        "'Between us and you a great chasm (chasma mega) has been fixed' (16:26). The "
                        "rich man begs that Lazarus be sent to warn his brothers. Abraham's devastating "
                        "reply: 'They have Moses and the Prophets; let them hear them... If they do not "
                        "hear Moses and the Prophets, neither will they be convinced if someone should "
                        "rise from the dead' (16:29, 31) -- prophetic irony pointing to Jesus' own "
                        "resurrection, which many will also reject."
            }
        ]
    },

    {
        "id": "luke-journey-04",
        "ref": "Luke 17:1-19:27",
        "chapter_num": 4,
        "title": "Faith on the Road -- Gratitude, Persistence, and the Son of Man's Mission",
        "era": "luke_journey",
        "type": "study",
        "themes": ["KING", "LOVE", "NATIONS", "COV", "DC"],

        "synopsis": "The final section of the Travel Narrative moves toward Jerusalem with increasing "
                    "urgency. Jesus teaches on forgiveness and faith: 'If you had faith like a grain of "
                    "mustard seed, you could say to this mulberry tree, \"Be uprooted and planted in the "
                    "sea,\" and it would obey you' (17:6). [A] The ten lepers (17:11-19) crystallize "
                    "Luke's Samaritan theology: ten are cleansed, but only one returns to give thanks -- "
                    "'and he was a Samaritan' (17:16). Jesus asks the devastating question: 'Was no one "
                    "found to return and give praise to God except this foreigner (allogenes)?' (17:18). "
                    "The kingdom's location is redefined: 'The kingdom of God is in the midst of you "
                    "(entos hymon)' (17:21) -- not a political territory but a present reality centered "
                    "on Jesus himself. [A] The Son of Man's coming will be sudden and unmistakable: "
                    "'as the lightning flashes and lights up the sky from one side to the other, so will "
                    "the Son of Man be in his day' (17:24). [A] Two parables address prayer and "
                    "humility: the persistent widow (18:1-8) who demands justice until the unjust judge "
                    "relents, and the Pharisee and tax collector (18:9-14) -- 'everyone who exalts "
                    "himself will be humbled, but the one who humbles himself will be exalted' (18:14). "
                    "The rich ruler (18:18-25) cannot release his wealth. Zacchaeus (19:1-10) can -- and "
                    "receives the Travel Narrative's thesis: 'For the Son of Man came to seek and to "
                    "save the lost' (19:10). [A] The parable of the ten minas (19:11-27) prepares for "
                    "Jerusalem: a nobleman goes to receive a kingdom and returns to settle accounts.",

        "key_verse": {
            "ref": "Luke 19:10",
            "text": "For the Son of Man came to seek and to save the lost.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "allogenes (foreigner / one of another race -- 'this foreigner' (17:18); the grateful Samaritan leper; the term appears in the Jerusalem Temple warning inscription forbidding Gentile entry)",
            "entos hymon (in the midst of you / within you -- 'the kingdom of God is entos hymon' (17:21); debated: 'within you' (interior spiritual reality) or 'among you' (Jesus' present ministry); both are theologically true)",
            "ekdikēsin (justice / vindication -- 'will not God give justice (ekdikēsin) to his elect?' (18:7); not revenge but righteous vindication; the persistent widow's cry is the cry of God's people under oppression)",
            "hilasthēti (be merciful / be propitiated -- 'God, be merciful (hilasthēti) to me, a sinner!' (18:13); the tax collector's prayer uses sacrificial language -- he appeals to the mercy seat, the place of atonement)",
            "sōsai (to save -- 'the Son of Man came to seek and to save (sōsai) the lost' (19:10); the comprehensive salvation: rescue from sin, death, and the hostile powers; Luke's thesis statement)",
            "mna (mina -- a unit of money (19:13); each servant receives one mina; unlike Matthew's talents (varying amounts), Luke's equal distribution tests faithfulness with equal opportunity)",
            "teleios (made whole / complete -- 'your faith has made you well (sesōken)' (17:19); the grateful leper receives not just healing but salvation -- the same verb sōzō used for spiritual rescue)"
        ],

        "ane_backdrop": "The ten lepers (17:11-19) reflects the social reality of leprosy in the "
                        "ancient world. Leviticus 13-14 required lepers to live outside the camp and "
                        "cry 'Unclean, unclean!' when approached. That the group includes a Samaritan "
                        "alongside Jews is remarkable -- disease had overridden ethnic boundaries. The "
                        "command to 'show yourselves to the priests' (17:14) follows Levitical protocol "
                        "for certification of healing (Lev 14:1-32). The Pharisee and tax collector "
                        "parable (18:9-14) operates within the honor-shame dynamics of Second Temple "
                        "synagogue culture. The Pharisee's prayer is not atypical -- thanksgiving for "
                        "covenant faithfulness was a recognized prayer form. But his prayer is directed "
                        "at himself ('he prayed thus with himself,' pros heauton, 18:11), while the tax "
                        "collector 'would not even lift up his eyes to heaven' (18:13) -- the posture "
                        "of absolute shame. The parable of the ten minas (19:11-27) draws on a known "
                        "historical event: Archelaus, son of Herod the Great, traveled to Rome in 4 BC "
                        "to receive his kingdom, and a Jewish delegation followed to oppose him "
                        "(Josephus, Ant. 17.11.1) -- the parable's 'citizens who hated him' (19:14) "
                        "directly echoes this event.",

        "second_temple": [
            {
                "source": "Temple Warning Inscription (OGIS 598)",
                "summary": "A Greek inscription from the Jerusalem Temple reads: 'No foreigner "
                           "(allogenes) is to enter within the balustrade and embankment around the "
                           "sanctuary. Whoever is caught will have himself to blame for his death.'",
                "relevance": "The same word allogenes that Jesus uses for the grateful Samaritan "
                             "(17:18) appears on the Temple barrier excluding Gentiles. The Samaritan "
                             "whom the Temple excludes is the one who gives glory to God -- a profound "
                             "irony in Luke's narrative."
            },
            {
                "source": "Josephus, Antiquities 17.11.1-2",
                "summary": "After Herod's death, Archelaus went to Rome to have his kingship "
                           "confirmed by Augustus. A delegation of fifty Jews followed to protest "
                           "his rule, preferring direct Roman governance.",
                "relevance": "The historical background for the parable of the ten minas: 'A nobleman "
                             "went into a far country to receive for himself a kingdom... But his "
                             "citizens hated him and sent a delegation after him' (19:12, 14). Jesus' "
                             "audience would have recognized the Archelaus allusion immediately."
            },
            {
                "source": "Targum Neofiti on Leviticus 14",
                "summary": "The Targum expands the cleansing ritual for healed lepers with "
                           "elaborate ceremonial detail, emphasizing the priest's role in certifying "
                           "restoration to the covenant community.",
                "relevance": "Illuminates Jesus' command to the ten lepers: 'Go and show yourselves "
                             "to the priests' (17:14). The healing was the miracle; the priestly "
                             "certification was the social and covenantal restoration."
            }
        ],

        "cross_refs": [
            {"ref": "Leviticus 13-14", "note": "The leprosy regulations: diagnosis, isolation, and the purification ritual -- the system Jesus engages when he sends the ten lepers to the priests (17:14)", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "'One like a son of man' coming on clouds with dominion -- the background for Jesus' Son of Man sayings about his sudden, glorious return (17:24-30)", "type": "ot"},
            {"ref": "Genesis 18-19", "note": "The destruction of Sodom: 'on the day when Lot went out from Sodom, fire and sulfur rained from heaven' (17:29) -- the prototype for the Son of Man's sudden coming", "type": "ot"},
            {"ref": "Psalm 51:1-2", "note": "'Have mercy on me, O God' -- the spiritual posture behind the tax collector's prayer: 'God, be merciful to me, a sinner!' (18:13)", "type": "ot"},
            {"ref": "Ezekiel 34:16", "note": "'I will seek the lost, and I will bring back the strayed' -- the divine shepherd mission fulfilled in 'the Son of Man came to seek and to save the lost' (19:10)", "type": "ot"},
            {"ref": "Matthew 25:14-30", "note": "Matthew's parable of the talents -- similar structure but different details; Luke's minas are equal amounts, emphasizing faithfulness over capacity", "type": "nt"},
            {"ref": "1 Enoch 62:1-5", "note": "The Son of Man seated on his throne of glory, judging kings and the mighty -- the eschatological Son of Man tradition behind Jesus' return language (17:24-30)", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "The Son of Man's return (17:22-37) draws on Daniel 7:13-14, where 'one "
                               "like a son of man' approaches the Ancient of Days and receives dominion "
                               "over all nations. This is a divine council enthronement scene: the Son of "
                               "Man is presented before the council, invested with authority, and given "
                               "the nations that were allotted to the rebellious bene elohim at Babel "
                               "(Deut 32:8). Jesus' declaration that 'the Son of Man came to seek and to "
                               "save the lost' (19:10) is the mission statement of this cosmic reclamation: "
                               "the lost are not merely individuals who have wandered but the nations and "
                               "peoples held captive under hostile spiritual governance. The Samaritan "
                               "leper's gratitude (17:15-18) is a case study: the foreigner (allogenes) "
                               "-- excluded from the Temple, outside the covenant boundaries as drawn by "
                               "the religious establishment -- is the one who recognizes the God of Israel "
                               "at work. The Temple inscription forbade the allogenes from entering God's "
                               "presence; Jesus declares that this allogenes has been 'made well' (sesōken, "
                               "17:19) -- the same verb for salvation. The territorial and ethnic barriers "
                               "maintained by the old order are being dismantled as the Son of Man reclaims "
                               "what the rebellious elohim corrupted. The parable of the ten minas (19:11-27) "
                               "pictures the king who departs to receive his kingdom and returns to judge -- "
                               "the Daniel 7 pattern of the Son of Man receiving dominion and returning to "
                               "exercise it.",

        "sections": [
            {
                "heading": "The Ten Lepers and the Kingdom in Your Midst (17:1-21)",
                "body": "Jesus teaches on stumbling blocks, forgiveness, and faith (17:1-10). The parable "
                        "of the unworthy servant (17:7-10) establishes the baseline: 'When you have done "
                        "all that you were commanded, say, \"We are unworthy servants; we have only done "
                        "what was our duty\"' (17:10). Then comes the ten lepers (17:11-19), set on the "
                        "border between Samaria and Galilee -- liminal territory, the boundary zone. Ten "
                        "lepers stand at a distance and cry out: 'Jesus, Master (epistata), have mercy on "
                        "us' (17:13). Jesus sends them to the priests, and 'as they went they were cleansed' "
                        "(17:14) -- the healing happens in the act of obedience. One turns back, falls at "
                        "Jesus' feet, and gives thanks. 'And he was a Samaritan' (17:16). Jesus' question "
                        "cuts deep: 'Were not ten cleansed? Where are the nine? Was no one found to return "
                        "and give praise to God except this foreigner (allogenes)?' (17:17-18). The nine "
                        "were healed; the Samaritan was saved -- 'Rise and go your way; your faith has "
                        "made you well (sesōken se)' (17:19). The verb sōzō means both physical healing "
                        "and spiritual salvation. The Pharisees then ask when the kingdom is coming (17:20). "
                        "Jesus' answer redefines their categories: 'The kingdom of God is not coming in "
                        "ways that can be observed... the kingdom of God is in the midst of you (entos "
                        "hymon)' (17:20-21). The kingdom is not a geopolitical event to watch for but a "
                        "present reality centered on the person of Jesus himself."
            },
            {
                "heading": "The Son of Man's Day and the Call to Readiness (17:22-37)",
                "body": "Jesus turns to eschatology. 'The days are coming when you will desire to see one "
                        "of the days of the Son of Man, and you will not see it' (17:22). The period "
                        "between his departure and return will be one of longing. False reports will "
                        "abound: 'They will say to you, \"Look, there!\" or \"Look, here!\" Do not go out "
                        "or follow them' (17:23). The real event will need no announcement: 'as the "
                        "lightning flashes and lights up the sky from one side to the other, so will the "
                        "Son of Man be in his day' (17:24). But first comes suffering: 'he must suffer "
                        "many things and be rejected by this generation' (17:25) -- the cross precedes the "
                        "glory, always. Jesus draws two OT parallels: the days of Noah (17:26-27) and the "
                        "days of Lot (17:28-29). In both cases, life continued normally -- eating, drinking, "
                        "buying, selling, planting, building -- until sudden judgment arrived. 'So will it "
                        "be on the day when the Son of Man is revealed (apokalyptetai)' (17:30). The "
                        "instruction is stark: 'Remember Lot's wife' (17:32) -- she looked back and was "
                        "lost. 'Whoever seeks to preserve his life will lose it, but whoever loses his "
                        "life will keep it' (17:33). The language of 'two in one bed, one taken and the "
                        "other left; two grinding together, one taken and the other left' (17:34-35) "
                        "pictures the sudden, selective nature of the Son of Man's coming -- not gradual "
                        "social change but decisive, cosmic intervention."
            },
            {
                "heading": "Parables of Prayer and the Rich Ruler's Failure (18:1-30)",
                "body": "Luke introduces the persistent widow parable with rare editorial comment: Jesus "
                        "'told them a parable to the effect that they ought always to pray and not lose "
                        "heart' (18:1). An unjust judge 'neither feared God nor respected man' (18:2). A "
                        "widow keeps coming to him: 'Give me justice (ekdikēson) against my adversary' "
                        "(18:3). The judge relents not from righteousness but from exhaustion: 'lest she "
                        "beat me down by her continual coming' (18:5). Jesus argues from lesser to greater: "
                        "if a corrupt judge yields to persistence, 'will not God give justice to his elect, "
                        "who cry to him day and night?' (18:7). The Pharisee and tax collector (18:9-14) "
                        "targets 'some who trusted in themselves that they were righteous' (18:9). The "
                        "Pharisee's prayer is a resume: 'I fast twice a week; I give tithes of all that I "
                        "get' (18:12). The tax collector 'would not even lift up his eyes to heaven, but "
                        "beat his breast, saying, \"God, be merciful (hilasthēti) to me, a sinner!\"' "
                        "(18:13). The verb hilasthēti is sacrificial -- it means 'be propitiated,' evoking "
                        "the mercy seat (hilastērion) where atonement is made. The verdict: 'This man went "
                        "down to his house justified (dedikaiomenos), rather than the other' (18:14). A "
                        "ruler then asks about eternal life (18:18). Jesus lists the commandments; the man "
                        "claims compliance. 'One thing you still lack. Sell all that you have and distribute "
                        "to the poor' (18:22). The man becomes sad, 'for he was extremely rich' (18:23)."
            },
            {
                "heading": "Zacchaeus, the Ten Minas, and the Son of Man's Mission (19:1-27)",
                "body": "Jesus enters Jericho, and 'a man was there named Zacchaeus. He was a chief tax "
                        "collector and was rich' (19:2). He climbs a sycamore tree to see Jesus -- a "
                        "comical and undignified act for a wealthy man, mirroring the father who runs to "
                        "the prodigal. Jesus looks up: 'Zacchaeus, hurry and come down, for I must (dei "
                        "-- divine necessity) stay at your house today' (19:5). The crowd grumbles: 'He "
                        "has gone in to be the guest of a man who is a sinner' (19:7) -- the same "
                        "complaint that triggered the Luke 15 parables. Zacchaeus responds with radical "
                        "generosity: 'Behold, Lord, the half of my goods I give to the poor. And if I "
                        "have defrauded anyone of anything, I restore it fourfold' (19:8) -- exceeding "
                        "the Torah's restitution requirement (Exod 22:1 requires fourfold only for stolen "
                        "livestock). Jesus declares: 'Today salvation has come to this house, since he also "
                        "is a son of Abraham' (19:9). Then the thesis statement: 'For the Son of Man came "
                        "to seek and to save the lost' (19:10). The verb 'seek' (zētēsai) echoes Ezekiel "
                        "34:16: 'I will seek the lost.' Jesus is YHWH the shepherd in the flesh, doing "
                        "what God promised through the prophet. The parable of the ten minas (19:11-27) "
                        "follows because they were 'near to Jerusalem' and people 'supposed that the "
                        "kingdom of God was to appear immediately' (19:11). The parable corrects: the king "
                        "departs, entrusts resources, and returns to settle accounts. Faithful servants "
                        "receive authority over cities. The wicked servant who hid his mina loses even "
                        "that. The citizens who rejected the king face judgment (19:27). The Travel "
                        "Narrative closes with the road to Jerusalem fully in view."
            }
        ]
    }
]
