"""
info.py -- Jeremiah (Yirmeyahu): Scholarly Text Introduction

This file provides the "front page" for Jeremiah in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Jeremiah is the longest prophetic book in the Hebrew Bible and the most
personally revealing. The "weeping prophet" ministered for over forty years
during Judah's final decline, the Babylonian siege, and the destruction of
Jerusalem in 586 BC. His message was profoundly unpopular: submit to Babylon,
for YHWH himself has sent Nebuchadnezzar as his instrument of judgment.
Jeremiah was beaten, imprisoned, thrown into a cistern, and accused of
treason -- yet he also delivered the most revolutionary promise in the Old
Testament: the New Covenant (31:31-34), in which YHWH would write his Torah
on human hearts. The divine council framework is explicit in Jeremiah 23:18-22,
where true prophets are defined as those who have "stood in the council of
YHWH" -- the most direct statement in scripture about what distinguishes
genuine from false prophecy.
"""

TEXT_INFO = {
    "text_id": "jeremiah",
    "display_name": "Jeremiah (Yirmeyahu)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Latter Prophets",
        "detail": "Jeremiah is the second book of the Major Prophets in the Christian Old Testament "
                  "and stands among the Latter Prophets (Nevi'im Acharonim) in the Hebrew Bible, "
                  "where it typically follows Isaiah. Jeremiah is universally canonical across all "
                  "Jewish and Christian traditions. The Septuagint preserves a significantly shorter "
                  "and differently ordered version of Jeremiah (about one-eighth shorter than the "
                  "Masoretic Text), raising important text-critical questions. The New Testament "
                  "quotes Jeremiah extensively: the New Covenant passage (Jer 31:31-34) is quoted "
                  "in full in Hebrews 8:8-12, the longest Old Testament quotation in the New "
                  "Testament. Jesus alludes to Jeremiah's temple sermon (Jer 7:11) when he cleanses "
                  "the temple: 'You have made it a den of robbers' (Matt 21:13). Matthew 2:17-18 "
                  "cites Jeremiah 31:15 ('Rachel weeping for her children') in connection with the "
                  "slaughter of the innocents. Paul's calling echoes Jeremiah's: 'set apart before "
                  "I was born' (Gal 1:15; cf. Jer 1:5)."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Jeremiah son of Hilkiah, a priest from Anathoth in the territory of Benjamin "
                       "(Jer 1:1). He was called to prophesy in the thirteenth year of King Josiah "
                       "(627 BC) and ministered through the reigns of Josiah, Jehoahaz, Jehoiakim, "
                       "Jehoiachin, and Zedekiah -- a span of over forty years. His scribe Baruch "
                       "son of Neriah recorded his oracles (Jer 36:4, 32; 45:1) and likely edited "
                       "portions of the biographical narrative (chapters 26-45). Jeremiah dictated "
                       "a scroll of prophecies that King Jehoiakim burned column by column (36:23), "
                       "after which Jeremiah re-dictated the entire scroll 'with many similar words "
                       "added' (36:32). After the fall of Jerusalem, Jeremiah was taken to Egypt "
                       "against his will by fleeing Judean refugees (43:6-7), where tradition says "
                       "he died.",

        "scholarly_debate": "Critical scholarship generally accepts Jeremiah ben Hilkiah as the historical "
                           "prophet behind the book but recognizes multiple editorial layers. The 'three "
                           "sources' model (Mowinckel, 1914) identifies: (A) poetic oracles from Jeremiah "
                           "himself (mainly chapters 1-25); (B) biographical prose narratives about "
                           "Jeremiah, likely composed by Baruch (chapters 26-45); and (C) Deuteronomistic "
                           "prose sermons that show theological and stylistic affinity with the books of "
                           "Kings and Deuteronomy (e.g., 7:1-8:3; 11:1-17; 18:1-12). The relationship "
                           "between the shorter LXX text and the longer MT is debated: some scholars "
                           "(Tov, Lundbom) argue the LXX preserves an earlier, shorter edition of the "
                           "book; others argue the MT preserves additions made during the exilic period. "
                           "Both textual traditions were attested at Qumran (4QJer^a aligns with MT; "
                           "4QJer^b with the shorter LXX tradition).",

        "bottom_line": "Jeremiah is a genuine prophetic figure whose oracles were preserved, edited, "
                       "and supplemented by his scribe Baruch and later Deuteronomistic editors. The "
                       "editorial process does not undermine the prophetic authority of the text -- it "
                       "reflects the normal process by which prophetic books were composed in ancient "
                       "Israel. The theological core -- YHWH's sovereignty over nations, the certainty "
                       "of covenant judgment, and the promise of a New Covenant -- is consistent "
                       "throughout all editorial layers."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Jeremiah's ministry spanned ~627-586 BC (from Josiah's thirteenth year to the "
                       "fall of Jerusalem), with additional oracles from Egypt (after 586 BC). The book "
                       "was compiled by Baruch during and after this period.",
        "critical_range": "The poetic oracles (source A) date to ~627-586 BC. The Baruch narrative "
                         "(source B) was likely composed shortly after 586 BC. The Deuteronomistic "
                         "prose (source C) may date to the exilic period (~586-539 BC). The final "
                         "form of the MT edition probably dates to the late 6th or 5th century BC. "
                         "The shorter LXX Vorlage may represent an earlier editorial stage.",
        "evidence": "Key evidence includes: (1) The Lachish Letters (588 BC), ostraca found at "
                    "Lachish mentioning 'the prophet' and reflecting the same political tensions "
                    "described in Jeremiah -- the pro-Babylonian vs. pro-Egyptian factions. (2) "
                    "The Baruch Bulla (Avigad, 1975), a clay seal impression reading 'Belonging "
                    "to Berekhyahu son of Neriyahu the scribe' -- likely Jeremiah's scribe Baruch "
                    "son of Neriah. (3) Dead Sea Scrolls: Six manuscripts of Jeremiah have been "
                    "identified at Qumran (4QJer^a-e, 2QJer), with 4QJer^b preserving a text "
                    "closer to the shorter LXX tradition. (4) Babylonian Chronicle records confirm "
                    "Nebuchadnezzar's campaigns against Jerusalem in 597 and 586 BC. (5) The "
                    "Weidner Tablets from Babylon record rations given to 'Jehoiachin king of "
                    "Judah' -- the exiled king mentioned in Jeremiah 52:31-34."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Judah in its final decades -- a nation caught between the superpowers "
                            "of Egypt and Babylon, facing the consequences of generations of covenant "
                            "unfaithfulness. The specific audiences include: King Josiah and the "
                            "reformers (early ministry), King Jehoiakim and the temple establishment "
                            "(who burned Jeremiah's scroll), King Zedekiah and the pro-Egyptian faction "
                            "(who imprisoned Jeremiah), and the exilic community (who received the "
                            "letter of Jeremiah 29). After the fall, the audience includes Judean "
                            "refugees in Egypt and the exiles in Babylon.",

        "purpose": "Jeremiah's prophecy serves a triple purpose: (1) to explain the fall of Jerusalem "
                   "as YHWH's righteous judgment for covenant violation, not as evidence of YHWH's "
                   "weakness; (2) to call for submission to Babylon as YHWH's instrument, against the "
                   "false prophets who promised quick deliverance; and (3) to announce that beyond "
                   "judgment lies restoration -- YHWH will make a New Covenant with Israel, writing "
                   "his Torah on their hearts (31:31-34), gathering the scattered exiles, and raising "
                   "up a righteous Branch from David's line (23:5-6; 33:15-16).",

        "theological_intent": "Jeremiah's theology is profoundly personal and relational. YHWH is not "
                             "an abstract sovereign but a wounded husband (2:1-3:5), a grieving father "
                             "(31:20), and a divine potter who reshapes nations (18:1-12). The prophet "
                             "himself embodies the divine pathos -- his confessions (11:18-12:6; 15:10-21; "
                             "17:14-18; 18:18-23; 20:7-18) reveal the anguish of proclaiming judgment "
                             "against his own people. The New Covenant oracle (31:31-34) is Jeremiah's "
                             "supreme theological contribution: the Sinai covenant failed not because it "
                             "was defective but because Israel's heart was defective. The New Covenant "
                             "will solve this by internalizing the Torah -- writing it on the heart -- so "
                             "that obedience flows from transformed nature rather than external compulsion. "
                             "Jesus identified this New Covenant with his own blood (Luke 22:20)."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew (with a small Aramaic section at 10:11)",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "Jeremiah's Hebrew spans two registers: the poetic oracles (chapters 1-25 "
                           "primarily) use powerful, emotionally charged prophetic poetry with vivid "
                           "metaphors -- YHWH as husband, Israel as adulterous wife, the land as a "
                           "mourning mother. The prose sections use a style closely related to "
                           "Deuteronomistic prose (repeated phrases like 'rising early and sending' "
                           "prophets, 'stubborn heart,' 'other gods'). Jeremiah 10:11 is the sole "
                           "Aramaic verse in the book -- a formula to recite to the nations: 'The gods "
                           "who did not make the heavens and the earth shall perish from the earth and "
                           "from under the heavens.' The name 'Jeremiah' (Yirmeyahu) likely means "
                           "'YHWH exalts' or 'YHWH establishes.' Key theological vocabulary includes "
                           "berit chadashah (new covenant, 31:31), tsemach tsaddiq (righteous Branch, "
                           "23:5), and sod YHWH (council of YHWH, 23:18).",
        "grammar_match": "The poetic sections display archaic forms and compact parallelism typical of "
                        "classical Hebrew prophecy. The prose sections show the longer, more formulaic "
                        "style associated with Deuteronomistic literature. This stylistic duality has "
                        "been used to argue for multiple authors, but it may equally reflect a prophet "
                        "whose own style evolved over four decades of ministry, combined with editorial "
                        "formatting by his scribe Baruch."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Jeremiah IS scripture -- the prophet of the New Covenant, the theological bridge "
                   "between the old and new dispensations, and the basis for the Christian understanding "
                   "of covenant transformation.",
        "nt_usage": "Jeremiah's New Covenant oracle (31:31-34) is the foundation of New Testament "
                    "covenant theology. It is quoted in full in Hebrews 8:8-12 (the longest OT "
                    "quotation in the NT) and again in Hebrews 10:16-17. Jesus explicitly identifies "
                    "his blood with the New Covenant at the Last Supper: 'This cup that is poured out "
                    "for you is the new covenant in my blood' (Luke 22:20; cf. 1 Cor 11:25). Paul "
                    "describes himself as a 'minister of a new covenant, not of the letter but of "
                    "the Spirit' (2 Cor 3:6). Jesus' temple cleansing quotes Jeremiah 7:11 ('den of "
                    "robbers'). Matthew 2:17-18 cites Jeremiah 31:15 ('Rachel weeping'). Jeremiah's "
                    "call narrative (1:5, 'Before I formed you in the womb I knew you') echoes in "
                    "Paul's self-understanding (Gal 1:15). The '70 years' prophecy (25:11-12; 29:10) "
                    "is the basis for Daniel's 70 weeks (Dan 9:2, 24-27).",
        "internal_consistency": "Jeremiah connects to the Deuteronomistic theology of Kings: both "
                               "interpret the exile as the consequence of covenant violation. The New "
                               "Covenant promise (31:31-34) presupposes the failure of the Sinai covenant "
                               "described in Exodus-Deuteronomy. The righteous Branch prophecy (23:5-6; "
                               "33:15-16) develops the Davidic covenant of 2 Samuel 7. Jeremiah's "
                               "oracles against the nations (chapters 46-51) parallel those in Isaiah "
                               "(13-23) and Ezekiel (25-32). The divine council language of 23:18-22 "
                               "connects directly to the council scenes of 1 Kings 22, Isaiah 6, and "
                               "Job 1-2."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls: Six manuscripts of Jeremiah have been identified at Qumran "
                    "(4QJer^a-e, 2QJer), dating to ~200-50 BC. These manuscripts are critically "
                    "important because they attest both textual traditions: 4QJer^a follows the "
                    "longer MT tradition, while 4QJer^b follows the shorter LXX tradition.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The longer text tradition (52 chapters). The MT of Jeremiah is approximately "
                     "one-eighth longer than the LXX and arranges the oracles against the nations "
                     "(chapters 46-51) at the end of the book. This is the basis for most English "
                     "translations (ESV, NASB, NIV, etc.)."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC translation",
             "note": "The LXX Jeremiah is significantly shorter (about 2,700 words fewer) and "
                     "arranges the oracles against the nations after 25:13 (in the middle of the book "
                     "rather than at the end). The LXX omits several passages found in the MT, "
                     "including much of 33:14-26 and portions of 27:1-22. Scholars debate whether "
                     "the LXX reflects an earlier, shorter edition or whether the MT expanded an "
                     "originally shorter text."},
            {"name": "Dead Sea Scrolls", "date": "~200-50 BC",
             "note": "4QJer^a (closer to MT) and 4QJer^b (closer to LXX) prove that both textual "
                     "traditions coexisted in the Second Temple period. This is one of the strongest "
                     "cases in the Hebrew Bible for two distinct literary editions of the same book."},
            {"name": "Targum Jonathan", "date": "1st-3rd century AD tradition",
             "note": "The Aramaic Targum of Jeremiah is relatively literal for the prophetic books "
                     "but includes interpretive expansions, particularly in the messianic passages "
                     "(23:5-6; 33:15-16) where the 'righteous Branch' is explicitly identified as "
                     "the Messiah."}
        ],
        "reliability": "The textual situation of Jeremiah is more complex than most biblical books "
                       "due to the significant divergence between the MT and LXX traditions. However, "
                       "the core theological content -- the covenant judgment, the New Covenant promise, "
                       "the divine council language, the messianic Branch prophecy -- is stable across "
                       "both traditions. The Qumran evidence confirms that the textual plurality is "
                       "ancient, not the result of medieval corruption."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Jeremiah prophesied during the most catastrophic period in Judah's history: the "
                   "final decades before the Babylonian destruction of Jerusalem in 586 BC. His ministry "
                   "began during Josiah's reforms (~627 BC), continued through the brief reign of "
                   "Jehoahaz (609 BC), the hostile reign of Jehoiakim (609-598 BC, who burned Jeremiah's "
                   "scroll), the three-month reign of Jehoiachin (598-597 BC, who was deported to "
                   "Babylon), and the final decade of Zedekiah (597-586 BC, who imprisoned Jeremiah). "
                   "After the fall, Jeremiah was taken to Egypt by Judean refugees, where tradition "
                   "says he continued to prophesy and eventually died.",

        "geography": "Jerusalem is the primary setting -- the temple, the palace, the prison, the "
                     "potter's house, the Benjamin Gate. The book also references Anathoth (Jeremiah's "
                     "hometown, 3 miles north of Jerusalem), Mizpah (where Gedaliah governed after the "
                     "fall), Tahpanhes and other Egyptian cities (where the refugees fled), and Babylon "
                     "(where the exiles were taken). The oracles against the nations (chapters 46-51) "
                     "range across Egypt, Philistia, Moab, Ammon, Edom, Damascus, Kedar, Elam, and "
                     "Babylon.",

        "historical_connections": "The Babylonian Chronicle confirms Nebuchadnezzar's capture of "
                                 "Jerusalem on 2 Adar 597 BC (matching 2 Kings 24:10-17 and Jeremiah "
                                 "52:28). The Lachish Letters (ostraca from ~588 BC) mention a prophet "
                                 "whose message 'weakens the hands' of the soldiers -- possibly a "
                                 "reference to Jeremiah (cf. 38:4). The Baruch Bulla provides possible "
                                 "archaeological evidence for Jeremiah's scribe. The Weidner Tablets "
                                 "from Babylon list rations for 'Jehoiachin king of Judah,' confirming "
                                 "his exile. Nebuchadnezzar's destruction of Jerusalem is confirmed by "
                                 "the Babylonian Chronicle and by the archaeological destruction layer "
                                 "found throughout excavations of Iron Age Jerusalem."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "high",
        "summary": "Jeremiah contains the most explicit definition of true prophecy in terms of the "
                   "divine council. Jeremiah 23:18-22 is the key passage."
                   "\n\n"
                   "THE COUNCIL OF YHWH -- THE TEST OF TRUE PROPHECY (Jeremiah 23:18-22): 'For "
                   "who among them has stood in the council (sod) of YHWH to see and to hear his "
                   "word? Who has paid attention to his word and listened?' (23:18). 'But if they "
                   "had stood in my council (sod), then they would have proclaimed my words to my "
                   "people, and they would have turned them from their evil way, and from the evil "
                   "of their deeds' (23:22). The Hebrew word sod means 'council, intimate assembly, "
                   "secret deliberation.' Jeremiah's criterion for distinguishing true from false "
                   "prophets is whether they have access to the divine council -- the heavenly "
                   "assembly where YHWH deliberates with his host. False prophets like Hananiah "
                   "(chapter 28) proclaim 'peace, peace' without having stood in YHWH's council; "
                   "they invent their own messages. True prophets (like Jeremiah, like Micaiah in "
                   "1 Kings 22) have been admitted to the council's deliberations and relay what "
                   "YHWH has decreed. This is the most systematic statement in scripture about the "
                   "prophetic office's connection to the divine council."
                   "\n\n"
                   "COSMIC WARFARE AND THE FALL OF BABYLON (Jeremiah 50-51): The oracles against "
                   "Babylon (the longest in the book) describe YHWH's judgment in cosmic terms. "
                   "'YHWH has opened his armory and brought out the weapons of his wrath, for the "
                   "Lord GOD of hosts has a work to do in the land of the Chaldeans' (50:25). The "
                   "fall of Babylon is not merely geopolitical -- it is a divine council decree "
                   "executed by YHWH's heavenly host. The 'destroyer' (mashchit) sent against "
                   "Babylon (51:1) echoes the destroyer sent against Egypt at the Passover (Exod "
                   "12:23) and the destroying angel of 2 Samuel 24:16. Babylon's spiritual patron, "
                   "Bel/Marduk, is explicitly named and shamed: 'Bel is put to shame, Merodach is "
                   "dismayed' (50:2) -- the patron deity of Babylon is defeated in the cosmic realm "
                   "as Babylon falls in the earthly realm."
                   "\n\n"
                   "THE RIGHTEOUS BRANCH AND THE DIVINE NAME (Jeremiah 23:5-6; 33:15-16): 'Behold, "
                   "the days are coming, declares YHWH, when I will raise up for David a righteous "
                   "Branch (tsemach tsaddiq), and he shall reign as king and deal wisely, and shall "
                   "execute justice and righteousness in the land. In his days Judah will be saved, "
                   "and Israel will dwell securely. And this is the name by which he will be called: "
                   "YHWH is our righteousness (YHWH Tsidqenu)' (23:5-6). The messianic Branch "
                   "receives YHWH's own name -- a staggering claim in the divine council framework. "
                   "The Messiah is not merely a human king but bears the divine name, placing him "
                   "within the identity of God himself.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 2-3 (the divine council and the sod of YHWH)",
            "The Unseen Realm, chapter 15-16 (false vs. true prophets and council access)",
            "Supernatural, chapter 5-6 (the prophetic office and the heavenly assembly)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 7-8 (council access and prophetic authority)",
            "The Naked Bible Podcast, episodes 175-190 (Jeremiah and the divine council)",
            "The Naked Bible Podcast, episode 50 (Jeremiah 23 -- the sod of YHWH)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The New Covenant -- Jeremiah's Supreme Theological Contribution",
            "body": "Jeremiah 31:31-34 is the foundation of New Testament covenant theology. The promise "
                    "is not merely a renewal of the Sinai covenant but something qualitatively new: 'Not "
                    "like the covenant that I made with their fathers on the day when I took them by the "
                    "hand to bring them out of the land of Egypt, my covenant that they broke' (31:32). "
                    "The Sinai covenant was external -- written on stone tablets. The New Covenant is "
                    "internal -- 'I will put my law within them, and I will write it on their hearts' "
                    "(31:33). The result: 'they shall all know me, from the least of them to the "
                    "greatest' (31:34) -- universal, direct, personal knowledge of YHWH. And the basis: "
                    "'For I will forgive their iniquity, and I will remember their sin no more' (31:34). "
                    "Jesus identified this New Covenant with his own sacrificial death (Luke 22:20). The "
                    "entire book of Hebrews is built on the argument that Jesus mediates a 'better "
                    "covenant' -- the New Covenant of Jeremiah 31."
        },
        {
            "type": "interpretation",
            "title": "The Sod of YHWH -- Standing in the Divine Council",
            "body": "Jeremiah 23:18-22 provides the clearest biblical definition of what makes a prophet "
                    "true: access to YHWH's heavenly council (sod). The Hebrew word sod carries the dual "
                    "meaning of 'council/assembly' and 'secret/intimate knowledge.' A true prophet is one "
                    "who has been granted audience in YHWH's throne room, heard the divine deliberation, "
                    "and been sent to relay the council's decree. This connects directly to the council "
                    "scenes of 1 Kings 22:19-23 (Micaiah sees YHWH deliberating with his host), Isaiah "
                    "6:1-8 ('Whom shall I send, and who will go for us?'), and Job 1-2 (the heavenly "
                    "assembly convenes). Michael Heiser argues that the prophetic office is fundamentally "
                    "a divine council role: prophets are human agents granted temporary access to the "
                    "heavenly assembly to receive and transmit YHWH's decrees."
        },
        {
            "type": "context",
            "title": "The Two Editions of Jeremiah",
            "body": "Jeremiah presents one of the most fascinating text-critical situations in the Hebrew "
                    "Bible. The Masoretic Text (MT) is approximately one-eighth longer than the Septuagint "
                    "(LXX), and the oracles against the nations are placed in different locations (end of "
                    "the book in MT, middle in LXX). The Dead Sea Scrolls confirmed that both traditions "
                    "existed in the Second Temple period (4QJer^a aligns with MT, 4QJer^b with LXX). "
                    "This means Jeremiah circulated in two distinct literary editions -- not because of "
                    "scribal error but because the book underwent deliberate editorial development. The "
                    "theological content is consistent across both editions; the differences are primarily "
                    "in arrangement and the presence or absence of certain repetitive or supplementary "
                    "passages."
        },
        {
            "type": "scholarship",
            "title": "Archaeological Confirmation -- Baruch Bulla and Lachish Letters",
            "body": "Jeremiah has stronger archaeological corroboration than almost any other prophetic "
                    "book. The Baruch Bulla (discovered by Nahman Avigad, published 1975) is a clay seal "
                    "impression reading 'Belonging to Berekhyahu son of Neriyahu the scribe' -- almost "
                    "certainly Jeremiah's scribe Baruch son of Neriah (Jer 36:4). The Lachish Letters "
                    "(discovered 1935) are ostraca from the final Babylonian siege (~588 BC) that reflect "
                    "the same political tensions described in Jeremiah: the pro-Babylonian vs. pro-Egyptian "
                    "factions, the silencing of prophetic voices, and the desperate military situation. "
                    "Letter IV mentions that 'we are watching for the fire signals of Lachish' because "
                    "'we cannot see Azekah' -- meaning Azekah had already fallen, matching the sequence "
                    "described in Jeremiah 34:7."
        }
    ]
}
