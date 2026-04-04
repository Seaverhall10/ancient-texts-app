"""
era_daniel_court.py -- The Court Tales (Daniel 1-6)

The first half of Daniel presents six narrative episodes set in the courts of
Babylon and Persia. Written partly in Hebrew (chapter 1) and partly in Aramaic
(chapters 2-6), these court tales demonstrate that YHWH remains sovereign over
the greatest empires on earth. Faithful Jews can survive and thrive in exile
without compromising their covenant loyalty. The tales contain remarkable
divine council content: the "fourth figure" in the fiery furnace (bar elahin,
"a son of the gods"), the Watchers (irin) who decree Nebuchadnezzar's
humiliation, the handwriting on the wall at Belshazzar's feast, and the angel
who shuts the lions' mouths. Together, these episodes reveal that behind every
earthly empire stands a spiritual reality -- and YHWH is the God who rules
over all.
"""

CHAPTERS = [
    {
        "id": "dan-1-2",
        "ref": "Daniel 1-2",
        "chapter_num": 1,
        "title": "Faithful in Babylon and the Dream of the Great Statue",
        "era": "daniel_court",
        "type": "chapter",
        "themes": ["DREAM", "KING", "DC", "NATIONS"],

        "synopsis": "Daniel opens with the historical marker: 'In the third year of the reign of "
                    "Jehoiakim king of Judah, Nebuchadnezzar king of Babylon came to Jerusalem and "
                    "besieged it. And the Lord gave (vayyitten Adonai) Jehoiakim king of Judah into his "
                    "hand' (1:1-2). The critical theological statement is vayyitten Adonai -- 'the Lord "
                    "gave.' Nebuchadnezzar does not conquer by his own power; YHWH delivers Judah into "
                    "his hand as an instrument of judgment. Daniel and his three companions -- Hananiah, "
                    "Mishael, and Azariah -- are among the Judean youth selected for Babylonian court "
                    "service. They are given Babylonian names: Belteshazzar, Shadrach, Meshach, and "
                    "Abednego. Daniel 'resolved in his heart (vayyasem Daniel al-libbo) that he would not "
                    "defile himself with the king's food (pathbag) or with the wine he drank' (1:8). The "
                    "vegetable test follows: after ten days on vegetables and water, Daniel and his friends "
                    "appear healthier than those who ate the royal food. 'As for these four youths, God "
                    "gave them learning (madda) and skill (sekhel) in all literature and wisdom, and "
                    "Daniel had understanding (binah) in all visions and dreams' (1:17). Chapter 2 "
                    "introduces the first great prophetic vision: Nebuchadnezzar dreams of an enormous "
                    "statue with a head of gold, chest and arms of silver, belly and thighs of bronze, "
                    "legs of iron, and feet of iron mixed with clay. No Babylonian wise man can tell the "
                    "king his dream, but Daniel receives it by divine revelation: 'There is a God in "
                    "heaven (Elah bishmayya) who reveals mysteries (razin)' (2:28). Daniel interprets the "
                    "statue as four successive kingdoms: gold is Babylon, silver is Medo-Persia, bronze "
                    "is Greece, and iron is Rome. 'In the days of those kings, the God of heaven will set "
                    "up a kingdom that shall never be destroyed' (2:44). A stone 'cut without hands' "
                    "(di-la bidayin) strikes the statue on its feet and becomes a great mountain that fills "
                    "the whole earth -- God's eternal kingdom that replaces all human empires.",

        "key_verse": {
            "ref": "Daniel 2:44",
            "text": "And in the days of those kings the God of heaven will set up a kingdom that shall never be destroyed, nor shall the kingdom be left to another people. It shall break in pieces all these kingdoms and bring them to an end, and it shall stand forever.",
            "translation": "ESV"
        },

        "original_terms": [
            "vayyitten Adonai (and the Lord gave -- YHWH's sovereignty over Judah's defeat)",
            "pathbag (portion of food -- the royal diet Daniel refuses; a Persian loanword)",
            "Elah bishmayya (God in heaven -- the Aramaic designation for the Most High who reveals mysteries)",
            "raz (mystery/secret -- an Aramaic word (possibly borrowed from Persian) for divine secrets that are hidden from human understanding but can be revealed by God. This is NOT 'mystery' in the modern English sense of a puzzle to be solved by clever thinking. A raz is a divine council decision or cosmic plan that no human can access through their own intelligence -- it must be REVEALED from above. Daniel can interpret Nebuchadnezzar's dream not because he is smarter than the Babylonian wise men but because 'there is a God in heaven who reveals mysteries' (2:28). Paul later uses the Greek equivalent, mysterion, in the same way: divine plans hidden in God and now revealed through Christ, Eph 3:3-9)",
            "di-la bidayin (not by human hands -- the supernatural origin of God's kingdom-stone)",
            "madda (knowledge/learning -- the God-given intellectual gifts; Aramaic cognate of Hebrew da'at)",
            "sekhel (skill/insight -- practical wisdom granted by God for court service)"
        ],

        "ane_backdrop": "The Babylonian court education system is well attested in cuneiform sources. "
                        "Scribal schools (edubba) trained young men in Sumerian and Akkadian languages, "
                        "mathematics, astronomy, and literature. The 'literature and language of the "
                        "Chaldeans' (1:4) refers to the comprehensive curriculum of the Babylonian "
                        "intellectual elite. The dietary restrictions Daniel maintains reflect not merely "
                        "kashrut (Jewish dietary law) but resistance to cultural assimilation -- the royal "
                        "food would have been sacrificed to Babylonian gods (Marduk, Nabu) before serving. "
                        "Dream interpretation was a major component of Mesopotamian divination: the Assyrian "
                        "Dream Book (7th c. BC) catalogs dream symbols and their meanings. The difference "
                        "in Daniel is the source of interpretation: Babylonian practitioners relied on "
                        "omen manuals, while Daniel receives revelation directly from 'the God in heaven.' "
                        "The four-kingdom scheme of chapter 2 may interact with the Babylonian concept of "
                        "declining ages (gold, silver, bronze, iron), attested in the Sibylline Oracles and "
                        "Hesiod's Works and Days, but Daniel's version introduces the decisive element: "
                        "God's kingdom that shatters all human empires.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 10.186-210",
                "summary": "Josephus retells the court tales with embellishments, noting that "
                           "Nebuchadnezzar was deeply impressed by Daniel's interpretation. Josephus "
                           "adds that the fourth kingdom is Rome, though he carefully avoids predicting "
                           "Rome's destruction.",
                "relevance": "Josephus confirms that first-century Judaism read Daniel 2 as a prophecy of "
                             "sequential empires ending with Rome -- the same interpretation that shaped "
                             "New Testament eschatology."
            },
            {
                "source": "4 Ezra 11-12 (2 Esdras)",
                "summary": "The eagle vision of 4 Ezra reinterprets Daniel's four-kingdom scheme, "
                           "identifying the fourth kingdom explicitly as Rome and anticipating its "
                           "eschatological destruction.",
                "relevance": "The Second Temple apocalyptic tradition built directly on Daniel 2's "
                             "four-kingdom framework to interpret current events."
            }
        ],

        "cross_refs": [
            {"ref": "2 Kings 24:1-2", "note": "The historical account of Nebuchadnezzar's first siege of Jerusalem -- the setting for Daniel's deportation", "type": "ot"},
            {"ref": "Jeremiah 25:11-12", "note": "Jeremiah's prophecy of 70 years of Babylonian servitude -- the exile Daniel experiences", "type": "ot"},
            {"ref": "Matthew 21:44", "note": "'The one who falls on this stone will be broken to pieces; and when it falls on anyone, it will crush him' -- Jesus as the stone of Daniel 2:34-35", "type": "nt"},
            {"ref": "Luke 20:18", "note": "Jesus identifies himself with the crushing stone -- the kingdom of God that destroys all rival kingdoms", "type": "nt"},
            {"ref": "1 Peter 2:4-8", "note": "Christ as the 'living stone' -- the messianic stone tradition that begins with Daniel 2:34", "type": "nt"},
            {"ref": "Revelation 11:15", "note": "'The kingdom of the world has become the kingdom of our Lord and of his Christ' -- fulfilling Daniel 2:44", "type": "nt"},
            {"ref": "Isaiah 44:28-45:1", "note": "Cyrus as YHWH's instrument -- the same theology of divine sovereignty over pagan rulers as Daniel 1:2", "type": "ot"}
        ],

        "divine_council_note": "Daniel 1-2 establishes the foundational divine council principle of the "
                               "book: YHWH is sovereign over all earthly empires and their rulers. The "
                               "statement 'the Lord gave (vayyitten Adonai) Jehoiakim into his hand' (1:2) "
                               "means Nebuchadnezzar's conquest is not a failure of YHWH's power but an "
                               "exercise of it -- YHWH hands his own people over to a pagan king as "
                               "judgment. The phrase 'God in heaven who reveals mysteries' (Elah bishmayya "
                               "di-galeh razin, 2:28) locates divine knowledge in the heavenly council "
                               "chamber. The Babylonian wise men -- omen priests, magicians, enchanters, "
                               "sorcerers -- cannot access this knowledge because they serve gods who are "
                               "not the Most High. Daniel can access it because he serves the God who "
                               "presides over the council. The four-kingdom dream (2:31-45) reveals "
                               "something crucial about the divine council's governance: empires rise and "
                               "fall not by accident but by decree. Each metal in the statue represents a "
                               "kingdom permitted by YHWH to exercise temporal authority. The stone 'cut "
                               "without hands' (2:34, 45) that destroys the statue is divine in origin -- "
                               "no human agency produces it. This is the kingdom of the 'God of heaven' "
                               "(2:44) that will replace the kingdoms allotted to lesser powers.",

        "sections": [
            {
                "heading": "Captivity and the Vegetable Test: Faithfulness in Exile (Daniel 1)",
                "body": "The opening verse establishes the geopolitical and theological context: 'In the "
                        "third year of the reign of Jehoiakim king of Judah' (1:1) -- approximately "
                        "605 BC, the first of three deportations from Jerusalem. The critical phrase "
                        "'vayyitten Adonai' ('and the Lord gave') is the theological key to the entire "
                        "book: YHWH is not absent or defeated. He deliberately hands Jehoiakim to "
                        "Nebuchadnezzar as an act of sovereign judgment. The young Judean captives are "
                        "selected for three years of Babylonian education: 'youths without blemish, of "
                        "good appearance and skillful in all wisdom, endowed with knowledge, understanding "
                        "learning, and competent to stand in the king's palace' (1:4). The Babylonian "
                        "renaming is an act of cultural assimilation -- each Hebrew name containing the "
                        "divine name is replaced with a Babylonian theophoric: Daniel ('God is my judge') "
                        "becomes Belteshazzar ('Bel, protect his life'); Hananiah ('YHWH is gracious') "
                        "becomes Shadrach (possibly 'command of Aku,' the moon god); Mishael ('who is "
                        "what God is?') becomes Meshach (possibly 'who is what Aku is?'); Azariah ('YHWH "
                        "has helped') becomes Abednego ('servant of Nabu'). The names replace YHWH and "
                        "El with Bel, Aku, and Nabu -- Babylon's chief deities. Daniel's resistance is "
                        "not dietary legalism but covenant identity: eating the king's food would signify "
                        "loyalty to the king's gods. After ten days on vegetables (zero'im) and water, "
                        "the four appear healthier than those who ate the royal portions. 'God gave them "
                        "learning and skill in all literature and wisdom, and Daniel had understanding "
                        "in all visions and dreams' (1:17). The gifts are divine, not merely intellectual."
            },
            {
                "heading": "Nebuchadnezzar's Dream of the Statue: Four Kingdoms and God's Stone (Daniel 2)",
                "body": "Nebuchadnezzar dreams a dream that terrifies him, and he demands that his wise "
                        "men tell him both the dream and its interpretation -- an impossible test that "
                        "reveals the limitations of human divination. The Chaldeans protest: 'There is "
                        "not a man on earth who can meet the king's demand... no king, lord, or enchanter "
                        "has asked such a thing' (2:10). The king orders all wise men executed. Daniel "
                        "requests time, gathers his companions for prayer, and 'the mystery (raz) was "
                        "revealed to Daniel in a vision of the night (chezev di-lelyah)' (2:19). His "
                        "praise identifies the source: 'Blessed be the name of God (Elah) forever and "
                        "ever, to whom belong wisdom (chokmeta) and might (gevureta). He changes times "
                        "and seasons; he removes kings and sets up kings; he gives wisdom to the wise and "
                        "knowledge to those who have understanding; he reveals deep and hidden things "
                        "(amiqata umesatreta); he knows what is in the darkness, and the light dwells "
                        "with him' (2:20-22). Before the king, Daniel declares: 'There is a God in "
                        "heaven (Elah bishmayya) who reveals mysteries' (2:28). The statue: a head of "
                        "gold (dahava, Babylon), chest and arms of silver (kesaph, Medo-Persia), belly "
                        "and thighs of bronze (nechash, Greece), legs of iron (parzel, Rome), and feet of "
                        "iron mixed with clay (chasaph). 'You saw a stone (even) cut out by no human hand "
                        "(di-la bidayin), and it struck the image on its feet of iron and clay, and broke "
                        "them in pieces' (2:34). The stone became 'a great mountain and filled the whole "
                        "earth' (2:35). 'In the days of those kings the God of heaven will set up a "
                        "kingdom (malku) that shall never be destroyed' (2:44). Nebuchadnezzar falls on "
                        "his face and declares: 'Truly, your God is God of gods and Lord of kings, and a "
                        "revealer of mysteries' (2:47)."
            }
        ]
    },

    {
        "id": "dan-3",
        "ref": "Daniel 3",
        "chapter_num": 2,
        "title": "The Fiery Furnace and the Fourth Figure: Bar Elahin",
        "era": "daniel_court",
        "type": "chapter",
        "themes": ["KING", "HOLY", "NAME"],

        "synopsis": "Nebuchadnezzar erects a golden image (tselem di-dahav) ninety feet high on the plain "
                    "of Dura. All officials must bow and worship when the musical instruments sound; "
                    "refusal means death in a furnace of blazing fire (attun di-nur yaqidta). Shadrach, "
                    "Meshach, and Abednego refuse. Their confession before the king is one of the "
                    "boldest statements of faith in Scripture: 'If it be so (hen itai), our God whom we "
                    "serve is able to deliver us from the burning fiery furnace, and he will deliver us "
                    "out of your hand, O king. But if not (vehen la), be it known to you, O king, that "
                    "we will not serve your gods or worship the golden image that you have set up' "
                    "(3:17-18). The 'but if not' is crucial -- their obedience does not depend on "
                    "deliverance. Nebuchadnezzar, furious, orders the furnace heated seven times hotter. "
                    "The heat kills the soldiers who throw the three men in. Then Nebuchadnezzar is "
                    "astonished: 'Did we not cast three men bound into the fire?... I see four men "
                    "unbound, walking in the midst of the fire, and they are not hurt; and the appearance "
                    "of the fourth is like a son of the gods (bar elahin)' (3:24-25). The phrase bar "
                    "elahin is the Aramaic equivalent of Hebrew b'nei ha-elohim ('sons of God') -- the "
                    "technical term for divine council members in Genesis 6:2, 4; Job 1:6; 2:1; 38:7; "
                    "and Psalm 82:6. Nebuchadnezzar, a pagan king, recognizes what he sees: a divine "
                    "being, a member of the heavenly council, standing with the three men in the fire. "
                    "When they emerge, not even the smell of smoke is on them. Nebuchadnezzar's decree: "
                    "'Blessed be the God of Shadrach, Meshach, and Abednego, who has sent his angel "
                    "(mal'akeh) and delivered his servants' (3:28). The bar elahin is identified as "
                    "YHWH's mal'akh -- his angel, his emissary from the divine council.",

        "key_verse": {
            "ref": "Daniel 3:25",
            "text": "He answered and said, 'But I see four men unbound, walking in the midst of the fire, and they are not hurt; and the appearance of the fourth is like a son of the gods.'",
            "translation": "ESV"
        },

        "original_terms": [
            "bar elahin (son of the gods/son of God -- this Aramaic phrase is the equivalent of the Hebrew b'nei ha-elohim ('sons of God') used in Gen 6:2, Job 1:6, and Ps 82:6 for members of the divine council. Nebuchadnezzar, speaking from his polytheistic worldview, says 'a son of the gods' (plural, since he believes in many gods). But the narrator reveals the true identity: this is YHWH's own mal'akh ('angel/messenger'), sent to protect the faithful. The early church fathers (Irenaeus, Hippolytus, Tertullian) identified this figure as a pre-incarnate appearance of Christ -- the divine Son who walks with his people through the fire)",
            "tselem di-dahav (image of gold -- the idol Nebuchadnezzar commands all to worship)",
            "attun di-nur (furnace of fire -- the instrument of execution for those who refuse to worship)",
            "hen itai...vehen la (if it be so...but if not -- the defiant faith that does not require deliverance to remain loyal)",
            "mal'akh (angel/messenger -- the divine council emissary YHWH sends to the furnace)",
            "segid (to worship/bow down -- the Aramaic term for the compulsory worship Nebuchadnezzar demands)",
            "pelach (to serve -- the religious service the three Hebrews refuse to render to Babylon's gods)"
        ],

        "ane_backdrop": "The golden image on the plain of Dura has parallels in Mesopotamian religious "
                        "practice. Colossal cult statues were common in Babylonian temples -- the statue "
                        "of Marduk in the Esagila temple was famously adorned with gold. Royal image "
                        "veneration was both religious and political: bowing to the king's image was an act "
                        "of political loyalty as well as religious submission. The musical instruments "
                        "listed in Daniel 3:5 -- horn (qarna), pipe (mashroqita), lyre (qithros), "
                        "trigon (sabbeka), harp (pesanterin), and bagpipe (sumponeyah) -- include possible "
                        "Greek loanwords (qithros from kitharis, pesanterin from psalterion), which critics "
                        "cite as evidence of a late date but which conservatives explain as evidence of "
                        "Greek cultural influence reaching Mesopotamia through trade before Alexander. "
                        "Execution by fire is attested in Babylonian law: Hammurabi's Code prescribes "
                        "burning for certain offenses. The use of a furnace (attun) specifically may "
                        "reflect the brick kilns used in Babylonian construction projects.",

        "second_temple": [
            {
                "source": "Prayer of Azariah and Song of the Three Young Men (LXX/Theodotion additions)",
                "summary": "The Greek additions to Daniel 3 include Azariah's (Abednego's) prayer inside "
                           "the furnace and a hymn of cosmic praise sung by all three men, calling on all "
                           "creation to bless the Lord.",
                "relevance": "Though not in the Hebrew/Aramaic text, these additions show that Second "
                             "Temple Judaism developed the fiery furnace narrative as a paradigm of "
                             "faithful worship in the midst of persecution."
            },
            {
                "source": "1 Maccabees 2:59",
                "summary": "Mattathias on his deathbed exhorts his sons: 'Hananiah, Azariah, and Mishael "
                           "believed and were saved from the flame.'",
                "relevance": "The Maccabean resistance movement used the fiery furnace as a model for "
                             "faithful Jews facing pagan persecution -- the same pattern repeated under "
                             "Antiochus IV Epiphanes."
            },
            {
                "source": "Hebrews 11:34",
                "summary": "'Quenched the power of fire' -- listed among the heroes of faith.",
                "relevance": "The author of Hebrews includes the three men's deliverance from the furnace "
                             "in the catalog of faith's triumphs."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 6:2, 4", "note": "'The sons of God (b'nei ha-elohim) saw the daughters of man' -- the same council terminology as bar elahin in 3:25", "type": "ot"},
            {"ref": "Job 1:6; 2:1", "note": "'The sons of God came to present themselves before YHWH' -- the divine council assembly that includes the bar elahin figure", "type": "ot"},
            {"ref": "Psalm 82:6", "note": "'You are gods (elohim), sons of the Most High (b'nei Elyon)' -- the council members to whom bar elahin belongs", "type": "ot"},
            {"ref": "Isaiah 43:2", "note": "'When you walk through the fire you shall not be burned, and the flame shall not consume you' -- the promise fulfilled in Daniel 3", "type": "ot"},
            {"ref": "Hebrews 11:34", "note": "'Quenched the power of fire' -- the three men in the furnace as heroes of faith", "type": "nt"},
            {"ref": "1 Peter 1:7", "note": "'So that the tested genuineness of your faith -- more precious than gold that perishes though it is tested by fire' -- faith refined in the furnace", "type": "nt"},
            {"ref": "Revelation 1:15", "note": "Christ's feet 'like burnished bronze, refined in a furnace' -- the one who walks in fire", "type": "nt"}
        ],

        "divine_council_note": "Daniel 3 contains one of the most explicit divine council christophanies "
                               "in the Old Testament. The 'fourth figure' in the furnace is identified by "
                               "Nebuchadnezzar as bar elahin -- literally 'a son of the gods' or 'a son of "
                               "God.' This is the Aramaic equivalent of the Hebrew b'nei ha-elohim used in "
                               "Genesis 6:2, Job 1:6, and Job 38:7 for members of the divine council. The "
                               "Babylonian king, from his pagan frame of reference, uses the polytheistic "
                               "plural ('gods'), but the text reveals that this is YHWH's own agent -- "
                               "Nebuchadnezzar later identifies him as God's 'angel' (mal'akh, 3:28). The "
                               "bar elahin who walks in the fire with the faithful is a divine council "
                               "member sent by YHWH to protect those who refuse to worship false gods. "
                               "This is the Angel of YHWH tradition -- the visible manifestation of the "
                               "divine presence that appeared to Abraham (Gen 18), to Moses (Exod 3:2), "
                               "to Joshua (Josh 5:13-15), and to Gideon (Judg 6:11-12). In the divine "
                               "council framework, this figure is the second power in heaven -- the visible "
                               "YHWH who acts in the created realm while the invisible YHWH remains "
                               "enthroned. The early church fathers (Irenaeus, Hippolytus, Tertullian) "
                               "identified the fourth figure as a pre-incarnate appearance of Christ.",

        "sections": [
            {
                "heading": "The Golden Image and the Command to Worship (3:1-7)",
                "body": "Nebuchadnezzar erects a tselem di-dahav ('image of gold') that is sixty cubits "
                        "high and six cubits wide (3:1) -- approximately ninety feet tall and nine feet "
                        "wide. The dimensions suggest an obelisk or stele rather than a human-proportioned "
                        "statue. It is set on the plain of Dura (bi'qa'at Dura), a location in the "
                        "Babylonian province. The dedication ceremony assembles every level of officialdom: "
                        "'the satraps (achashdarpanayya), the prefects (sighnayya), the governors "
                        "(pachawata), the counselors (adargaz'rayya), the treasurers (gedavrayya), the "
                        "justices (detavrayya), the magistrates (tiphta'ye), and all the officials of "
                        "the provinces' (3:2). The political structure of the entire empire is present. "
                        "The herald announces: 'When you hear the sound of the horn, pipe, lyre, trigon, "
                        "harp, bagpipe, and every kind of music, you are to fall down (tippelu) and "
                        "worship (tisgedon) the golden image' (3:5). The penalty: 'whoever does not fall "
                        "down and worship shall be cast into a burning fiery furnace (attun di-nur "
                        "yaqidta)' (3:6). The command conflates political loyalty with religious worship "
                        "-- the same totalitarian demand that the Roman imperial cult would later impose "
                        "on early Christians."
            },
            {
                "heading": "The Defiant Faith: 'But If Not' (3:8-18)",
                "body": "Certain Chaldeans bring an accusation (akal qartseh, literally 'ate the pieces "
                        "of') against the three Jews. The charge is religious and political: 'There are "
                        "certain Jews whom you have appointed over the affairs of the province of Babylon: "
                        "Shadrach, Meshach, and Abednego. These men, O king, pay no attention to you; they "
                        "do not serve (pelach) your gods or worship (segid) the golden image that you have "
                        "set up' (3:12). Nebuchadnezzar summons them and offers a second chance (3:15), "
                        "adding: 'And who is the god that will deliver you out of my hands?' The question "
                        "is a direct challenge to YHWH's power -- the same challenge the Rabshakeh will "
                        "make before Jerusalem (2 Kings 18:35). The three men's response is one of the "
                        "most remarkable confessions in Scripture: 'O Nebuchadnezzar, we have no need to "
                        "answer you in this matter (pitgam). If it be so (hen itai), our God whom we serve "
                        "(pelach) is able (yakil) to deliver us from the burning fiery furnace, and he "
                        "will deliver us out of your hand, O king' (3:16-17). Then the pivot: 'But if not "
                        "(vehen la), be it known to you, O king, that we will not serve (pelach) your "
                        "gods or worship (segid) the golden image' (3:18). The 'but if not' is the "
                        "summit of biblical faith: their obedience is not contingent on deliverance. "
                        "Whether God rescues them or not, their covenant loyalty is absolute."
            },
            {
                "heading": "The Fourth Figure: A Son of the Gods (3:19-30)",
                "body": "Nebuchadnezzar, 'full of fury' (3:19), orders the furnace heated seven times "
                        "hotter. The soldiers who throw the three men in are killed by the heat -- an "
                        "ironic reversal: those who serve the king's command die, while those who defy "
                        "it survive. 'Then King Nebuchadnezzar was astonished (tewah) and rose up in "
                        "haste (bithval)' (3:24). His declaration: 'I see four men unbound (shrain), "
                        "walking (mehallekin) in the midst of the fire, and they are not hurt (chaval "
                        "la itai behon); and the appearance (reveh) of the fourth (revi'a'a) is like "
                        "a bar elahin (son of the gods)' (3:25). The word reveh means 'appearance, "
                        "form, aspect' -- Nebuchadnezzar sees something in the fourth figure that "
                        "transcends human appearance. The term bar elahin in its Aramaic context means "
                        "'a son of the gods' from a polytheistic perspective, but the narrator reveals "
                        "the true identity: YHWH's mal'akh ('angel, messenger'). Nebuchadnezzar "
                        "approaches the furnace door and calls: 'Shadrach, Meshach, and Abednego, "
                        "servants (avdohi) of the Most High God (Elaha Illaya), come out!' (3:26). The "
                        "title Elaha Illaya ('God Most High') is the Aramaic equivalent of Hebrew El "
                        "Elyon -- a title going back to Genesis 14:18-22 (Melchizedek&rsquo;s priesthood) "
                        "that declares YHWH as the supreme deity who presides over all other spiritual "
                        "beings in the divine council. A pagan king uses this title for Israel&rsquo;s God. When the three "
                        "emerge, 'the fire had not had any power (sholtan) over the bodies (geshmeihon) "
                        "of those men. The hair of their heads was not singed, their cloaks were not "
                        "harmed, and no smell of fire had come upon them' (3:27). The fire's power is "
                        "annulled by a greater power. Nebuchadnezzar's confession: 'Blessed be the God "
                        "of Shadrach, Meshach, and Abednego, who has sent his angel (mal'akeh) and "
                        "delivered his servants' (3:28)."
            }
        ]
    },

    {
        "id": "dan-4-5",
        "ref": "Daniel 4-5",
        "chapter_num": 3,
        "title": "The Watchers' Decree and the Writing on the Wall",
        "era": "daniel_court",
        "type": "chapter",
        "themes": ["DREAM", "KING", "DC", "NATIONS"],

        "synopsis": "Daniel 4 is unique in the Hebrew Bible: it is narrated by a pagan king. "
                    "Nebuchadnezzar issues a decree recounting his own humiliation and restoration. He "
                    "dreams of an enormous tree that reaches to heaven and provides food and shelter for "
                    "all creatures. Then 'a watcher (ir), a holy one (qaddish), came down from heaven' "
                    "(4:13) and decreed the tree's destruction -- but the stump and roots were to be "
                    "preserved, bound with iron and bronze. 'Let his mind be changed from a man's, and "
                    "let a beast's mind be given to him; and let seven periods of time pass over him. The "
                    "sentence (pitgama) is by the decree (gezerat) of the watchers (irin), the decision "
                    "(she'elta) by the word (me'amar) of the holy ones (qaddishin), to the end that the "
                    "living may know that the Most High (Illaya) rules the kingdom of men and gives it to "
                    "whom he will' (4:16-17). This is the ONLY passage in the canonical Bible that uses "
                    "the term 'Watcher' (ir) for angelic beings -- the same term used extensively in "
                    "1 Enoch for the rebellious angels who descended to Mount Hermon. But Daniel's "
                    "Watchers are faithful council members executing divine judgment. Daniel interprets: "
                    "the tree is Nebuchadnezzar, and the sentence means he will be driven from among men "
                    "to live with beasts, eating grass like an ox, until he acknowledges the Most High's "
                    "sovereignty. The prophecy is fulfilled: Nebuchadnezzar is struck with a form of "
                    "insanity (possibly boanthropy) and lives among animals for 'seven times.' His "
                    "restoration comes when 'I lifted my eyes to heaven, and my reason returned to me, "
                    "and I blessed the Most High' (4:34). Chapter 5 shifts to Belshazzar's feast. The "
                    "king drinks from the sacred vessels taken from the Jerusalem temple. A hand appears "
                    "and writes on the wall: MENE MENE TEKEL UPHARSIN. Daniel interprets: 'MENE -- God "
                    "has numbered your kingdom and finished it. TEKEL -- you have been weighed in the "
                    "balances and found wanting. PERES -- your kingdom has been divided and given to the "
                    "Medes and Persians' (5:26-28). That night Belshazzar is killed and Darius the Mede "
                    "receives the kingdom.",

        "key_verse": {
            "ref": "Daniel 4:17",
            "text": "The sentence is by the decree of the watchers, the decision by the word of the holy ones, to the end that the living may know that the Most High rules the kingdom of men and gives it to whom he will and sets over it the lowliest of men.",
            "translation": "ESV"
        },

        "original_terms": [
            "ir (watcher -- Aramaic for 'wakeful one' or 'watcher.' This is the ONLY passage in the canonical Bible that uses this term for angelic beings. The name suggests beings who never sleep, who are always watching -- cosmic sentinels in YHWH's heavenly court. The same term appears extensively in 1 Enoch, a Second Temple Jewish text not in the Protestant Bible but quoted in Jude 14-15, where the 'Watchers' are the rebellious angels who descended to Mount Hermon and mated with human women (Gen 6:1-4). Crucially, Daniel's Watchers are the FAITHFUL ones -- they serve YHWH's purposes, not rebel against them. The existence of both faithful and rebellious Watchers suggests a complex heavenly hierarchy where some members of the divine council fell from their posts while others remained loyal)",
            "qaddish (holy one -- Aramaic for 'holy one, set-apart one.' When paired with ir ('watcher') as in 4:13 ('a watcher, a holy one, came down from heaven'), these are two titles for the same category of being: divine council members who serve as YHWH's judicial agents. The fact that these beings issue a 'decree' (gezerat) and render a 'decision' (she'elta) shows they function as a heavenly court -- passing binding verdicts on earthly kings)",
            "gezerat irin (decree of the watchers -- divine council judicial language for a binding decision)",
            "she'elta (decision/request -- the verdict issued by the holy ones)",
            "Illaya (Most High -- the Aramaic equivalent of Hebrew Elyon. This title is critical: it means YHWH is not merely one god among many but the supreme authority over ALL spiritual beings. In the divine council framework (Deut 32:8-9; Ps 82), Elyon/Illaya is the God who presides over the assembly of gods, judges them (Ps 82:1), and can strip them of authority. When Daniel repeatedly says 'the Most High rules the kingdom of men' (4:17, 25, 32), the Aramaic word is Illaya -- the supreme cosmic ruler whose authority no earthly emperor can rival)",
            "MENE MENE TEKEL UPHARSIN (numbered, numbered, weighed, and divided -- these are Aramaic words that also happen to be the names of monetary weights: a mina, a mina, a shekel, and half-minas. The Babylonian wise men could probably READ the words but could not INTERPRET them because the meaning operates on multiple levels simultaneously. Daniel unpacks the wordplay: MENE (from menah, 'to number') means 'God has numbered your kingdom and finished it'; TEKEL (from teqal, 'to weigh') means 'you have been weighed on the scales and found too light'; PERES (from peras, 'to divide,' also a pun on Paras, 'Persia') means 'your kingdom has been divided and given to the Persians.' The brilliance is that each word works as both a monetary unit and a divine verdict)",
            "mo'znayya (balances/scales -- the instrument of divine judgment; 'weighed and found wanting')"
        ],

        "ane_backdrop": "The 'World Tree' motif of Daniel 4 has extensive ANE parallels. Mesopotamian "
                        "texts describe cosmic trees reaching to heaven (the huluppu tree in Gilgamesh, "
                        "the kiskanu tree in incantation texts). Ezekiel 31 uses the same imagery for "
                        "Assyria as a great cedar. The concept of a king's madness is also attested: the "
                        "'Prayer of Nabonidus' (4Q242), a Dead Sea Scroll fragment, describes Nabonidus "
                        "(Nebuchadnezzar's successor's predecessor) being afflicted with a disease for "
                        "seven years and healed by a Jewish exorcist. Some scholars see this as a parallel "
                        "tradition to Daniel 4. Belshazzar's feast in chapter 5 has been historically "
                        "confirmed: cuneiform texts identify Belshazzar (Bel-shar-usur) as the son of "
                        "Nabonidus who served as regent in Babylon while Nabonidus resided at Tayma in "
                        "Arabia. The handwriting on the wall -- divine communication through mysterious "
                        "writing -- has parallels in the Mesopotamian tradition of divine messages inscribed "
                        "on tablets of destiny (tuppi shimati) in the assembly of the gods.",

        "second_temple": [
            {
                "source": "4Q242 (Prayer of Nabonidus)",
                "summary": "A Qumran fragment describes King Nabonidus being afflicted with a disease "
                           "for seven years in Tayma, and a Jewish diviner ('a Jew from among the exiles') "
                           "ordering him to honor the Most High God.",
                "relevance": "This Dead Sea Scroll preserves a variant tradition about a Babylonian king's "
                             "humiliation and a Jewish sage's intervention -- possibly an earlier form of "
                             "the tradition that became Daniel 4."
            },
            {
                "source": "1 Enoch 1:5; 10:9, 15; 12:2-3",
                "summary": "The Watchers (irin) in 1 Enoch are rebellious divine beings who descend to "
                           "earth, mate with human women, and teach forbidden knowledge.",
                "relevance": "Daniel 4 and 1 Enoch share the term 'Watcher' (ir) for angelic beings, but "
                             "with opposite valences: Daniel's Watchers are faithful council members "
                             "executing YHWH's judgment; 1 Enoch's Watchers are rebels. Both traditions "
                             "attest to the same underlying divine council theology."
            }
        ],

        "cross_refs": [
            {"ref": "1 Enoch 6:1-8", "note": "The Watchers who descend from heaven -- the same term (ir/Watcher) as Daniel 4:13, but here referring to the rebellious ones", "type": "dss"},
            {"ref": "Ezekiel 31:3-14", "note": "Assyria as a great cedar that reached to heaven and was cut down -- the same world-tree imagery as Daniel 4", "type": "ot"},
            {"ref": "Psalm 75:7", "note": "'It is God who executes judgment, putting down one and lifting up another' -- the same sovereignty theology as 4:17", "type": "ot"},
            {"ref": "Proverbs 16:18", "note": "'Pride goes before destruction' -- the principle Nebuchadnezzar and Belshazzar illustrate", "type": "ot"},
            {"ref": "Luke 1:52", "note": "'He has brought down the mighty from their thrones and exalted those of humble estate' -- Mary's Magnificat echoing Daniel 4:17", "type": "nt"},
            {"ref": "Revelation 18:1-8", "note": "The fall of Babylon -- the pattern established by Belshazzar's fall in Daniel 5 repeated eschatologically", "type": "nt"},
            {"ref": "2 Chronicles 36:22-23", "note": "Cyrus's decree ending the exile -- the new kingdom that replaces Babylon after Daniel 5", "type": "ot"},
            {"ref": "Isaiah 14:12-15", "note": "'How you are fallen from heaven, O Day Star!' -- the same pride-and-fall pattern: Helel aspires to the divine mountain and is cast down, just as Nebuchadnezzar is humbled for his arrogance", "type": "ot"},
            {"ref": "Genesis 11:4", "note": "'Let us build a city and a tower with its top in the heavens' -- the Babel pattern of human ambition reaching toward the divine realm, repeated in Nebuchadnezzar's tree that 'reached to heaven'", "type": "ot"},
            {"ref": "Daniel 10:13, 20", "note": "The Prince of Persia and Prince of Greece -- territorial spirits governing the empires; the Watchers of ch. 4 operate within this same hierarchy of spiritual governance", "type": "ot"},
            {"ref": "1 Enoch 6-16", "note": "The Watchers (irin) who descend and the judgment pronounced upon them -- the Enochic tradition expands the Watcher terminology found here in Daniel 4", "type": "dss"},
            {"ref": "Acts 12:22-23", "note": "Herod accepts divine honors and 'an angel of the Lord struck him down' -- the same pattern as Nebuchadnezzar: a king who exalts himself is judged by a divine council agent", "type": "nt"}
        ],

        "divine_council_note": "Daniel 4:17 contains the most explicit divine council judicial language in "
                               "the canonical Bible outside of Psalm 82 and 1 Kings 22. The 'decree of the "
                               "watchers' (gezerat irin) and the 'decision of the holy ones' (she'elat "
                               "qaddishin) describe a formal legal proceeding in the heavenly court. The "
                               "Watchers (irin) and holy ones (qaddishin) are council members who have "
                               "examined the case of Nebuchadnezzar's pride and rendered a verdict: "
                               "humiliation until he acknowledges the Most High's sovereignty. This is the "
                               "ONLY passage in the canonical Bible that uses the word 'Watcher' (ir) for "
                               "angelic beings. In 1 Enoch, the term 'Watcher' (Aramaic ir; Greek "
                               "egrigoroi) designates both the faithful watchers who serve in heaven and "
                               "the rebellious watchers who descended to Mount Hermon. Daniel's Watchers "
                               "are clearly the faithful ones -- they execute YHWH's judgment, not rebel "
                               "against it. The terminology confirms that the 'Watcher' tradition in Second "
                               "Temple Judaism was not invented by the Enochic authors but reflects a "
                               "broader understanding of the angelic hierarchy. Daniel 5's handwriting on "
                               "the wall is also a divine council communication -- YHWH's verdict against "
                               "Belshazzar delivered through supernatural inscription, a parallel to the "
                               "Mesopotamian concept of divine decrees written on the tablets of destiny. "
                               "The words MENE MENE TEKEL UPHARSIN function as a divine court judgment: "
                               "the kingdom has been audited, the king has been found deficient, and the "
                               "sentence is division and transfer of power.",

        "sections": [
            {
                "heading": "Nebuchadnezzar's Tree Dream and the Watchers' Decree (Daniel 4)",
                "body": "Chapter 4 is structured as a royal proclamation: 'King Nebuchadnezzar to all "
                        "peoples, nations, and languages, that dwell in all the earth: Peace (shelam) "
                        "be multiplied to you! It has seemed good to me to show the signs (atin) and "
                        "wonders (temhayya) that the Most High God (Elaha Illaya) has done for me' "
                        "(4:1-2). The king recounts his dream: a tree of enormous height 'visible to "
                        "the end of the whole earth. Its leaves were beautiful and its fruit abundant, "
                        "and in it was food for all. The beasts of the field found shade under it, and "
                        "the birds of the heavens lived in its branches' (4:11-12). Then the verdict: "
                        "'I saw in the visions of my head as I lay in bed, and behold, an ir (watcher), "
                        "a qaddish (holy one), came down (nachit) from heaven (min-shemayya)' (4:13). "
                        "The Watcher's decree: 'Chop down the tree and lop off its branches... "
                        "Nevertheless, leave the stump (iqqar) of its roots in the earth, bound with a "
                        "band of iron and bronze' (4:14-15). The purpose: 'The sentence (pitgama) is by "
                        "the decree (gezerat) of the watchers (irin), the decision (she'elta) by the "
                        "word (me'amar) of the holy ones (qaddishin), to the end that the living may "
                        "know that the Most High (Illaya) rules (shallit) the kingdom of men and gives "
                        "it to whom he will and sets over it the lowliest of men' (4:17). Daniel "
                        "interprets: the tree is Nebuchadnezzar, and 'you shall be driven from among "
                        "men, and your dwelling shall be with the beasts of the field. You shall be made "
                        "to eat grass like an ox... till you know that the Most High rules the kingdom "
                        "of men' (4:25). Twelve months later, as Nebuchadnezzar boasts on the roof of "
                        "his palace -- 'Is not this great Babylon, which I have built by my mighty "
                        "power?' (4:30) -- a voice falls from heaven, and the sentence is executed. "
                        "His restoration comes through acknowledgment: 'I lifted my eyes to heaven, "
                        "and my reason (mand'i) returned to me, and I blessed the Most High (Illaya)' "
                        "(4:34)."
            },
            {
                "heading": "Belshazzar's Feast and the Writing on the Wall (Daniel 5)",
                "body": "'King Belshazzar made a great feast (lechem rav) for a thousand of his lords' "
                        "(5:1). The occasion is an act of deliberate sacrilege: 'Belshazzar, when he "
                        "tasted the wine, commanded that the vessels of gold and silver that "
                        "Nebuchadnezzar his father had taken out of the temple in Jerusalem be brought' "
                        "(5:2). The sacred vessels of YHWH's temple -- the instruments of the holy -- "
                        "are desecrated: 'They drank wine and praised the gods of gold and silver, "
                        "bronze, iron, wood, and stone' (5:4). The judgment is immediate: 'Immediately "
                        "the fingers (etsbe'an) of a human hand appeared and wrote on the plaster "
                        "(gira) of the wall of the king's palace, opposite the lampstand' (5:5). The "
                        "king's reaction is visceral: 'the king's color changed, and his thoughts "
                        "alarmed him; his limbs gave way (qitrei chartseh mishtarin), and his knees "
                        "knocked together' (5:6). No Babylonian wise man can read the writing. Daniel is "
                        "summoned and delivers a devastating indictment: 'You his son, Belshazzar, have "
                        "not humbled your heart, though you knew all this, but you have lifted up "
                        "yourself against the Lord of heaven (Mare shemayya)' (5:22-23). The "
                        "interpretation: MENE (mena) -- 'God has numbered (menah) your kingdom and "
                        "finished it (hashlimah).' TEKEL (teqel) -- 'you have been weighed (teqilta) "
                        "in the balances (mo'znayya) and found wanting (chasiyr).' PERES (peres) -- "
                        "'your kingdom has been divided (perisat) and given to the Medes (Maday) and "
                        "Persians (Paras)' (5:26-28). 'That very night Belshazzar the Chaldean king "
                        "was killed' (5:30). The historical fall of Babylon to Cyrus in 539 BC -- "
                        "confirmed by the Nabonidus Chronicle and the Cyrus Cylinder -- fulfills the "
                        "divine court's sentence."
            }
        ]
    },

    {
        "id": "dan-6",
        "ref": "Daniel 6",
        "chapter_num": 4,
        "title": "Daniel in the Lions' Den: The Angel Shuts Their Mouths",
        "era": "daniel_court",
        "type": "chapter",
        "themes": ["DC", "KING"],

        "synopsis": "Under the new Persian administration of 'Darius the Mede,' Daniel's excellence "
                    "provokes jealousy among the other officials. They plot to destroy him by targeting "
                    "his religious practice -- the one area where Daniel will not compromise. They "
                    "persuade Darius to sign an irrevocable decree: 'whoever makes petition (ba'u) to "
                    "any god or man for thirty days, except to you, O king, shall be cast into the den "
                    "of lions (gob aryawata)' (6:7). Daniel, knowing the decree is signed, 'went to his "
                    "house where he had windows in his upper chamber open toward Jerusalem. He got down on "
                    "his knees three times a day and prayed and gave thanks before his God, as he had done "
                    "previously' (6:10). The detail 'as he had done previously' (kol-qovel di hava "
                    "aved min-qadmat denah) is critical: Daniel does not make a public spectacle of "
                    "defiance; he simply continues his lifelong practice. When reported, Darius is "
                    "distressed and tries to save Daniel, but the 'law of the Medes and Persians' (dat "
                    "Maday uPhras) cannot be revoked (6:15). Daniel is thrown into the lions' den. "
                    "Darius fasts all night and rushes to the den at dawn: 'O Daniel, servant of the "
                    "living God (eved Elaha chayya), has your God, whom you serve continually (bi-tedar), "
                    "been able to deliver you from the lions?' (6:20). Daniel's answer: 'My God sent "
                    "(shelach) his angel (mal'akeh), and he shut (segar) the lions' mouths (pum "
                    "aryawata), and they have not harmed me' (6:22). The angel (mal'akh) is a divine "
                    "council operative -- sent by YHWH to execute a specific protective mission. Daniel's "
                    "accusers are thrown into the den with their families, and the lions overpower them "
                    "before they reach the bottom. Darius issues a decree honoring Daniel's God: 'He is "
                    "the living God (Elaha chayya), enduring forever (qayyam le-almeyn); his kingdom "
                    "(malkuteh) shall never be destroyed, and his dominion (sholtaneh) shall be to the "
                    "end' (6:26).",

        "key_verse": {
            "ref": "Daniel 6:22",
            "text": "My God sent his angel and shut the lions' mouths, and they have not harmed me, because I was found blameless before him; and also before you, O king, I have done no harm.",
            "translation": "ESV"
        },

        "original_terms": [
            "mal'akh (angel/messenger -- the divine council operative sent to shut the lions' mouths)",
            "gob aryawata (den of lions -- the instrument of execution under Persian law)",
            "dat Maday uPhras (law of the Medes and Persians -- the irrevocable legal principle that traps even the king)",
            "Elaha chayya (the living God -- the Aramaic title distinguishing YHWH from ALL other deities. In the ANE worldview, gods were typically represented by statues made of wood, stone, or metal. These idols had to be fed, clothed, and carried in procession by their worshippers (see Isa 46:1-7 for YHWH&rsquo;s mockery of this). By calling YHWH the 'living God,' the text emphasizes that YHWH is not an inert object but a being who speaks, acts, sends agents, rescues, and endures forever. Remarkably, this title is spoken by a pagan king, Darius, who has witnessed YHWH&rsquo;s power firsthand in the lions&rsquo; den)",
            "bi-tedar (continually -- Daniel's uninterrupted pattern of faithful prayer)",
            "qayyam le-almeyn (enduring forever -- the eternal nature of YHWH's kingdom)",
            "shelach (sent -- the divine commissioning of the angel for a specific protective mission)"
        ],

        "ane_backdrop": "Lions were a powerful symbol in ANE culture. Assyrian kings hunted lions as a "
                        "demonstration of royal power (the lion hunt reliefs from Ashurbanipal's palace "
                        "at Nineveh are among the finest in ANE art). Lions also served as guardians at "
                        "temple and palace entrances -- the lamassu (winged bull with human head) and "
                        "other composite creatures. Execution by wild animals is attested in Persian "
                        "sources, though the specific practice of a 'lions' den' is debated. The concept "
                        "of an irrevocable royal decree (dat) is consistent with what we know of Persian "
                        "administrative practice -- Esther 1:19 and 8:8 describe the same legal principle. "
                        "Daniel's practice of praying toward Jerusalem (6:10) reflects the Solomonic "
                        "dedication prayer of 1 Kings 8:48-49, where Solomon asks YHWH to hear the "
                        "prayers of exiles who pray 'toward their land.' The three-times-daily prayer "
                        "became standard Jewish practice (shacharit, minchah, ma'ariv), possibly "
                        "influenced by this Danielic precedent (cf. Psalm 55:17).",

        "second_temple": [
            {
                "source": "Hebrews 11:33",
                "summary": "'Who through faith... stopped the mouths of lions.'",
                "relevance": "The author of Hebrews lists Daniel's deliverance among the triumphs of "
                             "faith, using the specific language of 'stopping lions' mouths.'"
            },
            {
                "source": "1 Maccabees 2:60",
                "summary": "Mattathias exhorts his sons: 'Daniel, because of his innocence, was "
                           "delivered from the mouth of the lions.'",
                "relevance": "The Maccabean resistance cited Daniel in the lions' den as encouragement "
                             "for Jews facing persecution under Antiochus IV Epiphanes."
            },
            {
                "source": "Bel and the Dragon (LXX/Theodotion addition)",
                "summary": "An expanded version of Daniel in the lions' den where Daniel spends six "
                           "days among the lions and is fed by the prophet Habakkuk, transported "
                           "miraculously by an angel.",
                "relevance": "Though deuterocanonical, this addition shows how the Second Temple "
                             "tradition developed the lions' den narrative with additional angelic "
                             "intervention motifs."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 8:48-49", "note": "Solomon's prayer that YHWH hear the exiles who pray toward Jerusalem -- the practice Daniel follows in 6:10", "type": "ot"},
            {"ref": "Psalm 55:17", "note": "'Evening and morning and at noon I utter my complaint and moan, and he hears my voice' -- three-times-daily prayer, like Daniel", "type": "ot"},
            {"ref": "Hebrews 11:33", "note": "'Who through faith stopped the mouths of lions' -- Daniel's deliverance in the catalog of faith", "type": "nt"},
            {"ref": "2 Timothy 4:17", "note": "'The Lord stood by me and strengthened me... so I was rescued from the lion's mouth' -- Paul echoing Daniel's experience", "type": "nt"},
            {"ref": "1 Peter 5:8", "note": "'Your adversary the devil prowls around like a roaring lion' -- the spiritual reality behind the physical lions", "type": "nt"},
            {"ref": "Psalm 34:7", "note": "'The angel of YHWH encamps around those who fear him and delivers them' -- the principle behind the angel in the lions' den", "type": "ot"},
            {"ref": "Esther 1:19; 8:8", "note": "The irrevocable law of the Medes and Persians -- the same legal framework as Daniel 6:15", "type": "ot"}
        ],

        "divine_council_note": "The angel (mal'akh) who shuts the lions' mouths in 6:22 is a divine "
                               "council operative carrying out a specific commission from YHWH. The verb "
                               "shelach ('sent') indicates formal commissioning -- YHWH dispatches a "
                               "council member to protect his servant. This is the same pattern as the "
                               "bar elahin in the furnace (chapter 3) and the Watchers who decree "
                               "Nebuchadnezzar's humiliation (chapter 4). Throughout the court tales, the "
                               "divine council is consistently active: sending agents, issuing decrees, "
                               "writing on walls, and shutting lions' mouths. The cumulative theology of "
                               "Daniel 1-6 is that YHWH's council governs all empires -- Babylon under "
                               "Nebuchadnezzar and Belshazzar, Medo-Persia under Darius -- and YHWH's "
                               "faithful servants are protected by council members who intervene in the "
                               "physical world. Darius's confession -- 'He is the living God (Elaha "
                               "chayya), enduring forever; his kingdom shall never be destroyed' (6:26) -- "
                               "echoes the theology of Daniel 2:44 and anticipates the Son of Man's "
                               "everlasting dominion in 7:14. The pagan kings of Daniel 1-6 are "
                               "progressively brought to acknowledge what the divine council has always "
                               "known: YHWH alone is the Most High (Illaya), and his kingdom alone "
                               "is eternal.",

        "sections": [
            {
                "heading": "The Plot Against Daniel: Targeting His Prayer Life (6:1-9)",
                "body": "Under the Persian reorganization, Daniel is appointed as one of three presidents "
                        "(sarkin) over 120 satraps (6:1-2). His excellence provokes jealousy: 'The "
                        "presidents and the satraps sought to find a ground for complaint (illah) against "
                        "Daniel with regard to the kingdom, but they could find no ground for complaint "
                        "or any fault (shechitah), because he was faithful (meheyman), and no error or "
                        "fault was found in him' (6:4). The word meheyman ('faithful, trustworthy') is "
                        "the Aramaic cognate of Hebrew ne'eman -- the covenant faithfulness term. Unable "
                        "to find professional misconduct, the conspirators target Daniel's religious "
                        "practice: 'We shall not find any ground for complaint against this Daniel unless "
                        "we find it in connection with the law of his God (dat elaheh)' (6:5). They "
                        "persuade Darius to sign a decree that 'whoever makes petition (ba'u) to any "
                        "god or man for thirty days, except to you, O king, shall be cast into the den "
                        "of lions' (6:7). The decree conflates religious devotion with political loyalty "
                        "-- the same totalitarian demand that characterized the golden image in chapter 3. "
                        "Darius signs, and the decree becomes irrevocable under the dat Maday uPhras "
                        "('law of the Medes and Persians')."
            },
            {
                "heading": "Daniel's Unbroken Practice and the Night in the Den (6:10-18)",
                "body": "'When Daniel knew that the document had been signed, he went to his house' "
                        "(6:10a). Daniel's response to the decree is not defiance for its own sake but "
                        "the continuation of a lifelong practice. He goes to 'his upper chamber where "
                        "he had windows open toward Jerusalem (neghed Yerushalem)' (6:10b). The windows "
                        "facing Jerusalem connect Daniel's prayer to Solomon's dedication prayer (1 Kings "
                        "8:48-49): even in exile, the faithful pray toward the place where YHWH's name "
                        "dwells. 'He got down on his knees three times a day (zimnin telatah beyoma) "
                        "and prayed (metsalle) and gave thanks (mode) before his God, as he had done "
                        "previously (kol-qovel di hava aved min-qadmat denah)' (6:10c). The phrase "
                        "'as he had done previously' is the critical detail: Daniel does not escalate "
                        "or dramatize. He simply refuses to stop what he has always done. The conspirators "
                        "report him, and Darius 'was much distressed (be'esh alahi saggi) and set his "
                        "mind to deliver Daniel' (6:14). When the law proves inescapable, Darius says to "
                        "Daniel: 'May your God, whom you serve continually (bi-tedar), deliver you!' "
                        "(6:16). The king spends the night fasting, unable to sleep (6:18) -- a remarkable "
                        "portrait of a pagan king who has come to hope in Daniel's God."
            },
            {
                "heading": "The Angel, the Deliverance, and the Pagan King's Confession (6:19-28)",
                "body": "At dawn, Darius 'went in haste (bithval) to the den of lions' and cried out 'in "
                        "a tone of anguish (qal atsiv)': 'O Daniel, servant of the living God (eved "
                        "Elaha chayya), has your God, whom you serve continually, been able (hayakhil) "
                        "to deliver you from the lions?' (6:19-20). The title 'living God' (Elaha chayya) "
                        "is the decisive contrast with the dead idols of Babylon. Daniel answers: 'O "
                        "king, live forever (le-olmeyn chey'i)! My God sent (shelach) his angel "
                        "(mal'akeh), and he shut (segar) the lions' mouths (pum aryawata), and they "
                        "have not harmed me, because I was found blameless (zakku) before him; and also "
                        "before you, O king, I have done no harm (chavalah)' (6:21-22). The angel is "
                        "a divine council member sent on a specific mission -- the verb shelach "
                        "('sent') indicates formal commissioning. Daniel's innocence is established on "
                        "two levels: before God (zakku, 'blameless/pure') and before the king (no "
                        "chavalah, 'harm/wrong'). Daniel is lifted from the den 'and no harm (chaval) "
                        "was found on him, because he had trusted (heymin) in his God' (6:23). The "
                        "verb heymin ('to trust, believe') is the Aramaic cognate of Hebrew he'emin -- "
                        "the root of 'amen' and 'faith.' Darius's decree provides the theological "
                        "summary of the entire court tales section: 'For he is the living God (Elaha "
                        "chayya), enduring forever (qayyam le-almeyn); his kingdom (malkuteh) shall "
                        "never be destroyed (la tithhabbal), and his dominion (sholtaneh) shall be to "
                        "the end (ad-sofah). He delivers (mesheziv) and rescues (matsil); he works signs "
                        "(atin) and wonders (temhin) in heaven and on earth' (6:26-27). The pagan king "
                        "confesses what the divine council has always proclaimed: YHWH alone is eternal, "
                        "his kingdom alone is indestructible, and his power operates across the entire "
                        "cosmos."
            }
        ]
    }
]
