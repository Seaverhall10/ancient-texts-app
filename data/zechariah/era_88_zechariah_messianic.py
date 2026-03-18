"""
era_88_zechariah_messianic.py -- Zechariah 9-14: The Passion Prophet

The most christologically dense chapters in the Minor Prophets. The triumphal entry
on a donkey (9:9), the thirty pieces of silver (11:12-13), the pierced one (12:10),
the struck shepherd (13:7), and the living waters from Jerusalem (14:8). More of
Zechariah is quoted in the Passion narratives than any OT book except the Psalms.
"""

CHAPTERS = [
    {
        "id": "zechariah-9-10",
        "ref": "Zechariah 9-10",
        "chapter_num": 9,
        "title": "The Coming King -- Humble, Riding on a Donkey",
        "era": "zechariah",
        "type": "chapter",
        "themes": ["SEED", "KING", "NATIONS"],

        "synopsis": "Chapter 9 opens with oracles against the surrounding nations: Damascus, Hamath, Tyre, "
                    "Sidon, and Philistia. YHWH will strip them of their pride and power. Then the stunning "
                    "messianic prophecy (9:9-10): 'Rejoice greatly, O daughter of Zion! Shout aloud, O daughter "
                    "of Jerusalem! Behold, your king is coming to you; righteous and having salvation is he, "
                    "humble and mounted on a donkey, on a colt, the foal of a donkey. I will cut off the chariot "
                    "from Ephraim and the war horse from Jerusalem; and the battle bow shall be cut off, and he "
                    "shall speak peace to the nations. His dominion shall be from sea to sea, and from the River "
                    "to the ends of the earth.' This was fulfilled on Palm Sunday (Matt 21:1-11). The king comes "
                    "not on a war horse but on a donkey -- a beast of peace. His kingdom extends to the ends of "
                    "the earth, achieved not through military conquest but through the word of peace. Chapter 10 "
                    "continues with YHWH's promise to restore Judah and Joseph (the northern tribes). YHWH will "
                    "'whistle for them' and gather them because he has 'compassion on them' (10:6-8).",

        "key_verse": {
            "ref": "Zechariah 9:9",
            "text": "Rejoice greatly, O daughter of Zion! Shout aloud, O daughter of Jerusalem! Behold, your king is coming to you; righteous and having salvation is he, humble and mounted on a donkey, on a colt, the foal of a donkey.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ani ve-rokhev al-chamor (humble and riding on a donkey -- the messianic king's deliberate rejection of military power)",
            "nosha (having salvation/saved -- passive participle; the king is both savior and saved by YHWH)",
            "yedabber shalom la-goyim (he shall speak peace to the nations -- the king's dominion is established by word, not sword)",
            "moshlo mi-yam ad-yam (his dominion from sea to sea -- universal sovereignty; cf. Psalm 72:8)"
        ],

        "ane_backdrop": "In the ancient Near East, kings rode horses or chariots in military contexts and donkeys "
                        "in peaceful/diplomatic contexts. Solomon rode David's mule to his coronation (1 Kings 1:33). "
                        "Zechariah's king rides a donkey -- announcing peace, not war. This was culturally legible: "
                        "the king comes as a peacemaker.",

        "second_temple": [
            {
                "source": "Matthew 21:1-11",
                "summary": "Jesus enters Jerusalem on a donkey, and the crowds shout 'Hosanna to the Son of David!'",
                "relevance": "Matthew explicitly cites Zechariah 9:9 as fulfilled in the triumphal entry. "
                             "Jesus deliberately arranges the donkey to enact Zechariah's prophecy."
            },
            {
                "source": "John 12:14-16",
                "summary": "Jesus finds a young donkey and sits on it, 'as it is written.'",
                "relevance": "John notes that the disciples understood the Zechariah connection only after "
                             "Jesus was glorified."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 49:10-11", "note": "The Shiloh prophecy: 'binding his foal to the vine' -- the donkey imagery of the messianic king", "type": "ot"},
            {"ref": "1 Kings 1:33", "note": "Solomon riding David's mule to his coronation -- the royal donkey tradition", "type": "ot"},
            {"ref": "Psalm 72:8", "note": "'May he have dominion from sea to sea' -- the universal reign Zechariah echoes", "type": "ot"},
            {"ref": "Isaiah 9:6-7", "note": "The Prince of Peace whose government increases without end", "type": "ot"},
            {"ref": "Matthew 21:1-11", "note": "The triumphal entry -- direct fulfillment of Zechariah 9:9", "type": "nt"},
            {"ref": "John 12:14-16", "note": "Jesus on the donkey -- John's citation of Zechariah 9:9", "type": "nt"}
        ],

        "divine_council_note": "Zechariah 9:9-10 presents the divine council's messianic decree in its most "
                               "counter-cultural form. Ancient Near Eastern divine council decrees typically "
                               "installed kings through military victory. YHWH's king comes humble and on a "
                               "donkey. The dismantling of war machinery -- 'I will cut off the chariot... the "
                               "war horse... the battle bow' -- is the divine council sovereign restructuring "
                               "how kingship operates. The king's dominion 'from sea to sea' is achieved by "
                               "speaking peace, not waging war. This is the divine council's ultimate subversion "
                               "of human power structures.",

        "sections": [
            {
                "heading": "Oracles Against the Nations (9:1-8)",
                "body": "Damascus, Hamath, Tyre, Sidon, and Philistia face judgment. Tyre's wealth and "
                        "fortifications will be consumed. Philistia's pride will be cut off. But YHWH will "
                        "protect his house: 'No oppressor shall again march over them, for now I see with "
                        "my own eyes' (9:8)."
            },
            {
                "heading": "The Coming King on a Donkey (9:9-10)",
                "body": "The messianic prophecy: Zion's king comes righteous, saved, humble, on a donkey. "
                        "War machinery is abolished. He speaks peace to the nations. His dominion is universal. "
                        "Fulfilled on Palm Sunday when Jesus rode into Jerusalem on a donkey's colt."
            },
            {
                "heading": "Restoration of Judah and Joseph (9:11-10:12)",
                "body": "YHWH will free prisoners from the 'waterless pit' by the blood of the covenant (9:11). "
                        "He will restore both Judah and the northern tribes. YHWH has compassion and will "
                        "gather them as though they had never been rejected. 'I will whistle for them and "
                        "gather them in' (10:8). The shepherdless condition of the people (10:2-3) prepares "
                        "for the shepherd imagery of chapters 11 and 13."
            }
        ]
    },

    {
        "id": "zechariah-11",
        "ref": "Zechariah 11",
        "chapter_num": 11,
        "title": "The Rejected Shepherd and the Thirty Pieces of Silver",
        "era": "zechariah",
        "type": "chapter",
        "themes": ["SEED", "BLOOD", "COV"],

        "synopsis": "One of the most enigmatic and christologically dense chapters in the OT. Zechariah enacts "
                    "a prophetic drama as a shepherd. He takes two staffs named 'Favor' (grace) and 'Union' "
                    "(brotherhood) and shepherds the flock. He becomes impatient with the sheep, and they "
                    "detest him. He breaks the staff 'Favor,' annulling the covenant. Then: 'I said to them, "
                    "If it seems good to you, give me my wages; but if not, keep them. And they weighed out as "
                    "my wages thirty pieces of silver. Then YHWH said to me, Throw it to the potter -- the "
                    "lordly price at which I was priced by them. So I took the thirty pieces of silver and "
                    "threw them into the house of YHWH, to the potter' (11:12-13). The price of a gored slave "
                    "(Exod 21:32) is the value placed on YHWH's shepherd -- the ultimate insult. He breaks the "
                    "second staff 'Union,' dissolving the brotherhood between Judah and Israel. A foolish "
                    "shepherd will replace the rejected one -- a worthless leader who cares nothing for the flock.",

        "key_verse": {
            "ref": "Zechariah 11:12-13",
            "text": "Then I said to them, 'If it seems good to you, give me my wages; but if not, keep them.' And they weighed out as my wages thirty pieces of silver. Then the LORD said to me, 'Throw it to the potter' -- the lordly price at which I was priced by them. So I took the thirty pieces of silver and threw them into the house of the LORD, to the potter.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "sheloshim kasef (thirty of silver -- the price of a gored slave in Exodus 21:32; an insultingly low valuation)",
            "ha-yotser (the potter -- the destination for the silver; Matt 27:7 records Judas' silver buying the 'potter's field')",
            "no'am (Favor/Grace -- the first staff, representing YHWH's gracious covenant with the nations; broken)",
            "chovlim (Union/Binders -- the second staff, representing brotherhood between Judah and Israel; broken)"
        ],

        "ane_backdrop": "Thirty pieces of silver was the standard compensation for a slave gored by an ox "
                        "(Exod 21:32). As the price placed on YHWH's shepherd, it is deliberately insulting -- "
                        "the people value their divinely appointed shepherd at slave price. The prophetic "
                        "sign-act of breaking staffs was a visible enacted prophecy: the audience sees the "
                        "covenant dissolution happening before their eyes.",

        "second_temple": [
            {
                "source": "Matthew 27:3-10",
                "summary": "Judas returns the thirty pieces of silver, which are used to buy the potter's field.",
                "relevance": "Matthew explicitly cites Zechariah 11:12-13 (attributed to Jeremiah in Matt 27:9, "
                             "possibly because Jeremiah's scroll stood first in the prophetic collection). "
                             "Every detail -- thirty silver pieces, the Temple, the potter -- is fulfilled in "
                             "Judas' betrayal and its aftermath."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 21:32", "note": "Thirty shekels of silver -- the price of a gored slave; the insult price for YHWH's shepherd", "type": "ot"},
            {"ref": "Jeremiah 19:1-11", "note": "Jeremiah's potter imagery -- possibly why Matthew attributes the quote to Jeremiah", "type": "ot"},
            {"ref": "Ezekiel 34:1-10", "note": "The worthless shepherds of Israel -- the same 'foolish shepherd' tradition", "type": "ot"},
            {"ref": "Matthew 26:14-16", "note": "Judas agrees to betray Jesus for thirty pieces of silver", "type": "nt"},
            {"ref": "Matthew 27:3-10", "note": "The thirty pieces returned, the potter's field purchased -- fulfilling Zechariah 11:12-13", "type": "nt"}
        ],

        "divine_council_note": "Zechariah 11 presents the divine council's shocking scenario: YHWH's appointed "
                               "shepherd is valued at slave price and rejected. The breaking of the staffs is "
                               "a divine council decree enacted on earth: 'Favor' (the covenant with the nations) "
                               "is annulled, and 'Union' (the brotherhood of Israel) is dissolved. The 'thirty "
                               "pieces of silver' is the price the people set on YHWH himself -- 'the lordly "
                               "price at which I was priced by them.' YHWH speaks in the first person: the "
                               "shepherd is YHWH's representative, and the insult to the shepherd is an insult "
                               "to YHWH. This is fulfilled in the Passion when Judas betrays Jesus -- the divine "
                               "council sovereign incarnate -- for thirty silver coins.",

        "sections": [
            {
                "heading": "The Shepherd's Two Staffs (11:1-6)",
                "body": "Lebanon's cedars, Bashan's oaks, and Jordan's thickets wail -- judgment is coming. "
                        "YHWH commands Zechariah to shepherd the flock 'doomed to slaughter.' He takes two "
                        "staffs: 'Favor' and 'Union.' The stage is set for a prophetic sign-act."
            },
            {
                "heading": "Rejection and the Thirty Pieces (11:7-14)",
                "body": "Zechariah shepherds the flock but becomes 'impatient with them, and they also "
                        "detested me.' He breaks 'Favor,' annulling the covenant. He asks for wages and "
                        "receives thirty pieces of silver -- slave price. YHWH orders: 'Throw it to the "
                        "potter.' The silver goes into the Temple, to the potter. Every detail is fulfilled "
                        "in Matthew 27."
            },
            {
                "heading": "The Foolish Shepherd (11:15-17)",
                "body": "YHWH commands Zechariah to take the equipment of a 'foolish shepherd' -- a worthless "
                        "leader who does not care for the sheep. He does not heal the maimed, nourish the "
                        "healthy, or seek the lost. 'Woe to my worthless shepherd!' His arm and right eye "
                        "will be destroyed. The rejected good shepherd is replaced by a worthless one -- "
                        "the pattern of Israel's leadership failure."
            }
        ]
    },

    {
        "id": "zechariah-12-13",
        "ref": "Zechariah 12-13",
        "chapter_num": 12,
        "title": "The Pierced One -- They Shall Look on Me Whom They Have Pierced",
        "era": "zechariah",
        "type": "chapter",
        "themes": ["SEED", "BLOOD", "SPIRIT", "DC"],

        "synopsis": "Chapters 12-13 contain the most christologically explosive verses in Zechariah. YHWH "
                    "declares that Jerusalem will be 'a cup of staggering to all the surrounding peoples' "
                    "(12:2) and 'a heavy stone for all the peoples' (12:3). All nations will be gathered "
                    "against Jerusalem, but YHWH will defend it. Then the astonishing oracle: 'And I will pour "
                    "out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for "
                    "mercy, so that, when they look on me, on him whom they have pierced, they shall mourn for "
                    "him, as one mourns for an only child' (12:10). YHWH speaks: 'they look on ME, whom they "
                    "have pierced' -- YHWH himself is the pierced one. Yet 'they mourn for HIM' -- suggesting "
                    "a distinction within the Godhead. Chapter 13 opens with a fountain for cleansing sin. Then "
                    "the struck shepherd: 'Strike the shepherd, and the sheep will be scattered; I will turn my "
                    "hand against the little ones' (13:7). YHWH calls this shepherd 'the man who stands next to "
                    "me' (amiti -- 'my associate, my fellow, my equal'). Two-thirds will be cut off, but one-third "
                    "will be refined through fire: 'I will say, They are my people; and they will say, YHWH is "
                    "my God' (13:9).",

        "key_verse": {
            "ref": "Zechariah 12:10",
            "text": "And I will pour out on the house of David and the inhabitants of Jerusalem a spirit of grace and pleas for mercy, so that, when they look on me, on him whom they have pierced, they shall mourn for him, as one mourns for an only child, and weep bitterly over him, as one weeps over a firstborn.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "vehibbitu elai et asher-daqaru (they shall look on me, whom they have pierced -- YHWH speaks of himself as pierced; fulfilled at the cross)",
            "ruach chen vetachanunim (spirit of grace and pleas for mercy -- the Holy Spirit poured out to produce repentance)",
            "amiti (my associate/fellow/equal -- YHWH calls the shepherd 'the man who stands next to me'; a divine council term of intimate proximity)",
            "hakh et ha-ro'eh (strike the shepherd -- the divine command to smite YHWH's own shepherd; quoted by Jesus at Gethsemane)"
        ],

        "ane_backdrop": "Mourning for an only child or firstborn was the most intense form of grief in the "
                        "ancient Near East. The combination of national mourning with the piercing of a divine "
                        "figure is unique in ancient literature. The 'fountain opened for sin and uncleanness' "
                        "(13:1) connects to ritual purification traditions but transcends them with permanent "
                        "cleansing.",

        "second_temple": [
            {
                "source": "John 19:34-37",
                "summary": "A soldier pierces Jesus' side, and blood and water flow out. John cites: 'They "
                           "will look on him whom they have pierced.'",
                "relevance": "John explicitly identifies Jesus on the cross as the fulfillment of Zechariah "
                             "12:10. The pierced one is YHWH incarnate."
            },
            {
                "source": "Matthew 26:31",
                "summary": "Jesus says to his disciples: 'You will all fall away because of me this night. "
                           "For it is written, I will strike the shepherd, and the sheep will be scattered.'",
                "relevance": "Jesus directly quotes Zechariah 13:7, identifying himself as the struck shepherd "
                             "and his disciples as the scattered sheep."
            },
            {
                "source": "Revelation 1:7",
                "summary": "'Behold, he is coming with the clouds, and every eye will see him, even those who "
                           "pierced him, and all tribes of the earth will wail on account of him.'",
                "relevance": "Revelation combines Daniel 7:13 and Zechariah 12:10 -- the pierced one returns "
                             "in glory, and the whole earth mourns."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 53:5", "note": "'He was pierced for our transgressions' -- Isaiah's suffering servant and Zechariah's pierced one converge", "type": "ot"},
            {"ref": "Psalm 22:16", "note": "'They have pierced my hands and my feet' -- the suffering psalms and Zechariah's piercing", "type": "ot"},
            {"ref": "John 19:34-37", "note": "The soldier pierces Jesus' side -- John cites Zechariah 12:10 as fulfilled", "type": "nt"},
            {"ref": "Matthew 26:31", "note": "Jesus quotes Zechariah 13:7 at Gethsemane: 'Strike the shepherd, the sheep will scatter'", "type": "nt"},
            {"ref": "Revelation 1:7", "note": "'Every eye will see him, even those who pierced him' -- combining Daniel 7 and Zechariah 12", "type": "nt"}
        ],

        "divine_council_note": "Zechariah 12:10 is one of the most significant divine council Christology texts "
                               "in the OT. YHWH speaks in the first person: 'they look on ME, whom they have "
                               "pierced.' Yet the verse shifts to third person: 'they mourn for HIM as for an "
                               "only child.' This me-him shift reflects the 'two powers in heaven' theology: "
                               "YHWH is both the transcendent God and the visible, pierceable figure. The divine "
                               "council sovereign takes on a form that can be wounded. John 19:37 identifies "
                               "this as Jesus on the cross -- God incarnate, pierced.\n\n"
                               "Zechariah 13:7 deepens the mystery: YHWH calls the struck shepherd 'the man "
                               "who stands next to me' (amiti). The Hebrew amith means 'associate, fellow, "
                               "one who is an equal.' This is not a mere servant but one who stands in YHWH's "
                               "intimate circle -- a divine council peer. YHWH commands the striking of his "
                               "own associate. Jesus quotes this verse at Gethsemane (Matt 26:31), identifying "
                               "himself as the shepherd-associate of YHWH who is struck by divine decree for "
                               "the sake of the flock.",

        "sections": [
            {
                "heading": "Jerusalem: Cup of Staggering, Heavy Stone (12:1-9)",
                "body": "YHWH declares Jerusalem will be a trap for all nations that attack it. On that day, "
                        "YHWH will make the clans of Judah 'like a blazing pot among sheaves' and 'like a "
                        "flaming torch among sheaves.' He will defend Jerusalem and strengthen even the "
                        "feeblest among them to be 'like David.'"
            },
            {
                "heading": "They Shall Look on Me Whom They Have Pierced (12:10-14)",
                "body": "The Spirit of grace is poured out. They look on YHWH, whom they have pierced, and "
                        "mourn as for an only child. The mourning is detailed: the house of David mourns "
                        "separately, the house of Nathan, Levi, the Shimeites -- every family apart with "
                        "their wives. The grief is universal and deeply personal. Fulfilled at the cross and "
                        "anticipated in the final coming (Rev 1:7)."
            },
            {
                "heading": "The Fountain, the Shepherd, the Refining (13:1-9)",
                "body": "A fountain for sin opens on that day. Idols and false prophets will be removed. Then "
                        "the terrible command: 'Strike the shepherd, and the sheep will be scattered.' YHWH "
                        "calls this shepherd 'my associate' (amiti) -- one who stands in his intimate presence. "
                        "Two-thirds will be cut off, one-third refined. The remnant covenant: 'They are my "
                        "people'; 'YHWH is my God.' Jesus quotes 13:7 at Gethsemane."
            }
        ]
    },

    {
        "id": "zechariah-14",
        "ref": "Zechariah 14",
        "chapter_num": 14,
        "title": "The Day of YHWH -- Living Waters and Universal Kingship",
        "era": "zechariah",
        "type": "chapter",
        "themes": ["KING", "DC", "NATIONS", "HOLY"],

        "synopsis": "The grand finale of Zechariah's prophecy and one of the most eschatological chapters in "
                    "the OT. 'A day is coming for YHWH' (14:1) -- all nations will be gathered against Jerusalem. "
                    "The city will be taken, but then 'YHWH will go out and fight against those nations as when "
                    "he fights on a day of battle' (14:3). His feet will stand on the Mount of Olives, which will "
                    "split in two (14:4). 'YHWH my God will come, and all the holy ones with him' (14:5) -- the "
                    "divine council host accompanies YHWH's theophany. On that day there will be 'neither cold "
                    "nor frost,' continuous light without the cycle of day and night. 'Living waters shall flow "
                    "out from Jerusalem, half of them to the eastern sea and half to the western sea' (14:8). "
                    "'And YHWH will be king over all the earth. On that day YHWH will be one and his name one' "
                    "(14:9). The nations that attacked Jerusalem will suffer plague, then the survivors will come "
                    "up year after year to worship YHWH at the Feast of Booths. Even the horses' bells will be "
                    "inscribed 'Holy to YHWH,' and every pot in Jerusalem will be holy -- the entire city becomes "
                    "a temple.",

        "key_verse": {
            "ref": "Zechariah 14:8-9",
            "text": "On that day living waters shall flow out from Jerusalem, half of them to the eastern sea and half of them to the western sea. It shall continue in summer as in winter. And the LORD will be king over all the earth. On that day the LORD will be one and his name one.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "mayim chayyim (living waters -- fresh, flowing water from Jerusalem; the source of life for the whole earth)",
            "YHWH echad u-shmo echad (YHWH will be one and his name one -- echoing the Shema; the final unification of all worship under YHWH)",
            "qadosh la-YHWH (holy to YHWH -- inscribed on horse bells and cooking pots; the entire city becomes sacred space)",
            "kedoshim (holy ones -- the divine council host accompanying YHWH at his coming)"
        ],

        "ane_backdrop": "The Mount of Olives splitting echoes ancient Near Eastern theophanic traditions where "
                        "mountains tremble and break at the appearance of a deity. The river flowing from the "
                        "temple is paralleled in Ezekiel 47:1-12 and connects to Eden's river (Gen 2:10-14). "
                        "The universal pilgrimage to Jerusalem for the Feast of Booths reflects the ancient "
                        "expectation that the nations would ultimately worship at YHWH's mountain.",

        "second_temple": [
            {
                "source": "John 7:37-38",
                "summary": "Jesus cries: 'If anyone thirsts, let him come to me and drink. Whoever believes "
                           "in me, as the Scripture has said, Out of his heart will flow rivers of living water.'",
                "relevance": "Jesus identifies himself as the source of living waters -- the fulfillment of "
                             "Zechariah 14:8's eschatological river."
            },
            {
                "source": "Acts 1:11-12",
                "summary": "'This Jesus, who was taken up from you into heaven, will come in the same way as "
                           "you saw him go into heaven.' Then they returned from the Mount of Olives.",
                "relevance": "Jesus ascends from the Mount of Olives and will return there -- fulfilling "
                             "Zechariah 14:4 where YHWH's feet stand on the Mount of Olives."
            },
            {
                "source": "Revelation 22:1-5",
                "summary": "The river of the water of life flowing from the throne of God and of the Lamb.",
                "relevance": "Revelation's river of life draws on both Ezekiel 47 and Zechariah 14:8 -- "
                             "living waters flowing from God's presence to heal the nations."
            }
        ],

        "cross_refs": [
            {"ref": "Ezekiel 47:1-12", "note": "The river flowing from the Temple -- the same eschatological river as Zechariah 14:8", "type": "ot"},
            {"ref": "Genesis 2:10-14", "note": "Eden's river -- the original living water; Zechariah envisions its eschatological return", "type": "ot"},
            {"ref": "Deuteronomy 6:4", "note": "The Shema: 'YHWH our God, YHWH is one' -- echoed in 'YHWH will be one and his name one'", "type": "ot"},
            {"ref": "Joel 3:18", "note": "'A fountain shall come forth from the house of YHWH' -- Joel's parallel river promise", "type": "ot"},
            {"ref": "Acts 1:11-12", "note": "Jesus will return to the Mount of Olives -- fulfilling Zechariah 14:4", "type": "nt"},
            {"ref": "John 7:37-38", "note": "Jesus as the source of living water -- fulfilling Zechariah 14:8", "type": "nt"},
            {"ref": "Revelation 22:1-5", "note": "The river of life from the throne -- the final fulfillment of Zechariah's living waters", "type": "nt"}
        ],

        "divine_council_note": "Zechariah 14 is the climactic divine council theophany. YHWH comes with 'all "
                               "the holy ones' (14:5) -- the kedoshim, the divine council host. His feet stand "
                               "on the Mount of Olives -- the divine council sovereign makes physical contact "
                               "with earth, splitting the mountain. The living waters flowing from Jerusalem "
                               "represent Eden restored -- the divine council's garden, where God dwelt with "
                               "his creatures, is re-established. 'YHWH will be king over all the earth' (14:9) "
                               "is the divine council's ultimate decree: the allotment of the nations to the "
                               "sons of God (Deut 32:8-9) is superseded by YHWH's direct universal kingship. "
                               "'YHWH will be one and his name one' -- no more rival gods, no more competing "
                               "council members. The entire city becomes 'Holy to YHWH' -- the sacred/profane "
                               "distinction dissolves because all creation becomes the divine council throne room.",

        "sections": [
            {
                "heading": "The Nations Attack, YHWH Defends (14:1-5)",
                "body": "All nations gather against Jerusalem. The city is taken, but then YHWH goes out to "
                        "fight. His feet stand on the Mount of Olives, splitting it east to west. A great "
                        "valley opens for escape. 'YHWH my God will come, and all the holy ones with him' -- "
                        "the divine council host accompanies the theophany. Fulfilled preliminarily in the "
                        "ascension/return from the Mount of Olives (Acts 1:11-12)."
            },
            {
                "heading": "Living Waters and Universal Kingship (14:6-11)",
                "body": "On that day: continuous light, no more cold or frost. Living waters flow from Jerusalem "
                        "to the eastern sea (Dead Sea) and western sea (Mediterranean) year-round. 'YHWH will "
                        "be king over all the earth. On that day YHWH will be one and his name one.' Jerusalem "
                        "will be elevated and inhabited in security."
            },
            {
                "heading": "The Plague, the Feast, and the Holy City (14:12-21)",
                "body": "The nations that attacked Jerusalem suffer plague. Their survivors come annually to "
                        "worship at the Feast of Booths. Those who refuse receive no rain. 'Holy to YHWH' -- "
                        "the high priest's turban inscription (Exod 28:36) -- will be engraved on horse bells "
                        "and cooking pots. Every vessel in Jerusalem will be holy. The sacred/profane distinction "
                        "dissolves. There will be no more traders in the house of YHWH. The entire city becomes "
                        "a temple."
            }
        ]
    }
]
