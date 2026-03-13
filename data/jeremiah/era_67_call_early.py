"""
era_67_call_early.py -- Call & Early Oracles (Jeremiah 1-10)

Jeremiah's prophetic commission and the first cycle of oracles against Judah.
The call narrative establishes Jeremiah as YHWH's prophet "to the nations"
(1:5), appointed before birth and given authority "over nations and over
kingdoms, to pluck up and to break down, to destroy and to overthrow, to
build and to plant" (1:10). The early oracles develop the covenant lawsuit
(rib) against Judah: Israel was YHWH's faithful bride in the wilderness
(2:2) but has since "changed her glory" for worthless idols (2:11). The
temple sermon of chapter 7 is the prophetic equivalent of a nuclear
detonation -- Jeremiah stands at the temple gates and declares that YHWH
will destroy this temple as he destroyed Shiloh.
"""

CHAPTERS = [
    {
        "id": "jer-1",
        "ref": "Jeremiah 1",
        "chapter_num": 1,
        "title": "The Call of Jeremiah -- Appointed Before Birth",
        "era": "jeremiah_call",
        "type": "chapter",

        "synopsis": "Jeremiah's call narrative is one of the most powerful in scripture. YHWH declares: "
                    "'Before I formed you in the womb I knew you, and before you were born I consecrated "
                    "you; I appointed you a prophet to the nations' (1:5). Jeremiah protests his youth and "
                    "inability to speak (1:6), echoing Moses' reluctance (Exod 4:10). YHWH responds by "
                    "touching Jeremiah's mouth: 'Behold, I have put my words in your mouth' (1:9) -- the "
                    "prophet becomes the mouthpiece of the divine council. His commission is cosmic in "
                    "scope: 'over nations and over kingdoms, to pluck up and to break down, to destroy "
                    "and to overthrow, to build and to plant' (1:10). Two confirming visions follow: an "
                    "almond branch (shaqed, a wordplay on shoqed, 'watching' -- YHWH is 'watching' over "
                    "his word to perform it, 1:11-12) and a boiling pot tilting from the north (1:13-14), "
                    "signifying the Babylonian invasion. YHWH promises to make Jeremiah 'a fortified city, "
                    "an iron pillar, and bronze walls' against the entire land (1:18).",

        "key_verse": {
            "ref": "Jeremiah 1:5",
            "text": "Before I formed you in the womb I knew you, and before you were born I consecrated you; I appointed you a prophet to the nations.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "yada (knew -- intimate, covenantal knowledge, not mere awareness)",
            "hiqdish (consecrated/set apart -- from qadash, the root of 'holy')",
            "navi (prophet -- one who speaks on behalf of another, the council's herald)",
            "shaqed (almond branch -- a wordplay on shoqed, 'watching/wakeful')",
            "natash (pluck up -- the first of six verbs describing Jeremiah's commission)"
        ],

        "ane_backdrop": "Prophetic call narratives are attested throughout the ANE. The Mari Letters "
                        "(18th century BC) describe prophets (apilum, muhhu) who claimed divine "
                        "commission and delivered oracles to the king. The Deir Alla Inscription "
                        "(~840 BC) records visions of the seer Balaam son of Beor, who saw a divine "
                        "assembly deliberating destruction. Jeremiah's call follows the pattern of "
                        "resistance and divine empowerment found also in Moses (Exod 3-4) and Isaiah "
                        "(Isa 6), but uniquely emphasizes predestination: the prophet was chosen "
                        "before conception.",

        "second_temple": [
            {
                "source": "Galatians 1:15",
                "summary": "Paul echoes Jeremiah's call: 'He who had set me apart before I was born "
                           "and who called me by his grace was pleased to reveal his Son to me.'",
                "relevance": "Paul understood his apostolic calling through the lens of Jeremiah's "
                             "prophetic commission -- set apart from the womb for a divine mission."
            },
            {
                "source": "Sirach 49:6-7",
                "summary": "Sirach honors Jeremiah as one who was 'consecrated in the womb to be "
                           "a prophet, to uproot, to destroy, and to overthrow, but also to build "
                           "and to plant.'",
                "relevance": "Second Temple tradition preserved the exact language of Jeremiah's "
                             "commission (1:10), showing its enduring theological significance."
            },
            {
                "source": "4Q385a (Pseudo-Jeremiah fragments)",
                "summary": "Fragmentary Qumran texts expanding on Jeremiah's prophetic ministry, "
                           "including divine speeches and judgment oracles attributed to the prophet.",
                "relevance": "The Qumran community produced additional Jeremiah literature, "
                             "demonstrating his continuing authority in Second Temple Judaism."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 6:1-8", "note": "Isaiah's call in the divine council throne room -- the paradigmatic prophetic commission", "type": "ot"},
            {"ref": "Exodus 4:10-12", "note": "Moses' reluctance and YHWH's promise to be with his mouth -- the same pattern as Jeremiah", "type": "ot"},
            {"ref": "Galatians 1:15", "note": "Paul's self-understanding modeled on Jeremiah's call -- set apart before birth", "type": "nt"},
            {"ref": "Luke 1:15", "note": "John the Baptist 'filled with the Holy Spirit from his mother's womb' -- Jeremianic pattern", "type": "nt"},
            {"ref": "Psalm 139:13-16", "note": "YHWH's knowledge of the person in the womb -- the same theological reality as Jer 1:5", "type": "ot"}
        ],

        "divine_council_note": "Jeremiah's call is a divine council commissioning. The language 'I have put "
                               "my words in your mouth' (1:9) identifies the prophet as the mouthpiece of "
                               "the council -- he does not speak his own words but relays what YHWH has "
                               "decreed. The scope of his commission ('over nations and over kingdoms') "
                               "reflects the council's authority over all earthly powers. The pre-birth "
                               "consecration (1:5) indicates that Jeremiah's role was determined in the "
                               "divine council before his existence in the earthly realm. The 'foe from "
                               "the north' (1:14) is YHWH's instrument -- the divine council has decreed "
                               "judgment, and Babylon is the agent of execution.",

        "sections": [
            {
                "heading": "Before I Formed You in the Womb (1:1-10)",
                "body": "The superscription identifies Jeremiah as 'son of Hilkiah, of the priests who were "
                        "in Anathoth in the land of Benjamin' (1:1) -- a priestly family in a Levitical "
                        "town. His call came 'in the thirteenth year of the reign of Josiah' (1:2), roughly "
                        "627 BC, during Josiah's reforms. YHWH's declaration to the young prophet is "
                        "staggering: 'Before I formed you (yatsarti) in the womb I knew you (yedatikha), "
                        "and before you came out of the womb I consecrated you (hiqdashtikha); I appointed "
                        "you (netatikha) a prophet to the nations (navi la-goyim)' (1:5). Four verbs "
                        "describe YHWH's sovereign action before Jeremiah's birth: formed, knew, consecrated, "
                        "appointed. The verb yada (knew) carries covenantal weight -- this is intimate, "
                        "purposeful knowledge. Jeremiah's response -- 'I do not know how to speak, for I "
                        "am only a youth (na'ar)' (1:6) -- follows the prophetic pattern of reluctance. "
                        "YHWH's counter is physical: 'YHWH put out his hand and touched my mouth' (1:9), "
                        "reminiscent of Isaiah's lips touched by the burning coal (Isa 6:7). The six-verb "
                        "commission (1:10) -- pluck up, break down, destroy, overthrow, build, plant -- "
                        "gives Jeremiah authority over the rise and fall of nations."
            },
            {
                "heading": "Two Visions: The Almond Branch and the Boiling Pot (1:11-16)",
                "body": "YHWH confirms the call with two visionary tests. The first: 'What do you see, "
                        "Jeremiah?' 'I see a branch of an almond tree (maqqel shaqed)' (1:11). YHWH "
                        "responds: 'You have seen well, for I am watching (shoqed) over my word to "
                        "perform it' (1:12). The wordplay shaqed/shoqed (almond/watching) is characteristic "
                        "of prophetic vision -- God reveals truth through verbal resonance. The almond is "
                        "the first tree to bloom in spring, the 'watcher' of the season. The second vision: "
                        "'I see a boiling pot (sir nafuach), facing away from the north (mipnei tsafonah)' "
                        "(1:13). YHWH interprets: 'Out of the north disaster shall be let loose upon all "
                        "the inhabitants of this land' (1:14). Babylon will come from the north -- not "
                        "geographically (Babylon is east) but strategically (invading armies approached "
                        "Judah from the north via the Fertile Crescent). The 'north' (tsafon) also carries "
                        "mythological weight: it is the location of the divine mountain in Canaanite "
                        "religion (Mount Zaphon), suggesting a cosmic dimension to the coming judgment."
            },
            {
                "heading": "A Fortified City Against the Whole Land (1:17-19)",
                "body": "YHWH's final word to the young prophet is simultaneously commission and warning: "
                        "'Do not be dismayed by them, lest I dismay you before them' (1:17). Then the "
                        "remarkable promise: 'Behold, I make you this day a fortified city (ir mivtsar), "
                        "an iron pillar (ammud barzel), and bronze walls (chomot nechoshet), against the "
                        "whole land -- against the kings of Judah, its officials, its priests, and the "
                        "people of the land' (1:18). Jeremiah will stand alone against the entire "
                        "establishment -- royal, priestly, and popular. The language of fortification is "
                        "ironic: Jerusalem's walls will fall, but Jeremiah will stand. The city will be "
                        "destroyed, but the prophet is the true fortress. 'They will fight against you, "
                        "but they shall not prevail over you, for I am with you, declares YHWH, to deliver "
                        "you' (1:19)."
            },
            {
                "heading": "Name Theology: Jeremiah — YHWH Exalts, YHWH Hurls",
                "body": "The name Yirmeyahu (יִרְמְיָהוּ) combines ramah (to throw/exalt) with Yahu (YHWH), "
                        "yielding the dual meaning 'YHWH exalts' and 'YHWH hurls.' Both meanings describe "
                        "his ministry: God raised him up before birth (1:5) to hurl the message of "
                        "Jerusalem's destruction. The prophet whose name means 'YHWH exalts' is the most "
                        "rejected, persecuted, and humiliated prophet in Scripture — thrown into a cistern "
                        "(38:6), imprisoned, mocked, and forced to watch Jerusalem burn. Yet YHWH also "
                        "'loosens' (releases) — Jeremiah prophesies the New Covenant (31:31-34), the "
                        "greatest message of liberation in the OT. His name's dual force — exaltation and "
                        "hurling — encapsulates the two halves of his book: judgment (chs. 1-29) and "
                        "restoration (chs. 30-33). Paul explicitly models his apostolic self-understanding "
                        "on Jeremiah's call: 'He who had set me apart before I was born' (Galatians 1:15), "
                        "using nearly identical language to Jeremiah 1:5. The prophet's name is his message, "
                        "his credential, and his destiny — the one YHWH exalted to hurl both judgment and hope."
            }
        ]
    },

    {
        "id": "jer-2-3",
        "ref": "Jeremiah 2-3",
        "chapter_num": 2,
        "title": "The Covenant Lawsuit -- Israel's Adultery",
        "era": "jeremiah_call",
        "type": "chapter",

        "synopsis": "Chapters 2-3 present YHWH's covenant lawsuit (rib) against Israel using the "
                    "devastating metaphor of marital unfaithfulness. YHWH remembers Israel's early "
                    "devotion: 'I remember the devotion (chesed) of your youth, your love (ahavah) as "
                    "a bride, how you followed me in the wilderness' (2:2). But Israel has 'changed her "
                    "glory for that which does not profit' (2:11) -- abandoning YHWH for worthless idols. "
                    "The indictment is forensic: 'What wrong did your fathers find in me that they went "
                    "far from me?' (2:5). Israel has committed two evils: 'They have forsaken me, the "
                    "fountain of living waters, and hewn out cisterns for themselves, broken cisterns that "
                    "can hold no water' (2:13). The prophetic poetry reaches its most emotionally "
                    "devastating pitch as YHWH pleads with his unfaithful wife to return.",

        "key_verse": {
            "ref": "Jeremiah 2:13",
            "text": "For my people have committed two evils: they have forsaken me, the fountain of living waters, and hewed out cisterns for themselves, broken cisterns that can hold no water.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "rib (covenant lawsuit -- a legal proceeding in which YHWH prosecutes Israel for covenant violation)",
            "chesed (covenant loyalty/devotion -- Israel's early faithfulness to YHWH in the wilderness)",
            "hevel (vanity/breath -- the worthlessness of idols, same word as in Ecclesiastes)",
            "mayin chayyim (living waters -- flowing, fresh water as a metaphor for YHWH's sustaining presence)",
            "zanah (to commit adultery/prostitution -- the dominant metaphor for Israel's idolatry)"
        ],

        "ane_backdrop": "The marriage metaphor for the deity-nation relationship is attested in ANE "
                        "covenant language. Hittite suzerainty treaties describe the vassal's unfaithfulness "
                        "as 'adultery' against the sovereign. The Ugaritic texts describe Baal and Anat's "
                        "relationship in sexually explicit terms. Jeremiah's innovation is the emotional "
                        "depth: YHWH is not merely an offended sovereign but a wounded husband who remembers "
                        "the early days of love. The 'broken cisterns' image draws on the arid Palestinian "
                        "landscape where cisterns were essential for survival -- choosing a broken cistern "
                        "over a living spring is choosing death over life.",

        "second_temple": [
            {
                "source": "John 4:10-14",
                "summary": "Jesus offers the Samaritan woman 'living water' (hydor zon) that becomes a "
                           "spring welling up to eternal life.",
                "relevance": "Jesus applies Jeremiah's 'fountain of living waters' metaphor to himself -- "
                             "he is the source that Israel's broken cisterns could never provide."
            },
            {
                "source": "John 7:37-38",
                "summary": "At the Feast of Tabernacles, Jesus cries out: 'If anyone thirsts, let him "
                           "come to me and drink.'",
                "relevance": "The water-of-life theme from Jeremiah 2:13 reaches its christological "
                             "fulfillment in Jesus' self-identification as the source of living water."
            }
        ],

        "cross_refs": [
            {"ref": "Hosea 1-3", "note": "Hosea's marriage metaphor for YHWH and Israel -- the same theological framework developed by Jeremiah", "type": "ot"},
            {"ref": "Ezekiel 16", "note": "Ezekiel's extended allegory of Jerusalem as an unfaithful wife -- parallel to Jeremiah 2-3", "type": "ot"},
            {"ref": "John 4:10-14", "note": "Jesus as the fountain of living waters -- christological fulfillment of Jeremiah 2:13", "type": "nt"},
            {"ref": "Revelation 21:6", "note": "'I will give from the spring of the water of life without payment' -- eschatological fulfillment", "type": "nt"},
            {"ref": "Deuteronomy 32:15-18", "note": "The Song of Moses: Israel 'forsook God who made him and scoffed at the Rock of his salvation'", "type": "ot"}
        ],

        "divine_council_note": "The covenant lawsuit (rib) of chapters 2-3 follows the pattern of divine "
                               "council legal proceedings. YHWH acts as both prosecutor and judge, summoning "
                               "heaven and earth as witnesses (cf. Deut 32:1; Isa 1:2). The accusation that "
                               "Israel has 'changed her glory' for idols (2:11) echoes the Deuteronomy 32 "
                               "framework: the nations were allotted to the sons of God, but Israel was YHWH's "
                               "own portion (Deut 32:8-9). By worshipping other gods, Israel has abandoned "
                               "the Most High for the subordinate members of the council -- or worse, for "
                               "entities that are 'not gods' (lo elohim) at all (2:11).",

        "sections": [
            {
                "heading": "The Memory of First Love (2:1-8)",
                "body": "YHWH opens the lawsuit with remembrance: 'I remember the devotion (chesed) of "
                        "your youth, your love (ahavah) as a bride, how you followed me in the wilderness, "
                        "in a land not sown' (2:2). Israel in the wilderness was like a young bride -- "
                        "devoted, trusting, following her husband into unknown territory. She was 'holy "
                        "to YHWH, the firstfruits (reshit) of his harvest' (2:3). The forensic question "
                        "follows: 'What wrong (avel) did your fathers find in me that they went far from "
                        "me, and went after worthlessness (hevel) and became worthless (vayyehbalu)?' "
                        "(2:5). The verb pattern is devastating: they pursued 'breath' (hevel) and became "
                        "'breath' themselves -- they became what they worshipped. The priests, rulers, "
                        "prophets, and Torah-handlers all failed: 'The priests did not say, \"Where is "
                        "YHWH?\"' (2:8)."
            },
            {
                "heading": "The Fountain and the Broken Cisterns (2:9-19)",
                "body": "YHWH brings the formal charge: 'Has a nation changed its gods, even though they "
                        "are no gods? But my people have changed their glory for that which does not profit' "
                        "(2:11). Even pagan nations maintain loyalty to their deities -- but Israel, who "
                        "has the living God, trades him for nothing. Then the central metaphor: 'My people "
                        "have committed two evils: they have forsaken me, the fountain of living waters "
                        "(meqor mayim chayyim), and hewn out cisterns for themselves, broken cisterns that "
                        "can hold no water' (2:13). In the arid landscape of Palestine, a spring of living "
                        "(flowing) water was the most precious resource -- reliable, self-renewing, life-giving. "
                        "A cistern is a poor substitute: stagnant, limited, prone to cracking. Israel has "
                        "abandoned the spring for cracked cisterns -- YHWH for idols. The double evil is "
                        "not merely choosing the wrong god but abandoning the real one."
            },
            {
                "heading": "The Adulterous Wife Who Cannot Return (2:20-3:5)",
                "body": "The marriage metaphor intensifies: 'Long ago you broke your yoke and burst your "
                        "bonds; and you said, \"I will not serve.\" Yes, on every high hill and under "
                        "every green tree you bowed down like a whore (zonah)' (2:20). The 'high places' "
                        "and 'green trees' are the sites of Canaanite fertility worship. Israel is described "
                        "as a 'restless young camel running here and there' (2:23) and 'a wild donkey used "
                        "to the wilderness, sniffing the wind in her desire' (2:24) -- driven by insatiable "
                        "appetite for other gods. Chapter 3 develops the legal complication: Deuteronomy "
                        "24:1-4 prohibits a divorced wife from returning to her first husband after "
                        "marrying another. Israel has 'played the whore with many lovers' (3:1) -- by "
                        "law, return should be impossible. Yet YHWH pleads: 'Return, faithless Israel... "
                        "I will not look on you in anger, for I am merciful (chasid)' (3:12). Grace "
                        "overrides the legal barrier."
            },
            {
                "heading": "The Call to Return (3:6-25)",
                "body": "YHWH draws a comparison between Israel (the northern kingdom) and Judah (the "
                        "southern kingdom). Israel was 'divorced' (sent into exile by Assyria in 722 BC), "
                        "but 'her treacherous sister Judah did not fear, but she too went and played the "
                        "whore' (3:8). Judah saw Israel's punishment and learned nothing. Despite this, "
                        "YHWH extends the astonishing invitation: 'Return, faithless children (shuvu "
                        "banim shovavim), declares YHWH, for I am your master (ba'al)' (3:14) -- the "
                        "wordplay on ba'al (master/husband, but also the name of the Canaanite deity) "
                        "is pointed. The vision of restoration includes a transformed worship: 'They "
                        "shall no more say, \"The ark of the covenant of YHWH.\" It shall not come to "
                        "mind or be remembered' (3:16) -- the ark, the supreme symbol of YHWH's "
                        "presence, will be superseded. Jerusalem itself will be 'the throne of YHWH' "
                        "(3:17), and 'all nations shall gather to it' -- a universalist eschatological "
                        "vision."
            }
        ]
    },

    {
        "id": "jer-7",
        "ref": "Jeremiah 7",
        "chapter_num": 7,
        "title": "The Temple Sermon -- 'Do Not Trust in Deceptive Words'",
        "era": "jeremiah_call",
        "type": "chapter",

        "synopsis": "The temple sermon is the most explosive public confrontation in Jeremiah's ministry. "
                    "Standing at the gate of YHWH's house, Jeremiah declares: 'Do not trust in these "
                    "deceptive words: \"The temple of YHWH, the temple of YHWH, the temple of YHWH\"' "
                    "(7:4). The threefold repetition mimics the popular mantra that the temple's presence "
                    "guaranteed Jerusalem's invincibility. Jeremiah demolishes this theology by invoking "
                    "Shiloh -- the earlier sanctuary YHWH destroyed because of Israel's wickedness: 'Go "
                    "now to my place that was in Shiloh, where I made my name dwell at first, and see "
                    "what I did to it because of the evil of my people Israel' (7:12). YHWH will do to "
                    "this temple what he did to Shiloh. The sermon exposes the hollowness of ritual "
                    "without righteousness and sets the stage for the temple's actual destruction in 586 BC.",

        "key_verse": {
            "ref": "Jeremiah 7:11",
            "text": "Has this house, which is called by my name, become a den of robbers in your eyes? Behold, I myself have seen it, declares the LORD.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "heikhal YHWH (temple of YHWH -- the threefold repetition mocks the false confidence in the temple)",
            "me'arat paritsim (den of robbers -- a hideout where thieves flee after committing crimes)",
            "Shiloh (the earlier sanctuary at Shiloh, destroyed ~1050 BC, proof that YHWH can abandon a sanctuary)",
            "sheqer (deception/falsehood -- the temple theology that YHWH would never destroy his own house)"
        ],

        "ane_backdrop": "Temple inviolability was a widespread ANE belief. Mesopotamian texts describe "
                        "temples as cosmically protected -- the dwelling of the god could not be "
                        "destroyed without the god's consent. The Assyrian annals record Sennacherib's "
                        "destruction of Babylon's temples as an act of supreme sacrilege. Jeremiah's "
                        "sermon overturns this theology: YHWH himself will destroy his own temple "
                        "because his people have turned it into a 'den of robbers.' The archaeological "
                        "evidence from Shiloh (Tell Seilun) confirms a destruction layer consistent "
                        "with Jeremiah's claim that YHWH had already destroyed one sanctuary.",

        "second_temple": [
            {
                "source": "Matthew 21:13 / Mark 11:17",
                "summary": "Jesus quotes Jeremiah 7:11 directly when cleansing the temple: 'You "
                           "have made it a den of robbers.'",
                "relevance": "Jesus explicitly invokes Jeremiah's temple sermon, signaling that the "
                             "Second Temple faces the same judgment as the First Temple -- and for "
                             "the same reasons."
            },
            {
                "source": "Acts 7:42-50",
                "summary": "Stephen's speech before the Sanhedrin argues that God 'does not dwell "
                           "in houses made with hands,' echoing Jeremiah's temple theology.",
                "relevance": "Stephen's martyrdom speech draws on Jeremiah's argument that the "
                             "temple is not an absolute guarantee of God's presence."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 21:13", "note": "Jesus quotes Jer 7:11 -- 'den of robbers' -- at the temple cleansing", "type": "nt"},
            {"ref": "1 Samuel 4:1-11", "note": "The capture of the ark at Shiloh -- the historical precedent Jeremiah invokes", "type": "ot"},
            {"ref": "Psalm 78:56-64", "note": "YHWH 'forsook his dwelling at Shiloh' -- the same event referenced by Jeremiah", "type": "ot"},
            {"ref": "Ezekiel 10-11", "note": "The glory of YHWH departing the temple -- the theological reality behind Jeremiah's warning", "type": "ot"},
            {"ref": "Acts 7:42-50", "note": "Stephen's speech: God does not dwell in temples made with hands", "type": "nt"}
        ],

        "divine_council_note": "The temple sermon asserts YHWH's sovereign freedom over his own sanctuary. "
                               "The popular theology assumed that YHWH's 'name' (shem) dwelling in the "
                               "temple guaranteed its inviolability -- a theology rooted in the legitimate "
                               "promise of 2 Samuel 7 and 1 Kings 8. Jeremiah reveals that this promise "
                               "was conditional: YHWH can withdraw his presence from his own house, just "
                               "as he withdrew from Shiloh. The divine council's decree overrides any "
                               "theology of automatic protection. The phrase 'den of robbers' (me'arat "
                               "paritsim) is particularly significant -- it does not mean the temple has "
                               "become a place of theft but a place where the wicked flee for safety after "
                               "committing injustice, treating YHWH's house as a criminal's hideout.",

        "sections": [
            {
                "heading": "The Triple Mantra Demolished (7:1-11)",
                "body": "YHWH stations Jeremiah at 'the gate of the house of YHWH' (7:2) -- the most "
                        "public possible location -- to deliver the most inflammatory possible message. "
                        "'Do not trust in these deceptive words (divrei ha-sheqer): \"The temple of YHWH, "
                        "the temple of YHWH, the temple of YHWH (heikhal YHWH, heikhal YHWH, heikhal "
                        "YHWH)\"' (7:4). The threefold repetition mimics a liturgical chant -- the people "
                        "have turned theology into a magical formula, believing that the temple's existence "
                        "makes them untouchable. YHWH's counter: 'If you truly amend your ways... if you "
                        "do not oppress the sojourner, the fatherless, or the widow, or shed innocent "
                        "blood... then I will let you dwell in this place' (7:5-7). The conditional nature "
                        "is absolute: justice, not ritual, is the condition of YHWH's continued presence. "
                        "Then the devastating accusation: 'Has this house, which is called by my name, "
                        "become a den of robbers (me'arat paritsim) in your eyes?' (7:11)."
            },
            {
                "heading": "Remember Shiloh (7:12-15)",
                "body": "'Go now to my place that was in Shiloh (Shilo), where I made my name dwell at "
                        "first (barishonah), and see what I did to it because of the evil of my people "
                        "Israel' (7:12). This is the argument that changes everything. Shiloh was the "
                        "primary sanctuary before Jerusalem -- the place where the tabernacle stood, "
                        "where the ark resided, where Samuel ministered. And YHWH destroyed it. The "
                        "archaeological evidence from Tell Seilun shows a destruction layer from "
                        "approximately 1050 BC, consistent with the Philistine devastation described "
                        "in 1 Samuel 4. If YHWH could abandon Shiloh, he can abandon Jerusalem. "
                        "'And now, because you have done all these things, declares YHWH... I will "
                        "do to the house that is called by my name... as I did to Shiloh' (7:13-14). "
                        "This is the divine council's verdict: the temple will fall."
            },
            {
                "heading": "The Queen of Heaven and Child Sacrifice (7:16-34)",
                "body": "The chapter's second half reveals the depth of Judah's apostasy. YHWH forbids "
                        "Jeremiah to intercede: 'Do not pray for this people... for I will not hear you' "
                        "(7:16). The intercession of the prophet -- the normal role of a divine council "
                        "mediator -- is now prohibited because the council's decree is final. Families "
                        "worship the 'Queen of Heaven' (melekhet ha-shamayim, 7:18) -- likely Ishtar or "
                        "Asherah -- with the whole family participating: children gather wood, fathers "
                        "kindle fire, women knead dough. Worse still: in the Valley of Hinnom (Ge-Hinnom, "
                        "from which 'Gehenna' derives), they burn their sons and daughters as offerings "
                        "to Molech (7:31). YHWH says: 'I did not command it, nor did it come into my "
                        "mind' (7:31) -- child sacrifice is utterly alien to YHWH's character. The valley "
                        "will become 'the Valley of Slaughter' (Ge Ha-Haregah, 7:32), and 'the dead "
                        "bodies of this people will be food for the birds of the air and for the beasts "
                        "of the earth' (7:33)."
            }
        ]
    },

    {
        "id": "jer-4-6",
        "ref": "Jeremiah 4-6",
        "chapter_num": 4,
        "title": "The Foe from the North -- Cosmic De-Creation",
        "era": "jeremiah_call",
        "type": "chapter",

        "synopsis": "Chapters 4-6 describe the coming Babylonian invasion in language that transcends "
                    "mere military conquest and reaches into cosmic de-creation. Jeremiah's vision of "
                    "the devastated land (4:23-26) deliberately reverses the creation language of "
                    "Genesis 1: 'I looked at the earth, and behold, it was without form and void (tohu "
                    "vavohu), and to the heavens, and they had no light. I looked at the mountains, and "
                    "behold, they were quaking... I looked, and behold, there was no man (adam), and all "
                    "the birds of the air had fled' (4:23-26). The Babylonian invasion is not merely a "
                    "political event -- it is an undoing of creation itself. YHWH commands Jeremiah to "
                    "search Jerusalem for one righteous person, as he searched Sodom (5:1; cf. Gen "
                    "18:22-32). None is found.",

        "key_verse": {
            "ref": "Jeremiah 4:23",
            "text": "I looked at the earth, and behold, it was without form and void; and to the heavens, and they had no light.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "tohu vavohu (without form and void -- the exact phrase from Gen 1:2, used nowhere else except here)",
            "tsafon (north -- both geographic and mythological; the direction of divine judgment and the mountain of the gods)",
            "adam (man/humanity -- the absence of humanity reverses the creation of Day 6)",
            "shuvu (return/repent -- the key imperative running through chapters 3-4)"
        ],

        "ane_backdrop": "The 'foe from the north' motif draws on ANE traditions of northern invasion "
                        "as divine judgment. In Mesopotamian literature, the north was associated with "
                        "the underworld and chaotic forces. The Canaanite Mount Zaphon (the divine "
                        "mountain) was in the far north. Jeremiah's de-creation language (4:23-26) is "
                        "unique in prophetic literature -- it describes the judgment not as destruction "
                        "but as the reversal of the creative order, returning the cosmos to its pre-"
                        "creation chaos. This is the most radical expression of covenant curse in the "
                        "Hebrew Bible: covenant violation does not merely bring punishment but undoes "
                        "creation itself.",

        "second_temple": [
            {
                "source": "2 Peter 3:10-12",
                "summary": "Peter's description of cosmic dissolution ('the heavens will pass away "
                           "with a roar') draws on the de-creation tradition inaugurated by Jeremiah.",
                "relevance": "The eschatological de-creation theme in the NT has its roots in "
                             "Jeremiah's vision of covenant judgment as cosmic reversal."
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 1:2", "note": "Tohu vavohu -- Jeremiah 4:23 is the only other use of this phrase, deliberately reversing creation", "type": "ot"},
            {"ref": "Genesis 18:22-32", "note": "Abraham bargains for Sodom -- Jeremiah 5:1 reprises the search for one righteous person", "type": "ot"},
            {"ref": "Isaiah 24:1-6", "note": "The 'Isaiah Apocalypse' describes cosmic devastation for covenant violation -- parallel to Jer 4", "type": "ot"},
            {"ref": "2 Peter 3:10-12", "note": "Eschatological de-creation -- the NT counterpart to Jeremiah's vision", "type": "nt"}
        ],

        "divine_council_note": "The de-creation vision of 4:23-26 carries divine council implications. If "
                               "creation was the act of the divine council ('Let us make man'), then de-"
                               "creation represents the council's reversal of its own work. The return to "
                               "tohu vavohu is not random destruction but sovereign dismantling -- the "
                               "council that ordered creation now disorders it in response to covenant "
                               "rebellion. The 'foe from the north' is YHWH's instrument, executing the "
                               "council's decree of judgment. The cosmic scope (no light in the heavens, "
                               "no birds, no humans, mountains quaking) indicates that the judgment "
                               "operates on both the earthly and heavenly planes -- the same dual judgment "
                               "described in Isaiah 24:21 ('YHWH will punish the host of heaven, in heaven, "
                               "and the kings of the earth, on the earth').",

        "sections": [
            {
                "heading": "If You Return, O Israel (4:1-4)",
                "body": "Before the judgment vision, YHWH offers the possibility of return: 'If you "
                        "return (tashuv), O Israel, declares YHWH, to me you should return (tashuv)' "
                        "(4:1). The condition: 'If you remove your detestable things from my presence, "
                        "and do not waver' (4:1). Then 'nations shall bless themselves in him, and in "
                        "him shall they glory' (4:2) -- the Abrahamic promise (Gen 12:3) is at stake. "
                        "The call to internal transformation: 'Circumcise yourselves to YHWH; remove "
                        "the foreskin of your hearts (orlat levavkhem)' (4:4). This anticipates the "
                        "New Covenant's promise of heart-transformation (31:33) and Paul's theology "
                        "of heart-circumcision (Rom 2:29)."
            },
            {
                "heading": "The Vision of De-Creation (4:5-31)",
                "body": "The alarm sounds: 'Blow the trumpet (shofar) through the land; cry aloud and "
                        "say, \"Assemble, and let us go into the fortified cities!\"' (4:5). A lion has "
                        "come up from his thicket (4:7) -- Babylon is the predator. Then the staggering "
                        "vision: 'I looked at the earth (ha-arets), and behold, it was tohu vavohu (without "
                        "form and void); and to the heavens (ha-shamayim), and they had no light. I looked "
                        "at the mountains, and behold, they were quaking (ro'ashim), and all the hills "
                        "moved to and fro. I looked, and behold, there was no man (adam), and all the "
                        "birds of the air had fled. I looked, and behold, the fruitful land was a desert, "
                        "and all its cities were laid in ruins before YHWH, before his fierce anger' "
                        "(4:23-26). Each 'I looked' (ra'iti) reverses a day of creation: earth without "
                        "form (Day 1), no light (Day 1/4), mountains shaking (Day 3), no birds (Day 5), "
                        "no humans (Day 6), no vegetation (Day 3). This is the most terrifying text in "
                        "the prophets -- the judgment for covenant violation is the unmaking of the world."
            },
            {
                "heading": "The Futile Search for One Righteous Person (5:1-6:30)",
                "body": "YHWH commands: 'Run to and fro through the streets of Jerusalem, look and take "
                        "note! Search her squares to see if you can find a man (ish), one who does "
                        "justice (mishpat) and seeks truth (emunah), that I may pardon her' (5:1). The "
                        "echo of Abraham's negotiation for Sodom (Gen 18:22-32) is unmistakable -- but "
                        "even Abraham's ten righteous cannot be found. The poor claim ignorance (5:4), "
                        "the great claim autonomy (5:5). 'Shall I not punish them for these things?' "
                        "YHWH asks (5:9). Chapter 6 describes the siege in graphic detail: 'Cut down "
                        "her trees; cast up a siege mound against Jerusalem' (6:6). The prophet's anguish "
                        "becomes unbearable: 'O daughter of my people, put on sackcloth and roll in "
                        "ashes; make mourning as for an only son, most bitter lamentation' (6:26). "
                        "Jeremiah himself is 'a tester and refiner' (6:27) among the people -- testing "
                        "them as silver, but finding only dross: 'Rejected silver (kesef nim'as) they "
                        "are called, for YHWH has rejected them' (6:30)."
            }
        ]
    },

    {
        "id": "jer-8-10",
        "ref": "Jeremiah 8-10",
        "chapter_num": 8,
        "title": "The Harvest Is Past -- Idolatry and Lament",
        "era": "jeremiah_call",
        "type": "chapter",

        "synopsis": "Chapters 8-10 continue the indictment of Judah's apostasy and develop the profound "
                    "lament that earns Jeremiah his title as the 'weeping prophet.' The devastating "
                    "pronouncement: 'The harvest is past, the summer is ended, and we are not saved' "
                    "(8:20) -- the time of opportunity has expired. Jeremiah weeps: 'O that my head "
                    "were waters, and my eyes a fountain of tears, that I might weep day and night for "
                    "the slain of the daughter of my people!' (9:1). Chapter 10 contrasts the living "
                    "God with the impotence of idols: 'Their idols are like scarecrows in a cucumber "
                    "field, and they cannot speak; they have to be carried, for they cannot walk' (10:5). "
                    "The true God is incomparable: 'YHWH is the true God (Elohim emet); he is the "
                    "living God (Elohim chayyim) and the everlasting King (Melek olam)' (10:10).",

        "key_verse": {
            "ref": "Jeremiah 9:23-24",
            "text": "Thus says the LORD: 'Let not the wise man boast in his wisdom, let not the mighty man boast in his might, let not the rich man boast in his riches, but let him who boasts boast in this, that he understands and knows me, that I am the LORD who practices steadfast love, justice, and righteousness in the earth.'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "chesed (steadfast love -- YHWH's primary self-description alongside mishpat and tsedaqah)",
            "mishpat (justice -- the exercise of righteous judgment)",
            "tsedaqah (righteousness -- conformity to YHWH's covenantal standard)",
            "Elohim emet (true God -- in contrast to the false gods/idols)",
            "Elohim chayyim (living God -- the fundamental distinction between YHWH and dead idols)"
        ],

        "ane_backdrop": "Jeremiah's idol polemic (10:1-16) engages directly with Mesopotamian idol-"
                        "manufacturing traditions. Babylonian ritual texts describe the 'mouth-washing' "
                        "(mis pi) and 'mouth-opening' (pit pi) ceremonies that transformed crafted "
                        "images into living deities. Jeremiah's mockery -- they are 'like scarecrows,' "
                        "they 'cannot speak,' they 'have to be carried' -- directly contradicts the "
                        "Babylonian claim that the gods inhabited their images. Isaiah 40:18-20 and "
                        "44:9-20 develop the same polemic. The Aramaic verse (10:11) may be a formula "
                        "Judeans were to recite to Babylonians: 'The gods who did not make the heavens "
                        "and the earth shall perish.'",

        "second_temple": [
            {
                "source": "1 Corinthians 1:31",
                "summary": "Paul quotes Jeremiah 9:24: 'Let the one who boasts, boast in the Lord.'",
                "relevance": "Paul applies Jeremiah's call to boast only in knowing YHWH to the "
                             "christological context of the cross as divine wisdom."
            },
            {
                "source": "2 Corinthians 10:17",
                "summary": "Paul again quotes Jeremiah 9:24 in the context of apostolic authority.",
                "relevance": "The Jeremianic principle of boasting only in YHWH becomes a Pauline "
                             "touchstone for authentic ministry."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 44:9-20", "note": "Isaiah's idol polemic -- the same theological argument as Jeremiah 10", "type": "ot"},
            {"ref": "1 Corinthians 1:31", "note": "Paul quotes Jer 9:24 -- boast in the Lord, not in wisdom or strength", "type": "nt"},
            {"ref": "Psalm 115:4-8", "note": "'Their idols are silver and gold, the work of human hands' -- parallel idol polemic", "type": "ot"},
            {"ref": "Acts 14:15", "note": "Paul at Lystra: 'Turn from these vain things to a living God' -- echoing Jeremiah's Elohim chayyim", "type": "nt"}
        ],

        "divine_council_note": "Chapter 10's contrast between YHWH and idols is a divine council argument. "
                               "The idols are 'not gods' (10:5) -- they are not members of the council, "
                               "not real elohim. YHWH alone is 'the true God, the living God, and the "
                               "everlasting King' (10:10). 'At his wrath the earth quakes, and the nations "
                               "cannot endure his indignation' (10:10) -- language of the divine warrior "
                               "who commands the council's forces. The climactic declaration: 'The gods who "
                               "did not make the heavens and the earth shall perish from the earth and from "
                               "under the heavens' (10:11, in Aramaic) -- the subordinate council members "
                               "who have been worshipped as gods will be judged and destroyed. Only the "
                               "Creator is truly God; the rest are pretenders.",

        "sections": [
            {
                "heading": "The Harvest Is Past (8:4-22)",
                "body": "Judah's stubbornness defies even nature: 'Even the stork in the heavens knows "
                        "her times, and the turtledove, swallow, and crane keep the time of their coming, "
                        "but my people know not the rules of YHWH' (8:7). Migratory birds follow their "
                        "divinely appointed patterns, but Israel ignores YHWH's Torah. The false prophets "
                        "cry 'Peace, peace (shalom, shalom)' when there is no peace (8:11) -- the same "
                        "accusation leveled in 6:14. Then the harvest metaphor: 'The harvest is past "
                        "(avar qatsir), the summer is ended (kalah qayits), and we are not saved (lo "
                        "nosha'nu)' (8:20). In the agricultural cycle, if the harvest and summer fruit "
                        "have passed without provision, starvation is certain. The time for repentance "
                        "has expired."
            },
            {
                "heading": "O That My Head Were Waters (9:1-11)",
                "body": "Jeremiah's personal anguish erupts: 'O that my head were waters (mi yitten roshi "
                        "mayim), and my eyes a fountain of tears (ueinai meqor dim'ah), that I might weep "
                        "day and night for the slain of the daughter of my people!' (9:1). This is the "
                        "verse that earned Jeremiah the title 'weeping prophet.' His tears are not weakness "
                        "but prophetic solidarity -- he weeps because YHWH weeps. The corruption is "
                        "pervasive: 'Everyone deceives his neighbor, and no one speaks the truth; they "
                        "have taught their tongue to speak lies' (9:5). The social fabric has disintegrated "
                        "completely."
            },
            {
                "heading": "Boast in Knowing YHWH (9:12-26)",
                "body": "The chapter climaxes with one of the most quoted passages in Jeremiah: 'Let not "
                        "the wise man boast in his wisdom, let not the mighty man boast in his might, let "
                        "not the rich man boast in his riches, but let him who boasts boast in this, that "
                        "he understands and knows me (haskel veyado'a oti), that I am YHWH who practices "
                        "steadfast love (chesed), justice (mishpat), and righteousness (tsedaqah) in the "
                        "earth' (9:23-24). Three human achievements -- wisdom, power, wealth -- are "
                        "dismissed as grounds for boasting. Only one thing matters: knowing YHWH and "
                        "knowing his character (chesed, mishpat, tsedaqah). This becomes a foundational "
                        "text for Paul (1 Cor 1:31; 2 Cor 10:17)."
            },
            {
                "heading": "The Living God vs. Dead Idols (10:1-16)",
                "body": "Chapter 10 develops a sustained idol polemic: 'The customs of the peoples are "
                        "vanity (hevel). A tree from the forest is cut down and worked with an axe by the "
                        "hands of a craftsman. They decorate it with silver and gold; they fasten it with "
                        "hammer and nails so that it cannot move. Their idols are like scarecrows in a "
                        "cucumber field (ketomer miqshah), and they cannot speak; they have to be carried, "
                        "for they cannot walk' (10:3-5). The contrast with YHWH is absolute: 'YHWH is "
                        "the true God (Elohim emet); he is the living God (Elohim chayyim) and the "
                        "everlasting King (Melek olam). At his wrath the earth quakes' (10:10). Then "
                        "the sole Aramaic verse in the book: 'The gods who did not make the heavens and "
                        "the earth shall perish from the earth and from under the heavens' (10:11). The "
                        "chapter concludes with a creation hymn: 'It is he who made the earth by his "
                        "power, who established the world by his wisdom, and by his understanding "
                        "stretched out the heavens' (10:12)."
            }
        ]
    }
]
