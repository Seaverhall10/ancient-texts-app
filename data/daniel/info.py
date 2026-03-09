"""
info.py — Daniel: Scholarly Text Introduction

This file provides the "front page" for Daniel in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Daniel is the divine council book par excellence for eschatological prophecy.
The vision of Daniel 7 — where the Ancient of Days takes his seat on a
fiery throne, the court of the divine council sits in judgment, and "one
like a son of man" approaches on the clouds of heaven to receive an
everlasting kingdom — is the single most important background text for
understanding Jesus' self-designation as "the Son of Man." Daniel 10
provides the most explicit revelation of territorial spirits in scripture:
the "Prince of Persia" and the "Prince of Greece" are divine beings who
govern empires, opposed by Michael, "your prince." No other book in the
Old Testament so directly reveals the architecture of the unseen realm.
"""

TEXT_INFO = {
    "text_id": "daniel",
    "display_name": "Daniel",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim) or Major Prophets",
        "detail": "Daniel's canonical placement differs between traditions. In the Hebrew Bible, "
                  "Daniel is placed among the Writings (Ketuvim), not the Prophets — possibly because "
                  "Daniel was a court sage rather than a classical prophet, or possibly due to the "
                  "late date of the book's acceptance into the canon. In the Septuagint and Christian "
                  "Old Testament, Daniel is placed among the Major Prophets, after Ezekiel. The book "
                  "is universally canonical in Jewish, Catholic, Orthodox, and Protestant traditions, "
                  "though the Catholic and Orthodox canons include additional material (the Prayer of "
                  "Azariah, the Song of the Three Young Men, Susanna, and Bel and the Dragon) that "
                  "Protestants classify as apocryphal. Daniel is extensively quoted in the New Testament: "
                  "Jesus' favorite self-designation 'Son of Man' derives from Daniel 7:13-14; his "
                  "Olivet Discourse references the 'abomination of desolation' (Matt 24:15; Mark "
                  "13:14; cf. Dan 9:27; 11:31; 12:11); and Revelation draws extensively on Daniel's "
                  "imagery (the four beasts, the Ancient of Days, the ten horns, the time periods). "
                  "Jesus specifically names Daniel as 'the prophet' (Matt 24:15), affirming both the "
                  "book's prophetic status and its association with Daniel."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Daniel, a Jewish nobleman deported to Babylon in 605 BC (Dan 1:1-6), who served "
                       "in the courts of Nebuchadnezzar, Belshazzar, Darius the Mede, and Cyrus of "
                       "Persia. The book is written partly in the first person (chapters 7-12), and "
                       "Daniel is commanded to 'seal up the book until the time of the end' (12:4). "
                       "Josephus (Antiquities 11.337) records that Alexander the Great was shown the "
                       "prophecies of Daniel when he entered Jerusalem (~332 BC), implying the book "
                       "was known and authoritative by that date. Ezekiel, Daniel's contemporary, "
                       "references a 'Daniel' renowned for wisdom and righteousness (Ezek 14:14, 20; "
                       "28:3), though some scholars identify this with a different legendary figure "
                       "(Dan'el of Ugaritic tradition). Jesus refers to 'Daniel the prophet' (Matt "
                       "24:15), affirming traditional authorship.",

        "scholarly_debate": "Critical scholarship almost universally dates Daniel's final form to the "
                           "Maccabean period (~167-164 BC), arguing that: (1) the detailed 'prophecies' "
                           "of chapters 10-11 describe the Seleucid-Ptolemaic conflicts and Antiochus "
                           "IV Epiphanes with such precision that they must be written after the events "
                           "(vaticinium ex eventu — 'prophecy after the event'); (2) the book's "
                           "apocalyptic genre flourished in the 2nd century BC; (3) the Hebrew and "
                           "Aramaic of Daniel contain Persian loanwords and possibly Greek loanwords "
                           "(the musical instruments in 3:5) suggesting a late date; (4) Daniel's "
                           "placement in the Writings rather than the Prophets may indicate it was not "
                           "yet written when the prophetic canon was closed. Conservative scholars "
                           "(Gleason Archer, Tremper Longman, Andrew Steinmann) defend 6th-century "
                           "authorship, arguing: (1) predictive prophecy is a genuine prophetic "
                           "phenomenon; (2) the Aramaic of Daniel fits the Imperial Aramaic of the "
                           "6th-5th century BC better than the 2nd century; (3) the Persian and possibly "
                           "Greek loanwords are consistent with the cosmopolitan culture of the "
                           "Neo-Babylonian and Persian empires; (4) Qumran manuscripts of Daniel "
                           "(1QDan^a, 4QDan^a-e) dating to ~125-50 BC require insufficient time for "
                           "a Maccabean composition to achieve canonical authority.",

        "bottom_line": "Whether Daniel wrote in the 6th century BC or the book achieved its final "
                       "form in the 2nd century BC, the divine council theology is not affected by "
                       "the dating question. The vision of the Ancient of Days and the Son of Man "
                       "(chapter 7), the territorial spirits (chapter 10), and the eschatological "
                       "framework (chapters 9, 12) reveal the architecture of the unseen realm "
                       "regardless of when they were written down. The book's theological authority "
                       "is attested by Jesus' own use of its categories — particularly the 'Son of "
                       "Man' title, which he chose as his primary self-designation."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events span ~605-536 BC (from the first deportation to the third year "
                       "of Cyrus). Daniel wrote or dictated the book during the Babylonian and early "
                       "Persian periods, with the visions of chapters 7-12 dating to ~553-536 BC.",
        "critical_range": "The court tales (chapters 1-6) may contain older traditions from the "
                         "Babylonian/Persian period. The visions (chapters 7-12) are typically dated "
                         "to ~167-164 BC, during the Maccabean crisis when Antiochus IV Epiphanes "
                         "desecrated the Temple. The book's final form is dated to ~164 BC, just before "
                         "or during the Maccabean revolt.",
        "evidence": "Key evidence includes: (1) Dead Sea Scrolls: Eight manuscripts of Daniel have "
                    "been found at Qumran (1QDan^a, 1QDan^b, 4QDan^a-e, pap6QDan), dating to "
                    "~125-50 BC. The earliest (4QDan^c) may date to ~125 BC, providing very little "
                    "time between a proposed Maccabean composition (~164 BC) and the production of "
                    "multiple copies at Qumran. (2) The Hebrew-Aramaic bilingualism (1:1-2:4a and "
                    "8:1-12:13 in Hebrew; 2:4b-7:28 in Aramaic) is unusual and debated — it may "
                    "reflect different sources, different audiences, or a deliberate literary "
                    "structure. (3) The Aramaic of Daniel is Imperial Aramaic, consistent with the "
                    "6th-5th century BC linguistic milieu but also explainable as a conservative "
                    "literary register. (4) The detailed accuracy of the four-kingdom scheme "
                    "(Babylon -> Media/Persia -> Greece -> Rome/Seleucids) has been debated: "
                    "traditionalists see genuine prediction; critical scholars see reflection on "
                    "known history. (5) Daniel's absence from the 'praise of the fathers' in "
                    "Sirach 44-50 (~180 BC) is sometimes cited as evidence the book was not yet "
                    "widely known, though arguments from silence are precarious."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "If 6th century: the Jewish exilic community in Babylon, needing "
                            "encouragement that YHWH remained sovereign over the empires that had "
                            "conquered them. If 2nd century: the Jewish community under Seleucid "
                            "persecution (Antiochus IV Epiphanes, who desecrated the Temple in "
                            "167 BC), needing assurance that God's kingdom would triumph over the "
                            "kingdoms of the world. In either case, the audience is a persecuted "
                            "community facing imperial power that claims divine authority and "
                            "demands worship of false gods.",

        "purpose": "Daniel has a dual purpose: (1) The court tales (chapters 1-6) demonstrate that "
                   "faithful Jews can survive and thrive in a pagan empire without compromising their "
                   "covenant loyalty — YHWH protects those who refuse to worship idols (the fiery "
                   "furnace, the lions' den) and humbles arrogant kings who claim divine status "
                   "(Nebuchadnezzar's madness, Belshazzar's feast). (2) The visions (chapters 7-12) "
                   "reveal that human empires rise and fall according to YHWH's sovereign plan, "
                   "that spiritual powers stand behind earthly kingdoms, and that YHWH's kingdom "
                   "will ultimately replace all human governments: 'the God of heaven will set up a "
                   "kingdom that shall never be destroyed' (2:44).",

        "theological_intent": "Daniel's theological contribution is unique in the Old Testament: it "
                             "provides the most systematic revelation of the relationship between "
                             "earthly empires and their spiritual patrons. The four kingdoms (chapters "
                             "2, 7) are not merely political entities but spiritual systems, each "
                             "represented by a beast that rises from the sea (the chaos waters, the "
                             "realm of hostile spiritual forces). The 'saints of the Most High' who "
                             "receive the kingdom (7:18, 22, 27) may be the divine council members "
                             "(the holy ones), the faithful human community, or both — the earthly "
                             "and heavenly communities united in YHWH's eschatological kingdom. The "
                             "70 weeks prophecy (9:24-27) provides the chronological framework for "
                             "messianic expectation that directly influenced first-century Judaism's "
                             "anticipation of the Messiah."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew and Biblical Aramaic (bilingual composition)",
        "script": "Aramaic square script (the standard script by the exilic/post-exilic period)",
        "linguistic_notes": "Daniel is unique in the Hebrew Bible for its extensive use of two languages: "
                           "Hebrew (1:1-2:4a and 8:1-12:13) and Aramaic (2:4b-7:28). The transition at "
                           "2:4 is dramatically marked: 'Then the Chaldeans said to the king in Aramaic' "
                           "— and the text itself shifts to Aramaic, remaining in that language through "
                           "chapter 7. The Aramaic is classified as Imperial Aramaic, the administrative "
                           "language of the Neo-Babylonian and Persian empires. Persian loanwords (e.g., "
                           "raz for 'mystery,' pithgam for 'decree,' satraps) are consistent with the "
                           "Persian imperial context. The Greek loanwords in the musical instruments list "
                           "(3:5 — qithros/kitharis, pesanterin/psalterion, sumponiah/symphonia) have "
                           "been debated: they may indicate Greek cultural influence that reached "
                           "Mesopotamia before Alexander, or they may indicate a later date. The Hebrew "
                           "sections of Daniel contain both early and late features, making linguistic "
                           "dating inconclusive. The apocalyptic vocabulary of the visions — 'Ancient of "
                           "Days' (attiq yomin), 'Son of Man' (bar enash), 'the holy ones of the Most "
                           "High' (qaddishei elyon) — creates a distinctive theological lexicon that "
                           "profoundly influenced Second Temple Judaism and the New Testament.",
        "grammar_match": "The prose style differs between the court tales (chapters 1-6), which use "
                        "standard narrative prose (both Hebrew and Aramaic), and the visions (chapters "
                        "7-12), which use apocalyptic visionary language with symbolic imagery, angelic "
                        "interpretation, and chronological calculations. The court tales are told in "
                        "the third person; the visions are largely first-person accounts by Daniel. "
                        "The bilingual structure creates a chiastic literary pattern in chapters 2-7: "
                        "A (chapter 2, four kingdoms), B (chapter 3, faithfulness under persecution), "
                        "C (chapter 4, God humbles Nebuchadnezzar), C' (chapter 5, God judges "
                        "Belshazzar), B' (chapter 6, faithfulness under persecution), A' (chapter 7, "
                        "four kingdoms). This chiasm suggests deliberate literary design."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Daniel IS scripture — the eschatological vision that provides the framework for "
                   "New Testament christology, particularly through the Son of Man and the kingdom of God.",
        "nt_usage": "Daniel's influence on the New Testament is immense. Jesus' primary self-designation "
                    "'Son of Man' (used over 80 times in the Gospels) derives from Daniel 7:13-14 — a "
                    "divine figure who receives authority from the Ancient of Days. Jesus explicitly cites "
                    "Daniel before the Sanhedrin: 'You will see the Son of Man seated at the right hand "
                    "of Power, and coming on the clouds of heaven' (Matt 26:64; Mark 14:62; cf. Dan "
                    "7:13-14). The 'abomination of desolation' (Dan 9:27; 11:31; 12:11) is cited in the "
                    "Olivet Discourse (Matt 24:15; Mark 13:14). The kingdom of God theme throughout the "
                    "Gospels draws on Daniel 2:44 and 7:14, 27. Revelation is saturated with Daniel: "
                    "the four beasts (Rev 13; cf. Dan 7), the Ancient of Days imagery (Rev 1:14; cf. "
                    "Dan 7:9), the ten horns (Rev 17:12; cf. Dan 7:7), the 'time, times, and half a "
                    "time' (Rev 12:14; cf. Dan 7:25; 12:7), the books opened for judgment (Rev 20:12; "
                    "cf. Dan 7:10), and the kingdom given to the saints (Rev 5:10; cf. Dan 7:27). "
                    "Paul's 'man of lawlessness' (2 Thess 2:3-4) draws on Daniel's little horn who "
                    "speaks 'great things' and opposes the Most High (Dan 7:8, 25; 11:36-37).",
        "internal_consistency": "Daniel connects to the broader Old Testament in multiple ways. The "
                               "four-kingdom scheme (chapters 2, 7) provides the geopolitical framework "
                               "that contextualizes the intertestamental period. The 70 weeks (9:24-27) "
                               "reinterpret Jeremiah's 70 years of exile (Jer 25:11-12; 29:10). The "
                               "territorial spirits (chapter 10) operationalize the Deuteronomy 32:8-9 "
                               "worldview. The Son of Man figure (7:13-14) develops the divine council "
                               "enthronement theology of Psalms 2, 89, and 110. The resurrection (12:2-3) "
                               "is the clearest statement of bodily resurrection in the Old Testament."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls: Eight manuscripts of Daniel have been identified at Qumran "
                    "(1QDan^a, 1QDan^b, 4QDan^a-e, pap6QDan), dating to ~125-50 BC. These are "
                    "among the most important DSS manuscripts because they establish the book's "
                    "existence and canonical authority by the mid-2nd century BC.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew-Aramaic text. The MT of Daniel is generally well-preserved. "
                     "The bilingual structure (Hebrew and Aramaic) is maintained consistently across "
                     "all Hebrew manuscripts."},
            {"name": "Septuagint (LXX / Old Greek)", "date": "2nd century BC",
             "note": "The Old Greek translation of Daniel differs significantly from the MT, "
                     "particularly in chapters 4-6 where the LXX appears to reflect a different "
                     "Vorlage or interpretive tradition. The OG was largely replaced in Christian "
                     "use by Theodotion's translation."},
            {"name": "Theodotion's Daniel", "date": "~2nd century AD (but possibly based on an "
                     "older revision)",
             "note": "Theodotion's revision of Daniel became the standard Greek text in Christian "
                     "churches, supplanting the Old Greek. It is closer to the MT and includes the "
                     "additions (Susanna, Bel and the Dragon, Prayer of Azariah). New Testament "
                     "quotations of Daniel generally align more closely with Theodotion than the OG, "
                     "suggesting a 'proto-Theodotion' text existed in the 1st century."},
            {"name": "Dead Sea Scrolls", "date": "~125-50 BC",
             "note": "Eight manuscripts provide the earliest witnesses to Daniel's text. 4QDan^a "
                     "preserves the transition from Hebrew to Aramaic at 2:4, confirming the "
                     "bilingual structure was original. The fragments generally align with the "
                     "proto-MT tradition."},
            {"name": "Peshitta (Syriac)", "date": "2nd-3rd century AD",
             "note": "The Syriac translation follows the MT closely and does not include the "
                     "Greek additions."}
        ],
        "reliability": "The text of Daniel is well-attested across multiple traditions. The most "
                       "significant textual issue is the divergence between the Old Greek and the MT "
                       "in chapters 4-6, which represents either a different textual tradition or "
                       "a different editorial stage. The theologically crucial passages — the Son of "
                       "Man vision (chapter 7), the 70 weeks (chapter 9), the territorial spirits "
                       "(chapter 10), and the resurrection (12:2-3) — are stable across all witnesses."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "The narrative setting is the Babylonian and early Persian periods (~605-536 BC). "
                   "Daniel is deported as a youth in Nebuchadnezzar's first campaign against Jerusalem "
                   "(605 BC) and serves in the Babylonian and Persian courts through the reigns of "
                   "Nebuchadnezzar (~605-562 BC), Belshazzar (regent ~553-539 BC), Darius the Mede "
                   "(a debated figure, possibly Gubaru/Gobryas, the governor Cyrus appointed over "
                   "Babylon, or a conflation), and Cyrus of Persia (539-530 BC). If the final form "
                   "dates to the Maccabean period, the contemporary setting is the persecution under "
                   "Antiochus IV Epiphanes (~167-164 BC), who desecrated the Jerusalem Temple, "
                   "banned Jewish religious practices, and erected an altar to Zeus Olympios in the "
                   "Temple (the 'abomination of desolation').",

        "geography": "The primary setting is Babylon — the capital of the Neo-Babylonian Empire, "
                     "located on the Euphrates River in modern Iraq. Daniel's visions are set at "
                     "various locations: the royal court of Babylon (chapters 1-5), the Ulai canal "
                     "near Susa (8:2, a major city of the Persian Empire, in modern Iran), and the "
                     "bank of the Tigris River (10:4). The visions encompass world geography: the "
                     "four kingdoms span from Babylon to Persia to Greece to Rome/the Seleucid "
                     "Empire. The 'beautiful land' (11:16, 41) is Israel.",

        "historical_connections": "The fall of Babylon to Cyrus in 539 BC (Daniel 5) is confirmed by "
                                 "the Nabonidus Chronicle and the Cyrus Cylinder. Belshazzar's existence "
                                 "as regent (his father Nabonidus was the actual king) was confirmed by "
                                 "the Nabonidus Cylinder and the 'Verse Account of Nabonidus' — before "
                                 "these discoveries, critics had cited Belshazzar as a historical error. "
                                 "The Seleucid-Ptolemaic conflicts described in Daniel 11 match the known "
                                 "history of these dynasties with remarkable precision. Antiochus IV "
                                 "Epiphanes' desecration of the Temple in 167 BC is described in 1 Maccabees "
                                 "1:54 and confirmed by archaeological evidence. The rededication of the "
                                 "Temple (Hanukkah, 164 BC) may correspond to Daniel's chronological "
                                 "calculations."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Daniel contains the most explicit and detailed divine council scenes in the Old "
                   "Testament outside of Job. Three passages are of supreme importance: the Ancient "
                   "of Days and the Son of Man (chapter 7), the territorial spirits (chapter 10), "
                   "and the eschatological judgment (chapters 7, 12)."
                   "\n\n"
                   "THE ANCIENT OF DAYS AND THE SON OF MAN (Daniel 7:9-14): 'As I looked, thrones "
                   "were placed, and the Ancient of Days took his seat; his clothing was white as "
                   "snow, and the hair of his head like pure wool; his throne was fiery flames; its "
                   "wheels were burning fire. A stream of fire issued and came out from before him; "
                   "a thousand thousands served him, and ten thousand times ten thousand stood before "
                   "him; the court sat in judgment, and the books were opened' (7:9-10). This is the "
                   "divine council in its fullest judicial function: the Ancient of Days (YHWH) is "
                   "enthroned, the heavenly court is seated (the 'thrones' — plural — are for the "
                   "council members), myriads of attendants serve, and the books of judgment are "
                   "opened. Then: 'I saw in the night visions, and behold, with the clouds of heaven "
                   "there came one like a son of man, and he came to the Ancient of Days and was "
                   "presented before him. And to him was given dominion and glory and a kingdom, that "
                   "all peoples, nations, and languages should serve him; his dominion is an "
                   "everlasting dominion, which shall not pass away' (7:13-14). The 'one like a son "
                   "of man' (bar enash) is a divine figure — he rides the clouds (a divine prerogative "
                   "throughout the Old Testament: Psalm 68:4; 104:3; Isa 19:1; Nah 1:3), approaches "
                   "the Ancient of Days as an equal (not prostrating but 'presented'), and receives "
                   "universal, eternal dominion. This is the 'second power in heaven' — the divine "
                   "council member who shares YHWH's authority. Jesus chose 'Son of Man' as his "
                   "primary self-designation precisely because of this passage: it identified him as "
                   "the divine figure of Daniel 7 who receives the kingdom from the Ancient of Days."
                   "\n\n"
                   "TERRITORIAL SPIRITS — THE PRINCES OF PERSIA AND GREECE (Daniel 10:13-21): "
                   "Daniel receives a vision after three weeks of mourning and fasting. An angelic "
                   "being (possibly Gabriel, cf. 9:21) appears and explains his delay: 'The prince "
                   "(sar) of the kingdom of Persia withstood me twenty-one days, but Michael, one "
                   "of the chief princes, came to help me, for I was left there with the kings of "
                   "Persia' (10:13). He adds: 'I will return to fight against the prince of Persia; "
                   "and when I go out, behold, the prince of Greece will come... There is none who "
                   "contends by my side against these except Michael, your prince' (10:20-21). This "
                   "passage is the most explicit revelation of territorial spirits in scripture. The "
                   "'princes' (sarim) of Persia and Greece are not human rulers — they are divine "
                   "beings who govern empires from the spiritual realm. Michael is Israel's 'prince' — "
                   "the angelic patron assigned to YHWH's people. This is the Deuteronomy 32:8-9 "
                   "worldview in full operation: the nations were allotted to the sons of God, and "
                   "these divine rulers continue to shape geopolitics from the unseen realm. The "
                   "angelic warfare between Michael and the prince of Persia reveals that earthly "
                   "political events have spiritual causes — a principle Paul develops in Ephesians "
                   "6:12 ('we do not wrestle against flesh and blood, but against the rulers, against "
                   "the authorities, against the cosmic powers over this present darkness')."
                   "\n\n"
                   "THE 70 WEEKS AND THE ABOMINATION (Daniel 9:24-27): Gabriel reveals to Daniel "
                   "a chronological framework: '70 weeks are decreed about your people and your holy "
                   "city, to finish the transgression, to put an end to sin, and to atone for "
                   "iniquity, to bring in everlasting righteousness, to seal both vision and prophet, "
                   "and to anoint a most holy place' (9:24). The 70 'weeks' (literally 'sevens') are "
                   "widely interpreted as 70 x 7 = 490 years. The prophecy includes an 'anointed one' "
                   "(mashiakh) who will be 'cut off' (9:26) — a messianic figure who dies — and a "
                   "'prince who is to come' who will destroy the city and the sanctuary (9:26) and "
                   "set up 'the abomination that makes desolate' (9:27). Jesus identifies the "
                   "'abomination of desolation' (Matt 24:15) as a still-future event, and the early "
                   "church saw its partial fulfillment in the destruction of Jerusalem in 70 AD."
                   "\n\n"
                   "RESURRECTION AND ESCHATOLOGICAL JUDGMENT (Daniel 12:1-3): 'At that time Michael, "
                   "the great prince who has charge of your people, shall arise. And there shall be "
                   "a time of trouble, such as never has been since there was a nation till that time. "
                   "But at that time your people shall be delivered... And many of those who sleep in "
                   "the dust of the earth shall awake, some to everlasting life, and some to shame "
                   "and everlasting contempt. And those who are wise shall shine like the brightness "
                   "of the sky above; and those who turn many to righteousness, like the stars forever "
                   "and ever' (12:1-3). This is the clearest Old Testament statement of bodily "
                   "resurrection and eschatological judgment. The wise who 'shine like the stars' may "
                   "echo the 'stars of God' language for divine council members (Job 38:7; Isa 14:13), "
                   "suggesting that the resurrected righteous will be elevated to a status comparable "
                   "to the heavenly host — a concept Jesus develops in Luke 20:36 ('they are equal "
                   "to angels').",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 4-5 (the Son of Man as 'second power in heaven')",
            "The Unseen Realm, chapter 13-14 (territorial spirits and Deuteronomy 32)",
            "The Unseen Realm, chapter 35-36 (eschatological judgment and the divine council)",
            "Supernatural, chapter 6-7 (Daniel 7 — the Ancient of Days and the Son of Man)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 10-12 (Michael, Gabriel, territorial princes)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 9-10 (the prince of Persia and cosmic warfare)",
            "The Naked Bible Podcast, episodes 156-170 (Daniel and the divine council)",
            "The Naked Bible Podcast, episode 39 (Daniel 7 — the Son of Man and the Ancient of Days)",
            "The Naked Bible Podcast, episode 43 (Daniel 10 — territorial spirits)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Son of Man — The Divine Figure Who Receives the Kingdom",
            "body": "Daniel 7:13-14 is the single most important background text for Jesus' "
                    "self-designation as 'the Son of Man.' The figure 'like a son of man' (bar enash) "
                    "is not merely human — he rides the clouds of heaven (an exclusive divine prerogative "
                    "in the Old Testament), approaches the Ancient of Days as a near-equal, and receives "
                    "universal, eternal dominion. In the divine council framework, this is the 'second "
                    "power in heaven' — the visible YHWH, the divine agent who shares the Father's "
                    "throne. Jesus' claim before the Sanhedrin — 'you will see the Son of Man seated at "
                    "the right hand of Power and coming on the clouds of heaven' (Mark 14:62) — combined "
                    "Daniel 7:13 with Psalm 110:1, producing the most explosive christological statement "
                    "possible: Jesus claimed to be both the Son of Man who receives the kingdom AND the "
                    "Lord who sits at YHWH's right hand. The high priest's response — tearing his robes "
                    "and declaring 'blasphemy!' — shows that the divine council implications were "
                    "understood: Jesus was claiming to be the divine figure of the heavenly throne room."
        },
        {
            "type": "interpretation",
            "title": "Territorial Spirits — The Architecture of the Unseen Realm",
            "body": "Daniel 10 provides the most detailed revelation of how the Deuteronomy 32 worldview "
                    "operates in practice. The 'prince of Persia' is not the human king of Persia — he "
                    "is a divine being, a member of the sons of God who was allotted authority over the "
                    "Persian Empire. He is powerful enough to oppose Gabriel for 21 days, requiring "
                    "Michael's intervention. The 'prince of Greece' who will come after him is the "
                    "spiritual ruler behind the Greek Empire. Michael is 'your prince' — Israel's "
                    "angelic patron. This passage reveals several critical principles: (1) earthly "
                    "empires have spiritual rulers in the unseen realm; (2) these rulers can affect "
                    "events in the visible world, including delaying angelic messengers; (3) angelic "
                    "warfare is real and ongoing; (4) Michael has a special role as Israel's defender; "
                    "(5) the 'princes' of the nations are not merely servants of YHWH but adversaries "
                    "who resist his purposes. Paul's 'rulers,' 'authorities,' 'cosmic powers,' and "
                    "'spiritual forces of evil in the heavenly places' (Eph 6:12) are the New Testament "
                    "continuation of Daniel 10's territorial spirits."
        },
        {
            "type": "context",
            "title": "The 70 Weeks — Messianic Chronology",
            "body": "Daniel 9:24-27 is the most debated chronological prophecy in the Bible. The 70 "
                    "'weeks' (shabu'im, literally 'sevens') are widely interpreted as 490 years, divided "
                    "into three periods: 7 weeks (49 years), 62 weeks (434 years), and 1 final week "
                    "(7 years). The starting point is 'the going out of the word to restore and build "
                    "Jerusalem' (9:25) — usually identified with either Cyrus's decree (539 BC), "
                    "Artaxerxes' decree to Ezra (458 BC), or Artaxerxes' decree to Nehemiah (445 BC). "
                    "The 'anointed one who is cut off' (9:26) is identified by Christians with Jesus' "
                    "crucifixion and by critical scholars with the murder of the high priest Onias III "
                    "(170 BC). The 'abomination of desolation' (9:27) has been identified with Antiochus "
                    "IV's desecration of the Temple (167 BC), the Roman destruction of the Temple (70 AD), "
                    "and/or a still-future eschatological event. Jesus' citation of the 'abomination of "
                    "desolation' (Matt 24:15) indicates he saw at least a partial future fulfillment "
                    "beyond Antiochus. The prophecy's theological significance is clear regardless of "
                    "the precise chronological calculation: YHWH has a determined plan for history, "
                    "the Messiah will come and be 'cut off,' and the Temple will be destroyed — all "
                    "within a divinely decreed timeframe."
        },
        {
            "type": "scholarship",
            "title": "The Dating Debate — Does It Matter for Theology?",
            "body": "The question of whether Daniel was written in the 6th century BC (traditional) or "
                    "the 2nd century BC (critical consensus) is one of the most contentious issues in "
                    "Old Testament scholarship. The arguments on both sides are substantial: traditionalists "
                    "point to the Imperial Aramaic language, the early Qumran manuscripts, Josephus's "
                    "report about Alexander, and the principle of genuine predictive prophecy. Critical "
                    "scholars point to the detailed accuracy of the 'predictions' about the Seleucid-"
                    "Ptolemaic conflicts, the apocalyptic genre's 2nd-century flowering, and the apparent "
                    "historical errors in the court tales (Darius the Mede, Belshazzar as 'king'). For "
                    "divine council theology, the dating question is secondary: whether Daniel saw the "
                    "Ancient of Days and the Son of Man in the 6th century or a 2nd-century author "
                    "described this vision, the theological content — the divine council enthroned in "
                    "judgment, the Son of Man receiving the kingdom, the territorial spirits governing "
                    "empires, the resurrection of the dead — is the same. Jesus treated Daniel as "
                    "authoritative prophecy (Matt 24:15), and the New Testament's use of Daniel's "
                    "categories (Son of Man, kingdom of God, abomination of desolation, resurrection) "
                    "confirms its theological authority regardless of the dating question."
        }
    ]
}
