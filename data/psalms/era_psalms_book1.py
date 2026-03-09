"""
era_psalms_book1.py -- Psalms 1-41 (Book I): The Davidic Collection

Book I of the Psalter is overwhelmingly attributed to David (73 of 150 psalms
bear the Davidic superscription, and nearly all of Book I does). These psalms
establish the theological vocabulary of the entire Psalter: the two ways (Ps 1),
the royal son enthroned on Zion (Ps 2), human dominion under divine authority
(Ps 8), resurrection hope (Ps 16), the suffering righteous one (Ps 22), the
divine shepherd (Ps 23), the king of glory entering his sanctuary (Ps 24),
YHWH's thundering voice over the cosmic waters (Ps 29), creation by the divine
word (Ps 33), and the angel of YHWH as protector (Ps 34). Book I is the
foundation on which the entire Psalter's theology of kingship, suffering, and
divine council sovereignty is built.
"""

CHAPTERS = [
    {
        "id": "ps-1-2",
        "ref": "Psalms 1-2",
        "chapter_num": 1,
        "title": "The Two Ways and the Enthroned Son -- Gateway to the Psalter",
        "era": "psalms_book1",
        "type": "chapter",

        "synopsis": "Psalms 1 and 2 function as a single literary gateway to the entire Psalter. "
                    "Psalm 1 establishes the two-ways theology: the righteous man who meditates "
                    "on Torah prospers like a tree planted by streams of water, while the wicked "
                    "are like chaff that the wind drives away. Psalm 2 shifts from the individual "
                    "to the cosmic: the nations and their kings conspire against YHWH and his "
                    "anointed (meshiach), but YHWH, enthroned in heaven, laughs at their rebellion. "
                    "He has installed his king on Zion and declared the decree: 'You are my Son "
                    "(beni); today I have begotten you (yelidtikha)' (2:7). The king is granted "
                    "the nations as his inheritance and the ends of the earth as his possession. "
                    "Together these psalms frame the Psalter: Torah obedience (Ps 1) and royal "
                    "enthronement (Ps 2) are the two pillars of Israel's hope. The phrase 'Blessed "
                    "is the man' (ashre ha'ish) opens Psalm 1:1, and 'Blessed are all who take "
                    "refuge in him' (ashre kol chosei vo) closes Psalm 2:12 -- an inclusio of "
                    "blessedness that frames the entire introduction.",

        "key_verse": {
            "ref": "Psalm 2:7",
            "text": "I will tell of the decree: The LORD said to me, 'You are my Son; today I have begotten you.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ashre (blessed/happy -- the opening word of the Psalter; a state of flourishing under God's favor)",
            "meshiach (anointed one -- the king YHWH has installed on Zion; the root of 'Messiah')",
            "ben (son -- the divine decree of sonship over the Davidic king; Ps 2:7, 12)",
            "nachalah (inheritance -- the nations given to the son as his possession)",
            "hagah (to meditate/murmur -- audible recitation of Torah, same verb as Josh 1:8)",
            "choq (decree -- the divine decree of enthronement, the royal protocol from YHWH's council)",
            "regash (to conspire/rage -- the tumultuous rebellion of the nations against YHWH)"
        ],

        "ane_backdrop": "Psalm 2 reflects the ANE royal enthronement protocol. In Egyptian coronation "
                        "texts, the pharaoh is declared 'son of Re' at his accession -- a divine "
                        "sonship that confers authority over the nations. The Instruction of Merikare "
                        "and the Bentresh Stela describe the pharaoh as begotten by the deity for "
                        "cosmic rule. In Mesopotamia, the Enuma Elish ends with Marduk enthroned as "
                        "king of the gods after defeating Tiamat -- his enthronement establishes "
                        "cosmic order. The language of Psalm 2 inverts these patterns: it is not "
                        "Pharaoh or a Mesopotamian king who receives divine sonship, but YHWH's "
                        "chosen king on Zion. The 'decree' (choq) of Psalm 2:7 parallels the "
                        "Egyptian royal protocol document read at coronation. The laughter of YHWH "
                        "in heaven (2:4) functions as a divine council scene: the Most High, seated "
                        "in the heavenly assembly, mocks the pretensions of earthly rulers who "
                        "challenge his appointed regent.",

        "second_temple": [
            {
                "source": "4QFlorilegium (4Q174)",
                "summary": "This Qumran text interprets Psalm 2:7 as referring to the 'Branch of "
                           "David' (tsemach David) who will arise in the last days. The 'begetting' "
                           "is understood as YHWH raising up the eschatological king.",
                "relevance": "The Dead Sea Scrolls community read Psalm 2 as a messianic prophecy -- "
                             "the 'Son' was the coming Davidic deliverer, not merely the historical king."
            },
            {
                "source": "Acts 4:25-28",
                "summary": "The early church quotes Psalm 2:1-2 as fulfilled in the conspiracy of "
                           "Herod and Pilate against Jesus: 'the kings of the earth set themselves, "
                           "and the rulers were gathered together, against the Lord and against his "
                           "Anointed.'",
                "relevance": "The apostolic interpretation identifies Jesus as the meshiach of Psalm 2 "
                             "and the crucifixion events as the nations raging against YHWH's king."
            },
            {
                "source": "Acts 13:33; Hebrews 1:5; 5:5",
                "summary": "Paul and the author of Hebrews both cite Psalm 2:7 ('You are my Son, "
                           "today I have begotten you') as referring to Jesus' resurrection and "
                           "exaltation. Hebrews argues the Son is superior to angels precisely "
                           "because this decree was never spoken to any angel.",
                "relevance": "The NT reading makes Psalm 2:7 the definitive proof-text for Jesus' "
                             "divine sonship -- a sonship that surpasses the elohim of the divine council."
            }
        ],

        "cross_refs": [
            {"ref": "2 Samuel 7:14", "note": "'I will be to him a father, and he shall be to me a son' -- the Davidic covenant that Psalm 2:7 echoes", "type": "ot"},
            {"ref": "Psalm 110:1", "note": "'Sit at my right hand' -- the companion enthronement psalm that completes the picture of the divine king", "type": "ot"},
            {"ref": "Joshua 1:8", "note": "'This Book of the Law shall not depart from your mouth; you shall meditate (hagah) on it day and night' -- same language as Ps 1:2", "type": "ot"},
            {"ref": "Daniel 7:13-14", "note": "The Son of Man receives dominion over all nations -- the eschatological fulfillment of Ps 2's grant of the nations to the Son", "type": "ot"},
            {"ref": "Revelation 2:26-27", "note": "'The one who conquers... I will give authority over the nations, and he will rule them with a rod of iron' -- quoting Ps 2:8-9", "type": "nt"},
            {"ref": "Hebrews 1:5", "note": "'To which of the angels did God ever say, You are my Son, today I have begotten you?' -- Ps 2:7 as proof of superiority over the sons of God", "type": "nt"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God, but Israel kept as YHWH's portion -- the background to Ps 2's grant of all nations to the Son", "type": "ot"}
        ],

        "divine_council_note": "Psalm 2 is a divine council enthronement text. The scene opens with "
                               "the nations in rebellion -- not merely against Israel's earthly king but "
                               "against YHWH and his meshiach (2:2). The rebellion is cosmic: the 'kings "
                               "of the earth' and 'rulers' represent the human agents of the territorial "
                               "elohim who were allotted the nations under Deuteronomy 32:8-9. Their "
                               "conspiracy to 'break the bonds' (2:3) is an attempt to overthrow YHWH's "
                               "sovereignty. But YHWH's response comes from the heavenly throne room: 'He "
                               "who sits in the heavens laughs; the Lord holds them in derision' (2:4). "
                               "This is the divine council in session -- the Most High, enthroned above the "
                               "assembly, regards the rebellion of the lower elohim's earthly proxies with "
                               "contempt. The decree of 2:7 is the key: 'You are my Son (beni); today I "
                               "have begotten you.' In the divine council framework, this is an adoption "
                               "formula that elevates the Davidic king above the sons of God (bene "
                               "elohim). The angels are bene elohim -- sons of God by nature. The Davidic "
                               "king becomes ben by decree. And this ben receives what the bene elohim "
                               "were given in Deut 32:8: 'Ask of me, and I will give you the nations as "
                               "your inheritance (nachalah), the ends of the earth as your possession' "
                               "(2:8). The nations that were parceled out to the sons of God are now "
                               "reclaimed and given to YHWH's human Son. This is the reversal of Babel. "
                               "Psalm 2 announces that a human king, seated on Zion, will inherit what "
                               "the rebellious elohim forfeited. The closing warning -- 'Kiss the Son "
                               "(bar), lest he be angry' (2:12) -- uses the Aramaic word bar rather than "
                               "the Hebrew ben, possibly reflecting the international scope of the decree: "
                               "even the Gentile nations must submit to YHWH's regent.",

        "sections": [
            {
                "heading": "Psalm 1: The Two Ways -- Torah Meditation and the Tree of Life",
                "body": "The Psalter opens not with a prayer or a hymn but with a wisdom instruction. "
                        "'Blessed (ashre) is the man who walks not in the counsel of the wicked, nor "
                        "stands in the way of sinners, nor sits in the seat of scoffers' (1:1). The "
                        "threefold progression -- walking, standing, sitting -- depicts the gradual "
                        "entrenchment of the unfaithful. The righteous man, by contrast, delights in "
                        "the Torah (torah) of YHWH and meditates (yehgeh) on it day and night (1:2). "
                        "The verb hagah is the same word used in Joshua 1:8 for the audible murmuring "
                        "of Scripture -- continuous, embodied engagement with the text. The result is "
                        "a cosmic image: 'He is like a tree planted by streams of water that yields "
                        "its fruit in its season, and its leaf does not wither. In all that he does, "
                        "he prospers' (1:3). The tree by water evokes Eden -- the garden where the "
                        "tree of life stood beside the river (Gen 2:9-10). The Torah-meditating man "
                        "is restored to an Edenic state of fruitfulness. The wicked, by contrast, "
                        "'are like chaff (mots) that the wind drives away' (1:4) -- rootless, "
                        "substanceless, blown into oblivion. The psalm closes with the theological "
                        "foundation of the entire Psalter: 'The LORD knows (yodea) the way of the "
                        "righteous, but the way of the wicked will perish' (1:6). YHWH's 'knowing' "
                        "is not passive awareness but active, intimate, covenantal engagement."
            },
            {
                "heading": "Psalm 2: The Nations Rage, the Son is Enthroned",
                "body": "The scene shifts from the individual to the cosmic. 'Why do the nations "
                        "rage (rageshu) and the peoples plot (yehgu) in vain?' (2:1). The verb "
                        "yehgu is the same root as hagah in Psalm 1:2 -- but where the righteous "
                        "man 'murmurs' Torah, the nations 'murmur' rebellion. The kings of the earth "
                        "and rulers take counsel together against YHWH and his meshiach ('anointed "
                        "one'), saying 'Let us burst their bonds apart and cast away their cords "
                        "from us' (2:3). This is anti-covenant language: the nations reject the "
                        "authority of YHWH and his regent. YHWH's response is devastating in its "
                        "calm: 'He who sits in the heavens laughs; the Lord holds them in derision' "
                        "(2:4). The God enthroned above the council regards the rebellion of earthly "
                        "powers as absurd. Then he speaks 'in his wrath' (2:5): 'As for me, I have "
                        "set my King on Zion, my holy hill' (2:6). The king reports the decree of "
                        "YHWH: 'You are my Son; today I have begotten you. Ask of me, and I will "
                        "make the nations your inheritance (nachalah), and the ends of the earth "
                        "your possession' (2:7-8). The son will rule with an iron rod (shevet "
                        "barzel), shattering rebellious nations like potter's vessels. The psalm "
                        "closes with a warning to the kings: 'Serve YHWH with fear... Kiss the Son "
                        "(bar), lest he be angry and you perish in the way' (2:11-12). The gateway "
                        "psalms together declare: the path of the individual is Torah (Ps 1); the "
                        "destiny of the nations is the Son (Ps 2)."
            }
        ]
    },

    {
        "id": "ps-8",
        "ref": "Psalm 8",
        "chapter_num": 2,
        "title": "What Is Man? -- Human Dominion and the Divine Council",
        "era": "psalms_book1",
        "type": "chapter",

        "synopsis": "Psalm 8 is the creation psalm of Book I -- a hymn of praise that begins and "
                    "ends with the majesty of YHWH's name in all the earth. Between the bookends "
                    "lies the central question of the Psalter and of all theology: 'What is man "
                    "(enosh) that you are mindful of him, and the son of man (ben-adam) that you "
                    "care for him?' (8:4). The answer is staggering: 'You have made him a little "
                    "lower than the elohim (the heavenly beings) and crowned him with glory and "
                    "honor' (8:5). Humanity is placed just below the divine council members -- "
                    "the elohim who surround YHWH's throne -- and given dominion over all creation. "
                    "The psalm is both a celebration of the Genesis 1:26-28 mandate and a profound "
                    "theological statement about human dignity in the cosmic hierarchy.",

        "key_verse": {
            "ref": "Psalm 8:4-5",
            "text": "What is man that you are mindful of him, and the son of man that you care for him? Yet you have made him a little lower than the heavenly beings and crowned him with glory and honor.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "enosh (man/mortal -- emphasizing human frailty and mortality)",
            "ben-adam (son of man/son of Adam -- the human being in his earthly, creaturely identity)",
            "elohim (gods/heavenly beings -- the divine council members; some translations render 'angels')",
            "me'at (a little -- the narrow gap between humans and the divine council beings)",
            "kavod (glory -- the radiance of the divine presence shared with humanity)",
            "hadar (honor/majesty -- royal splendor conferred on the human vice-regent)",
            "mashal (to rule/have dominion -- the Genesis 1 mandate restated)"
        ],

        "ane_backdrop": "The question 'What is man?' echoes the Babylonian Atrahasis epic, where "
                        "humanity is created to relieve the gods of labor. In Mesopotamian theology, "
                        "humans are slaves created for divine convenience. Psalm 8 radically inverts "
                        "this: humanity is crowned with glory and given dominion -- not as slaves but "
                        "as vice-regents. The Egyptian concept of the pharaoh as the image of the "
                        "god on earth (the only human with divine authority) is democratized in "
                        "Genesis 1:26-28 and celebrated in Psalm 8: all humanity bears the divine "
                        "image and exercises dominion. The Ugaritic texts describe the assembly of "
                        "the sons of El (bene il) as the ruling council of the cosmos. Psalm 8 "
                        "places humanity 'a little lower' than these elohim -- just below the "
                        "divine council in the cosmic hierarchy, yet crowned with the same kavod "
                        "(glory) that characterizes the divine presence.",

        "second_temple": [
            {
                "source": "Hebrews 2:6-9",
                "summary": "The author of Hebrews quotes Psalm 8:4-6 and applies it to Jesus: 'But "
                           "we see him who for a little while was made lower than the angels, namely "
                           "Jesus, crowned with glory and honor because of the suffering of death.'",
                "relevance": "Hebrews reads Psalm 8 christologically: Jesus is the true 'son of man' "
                             "who fulfills humanity's intended dominion. His temporary humiliation "
                             "(incarnation and death) leads to his exaltation above the elohim."
            },
            {
                "source": "1 Corinthians 15:27",
                "summary": "Paul quotes Psalm 8:6 ('you have put all things under his feet') as "
                           "referring to Christ's eschatological rule: 'For God has put all things "
                           "in subjection under his feet.'",
                "relevance": "Paul reads the dominion mandate of Psalm 8 as ultimately realized in "
                             "the risen Christ, who subjects all powers -- including the hostile "
                             "spiritual rulers -- under his authority."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 1:26-28", "note": "'Let us make man in our image... and let them have dominion' -- the creation mandate Psalm 8 celebrates", "type": "ot"},
            {"ref": "Hebrews 2:5-9", "note": "Psalm 8 applied to Jesus as the true 'son of man' who restores human dominion through his death and exaltation", "type": "nt"},
            {"ref": "Psalm 82:6-7", "note": "'You are gods (elohim), sons of the Most High, all of you; nevertheless, like men (adam) you shall die' -- the council members will lose their status; humanity will gain it", "type": "ot"},
            {"ref": "1 Corinthians 15:27", "note": "'He has put all things in subjection under his feet' -- Ps 8:6 fulfilled in Christ's cosmic reign", "type": "nt"},
            {"ref": "Daniel 7:13-14", "note": "The 'son of man' receives dominion over all nations -- the eschatological fulfillment of Ps 8's ben-adam theology", "type": "ot"},
            {"ref": "Psalm 144:3", "note": "'O LORD, what is man that you regard him, or the son of man that you think of him?' -- echoing the question of Ps 8", "type": "ot"}
        ],

        "divine_council_note": "Psalm 8:5 is a divine council text of the first order. The Hebrew reads "
                               "'You made him a little lower than elohim' -- the word elohim here refers "
                               "to the members of the heavenly council, the divine beings who surround "
                               "YHWH's throne. The LXX translated elohim as angelous ('angels'), and this "
                               "is the reading Hebrews 2:7 follows. But the Hebrew is more provocative: "
                               "humanity is positioned just below the gods in the cosmic hierarchy. The "
                               "gap is described as me'at -- 'a little' -- astonishingly narrow. Humans "
                               "are not creatures of a fundamentally different order from the council "
                               "members; they are near-peers, crowned with the same kavod (glory) and "
                               "hadar (honor/majesty) that characterize divine beings. The dominion "
                               "granted -- 'you have put all things under his feet' (8:6) -- parallels "
                               "the authority of the council members over territories and nations (Deut "
                               "32:8). Humanity's dominion over the created order (sheep, oxen, beasts, "
                               "birds, fish) is the earthly counterpart to the elohim's authority over "
                               "the spiritual realm. This is the imago Dei theology of Genesis 1 "
                               "expressed in divine council terms: humanity is YHWH's designated "
                               "vice-regent in the visible world, just as the bene elohim serve as "
                               "his agents in the invisible one. The tragedy of the Fall is that "
                               "humanity fell below this intended station; the hope of the Psalter is "
                               "that the royal 'son of man' will restore it.",

        "sections": [
            {
                "heading": "The Name Above All Names (8:1-2)",
                "body": "The psalm opens with a cosmic declaration: 'O YHWH, our Lord (adoneinu), "
                        "how majestic (addir) is your name in all the earth! You have set your "
                        "glory (hod) above the heavens' (8:1). The name of YHWH fills the entire "
                        "created order -- from the earth below to the heavens above. The word "
                        "addir means 'majestic, noble, mighty' and is used elsewhere for powerful "
                        "rulers and cosmic forces. YHWH's name surpasses all of them. Verse 2 is "
                        "enigmatic: 'Out of the mouth of babies and infants, you have established "
                        "strength because of your foes, to still the enemy and the avenger.' The "
                        "weakest of human voices -- nursing infants -- are the instruments by which "
                        "YHWH silences his cosmic enemies. Jesus quotes this verse in Matthew 21:16 "
                        "when the children cry 'Hosanna' in the temple. The 'enemy and avenger' "
                        "are cosmic adversaries -- the spiritual forces that oppose YHWH's order -- "
                        "and they are defeated not by military might but by the praise of the "
                        "smallest and weakest of YHWH's creatures."
            },
            {
                "heading": "What Is Man? The Central Question (8:3-5)",
                "body": "The psalmist gazes at the night sky -- 'your heavens, the work of your "
                        "fingers, the moon and the stars, which you have set in place' (8:3) -- "
                        "and the immensity of creation provokes the question that defines the "
                        "psalm: 'What is man (mah-enosh) that you are mindful of him, and the son "
                        "of man (ben-adam) that you care for him?' (8:4). The word enosh emphasizes "
                        "human frailty -- mortality, weakness, limitation. Ben-adam ('son of Adam') "
                        "connects to the dust-origin of Genesis 2:7. Against the backdrop of the "
                        "vast cosmos, human significance seems impossible. The answer overturns "
                        "every expectation: 'You have made him a little lower than the elohim and "
                        "crowned him with glory (kavod) and honor (hadar)' (8:5). The word kavod "
                        "is the same word used for YHWH's own radiant presence (the kavod that "
                        "fills the tabernacle in Exod 40:34). Humanity shares in the divine glory. "
                        "Hadar is royal splendor -- the majesty of a king. The frail, mortal "
                        "creature of dust is crowned like a king and placed just below the heavenly "
                        "council. This is the imago Dei: not a metaphor but a cosmic rank."
            },
            {
                "heading": "Dominion Over All Creation (8:6-9)",
                "body": "'You have given him dominion (tamshilehu) over the works of your hands; "
                        "you have put all things under his feet' (8:6). The verb mashal ('to rule, "
                        "to have dominion') is the exact verb of Genesis 1:28. The scope of "
                        "dominion is total: 'all sheep and oxen, and also the beasts of the field, "
                        "the birds of the heavens, and the fish of the sea, whatever passes along "
                        "the paths of the seas' (8:7-8). Land, air, and sea -- the three realms "
                        "of Genesis 1 -- are placed under human authority. The phrase 'under his "
                        "feet' is royal language: in ANE iconography, the victorious king places "
                        "his foot on the neck of the conquered enemy. Humanity's dominion over "
                        "creation is depicted as a royal conquest already accomplished by YHWH's "
                        "decree. The psalm closes by returning to its opening: 'O YHWH, our Lord, "
                        "how majestic is your name in all the earth!' (8:9). The inclusio frames "
                        "human dominion within divine sovereignty: humanity rules because YHWH "
                        "delegated authority. The dominion is real but derivative. When Hebrews "
                        "2:8 observes 'we do not yet see everything in subjection to him,' it "
                        "acknowledges that the Fall disrupted the mandate -- but in Jesus, the "
                        "true ben-adam, it will be fully restored."
            }
        ]
    },

    {
        "id": "ps-16-22",
        "ref": "Psalms 16, 22",
        "chapter_num": 3,
        "title": "Resurrection Hope and the Passion of the Righteous One",
        "era": "psalms_book1",
        "type": "chapter",

        "synopsis": "Psalms 16 and 22 are the two most significant messianic psalms in Book I -- "
                    "one pointing to resurrection, the other to the suffering that precedes it. "
                    "Psalm 16 is a miktam of David expressing unshakable confidence that YHWH "
                    "will not abandon his soul to Sheol or allow his faithful one (chasid) to see "
                    "corruption (shachat). Peter quotes it at Pentecost as proof of Jesus' "
                    "resurrection (Acts 2:25-31). Psalm 22 opens with the most famous cry of "
                    "dereliction in Scripture: 'My God, my God, why have you forsaken me (eli eli "
                    "lamah azavtani)?' -- the words Jesus spoke from the cross (Matt 27:46). The "
                    "psalm describes pierced hands and feet, divided garments, lots cast for "
                    "clothing, and mockery from surrounding enemies, culminating in a stunning "
                    "reversal where YHWH's deliverance is proclaimed 'to a people yet unborn' "
                    "(22:31). Together these psalms form the suffering-to-glory arc that defines "
                    "the messianic hope.",

        "key_verse": {
            "ref": "Psalm 22:1",
            "text": "My God, my God, why have you forsaken me? Why are you so far from saving me, from the words of my groaning?",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "miktam (a psalm type of uncertain meaning -- possibly 'inscription' or 'golden psalm')",
            "chasid (faithful one/holy one -- the one devoted to YHWH who is preserved from Sheol)",
            "shachat (pit/corruption -- the grave; YHWH will not allow his chasid to decay)",
            "eli eli lamah azavtani (my God my God why have you forsaken me -- the opening cry of Ps 22)",
            "kaaru (they pierced -- the disputed reading of Ps 22:16; MT has ka'ari, 'like a lion')",
            "yechalqu (they divide -- casting lots for garments; fulfilled at the cross)",
            "adat mere'im (congregation of evildoers -- the hostile assembly surrounding the sufferer)"
        ],

        "ane_backdrop": "The individual lament of Psalm 22 follows the standard pattern of ANE "
                        "complaint prayers: invocation, complaint, petition, vow of praise. "
                        "Mesopotamian 'righteous sufferer' texts (Ludlul Bel Nemeqi, the Babylonian "
                        "Theodicy) describe the experience of divine abandonment and physical "
                        "suffering followed by divine restoration. The 'bulls of Bashan' (22:12) "
                        "likely reference the powerful cattle of the Transjordan region, a metaphor "
                        "for powerful enemies. The description of encirclement by hostile forces -- "
                        "'dogs encompass me; a company of evildoers encircles me' (22:16) -- echoes "
                        "the ANE motif of the besieged king surrounded by demonic forces, found in "
                        "Mesopotamian exorcism texts. The division of garments (22:18) reflects the "
                        "spoil-taking practice after military victory or execution.",

        "second_temple": [
            {
                "source": "Acts 2:25-31",
                "summary": "Peter quotes Psalm 16:8-11 at Pentecost, arguing that David was not "
                           "speaking of himself (since David died and his tomb was known) but "
                           "prophetically of Christ: 'He foresaw and spoke about the resurrection "
                           "of the Christ, that he was not abandoned to Hades, nor did his flesh "
                           "see corruption.'",
                "relevance": "Peter's argument establishes the interpretive principle that David spoke "
                             "as a prophet about a descendant who would be raised from the dead."
            },
            {
                "source": "Matthew 27:35-46",
                "summary": "The Gospel accounts narrate the fulfillment of Psalm 22 in precise "
                           "detail: the dividing of garments (27:35), the mockery (27:39-43), and "
                           "Jesus' cry from the cross quoting Psalm 22:1.",
                "relevance": "The evangelists understood Psalm 22 as a prophetic script that Jesus "
                             "enacted on the cross -- the suffering righteous one par excellence."
            },
            {
                "source": "Pesikta Rabbati 36",
                "summary": "A medieval midrash that preserves earlier traditions about the "
                           "suffering Messiah ben Ephraim, applying elements of Psalm 22 to a "
                           "messianic figure who suffers before the redemption.",
                "relevance": "Jewish tradition preserved a strand of messianic suffering connected to "
                             "Psalm 22, parallel to and independent of the Christian reading."
            }
        ],

        "cross_refs": [
            {"ref": "Acts 2:25-31", "note": "Peter's Pentecost sermon quoting Ps 16:8-11 as a prophecy of Jesus' resurrection", "type": "nt"},
            {"ref": "Matthew 27:46", "note": "Jesus quotes Ps 22:1 from the cross: 'Eli, Eli, lema sabachthani?'", "type": "nt"},
            {"ref": "John 19:23-24", "note": "The soldiers cast lots for Jesus' garment, fulfilling Ps 22:18", "type": "nt"},
            {"ref": "Isaiah 53:3-12", "note": "The Suffering Servant parallels -- despised, rejected, pierced, bearing the sins of many", "type": "ot"},
            {"ref": "Hebrews 2:12", "note": "'I will tell of your name to my brothers; in the midst of the congregation I will sing your praise' -- quoting Ps 22:22 as Christ's words", "type": "nt"},
            {"ref": "Philippians 2:8-11", "note": "The pattern of humiliation-to-exaltation that Psalm 22 prefigures in its suffering-to-praise arc", "type": "nt"},
            {"ref": "Psalm 16:10 (Acts 13:35)", "note": "'You will not let your Holy One see corruption' -- Paul in Antioch applies this to Jesus' resurrection", "type": "nt"}
        ],

        "divine_council_note": "Psalm 22 moves from the cry of dereliction to a cosmic proclamation "
                               "scene. The sufferer, after being delivered, declares: 'I will tell of "
                               "your name to my brothers; in the midst of the congregation (qahal) I "
                               "will praise you' (22:22). The word qahal can mean both the earthly "
                               "assembly and the heavenly assembly. The psalm then expands to universal "
                               "scope: 'All the ends of the earth shall remember and turn to the LORD, "
                               "and all the families of the nations shall worship before you' (22:27). "
                               "This is a reversal of the Deuteronomy 32 disinheritance -- the nations "
                               "that were allotted to other elohim are now turning to YHWH because of "
                               "the suffering and deliverance of the righteous one. Verse 28 provides "
                               "the theological basis: 'For kingship belongs to the LORD, and he rules "
                               "over the nations.' YHWH's sovereignty extends over every territory, "
                               "regardless of which elohim was assigned to govern it. The closing verse "
                               "reaches forward into history: 'They shall come and proclaim his "
                               "righteousness to a people yet unborn, that he has done it' (22:31). "
                               "The Hebrew ki asah ('that he has done it') is a declaration of "
                               "accomplished redemption -- parallel to Jesus' tetelestai ('it is "
                               "finished') in John 19:30. Psalm 16 contributes the resurrection "
                               "component: YHWH will not abandon his chasid to Sheol. The divine "
                               "council theology here is that YHWH's faithful agent, though "
                               "overwhelmed by the 'congregation of evildoers' (adat mere'im -- a "
                               "term that may evoke hostile spiritual forces), will be vindicated, "
                               "raised, and proclaimed as Lord over all nations.",

        "sections": [
            {
                "heading": "Psalm 16: The Path of Life Beyond Death",
                "body": "'Preserve me, O God (El), for in you I take refuge (chasiti)' (16:1). "
                        "This <em>miktam</em> of David -- a psalm type whose name likely means "
                        "'inscription' or 'golden psalm,' suggesting a particularly precious or "
                        "permanent composition (see the glossary in the Book I Synthesis) -- opens "
                        "with a declaration of total dependence on YHWH. "
                        "Verse 2 affirms: 'I say to YHWH, You are my Lord (adonai); I have no good "
                        "apart from you.' The psalmist then contrasts those who 'run after another "
                        "god' (16:4) -- whose sorrows multiply -- with his own contentment: 'YHWH "
                        "is my chosen portion and my cup; you hold my lot' (16:5). The inheritance "
                        "language (nachalah, 16:6) echoes the Levitical portion: as the Levites "
                        "received YHWH himself as their inheritance rather than land, so the psalmist "
                        "possesses YHWH as his ultimate good. The theological core comes in 16:10: "
                        "'For you will not abandon my soul (nafshi) to Sheol, or let your holy one "
                        "(chasidkha) see corruption (shachat).' The word shachat means both 'pit' "
                        "and 'corruption/decay.' David expresses confidence that YHWH's faithful "
                        "one will not remain in the grave. Verse 11 closes with one of the most "
                        "luminous promises in the Psalter: 'You make known to me the path of life "
                        "(orach chayyim); in your presence there is fullness of joy (simchot); at "
                        "your right hand are pleasures forevermore (ne'imot netsach).' The 'right "
                        "hand' is the place of honor in the divine council -- the same position "
                        "offered to the king in Psalm 110:1."
            },
            {
                "heading": "Psalm 22: The Cry of Dereliction (22:1-11)",
                "body": "'My God, my God, why have you forsaken me?' (22:1). The opening cry is "
                        "the most devastating in Scripture -- a covenant partner experiencing the "
                        "absence of the God who promised never to leave (Deut 31:6, 8; Josh 1:5). "
                        "The juxtaposition with trust is deliberate: 'Yet you are holy, enthroned "
                        "on the praises of Israel' (22:3). YHWH has not ceased to be holy or "
                        "sovereign; the sufferer knows this. The ancestors trusted and were "
                        "delivered (22:4-5), but the sufferer is 'a worm (tola'at) and not a man, "
                        "scorned by mankind and despised by the people' (22:6). The mockery is "
                        "theologically loaded: 'He trusts in YHWH; let him deliver him; let him "
                        "rescue him, for he delights in him' (22:8) -- words virtually identical "
                        "to the taunts at the crucifixion (Matt 27:43). The sufferer appeals to "
                        "the intimacy of his origin: 'You are he who took me from the womb; you "
                        "made me trust you at my mother's breasts. On you was I cast from my birth' "
                        "(22:9-10). From the womb to the cross, YHWH has been his only God."
            },
            {
                "heading": "Psalm 22: The Passion and the Reversal (22:12-31)",
                "body": "The enemies are described in bestial terms: 'Many bulls encompass me; "
                        "strong bulls of Bashan surround me' (22:12). Bashan was the territory of "
                        "Og, the last of the Rephaim (Deut 3:11), and was associated with demonic "
                        "forces in Israelite tradition. The physical suffering is graphically "
                        "rendered: 'I am poured out like water, and all my bones are out of joint; "
                        "my heart is like wax; it is melted within my breast. My strength is dried "
                        "up like a potsherd, and my tongue sticks to my jaws; you lay me in the "
                        "dust of death' (22:14-15). The disputed verse 22:16 reads: 'they have "
                        "pierced my hands and my feet' (kaaru -- found in the Dead Sea Scrolls "
                        "and LXX; the Masoretic Text has ka'ari, 'like a lion'). Verse 18 describes "
                        "the division of garments: 'they divide my garments among them, and for my "
                        "clothing they cast lots.' Then the reversal begins abruptly at 22:21b: "
                        "'You have rescued me (anitani)!' The suffering is over; deliverance has "
                        "come. The rescued sufferer vows to praise YHWH 'in the midst of the "
                        "congregation (qahal)' (22:22). The scope expands: 'All the ends of the "
                        "earth shall remember and turn to YHWH' (22:27). Even the dead shall worship: "
                        "'All who go down to the dust shall bow before him' (22:29). The final verse "
                        "reaches into the future: the deliverance will be proclaimed 'to a people "
                        "yet unborn, that he has done it (ki asah)' -- accomplished, finished."
            }
        ]
    },

    {
        "id": "ps-23-24",
        "ref": "Psalms 23-24",
        "chapter_num": 4,
        "title": "The Shepherd and the King of Glory",
        "era": "psalms_book1",
        "type": "chapter",

        "synopsis": "Psalms 23 and 24 form a natural pair following the passion of Psalm 22. After "
                    "the suffering and vindication of the righteous one, Psalm 23 presents YHWH as "
                    "the divine shepherd (ro'i) who leads through the valley of the shadow of death "
                    "(tsalmawet), and Psalm 24 presents YHWH as the King of Glory (melek hakavod) "
                    "entering his sanctuary in triumphal procession. The progression is deliberate: "
                    "suffering (22) -> restoration (23) -> enthronement (24). Psalm 23 is the most "
                    "beloved psalm in the Psalter, a six-verse masterpiece that moves from pasture "
                    "to table, from shepherd imagery to host imagery, from following to dwelling. "
                    "Psalm 24 is a liturgical processional psalm where the gates of the temple (or "
                    "of heaven itself) are summoned to open for the arrival of the warrior-king who "
                    "is 'YHWH of hosts (tseva'ot), he is the King of Glory' (24:10).",

        "key_verse": {
            "ref": "Psalm 24:7-8",
            "text": "Lift up your heads, O gates! And be lifted up, O ancient doors, that the King of glory may come in. Who is this King of glory? The LORD, strong and mighty, the LORD, mighty in battle!",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ro'i (my shepherd -- YHWH as the divine shepherd of Israel, a royal ANE title)",
            "tsalmawet (shadow of death/deep darkness -- the darkest valley; possibly 'death-shadow')",
            "shevet (rod -- the shepherd's weapon against predators)",
            "mishenet (staff -- the shepherd's guiding tool)",
            "melek hakavod (King of Glory -- YHWH as the triumphant divine warrior entering the sanctuary)",
            "sha'ar (gate -- the gates of the temple or the cosmic gates of heaven)",
            "YHWH tseva'ot (LORD of hosts -- the commander of the heavenly armies; a divine council title)"
        ],

        "ane_backdrop": "The shepherd-king is a ubiquitous ANE royal title. Hammurabi calls himself "
                        "'the shepherd called by Enlil.' Egyptian pharaohs carried the crook and flail "
                        "as shepherd symbols. The Sumerian king Gudea was 'the faithful shepherd.' In "
                        "every case, the shepherd-king provides, protects, and leads. YHWH as shepherd "
                        "(Ps 23) claims the title that ANE kings claimed for themselves -- he is the "
                        "true king who provides for his people. The processional liturgy of Psalm 24 "
                        "parallels the Babylonian akitu (New Year) festival, where the statue of "
                        "Marduk was carried in procession through the Ishtar Gate and re-enthroned "
                        "in his temple. The Ugaritic Baal Cycle describes Baal's entry into his "
                        "newly built palace after defeating Yam -- a triumphal procession of the "
                        "divine warrior into his dwelling. Psalm 24 places YHWH in this role: the "
                        "warrior-king who has conquered enters his temple/palace in glory.",

        "second_temple": [
            {
                "source": "John 10:11, 14",
                "summary": "Jesus declares 'I am the good shepherd. The good shepherd lays down his "
                           "life for the sheep.' He identifies himself with the divine shepherd of "
                           "Psalm 23 and adds the element of sacrificial death.",
                "relevance": "Jesus' self-identification as the Good Shepherd is a direct claim to the "
                             "YHWH-shepherd role of Psalm 23, with the suffering of Psalm 22 integrated."
            },
            {
                "source": "Midrash Tehillim 24:7",
                "summary": "Rabbinic tradition interprets the 'gates lifting their heads' as the "
                           "gates of the temple -- or the gates of heaven -- opening for the ark "
                           "of the covenant (YHWH's throne) during Solomon's dedication.",
                "relevance": "The rabbinic reading connects Psalm 24 to the temple dedication, where "
                             "the divine presence entered the Most Holy Place and the kavod filled "
                             "the house (1 Kings 8:10-11)."
            }
        ],

        "cross_refs": [
            {"ref": "Ezekiel 34:11-16", "note": "'I myself will be the shepherd of my sheep' -- YHWH takes over the shepherding role from Israel's failed leaders", "type": "ot"},
            {"ref": "John 10:11", "note": "'I am the good shepherd. The good shepherd lays down his life for the sheep' -- Jesus claims the YHWH-shepherd identity", "type": "nt"},
            {"ref": "Revelation 7:17", "note": "'The Lamb in the midst of the throne will be their shepherd, and he will guide them to springs of living water'", "type": "nt"},
            {"ref": "1 Kings 8:10-11", "note": "The kavod of YHWH fills the temple -- the King of Glory entering his sanctuary as in Psalm 24", "type": "ot"},
            {"ref": "Psalm 22:1", "note": "The suffering that precedes the restoration of Ps 23 and the enthronement of Ps 24", "type": "ot"},
            {"ref": "Isaiah 40:11", "note": "'He will tend his flock like a shepherd; he will gather the lambs in his arms' -- the shepherd theology of Ps 23", "type": "ot"},
            {"ref": "Hebrews 13:20", "note": "'The great shepherd of the sheep' -- Jesus as the fulfillment of the divine shepherd", "type": "nt"}
        ],

        "divine_council_note": "Psalm 24 is a divine council processional. The question-and-answer "
                               "liturgy at the gates -- 'Who is this King of Glory?' / 'YHWH, strong "
                               "and mighty, YHWH mighty in battle' (24:8) -- depicts the moment when "
                               "the divine warrior returns from victory and enters the heavenly (or "
                               "earthly) sanctuary. The title melek hakavod ('King of Glory') is a "
                               "throne-room title: kavod is the radiant, weighty presence of YHWH "
                               "that fills the temple and overwhelms all other powers. The title "
                               "'YHWH tseva'ot' (24:10) -- 'LORD of hosts' -- identifies YHWH as the "
                               "commander of the heavenly army, the same tseva (host) whose commander "
                               "(sar) appeared to Joshua with a drawn sword (Josh 5:14). The gates are "
                               "personified and commanded to lift their heads -- as if the ancient doors "
                               "themselves must acknowledge the authority of the approaching king. The "
                               "cosmic scope is established in 24:1-2: 'The earth is YHWH's and the "
                               "fullness thereof, the world and those who dwell therein, for he has "
                               "founded it upon the seas and established it upon the rivers.' The "
                               "creation foundation establishes YHWH's ownership of all territory -- "
                               "he is not one god among many but the creator and possessor of the "
                               "entire world. The processional entry of the King of Glory into his "
                               "sanctuary is the ultimate assertion of cosmic sovereignty.",

        "sections": [
            {
                "heading": "Psalm 23: YHWH as Shepherd (23:1-4)",
                "body": "'YHWH is my shepherd (ro'i); I shall not want' (23:1). The opening "
                        "declaration is a covenant confession: the divine king has personally "
                        "assumed responsibility for the psalmist's provision. 'He makes me lie "
                        "down in green pastures (bi-ne'ot deshe). He leads me beside still waters "
                        "(me menuchot). He restores my soul (nafshi)' (23:2-3). Every image speaks "
                        "of abundant provision and restoration. The 'still waters' are waters of "
                        "rest -- the opposite of the chaotic waters that threaten to overwhelm. "
                        "'He leads me in paths of righteousness (ma'aglei-tsedeq) for his name's "
                        "sake' (23:3b). The guidance is not for the sheep's merit but for the "
                        "shepherd's reputation -- YHWH's name is at stake. The central verse: "
                        "'Even though I walk through the valley of the shadow of death (gei "
                        "tsalmawet), I will fear no evil, for you are with me; your rod (shevet) "
                        "and your staff (mishenet), they comfort me' (23:4). The tsalmawet valley "
                        "is the darkest place in the created order -- the threshold of death itself. "
                        "The rod is the weapon the shepherd uses against predators; the staff is "
                        "the crook used to guide and rescue. In the darkest place, the shepherd's "
                        "presence is sufficient."
            },
            {
                "heading": "Psalm 23: YHWH as Host (23:5-6) and Psalm 24: The King of Glory",
                "body": "The imagery shifts from shepherd to host: 'You prepare a table before me "
                        "in the presence of my enemies; you anoint my head with oil; my cup "
                        "overflows' (23:5). The table in the presence of enemies is a victory "
                        "banquet -- the host provides abundantly while the hostile forces can only "
                        "watch. The anointing with oil is a sign of honor and joy (cf. Ps 45:7). "
                        "The psalm closes with a declaration of permanent dwelling: 'Surely goodness "
                        "and mercy (chesed) shall follow me all the days of my life, and I shall "
                        "dwell in the house of YHWH forever (le'orek yamim)' (23:6). The 'house of "
                        "YHWH' is the temple -- the earthly counterpart of the heavenly throne room. "
                        "Psalm 24 then opens with a cosmic ownership claim: 'The earth is YHWH's "
                        "and the fullness thereof' (24:1). Who may ascend YHWH's hill? 'He who has "
                        "clean hands and a pure heart, who does not lift up his soul to what is "
                        "false' (24:4). Then the liturgical climax: 'Lift up your heads, O gates! "
                        "And be lifted up, O ancient doors, that the King of Glory may come in!' "
                        "(24:7). The question echoes: 'Who is this King of Glory?' The answer: "
                        "'YHWH of hosts (tseva'ot) -- he is the King of Glory!' (24:10). The "
                        "divine warrior, commander of the heavenly army, enters his sanctuary in "
                        "triumph. The progression is complete: suffering (22), restoration (23), "
                        "enthronement (24)."
            }
        ]
    },

    {
        "id": "ps-29",
        "ref": "Psalm 29",
        "chapter_num": 5,
        "title": "The Voice of YHWH -- Storm Theophany and Canaanite Polemic",
        "era": "psalms_book1",
        "type": "chapter",

        "synopsis": "Psalm 29 is the great storm theophany psalm -- a hymn that calls on the 'sons "
                    "of God' (bene elim) to ascribe glory to YHWH as his voice (qol YHWH) thunders "
                    "over the cosmic waters. Seven times 'the voice of YHWH' reverberates: breaking "
                    "cedars, flashing fire, shaking the wilderness, stripping forests bare. Scholars "
                    "have long recognized that Psalm 29 engages directly with Canaanite storm-god "
                    "theology: Baal was the storm god of Ugarit, the rider of the clouds, whose "
                    "voice was thunder. Psalm 29 takes every attribute of Baal and assigns it to "
                    "YHWH. This is not syncretism but polemic: the psalm declares that YHWH, not "
                    "Baal, is the true lord of the storm, the true voice over the waters, the true "
                    "king enthroned above the flood (mabbul). It opens with a divine council scene "
                    "and closes with YHWH enthroned as king forever.",

        "key_verse": {
            "ref": "Psalm 29:1-2",
            "text": "Ascribe to the LORD, O heavenly beings, ascribe to the LORD glory and strength. Ascribe to the LORD the glory due his name; worship the LORD in the splendor of holiness.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "bene elim (sons of God/sons of the mighty -- the divine council members called to worship YHWH)",
            "qol YHWH (voice of YHWH -- the thunder of the storm; appears seven times)",
            "kavod (glory -- the weighty, radiant presence that the elohim must ascribe to YHWH)",
            "mabbul (flood/deluge -- the cosmic waters; the same word used for Noah's flood in Gen 6-9)",
            "hadrat-qodesh (splendor of holiness -- the holy adornment of worship in the divine council)",
            "oz (strength/power -- YHWH's might manifested in the storm)",
            "yashav (to sit/be enthroned -- YHWH seated as king over the flood forever)"
        ],

        "ane_backdrop": "Psalm 29 is the most explicitly Canaanite-polemic psalm in the Psalter. The "
                        "Ugaritic Baal Cycle (KTU 1.1-1.6, ~1400-1200 BC) describes Baal as the "
                        "storm god whose voice is thunder: 'Baal gives forth his holy voice, Baal "
                        "repeats the utterance of his lips. His holy voice shatters the earth; at "
                        "his roaring the mountains quake' (KTU 1.4.VII.29-35). The parallels with "
                        "Psalm 29 are striking: both describe a divine voice over the waters that "
                        "breaks cedars and shakes mountains. Baal is called 'rider of the clouds' "
                        "(rkb 'rpt) -- a title YHWH claims in Psalm 68:4. The geographic references "
                        "in Psalm 29 (Lebanon, Sirion/Hermon, the wilderness of Kadesh) trace Baal's "
                        "traditional territory. The psalm strips Baal of every attribute and assigns "
                        "them to YHWH. The opening call to the bene elim -- the sons of God in the "
                        "divine council -- to worship YHWH is a declaration that even the divine "
                        "beings who might have been identified with Baal must bow to YHWH. He alone "
                        "sits enthroned over the mabbul (flood) -- the cosmic waters that represent "
                        "primordial chaos.",

        "second_temple": [
            {
                "source": "Targum on Psalm 29:1",
                "summary": "The Targum renders bene elim as 'companies of angels' (katey "
                           "mal'akhaya), clarifying the divine council reference for the synagogue.",
                "relevance": "The Targumic tradition confirms that bene elim was understood as a "
                             "reference to heavenly beings, not human worshippers."
            },
            {
                "source": "Midrash Tehillim 29:1",
                "summary": "The midrash connects Psalm 29 to the giving of Torah at Sinai, "
                           "interpreting the seven 'voices of YHWH' as the seven thunders that "
                           "accompanied the theophany.",
                "relevance": "The rabbinic connection of Psalm 29 to Sinai reinforces the theophanic "
                             "character of the psalm: YHWH's voice over the storm is the same voice "
                             "that spoke from the mountain."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 68:4", "note": "'Sing to God, ride through the deserts; his name is YAH' -- some translations 'rider of the clouds,' the Baal title claimed by YHWH", "type": "ot"},
            {"ref": "Psalm 93:3-4", "note": "'The floods have lifted up their voice... mightier than the thunders of many waters, mightier than the waves of the sea, YHWH on high is mighty'", "type": "ot"},
            {"ref": "Job 38:1", "note": "'Then YHWH answered Job out of the whirlwind' -- the storm theophany tradition", "type": "ot"},
            {"ref": "1 Kings 19:11-12", "note": "YHWH's presence at Horeb -- wind, earthquake, fire, then a still small voice; the storm elements without the storm", "type": "ot"},
            {"ref": "Revelation 4:5", "note": "'From the throne came flashes of lightning, and rumblings and peals of thunder' -- the divine council scene with storm theophany", "type": "nt"},
            {"ref": "Psalm 82:1", "note": "'God has taken his place in the divine council; in the midst of the gods he holds judgment' -- the assembly Psalm 29 calls to worship", "type": "ot"}
        ],

        "divine_council_note": "Psalm 29 opens with a direct address to the divine council: 'Ascribe "
                               "to YHWH, O bene elim, ascribe to YHWH glory and strength' (29:1). The "
                               "phrase bene elim ('sons of God' or 'sons of the mighty') is a divine "
                               "council designation -- the same class of beings as the bene elohim of "
                               "Job 1:6; 2:1; 38:7 and the bene elyon of Psalm 82:6. The council "
                               "members are commanded to worship YHWH in hadrat-qodesh ('the splendor "
                               "of holiness') -- the holy array of the heavenly court. This is a "
                               "throne-room scene: the elohim stand before YHWH and declare his kavod "
                               "(glory). The seven occurrences of 'the voice of YHWH' (29:3-9) "
                               "describe YHWH's power over every domain of creation: waters, cedars, "
                               "mountains, lightning, wilderness, forests. Where Baal's domain was "
                               "limited to specific territories, YHWH's voice shakes all creation. "
                               "The climax is verse 10: 'YHWH sits enthroned over the flood (mabbul); "
                               "YHWH sits enthroned as king forever.' The word mabbul occurs only here "
                               "and in Genesis 6-9 (the Noah flood). YHWH is enthroned over the "
                               "primordial chaos waters -- the same waters that in Canaanite mythology "
                               "Yam (Sea) wielded against Baal. YHWH does not merely defeat the chaos "
                               "waters; he sits on them as his throne. The closing verse (29:11) "
                               "declares: 'YHWH gives strength to his people; YHWH blesses his people "
                               "with peace (shalom).' The God who commands the storms and sits above "
                               "the flood uses his power not for cosmic warfare alone but for the "
                               "blessing and peace of his covenant people.",

        "sections": [
            {
                "heading": "The Call to the Divine Council (29:1-2)",
                "body": "'Ascribe (havu) to YHWH, O bene elim, ascribe to YHWH glory (kavod) and "
                        "strength (oz)' (29:1). The verb havu ('give, ascribe') is a command "
                        "directed to the heavenly beings: they are to render to YHWH the kavod "
                        "that belongs to him. The triple repetition of 'ascribe to YHWH' creates "
                        "a liturgical crescendo. The bene elim are not human worshippers but "
                        "divine council members -- the 'sons of the mighty' who serve in YHWH's "
                        "heavenly court. They are commanded to 'worship YHWH in hadrat-qodesh' "
                        "(29:2) -- 'the splendor of holiness' or 'holy array.' This is the dress "
                        "code of the divine court: the elohim appear before YHWH in sacred "
                        "adornment, their holiness reflecting his. The scene parallels Isaiah "
                        "6:1-3, where the seraphim cry 'Holy, holy, holy is YHWH of hosts,' and "
                        "1 Kings 22:19, where Micaiah sees YHWH seated on his throne with the "
                        "host of heaven standing at his right and left. Psalm 29 begins where "
                        "all true worship begins: in the heavenly council, before the throne."
            },
            {
                "heading": "The Seven Voices -- Storm Theophany (29:3-9)",
                "body": "Seven times the psalm declares 'the voice of YHWH' (qol YHWH), and each "
                        "time the voice manifests a different aspect of divine power. (1) 'The "
                        "voice of YHWH is over the waters; the God of glory (El hakavod) thunders; "
                        "YHWH is over many waters' (29:3). The 'many waters' (mayim rabbim) are "
                        "the cosmic waters -- the primordial deep that YHWH commands. (2) 'The "
                        "voice of YHWH is powerful (bakoach)' (29:4a). (3) 'The voice of YHWH is "
                        "full of majesty (behadar)' (29:4b). (4) 'The voice of YHWH breaks the "
                        "cedars; YHWH breaks the cedars of Lebanon' (29:5). Lebanon's cedars were "
                        "the strongest trees in the ancient world -- symbols of human pride (Isa "
                        "2:13) and divine territory. (5) 'He makes Lebanon skip like a calf, and "
                        "Sirion like a young wild ox' (29:6). Sirion is the Sidonian name for "
                        "Mount Hermon -- Baal's sacred mountain in Canaanite tradition. YHWH's "
                        "voice makes Baal's mountain dance. (6) 'The voice of YHWH flashes forth "
                        "flames of fire' (29:7). (7) 'The voice of YHWH shakes the wilderness; "
                        "YHWH shakes the wilderness of Kadesh' (29:8). From the cosmic waters to "
                        "the desert, YHWH's voice controls every domain. 'In his temple all cry, "
                        "Glory! (kavod)' (29:9b). The heavenly temple resounds with the worship "
                        "the psalm opened by commanding."
            },
            {
                "heading": "Enthroned Over the Flood (29:10-11)",
                "body": "'YHWH sits enthroned (yashav) over the flood (mabbul); YHWH sits "
                        "enthroned as king (melek) forever' (29:10). This single verse is the "
                        "theological climax. The word mabbul appears only here and in Genesis "
                        "6-9 -- the great flood that destroyed the first world. YHWH is enthroned "
                        "above those primordial chaos waters. In Canaanite mythology, Yam (Sea) "
                        "was Baal's rival -- the chaos force that threatened cosmic order. Baal "
                        "defeated Yam in combat (KTU 1.2.IV) and was proclaimed king. Psalm 29 "
                        "declares that YHWH does not merely defeat the chaos waters; he sits on "
                        "them. They are his footstool, not his adversary. His kingship is 'forever' "
                        "(le'olam) -- unlike Baal, whose kingship in the Ugaritic texts is "
                        "threatened, lost, and recovered. YHWH's sovereignty is eternal and "
                        "unchallenged. The final verse translates this cosmic power into covenant "
                        "blessing: 'YHWH gives strength (oz) to his people; YHWH blesses his "
                        "people with peace (shalom)' (29:11). The oz that shattered cedars and "
                        "shook mountains is the same oz that strengthens Israel. The shalom that "
                        "follows the storm is not the absence of conflict but the established "
                        "order of the divine king -- a world where chaos has been subjected and "
                        "YHWH's people live under his protection."
            }
        ]
    },

    {
        "id": "ps-33-34",
        "ref": "Psalms 33-34",
        "chapter_num": 6,
        "title": "Creation by the Word and the Angel of YHWH",
        "era": "psalms_book1",
        "type": "chapter",

        "synopsis": "Psalms 33 and 34 round out the major theological themes of Book I. Psalm 33 is "
                    "a creation hymn celebrating YHWH's sovereign word: 'By the word (davar) of "
                    "YHWH the heavens were made, and by the breath (ruach) of his mouth all their "
                    "host' (33:6). This verse is the Psalter's clearest articulation of creation ex "
                    "nihilo by divine speech -- the same theology as Genesis 1 ('And God said...'). "
                    "The psalm emphasizes YHWH's sovereignty over the nations: he frustrates the "
                    "plans of the peoples and looks down from heaven on all mankind. Psalm 34 is an "
                    "acrostic psalm of David with a critical divine council element: 'The angel of "
                    "YHWH (malakh YHWH) encamps around those who fear him, and delivers them' (34:7). "
                    "The angel of YHWH is the visible, active agent of YHWH's protection -- the "
                    "heavenly warrior who stands guard over the covenant community.",

        "key_verse": {
            "ref": "Psalm 33:6",
            "text": "By the word of the LORD the heavens were made, and by the breath of his mouth all their host.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "davar (word -- the creative, commanding speech of YHWH that brings reality into existence)",
            "ruach (breath/spirit -- the life-giving exhalation of YHWH; the same word as 'Spirit')",
            "tseva'am (their host -- the heavenly bodies and/or angelic armies created by YHWH's breath)",
            "malakh YHWH (angel of YHWH -- the divine messenger/agent who encamps around the faithful)",
            "chanah (to encamp -- military encampment; the angel deploys a protective perimeter)",
            "ta'amu (taste -- 'taste and see that YHWH is good'; experiential knowledge of divine goodness)",
            "etsah (counsel/plan -- YHWH's sovereign purpose that stands forever, 33:11)"
        ],

        "ane_backdrop": "Creation by divine speech is attested in Egyptian theology. The Memphite "
                        "Theology (Shabaka Stone, ~700 BC, preserving older traditions) describes Ptah "
                        "creating all things through the thought of his heart and the command of his "
                        "tongue. The Mesopotamian Enuma Elish describes Marduk proving his divine "
                        "power by destroying and recreating a garment by his word. Psalm 33 places "
                        "YHWH's creative speech above all these parallels: the heavens and their entire "
                        "host (tseva) were made by his davar and ruach. The 'angel of YHWH' (malakh "
                        "YHWH) in Psalm 34:7 connects to the broader ANE concept of the divine "
                        "messenger -- in Ugaritic texts, the gods communicate and act through "
                        "messenger-agents. The Israelite malakh YHWH is distinctive because he "
                        "frequently acts with YHWH's own authority and is at times indistinguishable "
                        "from YHWH himself (Gen 16:7-13; Exod 3:2-6; Judg 6:11-23).",

        "second_temple": [
            {
                "source": "John 1:1-3",
                "summary": "'In the beginning was the Word (logos), and the Word was with God, and "
                           "the Word was God. All things were made through him.' John identifies "
                           "the 'word' of Psalm 33:6 with the pre-incarnate Christ.",
                "relevance": "The Johannine prologue reads Psalm 33:6 through a binitarian lens: the "
                             "davar by which YHWH created is a personal agent -- the Word who was "
                             "both 'with God' and 'was God.'"
            },
            {
                "source": "1 Peter 2:3",
                "summary": "'If indeed you have tasted that the Lord is good' -- quoting Ps 34:8, "
                           "applying it to believers' experience of Christ.",
                "relevance": "Peter's allusion identifies the 'LORD' whose goodness is tasted in "
                             "Psalm 34 with the risen Jesus."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 1:3, 6, 9, 14, 20, 24", "note": "'And God said...' -- the creation-by-speech pattern that Psalm 33:6 celebrates", "type": "ot"},
            {"ref": "John 1:1-3", "note": "The Word (logos) through whom all things were made -- the personal agent behind the davar of Ps 33:6", "type": "nt"},
            {"ref": "Genesis 16:7-13", "note": "The angel of YHWH appears to Hagar and is identified as YHWH himself -- the ambiguous divine agent of Ps 34:7", "type": "ot"},
            {"ref": "2 Kings 6:17", "note": "Elisha's servant sees 'horses and chariots of fire' surrounding them -- the visible manifestation of the angelic encampment of Ps 34:7", "type": "ot"},
            {"ref": "Hebrews 1:14", "note": "'Are they not all ministering spirits sent out to serve for the sake of those who are to inherit salvation?' -- the protective ministry of the malakh YHWH", "type": "nt"},
            {"ref": "Isaiah 55:10-11", "note": "'So shall my word be that goes out from my mouth; it shall not return to me empty' -- the efficacy of the divine word", "type": "ot"},
            {"ref": "Psalm 104:4", "note": "'He makes his messengers winds, his ministers a flaming fire' -- the angelic agents of the divine council", "type": "ot"}
        ],

        "divine_council_note": "Psalm 33:6 is a divine council creation text: 'By the word of YHWH "
                               "the heavens were made, and by the breath (ruach) of his mouth all their "
                               "host (tseva'am).' The 'host of heaven' (tseva hashamayim) is a "
                               "comprehensive term that includes both the celestial bodies (sun, moon, "
                               "stars) and the angelic beings associated with them (Deut 4:19; 1 Kings "
                               "22:19). YHWH's ruach -- his breath, his Spirit -- is the agent of "
                               "creation. This same ruach hovered over the waters in Genesis 1:2 and "
                               "gives life to all creatures (Ps 104:30). Psalm 33:10-11 asserts YHWH's "
                               "sovereignty over the nations: 'YHWH brings the counsel (etsah) of the "
                               "nations to nothing; he frustrates the plans of the peoples. The counsel "
                               "(etsah) of YHWH stands forever, the plans of his heart to all "
                               "generations.' The word etsah is the same word used for the deliberations "
                               "of the divine council (Jer 23:18, 22; cf. Isa 40:13-14). The nations' "
                               "plans -- presumably influenced by the territorial elohim who govern them "
                               "-- are overruled by YHWH's sovereign purpose. Psalm 34:7 introduces "
                               "another council figure: 'The angel (malakh) of YHWH encamps (chanah) "
                               "around those who fear him and delivers them.' The verb chanah is military: "
                               "the angel sets up a military encampment -- a protective perimeter of "
                               "heavenly force around the faithful. This is the same angelic military "
                               "presence that Elisha's servant saw at Dothan: 'horses and chariots of "
                               "fire' surrounding the prophet (2 Kings 6:17). The divine council does "
                               "not merely observe from heaven; its agents deploy on earth to protect "
                               "YHWH's people.",

        "sections": [
            {
                "heading": "Psalm 33: Creation by the Word (33:1-9)",
                "body": "Psalm 33 opens with a call to worship: 'Shout for joy in YHWH, O you "
                        "righteous! Praise befits the upright' (33:1). The call to 'sing to him "
                        "a new song (shir chadash)' (33:3) introduces the theme of creative "
                        "novelty -- the God who creates by speech always has something new to "
                        "declare. The theological core is 33:6-9: 'By the word (davar) of YHWH "
                        "the heavens were made, and by the breath (ruach) of his mouth all their "
                        "host. He gathers the waters of the sea as a heap (ned); he puts the "
                        "deeps in storehouses' (33:6-7). The word ned ('heap') is the same word "
                        "used for the waters standing up at the Red Sea (Exod 15:8) and the Jordan "
                        "(Josh 3:13, 16) -- linking creation, exodus, and conquest as acts of the "
                        "same sovereign word. 'Let all the earth fear YHWH; let all the inhabitants "
                        "of the world stand in awe of him' (33:8). The response to creation is not "
                        "scientific curiosity but reverent fear. 'For he spoke, and it came to be "
                        "(vayehi); he commanded, and it stood firm' (33:9). The verbal echo of "
                        "Genesis 1 is unmistakable: vayehi -- 'and it was' -- the creation "
                        "formula. YHWH's word is performative: what he speaks, exists."
            },
            {
                "heading": "Psalm 33: YHWH's Sovereignty Over the Nations (33:10-22)",
                "body": "'YHWH brings the counsel (etsah) of the nations to nothing; he frustrates "
                        "the plans of the peoples' (33:10). The nations have their own etsah -- "
                        "their own council deliberations -- but YHWH overrules them all. 'The "
                        "counsel of YHWH stands forever, the plans of his heart to all generations' "
                        "(33:11). Human and angelic powers may scheme, but YHWH's purpose is "
                        "eternal. 'YHWH looks down from heaven; he sees all the children of man; "
                        "from where he sits enthroned he looks out on all the inhabitants of the "
                        "earth' (33:13-14). The divine surveillance is comprehensive: no nation, no "
                        "king, no army escapes his gaze. 'The king is not saved by his great army; "
                        "a warrior is not delivered by his great strength. The war horse is a false "
                        "hope for salvation, and by its great might it cannot rescue' (33:16-17). "
                        "The message is clear: military power is irrelevant before YHWH's sovereign "
                        "will. 'Behold, the eye of YHWH is on those who fear him, on those who "
                        "hope in his steadfast love (chesed)' (33:18). The psalm closes with trust: "
                        "'Let your steadfast love, O YHWH, be upon us, even as we hope in you' "
                        "(33:22)."
            },
            {
                "heading": "What Is an Acrostic Psalm?",
                "body": "Psalm 34 is an <strong>acrostic psalm</strong> -- a poem in which the "
                        "first letter of each verse (or group of verses) follows the order of "
                        "the Hebrew alphabet, from <em>aleph</em> to <em>tav</em> (22 letters). "
                        "This means the psalm has a carefully structured pattern that would be "
                        "immediately visible to a Hebrew reader: each new line begins with the "
                        "next letter of the alphabet. The acrostic form served multiple purposes: "
                        "(1) It was a memory aid -- the alphabetic pattern made the psalm easier "
                        "to memorize. (2) It expressed completeness -- by running from A to Z "
                        "(aleph to tav), the psalmist symbolically covered the full range of the "
                        "topic, saying everything that can be said. (3) It demonstrated literary "
                        "mastery -- composing a coherent theological poem within the constraint of "
                        "an alphabetic pattern required extraordinary skill. Other acrostic psalms "
                        "include Psalms 9-10, 25, 37, 111, 112, and the monumental Psalm 119 (which "
                        "devotes eight verses to each Hebrew letter across 176 verses). Psalm 34's "
                        "acrostic is slightly irregular -- the <em>vav</em> line is missing and an "
                        "extra <em>pe</em> line is added at the end -- but the overall alphabetic "
                        "structure is clear."
            },
            {
                "heading": "Psalm 34: The Angel of YHWH Encamps (34:1-22)",
                "body": "This acrostic psalm is attributed to David 'when he changed his behavior "
                        "before Abimelech' (the Achish incident, 1 Sam 21:10-15). It opens with "
                        "praise: 'I will bless YHWH at all times; his praise shall continually be "
                        "in my mouth' (34:1). The invitation to experiential knowledge is famous: "
                        "'Oh, taste (ta'amu) and see that YHWH is good! Blessed is the man who "
                        "takes refuge in him' (34:8). The taste is not metaphorical abstraction "
                        "but lived encounter. The divine council element comes in 34:7: 'The "
                        "angel (malakh) of YHWH encamps (chanah) around those who fear him, and "
                        "delivers them.' The malakh YHWH is a figure of tremendous theological "
                        "significance in the OT -- at times identified with YHWH himself (Gen "
                        "16:13; Exod 3:2-6), at times a distinct agent sent from the divine "
                        "council (2 Sam 24:16; 2 Kings 19:35). The verb chanah indicates a "
                        "military deployment: the angel establishes a defensive position around "
                        "the faithful. This is not a single visit but a persistent garrison -- "
                        "the heavenly warrior stands guard. The psalm concludes with a promise "
                        "that echoes throughout the NT: 'He keeps all his bones; not one of them "
                        "is broken' (34:20). John 19:36 applies this to Jesus on the cross, "
                        "whose bones were not broken: 'These things took place that the Scripture "
                        "might be fulfilled: Not one of his bones will be broken.' The righteous "
                        "sufferer of Psalm 22, the shepherded soul of Psalm 23, and the protected "
                        "servant of Psalm 34 converge in the person of the Messiah."
            }
        ]
    },

    {
        "id": "ps-book1-themes",
        "ref": "Psalms 1-41",
        "chapter_num": 7,
        "title": "Book I Synthesis: The Divine Council Theology of the Davidic Psalms",
        "era": "psalms_book1",
        "type": "chapter",

        "synopsis": "Book I (Psalms 1-41) establishes the theological foundation for the entire "
                    "Psalter. Its major themes -- Torah piety (Ps 1), royal enthronement (Ps 2), "
                    "human dignity in the cosmic hierarchy (Ps 8), resurrection hope (Ps 16), "
                    "vicarious suffering (Ps 22), divine shepherding (Ps 23), triumphal entry "
                    "(Ps 24), storm theophany and Canaanite polemic (Ps 29), creation by the "
                    "word (Ps 33), and angelic protection (Ps 34) -- all converge on a single "
                    "theological vision: YHWH is the Most High God, enthroned above the divine "
                    "council, who has chosen a human king to rule on his behalf. This king suffers, "
                    "is vindicated, and will ultimately receive the nations as his inheritance. "
                    "Book I is overwhelmingly Davidic -- nearly every psalm bears the ledavid "
                    "superscription -- and its David is both the historical king and the prophetic "
                    "template for the coming Messiah.",

        "key_verse": {
            "ref": "Psalm 2:7-8",
            "text": "I will tell of the decree: The LORD said to me, 'You are my Son; today I have begotten you. Ask of me, and I will make the nations your heritage, and the ends of the earth your possession.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ledavid (of David/for David/belonging to David -- the superscription of most Book I psalms)",
            "mizmor (psalm -- a song accompanied by stringed instruments; the defining genre of the Psalter)",
            "selah (a liturgical notation of uncertain meaning -- possibly a musical interlude or a call to contemplation)",
            "lamenatseach (to the choirmaster -- the musical director of the temple liturgy)",
            "tefillah (prayer -- the psalms as direct address to YHWH from the covenant community)",
            "tehillah (praise -- the Hebrew title of the Psalter is Tehillim, 'Praises')"
        ],

        "ane_backdrop": "The collection of royal psalms in Book I reflects the ANE tradition of "
                        "royal hymnography. Egyptian, Sumerian, and Akkadian royal hymns celebrated "
                        "the king's divine sonship, military victories, and relationship with the "
                        "national deity. The Gudea Cylinders of Lagash (~2100 BC) contain hymns to "
                        "the king's piety and temple-building that parallel the Davidic psalms' "
                        "emphasis on Torah devotion and temple worship. The Hittite royal prayers "
                        "combine personal lament with national petition in ways that parallel the "
                        "individual laments of Book I. The Egyptian 'Hymn to the Aten' (Akhenaten, "
                        "~1350 BC) has been compared to Psalm 104, demonstrating the international "
                        "character of creation hymnography in the ANE.",

        "second_temple": [
            {
                "source": "Psalms of Solomon 17:21-32",
                "summary": "This Second Temple text (1st century BC) describes the coming Davidic "
                           "Messiah who will purge Jerusalem, rule the nations with a rod of iron "
                           "(echoing Ps 2:9), and establish righteousness.",
                "relevance": "The Psalms of Solomon demonstrate that the messianic reading of Book I's "
                             "royal psalms was well established before the NT period."
            },
            {
                "source": "11QPsa (Great Psalms Scroll)",
                "summary": "The largest Psalms manuscript from Qumran preserves a different ordering "
                           "of psalms and includes non-canonical compositions, suggesting the Psalter's "
                           "final form was still fluid in the 1st century BC.",
                "relevance": "The Qumran evidence shows that while individual psalms were authoritative, "
                             "the canonical arrangement of the five books was still being settled."
            }
        ],

        "cross_refs": [
            {"ref": "Luke 24:44", "note": "'Everything written about me in the Law of Moses and the Prophets and the Psalms must be fulfilled' -- Jesus identifies the Psalms as messianic Scripture", "type": "nt"},
            {"ref": "2 Samuel 23:1-2", "note": "'The Spirit of the LORD speaks by me; his word is on my tongue' -- David as prophetic psalmist", "type": "ot"},
            {"ref": "Acts 1:16", "note": "'The Scripture had to be fulfilled, which the Holy Spirit spoke beforehand by the mouth of David' -- the apostolic view of Davidic authorship as prophetic", "type": "nt"},
            {"ref": "Deuteronomy 32:8-9", "note": "The Most High's allotment of the nations to the sons of God -- the cosmic background to Book I's theology of divine sovereignty over the nations", "type": "ot"},
            {"ref": "1 Chronicles 16:7-36", "note": "David's psalm at the ark's transfer to Jerusalem -- a composite of Pss 96, 105, 106, showing David's psalmic activity", "type": "ot"},
            {"ref": "Ephesians 4:8", "note": "'When he ascended on high he led a host of captives' -- quoting Ps 68:18, the divine warrior's triumphal ascent", "type": "nt"}
        ],

        "divine_council_note": "Book I of the Psalter is the foundation of divine council theology in "
                               "the poetic books. Its key contributions: (1) The Most High laughs at "
                               "the rebellion of the nations and their rulers, because he has enthroned "
                               "his Son on Zion (Ps 2). (2) Humanity is positioned just below the "
                               "elohim in the cosmic hierarchy, crowned with glory and given dominion "
                               "(Ps 8). (3) The righteous sufferer is not abandoned but vindicated, and "
                               "his deliverance results in all nations turning to YHWH (Ps 22). (4) The "
                               "divine council members (bene elim) are summoned to worship YHWH as the "
                               "true storm God who sits enthroned above the flood (Ps 29). (5) YHWH "
                               "creates by his word and his breath/Spirit, bringing into existence the "
                               "entire 'host' -- both celestial bodies and angelic beings (Ps 33). (6) "
                               "The angel of YHWH -- a divine council agent -- deploys a military "
                               "encampment around the faithful (Ps 34). Together these themes describe "
                               "a cosmos governed by YHWH from his heavenly throne, populated by divine "
                               "beings who serve his purposes, and focused on a human king who mediates "
                               "YHWH's rule to the nations. The Davidic king is the linchpin: he is the "
                               "Son who receives the nations (Ps 2), the ben-adam crowned with glory "
                               "(Ps 8), the sufferer who is vindicated (Ps 22), and the shepherd's "
                               "beloved sheep who dwells in YHWH's house forever (Ps 23). Book I lays "
                               "the groundwork for the divine council drama that will intensify in "
                               "Books II-V, culminating in the explicit council scenes of Psalms 82 "
                               "and 89.",

        "sections": [
            {
                "heading": "Understanding Hebrew Poetry: Parallelism -- The Key to Reading the Psalms",
                "body": "Before reading any psalm, the reader must understand the single most "
                        "important literary device in Hebrew poetry: <strong>parallelism</strong>. "
                        "Unlike English poetry, which typically relies on rhyme and meter, Hebrew "
                        "poetry is built on the pairing (or tripling) of thought-lines that relate "
                        "to each other in specific ways. There are three main types:<br><br>"
                        "<strong>Synonymous parallelism</strong>: The second line restates or "
                        "intensifies the first. Example: 'The heavens declare the glory of God, / "
                        "and the sky above proclaims his handiwork' (Ps 19:1). Both lines say "
                        "essentially the same thing with different vocabulary.<br><br>"
                        "<strong>Antithetic parallelism</strong>: The second line contrasts with "
                        "the first. Example: 'For YHWH knows the way of the righteous, / but the "
                        "way of the wicked will perish' (Ps 1:6). The two lines set up a stark "
                        "opposition between two fates.<br><br>"
                        "<strong>Synthetic (or staircase) parallelism</strong>: The second line "
                        "builds on or completes the first, advancing the thought. Example: 'I lift "
                        "up my eyes to the mountains -- / from where does my help come?' (Ps 121:1). "
                        "The second line extends the idea rather than restating or contrasting it."
                        "<br><br>"
                        "Recognizing parallelism transforms how one reads the Psalms. When Psalm "
                        "2:1 says, 'Why do the nations rage / and the peoples plot in vain?', the "
                        "reader should understand that 'nations' and 'peoples' are the same group "
                        "described in parallel, not two different groups. Similarly, 'rage' and "
                        "'plot in vain' are two perspectives on the same rebellious activity. "
                        "Parallelism is the heartbeat of the Psalter -- once recognized, the poetry "
                        "comes alive."
            },
            {
                "heading": "Key Terms the Reader Will Encounter Throughout the Psalter",
                "body": "<strong>Tehillim</strong> (the Hebrew title of the Book of Psalms): "
                        "The word means 'Praises' and comes from the root <em>hallal</em>, 'to "
                        "praise.' Our English word 'Psalms' comes from the Greek <em>psalmoi</em> "
                        "(songs sung to stringed accompaniment), but the Hebrew name tells us "
                        "the Psalter's true identity: it is a book of praise.<br><br>"
                        "<strong>Mizmor</strong> (psalm): The most common superscription term, "
                        "appearing in 57 psalm titles. It means 'a song accompanied by stringed "
                        "instruments' -- from the root <em>zamar</em>, 'to pluck, to make music.' "
                        "When a psalm is called a <em>mizmor</em>, it was meant to be sung with "
                        "instrumental accompaniment, not merely read.<br><br>"
                        "<strong>Lamnatseakh</strong> (To the choirmaster / For the director of "
                        "music): This superscription appears in 55 psalms. It designates the psalm "
                        "for the professional musical director of Temple worship -- indicating "
                        "these were liturgical compositions performed in public worship, not "
                        "private devotions.<br><br>"
                        "<strong>Selah</strong>: This mysterious word appears 71 times in 39 "
                        "psalms (and 3 times in Habakkuk 3). Its exact meaning is debated, but "
                        "the most widely accepted theories are: (1) a musical interlude -- a "
                        "signal for the instruments to play while the singers pause; (2) a call "
                        "to 'lift up' (from the root <em>salal</em>, 'to raise') -- either "
                        "lifting the voice, the instruments, or one's attention; (3) a liturgical "
                        "marker meaning 'pause and reflect on what was just said.' The Septuagint "
                        "(the ancient Greek translation) rendered it <em>diapsalma</em>, meaning "
                        "'a musical interlude.' Whatever its precise meaning, Selah appears to "
                        "be a performance direction that signals a break in the singing -- a "
                        "moment to let the weight of the words sink in. When you encounter Selah "
                        "in a psalm, pause. The psalmist wants you to absorb what came before."
                        "<br><br>"
                        "<strong>Miktam</strong>: A psalm superscription found in Psalms 16 and "
                        "56-60. Its meaning is uncertain -- possibly from a root meaning 'to "
                        "cover' (suggesting an atonement psalm) or 'to inscribe' (suggesting a "
                        "psalm written as an inscription or engraved record). Some scholars "
                        "connect it to the Akkadian <em>katamu</em>, 'to cover.' The Septuagint "
                        "translated it as <em>stelographia</em>, 'an inscription on a pillar.' "
                        "These psalms tend to express deep trust in YHWH during mortal danger.<br><br>"
                        "<strong>Maskil</strong>: A superscription appearing in 13 psalms (32, "
                        "42, 44, 45, 52-55, 74, 78, 88, 89, 142). It derives from the root "
                        "<em>sakal</em>, meaning 'to be wise, to instruct, to give insight.' A "
                        "maskil is therefore a 'wisdom psalm' or 'instructional psalm' -- one "
                        "designed to impart understanding, not merely express emotion. When a "
                        "psalm is labeled <em>maskil</em>, approach it as a teacher intending "
                        "to make you wiser."
            },
            {
                "heading": "The Five-Book Structure of the Psalter",
                "body": "The Psalter is divided into five books, mirroring the five books of Moses "
                        "(Torah/Pentateuch). Each book ends with a doxology: Book I (Pss 1-41) "
                        "closes with 'Blessed be YHWH, the God of Israel, from everlasting to "
                        "everlasting! Amen and Amen' (41:13). Book II (42-72) closes with 'Blessed "
                        "be YHWH God, the God of Israel, who alone does wondrous things. Blessed be "
                        "his glorious name forever; may the whole earth be filled with his glory! "
                        "Amen and Amen!' (72:18-19). Book III (73-89) closes with 'Blessed be YHWH "
                        "forever! Amen and Amen' (89:52). Book IV (90-106) closes with 'Blessed be "
                        "YHWH, the God of Israel, from everlasting to everlasting! And let all the "
                        "people say, Amen! Praise YHWH!' (106:48). Book V (107-150) ends with the "
                        "grand finale: Psalm 150, where everything that has breath praises YHWH. "
                        "The five-book structure suggests that the Psalter is Israel's response to "
                        "Torah -- if the Pentateuch is God's word to Israel, the Psalms are Israel's "
                        "word back to God. Book I, corresponding roughly to Genesis, establishes "
                        "origins: the origin of the righteous path (Ps 1), the origin of the "
                        "Messianic hope (Ps 2), and the fundamental relationship between the "
                        "Creator and his human vice-regent (Ps 8)."
            },
            {
                "heading": "The Davidic Superscription and Prophetic Authority",
                "body": "Of the 41 psalms in Book I, 37 bear the superscription ledavid ('of David' "
                        "or 'belonging to David'). The preposition le can indicate authorship ('by "
                        "David'), dedication ('for David'), or association ('belonging to the "
                        "Davidic collection'). The NT treats the Davidic superscription as "
                        "indicating prophetic authorship: Peter at Pentecost argues that David, "
                        "'being a prophet and knowing that God had sworn with an oath to him that "
                        "he would set one of his descendants on his throne, he foresaw and spoke "
                        "about the resurrection of the Christ' (Acts 2:30-31). David's psalms are "
                        "not merely personal devotions but prophetic utterances spoken through the "
                        "Spirit about the coming king. The superscriptions sometimes include "
                        "historical settings -- Psalm 3 is connected to David's flight from "
                        "Absalom, Psalm 34 to his feigning madness before Achish/Abimelech. These "
                        "settings anchor the psalms in David's experience while leaving them open "
                        "to the broader messianic application that the NT authors will develop. "
                        "The Davidic collection of Book I is, in this sense, a prophetic corpus: "
                        "the voice of David is the voice of the Spirit speaking about the greater "
                        "David to come."
            }
        ]
    }
]
