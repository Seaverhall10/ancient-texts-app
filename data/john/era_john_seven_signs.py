"""
era_john_seven_signs.py -- The Seven Signs: Miracles That Reveal the Divine Identity (John 2-11)

John's Gospel is structured around seven specific signs (semeia) -- not random
miracles but carefully selected revelations of who Jesus is. John explicitly
tells us his selection principle: "Jesus did many other signs in the presence
of the disciples, which are not written in this book; but these are written
so that you may believe that Jesus is the Christ, the Son of God, and that
by believing you may have life in his name" (20:30-31). Each sign escalates
the christological claim: (1) Water to Wine at Cana -- the Creator transforms
the elements; (2) Healing the Official's Son from a distance -- authority over
space and matter; (3) Healing at Bethesda on the Sabbath -- Jesus works as the
Father works, triggering the accusation that he "was making himself equal with
God" (5:18); (4) Feeding the 5,000 -- the new Moses who provides bread from
heaven, but "the bread of God is he who comes down from heaven" (6:33); (5)
Walking on Water with the absolute ego eimi -- "It is I; do not be afraid"
(6:20), invoking the divine name on the chaos waters; (6) Healing the Man Born
Blind -- "I am the light of the world" demonstrated in action; (7) Raising
Lazarus -- "I am the resurrection and the life" demonstrated in the supreme
sign. The progression moves from transformation to creation to conquest of
death itself. Each sign forces the same decision: worship or rejection.
"""

