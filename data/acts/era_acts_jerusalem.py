"""
era_acts_jerusalem.py -- Acts 1-12: Ascension, Pentecost, and the Jerusalem Church

The first half of Acts covers the founding and early expansion of the church
in Jerusalem, Judea, and Samaria. The ascension completes Jesus' "exodus"
(Luke 9:31). Pentecost reverses Babel -- the Spirit descends, the nations
hear in their own languages, and 3,000 are added. The Jerusalem church is
established with apostolic teaching, fellowship, breaking of bread, and
prayer. Stephen delivers the longest speech in Acts, retelling Israel's
history as a divine council narrative. Philip takes the gospel to Samaria
and the Ethiopian eunuch. Saul is converted on the Damascus road. Peter's
vision and the conversion of Cornelius demolish the Jew-Gentile barrier.
The church in Antioch sends the gospel to the nations.
"""

CHAPTERS = [
    {
        "id": "acts-1-2",
        "ref": "Acts 1-2",
        "chapter_num": 1,
        "title": "The Ascension and Pentecost -- The Spirit Poured Out on All Flesh",
        "era": "acts_jerusalem",
        "type": "study",
        "themes": ["DC", "KING", "NATIONS", "NAME", "SEED"],

        "synopsis": "Acts opens where Luke's Gospel ends: the risen Jesus spends 40 days teaching the "
                    "apostles about 'the kingdom of God' (1:3). He commissions them: 'You will receive "
                    "power (dynamin) when the Holy Spirit has come upon you, and you will be my "
                    "witnesses in Jerusalem and in all Judea and Samaria, and to the end of the earth' "
                    "(1:8). He ascends from the Mount of Olives, and two angels promise his return "
                    "(1:10-11). The disciples wait in Jerusalem. On the day of Pentecost (Shavuot -- "
                    "the harvest festival, 50 days after Passover), the Spirit comes as 'a sound like "
                    "a mighty rushing wind' and 'divided tongues as of fire' (2:2-3). They speak in "
                    "the languages of the gathered nations (2:4-11). Peter's sermon explains: this "
                    "fulfills Joel 2:28-32 ('I will pour out my Spirit on all flesh'), and Jesus, "
                    "crucified and risen, has been 'exalted at the right hand of God' (2:33). He "
                    "quotes Psalm 16 (the resurrection) and Psalm 110 (the ascension to God's right "
                    "hand). 'Let all the house of Israel therefore know for certain that God has made "
                    "him both Lord and Christ' (2:36). 3,000 are baptized (2:41). The church is born.",

        "key_verse": {
            "ref": "Acts 2:5-6",
            "text": "Now there were dwelling in Jerusalem Jews, devout men from every nation under heaven. And at this sound the multitude came together, and they were bewildered, because each one was hearing them speak in his own language.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "dynamis (power -- 'you will receive power when the Holy Spirit has come upon you' (1:8); the Spirit's empowerment for witness; the same power that raised Jesus from the dead)",
            "glossais (tongues / languages -- the Spirit enables the disciples to speak in the languages of the nations; the reversal of Babel's linguistic confusion)",
            "pantos ethnous (every nation -- 'devout men from every nation under heaven' (2:5); the nations of Genesis 10, scattered at Babel, now gathered by the Spirit)",
            "dexia tou theou (right hand of God -- 'exalted at the right hand of God' (2:33); the Psalm 110:1 position; the supreme seat in the divine council)",
            "Kyrios kai Christos (Lord and Christ -- 'God has made him both Lord and Christ' (2:36); the dual title: divine authority (Lord/Kyrios) and messianic office (Christ/Christos))"
        ],

        "ane_backdrop": "Pentecost (Shavuot) was originally the Festival of Weeks, celebrating the "
                        "wheat harvest (Exod 34:22; Deut 16:10). By the Second Temple period, it was "
                        "also associated with the giving of the Torah at Sinai (based on the chronology "
                        "of Exodus 19:1, which places Israel's arrival at Sinai in the third month). "
                        "The connection is theologically rich: at Sinai, YHWH descended with fire and "
                        "thunder (Exod 19:18); at Pentecost, the Spirit descends with wind and fire "
                        "(Acts 2:2-3). At Sinai, the Torah was given to one nation (Israel); at "
                        "Pentecost, the Spirit is given to all nations. A Jewish tradition (Midrash "
                        "Tanhuma, Shemot 22; b. Shabbat 88b) says that when God spoke at Sinai, his "
                        "voice divided into 70 languages so all nations could hear -- a direct parallel "
                        "to Pentecost's multilingual miracle. The Babel-Pentecost reversal is the "
                        "cosmic counterpart: Babel confused the languages and divided the nations; "
                        "Pentecost restores communication and gathers the nations.",

        "second_temple": [
            {
                "source": "Philo, On the Decalogue 33, 46 (1st century AD)",
                "summary": "Philo describes the voice at Sinai as a 'fire that was articulate, "
                           "producing a voice' that became 'a language that could be heard' by all, "
                           "so that 'even the furthest nations might hear.'",
                "relevance": "Philo's description of the Sinai theophany -- articulate fire producing "
                             "a universal voice -- closely parallels Acts 2's 'tongues of fire' and "
                             "multilingual speech, suggesting Luke draws on this Sinai-Pentecost "
                             "typology intentionally."
            },
            {
                "source": "Jubilees 6:17-22",
                "summary": "Jubilees connects the Festival of Weeks (Shavuot) to the renewal of the "
                           "covenant and dates it as the oldest festival, celebrated by Noah and "
                           "the patriarchs.",
                "relevance": "Shows that the covenantal significance of Shavuot was well-established "
                             "in Second Temple Judaism, supporting the reading of Pentecost as the "
                             "inauguration of the new covenant through the Spirit."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 11:1-9", "note": "The Tower of Babel: YHWH confused the languages and scattered the nations -- Pentecost reverses both: the Spirit gives languages and gathers the nations", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God at Babel -- the worldview that Pentecost's 'every nation under heaven' (2:5) is undoing", "type": "ot"},
            {"ref": "Joel 2:28-32", "note": "'I will pour out my Spirit on all flesh' -- quoted by Peter (2:17-21) as fulfilled at Pentecost; the Spirit for ALL flesh, not just Israel", "type": "ot"},
            {"ref": "Psalm 16:8-11", "note": "'You will not abandon my soul to Hades, or let your Holy One see corruption' -- quoted by Peter (2:25-28) as fulfilled in the resurrection", "type": "ot"},
            {"ref": "Psalm 110:1", "note": "'The Lord said to my Lord: Sit at my right hand' -- quoted by Peter (2:34-35) as fulfilled in the ascension", "type": "ot"},
            {"ref": "Exodus 19:16-19", "note": "The Sinai theophany: fire, thunder, and YHWH's descent -- the typological background to Pentecost's wind and fire", "type": "ot"},
            {"ref": "Luke 24:49", "note": "'I am sending the promise of my Father upon you' -- the promise fulfilled at Pentecost", "type": "nt"}
        ],

        "divine_council_note": "Pentecost is the definitive divine council event in the New Testament. "
                               "At Babel (Gen 11), YHWH confused the languages and, according to "
                               "Deuteronomy 32:8-9, allotted the nations to the sons of God (bene "
                               "elohim), keeping Israel as his own portion. The 70 nations of Genesis 10 "
                               "(72 in the LXX) were placed under the governance of lesser elohim, who "
                               "subsequently corrupted their rule (Psalm 82). At Pentecost, the Spirit "
                               "reverses this: (1) The languages confused at Babel are restored -- the "
                               "disciples speak 'in other tongues (heterais glossais)' (2:4), and people "
                               "'from every nation under heaven' (2:5) hear 'in their own language' "
                               "(2:6, 8, 11). (2) The nations scattered at Babel are gathered -- the "
                               "list of nations in 2:9-11 represents the entire known world, from "
                               "Parthia in the east to Rome in the west. (3) The Spirit confined to "
                               "Israel is poured out 'on all flesh' (2:17) -- breaking the Deuteronomy "
                               "32 restriction. Peter's sermon then connects Pentecost to the divine "
                               "council through Psalm 110:1: 'The Lord said to my Lord: Sit at my right "
                               "hand' (2:34). Jesus has been 'exalted at the right hand of God' (2:33) "
                               "-- installed in the supreme position in the heavenly council -- and from "
                               "that position has 'poured out this that you yourselves are seeing and "
                               "hearing' (2:33). The Spirit is the agent of the enthroned Son's "
                               "reclamation program. The 3,000 baptized (2:41) are the firstfruits of "
                               "the Babel reversal.",

        "sections": [
            {
                "heading": "The Ascension and the Wait for Power (1:1-26)",
                "body": "Acts opens: 'In the first book, O Theophilus, I dealt with all that Jesus "
                        "began to do and teach' (1:1) -- the word 'began' (erxato) implies Acts "
                        "records what Jesus continues to do through the Spirit and the church. Jesus "
                        "instructs the apostles to wait in Jerusalem for 'the promise of the Father' "
                        "(1:4) -- the Holy Spirit. 'You will receive power (dynamin) when the Holy "
                        "Spirit has come upon you, and you will be my witnesses in Jerusalem and in "
                        "all Judea and Samaria, and to the end of the earth' (1:8). This verse is the "
                        "outline for all of Acts: chapters 1-7 (Jerusalem), 8-12 (Judea and Samaria), "
                        "13-28 (the end of the earth). Jesus ascends (1:9), and two angels ask: 'Men "
                        "of Galilee, why do you stand looking into heaven? This Jesus, who was taken "
                        "up from you into heaven, will come in the same way as you saw him go' (1:11). "
                        "The ascension is not departure but enthronement: Jesus takes his seat at the "
                        "right hand of the Father. Matthias is chosen to replace Judas (1:15-26)."
            },
            {
                "heading": "Pentecost: Babel Reversed (2:1-47)",
                "body": "On the day of Pentecost, 'suddenly there came from heaven a sound like a "
                        "mighty rushing wind (pnoe), and it filled the entire house' (2:2). 'Divided "
                        "tongues as of fire appeared to them and rested on each one of them. And they "
                        "were all filled with the Holy Spirit and began to speak in other tongues "
                        "(heterais glossais) as the Spirit gave them utterance' (2:3-4). Jews 'from "
                        "every nation under heaven' are bewildered: 'How is it that we hear, each of "
                        "us in his own native language (dialekto)?' (2:8). The nation list (2:9-11) "
                        "spans the known world. Peter's sermon: 'This is what was uttered through the "
                        "prophet Joel: \"In the last days it shall be, God declares, that I will pour "
                        "out my Spirit on all flesh\"' (2:16-17). He argues: David prophesied the "
                        "resurrection (Ps 16:10, 'you will not abandon my soul to Hades') and the "
                        "ascension (Ps 110:1, 'sit at my right hand'). 'God has made him both Lord "
                        "(Kyrios) and Christ (Christos), this Jesus whom you crucified' (2:36). The "
                        "crowd is cut to the heart: 'What shall we do?' (2:37). 'Repent and be baptized "
                        "every one of you in the name of Jesus Christ for the forgiveness of your sins, "
                        "and you will receive the gift of the Holy Spirit. For the promise is for you "
                        "and for your children and for all who are far off (pasin tois eis makran) -- "
                        "everyone whom the Lord our God calls to himself' (2:38-39). 'All who are far "
                        "off' -- the nations! 3,000 souls are added (2:41). The early church: 'They "
                        "devoted themselves to the apostles' teaching and the fellowship, to the "
                        "breaking of bread and the prayers' (2:42)."
            }
        ]
    },

    {
        "id": "acts-3-7",
        "ref": "Acts 3-7",
        "chapter_num": 2,
        "title": "The Early Church, Temple Confrontations, and Stephen's Martyrdom",
        "era": "acts_jerusalem",
        "type": "study",
        "themes": ["DC", "KING", "SPIRIT", "NATIONS", "BLOOD"],

        "synopsis": "The early church grows amid opposition. Peter heals a lame man at the Temple "
                    "gate (3:1-10) and preaches: Jesus is 'the Author of life, whom God raised from "
                    "the dead' (3:15) and 'the prophet like Moses' of Deuteronomy 18:15 (3:22). Peter "
                    "and John are arrested, tried before the Sanhedrin, and released (4:1-22). The "
                    "community shares possessions (4:32-37). Ananias and Sapphira die for lying to "
                    "the Holy Spirit (5:1-11). Apostles are arrested again and miraculously freed "
                    "(5:17-42). Gamaliel counsels patience (5:34-39). Seven servants (including "
                    "Stephen and Philip) are appointed (6:1-7). Stephen, 'full of grace and power' "
                    "(6:8), is accused of blasphemy and delivers the longest speech in Acts (7:2-53) "
                    "-- a retelling of Israel's history that indicts the nation for repeated rejection "
                    "of God's chosen agents. Stephen sees 'the heavens opened, and the Son of Man "
                    "standing at the right hand of God' (7:56). He is stoned to death (7:58-60), "
                    "becoming the first Christian martyr. Saul watches, approving (7:58; 8:1).",

        "key_verse": {
            "ref": "Acts 7:42-43",
            "text": "But God turned away and gave them over to worship the host of heaven, as it is written in the book of the prophets: 'Did you bring to me slain beasts and sacrifices, during the forty years in the wilderness, O house of Israel? You took up the tent of Moloch and the star of your god Rephan, the images that you made to worship.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "stratia tou ouranou (host of heaven -- the celestial powers; Deut 4:19 says YHWH 'allotted' them to the nations; Israel was forbidden to worship them but did so anyway (7:42))",
            "archegos tes zoes (Author / Prince of life -- Peter's title for Jesus (3:15); the one who originates and leads into life; a divine council title for the Son)",
            "prophetes (prophet -- Jesus as 'the prophet like Moses' (3:22, quoting Deut 18:15); the definitive spokesman of YHWH's council)",
            "ho huios tou anthropou (the Son of Man -- Stephen's vision: 'I see the heavens opened and the Son of Man standing at the right hand of God' (7:56); the Daniel 7 figure enthroned)",
            "eis diatagas angelon (delivered by/through angels -- 'you who received the law as ordained by angels' (7:53); the angelic mediation of Torah; divine council members delivering YHWH's law)"
        ],

        "ane_backdrop": "Stephen's speech retells Israel's history using the pattern of the rejected "
                        "agent -- a common ANE motif where a deity's messenger is mistreated by the "
                        "very people sent to receive the message. The reference to 'the host of heaven' "
                        "(stratia tou ouranou, 7:42) connects to the ANE tradition of astral worship: "
                        "the sun, moon, stars, and planets were worshiped as deities throughout the "
                        "ancient Near East. Deuteronomy 4:19 acknowledges that YHWH 'allotted' these "
                        "celestial bodies to the nations -- they were assigned as objects of worship for "
                        "the Gentiles, but Israel was forbidden to worship them. Stephen's point: Israel "
                        "adopted the worship practices of the nations and was therefore 'given over' "
                        "to this idolatry as judgment. Moloch (Molek) was a Canaanite deity associated "
                        "with child sacrifice; Rephan (Remphan/Kaiwan) was likely Saturn, worshiped in "
                        "Mesopotamia as a planetary deity.",

        "second_temple": [
            {
                "source": "Jubilees 15:31-32",
                "summary": "God assigned angels (spirits) over the nations to lead them astray, but "
                           "over Israel he placed no angel or spirit: 'I alone am their ruler, and "
                           "I alone shall watch over them.'",
                "relevance": "Provides the Second Temple background for Stephen's argument: the nations "
                             "were assigned to spiritual rulers (the 'host of heaven'), but Israel was "
                             "supposed to worship YHWH alone. By worshiping the host of heaven, Israel "
                             "joined the nations in their error."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 4:19", "note": "YHWH 'allotted' the host of heaven to 'all the peoples under the whole heaven' -- the Deut 32 worldview that Stephen references in 7:42", "type": "ot"},
            {"ref": "Deuteronomy 18:15", "note": "'The LORD your God will raise up for you a prophet like me' -- quoted by Peter (3:22) and Stephen (7:37) as fulfilled in Jesus", "type": "ot"},
            {"ref": "Amos 5:25-27", "note": "'Did you bring me sacrifices... You took up Sikkuth your king and Kaiwan your star-god' -- quoted by Stephen (7:42-43) about Israel's astral idolatry", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "The Son of Man before the Ancient of Days -- the vision Stephen sees: 'the Son of Man standing at the right hand of God' (7:56)", "type": "ot"},
            {"ref": "Psalm 82", "note": "The judgment of the gods -- the background to the 'host of heaven' that the nations worship and that Israel was forbidden to worship", "type": "ot"},
            {"ref": "Galatians 3:19", "note": "'The law was put in place through angels' -- Paul confirms the tradition that Stephen references: the Torah was mediated by angels (7:53)", "type": "nt"},
            {"ref": "Hebrews 2:2", "note": "'The message declared by angels proved to be reliable' -- another NT confirmation of angelic Torah mediation", "type": "nt"}
        ],

        "divine_council_note": "Stephen's speech (7:2-53) is the most comprehensive divine council "
                               "retelling of Israel's history in the New Testament. Three elements are "
                               "critical: (1) Israel worshiped 'the host of heaven' (7:42) -- the "
                               "celestial/spiritual powers that Deuteronomy 4:19 says were 'allotted' "
                               "to the nations as objects of worship. By adopting this astral worship, "
                               "Israel abandoned its unique covenant position and joined the nations in "
                               "their spiritual bondage. (2) The Torah was 'delivered by angels' (eis "
                               "diatagas angelon, 7:53) -- the divine council members served as mediators "
                               "of YHWH's law at Sinai. This tradition (also in Deut 33:2 LXX; Gal 3:19; "
                               "Heb 2:2) elevates the Torah's authority: it was not merely human legislation "
                               "but a decree from the heavenly assembly. Israel's violation of this "
                               "angelically delivered law is all the more serious. (3) Stephen sees 'the "
                               "heavens opened and the Son of Man standing at the right hand of God' "
                               "(7:56). This is a divine council vision: the heavens are opened (as at "
                               "Jesus' baptism), and Stephen sees into the council chamber where the Son "
                               "of Man -- the Daniel 7:13 figure -- stands at YHWH's right hand. The "
                               "Son of Man is usually described as 'seated' (Mark 14:62; Heb 1:3); "
                               "Stephen sees him 'standing' (hestota) -- perhaps rising to receive his "
                               "witness, or standing as advocate/intercessor, or standing to render "
                               "judgment. Stephen's death as a martyr echoes Jesus' death: he forgives "
                               "his killers (7:60, 'Lord, do not hold this sin against them') just as "
                               "Jesus did (Luke 23:34).",

        "sections": [
            {
                "heading": "Temple Preaching and Early Opposition (3:1 - 5:42)",
                "body": "Peter heals a lame man at the Beautiful Gate: 'In the name of Jesus Christ "
                        "of Nazareth, rise up and walk!' (3:6). His sermon declares Jesus as 'the "
                        "Author (archegos) of life' (3:15) and the prophet like Moses (3:22). The "
                        "Sanhedrin orders them not to speak in Jesus' name; Peter responds: 'We must "
                        "obey God rather than men' (5:29). 'There is salvation in no one else, for "
                        "there is no other name under heaven given among men by which we must be "
                        "saved' (4:12). The community lives in radical generosity: 'No one said that "
                        "any of the things that belonged to him was his own' (4:32). Ananias and "
                        "Sapphira lie about their gift and die -- Peter says they lied 'not to man but "
                        "to God' (5:4) and 'to the Holy Spirit' (5:3). The apostles perform signs "
                        "and wonders (5:12-16). A second arrest; an angel frees them at night (5:19). "
                        "Gamaliel counsels: 'If this plan or this undertaking is of man, it will fail; "
                        "but if it is of God, you will not be able to overthrow them' (5:38-39)."
            },
            {
                "heading": "Stephen's Speech and Martyrdom (6:1 - 7:60)",
                "body": "The church appoints seven servants, including Stephen and Philip (6:1-7). "
                        "Stephen, 'full of grace and power, was doing great wonders and signs' (6:8). "
                        "He is accused of speaking against the Temple and the law (6:13-14). His "
                        "defense (7:2-53) retells Israel's history: Abraham called to leave his country "
                        "(7:2-8), Joseph rejected by his brothers (7:9-16), Moses rejected by Israel "
                        "(7:23-29, 35-43), and the golden calf (7:39-41). The turning point: 'God "
                        "turned away and gave them over to worship the host of heaven (stratia tou "
                        "ouranou)' (7:42). He quotes Amos 5:25-27: Israel took up Moloch and Rephan "
                        "(7:43). Stephen argues that God does not dwell in houses made with hands "
                        "(7:48-50, quoting Isa 66:1-2). His accusation: 'You stiff-necked people... "
                        "you always resist the Holy Spirit. Which of the prophets did your fathers "
                        "not persecute?' (7:51-52). 'You who received the law as delivered by angels "
                        "(eis diatagas angelon) and did not keep it' (7:53). 'Full of the Holy Spirit, "
                        "he gazed into heaven and saw the glory of God, and Jesus standing at the "
                        "right hand of God' (7:55). 'Behold, I see the heavens opened, and the Son "
                        "of Man standing at the right hand of God!' (7:56). They stone him. 'Lord "
                        "Jesus, receive my spirit... Lord, do not hold this sin against them' (7:59-60). "
                        "He dies. 'And Saul approved of his execution' (8:1)."
            }
        ]
    },

    {
        "id": "acts-8-12",
        "ref": "Acts 8-12",
        "chapter_num": 3,
        "title": "Samaria, Saul's Conversion, Cornelius, and the Antioch Church",
        "era": "acts_jerusalem",
        "type": "study",
        "themes": ["NATIONS", "DC", "SPIRIT", "REVERSAL", "LAW"],

        "synopsis": "The gospel breaks out of Jerusalem. Philip preaches in Samaria (8:4-25), then "
                    "is directed by an angel to the Ethiopian eunuch (8:26-39) -- a Gentile proselyte "
                    "who reads Isaiah 53 and is baptized. Saul, the persecutor, encounters the risen "
                    "Jesus on the Damascus road: 'Saul, Saul, why are you persecuting me?' (9:4). He "
                    "is blinded, healed by Ananias, filled with the Spirit, and begins preaching that "
                    "Jesus is 'the Son of God' (9:20). Peter's vision at Joppa (10:9-16) -- the sheet "
                    "with unclean animals and the command 'What God has made clean, do not call common' "
                    "(10:15) -- demolishes the Jew-Gentile purity barrier. The Spirit falls on Cornelius' "
                    "Gentile household (10:44-48), and Peter baptizes them. The Jerusalem church is "
                    "astonished: 'Then to the Gentiles also God has granted repentance that leads to "
                    "life' (11:18). The church in Antioch becomes the base for the Gentile mission. "
                    "Herod Agrippa I kills James and imprisons Peter (12:1-5); an angel frees Peter "
                    "(12:6-19). Herod is struck dead by an angel for accepting divine worship (12:23).",

        "key_verse": {
            "ref": "Acts 10:34-35",
            "text": "So Peter opened his mouth and said: 'Truly I understand that God shows no partiality, but in every nation anyone who fears him and does what is right is acceptable to him.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "prosopolemptes (one who shows partiality / respecter of persons -- 'God shows no partiality' (10:34); YHWH's impartiality extends to ALL nations, not just Israel)",
            "en panti ethnei (in every nation -- 'in every nation anyone who fears him is acceptable' (10:35); the Deuteronomy 32 boundaries are officially transcended)",
            "koinos (common / unclean -- 'What God has made clean (ekatharisen), do not call common (koinou)' (10:15); the purity distinction between Jew and Gentile is abolished)",
            "metanoia eis zoen (repentance that leads to life -- 'to the Gentiles also God has granted repentance that leads to life' (11:18); the Gentile mission is God's initiative)",
            "angelos kyriou (angel of the Lord -- divine council members active throughout: directing Philip (8:26), freeing Peter (12:7-11), striking Herod (12:23))"
        ],

        "ane_backdrop": "The Cornelius episode (10:1-48) is the Gentile Pentecost -- the decisive "
                        "moment when the Deuteronomy 32 barrier between Israel and the nations is "
                        "officially breached by divine initiative. Cornelius is a Roman centurion -- "
                        "a Gentile military officer of the occupying power. His 'fear of God' and "
                        "generosity (10:2) make him a 'God-fearer' -- a Gentile sympathizer with "
                        "Judaism who worshiped YHWH but had not undergone full conversion (circumcision). "
                        "Peter's vision of the sheet with unclean animals (10:9-16) overturns the "
                        "Levitical food laws that had separated Israel from the nations since Sinai. "
                        "The command 'What God has made clean, do not call common' applies not only to "
                        "food but to people: 'God has shown me that I should not call any person common "
                        "or unclean' (10:28). The Spirit falling on Cornelius' household without "
                        "circumcision or Torah observance (10:44-48) is the divine council's authoritative "
                        "verdict: Gentiles are accepted as they are, by grace through faith.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 20.34-48",
                "summary": "Josephus describes the conversion of Izates, king of Adiabene, to Judaism. "
                           "A debate occurs over whether he must be circumcised: one teacher says no "
                           "(worship of God is more important), another says yes (the law requires it). "
                           "Izates eventually chooses circumcision.",
                "relevance": "Illustrates the live debate in Judaism over whether Gentile converts "
                             "needed circumcision -- the very question Acts 10-11 and 15 address. "
                             "The Spirit's falling on uncircumcised Cornelius resolves the debate "
                             "definitively for the Christian community."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 53:7-8", "note": "'Like a sheep he was led to the slaughter' -- the passage the Ethiopian eunuch is reading when Philip meets him (8:32-33)", "type": "ot"},
            {"ref": "Leviticus 11", "note": "The food laws distinguishing clean and unclean animals -- overturned in Peter's vision (10:9-16) as symbols of the Jew-Gentile distinction", "type": "ot"},
            {"ref": "Genesis 10", "note": "The Table of Nations -- the ethnic diversity of converts (Ethiopian, Samaritan, Roman centurion) represents the reversal of Babel's ethnic division", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God -- the barrier that Cornelius' conversion officially breaches", "type": "ot"},
            {"ref": "Galatians 1:11-17", "note": "Paul's own account of his conversion -- differs in some details from Acts 9, 22, and 26 but shares the core: encounter with the risen Jesus on the road", "type": "nt"},
            {"ref": "Galatians 2:11-14", "note": "Paul confronts Peter at Antioch for withdrawing from Gentile table fellowship -- the ongoing struggle with the implications of the Cornelius breakthrough", "type": "nt"}
        ],

        "divine_council_note": "Acts 8-12 narrates the systematic demolition of the Deuteronomy 32 "
                               "barriers between Israel and the nations. Each episode breaks a new "
                               "boundary: (1) Philip to the Samaritans (8:4-25) -- the mixed-race "
                               "people despised by Jews receive the gospel and the Spirit. (2) Philip "
                               "to the Ethiopian eunuch (8:26-39) -- an African Gentile proselyte, "
                               "reading Isaiah 53, is baptized and sent on his way rejoicing. (3) Saul's "
                               "conversion (9:1-19) -- the church's greatest persecutor becomes its "
                               "greatest missionary to the nations. Jesus tells Ananias: 'he is a chosen "
                               "instrument (skeuos ekloges) of mine to carry my name before the Gentiles "
                               "(ethnon) and kings and the children of Israel' (9:15). (4) Cornelius "
                               "(10:1-48) -- the definitive breakthrough: a Roman centurion's household "
                               "receives the Spirit without circumcision. Peter's declaration is the "
                               "theological turning point: 'God shows no partiality (ou prosopolemptes), "
                               "but in every nation (en panti ethnei) anyone who fears him and does what "
                               "is right is acceptable to him' (10:34-35). The phrase 'every nation' "
                               "directly echoes the 'every nation under heaven' of Pentecost (2:5). The "
                               "Babel reversal is progressing: from Jewish Jerusalem to Samaria to the "
                               "Ethiopian court to a Roman military household. Divine council members "
                               "are active agents throughout: an angel directs Philip (8:26), the Spirit "
                               "directs Peter (10:19), an angel frees Peter from prison (12:7-11), and "
                               "an angel strikes Herod dead for blasphemously accepting divine worship "
                               "(12:23). The heavenly council is actively orchestrating the reclamation "
                               "of the nations.",

        "sections": [
            {
                "heading": "Philip, the Ethiopian, and Saul's Conversion (8:1 - 9:43)",
                "body": "Persecution scatters the church from Jerusalem (8:1) -- but the scattering "
                        "becomes the means of expansion (8:4). Philip preaches in Samaria with great "
                        "response (8:5-13). Peter and John confirm the Samaritan believers with the "
                        "Spirit (8:14-17). An angel directs Philip to the Gaza road, where he meets "
                        "an Ethiopian eunuch reading Isaiah 53 (8:26-33). Philip explains: Jesus is "
                        "the suffering servant. The eunuch is baptized (8:38). Saul, 'breathing "
                        "threats and murder' (9:1), encounters Jesus on the Damascus road: a blinding "
                        "light and a voice: 'Saul, Saul, why are you persecuting me?' (9:4). 'I am "
                        "Jesus, whom you are persecuting' (9:5). Blinded three days, healed by Ananias, "
                        "filled with the Spirit (9:17), Saul 'immediately proclaimed Jesus in the "
                        "synagogues, saying, \"He is the Son of God\"' (9:20). Peter heals Aeneas "
                        "(9:32-35) and raises Tabitha/Dorcas from the dead (9:36-43)."
            },
            {
                "heading": "Cornelius, the Antioch Church, and Herod's Death (10:1 - 12:25)",
                "body": "Cornelius, a Roman centurion in Caesarea, receives an angelic vision: 'Your "
                        "prayers and your alms have ascended as a memorial before God' (10:4). Peter "
                        "receives the sheet vision: 'What God has made clean, do not call common' "
                        "(10:15). At Cornelius' house, Peter preaches: 'God shows no partiality... in "
                        "every nation anyone who fears him is acceptable' (10:34-35). 'While Peter was "
                        "still saying these things, the Holy Spirit fell on all who heard the word' "
                        "(10:44). The Jewish believers are 'amazed, because the gift of the Holy Spirit "
                        "was poured out even on the Gentiles' (10:45). Peter baptizes them (10:47-48). "
                        "In Jerusalem, Peter defends his actions: 'If then God gave the same gift to "
                        "them as he gave to us... who was I that I could stand in God's way?' (11:17). "
                        "The verdict: 'Then to the Gentiles also God has granted repentance that leads "
                        "to life' (11:18). The church in Antioch grows (11:19-26); believers are first "
                        "called 'Christians' there (11:26). Herod Agrippa I kills James, imprisons "
                        "Peter (12:1-5). An angel frees Peter at night (12:6-19). Herod, acclaimed as "
                        "a god, is struck by an angel 'because he did not give God the glory, and he "
                        "was eaten by worms and breathed his last' (12:23) -- a divine council "
                        "execution of judgment against a human who usurps divine prerogatives."
            }
        ]
    }
]
