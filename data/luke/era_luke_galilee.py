"""
era_luke_galilee.py -- Luke 1-9: Birth, Nazareth Sermon, Miracles, and the Sending of the 72

The first half of Luke establishes the theological framework for the entire
two-volume work. The birth narratives (chapters 1-2) are saturated with OT
echoes, presenting Jesus as the fulfillment of Israel's hopes. The Nazareth
sermon (4:16-30) is Luke's programmatic statement: Jesus reads Isaiah 61
and declares "Today this Scripture has been fulfilled in your hearing." The
Galilean ministry demonstrates the kingdom's power through exorcisms,
healings, and nature miracles. The sending of the Twelve (9:1-6) and the
72 (10:1-20, which falls just after this era's boundary) extends the
kingdom's reach. Peter's confession and the Transfiguration (9:18-36)
reveal Jesus' identity as the Christ and the divine Son. As the section
closes, Jesus "sets his face to go to Jerusalem" (9:51) -- the journey
to the cross begins.
"""

CHAPTERS = [
    {
        "id": "luke-1-2",
        "ref": "Luke 1-2",
        "chapter_num": 1,
        "title": "The Birth Narratives -- Magnificat, Benedictus, and the Light to the Nations",
        "era": "luke_galilee",
        "type": "study",
        "themes": ["DC", "KING", "SEED", "COV", "TYPE"],

        "synopsis": "Luke's birth narratives are the most elaborate in the NT, framing Jesus' arrival "
                    "in the language and cadence of the Old Testament. The angel Gabriel appears to "
                    "Zechariah in the Temple to announce the birth of John the Baptist (1:5-25), then "
                    "to Mary in Nazareth to announce the conception of Jesus: 'The Holy Spirit will "
                    "come upon you, and the power of the Most High (dynamis hypsistou) will overshadow "
                    "you; therefore the child to be born will be called holy -- the Son of God (huios "
                    "theou)' (1:35). Mary's Magnificat (1:46-55) celebrates divine reversal: the "
                    "mighty pulled down, the humble exalted, the hungry filled, the rich sent away "
                    "empty. Zechariah's Benedictus (1:68-79) proclaims the Davidic covenant fulfilled. "
                    "Jesus is born in Bethlehem, placed in a manger. Angels announce to shepherds: "
                    "'For unto you is born this day in the city of David a Savior (soter), who is "
                    "Christ the Lord (Christos Kyrios)' (2:11). The heavenly host praises: 'Glory to "
                    "God in the highest, and on earth peace among those with whom he is pleased!' "
                    "(2:14). At the Temple, Simeon prophesies: 'a light for revelation to the Gentiles, "
                    "and for glory to your people Israel' (2:32). Anna the prophetess confirms the "
                    "redemption of Jerusalem (2:38). At age 12, Jesus is found in the Temple: 'Did "
                    "you not know that I must be in my Father's house?' (2:49).",

        "key_verse": {
            "ref": "Luke 1:35",
            "text": "And the angel answered her, 'The Holy Spirit will come upon you, and the power of the Most High will overshadow you; therefore the child to be born will be called holy -- the Son of God.'",
            "translation": "ESV"
        },

        "original_terms": [
            "hypsistos (Most High -- Greek translation of Hebrew elyon; the divine council title for the supreme God (Deut 32:8 LXX); Gabriel uses it for the Father)",
            "Christos Kyrios (Christ the Lord / Messiah the Lord -- the double title announced to the shepherds; combines the messianic office with the divine name)",
            "soter (Savior -- the angelic announcement's title for Jesus; used for YHWH in the OT: 'I, I am the LORD, and besides me there is no savior,' Isa 43:11)",
            "phos eis apokalypsin ethnon (a light for revelation to the Gentiles -- Simeon's quotation of Isa 42:6/49:6; the universal scope of Jesus' mission)",
            "megalynei (magnifies -- 'My soul magnifies (megalynei) the Lord'; the opening verb of the Magnificat; Mary declares YHWH's greatness)",
            "diatheke (covenant -- 'the oath that he swore to our father Abraham' (1:73); the Abrahamic covenant fulfilled in the birth of the Messiah)"
        ],

        "ane_backdrop": "The birth narratives draw on the ANE motif of the divine birth announcement "
                        "-- an angelic messenger appears to announce the birth of a divinely chosen "
                        "child. Parallels include the birth of Isaac (Gen 18:10-14), Samson (Judg 13:3-5), "
                        "and Samuel (1 Sam 1:17-20). The Magnificat's theme of divine reversal -- the "
                        "mighty brought low, the humble exalted -- echoes Hannah's prayer (1 Sam 2:1-10) "
                        "and the broader ANE wisdom tradition about the gods overturning human social "
                        "orders. The angelic host's appearance to the shepherds (2:8-14) is a theophanic "
                        "event: the 'glory of the Lord' (doxa kyriou) shining around them evokes the "
                        "shekinah glory of the Temple and the Sinai theophany. The census under Augustus "
                        "(2:1-2) serves as an ironic counterpoint: the Roman emperor thinks he rules the "
                        "world, but his census merely fulfills the prophetic plan that the Messiah be "
                        "born in Bethlehem (Micah 5:2).",

        "second_temple": [
            {
                "source": "4Q246 (Aramaic Apocalypse / 'Son of God' text)",
                "summary": "This Qumran fragment describes a figure called 'Son of God' and 'Son of the "
                           "Most High' who will arise and whose kingdom will be eternal. 'He shall be "
                           "hailed as Son of God, and they shall call him Son of the Most High.'",
                "relevance": "The exact titles used in Gabriel's annunciation to Mary (Luke 1:32, 35) -- "
                             "'Son of the Most High' and 'Son of God' -- appear in this pre-Christian "
                             "Jewish text, confirming these were recognized messianic/divine titles."
            },
            {
                "source": "Psalms of Solomon 17:21-32",
                "summary": "The expected 'Son of David' will 'purge Jerusalem from Gentiles... destroy "
                           "the unrighteous rulers... and shepherd the Lord's flock in faithfulness.'",
                "relevance": "Provides the context for the Davidic expectations that Gabriel's "
                             "announcement fulfills -- though Jesus' kingship will be very different "
                             "from the military messiah of the Psalms of Solomon."
            }
        ],

        "cross_refs": [
            {"ref": "1 Samuel 2:1-10", "note": "Hannah's prayer -- the literary model for the Magnificat; divine reversal of the proud and humble", "type": "ot"},
            {"ref": "Isaiah 42:6; 49:6", "note": "'A light to the nations' -- Simeon quotes the Servant Songs, identifying Jesus as the Servant who illuminates the Gentiles", "type": "ot"},
            {"ref": "Micah 5:2", "note": "'But you, O Bethlehem Ephrathah... from you shall come forth for me one who is to be ruler in Israel' -- fulfilled by the census and birth in Bethlehem", "type": "ot"},
            {"ref": "2 Samuel 7:12-16", "note": "The Davidic covenant: 'I will establish the throne of his kingdom forever' -- echoed in Gabriel's words: 'the Lord God will give to him the throne of his father David' (1:32)", "type": "ot"},
            {"ref": "Daniel 7:14", "note": "'His dominion is an everlasting dominion... his kingdom shall not be destroyed' -- echoed in 'of his kingdom there will be no end' (1:33)", "type": "ot"},
            {"ref": "Matthew 1-2", "note": "Matthew's parallel birth narrative -- different details (genealogy, Magi, flight to Egypt) but the same theological claims", "type": "nt"}
        ],

        "divine_council_note": "The birth narratives are dense with divine council language and action. "
                               "Gabriel -- one of only two named angels in the Protestant OT (the other "
                               "is Michael; both appear in Daniel) -- serves as the divine council "
                               "messenger who delivers the Father's decrees. His annunciation to Mary uses "
                               "the divine council title 'Most High' (hypsistos = Hebrew elyon): 'He will "
                               "be great and will be called the Son of the Most High (huios hypsistou). "
                               "And the Lord God will give to him the throne of his father David, and he "
                               "will reign over the house of Jacob forever, and of his kingdom there will "
                               "be no end' (1:32-33). 'Son of the Most High' is a divine council "
                               "designation -- the same language used in Psalm 82:6 ('sons of the Most "
                               "High') for the elohim members of the council. But Jesus is not merely one "
                               "of the bene elyon -- he is THE Son, unique, with an eternal kingdom. The "
                               "angelic host (stratia ouraniou, 'heavenly army,' 2:13) that appears to the "
                               "shepherds is the divine council's military wing -- the same 'host of heaven' "
                               "that 1 Kings 22:19 describes standing around YHWH's throne. Their "
                               "proclamation of 'peace on earth' (2:14) is a divine council decree: the "
                               "King has arrived, and his reign brings shalom. Simeon's prophecy (2:32) "
                               "identifies Jesus as 'a light for revelation to the Gentiles' (phos eis "
                               "apokalypsin ethnon) -- the light that will penetrate the darkness covering "
                               "the nations under the governance of the rebellious elohim.",

        "sections": [
            {
                "heading": "Annunciations: Gabriel's Messages to Zechariah and Mary (1:1-56)",
                "body": "Luke's prologue (1:1-4) is a masterpiece of Hellenistic historiographic style, "
                        "dedicating the work to Theophilus. The narrative begins in the Temple -- the "
                        "place where heaven and earth intersect. Zechariah, an elderly priest, is "
                        "performing the incense offering when Gabriel appears (1:11-20). Gabriel's "
                        "message: Elizabeth will bear a son named John, who will 'go before him in the "
                        "spirit and power of Elijah' (1:17). Zechariah doubts and is struck mute. Six "
                        "months later, Gabriel appears to Mary in Nazareth: 'Greetings, O favored one "
                        "(kecharitomene), the Lord is with you!' (1:28). The message: she will conceive "
                        "by the Holy Spirit and bear a son named Jesus. 'He will be great and will be "
                        "called the Son of the Most High' (1:32). 'Of his kingdom there will be no end' "
                        "(1:33). Mary's response: 'Behold, I am the servant (doule) of the Lord; let it "
                        "be to me according to your word' (1:38). Mary visits Elizabeth; John leaps in "
                        "the womb (1:41). Mary sings the Magnificat: 'My soul magnifies the Lord... he "
                        "has scattered the proud... he has brought down the mighty from their thrones "
                        "and exalted those of humble estate; he has filled the hungry with good things, "
                        "and the rich he has sent away empty' (1:46-55)."
            },
            {
                "heading": "The Birth, the Shepherds, and the Temple Encounters (1:57 - 2:52)",
                "body": "John is born and Zechariah sings the Benedictus (1:68-79): 'Blessed be the "
                        "Lord God of Israel, for he has visited and redeemed his people and has raised "
                        "up a horn of salvation for us in the house of his servant David.' The Benedictus "
                        "is a covenant hymn: God remembers 'his holy covenant, the oath that he swore "
                        "to our father Abraham' (1:72-73). Jesus is born in Bethlehem because of "
                        "Augustus' census -- the emperor unwittingly fulfills Micah 5:2. Angels announce "
                        "to shepherds (social outcasts, unable to observe purity laws) that 'a Savior "
                        "has been born' (2:11). The 'multitude of the heavenly host' (2:13) -- the divine "
                        "council's army -- praises God. Jesus is circumcised on the eighth day (2:21). "
                        "At the Temple, Simeon takes the child and prophesies: 'My eyes have seen your "
                        "salvation... a light for revelation to the Gentiles' (2:30-32). He also warns "
                        "Mary: 'A sword will pierce through your own soul also' (2:35). Anna the "
                        "prophetess 'spoke of him to all who were waiting for the redemption of "
                        "Jerusalem' (2:38). At age 12, Jesus stays behind in the Temple, discussing "
                        "with the teachers: 'Did you not know that I must (dei -- divine necessity) be "
                        "in my Father's house?' (2:49). The inclusio is set: Luke begins and ends "
                        "in the Temple."
            }
        ]
    },

    {
        "id": "luke-3-4",
        "ref": "Luke 3-4",
        "chapter_num": 2,
        "title": "Baptism, Genealogy, and the Nazareth Sermon -- Satan's Claim and YHWH's Anointed",
        "era": "luke_galilee",
        "type": "study",
        "themes": ["KING", "SEED", "DC", "REBEL", "NATIONS"],

        "synopsis": "Luke sets the stage with precise historical synchronization (3:1-2), placing "
                    "John's ministry in world-historical context. Jesus is baptized (3:21-22), the "
                    "heavens open, the Spirit descends, and the Father declares: 'You are my beloved "
                    "Son; with you I am well pleased.' Luke uniquely places the genealogy after the "
                    "baptism (3:23-38), tracing Jesus' lineage all the way back to 'Adam, the son of "
                    "God' (3:38) -- emphasizing Jesus as the representative of all humanity, not just "
                    "Israel. The temptation (4:1-13) includes Luke's distinctive addition: Satan claims "
                    "'all this authority has been delivered to me' (4:6) -- the Deuteronomy 32 worldview "
                    "explicit. The Nazareth sermon (4:16-30) is the programmatic statement of the "
                    "entire Gospel: Jesus reads Isaiah 61:1-2 ('The Spirit of the Lord is upon me, "
                    "because he has anointed me to proclaim good news to the poor'), declares 'Today "
                    "this Scripture has been fulfilled in your hearing' (4:21), and provokes a violent "
                    "reaction when he points to YHWH's grace extending to Gentiles (the widow of "
                    "Zarephath and Naaman the Syrian, 4:25-27).",

        "key_verse": {
            "ref": "Luke 4:5-6",
            "text": "And the devil took him up and showed him all the kingdoms of the world in a moment of time, and said to him, 'To you I will give all this authority and their glory, for it has been delivered to me, and I give it to whom I will.'",
            "translation": "ESV"
        },

        "original_terms": [
            "emoi paradedotai (it has been delivered to me -- Satan's claim of delegated authority over the nations; passive voice implying God as the ultimate source; the Deut 32 worldview)",
            "pneuma kyriou (Spirit of the Lord -- the anointing Spirit of Isaiah 61:1; Jesus is the Spirit-anointed Messiah who proclaims the jubilee)",
            "aphesis (release / forgiveness -- 'to proclaim release to the captives' (4:18); jubilee language from Leviticus 25; liberation from bondage)",
            "dektos (acceptable / favorable -- 'the year of the Lord's favor' (4:19, from Isa 61:2); the jubilee year when debts are canceled and slaves freed)",
            "huios tou theou (Son of God -- the genealogy ends with 'Adam, the son of God' (3:38); Jesus is the true Son who succeeds where Adam failed)"
        ],

        "ane_backdrop": "The Nazareth sermon's quotation of Isaiah 61:1-2 invokes the concept of "
                        "the jubilee year (Leviticus 25) -- the year of release when slaves were freed, "
                        "debts canceled, and land returned to original owners. In the ANE, royal "
                        "edicts of 'release' (Akkadian andurarum, cognate to Hebrew deror, 'liberty') "
                        "were proclaimed by new kings at their accession -- releasing prisoners, "
                        "canceling debts, and restoring order. Jesus' Nazareth declaration is his "
                        "accession announcement: the true King has arrived, and his reign means liberty "
                        "for the captives. The genealogy tracing to Adam (3:38) sets Jesus in the "
                        "broadest possible context: he is not merely the Messiah of Israel but the "
                        "representative of all humanity, the second Adam who will succeed where the "
                        "first failed.",

        "second_temple": [
            {
                "source": "11QMelchizedek (11Q13)",
                "summary": "This Qumran text applies Isaiah 61:1-2 to the eschatological jubilee, "
                           "when Melchizedek will proclaim release, execute judgment against Belial "
                           "and the spirits of his lot, and establish God's kingdom.",
                "relevance": "Shows that Isaiah 61's jubilee was interpreted eschatologically at "
                             "Qumran -- the same text Jesus claims to fulfill in the Nazareth sermon."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 61:1-2", "note": "'The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the poor' -- the text Jesus reads and declares fulfilled", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God -- the theological background to Satan's claim of authority over 'all the kingdoms of the world' (4:5-6)", "type": "ot"},
            {"ref": "1 Kings 17:8-24", "note": "Elijah and the widow of Zarephath -- Jesus' example of YHWH's grace to Gentiles (4:25-26) that provokes Nazareth's fury", "type": "ot"},
            {"ref": "2 Kings 5:1-14", "note": "Naaman the Syrian healed of leprosy -- Jesus' second example (4:27) of YHWH's grace to Gentiles bypassing Israel", "type": "ot"},
            {"ref": "Leviticus 25:8-17", "note": "The jubilee legislation: release of slaves, cancellation of debts -- the background to the 'year of the Lord's favor' (4:19)", "type": "ot"},
            {"ref": "Matthew 4:1-11", "note": "Matthew's temptation -- same three tests in different order; Matthew places the kingdoms temptation last; Luke places it second", "type": "nt"}
        ],

        "divine_council_note": "Luke 4:5-6 is the most explicit divine council text in the temptation "
                               "narratives. Satan shows Jesus 'all the kingdoms of the world in a moment "
                               "of time' (en stigme chronou, 4:5) -- a supernatural display of the entire "
                               "network of national authorities under his control. His claim is specific: "
                               "'To you I will give all this authority (exousia) and their glory (doxa), "
                               "for it has been delivered to me (emoi paradedotai), and I give it to whom "
                               "I will' (4:6). The passive voice paradedotai ('has been delivered') implies "
                               "a deliverer -- God himself, through the Deuteronomy 32 allotment at Babel. "
                               "Satan does not claim to have seized this authority by force; he claims it "
                               "was 'delivered' to him. In the Deut 32 framework, the nations were assigned "
                               "to the bene elohim at Babel, and these spiritual rulers have corrupted "
                               "their governance. Satan, as the chief adversary, claims to exercise "
                               "authority over the entire network of territorial spirits. His offer is a "
                               "genuine shortcut: worship me and receive the nations without the cross. "
                               "Jesus refuses. The Nazareth sermon (4:16-30) is the counter-proclamation: "
                               "the Spirit-anointed Messiah announces the jubilee -- the release of captives "
                               "from the bondage of sin, disease, and the hostile powers. When Jesus "
                               "mentions YHWH's grace to Gentiles (Zarephath, Naaman), the Nazareth crowd "
                               "tries to kill him (4:28-29) -- because the implication is that the kingdom "
                               "is not just for Israel. The nations that Satan claims to control are being "
                               "reclaimed by grace.",

        "sections": [
            {
                "heading": "Baptism, Genealogy, and Temptation (3:1 - 4:13)",
                "body": "Luke sets the scene with six-fold historical synchronization: 'In the fifteenth "
                        "year of the reign of Tiberius Caesar, Pontius Pilate being governor of Judea, "
                        "and Herod being tetrarch of Galilee...' (3:1-2). John preaches repentance and "
                        "gives practical ethical instruction (3:10-14). Jesus is baptized while praying "
                        "(a Lukan addition: Jesus often prays at key moments). The heavens open, the "
                        "Spirit descends, and the voice declares: 'You are my beloved Son; with you I "
                        "am well pleased' (3:22). Luke's genealogy (3:23-38) goes backward from Jesus "
                        "through David and Abraham to 'Adam, the son of God (huios theou)' -- Jesus is "
                        "the new Adam, the true Son. In the temptation (4:1-13), Luke places the "
                        "kingdoms temptation second (Matthew has it third). Satan's explicit claim: "
                        "'all this authority has been delivered to me' (4:6). Jesus responds with "
                        "Deuteronomy 6:8 and 6:12-13. Luke uniquely notes that the devil 'departed "
                        "from him until an opportune time (achri kairou)' (4:13) -- the battle is "
                        "not over; Satan will return, particularly in the passion (22:3, 31, 53)."
            },
            {
                "heading": "The Nazareth Sermon: The Kingdom's Manifesto (4:14-30)",
                "body": "Jesus returns to Nazareth 'in the power of the Spirit' (4:14). In the synagogue "
                        "on the Sabbath, he reads from the scroll of Isaiah: 'The Spirit of the Lord is "
                        "upon me, because he has anointed me to proclaim good news to the poor. He has "
                        "sent me to proclaim liberty to the captives and recovering of sight to the "
                        "blind, to set at liberty those who are oppressed, to proclaim the year of the "
                        "Lord's favor' (4:18-19, quoting Isa 61:1-2). He rolls up the scroll and sits "
                        "down. Every eye is fixed on him. 'Today this Scripture has been fulfilled in "
                        "your hearing (en tois osin hymon)' (4:21). The crowd marvels at first. But "
                        "Jesus presses: 'No prophet is acceptable in his hometown' (4:24). Then the "
                        "devastating comparison: Elijah was sent not to any widow in Israel but to a "
                        "Gentile widow in Zarephath; Elisha healed not any Israelite leper but Naaman "
                        "the Syrian (4:25-27). The implication: God's grace is not confined to Israel; "
                        "the kingdom extends to the nations. 'When they heard these things, all in the "
                        "synagogue were filled with wrath (thymou)' (4:28). They try to throw Jesus "
                        "off a cliff, but 'passing through their midst, he went away' (4:30) -- the "
                        "Messiah cannot be killed before his appointed time."
            }
        ]
    },

    {
        "id": "luke-5-6",
        "ref": "Luke 5-6",
        "chapter_num": 3,
        "title": "Calling Disciples, Healing, and the Sermon on the Plain",
        "era": "luke_galilee",
        "type": "study",
        "themes": ["HOLY", "TYPE", "KING", "LOVE", "COV"],

        "synopsis": "Jesus calls his first disciples with a miraculous catch of fish (5:1-11), heals "
                    "a leper and a paralytic (forgiving sins, 5:17-26), calls Levi the tax collector "
                    "(5:27-32), and teaches about fasting, new wine, and new wineskins (5:33-39). He "
                    "appoints the Twelve after a night of prayer (6:12-16) and delivers the Sermon on "
                    "the Plain (6:17-49) -- Luke's parallel to Matthew's Sermon on the Mount. Luke's "
                    "version is shorter, more direct, and includes both blessings and woes: 'Blessed "
                    "are you who are poor, for yours is the kingdom of God' (6:20) paired with 'Woe to "
                    "you who are rich, for you have received your consolation' (6:24). The ethic of "
                    "enemy-love reaches its peak: 'Love your enemies, do good to those who hate you, "
                    "bless those who curse you, pray for those who abuse you' (6:27-28). The sermon "
                    "concludes with the parable of the two foundations (6:46-49).",

        "key_verse": {
            "ref": "Luke 6:20-21",
            "text": "And he lifted up his eyes on his disciples, and said: 'Blessed are you who are poor, for yours is the kingdom of God. Blessed are you who are hungry now, for you shall be satisfied.'",
            "translation": "ESV"
        },

        "original_terms": [
            "ptochoi (poor -- Luke's Beatitudes address the literally poor, not just the 'poor in spirit' (Matt 5:3); Luke emphasizes material reversal)",
            "ouai (woe -- Luke's unique woes (6:24-26) pronounce judgment on the rich, the full, the laughing, and the popular; the covenant curses inverted)",
            "agapate tous echthrous (love your enemies -- the radical ethic of the kingdom; extending love beyond natural boundaries into enemy territory)",
            "aphiemi (forgive / release -- 'forgive, and you will be forgiven' (6:37); the jubilee ethic applied to human relationships)",
            "didaskale (teacher -- the crowds and disciples address Jesus as 'Teacher'; in Luke, Jesus is the authoritative interpreter of Torah)"
        ],

        "ane_backdrop": "The miraculous catch of fish (5:1-11) has parallels in ancient literature "
                        "where a deity or holy man demonstrates power over nature to call followers. "
                        "The Sermon on the Plain's blessings and woes follow the covenant pattern of "
                        "Deuteronomy 27-28: blessings for obedience, curses for disobedience. Luke's "
                        "version sharpens the social dimension: the poor are blessed, the rich are "
                        "cursed -- a reversal of the assumed social order that echoes the Magnificat "
                        "(1:52-53). The command to love enemies was radical in the ancient world, where "
                        "the duty of revenge was a fundamental social obligation. Neither Greek nor "
                        "Roman ethics demanded love of enemies; the Qumran community explicitly required "
                        "hatred of outsiders (1QS 1:9-10).",

        "second_temple": [
            {
                "source": "1QS 1:9-10 (Community Rule)",
                "summary": "Members are instructed 'to love all that He has chosen and to hate all "
                           "that He has rejected... to love all the sons of light... and to hate all "
                           "the sons of darkness.'",
                "relevance": "Provides a direct contrast to Jesus' command to 'love your enemies' -- "
                             "even the most devout Jewish community at Qumran did not extend love "
                             "beyond its boundaries."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 5-7", "note": "The Sermon on the Mount -- Matthew's longer parallel; 'poor in spirit' vs. Luke's 'poor'; no woes in Matthew", "type": "nt"},
            {"ref": "Deuteronomy 27-28", "note": "Covenant blessings and curses -- the literary form behind Luke's blessings and woes", "type": "ot"},
            {"ref": "Isaiah 61:1-2", "note": "'Good news to the poor' -- the Nazareth manifesto now realized: the poor receive the kingdom", "type": "ot"},
            {"ref": "Leviticus 19:18", "note": "'Love your neighbor as yourself' -- Jesus extends this beyond 'neighbor' to 'enemy'", "type": "ot"},
            {"ref": "James 2:5", "note": "'Has not God chosen those who are poor in the world to be rich in faith and heirs of the kingdom?' -- echoing Luke's Beatitude", "type": "nt"}
        ],

        "divine_council_note": "The Sermon on the Plain describes kingdom life as the reversal of the "
                               "present world order -- an order maintained by the hostile powers. The "
                               "poor are blessed because the kingdom belongs to them; the rich are warned "
                               "because their wealth is tied to the systems of the present age. The "
                               "command to love enemies (6:27-36) is not mere ethics but cosmic strategy: "
                               "the kingdom advances not through the power dynamics of the present age "
                               "(retaliation, domination, self-preservation) but through the radical "
                               "self-giving love that characterizes the Father himself ('he is kind to "
                               "the ungrateful and the evil,' 6:35). This ethic mirrors the divine "
                               "council's character: YHWH extends grace even to the nations under "
                               "rebellious rulers. The promise 'your reward will be great, and you will "
                               "be sons of the Most High (huioi hypsistou)' (6:35) uses the divine "
                               "council title: those who love their enemies are identified as children "
                               "of the Most High God -- participants in the divine family, sharing the "
                               "character of the God who rules the council.",

        "sections": [
            {
                "heading": "Miraculous Catch, Healings, and Calling Levi (5:1-39)",
                "body": "Jesus teaches from Simon's boat, then commands him to cast nets into the deep. "
                        "The catch is so great the nets begin to break (5:6). Peter falls at Jesus' "
                        "knees: 'Depart from me, for I am a sinful man, O Lord' (5:8) -- a response "
                        "to the numinous, the experience of divine holiness. Jesus: 'Do not be afraid; "
                        "from now on you will be catching men' (5:10). They leave everything and follow. "
                        "A leper is healed: 'I will; be clean' (5:13). A paralytic is lowered through "
                        "the roof; Jesus says 'Man, your sins are forgiven you' (5:20), then heals the "
                        "paralysis to prove his authority to forgive. Levi the tax collector is called "
                        "from his booth (5:27-28). At Levi's banquet with 'a great company of tax "
                        "collectors and others,' Jesus declares: 'I have not come to call the righteous "
                        "but sinners to repentance' (5:32)."
            },
            {
                "heading": "The Twelve Appointed and the Sermon on the Plain (6:1-49)",
                "body": "After Sabbath controversies (6:1-11), Jesus spends the night in prayer on a "
                        "mountain (6:12) and appoints the Twelve (6:13-16). Coming down to 'a level "
                        "place' (6:17), he delivers the Sermon on the Plain. Four blessings: blessed "
                        "are the poor, the hungry, the weeping, and the hated (6:20-23). Four woes: "
                        "woe to the rich, the full, the laughing, and the popular (6:24-26). The "
                        "central teaching: 'Love your enemies, do good to those who hate you' (6:27). "
                        "'If someone strikes you on one cheek, offer the other also' (6:29). 'Be "
                        "merciful, even as your Father is merciful' (6:36). 'Judge not, and you will "
                        "not be judged' (6:37). The log and speck (6:41-42). 'A good tree does not "
                        "bear bad fruit' (6:43). The two builders: 'Everyone who comes to me and hears "
                        "my words and does them... is like a man building a house, who dug deep and "
                        "laid the foundation on the rock' (6:47-48). The one who does not is a house "
                        "without a foundation that collapses when the flood strikes (6:49)."
            }
        ]
    },

    {
        "id": "luke-7-8",
        "ref": "Luke 7-8",
        "chapter_num": 4,
        "title": "Faith of Gentiles, Raising the Dead, and Parables of the Kingdom",
        "era": "luke_galilee",
        "type": "study",
        "themes": ["KING", "TYPE", "WOMEN", "LOVE", "DC"],

        "synopsis": "Chapters 7-8 demonstrate the kingdom's power reaching beyond expected boundaries. "
                    "A Roman centurion's faith astounds Jesus: 'I tell you, not even in Israel have I "
                    "found such faith' (7:9). Jesus raises the widow of Nain's son (7:11-17) -- a "
                    "miracle unique to Luke that echoes Elijah's raising of the widow's son in "
                    "Zarephath (1 Kings 17:17-24). John the Baptist sends his question, and Jesus "
                    "responds with the Isaiah 35/61 evidence (7:18-23). A sinful woman anoints "
                    "Jesus' feet (7:36-50) -- forgiven because she loved much. Jesus teaches in "
                    "parables (8:4-18): the Sower, with its emphasis on hearing and doing. Women "
                    "support the ministry financially: Mary Magdalene, Joanna, Susanna, and 'many "
                    "others' (8:1-3) -- a detail unique to Luke, reflecting his concern for women's "
                    "roles. The storm is stilled, the Gerasene demoniac is liberated, Jairus' "
                    "daughter is raised, and the hemorrhaging woman is healed (8:22-56).",

        "key_verse": {
            "ref": "Luke 7:9",
            "text": "When Jesus heard these things, he marveled at him, and turning to the crowd that followed him, said, 'I tell you, not even in Israel have I found such faith.'",
            "translation": "ESV"
        },

        "original_terms": [
            "pistis (faith -- the centurion's faith surpasses Israel's; faith is the operative response to the kingdom's arrival)",
            "prophetes megas (a great prophet -- the crowd's response to the raising of the widow's son: 'A great prophet has arisen among us!' (7:16); echoing Elijah)",
            "epeskepsato (has visited -- 'God has visited his people!' (7:16); the same verb used in 1:68 (Benedictus); YHWH's personal intervention in history)",
            "aphientai (are forgiven -- 'Her sins, which are many, are forgiven (aphientai) -- for she loved much' (7:47); the perfect passive indicates divine action)"
        ],

        "ane_backdrop": "The centurion's faith (7:1-10) involves the concept of delegated authority: "
                        "'I say to my servant, \"Do this,\" and he does it' (7:8). The centurion "
                        "recognizes that Jesus operates within a chain of command -- like a military "
                        "officer, Jesus has authority from above and can command spiritual forces with "
                        "a word. This is an implicit recognition of the divine council hierarchy: Jesus "
                        "exercises authority delegated by the Most High. The raising at Nain (7:11-17) "
                        "parallels Elijah's miracle in 1 Kings 17:17-24 -- both involve a widow's only "
                        "son in a town in the north. The crowd's response -- 'A great prophet has "
                        "arisen!' -- echoes the Deuteronomy 18:15 expectation of a prophet like Moses.",

        "second_temple": [
            {
                "source": "4Q521 (Messianic Apocalypse)",
                "summary": "When God's Messiah comes, 'the heavens and the earth will listen to his "
                           "Messiah... He will heal the wounded, revive the dead, and proclaim good "
                           "news to the poor.'",
                "relevance": "The catalog of messianic signs matches Jesus' answer to John: the blind "
                             "see, the lame walk, lepers are cleansed, the deaf hear, the dead are "
                             "raised, the poor have good news preached (7:22)."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 17:17-24", "note": "Elijah raises the widow of Zarephath's son -- the parallel to Jesus raising the widow of Nain's son (7:11-17)", "type": "ot"},
            {"ref": "Isaiah 35:5-6; 61:1", "note": "The messianic signs catalog -- the blind see, the deaf hear, the poor hear good news -- cited in Jesus' answer to John (7:22)", "type": "ot"},
            {"ref": "Matthew 8:5-13", "note": "Matthew's parallel centurion story -- similar dialogue but different framing; Matthew adds the 'many from east and west' saying", "type": "nt"},
            {"ref": "Mark 4-5", "note": "Mark's parallel parables, storm stilling, Gerasene demoniac, and Jairus' daughter -- Luke follows Mark's order closely", "type": "nt"}
        ],

        "divine_council_note": "The centurion's faith (7:1-10) has profound divine council implications. "
                               "The centurion -- a Gentile military officer serving the occupying power -- "
                               "recognizes Jesus' authority as operating within a hierarchical chain of "
                               "command. Just as the centurion commands soldiers and servants by virtue of "
                               "the authority above him, Jesus commands disease and demons by virtue of "
                               "the authority of the Most High. The centurion's insight into Jesus' "
                               "authority surpasses all of Israel's understanding -- a Gentile, from the "
                               "territory of the nations, recognizes the divine council's authority in "
                               "Jesus. This foreshadows the Gentile mission: the nations will receive the "
                               "kingdom's good news and respond with faith. The raising at Nain (7:11-17) "
                               "demonstrates authority over death itself -- the ultimate enemy, the domain "
                               "that Sheol and Hades claim as their own. Jesus invades death's territory "
                               "and brings back a captive.",

        "sections": [
            {
                "heading": "The Centurion, the Widow, and John's Question (7:1-35)",
                "body": "A centurion in Capernaum sends Jewish elders to Jesus, asking him to heal his "
                        "servant. The elders commend the centurion: 'He is worthy... he loves our "
                        "nation, and he is the one who built us our synagogue' (7:4-5). As Jesus "
                        "approaches, the centurion sends friends: 'Lord, do not trouble yourself, for "
                        "I am not worthy to have you come under my roof... say the word, and let my "
                        "servant be healed. For I too am a man set under authority' (7:6-8). Jesus "
                        "marvels: 'Not even in Israel have I found such faith' (7:9). At Nain, Jesus "
                        "encounters a funeral procession for the only son of a widow (7:11-12). 'He "
                        "had compassion (esplanchnisthe) on her' (7:13) and says 'Young man, I say to "
                        "you, arise' (7:14). The dead man sits up and begins to speak (7:15). The crowd: "
                        "'A great prophet has arisen among us!' and 'God has visited (epeskepsato) his "
                        "people!' (7:16). John sends his question: 'Are you the one who is to come?' "
                        "(7:19). Jesus responds with evidence: the blind see, the lame walk, lepers are "
                        "cleansed, the deaf hear, the dead are raised, the poor hear good news (7:22)."
            },
            {
                "heading": "The Sinful Woman, the Women Disciples, and Miracles (7:36 - 8:56)",
                "body": "At a Pharisee's house, a 'woman of the city, who was a sinner' (7:37) wets "
                        "Jesus' feet with tears, wipes them with her hair, and anoints them with "
                        "ointment. The Pharisee thinks: 'If this man were a prophet, he would know "
                        "who and what sort of woman this is' (7:39). Jesus tells the parable of the "
                        "two debtors (7:41-43) and declares: 'Her sins, which are many, are forgiven -- "
                        "for she loved much' (7:47). Chapter 8 notes the women who support Jesus' "
                        "ministry: Mary Magdalene ('from whom seven demons had gone out'), Joanna (wife "
                        "of Chuza, Herod's household manager), Susanna, and 'many others' (8:1-3). "
                        "Jesus teaches the parable of the Sower (8:4-15), then demonstrates authority "
                        "over nature (the storm stilled, 8:22-25), over a legion of demons (the "
                        "Gerasene demoniac, 8:26-39), over disease (the hemorrhaging woman, 8:43-48), "
                        "and over death (Jairus' daughter, 8:49-56). The authority proclaimed in the "
                        "parables is confirmed in the miracles."
            }
        ]
    },

    {
        "id": "luke-9",
        "ref": "Luke 9",
        "chapter_num": 5,
        "title": "The Twelve Sent, Peter's Confession, Transfiguration, and the Turn to Jerusalem",
        "era": "luke_galilee",
        "type": "study",
        "themes": ["KING", "BLOOD", "SEED", "DC", "TYPE"],

        "synopsis": "Chapter 9 is the hinge of Luke's Gospel. Jesus sends the Twelve with 'power and "
                    "authority over all demons and to cure diseases' (9:1). He feeds the 5,000 (9:10-17). "
                    "Peter confesses: 'The Christ of God' (9:20). Jesus predicts his death (9:22), "
                    "teaches the cost of discipleship (9:23-27), and is transfigured on the mountain "
                    "(9:28-36). Luke uniquely records that Moses and Elijah 'spoke of his departure "
                    "(exodon), which he was about to accomplish at Jerusalem' (9:31) -- the word "
                    "exodos ('exodus/departure') links Jesus' death to Israel's liberation from Egypt. "
                    "After healing a demon-possessed boy (9:37-43), Jesus predicts his death again "
                    "(9:44-45), teaches about true greatness (9:46-48), and then the critical turning "
                    "point: 'When the days drew near for him to be taken up, he set his face to go to "
                    "Jerusalem' (9:51). The Galilean ministry is over. The journey to the cross begins.",

        "key_verse": {
            "ref": "Luke 9:31",
            "text": "[They] appeared in glory and spoke of his departure (exodon), which he was about to accomplish at Jerusalem.",
            "translation": "ESV"
        },

        "original_terms": [
            "exodos (departure / exodus -- Moses and Elijah discuss Jesus' 'exodus' at Jerusalem; linking the crucifixion to Israel's liberation from bondage; Jesus' death is the new exodus)",
            "Christos tou theou (the Christ of God -- Peter's confession; the anointed one who belongs to God; the long-awaited Messiah)",
            "to prosopon esterisen (he set his face -- 'he set his face to go to Jerusalem' (9:51); echoing Isaiah 50:7, the Servant's resolve: 'I have set my face like a flint')",
            "analempsis (taking up -- 'the days drew near for him to be taken up' (9:51); referring to the ascension; the entire journey is oriented toward his 'taking up' into heaven)",
            "doxa (glory -- Moses and Elijah 'appeared in glory' (9:31); Jesus' face 'altered' and his clothing 'dazzling white' (9:29); the divine glory unveiled)"
        ],

        "ane_backdrop": "The Transfiguration's connection to the exodus motif is profound. Moses and "
                        "Elijah -- the two figures most associated with Sinai/Horeb -- appear to discuss "
                        "Jesus' 'exodus' (exodon, 9:31). The first exodus liberated Israel from Egypt "
                        "through blood (Passover lamb) and water (Red Sea). Jesus' exodus will liberate "
                        "humanity from the bondage of sin and the hostile powers through his death (the "
                        "blood of the new covenant) and resurrection (the passage through death to new "
                        "life). Luke's use of the word exodos is deliberate: the entire Lukan passion "
                        "narrative is a new exodus, with Jesus as both the new Moses (leading the people "
                        "to freedom) and the Passover lamb (whose blood effects liberation).",

        "second_temple": [
            {
                "source": "2 Peter 1:15",
                "summary": "Peter uses the same word exodos for his own impending death: 'I will make "
                           "every effort so that after my exodus (exodon) you may be able at any time "
                           "to recall these things.'",
                "relevance": "Confirms that the Transfiguration's exodus language shaped early Christian "
                             "understanding of death as a 'departure' that leads to glory."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 50:7", "note": "'I have set my face like a flint' -- the Servant's resolve echoed in Jesus setting his face toward Jerusalem (9:51)", "type": "ot"},
            {"ref": "Exodus 12-14", "note": "The original exodus: liberation through blood and water -- the background to Jesus' 'exodus' discussed at the Transfiguration", "type": "ot"},
            {"ref": "Deuteronomy 18:15", "note": "'Listen to him' -- the command at the Transfiguration (9:35) echoes Moses' prophecy of the prophet like him", "type": "ot"},
            {"ref": "Mark 8:27 - 9:13", "note": "Mark's parallel: Peter's confession, passion prediction, and Transfiguration -- Mark does not mention the 'exodus' discussion", "type": "nt"},
            {"ref": "Matthew 16:13 - 17:13", "note": "Matthew's parallel: adds the rock/keys saying, 'gates of Hades' declaration, and 'flesh and blood' revelation", "type": "nt"}
        ],

        "divine_council_note": "Luke's Transfiguration account adds the crucial detail that Moses and "
                               "Elijah 'appeared in glory (doxa)' (9:31) and discussed Jesus' 'exodus "
                               "(exodon), which he was about to accomplish at Jerusalem.' This is a "
                               "divine council deliberation: the representatives of the Law and the "
                               "Prophets, appearing in divine glory, discuss the plan of salvation with "
                               "the Son of God on the mountain. The word exodon is Luke's theological "
                               "key: just as the first exodus was YHWH's definitive act of liberation "
                               "from the powers that held Israel in bondage (Egypt, Pharaoh, the gods of "
                               "Egypt), Jesus' death-resurrection-ascension will be YHWH's definitive act "
                               "of liberation from the powers that hold all humanity in bondage (sin, "
                               "death, Satan, and the rebellious elohim). The voice from the cloud -- "
                               "'This is my Son, my Chosen One (ho eklelegmenos mou); listen to him' "
                               "(9:35) -- uses the language of Isaiah 42:1 (the Chosen Servant) and "
                               "Deuteronomy 18:15 (the prophet like Moses). The turning point at 9:51 -- "
                               "'he set his face to go to Jerusalem' -- is the Son's resolve to accomplish "
                               "the exodus that the council has decreed. The journey that follows "
                               "(9:51-19:44) is the march toward the cross, the exodus event that will "
                               "liberate the nations.",

        "sections": [
            {
                "heading": "The Twelve Sent, Feeding, and Peter's Confession (9:1-27)",
                "body": "Jesus gives the Twelve 'power and authority (dynamin kai exousian) over all "
                        "demons and to cure diseases' (9:1). They go out preaching and healing (9:6). "
                        "Herod is perplexed, hearing reports that John has been raised or that Elijah "
                        "or a prophet has appeared (9:7-9). Jesus feeds 5,000 with five loaves and "
                        "two fish (9:10-17). While praying alone (a Lukan detail), Jesus asks: 'Who "
                        "do the crowds say that I am?' (9:18). Peter answers: 'The Christ of God "
                        "(ton Christon tou theou)' (9:20). Jesus commands secrecy and predicts: 'The "
                        "Son of Man must (dei) suffer many things and be rejected... and be killed, "
                        "and on the third day be raised' (9:22). 'If anyone would come after me, let "
                        "him deny himself and take up his cross daily (kath hemeran -- a Lukan addition: "
                        "daily cross-bearing) and follow me' (9:23)."
            },
            {
                "heading": "The Transfiguration and the Turn to Jerusalem (9:28-62)",
                "body": "About eight days later (Luke's timing differs from Mark's 'six days'), Jesus "
                        "takes Peter, John, and James up the mountain 'to pray' (9:28 -- another Lukan "
                        "detail). While praying, 'the appearance of his face was altered, and his "
                        "clothing became dazzling white' (9:29). Moses and Elijah appear 'in glory' "
                        "and discuss his 'exodus' (exodon) to be accomplished at Jerusalem (9:31). "
                        "Peter, James, and John are 'heavy with sleep' but awaken to see the glory "
                        "(9:32). Peter offers to build three tabernacles (9:33). A cloud overshadows "
                        "them, and the voice says: 'This is my Son, my Chosen One; listen to him' "
                        "(9:35). The next day, Jesus heals a demon-possessed boy the disciples could "
                        "not heal (9:37-43). He predicts his death a second time (9:44). The disciples "
                        "argue about greatness; Jesus places a child beside him (9:46-48). Then the "
                        "decisive verse: 'When the days drew near for him to be taken up (analempsis), "
                        "he set his face (to prosopon esterisen) to go to Jerusalem' (9:51). The "
                        "journey begins. He encounters would-be followers: 'Foxes have holes, and "
                        "birds of the air have nests, but the Son of Man has nowhere to lay his "
                        "head' (9:58). 'No one who puts his hand to the plow and looks back is fit "
                        "for the kingdom of God' (9:62)."
            }
        ]
    }
]
