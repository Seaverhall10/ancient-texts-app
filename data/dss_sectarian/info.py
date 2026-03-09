"""
info.py — Dead Sea Scrolls Sectarian Texts: Scholarly Text Introduction

Honest scholarly introduction to the texts produced BY the Qumran community —
the rule books, hymns, war plans, and theological treatises of the Yahad,
the Jewish sect that preserved the Dead Sea Scrolls.
"""

TEXT_INFO = {
    "text_id": "dss_sectarian",
    "display_name": "Dead Sea Scrolls — Sectarian Texts",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "non-canonical",
        "label": "Non-Canonical — Dead Sea Scrolls (Sectarian Compositions)",
        "detail": "The sectarian Dead Sea Scrolls are not part of any Christian or Jewish canon. "
                  "They were never considered scripture by any tradition — they are the internal "
                  "documents of a specific Jewish community. This is an important distinction from "
                  "texts like 1 Enoch and Jubilees, which the Qumran community copied and "
                  "preserved but did not compose. The sectarian texts were PRODUCED by the Yahad "
                  "community itself: their rules for communal life, their hymns, their plans for "
                  "the eschatological war, their legal interpretations, and their angelic liturgy. "
                  "Their value is not as competing scripture but as a window into how one devout "
                  "Jewish community — contemporaneous with Jesus and the New Testament authors — "
                  "read, interpreted, and applied the Hebrew Bible."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "Several of the sectarian texts reference a figure called the 'Teacher of "
                       "Righteousness' (moreh ha-tsedeq) — the community's founding leader who is "
                       "portrayed as receiving divine insight into the meaning of the prophets. The "
                       "Hodayot (Thanksgiving Hymns) may include compositions by the Teacher himself. "
                       "The Damascus Document describes the community's origins: God raised up the "
                       "Teacher of Righteousness 'to lead them in the way of His heart' (CD I.11). "
                       "The identity of this Teacher is unknown — he is never named.",

        "scholarly_debate": "The sectarian texts were composed by multiple authors over approximately "
                           "two centuries (~150 BC to 68 AD). The Community Rule (1QS) likely evolved "
                           "through multiple editions — the Cave 4 copies (4QS manuscripts) show "
                           "variant versions, suggesting the text was a living document that was "
                           "revised as the community's practices changed. The War Scroll (1QM) may "
                           "draw on earlier military traditions. The Hodayot (1QHa) contain two types "
                           "of hymns: 'Teacher Hymns' with a distinctive first-person voice (possibly "
                           "by the Teacher of Righteousness) and 'Community Hymns' with more generic "
                           "piety. The Songs of Sabbath Sacrifice show connections to later Jewish "
                           "mysticism (merkabah tradition). The Temple Scroll (11Q19) presents itself "
                           "as God speaking directly in first person — a bold literary move that "
                           "effectively rewrites Deuteronomy.\n\n"
                           "The prevailing scholarly consensus (following de Vaux, Cross, VanderKam) "
                           "identifies the community as Essenes — matching Josephus's and Philo's "
                           "descriptions of a separatist Jewish sect practicing communal property, "
                           "ritual purity, and eschatological expectation. A minority of scholars "
                           "(Schiffman) argues for a Sadducean origin based on halakhic parallels.",

        "bottom_line": "These texts were written by the members and leaders of a sectarian Jewish "
                       "community over roughly two centuries. No single author stands behind the "
                       "collection. The Teacher of Righteousness was the founding figure, but most "
                       "texts are anonymous community products that evolved over time. They represent "
                       "the living theology of a real community — not abstract literary exercises."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "The texts themselves do not claim ancient authorship (unlike 1 Enoch or "
                       "Jubilees). The Damascus Document traces the community's origins to '390 "
                       "years after Nebuchadnezzar' (CD I.5-6), which would place the founding "
                       "around ~196 BC — though this number may be symbolic rather than precise.",
        "critical_range": "Composed between ~150 BC and 68 AD, when the Qumran settlement was "
                         "destroyed by the Romans during the First Jewish Revolt. The Community "
                         "Rule and Damascus Document are among the earliest compositions (~150-100 "
                         "BC). The War Scroll and Temple Scroll may date to the late 2nd or early "
                         "1st century BC. The Hodayot and pesharim span the community's entire "
                         "existence. Copying and revision continued until the community's end.",
        "evidence": "Dating relies on paleography (handwriting analysis), radiocarbon testing, "
                    "and archaeological context. The Qumran caves were sealed when the community "
                    "fled the Roman advance in 68 AD — providing a firm terminus ad quem. "
                    "Paleographic analysis of the scrolls spans from ~250 BC (the oldest biblical "
                    "manuscripts) to ~68 AD. The sectarian texts cluster between ~150 BC and 50 AD. "
                    "Carbon-14 testing of scroll material has broadly confirmed the paleographic "
                    "dates. The archaeological evidence at Khirbet Qumran (coins, pottery, "
                    "stratigraphy) shows occupation from ~130 BC to 68 AD with a gap during "
                    "Herod's reign (~31-4 BC, possibly due to earthquake damage)."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "The Yahad ('community' or 'unity') — a sectarian Jewish group that "
                            "separated from mainstream Judaism and the Jerusalem Temple establishment. "
                            "They considered themselves the true Israel, the 'Sons of Light,' the "
                            "remnant faithful to God's covenant. Most scholars identify them as "
                            "Essenes, the 'third sect' described by Josephus alongside the Pharisees "
                            "and Sadducees. They lived communally, practiced strict ritual purity, "
                            "shared property, and expected the imminent arrival of two messiahs — "
                            "a priestly Messiah of Aaron and a royal Messiah of Israel.",

        "purpose": "The sectarian texts served multiple functions within the community:\n\n"
                   "- COMMUNITY RULE (1QS): Constitution and initiation manual — how to join, "
                   "how to live, how to be disciplined, the annual covenant renewal ceremony.\n"
                   "- WAR SCROLL (1QM): Eschatological battle plan — detailed military organization "
                   "for the final war between the Sons of Light and the Sons of Darkness, led by "
                   "Michael against Belial.\n"
                   "- TEMPLE SCROLL (11Q19): An idealized Torah — how the Temple SHOULD be built "
                   "and operated, implicitly critiquing the current Jerusalem Temple.\n"
                   "- DAMASCUS DOCUMENT (CD): Community history and law — origins of the movement, "
                   "legal rulings, and regulations for members living outside Qumran ('camps').\n"
                   "- HODAYOT (1QHa): Community hymnbook — thanksgiving psalms for worship.\n"
                   "- SONGS OF SABBATH SACRIFICE (4Q400-407): Angelic liturgy — the community "
                   "worshipping alongside the angels in the heavenly temple.\n"
                   "- PESHARIM: Prophetic commentaries — reading Isaiah, Habakkuk, Nahum, and "
                   "the Psalms as speaking about the community's own situation.\n"
                   "- MELCHIZEDEK SCROLL (11Q13): Eschatological interpretation — Melchizedek as "
                   "a divine being who executes final judgment.",

        "theological_intent": "The sectarian texts express a community that believed it was living "
                             "in the last days. History was divided into the present 'dominion of "
                             "Belial' (the current evil age) and the coming 'dominion of God' (when "
                             "the messiahs would arrive, the wicked would be destroyed, and the "
                             "righteous would be vindicated). Their strict purity, communal discipline, "
                             "and intensive scripture study were preparation for this imminent "
                             "eschatological shift. They did not withdraw from the world out of "
                             "apathy — they withdrew to prepare for the final battle."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Hebrew for the vast majority of sectarian compositions. Some texts include "
                    "Aramaic portions. The Community Rule, War Scroll, Hodayot, Temple Scroll, "
                    "and pesharim are all in Hebrew.",
        "script": "Late Second Temple Hebrew script — the same Aramaic-derived square script used "
                  "for copying biblical manuscripts at Qumran. Some scrolls use a distinctive "
                  "'Qumran scribal practice' with specific orthographic conventions (e.g., "
                  "extended use of matres lectionis — vowel letters).",
        "linguistic_notes": "The Hebrew of the sectarian texts is a distinctive register sometimes "
                           "called 'Qumran Hebrew.' It blends biblical Hebrew (deliberate archaizing, "
                           "quotation of and allusion to scripture) with features of late Second Temple "
                           "Hebrew that anticipate Mishnaic Hebrew. The Hodayot's poetic Hebrew is "
                           "particularly rich, drawing heavily on the Psalms and Isaiah. The Temple "
                           "Scroll rewrites Deuteronomy in a Hebrew that closely imitates the "
                           "Pentateuchal style. The pesharim use a formulaic interpretive vocabulary: "
                           "'its interpretation concerns...' (pishro al).",
        "grammar_match": "The linguistic profile is consistent with Jewish Palestinian Hebrew of "
                        "the 2nd century BC through 1st century AD. It is neither biblical Hebrew "
                        "frozen in time nor yet Mishnaic Hebrew — it occupies the transitional "
                        "space between them, exactly as expected for texts of this period and "
                        "provenance."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "These are not competing scripture — they are a community's interpretation and "
                   "application of canonical scripture. They illuminate how the Hebrew Bible was "
                   "read in the generation before Jesus, even when the specific interpretations "
                   "are sectarian or idiosyncratic.",

        "where_it_aligns": [
            "The Two Spirits doctrine (1QS III.13-IV.26) develops the cosmic dualism that is "
            "implicit in Genesis 1-3, the conflict between YHWH and the nations' gods in the "
            "prophets, and the eschatological battle in Daniel. The New Testament inherits this "
            "light/darkness framework (John 1:5, 3:19-21; 2 Corinthians 6:14; Ephesians 5:8-11).",
            "The War Scroll's portrayal of Michael leading angelic armies against the forces of "
            "evil is consistent with Daniel 10:13, 10:21, 12:1, and Revelation 12:7-9.",
            "The pesher interpretation of the prophets — reading Habakkuk, Isaiah, and the Psalms "
            "as speaking about current events — uses the same hermeneutic that the New Testament "
            "applies (e.g., Matthew's fulfillment quotations, Peter's sermon in Acts 2).",
            "The Melchizedek Scroll (11Q13) identifies Melchizedek as an elohim who executes "
            "divine judgment — consistent with Psalm 82's portrayal of divine beings judging the "
            "nations and with Hebrews 7's treatment of Melchizedek as a figure greater than Abraham.",
            "The expectation of two messiahs (priestly and royal) reflects genuine biblical "
            "categories — the distinction between priestly and royal anointed figures runs through "
            "the Old Testament (Zechariah 4:14, 'the two anointed ones').",
            "The Damascus Document (CD II.17-III.1) explicitly references the Watchers tradition, "
            "confirming that this reading of Genesis 6:1-4 was standard in the community."
        ],

        "where_it_diverges": [
            "The extreme sectarian exclusivism — only members of the Yahad are 'Sons of Light,' "
            "everyone else is under Belial — goes beyond the canonical prophets' vision. Isaiah "
            "envisions nations streaming to Zion (Isaiah 2:2-4), not being consigned to darkness.",
            "The pesher method, while theologically creative, sometimes forces the prophetic text "
            "into meanings the original authors could not have intended. The Habakkuk Pesher reads "
            "the 'Chaldeans' as the Romans — a valid typological move, but the specific "
            "identifications of the 'Wicked Priest' and 'Man of the Lie' are sectarian claims, "
            "not revealed interpretation.",
            "The Temple Scroll's extensive rewriting of Torah in God's first-person voice is a bold "
            "literary claim that effectively creates new Torah legislation. No canonical tradition "
            "supports these additions.",
            "The 364-day solar calendar (shared with Jubilees and 1 Enoch) conflicts with the "
            "lunisolar calendar of the canonical Torah's festival system.",
            "The rigid determinism of the Two Spirits doctrine — that God created humans with "
            "predetermined portions of light and darkness — is in tension with the biblical "
            "emphasis on genuine human choice and responsibility (Deuteronomy 30:19, Joshua 24:15)."
        ],

        "reader_guidance": "The sectarian scrolls are not scripture and do not claim to be (with the "
                          "partial exception of the Temple Scroll). They are the working documents of "
                          "a real community trying to live faithfully before God in a turbulent time. "
                          "Their greatest value is showing us how the Hebrew Bible was read, "
                          "interpreted, and applied in the century before Jesus. Where their "
                          "interpretations align with the New Testament's reading of the Old "
                          "Testament, they illuminate the shared Jewish context. Where they diverge, "
                          "they remind us that the Qumran community — for all its devotion — was one "
                          "voice among many in Second Temple Judaism, not the definitive voice."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "The manuscripts ARE the earliest (and in most cases only) witnesses — these "
                    "texts were not transmitted through later copying traditions like the biblical "
                    "manuscripts. They were written at Qumran, deposited in caves, and discovered "
                    "in 1947-1956. What we have is what was found.",
        "major_witnesses": [
            {"name": "Community Rule (1QS)", "date": "~100-75 BC (this copy); text composed ~150-130 BC",
             "note": "The 'constitution' of the Yahad. Found in Cave 1. 11 columns on a single "
                     "scroll. Additional copies from Cave 4 (4QS^a-j) show the text evolved over "
                     "time — some copies lack the Two Spirits section, suggesting it was added later. "
                     "Contains the foundational Two Spirits doctrine (III.13-IV.26)."},
            {"name": "War Scroll (1QM)", "date": "~50 BC - 25 AD (this copy); composed late 2nd-early 1st century BC",
             "note": "Eschatological battle plan for the 40-year war between the Sons of Light and "
                     "the Sons of Darkness. Found in Cave 1. 19 columns. Additional fragments from "
                     "Cave 4 (4Q491-497) show variant recensions. Michael leads the angelic host; "
                     "Belial leads the forces of darkness."},
            {"name": "Temple Scroll (11Q19)", "date": "~25 BC (this copy); composed late 2nd century BC",
             "note": "The longest Dead Sea Scroll (66+ columns, over 28 feet). Found in Cave 11. "
                     "Rewrites Deuteronomy and Leviticus in God's first-person voice, prescribing "
                     "an idealized Temple and festival calendar. A second copy (11Q20) confirms the "
                     "text was valued."},
            {"name": "Damascus Document (CD)", "date": "~75-50 BC (Qumran copies); composed ~100 BC",
             "note": "Two medieval copies had been found in the Cairo Genizah in 1896 (CD^A and CD^B) "
                     "before fragments turned up at Qumran (4Q266-273, 5Q12, 6Q15). The Cairo copies "
                     "provide extensive text. Combines community history, legal rulings, and "
                     "regulations for 'camps' outside Qumran. Explicitly references the Watchers "
                     "tradition (CD II.17-III.1) and cites Jubilees by name (CD XVI.3-4)."},
            {"name": "Hodayot / Thanksgiving Hymns (1QHa)", "date": "~50-1 BC (this copy); composed over decades",
             "note": "Collection of approximately 25-30 hymns modeled on the biblical Psalms. Found "
                     "in Cave 1 (badly deteriorated). The 'Teacher Hymns' (cols. X-XVII) feature a "
                     "distinctive first-person voice of suffering and vindication that may reflect "
                     "the Teacher of Righteousness's own experience."},
            {"name": "Songs of Sabbath Sacrifice (4Q400-407, 11Q17, Masada fragment)",
             "date": "~75-50 BC (oldest Qumran copy); composed ~150-100 BC",
             "note": "Angelic liturgy for 13 Sabbaths — the community worshipping alongside angelic "
                     "priests in the heavenly temple. Found at both Qumran AND Masada, proving wider "
                     "circulation beyond the Yahad. Important for understanding the 'heavenly worship' "
                     "tradition that appears in Hebrews, Revelation, and later Jewish mysticism."},
            {"name": "Melchizedek Scroll (11Q13)", "date": "~75-50 BC (this copy); composed 1st century BC",
             "note": "13 fragments of a single column. Identifies Melchizedek as an elohim figure "
                     "who executes the Day of Atonement judgment described in Leviticus 25 and the "
                     "jubilee release of Isaiah 61. Applies Psalm 82:1 ('God [elohim] stands in the "
                     "divine assembly') to Melchizedek. Crucial for Heiser's divine council reading "
                     "of Psalm 82 and for understanding Hebrews 7."}
        ],
        "reliability": "For the sectarian texts, 'reliability' means something different than for "
                       "biblical manuscripts. We are not comparing across centuries of copying — we "
                       "have the original community's own manuscripts. The question is completeness: "
                       "many scrolls are fragmentary (damaged by time, moisture, and insects over "
                       "2,000 years in desert caves). The Cave 1 scrolls are generally well-preserved; "
                       "the Cave 4 materials are often highly fragmentary (tens of thousands of "
                       "fragments requiring decades of jigsaw-puzzle reconstruction). Where multiple "
                       "copies of the same text exist (e.g., Community Rule, War Scroll), they show "
                       "that these were living documents subject to revision — not frozen texts "
                       "transmitted verbatim."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "The Qumran community existed from approximately 150 BC to 68 AD — spanning "
                   "the late Hasmonean period, the Roman conquest of Judea (63 BC), Herod's reign "
                   "(37-4 BC), and the early Roman provincial period up to the First Jewish Revolt "
                   "(66-73 AD). The community settled at Khirbet Qumran on the northwestern shore "
                   "of the Dead Sea, a remote and arid location chosen deliberately for its "
                   "separation from the corrupted Jerusalem establishment. They believed the "
                   "Jerusalem Temple had been defiled by an illegitimate priesthood (the Hasmoneans "
                   "who combined kingship and priesthood, violating the Torah's separation of offices) "
                   "and that the Temple's calendar was wrong.",

        "geography": "Khirbet Qumran sits on a marl terrace overlooking the Dead Sea in the Judean "
                     "desert, about 1.5 km from the shore and roughly 13 km south of Jericho. The "
                     "site includes a main building complex (communal rooms, scriptorium, cisterns, "
                     "mikvaot/ritual baths) and the surrounding caves (11 caves yielded scrolls). "
                     "The settlement is connected to the Ein Feshkha spring to the south. The "
                     "deliberate isolation — desert, cliffs, Dead Sea — reflects the community's "
                     "self-understanding as the 'wilderness' people of Isaiah 40:3: 'In the "
                     "wilderness prepare the way of the LORD.' The Damascus Document also references "
                     "community members in 'camps' throughout Palestine, suggesting the movement "
                     "extended beyond Qumran itself.",

        "historical_connections": "The sectarian scrolls illuminate the world of the New Testament "
                                 "in extraordinary ways: (1) The eschatological urgency — expectation "
                                 "of imminent divine intervention, messianic figures, final judgment "
                                 "— is the same atmosphere in which John the Baptist and Jesus "
                                 "appeared. (2) The dualistic language (light vs. darkness, truth vs. "
                                 "falsehood, Spirit of Truth vs. Spirit of Error) echoes prominently "
                                 "in John's Gospel and 1 John. (3) The communal meals, communal "
                                 "property, and water purification rituals parallel early church "
                                 "practices (Acts 2:44-47). (4) The pesher hermeneutic — reading "
                                 "ancient prophecy as fulfilled in recent events — is precisely what "
                                 "the New Testament does with the Hebrew Bible. (5) The Two Messiahs "
                                 "expectation (priestly and royal) may illuminate why the New Testament "
                                 "insists that Jesus fulfills BOTH roles (Hebrews 7-10: priest after "
                                 "Melchizedek's order; the Gospels: son of David, king of Israel). "
                                 "None of this means Jesus was an Essene or that Christianity derived "
                                 "from Qumran — but it does mean both movements breathed the same "
                                 "theological air."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "high",
        "summary": "The sectarian scrolls provide critical evidence for how Second Temple Jews "
                   "understood the divine council, cosmic warfare, and the role of spiritual beings "
                   "in human affairs. Key contributions to the Heiser framework:\n\n"
                   "(1) THE TWO SPIRITS DOCTRINE (1QS III.13-IV.26): God created two spirits to "
                   "govern humanity — the Prince of Light (also called the Angel of Truth) and the "
                   "Angel of Darkness (Belial). All humans walk in portions of both light and "
                   "darkness until the 'appointed end' when God will destroy evil forever. This "
                   "systematizes the cosmic dualism that Genesis implies (the serpent vs. God, Cain "
                   "vs. Abel, the Watchers vs. the faithful) into an explicit theological framework. "
                   "The New Testament inherits this exact language: 'children of light' and 'children "
                   "of darkness' (1 Thessalonians 5:5, Ephesians 5:8), the 'prince of this world' "
                   "(John 12:31, 14:30), and the 'spirit of truth' vs. 'spirit of error' "
                   "(1 John 4:6).\n\n"
                   "(2) THE WAR SCROLL AND MICHAEL (1QM): The eschatological battle pits Michael "
                   "and his angels against Belial and the 'army of his lot' — a cosmic war that "
                   "mirrors Daniel 10-12 and anticipates Revelation 12:7-9. The War Scroll makes "
                   "explicit what Daniel implies: the earthly conflict between nations is the visible "
                   "surface of an invisible war between divine council members. This is the "
                   "Deuteronomy 32 worldview in military form.\n\n"
                   "(3) THE MELCHIZEDEK SCROLL (11Q13): This is perhaps the most important single "
                   "text for Heiser's divine council thesis. It takes Psalm 82:1 — 'Elohim stands "
                   "in the assembly of El; in the midst of the elohim he judges' — and identifies "
                   "the presiding elohim as Melchizedek. This divine Melchizedek executes the Day "
                   "of Atonement judgment, the jubilee release, and the vengeance of Isaiah 61. "
                   "For Heiser, this proves that pre-Christian Judaism read Psalm 82 as describing "
                   "real divine beings (not human judges) and that at least one Jewish community "
                   "identified Melchizedek as a divine figure — exactly the theology Hebrews 7 "
                   "develops when it presents Jesus as 'a priest forever after the order of "
                   "Melchizedek.'\n\n"
                   "(4) THE WATCHERS IN THE DAMASCUS DOCUMENT (CD II.17-III.1): 'Because they "
                   "walked in the stubbornness of their hearts, the Watchers of heaven fell; on "
                   "account of it they were caught, because they did not keep the commandments of "
                   "God. And their sons, whose height was like the height of cedars... also fell.' "
                   "This shows that the Watchers reading of Genesis 6 was not fringe Enochic "
                   "speculation — it was accepted and applied by the broader sectarian community.\n\n"
                   "(5) THE SONGS OF SABBATH SACRIFICE (4Q400-407): The angelic liturgy describes "
                   "the heavenly temple, its angelic priests, and the worship before God's throne "
                   "in extraordinary detail. This is the divine council at worship — and it shows "
                   "that the Qumran community believed their earthly worship participated in the "
                   "heavenly liturgy. The parallels with Revelation 4-5 (heavenly throne room, "
                   "angelic worship, living creatures) and Hebrews 12:22-24 (the heavenly Jerusalem "
                   "with 'innumerable angels in festal gathering') are striking.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 4 (Psalm 82 and the divine council — 11Q13 is key evidence)",
            "The Unseen Realm, chapter 15 (cosmic warfare and the War Scroll's framework)",
            "Reversing Hermon, chapter 2 (the Watchers tradition in Second Temple Judaism — "
            "CD II.17-III.1 as corroboration)",
            "Supernatural, chapters 5-6 (the divine council in Jewish tradition)",
            "Angels (2018), discussion of the Two Spirits doctrine and angelic hierarchies",
            "The Naked Bible Podcast, episodes on Psalm 82 and Melchizedek (11Q13 extensively discussed)"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "A Window, Not a Mirror",
            "body": "The sectarian scrolls show us how one Jewish community read the Bible in the "
                    "generation before Jesus. They are a window into Second Temple thought — not a "
                    "mirror of our own theology. Their value is enormous: they demonstrate that the "
                    "divine council, cosmic warfare, and angelic hierarchy were mainstream Jewish "
                    "concepts (not later Christian inventions). But their specific sectarian "
                    "positions — calendar, purity laws, exclusivism, determinism — should not be "
                    "adopted uncritically. The New Testament emerged from the same theological "
                    "soil but drew very different conclusions on key points (Gentile inclusion, "
                    "Temple replacement, Jesus as the single Messiah fulfilling both priestly and "
                    "royal roles)."
        },
        {
            "type": "scholarship",
            "title": "The 'Essene Hypothesis' Debate",
            "body": "The majority of scholars identify the Qumran community as Essenes — the "
                    "'third sect' described by Josephus (Jewish War 2.119-161), Philo (Every Good "
                    "Man is Free 75-91), and Pliny (Natural History 5.73). The correspondence is "
                    "strong: celibacy (or restricted marriage), communal property, ritual immersion, "
                    "deterministic theology, and geographical location near the Dead Sea all match. "
                    "However, some scholars (notably Lawrence Schiffman) argue for Sadducean "
                    "connections based on halakhic parallels in 4QMMT. Others (Norman Golb) reject "
                    "the Qumran-sectarian connection entirely, proposing the scrolls were a Jerusalem "
                    "library cached during the Roman war. The Essene hypothesis remains dominant but "
                    "should be held with appropriate scholarly humility."
        },
        {
            "type": "interpretation",
            "title": "Pesher Is Not Prophecy",
            "body": "The Qumran pesharim (prophetic commentaries) read Habakkuk, Isaiah, Nahum, "
                    "and the Psalms as coded references to the community's own situation: the "
                    "'Wicked Priest' is their enemy, the 'Teacher of Righteousness' is their "
                    "founder, the 'Kittim' are the Romans. This is the same TYPE of hermeneutic "
                    "the New Testament uses (reading Old Testament prophecy as fulfilled in Jesus), "
                    "but the specific applications are different. The pesher method tells us HOW "
                    "Jews in this period read prophecy — as directly relevant to current events — "
                    "which is invaluable for understanding how Matthew, Paul, and Peter read the "
                    "same Hebrew Bible. But the Qumran identifications themselves (who is the "
                    "Wicked Priest? who are the Kittim?) are the community's own claims, not "
                    "inspired interpretation."
        },
        {
            "type": "warning",
            "title": "Jesus Was Not an Essene",
            "body": "The similarities between the scrolls and the New Testament have led some "
                    "popular writers to claim that Jesus was an Essene, that Christianity is "
                    "derivative of Qumran theology, or that the scrolls contain 'suppressed' "
                    "Christian teachings. None of these claims survive serious scrutiny. The "
                    "parallels (dualistic language, messianic expectation, communal meals, "
                    "eschatological urgency) reflect shared Jewish context, not direct dependence. "
                    "The differences are more striking than the similarities: Jesus ate with sinners "
                    "(the Yahad expelled them), welcomed Gentiles (the Yahad demonized them), "
                    "proclaimed himself the Messiah (the Yahad awaited two future messiahs), and "
                    "claimed to forgive sins (something no Qumran text imagines for any human "
                    "figure). The scrolls illuminate the world Jesus entered — they do not explain "
                    "him away."
        }
    ]
}
