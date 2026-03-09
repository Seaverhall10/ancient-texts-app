"""
info.py — Book of Jasher (Sefer haYashar): Scholarly Text Introduction

CRITICAL PROVENANCE WARNING: The "Book of Jasher" available today is the
Sefer haYashar published in 1625 (Venice/Naples). Most scholars consider it
a MEDIEVAL composition (11th-12th century), NOT the ancient book referenced
in Joshua 10:13 and 2 Samuel 1:18. The original Book of Jashar is LOST.

This file provides the "front page" for the Book of Jasher in the Ancient
Texts Library. It answers: Who wrote it? When? For whom? In what language?
Does it align with other scripture? What's the manuscript tradition? Where
does it fit in history and geography?
"""

TEXT_INFO = {
    "text_id": "jasher",
    "display_name": "Book of Jasher (Sefer haYashar)",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "non-canonical",
        "label": "Non-Canonical — Disputed Provenance",
        "detail": "The Book of Jasher is NOT canonical in any Jewish, Catholic, Orthodox, or "
                  "Protestant tradition. Its status is further complicated by a provenance "
                  "problem: the Bible references a 'Book of Jashar' (sefer hayashar) in two "
                  "places — Joshua 10:13 ('Is this not written in the Book of Jashar?') and "
                  "2 Samuel 1:18 ('it is written in the Book of Jashar'). These references "
                  "point to a genuinely ancient Israelite text, likely a collection of heroic "
                  "poetry that predates the monarchy. However, the book available to us today "
                  "under the title 'Book of Jasher' (Sefer haYashar) was first published in "
                  "Venice/Naples in 1625 and is considered by most scholars to be a MEDIEVAL "
                  "composition from the 11th-12th century AD. It is NOT the same text the "
                  "Bible references. The original Book of Jashar is lost. Readers must "
                  "understand this distinction clearly: the biblical citation lends authority "
                  "to a text we do not have, not to the medieval text we do have."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "The text presents itself as an ancient chronicle spanning from creation "
                       "to the period of the Judges, implicitly claiming to be the book referenced "
                       "in Joshua and 2 Samuel. Some readers have taken this at face value, "
                       "treating it as the genuine ancient Book of Jashar recovered and preserved "
                       "through Jewish tradition. This claim is not supported by scholarly evidence.",

        "scholarly_debate": "The overwhelming consensus of scholarship (Zunz, Goldschmidt, "
                           "Dan, Yasif) is that Sefer haYashar is a medieval Jewish composition, "
                           "written in the 11th or 12th century AD, likely in Spain or southern Italy. "
                           "The evidence for medieval composition is substantial:\n\n"
                           "- The Hebrew style is medieval, not biblical or Second Temple period\n"
                           "- It draws on midrashic traditions found in works like Pirke de-Rabbi "
                           "Eliezer (8th-9th century), Sefer haZikhronot, and the Talmud\n"
                           "- It contains expansions and legends that match medieval midrashic "
                           "compilations, not ancient sources\n"
                           "- No manuscript predates the medieval period\n"
                           "- The first printed edition appeared in Venice/Naples in 1625\n"
                           "- Its literary structure follows the pattern of medieval 'rewritten Bible' "
                           "works, not ancient Israelite poetic collections\n\n"
                           "The original Book of Jashar referenced in the Bible was likely a "
                           "collection of ancient Israelite victory songs and heroic poetry — the "
                           "passage in Joshua quotes a poem about the sun standing still, and the "
                           "passage in 2 Samuel references David's lament for Saul and Jonathan. "
                           "This type of text (a national poetic anthology) is well-attested in "
                           "ancient Near Eastern cultures but has not survived.",

        "bottom_line": "The Book of Jasher we possess is a medieval Jewish literary work — a "
                       "'rewritten Bible' that retells Genesis through Joshua with midrashic "
                       "expansions. It was NOT written by any biblical figure, and it is NOT "
                       "the ancient Book of Jashar that Joshua and Samuel reference. That text "
                       "is lost. The medieval Sefer haYashar may preserve some genuinely ancient "
                       "Jewish traditions (transmitted orally or through earlier midrashic works), "
                       "but the compilation itself is from the 11th-12th century AD. Treating it "
                       "as an ancient text on par with the Dead Sea Scrolls or Second Temple "
                       "literature is a historical error."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "The text implicitly claims to cover the period from creation to the "
                       "conquest of Canaan (pre-12th century BC). Some popular writers date it "
                       "to the patriarchal or Mosaic period based on the biblical references in "
                       "Joshua 10:13 and 2 Samuel 1:18.",
        "critical_range": "COMPOSITION: 11th-12th century AD (medieval period). The earliest "
                         "known manuscript evidence comes from the medieval period. The first "
                         "printed edition was published in Venice or Naples in 1625. Internal "
                         "evidence (literary style, midrashic parallels, Hebrew vocabulary) "
                         "consistently points to medieval composition.\n\n"
                         "THE LOST ORIGINAL: The actual Book of Jashar referenced in the Bible "
                         "would date to the period of the early monarchy or earlier (pre-10th "
                         "century BC), as 2 Samuel 1:18 already cites it in the context of "
                         "David's reign. It may have been compiled as early as the period of "
                         "the Judges. This text no longer exists.",
        "evidence": "There is no manuscript evidence placing the extant Sefer haYashar earlier "
                    "than the medieval period. The midrashic traditions it incorporates can be "
                    "traced to works no earlier than the Talmudic and Geonic periods (5th-10th "
                    "century AD). The Hebrew is stylistically medieval. The argument that this is "
                    "the actual biblical Book of Jashar relies entirely on the title claim, not "
                    "on any textual, linguistic, or manuscript evidence. Multiple other medieval "
                    "works also claimed the title 'Sefer haYashar' — there is a separate ethical "
                    "treatise by Rabbenu Tam (12th century) with the same name."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Medieval Jewish readers. The text functions as a popular retelling "
                            "of biblical history enriched with midrashic expansions — legends, "
                            "dialogues, and narrative details not found in the biblical text. This "
                            "is a genre of Jewish literature known as 'rewritten Bible' (also seen "
                            "in Jubilees, the Genesis Apocryphon, Pseudo-Philo, and Josephus's "
                            "Antiquities), in which the biblical narrative is retold with expansions "
                            "that fill gaps, resolve apparent contradictions, and edify the reader.",

        "purpose": "Sefer haYashar serves as an entertaining and edifying retelling of biblical "
                   "history from creation through the conquest. It fills narrative gaps that "
                   "readers naturally wonder about: What was Abraham's childhood like? How did "
                   "he come to reject idolatry? What happened to the generation between Joseph "
                   "and Moses? The expansions are drawn from centuries of Jewish interpretive "
                   "tradition (midrash), compiled into a continuous narrative that reads like "
                   "an adventure chronicle. It is more accessible than the Talmud's scattered "
                   "midrashic comments because it arranges everything in chronological story form.",

        "theological_intent": "The theological intent is broadly consistent with rabbinic Judaism: "
                             "exalting the patriarchs as men of extraordinary faith and courage, "
                             "emphasizing God's providential control of history, and demonstrating "
                             "that Israel's covenant relationship with God has deep roots. The "
                             "expansions tend to magnify the heroism of biblical figures (Abraham "
                             "surviving Nimrod's furnace, Jacob as a warrior, Moses as a king in "
                             "Ethiopia) in ways that go well beyond the biblical text. This is "
                             "hagiographic storytelling, not critical history."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Medieval Hebrew. The text was composed in Hebrew, but it is the literary "
                    "Hebrew of the medieval period, not the Biblical Hebrew of the Old Testament "
                    "or the Aramaic of the Second Temple period.",
        "script": "Hebrew square script (standard medieval Jewish manuscript tradition).",
        "linguistic_notes": "The Hebrew of Sefer haYashar is recognizably medieval in its "
                           "vocabulary, syntax, and style. It imitates biblical Hebrew in places "
                           "(as medieval Jewish authors commonly did) but contains constructions "
                           "and word usages that do not appear before the medieval period. This is "
                           "one of the strongest arguments against an ancient date — a text genuinely "
                           "composed in the biblical period would exhibit the linguistic features of "
                           "that period (as the Dead Sea Scrolls, for example, demonstrably do). The "
                           "English translation most commonly encountered is the 1840 translation by "
                           "Moses Samuel, which gives the text a King James Bible flavor that makes "
                           "it feel more ancient than the Hebrew original actually is.",
        "grammar_match": "The grammar does NOT match biblical-period Hebrew. It matches the "
                        "literary Hebrew conventions of medieval Jewish writing in the Islamic "
                        "world and southern Europe. Scholars who have analyzed the language "
                        "(Zunz, Dan, Yasif) consistently conclude it is medieval composition."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "Mixed — the core narrative closely follows the biblical text (Genesis through "
                   "Joshua), but the expansions range from plausible gap-filling to clearly "
                   "legendary material. Read with discernment and awareness that this is medieval "
                   "midrash, not ancient history.",

        "where_it_aligns": [
            "The basic narrative framework faithfully follows Genesis through Joshua — creation, "
            "the patriarchs, the bondage in Egypt, the exodus, the wilderness, the conquest",
            "Many of its expansions reflect traditions also found in the Talmud, Targumim, and "
            "earlier midrashic collections, suggesting they draw on genuine streams of Jewish "
            "interpretive tradition even if the compilation is medieval",
            "Some chronological and genealogical details fill gaps in the biblical narrative in "
            "ways that are internally consistent with the biblical text",
            "The basic theology — monotheism, covenant faithfulness, divine judgment on idolatry — "
            "is consistent with the canonical scriptures"
        ],

        "where_it_diverges": [
            "Abraham being thrown into Nimrod's furnace and miraculously surviving (Jasher 12) — "
            "this is a well-known midrashic legend with no biblical basis",
            "Nimrod possessing the 'garments of Adam' that gave him power over animals (Jasher 7) — "
            "this is legendary material not found in any ancient source",
            "Extensive warrior narratives for Jacob and his sons that portray them as military "
            "conquerors in ways the Bible does not support",
            "Moses serving as king of Ethiopia for 40 years (Jasher 72-76) — an elaborate "
            "expansion of the brief Numbers 12:1 reference to Moses' Cushite wife",
            "Detailed dialogue and scenes that are clearly literary invention, filling narrative "
            "gaps with content that cannot be historically verified",
            "Chronological calculations that sometimes conflict with the biblical timeline"
        ],

        "reader_guidance": "The safest approach: Read Sefer haYashar as medieval Jewish storytelling "
                          "that retells the biblical narrative with legendary expansions. Where it "
                          "simply follows the Bible, it adds nothing the Bible doesn't already say. "
                          "Where it expands, ask: Is this expansion attested in earlier sources? Does "
                          "it contradict the biblical text? Or is it plausible gap-filling? Some "
                          "traditions it preserves may genuinely be ancient (transmitted through oral "
                          "tradition and earlier midrashic works). But many of its most dramatic "
                          "stories — Abraham in the furnace, Nimrod's garments, Moses in Ethiopia — "
                          "are legendary material that should not be treated as historical fact."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "No manuscript of Sefer haYashar predates the medieval period. The first "
                    "printed edition was published in Venice (or Naples) in 1625. Manuscript "
                    "copies circulated in the medieval Jewish communities of Spain and Italy, "
                    "but none have been dated earlier than the 12th-13th century AD.",
        "major_witnesses": [
            {"name": "1625 Venice/Naples printed edition", "date": "1625 AD",
             "note": "The first printed edition and the basis for all subsequent editions and "
                     "translations. Published from a manuscript whose provenance is unclear."},
            {"name": "Medieval Hebrew manuscripts", "date": "12th-15th century AD (approximate)",
             "note": "Several manuscript copies exist in European libraries, but none predate the "
                     "medieval period. No Dead Sea Scroll fragments, no ancient Greek or Aramaic "
                     "versions, no papyrus witnesses — the manuscript tradition begins and ends "
                     "in the medieval period."},
            {"name": "Moses Samuel English translation", "date": "1840 AD",
             "note": "The most widely circulated English translation, published in London. This "
                     "is the version most English readers encounter. Its archaic King James-style "
                     "language gives a false impression of antiquity."},
            {"name": "J.H. Parry & Company edition", "date": "1887 AD",
             "note": "A widely reprinted English edition based on Samuel's translation, commonly "
                     "available in print and online. This is the edition most popular in Christian "
                     "circles today."}
        ],
        "reliability": "The manuscript tradition is thin and entirely medieval. There are no ancient "
                       "witnesses whatsoever — no Dead Sea Scroll fragments, no Greek or Latin "
                       "translations from antiquity, no patristic quotations, no reference in any "
                       "ancient Jewish or Christian source to this specific text. This stands in "
                       "stark contrast to genuinely ancient non-canonical texts like 1 Enoch "
                       "(Qumran fragments from the 2nd century BC), Jubilees (Qumran fragments), "
                       "or the Genesis Apocryphon (Qumran). The complete absence of ancient "
                       "manuscript evidence is the single strongest argument that this is not the "
                       "biblical Book of Jashar."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "The narrative covers creation through the conquest of Canaan — the same span "
                   "as Genesis through Joshua. However, the text was composed in the context of "
                   "medieval Jewish communities in Spain or Italy during the 11th-12th century AD, "
                   "a period of vigorous Jewish literary production that also produced works like "
                   "Yosippon (a medieval Jewish rewriting of Josephus), various midrashic "
                   "compilations, and the ethical Sefer haYashar of Rabbenu Tam.",

        "geography": "The narrative geography follows the Bible: Mesopotamia (creation, Babel, "
                     "Abraham's origins), Canaan (patriarchal narratives), Egypt (bondage and "
                     "exodus), Sinai (wilderness), and Canaan again (conquest). Some expansions "
                     "add additional geography: Ethiopia/Cush (where Moses allegedly reigned as "
                     "king), and various battle locations for Jacob's sons. The actual composition "
                     "geography is medieval Spain or Italy.",

        "historical_connections": "The text must be understood within the medieval 'rewritten Bible' "
                                 "tradition. Jewish communities throughout the medieval period produced "
                                 "expanded retellings of biblical history that incorporated midrashic "
                                 "traditions, filled narrative gaps, and made the biblical story more "
                                 "vivid and accessible. Sefer haYashar is one of the most successful "
                                 "examples of this genre — so successful that many readers have mistaken "
                                 "it for the genuine ancient text referenced in the Bible. Other notable "
                                 "examples of the same genre (from different periods) include Jubilees "
                                 "(2nd century BC — genuinely ancient), Pseudo-Philo's Biblical "
                                 "Antiquities (1st century AD — genuinely ancient), and Yosippon (10th "
                                 "century AD — medieval, like Sefer haYashar)."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "low",
        "summary": "Michael Heiser rarely if ever cites the Book of Jasher in his published work, "
                   "and for good reason — as a medieval composition, it does not provide independent "
                   "evidence for ancient Israelite beliefs about the divine council. When Heiser "
                   "builds his case for the divine council worldview, he relies on the Hebrew Bible "
                   "itself, the Dead Sea Scrolls, Second Temple literature with verified ancient "
                   "provenance (1 Enoch, Jubilees), and ancient Near Eastern comparative texts "
                   "(Ugaritic literature, Mesopotamian texts). Sefer haYashar does not belong in "
                   "that evidentiary category.\n\n"
                   "That said, some of the traditions in Sefer haYashar touch on themes relevant "
                   "to the divine council framework:\n\n"
                   "- The Nimrod traditions (Nimrod as a mighty hunter before/against YHWH, his "
                   "garments of power, his tower-building) parallel the Genesis 10-11 rebellion "
                   "narrative that Heiser connects to Deuteronomy 32:8-9\n"
                   "- Angel interactions with the patriarchs are expanded in ways that overlap "
                   "with the Watchers tradition\n"
                   "- The wars of the sons of Jacob include encounters with supernatural elements\n\n"
                   "However, none of these traditions in Sefer haYashar add anything that cannot "
                   "be found in earlier, better-attested sources (Genesis itself, 1 Enoch, Jubilees, "
                   "the Targumim). For the divine council framework, Sefer haYashar is redundant "
                   "at best.",

        "key_heiser_refs": [
            "Heiser does not cite Sefer haYashar in The Unseen Realm, Supernatural, or Reversing Hermon",
            "For the Nimrod/Babel traditions, Heiser relies on Genesis 10-11 and Deuteronomy 32:8-9 directly",
            "For angelology and Watchers, Heiser relies on 1 Enoch, Jubilees, and the Dead Sea Scrolls",
            "The divine council framework is built on ancient sources with verified provenance, "
            "not medieval retellings"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "warning",
            "title": "THIS IS NOT THE BIBLICAL BOOK OF JASHAR",
            "body": "This is the single most important thing to understand about this text. The "
                    "Bible references a 'Book of Jashar' in Joshua 10:13 and 2 Samuel 1:18. That "
                    "was a genuinely ancient Israelite text — likely a collection of heroic poetry — "
                    "that predated the monarchy. It is LOST. The text we have, published in 1625, "
                    "is a medieval Jewish composition from the 11th-12th century AD that borrowed "
                    "the prestigious title. Treating the medieval Sefer haYashar as though it were "
                    "the ancient Book of Jashar is a category error that undermines credibility. "
                    "Many popular Christian and Messianic teachers present this text as the genuine "
                    "ancient book without disclosing its actual provenance. Be aware of this."
        },
        {
            "type": "context",
            "title": "Publication History and Popular Reception",
            "body": "Sefer haYashar was first published in Venice (or Naples) in 1625. It was "
                    "translated into English by Moses Samuel in 1840 and has been widely reprinted "
                    "since, especially by the J.H. Parry & Company edition (1887). In the 20th "
                    "and 21st centuries, it gained enormous popularity in Christian, Messianic, and "
                    "Hebrew Roots circles, often presented alongside 1 Enoch and Jubilees as a "
                    "'lost book of the Bible.' This is misleading. Unlike 1 Enoch and Jubilees, "
                    "which have verified ancient manuscript traditions (Dead Sea Scrolls), the Book "
                    "of Jasher has NO ancient manuscript evidence whatsoever. It belongs to a "
                    "different evidentiary category entirely."
        },
        {
            "type": "interpretation",
            "title": "Ancient Traditions in a Medieval Package",
            "body": "While the compilation is medieval, some traditions preserved in Sefer haYashar "
                    "may genuinely be ancient. The Abraham-in-the-furnace tradition appears in "
                    "earlier Jewish sources (Genesis Rabbah, Pesikta Rabbati). The Nimrod legends "
                    "have parallels in Josephus and the Talmud. The Moses-in-Ethiopia tradition "
                    "echoes material in Artapanus (2nd century BC). This does not make the Book of "
                    "Jasher an ancient text — it makes it a medieval compilation that draws on "
                    "earlier sources, some of which may preserve genuinely old traditions. The "
                    "proper approach is to trace individual traditions back to their earliest "
                    "attestation rather than treating the entire compilation as ancient."
        },
        {
            "type": "warning",
            "title": "Legendary Expansions Are Not History",
            "body": "Some of the most popular stories from the Book of Jasher — Nimrod possessing "
                    "the garments of Adam and Eve that gave him dominion over animals, Abraham "
                    "being cast into a fiery furnace by Nimrod and miraculously surviving, the "
                    "detailed wars of Jacob's sons against Canaanite city-states, Moses reigning "
                    "as king of Ethiopia for 40 years — are legendary expansions with no biblical "
                    "basis and no ancient attestation beyond midrashic tradition. They are "
                    "entertaining and sometimes theologically interesting, but they should not be "
                    "cited as historical evidence or used to build theological arguments. The line "
                    "between 'the Bible says' and 'the Book of Jasher says' must be maintained."
        }
    ]
}
