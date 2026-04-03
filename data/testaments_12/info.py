"""
info.py — Testaments of the Twelve Patriarchs: Scholarly Text Introduction

Composite Jewish-Christian work preserving the deathbed speeches of Jacob's
twelve sons — a unique window into pre-Christian Jewish ethics, messianic
expectation, and the Watcher tradition's development.
"""

TEXT_INFO = {
    "text_id": "testaments_12",
    "display_name": "Testaments of the Twelve Patriarchs",
    "full_title": "The Testaments of the Twelve Patriarchs",

    "canonical_status": {
        "status": "pseudepigrapha",
        "label": "Pseudepigrapha (not in any major canon; extremely influential on early Christianity)",
        "detail": "The Testaments of the Twelve Patriarchs are not canonical in any major "
                  "Christian or Jewish tradition, but their influence on early Christian ethics "
                  "and eschatology was enormous. The 'Two Ways' doctrine (spirit of truth vs. "
                  "spirit of error) appears in the Didache, the Epistle of Barnabas, and the "
                  "Qumran Community Rule (1QS 3:13-4:26). The two-messiah expectation (priestly "
                  "from Levi, royal from Judah) illuminates the Dead Sea Scrolls' messianic "
                  "theology. Aramaic fragments of the Testament of Levi (4Q213-214) and the "
                  "Testament of Naphtali (4Q215) were found at Qumran, confirming a pre-Christian "
                  "Jewish core beneath the Christian editorial layer."
    },

    "authorship": {
        "traditional": "The text presents itself as the final words of each of Jacob's twelve sons, "
                       "delivered on their deathbeds to their descendants — a literary form modeled "
                       "on Jacob's own blessing in Genesis 49.",
        "scholarly_debate": "The Testaments are a composite work with a complex literary history. "
                           "A Jewish core dating to the 2nd century BC is widely accepted, confirmed "
                           "by the Qumran Aramaic fragments of the Testament of Levi (4Q213-214) and "
                           "Testament of Naphtali (4Q215). However, the surviving Greek text contains "
                           "significant Christian interpolations — references to Christ, the crucifixion, "
                           "and the resurrection that are clearly secondary additions. The central "
                           "scholarly debate concerns the extent of Christian editing: some passages "
                           "may be lightly retouched, while others (especially in Testament of Benjamin "
                           "and Testament of Levi) appear to be substantial Christian compositions "
                           "inserted into the Jewish framework.",
        "bottom_line": "A Jewish work from the 2nd century BC, significantly edited by Christian "
                       "scribes in the 2nd century AD. The Qumran fragments prove the Jewish core "
                       "is pre-Christian. Separating original Jewish material from Christian additions "
                       "remains one of the great puzzles of pseudepigrapha scholarship."
    },

    "date": {
        "traditional": "Set in the patriarchal period, at the deaths of Jacob's twelve sons "
                       "in Egypt and Canaan.",
        "critical_range": "Jewish core: 2nd century BC, roughly contemporary with the Book of "
                         "Jubilees and early Enochic literature. The Qumran Aramaic Levi fragments "
                         "may preserve material from the 3rd century BC or earlier. Final Greek form "
                         "with Christian additions: 2nd century AD.",
        "evidence": "The Aramaic Testament of Levi fragments from Qumran (4Q213-214) and the "
                    "Cairo Genizah establish that a Jewish Testament of Levi existed independently "
                    "before being incorporated into the Twelve. The ethical vocabulary and "
                    "theological concerns overlap extensively with Jubilees, the Enochic corpus, "
                    "and the Qumran sectarian texts, confirming the 2nd century BC dating for "
                    "the Jewish core. Christian interpolations reflect 2nd century AD Christology."
    },

    "audience": {
        "original_audience": "The Jewish core addressed a Jewish community interested in ethical "
                            "instruction grounded in patriarchal authority. The testament genre — "
                            "a dying father's wisdom to his sons — carried immense weight in a "
                            "culture that venerated ancestral teaching.",
        "purpose": "Each testament follows a three-part pattern: (1) autobiographical narrative "
                   "in which the patriarch confesses his sins and virtues, (2) ethical exhortation "
                   "based on the patriarch's experience, and (3) prophecy about the future of "
                   "the tribe and Israel. The overall purpose is moral instruction through the "
                   "authority of the patriarchs themselves.",
        "theological_intent": "The Jewish core teaches that virtue and vice are cosmic forces — "
                             "the 'spirit of truth' and 'spirit of error' (Beliar) compete for "
                             "human allegiance. Salvation comes through the priestly messiah from "
                             "Levi and the royal messiah from Judah. The Christian editors redirected "
                             "this dual messianism toward Christ, who fulfills both priestly and "
                             "royal roles."
    },

    "language": {
        "original": "The surviving text is in Greek. However, the Qumran fragments prove that at "
                    "least the Testament of Levi and Testament of Naphtali existed in Aramaic and "
                    "Hebrew, respectively. The Jewish core was likely composed in Hebrew or Aramaic "
                    "and translated into Greek, at which point Christian editors made their additions.",
        "script": "Greek manuscripts from the medieval period provide the main text. The Armenian "
                  "version is an important independent witness, sometimes preserving readings "
                  "closer to the Jewish original than the Greek. Aramaic Levi fragments from "
                  "Qumran (4Q213-214) and the Cairo Genizah provide direct access to pre-Christian "
                  "material.",
        "linguistic_notes": "The Greek text shows signs of translation from a Semitic original — "
                           "Hebraisms in syntax and vocabulary are evident throughout. The Christian "
                           "interpolations tend to be smoother Greek, providing one criterion for "
                           "distinguishing layers. Comparison of the Greek Testament of Levi with "
                           "the Aramaic Qumran fragments reveals both fidelity to the original and "
                           "significant expansion by later editors."
    },

    "manuscripts": {
        "earliest": "Aramaic fragments from Qumran (4Q213-214, 4Q215), 2nd-1st century BC. "
                    "Greek manuscripts from the medieval period. Armenian version.",
        "major_witnesses": [
            {"name": "4Q213-214 (Aramaic Levi)", "date": "2nd-1st century BC",
             "note": "Qumran fragments of the Testament of Levi in Aramaic, proving the "
                     "pre-Christian Jewish origin of the work."},
            {"name": "4Q215 (Testament of Naphtali)", "date": "2nd-1st century BC",
             "note": "Qumran Hebrew fragment of the Testament of Naphtali."},
            {"name": "Cairo Genizah Aramaic Levi", "date": "medieval copy of ancient text",
             "note": "Aramaic Levi document from the Cairo Genizah, overlapping with but "
                     "distinct from the Qumran fragments."},
            {"name": "Greek manuscript tradition", "date": "10th-13th century AD",
             "note": "Multiple Greek manuscripts preserving the full twelve testaments "
                     "with Christian interpolations."},
            {"name": "Armenian version", "date": "medieval",
             "note": "Important independent witness, sometimes preserving readings closer "
                     "to the Jewish original than the Greek manuscripts."}
        ],
        "reliability": "The textual situation is complex. The Qumran fragments confirm a "
                       "pre-Christian Jewish original but cover only portions of two testaments. "
                       "The full Greek text contains undeniable Christian additions, and scholars "
                       "debate the extent of editing in nearly every passage. The Armenian version "
                       "provides a valuable check on the Greek but is itself a translation. Despite "
                       "these challenges, the broad outlines of the Jewish core — the ethical "
                       "framework, the Levi-Judah messianism, the Watcher tradition — are secure."
    },

    "historical_context": {
        "setting": "Each testament is set at the deathbed of one of Jacob's twelve sons, following "
                   "the model of Jacob's own final blessings in Genesis 49. The patriarchs confess "
                   "their sins (Reuben's defilement of Bilhah, Simeon's jealousy of Joseph, Judah's "
                   "affair with Tamar), draw moral lessons, and prophesy about the future.",
        "geography": "The settings reflect the patriarchal narratives — Egypt, Canaan, Hebron. The "
                     "Testament of Levi includes a heavenly ascent through multiple heavens, "
                     "connecting to the broader Second Temple tradition of heavenly journeys "
                     "(1 Enoch, 2 Enoch, Ascension of Isaiah).",
        "historical_connections": "The Testaments stand at the intersection of several major streams "
                                 "of Second Temple thought. The Two Ways doctrine (spirit of truth vs. "
                                 "spirit of error) appears in the Qumran Community Rule (1QS 3:13-4:26), "
                                 "the Didache, and 1 John 4:6. The dual Levi-Judah messianism illuminates "
                                 "the Dead Sea Scrolls' expectation of two messiahs — a priestly Messiah "
                                 "of Aaron and a royal Messiah of Israel. The Watcher tradition in "
                                 "Testament of Reuben 5:6-7 describes the Watchers changing their form "
                                 "to appear as human men to seduce women, expanding the Genesis 6:1-4 "
                                 "and 1 Enoch tradition with specific details about angelic shape-shifting."
    },

    "reader_notes": [
        {
            "type": "deeper_reading",
            "title": "Two Ways Doctrine",
            "body": "The virtue/vice framework in the Testaments — the spirit of truth versus the "
                    "spirit of error (Beliar) — is one of the most influential ethical schemas in "
                    "Second Temple Judaism. Each human faces a cosmic choice between two competing "
                    "spiritual forces. This exact framework appears in the Qumran Community Rule "
                    "(1QS 3:13-4:26), which describes the Angel of Light and the Angel of Darkness "
                    "ruling over the 'two spirits' in humanity. It continues into early Christianity "
                    "through the Didache's 'Two Ways' teaching and echoes in 1 John 4:6's 'spirit "
                    "of truth and spirit of error.' The Testaments may represent an early, widely "
                    "circulated form of this doctrine that influenced both Qumran and Christianity."
        },
        {
            "type": "context",
            "title": "Levi-Judah Messianism",
            "body": "The Testaments consistently elevate Levi (priestly) and Judah (royal) above the "
                    "other tribes, expecting salvation to come from both lineages. This dual messianism "
                    "is crucial for understanding the Dead Sea Scrolls' expectation of two messiahs — "
                    "a priestly Messiah of Aaron and a royal Messiah of Israel (1QS 9:11, CD 12:23). "
                    "The New Testament authors present Jesus as fulfilling both roles: royal son of "
                    "David through Judah, and eternal priest through the order of Melchizedek "
                    "(Hebrews 7), transcending the Levi-Judah division entirely."
        },
        {
            "type": "context",
            "title": "Watcher Tradition",
            "body": "Testament of Reuben 5:6-7 contains a striking expansion of the Watcher "
                    "tradition from Genesis 6:1-4 and 1 Enoch. It describes the Watchers as "
                    "transforming themselves into human appearance to approach mortal women — an "
                    "explicit claim of angelic shape-shifting not found in the Genesis text itself. "
                    "This detail develops the tradition beyond 1 Enoch's account and demonstrates "
                    "that the Watcher interpretation of Genesis 6 was widespread in Second Temple "
                    "Judaism, not a marginal reading. The Sethite reinterpretation (which claims "
                    "'sons of God' means the line of Seth) did not appear until the 3rd century AD "
                    "and has no grounding in these earlier Jewish sources."
        }
    ]
}
