"""
info.py — Text introduction for "The Bible You Read and the One They Wrote"

A thematic study examining the textual history behind our modern Bibles:
the Septuagint vs. the Masoretic Text, the Dead Sea Scrolls verdict on
ancient variants, how the canon was historically formed, the enduring
authority of 1 Enoch, and the other Second Temple texts that illuminate
the world of Scripture.
"""

TEXT_INFO = {
    "text_id": "canon_septuagint",
    "display_name": "The Bible You Read and the One They Wrote",
    "full_title": "The Bible You Read and the One They Wrote: LXX, MT, DSS, and the Texts Behind Scripture",

    "canonical_status": {
        "status": "thematic_study",
        "label": "Thematic Study (Multi-Source)",
        "detail": "This is not a single ancient text but a comprehensive thematic study "
                  "examining the textual traditions behind modern Bibles. It covers the "
                  "Septuagint (LXX) as the Bible of the apostles, the Masoretic Text (MT) "
                  "and its post-temple standardization, the Dead Sea Scrolls as independent "
                  "witnesses, the historical process of canon formation, the enduring "
                  "authority of 1 Enoch, and the illuminating value of Jubilees, the Book "
                  "of Giants, and 4 Ezra. Each claim is tagged with evidence classification: "
                  "A (direct Scripture), B (valid inference), C (ancient parallels)."
    },

    "authorship": {
        "traditional": "Modern thematic compilation by Seaver Hall (2025\u20132026)",
        "scholarly_debate": "N/A \u2014 this is a research compilation, not an ancient text.",
        "bottom_line": "A systematic study synthesizing textual criticism, canon history, "
                       "and Second Temple Jewish literature to help readers understand what "
                       "Bible they are actually reading \u2014 and what the original authors and "
                       "audiences had access to. Draws on the work of Emanuel Tov (Textual "
                       "Criticism of the Hebrew Bible), Karen Jobes & Mois\u00e9s Silva (Invitation "
                       "to the Septuagint), Michael S. Heiser (The Unseen Realm, Reversing "
                       "Hermon), and primary DSS scholarship."
    },

    "date": {
        "traditional": "2025\u20132026",
        "critical_range": "Research compiled November 2025 \u2013 March 2026",
        "evidence": "Built iteratively through textual analysis, manuscript comparison, "
                    "and scholarly cross-referencing of LXX, MT, and DSS traditions."
    },

    "audience": {
        "original": "Students of biblical theology who want to understand the textual "
                    "traditions behind their English Bibles \u2014 and why it matters for "
                    "theology, especially divine council passages.",
        "modern": "Anyone who has ever asked: 'Which Bible am I actually reading? How "
                  "close is it to the original? Why do some traditions include different "
                  "books?' This study answers those questions with evidence, not assumptions."
    },

    "language": {
        "original": "English with extensive Hebrew, Aramaic, Greek, and Ge\u2019ez "
                    "original-language analysis",
        "translations": "Scripture quotations primarily from ESV with original-language "
                        "comparisons across LXX, MT, and DSS traditions"
    },

    "scripture_alignment": {
        "relationship": "Examines how different textual traditions preserve \u2014 or alter \u2014 "
                        "the original text of Scripture, with special attention to divine "
                        "council passages where the MT and LXX/DSS diverge.",
        "key_tensions": "The Masoretic Text, while carefully preserved, contains post-temple "
                        "alterations in key passages (Deut 32:8, Deut 32:43, Gen 3:15 pronoun). "
                        "The Dead Sea Scrolls frequently confirm the LXX against the MT in "
                        "these passages. This study follows the oldest textual witnesses."
    },

    "manuscripts": {
        "key_witnesses": "Draws from the Septuagint (3rd\u20131st century BC), Masoretic Text "
                         "(7th\u201310th century AD standardization), Dead Sea Scrolls (3rd century "
                         "BC \u2013 1st century AD), Vulgate (382\u2013405 AD), Ge\u2019ez manuscripts of "
                         "1 Enoch, and Aramaic fragments from Qumran.",
        "textual_issues": "Key variants: Deuteronomy 32:8 (MT 'sons of Israel' vs. DSS/LXX "
                          "'sons of God'), Deuteronomy 32:43 (LXX contains line absent in MT "
                          "quoted in Hebrews 1:6), Genesis 3:15 pronoun (Hebrew hu\u2019 'he' vs. "
                          "Jerome's ipsa 'she'). This study consistently follows the oldest "
                          "available textual witnesses."
    },

    "historical_context": {
        "setting": "The textual history of the Bible spans from the earliest Hebrew "
                   "compositions through the Greek translation in Alexandria, the Qumran "
                   "community's library, Jerome's Vulgate, the medieval Masoretic "
                   "standardization, the Reformation canon debates, and the 1947 discovery "
                   "of the Dead Sea Scrolls that overturned centuries of assumptions.",
        "significance": "Understanding which text tradition your Bible comes from is not "
                        "an academic exercise \u2014 it directly affects how you read key "
                        "theological passages about the divine council, the Messiah, and "
                        "the cosmic war. The NT authors quoted the LXX approximately 80% "
                        "of the time, yet most Protestant Bibles translate from the MT."
    },

    "divine_council": {
        "relevance": "central",
        "key_passages": "Deuteronomy 32:8-9, Deuteronomy 32:43, Genesis 3:15, Psalm 82:1, "
                        "Hebrews 1:6, Jude 14-15, 2 Peter 2:4, 1 Enoch 1:9, 1 Enoch 15:8-10",
        "summary": "The divine council framework is precisely where the LXX/DSS and MT "
                   "diverge most significantly. The MT alteration of 'sons of God' to "
                   "'sons of Israel' in Deuteronomy 32:8 obscures the entire Deuteronomy 32 "
                   "worldview \u2014 that Yahweh divided the nations among divine beings and kept "
                   "Israel as His own portion. The Dead Sea Scrolls confirmed the LXX reading "
                   "as original, vindicating the divine council interpretation. Similarly, "
                   "1 Enoch's framework for understanding demons, the Watchers, and cosmic "
                   "warfare was the background the NT authors assumed their readers knew."
    },

    "reader_notes": [
        "Evidence tags throughout: [A] = direct Scripture, [B] = valid inference from "
        "Scripture, [C] = ancient parallels (non-canonical context).",
        "Non-canonical texts are always introduced with 'According to [source]...' \u2014 "
        "never 'the Bible says' for extra-biblical material.",
        "1 Enoch is treated as highly authoritative background material based on Jude 14-15, "
        "DSS confirmation, and Ethiopian Orthodox canonical tradition \u2014 but is never "
        "elevated above the 66-book canon.",
        "The three-tier framework: Tier 1 (canonical = authoritative), Tier 2 (DSS-confirmed "
        "and NT-quoted = highly valuable), Tier 3 (illuminating ancient context).",
        "10 chapters organized in 5 eras covering LXX/MT traditions, DSS confirmation, "
        "canon history, 1 Enoch, and other Second Temple texts."
    ]
}
