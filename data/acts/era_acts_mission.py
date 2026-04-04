"""
era_acts_mission.py -- Acts 13-28: Paul's Mission to the Nations

The second half of Acts narrates the systematic reclamation of the Gentile
world through Paul's missionary journeys. From the Antioch church's
Spirit-directed commissioning (13:1-3), Paul and his companions carry the
gospel through Cyprus, Asia Minor, Macedonia, Greece, and finally to Rome
itself. Each journey follows a pattern: preaching in the synagogue, turning
to the Gentiles when rejected, confronting spiritual powers (Bar-Jesus,
the Python spirit, Ephesian spirits), planting churches, and enduring
persecution. The theological center is the Jerusalem Council (chapter 15),
where the apostles and elders officially declare that Gentiles need not
become Jews to be saved -- the Deuteronomy 32 reversal is ratified by the
church's leadership. Paul's journey ends in Rome, where he preaches "the
kingdom of God" and teaches about "the Lord Jesus Christ with all boldness
and without hindrance" (28:31). The gospel has reached the capital of the
world. The Babel reversal is underway.
"""

CHAPTERS = [
    {
        "id": "acts-13-14",
        "ref": "Acts 13-14",
        "chapter_num": 1,
        "title": "The First Journey -- Bar-Jesus, Pisidian Antioch, and the Turn to the Gentiles",
        "era": "acts_mission",
        "type": "study",
        "themes": ["DC", "HOLY", "TYPE", "KING", "SEED"],

        "synopsis": "The Holy Spirit initiates the Gentile mission directly: 'While they were worshiping "
                    "the Lord and fasting, the Holy Spirit said, \"Set apart for me Barnabas and Saul for "
                    "the work to which I have called them\"' (13:2). This is the divine council commissioning "
                    "Paul and Barnabas as authorized agents. They sail to Cyprus, where they encounter "
                    "Bar-Jesus (also called Elymas), a Jewish sorcerer and false prophet attached to the "
                    "Roman proconsul Sergius Paulus. Paul, 'filled with the Holy Spirit,' denounces him: "
                    "'You son of the devil (huie diabolou), you enemy of all righteousness, full of all "
                    "deceit and villainy, will you not stop making crooked the straight paths of the Lord?' "
                    "(13:10). Bar-Jesus is struck blind (13:11) -- a territorial spirit's human agent is "
                    "defeated by the Spirit's power. The proconsul believes (13:12). From here, Saul becomes "
                    "'Paul' (13:9) and takes the lead. At Pisidian Antioch, Paul delivers his first major "
                    "sermon in Acts (13:16-41), tracing Israel's history from the exodus to David, then "
                    "declaring Jesus as the fulfillment: 'Through this man forgiveness of sins is proclaimed "
                    "to you, and by him everyone who believes is freed (dikaioutai) from everything from "
                    "which you could not be freed by the law of Moses' (13:38-39). When Jews reject the "
                    "message, Paul and Barnabas make the decisive declaration: 'It was necessary that the "
                    "word of God be spoken first to you. Since you thrust it aside and judge yourselves "
                    "unworthy of eternal life, behold, we are turning to the Gentiles. For so the Lord has "
                    "commanded us, saying, \"I have made you a light for the Gentiles, that you may bring "
                    "salvation to the ends of the earth\"' (13:46-47, quoting Isaiah 49:6). They are "
                    "expelled from Pisidian Antioch, preach in Iconium, Lystra, and Derbe, then return "
                    "through the same cities, 'strengthening the souls of the disciples' and appointing "
                    "elders (14:21-23).",

        "key_verse": {
            "ref": "Acts 13:47",
            "text": "For so the Lord has commanded us, saying, 'I have made you a light for the Gentiles, that you may bring salvation to the ends of the earth.'",
            "translation": "ESV"
        },

        "original_terms": [
            "aphorisate (set apart -- 'Set apart for me Barnabas and Saul' (13:2); the same verb used of Paul's apostolic call in Gal 1:15; the Spirit commissions missionaries as the divine council commissions agents)",
            "huie diabolou (son of the devil -- Paul's denunciation of Bar-Jesus (13:10); the sorcerer is identified as an agent of the adversary, opposing God's mission)",
            "phos ethnon (light for the Gentiles -- 'I have made you a light for the Gentiles' (13:47, quoting Isa 49:6); the Servant's mission now applied to the church's Gentile mission)",
            "dikaioutai (is justified / freed -- 'by him everyone who believes is freed' (13:39); Paul's first recorded use of justification language in Acts)",
            "soteria (salvation -- 'that you may bring salvation to the ends of the earth' (13:47); salvation reaching beyond Israel to the nations; the Deut 32 reversal in action)"
        ],

        "ane_backdrop": "Bar-Jesus/Elymas represents the phenomenon of court magicians and sorcerers "
                        "common in the ancient Mediterranean world. Roman officials often kept such "
                        "figures as advisors -- Pliny the Elder describes the prevalence of magical "
                        "practitioners in Roman society (Natural History 30.1-2). The confrontation "
                        "between Paul and Bar-Jesus echoes the OT pattern of prophetic contest: Moses "
                        "vs. Pharaoh's magicians (Exod 7:8-13), Elijah vs. the prophets of Baal "
                        "(1 Kings 18:20-40). In each case, YHWH's representative defeats the agents of "
                        "false spiritual powers. The title 'son of the devil' places Bar-Jesus in the "
                        "lineage of the adversary -- he is a human instrument of the hostile powers that "
                        "govern the nations under the Deuteronomy 32 arrangement. Paul's sermon at "
                        "Pisidian Antioch (13:16-41) follows the pattern of Hellenistic synagogue "
                        "homilies, recounting Israel's history and applying it to the present situation, "
                        "similar to Stephen's speech but with a different conclusion: not judgment on "
                        "Israel but the offer of forgiveness extended to all who believe.",

        "second_temple": [
            {
                "source": "Testament of Solomon (1st-3rd century AD)",
                "summary": "This pseudepigraphic text portrays Solomon commanding demons by the "
                           "authority of God's name, using a magical ring. It reflects widespread "
                           "Jewish belief in the power of divine names over demonic forces.",
                "relevance": "Provides context for the Jewish magical tradition that Bar-Jesus "
                             "represents and that Paul confronts. The difference: Paul uses the name "
                             "of Jesus not as a magical formula but as the delegated authority of the "
                             "risen Lord."
            },
            {
                "source": "Isaiah 49:6 (Servant Song)",
                "summary": "'I will make you as a light for the nations, that my salvation may reach "
                           "to the end of the earth.' Originally addressed to the Servant of YHWH.",
                "relevance": "Paul quotes this as his commission (13:47), applying the Servant's "
                             "mission to the apostolic ministry. The church inherits the Servant's "
                             "mandate to bring light to the disinherited nations."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 49:6", "note": "'A light for the nations' -- Paul quotes this as the scriptural basis for turning to the Gentiles (13:47)", "type": "ot"},
            {"ref": "Psalm 2:7", "note": "'You are my Son; today I have begotten you' -- quoted by Paul (13:33) as fulfilled in the resurrection; the divine council enthronement psalm", "type": "ot"},
            {"ref": "Psalm 16:10", "note": "'You will not let your Holy One see corruption' -- quoted by Paul (13:35) as fulfilled in Jesus, not David", "type": "ot"},
            {"ref": "Habakkuk 1:5", "note": "'Look, you scoffers, be astounded and perish' -- Paul's warning to those who reject the message (13:41)", "type": "ot"},
            {"ref": "Isaiah 55:3", "note": "'I will give you the holy and sure blessings of David' -- quoted by Paul (13:34) linking the resurrection to the Davidic covenant promises", "type": "ot"},
            {"ref": "Exodus 7:8-13", "note": "Moses vs. Pharaoh's magicians -- the prophetic contest pattern that Paul vs. Bar-Jesus follows", "type": "ot"},
            {"ref": "Galatians 1:15", "note": "'He who had set me apart (aphorisas) before I was born' -- Paul uses the same verb the Spirit uses in Acts 13:2", "type": "nt"}
        ],

        "divine_council_note": "The first missionary journey opens with the most explicit divine council "
                               "commissioning in Acts: 'The Holy Spirit said, \"Set apart for me Barnabas "
                               "and Saul for the work to which I have called them\"' (13:2). The Spirit "
                               "speaks directly, issuing orders as the divine council's executive agent. "
                               "The verb 'set apart' (aphorisate) is the same word Paul uses for his own "
                               "calling in Galatians 1:15 -- he was 'set apart before I was born,' "
                               "appointed by the council before his existence. The Bar-Jesus confrontation "
                               "(13:6-12) is the first direct spiritual warfare encounter of Paul's "
                               "missions. Bar-Jesus is a 'Jewish false prophet' (13:6) -- a member of "
                               "YHWH's covenant people who serves the adversary. Paul identifies him: "
                               "'son of the devil, enemy of all righteousness' (13:10). The conflict "
                               "is cosmic: the Spirit in Paul opposes the devil in Bar-Jesus. The "
                               "territorial spirit operating through this sorcerer is defeated, and the "
                               "Roman proconsul -- a representative of the Gentile imperial power -- "
                               "believes (13:12). The turn to the Gentiles at Pisidian Antioch (13:46-47) "
                               "is the programmatic moment for Paul's mission. Quoting Isaiah 49:6, he "
                               "applies the Servant's mandate to himself: 'I have made you a light for "
                               "the Gentiles, that you may bring salvation to the ends of the earth.' "
                               "The Servant's mission was always the reversal of Deuteronomy 32 -- light "
                               "penetrating the darkness of the disinherited nations. Paul's ministry is "
                               "the fulfillment of this cosmic program.",

        "sections": [
            {
                "heading": "The Spirit's Commission and the Bar-Jesus Confrontation (13:1-12)",
                "body": "At Antioch, the church's prophets and teachers worship and fast. 'The Holy "
                        "Spirit said, \"Set apart (aphorisate) for me Barnabas and Saul for the work "
                        "to which I have called them\"' (13:2). After fasting and prayer, they lay "
                        "hands on them and send them off (13:3) -- 'sent out by the Holy Spirit' (13:4). "
                        "They sail to Cyprus. At Paphos, they find Bar-Jesus (Elymas), 'a Jewish "
                        "false prophet' attached to the proconsul Sergius Paulus (13:6-7). When Bar-Jesus "
                        "opposes them, 'trying to turn the proconsul away from the faith' (13:8), Paul, "
                        "'filled with the Holy Spirit, looked intently at him and said, \"You son of the "
                        "devil, you enemy of all righteousness, full of all deceit and villainy, will "
                        "you not stop making crooked the straight paths of the Lord?\"' (13:9-10). "
                        "Elymas is struck blind 'for a time' (13:11). The proconsul believes, 'astonished "
                        "at the teaching of the Lord' (13:12). The pattern is set for Paul's missions: "
                        "spiritual opposition, Spirit-powered confrontation, and advance of the gospel."
            },
            {
                "heading": "Pisidian Antioch, the Turn to the Gentiles, and the First Journey (13:13 - 14:28)",
                "body": "Paul and Barnabas travel to Pisidian Antioch. In the synagogue on the Sabbath, "
                        "Paul delivers his first major sermon (13:16-41). He traces Israel's history: "
                        "'The God of this people Israel chose our fathers and made the people great "
                        "during their stay in the land of Egypt' (13:17). From the exodus through the "
                        "judges to David, God raised up Jesus as Savior (13:23). Paul argues that the "
                        "crucifixion was carried out 'by those who did not recognize him nor understand "
                        "the utterances of the prophets' (13:27). The resurrection fulfills Psalm 2:7 "
                        "('You are my Son; today I have begotten you,' 13:33), Isaiah 55:3 ('the holy "
                        "and sure blessings of David,' 13:34), and Psalm 16:10 ('You will not let your "
                        "Holy One see corruption,' 13:35). 'Through this man forgiveness of sins is "
                        "proclaimed to you' (13:38). When Jewish opposition intensifies, Paul makes the "
                        "decisive turn: 'Since you thrust it aside... behold, we are turning to the "
                        "Gentiles' (13:46), quoting Isaiah 49:6. They preach in Iconium (14:1-7). At "
                        "Lystra, Paul heals a crippled man (14:8-10), and the crowds try to worship "
                        "them as gods -- 'Barnabas they called Zeus, and Paul, Hermes' (14:12). Paul "
                        "protests: 'We bring you good news, that you should turn from these vain things "
                        "(mataion) to a living God' (14:15). The 'vain things' are the gods of the "
                        "nations -- the lesser elohim. They return through the cities, appointing "
                        "elders (14:23), and report back to Antioch: 'God had opened a door of faith "
                        "to the Gentiles' (14:27)."
            },
            {
                "heading": "Name Theology: Saul to Paul — The Identity Shift for a Gentile Mission",
                "body": "Acts 13:9 marks one of the most significant name transitions in Scripture: 'But "
                        "Saul, who was also called Paul (Saulos de, ho kai Paulos), filled with the Holy "
                        "Spirit, looked intently at him.' From this point forward, Luke never again calls "
                        "him 'Saul' in the narrative. The birth name Saul (Šāʾûl, שָׁאוּל) means 'asked "
                        "for' — the same name as Israel's first king, the tallest man in the nation "
                        "(1 Samuel 9:2), the Benjaminite tribal hero. Paul (Paulos, from Latin paulus) "
                        "means 'small' or 'humble.' The shift occurs at the precise moment Paul confronts "
                        "Bar-Jesus and converts the Roman proconsul Sergius Paulus — a man who shares his "
                        "new name. Luke's literary timing is deliberate: the Pharisaic zealot named after "
                        "Israel's first king becomes the humble apostle to the nations. Paul likely always "
                        "carried both names (Jewish + Roman citizen), but Luke's narrative shift from 'Saul' "
                        "to 'Paul' marks an identity transformation: from persecutor to preacher, from "
                        "synagogue authority to Gentile missionary. Paul himself embraces the smallness his "
                        "name implies: 'I am the least (elachistos) of the apostles' (1 Corinthians 15:9). "
                        "The pattern echoes the OT: God takes the one 'asked for' by human ambition and "
                        "transforms him into something small enough to be used — the same reversal of "
                        "Abram→Abraham (exalted father → father of multitudes) and Jacob→Israel (supplanter "
                        "→ one who strives with God). The name itself becomes a theological confession: "
                        "power is made perfect in weakness (2 Corinthians 12:9)."
            }
        ]
    },

    {
        "id": "acts-15",
        "ref": "Acts 15",
        "chapter_num": 2,
        "title": "The Jerusalem Council -- The Deuteronomy 32 Reversal Ratified",
        "era": "acts_mission",
        "type": "study",
        "themes": ["DC", "SEED", "NATIONS", "KING", "LAW"],

        "synopsis": "The Jerusalem Council (Acts 15) is the most theologically decisive moment in Acts "
                    "and one of the most important events in early church history. The question: 'Unless "
                    "you are circumcised according to the custom of Moses, you cannot be saved' (15:1). "
                    "Must Gentiles become Jews to be saved? Paul, Barnabas, Peter, and James all testify. "
                    "Peter recalls the Cornelius event: 'God, who knows the heart, bore witness to them, "
                    "by giving them the Holy Spirit just as he did to us, and he made no distinction "
                    "between us and them, having cleansed their hearts by faith' (15:8-9). James renders "
                    "the verdict, quoting Amos 9:11-12: 'After this I will return, and I will rebuild "
                    "the tent of David that has fallen... that the remnant of mankind may seek the Lord, "
                    "and all the Gentiles who are called by my name' (15:16-17). The James quotation is "
                    "stunning in its implications: the 'tent of David' is not the physical Temple but "
                    "the Davidic dynasty restored in Jesus, and its purpose is that 'all the Gentiles' "
                    "-- the disinherited nations of Deuteronomy 32 -- 'may seek the Lord.' The council "
                    "issues its decree: Gentiles need not be circumcised or keep the Mosaic law. They "
                    "should abstain from 'things polluted by idols, from sexual immorality, from what "
                    "has been strangled, and from blood' (15:20) -- requirements that likely correspond "
                    "to the Noahide laws for Gentiles living among Jews. The letter declares: 'It has "
                    "seemed good to the Holy Spirit and to us' (15:28) -- the council's decision is "
                    "ratified by the divine council itself.",

        "key_verse": {
            "ref": "Acts 15:16-17",
            "text": "'After this I will return, and I will rebuild the tent of David that has fallen; I will rebuild its ruins, and I will restore it, that the remnant of mankind may seek the Lord, and all the Gentiles who are called by my name, says the Lord, who makes these things known from of old.'",
            "translation": "ESV"
        },

        "original_terms": [
            "skene Dauid (tent/tabernacle of David -- Amos 9:11 LXX; the fallen Davidic dynasty rebuilt in Jesus; NOT the Temple but the messianic kingdom)",
            "ta ethne (the Gentiles / the nations -- 'all the Gentiles who are called by my name' (15:17); the disinherited nations of Deut 32 now claimed by YHWH)",
            "to pneumati to hagio kai hemin (to the Holy Spirit and to us -- 'it seemed good to the Holy Spirit and to us' (15:28); the council's human decision ratified by the divine Spirit; the earthly assembly aligned with the heavenly)",
            "kardiognostes (heart-knower -- 'God, who knows the heart (kardiognostes), bore witness' (15:8); a divine attribute applied to God's acceptance of Gentile faith)",
            "alisgematon ton eidolon (pollutions of idols -- the Jerusalem decree's dietary restriction (15:20); abstaining from idol-meat as a separation from the worship of false elohim)"
        ],

        "ane_backdrop": "The Jerusalem Council addresses the central question of how Gentiles relate to "
                        "Israel's covenant. In the ancient world, joining a people meant adopting their "
                        "gods, laws, and customs -- for Gentiles converting to Judaism, this meant "
                        "circumcision, Torah observance, and separation from pagan worship. The council's "
                        "decision that Gentiles could be saved without becoming Jews was revolutionary: "
                        "it recognized that the gospel creates a new category -- Gentile believers who "
                        "belong to YHWH without belonging to ethnic Israel. James' quotation of Amos "
                        "9:11-12 is especially significant because the LXX version he quotes differs from "
                        "the Hebrew MT. The Hebrew reads 'that they may possess the remnant of Edom'; the "
                        "LXX reads 'that the remnant of mankind may seek the Lord.' James uses the LXX "
                        "because it supports the theological point: the restored Davidic kingdom includes "
                        "the nations who seek YHWH. The four prohibitions of the decree (15:20, 29) may "
                        "reflect the Noahide commandments -- universal moral laws binding on all humanity "
                        "(cf. Genesis 9:1-7) -- or Leviticus 17-18's rules for Gentile residents in "
                        "Israel's land. Either way, they represent the minimum requirements for Gentile "
                        "table fellowship with Jewish believers.",

        "second_temple": [
            {
                "source": "Amos 9:11-12 (LXX vs. MT)",
                "summary": "The Hebrew (MT) reads: 'that they may possess the remnant of Edom and all "
                           "the nations who are called by my name.' The LXX reads: 'that the remnant "
                           "of mankind (anthropoi) may seek the Lord, and all the nations (ethne) who "
                           "are called by my name.' The LXX's 'Adam' (mankind) replaces 'Edom' due to "
                           "consonantal similarity (aleph-dalet-mem in both).",
                "relevance": "James quotes the LXX version precisely because it universalizes the "
                             "promise: not just 'Edom' (one nation) but 'mankind' (all nations) will "
                             "seek the Lord. The textual variant becomes the scriptural basis for the "
                             "Gentile mission."
            },
            {
                "source": "Jubilees 7:20-28 (Noahide Commandments)",
                "summary": "Jubilees records Noah commanding his sons to observe justice, cover the "
                           "shame of their flesh, bless their creator, honor parents, love their "
                           "neighbors, and guard against fornication, uncleanness, and iniquity.",
                "relevance": "The four prohibitions of the Jerusalem decree (15:20) may reflect this "
                             "Noahide tradition -- universal commandments for all humanity, not just "
                             "Israel, providing a framework for Gentile inclusion without full Torah "
                             "observance."
            }
        ],

        "cross_refs": [
            {"ref": "Amos 9:11-12", "note": "'I will rebuild the booth of David that is fallen' -- quoted by James (15:16-17) as the prophetic basis for Gentile inclusion in the messianic kingdom", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The allotment of nations to the sons of God -- the theological background that the Jerusalem Council is reversing: the nations are now claimed by YHWH through Christ", "type": "ot"},
            {"ref": "Genesis 9:1-7", "note": "The Noahide covenant -- the possible background to the four prohibitions of the Jerusalem decree (15:20)", "type": "ot"},
            {"ref": "Leviticus 17-18", "note": "Rules for 'strangers who sojourn among you' -- the Levitical background to the decree's restrictions on idol-food, blood, strangled animals, and sexual immorality", "type": "ot"},
            {"ref": "Galatians 2:1-10", "note": "Paul's account of the Jerusalem meeting -- broadly parallel to Acts 15 but with different emphases and possibly different timing", "type": "nt"},
            {"ref": "Romans 14:1-15:13", "note": "The 'strong and weak' discussion -- the practical application of the Jerusalem Council's principles in a mixed Jewish-Gentile community", "type": "nt"}
        ],

        "divine_council_note": "The Jerusalem Council is the human ratification of what the divine council "
                               "has already decreed. Three theological moves make this clear: (1) Peter "
                               "testifies that 'God, who knows the heart (kardiognostes), bore witness "
                               "to them by giving them the Holy Spirit just as he did to us, and he made "
                               "no distinction between us and them' (15:8-9). God himself has already "
                               "decided: the Gentiles are accepted. (2) James quotes Amos 9:11-12 to show "
                               "that this was always the plan: the rebuilt 'tent of David' (the messianic "
                               "kingdom) exists precisely 'that the remnant of mankind may seek the Lord, "
                               "and all the Gentiles who are called by my name' (15:17). The Deuteronomy 32 "
                               "disinheritance of the nations was always temporary -- the prophets foresaw "
                               "its reversal. (3) The decree itself is issued with the formula 'it seemed "
                               "good to the Holy Spirit and to us' (15:28). This extraordinary phrase "
                               "claims that the earthly assembly's decision aligns with the heavenly "
                               "council's will. The Spirit -- the agent of the risen Christ, operating as "
                               "the divine council's executive -- endorses the decision. The four "
                               "prohibitions (idol-food, blood, strangled animals, sexual immorality) are "
                               "not Torah-lite but the baseline requirements for Gentiles leaving the "
                               "worship of the lesser elohim: stop eating food offered to false gods, stop "
                               "participating in their cult practices (blood rituals, temple prostitution). "
                               "The council has spoken: the nations are YHWH's, and they may come as they "
                               "are -- without circumcision, without Torah observance -- through faith in "
                               "Jesus the Messiah.",

        "sections": [
            {
                "heading": "The Circumcision Debate and the Council's Deliberation (15:1-21)",
                "body": "Men from Judea come to Antioch teaching: 'Unless you are circumcised according "
                        "to the custom of Moses, you cannot be saved' (15:1). Paul and Barnabas debate "
                        "them sharply (15:2). The church sends them to Jerusalem to consult the apostles "
                        "and elders. Some believing Pharisees insist: 'It is necessary to circumcise "
                        "them and to order them to keep the law of Moses' (15:5). Peter speaks first: "
                        "'Brothers, you know that in the early days God made a choice among you, that "
                        "by my mouth the Gentiles should hear the word of the gospel and believe' (15:7). "
                        "He recalls Cornelius: God 'made no distinction between us and them, having "
                        "cleansed their hearts by faith' (15:9). 'We believe that we will be saved "
                        "through the grace of the Lord Jesus, just as they will' (15:11) -- note the "
                        "reversal: not 'they are saved like us' but 'we are saved like them' -- by "
                        "grace alone. Paul and Barnabas recount 'signs and wonders God had done through "
                        "them among the Gentiles' (15:12). James delivers the verdict, quoting Amos "
                        "9:11-12: the rebuilt tent of David includes the nations. His judgment: 'We "
                        "should not trouble those of the Gentiles who turn to God' (15:19). The "
                        "requirements: abstain from idol pollution, sexual immorality, strangled animals, "
                        "and blood (15:20)."
            },
            {
                "heading": "The Apostolic Letter and Its Aftermath (15:22-41)",
                "body": "The council sends a letter with Judas Barsabbas and Silas: 'Since we have heard "
                        "that some persons have gone out from us and troubled you with words, unsettling "
                        "your minds, although we gave them no instructions...' (15:24). The key phrase: "
                        "'For it has seemed good to the Holy Spirit and to us to lay on you no greater "
                        "burden than these requirements' (15:28). The letter is received in Antioch with "
                        "rejoicing (15:31). Paul and Barnabas part ways over John Mark (15:36-41) -- "
                        "Barnabas takes Mark to Cyprus; Paul chooses Silas and heads through Syria and "
                        "Cilicia, 'strengthening the churches' (15:41). The council's decision is the "
                        "theological foundation for all subsequent Gentile mission: the nations can come "
                        "to YHWH without becoming Jews. The Deuteronomy 32 reversal does not require "
                        "the nations to join Israel ethnically; it requires them to turn from the lesser "
                        "elohim to the living God through faith in Jesus Christ."
            }
        ]
    },

    {
        "id": "acts-16-17",
        "ref": "Acts 16-17",
        "chapter_num": 3,
        "title": "Philippi, Thessalonica, and Athens -- The Python Spirit and the Unknown God",
        "era": "acts_mission",
        "type": "study",
        "themes": ["NATIONS", "KING", "DC", "RIV", "SEED"],

        "synopsis": "Paul's second journey brings the gospel to Europe. The Spirit directs the mission "
                    "through a vision: 'A man of Macedonia was standing there, urging him and saying, "
                    "\"Come over to Macedonia and help us\"' (16:9). In Philippi, Paul encounters a slave "
                    "girl with 'a spirit of divination' -- literally 'a Python spirit' (pneuma pythona, "
                    "16:16). This spirit, associated with the oracle at Delphi, represents the territorial "
                    "spiritual authority of the Greek world. The girl follows Paul crying, 'These men are "
                    "servants of the Most High God, who proclaim to you the way of salvation' (16:17). "
                    "Paul casts out the spirit 'in the name of Jesus Christ' (16:18). The exorcism triggers "
                    "a chain of events: the slave owners lose their profit, Paul and Silas are beaten and "
                    "imprisoned, an earthquake strikes at midnight while they sing hymns, the jailer asks "
                    "'What must I do to be saved?' (16:30), and Paul responds: 'Believe in the Lord Jesus, "
                    "and you will be saved, you and your household' (16:31). The jailer's household is "
                    "baptized. In Thessalonica, Jews accuse Paul of 'acting against the decrees of Caesar, "
                    "saying that there is another king, Jesus' (17:7). In Athens, Paul encounters Greek "
                    "philosophy at the Areopagus and delivers his most culturally adapted speech: 'The God "
                    "who made the world and everything in it, being Lord of heaven and earth, does not live "
                    "in temples made by man' (17:24). He declares that God 'made from one man every nation "
                    "of mankind to live on all the face of the earth, having determined allotted periods "
                    "and the boundaries of their dwelling place' (17:26) -- a direct echo of Deuteronomy "
                    "32:8. 'The times of ignorance God overlooked, but now he commands all people everywhere "
                    "to repent' (17:30).",

        "key_verse": {
            "ref": "Acts 17:26-27",
            "text": "And he made from one man every nation of mankind to live on all the face of the earth, having determined allotted periods and the boundaries of their dwelling place, that they should seek God, and perhaps feel their way toward him and find him. Yet he is actually not far from each one of us.",
            "translation": "ESV"
        },

        "original_terms": [
            "pneuma pythona (Python spirit -- literally a spirit associated with the Delphic oracle; the territorial spiritual authority of Greek paganism; Paul casts it out in Jesus' name (16:16-18))",
            "theou hypsistou (of the Most High God -- the Python spirit's testimony: 'servants of the Most High God' (16:17); the divine council title (cf. Deut 32:8, 'When the Most High gave the nations their inheritance'); even hostile spirits recognize the supreme God)",
            "prostetagmenous kairous (allotted periods/appointed times -- 'having determined allotted periods' (17:26); the same concept as Deut 32:8's allotment; God assigned the nations their historical epochs)",
            "horothesias tes katoikias (boundaries of their dwelling place -- 'the boundaries of their dwelling place' (17:26); echoing Deut 32:8 LXX: God 'fixed the boundaries of the peoples')",
            "agnostos theos (unknown god -- 'to the unknown god' (17:23); the altar Paul references; the true God was 'unknown' to the Athenians because they worshiped the territorial elohim instead)"
        ],

        "ane_backdrop": "The Python spirit (pneuma pythona, 16:16) represents one of the most powerful "
                        "territorial spiritual authorities in the ancient world. The oracle at Delphi was "
                        "the most prestigious religious institution in the Greek world for over a thousand "
                        "years. The Pythia (priestess) sat over a chasm, inhaled vapors, and delivered "
                        "prophecies attributed to Apollo. Generals, kings, and cities consulted the oracle "
                        "before major decisions. The mythological background: Apollo slew the great Python "
                        "(serpent-dragon) that guarded Delphi and established his oracle on the site. A "
                        "person described as having a 'Python spirit' was a ventriloquist or oracle-speaker "
                        "who channeled this particular spiritual power. Paul's casting out of this spirit "
                        "is not merely an exorcism but a confrontation with a major territorial authority. "
                        "At Athens, Paul's Areopagus speech engages Greek philosophical categories while "
                        "maintaining the biblical worldview. He quotes the Cretan poet Epimenides ('In him "
                        "we live and move and have our being,' 17:28a) and the Cilician poet Aratus ('For "
                        "we are indeed his offspring,' 17:28b) -- using pagan poets to argue for the "
                        "biblical God. The 'unknown god' (agnostos theos) altar was a real phenomenon "
                        "in Athens, attested by Pausanias (Description of Greece 1.1.4) and Diogenes "
                        "Laertius (Lives of the Philosophers 1.110).",

        "second_temple": [
            {
                "source": "Plutarch, On the Obsolescence of Oracles (1st century AD)",
                "summary": "Plutarch discusses the decline of oracular sites and attributes it to "
                           "the departure of the 'daimones' (spiritual beings) who powered them. "
                           "He describes the Python spirit as a 'pneuma' that inspired the Pythia.",
                "relevance": "Provides contemporary pagan testimony about the Python spirit that "
                             "Paul confronts. Even Greek philosophers acknowledged that oracles "
                             "were powered by spiritual beings -- Paul identifies these beings as "
                             "hostile spirits opposed to the true God."
            },
            {
                "source": "Aristobulus and Pseudo-Aristeas (2nd century BC)",
                "summary": "Jewish philosophers in Alexandria argued that Greek poets and "
                           "philosophers had borrowed from Moses and the prophets, making Greek "
                           "wisdom derivative of Hebrew revelation.",
                "relevance": "Paul's quotation of Greek poets at the Areopagus follows this "
                             "Hellenistic Jewish tradition of finding common ground between Greek "
                             "philosophy and biblical theology."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9", "note": "'When the Most High gave to the nations their inheritance, when he divided mankind, he fixed the borders of the peoples' -- the direct background to Paul's speech at Athens (17:26)", "type": "ot"},
            {"ref": "Psalm 82", "note": "The judgment of the gods -- the 'unknown god' of Athens is YHWH, unknown because the nations worship the lesser elohim instead", "type": "ot"},
            {"ref": "Genesis 11:1-9", "note": "Babel: the nations scattered and allotted -- Paul's Athens speech describes the aftermath: God 'determined allotted periods and the boundaries of their dwelling place' (17:26)", "type": "ot"},
            {"ref": "Isaiah 40:18-20", "note": "'To whom then will you liken God?' -- the idol polemic that Paul echoes: 'we ought not to think that the divine being is like gold or silver or stone, an image formed by the art and imagination of man' (17:29)", "type": "ot"},
            {"ref": "1 Thessalonians 1:9-10", "note": "'You turned to God from idols to serve the living and true God' -- Paul's letter confirms the Thessalonian conversion from idol-worship described in Acts 17:1-9", "type": "nt"},
            {"ref": "Philippians 1:1-2", "note": "Paul's letter to the Philippian church he founded after the Python spirit encounter and the jailer's conversion (16:12-40)", "type": "nt"}
        ],

        "divine_council_note": "Acts 16-17 contains two of the most explicit divine council encounters in "
                               "the New Testament. (1) The Python spirit at Philippi (16:16-18): The slave "
                               "girl has a 'pneuma pythona' -- a spirit connected to the Delphic oracle, "
                               "the most authoritative religious institution in the Greek world. The Python "
                               "was the serpent-dragon of Delphi, and in the divine council framework, this "
                               "is a territorial spirit: a spiritual power claiming jurisdiction over Greek "
                               "religious life. The spirit's testimony is technically accurate -- 'These men "
                               "are servants of the Most High God (theou hypsistou)' (16:17) -- but Paul "
                               "recognizes the source and rejects its endorsement. He commands it to leave "
                               "'in the name of Jesus Christ' (16:18), asserting the authority of the "
                               "enthroned Son over the territorial power. The result: the gospel advances "
                               "into Europe, a Gentile jailer's household is saved, and the Philippian "
                               "church -- Paul's most beloved -- is established on the rubble of a defeated "
                               "territorial spirit. (2) Paul's Areopagus speech (17:22-31): Paul directly "
                               "invokes the Deuteronomy 32 worldview when he says God 'determined allotted "
                               "periods (prostetagmenous kairous) and the boundaries of their dwelling "
                               "place (horothesias)' (17:26). This echoes Deuteronomy 32:8: 'He fixed the "
                               "boundaries (horia) of the peoples according to the number of the sons of "
                               "God.' Paul tells the Athenians that their national existence, their "
                               "geography, and their history were all determined by the one true God -- "
                               "not by the gods they worship. The 'times of ignorance' (17:30) are the "
                               "Deuteronomy 32 era: the period when the nations were under the governance "
                               "of lesser elohim. That era is now over: 'he commands all people everywhere "
                               "to repent' (17:30). The risen Jesus is the appointed judge of the world "
                               "(17:31), and all nations must now answer to him directly.",

        "sections": [
            {
                "heading": "The Python Spirit, the Jailer, and the Gospel in Europe (16:1-40)",
                "body": "Paul recruits Timothy (16:1-3). The Spirit forbids preaching in Asia and "
                        "Bithynia (16:6-7) -- 'the Spirit of Jesus did not allow them' (16:7). The "
                        "Macedonian vision: 'Come over to Macedonia and help us' (16:9). In Philippi, "
                        "Lydia, a 'worshiper of God' and seller of purple cloth, believes and is "
                        "baptized with her household (16:14-15). A slave girl with 'a Python spirit' "
                        "(pneuma pythona) follows them for many days crying, 'These men are servants "
                        "of the Most High God (theou hypsistou), who proclaim to you the way of "
                        "salvation (hodon soterias)' (16:17). 'Paul, having become greatly annoyed, "
                        "turned and said to the spirit, \"I command you in the name of Jesus Christ "
                        "to come out of her.\" And it came out that very hour' (16:18). The slave "
                        "owners drag Paul and Silas before the magistrates (16:19-21). They are beaten "
                        "and imprisoned. 'About midnight Paul and Silas were praying and singing hymns "
                        "to God' (16:25). An earthquake opens the prison doors (16:26). The jailer, "
                        "about to kill himself, is stopped: 'Do yourself no harm, for we are all here' "
                        "(16:28). 'What must I do to be saved?' (16:30). 'Believe in the Lord Jesus, "
                        "and you will be saved, you and your household' (16:31). The household is "
                        "baptized and rejoices (16:33-34). Paul asserts his Roman citizenship (16:37-39)."
            },
            {
                "heading": "Thessalonica, Berea, and the Areopagus at Athens (17:1-34)",
                "body": "In Thessalonica, Paul reasons from the Scriptures: 'This Jesus, whom I "
                        "proclaim to you, is the Christ' (17:3). Some Jews and 'a great many of the "
                        "devout Greeks' believe (17:4). Opponents accuse: 'These men who have turned "
                        "the world upside down have come here also... they are all acting against the "
                        "decrees of Caesar, saying that there is another king, Jesus' (17:6-7). The "
                        "charge is truer than the accusers know: Jesus IS another king -- the King of "
                        "kings, whose kingdom supersedes Caesar's. In Berea, the Jews are 'more noble' "
                        "-- 'examining the Scriptures daily to see if these things were so' (17:11). "
                        "In Athens, Paul is 'provoked' (paroxyneto) by the city 'full of idols' (17:16). "
                        "At the Areopagus, he begins: 'Men of Athens, I perceive that in every way you "
                        "are very religious (deisidaimonesterous)' (17:22). He references 'an altar with "
                        "this inscription: \"To the unknown god.\" What therefore you worship as unknown, "
                        "this I proclaim to you' (17:23). God 'does not live in temples made by man' "
                        "(17:24). He 'made from one man every nation of mankind... having determined "
                        "allotted periods and the boundaries of their dwelling place, that they should "
                        "seek God' (17:26-27). He quotes pagan poets: 'In him we live and move and have "
                        "our being... For we are indeed his offspring' (17:28). 'The times of ignorance "
                        "God overlooked, but now he commands all people everywhere to repent, because he "
                        "has fixed a day on which he will judge the world in righteousness by a man whom "
                        "he has appointed, and of this he has given assurance to all by raising him from "
                        "the dead' (17:30-31). Some mock; Dionysius and Damaris believe (17:34)."
            }
        ]
    },

    {
        "id": "acts-18-20",
        "ref": "Acts 18-20",
        "chapter_num": 4,
        "title": "Corinth, Ephesus, and the Burning of the Books -- The Powers Stripped",
        "era": "acts_mission",
        "type": "study",
        "themes": ["DC", "KING", "NAME", "HOLY", "SPIRIT"],

        "synopsis": "Paul establishes the church in Corinth (18:1-17), where he meets Aquila and Priscilla, "
                    "expelled from Rome by Claudius' edict (18:2). The Lord speaks to Paul in a vision: 'Do "
                    "not be afraid, but go on speaking and do not be silent, for I am with you... for I have "
                    "many in this city who are my people' (18:9-10). When Jews bring Paul before the proconsul "
                    "Gallio, Gallio dismisses the charges: 'I refuse to be a judge of these things' (18:15) -- "
                    "Roman law protects the gospel's advance. Paul returns briefly to Jerusalem and Antioch "
                    "(18:22) before beginning his third journey, focused on Ephesus. At Ephesus, Paul "
                    "encounters twelve disciples of John the Baptist who have not heard of the Holy Spirit "
                    "(19:1-7) -- they are baptized in Jesus' name and the Spirit comes upon them. Paul "
                    "teaches daily in the hall of Tyrannus for two years, 'so that all the residents of Asia "
                    "heard the word of the Lord, both Jews and Greeks' (19:10). 'God was doing extraordinary "
                    "miracles by the hands of Paul' (19:11). Then the sons of Sceva incident: seven Jewish "
                    "exorcists try to use Jesus' name without authorization. The evil spirit replies: 'Jesus "
                    "I know, and Paul I recognize, but who are you?' (19:15). The demon overpowers them "
                    "(19:16). The result: 'Fear fell upon them all, and the name of the Lord Jesus was "
                    "extolled' (19:17). Converts bring their magic books and burn them publicly -- '50,000 "
                    "pieces of silver' worth (19:19). 'So the word of the Lord continued to increase and "
                    "prevail mightily (kata kratos)' (19:20). Demetrius the silversmith incites a riot "
                    "because the gospel threatens the Artemis cult (19:23-41). Paul gives his farewell "
                    "address to the Ephesian elders at Miletus (20:17-38).",

        "key_verse": {
            "ref": "Acts 19:15-17",
            "text": "But the evil spirit answered them, 'Jesus I know, and Paul I recognize, but who are you?' And the man in whom was the evil spirit leaped on them, mastered all of them and overpowered them, so that they fled out of that house naked and wounded. And this became known to all the residents of Ephesus, both Jews and Greeks. And fear fell upon them all, and the name of the Lord Jesus was extolled.",
            "translation": "ESV"
        },

        "original_terms": [
            "ton Iesoun ginosko kai ton Paulon epistamai (Jesus I know and Paul I recognize -- the demon's response (19:15); two different verbs: ginosko (know by experience/relationship) for Jesus, epistamai (recognize/be acquainted with) for Paul; the demon recognizes the authority hierarchy)",
            "periergos (magic / curious arts -- 'those who practiced magic arts (ta perierga)' (19:19); the technical term for occult practices; the Ephesian magical tradition was famous throughout the ancient world)",
            "Ephesia grammata (Ephesian letters -- the famous magical texts of Ephesus; burning them (19:19) represents a complete break with the territorial spiritual powers)",
            "kata kratos (with might / prevailing power -- 'the word of the Lord continued to increase and prevail mightily' (19:20); the gospel overcomes the strongest spiritual opposition)",
            "Artemis (Diana -- the Ephesian goddess whose temple was one of the Seven Wonders; Demetrius' riot shows the economic and spiritual infrastructure of idol-worship (19:24-27))"
        ],

        "ane_backdrop": "Ephesus was one of the greatest centers of magical practice in the ancient world. "
                        "The 'Ephesian letters' (Ephesia grammata) were famous magical incantations known "
                        "throughout the Mediterranean -- Plutarch, Clement of Alexandria, and others attest "
                        "to their fame. The city was dominated by the cult of Artemis (Diana), whose temple "
                        "was one of the Seven Wonders of the Ancient World. Artemis of Ephesus was not the "
                        "Greek goddess of the hunt but an ancient Anatolian fertility deity, depicted with "
                        "multiple breasts or eggs, associated with cosmic creative power. The silversmith "
                        "riot (19:23-41) reveals the economic dimension of idolatry: the entire economy of "
                        "Ephesus depended on Artemis worship -- silver shrines, tourism, temple banking. "
                        "Paul's gospel threatened not just a religious system but a spiritual-economic "
                        "complex. The sons of Sceva (19:13-17) illustrate the widespread Jewish magical "
                        "tradition: Jewish exorcists were famous in the ancient world, often using divine "
                        "names (including 'Solomon' and 'the God of Abraham') in their incantations. The "
                        "difference between Jewish magical practice and Paul's ministry is authorization: "
                        "the sons of Sceva use the name without the relationship; Paul operates under the "
                        "direct commission of the risen Christ.",

        "second_temple": [
            {
                "source": "Greek Magical Papyri (PGM, 2nd century BC - 5th century AD)",
                "summary": "A collection of spells, invocations, and magical recipes from Greco-Roman "
                           "Egypt. They frequently invoke Jewish divine names (IAO, Sabaoth, Adonai) "
                           "alongside pagan deities, demonstrating the syncretistic magical culture.",
                "relevance": "Provides the cultural context for the sons of Sceva's attempt to use Jesus' "
                             "name as a magical formula. The Greek Magical Papyri show that invoking "
                             "powerful divine names was standard practice in ancient magic -- but Jesus' "
                             "name is not a spell; it is the authority of the enthroned Lord."
            },
            {
                "source": "Josephus, Antiquities 8.45-49",
                "summary": "Josephus describes Jewish exorcists using incantations attributed to Solomon, "
                           "including a certain Eleazar who exorcised a demon before the emperor Vespasian "
                           "by holding a ring with a root under the possessed person's nose.",
                "relevance": "Demonstrates the Jewish exorcistic tradition that the sons of Sceva "
                             "represent. The contrast with Paul is sharp: the sons of Sceva rely on "
                             "technique and formula; Paul relies on the Spirit's authority."
            }
        ],

        "cross_refs": [
            {"ref": "1 Corinthians 1:1-2", "note": "'To the church of God that is in Corinth' -- Paul's letter to the church he founded in Acts 18, written during his Ephesian ministry", "type": "nt"},
            {"ref": "Ephesians 6:10-20", "note": "'We do not wrestle against flesh and blood, but against the rulers, against the authorities' -- Paul's spiritual warfare teaching to the Ephesian church, informed by his experiences in Acts 19", "type": "nt"},
            {"ref": "1 Timothy 1:3", "note": "'Remain at Ephesus' -- Paul later charges Timothy to shepherd the Ephesian church he established", "type": "nt"},
            {"ref": "Deuteronomy 18:10-12", "note": "'There shall not be found among you anyone who practices divination or tells fortunes or interprets omens, or a sorcerer' -- the Torah prohibition that the Ephesian book-burning fulfills", "type": "ot"},
            {"ref": "Isaiah 44:9-20", "note": "The idol polemic: those who make idols are 'nothing' -- the Artemis cult's collapse in the face of the gospel confirms Isaiah's judgment on idol-worship", "type": "ot"},
            {"ref": "Acts 20:28-30", "note": "Paul's farewell to the Ephesian elders warns of 'fierce wolves' who will enter -- even after the territorial powers are defeated, internal threats remain", "type": "nt"}
        ],

        "divine_council_note": "The Ephesian ministry (Acts 19) is the climactic spiritual warfare episode "
                               "in Acts and one of the most revealing divine council confrontations in the "
                               "entire NT. Ephesus was a stronghold of the territorial powers: the Artemis "
                               "cult, the magical tradition, and the exorcistic industry all represented "
                               "the spiritual infrastructure that held the city under the governance of "
                               "hostile elohim. Paul's ministry systematically dismantles this infrastructure. "
                               "(1) The sons of Sceva episode (19:13-17) is the pivotal teaching moment. "
                               "Seven Jewish exorcists try to invoke Jesus' name as a magical formula: 'I "
                               "adjure you by the Jesus whom Paul proclaims' (19:13). The evil spirit's "
                               "response is devastating: 'Jesus I know (ginosko), and Paul I recognize "
                               "(epistamai), but who are you?' (19:15). The demon distinguishes between "
                               "knowing Jesus (personal relationship/authority), recognizing Paul (an "
                               "authorized agent), and having no knowledge of the sons of Sceva (unauthorized "
                               "users). This reveals the divine council's authority structure: the name of "
                               "Jesus carries power only for those commissioned by the council. (2) The "
                               "book-burning (19:19) represents the renunciation of the territorial powers' "
                               "spiritual technology. 'Fifty thousand pieces of silver' worth of magical "
                               "texts -- the famous 'Ephesian letters' (Ephesia grammata) -- are publicly "
                               "destroyed. This is not censorship but liberation: converts voluntarily "
                               "destroy the instruments of their bondage to the territorial spirits. (3) "
                               "The Artemis riot (19:23-41) reveals the economic dimension: the territorial "
                               "spirits sustain not only spiritual bondage but economic systems built on "
                               "idol-worship. Demetrius' complaint is honest: 'There is danger not only "
                               "that this trade of ours may come into disrepute but also that the temple of "
                               "the great goddess Artemis may be counted as nothing' (19:27). The gospel "
                               "threatens the entire spiritual-economic order of Ephesus.",

        "sections": [
            {
                "heading": "Corinth, Gallio, and the Gospel Under Roman Law (18:1-28)",
                "body": "Paul arrives in Corinth and meets Aquila and Priscilla, Jewish tentmakers "
                        "expelled from Rome by Claudius (18:2). He works with them and preaches in the "
                        "synagogue every Sabbath (18:3-4). When Silas and Timothy arrive from Macedonia, "
                        "'Paul was occupied with the word, testifying to the Jews that the Christ was "
                        "Jesus' (18:5). Rejected by the synagogue, he declares: 'Your blood be on your "
                        "own heads! I am innocent. From now on I will go to the Gentiles' (18:6). He "
                        "moves next door to the house of Titius Justus, a worshiper of God (18:7). "
                        "Crispus, the synagogue ruler, believes (18:8). The Lord speaks in a night "
                        "vision: 'Do not be afraid... for I have many in this city who are my people' "
                        "(18:9-10). Paul stays eighteen months (18:11). When Jews bring Paul before "
                        "Gallio, the proconsul of Achaia, Gallio refuses to judge 'a matter of questions "
                        "about words and names and your own law' (18:15). This is a landmark: Roman law "
                        "recognizes the gospel as an internal Jewish dispute, not a criminal matter. "
                        "Paul sails to Ephesus briefly (18:19-21), returns to Antioch (18:22), and "
                        "begins his third journey. Apollos, an Alexandrian Jew 'eloquent and competent "
                        "in the Scriptures' (18:24), is further instructed by Priscilla and Aquila "
                        "(18:26) and becomes a powerful preacher in Achaia (18:27-28)."
            },
            {
                "heading": "Ephesus: Miracles, Exorcists, Books, and Artemis (19:1 - 20:38)",
                "body": "Paul finds twelve disciples of John the Baptist in Ephesus who have not received "
                        "the Holy Spirit (19:1-7). He teaches daily in the hall of Tyrannus for two years "
                        "(19:9-10). 'God was doing extraordinary miracles (dynameis ou tas tychousas) by "
                        "the hands of Paul' -- handkerchiefs and aprons carried from his body healed the "
                        "sick and expelled evil spirits (19:11-12). Jewish exorcists attempt to use Jesus' "
                        "name: 'I adjure you by the Jesus whom Paul proclaims' (19:13). The evil spirit "
                        "responds: 'Jesus I know, and Paul I recognize, but who are you?' (19:15). The "
                        "demonized man overpowers all seven of them (19:16). 'Fear fell upon them all, "
                        "and the name of the Lord Jesus was extolled' (19:17). Converts bring their "
                        "magic books (ta perierga) and burn them publicly: value, '50,000 pieces of "
                        "silver' (19:19). 'So the word of the Lord continued to increase and prevail "
                        "mightily (kata kratos)' (19:20). Demetrius the silversmith incites a riot: "
                        "'Great is Artemis of the Ephesians!' (19:28). The city clerk calms the crowd "
                        "(19:35-41). Paul travels through Macedonia and Greece (20:1-6), raises Eutychus "
                        "from the dead at Troas (20:7-12), and gives his farewell to the Ephesian elders "
                        "at Miletus: 'I did not shrink from declaring to you the whole counsel (boulen) "
                        "of God' (20:27). 'Pay careful attention to yourselves and to all the flock, in "
                        "which the Holy Spirit has made you overseers (episkopous)' (20:28). He warns: "
                        "'Fierce wolves will come in among you, not sparing the flock' (20:29)."
            }
        ]
    },

    {
        "id": "acts-21-23",
        "ref": "Acts 21-23",
        "chapter_num": 5,
        "title": "Jerusalem Arrest, the Sanhedrin, and Angels -- Paul in the Eye of the Storm",
        "era": "acts_mission",
        "type": "study",
        "themes": ["DC", "KING", "SEED", "HOLY", "SPIRIT"],

        "synopsis": "Paul returns to Jerusalem despite prophetic warnings. At Tyre, disciples 'through "
                    "the Spirit' urge Paul not to go (21:4). At Caesarea, the prophet Agabus binds Paul's "
                    "hands and feet with his belt: 'Thus says the Holy Spirit, \"This is how the Jews at "
                    "Jerusalem will bind the man who owns this belt\"' (21:11). Paul's response: 'I am "
                    "ready not only to be imprisoned but even to die in Jerusalem for the name of the Lord "
                    "Jesus' (21:13). In Jerusalem, Paul meets James and the elders, who report that thousands "
                    "of Jewish believers are 'zealous for the law' (21:20). To demonstrate his own Torah "
                    "observance, Paul undertakes a purification vow at the Temple (21:23-26). But Jews from "
                    "Asia recognize him, drag him from the Temple, and try to kill him (21:27-31). Roman "
                    "soldiers rescue him. Paul addresses the crowd from the barracks steps (22:1-21), "
                    "recounting his conversion on the Damascus road. The crowd listens until he mentions "
                    "being sent 'far away to the Gentiles' (22:21) -- then they erupt: 'Away with such a "
                    "fellow from the earth! For he should not be allowed to live' (22:22). Paul reveals his "
                    "Roman citizenship to avoid scourging (22:25-29). Before the Sanhedrin, Paul declares: "
                    "'I am a Pharisee, a son of Pharisees. It is with respect to the hope and the "
                    "resurrection of the dead that I am on trial' (23:6). This divides the council: 'The "
                    "Pharisees argued vigorously, saying, \"We find nothing wrong in this man. What if a "
                    "spirit or an angel spoke to him?\"' (23:9). The Pharisee-Sadducee split on angels and "
                    "resurrection becomes Paul's defense. That night, the Lord stands by Paul: 'Take "
                    "courage, for as you have testified to the facts about me in Jerusalem, so you must "
                    "testify also in Rome' (23:11).",

        "key_verse": {
            "ref": "Acts 23:6, 8-9",
            "text": "Now when Paul perceived that one part were Sadducees and the other Pharisees, he cried out in the council, 'Brothers, I am a Pharisee, a son of Pharisees. It is with respect to the hope and the resurrection of the dead that I am on trial.' ... For the Sadducees say that there is no resurrection, nor angel, nor spirit, but the Pharisees acknowledge them all. Then a great clamor arose, and some of the scribes of the Pharisees' party stood up and argued vigorously, 'We find nothing wrong in this man. What if a spirit or an angel spoke to him?'",
            "translation": "ESV"
        },

        "original_terms": [
            "anastasis (resurrection -- the core issue dividing Pharisees and Sadducees; the Sadducees denied it; Paul exploits this theological division (23:6-8))",
            "angelos kai pneuma (angel and spirit -- the Sadducees deny these (23:8); the Pharisees affirm them; the divine council worldview is the battleground)",
            "episte de auto ho kyrios (the Lord stood by him -- 'the Lord stood by him' (23:11); a divine council appearance: the risen Christ appears to Paul in his cell to commission him for Rome)",
            "onoma tou kyriou Iesou (the name of the Lord Jesus -- Paul is willing to die 'for the name' (21:13); the name represents the person and authority of the enthroned Christ)",
            "boule tou theou (the counsel/plan of God -- echoing Paul's farewell: 'the whole counsel of God' (20:27); God's sovereign plan unfolds even through Paul's arrest and imprisonment)"
        ],

        "ane_backdrop": "The Pharisee-Sadducee split over angels and resurrection (23:8) reveals a "
                        "fundamental theological divide in Second Temple Judaism. The Sadducees, who "
                        "accepted only the Torah (Pentateuch) as authoritative, rejected belief in "
                        "angels, spirits, and resurrection because they found no clear basis for these "
                        "doctrines in the five books of Moses (though the Torah does mention angels). "
                        "The Pharisees affirmed all three based on the broader canonical tradition. This "
                        "divide is a divine council issue: the Sadducees rejected the elaborate angelology "
                        "and demonology that had developed in the Second Temple period (1 Enoch, Daniel, "
                        "Jubilees), while the Pharisees embraced it. Paul, as a Pharisee, affirms the "
                        "full divine council worldview -- angels, spirits, and resurrection -- and his "
                        "Damascus road encounter is proof that this worldview is correct: a spirit (the "
                        "risen Jesus) spoke to him. The Pharisees' question -- 'What if a spirit or an "
                        "angel spoke to him?' (23:9) -- inadvertently validates Paul's entire ministry.",

        "second_temple": [
            {
                "source": "Josephus, Jewish War 2.162-166",
                "summary": "Josephus describes the Pharisees as believing in the immortality of the "
                           "soul and rewards and punishments after death, while the Sadducees deny "
                           "the survival of the soul and all postmortem rewards.",
                "relevance": "Confirms the Pharisee-Sadducee division that Paul exploits in Acts 23:6-9. "
                             "Josephus' description of Pharisaic belief in spiritual beings aligns with "
                             "the divine council worldview that Paul affirms."
            },
            {
                "source": "Acts of the Apostles 23:8 itself as historical source",
                "summary": "Luke notes: 'The Sadducees say that there is no resurrection, nor angel, "
                           "nor spirit, but the Pharisees acknowledge them all.'",
                "relevance": "This is one of the most concise summaries of the theological divide in "
                             "Second Temple Judaism. The Sadducees' denial of angels and spirits amounts "
                             "to a rejection of the divine council framework; the Pharisees' affirmation "
                             "of 'them all' embraces it."
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 12:2-3", "note": "'Many of those who sleep in the dust of the earth shall awake' -- the OT basis for resurrection belief that Pharisees affirmed and Sadducees denied", "type": "ot"},
            {"ref": "Genesis 22:11", "note": "'Abraham, Abraham!' -- the doubled name pattern echoed in 'Saul, Saul' (22:7); divine address to a chosen agent", "type": "ot"},
            {"ref": "Isaiah 6:1-8", "note": "Isaiah's throne room vision and commission -- the pattern for Paul's Damascus road encounter: seeing the divine glory, receiving a commission", "type": "ot"},
            {"ref": "Acts 9:1-19", "note": "The first account of Paul's conversion -- Acts 22:6-16 retells it before the Jerusalem crowd with additional details", "type": "nt"},
            {"ref": "Acts 26:12-18", "note": "The third account of Paul's conversion -- before Agrippa, emphasizing the commission to turn Gentiles 'from the power of Satan to God'", "type": "nt"},
            {"ref": "2 Corinthians 11:23-28", "note": "Paul's catalog of sufferings -- the Jerusalem arrest and subsequent imprisonment are part of the pattern he describes", "type": "nt"}
        ],

        "divine_council_note": "Acts 21-23 reveals the divine council operating at multiple levels. "
                               "(1) Prophetic warnings: the Spirit warns Paul about Jerusalem through "
                               "disciples at Tyre (21:4) and through the prophet Agabus (21:10-11). The "
                               "Spirit is not forbidding the journey but revealing its cost -- the divine "
                               "council's plan includes Paul's suffering. (2) The Pharisee-Sadducee split "
                               "on angels and resurrection (23:6-9) is fundamentally a split over the "
                               "divine council worldview. The Sadducees reject the developed angelology "
                               "of the Second Temple period; the Pharisees affirm it. Paul identifies "
                               "with the Pharisaic position -- he affirms angels, spirits, and resurrection "
                               "because his entire ministry was launched by an encounter with a 'spirit' "
                               "(the risen Jesus) and an 'angel' (the heavenly light and voice on the "
                               "Damascus road). The Pharisees' half-defense -- 'What if a spirit or an "
                               "angel spoke to him?' (23:9) -- is more accurate than they know: the "
                               "enthroned Son of God, the supreme member of the divine council, DID speak "
                               "to Paul. (3) The Lord's appearance to Paul in his cell (23:11) is a divine "
                               "council visitation: 'Take courage, for as you have testified to the facts "
                               "about me in Jerusalem, so you must (dei -- divine necessity) testify also "
                               "in Rome.' The divine council has decreed Paul's journey to Rome. Nothing "
                               "-- not the Jewish plot (23:12-22), not Roman bureaucracy, not storms at sea "
                               "-- can prevent the council's plan from being fulfilled.",

        "sections": [
            {
                "heading": "Return to Jerusalem and Arrest at the Temple (21:1 - 22:29)",
                "body": "Paul travels to Jerusalem despite warnings. At Tyre, disciples 'through the "
                        "Spirit' urge him not to go (21:4). Agabus prophesies his binding (21:10-11). "
                        "Paul: 'I am ready not only to be imprisoned but even to die... for the name of "
                        "the Lord Jesus' (21:13). In Jerusalem, James and the elders report thousands of "
                        "Jewish believers 'zealous for the law' (21:20). Paul undertakes a Temple vow "
                        "(21:23-26). Jews from Asia see him in the Temple and seize him: 'This is the "
                        "man who is teaching everyone everywhere against the people and the law and this "
                        "place' (21:28). They drag him out and try to kill him (21:30-31). Roman soldiers "
                        "rescue him (21:32). Paul addresses the crowd in Aramaic (22:2): recounts his "
                        "upbringing under Gamaliel (22:3), his persecution of the Way (22:4-5), and the "
                        "Damascus road encounter: 'A great light from heaven suddenly shone around me' "
                        "(22:6). 'Saul, Saul, why are you persecuting me?' (22:7). 'I am Jesus of "
                        "Nazareth, whom you are persecuting' (22:8). Ananias comes: 'The God of our "
                        "fathers appointed you to know his will, to see the Righteous One and to hear "
                        "a voice from his mouth' (22:14). In a Temple vision, Jesus tells Paul: 'Go, "
                        "for I will send you far away to the Gentiles (ethne)' (22:21). At this word "
                        "they erupt (22:22). Paul invokes Roman citizenship (22:25-29)."
            },
            {
                "heading": "The Sanhedrin, the Plot, and the Lord's Commission (22:30 - 23:35)",
                "body": "Paul before the Sanhedrin: 'Brothers, I have lived my life before God in all "
                        "good conscience up to this day' (23:1). The high priest Ananias orders him "
                        "struck; Paul responds: 'God is going to strike you, you whitewashed wall!' "
                        "(23:3). Perceiving the Pharisee-Sadducee divide, Paul cries: 'I am a Pharisee! "
                        "It is with respect to the hope and the resurrection of the dead that I am on "
                        "trial' (23:6). The council erupts. 'The Sadducees say that there is no "
                        "resurrection, nor angel, nor spirit, but the Pharisees acknowledge them all' "
                        "(23:8). Pharisaic scribes defend Paul: 'What if a spirit or an angel spoke to "
                        "him?' (23:9). That night, 'the Lord stood by him (episte de auto ho kyrios) "
                        "and said, \"Take courage, for as you have testified to the facts about me in "
                        "Jerusalem, so you must testify also in Rome\"' (23:11). A conspiracy of more "
                        "than forty Jews vows not to eat until they have killed Paul (23:12-14). Paul's "
                        "nephew alerts the tribune (23:16-22). Paul is transferred under heavy guard to "
                        "Caesarea and the governor Felix (23:23-35). The divine plan is in motion: "
                        "Paul will reach Rome."
            }
        ]
    },

    {
        "id": "acts-24-28",
        "ref": "Acts 24-28",
        "chapter_num": 6,
        "title": "Felix, Festus, Agrippa, and the Voyage to Rome -- The Gospel Reaches the Capital",
        "era": "acts_mission",
        "type": "study",
        "themes": ["KING", "NATIONS", "DC", "REVERSAL", "RIV"],

        "synopsis": "Paul's trial and journey to Rome occupy the final five chapters of Acts. Before Felix, "
                    "Paul declares: 'I worship the God of our fathers, believing everything laid down by the "
                    "Law and written in the Prophets, having a hope in God... that there will be a "
                    "resurrection of both the just and the unjust' (24:14-15). Felix, 'well informed about "
                    "the Way' (24:22), keeps Paul imprisoned for two years, hoping for a bribe (24:26). "
                    "Festus succeeds Felix and proposes a Jerusalem trial; Paul appeals to Caesar: 'I appeal "
                    "to Caesar' (25:11). Before King Agrippa II, Paul delivers his most comprehensive defense "
                    "(26:1-29), recounting his Damascus road encounter a third time with the fullest "
                    "commission statement: 'I am sending you to open their eyes, so that they may turn from "
                    "darkness to light and from the power (exousia) of Satan to God, that they may receive "
                    "forgiveness of sins and a place among those who are sanctified by faith in me' "
                    "(26:17-18). Agrippa's verdict: 'This man could have been set free if he had not appealed "
                    "to Caesar' (26:32). The sea voyage to Rome (chapter 27) is a masterpiece of ancient "
                    "maritime narrative. A storm threatens destruction; Paul is assured by an angel: 'Do not "
                    "be afraid, Paul; you must stand before Caesar. And behold, God has granted you all "
                    "those who sail with you' (27:24). They are shipwrecked on Malta (28:1-10). Paul finally "
                    "reaches Rome (28:14-16). He meets with Jewish leaders and quotes Isaiah 6:9-10 -- the "
                    "hardening prophecy. Acts ends with Paul 'proclaiming the kingdom of God and teaching "
                    "about the Lord Jesus Christ with all boldness and without hindrance' (28:31).",

        "key_verse": {
            "ref": "Acts 26:17-18",
            "text": "'I am sending you to open their eyes, so that they may turn from darkness to light and from the power of Satan to God, that they may receive forgiveness of sins and a place among those who are sanctified by faith in me.'",
            "translation": "ESV"
        },

        "original_terms": [
            "exousia tou Satana (the power/authority of Satan -- 'from the power of Satan to God' (26:18); the nations are under Satan's jurisdiction; Paul's mission transfers them to God's kingdom)",
            "he hodos (the Way -- 'concerning the Way (tes hodou)' (24:14, 22); the self-designation of early Christians; not a new religion but the fulfillment of Israel's path)",
            "meta parrhesias akolytos (with all boldness without hindrance -- the final words of Acts (28:31); the gospel preached in Rome, the center of the world's power, with complete freedom)",
            "basileia tou theou (the kingdom of God -- Paul preaches 'the kingdom of God' in Rome (28:31); the divine council's reign advancing into the capital of the human empire)",
            "angelos theou (angel of God -- 'there stood before me this night an angel of the God to whom I belong' (27:23); a divine council messenger reassures Paul during the storm)"
        ],

        "ane_backdrop": "Paul's appeal to Caesar (25:11) invokes the right of 'provocatio' -- a Roman "
                        "citizen's legal right to have their case heard by the emperor. This legal "
                        "mechanism becomes the means by which the divine council ensures Paul reaches "
                        "Rome. The sea voyage of chapter 27 is one of the finest pieces of ancient "
                        "maritime narrative, with technical details of navigation, ship types, and weather "
                        "patterns that have been confirmed by maritime historians. The route from Caesarea "
                        "to Rome via Myra, Cnidus, Fair Havens (Crete), Malta, Syracuse, Rhegium, and "
                        "Puteoli covers approximately 2,000 nautical miles. The 'Euroclydon' (euraquilo, "
                        "27:14) was a northeast wind notorious in the central Mediterranean. The "
                        "shipwreck narrative includes 276 persons (27:37) -- a detail typical of ancient "
                        "historical precision. Paul's arrival in Rome fulfills both the commission of "
                        "Acts 1:8 ('to the end of the earth' -- Rome was the center of the known world) "
                        "and the Lord's direct promise (23:11, 'you must testify also in Rome'). The "
                        "theological geography is complete: the gospel has traveled from Jerusalem, "
                        "the center of the Jewish world, to Rome, the center of the Gentile world.",

        "second_temple": [
            {
                "source": "Isaiah 6:9-10 (LXX)",
                "summary": "'Go and say to this people: Keep on hearing, but do not understand; keep "
                           "on seeing, but do not perceive. Make the heart of this people dull, and "
                           "their ears heavy, and blind their eyes.'",
                "relevance": "Paul quotes this as his final word to the Roman Jews (28:26-27), "
                             "interpreting Israel's rejection of the gospel as the fulfillment of "
                             "Isaiah's hardening prophecy -- the same text Jesus used (Mark 4:12; "
                             "Luke 8:10) and that Romans 11:7-10 develops."
            },
            {
                "source": "Josephus, Jewish War 2.184-203",
                "summary": "Josephus describes King Agrippa I's speech urging the Jews not to rebel "
                           "against Rome, noting Agrippa II's close relationship with Rome and his "
                           "role as a client king.",
                "relevance": "Provides historical context for Paul's appearance before Agrippa II "
                             "(Acts 25:13 - 26:32). Agrippa is a Herodian king, nominally Jewish, "
                             "politically beholden to Rome -- the perfect audience for Paul's case "
                             "that the gospel fulfills Jewish hopes without threatening Roman order."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 6:9-10", "note": "'Make the heart of this people dull' -- quoted by Paul as his final word to the Roman Jews (28:26-27); the hardening prophecy that closes the book", "type": "ot"},
            {"ref": "Isaiah 49:6", "note": "'A light for the Gentiles, that my salvation may reach to the end of the earth' -- the mandate fulfilled as the gospel reaches Rome", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God -- the framework Paul summarizes in 26:18: the nations are under 'the power of Satan' and Paul's mission reclaims them", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "'To him was given dominion and glory and a kingdom, that all peoples, nations, and languages should serve him' -- fulfilled as the gospel reaches the nations through Paul's ministry", "type": "ot"},
            {"ref": "Romans 1:15-16", "note": "'I am eager to preach the gospel to you also who are in Rome... it is the power of God for salvation to everyone who believes' -- Paul's letter anticipates his arrival in Acts 28", "type": "nt"},
            {"ref": "Philippians 1:12-14", "note": "'What has happened to me has really served to advance the gospel... throughout the whole imperial guard' -- Paul's imprisonment in Rome advances the kingdom", "type": "nt"}
        ],

        "divine_council_note": "The final chapters of Acts bring the divine council narrative to its "
                               "climax. (1) Paul's speech before Agrippa (26:1-29) contains the fullest "
                               "statement of his commission: 'I am sending you to open their eyes, so "
                               "that they may turn from darkness to light and from the power (exousia) of "
                               "Satan to God' (26:17-18). This is the Deuteronomy 32 reversal expressed "
                               "in its clearest terms: the nations are under Satan's exousia -- the "
                               "authority structure established when the nations were allotted to the sons "
                               "of God at Babel. Paul's mission is to transfer them 'from the power of "
                               "Satan to God.' Every conversion is a territorial transfer, every church "
                               "planted is a beachhead of the divine kingdom in enemy territory. (2) The "
                               "sea voyage angel (27:23-24) is a divine council messenger: 'There stood "
                               "before me this night an angel of the God to whom I belong and whom I "
                               "worship, and he said, \"Do not be afraid, Paul; you must (dei) stand "
                               "before Caesar.\"' The divine necessity (dei) is the council's decree: "
                               "nothing can prevent Paul from reaching Rome. (3) The ending of Acts is "
                               "theologically deliberate. Paul quotes Isaiah 6:9-10 to the Roman Jews "
                               "(28:26-27), then declares: 'Therefore let it be known to you that this "
                               "salvation of God has been sent to the Gentiles; they will listen' (28:28). "
                               "This is the final programmatic statement of Babel reversal: the salvation "
                               "intended for all nations has reached the capital of the world. Paul "
                               "preaches 'the kingdom of God' (28:31) -- the divine council's reign -- "
                               "'with all boldness and without hindrance (akolytos).' The last word of "
                               "Acts, akolytos ('unhindered'), is the book's final theological claim: "
                               "nothing -- not Jewish opposition, not Roman power, not the territorial "
                               "spirits -- can hinder the advance of God's kingdom. The Babel judgment is "
                               "being reversed. The nations are coming home.",

        "sections": [
            {
                "heading": "Before Felix, Festus, and Agrippa (24:1 - 26:32)",
                "body": "Before Felix, Paul declares: 'According to the Way (kata ten hodon), which they "
                        "call a sect, I worship the God of our fathers, believing everything laid down by "
                        "the Law and written in the Prophets' (24:14). He affirms: 'a hope in God... that "
                        "there will be a resurrection of both the just and the unjust' (24:15). Felix, "
                        "'well informed about the Way' (24:22), keeps Paul two years, hoping for a bribe "
                        "(24:26). Festus proposes a Jerusalem trial; Paul appeals to Caesar (25:10-11). "
                        "Festus to Agrippa: 'The accused... had certain points of dispute with him about "
                        "their own religion and about a certain Jesus, who was dead, but whom Paul "
                        "asserted to be alive' (25:19). Before Agrippa, Paul delivers his fullest "
                        "defense: 'I stand here on trial because of my hope in the promise made by God "
                        "to our fathers, to which our twelve tribes hope to attain' (26:6-7). The Damascus "
                        "road: 'A light from heaven, brighter than the sun, shining around me' (26:13). "
                        "The commission: 'I am sending you to open their eyes, so that they may turn from "
                        "darkness to light and from the power of Satan to God' (26:17-18). Agrippa: "
                        "'In a short time would you persuade me to be a Christian?' (26:28). Paul: 'I "
                        "would to God that... all who hear me this day might become such as I am -- "
                        "except for these chains' (26:29). Verdict: 'This man could have been set free "
                        "if he had not appealed to Caesar' (26:32). But the appeal is providential: "
                        "the council has decreed that Paul will testify in Rome."
            },
            {
                "heading": "The Voyage to Rome and the Gospel Unhindered (27:1 - 28:31)",
                "body": "Paul sails for Rome under guard (27:1). The 'we-passage' resumes (27:1) -- "
                        "Luke is present. They sail via Myra, Cnidus, and Fair Havens on Crete (27:5-8). "
                        "Paul warns against continuing: 'I perceive that the voyage will be with injury "
                        "and much loss' (27:10). They sail anyway and are caught by the Euroclydon "
                        "(27:14). After fourteen days without sun or stars, 'all hope of our being saved "
                        "was at last abandoned' (27:20). Paul stands up: 'There stood before me this "
                        "night an angel of the God to whom I belong... saying, \"Do not be afraid, Paul; "
                        "you must stand before Caesar. And behold, God has granted you all those who "
                        "sail with you\"' (27:23-24). They run aground on Malta; all 276 persons survive "
                        "(27:44). On Malta, Paul is bitten by a viper and survives (28:3-6). He heals "
                        "the father of Publius (28:8) and many others (28:9). After three months, they "
                        "sail to Rome (28:11-14). Paul meets with Jewish leaders: 'It is because of the "
                        "hope of Israel that I am wearing this chain' (28:20). Some believe, some "
                        "disbelieve (28:24). Paul quotes Isaiah 6:9-10: 'The heart of this people has "
                        "grown dull' (28:27). Then the programmatic conclusion: 'Let it be known to you "
                        "that this salvation of God has been sent to the Gentiles (tois ethnesin); they "
                        "will listen (autoi kai akousontai)' (28:28). 'He lived there two whole years... "
                        "proclaiming the kingdom of God and teaching about the Lord Jesus Christ with "
                        "all boldness and without hindrance (akolytos)' (28:30-31). Acts ends not with "
                        "a period but with an open door: the gospel is loose in Rome, preached without "
                        "hindrance. The Deuteronomy 32 reversal has reached the center of the world."
            }
        ]
    }
]
