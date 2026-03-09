"""
info.py -- Josephus: Scholarly Text Introduction

Titus Flavius Josephus (born Yosef ben Matityahu, 37-100 AD) is the single most
important non-biblical source for Second Temple Judaism, the Jewish revolt against
Rome, and the world in which Jesus and the early church emerged. A priest of the
first course (Jehoiarib), a Pharisee by conviction, a failed military commander
turned Roman client, and a prolific historian -- Josephus is indispensable and
deeply problematic in equal measure.

His four surviving works span the arc from Jewish War (written under Flavian
patronage in the late 70s AD) to Against Apion (his final apologetic, ca. 97 AD).
Across these works, scholars have detected a significant tonal evolution: the early
Josephus writes as a Roman propagandist justifying the destruction of Jerusalem;
the late Josephus writes as a defender of Jewish civilization and a man grappling
with the meaning of Israel's catastrophe. The Testimonium Flavianum (Antiquities
18.63-64) sits at the center of this evolution and remains the most debated passage
in all of ancient historiography.
"""

TEXT_INFO = {
    "text_id": "josephus",
    "display_name": "Josephus",

    # -- CANONICAL STATUS --
    "canonical_status": {
        "status": "non-canonical",
        "label": "Non-Canonical -- Greco-Roman Historical Writing",
        "detail": "The works of Josephus have never been considered scripture by any "
                  "Jewish or Christian tradition. They are historical prose written by "
                  "a Jewish priest for a Roman audience. However, Josephus was preserved "
                  "almost exclusively by Christian scribes, who valued his writings as "
                  "independent corroboration of biblical history and as a witness to "
                  "the destruction of Jerusalem -- which the church fathers interpreted "
                  "as divine judgment for the rejection of Christ (Eusebius, Ecclesiastical "
                  "History 3.5-8). This Christian transmission history is directly relevant "
                  "to the Testimonium Flavianum debate: the manuscripts passed through "
                  "centuries of Christian copyists who had both motive and opportunity "
                  "to alter the text. Josephus's value is not as scripture but as the "
                  "richest surviving witness to the world of the Bible in its final centuries."
    },

    # -- AUTHORSHIP --
    "authorship": {
        "traditional": "Josephus identifies himself extensively. Born Yosef ben Matityahu "
                       "(Joseph son of Matthias) in 37 AD, he was a priest of the first "
                       "course (Jehoiarib, 1 Chronicles 24:7) and claimed royal Hasmonean "
                       "descent through his mother. He studied with the Pharisees, Sadducees, "
                       "and Essenes in his youth, spending three years with a desert ascetic "
                       "named Bannus before adopting Pharisaic practice at age 19 (Life 10-12). "
                       "Appointed commander of Galilee during the revolt (66 AD), he was "
                       "captured at Jotapata and famously prophesied that Vespasian would "
                       "become emperor (War 3.400-402). After the war, he lived in Rome under "
                       "Flavian patronage, taking the name Titus Flavius Josephus. He wrote "
                       "four works: Jewish War (~75-79 AD), Jewish Antiquities (~93-94 AD), "
                       "Life (~94-95 AD), and Against Apion (~97 AD).",

        "scholarly_debate": "There is no serious doubt that Josephus authored all four works. "
                           "The question is not WHO wrote them but HOW FREELY he wrote. Jewish "
                           "War was composed under Flavian patronage -- Josephus states that "
                           "Vespasian and Titus themselves read and approved the work (Life 363, "
                           "Against Apion 1.50-51). This raises the question of Roman editorial "
                           "influence: did Josephus suppress material unfavorable to Rome? Did "
                           "he exaggerate Jewish factionalism to deflect blame from Roman "
                           "aggression? Steve Mason (2016) argues that War is essentially "
                           "Flavian propaganda dressed in Thucydidean prose. Tessa Rajak (2002) "
                           "takes a more nuanced view: Josephus had genuine literary and "
                           "theological purposes even while writing under constraint. By the "
                           "time of Antiquities (15 years later), Josephus writes with "
                           "noticeably more independence -- he is more sympathetic to Jewish "
                           "traditions, more willing to criticize Roman governors, and more "
                           "open about messianic expectations. Whether this reflects growing "
                           "confidence, fading Flavian oversight (Domitian was less interested "
                           "in Josephus than Titus had been), or genuine theological development "
                           "is debated.\n\n"
                           "Josephus also had literary assistants (synergoi) who helped with "
                           "his Greek (Against Apion 1.50). Some scholars (Thackeray, 1929) "
                           "detected different 'assistants' across different sections of "
                           "Antiquities based on stylistic variation. This has implications "
                           "for the Testimonium: if the passage's style differs from its "
                           "context, this might reflect an assistant's hand rather than "
                           "Christian interpolation.",

        "bottom_line": "Josephus wrote all four works, but under evolving circumstances. "
                       "The early War reflects Flavian constraints and Roman-friendly bias. "
                       "The later Antiquities and Against Apion reflect a more independent, "
                       "more Jewish, and more personally reflective author. Understanding "
                       "this tonal evolution is essential to evaluating every passage, "
                       "especially the Jesus references."
    },

    # -- DATE --
    "date": {
        "traditional": "Jewish War: ~75-79 AD (under Vespasian and Titus). "
                       "Jewish Antiquities: ~93-94 AD (in the 13th year of Domitian, "
                       "as Josephus states at Ant. 20.267). "
                       "Life: ~94-95 AD (published as an appendix to Antiquities). "
                       "Against Apion: ~97 AD (Josephus's final work, after Agrippa II's "
                       "death mentioned at Life 359-360).",
        "critical_range": "The dates are among the most secure in ancient literature because "
                         "Josephus repeatedly anchors his writings to known events and "
                         "imperial reigns. War was completed before Vespasian's death (79 AD). "
                         "Antiquities was completed in Domitian's 13th year (93/94 AD). Against "
                         "Apion followed shortly after, likely ~96-100 AD. Josephus's date of "
                         "death is unknown but assumed to be around 100 AD.",
        "evidence": "Internal dating markers: War 7.158 references the temple of Pax "
                    "(dedicated 75 AD). Ant. 20.267 gives the 13th year of Domitian (93/94). "
                    "Life 359 references Agrippa II, who died ~92-100 AD. The relative "
                    "chronology is certain: War first, then Antiquities, then Life "
                    "(as an appendix to Antiquities), then Against Apion last."
    },

    # -- AUDIENCE & PURPOSE --
    "audience": {
        "original_audience": "Josephus wrote for multiple audiences simultaneously. Jewish War "
                            "was explicitly written for 'the upper barbarians' (Parthians and "
                            "Mesopotamian Jews) in Aramaic, then rewritten in Greek for the "
                            "Greco-Roman educated public (War 1.3). Antiquities was addressed "
                            "to a Roman patron named Epaphroditus and aimed to present Jewish "
                            "history as comparable in antiquity and wisdom to Greek civilization. "
                            "Against Apion was a direct response to anti-Jewish polemicists, "
                            "defending Jewish culture against Alexandrian slanders.",

        "purpose": "Josephus had overlapping purposes that shifted over time. In War, his "
                   "primary goal was to explain the Jewish revolt to a Roman audience while "
                   "defending his own conduct and the Jewish people's essential loyalty to Rome "
                   "(blaming the revolt on a small faction of zealots). In Antiquities, his "
                   "purpose broadened: he wanted to demonstrate that Jewish civilization was "
                   "ancient, philosophically sophisticated, and worthy of Roman respect. By "
                   "Against Apion, his purpose had become overtly apologetic -- a passionate "
                   "defense of Jewish monotheism, law, and way of life as superior to pagan "
                   "alternatives. This progression from political apology to cultural defense "
                   "to theological conviction is the tonal arc that scholars track.",

        "theological_intent": "Josephus was a Pharisee and a priest, and his theology permeates "
                             "his work even when he writes as a 'historian.' He consistently "
                             "interprets Jewish history through the lens of divine providence: "
                             "God rewards obedience and punishes transgression (Ant. 1.14, 20.166). "
                             "He interprets the Temple's destruction as divine judgment for the "
                             "sins of the Zealots who defiled it (War 5.412, 6.110). He describes "
                             "prophecy as genuine foreknowledge given by God (War 3.351-354, his "
                             "own Vespasian prophecy). He presents the Jewish sects as philosophical "
                             "schools comparable to Greek ones, with the Pharisees resembling Stoics "
                             "and the Essenes resembling Pythagoreans (Ant. 15.371, War 2.119-166). "
                             "His theology of history is fundamentally Deuteronomistic: Israel "
                             "prospers under God when faithful, suffers when disobedient."
    },

    # -- ORIGINAL LANGUAGE --
    "language": {
        "original": "Koine Greek (the literary works that survive). Josephus states that he "
                    "first composed Jewish War in Aramaic for the 'upper barbarians' "
                    "(War 1.3), but this Aramaic version is entirely lost. The Greek text "
                    "that survives is either a translation or a free rewriting by Josephus "
                    "with the help of Greek-speaking literary assistants.",
        "script": "Greek uncial script in the earliest manuscripts. No Hebrew or Aramaic "
                  "manuscripts of any Josephan work survive.",
        "linguistic_notes": "Josephus's Greek is literary Koine with strong Atticizing tendencies -- "
                           "he modeled his style on Thucydides, Polybius, and Dionysius of "
                           "Halicarnassus. His vocabulary is extensive (over 5,000 distinct words "
                           "across his corpus). Thackeray (1929) detected at least two different "
                           "levels of Greek style in Antiquities, suggesting the use of different "
                           "literary assistants for different sections. The Testimonium Flavianum "
                           "(Ant. 18.63-64) has been analyzed stylistically by multiple scholars: "
                           "some (Feldman) argue its vocabulary matches Josephan usage; others "
                           "(Olson) argue key phrases are un-Josephan. The linguistic evidence "
                           "alone is inconclusive.",
        "grammar_match": "The Greek of Josephus is consistent with educated literary Koine of the "
                        "late first century AD. It matches the conventions of Greco-Roman "
                        "historiography (Thucydides, Polybius, Dionysius) and is distinct from "
                        "the simpler Koine of the New Testament or the technical Greek of the "
                        "Septuagint."
    },

    # -- SCRIPTURE ALIGNMENT --
    "scripture_alignment": {
        "verdict": "Josephus is NOT scripture. He is an independent historical witness whose "
                   "testimony sometimes confirms, sometimes supplements, and occasionally "
                   "contradicts the biblical record. His value is as corroboration and context, "
                   "not as revelation.",
        "nt_usage": "Josephus provides independent attestation for numerous figures mentioned in "
                    "the New Testament: Herod the Great (Ant. 14-17), Herod Antipas (Ant. 18), "
                    "Pontius Pilate (Ant. 18.35, 55-89), the high priests Annas and Caiaphas "
                    "(Ant. 18.26, 34-35), King Agrippa I (Ant. 19.343-350, cf. Acts 12), "
                    "the Pharisees and Sadducees (War 2.119-166, Ant. 13.171-173), John the "
                    "Baptist (Ant. 18.116-119), James the brother of Jesus (Ant. 20.200), "
                    "and -- most controversially -- Jesus himself (Ant. 18.63-64). He also "
                    "provides the only detailed eyewitness account of the Temple's destruction "
                    "in 70 AD, the event that Jesus prophesied (Mark 13:1-2, Luke 21:5-6).",
        "internal_consistency": "Josephus is broadly consistent with the biblical timeline for the "
                               "Hasmonean and Herodian periods. His account of Herod the Great "
                               "largely aligns with Matthew 2 (the paranoia, the cruelty, the "
                               "death date). His account of the Jewish sects illuminates the "
                               "Pharisee/Sadducee debates in the Gospels. However, there are "
                               "discrepancies: his chronology of the governors does not always "
                               "match Acts precisely, and his portrayal of events sometimes "
                               "diverges from the NT perspective."
    },

    # -- MANUSCRIPT TRADITION --
    "manuscripts": {
        "earliest": "The earliest surviving manuscripts of Josephus date to the 9th-11th centuries "
                    "AD -- a gap of roughly 800-900 years from composition. This is comparable to "
                    "most classical authors but far worse than the New Testament or Dead Sea Scrolls. "
                    "The manuscript tradition is entirely Christian: no Jewish manuscripts of "
                    "Josephus survive from antiquity.",
        "major_witnesses": [
            {"name": "Greek manuscripts", "date": "9th-15th century AD",
             "note": "Approximately 133 Greek manuscripts survive, divided into two families. "
                     "The most important are: Codex Parisinus gr. 1425 (11th century, for "
                     "Antiquities 1-10) and Codex Ambrosianus F 128 (11th century, for "
                     "Antiquities 11-20 and Life). No single manuscript preserves all of Josephus."},
            {"name": "Latin translation (Pseudo-Hegesippus)", "date": "4th century AD",
             "note": "A free Latin paraphrase of Jewish War, significantly reworked with Christian "
                     "theological interpretation. Not a reliable witness to Josephus's original text "
                     "but valuable as evidence of early Christian reception."},
            {"name": "Latin translation (Cassiodorus)", "date": "6th century AD",
             "note": "A more literal Latin translation of Antiquities commissioned by Cassiodorus. "
                     "Important for textual criticism where it preserves readings lost in the Greek."},
            {"name": "Slavonic Josephus", "date": "11th-12th century AD",
             "note": "An Old Russian version of Jewish War containing extensive interpolations about "
                     "Jesus and John the Baptist not found in any Greek manuscript. Most scholars "
                     "consider these additions medieval Christian expansions, though Eisler (1929) "
                     "controversially argued they preserved original Josephan material."},
            {"name": "Arabic Testimonium (Agapius)", "date": "10th century AD",
             "note": "The 10th-century Melkite bishop Agapius of Hierapolis preserves an Arabic "
                     "version of the Testimonium Flavianum in his Universal History that reads more "
                     "neutrally than the Greek: 'He was perhaps the Messiah' rather than 'He was "
                     "the Christ.' Many scholars consider this closer to what Josephus originally wrote."}
        ],
        "reliability": "The text of Josephus is reasonably well-preserved for a classical author, "
                       "but the Christian transmission history creates unique problems. Every passage "
                       "touching on Jesus or Christian origins must be evaluated for possible "
                       "interpolation. The Testimonium Flavianum (Ant. 18.63-64) is the most "
                       "contested passage, but scholars also debate smaller phrases throughout the "
                       "corpus. The Syriac and Arabic versions occasionally preserve readings that "
                       "may be closer to the original than the Greek manuscripts."
    },

    # -- HISTORICAL CONTEXT --
    "historical_context": {
        "setting": "Josephus lived through the most catastrophic period in Jewish history since "
                   "the Babylonian exile. Born in 37 AD (the year Caligula became emperor), he "
                   "came of age in a Jerusalem seething with messianic expectation, factional "
                   "strife, and tension with Rome. He personally participated in the Great "
                   "Revolt (66-73 AD), survived the siege of Jotapata (67 AD), witnessed the "
                   "siege and destruction of Jerusalem and the Temple (70 AD), and spent his "
                   "remaining decades in Rome processing what it all meant.",

        "geography": "Josephus's works cover the entire Jewish world: Jerusalem and Judea "
                     "(the center of his narrative), Galilee (where he commanded during the "
                     "revolt), the Decapolis, Idumea, Perea, the Jewish diaspora in Alexandria "
                     "and Mesopotamia, and Rome itself (where he lived and wrote). His "
                     "description of Jerusalem and the Temple (War 5.136-247) is the most "
                     "detailed surviving ancient account and has been confirmed by archaeology "
                     "at numerous points.",

        "historical_connections": "Josephus is the primary source for: the Hasmonean dynasty "
                                 "(167-63 BC), the rise of Herod the Great (37-4 BC), the "
                                 "Roman governors of Judea (6-66 AD), the Jewish sects (Pharisees, "
                                 "Sadducees, Essenes, Fourth Philosophy), the Great Revolt (66-73 AD), "
                                 "and the fall of Masada (73/74 AD). Without Josephus, our knowledge "
                                 "of the intertestamental and New Testament period would be reduced "
                                 "to fragmentary notices in Roman historians (Tacitus, Suetonius, "
                                 "Dio Cassius) and the New Testament itself."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --
    "divine_council": {
        "relevance": "moderate",
        "summary": "Josephus is not a theologian of the divine council in the way that 1 Enoch "
                   "or the Dead Sea Scrolls are. However, his works contain significant material "
                   "relevant to the council framework: (1) His descriptions of the Essenes include "
                   "their angelology and belief in the immortality of souls (War 2.154-158), which "
                   "connects to the Qumran community's intense divine council theology. (2) His "
                   "account of the Jewish sects preserves the Sadducees' denial of angels and the "
                   "Pharisees' affirmation of them (cf. Acts 23:8). (3) His retelling of OT "
                   "narratives in Antiquities systematically de-angelizes some passages (e.g., "
                   "softening the angel of the LORD encounters) while retaining others, revealing "
                   "how a sophisticated first-century Jew navigated divine intermediary theology "
                   "for a pagan audience. (4) His account of prophecy -- both biblical prophets "
                   "and his own prophetic experience at Jotapata -- engages with the question of "
                   "divine communication through intermediaries. (5) His descriptions of the "
                   "Temple and its symbolism (War 5.212-218) connect the earthly sanctuary to "
                   "the cosmic order in ways that echo divine council cosmology.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 31 (Josephus on Jewish sects and angels)",
            "Reversing Hermon, chapters 6-7 (Josephus's retelling of Genesis traditions)",
            "The Naked Bible Podcast, episodes on Second Temple Judaism and the historical Jesus"
        ]
    },

    # -- WARNINGS / READER NOTES --
    "reader_notes": [
        {
            "type": "context",
            "title": "Josephus the Survivor",
            "body": "Everything Josephus wrote must be read through the lens of a man who "
                    "survived by switching sides. He was a Jewish commander who surrendered "
                    "to Rome, prophesied Vespasian's rise, and lived in Rome on imperial "
                    "patronage while Jerusalem burned. His fellow Jews considered him a "
                    "traitor. His Roman patrons expected favorable coverage. Every sentence "
                    "he wrote navigated these competing pressures. This does not make him "
                    "unreliable -- it makes him a source who must be read critically, with "
                    "awareness of what he had reason to emphasize, minimize, or omit."
        },
        {
            "type": "scholarship",
            "title": "The Testimonium Problem",
            "body": "Antiquities 18.63-64 contains the most famous and controversial passage "
                    "in Josephus: 'About this time there lived Jesus, a wise man, if indeed "
                    "one ought to call him a man...' In its current form, the passage affirms "
                    "Jesus as the Messiah, the performer of 'surprising deeds,' and the risen "
                    "Lord -- statements that a non-Christian Jew almost certainly would not have "
                    "written. The scholarly consensus is that Josephus wrote SOMETHING about Jesus "
                    "in this location (a total interpolation would be harder to explain than a "
                    "partial one), but that Christian scribes expanded the passage. The original "
                    "likely identified Jesus as a 'wise man' and teacher who was crucified under "
                    "Pilate and had continuing followers. The Arabic version preserved by Agapius "
                    "may reflect something closer to the original. This study examines the evidence "
                    "in detail."
        },
        {
            "type": "interpretation",
            "title": "The Tonal Evolution",
            "body": "One of the most rewarding ways to read Josephus is to trace his evolving "
                    "voice across his career. In Jewish War (late 70s), he writes as a Roman "
                    "client explaining Jewish catastrophe to a Greek audience -- his tone is "
                    "detached, Thucydidean, and pro-Flavian. In Antiquities (93/94), written "
                    "15 years later, he is warmer toward Jewish traditions, more willing to "
                    "criticize Roman governors (Pilate, Florus), and more openly engaged with "
                    "messianic and prophetic themes. In Against Apion (late 90s), he is "
                    "passionately defensive of Jewish identity, monotheism, and the superiority "
                    "of Moses's legislation. And in Life (his autobiography), he is combative "
                    "and personal, settling scores with rivals. This progression -- from Roman "
                    "propagandist to Jewish apologist -- is the narrative arc this study traces."
        },
        {
            "type": "theology",
            "title": "Josephus and the Divine Council -- Angels, Prophecy, and the Sects",
            "body": "While Josephus is not a theologian writing about the divine council, his "
                    "descriptions of Jewish beliefs about angels and spiritual beings are invaluable "
                    "for understanding the world of the New Testament. His accounts of the three "
                    "major Jewish sects reveal a sharp divide: the Sadducees 'do away with fate "
                    "entirely' and deny the existence of angels and spirits (War 2.165; cf. Acts "
                    "23:8), while the Pharisees affirm both fate and free will, believe in the "
                    "immortality of the soul, and acknowledge angelic beings (War 2.162-163; Ant. "
                    "18.14). The Essenes, whom Josephus describes most admiringly, believe in strict "
                    "predestination, practice intensive purity rituals, and hold secrets about 'the "
                    "names of the angels' (War 2.142) -- a detail that connects directly to the "
                    "Qumran community's elaborate angelology in texts like the Songs of Sabbath "
                    "Sacrifice and the War Scroll. Josephus himself claims prophetic ability: at "
                    "Jotapata, he says God gave him foreknowledge of Vespasian's rise through dream "
                    "interpretation (War 3.351-354). He interprets the entire history of Israel "
                    "through the lens of divine providence -- God rewarding obedience and punishing "
                    "transgression -- which is fundamentally the Deuteronomistic theology that also "
                    "undergirds the divine council worldview."
        },
        {
            "type": "warning",
            "title": "How Reliable Is Josephus? Where He Confirms and Contradicts the Bible",
            "body": "Josephus is neither a neutral journalist nor a propagandist without value. "
                    "His reliability varies significantly depending on the topic and the work. "
                    "Where he confirms the Bible: His accounts of Herod the Great's paranoia and "
                    "cruelty (Ant. 14-17) make the massacre of the innocents in Matthew 2 entirely "
                    "plausible -- Herod killed his own wife and three sons; slaughtering Bethlehem "
                    "infants would have been a footnote to his reign. His description of Pontius "
                    "Pilate's provocations (Ant. 18.55-89) matches the Gospels' portrait of a "
                    "governor willing to bend to Jewish pressure. His account of John the Baptist "
                    "(Ant. 18.116-119) independently confirms John's existence, popularity, and "
                    "execution by Herod Antipas. His reference to James 'the brother of Jesus, "
                    "who was called Christ' (Ant. 20.200) is a virtually undisputed independent "
                    "attestation of Jesus' historicity. Where he must be read critically: Josephus "
                    "systematically downplays messianic expectation in Jewish War (to avoid "
                    "alarming Roman readers), inflates troop numbers and casualty figures (a common "
                    "ancient practice), sanitizes his own conduct during the war, and presents "
                    "Jewish theology through Greek philosophical categories that sometimes distort "
                    "the original concepts. His biases are consistent and predictable: pro-Roman in "
                    "War, pro-Jewish in Antiquities, and always self-serving. Knowing the biases "
                    "makes him more useful, not less."
        },
        {
            "type": "context",
            "title": "The Destruction of the Temple -- Josephus as Eyewitness",
            "body": "Josephus's account of the Temple's destruction in 70 AD (War 5-7) is the most "
                    "detailed eyewitness account of the event that Jesus prophesied in Mark 13:1-2, "
                    "Matthew 24:1-2, and Luke 21:5-6. For readers of the New Testament, this account "
                    "is essential reading because it shows exactly what happened when Jesus' prophecy "
                    "came true. Josephus describes the Roman siege of Jerusalem, the famine inside "
                    "the walls that drove people to cannibalism (War 6.193-213), the burning of the "
                    "Temple by Roman soldiers despite Titus's alleged order to preserve it (War "
                    "6.241-266), and the systematic demolition that left not one stone upon another "
                    "(War 7.1-4) -- precisely as Jesus had said. Josephus interprets the destruction "
                    "as divine judgment, not for rejecting Jesus (he does not make this connection), "
                    "but for the Zealots' defilement of the Temple with civil bloodshed (War 5.412; "
                    "6.110). The early church fathers, however, explicitly connected Josephus's "
                    "account with Jesus' prophecy and interpreted the destruction as God's judgment "
                    "on Israel for rejecting the Messiah (Eusebius, Ecclesiastical History 3.5-8). "
                    "Whether or not one accepts that theological interpretation, Josephus's eyewitness "
                    "narrative makes the New Testament's eschatological discourse historically concrete."
        }
    ]
}
