"""
info.py — 2 Kings (Melakhim Bet): Scholarly Text Introduction

This file provides the "front page" for 2 Kings in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

2 Kings narrates the final centuries of the divided monarchy — from Elisha's
succession to the destruction of Samaria (722 BC) and Jerusalem (586 BC).
It contains extraordinary divine council encounters: Elisha's servant seeing
the angelic army surrounding the city of Dothan, the angel of YHWH slaying
185,000 Assyrians in a single night, and the ultimate covenant judgment —
the exile. The book is a sustained demonstration that YHWH governs the rise
and fall of kingdoms through the unseen realm, and that the gods of the
nations, despite their territorial claims, cannot protect their peoples
against YHWH's sovereign judgment.
"""

TEXT_INFO = {
    "text_id": "2kings",
    "display_name": "2 Kings (Melakhim Bet)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Former Prophets",
        "detail": "2 Kings is the sixth and final book of the Former Prophets (Nevi'im Rishonim) "
                  "in the Hebrew Bible and the twelfth book of the Christian Old Testament. Originally "
                  "part of a single 'Kings' scroll with 1 Kings, it was divided by the LXX translators. "
                  "The Talmud (Bava Batra 15a) attributes Kings to Jeremiah. 2 Kings is referenced in "
                  "the New Testament: Jesus cites the healing of Naaman the Syrian (Luke 4:27) as "
                  "evidence that God's grace extends beyond Israel. Elisha's miracles — particularly "
                  "the multiplication of bread (4:42-44) and the raising of the dead (4:32-37) — are "
                  "typological forerunners of Jesus' ministry. The fall of Jerusalem and the exile are "
                  "the assumed historical background for much of the prophetic literature and the "
                  "theological context of the New Testament's message of restoration. No tradition has "
                  "questioned the canonical status of 2 Kings."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "The Talmud (Bava Batra 15a) attributes Kings to Jeremiah, who lived through the "
                       "fall of Jerusalem in 586 BC. The final chapter of 2 Kings (25:27-30), which "
                       "records the release of Jehoiachin from Babylonian prison in ~561 BC, may postdate "
                       "Jeremiah's lifetime and could be a later addendum. Jeremiah would have had access "
                       "to the royal archives of Judah (the 'Book of the Chronicles of the Kings of "
                       "Judah' cited throughout Kings) and would have written with the theological "
                       "perspective of one who had warned of Jerusalem's destruction and witnessed its "
                       "fulfillment.",

        "scholarly_debate": "2 Kings is the conclusion of the Deuteronomistic History. The exilic editor "
                           "(Dtr2 in Cross's model) shaped the narrative to explain the catastrophe of "
                           "586 BC: the exile was not YHWH's failure but his judgment on centuries of "
                           "covenant violation. The evaluation of each king follows the Deuteronomistic "
                           "formula, and the theological explanation for the fall of Samaria (2 Kings "
                           "17:7-23) is the most extensive Deuteronomistic theological reflection in the "
                           "entire DtrH. The Elisha narratives (chapters 2-13) are generally regarded as "
                           "derived from prophetic circles in the northern kingdom — they have a different "
                           "style and character from the regnal framework. The Hezekiah narratives "
                           "(chapters 18-20) parallel Isaiah 36-39 almost verbatim, raising questions "
                           "about the direction of literary dependence.",

        "bottom_line": "2 Kings draws on authentic historical sources — royal annals, prophetic "
                       "traditions, and temple records — compiled and interpreted within the "
                       "Deuteronomistic framework. The book's theological interpretation of history is "
                       "not imposed on the events but emerges from the prophetic worldview: the same "
                       "prophets who warned of judgment (Isaiah, Jeremiah, the unnamed prophets cited "
                       "in the text) provided the theological categories by which the catastrophe was "
                       "understood. The exile was not random political misfortune but YHWH's covenant "
                       "judgment, foreseen and explained by his prophetic representatives."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "The events span approximately 850-560 BC, from Elisha's ministry to "
                       "Jehoiachin's release. Compilation by Jeremiah would date to ~586-560 BC.",
        "critical_range": "The events cover ~850-560 BC. The final form dates to the exilic period "
                         "(~560-540 BC, after Jehoiachin's release in 25:27-30). The Dtr1 edition is "
                         "dated to ~620 BC under Josiah. The sources (annals, prophetic narratives) "
                         "date to the periods they describe. The Hezekiah narratives share material "
                         "with Isaiah 36-39.",
        "evidence": "2 Kings has more extra-biblical corroboration than any other biblical book: "
                    "(1) Assyrian inscriptions confirm Sennacherib's campaign against Hezekiah "
                    "(the Taylor Prism/Sennacherib's Prism, ~701 BC, which describes besieging "
                    "Jerusalem though it does not mention the angelic destruction). (2) The Siloam "
                    "Tunnel inscription (~701 BC) confirms Hezekiah's water tunnel (2 Kings 20:20). "
                    "(3) The LMLK seal impressions ('belonging to the king') on storage jars match "
                    "Hezekiah's administrative preparations. (4) The Babylonian Chronicles record "
                    "the fall of Nineveh (612 BC), the Battle of Carchemish (605 BC), and "
                    "Nebuchadnezzar's capture of Jerusalem (597 BC). (5) The Lachish Letters (~588 BC) "
                    "are military correspondence from the final Babylonian siege, mentioning prophetic "
                    "activity and conditions matching 2 Kings 25 and Jeremiah. (6) Babylonian ration "
                    "tablets from Nebuchadnezzar's palace list rations for 'Yaukin, king of the land "
                    "of Yahud' — Jehoiachin king of Judah — confirming his imprisonment and "
                    "provisioning in Babylon (cf. 2 Kings 25:27-30)."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The exilic community — the Judahites deported to Babylon in 597 and "
                            "586 BC who needed to understand why YHWH allowed the destruction of his "
                            "Temple, his city, and his people's land. 2 Kings answers this question "
                            "with devastating clarity: the exile is YHWH's covenant judgment, "
                            "foreseen, warned about, and executed according to the terms of Deuteronomy "
                            "28-30. The book ends with a glimmer of hope — Jehoiachin's release "
                            "(25:27-30) — suggesting that the Davidic line survives and the covenant "
                            "promise endures even through exile.",

        "purpose": "2 Kings completes the Deuteronomistic History's argument: possession of the land "
                   "was conditional on covenant faithfulness, Israel and Judah systematically violated "
                   "the covenant by serving other gods, and the exile was the inevitable result. The "
                   "theological explanation for Samaria's fall (17:7-23) serves as the interpretive "
                   "key for the entire DtrH: 'They went after false idols and became false... they "
                   "followed the nations that were around them... they forsook all the commandments "
                   "of YHWH their God' (17:15-16). Judah survived longer because of the Davidic "
                   "covenant and occasional reforming kings (Hezekiah, Josiah), but Manasseh's "
                   "accumulated evil 'filled Jerusalem with innocent blood' (24:4), making judgment "
                   "irreversible.",

        "theological_intent": "The deepest theological claim of 2 Kings is that YHWH is sovereign "
                             "over all nations — not just Israel. Assyria and Babylon are his instruments "
                             "of judgment ('the rod of my anger,' Isa 10:5). Their gods cannot protect "
                             "their worshipers against YHWH's decree. The Rabshakeh's blasphemous speech "
                             "(18:28-35) — 'Where are the gods of Hamath and Arpad? Where are the gods "
                             "of Sepharvaim? Have they delivered Samaria out of my hand?' — is answered "
                             "by the angel's destruction of 185,000 Assyrians. YHWH is not one territorial "
                             "god among many; he is the God who governs all territories and uses all "
                             "nations for his purposes."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "2 Kings shows the same linguistic diversity as 1 Kings: Deuteronomistic "
                           "framework passages (regnal formulas, theological evaluations), vivid prophetic "
                           "narratives (the Elisha stories), diplomatic speeches (the Rabshakeh's address "
                           "in 18:19-37, which includes the detail that it was spoken in Aramaic and "
                           "Hebrew — 18:26), and historical summaries. The theological reflection in "
                           "17:7-23 is the longest sustained Deuteronomistic prose in the entire DtrH. "
                           "The Elisha narratives use a distinctive folklorist style — miracle stories "
                           "told with economy and wonder. The Hezekiah-Isaiah narratives (chapters 18-20) "
                           "share their text with Isaiah 36-39 almost verbatim, one of the most "
                           "significant internal parallels in the Hebrew Bible.",
        "grammar_match": "The prose registers include the formulaic (regnal evaluations), the narrative "
                        "(Elisha stories, military campaigns), the diplomatic (Rabshakeh's speeches), "
                        "and the theological (the 17:7-23 reflection). The Elisha miracle stories use "
                        "simple, declarative prose that creates a sense of wonder through understatement."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "2 Kings IS scripture — the prophetic conclusion of the Deuteronomistic History, "
                   "explaining the exile as YHWH's sovereign judgment while preserving hope in the "
                   "Davidic covenant.",
        "nt_usage": "Jesus references Naaman's healing (Luke 4:27) to demonstrate that God's grace "
                    "extended to Gentiles even under the old covenant — a provocative claim that nearly "
                    "gets him killed (Luke 4:28-30). Elisha's multiplication of bread for 100 people "
                    "(4:42-44) prefigures Jesus' feeding of 5,000 (Matt 14:13-21). Elisha's raising of "
                    "the Shunammite's son (4:32-37) anticipates Jesus' resurrections (Mark 5:35-43; "
                    "Luke 7:11-17; John 11:38-44). The Elijah-Elisha succession (2 Kings 2) — with its "
                    "double portion of the Spirit — provides the pattern for understanding the Spirit's "
                    "outpouring at Pentecost (Acts 2). The exile is the assumed historical background "
                    "for the prophetic promises of restoration that the New Testament claims Jesus "
                    "fulfills (Jer 31:31-34; Ezek 37; Isa 40-66).",
        "internal_consistency": "2 Kings completes the trajectory established in Deuteronomy through "
                               "Joshua, Judges, and Samuel. The covenant curses of Deuteronomy 28:36, "
                               "49-68 (siege, exile, scattering) are fulfilled in 2 Kings 25. The "
                               "promise that Josiah would reform worship (1 Kings 13:2, the prophecy "
                               "against Jeroboam's altar 'by name' — 'Josiah') is fulfilled in 2 Kings "
                               "23:15-20. The Davidic covenant's conditional discipline (2 Sam 7:14) is "
                               "realized in the exile, while its unconditional survival is hinted at in "
                               "Jehoiachin's release."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls fragments: 4QKgs (4Q54), 5QKgs (5Q2), and pap6QKgs (6Q4) "
                    "preserve small portions of 2 Kings, generally aligning with the MT.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The MT of 2 Kings is generally well-preserved. The parallel in Isaiah 36-39 "
                     "provides an internal textual check for chapters 18-20."},
            {"name": "Septuagint (LXX)", "date": "3rd-2nd century BC translation",
             "note": "The LXX of 2 Kings (= 4 Kingdoms) is generally close to the MT, with "
                     "occasional expansions and clarifications. The Lucianic recension provides "
                     "important variant readings."},
            {"name": "Dead Sea Scrolls", "date": "~150-50 BC",
             "note": "Fragmentary coverage. The preserved portions confirm the general stability "
                     "of the Hebrew text tradition."},
            {"name": "2 Chronicles parallel", "date": "Post-exilic, ~400 BC",
             "note": "2 Chronicles 10-36 parallels 2 Kings with significant theological adjustments, "
                     "emphasizing the cult, the Levites, and retributive theology."}
        ],
        "reliability": "The text of 2 Kings is well-preserved across the major witnesses. The "
                       "Isaiah 36-39 parallel provides a unique control text for chapters 18-20. "
                       "The extensive extra-biblical corroboration (Assyrian and Babylonian records) "
                       "confirms the historical framework's reliability."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "2 Kings covers the period from ~850 to ~560 BC — one of the best-documented "
                   "periods of ancient Near Eastern history. The Assyrian Empire rose to dominate "
                   "the region in the 8th century BC, destroying the northern kingdom of Israel in "
                   "722 BC. Babylonia succeeded Assyria in the late 7th century, and Nebuchadnezzar "
                   "destroyed Jerusalem in 586 BC. These events are abundantly documented in "
                   "Assyrian and Babylonian records, providing unparalleled external corroboration "
                   "for the biblical narrative.",

        "geography": "Key locations include: Samaria (the northern capital, destroyed 722 BC), "
                     "Jerusalem (besieged by Sennacherib ~701 BC, destroyed by Nebuchadnezzar 586 BC), "
                     "Dothan (where Elisha saw the angelic army), Nineveh (the Assyrian capital, "
                     "destroyed 612 BC), Babylon (the exile destination), Lachish (besieged by "
                     "Sennacherib, graphically depicted on his palace reliefs now in the British "
                     "Museum), and the Siloam Tunnel in Jerusalem (Hezekiah's water engineering).",

        "historical_connections": "More extra-biblical evidence exists for 2 Kings than any other "
                                 "biblical book. Sennacherib's Prism describes his siege of Jerusalem "
                                 "and Hezekiah 'shut up like a caged bird' — but notably does NOT claim "
                                 "to have captured Jerusalem, consistent with 2 Kings 19:35-36. The "
                                 "Babylonian Chronicles document the fall of Nineveh and Nebuchadnezzar's "
                                 "campaigns. The Lachish Reliefs in the British Museum provide a visual "
                                 "record of Sennacherib's siege tactics. The discovery of the Siloam "
                                 "Inscription in 1880 confirmed Hezekiah's tunnel (2 Kings 20:20). The "
                                 "Babylonian ration tablets confirm Jehoiachin's imprisonment. The "
                                 "destruction layers at Lachish, Jerusalem, and other Judahite sites "
                                 "provide dramatic archaeological evidence of the Babylonian conquest."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "major",
        "summary": "2 Kings contains two of the most vivid angelic encounters in the Old Testament "
                   "and culminates in the divine judgment that the entire Deuteronomistic History has "
                   "been building toward."
                   "\n\n"
                   "ELISHA'S ANGELIC ARMY (2 Kings 6:15-17): When the king of Aram sends an army "
                   "to capture Elisha at Dothan, Elisha's servant is terrified. Elisha responds: "
                   "'Do not be afraid, for those who are with us are more than those who are with "
                   "them' (6:16). Then Elisha prays: 'O YHWH, please open his eyes that he may see.' "
                   "YHWH opens the servant's eyes, and 'behold, the mountain was full of horses and "
                   "chariots of fire all around Elisha' (6:17). This is one of the most explicit "
                   "revelations of the heavenly host in scripture — the invisible army of YHWH, the "
                   "divine council's military forces, present but normally unseen. The 'chariots of "
                   "fire' echo the chariot that took Elijah to heaven (2:11) and connect to the "
                   "throne-chariot of Ezekiel 1. The theological point is foundational: the spiritual "
                   "realm is more real and more powerful than the visible world. YHWH's heavenly army "
                   "surrounds and protects his servants, even when the earthly situation appears "
                   "hopeless. This principle underlies Paul's confidence in Romans 8:31 ('If God is "
                   "for us, who can be against us?') and Hebrews 1:14 (angels as 'ministering spirits "
                   "sent out to serve for the sake of those who are to inherit salvation')."
                   "\n\n"
                   "SENNACHERIB'S 185,000 (2 Kings 19:35): 'And that night the angel of YHWH went "
                   "out and struck down 185,000 in the camp of the Assyrians. And when people arose "
                   "early in the morning, behold, these were all dead bodies.' This is the most "
                   "dramatic single act of angelic warfare in the Old Testament. The destroying angel "
                   "(mal'akh) executes YHWH's judgment on the most powerful military force in the "
                   "world — the Assyrian army that had conquered every nation it faced. Sennacherib's "
                   "own Prism inscription confirms he besieged Jerusalem but never claims to have "
                   "captured it — a remarkable silence for Assyrian propaganda, which normally "
                   "exaggerated victories. The divine council context is explicit: Hezekiah prays to "
                   "'YHWH of hosts (tseva'ot), God of Israel, enthroned above the cherubim' (19:15) "
                   "— invoking the divine council throne — and Isaiah delivers YHWH's response: 'I "
                   "will defend this city to save it, for my own sake and for the sake of my servant "
                   "David' (19:34). The Davidic covenant is the reason Jerusalem survives when Samaria "
                   "did not."
                   "\n\n"
                   "THE FALL OF SAMARIA AND JUDAH — DIVINE JUDGMENT: The theological summary of "
                   "Samaria's fall (17:7-23) is the clearest statement of the Deuteronomy 32 worldview "
                   "in the narrative books. Israel 'feared other gods and walked in the customs of "
                   "the nations' (17:8), 'set up for themselves pillars and Asherim on every high hill' "
                   "(17:10), 'served idols' (17:12), and 'went after false idols and became false' "
                   "(17:15). The result: 'YHWH was very angry with Israel and removed them out of his "
                   "sight' (17:18). The territorial logic is explicit: the gods Israel served could not "
                   "protect them, and YHWH, whom they had abandoned, withdrew his protection. The "
                   "Assyrian resettlement of foreigners in Samaria (17:24-41) — who bring their own "
                   "gods but also learn to 'fear YHWH' — creates the syncretistic religion that will "
                   "define Samaria for centuries (cf. the Samaritan tensions in the New Testament).",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 16-17 (territorial judgment and the exile)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 8-10 (angelic armies, the destroying angel)",
            "Supernatural, chapter 16-17 (the fall of Israel as divine council judgment)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 7 (the gods of the nations and divine judgment)",
            "The Naked Bible Podcast, episodes 126-135 (2 Kings and the divine council)",
            "The Naked Bible Podcast, episode 62 (Elisha's invisible army and the heavenly host)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "'Those Who Are with Us' — The Invisible Army",
            "body": "Elisha's declaration at Dothan (6:16) — 'those who are with us are more than "
                    "those who are with them' — is one of the most important theological statements "
                    "in the Old Testament. It reveals the foundational principle of the divine council "
                    "worldview: the visible world is not the whole reality. Behind and around every "
                    "earthly situation stands the invisible realm — YHWH's heavenly host, deployed for "
                    "his purposes. The servant's 'opened eyes' do not see a new reality; they see the "
                    "reality that was always there. This principle reframes all of biblical history: "
                    "every battle in Joshua, every deliverance in Judges, every protection of David "
                    "from Saul — the heavenly host was always present. The New Testament extends this "
                    "truth: angels ministered to Jesus in the wilderness (Matt 4:11) and in Gethsemane "
                    "(Luke 22:43), and Jesus stated he could summon 'more than twelve legions of angels' "
                    "(Matt 26:53). Hebrews 12:22 declares that believers have 'come to Mount Zion... "
                    "and to innumerable angels in festal gathering.' The invisible army is real."
        },
        {
            "type": "interpretation",
            "title": "The Destroying Angel and Sennacherib's Army",
            "body": "The destruction of 185,000 Assyrian soldiers in a single night (19:35) is the "
                    "most devastating act of angelic warfare in scripture. The 'angel of YHWH' "
                    "(mal'akh YHWH) who executes this judgment is the same figure who brings the plague "
                    "after David's census (2 Sam 24:15-17), slays the firstborn of Egypt (Exod 12:23, "
                    "cf. 'the destroyer'), and will ultimately execute eschatological judgment "
                    "(Rev 14:17-20). Ancient Near Eastern sources provide partial corroboration: "
                    "Herodotus (Histories 2.141) records a tradition that Sennacherib's army was "
                    "defeated when field mice ate through their bowstrings and quivers — a rationalized "
                    "memory of a sudden disaster (possibly plague, which mice symbolized in the ancient "
                    "world). Josephus (Antiquities 10.21) identifies the cause as a 'pestilential "
                    "distemper.' Whether the mechanism was supernatural plague or direct angelic "
                    "violence, the theological point is clear: YHWH alone defends Jerusalem, and his "
                    "instrument is the heavenly host."
        },
        {
            "type": "context",
            "title": "Josiah's Reform — Too Little, Too Late",
            "body": "Josiah's reform (2 Kings 22-23) is the most thoroughgoing religious reformation "
                    "in Israel's history. After the discovery of 'the Book of the Law' in the Temple "
                    "(widely identified as Deuteronomy or a form of it), Josiah destroyed the high "
                    "places, removed the Asherah from the Temple, demolished the houses of the cult "
                    "prostitutes, defiled Topheth in the Valley of Hinnom (where children were burned "
                    "to Molech), and even desecrated the altar at Bethel — fulfilling the prophecy "
                    "of 1 Kings 13:2 by name. The Deuteronomistic verdict on Josiah is the highest "
                    "praise given to any king: 'Before him there was no king like him, who turned to "
                    "YHWH with all his heart and with all his soul and with all his might, according "
                    "to all the Law of Moses, nor did any like him arise after him' (23:25). Yet the "
                    "next verse delivers the devastating caveat: 'Still YHWH did not turn from the "
                    "burning of his great wrath, by which his anger was kindled against Judah, because "
                    "of all the provocations with which Manasseh had provoked him' (23:26). The "
                    "accumulated sin was too great; the judgment was irreversible. Josiah's reform "
                    "could delay but not prevent the exile."
        },
        {
            "type": "scholarship",
            "title": "Extra-Biblical Corroboration — The Most Confirmed Book in the Bible",
            "body": "2 Kings is the most externally corroborated book in the Hebrew Bible. Assyrian "
                    "and Babylonian royal inscriptions, the Tel Dan Inscription, the Mesha Stele, the "
                    "Siloam Tunnel Inscription, the Lachish Letters, the Babylonian ration tablets, and "
                    "extensive archaeological evidence from destruction layers across Judah all confirm "
                    "the historical framework of 2 Kings. Sennacherib's Prism describes his campaign "
                    "against Hezekiah in terms remarkably consistent with 2 Kings 18-19 — including "
                    "the notable failure to claim Jerusalem's capture. The Babylonian Chronicles record "
                    "Nebuchadnezzar's conquest of Jerusalem in 597 BC in terms matching 2 Kings 24:10-17. "
                    "The ration tablets from Babylon list 'Yaukin, king of the land of Yahud' (Jehoiachin "
                    "of Judah) as receiving provisions — confirming 2 Kings 25:27-30 from the Babylonian "
                    "side. This wealth of external evidence establishes the historical reliability of "
                    "the book's narrative framework and provides a control against which the theological "
                    "interpretation can be assessed."
        }
    ]
}
