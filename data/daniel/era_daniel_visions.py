"""
era_daniel_visions.py -- The Apocalyptic Visions (Daniel 7-12)

The second half of Daniel shifts from court tales to apocalyptic visions,
all narrated in the first person by Daniel himself. These six chapters
contain the most important divine council texts in the Hebrew Bible for
New Testament christology. Daniel 7's vision of the Ancient of Days
enthroned, with the divine council seated in judgment and "one like a son
of man" receiving everlasting dominion, provided Jesus with his primary
self-designation. Daniel 10 reveals the territorial spirit warfare behind
human history -- the Prince of Persia and the Prince of Greece as the
Deuteronomy 32:8 beings who govern empires from the unseen realm, opposed
by Michael, Israel's prince. Daniel 12 contains the clearest Old Testament
statement of bodily resurrection: "Many of those who sleep in the dust of
the earth shall awake, some to everlasting life, and some to shame and
everlasting contempt." These visions are the bridge between the Old
Testament and the New -- the theological framework within which Jesus
understood and proclaimed his own identity and mission.
"""

CHAPTERS = [
    {
        "id": "dan-7",
        "ref": "Daniel 7",
        "chapter_num": 1,
        "title": "The Four Beasts, the Ancient of Days, and the Son of Man",
        "era": "daniel_visions",
        "type": "chapter",
        "themes": ["DC", "KING", "SEED", "NATIONS", "DREAM"],

        "synopsis": "Daniel 7 is the pivotal chapter of the entire book and one of the most important "
                    "texts in the Bible for understanding Jesus' self-identification. The vision comes 'in "
                    "the first year of Belshazzar king of Babylon' (7:1) -- chronologically, this predates "
                    "the events of chapters 5-6. Daniel sees 'the four winds of heaven stirring up the "
                    "great sea (yamma rabba)' (7:2). From the chaos waters emerge four beasts: a lion with "
                    "eagle's wings (Babylon), a bear raised on one side (Medo-Persia), a leopard with four "
                    "wings and four heads (Greece under Alexander's four successors), and a terrifying "
                    "fourth beast with iron teeth and ten horns (Rome). From the ten horns emerges a "
                    "'little horn' with 'eyes like the eyes of a man, and a mouth speaking great things' "
                    "(7:8). Then the scene shifts to the heavenly throne room: 'As I looked, thrones "
                    "(karsavan) were placed, and the Ancient of Days (Attiq Yomin) took his seat; his "
                    "clothing was white as snow, and the hair of his head like pure wool; his throne was "
                    "fiery flames (shevivim di-nur); its wheels (galgilloh) were burning fire (nur "
                    "daliq). A stream of fire (nehar di-nur) issued and came out from before him; a "
                    "thousand thousands (aleph alphin) served him, and ten thousand times ten thousand "
                    "(ribbo rivvan) stood before him; the court (dina) sat in judgment, and the books "
                    "(siphrin) were opened' (7:9-10). This is the divine council in its fullest judicial "
                    "function. The 'thrones' (plural) are for council members who sit in judgment. The "
                    "fourth beast is destroyed, and then the climactic moment: 'I saw in the night "
                    "visions, and behold, with the clouds of heaven (im-ananei shemayya) there came one "
                    "like a son of man (kebar enash), and he came to the Ancient of Days and was presented "
                    "before him. And to him was given dominion (sholtan) and glory (yeqar) and a kingdom "
                    "(malku), that all peoples, nations, and languages should serve (yiphlchun) him; his "
                    "dominion is an everlasting dominion (sholtan alam), which shall not pass away, and "
                    "his kingdom one that shall not be destroyed' (7:13-14). The 'one like a son of man' "
                    "rides the clouds -- a divine prerogative throughout the Old Testament (Ps 68:4; "
                    "104:3; Isa 19:1) -- approaches the Ancient of Days as an equal, and receives "
                    "universal, eternal sovereignty. This is the 'second power in heaven' -- the divine "
                    "figure who shares YHWH's throne. Jesus chose 'Son of Man' as his primary "
                    "self-designation precisely because of this passage.",

        "key_verse": {
            "ref": "Daniel 7:13-14",
            "text": "I saw in the night visions, and behold, with the clouds of heaven there came one like a son of man, and he came to the Ancient of Days and was presented before him. And to him was given dominion and glory and a kingdom, that all peoples, nations, and languages should serve him; his dominion is an everlasting dominion, which shall not pass away, and his kingdom one that shall not be destroyed.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "Attiq Yomin (Ancient of Days -- the eternal God enthroned as cosmic judge; appears only in Daniel 7)",
            "kebar enash (one like a son of man -- the divine figure who receives dominion from the Ancient of Days)",
            "karsavan (thrones -- PLURAL, set up for the divine council members who sit in judgment)",
            "ananei shemayya (clouds of heaven -- the divine mode of transportation; a marker of deity in the OT)",
            "sholtan alam (everlasting dominion -- the eternal authority given to the Son of Man)",
            "dina yetiv (the court sat -- the divine council in judicial session)",
            "siphrin (books -- the records opened for the eschatological judgment)",
            "qaddishei Elyon (saints/holy ones of the Most High -- the council members who receive the kingdom)",
            "aleph alphin (thousand thousands -- the innumerable attendants of the divine throne)"
        ],

        "ane_backdrop": "The four beasts emerging from the sea draw on widespread ANE chaos mythology. "
                        "The 'great sea' (yamma rabba) is the primordial chaos waters -- the Mesopotamian "
                        "Tiamat, the Ugaritic Yamm -- from which hostile forces arise. In the Enuma Elish, "
                        "Marduk defeats Tiamat's monsters to establish cosmic order; in the Baal Cycle from "
                        "Ugarit, Baal defeats Yamm (Sea) and Mot (Death). Daniel's vision participates in "
                        "this tradition: empires are chaos beasts arising from the sea, and YHWH (the "
                        "Ancient of Days) subdues them from his throne. The composite nature of the beasts "
                        "(lion with wings, leopard with multiple heads) echoes the hybrid creatures of ANE "
                        "mythology. The throne scene draws on the divine council assembly traditions well "
                        "attested at Ugarit, where El presides over the assembly of the gods (phr ilm). "
                        "But Daniel's vision transcends its ANE background: the figure 'like a son of man' "
                        "who rides the clouds is not merely another deity in a pantheon but the unique "
                        "figure who receives universal dominion from the one true God.",

        "second_temple": [
            {
                "source": "1 Enoch 46:1-4; 48:2-6",
                "summary": "The Parables of Enoch describe 'the Son of Man' (or 'that Son of Man') who "
                           "sits on the throne of glory, judges the nations, and receives worship from "
                           "all peoples. His name was 'named before the Lord of Spirits' before creation.",
                "relevance": "The Enochic Son of Man tradition develops Daniel 7's figure into a "
                             "pre-existent, enthroned judge -- providing crucial background for Jesus' "
                             "use of the title."
            },
            {
                "source": "Mark 14:61-62",
                "summary": "The high priest asks: 'Are you the Christ, the Son of the Blessed?' Jesus "
                           "answers: 'I am, and you will see the Son of Man seated at the right hand "
                           "of Power, and coming with the clouds of heaven.'",
                "relevance": "Jesus combines Daniel 7:13 (clouds of heaven) with Psalm 110:1 (right hand "
                             "of Power) before the Sanhedrin -- the most explosive christological claim "
                             "possible. The high priest tears his robes because the divine council "
                             "implications were understood."
            },
            {
                "source": "Revelation 1:7, 13-14",
                "summary": "'Behold, he is coming with the clouds' (1:7). John sees 'one like a son of "
                           "man... the hair of his head was white like wool, like snow' (1:13-14).",
                "relevance": "Revelation merges the Ancient of Days imagery (white hair) with the Son of "
                             "Man figure -- identifying Christ as both the Ancient of Days and the Son of "
                             "Man, the two YHWH figures of Daniel 7."
            },
            {
                "source": "4 Ezra 13:1-13 (2 Esdras)",
                "summary": "A man rises from the sea and flies with the clouds of heaven; all who see "
                           "him tremble. He carves a mountain and stands on it, destroys his enemies "
                           "with fire from his mouth.",
                "relevance": "The Son of Man tradition from Daniel 7 is developed in late Second Temple "
                             "apocalyptic literature, confirming that the figure was understood as a "
                             "messianic, divine agent."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 68:4", "note": "'Rider of the clouds' (rokhev ba-aravot) -- the divine title for YHWH that the Son of Man shares by riding the clouds in 7:13", "type": "ot"},
            {"ref": "Psalm 110:1", "note": "'The LORD said to my Lord: Sit at my right hand' -- the two YHWH figures that Jesus combines with Daniel 7 at his trial", "type": "ot"},
            {"ref": "Mark 14:62", "note": "Jesus claims to be the Son of Man of Daniel 7 seated at the right hand of Power -- the claim that seals his death sentence", "type": "nt"},
            {"ref": "Matthew 26:64", "note": "'You will see the Son of Man seated at the right hand of Power and coming on the clouds of heaven'", "type": "nt"},
            {"ref": "Revelation 1:7, 13-14", "note": "Christ coming with clouds, hair white like wool -- merging the Ancient of Days and Son of Man into one figure", "type": "nt"},
            {"ref": "Revelation 5:11-12", "note": "'Myriads of myriads and thousands of thousands' worshiping the Lamb -- echoing the council attendance of 7:10", "type": "nt"},
            {"ref": "Psalm 82:1", "note": "'God has taken his place in the divine council' -- the same council setting as Daniel 7's judgment scene", "type": "ot"},
            {"ref": "1 Kings 22:19-23", "note": "Micaiah sees YHWH on his throne with the host of heaven -- another prophet's vision of the divine council in judgment", "type": "ot"},
            {"ref": "Acts 7:56", "note": "Stephen's vision: 'I see the heavens opened, and the Son of Man standing at the right hand of God'", "type": "nt"},
            {"ref": "Isaiah 6:1", "note": "'I saw the Lord sitting upon a throne, high and lifted up' -- the same throne-room vision as Daniel 7:9, with the same council members attending", "type": "ot"},
            {"ref": "Isaiah 24:21-23", "note": "'YHWH will punish the host of heaven... YHWH tseva'ot will reign on Mount Zion before his elders in glory' -- the cosmic judgment and enthronement that Daniel 7 dramatizes", "type": "ot"},
            {"ref": "Isaiah 52:13", "note": "'My servant shall be high (yarum) and lifted up (venissa) and exalted (vegavah me'od)' -- the Servant elevated to the same throne-position as Daniel 7:14's Son of Man", "type": "ot"},
            {"ref": "Ezekiel 1:26-28", "note": "The likeness of a human form on the sapphire throne -- the same 'one like a son of man' theology of a human-like divine figure", "type": "ot"},
            {"ref": "Philippians 2:9-11", "note": "'God has highly exalted him and bestowed on him the name that is above every name' -- the NT enthronement of Christ fulfilling Daniel 7:14", "type": "nt"},
            {"ref": "Hebrews 1:3-4", "note": "'He sat down at the right hand of the Majesty on high, having become as much superior to angels' -- the Son of Man/Son of God occupying the throne of Daniel 7", "type": "nt"}
        ],

        "divine_council_note": "Daniel 7 is THE pivotal divine council vision in the Hebrew Bible. Multiple "
                               "council elements converge: (1) Thrones (karsavan) are placed -- the plural "
                               "is critical. These thrones are for the divine council members who sit in "
                               "judgment alongside the Ancient of Days, the same 'thrones' Paul references "
                               "in Colossians 1:16 ('whether thrones or dominions'). (2) The Ancient of "
                               "Days (Attiq Yomin) presides -- YHWH as the eternal God, the head of the "
                               "council. His white hair, fiery throne, and burning wheels draw on the same "
                               "imagery as Ezekiel 1 and Isaiah 6. (3) Myriads of attendants serve and "
                               "stand -- the council in full assembly. (4) 'The court sat in judgment and "
                               "the books were opened' (7:10) -- the council's judicial function, executing "
                               "the verdict against the beast empires. (5) The 'one like a son of man' "
                               "(kebar enash) arrives on the clouds of heaven -- cloud-riding is a divine "
                               "prerogative throughout the OT (Psalm 68:4; 104:3; Isaiah 19:1; Nahum 1:3). "
                               "This figure approaches the Ancient of Days and receives universal, eternal "
                               "dominion. The Son of Man is the 'second power in heaven' -- the divine "
                               "council member who shares YHWH's authority. (6) The 'saints of the Most "
                               "High' (qaddishei Elyon, 7:18, 22, 27) who receive the kingdom are the "
                               "reconstituted council -- the holy ones of the Most High who will co-reign "
                               "with the Son of Man. The term qaddishei ('holy ones') is the standard "
                               "designation for divine council members throughout the OT (Deut 33:2-3; "
                               "Job 5:1; 15:15; Psalm 89:5, 7; Zech 14:5). Jesus chose 'Son of Man' as "
                               "his primary self-designation precisely because Daniel 7 identifies this "
                               "figure as divine (cloud-rider), authoritative (receives dominion from the "
                               "Ancient of Days), and eternal (his kingdom shall not be destroyed).",

        "sections": [
            {
                "heading": "The Four Beasts from the Chaos Sea (7:1-8)",
                "body": "'In the first year of Belshazzar' (7:1) -- chronologically before chapter 5. "
                        "Daniel dreams of 'the four winds of heaven (arba ruchei shemayya) stirring up "
                        "the great sea (yamma rabba)' (7:2). The 'great sea' is not the Mediterranean "
                        "but the primordial chaos waters -- the tehom of Genesis 1:2, the Tiamat of "
                        "Mesopotamian mythology. Empires emerge from chaos. Four beasts arise: the first "
                        "'like a lion (aryeh) and had eagles' wings (gappin di-neshar)' (7:4) -- Babylon, "
                        "whose symbol was the winged lion (seen on the Ishtar Gate). Its wings are plucked "
                        "and it is given a human mind -- possibly Nebuchadnezzar's humiliation and "
                        "restoration (chapter 4). The second beast 'like a bear (dov), raised up on one "
                        "side... with three ribs in its mouth' (7:5) -- Medo-Persia, with the 'one side' "
                        "indicating Persian dominance over Media, and the three ribs representing conquered "
                        "nations (Lydia, Babylon, Egypt). The third beast 'like a leopard (nemar), with "
                        "four wings (arba gappin) on its back... and four heads (arba'ah reshin)' (7:6) -- "
                        "Greece under Alexander (the four wings representing speed of conquest) divided "
                        "among four successors (the Diadochi). The fourth beast is 'terrifying and "
                        "dreadful and exceedingly strong (taqipha yatira). It had great iron teeth (shinnan "
                        "di-pharzel ravrevan); it devoured and broke in pieces and stamped what was left "
                        "with its feet' (7:7). It has ten horns, and from them a 'little horn' (qeren "
                        "ze'era) with 'eyes like the eyes of a man (aynan ke-aynei enasha) and a mouth "
                        "speaking great things (memallela ravrevan)' (7:8). The little horn speaks "
                        "arrogantly against the Most High (7:25) -- identified variously with Antiochus "
                        "IV Epiphanes, the Roman Empire, and the eschatological Antichrist."
            },
            {
                "heading": "The Ancient of Days: The Divine Council Enthroned in Judgment (7:9-12)",
                "body": "'As I looked (chazeh haveit), thrones (karsavan) were placed (remiv)' (7:9a). The "
                        "verb remiv means 'set up, established' -- the thrones are placed for a judicial "
                        "session. The plural 'thrones' is crucial: the Ancient of Days does not sit alone "
                        "but is surrounded by council members in their own seats of authority. 'And the "
                        "Ancient of Days (Attiq Yomin) took his seat (yetiv)' (7:9b). The title Attiq "
                        "Yomin appears only in Daniel 7 (verses 9, 13, 22) and designates YHWH as the "
                        "eternal one -- literally 'advanced in days,' meaning primordially ancient. His "
                        "appearance: 'his clothing (levusheh) was white as snow (ke-thelag chivvar), and "
                        "the hair of his head like pure wool (ke-amar neqi)' (7:9c). White signifies "
                        "purity, holiness, and glory. 'His throne was fiery flames (shevivim di-nur); "
                        "its wheels (galgilloh) were burning fire (nur daliq)' (7:9d). The fiery throne "
                        "and wheels recall Ezekiel's merkavah (throne chariot) vision (Ezek 1:15-28). "
                        "'A stream of fire (nehar di-nur) issued and came out from before him' (7:10a) -- "
                        "fire is the consistent element of theophany (Sinai, the burning bush, the pillar "
                        "of fire). 'A thousand thousands (aleph alphin) served him, and ten thousand "
                        "times ten thousand (ribbo rivvan) stood before him' (7:10b). The innumerable "
                        "hosts are the divine council in full assembly -- serving and attending the "
                        "enthroned King. 'The court (dina) sat in judgment (yetiv), and the books "
                        "(siphrin) were opened (petichun)' (7:10c). The 'books' are the records of "
                        "nations and empires -- the divine council maintains an audit of history. The "
                        "fourth beast is 'killed and its body destroyed and given over to be burned "
                        "with fire' (7:11). The other beasts have 'their dominion taken away, but their "
                        "lives were prolonged for a season and a time' (7:12)."
            },
            {
                "heading": "The Son of Man Receives Everlasting Dominion (7:13-14)",
                "body": "'I saw in the night visions (chevzei di-lelyah), and behold, with the clouds of "
                        "heaven (im-ananei shemayya) there came one like a son of man (kebar enash)' "
                        "(7:13a). The phrase 'clouds of heaven' is the decisive indicator of deity. "
                        "Throughout the Old Testament, cloud-riding is an exclusive divine prerogative: "
                        "YHWH 'rides on the clouds' (rokhev ba-aravot, Ps 68:4), 'makes the clouds his "
                        "chariot' (Ps 104:3), 'rides on a swift cloud' to judge Egypt (Isa 19:1), and "
                        "'his way is in whirlwind and storm, and the clouds are the dust of his feet' "
                        "(Nah 1:3). In the Ugaritic texts, the epithet 'Rider of the Clouds' (rkb 'rpt) "
                        "belongs exclusively to Baal -- a divine title. The figure 'like a son of man' "
                        "who rides the clouds is therefore a divine being. 'He came to the Ancient of "
                        "Days and was presented (haqribuh) before him' (7:13b). The verb haqribuh means "
                        "'they brought him near' or 'he was presented' -- the figure approaches the "
                        "Ancient of Days not in prostration but as an equal receiving a commission. "
                        "'And to him was given (yehiv leh) dominion (sholtan) and glory (yeqar) and a "
                        "kingdom (malku), that all peoples (kol-ammayya), nations (ummayya), and "
                        "languages (lishanayya) should serve him (yiphlchun leh)' (7:14a). The verb "
                        "pelach ('to serve, worship') is the same word used for serving deity throughout "
                        "Daniel (3:12, 14, 17, 28; 6:16, 20). Universal worship is rendered to the Son "
                        "of Man. 'His dominion is an everlasting dominion (sholtan alam) which shall not "
                        "pass away (la ye'deh), and his kingdom one that shall not be destroyed (la "
                        "titchabbel)' (7:14b). The kingdom is eternal and indestructible -- the same "
                        "qualities attributed to YHWH's kingdom in 2:44, 4:3, 4:34, and 6:26. When Jesus "
                        "stands before the Sanhedrin and claims to be the Son of Man 'coming on the clouds "
                        "of heaven' (Matt 26:64; Mark 14:62), he claims to be this divine figure."
            },
            {
                "heading": "The Saints of the Most High: The Reconstituted Council (7:15-28)",
                "body": "Daniel is troubled and asks 'one of those who stood there' (7:16) -- an attending "
                        "angel -- for the interpretation. The four beasts are four kingdoms (7:17). But "
                        "'the saints of the Most High (qaddishei Elyon) shall receive the kingdom and "
                        "possess the kingdom forever, forever and ever' (7:18). The term qaddishei Elyon "
                        "('holy ones of the Most High') is ambiguous and may refer to divine council "
                        "members, faithful human beings, or both. In the divine council framework (Heiser), "
                        "the qaddishim ('holy ones') are the standard designation for council members "
                        "(cf. Deut 33:2-3; Job 5:1; 15:15; Ps 89:5, 7; Zech 14:5). The 'saints of "
                        "the Most High' who receive the kingdom may therefore be the reconstituted divine "
                        "council -- the holy ones who will co-reign with the Son of Man in the restored "
                        "cosmic order. This interpretation is supported by Jesus' promise to the twelve: "
                        "'You who have followed me will also sit on twelve thrones, judging the twelve "
                        "tribes of Israel' (Matt 19:28). The little horn's war against the saints (7:21) "
                        "and the Ancient of Days' intervention (7:22) describe the eschatological conflict "
                        "between the forces arrayed against YHWH's people and the divine council's final "
                        "verdict. The little horn 'shall speak words against the Most High (Illaya), and "
                        "shall wear out (yevalei) the saints of the Most High, and shall think to change "
                        "the times (zimnin) and the law (dat)' (7:25). His dominion lasts 'a time, times, "
                        "and half a time' (iddan ve-iddanin u-felaq iddan) -- three and a half years, the "
                        "period of intense persecution that reappears in Revelation 11:2; 12:6, 14; 13:5. "
                        "'But the court (dina) shall sit in judgment, and his dominion shall be taken away "
                        "(7:26). The kingdom and the dominion and the greatness of the kingdoms under the "
                        "whole heaven shall be given to the people of the saints of the Most High (am "
                        "qaddishei Elyon)' (7:27). The eschatological reversal is complete: the beast "
                        "empires are destroyed, and the Son of Man's people receive eternal dominion."
            }
        ]
    },

    {
        "id": "dan-8",
        "ref": "Daniel 8",
        "chapter_num": 2,
        "title": "The Ram, the Goat, and the Host of Heaven Trampled",
        "era": "daniel_visions",
        "type": "chapter",
        "themes": ["DC", "NATIONS", "DREAM"],

        "synopsis": "Daniel 8 shifts from Aramaic back to Hebrew and presents a vision of two specific "
                    "empires: Medo-Persia and Greece. Daniel sees a ram (ayil) with two horns -- 'the "
                    "two horns are the kings of Media and Persia' (8:20) -- charging westward, northward, "
                    "and southward. No beast can stand before it. Then a male goat (tsephir izzim) comes "
                    "from the west 'across the face of the whole earth, without touching the ground' "
                    "(8:5) -- the speed of Alexander's conquests. The goat has a conspicuous horn between "
                    "its eyes (Alexander) that breaks the ram's two horns. But 'when he was strong, the "
                    "great horn was broken' (8:8) -- Alexander's death at thirty-two. In its place rise "
                    "four notable horns (the four Diadochi kingdoms). From one of them comes a 'little "
                    "horn' (qeren achat mitts'irah) that 'grew exceedingly great toward the south, toward "
                    "the east, and toward the glorious land (ha-tsevi)' (8:9). This little horn is "
                    "identified with Antiochus IV Epiphanes (175-164 BC), who 'grew great, even to the "
                    "host of heaven (tseva hashamayim). And some of the host and some of the stars it "
                    "threw down to the ground and trampled on them' (8:10). The 'host of heaven' and "
                    "'stars' are divine council language -- the little horn attacks the heavenly realm "
                    "itself. 'It became great, even as great as the Prince of the host (sar-hatsava)' "
                    "(8:11) -- the 'Prince of the host' is YHWH himself or his chief angelic agent. The "
                    "daily offering (tamid) is taken away and the sanctuary (miqdash) is overthrown. "
                    "Gabriel (Gavriel) is named for the first time in Scripture and interprets the vision: "
                    "the ram is Medo-Persia, the goat is Greece, and the little horn is 'a king of bold "
                    "face (az panim), one who understands riddles (mevin chidot)' -- Antiochus IV. He "
                    "'shall destroy mighty men and the people of the saints (am-qedoshim)' (8:24) and "
                    "'shall even rise up against the Prince of princes (sar-sarim)' (8:25). But 'he shall "
                    "be broken -- but by no human hand (be-ephes yad)' (8:25) -- the same supernatural "
                    "agency as the stone 'cut without hands' in chapter 2.",

        "key_verse": {
            "ref": "Daniel 8:10",
            "text": "It grew great, even to the host of heaven. And some of the host and some of the stars it threw down to the ground and trampled on them.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tseva hashamayim (host of heaven -- the angelic/divine council army; the 'stars' are council members)",
            "sar-hatsava (Prince of the host -- YHWH or his chief angel, the commander of the heavenly army)",
            "sar-sarim (Prince of princes -- the supreme Prince, YHWH himself)",
            "tamid (the continual offering -- the daily sacrifice in the Jerusalem temple that Antiochus abolished)",
            "Gavriel (Gabriel -- 'man/warrior of God'; the first named angel in the Hebrew Bible)",
            "az panim (bold/fierce of face -- the character of the oppressor king)",
            "ha-tsevi (the glorious land -- Israel, the beautiful land of YHWH's inheritance)",
            "be-ephes yad (without a human hand -- supernatural destruction, the same agency as 2:34)"
        ],

        "ane_backdrop": "The ram and the goat imagery draws on the zodiacal symbolism known in the ANE: "
                        "the ram was associated with Persia in astrological tradition, and the goat with "
                        "the western Mediterranean region. More importantly, the historical events of "
                        "Daniel 8 are precisely attested: Alexander the Great's campaigns against the "
                        "Persian Empire (334-323 BC), his sudden death (the 'great horn broken'), and "
                        "the division among the Diadochi (Ptolemy, Seleucus, Lysimachus, Cassander) are "
                        "well documented in Greek and Near Eastern sources. Antiochus IV Epiphanes' "
                        "desecration of the Jerusalem temple in 167 BC -- abolishing the daily sacrifice "
                        "and erecting an altar to Zeus Olympios on the altar of burnt offering (1 Macc "
                        "1:54) -- is the historical fulfillment of 8:11-12. The 2,300 evenings and "
                        "mornings (8:14) correspond roughly to the period from the desecration (167 BC) "
                        "to the rededication of the temple by Judas Maccabeus in 164 BC (the origin of "
                        "Hanukkah).",

        "second_temple": [
            {
                "source": "1 Maccabees 1:20-64",
                "summary": "The detailed historical account of Antiochus IV Epiphanes' desecration of "
                           "the Jerusalem temple: he 'entered arrogantly into the sanctuary,' took the "
                           "golden altar and lampstand, and set up 'a desolating sacrilege' on the altar.",
                "relevance": "1 Maccabees provides the historical fulfillment of Daniel 8:11-12 -- the "
                             "abolition of the daily offering and the desecration of the sanctuary."
            },
            {
                "source": "Luke 1:19, 26",
                "summary": "Gabriel appears to Zechariah ('I am Gabriel. I stand in the presence of "
                           "God') and to Mary to announce the births of John the Baptist and Jesus.",
                "relevance": "Gabriel, first named in Daniel 8:16 as the interpreter of apocalyptic "
                             "visions, appears in the New Testament as the announcer of the messianic "
                             "age that Daniel's visions anticipated."
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 2:34, 45", "note": "The stone 'cut without hands' -- the same supernatural agency as 'broken without a human hand' in 8:25", "type": "ot"},
            {"ref": "Revelation 12:4", "note": "The dragon's tail 'swept down a third of the stars of heaven and cast them to the earth' -- echoing 8:10's trampling of the host", "type": "nt"},
            {"ref": "Luke 1:19, 26", "note": "Gabriel appears in the New Testament as the angel of messianic announcement", "type": "nt"},
            {"ref": "1 Maccabees 1:54", "note": "The 'abomination of desolation' set up by Antiochus IV -- the historical event Daniel 8 prophesies", "type": "dss"},
            {"ref": "Matthew 24:15", "note": "Jesus cites the 'abomination of desolation spoken of by the prophet Daniel' as still future", "type": "nt"},
            {"ref": "Isaiah 14:12-14", "note": "Helel ben Shachar who tries to 'set my throne above the stars of God' -- the same cosmic rebellion as the little horn attacking the host of heaven", "type": "ot"}
        ],

        "divine_council_note": "Daniel 8 reveals that the little horn's persecution of God's people has a "
                               "cosmic dimension: he attacks the 'host of heaven' (tseva hashamayim) and "
                               "tramples 'stars' (kokhavim) -- both are divine council terminology. The "
                               "'stars' of heaven are identified with divine beings throughout the OT (Job "
                               "38:7 -- 'the morning stars sang together, and all the sons of God shouted "
                               "for joy'; Judges 5:20 -- 'From heaven the stars fought, from their courses "
                               "they fought against Sisera'; Isa 14:13 -- 'I will raise my throne above the "
                               "stars of God'). The little horn's assault on the host of heaven means "
                               "Antiochus attacks not only the earthly temple but the cosmic order itself. "
                               "The 'Prince of the host' (sar-hatsava, 8:11) and 'Prince of princes' "
                               "(sar-sarim, 8:25) designate either YHWH himself or the supreme angelic "
                               "commander (cf. Josh 5:14, where the 'commander of YHWH's army' appears to "
                               "Joshua). Gabriel's first appearance as an interpreter angel (8:16) "
                               "introduces a named council member into the narrative -- one who 'stands in "
                               "the presence of God' (Luke 1:19) and serves as the bridge between the "
                               "divine council's knowledge and the human prophet's understanding.",

        "sections": [
            {
                "heading": "The Ram and the Goat: Medo-Persia Falls to Greece (8:1-8)",
                "body": "The vision is set 'in the third year of the reign of King Belshazzar' (8:1) -- "
                        "about two years after the vision of chapter 7. Daniel sees himself at 'Susa the "
                        "capital (Shushan habirah), in the province of Elam' (8:2), by the Ulai canal "
                        "(uval Ulai). The ram (ayil) with two horns represents 'the kings of Media and "
                        "Persia' (8:20) -- the two horns are the two component peoples, with the higher "
                        "horn (Persia) coming up last. The ram charges 'westward and northward and "
                        "southward' (8:4) -- the directions of Persian expansion. Then the male goat "
                        "(tsephir ha-izzim) appears from the west, 'across the face of the whole earth, "
                        "without touching the ground (ein nogea ba-arets)' (8:5). The 'without touching "
                        "the ground' captures the legendary speed of Alexander's conquests -- from "
                        "Macedon to India in a decade. The 'conspicuous horn' (qeren chazut) between "
                        "the goat's eyes is 'the first king' (8:21) -- Alexander the Great. The goat "
                        "strikes the ram and shatters its two horns (8:7) -- Alexander's destruction of "
                        "the Persian Empire at Granicus (334 BC), Issus (333 BC), and Gaugamela (331 BC). "
                        "'When he was strong, the great horn was broken (nishberah)' (8:8) -- Alexander's "
                        "death at thirty-two in Babylon (323 BC). 'In place of it there came up four "
                        "conspicuous horns toward the four winds of heaven' (8:8b) -- the four Diadochi "
                        "kingdoms that emerged from the wars of succession."
            },
            {
                "heading": "The Little Horn and the Assault on Heaven (8:9-14)",
                "body": "From one of the four horns comes 'a little horn (qeren achat mitts'irah), which "
                        "grew exceedingly great toward the south, toward the east, and toward the "
                        "glorious land (ha-tsevi)' (8:9). This is Antiochus IV Epiphanes (175-164 BC), "
                        "the Seleucid king who launched a systematic campaign to Hellenize Judea. His "
                        "assault transcends the earthly: 'It grew great, even to the host of heaven "
                        "(tseva hashamayim). And some of the host and some of the stars (kokhavim) it "
                        "threw down to the ground and trampled (tirmesem) on them' (8:10). The trampling "
                        "of heavenly beings signifies cosmic rebellion -- Antiochus's persecution of "
                        "God's people is simultaneously an attack on the heavenly order. 'It became "
                        "great, even as great as the sar-hatsava (Prince of the host)' (8:11a). Antiochus "
                        "exalts himself to the level of YHWH's own commander. 'And the tamid (regular "
                        "offering) was taken away from him, and the place (makhon) of his sanctuary "
                        "(miqdash) was overthrown (hushlakh)' (8:11b). The abolition of the daily sacrifice "
                        "and the desecration of the temple -- historically fulfilled in 167 BC (1 Macc "
                        "1:45-50). Daniel asks: 'For how long?' The answer: 'For 2,300 evenings and "
                        "mornings (erev boqer). Then the sanctuary shall be restored to its rightful "
                        "state (venitsdaq qodesh)' (8:14). The 2,300 evenings and mornings (approximately "
                        "six years and four months, or 1,150 days if counting evening and morning "
                        "sacrifices separately) corresponds roughly to the period from the desecration to "
                        "the rededication under Judas Maccabeus."
            },
            {
                "heading": "Gabriel Interprets: The King of Bold Face (8:15-27)",
                "body": "'When I, Daniel, had seen the vision, I sought to understand it. And behold, "
                        "there stood before me one having the appearance of a man (kemar'eh gaver)' "
                        "(8:15). Then a voice: 'Gabriel (Gavriel), make this man understand the vision' "
                        "(8:16). This is the first time an angel is named in the canonical Hebrew Bible. "
                        "The name Gavriel means 'man/warrior of God' (gever + El). Gabriel will appear "
                        "again in 9:21 and in the New Testament (Luke 1:19, 26) as the angel of "
                        "revelatory communication. Daniel falls on his face, and Gabriel says: 'Understand, "
                        "O son of man (ben-adam), that the vision is for the time of the end (et-qets)' "
                        "(8:17). The address 'son of man' to Daniel is ordinary human terminology -- "
                        "contrasting with the divine 'Son of Man' of chapter 7. Gabriel's interpretation: "
                        "'At the latter end of their kingdom, when the transgressors (posh'im) have "
                        "reached their limit (kehatem), a king of bold face (az panim), one who understands "
                        "riddles (mevin chidot), shall arise' (8:23). This king 'shall destroy wonderfully "
                        "(yashchit niphla'ot) and shall prosper and do as he will. He shall destroy mighty "
                        "men (atsu'mim) and the people of the saints (am-qedoshim)' (8:24). His arrogance "
                        "reaches its zenith: 'He shall even rise up against the sar-sarim (Prince of "
                        "princes)' (8:25a). But the verdict: 'he shall be broken (yishaver) -- but by "
                        "no human hand (be-ephes yad)' (8:25b). Antiochus died in 164 BC of a disease "
                        "during a campaign in Persia -- broken not by military force but by what the "
                        "text presents as divine intervention."
            }
        ]
    },

    {
        "id": "dan-9",
        "ref": "Daniel 9",
        "chapter_num": 3,
        "title": "Daniel's Prayer and the Seventy Weeks",
        "era": "daniel_visions",
        "type": "chapter",
        "themes": ["COV", "SEED", "BLOOD", "HOLY"],

        "synopsis": "Daniel 9 opens with Daniel studying the prophets: 'I, Daniel, perceived in the "
                    "books (basepharim) the number of years that, according to the word of YHWH to "
                    "Jeremiah the prophet, must pass before the end of the desolations of Jerusalem, "
                    "namely, seventy years' (9:2; cf. Jer 25:11-12; 29:10). Daniel responds with one of "
                    "the most powerful intercessory prayers in Scripture: 'O Lord (Adonai), the great and "
                    "awesome God (ha-El hagadol vehanora), who keeps covenant (berit) and steadfast love "
                    "(chesed) with those who love him and keep his commandments, we have sinned (chatanu) "
                    "and done wrong (he'evinu) and acted wickedly (hirsha'nu) and rebelled (maranu)' "
                    "(9:4-5). The prayer is thoroughly Deuteronomic -- confessing the national sin that "
                    "caused the exile. While Daniel is praying, Gabriel appears again: 'the man Gabriel "
                    "(ha-ish Gavriel), whom I had seen in the vision at the first, came to me in swift "
                    "flight (bi-y'aph mu'aph) at the time of the evening offering (minchat-erev)' "
                    "(9:21). Gabriel brings the most detailed chronological prophecy in the Old Testament: "
                    "'Seventy weeks (shavu'im shiv'im) are decreed about your people and your holy city, "
                    "to finish the transgression (pesha), to put an end to sin (chattat), to atone for "
                    "iniquity (avon), to bring in everlasting righteousness (tsedek olamim), to seal "
                    "both vision and prophet, and to anoint a most holy place (qodesh qodashim)' (9:24). "
                    "The seventy 'weeks' (literally 'sevens') are widely interpreted as 490 years, divided "
                    "into three periods: seven weeks (49 years), sixty-two weeks (434 years), and one "
                    "final week (7 years). The prophecy includes an 'anointed one' (mashiach) who will be "
                    "'cut off' (yikkaret) -- a messianic figure who dies. 'And the people of the prince "
                    "who is to come shall destroy the city and the sanctuary' (9:26) -- fulfilled in the "
                    "Roman destruction of Jerusalem in 70 AD. 'And on the wing of abominations shall come "
                    "one who makes desolate (meshomem)' (9:27) -- the 'abomination of desolation' that "
                    "Jesus cites in his Olivet Discourse (Matt 24:15).",

        "key_verse": {
            "ref": "Daniel 9:24",
            "text": "Seventy weeks are decreed about your people and your holy city, to finish the transgression, to put an end to sin, and to atone for iniquity, to bring in everlasting righteousness, to seal both vision and prophet, and to anoint a most holy place.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "shavu'im shiv'im (seventy weeks/sevens -- the 490-year prophetic timeline)",
            "mashiach nagid (anointed one, a prince -- the messianic ruler; mashiach is the root of 'Messiah')",
            "yikkaret (shall be cut off -- the death of the anointed one; karat means to cut, kill, or make a covenant)",
            "ve-ein lo (and shall have nothing -- the anointed one is cut off without receiving what is his)",
            "shiqqutsim meshomem (abomination of desolation -- the desecrating sacrilege; quoted by Jesus in Matt 24:15)",
            "chesed (steadfast love/covenant loyalty -- Daniel's appeal to YHWH's covenant character)",
            "qodesh qodashim (most holy place/most holy one -- either the temple or the Messiah himself anointed)"
        ],

        "ane_backdrop": "The seventy-year exile prophecy (Jer 25:11-12; 29:10) that Daniel studies has "
                        "a background in Mesopotamian seventy-year periods: Marduk was said to have "
                        "decreed seventy years of desolation for Babylon (reflected in the Esarhaddon "
                        "inscription). The concept of divine time periods governing history -- specific "
                        "numbers of years decreed for specific purposes -- is well attested in ANE "
                        "apocalyptic thinking. The Akkadian concept of simtu ('decreed fate') describes "
                        "the gods' council determining the duration of kingdoms and the fate of nations. "
                        "Gabriel's reinterpretation of Jeremiah's seventy years as seventy 'weeks' (490 "
                        "years) follows the interpretive principle of expanding numerical prophecies -- "
                        "a practice also seen in the Qumran pesher literature. The intercessory prayer of "
                        "Daniel 9:4-19 follows the structure of ANE penitential prayers (dingir.sha.dib.ba "
                        "in Sumerian), where the suppliant confesses sins and appeals to divine mercy.",

        "second_temple": [
            {
                "source": "11QMelchizedek (11Q13)",
                "summary": "This Qumran text interprets Daniel 9's seventy weeks in conjunction with "
                           "the Jubilee cycle. The tenth Jubilee (490 years) culminates in Melchizedek's "
                           "eschatological judgment and liberation of the captives.",
                "relevance": "The Dead Sea Scrolls community read Daniel 9 as an eschatological timeline "
                             "linked to the Jubilee system, with a heavenly deliverer (Melchizedek) as "
                             "the agent of the final liberation."
            },
            {
                "source": "Matthew 24:15",
                "summary": "Jesus warns: 'So when you see the abomination of desolation spoken of by "
                           "the prophet Daniel, standing in the holy place (let the reader understand)...'",
                "relevance": "Jesus treats Daniel 9's prophecy of the 'abomination of desolation' as "
                             "still future, beyond Antiochus IV's desecration -- pointing to the Roman "
                             "destruction of 70 AD and/or an eschatological fulfillment."
            },
            {
                "source": "Luke 19:41-44",
                "summary": "Jesus weeps over Jerusalem: 'They will not leave one stone upon another in "
                           "you, because you did not know the time of your visitation.'",
                "relevance": "Jesus' lament over Jerusalem's destruction echoes Daniel 9:26 ('the people "
                             "of the prince who is to come shall destroy the city and the sanctuary') and "
                             "implies that Jerusalem missed its prophetic 'visitation.'"
            }
        ],

        "cross_refs": [
            {"ref": "Jeremiah 25:11-12; 29:10", "note": "The seventy-year exile prophecy that Daniel studies and that Gabriel reinterprets as seventy 'weeks'", "type": "ot"},
            {"ref": "Matthew 24:15", "note": "Jesus cites Daniel's 'abomination of desolation' as a sign of the end", "type": "nt"},
            {"ref": "Mark 13:14", "note": "'When you see the abomination of desolation standing where it ought not to be' -- Jesus' Olivet Discourse", "type": "nt"},
            {"ref": "Luke 19:41-44", "note": "Jesus weeps over Jerusalem's coming destruction -- fulfilling 9:26", "type": "nt"},
            {"ref": "Isaiah 53:8", "note": "'He was cut off from the land of the living' -- the Servant who is 'cut off,' the same verb as the mashiach in 9:26", "type": "ot"},
            {"ref": "Leviticus 25:8-10", "note": "The Jubilee system (7 x 7 years + 1) that provides the background for the seventy 'sevens'", "type": "ot"},
            {"ref": "2 Thessalonians 2:3-4", "note": "Paul's 'man of lawlessness' who 'takes his seat in the temple of God' -- developing Daniel 9:27's abomination imagery", "type": "nt"}
        ],

        "divine_council_note": "Gabriel's mission to Daniel in chapter 9 reveals the divine council "
                               "operating as the source of prophetic chronology. Gabriel states that he "
                               "came to give Daniel 'insight and understanding' (9:22) -- the council "
                               "member bridges the gap between divine knowledge and human comprehension. "
                               "The seventy-weeks prophecy itself is a divine decree: 'Seventy weeks are "
                               "decreed (nechtakh) about your people' (9:24). The verb nechtakh means 'cut, "
                               "determined, decreed' -- the council has issued a ruling about the timeline "
                               "of redemption. The six purposes of the seventy weeks (9:24) -- finish "
                               "transgression, end sin, atone for iniquity, bring everlasting righteousness, "
                               "seal vision and prophet, anoint the most holy -- are a comprehensive "
                               "summary of the divine council's redemptive plan. The 'anointed one who is "
                               "cut off' (9:26) directly connects to the Suffering Servant of Isaiah 53:8 "
                               "('he was cut off from the land of the living'). The mashiach who dies is "
                               "the council's agent of atonement -- the same figure who bears the sin of "
                               "the many (Isa 53:11-12) and whose death accomplishes the purposes listed "
                               "in 9:24.",

        "sections": [
            {
                "heading": "Daniel's Prayer of Confession and Intercession (9:1-19)",
                "body": "'In the first year of Darius the son of Ahasuerus, by descent a Mede, who was "
                        "made king over the realm of the Chaldeans' (9:1). Daniel is studying the "
                        "prophecies: 'I, Daniel, perceived in the books (basepharim) the number of years' "
                        "(9:2) -- he is reading Jeremiah's prophecy of seventy years of exile (Jer 25:11-12; "
                        "29:10). His response is not passive waiting but active intercession: 'I turned "
                        "my face (panai) to the Lord God (ha-Adonai ha-Elohim), seeking him by prayer "
                        "(tefillah) and pleas for mercy (tachanun), with fasting and sackcloth and ashes' "
                        "(9:3). The prayer that follows (9:4-19) is a model of covenantal intercession. "
                        "It opens with YHWH's covenant character: 'O Lord, the great and awesome God "
                        "(ha-El hagadol vehanora), who keeps covenant (berit) and steadfast love (chesed)' "
                        "(9:4). The confession is comprehensive: 'We have sinned (chatanu) and done wrong "
                        "(he'evinu) and acted wickedly (hirsha'nu) and rebelled (maranu), turning aside "
                        "from your commandments and rules' (9:5). Five verbs of sin, covering every "
                        "category. Daniel identifies with the nation -- 'we,' not 'they.' The prayer "
                        "appeals to YHWH's reputation: 'O Lord, according to all your righteous acts "
                        "(tsidqotekha), let your anger and your wrath turn away from your city Jerusalem, "
                        "your holy mountain... for your own sake (lema'ankha), O Lord, because your city "
                        "and your people are called by your name (shimkha)' (9:16, 19). The appeal is "
                        "not based on Israel's merit but on YHWH's name and character."
            },
            {
                "heading": "Gabriel's Revelation: The Seventy Weeks (9:20-27)",
                "body": "'While I was speaking and praying and confessing my sin and the sin of my people "
                        "Israel... the man Gabriel (ha-ish Gavriel), whom I had seen in the vision at "
                        "the first, came to me in swift flight (bi-y'aph mu'aph) at the time of the "
                        "evening offering (minchat erev)' (9:20-21). Gabriel's arrival 'at the time of "
                        "the evening offering' connects the revelation to the temple liturgy -- even "
                        "though the temple lies in ruins, the prayer calendar continues. Gabriel says: "
                        "'At the beginning of your pleas for mercy (tachanun) a word (davar) went out, "
                        "and I have come to tell it to you, for you are greatly loved (chamudot)' (9:23). "
                        "The 'word' that goes out is a divine council decree -- the moment Daniel begins "
                        "praying, the council issues its response. The seventy-weeks prophecy: 'Seventy "
                        "weeks (shavu'im shiv'im) are decreed (nechtakh) about your people' (9:24). The "
                        "six purposes are paired: finish transgression / end sin (dealing with sin); atone "
                        "for iniquity / bring everlasting righteousness (dealing with reconciliation); "
                        "seal vision and prophet / anoint a most holy (dealing with consummation). The "
                        "timeline: 'from the going out of the word (davar) to restore and build Jerusalem "
                        "to the coming of an anointed one, a prince (mashiach nagid), there shall be seven "
                        "weeks' (9:25). Then: 'for sixty-two weeks... the anointed one (mashiach) shall "
                        "be cut off (yikkaret) and shall have nothing (ve-ein lo)' (9:26a). The verb "
                        "karat ('to cut off') can mean death or covenant-cutting -- here the context "
                        "demands death: the mashiach is killed and receives nothing ('shall have nothing'). "
                        "'The people of the prince (nagid) who is to come shall destroy the city and the "
                        "sanctuary' (9:26b) -- fulfilled in Titus's destruction of Jerusalem in 70 AD."
            }
        ]
    },

    {
        "id": "dan-10-12",
        "ref": "Daniel 10-12",
        "chapter_num": 4,
        "title": "The Spiritual War Behind History: Territorial Spirits, Michael, and the Resurrection",
        "era": "daniel_visions",
        "type": "chapter",
        "themes": ["DC", "NATIONS", "DREAM", "SPIRIT", "GLORY"],

        "synopsis": "Daniel 10-12 contains the most explicit revelation of territorial spirit warfare in "
                    "all of Scripture. In the third year of Cyrus (10:1), Daniel receives a vision after "
                    "three weeks of mourning and fasting. An angelic being appears -- 'a man clothed in "
                    "linen (bad), whose body was like beryl (tarshish), his face like the appearance of "
                    "lightning (baraq), his eyes like flaming torches (lappidei esh), his arms and legs "
                    "like the gleam of burnished bronze (nechoshet qalal), and the sound of his words "
                    "like the sound of a multitude (qol hamon)' (10:5-6). Daniel alone sees the vision; "
                    "his companions flee in terror. The angelic figure explains his delay: 'The prince "
                    "(sar) of the kingdom of Persia withstood me twenty-one days, but Michael (Mikha'el), "
                    "one of the chief princes (ahadei hasarim harishonim), came to help me, for I was "
                    "left there with the kings of Persia' (10:13). He adds: 'Do you know why I have come "
                    "to you? But now I will return to fight against the prince of Persia (sar Paras); and "
                    "when I go out, behold, the prince of Greece (sar Yavan) will come... There is none "
                    "who contends by my side against these except Michael, your prince (sarkhem)' "
                    "(10:20-21). This is the Deuteronomy 32:8-9 worldview in full operation: the nations "
                    "have been allotted to divine beings who govern them from the spiritual realm. The "
                    "'princes' (sarim) of Persia and Greece are not human rulers but territorial spirits "
                    "-- divine council members who were allotted governance over these empires. Michael is "
                    "Israel's prince -- the angelic patron of YHWH's own people. Chapter 11 provides "
                    "detailed prophecy of the conflicts between the Ptolemaic ('king of the South') and "
                    "Seleucid ('king of the North') dynasties, culminating in the 'abomination of "
                    "desolation' (11:31) set up by Antiochus IV. Chapter 12 brings the eschatological "
                    "climax: 'At that time shall arise Michael (Mikha'el), the great prince (hasar "
                    "hagadol) who has charge of your people. And there shall be a time of trouble "
                    "(tsarah), such as never has been since there was a nation till that time. But at "
                    "that time your people shall be delivered (yimalet), everyone whose name shall be "
                    "found written in the book (katov bassepher)' (12:1). Then the clearest Old "
                    "Testament statement of bodily resurrection: 'And many of those who sleep "
                    "(miyyeshenei) in the dust of the earth (admat-aphar) shall awake (yaqitsu), some "
                    "to everlasting life (chayyei olam), and some to shame (charaphah) and everlasting "
                    "contempt (dir'on olam)' (12:2). 'And those who are wise (hamaskilim) shall shine "
                    "(yazhiru) like the brightness (kezohar) of the expanse (raqia), and those who turn "
                    "many to righteousness (matsdiqei harabbim), like the stars (kakkokhavim) forever and "
                    "ever' (12:3). The wise who 'shine like stars' may echo the 'stars of God' language "
                    "for divine council members (Job 38:7; Isa 14:13), suggesting that the resurrected "
                    "righteous are elevated to a status comparable to the heavenly host.",

        "key_verse": {
            "ref": "Daniel 12:2-3",
            "text": "And many of those who sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt. And those who are wise shall shine like the brightness of the sky above; and those who turn many to righteousness, like the stars forever and ever.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "sar (prince -- a territorial spirit, a divine being assigned to govern a nation or empire)",
            "sar Paras (Prince of Persia -- the divine being governing the Persian Empire from the unseen realm)",
            "sar Yavan (Prince of Greece -- the divine being behind the Greek Empire)",
            "Mikha'el (Michael -- 'who is like God?'; Israel's chief angelic prince and defender)",
            "ahadei hasarim harishonim (one of the chief princes -- Michael's rank among the council's leaders)",
            "chayyei olam (everlasting life -- the eternal existence of the resurrected righteous)",
            "dir'on olam (everlasting contempt -- the same rare word as Isaiah 66:24's dera'on)",
            "hamaskilim (the wise -- those who understand God's purposes and lead others to righteousness)",
            "raqia (expanse/firmament -- the sky-dome of Genesis 1:6-8; the wise shine with its brightness)"
        ],

        "ane_backdrop": "The concept of divine beings governing nations is deeply rooted in the ANE. "
                        "Every major ancient culture believed its patron deity or deities governed its "
                        "affairs: Marduk ruled Babylon, Ashur ruled Assyria, Chemosh ruled Moab, and "
                        "so on. The difference in biblical theology is that these 'gods of the nations' "
                        "are not independent deities but subordinate members of YHWH's council, allotted "
                        "to the nations at Babel (Deut 32:8-9 LXX/DSS: 'he fixed the borders of the "
                        "peoples according to the number of the sons of God'). Daniel 10 uniquely "
                        "reveals the ongoing conflict between these territorial spirits. The detailed "
                        "prophecy of chapter 11 corresponds with remarkable precision to the known "
                        "history of the Ptolemaic-Seleucid conflicts (the 'Wars of the Diadochi' and "
                        "the 'Syrian Wars' of the 3rd-2nd centuries BC). The concept of bodily "
                        "resurrection (12:2) develops from earlier hints in the OT (Job 19:25-27; Isa "
                        "26:19; Ezek 37) into the most explicit statement in the Hebrew Bible, providing "
                        "the foundation for the Pharisaic belief in resurrection that Jesus affirmed.",

        "second_temple": [
            {
                "source": "Ephesians 6:12",
                "summary": "'For we do not wrestle against flesh and blood, but against the rulers, "
                           "against the authorities, against the cosmic powers over this present darkness, "
                           "against the spiritual forces of evil in the heavenly places.'",
                "relevance": "Paul's description of spiritual warfare directly develops Daniel 10's "
                             "revelation of territorial spirits. The 'rulers' and 'authorities' are the "
                             "New Testament equivalent of the 'princes' of Persia and Greece."
            },
            {
                "source": "Revelation 12:7-9",
                "summary": "'Now war arose in heaven, Michael and his angels fighting against the dragon... "
                           "And the great dragon was thrown down.'",
                "relevance": "Revelation's war in heaven between Michael and the dragon continues the "
                             "cosmic warfare motif of Daniel 10-12, with Michael fighting the same kind of "
                             "spiritual battle against the ultimate adversary."
            },
            {
                "source": "Jude 9",
                "summary": "'But when the archangel Michael, contending with the devil, disputed about "
                           "the body of Moses, he did not presume to pronounce a blasphemous judgment, "
                           "but said, The Lord rebuke you.'",
                "relevance": "Jude identifies Michael as 'the archangel' (archistrategos), confirming his "
                             "status as the chief prince of the divine council's military hierarchy."
            },
            {
                "source": "John 5:28-29",
                "summary": "'An hour is coming when all who are in the tombs will hear his voice and "
                           "come out, those who have done good to the resurrection of life, and those "
                           "who have done evil to the resurrection of judgment.'",
                "relevance": "Jesus' teaching on the resurrection directly echoes Daniel 12:2 -- the "
                             "two-fold resurrection to life and to judgment."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9", "note": "'He fixed the borders of the peoples according to the number of the sons of God' (DSS/LXX) -- the allotment that creates the territorial spirits of Daniel 10", "type": "ot"},
            {"ref": "Ephesians 6:12", "note": "Paul's 'rulers and authorities in the heavenly places' -- the NT development of Daniel 10's territorial spirits", "type": "nt"},
            {"ref": "Revelation 12:7-9", "note": "Michael and his angels fighting the dragon -- continuing Daniel's cosmic warfare", "type": "nt"},
            {"ref": "Jude 9", "note": "Michael the archangel contending with the devil -- Michael's ongoing role as YHWH's chief warrior", "type": "nt"},
            {"ref": "John 5:28-29", "note": "Jesus' teaching on the two-fold resurrection echoing Daniel 12:2", "type": "nt"},
            {"ref": "Matthew 13:43", "note": "'The righteous will shine like the sun in the kingdom of their Father' -- echoing Daniel 12:3", "type": "nt"},
            {"ref": "Isaiah 26:19", "note": "'Your dead shall live; their bodies shall rise' -- an earlier hint of the resurrection Daniel 12:2 makes explicit", "type": "ot"},
            {"ref": "Isaiah 66:24", "note": "'Their worm shall not die' -- the same rare word dir'on/dera'on ('contempt') as Daniel 12:2", "type": "ot"},
            {"ref": "Job 38:7", "note": "'When the morning stars sang together, and all the sons of God shouted for joy' -- the 'stars' as divine council members, echoing Daniel 12:3", "type": "ot"},
            {"ref": "Luke 20:36", "note": "'They are equal to angels (isangeloi)' -- the resurrected righteous elevated to angelic status, fulfilling Daniel 12:3", "type": "nt"},
            {"ref": "Isaiah 34:4", "note": "'All the host of heaven shall rot away' -- the territorial spirits of Daniel 10 face dissolution in Isaiah 34's cosmic judgment", "type": "ot"},
            {"ref": "Isaiah 24:21-22", "note": "'YHWH will punish the host of heaven in heaven, and the kings of the earth on the earth' -- the same dual-realm judgment as Daniel 10's spiritual and earthly warfare", "type": "ot"},
            {"ref": "Psalm 82:6-7", "note": "'You shall die like men and fall like any prince' -- the verdict on the divine council members who govern the nations, fulfilled in Daniel 10-12's cosmic battles", "type": "ot"},
            {"ref": "Colossians 2:15", "note": "'He disarmed the rulers and authorities and put them to open shame' -- Christ's cross as the decisive defeat of Daniel 10's territorial spirits", "type": "nt"},
            {"ref": "1 Corinthians 15:24-26", "note": "'Then comes the end, when he delivers the kingdom to God the Father after destroying every rule and every authority and power' -- the final dismantling of the territorial-spirit system Daniel 10 reveals", "type": "nt"}
        ],

        "divine_council_note": "Daniel 10-12 provides the clearest biblical window into how the divine "
                               "council operates in real-time history. The territorial spirit warfare -- "
                               "the Prince of Persia blocking Gabriel for 21 days, Michael intervening, "
                               "the Prince of Greece waiting in the wings -- reveals that human geopolitics "
                               "is the surface manifestation of invisible cosmic conflict. The 'princes' "
                               "(sarim) of Persia and Greece are the Deuteronomy 32:8-9 beings -- the sons "
                               "of God allotted to govern the nations after Babel. They are not mere "
                               "messengers but powerful beings who can resist a major angel (possibly "
                               "Gabriel) for three weeks. Michael is identified as 'one of the chief "
                               "princes' (10:13) and 'your prince' (10:21; 12:1) -- Israel's angelic "
                               "patron who fights on behalf of YHWH's people. The designation 'chief "
                               "princes' (hasarim harishonim) implies a hierarchy within the council -- "
                               "Michael is among the highest-ranking members. Daniel 12:1-3 brings the "
                               "divine council narrative to its eschatological climax: Michael rises for "
                               "the final battle, the dead are resurrected, and the wise 'shine like the "
                               "stars forever and ever' (12:3). The 'stars' (kokhavim) in divine council "
                               "theology are divine beings (Job 38:7; Judg 5:20). The promise that the "
                               "resurrected righteous will shine 'like the stars' suggests that they are "
                               "elevated to a status comparable to the heavenly host -- a concept Jesus "
                               "develops in Luke 20:36 ('they are equal to angels') and that Paul develops "
                               "in 1 Corinthians 15:40-42 ('the glory of the stars'). The human story and "
                               "the divine council story converge in the resurrection: the faithful become "
                               "part of the reconstituted council, shining forever in YHWH's presence.",

        "sections": [
            {
                "heading": "The Angelic Vision and the Prince of Persia (Daniel 10)",
                "body": "'In the third year of Cyrus king of Persia' (10:1) -- approximately 536 BC, "
                        "after the decree allowing the Jews to return. Daniel mourns for three full weeks "
                        "(10:2-3). Then the vision: 'I lifted up my eyes and looked, and behold, a man "
                        "(ish echad) clothed in linen (bad), with a belt of fine gold (ketem Uphaz) "
                        "around his waist' (10:5). The description -- body like beryl, face like "
                        "lightning, eyes like flaming torches, arms and legs like burnished bronze, voice "
                        "like the sound of a multitude (10:6) -- closely parallels the description of "
                        "the risen Christ in Revelation 1:13-16. Daniel alone sees the vision; his "
                        "companions are struck with terror and flee (10:7). Daniel falls into a deep "
                        "sleep, face to the ground. A hand touches him and the angel speaks: 'Do not "
                        "fear, Daniel, for from the first day that you set your heart (libbekha) to "
                        "understand and to humble yourself before your God, your words have been heard, "
                        "and I have come because of your words (devarekha)' (10:12). The angel's coming "
                        "is a direct response to Daniel's prayer -- but: 'The prince (sar) of the "
                        "kingdom of Persia withstood me (omed lenegdi) twenty-one days (esrim ve-echad "
                        "yom)' (10:13a). A divine being assigned to govern Persia blocked the angel for "
                        "three weeks. 'But Michael (Mikha'el), one of the chief princes (ahadei hasarim "
                        "harishonim), came to help me (la'azreni)' (10:13b). Michael is named as "
                        "Israel's champion and a top-ranking council member. The angel continues: 'Now "
                        "I will return to fight (lehillachem) against the prince of Persia (sar Paras); "
                        "and when I go out, behold, the prince of Greece (sar Yavan) will come' "
                        "(10:20). As one territorial spirit's influence wanes (Persia), another's rises "
                        "(Greece) -- the divine council's governance of empires operates through these "
                        "spiritual rulers."
            },
            {
                "heading": "The Kings of the North and South (Daniel 11)",
                "body": "Chapter 11 provides the most detailed prophetic narrative in the Old Testament, "
                        "tracing the conflicts between the Ptolemaic dynasty of Egypt ('the king of the "
                        "South,' melekh hanegev) and the Seleucid dynasty of Syria ('the king of the "
                        "North,' melekh hatsaphon) with extraordinary precision. 'A mighty king (melekh "
                        "gibbor) shall arise, who shall rule with great dominion' (11:3) -- Alexander the "
                        "Great. 'His kingdom shall be broken and divided toward the four winds of heaven' "
                        "(11:4) -- the Diadochi. The narrative traces the Syrian Wars between the "
                        "Ptolemies and Seleucids through the 3rd and 2nd centuries BC, culminating in "
                        "Antiochus IV Epiphanes: 'Forces from him shall appear and profane the temple and "
                        "fortress, and shall take away the regular burnt offering (tamid). And they shall "
                        "set up the abomination that makes desolate (shiqqutz shomem)' (11:31). This is "
                        "the historical desecration of the Jerusalem temple in 167 BC, when Antiochus "
                        "erected an altar to Zeus Olympios on the altar of burnt offering and sacrificed "
                        "swine (1 Macc 1:54; 2 Macc 6:2). 'The people who know their God shall stand "
                        "firm (yachazqu) and take action (asu)' (11:32b) -- the Maccabean resistance. "
                        "'And the wise among the people (maskilei am) shall make many understand, yet "
                        "for some days they shall stumble by sword and flame, by captivity and plunder' "
                        "(11:33). The maskilim ('the wise') endure martyrdom -- the same group who will "
                        "'shine like the stars' in 12:3. The prophecy's scope extends beyond Antiochus "
                        "to an eschatological figure (11:36-45) who 'shall exalt himself and magnify "
                        "himself above every god' (11:36) -- a passage Paul develops into the 'man of "
                        "lawlessness' in 2 Thessalonians 2:3-4."
            },
            {
                "heading": "Michael Rises, the Dead Awake, the Wise Shine Like Stars (Daniel 12)",
                "body": "'At that time (ba-et hahi) shall arise (ya'amod) Michael (Mikha'el), the great "
                        "prince (hasar hagadol) who has charge (ha-omed) of your people' (12:1a). "
                        "Michael -- whose name means 'Who is like God?' -- rises for the ultimate "
                        "confrontation. 'And there shall be a time of trouble (et tsarah), such as never "
                        "has been (lo nihyetah) since there was a nation till that time' (12:1b). Jesus "
                        "quotes this in Matthew 24:21 ('great tribulation, such as has not been from the "
                        "beginning of the world until now'). 'But at that time your people shall be "
                        "delivered (yimalet), everyone whose name shall be found written in the book "
                        "(katov bassepher)' (12:1c). The 'book' is the heavenly register -- the divine "
                        "council's record of the faithful (cf. Exod 32:32; Ps 69:28; Rev 20:12). Then "
                        "the resurrection: 'And many of those who sleep (miyyeshenei) in the dust of the "
                        "earth (admat-aphar) shall awake (yaqitsu), some to everlasting life (chayyei "
                        "olam), and some to shame (charaphah) and everlasting contempt (dir'on olam)' "
                        "(12:2). The 'dust of the earth' (admat-aphar) echoes Genesis 3:19 ('you are "
                        "dust, and to dust you shall return') -- the resurrection reverses the curse. "
                        "The two destinies -- everlasting life and everlasting contempt -- establish the "
                        "double outcome of the final judgment. The rare word dir'on ('abhorrence, "
                        "contempt') appears only here and in Isaiah 66:24, linking Daniel's resurrection "
                        "to Isaiah's final judgment. 'And those who are wise (hamaskilim) shall shine "
                        "(yazhiru) like the brightness (kezohar) of the firmament (raqia), and those who "
                        "turn many to righteousness (matsdiqei harabbim), like the stars (kakkokhavim) "
                        "forever and ever (le-olam va'ed)' (12:3). The maskilim who endured persecution "
                        "in 11:33 are now glorified. Their brightness is compared to the raqia ('expanse/ "
                        "firmament') of Genesis 1:6-8 and to the kokhavim ('stars') -- the same 'stars' "
                        "that represent divine council members in Job 38:7. The resurrection is not "
                        "merely survival but glorification -- the faithful become luminous like the "
                        "heavenly host. Daniel is told: 'But you, go your way (lekh leqets) till the "
                        "end. And you shall rest (tanuach) and shall stand (ta'amod) in your allotted "
                        "place (goralekha) at the end of the days' (12:13). Daniel will die ('rest'), "
                        "be resurrected ('stand'), and receive his inheritance ('allotted place') at "
                        "the end -- the personal assurance of resurrection that seals the entire book."
            }
        ]
    }
]
