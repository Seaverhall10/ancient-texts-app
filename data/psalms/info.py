"""
info.py — Psalms (Tehillim): Scholarly Text Introduction

This file provides the "front page" for Psalms in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Psalms is THE divine council book of the Old Testament. Psalm 82 portrays
YHWH standing in the divine assembly to judge the gods. Psalm 89 describes
YHWH's incomparability among the holy ones, the heavenly council's awe
before him, and the Davidic covenant established in the presence of the
council. Psalm 2 declares YHWH's anointed as his son, enthroned on Zion
against the raging nations and their rulers. Psalm 110 installs the Davidic
king as a priest forever after the order of Melchizedek, seated at YHWH's
right hand. No other book in the Bible provides such sustained, explicit
access to the operations of the divine council, the enthronement of YHWH's
king, and the cosmic scope of YHWH's rule over all spiritual powers.
"""

TEXT_INFO = {
    "text_id": "psalms",
    "display_name": "Psalms (Tehillim)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim)",
        "detail": "Psalms is the first book of the Writings (Ketuvim) in the Hebrew Bible and a "
                  "central book of the Christian Old Testament. It is universally canonical across all "
                  "Jewish and Christian traditions. The Psalter is the most frequently quoted Old "
                  "Testament book in the New Testament — cited or alluded to over 400 times. Jesus "
                  "himself quoted Psalms extensively: Psalm 22 from the cross ('My God, my God, why "
                  "have you forsaken me?'), Psalm 110:1 in his debate with the Pharisees about the "
                  "Messiah's identity ('The LORD said to my Lord'), Psalm 118:22-23 about the rejected "
                  "cornerstone, and Psalm 69:9 about zeal for God's house. Peter's Pentecost sermon "
                  "builds its christological argument on Psalms 16 and 110. Paul uses Psalms extensively "
                  "in Romans, Galatians, and Ephesians. Hebrews quotes Psalms 2, 8, 45, 95, 97, 102, "
                  "104, and 110 to establish Christ's superiority. Luke 24:44 records Jesus saying "
                  "'everything written about me in the Law of Moses and the Prophets and the Psalms "
                  "must be fulfilled' — placing Psalms as a distinct category of messianic witness. "
                  "The Psalter has been the prayer book and hymnal of both synagogue and church from "
                  "antiquity to the present."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Psalter is attributed to multiple authors through its superscriptions: "
                       "73 psalms are attributed to David (ledavid — 'of David' or 'for David' or "
                       "'belonging to the Davidic collection'), 12 to Asaph (a Levitical musician, "
                       "1 Chr 6:39), 11 to the Sons of Korah (a Levitical guild), 2 to Solomon "
                       "(Psalms 72, 127), 1 to Moses (Psalm 90), 1 to Heman the Ezrahite (Psalm 88), "
                       "1 to Ethan the Ezrahite (Psalm 89), and 50 are anonymous (sometimes called "
                       "'orphan psalms'). The Talmud (Bava Batra 14b-15a) credits David as the "
                       "primary compiler, stating he 'composed the Book of Psalms by the hand of ten "
                       "elders,' including Adam, Melchizedek, Abraham, Moses, Heman, Jeduthun, Asaph, "
                       "and the three sons of Korah. Jesus and the New Testament authors consistently "
                       "attribute psalms to David (Matt 22:43; Acts 2:25; 4:25; Rom 4:6; 11:9).",

        "scholarly_debate": "Critical scholarship recognizes the Psalter as an edited collection that "
                           "grew over centuries. The five-book structure (Book I: 1-41; Book II: 42-72; "
                           "Book III: 73-89; Book IV: 90-106; Book V: 107-150) is an editorial creation, "
                           "perhaps modeled on the five books of the Torah. Hermann Gunkel's form-critical "
                           "approach (1933) classified psalms by genre: hymns of praise, individual and "
                           "communal laments, royal psalms, enthronement psalms, wisdom psalms, and songs "
                           "of thanksgiving. Sigmund Mowinckel (1962) proposed that many psalms originated "
                           "in the cult, particularly an annual New Year enthronement festival. Gerald "
                           "Wilson's landmark study (1985) demonstrated that the Psalter's final shape "
                           "has a deliberate editorial theology: Books I-III trace the rise and fall of "
                           "the Davidic covenant (climaxing in the crisis of Psalm 89), and Books IV-V "
                           "respond by affirming YHWH's eternal kingship (Psalm 90: 'Lord, you have been "
                           "our dwelling place in all generations'). The superscriptions are treated by "
                           "some scholars as editorial additions, by others as authentic ancient tradition.",

        "bottom_line": "The Psalter is a collection spanning a millennium of Israelite worship — from "
                       "Moses (Psalm 90, ~1400 BC) to the post-exilic community (Psalm 137, after "
                       "586 BC). David is the dominant author and the theological center of the "
                       "collection: even psalms not by David are shaped by the Davidic covenant theology "
                       "that pervades the Psalter. The five-book structure and editorial arrangement "
                       "indicate intentional compilation, producing a unified theological work from "
                       "diverse sources. The royal and divine council psalms form the theological spine "
                       "of the collection."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Individual psalms range from Moses (~1400 BC, Psalm 90) to David (~1000 BC, "
                       "the bulk of the collection) to the exilic/post-exilic period (Psalm 137, after "
                       "586 BC). The collection was compiled over centuries, with final editing in the "
                       "post-exilic period.",
        "critical_range": "Individual psalms date from as early as the 12th-10th century BC (some Davidic "
                         "psalms, royal psalms) to the post-exilic period (5th-3rd century BC). The "
                         "five-book editorial structure was probably finalized in the Persian or early "
                         "Hellenistic period (~400-200 BC). The Dead Sea Scrolls reveal that the Psalter's "
                         "arrangement was not fully fixed by the 2nd century BC — the Great Psalms Scroll "
                         "(11QPsa) has a different arrangement for Psalms 90-150.",
        "evidence": "Key evidence includes: (1) The Great Psalms Scroll (11QPsa) from Qumran (~50 AD) "
                    "is the most important manuscript, containing 41 canonical psalms plus additional "
                    "compositions (including Psalm 151 and the 'Last Words of David') in an arrangement "
                    "different from the MT, suggesting the Psalter's final third was still fluid. "
                    "(2) Other DSS psalms manuscripts (4QPsa-q, etc.) show various arrangements, "
                    "particularly for Books IV-V. (3) The LXX includes Psalm 151 as canonical and "
                    "numbers several psalms differently (combining and splitting). (4) The royal psalms "
                    "(2, 18, 20, 21, 45, 72, 89, 101, 110, 132, 144) presuppose an active monarchy, "
                    "suggesting pre-exilic composition. (5) Ugaritic parallels (especially to Psalm 29, "
                    "with its storm-god imagery) suggest some psalms have roots in Late Bronze Age "
                    "Canaanite hymnography, adapted to YHWH worship."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Israel — the worshiping community, from the Davidic court to the Temple "
                            "congregation to the post-exilic synagogue. The Psalter served multiple "
                            "functions: royal liturgy (the enthronement and royal psalms), Temple worship "
                            "(the songs of ascent, the Hallelujah psalms), personal prayer (the individual "
                            "laments and thanksgivings), and theological instruction (the wisdom psalms, "
                            "the historical psalms). The editorial arrangement suggests the final Psalter "
                            "was intended for both liturgical use and private meditation — a 'Torah of "
                            "David' that complemented the Torah of Moses.",

        "purpose": "The Psalter teaches Israel how to speak to God and about God across every human "
                   "experience — praise, lament, thanksgiving, confession, rage, despair, wonder, and "
                   "worship. Its theological purposes include: (1) celebrating YHWH as Creator, King, "
                   "and Redeemer; (2) establishing the Davidic covenant as the channel of YHWH's "
                   "earthly rule; (3) processing the crisis of exile and the apparent failure of the "
                   "Davidic promise; (4) affirming YHWH's eternal kingship that transcends and "
                   "undergirds the Davidic covenant; (5) pointing forward to the messianic King who "
                   "will fulfill all the royal promises.",

        "theological_intent": "The Psalter's deepest theological contribution is its revelation of the "
                             "divine council and YHWH's cosmic kingship. The enthronement psalms (47, 93, "
                             "95-99) declare 'YHWH reigns!' over all creation, all nations, and all gods. "
                             "The royal psalms install David's son as YHWH's viceroy, seated at his right "
                             "hand (110:1), begotten as his son (2:7), and ruling from Zion (2:6). The "
                             "divine council psalms (82, 89) reveal the heavenly assembly where YHWH "
                             "judges the gods and is praised by the holy ones. The creation psalms (8, 19, "
                             "33, 104, 148) celebrate YHWH's sovereignty over the cosmos. The lament psalms "
                             "express the anguished faith of those who trust YHWH despite suffering — a "
                             "pattern that culminates in Christ's use of Psalm 22 from the cross."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew (with one Aramaic verse: Psalm 2:12 is debated; Psalm 139:20 "
                    "may contain Aramaic influence)",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "The Psalter spans the full range of Biblical Hebrew poetry from archaic "
                           "to late. Psalm 29 contains vocabulary and imagery paralleled in Ugaritic "
                           "Baal hymns, suggesting a very early composition or adaptation from Canaanite "
                           "hymnography. Psalm 68 is notoriously difficult, with archaic forms that "
                           "may date to the early monarchy. The acrostic psalms (9-10, 25, 34, 37, 111, "
                           "112, 119, 145) demonstrate sophisticated literary artistry. Psalm 119, the "
                           "longest chapter in the Bible (176 verses), is an eight-fold acrostic "
                           "celebrating the Torah. The poetic techniques include parallelism (synonymous, "
                           "antithetical, synthetic), chiasm, inclusio, staircase parallelism, and "
                           "extensive use of metaphor and imagery. The musical terminology in the "
                           "superscriptions (selah, mizmor, shir, maskil, miktam, lamnatseakh, "
                           "alamot, sheminit, gittit, etc.) preserves ancient liturgical performance "
                           "instructions whose exact meaning is often uncertain.",
        "grammar_match": "Hebrew poetry differs fundamentally from prose in its use of parallelism "
                        "rather than narrative sequence as the primary structuring device. Robert "
                        "Alter's work on biblical poetry has demonstrated that the 'second line' of "
                        "a parallel couplet typically intensifies, specifies, or extends the first — "
                        "not merely repeating it. The Psalms' language ranges from the intimate "
                        "(Psalm 23, 'YHWH is my shepherd') to the cosmic (Psalm 29, 'The voice of "
                        "YHWH breaks the cedars'), from the anguished (Psalm 88, the darkest psalm) "
                        "to the ecstatic (Psalm 150, the final Hallelujah)."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Psalms IS scripture — the most quoted Old Testament book in the New Testament "
                   "and the foundation of messianic theology.",
        "nt_usage": "Psalms is cited more than any other Old Testament book in the New Testament — "
                    "over 400 quotations and allusions. The most theologically significant include: "
                    "Psalm 2:7 ('You are my son; today I have begotten you') — applied to Jesus at "
                    "his baptism (Mark 1:11), in Paul's preaching (Acts 13:33), and in Hebrews "
                    "(1:5; 5:5). Psalm 110:1 ('The LORD said to my Lord, Sit at my right hand') — "
                    "the most quoted OT verse in the NT, used by Jesus (Matt 22:44), Peter (Acts "
                    "2:34-35), Paul (1 Cor 15:25), and Hebrews (1:13; 10:12-13). Psalm 22 — cited "
                    "by Jesus from the cross (Matt 27:46) and fulfilled in the crucifixion details "
                    "(pierced hands and feet, lots cast for garments, mocking bystanders). Psalm "
                    "16:8-11 — Peter's proof of the resurrection (Acts 2:25-28). Psalm 118:22 — "
                    "'the stone the builders rejected' applied to Jesus (Matt 21:42; Acts 4:11; "
                    "1 Pet 2:7). Psalm 45:6-7 — applied to Christ in Hebrews 1:8-9 ('Your throne, "
                    "O God, is forever and ever'). Psalm 82 — cited by Jesus in John 10:34 to "
                    "defend his claim to be the Son of God.",
        "internal_consistency": "The Psalter is deeply interconnected with the rest of scripture. The "
                               "royal psalms develop the Davidic covenant of 2 Samuel 7. The creation "
                               "psalms echo Genesis 1-2. The historical psalms (78, 105, 106, 135, 136) "
                               "retell the Exodus through Conquest narratives. The Torah psalms (1, 19, "
                               "119) celebrate the Mosaic covenant. The enthronement psalms declare the "
                               "kingship that the prophets will develop eschatologically. The lament "
                               "psalms express the theology of suffering that Job explores and that the "
                               "Servant Songs of Isaiah will transform. The Psalter is the Hebrew Bible's "
                               "internal commentary on itself."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "The Great Psalms Scroll (11QPsa) from Qumran Cave 11, dating to ~50 AD, is the "
                    "most important manuscript. It contains 41 canonical psalms (from Books IV-V) plus "
                    "additional compositions, in an arrangement different from the MT. Over 30 other "
                    "psalms manuscripts have been found at Qumran, making Psalms the most attested "
                    "biblical book in the Dead Sea Scrolls.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The MT preserves 150 psalms in the standard five-book arrangement. The "
                     "superscriptions are included in the verse numbering (so Psalm 3:1 in the MT "
                     "is the superscription, and what English Bibles call v. 1 is MT v. 2). The "
                     "MT numbering differs from the LXX in Psalms 9-147."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The LXX preserves 151 psalms (Psalm 151, a short psalm about David, is "
                     "also found at Qumran). The LXX combines MT Psalms 9-10 into one (LXX 9) and "
                     "splits MT Psalm 147 into two, creating a different numbering system that "
                     "persists in Catholic and Orthodox Bibles. The LXX superscriptions sometimes "
                     "differ from the MT, occasionally adding Davidic attributions."},
            {"name": "Dead Sea Scrolls (11QPsa)", "date": "~50 AD",
             "note": "The most important DSS manuscript for Psalms. Its different arrangement of "
                     "Psalms 90-150, including non-canonical compositions, has sparked major debate: "
                     "Peter Flint argued it represents an alternative authoritative Psalter; others "
                     "(like Ulrich) see it as a liturgical collection rather than a rival canon."},
            {"name": "Syriac Peshitta", "date": "2nd-3rd century AD",
             "note": "The Syriac Psalter generally follows the MT arrangement but includes "
                     "Psalm 151 and additional apocryphal psalms (Psalms 152-155). The Syriac "
                     "superscriptions often add historical or liturgical context not found in "
                     "the Hebrew or Greek."}
        ],
        "reliability": "Books I-III (Psalms 1-89) are remarkably stable across all witnesses — the "
                       "order and content are consistent in the MT, LXX, and DSS. Books IV-V (Psalms "
                       "90-150) show more variation in the DSS, suggesting the final arrangement was "
                       "not fixed until later. Individual psalm texts are generally well-preserved, "
                       "with most variants involving minor orthographic or grammatical differences. "
                       "The theologically crucial psalms (2, 22, 82, 89, 110) are stable across all "
                       "traditions."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "The Psalter spans Israel's entire history, from the Mosaic era (Psalm 90) through "
                   "the monarchy (the Davidic psalms), the exile (Psalm 137, 'By the rivers of Babylon'), "
                   "and the post-exilic restoration. The primary institutional setting is the Jerusalem "
                   "Temple — many psalms were composed for Temple liturgy, including the Songs of Ascent "
                   "(120-134, sung by pilgrims ascending to Jerusalem), the Hallel psalms (113-118, sung "
                   "at Passover — the 'hymn' Jesus and his disciples sang after the Last Supper, "
                   "Matt 26:30), and the Hallelujah psalms (146-150, the final doxology).",

        "geography": "The Psalter's geography centers on Zion/Jerusalem — the cosmic mountain, YHWH's "
                     "earthly dwelling, the 'joy of the whole earth' (48:2). But it ranges widely: "
                     "the wilderness of Judah (63), the Jordan and Mount Hermon (42:6), Lebanon's "
                     "cedars (29; 92:12), the seas and rivers (93; 104), Bashan (68:15), Sinai/Horeb "
                     "(68:8, 17), Egypt and the Red Sea (78; 106; 136), and Babylon (137). The cosmic "
                     "geography is equally important: the heavens (19; 104), the deep (107), Sheol "
                     "(6:5; 16:10; 88:3-6), and the divine council's assembly hall (82:1; 89:5-7).",

        "historical_connections": "The Psalms' superscriptions link specific psalms to historical "
                                 "events: Psalm 3 (David fleeing Absalom), Psalm 51 (David after the "
                                 "Bathsheba affair), Psalm 56 (David among the Philistines at Gath), "
                                 "Psalm 63 (David in the wilderness of Judah). While some scholars "
                                 "treat these as editorial additions, they preserve ancient tradition "
                                 "about the psalms' origins. The royal psalms (2, 18, 20, 21, 45, 72, "
                                 "89, 101, 110, 132, 144) reflect the pre-exilic monarchy's liturgical "
                                 "practices. The Ugaritic parallels to Psalm 29 (the 'voice of YHWH' "
                                 "hymn) connect Israelite psalmody to broader Canaanite literary culture."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Psalms is the single most important book in the Bible for understanding the "
                   "divine council. It contains the explicit council scenes, the enthronement decrees, "
                   "the judgment of the gods, and the messianic installation that form the backbone "
                   "of divine council theology."
                   "\n\n"
                   "PSALM 82 — JUDGMENT OF THE GODS: 'God (Elohim) stands in the divine assembly "
                   "(adat el); in the midst of the gods (elohim) he renders judgment' (82:1). This "
                   "is the foundational divine council text. YHWH presides over the assembly of the "
                   "sons of God — the spiritual beings allotted authority over the nations at Babel "
                   "(Deut 32:8-9). He indicts them for corrupt governance: 'How long will you judge "
                   "unjustly and show partiality to the wicked?' (82:2). They were supposed to "
                   "administer justice among the nations but instead allowed oppression and darkness. "
                   "YHWH's sentence: 'I said, \"You are gods (elohim), sons of the Most High (bene "
                   "elyon), all of you; nevertheless, like men you shall die, and fall like any "
                   "prince\"' (82:6-7). The gods who ruled the nations are judged and sentenced to "
                   "mortality. The psalm concludes with a plea: 'Arise, O God (Elohim), judge the "
                   "earth! For you shall inherit all the nations!' (82:8) — the eschatological "
                   "reclamation of all nations from the corrupt spiritual rulers. Jesus quotes "
                   "Psalm 82:6 in John 10:34 in his most direct engagement with divine council "
                   "theology."
                   "\n\n"
                   "PSALM 89 — THE COUNCIL AND THE COVENANT: Psalm 89 contains the most extensive "
                   "divine council description in the Psalter. 'The heavens praise your wonders, "
                   "O YHWH, your faithfulness in the assembly of the holy ones (qehal qedoshim). "
                   "For who in the skies can be compared to YHWH? Who among the sons of God (bene "
                   "elim) is like YHWH? God is greatly to be feared in the council (sod) of the "
                   "holy ones (qedoshim), and awesome above all who are around him' (89:5-7). The "
                   "psalm then moves from the heavenly council to the Davidic covenant: YHWH has "
                   "chosen David, anointed him, established his throne, and declared 'He shall cry "
                   "to me, \"You are my Father, my God, and the Rock of my salvation.\" And I will "
                   "make him the firstborn, the highest of the kings of the earth' (89:26-27). The "
                   "juxtaposition is deliberate: the Davidic king is installed by the same council "
                   "that governs the cosmos. But the psalm ends in crisis: the covenant seems broken, "
                   "the crown defiled, the throne cast down (89:38-51). This crisis drives the "
                   "Psalter's final answer: YHWH himself is king (Psalms 93-99), and the ultimate "
                   "Son of David will resolve the apparent failure."
                   "\n\n"
                   "PSALM 2 — THE SON'S ENTHRONEMENT: 'Why do the nations rage and the peoples "
                   "plot in vain? The kings of the earth set themselves, and the rulers take counsel "
                   "together, against YHWH and against his Anointed (Meshiakho)' (2:1-2). The "
                   "nations' rebellion against YHWH and his king is the Deuteronomy 32 worldview in "
                   "motion — the gods of the nations incite their peoples against YHWH's authority. "
                   "YHWH's response: 'I have set my King on Zion, my holy hill' (2:6). The decree "
                   "of installation: 'You are my Son; today I have begotten you. Ask of me, and I "
                   "will make the nations your heritage, and the ends of the earth your possession' "
                   "(2:7-8). This is the reversal of Deuteronomy 32:8-9: the nations allotted to "
                   "the sons of God will become the inheritance of YHWH's Son — the Davidic king, "
                   "ultimately the Messiah."
                   "\n\n"
                   "PSALM 110 — THE PRIEST-KING AT YHWH'S RIGHT HAND: 'YHWH says to my Lord: "
                   "\"Sit at my right hand, until I make your enemies your footstool\"' (110:1). "
                   "David writes of someone he calls 'my Lord' (adoni) who is invited to sit at "
                   "YHWH's right hand — the position of supreme authority in the divine council. "
                   "This figure is also 'a priest forever after the order of Melchizedek' (110:4) — "
                   "combining royal and priestly functions in a way that the Mosaic covenant kept "
                   "separate. Melchizedek, the priest-king of Salem (Jerusalem) who blessed Abraham "
                   "(Gen 14:18-20), becomes the type of a priesthood that transcends the Levitical "
                   "order. Hebrews 5-7 builds its entire christological argument on this psalm. "
                   "Jesus uses 110:1 to demonstrate that the Messiah is not merely David's descendant "
                   "but David's Lord — a divine figure who shares YHWH's throne (Matt 22:41-46).",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 1-3 (Psalm 82 — the foundational divine council text)",
            "The Unseen Realm, chapter 4-5 (the 'two powers in heaven' — Psalm 110 and the second YHWH)",
            "The Unseen Realm, chapter 24-25 (Psalm 2 — the Son's enthronement and the nations)",
            "The Unseen Realm, chapter 13-14 (Psalm 82 and Deuteronomy 32 — the worldview)",
            "Supernatural, chapter 3-4 (the divine council in Psalms)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 2-4 (the council scenes in Psalms)",
            "The Naked Bible Podcast, episode 1 (Psalm 82 — Heiser's starting point)",
            "The Naked Bible Podcast, episode 109 (Psalm 89 — the council and the covenant)",
            "The Naked Bible Podcast, episode 173 (Psalm 110 and Melchizedek)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "Psalm 82 — The Judgment of the Gods",
            "body": "Psalm 82 is the single most important text for understanding the divine council "
                    "worldview. Michael Heiser's entire scholarly career was catalyzed by this psalm. "
                    "The key interpretive question is: who are the 'elohim' in 82:1, 6? Three main "
                    "views exist: (1) Human judges — the traditional rabbinic and some patristic view. "
                    "This fails because human judges were never called 'sons of the Most High' or "
                    "sentenced to 'die like men' (they already are men). (2) The gods of the nations — "
                    "Heiser's view, supported by the Deuteronomy 32 worldview: these are the divine "
                    "beings placed over the nations at Babel who have corrupted their rule and are now "
                    "sentenced to lose their immortality. (3) Demythologized ANE language — merely "
                    "poetic imagery without ontological claims. This fails to account for Jesus' "
                    "quotation in John 10:34, where he treats the psalm's claim about 'gods' as "
                    "authoritative. The divine council reading makes the best sense of the context, "
                    "the Deuteronomy 32 background, and Jesus' use of the passage."
        },
        {
            "type": "interpretation",
            "title": "Psalm 110 — The Most Quoted Verse in the New Testament",
            "body": "Psalm 110:1 is quoted or alluded to more than any other Old Testament verse in "
                    "the New Testament. Its theological significance is immense: David writes of 'my "
                    "Lord' (adoni) who is invited by YHWH to share his throne. In Jesus' argument "
                    "(Matt 22:41-46), this creates an insoluble puzzle for a merely human Messiah: "
                    "how can David's descendant be David's Lord? The answer is that the Messiah is "
                    "both human (David's seed) and divine (David's Lord) — the 'two powers in heaven' "
                    "theology that the divine council framework illuminates. The Melchizedek priesthood "
                    "(110:4) further transcends normal categories: the Messiah is not a Levitical priest "
                    "but a priest-king after an order that predates the Mosaic covenant and continues "
                    "forever. Hebrews 5-7 develops this into a full christological argument: Jesus is "
                    "the eternal high priest who has sat down at God's right hand, having offered the "
                    "perfect sacrifice once for all."
        },
        {
            "type": "context",
            "title": "The Imprecatory Psalms — Cursing the Enemy",
            "body": "The imprecatory (cursing) psalms — especially 69, 109, and 137 ('Happy shall he "
                    "be who takes your little ones and dashes them against the rock!') — present "
                    "serious theological challenges for modern readers. Several interpretive frameworks "
                    "help: (1) These are cries for divine justice, not personal vengeance — the psalmist "
                    "is asking God to act as judge, not taking justice into his own hands. (2) In the "
                    "divine council framework, the enemies of the psalmist are often agents of the "
                    "rebellious gods — spiritual warfare expressed in human terms. (3) The language is "
                    "often covenantal: the curses invoke the covenant sanctions of Deuteronomy 28 upon "
                    "those who have violated the covenant. (4) The emotional honesty of the psalms is "
                    "part of their theological function: they model bringing raw emotion to God rather "
                    "than suppressing it. (5) New Testament appropriation transforms the target: 'we do "
                    "not wrestle against flesh and blood, but against... spiritual forces of evil' "
                    "(Eph 6:12)."
        },
        {
            "type": "language",
            "title": "Selah (סֶלָה) — The Most Mysterious Word in the Bible",
            "body": "The word <em>selah</em> (Hebrew: <strong>סֶלָה</strong>, transliterated <em>selah</em>) "
                    "appears 71 times in Psalms and 3 times in Habakkuk 3 — 74 total occurrences. It is one "
                    "of the most debated words in biblical scholarship because <strong>nobody knows for certain "
                    "what it means</strong>. The word is not translated in most English Bibles — it is simply "
                    "transliterated from the Hebrew, which is why you see 'Selah' sitting untranslated in the "
                    "middle of psalms.<br><br>"
                    "<strong>Why some translations include it and others don't:</strong><br>"
                    "The Masoretic Text (Hebrew) includes <em>selah</em> in every occurrence. The KJV, NKJV, "
                    "ESV, NASB, and most literal translations preserve it. The NIV includes it. The NLT and "
                    "some dynamic translations omit it because it is a liturgical/musical instruction, not "
                    "part of the psalm's theological content — similar to how a hymnal might include 'Repeat "
                    "chorus' without considering it part of the lyrics. The Septuagint (LXX) translates it as "
                    "<em>diapsalma</em> (διάψαλμα), meaning 'musical interlude,' suggesting the ancient Greek "
                    "translators understood it as a performance direction.<br><br>"
                    "<strong>The leading theories on its meaning:</strong><br>"
                    "(1) <strong>Musical interlude</strong> — The most common scholarly view. Selah signals a "
                    "pause for instrumental music between sections of a psalm. The LXX's <em>diapsalma</em> "
                    "supports this. When you see <em>selah</em>, imagine the singers stopping while the "
                    "instruments play — a musical bridge between stanzas.<br>"
                    "(2) <strong>'Lift up' — a volume or worship cue</strong> — From the Hebrew root "
                    "<em>salal</em> (סלל, 'to lift up, to raise'). This could mean: raise the volume, lift "
                    "up your voices, lift up your hands in worship, or the emotional intensity should increase. "
                    "Think of a worship leader saying 'Now louder!' or 'Lift your hands!'<br>"
                    "(3) <strong>'Pause and reflect' — a meditation marker</strong> — The Targum (Aramaic "
                    "translation) renders it as <em>le'almin</em> ('forever'), and the Talmud (Eruvin 54a) "
                    "associates it with a pause for contemplation. This popular devotional interpretation sees "
                    "<em>selah</em> as an invitation: stop reading and let this truth sink in.<br>"
                    "(4) <strong>A liturgical response cue</strong> — Similar to 'Amen' or 'Hallelujah,' "
                    "<em>selah</em> may have been a cue for the congregation to respond — perhaps with a "
                    "shout, a prostration, or a spoken affirmation.<br>"
                    "(5) <strong>'To weigh / to measure'</strong> — From the related root <em>salah</em> "
                    "(to weigh on scales). This would mean: weigh what was just said, measure its importance, "
                    "consider its gravity.<br><br>"
                    "<strong>Key observations:</strong><br>"
                    "• <em>Selah</em> appears most frequently in lament psalms (Psalms 3, 4, 7, 9, etc.) and "
                    "at moments of theological intensity — suggesting it marks significant turning points<br>"
                    "• It often appears at the boundary between complaint and trust, between crisis and "
                    "praise — as if the pause is the pivot where faith turns from despair to hope<br>"
                    "• In Psalm 3:2,4,8 it appears three times, each time after a statement about YHWH's "
                    "protection — the pause reinforces the contrast between danger and divine security<br>"
                    "• In Habakkuk 3:3,9,13, it punctuates the prophet's vision of YHWH as the divine "
                    "warrior — pausing to let the cosmic imagery resonate<br>"
                    "• The word was clearly understood by ancient musicians but its precise meaning was lost "
                    "when Temple worship ceased after 70 AD<br><br>"
                    "<strong>Bottom line for readers:</strong> When you encounter <em>selah</em>, it most "
                    "likely meant a musical or liturgical pause — a moment where the congregation stopped, "
                    "the instruments played, and the weight of what was just proclaimed was allowed to settle "
                    "into the hearts of the worshipers. Read it as: <em>'Pause. Let that truth resonate.'</em>"
        },
        {
            "type": "language",
            "title": "Psalms Musical Superscriptions — Decoding the Headers",
            "body": "Many psalms begin with superscriptions containing musical terms that confuse modern "
                    "readers. These are ancient performance instructions — the equivalent of sheet music "
                    "notation. Here are the most common:<br><br>"
                    "<strong>lamnatseakh</strong> (לַמְנַצֵּחַ) — 'For the choir director' or 'For the music "
                    "leader.' Appears in 55 psalm headings. From the root <em>natsakh</em> (to lead, to "
                    "oversee). This psalm was assigned to the professional Temple music director for "
                    "performance.<br>"
                    "<strong>mizmor</strong> (מִזְמוֹר) — 'A psalm' — literally, a composition accompanied by "
                    "stringed instruments. From <em>zamar</em> (to pluck strings, to make music). The word "
                    "'Psalm' itself comes from the Greek <em>psalmos</em>, translating this Hebrew term.<br>"
                    "<strong>shir</strong> (שִׁיר) — 'A song' — a vocal composition. When both <em>mizmor</em> "
                    "and <em>shir</em> appear together ('A psalm, a song'), it indicates both instrumental "
                    "accompaniment and singing.<br>"
                    "<strong>maskil</strong> (מַשְׂכִּיל) — 'A contemplative poem' or 'a skillful psalm.' "
                    "From <em>sakal</em> (to understand, to be wise). These are 13 psalms requiring "
                    "thoughtful, skillful performance and meditation.<br>"
                    "<strong>miktam</strong> (מִכְתָּם) — Meaning uncertain. Possibly 'golden psalm,' 'psalm "
                    "of atonement,' or 'inscription psalm.' Only 6 psalms carry this label (16, 56-60), all "
                    "attributed to David during times of danger.<br>"
                    "<strong>shiggaion</strong> (שִׁגָּיוֹן) — 'A passionate, emotional song' or 'wandering "
                    "poem' (only Psalm 7). May indicate irregular rhythm reflecting emotional turmoil.<br>"
                    "<strong>Tune indicators:</strong> Several psalms specify a melody: 'al-tashheth' "
                    "('Do not destroy'), 'ayyeleth hasshachar' ('The Doe of the Dawn' — Psalm 22), "
                    "'yonath elem rekhokim' ('The Dove on Distant Oaks' — Psalm 56), 'shoshannim' "
                    "('Lilies' — Psalms 45, 69, 80). These reference well-known melodies in ancient Israel "
                    "that have been entirely lost.<br>"
                    "<strong>Instrument instructions:</strong> 'al-neginot' (on stringed instruments), "
                    "'al-nehilot' (on flutes), 'al-haggittit' (on a Gittite instrument — possibly from the "
                    "city of Gath), 'al-alamot' (for soprano voices), 'al-sheminit' (on the eighth — "
                    "possibly bass register or an 8-string instrument).<br><br>"
                    "These terms remind us that Psalms is a <strong>hymnal</strong>, not just a book of "
                    "poetry. Every psalm was sung, chanted, or performed with instruments in the worship of "
                    "the living God. The loss of the melodies is one of the great cultural losses of "
                    "antiquity."
        },
        {
            "type": "scholarship",
            "title": "The Psalter's Editorial Shape — A Story in Five Acts",
            "body": "Gerald Wilson's groundbreaking study The Editing of the Hebrew Psalter (1985) "
                    "demonstrated that the Psalter's five-book structure tells a theological story. "
                    "Books I-II (Psalms 1-72) are dominated by Davidic psalms — the king prays, "
                    "trusts, laments, and praises in his covenant relationship with YHWH. Book III "
                    "(Psalms 73-89) moves into crisis: the Asaph and Korah psalms grapple with "
                    "theodicy and national suffering, climaxing in Psalm 89's anguished question — "
                    "why has YHWH rejected his anointed and seemingly broken the Davidic covenant? "
                    "Book IV (Psalms 90-106) responds: before David, before the monarchy, before the "
                    "covenant — YHWH reigned. 'YHWH reigns!' (93:1; 96:10; 97:1; 99:1). The answer "
                    "to the Davidic covenant's apparent failure is not a new covenant but a deeper "
                    "trust in the eternal King. Book V (Psalms 107-150) moves toward eschatological "
                    "praise: the Hallel psalms, the Songs of Ascent, and the final Hallelujah chorus "
                    "that ends the entire Psalter with 'Let everything that has breath praise YHWH! "
                    "Hallelujah!' (150:6)."
        }
    ]
}
