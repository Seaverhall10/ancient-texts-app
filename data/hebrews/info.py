"""
info.py -- Hebrews: Scholarly Text Introduction

This file provides the "front page" for Hebrews in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Hebrews is THE divine council christology book of the New Testament. It takes
the enthronement theology of Psalms 2, 8, and 110, the Melchizedek priesthood,
and the heavenly tabernacle tradition, and builds from them the most sustained
argument in the NT for Christ's supremacy over the entire spiritual hierarchy.
Hebrews 1:5 quotes Psalm 2:7 -- the Son's enthronement decree. Hebrews 1:6
quotes Deuteronomy 32:43 (LXX/DSS) -- the divine council COMMANDED to worship
the Son. Hebrews 1:13 quotes Psalm 110:1 -- no angel was ever invited to sit
at YHWH's right hand. Hebrews 2:5-9 quotes Psalm 8 -- the world to come was
NOT subjected to angels but to the Son of Man. Hebrews 5-7 develops the
Melchizedek priesthood from Psalm 110:4. Hebrews 8-10 reveals the heavenly
tabernacle -- the true sanctuary where Christ ministers. Hebrews 12:22-24
climaxes with the vision of Mount Zion, the heavenly Jerusalem, thousands of
angels in festal assembly, and the mediator of the new covenant. No other NT
book so systematically establishes Christ's position above every tier of the
cosmic governance structure -- prophets, angels, Moses, Aaron, Melchizedek --
from the divine council's own scriptures.
"""

