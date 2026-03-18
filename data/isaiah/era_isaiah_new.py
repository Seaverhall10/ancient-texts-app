"""
era_isaiah_new.py -- The New Creation Vision (Isaiah 56-66)

Third Isaiah (Trito-Isaiah) moves from the comfort of exile to the vision of
cosmic renewal. These chapters open with a radical inclusivity -- foreigners
and eunuchs welcomed into YHWH's covenant -- and close with the most
comprehensive vision of new creation in the Hebrew Bible: new heavens and a
new earth (65:17; 66:22). Between these bookends, the Divine Warrior treads
the winepress alone (63:1-6), the remnant prays the most desperate prayer
in the prophetic corpus (63:7-64:12), and YHWH announces the final judgment
that separates his servants from those who forsake him. Isaiah 61:1-2 --
"The Spirit of the Lord GOD is upon me" -- is the text Jesus reads in the
Nazareth synagogue (Luke 4:16-21), declaring its fulfillment in his own
person. The section climaxes with the restoration of the original cosmic
order: the wolf and the lamb feed together (65:25), new heavens and new
earth replace the old (65:17), and "all flesh" comes to worship before YHWH
(66:23). This is not escapism but transformation -- the earth itself is
redeemed.
"""

CHAPTERS = [
    {
        "id": "isa-56-57",
        "ref": "Isaiah 56-57",
        "chapter_num": 1,
        "title": "The Universal Invitation and Corrupt Leaders",
        "era": "isaiah_new",
        "type": "chapter",
        "themes": ["COV", "HOLY", "NATIONS"],

        "synopsis": "Isaiah 56 opens Third Isaiah with one of the most radical declarations in the "
                    "Hebrew Bible: the covenant is thrown open to those previously excluded. 'Thus says "
                    "YHWH: Keep justice (mishpat), and do righteousness (tsedaqah), for soon my salvation "
                    "(yeshu'ati) will come, and my righteousness (tsidqati) be revealed' (56:1). The "
                    "foreigners (ben-nekar) who join themselves to YHWH need no longer say 'YHWH will "
                    "surely separate me from his people,' and the eunuch (saris) need no longer say "
                    "'Behold, I am a dry tree' (56:3). Both classes were excluded under the Deuteronomic "
                    "law (Deut 23:1-8), yet YHWH now declares: 'To the eunuchs who keep my Sabbaths, "
                    "who choose the things that please me and hold fast my covenant, I will give in my "
                    "house and within my walls a monument (yad) and a name (shem) better than sons and "
                    "daughters; I will give them an everlasting name (shem olam) that shall not be cut "
                    "off' (56:4-5). The eunuch, who has no biological posterity, receives something "
                    "greater: a permanent memorial in YHWH's own house. The foreigners are likewise "
                    "welcomed: 'These I will bring to my holy mountain, and make them joyful in my house "
                    "of prayer; their burnt offerings and their sacrifices will be accepted on my altar, "
                    "for my house shall be called a house of prayer for all peoples (kol-ha'ammim)' "
                    "(56:7). Jesus quotes this verse when he cleanses the temple (Mark 11:17). Then the "
                    "tone shifts sharply: Israel's leaders are condemned as blind watchmen, dumb dogs "
                    "that cannot bark, shepherds without understanding who 'have all turned to their own "
                    "way, each to his own gain' (56:11). Chapter 57 continues the indictment: the "
                    "righteous perish and no one cares (57:1), while the people practice fertility "
                    "religion -- 'inflaming yourselves among the oaks (elim), under every green tree, "
                    "slaughtering children in the valleys' (57:5). The chapter identifies a critical "
                    "spiritual condition: 'Your iniquities (avonotekhem) have made a separation between "
                    "you and your God, and your sins have hidden his face from you so that he does not "
                    "hear' (59:2, thematically echoed here). Yet the chapter ends with the extraordinary "
                    "promise of YHWH dwelling in two places simultaneously: 'I dwell in the high and "
                    "holy place (marom veqadosh), and also with him who is of a contrite and lowly "
                    "spirit (dakka ushfal-ruach)' (57:15). The transcendent God who inhabits eternity "
                    "also inhabits the broken heart.",

        "key_verse": {
            "ref": "Isaiah 56:7",
            "text": "These I will bring to my holy mountain, and make them joyful in my house of prayer; their burnt offerings and their sacrifices will be accepted on my altar, for my house shall be called a house of prayer for all peoples.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ben-nekar (son of the foreigner -- a non-Israelite who joins YHWH's covenant)",
            "saris (eunuch -- one excluded under Deut 23:1 but now welcomed by YHWH's grace)",
            "yad vashem (a monument and a name -- the memorial given to the eunuch; this phrase became the name of Israel's Holocaust memorial)",
            "beit tefillah (house of prayer -- YHWH's temple as a universal worship center)",
            "kol-ha'ammim (all peoples -- the universal scope of YHWH's house)",
            "tsophim (watchmen -- Israel's leaders who were supposed to guard and warn but have failed)",
            "marom veqadosh (the high and holy place -- YHWH's transcendent dwelling)",
            "dakka ushfal-ruach (contrite and lowly of spirit -- the broken heart YHWH inhabits)"
        ],

        "ane_backdrop": "The inclusion of eunuchs and foreigners reverses specific ANE cultic restrictions. "
                        "In Mesopotamian temple practice, physical wholeness was required for cultic service -- "
                        "the Babylonian priesthood excluded those with physical defects, paralleling the "
                        "Levitical requirements of Leviticus 21:17-23. Eunuchs served extensively in ANE "
                        "royal courts (the Assyrian and Babylonian empires employed large numbers as officials), "
                        "but they were marginalized in cultic contexts because their inability to procreate "
                        "was seen as a form of incompleteness. The Hebrew term saris may derive from the "
                        "Akkadian sha reshi ('he of the head,' i.e., a court official). Isaiah's reversal "
                        "of these exclusions is theologically revolutionary: YHWH values covenant loyalty "
                        "over physical status. The condemnation of 'slaughtering children in the valleys' "
                        "(57:5) refers to the practice of child sacrifice in the Valley of Hinnom (ge-hinnom, "
                        "later Gehenna), attested archaeologically at Tophet sites in the Levant.",

        "second_temple": [
            {
                "source": "Mark 11:17",
                "summary": "Jesus cleanses the temple and declares: 'Is it not written, My house shall be "
                           "called a house of prayer for all the nations? But you have made it a den of "
                           "robbers.'",
                "relevance": "Jesus quotes Isaiah 56:7 directly, condemning the temple authorities for "
                             "violating YHWH's intention that the temple serve all nations -- the same "
                             "universal vision Third Isaiah proclaims."
            },
            {
                "source": "Acts 8:26-39",
                "summary": "Philip encounters the Ethiopian eunuch reading Isaiah on the road from "
                           "Jerusalem. The eunuch -- a foreigner and a eunuch -- is baptized and becomes "
                           "one of the first non-Jewish converts.",
                "relevance": "The Ethiopian eunuch is the living fulfillment of Isaiah 56:3-5: a foreigner "
                             "and a eunuch welcomed into YHWH's covenant community through Christ."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 23:1-8", "note": "The exclusion laws for eunuchs and certain foreigners that Isaiah 56 now overturns", "type": "ot"},
            {"ref": "Mark 11:17", "note": "Jesus quotes 56:7 when cleansing the temple -- 'a house of prayer for all nations'", "type": "nt"},
            {"ref": "Acts 8:26-39", "note": "The Ethiopian eunuch baptized -- the fulfillment of 56:3-5's inclusive vision", "type": "nt"},
            {"ref": "Ezekiel 34:1-10", "note": "Ezekiel's indictment of false shepherds -- the same theme as 56:10-12", "type": "ot"},
            {"ref": "Psalm 51:17", "note": "'A broken and contrite heart, O God, you will not despise' -- the same theology as 57:15", "type": "ot"},
            {"ref": "John 4:21-24", "note": "Jesus tells the Samaritan woman that true worshipers worship in spirit and truth -- extending the universal worship of 56:7", "type": "nt"},
            {"ref": "Ephesians 2:13-14", "note": "'You who once were far off have been brought near by the blood of Christ' -- the foreigner welcomed", "type": "nt"}
        ],

        "divine_council_note": "Isaiah 56's universal inclusion directly addresses the Deuteronomy 32:8-9 "
                               "framework. Under the original allotment, the nations were given to the sons "
                               "of God while YHWH kept Israel as his nachalah (inheritance). The foreigners "
                               "who 'join themselves to YHWH' (56:3, 6) are leaving the governance of their "
                               "allotted elohim and attaching themselves to the Most High. This is not merely "
                               "a humanitarian gesture but a cosmic realignment: the boundaries of Deuteronomy "
                               "32 are being dissolved as YHWH reclaims the nations. The eunuch, who was "
                               "excluded from the qahal (assembly) of YHWH under Deuteronomic law, receives "
                               "a yad vashem ('monument and name') in YHWH's own house -- a permanent memorial "
                               "in the divine King's palace. The condemnation of Israel's leaders as 'blind "
                               "watchmen' (tsophim ivrim, 56:10) echoes the failure of the divine council "
                               "members in Psalm 82: those entrusted with YHWH's governance have failed in "
                               "their duty. The remarkable declaration of 57:15 -- that YHWH dwells both in "
                               "'the high and holy place' (the divine council throne room) and with 'the "
                               "contrite and lowly of spirit' -- bridges heaven and earth, anticipating the "
                               "incarnation.",

        "sections": [
            {
                "heading": "The Foreigner and the Eunuch Welcomed (56:1-8)",
                "body": "'Keep mishpat (justice), and do tsedaqah (righteousness), for soon my yeshu'ah "
                        "(salvation) will come' (56:1). The imperative precedes the promise: justice is "
                        "both the precondition and the fruit of salvation. The ben-nekar ('son of the "
                        "foreigner') and the saris (eunuch) -- both excluded under Deuteronomy 23 -- are "
                        "now explicitly welcomed. The conditions are not ethnic or physical but covenantal: "
                        "'the eunuchs who keep my Sabbaths, who choose the things that please me and hold "
                        "fast my covenant' (56:4). Sabbath-keeping functions as the covenant marker: it "
                        "identifies those who belong to YHWH regardless of their national or physical "
                        "status. The eunuch's reward transcends biology: 'I will give them in my house "
                        "and within my walls a yad vashem (monument and name) better than sons and "
                        "daughters' (56:5). The yad ('hand/monument') is a permanent marker; the shem "
                        "('name') is identity preserved forever. For the foreigner: 'I will bring them "
                        "to my holy mountain and make them joyful in my beit tefillah (house of prayer). "
                        "Their olot (burnt offerings) and zevachim (sacrifices) will be accepted (lirratson) "
                        "on my altar' (56:7). The verb ratsah ('to accept, to be pleased with') is the "
                        "technical term for acceptable sacrifice (Lev 1:3-4). YHWH accepts the worship of "
                        "foreigners as fully as that of Israelites. 'For my house shall be called a beit "
                        "tefillah le-kol-ha'ammim -- a house of prayer for all peoples' (56:7b). The "
                        "declaration 'Adonai YHWH, who gathers the outcasts (nidchei) of Israel, declares: "
                        "I will gather yet others to him besides those already gathered' (56:8). The "
                        "gathering extends beyond Israel's diaspora to include the nations."
            },
            {
                "heading": "Blind Watchmen and False Shepherds (56:9-57:2)",
                "body": "The indictment of Israel's leaders follows immediately after the universal "
                        "invitation, creating a devastating contrast. 'His watchmen (tsophav) are blind "
                        "(ivrim); they are all without knowledge (lo yadu); they are all silent dogs (kelavim "
                        "illemim) that cannot bark (linboach); dreaming, lying down, loving to slumber' "
                        "(56:10). The tsopheh ('watchman') was the prophetic function -- the sentinel on "
                        "the wall who saw danger and warned the people (cf. Ezek 3:17; 33:7). These "
                        "watchmen are blind and mute: they cannot see the approaching threat and cannot "
                        "sound the alarm. 'The dogs have a mighty appetite (nafsham); they never have "
                        "enough. But they are shepherds (ro'im) who have no understanding (havin); they "
                        "have all turned to their own way (darko), each to his own gain (betsa'o)' "
                        "(56:11). The shepherds who should feed the flock feed only themselves -- the same "
                        "indictment Ezekiel levels in chapter 34. Meanwhile, 'the righteous man (tsaddiq) "
                        "perishes, and no one lays it to heart; devout men (anshei-chesed) are taken away, "
                        "while no one understands. The righteous man is taken away from calamity; he "
                        "enters into peace (shalom)' (57:1-2). The death of the righteous is both judgment "
                        "on the community that ignores their loss and mercy on the righteous themselves -- "
                        "they are spared the coming disaster."
            },
            {
                "heading": "Idolatry Condemned and the Contrite Heart Exalted (57:3-21)",
                "body": "The accusation is savage: 'But you, draw near, sons of the sorceress (ananah), "
                        "offspring of the adulterer and the loose woman' (57:3). The people are 'inflaming "
                        "yourselves among the oaks (elim), under every green tree, slaughtering (shochatei) "
                        "children (yeladim) in the valleys (nachalim), under the clefts of the rocks' "
                        "(57:5). The word elim ('oaks') creates a deliberate pun with elim ('gods') -- the "
                        "people worship among the trees and among the gods simultaneously. Child sacrifice "
                        "is the ultimate abomination -- the life YHWH gives is offered to beings who are "
                        "not God. 'On a high (gavoah) and lofty (nissa) mountain you have set your bed' "
                        "(57:7) -- the 'high places' (bamot) of Canaanite worship. But then the oracle "
                        "pivots to grace: 'For thus says the High (ram) and Lofty One (nissa) who inhabits "
                        "eternity (shokhen ad), whose name is Holy (qadosh): I dwell in the high and holy "
                        "place, and also with him who is of a contrite (dakka) and lowly (shfal) spirit "
                        "(ruach), to revive the spirit of the lowly, and to revive the heart of the "
                        "contrite' (57:15). YHWH's self-description uses the same words -- ram venissa "
                        "('high and lifted up') -- applied to his throne in 6:1 and to the Servant in "
                        "52:13. He inhabits eternity and simultaneously inhabits the broken heart. 'For I "
                        "will not contend forever, nor will I always be angry; for the spirit (ruach) would "
                        "grow faint before me, and the breath (neshamot) that I have made' (57:16). YHWH's "
                        "anger has a limit, because he is the source of life itself. But the wicked have no "
                        "peace: 'There is no shalom, says my God, for the wicked (resha'im)' (57:21)."
            }
        ]
    },

    {
        "id": "isa-58-59",
        "ref": "Isaiah 58-59",
        "chapter_num": 2,
        "title": "True Fasting, Sin's Separation, and the Redeemer Comes to Zion",
        "era": "isaiah_new",
        "type": "chapter",
        "themes": ["RIV", "BLOOD", "SPIRIT"],

        "synopsis": "Isaiah 58 confronts the hypocrisy of religious observance divorced from justice -- "
                    "the same theme sounded in chapter 1. The people 'seek me daily and delight to know "
                    "my ways, as if they were a nation that did righteousness' (58:2). They fast and "
                    "afflict themselves, yet wonder why YHWH does not respond: 'Why have we fasted, and "
                    "you see it not?' (58:3). YHWH's answer is devastating: their fasting is accompanied "
                    "by exploitation -- 'you fast only to quarrel and to fight and to hit with a wicked "
                    "fist' (58:4). The fast YHWH chooses is social justice: 'to loose the bonds of "
                    "wickedness, to undo the straps of the yoke, to let the oppressed go free... to share "
                    "your bread with the hungry and bring the homeless poor into your house' (58:6-7). "
                    "When this fast is practiced, 'your light shall break forth like the dawn, and your "
                    "healing shall spring up speedily' (58:8). Chapter 59 then diagnoses the root problem: "
                    "'Your iniquities (avonotekhem) have made a separation (mavdilim) between you and "
                    "your God, and your sins have hidden his face from you so that he does not hear' "
                    "(59:2). The confession is collective: 'Our transgressions are multiplied before you, "
                    "and our sins testify against us' (59:12). Justice is absent: 'Truth (emet) has "
                    "stumbled in the public square (ba-rechov), and uprightness (nekhochah) cannot enter' "
                    "(59:14). YHWH sees that there is no justice and no intercessor, so he acts himself: "
                    "'He put on righteousness (tsedaqah) as a breastplate, and a helmet of salvation "
                    "(yeshu'ah) on his head; he put on garments of vengeance (naqam) for clothing, and "
                    "wrapped himself in zeal (qin'ah) as a cloak' (59:17). This is the Divine Warrior "
                    "arming for battle -- the source text for Paul's 'armor of God' in Ephesians 6:14-17. "
                    "The chapter concludes with the promise: 'A Redeemer (Go'el) will come to Zion, to "
                    "those in Jacob who turn from transgression' (59:20).",

        "key_verse": {
            "ref": "Isaiah 59:17",
            "text": "He put on righteousness as a breastplate, and a helmet of salvation on his head; he put on garments of vengeance for clothing, and wrapped himself in zeal as a cloak.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tsom (fast -- the religious observance YHWH redefines as social justice)",
            "mavdilim (making a separation -- sin as the barrier between God and humanity)",
            "emet (truth/faithfulness -- the quality that has fallen in the public square)",
            "Go'el (Redeemer/kinsman-redeemer -- this is NOT simply a synonym for 'savior.' In Israelite law, the go'el was a specific legal role: the nearest male relative who was obligated to (1) buy back family land that had been sold due to poverty (Lev 25:25), (2) redeem a relative sold into slavery (Lev 25:47-49), (3) avenge the blood of a murdered kinsman (Num 35:19-21), and (4) marry a deceased relative's widow to preserve his family line (Ruth 3-4). When YHWH calls himself Israel's Go'el, he is claiming the role of nearest kinsman -- the one who will buy back what was lost, avenge what was done, and restore the broken family. It is one of the most intimate titles YHWH uses for himself)",
            "tsedaqah (righteousness -- the breastplate of the Divine Warrior)",
            "yeshu'ah (salvation -- the helmet of the Divine Warrior)",
            "naqam (vengeance -- not personal vindictiveness but righteous retribution)",
            "qin'ah (zeal/jealousy -- the passionate intensity of YHWH's commitment)",
            "maphgia (intercessor -- the one who intervenes; none is found, so YHWH acts)"
        ],

        "ane_backdrop": "Fasting as a religious practice is well attested across the ANE. Mesopotamian "
                        "texts describe ritual fasting before the gods to avert divine anger or procure "
                        "oracles. The Babylonian Day of Atonement (Akitu festival, Day 5) included "
                        "penitential rites and humiliation of the king. In Egypt, fasting accompanied "
                        "mourning rituals and prophetic consultation. Isaiah 58's radical redefinition of "
                        "fasting as social justice has no ANE parallel -- other cultures understood fasting "
                        "as affecting the gods through self-denial, but Isaiah declares that YHWH is "
                        "affected by how one treats other human beings. The Divine Warrior imagery of "
                        "59:17 draws on the widespread ANE motif of the warrior-god arming for combat "
                        "(cf. Marduk arming to fight Tiamat in the Enuma Elish), but Isaiah applies it "
                        "to YHWH's battle against injustice itself.",

        "second_temple": [
            {
                "source": "Ephesians 6:14-17",
                "summary": "Paul describes the 'armor of God': the belt of truth, breastplate of "
                           "righteousness, shoes of the gospel, shield of faith, helmet of salvation, "
                           "and the sword of the Spirit.",
                "relevance": "Paul's spiritual armor is directly adapted from Isaiah 59:17. The armor "
                             "YHWH puts on in Isaiah becomes the armor believers wear in Ephesians -- "
                             "because the church participates in the Divine Warrior's battle."
            },
            {
                "source": "1 Thessalonians 5:8",
                "summary": "'Let us put on the breastplate of faith and love, and for a helmet the "
                           "hope of salvation.'",
                "relevance": "Another Pauline adaptation of Isaiah 59:17, confirming that the Divine "
                             "Warrior imagery shapes New Testament spiritual warfare theology."
            },
            {
                "source": "Romans 11:26-27",
                "summary": "Paul quotes Isaiah 59:20-21: 'The Deliverer will come from Zion, he will "
                           "banish ungodliness from Jacob.'",
                "relevance": "Paul applies the Redeemer's coming to Zion to Christ's eschatological "
                             "mission -- the Go'el of Isaiah 59:20 is Jesus."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 1:11-17", "note": "The same theme: YHWH rejects worship divorced from justice -- 'learn to do good; seek justice'", "type": "ot"},
            {"ref": "Micah 6:6-8", "note": "'What does the LORD require of you but to do justice, love kindness, and walk humbly?' -- the same fast YHWH chooses", "type": "ot"},
            {"ref": "Ephesians 6:14-17", "note": "Paul's 'armor of God' directly adapted from the Divine Warrior's armor in 59:17", "type": "nt"},
            {"ref": "Romans 11:26-27", "note": "Paul quotes 59:20 -- 'The Deliverer will come from Zion' -- applied to Christ", "type": "nt"},
            {"ref": "Romans 3:10-18", "note": "Paul quotes 59:7-8 in his indictment of universal human sinfulness -- 'their feet are swift to shed blood'", "type": "nt"},
            {"ref": "1 John 1:9", "note": "'If we confess our sins, he is faithful and just to forgive us' -- the New Testament resolution of the sin-separation of 59:2", "type": "nt"},
            {"ref": "Matthew 25:35-40", "note": "'I was hungry and you gave me food' -- the true fasting of Isaiah 58 fulfilled in care for the least", "type": "nt"}
        ],

        "divine_council_note": "Isaiah 59 presents a crisis within the divine economy: YHWH looks for an "
                               "intercessor (maphgia, 59:16) and finds none. The same term maphgia appears "
                               "in 53:12, where the Servant 'makes intercession for the transgressors.' The "
                               "absence of an intercessor in chapter 59 is resolved by the presence of the "
                               "Servant in chapter 53 -- and by YHWH himself arming for battle in 59:17. "
                               "When no council member, no prophet, no human mediator can bridge the gap "
                               "between YHWH and his sinful people, YHWH's own arm 'brought him salvation' "
                               "(59:16). The Divine Warrior putting on armor (59:17) is YHWH doing what his "
                               "council members and his people have failed to do: establishing justice on "
                               "earth. The Go'el ('Redeemer') who comes to Zion (59:20) is YHWH himself in "
                               "his warrior-redeemer role -- the same Go'el theology from Ruth and Job now "
                               "applied cosmically. Paul's adaptation of this armor for believers (Eph 6) "
                               "implies that the church participates in YHWH's divine warrior mission.",

        "sections": [
            {
                "heading": "The Fast YHWH Chooses: Justice, Not Ritual (58:1-12)",
                "body": "'Cry aloud (qera begaron); do not hold back; lift up your voice like a shofar' "
                        "(58:1). The prophet is commanded to announce Israel's sins with the volume and "
                        "urgency of a trumpet blast. The people perform religious devotion: 'they seek "
                        "me daily (yom yom yidreshun) and delight (yechpatsun) to know my ways, as if "
                        "(ke-goy) they were a nation that did righteousness' (58:2). The devastating "
                        "phrase ke-goy ('as if they were a nation') implies they are not what they appear. "
                        "Their complaint: 'Why have we fasted (tsamnu), and you see it not? Why have we "
                        "afflicted ourselves (inninu nafshenu), and you take no knowledge of it?' (58:3a). "
                        "YHWH's answer: 'In the day of your fast you seek your own pleasure (chephets), "
                        "and oppress all your workers' (58:3b). The fast YHWH chooses is defined: 'Is it "
                        "not to loose the bonds of wickedness (chartsuvbot resha), to undo the straps of "
                        "the yoke (aguddot motah), to let the oppressed go free (shalach retsutsim "
                        "chophshim), and to break every yoke?' (58:6). Four commands, all about liberation. "
                        "'Is it not to share your bread (lachmekha) with the hungry (ra'ev) and bring "
                        "the homeless poor (aniyim merudim) into your house?' (58:7). When this fast is "
                        "practiced, the restoration is immediate: 'Then shall your light break forth like "
                        "the dawn (sha'char), and your healing (arukhatekha) shall spring up speedily; "
                        "your righteousness shall go before you; the kevod (glory) of YHWH shall be your "
                        "rear guard' (58:8). (The Hebrew word kavod, often translated &lsquo;glory,&rsquo; "
                        "literally means &lsquo;weight&rsquo; or &lsquo;heaviness.&rsquo; When applied to YHWH, "
                        "it refers to his manifest, radiant presence &mdash; the visible expression of his "
                        "being. This is the same luminous cloud that filled the Tabernacle (Exod 40:34), "
                        "settled on Sinai (Exod 24:16-17), and will later depart the Temple before its "
                        "destruction (Ezek 10-11). Kavod is not an abstract quality like &lsquo;fame&rsquo; "
                        "&mdash; it is God&rsquo;s tangible, weighty, overwhelming presence.) YHWH&rsquo;s "
                        "kavod accompanies those who practice justice."
            },
            {
                "heading": "Sin's Separation and the Collapse of Truth (59:1-15a)",
                "body": "'Behold, the hand (yad) of YHWH is not shortened (qatsrah), that it cannot save, "
                        "nor his ear (ozno) heavy (khavedah), that it cannot hear' (59:1). The problem is "
                        "not divine inability but human sin. 'Your iniquities (avonotekhem) have made a "
                        "separation (mavdilim) between you and your God, and your sins (chatoteikhem) have "
                        "hidden his face (panim) from you so that he does not hear' (59:2). The verb "
                        "mavdilim ('making a separation') uses the same root as the creation separations "
                        "of Genesis 1 (mavdil) -- sin un-creates, reverses the ordering work of God. "
                        "The catalog of sins is comprehensive: 'your hands are defiled (nego'alu) with "
                        "blood, and your fingers with iniquity; your lips have spoken lies, your tongue "
                        "mutters wickedness' (59:3). No one calls for justice: 'they trust in emptiness "
                        "(tohu) and speak vanity (shav)' (59:4) -- the same tohu of Genesis 1:2, the "
                        "primordial chaos. The moral collapse is total: 'Truth (emet) has stumbled in "
                        "the public square (rechov), and uprightness (nekhochah) cannot enter' (59:14). "
                        "Emet -- faithfulness, reliability, truth itself -- lies prostrate in the street. "
                        "'Whoever departs from evil makes himself a prey (mishtollel)' (59:15a). In a "
                        "society this corrupt, the righteous person becomes the victim."
            },
            {
                "heading": "The Divine Warrior Arms and the Redeemer Comes (59:15b-21)",
                "body": "YHWH sees the injustice and responds personally: 'He saw that there was no man "
                        "(ish), and wondered (yishtomem) that there was no one to intercede (maphgia)' "
                        "(59:16a). The word maphgia ('intercessor, one who intervenes') echoes the Servant "
                        "of 53:12 who 'makes intercession (yaphgia) for the transgressors.' Here, no "
                        "intercessor exists -- so 'his own arm (zero'o) brought him salvation, and his "
                        "righteousness upheld him' (59:16b). YHWH acts unilaterally. The arming scene: "
                        "'He put on tsedaqah (righteousness) as a breastplate (shiryon), and a helmet "
                        "(kova) of yeshu'ah (salvation) on his head; he put on garments (bigdei) of naqam "
                        "(vengeance) for clothing, and wrapped himself in qin'ah (zeal) as a cloak "
                        "(me'il)' (59:17). Four pieces of armor, each a divine attribute: righteousness "
                        "protects the heart, salvation guards the mind, vengeance covers the body, and "
                        "zeal wraps the whole. Paul will adapt this for believers in Ephesians 6:14-17, "
                        "replacing vengeance with the gospel of peace and adding the shield of faith and "
                        "the sword of the Spirit. 'According to their deeds, accordingly he will repay: "
                        "wrath (chemah) to his adversaries, retribution (gemul) to his enemies; to the "
                        "coastlands (iyyim) he will render recompense' (59:18). The judgment is universal. "
                        "'So they shall fear the name of YHWH from the west, and his glory from the "
                        "rising of the sun' (59:19). Then the climactic promise: 'A Go'el (Redeemer) will "
                        "come to Zion, to those in Jacob who turn from transgression (pesha), declares "
                        "YHWH' (59:20). The Go'el is the kinsman-redeemer -- the nearest relative who "
                        "avenges blood, redeems property, and restores family honor (cf. Ruth 3-4; Job "
                        "19:25). YHWH himself is Israel's Go'el, coming to his own people."
            }
        ]
    },

    {
        "id": "isa-60-62",
        "ref": "Isaiah 60-62",
        "chapter_num": 3,
        "title": "Arise, Shine! The Glory of Zion and the Year of the LORD's Favor",
        "era": "isaiah_new",
        "type": "chapter",
        "themes": ["GLORY", "SEED", "REVERSAL", "LAND"],

        "synopsis": "These three chapters form the radiant center of Third Isaiah. Chapter 60 opens with "
                    "the command: 'Arise (qumi), shine (ori), for your light (orekh) has come, and the "
                    "glory (kevod) of YHWH has risen (zarach) upon you!' (60:1). While darkness covers the "
                    "earth and thick darkness the peoples, YHWH's glory rises on Zion, and 'nations shall "
                    "come to your light, and kings to the brightness of your rising' (60:3). The wealth of "
                    "the nations streams to Jerusalem: camels from Midian and Ephah, gold and frankincense "
                    "from Sheba (60:6 -- the background for the Magi's gifts in Matthew 2:11). 'Your gates "
                    "shall be open continually; day and night they shall not be shut' (60:11). The sun and "
                    "moon will no longer be needed: 'YHWH will be your everlasting light (or olam), and "
                    "your God will be your glory (tif'artekh)' (60:19). Chapter 61 contains the passage "
                    "Jesus reads in the Nazareth synagogue: 'The Spirit (ruach) of the Lord GOD (Adonai "
                    "YHWH) is upon me, because YHWH has anointed me (mashach oti) to bring good news "
                    "(basar) to the poor (anavim); he has sent me to bind up the brokenhearted (nishberei "
                    "lev), to proclaim liberty (deror) to the captives (shevuyim), and the opening of the "
                    "prison to those who are bound; to proclaim the year of YHWH's favor (shenat ratson "
                    "la-YHWH)' (61:1-2a). In Luke 4:18-21, Jesus reads this text, rolls up the scroll, "
                    "and declares: 'Today this Scripture has been fulfilled in your hearing.' He stops "
                    "mid-sentence, omitting 'the day of vengeance of our God' (61:2b) -- because his first "
                    "coming is the year of favor; the day of vengeance awaits his return. Chapter 62 "
                    "continues the bridal imagery: Zion receives new names -- Hephzibah ('my delight is "
                    "in her') and Beulah ('married') -- replacing the shame of Azuvah ('forsaken') and "
                    "Shemamah ('desolate'). 'As the bridegroom rejoices over the bride, so shall your God "
                    "rejoice over you' (62:5).",

        "key_verse": {
            "ref": "Isaiah 61:1",
            "text": "The Spirit of the Lord GOD is upon me, because the LORD has anointed me to bring good news to the poor; he has sent me to bind up the brokenhearted, to proclaim liberty to the captives, and the opening of the prison to those who are bound.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "qumi ori (arise, shine -- the imperative to Zion personified as a woman)",
            "mashach (to anoint -- the verb from which mashiach/Messiah derives; the speaker of 61:1 is the Anointed One)",
            "basar (to bring good news -- the verb root of besorah, 'gospel/good news')",
            "deror (liberty/release -- the Jubilee term from Leviticus 25:10)",
            "shenat ratson (year of favor -- the acceptable year, the Jubilee of YHWH's grace)",
            "Hephzibah (my delight is in her -- Zion's new name, replacing abandonment)",
            "Beulah (married -- Zion's restored covenant relationship with YHWH)",
            "or olam (everlasting light -- YHWH himself as the light source replacing sun and moon)"
        ],

        "ane_backdrop": "The imagery of nations streaming to a central city carrying tribute is well "
                        "attested in ANE royal propaganda. Egyptian temple reliefs at Karnak and Medinet "
                        "Habu depict processions of conquered peoples bringing gold, incense, and exotic "
                        "goods to Pharaoh. Assyrian palace reliefs show similar tributary processions. "
                        "Isaiah transforms this imperial imagery: the nations come not as conquered peoples "
                        "but as willing worshipers drawn by YHWH's light. The mention of Midian, Ephah, "
                        "and Sheba (60:6) traces the Arabian incense trade routes -- gold and frankincense "
                        "were the premier luxury goods of the ANE. The Jubilee background of 61:1-2 (deror, "
                        "'liberty'; shenat ratson, 'year of favor') draws on Leviticus 25, where every "
                        "fiftieth year brought the release of debts, return of ancestral lands, and "
                        "liberation of slaves. Similar debt-release practices (the Mesopotamian misharum "
                        "and andurarum edicts) are attested in the Old Babylonian period.",

        "second_temple": [
            {
                "source": "Luke 4:16-21",
                "summary": "Jesus reads Isaiah 61:1-2a in the Nazareth synagogue and declares: 'Today "
                           "this Scripture has been fulfilled in your hearing.'",
                "relevance": "This is the definitive christological application of Third Isaiah: Jesus "
                             "identifies himself as the anointed speaker of 61:1 and claims the text is "
                             "fulfilled in his own person and ministry."
            },
            {
                "source": "Matthew 2:11",
                "summary": "The Magi bring gifts of gold, frankincense, and myrrh to the infant Jesus.",
                "relevance": "The Magi's gifts echo Isaiah 60:6 ('they shall bring gold and "
                             "frankincense') -- the nations' tribute streaming to the messianic King."
            },
            {
                "source": "Revelation 21:23-25",
                "summary": "'The city has no need of sun or moon to shine on it, for the glory of God "
                           "gives it light, and its lamp is the Lamb. The nations will walk by its "
                           "light... its gates will never be shut.'",
                "relevance": "Revelation's New Jerusalem directly fulfills Isaiah 60:19-20 (YHWH as "
                             "everlasting light) and 60:11 (gates never shut)."
            },
            {
                "source": "11QMelchizedek (11Q13)",
                "summary": "The Qumran Melchizedek scroll interprets Isaiah 61:1 in terms of the "
                           "eschatological Jubilee, where Melchizedek proclaims 'liberty to the "
                           "captives' on the Day of Atonement at the end of the tenth Jubilee.",
                "relevance": "The Dead Sea Scrolls community read 61:1 as an eschatological text tied "
                             "to the Jubilee cycle, with a heavenly deliverer (Melchizedek) as its agent."
            }
        ],

        "cross_refs": [
            {"ref": "Luke 4:16-21", "note": "Jesus reads 61:1-2a and claims fulfillment in himself -- the inaugural sermon of his ministry", "type": "nt"},
            {"ref": "Matthew 2:11", "note": "Gold and frankincense brought by the Magi -- echoing 60:6", "type": "nt"},
            {"ref": "Revelation 21:23-25", "note": "No sun or moon needed, gates never shut -- direct fulfillment of 60:11, 19-20", "type": "nt"},
            {"ref": "Leviticus 25:10", "note": "The Jubilee: 'proclaim liberty (deror) throughout the land' -- the background for 61:1-2", "type": "ot"},
            {"ref": "Revelation 19:7-8", "note": "'The marriage of the Lamb has come, and his Bride has made herself ready' -- the bridal imagery of 62:4-5", "type": "nt"},
            {"ref": "2 Corinthians 6:2", "note": "Paul quotes 49:8 ('in a favorable time I listened to you') alongside the 'year of favor' theology", "type": "nt"},
            {"ref": "Hosea 2:19-20", "note": "'I will betroth you to me forever' -- the same bridal covenant theology as 62:4-5", "type": "ot"}
        ],

        "divine_council_note": "Isaiah 61:1 is a divine council commissioning text. The speaker -- whether "
                               "the prophet or the Servant or both -- has received the ruach (Spirit) of "
                               "Adonai YHWH and has been 'anointed' (mashach) for a specific mission. The "
                               "anointing terminology connects to the royal anointing of kings (1 Sam 16:13) "
                               "and the Servant's Spirit-endowment (42:1). Jesus' claim in Luke 4 that he "
                               "is the fulfillment of this text is a claim to be the divinely anointed "
                               "council agent sent to execute YHWH's decree of liberation. The vision of "
                               "Zion's glory in chapter 60 -- YHWH as everlasting light replacing sun and "
                               "moon -- anticipates the new creation where the divine council's throne room "
                               "illumination (the kavod, 'glory') extends over the entire earth. The nations "
                               "streaming to Zion's light (60:3) represents the reversal of the Deuteronomy "
                               "32 allotment: peoples formerly under the governance of lesser elohim now come "
                               "to YHWH's own city. The bridal imagery of chapter 62 -- YHWH rejoicing over "
                               "Zion as a bridegroom over his bride -- portrays the covenant relationship as "
                               "a wedding feast, the same imagery Jesus uses for the kingdom (Matt 22:1-14; "
                               "25:1-13) and Revelation uses for the consummation (Rev 19:7-9).",

        "sections": [
            {
                "heading": "Arise, Shine: Nations Stream to Zion's Light (60:1-14)",
                "body": "'Qumi ori ki va orekh, ukhvod YHWH alayikh zarach' -- 'Arise, shine, for your "
                        "light has come, and the glory of YHWH has risen upon you' (60:1). The imperatives "
                        "are feminine singular -- addressed to Zion personified as a woman. The verb zarach "
                        "('to rise, shine') is the same word used for the sunrise; YHWH's glory dawns over "
                        "Zion like the morning sun. 'For behold, darkness (choshek) shall cover the earth, "
                        "and thick darkness (araphel) the peoples; but YHWH will rise (yizrach) upon you, "
                        "and his glory (kevodo) will be seen upon you' (60:2). The contrast is absolute: "
                        "global darkness vs. Zion's illumination. 'Nations (goyim) shall come to your light "
                        "(orekh), and kings (melakhim) to the brightness (nogah) of your rising' (60:3). "
                        "The nations' pilgrimage brings wealth: 'A multitude of camels shall cover you, "
                        "the young camels of Midian and Ephah; all those from Sheba shall come. They shall "
                        "bring gold (zahav) and frankincense (levonah), and shall bring good news (besorah), "
                        "the praises of YHWH' (60:6). Gold and frankincense from Sheba -- the same goods "
                        "the Magi bring to Jesus in Matthew 2:11. 'Your gates shall be open continually; "
                        "day and night they shall not be shut, that people may bring to you the wealth "
                        "(cheil) of the nations' (60:11). The ever-open gates signify permanent welcome -- "
                        "no threat remains that would require closed gates. This detail reappears in "
                        "Revelation 21:25."
            },
            {
                "heading": "The Spirit's Anointing: The Year of YHWH's Favor (61:1-4)",
                "body": "'Ruach Adonai YHWH alai, ya'an mashach YHWH oti' -- 'The Spirit of the Lord GOD "
                        "is upon me, because YHWH has anointed me' (61:1a). The verb mashach ('to anoint') "
                        "is the root of mashiach ('anointed one, Messiah'). The speaker has been commissioned "
                        "by divine anointing for a specific mission: 'levasar anavim' -- 'to bring good "
                        "news (basar) to the poor (anavim)' (61:1b). The verb basar is the root of besorah "
                        "('gospel, good news'). The mission: 'to bind up the brokenhearted (nishberei lev), "
                        "to proclaim liberty (deror) to the captives' (61:1c). The word deror is the "
                        "technical Jubilee term from Leviticus 25:10 -- the year of universal release and "
                        "restoration. 'To proclaim the year of YHWH's favor (shenat ratson la-YHWH) and "
                        "the day of vengeance (yom naqam) of our God' (61:2). When Jesus reads this in "
                        "Nazareth (Luke 4:18-19), he stops after 'the year of the LORD's favor' and does "
                        "NOT read 'the day of vengeance' -- because his first coming is the year of grace; "
                        "the day of vengeance belongs to his return. This mid-sentence stop is one of the "
                        "most theologically significant pauses in the Bible. The result of the anointed "
                        "one's ministry: 'to comfort all who mourn... to give them a beautiful headdress "
                        "(pe'er) instead of ashes (epher), the oil of gladness (shemen sasson) instead of "
                        "mourning, the garment of praise (ma'ateh tehillah) instead of a faint spirit "
                        "(ruach kehah)' (61:2-3)."
            },
            {
                "heading": "The Bridegroom Rejoices: New Names for Zion (62:1-12)",
                "body": "'For Zion's sake I will not keep silent (lo echesheh), and for Jerusalem's sake "
                        "I will not be quiet (lo eshqot), until her righteousness (tsidqah) goes forth as "
                        "brightness (nogah), and her salvation (yeshu'atah) as a burning torch (lappid "
                        "yo'er)' (62:1). Whether YHWH or the prophet speaks, the urgency is absolute. "
                        "'The nations (goyim) shall see your righteousness, and all the kings your glory "
                        "(kevod); and you shall be called by a new name (shem chadash) that the mouth of "
                        "YHWH will give' (62:2). New names signify new identity: 'You shall no more be "
                        "termed Azuvah (Forsaken), and your land shall no more be termed Shemamah "
                        "(Desolate), but you shall be called Hephzibah (My-Delight-Is-in-Her), and your "
                        "land Beulah (Married); for YHWH delights (chaphets) in you, and your land shall "
                        "be married (tiba'el)' (62:4). The covenant is a marriage, and YHWH is the "
                        "bridegroom. 'As the bridegroom (chatan) rejoices (masos) over the bride (kallah), "
                        "so shall your God rejoice (yasis) over you' (62:5). YHWH's joy over his people "
                        "is compared to wedding-day ecstasy -- the most intense human happiness becomes "
                        "the analogy for divine delight. The chapter ends with the declaration: 'Say to "
                        "the daughter of Zion: Behold, your salvation (yish'ekh) comes; behold, his reward "
                        "(sekharo) is with him, and his recompense (pe'ullato) before him' (62:11). The "
                        "language echoes 40:10, completing the arc from comfort to consummation."
            }
        ]
    },

    {
        "id": "isa-63-64",
        "ref": "Isaiah 63-64",
        "chapter_num": 4,
        "title": "The Divine Warrior from Edom and the Prayer of the Remnant",
        "era": "isaiah_new",
        "type": "chapter",
        "themes": ["BLOOD", "REMEMBER", "RIV"],

        "synopsis": "Isaiah 63 opens with one of the most dramatic scenes in prophetic literature: a "
                    "solitary figure approaches from Edom, from Bozrah, his garments stained crimson red. "
                    "'Who is this who comes from Edom (Edom), in crimsoned garments from Bozrah, he who "
                    "is splendid in his apparel, marching in the greatness of his strength? It is I, "
                    "speaking in righteousness (tsedaqah), mighty to save (rav lehoshia)' (63:1). The "
                    "figure is YHWH himself -- the Divine Warrior returning from battle. 'Why is your "
                    "apparel red, and your garments like his who treads in the winepress (gat)?' (63:2). "
                    "The answer: 'I have trodden the winepress alone (levaddi), and from the peoples no "
                    "one was with me; I trod them in my anger and trampled them in my wrath; their "
                    "lifeblood (nitsacham) spattered on my garments, and stained all my apparel' (63:3). "
                    "The winepress is judgment, and YHWH treads it alone -- no army, no allies, no council "
                    "members assist. 'I looked, but there was no one to help; I was appalled, but there "
                    "was no one to uphold; so my own arm brought me salvation' (63:5). This parallels "
                    "59:16 and anticipates Revelation 19:13-15, where Christ returns with a robe 'dipped "
                    "in blood,' treading 'the winepress of the fury of the wrath of God.' The chapter "
                    "then shifts to a communal prayer -- one of the most anguished in Scripture. The "
                    "remnant remembers YHWH's past faithfulness: 'he became their Savior (moshia). In "
                    "all their affliction he was afflicted, and the Angel of his Presence (mal'akh panav) "
                    "saved them' (63:8-9). But now they feel abandoned: 'Look down from heaven and see, "
                    "from your holy and beautiful habitation. Where are your zeal (qin'atekha) and your "
                    "might (gevurotekha)?... For you are our Father (Avinu), though Abraham does not know "
                    "us and Israel does not acknowledge us; you, O YHWH, are our Father, our Redeemer "
                    "(Go'elenu) from of old is your name' (63:15-16). Chapter 64 continues the desperate "
                    "plea: 'Oh that you would rend (qara'ta) the heavens and come down (yaradeta)!' "
                    "(64:1). The prayer reaches its climax with the confession: 'We have all become like "
                    "one who is unclean, and all our righteous deeds (tsidqotenu) are like a polluted "
                    "garment (beged iddim)' (64:6). Yet even in desperation, trust endures: 'O YHWH, "
                    "you are our Father; we are the clay, and you are our potter (yotsrenu); we are all "
                    "the work of your hand' (64:8).",

        "key_verse": {
            "ref": "Isaiah 63:3",
            "text": "I have trodden the winepress alone, and from the peoples no one was with me; I trod them in my anger and trampled them in my wrath; their lifeblood spattered on my garments, and stained all my apparel.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "gat (winepress -- the instrument of divine judgment; YHWH treads it alone)",
            "levaddi (alone/by myself -- no council member, no ally assists the Divine Warrior)",
            "nitsach (lifeblood/juice -- the crimson stain on the warrior's garments)",
            "mal'akh panav (Angel of his Presence -- Hebrew mal'akh means 'messenger' (translated 'angel' in English Bibles), and panav means 'his face/presence.' This is the divine agent who carries YHWH's own panim ('face') -- meaning he bears YHWH's very identity and authority. This figure appears throughout Israel's history: at the burning bush (Exod 3:2), leading Israel through the wilderness (Exod 23:20-23), confronting Joshua (Josh 5:13-15). The remarkable thing about this angel is that he sometimes speaks AS YHWH in the first person, blurring the line between messenger and sender. This is a divine council member of the highest rank, carrying the full presence of the God who sent him)",
            "Avinu (our Father -- the intimate address to YHWH as parent)",
            "Go'elenu (our Redeemer -- the kinsman-redeemer title applied to YHWH)",
            "beged iddim (polluted garment -- the translation 'filthy rags' in older English Bibles is a euphemism. The Hebrew is blunter: beged iddim literally means 'menstrual cloth' -- a garment stained with menstrual blood, which under Levitical law was a source of ritual impurity (Lev 15:19-24). The image is deliberately shocking: even humanity's best moral efforts (tsidqotenu, 'our righteous deeds') are as contaminated before YHWH as a cloth saturated with bodily impurity. This is not misogyny but a visceral metaphor for the gap between human morality and divine holiness)",
            "yotser (potter -- YHWH as the craftsman who shapes his people like clay)"
        ],

        "ane_backdrop": "The winepress as a metaphor for judgment is attested in ANE imagery. Egyptian "
                        "battle reliefs depict the pharaoh as a harvester treading enemies underfoot, "
                        "and the Ugaritic texts describe Anat, Baal's sister-warrior, wading through "
                        "blood after battle. The distinction in Isaiah 63 is that YHWH treads the "
                        "winepress alone -- in ANE mythology, warrior gods typically fight with armies "
                        "of lesser deities. YHWH's solitary combat emphasizes his incomparability. The "
                        "reference to Edom and Bozrah may reflect the traditional enmity between Israel "
                        "and Edom (descendants of Esau), but 'Edom' (from adom, 'red') also creates a "
                        "wordplay with the blood-red garments. The potter-and-clay metaphor (64:8) has "
                        "parallels in Egyptian wisdom literature (the Instruction of Ptahhotep) and in "
                        "Mesopotamian creation accounts where humans are fashioned from clay by the gods "
                        "(the Atrahasis Epic).",

        "second_temple": [
            {
                "source": "Revelation 19:13-15",
                "summary": "'He is clothed in a robe dipped in blood, and the name by which he is called "
                           "is The Word of God... He will tread the winepress of the fury of the wrath "
                           "of God the Almighty.'",
                "relevance": "John directly applies the Divine Warrior winepress imagery of Isaiah 63 to "
                             "Christ at his second coming. The blood-stained garments of Isaiah's Warrior "
                             "become the blood-dipped robe of the returning King."
            },
            {
                "source": "Revelation 14:19-20",
                "summary": "'The angel swung his sickle across the earth... and threw it into the great "
                           "winepress of the wrath of God.'",
                "relevance": "The winepress of divine judgment in Revelation draws directly on Isaiah 63's "
                             "imagery of treading the nations."
            },
            {
                "source": "Romans 9:20-21",
                "summary": "'Who are you, O man, to answer back to God? Will what is molded say to its "
                           "molder, Why have you made me like this?'",
                "relevance": "Paul's potter-clay argument echoes Isaiah 64:8, using the same sovereignty "
                             "theology: God is the potter; humanity is the clay."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 59:16", "note": "'His own arm brought him salvation' -- the same solitary divine action as 63:5", "type": "ot"},
            {"ref": "Revelation 19:13-15", "note": "Christ returns in blood-dipped garments, treading the winepress -- directly fulfilling 63:1-6", "type": "nt"},
            {"ref": "Exodus 23:20-21", "note": "The Angel in whom YHWH's name dwells -- the mal'akh panav ('Angel of his Presence') of 63:9", "type": "ot"},
            {"ref": "Psalm 44:23-26", "note": "'Awake! Why are you sleeping, O Lord?' -- the same desperate appeal to a seemingly silent God", "type": "ot"},
            {"ref": "Romans 9:20-21", "note": "Paul's potter-clay argument drawn from Isaiah 64:8", "type": "nt"},
            {"ref": "Jeremiah 18:1-6", "note": "Jeremiah's potter-and-clay vision -- the same divine sovereignty imagery", "type": "ot"},
            {"ref": "Mark 1:10", "note": "'He saw the heavens being torn open (schizomenous)' at Jesus' baptism -- the heavens 'rent' that Isaiah 64:1 cried for", "type": "nt"},
            {"ref": "Joel 3:13", "note": "'Put in the sickle, for the harvest is ripe. Go in, tread, for the winepress is full' -- the same judgment imagery", "type": "ot"},
            {"ref": "Isaiah 34:5-6", "note": "YHWH's sword descends on Edom/Bozrah -- the same geographical focus as 63:1, forming an inclusio of divine judgment around Second Isaiah", "type": "ot"},
            {"ref": "Deuteronomy 32:41-43", "note": "'I will take vengeance on my adversaries... I will make my arrows drunk with blood, and my sword shall devour flesh' -- the Song of Moses' divine warrior passage that Isaiah 63 fulfills", "type": "ot"},
            {"ref": "Habakkuk 3:3-15", "note": "The divine warrior marching from Teman/Edom -- the same geographical and theological tradition as Isaiah 63's warrior from Edom", "type": "ot"},
            {"ref": "Judges 5:4-5", "note": "'YHWH, when you went out from Seir, when you marched from the region of Edom' -- the Deborah Song's divine warrior tradition that Isaiah 63 develops", "type": "ot"},
            {"ref": "Psalm 110:5-6", "note": "'The Lord is at your right hand; he will shatter kings on the day of his wrath. He will execute judgment among the nations, filling them with corpses' -- the messianic warrior-priest psalm parallel", "type": "ot"},
            {"ref": "Revelation 14:19-20", "note": "The angel swings his sickle and throws the harvest into 'the great winepress of the wrath of God' -- the Isaiah 63 winepress becomes cosmic in Revelation's final judgment", "type": "nt"},
            {"ref": "Galatians 4:6", "note": "'Because you are sons, God has sent the Spirit of his Son into our hearts, crying, Abba! Father!' -- the 'Avinu' (our Father) cry of 63:16 and 64:8 becomes the Christian's cry through the Spirit", "type": "nt"}
        ],

        "divine_council_note": "Isaiah 63's Divine Warrior treading the winepress alone (levaddi) is YHWH "
                               "doing what his council members failed to do. The repeated emphasis -- 'alone,' "
                               "'no one was with me,' 'there was no one to help' (63:3, 5) -- underscores "
                               "that the divine council members who were allotted the nations (Deut 32:8-9) "
                               "have failed in their governance, and the Servant who was to intercede (53:12) "
                               "has not yet been recognized. So YHWH acts unilaterally. The 'Angel of his "
                               "Presence' (mal'akh panav, 63:9) is a council figure -- the Angel who bears "
                               "YHWH's panim ('face/presence') and who saved Israel in the past. This is the "
                               "same 'Angel of YHWH' who appeared to Moses, Joshua, and the judges -- a "
                               "divine being who carries YHWH's authority and name (cf. Exod 23:20-21). The "
                               "prayer of 63:15-64:12 is addressed to YHWH in his 'holy and beautiful "
                               "habitation' (zevul qodshekha vetif'artekha, 63:15) -- the throne room of "
                               "the divine council. The cry 'Oh that you would rend the heavens and come "
                               "down!' (64:1) is a plea for the council's King to leave his throne and "
                               "personally intervene. Mark 1:10's description of the heavens being 'torn "
                               "open' (schizomenous) at Jesus' baptism uses language that may echo this "
                               "prayer: the heavens have finally been rent, and God has come down.",

        "sections": [
            {
                "heading": "The Winepress: YHWH Treads Alone (63:1-6)",
                "body": "'Who is this who comes from Edom (Edom), in crimsoned garments (chamutz begadim) "
                        "from Bozrah?' (63:1a). The question comes from a watcher on Zion's walls, "
                        "seeing a lone figure approaching from the southeast. Bozrah was the capital of "
                        "Edom, and the name means 'grape-gathering' -- a deliberate wordplay with the "
                        "winepress imagery that follows. The figure identifies himself: 'It is I (ani), "
                        "speaking in righteousness (tsedaqah), mighty to save (rav lehoshia)' (63:1b). "
                        "The self-identification 'ani' ('I') echoes the divine self-revelation formula "
                        "(cf. 'I am YHWH' throughout Exodus and Isaiah). 'Why is your apparel red (adom), "
                        "and your garments like his who treads in the gat (winepress)?' (63:2). The "
                        "color wordplay is layered: Edom (from adom, 'red'), the red garments, the red "
                        "wine/blood of the winepress. 'I have trodden the winepress levaddi (alone), and "
                        "from the peoples (me-ammim) no one (ein-ish) was with me' (63:3a). YHWH fought "
                        "alone -- no army, no allies, no angelic host. 'I trod them in my anger (be-appi) "
                        "and trampled them in my wrath (bachamati); their lifeblood (nitsacham) spattered "
                        "on my garments, and stained (ega'alti) all my apparel' (63:3b). The image is of "
                        "a vintner whose clothes are splashed with grape juice -- but the grapes are "
                        "nations under judgment. 'For the day of vengeance (yom naqam) was in my heart, "
                        "and my year of redemption (shenat ge'ulai) had come' (63:4). Vengeance and "
                        "redemption are paired: YHWH's judgment on the oppressors IS the redemption of "
                        "his people."
            },
            {
                "heading": "Remembering YHWH's Past Faithfulness (63:7-14)",
                "body": "The tone shifts to liturgical recitation: 'I will recount (azkir) the steadfast "
                        "love (chasdei) of YHWH, the praises of YHWH, according to all that YHWH has "
                        "granted us' (63:7). The community remembers YHWH's past relationship: 'He said, "
                        "Surely they are my people (ammi), children (banim) who will not deal falsely. "
                        "And he became their Savior (moshia)' (63:8). 'In all their affliction (tsaratam) "
                        "he was afflicted (tsar lo), and the Angel of his Presence (mal'akh panav) saved "
                        "them; in his love (ahavato) and in his pity (chemlato) he redeemed them (ge'alam); "
                        "he lifted them and carried them all the days of old' (63:9). The mal'akh panav "
                        "('Angel of his Presence/Face') is a key divine council figure -- the angel who "
                        "bears YHWH's own panim and acts with his full authority. This is the Angel of "
                        "the burning bush (Exod 3:2), the Angel who led Israel through the wilderness "
                        "(Exod 23:20-23), the Angel of YHWH who fought for Israel. 'But they rebelled "
                        "(maru) and grieved (itsevu) his Holy Spirit (ruach qodsho); therefore he turned "
                        "to be their enemy, and himself fought against them' (63:10). The rebellion turns "
                        "YHWH from savior to adversary -- the same God who fought for Israel now fights "
                        "against them. 'Then he remembered (yizkor) the days of old, of Moses and his "
                        "people. Where is he who brought them up out of the sea... who put in the midst "
                        "of them his Holy Spirit (ruach qodsho)?' (63:11)."
            },
            {
                "heading": "The Desperate Prayer: Rend the Heavens and Come Down (63:15-64:12)",
                "body": "'Look down from heaven (shamayim) and see, from your holy and beautiful "
                        "habitation (zevul qodshekha vetif'artekha)' (63:15a). The prayer is addressed "
                        "upward -- to the divine council throne room. 'Where are your zeal (qin'atekha) "
                        "and your might (gevurotekha)? The stirring of your inner parts (hamon me'ekha) "
                        "and your compassion (rachamekha) -- are they restrained (hit'appaq)?' (63:15b). "
                        "The language is visceral: YHWH's 'inner parts' (me'im) are his emotional core. "
                        "'For you are our Father (Avinu), though Abraham does not know us and Israel does "
                        "not acknowledge us; you, O YHWH, are our Father; our Redeemer (Go'elenu) from "
                        "of old is your name' (63:16). The double 'Avinu' ('our Father') is remarkable "
                        "-- a title rarely applied to YHWH in the Hebrew Bible but central to Jesus' "
                        "teaching. Then the anguished cry: 'Oh that you would rend (qara'ta) the heavens "
                        "(shamayim) and come down (yaradeta)!' (64:1). The word qara ('to tear, rend') is "
                        "violent -- the image is of YHWH literally tearing the sky apart to descend. 'The "
                        "mountains would quake at your presence -- as when fire kindles brushwood and fire "
                        "causes water to boil' (64:1b-2). The confession of sin: 'We have all become "
                        "like one who is unclean (tame), and all our righteous deeds (tsidqotenu) are like "
                        "a beged iddim (polluted garment)' (64:6). Yet hope persists: 'But now, O YHWH, "
                        "you are our Father (Avinu); we are the clay (chomer), and you are our potter "
                        "(yotsrenu); we are all the work of your hand (ma'aseh yadekha)' (64:8). The "
                        "final plea: 'Will you restrain yourself at these things, O YHWH? Will you keep "
                        "silent and afflict us so terribly?' (64:12)."
            }
        ]
    },

    {
        "id": "isa-65-66",
        "ref": "Isaiah 65-66",
        "chapter_num": 5,
        "title": "The Divine Warrior's Answer: New Heavens, New Earth, and Final Judgment",
        "era": "isaiah_new",
        "type": "chapter",
        "themes": ["LAND", "REVERSAL", "GLORY", "HOLY"],

        "synopsis": "YHWH answers the remnant's prayer of chapters 63-64 -- but the answer separates the "
                    "faithful from the rebellious. 'I was ready to be sought (nidrashti) by those who did "
                    "not ask for me; I was ready to be found (nimtseti) by those who did not seek me. I "
                    "said, Here I am, here I am (hineni, hineni), to a nation that was not called by my "
                    "name' (65:1). Paul applies this to the Gentile mission in Romans 10:20. But YHWH's "
                    "own people provoked him: 'a people who provoke me to my face continually, sacrificing "
                    "in gardens and making offerings on bricks; who sit in tombs, and spend the night in "
                    "secret places; who eat swine's flesh' (65:3-4). The verdict is separation: 'Behold, "
                    "my servants (avadai) shall eat, but you shall be hungry; behold, my servants shall "
                    "drink, but you shall be thirsty; behold, my servants shall rejoice, but you shall be "
                    "put to shame' (65:13). Then the cosmic declaration: 'For behold, I create (bore) new "
                    "heavens (shamayim chadashim) and a new earth (erets chadashah), and the former things "
                    "shall not be remembered or come into mind' (65:17). The new creation is described in "
                    "terms of radical transformation: 'No more shall there be in it an infant who lives "
                    "but a few days, or an old man who does not fill out his days, for the young man shall "
                    "die a hundred years old' (65:20). The Edenic peace returns: 'The wolf (ze'ev) and the "
                    "lamb (taleh) shall feed (yir'u) together; the lion shall eat straw like the ox, and "
                    "dust shall be the serpent's food. They shall not hurt or destroy in all my holy "
                    "mountain' (65:25). Chapter 66 opens with YHWH's cosmic self-declaration: 'Heaven "
                    "(shamayim) is my throne (kis'i), and the earth (erets) is my footstool (hadom raglai). "
                    "What is the house that you would build for me, and what is the place of my rest?' "
                    "(66:1). No temple can contain YHWH -- yet 'this is the one to whom I will look: he "
                    "who is humble and contrite in spirit and trembles at my word' (66:2). The book "
                    "concludes with the vision of universal worship: 'From new moon to new moon, and from "
                    "Sabbath to Sabbath, all flesh (kol-basar) shall come to worship before me, declares "
                    "YHWH' (66:23). The final verse is a sobering warning: 'And they shall go out and look "
                    "on the dead bodies of the men who have rebelled against me. For their worm (tolaat) "
                    "shall not die, their fire (esh) shall not be quenched, and they shall be an "
                    "abhorrence (dera'on) to all flesh' (66:24). Jesus quotes this for Gehenna in Mark "
                    "9:48.",

        "key_verse": {
            "ref": "Isaiah 65:17",
            "text": "For behold, I create new heavens and a new earth, and the former things shall not be remembered or come into mind.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "shamayim chadashim (new heavens -- the renewed cosmic realm)",
            "erets chadashah (new earth -- the transformed terrestrial realm)",
            "bore (creating -- the same verb as Genesis 1:1; a new act of divine creation)",
            "kis'i (my throne -- heaven as YHWH's seat of authority)",
            "hadom raglai (my footstool -- the earth as YHWH's footrest, implying cosmic kingship)",
            "kol-basar (all flesh -- universal humanity worshiping YHWH)",
            "tolaat (worm -- the agent of decomposition that never ceases in the final judgment; Jesus quotes this image in Mark 9:48 for his teaching on Gehenna)",
            "dera'on (abhorrence/contempt -- an extremely rare Hebrew word appearing only here and in Daniel 12:2. It describes the permanent revulsion felt toward the wicked dead -- not pity, not indifference, but visceral horror. This is one of the few Old Testament passages that points toward a distinction between the destinies of the righteous and the wicked after death, a concept that develops more fully in Daniel 12:2 and in Second Temple Judaism)",
            "Gehenna (ge-hinnom -- the Valley of Hinnom outside Jerusalem; IMPORTANT: this is NOT the same as Sheol. Sheol is the shadowy underworld where ALL the dead go in early Hebrew thought. Gehenna is the place of fiery judgment for the wicked, developed from the literal Valley of Hinnom where children were sacrificed to Molech and which later became a burning garbage dump. Jesus uses 'Gehenna' (NOT 'Sheol') in his warnings about final punishment. Isaiah 66:24 provides the foundational imagery for Gehenna: undying worms and unquenchable fire)"
        ],

        "ane_backdrop": "The concept of cosmic renewal -- new heavens and new earth -- has partial "
                        "parallels in ANE mythology. Egyptian funerary literature describes the 'Field of "
                        "Reeds' (Sekhet-Aaru) as a perfected agricultural paradise. Mesopotamian traditions "
                        "speak of Dilmun, a primordial paradise where there is no death, disease, or "
                        "predation. But Isaiah's vision transcends these: he does not describe escape to "
                        "another realm but the transformation of this cosmos. The heavens and earth are not "
                        "abandoned but re-created (bore -- the same creation verb of Genesis 1:1). The "
                        "statement 'heaven is my throne and earth is my footstool' (66:1) echoes ANE "
                        "throne-room imagery: Mesopotamian temples were understood as the footstool of the "
                        "deity's throne, and the Ark of the Covenant was called YHWH's footstool (1 Chr "
                        "28:2; Ps 132:7). Isaiah pushes this to its cosmic limit: the entire earth is "
                        "merely YHWH's footstool. The 'undying worm' and 'unquenchable fire' of 66:24 "
                        "became foundational imagery for Gehenna (ge-Hinnom, the Valley of Hinnom) in "
                        "later Jewish eschatology.",

        "second_temple": [
            {
                "source": "Revelation 21:1",
                "summary": "'Then I saw a new heaven and a new earth, for the first heaven and the first "
                           "earth had passed away, and the sea was no more.'",
                "relevance": "John's vision of the new creation directly fulfills Isaiah 65:17 and 66:22. "
                             "The 'new heavens and new earth' of Isaiah become the consummation of all "
                             "things in Revelation."
            },
            {
                "source": "2 Peter 3:13",
                "summary": "'According to his promise we are waiting for new heavens and a new earth in "
                           "which righteousness dwells.'",
                "relevance": "Peter explicitly cites the promise of Isaiah 65:17/66:22 as the Christian "
                             "eschatological hope -- the new creation where tsedaqah ('righteousness') "
                             "permanently dwells."
            },
            {
                "source": "Mark 9:48",
                "summary": "Jesus describes Gehenna as the place 'where their worm does not die and the "
                           "fire is not quenched.'",
                "relevance": "Jesus directly quotes Isaiah 66:24 to describe the final state of the "
                             "unrepentant -- the 'undying worm' and 'unquenchable fire' of Isaiah's "
                             "closing verse become Jesus' primary Gehenna imagery."
            },
            {
                "source": "Acts 7:49-50",
                "summary": "Stephen quotes Isaiah 66:1-2 in his speech before the Sanhedrin: 'Heaven is "
                           "my throne, and the earth is my footstool. What kind of house will you build "
                           "for me?'",
                "relevance": "Stephen uses Isaiah 66:1 to argue that the Jerusalem temple cannot contain "
                             "YHWH -- the same point Isaiah makes about the limits of human worship space."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 1:1", "note": "'In the beginning, God created (bara) the heavens and the earth' -- Isaiah 65:17 uses the same verb bore for the new creation", "type": "ot"},
            {"ref": "Revelation 21:1-4", "note": "The new heaven and new earth, no more tears, no more death -- the fulfillment of Isaiah 65:17-25", "type": "nt"},
            {"ref": "2 Peter 3:13", "note": "Peter cites Isaiah's new heavens and new earth as the Christian eschatological hope", "type": "nt"},
            {"ref": "Mark 9:48", "note": "Jesus quotes Isaiah 66:24 for his Gehenna teaching -- 'their worm does not die'", "type": "nt"},
            {"ref": "Acts 7:49-50", "note": "Stephen quotes 66:1 to challenge temple theology", "type": "nt"},
            {"ref": "Romans 10:20-21", "note": "Paul quotes 65:1-2 to explain Gentile inclusion and Israelite disobedience", "type": "nt"},
            {"ref": "Isaiah 11:6-9", "note": "The earlier Edenic peace vision -- wolf and lamb, no hurt or destruction -- echoed in 65:25", "type": "ot"},
            {"ref": "Daniel 12:2", "note": "'Some to everlasting life, and some to shame and everlasting contempt (dera'on)' -- the same rare word as 66:24", "type": "ot"},
            {"ref": "1 Kings 22:19", "note": "Micaiah sees YHWH on his throne with the host of heaven -- 66:1 ('heaven is my throne') echoes this council throne room", "type": "ot"}
        ],

        "divine_council_note": "Isaiah 65-66 brings the divine council narrative to its cosmic conclusion. "
                               "The new heavens and new earth (65:17; 66:22) represent the restoration of "
                               "the original cosmic order -- the Genesis 1 creation remade, with the curse "
                               "of Genesis 3 reversed and the effects of the Watchers' rebellion undone. "
                               "The declaration 'heaven is my throne, and the earth is my footstool' (66:1) "
                               "echoes the divine council throne room of 1 Kings 22:19, Isaiah 6:1, and "
                               "Daniel 7:9 -- but now the throne room extends over the entire cosmos. No "
                               "temple is needed because the entire earth is YHWH's temple. The 'host of "
                               "heaven' (tseva hashamayim) is referenced in the judgment context: those who "
                               "'worship the host of heaven' (cf. 2 Kings 21:3; Deut 4:19) -- the divine "
                               "council members allotted to the nations -- are judged alongside idolaters. "
                               "The final vision of 'all flesh' (kol-basar) worshiping YHWH 'from new moon "
                               "to new moon and from Sabbath to Sabbath' (66:23) is the ultimate reversal "
                               "of the Deuteronomy 32:8-9 allotment: the nations are no longer under the "
                               "governance of lesser elohim but worship YHWH directly. The rare word dera'on "
                               "('abhorrence, contempt') in 66:24 appears only here and in Daniel 12:2, "
                               "linking Isaiah's final judgment to Daniel's vision of resurrection and "
                               "eschatological separation. The council's plan, from creation through fall "
                               "through exile through suffering through new creation, reaches its terminus: "
                               "YHWH reigns, the nations worship, and the rebels face unending judgment.",

        "sections": [
            {
                "heading": "YHWH Found by Those Who Did Not Seek: Separation of Servants and Rebels (65:1-16)",
                "body": "'I was ready to be sought (nidrashti) by those who did not ask for me (lo sha'alu); "
                        "I was ready to be found (nimtseti) by those who did not seek me (lo biqshuni). I "
                        "said, Hineni, hineni (Here I am, here I am), to a nation that was not called by "
                        "my name (shemi)' (65:1). YHWH extends himself to a people who are not Israel -- "
                        "Paul applies this to the Gentile mission in Romans 10:20. But to Israel: 'I spread "
                        "out my hands all the day to a rebellious (sorer) people, who walk in a way that is "
                        "not good, following their own devices' (65:2). The specific sins: 'sacrificing in "
                        "gardens (gannot) and making offerings on bricks (levenim)' (65:3) -- garden shrines "
                        "and possibly rooftop altars for astral worship. 'Who sit in tombs and spend the "
                        "night in secret places' (65:4) -- necromancy, consultation with the dead. 'Who eat "
                        "swine's flesh (besar hachazir)' (65:4) -- violation of the dietary laws. 'Who say, "
                        "Keep to yourself, do not come near me, for I am too holy (qedashtikha) for you' "
                        "(65:5). The irony is devastating: the sinners claim holiness. YHWH responds with "
                        "the great separation: 'Behold, my servants (avadai) shall eat, but you shall be "
                        "hungry; my servants shall drink, but you shall be thirsty; my servants shall "
                        "rejoice, but you shall be put to shame' (65:13). The line between YHWH's servants "
                        "and the rebellious is drawn by covenant loyalty, not ethnic identity. 'He who "
                        "blesses himself in the land shall bless himself by the God of truth (Elohei amen), "
                        "and he who takes an oath in the land shall swear by the God of truth' (65:16). "
                        "YHWH is the Elohei amen -- the God of Amen, the God of absolute faithfulness."
            },
            {
                "heading": "New Heavens, New Earth: The Curse Reversed (65:17-25)",
                "body": "'For behold, I bore (am creating) shamayim chadashim (new heavens) and erets "
                        "chadashah (new earth), and the former things (rishonot) shall not be remembered "
                        "(lo tizzakharnah) or come into mind (lo ta'alenah al-lev)' (65:17). The verb "
                        "bore is the same as Genesis 1:1's bara -- this is a new act of divine creation, "
                        "not renovation but re-creation. 'But be glad and rejoice forever in that which I "
                        "create; for behold, I create Jerusalem to be a joy (gilah), and her people to be "
                        "a gladness (masos)' (65:18). The new creation centers on a renewed Jerusalem. "
                        "The conditions of the new world: 'No more shall there be in it an infant who "
                        "lives but a few days, or an old man who does not fill out his days, for the "
                        "young man shall die a hundred years old' (65:20). Lifespan returns to the "
                        "antediluvian standard -- death is not yet fully abolished (that awaits Revelation "
                        "21:4) but is radically reduced. 'They shall build houses and inhabit them; they "
                        "shall plant vineyards and eat their fruit. They shall not build and another "
                        "inhabit; they shall not plant and another eat' (65:21-22). The curse of "
                        "Deuteronomy 28:30 ('you shall build a house and not live in it; you shall plant "
                        "a vineyard and not enjoy its fruit') is reversed. The climactic promise: 'The "
                        "wolf and the lamb shall feed together; the lion shall eat straw like the ox, "
                        "and dust shall be the serpent's (nachash) food. They shall not hurt or destroy "
                        "in all my holy mountain, says YHWH' (65:25). The nachash -- the serpent of "
                        "Genesis 3 -- is reduced to eating dust (cf. Gen 3:14), and the predator-prey "
                        "relationship is abolished. Isaiah 11:6-9 is fulfilled."
            },
            {
                "heading": "Heaven Is My Throne: Universal Worship and Final Judgment (66:1-24)",
                "body": "'Thus says YHWH: Heaven (shamayim) is my throne (kis'i), and the earth (erets) "
                        "is my footstool (hadom raglai). Where is the house that you would build for me, "
                        "and where is the place of my rest (menuchati)?' (66:1). YHWH cannot be contained "
                        "by any structure -- the entire cosmos is his throne room. 'But this is the one "
                        "to whom I will look (abbit): he who is humble (ani) and contrite (nekheh) in "
                        "spirit (ruach), and trembles (chared) at my word (devari)' (66:2). Not a "
                        "building but a broken heart attracts YHWH's attention. The vision of Zion's "
                        "sudden restoration follows: 'Before she was in labor she gave birth; before "
                        "her pain came upon her she delivered a son. Who has heard such a thing? Who has "
                        "seen such things? Shall a land be born in one day? Shall a nation be brought "
                        "forth in one moment?' (66:7-8). The restoration is instantaneous -- supernatural. "
                        "The enemies of YHWH face judgment: 'For by fire (esh) will YHWH enter into "
                        "judgment, and by his sword (cherev), with all flesh (kol-basar); and those slain "
                        "by YHWH shall be many' (66:16). The final vision: 'From new moon to new moon, "
                        "and from Sabbath to Sabbath, all flesh (kol-basar) shall come to worship "
                        "(lehishtachavot) before me, declares YHWH' (66:23). Universal worship -- the "
                        "entire human race bowing before the cosmic King. But the book's last word is "
                        "judgment: 'They shall go out and look on the dead bodies of the men who have "
                        "rebelled (posh'im) against me. For their worm (tola'tam) shall not die (lo "
                        "tamut), their fire (isham) shall not be quenched (lo tikhbeh), and they shall "
                        "be an abhorrence (dera'on) to all flesh' (66:24). Jesus quotes this verse "
                        "three times in Mark 9:44, 46, 48 for his teaching on Gehenna. Isaiah ends not "
                        "with comfort but with the starkest possible reminder that YHWH's salvation "
                        "requires a response -- and refusal carries eternal consequences."
            }
        ]
    }
]
