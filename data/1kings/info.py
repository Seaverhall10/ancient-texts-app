"""
info.py — 1 Kings (Melakhim Aleph): Scholarly Text Introduction

This file provides the "front page" for 1 Kings in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

1 Kings contains some of the most dramatic divine council encounters in
scripture: Solomon's Temple as the cosmic mountain where heaven meets earth,
Elijah's contest with the prophets of Baal on Mount Carmel — a direct
power encounter between YHWH and a rival elohim — and the extraordinary
divine council vision in 1 Kings 22, where the prophet Micaiah sees YHWH
enthroned among his heavenly host and a "lying spirit" volunteering for a
mission. This book moves from the glory of Solomon's kingdom to the division
and decline of Israel, tracing the consequences of serving the gods of the
nations.
"""

TEXT_INFO = {
    "text_id": "1kings",
    "display_name": "1 Kings (Melakhim Aleph)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Former Prophets",
        "detail": "1 Kings is the fifth book of the Former Prophets (Nevi'im Rishonim) in the Hebrew "
                  "Bible and the eleventh book of the Christian Old Testament. In the Hebrew Bible, "
                  "1 and 2 Kings were originally a single book called 'Kings' (Melakhim), divided by "
                  "the LXX translators (who titled them '3-4 Kingdoms,' continuing from '1-2 Kingdoms' "
                  "= 1-2 Samuel). The Talmud (Bava Batra 15a) attributes Kings to Jeremiah. 1 Kings "
                  "is extensively referenced in the New Testament: Jesus cites Solomon's glory "
                  "(Matt 6:29; Luke 12:27), the Queen of Sheba's visit (Matt 12:42; Luke 11:31), "
                  "the widow of Zarephath (Luke 4:25-26), and Elijah's ministry (Luke 4:25-26; "
                  "James 5:17-18). Elijah becomes the paradigmatic prophet, appearing at the "
                  "Transfiguration (Matt 17:3) and expected as the forerunner of the Messiah "
                  "(Mal 4:5-6; Matt 11:14; 17:10-13). No tradition has questioned the canonical "
                  "status of 1 Kings."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud (Bava Batra 15a) states: 'Jeremiah wrote the book that bears his "
                       "name, the Book of Kings, and Lamentations.' This attribution makes chronological "
                       "sense: Jeremiah lived through the final decades of Judah and the fall of Jerusalem "
                       "(~626-586 BC), and Kings concludes with events from this period. The book itself "
                       "cites its sources: 'the Book of the Acts of Solomon' (11:41), 'the Book of the "
                       "Chronicles of the Kings of Israel' (14:19, etc.), and 'the Book of the Chronicles "
                       "of the Kings of Judah' (14:29, etc.). These were royal annals — court records "
                       "that the author/editor compiled and interpreted theologically.",

        "scholarly_debate": "1 Kings is the centerpiece of the Deuteronomistic History. The theological "
                           "evaluation formula — each king is judged by whether 'he did what was right/evil "
                           "in the eyes of YHWH' and whether he removed or tolerated the high places — is "
                           "the hallmark of the Deuteronomistic editor. Cross's double-redaction theory "
                           "proposes a pre-exilic Dtr1 edition under Josiah (~620 BC) that climaxed with "
                           "Josiah's reform as the ideal Davidic king, and an exilic Dtr2 edition (~550 BC) "
                           "that extended the narrative through the fall of Jerusalem and added the themes "
                           "of irreversible judgment. The Elijah-Elisha narratives (1 Kings 17-2 Kings 13) "
                           "may derive from independent prophetic circles in the northern kingdom. The "
                           "Solomon traditions (1 Kings 1-11) draw on both court records and wisdom "
                           "traditions.",

        "bottom_line": "1 Kings was compiled from multiple authentic sources — royal annals, prophetic "
                       "narratives, and temple records — and shaped by Deuteronomistic editorial theology. "
                       "Whether Jeremiah or another exilic editor compiled the final form, the sources "
                       "are rooted in the historical periods they describe. The theological evaluation "
                       "of each king against the Deuteronomic standard of centralized worship and "
                       "covenant loyalty is the interpretive framework that gives the raw historical "
                       "data its meaning."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events span approximately 970-850 BC, from Solomon's accession to "
                       "Ahaziah's death. Jeremiah's compilation would date to ~586-560 BC.",
        "critical_range": "The events cover ~970-850 BC. The pre-exilic Dtr1 edition is dated to "
                         "~620 BC under Josiah. The exilic Dtr2 edition is dated to ~550 BC. The "
                         "sources (royal annals, prophetic narratives) date to the periods they "
                         "describe. The synchronistic chronology system (correlating the kings of "
                         "Israel and Judah) is an editorial achievement that has been largely "
                         "vindicated by external evidence.",
        "evidence": "Key evidence includes: (1) The Shishak/Shoshenq invasion (1 Kings 14:25-26) "
                    "is confirmed by Shoshenq I's campaign relief at Karnak temple (~925 BC), listing "
                    "conquered cities in Canaan. (2) The Mesha Stele (~840 BC) confirms Omri as king "
                    "of Israel and describes Moabite-Israelite relations consistent with 2 Kings 3. "
                    "(3) Assyrian inscriptions name several Israelite and Judahite kings mentioned in "
                    "Kings: Ahab (at the Battle of Qarqar, 853 BC), Jehu (Black Obelisk of "
                    "Shalmaneser III), Menahem, Hoshea, Hezekiah, and Manasseh. (4) The ivory "
                    "collections at Samaria match the description of Ahab's 'ivory house' (1 Kings "
                    "22:39). (5) Dead Sea Scrolls fragments of Kings (4QKgs, 5QKgs) generally align "
                    "with the MT, with minor variants."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Israel — specifically the exilic community that needed to understand "
                            "why they lost the land, the temple, and the monarchy. 1 Kings answers "
                            "this question systematically: the kingdom was divided because Solomon "
                            "served other gods (11:1-13); Israel fell because its kings perpetuated "
                            "Jeroboam's sin of unauthorized worship; Judah survived longer because of "
                            "the Davidic covenant and occasional righteous kings, but eventually fell "
                            "because the accumulated sin of Manasseh was irreversible (2 Kings 21:10-15; "
                            "23:26-27; 24:3-4).",

        "purpose": "1 Kings traces the arc from Solomon's glory to the kingdom's division and decline, "
                   "demonstrating the theological principle that covenant unfaithfulness leads to "
                   "national disaster. Solomon's reign begins with extraordinary promise — divine "
                   "wisdom, unprecedented wealth, and the construction of YHWH's Temple — but ends "
                   "with apostasy, as his foreign wives 'turned his heart after other gods' (11:4). "
                   "The division of the kingdom is YHWH's judgment: the northern tribes are torn away "
                   "because of Solomon's idolatry (11:11-13), but one tribe (Judah, with Benjamin) is "
                   "preserved 'for the sake of David my servant and for the sake of Jerusalem' (11:13) "
                   "— the Davidic covenant remains operative even under judgment.",

        "theological_intent": "The book presents YHWH as sovereign over history, working through and "
                             "despite human kings. The prophets (Ahijah, Elijah, Micaiah) are YHWH's "
                             "representatives who speak his word into the political realm, confronting "
                             "kings and overturning nations. The central theological question is: Who is "
                             "God — YHWH or Baal? Elijah's contest on Carmel (chapter 18) is the climactic "
                             "answer: YHWH is the true God; Baal is either powerless or nonexistent as a "
                             "deity capable of responding. The divine council vision in chapter 22 reveals "
                             "the mechanism behind prophetic speech: true prophets stand in YHWH's council "
                             "and relay its decisions; false prophets speak from their own imagination or "
                             "are deliberately deceived by spirits operating under YHWH's authority."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "1 Kings exhibits the characteristic Deuteronomistic prose style in its "
                           "framework passages: the regnal formulas, theological evaluations, and "
                           "prophetic speeches. The source material shows different linguistic registers: "
                           "the Solomon narratives use a combination of wisdom vocabulary and "
                           "administrative terminology; the Elijah narratives use vivid, dramatic prose "
                           "with terse, powerful dialogue; and the temple description (chapters 6-7) "
                           "employs technical architectural terminology that has been illuminated by "
                           "archaeological discoveries of Phoenician-style temples. The divine council "
                           "vision in 1 Kings 22:19-23 uses specific council terminology: 'YHWH sitting "
                           "on his throne, and all the host of heaven standing beside him on his right "
                           "hand and on his left' — the language of a royal court assembly, with the "
                           "heavenly beings deliberating and volunteering for missions.",
        "grammar_match": "The prose alternates between formulaic (the regnal frameworks) and narrative "
                        "(the stories of Solomon, Elijah, Ahab). The Elijah narratives are among the "
                        "most vivid and emotionally compelling prose in the Hebrew Bible, using short, "
                        "punchy sentences, dramatic irony, and powerful imagery. The temple description "
                        "uses a technical register unique in the Bible."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "1 Kings IS scripture — the prophetic history of Israel's monarchy, demonstrating "
                   "YHWH's sovereignty over kingdoms and the consequences of covenant unfaithfulness.",
        "nt_usage": "Jesus references 1 Kings repeatedly: Solomon's glory (Matt 6:29; Luke 12:27), "
                    "the Queen of the South visiting Solomon (Matt 12:42; Luke 11:31), and the widow "
                    "of Zarephath to whom Elijah was sent rather than Israelite widows (Luke 4:25-26, "
                    "a provocative statement about grace to Gentiles). Elijah becomes a foundational "
                    "New Testament figure: he appears with Moses at the Transfiguration (Matt 17:3; "
                    "Mark 9:4; Luke 9:30), is expected as the forerunner of the Messiah (Mal 4:5-6; "
                    "Matt 11:14; 17:10-13), and John the Baptist is identified as the Elijah figure "
                    "(Matt 11:14; Luke 1:17). James 5:17-18 cites Elijah's prayer as a model of "
                    "effective prayer. The divine council scene in 1 Kings 22 is a critical background "
                    "text for understanding the New Testament's teaching on spiritual warfare and "
                    "deceptive spirits (1 Tim 4:1; 1 John 4:1-6; 2 Thess 2:9-12).",
        "internal_consistency": "1 Kings continues the Davidic covenant trajectory from 2 Samuel 7. "
                               "Solomon's Temple fulfills David's desire to build a 'house for YHWH' "
                               "(2 Sam 7:2-13). The division of the kingdom fulfills Ahijah's prophecy "
                               "(1 Kings 11:29-39). The evaluation of kings against the Deuteronomic "
                               "standard connects to the covenant curses of Deuteronomy 28. Elijah's "
                               "experience at Horeb/Sinai (1 Kings 19) deliberately echoes Moses' Sinai "
                               "encounter (Exod 33-34)."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: 4QKgs (4Q54) and 5QKgs (5Q2) preserve small "
                    "portions of 1 Kings. The fragments generally align with the MT but are too "
                    "small for comprehensive textual analysis.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The MT of 1 Kings is generally well-preserved. The most significant textual "
                     "issue is the relationship between the MT and LXX arrangements of the Solomon "
                     "narratives, where the LXX sometimes has material in a different order."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The LXX of Kings (= 3-4 Kingdoms) shows significant differences from the MT "
                     "in the Solomon section. The LXX has additional material about Jeroboam's "
                     "rebellion and rearranges some of the Solomon narratives. The 'Lucianic' "
                     "recension preserves readings of particular textual value."},
            {"name": "Dead Sea Scrolls", "date": "~150-50 BC",
             "note": "Fragmentary. Insufficient for comprehensive text-critical analysis but "
                     "confirming the general stability of the Hebrew tradition."},
            {"name": "2 Chronicles parallel", "date": "Post-exilic, ~400 BC",
             "note": "2 Chronicles 1-9 parallels 1 Kings 1-11 (Solomon's reign) with significant "
                     "theological adjustments. Chronicles omits David's sin with Bathsheba, Solomon's "
                     "apostasy, and most negative material, presenting an idealized portrait."}
        ],
        "reliability": "The text of 1 Kings is well-preserved in the MT. The main textual issues "
                       "involve the LXX's different arrangement of the Solomon material and "
                       "occasional expansions in the Elijah narratives. The theological content — "
                       "the temple construction, the Carmel contest, the divine council vision — "
                       "is stable across all major witnesses."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "1 Kings covers the period from Solomon's accession (~970 BC) to the reign of "
                   "Ahaziah of Israel (~850 BC). This spans the united monarchy's golden age, the "
                   "traumatic division of the kingdom (~930 BC), and the early period of the divided "
                   "monarchy. Solomon's reign coincided with a power vacuum in the ancient Near East "
                   "that allowed Israel to prosper. The kingdom's division was precipitated by heavy "
                   "taxation and forced labor under Solomon (12:4) and was formalized under Rehoboam "
                   "and Jeroboam. The Omride dynasty of the northern kingdom (Omri, Ahab, etc.) was "
                   "one of the most powerful Israelite regimes, though it receives negative theological "
                   "evaluation in Kings because of its promotion of Baal worship.",

        "geography": "Key locations include: Jerusalem and the Temple Mount (the cosmic center of "
                     "Israelite worship), Shechem and Penuel (Jeroboam's initial northern capitals), "
                     "Dan and Bethel (the sites of Jeroboam's golden calves), Samaria (the Omride "
                     "capital, built by Omri ~880 BC), Mount Carmel (the site of Elijah's contest with "
                     "Baal's prophets), the Kerith Ravine and Zarephath (Elijah's hiding places), and "
                     "Horeb/Sinai (Elijah's divine encounter). Ramoth-Gilead (the site of Ahab's death) "
                     "was a contested frontier town on the Aramean border.",

        "historical_connections": "Multiple external sources confirm 1 Kings' historical framework: "
                                 "the Shoshenq I relief at Karnak (~925 BC) confirms the invasion of "
                                 "1 Kings 14:25-26; Assyrian records mention Ahab's 2,000 chariots and "
                                 "10,000 soldiers at the Battle of Qarqar (853 BC, not mentioned in Kings "
                                 "but consistent with Ahab's military power); the Mesha Stele confirms "
                                 "Omri's domination of Moab; ivory collections at Samaria match 1 Kings "
                                 "22:39. The Phoenician temple architecture described in 1 Kings 6-7 is "
                                 "paralleled by archaeological finds at Ain Dara (Syria) and other sites."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "major",
        "summary": "1 Kings contains three of the most important divine council passages in the "
                   "entire Bible: Solomon's Temple as the cosmic mountain, Elijah's contest with "
                   "Baal at Carmel, and Micaiah's divine council vision in chapter 22."
                   "\n\n"
                   "SOLOMON'S TEMPLE — THE COSMIC MOUNTAIN (1 Kings 6-8): The Temple is not merely "
                   "a building — it is the architectural representation of the cosmic mountain where "
                   "YHWH's heavenly throne room intersects with earth. The temple design reflects "
                   "the three-tiered cosmos: the porch (ulam) represents the visible world; the "
                   "Holy Place (hekal) represents the heavens; and the Holy of Holies (devir, the "
                   "inner sanctuary) represents YHWH's throne room in the highest heaven. The "
                   "cherubim in the Holy of Holies (6:23-28) — two enormous olive-wood figures "
                   "fifteen feet tall whose wings span the entire room — are the divine council's "
                   "throne-guardians, the same beings who guard Eden (Gen 3:24) and carry YHWH's "
                   "throne in Ezekiel's vision (Ezek 1, 10). The Temple's floral and garden imagery "
                   "(carved palm trees, open flowers, cherubim, 6:29-35) recreates the Garden of "
                   "Eden — the original meeting place of heaven and earth that was lost at the Fall "
                   "and is now symbolically restored. When YHWH's kavod (glory/presence) fills the "
                   "Temple (8:10-11), heaven and earth overlap — the cosmic mountain is active."
                   "\n\n"
                   "ELIJAH VS. BAAL AT CARMEL (1 Kings 18): The Carmel contest is the ultimate "
                   "divine council power encounter in the Old Testament. Elijah challenges the "
                   "450 prophets of Baal and 400 prophets of Asherah to a simple test: 'The god "
                   "who answers by fire, he is God' (18:24). Baal was the Canaanite storm god — "
                   "if any deity could send fire from heaven, it would be Baal. His prophets dance, "
                   "shout, and cut themselves from morning to evening. Elijah mocks them: 'Perhaps "
                   "he is meditating, or relieving himself, or on a journey, or sleeping and must "
                   "be awakened' (18:27). In the Deuteronomy 32 framework, Baal is a real spiritual "
                   "entity — one of the gods allotted to the nations who has claimed authority over "
                   "Canaan's weather and fertility. The contest is a direct challenge to his claimed "
                   "jurisdiction. YHWH's fire falls not just on the sacrifice but 'consumed the "
                   "burnt offering and the wood and the stones and the dust, and licked up the "
                   "water that was in the trench' (18:38) — a total demonstration of power that "
                   "leaves no room for ambiguity. The people's response — 'YHWH, he is God! YHWH, "
                   "he is God!' (18:39) — is the divine council verdict pronounced by Israel."
                   "\n\n"
                   "THE DIVINE COUNCIL SCENE (1 Kings 22:19-23): Micaiah's vision is the most "
                   "explicit divine council scene in the Old Testament. He sees 'YHWH sitting on "
                   "his throne, and all the host of heaven standing beside him on his right hand "
                   "and on his left' (22:19). YHWH asks the council: 'Who will entice Ahab to go "
                   "up and fall at Ramoth-Gilead?' (22:20). Various spirits propose plans. Then 'a "
                   "spirit' (ruakh) comes forward and volunteers: 'I will go out and be a lying "
                   "spirit in the mouth of all his prophets' (22:22). YHWH approves the plan: 'You "
                   "are to entice him, and you shall succeed. Go out and do so' (22:22). This "
                   "passage is extraordinary for several reasons: (1) It portrays the divine council "
                   "as a deliberative body where YHWH consults with spiritual beings. (2) The "
                   "spirits have agency — they propose, and YHWH authorizes. (3) YHWH uses a lying "
                   "spirit as an instrument of judgment against Ahab. (4) The prophet gains his "
                   "message by 'standing in the council' (cf. Jer 23:18, 22). This is the biblical "
                   "basis for understanding how false prophecy can be part of YHWH's sovereign plan — "
                   "and it has direct New Testament parallels in 2 Thessalonians 2:11 ('God sends "
                   "them a strong delusion') and 1 Timothy 4:1 ('deceitful spirits').",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 2-3 (the divine council — 1 Kings 22 as the key passage)",
            "The Unseen Realm, chapter 14-16 (the Carmel contest and the gods of the nations)",
            "The Unseen Realm, chapter 20-21 (the Temple as cosmic mountain)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 4-5 (the heavenly court scene)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 6-7 (the lying spirit and deception)",
            "Supernatural, chapter 16 (Elijah, Baal, and the divine warrior)",
            "The Naked Bible Podcast, episode 15 (1 Kings 22 — the divine council in session)",
            "The Naked Bible Podcast, episodes 119-125 (1 Kings and the divine council)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Temple as Cosmic Mountain and Eden Restored",
            "body": "Solomon's Temple was not merely a house of worship — it was the architectural "
                    "embodiment of the cosmic mountain, the place where heaven and earth overlap. "
                    "In the ancient Near Eastern worldview, the cosmic mountain was where the chief "
                    "god dwelt and from which he ruled. For Israel, this mountain was Zion/Moriah. "
                    "The Temple's design recapitulated the cosmos: the sea of cast metal (7:23-26) "
                    "represented the cosmic waters; the twelve oxen supporting it represented the "
                    "twelve tribes or the ordered world; the garden imagery (palm trees, flowers, "
                    "cherubim) recreated Eden; and the Holy of Holies, where YHWH's presence dwelt "
                    "between the cherubim, was the throne room of the divine council. When the glory "
                    "cloud filled the Temple (8:10-11), the priests could not stand to minister — "
                    "the raw presence of YHWH had entered his earthly dwelling. Solomon's dedication "
                    "prayer (8:22-53) acknowledges that 'heaven and the highest heaven cannot contain "
                    "you; how much less this house that I have built!' (8:27) — the Temple is a "
                    "concession to human limitation, a point of access to the divine presence that "
                    "transcends all physical space."
        },
        {
            "type": "interpretation",
            "title": "The Lying Spirit — YHWH's Use of Deception in Judgment",
            "body": "The divine council scene in 1 Kings 22:19-23 raises one of the most profound "
                    "theological questions in scripture: Does YHWH use deception? The text is explicit: "
                    "YHWH authorizes a spirit to be a 'lying spirit in the mouth of all [Ahab's] "
                    "prophets.' Three key principles govern interpretation: (1) The deception is "
                    "judicial — Ahab has repeatedly rejected YHWH's truth, and the lying spirit is "
                    "an instrument of judgment on one who has already chosen falsehood. (2) The "
                    "deception operates within the divine council's authority — the spirit volunteers "
                    "and is authorized, not forced. (3) YHWH reveals the deception through his true "
                    "prophet Micaiah — Ahab has access to the truth but chooses to reject it. This "
                    "pattern recurs in 2 Thessalonians 2:9-12: God sends a 'strong delusion' to "
                    "those who 'refused to love the truth,' and they believe the lie because they "
                    "'had pleasure in unrighteousness.' The divine council's use of deception is "
                    "always judicial, never arbitrary."
        },
        {
            "type": "context",
            "title": "Elijah and Baal — The Contest of the Gods",
            "body": "Elijah's contest at Carmel must be understood in the Deuteronomy 32 framework. "
                    "Baal was not an imaginary deity in the biblical worldview — he was one of the "
                    "gods allotted to the nations, a spiritual entity who had usurped authority in "
                    "YHWH's own territory through Jezebel's Phoenician Baal cult. The specific test — "
                    "sending fire from heaven — targeted Baal's core claim: as the storm god, he "
                    "controlled lightning and fire. His failure to respond demonstrated not merely "
                    "that idols are powerless (the standard prophetic critique, cf. Isa 44:9-20) but "
                    "that YHWH has absolute authority over the domain Baal claimed. The immediate "
                    "aftermath — rain returning after three years of drought (18:41-46) — further "
                    "demonstrated YHWH's control over weather, another of Baal's claimed jurisdictions. "
                    "Elijah's subsequent experience at Horeb (chapter 19), where YHWH speaks not in "
                    "wind, earthquake, or fire but in a 'still small voice' (or 'sound of thin "
                    "silence'), provides a counterpoint: YHWH's power is not limited to dramatic "
                    "displays but operates in ways that transcend the storm-god paradigm entirely."
        },
        {
            "type": "scholarship",
            "title": "Solomon and Demons in Later Jewish Tradition",
            "body": "While 1 Kings describes Solomon's extraordinary wisdom (3:12; 4:29-34) and "
                    "his eventual apostasy through worship of foreign gods (11:1-8), later Jewish "
                    "tradition dramatically expanded the supernatural dimensions of his story. The "
                    "Testament of Solomon (1st-3rd century AD pseudepigraphon) portrays Solomon "
                    "commanding demons by the authority of a ring given him by the archangel Michael, "
                    "forcing them to build the Temple. Josephus (Antiquities 8.45-49) describes "
                    "Solomon composing incantations for healing and exorcism. Rabbinic tradition "
                    "(Gittin 68a-b) tells of Solomon enslaving the demon Asmodeus. While these are "
                    "later legends, they reflect an ancient conviction that Solomon's wisdom extended "
                    "into the spiritual realm and that the Temple's construction involved mastery over "
                    "supernatural forces. This tradition influenced New Testament references to "
                    "exorcism 'in the name of Solomon' and may be behind Jesus' comparison of himself "
                    "to Solomon: 'something greater than Solomon is here' (Matt 12:42)."
        }
    ]
}
