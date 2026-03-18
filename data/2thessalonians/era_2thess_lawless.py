"""
era_2thess_lawless.py -- 2 Thessalonians: The Man of Lawlessness

Paul corrects eschatological confusion and reveals the apocalyptic sequence:
the apostasy must come first, then the man of lawlessness is revealed -- one
empowered by Satan who seats himself in God's temple. The restrainer holds
back the mystery of lawlessness until the appointed time.
"""

CHAPTERS = [
    {
        "id": "2thess-1-3",
        "ref": "2 Thessalonians 1-3",
        "chapter_num": 1,
        "title": "The Man of Lawlessness and the Mystery of Iniquity",
        "era": "2thess_lawless",
        "type": "chapter",
        "themes": ["DC", "REBEL", "KING", "TYPE", "HOLY"],

        "synopsis": "Paul opens by commending the Thessalonians' faith under persecution and describing "
                    "the 'righteous judgment of God' (1:5) when 'the Lord Jesus is revealed from heaven "
                    "with his mighty angels (angelon dynameos autou) in flaming fire, inflicting vengeance "
                    "on those who do not know God' (1:7-8). Chapter 2 is the apocalyptic core: Paul "
                    "corrects the false claim that 'the day of the Lord has come' (2:2). Two events must "
                    "precede: (1) 'the apostasy' (he apostasia -- the great falling away) and (2) the "
                    "revelation of 'the man of lawlessness, the son of destruction, who opposes and exalts "
                    "himself against every so-called god or object of worship, so that he takes his seat "
                    "in the temple of God, proclaiming himself to be God' (2:3-4). Something/someone "
                    "currently restrains this figure (to katechon / ho katechon, 2:6-7). When the "
                    "restrainer is removed, the lawless one will be revealed, and the Lord Jesus will "
                    "'kill him with the breath of his mouth and bring him to nothing by the appearance "
                    "of his coming' (2:8). The lawless one comes 'by the activity of Satan with all "
                    "power and false signs and wonders' (2:9). Chapter 3 addresses practical matters: "
                    "the idle must work, and the community must maintain discipline.",

        "key_verse": {
            "ref": "2 Thessalonians 2:3-4",
            "text": "Let no one deceive you in any way. For that day will not come, unless the rebellion comes first, and the man of lawlessness is revealed, the son of destruction, who opposes and exalts himself against every so-called god or object of worship, so that he takes his seat in the temple of God, proclaiming himself to be God.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ho anthropos tes anomias (the man of lawlessness -- the eschatological opponent of God; anomia = lawlessness/torah-lessness; a human agent of Satan's cosmic rebellion)",
            "ho huios tes apoleias (the son of destruction/perdition -- Semitic idiom: one destined for destruction; same title applied to Judas in John 17:12)",
            "apostasia (apostasy/rebellion -- a deliberate departure from established truth; in military usage, a desertion or mutiny; the great cosmic defection before the end)",
            "to katechon / ho katechon (the restrainer -- neuter 'what restrains' [2:6] and masculine 'who restrains' [2:7]; the mysterious force/person holding back the lawless one)",
            "mysterion tes anomias (mystery of lawlessness -- the hidden operation of cosmic rebellion already at work; parallel to Paul's 'mystery' of the gospel but demonic)",
            "energeia tou Satana (the working/activity of Satan -- Satan's operative power behind the lawless one; energeia = effective, active power)",
            "epiphaneia tes parousias (the appearance of his coming -- Christ's return is described with two words: epiphaneia [visible manifestation] + parousia [royal arrival])",
            "angelon dynameos autou (his mighty angels / angels of his power -- the angelic host accompanying Christ's return; the divine council army)"
        ],

        "ane_backdrop": "The 'man of lawlessness' draws on the tradition of sacrilegious rulers who claimed "
                        "divine status: Antiochus IV Epiphanes (who desecrated the Jerusalem temple in 167 "
                        "BC and was called 'Epiphanes' -- 'God Manifest'), the Roman emperor Gaius (Caligula) "
                        "who ordered his statue placed in the Jerusalem temple in 40 AD, and the broader "
                        "pattern of ANE kings claiming divine prerogatives. The 'temple of God' (naos tou "
                        "theou) in which the man of lawlessness sits may be the literal Jerusalem temple, "
                        "the eschatological temple, or a metaphorical reference to the church as God's "
                        "temple (cf. 1 Cor 3:16; 2 Cor 6:16).",

        "second_temple": [
            {
                "source": "Daniel 11:36-37",
                "summary": "The king 'shall exalt himself and magnify himself above every god, and shall "
                           "speak astonishing things against the God of gods.'",
                "relevance": "Paul's description of the man of lawlessness who 'exalts himself against "
                             "every so-called god' directly echoes Daniel 11:36. Both describe a figure "
                             "who usurps divine prerogatives."
            },
            {
                "source": "Daniel 9:27; 12:11",
                "summary": "The 'abomination that makes desolate' set up in the temple -- the desecration "
                           "of the holy place.",
                "relevance": "The man of lawlessness 'taking his seat in the temple of God' parallels the "
                             "Danielic abomination of desolation. Jesus references this tradition in the "
                             "Olivet Discourse (Matt 24:15)."
            },
            {
                "source": "1 Enoch 54:6",
                "summary": "Michael and other angels bind the host of Azazel and cast them into the "
                           "fiery furnace at the appointed time.",
                "relevance": "The tradition of angelic beings restraining evil forces until the appointed "
                             "eschatological moment parallels the restrainer concept in 2 Thess 2:6-7."
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 11:36", "note": "The king who exalts himself above every god -- the OT source for the man of lawlessness", "type": "ot"},
            {"ref": "Daniel 9:27", "note": "The abomination of desolation in the temple -- the same sacrilege", "type": "ot"},
            {"ref": "Isaiah 11:4", "note": "'He shall strike the earth with the rod of his mouth' -- Paul echoes this for Christ's destruction of the lawless one", "type": "ot"},
            {"ref": "Ezekiel 28:2", "note": "The prince of Tyre: 'I am a god, I sit in the seat of the gods' -- the same self-deification", "type": "ot"},
            {"ref": "1 John 2:18", "note": "'The antichrist is coming' -- the Johannine parallel to Paul's man of lawlessness", "type": "nt"},
            {"ref": "Revelation 13:1-8", "note": "The beast from the sea: given authority by the dragon, receives worship, blasphemes God", "type": "nt"},
            {"ref": "Matthew 24:15", "note": "'The abomination of desolation spoken of by the prophet Daniel, standing in the holy place'", "type": "nt"},
            {"ref": "Daniel 12:1", "note": "'At that time Michael shall arise' -- the archangel's role in the end-time crisis", "type": "ot"}
        ],

        "divine_council_note": "2 Thessalonians 2 describes the climax of the cosmic rebellion. The man of "
                               "lawlessness is Satan's ultimate human agent -- one who claims to be God and "
                               "sits in God's temple. This is the final escalation of the divine council "
                               "rebellion: from the nachash challenging God's word in Eden, to the Watchers "
                               "crossing the divine-human boundary, to the gods of the nations leading worship "
                               "away from YHWH, to a human figure who claims to BE God. The phrase 'every "
                               "so-called god' (panta legomenon theon, 2:4) echoes 1 Cor 8:5 -- these are "
                               "the divine council members, and the man of lawlessness exalts himself above "
                               "even them. The 'restrainer' (to katechon) may be a divine council agent "
                               "-- Michael the archangel, who in Daniel 12:1 'arises' at the end to protect "
                               "God's people. The 'mystery of lawlessness' (2:7) is already at work: the "
                               "cosmic rebellion operates in hidden form, restrained but active, until the "
                               "appointed time. Christ's return destroys the lawless one 'with the breath "
                               "of his mouth' (2:8) -- the divine Word that created all things (Gen 1; John "
                               "1:1-3) is the same Word that destroys the rebellion.",

        "sections": [
            {
                "heading": "Christ Revealed with His Mighty Angels (1:1-12)",
                "body": "Paul opens by commending the Thessalonians' growing faith and endurance under "
                        "persecution (1:3-4). He frames their suffering as evidence of God's righteous "
                        "judgment (1:5): they will be counted worthy of the kingdom they suffer for. The "
                        "vindication comes 'when the Lord Jesus is revealed from heaven with his mighty "
                        "angels (met' angelon dynameos autou) in flaming fire' (1:7). This is a divine "
                        "council theophany: the Lord descends with the angelic army, 'inflicting vengeance "
                        "on those who do not know God and on those who do not obey the gospel' (1:8). The "
                        "punishment is 'eternal destruction, away from the presence of the Lord and from "
                        "the glory of his might' (1:9) -- separation from the divine council's presence."
            },
            {
                "heading": "The Apostasy and the Man of Lawlessness (2:1-12)",
                "body": "Paul corrects the false claim that the day of the Lord has already come (2:2). "
                        "Two events must precede: (1) 'the apostasy' (he apostasia) -- a great falling "
                        "away from the faith; (2) the revelation of 'the man of lawlessness' (2:3). This "
                        "figure 'opposes and exalts himself against every so-called god' and 'takes his "
                        "seat in the temple of God, proclaiming himself to be God' (2:4). Something "
                        "currently restrains him (2:6-7): 'you know what is restraining him now so that "
                        "he may be revealed in his time.' When the restrainer is removed, the lawless one "
                        "is revealed -- and the Lord Jesus destroys him 'with the breath of his mouth' "
                        "(2:8). The lawless one comes 'by the activity of Satan with all power and false "
                        "signs and wonders, and with all wicked deception' (2:9-10). God sends 'a strong "
                        "delusion' on those who refuse to love the truth (2:11) -- judicial blindness, "
                        "paralleling the hardening of Pharaoh's heart and the blinding by 'the god of "
                        "this age' (2 Cor 4:4)."
            },
            {
                "heading": "Stand Firm and Keep Working (2:13-3:18)",
                "body": "Paul encourages the Thessalonians to 'stand firm and hold to the traditions' "
                        "he taught them (2:15). He prays that the Lord would 'direct your hearts to the "
                        "love of God and to the steadfastness of Christ' (3:5). He addresses the idle: "
                        "'If anyone is not willing to work, let him not eat' (3:10). Some Thessalonians "
                        "had apparently quit working in expectation of the imminent parousia. Paul "
                        "commands them to 'do their work quietly and earn their own living' (3:12). The "
                        "eschatological hope does not produce passivity but faithful, steady labor in the "
                        "present age."
            }
        ]
    }
]
