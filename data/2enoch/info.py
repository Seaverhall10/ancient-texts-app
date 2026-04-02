"""
info.py -- 2 Enoch: Scholarly Text Introduction

Honest scholarly introduction to the Slavonic Enoch, a major pseudepigraphic
text preserving unique traditions about seven heavens, creation, and the
Melchizedek birth narrative.
"""

TEXT_INFO = {
    "text_id": "2enoch",
    "display_name": "2 Enoch: The Book of the Secrets of Enoch",

    # -- CANONICAL STATUS -------------------------------------------------
    "canonical_status": {
        "status": "non-canonical",
        "label": "Pseudepigrapha (not in any modern canon)",
        "detail": "2 Enoch is not included in the Protestant, Catholic, Eastern Orthodox, "
                  "or Ethiopian Orthodox canons. Unlike 1 Enoch, no New Testament author "
                  "directly quotes from it, and no Dead Sea Scroll fragments have been "
                  "identified. However, the text preserves traditions about the heavenly "
                  "realm, the Watchers, and creation that overlap with and sometimes expand "
                  "upon themes found in 1 Enoch, Genesis, and the Psalms. The Melchizedek "
                  "birth narrative in the longer recension (chs. 68-73) is of particular "
                  "interest for its possible connections to Hebrews 7 and 11QMelchizedek "
                  "from Qumran. The text survives only in Old Slavonic manuscripts, making "
                  "its transmission history more opaque than that of 1 Enoch."
    },

    # -- AUTHORSHIP -------------------------------------------------------
    "authorship": {
        "traditional": "The text presents itself as the words of Enoch, the seventh from "
                       "Adam (Genesis 5:18-24), recording what he saw during his journey "
                       "through the seven heavens and the creation revelations given to him "
                       "by God before his final translation.",

        "scholarly_debate": "2 Enoch is a pseudepigraphic work attributed to the biblical "
                           "Enoch but composed by an unknown Jewish author. The date and "
                           "provenance are heavily debated:\n\n"
                           "- Most scholars place composition in the 1st century AD, possibly "
                           "before the destruction of the Temple in 70 AD (the text assumes "
                           "a functioning Temple and animal sacrifice system).\n"
                           "- Some scholars (Andersen, Orlov) argue for an Alexandrian Jewish "
                           "origin based on cosmological and calendrical affinities with "
                           "Hellenistic thought.\n"
                           "- Others (Bottrich, Macaskill) suggest a Palestinian Jewish origin "
                           "with later Slavonic Christian editing.\n"
                           "- A minority position (Vaillant) dates it much later as a medieval "
                           "composition, but this view is now largely rejected.\n\n"
                           "The text exists in two recensions: a shorter version and a longer "
                           "version. Scholarly opinion is divided on which is more original. "
                           "The Melchizedek section (chs. 68-73) appears only in the longer "
                           "recension and may be a later addition.",

        "bottom_line": "2 Enoch was not written by the biblical Enoch. It was composed by "
                       "an unknown Jewish author, most likely in the 1st century AD, and "
                       "later translated into Old Slavonic by Christian scribes. The text "
                       "preserves genuine Second Temple Jewish traditions about the heavenly "
                       "realm but has passed through Christian editorial hands, requiring "
                       "careful reading to distinguish older Jewish layers from later "
                       "Christian additions."
    },

    # -- DATE -------------------------------------------------------------
    "date": {
        "traditional": "The text claims to preserve Enoch's experiences before the Flood.",
        "critical_range": "Most likely composed in the 1st century AD (before 70 AD). "
                         "The terminus ante quem is debated: the assumption of a functioning "
                         "Temple suggests pre-70 AD, but the Slavonic translation dates to "
                         "no earlier than the 11th century AD.",
        "evidence": "Dating evidence is primarily internal: (1) The text assumes Temple "
                    "worship is ongoing (suggesting pre-70 AD composition). (2) The "
                    "cosmological scheme of seven heavens appears in Jewish texts from "
                    "the 1st century BC to 2nd century AD (Testament of Levi, Ascension "
                    "of Isaiah). (3) The solar calendar of 364 days connects to Qumran "
                    "and Jubilees traditions. (4) No Dead Sea Scroll fragments exist, "
                    "and the earliest manuscripts are medieval Slavonic copies, leaving "
                    "a significant gap in the textual history. (5) The Greek original "
                    "is lost entirely."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------
    "audience": {
        "original_audience": "Jewish readers in the 1st century AD, likely in a diaspora "
                            "setting (possibly Alexandria or another Hellenistic Jewish "
                            "community). The text's interest in cosmology, angelology, and "
                            "ethical instruction suggests a scribal-intellectual audience.",

        "purpose": "2 Enoch serves multiple purposes: (1) It provides a guided tour of the "
                   "heavenly realm, revealing the structure of the seven heavens and the "
                   "hierarchy of angelic beings. (2) It presents an alternative creation "
                   "account that expands on Genesis 1-2 with detailed cosmological "
                   "speculation. (3) It reinforces ethical monotheism through Enoch's "
                   "moral instructions to his sons. (4) It addresses the fate of the "
                   "Watchers, confirming their imprisonment and punishment. (5) The "
                   "Melchizedek birth narrative connects priestly and eschatological "
                   "traditions in ways relevant to early Jewish-Christian theology.",

        "theological_intent": "2 Enoch extends the Enochic tradition into new territory: "
                             "Where 1 Enoch focuses on the Watchers, judgment, and the Son "
                             "of Man, 2 Enoch emphasizes creation theology, heavenly geography, "
                             "and the structure of the divine administration. The throne room "
                             "vision in the tenth heaven (longer recension) or seventh heaven "
                             "(shorter recension) connects to the merkabah tradition and "
                             "Ezekiel 1. The text asks: What does God's heavenly court look "
                             "like? How is creation structured? What are the moral obligations "
                             "of those who know these secrets?"
    },

    # -- ORIGINAL LANGUAGE ------------------------------------------------
    "language": {
        "original": "The original was almost certainly Greek, translated from a possible "
                    "Hebrew or Aramaic Vorlage (underlying source text). No Greek manuscript "
                    "survives. The text is extant only in Old Slavonic (Church Slavonic).",
        "script": "Old Slavonic (Cyrillic and Glagolitic manuscripts), translated from a "
                  "lost Greek text. The standard critical edition is based on over 20 "
                  "Slavonic manuscripts dating from the 14th to 18th centuries.",
        "linguistic_notes": "The Slavonic translation preserves Semitic idioms and "
                           "constructions that suggest an underlying Semitic or Greek "
                           "original. F.I. Andersen's critical edition (OTP, 1983) and "
                           "the W.R. Morfill translation (1896, edited by R.H. Charles) "
                           "remain the standard English references. Morfill's translation "
                           "was the first English rendering and was based on a limited "
                           "number of Slavonic manuscripts available at the time.",
        "grammar_match": "The Slavonic text shows signs of translation from Greek: word "
                        "order patterns, calques, and syntactic structures that do not "
                        "arise naturally in Slavonic composition. Some Hebraisms visible "
                        "through the Greek suggest an ultimate Semitic origin for at "
                        "least parts of the text."
    },

    # -- SCRIPTURE ALIGNMENT ----------------------------------------------
    "scripture_alignment": {
        "verdict": "Mixed -- contains traditions that enrich biblical reading alongside "
                   "speculative cosmology that goes well beyond canonical revelation. "
                   "Read with discernment.",

        "where_it_aligns": [
            "The seven heavens cosmology is consistent with Paul's reference to the "
            "'third heaven' in 2 Corinthians 12:2",
            "The Watcher tradition (chs. 7, 18) aligns with Genesis 6:1-4, 1 Enoch 6-16, "
            "Jude 6, and 2 Peter 2:4",
            "The creation account expands Genesis 1-2 with details about light, darkness, "
            "and the ordering of creation that do not contradict the canonical account",
            "The throne room vision connects to Isaiah 6, Ezekiel 1, Daniel 7, and "
            "Revelation 4-5 in describing God's heavenly court",
            "The Melchizedek birth narrative (longer recension) provides background for "
            "the mysterious priest-king of Genesis 14 and Hebrews 7",
            "The solar calendar tradition connects to Jubilees and 1 Enoch's Astronomical "
            "Book, reflecting genuine Second Temple calendrical debates"
        ],

        "where_it_diverges": [
            "The detailed cosmological scheme (multiple heavens with specific contents) "
            "goes beyond anything revealed in canonical scripture",
            "The creation narrative includes speculative elements (Adoil, Arukhas) not "
            "found in Genesis or any canonical text",
            "Some ethical instructions reflect Hellenistic philosophical influence "
            "alongside Jewish Torah ethics",
            "The Melchizedek birth narrative's miraculous elements (born from a corpse, "
            "priestly from birth) are unattested in canonical texts",
            "The text's cosmography reflects ancient models rather than revealed truth"
        ],

        "reader_guidance": "2 Enoch is best read as a window into 1st century Jewish "
                          "cosmological and theological thinking. Where it aligns with "
                          "canonical scripture, it provides rich context for understanding "
                          "how Second Temple Jews visualized the heavenly realm. Where it "
                          "adds speculative details, treat these as interesting theological "
                          "reflection rather than authoritative revelation. The Melchizedek "
                          "material is particularly valuable for Hebrews study but should "
                          "not override the canonical text's own presentation."
    },

    # -- MANUSCRIPT TRADITION ---------------------------------------------
    "manuscripts": {
        "earliest": "No ancient manuscripts survive. The earliest known copies are "
                    "medieval Slavonic manuscripts from the 14th century onward. The "
                    "Greek original is entirely lost. No Hebrew, Aramaic, or Latin "
                    "versions are known.",
        "major_witnesses": [
            {"name": "Slavonic manuscripts (20+ copies)", "date": "14th-18th century AD",
             "note": "All extant manuscripts are in Old Slavonic (Church Slavonic). They "
                     "divide into a longer recension (J) and a shorter recension (A). "
                     "The relationship between the two recensions is debated."},
            {"name": "Longer recension (J)", "date": "Various medieval copies",
             "note": "Contains the Melchizedek birth narrative (chs. 68-73) and additional "
                     "material. Some scholars consider this closer to the original; others "
                     "view the additions as later expansions."},
            {"name": "Shorter recension (A)", "date": "Various medieval copies",
             "note": "A more compact version that omits or abbreviates several passages. "
                     "Some scholars consider this a condensed form of the longer text; "
                     "others see it as preserving the more original form."},
            {"name": "W.R. Morfill translation (1896)", "date": "Published 1896",
             "note": "First English translation, edited by R.H. Charles. Based on a "
                     "limited manuscript base but historically important as the text that "
                     "introduced 2 Enoch to English-speaking scholarship."},
            {"name": "F.I. Andersen critical edition (OTP, 1983)", "date": "Published 1983",
             "note": "The standard modern English translation with critical apparatus, "
                     "published in Charlesworth's Old Testament Pseudepigrapha. Based on "
                     "a comprehensive survey of available Slavonic manuscripts."}
        ],
        "reliability": "The manuscript situation for 2 Enoch is far more precarious than "
                       "for 1 Enoch. The complete loss of the Greek original and the "
                       "exclusively medieval Slavonic transmission means we are reading a "
                       "translation of a translation, with centuries of potential scribal "
                       "alteration. The existence of two recensions further complicates "
                       "reconstruction of the original text. Christian editorial activity "
                       "is evident in some manuscripts. Despite these challenges, the core "
                       "Jewish theological content appears genuine and consistent with "
                       "known Second Temple traditions."
    },

    # -- HISTORICAL CONTEXT -----------------------------------------------
    "historical_context": {
        "setting": "2 Enoch claims to describe Enoch's journey through the heavens before "
                   "the Flood, but the text was composed in the 1st century AD during a "
                   "period of intense Jewish cosmological speculation. The Second Temple "
                   "still stood, diaspora Jewish communities were engaging with Hellenistic "
                   "intellectual culture, and merkabah (divine chariot/throne) mysticism "
                   "was developing as a strand of Jewish religious practice.",

        "geography": "The text is set in cosmic geography -- seven (or ten) heavens, each "
                     "with distinct contents and inhabitants. Earthly anchors include "
                     "Enoch's homeland (unspecified) and the location where he instructs "
                     "his sons. The Melchizedek section references Nir (Noah's brother) "
                     "and Sopanima, connecting to the patriarchal narratives. If composed "
                     "in Alexandria, the text reflects the rich intellectual environment "
                     "of the largest Jewish diaspora community.",

        "historical_connections": "2 Enoch connects to several historical currents: "
                                 "(1) The merkabah mysticism tradition that would later "
                                 "develop into the Hekhalot literature. (2) Hellenistic "
                                 "Jewish cosmological speculation (Philo of Alexandria's "
                                 "similar interests in the heavenly realm). (3) The ongoing "
                                 "Enochic tradition that produced 1 Enoch, Jubilees, and "
                                 "the Book of Giants. (4) Pre-70 AD debates about priesthood, "
                                 "calendar, and Temple worship. (5) Early Jewish-Christian "
                                 "interest in Melchizedek as a priestly-messianic figure "
                                 "(Hebrews 7, 11QMelchizedek)."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------
    "divine_council": {
        "relevance": "central",
        "summary": "2 Enoch provides one of the most detailed descriptions of the heavenly "
                   "hierarchy in all of Second Temple literature. The journey through the "
                   "seven heavens reveals a structured divine administration with multiple "
                   "ranks of angelic beings, each with specific functions and territories. "
                   "This directly supports the divine council framework:\n\n"
                   "- The throne room vision (7th/10th heaven) parallels Isaiah 6, "
                   "Ezekiel 1, Daniel 7, and 1 Kings 22:19-22 in depicting God surrounded "
                   "by his heavenly court.\n"
                   "- The imprisoned Watchers in the 2nd and 5th heavens confirm the "
                   "tradition of rebellious divine beings held in chains of darkness "
                   "(cf. Jude 6, 2 Peter 2:4, 1 Enoch 10-16).\n"
                   "- The angelic hierarchy (archangels, cherubim, seraphim, ophanim) "
                   "maps onto the biblical portrayal of God's heavenly host.\n"
                   "- The Melchizedek birth narrative connects to the divine council's "
                   "role in establishing priestly mediation between heaven and earth.\n\n"
                   "For Heiser's framework, 2 Enoch reinforces the reality of the "
                   "heavenly council as a governing body, confirms the Watcher rebellion "
                   "tradition, and provides rich detail about the structure of the unseen "
                   "realm that the biblical authors assumed but did not always make explicit.",

        "key_connections": [
            "The Unseen Realm, chs. 2-4 (divine council as heavenly bureaucracy)",
            "Reversing Hermon (Watcher tradition across Second Temple literature)",
            "Angels (2018) -- heavenly hierarchy and angelic categories",
            "The Naked Bible Podcast, episodes on 2 Corinthians 12 and heavenly ascent"
        ]
    },

    # -- KEY CONTENT SUMMARY ----------------------------------------------
    "key_content": {
        "seven_heavens": "Enoch is taken through seven (or ten) heavens, each containing "
                        "distinct features: the 1st heaven holds weather phenomena; the "
                        "2nd holds imprisoned rebellious angels (Watchers); the 3rd holds "
                        "paradise and the place of punishment; the 4th holds the sun and "
                        "moon with their chariots; the 5th holds the Grigori (more "
                        "Watchers); the 6th holds archangels who govern cosmic order; "
                        "the 7th (or 10th in the longer recension) holds God's throne.",

        "creation_account": "God reveals to Enoch how He created the visible and invisible "
                           "world. Key elements include the primordial beings Adoil (from "
                           "whom light comes) and Arukhas (from whom darkness comes), the "
                           "ordering of the elements, and the creation of Adam. This account "
                           "expands Genesis 1-2 with cosmological detail.",

        "solar_calendar": "Like 1 Enoch and Jubilees, 2 Enoch supports a 364-day solar "
                         "calendar, connecting to the calendrical debates between the "
                         "Qumran community and the Jerusalem Temple establishment.",

        "watcher_punishment": "2 Enoch confirms the imprisonment of the Watchers who "
                             "descended to earth and corrupted humanity. They are found "
                             "in the 2nd heaven (weeping) and the 5th heaven (silent and "
                             "grieving), awaiting final judgment.",

        "melchizedek_birth": "In the longer recension (chs. 68-73), Melchizedek is born "
                            "miraculously from the corpse of Sopanima (wife of Nir, "
                            "Noah's brother). The child bears the priestly insignia from "
                            "birth and is taken by the archangel Michael to paradise to "
                            "preserve the priestly line through the Flood. This tradition "
                            "illuminates the 'without father, without mother, without "
                            "genealogy' description in Hebrews 7:3.",

        "enoch_testament": "Before his final translation to heaven, Enoch delivers ethical "
                          "and theological instruction to his sons: care for the poor, "
                          "right worship, moral living, and the coming judgment. These "
                          "instructions reflect both Torah ethics and wisdom literature "
                          "traditions."
    },

    # -- RELIABILITY RATING -------------------------------------------------
    "reliability": {
        "rating": "LOW",
        "score": "1/5",
        "comparison": "For context: 1 Enoch = 4/5 (Jude quotes it, 11 Qumran copies, "
                     "Ethiopian canon). Jubilees = 4/5 (15+ Qumran fragments, Ethiopian "
                     "canon). Book of Giants = 3/5 (6 Qumran manuscripts). Sirach = 4/5 "
                     "(Qumran + Masada fragments, Catholic/Orthodox canon, known author). "
                     "2 Enoch = 1/5 (no ancient copies, no NT citation, Slavonic only, "
                     "possible medieval composition).",
        "why_low": [
            "Zero Dead Sea Scroll fragments (1 Enoch has 11 copies at Qumran)",
            "No New Testament author cites or references it (Jude quotes 1 Enoch as prophecy)",
            "Not in any canon -- Protestant, Catholic, Orthodox, or Ethiopian",
            "Survives ONLY in medieval Slavonic manuscripts (14th century earliest)",
            "The Greek original is completely lost -- no ancient witness in any language",
            "Two conflicting recensions with no way to determine which is original",
            "Christian scribal editing is evident in multiple manuscripts",
            "A minority of scholars argue it may be a medieval Slavonic composition entirely",
            "The Melchizedek birth narrative (chs. 68-73) is almost certainly a later addition"
        ]
    },

    # -- BIBLICAL TENSIONS & PROBLEMS --------------------------------------
    "biblical_tensions": [
        {
            "issue": "Adoil and Arukhas -- non-biblical creation beings",
            "location": "Chapters 24-25",
            "description": "2 Enoch introduces Adoil (a great light-being) and Arukhas "
                          "(a darkness-being) as primordial entities from which God draws "
                          "light and the physical foundations of creation. These beings "
                          "have no basis in Genesis 1, Isaiah 45:7, or any canonical text. "
                          "They appear to be speculative cosmogony influenced by Hellenistic "
                          "dualist philosophy.",
            "severity": "SIGNIFICANT -- introduces non-biblical cosmological entities"
        },
        {
            "issue": "Ten heavens vs. three/seven in other traditions",
            "location": "Longer recension throughout",
            "description": "The longer recension of 2 Enoch describes ten heavens, while "
                          "the shorter has seven. Paul references the 'third heaven' "
                          "(2 Cor 12:2) and other Jewish traditions use seven. The ten-heaven "
                          "scheme appears to be a later inflation with no scriptural warrant.",
            "severity": "MODERATE -- speculative cosmology beyond scriptural revelation"
        },
        {
            "issue": "Melchizedek born from a corpse",
            "location": "Chapters 68-73 (longer recension only)",
            "description": "The Melchizedek birth narrative claims he was born miraculously "
                          "from the dead body of Sopanima (wife of Nir, Noah's brother). "
                          "This contradicts Hebrews 7:3 which emphasizes Melchizedek as "
                          "'without father, without mother, without genealogy' -- 2 Enoch "
                          "gives him both parents and a genealogy. The narrative is likely "
                          "a later Christian addition attempting to explain Hebrews 7.",
            "severity": "SIGNIFICANT -- contradicts Hebrews 7:3 interpretation"
        },
        {
            "issue": "Trinitarian-sounding language",
            "location": "Various passages in longer recension",
            "description": "Some passages contain language that sounds Trinitarian, which "
                          "would be anachronistic for a 1st century Jewish text. These are "
                          "almost certainly Christian scribal additions inserted during "
                          "centuries of Slavonic manuscript transmission.",
            "severity": "MODERATE -- evidence of Christian editorial contamination"
        },
        {
            "issue": "Enoch as pre-existent being",
            "location": "Chapter 23 (longer recension)",
            "description": "Some passages hint at Enoch's pre-existence or identification "
                          "with a heavenly figure in ways that go beyond Genesis 5:24 and "
                          "the canonical presentation. This may reflect later metatron "
                          "traditions that developed in rabbinic and mystical Judaism.",
            "severity": "MINOR -- speculative expansion of Enoch's role"
        },
        {
            "issue": "No external verification of key claims",
            "location": "Throughout",
            "description": "Unlike 1 Enoch (whose Watcher tradition is confirmed by Jude "
                          "14-15, 2 Peter 2:4, Genesis 6:1-4, and 11 Qumran manuscripts), "
                          "2 Enoch's distinctive content -- Adoil/Arukhas, the ten heavens, "
                          "the Melchizedek birth -- has zero external support from any "
                          "canonical or ancient text. Every unique claim in 2 Enoch stands "
                          "alone.",
            "severity": "CRITICAL -- no independent attestation for distinctive material"
        }
    ],

    # -- WARNINGS / READER NOTES ------------------------------------------
    "reader_notes": [
        {
            "type": "warning",
            "title": "RELIABILITY WARNING: This Is the Weakest Text in the App",
            "body": "2 Enoch has the lowest reliability rating of any text in this app. "
                    "No ancient manuscripts survive. No NT author cites it. No Qumran "
                    "fragments exist. It survives only in medieval Slavonic copies that "
                    "show evidence of Christian editorial tampering. It is included here "
                    "as a window into Second Temple cosmological thinking, NOT as an "
                    "authoritative source. Every claim unique to 2 Enoch should be held "
                    "with extreme caution. Where it agrees with canonical scripture and "
                    "1 Enoch, the canonical/1 Enoch version is the reliable source -- "
                    "not 2 Enoch."
        },
        {
            "type": "warning",
            "title": "The Melchizedek Section Is Probably Not Original",
            "body": "Chapters 68-73 (the Melchizedek birth narrative) appear only in the "
                    "longer recension and are almost certainly a later addition -- likely "
                    "by a Christian editor trying to explain Hebrews 7:3. Ironically, the "
                    "narrative contradicts Hebrews by giving Melchizedek parents and a "
                    "genealogy. Do not use this section to build theology about Melchizedek."
        },
        {
            "type": "context",
            "title": "Why Include It At All?",
            "body": "Despite its problems, 2 Enoch preserves some genuine Second Temple "
                    "Jewish traditions about heavenly geography that help us understand "
                    "how Paul's 'third heaven' (2 Cor 12:2), the Watcher imprisonment "
                    "(Jude 6, 2 Pet 2:4), and merkabah throne visions (Ezekiel 1, "
                    "Isaiah 6, Revelation 4) were understood by Jewish readers in the "
                    "1st century. The text is included for CONTEXT, not as a source of "
                    "doctrine. Think of it as reading a contemporary commentary, not "
                    "reading Scripture."
        },
        {
            "type": "context",
            "title": "The Recension Problem",
            "body": "2 Enoch exists in two significantly different versions: a longer "
                    "recension and a shorter recension. Scholars disagree on which is "
                    "more original. The most theologically interesting material "
                    "(Melchizedek birth, ten heavens, Adoil/Arukhas) appears only in the "
                    "longer version and may be later additions. 'What 2 Enoch says' "
                    "depends on which recension you are reading."
        },
        {
            "type": "warning",
            "title": "Christian Editorial Contamination",
            "body": "Slavonic manuscripts were copied by Christian scribes for centuries. "
                    "Trinitarian-sounding language, christological insertions, and other "
                    "Christian editorial additions are present in the text. There is no "
                    "way to cleanly separate the original Jewish composition from later "
                    "Christian layers. Read with awareness that what you see may not be "
                    "what was originally written."
        }
    ]
}
