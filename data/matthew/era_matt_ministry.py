"""
era_matt_ministry.py -- Matthew 1-13: Birth, Kingdom Proclamation, and Parables

The first half of Matthew establishes Jesus' identity and mission. The genealogy
roots him in Abraham and David. The birth narrative reveals him as Immanuel --
"God with us." The temptation narrative shows him defeating Satan where Israel
failed. The Sermon on the Mount presents his authoritative Torah of the Kingdom.
The miracles demonstrate the kingdom's power over disease, demons, nature, and
death. The parables reveal the kingdom's hidden, surprising, and all-encompassing
nature. Through it all, Matthew builds his case: Jesus is the promised Messiah,
the Son of David, the Son of God, and the one through whom YHWH is reclaiming
his creation from the powers of darkness.
"""

CHAPTERS = [
    {
        "id": "matt-1-2",
        "ref": "Matthew 1-2",
        "chapter_num": 1,
        "title": "The Genealogy, the Virgin Birth, and the Flight to Egypt",
        "era": "matt_ministry",
        "type": "study",

        "synopsis": "Matthew opens with a genealogy that is a theological argument in compressed "
                    "form: 'The book of the genealogy (biblos geneseos) of Jesus Christ, the son "
                    "of David, the son of Abraham' (1:1). The phrase biblos geneseos echoes Genesis "
                    "2:4 and 5:1 in the LXX -- Matthew is announcing a new genesis, a new beginning "
                    "of creation. The genealogy is structured in three sets of fourteen generations: "
                    "Abraham to David (the promise), David to the exile (the failure), exile to "
                    "Christ (the fulfillment). The number 14 is the gematria (numerical value) of "
                    "David's name in Hebrew (dalet-vav-dalet = 4+6+4 = 14). Four women are included "
                    "in the genealogy -- Tamar, Rahab, Ruth, and Bathsheba ('the wife of Uriah') -- "
                    "all of whom are Gentiles or connected to Gentile backgrounds, foreshadowing "
                    "the Gospel's climactic commission to 'all nations.' The birth narrative introduces "
                    "Jesus as 'Immanuel' (Hebrew: immanu-el, 'God with us'), fulfilling Isaiah 7:14. "
                    "The Magi from the East follow a star -- cosmic signs heralding the birth of the "
                    "king. Herod's massacre of the innocents echoes Pharaoh's murder of Hebrew infants, "
                    "establishing Jesus as a new Moses. The flight to Egypt and return fulfills "
                    "Hosea 11:1: 'Out of Egypt I called my son' -- Jesus recapitulates Israel's story.",

        "key_verse": {
            "ref": "Matthew 1:23",
            "text": "'Behold, the virgin shall conceive and bear a son, and they shall call his name Immanuel' (which means, God with us).",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Christos / Meshiach (Christ / Anointed One -- the Greek and Hebrew terms for the promised king anointed by YHWH)",
            "biblos geneseos (book of genesis/genealogy -- echoing Gen 2:4 LXX, signaling a new creation narrative)",
            "Immanuel / immanu-el (God with us -- from Isaiah 7:14; the claim that God's presence is embodied in Jesus)",
            "parthenos (virgin -- the LXX translation of Hebrew almah in Isaiah 7:14; Matthew follows the LXX reading)",
            "magoi (Magi/wise men -- Persian or Babylonian astrologer-priests; Gentiles who recognize the Jewish king)",
            "aster (star -- the star of Bethlehem; in ANE thought, celestial signs announced the births of kings and gods)"
        ],

        "ane_backdrop": "The birth narrative draws on multiple ANE motifs. The threatened infant king who "
                        "survives a massacre is a widespread pattern: Moses survives Pharaoh's edict "
                        "(Exod 1-2), Sargon of Akkad is placed in a basket on the river, and the "
                        "Mesopotamian flood hero's line survives destruction. The star followed by the "
                        "Magi reflects Babylonian astral divination -- the belief that celestial events "
                        "signal terrestrial changes, especially the births of great kings. Balaam's "
                        "oracle in Numbers 24:17 ('A star shall come out of Jacob, and a scepter shall "
                        "rise out of Israel') was widely read as a messianic prophecy in Second Temple "
                        "Judaism, including at Qumran (4QTestimonia). The gifts of gold, frankincense, "
                        "and myrrh echo Isaiah 60:6 ('They shall bring gold and frankincense') and the "
                        "tribute brought to Solomon by the Queen of Sheba (1 Kings 10:2). Herod's "
                        "slaughter of the innocents mirrors the ANE pattern of the paranoid tyrant who "
                        "tries to eliminate the divinely chosen rival -- a cosmic conflict between the "
                        "powers of the old order and the divinely appointed king.",

        "second_temple": [
            {
                "source": "4QTestimonia (4Q175)",
                "summary": "This Qumran text collects messianic proof-texts including Numbers 24:17 "
                           "(the star prophecy), Deuteronomy 18:18-19 (the prophet like Moses), and "
                           "Deuteronomy 33:8-11 (the priestly blessing). The star of Bethlehem "
                           "narrative resonates with the Qumran community's expectation of a royal "
                           "messiah heralded by a star.",
                "relevance": "Shows that the star-messiah connection was already established in "
                             "Jewish thought before Matthew wrote -- Matthew did not invent it."
            },
            {
                "source": "Protevangelium of James (~150 AD)",
                "summary": "This apocryphal infancy gospel expands Matthew's birth narrative with "
                           "legendary details about Mary's childhood, the star's extraordinary "
                           "brightness, and the midwife who verified the virgin birth.",
                "relevance": "Demonstrates how Matthew's sparse birth narrative generated enormous "
                             "popular interest and theological reflection in the early church."
            },
            {
                "source": "Targum Pseudo-Jonathan on Numbers 24:17",
                "summary": "The Aramaic Targum interprets Balaam's star oracle as: 'A king shall "
                           "arise from Jacob, and the Messiah shall be anointed from Israel.'",
                "relevance": "Confirms that the star-messiah connection was standard Jewish "
                             "interpretation, not a Christian innovation."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 2:4; 5:1", "note": "'These are the generations (toledot)...' -- Matthew's biblos geneseos deliberately echoes Genesis, presenting Jesus as a new beginning", "type": "ot"},
            {"ref": "Isaiah 7:14", "note": "'The virgin shall conceive and bear a son, and shall call his name Immanuel' -- the foundational fulfillment quotation of the birth narrative", "type": "ot"},
            {"ref": "Hosea 11:1", "note": "'Out of Egypt I called my son' -- originally about Israel's exodus; Matthew reads Jesus as recapitulating Israel's story", "type": "ot"},
            {"ref": "Numbers 24:17", "note": "'A star shall come out of Jacob' -- Balaam's prophecy, the OT background to the star of Bethlehem", "type": "ot"},
            {"ref": "Jeremiah 31:15", "note": "'Rachel weeping for her children' -- fulfilled in Herod's massacre of the innocents (Matt 2:17-18)", "type": "ot"},
            {"ref": "Luke 1-2", "note": "Luke's parallel birth narrative -- different details (shepherds not Magi, Nazareth origin, census) but the same theological claim: the Messiah has been born", "type": "nt"}
        ],

        "divine_council_note": "The birth narrative establishes Jesus' identity in divine council terms. "
                               "The name 'Immanuel' (God with us) is not merely honorific -- it is an "
                               "ontological claim that YHWH's presence is embodied in this child. The "
                               "angel's announcement to Joseph (1:20-21) is a divine council message "
                               "delivered by a member of the heavenly assembly. The star that guides the "
                               "Magi reflects the ancient belief that celestial bodies are connected to "
                               "spiritual powers (Deut 4:19; Dan 8:10 -- stars as angelic beings). A new "
                               "star signals a new authority in the heavenly realm. Herod's frantic response "
                               "mirrors the reaction of earthly rulers in Psalm 2:1-3 when YHWH installs "
                               "his king on Zion: 'The kings of the earth set themselves... against YHWH and "
                               "his Anointed.' Herod is the Psalm 2 king who rages against YHWH's Messiah. "
                               "The Magi -- Gentile priests from the East -- represent the firstfruits of "
                               "the nations recognizing the true king, anticipating the Great Commission's "
                               "reclamation of the ethne.",

        "sections": [
            {
                "heading": "The Genealogy: A Theological Argument in Three Acts (1:1-17)",
                "body": "Matthew's genealogy is not a dry list but a compressed narrative of salvation "
                        "history. The three sections tell a story: (1) Abraham to David (1:2-6a) -- the "
                        "era of promise, from God's call of Abraham to the establishment of the Davidic "
                        "kingdom. (2) David to the exile (1:6b-11) -- the era of failure, tracing the "
                        "decline from Solomon through the divided monarchy to the catastrophe of Babylon. "
                        "(3) Exile to Christ (1:12-16) -- the era of hope, the obscure generations of "
                        "waiting that culminate in 'Jesus who is called Christ' (1:16). The inclusion "
                        "of four women -- Tamar (a Canaanite who seduced her father-in-law), Rahab (a "
                        "Canaanite prostitute who hid the spies), Ruth (a Moabite who married into "
                        "Israel), and Bathsheba ('the wife of Uriah' -- a Hittite connection) -- is "
                        "striking. All four have irregular or scandalous sexual histories, and all four "
                        "have Gentile connections. They prepare the reader for two Matthean themes: God "
                        "works through the unexpected and marginalized, and the Messiah's lineage already "
                        "encompasses the nations."
            },
            {
                "heading": "The Virgin Birth and Immanuel (1:18-25)",
                "body": "Joseph discovers Mary is pregnant and plans to divorce her quietly. An angel "
                        "(angelos kyriou, 'angel of the Lord' -- a divine council messenger) appears in "
                        "a dream with the explanation: 'that which is conceived in her is from the Holy "
                        "Spirit (ek pneumatos hagiou)' (1:20). The child is to be named Jesus (Iesous, "
                        "from Hebrew Yehoshua/Yeshua, meaning 'YHWH saves'), 'for he will save his "
                        "people from their sins' (1:21). Matthew then provides his first fulfillment "
                        "quotation: this fulfills Isaiah 7:14, 'the virgin (parthenos) shall conceive "
                        "and bear a son, and they shall call his name Immanuel, which means God with "
                        "us' (1:22-23). The name Immanuel frames the entire Gospel: it opens with 'God "
                        "with us' and closes with Jesus' promise 'I am with you always, to the end of "
                        "the age' (28:20). The incarnation is the ultimate divine council act: YHWH "
                        "himself enters the human realm as a human being, the visible image of the "
                        "invisible God, the second YHWH figure who shares the identity of the Father "
                        "while being distinct from him."
            },
            {
                "heading": "The Magi, Herod, and the Flight to Egypt (2:1-23)",
                "body": "Magi (magoi -- likely Zoroastrian priestly astrologers from Persia or Babylon) "
                        "arrive in Jerusalem asking 'Where is he who has been born king of the Jews? "
                        "For we saw his star when it rose and have come to worship him' (2:2). Herod "
                        "is 'troubled, and all Jerusalem with him' (2:3) -- the city's response mirrors "
                        "Psalm 2:1-2, where the earthly rulers conspire against YHWH's anointed. Herod "
                        "consults the chief priests and scribes, who identify Bethlehem from Micah 5:2 "
                        "as the Messiah's birthplace (2:5-6). The Magi find the child, worship him, and "
                        "offer gifts: gold (kingship), frankincense (deity/priesthood), and myrrh "
                        "(suffering/death -- used in embalming). Warned in a dream (another divine "
                        "council communication), they return home by a different route. Herod, enraged, "
                        "orders the massacre of all male children in Bethlehem under two years old -- "
                        "fulfilling Jeremiah 31:15, 'Rachel weeping for her children.' Joseph flees "
                        "to Egypt with Mary and Jesus (fulfilling Hosea 11:1, 'Out of Egypt I called "
                        "my son'), returns after Herod's death, and settles in Nazareth (fulfilling "
                        "an unspecified prophetic word, 2:23). Jesus recapitulates Israel's journey: "
                        "born in the land, exiled to Egypt, called out to begin his mission."
            },
            {
                "heading": "Name Theology: Five Names That Tell the Gospel Story",
                "body": "Matthew 1-2 is saturated with name theology. Five names carry the weight of "
                        "Matthew's Christology: (1) Jesus (Yeshua, יֵשׁוּעַ) = 'YHWH saves.' The angel "
                        "explains: 'You shall call his name Jesus, for he will save his people from "
                        "their sins' (1:21). This is the same name as Joshua (Yehoshua), who led Israel "
                        "into the Promised Land — Jesus leads humanity into the Kingdom. (2) Immanuel "
                        "(עִמָּנוּ אֵל) = 'God with us' (Isaiah 7:14). Matthew brackets his entire "
                        "Gospel with this concept: 'God with us' at birth (1:23), 'I am with you always' "
                        "at the end (28:20). (3) Christ (Christos/Meshiach) = 'Anointed One.' The "
                        "genealogy's title: 'Jesus Christ, the son of David, the son of Abraham' — three "
                        "names, three identities: anointed king, Davidic heir, Abrahamic promise-bearer. "
                        "(4) Bethlehem (Bêt Leḥem) = 'House of Bread.' The one who calls himself 'the "
                        "Bread of Life' (John 6:35) is born in the House of Bread. (5) Nazareth "
                        "(Nāṣěreṯ) — possibly connected to netzer (נֵצֶר, 'branch'), the messianic "
                        "title from Isaiah 11:1: 'A shoot from the stump of Jesse, a branch (netzer) "
                        "from his roots.' Matthew 2:23 says Jesus fulfilled 'He shall be called a "
                        "Nazarene' — likely a wordplay on this prophetic branch. The four women in the "
                        "genealogy also carry name significance: Tamar ('palm tree' — she bore fruit "
                        "from seeming barrenness), Ruth ('friend/companion' — the Gentile who clung to "
                        "Israel's God), and Rahab ('broad/wide' — she who sheltered the spies)."
            }
        ]
    },

    {
        "id": "matt-3-4",
        "ref": "Matthew 3-4",
        "chapter_num": 2,
        "title": "Baptism, Temptation, and the Kingdom Announced",
        "era": "matt_ministry",
        "type": "study",

        "synopsis": "John the Baptist appears in the wilderness proclaiming 'Repent, for the kingdom "
                    "of heaven is at hand' (3:2) -- the same message Jesus will preach (4:17). John "
                    "identifies himself as the Isaianic voice 'crying in the wilderness' (3:3; Isa "
                    "40:3) and announces one coming after him who will baptize 'with the Holy Spirit "
                    "and fire' (3:11). At Jesus' baptism, the heavens are 'opened' (3:16) -- a "
                    "visionary rupture between the earthly and heavenly realms -- and the Spirit "
                    "descends like a dove while a voice from heaven declares: 'This is my beloved "
                    "Son, with whom I am well pleased' (3:17), combining Psalm 2:7 (the royal "
                    "enthronement decree) with Isaiah 42:1 (the Servant of YHWH). Immediately the "
                    "Spirit drives Jesus into the wilderness to be tempted by the devil -- a 40-day "
                    "ordeal recapitulating Israel's 40-year wilderness testing. Satan's three "
                    "temptations target Jesus' identity as Son and his mission: turn stones to bread "
                    "(test of provision), throw yourself from the Temple (test of protection), worship "
                    "me and receive all kingdoms (test of allegiance). Jesus defeats each with "
                    "Deuteronomy quotations, succeeding where Israel failed. He then begins his "
                    "Galilean ministry, calling disciples and proclaiming the kingdom.",

        "key_verse": {
            "ref": "Matthew 4:8-10",
            "text": "Again, the devil took him to a very high mountain and showed him all the kingdoms of the world and their glory. And he said to him, 'All these I will give you, if you will fall down and worship me.' Then Jesus said to him, 'Be gone, Satan! For it is written, \"You shall worship the Lord your God and him only shall you serve.\"'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "basileia ton ouranon (kingdom of heaven -- Matthew's circumlocution for kingdom of God; God's sovereign rule breaking into the present age)",
            "metanoeite (repent -- Greek metanoia, a complete change of mind and direction; the proper response to the kingdom's arrival)",
            "huios agapetos (beloved Son -- the divine declaration at baptism; echoing Ps 2:7 and Isa 42:1; identity as unique divine Son)",
            "diabolos (devil / slanderer -- from diaballo, 'to throw across, to slander'; the accuser who opposes YHWH's plan)",
            "Satanas (Satan -- from Hebrew satan, 'adversary'; the prosecutor/accuser in the divine council who has become YHWH's enemy)",
            "peirazein (to test/tempt -- the wilderness testing that recapitulates Israel's testing; proving faithfulness or exposing failure)"
        ],

        "ane_backdrop": "The wilderness temptation narrative operates within the ANE motif of the "
                        "divine king tested before his enthronement. In the Mesopotamian tradition, "
                        "kings underwent ritual testing to prove their fitness for rule. The wilderness "
                        "setting evokes Israel's 40-year testing period (Deut 8:2-3), during which God "
                        "tested them to know what was in their hearts. Satan's offer of 'all the kingdoms "
                        "of the world' (4:8) reflects the Deuteronomy 32 worldview directly: the nations "
                        "were allotted to the sons of God at Babel, and Satan claims authority over these "
                        "territorial powers. In the Book of Job (1:6-12; 2:1-6), the satan figure appears "
                        "in the divine council as an accuser/prosecutor who tests the faithful. In "
                        "Matthew 4, this figure has become the adversary who offers the kingdoms to Jesus "
                        "in exchange for worship -- a cosmic power play to prevent the reclamation of "
                        "the nations. The baptism narrative's opened heavens, descending Spirit, and "
                        "divine voice parallel prophetic call narratives (Ezekiel 1:1, 'the heavens "
                        "were opened, and I saw visions of God'), commissioning Jesus as prophet, "
                        "priest, and king simultaneously.",

        "second_temple": [
            {
                "source": "Testament of Job (1st century BC - 1st century AD)",
                "summary": "The Testament of Job expands the canonical Job story with extensive "
                           "dialogue between Job and Satan, portraying Satan as a cosmic adversary "
                           "who tests the righteous to prove their unworthiness before the divine "
                           "council.",
                "relevance": "Provides context for the development of Satan from a council prosecutor "
                             "(as in Job 1-2) to a cosmic enemy who tempts the Son of God in Matthew 4."
            },
            {
                "source": "4Q521 (Messianic Apocalypse)",
                "summary": "This Qumran text describes the age when God's Messiah comes: 'the heavens "
                           "and the earth will listen to his Messiah... He will heal the wounded, "
                           "revive the dead, and proclaim good news to the poor.'",
                "relevance": "Shows that the expected Messiah was associated with the works Jesus "
                             "performs in Matthew 4-12 -- healings, exorcisms, good news to the poor."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 8:3", "note": "'Man shall not live by bread alone, but by every word that comes from the mouth of God' -- Jesus' first response to Satan, quoting from Israel's wilderness testing", "type": "ot"},
            {"ref": "Deuteronomy 6:16", "note": "'You shall not put the Lord your God to the test' -- Jesus' second response, referencing Israel's testing at Massah (Exod 17:1-7)", "type": "ot"},
            {"ref": "Deuteronomy 6:13", "note": "'You shall worship the Lord your God and him only shall you serve' -- Jesus' third response, the Shema loyalty that Satan's offer violates", "type": "ot"},
            {"ref": "Psalm 2:7", "note": "'You are my Son; today I have begotten you' -- echoed in the baptismal voice, 'This is my beloved Son'", "type": "ot"},
            {"ref": "Isaiah 42:1", "note": "'Behold my servant, whom I uphold, my chosen, in whom my soul delights' -- the Servant Song echoed in 'with whom I am well pleased'", "type": "ot"},
            {"ref": "Mark 1:9-13", "note": "Mark's compressed parallel: baptism, Spirit descent, voice, and temptation in four verses -- Matthew expands with the three specific temptations", "type": "nt"},
            {"ref": "Luke 4:1-13", "note": "Luke's parallel temptation -- same three tests but in different order (Luke places the Temple temptation last); Luke 4:6 adds Satan's explicit claim: 'all this authority has been delivered to me'", "type": "nt"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God -- the theological backdrop to Satan's claim of authority over 'all the kingdoms of the world'", "type": "ot"}
        ],

        "divine_council_note": "The baptism-temptation sequence is a divine council drama in two acts. "
                               "Act 1 -- Baptism (3:13-17): The heavens are 'opened' (eneochthesan), "
                               "creating a portal between the earthly and heavenly realms. The Spirit "
                               "descends 'like a dove' (hos peristeran) -- the visible manifestation "
                               "of YHWH's empowering presence. The Father's voice declares 'This is my "
                               "beloved Son' -- the Psalm 2:7 decree of royal installation, spoken from "
                               "the heavenly council chamber. Jesus is publicly identified as the Son "
                               "enthroned on Zion, the one to whom the nations will be given. Act 2 -- "
                               "Temptation (4:1-11): The Spirit immediately drives Jesus into the wilderness "
                               "to face the satan (the adversary). Satan's third temptation is the key: "
                               "he shows Jesus 'all the kingdoms of the world and their glory' (4:8) and "
                               "offers them in exchange for worship. This is the Deuteronomy 32 worldview "
                               "made explicit: Satan claims authority over the nations that were allotted "
                               "to the sons of God at Babel. His offer is a shortcut -- Jesus can have "
                               "the nations without the cross, if he will submit to Satan's authority. "
                               "Jesus refuses with Deuteronomy 6:13: 'You shall worship the Lord your God "
                               "and him only shall you serve.' He will reclaim the nations the Father's way "
                               "-- through suffering, death, and resurrection. The angels who 'came and "
                               "were ministering to him' (4:11) after Satan's departure are divine council "
                               "members serving the victorious Son.",

        "sections": [
            {
                "heading": "John the Baptist and the Wilderness Announcement (3:1-12)",
                "body": "John the Baptist appears 'in the wilderness of Judea' (3:1) -- the liminal "
                        "space between civilization and chaos, the place of testing and encounter with "
                        "God. His message is urgent: 'Repent (metanoeite), for the kingdom of heaven "
                        "is at hand (engiken)' (3:2). The verb engiken means 'has drawn near, is "
                        "imminent' -- the kingdom is not a distant hope but a breaking-in reality. "
                        "Matthew identifies John with Isaiah 40:3: 'The voice of one crying in the "
                        "wilderness: Prepare the way of the Lord, make his paths straight.' In Isaiah, "
                        "this is YHWH's return to Zion after exile -- the one whose way John prepares "
                        "is YHWH himself. John warns the Pharisees and Sadducees: 'Do not presume to "
                        "say to yourselves, \"We have Abraham as our father\"' (3:9). Ethnic lineage "
                        "is not enough; the axe is at the root of the trees, and the one coming after "
                        "John will baptize 'with the Holy Spirit and fire' (3:11) and sort the wheat "
                        "from the chaff on the threshing floor (3:12). This is eschatological judgment "
                        "language -- the Messiah comes not just to heal but to judge."
            },
            {
                "heading": "The Baptism: The Heavens Opened (3:13-17)",
                "body": "Jesus comes from Galilee to be baptized by John. John protests: 'I need to be "
                        "baptized by you' (3:14), recognizing Jesus' superiority. Jesus insists: 'It is "
                        "fitting for us to fulfill all righteousness (dikaiosynen)' (3:15). Jesus' "
                        "baptism is not for his own repentance but an act of identification -- he enters "
                        "the waters with sinful Israel, taking their place. At the moment he rises from "
                        "the water, three things happen simultaneously: (1) 'The heavens were opened to "
                        "him' (3:16a) -- the barrier between the earthly and heavenly realms is breached. "
                        "This is the language of prophetic vision (Ezek 1:1; Isa 64:1). (2) 'He saw the "
                        "Spirit of God descending like a dove and coming to rest on him' (3:16b) -- the "
                        "Spirit's descent anoints Jesus for his mission, echoing the anointing of kings "
                        "(1 Sam 16:13) and the promise of Isaiah 61:1 ('The Spirit of the Lord GOD is "
                        "upon me, because the LORD has anointed me'). (3) 'A voice from heaven said, "
                        "\"This is my beloved Son, with whom I am well pleased\"' (3:17). The voice "
                        "combines Psalm 2:7 ('You are my Son') -- the royal enthronement decree -- with "
                        "Isaiah 42:1 ('my chosen, in whom my soul delights') -- the Servant of YHWH. "
                        "Jesus is simultaneously king and servant, enthroned and appointed to suffer."
            },
            {
                "heading": "The Temptation: Satan's Offer of the Nations (4:1-11)",
                "body": "The Spirit leads Jesus into the wilderness 'to be tempted (peirasthenai) by "
                        "the devil' (4:1). The testing lasts 40 days and 40 nights -- recapitulating "
                        "Israel's 40 years of wilderness testing (Deut 8:2) and Moses' 40 days on Sinai "
                        "(Exod 34:28). Three temptations follow, each targeting a different dimension of "
                        "Jesus' mission. First, the bread test (4:3-4): 'If you are the Son of God, "
                        "command these stones to become loaves of bread.' This echoes Israel's complaint "
                        "about food in the wilderness (Exod 16). Jesus responds with Deuteronomy 8:3: "
                        "'Man shall not live by bread alone, but by every word that comes from the mouth "
                        "of God.' Second, the Temple test (4:5-7): Satan takes Jesus to the pinnacle of "
                        "the Temple and quotes Psalm 91:11-12 -- 'He will command his angels concerning "
                        "you.' This is scripture used against scripture, a distortion of divine council "
                        "protection promises. Jesus responds with Deuteronomy 6:16: 'You shall not put "
                        "the Lord your God to the test' -- referencing Massah (Exod 17:1-7), where Israel "
                        "tested YHWH's faithfulness. Third, the kingdoms test (4:8-10): Satan shows Jesus "
                        "'all the kingdoms of the world and their glory' and offers them for worship. "
                        "This is the decisive temptation -- the Deuteronomy 32 worldview made visible. "
                        "Satan offers what Psalm 2:8 promises: the nations as the Son's inheritance. But "
                        "the price is apostasy -- worship of the adversary instead of the Father. Jesus "
                        "responds with Deuteronomy 6:13: 'You shall worship the Lord your God and him "
                        "only shall you serve.' Angels then minister to Jesus (4:11) -- the divine council "
                        "serves the victorious Son."
            },
            {
                "heading": "The Kingdom Announced and the First Disciples (4:12-25)",
                "body": "After John's arrest, Jesus withdraws to Galilee -- specifically to Capernaum, "
                        "'by the sea, in the territory of Zebulun and Naphtali' (4:13). Matthew sees "
                        "this as fulfilling Isaiah 9:1-2: 'The land of Zebulun and the land of Naphtali "
                        "... Galilee of the Gentiles -- the people dwelling in darkness have seen a great "
                        "light.' The light metaphor is cosmic: darkness represents the domain of the "
                        "hostile spiritual powers, and the light is the kingdom of God invading their "
                        "territory. Jesus' message is identical to John's: 'Repent, for the kingdom of "
                        "heaven is at hand' (4:17). He calls his first disciples -- Simon Peter and "
                        "Andrew, James and John -- from their fishing boats with the words 'Follow me, "
                        "and I will make you fishers of men' (4:19). This is not gentle invitation but "
                        "sovereign command -- the king recruiting his followers. The chapter closes with "
                        "a summary of Jesus' early ministry: teaching in synagogues, proclaiming the "
                        "gospel of the kingdom, and healing 'every disease and every affliction among "
                        "the people' (4:23). Crowds come from 'Galilee, the Decapolis, Jerusalem, Judea, "
                        "and beyond the Jordan' (4:25) -- a geographical expansion foreshadowing the "
                        "universal scope of the Great Commission."
            }
        ]
    },

    {
        "id": "matt-5-7",
        "ref": "Matthew 5-7",
        "chapter_num": 3,
        "title": "The Sermon on the Mount -- The Torah of the Kingdom",
        "era": "matt_ministry",
        "type": "study",

        "synopsis": "The Sermon on the Mount is the most famous discourse in human history and the "
                    "first of Matthew's five great teaching blocks. Jesus ascends 'the mountain' "
                    "(5:1) -- evoking Moses on Sinai -- and delivers the charter of the kingdom of "
                    "heaven. The Beatitudes (5:3-12) describe the citizens of the kingdom: the poor "
                    "in spirit, those who mourn, the meek, those who hunger for righteousness, the "
                    "merciful, the pure in heart, the peacemakers, and those persecuted for "
                    "righteousness' sake. The 'salt and light' sayings (5:13-16) define the community's "
                    "mission. The antitheses (5:21-48) -- 'You have heard that it was said... but I say "
                    "to you' -- demonstrate Jesus' authority to interpret Torah with an authority that "
                    "surpasses Moses himself. The Lord's Prayer (6:9-13) teaches the disciples to pray "
                    "for the kingdom's coming. The teaching on anxiety (6:25-34) calls for radical trust "
                    "in the Father's provision. The sermon concludes with the two builders (7:24-27): "
                    "those who hear Jesus' words and do them are building on rock; those who hear and "
                    "do not are building on sand. The crowds are 'astonished' because 'he was teaching "
                    "them as one who had authority (exousia), and not as their scribes' (7:28-29).",

        "key_verse": {
            "ref": "Matthew 5:17",
            "text": "Do not think that I have come to abolish the Law or the Prophets; I have not come to abolish them but to fulfill them.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "makarioi (blessed -- the Greek beatitude formula; equivalent to Hebrew ashre; not emotional happiness but divine favor and flourishing)",
            "dikaiosyne (righteousness -- right standing with God and right conduct before God; the central demand of the kingdom)",
            "pleroo (to fulfill -- not to abolish or replace but to fill up, to bring to fullest expression and intended meaning)",
            "teleios (perfect/complete -- 'Be perfect as your heavenly Father is perfect' (5:48); not sinlessness but wholeness, maturity, covenant faithfulness)",
            "basileia ton ouranon (kingdom of heaven -- the domain and rule of God breaking into the present age; the reality the Sermon describes)",
            "Abba / Pater (Father -- Jesus' characteristic address for God; the intimate relationship that grounds the Sermon's ethic)",
            "mammonas (mammon -- Aramaic loanword for wealth/possessions; personified as a rival deity: 'You cannot serve God and mammon' (6:24))"
        ],

        "ane_backdrop": "The Sermon on the Mount has parallels to ANE wisdom instruction literature, "
                        "particularly the Egyptian Instruction texts (Instruction of Ptah-hotep, "
                        "Instruction of Amenemope). Like these works, the Sermon provides comprehensive "
                        "guidance for righteous living from a figure of authority. However, the Sermon "
                        "transcends the wisdom genre: Jesus speaks not as a sage sharing observations "
                        "about life but as a king declaring the laws of his kingdom. The mountain "
                        "setting deliberately evokes Sinai, where Moses received the Torah from YHWH. "
                        "The six antitheses ('You have heard... but I say to you') function like a "
                        "royal edict -- Jesus claims an authority that goes beyond interpreting Moses "
                        "to issuing authoritative rulings that intensify and fulfill the Torah. The "
                        "Lord's Prayer's opening ('Our Father in heaven') uses language familiar from "
                        "Mesopotamian prayers addressing patron deities, but transforms it: the God "
                        "of Israel is not merely a patron but a Father whose kingdom is coming to earth.",

        "second_temple": [
            {
                "source": "Didache 1-6 (~90-100 AD)",
                "summary": "The Didache ('Teaching of the Twelve Apostles') opens with a 'Two Ways' "
                           "section that draws extensively on the Sermon on the Mount, incorporating "
                           "the Golden Rule, the command to love enemies, and other Matthean teachings "
                           "into a catechetical manual for new converts.",
                "relevance": "Demonstrates that the Sermon on the Mount was being used as a baptismal "
                             "catechism within decades of the Gospel's composition."
            },
            {
                "source": "Qumran Community Rule (1QS)",
                "summary": "The Community Rule outlines ethical requirements for members, including "
                           "instructions on loving fellow community members and hating outsiders (1QS "
                           "1:9-10). Jesus' command to 'love your enemies' (Matt 5:44) stands in "
                           "direct contrast to this sectarian ethic.",
                "relevance": "Highlights the radical nature of Jesus' ethic: even Qumran, with its "
                             "intense Torah devotion, did not command love of enemies."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 19-24", "note": "The Sinai covenant -- Moses on the mountain receiving Torah; Jesus on the mountain delivering the new Torah of the kingdom", "type": "ot"},
            {"ref": "Psalm 1:1-3", "note": "'Blessed is the man...' -- the Torah-meditation ideal that the Beatitudes develop into a full portrait of kingdom citizenship", "type": "ot"},
            {"ref": "Deuteronomy 6:4-9", "note": "The Shema -- 'You shall love the LORD your God with all your heart' -- the foundational commandment behind the Sermon's entire ethic", "type": "ot"},
            {"ref": "Luke 6:20-49", "note": "Luke's 'Sermon on the Plain' -- a shorter parallel with 'Blessed are the poor' (not 'poor in spirit') and 'Woe to you who are rich'", "type": "nt"},
            {"ref": "James 1-5", "note": "James' epistle as practical application of the Sermon's ethic -- faith without works, taming the tongue, patience in suffering", "type": "nt"},
            {"ref": "Romans 12:14-21", "note": "Paul's ethic of enemy-love and non-retaliation -- parallel to Matt 5:38-48", "type": "nt"}
        ],

        "divine_council_note": "The Sermon on the Mount is the constitution of the kingdom that has "
                               "invaded the domain of the hostile powers. Its ethic is not mere moral "
                               "teaching -- it describes life under YHWH's rule in contrast to life under "
                               "the governance of the rebellious elohim. When Jesus says 'You have heard "
                               "that it was said... but I say to you,' he speaks with authority that "
                               "surpasses Moses -- an authority that can only belong to one who shares "
                               "YHWH's throne. The Lord's Prayer is a divine council document: 'Our "
                               "Father in heaven' addresses the Most High God, enthroned in the heavenly "
                               "assembly. 'Hallowed be your name' declares YHWH's supreme authority over "
                               "all other spiritual powers. 'Your kingdom come, your will be done, on "
                               "earth as it is in heaven' (6:10) is a prayer for the heavenly council's "
                               "rule to be replicated on earth -- displacing the corrupt governance of "
                               "the territorial spirits. 'Deliver us from the evil one' (6:13) is a "
                               "plea for protection from the adversary who rules the present age. The "
                               "personification of mammon (6:24, 'You cannot serve God and mammon') may "
                               "reflect the Jewish tradition of spiritual powers behind material forces -- "
                               "wealth as a rival god demanding allegiance. The entire Sermon is training "
                               "for citizens of the kingdom that has come to reclaim the earth from the "
                               "powers of darkness.",

        "sections": [
            {
                "heading": "The Beatitudes: Citizens of the Kingdom (5:1-12)",
                "body": "Jesus ascends the mountain, sits down (the posture of a rabbi teaching with "
                        "authority, or a king on his throne), and opens his mouth to teach. The eight "
                        "Beatitudes form a poetic portrait of kingdom citizenship. 'Blessed (makarioi) "
                        "are the poor in spirit (hoi ptochoi to pneumati)' (5:3) -- not the materially "
                        "destitute (as in Luke's version) but those who recognize their spiritual "
                        "bankruptcy before God. 'For theirs is the kingdom of heaven' -- present tense, "
                        "the kingdom belongs to them now. The mourners will be comforted (5:4; echoing "
                        "Isaiah 61:2). The meek (praus -- gentle, humble, not self-asserting) will "
                        "inherit the earth (5:5; quoting Psalm 37:11). Those who hunger and thirst for "
                        "righteousness will be satisfied (5:6). The merciful will receive mercy (5:7). "
                        "The pure in heart will see God (5:8; echoing Psalm 24:3-4). The peacemakers "
                        "will be called 'sons of God' (huioi theou, 5:9) -- a divine council title: "
                        "the peacemakers share the family identity of YHWH himself. Those persecuted "
                        "for righteousness' sake inherit the kingdom (5:10). Jesus concludes: 'Rejoice "
                        "and be glad, for your reward is great in heaven, for so they persecuted the "
                        "prophets who were before you' (5:12) -- the community is placed in the line "
                        "of the prophets, those who spoke for the divine council."
            },
            {
                "heading": "The Antitheses: Jesus' Authority Over Torah (5:17-48)",
                "body": "Jesus first declares: 'Do not think that I have come to abolish the Law or "
                        "the Prophets; I have not come to abolish them but to fulfill (plerosai) them' "
                        "(5:17). Then he issues six antitheses that intensify, deepen, and radicalize "
                        "the Torah: (1) Murder expanded to anger (5:21-26): even calling someone 'Raka' "
                        "(Aramaic: 'empty one, worthless') or 'fool' is subject to judgment. (2) Adultery "
                        "expanded to lust (5:27-30): the lustful gaze is adultery of the heart. (3) "
                        "Divorce restricted (5:31-32): Moses permitted divorce, but Jesus limits it to "
                        "cases of porneia (sexual immorality). (4) Oaths abolished (5:33-37): do not "
                        "swear at all -- let your yes be yes. (5) Retaliation replaced with generosity "
                        "(5:38-42): 'Do not resist the one who is evil. But if anyone slaps you on the "
                        "right cheek, turn to him the other also.' (6) Enemy-love commanded (5:43-48): "
                        "'Love your enemies and pray for those who persecute you, so that you may be "
                        "sons (huioi) of your Father who is in heaven' (5:44-45). The reasoning is "
                        "theological: God sends rain on the just and unjust alike. The standard is "
                        "staggering: 'You therefore must be perfect (teleioi), as your heavenly Father "
                        "is perfect' (5:48)."
            },
            {
                "heading": "The Lord's Prayer and Trust in the Father (6:1-34)",
                "body": "Chapter 6 addresses the interior life of the kingdom citizen: giving (6:1-4), "
                        "praying (6:5-15), fasting (6:16-18), and trust (6:19-34). The Lord's Prayer "
                        "(6:9-13) is the center: 'Our Father in heaven, hallowed be your name. Your "
                        "kingdom come, your will be done, on earth as it is in heaven. Give us this "
                        "day our daily bread, and forgive us our debts, as we also have forgiven our "
                        "debtors. And lead us not into temptation, but deliver us from the evil one.' "
                        "Each petition has divine council resonance: 'hallowed be your name' declares "
                        "YHWH supreme over all rival powers; 'your kingdom come' prays for the "
                        "displacement of the hostile rulers; 'on earth as in heaven' asks for the "
                        "heavenly council's rule to extend to the earthly realm; 'deliver us from the "
                        "evil one' (tou ponerou) is protection against the adversary. Jesus then "
                        "addresses anxiety about provision (6:25-34): 'Do not be anxious about your "
                        "life... Look at the birds of the air... Consider the lilies of the field.' "
                        "The argument is from creation theology: the Father who sustains the whole "
                        "created order will sustain his children. 'Seek first the kingdom of God and "
                        "his righteousness, and all these things will be added to you' (6:33). The "
                        "kingdom is the priority; everything else follows."
            },
            {
                "heading": "The Two Ways: Rock and Sand (7:1-29)",
                "body": "Chapter 7 concludes the Sermon with practical instructions and the decisive "
                        "choice. 'Judge not, that you be not judged' (7:1) -- not a prohibition against "
                        "discernment but against hypocritical condemnation (the log and speck, 7:3-5). "
                        "'Ask, and it will be given to you; seek, and you will find; knock, and it will "
                        "be opened to you' (7:7) -- the Father gives good things to those who ask. The "
                        "Golden Rule: 'Whatever you wish that others would do to you, do also to them, "
                        "for this is the Law and the Prophets' (7:12). Then the warning: the gate is "
                        "narrow and the way is hard that leads to life (7:13-14). Beware of false "
                        "prophets -- wolves in sheep's clothing (7:15-20). 'Not everyone who says to "
                        "me, \"Lord, Lord,\" will enter the kingdom of heaven, but the one who does the "
                        "will of my Father who is in heaven' (7:21) -- even those who prophesy and cast "
                        "out demons in Jesus' name may be rejected if they practice 'lawlessness' "
                        "(anomian, 7:23). The Sermon closes with the parable of the two builders: 'the "
                        "rain fell, and the floods came, and the winds blew' (7:25, 27) -- the language "
                        "of cosmic judgment testing every life. Building on rock (Jesus' words) survives; "
                        "building on sand collapses. The crowds respond with astonishment at his "
                        "authority (exousia) -- an authority that surpasses the scribes (7:28-29)."
            }
        ]
    },

    {
        "id": "matt-8-10",
        "ref": "Matthew 8-10",
        "chapter_num": 4,
        "title": "Miracles of the Kingdom and the Mission of the Twelve",
        "era": "matt_ministry",
        "type": "study",

        "synopsis": "After the Sermon on the Mount's words, Matthew presents the kingdom's works: a "
                    "cascade of ten miracles demonstrating Jesus' authority over disease (leper, "
                    "centurion's servant, Peter's mother-in-law, the sick at evening), nature (the "
                    "storm stilled), demons (the Gadarene demoniacs), paralysis, death (Jairus' "
                    "daughter), blindness, and muteness. Interwoven are discipleship episodes that "
                    "reveal the cost of following Jesus. The centurion's faith (8:5-13) provokes "
                    "Jesus' remarkable declaration: 'Many will come from east and west and recline "
                    "at table with Abraham, Isaac, and Jacob in the kingdom of heaven, while the "
                    "sons of the kingdom will be thrown into the outer darkness' (8:11-12) -- the "
                    "Gentile inclusion theme. Chapter 10 records the Mission Discourse: Jesus sends "
                    "the Twelve with authority over unclean spirits and diseases, instructing them "
                    "to proclaim 'The kingdom of heaven is at hand' (10:7). He warns of persecution, "
                    "family division, and the need for absolute loyalty: 'Whoever does not take his "
                    "cross and follow me is not worthy of me' (10:38).",

        "key_verse": {
            "ref": "Matthew 8:11-12",
            "text": "I tell you, many will come from east and west and recline at table with Abraham, Isaac, and Jacob in the kingdom of heaven, while the sons of the kingdom will be thrown into the outer darkness.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "exousia (authority -- delegated power; Jesus has authority over disease, demons, nature, and death; he delegates it to the Twelve)",
            "daimonizomai (to be demonized -- not merely 'possessed' but under the oppressive influence of demonic powers)",
            "pistis (faith -- trusting reliance on Jesus' authority; the centurion's faith surpasses Israel's)",
            "stauros (cross -- the instrument of Roman execution; Jesus introduces it as the symbol of radical discipleship)",
            "apostolos (apostle / sent one -- from apostello, 'to send'; the Twelve are commissioned agents of the kingdom)",
            "exousia akathartou pneumaton (authority over unclean spirits -- the delegated power to confront and expel hostile spiritual beings)"
        ],

        "ane_backdrop": "The miracle collections in chapters 8-9 follow a pattern known in ancient "
                        "biographical literature: after the hero's inaugural speech, his deeds demonstrate "
                        "his authority. The stilling of the storm (8:23-27) draws on the ANE motif of the "
                        "divine warrior who conquers the chaotic sea: in Ugaritic mythology, Baal defeats "
                        "Yam (Sea); in the Enuma Elish, Marduk defeats Tiamat (the sea monster). YHWH's "
                        "power over the sea is celebrated in Psalms 74:13-14; 89:9-10; 93:3-4; and "
                        "Job 38:8-11. When Jesus rebukes the wind and sea, he exercises the divine "
                        "prerogative -- authority over chaos. The Gadarene exorcism (8:28-34) involves "
                        "demons who recognize Jesus as 'Son of God' and beg not to be tormented 'before "
                        "the time' (pro kairou) -- acknowledging that an eschatological judgment awaits "
                        "them. The mission discourse (ch. 10) parallels the commissioning of ancient "
                        "royal emissaries: the sent ones carry the authority of the sender.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 8.46-49",
                "summary": "Josephus describes Solomon as an exorcist and records witnessing an exorcism "
                           "performed by a Jew named Eleazar who used a ring with a Solomonic root and "
                           "incantations attributed to Solomon.",
                "relevance": "Shows that Jewish exorcism traditions existed alongside Jesus' ministry. "
                             "The key difference: Jesus exorcises by his own authority ('I cast out demons "
                             "by the Spirit of God,' Matt 12:28), not by incantations or magical objects."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 53:4", "note": "'He took our illnesses and bore our diseases' -- quoted in Matt 8:17 as fulfilled in Jesus' healing ministry", "type": "ot"},
            {"ref": "Psalm 107:23-32", "note": "YHWH stills the storm and calms the sea -- the background to Jesus' stilling of the storm, identifying him with YHWH's authority over chaos", "type": "ot"},
            {"ref": "Mark 5:1-20", "note": "Mark's longer parallel to the Gadarene exorcism -- one demoniac named 'Legion,' with more detail on the dialogue", "type": "nt"},
            {"ref": "Luke 10:1-20", "note": "Luke's sending of the Seventy-two -- a broader mission foreshadowing the Gentile mission", "type": "nt"},
            {"ref": "Psalm 82:6-7", "note": "The judgment of the gods who failed in their governance -- the demons' fear of being tormented 'before the time' anticipates this final judgment", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "The Son of Man's authority over all nations -- the background to Jesus' delegated authority", "type": "ot"}
        ],

        "divine_council_note": "The miracle chapters demonstrate that the kingdom of heaven is not "
                               "merely a teaching program but an invasion of enemy-held territory. Each "
                               "miracle category represents a domain of the hostile powers being reclaimed: "
                               "disease (the corruption of the body), demons (direct spiritual oppression), "
                               "nature (chaos threatening the created order), and death (the ultimate enemy). "
                               "The Gadarene exorcism (8:28-34) is particularly revealing: the demons "
                               "identify Jesus as 'Son of God' and ask 'Have you come here to torment us "
                               "before the time (pro kairou)?' The 'time' they reference is the final "
                               "judgment of the rebellious elohim -- the day when the sentence of Psalm "
                               "82:6-7 is executed and the gods 'die like men.' The demons know their "
                               "destiny; they know Jesus has the authority to execute it; they are terrified "
                               "that the timetable has been accelerated. The mission of the Twelve (ch. 10) "
                               "extends the kingdom invasion: Jesus delegates his exousia (authority) over "
                               "unclean spirits to his followers, making them agents of the divine council's "
                               "reclamation program. 'Behold, I am sending you out as sheep in the midst "
                               "of wolves' (10:16) -- the mission is dangerous precisely because it invades "
                               "territory held by hostile powers.",

        "sections": [
            {
                "heading": "Ten Miracles: The Kingdom in Action (8:1 - 9:34)",
                "body": "Matthew arranges ten miracles in three groups, interspersed with discipleship "
                        "teaching. Group 1 (8:1-17): Three healings -- a leper cleansed (echoing Elisha's "
                        "healing of Naaman, showing Jesus' superiority to the prophets), the centurion's "
                        "servant healed at a distance (the first Gentile faith story, provoking Jesus' "
                        "declaration about 'many from east and west' at the messianic banquet), and "
                        "Peter's mother-in-law healed. The evening healings fulfill Isaiah 53:4: 'He "
                        "took our illnesses and bore our diseases' (8:17). Group 2 (8:23 - 9:8): Three "
                        "nature/spiritual miracles -- the storm stilled (Jesus rebukes the sea as YHWH "
                        "rebukes chaos), the Gadarene demoniacs exorcised (demons expelled into pigs, "
                        "which rush into the sea -- chaos returning to chaos), and a paralytic forgiven "
                        "and healed (the double miracle: 'that you may know that the Son of Man has "
                        "authority on earth to forgive sins,' 9:6). Group 3 (9:18-34): Four more "
                        "miracles -- Jairus' daughter raised, the hemorrhaging woman healed, two blind "
                        "men given sight, and a mute demoniac freed. The crescendo is clear: authority "
                        "over disease, over demons, over nature, over death itself."
            },
            {
                "heading": "The Mission of the Twelve (10:1-42)",
                "body": "Jesus summons the Twelve and gives them 'authority (exousia) over unclean spirits, "
                        "to cast them out, and to heal every disease and every affliction' (10:1). The "
                        "initial scope is limited: 'Go nowhere among the Gentiles... but go rather to "
                        "the lost sheep of the house of Israel' (10:5-6). This is not exclusion of "
                        "Gentiles but priority of Israel -- the covenant people must hear first. The "
                        "message: 'The kingdom of heaven is at hand' (10:7), confirmed by miracles: "
                        "'Heal the sick, raise the dead, cleanse lepers, cast out demons. You received "
                        "without paying; give without pay' (10:8). But the mission will be opposed: "
                        "'I am sending you out as sheep in the midst of wolves' (10:16). They will be "
                        "handed over to councils, flogged in synagogues, and dragged before governors "
                        "(10:17-18). Family members will betray each other (10:21). 'You will be hated "
                        "by all for my name's sake' (10:22). The comfort: 'Do not fear those who kill "
                        "the body but cannot kill the soul. Rather fear him who can destroy both soul "
                        "and body in hell' (10:28). Even the hairs of their heads are numbered (10:30). "
                        "The radical demand: 'Whoever loves father or mother more than me is not worthy "
                        "of me' (10:37). 'Whoever does not take his cross and follow me is not worthy "
                        "of me' (10:38) -- the first mention of the cross in Matthew."
            }
        ]
    },

    {
        "id": "matt-11-13",
        "ref": "Matthew 11-13",
        "chapter_num": 5,
        "title": "The Kingdom Questioned, the Strong Man Bound, and the Parables",
        "era": "matt_ministry",
        "type": "study",

        "synopsis": "Chapters 11-13 mark a turning point in Matthew's narrative. John the Baptist, "
                    "imprisoned, sends a question: 'Are you the one who is to come, or shall we look "
                    "for another?' (11:3). Jesus responds with his messianic resume -- the works of "
                    "Isaiah 35 and 61 are happening. He denounces the unrepentant cities (Chorazin, "
                    "Bethsaida, Capernaum) and utters the great thanksgiving: 'All things have been "
                    "handed over to me by my Father, and no one knows the Son except the Father, and "
                    "no one knows the Father except the Son' (11:27) -- a claim of unique divine "
                    "knowledge. Chapter 12 contains the Beelzebul controversy, the theological "
                    "centerpiece of the Gospel: Jesus' exorcisms prove the kingdom has come, and "
                    "blaspheming the Spirit's work is the unforgivable sin. Chapter 13 delivers the "
                    "Parables Discourse -- seven parables revealing the kingdom's hidden, growing, "
                    "costly, and all-encompassing nature. The kingdom is a sower's seed, a mustard "
                    "seed, yeast, hidden treasure, a pearl of great price, a dragnet. Its growth is "
                    "mysterious, its value incomparable, and its consummation certain.",

        "key_verse": {
            "ref": "Matthew 12:28-29",
            "text": "But if it is by the Spirit of God that I cast out demons, then the kingdom of God has come upon you. Or how can someone enter a strong man's house and plunder his goods, unless he first binds the strong man? Then indeed he may plunder his house.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Beelzeboul (Beelzebul -- from Baal-Zebub/'lord of flies' or Baal-Zebul/'lord of the high place'; a derogatory name for Satan as prince of demons)",
            "ephthasen (has come upon -- aorist of phthano; the kingdom has arrived, not merely approached; decisive, completed arrival)",
            "ischuros (strong man -- Satan as the fortified ruler whose domain Jesus invades; binding language echoes apocalyptic judgment)",
            "blasphemia tou pneumatos (blasphemy against the Spirit -- attributing the Spirit's liberating work to Satan; the unforgivable sin because it rejects the very means of forgiveness)",
            "mysterion (mystery -- the parables reveal the 'secrets of the kingdom of heaven' (13:11); not puzzles but revealed truths hidden from the unperceptive)",
            "parabole (parable -- from paraballo, 'to throw alongside'; stories that illuminate the kingdom by comparison with everyday experience)"
        ],

        "ane_backdrop": "The Beelzebul controversy connects to the long history of ANE spiritual "
                        "warfare theology. The name 'Beelzebul' is likely a deliberate corruption of "
                        "'Baal-Zebul' ('Lord of the High Place' or 'Prince Baal'), degraded in 2 Kings "
                        "1:2-3 to 'Baal-Zebub' ('Lord of the Flies') -- a mocking distortion of the "
                        "Canaanite deity's title. By Jesus' day, this name had become a designation for "
                        "the prince of demons. The 'strong man' parable (12:29) uses the language of "
                        "ancient siege warfare: entering a fortified house (oikia), binding (desai) the "
                        "owner, and plundering (diarpasai) his goods. This is cosmic conquest language. "
                        "The parables of chapter 13 draw on agricultural imagery universal in ANE "
                        "culture but use it to describe realities unseen in any ANE mythology: a kingdom "
                        "that starts invisibly small (mustard seed), works from within (yeast), is worth "
                        "everything (pearl), and will be sorted at the end of the age (dragnet).",

        "second_temple": [
            {
                "source": "Testament of Solomon (1st-3rd century AD)",
                "summary": "This pseudepigraphal work describes Solomon commanding demons by divine "
                           "authority, interrogating them about their names and functions, and binding "
                           "them to build the Temple. The 'binding' language parallels Matthew 12:29.",
                "relevance": "Reflects the widespread Jewish tradition that spiritual authorities can "
                             "be bound and subjected -- a framework Jesus invokes in the strong man parable."
            },
            {
                "source": "1 Enoch 10:4-6",
                "summary": "God commands the angel Raphael to 'bind Azazel hand and foot' and cast "
                           "him into darkness until the day of judgment. The binding of rebellious "
                           "spiritual powers is a core theme of apocalyptic literature.",
                "relevance": "The 'binding the strong man' motif in Matt 12:29 resonates with the "
                             "Enochic tradition of binding rebellious watchers/spirits."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 35:5-6", "note": "'The eyes of the blind shall be opened, the ears of the deaf unstopped...' -- the messianic signs Jesus points to in his answer to John (11:4-5)", "type": "ot"},
            {"ref": "Isaiah 61:1", "note": "'The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the poor' -- the background to Jesus' claim that the kingdom has come", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "The Son of Man's authority -- background to Jesus' 'Son of Man' title used throughout these chapters (12:8, 32, 40)", "type": "ot"},
            {"ref": "Psalm 78:2", "note": "'I will open my mouth in a parable; I will utter dark sayings from of old' -- quoted in Matt 13:35 as the basis for Jesus' parabolic teaching", "type": "ot"},
            {"ref": "Mark 3:22-30", "note": "Mark's parallel Beelzebul controversy -- includes the 'blasphemy against the Holy Spirit' warning with Mark's characteristic urgency", "type": "nt"},
            {"ref": "1 Enoch 10:4-6", "note": "The binding of Azazel -- apocalyptic background to the 'binding the strong man' in Matt 12:29", "type": "noncanonical"},
            {"ref": "Revelation 20:1-3", "note": "Satan bound for a thousand years -- the eschatological fulfillment of the 'binding the strong man' that Jesus began in his ministry", "type": "nt"}
        ],

        "divine_council_note": "Matthew 12:22-29 is the single most important passage in the Gospel "
                               "for understanding the divine council conflict. The Pharisees' accusation "
                               "-- 'It is only by Beelzebul, the prince of demons, that this man casts out "
                               "demons' (12:24) -- forces Jesus to make his theology of cosmic warfare "
                               "explicit. His argument is a fortiori: if Satan is divided against himself, "
                               "his kingdom cannot stand (12:26). Therefore, the exorcisms must come from "
                               "a power opposed to Satan. 'If it is by the Spirit of God that I cast out "
                               "demons, then the kingdom of God has come upon you' (12:28). The verb "
                               "ephthasen is decisive -- not 'is coming' but 'has come.' The kingdom has "
                               "arrived. The evidence? The strong man (Satan) is being bound and his house "
                               "plundered (12:29). Every exorcism is an act of plundering -- liberating a "
                               "human being from the jurisdiction of the enemy and transferring them to the "
                               "kingdom of God. The 'unforgivable sin' -- blasphemy against the Holy Spirit "
                               "(12:31-32) -- is the deliberate attribution of the Spirit's liberating work "
                               "to Satan. This is not a casual mistake but a willful identification of light "
                               "as darkness, of liberation as enslavement, of the divine council's rescue "
                               "operation as demonic activity. It is unforgivable not because God's mercy "
                               "has limits but because the one who calls the Spirit's work satanic has "
                               "cut himself off from the very means of forgiveness. The parables of "
                               "chapter 13 then describe the kingdom's operation within enemy territory: "
                               "it grows secretly (mustard seed, yeast), it coexists with evil until the "
                               "harvest (wheat and tares), and it will be definitively separated at the "
                               "end (dragnet, furnace of fire).",

        "sections": [
            {
                "heading": "John's Question and Jesus' Answer (11:1-19)",
                "body": "John the Baptist, imprisoned by Herod Antipas (14:3-4), sends disciples to "
                        "ask Jesus: 'Are you the one who is to come (ho erchomenos), or shall we look "
                        "for another?' (11:3). The question reveals John's own struggle: he expected "
                        "the Messiah to bring judgment (3:10-12), but Jesus is healing and teaching "
                        "rather than wielding the axe. Jesus responds not with a direct claim but with "
                        "evidence: 'The blind receive their sight and the lame walk, lepers are cleansed "
                        "and the deaf hear, and the dead are raised up, and the poor have good news "
                        "preached to them' (11:5) -- a catalog drawn from Isaiah 35:5-6 and 61:1. "
                        "The messianic signs are happening. Then: 'Blessed is the one who is not "
                        "offended (skandalisthai) by me' (11:6) -- the Messiah who heals before he "
                        "judges is a stumbling block to those expecting immediate cosmic overthrow."
            },
            {
                "heading": "The Beelzebul Controversy: The Strong Man Bound (12:22-37)",
                "body": "Jesus heals a demon-oppressed man who was blind and mute (12:22). The crowds "
                        "wonder: 'Can this be the Son of David?' (12:23). The Pharisees counter: 'It "
                        "is only by Beelzebul, the prince (archon) of demons, that this man casts out "
                        "demons' (12:24). The term archon (ruler, prince) is significant -- it is the "
                        "same word Paul uses for the spiritual 'rulers' in Ephesians 6:12. Jesus' "
                        "response is devastating: a kingdom divided against itself cannot stand (12:25). "
                        "If Satan casts out Satan, his kingdom is collapsing from within. The true "
                        "explanation: 'If it is by the Spirit of God (en pneumati theou) that I cast "
                        "out demons, then the kingdom of God has come upon you (ephthasen eph hymas)' "
                        "(12:28). This is the most important sentence in the Beelzebul controversy: "
                        "the arrival of the kingdom is proven by the expulsion of demons. Then the "
                        "strong man parable: 'How can someone enter a strong man's house and plunder "
                        "his goods, unless he first binds the strong man? Then indeed he may plunder "
                        "his house' (12:29). Satan is the strong man. His 'house' is the domain of "
                        "the nations and people he controls. Jesus has come to bind him and free the "
                        "captives. The warning about blasphemy against the Spirit (12:31-32) follows: "
                        "attributing the Spirit's work to Satan is the one sin that cannot be forgiven, "
                        "because it rejects the very agent of forgiveness."
            },
            {
                "heading": "The Parables Discourse: Secrets of the Kingdom (13:1-58)",
                "body": "Jesus teaches in parables (parabolai) -- stories drawn from everyday life "
                        "that reveal 'the secrets (mysteria) of the kingdom of heaven' (13:11). The "
                        "Sower (13:3-23): the word of the kingdom is scattered broadly; its reception "
                        "depends on the soil -- the path (Satan snatches the word), rocky ground "
                        "(persecution causes falling away), thorns (cares and wealth choke it), and "
                        "good soil (fruitful life). The Wheat and Tares (13:24-30, 36-43): the kingdom "
                        "and evil coexist until the harvest (the end of the age), when the Son of Man "
                        "sends his angels to separate them. This parable addresses the puzzle of why "
                        "the kingdom has come but evil persists -- the answer is patience, not "
                        "premature judgment. The Mustard Seed and Yeast (13:31-33): the kingdom starts "
                        "invisibly small and grows to encompass everything -- from a tiny seed to the "
                        "greatest of garden plants, from a pinch of yeast to three measures of flour "
                        "leavened throughout. The Hidden Treasure and Pearl (13:44-46): the kingdom is "
                        "worth everything -- the man sells all he has for the treasure, the merchant "
                        "sells everything for the pearl. The Dragnet (13:47-50): at the end of the age, "
                        "the angels will separate the evil from the righteous -- the final sorting that "
                        "the kingdom awaits. Jesus asks: 'Have you understood all these things?' They "
                        "say 'Yes' (13:51). 'Every scribe trained for the kingdom of heaven is like a "
                        "master of a house, who brings out of his treasure what is new and what is old' "
                        "(13:52) -- the kingdom scholar draws on the whole tradition, old and new."
            }
        ]
    }
]
