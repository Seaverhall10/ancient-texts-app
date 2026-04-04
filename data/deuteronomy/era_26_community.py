"""
era_26_community.py — Community Laws (Deuteronomy 19-26)

The detailed stipulations governing community life: justice, warfare, family,
social ethics, and the firstfruits confession. These laws shape Israel's
daily existence as YHWH's covenant people, distinct from the nations governed
by the allotted 'elohim.
"""

CHAPTERS = [
    {
        "id": "deut-19",
        "ref": "Deuteronomy 19",
        "chapter_num": 19,
        "title": "Cities of Refuge and the Justice of Witnesses",
        "era": "community",
        "type": "chapter",
        "themes": ["LAW", "LAND"],

        "synopsis": "Deuteronomy 19 establishes the cities of refuge system and regulates judicial "
                    "evidence standards. Three cities are to be set apart in the Promised Land where "
                    "a person who kills unintentionally can flee from the 'avenger of blood' (go'el "
                    "haddam, 19:6) — the kinsman obligated to avenge a murder. The distinction between "
                    "accidental homicide and premeditated murder is carefully drawn (19:4-6 vs. 19:11-13). "
                    "If Israel obeys and the territory expands, three additional cities may be added "
                    "(19:8-9). The chapter also addresses boundary markers — 'You shall not move your "
                    "neighbor's landmark' (19:14) — which in the ANE carried religious as well as legal "
                    "significance, as boundaries were considered divinely established. The witness "
                    "regulations require two or three witnesses for any criminal charge (19:15) and "
                    "prescribe the lex talionis for false witnesses: 'Then you shall do to him as he "
                    "had meant to do to his brother... eye for eye, tooth for tooth' (19:19-21). "
                    "These provisions create a justice system that protects both the innocent victim "
                    "and the falsely accused.",

        "key_verse": {
            "ref": "Deuteronomy 19:15",
            "text": "A single witness shall not suffice against a person for any crime or for any wrong in connection with any offense that he has committed. Only on the evidence of two witnesses or of three witnesses shall a charge be established.",
            "translation": "ESV"
        },

        "original_terms": ["ir_miqlat", "goel_haddam", "rotseach", "gevul", "ed", "lex_talionis", "ayin_tachat_ayin"],

        "hebrew_glossary": {
            "ir_miqlat": "City of refuge (a designated safe city where someone who kills accidentally can flee from blood vengeance — a theological institution that reflects YHWH's justice: he distinguishes between intent and accident, unlike the capricious gods of the ANE)",
            "goel_haddam": "Avenger of blood / kinsman-redeemer of blood (the nearest male relative obligated by honor and law to avenge a murder — the goel institution is broader than vengeance; the goel also redeems property, marries widows, and restores family honor; YHWH himself is called Israel's goel)",
            "lex_talionis": "Law of retaliation (Latin: 'eye for eye, tooth for tooth' — NOT a mandate for revenge but a LIMIT on punishment: the penalty must be proportional to the crime, no more; it prevents escalation and blood feuds)"
        },

        "ane_backdrop": "The cities of refuge concept has parallels in ANE asylum traditions. "
                        "Mesopotamian temples and Egyptian sanctuaries offered asylum to fugitives, "
                        "though the specific distinction between accidental and intentional homicide "
                        "is unique to Israelite law. The lex talionis ('eye for eye') appears in the "
                        "Code of Hammurabi (Laws 196-201, ~1750 BC) but applies only within the same "
                        "social class. Deuteronomy applies it universally, and specifically to false "
                        "witnesses — a distinctive application. Boundary stones (kudurru) in "
                        "Mesopotamia were inscribed with curses against anyone who moved them and "
                        "were protected by divine sanction.",

        "second_temple": [
            {
                "source": "Mishnah Makkot 2:1-8",
                "summary": "The Mishnah extensively develops the cities of refuge legislation, "
                           "specifying road maintenance, signage, and the rights of the manslayer.",
                "relevance": "Shows that the Deut 19 refuge system was taken with full legal "
                             "seriousness in rabbinic tradition."
            },
            {
                "source": "Philo, On the Special Laws 3.115-123",
                "summary": "Philo provides philosophical justification for the cities of refuge, "
                           "arguing that they reflect the Stoic principle of proportional justice.",
                "relevance": "Illustrates how Hellenistic Judaism rationalized Deut 19 for a "
                             "philosophical audience."
            }
        ],

        "cross_refs": [
            {"ref": "Numbers 35:9-34", "note": "The parallel cities of refuge legislation in Numbers, with additional details", "type": "ot"},
            {"ref": "Joshua 20:1-9", "note": "The establishment of the actual cities of refuge after the conquest", "type": "ot"},
            {"ref": "Matthew 18:16", "note": "Jesus applies the two-witness rule: 'that every charge may be established by the evidence of two or three witnesses'", "type": "nt"},
            {"ref": "2 Corinthians 13:1", "note": "Paul: 'Every charge must be established by the evidence of two or three witnesses' — citing Deut 19:15", "type": "nt"},
            {"ref": "Hebrews 6:18", "note": "Christ as the ultimate 'city of refuge' for those who have 'fled for refuge to lay hold of the hope set before us'", "type": "nt"},
            {"ref": "Proverbs 22:28", "note": "'Do not move the ancient landmark that your fathers have set' — echoing Deut 19:14", "type": "ot"}
        ],

        "divine_council_note": "The cities of refuge system reflects YHWH's character as a just God "
                               "who distinguishes between intentional and unintentional harm — a "
                               "contrast to the capricious justice attributed to the gods of the ANE "
                               "nations. In Psalm 82, YHWH condemns the allotted 'elohim precisely "
                               "for their failure to maintain justice: 'How long will you judge unjustly "
                               "and show partiality to the wicked?' (Ps 82:2). The Deuteronomic justice "
                               "system is what the 'elohim should have established for their nations but "
                               "failed to — Israel models the divine council ideal of justice under "
                               "YHWH's direct governance.",

        "sections": [
            {
                "heading": "Cities of Refuge in the Promised Land (19:1-7)",
                "body": "Three cities are to be set apart in the land 'that the LORD your God is "
                        "giving you to possess' (19:2). The purpose: 'that any manslayer may flee to "
                        "them' (19:3). Moses provides a specific example: 'as when someone goes into "
                        "the forest with his neighbor to cut wood, and his hand swings the axe to cut "
                        "down a tree, and the head slips from the handle and strikes his neighbor so "
                        "that he dies — he may flee to one of these cities and live' (19:5). Without "
                        "the refuge city, the go'el haddam ('avenger of blood') — the dead person's "
                        "nearest kinsman, obligated by honor to avenge the death — might 'pursue the "
                        "manslayer in hot anger and overtake him' (19:6). The roads to the refuge "
                        "cities must be prepared and the territory divided into three districts to "
                        "minimize travel distance (19:3). This is practical theology: justice requires "
                        "infrastructure."
            },
            {
                "heading": "Additional Cities and the Exclusion of Murderers (19:8-13)",
                "body": "If YHWH enlarges Israel's territory (fulfilling the full Abrahamic land "
                        "promise), three more cities may be added (19:8-9). But deliberate murderers "
                        "receive no asylum: 'If anyone hates his neighbor and lies in wait for him "
                        "and attacks him and strikes him fatally... the elders of his city shall send "
                        "and take him from there, and hand him over to the avenger of blood, so that "
                        "he may die' (19:11-12). The purpose: 'You shall purge the guilt of innocent "
                        "blood from Israel' (19:13). The verb 'purge' (bi'er) is cultic — innocent "
                        "blood pollutes the land covenantally. Justice is not merely social but "
                        "spiritual: unresolved bloodguilt contaminates the covenant territory."
            },
            {
                "heading": "Boundary Markers (19:14)",
                "body": "A single verse with enormous significance: 'You shall not move your neighbor's "
                        "landmark, which the men of old have set, in the inheritance that you will hold' "
                        "(19:14). In the ANE, boundary stones were sacred. Mesopotamian kudurru stones "
                        "were inscribed with divine curses. In Israel, land boundaries were considered "
                        "YHWH's allocation — to move them was to steal from the divine inheritance "
                        "system. This connects to Deut 32:8-9: God set the boundaries of the nations; "
                        "moving boundaries defies divine ordering."
            },
            {
                "heading": "Two Witnesses and the False Witness Law (19:15-21)",
                "body": "The evidence standard: 'A single witness shall not suffice against a person "
                        "for any crime' (19:15). The procedure for a disputed case: both parties 'shall "
                        "appear before the LORD, before the priests and the judges who are in office' "
                        "(19:17). If a witness is found false, 'then you shall do to him as he had "
                        "meant to do to his brother' (19:19). The lex talionis follows: 'life for life, "
                        "eye for eye, tooth for tooth, hand for hand, foot for foot' (19:21). This is "
                        "not savage retribution but proportional justice — the punishment must match, "
                        "not exceed, the crime. It limits vengeance rather than promoting it. Jesus "
                        "addresses this in the Sermon on the Mount (Matt 5:38-42), not abolishing "
                        "the principle of justice but transcending it with the ethic of non-retaliation."
            }
        ]
    },

    {
        "id": "deut-20",
        "ref": "Deuteronomy 20",
        "chapter_num": 20,
        "title": "Laws of Holy War — Trust, Exemptions, and the Ban",
        "era": "community",
        "type": "chapter",
        "themes": ["LAW", "NATIONS", "LAND", "HOLY"],

        "synopsis": "Deuteronomy 20 provides the most comprehensive warfare legislation in the Torah. "
                    "Before battle, the priest addresses the army: 'Do not let your heart faint. Do "
                    "not fear or panic or be in dread of them, for the LORD your God is he who goes "
                    "with you to fight for you' (20:3-4). Four categories of soldiers are exempted: "
                    "those who built a new house, planted a new vineyard, betrothed a wife, or are "
                    "fearful (20:5-8). For distant cities, Israel must offer peace terms first; if "
                    "rejected, males are killed but women, children, and livestock are spared (20:10-15). "
                    "For the seven Canaanite nations within the Promised Land, however, the cherem "
                    "is total: 'you shall save alive nothing that breathes' (20:16). The reason is "
                    "theological, not ethnic: 'that they may not teach you to do according to all "
                    "their abominable practices that they have done for their gods' (20:18). The "
                    "chapter closes with an unexpected ecological provision: fruit trees must not be "
                    "destroyed during sieges (20:19-20).",

        "key_verse": {
            "ref": "Deuteronomy 20:4",
            "text": "For the LORD your God is he who goes with you to fight for you against your enemies, to give you the victory.",
            "translation": "ESV"
        },

        "original_terms": ["milchamah", "kohen", "shoter", "cherem", "shalom", "mas", "ets_maakhal"],

        "hebrew_glossary": {
            "milchamah": "War / battle (in Deuteronomy, warfare is theological, not merely military — YHWH 'goes with you to fight for you'; Israel's battles are extensions of the divine council's purposes against the allotted 'elohim's territories)",
            "cherem": "Devoted destruction / the ban (total consecration of conquered populations to YHWH — applied only to the Canaanite nations within the Promised Land, not to distant cities; the distinction reflects the spiritual threat level of the allotted 'elohim's worship systems nearby vs. far away)",
            "shalom": "Peace (the peace offer to distant cities reflects YHWH's preference for reconciliation over destruction — even in warfare, Israel must first offer terms; only after rejection does military action proceed)",
            "mas": "Forced labor / tribute (the status of a distant city that accepts peace — its inhabitants become laborers, not destroyed; this is the standard ANE vassal arrangement)",
            "ets_maakhal": "Fruit tree (the tree preservation law: 'Are the trees in the field human, that they should be besieged by you?' — remarkable ecological sensitivity within warfare legislation; the land is YHWH's gift and must be treated with respect even during conquest)"
        },

        "ane_backdrop": "Warfare legislation is attested across ANE law codes but nowhere with the "
                        "theological framing of Deuteronomy 20. The exemptions for builders, planters, "
                        "and the betrothed have partial parallels in Hittite military texts, where "
                        "certain categories of men could be excused from campaign duty. The cherem "
                        "('devotion to destruction') parallels the Moabite practice attested on the "
                        "Mesha Stele. The tree-preservation law (20:19-20) is unique — most ANE armies "
                        "practiced scorched-earth warfare. Assyrian palace reliefs routinely depict "
                        "soldiers cutting down the enemy's orchards.",

        "second_temple": [
            {
                "source": "1QM (War Scroll)",
                "summary": "The War Scroll reinterprets Deut 20 for an eschatological holy war "
                           "between the sons of light and the sons of darkness.",
                "relevance": "Shows Qumran's belief that Deut 20's warfare theology would be "
                             "fulfilled in a final cosmic battle.",
                "canon": False
            },
            {
                "source": "Josephus, Antiquities 4.8.41-42",
                "summary": "Josephus recounts the warfare laws with emphasis on the offer of "
                           "peace terms, presenting Israel as more humane than surrounding nations.",
                "relevance": "Apologetic use of Deut 20 to defend Israelite warfare practices "
                             "to a Greco-Roman audience."
            }
        ],

        "cross_refs": [
            {"ref": "Joshua 6:17-21", "note": "The cherem applied at Jericho — the first fulfillment of Deut 20:16-18", "type": "ot"},
            {"ref": "Joshua 9:3-27", "note": "The Gibeonite deception — exploiting the peace offer provision of Deut 20:10-11", "type": "ot"},
            {"ref": "2 Corinthians 10:3-5", "note": "'The weapons of our warfare are not of the flesh' — the NT spiritualization of holy war", "type": "nt"},
            {"ref": "Ephesians 6:10-18", "note": "The 'armor of God' — spiritual warfare replacing physical holy war", "type": "nt"},
            {"ref": "Psalm 20:7", "note": "'Some trust in chariots and some in horses, but we trust in the name of the LORD our God'", "type": "ot"},
            {"ref": "Isaiah 2:4", "note": "'They shall beat their swords into plowshares' — the eschatological end of warfare", "type": "ot"}
        ],

        "divine_council_note": "Deuteronomy 20's warfare theology presupposes the divine council "
                               "worldview. The priest's declaration that 'the LORD your God goes with "
                               "you' (20:4) asserts YHWH's presence on the battlefield against nations "
                               "whose allotted 'elohim also have territorial claims. The cherem against "
                               "Canaanite nations (20:16-18) is spiritual warfare: these nations' "
                               "worship practices — empowered by their allotted 'elohim — must be "
                               "completely eradicated from YHWH's territory. The distinction between "
                               "distant cities (which can be offered peace) and Canaanite cities "
                               "(which must be destroyed) reflects the distinction between nations "
                               "under their allotted 'elohim at a distance and nations whose "
                               "'elohim-worship directly contaminates the land YHWH claims as his own.",

        "sections": [
            {
                "heading": "The Priest's Battle Address (20:1-4)",
                "body": "Before engagement, the priest addresses the army with covenant assurance: "
                        "'Hear, O Israel: today you are drawing near for battle against your enemies. "
                        "Let not your heart faint. Do not fear or panic or be in dread of them, for "
                        "the LORD your God is he who goes with you' (20:3-4). Four negative commands "
                        "(do not let your heart faint, do not fear, do not panic, do not dread) "
                        "address the full spectrum of battlefield terror. The antidote is theological: "
                        "YHWH fights for you. This is not motivational rhetoric but covenant reality — "
                        "the Great King himself enters battle alongside his vassal."
            },
            {
                "heading": "Military Exemptions (20:5-9)",
                "body": "Four categories of soldiers may go home: (1) the one who has built a new "
                        "house and not dedicated it, (2) the one who has planted a vineyard and not "
                        "enjoyed its fruit, (3) the one who is betrothed and not yet married, and "
                        "(4) the one who is afraid. The first three share a logic: the person should "
                        "not die without experiencing the fruit of their labor. The fourth exemption "
                        "is pragmatic: fear is contagious and demoralizes the entire army. These "
                        "exemptions reveal Deuteronomy's humane priorities — human fulfillment and "
                        "covenant joy matter more than military manpower."
            },
            {
                "heading": "Rules for Distant vs. Near Cities (20:10-18)",
                "body": "For cities 'very far from you' (20:15), Israel must first offer peace "
                        "(shalom). If accepted, the city becomes a tributary (forced labor, mas). If "
                        "rejected, the males are killed but women, children, livestock, and spoil are "
                        "kept (20:11-14). For the seven nations within the land, no quarter: 'you shall "
                        "save alive nothing that breathes' (20:16). The distinction is theological: "
                        "distant nations pose no immediate threat to covenant fidelity; Canaanite "
                        "nations do. The rationale: 'that they may not teach you to do according to "
                        "all their abominable practices' (20:18). The cherem is spiritual quarantine."
            },
            {
                "heading": "The Tree Preservation Law (20:19-20)",
                "body": "An ecological provision within military law: 'When you besiege a city for a "
                        "long time... you shall not destroy its trees by wielding an axe against them. "
                        "You may eat from them, but you shall not cut them down. Are the trees in the "
                        "field human, that they should be besieged by you?' (20:19). Only non-fruit "
                        "trees may be used for siege works. This is remarkable — environmental "
                        "sensitivity in the midst of warfare legislation. The land is YHWH's gift, "
                        "and even enemy territory's fruit trees participate in divine blessing."
            }
        ]
    },

    {
        "id": "deut-21",
        "ref": "Deuteronomy 21",
        "chapter_num": 21,
        "title": "Unsolved Murder, War Captives, and Family Law",
        "era": "community",
        "type": "chapter",
        "themes": ["LAW", "BLOOD", "LAND"],

        "synopsis": "Deuteronomy 21 addresses three challenging social situations. First, the ritual "
                    "for an unsolved murder: the nearest city's elders must perform a heifer-breaking "
                    "ceremony to purge bloodguilt from the land (21:1-9). Second, the rights of female "
                    "war captives: a man who desires a captive woman must allow her a month to mourn "
                    "before marriage, and if he later divorces her, she goes free — 'you shall not "
                    "sell her for money' (21:10-14). Third, laws protecting the firstborn's inheritance "
                    "rights even when the father favors a different wife (21:15-17), and the procedure "
                    "for a rebellious son (21:18-21). The chapter closes with the hanging law: 'if a "
                    "man has committed a crime punishable by death and he is put to death, and you "
                    "hang him on a tree, his body shall not remain overnight on the tree... for a "
                    "hanged man is cursed by God' (21:22-23) — the verse Paul applies to Christ's "
                    "crucifixion in Galatians 3:13.",

        "key_verse": {
            "ref": "Deuteronomy 21:22-23",
            "text": "And if a man has committed a crime punishable by death and he is put to death, and you hang him on a tree, his body shall not remain overnight on the tree, but you shall bury him the same day, for a hanged man is cursed by God. You shall not defile your land that the LORD your God is giving you for an inheritance.",
            "translation": "ESV"
        },

        "original_terms": ["eglah_arufah", "chalal", "bekhor", "ben_sorer_umoreh", "qelalat_elohim", "talah_al_ets"],

        "hebrew_glossary": {
            "eglah_arufah": "Broken-necked heifer (the animal used to purge bloodguilt from an unsolved murder — a heifer that has never been worked, killed in an uncultivated valley with running water; the untouched elements symbolize purity absorbing the pollution of innocent blood)",
            "qelalat_elohim": "Cursed by God / curse of God (the status of a body hung on a tree — the Hebrew is deliberately ambiguous: 'cursed by God,' 'an affront to God,' or 'a divine curse'; Paul takes it as 'cursed by God' and applies it to Christ on the cross in Galatians 3:13)",
            "talah_al_ets": "Hung on a tree (a criminal's body displayed after execution — must be removed before nightfall to prevent land defilement; this phrase became christologically decisive: Peter says Jesus was 'hung on a tree' (Acts 5:30; 10:39), and Paul says Christ 'became a curse for us' (Gal 3:13))",
            "bekhor": "Firstborn (the firstborn son's right to a double inheritance portion — protected by law even when the father favors a different wife's son; the firstborn principle runs through all of scripture from Esau/Jacob to Christ as 'firstborn over all creation,' Col 1:15)",
            "ben_sorer_umoreh": "Stubborn and rebellious son (a legal designation for incorrigible covenant rebellion in a son — not youthful misbehavior but persistent refusal to submit to parental and communal authority; the verbs are the same used for Israel's rebellion against YHWH)"
        },

        "ane_backdrop": "The heifer ritual (21:1-9) has parallels in Hittite purification rituals "
                        "where an animal is killed to absorb impurity from the community. The "
                        "captive-bride regulation (21:10-14) represents a significant improvement "
                        "over ANE norms, where female captives had virtually no rights. The "
                        "firstborn inheritance protection (21:15-17) parallels Nuzi and Middle "
                        "Assyrian laws on patrimony. The hanging/exposure of executed criminals "
                        "was practiced throughout the ANE (Assyrian and Egyptian records show "
                        "bodies displayed on city walls), but Deuteronomy uniquely limits the "
                        "exposure to prevent land defilement.",

        "second_temple": [
            {
                "source": "11QTemple (Temple Scroll) 64:6-13",
                "summary": "The Temple Scroll interprets Deut 21:22-23 as applying to those "
                           "who betray the nation — crucifixion is mentioned as a specific "
                           "form of the 'hanging on a tree.'",
                "relevance": "Provides pre-Christian evidence that Deut 21:22-23 was applied "
                             "to crucifixion specifically, not just post-mortem display."
            },
            {
                "source": "Galatians 3:13",
                "summary": "Paul: 'Christ redeemed us from the curse of the law by becoming a "
                           "curse for us — for it is written, \"Cursed is everyone who is hanged "
                           "on a tree.\"'",
                "relevance": "The most theologically consequential NT use of Deut 21:23 — Christ "
                             "bears the covenant curse on the cross."
            }
        ],

        "cross_refs": [
            {"ref": "Galatians 3:13", "note": "Paul applies Deut 21:23 to Christ's crucifixion: 'Cursed is everyone who is hanged on a tree'", "type": "nt"},
            {"ref": "Joshua 8:29", "note": "Joshua hangs the king of Ai on a tree and takes him down at sunset — obeying Deut 21:23", "type": "ot"},
            {"ref": "John 19:31", "note": "The Jews ask Pilate to remove the bodies before sunset — observing Deut 21:23", "type": "nt"},
            {"ref": "1 Peter 2:24", "note": "'He himself bore our sins in his body on the tree' — Deut 21:23 language", "type": "nt"},
            {"ref": "Genesis 25:29-34", "note": "Esau sold his birthright — the firstborn right Deut 21:15-17 protects", "type": "ot"}
        ],

        "divine_council_note": "Deuteronomy 21:23 — 'a hanged man is cursed by God (qelalat elohim)' — "
                               "has profound divine council implications when applied to Christ's "
                               "crucifixion. Paul's interpretation in Galatians 3:13 means that Christ "
                               "absorbed the full covenant curse — the 'curse' of Deuteronomy 27-28 — "
                               "on the cross. In the divine council framework, this is the cosmic turning "
                               "point: the curse that bound Israel to judgment under the 'elohim is borne "
                               "by Christ, and the blessing promised to Abraham flows to the nations "
                               "(Gal 3:14). The cross is the divine council event that reverses the "
                               "Deuteronomy 32 allotment — the nations are no longer bound to their "
                               "allotted 'elohim but can come under YHWH's direct rule through Christ.",

        "sections": [
            {
                "heading": "The Unsolved Murder Ritual (21:1-9)",
                "body": "When a murder victim is found in open country and the killer is unknown, the "
                        "elders of the nearest city must perform a specific ritual: a heifer that has "
                        "never been worked or yoked is taken to a valley with running water, its neck "
                        "is broken, and the elders wash their hands over it, declaring: 'Our hands did "
                        "not shed this blood, nor did our eyes see it shed. Accept atonement, O LORD, "
                        "for your people Israel' (21:7-8). The ritual purges bloodguilt from the "
                        "community. The unworn heifer and the uncultivated valley symbolize untouched "
                        "purity — the fresh elements absorb the pollution of innocent blood."
            },
            {
                "heading": "Rights of the Female War Captive (21:10-14)",
                "body": "If a soldier desires a female captive, she must be brought into his home, "
                        "allowed to shave her head, trim her nails, and change her clothes (mourning "
                        "rituals for her former life), then mourn her father and mother for a full "
                        "month (21:12-13). Only then may the marriage proceed. If he later finds 'no "
                        "delight in her,' she goes free: 'You shall not sell her for money. You shall "
                        "not treat her as a slave, since you have humiliated her' (21:14). While "
                        "deeply troubling by modern standards, this legislation represents significant "
                        "protections for women in the ANE context, where captives had no rights whatsoever."
            },
            {
                "heading": "Firstborn Rights and the Rebellious Son (21:15-21)",
                "body": "A man with two wives may not disinherit the firstborn son of the unloved wife "
                        "in favor of the loved wife's son (21:15-17). The firstborn's double portion "
                        "is a right, not a gift. The rebellious son law (21:18-21) addresses a son who "
                        "is 'stubborn and rebellious' and 'will not obey' — the parents must bring him "
                        "before the city elders. If convicted, 'all the men of the city shall stone him "
                        "to death' (21:21). This is not about youthful misbehavior but about incorrigible "
                        "covenant rebellion — the same verb 'rebellious' (moreh) used of Israel's "
                        "rebellion against YHWH. The law limits parental authority (the case must go to "
                        "the elders) while protecting community integrity."
            },
            {
                "heading": "The Curse of the Hanged Man (21:22-23)",
                "body": "A criminal executed and hung on a tree (for public display) must be buried "
                        "the same day: 'his body shall not remain overnight on the tree, but you shall "
                        "bury him the same day, for a hanged man is cursed by God (qelalat elohim)' "
                        "(21:23). The Hebrew is ambiguous: qelalat elohim could mean 'cursed by God' "
                        "(God has cursed this person), 'an affront to God' (the exposed body dishonors "
                        "the image of God), or 'cursed of God' (divine curse rests on the exposed). "
                        "Paul takes the first reading in Galatians 3:13: Christ, hung on the 'tree' "
                        "of the cross, became the curse-bearer — absorbing the covenant curse so that "
                        "'the blessing of Abraham might come to the Gentiles' (Gal 3:14). This single "
                        "verse connects Deuteronomy's covenant curse to the cross of Christ."
            }
        ]
    },

    {
        "id": "deut-22",
        "ref": "Deuteronomy 22",
        "chapter_num": 22,
        "title": "Neighborly Duty, Distinctive Identity, and Sexual Ethics",
        "era": "community",
        "type": "chapter",
        "themes": ["LAW", "HOLY"],

        "synopsis": "Deuteronomy 22 collects diverse community laws united by the theme of maintaining "
                    "covenant order. The chapter opens with obligations to return lost property and "
                    "assist a neighbor's fallen animal (22:1-4) — covenant community requires active "
                    "care for one another's welfare. Cross-dressing is prohibited (22:5), as is taking "
                    "a mother bird with her eggs (22:6-7). Building parapets on flat roofs prevents "
                    "liability for accidental death (22:8). Several mixing prohibitions follow: no "
                    "sowing two kinds of seed together, no plowing with an ox and donkey yoked "
                    "together, no wearing cloth of mixed wool and linen (22:9-11). These 'mixture' "
                    "laws maintain the category distinctions established in creation (Gen 1, 'according "
                    "to their kinds'). The final section (22:13-30) addresses sexual ethics: false "
                    "accusations of a bride's virginity, premarital sex, adultery, rape within the "
                    "city vs. in the open country, and violations of betrothal. These laws protect "
                    "women's honor within the patriarchal framework while maintaining sexual boundaries "
                    "as covenant requirements.",

        "key_verse": {
            "ref": "Deuteronomy 22:8",
            "text": "When you build a new house, you shall make a parapet for your roof, that you may not bring the guilt of blood upon your house, if anyone should fall from it.",
            "translation": "ESV"
        },

        "original_terms": ["shilu'ach_haqen", "kilayim", "sha'atnez", "betulah", "na'arah", "naaph", "ones"],

        "hebrew_glossary": {
            "kilayim": "Mixture / forbidden crossbreeding (the prohibition of mixing different kinds — seeds, plowing animals, fabrics; these maintain the category distinctions God established at creation in Genesis 1; in the divine council framework, the Watchers' sin was crossing the ultimate boundary between divine and human kinds)",
            "sha'atnez": "Mixed wool and linen (a specific fabric mixture forbidden to common Israelites — priestly garments DID combine these materials, suggesting the prohibition maintains the distinction between priestly and common status; only those consecrated to direct divine service may blur this boundary)",
            "betulah": "Virgin (a young woman who has not had sexual intercourse — virginity at marriage was a family honor issue in the patrilineal system; the laws of 22:13-21 protect women against false accusations as much as they enforce the standard)",
            "hit'allem": "Hide yourself / ignore (the verb used in 22:1,4 for pretending not to see a neighbor's lost property or fallen animal — covenant community prohibits looking away; indifference to a brother's need is a covenant violation)"
        },

        "ane_backdrop": "The lost property return laws have parallels in the Code of Hammurabi "
                        "(Laws 9-13) and the Laws of Eshnunna. The rooftop parapet law reflects "
                        "the flat-roofed architecture of the Levant, where rooftops served as living "
                        "space. The mixing prohibitions (kilayim) may counter the blurring of "
                        "categories associated with Canaanite fertility magic, where mixing was "
                        "thought to enhance productivity. The sexual ethics reflect the patrilineal "
                        "kinship system of the ANE, where a woman's sexual status directly affected "
                        "inheritance, lineage, and family honor.",

        "second_temple": [
            {
                "source": "Mishnah Kilayim",
                "summary": "An entire tractate devoted to the mixing prohibitions of Deut 22:9-11, "
                           "with detailed rules about seed mixtures, animal yoking, and sha'atnez.",
                "relevance": "Shows that the kilayim laws were taken with full legal seriousness in "
                             "rabbinic Judaism and generated extensive halakhic discussion."
            }
        ],

        "cross_refs": [
            {"ref": "Luke 14:5", "note": "Jesus: 'Which of you, having a son or an ox that has fallen into a well, will not immediately pull him out?' — echoing Deut 22:4", "type": "nt"},
            {"ref": "John 8:1-11", "note": "The woman caught in adultery — Jesus confronts the application of laws like Deut 22:22", "type": "nt"},
            {"ref": "Leviticus 19:19", "note": "The parallel mixing prohibitions in the Holiness Code", "type": "ot"},
            {"ref": "2 Corinthians 6:14", "note": "'Do not be unequally yoked with unbelievers' — possible allusion to Deut 22:10", "type": "nt"},
            {"ref": "Matthew 10:29-31", "note": "'Not one sparrow falls apart from your Father' — God's care for creation that Deut 22:6-7 reflects", "type": "nt"}
        ],

        "divine_council_note": "The mixing prohibitions (22:9-11) maintain the category distinctions "
                               "established at creation — the same distinctions that the Watchers "
                               "violated by crossing the divine-human boundary (Gen 6:1-4). The "
                               "principle of 'keeping kinds separate' extends from agriculture and "
                               "textiles to the most fundamental category boundary: the distinction "
                               "between the divine realm and the human realm. Israel's maintenance of "
                               "these boundaries witnesses to the creation order that the rebellious "
                               "'sons of God' violated.",

        "sections": [
            {
                "heading": "Neighborly Responsibility (22:1-4)",
                "body": "The obligation to return a neighbor's strayed ox, sheep, or lost property "
                        "extends Exodus 23:4-5 with the addition: 'You shall not see your brother's "
                        "donkey or his ox fallen down by the way and ignore them. You shall help him "
                        "to lift them up again' (22:4). The verb 'ignore' (hit'allem) means to "
                        "'hide yourself' — to look away and pretend not to see. Covenant community "
                        "prohibits indifference. You cannot be a bystander when your brother's "
                        "livelihood is at stake."
            },
            {
                "heading": "Category Distinctions and Safety (22:5-12)",
                "body": "Cross-dressing is 'an abomination to the LORD' (22:5) — possibly connected "
                        "to Canaanite religious practices involving ritual gender blurring. The mother "
                        "bird law (22:6-7) commands compassion toward animals: take the eggs, but let "
                        "the mother go, 'that it may go well with you and that you may live long.' "
                        "The roof parapet (22:8) prevents accidental death and the resulting bloodguilt. "
                        "The three mixing prohibitions — seeds (22:9), plowing animals (22:10), fabrics "
                        "(22:11) — maintain creation categories. The sha'atnez (wool-linen mixture) "
                        "prohibition has been linked to the priestly garments (which DID combine wool "
                        "and linen), suggesting that Israel must not blur the distinction between "
                        "priestly and common clothing. Tassels on the garment corners (22:12) serve "
                        "as visual reminders of covenant identity (cf. Num 15:37-41)."
            },
            {
                "heading": "Marriage and Sexual Ethics (22:13-21)",
                "body": "The first case: a husband falsely accuses his bride of not being a virgin. "
                        "If the parents produce the 'evidence of her virginity' (the betulim — likely "
                        "the bloodstained wedding cloth), the husband is fined, publicly whipped, and "
                        "forbidden from ever divorcing her (22:18-19). If the accusation is true, the "
                        "woman is stoned at her father's house (22:21). These laws must be read in "
                        "their ANE context: a woman's honor was her family's honor, and false "
                        "accusations could destroy entire families. The protection against false "
                        "accusation (22:13-19) is as significant as the penalty for violation."
            },
            {
                "heading": "Adultery, Rape, and Betrothal Violations (22:22-30)",
                "body": "Adultery carries the death penalty for both parties (22:22). Consensual sex "
                        "with a betrothed woman in the city results in death for both (22:23-24), "
                        "since the woman could have cried for help. Sex with a betrothed woman in the "
                        "open country results in death for the man only (22:25-27), since the woman "
                        "could not summon aid. The case of sex with an unbetrothed virgin results in "
                        "the man paying the bride price and marrying her without right of divorce "
                        "(22:28-29). Modern readers find this deeply troubling, but in the ANE "
                        "context, this law protected the woman's economic future — a non-virgin woman "
                        "without a husband faced destitution. The man is forced to provide for her "
                        "permanently."
            }
        ]
    },

    {
        "id": "deut-23",
        "ref": "Deuteronomy 23",
        "chapter_num": 23,
        "title": "Holiness of the Assembly — Inclusion, Exclusion, and Purity",
        "era": "community",
        "type": "chapter",
        "themes": ["HOLY", "LAW", "NATIONS"],

        "synopsis": "Deuteronomy 23 defines the boundaries of the covenant assembly (qahal YHWH) and "
                    "legislates camp purity, vow fulfillment, and economic ethics. Certain categories "
                    "of people are excluded from the assembly: those with crushed genitals, those of "
                    "illegitimate birth, Ammonites and Moabites (23:1-6). Edomites and Egyptians may "
                    "enter in the third generation (23:7-8). Camp purity during warfare requires "
                    "hygiene provisions (23:9-14) — God 'walks in the midst of your camp,' so the "
                    "camp must be holy. Escaped slaves must not be returned to their masters (23:15-16) "
                    "— a remarkable provision with no ANE parallel. Temple prostitution is forbidden "
                    "(23:17-18). Interest may not be charged to fellow Israelites (23:19-20). Vows to "
                    "YHWH must be fulfilled (23:21-23). Eating from a neighbor's vineyard or grain "
                    "field is permitted, but taking produce away is not (23:24-25).",

        "key_verse": {
            "ref": "Deuteronomy 23:14",
            "text": "Because the LORD your God walks in the midst of your camp, to deliver you and to give up your enemies before you, therefore your camp must be holy, so that he may not see anything indecent among you and turn away from you.",
            "translation": "ESV"
        },

        "original_terms": ["qahal_yhwh", "mamzer", "qedeshah", "neshekh", "neder", "machaneh", "ervat_davar"],

        "hebrew_glossary": {
            "qahal_yhwh": "Assembly of the LORD (the gathered covenant community in YHWH's presence — not every Israelite gathering, but the formal worship assembly; exclusions from the qahal are religious, not civil; those excluded could still live in Israel but could not participate in formal worship)",
            "mamzer": "Illegitimate offspring (the precise meaning is debated — it may refer to the child of a forbidden union (incest or adultery), not simply a child born outside marriage; the exclusion 'to the tenth generation' effectively means permanent in the Ancient Near Eastern context)",
            "qedeshah": "Cult prostitute / sacred sex worker (a woman or man (qadesh) dedicated to sexual rites in the service of a Canaanite deity — the practice was part of fertility worship associated with Asherah and Baal; Israel must not adopt the allotted 'elohim's worship methods)",
            "neshekh": "Interest / usury (literally 'biting' — lending at interest to a fellow Israelite is forbidden; within the covenant community, loans are acts of brotherhood, not commerce; interest to foreigners is permitted, reflecting the covenant's internal vs. external ethic)",
            "machaneh": "Camp (the military camp where YHWH's presence dwells — 'the LORD your God walks in the midst of your camp'; the camp is portable sacred space, like a mobile Eden, requiring the same holiness)"
        },

        "ane_backdrop": "Exclusion from religious assemblies was common in ANE temple practice — "
                        "physical defects were considered disqualifying for approaching the divine. "
                        "Camp purity regulations parallel ANE military camp holiness rules, well-attested "
                        "in Hittite military texts. The prohibition of returning escaped slaves (23:15-16) "
                        "directly contradicts the Code of Hammurabi (Laws 15-20), which prescribed death "
                        "for harboring a runaway slave. Deuteronomy's provision is revolutionary. The "
                        "prohibition of cult prostitution addresses the Canaanite practice of sacred "
                        "sexual rites associated with fertility worship of Asherah and Baal.",

        "second_temple": [
            {
                "source": "Isaiah 56:3-8",
                "summary": "Isaiah prophesies that eunuchs and foreigners who keep the covenant "
                           "will be given 'a monument and a name better than sons and daughters.'",
                "relevance": "The prophetic reversal of Deut 23:1's exclusion — pointing toward "
                             "the universal inclusion of the new covenant."
            },
            {
                "source": "Acts 8:26-39",
                "summary": "Philip baptizes the Ethiopian eunuch — a person excluded by Deut 23:1 "
                           "but included by the new covenant (fulfilling Isaiah 56).",
                "relevance": "The NT's dramatic reversal of the Deut 23 exclusions through Christ."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 56:3-8", "note": "The prophetic expansion of the assembly to include eunuchs and foreigners", "type": "ot"},
            {"ref": "Acts 8:26-39", "note": "The Ethiopian eunuch — Deut 23:1 reversed through the gospel", "type": "nt"},
            {"ref": "Ruth 1:16-17", "note": "Ruth the Moabitess — the Deut 23:3 exclusion overcome by covenant loyalty", "type": "ot"},
            {"ref": "Nehemiah 13:1-3", "note": "Post-exilic enforcement of the Ammonite/Moabite exclusion", "type": "ot"},
            {"ref": "Philemon 1:10-16", "note": "Paul returns Onesimus to Philemon as a brother — transcending Deut 23:15 in Christ", "type": "nt"},
            {"ref": "Matthew 12:1-8", "note": "The disciples pluck grain on the Sabbath — echoing the right of Deut 23:24-25", "type": "nt"}
        ],

        "divine_council_note": "The camp purity requirement (23:14) — 'because the LORD your God walks "
                               "in the midst of your camp' — recalls the garden of Eden, where God "
                               "'walked' (mithallek) in the cool of the day (Gen 3:8). YHWH's presence "
                               "among Israel transforms the camp into sacred space, requiring the same "
                               "holiness expected in Eden. The exclusion of Moabites and Ammonites (23:3-4) "
                               "is partly because they hired Balaam to curse Israel — an attempt to "
                               "weaponize spiritual power against YHWH's people, which has divine council "
                               "implications (Balaam's oracles come from God despite being hired by Israel's "
                               "enemies, showing YHWH's sovereignty over prophetic speech).",

        "sections": [
            {
                "heading": "Exclusions from the Assembly (23:1-8)",
                "body": "Those with crushed testicles or a severed member are excluded (23:1), as are "
                        "those of illegitimate birth (mamzer) to the tenth generation (23:2). Ammonites "
                        "and Moabites are permanently excluded because they did not meet Israel with "
                        "bread and water and because they hired Balaam (23:3-4). Edomites ('your "
                        "brother') and Egyptians ('you were a sojourner in his land') may enter in "
                        "the third generation (23:7-8). These exclusions define the covenant assembly's "
                        "boundaries but are not absolute — the book of Ruth shows a Moabitess entering "
                        "not just the assembly but the Davidic genealogy."
            },
            {
                "heading": "Camp Purity (23:9-14)",
                "body": "During military campaigns, the camp must be kept pure: a man who has a "
                        "nocturnal emission must go outside the camp and bathe at evening (23:10-11). "
                        "A designated area outside the camp serves for bodily functions (23:12-13). "
                        "The reason is theological, not hygienic: 'Because the LORD your God walks in "
                        "the midst of your camp... therefore your camp must be holy, so that he may "
                        "not see anything indecent (ervat davar) among you and turn away from you' "
                        "(23:14). YHWH's presence in the camp requires physical holiness."
            },
            {
                "heading": "Slave Refuge, Prostitution, and Interest (23:15-20)",
                "body": "A runaway slave must not be returned: 'He shall dwell with you, in your "
                        "midst, in the place that he shall choose within one of your towns, wherever "
                        "it suits him. You shall not oppress him' (23:16). This is astonishing in its "
                        "ANE context — Hammurabi prescribed death for harboring runaways. Israel is "
                        "to be a refuge, not a slave-catcher. Cult prostitution (qedeshah/qadesh) is "
                        "forbidden (23:17-18), and the 'wages of a prostitute or the price of a dog' "
                        "may not be brought as a vow offering. Interest (neshekh, literally 'biting') "
                        "may not be charged to fellow Israelites, though it may be charged to "
                        "foreigners (23:19-20)."
            },
            {
                "heading": "Vows and Gleaning Rights (23:21-25)",
                "body": "Vows are voluntary but binding: 'When you make a vow to the LORD your God, "
                        "you shall not delay fulfilling it' (23:21). Not making a vow is fine (23:22), "
                        "but once spoken, it must be kept. A traveler may eat grapes or grain from a "
                        "neighbor's field but may not harvest into a vessel or use a sickle (23:24-25). "
                        "This is the background for the disciples' grain-plucking in Matthew 12:1."
            }
        ]
    },

    {
        "id": "deut-24",
        "ref": "Deuteronomy 24",
        "chapter_num": 24,
        "title": "Divorce, Dignity, and Protection of the Vulnerable",
        "era": "community",
        "type": "chapter",
        "themes": ["LAW", "LOVE", "REMEMBER"],

        "synopsis": "Deuteronomy 24 is a collection of humanitarian laws protecting the dignity of "
                    "individuals within the covenant community. The chapter opens with the divorce "
                    "regulation (24:1-4): a man may divorce his wife if he finds 'some indecency' "
                    "(ervat davar) in her, must give her a written certificate, and she is free to "
                    "remarry — but if she divorces again or her second husband dies, the first "
                    "husband may NOT take her back. The chapter then addresses: a newlywed's military "
                    "exemption (24:5), prohibition of taking millstones as collateral (24:6), "
                    "kidnapping (24:7), skin disease protocols (24:8-9), dignity in taking collateral "
                    "(24:10-13), just wages for laborers (24:14-15), individual legal responsibility "
                    "(24:16), justice for the sojourner and fatherless (24:17-18), and gleaning rights "
                    "for the vulnerable (24:19-22). The common thread is human dignity within covenant "
                    "community — even the poorest, most marginalized person has rights before YHWH.",

        "key_verse": {
            "ref": "Deuteronomy 24:17-18",
            "text": "You shall not pervert the justice due to the sojourner or to the fatherless, or take a widow's garment in pledge. But you shall remember that you were a slave in Egypt and the LORD your God redeemed you from there; therefore I command you to do this.",
            "translation": "ESV"
        },

        "original_terms": ["sefer_keritut", "ervat_davar", "mashkon", "ganav", "sakar", "leqet", "shikhechah", "peah"],

        "hebrew_glossary": {
            "sefer_keritut": "Certificate of divorce (literally 'document of cutting off' — a written legal instrument that freed the woman to remarry; the certificate protected the woman's status by providing proof that her marriage was legitimately ended, not that she was abandoned or an adulteress)",
            "ervat_davar": "Some indecency / a matter of nakedness (the deliberately vague grounds for divorce — the rabbinical schools of Shammai and Hillel famously disagreed: Shammai restricted it to sexual immorality; Hillel allowed it for anything displeasing; Jesus sided closer to Shammai in Matt 19:9 while going beyond both to the creation ideal)",
            "mashkon": "Pledge / collateral (an item taken to secure a loan — Deuteronomy humanizes debt relations: the creditor cannot enter the debtor's house to seize it, and a poor person's cloak must be returned by sunset so they can sleep warmly)",
            "leqet": "Gleanings (the produce left behind after the first harvest pass — the poor, the sojourner, the fatherless, and the widow are entitled to gather what remains; this is God's social safety net, enacted through the Ruth narrative)"
        },

        "ane_backdrop": "Divorce law is attested throughout the ANE. The Code of Hammurabi (Laws "
                        "137-143) allows divorce by either party with varying financial consequences. "
                        "The divorce certificate (sefer keritut) in Deut 24:1 has parallels in "
                        "Mesopotamian and Egyptian divorce documents. The prohibition against "
                        "remarrying the first wife after an intervening marriage is unique to "
                        "Deuteronomy and may reflect concerns about property transfer or about "
                        "treating marriage as a commercial transaction. The gleaning rights "
                        "(24:19-22) have no known ANE parallel — they represent a uniquely Israelite "
                        "social safety net.",

        "second_temple": [
            {
                "source": "Mishnah Gittin 9:10",
                "summary": "The famous debate between the schools of Shammai and Hillel over what "
                           "'ervat davar' (some indecency) means: Shammai allows divorce only for "
                           "sexual immorality; Hillel allows it for anything, even burning dinner.",
                "relevance": "The debate Jesus addresses in Matthew 19:3-9, siding closer to Shammai "
                             "while transcending both positions."
            },
            {
                "source": "Ruth 2:2-23",
                "summary": "Ruth gleans in Boaz's field — the direct fulfillment of Deut 24:19-22's "
                           "gleaning provision for the vulnerable.",
                "relevance": "The book of Ruth dramatizes the Deuteronomic social safety net in action."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 19:3-9", "note": "Jesus on divorce: 'Because of your hardness of heart Moses allowed you to divorce' — interpreting Deut 24:1-4", "type": "nt"},
            {"ref": "Mark 10:2-12", "note": "Jesus appeals behind Deut 24 to Genesis 2:24: 'What God has joined together, let not man separate'", "type": "nt"},
            {"ref": "Jeremiah 3:1", "note": "God uses Deut 24:1-4's remarriage prohibition as an analogy for Israel's infidelity", "type": "ot"},
            {"ref": "Ruth 2:1-23", "note": "Ruth gleans in Boaz's field — Deut 24:19-22 in action", "type": "ot"},
            {"ref": "2 Kings 14:6", "note": "Amaziah obeys Deut 24:16: 'Fathers shall not be put to death because of their children'", "type": "ot"},
            {"ref": "James 5:4", "note": "'The wages of the laborers who mowed your fields, which you kept back by fraud, are crying out' — echoing Deut 24:14-15", "type": "nt"}
        ],

        "divine_council_note": "The humanitarian laws of Deuteronomy 24 embody the justice that YHWH "
                               "demands of Israel — and that the allotted 'elohim failed to provide for "
                               "their nations. Psalm 82:3-4 condemns the 'elohim: 'Give justice to the "
                               "weak and the fatherless; maintain the right of the afflicted and the "
                               "destitute. Rescue the weak and the needy.' Deuteronomy 24's laws for the "
                               "sojourner, fatherless, and widow (24:17-22) are Israel's concrete "
                               "enactment of what the 'elohim failed to do. YHWH's people must demonstrate "
                               "the justice that the divine council was supposed to enforce but didn't.",

        "sections": [
            {
                "heading": "Divorce Regulation (24:1-4)",
                "body": "If a man finds 'some indecency' (ervat davar) in his wife, he may write a "
                        "certificate of divorce (sefer keritut) and send her away (24:1). She may "
                        "remarry (24:2), but if the second marriage also ends, the first husband may "
                        "not take her back — 'that is an abomination before the LORD' (24:4). The "
                        "certificate protects the woman legally: it is proof of her free status. The "
                        "phrase ervat davar is deliberately ambiguous — it generated the Shammai-Hillel "
                        "debate and Jesus' definitive response in Matthew 19."
            },
            {
                "heading": "Protecting the Newly Married and the Vulnerable (24:5-9)",
                "body": "A newly married man is exempt from military service for one year: 'he shall "
                        "be free at home one year to be happy with his wife whom he has taken' (24:5). "
                        "Millstones may not be taken as collateral — they are essential for daily "
                        "bread (24:6). Kidnapping for slave trade is a capital crime (24:7). Skin "
                        "disease must be handled according to Levitical protocols, with the reminder "
                        "of Miriam's punishment (24:8-9)."
            },
            {
                "heading": "Dignity in Debt and Wages (24:10-15)",
                "body": "When taking collateral for a loan, the creditor must not enter the debtor's "
                        "house — 'you shall stand outside, and the man to whom you make the loan "
                        "shall bring the pledge out to you' (24:11). A poor person's cloak taken as "
                        "collateral must be returned by sunset — 'that he may sleep in his cloak and "
                        "bless you' (24:13). Day laborers must be paid on the same day: 'You shall "
                        "give him his wages on the same day... for he is poor and counts on it' "
                        "(24:15). Delayed payment is not merely unfair — it is a sin that the "
                        "laborer will 'cry against you to the LORD' (24:15)."
            },
            {
                "heading": "Individual Responsibility and Gleaning (24:16-22)",
                "body": "A crucial legal principle: 'Fathers shall not be put to death because of "
                        "their children, nor shall children be put to death because of their fathers. "
                        "Each one shall be put to death for his own sin' (24:16). This limits "
                        "collective punishment — a significant advance over ANE practice. Justice "
                        "for the sojourner, fatherless, and widow is commanded with the exodus "
                        "motivation: 'You shall remember that you were a slave in Egypt' (24:18). "
                        "The gleaning laws (24:19-22) mandate leaving forgotten sheaves, olive "
                        "branches, and grape clusters for the vulnerable — God's social safety net."
            }
        ]
    },

    {
        "id": "deut-25",
        "ref": "Deuteronomy 25",
        "chapter_num": 25,
        "title": "Justice, Levirate Marriage, and Honest Measures",
        "era": "community",
        "type": "chapter",
        "themes": ["LAW", "SEED", "NATIONS"],

        "synopsis": "Deuteronomy 25 addresses miscellaneous community laws with a focus on justice "
                    "and dignity. Judicial flogging is limited to forty stripes — 'lest, if one should "
                    "go on to beat him with more stripes... your brother be degraded in your sight' "
                    "(25:3). Even a convicted criminal retains 'brother' status. The ox must not be "
                    "muzzled while threshing (25:4) — a provision for animal welfare that Paul applies "
                    "to ministerial support (1 Cor 9:9). The levirate marriage law (25:5-10) requires "
                    "a brother to marry his deceased brother's childless widow and raise children in "
                    "the dead brother's name — continuing the family line and inheritance. Honest "
                    "weights and measures are commanded (25:13-16). The chapter closes with the "
                    "command to 'remember what Amalek did to you' (25:17-19) — the paradigmatic "
                    "enemy who attacked Israel's weakest members during the exodus.",

        "key_verse": {
            "ref": "Deuteronomy 25:4",
            "text": "You shall not muzzle an ox when it treads out the grain.",
            "translation": "ESV"
        },

        "original_terms": ["malkot", "yibum", "goel", "chalutsah", "even_vaeven", "efah_veefah", "amaleq"],

        "hebrew_glossary": {
            "malkot": "Stripes / lashes (judicial corporal punishment — limited to forty stripes to preserve the convicted person's dignity; Jewish practice reduced it to thirty-nine as a safety margin; Paul received this punishment five times, 2 Cor 11:24)",
            "yibum": "Levirate marriage (from Latin levir, 'brother-in-law' — the obligation of a brother to marry his deceased brother's childless widow and raise offspring 'in the dead brother's name'; this preserves the family line and land inheritance; Boaz's redemption of Ruth is the most famous application)",
            "chalutsah": "Sandal-removal ceremony (the public shaming ritual performed when a brother refuses levirate marriage — the widow pulls off his sandal and spits in his face, and his family is called 'the house of him whose sandal was pulled off'; cf. Ruth 4:7-8 for the transfer of rights)",
            "amaleq": "Amalek (the paradigmatic enemy of Israel who attacked the vulnerable stragglers during the exodus — 'he did not fear God'; the command to 'blot out the memory of Amalek' represents the total elimination of cosmic opposition to YHWH's people)",
            "even_vaeven": "Stone and stone / diverse weights (literally 'a stone and a stone' — having two sets of weights, one heavy for buying and one light for selling; fraudulent commerce is 'an abomination to the LORD,' placing dishonest business alongside idolatry in severity)"
        },

        "ane_backdrop": "Levirate marriage (from Latin levir, 'brother-in-law') is attested in Hittite "
                        "laws (Law 193) and Middle Assyrian laws (Law 30, 33). The practice preserves "
                        "the dead brother's name and inheritance — critical in patrilineal societies "
                        "where a man's legacy depended on having sons. The honest weights command "
                        "parallels the Egyptian 'Instruction of Amenemope' and Mesopotamian commercial "
                        "regulations. Amalek's attack on the stragglers (25:18) reflects the ANE "
                        "practice of targeting vulnerable rearguard elements.",

        "second_temple": [
            {
                "source": "Matthew 22:23-33",
                "summary": "The Sadducees pose a levirate marriage scenario to Jesus to challenge "
                           "resurrection doctrine.",
                "relevance": "Shows that levirate marriage (Deut 25:5-10) was still a live legal "
                             "and theological issue in Jesus' day."
            },
            {
                "source": "Ruth 4:1-12",
                "summary": "Boaz's redemption of Ruth involves the levirate principle, with the "
                           "sandal ceremony of Deut 25:9-10 referenced.",
                "relevance": "The book of Ruth is the narrative fulfillment of Deut 25's levirate "
                             "marriage law."
            }
        ],

        "cross_refs": [
            {"ref": "1 Corinthians 9:9", "note": "Paul: 'Is it for oxen that God is concerned? Does he not certainly speak for our sake?' — applying Deut 25:4 to ministerial support", "type": "nt"},
            {"ref": "1 Timothy 5:18", "note": "Paul again cites Deut 25:4 alongside Luke 10:7 to argue for compensating church leaders", "type": "nt"},
            {"ref": "2 Corinthians 11:24", "note": "Paul: 'Five times I received at the hands of the Jews the forty lashes less one' — the Deut 25:3 limit in practice", "type": "nt"},
            {"ref": "Ruth 4:1-12", "note": "Boaz's levirate redemption — the sandal ceremony reflects Deut 25:9", "type": "ot"},
            {"ref": "Matthew 22:23-33", "note": "The Sadducees' levirate marriage question to Jesus", "type": "nt"},
            {"ref": "1 Samuel 15:1-35", "note": "Saul's failure to destroy Amalek — the Deut 25:19 command partially executed", "type": "ot"}
        ],

        "divine_council_note": "The command to 'blot out the memory of Amalek' (25:19) has divine "
                               "council resonance. Amalek attacked Israel's weakest members — 'the "
                               "faint and weary' at the rear of the march (25:18). The phrase 'he did "
                               "not fear God' (25:18) identifies Amalek's sin as cosmic insubordination "
                               "— attacking YHWH's people is tantamount to attacking YHWH himself. In "
                               "the divine council framework, Amalek represents opposition to YHWH's "
                               "purposes that must be eradicated — foreshadowing the final destruction "
                               "of all cosmic opposition in Revelation.",

        "sections": [
            {
                "heading": "Limits on Punishment — Dignity of the Criminal (25:1-3)",
                "body": "In a dispute settled by judges, the guilty party may be beaten — but no more "
                        "than forty stripes. 'Lest, if one should go on to beat him with more stripes "
                        "than these, your brother be degraded in your sight' (25:3). Even a convicted "
                        "person is 'your brother' — punishment must preserve human dignity. The Jewish "
                        "tradition limited stripes to thirty-nine ('forty less one,' 2 Cor 11:24) to "
                        "provide a margin of error."
            },
            {
                "heading": "The Unmuzzled Ox and Levirate Marriage (25:4-10)",
                "body": "The ox threshing grain must be allowed to eat (25:4) — basic animal welfare "
                        "that Paul extrapolates to ministerial support. The levirate law: if a man "
                        "dies childless, his brother must marry the widow and the first son 'shall "
                        "succeed to the name of his dead brother, that his name may not be blotted out "
                        "of Israel' (25:6). If the brother refuses, the widow performs the chalitzah "
                        "ceremony: pulling off his sandal and spitting in his face, declaring, 'So "
                        "shall it be done to the man who does not build up his brother's house' (25:9). "
                        "The sandal ceremony transfers the right of redemption (cf. Ruth 4:7-8)."
            },
            {
                "heading": "Honest Weights and the Amalek Command (25:11-19)",
                "body": "Diverse weights and measures are forbidden: 'A full and fair weight you shall "
                        "have, a full and fair measure you shall have, that your days may be long' "
                        "(25:15). Dishonest business practices are 'an abomination to the LORD' (25:16). "
                        "The final law is a command of remembrance: 'Remember what Amalek did to you "
                        "on the way as you came out of Egypt, how he attacked you on the way when you "
                        "were faint and weary, and cut off your tail, those who were lagging behind you, "
                        "and he did not fear God' (25:17-18). The command: 'you shall blot out the "
                        "memory of Amalek from under heaven. You shall not forget' (25:19)."
            }
        ]
    },

    {
        "id": "deut-26",
        "ref": "Deuteronomy 26",
        "chapter_num": 26,
        "title": "Firstfruits Confession and Covenant Ratification",
        "era": "community",
        "type": "chapter",
        "themes": ["COV", "LAND", "REMEMBER", "HOLY"],

        "synopsis": "Deuteronomy 26 closes the Deuteronomic Code with two liturgical texts that "
                    "summarize the entire covenant relationship. The firstfruits confession (26:1-11) "
                    "is a creedal recitation performed when the worshipper brings the first produce of "
                    "the land to the central sanctuary: 'A wandering Aramean was my father. And he "
                    "went down into Egypt and sojourned there, few in number, and there he became a "
                    "nation, great, mighty, and populous' (26:5). This creed traces the arc from "
                    "patriarchal vulnerability through Egyptian slavery to divine deliverance to "
                    "landed inheritance — the entire salvation narrative in four verses. The tithe "
                    "confession (26:12-15) is performed every third year, declaring that the tithe "
                    "has been properly distributed. The chapter concludes with the formal covenant "
                    "ratification (26:16-19): 'You have declared today that the LORD is your God... "
                    "And the LORD has declared today that you are a people for his treasured "
                    "possession' (26:17-18). This mutual declaration is the essence of the covenant: "
                    "YHWH belongs to Israel; Israel belongs to YHWH.",

        "key_verse": {
            "ref": "Deuteronomy 26:5",
            "text": "A wandering Aramean was my father. And he went down into Egypt and sojourned there, few in number, and there he became a nation, great, mighty, and populous.",
            "translation": "ESV"
        },

        "original_terms": ["bikkurim", "vidui", "arami_oved", "segullah", "hemir", "am_qadosh", "tehillah"],

        "hebrew_glossary": {
            "bikkurim": "Firstfruits (the first produce of the land, brought to the central sanctuary — presenting firstfruits acknowledges that the land and its fertility belong to YHWH; the worshipper gives back from what God gave first)",
            "vidui": "Confession (a formal declaration — both the firstfruits confession (26:5-10) and the tithe confession (26:13-15) are liturgical recitations that rehearse the salvation narrative; confession in Hebrew is not about admitting guilt but about declaring truth before God)",
            "arami_oved": "A wandering Aramean (the opening of Israel's shortest creed — 'a wandering Aramean was my father'; the Aramean is Jacob, who was connected to Aram through his mother Rebecca and his wives; oved can mean 'wandering,' 'perishing,' or 'lost,' capturing the vulnerability of the patriarchs before God intervened)",
            "segullah": "Treasured possession (YHWH's personal, royal treasure — in the mutual declaration of 26:18, God declares Israel his segullah; this is the climactic use of the term in Deuteronomy, sealing the covenant relationship)",
            "hemir": "Declare / affirm (the verb used in the mutual covenant declaration: Israel 'declares' YHWH as their God, and YHWH 'declares' Israel as his people — a solemn, binding affirmation; the covenant is bilateral: both parties commit)"
        },

        "ane_backdrop": "Firstfruits offerings are attested throughout the ANE — Mesopotamian and "
                        "Egyptian temple records show regular firstfruits presentations. What is unique "
                        "to Israel is the accompanying historical-theological confession. No ANE "
                        "firstfruits ritual includes a narrative recitation of national salvation "
                        "history. The mutual covenant declaration (26:17-19) parallels ANE treaty "
                        "ratification ceremonies where both parties formally affirmed their commitments.",

        "second_temple": [
            {
                "source": "Mishnah Bikkurim 1:1-3:12",
                "summary": "An entire Mishnah tractate devoted to the firstfruits ceremony, "
                           "describing the procession to Jerusalem and the recitation of Deut 26:5-10.",
                "relevance": "Shows that Deut 26's firstfruits liturgy was practiced with elaborate "
                             "ceremony throughout the Second Temple period."
            },
            {
                "source": "Passover Haggadah",
                "summary": "The Haggadah incorporates Deut 26:5 as a key text, with verse-by-verse "
                           "midrashic exposition of 'A wandering Aramean was my father.'",
                "relevance": "The firstfruits confession became the foundation of the Passover Seder "
                             "liturgy — Israel retells the story at every Passover."
            }
        ],

        "cross_refs": [
            {"ref": "Romans 10:9-10", "note": "'If you confess with your mouth that Jesus is Lord... you will be saved' — confession as covenant ratification, echoing Deut 26:17-18", "type": "nt"},
            {"ref": "1 Peter 2:9", "note": "'A people for his own possession' — the Deut 26:18 language applied to the church", "type": "nt"},
            {"ref": "Genesis 46:1-7", "note": "Jacob's descent into Egypt — the event the firstfruits confession narrates", "type": "ot"},
            {"ref": "Exodus 1:7", "note": "'The people of Israel were fruitful and increased greatly' — the 'great, mighty, populous' of Deut 26:5", "type": "ot"},
            {"ref": "Joshua 24:1-28", "note": "Joshua's covenant renewal at Shechem — a parallel covenant ratification ceremony", "type": "ot"},
            {"ref": "Philippians 3:20", "note": "'Our citizenship is in heaven' — the ultimate covenant identity beyond land", "type": "nt"}
        ],

        "divine_council_note": "The mutual covenant declaration of Deuteronomy 26:17-19 is the "
                               "climactic expression of the Deuteronomy 32 worldview in personal terms. "
                               "'You have declared today that the LORD is your God' — not the allotted "
                               "'elohim of the nations, but YHWH. 'And the LORD has declared today that "
                               "you are a people for his treasured possession' — not one of the nations "
                               "allotted to the 'sons of God' in 32:8, but YHWH's own inheritance. The "
                               "firstfruits confession (26:5-10) tells the story from one perspective: "
                               "how Israel came to be YHWH's people. The divine council tells it from "
                               "the other: how YHWH chose Israel when the nations were allotted to "
                               "lesser 'elohim. These are two sides of the same covenant reality.",

        "sections": [
            {
                "heading": "The Firstfruits Confession (26:1-11)",
                "body": "When Israel enters the land and harvests, the worshipper takes the first "
                        "produce to the central sanctuary and sets it before the altar (26:2-4). Then "
                        "the creedal recitation: 'A wandering (oved) Aramean was my father' (26:5a). "
                        "The Hebrew oved can mean 'wandering,' 'perishing,' or 'lost.' Jacob is the "
                        "'father' — an Aramean by family connection (Gen 25:20). The confession traces "
                        "the narrative: descent into Egypt (26:5b), oppression (26:6), crying out to "
                        "YHWH (26:7), deliverance with signs, wonders, and a mighty hand (26:8), and "
                        "entry into the land 'flowing with milk and honey' (26:9). The worshipper then "
                        "sets down the basket and bows, and 'you shall rejoice in all the good that "
                        "the LORD your God has given to you' (26:11). The Levite and the sojourner "
                        "participate in the celebration. This is the shortest creed in the Bible — "
                        "four verses that encapsulate the entire salvation narrative. It became the "
                        "structural core of the Passover Haggadah."
            },
            {
                "heading": "The Tithe Confession (26:12-15)",
                "body": "Every third year, the worshipper declares: 'I have removed the sacred "
                        "portion out of my house, and moreover, I have given it to the Levite, the "
                        "sojourner, the fatherless, and the widow, according to all your commandment "
                        "that you have commanded me. I have not transgressed any of your commandments, "
                        "nor have I forgotten them' (26:13). Then a series of negatives: 'I have not "
                        "eaten of the tithe while I was mourning... I have not offered any of it to "
                        "the dead' (26:14). The final petition: 'Look down from your holy habitation, "
                        "from heaven, and bless your people Israel and the ground that you have given "
                        "us' (26:15). This is one of the few places in Deuteronomy where heaven is "
                        "explicitly identified as God's dwelling — balancing the name-theology with "
                        "transcendence."
            },
            {
                "heading": "Mutual Covenant Declaration (26:16-19)",
                "body": "The Deuteronomic Code concludes with a formal covenant ratification: 'This "
                        "day the LORD your God commands you to do these statutes and rules. You shall "
                        "therefore be careful to do them with all your heart and with all your soul' "
                        "(26:16). Then the mutual declaration: 'You have declared today that the LORD "
                        "is your God, and that you will walk in his ways, and keep his statutes... "
                        "And the LORD has declared today that you are a people for his treasured "
                        "possession (am segullah)... and that you shall be a people holy to the LORD "
                        "your God' (26:17-19). The covenant is bilateral: Israel commits to obedience; "
                        "YHWH commits to Israel. The word hemir ('declared/affirmed') implies a solemn, "
                        "binding commitment. This is the covenant in its simplest form: 'I will be "
                        "your God; you will be my people' (Jer 31:33; Rev 21:3)."
            }
        ]
    }
]
