"""
info.py — Isaiah (Yeshayahu): Scholarly Text Introduction

This file provides the "front page" for Isaiah in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Isaiah is the Mount Everest of Old Testament prophecy — 66 chapters that
span the full arc of redemptive history from the divine council's throne room
(chapter 6) to the new heavens and new earth (chapters 65-66). It contains
the most explicit divine council call narrative in scripture ("Whom shall I
send, and who will go for us?" — 6:8), the Servant Songs that describe the
Messiah's suffering and exaltation, the fall of the divine rebel Helel ben
Shachar (14:12-15), the cosmic Day of the Lord judgment against all spiritual
powers, and the eschatological vision of YHWH's universal reign. Isaiah is
the most quoted prophetic book in the New Testament and the theological
foundation for understanding Jesus' mission.
"""

TEXT_INFO = {
    "text_id": "isaiah",
    "display_name": "Isaiah (Yeshayahu)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Latter Prophets",
        "detail": "Isaiah is the first book of the Latter Prophets (Nevi'im Acharonim) in the Hebrew "
                  "Bible and the first of the Major Prophets in the Christian Old Testament. It is "
                  "universally canonical across all Jewish and Christian traditions. Isaiah is the "
                  "second most quoted OT book in the New Testament (after Psalms), with over 250 "
                  "quotations and allusions. Jesus inaugurated his public ministry by reading from "
                  "Isaiah 61 in the Nazareth synagogue: 'The Spirit of the Lord is upon me, because "
                  "he has anointed me to proclaim good news to the poor' (Luke 4:18-19). The Ethiopian "
                  "eunuch was reading Isaiah 53 when Philip encountered him (Acts 8:26-35). Paul built "
                  "his theology of Gentile inclusion on Isaiah's vision of the nations streaming to "
                  "Zion (Isa 2:2-4; cf. Rom 15:12). John's Gospel identifies Isaiah as the prophet "
                  "who 'saw Christ's glory and spoke of him' (John 12:41, referencing the throne vision "
                  "of Isaiah 6). The book's canonical authority has never been questioned by any "
                  "tradition."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Isaiah son of Amoz, a prophet active in Jerusalem during the reigns of Uzziah, "
                       "Jotham, Ahaz, and Hezekiah (~740-686 BC). Jewish tradition (Talmud Bava Batra "
                       "15a) states that 'Hezekiah and his council wrote Isaiah,' meaning they compiled "
                       "and edited Isaiah's oracles. Isaiah had access to the royal court (7:3; 37-39) "
                       "and was married to a prophetess (8:3). Rabbinic tradition records that he was "
                       "martyred under Manasseh by being sawn in two (possibly referenced in Hebrews "
                       "11:37). The New Testament attributes the entire book to 'Isaiah the prophet': "
                       "Matthew 4:14 cites Isaiah 9:1-2; Matthew 12:17 cites the Servant Song of "
                       "42:1-4; John 12:38-41 cites both Isaiah 53:1 and 6:10 under Isaiah's name; "
                       "Romans 10:16-20 cites both Isaiah 53:1 and 65:1 as 'Isaiah says.'",

        "scholarly_debate": "Since Bernhard Duhm (1892), critical scholarship has divided Isaiah into "
                           "three sections: First Isaiah (chapters 1-39), attributed to the 8th-century "
                           "prophet; Second Isaiah or Deutero-Isaiah (chapters 40-55), attributed to an "
                           "anonymous exilic prophet (~545-539 BC) who proclaimed comfort and return; "
                           "and Third Isaiah or Trito-Isaiah (chapters 56-66), attributed to a post-exilic "
                           "prophet or school (~520-450 BC). The primary argument for multiple authorship "
                           "is the historical setting: chapters 40-55 address an exilic audience and name "
                           "Cyrus of Persia (44:28; 45:1), who lived 150 years after Isaiah. Conservative "
                           "scholars (Oswalt, Motyer, Young) argue for essential unity of authorship, "
                           "noting: (1) the naming of Cyrus is predictive prophecy, consistent with "
                           "Isaiah's prophetic gift; (2) the theological vocabulary, imagery, and themes "
                           "('the Holy One of Israel' — used 25 times across all sections) unify the book; "
                           "(3) the Dead Sea Scrolls Great Isaiah Scroll (1QIsa^a) shows no break between "
                           "chapters 39 and 40; (4) ancient Jewish and Christian tradition uniformly "
                           "attributed the entire book to Isaiah.",

        "bottom_line": "Whether composed by a single prophet (Isaiah son of Amoz) whose vision spanned "
                       "centuries, or by a school of disciples who preserved and extended his prophetic "
                       "tradition, the book of Isaiah presents a unified theological vision centered on "
                       "'the Holy One of Israel,' the sovereignty of YHWH over all nations and all "
                       "spiritual powers, and the coming of a Servant-King who will bring salvation "
                       "to both Israel and the nations. The divine council framework is consistent "
                       "throughout: the throne vision of chapter 6 establishes the prophetic commission, "
                       "and the Servant Songs (42, 49, 50, 52-53) describe the council's chosen agent "
                       "for cosmic redemption."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Isaiah's ministry spanned ~740-686 BC (from Uzziah's death to Hezekiah's "
                       "reign). The entire book is attributed to this period, with chapters 40-66 "
                       "representing prophetic vision of the future rather than contemporary address.",
        "critical_range": "First Isaiah (1-39): ~740-686 BC, with possible editorial additions from "
                         "the 7th-6th century. Deutero-Isaiah (40-55): ~545-539 BC, during the Babylonian "
                         "exile. Trito-Isaiah (56-66): ~520-450 BC, during the early post-exilic period. "
                         "Final editing and compilation: ~450-300 BC.",
        "evidence": "Key evidence includes: (1) The Great Isaiah Scroll (1QIsa^a) from Qumran, dating "
                    "to ~125 BC, is the oldest complete manuscript of any biblical book. It preserves "
                    "all 66 chapters with no physical break between chapters 39 and 40, supporting the "
                    "book's unity as received. (2) The Isaiah Scroll (1QIsa^b) is a fragmentary second "
                    "copy generally closer to the MT. (3) Multiple additional DSS Isaiah fragments "
                    "(4QIsa^a-f) have been found, making Isaiah one of the best-attested books at "
                    "Qumran. (4) The Sennacherib narrative (chapters 36-39) parallels 2 Kings 18-20 "
                    "almost verbatim, confirming the 8th-century historical setting. (5) The Cyrus "
                    "Oracle (44:28-45:1) names the Persian king who conquered Babylon in 539 BC — "
                    "either predictive prophecy or evidence of an exilic author. (6) The theological "
                    "vocabulary ('the Holy One of Israel,' 'the Servant of YHWH') is remarkably "
                    "consistent across all sections."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "Multiple audiences across multiple settings: (1) 8th-century Judah — "
                            "facing the Assyrian crisis, challenged to trust YHWH rather than foreign "
                            "alliances; (2) the exilic community — addressed with comfort and the promise "
                            "of return through YHWH's anointed agent Cyrus; (3) the post-exilic community "
                            "— challenged to rebuild, maintain justice, and wait for YHWH's final "
                            "redemption. Across all settings, the audience is called to trust the Holy "
                            "One of Israel rather than the gods of the nations or human political power.",

        "purpose": "Isaiah's overarching purpose is to declare YHWH's absolute sovereignty over all "
                   "nations, all history, and all spiritual powers — and to announce his plan to redeem "
                   "Israel and the world through his chosen Servant. The book moves in a grand arc: "
                   "judgment on Judah and the nations (1-35), the hinge of the Hezekiah narratives "
                   "(36-39), comfort and the promise of return (40-55), and the eschatological vision "
                   "of new creation (56-66). The Servant of YHWH is the central figure of chapters "
                   "40-55 — initially identified with Israel (41:8-9; 44:1-2; 49:3) but progressively "
                   "distinguished from Israel as an individual who will suffer for the nation's sins "
                   "(52:13-53:12) and bring light to the Gentiles (42:6; 49:6).",

        "theological_intent": "Isaiah's theological vision is cosmic in scope. The throne vision "
                             "(chapter 6) establishes YHWH as the universal sovereign, enthroned in "
                             "the heavenly temple, with seraphim declaring his holiness. The oracles "
                             "against the nations (chapters 13-23) demonstrate YHWH's authority over "
                             "every territory — including those allotted to other gods under the "
                             "Deuteronomy 32 framework. The Servant Songs reveal YHWH's plan to redeem "
                             "not just Israel but 'the ends of the earth' (49:6). The Day of the Lord "
                             "passages (13:6-13; 24-27; 34-35; 63-66) envision a final judgment that "
                             "encompasses both the earthly and heavenly realms: 'On that day YHWH will "
                             "punish the host of heaven, in heaven, and the kings of the earth, on the "
                             "earth' (24:21). This is the divine council's eschatological judgment — the "
                             "corrupt spiritual rulers and their human agents will be judged together."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Paleo-Hebrew script (pre-exilic) -> Aramaic square script (post-exilic)",
        "linguistic_notes": "Isaiah's Hebrew is among the most sophisticated in the Bible. First Isaiah "
                           "(1-39) uses powerful, compact prophetic poetry with vivid imagery: the 'Song "
                           "of the Vineyard' (5:1-7), the Immanuel oracle (7:14), and the messianic hymn "
                           "(9:2-7) are masterpieces of Hebrew verse. Deutero-Isaiah (40-55) develops a "
                           "distinctive rhetorical style characterized by comfort language ('Comfort, "
                           "comfort my people'), trial speeches (41:1-5, 21-29; 43:8-13), disputations "
                           "(40:12-31), and the Servant Songs (42:1-9; 49:1-7; 50:4-11; 52:13-53:12). "
                           "The name 'Isaiah' (Yeshayahu) means 'YHWH saves/is salvation' — the same "
                           "root (y-sh-a) as 'Jesus' (Yeshua). The title 'Holy One of Israel' (qedosh "
                           "yisrael) appears 25 times across all sections, serving as a unifying "
                           "theological signature. The seraphim's trishagion (6:3, 'Holy, holy, holy is "
                           "YHWH of hosts; the whole earth is full of his glory') is the foundational "
                           "worship formula that recurs in Revelation 4:8.",
        "grammar_match": "The poetic style varies across the book's sections but maintains a "
                        "consistently elevated register. First Isaiah favors terse, compact oracles "
                        "with striking metaphors. Deutero-Isaiah uses longer, flowing lines with "
                        "rhetorical questions and comfort language. Trito-Isaiah combines elements of "
                        "both with additional liturgical and eschatological vocabulary. The linguistic "
                        "debate about unity vs. multiple authors partly depends on whether these "
                        "stylistic differences indicate different authors or different literary "
                        "situations addressed by the same prophetic tradition."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Isaiah IS scripture — the prophetic summit of the Old Testament, the theological "
                   "foundation for understanding Jesus' messianic mission, and the most quoted "
                   "prophetic book in the New Testament.",
        "nt_usage": "Isaiah is quoted or alluded to over 250 times in the New Testament. The most "
                    "theologically significant citations include: Isaiah 7:14 ('a virgin shall conceive') "
                    "— applied to Jesus' birth (Matt 1:23). Isaiah 9:1-2 ('a great light') — fulfilled "
                    "in Jesus' Galilean ministry (Matt 4:14-16). Isaiah 9:6-7 ('Wonderful Counselor, "
                    "Mighty God, Everlasting Father, Prince of Peace') — the messianic titles. Isaiah "
                    "40:3 ('a voice crying in the wilderness') — applied to John the Baptist (Matt 3:3; "
                    "Mark 1:3; Luke 3:4; John 1:23). Isaiah 42:1-4 (the first Servant Song) — applied "
                    "to Jesus (Matt 12:17-21). Isaiah 52:13-53:12 (the Suffering Servant) — the single "
                    "most important OT messianic prophecy, cited throughout the NT (Matt 8:17; Luke "
                    "22:37; John 12:38; Acts 8:32-35; Rom 10:16; 1 Pet 2:22-25). Isaiah 61:1-2 — "
                    "Jesus' inaugural sermon text (Luke 4:18-19). Isaiah 6:9-10 (the hardening "
                    "commission) — cited by Jesus (Matt 13:14-15), John (12:40), and Paul (Acts 28:26-27).",
        "internal_consistency": "Isaiah is deeply interwoven with the rest of the Hebrew Bible. The "
                               "throne vision (chapter 6) connects to the divine council scenes of "
                               "1 Kings 22, Job 1-2, and Psalm 82. The Immanuel prophecy (7:14) develops "
                               "the Davidic covenant of 2 Samuel 7. The Servant Songs draw on and "
                               "transform the 'Servant' (ebed) language used of Moses, David, and Israel. "
                               "The oracles against Babylon (13-14) connect to the Babel narrative "
                               "(Genesis 11) and the fall of Babylon in Daniel 5. The new creation vision "
                               "(65:17-25) echoes and fulfills Genesis 1-2. Isaiah 24-27 (the 'Isaiah "
                               "Apocalypse') provides the earliest sustained eschatological vision that "
                               "Daniel and Revelation will develop."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "The Great Isaiah Scroll (1QIsa^a) from Qumran Cave 1, dating to ~125 BC, is the "
                    "oldest complete manuscript of any biblical book. It contains all 66 chapters of "
                    "Isaiah written on 17 sheets of parchment sewn together into a scroll approximately "
                    "24 feet long. It is one of the most important manuscript discoveries in history.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. The MT of Isaiah is well-preserved and generally "
                     "close to 1QIsa^b (the second Qumran Isaiah scroll)."},
            {"name": "Great Isaiah Scroll (1QIsa^a)", "date": "~125 BC",
             "note": "The oldest complete biblical manuscript. It differs from the MT in approximately "
                     "2,600 textual variants, most of which are orthographic (spelling differences) "
                     "or minor. A handful are theologically significant: e.g., 1QIsa^a reads 'and they "
                     "will look on me, whom they have pierced' at a passage related to Zechariah 12:10 "
                     "tradition. The scroll shows no break between chapters 39 and 40."},
            {"name": "Second Isaiah Scroll (1QIsa^b)", "date": "~50 BC",
             "note": "Fragmentary, preserving portions of chapters 7-66. Closer to the MT than "
                     "1QIsa^a, supporting the proto-Masoretic text tradition's early existence."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC translation",
             "note": "The Greek Isaiah is one of the most 'free' LXX translations, sometimes "
                     "paraphrasing or interpreting rather than literally translating. Key variant: "
                     "Isaiah 7:14 reads 'parthenos' (virgin) for the Hebrew 'almah' (young woman), "
                     "a translation decision that became critically important for christology. The "
                     "LXX of Isaiah 52:13-53:12 shows messianic interpretive tendencies."},
            {"name": "Targum Jonathan", "date": "1st-3rd century AD tradition",
             "note": "The Aramaic Targum of Isaiah is highly interpretive, often adding messianic "
                     "identifications and theological commentary. At Isaiah 52:13-53:12, the Targum "
                     "identifies the Servant as the Messiah but redistributes the suffering to the "
                     "nations rather than the Messiah himself — a remarkable interpretive move."}
        ],
        "reliability": "Isaiah has the best manuscript attestation of any prophetic book. The Great "
                       "Isaiah Scroll (1QIsa^a) predates the earliest MT manuscripts by over 1,000 "
                       "years and confirms the remarkable stability of the textual transmission. The "
                       "theological content — the throne vision, the Servant Songs, the messianic "
                       "oracles, the eschatological vision — is stable across all major witnesses."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Isaiah's ministry began in the year King Uzziah died (~740 BC) and extended through "
                   "the Assyrian crisis — the most traumatic geopolitical event of the 8th century. The "
                   "Assyrian Empire under Tiglath-Pileser III, Shalmaneser V, Sargon II, and Sennacherib "
                   "conquered the entire Near East, destroying the northern kingdom of Israel in 722 BC "
                   "and besieging Jerusalem in 701 BC. Isaiah's prophetic ministry addressed this crisis "
                   "directly: trust YHWH, not Egypt or Assyria; the Holy One of Israel will protect "
                   "Jerusalem for the sake of the Davidic covenant.",

        "geography": "Isaiah's primary setting is Jerusalem — the city from which he prophesied, the "
                     "Temple where he received his call (chapter 6), and the Zion whose future glory "
                     "he proclaims. The oracles against the nations (chapters 13-23) range across the "
                     "ancient Near East: Babylon, Assyria, Philistia, Moab, Damascus, Ethiopia, Egypt, "
                     "Edom, Arabia, and Tyre. The Servant Songs envision a ministry that extends to "
                     "'the ends of the earth' (49:6). The eschatological vision encompasses 'new heavens "
                     "and a new earth' (65:17; 66:22) — the entire cosmos remade.",

        "historical_connections": "The Sennacherib crisis (chapters 36-39 // 2 Kings 18-20) is confirmed "
                                 "by Sennacherib's Prism, which describes besieging Hezekiah in Jerusalem "
                                 "but never claims to have captured the city. The fall of Babylon to Cyrus "
                                 "in 539 BC fulfills the oracles of chapters 13-14 and 44-45. The return "
                                 "from exile under Cyrus's edict (Ezra 1:1-4) fulfills the comfort "
                                 "prophecies of chapters 40-55. The Cyrus Cylinder (~539 BC) — a Babylonian "
                                 "inscription recording Cyrus's policy of returning exiled peoples and their "
                                 "gods — provides external confirmation of the type of activity described in "
                                 "Isaiah 44-45 and Ezra 1."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "foundational",
        "summary": "Isaiah contains the most comprehensive divine council theology of any prophetic "
                   "book — from the throne vision and council call to the cosmic Day of the Lord "
                   "judgment against spiritual powers."
                   "\n\n"
                   "THE THRONE VISION AND COUNCIL CALL (Isaiah 6): Isaiah sees 'the Lord sitting "
                   "upon a throne, high and lifted up, and the train of his robe filled the temple' "
                   "(6:1). The seraphim — fiery, six-winged celestial beings — attend the throne, "
                   "crying 'Holy, holy, holy is YHWH of hosts; the whole earth is full of his glory' "
                   "(6:3). This is the divine council in its most exalted form: YHWH enthroned, "
                   "surrounded by his heavenly court, in the temple that is simultaneously the "
                   "earthly sanctuary and the heavenly throne room. After Isaiah's cleansing (the "
                   "coal from the altar, 6:6-7), YHWH speaks to the council: 'Whom shall I send, "
                   "and who will go for US?' (6:8). The plural 'us' is divine council language — "
                   "YHWH is addressing his heavenly assembly, and Isaiah volunteers for the council's "
                   "mission. This is the paradigmatic prophetic call: the prophet stands in YHWH's "
                   "council, hears the council's deliberation, and is sent as its messenger (cf. "
                   "Jer 23:18, 22 — 'Who has stood in the council of YHWH?'). John 12:41 identifies "
                   "the figure on the throne as the pre-incarnate Christ: 'Isaiah said these things "
                   "because he saw his glory and spoke of him.'"
                   "\n\n"
                   "HELEL BEN SHACHAR — THE FALL OF THE SHINING ONE (Isaiah 14:12-15): 'How you "
                   "are fallen from heaven, O Day Star, son of Dawn! How you are cut down to the "
                   "ground, you who laid the nations low! You said in your heart, \"I will ascend "
                   "to heaven; above the stars of God I will set my throne; I will sit on the mount "
                   "of assembly (har mo'ed) in the far reaches of the north...\"' (14:12-13). While "
                   "the primary referent is the king of Babylon, the cosmic language transcends any "
                   "human king: ascending to heaven, setting a throne above the 'stars of God' "
                   "(a divine council term for spiritual beings, cf. Job 38:7), sitting on the "
                   "'mount of assembly' (the divine council's meeting place) — this describes a "
                   "divine being's rebellion against YHWH's authority. The 'mount of assembly in the "
                   "far reaches of the north' (tsaphon) is the Canaanite term for the gods' mountain "
                   "(Mount Zaphon, Baal's sacred mountain). The passage became the foundational text "
                   "for the Christian tradition of Satan's fall (cf. Luke 10:18, 'I saw Satan fall "
                   "like lightning from heaven'; Rev 12:7-9). In the divine council framework, this "
                   "is a divine being who sought to usurp YHWH's throne — the ultimate cosmic rebellion."
                   "\n\n"
                   "THE SERVANT SONGS (42:1-9; 49:1-7; 50:4-11; 52:13-53:12): The Servant of YHWH "
                   "is the divine council's chosen agent for cosmic redemption. 'Behold my servant, "
                   "whom I uphold, my chosen, in whom my soul delights; I have put my Spirit upon "
                   "him; he will bring forth justice to the nations' (42:1). The Servant is presented "
                   "to the council and commissioned with a universal mission. The Fourth Servant Song "
                   "(52:13-53:12) describes vicarious suffering: 'He was pierced for our transgressions; "
                   "he was crushed for our iniquities... YHWH has laid on him the iniquity of us all' "
                   "(53:5-6). The Servant's exaltation — 'he shall be high and lifted up' (52:13, using "
                   "the same language as the throne vision in 6:1) — places him at the highest position "
                   "in the divine council. The Ethiopian eunuch's question — 'About whom does the "
                   "prophet say this, about himself or about someone else?' (Acts 8:34) — is answered "
                   "by Philip: Jesus."
                   "\n\n"
                   "THE DAY OF THE LORD — COSMIC JUDGMENT (Isaiah 24:21; 34:1-5): 'On that day YHWH "
                   "will punish the host of heaven, in heaven, and the kings of the earth, on the "
                   "earth. They will be gathered together as prisoners in a pit; they will be shut up "
                   "in a prison, and after many days they will be punished' (24:21-22). This is the "
                   "Deuteronomy 32 worldview in its eschatological culmination: the spiritual rulers "
                   "of the nations ('the host of heaven') and their human agents ('the kings of the "
                   "earth') will be judged together. Isaiah 34:1-5 extends this: 'All the host of "
                   "heaven shall rot away, and the skies roll up like a scroll. All their host shall "
                   "fall' (34:4). The New Testament draws directly on this language: Revelation 6:13-14 "
                   "echoes Isaiah 34:4; Ephesians 6:12 identifies the 'cosmic powers over this present "
                   "darkness' and 'spiritual forces of evil in the heavenly places' as the enemy.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 2-3 (the divine council — Isaiah 6 as paradigmatic)",
            "The Unseen Realm, chapter 8-10 (the fall of Helel ben Shachar / Satan's rebellion)",
            "The Unseen Realm, chapter 27-30 (the Servant Songs and the messianic agent)",
            "The Unseen Realm, chapter 35 (eschatological judgment of the host of heaven)",
            "Supernatural, chapter 5-6 (the throne vision and the divine council call)",
            "Angels: What the Bible Really Says About God's Heavenly Host, ch. 5-6 (seraphim, the heavenly court)",
            "Demons: What the Bible Really Says About the Powers of Darkness, ch. 8-9 (Helel/Lucifer and cosmic rebellion)",
            "The Naked Bible Podcast, episodes 140-155 (Isaiah and the divine council)",
            "The Naked Bible Podcast, episode 12 (Isaiah 14 — the fall of Helel ben Shachar)"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Throne Vision — Standing in the Council of YHWH",
            "body": "Isaiah 6 is the paradigmatic divine council call narrative. Isaiah does not merely "
                    "receive a message — he is transported into YHWH's throne room and participates in "
                    "the council's deliberation. The seraphim (literally 'burning ones') are a class of "
                    "celestial beings found only here in the Hebrew Bible. Their six wings serve three "
                    "functions: two cover their faces (they cannot look directly at YHWH's glory), two "
                    "cover their 'feet' (a euphemism for their lower body, indicating modesty before "
                    "the divine presence), and two are used for flight. The trishagion — 'Holy, holy, "
                    "holy' — became the foundational worship formula for both synagogue and church, "
                    "echoed in Revelation 4:8. Isaiah's response ('Woe is me! I am lost, for I am a "
                    "man of unclean lips') and his cleansing by the burning coal model the prophetic "
                    "pattern: awareness of sin, divine purification, and commission. The plural 'us' "
                    "in 'who will go for us?' (6:8) is the voice of the divine council — and John "
                    "12:41's identification of the enthroned figure as Christ means Isaiah saw the "
                    "pre-incarnate Son in his heavenly glory."
        },
        {
            "type": "interpretation",
            "title": "Helel ben Shachar — Lucifer, Satan, and the King of Babylon",
            "body": "Isaiah 14:12-15 addresses the king of Babylon but uses cosmic language that "
                    "transcends any human ruler. 'Helel ben Shachar' (shining one, son of the dawn) "
                    "was translated 'Lucifer' (light-bearer) in the Latin Vulgate, and this passage "
                    "became the primary source for the Christian tradition of Satan's fall from heaven. "
                    "Michael Heiser's analysis places this in the divine council framework: the figure "
                    "is a divine being who aspired to usurp YHWH's throne, claiming authority over the "
                    "'mount of assembly' (har mo'ed) — the divine council's meeting place. The 'stars "
                    "of God' above which he sought to place his throne are council members (cf. Job "
                    "38:7, where 'morning stars' parallel 'sons of God'). Whether this describes Satan "
                    "specifically, the spiritual power behind Babylon, or a broader pattern of cosmic "
                    "rebellion, the passage establishes that divine beings can rebel against YHWH's "
                    "authority and that such rebellion results in catastrophic judgment — being 'brought "
                    "down to Sheol, to the far reaches of the pit' (14:15)."
        },
        {
            "type": "context",
            "title": "The Suffering Servant — Isaiah 53 and the Messiah",
            "body": "Isaiah 52:13-53:12 is the most detailed prophecy of the Messiah's suffering in the "
                    "Old Testament. The passage describes a figure who is despised, rejected, pierced for "
                    "transgressions, crushed for iniquities, led like a lamb to slaughter, assigned a "
                    "grave with the wicked, and yet 'after his anguish he shall see light' and 'make many "
                    "to be accounted righteous' (53:11). The early church identified this with Jesus' "
                    "passion from the very beginning (Acts 8:32-35). The passage's opening — 'he shall be "
                    "high and lifted up' (52:13) — uses the same Hebrew words (rum, nasa, gavah) as the "
                    "throne vision (6:1), suggesting the Servant shares YHWH's exalted status. The "
                    "Targum Jonathan identifies the Servant as the Messiah but deflects the suffering onto "
                    "the nations, revealing that the messianic identification was known in Judaism but the "
                    "suffering element was theologically problematic. In the divine council framework, the "
                    "Servant is YHWH's agent par excellence — commissioned by the council, empowered by "
                    "the Spirit, accomplishing through suffering what conquest could not achieve."
        },
        {
            "type": "scholarship",
            "title": "The Great Isaiah Scroll — Oldest Complete Biblical Manuscript",
            "body": "The Great Isaiah Scroll (1QIsa^a), discovered in 1947 in Qumran Cave 1, is the "
                    "oldest complete manuscript of any biblical book, dating to approximately 125 BC. "
                    "It predates the oldest MT manuscript by over 1,000 years and confirms the remarkable "
                    "fidelity of the textual transmission. Of approximately 2,600 textual variants between "
                    "1QIsa^a and the MT, the vast majority are orthographic (spelling differences) or "
                    "minor grammatical variations. Only a handful affect meaning significantly. The scroll "
                    "is particularly important for the authorship debate: there is no physical break, "
                    "scribal notation, or any other indication that chapters 1-39 and 40-66 were treated "
                    "as separate compositions. Column 27 (which contains the end of chapter 33) shows "
                    "the scribe leaving a few blank lines at the bottom — the only place this happens — "
                    "but this falls within 'First Isaiah,' not at the chapter 39-40 boundary. The scroll "
                    "is now housed in the Shrine of the Book at the Israel Museum in Jerusalem."
        }
    ]
}
