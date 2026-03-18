"""
era_75b_prayer.py -- From Ashes to Prayer (Lamentations 4-5)

The final two poems of Lamentations move from the horrors of siege and social
collapse (ch 4) to a raw, unresolved communal prayer (ch 5). Chapter 4 returns
to third-person description of the siege's devastation -- gold grown dim, sacred
stones scattered, compassionate mothers boiling their children, the anointed king
captured -- declaring Jerusalem's punishment greater than Sodom's. Chapter 5
breaks the acrostic pattern (22 verses but no alphabetic sequence) and addresses
YHWH directly in communal lament: 'Remember, O YHWH, what has befallen us.' The
book ends not with resolution but with an unresolved plea -- 'Restore us to
yourself, O YHWH, that we may be restored! Renew our days as of old -- unless
you have utterly rejected us.' Jewish liturgical practice repeats 5:21 after 5:22
so that the book ends on prayer rather than fear. The NT answers the haunting
question: God has not rejected his people (Rom 11:1-2), and the one on the
eternal throne will make all things new (Rev 21:5).
"""

CHAPTERS = [
    {
        "id": "lam-4",
        "ref": "Lamentations 4",
        "chapter_num": 1,
        "title": "Gold Grows Dim -- The Horrors of Siege and Judgment",
        "era": "lam_prayer",
        "type": "chapter",
        "themes": ["EXILE", "BLOOD", "KING"],

        "synopsis": "Chapter 4 returns to third-person description of the siege's horrors, with "
                    "particular focus on the reversal of the social order and the fulfillment of "
                    "covenant curses. The opening image sets the tone: 'How the gold has grown dim, "
                    "how the pure gold is changed!' (4:1). Sacred stones lie scattered at the head "
                    "of every street. The 'precious children of Zion, worth their weight in fine "
                    "gold' (4:2) are now regarded as clay pots. The famine descriptions are "
                    "harrowing: nursing mothers' breasts have dried up (4:3); children's tongues "
                    "cling to the roof of their mouths for thirst (4:4); those who once feasted on "
                    "delicacies perish in the streets (4:5). The horror reaches its peak in 4:10: "
                    "'The hands of compassionate women have boiled their own children; they became "
                    "their food during the destruction of the daughter of my people.' The poet "
                    "declares this punishment greater than Sodom's (4:6). Verses 12-16 distribute "
                    "blame: the prophets and priests 'shed the blood of the righteous in the midst "
                    "of her' (4:13). Verse 17 describes futile hope for Egyptian rescue ('a nation "
                    "that could not save'). The 'breath of our nostrils, the anointed of YHWH' -- "
                    "the Davidic king -- has been captured (4:20). The chapter ends with judgment "
                    "pronounced on Edom, who gloated over Jerusalem's fall.",

        "key_verse": {
            "ref": "Lamentations 4:6",
            "text": "For the chastisement of the daughter of my people has been greater than the punishment of Sodom, which was overthrown in a moment, and no hands were wrung for her.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ketem (fine gold -- now 'grown dim,' symbolizing the degradation of all that was precious, 4:1)",
            "avnei-qodesh (sacred stones -- scattered in the streets, possibly temple stones or precious children, 4:1)",
            "tannim (jackals -- even jackals nurse their young, but Zion's daughters are cruel, 4:3)",
            "mashiach YHWH (anointed of YHWH -- the Davidic king, captured in 'their pits,' 4:20)",
            "ruach appenu (breath of our nostrils -- the king as the life-breath of the nation, 4:20)"
        ],

        "ane_backdrop": "Siege warfare in the ANE was designed to produce exactly the horrors described "
                        "in Lamentations 4. Neo-Assyrian royal inscriptions boast of sieges that reduced "
                        "defenders to cannibalism. The Lachish Reliefs (701 BC, Sennacherib) depict the "
                        "suffering of a besieged Judean city in graphic detail. Babylonian siege tactics "
                        "at Jerusalem (588-586 BC) included constructing siege works, cutting off food "
                        "supplies, and waiting for starvation to do the work of conquest. The references "
                        "to hoping for 'a nation that could not save' (4:17) reflect the geopolitical "
                        "reality: Judah's alliance with Egypt (Pharaoh Hophra/Apries) proved worthless, "
                        "as Jeremiah had warned (Jer 37:7-8).",

        "second_temple": [
            {
                "source": "Josephus, Jewish War 6.193-213",
                "summary": "Josephus describes a woman named Mary who roasted and ate her own infant "
                           "during the Roman siege of Jerusalem in 70 AD, explicitly echoing the horror "
                           "of Lamentations 4:10.",
                "relevance": "The siege of 70 AD replayed the horrors of 586 BC, confirming the "
                             "pattern: covenant violation leads to covenant curse. Jesus wept over "
                             "Jerusalem (Luke 19:41-44) knowing this repetition was coming."
            },
            {
                "source": "4Q179 (4QLamentations)",
                "summary": "A Qumran text that expands on the themes of Lamentations with additional "
                           "lament compositions, demonstrating that the community continued to compose "
                           "in the lamentation tradition.",
                "relevance": "The Dead Sea Scrolls community saw themselves living in a time analogous "
                             "to the post-destruction period and used Lamentations as a model for "
                             "expressing their own sense of exile and longing for restoration."
            },
            {
                "source": "Obadiah 10-14",
                "summary": "Obadiah condemns Edom for gloating over Jerusalem's fall: 'You should not "
                           "have looked on the day of your brother in the day of his misfortune.'",
                "relevance": "The judgment on Edom in Lam 4:21-22 connects to the broader prophetic "
                             "tradition of condemning those who exploited Judah's disaster. Edom's "
                             "rejoicing over Jerusalem's fall brings its own covenant curse."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 28:53-57", "note": "The siege cannibalism of Lam 4:10 fulfills the covenant curse of Deut 28:53: 'You shall eat the fruit of your womb, the flesh of your sons and daughters.'", "type": "ot"},
            {"ref": "Genesis 19:24-25", "note": "The destruction of Sodom -- the benchmark for divine judgment -- is surpassed by Jerusalem's suffering (4:6). The covenant city's punishment exceeds Sodom's.", "type": "ot"},
            {"ref": "2 Kings 25:4-7", "note": "The capture of King Zedekiah fulfills Lam 4:20: 'The breath of our nostrils, the anointed of YHWH, was captured in their pits.'", "type": "ot"},
            {"ref": "Obadiah 10-14", "note": "Edom's gloating over Jerusalem's fall draws prophetic judgment. Lam 4:21-22 promises that Edom's own cup of judgment is coming.", "type": "ot"},
            {"ref": "Luke 19:41-44", "note": "Jesus weeps over Jerusalem knowing the horrors of 586 BC will be replicated in 70 AD. The pattern of covenant curse recurs when the Messiah is rejected.", "type": "nt"},
            {"ref": "Revelation 18:4-8", "note": "The call to 'come out of Babylon' and the declaration that her plagues will come in a single day echo the judgment language of Lam 4.", "type": "nt"}
        ],

        "divine_council_note": "[B] The capture of the mashiach YHWH (the anointed of YHWH, the Davidic "
                               "king, 4:20) is theologically significant for divine council theology. The "
                               "Davidic king was YHWH's earthly vice-regent, the human representative of "
                               "divine rule (Ps 2:6-7; 2 Sam 7:14). His capture means the visible "
                               "representation of YHWH's kingship has been removed from the earth. The "
                               "community had trusted that 'under his shadow we shall live among the "
                               "nations' (4:20b) -- but even the anointed king cannot protect when the "
                               "divine council has decreed judgment. The judgment on Edom (4:21-22) also "
                               "reflects council theology: the nations are accountable to YHWH's justice, "
                               "and those who exploited his judgment on Judah will themselves face judgment.",

        "sections": [
            {
                "heading": "Gold Grows Dim -- Reversal of Glory (Lam 4:1-6)",
                "body": "The fourth poem opens with another 'Eikhah!' cry: 'How the gold has grown "
                        "dim, how the pure gold is changed! The sacred stones (avnei-qodesh) lie "
                        "scattered at the head of every street' (4:1). Whether the 'sacred stones' "
                        "are the temple's precious stones or a metaphor for the children of Zion (4:2), "
                        "the image conveys total desecration -- the holy reduced to rubble in the "
                        "gutter. 'The precious children of Zion, worth their weight in fine gold, how "
                        "they are regarded as earthen pots, the work of a potter's hands!' (4:2). The "
                        "poet reaches for animal comparisons: even jackals (tannim) nurse their young, "
                        "but 'the daughter of my people has become cruel, like the ostriches in the "
                        "wilderness' (4:3) -- starvation has destroyed even maternal instinct. Children "
                        "beg for bread 'but no one gives to them' (4:4). Those who feasted on delicacies "
                        "now perish in the streets; those raised in scarlet embrace ash heaps (4:5). "
                        "Then the stunning comparison: 'The chastisement (avon) of the daughter of my "
                        "people has been greater than the punishment of Sodom, which was overthrown in "
                        "a moment' (4:6). Sodom at least died quickly. Jerusalem's suffering is slow, "
                        "grinding, and prolonged."
            },
            {
                "heading": "Famine's Horror -- Compassionate Women Boil Their Children (Lam 4:7-11)",
                "body": "The poem catalogues the physical devastation of famine on the population. "
                        "The nazirites (or princes), once 'purer than snow, whiter than milk, their "
                        "bodies more ruddy than coral' (4:7), are now 'blacker than soot; they are not "
                        "recognized in the streets; their skin has shriveled on their bones; it has "
                        "become as dry as wood' (4:8). The poet makes a grim calculation: 'Happier "
                        "were the victims of the sword than the victims of hunger, for these pine away, "
                        "stricken by lack of the fruits of the field' (4:9). Death by sword is quick; "
                        "death by starvation is slow agony. Then comes the chapter's most horrifying "
                        "verse: 'The hands of compassionate (rachamaniyyot) women have boiled their "
                        "own children; they became their food during the destruction of the daughter of "
                        "my people' (4:10). The word rachamaniyyot (compassionate) -- from the same "
                        "root as rachamim (mercies) in 3:22 -- makes the horror unbearable. These are "
                        "not monsters but mothers driven beyond humanity. 'YHWH gave full vent to his "
                        "wrath; he poured out his hot anger, and he kindled a fire in Zion that consumed "
                        "its foundations' (4:11). The fire that consumed the temple consumed the "
                        "foundations of the world as Israel knew it."
            },
            {
                "heading": "Blame and Futile Hope (Lam 4:12-20)",
                "body": "Verse 12 expresses the universal astonishment: 'The kings of the earth did "
                        "not believe, nor any of the inhabitants of the world, that foe or enemy could "
                        "enter the gates of Jerusalem.' Jerusalem was supposed to be inviolable -- the "
                        "Zion theology of Psalm 46 ('God is in the midst of her; she shall not be "
                        "moved') seemed to guarantee it. But the theological reality was more nuanced: "
                        "YHWH's protection was covenantal, not unconditional. Verses 13-16 identify the "
                        "guilty parties: prophets and priests 'who shed in the midst of her the blood "
                        "of the righteous' (4:13). They now wander blind in the streets, so defiled "
                        "with blood that people cry 'Unclean! Unclean!' (4:15) -- priestly purity "
                        "language turned against the priests themselves. Verse 17 describes the futile "
                        "hope for Egyptian rescue: 'Our eyes failed, ever watching vainly for help; in "
                        "our watching we watched for a nation which could not save.' This is exactly "
                        "what Jeremiah warned against (Jer 37:7-8). The section climaxes with the "
                        "capture of the king: 'The breath of our nostrils (ruach appenu), the anointed "
                        "of YHWH (mashiach YHWH), was captured in their pits, of whom we said, \"Under "
                        "his shadow we shall live among the nations\"' (4:20)."
            },
            {
                "heading": "Edom's Cup Is Coming (Lam 4:21-22)",
                "body": "The poem ends by addressing Edom (Judah's neighbor who exploited Jerusalem's "
                        "fall): 'Rejoice and be glad, O daughter of Edom, you who dwell in the land of "
                        "Uz; but to you also the cup shall pass; you shall become drunk and strip "
                        "yourself bare' (4:21). The irony is sharp -- the invitation to 'rejoice' is "
                        "actually a pronouncement of doom. The 'cup' is the cup of YHWH's wrath (cf. "
                        "Jer 25:15-29; Hab 2:16), which passes from nation to nation. Edom's gloating "
                        "(cf. Obadiah 10-14; Ps 137:7; Ezek 25:12-14; 35:1-15) was not merely "
                        "political opportunism but a violation of kinship bonds (Edom/Esau was Jacob's "
                        "brother). The final verse speaks to Zion: 'The punishment of your iniquity, "
                        "O daughter of Zion, is accomplished (tam); he will keep you in exile no "
                        "longer' (4:22a). This is the first hint of restoration -- the word tam "
                        "(completed/finished) suggests the judgment has a limit. YHWH's anger is not "
                        "infinite. But Edom's reckoning is just beginning: 'But your iniquity, O "
                        "daughter of Edom, he will punish; he will uncover your sins' (4:22b)."
            }
        ]
    },

    {
        "id": "lam-5",
        "ref": "Lamentations 5",
        "chapter_num": 2,
        "title": "Remember, O YHWH -- The Unresolved Prayer",
        "era": "lam_prayer",
        "type": "chapter",
        "themes": ["EXILE", "REMEMBER", "COV"],

        "synopsis": "The final chapter breaks the acrostic pattern -- it has 22 verses (matching the "
                    "number of letters in the Hebrew alphabet) but does not follow the alphabetic "
                    "sequence. This structural breakdown may itself be a theological statement: even "
                    "the poetic order that held through four chapters finally collapses under the "
                    "weight of grief. The poem is a communal prayer addressed directly to YHWH: "
                    "'Remember, O YHWH, what has befallen us; look, and see our disgrace!' (5:1). It "
                    "describes the ongoing conditions of life under foreign domination: loss of "
                    "inheritance (5:2), orphaned children (5:3), water and wood now commodities (5:4), "
                    "forced labor (5:5), dependence on Egypt and Assyria for bread (5:6). 'Our "
                    "fathers sinned, and are no more; and we bear their iniquities' (5:7). The temple "
                    "mount is desolate -- 'jackals prowl over it' (5:18). The theological climax "
                    "comes in 5:19-22: 'But you, O YHWH, reign forever; your throne endures to all "
                    "generations. Why do you forget us forever, why do you forsake us so long? Restore "
                    "us to yourself, O YHWH, that we may be restored! Renew our days as of old -- "
                    "unless you have utterly rejected us, and you remain exceedingly angry with us.' "
                    "The book ends on this unresolved note -- a plea, not a resolution. Jewish "
                    "liturgical practice repeats 5:21 after 5:22, so the book does not end on "
                    "rejection but on prayer.",

        "key_verse": {
            "ref": "Lamentations 5:21",
            "text": "Restore us to yourself, O LORD, that we may be restored! Renew our days as of old--",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "zekhor (remember! -- the imperative cry opening the chapter; to 'remember' in Hebrew is to act, not merely recall, 5:1)",
            "nachalatenu (our inheritance -- the land promised to Abraham, now occupied by strangers, 5:2)",
            "kiseh (throne -- YHWH's throne endures forever, 5:19, even when his earthly dwelling is destroyed)",
            "hashivenu (restore us/bring us back -- from shuv, the root of 'repentance/return,' 5:21)",
            "qedem (of old/ancient times -- 'renew our days as of old,' looking back to the covenant relationship, 5:21)"
        ],

        "ane_backdrop": "Communal lament prayers addressed to deity are well-attested across the ANE. "
                        "Mesopotamian 'ersemma' and 'balag' compositions are liturgical prayers appealing "
                        "to the gods for restoration after destruction. The Sumerian 'Letter-Prayer of "
                        "Ibbi-Sin' pleads for divine aid when the empire is collapsing. Lamentations 5 "
                        "follows this pattern but with a crucial difference: the prayer is addressed to "
                        "the very God who caused the destruction, not to a different deity who might "
                        "overrule the first. There is no appeal to a higher court -- YHWH is both judge "
                        "and the only possible savior. The unresolved ending is itself distinctive: most "
                        "ANE lament liturgies conclude with assured restoration. Lamentations refuses "
                        "this closure, leaving the community suspended between plea and silence.",

        "second_temple": [
            {
                "source": "Talmud Bavli, Megillah 31b",
                "summary": "The Talmud prescribes reading Lamentations on Tisha B'Av and specifies "
                           "that after reading 5:22, the reader returns to repeat 5:21, so the "
                           "book ends on hope rather than rejection.",
                "relevance": "Jewish liturgical practice addresses the book's unresolved ending by "
                             "repeating the penultimate verse. This is not a literary correction but "
                             "a theological act: the community refuses to let rejection be the final word."
            },
            {
                "source": "Psalm 80:3, 7, 19",
                "summary": "The refrain 'Restore us, O God; let your face shine, that we may be "
                           "saved!' uses the same root (shuv) as Lam 5:21's 'hashivenu.'",
                "relevance": "The prayer for restoration in Lam 5:21 connects to the broader psalmic "
                             "tradition of calling on YHWH to 'turn' (shuv) and restore his people. "
                             "The same root means both 'repent' and 'restore.'"
            },
            {
                "source": "Revelation 21:1-5",
                "summary": "God declares: 'Behold, I am making all things new... He will wipe away "
                           "every tear from their eyes, and death shall be no more.'",
                "relevance": "The unresolved prayer of Lam 5:21 ('Renew our days as of old') finds "
                             "its ultimate answer not in a return to the past but in the eschatological "
                             "renewal of all things. The tears that flow through Lamentations are "
                             "finally wiped away in the new creation."
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 44:23-26", "note": "'Awake! Why do you sleep, O Lord? Rouse yourself! Do not reject us forever!' -- the same plea for YHWH to 'wake up' and act that animates Lam 5.", "type": "ot"},
            {"ref": "Psalm 80:3, 7, 19", "note": "'Restore us, O God!' -- the same hashivenu prayer using the same root as Lam 5:21.", "type": "ot"},
            {"ref": "Isaiah 64:8-12", "note": "Another post-destruction prayer: 'Will you restrain yourself at these things, O YHWH? Will you keep silent and afflict us so terribly?' -- echoes Lam 5's unresolved ending.", "type": "ot"},
            {"ref": "Revelation 21:1-5", "note": "The prayer for renewal in Lam 5:21 finds its eschatological answer: 'Behold, I am making all things new.' The tears of Lamentations are wiped away.", "type": "nt"},
            {"ref": "Romans 11:1-2", "note": "Paul asks, 'Has God rejected his people?' and answers: 'By no means!' -- the NT answer to Lam 5:22's haunting question.", "type": "nt"}
        ],

        "divine_council_note": "[B] The final chapter's theology is profound for understanding the "
                               "divine council. Verse 19 affirms: 'But you, O YHWH, reign forever; your "
                               "throne (kiseh) endures to all generations.' The destruction of the "
                               "earthly temple has not destroyed the heavenly throne. YHWH's sovereignty "
                               "over the council is undiminished even when his earthly dwelling lies in "
                               "ruins. The question 'Why do you forget us forever?' (5:20) is not a "
                               "denial of divine sovereignty but an appeal to it -- the community asks "
                               "the sovereign king to remember his subjects. The prayer 'Restore us to "
                               "yourself' (hashivenu, 5:21) is ultimately a prayer for the restoration "
                               "of the covenant relationship -- for the divine king to turn toward his "
                               "people again. The unresolved ending leaves the council's next decree "
                               "unspoken: will YHWH restore? The prophets (Jeremiah 31, Ezekiel 37, "
                               "Isaiah 40-66) answer yes -- but Lamentations, in its integrity, does "
                               "not presume the answer.",

        "sections": [
            {
                "heading": "Remember, O YHWH -- The Opening Plea (Lam 5:1-10)",
                "body": "The chapter opens with a direct imperative to YHWH: 'Remember (zekhor), O "
                        "YHWH, what has befallen us; look (habbit), and see (re'eh) our disgrace!' "
                        "(5:1). Three verbs -- remember, look, see -- demand YHWH's attention. In "
                        "Hebrew, 'remembering' is not mere mental recall but active intervention: when "
                        "God 'remembers' Noah (Gen 8:1) or Rachel (Gen 30:22), he acts. The community "
                        "catalogues its losses: 'Our inheritance (nachalatenu) has been turned over to "
                        "strangers, our homes to foreigners' (5:2). The nahalah -- the land promised to "
                        "Abraham, divided by lot under Joshua -- is in alien hands. 'We have become "
                        "orphans, fatherless; our mothers are like widows' (5:3). The entire community "
                        "is socially unprotected. Basic necessities are now purchased: 'We must pay for "
                        "the water we drink; the wood we get must be bought' (5:4). They are hunted, "
                        "exhausted, forced to submit to Egypt and Assyria (i.e., foreign powers) 'to "
                        "get enough bread' (5:6). Verse 7 raises the question of intergenerational "
                        "justice: 'Our fathers sinned, and are no more; and we bear their iniquities.' "
                        "This is not a denial of their own guilt (cf. 5:16) but a recognition that the "
                        "accumulated weight of generations of covenant violation has fallen on this "
                        "generation. Famine has ravaged their bodies: 'Our skin is hot as an oven with "
                        "the burning heat of famine' (5:10)."
            },
            {
                "heading": "The Social Order Shattered (Lam 5:11-18)",
                "body": "The middle section describes the comprehensive destruction of social order. "
                        "'Women are raped in Zion, young women in the towns of Judah' (5:11). 'Princes "
                        "are hung up by their hands; no respect is shown to the elders' (5:12). 'Young "
                        "men are compelled to grind at the mill, and boys stagger under loads of wood' "
                        "(5:13). 'The old men have left the city gate; the young men have ceased their "
                        "music' (5:14). Every social structure -- sexual protection, political authority, "
                        "generational respect, economic productivity, legal process, cultural "
                        "celebration -- has collapsed. 'The joy of our hearts has ceased; our dancing "
                        "has been turned to mourning' (5:15). Then the confession: 'The crown has "
                        "fallen from our head; woe (oi) to us, for we have sinned (chatanu)!' (5:16). "
                        "The 'crown' may be the monarchy, the temple, or national glory -- all have "
                        "fallen. The cause is acknowledged: 'we have sinned.' Verses 17-18 describe "
                        "the emotional and physical devastation: 'Because of this our heart has become "
                        "sick, because of these things our eyes have grown dim' (5:17). And the temple "
                        "mount: 'Because of Mount Zion which lies desolate; jackals prowl over it' "
                        "(5:18). The image of wild animals on the temple mount captures the depth of "
                        "desolation."
            },
            {
                "heading": "But You, O YHWH -- The Eternal Throne and the Unresolved Plea (Lam 5:19-22)",
                "body": "The final four verses are the theological climax of the entire book. Verse 19 "
                        "asserts what nothing can shake: 'But you, O YHWH, reign forever; your throne "
                        "(kiseh) endures to all generations.' The earthly temple is destroyed, but the "
                        "heavenly throne is unmoved. The Davidic king is captured, but the divine king "
                        "reigns. This is not pious platitude but theological bedrock -- the same "
                        "affirmation that opens Psalm 93 and closes Psalm 146. Then comes the raw "
                        "question: 'Why do you forget us forever, why do you forsake us for so many "
                        "days?' (5:20). The tension between 5:19 (you reign forever) and 5:20 (why do "
                        "you forget us?) is the tension of faith in the darkness. The prayer of 5:21 "
                        "is the book's most hopeful moment: 'Restore us to yourself (hashivenu elekha), "
                        "O YHWH, that we may be restored (venashuvah)! Renew (chadesh) our days as of "
                        "old (ke-qedem).' The wordplay on shuv (return/restore) is profound: the "
                        "community asks YHWH to 'turn us back' so that they may 'turn back.' Repentance "
                        "and restoration are YHWH's work before they are ours. Then the haunting final "
                        "verse: 'Unless (ki im) you have utterly rejected us (ma'os me'astanu), and "
                        "you remain exceedingly angry (qatsafta) with us' (5:22). The book ends with "
                        "a conditional clause of dread. Has YHWH utterly rejected? Is his anger "
                        "permanent? The book does not answer. In Jewish liturgical practice, verse 21 "
                        "is repeated after verse 22, so the reading ends on prayer rather than fear. "
                        "The NT provides the definitive answer: God has not rejected his people (Rom "
                        "11:1-2), and the one who sits on the eternal throne will make all things new "
                        "(Rev 21:5)."
            }
        ]
    }
]
