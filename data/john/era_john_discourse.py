"""
era_john_discourse.py -- The Farewell Discourse and I AM Deep Dives (John 14-19)

John's Gospel reaches its theological summit in two interlocking sequences:
the seven I AM statements (scattered through the Book of Signs and the Farewell
Discourse) and the Farewell Discourse itself (John 14-17), which is the longest
sustained teaching of Jesus in any Gospel. The I AM statements are not random
metaphors -- they are ego eimi declarations that invoke the divine name revealed
at the burning bush (Exod 3:14) and force a decision: either Jesus is YHWH
incarnate or he is a blasphemer. The Farewell Discourse (Upper Room) is Jesus'
final instruction to the disciples before the cross. It covers the Paraclete
(Holy Spirit), the vine and branches, the world's hatred, the Spirit of Truth,
the High Priestly Prayer, and the cosmic meaning of the cross. These chapters
are where John's theology reaches its densest concentration: Christology,
pneumatology, ecclesiology, and eschatology converge in Jesus' last words
before the "hour" that the entire Gospel has been building toward.
"""

CHAPTERS = [
    {
        "id": "john-discourse-01",
        "ref": "John 6:35-58, 8:12-59, 10:1-18, 11:25-26, 14:6, 15:1-8",
        "chapter_num": 1,
        "title": "I AM -- The Divine Name in John",
        "era": "john_discourse",
        "type": "chapter",
        "themes": ["DC", "GLORY", "SEED", "KING", "TYPE"],

        "synopsis": "The seven ego eimi statements with predicates form the christological backbone "
                    "of John's Gospel. Each claim reaches into the Old Testament and pulls forward a "
                    "divine attribute that Jesus applies to himself: 'I am the bread of life' (6:35) -- "
                    "the manna from heaven that sustained Israel in the wilderness; 'I am the light of "
                    "the world' (8:12) -- the pillar of fire that led Israel through darkness; 'I am the "
                    "door of the sheep' (10:7) -- the only legitimate entry to the covenant flock; 'I am "
                    "the good shepherd' (10:11) -- YHWH himself who shepherds Israel (Ezek 34:11-16); "
                    "'I am the resurrection and the life' (11:25) -- the one who holds the keys of death "
                    "and Sheol; 'I am the way, the truth, and the life' (14:6) -- the exclusive mediator "
                    "between God and humanity; 'I am the true vine' (15:1) -- replacing unfaithful Israel "
                    "(Isa 5:1-7) as the source of covenant life. [A] Direct Scripture. But behind all "
                    "seven stands the absolute ego eimi of John 8:58: 'Before Abraham was, I AM (ego "
                    "eimi).' [A] This is not a predicated metaphor -- it is the divine name claim. The "
                    "Jews picked up stones because they understood exactly what Jesus was saying: he was "
                    "claiming to be the I AM of Exodus 3:14, the self-existent one who spoke to Moses "
                    "from the burning bush. [B] The high priest's reaction at the trial (Mark 14:62-63) "
                    "-- tearing his robes -- was not because Jesus claimed to be the Messiah (many did), "
                    "but because he claimed to be the cloud-rider of Daniel 7:13, a prerogative belonging "
                    "exclusively to YHWH in the Old Testament (Ps 68:4, 104:3, Deut 33:26, Isa 19:1).",

        "key_verse": {
            "ref": "John 8:58",
            "text": "Jesus said to them, 'Truly, truly, I say to you, before Abraham was, I am.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ego eimi (I AM -- Greek rendering of the divine name; when Jesus uses it without a "
            "predicate in 8:58, it echoes the Hebrew ehyeh asher ehyeh, 'I AM WHO I AM,' of Exodus "
            "3:14; the Septuagint renders Exodus 3:14 as ego eimi ho on, 'I am the one who is')",
            "artos tes zoes (bread of life -- 6:35; artos = bread/loaf, zoe = life; Jesus as the "
            "true manna that gives eternal life, surpassing the wilderness manna that sustained "
            "the body temporarily; cf. Exod 16:4, Ps 78:24-25)",
            "phos tou kosmou (light of the world -- 8:12; phos = light, kosmos = world/ordered "
            "creation; Jesus as the cosmic light that dispels the darkness of the fallen world; "
            "echoes the pillar of fire, Exod 13:21, and the Servant light, Isa 42:6, 49:6)",
            "ho poimen ho kalos (the good shepherd -- 10:11; poimen = shepherd, kalos = good/ "
            "noble/beautiful; Jesus claims the role that Ezekiel 34 reserves for YHWH himself: "
            "'I myself will search for my sheep... I myself will be the shepherd of my flock')",
            "he anastasis kai he zoe (the resurrection and the life -- 11:25; anastasis = "
            "resurrection/rising up, zoe = life; Jesus does not merely promise resurrection -- "
            "he IS the resurrection; the power of life resides in his person)",
            "he hodos kai he aletheia kai he zoe (the way, the truth, and the life -- 14:6; "
            "hodos = way/road/path, aletheia = truth/reality, zoe = life; three attributes "
            "in one declaration -- Jesus is the exclusive path to the Father)",
            "he ampelos he alethine (the true vine -- 15:1; ampelos = vine/grapevine, alethinos "
            "= true/genuine/real; Israel was the vine that failed (Isa 5, Jer 2:21, Ezek 15); "
            "Jesus is the true vine that produces the fruit Israel never could)"
        ],

        "ane_backdrop": "The formula 'I am [deity]' was widespread in the ancient Near East as a "
                        "self-revelation formula for gods. Egyptian texts record the sun god Re "
                        "declaring 'I am Khepri in the morning, Re at noon, Atum in the evening' -- "
                        "a divine self-identification pattern. In Mesopotamian hymns, Ishtar declares "
                        "'I am the queen of heaven and earth.' The Baal Cycle has Baal announce his "
                        "identity through deeds of power. But the Hebrew pattern is unique: YHWH's "
                        "'I AM WHO I AM' (ehyeh asher ehyeh, Exod 3:14) is not a predicated identity "
                        "('I am the god of X') but an absolute self-existence claim -- the name "
                        "derives from the verb 'to be' (hayah). When Jesus uses ego eimi absolutely "
                        "(8:58, 18:6), he claims not merely divine status but the specific identity "
                        "of YHWH. The shepherd imagery also has deep ANE roots: Mesopotamian kings "
                        "were called 'shepherd of the people,' and the Code of Hammurabi opens with "
                        "Hammurabi as the shepherd appointed by the gods. But Ezekiel 34 strips the "
                        "title from human kings and reserves it for YHWH alone -- and Jesus claims "
                        "that role directly.",

        "second_temple": [
            {
                "source": "Dead Sea Scrolls -- 4Q521 (Messianic Apocalypse)",
                "summary": "This fragment describes a coming figure through whom God will 'heal the "
                           "wounded, revive the dead, and bring good news to the poor.' It attributes "
                           "resurrection power to a messianic agent.",
                "relevance": "Jesus' claim 'I am the resurrection and the life' (11:25) fits within "
                             "the Second Temple expectation of a messianic figure with divine power "
                             "over death. But Jesus goes beyond the expectation: he does not merely "
                             "channel God's resurrection power -- he IS the resurrection."
            },
            {
                "source": "Philo of Alexandria, On Dreams (De Somniis 1.229-230)",
                "summary": "Philo interprets the burning bush theophany and the 'I AM' as God's "
                           "declaration of absolute self-existence: God alone truly 'is,' and all "
                           "created beings derive their existence from him.",
                "relevance": "Philo's philosophical reflection on 'I AM' as a claim to absolute being "
                             "illuminates how a first-century Jewish audience would hear Jesus' ego eimi "
                             "in 8:58 -- as a direct claim to the divine attribute of self-existence."
            },
            {
                "source": "Isaiah 43:10-13 (Septuagint/LXX)",
                "summary": "YHWH declares through Isaiah: 'You are my witnesses... that you may know "
                           "and believe me and understand that I am he (ego eimi). Before me no god "
                           "was formed, nor shall there be any after me. I, I am the LORD (ego eimi), "
                           "and besides me there is no savior.'",
                "relevance": "The LXX uses the same ego eimi formula that Jesus uses in John 8:58. "
                             "Isaiah's context is explicitly monotheistic: ego eimi is YHWH's exclusive "
                             "self-designation. Jesus' use of the same formula in the same absolute way "
                             "is a claim to be the speaker of Isaiah 43."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 3:14", "note": "'God said to Moses, I AM WHO I AM (ehyeh asher ehyeh)' -- the divine name that Jesus invokes with the absolute ego eimi of John 8:58", "type": "ot"},
            {"ref": "Isaiah 43:10, 25; 45:18", "note": "YHWH's ego eimi declarations in the LXX -- 'I am he' (ego eimi) -- the exclusive self-designation of the God of Israel that Jesus appropriates", "type": "ot"},
            {"ref": "Ezekiel 34:11-16", "note": "'I myself will search for my sheep... I myself will be the shepherd of my flock' -- YHWH reclaims the shepherd role that Jesus claims in John 10:11", "type": "ot"},
            {"ref": "Isaiah 5:1-7", "note": "The Song of the Vineyard -- Israel as YHWH's vine that produced wild grapes instead of good fruit; Jesus replaces the failed vine as 'the true vine' (15:1)", "type": "ot"},
            {"ref": "Psalm 23:1", "note": "'The LORD is my shepherd' -- David identifies YHWH as his shepherd; Jesus claims that identity directly: 'I am the good shepherd' (10:11)", "type": "ot"},
            {"ref": "Mark 14:62-63", "note": "Jesus declares 'I am' (ego eimi) and claims to be the cloud-rider of Dan 7:13 -- the high priest tears his robes because cloud-riding is an exclusively divine prerogative (Ps 68:4, Deut 33:26)", "type": "nt"},
            {"ref": "Daniel 7:13-14", "note": "The Son of Man comes 'with the clouds of heaven' to the Ancient of Days -- the cloud-rider role that belongs to YHWH alone in the OT, claimed by Jesus at his trial", "type": "ot"},
            {"ref": "Revelation 1:8, 17-18", "note": "'I am the Alpha and the Omega... I am the first and the last, and the living one. I died, and behold I am alive forevermore, and I have the keys of Death and Hades' -- the risen Christ claims the I AM identity", "type": "nt"}
        ],

        "divine_council_note": "The seven I AM statements are not merely christological titles -- they are "
                               "divine council credentials. In the Old Testament, YHWH's identity is revealed "
                               "through what he does for Israel: he provides bread (manna), light (pillar of "
                               "fire), shepherding (Ezek 34), resurrection (Ezek 37), the way of life (Deut "
                               "30:15-20), and fruitfulness (the vine metaphor). When Jesus says 'I AM the "
                               "bread / light / shepherd / resurrection / way / vine,' he is systematically "
                               "claiming every function that the Old Testament reserves for YHWH. This is why "
                               "Alan Segal's 'two powers in heaven' framework is essential: the Second Temple "
                               "Jewish world already had a category for a second divine figure who shared "
                               "YHWH's prerogatives. Jesus' I AM statements fill that category with a specific "
                               "person. The absolute ego eimi of 8:58 is the capstone: Jesus does not merely "
                               "share YHWH's functions -- he shares YHWH's name. The soldiers falling to the "
                               "ground when Jesus says ego eimi in the garden (18:6) confirms that the divine "
                               "name has power even from the mouth of the incarnate Word. The high priest's "
                               "reaction at the trial (Mark 14:62-63) shows that the divine council theology "
                               "was understood: claiming to be the cloud-rider who sits at the right hand of "
                               "Power was not a messianic claim -- it was a claim to be the second YHWH figure "
                               "of Daniel 7, Psalm 110, and the entire 'two powers' tradition.",

        "sections": [
            {
                "heading": "The Seven Predicated I AM Statements -- YHWH's Functions Made Flesh",
                "body": "Each predicated ego eimi statement takes a divine function from the Old Testament "
                        "and locates it in the person of Jesus. 'I am the bread of life' (6:35) answers "
                        "the crowd's demand for a sign like Moses' manna (6:30-31). Jesus' response is "
                        "stunning: the manna was not from Moses but from the Father, and Jesus himself is "
                        "the true bread from heaven (6:32-33). 'Whoever comes to me shall not hunger, and "
                        "whoever believes in me shall never thirst' (6:35). The claim escalates: 'I am the "
                        "living bread that came down from heaven. If anyone eats of this bread, he will live "
                        "forever' (6:51). 'I am the light of the world' (8:12) is spoken during the Feast "
                        "of Tabernacles, when four great menorahs illuminated the Temple courts -- Jesus "
                        "claims to be what those lights symbolized: the divine presence that guided Israel "
                        "as the pillar of fire (Exod 13:21). 'I am the door' (10:7, 9) and 'I am the good "
                        "shepherd' (10:11, 14) draw on Ezekiel 34, where YHWH condemns Israel's failed "
                        "shepherds and declares: 'I myself will search for my sheep... I will rescue them' "
                        "(Ezek 34:11-12). Jesus claims the role that Ezekiel reserves for YHWH alone. "
                        "'I am the resurrection and the life' (11:25) is spoken to Martha before the raising "
                        "of Lazarus -- Jesus does not say 'I will give resurrection'; he says 'I AM the "
                        "resurrection.' The power over death resides in his person, not in an external gift. "
                        "'I am the way, the truth, and the life' (14:6) and 'I am the true vine' (15:1) "
                        "complete the set in the Upper Room discourse."
            },
            {
                "heading": "The Absolute Ego Eimi -- The Name Above All Names (8:58)",
                "body": "The absolute ego eimi of John 8:58 is the most explosive christological statement "
                        "in the Gospels. The context is a debate about Abraham: the Jews claim Abraham as "
                        "their father (8:39). Jesus responds that Abraham 'rejoiced that he would see my "
                        "day. He saw it and was glad' (8:56). The crowd objects: 'You are not yet fifty "
                        "years old, and have you seen Abraham?' (8:57). Jesus' answer shatters every "
                        "category: 'Before Abraham was (prin Abraam genesthai), I AM (ego eimi)' (8:58). "
                        "The grammar is deliberate: Abraham 'came into being' (genesthai, aorist -- a point "
                        "in time) but Jesus 'I AM' (eimi, present tense -- continuous, timeless existence). "
                        "This is not 'before Abraham was, I was' (which would indicate mere pre-existence) "
                        "but 'before Abraham was, I AM' -- the present tense signals eternal self-existence. "
                        "The crowd understood perfectly: 'they picked up stones to throw at him' (8:59). "
                        "Stoning was the penalty for blasphemy (Lev 24:16). They were not stoning him for "
                        "claiming to be old -- they were stoning him for claiming to be YHWH. The connection "
                        "to Exodus 3:14 is unmistakable: when Moses asked God's name, God answered ehyeh "
                        "asher ehyeh ('I AM WHO I AM'). The Septuagint renders this ego eimi ho on ('I am "
                        "the one who is'). Jesus uses the same formula. Isaiah 43:10 reinforces this: 'that "
                        "you may know and believe me and understand that I am he (ego eimi).' Jesus is not "
                        "borrowing divine language as a metaphor -- he is speaking as the God who spoke to "
                        "Moses and to Isaiah."
            },
            {
                "heading": "The Cloud-Rider Claim -- Why the High Priest Tore His Robes",
                "body": "Mark 14:61-63 records the moment the high priest asks Jesus directly: 'Are you "
                        "the Christ, the Son of the Blessed?' Jesus answers: 'I am (ego eimi), and you "
                        "will see the Son of Man seated at the right hand of Power, and coming with the "
                        "clouds of heaven.' The high priest tears his garments and declares: 'What further "
                        "witnesses do we need? You have heard his blasphemy.' The critical question is: "
                        "why was this blasphemy? Claiming to be the Messiah was not blasphemous -- many "
                        "claimed it (Bar Kochba, Theudas, the Egyptian). What was blasphemous was the "
                        "cloud-rider claim. In the Old Testament, riding the clouds is an exclusively "
                        "divine prerogative. Psalm 68:4 (MT 68:5): 'Sing to God, ride to him who rides "
                        "through the deserts' -- but the Hebrew rokev ba-aravot can also mean 'rider of "
                        "the clouds,' and the Ugaritic parallel (Baal as rkb 'rpt, 'rider of the clouds') "
                        "confirms this meaning. Deuteronomy 33:26: 'There is none like God, O Jeshurun, "
                        "who rides through the heavens to your help, through the skies in his majesty.' "
                        "Isaiah 19:1: 'Behold, the LORD is riding on a swift cloud and comes to Egypt.' "
                        "Psalm 104:3: 'He makes the clouds his chariot.' Only YHWH rides the clouds. "
                        "Daniel 7:13 presents 'one like a son of man' coming 'with the clouds of heaven' "
                        "-- this figure receives universal dominion from the Ancient of Days. By combining "
                        "ego eimi with the cloud-rider role and the right hand of Power (Ps 110:1), Jesus "
                        "claimed to be the second YHWH figure of the divine council tradition -- not "
                        "merely the Messiah, but God himself."
            },
            {
                "heading": "I AM as Theophany -- The Garden Arrest (18:4-8)",
                "body": "The divine name claim receives a dramatic physical confirmation in the garden of "
                        "Gethsemane. When the soldiers and officers arrive to arrest Jesus, he steps forward "
                        "and asks: 'Whom do you seek?' They answer: 'Jesus of Nazareth.' Jesus replies: "
                        "'I am he' (ego eimi -- 18:5). John records what happened next: 'When Jesus said "
                        "to them, \"I am he,\" they drew back and fell to the ground' (18:6). This is not "
                        "natural surprise -- it is a theophanic reaction. Throughout the Old Testament, "
                        "falling to the ground is the response to encountering the divine presence: Ezekiel "
                        "falls on his face before the glory of YHWH (Ezek 1:28, 3:23, 44:4); Daniel falls "
                        "prostrate before the angelic messenger (Dan 8:17, 10:9); Isaiah cries 'Woe is me!' "
                        "in the throne room (Isa 6:5); the priests cannot stand to minister when the glory "
                        "fills Solomon's Temple (1 Kings 8:11). A Roman cohort (speira -- up to 600 soldiers) "
                        "does not fall backward because a carpenter says 'I am he.' They fall because the "
                        "divine name has power, even from the lips of the one about to be arrested. John "
                        "records this detail deliberately: the ego eimi that claimed eternal self-existence "
                        "in 8:58, that provoked stoning attempts, that fused every divine function into one "
                        "person -- this same ego eimi now manifests its power physically. The soldiers fall "
                        "not because Jesus used force but because the Name itself pushed them back. Even in "
                        "his voluntary submission to arrest, Jesus demonstrates that he is not a victim but "
                        "the sovereign Lord who lays down his life by his own authority (10:18). The arrest "
                        "only proceeds because Jesus allows it: 'I told you that I am he. So, if you seek "
                        "me, let these men go' (18:8)."
            }
        ]
    },

    {
        "id": "john-discourse-02",
        "ref": "John 14:1-15:27",
        "chapter_num": 2,
        "title": "The Farewell Discourse Part 1 -- John 14-15",
        "era": "john_discourse",
        "type": "chapter",
        "themes": ["DC", "SPIRIT", "SEED", "HOLY", "GLORY"],

        "synopsis": "The Farewell Discourse begins in the Upper Room on the night of Jesus' arrest. "
                    "The disciples are troubled -- Jesus has just predicted his betrayal (13:21) and "
                    "Peter's denial (13:38). Into this atmosphere of confusion and fear, Jesus speaks "
                    "some of the most theologically dense words in all of Scripture. John 14 opens with "
                    "'Let not your hearts be troubled' (14:1) and immediately launches into three "
                    "explosive claims. [A] First: 'I am the way, and the truth, and the life. No one "
                    "comes to the Father except through me' (14:6) -- the exclusive mediation claim. "
                    "Second: 'Whoever has seen me has seen the Father' (14:9) -- the incarnational "
                    "identity claim. Third: the promise of 'another Helper (allon parakleton), the "
                    "Spirit of truth' (14:16-17) -- the Paraclete who will continue Jesus' presence "
                    "after the ascension. [A] Direct Scripture throughout. John 15 shifts to the vine "
                    "metaphor: 'I am the true vine, and my Father is the vinedresser' (15:1). Israel "
                    "was YHWH's vine (Isa 5:1-7, Jer 2:21, Ezek 15:1-8, Ps 80:8-16) but produced "
                    "wild grapes. Jesus replaces the failed vine and warns: 'Apart from me you can do "
                    "nothing' (15:5). [B] The cosmic conflict framework emerges in 15:18-27: the world "
                    "hates the disciples because it hated Jesus first. This is not social rejection but "
                    "the hostility of a world system governed by fallen powers (the archon tou kosmou "
                    "of 12:31, 14:30) against the kingdom of light.",

        "key_verse": {
            "ref": "John 14:6",
            "text": "Jesus said to him, 'I am the way, and the truth, and the life. No one comes to the Father except through me.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "he hodos kai he aletheia kai he zoe (the way, the truth, and the life -- 14:6; "
            "hodos = way/path, the singular road to the Father; aletheia = truth/ultimate reality; "
            "zoe = life/the divine life; three attributes that converge in one person)",
            "allos parakletos (another Helper/Advocate -- 14:16; allos = another of the same kind "
            "(not heteros, another of a different kind); parakletos = one called alongside, an "
            "advocate/intercessor/comforter; the Spirit is 'another' like Jesus, of the same divine "
            "nature; the Spirit continues Jesus' presence and ministry)",
            "to pneuma tes aletheias (the Spirit of truth -- 14:17, 15:26, 16:13; pneuma = spirit/ "
            "breath/wind; aletheia = truth; the Spirit who guides into all truth and testifies about "
            "Jesus; the third person of the divine council's inner circle)",
            "he ampelos he alethine (the true vine -- 15:1; ampelos = vine, alethinos = true/ "
            "genuine/real; Jesus replaces Israel as the source of covenant life; the Father is the "
            "georgos, the vinedresser/farmer who prunes and tends)",
            "menate en emoi (abide in me -- 15:4; meno = abide/remain/dwell/stay; the vine metaphor "
            "demands continuous connection; fruitfulness is impossible apart from union with Christ)",
            "kosmos (world -- 15:18-19; not the physical creation but the organized system of "
            "rebellion against God; the world 'hates' the disciples because they have been 'chosen "
            "out of the world' -- the Deuteronomy 32 framework of nations under hostile powers)"
        ],

        "ane_backdrop": "The vine as a national symbol was widespread in the ancient Near East. Israel's "
                        "self-identification as YHWH's vine is attested in multiple Old Testament passages "
                        "(Isa 5, Jer 2:21, Hos 10:1, Ps 80:8-16). The Maccabean coinage bore a vine symbol "
                        "representing Israel, and Herod's Temple had a massive golden vine decoration over "
                        "the entrance to the Holy Place (Josephus, Antiquities 15.395). When Jesus says 'I "
                        "am the true vine,' he is standing in the shadow of the Temple's golden vine and "
                        "replacing it: the true Israel is not the nation, not the Temple, but Jesus himself. "
                        "The Paraclete concept also has ancient parallels: in Mesopotamian legal texts, a "
                        "personal god could serve as an advocate or intercessor for the individual before "
                        "the assembly of the gods. The Hebrew concept of a melitz (intercessor/mediator, "
                        "Job 33:23) and the angelic advocate (Michael as Israel's patron in Dan 12:1) "
                        "provide the background for the Paraclete as a divine advocate who testifies on "
                        "behalf of believers in the cosmic court.",

        "second_temple": [
            {
                "source": "Dead Sea Scrolls -- 1QS 3:18-21 (Community Rule)",
                "summary": "The Qumran community spoke of the 'Spirit of Truth' (ruach emet) and the "
                           "'Spirit of Falsehood' (ruach avel) as two opposing cosmic forces. The sons "
                           "of light walk by the Spirit of Truth; the sons of darkness by the Spirit "
                           "of Falsehood.",
                "relevance": "Jesus' promise of 'the Spirit of truth' (to pneuma tes aletheias, 14:17) "
                             "resonates with the Qumran dualism -- but personalizes it. The Spirit is not "
                             "an impersonal cosmic force but 'another Paraclete' of the same kind as Jesus."
            },
            {
                "source": "Testament of Judah 20:1-5 (Testaments of the Twelve Patriarchs)",
                "summary": "Two spirits attend upon humanity: the spirit of truth and the spirit of "
                           "error. The spirit of truth testifies to all things and convicts concerning "
                           "sins.",
                "relevance": "The Second Temple two-spirits framework illuminates Jesus' contrast between "
                             "the Spirit of truth and 'the ruler of this world' (14:30) -- two opposing "
                             "powers in a cosmic conflict over humanity."
            },
            {
                "source": "Sirach 24:17-21 (Ecclesiasticus)",
                "summary": "Personified Wisdom says: 'Like the vine I bud forth delights, and my "
                           "blossoms become glorious and abundant fruit. Come to me, you who desire me, "
                           "and eat your fill of my fruits.'",
                "relevance": "The Wisdom tradition's vine imagery connects to Jesus' 'I am the true vine' "
                             "(15:1) -- Jesus embodies the divine Wisdom that Israel's sages celebrated, "
                             "but goes beyond metaphor: he IS the vine, not merely like it."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 5:1-7", "note": "The Song of the Vineyard -- YHWH planted Israel as a vine, but it produced wild grapes; Jesus replaces the failed vine as 'the true vine' (15:1)", "type": "ot"},
            {"ref": "Ezekiel 15:1-8", "note": "The vine of Jerusalem is useless wood fit only for burning -- the failure of Israel as YHWH's vine that Jesus reverses by becoming the true vine", "type": "ot"},
            {"ref": "Psalm 80:8-16", "note": "'You brought a vine out of Egypt... why then have you broken down its walls?' -- Israel as YHWH's vine transplanted from Egypt, now broken; Jesus is the restoration", "type": "ot"},
            {"ref": "Joel 2:28-32", "note": "'I will pour out my Spirit on all flesh' -- the prophetic promise that Jesus begins to fulfill through the Paraclete promise of John 14-16", "type": "ot"},
            {"ref": "1 John 2:1", "note": "'We have an advocate (parakletos) with the Father, Jesus Christ the righteous' -- the same Johannine community applies the Paraclete title to the ascended Jesus", "type": "nt"},
            {"ref": "Romans 8:26-27", "note": "'The Spirit himself intercedes for us with groanings too deep for words' -- Paul's parallel to the Paraclete as divine intercessor", "type": "nt"},
            {"ref": "Jeremiah 2:21", "note": "'I planted you a choice vine, wholly of pure seed. How then have you turned degenerate and become a wild vine?' -- YHWH's lament over Israel that Jesus' 'true vine' answers", "type": "ot"}
        ],

        "divine_council_note": "The Farewell Discourse reveals the inner workings of the divine council in "
                               "an unprecedented way. Jesus promises 'another Paraclete' (allon parakleton, "
                               "14:16) -- the word allos ('another of the same kind') means the Spirit is "
                               "another divine person of the same nature as Jesus. The Paraclete 'will teach "
                               "you all things and bring to your remembrance all that I have said to you' "
                               "(14:26) -- the Spirit continues the Son's mission just as the Son continued "
                               "the Father's mission. This is the divine council operating through the "
                               "economy of redemption: the Father sends the Son (3:16); the Son and Father "
                               "send the Spirit (14:26, 15:26); the Spirit empowers the ekklesia. The cosmic "
                               "conflict dimension is equally present: 'the ruler of this world (ho archon "
                               "tou kosmou) is coming. He has no claim on me' (14:30). The archon tou kosmou "
                               "is the Deuteronomy 32 framework in its New Testament expression -- the "
                               "hostile power who currently exercises authority over the nations (cf. the "
                               "territorial princes of Dan 10:13, 20-21). But Jesus declares that this ruler "
                               "'has no claim' (ouk echei ouden) on him -- the sinless Son is immune to the "
                               "accusations that give the adversary his power. The world's hatred (15:18-25) "
                               "is not sociological but cosmological: the world-system hates the light "
                               "because its deeds are evil (3:19-20), and the disciples, chosen out of the "
                               "world (15:19), become targets of the same hostility that the rebellious "
                               "powers direct at Christ.",

        "sections": [
            {
                "heading": "The Way, the Truth, and the Life -- Exclusive Mediation (14:1-14)",
                "body": "Jesus begins the discourse with comfort: 'Let not your hearts be troubled. Believe "
                        "in God; believe also in me' (14:1). The parallel construction places belief in Jesus "
                        "on the same level as belief in God -- a claim no mere prophet could make. He speaks "
                        "of 'my Father's house' with 'many rooms' (monai pollai, 14:2) -- not individual "
                        "mansions in the sky but dwelling places in the Father's household, the language of "
                        "family belonging. Thomas asks, 'Lord, we do not know where you are going. How can "
                        "we know the way?' (14:5). Jesus' answer is the sixth I AM statement: 'I am the way "
                        "(he hodos), and the truth (he aletheia), and the life (he zoe). No one comes to "
                        "the Father except through me' (14:6). Three articles, three nouns, one person. The "
                        "exclusivity claim ('no one... except through me') is not narrow-mindedness -- it is "
                        "the logical consequence of the incarnation. If the Logos through whom all things "
                        "were made has become flesh (1:1-14), then he is necessarily the only mediator "
                        "between the Creator and the creation. Philip asks, 'Lord, show us the Father' "
                        "(14:8). Jesus' response is astonishing: 'Whoever has seen me has seen the Father' "
                        "(14:9). This is not metaphor -- it is incarnational reality. The invisible God "
                        "(1:18) has become visible in Jesus. The same word used in the prologue (exegesato, "
                        "'made known/exegeted') is now embodied: Jesus does not merely describe the Father; "
                        "he IS the visible manifestation of the Father's nature, character, and will."
            },
            {
                "heading": "The Promise of the Paraclete -- Another Helper of the Same Kind (14:15-31)",
                "body": "The Paraclete passages (14:15-17, 14:25-26, 15:26-27, 16:7-15) are among the most "
                        "important pneumatological texts in the New Testament. Jesus promises: 'I will ask "
                        "the Father, and he will give you another Helper (allon parakleton), to be with you "
                        "forever, the Spirit of truth (to pneuma tes aletheias)' (14:16-17). The word allos "
                        "is critical: it means 'another of the same kind,' not heteros, 'another of a "
                        "different kind.' The Paraclete is another divine person who is like Jesus -- of the "
                        "same nature, performing the same role of advocacy and truth-telling. The Paraclete "
                        "'dwells with you and will be in you' (14:17) -- the progression from 'with' (para) "
                        "to 'in' (en) marks the new covenant's internalization of the divine presence. Under "
                        "the old covenant, the Spirit came upon individuals temporarily (Judg 3:10, 6:34, "
                        "1 Sam 16:13); under the new covenant, the Spirit indwells permanently. 'The Helper, "
                        "the Holy Spirit, whom the Father will send in my name, he will teach you all things "
                        "and bring to your remembrance all that I have said to you' (14:26). The Spirit's "
                        "ministry is not independent of Christ but Christocentric: he teaches what Christ "
                        "taught and reminds of what Christ said. Then the cosmic conflict note: 'the ruler "
                        "of this world is coming. He has no claim on me' (14:30). The archon tou kosmou -- "
                        "the rebellious power who governs the world-system (cf. 2 Cor 4:4, Eph 2:2) -- "
                        "approaches for the final confrontation, but finds nothing in Jesus to accuse."
            },
            {
                "heading": "The True Vine -- Replacing Unfaithful Israel (15:1-17)",
                "body": "The seventh and final I AM statement: 'I am the true vine (he ampelos he alethine), "
                        "and my Father is the vinedresser (ho georgos)' (15:1). The word alethinos ('true/ "
                        "genuine/real') implies that there was a false or shadow vine -- and the Old Testament "
                        "identifies it explicitly. Isaiah 5:1-7: YHWH planted Israel as a vineyard, expecting "
                        "good grapes, but it produced wild grapes (be'ushim). Jeremiah 2:21: 'I planted you "
                        "a choice vine... how then have you turned degenerate?' Ezekiel 15:1-8: the wood of "
                        "the vine is useless for anything -- it can only be burned. Psalm 80:8-16: 'You "
                        "brought a vine out of Egypt... why then have you broken down its walls?' Israel was "
                        "the vine that failed. Jesus is the true vine that succeeds. 'Abide in me, and I in "
                        "you' (15:4) -- the key verb meno (abide/remain) appears eleven times in 15:1-11. "
                        "Fruitfulness is not achieved by effort but by connection: 'Apart from me you can do "
                        "nothing' (15:5). Branches that do not bear fruit are 'taken away' (airei, 15:2); "
                        "branches that bear fruit are 'pruned' (kathairei, 15:2) -- a wordplay in Greek "
                        "(aireo/kathairo). The fruit is not merely good works but love: 'This is my "
                        "commandment, that you love one another as I have loved you. Greater love has no one "
                        "than this, that someone lay down his life for his friends' (15:12-13). The standard "
                        "of love is the cross. 'You did not choose me, but I chose you' (15:16) -- election "
                        "is the ground of belonging, not human decision."
            },
            {
                "heading": "The World's Hatred -- Cosmic Conflict in the Upper Room (15:18-27)",
                "body": "The discourse shifts from the intimacy of vine-and-branches to the reality of cosmic "
                        "warfare. 'If the world hates you, know that it has hated me before it hated you' "
                        "(15:18). The kosmos here is not the physical creation but the organized system of "
                        "rebellion against God -- the Deuteronomy 32 framework where the nations have been "
                        "assigned to corrupt sons of God who rule them in opposition to YHWH. 'If you were "
                        "of the world, the world would love you as its own; but because you are not of the "
                        "world, but I chose you out of the world, therefore the world hates you' (15:19). "
                        "The language of being 'chosen out of the world' echoes Israel's election out of the "
                        "nations in Deuteronomy 32:8-9 -- but now it is not an ethnic nation but the ekklesia "
                        "that is YHWH's chosen people, called out of the world-system to be his inheritance. "
                        "'Remember the word that I said to you: A servant is not greater than his master. If "
                        "they persecuted me, they will also persecute you' (15:20). Persecution is not an "
                        "accident of history but a structural feature of the cosmic conflict. The world-system "
                        "persecutes the ekklesia because the ekklesia represents the kingdom that will "
                        "displace the rulers of this age (1 Cor 2:6-8). 'They will do all these things to "
                        "you on account of my name, because they do not know him who sent me' (15:21). The "
                        "rejection of Jesus is ultimately the rejection of the Father -- the same pattern as "
                        "Israel's rejection of YHWH through the judges and kings (1 Sam 8:7). The Paraclete "
                        "reappears: 'When the Helper comes, whom I will send to you from the Father, the "
                        "Spirit of truth who proceeds from the Father, he will bear witness about me' "
                        "(15:26). The Spirit's testimony in the cosmic court counters the accusations of "
                        "the archon tou kosmou."
            }
        ]
    },

    {
        "id": "john-discourse-03",
        "ref": "John 16:1-17:26",
        "chapter_num": 3,
        "title": "The Farewell Discourse Part 2 -- John 16-17",
        "era": "john_discourse",
        "type": "chapter",
        "themes": ["SPIRIT", "DC", "GLORY", "HOLY", "KING"],

        "synopsis": "John 16-17 brings the Farewell Discourse to its climax. Chapter 16 completes the "
                    "Paraclete teaching: the Spirit of Truth will 'convict the world concerning sin and "
                    "righteousness and judgment' (16:8-11) -- a cosmic legal proceeding where the Spirit "
                    "prosecutes the case against the world-system. [A] Direct Scripture. The Spirit "
                    "convicts concerning judgment 'because the ruler of this world is judged' (16:11) -- "
                    "the archon tou kosmou has already been sentenced at the cross, and the Spirit "
                    "executes the verdict in history. Jesus promises that the disciples' grief will turn "
                    "to joy 'like a woman giving birth' (16:20-22) -- resurrection joy that 'no one will "
                    "take from you.' [A] Chapter 17 is the High Priestly Prayer -- the most intimate "
                    "window into the inner life of the Godhead anywhere in Scripture. Jesus prays for his "
                    "own glorification (17:1-5), revealing that he shared the Father's glory 'before the "
                    "world existed' (17:5) -- pre-existence stated explicitly. [A] He prays for the "
                    "disciples (17:6-19) and then for all future believers (17:20-26), asking 'that they "
                    "may all be one... so that the world may believe' (17:21). [B] This unity is not "
                    "institutional ecumenism but participation in the divine life itself: 'even as you, "
                    "Father, are in me, and I in you, that they also may be in us' (17:21). The ekklesia "
                    "is called into the communion of the Godhead -- the governing assembly destined to "
                    "judge angels (1 Cor 6:3) and display God's wisdom to the cosmic powers (Eph 3:10).",

        "key_verse": {
            "ref": "John 17:5",
            "text": "And now, Father, glorify me in your own presence with the glory that I had with you before the world existed.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "elegxei ton kosmon (will convict the world -- 16:8; elegcho = to convict/expose/reprove; "
            "a legal term for cross-examination that exposes the truth; the Spirit acts as prosecutor "
            "in the cosmic court, convicting the world-system of sin, righteousness, and judgment)",
            "ho archon tou kosmou (the ruler of this world -- 16:11; archon = ruler/prince/first one; "
            "kosmos = world-system; the hostile spiritual power who governs the fallen world order; "
            "already 'judged' (kekritai, perfect tense -- completed action) at the cross)",
            "hodegeo eis pasan ten aletheian (guide into all the truth -- 16:13; hodegeo = to lead "
            "the way/guide; the Spirit as a guide who leads the community progressively into the "
            "full truth of Christ; not new revelation but deeper understanding of the same revelation)",
            "doxa (glory -- 17:5, 22, 24; the kavod/weight/radiance of the divine presence; Jesus "
            "claims to have shared this glory with the Father 'before the world existed' -- "
            "pre-temporal divine glory, not earned honor but eternal attribute)",
            "hen (one -- 17:11, 21, 22, 23; the unity Jesus prays for is not organizational uniformity "
            "but ontological participation in the divine life; 'that they may be one, even as we are "
            "one' -- the standard of unity is the Father-Son relationship itself)",
            "hagiason autous en te aletheia (sanctify them in the truth -- 17:17; hagiazo = to set "
            "apart/make holy/consecrate; the disciples are consecrated for mission just as priests "
            "were consecrated for service; the truth (aletheia) is the means of sanctification)"
        ],

        "ane_backdrop": "The High Priestly Prayer (John 17) functions within the framework of ancient "
                        "Near Eastern royal intercession. In Mesopotamian religion, the king served as "
                        "mediator between the gods and the people, interceding at the temple on behalf "
                        "of his subjects. The Akkadian term shupu ('to pray/intercede') was associated "
                        "with royal responsibility. Egyptian pharaohs were considered the intermediary "
                        "between the divine realm and humanity, offering prayers and sacrifices to "
                        "maintain cosmic order (ma'at). Israel adapted this framework: the high priest "
                        "entered the Holy of Holies once a year on the Day of Atonement (Lev 16) to "
                        "intercede for the nation. Jesus' prayer in John 17 combines the royal and "
                        "priestly roles: he intercedes as the Melchizedekian priest-king (Heb 7) who "
                        "has access to the Father's presence not through the blood of goats and calves "
                        "but through his own blood (Heb 9:11-12). The concept of divine glory existing "
                        "before creation also has ANE parallels: the Mesopotamian concept of melammu "
                        "(divine radiance) was considered an inherent attribute of the gods, not "
                        "something acquired.",

        "second_temple": [
            {
                "source": "Dead Sea Scrolls -- 1QS 4:20-23 (Community Rule)",
                "summary": "The Qumran community expected a future age when 'God will purge every wicked "
                           "deed by his truth and will cleanse the body of every person by the spirit of "
                           "holiness.' The Spirit of Truth would ultimately prevail over the Spirit of "
                           "Falsehood.",
                "relevance": "Jesus' teaching that the Spirit will 'convict the world concerning sin and "
                             "righteousness and judgment' (16:8) fulfills the Qumran expectation of a "
                             "final triumph of truth over falsehood -- but locates it in history through "
                             "the Paraclete's ongoing ministry, not only at the eschaton."
            },
            {
                "source": "1 Enoch 62:7 (Similitudes/Parables of Enoch)",
                "summary": "The Son of Man is depicted as having glory 'from the beginning' -- 'the Son "
                           "of Man was given a name, before the creation of the sun and moon, before the "
                           "creation of the stars, his name was named before the Lord of Spirits.'",
                "relevance": "Jesus' claim to glory 'before the world existed' (17:5) aligns with the "
                             "Enochic tradition of a pre-existent Son of Man figure who shares divine "
                             "glory. According to 1 Enoch, this figure was named before creation -- "
                             "Jesus claims the same pre-temporal status."
            },
            {
                "source": "Wisdom of Solomon 9:9-11",
                "summary": "'With you is wisdom (sophia), she who knows your works and was present when "
                           "you made the world; she understands what is pleasing in your sight and what "
                           "is right according to your commandments. Send her forth from the holy heavens, "
                           "and from the throne of your glory send her.'",
                "relevance": "The 'sending' language -- wisdom sent from the throne of glory -- parallels "
                             "Jesus' repeated statement that the Father 'sent' him (17:3, 8, 18, 21, 23, "
                             "25). Jesus embodies the divine Wisdom sent from the Father's presence."
            }
        ],

        "cross_refs": [
            {"ref": "Leviticus 16:1-34", "note": "The Day of Atonement -- the high priest enters the Holy of Holies to intercede for Israel; Jesus' prayer in John 17 fulfills this priestly function permanently", "type": "ot"},
            {"ref": "Psalm 110:4", "note": "'You are a priest forever after the order of Melchizedek' -- Jesus' High Priestly Prayer reflects his Melchizedekian priesthood, not Levitical (Heb 7:13-14, wrong tribe)", "type": "ot"},
            {"ref": "Ephesians 3:10", "note": "'Through the ekklesia the manifold wisdom of God might now be made known to the rulers and authorities in the heavenly places' -- the ekklesia displays divine wisdom to the powers", "type": "nt"},
            {"ref": "1 Corinthians 6:3", "note": "'Do you not know that we are to judge angels?' -- the ekklesia's cosmic destiny as governing assembly, rooted in the unity Jesus prays for in John 17", "type": "nt"},
            {"ref": "Hebrews 7:25", "note": "'He always lives to make intercession for them' -- the ongoing heavenly intercession that began in the Upper Room prayer of John 17", "type": "nt"},
            {"ref": "Isaiah 6:1-8", "note": "Isaiah sees the Lord's glory and is commissioned; Jesus claims to have shared that glory 'before the world existed' (17:5) -- the glory Isaiah glimpsed was the Logos", "type": "ot"},
            {"ref": "1 Enoch 62:7", "note": "The Son of Man's name was 'named before the Lord of Spirits' before creation -- the pre-existence tradition that Jesus claims in his prayer for restoration of pre-temporal glory", "type": "pseudepigrapha"},
            {"ref": "Daniel 10:13, 20-21", "note": "The 'prince of Persia' and 'prince of Greece' as territorial powers -- the archon tou kosmou of John 16:11 belongs to the same framework of hostile spiritual rulers", "type": "ot"}
        ],

        "divine_council_note": "John 16-17 reveals the divine council's inner dynamics and the ekklesia's "
                               "place within it. The Spirit's threefold conviction (16:8-11) operates as a "
                               "cosmic legal proceeding. The Spirit convicts 'concerning sin, because they do "
                               "not believe in me' (16:9) -- the fundamental sin is rejection of the Son, "
                               "the visible YHWH. 'Concerning righteousness, because I go to the Father' "
                               "(16:10) -- the ascension vindicates Jesus' claims; he returns to the throne "
                               "room from which he came. 'Concerning judgment, because the ruler of this "
                               "world is judged' (16:11) -- the archon tou kosmou stands convicted. The "
                               "perfect tense kekritai ('has been judged') indicates a completed verdict: "
                               "the hostile power who has governed the nations since Deuteronomy 32:8 has "
                               "been sentenced at the cross, even though the full execution of the sentence "
                               "awaits the eschaton. The High Priestly Prayer (17) then reveals the "
                               "ekklesia's cosmic assignment. 'The glory that you have given me I have "
                               "given to them, that they may be one even as we are one' (17:22). The glory "
                               "(doxa/kavod) that belongs to the divine council's inner life -- the radiance "
                               "of the throne room -- is now shared with the community of believers. This is "
                               "not metaphorical: the ekklesia participates in the divine glory because it "
                               "is destined to participate in the divine governance. 'That they may be one... "
                               "so that the world may believe' (17:21) -- the unity of the ekklesia is itself "
                               "a testimony to the watching world and to the watching powers (Eph 3:10). The "
                               "cosmic assembly that once watched the sons of God shout for joy at creation "
                               "(Job 38:7) now watches the redeemed community display the wisdom that the "
                               "rebellious powers failed to understand (1 Cor 2:7-8).",

        "sections": [
            {
                "heading": "The Spirit as Cosmic Prosecutor -- Convicting the World (16:1-15)",
                "body": "Jesus warns the disciples of coming persecution: expulsion from synagogues and "
                        "even death at the hands of those who think they are serving God (16:2). Then he "
                        "makes a startling claim: 'It is to your advantage that I go away, for if I do not "
                        "go away, the Helper will not come to you. But if I go, I will send him to you' "
                        "(16:7). The departure of the incarnate Son is necessary for the coming of the "
                        "Paraclete. The Spirit's ministry is described in legal terms: 'When he comes, he "
                        "will convict (elegxei) the world concerning sin and righteousness and judgment' "
                        "(16:8). The verb elegcho is a courtroom term: to cross-examine, to expose, to "
                        "prove guilty. The Spirit acts as a prosecutor in the cosmic court. Three charges: "
                        "(1) 'concerning sin, because they do not believe in me' (16:9) -- the fundamental "
                        "sin that underlies all others is rejection of the Son; (2) 'concerning "
                        "righteousness, because I go to the Father, and you will see me no longer' (16:10) "
                        "-- Jesus' ascension proves his righteousness; the one the world condemned is "
                        "vindicated by the Father's acceptance; (3) 'concerning judgment, because the ruler "
                        "of this world is judged' (16:11) -- the archon tou kosmou has been convicted. The "
                        "perfect tense kekritai indicates a completed, standing verdict: the hostile power "
                        "was judged at the cross. 'When the Spirit of truth comes, he will guide you into "
                        "all the truth' (16:13) -- not new revelation independent of Christ but deeper "
                        "understanding of the revelation already given in the Son."
            },
            {
                "heading": "Sorrow Turned to Joy -- The Birth Pangs Metaphor (16:16-33)",
                "body": "Jesus introduces a riddle: 'A little while, and you will see me no longer; and "
                        "again a little while, and you will see me' (16:16). The disciples are confused "
                        "(16:17-18), and Jesus explains through the metaphor of childbirth: 'When a woman "
                        "is giving birth, she has sorrow because her hour has come, but when she has "
                        "delivered the baby, she no longer remembers the anguish, for joy that a human being "
                        "has been born into the world' (16:21). The birth-pangs imagery is deeply rooted in "
                        "Old Testament prophetic tradition: Isaiah 26:17-19 connects labor pains to the "
                        "resurrection of the dead; Isaiah 66:7-9 describes Zion giving birth to a nation "
                        "'in a moment'; Micah 4:9-10 pictures Jerusalem in labor before deliverance comes. "
                        "Jesus applies this to the crucifixion and resurrection: the cross is the anguish, "
                        "the resurrection is the birth, and the resulting joy is permanent -- 'no one will "
                        "take your joy from you' (16:22). 'In that day you will ask nothing of me' (16:23) "
                        "-- the resurrection inaugurates a new era of direct access to the Father. 'In the "
                        "world you will have tribulation. But take heart; I have overcome (nenikeeka) the "
                        "world' (16:33). The perfect tense nenikeeka ('I have overcome') is remarkable: "
                        "Jesus speaks of his victory as already accomplished before the cross has even "
                        "occurred. The cosmic conflict is already decided in the divine council's decree, "
                        "even though the historical event still lies ahead."
            },
            {
                "heading": "The High Priestly Prayer -- Glory Before the World Existed (17:1-5)",
                "body": "John 17 is the longest recorded prayer of Jesus and the most sustained glimpse into "
                        "the inner relationship of Father and Son. 'Father, the hour has come. Glorify your "
                        "Son that the Son may glorify you' (17:1). The 'hour' (hora) that has been approaching "
                        "since 2:4 ('My hour has not yet come') has now arrived. 'Since you have given him "
                        "authority over all flesh, to give eternal life to all whom you have given him' (17:2) "
                        "-- the Son's authority is universal ('all flesh') yet particular ('all whom you have "
                        "given him'). Eternal life is defined: 'This is eternal life, that they know you, the "
                        "only true God, and Jesus Christ whom you have sent' (17:3). Eternal life is not "
                        "merely unending existence but relational knowledge of the Father and the Son. Then "
                        "the statement that pierces the veil of eternity: 'And now, Father, glorify me in "
                        "your own presence with the glory that I had with you before the world existed (pro "
                        "tou ton kosmon einai)' (17:5). This is the most explicit pre-existence claim in the "
                        "Gospels. Jesus does not say 'give me glory' (as though receiving something new) but "
                        "'glorify me with the glory I had' -- he is asking for the restoration of the divine "
                        "glory he voluntarily set aside in the incarnation (cf. Phil 2:6-8). The Word who "
                        "was 'with God' and 'was God' in the beginning (1:1) is now asking to return to that "
                        "pre-temporal state of shared glory. This is not the prayer of a prophet or even of "
                        "a supreme angel -- it is the prayer of the second YHWH figure requesting the "
                        "restoration of his eternal divine prerogatives."
            },
            {
                "heading": "The Unity Prayer -- Ekklesia as Cosmic Governing Assembly (17:20-26)",
                "body": "The prayer expands from the immediate disciples to 'those who will believe in me "
                        "through their word' (17:20) -- every future believer, including us. The petition: "
                        "'that they may all be one, just as you, Father, are in me, and I in you, that they "
                        "also may be in us, so that the world may believe that you sent me' (17:21). The "
                        "standard of unity is staggering: the believers' oneness is to be modeled on the "
                        "Father-Son unity -- mutual indwelling, not organizational uniformity. 'The glory "
                        "that you have given me I have given to them, that they may be one even as we are "
                        "one, I in them and you in me, that they may become perfectly one, so that the world "
                        "may know that you sent me and loved them even as you loved me' (17:22-23). The divine "
                        "glory (doxa) is shared with the community. This is the ekklesia's cosmic identity: "
                        "not an institution but a governing assembly that participates in the divine life "
                        "and manifests the divine glory to the watching world and the watching powers. Paul "
                        "unpacks this in Ephesians 3:10: 'through the ekklesia the manifold wisdom of God "
                        "might now be made known to the rulers and authorities in the heavenly places.' The "
                        "rebellious sons of God who were assigned the nations at Babel (Deut 32:8) now see "
                        "the wisdom they rejected displayed through the redeemed community. In 1 Corinthians "
                        "6:3, Paul reveals the destiny: 'Do you not know that we are to judge angels?' The "
                        "ekklesia is not merely saved -- it is commissioned as the divine council's human "
                        "delegation, destined to participate in the governance of creation itself. Jesus' "
                        "final words in the prayer: 'I made known to them your name, and I will continue to "
                        "make it known, that the love with which you have loved me may be in them, and I in "
                        "them' (17:26). The name (the divine identity) and the love (the divine nature) are "
                        "deposited in the community for eternity."
            }
        ]
    },

    {
        "id": "john-discourse-04",
        "ref": "John 18:1-19:42",
        "chapter_num": 4,
        "title": "The Hour of Glory -- John 18-19 Deep Dive",
        "era": "john_discourse",
        "type": "chapter",
        "themes": ["BLOOD", "KING", "DC", "GLORY", "SEED"],

        "synopsis": "John 18-19 narrates the Passion -- the arrest, trial, crucifixion, and burial of "
                    "Jesus -- but through a distinctly Johannine theological lens. Where the Synoptics "
                    "emphasize Jesus' suffering and abandonment, John emphasizes his sovereignty and "
                    "glory. [A] The arrest begins with a theophanic moment: when Jesus says ego eimi "
                    "(18:5-6), the entire arresting party 'drew back and fell to the ground' -- the "
                    "divine name has power even from the lips of the one being arrested. [A] The trial "
                    "before Pilate is the most extended in any Gospel, and John structures it as a "
                    "dramatic irony: the Roman governor asks 'What is truth?' (18:38) while standing "
                    "face-to-face with the one who IS truth (14:6). [A] The crucifixion scene reaches "
                    "its climax with tetelestai -- 'It is finished' (19:30). [B] This is not a dying "
                    "gasp but a priestly declaration: the Greek tetelestai was used in commercial "
                    "contexts for 'paid in full' and in cultic contexts for the completion of a "
                    "sacrificial ritual. Jesus as the Melchizedekian high priest declares the sacrifice "
                    "complete. [A] The pierced side releasing blood and water (19:34) echoes Ezekiel's "
                    "temple vision (Ezek 47:1-12) where water flows from the temple to give life to "
                    "the Dead Sea, and Zechariah 13:1 where a fountain is opened for cleansing. [B] "
                    "Jesus IS the temple (2:19-21), and from his pierced body flows the water of life. "
                    "[C] The entire Passion in John is not defeat but enthronement -- the cross is the "
                    "throne from which the King of Kings reigns.",

        "key_verse": {
            "ref": "John 19:30",
            "text": "When Jesus had received the sour wine, he said, 'It is finished,' and he bowed his head and gave up his spirit.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tetelestai (it is finished/completed/accomplished -- 19:30; from teleo = to bring to "
            "an end/to complete/to fulfill; perfect tense indicating a completed action with ongoing "
            "results; used in commercial papyri for 'paid in full' and in sacrificial contexts for "
            "the completion of a ritual; Jesus' final word is a priestly declaration, not a victim's "
            "last gasp)",
            "ego eimi (I am he -- 18:5, 6, 8; the same divine name formula used in 8:58; in the "
            "garden it produces a theophanic effect -- the soldiers fall to the ground; the divine "
            "name retains its power even as the incarnate Word submits to arrest)",
            "ho basileus ton Ioudaion (the King of the Jews -- 18:33, 39; 19:3, 19, 21; the title "
            "used throughout the trial; Pilate inscribes it on the cross in Hebrew, Latin, and "
            "Greek -- a trilingual proclamation of kingship that Pilate intends as mockery but God "
            "intends as truth)",
            "aletheia (truth -- 18:37-38; Jesus says 'For this purpose I was born and for this "
            "purpose I have come into the world -- to bear witness to the truth'; Pilate's question "
            "'What is truth?' is the supreme irony of the Passion: truth stands incarnate before "
            "him and he cannot recognize it)",
            "haima kai hydor (blood and water -- 19:34; the pierced side releases both; blood = "
            "sacrificial atonement (Lev 17:11); water = cleansing and new life (Ezek 36:25-27, "
            "47:1-12); the temple of his body (2:19-21) pours forth life-giving streams)",
            "paredoken to pneuma (gave up his spirit -- 19:30; paradidomi = to hand over/deliver/ "
            "entrust; Jesus does not merely die -- he actively 'hands over' his spirit; even death "
            "is a sovereign act, not something done to him but something he does; cf. 10:18 'I lay "
            "it down of my own accord')"
        ],

        "ane_backdrop": "The trial and crucifixion of Jesus intersect with multiple ancient Near Eastern "
                        "patterns. The Roman practice of titulus (the written charge placed on the cross) "
                        "parallels the Mesopotamian practice of publicly displaying the charges against a "
                        "condemned person. The irony in John's account is that the titulus -- 'Jesus of "
                        "Nazareth, the King of the Jews' (19:19) -- is true in a sense Pilate never "
                        "intended. The trilingual inscription (Hebrew, Latin, Greek) functions as a "
                        "universal proclamation of kingship to every linguistic community in Jerusalem. "
                        "The water and blood from the pierced side resonates with ancient temple "
                        "traditions: in Mesopotamian temples, water rituals symbolized the life-giving "
                        "power of the gods; the temple at Jerusalem had water channels for sacrificial "
                        "blood and purification water. Ezekiel's vision of the eschatological temple "
                        "(Ezek 47:1-12) describes water flowing from the threshold of the temple, "
                        "growing into a river that heals everything it touches. Jesus identified his "
                        "body as the true temple (2:19-21), and the water flowing from his pierced side "
                        "fulfills Ezekiel's vision: the destroyed-and-raised temple now pours forth "
                        "living water.",

        "second_temple": [
            {
                "source": "Dead Sea Scrolls -- 11QMelchizedek (11Q13)",
                "summary": "This fragmentary text presents Melchizedek as an eschatological divine figure "
                           "who will execute judgment, proclaim liberty, and atone for the sins of the "
                           "sons of light. He is associated with Psalm 82:1 -- 'God (elohim) has taken "
                           "his place in the divine council.'",
                "relevance": "Jesus' priestly act on the cross -- declaring tetelestai as the completion "
                             "of atonement -- fulfills the Melchizedekian role. His priesthood is not "
                             "Levitical (wrong tribe -- Judah, not Levi, Heb 7:13-14) but after the "
                             "order of Melchizedek, the divine priest-king."
            },
            {
                "source": "Zechariah 12:10 and 13:1 (Second Temple interpretation)",
                "summary": "Zechariah prophesies: 'They will look on me, the one they have pierced, "
                           "and they will mourn for him' (12:10). And: 'On that day there shall be a "
                           "fountain opened for the house of David and the inhabitants of Jerusalem, "
                           "to cleanse them from sin and uncleanness' (13:1).",
                "relevance": "John explicitly cites Zechariah 12:10 in reference to the piercing of "
                             "Jesus' side (19:37). The fountain of Zechariah 13:1 is fulfilled in the "
                             "blood and water flowing from the pierced side -- the cleansing fountain "
                             "opened through the death of the pierced one."
            },
            {
                "source": "Isaiah 53:7-12 (Suffering Servant)",
                "summary": "The Servant is 'led like a lamb to the slaughter,' 'pierced for our "
                           "transgressions,' and 'numbered with the transgressors.' Yet through his "
                           "suffering, 'the will of the LORD shall prosper in his hand.'",
                "relevance": "John's Passion narrative fulfills Isaiah 53 at every point: the silence "
                             "before accusers (cf. 19:9 -- Jesus gives Pilate no answer), the voluntary "
                             "submission to death, the redemptive purpose of the suffering. The Lamb of "
                             "God first announced in 1:29 now completes his sacrificial work."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 12:46; Numbers 9:12", "note": "'Not one of his bones will be broken' (19:36) -- Jesus as the true Passover lamb whose bones remain unbroken, fulfilling the Passover regulation", "type": "ot"},
            {"ref": "Zechariah 12:10", "note": "'They will look on me, on him whom they have pierced' -- John 19:37 explicitly cites this prophecy at the piercing of Jesus' side", "type": "ot"},
            {"ref": "Ezekiel 47:1-12", "note": "Water flowing from the eschatological temple bringing life to the Dead Sea -- fulfilled in the water flowing from Jesus' pierced side, since his body IS the temple (2:19-21)", "type": "ot"},
            {"ref": "Isaiah 53:7-12", "note": "The Suffering Servant 'pierced for our transgressions' who is 'like a lamb led to the slaughter' -- the Passion fulfills the servant prophecy", "type": "ot"},
            {"ref": "Colossians 2:14-15", "note": "'He set aside the record of debt... nailing it to the cross. He disarmed the rulers and authorities and put them to open shame' -- the cross as cosmic victory over the powers", "type": "nt"},
            {"ref": "1 Peter 3:18-19", "note": "'He went and proclaimed (kerysso, herald's announcement, not euangelizo, gospel offer) to the spirits in prison' -- the victorious Christ announces his triumph to the imprisoned Watchers", "type": "nt"},
            {"ref": "Hebrews 9:11-14", "note": "'Through his own blood he entered once for all into the holy places' -- tetelestai as the completion of the Melchizedekian high priest's once-for-all sacrifice", "type": "nt"},
            {"ref": "Psalm 22:1, 14-18", "note": "The Passion psalm: 'they pierce my hands and my feet... they divide my garments among them' (fulfilled in 19:23-24) -- David's prophetic vision of the crucifixion", "type": "ot"},
            {"ref": "Zechariah 13:1", "note": "'On that day there shall be a fountain opened for the house of David... to cleanse them from sin' -- the blood and water from Jesus' side as the cleansing fountain", "type": "ot"}
        ],

        "divine_council_note": "The Passion narrative in John is the climax of the divine council's war "
                               "against the rebellious powers. The cross is not defeat -- it is the moment "
                               "when 'the ruler of this world' is 'cast out' (12:31). Colossians 2:14-15 "
                               "provides the divine council interpretation: on the cross, Christ 'disarmed "
                               "the rulers and authorities and put them to open shame, triumphing over them.' "
                               "The language is military and judicial: the hostile powers who have governed "
                               "the nations since Deuteronomy 32:8 are publicly humiliated. The ego eimi "
                               "in the garden (18:5-6) demonstrates that even at the moment of arrest, the "
                               "divine name retains its theophanic power -- the soldiers fall as before the "
                               "presence of YHWH. Pilate's question 'What is truth?' (18:38) is the ultimate "
                               "expression of the world-system's blindness: the archon tou kosmou has so "
                               "thoroughly deceived the nations (cf. Rev 12:9) that the Roman governor cannot "
                               "recognize Truth when it stands embodied before him. Tetelestai (19:30) is the "
                               "divine council's verdict executed: the sacrifice that defeats death, pays the "
                               "debt, and opens the way back into the divine presence is complete. The pierced "
                               "side releasing blood and water (19:34) is the new temple pouring forth life -- "
                               "Ezekiel's river that heals the Dead Sea (Ezek 47) now flows from the body of "
                               "Christ. The cross is simultaneously the altar of sacrifice (the Lamb of God), "
                               "the throne of enthronement (the King of the Jews), and the temple of God's "
                               "presence (the body from which living water flows). What the powers meant for "
                               "destruction, the divine council meant for the redemption of all creation.",

        "sections": [
            {
                "heading": "The Garden Arrest -- Ego Eimi as Theophany (18:1-14)",
                "body": "Jesus crosses the Kidron Valley to a garden (kepos, 18:1) -- John does not call "
                        "it Gethsemane, and he does not record the agony in prayer (the Synoptics cover "
                        "that). John's focus is the sovereignty of the arrest. Judas arrives with 'a band "
                        "of soldiers (speiran -- a Roman cohort, potentially 200-600 soldiers) and some "
                        "officers from the chief priests and the Pharisees' (18:3). The combined Roman and "
                        "Jewish force represents the totality of worldly power -- and it is about to fall "
                        "to the ground. Jesus steps forward: 'Whom do you seek?' They answer: 'Jesus of "
                        "Nazareth.' Jesus says: 'Ego eimi' (18:5). John records: 'When Jesus said to them, "
                        "\"Ego eimi,\" they drew back and fell to the ground' (18:6). This is a theophanic "
                        "reaction, not a fainting spell. The same ego eimi that claimed eternal self-existence "
                        "(8:58), that invoked the burning bush (Exod 3:14), that bears the divine name of "
                        "Isaiah 43:10 -- this Name, spoken by the incarnate Word, manifests its power in "
                        "the physical world. A Roman cohort trained for combat does not stumble backward "
                        "because a prisoner identifies himself. They fall because they have encountered the "
                        "divine presence. Yet Jesus does not use this power to escape. He asks again, 'Whom "
                        "do you seek?' and repeats, 'I told you that ego eimi. So, if you seek me, let "
                        "these men go' (18:8). John explains this as fulfilling Jesus' own word: 'Of those "
                        "whom you gave me I have lost not one' (18:9, cf. 17:12). Even in arrest, Jesus "
                        "is the Good Shepherd protecting his flock."
            },
            {
                "heading": "The Trial Before Pilate -- Truth Incarnate Before Blind Power (18:28-19:16)",
                "body": "John's trial narrative is the most dramatic and theologically layered of all four "
                        "Gospels. It is structured as a chiasm with Pilate moving back and forth between "
                        "Jesus (inside the Praetorium) and the Jewish leaders (outside, since entering a "
                        "Gentile building would defile them for Passover -- 18:28). The irony is devastating: "
                        "they avoid ritual defilement while demanding the death of the Lamb of God. Pilate "
                        "asks: 'Are you the King of the Jews?' (18:33). Jesus responds: 'My kingdom is not "
                        "of this world (ek tou kosmou toutou). If my kingdom were of this world, my servants "
                        "would have been fighting' (18:36). The phrase 'not of this world' does not mean "
                        "'not relevant to this world' but 'not derived from the world-system' -- Jesus' "
                        "kingdom has a heavenly origin, not an earthly power base. Pilate presses: 'So you "
                        "are a king?' Jesus answers: 'You say that I am a king. For this purpose I was born "
                        "and for this purpose I have come into the world -- to bear witness to the truth. "
                        "Everyone who is of the truth listens to my voice' (18:37). Pilate's response is "
                        "the most tragically ironic question in history: 'What is truth?' (Ti estin "
                        "aletheia? -- 18:38). He is standing face-to-face with the one who said 'I am... "
                        "the truth' (14:6), and he cannot see it. The world-system's blindness is total. "
                        "The Roman governor has the power of life and death, but he lacks the capacity to "
                        "recognize the Truth standing before him in chains."
            },
            {
                "heading": "Tetelestai -- The Priestly Declaration From the Cross (19:28-30)",
                "body": "The crucifixion scene in John is stripped to its theological essentials. Jesus "
                        "knows 'that all was now finished (tetelestai)' and says 'I thirst' (19:28) -- "
                        "to fulfill Psalm 69:21 ('for my thirst they gave me sour wine to drink'). After "
                        "receiving the sour wine, Jesus speaks his final word: 'Tetelestai' -- 'It is "
                        "finished' (19:30). This single word carries at least three dimensions of meaning. "
                        "First, commercial: tetelestai was written on receipts in the ancient world to mean "
                        "'paid in full.' The debt of sin is discharged completely -- there is nothing left "
                        "to pay, nothing remaining on the ledger. Second, cultic/priestly: the word was "
                        "used to describe the completion of a sacrificial ritual. Jesus is the Melchizedekian "
                        "high priest (not Levitical -- wrong tribe, Judah not Levi, Heb 7:13-14) who has "
                        "completed the once-for-all sacrifice (Heb 9:11-14). The Levitical system required "
                        "repeated sacrifices precisely because they were never 'finished' (Heb 10:1-4). "
                        "Jesus' sacrifice is tetelestai -- complete, final, unrepeatable. Third, prophetic: "
                        "every Old Testament type, shadow, and promise that pointed to the cross is now "
                        "fulfilled. The Passover lamb (Exod 12), the Day of Atonement (Lev 16), the brazen "
                        "serpent (Num 21:8-9, cf. John 3:14), the Suffering Servant (Isa 53), the pierced "
                        "one of Zechariah 12:10 -- all are tetelestai. Then John records: 'he bowed his "
                        "head and gave up (paredoken) his spirit' (19:30). The verb paradidomi ('to hand "
                        "over/deliver') is active, not passive: Jesus is not a victim whose life is taken "
                        "but a sovereign priest who hands over his spirit by his own authority (10:18)."
            },
            {
                "heading": "The Pierced Side -- Blood, Water, and the New Temple (19:31-42)",
                "body": "Because it is the day of Preparation and the bodies must not remain on the cross "
                        "during the Sabbath (a 'high day' -- the Sabbath of Passover week, 19:31), the "
                        "soldiers break the legs of the two criminals to hasten death. But when they come "
                        "to Jesus, they find him already dead and do not break his legs (19:33). Instead, "
                        "'one of the soldiers pierced his side with a spear, and at once there came out "
                        "blood and water' (19:34). John stresses the eyewitness reliability: 'He who saw "
                        "it has borne witness -- his testimony is true, and he knows that he is telling the "
                        "truth -- that you also may believe' (19:35). Why does John emphasize blood and "
                        "water so urgently? Because Jesus IS the temple (2:19-21), and from the pierced "
                        "temple flows the river of life. Ezekiel 47:1-12 describes water flowing from the "
                        "threshold of the eschatological temple, becoming a river that heals the Dead Sea "
                        "and produces trees whose leaves are 'for healing.' Zechariah 13:1 prophesies 'a "
                        "fountain opened for the house of David and the inhabitants of Jerusalem, to "
                        "cleanse them from sin and uncleanness.' The blood is the sacrificial blood of "
                        "atonement (Lev 17:11 -- 'the life of the flesh is in the blood, and I have given "
                        "it for you on the altar to make atonement for your souls'). The water is the "
                        "cleansing and life-giving stream of the new creation. Together they flow from "
                        "the pierced body-temple of Christ: atonement and new life, sacrifice and cleansing, "
                        "death and resurrection joined in a single act. John notes the unbroken bones "
                        "(19:36) fulfilling Exodus 12:46 and Numbers 9:12 -- the Passover lamb regulation. "
                        "And the piercing fulfills Zechariah 12:10 (19:37). The Lamb of God announced in "
                        "1:29 has completed his work. The temple destroyed and raised in three days (2:19) "
                        "now pours forth life for the world."
            }
        ]
    }
]
