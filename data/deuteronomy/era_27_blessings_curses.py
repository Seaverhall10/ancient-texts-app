"""
era_27_blessings_curses.py — Blessings, Curses, and the Covenant Choice (Deuteronomy 27-30)

The covenant sanctions: blessings for obedience and curses for disobedience.
This section follows the standard ANE treaty form and contains some of the
most terrifying and most hopeful passages in the entire Torah. Chapter 30
promises the circumcision of the heart — the new covenant in embryonic form.
"""

CHAPTERS = [
    {
        "id": "deut-27",
        "ref": "Deuteronomy 27",
        "chapter_num": 27,
        "title": "The Altar on Ebal and the Twelve Curses",
        "era": "blessings_curses",
        "type": "chapter",

        "synopsis": "Deuteronomy 27 prescribes the covenant ratification ceremony to be performed "
                    "upon entering the land. Moses and the elders command Israel to set up large "
                    "stones on Mount Ebal, coat them with plaster, and write 'all the words of this "
                    "law' on them (27:2-4) — the covenant document publicly displayed. An altar of "
                    "uncut stones is to be built on Ebal for burnt offerings and peace offerings "
                    "(27:5-7). The tribes are then divided: six tribes on Mount Gerizim to bless "
                    "(Simeon, Levi, Judah, Issachar, Joseph, Benjamin) and six on Mount Ebal to "
                    "curse (Reuben, Gad, Asher, Zebulun, Dan, Naphtali, 27:12-13). The Levites "
                    "pronounce twelve curses — each beginning with 'Cursed be the one who...' — and "
                    "the people respond 'Amen' to each (27:14-26). The curses address: idolatry, "
                    "dishonoring parents, moving boundary markers, misleading the blind, perverting "
                    "justice for the vulnerable, various sexual sins, secret murder, accepting bribes, "
                    "and the catch-all: 'Cursed be anyone who does not confirm the words of this law "
                    "by doing them' (27:26). This verse is quoted by Paul in Galatians 3:10 as "
                    "evidence that 'all who rely on works of the law are under a curse.' The ceremony "
                    "transforms the landscape into a covenant witness: every time Israel looks at "
                    "Gerizim and Ebal, they see blessing and curse.",

        "key_verse": {
            "ref": "Deuteronomy 27:26",
            "text": "Cursed be anyone who does not confirm the words of this law by doing them. And all the people shall say, 'Amen.'",
            "translation": "ESV"
        },

        "hebrew_terms": ["arur", "amen", "eval", "gerizim", "sid", "mizbeach", "abanim_shelemot", "kol_divrei_hatorah"],

        "hebrew_glossary": {
            "arur": "Cursed (the covenant sanction for disobedience — each of the twelve curses begins with this word; by responding 'Amen,' Israel voluntarily invokes these curses upon themselves if they violate the covenant; the opposite of barukh, 'blessed')",
            "amen": "Truly / so be it / let it stand (the people's response to each curse — not passive agreement but active acceptance; by saying 'Amen,' each Israelite personally ratifies the covenant sanctions and takes responsibility for the consequences of violation)",
            "sid": "Plaster / lime coating (the white surface applied to the memorial stones to make them writable — a technique attested in ANE monumental inscriptions; the plaster created a smooth surface on which 'all the words of this law' could be inscribed for public reading)",
            "abanim_shelemot": "Whole stones / uncut stones (the altar must be built of natural, unworked stones — no iron tools; human artistry must not shape the place of sacrifice; God provides the materials, humans must not improve upon them)",
            "kol_divrei_hatorah": "All the words of this Torah (the comprehensive scope of the covenant — the final curse (27:26) condemns anyone who fails to uphold ALL the words, not just some; Paul quotes this in Galatians 3:10 to argue that no one can keep the whole law, making everyone liable to the curse)"
        },

        "ane_backdrop": "The public inscription of treaty terms on stone is well-attested in ANE "
                        "practice. The Hittite treaties of Suppiluliuma I required copies to be "
                        "inscribed and deposited in temples. The Code of Hammurabi was inscribed on "
                        "a basalt stele for public display. The Egyptian-Hittite peace treaty was "
                        "inscribed on both Egyptian and Hittite monuments. The Shechem setting between "
                        "Ebal and Gerizim provided a natural amphitheater for public proclamation. "
                        "The curse-and-blessing format follows standard ANE treaty sanctions: Hittite "
                        "and Akkadian treaties contain similar lists of blessings for compliance and "
                        "curses for violation. The Esarhaddon vassal treaties (672 BC) contain "
                        "particularly elaborate curse formulas with striking parallels to Deut 28.",

        "second_temple": [
            {
                "source": "Joshua 8:30-35",
                "summary": "Joshua performs the Ebal/Gerizim ceremony as commanded, reading 'all "
                           "the words of the law, the blessing and the curse.'",
                "relevance": "The fulfillment of Deut 27's command — confirmation that the covenant "
                             "ratification ceremony was actually performed upon entering the land."
            },
            {
                "source": "Galatians 3:10",
                "summary": "Paul quotes Deut 27:26: 'Cursed be everyone who does not abide by all "
                           "things written in the Book of the Law, and do them.'",
                "relevance": "Paul's argument that the law's curse falls on all who fail to keep it "
                             "perfectly — which is everyone. The solution: Christ became the curse "
                             "(Gal 3:13)."
            },
            {
                "source": "Samaritan Pentateuch — Deut 27:4",
                "summary": "The SP reads 'Mount Gerizim' where the MT reads 'Mount Ebal' — the "
                           "altar was to be built on Gerizim (the blessing mountain) according to "
                           "the Samaritan tradition.",
                "relevance": "The textual variant that defines the Jewish-Samaritan schism. Some "
                             "scholars argue the SP preserves the older reading."
            }
        ],

        "cross_refs": [
            {"ref": "Joshua 8:30-35", "note": "The fulfillment of the Ebal/Gerizim ceremony", "type": "ot"},
            {"ref": "Galatians 3:10-14", "note": "Paul cites Deut 27:26 to argue that the law's curse falls on all, and Christ redeemed us by becoming the curse", "type": "nt"},
            {"ref": "Joshua 24:25-27", "note": "Joshua sets up a stone as covenant witness at Shechem — the same region as Ebal/Gerizim", "type": "ot"},
            {"ref": "James 2:10", "note": "'Whoever keeps the whole law but fails in one point has become guilty of all of it' — the logic of Deut 27:26", "type": "nt"},
            {"ref": "Jeremiah 11:3-5", "note": "'Cursed be the man who does not hear the words of this covenant' — prophetic invocation of the Deut 27 curse", "type": "ot"},
            {"ref": "John 4:20", "note": "The Samaritan woman: 'Our fathers worshiped on this mountain' — Mount Gerizim, the Deut 27 blessing mountain", "type": "nt"}
        ],

        "divine_council_note": "The twelve curses of Deuteronomy 27 function as the covenant's "
                               "sanctions — the consequences of treaty violation. In ANE suzerainty "
                               "treaties, the gods of both parties served as witnesses and enforcers of "
                               "the curses. In Israel's covenant, heaven and earth serve as witnesses "
                               "(Deut 30:19), and YHWH himself is both treaty-maker and enforcer. The "
                               "comprehensive final curse — 'Cursed be anyone who does not confirm the "
                               "words of this law by doing them' (27:26) — places ALL of Israel under "
                               "potential curse. Paul's interpretation in Galatians 3:10-14 is that the "
                               "curse DID fall on Israel (exile), and Christ absorbed it on the cross "
                               "(Gal 3:13), so that 'the blessing of Abraham might come to the Gentiles' "
                               "(Gal 3:14). In divine council terms: the curse that separated Israel "
                               "from YHWH (subjecting them to the allotted 'elohim's authority in exile) "
                               "was broken by Christ, and the nations held by the allotted 'elohim can "
                               "now receive Abraham's blessing.",

        "sections": [
            {
                "heading": "The Stones and Altar on Mount Ebal (27:1-8)",
                "body": "Moses and the elders command: 'On the day you cross over the Jordan to the "
                        "land that the LORD your God is giving you, you shall set up large stones and "
                        "plaster them with plaster. And you shall write on them all the words of this "
                        "law' (27:2-3). The plaster coating (sid) would create a smooth, white surface "
                        "for writing — a technique attested in ANE monumental inscriptions. The altar "
                        "must be of 'whole stones' (abanim shelemot) — uncut, without iron tools "
                        "(27:5-6). The avoidance of iron tools recalls Exodus 20:25 and reflects "
                        "the principle that human artistry must not shape the altar; it remains as "
                        "God made it. Burnt offerings and peace offerings are to be offered, and "
                        "'you shall eat there, and you shall rejoice before the LORD your God' (27:7). "
                        "The covenant ratification includes communal feasting — joy alongside solemnity."
            },
            {
                "heading": "Tribes on Gerizim and Ebal (27:9-13)",
                "body": "Moses and the Levitical priests declare: 'This day you have become the people "
                        "of the LORD your God' (27:9). The tribes are divided: Simeon, Levi, Judah, "
                        "Issachar, Joseph, and Benjamin stand on Gerizim (the blessing mountain); "
                        "Reuben, Gad, Asher, Zebulun, Dan, and Naphtali stand on Ebal (the curse "
                        "mountain). The division is not arbitrary: the Gerizim tribes include the "
                        "four sons of the favored wives (Leah: Simeon, Levi, Judah, Issachar; "
                        "Rachel: Joseph, Benjamin), while the Ebal tribes include sons of the "
                        "concubines (Dan, Naphtali, Gad, Asher) plus Reuben (who lost his birthright) "
                        "and Zebulun. The geography creates a living tableau: blessing and curse are "
                        "visible, embodied, and inescapable."
            },
            {
                "heading": "The Twelve Curses (27:14-26)",
                "body": "The Levites pronounce twelve curses with a loud voice, and the people respond "
                        "'Amen' to each — freely accepting the covenant sanctions. The curses address: "
                        "(1) Making carved or metal images (27:15). (2) Dishonoring father or mother "
                        "(27:16). (3) Moving a neighbor's boundary marker (27:17). (4) Misleading a "
                        "blind person (27:18). (5) Perverting justice for the sojourner, fatherless, "
                        "or widow (27:19). (6-9) Four sexual violations: father's wife, any animal, "
                        "sister, and mother-in-law (27:20-23). (10) Striking a neighbor in secret "
                        "(27:24). (11) Taking a bribe to shed innocent blood (27:25). (12) The "
                        "comprehensive curse: 'Cursed be anyone who does not confirm the words of "
                        "this law by doing them' (27:26). The twelfth curse is devastating: it "
                        "catches everyone. No one keeps 'all the words of this law.' Israel says "
                        "'Amen' to their own condemnation — and the history that follows proves it. "
                        "Paul sees this as the human condition universalized: 'All have sinned and "
                        "fall short' (Rom 3:23)."
            }
        ]
    },

    {
        "id": "deut-28",
        "ref": "Deuteronomy 28",
        "chapter_num": 28,
        "title": "The Blessings and Curses — Covenant Consequences in Full",
        "era": "blessings_curses",
        "type": "chapter",

        "synopsis": "Deuteronomy 28 is the longest and most intense chapter in the entire Torah — "
                    "68 verses of blessings (28:1-14) followed by curses (28:15-68) that escalate "
                    "from agricultural failure to disease to military defeat to cannibalism to exile. "
                    "The blessings are comprehensive: blessed in the city and in the field, in the "
                    "fruit of the womb and ground and livestock, in the basket and kneading bowl, in "
                    "coming in and going out (28:3-6). Israel will be the head and not the tail, "
                    "above and not beneath (28:13). The curses are a horrifying mirror image: cursed "
                    "in all the same categories, plus disease, drought, military disaster, siege, "
                    "madness, and the ultimate curse — exile among the nations. The siege curses are "
                    "graphic: 'The most tender and refined woman among you... will begrudge food to "
                    "the husband she embraces... because of the siege' (28:56-57). This was literally "
                    "fulfilled at the siege of Jerusalem in 70 AD (Josephus, Wars 6.3.4). The chapter "
                    "closes with exile: 'The LORD will scatter you among all peoples, from one end of "
                    "the earth to the other... Among these nations you shall find no respite' (28:64-65). "
                    "Deuteronomy 28 is covenant theology at its most terrifying — and its most "
                    "historically verified.",

        "key_verse": {
            "ref": "Deuteronomy 28:1-2",
            "text": "And if you faithfully obey the voice of the LORD your God, being careful to do all his commandments that I command you today, the LORD your God will set you high above all the nations of the earth. And all these blessings shall come upon you and overtake you, if you obey the voice of the LORD your God.",
            "translation": "ESV"
        },

        "hebrew_terms": ["barukh", "arur", "dever", "shachin", "shiddafon", "shoteh", "galut", "magor", "tzalmavet"],

        "hebrew_glossary": {
            "barukh": "Blessed (the covenant reward for faithfulness — the blessings are active, they 'come upon you and overtake you'; barukh is the opposite of arur and covers every dimension of life: city, field, womb, ground, basket, and movement)",
            "arur": "Cursed (the covenant punishment for unfaithfulness — the curses mirror the blessings in exact reverse, then escalate far beyond: disease, defeat, siege, cannibalism, exile; the asymmetry between 14 verses of blessing and 54 verses of curse reflects the trajectory Moses foresees)",
            "dever": "Pestilence / plague (one of the covenant curses — disease as divine judgment; the plagues God inflicted on Egypt are now threatened against Israel if they behave like Egypt's gods' vassals rather than YHWH's people)",
            "galut": "Exile / diaspora (the climactic covenant curse — scattering among the nations; in divine council terms, exile means transfer from YHWH's direct governance to the territory of the allotted 'elohim; Israel will 'serve gods of wood and stone' in exile, 28:36, 64)",
            "ol_barzel": "Yoke of iron (the metaphor for enemy oppression in 28:48 — the iron yoke replaces YHWH's 'easy' yoke of Torah; Jeremiah 28:13-14 echoes this with Nebuchadnezzar's iron yoke on the nations)"
        },

        "ane_backdrop": "Deuteronomy 28's curse sequence has remarkable parallels to the Esarhaddon "
                        "vassal treaties (672 BC), which contain similar escalating curses: disease, "
                        "agricultural failure, darkness, madness, and cannibalism during siege. The "
                        "sequence of curses also parallels Hittite treaty sanctions (14th-13th century "
                        "BC). The debate over whether Deuteronomy borrows from Esarhaddon or both "
                        "draw on a common ANE curse tradition remains unresolved. The blessings section "
                        "also parallels ANE treaty rewards: fertility, military success, and elevated "
                        "status among vassal nations. The most distinctive element is the theological "
                        "interpretation: the curses are not arbitrary divine punishment but covenant "
                        "consequences — YHWH warned in advance, Israel accepted the terms, and the "
                        "sanctions execute themselves when the terms are violated.",

        "second_temple": [
            {
                "source": "Josephus, Wars 6.3.3-4",
                "summary": "Josephus records the cannibalism during the Roman siege of Jerusalem "
                           "in 70 AD: a woman named Mary roasted and ate her own infant.",
                "relevance": "The horrifying literal fulfillment of Deut 28:53-57. Josephus himself "
                             "recognized the connection to Deuteronomy's curse."
            },
            {
                "source": "4Q504 (Words of the Luminaries)",
                "summary": "Qumran liturgical prayers that confess the community's experience of "
                           "Deut 28's curses and plead for restoration.",
                "relevance": "Shows that the Qumran community understood their marginalization as "
                             "a partial experience of the Deuteronomic curses.",
                "canon": False
            },
            {
                "source": "Baruch 1:15-3:8",
                "summary": "A prayer of confession from the Babylonian exile that draws extensively "
                           "on Deut 28-30's curse and restoration language.",
                "relevance": "Demonstrates that the exilic community understood their experience "
                             "through the lens of Deuteronomy 28's covenant curses."
            }
        ],

        "cross_refs": [
            {"ref": "Leviticus 26:14-45", "note": "The parallel blessing-and-curse list in the Holiness Code — Deut 28 expands and intensifies it", "type": "ot"},
            {"ref": "Lamentations 1-5", "note": "The fall of Jerusalem as the fulfillment of the Deut 28 curses", "type": "ot"},
            {"ref": "2 Kings 25:1-21", "note": "The Babylonian destruction of Jerusalem — the Deut 28 curses realized", "type": "ot"},
            {"ref": "Romans 11:7-10", "note": "Paul quotes Deut 28-29 regarding Israel's hardening: 'God gave them a spirit of stupor'", "type": "nt"},
            {"ref": "Daniel 9:11-14", "note": "Daniel's prayer: 'The curse and oath that are written in the Law of Moses have been poured out upon us'", "type": "ot"},
            {"ref": "Galatians 3:13-14", "note": "'Christ redeemed us from the curse of the law by becoming a curse for us' — the Deut 28 curse borne by Christ", "type": "nt"},
            {"ref": "Esarhaddon Vassal Treaties (672 BC)", "note": "Parallel escalating curse sequence: disease, madness, siege, cannibalism", "type": "ane"}
        ],

        "divine_council_note": "Deuteronomy 28 has profound divine council implications. The curses "
                               "describe what happens when Israel leaves YHWH's protection and comes "
                               "under the power of the allotted 'elohim through exile: 'And there you "
                               "shall serve other gods of wood and stone' (28:36). Exile is not just "
                               "political displacement — it is transfer from YHWH's direct governance "
                               "to the territory and authority of the allotted 'elohim. The curse of "
                               "serving 'gods of wood and stone' (28:36, 64) echoes Deut 4:28: this "
                               "is what happens when Israel falls under the jurisdiction of the nations "
                               "and their 'elohim. The reversal promised in Deut 30 (return from exile, "
                               "circumcision of the heart) is therefore a divine council reversal: YHWH "
                               "reclaims his people from the territory of the allotted 'elohim. The "
                               "ultimate fulfillment is in Christ, who bears the curse (Gal 3:13) and "
                               "thereby breaks the power of the allotted 'elohim over both Israel and "
                               "the nations.",

        "sections": [
            {
                "heading": "The Covenant Blessings (28:1-14)",
                "body": "The blessings are introduced with a conditional: 'And if you faithfully obey "
                        "the voice of the LORD your God... all these blessings shall come upon you and "
                        "overtake you' (28:1-2). The verb 'overtake' (hissigu) is striking — the "
                        "blessings are active, pursuing Israel like a hunter. The blessings cover "
                        "every sphere: 'Blessed shall you be in the city, and blessed shall you be "
                        "in the field' (28:3). Fertility of womb, ground, and livestock (28:4). "
                        "Blessed basket and kneading bowl — the daily bread of life (28:5). Blessed "
                        "in coming in and going out — all movement and activity (28:6). Military "
                        "victory: enemies attack by one road and flee by seven (28:7). Abundant "
                        "prosperity that causes all nations to 'see that you are called by the name "
                        "of the LORD, and they shall be afraid of you' (28:10). Israel will lend to "
                        "nations and not borrow, will be 'the head and not the tail' (28:13). The "
                        "condition is restated: 'if you obey the commandments of the LORD your God "
                        "... and do not turn aside from any of the words... to go after other gods' "
                        "(28:13-14). The 'other gods' are the allotted 'elohim — the nations' "
                        "spiritual rulers that Israel must not serve."
            },
            {
                "heading": "The Covenant Curses Begin — Disease and Defeat (28:15-44)",
                "body": "The curses mirror the blessings in reverse: cursed in city and field, in "
                        "womb and ground, in basket and bowl, in coming and going (28:16-19). Then "
                        "they escalate beyond mere reversal: 'The LORD will send on you curses, "
                        "confusion, and frustration in all that you undertake to do' (28:20). Disease: "
                        "consumption, fever, inflammation, fiery heat, drought, blight, mildew "
                        "(28:22). Military defeat: 'You shall go out one way against them and flee "
                        "seven ways before them' (28:25) — the exact reversal of the blessing (28:7). "
                        "The bodies of the slain will be 'food for all birds of the air and for the "
                        "beasts of the earth' (28:26). Boils, tumors, scurvy, madness, blindness, "
                        "confusion (28:27-28). Another man will enjoy your wife, house, vineyard "
                        "(28:30). Your children will be taken, and 'there shall be no power in your "
                        "hand' (28:32). The trajectory is relentless: from inconvenience to disease "
                        "to defeat to total dispossession."
            },
            {
                "heading": "Exile and Servitude (28:45-57)",
                "body": "The curses intensify toward exile: 'Because you did not serve the LORD your "
                        "God with joyfulness and gladness of heart, because of the abundance of all "
                        "things, therefore you shall serve your enemies whom the LORD will send against "
                        "you, in hunger and thirst, in nakedness, and lacking everything. And he will "
                        "put a yoke of iron on your neck until he has destroyed you' (28:47-48). A "
                        "nation from afar will besiege every city — 'a nation whose language you do "
                        "not understand, a hard-faced nation' (28:49-50). The siege will reduce Israel "
                        "to cannibalism: 'You shall eat the fruit of your womb, the flesh of your "
                        "sons and daughters, in the siege and in the distress with which your enemies "
                        "shall distress you' (28:53). Even 'the most tender and refined woman among "
                        "you' will begrudge food to her own family and secretly consume her own "
                        "afterbirth (28:56-57). These horrifying predictions were fulfilled in the "
                        "sieges of Samaria (2 Kings 6:28-29) and Jerusalem (Lam 2:20; 4:10; Josephus, "
                        "Wars 6.3.4). Deuteronomy 28 reads less like curse-formulas and more like "
                        "prophecy-in-advance."
            },
            {
                "heading": "Scattering Among the Nations (28:58-68)",
                "body": "The climactic curse: exile and scattering. 'The LORD will scatter you among "
                        "all peoples, from one end of the earth to the other, and there you shall "
                        "serve other gods of wood and stone, which neither you nor your fathers have "
                        "known' (28:64). Among the nations, Israel will find 'no respite' (28:65) "
                        "but 'a trembling heart and failing eyes and a languishing soul. Your life "
                        "shall hang in doubt before you. Night and day you shall be in dread and have "
                        "no assurance of your life' (28:65-66). The final verse is devastating: 'And "
                        "the LORD will bring you back in ships to Egypt, a journey that I promised "
                        "that you should never make again. And there you shall offer yourselves for "
                        "sale to your enemies as male and female slaves, but there will be no buyer' "
                        "(28:68). The exodus reversed. The liberation undone. Israel returns to the "
                        "place of slavery — and no one will even want them as slaves. This is the "
                        "covenant's ultimate sanction: not just exile but the nullification of the "
                        "salvation story itself."
            }
        ]
    },

    {
        "id": "deut-29",
        "ref": "Deuteronomy 29",
        "chapter_num": 29,
        "title": "The Covenant in Moab — Warning and the God Who Allots",
        "era": "blessings_curses",
        "type": "chapter",

        "synopsis": "Deuteronomy 29 opens Moses' third and final address, marking a new covenant "
                    "ceremony 'in the land of Moab, besides the covenant that he had made with them "
                    "at Horeb' (29:1). This is not merely a restatement of Sinai but a distinct "
                    "covenant renewal. Moses recounts God's mighty acts (29:2-8) and then includes "
                    "ALL of Israel in the covenant — from leaders to the 'sojourner who cuts your "
                    "wood and draws your water' (29:10-11). Even future generations and those 'not "
                    "here today' are bound by this covenant (29:14-15). Moses warns against a 'root "
                    "bearing poisonous and bitter fruit' — someone who hears the covenant curses and "
                    "secretly thinks 'I shall be safe, though I walk in the stubbornness of my heart' "
                    "(29:18-19). That person's self-deception will bring the full weight of the "
                    "curses. Future generations and foreigners will see the devastated land and ask: "
                    "'Why has the LORD done thus to this land?' The answer: 'Because they abandoned "
                    "the covenant of the LORD... and went and served other gods and worshipped them, "
                    "gods whom they had not known and whom he had not allotted to them' (29:25-26). "
                    "The phrase 'whom he had not allotted to them' (29:26) is a divine council "
                    "reference: these gods WERE allotted — but to OTHER nations, not to Israel. "
                    "The chapter closes with one of the most quoted verses in Deuteronomy: 'The "
                    "secret things belong to the LORD our God, but the things that are revealed "
                    "belong to us and to our children forever' (29:29).",

        "key_verse": {
            "ref": "Deuteronomy 29:25-26",
            "text": "Then people will say, 'It is because they abandoned the covenant of the LORD, the God of their fathers, which he made with them when he brought them out of the land of Egypt, and went and served other gods and worshiped them, gods whom they had not known and whom he had not allotted to them.'",
            "translation": "ESV"
        },

        "hebrew_terms": ["berit", "alah", "shoresh", "rosh_velaanah", "nistarot", "niglot", "chalaq"],

        "hebrew_glossary": {
            "berit": "Covenant (the solemn, binding agreement between YHWH and Israel — the Moab covenant here is distinct from the Sinai/Horeb covenant, a supplemental treaty renewal for the new generation)",
            "alah": "Oath / curse (the self-imprecation that accompanies covenant-making — by saying 'Amen' to the curses, Israel invokes them upon themselves if they break the covenant)",
            "chalaq": "Allot / divide (the same verb used in 4:19 and implied in 32:8 — God 'allotted' the nations' gods to them; 29:26 uses it explicitly: gods 'he had not allotted to them')",
            "nistarot": "Secret things (what belongs to YHWH alone — the hidden workings of the divine council, the mystery of election, the full scope of the cosmic drama; humans are not entitled to know everything God knows)",
            "niglot": "Revealed things (what God has disclosed through Torah — sufficient for obedience and life; the contrast with nistarot establishes a boundary: pursue what God has revealed, trust him with what remains hidden)"
        },

        "ane_backdrop": "The covenant renewal at Moab parallels ANE treaty renewal ceremonies, where "
                        "a suzerainty treaty was periodically reaffirmed, especially at generational "
                        "transitions. The inclusion of all social classes in the covenant community "
                        "(29:10-11) — from leaders to wood-cutters — is distinctive; ANE treaties "
                        "typically bound only the ruling class. The 'question from foreigners' motif "
                        "(29:22-28) parallels the genre of 'ruin oracles' found in Mesopotamian "
                        "literature, where passersby view a destroyed city and ask what caused its "
                        "devastation. The answer is always theological: the city's god was offended.",

        "second_temple": [
            {
                "source": "Hebrews 12:15",
                "summary": "The author warns against 'a root of bitterness' that defiles many — "
                           "directly echoing Deut 29:18.",
                "relevance": "The NT application of Deut 29's warning about hidden apostasy "
                             "within the covenant community."
            },
            {
                "source": "1QS (Community Rule) 1:16-2:18",
                "summary": "The Qumran covenant renewal ceremony explicitly models itself on "
                           "Deuteronomy 29-30, with blessings and curses pronounced over new members.",
                "relevance": "Proves that Qumran understood itself as renewing the Deuteronomic "
                             "covenant in their own community."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 12:15", "note": "'See to it that no root of bitterness springs up and causes trouble' — quoting Deut 29:18", "type": "nt"},
            {"ref": "1 Kings 9:8-9", "note": "Foreigners will ask why God destroyed the temple — the fulfillment of Deut 29:22-28", "type": "ot"},
            {"ref": "Jeremiah 22:8-9", "note": "Nations ask why Jerusalem was destroyed: 'Because they abandoned the covenant of the LORD' — echoing Deut 29:25", "type": "ot"},
            {"ref": "Romans 11:33-36", "note": "'How unsearchable are his judgments and how inscrutable his ways!' — the NT echo of 'the secret things belong to the LORD' (29:29)", "type": "nt"},
            {"ref": "Acts 2:39", "note": "'The promise is for you and for your children and for all who are far off' — the Deut 29:14-15 inclusion extended to the Gentiles", "type": "nt"}
        ],

        "divine_council_note": "Deuteronomy 29:26 contains one of the most explicit divine council "
                               "statements in the Torah: Israel served 'gods whom they had not known "
                               "and whom he [God] had not allotted (chalaq) to them.' The verb chalaq "
                               "is the same used in 4:19 ('things that the LORD your God has allotted "
                               "to all the peoples') and implied in 32:8 (the allotment of nations to "
                               "the 'sons of God'). The statement in 29:26 confirms: (1) The nations' "
                               "gods were allotted by YHWH — this is an intentional divine arrangement. "
                               "(2) These gods were NOT allotted to Israel — Israel's worship of them "
                               "is a violation of the cosmic order YHWH established. (3) Israel's sin "
                               "is therefore doubly treasonous: they violated their covenant with YHWH "
                               "AND they trespassed into the jurisdiction of 'elohim assigned to other "
                               "nations. This passage destroys any reading of Deuteronomy that denies "
                               "the existence of the nations' gods — the text explicitly states God "
                               "allotted them.",

        "sections": [
            {
                "heading": "The Covenant at Moab — Distinct from Horeb (29:1-9)",
                "body": "The chapter heading establishes a new covenant: 'These are the words of the "
                        "covenant that the LORD commanded Moses to make with the people of Israel in "
                        "the land of Moab, besides the covenant that he had made with them at Horeb' "
                        "(29:1). The Moab covenant supplements Sinai; it does not replace it. Moses "
                        "recounts God's deeds in Egypt and the wilderness, then adds a penetrating "
                        "observation: 'But to this day the LORD has not given you a heart to understand "
                        "or eyes to see or ears to hear' (29:4). Despite forty years of miracles, "
                        "Israel's spiritual perception remains dull. This verse anticipates the need "
                        "for the heart-circumcision of chapter 30 and the new covenant of Jeremiah 31."
            },
            {
                "heading": "All Israel Enters the Covenant (29:10-15)",
                "body": "Moses includes every stratum of society: 'You are standing today, all of you, "
                        "before the LORD your God: the heads of your tribes, your elders, and your "
                        "officers, all the men of Israel, your little ones, your wives, and the "
                        "sojourner who is in your camp, from the one who chops your wood to the one "
                        "who draws your water' (29:10-11). The covenant is radically inclusive — no "
                        "social class is exempt or excluded. Even the sojourner (ger) — a non-Israelite "
                        "residing among Israel — is bound. Most remarkably: 'It is not with you alone "
                        "that I am making this sworn covenant, but with whoever is standing here with "
                        "us today before the LORD our God, and with whoever is not here with us today' "
                        "(29:14-15). Future generations are included. The covenant transcends time."
            },
            {
                "heading": "The Root of Bitterness — Hidden Apostasy (29:16-21)",
                "body": "Moses warns against someone who hears the covenant curses and privately "
                        "calculates: 'I shall be safe, though I walk in the stubbornness of my heart' "
                        "(29:19). This self-deception is called a 'root bearing poisonous and bitter "
                        "fruit' (29:18) — internal rebellion that will eventually poison the whole "
                        "community. 'The LORD will not be willing to forgive him, but rather the anger "
                        "of the LORD and his jealousy will smoke against that man, and the curses "
                        "written in this book will settle upon him' (29:20). The individual's name "
                        "will be 'blotted out from under heaven' (29:20). Hebrews 12:15 applies this "
                        "to the church: beware of a root of bitterness that 'springs up and causes "
                        "trouble, and by it many become defiled.'"
            },
            {
                "heading": "Why Did God Do This? — The Nations' Question (29:22-29)",
                "body": "Moses foresees the devastation and the question it will provoke: 'All the "
                        "nations will say, \"Why has the LORD done thus to this land? What caused the "
                        "heat of this great anger?\"' (29:24). The answer: 'It is because they "
                        "abandoned the covenant of the LORD... and went and served other gods and "
                        "worshiped them, gods whom they had not known and whom he had not allotted to "
                        "them' (29:25-26). The allotment language is crucial — Israel's sin is "
                        "worshipping gods assigned to other nations, not to them. The chapter closes "
                        "with a wisdom saying: 'The secret things (nistarot) belong to the LORD our "
                        "God, but the things that are revealed (niglot) belong to us and to our "
                        "children forever, that we may do all the words of this law' (29:29). What "
                        "God has revealed (the Torah) is sufficient; what remains hidden (the full "
                        "scope of the divine council, the mystery of election, the timing of "
                        "fulfillment) belongs to God alone."
            }
        ]
    },

    {
        "id": "deut-30",
        "ref": "Deuteronomy 30",
        "chapter_num": 30,
        "title": "Return, Restoration, and the Circumcision of the Heart",
        "era": "blessings_curses",
        "type": "chapter",

        "synopsis": "Deuteronomy 30 is the most hopeful chapter in the Torah — the divine answer to "
                    "the devastating curses of chapter 28 and the honest assessment of chapter 29. "
                    "Moses looks BEYOND the curse, beyond the exile, to a promised restoration: 'When "
                    "all these things come upon you... and you call them to mind among all the nations "
                    "where the LORD your God has driven you, and return to the LORD your God... then "
                    "the LORD your God will restore your fortunes' (30:1-3). God will gather the "
                    "scattered exiles 'from all the peoples where the LORD your God has scattered you' "
                    "(30:3). Then comes the remarkable promise: 'And the LORD your God will circumcise "
                    "your heart and the heart of your offspring, so that you will love the LORD your "
                    "God with all your heart and with all your soul, that you may live' (30:6). Moses "
                    "commanded heart-circumcision in 10:16; now God promises to DO it himself. This "
                    "is the embryonic form of the new covenant — the divine solution to Israel's "
                    "persistent inability to keep the covenant. The curse will be transferred to "
                    "Israel's enemies (30:7). Prosperity will return (30:9). The commandment is 'not "
                    "too hard for you... it is not in heaven... not beyond the sea... but the word is "
                    "very near you, in your mouth and in your heart' (30:11-14) — a passage Paul "
                    "applies christologically in Romans 10:6-8. The chapter climaxes with the most "
                    "famous choice in the Bible: 'I have set before you today life and death, blessing "
                    "and curse. Therefore choose life' (30:19).",

        "key_verse": {
            "ref": "Deuteronomy 30:6",
            "text": "And the LORD your God will circumcise your heart and the heart of your offspring, so that you will love the LORD your God with all your heart and with all your soul, that you may live.",
            "translation": "ESV"
        },

        "hebrew_terms": ["teshuvah", "shuv", "milat_halev", "chayyim", "mavet", "bachar", "shamayim_vaarets"],

        "hebrew_glossary": {
            "teshuvah": "Repentance / return (from the verb shuv — a physical and spiritual turning; teshuvah means both returning to the land from exile and returning to YHWH from apostasy; it is the central concept of Jewish repentance theology)",
            "shuv": "Return / turn back / repent (used seven times in Deut 30:1-10, creating a 'return' motif — Israel turns back to YHWH, and YHWH turns Israel's fortunes back; the repetition emphasizes that restoration is a mutual turning)",
            "milat_halev": "Circumcision of the heart (the internal transformation God promises to perform — 10:16 commands Israel to circumcise their own hearts, but they cannot; 30:6 promises that God will do it FOR them; this is the embryonic form of the new covenant of Jeremiah 31:31-34)",
            "chayyim": "Life (not merely biological existence but covenant flourishing — in 30:20, 'he is your life': YHWH himself IS Israel's life; to choose YHWH is to choose existence itself)",
            "mavet": "Death (not merely biological death but covenant separation from the source of life — choosing 'other gods' is choosing death because it means leaving the only God who sustains life)",
            "bachar": "Choose (the climactic imperative of the Torah: 'choose life' — God sets the choice before Israel, but the choice must be made; the entire book of Deuteronomy builds to this single verb)",
            "shamayim_vaarets": "Heaven and earth (the cosmic treaty witnesses — in ANE treaties, the gods of both parties witnessed the covenant; Israel's covenant has no gods as witnesses because the only God is a party to the treaty; instead, heaven and earth themselves serve as eternal witnesses)"
        },

        "ane_backdrop": "Restoration oracles following curse sequences are found in some ANE treaties, "
                        "though rarely with the theological depth of Deuteronomy 30. The concept of "
                        "divine transformation of the human heart has no known ANE parallel — the gods "
                        "of Mesopotamia demanded obedience but did not promise to create the capacity "
                        "for it. The 'choose life' formula (30:19) parallels ANE treaty conclusions "
                        "where the vassal is urged to choose compliance. The invocation of 'heaven and "
                        "earth' as witnesses (30:19) mirrors the treaty witness formula, where both "
                        "parties' gods, plus natural features, were called to witness the covenant.",

        "second_temple": [
            {
                "source": "Jeremiah 31:31-34",
                "summary": "The 'new covenant' promise: 'I will put my law within them, and I will "
                           "write it on their hearts' — the prophetic development of Deut 30:6.",
                "relevance": "Jeremiah takes the embryonic promise of Deut 30:6 and develops it into "
                             "the full new covenant vision that Jesus inaugurates at the Last Supper."
            },
            {
                "source": "Ezekiel 36:26-27",
                "summary": "'I will give you a new heart, and a new spirit I will put within you. "
                           "And I will remove the heart of stone from your flesh and give you a heart "
                           "of flesh. And I will put my Spirit within you.'",
                "relevance": "Ezekiel amplifies Deut 30:6's heart-circumcision with the language of "
                             "Spirit-indwelling — the mechanism by which God transforms the heart."
            },
            {
                "source": "Romans 10:6-8",
                "summary": "Paul applies Deut 30:12-14 christologically: 'The word is near you, in "
                           "your mouth and in your heart' — that is, the word of faith that we proclaim.",
                "relevance": "Paul reads Deut 30's accessibility of the commandment as pointing to "
                             "Christ: the Word made near through the incarnation, accessible through "
                             "faith."
            }
        ],

        "cross_refs": [
            {"ref": "Jeremiah 31:31-34", "note": "The new covenant: law written on hearts — fulfilling Deut 30:6", "type": "ot"},
            {"ref": "Ezekiel 36:26-27", "note": "New heart, new spirit, indwelling Spirit — the mechanism of Deut 30:6", "type": "ot"},
            {"ref": "Romans 10:6-8", "note": "Paul's christological reading of Deut 30:12-14: the word of faith is near", "type": "nt"},
            {"ref": "Romans 2:28-29", "note": "Circumcision of the heart, by the Spirit — fulfilling Deut 30:6", "type": "nt"},
            {"ref": "Acts 2:1-41", "note": "Pentecost: the Spirit poured out on all flesh — the Deut 30:6 promise realized", "type": "nt"},
            {"ref": "Philippians 3:3", "note": "'We are the circumcision, who worship by the Spirit of God' — Deut 30:6 fulfilled in Christ", "type": "nt"},
            {"ref": "Joshua 24:15", "note": "'Choose this day whom you will serve' — echoing Deut 30:19", "type": "ot"},
            {"ref": "Revelation 22:17", "note": "'Let the one who desires take the water of life without price' — the ultimate 'choose life'", "type": "nt"}
        ],

        "divine_council_note": "Deuteronomy 30 is the divine answer to the divine council problem. "
                               "The allotment of nations to the 'sons of God' (32:8-9) created a cosmic "
                               "political reality where the nations were governed by lesser 'elohim who "
                               "failed in their mandate (Psalm 82). Israel, under YHWH's direct rule, "
                               "also failed — the curses of chapter 28 prove it. The solution is not "
                               "external (better laws, more prophets) but internal: God will circumcise "
                               "the heart (30:6). This is the embryonic form of what Paul calls the 'new "
                               "creation' (2 Cor 5:17) and what Ezekiel describes as the Spirit-indwelt "
                               "heart (Ezek 36:26-27). The divine council crisis — rebellious 'elohim, "
                               "rebellious Israel, a broken cosmos — is solved by divine transformation "
                               "of the human agent. And this transformation is not limited to Israel: "
                               "Paul reads Deut 30:12-14 as pointing to Christ (Rom 10:6-8), who brings "
                               "the 'word of faith' to all nations. The Great Commission (Matt 28:18-20) "
                               "is the reversal of the Deuteronomy 32 allotment, and the Spirit poured "
                               "out at Pentecost (Acts 2) is the fulfillment of Deuteronomy 30:6 — "
                               "heart-circumcision for all peoples, not just Israel.",

        "sections": [
            {
                "heading": "Restoration After Exile (30:1-5)",
                "body": "Moses prophesies beyond the curse: 'When all these things come upon you, "
                        "the blessing and the curse that I have set before you, and you call them to "
                        "mind among all the nations where the LORD your God has driven you, and return "
                        "(shuv) to the LORD your God' (30:1-2). The verb shuv ('return/repent') is "
                        "the key — it means both physical return to the land and spiritual return to "
                        "YHWH. God's response is immediate and comprehensive: 'the LORD your God will "
                        "restore your fortunes and have mercy on you, and he will gather you again "
                        "from all the peoples where the LORD your God has scattered you' (30:3). Even "
                        "'if your outcasts are in the uttermost parts of heaven, from there the LORD "
                        "your God will gather you' (30:4). God will bring them to 'the land that your "
                        "fathers possessed, and you shall possess it. And he will make you more "
                        "prosperous and numerous than your fathers' (30:5). Restoration exceeds the "
                        "original state — more prosperous, more numerous. Grace surpasses judgment."
            },
            {
                "heading": "The Circumcision of the Heart (30:6-10)",
                "body": "The theological climax: 'And the LORD your God will circumcise your heart and "
                        "the heart of your offspring, so that you will love the LORD your God with all "
                        "your heart and with all your soul, that you may live' (30:6). In 10:16, Moses "
                        "commanded Israel to circumcise their own hearts. They couldn't do it — 29:4 "
                        "admitted they lacked the heart to understand. Now God promises to do it FOR "
                        "them. This is the new covenant in seed form: the same internal transformation "
                        "that Jeremiah 31 and Ezekiel 36 will develop in full. The result of divine "
                        "heart-surgery is that Israel WILL love God with all their heart and soul — "
                        "the Shema (6:5) finally fulfilled, not by human effort but by divine "
                        "intervention. The curse transfers to Israel's enemies (30:7), and Israel "
                        "'will again obey the voice of the LORD and keep all his commandments' (30:8). "
                        "Obedience becomes possible because God has changed the heart. This is the "
                        "most important theological promise in the Torah: the God who demands heart-love "
                        "will create the capacity for heart-love."
            },
            {
                "heading": "The Word Is Near — Not Too Hard, Not Too Far (30:11-14)",
                "body": "Moses counters the objection that the commandment is inaccessible: 'For this "
                        "commandment that I command you today is not too hard for you, neither is it "
                        "far off. It is not in heaven, that you should say, \"Who will ascend to "
                        "heaven for us and bring it to us?\" Neither is it beyond the sea, that you "
                        "should say, \"Who will go over the sea for us and bring it to us?\"' (30:11-13). "
                        "The word is not hidden in the heavenly council, not locked behind cosmic "
                        "barriers. 'But the word is very near you. It is in your mouth and in your "
                        "heart, so that you can do it' (30:14). Paul's christological reading in "
                        "Romans 10:6-8 is remarkable: he identifies the 'word' with Christ himself — "
                        "'Who will ascend to heaven?' (that is, to bring Christ down) and 'Who will "
                        "descend into the abyss?' (that is, to bring Christ up from the dead). For "
                        "Paul, the 'word near you' IS the incarnate Word. The commandment's "
                        "accessibility in Moses points forward to Christ's accessibility in the gospel."
            },
            {
                "heading": "Choose Life (30:15-20)",
                "body": "The covenant choice is presented with absolute clarity: 'See, I have set "
                        "before you today life and good, death and evil' (30:15). If Israel loves "
                        "YHWH, walks in his ways, and keeps his commandments: 'then you shall live "
                        "and multiply, and the LORD your God will bless you' (30:16). If Israel turns "
                        "away and serves other gods: 'you shall surely perish. You shall not live long "
                        "in the land' (30:18). Then the climactic appeal: 'I call heaven and earth to "
                        "witness against you today, that I have set before you life and death, blessing "
                        "and curse. Therefore choose life, that you and your offspring may live, loving "
                        "the LORD your God, obeying his voice and holding fast to him, for he is your "
                        "life and length of days' (30:19-20). The witnesses are heaven and earth — the "
                        "treaty's cosmic attestors, replacing the gods of both parties in ANE treaties. "
                        "'He is your life' (hu chayyekha) — YHWH himself is not just the source of "
                        "life but IS Israel's life. The identification of God with life itself is the "
                        "deepest theology in Deuteronomy. To choose YHWH is to choose existence; to "
                        "reject him is to choose death — not as punishment but as ontological reality."
            }
        ]
    }
]
