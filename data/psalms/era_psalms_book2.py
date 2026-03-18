"""
era_psalms_book2.py -- Psalms 42-72 (Book II): Korah and Davidic Collections

Book II of the Psalter shifts from the predominantly Davidic voice of Book I
to include the Sons of Korah (Pss 42-49) alongside a second Davidic collection
(Pss 51-65, 68-70) and a Solomonic closing (Ps 72). The Korahite psalms
introduce the theology of Zion as the cosmic mountain -- the earthly
counterpart of YHWH's heavenly throne room -- and the divine king whose throne
is eternal. Key psalms include the royal wedding hymn (Ps 45) where the king
is addressed as elohim, the cosmic mountain theology of Psalms 46 and 48, the
divine warrior march of Psalm 68, and the Solomonic ideal king of Psalm 72.
Book II ends with the colophon 'The prayers of David, the son of Jesse, are
ended' (72:20), marking a structural boundary in the Psalter. The divine name
shifts: Book II predominantly uses Elohim rather than YHWH (the 'Elohistic
Psalter,' Pss 42-83), suggesting an editorial preference for the universal
divine name over the covenantal name.
"""

CHAPTERS = [
    {
        "id": "ps-42-43",
        "ref": "Psalms 42-43",
        "chapter_num": 1,
        "title": "The Korahite Longing -- Thirsting for the Living God",
        "era": "psalms_book2",
        "type": "chapter",
        "themes": ["EXILE", "HOLY", "SPIRIT"],

        "synopsis": "Psalms 42 and 43 are a single poem (42 has no separate superscription for 43 in "
                    "many manuscripts) that introduces the Sons of Korah collection with a cry of "
                    "spiritual exile. The psalmist is far from the temple, remembering the festive "
                    "procession with deep longing: 'As a deer pants for flowing streams, so pants "
                    "my soul for you, O God (Elohim). My soul thirsts for the living God (El Chai). "
                    "When shall I come and appear before the face of God (penei Elohim)?' (42:1-2). "
                    "The refrain punctuates the poem three times: 'Why are you cast down, O my soul, "
                    "and why are you in turmoil within me? Hope in God; for I shall again praise him, "
                    "my salvation and my God' (42:5, 11; 43:5). The psalmist's distress is deepened "
                    "by the taunt of his enemies: 'Where is your God?' (42:3, 10). The theological "
                    "crisis is the apparent absence of the God who is supposed to be present in his "
                    "sanctuary. Psalm 43 petitions for vindication: 'Send out your light and your "
                    "truth; let them lead me; let them bring me to your holy hill and to your "
                    "dwelling' (43:3). The Korahite psalms thus begin with the fundamental question: "
                    "how does one worship when separated from the place where YHWH has put his name?",

        "key_verse": {
            "ref": "Psalm 42:1-2",
            "text": "As a deer pants for flowing streams, so pants my soul for you, O God. My soul thirsts for God, for the living God. When shall I come and appear before God?",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "bene Qorach (Sons of Korah -- a Levitical guild of temple musicians descended from Korah)",
            "El Chai (the living God -- the God who is vitally present, not a dead idol)",
            "penei Elohim (the face of God -- the divine presence encountered in worship at the sanctuary)",
            "maskil (an instructional psalm -- a psalm intended to impart wisdom)",
            "tehom (deep -- the cosmic deep that calls to deep; primordial waters echoing the psalmist's turmoil)",
            "mishbar (breaker/wave -- YHWH's waves of affliction; cf. Jonah 2:3)"
        ],

        "ane_backdrop": "The Sons of Korah were a Levitical guild responsible for temple music "
                        "(1 Chr 6:31-38; 2 Chr 20:19). Despite Korah's rebellion against Moses "
                        "(Num 16), his descendants survived (Num 26:11) and became one of the most "
                        "important musical families in Israel's worship. The longing for the temple "
                        "reflects the ANE understanding of the temple as the intersection of heaven "
                        "and earth -- the place where the divine presence was accessible. Egyptian "
                        "and Mesopotamian texts describe the terror of being cut off from one's "
                        "temple and deity: the Babylonian exile prayers express similar anguish "
                        "over separation from Marduk's temple in Babylon.",

        "second_temple": [
            {
                "source": "2 Chronicles 20:19",
                "summary": "The Kohathites and Korahites stood to praise YHWH before Jehoshaphat's "
                           "battle -- the Sons of Korah as liturgical warriors.",
                "relevance": "The Korahite guild functioned as worship leaders in critical moments, "
                             "combining liturgy with spiritual warfare."
            }
        ],

        "cross_refs": [
            {"ref": "Numbers 16:1-35; 26:11", "note": "Korah's rebellion and the survival of his sons -- the origin of the Korahite guild", "type": "ot"},
            {"ref": "Psalm 84:1-2", "note": "'My soul longs, yes, faints for the courts of YHWH' -- another Korahite psalm of temple longing", "type": "ot"},
            {"ref": "John 7:37", "note": "'If anyone thirsts, let him come to me and drink' -- Jesus as the fulfillment of the thirst for the living God", "type": "nt"},
            {"ref": "Psalm 63:1", "note": "'O God, you are my God; earnestly I seek you; my soul thirsts for you' -- Davidic parallel to the Korahite thirst", "type": "ot"}
        ],

        "divine_council_note": "The phrase 'the living God' (El Chai) in 42:2 is a divine council "
                               "title that distinguishes YHWH from the 'dead' gods of the nations. "
                               "While the idols of the nations are inert -- they have mouths but do "
                               "not speak, eyes but do not see (Ps 115:4-7) -- YHWH is chai, alive, "
                               "active, present. The psalmist's longing to 'appear before the face of "
                               "God' (penei Elohim) is the desire to stand in the visible presence of "
                               "the enthroned king -- to have audience in the divine court. The temple "
                               "was understood as the earthly counterpart of the heavenly throne room; "
                               "to be cut off from the temple was to be exiled from the place where "
                               "heaven and earth intersect. The 'deep calls to deep' (tehom el-tehom "
                               "qore, 42:7) uses the word tehom -- the primordial deep of Genesis 1:2 "
                               "-- suggesting that the psalmist's inner turmoil mirrors the cosmic "
                               "chaos that preceded creation. Only the living God can bring order to "
                               "this inner tehom.",

        "sections": [
            {
                "heading": "Who Are the Sons of Korah?",
                "body": "The superscription 'Of the Sons of Korah' (<em>livnei-Qorach</em>) "
                        "appears in Psalms 42, 44-49, 84-85, 87-88 -- eleven psalms in total. "
                        "Readers encountering this attribution naturally ask: who are these people?"
                        "<br><br>"
                        "Korah was a Levite -- a descendant of Levi through Kohath (Exodus 6:16-24) "
                        "-- who led a rebellion against Moses and Aaron in the wilderness, "
                        "challenging their exclusive authority to lead and offer sacrifice "
                        "(Numbers 16:1-35). YHWH judged Korah dramatically: 'the ground under them "
                        "split apart, and the earth opened its mouth and swallowed them up' "
                        "(Numbers 16:31-32). It was one of the most dramatic divine judgments in "
                        "Israel's history.<br><br>"
                        "But here is the remarkable detail: <strong>Korah's sons did not die</strong>. "
                        "Numbers 26:11 explicitly states, 'The sons of Korah did not die.' They "
                        "survived their father's judgment and went on to become one of the most "
                        "important musical guilds in Israel's worship. First Chronicles 6:31-38 "
                        "traces their lineage and identifies them among the musicians David "
                        "appointed for the Temple. The prophet Samuel himself was a descendant "
                        "of Korah (1 Chronicles 6:33-38).<br><br>"
                        "The Korahite psalms are characterized by deep longing for God's presence, "
                        "love for the Temple, and rich Zion theology. There is a profound irony "
                        "in this: the descendants of the man who challenged YHWH's chosen place of "
                        "worship became the most passionate poets of worship in Israel. Their psalms "
                        "celebrate the very Temple their ancestor tried to circumvent. The story of "
                        "the Sons of Korah is a story of grace -- judgment on the rebel, mercy on "
                        "his children, and transformation of a cursed lineage into a lineage of praise."
            },
            {
                "heading": "Understanding 'Maskil' and 'Selah' in This Psalm",
                "body": "Psalm 42 is labeled a <em>maskil</em> -- an instructional or wisdom psalm "
                        "(from <em>sakal</em>, 'to give insight'). This means it is not simply a "
                        "personal lament but a teaching composition: the psalmist's experience of "
                        "spiritual desolation is presented as a lesson for the community on how to "
                        "hope in God during his apparent absence.<br><br>"
                        "Readers will also encounter <strong>Selah</strong> in Psalms 42-43 (which "
                        "form a single poem). Selah appears at the end of each occurrence of the "
                        "refrain: 'Why are you cast down, O my soul?' (42:5, 11; 43:5). In this "
                        "context, Selah functions as a musical and meditative pause -- it invites "
                        "the listener to stop, reflect on the question just asked ('why are you "
                        "cast down?'), and consider the answer ('hope in God'). The placement of "
                        "Selah at these emotional turning points suggests it was used to create "
                        "space for reflection between the despair and the hope."
            },
            {
                "heading": "Thirsting for God's Presence (42:1-5)",
                "body": "The psalm opens with one of the most evocative images in Scripture: a deer "
                        "(ayal) panting for flowing water in a dry land. The psalmist's soul is in "
                        "the same condition -- desperately longing for the God who gives life. The "
                        "phrase 'the living God' (El Chai) sets YHWH apart from every other deity: "
                        "he is not a concept or a distant force but a living being who can be "
                        "encountered. The question 'When shall I come and appear before the face "
                        "of God?' (42:2) is the question of the exile -- whether geographical "
                        "exile from the temple or the spiritual exile of divine silence. The "
                        "psalmist remembers the festive procession: 'how I would go with the "
                        "throng and lead them in procession to the house of God with glad shouts "
                        "and songs of praise, a multitude keeping festival' (42:4). The memory "
                        "of communal worship intensifies the present pain. The first refrain "
                        "answers the despair with hope: 'Hope in God (yachel l'Elohim); for I "
                        "shall again praise him, my salvation (yeshu'at) and my God' (42:5)."
            },
            {
                "heading": "Deep Calls to Deep (42:6-11) and the Petition (43:1-5)",
                "body": "'My soul is cast down within me; therefore I remember you from the land "
                        "of Jordan and of Hermon, from Mount Mizar' (42:6). The psalmist is in "
                        "the far north -- near the headwaters of the Jordan, at the foot of "
                        "Hermon -- geographically distant from Zion. The cosmic imagery intensifies: "
                        "'Deep calls to deep (tehom el-tehom qore) at the roar of your waterfalls; "
                        "all your breakers (mishbarekha) and your waves (gallekha) have gone over "
                        "me' (42:7). The tehom is the primordial deep of Genesis 1:2; the breakers "
                        "and waves are YHWH's instruments of overwhelming affliction. Yet the "
                        "psalmist holds to the covenant: 'By day YHWH commands his steadfast love "
                        "(chesed), and at night his song is with me, a prayer to the God of my "
                        "life (El chayyai)' (42:8). Psalm 43 petitions for deliverance: 'Send out "
                        "your light (or) and your truth (emet); let them lead me; let them bring "
                        "me to your holy hill (har qodshekha) and to your dwelling (mishkenotekha)' "
                        "(43:3). Light and truth are personified as divine guides -- angelic agents "
                        "who escort the worshipper back to the holy mountain. The final refrain "
                        "resolves: 'Hope in God; for I shall again praise him, my salvation and "
                        "my God' (43:5). The psalm does not end with deliverance accomplished but "
                        "with faith projected forward."
            }
        ]
    },

    {
        "id": "ps-45",
        "ref": "Psalm 45",
        "chapter_num": 2,
        "title": "The Royal Wedding -- The King Addressed as Elohim",
        "era": "psalms_book2",
        "type": "chapter",
        "themes": ["KING", "SEED", "LOVE", "WOMEN"],

        "synopsis": "Psalm 45 is the most extraordinary royal psalm in the Psalter -- a wedding "
                    "hymn for the Davidic king that addresses him directly as elohim. 'Your throne, "
                    "O God (elohim), is forever and ever. The scepter of your kingdom is a scepter "
                    "of uprightness' (45:6). The king is described in terms that blur the boundary "
                    "between the human and the divine: he is 'fairer than the children of men' "
                    "(45:2), rides forth 'in the cause of truth and meekness and righteousness' "
                    "(45:4), and has been anointed by God 'with the oil of gladness beyond your "
                    "companions (chavereiha)' (45:7). The queen stands at his right hand in gold "
                    "of Ophir. The nations bring tribute. The psalm is a celebration of the "
                    "Davidic covenant in its most exalted form -- the human king participating "
                    "in divine attributes.",

        "key_verse": {
            "ref": "Psalm 45:6-7",
            "text": "Your throne, O God, is forever and ever. The scepter of your kingdom is a scepter of uprightness; you have loved righteousness and hated wickedness. Therefore God, your God, has anointed you with the oil of gladness beyond your companions.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "elohim (God/gods -- the king is addressed with this title in 45:6; the interpretation is debated)",
            "shir yedidot (a love song -- the superscription; a wedding hymn for the king)",
            "hod (splendor/majesty -- the royal garment imagery of the king)",
            "shemen sason (oil of gladness -- the anointing oil of joy; the consecration of the king)",
            "chaverim (companions -- the king's peers; he is anointed above them)",
            "mishgal (queen -- from shegal, the royal consort; the queen stands at his right hand)",
            "shoshannim (lilies -- in the superscription; possibly a melody name)"
        ],

        "ane_backdrop": "Royal wedding hymns are attested throughout the ANE. The Song of Solomon and "
                        "Egyptian love poetry share imagery of royal beauty and fragrant garments. The "
                        "address to the king as elohim in 45:6 has a profound parallel in Canaanite "
                        "literature: the Ugaritic texts describe the human king as participating in "
                        "the divine realm through his installation by El, the head of the pantheon. "
                        "In Egypt, the pharaoh was addressed as 'god' (ntr) and considered a divine "
                        "being incarnate. The Israelite theology is more nuanced: the Davidic king "
                        "is not God by nature but by divine decree and adoption (Ps 2:7). The address "
                        "as elohim in 45:6 reflects this unique status -- the human king participates "
                        "in the divine council's authority as YHWH's designated regent.",

        "second_temple": [
            {
                "source": "Hebrews 1:8-9",
                "summary": "The author of Hebrews quotes Psalm 45:6-7 as God the Father speaking "
                           "to the Son: 'But of the Son he says, Your throne, O God, is forever "
                           "and ever.' This is used to demonstrate the Son's superiority over angels.",
                "relevance": "Hebrews treats the elohim address in Psalm 45 as a literal divine title "
                             "applied to the messianic Son -- the king is truly divine, not merely "
                             "an exalted human."
            },
            {
                "source": "Targum on Psalm 45:3",
                "summary": "The Targum renders the psalm as addressed to the 'King Messiah,' "
                           "explicitly identifying the royal bridegroom as the coming deliverer.",
                "relevance": "The Targumic tradition confirms that Psalm 45 was read messianically in "
                             "Jewish interpretation, not merely as a historical wedding song."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 1:8-9", "note": "'Your throne, O God, is forever and ever' -- quoted as proof of the Son's deity, superior to angels", "type": "nt"},
            {"ref": "2 Samuel 7:13, 16", "note": "'I will establish the throne of his kingdom forever' -- the Davidic covenant behind the 'forever' throne of 45:6", "type": "ot"},
            {"ref": "Isaiah 9:6-7", "note": "'Mighty God, Everlasting Father, Prince of Peace... on the throne of David' -- the same blurring of human and divine categories", "type": "ot"},
            {"ref": "Revelation 19:7-9", "note": "'The marriage of the Lamb has come, and his Bride has made herself ready' -- the eschatological wedding Ps 45 prefigures", "type": "nt"},
            {"ref": "Song of Solomon 3:6-11", "note": "Solomon's wedding procession -- the closest literary parallel to the royal wedding of Ps 45", "type": "ot"},
            {"ref": "Psalm 2:7", "note": "'You are my Son; today I have begotten you' -- the divine sonship decree that underlies the elohim address in 45:6", "type": "ot"}
        ],

        "divine_council_note": "Psalm 45:6 is one of the most theologically explosive verses in the "
                               "Old Testament: 'Your throne, O God (elohim), is forever and ever.' A "
                               "human king is addressed with the title elohim -- the same word used for "
                               "YHWH, for the gods of the nations, and for the members of the divine "
                               "council. How is this possible? In the divine council framework, the "
                               "Davidic king occupies a unique position: he is YHWH's regent on earth, "
                               "adopted as 'son' (Ps 2:7), seated at YHWH's right hand (Ps 110:1), and "
                               "granted authority over the nations. The word elohim in 45:6 may function "
                               "as a title of office rather than a statement of ontological identity -- "
                               "the king is elohim in the sense that he represents the divine presence "
                               "on earth and exercises divine authority. Verse 7 clarifies the hierarchy: "
                               "'Therefore God (elohim), your God (elohekha), has anointed you' -- there "
                               "is an elohim above the king-elohim. The king is divine by decree, not "
                               "by nature. Yet the author of Hebrews reads 45:6 as spoken by the Father "
                               "to the Son and uses it to prove the Son's superiority over angels (Heb "
                               "1:8-9). In the NT reading, the messianic king is not merely an adopted "
                               "elohim but the unique Son who is 'the radiance of the glory of God and "
                               "the exact imprint of his nature' (Heb 1:3). The 'companions' "
                               "(chaverim) of 45:7 above whom the king is anointed may be the other "
                               "elohim of the council -- the king surpasses them all.",

        "sections": [
            {
                "heading": "Understanding the Superscription: Musical Directions in the Psalms",
                "body": "Psalm 45's superscription reads: 'To the choirmaster: according to "
                        "<em>Shoshannim</em>. A Maskil of the Sons of Korah. A Love Song.' This "
                        "packed heading contains several terms that readers should understand:"
                        "<br><br>"
                        "<strong>Shoshannim</strong> (literally 'lilies'): This is one of several "
                        "musical direction terms in the Psalter that likely refer to a specific "
                        "melody or tune to which the psalm was sung. Other examples include "
                        "<em>alamot</em> ('maidens,' Ps 46 -- possibly a high-pitched vocal "
                        "register), <em>sheminit</em> ('the eighth,' Ps 6, 12 -- possibly a "
                        "lower octave or an eight-stringed instrument), <em>gittit</em> (Pss 8, "
                        "81, 84 -- possibly a tune associated with Gath or a winepress song), "
                        "and <em>mahalat</em> (Ps 53, 88 -- possibly 'sickness' or a dirge-like "
                        "tune). These terms are largely opaque to modern readers because the "
                        "melodies themselves have been lost. They are fossils of a living musical "
                        "tradition -- evidence that the Psalms were not merely poems but songs "
                        "with specific musical settings.<br><br>"
                        "<strong>Shir Yedidot</strong> ('A Love Song'): This unique "
                        "superscription marks Psalm 45 as the only psalm explicitly identified "
                        "as a love song -- a royal wedding hymn. The word <em>yedidot</em> "
                        "comes from <em>yadid</em>, 'beloved,' the same root as the name "
                        "Jedidiah ('beloved of YHWH'), which was the name YHWH gave to Solomon "
                        "through Nathan the prophet (2 Samuel 12:25)."
            },
            {
                "heading": "The King's Beauty and Valor (45:1-5)",
                "body": "The poet's heart 'overflows with a pleasing theme' (45:1) -- this is a "
                        "song of celebration, not lament. The king is 'fairer than the children of "
                        "men; grace is poured upon your lips' (45:2). The beauty is not merely "
                        "physical but charismatic -- the king embodies divine grace (chen). He "
                        "girds his sword on his thigh in 'splendor and majesty' (hod vehadar, "
                        "45:3) -- the same paired terms used for YHWH's own appearance (Ps 96:6; "
                        "104:1). The king rides forth 'in the cause of truth (emet) and meekness "
                        "(anvah) and righteousness (tsedeq)' (45:4). These are not merely royal "
                        "virtues but divine attributes -- the qualities by which YHWH himself "
                        "governs. The king's arrows are 'sharp in the heart of the king's "
                        "enemies; the peoples fall under you' (45:5). The warrior-king subdues "
                        "the nations -- echoing the grant of Psalm 2:8-9."
            },
            {
                "heading": "The Divine Throne and the Anointing (45:6-9)",
                "body": "'Your throne, O God (elohim), is forever and ever. The scepter of your "
                        "kingdom is a scepter of uprightness (mishor)' (45:6). The word mishor "
                        "means 'equity, straightness, justice' -- the king's rule is characterized "
                        "by righteous judgment. 'You have loved righteousness and hated wickedness. "
                        "Therefore God (elohim), your God (elohekha), has anointed you with the "
                        "oil of gladness (shemen sason) beyond your companions (chaverekha)' "
                        "(45:7). The double elohim is the crux of the passage: the first elohim "
                        "addresses the king; the second is the God who anoints him. The anointing "
                        "'beyond companions' sets the king apart from all peers -- whether human "
                        "princes or divine council members. The king's robes are fragrant with "
                        "'myrrh and aloes and cassia' (45:8) -- the spices of the anointing oil "
                        "(Exod 30:23-25) and of the bridal chamber (Song 4:14). Ivory palaces "
                        "provide the setting -- archaeological evidence of ivory-inlaid furniture "
                        "has been found at Samaria and Nimrud. 'Daughters of kings are among your "
                        "honored women; at your right hand stands the queen (shegal) in gold of "
                        "Ophir' (45:9)."
            },
            {
                "heading": "The Bride and the Eternal Dynasty (45:10-17)",
                "body": "The bride is counseled: 'Hear, O daughter, and consider, and incline your "
                        "ear: forget your people and your father's house, and the king will desire "
                        "your beauty' (45:10-11). She must leave her former identity and become "
                        "fully part of the royal household. 'Since he is your lord (adon), bow to "
                        "him' (45:11b). The people of Tyre bring gifts; 'the richest of the "
                        "people' seek favor (45:12). The bride is 'all glorious within' (penimah), "
                        "her clothing 'interwoven with gold' (45:13). She is led to the king 'with "
                        "her virgin companions' in a joyful procession (45:14-15). The psalm closes "
                        "with a dynastic promise: 'In place of your fathers shall be your sons; "
                        "you will make them princes in all the earth' (45:16). The royal line will "
                        "not merely continue but expand -- the king's sons will rule all the earth. "
                        "'I will cause your name to be remembered in all generations; therefore "
                        "nations will praise you forever and ever' (45:17). The scope is universal "
                        "and eternal -- this is not merely a Judean king but a ruler whose name "
                        "fills the earth. The prophetic trajectory points beyond any historical "
                        "king to the messianic fulfillment."
            }
        ]
    },

    {
        "id": "ps-46-48",
        "ref": "Psalms 46, 48",
        "chapter_num": 3,
        "title": "Zion as Cosmic Mountain -- God Is Our Refuge",
        "era": "psalms_book2",
        "type": "chapter",
        "themes": ["KING", "DC", "LAND", "HOLY"],

        "synopsis": "Psalms 46 and 48 are Korahite 'Songs of Zion' that present Jerusalem/Zion not "
                    "merely as a political capital but as the cosmic mountain -- the junction of "
                    "heaven and earth, the seat of YHWH's earthly throne. Psalm 46 declares 'God "
                    "is our refuge and strength, a very present help in trouble' (46:1) and "
                    "describes cosmic upheaval -- mountains falling into the sea, waters roaring "
                    "and foaming -- all rendered irrelevant by God's presence in the city. 'There "
                    "is a river whose streams make glad the city of God (ir Elohim), the holy "
                    "habitation of the Most High (mishkenei Elyon)' (46:4). Psalm 48 celebrates "
                    "Zion as 'beautiful in elevation, the joy of all the earth... the city of the "
                    "great King' (48:2), identifying it with 'the far north' (tsaphon) -- the "
                    "Canaanite name for the mountain of the gods. This is deliberate polemic: "
                    "YHWH's mountain is not Baal's Zaphon but Zion.",

        "key_verse": {
            "ref": "Psalm 46:4-5",
            "text": "There is a river whose streams make glad the city of God, the holy habitation of the Most High. God is in the midst of her; she shall not be moved; God will help her when morning dawns.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "machseh (refuge -- a place of shelter from cosmic and military threat)",
            "Elyon (Most High -- YHWH's supreme title as head of the divine council)",
            "ir Elohim (city of God -- Jerusalem/Zion as YHWH's earthly dwelling place)",
            "tsaphon (the north/Zaphon -- the Canaanite mountain of the gods; applied to Zion in 48:2)",
            "melek gadol (great King -- YHWH as the cosmic sovereign whose capital is Zion)",
            "nahar (river -- the life-giving stream of the divine city; cf. Ezek 47; Rev 22)",
            "selah (liturgical notation -- occurs three times in Ps 46)"
        ],

        "ane_backdrop": "The concept of the cosmic mountain is universal in ANE religion. In Ugaritic "
                        "texts, Mount Zaphon (tsapanu) is the abode of Baal, the mountain where the "
                        "divine assembly meets and where Baal's palace stands (KTU 1.3.I). In "
                        "Mesopotamia, the cosmic mountain is the place where heaven meets earth -- "
                        "the ziggurat was a man-made cosmic mountain designed to link the human and "
                        "divine realms. In Egyptian theology, the primeval mound (benben) that first "
                        "emerged from the waters of chaos was the original cosmic mountain. Psalm "
                        "48:2 deliberately appropriates the Canaanite Zaphon tradition by calling "
                        "Zion 'the heights of Zaphon' (yarkete tsaphon). The polemic is clear: the "
                        "true cosmic mountain is not Baal's Zaphon but YHWH's Zion. The river of "
                        "Psalm 46:4 has no geographical counterpart in Jerusalem (which has only the "
                        "spring of Gihon) and is best understood as the cosmic river that flows from "
                        "the throne of God (cf. Gen 2:10; Ezek 47:1-12; Rev 22:1-2).",

        "second_temple": [
            {
                "source": "Ezekiel 47:1-12",
                "summary": "Ezekiel sees a river flowing from the threshold of the eschatological "
                           "temple, deepening as it flows, bringing life wherever it goes.",
                "relevance": "The river of Psalm 46:4 finds its prophetic elaboration in Ezekiel's "
                             "temple vision -- the cosmic river of the city of God."
            },
            {
                "source": "Revelation 22:1-2",
                "summary": "John sees 'the river of the water of life, bright as crystal, flowing "
                           "from the throne of God and of the Lamb.'",
                "relevance": "The eschatological fulfillment of Psalm 46's river: in the new Jerusalem, "
                             "the cosmic river flows openly from the divine throne."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 2:10", "note": "'A river flowed out of Eden to water the garden' -- the primordial river of the divine garden, echoed in Ps 46:4", "type": "ot"},
            {"ref": "Ezekiel 47:1-12", "note": "The eschatological river from the temple -- the prophetic development of Ps 46's cosmic river", "type": "ot"},
            {"ref": "Isaiah 2:2-3", "note": "'The mountain of the house of YHWH shall be established as the highest of the mountains' -- Zion as the supreme cosmic mountain", "type": "ot"},
            {"ref": "Revelation 21:2-3", "note": "The new Jerusalem coming down from God -- the ultimate city of God", "type": "nt"},
            {"ref": "Psalm 87:1-3", "note": "'On the holy mount stands the city he founded... Glorious things of you are spoken, O city of God'", "type": "ot"},
            {"ref": "Isaiah 14:13", "note": "The king of Babylon's boast: 'I will sit on the mount of assembly in the far reaches of the north (tsaphon)' -- competing with YHWH's Zion", "type": "ot"}
        ],

        "divine_council_note": "The Zion theology of Psalms 46 and 48 is divine council theology "
                               "expressed geographically. Zion is not merely a hill in Judah but the "
                               "earthly counterpart of YHWH's heavenly throne room. The title 'Most "
                               "High' (Elyon) in 46:4 is YHWH's supreme divine council designation -- "
                               "the same title used in Deuteronomy 32:8 ('When the Most High gave to "
                               "the nations their inheritance') and Psalm 82:6 ('sons of the Most "
                               "High'). The 'holy habitation' (mishkenei, literally 'tabernacles' or "
                               "'dwelling places') of the Most High is the cosmic sanctuary where "
                               "heaven touches earth. Psalm 48:2 identifies Zion with 'the heights of "
                               "Zaphon' (yarkete tsaphon) -- a direct appropriation of the Canaanite "
                               "divine mountain. In Ugaritic mythology, Zaphon is where the gods "
                               "assemble and where Baal holds court. By calling Zion 'Zaphon,' the "
                               "psalmist declares that YHWH has replaced Baal as the true lord of the "
                               "cosmic mountain. The 'great King' (melek gadol) of 48:2 is a divine "
                               "council title for YHWH as supreme sovereign. The nations that assembled "
                               "against Zion are routed (48:4-7) -- their kings 'saw and were astounded; "
                               "they were in panic; they took to flight.' The cosmic mountain is "
                               "impregnable because the God who sits enthroned there commands the "
                               "heavenly hosts. Psalm 46:10 issues the definitive divine council "
                               "declaration: 'Be still, and know that I am God (Elohim). I will be "
                               "exalted among the nations, I will be exalted in the earth!' -- the "
                               "Most High asserting his supremacy over all earthly and heavenly powers.",

        "sections": [
            {
                "heading": "Why Does Book II Say 'God' Instead of 'LORD'? The Elohistic Psalter",
                "body": "Readers who are attentive to the biblical text will notice a shift "
                        "beginning in Book II: where Book I overwhelmingly uses the name "
                        "<strong>YHWH</strong> (rendered as 'the LORD' in most English translations), "
                        "Books II and III (Psalms 42-83) predominantly use the word "
                        "<strong>Elohim</strong> (rendered simply as 'God'). Scholars call this "
                        "section the <strong>Elohistic Psalter</strong>.<br><br>"
                        "The reason for this shift is debated. The most common explanation is that "
                        "an editor (or school of editors) systematically replaced the personal "
                        "covenant name YHWH with the more universal term Elohim throughout this "
                        "section. This may reflect a theological preference: Elohim emphasizes "
                        "God's universal sovereignty over all creation and all nations, while YHWH "
                        "emphasizes the personal covenant relationship with Israel. Since Book II "
                        "introduces the Korahite psalms with their emphasis on Zion as the cosmic "
                        "mountain and YHWH's supremacy over all the earth, the use of the universal "
                        "name Elohim fits the theological scope.<br><br>"
                        "Evidence for editorial substitution: when parallel versions of the same "
                        "psalm exist (e.g., Psalm 14 = Psalm 53, Psalm 40:13-17 = Psalm 70), the "
                        "version inside the Elohistic Psalter uses 'Elohim' where the version "
                        "outside it uses 'YHWH.' This does not change the meaning -- both names "
                        "refer to the same God of Israel -- but it explains why you will hear "
                        "'God' more often than 'the LORD' in Psalms 42-83."
            },
            {
                "heading": "Selah in Psalm 46",
                "body": "Psalm 46 contains three occurrences of <strong>Selah</strong> (46:3, 7, "
                        "11), which divide the psalm into three sections. This is a particularly "
                        "instructive use of Selah because each occurrence follows a dramatic "
                        "theological statement:<br><br>"
                        "After 46:3 (the waters roaring and mountains trembling) -- Selah: pause "
                        "and absorb the cosmic upheaval before hearing of God's river of peace.<br>"
                        "After 46:7 ('YHWH of hosts is with us; the God of Jacob is our fortress') "
                        "-- Selah: pause and let this declaration of divine protection settle.<br>"
                        "After 46:11 (the same refrain repeated) -- Selah: the final pause, an "
                        "invitation to carry this truth beyond the psalm.<br><br>"
                        "The Selah markers in Psalm 46 function like breathing spaces in music -- "
                        "they allow the weight of each section to be felt before the next begins. "
                        "The word likely derives from <em>salal</em> ('to lift up') and may have "
                        "signaled the instruments to play an interlude while the singers paused."
            },
            {
                "heading": "Psalm 46: God is Our Refuge (46:1-7)",
                "body": "'God (Elohim) is our refuge (machseh) and strength, a very present help "
                        "(nimtsa me'od) in trouble' (46:1). The opening declaration establishes "
                        "absolute confidence. The scenario that follows is cosmic collapse: "
                        "'Therefore we will not fear though the earth gives way, though the "
                        "mountains be moved into the heart of the sea, though its waters roar "
                        "and foam, though the mountains tremble at its swelling' (46:2-3). This "
                        "is de-creation language -- the reversal of Genesis 1, where God separated "
                        "land from sea. Even if creation itself unravels, the worshippers of YHWH "
                        "have nothing to fear. Against this cosmic chaos, the contrast is serene: "
                        "'There is a river whose streams make glad the city of God, the holy "
                        "habitation of the Most High' (46:4). The river is the counter-image to "
                        "the chaotic sea: where the sea roars and threatens, the river gladdens "
                        "and nourishes. 'God is in the midst of her; she shall not be moved. God "
                        "will help her when morning dawns' (46:5). The divine presence within the "
                        "city guarantees its stability. The morning is the time of deliverance -- "
                        "when the night of crisis gives way to YHWH's intervention (cf. Exod 14:27). "
                        "'The nations rage (hamu), the kingdoms totter (motu); he utters his voice, "
                        "the earth melts (tamug)' (46:6). One word from YHWH dissolves the "
                        "opposition of the nations."
            },
            {
                "heading": "Psalm 46:8-11 and Psalm 48: Zion, the Joy of All the Earth",
                "body": "'Come, behold the works of YHWH, how he has brought desolations on the "
                        "earth. He makes wars cease to the end of the earth; he breaks the bow "
                        "and shatters the spear; he burns the chariots with fire' (46:8-9). YHWH "
                        "does not merely win wars; he abolishes war. The divine warrior's final "
                        "victory is not conquest but peace (shalom). 'Be still (harpu), and know "
                        "that I am God. I will be exalted among the nations, I will be exalted "
                        "in the earth!' (46:10). The verb harpu means 'let go, cease, desist' -- "
                        "a command to all powers, human and spiritual, to cease their striving "
                        "and acknowledge YHWH's sovereignty. Psalm 48 develops the Zion theology "
                        "further: 'Great is YHWH and greatly to be praised in the city of our "
                        "God! His holy mountain, beautiful in elevation, is the joy of all the "
                        "earth, Mount Zion, the heights of Zaphon (yarkete tsaphon), the city of "
                        "the great King' (48:1-2). The identification of Zion with Zaphon "
                        "transfers every attribute of the Canaanite divine mountain to YHWH's "
                        "city. The kings who assembled against Zion 'saw it and were astounded; "
                        "they were in panic; they took to flight. Trembling took hold of them "
                        "there, anguish as of a woman in labor' (48:5-6). The cosmic mountain "
                        "is inviolable because the great King dwells there."
            }
        ]
    },

    {
        "id": "ps-68",
        "ref": "Psalm 68",
        "chapter_num": 4,
        "title": "The Divine Warrior March -- Thousands of Chariots",
        "era": "psalms_book2",
        "type": "chapter",
        "themes": ["DC", "GLORY", "KING", "NATIONS"],

        "synopsis": "Psalm 68 is the most complex and dramatic divine warrior hymn in the Psalter. "
                    "It traces YHWH's march from Sinai through the wilderness to Zion, scattering "
                    "enemies, providing for the poor, and ascending to his mountain throne with "
                    "'thousands upon thousands of chariots' (68:17). The psalm opens with the ark "
                    "procession formula of Numbers 10:35: 'God shall arise, his enemies shall be "
                    "scattered' (68:1). YHWH is called 'the rider of the clouds' (rokhev "
                    "ba'aravot, 68:4) -- the exact title of Baal in the Ugaritic texts (rkb 'rpt). "
                    "He is 'a father of the fatherless and protector of widows' (68:5). Kings and "
                    "their armies flee; women divide the spoil. The climax is the procession to "
                    "Zion: 'The chariots of God are twice ten thousand, thousands upon thousands; "
                    "the Lord is among them; Sinai is now in the sanctuary' (68:17). YHWH has "
                    "ascended on high, leading a host of captives (68:18 -- quoted in Eph 4:8).",

        "key_verse": {
            "ref": "Psalm 68:17-18",
            "text": "The chariots of God are twice ten thousand, thousands upon thousands; the Lord is among them; Sinai is now in the sanctuary. You ascended on high, leading a host of captives in your train and receiving gifts among men, even among the rebellious, that the LORD God may dwell there.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "rokhev ba'aravot (rider of the clouds/deserts -- the Baal epithet claimed by YHWH)",
            "rekhev Elohim (chariots of God -- the angelic war chariot army; twenty thousand strong)",
            "ribotayim (twice ten thousand -- the overwhelming number of YHWH's chariots)",
            "shavah shevi (you led captives captive -- the divine warrior's triumphal procession)",
            "mattanot ba'adam (gifts among men -- tribute received by the ascending conqueror)",
            "Yah (the shortened form of YHWH -- appears multiple times in Ps 68)",
            "avi yetomim (father of the fatherless -- YHWH's social justice identity)"
        ],

        "ane_backdrop": "Psalm 68 is saturated with Canaanite divine warrior imagery. The title "
                        "'rider of the clouds' (rokhev ba'aravot, 68:4) directly parallels Baal's "
                        "title rkb 'rpt ('rider of the clouds') in the Ugaritic texts (KTU 1.2.IV.8; "
                        "1.3.II.40; 1.4.III.11). The divine warrior marching from Sinai through the "
                        "wilderness parallels the ANE divine march traditions where the deity leaves "
                        "his sacred mountain to fight on behalf of his people. The 'thousands of "
                        "chariots' (68:17) reflect the heavenly army -- the angelic host that "
                        "accompanies YHWH into battle. Mesopotamian royal inscriptions describe the "
                        "gods' chariots accompanying the king; the Hittite texts describe the storm "
                        "god's chariot army. The triumphal ascension with captives (68:18) parallels "
                        "the ANE victory procession where the conquering king ascends to his temple "
                        "with prisoners and spoil.",

        "second_temple": [
            {
                "source": "Ephesians 4:8-10",
                "summary": "Paul quotes Psalm 68:18 and applies it to Christ's ascension: 'When he "
                           "ascended on high he led a host of captives, and he gave gifts to men.' "
                           "Paul changes 'received' to 'gave,' following a tradition also found in "
                           "the Targum.",
                "relevance": "The apostolic interpretation identifies the divine warrior of Psalm 68 "
                             "with the ascended Christ who distributes spiritual gifts to the church."
            },
            {
                "source": "Targum on Psalm 68:18",
                "summary": "The Targum renders the verse: 'You ascended to the firmament, O prophet "
                           "Moses; you took captivity captive; you learned the words of Torah; you "
                           "gave them as gifts to the sons of men.'",
                "relevance": "The Targumic tradition interprets the ascension as Moses' ascent of Sinai "
                             "to receive Torah -- connecting the divine warrior march to Torah revelation."
            }
        ],

        "cross_refs": [
            {"ref": "Numbers 10:35", "note": "'Arise, O YHWH, and let your enemies be scattered' -- the ark procession formula that Ps 68:1 quotes", "type": "ot"},
            {"ref": "Ephesians 4:8-10", "note": "Paul quotes Ps 68:18 as Christ's ascension: 'he ascended on high, he led a host of captives'", "type": "nt"},
            {"ref": "Deuteronomy 33:2", "note": "'YHWH came from Sinai... he came from the ten thousands of holy ones' -- the divine march with angelic army", "type": "ot"},
            {"ref": "Judges 5:4-5", "note": "'YHWH, when you went out from Seir... the earth trembled, the heavens poured' -- Deborah's divine march song paralleling Ps 68", "type": "ot"},
            {"ref": "Habakkuk 3:3-15", "note": "The divine warrior march from Teman/Paran -- the same Sinai-to-conquest trajectory as Ps 68", "type": "ot"},
            {"ref": "2 Kings 6:17", "note": "'Horses and chariots of fire all around Elisha' -- the visible manifestation of the rekhev Elohim", "type": "ot"},
            {"ref": "Psalm 18:9-14", "note": "YHWH's storm theophany descent -- riding on a cherub, flying on the wings of the wind", "type": "ot"}
        ],

        "divine_council_note": "Psalm 68 is the supreme divine warrior hymn in the Psalter, and its "
                               "divine council content is dense. (1) The 'rider of the clouds' title "
                               "(68:4) transfers Baal's supreme attribute to YHWH -- the Most High, not "
                               "the storm god, rides the heavens. (2) The march from Sinai (68:7-8) "
                               "depicts YHWH leading his heavenly army through physical territory, "
                               "causing the earth to quake and the heavens to rain. (3) The 'chariots "
                               "of God are twice ten thousand, thousands upon thousands' (68:17) is the "
                               "heavenly army in full deployment -- the angelic host that accompanies "
                               "YHWH from Sinai to Zion. The phrase 'the Lord is among them; Sinai is "
                               "now in the sanctuary' declares that the Sinai theophany has been "
                               "permanently relocated to Zion. The God who descended on Sinai in fire "
                               "and thunder now dwells on Zion. (4) The ascension with captives (68:18) "
                               "is the divine warrior's triumphal return to his throne after conquest -- "
                               "the same pattern as Marduk's ascension after defeating Tiamat in the "
                               "Enuma Elish, or Baal's enthronement after defeating Yam. But YHWH's "
                               "ascension surpasses all: he receives gifts 'even among the rebellious' "
                               "(sorerim) -- a term that may include the rebellious elohim who opposed "
                               "his rule. (5) Verse 35 is the theological climax: 'Awesome is God from "
                               "his sanctuary; the God of Israel -- he is the one who gives power and "
                               "strength to his people. Blessed be God!' The power flows from the "
                               "heavenly sanctuary through the divine council to YHWH's people on earth.",

        "sections": [
            {
                "heading": "The Divine Warrior Arises (68:1-10)",
                "body": "'God shall arise (yaqum Elohim), his enemies shall be scattered; and "
                        "those who hate him shall flee before him!' (68:1). This echoes the ark "
                        "procession formula of Numbers 10:35, connecting the psalm to the "
                        "wilderness march when the ark led Israel into battle. 'As smoke is "
                        "driven away, so you shall drive them away; as wax melts before fire, "
                        "so the wicked shall perish before God' (68:2). The imagery is theophanic: "
                        "God's presence dissolves opposition as fire melts wax. YHWH is then "
                        "described in his most tender role: 'Father of the fatherless and "
                        "protector of widows is God in his holy habitation' (68:5). The divine "
                        "warrior fights for the vulnerable. 'God leads out the prisoners to "
                        "prosperity, but the rebellious dwell in a parched land' (68:6). The "
                        "march from Sinai begins: 'O God, when you went out before your people, "
                        "when you marched through the wilderness -- the earth quaked, the heavens "
                        "poured down rain before God, the One of Sinai, before God, the God of "
                        "Israel' (68:7-8). The title 'the One of Sinai' (zeh Sinai) identifies "
                        "YHWH inseparably with the mountain of revelation."
            },
            {
                "heading": "The Ascension and the Angelic Army (68:11-18)",
                "body": "'The Lord gives the word; the women who announce the news are a great "
                        "host' (68:11). The victory proclamation is broadcast by women -- as "
                        "Miriam led the song at the Sea (Exod 15:20-21). 'Kings of armies -- "
                        "they flee, they flee! The women at home divide the spoil' (68:12). "
                        "YHWH's question addresses those who remained behind: 'Though you men "
                        "lie among the sheepfolds, the wings of a dove are covered with silver, "
                        "its pinions with shimmering gold' (68:13) -- beauty emerges from the "
                        "ashes of battle. The divine warrior chooses his mountain: 'Why do you "
                        "look with hatred, O many-peaked mountain, at the mount that God desired "
                        "for his abode, yes, where YHWH will dwell forever?' (68:16). The other "
                        "mountains -- including Bashan, associated with the Rephaim (Deut 3:11, "
                        "13) -- are jealous of Zion. Then the climax: 'The chariots (rekhev) of "
                        "God are twice ten thousand, thousands upon thousands (alphei shin'an); "
                        "the Lord is among them; Sinai is now in the sanctuary' (68:17). Twenty "
                        "thousand angelic chariots -- the heavenly army in full array. 'You "
                        "ascended on high (marom), leading a host of captives (shavita shevi), "
                        "you received gifts among men (mattanot ba'adam), even among the "
                        "rebellious (sorerim)' (68:18). The divine warrior ascends to his throne "
                        "with prisoners of war and tribute."
            }
        ]
    },

    {
        "id": "ps-72",
        "ref": "Psalm 72",
        "chapter_num": 5,
        "title": "The Solomonic Ideal King -- Messianic Reign to the Ends of the Earth",
        "era": "psalms_book2",
        "type": "chapter",
        "themes": ["KING", "SEED", "NATIONS", "PROV"],

        "synopsis": "Psalm 72 closes Book II with a vision of the ideal king that transcends any "
                    "historical monarch. Attributed to Solomon (or 'for Solomon'), it describes a "
                    "king who 'judges your people with righteousness, and your poor with justice' "
                    "(72:2), whose reign extends 'from sea to sea, and from the River to the ends "
                    "of the earth' (72:8). Kings bow before him, nations serve him, and the needy "
                    "find deliverance. The psalm reaches cosmic proportions: 'May his name endure "
                    "forever, his fame continue as long as the sun! May people be blessed in him, "
                    "all nations call him blessed!' (72:17) -- echoing the Abrahamic blessing "
                    "('in you all the families of the earth shall be blessed,' Gen 12:3). The "
                    "colophon 'The prayers of David, the son of Jesse, are ended' (72:20) marks "
                    "the structural close of the Davidic core of the Psalter.",

        "key_verse": {
            "ref": "Psalm 72:8, 17",
            "text": "May he have dominion from sea to sea, and from the River to the ends of the earth! ... May his name endure forever, his fame continue as long as the sun! May people be blessed in him, all nations call him blessed!",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "lishlomoh (of Solomon/for Solomon -- the Solomonic attribution or dedication)",
            "tsedeq (righteousness -- the defining quality of the ideal king's rule)",
            "mishpat (justice -- the equitable judgment the king renders for the poor)",
            "yam ad-yam (from sea to sea -- the universal extent of the messianic kingdom)",
            "nahar (the River -- the Euphrates; the eastern boundary of the promised land)",
            "shemo (his name -- the name that endures forever; the eternal reputation of the king)",
            "yitbaraku-vo (be blessed in him -- the Abrahamic blessing channeled through the king)"
        ],

        "ane_backdrop": "Psalm 72 follows the genre of ANE royal idealization. Mesopotamian royal "
                        "hymns describe the ideal king as the guarantor of cosmic justice: the "
                        "Code of Hammurabi's prologue presents the king as the one who 'makes "
                        "justice prevail in the land' and 'destroys the wicked and evil.' Egyptian "
                        "instructions for the prince describe the ideal pharaoh as the one who "
                        "protects the weak and judges with equity. The universal dominion 'from sea "
                        "to sea' echoes the Akkadian formula 'king of the four quarters' (shar "
                        "kibrat arba'im) -- the claim to universal sovereignty. The tribute of "
                        "Tarshish and Sheba (72:10) reflects the international trade networks of "
                        "Solomon's era but also the eschatological expectation that all nations will "
                        "bring their wealth to YHWH's king (cf. Isa 60:6-9).",

        "second_temple": [
            {
                "source": "Psalms of Solomon 17:21-46",
                "summary": "A 1st century BC text describing the Davidic Messiah who will purge "
                           "Jerusalem, rule with righteousness, and bring the nations under his "
                           "authority -- heavily dependent on Psalm 72's imagery.",
                "relevance": "Demonstrates that Psalm 72 was a primary source for Second Temple "
                             "messianic expectation."
            },
            {
                "source": "Matthew 2:1-12",
                "summary": "The Magi from the East bring gifts to the newborn king -- gold, "
                           "frankincense, and myrrh. This has been connected to Psalm 72:10-11 "
                           "('kings of Sheba and Seba bring gifts').",
                "relevance": "The Matthean nativity narrative enacts the tribute scene of Psalm 72: "
                             "foreign kings bringing gifts to YHWH's anointed."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 12:3", "note": "'In you all the families of the earth shall be blessed' -- the Abrahamic promise that Ps 72:17 echoes", "type": "ot"},
            {"ref": "1 Kings 4:21, 24-25", "note": "Solomon's historical reign 'from the Euphrates to the border of Egypt' -- the partial fulfillment of 72:8", "type": "ot"},
            {"ref": "Isaiah 11:1-9", "note": "The Branch of Jesse who judges the poor with righteousness -- the prophetic parallel to Ps 72's ideal king", "type": "ot"},
            {"ref": "Isaiah 60:6-9", "note": "Nations bringing gold and frankincense to Zion -- the eschatological tribute of Ps 72:10-11", "type": "ot"},
            {"ref": "Zechariah 9:10", "note": "'His rule shall be from sea to sea, and from the River to the ends of the earth' -- quoting Ps 72:8", "type": "ot"},
            {"ref": "Revelation 11:15", "note": "'The kingdom of the world has become the kingdom of our Lord and of his Christ, and he shall reign forever' -- the fulfillment of Ps 72", "type": "nt"}
        ],

        "divine_council_note": "Psalm 72 describes the messianic king's universal reign in terms that "
                               "reverse the Deuteronomy 32 disinheritance. Where the Most High allotted "
                               "the nations to the sons of God (Deut 32:8), keeping only Israel as his "
                               "own inheritance, Psalm 72 envisions a Davidic king who reclaims all "
                               "nations: 'May he have dominion from sea to sea, and from the River to "
                               "the ends of the earth' (72:8). The 'kings of Tarshish and of the "
                               "coastlands' -- the farthest known territories -- bring tribute (72:10). "
                               "'All kings fall down before him; all nations serve him' (72:11). This is "
                               "the reversal of Babel: the nations that were scattered and allotted to "
                               "lesser elohim are now gathered under the rule of YHWH's chosen king. "
                               "The Abrahamic echo in 72:17 ('may people be blessed in him, all nations "
                               "call him blessed') connects this universal reign to the original "
                               "promise: through Abraham's seed, the blessing that was lost at Eden "
                               "and fractured at Babel will be restored to all humanity. The closing "
                               "doxology of Book II confirms the cosmic scope: 'Blessed be his glorious "
                               "name forever; may the whole earth be filled with his glory! Amen and "
                               "Amen!' (72:19). The divine glory (kavod) that fills the temple (1 Kings "
                               "8:11) will one day fill the entire earth -- the cosmic mountain of Zion "
                               "expanding to encompass all creation.",

        "sections": [
            {
                "heading": "The Righteous Judge of the Poor (72:1-7)",
                "body": "'Give the king your justice (mishpat), O God, and your righteousness "
                        "(tsidqah) to the royal son!' (72:1). The psalm opens with a prayer that "
                        "the king receive YHWH's own justice -- not human wisdom but divine equity. "
                        "'May he judge your people with righteousness, and your poor with justice!' "
                        "(72:2). The test of the ideal king is not military conquest but care for "
                        "the vulnerable. 'May the mountains bear prosperity (shalom) for the "
                        "people, and the hills, in righteousness!' (72:3). The land itself "
                        "responds to the king's justice with fertility. 'May he defend the cause "
                        "of the poor of the people, give deliverance to the children of the "
                        "needy, and crush the oppressor!' (72:4). Justice and deliverance are "
                        "inseparable: to judge rightly is to save the weak and crush the powerful "
                        "who exploit them. 'May they fear you while the sun endures, and as long "
                        "as the moon, throughout all generations!' (72:5). The king's reign is "
                        "measured by cosmic time -- as long as sun and moon exist. 'May he be "
                        "like rain (matar) that falls on the mown grass, like showers (revivim) "
                        "that water the earth!' (72:6). The king brings life and refreshment to "
                        "a parched world. 'In his days may the righteous flourish, and peace "
                        "(shalom) abound, till the moon be no more!' (72:7)."
            },
            {
                "heading": "Universal Dominion and the Abrahamic Blessing (72:8-17)",
                "body": "'May he have dominion (yerd) from sea to sea, and from the River to the "
                        "ends of the earth!' (72:8). The verb yerd ('to rule, have dominion') "
                        "echoes Genesis 1:28 and Psalm 8:6 -- the messianic king fulfills the "
                        "original human dominion mandate. 'May desert tribes bow down before him, "
                        "and his enemies lick the dust!' (72:9). 'May the kings of Tarshish and "
                        "of the coastlands render him tribute; may the kings of Sheba and Seba "
                        "bring gifts!' (72:10). Tarshish (western Mediterranean, possibly Spain) "
                        "and Sheba (southwest Arabia) represent the extremes of the known world. "
                        "'All kings fall down before him; all nations serve him!' (72:11). The "
                        "basis for this universal authority is not military power but compassion: "
                        "'For he delivers the needy when he calls, the poor and him who has no "
                        "helper' (72:12). The climax: 'May his name endure forever (le'olam), "
                        "his fame continue as long as the sun! May people be blessed in him (be "
                        "blessed through him -- yitbaraku vo), all nations call him blessed!' "
                        "(72:17). The phrase yitbaraku vo is the hitpael of barakh with the "
                        "preposition be -- the same construction as Genesis 12:3. The Abrahamic "
                        "blessing flows through this king to all nations. The doxology follows: "
                        "'Blessed be YHWH God, the God of Israel, who alone does wondrous things. "
                        "Blessed be his glorious name forever; may the whole earth be filled with "
                        "his glory!' (72:18-19)."
            }
        ]
    }
]
