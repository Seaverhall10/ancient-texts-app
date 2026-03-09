"""
info.py -- Ezra: Scholarly Text Introduction

This file provides the "front page" for Ezra in the Ancient Texts Library.
Ezra narrates the return from Babylonian exile, the rebuilding of the temple,
and the covenant renewal under Ezra the scribe. The book is notable for its
bilingual composition (Hebrew and Aramaic), its inclusion of official Persian
documents, and its theology of restoration: God is bringing his people home
and reestablishing his worship. Ezra the priest-scribe represents a new kind
of leader in Israel -- not king or prophet, but Torah scholar.
"""

TEXT_INFO = {
    "text_id": "ezra",
    "display_name": "Ezra",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "Ezra is universally recognized as canonical by Jewish, Catholic, Orthodox, "
                  "and Protestant traditions. In the Hebrew Bible, Ezra and Nehemiah were "
                  "originally a single book (Ezra-Nehemiah), placed among the Ketuvim (Writings) "
                  "near Chronicles. The Septuagint designates them as '2 Esdras' (with 1 Esdras "
                  "being a Greek version of Ezra with additional material). The Talmud (Bava Batra "
                  "15a) treats Ezra-Nehemiah as one book. The division into two books occurs in "
                  "Christian manuscripts beginning with Origen (3rd century AD). The book's "
                  "inclusion of official Aramaic documents and its eyewitness Ezra memoir give it "
                  "a unique documentary character among biblical books."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud (Bava Batra 15a) attributes authorship to Ezra himself, with "
                       "Nehemiah completing the work. The 'Ezra memoir' sections (7:27-9:15) are "
                       "written in the first person, supporting Ezra's personal involvement. Jewish "
                       "tradition holds Ezra in the highest regard -- the Talmud states that 'Ezra "
                       "was worthy of receiving the Torah had Moses not preceded him' (Sanhedrin 21b).",

        "scholarly_debate": "The relationship between Ezra, Nehemiah, and Chronicles is debated. "
                           "The traditional view (Albright, Cross) holds that a single 'Chronicler' "
                           "authored all three. Japhet and Williamson argue for separate authorship, "
                           "noting differences in vocabulary, theology (Chronicles is more inclusive; "
                           "Ezra emphasizes separation), and attitude toward the north. The Aramaic "
                           "documents in Ezra 4-7 are widely regarded as authentic Persian-period "
                           "correspondence, though some scholars debate whether they have been edited "
                           "or expanded. The order of Ezra's and Nehemiah's missions is debated: the "
                           "traditional chronology places Ezra first (458 BC) and Nehemiah second "
                           "(445 BC), but some scholars reverse or overlap them.",

        "bottom_line": "Ezra contains a core of authentic memoir material and genuine Persian "
                       "documents, compiled into a narrative of restoration. Whether Ezra himself "
                       "compiled the final book or an editor assembled his memoir with other sources, "
                       "the text provides a firsthand window into the post-exilic community's "
                       "struggle to rebuild its identity around Torah, temple, and covenant."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events span ~538-458 BC. Ezra's mission to Jerusalem is dated to "
                       "the seventh year of Artaxerxes (Ezra 7:7-8), which is 458 BC if this is "
                       "Artaxerxes I, or 398 BC if Artaxerxes II.",
        "critical_range": "The events in Ezra 1-6 (the first return under Sheshbazzar/Zerubbabel "
                         "and the temple rebuilding) span ~538-516 BC. Ezra's own mission (chs. 7-10) "
                         "occurs in 458 BC (traditional date). The final compilation of the book "
                         "likely dates to the late 5th or 4th century BC.",
        "evidence": "The Aramaic documents in Ezra are linguistically consistent with Imperial "
                    "Aramaic of the Persian period, as confirmed by comparison with other Aramaic "
                    "texts from Elephantine (Egypt) and Wadi Daliyeh. Persian administrative terms "
                    "and governmental procedures described in the book match what is known from "
                    "Persian-period sources. The Cyrus Cylinder confirms the general policy of "
                    "allowing displaced peoples to return and rebuild their temples."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The post-exilic Jewish community in Jerusalem and the diaspora -- "
                            "people who needed to understand their community's origins and legal "
                            "standing, the legitimacy of the Second Temple, and the authority of "
                            "Torah as the community's constitution.",

        "purpose": "Ezra serves three purposes: (1) HISTORICAL -- documenting the return from "
                   "exile and the rebuilding of the temple, establishing the legal and historical "
                   "basis for the post-exilic community; (2) THEOLOGICAL -- demonstrating that "
                   "YHWH fulfilled his promise through Jeremiah (the 70-year exile) and through "
                   "Isaiah (Cyrus as his instrument), proving his faithfulness; (3) PRACTICAL -- "
                   "establishing Torah as the authoritative basis for community life, replacing "
                   "the monarchy with covenant obedience as the organizing principle of Israel.",

        "theological_intent": "The theology of Ezra centers on the concept of holy separation "
                             "(havdalah/qadosh): the returned community must separate from the peoples "
                             "of the land to maintain covenant purity. The intermarriage crisis (chs. 9-10) "
                             "is not mere ethnocentrism but covenant theology: intermarriage with idolatrous "
                             "peoples was the sin that led to exile in the first place. Ezra's grief over "
                             "intermarriage parallels YHWH's grief over Israel's unfaithfulness."
    },

    # -- ORIGINAL LANGUAGE ------------------------------------------------------
    "language": {
        "original": "Hebrew and Aramaic (bilingual)",
        "script": "Aramaic square script",
        "linguistic_notes": "Ezra is one of only two OT books written partly in Aramaic (the other "
                           "is Daniel). Ezra 4:8-6:18 and 7:12-26 are in Imperial (Official) Aramaic, "
                           "the administrative language of the Persian Empire. The Hebrew sections are "
                           "in Late Biblical Hebrew, consistent with the post-exilic period. The Aramaic "
                           "portions include official correspondence and decrees that may preserve the "
                           "actual language of the Persian chancery. The bilingual nature of the book "
                           "reflects the bilingual reality of post-exilic Judah: Hebrew for sacred "
                           "literature and liturgy, Aramaic for administration and daily life.",
        "grammar_match": "The Aramaic is consistent with other Imperial Aramaic texts from the "
                        "Persian period (Elephantine Papyri, Wadi Daliyeh documents). The Hebrew "
                        "matches other Late Biblical Hebrew compositions."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Ezra IS scripture -- it documents the fulfillment of prophetic promises and "
                   "establishes the legal and theological framework for the post-exilic community.",
        "nt_usage": "The New Testament does not directly quote Ezra but presupposes its theology. "
                    "The temple restored in Ezra is the temple Jesus knows. The Torah authority Ezra "
                    "establishes is the same Torah authority Jesus and the Pharisees debate. The "
                    "separation theology of Ezra anticipates the NT's concern with holiness and "
                    "sanctification (2 Cor 6:14-18 echoes Ezra's logic). Jesus' genealogy in Matthew "
                    "traces through the post-exilic period that Ezra documents.",
        "internal_consistency": "Ezra picks up directly from 2 Chronicles 36:22-23 (Cyrus's decree). "
                               "It fulfills Jeremiah's 70-year prophecy (Jer 25:11-12; 29:10) and "
                               "Isaiah's Cyrus prophecy (Isa 44:28-45:1). It connects to Haggai and "
                               "Zechariah, who prophesied during the temple rebuilding (Ezra 5:1-2)."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragment 4QEzra (~50 BC), preserving small portions of "
                    "the text in Hebrew.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew/Aramaic text of Ezra."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC",
             "note": "The LXX includes Ezra within 'Esdras B.' The Greek translation is generally "
                     "reliable but shows some interpretive adjustments."},
            {"name": "1 Esdras", "date": "2nd-1st century BC",
             "note": "An alternative Greek version that overlaps with Ezra but includes additional "
                     "material (the 'Debate of the Three Guardsmen'). Its relationship to canonical "
                     "Ezra is debated."},
            {"name": "Dead Sea Scrolls", "date": "4QEzra, ~50 BC",
             "note": "Small fragments consistent with the MT tradition."}
        ],
        "reliability": "The text of Ezra is well-preserved. The Aramaic sections have been "
                       "confirmed as linguistically authentic to the Persian period by comparison "
                       "with other Aramaic documents from the same era."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------------
    "historical_context": {
        "setting": "Ezra spans from Cyrus's decree (538 BC) to Ezra's reforms (458 BC) -- "
                   "approximately 80 years of Persian-period history. The setting is the Persian "
                   "province of Yehud (Judah), centered on Jerusalem and the rebuilt temple.",

        "geography": "The key locations are Babylon (where the exiles live), the route from "
                     "Babylon to Jerusalem (Ezra's journey in ch. 8), and Jerusalem itself, "
                     "specifically the temple mount. The Ahava Canal (8:21) is a waypoint on "
                     "the journey where Ezra assembles his caravan.",

        "historical_connections": "The Cyrus Cylinder (539 BC) confirms Cyrus's policy of restoring "
                                 "displaced peoples. The Elephantine Papyri (5th century BC) from a "
                                 "Jewish military colony in Egypt mention the temple in Jerusalem and "
                                 "Persian administrative involvement in Jewish religious affairs -- "
                                 "exactly the world Ezra describes. The Murashu Archive (Nippur, 5th "
                                 "century BC) documents Jewish families living and doing business in "
                                 "Babylonia during this period."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "low-moderate",
        "summary": "Ezra does not contain explicit divine council scenes but operates within the "
                   "divine council's governance framework. YHWH 'stirred up the spirit (ruach) of "
                   "Cyrus king of Persia' (1:1) -- the same language used for divine council "
                   "influence on human rulers (cf. 1 Chr 5:26; 2 Chr 21:16). The hand of God "
                   "'upon' Ezra (7:6, 9, 28; 8:18, 22, 31) suggests divine council protection "
                   "and direction -- the invisible heavenly administration acting through a human "
                   "agent. The opposition to the temple rebuilding (Ezra 4) has overtones of "
                   "territorial spiritual conflict: the 'peoples of the land' who oppose the "
                   "rebuilding may include those under the influence of the territorial spirits "
                   "allotted to the nations at Babel (Deut 32:8-9). The restoration of temple "
                   "worship is a reassertion of YHWH's kingship in a land where rival spiritual "
                   "powers have held sway during the exile.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 27 (the restoration and divine council geography)",
            "Supernatural, chapter 17 (the cosmic significance of temple restoration)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "context",
            "title": "The Intermarriage Crisis in Context",
            "body": "Ezra 9-10 records the forced dissolution of marriages between returned "
                    "exiles and 'peoples of the lands.' Modern readers often find this deeply "
                    "troubling. Context is essential: the concern is not ethnic but covenantal. "
                    "Deuteronomy 7:3-4 prohibited intermarriage with specific Canaanite peoples "
                    "because 'they would turn away your sons from following me, to serve other "
                    "gods.' The post-exilic community had just returned from an exile CAUSED by "
                    "exactly this pattern (Solomon's foreign wives led him to worship other gods, "
                    "1 Kings 11). Ezra's reforms aim to prevent repeating the cycle. This is not "
                    "a universal prohibition of interethnic marriage (Ruth the Moabite is an "
                    "ancestor of David and Jesus) but a specific covenantal safeguard in a "
                    "moment of extreme vulnerability."
        },
        {
            "type": "scholarship",
            "title": "The Aramaic Documents: Authentic or Literary?",
            "body": "Ezra contains several Aramaic documents purporting to be official Persian "
                    "correspondence (4:11-16, 17-22; 5:7-17; 6:2-12; 7:12-26). Their authenticity "
                    "has been debated since the 19th century. The linguistic evidence strongly "
                    "favors authenticity: the Aramaic is Imperial (Official) Aramaic consistent "
                    "with Persian-period administrative language, the bureaucratic formulas match "
                    "known Persian practices, and the Persian governmental titles are accurate. "
                    "Even scholars who question specific details generally accept that these "
                    "documents reflect genuine Persian-period correspondence."
        }
    ]
}
