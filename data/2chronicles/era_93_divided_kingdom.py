"""
era_93_divided_kingdom.py -- Divided Kingdom (2 Chronicles 10-28)

After Solomon's death, the kingdom divides. The Chronicler's treatment of this
period is radically different from Kings: the northern kingdom barely exists in
his narrative. His focus is Judah -- specifically, how each Judahite king relates
to the temple and to YHWH. The theological formula repeats: faithfulness brings
blessing, unfaithfulness brings judgment. This section contains the magnificent
divine council scene of Micaiah's vision (2 Chr 18:18-22), where YHWH's throne
room is opened and a lying spirit is commissioned to deceive Ahab.
"""

CHAPTERS = [
    {
        "id": "2chr-10-16",
        "ref": "2 Chronicles 10-16",
        "chapter_num": 1,
        "title": "Rehoboam to Asa: Division, Faithfulness, and the Seeking Formula",
        "era": "divided_kingdom",
        "type": "chapter",

        "synopsis": "The kingdom divides when Rehoboam follows foolish counsel and rejects the "
                    "northern tribes' plea for lighter burdens (ch. 10). The Chronicler attributes "
                    "the division to divine plan: 'It was a turn of affairs brought about by God' "
                    "(10:15). Rehoboam's early faithfulness gives way to unfaithfulness: 'When the "
                    "rule of Rehoboam was established and he was strong, he abandoned the law of "
                    "the LORD, and all Israel with him' (12:1). Shishak of Egypt invades as judgment "
                    "(ch. 12). Abijah delivers a remarkable speech defending the legitimacy of Judah's "
                    "worship against the north's apostasy (ch. 13). Asa initiates a major religious "
                    "reform, removes idols, and leads a national covenant renewal: 'They entered into "
                    "a covenant to seek the LORD, the God of their fathers, with all their heart and "
                    "with all their soul' (15:12). But Asa's later years bring failure: he relies on "
                    "Aram rather than YHWH (16:7) and persecutes the prophet who rebukes him.",

        "key_verse": {
            "ref": "2 Chronicles 15:2",
            "text": "The LORD is with you while you are with him. If you seek him, he will be found by you, but if you forsake him, he will forsake you.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "darash (to seek -- the defining verb of the Chronicler's theology; kings and people who 'seek' YHWH prosper; those who do not are punished)",
            "azav (to forsake/abandon -- the opposite of darash; when Israel 'forsakes' YHWH, he 'forsakes' them; the covenant is bilateral)",
            "sibbah me-elohim (a turn of affairs from God -- the divine causation behind the political division; YHWH orchestrates historical events)",
            "ma'al (breach of faith -- the Chronicler's characteristic word for covenant infidelity; Rehoboam's defining failure)"
        ],

        "ane_backdrop": "Political divisions of kingdoms after the death of a strong king are common in "
                        "ANE history. The Egyptian Third Intermediate Period saw Egypt fragment into "
                        "competing dynasties after the fall of the New Kingdom. The neo-Assyrian empire "
                        "experienced provincial breakaways during transitions. The Chronicler's unique "
                        "contribution is the theological interpretation: the division is not merely "
                        "political failure but divine action. Shishak's invasion (2 Chr 12) is confirmed "
                        "by his triumphal relief at Karnak, listing over 150 conquered cities in Israel "
                        "and Judah -- one of the most important extra-biblical confirmations of the "
                        "biblical narrative.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities 8.247-253",
                "summary": "Josephus retells the kingdom division, attributing Rehoboam's folly to "
                           "divine judgment for Solomon's sins -- bridging the material the Chronicler "
                           "omits with the Chronicler's own theological framework.",
                "relevance": "Shows how later tradition combined Kings' and Chronicles' perspectives."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 12:1-24", "note": "The parallel account of the kingdom division -- Chronicles adds Abijah's speech and emphasizes the religious dimension", "type": "ot"},
            {"ref": "1 Kings 14:25-28", "note": "Shishak's invasion in Kings -- Chronicles adds the prophetic explanation (2 Chr 12:5-8)", "type": "ot"},
            {"ref": "Deuteronomy 4:29", "note": "'You will seek the LORD your God and you will find him, if you search after him with all your heart' -- the theological foundation for Azariah's prophecy in 2 Chr 15:2", "type": "ot"},
            {"ref": "Jeremiah 29:13-14", "note": "'You will seek me and find me, when you seek me with all your heart' -- the same seeking theology", "type": "ot"},
            {"ref": "James 4:8", "note": "'Draw near to God, and he will draw near to you' -- NT restatement of the Chronicler's bilateral seeking principle", "type": "nt"}
        ],

        "divine_council_note": "The Chronicler's interpretation of the kingdom division as 'a turn of affairs "
                               "brought about by God' (sibbah me-elohim, 10:15) places the event within the "
                               "divine council's governance of history. YHWH does not merely permit the division "
                               "-- he orchestrates it. This is consistent with the divine council pattern where "
                               "historical events are decreed in the heavenly assembly and executed through human "
                               "agents. Rehoboam's foolish counselors are the instruments of a divine decision.",

        "sections": [
            {
                "heading": "The Kingdom Divides: A Turn of Affairs from God (2 Chr 10:1-11:23)",
                "body": "Rehoboam goes to Shechem where 'all Israel' has gathered to make him king (10:1). "
                        "The people, led by Jeroboam, ask for lighter burdens. Rehoboam consults the elders "
                        "(who advise concession) and then the young men (who advise escalation). He follows "
                        "the young men: 'My father made your yoke heavy, but I will add to it. My father "
                        "disciplined you with whips, but I will discipline you with scorpions' (10:11). The "
                        "Chronicler adds the theological interpretation: 'It was a turn of affairs brought "
                        "about by God, that the LORD might fulfill his word spoken by Ahijah the Shilonite' "
                        "(10:15). The ten northern tribes depart. The Chronicler then notes that the Levites "
                        "throughout the north migrate south to Judah (11:13-17), because Jeroboam 'cast them "
                        "out from serving as priests of the LORD' (11:14). This Levitical migration strengthens "
                        "Judah as the legitimate worship center."
            },
            {
                "heading": "Shishak's Invasion and Rehoboam's Partial Repentance (2 Chr 12:1-16)",
                "body": "After Rehoboam 'abandoned the law of the LORD' (12:1), Shishak of Egypt invades with "
                        "'1,200 chariots and 60,000 horsemen' (12:3). The prophet Shemaiah delivers the "
                        "theological verdict: 'You abandoned me, so I have abandoned you to the hand of "
                        "Shishak' (12:5). The bilateral nature of the covenant is stark: abandonment begets "
                        "abandonment. But Rehoboam and the princes humble themselves (kanaf, 12:6), and YHWH's "
                        "response through Shemaiah is immediate: 'They have humbled themselves. I will not "
                        "destroy them, but I will grant them some deliverance' (12:7). The Chronicler's "
                        "theology in miniature: unfaithfulness brings judgment, repentance brings measured "
                        "mercy. Shishak plunders the temple treasures but does not destroy Jerusalem. The "
                        "final verdict on Rehoboam: 'He did evil, for he did not set his heart to seek the "
                        "LORD' (12:14) -- the 'seeking' verb (darash) again."
            },
            {
                "heading": "Abijah's Theological Speech and Asa's Reform (2 Chr 13-16)",
                "body": "Abijah (called Abijam in Kings) delivers a speech that is entirely unique to "
                        "Chronicles -- the Chronicler's theological defense of Judah's legitimacy. Standing "
                        "on Mount Zemaraim, Abijah addresses the northern army: 'Do you not know that the "
                        "LORD God of Israel gave the kingship over Israel forever to David and his sons by "
                        "a covenant of salt?' (13:5). He argues that the north has rejected the Davidic "
                        "covenant, the Levitical priesthood, and the temple -- and has set up golden calves "
                        "instead (13:8-9). Asa then carries out a major reform (ch. 14-15), including a "
                        "covenant renewal ceremony where the people vow 'to seek the LORD, the God of their "
                        "fathers, with all their heart and with all their soul' (15:12). Asa's tragedy is "
                        "that he starts well but finishes poorly: in his old age, he relies on Aram rather "
                        "than YHWH and imprisons the prophet Hanani who rebukes him. Even his illness -- "
                        "'yet even in his disease he did not seek the LORD, but sought help from physicians' "
                        "(16:12) -- is cast in the Chronicler's seeking/forsaking framework."
            }
        ]
    },

    {
        "id": "2chr-17-23",
        "ref": "2 Chronicles 17-23",
        "chapter_num": 2,
        "title": "Jehoshaphat, Micaiah's Vision, and Athaliah: Council and Conflict",
        "era": "divided_kingdom",
        "type": "chapter",

        "synopsis": "Jehoshaphat is one of the Chronicler's model kings: he 'sought the God of his "
                    "father' (17:4), sent Levites throughout Judah to teach the law (17:7-9), and "
                    "established a judicial system grounded in YHWH's justice (19:5-7). But his "
                    "alliance with Ahab of Israel produces the stunning divine council scene of "
                    "chapter 18: Micaiah's vision of YHWH on his throne, deliberating with the host "
                    "of heaven over Ahab's fate. Jehoshaphat's prayer before the battle against Moab "
                    "and Ammon (ch. 20) is a model of faith in crisis: 'We do not know what to do, "
                    "but our eyes are on you' (20:12). The answer comes through a Levite: 'Do not be "
                    "afraid... for the battle is not yours but God's' (20:15). After Jehoshaphat, his "
                    "son Jehoram (ch. 21) and grandson Ahaziah (ch. 22) bring disaster through "
                    "alliance with Ahab's house. Athaliah, Ahab's daughter, seizes the throne and "
                    "nearly extinguishes the Davidic line (22:10-12), until the priest Jehoiada "
                    "engineers the coronation of young Joash (ch. 23).",

        "key_verse": {
            "ref": "2 Chronicles 18:18",
            "text": "I saw the LORD sitting on his throne, and all the host of heaven standing on his right hand and on his left.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "kol-tseva hashamayim (all the host of heaven -- the divine council assembled around YHWH's throne; the spiritual beings who serve in the heavenly administration)",
            "ruach (spirit -- the spirit who volunteers to be a lying spirit in the prophets' mouths; a divine council agent commissioned for a specific mission)",
            "darash (to seek -- Jehoshaphat 'sought' YHWH and prospered; the recurring verb of faithfulness)",
            "lo yada'nu mah-na'aseh (we do not know what to do -- Jehoshaphat's prayer of total dependence; the honest confession that precedes divine intervention)"
        ],

        "ane_backdrop": "Micaiah's vision (2 Chr 18:18-22) is the clearest biblical window into the "
                        "divine council's deliberative process. The council assembly -- YHWH on his throne, "
                        "the host of heaven standing around him, deliberation over a specific question, a "
                        "spirit volunteering for a mission -- parallels the council scenes in Ugaritic "
                        "literature: El presides over the assembly of the gods (phr ilm), divine messengers "
                        "are dispatched with specific mandates, and lower deities carry out the council's "
                        "decrees. The key difference: in the Ugaritic texts, the high god is sometimes "
                        "overruled or manipulated by other deities; in Micaiah's vision, YHWH is the "
                        "unchallenged sovereign who authorizes the lying spirit's mission. No spirit acts "
                        "without his permission.",

        "second_temple": [
            {
                "source": "1 Enoch 14-16",
                "summary": "Enoch ascends to the divine throne room and sees God seated on his throne "
                           "of glory, surrounded by myriads of holy ones. The vision parallels Micaiah's "
                           "in its depiction of the heavenly court.",
                "relevance": "The Enochic throne room vision belongs to the same tradition as Micaiah's -- "
                             "both depict the divine council assembled before YHWH's throne for deliberation "
                             "and decree."
            },
            {
                "source": "Job 1:6-12; 2:1-6",
                "summary": "The sons of God (benei ha-elohim) present themselves before YHWH, and the "
                           "satan among them. YHWH authorizes the satan's testing of Job within set limits.",
                "relevance": "The same divine council pattern as 2 Chr 18: spiritual beings present themselves "
                             "before YHWH, a specific agent receives a specific commission, and YHWH sets the "
                             "boundaries of the mission."
            }
        ],

        "cross_refs": [
            {"ref": "1 Kings 22:1-40", "note": "The parallel account of Micaiah's vision and Ahab's death -- virtually identical in both texts", "type": "ot"},
            {"ref": "Job 1:6-12", "note": "The divine council scene in Job: the sons of God present themselves before YHWH, the satan among them -- the same assembly Micaiah sees", "type": "ot"},
            {"ref": "Isaiah 6:1-8", "note": "Isaiah's vision of YHWH on his throne, the seraphim, and the divine commission 'Whom shall I send?' -- another divine council commissioning scene", "type": "ot"},
            {"ref": "Psalm 82:1", "note": "'God has taken his place in the divine council; in the midst of the gods he holds judgment' -- the theological framework for Micaiah's vision", "type": "ot"},
            {"ref": "1 Timothy 4:1", "note": "'The Spirit expressly says that in later times some will depart from the faith, devoting themselves to deceitful spirits' -- the NT awareness of deceiving spirits operating under divine permission", "type": "nt"},
            {"ref": "2 Thessalonians 2:11", "note": "'God sends them a strong delusion, so that they may believe what is false' -- the same theology as YHWH authorizing the lying spirit in 2 Chr 18", "type": "nt"}
        ],

        "divine_council_note": "2 Chronicles 18:18-22 is one of the TWO most explicit divine council scenes in "
                               "the Old Testament (the other being Job 1-2). Micaiah's vision reveals the full "
                               "structure of the council: (1) YHWH PRESIDES -- he sits on his throne as the "
                               "supreme authority; (2) THE HOST ASSEMBLES -- 'all the host of heaven' (kol-tseva "
                               "hashamayim) stands before him, a vast assembly of spiritual beings; (3) YHWH POSES "
                               "A QUESTION -- 'Who will entice Ahab?' This is not ignorance but deliberation; "
                               "YHWH invites participation from his council; (4) SPIRITS PROPOSE -- 'one said one "
                               "thing, and another said another' (18:19); the council deliberates with diverse "
                               "opinions; (5) A SPIRIT VOLUNTEERS -- 'I will go out and will be a lying spirit in "
                               "the mouth of all his prophets' (18:21); (6) YHWH AUTHORIZES -- 'You are to entice "
                               "him, and you shall succeed; go out and do so' (18:21). The lying spirit then "
                               "operates through Ahab's 400 prophets, who genuinely believe they are speaking for "
                               "God but are actually channeling a council-authorized deception. This reveals that "
                               "not all spiritual influence is transparent -- YHWH can and does authorize deceptive "
                               "spirits as instruments of judgment against those who have rejected truth. The "
                               "theological implications are staggering: YHWH's sovereignty extends even over "
                               "deception when it serves his just purposes.",

        "sections": [
            {
                "heading": "Jehoshaphat the Seeker: Reform, Teaching, Justice (2 Chr 17; 19)",
                "body": "Jehoshaphat 'sought the God of his father and walked in his commandments and not "
                        "according to the practices of Israel' (17:4). The Chronicler notes three specific "
                        "reforms unique to his account: (1) Jehoshaphat sends officials, Levites, and "
                        "priests throughout Judah 'having the Book of the Law of the LORD with them. They "
                        "went about through all the cities of Judah and taught among the people' (17:9). "
                        "This is organized religious education -- the Torah brought to the people. (2) He "
                        "establishes a judicial system: 'He appointed judges in the land in all the fortified "
                        "cities of Judah' with the charge: 'Consider what you do, for you judge not for man "
                        "but for the LORD' (19:5-6). (3) In Jerusalem, he creates a court of appeal with "
                        "Levites, priests, and family heads. The Chronicler's Jehoshaphat is the model of "
                        "a king who institutionalizes faithfulness through education, justice, and worship."
            },
            {
                "heading": "Micaiah's Vision: The Divine Council Exposed (2 Chr 18:1-34)",
                "body": "Jehoshaphat allies with Ahab of Israel against Aram at Ramoth-gilead. Jehoshaphat "
                        "asks: 'Is there not yet a prophet of the LORD of whom we may inquire?' (18:6). Ahab "
                        "grudgingly summons Micaiah ben Imlah -- 'I hate him, for he never prophesies good "
                        "concerning me, but always evil' (18:7). When Micaiah arrives, he first mocks: 'Go up "
                        "and triumph; they will be given into your hand' (18:14). Pressed to speak truly, "
                        "Micaiah describes two visions. First: 'I saw all Israel scattered on the mountains, "
                        "as sheep that have no shepherd' (18:16) -- Ahab's death predicted. Second: the divine "
                        "council vision. 'I saw the LORD sitting on his throne, and all the host of heaven "
                        "standing on his right hand and on his left' (18:18). YHWH asks: 'Who will entice "
                        "Ahab?' A spirit comes forward: 'I will be a lying spirit in the mouth of all his "
                        "prophets.' YHWH authorizes the mission. Ahab, disguised in battle, is struck by a "
                        "'random' arrow and dies -- but the arrow is not random. It is the council's decree "
                        "executed through a bowman who 'drew his bow at random and struck the king of Israel' "
                        "(18:33). Human randomness and divine sovereignty intersect."
            },
            {
                "heading": "The Battle of Faith: Jehoshaphat's Prayer and the Singing Army (2 Chr 20)",
                "body": "A vast coalition of Moab, Ammon, and others marches against Judah (20:1-2). "
                        "Jehoshaphat's response is the Chronicler's ideal of faithful kingship: he sets "
                        "his face 'to seek the LORD' and proclaims a fast (20:3). His prayer is a model "
                        "of covenantal reasoning: he appeals to YHWH's past acts (20:7-9), acknowledges "
                        "Israel's helplessness (20:12), and concludes with radical dependence: 'We do not "
                        "know what to do, but our eyes are on you' (20:12). The Spirit comes on Jahaziel "
                        "the Levite: 'Do not be afraid and do not be dismayed because of this great horde, "
                        "for the battle is not yours but God's' (20:15). Jehoshaphat then makes a stunning "
                        "tactical decision: he appoints SINGERS to march ahead of the army, praising YHWH "
                        "'in holy attire' (20:21). 'When they began to sing and praise, the LORD set an "
                        "ambush against the men of Ammon, Moab, and Mount Seir' (20:22). The enemy armies "
                        "destroy each other. Judah does not fight at all. This is the Chronicler's theology "
                        "in action: worship IS warfare. The singers who march before the army are as "
                        "decisive as any military formation."
            },
            {
                "heading": "Decline and Rescue: Jehoram, Ahaziah, Athaliah, and Joash (2 Chr 21-23)",
                "body": "After Jehoshaphat, the dynasty descends into crisis. Jehoram marries Ahab's daughter "
                        "and 'walked in the way of the kings of Israel' (21:6). God does not destroy Judah "
                        "'because of the covenant that he had made with David' (21:7) -- the covenant holds "
                        "even when the king fails. Ahaziah (ch. 22) continues the Ahab alliance and dies at "
                        "Jehu's hand. Then Athaliah, the queen mother, 'arose and destroyed all the royal "
                        "family of the house of Judah' (22:10). The Davidic line is nearly extinguished. But "
                        "Jehoshabeath (the priest Jehoiada's wife) hides the infant Joash for six years. In "
                        "chapter 23, Jehoiada engineers a coup: he reveals Joash, anoints him king, and "
                        "Athaliah is executed. 'Then all the people of the land rejoiced, and the city was "
                        "quiet after Athaliah had been put to death with the sword' (23:21). The Davidic "
                        "covenant survives by a single child -- a thread of promise that runs through "
                        "Chronicles to the ultimate son of David."
            }
        ]
    },

    {
        "id": "2chr-24-28",
        "ref": "2 Chronicles 24-28",
        "chapter_num": 3,
        "title": "From Reform to Apostasy: Joash, Amaziah, Uzziah, Jotham, and Ahaz",
        "era": "divided_kingdom",
        "type": "chapter",

        "synopsis": "The middle period of the divided monarchy follows a pattern of reform followed "
                    "by decline. Joash starts well under Jehoiada's guidance, repairing the temple, "
                    "but after Jehoiada dies he 'abandoned the house of the LORD' (24:18) and murders "
                    "Zechariah the priest -- the martyr Jesus references in Matthew 23:35. Amaziah "
                    "defeats Edom but brings back their gods (25:14). Uzziah prospers greatly until "
                    "'his heart was proud' and he attempts to burn incense in the temple, which is "
                    "the priests' prerogative alone -- and God strikes him with leprosy (26:16-21). "
                    "Jotham follows a pattern of mixed faithfulness (ch. 27). Then Ahaz (ch. 28) "
                    "represents the nadir: he makes molten images for the Baals, burns his sons as "
                    "offerings in the Valley of Hinnom, and shuts the doors of the temple. Ahaz is "
                    "the anti-David, the king who does everything wrong.",

        "key_verse": {
            "ref": "2 Chronicles 26:16",
            "text": "But when he was strong, he grew proud, to his destruction. For he was unfaithful to the LORD his God and entered the temple of the LORD to burn incense on the altar of incense.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ma'al (breach of faith -- Uzziah's defining sin: entering the temple unauthorized; the same word used for Saul, Rehoboam, and the exile itself)",
            "tsara'at (skin disease/leprosy -- Uzziah's punishment for temple violation; a sign of divine displeasure marking him as unclean)",
            "ge-ben-hinnom (Valley of the son of Hinnom/Gehenna -- where Ahaz burned his sons; later becomes the symbol of eternal judgment in Jesus' teaching)",
            "ga'avah (pride -- the root sin that leads to Uzziah's fall; 'when he was strong, his heart was lifted up')"
        ],

        "ane_backdrop": "The tension between royal and priestly authority over temple functions was "
                        "real throughout the ancient Near East. In Mesopotamia, kings frequently "
                        "performed priestly functions. In Egypt, Pharaoh was the supreme priest. "
                        "Israel's system was distinctive: the king could not offer incense or perform "
                        "priestly duties. When Uzziah crosses this boundary (26:16-18), he violates "
                        "the distinctive Israelite separation of powers that protects the holiness of "
                        "YHWH's worship from royal manipulation. The leprosy that strikes him is not "
                        "arbitrary punishment but a boundary marker: 'You have no right here' is "
                        "inscribed on Uzziah's body. Child sacrifice in the Valley of Hinnom (Ahaz, "
                        "28:3) is well-attested in the Levant: Phoenician and Punic tophets (sacred "
                        "precincts for child sacrifice) have been excavated at Carthage and other sites.",

        "second_temple": [
            {
                "source": "Matthew 23:35 / Luke 11:51",
                "summary": "Jesus says: 'from the blood of righteous Abel to the blood of Zechariah "
                           "the son of Barachiah, whom you murdered between the sanctuary and the "
                           "altar' -- referencing the murder of Zechariah in 2 Chr 24:20-22.",
                "relevance": "Jesus brackets the entire Old Testament's martyrdom record between Genesis "
                             "(Abel) and 2 Chronicles (Zechariah) -- the first and last books of the "
                             "Hebrew canon. This confirms Chronicles' position as the final book of "
                             "Jesus' Bible."
            },
            {
                "source": "Isaiah 6:1",
                "summary": "'In the year that King Uzziah died I saw the Lord sitting upon a throne, "
                           "high and lifted up' -- Isaiah's commissioning vision occurs in the year of "
                           "Uzziah's death.",
                "relevance": "The leprous king who unlawfully entered the temple is replaced in Isaiah's "
                             "vision by the true King who fills the temple with his glory. Uzziah's story "
                             "and Isaiah's call are theologically linked."
            }
        ],

        "cross_refs": [
            {"ref": "2 Kings 12:1-21", "note": "The parallel account of Joash's temple repair -- Kings and Chronicles agree on the basic facts but frame them differently", "type": "ot"},
            {"ref": "2 Kings 15:1-7", "note": "Uzziah (Azariah) in Kings -- a brief account; Chronicles adds the dramatic temple intrusion and leprosy scene", "type": "ot"},
            {"ref": "Isaiah 6:1-8", "note": "Isaiah's throne room vision in the year Uzziah died -- the divine council appears as the earthly king falls", "type": "ot"},
            {"ref": "Matthew 23:35", "note": "Jesus references Zechariah's murder 'between the sanctuary and the altar' -- the martyrdom recorded in 2 Chr 24:20-22", "type": "nt"},
            {"ref": "Mark 9:43-48", "note": "Jesus uses 'Gehenna' (ge-hinnom) as the image of eschatological judgment -- the valley where Ahaz burned his sons (2 Chr 28:3) becomes the symbol of hell", "type": "nt"}
        ],

        "divine_council_note": "Uzziah's temple intrusion (26:16-21) carries divine council significance. "
                               "The altar of incense is located directly before the veil separating the Holy "
                               "Place from the Holy of Holies -- it stands at the threshold of YHWH's throne "
                               "room, the earthly entrance to the divine council chamber. When Uzziah attempts "
                               "to burn incense there, he is not merely breaking a ritual rule; he is entering "
                               "sacred space reserved for those specifically authorized by YHWH (the Aaronic "
                               "priests). The 80 priests who confront him -- 'It is not for you, Uzziah, to "
                               "burn incense to the LORD, but for the priests, the sons of Aaron, who are "
                               "consecrated to burn incense' (26:18) -- are defending the boundary between the "
                               "divine and human realms. Uzziah's leprosy is the consequence of unauthorized "
                               "approach to the council threshold. It is significant that Isaiah's divine "
                               "council vision (Isa 6:1-8) occurs 'in the year that King Uzziah died' -- the "
                               "king who intruded into the temple is replaced by a vision of the true King "
                               "who fills the temple with his kavod.",

        "sections": [
            {
                "heading": "Joash: Temple Repair and Tragic Betrayal (2 Chr 24)",
                "body": "Joash begins well under the priest Jehoiada's guidance. His defining act is the "
                        "repair of the temple: 'Joash decided to restore the house of the LORD' (24:4). "
                        "A collection box is placed at the temple gate, and the people give generously -- "
                        "a prototype for all later temple and church giving. But after Jehoiada dies at age "
                        "130 (24:15), the princes of Judah lead Joash astray: they 'abandoned the house of "
                        "the LORD, the God of their fathers, and served the Asherim and the idols' (24:18). "
                        "YHWH sends prophets, but they do not listen. Then 'the Spirit of God clothed "
                        "Zechariah the son of Jehoiada the priest, and he stood above the people and said, "
                        "Why do you break the commandments of the LORD?' (24:20). Joash commands Zechariah "
                        "stoned to death 'in the court of the house of the LORD' (24:21). Zechariah's dying "
                        "words: 'May the LORD see and avenge!' (24:22). This is the martyrdom Jesus "
                        "references as the last recorded in the Hebrew canon."
            },
            {
                "heading": "Uzziah: Prosperity, Pride, and the Throne Room Violation (2 Chr 26)",
                "body": "Uzziah reigns for 52 years -- one of Judah's longest and most prosperous reigns. "
                        "The Chronicler gives him extensive coverage unique to his account: military innovations "
                        "(towers, siege engines), agricultural development, a standing army of 307,500 soldiers. "
                        "'He was marvelously helped, till he was strong' (26:15). Then the turning point: 'But "
                        "when he was strong, he grew proud, to his destruction. For he was unfaithful (ma'al) "
                        "to the LORD his God and entered the temple of the LORD to burn incense on the altar "
                        "of incense' (26:16). Azariah the chief priest and 80 priests confront him: 'It is "
                        "not for you, Uzziah, to burn incense to the LORD' (26:18). Uzziah becomes angry -- "
                        "and as he rages, 'leprosy broke out on his forehead' (26:19). He is rushed out of "
                        "the temple, 'and he himself hurried to go out, because the LORD had struck him' "
                        "(26:20). Uzziah lives the rest of his life in quarantine, excluded from the temple "
                        "he had violated. His body bears the mark of his trespass."
            },
            {
                "heading": "Ahaz: The Anti-David and the Valley of Hinnom (2 Chr 28)",
                "body": "Ahaz is the Chronicler's paradigm of unfaithfulness. He 'made metal images for the "
                        "Baals, and he made offerings in the Valley of the Son of Hinnom and burned his sons "
                        "as an offering' (28:2-3). Child sacrifice in the ge-ben-hinnom -- the valley that "
                        "becomes Gehenna in later Jewish and New Testament usage, the symbol of divine "
                        "judgment. Ahaz is defeated by Aram, by Israel, and by Edom and Philistia. The "
                        "Chronicler's verdict: 'For the LORD humbled Judah because of Ahaz king of Israel, "
                        "for he had acted without restraint in Judah and had been utterly unfaithful (ma'ol "
                        "ma'al) to the LORD' (28:19). The double use of ma'al emphasizes the extremity. "
                        "Ahaz's final act: 'He shut up the doors of the house of the LORD' (28:24). This "
                        "is the ultimate sacrilege -- closing God's house, cutting off the people from "
                        "worship. The stage is set for Hezekiah's dramatic reopening."
            }
        ]
    }
]