TEXT_INFO = {
    "text_id": "hebrews",
    "display_name": "Hebrews (Pros Hebraious)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- New Testament / Pauline-associated Epistles",
        "detail": "Hebrews is universally canonical in all Christian traditions today, though its "
                  "path to acceptance was debated. In the Eastern church, Hebrews was accepted early "
                  "as Pauline (Clement of Alexandria, Origen, Athanasius). The Western church was more "
                  "cautious: the Muratorian Fragment (late 2nd century) does not include it, Tertullian "
                  "attributed it to Barnabas, and it was only firmly accepted in the West after "
                  "Augustine and the councils of Hippo (393 AD) and Carthage (397 AD) included it in "
                  "the canon. Jerome included it in the Vulgate while noting the authorship debate. The "
                  "Reformers (Luther, Calvin) accepted its canonicity but questioned Pauline authorship. "
                  "Luther famously placed Hebrews after the undisputed Pauline letters in his NT arrangement. "
                  "Despite the authorship question, Hebrews has never been seriously challenged on doctrinal "
                  "grounds -- its christology is deeply rooted in the Old Testament and consistent with the "
                  "apostolic witness. It is the single most important NT text for understanding how the "
                  "early church read the Psalms, the Pentateuch, and the prophets christologically."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Eastern church attributed Hebrews to Paul from an early date. Clement of "
                       "Alexandria (c. 200 AD) proposed that Paul wrote it in Hebrew and Luke translated "
                       "it into Greek. Origen (c. 250 AD) noted that the thoughts were Paul's but the "
                       "style was not, famously concluding: 'Who wrote the epistle, in truth God knows.' "
                       "The superscription 'To the Hebrews' (Pros Hebraious) is not original but was "
                       "added by the 2nd century. Ancient alternatives to Paul include: Barnabas "
                       "(Tertullian's attribution), Luke (Clement of Alexandria's translation theory), "
                       "Clement of Rome (some early traditions), and Apollos (Luther's guess, widely "
                       "favored today). The letter itself never names its author -- the only NT epistle "
                       "traditionally grouped with Paul's letters that lacks a Pauline salutation.",

        "scholarly_debate": "Modern scholarship is nearly unanimous that Paul did not write Hebrews. The "
                           "evidence is substantial: (1) The Greek style is the most polished and literary "
                           "in the entire NT -- far more elegant than Paul's koine Greek. (2) The author "
                           "places himself among those who received the gospel secondhand (2:3), while Paul "
                           "emphatically claims direct revelation (Gal 1:12). (3) The theological vocabulary "
                           "differs: Paul's key terms (justification, flesh vs. spirit, in Christ) are absent; "
                           "Hebrews uses unique terms (archegos/pioneer, teleiosis/perfection, hypostasis/ "
                           "substance). (4) The OT quotation technique differs: Paul quotes the Hebrew and "
                           "Greek freely; Hebrews quotes exclusively from the LXX. (5) The theological method "
                           "differs: Paul argues from the Christ-event backward to scripture; Hebrews argues "
                           "from scripture forward to Christ. Luther's suggestion of Apollos (Acts 18:24 -- "
                           "'an eloquent man, competent in the Scriptures, from Alexandria') fits many of the "
                           "stylistic features: Alexandrian rhetorical training, deep LXX knowledge, christological "
                           "exegesis. Other proposals include Priscilla (Harnack, 1900 -- explaining why the "
                           "name was suppressed), Silas, or Philip. None can be proven.",

        "bottom_line": "The author of Hebrews is unknown. This is one of the great mysteries of the New "
                       "Testament. What is clear: the author was a second-generation Christian (2:3), deeply "
                       "trained in the Septuagint (LXX), skilled in Alexandrian-style exegesis, possessed of "
                       "extraordinary rhetorical ability, and steeped in the theology of the heavenly "
                       "sanctuary and the divine council. The author knew the recipients personally (13:19, "
                       "23), was associated with Timothy (13:23), and wrote from or to an Italian community "
                       "(13:24). Whether Apollos, Barnabas, Priscilla, or someone else entirely, Origen's "
                       "verdict stands: 'Who wrote the epistle, in truth God knows.'"
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Before the destruction of the Jerusalem Temple in 70 AD. The argument for an "
                       "early date rests on the author's present-tense discussion of Temple sacrifices "
                       "(8:4-5; 9:6-9; 10:1-3, 11; 13:10-11) -- if the Temple had already been destroyed, "
                       "the argument against the old covenant's sacrificial system would have been vastly "
                       "strengthened by that catastrophic historical event. The silence about the Temple's "
                       "destruction is the strongest evidence for a pre-70 date.",
        "critical_range": "Most scholars date Hebrews between 60-90 AD. The pre-70 camp (Robinson, "
                         "Guthrie, Bruce, Lane) argues the present-tense cultic language demands a date "
                         "before the Temple fell. The post-70 camp (Koester, Attridge) notes that: (1) "
                         "Hebrews describes the Tabernacle (skene), not the Temple (hieron/naos) -- the "
                         "author argues from the Pentateuchal text, not current practice. (2) Clement of "
                         "Rome (c. 96 AD) appears to quote or echo Hebrews (1 Clement 36:2-5 closely "
                         "parallels Hebrews 1:3-13), providing a terminus ante quem. (3) The 'former days' "
                         "of persecution (10:32-34) may refer to Nero's persecution (64 AD) or Claudius' "
                         "expulsion of Jews from Rome (49 AD). A date in the mid-60s AD is the most common "
                         "scholarly estimate, though certainty is impossible.",
        "evidence": "Key evidence includes: (1) The present-tense sacrificial language (8:4-5; 9:6-9; "
                    "10:1-3, 11) -- strongly suggesting the Temple still stands. (2) 1 Clement (c. 96 AD) "
                    "echoes Hebrews extensively, meaning Hebrews must predate that letter. (3) The reference "
                    "to Timothy (13:23) places the letter within the apostolic generation. (4) The persecution "
                    "history (10:32-34; 12:4 -- 'you have not yet resisted to the point of shedding blood') "
                    "suggests a community that has suffered imprisonment and property loss but not martyrdom -- "
                    "possibly before the Neronian persecution's full fury (64-68 AD) or in a community "
                    "outside Rome that escaped the worst. (5) The theological sophistication of the "
                    "christological argument suggests a mature stage of early Christian reflection on the "
                    "OT, but not so late that Hebrews' unique categories (Melchizedek typology, heavenly "
                    "tabernacle) have become standard -- they are being freshly argued."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "A specific community of Jewish Christians (or at minimum, Gentile Christians "
                            "deeply versed in the Septuagint and Jewish liturgical tradition) who are in "
                            "danger of abandoning their faith and reverting to Judaism or simply drifting "
                            "away from the Christian confession. The title 'To the Hebrews' reflects early "
                            "church tradition about the recipients. The community has experienced persecution "
                            "(10:32-34), has been believers for some time (5:12 -- 'by this time you ought "
                            "to be teachers'), and is in danger of apostasy (6:4-6; 10:26-31). The Italian "
                            "connection (13:24 -- 'those from Italy send you greetings') may indicate a "
                            "Roman community, possibly the Jewish-Christian house churches affected by "
                            "Claudius' edict (49 AD) and Nero's persecution (64 AD).",

        "purpose": "Hebrews is a 'word of exhortation' (logos tes parakleseos, 13:22) -- the same phrase "
                   "used for a synagogue sermon in Acts 13:15. It is essentially a written sermon designed "
                   "to prevent apostasy by demonstrating that Christ is superior to every element of the "
                   "old covenant: superior to the prophets (1:1-3), to the angels who mediated the law "
                   "(1:4-2:18), to Moses (3:1-6), to Joshua (4:1-13), to Aaron and the Levitical "
                   "priesthood (4:14-7:28), to the old covenant itself (8:1-13), to the tabernacle and "
                   "its sacrifices (9:1-10:18). The pastoral logic is: if Christ is superior to everything "
                   "you would go back to, why would you go back? The five warning passages (2:1-4; "
                   "3:7-4:13; 5:11-6:12; 10:26-39; 12:14-29) punctuate the argument with increasing "
                   "urgency.",

        "theological_intent": "Hebrews provides the most sustained christological exegesis of the Old "
                             "Testament in the New Testament. Its central theological claims are: (1) The "
                             "Son is the exact imprint (charakter) of God's nature and the radiance "
                             "(apaugasma) of his glory (1:3) -- ontological divine identity. (2) The Son "
                             "is superior to the angels -- the entire divine council is commanded to worship "
                             "him (1:6). (3) The Son is both the enthroned king (Ps 2:7; 110:1) and the "
                             "eternal priest (Ps 110:4) -- combining in one person what the old covenant "
                             "kept separate. (4) The earthly tabernacle was a copy (typos) and shadow "
                             "(skia) of the heavenly reality where Christ now ministers (8:5; 9:24). (5) "
                             "Christ's single sacrifice replaces the entire sacrificial system permanently "
                             "(10:10-14). (6) Faith is the substance of heavenly realities and the evidence "
                             "of unseen things (11:1) -- the bridge between the visible and invisible "
                             "worlds that the divine council theology maps."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Koine Greek -- the most elegant and literary Greek in the entire New Testament",
        "script": "Greek uncial script (earliest manuscripts)",
        "linguistic_notes": "The Greek of Hebrews is widely regarded as the finest in the NT. The author "
                           "employs classical rhetorical techniques: periodic sentences with balanced clauses "
                           "(1:1-4 is a single magnificent sentence in Greek), alliteration (1:1 -- polumeros "
                           "kai polutropos, 'in many portions and many ways'), chiastic structures, "
                           "inclusio (the letter opens and closes with the Son's cosmic supremacy), and "
                           "sophisticated vocabulary drawn from both literary Greek and the Septuagint. "
                           "The vocabulary includes 154 words not found elsewhere in the NT (hapax legomena). "
                           "Key theological terms include: apaugasma (radiance/effulgence -- 1:3), charakter "
                           "(exact imprint -- 1:3), hypostasis (substance/reality -- 1:3; 11:1), archegos "
                           "(pioneer/founder -- 2:10; 12:2), teleiosis (perfection/completion -- 7:11), and "
                           "parrhesia (boldness/confidence -- 4:16; 10:19). The author quotes the OT "
                           "exclusively from the Septuagint (LXX), sometimes following readings that differ "
                           "significantly from the Masoretic Text (MT) -- most notably Deuteronomy 32:43 in "
                           "Hebrews 1:6 and Psalm 40:6 in Hebrews 10:5. This LXX dependence is critical for "
                           "the theological argument: several key proof-texts work only in the Greek, not the "
                           "Hebrew.",
        "grammar_match": "Hebrews reads less like a letter and more like a rhetorical sermon (logos tes "
                        "parakleseos, 13:22) with epistolary features appended at the end (13:22-25). The "
                        "rhetorical structure has been analyzed as: exordium (1:1-4), a series of synkrisis "
                        "(comparison arguments: Son vs. angels, Moses, Aaron, etc.), interspersed with "
                        "paraenetic (exhortation) sections, and a peroration (12:1-13:21). The author "
                        "shifts between exposition and exhortation in a careful rhythm: theological "
                        "argument followed by 'therefore' (oun) or 'for this reason' (dio) introducing "
                        "pastoral application. The sentence structure is complex, with long embedded "
                        "clauses and careful subordination -- more like Thucydides or Philo than like "
                        "Paul's sometimes-broken syntax."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Hebrews IS scripture -- the NT's most sustained christological reading of the Old "
                   "Testament, demonstrating how the entire old covenant system pointed forward to Christ.",
        "nt_usage": "Hebrews contains more OT quotations per page than any other NT book. The author cites "
                    "the OT at least 35 times explicitly and alludes to it dozens more. The most theologically "
                    "significant quotations include: Psalm 2:7 (Heb 1:5; 5:5) -- the Son's enthronement "
                    "decree. 2 Samuel 7:14 (Heb 1:5) -- 'I will be to him a Father.' Deuteronomy 32:43 "
                    "LXX/DSS (Heb 1:6) -- 'Let all God's angels worship him.' Psalm 45:6-7 (Heb 1:8-9) -- "
                    "'Your throne, O God, is forever.' Psalm 102:25-27 (Heb 1:10-12) -- the Son as creator "
                    "who outlasts creation. Psalm 110:1 (Heb 1:13; 10:12-13) -- 'Sit at my right hand.' "
                    "Psalm 8:4-6 (Heb 2:6-8) -- humanity's destiny fulfilled in Christ. Psalm 22:22 "
                    "(Heb 2:12) -- Christ declares God's name among the brothers. Isaiah 8:17-18 "
                    "(Heb 2:13) -- the children God has given. Psalm 95:7-11 (Heb 3:7-4:7) -- 'Today if "
                    "you hear his voice.' Psalm 110:4 (Heb 5:6; 7:17, 21) -- 'A priest forever after "
                    "the order of Melchizedek.' Jeremiah 31:31-34 (Heb 8:8-12; 10:16-17) -- the new "
                    "covenant promise. Habakkuk 2:3-4 (Heb 10:37-38) -- 'The righteous shall live by "
                    "faith.' Proverbs 3:11-12 (Heb 12:5-6) -- divine discipline as fatherly love. Haggai "
                    "2:6 (Heb 12:26) -- God will shake heaven and earth one more time.",
        "internal_consistency": "Hebrews is perfectly consistent with the theological trajectory of the OT: "
                               "the Davidic covenant (2 Sam 7), the royal psalms (Ps 2, 45, 110), the "
                               "prophetic promise of a new covenant (Jer 31), the suffering servant "
                               "(Isa 53, echoed in Heb 9:28), and the Day of Atonement ritual (Lev 16, "
                               "expounded in Heb 9). It is also consistent with NT christology: the "
                               "pre-existence of Christ (John 1:1-3; Col 1:15-17; Heb 1:2-3), his "
                               "mediatorial role (1 Tim 2:5; Heb 8:6; 9:15; 12:24), and his session at "
                               "God's right hand (Mark 16:19; Acts 2:33-34; Rom 8:34; Eph 1:20; Heb 1:3, "
                               "13; 10:12). Hebrews' unique contribution is synthesizing these themes into "
                               "a single comprehensive argument from the divine council texts."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "P46 (Chester Beatty Papyrus II), dating to approximately 175-225 AD, is the earliest "
                    "manuscript containing Hebrews. Remarkably, P46 places Hebrews immediately after "
                    "Romans in the Pauline collection -- before 1 and 2 Corinthians -- suggesting that "
                    "the Alexandrian tradition regarded it as Paul's most important letter after Romans. "
                    "P13 (3rd-4th century) also contains portions of Hebrews.",
        "major_witnesses": [
            {"name": "P46 (Chester Beatty Papyrus II)", "date": "c. 175-225 AD",
             "note": "The earliest witness to Hebrews. Contains Heb 1:1-9:16 and 9:18-10:20, with some "
                     "lacunae. Placed between Romans and 1 Corinthians in the codex, indicating early "
                     "acceptance as Pauline and high regard for its theological importance."},
            {"name": "Codex Sinaiticus (Aleph)", "date": "c. 330-360 AD",
             "note": "Complete text of Hebrews. Places it after 2 Thessalonians in the Pauline corpus. "
                     "One of the two great uncial codices, providing the foundation for the critical text."},
            {"name": "Codex Vaticanus (B)", "date": "c. 325-350 AD",
             "note": "Complete text of Hebrews. Places it after Galatians and before Ephesians -- "
                     "between the 'church' epistles and the 'personal' epistles. Vaticanus and Sinaiticus "
                     "together provide the most reliable early text of Hebrews."},
            {"name": "Codex Alexandrinus (A)", "date": "c. 400-440 AD",
             "note": "Complete text of Hebrews. Places it after 2 Thessalonians. Reflects the "
                     "Alexandrian text tradition and preserves a text very close to the other great "
                     "uncials."},
            {"name": "Codex Claromontanus (D)", "date": "c. 550 AD",
             "note": "A Greek-Latin bilingual manuscript of the Pauline epistles. Places Hebrews after "
                     "Philemon at the end of the Pauline collection, reflecting Western hesitation about "
                     "its authorship while accepting its canonical status."}
        ],
        "reliability": "The text of Hebrews is exceptionally well-preserved. The major uncial codices agree "
                       "closely, and there are no significant textual variants that affect the theological "
                       "argument. The most notable variant is in 2:9: most manuscripts read 'by the grace "
                       "of God (chariti theou) he might taste death for everyone,' but a few witnesses "
                       "(including some manuscripts known to Origen) read 'apart from God (choris theou) "
                       "he tasted death for everyone' -- a theologically provocative reading that may be "
                       "original but was likely changed by scribes uncomfortable with the implication. "
                       "Overall, Hebrews' textual tradition is stable and reliable."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Hebrews was written to a community under pressure -- believers who had endured "
                   "persecution (10:32-34: imprisonment, public shame, seizure of property) and were now "
                   "tempted to drift away from the Christian confession (2:1), perhaps back to the "
                   "synagogue or to a non-committal religious stance. The 'former days' of suffering "
                   "(10:32) may refer to the turmoil following Claudius' expulsion of Jews from Rome "
                   "(49 AD, Acts 18:2) or early Neronian harassment. The community had not yet experienced "
                   "martyrdom (12:4 -- 'you have not yet resisted to the point of shedding blood'), "
                   "which may place them before the full fury of Nero's persecution (64-68 AD). They "
                   "had known the faith long enough that they should be teachers (5:12) but were "
                   "regressing to spiritual infancy. The author's pastoral strategy is to overwhelm "
                   "them with the superiority of what they have in Christ -- so that going back to "
                   "anything less becomes unthinkable.",

        "geography": "The most likely geographical connection is Rome. Hebrews 13:24 ('Those who come "
                     "from Italy send you greetings') is ambiguous: it could mean the letter was sent "
                     "from Italy (Italian Christians sending greetings with it) or sent to Italy "
                     "(Italian expatriates sending greetings home). The Roman connection is strengthened "
                     "by the fact that 1 Clement (written from Rome, c. 96 AD) is the earliest external "
                     "witness to Hebrews, suggesting the letter was known and authoritative in Rome "
                     "very early. If the audience is Roman Jewish Christians, the letter addresses a "
                     "community caught between synagogue and church, between the old covenant's visible "
                     "institutions and the new covenant's invisible heavenly realities.",

        "historical_connections": "Hebrews stands at a critical juncture in early Christianity: the "
                                 "generation of eyewitnesses is passing (2:3 -- the message 'was declared "
                                 "at first by the Lord, and it was attested to us by those who heard'), "
                                 "the Temple still stands but its theological obsolescence has been declared "
                                 "(8:13 -- the old covenant 'is becoming obsolete and growing old, ready to "
                                 "vanish away'), and the community must decide whether the heavenly reality "
                                 "of Christ's priesthood is sufficient to sustain them without the visible "
                                 "supports of Temple, priesthood, and sacrifice. If written before 70 AD, "
                                 "the author's declaration that the old covenant is 'ready to vanish away' "
                                 "is prophetic -- the Temple would be destroyed within years. The letter "
                                 "also reflects engagement with Jewish angelology and speculation about "
                                 "intermediaries that was flourishing in Second Temple Judaism."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Hebrews is the New Testament's definitive statement on Christ's position within "
                   "the cosmic governance hierarchy. Every chapter of the theological argument engages "
                   "the divine council framework, establishing the Son's supremacy over every tier of "
                   "spiritual authority."
                   "\n\n"
                   "HEBREWS 1 -- THE SON ABOVE THE COUNCIL: The opening catena (chain of OT "
                   "quotations, 1:5-14) is a systematic demonstration that the Son holds a rank that "
                   "no member of the divine council has ever held. Psalm 2:7 ('You are my Son, today "
                   "I have begotten you') and 2 Samuel 7:14 ('I will be to him a Father') establish "
                   "the Son's unique filial relationship with YHWH -- a relationship never extended to "
                   "any angel (1:5). Then comes the bombshell: quoting Deuteronomy 32:43 in the LXX/ "
                   "DSS reading ('Let all God's angels worship him'), the author declares that when God "
                   "brings his firstborn into the world, the entire divine council is COMMANDED to "
                   "worship the Son (1:6). This is the Deuteronomy 32 worldview in its christological "
                   "climax: the same council of 'sons of God' (bene elohim) that was allotted the "
                   "nations at Babel is now ordered to prostrate before YHWH's ultimate Son. Psalm 45:6-7 "
                   "('Your throne, O God, is forever and ever') addresses the Son as God -- a divine "
                   "figure who is simultaneously distinct from God ('therefore God, your God, has anointed "
                   "you,' 1:9). Psalm 102:25-27 applies to the Son the creation language of YHWH himself: "
                   "'You, Lord, laid the foundation of the earth.' The Son is not a created being but "
                   "the creator. The catena climaxes with Psalm 110:1 ('Sit at my right hand until I "
                   "make your enemies a footstool for your feet') -- the Son sits where no angel has "
                   "ever been invited to sit, at the right hand of power itself (1:13)."
                   "\n\n"
                   "HEBREWS 2 -- THE SON BELOW THE COUNCIL (TEMPORARILY): The argument takes a "
                   "stunning turn in chapter 2. Quoting Psalm 8 ('What is man that you are mindful of "
                   "him?'), the author notes that God did not subject 'the world to come' to angels "
                   "(2:5) but to the son of man. Yet we see Jesus 'made lower than the angels for a "
                   "little while' (2:9) -- the incarnation is a temporary descent below the divine "
                   "council in order to taste death for everyone and then be 'crowned with glory and "
                   "honor.' The pioneer (archegos) of salvation was made perfect through suffering (2:10). "
                   "He identifies with humanity -- 'he is not ashamed to call them brothers' (2:11) -- "
                   "quoting Psalm 22:22 and Isaiah 8:17-18. The incarnation is presented as a cosmic "
                   "strategy: by sharing flesh and blood, the Son destroys 'the one who has the power of "
                   "death, that is, the devil' (2:14) and liberates those held in slavery through fear "
                   "of death. This is divine council warfare: the Son descends through the council's "
                   "ranks, enters enemy-held territory (the realm of death), defeats the usurper, and "
                   "ascends back above all principalities and powers."
                   "\n\n"
                   "HEBREWS 5-7 -- THE MELCHIZEDEK PRIESTHOOD: The author develops Psalm 110:4 ('You "
                   "are a priest forever after the order of Melchizedek') into the longest sustained "
                   "typological argument in the NT. Melchizedek (Gen 14:18-20) was the priest-king of "
                   "Salem (Jerusalem) who blessed Abraham and received tithes from him. In Hebrews' "
                   "reading, Melchizedek's silence in Genesis about parentage, birth, and death makes "
                   "him a type of the eternal Son -- 'without father, without mother, without genealogy, "
                   "having neither beginning of days nor end of life, resembling the Son of God, he "
                   "continues a priest forever' (7:3). The Levitical priesthood (descended from Abraham "
                   "through Levi) is subordinate to Melchizedek because Abraham paid tithes to him and "
                   "received his blessing -- and 'the lesser is blessed by the greater' (7:7). The "
                   "Melchizedek priesthood is superior because it is (a) by divine oath, not law (7:20-22), "
                   "(b) permanent, not hereditary (7:23-24), (c) based on an indestructible life, not "
                   "physical descent (7:16), and (d) proven effective because its priest 'always lives to "
                   "make intercession' (7:25). In divine council terms, the Melchizedek priest-king "
                   "represents a cosmic order of priesthood that predates and transcends the Mosaic "
                   "system -- a heavenly office that the earthly Levitical priesthood could only shadow."
                   "\n\n"
                   "HEBREWS 8-10 -- THE HEAVENLY TABERNACLE: The argument reaches its architectural "
                   "climax: the earthly tabernacle was a 'copy and shadow' (hypodeigma kai skia) of the "
                   "heavenly one (8:5), built according to the 'pattern' (typos) shown to Moses on Sinai "
                   "(8:5, quoting Exod 25:40). Christ ministers in 'the true tent' (skene) that the Lord "
                   "set up, not man (8:2) -- the heavenly sanctuary itself. The Day of Atonement ritual "
                   "(Lev 16) is the type: the high priest entered the Most Holy Place once a year with "
                   "blood not his own. Christ entered the heavenly Most Holy Place 'once for all' with "
                   "his own blood (9:12), obtaining 'eternal redemption.' The veil of the earthly "
                   "sanctuary represented the barrier between the visible and invisible realms (9:8); "
                   "Christ's flesh was the veil through which he opened 'a new and living way' (10:20) "
                   "into the very presence of God -- the throne room of the divine council."
                   "\n\n"
                   "HEBREWS 12:22-24 -- THE HEAVENLY ASSEMBLY: The letter climaxes with a vision of "
                   "the destination: 'You have come to Mount Zion and to the city of the living God, "
                   "the heavenly Jerusalem, and to innumerable angels in festal gathering, and to the "
                   "assembly (ekklesia) of the firstborn who are enrolled in heaven, and to God, the "
                   "judge of all, and to the spirits of the righteous made perfect, and to Jesus, the "
                   "mediator of a new covenant' (12:22-24). This is the divine council scene of the "
                   "New Testament: the heavenly Jerusalem, the angelic myriads, the assembly of the "
                   "firstborn, God enthroned as judge, the perfected saints, and Jesus as mediator. "
                   "The believers are told they have already arrived at this cosmic assembly through "
                   "faith. The contrast with Sinai (12:18-21 -- fire, darkness, storm, terror) makes "
                   "the point: the old covenant brought you to a terrifying mountain; the new covenant "
                   "brings you to the heavenly council chamber itself.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 4-5 (the 'two powers in heaven' -- Hebrews' quotation of Ps 45:6-7 and Ps 102:25-27 as applied to the Son)",
            "The Unseen Realm, chapter 24-25 (Ps 2:7 in Hebrews 1:5 -- the Son's enthronement above the council)",
            "The Unseen Realm, chapter 12-13 (Deuteronomy 32 worldview -- Hebrews 1:6 quotes Deut 32:43 LXX/DSS)",
            "The Unseen Realm, chapter 30-31 (Melchizedek and Psalm 110 -- the priest-king theology Hebrews develops)",
            "Supernatural, chapter 12 (Christ's authority over the spirit realm -- the argument of Hebrews 1-2)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 14-15 (angels as ministering spirits -- Heb 1:14)",
            "The Naked Bible Podcast, episode 173 (Psalm 110 and Melchizedek -- the foundation of Hebrews 5-7)",
            "The Naked Bible Podcast, episode 69 (Hebrews 1 and the divine council)",
            "The Naked Bible Podcast, episode 2 (Deuteronomy 32 worldview -- the backdrop of Hebrews 1:6)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "Melchizedek -- Who Is He and Why Does He Matter?",
            "body": "Melchizedek is one of the most mysterious figures in the Bible, appearing in only "
                    "three passages: Genesis 14:18-20, Psalm 110:4, and Hebrews 5-7. In Genesis, he is "
                    "introduced without warning as 'king of Salem' and 'priest of God Most High' (El "
                    "Elyon). He brings out bread and wine, blesses Abraham, and receives a tenth of the "
                    "spoils from Abraham's victory. Then he vanishes from the narrative -- no genealogy, "
                    "no birth record, no death record.<br><br>"
                    "His name means 'king of righteousness' (melek = king, tsedeq = righteousness) in "
                    "Hebrew. His title 'king of Salem' is understood as 'king of peace' (shalom = peace), "
                    "and Salem is identified with Jerusalem (Ps 76:2).<br><br>"
                    "<strong>Why this matters for Hebrews:</strong> In the Mosaic covenant, the offices of "
                    "king and priest were strictly separated. Kings came from Judah (David's line); priests "
                    "came from Levi (Aaron's line). King Uzziah was struck with leprosy for trying to burn "
                    "incense in the Temple (2 Chr 26:16-21). But Melchizedek held BOTH offices -- he was a "
                    "priest-king, predating the Mosaic separation by centuries. Psalm 110:4 declares that "
                    "the Messiah will be 'a priest forever after the order of Melchizedek' -- not after "
                    "Aaron's order. Hebrews argues this means: (1) The Levitical priesthood was always "
                    "temporary; a superior priesthood was prophesied. (2) Jesus, from the tribe of Judah "
                    "(not Levi), can be a legitimate priest because Melchizedek's priesthood was not based "
                    "on tribal descent. (3) The Melchizedek priesthood is eternal and sworn by God's oath, "
                    "making it unbreakable.<br><br>"
                    "<strong>Second Temple speculation:</strong> The Dead Sea Scrolls contain a remarkable "
                    "text (11QMelchizedek / 11Q13) that presents Melchizedek as a heavenly figure -- an "
                    "elohim who presides over the divine council's judgment in the final jubilee, executing "
                    "the verdict of Psalm 82. This Qumran text shows that pre-Christian Judaism already "
                    "connected Melchizedek with divine council authority and eschatological judgment. "
                    "Hebrews' identification of Jesus with the Melchizedek order takes this tradition to "
                    "its christological conclusion."
        },
        {
            "type": "theology",
            "title": "Levitical vs. Melchizedek Priesthood -- What Changed and Why",
            "body": "Understanding the priesthood argument of Hebrews 5-7 requires knowing what the "
                    "Levitical priesthood was and why it was replaced.<br><br>"
                    "<strong>The Levitical Priesthood (Aaron's order):</strong><br>"
                    "Established at Sinai (Exod 28-29; Lev 8-9). Only descendants of Aaron from the "
                    "tribe of Levi could serve as priests. The high priest entered the Most Holy Place "
                    "once a year on the Day of Atonement (Yom Kippur, Lev 16) to sprinkle blood on the "
                    "mercy seat -- a ritual that had to be repeated annually because it could never "
                    "permanently deal with sin. Priests served until death and were replaced by their "
                    "sons. The system was inherently temporary: priests died, sacrifices were repeated, "
                    "the veil remained, and access to God's presence was restricted to one man on one "
                    "day per year.<br><br>"
                    "<strong>The Melchizedek Priesthood (Christ's order):</strong><br>"
                    "Not based on genealogy or tribal descent (Heb 7:3, 16). Established by God's "
                    "oath: 'The Lord has sworn and will not change his mind: You are a priest forever' "
                    "(Ps 110:4; Heb 7:21). Jesus serves as priest permanently because he lives forever "
                    "(Heb 7:24-25). He entered the heavenly Most Holy Place once for all with his own "
                    "blood (Heb 9:12), not the blood of animals. The sacrifice never needs repeating "
                    "because it achieved eternal redemption. The veil is torn; access to God is "
                    "permanently open (Heb 10:19-22).<br><br>"
                    "<strong>Hebrews' argument:</strong> The very existence of Psalm 110:4 -- a prophecy "
                    "of a non-Levitical, Melchizedek-order priest -- proves the Levitical system was "
                    "never God's final intention. It was a shadow of the heavenly reality (Heb 8:5; "
                    "10:1). When the priesthood changes, the law must change too (Heb 7:12). This is "
                    "not God abandoning his plan but fulfilling it: the copy gives way to the original, "
                    "the shadow yields to the substance."
        },
        {
            "type": "interpretation",
            "title": "Why Hebrews Quotes the LXX/DSS Instead of the Hebrew Bible (MT)",
            "body": "One of the most striking features of Hebrews is that its Old Testament quotations "
                    "come exclusively from the Septuagint (LXX) -- the Greek translation of the Hebrew "
                    "Bible made in Alexandria, Egypt (3rd-2nd century BC). In several crucial passages, "
                    "the LXX reading differs significantly from the Masoretic Text (MT, the standard "
                    "Hebrew text), and the author's theological argument depends on the Greek reading. "
                    "This is not a flaw -- it is a window into how the early church read scripture.<br><br>"
                    "<strong>Key examples:</strong><br>"
                    "<strong>Hebrews 1:6 / Deuteronomy 32:43:</strong> The MT reads 'Rejoice, O nations, "
                    "with his people.' The LXX reads 'Let all God's angels worship him.' The Dead Sea "
                    "Scrolls (4QDeutq) confirm that the LXX preserves an older Hebrew reading that was "
                    "shortened in the MT. Hebrews uses this reading to prove the angels worship the Son. "
                    "Without the LXX/DSS reading, this proof-text does not exist in the Hebrew.<br>"
                    "<strong>Hebrews 10:5 / Psalm 40:6:</strong> The MT reads 'ears you have dug for me' "
                    "(a metaphor for obedient listening). The LXX reads 'a body you have prepared for me.' "
                    "Hebrews uses the LXX reading to argue that Christ's incarnation -- his body -- was the "
                    "sacrifice God prepared to replace animal offerings. The theological argument about the "
                    "incarnation depends on the Greek reading.<br>"
                    "<strong>Hebrews 2:7 / Psalm 8:5:</strong> The Hebrew 'a little lower than elohim' "
                    "becomes in the LXX 'a little lower than angels (angelous).' Hebrews uses 'angels' to "
                    "support the argument about Christ's temporary incarnational humiliation below the "
                    "angelic realm.<br><br>"
                    "<strong>Why does this matter?</strong> The Septuagint was the Bible of the early "
                    "church. Greek-speaking Jews and Christians read the OT in Greek, and the LXX was "
                    "regarded as inspired -- Philo of Alexandria considered it a divinely guided translation. "
                    "The Dead Sea Scrolls have vindicated many LXX readings by showing they reflect Hebrew "
                    "originals older than the MT. The author of Hebrews was not misquoting scripture; he "
                    "was reading from a textual tradition that, in several key places, preserves readings "
                    "the MT shortened or altered. This is a powerful argument for taking the LXX seriously "
                    "as a witness to the original text."
        },
        {
            "type": "theology",
            "title": "The Heavenly Tabernacle -- What Is the 'True Tent'?",
            "body": "Hebrews 8-10 builds its argument on a concept that strikes modern readers as strange: "
                    "there is a tabernacle in heaven -- the 'true tent' (skene) -- and the earthly "
                    "tabernacle Moses built was merely a copy of it.<br><br>"
                    "<strong>The biblical foundation:</strong> When God commanded Moses to build the "
                    "tabernacle, he said: 'See that you make everything according to the pattern (typos) "
                    "that was shown you on the mountain' (Exod 25:40; quoted in Heb 8:5). Moses was shown "
                    "a heavenly original and told to replicate it on earth. The earthly tabernacle was never "
                    "the ultimate reality -- it was a scale model of the heavenly throne room.<br><br>"
                    "<strong>What the heavenly tabernacle represents:</strong> In divine council theology, "
                    "God's throne room is the command center of cosmic governance. The cherubim on the ark's "
                    "mercy seat (Exod 25:18-22) represent the council members who flank God's throne (cf. "
                    "Isa 6:1-3; Ezek 1:4-28; Rev 4:6-8). The Most Holy Place represents God's immediate "
                    "presence -- the inner sanctum of the divine council chamber. The veil separating the "
                    "Holy Place from the Most Holy Place represents the boundary between the visible and "
                    "invisible realms. The earthly high priest's annual entry through the veil was a "
                    "ritual re-enactment of what the heavenly high priest would do definitively.<br><br>"
                    "<strong>Christ in the heavenly tabernacle:</strong> Hebrews argues that Christ has "
                    "entered 'not into holy places made with hands, which are copies (antitypa) of the "
                    "true things, but into heaven itself, now to appear in the presence of God on our "
                    "behalf' (9:24). He passed through the veil (his flesh, 10:20), entered the heavenly "
                    "Most Holy Place with his own blood (9:12), and sat down at the right hand of the "
                    "Majesty on high (1:3; 8:1; 10:12) -- permanently, because the sacrifice never needs "
                    "repeating. The believers are invited to follow: 'We have confidence (parrhesia) to "
                    "enter the holy places by the blood of Jesus' (10:19). The veil is permanently open. "
                    "Access to the divine council's throne room is now available to every believer."
        },
        {
            "type": "interpretation",
            "title": "The 'Cloud of Witnesses' (12:1) -- Dead Saints or Divine Council?",
            "body": "Hebrews 12:1 says: 'Therefore, since we are surrounded by so great a cloud of "
                    "witnesses (nephos martyron), let us also lay aside every weight, and sin which "
                    "clings so closely, and let us run with endurance the race that is set before us.' "
                    "The popular interpretation is that the saints of Hebrews 11 (the 'faith hall of "
                    "fame') are now in heaven watching us like spectators in an arena. But this reading "
                    "has problems, and the divine council framework offers a richer alternative.<br><br>"
                    "<strong>The standard reading:</strong> The heroes of faith from chapter 11 are now "
                    "in heaven, watching believers run their race, cheering them on like fans in a stadium. "
                    "This is emotionally appealing but theologically thin. The word 'witnesses' (martyres) "
                    "does not mean 'spectators' -- it means those who have borne testimony. They are "
                    "witnesses in the legal/testimonial sense, not the observational sense.<br><br>"
                    "<strong>The divine council reading:</strong> Just eight verses later, Hebrews "
                    "12:22-24 describes the heavenly assembly: Mount Zion, the heavenly Jerusalem, "
                    "myriads of angels in festal gathering, the assembly of the firstborn, the spirits "
                    "of the righteous made perfect, and Jesus the mediator. The 'cloud of witnesses' in "
                    "12:1 may be a preview of this heavenly assembly -- not dead saints watching from "
                    "bleachers, but the entire celestial court that surrounds God's throne. The 'cloud' "
                    "(nephos) echoes the cloud of God's presence (the Shekinah) and the clouds associated "
                    "with divine council theophanies (Dan 7:13; Rev 1:7). The witnesses are those whose "
                    "testimony of faith (Heb 11) has been recorded in the heavenly court -- their lives "
                    "are entered into evidence before the divine judge.<br><br>"
                    "<strong>Bottom line:</strong> The 'cloud of witnesses' is probably not about "
                    "deceased saints having a viewing party. It is about the weight of accumulated "
                    "testimony: the faithful of all ages have borne witness to God's faithfulness, and "
                    "their testimony stands in the heavenly court. The believers are running their race "
                    "in the context of that cosmic courtroom, surrounded by the evidence of God's "
                    "trustworthiness. Hebrews 12:22-24 then makes it explicit: you have come to the "
                    "heavenly assembly itself."
        },
        {
            "type": "context",
            "title": "The Authorship Mystery -- Why We Don't Know Who Wrote Hebrews",
            "body": "Hebrews is the only New Testament letter traditionally grouped with Paul's writings "
                    "that does not name its author. Every other Pauline epistle opens with 'Paul, an "
                    "apostle...' or 'Paul, a servant...' Hebrews simply begins: 'Long ago, at many "
                    "times and in many ways, God spoke to our fathers by the prophets...' (1:1). The "
                    "author never identifies himself anywhere in the text.<br><br>"
                    "<strong>Why the mystery?</strong><br>"
                    "Several factors contribute: (1) The author may have been well-known to the original "
                    "audience and saw no need for identification. (2) The letter is technically a sermon "
                    "(13:22, 'word of exhortation'), not a formal letter -- sermons did not require "
                    "authorial identification. (3) If the author was a woman (Priscilla, as Harnack "
                    "proposed), the name may have been suppressed in a culture reluctant to accept female "
                    "theological authority. (4) If the author was not an apostle, early Christians may "
                    "have been reluctant to attribute it to a lesser figure once it began circulating "
                    "alongside Paul's letters.<br><br>"
                    "<strong>Why Paul almost certainly did not write it:</strong><br>"
                    "(1) The Greek is vastly more polished than Paul's -- it is the most literary Greek "
                    "in the NT. Paul's style is vigorous but sometimes grammatically rough; Hebrews is "
                    "classically elegant. (2) The author says he received the gospel secondhand (2:3 -- "
                    "'it was attested to us by those who heard'), while Paul emphatically denies this "
                    "(Gal 1:11-12 -- 'I did not receive it from any man, nor was I taught it'). (3) "
                    "Paul's signature theological terms (justification by faith, flesh vs. spirit, "
                    "'in Christ') are absent. (4) Paul's method of OT quotation (mixing Hebrew and "
                    "Greek) differs from Hebrews' exclusive use of the LXX. (5) The theological "
                    "framework is different: Paul argues from the cross; Hebrews argues from the "
                    "heavenly sanctuary.<br><br>"
                    "<strong>The best candidates:</strong><br>"
                    "<strong>Apollos</strong> -- Luther's suggestion. Acts 18:24 describes Apollos as "
                    "'an eloquent man, competent in the Scriptures,' a native of Alexandria (which would "
                    "explain the Alexandrian rhetorical style and LXX expertise), who 'powerfully refuted "
                    "the Jews in public, showing by the Scriptures that the Christ was Jesus' (Acts "
                    "18:28). This matches Hebrews' method perfectly. No ancient tradition supports this, "
                    "but the circumstantial evidence is strong.<br>"
                    "<strong>Barnabas</strong> -- Tertullian's attribution (De Pudicitia 20). Barnabas "
                    "was a Levite (Acts 4:36), which would explain the detailed knowledge of the "
                    "Levitical system. He was a leader in the early church and associated with Paul.<br>"
                    "<strong>Priscilla</strong> -- Harnack's proposal (1900). She was a teacher (Acts "
                    "18:26), associated with Apollos, connected to both Rome and Ephesus. The suppression "
                    "of the author's name could be explained by gender.<br><br>"
                    "Origen's judgment from the 3rd century remains the wisest word: 'Who wrote the "
                    "epistle, in truth God knows.'"
        },
        {
            "type": "interpretation",
            "title": "The Warning Passages -- Can Believers Lose Their Salvation?",
            "body": "Hebrews contains five warning passages that are among the most debated texts in "
                    "the New Testament: 2:1-4, 3:7-4:13, 5:11-6:12, 10:26-39, and 12:14-29. The most "
                    "controversial is Hebrews 6:4-6: 'For it is impossible, in the case of those who "
                    "have once been enlightened, who have tasted the heavenly gift, and have shared in "
                    "the Holy Spirit, and have tasted the goodness of the word of God and the powers of "
                    "the age to come, and then have fallen away, to restore them again to repentance, "
                    "since they are crucifying once again the Son of God to their own harm and holding "
                    "him up to contempt.'<br><br>"
                    "<strong>The interpretive options:</strong><br>"
                    "(1) <strong>Genuine believers can lose salvation</strong> (Arminian/Wesleyan view): "
                    "The descriptions ('enlightened,' 'tasted the heavenly gift,' 'shared in the Holy "
                    "Spirit') describe genuine saving experiences. Apostasy is a real danger for real "
                    "Christians.<br>"
                    "(2) <strong>The warning is hypothetical</strong> (some Reformed view): The author "
                    "describes what WOULD happen if a believer fell away, but genuine believers never "
                    "actually do. The warning serves to prevent what it describes.<br>"
                    "(3) <strong>The people described were never truly saved</strong> (some Calvinist "
                    "view): 'Tasting' the heavenly gift is not the same as 'eating' it. These are people "
                    "who experienced the community's spiritual life externally without genuine internal "
                    "transformation.<br>"
                    "(4) <strong>The warning is about loss of reward, not salvation</strong> (Free Grace "
                    "view): Falling away means losing heavenly inheritance and reward, not losing eternal "
                    "life.<br>"
                    "(5) <strong>The 'falling away' is returning to the old covenant sacrificial system</strong> "
                    "(contextual reading): Given the audience (Jewish Christians tempted to return to "
                    "Judaism), the warning is specifically about abandoning Christ's once-for-all sacrifice "
                    "and returning to animal sacrifices -- which 'crucifies the Son of God afresh' by "
                    "implicitly declaring his sacrifice insufficient. In this reading, the impossibility "
                    "of restoration is not about God's unwillingness but about the theological dead end: "
                    "if you reject the only sacrifice that works, there is no other sacrifice left "
                    "(10:26 -- 'there no longer remains a sacrifice for sins').<br><br>"
                    "This is one of the passages where honest interpreters disagree. Hebrews is pastoral, "
                    "not systematic: the author is trying to prevent apostasy, not construct a doctrine "
                    "of perseverance. The urgency of the warning is the point."
        }
    ]
}
