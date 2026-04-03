"""
info.py — Letter of Aristeas: Scholarly Text Introduction

The foundational account of how the Hebrew Torah was translated into Greek,
producing the Septuagint (LXX) — the Bible of the early church and the
translation that shaped New Testament theology.
"""

TEXT_INFO = {
    "text_id": "letter_aristeas",
    "display_name": "Letter of Aristeas",
    "full_title": "The Letter of Aristeas to Philocrates",

    "canonical_status": {
        "status": "pseudepigrapha",
        "label": "Pseudepigrapha (not canonical in any tradition; historically important as the Septuagint origin account)",
        "detail": "The Letter of Aristeas is not canonical in any Jewish or Christian tradition, "
                  "but its historical importance is immense. It provides the only detailed narrative "
                  "of how the Hebrew Torah came to be translated into Greek under Ptolemy II "
                  "Philadelphus in Alexandria — the event that produced the Septuagint (LXX). "
                  "The LXX became the Bible of Diaspora Judaism, one of the major textual "
                  "traditions used by New Testament authors, and the Old Testament of the early "
                  "church. (NT authors drew from mixed text types including proto-Masoretic, "
                  "proto-Septuagintal, and independent traditions — many quotations align with "
                  "the LXX, but not exclusively.) Josephus "
                  "paraphrases the Letter extensively in Antiquities 12.12-118, and Philo of "
                  "Alexandria builds on its claims of divine inspiration for the Greek translation. "
                  "Church fathers from Justin Martyr to Augustine treated the Septuagint's origin "
                  "as divinely guided, largely on the authority of this letter."
    },

    "authorship": {
        "traditional": "The letter claims to be written by Aristeas, a courtier of Ptolemy II "
                       "Philadelphus (reigned 285-246 BC), to his brother Philocrates. Aristeas "
                       "describes himself as a pagan Greek official who participated in the events "
                       "surrounding the translation.",
        "scholarly_debate": "The pseudonymous authorship has been recognized since the 16th century. "
                           "The real author was an Alexandrian Jew writing approximately a century "
                           "after the events described — probably between 170 and 100 BC. Several "
                           "indicators betray the pseudonym: the author has detailed knowledge of "
                           "Jewish theology and practice that a pagan courtier would not possess, "
                           "the Greek style reflects Hellenistic Jewish literary conventions, and "
                           "certain historical details about the Ptolemaic court contain anachronisms. "
                           "The author's purpose was apologetic — to defend the authority of the "
                           "Greek Torah for Diaspora Jews who could no longer read Hebrew.",
        "bottom_line": "Written by an anonymous Alexandrian Jew (c. 170-100 BC) under the persona "
                       "of a pagan Greek courtier. The pseudonymous framing serves an apologetic "
                       "purpose: a Greek official testifying to the excellence of Jewish wisdom "
                       "and the divine character of the Greek translation."
    },

    "date": {
        "traditional": "Claims to describe events during the reign of Ptolemy II Philadelphus "
                       "(285-246 BC).",
        "critical_range": "c. 170-100 BC. Most scholars place the composition in the mid-to-late "
                         "2nd century BC, during a period when Alexandrian Jews were actively "
                         "defending their cultural and religious identity in a Hellenistic context.",
        "evidence": "The author knows the Ptolemaic court protocol well but makes certain "
                    "anachronisms — references to institutions and practices that post-date "
                    "Ptolemy II's reign. The philosophical vocabulary and rhetorical strategies "
                    "reflect mid-2nd century BC Alexandrian Jewish thought. The emphasis on the "
                    "Torah's compatibility with Greek philosophy suggests a context where this "
                    "compatibility was being challenged or needed defending. The letter's existence "
                    "by Aristobulus's time (mid-2nd century BC, if his fragments are authentic) "
                    "provides a rough terminus ante quem."
    },

    "audience": {
        "original_audience": "Diaspora Jews in Alexandria and throughout the Greek-speaking world. "
                            "These communities had largely adopted Greek as their primary language "
                            "and needed assurance that reading scripture in Greek was legitimate — "
                            "not a compromise but a divinely sanctioned translation.",
        "purpose": "To establish the authority and divine inspiration of the Greek Torah (Septuagint). "
                   "The letter accomplishes this on multiple levels: the translation was commissioned "
                   "by a great king, performed by the most learned scholars from Jerusalem itself, "
                   "completed with miraculous consensus, and ratified by the Alexandrian Jewish "
                   "community with a curse on anyone who would alter it.",
        "theological_intent": "The Greek Torah is not merely a translation but a divinely guided "
                             "rendering, equivalent in authority to the Hebrew original. Jewish "
                             "wisdom is not inferior to Greek philosophy — it is, in fact, the "
                             "source from which Greek philosophers unknowingly drew. The God of "
                             "Israel is the same God recognized by Greek philosophical theism, "
                             "but known more fully through the Torah."
    },

    "language": {
        "original": "Greek. Unlike most pseudepigrapha, the Letter of Aristeas was composed in "
                    "Greek from the outset — it is not a translation from Hebrew or Aramaic. "
                    "This reflects its Alexandrian Jewish context, where Greek was the literary "
                    "language of the community.",
        "script": "The author writes in educated Hellenistic Greek prose with features typical "
                  "of Alexandrian literary culture. The philosophical banquet dialogues employ "
                  "the conventions of Greek symposium literature. The vocabulary includes both "
                  "Hellenistic administrative terminology (court protocol, royal decrees) and "
                  "Jewish theological language adapted into Greek.",
        "linguistic_notes": "The Greek of the Letter is generally competent Hellenistic prose, "
                           "though not of the highest literary quality. It represents the kind of "
                           "educated Greek written by bilingual Alexandrian Jews. The philosophical "
                           "sections show familiarity with Peripatetic and Stoic vocabulary, adapted "
                           "to express Jewish theological concepts. The letter is an important "
                           "witness to the Greek of the Alexandrian Jewish community."
    },

    "manuscripts": {
        "earliest": "Over 20 Greek manuscripts, the earliest from the 11th century AD. "
                    "Armenian version. Josephus's paraphrase (Antiquities 12).",
        "major_witnesses": [
            {"name": "Greek manuscript tradition", "date": "11th century AD and later",
             "note": "Over 20 Greek manuscripts survive, allowing scholars to establish "
                     "a reliable critical text despite the relatively late dates."},
            {"name": "Josephus, Antiquities 12.12-118", "date": "c. 93 AD",
             "note": "Josephus paraphrases the Letter extensively, providing the earliest "
                     "datable witness to its content. His version contains some variations "
                     "that may reflect an earlier textual stage."},
            {"name": "Armenian version", "date": "medieval",
             "note": "An Armenian translation providing an independent witness to the "
                     "Greek text."},
            {"name": "Eusebius, Praeparatio Evangelica", "date": "early 4th century AD",
             "note": "Eusebius quotes substantial sections, preserving early readings "
                     "and confirming the text's circulation in Christian circles."},
            {"name": "Philo's references", "date": "1st century AD",
             "note": "Philo of Alexandria references the Septuagint's origin in terms "
                     "that depend on the Letter's account, confirming its early circulation."}
        ],
        "reliability": "The text is well preserved thanks to the large number of Greek manuscripts "
                       "and early witnesses (Josephus, Eusebius). The main outlines are not in "
                       "dispute. Minor textual variations exist between manuscripts, but the Letter "
                       "is in better textual shape than most pseudepigrapha. Josephus's paraphrase "
                       "provides an invaluable 1st century AD control for the later manuscripts."
    },

    "historical_context": {
        "setting": "The letter narrates events at the Ptolemaic court in Alexandria under Ptolemy II "
                   "Philadelphus (285-246 BC). The king, advised by his librarian Demetrius of "
                   "Phalerum, decides to add the Jewish Torah to the great Library of Alexandria. "
                   "Aristeas is sent to Jerusalem with lavish gifts, where the high priest Eleazar "
                   "selects 72 elders (six from each tribe) to perform the translation.",
        "geography": "The narrative moves between Alexandria (the Ptolemaic court and the island of "
                     "Pharos where the translation is completed) and Jerusalem (the Temple and the "
                     "high priest's court). The description of Jerusalem and the Temple is one of "
                     "the most detailed from the Second Temple period.",
        "historical_connections": "Whether or not the Letter's specific narrative is historically "
                                 "accurate, the Septuagint itself is real and transformative. The "
                                 "Greek Torah translation — however it actually came about — made "
                                 "Jewish scripture accessible to the entire Greek-speaking world. "
                                 "The New Testament authors overwhelmingly quote the Old Testament "
                                 "from Septuagintal text types, though they also drew on proto-Masoretic "
                                 "and independent traditions. Some passages involve significant LXX "
                                 "readings: in Isaiah 7:14, the Hebrew almah ('young woman of "
                                 "marriageable age') carries its own theological weight — Isaiah's sign "
                                 "required a specific, identifiable woman. The LXX's parthenos ('virgin') "
                                 "reflects an interpretive tradition that Matthew (1:23) cites as fulfilled "
                                 "in Mary's virgin conception. Both readings point to the same fulfillment; "
                                 "the Hebrew is not 'less' than the Greek — it is the foundation the Greek "
                                 "builds upon. The LXX of Deuteronomy 32:8 reads 'sons of God' (angels) "
                                 "rather than the Masoretic 'sons of Israel' — a reading now confirmed by "
                                 "the Dead Sea Scrolls (4QDeutJ). The Letter of Aristeas explains how this "
                                 "epoch-making translation came to exist and why it should be trusted."
    },

    "reader_notes": [
        {
            "type": "deeper_reading",
            "title": "LXX Authority",
            "body": "The Letter's primary purpose is to defend the Greek Torah as a divinely "
                    "authorized translation, fully equivalent to the Hebrew original. The narrative "
                    "constructs this authority on multiple levels: royal patronage (Ptolemy's "
                    "commission), scholarly credentials (72 elders chosen by the high priest), "
                    "miraculous consensus (the translators agree perfectly), and community "
                    "ratification (the Alexandrian Jews accept it with a curse on alteration). "
                    "This defense was not academic — for Diaspora Jews who could no longer read "
                    "Hebrew, the Septuagint's authority was an existential question. Could you "
                    "truly know God's word in Greek? The Letter answers with an emphatic yes, "
                    "and the early church inherited that conviction."
        },
        {
            "type": "context",
            "title": "Jewish-Hellenistic Apologetic",
            "body": "The philosophical banquet scenes (chapters 187-300), where each of the 72 "
                    "elders answers a philosophical question posed by the king, represent a "
                    "sophisticated work of Jewish cultural apologetics. The elders consistently "
                    "ground their answers in theology — every ethical and political question is "
                    "answered by reference to God as creator and sustainer. The effect is to "
                    "present Jewish wisdom as equal or superior to Greek philosophy, while "
                    "speaking in terms that Greek-educated readers would recognize and respect. "
                    "This is the same cultural negotiation visible in Philo of Alexandria and, "
                    "later, in Paul's Areopagus speech (Acts 17:22-31)."
        },
        {
            "type": "authority",
            "title": "Temple Description",
            "body": "The Letter's description of the Jerusalem Temple, its rituals, the water "
                    "system, and the priestly service (chapters 83-120) is one of the most "
                    "detailed surviving accounts from the Second Temple period. While the "
                    "description may idealize or embellish, it provides valuable evidence for "
                    "the Temple's operation, architecture, and the impression it made on visitors. "
                    "The author describes the silence of the priests at work, the elaborate water "
                    "channels, and the scale of the sacrificial system with what appears to be "
                    "either personal observation or access to reliable accounts. For scholars "
                    "reconstructing the Second Temple, this passage is an indispensable source "
                    "alongside Josephus and the Mishnah tractate Middot."
        }
    ]
}
