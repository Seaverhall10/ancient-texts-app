"""
era_isaiah_judgment.py -- Judgment on Judah and the Throne Vision (Isaiah 1-12)

The opening collection of Isaiah's oracles, delivered primarily during the reigns
of Uzziah, Jotham, Ahaz, and Hezekiah. These chapters contain some of the most
theologically dense material in the prophetic corpus: the divine courtroom
indictment of Judah (ch. 1), the seraphim throne vision and divine council
commissioning (ch. 6), the Immanuel sign during the Syro-Ephraimite crisis (ch. 7),
and the messianic oracle of the child who is El Gibbor and Sar Shalom (9:6-7).
The section moves from judgment to hope, from indictment to the promise of a
righteous Branch from the stump of Jesse.
"""

CHAPTERS = [
    {
        "id": "isa-1",
        "ref": "Isaiah 1",
        "chapter_num": 1,
        "title": "The Divine Courtroom: YHWH's Lawsuit Against Judah",
        "era": "isaiah_judgment",
        "type": "chapter",

        "synopsis": "Isaiah opens with a riv -- a covenant lawsuit -- in which YHWH summons heaven "
                    "and earth as witnesses against his people. The language is forensic: 'Hear, O "
                    "heavens, and give ear, O earth; for YHWH has spoken' (1:2). Heaven and earth "
                    "serve as treaty witnesses, the same cosmic pair invoked in Deuteronomy 32:1 when "
                    "Moses called them to witness the covenant. YHWH's indictment is devastating: "
                    "'Children I have reared and brought up, but they have rebelled against me. The "
                    "ox knows its owner, and the donkey its master's crib, but Israel does not know, "
                    "my people do not understand' (1:2-3). The animals display more loyalty than YHWH's "
                    "own people. Judah is described as a beaten body -- 'the whole head is sick, and "
                    "the whole heart faint' (1:5). Their sacrificial worship is rejected because it is "
                    "decoupled from justice: 'What to me is the multitude of your sacrifices?' (1:11). "
                    "YHWH demands justice, not ritual: 'Wash yourselves; make yourselves clean... learn "
                    "to do good; seek justice, correct oppression; bring justice to the fatherless, "
                    "plead the widow's cause' (1:16-17). The chapter ends with the famous offer: "
                    "'Though your sins are like scarlet, they shall be as white as snow' (1:18), "
                    "followed by the warning that the 'faithful city' (Zion) has become a harlot.",

        "key_verse": {
            "ref": "Isaiah 1:18",
            "text": "Come now, let us reason together, says the LORD: though your sins are like scarlet, they shall be as white as snow; though they are red like crimson, they shall become like wool.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "riv (covenant lawsuit -- the legal genre YHWH employs against his people)",
            "chazon (vision -- the term for Isaiah's entire prophetic collection)",
            "pasha (to rebel/transgress -- deliberate covenant violation, not mere error)",
            "mishpat (justice/judgment -- the social righteousness YHWH demands over ritual)",
            "tsedaqah (righteousness -- right standing, covenant faithfulness in action)",
            "shanim (scarlet -- the deep red of sin, transformed to white by YHWH's grace)",
            "zonah (harlot -- the faithful city become unfaithful, echoing Hosea's theme)"
        ],

        "ane_backdrop": "The riv (covenant lawsuit) pattern is well attested in ANE treaty literature. "
                        "Hittite suzerainty treaties from the second millennium BC include provisions "
                        "for the divine witnesses -- typically the gods of both parties -- to be invoked "
                        "when treaty violations are adjudicated. The summons of heaven and earth as "
                        "witnesses (1:2) follows this pattern precisely: YHWH invokes the cosmic "
                        "witnesses who were present when the covenant was ratified at Sinai (cf. Deut "
                        "4:26; 30:19; 32:1). The indictment of sacrificial worship divorced from justice "
                        "parallels prophetic critiques throughout the ANE, where temple rituals were "
                        "sometimes challenged as empty formalism. Egyptian wisdom texts (particularly "
                        "the Instruction of Amenemope) also contrast genuine piety with mere ritual "
                        "performance.",

        "second_temple": [
            {
                "source": "1QIsa^a (Great Isaiah Scroll)",
                "summary": "The complete Isaiah scroll from Qumran preserves chapter 1 with minor "
                           "orthographic variations, confirming the textual stability of the lawsuit "
                           "oracle across a millennium of transmission.",
                "relevance": "The Dead Sea Scrolls demonstrate that Isaiah 1 was transmitted with "
                             "extraordinary fidelity, and the Qumran community regarded it as directly "
                             "applicable to their own generation's unfaithfulness."
            },
            {
                "source": "Targum Jonathan on Isaiah 1:18",
                "summary": "The Targum renders 'let us reason together' as 'turn to my Torah,' "
                           "interpreting the forensic language as a call to repentance through "
                           "Torah study.",
                "relevance": "The Targumic tradition emphasizes that YHWH's courtroom offer is not "
                             "merely legal but redemptive -- the goal of the lawsuit is restoration, "
                             "not destruction."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:1", "note": "'Give ear, O heavens, and I will speak; and let the earth hear' -- the covenant witness formula Isaiah echoes", "type": "ot"},
            {"ref": "Micah 6:1-8", "note": "Another prophetic riv lawsuit: 'He has told you, O man, what is good... to do justice, love kindness, walk humbly'", "type": "ot"},
            {"ref": "Amos 5:21-24", "note": "'I hate, I despise your feasts... let justice roll down like waters' -- the same rejection of ritual without justice", "type": "ot"},
            {"ref": "Hosea 4:1-3", "note": "YHWH's lawsuit against Israel: 'there is no faithfulness or steadfast love, and no knowledge of God in the land'", "type": "ot"},
            {"ref": "Revelation 1:5", "note": "Christ's blood washes sin white -- fulfilling the scarlet-to-snow promise of 1:18", "type": "nt"},
            {"ref": "Romans 12:1", "note": "Present your bodies as a living sacrifice -- the NT resolution of the ritual-vs-justice tension", "type": "nt"}
        ],

        "divine_council_note": "Isaiah 1 opens as a divine courtroom scene. YHWH is the judge, heaven "
                               "and earth are the witnesses, and Israel is the defendant. The riv genre "
                               "presupposes the divine council setting of Psalm 82, where YHWH judges "
                               "among the elohim. Here the judgment falls not on the divine council "
                               "members who failed to govern the nations justly (Ps 82:2-4) but on YHWH's "
                               "own people who have failed to embody the justice their God demands. The "
                               "cosmic witness formula -- shamayim and erets -- invokes the entire created "
                               "order as testimony: the covenant violations are not private matters but "
                               "offenses against the cosmic order that YHWH established. The 'faithful "
                               "city become a harlot' (1:21) uses the same adultery metaphor found in "
                               "Hosea and Ezekiel, where Israel's idolatry is described as spiritual "
                               "prostitution with other elohim -- the very beings allotted to other "
                               "nations in the Deuteronomy 32:8-9 framework.",

        "sections": [
            {
                "heading": "The Covenant Lawsuit: Heaven and Earth as Witnesses (1:1-9)",
                "body": "The superscription identifies the collection as 'the chazon (vision) of Isaiah "
                        "son of Amoz, which he saw concerning Judah and Jerusalem in the days of Uzziah, "
                        "Jotham, Ahaz, and Hezekiah, kings of Judah' (1:1). The span of four kings "
                        "covers roughly 740-686 BC -- over half a century of prophetic ministry during "
                        "one of the most turbulent periods in Judah's history. The lawsuit begins with "
                        "the summons: 'Hear (shimu), O heavens, and give ear (ha'azini), O earth' (1:2). "
                        "These verbs are the technical vocabulary of treaty witness invocation, echoing "
                        "the Song of Moses (Deut 32:1) where heaven and earth were first called to "
                        "witness the covenant. YHWH's charge is parental betrayal: 'Children (banim) I "
                        "have reared (giddalti) and brought up (romamti), but they have rebelled (pashu) "
                        "against me' (1:2). The verb pasha is the strongest Hebrew word for covenant "
                        "violation -- deliberate, willful rebellion. Even animals demonstrate more "
                        "covenant loyalty than Israel: 'The ox knows its owner (qonehu), and the donkey "
                        "its master's feeding trough' (1:3). The indictment escalates: 'Ah, sinful "
                        "nation, a people laden with iniquity, offspring of evildoers, children who deal "
                        "corruptly! They have forsaken YHWH, they have despised the Holy One of Israel' "
                        "(1:4). The title Qedosh Yisrael ('Holy One of Israel') is Isaiah's signature "
                        "divine name -- appearing 25 times in the book -- and it connects directly to "
                        "the throne vision of chapter 6 where the seraphim cry 'qadosh, qadosh, qadosh.'"
            },
            {
                "heading": "The Rejection of Empty Worship (1:10-20)",
                "body": "YHWH addresses Judah's leaders as 'rulers of Sodom' and the people as 'people "
                        "of Gomorrah' (1:10) -- a shocking equivalence between the covenant people and "
                        "the paradigmatic cities of divine judgment. The indictment targets the "
                        "sacrificial system itself: 'What to me is the multitude of your sacrifices? "
                        "says YHWH. I have had enough of burnt offerings (olot) of rams and the fat of "
                        "well-fed beasts. I do not delight in the blood of bulls, or of lambs, or of "
                        "goats' (1:11). This is not a rejection of sacrifice per se but of sacrifice "
                        "divorced from justice. YHWH continues: 'When you come to appear before me, who "
                        "has required of you this trampling of my courts?' (1:12). The verb ramas "
                        "('trampling') suggests that worship has become desecration. New moons, "
                        "Sabbaths, and appointed feasts (mo'adim) are called 'an abomination' (1:13). "
                        "Even prayer is rejected: 'When you spread out your hands, I will hide my eyes "
                        "from you; even though you make many prayers, I will not listen; your hands are "
                        "full of blood (damim)' (1:15). The hands raised in prayer are stained with the "
                        "blood of injustice. The remedy is not more ritual but transformed behavior: "
                        "'Wash yourselves; make yourselves clean... cease to do evil, learn to do good; "
                        "seek mishpat, correct oppression; bring justice to the fatherless, plead the "
                        "widow's cause' (1:16-17). Then comes the offer of grace: 'Though your sins are "
                        "like shanim (scarlet), they shall be white as snow' (1:18). The imagery is of "
                        "a deep, fast dye -- permanent in human terms -- made impermanent by divine power."
            },
            {
                "heading": "The Faithful City Become a Harlot (1:21-31)",
                "body": "The lament over Jerusalem is structured as a qinah (funeral dirge): 'How the "
                        "faithful city (qiryah ne'emanah) has become a harlot (zonah)! She who was full "
                        "of mishpat! Righteousness (tsedeq) lodged in her, but now murderers' (1:21). "
                        "The degradation is expressed in metallurgical terms: 'Your silver has become "
                        "dross (sigim), your choice wine mixed with water' (1:22). What was pure has been "
                        "corrupted. The accusation is institutional: 'Your princes (sarim) are rebels and "
                        "companions of thieves. Everyone loves a bribe and runs after gifts. They do not "
                        "bring justice to the fatherless, and the widow's cause does not come to them' "
                        "(1:23). The leaders who should embody YHWH's justice have become agents of "
                        "injustice. YHWH's response is a purging fire: 'I will turn my hand against you "
                        "and will smelt away your dross as with lye and remove all your alloy' (1:25). "
                        "The divine refiner will restore Zion to purity: 'Afterward you shall be called "
                        "the city of righteousness, the faithful city' (1:26). The chapter ends with the "
                        "announcement that Zion will be redeemed through mishpat (justice) and those who "
                        "return through tsedaqah (righteousness), while rebels and sinners will be "
                        "destroyed. The oak gardens and idol worship (1:29-31) point to the nature "
                        "religion of Canaanite influence -- the cosmic conflict between YHWH worship and "
                        "the worship of other elohim plays out in Judah's own territory."
            }
        ]
    },

    {
        "id": "isa-6",
        "ref": "Isaiah 6",
        "chapter_num": 6,
        "title": "The Seraphim Throne Vision: Divine Council Commissioning",
        "era": "isaiah_judgment",
        "type": "chapter",

        "synopsis": "'In the year that King Uzziah died, I saw the Lord (Adonai) sitting upon a "
                    "throne, high and lifted up; and the train of his robe filled the temple' (6:1). "
                    "Isaiah is granted a vision of the divine council in session -- the throne room "
                    "of YHWH. The seraphim (saraphim, 'burning ones') attend the throne, each with "
                    "six wings: two covering the face (shielding from the divine glory), two covering "
                    "the feet (a euphemism for genitalia -- modesty before the Holy One), and two for "
                    "flying. They cry the Trisagion: 'Qadosh, qadosh, qadosh YHWH tseva'ot! The "
                    "fullness of all the earth is his glory!' (6:3). The threefold repetition is the "
                    "Hebrew superlative -- YHWH is not merely holy but supremely, incomparably, "
                    "transcendently holy. The doorposts shake, the temple fills with smoke -- the "
                    "sensory markers of a genuine theophany. Isaiah's response is terror: 'Woe is "
                    "me! For I am undone (nidmeti); for I am a man of unclean lips, and I dwell in "
                    "the midst of a people of unclean lips; for my eyes have seen the King, YHWH "
                    "tseva'ot!' (6:5). A seraph takes a burning coal (ritspah) from the altar and "
                    "touches Isaiah's mouth, declaring his guilt removed and his sin atoned for. Then "
                    "comes the divine council deliberation: 'Whom shall I send, and who will go for "
                    "us?' (6:8). The plural 'us' is the voice of YHWH addressing his council. Isaiah "
                    "volunteers: 'Here am I! Send me.' The commission is devastating: preach, but the "
                    "people will not understand. 'Make the heart of this people dull, and their ears "
                    "heavy, and blind their eyes' (6:10). When Isaiah asks 'How long, O Lord?' the "
                    "answer is: until the land is utterly desolated. Yet a seed remains -- the holy "
                    "seed (zera qodesh) is the stump that endures (6:13).",

        "key_verse": {
            "ref": "Isaiah 6:3",
            "text": "And one called to another and said: 'Holy, holy, holy is the LORD of hosts; the whole earth is full of his glory!'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "saraphim (burning ones -- fiery angelic beings attending YHWH's throne)",
            "qadosh (holy -- set apart, transcendently other; the Trisagion's core word)",
            "YHWH tseva'ot (YHWH of hosts/armies -- the divine warrior enthroned over his council)",
            "kavod (glory -- the visible radiance of YHWH's presence filling the earth)",
            "nidmeti (I am undone/ruined -- literally 'I am silenced/destroyed')",
            "ritspah (burning coal/glowing stone -- the instrument of Isaiah's purification)",
            "kaphar (to atone/cover -- the technical term for sacrificial atonement applied to Isaiah's lips)",
            "zera qodesh (holy seed -- the faithful remnant that survives judgment)"
        ],

        "ane_backdrop": "The throne-room vision of Isaiah 6 participates in a widespread ANE genre: "
                        "the divine council scene. In Ugaritic texts from Ras Shamra (14th-13th c. BC), "
                        "El presides over the assembly of the gods (phr ilm, 'assembly of the gods') "
                        "on his cosmic mountain. Messengers come and go, decisions are made about the "
                        "fate of nations, and warrior-gods are commissioned for tasks. In Mesopotamian "
                        "literature, the Enuma Elish describes Marduk receiving his commission from the "
                        "divine assembly to fight Tiamat. The Israelite version is distinctive in its "
                        "monotheistic reframing: YHWH does not rule as first-among-equals but as the "
                        "incomparable sovereign. The seraphim are not rival gods but attendants. The "
                        "term saraph connects to the fiery serpents (seraphim nechashim) of Numbers 21:6 "
                        "and to the 'flying serpent' (saraph me'opheph) of Isaiah 14:29 and 30:6. In "
                        "Egyptian iconography, winged uraei (serpents) flank the pharaoh's throne as "
                        "guardians. The seraphim of Isaiah 6 are throne guardians of the cosmic King.",

        "second_temple": [
            {
                "source": "1 Enoch 14:8-25",
                "summary": "Enoch's throne vision describes YHWH on a lofty throne with wheels of "
                           "fire, surrounded by ten thousand times ten thousand angels. The parallels "
                           "to Isaiah 6 are extensive: the throne, the fear, the fire, the attendants.",
                "relevance": "The Enochic tradition elaborates the divine council throne room that "
                             "Isaiah glimpsed, developing a detailed angelology around the council setting."
            },
            {
                "source": "Revelation 4:1-11",
                "summary": "John's throne vision in Revelation echoes Isaiah 6 directly: the throne, "
                           "the living creatures crying 'Holy, holy, holy,' the sea of glass, the "
                           "overwhelming worship.",
                "relevance": "John's Apocalypse presents the same divine council throne room Isaiah "
                             "saw, now with the Lamb (Christ) at the center -- the fulfillment of the "
                             "council's purposes."
            },
            {
                "source": "Songs of the Sabbath Sacrifice (4Q400-407)",
                "summary": "These Qumran texts describe angelic liturgy in the heavenly temple, with "
                           "detailed accounts of the 'holy ones' praising God's glory -- extending the "
                           "Isaiah 6 tradition into elaborate heavenly worship.",
                "relevance": "The Dead Sea Scrolls community believed they were participating in the "
                             "same worship the seraphim performed, joining heaven and earth in praise."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 22:19-23", "note": "Micaiah sees YHWH on his throne with the host of heaven -- another prophet's vision of the divine council in session", "type": "ot"},
            {"ref": "Ezekiel 1:4-28", "note": "Ezekiel's throne chariot vision -- living creatures, wheels, fire, the likeness of the glory of YHWH", "type": "ot"},
            {"ref": "Exodus 3:1-6", "note": "Moses at the burning bush -- covering his face because he was afraid to look at God, paralleling Isaiah's terror", "type": "ot"},
            {"ref": "Daniel 7:9-10", "note": "The Ancient of Days on his throne, fire streaming, books opened, thousands upon thousands attending -- the same council scene", "type": "ot"},
            {"ref": "John 12:41", "note": "'Isaiah said these things because he saw his glory and spoke of him' -- John identifies the one Isaiah saw as Christ", "type": "nt"},
            {"ref": "Revelation 4:8", "note": "The four living creatures never cease to say 'Holy, holy, holy, is the Lord God Almighty' -- the eternal Trisagion", "type": "nt"},
            {"ref": "Acts 28:25-27", "note": "Paul quotes Isaiah 6:9-10 to explain Israel's hardening -- the judicial blinding still operative in the apostolic era", "type": "nt"},
            {"ref": "Psalm 82:1", "note": "'God has taken his place in the divine council; in the midst of the elohim he holds judgment' -- the council setting Isaiah enters", "type": "ot"}
        ],

        "divine_council_note": "Isaiah 6 is the premier divine council commissioning text in the Old "
                               "Testament. YHWH is enthroned as King (melek) over his council (6:5). The "
                               "seraphim are council members -- fiery beings who attend the throne and "
                               "proclaim YHWH's holiness. The Trisagion ('qadosh, qadosh, qadosh') is "
                               "not merely praise but a declaration of cosmic reality: YHWH is supremely "
                               "other, set apart from all created beings including the divine council "
                               "members themselves. The deliberation formula 'Whom shall I send, and who "
                               "will go for US?' (6:8) is the most explicit divine council language in "
                               "Isaiah. The plural 'us' is not a 'plural of majesty' (a grammatical "
                               "category unattested in Hebrew) but the voice of the divine King addressing "
                               "his assembled council -- the same 'us' of Genesis 1:26 ('let us make man'), "
                               "Genesis 3:22 ('the man has become like one of us'), and Genesis 11:7 ('let "
                               "us go down'). Isaiah, a human, is given the extraordinary privilege of "
                               "standing in the divine council and volunteering for a commission normally "
                               "given to angelic beings. This parallels the prophetic claim of Jeremiah "
                               "23:18, 22: the true prophet is one who has 'stood in the council (sod) of "
                               "YHWH' and heard his word. Isaiah's commission -- to preach judgment that "
                               "hardens rather than heals -- is a council decree: the people's obstinacy "
                               "has been judicially ratified in the heavenly court.",

        "sections": [
            {
                "heading": "The Throne Vision: Adonai Enthroned (6:1-4)",
                "body": "'In the year that King Uzziah died' (6:1) -- approximately 740 BC. Uzziah's "
                        "death marks the end of a prosperous era and the beginning of the Assyrian "
                        "crisis that will dominate Isaiah's ministry. As the earthly throne empties, "
                        "the heavenly throne is revealed: 'I saw Adonai sitting upon a throne, high and "
                        "lifted up, and the train (shulav) of his robe filled the temple (hekal)' "
                        "(6:1). The term Adonai ('my Lord, sovereign') designates YHWH in his royal "
                        "authority. The throne is 'high and lifted up' (ram venissa) -- the same "
                        "description applied to the Suffering Servant in 52:13, creating a deliberate "
                        "theological arc: the enthroned King will become the exalted Servant. The shulav "
                        "(train, skirts) filling the hekal suggests a figure of cosmic proportions -- "
                        "YHWH's very garment overflows the temple space. The seraphim (saraphim) stand "
                        "above him -- 'burning ones,' a term connected to the fiery serpents of the "
                        "wilderness (Num 21:6) and to ancient Near Eastern guardian figures. Each has "
                        "six wings: 'with two he covered his face' (shielding from unbearable glory), "
                        "'and with two he covered his feet' (raglav -- often a euphemism for the lower "
                        "body, expressing modesty before the divine), 'and with two he flew' (6:2). "
                        "Their cry shakes the foundations: 'Qadosh, qadosh, qadosh YHWH tseva'ot! "
                        "Melo kol-ha'arets kevodo!' ('Holy, holy, holy is YHWH of hosts! The fullness "
                        "of all the earth is his glory!') (6:3). The threefold repetition is the Hebrew "
                        "superlative absolute -- the maximum degree of holiness. YHWH tseva'ot ('YHWH "
                        "of armies/hosts') is the divine warrior title designating command over both "
                        "heavenly and earthly forces. The doorposts tremble, the temple fills with "
                        "smoke -- the classic accompaniments of theophany (cf. Sinai, Exod 19:18)."
            },
            {
                "heading": "Isaiah's Terror and the Burning Coal (6:5-7)",
                "body": "Isaiah's response is not worship but dread: 'Woe (oi) is me! For I am undone "
                        "(nidmeti)!' (6:5). The word nidmeti can mean 'I am silenced,' 'I am destroyed,' "
                        "or 'I am cut off' -- a man of impure speech confronting the source of all "
                        "purity. The specific nature of his uncleanness is 'lips' (sephatayim) -- the "
                        "organ of prophetic speech. Isaiah cannot speak for God because his mouth is "
                        "contaminated, and he dwells among a people whose collective speech is equally "
                        "polluted. His final statement explains the terror: 'for my eyes have seen the "
                        "King (ha-Melek), YHWH tseva'ot!' (6:5). To see YHWH is to die (Exod 33:20); "
                        "Isaiah expects destruction. Instead, one of the seraphim flies to him with a "
                        "ritspah -- a burning coal or glowing stone -- taken with tongs from the altar "
                        "(mizbe'ach). The seraph touches (naga) Isaiah's mouth with the coal and "
                        "declares: 'Behold, this has touched your lips; your guilt (avon) is taken "
                        "away, and your sin (chata'ah) is atoned for (tekuppar)' (6:7). The verb "
                        "kaphar ('to atone, cover, purge') is the central term of the Levitical "
                        "sacrificial system. The altar coal -- fire from the place of sacrifice -- "
                        "purifies the prophet's lips for service. The seraph acts as a priestly "
                        "mediator, performing an atonement that enables Isaiah to survive the divine "
                        "presence and speak the divine word."
            },
            {
                "heading": "The Council Deliberation: 'Who Will Go for Us?' (6:8-10)",
                "body": "With his lips purified, Isaiah hears the voice of YHWH addressing the "
                        "assembled council: 'Whom shall I send (eshlach), and who will go for us "
                        "(lanu)?' (6:8). The shift from first person singular ('I') to first person "
                        "plural ('us') is the key to the passage's divine council significance. YHWH "
                        "speaks as the council's head, seeking a messenger (malak) for a mission. "
                        "Isaiah volunteers: 'Hineni! Shelacheni!' ('Here am I! Send me!'). The response "
                        "echoes Abraham's 'hineni' to God (Gen 22:1) and Moses' response at the burning "
                        "bush (Exod 3:4). Isaiah becomes the council's emissary to the human realm. "
                        "The commission, however, is paradoxically devastating: 'Go, and say to this "
                        "people: Keep on hearing (shimu shamoa), but do not understand (al-tavinu); "
                        "keep on seeing (re'u ra'o), but do not perceive (al-ted'u)' (6:9). The "
                        "infinitive-absolute constructions (shamoa...ra'o) intensify the irony: the "
                        "more they hear, the less they understand. 'Make the heart of this people fat "
                        "(hashmen), and their ears heavy (hakhbed), and shut (hasha) their eyes; lest "
                        "they see with their eyes, and hear with their ears, and understand with their "
                        "hearts, and turn and be healed' (6:10). This is judicial hardening -- a "
                        "divine council decree that Israel's refusal to hear has been ratified in the "
                        "heavenly court. The New Testament cites this passage more than any other "
                        "Isaiah text (Matt 13:14-15; Mark 4:12; Luke 8:10; John 12:40; Acts 28:26-27; "
                        "Rom 11:8) to explain Israel's rejection of the Messiah."
            },
            {
                "heading": "How Long? The Stump and the Holy Seed (6:11-13)",
                "body": "Isaiah asks the agonizing question: 'How long, Adonai?' (ad-matai, Adonai) "
                        "(6:11). The answer is total devastation: 'Until cities lie waste without "
                        "inhabitant, and houses without people, and the land is a desolate waste, and "
                        "YHWH removes people far away, and the forsaken places are many in the midst of "
                        "the land' (6:11-12). The prophecy envisions the Babylonian exile -- cities "
                        "emptied, land abandoned, the people 'removed far away' (richaq). But the oracle "
                        "does not end in annihilation: 'And though a tenth remain in it, it will be "
                        "burned again, like a terebinth or an oak, whose stump (matstsevet) remains when "
                        "it is felled. The holy seed (zera qodesh) is its stump' (6:13). The image is "
                        "of a tree cut down but not dead -- the stump retains life and will sprout again. "
                        "This 'holy seed' is the remnant theology that runs through Isaiah: not all will "
                        "be destroyed. From the devastated stump, new growth will emerge. The connection "
                        "to Isaiah 11:1 is explicit: 'There shall come forth a shoot (choter) from the "
                        "stump (geza) of Jesse, and a branch (netser) from his roots shall bear fruit.' "
                        "The holy seed of 6:13 becomes the messianic branch of 11:1. The throne vision "
                        "that began with the glory of the divine King ends with the promise that from "
                        "the desolation his council has decreed, a seed of holiness will survive."
            }
        ]
    },

    {
        "id": "isa-7",
        "ref": "Isaiah 7",
        "chapter_num": 7,
        "title": "The Immanuel Sign: God With Us in the Crisis",
        "era": "isaiah_judgment",
        "type": "chapter",

        "synopsis": "The Syro-Ephraimite crisis (~735 BC): King Rezin of Aram (Syria) and King Pekah "
                    "of Israel (Ephraim) march against Jerusalem to depose King Ahaz of Judah and "
                    "install a puppet king (the 'son of Tabeel'). Ahaz and his people tremble 'as the "
                    "trees of the forest shake before the wind' (7:2). YHWH sends Isaiah with his son "
                    "Shear-jashub ('a remnant shall return') to meet Ahaz at the end of the conduit "
                    "of the upper pool -- the same location where the Rabshakeh will later deliver "
                    "Sennacherib's ultimatum (36:2). Isaiah's message: 'Be quiet (hashqet), do not "
                    "fear, and do not let your heart be faint because of these two smoldering stumps "
                    "of firebrands' (7:4). YHWH offers Ahaz a sign -- anything, 'deep as Sheol or "
                    "high as heaven' (7:11). Ahaz refuses with false piety: 'I will not ask, and I "
                    "will not put YHWH to the test' (7:12). His real plan is to appeal to Assyria's "
                    "Tiglath-pileser III for help (2 Kings 16:7). Isaiah responds with the sign Ahaz "
                    "refused to ask for: 'Therefore the Lord himself will give you a sign. Behold, "
                    "the almah (young woman) shall conceive and bear a son, and shall call his name "
                    "Immanuel (Immanu-El, God with us)' (7:14). The child's infancy will be the "
                    "measure of judgment: before he knows good from evil, the two threatening kings "
                    "will be gone -- but Assyria, the very power Ahaz trusts, will become the real "
                    "devastator.",

        "key_verse": {
            "ref": "Isaiah 7:14",
            "text": "Therefore the Lord himself will give you a sign. Behold, the virgin shall conceive and bear a son, and shall call his name Immanuel.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "almah (young woman of marriageable age -- LXX renders as parthenos, 'virgin')",
            "Immanu-El (God with us -- the theophoric name of the promised child)",
            "ot (sign -- a prophetic marker confirming divine involvement)",
            "Shear-jashub (a remnant shall return -- Isaiah's son as a living prophetic sign)",
            "hashqet (be still/quiet -- the command to trust YHWH rather than human alliance)",
            "she'ol (the underworld -- the depth YHWH's sign could reach)",
            "chem'ah (curds/butter -- the food of the Immanuel child, signifying either abundance or desolation)"
        ],

        "ane_backdrop": "The Syro-Ephraimite crisis fits into the larger geopolitical upheaval caused "
                        "by Tiglath-pileser III's aggressive expansion of the Neo-Assyrian Empire "
                        "(745-727 BC). The anti-Assyrian coalition of Damascus (Aram) and Samaria "
                        "(Israel) pressured Judah to join. Ahaz's refusal prompted the invasion. "
                        "Prophetic sign-children are attested in ANE practice: Egyptian and Mesopotamian "
                        "omen traditions interpreted births, names, and childhood events as divine "
                        "messages about political outcomes. The practice of a king consulting a prophet "
                        "before battle is well attested in the Mari archives (18th c. BC), where kings "
                        "received oracles from prophets before military campaigns. The 'almah' debate "
                        "has ancient roots: the Hebrew word denotes a young woman of marriageable age "
                        "(Gen 24:43; Exod 2:8; Ps 68:25; Prov 30:19; Song 1:3; 6:8), while the LXX "
                        "translation parthenos ('virgin') reflects a Second Temple interpretive tradition "
                        "that saw deeper messianic significance.",

        "second_temple": [
            {
                "source": "LXX (Septuagint) Isaiah 7:14",
                "summary": "The LXX translates almah as parthenos ('virgin'), narrowing the semantic "
                           "range from 'young woman' to 'virgin,' which became the basis for the "
                           "New Testament citation in Matthew 1:23.",
                "relevance": "The LXX translation reflects a pre-Christian Jewish interpretive tradition "
                             "that already saw messianic virginal significance in the Immanuel oracle."
            },
            {
                "source": "Matthew 1:22-23",
                "summary": "Matthew explicitly cites Isaiah 7:14 as fulfilled in Mary's virginal "
                           "conception of Jesus: 'All this took place to fulfill what the Lord had "
                           "spoken by the prophet.'",
                "relevance": "The Gospel applies the Immanuel oracle to Jesus as the ultimate 'God "
                             "with us' -- the divine presence incarnate."
            }
        ],

        "cross_refs": [
            {"ref": "2 Kings 16:5-9", "note": "The historical account of the Syro-Ephraimite crisis and Ahaz's appeal to Assyria", "type": "ot"},
            {"ref": "Matthew 1:22-23", "note": "'Behold, the virgin shall conceive and bear a son, and they shall call his name Immanuel' -- the messianic fulfillment", "type": "nt"},
            {"ref": "Isaiah 8:8, 10", "note": "Immanuel named again -- 'your land, O Immanuel' and 'God is with us (Immanu-El)'", "type": "ot"},
            {"ref": "Isaiah 9:6-7", "note": "The child of the Immanuel promise elaborated: Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace", "type": "ot"},
            {"ref": "Isaiah 11:1-5", "note": "The shoot from Jesse's stump -- the messianic king who fulfills the Immanuel hope", "type": "ot"},
            {"ref": "2 Chronicles 28:1-5", "note": "Ahaz's unfaithfulness: he made molten images for the Baals and burned his sons as offerings", "type": "ot"},
            {"ref": "Matthew 28:20", "note": "'I am with you always, to the end of the age' -- Jesus as the permanent Immanuel", "type": "nt"}
        ],

        "divine_council_note": "The Immanuel oracle operates on multiple levels of divine council "
                               "theology. Ahaz refuses to ask for a sign 'deep as Sheol or high as "
                               "heaven' (7:11) -- a merism encompassing the entire cosmic realm, from the "
                               "underworld to the divine council's heavenly throne room. YHWH's response "
                               "is to give a sign anyway -- one that will ultimately reach both extremes. "
                               "The name Immanu-El ('God with us') is a divine council declaration: the "
                               "Most High himself will be present with his people. In the immediate "
                               "context, this means YHWH's sovereign control over the political crisis. "
                               "In the fuller canonical context, Immanuel becomes the title of the "
                               "messianic child who is also called El Gibbor (Mighty God) in 9:6 -- a "
                               "divine being who enters the human realm. The dual nature of the Immanuel "
                               "figure -- a child born of a woman who bears the name 'God with us' -- "
                               "anticipates the two-powers-in-heaven theology where the visible YHWH (the "
                               "Angel of YHWH, the Word, the Son) takes human form.",

        "sections": [
            {
                "heading": "The Crisis: Aram and Ephraim March on Jerusalem (7:1-9)",
                "body": "The historical setting is precisely dated to the reign of Ahaz son of Jotham "
                        "(~735 BC). Rezin of Aram and Pekah ben Remaliah of Israel form a coalition to "
                        "force Judah into an anti-Assyrian alliance. When they march on Jerusalem, 'the "
                        "heart of Ahaz and the heart of his people shook as the trees of the forest "
                        "shake before the wind' (7:2). YHWH sends Isaiah with his son Shear-jashub ('a "
                        "remnant shall return') to meet Ahaz at the water conduit -- a location of "
                        "strategic vulnerability where the king is inspecting Jerusalem's water supply "
                        "in preparation for siege. Isaiah's message is calm defiance: the two enemy "
                        "kings are merely 'smoldering stumps of firebrands' (zanvot udim ashenim, 7:4) "
                        "-- they have already burned out and are merely smoking. Within sixty-five years "
                        "Ephraim will cease to be a people (7:8) -- fulfilled when Esarhaddon resettled "
                        "foreigners in Samaria (~670 BC). The condition for Judah's survival: 'If you "
                        "are not firm in faith (ta'aminu), you shall not be established (te'amenu)' "
                        "(7:9b) -- a wordplay on the root aman (to be firm, faithful, reliable) that "
                        "defines the entire theological challenge: trust YHWH or be destroyed."
            },
            {
                "heading": "The Sign Refused and Given: Immanuel (7:10-17)",
                "body": "YHWH invites Ahaz to ask for a sign -- any sign, from the depths of Sheol to "
                        "the heights of heaven (7:11). The offer is extraordinary: God himself invites "
                        "the king to name his terms for a faith demonstration. Ahaz's refusal -- 'I "
                        "will not ask, and I will not put YHWH to the test' (7:12) -- sounds pious but "
                        "is actually faithless. His real plan is to ask Tiglath-pileser III for help "
                        "(2 Kings 16:7), offering the temple treasury as payment. Isaiah's rebuke is "
                        "sharp: 'Is it too little for you to weary men, that you weary my God also?' "
                        "(7:13). Then the sign comes uninvited: 'The almah shall conceive and bear a son, "
                        "and shall call his name Immanuel' (7:14). The word almah appears seven times "
                        "in the Hebrew Bible and consistently denotes a young woman of marriageable age, "
                        "with the expectation of virginity. The LXX's rendering as parthenos ('virgin') "
                        "reflects a legitimate narrowing of the sense. The sign functions on two levels: "
                        "in the immediate context, a child will be born, and before he reaches the age "
                        "of moral discernment ('before he knows how to refuse the evil and choose the "
                        "good,' 7:16), the two threatening kings will be removed. But the name Immanu-El "
                        "('God with us') transcends the immediate crisis. YHWH warns that the very "
                        "Assyria Ahaz trusts will become the instrument of Judah's devastation (7:17)."
            }
        ]
    },

    {
        "id": "isa-9",
        "ref": "Isaiah 9:1-7",
        "chapter_num": 9,
        "title": "Unto Us a Child Is Born: El Gibbor and Sar Shalom",
        "era": "isaiah_judgment",
        "type": "chapter",

        "synopsis": "From the darkness of judgment (8:22), light breaks in Galilee -- the very region "
                    "first devastated by Assyria (2 Kings 15:29): 'The people who walked in darkness "
                    "have seen a great light; those who dwelt in a land of deep darkness (tsalmut), on "
                    "them has light shined' (9:2). Joy multiplies like the harvest and the spoils of "
                    "war. The oppressor's yoke is shattered 'as on the day of Midian' (9:4) -- a "
                    "reference to Gideon's miraculous victory in Judges 7 where YHWH fought with 300 "
                    "men against thousands. Then the oracle reaches its messianic climax: 'For to us a "
                    "child is born (yeled yullad lanu), to us a son is given (ben nittan lanu), and "
                    "the government shall be upon his shoulder, and his name shall be called Wonderful "
                    "Counselor (Pele Yo'ets), Mighty God (El Gibbor), Everlasting Father (Avi-Ad), "
                    "Prince of Peace (Sar Shalom)' (9:6). The four throne names are extraordinary. "
                    "Pele Yo'ets echoes the divine attribute of wonder (pele is used for God's "
                    "miracles). El Gibbor is an unambiguous divine title -- 'God' (El) who is a "
                    "'warrior/mighty one' (gibbor); the same title is applied to YHWH in Isaiah 10:21. "
                    "Avi-Ad means 'Father of Eternity' -- one who transcends time. Sar Shalom is "
                    "'Prince of Peace' -- shalom in its fullest sense of wholeness, prosperity, and "
                    "cosmic order. This child will reign on David's throne 'with justice (mishpat) and "
                    "with righteousness (tsedaqah) from this time forth and forevermore' (9:7). 'The "
                    "zeal of YHWH tseva'ot will do this' (9:7b) -- the divine warrior's own passion "
                    "guarantees the fulfillment.",

        "key_verse": {
            "ref": "Isaiah 9:6",
            "text": "For to us a child is born, to us a son is given; and the government shall be upon his shoulder, and his name shall be called Wonderful Counselor, Mighty God, Everlasting Father, Prince of Peace.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Pele Yo'ets (Wonderful Counselor -- supernatural wisdom, divine planning)",
            "El Gibbor (Mighty God -- a divine title applied to a human child; also used for YHWH in 10:21)",
            "Avi-Ad (Father of Eternity/Everlasting Father -- transcending temporal limits)",
            "Sar Shalom (Prince of Peace -- cosmic wholeness, not merely absence of war)",
            "tsalmut (deep darkness/shadow of death -- the darkness before the messianic dawn)",
            "misrah (government/dominion -- the authority placed on the child's shoulder)",
            "qin'at YHWH (zeal of YHWH -- the passionate commitment ensuring fulfillment)"
        ],

        "ane_backdrop": "The four throne names of Isaiah 9:6 follow the pattern of Egyptian royal "
                        "titulary. Egyptian pharaohs received five 'great names' at coronation: the "
                        "Horus name, the Two Ladies name, the Golden Horus name, the praenomen, and "
                        "the nomen. Each name declared the king's relationship to the gods and his "
                        "divine mandate. Isaiah's four names function similarly -- they are throne names "
                        "declaring the messianic king's divine nature and cosmic authority. The title "
                        "El Gibbor ('Mighty God') would be shocking in any ANE context: no Egyptian or "
                        "Mesopotamian king was called by the actual name of the supreme deity. Egyptian "
                        "pharaohs were called 'son of Re' or 'Horus incarnate,' but not 'Re' itself. "
                        "Isaiah gives this child the actual divine name El -- a claim that transcends "
                        "even the highest royal theology of the ancient world.",

        "second_temple": [
            {
                "source": "Targum Jonathan on Isaiah 9:5-6",
                "summary": "The Targum renders the passage messianically: 'The prophet says to the "
                           "house of David, for unto us a child is born, unto us a son is given, and "
                           "his name has been called from of old: Wonderful Counselor, Mighty God, "
                           "He who lives forever, the Messiah in whose days peace shall increase.'",
                "relevance": "The Targumic tradition confirms pre-Christian Jewish messianic reading "
                             "of Isaiah 9:6 -- the child is the Mashiach."
            },
            {
                "source": "Luke 1:32-33",
                "summary": "The angel Gabriel tells Mary: 'He will be great and will be called the Son "
                           "of the Most High. And the Lord God will give to him the throne of his "
                           "father David, and he will reign over the house of Jacob forever.'",
                "relevance": "Luke explicitly connects Jesus' birth to the Davidic throne promise of "
                             "Isaiah 9:7 -- the child whose government has no end."
            },
            {
                "source": "Luke 2:14",
                "summary": "'Glory to God in the highest, and on earth peace (eirene) among those "
                           "with whom he is pleased!'",
                "relevance": "The angelic announcement at Jesus' birth echoes the Sar Shalom title -- "
                             "the Prince of Peace has arrived, and the divine council (angels) announces it."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 7:14", "note": "The Immanuel child -- the same messianic figure now given four throne names", "type": "ot"},
            {"ref": "Isaiah 11:1-5", "note": "The shoot from Jesse's stump, the Spirit-endowed messianic king -- the same figure", "type": "ot"},
            {"ref": "Isaiah 10:21", "note": "'A remnant will return... to El Gibbor (the Mighty God)' -- the same divine title applied to YHWH himself", "type": "ot"},
            {"ref": "Judges 7:1-25", "note": "The 'day of Midian' (9:4) -- Gideon's divine victory with 300 men, the paradigm of YHWH fighting for Israel", "type": "ot"},
            {"ref": "2 Samuel 7:12-16", "note": "The Davidic covenant: 'I will establish the throne of his kingdom forever' -- fulfilled in 9:7", "type": "ot"},
            {"ref": "Matthew 4:15-16", "note": "Matthew quotes Isaiah 9:1-2 to explain Jesus' Galilean ministry: 'the people dwelling in darkness have seen a great light'", "type": "nt"},
            {"ref": "Luke 1:32-33", "note": "Gabriel's announcement to Mary echoes the Davidic throne promise of 9:7", "type": "nt"},
            {"ref": "Ephesians 2:14", "note": "'He himself is our peace' -- Christ as the Sar Shalom who reconciles all things", "type": "nt"}
        ],

        "divine_council_note": "The throne names of Isaiah 9:6 constitute the most explicit 'two powers "
                               "in heaven' text in the prophetic corpus. A child is born -- fully human, "
                               "entering the world through birth. Yet this child bears the name El Gibbor "
                               "('Mighty God'), the same title applied to YHWH himself in Isaiah 10:21. "
                               "This is not honorific hyperbole: El is the proper name for deity, and "
                               "gibbor ('mighty one, warrior') is the council title for the divine "
                               "warrior. The child is simultaneously human (born, given) and divine (El "
                               "Gibbor, Avi-Ad). The title Sar Shalom ('Prince of Peace') uses the same "
                               "word sar ('prince, commander') applied to the Commander of YHWH's army in "
                               "Joshua 5:14 and to Michael the great prince in Daniel 12:1. This child "
                               "will occupy David's throne 'from this time forth and forevermore' (9:7) -- "
                               "an eternal reign that no merely human king could sustain. The 'zeal of "
                               "YHWH tseva'ot' (qin'at YHWH tseva'ot) that guarantees this fulfillment "
                               "is the divine warrior's own passionate commitment: the council has decreed "
                               "it, and the Most High's fervent will ensures it. This oracle, taken with "
                               "Isaiah 7:14 (Immanuel) and 11:1-5 (the Spirit-endowed branch), presents "
                               "a messianic figure who bridges heaven and earth -- a member of the divine "
                               "council who takes on human flesh and reigns forever.",

        "sections": [
            {
                "heading": "Light in Galilee: The Dawn After Darkness (9:1-5)",
                "body": "The oracle begins with geographical specificity: 'the land of Zebulun and the "
                        "land of Naphtali' (9:1) -- the northernmost tribes, the first to fall to "
                        "Assyria when Tiglath-pileser III invaded in 733 BC (2 Kings 15:29). The 'way "
                        "of the sea' (derek hayam) is the Via Maris, the great international highway, "
                        "and 'Galilee of the nations' (gelil ha-goyim) reflects the mixed ethnic "
                        "character of the northern region. From this most unlikely place -- the land of "
                        "first judgment -- comes first restoration. 'The people who walked in darkness "
                        "(choshek) have seen a great light (or gadol); those who dwelt in a land of "
                        "deep darkness (tsalmut), on them has light shined' (9:2). The word tsalmut "
                        "('shadow of death' or 'deep darkness') is the same term used in Psalm 23:4 "
                        "('the valley of the shadow of death'). The joy that erupts is compared to "
                        "harvest celebration and the division of spoils after victory (9:3). The "
                        "oppressor's yoke, rod, and staff are shattered 'as on the day of Midian' (9:4) "
                        "-- the day when YHWH defeated the Midianite horde through Gideon's absurdly "
                        "small force (Judg 7). The allusion is deliberate: this victory, like Gideon's, "
                        "will be divine, not human. Every warrior's boot and blood-stained garment will "
                        "be 'burned as fuel for the fire' (9:5) -- the implements of war consumed "
                        "because war itself has been ended by the Prince of Peace."
            },
            {
                "heading": "The Four Throne Names: The Child Who Is God (9:6-7)",
                "body": "'For to us a child is born (yeled yullad lanu), to us a son is given (ben "
                        "nittan lanu)' (9:6a). The passive constructions ('is born,' 'is given') point "
                        "to YHWH as the unspoken agent: God gives this child. 'And the government "
                        "(misrah) shall be upon his shoulder' (9:6b) -- the shoulder bearing the "
                        "insignia of rule, perhaps the key of the house of David (cf. 22:22). Then the "
                        "four throne names, each a compound divine title. Pele Yo'ets: pele ('wonder') "
                        "is used exclusively for supernatural acts of God (Exod 15:11; Judg 13:18; Ps "
                        "77:14); yo'ets ('counselor') designates one who gives counsel in the royal "
                        "court or divine council. El Gibbor: El is the generic name for deity AND the "
                        "proper name of the supreme god in the Canaanite pantheon; gibbor ('warrior, "
                        "mighty one') describes God's combat power. Isaiah 10:21 uses El Gibbor "
                        "unambiguously for YHWH: 'A remnant will return to El Gibbor.' Avi-Ad: avi "
                        "('father of') plus ad ('eternity, perpetuity') -- this child is the source "
                        "and sustainer of time itself. Sar Shalom: sar ('prince, chief, commander') "
                        "plus shalom ('peace, wholeness, completeness') -- not the absence of conflict "
                        "but the presence of total cosmic order. 'Of the increase of his government "
                        "and of peace there will be no end (ein-qets), on the throne of David and "
                        "over his kingdom, to establish it and to uphold it with mishpat and tsedaqah "
                        "from this time forth and forevermore' (9:7). The eternal reign on David's "
                        "throne fulfills the Davidic covenant of 2 Samuel 7:12-16. 'The zeal (qin'ah) "
                        "of YHWH tseva'ot will do this' -- the divine warrior's own jealous love "
                        "guarantees the promise."
            }
        ]
    },

    {
        "id": "isa-11",
        "ref": "Isaiah 11",
        "chapter_num": 11,
        "title": "The Branch from Jesse's Stump: Spirit, Justice, and Edenic Peace",
        "era": "isaiah_judgment",
        "type": "chapter",

        "synopsis": "From the stump (geza) of Jesse -- the Davidic dynasty cut down to nothing -- a "
                    "shoot (choter) and branch (netser) emerge. The sevenfold Spirit of YHWH rests "
                    "upon him: the Spirit of wisdom (chokmah) and understanding (binah), the Spirit "
                    "of counsel (etsah) and might (gevurah), the Spirit of knowledge (da'at) and the "
                    "fear of YHWH (yir'at YHWH) (11:2). This king judges not by appearance but by "
                    "righteousness: 'he shall strike the earth with the rod of his mouth, and with "
                    "the breath (ruach) of his lips he shall kill the wicked' (11:4). His reign "
                    "produces cosmic peace: the wolf dwells with the lamb, the leopard lies down with "
                    "the young goat, a little child leads them (11:6-8). 'They shall not hurt or "
                    "destroy in all my holy mountain, for the earth shall be full of the knowledge "
                    "(da'at) of YHWH as the waters cover the sea' (11:9). The chapter envisions a "
                    "second exodus: 'There will be a highway from Assyria for the remnant that remains "
                    "of his people, as there was for Israel when they came up from the land of Egypt' "
                    "(11:16). The messianic king's reign restores Eden, reverses the curse, and gathers "
                    "the scattered people of God from the four corners of the earth.",

        "key_verse": {
            "ref": "Isaiah 11:1-2",
            "text": "There shall come forth a shoot from the stump of Jesse, and a branch from his roots shall bear fruit. And the Spirit of the LORD shall rest upon him, the Spirit of wisdom and understanding, the Spirit of counsel and might, the Spirit of knowledge and the fear of the LORD.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "geza (stump -- the Davidic dynasty reduced to a rootstock, but alive)",
            "choter (shoot -- new growth from the stump; messianic terminology)",
            "netser (branch -- a green shoot; possibly the root of 'Nazarene' in Matt 2:23)",
            "ruach YHWH (Spirit of YHWH -- the sevenfold endowment of the messianic king)",
            "chokmah/binah (wisdom/understanding -- the intellectual gifts of the Spirit)",
            "etsah/gevurah (counsel/might -- the strategic and military gifts)",
            "da'at YHWH (knowledge of YHWH -- experiential, relational knowing of God)"
        ],

        "ane_backdrop": "The 'stump' imagery reflects the ANE understanding of dynastic continuity. "
                        "In Mesopotamian royal ideology, the 'root' (shurshu) of a dynasty was the "
                        "founding ancestor, and a dynasty could be 'cut down' by conquest but survive "
                        "through remnant heirs. The sevenfold Spirit endowment parallels the ANE concept "
                        "of divine gifts bestowed at coronation: Egyptian coronation texts describe the "
                        "gods granting wisdom, power, and authority to the new pharaoh. The animal "
                        "peace vision (11:6-9) echoes the widespread ANE motif of paradise restoration, "
                        "found in Sumerian texts about Dilmun (where the lion does not kill and the "
                        "wolf does not snatch the lamb) and in Egyptian depictions of the 'Field of "
                        "Reeds' where all creatures coexist peacefully.",

        "second_temple": [
            {
                "source": "4QpIsa^a (Pesher on Isaiah, 4Q161)",
                "summary": "The Qumran pesher interprets the 'Branch of David' (netser David) as the "
                           "eschatological messianic king who will defeat the Kittim (Romans) and "
                           "establish righteous rule.",
                "relevance": "The Dead Sea Scrolls community read Isaiah 11 as a prophecy of their "
                             "expected warrior-messiah who would restore Israel's independence."
            },
            {
                "source": "Romans 15:12",
                "summary": "Paul quotes Isaiah 11:10 ('the root of Jesse will come, even he who arises "
                           "to rule the Gentiles; in him will the Gentiles hope') as fulfilled in "
                           "Christ's inclusion of the nations.",
                "relevance": "Paul reads the 'root of Jesse' as Christ, and the Gentile hope of 11:10 "
                             "as the church's mission to the nations."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 6:13", "note": "'The holy seed is its stump' -- the stump of 6:13 sprouts the branch of 11:1", "type": "ot"},
            {"ref": "Isaiah 9:6-7", "note": "The child with four throne names -- the same messianic figure as the branch from Jesse", "type": "ot"},
            {"ref": "Jeremiah 23:5", "note": "'I will raise up for David a righteous Branch (tsemach)' -- the same messianic branch theology", "type": "ot"},
            {"ref": "Revelation 5:5", "note": "'The Lion of the tribe of Judah, the Root of David, has conquered' -- the branch fulfilled in Christ", "type": "nt"},
            {"ref": "Matthew 2:23", "note": "'He shall be called a Nazarene (Natsri)' -- possibly a wordplay on netser ('branch') from 11:1", "type": "nt"},
            {"ref": "Romans 8:19-22", "note": "Creation groaning for liberation -- the cosmic renewal that Isaiah 11:6-9 envisions", "type": "nt"},
            {"ref": "Genesis 1:29-30", "note": "The original Edenic peace among animals -- restored in Isaiah 11:6-9", "type": "ot"}
        ],

        "divine_council_note": "Isaiah 11 presents the messianic king as the Spirit-endowed agent of "
                               "YHWH's cosmic restoration. The sevenfold Spirit (ruach YHWH) that rests "
                               "upon him is the same Spirit that hovered over the waters at creation (Gen "
                               "1:2) and empowered the judges and prophets. The branch from Jesse's stump "
                               "is YHWH's answer to the devastation decreed in chapter 6: the holy seed "
                               "from the stump has become a king who will restore not only Israel but the "
                               "entire created order. The Edenic animal peace (11:6-9) reverses the curse "
                               "of Genesis 3 and anticipates the new creation. The earth 'full of the "
                               "knowledge of YHWH as the waters cover the sea' (11:9) describes a world "
                               "where the divine council's original purpose -- that all creation would "
                               "know YHWH -- is finally achieved. The second exodus (11:11-16) gathers "
                               "the remnant from the nations where they were scattered -- a reversal of "
                               "the Babel dispersion and the Deuteronomy 32 allotment. What was divided "
                               "is reunited under the messianic king who bears YHWH's own Spirit.",

        "sections": [
            {
                "heading": "The Spirit-Endowed Branch (11:1-5)",
                "body": "'There shall come forth a shoot (choter) from the stump (geza) of Jesse, and "
                        "a branch (netser) from his roots shall bear fruit' (11:1). The choice of "
                        "'Jesse' rather than 'David' is significant: the dynasty will be reduced to its "
                        "pre-royal origin, below even the level of David. From this humbled state, new "
                        "life emerges. The Spirit's sevenfold endowment is structured in three pairs "
                        "plus a crown: wisdom (chokmah) and understanding (binah) -- the intellectual "
                        "gifts; counsel (etsah) and might (gevurah) -- the strategic and martial gifts; "
                        "knowledge (da'at) and fear of YHWH (yir'at YHWH) -- the relational and "
                        "devotional gifts. 'His delight (harichoach) shall be in the fear of YHWH' "
                        "(11:3a) -- the messianic king's deepest pleasure is reverence for God. His "
                        "judgment is supernatural: 'He shall not judge by what his eyes see, or decide "
                        "disputes by what his ears hear' (11:3b). Unlike human judges who rely on "
                        "external evidence, this king perceives truth directly. 'With righteousness "
                        "(tsedeq) he shall judge the poor (dallim), and decide with equity (mishor) for "
                        "the meek (anvei-erets) of the earth' (11:4a). The messianic king is the "
                        "champion of the marginalized -- the very injustice condemned in chapter 1 is "
                        "now rectified by the branch's reign. His word is lethal to evil: 'he shall "
                        "strike the earth with the rod of his mouth, and with the breath (ruach) of his "
                        "lips he shall kill the wicked' (11:4b). The messianic king fights not with "
                        "sword but with speech -- his word is the ultimate weapon."
            },
            {
                "heading": "Edenic Peace: The Curse Reversed (11:6-9)",
                "body": "The reign of the branch produces a reversal of the natural order that has "
                        "prevailed since the Fall: 'The wolf shall dwell with the lamb, and the leopard "
                        "shall lie down with the young goat, and the calf and the lion and the fattened "
                        "calf together; and a little child shall lead them' (11:6). The predator-prey "
                        "relationship -- part of the cursed creation since Genesis 3:14-19 -- is "
                        "dissolved. 'The cow and the bear shall graze; their young shall lie down "
                        "together; and the lion shall eat straw like the ox' (11:7) -- a return to the "
                        "pre-Fall vegetarian order of Genesis 1:29-30. The most startling image: 'The "
                        "nursing child shall play over the hole of the cobra, and the weaned child shall "
                        "put his hand on the adder's den' (11:8). The serpent (nachash) that brought "
                        "the curse in Eden is now harmless -- the enmity of Genesis 3:15 is resolved. "
                        "'They shall not hurt or destroy in all my holy mountain' (11:9a) -- the 'holy "
                        "mountain' is Zion, but in this vision it expands to encompass the entire world. "
                        "'For the earth shall be full of the knowledge (de'ah) of YHWH as the waters "
                        "cover the sea' (11:9b). The knowledge of YHWH -- not information about God but "
                        "intimate, experiential communion with God -- saturates the earth as completely "
                        "as water fills the ocean. This is the ultimate vision: not escape from earth "
                        "but earth transformed into Eden."
            }
        ]
    },

    {
        "id": "isa-12",
        "ref": "Isaiah 12",
        "chapter_num": 12,
        "title": "The Song of Salvation: A Doxology of the Redeemed",
        "era": "isaiah_judgment",
        "type": "chapter",

        "synopsis": "Isaiah 12 serves as the closing hymn of the first major section (chs. 1-12), "
                    "forming an inclusio with the judgment oracle of chapter 1. Where chapter 1 opened "
                    "with accusation, chapter 12 closes with praise. The song is structured in two "
                    "stanzas. The first (12:1-3) is individual thanksgiving: 'I will give thanks to "
                    "you, O YHWH, for though you were angry with me, your anger turned away, that you "
                    "might comfort me. Behold, God (El) is my salvation (yeshuati); I will trust, and "
                    "will not be afraid; for YAH, YHWH is my strength and my song, and he has become "
                    "my salvation (yeshu'ah)' (12:1-2). The language deliberately echoes the Song of "
                    "the Sea (Exod 15:2), connecting the future redemption to the original exodus. "
                    "'With joy you will draw water from the wells of salvation (yeshu'ah)' (12:3). "
                    "The second stanza (12:4-6) is communal: 'Give thanks to YHWH, call upon his name, "
                    "make known his deeds among the peoples... Shout, and sing for joy, O inhabitant "
                    "of Zion, for great in your midst is the Holy One of Israel (Qedosh Yisrael)' "
                    "(12:6). The title 'Holy One of Israel,' introduced in the throne vision (6:3), "
                    "bookends the entire section. The threefold-holy God who commissioned Isaiah now "
                    "dwells 'in your midst' (beqirbekh) -- the Immanuel promise fulfilled in worship.",

        "key_verse": {
            "ref": "Isaiah 12:2",
            "text": "Behold, God is my salvation; I will trust, and will not be afraid; for the LORD GOD is my strength and my song, and he has become my salvation.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "yeshu'ah (salvation -- from the same root as Yeshua/Joshua/Jesus)",
            "Yah YHWH (the LORD GOD -- the doubled divine name emphasizing covenant identity)",
            "zimrat (song/strength -- the music of YHWH's people in response to deliverance)",
            "ma'ayanei hayeshu'ah (wells of salvation -- the springs of divine deliverance)",
            "Qedosh Yisrael (Holy One of Israel -- Isaiah's signature title for YHWH)"
        ],

        "ane_backdrop": "Victory songs after divine deliverance are well attested in ANE literature. "
                        "Egyptian hymns to Amun-Re celebrate military victories as divine acts. The "
                        "Moabite Stone (Mesha Stele, ~840 BC) records a king's thanksgiving to his god "
                        "Chemosh for victory. The Israelite tradition roots the practice in the Song of "
                        "the Sea (Exodus 15), the foundational victory hymn. Isaiah 12's deliberate "
                        "echoes of Exodus 15 indicate that the future salvation will be a new exodus -- "
                        "the same God who delivered from Egypt will deliver again.",

        "second_temple": [
            {
                "source": "Mishnah Sukkah 4:9",
                "summary": "During the Feast of Tabernacles (Sukkot), the water-drawing ceremony "
                           "was accompanied by the citation of Isaiah 12:3: 'With joy you will "
                           "draw water from the wells of salvation.'",
                "relevance": "The Second Temple liturgical practice connected Isaiah 12:3 to the "
                             "Sukkot water ceremony, which Jesus would later reference in John 7:37-38."
            },
            {
                "source": "John 7:37-38",
                "summary": "On the last day of Sukkot, Jesus stood and cried out: 'If anyone thirsts, "
                           "let him come to me and drink. Whoever believes in me... out of his heart "
                           "will flow rivers of living water.'",
                "relevance": "Jesus claims to be the fulfillment of the 'wells of salvation' in "
                             "Isaiah 12:3, identifying himself as the source of the living water "
                             "drawn during the Sukkot ceremony."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 15:1-2", "note": "'YHWH is my strength and my song, and he has become my salvation' -- the Song of the Sea, directly quoted in Isaiah 12:2", "type": "ot"},
            {"ref": "Psalm 118:14", "note": "Same exodus hymn quoted: 'The LORD is my strength and my song; he has become my salvation'", "type": "ot"},
            {"ref": "John 7:37-38", "note": "Jesus at Sukkot claiming to be the 'wells of salvation' -- the living water of Isaiah 12:3", "type": "nt"},
            {"ref": "John 4:14", "note": "'The water that I will give him will become in him a spring of water welling up to eternal life' -- the well of salvation personified", "type": "nt"},
            {"ref": "Revelation 7:17", "note": "'The Lamb in the midst of the throne will be their shepherd, and he will guide them to springs of living water'", "type": "nt"}
        ],

        "divine_council_note": "Isaiah 12 completes the arc that began in chapter 1. The riv (lawsuit) "
                               "against Judah reaches its resolution in a song of salvation. The title "
                               "'Holy One of Israel' (Qedosh Yisrael) that defines YHWH's character in the "
                               "throne vision (6:3) now appears as the ground of joy: 'Great in your midst "
                               "is the Holy One of Israel' (12:6). The thrice-holy God who commissioned "
                               "Isaiah from the divine council chamber now dwells among his people. The "
                               "call to 'make known his deeds among the peoples' (12:4) extends beyond "
                               "Israel to the nations -- the same missionary impulse that will culminate "
                               "in the Servant Songs of chapters 42-53. The cosmic scope is unmistakable: "
                               "'Let this be known in all the earth' (12:5). The knowledge of YHWH that "
                               "fills the earth in 11:9 now produces global praise in 12:5.",

        "sections": [
            {
                "heading": "Individual Thanksgiving: El Is My Salvation (12:1-3)",
                "body": "The first stanza is personal: 'You will say in that day: I will give thanks "
                        "to you, O YHWH, for though you were angry with me, your anger turned away, "
                        "that you might comfort me (tenachemeni)' (12:1). The verb nacham ('to comfort') "
                        "anticipates the great comfort oracle of Isaiah 40:1 ('nachamu, nachamu ammi' -- "
                        "'Comfort, comfort my people'). The confession acknowledges both YHWH's righteous "
                        "anger and his gracious restoration. 'Behold, El is my yeshu'ah' (12:2) -- the "
                        "word yeshu'ah ('salvation') shares its root with the name Yeshua (Jesus). Isaiah "
                        "12:2 is a virtual quotation of Exodus 15:2, the Song of the Sea: 'Yah YHWH is "
                        "my strength and my song, and he has become my salvation.' The repetition links "
                        "the future redemption to the original exodus -- the same God, the same power, "
                        "the same song. 'With joy (sasson) you will draw water from the wells of "
                        "salvation' (12:3) -- an image of abundant provision, of salvation available like "
                        "water from a spring."
            },
            {
                "heading": "Communal Praise: Make Known Among the Nations (12:4-6)",
                "body": "The second stanza shifts to communal, universal praise: 'Give thanks to YHWH, "
                        "call upon his name, make known his deeds among the peoples (ba'ammim), declare "
                        "that his name is exalted' (12:4). The mission is proclamation to the nations -- "
                        "the same nations allotted to other elohim in Deuteronomy 32:8-9 must hear of "
                        "YHWH's deeds. 'Sing praises to YHWH, for he has done gloriously; let this be "
                        "known in all the earth' (12:5). 'Shout (tsahali), and sing for joy (ronni), O "
                        "inhabitant of Zion (yoshevet Tsiyon), for great (gadol) in your midst "
                        "(beqirbekh) is the Holy One of Israel (Qedosh Yisrael)' (12:6). The feminine "
                        "singular 'inhabitant of Zion' personifies Jerusalem as a woman -- a beloved "
                        "city whose divine husband dwells within her. The Holy One of Israel is gadol "
                        "('great') in her midst -- the transcendent God is also immanent, present, "
                        "near. This is the final word of the section: not judgment but joy, not "
                        "desolation but divine presence, not exile but the Holy One dwelling among "
                        "his people."
            }
        ]
    }
]
