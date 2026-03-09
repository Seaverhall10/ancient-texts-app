"""
info.py -- Lamentations (Eikhah): Scholarly Text Introduction

This file provides the "front page" for Lamentations in the Ancient Texts Library.
It answers: Who wrote it? When? For whom? In what language? Does it align
with other scripture? What's the manuscript tradition? Where does it fit
in history and geography?

Lamentations is the Hebrew Bible's grief made poetry -- five acrostic poems
mourning the destruction of Jerusalem and the temple in 586 BC. The Hebrew
title "Eikhah" (How!) is the book's opening cry: "How lonely sits the city
that was full of people!" (1:1). The poems unflinchingly describe the horror
of siege, starvation, and slaughter, while wrestling with the theological
crisis: YHWH has done this. "He has bent his bow like an enemy" (2:4). Yet
at the center of the book (3:21-24), hope breaks through: "The steadfast
love (chesed) of YHWH never ceases; his mercies (rachamim) never come to
an end; they are new every morning; great is your faithfulness (emunatekha)."
The book is a theological masterwork: it holds together the reality of divine
judgment, the legitimacy of human grief, and the persistence of hope.
"""

TEXT_INFO = {
    "text_id": "lamentations",
    "display_name": "Lamentations (Eikhah)",

    # -- CANONICAL STATUS -------------------------------------------------------
    "canonical_status": {
        "status": "canonical",
        "label": "Canonical -- Old Testament / Writings (Ketuvim) or follows Jeremiah",
        "detail": "Lamentations is universally canonical across all Jewish and Christian traditions. In "
                  "the Hebrew Bible, it is placed among the Five Megillot (Scrolls) in the Writings "
                  "(Ketuvim), read liturgically on Tisha B'Av (the 9th of Av), the annual fast "
                  "commemorating the destruction of both the First and Second Temples. In the "
                  "Septuagint and Christian Old Testament, Lamentations is placed immediately after "
                  "Jeremiah, reflecting the traditional attribution to that prophet. The LXX prefixes "
                  "the book with a note: 'And it came to pass, after Israel was carried away captive "
                  "and Jerusalem laid waste, that Jeremiah sat weeping and composed this lament over "
                  "Jerusalem.' The book is not directly quoted in the New Testament but its theology "
                  "of divine judgment, righteous suffering, and persistent hope permeates NT thought, "
                  "especially the passion narratives."
    },

    # -- AUTHORSHIP -------------------------------------------------------------
    "authorship": {
        "traditional": "Jeremiah the prophet, as attributed by Jewish tradition (Talmud Bava Batra 15a: "
                       "'Jeremiah wrote his book, the book of Kings, and Lamentations') and the "
                       "Septuagint's superscription. The identification is based on 2 Chronicles 35:25 "
                       "('Jeremiah also uttered a lament for Josiah'), Jeremiah's presence in Jerusalem "
                       "during and after the siege, and the thematic connections between Lamentations and "
                       "Jeremiah's prophecy (suffering prophet, fall of Jerusalem, covenant judgment).",

        "scholarly_debate": "Most modern scholars doubt Jeremianic authorship, noting: (1) the poetry of "
                           "Lamentations differs stylistically from Jeremiah's prophetic oracles; (2) "
                           "Lamentations never names its author; (3) certain perspectives differ -- e.g., "
                           "Lamentations 4:17 describes hoping for help from a 'nation that could not save' "
                           "(Egypt), while Jeremiah consistently warned against Egyptian alliance; (4) the "
                           "elaborate acrostic structure suggests careful literary composition rather than "
                           "spontaneous prophetic utterance. Some scholars attribute the poems to multiple "
                           "authors; others to a single anonymous poet who witnessed the destruction.",

        "bottom_line": "Whether Jeremiah or another eyewitness composed these poems, they represent the "
                       "authentic voice of a community that experienced the destruction of Jerusalem "
                       "firsthand. The theology is consistent with the prophetic tradition: the destruction "
                       "was YHWH's righteous judgment for covenant violation, yet his steadfast love (chesed) "
                       "endures, and hope remains for restoration."
    },

    # -- DATE -------------------------------------------------------------------
    "date": {
        "traditional": "Shortly after the destruction of Jerusalem in 586 BC, while the devastation "
                       "was still fresh. The vivid, eyewitness quality of the descriptions suggests "
                       "composition within years of the event.",
        "critical_range": "~586-550 BC. The poems reflect immediate experience of the destruction and "
                         "its aftermath. Some scholars suggest the five poems may have been composed "
                         "at slightly different times and compiled into a collection. The acrostic "
                         "structure suggests deliberate literary crafting, but the raw emotional power "
                         "argues against significant temporal distance from the events.",
        "evidence": "Key evidence includes: (1) The descriptions match the archaeological and historical "
                    "record of Jerusalem's destruction by Babylon. (2) The emotional intensity and "
                    "specificity of the suffering described (starvation, cannibalism, slaughter) argue "
                    "for eyewitness composition. (3) The acrostic structure using the Hebrew alphabet "
                    "reflects a literary tradition attested in earlier Hebrew poetry (Psalm 119, "
                    "Proverbs 31:10-31). (4) Dead Sea Scrolls: Fragments of Lamentations have been "
                    "found at Qumran (3QLam, 4QLam, 5QLam^a-b), confirming the text's early stability."
    },

    # -- AUDIENCE & PURPOSE -----------------------------------------------------
    "audience": {
        "original_audience": "The surviving community in the ruins of Jerusalem and Judah, and possibly "
                            "the exiles in Babylon. The poems gave voice to communal grief and provided "
                            "a theological framework for understanding the catastrophe. They were likely "
                            "used in liturgical gatherings to mourn the temple's destruction -- a practice "
                            "that continues to this day in Jewish liturgy on Tisha B'Av.",

        "purpose": "Lamentations serves multiple purposes: (1) to express and validate communal grief -- "
                   "the destruction was real, the suffering was devastating, and the community needed "
                   "authorized language for their pain; (2) to interpret the destruction theologically -- "
                   "YHWH did this as righteous judgment for covenant violation, not because he was absent "
                   "or powerless; (3) to preserve hope -- even in the darkest moment, YHWH's chesed "
                   "endures (3:22-24); (4) to model faithful prayer -- the poems address YHWH directly, "
                   "even accusingly, maintaining the covenant relationship even through judgment.",

        "theological_intent": "Lamentations holds together truths that lesser theology would separate: "
                             "YHWH is sovereign AND the suffering is devastating; the judgment is deserved "
                             "AND the pain is legitimate; hope persists AND grief is appropriate. The "
                             "book refuses both cheap comfort (everything is fine) and total despair "
                             "(everything is lost). It models what Walter Brueggemann calls 'costly speech' "
                             "-- speaking to God from the depths of suffering without abandoning faith. The "
                             "acrostic structure itself is theologically significant: by using every letter "
                             "of the Hebrew alphabet, the poet exhausts the full range of grief, literally "
                             "going from aleph to tav (A to Z) in lamentation."
    },

    # -- ORIGINAL LANGUAGE -------------------------------------------------------
    "language": {
        "original": "Biblical Hebrew",
        "script": "Aramaic square script (post-exilic)",
        "linguistic_notes": "Lamentations is among the finest poetry in the Hebrew Bible. The five chapters "
                           "employ acrostic structures: chapters 1, 2, and 4 are alphabetic acrostics "
                           "(22 verses, each beginning with a successive letter of the Hebrew alphabet); "
                           "chapter 3 is a triple acrostic (66 verses, three verses for each letter); "
                           "chapter 5 has 22 verses but is not acrostic (perhaps representing the breakdown "
                           "of order). The qinah (lament) meter -- a 3+2 beat pattern -- dominates, "
                           "creating a limping, falling rhythm that embodies the sense of loss. The Hebrew "
                           "title 'Eikhah' (How!) is the characteristic opening of the funeral lament. "
                           "Key vocabulary includes chesed (steadfast love), rachamim (mercies/compassion), "
                           "emunah (faithfulness), and chata (to sin) -- the theological lexicon of "
                           "covenant, judgment, and hope.",
        "grammar_match": "The poetry is classical Hebrew at its most disciplined and powerful. The "
                        "acrostic constraint forces a compression of expression that heightens emotional "
                        "intensity. The language is generally consistent with 6th-century BC Hebrew, "
                        "though the poetic register makes precise dating by linguistic criteria difficult."
    },

    # -- SCRIPTURE ALIGNMENT -----------------------------------------------------
    "scripture_alignment": {
        "verdict": "Lamentations IS scripture -- the authorized voice of grief before God, the "
                   "theological interpretation of Jerusalem's destruction, and the stubborn persistence "
                   "of hope in the midst of judgment.",
        "nt_usage": "Lamentations is not directly quoted in the New Testament, but its themes pervade "
                    "the passion narratives. Jesus weeps over Jerusalem (Luke 19:41-44), echoing the "
                    "weeping of Lamentations. The cry of dereliction ('My God, my God, why have you "
                    "forsaken me?' Matt 27:46) resonates with Lamentations' sense of divine absence. "
                    "The Suffering Servant of Isaiah 53, who bears the people's griefs, fulfills the "
                    "theology of righteous suffering that Lamentations develops. The book of Revelation's "
                    "portrayal of 'Babylon the Great' falling (Rev 18) echoes the fall of Jerusalem "
                    "mourned in Lamentations.",
        "internal_consistency": "Lamentations fulfills the covenant curses of Deuteronomy 28 (especially "
                               "28:53-57 on siege cannibalism, cf. Lam 2:20; 4:10) and the prophetic "
                               "warnings of Jeremiah, Ezekiel, and Isaiah. It confirms the theological "
                               "interpretation found throughout the prophets: Jerusalem fell because of "
                               "covenant unfaithfulness, not because YHWH was powerless. The central "
                               "affirmation of YHWH's chesed (3:22-24) connects to the covenant theology "
                               "of Exodus 34:6-7 and the Psalms."
    },

    # -- MANUSCRIPT TRADITION ----------------------------------------------------
    "manuscripts": {
        "earliest": "Dead Sea Scrolls: Fragments from Qumran (3QLam, 4QLam, 5QLam^a-b) dating to "
                    "~150-50 BC. The fragments are small but confirm the text's general stability.",
        "major_witnesses": [
            {"name": "Masoretic Text (MT)", "date": "Codex Leningradensis, 1009 AD",
             "note": "The standard Hebrew text. The MT of Lamentations is well-preserved. Chapters 2, "
                     "3, and 4 reverse the order of the ayin and pe letters in the acrostic (pe before "
                     "ayin instead of ayin before pe), which may reflect an older alphabet order."},
            {"name": "Septuagint (LXX)", "date": "2nd century BC translation",
             "note": "The LXX adds a superscription attributing the book to Jeremiah and provides a "
                     "generally faithful translation. The LXX preserves the standard alphabet order "
                     "(ayin before pe) in all chapters."},
            {"name": "Dead Sea Scrolls", "date": "~150-50 BC",
             "note": "Small fragments confirming the proto-MT tradition. The acrostic structure is "
                     "preserved in the extant fragments."}
        ],
        "reliability": "The text of Lamentations is well-preserved and relatively simple from a text-"
                       "critical perspective. The most significant textual question is the ayin-pe "
                       "reversal in chapters 2-4 (MT) versus the standard order (LXX), which affects "
                       "the acrostic structure but not the meaning."
    },

    # -- HISTORICAL CONTEXT ------------------------------------------------------
    "historical_context": {
        "setting": "Jerusalem in the immediate aftermath of the Babylonian destruction of 586 BC. The "
                   "city has been burned, the temple destroyed, the walls breached, the population "
                   "killed, starved, or deported. The survivors live among the ruins, attempting to "
                   "comprehend the unthinkable: YHWH's city, YHWH's temple, YHWH's people -- "
                   "destroyed.",

        "geography": "Jerusalem -- the ruined city, its breached walls, its burned temple, its empty "
                     "streets. The 'daughter of Zion' (bat-Tsiyyon) sits in the dust. The 'roads to "
                     "Zion mourn, for none come to the festival' (1:4). The gates are 'desolate' (1:4). "
                     "The geography is intimate -- this is the poetry of someone who walked through "
                     "the ruins.",

        "historical_connections": "The Babylonian destruction of Jerusalem in 586 BC is confirmed by "
                                 "the Babylonian Chronicle, the archaeological destruction layer in "
                                 "Jerusalem, the Lachish Letters, and the books of Jeremiah, Ezekiel, "
                                 "and 2 Kings. The descriptions of famine, cannibalism, and slaughter in "
                                 "Lamentations match the horrific realities of ancient siege warfare "
                                 "described in other sources (the Neo-Assyrian Siege of Lachish reliefs, "
                                 "for example). The exile community commemorated the destruction annually, "
                                 "a practice that continues in Jewish observance of Tisha B'Av."
    },

    # -- DIVINE COUNCIL / HEISER FRAMEWORK --------------------------------------
    "divine_council": {
        "relevance": "moderate",
        "summary": "Lamentations does not contain explicit divine council scenes, but its theology "
                   "presupposes the council's sovereign authority. The destruction of Jerusalem is "
                   "portrayed as YHWH's deliberate action -- 'He has bent his bow like an enemy' "
                   "(2:4); 'YHWH has done what he purposed' (2:17); 'He has torn down without pity' "
                   "(2:17). The poet does not attribute the destruction to Babylonian military "
                   "superiority or to YHWH's absence but to YHWH's active, sovereign judgment. This "
                   "is the divine council's decree being executed."
                   "\n\n"
                   "The language of 2:1-8 describes YHWH as a warrior who has attacked his own people "
                   "-- language drawn from the divine warrior tradition associated with YHWH's council "
                   "appearances. 'He has cut down in fierce anger all the might of Israel; he has "
                   "withdrawn from them his right hand' (2:3). The withdrawal of the 'right hand' is "
                   "the withdrawal of divine protection -- the council's shield removed."
                   "\n\n"
                   "The central hope passage (3:22-24) appeals to YHWH's covenant character -- his "
                   "chesed, rachamim, and emunah -- which are attributes of the divine king presiding "
                   "over the council. Even in judgment, the council's sovereign is characterized by "
                   "steadfast love. The book's theology of justified grief, legitimate protest, and "
                   "persistent hope models the proper response of the covenant community when the "
                   "council's judgment falls.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 14 (covenant curses and divine judgment)",
            "Supernatural, chapter 10 (YHWH as divine warrior)",
            "The Naked Bible Podcast, episodes on covenant theology and divine judgment"
        ]
    },

    # -- WARNINGS / READER NOTES ------------------------------------------------
    "reader_notes": [
        {
            "type": "theology",
            "title": "The Steadfast Love of YHWH -- Hope at the Center",
            "body": "Lamentations 3:22-24 is the theological center of the book -- literally (chapter 3 "
                    "is the middle chapter) and theologically. 'The steadfast love (chesed) of YHWH never "
                    "ceases; his mercies (rachamim) never come to an end; they are new every morning; "
                    "great is your faithfulness (emunatekha). \"YHWH is my portion (chelqi),\" says my "
                    "soul, \"therefore I will hope in him.\"' This affirmation is not naive optimism -- "
                    "it comes after two chapters of devastating grief and before two more. Hope is not "
                    "denial of suffering but a stubborn refusal to let suffering have the final word. "
                    "The hymn 'Great Is Thy Faithfulness' is based on this passage."
        },
        {
            "type": "context",
            "title": "Tisha B'Av -- The Ongoing Liturgical Life of Lamentations",
            "body": "Lamentations is read in Jewish synagogues on Tisha B'Av (the 9th of Av), a fast "
                    "day commemorating the destruction of both the First Temple (586 BC) and the Second "
                    "Temple (70 AD). According to tradition, both destructions occurred on the same "
                    "calendar date. The book is chanted in a distinctive, mournful melody (trope). "
                    "Worshippers sit on low chairs or the floor, as mourners do during shiva. Lamentations "
                    "is thus not merely ancient literature but living liturgy -- a community continues "
                    "to give voice to grief, to confess sin, and to hope in YHWH's chesed."
        },
        {
            "type": "interpretation",
            "title": "The Acrostic Structure -- Ordering Chaos Through Poetry",
            "body": "The acrostic structure (each verse or set of verses beginning with successive letters "
                    "of the Hebrew alphabet) is not mere literary artifice but theological statement. By "
                    "using every letter from aleph to tav, the poet exhausts the full range of grief -- "
                    "literally saying everything that can be said, from A to Z. The structure imposes "
                    "order on chaos: the destruction has shattered the world, but the poet's alphabet "
                    "holds. Chapter 3's triple acrostic (three verses per letter) intensifies the effect. "
                    "Chapter 5's abandonment of the acrostic form (22 verses, matching the alphabet's "
                    "count, but not actually acrostic) may represent the breakdown of even poetic order "
                    "under the weight of grief."
        }
    ]
}
