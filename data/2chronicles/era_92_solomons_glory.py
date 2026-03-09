"""
era_92_solomons_glory.py -- Solomon's Glory (2 Chronicles 1-9)

The Chronicler's portrait of Solomon focuses almost exclusively on the temple:
its construction, dedication, and the divine response. Solomon's wisdom request
(ch. 1), the temple building (chs. 2-4), the dedication ceremony where YHWH's
glory fills the house (chs. 5-7), and the Queen of Sheba's visit (ch. 9) form
a unified narrative of temple theology at its peak. The Chronicler omits
Solomon's apostasy (1 Kings 11) -- not because he is unaware of it but because
his portrait of Solomon is typological: Solomon as temple-builder is the model
for the ideal king, the son of David who builds God's house.
"""

CHAPTERS = [
    {
        "id": "2chr-1-4",
        "ref": "2 Chronicles 1-4",
        "chapter_num": 1,
        "title": "Solomon's Wisdom and the Temple Construction",
        "era": "solomons_glory",
        "type": "chapter",

        "synopsis": "Solomon's reign begins at Gibeon, where the tabernacle of Moses still stands. "
                    "God appears to Solomon in a dream: 'Ask what I shall give you' (1:7). Solomon "
                    "requests wisdom (chokmah) and knowledge (madda) to govern the people -- and God "
                    "grants both, along with riches and honor (1:11-12). Chapters 2-4 detail the "
                    "temple construction with meticulous attention to materials, dimensions, and "
                    "furnishings. The Chronicler includes Solomon's correspondence with Huram (Hiram) "
                    "of Tyre, the skilled craftsman Huram-abi, and the massive workforce. The bronze "
                    "pillars (Jachin and Boaz), the bronze sea, the golden altar, the lampstands, the "
                    "tables -- every detail is recorded because every detail is theologically significant. "
                    "The temple is not merely a building but a microcosm of creation, a heaven-earth "
                    "meeting point, the visible sign of YHWH's invisible presence.",

        "key_verse": {
            "ref": "2 Chronicles 2:6",
            "text": "But who is able to build him a house, since heaven, even highest heaven, cannot contain him? Who am I to build a house for him, except as a place to make offerings before him?",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "chokmah (wisdom -- Solomon's defining gift; not mere intelligence but the skill to rule justly and build rightly)",
            "bayit YHWH (house of YHWH -- the temple; God's earthly dwelling place, mirror of his heavenly throne room)",
            "devir (inner sanctuary/Holy of Holies -- the most sacred space, where the Ark of the Covenant rests between the cherubim)",
            "Yakin u-Boaz (He establishes / In him is strength -- the names of the two bronze pillars; possibly declarations of YHWH's power)"
        ],

        "ane_backdrop": "Solomon's temple follows the general plan of ANE temple architecture: a "
                        "tripartite structure (porch/ulam, main hall/hekal, inner room/devir) found in "
                        "temples at 'Ain Dara (Syria), Tell Tayinat, and Hazor. The dimensions and "
                        "proportions are consistent with Late Bronze/Early Iron Age temple design in the "
                        "Levant. The freestanding pillars (Jachin and Boaz) have parallels at 'Ain Dara "
                        "and in Egyptian temple architecture. The bronze sea (4:2-5) parallels the Apsu "
                        "(cosmic waters) in Mesopotamian temples -- the primordial sea tamed and contained "
                        "by divine power. Temple building accounts from Mesopotamia (Gudea Cylinders) and "
                        "Egypt (Karnak inscriptions) follow a similar pattern: divine commission, material "
                        "preparation, construction, dedication, divine approval. The Chronicler's account "
                        "follows this template because the theology is the same across the ANE: the god "
                        "must authorize, approve, and inhabit his house.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 8.61-98",
                "summary": "Josephus provides detailed descriptions of Solomon's temple, drawing on "
                           "both biblical accounts and additional traditions. He emphasizes the temple's "
                           "magnificence as a wonder of the ancient world.",
                "relevance": "Shows how the Second Temple community remembered and idealized Solomon's "
                             "temple as the benchmark against which the Second Temple was measured."
            },
            {
                "source": "Wisdom of Solomon 9:8",
                "summary": "'You have given command to build a temple on your holy mountain, and an "
                           "altar in the city of your habitation, a copy of the holy tent which you "
                           "prepared from the beginning.'",
                "relevance": "Explicitly identifies Solomon's temple as a 'copy' (mimema) of a heavenly "
                             "archetype -- the same tavnit/pattern theology as 1 Chronicles 28."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 3:5-14", "note": "The parallel account of Solomon's wisdom request -- the Chronicler abbreviates the dream but preserves the core exchange", "type": "ot"},
            {"ref": "1 Kings 5-7", "note": "The parallel temple construction account in Kings, with additional structural details", "type": "ot"},
            {"ref": "Exodus 25-31", "note": "The tabernacle instructions -- Solomon's temple is the permanent version of Moses' portable sanctuary", "type": "ot"},
            {"ref": "1 Chronicles 28:11-19", "note": "David's transmission of the temple plan received 'by the Spirit' -- the blueprint Solomon executes", "type": "ot"},
            {"ref": "John 2:19-21", "note": "Jesus: 'Destroy this temple, and in three days I will raise it up' -- 'he was speaking about the temple of his body'; the true temple Solomon's pointed toward", "type": "nt"},
            {"ref": "Ephesians 2:20-22", "note": "The church as God's temple -- the fulfillment of what Solomon built in stone", "type": "nt"}
        ],

        "divine_council_note": "Solomon's temple is the earthly counterpart to YHWH's heavenly throne "
                               "room. The Holy of Holies, with its two massive cherubim whose wings span "
                               "the entire room (3:10-13), replicates the divine council throne described "
                               "in Ezekiel 1 and 10. The cherubim are not decorative but functional: they "
                               "are throne-guardians, divine council beings whose presence marks the space "
                               "as YHWH's throne room. Solomon's own confession -- 'Heaven, even highest "
                               "heaven, cannot contain him' (2:6) -- acknowledges that the temple is not "
                               "God's prison but his chosen meeting point. The God who presides over the "
                               "council of all spiritual beings condescends to dwell in a house built by "
                               "human hands -- a staggering act of divine humility.",

        "sections": [
            {
                "heading": "Solomon's Wisdom Request at Gibeon (2 Chr 1:1-17)",
                "body": "Solomon goes to Gibeon, where the tabernacle of Moses and the bronze altar of "
                        "Bezalel stand (1:3-5). The Ark, however, is in Jerusalem (David moved it there). "
                        "This split between the tabernacle (at Gibeon) and the Ark (in Jerusalem) is the "
                        "architectural problem the temple will solve. At Gibeon, God appears: 'Ask what I "
                        "shall give you' (1:7). Solomon's request is for 'wisdom and knowledge' (chokmah "
                        "umadda) to govern 'this people' (1:10). God's response is lavish: because Solomon "
                        "did not ask for riches, possessions, honor, long life, or the death of enemies, "
                        "God grants wisdom AND all the rest (1:11-12). The Chronicler then notes Solomon's "
                        "wealth: 1,400 chariots, 12,000 horsemen, silver 'as common as stone in Jerusalem, "
                        "and cedar as plentiful as the sycamore of the Shephelah' (1:15). This abundance "
                        "foreshadows the temple: God's chosen king lacks nothing for the task ahead."
            },
            {
                "heading": "Correspondence with Huram of Tyre (2 Chr 2:1-18)",
                "body": "Solomon's letter to Huram (Hiram) of Tyre reveals profound theology in the context "
                        "of diplomatic correspondence. Solomon states his purpose: 'I am about to build a "
                        "house for the name of the LORD my God' (2:4). Then comes the stunning admission: "
                        "'But who is able to build him a house, since heaven, even highest heaven, cannot "
                        "contain him? Who am I to build a house for him, except as a place to make offerings "
                        "before him?' (2:6). Solomon knows the temple cannot 'contain' God -- it is a place "
                        "of meeting, sacrifice, and worship, not a divine prison. Huram's response is equally "
                        "theological: 'Because the LORD loves his people, he has made you king over them' "
                        "(2:11). Even a pagan king recognizes that Israel's king rules by YHWH's love."
            },
            {
                "heading": "The Temple Rises on Mount Moriah (2 Chr 3:1-4:22)",
                "body": "The Chronicler provides the crucial geographical identification absent from Kings: "
                        "'Solomon began to build the house of the LORD in Jerusalem on Mount Moriah, where "
                        "the LORD had appeared to David his father, at the place that David had appointed, on "
                        "the threshing floor of Ornan the Jebusite' (3:1). Mount Moriah is where Abraham was "
                        "told to sacrifice Isaac (Gen 22:2). The Chronicler connects three foundational events "
                        "at one site: Abraham's near-sacrifice, David's altar after the census (1 Chr 21), and "
                        "Solomon's temple. The temple's architecture is described in detail: 60 cubits long, "
                        "20 cubits wide, the vestibule rising 120 cubits high (3:3-4; the height is unique to "
                        "Chronicles and debated). The two great cherubim in the Holy of Holies each have a "
                        "15-foot wingspan, together spanning the entire 20-cubit width of the room (3:11-13). "
                        "Their wings touch wall and wall, creating a throne canopy over the Ark. The bronze "
                        "sea (4:2-5) -- 15 feet in diameter, held by twelve oxen facing outward in groups of "
                        "three -- represents the cosmic waters subdued by YHWH, the creator who rules over chaos."
            }
        ]
    },

    {
        "id": "2chr-5-7",
        "ref": "2 Chronicles 5-7",
        "chapter_num": 2,
        "title": "The Glory Fills the Temple: YHWH Comes Home",
        "era": "solomons_glory",
        "type": "chapter",

        "synopsis": "The dedication of Solomon's temple is the theological climax of the entire "
                    "Chronicler's history. The Ark is brought into the Holy of Holies (ch. 5). "
                    "The Levitical musicians and 120 priests with trumpets unite in praising YHWH -- "
                    "'and when the song was raised... the house of the LORD was filled with a cloud, "
                    "so that the priests could not stand to minister because of the cloud, for the "
                    "glory (kavod) of the LORD filled the house of God' (5:13-14). YHWH has come home. "
                    "Solomon delivers his dedication prayer (ch. 6), and fire falls from heaven to "
                    "consume the offerings (7:1). Then comes YHWH's response to Solomon at night -- "
                    "including the famous covenant promise of 7:14: 'If my people who are called by my "
                    "name humble themselves, and pray and seek my face and turn from their wicked ways, "
                    "then I will hear from heaven and will forgive their sin and heal their land.'",

        "key_verse": {
            "ref": "2 Chronicles 7:14",
            "text": "If my people who are called by my name humble themselves, and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive their sin and heal their land.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "kavod (glory -- the visible manifestation of YHWH's presence; the cloud that fills the temple is the same kavod that led Israel through the wilderness and descended on Sinai)",
            "anan (cloud -- the vehicle of divine presence; when the cloud fills the temple, heaven has descended to earth)",
            "esh min-hashamayim (fire from heaven -- divine acceptance of Solomon's offerings, as with the tabernacle dedication in Lev 9:24 and Elijah's sacrifice in 1 Kgs 18:38)",
            "kanaf (to humble oneself -- the required posture for covenant renewal; literally 'to make low,' the opposite of human pride)",
            "darash (to seek -- the Chronicler's key verb for faithfulness; 'seek my face' is the pathway to covenant restoration)"
        ],

        "ane_backdrop": "Temple dedication ceremonies in the ancient Near East followed a common pattern: "
                        "the deity's image (or in Israel's case, the Ark) is installed in the inner "
                        "sanctuary, sacrifices are offered, and a sign confirms the god's acceptance. "
                        "The Gudea Cylinders describe how Ningirsu 'entered his house' after the temple "
                        "was built and the dedication sacrifices were offered. Egyptian temple inscriptions "
                        "at Karnak describe the Opet Festival, where Amun's presence 'fills' his temple "
                        "during the dedication. The fire from heaven in 2 Chr 7:1 parallels the divine fire "
                        "that consumed offerings in other temple dedications -- it is the universal sign "
                        "that the deity has accepted the house built for him. The Chronicler adds details "
                        "not in Kings: the 120 priests with trumpets, the Levitical musicians, and the "
                        "specific notation that worship preceded and accompanied the theophany.",

        "second_temple": [
            {
                "source": "Ezekiel 43:1-5",
                "summary": "Ezekiel's vision of the glory of YHWH returning to the eschatological "
                           "temple: 'The glory of the LORD entered the temple by the gate facing east... "
                           "and the glory of the LORD filled the temple.'",
                "relevance": "Ezekiel envisions the same kavod that filled Solomon's temple returning to a "
                             "future temple -- suggesting that YHWH's glory departed at the exile (Ezek 10-11) "
                             "and will return. The Second Temple community awaited this return."
            },
            {
                "source": "Sirach (Ben Sira) 50:1-21",
                "summary": "Ben Sira describes the Second Temple high priest Simon II performing the "
                           "Day of Atonement ritual, with the congregation falling in worship -- an "
                           "echo of the Solomon dedication scene.",
                "relevance": "The Second Temple liturgy was modeled on the Solomonic dedication pattern, "
                             "maintaining continuity with the Chronicler's ideal."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 8:1-66", "note": "The parallel dedication account in Kings -- Chronicles adds the fire from heaven (7:1) and the Levitical musicians (5:12-13)", "type": "ot"},
            {"ref": "Exodus 40:34-35", "note": "The glory of YHWH filling the tabernacle: 'Moses was not able to enter the tent of meeting because the cloud settled on it' -- exact parallel to 2 Chr 5:14", "type": "ot"},
            {"ref": "Leviticus 9:23-24", "note": "Fire from YHWH consuming the inaugural offerings at the tabernacle dedication -- the same sign as 2 Chr 7:1", "type": "ot"},
            {"ref": "Isaiah 6:1-4", "note": "Isaiah sees YHWH's glory filling the temple, with seraphim crying 'Holy, holy, holy' -- the heavenly reality behind the earthly kavod", "type": "ot"},
            {"ref": "Ezekiel 10:18-19; 11:22-23", "note": "The glory of YHWH departing from Solomon's temple before the exile -- the devastating reversal of 2 Chr 5:13-14", "type": "ot"},
            {"ref": "Revelation 21:22-23", "note": "The new Jerusalem has no temple 'for its temple is the Lord God the Almighty and the Lamb... and the glory of God gives it light' -- the ultimate fulfillment of what Solomon's temple foreshadowed", "type": "nt"}
        ],

        "divine_council_note": "The theophany at the temple dedication is a divine council event. The kavod "
                               "(glory) that fills the temple is YHWH's visible presence descending from the "
                               "heavenly council chamber to inhabit the earthly sanctuary. The cloud (anan) "
                               "is the same vehicle of divine presence that appeared at Sinai (Exod 24:15-18), "
                               "led Israel through the wilderness (Exod 13:21-22), and filled the tabernacle "
                               "(Exod 40:34-35). When the cloud fills Solomon's temple 'so that the priests "
                               "could not stand to minister' (5:14), the boundary between heaven and earth "
                               "has collapsed -- the divine council's presence has invaded the human realm. "
                               "The fire from heaven (7:1) is the council's seal of approval. YHWH's nighttime "
                               "promise to Solomon -- 'I have chosen and consecrated this house that my name "
                               "may be there forever. My eyes and my heart will be there for all time' (7:16) -- "
                               "means the divine council has established a permanent embassy in the human world.",

        "sections": [
            {
                "heading": "The Ark Enters the Holy of Holies (2 Chr 5:1-14)",
                "body": "Solomon assembles all Israel for the Feast of Tabernacles (the seventh month) to "
                        "bring the Ark into the completed temple. The priests carry the Ark and the tent of "
                        "meeting with all its furnishings into the Holy of Holies, 'underneath the wings of "
                        "the cherubim' (5:7). Then comes the Chronicler's unique addition: the Levitical "
                        "musicians -- 'Asaph, Heman, and Jeduthun, with their sons and kinsmen, arrayed in "
                        "fine linen, with cymbals, harps, and lyres, stood east of the altar with 120 priests "
                        "who were trumpeters' (5:12). When they 'were as one' (ke-echad) in praising YHWH -- "
                        "when the music, the singing, and the trumpets unified in a single voice -- 'the house "
                        "of the LORD was filled with a cloud' (5:13). The Chronicler's addition of the "
                        "musicians reveals his theology: worship is the condition for divine presence. The "
                        "kavod descends not merely because the building is complete but because the praise is "
                        "offered. The content of their worship is recorded: 'For he is good, for his steadfast "
                        "love endures forever' (5:13) -- the foundational confession of Israel's faith."
            },
            {
                "heading": "Solomon's Dedication Prayer (2 Chr 6:1-42)",
                "body": "Solomon's prayer is a theological masterpiece. He begins by acknowledging the paradox: "
                        "'But will God indeed dwell with man on the earth? Behold, heaven and the highest "
                        "heaven cannot contain you, how much less this house that I have built!' (6:18). The "
                        "prayer envisions seven scenarios where Israel will come to the temple in need: "
                        "disputes (6:22-23), military defeat (6:24-25), drought (6:26-27), famine and plague "
                        "(6:28-31), foreigners seeking YHWH (6:32-33), war (6:34-35), and exile (6:36-39). "
                        "In each case, Solomon asks God to hear 'from heaven your dwelling place' (6:21, 30, "
                        "33, 39). The phrase is crucial: God's actual dwelling is in heaven; the temple is the "
                        "point of contact, not the totality of God's residence. The prayer's climax addresses "
                        "exile -- the very situation the Chronicler's audience was recovering from: 'If they "
                        "repent... and pray toward this land that you gave to their fathers, the city that you "
                        "have chosen, and the house that I have built for your name, then hear from heaven "
                        "your dwelling place their prayer and their pleas' (6:37-39)."
            },
            {
                "heading": "Fire from Heaven and the Divine Response (2 Chr 7:1-22)",
                "body": "Immediately after Solomon's prayer, 'fire came down from heaven and consumed the "
                        "burnt offering and the sacrifices, and the glory of the LORD filled the temple' (7:1). "
                        "This fire from heaven is unique to the Chronicler -- 1 Kings does not record it. It "
                        "parallels the fire that fell at the tabernacle dedication (Lev 9:24) and at Elijah's "
                        "altar on Carmel (1 Kgs 18:38), establishing Solomon's temple in continuity with both. "
                        "'All the people of Israel saw the fire come down and the glory of the LORD on the "
                        "temple, and they bowed down with their faces to the ground on the pavement and "
                        "worshiped' (7:3). YHWH then appears to Solomon at night with the covenant promise "
                        "and warning that defines the rest of 2 Chronicles: 7:14 -- 'If my people who are "
                        "called by my name humble themselves, and pray and seek my face and turn from their "
                        "wicked ways, then I will hear from heaven and will forgive their sin and heal their "
                        "land.' But the warning follows: 'If you turn aside and forsake my statutes... and "
                        "serve other gods and worship them, then I will pluck you up from my land... and "
                        "this house... will become a heap of ruins' (7:19-21). The rest of 2 Chronicles "
                        "narrates the outworking of this conditional promise."
            }
        ]
    },

    {
        "id": "2chr-8-9",
        "ref": "2 Chronicles 8-9",
        "chapter_num": 3,
        "title": "Solomon's Reign and the Queen of Sheba: Wisdom Recognized",
        "era": "solomons_glory",
        "type": "chapter",

        "synopsis": "Chapters 8-9 round out the Chronicler's portrait of Solomon's glory. Chapter 8 "
                    "surveys Solomon's building projects, his administration of forced labor, and his "
                    "establishment of regular worship at the temple according to 'the rule of Moses' "
                    "and 'the direction of David his father' (8:13-14). Chapter 9 narrates the visit "
                    "of the Queen of Sheba, who comes to test Solomon's wisdom with 'hard questions' "
                    "(9:1). She declares: 'The report was true that I heard in my own land of your "
                    "words and of your wisdom... Behold, the half of the greatness of your wisdom was "
                    "not told me; you surpass the report that I heard' (9:5-6). The chapter catalogs "
                    "Solomon's wealth in staggering terms. The Chronicler concludes Solomon's reign "
                    "without mentioning his apostasy (1 Kings 11): no foreign wives, no worship of "
                    "Ashtoreth, Chemosh, or Molech. This omission is deliberate -- Solomon in "
                    "Chronicles is the ideal temple-builder, not a cautionary tale.",

        "key_verse": {
            "ref": "2 Chronicles 9:8",
            "text": "Blessed be the LORD your God, who has delighted in you and set you on his throne as king for the LORD your God! Because your God loved Israel and would establish them forever, he has made you king over them, that you may execute justice and righteousness.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "chidot (riddles/hard questions -- the Queen of Sheba tests Solomon with complex problems; the same term for Samson's riddle in Judges 14)",
            "mishpat u-tsedaqah (justice and righteousness -- the Queen recognizes Solomon's purpose: not personal glory but just governance)",
            "kisse YHWH (throne of YHWH -- the Queen says Solomon sits 'on his throne as king for the LORD your God'; the Davidic throne is YHWH's own throne)"
        ],

        "ane_backdrop": "The Queen of Sheba's visit fits the pattern of ANE royal diplomatic visits. "
                        "Sheba (Saba) was located in southwest Arabia (modern Yemen/Ethiopia), controlling "
                        "the lucrative incense trade route. Arabian queens are attested in Assyrian "
                        "inscriptions: Tiglath-Pileser III records tribute from 'Samsi, queen of the "
                        "Arabs.' The visit combines trade negotiation with wisdom competition -- both "
                        "common in ANE royal encounters. The lavish gift exchange (120 talents of gold, "
                        "spices, and precious stones from Sheba; 'all that she desired' from Solomon) "
                        "follows the conventions of royal diplomacy.",

        "second_temple": [
            {
                "source": "Matthew 12:42 (Luke 11:31)",
                "summary": "Jesus declares: 'The queen of the South will rise up at the judgment "
                           "with this generation and condemn it, for she came from the ends of the "
                           "earth to hear the wisdom of Solomon, and behold, something greater than "
                           "Solomon is here.'",
                "relevance": "Jesus identifies himself as greater than Solomon -- the ultimate "
                             "fulfillment of the wisdom and glory the Chronicler ascribes to Solomon."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 10:1-13", "note": "The parallel account of the Queen of Sheba's visit -- substantially identical in both accounts", "type": "ot"},
            {"ref": "1 Kings 11:1-13", "note": "Solomon's apostasy -- the material the Chronicler deliberately OMITS to maintain his typological portrait", "type": "ot"},
            {"ref": "Matthew 12:42", "note": "Jesus declares 'something greater than Solomon is here' -- the true temple-builder who supersedes Solomon's glory", "type": "nt"},
            {"ref": "Psalm 72:1-19", "note": "'A Psalm of Solomon' -- the ideal king whose rule brings justice, peace, and international tribute; the vision 2 Chr 9 partially fulfills", "type": "ot"}
        ],

        "divine_council_note": "The Queen of Sheba's confession that Solomon sits 'on his throne as king "
                               "for the LORD your God' (9:8) identifies the Davidic throne as a divine "
                               "council seat. Solomon does not rule in his own right but as YHWH's appointed "
                               "regent -- the human member of the divine council who administers YHWH's rule "
                               "on earth. This is the theology of Psalm 2:6-7 and Psalm 110:1: the Davidic "
                               "king rules because YHWH has set him on the holy hill, at his right hand. Even "
                               "a foreign queen recognizes what Israel sometimes forgot: the king serves at "
                               "YHWH's pleasure, not his own.",

        "sections": [
            {
                "heading": "Solomon's Building and Worship Administration (2 Chr 8:1-18)",
                "body": "The Chronicler summarizes Solomon's twenty-year building program: cities, "
                        "storehouses, and garrison towns throughout his kingdom (8:1-6). He notes that "
                        "Solomon used non-Israelite forced labor for construction (8:7-9) while Israelites "
                        "served as commanders and officers -- a detail that addresses the tension around "
                        "corvee labor. The chapter's climax is Solomon's regulation of temple worship: "
                        "daily offerings, Sabbath offerings, new moon offerings, and the three annual "
                        "festivals (8:12-13), all carried out 'according to the rule of Moses his father "
                        "David had commanded' (8:14). The Chronicler presents Solomon as the executor of "
                        "both Mosaic law and Davidic design. Proper worship is the measure of a righteous "
                        "king, and Solomon meets the standard perfectly."
            },
            {
                "heading": "The Queen of Sheba: The Nations Witness YHWH's Wisdom (2 Chr 9:1-12)",
                "body": "The Queen of Sheba arrives with 'a very great retinue and camels bearing spices "
                        "and very much gold and precious stones' (9:1). She tests Solomon 'with hard "
                        "questions,' and 'Solomon answered all her questions. There was nothing hidden from "
                        "Solomon that he could not explain to her' (9:2). Her response is worship: 'Blessed "
                        "be the LORD your God, who has delighted in you and set you on his throne as king "
                        "for the LORD your God! Because your God loved Israel and would establish them "
                        "forever, he has made you king over them, that you may execute justice and "
                        "righteousness' (9:8). A pagan queen recognizes YHWH's sovereign love as the "
                        "source of Solomon's reign. This is the Chronicler's missional note: the nations "
                        "are meant to see YHWH's glory through Israel's king."
            },
            {
                "heading": "The Wealth of Solomon and His Death (2 Chr 9:13-31)",
                "body": "Solomon's annual gold income: 666 talents (9:13) -- a number later echoed in "
                        "Revelation 13:18. His throne of ivory overlaid with gold, with twelve lions on "
                        "six steps (9:17-19), represents royal magnificence without parallel: 'Nothing "
                        "like it was ever made in any kingdom' (9:19). Silver was 'not considered as "
                        "anything in the days of Solomon' (9:20). The Chronicler's Solomon dies without "
                        "the shadow that falls in 1 Kings 11. There is no mention of foreign wives "
                        "leading him astray, no worship of Ashtoreth or Molech, no divine anger. The "
                        "Chronicler is not lying -- he is selecting material for theological purpose. "
                        "His Solomon is a TYPE of the ideal king, the model of what faithful temple "
                        "worship looks like at its best. The imperfections recorded in Kings serve "
                        "Kings' purposes; the Chronicler has different purposes."
            }
        ]
    }
]
