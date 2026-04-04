"""
era_john_signs.py -- The Book of Signs (John 1-12)

The first half of John's Gospel is traditionally called the "Book of Signs"
because it is structured around seven miraculous signs (semeia) that reveal
Jesus' glory. But the signs are only the surface structure. Beneath them
lies the most sustained christological argument in the New Testament: Jesus
is the pre-existent Logos who created all things (1:1-3), who descended from
heaven (3:13), who bears the divine name "I AM" (8:58), who exercises the
divine prerogatives of judgment and life-giving (5:21-27), who quotes Psalm
82 to defend his claim to be the Son of God (10:34-36), and who is the
fulfillment of every major Old Testament institution -- the Temple (2:19-21),
the Passover lamb (1:29), the brazen serpent (3:14), the manna (6:32-35),
the water from the rock (7:37-39), the light of the pillar of fire (8:12),
and the shepherd of Israel (10:11). The Book of Signs ends with the raising
of Lazarus (chapter 11) -- the supreme sign that Jesus is "the resurrection
and the life" (11:25) -- and the arrival of Jesus' "hour" (12:23), the
moment when the Son of Man will be "lifted up" (12:32) and the ruler of
this world will be cast out (12:31).
"""

CHAPTERS = [
    {
        "id": "john-1",
        "ref": "John 1",
        "chapter_num": 1,
        "title": "The Logos Prologue and the First Witnesses -- In the Beginning Was the Word",
        "era": "john_signs",
        "type": "chapter",
        "themes": ["SEED", "DC", "GLORY", "BLOOD", "KING"],

        "synopsis": "John 1 is the most theologically dense chapter in the New Testament. It opens not "
                    "with a genealogy (Matthew), a Roman census (Luke), or the beginning of the ministry "
                    "(Mark), but with the beginning of everything: 'In the beginning (en arche) was the "
                    "Word (ho logos), and the Word was with God (pros ton theon), and the Word was God "
                    "(theos en ho logos)' (1:1). The echo of Genesis 1:1 ('In the beginning, God created "
                    "the heavens and the earth') is deliberate -- John is telling the creation story "
                    "again, but now revealing the hidden actor: the Word who was the agent of all "
                    "creation. 'All things were made through him, and without him was not any thing made "
                    "that was made' (1:3). The Word is not a created being; he is the Creator. In him "
                    "was life (zoe), and the life was the light (phos) of men (1:4). The light shines "
                    "in the darkness (skotia), and the darkness has not overcome (katelaben) it (1:5). "
                    "John the Baptist is introduced as a witness to the light -- 'he was not the light, "
                    "but came to bear witness about the light' (1:8). The true light that gives light "
                    "to everyone was coming into the world (1:9). 'He was in the world, and the world "
                    "was made through him, yet the world did not know him. He came to his own (ta idia), "
                    "and his own people (hoi idioi) did not receive him' (1:10-11). But to all who "
                    "received him, he gave the right to become children of God (tekna theou) -- those "
                    "born not of blood, nor of the will of the flesh, nor of the will of man, but of "
                    "God (1:12-13). Then the climax: 'And the Word became flesh (ho logos sarx egeneto) "
                    "and dwelt (eskenosen -- tabernacled) among us, and we have seen his glory (doxa), "
                    "glory as of the only Son (monogenes) from the Father, full of grace (charis) and "
                    "truth (aletheia)' (1:14). The prologue ends: 'No one has ever seen God; the only "
                    "God (monogenes theos), who is at the Father's side, he has made him known "
                    "(exegesato)' (1:18). The rest of the chapter narrates the Baptist's testimony "
                    "('Behold, the Lamb of God, who takes away the sin of the world!' -- 1:29), the "
                    "calling of the first disciples (Andrew, Peter, Philip, Nathanael), and the promise "
                    "to Nathanael: 'You will see heaven opened, and the angels of God ascending and "
                    "descending on the Son of Man' (1:51) -- Jacob's ladder fulfilled in Christ.",

        "key_verse": {
            "ref": "John 1:1, 14",
            "text": "In the beginning was the Word, and the Word was with God, and the Word was God... And the Word became flesh and dwelt among us, and we have seen his glory, glory as of the only Son from the Father, full of grace and truth.",
            "translation": "ESV"
        },

        "original_terms": [
            "Logos (ho logos -- the Word; Greek philosophical term for rational principle/ordering intelligence, "
            "but John's usage draws on the Hebrew dabar YHWH -- the creative, active word of God that "
            "accomplishes his purposes; Gen 1:3; Ps 33:6; Isa 55:11; also the Aramaic memra of the Targums)",
            "pros ton theon (with God -- the preposition pros means 'toward' or 'face-to-face with,' implying "
            "a personal, relational distinction between the Word and God; not mere proximity but intimate "
            "communion -- the 'two powers in heaven')",
            "theos en ho logos (the Word was God -- theos without the article as predicate nominative describes "
            "the Word's nature; the Word is fully divine without being identical to the Father)",
            "sarx egeneto (became flesh -- not 'entered flesh' or 'put on flesh' but 'became' -- the Word "
            "took on a fully human nature; the incarnation)",
            "eskenosen (tabernacled/dwelt -- from skene, 'tent/tabernacle'; the Word pitched his tent among "
            "us like the Shekinah glory in the Tabernacle; Exod 40:34-35)",
            "monogenes (only-begotten/unique -- from monos + genos, 'one of a kind'; the Son's unique "
            "relationship to the Father, unlike any other being in the divine council)",
            "exegesato (made known/exegeted -- the Word is the exegete of the invisible God; he 'narrates' "
            "God to humanity; the source of the English word 'exegesis')",
            "ho amnos tou theou (the Lamb of God -- 1:29, 36; the Passover lamb whose blood delivers from "
            "death; Exod 12:1-13; Isa 53:7)"
        ],

        "ane_backdrop": "The concept of a divine 'word' as the agent of creation has deep roots in the "
                        "ancient Near East. In Egyptian theology, the god Ptah created all things through "
                        "his 'heart and tongue' -- conceiving in his mind and speaking things into existence "
                        "(the Memphite Theology). In Mesopotamian creation accounts, Marduk's word has "
                        "creative power: 'He spoke, and the garment was destroyed; he spoke again, and the "
                        "garment was restored' (Enuma Elish IV.19-26). The Genesis 1 creation account uses "
                        "this ANE pattern but applies it exclusively to YHWH: 'And God said... and it was "
                        "so.' John's prologue takes this further: the creative 'word' of God is not merely "
                        "speech but a person -- the Logos who was 'with God' and 'was God' before anything "
                        "was made. The angels 'ascending and descending on the Son of Man' (1:51) echoes "
                        "the widespread ANE concept of divine messengers traveling between the heavenly "
                        "court and the earthly realm -- but now the stairway is not a location (Bethel) "
                        "but a person (the Son of Man).",

        "second_temple": [
            {
                "source": "Philo of Alexandria, On the Creation (De Opificio Mundi)",
                "summary": "Philo describes the Logos as God's 'firstborn son,' the instrument through "
                           "which God created the world, the 'image (eikon) of God,' and the mediator "
                           "between the transcendent God and the material world.",
                "relevance": "Philo demonstrates that first-century Hellenistic Jews were already thinking "
                             "about the Logos as a divine intermediary. John's prologue both draws on and "
                             "transcends Philo: John's Logos is not a philosophical abstraction but a "
                             "person who 'became flesh.'"
            },
            {
                "source": "Targum Neofiti on Genesis 1:1",
                "summary": "The Targum renders 'In the beginning God created' as 'From the beginning "
                           "with wisdom (behokhma) the Memra (Word) of the LORD created.' The memra "
                           "is used throughout the Targums to describe God's active, personal presence.",
                "relevance": "The memra tradition shows that pre-Christian Judaism was already personalizing "
                             "God's 'Word' as a distinct agent of creation and revelation -- the conceptual "
                             "world that John's prologue inhabits."
            },
            {
                "source": "Wisdom of Solomon 18:14-16",
                "summary": "'While gentle silence enveloped all things... your all-powerful word (logos) "
                           "leaped from heaven, from the royal throne, into the midst of the land that "
                           "was doomed, a stern warrior carrying the sharp sword of your authentic command.'",
                "relevance": "The personification of God's Word as an agent who 'leaps from heaven' to act "
                             "in the world parallels John's concept of the Logos who was 'with God' and "
                             "came 'into the world.'"
            },
            {
                "source": "Colossians 1:15-17 (Paul, ~60 AD)",
                "summary": "'He is the image of the invisible God, the firstborn of all creation. For by "
                           "him all things were created, in heaven and on earth... all things were created "
                           "through him and for him. He is before all things, and in him all things hold "
                           "together.'",
                "relevance": "Paul's christological hymn parallels John's prologue: Christ as agent of "
                             "creation, pre-existent, sustainer of all things. Both draw on the same 'two "
                             "powers in heaven' theology."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 1:1-3", "note": "'In the beginning, God created... And God said, Let there be light' -- John 1:1 echoes the opening of Genesis, revealing the Word as the agent of 'God said'", "type": "ot"},
            {"ref": "Proverbs 8:22-31", "note": "Wisdom personified as present with God before creation: 'I was beside him, like a master workman' -- a precursor to the Logos concept", "type": "ot"},
            {"ref": "Psalm 33:6", "note": "'By the word (dabar) of the LORD the heavens were made, and by the breath of his mouth all their host' -- creation through the divine word", "type": "ot"},
            {"ref": "Isaiah 55:10-11", "note": "'My word that goes out from my mouth shall not return to me empty, but shall accomplish that which I purpose' -- the active, effective word of God", "type": "ot"},
            {"ref": "Genesis 28:12", "note": "Jacob's dream at Bethel: 'a ladder set up on the earth, and the top of it reached to heaven; and the angels of God were ascending and descending on it' -- fulfilled in 1:51", "type": "ot"},
            {"ref": "Exodus 12:1-13", "note": "The Passover lamb -- the background for the Baptist's declaration: 'Behold, the Lamb of God, who takes away the sin of the world' (1:29)", "type": "ot"},
            {"ref": "Hebrews 1:1-3", "note": "'In these last days he has spoken to us by his Son... through whom also he created the world. He is the radiance of the glory of God' -- parallel to John's Logos theology", "type": "nt"},
            {"ref": "Revelation 19:13", "note": "'He is clothed in a robe dipped in blood, and the name by which he is called is The Word of God' -- the Logos title reappears in Revelation", "type": "nt"},
            {"ref": "1 John 1:1-3", "note": "'That which was from the beginning, which we have heard, which we have seen... concerning the word of life' -- the Johannine community's testimony", "type": "nt"}
        ],

        "divine_council_note": "John 1 is the New Testament's most explicit statement of the 'two powers "
                               "in heaven' theology. The opening verse -- 'the Word was with God (pros ton "
                               "theon) and the Word was God (theos en ho logos)' -- articulates the pattern "
                               "that runs through the entire Old Testament: there are two figures who can be "
                               "called 'God,' who are distinct yet unified. The Word is 'with God' (a second "
                               "figure, face-to-face with the first) and simultaneously 'is God' (shares the "
                               "divine nature completely). This is the same pattern as: the Angel of YHWH who "
                               "bears YHWH's name and is identified as YHWH (Gen 16:7-13; 22:11-18; Exod "
                               "3:2-6; 23:20-21); the 'Lord' at YHWH's right hand (Ps 110:1); the Son of Man "
                               "who approaches the Ancient of Days on the clouds (Dan 7:13-14); the 'Mighty "
                               "God' (El Gibbor) and 'Eternal Father' (Avi-Ad) who is also a child born and "
                               "a son given (Isa 9:6). Alan Segal's academic study 'Two Powers in Heaven' "
                               "(1977) documented that the rabbinic authorities of the 2nd century AD considered "
                               "the 'two powers' belief a heresy -- precisely because early Christians were "
                               "using these Old Testament passages to argue for Christ's divinity. John 1:1 "
                               "is the definitive New Testament articulation of what the Old Testament's 'two "
                               "YHWH figures' meant all along: the Word who created all things, who appeared "
                               "as the Angel of YHWH, who sat enthroned in the divine council -- this Word "
                               "'became flesh and tabernacled among us.' The verse 'No one has ever seen God; "
                               "the only God who is at the Father's side, he has made him known' (1:18) "
                               "resolves the tension of the OT theophanies: when people 'saw God' (Abraham, "
                               "Jacob, Moses, Isaiah), they saw the Logos -- the visible YHWH, the second "
                               "power -- not the invisible Father. John 1:51 extends the divine council "
                               "framework: Jesus is the new Bethel, the new meeting point between the "
                               "heavenly council and earth. The angels ascending and descending 'on the Son "
                               "of Man' means the divine council's traffic -- its messages, its actions, its "
                               "governance of creation -- now flows through Christ.",

        "sections": [
            {
                "heading": "The Logos Prologue (1:1-18) -- Before All Things, the Word",
                "body": "The prologue functions as a theological overture, introducing every major theme "
                        "of the Gospel. 'In the beginning was the Word' (1:1a) -- the imperfect tense "
                        "(en, 'was') indicates continuous existence: the Word did not come into being at "
                        "the beginning; he already was. 'The Word was with God' (1:1b) -- pros ton theon "
                        "implies face-to-face relationship, two distinct persons in communion. 'The Word "
                        "was God' (1:1c) -- theos without the article as predicate: the Word shares the "
                        "divine nature fully. The pattern is trinitarian before the word 'Trinity' existed. "
                        "'All things were made through him' (1:3) -- the Word is the agent of creation, "
                        "the one through whom God spoke the universe into existence. 'In him was life, and "
                        "the life was the light of men' (1:4) -- life and light are divine attributes now "
                        "located in the Word. 'The light shines in the darkness, and the darkness has not "
                        "overcome (katelaben) it' (1:5) -- katelaben can mean both 'overcome' and "
                        "'comprehend'; the darkness neither defeats nor understands the light. Verses 6-8 "
                        "introduce John the Baptist as a witness -- 'he was not the light' -- a pointed "
                        "clarification for any who elevated the Baptist. Verses 10-11 record the tragedy: "
                        "'He was in the world, and the world was made through him, yet the world did not "
                        "know him. He came to his own, and his own people did not receive him.' The Creator "
                        "entered his own creation and was rejected by the creatures he made. Verse 14 is "
                        "the hinge of the prologue and of all theology: 'The Word became flesh.' The verb "
                        "egeneto ('became') is the same verb used for creation in 1:3 -- the one through "
                        "whom all things 'came into being' has himself 'become' flesh. He 'tabernacled' "
                        "(eskenosen) among us -- the divine presence that filled the Tabernacle (Exod "
                        "40:34-35) now fills a human body. 'We have seen his glory' -- the kavod/doxa "
                        "that Moses glimpsed on Sinai (Exod 33:18-23), the disciples have seen in the "
                        "flesh. Verse 18 crowns it: 'No one has ever seen God' -- this is the theological "
                        "key to every Old Testament theophany. When Abraham saw YHWH at Mamre, when Jacob "
                        "wrestled with God at Peniel, when Moses saw the burning bush, when Isaiah saw "
                        "the Lord high and lifted up -- they saw the Logos, the visible God, the 'only "
                        "God who is at the Father's side.' The Logos has been 'exegeting' (exegesato) "
                        "the invisible Father from the very first theophany."
            },
            {
                "heading": "The Baptist's Testimony and the First Disciples (1:19-51)",
                "body": "The Baptist identifies himself as the voice of Isaiah 40:3 -- 'Make straight the "
                        "way of the Lord' -- and emphatically denies being the Christ, Elijah, or the "
                        "Prophet (1:19-28). His testimony about Jesus is christologically loaded: 'Behold, "
                        "the Lamb of God (ho amnos tou theou), who takes away the sin of the world!' "
                        "(1:29). The 'Lamb of God' fuses multiple Old Testament images: the Passover lamb "
                        "(Exod 12), the scapegoat of the Day of Atonement (Lev 16), the lamb led to "
                        "slaughter in Isaiah 53:7, and the daily tamid offerings. The Baptist testifies "
                        "to seeing the Spirit descend 'like a dove' on Jesus and declares: 'This is the "
                        "Son of God' (1:34, or in some manuscripts, 'the chosen one of God'). The first "
                        "disciples come through a chain of testimony: Andrew follows Jesus and tells "
                        "Peter, 'We have found the Messiah' (Messian, the Hebrew/Aramaic title translated "
                        "into Greek as Christos -- 1:41). Philip tells Nathanael, 'We have found him of "
                        "whom Moses in the Law and also the prophets wrote' (1:45). Nathanael's skepticism "
                        "('Can anything good come out of Nazareth?' -- 1:46) gives way to confession: "
                        "'Rabbi, you are the Son of God! You are the King of Israel!' (1:49). Jesus' "
                        "response escalates the christological claims: 'You will see heaven opened, and "
                        "the angels of God ascending and descending on the Son of Man' (1:51). This "
                        "references Genesis 28:12 -- Jacob's ladder at Bethel. In Jacob's dream, the "
                        "ladder connected the divine council's throne room to earth. Jesus replaces the "
                        "ladder: he is the point where heaven and earth intersect. The divine council's "
                        "messengers ascend and descend 'on' (epi) the Son of Man -- he is the new Bethel, "
                        "the house of God, the meeting place of the divine and human realms."
            }
        ]
    },

    {
        "id": "john-2-3",
        "ref": "John 2-3",
        "chapter_num": 2,
        "title": "The New Temple and the New Birth -- Cana, Jerusalem, and Nicodemus",
        "era": "john_signs",
        "type": "chapter",
        "themes": ["DC", "GLORY", "TYPE", "SEED", "WOMEN"],

        "synopsis": "Chapters 2-3 introduce the themes of replacement and revelation. At the wedding in "
                    "Cana (2:1-11), Jesus performs the first sign (semeion) -- turning water into wine. "
                    "The six stone water jars 'for the Jewish rites of purification' (2:6) represent the "
                    "old covenant system; Jesus transforms them into something new and abundantly better "
                    "(the master of the banquet marvels at the quality). The sign 'manifested his glory "
                    "(doxa), and his disciples believed in him' (2:11). In Jerusalem, Jesus cleanses the "
                    "Temple (2:13-22) -- in John, this occurs at the beginning of the ministry, not the "
                    "end. When challenged, Jesus says: 'Destroy this temple (naon), and in three days I "
                    "will raise it up' (2:19). John explains: 'He was speaking about the temple of his "
                    "body' (2:21). Jesus himself is the new Temple -- the place where God's presence "
                    "dwells (cf. 1:14, 'tabernacled among us'). Chapter 3 presents the dialogue with "
                    "Nicodemus, a Pharisee and 'ruler of the Jews' (archon ton Ioudaion -- 3:1), who "
                    "comes to Jesus at night. Jesus tells him: 'Unless one is born again (anothen -- "
                    "'from above' or 'again,' the double meaning is intentional) he cannot see the "
                    "kingdom of God' (3:3). Nicodemus misunderstands, taking the physical meaning. "
                    "Jesus clarifies: 'Unless one is born of water and the Spirit (pneuma), he cannot "
                    "enter the kingdom of God. That which is born of the flesh is flesh, and that which "
                    "is born of the Spirit is spirit' (3:5-6). The discourse ascends to cosmic claims: "
                    "'No one has ascended into heaven except he who descended from heaven, the Son of "
                    "Man' (3:13) -- Jesus alone has come from the divine council's realm. 'As Moses "
                    "lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that "
                    "whoever believes in him may have eternal life' (3:14-15). Then the most famous "
                    "verse in the Bible: 'For God so loved the world, that he gave his only Son "
                    "(monogenes), that whoever believes in him should not perish but have eternal life' "
                    "(3:16).",

        "key_verse": {
            "ref": "John 3:13-16",
            "text": "No one has ascended into heaven except he who descended from heaven, the Son of Man. And as Moses lifted up the serpent in the wilderness, so must the Son of Man be lifted up, that whoever believes in him may have eternal life. For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.",
            "translation": "ESV"
        },

        "original_terms": [
            "semeion (sign -- John's term for Jesus' miracles; they point beyond themselves to his identity "
            "and glory; seven signs structure the Book of Signs)",
            "naos (temple sanctuary -- the inner dwelling of God's presence, not the outer courts; Jesus "
            "identifies his body as the new naos, the new dwelling place of God)",
            "anothen (from above / again -- deliberately ambiguous; Nicodemus hears 'again,' Jesus means "
            "'from above'; the new birth is a heavenly origin, not a repetition of natural birth)",
            "pneuma (spirit/wind -- the same word in Greek; Jesus plays on the double meaning in 3:8: "
            "'The wind/spirit blows where it wishes')",
            "monogenes huios (only/unique Son -- the Father's gift to the world; not one among many sons "
            "but the unique, one-of-a-kind Son)",
            "hypsoo (to lift up / to exalt -- used for the crucifixion in 3:14; 8:28; 12:32-34; a double "
            "meaning: physical lifting on the cross AND exaltation to glory)"
        ],

        "ane_backdrop": "The wedding at Cana echoes the ANE motif of the divine banquet. In Ugaritic "
                        "literature, the gods feast with abundant wine at El's mountain; in Isaiah's "
                        "eschatological vision, 'the LORD of hosts will make for all peoples a feast of "
                        "rich food, a feast of well-aged wine' (Isa 25:6). Jesus providing wine in "
                        "abundance at a wedding signals the arrival of the messianic age. The brazen "
                        "serpent reference (3:14, from Num 21:4-9) has ANE background: serpent imagery "
                        "was widespread in the ancient Near East as a symbol of both death and healing "
                        "(the Egyptian uraeus, the Mesopotamian serpent deities). The bronze serpent on "
                        "a pole that healed those who looked at it prefigures the Son of Man 'lifted "
                        "up' on the cross -- death on display becoming the source of life for those who "
                        "'look' (believe).",

        "second_temple": [
            {
                "source": "Dead Sea Scrolls: Rule of the Community (1QS 3:13-4:26)",
                "summary": "The 'two spirits' section describes God placing in humanity a 'spirit of truth' "
                           "and a 'spirit of deceit,' with light and darkness in cosmic conflict. Those "
                           "born of the 'spirit of truth' walk in light; those of the 'spirit of deceit' "
                           "walk in darkness.",
                "relevance": "John 3's language of being 'born of the Spirit,' the light/darkness dualism "
                             "(3:19-21), and the contrast between flesh and spirit parallels Qumran's two-"
                             "spirits theology, suggesting shared Second Temple conceptual categories."
            },
            {
                "source": "Josephus, Jewish War 5.184-247",
                "summary": "Josephus describes the Jerusalem Temple in elaborate detail, including the "
                           "Herodian expansion that made it one of the architectural wonders of the "
                           "Roman world. The Temple took 46 years to build (cf. John 2:20).",
                "relevance": "The Jews' objection -- 'It has taken forty-six years to build this temple, "
                             "and will you raise it up in three days?' (2:20) -- reflects the historical "
                             "reality of Herod's massive Temple project, begun ~20 BC."
            },
            {
                "source": "Ezekiel 36:25-27",
                "summary": "'I will sprinkle clean water on you... I will give you a new heart and a "
                           "new spirit I will put within you... I will put my Spirit within you.'",
                "relevance": "Jesus' words about being 'born of water and the Spirit' (3:5) echo Ezekiel's "
                             "eschatological promise of spiritual cleansing and new creation -- the new "
                             "covenant transformation that Nicodemus, as a 'teacher of Israel' (3:10), "
                             "should have recognized."
            }
        ],

        "cross_refs": [
            {"ref": "Numbers 21:4-9", "note": "The bronze serpent in the wilderness: those who looked at it lived -- the type fulfilled in Jesus being 'lifted up' on the cross (3:14)", "type": "ot"},
            {"ref": "Isaiah 25:6-8", "note": "The messianic banquet with 'well-aged wine' -- the background for the wedding at Cana as a sign of the messianic age", "type": "ot"},
            {"ref": "Ezekiel 36:25-27", "note": "'I will sprinkle clean water... I will put my Spirit within you' -- the new-birth passage Nicodemus should have known (3:5, 10)", "type": "ot"},
            {"ref": "Ezekiel 37:1-14", "note": "The valley of dry bones: 'I will put my Spirit in you, and you shall live' -- corporate resurrection through the Spirit, parallel to John 3", "type": "ot"},
            {"ref": "Malachi 3:1", "note": "'The Lord whom you seek will suddenly come to his temple' -- fulfilled in the Temple cleansing (2:13-17)", "type": "ot"},
            {"ref": "1 Corinthians 3:16", "note": "'Do you not know that you are God's temple (naos) and that God's Spirit dwells in you?' -- Paul extends the 'body as temple' theology", "type": "nt"},
            {"ref": "Revelation 21:22", "note": "'I saw no temple in the city, for its temple is the Lord God the Almighty and the Lamb' -- the eschatological fulfillment of Jesus as Temple", "type": "nt"}
        ],

        "divine_council_note": "Three divine council connections dominate these chapters. First, the Temple "
                               "cleansing (2:13-22): the Jerusalem Temple was understood as the earthly "
                               "counterpart of the heavenly temple/throne room -- the place where YHWH's "
                               "presence (Shekinah) dwelt on earth, mirroring the divine council's heavenly "
                               "sanctuary. Jesus' claim that his body is the new Temple (2:19-21) means the "
                               "divine council's earthly dwelling is no longer a building but a person. The "
                               "Logos who 'tabernacled among us' (1:14) is himself the meeting place of "
                               "heaven and earth. Second, 3:13: 'No one has ascended into heaven except he "
                               "who descended from heaven, the Son of Man.' This claims a unique origin in "
                               "the divine council's realm. No prophet, no angel, no human has the kind of "
                               "access to the heavenly throne room that the Son of Man has -- because he "
                               "came FROM there. He 'descended from heaven,' implying prior existence in the "
                               "heavenly council. Third, 3:16-18: the language of the 'only Son' (monogenes "
                               "huios) given by the Father echoes the divine council's distinction between "
                               "the 'sons of God' (bene elohim -- the council members) and the unique Son "
                               "who is monogenes -- one of a kind, unlike any other son. The divine council "
                               "has many sons (Job 1:6; 38:7; Ps 89:6); the Father has only one.",

        "sections": [
            {
                "heading": "The Wedding at Cana -- The First Sign (2:1-11)",
                "body": "The first sign occurs 'on the third day' (2:1) -- a subtle resurrection echo. "
                        "Jesus' mother tells him the wine has run out. His response -- 'Woman, what does "
                        "this have to do with me? My hour (hora) has not yet come' (2:4) -- introduces "
                        "the critical Johannine concept of the 'hour': the appointed time of Jesus' "
                        "death, resurrection, and glorification (see 7:30; 8:20; 12:23, 27; 13:1; 17:1). "
                        "Despite this, Mary instructs the servants: 'Do whatever he tells you' (2:5). "
                        "Six stone water jars, each holding 20-30 gallons, 'for the Jewish rites of "
                        "purification' (2:6), are filled with water that Jesus transforms into wine. "
                        "The master of the banquet marvels that the best wine was kept until last (2:10). "
                        "The sign reveals: (1) Jesus has power over creation -- the one through whom 'all "
                        "things were made' (1:3) transforms the elements; (2) the old purification system "
                        "is being replaced by something better -- the water of ritual cleansing becomes "
                        "the wine of messianic celebration; (3) the abundance (120-180 gallons of the "
                        "finest wine) signals the messianic age prophesied in Amos 9:13-14 and Isaiah "
                        "25:6. 'This, the first of his signs, Jesus did at Cana in Galilee, and manifested "
                        "his glory (doxa). And his disciples believed in him' (2:11)."
            },
            {
                "heading": "The Temple Cleansing and the Body as Temple (2:13-22)",
                "body": "At Passover in Jerusalem, Jesus drives out the animal sellers and money changers "
                        "with a whip of cords: 'Take these things away; do not make my Father's house a "
                        "house of trade' (2:16). The disciples remember Psalm 69:9: 'Zeal for your house "
                        "will consume me.' When the authorities demand a sign to justify this action, "
                        "Jesus says: 'Destroy this temple (naon), and in three days I will raise it up' "
                        "(2:19). They assume he means the physical Temple ('It has taken forty-six years "
                        "to build this temple, and will you raise it up in three days?' -- 2:20). John "
                        "explains: 'He was speaking about the temple of his body. When therefore he was "
                        "raised from the dead, his disciples remembered that he had said this, and they "
                        "believed the Scripture and the word that Jesus had spoken' (2:21-22). The "
                        "theological claim is enormous: the physical Temple in Jerusalem -- the place "
                        "where YHWH's kavod dwelt, where the divine council's presence touched earth, "
                        "where heaven and earth overlapped -- is being replaced by the body of Jesus. "
                        "The incarnation IS the new Temple. After the resurrection, God's dwelling among "
                        "humanity is no longer architectural but personal."
            },
            {
                "heading": "Nicodemus and the New Birth (3:1-21)",
                "body": "Nicodemus comes 'by night' (3:2) -- in John's symbolic world, night represents "
                        "spiritual darkness (cf. 9:4; 11:10; 13:30). He acknowledges Jesus as 'a teacher "
                        "come from God' but does not yet grasp who Jesus truly is. Jesus' response cuts "
                        "through religious politeness: 'Unless one is born anothen (from above/again), "
                        "he cannot see the kingdom of God' (3:3). The word anothen carries a double "
                        "meaning: Nicodemus hears 'again' (physical rebirth); Jesus means 'from above' "
                        "(heavenly origin). Natural birth -- descent from Abraham, circumcision, Torah "
                        "observance -- is insufficient. One must be 'born of water and the Spirit' (3:5) "
                        "-- a reference to Ezekiel 36:25-27's promise of eschatological cleansing and "
                        "spiritual renewal. 'That which is born of the flesh is flesh, and that which is "
                        "born of the Spirit is spirit' (3:6) -- flesh (sarx) and spirit (pneuma) are two "
                        "orders of existence. Entry into God's kingdom requires a new origin -- from "
                        "above, from the Spirit, from God himself. Jesus rebukes Nicodemus: 'Are you the "
                        "teacher of Israel and yet you do not understand these things?' (3:10) -- Ezekiel "
                        "36-37 should have been his framework. The discourse rises to its cosmic climax: "
                        "'No one has ascended into heaven except he who descended from heaven, the Son of "
                        "Man' (3:13). Only the one who came from the divine council's realm can reveal "
                        "heavenly things. 'As Moses lifted up the serpent in the wilderness, so must the "
                        "Son of Man be lifted up' (3:14) -- hypsoo means both 'lift up' physically (on "
                        "the cross) and 'exalt' in glory. The crucifixion is simultaneously execution and "
                        "enthronement. Then: 'For God so loved the world, that he gave his only Son, that "
                        "whoever believes in him should not perish but have eternal life' (3:16). The "
                        "'giving' of the Son is both the incarnation (the Son given to the world) and the "
                        "cross (the Son given up to death). The judgment theme follows: 'This is the "
                        "judgment: the light has come into the world, and people loved the darkness rather "
                        "than the light because their works were evil' (3:19)."
            }
        ]
    },

    {
        "id": "john-4-5",
        "ref": "John 4-5",
        "chapter_num": 3,
        "title": "Living Water and Divine Authority -- The Samaritan Woman and the Healing at Bethesda",
        "era": "john_signs",
        "type": "chapter",
        "themes": ["KING", "SEED", "SPIRIT", "DC", "TYPE"],

        "synopsis": "Chapters 4-5 expand the scope of Jesus' mission beyond Jewish territory and assert "
                    "his divine prerogatives with unprecedented directness. In chapter 4, Jesus travels "
                    "through Samaria and encounters a woman at Jacob's well near Sychar (4:4-6). The "
                    "dialogue is masterfully structured: Jesus asks for water, then offers 'living water' "
                    "(hydor zon -- 4:10) that becomes 'a spring of water welling up to eternal life' "
                    "(4:14). The woman asks for this water; Jesus exposes her personal history (five "
                    "husbands, now living with a man who is not her husband -- 4:17-18); she deflects "
                    "to the theological debate between Jews and Samaritans about the proper place of "
                    "worship (Mount Gerizim vs. Jerusalem -- 4:20). Jesus' response transcends both "
                    "locations: 'The hour is coming when neither on this mountain nor in Jerusalem will "
                    "you worship the Father... the true worshipers will worship the Father in spirit "
                    "and truth (en pneumati kai aletheia)' (4:21-23). Then the woman says, 'I know that "
                    "Messiah is coming (the one called Christ). When he comes, he will tell us all "
                    "things' (4:25). Jesus responds with the absolute ego eimi: 'I who speak to you am "
                    "he' (ego eimi, ho lalon soi -- 4:26). The Samaritans believe and declare: 'This is "
                    "indeed the Savior of the world (ho soter tou kosmou)' (4:42). Chapter 5 records the "
                    "healing at the Pool of Bethesda (5:1-15) on the Sabbath, provoking a confrontation "
                    "with the Jewish authorities. Jesus' defense is explosive: 'My Father is working "
                    "until now, and I am working' (5:17). John notes: 'This was why the Jews were "
                    "seeking all the more to kill him, because not only was he breaking the Sabbath, but "
                    "he was even calling God his own Father (patera idion), making himself equal with God "
                    "(ison to theo)' (5:18). Jesus then delivers a discourse claiming the divine "
                    "prerogatives of giving life and executing judgment: 'As the Father raises the dead "
                    "and gives them life, so also the Son gives life to whom he will. For the Father "
                    "judges no one, but has given all judgment to the Son, that all may honor the Son, "
                    "just as they honor the Father' (5:21-23). 'An hour is coming when all who are in "
                    "the tombs will hear his voice and come out' (5:28-29) -- the Son of Man exercises "
                    "the power of resurrection itself.",

        "key_verse": {
            "ref": "John 5:21-23",
            "text": "For as the Father raises the dead and gives them life, so also the Son gives life to whom he will. For the Father judges no one, but has given all judgment to the Son, that all may honor the Son, just as they honor the Father. Whoever does not honor the Son does not honor the Father who sent him.",
            "translation": "ESV"
        },

        "original_terms": [
            "hydor zon (living water -- in the OT, 'living water' is flowing, fresh water as opposed to "
            "cistern water; metaphorically, God himself is the 'fountain of living water,' Jer 2:13; 17:13)",
            "en pneumati kai aletheia (in spirit and truth -- worship that transcends location because it "
            "is empowered by the Holy Spirit and grounded in the truth revealed by Jesus)",
            "ego eimi ho lalon soi (I AM, the one speaking to you -- 4:26; Jesus' self-revelation to the "
            "Samaritan woman using the absolute ego eimi with the divine name connotation)",
            "patera idion (his own Father -- 5:18; a claim to unique, intimate relationship with God that "
            "the authorities understood as claiming equality with God)",
            "ison to theo (equal with God -- 5:18; the authorities' interpretation of Jesus' claim, which "
            "John presents as correct -- Jesus IS making himself equal with God)",
            "krisis (judgment -- the authority to judge the living and the dead, given to the Son by the "
            "Father; 5:22, 27, 30)"
        ],

        "ane_backdrop": "The Samaritan woman's mention of worship at 'this mountain' (Mount Gerizim, "
                        "4:20) reflects the ancient competition between Jerusalem and Samaria. After the "
                        "Assyrian conquest of the northern kingdom (722 BC), the Samaritans developed "
                        "their own worship tradition centered on Mount Gerizim, where they built a temple "
                        "(later destroyed by John Hyrcanus in ~128 BC). They accepted only the Torah "
                        "(not the Prophets or Writings) and awaited not a 'Messiah' in the Davidic sense "
                        "but a 'Taheb' (restorer) -- a Moses-like prophet figure (based on Deut 18:15-18). "
                        "The Pool of Bethesda (5:2), described by John as having 'five roofed colonnades' "
                        "(stoas), has been archaeologically confirmed -- excavations in the 1950s-60s "
                        "revealed a pool complex with five porticoes near the Sheep Gate, exactly matching "
                        "John's description. This is significant evidence for the Gospel's eyewitness "
                        "tradition about pre-70 AD Jerusalem.",

        "second_temple": [
            {
                "source": "Samaritan Pentateuch and Memar Marqah",
                "summary": "The Samaritans expected a 'Taheb' (Restorer) based on Deuteronomy 18:15-18, "
                           "a prophet like Moses who would reveal all things. The Memar Marqah (4th "
                           "century AD, but preserving earlier traditions) describes the Taheb as a "
                           "teacher and restorer of true worship.",
                "relevance": "The woman's statement 'I know that Messiah is coming... he will tell us "
                             "all things' (4:25) reflects the Samaritan Taheb expectation. Jesus' 'I AM' "
                             "response (4:26) claims to be this awaited figure -- and more."
            },
            {
                "source": "Philo, On the Cherubim 27-29",
                "summary": "Philo discusses God as the source of living, flowing water and the soul's "
                           "thirst for divine wisdom as a thirst for 'living water.'",
                "relevance": "The 'living water' imagery has both scriptural (Jer 2:13; Zech 14:8) and "
                             "philosophical roots in Second Temple Judaism, making Jesus' offer "
                             "intelligible to both Jewish and Hellenistic audiences."
            },
            {
                "source": "Daniel 7:13-14",
                "summary": "The Son of Man receives 'dominion and glory and a kingdom, that all peoples, "
                           "nations, and languages should serve him.'",
                "relevance": "Jesus' claim in 5:27 that the Father has given him 'authority to execute "
                             "judgment, because he is the Son of Man' directly invokes Daniel 7's divine "
                             "council figure who receives universal authority."
            }
        ],

        "cross_refs": [
            {"ref": "Jeremiah 2:13", "note": "'My people have committed two evils: they have forsaken me, the fountain of living waters, and hewed out cisterns... that can hold no water' -- the OT background for Jesus as living water", "type": "ot"},
            {"ref": "Isaiah 12:3", "note": "'With joy you will draw water from the wells of salvation' -- the messianic promise of abundant water/Spirit", "type": "ot"},
            {"ref": "Zechariah 14:8", "note": "'On that day living waters shall flow out from Jerusalem' -- the eschatological promise fulfilled in Jesus", "type": "ot"},
            {"ref": "Deuteronomy 18:15-18", "note": "'The LORD your God will raise up for you a prophet like me' -- the Moses-like prophet the Samaritan woman awaited", "type": "ot"},
            {"ref": "Daniel 7:13-14, 22", "note": "The Son of Man given authority to judge -- the background for 5:22-27 where Jesus claims the Father has given 'all judgment to the Son'", "type": "ot"},
            {"ref": "Daniel 12:2", "note": "'Many of those who sleep in the dust of the earth shall awake' -- the background for 5:28-29: 'all who are in the tombs will hear his voice'", "type": "ot"},
            {"ref": "Philippians 2:5-11", "note": "'He did not count equality with God a thing to be grasped' -- Paul's language parallels John 5:18's claim of equality with God", "type": "nt"}
        ],

        "divine_council_note": "Chapter 5 contains the most explicit claim to divine prerogatives in the "
                               "Gospels. Jesus claims two powers that belong exclusively to God in the Old "
                               "Testament: (1) giving life -- 'As the Father raises the dead and gives them "
                               "life, so also the Son gives life to whom he will' (5:21). In the OT, raising "
                               "the dead is YHWH's unique prerogative (Deut 32:39; 1 Sam 2:6; 2 Kings 5:7). "
                               "Jesus claims this power as his own. (2) Executing judgment -- 'The Father "
                               "judges no one, but has given all judgment to the Son' (5:22). In the divine "
                               "council, YHWH is the supreme judge (Ps 82:1, 8; Dan 7:9-10). Jesus claims "
                               "this authority has been delegated to him -- not as a subordinate functionary "
                               "but so that 'all may honor the Son, just as they honor the Father' (5:23). "
                               "Equal honor means equal status. The authorities understood exactly what Jesus "
                               "was claiming: 'making himself equal with God' (5:18). In Daniel 7, the Son of "
                               "Man receives authority from the Ancient of Days in the divine council. John 5 "
                               "is the narrative fulfillment of that vision: the Father (Ancient of Days) has "
                               "given 'all judgment' and 'authority' to the Son (Son of Man) -- 'because he "
                               "is the Son of Man' (5:27). The 'hour is coming when all who are in the tombs "
                               "will hear his voice' (5:28) claims the eschatological power that Daniel 12:2 "
                               "attributes to the time of Michael's arising -- but here it is the Son of Man's "
                               "voice, not Michael's, that summons the dead.",

        "sections": [
            {
                "heading": "The Samaritan Woman at the Well (4:1-42)",
                "body": "Jesus 'had to pass through Samaria' (4:4) -- the geographical necessity may "
                        "carry theological significance: the Messiah must reach beyond Jewish borders. "
                        "At Jacob's well (a site with deep patriarchal significance), Jesus asks a "
                        "Samaritan woman for water -- crossing both gender and ethnic boundaries (4:9: "
                        "'Jews have no dealings with Samaritans'). The dialogue ascends through levels "
                        "of meaning: from physical water to 'living water' (hydor zon -- 4:10), from "
                        "the well of Jacob to the 'spring welling up to eternal life' (4:14), from "
                        "the proper mountain for worship to 'worship in spirit and truth' (4:23-24). "
                        "Jesus' statement 'God is spirit (pneuma ho theos)' (4:24) is one of the most "
                        "important theological declarations in Scripture -- not that God is an impersonal "
                        "force, but that authentic worship requires spiritual transformation (the 'birth "
                        "from above' of chapter 3), not merely correct geography. The woman's prophetic "
                        "expectation -- 'I know that Messiah is coming' (4:25) -- receives the most "
                        "direct messianic declaration in the Gospels: 'ego eimi, ho lalon soi' -- 'I AM, "
                        "the one speaking to you' (4:26). The ego eimi carries the divine name overtones. "
                        "The Samaritan response is remarkable: 'This is indeed the Savior of the world "
                        "(ho soter tou kosmou)' (4:42) -- a title that in the Roman world belonged to "
                        "the emperor. The Samaritans, despised by the Jews, become the first to recognize "
                        "Jesus' universal significance."
            },
            {
                "heading": "The Healing at Bethesda and the Divine Prerogatives (5:1-47)",
                "body": "At the Pool of Bethesda in Jerusalem (confirmed by archaeology), Jesus heals a "
                        "man who had been an invalid for 38 years -- on the Sabbath. When confronted, "
                        "Jesus does not apologize or explain away the Sabbath violation. Instead, he "
                        "escalates: 'My Father is working until now, and I am working' (5:17). The claim "
                        "is twofold: (1) God is 'my Father' (not merely 'our Father' but patera idion -- "
                        "'his own Father'), implying a unique filial relationship; (2) the Son works as "
                        "the Father works -- even on the Sabbath. God does not cease sustaining creation "
                        "on the Sabbath; neither does his Son. The authorities correctly interpret this as "
                        "a claim to equality with God (5:18). The discourse that follows (5:19-47) is the "
                        "most systematic statement of the Father-Son relationship in the Gospels. The Son "
                        "does nothing 'of his own accord' but only what he sees the Father doing (5:19) -- "
                        "not subordination but perfect unity of will. The Father shows the Son 'all that "
                        "he himself is doing' (5:20) -- complete transparency between the two divine "
                        "persons. Two divine prerogatives are claimed: giving life (5:21) and executing "
                        "judgment (5:22). The purpose: 'that all may honor the Son, just as they honor the "
                        "Father' (5:23). Equal honor demands equal nature. Jesus then points to four "
                        "witnesses who testify to his identity: John the Baptist (5:33-35), his works "
                        "(5:36), the Father himself (5:37), and the Scriptures (5:39-40). The climax: "
                        "'If you believed Moses, you would believe me; for he wrote of me' (5:46) -- the "
                        "entire Torah points to Jesus."
            }
        ]
    },

    {
        "id": "john-6",
        "ref": "John 6",
        "chapter_num": 4,
        "title": "The Bread of Life -- Manna, Flesh, and the I AM Who Descended from Heaven",
        "era": "john_signs",
        "type": "chapter",
        "themes": ["KING", "PROV", "DC", "HOLY", "TYPE"],

        "synopsis": "Chapter 6 is one of the longest and most theologically demanding chapters in the "
                    "Gospels. It begins with the feeding of the 5,000 (6:1-15) -- the only miracle "
                    "recorded in all four Gospels -- followed by Jesus walking on the Sea of Galilee "
                    "(6:16-21), where he again says 'ego eimi' ('It is I' or 'I AM' -- 6:20). But the "
                    "heart of the chapter is the Bread of Life discourse (6:22-71), delivered in the "
                    "synagogue at Capernaum. The crowd, wanting more bread, seeks Jesus. He tells them: "
                    "'Do not work for the food that perishes, but for the food that endures to eternal "
                    "life, which the Son of Man will give to you' (6:27). They ask: 'Our fathers ate "
                    "the manna in the wilderness; as it is written, \"He gave them bread from heaven "
                    "to eat\"' (6:31, quoting Ps 78:24). Jesus' response redefines the manna: 'It was "
                    "not Moses who gave you the bread from heaven, but my Father gives you the true "
                    "bread from heaven. For the bread of God is he who comes down from heaven and gives "
                    "life to the world' (6:32-33). Then the I AM statement: 'I am the bread of life "
                    "(ego eimi ho artos tes zoes). Whoever comes to me shall not hunger, and whoever "
                    "believes in me shall never thirst' (6:35). The discourse intensifies: 'I am the "
                    "living bread that came down from heaven. If anyone eats of this bread, he will "
                    "live forever. And the bread that I will give for the life of the world is my flesh "
                    "(sarx)' (6:51). The Jews dispute among themselves: 'How can this man give us his "
                    "flesh to eat?' (6:52). Jesus does not soften the language: 'Unless you eat the "
                    "flesh of the Son of Man and drink his blood, you have no life in you' (6:53). "
                    "Many disciples find this a 'hard saying' (skleros ho logos -- 6:60) and leave. "
                    "Jesus asks the Twelve: 'Do you want to go away as well?' Peter responds: 'Lord, "
                    "to whom shall we go? You have the words of eternal life, and we have believed, "
                    "and have come to know, that you are the Holy One of God' (6:68-69).",

        "key_verse": {
            "ref": "John 6:35, 51",
            "text": "Jesus said to them, 'I am the bread of life; whoever comes to me shall not hunger, and whoever believes in me shall never thirst... I am the living bread that came down from heaven. If anyone eats of this bread, he will live forever. And the bread that I will give for the life of the world is my flesh.'",
            "translation": "ESV"
        },

        "original_terms": [
            "artos tes zoes (bread of life -- the first I AM + predicate statement; Jesus as the true manna, "
            "the bread from heaven that gives eternal life; replacing the wilderness manna of Exod 16)",
            "ego eimi (I AM -- used both in the Bread of Life declaration and on the sea in 6:20; the "
            "latter echoes Job 9:8, where YHWH 'trampled the waves of the sea')",
            "sarx (flesh -- Jesus' humanity offered as spiritual food; the same word used for the incarnation "
            "in 1:14; deliberately shocking language meant to point to the cross)",
            "skleros ho logos (hard saying -- literally 'harsh/rough word'; the disciples' reaction to the "
            "eucharistic language; the logos that offends)",
            "ho hagios tou theou (the Holy One of God -- Peter's confession in 6:69; a divine council title "
            "that identifies Jesus as uniquely set apart by God)"
        ],

        "ane_backdrop": "The feeding miracle and Bread of Life discourse are set against the backdrop of "
                        "the Exodus manna tradition, but they also engage broader ANE concepts of divine "
                        "provision. In Mesopotamian mythology, the gods ate the 'bread of life' and drank "
                        "the 'water of life' in the heavenly realm -- these were substances that conferred "
                        "immortality (see the Epic of Gilgamesh, where Gilgamesh is offered but loses "
                        "the plant of life). In the Exodus narrative, YHWH provides manna -- 'bread from "
                        "heaven' (lechem min hashamayim, Exod 16:4) -- to sustain Israel in the wilderness. "
                        "Jesus claims to BE the bread from heaven -- not a created substance but a divine "
                        "person who gives life by giving himself. The walking on the sea (6:16-21) echoes "
                        "YHWH's sovereignty over the chaotic waters: 'He alone... trampled the waves of "
                        "the sea' (Job 9:8); 'Your way was through the sea, your path through the great "
                        "waters' (Ps 77:19). Jesus' 'I AM' on the sea is a theophany -- the divine "
                        "council's Lord asserting his authority over chaos.",

        "second_temple": [
            {
                "source": "2 Baruch 29:8",
                "summary": "'The treasury of manna shall again descend from on high, and they will eat of "
                           "it in those years, because these are they who have come to the consummation "
                           "of time.'",
                "relevance": "Second Temple expectation held that the manna would return in the messianic "
                             "age. Jesus claims he IS the returned manna -- the true bread from heaven "
                             "that the eschatological expectation pointed to."
            },
            {
                "source": "Mekhilta de-Rabbi Ishmael on Exodus 16:25",
                "summary": "Rabbinic tradition held that 'as the first redeemer (Moses) caused manna to "
                           "descend, so will the last redeemer (Messiah) cause manna to descend.'",
                "relevance": "The crowd's expectation that Jesus should provide manna (6:30-31) reflects "
                             "this messianic-manna tradition. Jesus redirects: the manna is not bread but "
                             "himself -- 'the bread of God is he who comes down from heaven.'"
            },
            {
                "source": "Psalm 78:24-25",
                "summary": "'He rained down on them manna to eat and gave them the grain of heaven. Man "
                           "ate of the bread of the angels (lechem abbirim).'",
                "relevance": "The crowd quotes this psalm (6:31). 'Bread of angels' (lechem abbirim) "
                             "suggests the manna had a heavenly, divine-council origin. Jesus claims to "
                             "be the reality the manna only shadowed."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 16:1-36", "note": "The manna narrative: YHWH provides 'bread from heaven' for Israel in the wilderness -- the type that Jesus fulfills as the 'true bread from heaven' (6:32)", "type": "ot"},
            {"ref": "Psalm 78:24-25", "note": "'He gave them the grain of heaven. Man ate of the bread of the angels' -- quoted by the crowd in 6:31", "type": "ot"},
            {"ref": "Job 9:8", "note": "YHWH 'alone stretched out the heavens and trampled the waves of the sea' -- the background for Jesus walking on the sea and saying 'I AM' (6:20)", "type": "ot"},
            {"ref": "Psalm 77:19", "note": "'Your way was through the sea, your path through the great waters, yet your footprints were unseen' -- YHWH's sovereign power over the waters", "type": "ot"},
            {"ref": "Mark 6:30-52", "note": "The Synoptic account of the feeding and the sea walking -- Mark notes the disciples 'did not understand about the loaves' (Mark 6:52)", "type": "nt"},
            {"ref": "1 Corinthians 10:1-4", "note": "Paul interprets the wilderness manna and water as Christ: 'they drank from the spiritual Rock that followed them, and the Rock was Christ'", "type": "nt"},
            {"ref": "1 Corinthians 11:23-26", "note": "The Lord's Supper tradition: 'This is my body... this is my blood' -- eucharistic language that parallels John 6:51-56", "type": "nt"}
        ],

        "divine_council_note": "The Bread of Life discourse makes three divine council claims. First, "
                               "Jesus claims heavenly origin: 'I have come down from heaven' (6:38, 41-42, "
                               "50-51, 58). He has not merely been 'sent from God' like a prophet; he "
                               "'came down from heaven' -- his origin is in the divine council's realm, and "
                               "the incarnation is his descent from that realm into the world. Second, the "
                               "walking on the sea (6:16-21) is a divine council theophany. In the Old "
                               "Testament, YHWH alone walks on the sea (Job 9:8; Ps 77:19; Hab 3:15). "
                               "Jesus does what only YHWH does, and his 'ego eimi' on the water is the "
                               "divine name spoken in the context of divine action. Third, the Bread of "
                               "Life claim itself transcends any prophetic or angelic category. Moses "
                               "provided manna, but Moses was merely the mediator -- 'it was not Moses who "
                               "gave you the bread from heaven, but my Father gives you the true bread' "
                               "(6:32). Jesus is not a new Moses; he is the bread itself -- the divine "
                               "provision that the manna merely typified. The manna came from the realm of "
                               "the divine council ('the grain of heaven,' 'the bread of the angels' -- "
                               "Ps 78:24-25); Jesus is the divine council member who has personally come "
                               "from that realm to give his own flesh for the life of the world.",

        "sections": [
            {
                "heading": "The Feeding of the 5,000 and Walking on the Sea (6:1-21)",
                "body": "The feeding of the 5,000 (6:1-15) occurs near Passover (6:4) -- the second of "
                        "John's three Passovers, and the connection to the Passover/Exodus is theologically "
                        "deliberate. The five barley loaves and two fish (6:9) are multiplied to feed the "
                        "multitude with twelve baskets left over (6:13). The people's reaction is "
                        "significant: 'This is indeed the Prophet who is to come into the world!' (6:14, "
                        "echoing Deut 18:15). They try to make Jesus king by force (6:15), but he "
                        "withdraws -- his kingdom is 'not of this world' (18:36). That evening, Jesus "
                        "walks on the Sea of Galilee toward the disciples' boat. John records: 'They were "
                        "frightened. But he said to them, \"ego eimi (I AM); do not be afraid\"' (6:19-20). "
                        "On the surface, ego eimi means 'It is I' -- reassurance. But in John's theology, "
                        "it carries the divine name overtones. Jesus walking on the chaos waters, speaking "
                        "the divine name, calming fear -- this is a theophany. The one who 'trampled the "
                        "waves of the sea' (Job 9:8) and whose 'way was through the sea' (Ps 77:19) has "
                        "appeared in person."
            },
            {
                "heading": "The Bread of Life Discourse (6:22-71)",
                "body": "The crowd follows Jesus to Capernaum seeking more bread. Jesus redirects: 'Do not "
                        "work for the food that perishes' (6:27). They demand a sign comparable to Moses' "
                        "manna: 'He gave them bread from heaven to eat' (6:31, quoting Ps 78:24). Jesus' "
                        "response reinterprets the manna tradition at every level: (1) It was not Moses "
                        "but the Father who gave the manna (6:32a). (2) The manna was not the 'true "
                        "bread' -- Jesus is (6:32b). (3) The manna sustained physical life temporarily; "
                        "the true bread gives eternal life (6:49-51). The first Bread of Life declaration: "
                        "'I am the bread of life. Whoever comes to me shall not hunger, and whoever "
                        "believes in me shall never thirst' (6:35). The Jews 'grumble' (egogguzon -- "
                        "6:41, the same verb used of Israel's grumbling in the wilderness, Exod 16:2) "
                        "because they know his parents: 'Is not this Jesus, the son of Joseph? How does "
                        "he now say, \"I have come down from heaven\"?' (6:42). The discourse escalates: "
                        "'I am the living bread that came down from heaven... the bread that I will give "
                        "for the life of the world is my flesh' (6:51). The language becomes deliberately "
                        "visceral: 'eat the flesh of the Son of Man and drink his blood' (6:53); 'my "
                        "flesh is true food, and my blood is true drink' (6:55); 'whoever feeds on me "
                        "(ho trogon me -- literally 'chews/gnaws on me'), he also will live because of "
                        "me' (6:57). This language points both to the eucharist and to the cross -- the "
                        "giving of Jesus' body and blood. Many disciples cannot accept it: 'This is a "
                        "hard saying; who can listen to it?' (6:60). Jesus does not soften: 'It is the "
                        "Spirit who gives life; the flesh is no help at all. The words that I have "
                        "spoken to you are spirit and life' (6:63). Many leave. Peter speaks for the "
                        "Twelve: 'Lord, to whom shall we go? You have the words of eternal life, and we "
                        "have believed, and have come to know, that you are the Holy One of God (ho "
                        "hagios tou theou)' (6:68-69). The title 'Holy One of God' is a divine council "
                        "designation -- the one uniquely set apart (sanctified) by God for his mission."
            }
        ]
    },

    {
        "id": "john-7-8",
        "ref": "John 7-8",
        "chapter_num": 5,
        "title": "The Festival of Tabernacles -- Living Water, Light of the World, and the I AM",
        "era": "john_signs",
        "type": "chapter",
        "themes": ["SEED", "KING", "DC", "TYPE", "BLOOD"],

        "synopsis": "Chapters 7-8 are set during the Festival of Tabernacles (Sukkot) in Jerusalem -- "
                    "the most joyful and symbolically rich festival of the Jewish calendar. The festival "
                    "celebrated the wilderness wandering, commemorating God's provision of water, light, "
                    "and shelter. Two key ceremonies framed the festival: (1) the water-pouring ceremony "
                    "(nisukh ha-mayim), where a priest drew water from the Pool of Siloam and poured it "
                    "on the altar while the people sang Isaiah 12:3 ('With joy you will draw water from "
                    "the wells of salvation'); and (2) the lighting of the great menorot (candelabra) in "
                    "the Court of the Women, illuminating the entire Temple complex. Against this "
                    "backdrop, Jesus makes two staggering claims. On the last day of the festival, he "
                    "stands and cries out: 'If anyone thirsts, let him come to me and drink. Whoever "
                    "believes in me, as the Scripture has said, \"Out of his heart will flow rivers of "
                    "living water\"' (7:37-38). John explains: 'Now this he said about the Spirit, "
                    "whom those who believed in him were to receive' (7:39). Then in chapter 8: 'I am "
                    "the light of the world (ego eimi to phos tou kosmou). Whoever follows me will not "
                    "walk in darkness, but will have the light of life' (8:12). The discourse with the "
                    "Pharisees escalates to the climactic ego eimi: 'Before Abraham was, I AM' (8:58). "
                    "They pick up stones to kill him.",

        "key_verse": {
            "ref": "John 8:12, 58",
            "text": "Again Jesus spoke to them, saying, 'I am the light of the world. Whoever follows me will not walk in darkness, but will have the light of life.'... Jesus said to them, 'Truly, truly, I say to you, before Abraham was, I AM.'",
            "translation": "ESV"
        },

        "original_terms": [
            "Sukkot (Festival of Tabernacles/Booths -- the seven-day harvest festival celebrating God's "
            "provision in the wilderness; the most joyful festival, associated with water and light)",
            "nisukh ha-mayim (water-pouring ceremony -- the priest drew water from the Pool of Siloam and "
            "poured it on the altar during Sukkot; the background for 7:37-38)",
            "to phos tou kosmou (the light of the world -- the second I AM + predicate; spoken during "
            "Sukkot when the Temple was illuminated by four great candelabra; Jesus claims to be "
            "what the festival symbolized)",
            "ego eimi (I AM -- the absolute form in 8:24, 28, 58; the claim to the divine name from "
            "Exodus 3:14; the most direct claim to deity in the Gospels)",
            "eleutheros (free -- 8:32, 36; 'the truth will set you free'; 'if the Son sets you free, "
            "you will be free indeed')",
            "sperma Abraam (seed of Abraham -- 8:33, 37; the Jewish claim to covenant status through "
            "physical descent; Jesus argues spiritual ancestry matters more)"
        ],

        "ane_backdrop": "The Festival of Tabernacles had deep agricultural and cosmological roots in the "
                        "ANE. The autumn harvest festival was universal in ancient agrarian societies, and "
                        "the water-pouring ceremony reflects the ancient Near Eastern concern for rain at "
                        "the transition from the dry to the rainy season. Zechariah 14:16-19 envisions "
                        "all nations coming to Jerusalem for Sukkot in the messianic age -- the nations "
                        "must worship YHWH or receive no rain. The light ceremonies connect to the "
                        "widespread ANE symbolism of the divine as light: Egyptian sun worship, the "
                        "Mesopotamian light-god Shamash, and the biblical tradition of YHWH as light "
                        "(Ps 27:1; Isa 60:19-20). Jesus' claim to be 'the light of the world' during "
                        "the festival's light ceremony is a direct claim to be what the festival's "
                        "symbolism pointed to -- the divine light that illuminates the nations.",

        "second_temple": [
            {
                "source": "Mishnah Sukkah 4:9-10; 5:1-4",
                "summary": "The Mishnah describes the water-pouring ceremony in detail: the golden pitcher "
                           "filled at the Pool of Siloam, the procession to the altar, the pouring of "
                           "water and wine, and the great rejoicing. The lighting ceremony: 'Men of piety "
                           "and good works used to dance before them with burning torches in their hands.'",
                "relevance": "The Mishnah preserves the liturgical context for Jesus' claims: the water "
                             "and light ceremonies were the precise setting in which he declared himself "
                             "the living water (7:37-38) and the light of the world (8:12)."
            },
            {
                "source": "Isaiah 9:1-2",
                "summary": "'The people who walked in darkness have seen a great light; those who dwelt "
                           "in a land of deep darkness, on them has light shone.'",
                "relevance": "Isaiah's prophecy of eschatological light is the backdrop for Jesus' 'I am "
                             "the light of the world' (8:12). The light that shines in the darkness "
                             "(cf. John 1:5) is now personally present."
            },
            {
                "source": "Dead Sea Scrolls: 1QS 3:13-4:26",
                "summary": "The Rule of the Community's 'two spirits' section describes the 'Prince of "
                           "Light' who leads the 'sons of light' against the 'Angel of Darkness' and "
                           "the 'sons of darkness.'",
                "relevance": "John's light/darkness dualism (1:5; 3:19-21; 8:12; 12:35-46) has parallels "
                             "in Qumran's cosmic dualism, both drawing on the OT's divine council "
                             "framework of light versus rebellious darkness."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 13:21-22", "note": "'The LORD went before them by day in a pillar of cloud... and by night in a pillar of fire to give them light' -- Jesus as the pillar of fire, the 'light of the world'", "type": "ot"},
            {"ref": "Isaiah 12:3", "note": "'With joy you will draw water from the wells of salvation' -- sung during Sukkot's water-pouring ceremony; fulfilled in Jesus' offer of living water (7:37-38)", "type": "ot"},
            {"ref": "Exodus 3:14", "note": "'I AM WHO I AM (ehyeh asher ehyeh)' -- the divine name that Jesus claims in 8:24, 28, 58", "type": "ot"},
            {"ref": "Isaiah 43:10", "note": "'You are my witnesses... that you may know and believe me and understand that I AM HE (ani hu)' -- the divine self-identification that Jesus echoes", "type": "ot"},
            {"ref": "Zechariah 14:8, 16-19", "note": "Living waters flowing from Jerusalem; all nations coming to keep the Festival of Tabernacles -- the eschatological Sukkot Jesus fulfills", "type": "ot"},
            {"ref": "Revelation 21:23-24", "note": "'The city has no need of sun or moon to shine on it, for the glory of God gives it light, and its lamp is the Lamb' -- the eschatological fulfillment of 'I am the light of the world'", "type": "nt"},
            {"ref": "Revelation 22:1", "note": "'The river of the water of life, bright as crystal, flowing from the throne of God and of the Lamb' -- the eschatological 'living water' of 7:37-38", "type": "nt"}
        ],

        "divine_council_note": "The ego eimi declarations of chapters 7-8 are the most explicit divine name "
                               "claims in the Gospels. 'Before Abraham was, I AM' (8:58) is not merely a "
                               "claim to pre-existence; it is a claim to the divine name. The verb tense is "
                               "critical: 'Before Abraham was (genesthai -- came into being, aorist), I AM "
                               "(ego eimi -- present tense, continuous existence).' Abraham came into being at "
                               "a point in time; Jesus simply IS -- his existence is not bounded by time. This "
                               "is the language of deity, not merely of an exalted being. The reaction of the "
                               "audience -- picking up stones (8:59) -- confirms they understood: he was "
                               "claiming to be the 'I AM' of Exodus 3:14. In 8:24, Jesus says 'unless you "
                               "believe that ego eimi, you will die in your sins.' This is not 'unless you "
                               "believe that I am the Messiah' -- it is 'unless you believe that I AM.' The "
                               "divine name is the content of salvific faith. In the divine council framework, "
                               "the 'I AM' is the name of the God who presides over the council, the God of "
                               "Psalm 82 who stands in the assembly. Jesus claims this name for himself, "
                               "identifying himself as the YHWH of the Old Testament -- the second power in "
                               "heaven, the visible God, the Logos who was 'with God and was God.'",

        "sections": [
            {
                "heading": "The Water of Life at Tabernacles (7:1-52)",
                "body": "Jesus goes to Jerusalem 'in secret' (7:10) during Tabernacles while the people "
                        "debate his identity: 'Is he a good man or a deceiver?' (7:12). Midway through "
                        "the festival, he teaches in the Temple (7:14), astonishing the authorities with "
                        "his learning (7:15). On 'the last day of the feast, the great day' (7:37) -- "
                        "when the water-pouring ceremony reached its climax -- Jesus stands and cries "
                        "out: 'If anyone thirsts, let him come to me and drink. Whoever believes in me, "
                        "as the Scripture has said, \"Out of his heart (koilia -- belly, innermost being) "
                        "will flow rivers of living water\"' (7:37-38). John explains this refers to the "
                        "Spirit (7:39). The moment is dramatically staged: at the very instant the priest "
                        "pours water on the altar in the ceremony that symbolized God's provision and "
                        "the eschatological hope of living water flowing from Jerusalem (Zech 14:8; Ezek "
                        "47:1-12), Jesus declares that HE is the source of that water. The people are "
                        "divided: 'This really is the Prophet' (7:40); 'This is the Christ' (7:41); "
                        "'Is the Christ to come from Galilee?' (7:41). The authorities attempt to arrest "
                        "him but fail: 'No one ever spoke like this man!' (7:46). Nicodemus, who had "
                        "come to Jesus 'by night' (3:2), makes a cautious defense (7:50-51)."
            },
            {
                "heading": "Light of the World and Before Abraham Was, I AM (8:12-59)",
                "body": "Speaking in the Temple treasury (8:20), near the great candelabra that illuminated "
                        "Sukkot, Jesus declares: 'I am the light of the world (ego eimi to phos tou "
                        "kosmou). Whoever follows me will not walk in darkness, but will have the light "
                        "of life' (8:12). The claim evokes the pillar of fire that led Israel through the "
                        "wilderness (Exod 13:21), the divine light of creation (Gen 1:3), and YHWH himself "
                        "as light (Ps 27:1; Isa 60:19-20). The Pharisees challenge his self-testimony; "
                        "Jesus responds by pointing to the Father as his second witness (8:17-18). The "
                        "discourse escalates: 'Unless you believe that ego eimi (I AM), you will die in "
                        "your sins' (8:24). 'When you have lifted up the Son of Man, then you will know "
                        "that ego eimi' (8:28) -- the crucifixion will reveal the divine identity. The "
                        "debate about Abraham's descendants (8:31-47) is sharp: Jesus asserts they are "
                        "children of the devil (8:44), not true children of Abraham. The climax: 'Your "
                        "father Abraham rejoiced that he would see my day. He saw it and was glad' (8:56). "
                        "'You are not yet fifty years old, and have you seen Abraham?' (8:57). 'Truly, "
                        "truly, I say to you, before Abraham was (genesthai -- came into being), ego eimi "
                        "(I AM -- continuous, timeless existence)' (8:58). They pick up stones to kill "
                        "him. The contrast between genesthai (aorist, a moment in time) and eimi (present, "
                        "continuous being) is the contrast between the created and the uncreated, the "
                        "temporal and the eternal. Jesus claims to exist before and beyond all creation -- "
                        "the eternal I AM of Exodus 3:14."
            }
        ]
    },

    {
        "id": "john-9-10",
        "ref": "John 9-10",
        "chapter_num": 6,
        "title": "The Man Born Blind, the Good Shepherd, and the Psalm 82 Debate",
        "era": "john_signs",
        "type": "chapter",
        "themes": ["DC", "SEED", "HOLY", "KING", "NATIONS"],

        "synopsis": "Chapters 9-10 contain two of John's most important narratives: the healing of the "
                    "man born blind (chapter 9 -- the sixth sign) and the Good Shepherd discourse with "
                    "the Psalm 82 debate (chapter 10). In chapter 9, Jesus heals a man blind from birth "
                    "by making mud with saliva and sending him to wash in the Pool of Siloam (9:6-7). "
                    "The Pharisees investigate, divide over the Sabbath healing, interrogate the man "
                    "and his parents (who fear the aposynagogos -- expulsion from the synagogue, 9:22), "
                    "and ultimately expel the healed man himself. Jesus finds him and asks: 'Do you "
                    "believe in the Son of Man?' The man asks who this is, and Jesus says: 'You have "
                    "seen him, and it is he who is speaking to you' (9:37). The man responds: 'Lord, "
                    "I believe,' and worships (prosekynesin) him (9:38). Jesus declares: 'For judgment "
                    "I came into this world, that those who do not see may see, and those who see may "
                    "become blind' (9:39). Chapter 10 opens with the shepherd imagery: 'I am the good "
                    "shepherd (ego eimi ho poimen ho kalos). The good shepherd lays down his life for "
                    "the sheep' (10:11). Jesus distinguishes himself from hired hands who flee when the "
                    "wolf comes. He speaks of 'other sheep that are not of this fold' (10:16) -- the "
                    "Gentile mission. 'I lay down my life that I may take it up again. No one takes it "
                    "from me, but I lay it down of my own accord' (10:17-18). At the Festival of "
                    "Dedication (Hanukkah -- 10:22), Jesus walks in Solomon's Colonnade. The Jews "
                    "demand: 'If you are the Christ, tell us plainly' (10:24). Jesus responds: 'I and "
                    "the Father are one (hen)' (10:30). They pick up stones. He asks: 'For which good "
                    "work do you stone me?' They answer: 'For blasphemy, because you, being a man, make "
                    "yourself God' (10:33). Jesus then quotes Psalm 82:6: 'Is it not written in your "
                    "Law, \"I said, you are gods\"?' (10:34) and makes the a fortiori argument -- the "
                    "most direct engagement with divine council theology in the New Testament.",

        "key_verse": {
            "ref": "John 10:30, 34-36",
            "text": "'I and the Father are one.'... Jesus answered them, 'Is it not written in your Law, \"I said, you are gods\"? If he called them gods to whom the word of God came -- and Scripture cannot be broken -- do you say of him whom the Father consecrated and sent into the world, \"You are blaspheming,\" because I said, \"I am the Son of God\"?'",
            "translation": "ESV"
        },

        "original_terms": [
            "poimen ho kalos (the good/noble shepherd -- the fourth I AM + predicate; echoes YHWH as "
            "Israel's shepherd in Ps 23:1; Isa 40:11; Ezek 34:11-16; Jesus claims the divine role)",
            "hen (one -- 10:30; neuter, indicating unity of nature/essence/will, not personal identity; "
            "'I and the Father are one thing,' not 'one person')",
            "theoi (gods -- 10:34, quoting Ps 82:6; the Greek rendering of Hebrew elohim; divine council "
            "members to whom God assigned authority over the nations)",
            "hegiasen (consecrated/sanctified -- 10:36; set apart for a sacred purpose; the Father "
            "consecrated the Son and sent him into the world)",
            "aposynagogos (expelled from the synagogue -- 9:22; 12:42; 16:2; reflects the painful "
            "separation between the early Christian community and the Jewish synagogue)",
            "Siloam (Sent -- 9:7; John notes the etymology: the pool's name means 'Sent,' pointing "
            "to Jesus as the one 'sent' by the Father)"
        ],

        "ane_backdrop": "The shepherd imagery has deep ANE roots. In Mesopotamia and Egypt, kings were "
                        "called 'shepherds' of their people -- the Code of Hammurabi opens with Hammurabi "
                        "as the 'shepherd' of the people, and Egyptian pharaohs carried a shepherd's crook "
                        "as a symbol of royal authority. In the Old Testament, YHWH himself is Israel's "
                        "shepherd (Ps 23:1; 80:1; Isa 40:11), and the failure of Israel's human leaders "
                        "is described as the failure of bad shepherds (Ezek 34). The Festival of Dedication "
                        "(Hanukkah, 10:22) commemorated the Maccabean rededication of the Temple in 164 BC "
                        "after its desecration by Antiochus IV Epiphanes. The question 'Are you the Christ?' "
                        "(10:24) takes on special resonance during a festival celebrating the last great "
                        "deliverance -- the people want to know if Jesus will be a new Judas Maccabeus.",

        "second_temple": [
            {
                "source": "Ezekiel 34:11-16, 23-24",
                "summary": "'I myself will search for my sheep and will seek them out... I will set up "
                           "over them one shepherd, my servant David, and he shall feed them... And I, "
                           "the LORD, will be their God, and my servant David shall be prince among them.'",
                "relevance": "Ezekiel prophesied that YHWH himself would shepherd Israel AND that a "
                             "Davidic shepherd would be appointed. Jesus fulfills BOTH roles: he is "
                             "simultaneously the divine shepherd (YHWH) and the Davidic shepherd-king. "
                             "The 'two powers' theology again."
            },
            {
                "source": "Psalm 82:1-8",
                "summary": "'God (Elohim) stands in the divine assembly (adat el); in the midst of the "
                           "gods (elohim) he renders judgment... I said, \"You are gods (elohim), sons of "
                           "the Most High (bene elyon), all of you; nevertheless, like men you shall die.\"'",
                "relevance": "Jesus quotes this psalm in 10:34 to make his a fortiori argument: if the "
                             "divine council members are called 'gods,' how much more can the one whom the "
                             "Father consecrated and sent claim divine sonship? This is the NT's most direct "
                             "engagement with divine council theology."
            },
            {
                "source": "1 Maccabees 4:36-59",
                "summary": "The rededication of the Temple after Antiochus IV's desecration: Judas "
                           "Maccabeus cleanses the sanctuary and lights new lamps on the 25th of Kislev.",
                "relevance": "The Festival of Dedication/Hanukkah (10:22) commemorates this event. Jesus' "
                             "claims during this festival -- 'I and the Father are one' (10:30) -- assert "
                             "that he, not the Temple, is the true locus of God's presence."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 23:1", "note": "'The LORD is my shepherd' -- Jesus claims this divine role: 'I am the good shepherd' (10:11)", "type": "ot"},
            {"ref": "Ezekiel 34:11-16, 23", "note": "YHWH will shepherd Israel himself and raise up a Davidic shepherd -- Jesus fulfills both roles simultaneously", "type": "ot"},
            {"ref": "Psalm 82:1-8", "note": "The divine council judgment scene -- quoted by Jesus in 10:34 to defend his claim to be the Son of God", "type": "ot"},
            {"ref": "Isaiah 42:6-7", "note": "'I will give you as a light to the nations, to open the eyes that are blind' -- Jesus as the light who gives sight to the blind man in chapter 9", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God -- the Psalm 82 background that makes Jesus' quotation in 10:34 intelligible", "type": "ot"},
            {"ref": "Hebrews 13:20", "note": "'The great shepherd of the sheep' -- applying the shepherd title to the risen Jesus", "type": "nt"},
            {"ref": "1 Peter 5:4", "note": "'When the chief Shepherd appears, you will receive the unfading crown of glory' -- the eschatological shepherd", "type": "nt"},
            {"ref": "Revelation 7:17", "note": "'The Lamb in the midst of the throne will be their shepherd, and he will guide them to springs of living water' -- shepherd and lamb united", "type": "nt"}
        ],

        "divine_council_note": "John 10:34-36 is the single most important verse in the New Testament for "
                               "the divine council framework. When Jesus quotes Psalm 82:6 -- 'I said, you "
                               "are gods (theoi)' -- he is directly citing the divine council judgment scene "
                               "where YHWH addresses the assembled elohim and pronounces sentence on them. "
                               "His argument is a fortiori: (1) Scripture calls the divine council members "
                               "'gods' (elohim/theoi). These are real spiritual beings who received authority "
                               "from God ('to whom the word of God came'). (2) 'Scripture cannot be broken' -- "
                               "the designation 'gods' is authoritative and true. (3) If created spiritual "
                               "beings can legitimately be called 'gods,' how much more can the one whom the "
                               "Father 'consecrated (hegiasen) and sent into the world' be called 'the Son of "
                               "God'? The argument only works if the 'gods' of Psalm 82 are real divine "
                               "beings. If they were merely human judges (the rabbinic deflection), the "
                               "argument collapses -- calling a human judge 'god' as a courtesy does not "
                               "establish the right to claim genuine divine sonship. Jesus is placing himself "
                               "in the divine council hierarchy and claiming to be above all the council "
                               "members: they are elohim by nature and assignment; he is the Son of God by "
                               "unique consecration and mission from the Father. They were judged and "
                               "sentenced to 'die like men' (Ps 82:7); he will die voluntarily ('I lay down "
                               "my life of my own accord,' 10:18) and rise again. The statement 'I and the "
                               "Father are one' (10:30) is the culmination: the Son and the Father are not "
                               "separate gods in a pantheon but one in essence, will, and purpose. This is "
                               "the divine council's 'two powers in heaven' resolved into unity -- two "
                               "persons, one God. The healed blind man's worship of Jesus (9:38) is the "
                               "appropriate response: if Jesus is who he claims to be, he is worthy of the "
                               "worship that belongs to God alone.",

        "sections": [
            {
                "heading": "The Man Born Blind -- Physical and Spiritual Sight (9:1-41)",
                "body": "Jesus encounters a man blind from birth. The disciples ask whose sin caused the "
                        "blindness -- his or his parents' (9:2). Jesus rejects the premise: 'It was not "
                        "that this man sinned, or his parents, but that the works of God might be "
                        "displayed in him' (9:3). He declares: 'As long as I am in the world, I am the "
                        "light of the world' (9:5) -- connecting this sign to the 'I AM' of 8:12. He "
                        "makes mud with saliva (recalling God forming Adam from the ground, Gen 2:7), "
                        "applies it to the man's eyes, and sends him to wash in the Pool of Siloam "
                        "(Siloam means 'Sent' -- 9:7, pointing to Jesus as the one 'sent' by the "
                        "Father). The man washes and sees. What follows is a masterful narrative of "
                        "increasing sight and increasing blindness: the healed man's understanding grows "
                        "(from 'the man called Jesus' to 'a prophet' to 'Lord, I believe' and worship), "
                        "while the Pharisees' understanding darkens (from investigation to accusation to "
                        "expulsion). The parents refuse to testify 'because they feared the Jews, for "
                        "the Jews had already agreed that if anyone should confess Jesus to be Christ, "
                        "he was to be put out of the synagogue (aposynagogos)' (9:22). This reflects the "
                        "painful historical reality of the Johannine community's expulsion from the "
                        "synagogue. The man's logic is devastating: 'If this man were not from God, he "
                        "could do nothing' (9:33). They throw him out. Jesus finds him and reveals "
                        "himself as the Son of Man (9:35-37). The man believes and worships -- the "
                        "response of true sight. Jesus pronounces the ironic judgment: 'For judgment I "
                        "came into this world, that those who do not see may see, and those who see may "
                        "become blind' (9:39)."
            },
            {
                "heading": "The Good Shepherd and the Psalm 82 Debate (10:1-42)",
                "body": "Jesus delivers the shepherd parable-discourse, distinguishing the true shepherd "
                        "from thieves and hired hands. The good shepherd 'calls his own sheep by name "
                        "and leads them out' (10:3); the sheep 'know his voice' (10:4). 'I am the door "
                        "(he thyra); if anyone enters by me, he will be saved' (10:9). 'I am the good "
                        "shepherd (ho poimen ho kalos). The good shepherd lays down his life for the "
                        "sheep' (10:11). The 'hired hand' (misthotos) flees when the wolf (lykos) comes "
                        "(10:12-13) -- the false leaders of Israel who abandoned the flock. Jesus mentions "
                        "'other sheep that are not of this fold' (10:16) -- the Gentiles who will be "
                        "gathered into one flock under one shepherd. The voluntary nature of his death is "
                        "emphasized: 'No one takes it from me, but I lay it down of my own accord. I "
                        "have authority to lay it down, and I have authority to take it up again' (10:18). "
                        "At Hanukkah, the confrontation intensifies. 'I and the Father are one (hen)' "
                        "(10:30). The neuter hen (one thing) rather than heis (one person) indicates unity "
                        "of nature and will, not identity of persons -- exactly the 'two powers' theology "
                        "of the divine council. The Jews prepare to stone him for blasphemy: 'You, being "
                        "a man, make yourself God (theon)' (10:33). Jesus responds with Psalm 82:6 and "
                        "the devastating a fortiori argument. He then appeals to his works: 'If I am not "
                        "doing the works of my Father, then do not believe me; but if I do them, even "
                        "though you do not believe me, believe the works, that you may know and understand "
                        "that the Father is in me and I am in the Father' (10:37-38). The mutual "
                        "indwelling of Father and Son -- 'the Father is in me and I am in the Father' -- "
                        "is the relational core of the divine council's 'two powers' theology. Two "
                        "distinct persons, completely interpenetrating, one God."
            }
        ]
    },

    {
        "id": "john-11-12",
        "ref": "John 11-12",
        "chapter_num": 7,
        "title": "The Resurrection and the Life -- Lazarus, the Anointing, and the Arrival of the Hour",
        "era": "john_signs",
        "type": "chapter",
        "themes": ["DC", "KING", "SEED", "REBEL", "TYPE"],

        "synopsis": "Chapters 11-12 form the climactic conclusion of the Book of Signs. Chapter 11 "
                    "narrates the raising of Lazarus -- the seventh and greatest sign -- which reveals "
                    "Jesus as 'the resurrection and the life' (11:25) and, ironically, triggers the "
                    "plot to kill him. Lazarus has been dead four days (11:39) when Jesus arrives in "
                    "Bethany. Martha meets him and says: 'Lord, if you had been here, my brother would "
                    "not have died' (11:21). Jesus responds: 'I am the resurrection and the life (ego "
                    "eimi he anastasis kai he zoe). Whoever believes in me, though he die, yet shall "
                    "he live, and everyone who lives and believes in me shall never die. Do you believe "
                    "this?' (11:25-26). Martha confesses: 'Yes, Lord; I believe that you are the Christ, "
                    "the Son of God, who is coming into the world' (11:27) -- a confession as comprehensive "
                    "as Peter's in the Synoptics. At the tomb, Jesus weeps (edakrysen -- 11:35, the "
                    "shortest verse in the Bible in English), then commands: 'Lazarus, come out!' (11:43). "
                    "The dead man comes out, still bound in grave clothes. 'Unbind him, and let him go' "
                    "(11:44). The Sanhedrin convenes and Caiaphas prophesies: 'It is better for you that "
                    "one man should die for the people, not that the whole nation should perish' (11:50). "
                    "John notes the irony: Caiaphas spoke better than he knew -- Jesus would die 'for "
                    "the nation, and not for the nation only, but also to gather into one the children "
                    "of God who are scattered abroad' (11:51-52). Chapter 12 narrates Mary's anointing "
                    "of Jesus (12:1-8), the triumphal entry (12:12-19), Greeks seeking Jesus (12:20-22), "
                    "and Jesus' declaration that his 'hour has come' (12:23). The pivotal statement: "
                    "'Now is the judgment of this world; now will the ruler of this world be cast out. "
                    "And I, when I am lifted up from the earth, will draw all people to myself' "
                    "(12:31-32). The Book of Signs closes with a retrospective: 'Though he had done so "
                    "many signs before them, they still did not believe in him' (12:37).",

        "key_verse": {
            "ref": "John 11:25-26; 12:31-32",
            "text": "Jesus said to her, 'I am the resurrection and the life. Whoever believes in me, though he die, yet shall he live, and everyone who lives and believes in me shall never die.'... 'Now is the judgment of this world; now will the ruler of this world be cast out. And I, when I am lifted up from the earth, will draw all people to myself.'",
            "translation": "ESV"
        },

        "original_terms": [
            "he anastasis kai he zoe (the resurrection and the life -- the fifth I AM + predicate; Jesus "
            "does not merely give resurrection; he IS resurrection; life and death are under his "
            "personal authority)",
            "edakrysen (he wept -- 11:35; aorist, a burst of tears; the incarnate God's genuine grief "
            "at death -- even though he knows he will reverse it)",
            "ho archon tou kosmou toutou (the ruler of this world -- 12:31; the hostile spiritual power "
            "who governs the world system; the Deuteronomy 32 worldview's chief adversary)",
            "hypsoo (to lift up/exalt -- 12:32-34; the crucifixion as both execution and enthronement; "
            "the cross lifts Jesus up physically and exalts him cosmically)",
            "he hora (the hour -- 12:23, 27; the divinely appointed moment of Jesus' death, resurrection, "
            "and glorification; anticipated throughout the Gospel: 2:4; 7:30; 8:20)",
            "kokkos tou sitou (grain of wheat -- 12:24; 'unless a grain of wheat falls into the earth "
            "and dies, it remains alone; but if it dies, it bears much fruit' -- the principle of "
            "death as the path to fruitfulness)"
        ],

        "ane_backdrop": "The raising of Lazarus engages the ANE understanding of death and the underworld. "
                        "In Mesopotamian thought, the dead descended to the 'land of no return' (Irkalla), "
                        "ruled by Ereshkigal and Nergal. In the Old Testament, the dead go to Sheol -- a "
                        "shadowy existence, not the full life of communion with God (Ps 6:5; 88:10-12). "
                        "The four-day detail (11:39) is significant: rabbinic tradition held that the "
                        "soul lingered near the body for three days, hoping to return, but departed on "
                        "the fourth day when decomposition was unmistakable (Genesis Rabbah 100:7). By "
                        "raising Lazarus after four days, Jesus demonstrates authority over death at its "
                        "most definitive point. The anointing at Bethany (12:1-8) echoes the ANE practice "
                        "of anointing kings and preparing bodies for burial -- Mary performs both acts "
                        "simultaneously, anointing Jesus as king and preparing him for his death. The "
                        "'ruler of this world' being 'cast out' (12:31) echoes the divine council "
                        "judgment pattern: the rebellious elohim who governed the nations are judged "
                        "and deposed.",

        "second_temple": [
            {
                "source": "Daniel 12:2-3",
                "summary": "'Many of those who sleep in the dust of the earth shall awake, some to "
                           "everlasting life, and some to shame and everlasting contempt.'",
                "relevance": "Martha's belief in 'the resurrection at the last day' (11:24) reflects "
                             "the Pharisaic interpretation of Daniel 12. Jesus does not deny the future "
                             "resurrection but personalizes it: 'I AM the resurrection' -- he is not "
                             "merely the one who will raise the dead at the last day but the one in "
                             "whom resurrection power resides right now."
            },
            {
                "source": "Isaiah 53:4-12",
                "summary": "The Suffering Servant who is 'wounded for our transgressions' and makes "
                           "his life 'an offering for sin' (asham), yet 'shall see his offspring; he "
                           "shall prolong his days.'",
                "relevance": "Caiaphas's unwitting prophecy that 'one man should die for the people' "
                             "(11:50) echoes the Suffering Servant motif. John sees Caiaphas as an "
                             "unconscious prophet: Jesus' death IS substitutionary -- for the nation "
                             "and for the scattered children of God worldwide (11:51-52)."
            },
            {
                "source": "Zechariah 9:9",
                "summary": "'Rejoice greatly, O daughter of Zion!... Behold, your king is coming to "
                           "you, righteous and having salvation, humble and mounted on a donkey.'",
                "relevance": "Jesus' triumphal entry on a donkey (12:14-15) fulfills Zechariah's "
                             "prophecy. John quotes it directly (12:15) and notes that 'his disciples "
                             "did not understand these things at first' (12:16) -- the full meaning "
                             "became clear only after the resurrection."
            },
            {
                "source": "Isaiah 6:10",
                "summary": "'Make the heart of this people dull, and their ears heavy, and blind their "
                           "eyes; lest they see with their eyes, and hear with their ears, and "
                           "understand with their hearts, and turn and be healed.'",
                "relevance": "John quotes this (12:40) to explain Israel's unbelief despite the signs. "
                             "He adds a remarkable statement: 'Isaiah said these things because he saw "
                             "his (Jesus') glory and spoke of him' (12:41). Isaiah's vision of YHWH in "
                             "the Temple (Isa 6:1-5) was a vision of the pre-incarnate Christ -- the "
                             "Logos, the visible YHWH."
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 12:2", "note": "'Many who sleep in the dust of the earth shall awake' -- Martha's hope (11:24) and Jesus' surpassing claim: 'I AM the resurrection' (11:25)", "type": "ot"},
            {"ref": "Isaiah 53:4-12", "note": "The Suffering Servant who dies for the people -- the unwitting prophecy of Caiaphas (11:50)", "type": "ot"},
            {"ref": "Zechariah 9:9", "note": "The king on a donkey -- fulfilled in the triumphal entry (12:14-15)", "type": "ot"},
            {"ref": "Isaiah 6:1-5", "note": "Isaiah's vision of YHWH in the Temple -- John says Isaiah 'saw his (Jesus') glory' (12:41); the pre-incarnate Logos", "type": "ot"},
            {"ref": "Psalm 118:25-26", "note": "'Hosanna! Blessed is he who comes in the name of the Lord!' -- the crowd's cry at the triumphal entry (12:13)", "type": "ot"},
            {"ref": "Ephesians 2:2", "note": "'The prince of the power of the air, the spirit that is now at work in the sons of disobedience' -- Paul's parallel to 'the ruler of this world' (12:31)", "type": "nt"},
            {"ref": "Colossians 2:15", "note": "'He disarmed the rulers and authorities and put them to open shame, triumphing over them in the cross' -- the cross as divine council judgment", "type": "nt"},
            {"ref": "Revelation 12:9", "note": "'The great dragon was thrown down... the deceiver of the whole world -- he was thrown down to the earth' -- the ultimate casting out of the ruler", "type": "nt"}
        ],

        "divine_council_note": "The Book of Signs culminates with three massive divine council themes. "
                               "First, 'I am the resurrection and the life' (11:25): the power to raise "
                               "the dead belongs exclusively to God in the Old Testament (Deut 32:39; 1 Sam "
                               "2:6). When Jesus raises Lazarus -- who has been dead four days -- he exercises "
                               "the most fundamental divine prerogative. He does not pray for resurrection "
                               "(as Elijah and Elisha did, 1 Kings 17; 2 Kings 4); he commands it: 'Lazarus, "
                               "come out!' (11:43). The voice that summons the dead is the voice of the "
                               "divine council's Lord. Second, 12:31: 'Now is the judgment of this world; "
                               "now will the ruler of this world be cast out.' This is the divine council's "
                               "verdict on the hostile spiritual power who has ruled the nations since Babel. "
                               "The 'casting out' (ekblethesetai) uses the exorcism verb -- the cross is "
                               "the cosmic exorcism, the judgment of Psalm 82:8 ('Arise, O God, judge the "
                               "earth!') executed through the death and resurrection of the Son. Third, "
                               "12:41: 'Isaiah said these things because he saw his glory and spoke of him.' "
                               "John identifies the YHWH whom Isaiah saw 'high and lifted up' in the Temple "
                               "vision (Isa 6:1-5) as Jesus. This means Isaiah's vision of the divine "
                               "council throne room -- with the seraphim crying 'Holy, holy, holy is YHWH "
                               "of hosts' -- was a vision of the pre-incarnate Logos. The Logos is the YHWH "
                               "of Isaiah 6, the visible God whom the prophets encountered when they were "
                               "granted access to the divine council.",

        "sections": [
            {
                "heading": "The Raising of Lazarus -- The Seventh Sign (11:1-57)",
                "body": "The structure of chapter 11 is masterful. Lazarus of Bethany is sick; his sisters "
                        "Martha and Mary send word to Jesus: 'Lord, he whom you love is ill' (11:3). "
                        "Jesus deliberately delays two days (11:6), then announces: 'Lazarus has died, "
                        "and for your sake I am glad that I was not there, so that you may believe' "
                        "(11:14-15). By the time Jesus arrives, Lazarus has been in the tomb four days. "
                        "Martha meets Jesus and professes faith in the final resurrection (11:24). Jesus' "
                        "response transcends her expectation: 'I am the resurrection and the life' (11:25). "
                        "He does not say 'I will perform the resurrection' or 'I will give you "
                        "resurrection.' He says he IS resurrection -- the power over death is not a "
                        "capability he possesses but his very nature. Martha's confession (11:27) is "
                        "the fullest christological statement in the Gospels before the crucifixion. When "
                        "Mary comes weeping, 'Jesus wept' (edakrysen, 11:35). The incarnate God who IS "
                        "the resurrection and the life weeps at the tomb of his friend. His grief is not "
                        "ignorance of the outcome but a genuine sharing of human anguish at death -- the "
                        "enemy that has no right to exist in God's good creation. At the tomb, he "
                        "commands the stone removed. Martha warns: 'Lord, by this time there will be an "
                        "odor, for he has been dead four days' (11:39). Jesus prays to the Father (for "
                        "the crowd's sake, 11:42) and cries out 'with a loud voice (phone megale), "
                        "\"Lazarus, come out!\"' (11:43). The specificity of the name is noted by the "
                        "church fathers: had Jesus simply said 'Come out!' all the dead might have "
                        "risen. Lazarus emerges, still wrapped in burial cloths. 'Unbind him, and let "
                        "him go' (11:44). The ironic result: the supreme sign of life triggers the "
                        "decision to pursue Jesus' death. The Sanhedrin convenes, and Caiaphas speaks "
                        "his unwitting prophecy (11:49-52)."
            },
            {
                "heading": "The Arrival of the Hour -- Anointing, Entry, and Judgment (12:1-50)",
                "body": "Six days before Passover, Mary anoints Jesus' feet with 'a pound of expensive "
                        "ointment made from pure nard' (12:3) -- worth a year's wages. Jesus defends "
                        "her: 'She has kept it for the day of my burial' (12:7). The anointing anticipates "
                        "his death; the house 'was filled with the fragrance' (12:3) -- a sensory image "
                        "of the gospel's spread. The triumphal entry (12:12-19) fulfills Zechariah 9:9: "
                        "the king comes on a donkey, not a war horse -- a humble king, not a military "
                        "conqueror. Greeks come seeking Jesus (12:20-22), prompting his declaration: "
                        "'The hour has come for the Son of Man to be glorified' (12:23). The 'hour' "
                        "(hora) that was 'not yet' at Cana (2:4), that the authorities could not "
                        "precipitate (7:30; 8:20), has now arrived. Jesus states the cosmic principle: "
                        "'Unless a grain of wheat falls into the earth and dies, it remains alone; but "
                        "if it dies, it bears much fruit' (12:24). Then the soul's anguish: 'Now is my "
                        "soul troubled. And what shall I say? \"Father, save me from this hour\"? But "
                        "for this purpose I have come to this hour. Father, glorify your name' (12:27-28). "
                        "A voice from heaven responds: 'I have glorified it, and I will glorify it again' "
                        "(12:28). Then the climactic divine council declaration: 'Now is the judgment of "
                        "this world; now will the ruler of this world be cast out. And I, when I am "
                        "lifted up from the earth, will draw all people to myself' (12:31-32). The cross "
                        "is the divine council's judgment on the hostile archon. The lifting up of the "
                        "Son of Man is the mechanism by which the ruler's authority is broken and 'all "
                        "people' -- not just Israel -- are drawn to the true King. The Book of Signs "
                        "closes with John's theological retrospective: 'Isaiah said these things because "
                        "he saw his glory (doxa) and spoke of him' (12:41) -- identifying the YHWH of "
                        "Isaiah 6 as the pre-incarnate Christ. Despite the signs, many did not believe "
                        "(12:37); yet 'many even of the authorities believed in him, but for fear of "
                        "the Pharisees they did not confess it, so that they would not be put out of the "
                        "synagogue (aposynagogoi)' (12:42). The Book of Signs ends with light and "
                        "darkness in tension, the hour arrived, the ruler of this world about to be "
                        "judged."
            }
        ]
    }
]
