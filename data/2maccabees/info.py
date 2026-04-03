"""
info.py — 2 Maccabees: Scholarly Text Introduction

Theological history of the Maccabean revolt, an epitome of Jason of Cyrene's
larger work, with major contributions to resurrection theology and martyrdom.
"""

TEXT_INFO = {
    "text_id": "2maccabees",
    "display_name": "2 Maccabees",
    "full_title": "The Second Book of the Maccabees",

    "canonical_status": {
        "status": "deuterocanonical",
        "label": "Deuterocanonical (Catholic & Orthodox canon; not in Protestant canon)",
        "detail": "2 Maccabees is included in the Catholic and Eastern Orthodox Old Testament "
                  "canons but excluded from the Protestant canon. Unlike 1 Maccabees, it is "
                  "not a straightforward historical chronicle but a theological interpretation "
                  "of the Maccabean revolt. It is an abridgment (epitome) of a five-volume "
                  "history by Jason of Cyrene (2:23). The book has had outsized theological "
                  "influence: its martyrdom accounts shaped early Christian martyrology, and "
                  "its statements on resurrection and prayers for the dead became foundational "
                  "for Catholic doctrine."
    },

    "authorship": {
        "traditional": "The text identifies itself as an abridgment of a five-volume work by "
                       "Jason of Cyrene (2:23). The epitomist (abridger) is anonymous.",
        "scholarly_debate": "Jason of Cyrene was a Hellenistic Jewish historian from Cyrene in "
                           "North Africa. His original five-volume work is entirely lost; we "
                           "know it only through this abridgment. The epitomist was a competent "
                           "Greek stylist who added a rhetorical preface (2:19-32), the prefixed "
                           "letters (1:1-2:18), and possibly the theological commentary woven "
                           "throughout. The epitomist's theological interests — Temple, martyrdom, "
                           "resurrection, divine retribution — shape the entire narrative.",
        "bottom_line": "An anonymous Hellenistic Jewish epitomist condensing Jason of Cyrene's "
                       "lost five-volume history into a single theological narrative focused on "
                       "God's defense of the Temple and vindication of the faithful."
    },

    "date": {
        "traditional": "The prefixed letters are dated to 124 BC (1:9), providing a terminus "
                       "ante quem for the epitome.",
        "critical_range": "Jason's original work: c. 160-150 BC (written shortly after the events). "
                         "The epitome: c. 124 BC or shortly after, based on the date in the "
                         "prefixed letter (1:9). The letters themselves may have been added when "
                         "the epitome was prepared for circulation.",
        "evidence": "The letter dated to 124 BC (1:9) is the strongest anchor. Jason must have "
                    "written before the epitomist, probably within a generation of the events "
                    "(ending ~161 BC with Nicanor's defeat). The sophisticated Greek style and "
                    "Hellenistic historiographical conventions point to a Diaspora milieu."
    },

    "audience": {
        "original_audience": "Diaspora Jews, particularly in Egypt. The prefixed letters urge "
                            "Egyptian Jews to observe the festival of the Temple rededication.",
        "purpose": "To promote the Jerusalem Temple and its festivals among Diaspora Jews, "
                   "and to demonstrate that God actively defends the Temple against desecration. "
                   "The elaborate martyrdom accounts (ch. 6-7) serve as models of faithfulness "
                   "under persecution, with explicit theology of resurrection as divine reward.",
        "theological_intent": "God is the active protagonist — sending angelic warriors, striking "
                             "down blasphemers, and vindicating martyrs through bodily resurrection. "
                             "The Temple is the cosmic center that God will always defend."
    },

    "language": {
        "original": "Greek. Unlike 1 Maccabees, 2 Maccabees was composed in Greek and is not "
                    "a translation from a Semitic original.",
        "script": "Greek, written in a sophisticated Hellenistic historiographical style with "
                  "rhetorical flourishes, dramatic speeches, and pathetic (emotional) narration.",
        "linguistic_notes": "The Greek is polished and literary, employing rhetorical techniques "
                           "common in Hellenistic historiography: dramatic irony, divine epiphanies, "
                           "elaborate death scenes, and authorial commentary. The vocabulary is "
                           "rich and the syntax complex — a marked contrast to the translation "
                           "Greek of 1 Maccabees."
    },

    "manuscripts": {
        "earliest": "Greek Septuagint manuscripts from the 4th-5th century AD.",
        "major_witnesses": [
            {"name": "Codex Sinaiticus", "date": "4th century AD",
             "note": "Does not contain 2 Maccabees (it has 1 and 4 Maccabees)."},
            {"name": "Codex Alexandrinus", "date": "5th century AD",
             "note": "Contains 1-4 Maccabees. Primary witness for 2 Maccabees."},
            {"name": "Codex Venetus", "date": "8th century AD",
             "note": "Important witness for the Maccabean books."},
            {"name": "Latin Vulgate", "date": "4th century AD (translation)",
             "note": "Jerome translated from the Greek, noting its non-Hebrew origin."}
        ],
        "reliability": "The Greek text is well preserved. Since it was composed in Greek (not "
                       "translated), there are no retroversion questions. The main textual issue "
                       "is the relationship of the prefixed letters to the body of the epitome."
    },

    "historical_context": {
        "setting": "The narrative covers approximately 180-161 BC, overlapping with but not "
                   "duplicating 1 Maccabees. It begins with the high priest Onias III and the "
                   "Heliodorus affair and ends with Judas Maccabeus' victory over Nicanor. "
                   "The focus is narrower than 1 Maccabees — centered on Jerusalem and the Temple "
                   "rather than the wider Hasmonean political story.",
        "geography": "Centered almost entirely on Jerusalem and the Temple. Events in Antioch "
                     "and other Seleucid centers are reported only as they affect the Temple.",
        "historical_connections": "2 Maccabees provides crucial evidence for Second Temple theology: "
                                 "explicit bodily resurrection (ch. 7), creation from nothing (7:28), "
                                 "intercessory prayer for the dead (12:43-45), angelic intervention "
                                 "in battle (3:24-26, 10:29-30, 11:8), and the theology of martyrdom "
                                 "as atoning sacrifice (7:37-38). These ideas profoundly influenced "
                                 "early Christianity, Rabbinic Judaism, and Catholic doctrine."
    },

    "reader_notes": [
        {
            "type": "authority",
            "title": "Resurrection Theology",
            "body": "2 Maccabees 7 contains the clearest pre-Christian statement of bodily "
                    "resurrection in Jewish literature. The mother and her seven sons face "
                    "torture and death, each affirming that God will raise them bodily. This "
                    "is not 'spiritual survival' but physical resurrection — the God who made "
                    "the body will restore it. Note: when Jesus confronted the Sadducees on "
                    "resurrection (Mark 12:18-27), he grounded the doctrine in Torah — Exodus "
                    "3:6, 'I am the God of Abraham, Isaac, and Jacob... He is not God of the "
                    "dead but of the living.' The canonical foundation for resurrection is Torah "
                    "itself. 2 Maccabees 7 shows how that Torah-rooted hope had developed into "
                    "explicit bodily resurrection theology by the Maccabean period, which Paul "
                    "later proclaimed fully in 1 Corinthians 15."
        },
        {
            "type": "context",
            "title": "Creation Ex Nihilo",
            "body": "2 Maccabees 7:28 contains the earliest Jewish articulation of creation from "
                    "nothing (ex nihilo): the mother tells her youngest son that God made everything "
                    "'out of things that did not exist.' This theological development goes beyond "
                    "Genesis 1 (which does not explicitly address pre-existing matter). The concept "
                    "is later affirmed canonically in Romans 4:17 (God 'calls into existence the "
                    "things that do not exist'), Hebrews 11:3, and John 1:3. Those canonical texts "
                    "are the doctrinal foundation; 2 Maccabees is the important historical precedent "
                    "showing this idea was already active in Second Temple Judaism."
        },
        {
            "type": "deeper_reading",
            "title": "Prayers for the Dead",
            "body": "2 Maccabees 12:43-45 describes Judas Maccabeus collecting money for a sin "
                    "offering on behalf of fallen soldiers found wearing pagan amulets. The text "
                    "explicitly connects this to belief in resurrection — it would be pointless "
                    "to pray for the dead if there were no resurrection. This passage became the "
                    "primary scriptural source cited by Catholic tradition for the doctrine of purgatory and prayers "
                    "for the dead, and was a key point of contention during the Reformation."
        }
    ]
}
