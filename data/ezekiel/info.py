"""
info.py -- Ezekiel (Yechezkel): Scholarly Text Introduction

This file provides the "front page" for Ezekiel in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Ezekiel is the divine council book par excellence among the Major Prophets.
The opening throne-chariot vision (chapter 1) -- the merkabah -- is the most
elaborate description of YHWH's heavenly court in the prophetic literature:
four living creatures (later identified as cherubim in chapter 10) bearing
YHWH's mobile throne in a storm theophany of fire, crystal, and wheels within
wheels. The vision of the "anointed guardian cherub" in Eden (28:12-19) is
the most detailed description of a divine council member's fall outside of
Isaiah 14. Ezekiel uniquely combines priestly, prophetic, and apocalyptic
traditions, anticipating the later merkabah mysticism of rabbinic Judaism.
"""

TEXT_INFO = {
    "text_id": "ezekiel",
    "display_name": "Ezekiel (Yechezkel)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Latter Prophets",
        "detail": "Ezekiel is the third of the Major Prophets in the Christian Old Testament and stands "
                  "among the Latter Prophets in the Hebrew Bible, following Jeremiah. The book is "
                  "universally canonical across all Jewish and Christian traditions. Rabbinic literature "
                  "records that the book's canonicity was debated (Talmud Shabbat 13b, Chagigah 13a, "
                  "Menachot 45a) because certain passages appeared to contradict the Torah -- particularly "
                  "the temple vision (chapters 40-48), whose sacrificial regulations differ from those in "
                  "Leviticus. The sage Hananiah ben Hezekiah reportedly 'used 300 jars of oil' burning "
                  "the midnight lamp to resolve these contradictions and preserve Ezekiel's canonical "
                  "status. The opening merkabah vision (chapter 1) was considered so powerful and "
                  "potentially dangerous that the Mishnah (Chagigah 2:1) restricted its public reading: "
                  "'The Merkabah may not be expounded... unless one is wise and understands of his own "
                  "knowledge.' The New Testament draws on Ezekiel extensively: Revelation's four living "
                  "creatures (Rev 4:6-8) come directly from Ezekiel 1 and 10; the Gog and Magog "
                  "eschatology (Rev 20:8) comes from Ezekiel 38-39; the river of life flowing from the "
                  "temple (Rev 22:1-2) comes from Ezekiel 47."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Ezekiel son of Buzi, a priest (kohen) who was among the exiles deported to "
                       "Babylon with King Jehoiachin in 597 BC (Ezek 1:1-3). He was settled at Tel-abib "
                       "by the Chebar canal (3:15), an irrigation channel near the city of Nippur in "
                       "southern Mesopotamia. His ministry spans from 593 BC (the fifth year of "
                       "Jehoiachin's exile, 1:2) to at least 571 BC (the latest dated oracle, 29:17) -- "
                       "a period of at least 22 years. Ezekiel's priestly background profoundly shapes "
                       "his theology: his concern with holiness, purity, the temple, the glory (kavod) "
                       "of YHWH, and the distinction between sacred and profane permeates the entire book.",

        "scholarly_debate": "Critical scholarship has generally accepted a historical Ezekiel as the primary "
                           "author of the book. Unlike Isaiah and Jeremiah, where multiple authorship is "
                           "widely proposed, Ezekiel shows strong literary and theological unity. Debates "
                           "focus on: (1) whether Ezekiel prophesied exclusively in Babylon or also in "
                           "Jerusalem (some passages seem to describe Jerusalem events as if witnessed "
                           "firsthand); (2) the relationship between the historical prophet and the final "
                           "literary form (Zimmerli identified a 'Nachinterpretation' layer of editorial "
                           "expansion); (3) the date and origin of the temple vision (chapters 40-48), "
                           "which some scholars attribute to a later priestly school. The book's elaborate "
                           "dating system (14 precise chronological notices) is unusual and suggests a "
                           "carefully organized literary composition.",

        "bottom_line": "Ezekiel is the most consistently attributable of the Major Prophets. The priestly "
                       "background, the Babylonian setting, the elaborate visionary style, and the "
                       "theological concerns are remarkably consistent throughout. Whether the final form "
                       "involved editorial polish by disciples, the prophetic voice and theological vision "
                       "are recognizably the work of a single powerful mind -- a priest-prophet who saw "
                       "the glory of YHWH depart from the temple and envisioned its glorious return."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Ezekiel's ministry spans 593-571 BC (from the fifth year of Jehoiachin's exile "
                       "to the twenty-seventh year). The book was likely compiled during or shortly after "
                       "this period.",
        "critical_range": "The core of the book dates to Ezekiel's ministry (~593-571 BC). The temple "
                         "vision (chapters 40-48) may have been expanded by priestly editors in the late "
                         "exilic or early post-exilic period (~570-515 BC). The Gog and Magog oracles "
                         "(38-39) are sometimes dated to the post-exilic period. The final form of the "
                         "book was likely established by the 5th century BC.",
        "evidence": "Key evidence includes: (1) The elaborate dating system provides 14 precise dates "
                    "linked to specific regnal years, all consistent with a Babylonian exilic setting. "
                    "(2) Babylonian cultural knowledge pervades the book: the merkabah vision shows "
                    "familiarity with Babylonian throne imagery (the lamassu figures); the Tammuz "
                    "worship in 8:14 reflects Mesopotamian religion; the trade networks in chapter 27 "
                    "reflect Neo-Babylonian commerce. (3) Dead Sea Scrolls: Six manuscripts of Ezekiel "
                    "have been identified at Qumran (4QEzek^a-f, 3QEzek, 11QEzek), dating to ~150-50 "
                    "BC. (4) The 4QEzek^a fragment (4Q73) preserves text very close to the MT, "
                    "suggesting the text was relatively stable by the 2nd century BC."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The Judean exilic community in Babylon, specifically those deported with "
                            "Jehoiachin in 597 BC. This community included priestly families, royal "
                            "officials, and skilled workers (2 Kings 24:14-16). They lived as a distinct "
                            "community near Nippur, maintaining their identity while awaiting either "
                            "return or further judgment. Ezekiel's audience needed to understand: (1) "
                            "that YHWH had not been defeated by Marduk -- he had deliberately withdrawn "
                            "his glory from the defiled temple; (2) that Jerusalem's fall (586 BC) was "
                            "divinely decreed judgment, not divine absence; (3) that beyond judgment lay "
                            "restoration, resurrection, and a new temple filled with YHWH's returned glory.",

        "purpose": "Ezekiel's prophecy serves three phases: (1) Before 586 BC (chapters 1-24): to "
                   "demolish false hope that Jerusalem would be spared, explaining that YHWH's glory "
                   "has departed the temple because of Judah's abominations. (2) During the crisis "
                   "(chapters 25-32): to declare YHWH's sovereignty over all nations through oracles "
                   "of judgment. (3) After 586 BC (chapters 33-48): to proclaim restoration -- new "
                   "hearts, new spirit, dry bones brought to life, a new shepherd (David), a new "
                   "temple, and the return of YHWH's glory.",

        "theological_intent": "Ezekiel's theology revolves around the kavod (glory) of YHWH. The glory "
                             "appears on the merkabah throne (chapter 1), departs the defiled temple in "
                             "stages (chapters 8-11), and returns to the new temple through the east gate "
                             "(43:1-5). The mobility of YHWH's glory is the key theological insight: YHWH "
                             "is not bound to the temple or to the land. He can be present in Babylon, "
                             "standing with his exiled people. The repeated phrase 'and they shall know "
                             "that I am YHWH' (over 60 times) drives the entire book: every act of "
                             "judgment and restoration serves the purpose of YHWH making himself known. "
                             "Ezekiel's contribution to divine council theology is unmatched among the "
                             "prophets: the merkabah, the cherubim, the fallen guardian cherub of Eden "
                             "(chapter 28), and the cosmic warfare of Gog and Magog (38-39) all reveal "
                             "the architecture of the unseen realm."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Aramaic square script (the standard exilic/post-exilic script)",
        "linguistic_notes": "Ezekiel's Hebrew is distinctive and sometimes considered 'late' or 'transitional' "
                           "between classical biblical Hebrew and the Hebrew of the post-exilic period. The "
                           "prose is elaborate and often repetitive, with formulaic expressions: 'the word "
                           "of YHWH came to me' (over 50 times), 'and they shall know that I am YHWH' (over "
                           "60 times), 'son of man' (ben-adam, over 90 times as YHWH's address to Ezekiel). "
                           "The visionary sections (chapters 1, 10, 37, 40-48) use highly technical "
                           "architectural and priestly vocabulary. The book shows some Aramaic influence "
                           "consistent with the Babylonian setting. The name 'Ezekiel' (Yechezqel) means "
                           "'God strengthens' -- appropriate for a prophet commissioned to speak to a "
                           "'hard-forehead and stubborn-heart' people (3:7-8).",
        "grammar_match": "Ezekiel's style is among the most distinctive in the Hebrew Bible -- "
                        "characterized by elaborate symbolic visions, extended allegories (chapters 16, "
                        "23), symbolic actions (chapters 4-5, 12, 24), and detailed architectural "
                        "descriptions (chapters 40-48). The prophetic disputation style (chapters 14, "
                        "18, 33) engages directly with popular theology. The Hebrew is consistent "
                        "throughout, supporting essential unity of authorship."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Ezekiel IS scripture -- the priestly prophet who revealed the mobility of God's "
                   "glory, the architecture of the heavenly throne, and the promise of resurrection "
                   "and cosmic restoration.",
        "nt_usage": "Ezekiel's influence on the New Testament is pervasive, especially in Revelation. "
                    "The four living creatures of Revelation 4:6-8 are drawn from Ezekiel 1 and 10, "
                    "adapted from four faces each to four distinct creatures. The Gog and Magog "
                    "eschatology (Rev 20:8) comes from Ezekiel 38-39. The measuring of the temple "
                    "(Rev 11:1) echoes Ezekiel 40-42. The river of life flowing from the temple (Rev "
                    "22:1-2) comes from Ezekiel 47:1-12. Jesus identifies himself as the 'good shepherd' "
                    "(John 10:11-14) against the background of Ezekiel 34's indictment of Israel's "
                    "shepherds and the promise: 'I myself will search for my sheep' (Ezek 34:11). "
                    "Ezekiel 37's valley of dry bones is the most vivid resurrection image in the OT "
                    "and underlies Paul's resurrection theology (Rom 8:11). The 'new heart and new "
                    "spirit' of Ezekiel 36:26-27 parallels Jeremiah's New Covenant and is fulfilled "
                    "in the Spirit's work at Pentecost.",
        "internal_consistency": "Ezekiel is deeply connected to the Priestly literature (Leviticus, "
                               "Numbers) in its concern for holiness, purity, and proper worship. The "
                               "temple vision (chapters 40-48) deliberately recalls and transforms the "
                               "tabernacle instructions of Exodus 25-40. The shepherd theology (chapter "
                               "34) develops the Davidic covenant of 2 Samuel 7. The cherubim of chapters "
                               "1 and 10 connect to the cherubim over the ark in Exodus 25:18-22. The "
                               "fallen guardian cherub of 28:12-19 connects to the Eden narrative of "
                               "Genesis 2-3. Ezekiel's oracles against the nations (25-32) parallel "
                               "those in Isaiah (13-23) and Jeremiah (46-51)."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls: Six manuscripts of Ezekiel have been identified at Qumran "
                    "(4QEzek^a-f, 3QEzek, 11QEzek), dating to ~150-50 BC. The most significant is "
                    "4QEzek^a (4Q73), which preserves portions of chapters 10, 23, and 41.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. The MT of Ezekiel is generally well-preserved and "
                     "textually stable. The temple vision (chapters 40-48) contains some of the most "
                     "complex Hebrew in the Bible, leading to occasional textual difficulties."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC translation",
             "note": "The LXX of Ezekiel is shorter than the MT (though not as dramatically as with "
                     "Jeremiah). The most significant divergences are in chapters 7, 12, and 36. "
                     "Papyrus 967 (Chester Beatty-Scheide, 3rd century AD) preserves a Greek text "
                     "of Ezekiel that places chapters 36:24-38:29 after 39:29, suggesting a different "
                     "arrangement of the restoration oracles."},
            {"name": "Dead Sea Scrolls", "date": "~150-50 BC",
             "note": "The Qumran Ezekiel fragments generally support the proto-MT tradition. The "
                     "4QEzek manuscripts confirm the early stability of the text."},
            {"name": "Targum Jonathan", "date": "1st-3rd century AD tradition",
             "note": "The Aramaic Targum of Ezekiel is particularly valuable for its treatment of "
                     "the merkabah vision (chapter 1), where it softens the anthropomorphic language "
                     "and adds interpretive glosses to protect the mystery of the divine throne."}
        ],
        "reliability": "Ezekiel's text is well-preserved and relatively stable across the major "
                       "witnesses. The textual situation is simpler than that of Jeremiah. The most "
                       "significant debates concern the Papyrus 967 arrangement of chapters 36-39 and "
                       "occasional difficulties in the temple vision's architectural vocabulary."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Ezekiel prophesied among the Judean exiles in Babylon from ~593 to ~571 BC. The "
                   "first deportation (597 BC) carried King Jehoiachin, the royal family, military "
                   "leaders, craftsmen, and priests (including Ezekiel) to Babylon (2 Kings 24:14-16). "
                   "The exiles were settled in communities along the irrigation canals of southern "
                   "Mesopotamia, near the city of Nippur. The Chebar canal (nahar kebar) where Ezekiel "
                   "received his visions has been identified with the naru kabari, a major Babylonian "
                   "irrigation canal. Ezekiel's ministry had two phases: before the fall of Jerusalem "
                   "(593-586 BC), he proclaimed coming judgment; after the fall (586-571 BC), he "
                   "proclaimed restoration.",

        "geography": "The primary setting is the Babylonian exile -- specifically the community at "
                     "Tel-abib (3:15) by the Chebar canal, near Nippur in southern Mesopotamia. "
                     "Ezekiel's visionary journeys transport him to Jerusalem (chapters 8-11, where "
                     "he sees the temple abominations and the departure of YHWH's glory), to a valley "
                     "of dry bones (chapter 37), and to a high mountain overlooking the new temple "
                     "(chapters 40-48). The oracles against the nations (chapters 25-32) address Ammon, "
                     "Moab, Edom, Philistia, Tyre, Sidon, and Egypt.",

        "historical_connections": "The Babylonian context is confirmed by multiple sources. The TAYN "
                                 "tablets from Nippur (5th century BC) record Judean names in economic "
                                 "transactions, confirming the exilic community's settlement near Nippur. "
                                 "The Al-Yahudu tablets (published 2015) record the activities of Judean "
                                 "exiles in a town called 'al-Yahudu' ('the city of Judah') in Babylonia, "
                                 "providing direct evidence of the exilic communities Ezekiel addressed. "
                                 "Nebuchadnezzar's siege of Tyre (585-573 BC) corresponds to the Tyre "
                                 "oracles (chapters 26-28). The Murashu archive from Nippur (5th century "
                                 "BC) records Judean names participating in Babylonian economic life, "
                                 "consistent with Jeremiah's counsel to 'seek the welfare of the city.'"
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Ezekiel contains the most elaborate divine council imagery in the prophetic "
                   "literature. Three passages are of supreme importance: the merkabah throne vision "
                   "(chapters 1, 10), the fallen guardian cherub (28:12-19), and the departure and "
                   "return of YHWH's glory (chapters 10-11, 43)."
                   "\n\n"
                   "THE MERKABAH -- YHWH'S MOBILE THRONE (Ezekiel 1, 10): Ezekiel's inaugural vision "
                   "is the most elaborate theophany in the Hebrew Bible. A storm wind (ruach se'arah) "
                   "comes from the north, with 'a great cloud, with brightness around it, and fire "
                   "flashing forth continually' (1:4). Within the cloud are four living creatures "
                   "(chayyot), each with four faces (human, lion, ox, eagle), four wings, and 'the "
                   "appearance of burning coals of fire' (1:13). Beside each creature is a wheel "
                   "(ophan) within a wheel, with rims 'full of eyes all around' (1:18). Above the "
                   "creatures is a firmament (raqia) 'shining like awe-inspiring crystal' (1:22), and "
                   "above the firmament is 'the likeness of a throne, in appearance like sapphire' "
                   "(1:26). On the throne sits 'a likeness with a human appearance' (demut kemar'eh "
                   "adam, 1:26) -- YHWH himself, described in the most careful, distancing language "
                   "possible. This is the divine council's throne room made mobile: YHWH is not "
                   "confined to the Jerusalem temple but rides on a living throne, attended by the "
                   "cherubim of the council. Chapter 10 explicitly identifies the 'living creatures' "
                   "as cherubim (10:15, 20), connecting the merkabah to the cherubim over the ark in "
                   "the Holy of Holies. The merkabah became the foundation of Jewish mystical "
                   "tradition (merkabah mysticism)."
                   "\n\n"
                   "THE ANOINTED GUARDIAN CHERUB (Ezekiel 28:12-19): The lament over the king of Tyre "
                   "transcends any human ruler: 'You were the signet of perfection (chotam tokhnit), "
                   "full of wisdom (male chokmah) and perfect in beauty (kelil yofi). You were in Eden "
                   "(be-Eden), the garden of God; every precious stone was your covering... On the day "
                   "that you were created they were prepared. You were an anointed guardian cherub "
                   "(keruv mimshach hassokek). I placed you; you were on the holy mountain of God "
                   "(behar-qodesh elohim); in the midst of the stones of fire you walked. You were "
                   "blameless in your ways from the day you were created, till unrighteousness was "
                   "found in you' (28:12-15). This is the most detailed portrait of a fallen divine "
                   "council member in scripture: a cherub (council attendant), anointed and installed "
                   "by God himself, dwelling in Eden (the divine council's garden), walking among the "
                   "'stones of fire' (the fiery court of YHWH's presence). His sin: 'Your heart was "
                   "proud because of your beauty; you corrupted your wisdom for the sake of your "
                   "splendor. I cast you to the ground' (28:17). Michael Heiser identifies this "
                   "passage as describing a divine being distinct from the nachash (serpent) of Genesis "
                   "3 and from the Helel ben Shachar of Isaiah 14 -- multiple divine council members "
                   "rebelled, not just one."
                   "\n\n"
                   "THE DEPARTURE AND RETURN OF YHWH'S GLORY (Ezekiel 10-11, 43): The glory "
                   "(kavod) of YHWH departs the temple in three stages: from the cherubim above the "
                   "ark to the threshold of the temple (10:4), from the threshold to the east gate "
                   "(10:18-19), and from the east gate to the Mount of Olives (11:23). Each stage is "
                   "a withdrawal of divine presence in response to the abominations described in "
                   "chapter 8 (sun worship, Tammuz worship, idol worship in the inner court). The "
                   "glory does not return until the new temple vision (43:1-5): 'The glory of the God "
                   "of Israel was coming from the east... and the earth shone with his glory... the "
                   "glory of YHWH filled the temple' (43:2, 5). This is the divine council's sovereign "
                   "decision: YHWH is free to withdraw and free to return. The departure explains the "
                   "destruction of 586 BC; the return promises the eschatological restoration.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 2-3 (the divine council throne room -- Ezekiel 1)",
            "The Unseen Realm, chapter 8-10 (the guardian cherub in Eden -- Ezekiel 28:12-19)",
            "The Unseen Realm, chapter 35-36 (the return of YHWH's glory -- Ezekiel 43)",
            "Supernatural, chapter 5-6 (the merkabah and the cherubim)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 4-6 (cherubim as council attendants)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 7-8 (the fallen guardian cherub)",
            "The Naked Bible Podcast, episodes 191-210 (Ezekiel and the divine council)",
            "The Naked Bible Podcast, episode 30 (Ezekiel 28 -- the guardian cherub in Eden)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Merkabah -- The Most Elaborate Divine Throne Vision",
            "body": "Ezekiel 1 describes YHWH's throne in more detail than any other passage in scripture. "
                    "The four living creatures (chayyot) are identified as cherubim in chapter 10 -- the "
                    "same class of beings that guarded Eden (Gen 3:24) and spread their wings over the "
                    "ark of the covenant (Exod 25:18-22). Their four faces (human, lion, ox, eagle) may "
                    "represent the four highest orders of creation: humanity, wild animals, domestic "
                    "animals, and birds. The wheels (ophanim) 'full of eyes' suggest all-seeing "
                    "omniscience. The entire apparatus is a mobile throne -- YHWH is not confined to "
                    "Jerusalem but can appear in Babylon, among his exiled people. This vision became "
                    "the foundation of merkabah mysticism in rabbinic Judaism and profoundly influenced "
                    "the throne room visions of Daniel 7, 1 Enoch 14, and Revelation 4."
        },
        {
            "type": "interpretation",
            "title": "The Guardian Cherub in Eden -- A Fallen Divine Council Member",
            "body": "Ezekiel 28:12-19 describes a being who was 'in Eden, the garden of God,' who was an "
                    "'anointed guardian cherub,' who walked 'in the midst of the stones of fire' on the "
                    "'holy mountain of God.' This transcends any human king of Tyre. Michael Heiser "
                    "identifies this as a divine council member -- a cherub installed by God himself to "
                    "guard the sacred garden. His fall was caused by pride: 'Your heart was proud because "
                    "of your beauty; you corrupted your wisdom for the sake of your splendor.' Heiser "
                    "distinguishes this figure from the nachash (serpent) of Genesis 3 and the Helel ben "
                    "Shachar of Isaiah 14 -- multiple divine beings may have rebelled at different times "
                    "and in different ways. The 'stones of fire' may refer to the fiery court of YHWH's "
                    "presence (cf. the burning coals of Ezekiel 1:13 and Isaiah 6:6)."
        },
        {
            "type": "context",
            "title": "The Valley of Dry Bones -- Resurrection and Restoration",
            "body": "Ezekiel 37:1-14 is the most powerful resurrection vision in the Old Testament. "
                    "YHWH sets Ezekiel down in a valley full of bones that are 'very dry' -- they have "
                    "been dead a long time. 'Son of man, can these bones live?' (37:3). Ezekiel "
                    "prophesies as commanded, and the bones reassemble: 'breath (ruach) came into them, "
                    "and they lived and stood on their feet, an exceedingly great army' (37:10). YHWH "
                    "interprets: 'These bones are the whole house of Israel. They say, \"Our bones are "
                    "dried up, and our hope is lost\"' (37:11). The primary meaning is national "
                    "restoration -- Israel will be 'raised' from the 'grave' of exile. But the imagery "
                    "has always carried eschatological weight: if YHWH can raise a nation from exile, he "
                    "can raise bodies from death. Paul's teaching on bodily resurrection (Rom 8:11; "
                    "1 Cor 15) draws on this Ezekielian tradition."
        },
        {
            "type": "scholarship",
            "title": "Ezekiel and the Priestly Tradition",
            "body": "Ezekiel is a priest-prophet -- the only Major Prophet with explicit priestly "
                    "credentials (1:3). His priestly background explains the book's distinctive "
                    "theology: the obsessive concern with holiness and defilement, the detailed "
                    "temple measurements (chapters 40-48), the vision of YHWH's glory (kavod) as "
                    "the central theological concept, the distinction between 'holy' and 'profane' "
                    "(42:20; 44:23), and the use of priestly vocabulary throughout. The temple vision "
                    "of chapters 40-48 has puzzled interpreters for centuries: does it describe a "
                    "literal future temple, a symbolic representation of YHWH's restored presence, or "
                    "a priestly ideal that was never meant to be physically constructed? The vision's "
                    "river of life (47:1-12), which flows from the temple and transforms the Dead Sea "
                    "into fresh water, clearly transcends any historical temple -- it is an eschatological "
                    "vision of cosmic healing that Revelation 22:1-2 develops."
        }
    ]
}