CHAPTERS = [
    {
        "id": "john-seven-signs-01",
        "ref": "John 2:1-11, 4:46-54",
        "chapter_num": 1,
        "title": "The First and Second Signs -- Water to Wine and the Official's Son",
        "era": "john_seven_signs",
        "type": "chapter",
        "themes": ["DC", "GLORY", "TYPE", "SEED", "KING"],

        "synopsis": "The first two signs bracket Jesus' early Galilean ministry, and John explicitly "
                    "numbers them: 'This, the first of his signs (proten semeion), Jesus did at Cana' "
                    "(2:11) and 'This was now the second sign (deuteron semeion) that Jesus did when he "
                    "had come from Judea to Galilee' (4:54). The first sign -- water to wine at the "
                    "wedding feast (2:1-11) -- reveals Jesus as the Creator who transforms the elements "
                    "of the old covenant into the abundance of the new. Six stone jars 'for the Jewish "
                    "rites of purification' (2:6) become vessels of messianic wine. The sign 'manifested "
                    "his glory (doxa), and his disciples believed in him' (2:11). The second sign -- "
                    "healing the royal official's (basilikos) son at Capernaum from a distance while "
                    "Jesus remains in Cana (4:46-54) -- reveals Jesus' authority over space, disease, "
                    "and death itself ('Your son will live,' 4:50). The official 'believed the word "
                    "(logo) that Jesus spoke to him' (4:50) -- faith in the Word's word. The fever "
                    "left the boy 'at the seventh hour' (4:52), the exact moment Jesus spoke. Together "
                    "these two signs establish the pattern: Jesus is not a prophet performing wonders "
                    "to authenticate a message -- he is the Logos exercising the Creator's authority "
                    "over his creation. The signs reveal his identity, not merely his power.",

        "key_verse": {
            "ref": "John 2:11",
            "text": "This, the first of his signs, Jesus did at Cana in Galilee, and manifested his glory. And his disciples believed in him.",
            "translation": "ESV"
        },

        # NOTE: These are Greek (NT) terms — field name is a known schema limitation
        "hebrew_terms": [
            "semeion (sign -- John's term for Jesus' miracles; distinct from teras, 'wonder/portent'; "
            "a semeion points beyond itself to reveal something about the one performing it; the signs "
            "are not just demonstrations of power but revelations of identity and glory)",
            "doxa (glory -- the Greek rendering of kavod; the weighty, radiant divine presence; the "
            "first sign 'manifested his glory' -- the kavod of the Logos was visible in the miracle; "
            "this is the glory shared with the Father 'before the world existed,' 17:5)",
            "hora (hour -- 2:4, 'My hour has not yet come'; the divinely appointed moment of Jesus' "
            "death and glorification; every sign points forward to the 'hour' when the supreme sign "
            "-- the cross and resurrection -- will occur)",
            "basilikos (royal official -- 4:46; from basileus, 'king'; a man of royal standing, "
            "possibly connected to Herod Antipas's court; his son is healed by the authority of "
            "the true King's spoken word)",
            "logos (word -- 4:50, 'the man believed the word (logo) that Jesus spoke'; the healing "
            "occurs through the spoken word of the Logos; the same Word who created all things (1:3) "
            "now restores what sin and death have corrupted)"
        ],

        "ane_backdrop": "The wedding at Cana evokes the ANE motif of the divine banquet. In Ugaritic "
                        "literature, the gods feast with abundant wine at El's mountain; in Isaiah's "
                        "eschatological vision, 'the LORD of hosts will make for all peoples a feast of "
                        "rich food, a feast of well-aged wine' (Isa 25:6). Wine abundance was a marker of "
                        "the messianic age in prophetic expectation: 'The mountains shall drip sweet wine' "
                        "(Amos 9:13); 'new wine will drip from the mountains' (Joel 3:18). Jesus providing "
                        "120-180 gallons of the finest wine at a wedding signals the arrival of the age the "
                        "prophets foretold. The healing-at-a-distance motif (the official's son) parallels "
                        "ANE royal healing traditions where a king's decree carried power across distance, "
                        "but here the authority is not political but cosmic -- the Word speaks and reality "
                        "reshapes itself.",

        "second_temple": [
            {
                "source": "2 Baruch 29:5 (~early 2nd century AD, but reflecting earlier traditions)",
                "summary": "'The earth shall also yield its fruit ten-thousandfold, and on each vine there "
                           "shall be a thousand branches, and each branch shall produce a thousand clusters, "
                           "and each cluster produce a thousand grapes, and each grape produce a cor of wine.'",
                "relevance": "The extravagant wine abundance expected in the messianic age provides the "
                             "eschatological context for Cana: Jesus producing 120-180 gallons of the finest "
                             "wine signals that the messianic age has arrived."
            },
            {
                "source": "Philo, On the Life of Moses 1.97-100",
                "summary": "Philo interprets Moses' miracles as signs (semeia) revealing the power of the "
                           "God who sent him, not merely as wonders to impress. The signs authenticate the "
                           "messenger by pointing to the sender.",
                "relevance": "John's sign-theology parallels this understanding: the signs point beyond Jesus' "
                             "power to his identity -- he is not merely sent by God (as Moses was) but IS the "
                             "Logos through whom God created all things."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 25:6-8", "note": "'The LORD of hosts will make for all peoples a feast of rich food, a feast of well-aged wine' -- the messianic banquet inaugurated at Cana", "type": "ot"},
            {"ref": "Amos 9:13-14", "note": "'The mountains shall drip sweet wine, and all the hills shall flow with it' -- wine abundance as a marker of the restored kingdom", "type": "ot"},
            {"ref": "Genesis 1:3", "note": "'And God said, Let there be light, and there was light' -- the Creator's word reshaping reality, paralleled in Jesus' word healing the official's son", "type": "ot"},
            {"ref": "Psalm 107:20", "note": "'He sent out his word and healed them' -- YHWH heals by his word; Jesus heals by his word; the identity claim is implicit", "type": "ot"},
            {"ref": "2 Kings 5:10-14", "note": "Naaman healed at a distance by Elisha's word -- a prophetic precedent, but Jesus' healing surpasses it: no intermediary, no ritual, just the Logos speaking", "type": "ot"},
            {"ref": "Revelation 19:7-9", "note": "'The marriage supper of the Lamb has come' -- the eschatological wedding feast that Cana foreshadows reaches its consummation", "type": "nt"},
            {"ref": "Matthew 8:5-13", "note": "The centurion's servant healed at a distance -- a Synoptic parallel to the long-distance healing authority demonstrated in the second sign", "type": "nt"}
        ],

        "divine_council_note": "The first two signs establish a critical divine council principle: the one "
                               "performing them is not a prophet, not an angel, not a lesser elohim -- he is "
                               "the Creator himself. The water-to-wine miracle is an act of creation: the one "
                               "through whom 'all things were made' (1:3) transforms the molecular structure "
                               "of water into wine. No prophet ever did this -- Moses turned water to blood "
                               "(Exod 7:20) as a judgment; Jesus turns water to wine as a celebration. Elijah "
                               "multiplied oil (1 Kgs 17:14-16); Elisha multiplied oil (2 Kgs 4:1-7). These "
                               "were acts of prophetic mediation -- God working through a human agent. At Cana, "
                               "the agent IS the Creator. The second sign reinforces this: healing at a distance "
                               "by the spoken word, with the healing occurring at the precise moment the word "
                               "was spoken (4:52-53). In the divine council framework, only YHWH's word has "
                               "this kind of creative, reality-shaping power: 'He spoke, and it came to be' "
                               "(Ps 33:9). The signs do not prove Jesus is a great miracle worker; they prove "
                               "he is the Logos -- the divine Word whose speech is creative power itself.",

        "sections": [
            {
                "heading": "The First Sign: Water to Wine -- The Creator Transforms the Elements (2:1-11)",
                "body": "The first sign occurs 'on the third day' (te hemera te trite -- 2:1), completing "
                        "the new creation week that began in 1:19. Six stone water jars, each holding 20-30 "
                        "gallons (metretas duo e treis -- 2:6), stand ready 'for the Jewish rites of "
                        "purification' (kata ton katharismon ton Ioudaion). These are not just containers "
                        "but symbols: the old covenant's system of external purification, about to be "
                        "transformed. Jesus instructs: 'Fill the jars with water' (2:7); they fill them "
                        "to the brim (heos ano). Then: 'Now draw some out and take it to the master of "
                        "the feast' (2:8). No incantation, no ritual, no visible act of power -- the "
                        "Creator's will is sufficient. The master of the banquet tastes it and marvels: "
                        "'Everyone serves the good wine first, and when people have drunk freely, then "
                        "the poor wine. But you have kept the good wine until now (heos arti)' (2:10). "
                        "The theological statement is precise: the 'good wine' was kept for the end -- "
                        "the best of God's provision arrives in the messianic age, surpassing everything "
                        "that came before. The old purification system (water) gives way to messianic "
                        "celebration (wine). John's summary: 'This, the first of his signs (archen ton "
                        "semeion), Jesus did at Cana in Galilee, and manifested his glory (ephanerosen "
                        "ten doxan autou). And his disciples believed in him' (2:11). The doxa that "
                        "filled the Tabernacle is visible in the Logos's first creative act. [A]"
            },
            {
                "heading": "The Second Sign: The Official's Son Healed by the Word (4:46-54)",
                "body": "The second sign also occurs in Cana, creating an inclusio (literary bracket) "
                        "around the early ministry. A royal official (basilikos) from Capernaum comes to "
                        "Jesus because his son is 'at the point of death' (emellen gar apothneskein -- "
                        "4:47). He begs Jesus to 'come down and heal his son' (4:47) -- he assumes "
                        "physical presence is required. Jesus tests: 'Unless you see signs and wonders "
                        "(semeia kai terata), you will not believe' (4:48). The official persists: 'Sir, "
                        "come down before my child dies' (4:49). Then Jesus speaks the creative word: "
                        "'Go; your son will live (poreuou, ho huios sou ze)' (4:50). The man 'believed "
                        "the word (episteusen to logo) that Jesus spoke to him and went on his way' "
                        "(4:50). Faith in the logos -- the spoken word of the Logos. His servants meet "
                        "him with news: 'Your son will live!' (4:51, using the same word ze). He inquires "
                        "when the improvement began: 'Yesterday at the seventh hour (horan hebdomen) the "
                        "fever left him' (4:52). The father knows: 'that was the hour when Jesus had said "
                        "to him, Your son will live' (4:53). The healing occurred at the exact moment the "
                        "Word spoke. No delay, no process, no mechanism -- just the creative power of the "
                        "divine word reshaping reality across distance. [A] John numbers it explicitly: "
                        "'This was now the second sign (deuteron semeion) that Jesus did' (4:54). The "
                        "progression from sign one to sign two: transformation of elements (wine) to "
                        "restoration of life (healing). The Creator's authority over creation deepens. [A]"
            },
            {
                "heading": "The Sign Theology: Why John Uses Semeia, Not Dynameis",
                "body": "John's choice of semeion ('sign') rather than the Synoptic dynamis ('mighty work/ "
                        "power') is theologically deliberate. A dynamis emphasizes power -- what was done. "
                        "A semeion emphasizes meaning -- what it reveals. The Synoptics record dozens of "
                        "miracles; John selects exactly seven because each one is a signpost pointing to "
                        "Jesus' divine identity. [B] The number seven is itself significant: in Hebrew "
                        "symbolism, seven (sheva) represents completeness and divine perfection (the seven "
                        "days of creation, the seven branches of the menorah, the seven seals of Revelation). "
                        "Seven signs means a complete revelation of who Jesus is. John's editorial statement "
                        "confirms the purpose: 'Now Jesus did many other signs in the presence of the "
                        "disciples, which are not written in this book; but these are written so that you "
                        "may believe (pisteusete) that Jesus is the Christ (Christos), the Son of God "
                        "(huios tou theou), and that by believing you may have life (zoen) in his name' "
                        "(20:30-31). The signs are not evidence for a courtroom argument -- they are "
                        "encounters that demand a response. Each sign forced the original witnesses to "
                        "decide: is this the Creator in the flesh, or not? [B] The two responses to the "
                        "signs mirror the light/darkness dualism of the prologue (1:5): some see the signs "
                        "and believe (2:11; 4:53; 9:38; 11:45); others see the same signs and plot to kill "
                        "(11:47-53; 12:37). The light shines; some comprehend, some do not. [A]"
            }
        ]
    },

    {
        "id": "john-seven-signs-02",
        "ref": "John 5:1-15, 6:1-14",
        "chapter_num": 2,
        "title": "The Third and Fourth Signs -- Bethesda and the Feeding of 5,000",
        "era": "john_seven_signs",
        "type": "chapter",
        "themes": ["DC", "KING", "TYPE", "SEED", "GLORY"],

        "synopsis": "The third and fourth signs escalate the christological confrontation. At the Pool of "
                    "Bethesda (5:1-15), Jesus heals a man who has been paralyzed for 38 years -- and he "
                    "does it on the Sabbath, deliberately provoking the authorities. When challenged, Jesus "
                    "responds with the most radical claim yet: 'My Father is working until now, and I am "
                    "working (ho pater mou heos arti ergazetai, kago ergazomai)' (5:17). John notes: 'This "
                    "was why the Jews were seeking all the more to kill him, because not only was he breaking "
                    "the Sabbath, but he was even calling God his own Father (patera idion), making himself "
                    "equal with God (ison heauto poion to theo)' (5:18). The authorities understood the "
                    "claim perfectly: Jesus was asserting the same continuous creative-sustaining work as "
                    "YHWH, whose Sabbath rest did not mean cessation but ongoing governance. The fourth "
                    "sign -- feeding the 5,000 (6:1-14) -- presents Jesus as the new Moses who provides "
                    "bread from heaven. When the crowd sees the sign, they declare: 'This is indeed the "
                    "Prophet who is to come into the world (ho prophetes ho erchomenos eis ton kosmon)!' "
                    "(6:14), invoking the Deuteronomy 18:15-18 expectation. But they are thinking too small. "
                    "Jesus is not the new Moses; he is the reality that Moses mediated. 'The bread of God "
                    "is he who comes down from heaven and gives life to the world' (6:33). The manna "
                    "sustained bodies; the true bread IS a person who gives eternal life.",

        "key_verse": {
            "ref": "John 5:17-18",
            "text": "But Jesus answered them, 'My Father is working until now, and I am working.' This was why the Jews were seeking all the more to kill him, because not only was he breaking the Sabbath, but he was even calling God his own Father, making himself equal with God.",
            "translation": "ESV"
        },

        # NOTE: These are Greek (NT) terms — field name is a known schema limitation
        "hebrew_terms": [
            "ergazomai (to work -- 5:17; Jesus claims the same continuous working as the Father; "
            "the rabbinic tradition acknowledged that God does not cease working on the Sabbath -- "
            "he sustains creation, gives life, and judges even on the seventh day; Jesus claims the "
            "same divine prerogative)",
            "patera idion (his own Father -- 5:18; the construction with idios, 'one's own,' implies "
            "a unique relationship, not general divine fatherhood; to call God 'my own Father' in "
            "this context was understood as a claim to share God's nature)",
            "ison to theo (equal with God -- 5:18; the opponents' interpretation of Jesus' claim; "
            "isos means 'equal in nature, quality, or status'; cf. Phil 2:6 where Christ 'did not "
            "count equality (isa) with God a thing to be grasped')",
            "ho prophetes (the Prophet -- 6:14; from Deut 18:15-18, where Moses promises God will "
            "raise up 'a prophet like me'; the crowd applies this title after the feeding, seeing "
            "the Moses-manna parallel; but Jesus exceeds the category)",
            "artos tou theou (bread of God -- 6:33; not merely bread FROM God (as the manna was) "
            "but bread that IS God's self-giving; the bread 'comes down from heaven and gives life "
            "to the world'; the bread is a person, not a substance)",
            "manna (the wilderness bread -- traditionally from Hebrew man hu, 'what is it?'; Exod 16:15; "
            "the etymology is contested — some scholars derive it from Egyptian 'a gift' rather than "
            "Hebrew man hu; the Exodus 16:15 wordplay may be a folk etymology; the crowd demands a "
            "manna-like sign (6:31); Jesus reveals that the true manna was never about bread -- it "
            "was about the one the bread pointed to)"
        ],

        "ane_backdrop": "The Sabbath controversy has deep ANE background. In Mesopotamian religion, the "
                        "gods rested after creation because they were weary -- the creation of humanity was "
                        "specifically to relieve the gods of labor (Atrahasis Epic I). YHWH's Sabbath rest "
                        "(Gen 2:2-3) is fundamentally different: not cessation from exhaustion but enthronement "
                        "in completed creation -- the cosmic temple is finished, and the King takes his throne. "
                        "The rabbinic tradition (Genesis Rabbah 11:10) explicitly addressed the problem: God "
                        "cannot cease working on the Sabbath because the universe would collapse. He continues "
                        "his 'work' of giving life and executing judgment. Jesus' claim in 5:17 places himself "
                        "in this category: he works as the Father works, sustaining and governing creation. "
                        "The feeding miracle echoes the manna tradition, but the ANE royal ideology is also "
                        "relevant: ancient Near Eastern kings demonstrated their legitimacy by providing food "
                        "for their people. Jesus provides bread in the wilderness, marking him as the true King.",

        "second_temple": [
            {
                "source": "Genesis Rabbah 11:10",
                "summary": "The rabbinic tradition debated whether God works on the Sabbath. The conclusion: "
                           "God rests from creating new things but continues to sustain creation, give life "
                           "to the newborn, and execute judgment on the dead -- even on the Sabbath.",
                "relevance": "Jesus' claim in 5:17 uses exactly this rabbinic framework but applies it to "
                             "himself: 'My Father is working until now, and I am working.' He claims the same "
                             "continuous divine prerogative. The authorities understood this as a claim to "
                             "equality with God (5:18)."
            },
            {
                "source": "2 Baruch 29:8",
                "summary": "'At that time the treasury of manna shall come down again from on high, and "
                           "they will eat of it in those years, because these are they who have arrived at "
                           "the consummation of time.'",
                "relevance": "Jewish eschatological expectation included the return of manna in the messianic "
                             "age. The crowd's demand -- 'Our fathers ate the manna in the wilderness... what "
                             "sign do you do?' (6:31) -- reflects this expectation. Jesus redirects: the true "
                             "bread is not a substance but a person."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 2:2-3", "note": "'On the seventh day God finished his work... and rested' -- Jesus claims the Father's Sabbath 'work' of sustaining creation as his own (5:17)", "type": "ot"},
            {"ref": "Exodus 16:4-15", "note": "'I am about to rain bread from heaven for you' (16:4); 'It is the bread that the LORD has given you to eat' (16:15) -- Jesus corrects the attribution: 'It was not Moses who gave you the bread from heaven, but my Father gives you the true bread from heaven' (6:32); the manna tradition that Jesus fulfills and surpasses: the true bread is a person, not a substance", "type": "ot"},
            {"ref": "Deuteronomy 18:15-18", "note": "'The LORD your God will raise up for you a prophet like me' -- the crowd's identification of Jesus after the feeding (6:14), which Jesus exceeds", "type": "ot"},
            {"ref": "Psalm 78:24-25", "note": "'He rained down on them manna to eat and gave them the grain of heaven. Man ate of the bread of the angels' -- the manna as heavenly bread; Jesus is the reality it typified", "type": "ot"},
            {"ref": "Philippians 2:6", "note": "'Though he was in the form of God, did not count equality with God (isa theo) a thing to be grasped' -- Paul uses the same 'equal with God' language as John 5:18", "type": "nt"},
            {"ref": "Mark 6:30-44", "note": "The Synoptic feeding account -- all four Gospels record this miracle, the only sign besides the resurrection that appears in all four", "type": "nt"},
            {"ref": "1 Corinthians 10:1-4", "note": "'They all ate the same spiritual food... the Rock was Christ' -- Paul identifies Christ as the source of wilderness provision, paralleling John 6", "type": "nt"}
        ],

        "divine_council_note": "John 5:17-30 is the most explicit divine council Christology in the Gospels. "
                               "Jesus claims five divine prerogatives that belong to YHWH alone in the OT: "
                               "(1) Sabbath work -- sustaining creation continuously (5:17); (2) Life-giving -- "
                               "'as the Father raises the dead and gives them life, so also the Son gives life "
                               "to whom he will' (5:21); (3) Judgment -- 'the Father judges no one, but has "
                               "given all judgment to the Son' (5:22); (4) Honor equal to God -- 'that all may "
                               "honor the Son, just as they honor the Father' (5:23); (5) Life-in-himself -- "
                               "'as the Father has life in himself, so he has granted the Son also to have life "
                               "in himself' (5:26). Each of these is an exclusively divine function in the OT: "
                               "only YHWH sustains creation (Ps 104), only YHWH gives life (Deut 32:39; 1 Sam "
                               "2:6), only YHWH judges the world (Ps 96:13), only YHWH deserves ultimate honor "
                               "(Isa 42:8), only YHWH has inherent life. Jesus claims ALL of them -- not as a "
                               "delegate or angel, but as the Son who does 'whatever the Father does' (5:19). "
                               "The feeding of the 5,000 extends this: the one who provides bread in the "
                               "wilderness is the one who rained manna from heaven -- YHWH himself (Exod 16:4). "
                               "The crowd sees Moses; Jesus reveals YHWH.",

        "sections": [
            {
                "heading": "The Third Sign: Healing at Bethesda -- Sabbath Lord (5:1-15)",
                "body": "At the Pool of Bethesda in Jerusalem -- archaeologically confirmed with its five "
                        "porticoes (5:2) -- Jesus finds a man paralyzed for 38 years (5:5). The number "
                        "echoes Israel's 38 years of wilderness wandering after Kadesh-Barnea (Deut 2:14). "
                        "Jesus asks: 'Do you want to be healed (theleis hygies genesthai)?' (5:6). The man "
                        "gives excuses about having no one to put him in the pool (5:7). Jesus bypasses the "
                        "pool entirely: 'Get up, take up your bed, and walk (egeire, aron ton krabatton "
                        "sou kai peripatei)' (5:8). The man is healed instantly (eutheos -- 5:9). The "
                        "healing occurs on the Sabbath, and the authorities confront the man for carrying "
                        "his bed (5:10). When they learn Jesus did this, the confrontation escalates: 'This "
                        "was why the Jews were persecuting Jesus, because he was doing these things on the "
                        "Sabbath' (5:16). Jesus' response detonates a theological explosion: 'My Father is "
                        "working until now, and I am working' (5:17). The rabbinic tradition acknowledged "
                        "that God works on the Sabbath (sustaining life, judging the dead). Jesus claims "
                        "the same continuous divine activity -- not 'God is working and I serve him,' but "
                        "'My Father is working and I am working.' The authorities understand perfectly: "
                        "'he was making himself equal with God (ison heauto poion to theo)' (5:18). [A]"
            },
            {
                "heading": "The Divine Prerogative Discourse -- Life, Judgment, Honor (5:19-30)",
                "body": "The discourse following the Bethesda healing is the most systematic statement of "
                        "Jesus' divine authority in the Gospels. Five claims, each asserting a prerogative "
                        "that the OT reserves for YHWH alone: (1) Imitative sovereignty: 'The Son can do "
                        "nothing of his own accord, but only what he sees the Father doing. For whatever "
                        "the Father does, that the Son does likewise (homoios)' (5:19). This is not "
                        "limitation but identification -- the Son's actions perfectly mirror the Father's "
                        "because they share the same nature. (2) Life-giving: 'As the Father raises the "
                        "dead and gives them life (zoopoiei), so also the Son gives life to whom he will "
                        "(hous thelei)' (5:21). Only YHWH raises the dead (Deut 32:39; 1 Sam 2:6). (3) "
                        "Judgment: 'The Father judges no one, but has given all judgment (ten krisin pasan) "
                        "to the Son' (5:22). YHWH is the judge of all the earth (Gen 18:25; Ps 96:13); "
                        "that authority now belongs to the Son. (4) Equal honor: 'That all may honor "
                        "(timosin) the Son just as (kathos) they honor the Father. Whoever does not honor "
                        "the Son does not honor the Father who sent him' (5:23). YHWH declares: 'My glory "
                        "I will not give to another' (Isa 42:8) -- yet the Son receives equal honor. (5) "
                        "Life-in-himself: 'As the Father has life in himself (zoen en heauto), so he has "
                        "granted the Son also to have life in himself' (5:26). Self-existent life is the "
                        "defining attribute of deity. The Son possesses it. [A]"
            },
            {
                "heading": "The Fourth Sign: Feeding the 5,000 -- Bread from Heaven (6:1-14)",
                "body": "The fourth sign occurs near the Sea of Galilee at Passover (6:4) -- a detail that "
                        "connects the feeding to the Exodus. Jesus tests Philip: 'Where are we to buy "
                        "bread, so that these people may eat?' (6:5). Philip calculates: '200 denarii would "
                        "not buy enough bread for each of them to get a little' (6:7). Andrew finds a boy "
                        "with five barley loaves (artous krithinous -- 6:9; barley was the poor person's "
                        "grain; cf. 2 Kgs 4:42-44 where Elisha feeds 100 with 20 barley loaves) and two "
                        "fish. Jesus gives thanks (eucharistesas -- 6:11; the word that will name the "
                        "Christian meal) and distributes to the seated crowd. 'They all ate and were "
                        "satisfied (eneplesthesan)' (6:12), and twelve baskets (dodexa kophinous) of "
                        "fragments remain -- one for each tribe of Israel. The sign deliberately parallels "
                        "the manna: wilderness setting, Passover timing, miraculous bread provision, "
                        "abundant surplus. But Jesus is not Moses -- he is the source Moses pointed to. "
                        "In 6:32 he will clarify: 'It was not Moses who gave you the bread from heaven, "
                        "but my Father gives you the true bread from heaven.' The crowd's response: 'This "
                        "is indeed the Prophet (ho prophetes) who is to come into the world!' (6:14) -- "
                        "the Deuteronomy 18 expectation. They try to 'take him by force to make him king' "
                        "(6:15), but Jesus withdraws. They want a bread-king; he is the bread itself. [A]"
            },
            {
                "heading": "I Am the Bread of Life -- The Discourse That Divided (6:22-59)",
                "body": "The feeding sign leads to the Bread of Life discourse, where Jesus interprets the "
                        "sign's meaning. The crowd wants more bread (6:26). Jesus redirects: 'Do not work "
                        "for the food that perishes, but for the food that endures to eternal life, which "
                        "the Son of Man will give to you' (6:27). They ask for a sign like the manna "
                        "(6:31). Jesus corrects: 'My Father gives you the true bread from heaven. For the "
                        "bread of God (ho artos tou theou) is he who comes down from heaven and gives life "
                        "to the world (to kosmo)' (6:32-33). Then the first of the seven I AM statements "
                        "with a predicate: 'I am the bread of life (ego eimi ho artos tes zoes). Whoever "
                        "comes to me shall not hunger, and whoever believes in me shall never thirst' "
                        "(6:35). [A] The claim escalates: 'I am the living bread (ho artos ho zon) that "
                        "came down from heaven. If anyone eats of this bread, he will live forever. And the "
                        "bread that I will give for the life of the world is my flesh (sarx)' (6:51). The "
                        "discourse reaches its most offensive point: 'Unless you eat the flesh (sarka) of "
                        "the Son of Man and drink his blood (haima), you have no life in you' (6:53). Many "
                        "disciples find this intolerable and leave (6:66). Jesus asks the Twelve: 'Do you "
                        "want to go away as well?' Peter answers: 'Lord, to whom shall we go? You have the "
                        "words of eternal life (rhemata zoes aioniou), and we have believed, and have come "
                        "to know, that you are the Holy One of God (ho hagios tou theou)' (6:68-69). The "
                        "sign divides: some see bread; Peter sees the Holy One. [A]"
            }
        ]
    },

    {
        "id": "john-seven-signs-03",
        "ref": "John 6:16-21, 9:1-41",
        "chapter_num": 3,
        "title": "The Fifth and Sixth Signs -- Walking on Water and Healing the Blind Man",
        "era": "john_seven_signs",
        "type": "chapter",
        "themes": ["DC", "GLORY", "KING", "TYPE", "REBEL"],

        "synopsis": "The fifth and sixth signs each pair a miraculous act with an ego eimi declaration. "
                    "Walking on the sea (6:16-21): the disciples are rowing across the Sea of Galilee in "
                    "darkness when Jesus comes to them 'walking on the sea (peripatonta epi tes thalasses)' "
                    "(6:19). They are terrified. Jesus says: 'It is I; do not be afraid (ego eimi, me "
                    "phobeisthe)' (6:20). The ego eimi here operates on two levels: the mundane 'It's me' "
                    "and the divine 'I AM' -- because walking on the sea is an exclusively divine "
                    "prerogative in the OT. 'He alone stretches out the heavens and treads on the waves "
                    "of the sea (draka thalasses)' (Job 9:8 LXX). 'Your way was through the sea, your "
                    "path through the great waters' (Ps 77:19). Only YHWH walks on water. Healing the man "
                    "born blind (9:1-41): Jesus declares 'I am the light of the world (ego eimi to phos "
                    "tou kosmou)' (9:5) and then demonstrates it by giving sight to a man blind from birth. "
                    "The healing method -- making mud (pelos) with saliva and spreading it on the man's "
                    "eyes -- echoes Genesis 2:7, where God formed man from the dust (aphar/chous). This "
                    "is a new creation act: the Logos who made eyes in the first creation now creates "
                    "functional eyes in a man who never had them. The Pharisees investigate, interrogate, "
                    "and ultimately excommunicate the healed man. Jesus finds him and asks: 'Do you believe "
                    "in the Son of Man?' The man worships (prosekunesen -- 9:38). The sign forces the "
                    "division: the physically blind receive sight; the spiritually 'seeing' become blind.",

        "key_verse": {
            "ref": "John 6:20",
            "text": "But he said to them, 'It is I; do not be afraid.'",
            "translation": "ESV"
        },

        # NOTE: These are Greek (NT) terms — field name is a known schema limitation
        "hebrew_terms": [
            "ego eimi (I AM -- 6:20; on the surface, 'It is I'; but in the context of walking on "
            "water -- a divine prerogative (Job 9:8; Ps 77:19; Isa 43:16) -- the phrase carries "
            "the full weight of the divine name revealed at the burning bush (Exod 3:14, ehyeh "
            "asher ehyeh); the LXX renders Exod 3:14 as ego eimi ho on, 'I am the one who is')",
            "peripateo epi tes thalasses (walking on the sea -- from peripateo, 'to walk about'; "
            "epi tes thalasses, 'upon the sea'; in Job 9:8 LXX, this is attributed to God alone: "
            "ho tanaon ton ouranon monos kai peripateo hos ep edaphous epi thalasses, 'who alone "
            "stretches out the heavens and walks on the sea as on dry ground')",
            "phos tou kosmou (light of the world -- 9:5; cf. 8:12; phos = light, kosmos = world; "
            "Jesus claims to be the cosmic light that Genesis 1:3 brought into existence -- but "
            "he is not the created light; he is the source of all light, the one who said 'Let "
            "there be light')",
            "pelos (mud/clay -- 9:6; Jesus makes mud from saliva and ground, echoing Gen 2:7 where "
            "God formed adam from adamah; a new-creation act: the Logos who made humanity from dust "
            "now heals with dust, demonstrating Creator authority)",
            "prosekunesen (worshiped -- 9:38; from proskyneo, 'to bow down/worship'; the healed "
            "man worships Jesus; in the OT, proskyneo directed at anyone other than YHWH is "
            "idolatry; Jesus accepts it because he IS the one to whom worship belongs)"
        ],

        "ane_backdrop": "The sea in ANE cosmology represented chaos, danger, and the domain of hostile "
                        "cosmic powers. In Ugaritic mythology, Yamm (Sea) was the chaos deity whom Baal "
                        "defeated. In Babylonian mythology, Tiamat (the saltwater chaos monster) was slain "
                        "by Marduk to create the world. In the OT, YHWH's mastery over the sea is a "
                        "recurring demonstration of divine sovereignty: he split the Red Sea (Exod 14), "
                        "he 'rebuked the Red Sea and it dried up' (Ps 106:9), he 'trampled the waves of "
                        "the sea' (Job 9:8). When Jesus walks on the water, he performs an act that the "
                        "ANE worldview universally recognized as the exclusive prerogative of the supreme "
                        "deity -- dominion over the chaos waters. The blind-man healing has parallels to "
                        "ANE creation accounts where a deity forms humanity from clay or earth. Jesus "
                        "making mud and forming functional eyes replicates the Creator's original act in "
                        "Genesis 2:7 -- he is not healing so much as re-creating.",

        "second_temple": [
            {
                "source": "Psalm 77:16-19 (a Psalm of Asaph)",
                "summary": "'The waters saw you, O God, the waters saw you; they were afraid... Your way "
                           "was through the sea, your path through the great waters, yet your footprints "
                           "were unseen.'",
                "relevance": "The psalm describes YHWH's invisible passage through the sea waters. Jesus "
                             "makes this visible: he literally walks on the water, visibly doing what the "
                             "psalm attributes to YHWH. The 'unseen footprints' become seen."
            },
            {
                "source": "Job 9:8 (LXX translation)",
                "summary": "'He alone stretched out the heavens and walks upon the sea as on dry ground' "
                           "(ho peripateon epi thalasses hos epi edaphous).",
                "relevance": "This is the most direct OT parallel to John 6:16-21. Job attributes walking "
                             "on the sea exclusively to God. When Jesus does it, the divine identity claim "
                             "is unmistakable -- especially when accompanied by ego eimi (6:20)."
            },
            {
                "source": "Isaiah 35:5-6 (the eschatological healing oracle)",
                "summary": "'Then the eyes of the blind shall be opened, and the ears of the deaf unstopped; "
                           "then shall the lame man leap like a deer, and the tongue of the mute sing for joy.'",
                "relevance": "Isaiah associates the healing of blindness with the messianic age when YHWH "
                             "himself comes: 'Say to those who have a fearful heart, Be strong; fear not! "
                             "Behold, your God will come' (Isa 35:4). The healing of the man born blind "
                             "signals: your God has come."
            }
        ],

        "cross_refs": [
            {"ref": "Job 9:8", "note": "'He alone stretches out the heavens and treads on the waves of the sea' -- walking on water is YHWH's exclusive prerogative; Jesus does it", "type": "ot"},
            {"ref": "Psalm 77:19", "note": "'Your way was through the sea, your path through the great waters, yet your footprints were unseen' -- YHWH's passage through the sea, made visible in Jesus", "type": "ot"},
            {"ref": "Exodus 3:14", "note": "'I AM WHO I AM (ehyeh asher ehyeh)' -- the divine name behind Jesus' ego eimi on the water (6:20)", "type": "ot"},
            {"ref": "Isaiah 35:4-6", "note": "'Behold, your God will come... then the eyes of the blind shall be opened' -- the healing of blindness signals YHWH's arrival", "type": "ot"},
            {"ref": "Genesis 2:7", "note": "'The LORD God formed the man of dust from the ground' -- Jesus making mud to give sight echoes the original creation of humanity from earth", "type": "ot"},
            {"ref": "Isaiah 42:6-7", "note": "'I will give you as a covenant for the people, a light for the nations, to open the eyes that are blind' -- the Servant's mission fulfilled in the sixth sign", "type": "ot"},
            {"ref": "Mark 6:45-52", "note": "The Synoptic account of walking on water -- Mark adds that 'they were utterly astounded, for they did not understand about the loaves' (6:51-52)", "type": "nt"},
            {"ref": "Psalm 82:6-7", "note": "'I said, You are gods (elohim), sons of the Most High' -- Jesus quotes this in John 10:34 after the blind-man controversy, linking the sign to divine council theology", "type": "ot"}
        ],

        "divine_council_note": "These two signs make divine identity claims that no angel, no lesser elohim, "
                               "no member of the divine council could make. Walking on the sea is YHWH's "
                               "prerogative in the OT (Job 9:8; Ps 77:19; Hab 3:15; Isa 43:16). No bene "
                               "elohim, no divine council member, no Watcher, no territorial prince is ever "
                               "described as walking on water. This belongs to the Creator alone -- the one who "
                               "brought order from chaos (Gen 1:2; Ps 74:13-14), who split the sea (Exod "
                               "14:21-22), who treads on the waves (Job 9:8). When Jesus walks on the water "
                               "and says 'ego eimi,' he is claiming to be that God. The healing of the man "
                               "born blind extends the claim: Jesus performs a creative act -- forming eyes "
                               "that never existed. This goes beyond healing; it is new creation. Only the "
                               "Creator can make something from nothing. The Pharisees' response is telling: "
                               "'This man is not from God (para theou), for he does not keep the Sabbath' "
                               "(9:16). Some dissent: 'How can a man who is a sinner do such signs?' (9:16). "
                               "The division mirrors the prologue's light/darkness theme: the physically blind "
                               "man sees (both physically and spiritually -- he worships Jesus, 9:38), while "
                               "the 'seeing' Pharisees are declared blind (9:39-41). Jesus pronounces: 'For "
                               "judgment I came into this world, that those who do not see may see, and those "
                               "who see may become blind' (9:39).",

        "sections": [
            {
                "heading": "The Fifth Sign: Ego Eimi on the Chaos Waters (6:16-21)",
                "body": "As evening falls, the disciples set out across the Sea of Galilee toward Capernaum "
                        "'and it was now dark (skotia ede egegenei), and Jesus had not yet come to them' "
                        "(6:17). John's symbolism is deliberate: darkness, the absence of Jesus, and a "
                        "storm. 'The sea became rough because a strong wind was blowing (anemos megas "
                        "pneon)' (6:18). After rowing three or four miles (stadious eikosi pente e "
                        "triakonta -- 6:19), they see Jesus 'walking on the sea (peripatonta epi tes "
                        "thalasses) and coming near the boat, and they were frightened (ephobethesan)' "
                        "(6:19). In the OT, human fear in the presence of divine action is the standard "
                        "theophanic response (Exod 3:6; Isa 6:5; Dan 10:7-9). Jesus responds: 'Ego eimi; "
                        "me phobeisthe' -- 'I AM; do not be afraid' (6:20). The phrase ego eimi is the "
                        "Greek rendering of the divine name (Exod 3:14 LXX: ego eimi ho on). Combined "
                        "with walking on the sea -- which Job 9:8 reserves exclusively for God -- the "
                        "declaration is a theophany: YHWH appearing to his people on the chaos waters. "
                        "'Then they were glad to take him into the boat, and immediately (eutheos) the "
                        "boat was at the land (epi tes ges) to which they were going' (6:21). The "
                        "instantaneous arrival suggests another miracle -- the Creator who commands the "
                        "waters also commands space and time. [A]"
            },
            {
                "heading": "The Sixth Sign: Light of the World Demonstrated (9:1-12)",
                "body": "Jesus encounters 'a man blind from birth (typhlon ek genetes)' (9:1). The "
                        "disciples ask: 'Who sinned, this man or his parents, that he was born blind?' "
                        "(9:2). Jesus rejects the sin-causation framework: 'It was not that this man "
                        "sinned, or his parents, but that the works of God (ta erga tou theou) might be "
                        "displayed (phanerothei) in him' (9:3). The blindness exists so that the Creator "
                        "can display his creative power. Jesus declares: 'As long as I am in the world, "
                        "I am the light of the world (phos eimi tou kosmou)' (9:5) -- the same claim as "
                        "8:12, now backed by action. His method is extraordinary: 'He spat on the ground "
                        "(epthusen chamai) and made mud (pelos) with the saliva. Then he anointed "
                        "(epechrisen) the man's eyes with the mud' (9:6). The echo of Genesis 2:7 is "
                        "unmistakable: God formed (yatsar) the man from the dust (aphar) of the ground "
                        "(adamah). Jesus forms mud from earth and applies it to create what was never "
                        "there -- functioning eyes. This is not repair but creation. He sends the man "
                        "to 'wash in the pool of Siloam (Siloam -- which means Sent, apestalmenos)' "
                        "(9:7). The man 'went and washed and came back seeing (blepon)' (9:7). John "
                        "interprets the pool's name: 'Sent' -- the man is healed by the one who was "
                        "sent from God, the apostolos of the divine council. [A]"
            },
            {
                "heading": "The Trial of the Healed Man -- Spiritual Blindness Exposed (9:13-41)",
                "body": "The healed man is brought before the Pharisees -- and it was a Sabbath (9:14). "
                        "The pattern repeats from chapter 5: a healing on the Sabbath provokes theological "
                        "fury. The Pharisees divide: 'This man is not from God (ouk estin houtos para "
                        "theou ho anthropos), for he does not keep the Sabbath' (9:16a). Others object: "
                        "'How can a man who is a sinner (hamartolos) do such signs (semeia)?' (9:16b). "
                        "The division -- schisma (9:16) -- runs through the entire Gospel. The authorities "
                        "interrogate the man's parents (9:18-23), who confirm the blindness from birth but "
                        "refuse to explain the healing 'because they feared the Jews, for the Jews had "
                        "already agreed (sunetethento) that if anyone should confess Jesus to be the "
                        "Christ, he was to be put out of the synagogue (aposynagogos genetai)' (9:22). "
                        "The healed man is called back and pressed to deny Jesus. His response escalates "
                        "from neutrality ('He is a prophet,' 9:17) to boldness: 'If this man were not "
                        "from God (para theou), he could do nothing (ouden edynato poiein)' (9:33). They "
                        "excommunicate him (exebalon auton exo -- 9:34). Jesus finds him and asks: 'Do "
                        "you believe in the Son of Man (ton huion tou anthropou)?' (9:35). The man asks "
                        "who he is. Jesus: 'You have seen him, and it is he who is speaking to you' "
                        "(9:37). The man says: 'Lord, I believe (pisteuo, kyrie)' -- and worships him "
                        "(prosekunesen auto -- 9:38). Proskyneo directed at a human is idolatry (Acts "
                        "10:25-26; Rev 19:10; 22:8-9). Jesus accepts it. The sign's verdict: 'For "
                        "judgment I came into this world, that those who do not see may see, and those "
                        "who see may become blind' (9:39). [A]"
            }
        ]
    },

    {
        "id": "john-seven-signs-04",
        "ref": "John 11:1-44",
        "chapter_num": 4,
        "title": "The Seventh Sign -- Raising Lazarus: I Am the Resurrection and the Life",
        "era": "john_seven_signs",
        "type": "chapter",
        "themes": ["DC", "GLORY", "SEED", "BLOOD", "TYPE"],

        "synopsis": "The seventh and climactic sign is the raising of Lazarus from the dead (11:1-44) -- "
                    "the supreme demonstration that Jesus is who the prologue claims: the Logos in whom was "
                    "life (zoe, 1:4), the one who gives life to whom he will (5:21), the bread of life "
                    "that gives eternal life (6:35), the light of the world that overcomes darkness (8:12). "
                    "Lazarus has been dead four days (11:17) -- in Jewish tradition, the soul departed the "
                    "body after three days, making decomposition irreversible. Martha confesses: 'I know "
                    "that he will rise again in the resurrection at the last day' (11:24) -- standard "
                    "Pharisaic eschatology. Jesus shatters the timeline: 'I am (ego eimi) the resurrection "
                    "(he anastasis) and the life (he zoe). Whoever believes in me, though he die, yet "
                    "shall he live, and everyone who lives and believes in me shall never die' (11:25-26). "
                    "The resurrection is not an event in the future; it is a person standing in front of "
                    "her. Then: 'Jesus wept (edakrysen ho Iesous)' (11:35) -- the shortest verse in the "
                    "Bible and one of the most profound: the Logos who created all things, who has life in "
                    "himself, who will raise Lazarus in moments, weeps at the tomb. The Creator grieves "
                    "over the destruction wrought by sin and death in his creation. At the tomb: 'Lazarus, "
                    "come out (Lazare, deuro exo)!' (11:43). The dead man walks out, still wrapped in "
                    "burial cloths. The sign that triggers the plot to kill Jesus (11:47-53) -- the one "
                    "who gives life becomes the target of those who deal death.",

        "key_verse": {
            "ref": "John 11:25-26",
            "text": "Jesus said to her, 'I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live, and everyone who lives and believes in me shall never die. Do you believe this?'",
            "translation": "ESV"
        },

        # NOTE: These are Greek (NT) terms — field name is a known schema limitation
        "hebrew_terms": [
            "anastasis (resurrection -- from ana + histemi, 'to stand up again'; the bodily raising "
            "from death; in Jewish eschatology (Dan 12:2), resurrection occurs at the end of the age; "
            "Jesus claims to BE the resurrection -- the eschatological power is not an event but a "
            "person; he does not merely raise the dead -- he IS the resurrection itself)",
            "zoe (life -- the divine quality of life that belongs to God alone; paired with anastasis "
            "in 11:25 to create a comprehensive claim: Jesus is both the power that raises the dead "
            "AND the life that sustains the raised forever; cf. 1:4 'In him was life')",
            "edakrysen (wept -- 11:35; from dakryo, 'to shed tears'; distinct from klaio, the "
            "loud wailing of the mourners (11:33); Jesus' weeping is quiet, deep grief; the "
            "incarnate Logos experiencing genuine human sorrow at the ruin of death in his creation)",
            "enebrimesato (deeply moved/indignant -- 11:33, 38; from embrimaomai, a strong word "
            "meaning 'to snort with anger' or 'to be deeply agitated'; not merely sad but angry -- "
            "the Creator confronting the enemy, death, that has invaded his creation)",
            "deuro exo (come out/come forth -- 11:43; the creative command of the Logos; the same "
            "Word who spoke creation into existence (1:3; Gen 1:3) now speaks life into a corpse; "
            "the voice that created the universe commands the dead to live)",
            "keiriai (burial strips/wrappings -- 11:44; the linen strips wound around the corpse; "
            "Lazarus emerges still bound -- he is raised but not yet glorified; contrast with "
            "Jesus' resurrection where the burial cloths are left behind (20:6-7))"
        ],

        "ane_backdrop": "Raising the dead was the supreme demonstration of divine power in the ancient Near "
                        "East. In the Ugaritic Baal Cycle, Mot (Death) swallows Baal, and Baal's return "
                        "from the underworld signals the restoration of fertility and life. In Mesopotamian "
                        "mythology, Inanna/Ishtar descends to the underworld and must be rescued. In the OT, "
                        "only YHWH has power over death: 'I kill and I make alive (ani amit va'achayeh); I "
                        "wound and I heal' (Deut 32:39). 'The LORD kills and brings to life; he brings down "
                        "to Sheol and raises up' (1 Sam 2:6). The prophets performed resurrections (Elijah "
                        "in 1 Kgs 17:17-24; Elisha in 2 Kgs 4:18-37), but always by prayer -- calling on "
                        "YHWH's power. Jesus does not pray for Lazarus's resurrection; he commands it by his "
                        "own authority: 'Lazarus, come out!' The distinction is enormous: the prophets were "
                        "mediators; Jesus is the source. He IS the resurrection and the life.",

        "second_temple": [
            {
                "source": "Daniel 12:2",
                "summary": "'Many of those who sleep in the dust of the earth shall awake, some to "
                           "everlasting life (chayyei olam), and some to shame and everlasting contempt.'",
                "relevance": "Martha expresses the standard Pharisaic hope based on Daniel 12:2: 'I know "
                             "that he will rise again in the resurrection at the last day' (11:24). Jesus "
                             "transforms eschatological hope into present reality: the resurrection is not "
                             "just a future event -- it is a person standing before her."
            },
            {
                "source": "2 Maccabees 7:9, 14 (~124 BC)",
                "summary": "The seven brothers martyred by Antiochus express confidence in resurrection: "
                           "'The King of the universe will raise us up to an everlasting renewal of life.'",
                "relevance": "Second Temple martyrology texts show resurrection hope was widespread in "
                             "pre-Christian Judaism. The Lazarus miracle demonstrates that this hope is "
                             "grounded in a person who has power over death now, not merely at the eschaton."
            },
            {
                "source": "Ezekiel 37:1-14 (the valley of dry bones)",
                "summary": "'Thus says the Lord GOD to these bones: Behold, I will cause breath (ruach) "
                           "to enter you, and you shall live... I will put my Spirit within you, and you "
                           "shall live.'",
                "relevance": "Ezekiel's vision of corporate resurrection -- YHWH breathing life into dead "
                             "bones -- is enacted in miniature at Lazarus's tomb. Jesus speaks and the dead "
                             "live. The one who promised resurrection in Ezekiel 37 is the one performing "
                             "it in John 11."
            },
            {
                "source": "1 Enoch 51:1 (~2nd century BC)",
                "summary": "'In those days, Sheol will return all the deposits that she has received, and "
                           "Hell will give back all that it owes. And he will choose the righteous and the "
                           "holy ones from among them.'",
                "relevance": "According to 1 Enoch, resurrection belongs to the eschatological judgment. "
                             "Jesus' raising of Lazarus brings this eschatological reality into the present: "
                             "the one who will command Sheol to release the dead at the end is commanding "
                             "a tomb to release Lazarus now."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:39", "note": "'I kill and I make alive (ani amit va'achayeh)' -- YHWH's exclusive authority over life and death, claimed by Jesus in raising Lazarus", "type": "ot"},
            {"ref": "1 Samuel 2:6", "note": "'The LORD kills and brings to life; he brings down to Sheol and raises up' -- Hannah's song attributes resurrection power to YHWH alone", "type": "ot"},
            {"ref": "Ezekiel 37:1-14", "note": "'I will cause breath to enter you, and you shall live' -- YHWH's promise of resurrection, enacted at Lazarus's tomb by the incarnate Logos", "type": "ot"},
            {"ref": "Daniel 12:2", "note": "'Many who sleep in the dust shall awake' -- the eschatological resurrection Martha hoped for (11:24) that Jesus makes present in his person", "type": "ot"},
            {"ref": "1 Kings 17:17-24", "note": "Elijah raises the widow's son by crying out to YHWH -- a prophet mediating God's power; Jesus raises Lazarus by his own command, not prayer", "type": "ot"},
            {"ref": "Romans 6:5-11", "note": "'If we have been united with him in a death like his, we shall certainly be united with him in a resurrection like his' -- Paul builds on the resurrection-through-Christ theology", "type": "nt"},
            {"ref": "1 Corinthians 15:20-23", "note": "'Christ has been raised from the dead, the firstfruits of those who have fallen asleep' -- the Lazarus miracle prefigures the universal resurrection Christ inaugurates", "type": "nt"},
            {"ref": "Revelation 1:17-18", "note": "'Fear not, I am the first and the last, and the living one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades'", "type": "nt"},
            {"ref": "1 Enoch 51:1", "note": "'Sheol will return all the deposits she has received' -- the eschatological hope of Enoch, enacted proleptically at Lazarus's tomb", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "The raising of Lazarus is the ultimate divine council statement in the Book of "
                               "Signs. In the OT divine council framework, YHWH alone has authority over death "
                               "and Sheol: 'I kill and I make alive' (Deut 32:39). The bene elohim, the "
                               "territorial princes, the angelic hosts -- none of them can raise the dead. Even "
                               "Satan, the most powerful hostile spiritual being, cannot create life; he can "
                               "only corrupt and destroy it. Death is the domain that only the Creator can "
                               "enter and reverse. When Jesus stands at Lazarus's tomb and commands a four-day "
                               "corpse to live, he exercises the prerogative that the entire OT reserves for "
                               "YHWH. But notice what precedes the command: 'Jesus, deeply moved (enebrimesato) "
                               "again' (11:38). The verb embrimaomai suggests anger, not just grief. The Logos "
                               "who created life (1:3-4) is confronting the enemy that has invaded his creation. "
                               "Death was not part of the original design (Gen 1:31 -- 'very good'); it entered "
                               "through the nachash's rebellion in Eden (Gen 3:19; Rom 5:12). The Creator's "
                               "anger at the tomb is the anger of a king surveying the damage done by an enemy "
                               "in his territory. The command 'Lazarus, come out!' is the Creator's authority "
                               "exercised against the last enemy (1 Cor 15:26). The sign triggers the plot to "
                               "kill Jesus (11:47-53) -- the supreme irony of John's Gospel: the one who IS "
                               "the resurrection and the life is condemned to death by those who witnessed him "
                               "conquer death. Caiaphas unwittingly prophesies: 'It is better for you that one "
                               "man should die for the people' (11:50). John comments: 'He did not say this of "
                               "his own accord' (11:51) -- the high priest becomes an unwitting mouthpiece of "
                               "the divine council's redemptive plan.",

        "sections": [
            {
                "heading": "The Setup: Lazarus Is Dead, and Jesus Waits (11:1-16)",
                "body": "The scene opens in Bethany, near Jerusalem, where Lazarus is ill (11:1). His sisters "
                        "Mary and Martha send word to Jesus: 'Lord, he whom you love (phileis) is ill' "
                        "(11:3). Jesus' response is startling: 'This illness does not lead to death (ouk "
                        "estin pros thanaton). It is for the glory (hyper tes doxes) of God, so that the "
                        "Son of God may be glorified (doxasthe) through it' (11:4). Then: 'Jesus loved "
                        "(egapa) Martha and her sister and Lazarus. So, when he heard that Lazarus was ill, "
                        "he stayed two days longer (emeinen... duo hemeras) in the place where he was' "
                        "(11:5-6). The word 'so' (oun) is crucial: it connects the love to the delay. Jesus "
                        "waits BECAUSE he loves them -- not despite it. The delay ensures Lazarus will be "
                        "dead four days (11:17), past the point of any natural recovery or resuscitation "
                        "claim. After two days, Jesus tells the disciples: 'Lazarus has fallen asleep "
                        "(kekoimetai), but I go to awaken (exypniso) him' (11:11). The disciples misunderstand: "
                        "'if he has fallen asleep, he will recover' (11:12). Jesus speaks plainly: 'Lazarus "
                        "has died (apethanen), and for your sake I am glad (chairo) that I was not there, "
                        "so that you may believe (pisteusete)' (11:14-15). Thomas, with dark courage: "
                        "'Let us also go, that we may die with him' (11:16). The stage is set for the "
                        "supreme sign. [A]"
            },
            {
                "heading": "Ego Eimi He Anastasis Kai He Zoe -- The Fifth I AM Statement (11:17-27)",
                "body": "Jesus arrives to find Lazarus has been in the tomb four days (11:17). In Jewish "
                        "tradition, the soul was believed to hover near the body for three days, making "
                        "the fourth day the point of no return -- irreversible death, unmistakable "
                        "decomposition. Martha meets Jesus: 'Lord, if you had been here, my brother would "
                        "not have died' (11:21) -- a statement of faith in Jesus' healing power, but limited "
                        "to prevention, not reversal. She adds: 'But even now I know that whatever you ask "
                        "from God, God will give you' (11:22) -- still thinking of Jesus as a mediator who "
                        "petitions God. Jesus: 'Your brother will rise again' (11:23). Martha defaults to "
                        "standard eschatology: 'I know that he will rise again in the resurrection at the "
                        "last day' (11:24). Then Jesus speaks the fifth ego eimi with predicate: 'I AM "
                        "(ego eimi) the resurrection (he anastasis) and the life (he zoe). Whoever believes "
                        "in me, though he die, yet shall he live (zesetai), and everyone who lives and "
                        "believes in me shall never die (ou me apothane eis ton aiona)' (11:25-26). The "
                        "claim shatters the eschatological timeline: the resurrection is not a distant "
                        "event -- it is a person standing before her. The power of life and death resides "
                        "in HIM. Martha's confession: 'Yes, Lord; I believe that you are the Christ "
                        "(ho Christos), the Son of God (ho huios tou theou), who is coming into the world "
                        "(ho eis ton kosmon erchomenos)' (11:27) -- a triple confession matching the "
                        "Gospel's stated purpose (20:31). [A]"
            },
            {
                "heading": "Jesus Wept -- The Creator Confronts the Enemy (11:28-37)",
                "body": "Mary comes to Jesus and falls at his feet with the same words as Martha: 'Lord, "
                        "if you had been here, my brother would not have died' (11:32). Jesus sees her "
                        "weeping (klaiousan) and the Jews with her weeping (klaiontas), and he is 'deeply "
                        "moved in his spirit (enebrimesato to pneumati) and greatly troubled (etaraxen "
                        "heauton)' (11:33). The verb embrimaomai is intense -- it can mean 'to snort with "
                        "anger' or 'to be deeply agitated.' Some scholars translate it as indignation or "
                        "fury. The Logos is not merely sympathetic; he is angry. Angry at what? At death "
                        "itself -- the intruder in his creation, the consequence of the nachash's lie in "
                        "Eden, the corruption that has turned his 'very good' creation into a place of "
                        "tombs and tears. 'Where have you laid him?' (11:34). 'Lord, come and see' (11:34). "
                        "Then: 'Jesus wept (edakrysen ho Iesous)' (11:35). The verb dakryo describes quiet "
                        "tears, distinct from the loud wailing (klaio) of the mourners. The incarnate "
                        "Logos -- the one through whom all things were made (1:3), who has life in himself "
                        "(5:26), who will speak Lazarus out of the grave in moments -- weeps. Not because "
                        "he cannot fix the problem, but because the problem should never have existed. "
                        "The Creator grieves over the ruin of his creation. [A] The crowd's divided "
                        "response: 'See how he loved him!' (11:36) -- some see love. Others: 'Could not "
                        "he who opened the eyes of the blind man also have kept this man from dying?' "
                        "(11:37) -- some see failure. The light shines; the responses diverge. [B]"
            },
            {
                "heading": "Lazare, Deuro Exo -- The Voice That Commands the Dead (11:38-44)",
                "body": "At the tomb -- a cave with a stone across its entrance (11:38) -- Jesus is again "
                        "'deeply moved (embrimomenos)' (11:38). The anger returns. He orders: 'Take away "
                        "the stone (arate ton lithon)' (11:39). Martha objects: 'Lord, by this time there "
                        "will be an odor (oze), for he has been dead four days (tetartaios gar estin)' "
                        "(11:39). The Greek oze is blunt: he stinks. Decomposition is advanced. Jesus "
                        "responds: 'Did I not tell you that if you believed you would see the glory "
                        "(doxan) of God?' (11:40). The stone is removed. Jesus lifts his eyes and prays "
                        "-- not for power to raise Lazarus, but for the crowd's sake: 'Father, I thank "
                        "you that you have heard me. I knew that you always hear me, but I said this on "
                        "account of the people standing around, that they may believe that you sent me' "
                        "(11:41-42). The prayer is not petition but testimony: the Father and Son are "
                        "already aligned. Then the command: 'Lazarus, come out! (Lazare, deuro exo!)' "
                        "(11:43). He cried out 'with a loud voice (phone megale)' -- the same creative "
                        "voice that spoke the universe into existence (1:3; Gen 1:3). 'The man who had "
                        "died came out (exelthen ho tethnekos), his hands and feet bound with linen "
                        "strips (keiriais), and his face wrapped with a cloth (soudarion)' (11:44). A "
                        "four-day corpse walks. The Creator has commanded death to release its prisoner, "
                        "and death obeyed. 'Unbind him, and let him go (lysate auton kai aphete auton "
                        "hypagein)' (11:44). The seventh sign is complete: the Logos who IS the "
                        "resurrection and the life has demonstrated it before witnesses. [A]"
            },
            {
                "heading": "The Irony: The Life-Giver Condemned to Death (11:45-53)",
                "body": "The sign produces the expected division: 'Many of the Jews therefore, who had "
                        "come with Mary and had seen what he did, believed in him (episteusan eis auton)' "
                        "(11:45). But others report to the Pharisees (11:46). The chief priests and "
                        "Pharisees convene the Sanhedrin (synedrion -- 11:47): 'What are we to do? For "
                        "this man performs many signs (semeia polla poiei)' (11:47). They do not deny the "
                        "signs -- they cannot. Their concern is political: 'If we let him go on like this, "
                        "everyone will believe in him, and the Romans will come and take away both our "
                        "place (topon -- the Temple) and our nation (ethnos)' (11:48). Caiaphas, the high "
                        "priest, delivers the verdict: 'You know nothing at all. Nor do you understand "
                        "that it is better for you that one man should die for the people (hyper tou "
                        "laou), not that the whole nation should perish (apoletai)' (11:49-50). John "
                        "provides the theological commentary: 'He did not say this of his own accord "
                        "(aph heautou ouk eipen), but being high priest that year he prophesied "
                        "(epropheteuson) that Jesus would die for the nation, and not for the nation "
                        "only, but also to gather into one (synagage eis hen) the children of God who "
                        "are scattered abroad (ta tekna tou theou ta dieskorpismena)' (11:51-52). The "
                        "high priest unwittingly speaks the divine council's plan: the death of the Logos "
                        "will reverse the scattering of the nations at Babel (Gen 11; Deut 32:8) and "
                        "gather the scattered children of God from every nation. From that day, 'they "
                        "made plans to put him to death (ebouleusanto hina apokteinosin auton)' (11:53). "
                        "The supreme irony: the one who IS the resurrection is sentenced to die by those "
                        "who witnessed him conquer death. [A]"
            }
        ]
    }
]
