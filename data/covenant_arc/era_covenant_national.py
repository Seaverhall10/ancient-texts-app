"""
era_covenant_national.py -- The Covenant Arc: National Covenants (Chapters 4-6)

The Mosaic covenant, the Davidic covenant, and the covenant lawsuit that
followed Israel's failure. These three chapters trace the arc from Sinai
to exile: a bilateral covenant given, a royal promise secured, and a
covenant broken with devastating consequences.

The Mosaic covenant is the ONLY bilateral covenant in Scripture -- both
parties have obligations. Every other major covenant (Abrahamic, Davidic,
New) is unilateral -- God binds himself. This distinction is the hinge
on which all of covenant theology turns.

Evidence tiers throughout:
  [A] Direct Scripture -- explicit biblical text
  [B] Valid inference -- drawn from Scripture by sound reasoning
  [C] Ancient parallel -- ANE, DSS, or documentary evidence

Hebrew-first approach: every theological claim begins with the Hebrew or
Greek terminology, then builds the interpretation. Torah before theology.

Sources: ESV (Scripture), Michael S. Heiser (The Unseen Realm), Meredith
Kline (Treaty of the Great King), Kenneth Kitchen (On the Reliability of
the Old Testament), N.T. Wright (The Climax of the Covenant), John
Walton (Ancient Near Eastern Thought and the Old Testament), G.E.
Mendenhall (Law and Covenant in Israel and the Ancient Near East).
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 4: THE MOSAIC COVENANT -- SINAI AND THE SUZERAIN TREATY
    # =========================================================================
    {
        "id": "covenant-mosaic-sinai",
        "ref": "Exodus 19-24",
        "chapter_num": 4,
        "title": "The Mosaic Covenant \u2014 Sinai and the Suzerain Treaty",
        "era": "covenant_arc_national",
        "type": "chapter",

        "synopsis": (
            "At Sinai, YHWH enters into a covenant with Israel that is unique "
            "in all of Scripture: it is the only BILATERAL covenant. Every "
            "other major covenant -- Abrahamic, Davidic, New -- is unilateral, "
            "with God binding himself unconditionally. The Mosaic covenant is "
            "different: 'If you will indeed obey my voice and keep my covenant, "
            "you shall be my treasured possession' (Ex 19:5). That 'if' changes "
            "everything. The structure follows the ANE suzerain-vassal treaty "
            "pattern exactly: preamble identifying the sovereign ('I am YHWH "
            "your God'), historical prologue recounting past benefits ('who "
            "brought you out of Egypt'), stipulations binding the vassal (the "
            "Ten Commandments and the Book of the Covenant), provision for "
            "deposit and public reading, witnesses, and blessings and curses "
            "for obedience or disobedience. The blood ceremony of Exodus "
            "24:3-8 seals it: Moses takes the blood, throws half against the "
            "altar and half on the people, and declares, 'Behold the blood of "
            "the covenant that YHWH has made with you.' This covenant is GOOD "
            "-- Paul insists on this (Rom 7:12, 'the law is holy'). But it is "
            "also TEMPORARY -- designed to expose sin, not to solve it."
        ),

        "key_verse": {
            "ref": "Exodus 19:5-6",
            "text": (
                "Now therefore, if you will indeed obey my voice and keep "
                "my covenant, you shall be my treasured possession among all "
                "peoples, for all the earth is mine; and you shall be to me "
                "a kingdom of priests and a holy nation."
            ),
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05ea\u05d5\u05b9\u05e8\u05b8\u05d4 (torah)",
                "meaning": (
                    "'Instruction,' 'teaching,' 'direction' -- from the root "
                    "yarah, 'to throw, to shoot, to direct.' Torah does NOT "
                    "mean 'law' in the modern legislative sense. It means "
                    "instruction from a father to a child, direction for life. "
                    "The LXX translation nomos ('law') narrowed the meaning "
                    "and has shaped Western misunderstanding ever since. Torah "
                    "encompasses narrative, poetry, prophecy, and legal "
                    "material -- it is YHWH's comprehensive instruction for "
                    "his covenant people, not a mere legal code."
                )
            },
            {
                "term": "\u05d1\u05b0\u05bc\u05e8\u05b4\u05d9\u05ea (berit)",
                "meaning": (
                    "'Covenant' -- the foundational relational term in "
                    "Scripture. A berit is a solemn, binding agreement, often "
                    "ratified by blood sacrifice (the verb 'to make a "
                    "covenant' is karat berit, literally 'to cut a covenant,' "
                    "referring to the cutting of sacrificial animals). Unlike "
                    "a contract (bilateral by definition), a berit can be "
                    "unilateral (God binds himself alone, as with Abraham) or "
                    "bilateral (both parties have obligations, as at Sinai)."
                )
            },
            {
                "term": "\u05e1\u05b0\u05d2\u05bb\u05dc\u05bc\u05b8\u05d4 (segullah)",
                "meaning": (
                    "'Treasured possession,' 'special property' -- from a "
                    "root meaning 'to shut up, to treasure.' In the ANE, "
                    "segullah referred to a king's private treasure as "
                    "distinct from general state wealth. YHWH calls Israel "
                    "his segullah (Ex 19:5, Deut 7:6, 14:2, 26:18) -- his "
                    "personal, valued possession among all nations. [B] This "
                    "is not favoritism but election for purpose: Israel is "
                    "treasured in order to be 'a kingdom of priests' -- "
                    "mediating YHWH's presence to the nations."
                )
            },
            {
                "term": "\u05de\u05b7\u05de\u05b0\u05dc\u05b6\u05db\u05b6\u05ea \u05db\u05b9\u05d4\u05b2\u05e0\u05b4\u05d9\u05dd (mamlechet kohanim)",
                "meaning": (
                    "'Kingdom of priests' -- a collective priestly vocation "
                    "for the entire nation. Israel's role among the nations "
                    "mirrors the priest's role within Israel: to stand between "
                    "God and people, mediating his presence and instruction. "
                    "[B] This corporate calling is later echoed in 1 Peter "
                    "2:9 (basileion hierateuma, 'a royal priesthood') -- "
                    "applied to the ekklesia, the new covenant community."
                )
            }
        ],

        "ane_backdrop": (
            "The Mosaic covenant follows the structure of second-millennium "
            "BC Hittite suzerain-vassal treaties with remarkable precision. "
            "Kenneth Kitchen and Meredith Kline independently identified the "
            "six-element pattern: (1) Preamble identifying the great king -- "
            "'I am YHWH your God' (Ex 20:2a). (2) Historical prologue "
            "recounting the sovereign's past benefits -- 'who brought you out "
            "of the land of Egypt, out of the house of slavery' (Ex 20:2b). "
            "(3) Stipulations -- the Ten Commandments (Ex 20:3-17) plus the "
            "Book of the Covenant (Ex 21-23). (4) Provision for deposit in "
            "the sanctuary and periodic public reading (Deut 31:9-13). (5) "
            "Witnesses -- 'heaven and earth' (Deut 30:19), paralleling ANE "
            "invocation of divine witnesses. (6) Blessings for obedience and "
            "curses for violation (Deut 28). [C] This parallel is significant "
            "because it locates the Mosaic covenant firmly in its historical "
            "context. YHWH is not borrowing a pagan form -- he is the true "
            "suzerain, the Great King, and the ANE treaty form is the "
            "appropriate vehicle for a sovereign addressing his vassals. The "
            "first-millennium Assyrian treaties (7th c. BC) differ in "
            "structure, lacking the historical prologue -- which argues for "
            "an early (Mosaic-era) date for Deuteronomy, not the late date "
            "preferred by critical scholars."
        ),

        "second_temple": [
            {
                "source": "Dead Sea Scrolls -- Temple Scroll (11QT)",
                "summary": (
                    "The Temple Scroll from Qumran presents itself as a "
                    "direct divine speech rewriting Deuteronomy in the first "
                    "person -- YHWH giving instructions for an ideal temple "
                    "and its practices. The Qumran community viewed the "
                    "Mosaic covenant as still binding but believed the "
                    "Jerusalem establishment had corrupted its administration. "
                    "Their withdrawal to the desert was an act of covenant "
                    "faithfulness, awaiting a purified priesthood."
                ),
                "relevance": (
                    "[C] The Qumran community's radical commitment to "
                    "covenant purity demonstrates how seriously Second Temple "
                    "Jews took the Mosaic framework. Their critique of the "
                    "temple establishment parallels the prophetic riv -- "
                    "covenant prosecution of those who claimed to represent "
                    "YHWH but violated his terms."
                )
            },
            {
                "source": "Jubilees 1:1-4",
                "summary": (
                    "The Book of Jubilees presents Sinai as the culmination "
                    "of a covenant history stretching back to creation. It "
                    "emphasizes that the Torah was inscribed on heavenly "
                    "tablets before being given to Moses -- the law is not "
                    "merely historical legislation but an eternal divine "
                    "order. Jubilees insists on strict calendar observance "
                    "as a covenant marker."
                ),
                "relevance": (
                    "[C] Jubilees reflects the Second Temple emphasis on "
                    "Torah as cosmic order, not just national legislation. "
                    "This tradition shaped how Jews understood Sinai: not as "
                    "one covenant among many, but as the definitive revelation "
                    "of God's will for his people."
                )
            }
        ],

        "cross_refs": [
            {
                "ref": "Exodus 20:1-17",
                "note": (
                    "[A] The Ten Commandments (aseret ha-devarim, 'ten words') "
                    "-- the stipulations of the suzerain treaty. The first "
                    "four govern the relationship with YHWH; the last six "
                    "govern relationships within the covenant community."
                ),
                "type": "ot"
            },
            {
                "ref": "Exodus 24:3-8",
                "note": (
                    "[A] The blood ceremony ratifying the covenant. Moses "
                    "throws half the blood on the altar (representing YHWH) "
                    "and half on the people -- both parties are bound by "
                    "blood. 'Behold the blood of the covenant' (dam ha-berit)."
                ),
                "type": "ot"
            },
            {
                "ref": "Romans 7:7-12",
                "note": (
                    "[A] Paul's defense of the Torah: 'Is the law sin? By no "
                    "means!' The law is holy, righteous, and good -- but its "
                    "function is diagnostic, not curative. It reveals sin "
                    "without providing the power to overcome it."
                ),
                "type": "nt"
            },
            {
                "ref": "Galatians 3:19-24",
                "note": (
                    "[A] The Torah as paidagogos -- a household tutor who "
                    "supervises children until maturity. The law was 'added "
                    "because of transgressions, until the offspring should "
                    "come to whom the promise had been made.' It was never "
                    "the destination -- it was the road to Christ."
                ),
                "type": "nt"
            },
            {
                "ref": "Hebrews 9:18-22",
                "note": (
                    "[A] The author of Hebrews directly links the Sinai blood "
                    "ceremony to Christ: 'Not even the first covenant was "
                    "inaugurated without blood.' The Mosaic pattern of blood "
                    "ratification foreshadows the blood of the new covenant."
                ),
                "type": "nt"
            },
            {
                "ref": "Deuteronomy 28",
                "note": (
                    "[A] The blessings and curses section of the suzerain "
                    "treaty. Obedience yields prosperity, fruitfulness, and "
                    "security. Disobedience yields famine, plague, siege, "
                    "exile, and horror. These curses activate in Chapter 6."
                ),
                "type": "ot"
            }
        ],

        "divine_council_note": (
            "The Sinai theophany is a divine council event. YHWH descends on "
            "the mountain with thunder, lightning, thick cloud, and the sound "
            "of a trumpet (Ex 19:16-19) -- the standard elements of a divine "
            "council assembly. Deuteronomy 33:2 makes this explicit: 'YHWH "
            "came from Sinai... he came from the ten thousands of holy ones, "
            "with flaming fire at his right hand.' The 'holy ones' (qodesh) "
            "are members of the divine council -- the heavenly host present "
            "at the covenant ratification. [B] Acts 7:53 and Galatians 3:19 "
            "both state that the law was 'delivered through angels' "
            "(diatageis angelon) -- mediated by divine beings. This does not "
            "diminish the Torah's authority; it situates it within YHWH's "
            "cosmic administration. The giving of the Torah was not a private "
            "transaction between God and Moses but a public decree of the "
            "divine council, witnessed by the heavenly host and ratified in "
            "blood before the assembled nation. [C] This parallels ANE "
            "treaty-making where the gods of both parties served as "
            "witnesses. At Sinai, the 'gods' are real -- the bene elohim "
            "of YHWH's council -- but they are witnesses, not co-sovereigns. "
            "YHWH alone is the great king."
        ),

        "sections": [
            {
                "heading": "The Only Bilateral Covenant",
                "body": (
                    "[A] The word 'if' (im) in Exodus 19:5 sets the Mosaic "
                    "covenant apart from every other major covenant in "
                    "Scripture. 'If you will indeed obey my voice and keep "
                    "my covenant, you shall be my segullah.' Compare this "
                    "with the Abrahamic covenant, where God alone passes "
                    "between the animal pieces while Abraham sleeps (Gen "
                    "15:12-17) -- no conditions, no 'if.' Compare it with "
                    "the Davidic covenant: 'When he commits iniquity, I "
                    "will discipline him... but my steadfast love will not "
                    "depart' (2 Sam 7:14-15) -- discipline, but never "
                    "abandonment. The Mosaic covenant alone requires Israel's "
                    "obedience as a condition for the relationship. [B] This "
                    "is not a flaw -- it is by design. The bilateral "
                    "covenant creates the conditions for Israel to demonstrate "
                    "either faithfulness or failure. And since Israel is "
                    "composed of the same fallen humanity as everyone else, "
                    "failure was inevitable. The Torah was never meant to be "
                    "the solution to sin. It was meant to demonstrate that "
                    "sin NEEDS a solution that human obedience cannot provide."
                )
            },
            {
                "heading": "The Suzerain-Vassal Treaty Structure",
                "body": (
                    "[C] The Mosaic covenant follows the six-part structure "
                    "of second-millennium Hittite suzerain-vassal treaties "
                    "identified by George Mendenhall and Meredith Kline. "
                    "(1) Preamble: 'I am YHWH your God' (Ex 20:2a) -- the "
                    "sovereign identifies himself. (2) Historical prologue: "
                    "'who brought you out of the land of Egypt' (Ex 20:2b) "
                    "-- recounting past benefits that obligate the vassal. "
                    "(3) Stipulations: the Decalogue (Ex 20:3-17) and the "
                    "Book of the Covenant (Ex 21-23). (4) Deposit and "
                    "reading: the tablets placed in the ark (Deut 10:1-5) "
                    "and the command to read the Torah every seven years "
                    "(Deut 31:10-13). (5) Witnesses: 'I call heaven and "
                    "earth to witness against you today' (Deut 30:19). "
                    "(6) Blessings and curses: Deuteronomy 28 in full. "
                    "[B] This structure matters because it demonstrates "
                    "that YHWH is operating as the legitimate sovereign "
                    "king -- not negotiating with Israel as an equal, but "
                    "graciously establishing terms with a people he has "
                    "already delivered. The treaty is offered from a "
                    "position of accomplished redemption: 'I brought you "
                    "out' comes BEFORE 'now obey.' Grace precedes law."
                )
            },
            {
                "heading": "The Blood of the Covenant",
                "body": (
                    "[A] Exodus 24:3-8 records the ratification ceremony. "
                    "Moses builds an altar and twelve pillars. Young men "
                    "offer burnt offerings and peace offerings. Moses takes "
                    "half the blood and throws it against the altar "
                    "(representing YHWH's side). He reads the Book of the "
                    "Covenant aloud. The people respond: 'All that YHWH has "
                    "spoken we will do, and we will be obedient' (na'aseh "
                    "ve-nishma, literally 'we will do and we will hear'). "
                    "Then Moses throws the remaining blood on the people "
                    "and declares: 'Behold the blood of the covenant that "
                    "YHWH has made with you.' Both parties are bound by the "
                    "same blood. [B] This ceremony is the direct background "
                    "for Jesus' words at the Last Supper: 'This is my blood "
                    "of the covenant, which is poured out for many' (Mark "
                    "14:24). Jesus is not inventing new language -- he is "
                    "invoking Exodus 24. But where Moses sprinkled animal "
                    "blood on a temporary covenant, Jesus offers his own "
                    "blood for an everlasting one. The Mosaic ceremony was "
                    "always pointing forward."
                )
            },
            {
                "heading": "Torah as Pedagogue -- Good but Temporary",
                "body": (
                    "[A] Paul's argument in Galatians 3:19-24 is essential "
                    "for understanding the Mosaic covenant's purpose. 'Why "
                    "then the law? It was added because of transgressions, "
                    "until the offspring should come to whom the promise had "
                    "been made' (3:19). The Torah had an expiration date "
                    "built in -- it was 'until' (achris hou) Christ. Paul "
                    "uses the metaphor of the paidagogos -- not a teacher in "
                    "the modern sense, but a household slave who supervised "
                    "children, walked them to school, and enforced discipline "
                    "until they came of age. 'The law was our paidagogos "
                    "until Christ came, in order that we might be justified "
                    "by faith' (3:24). [B] This does not make the Torah bad. "
                    "Romans 7:12 insists it is 'holy and righteous and good.' "
                    "But its function was diagnostic: it revealed the disease "
                    "of sin without providing the cure. It was the X-ray, not "
                    "the surgery. It held Israel in custody (phroureo, Gal "
                    "3:23 -- 'guarded,' 'confined') until faith was revealed. "
                    "[B] The Mosaic covenant's temporary design is precisely "
                    "what makes the unconditional covenants (Abrahamic, "
                    "Davidic) so critical. They carry the promise through "
                    "Israel's failure and out the other side."
                )
            },
            {
                "heading": "The Seventy Elders and the Covenant Meal",
                "body": (
                    "[A] After the blood ceremony, something extraordinary "
                    "happens. Moses, Aaron, Nadab, Abihu, and seventy elders "
                    "of Israel ascend the mountain and 'they saw the God of "
                    "Israel' (Ex 24:10). Under his feet was 'a pavement of "
                    "sapphire stone, like the very heaven for clearness.' "
                    "And the text says: 'He did not lay his hand on the "
                    "chief men of Israel; they beheld God, and ate and drank' "
                    "(24:11). [B] This is a covenant meal in the divine "
                    "presence -- eating and drinking before God, sealed by "
                    "blood, witnessed by the elders. It is the OT prototype "
                    "for the Lord's Supper: a meal in God's presence that "
                    "ratifies a covenant sealed in blood. The seventy elders "
                    "represent the nation, just as the twelve disciples "
                    "represent the restored Israel at the Last Supper. The "
                    "pattern is consistent: covenant, blood, meal, presence. "
                    "What Moses inaugurated with animal blood on a mountain, "
                    "Jesus fulfilled with his own blood in an upper room."
                )
            }
        ]
    },

    # =========================================================================
    # CHAPTER 5: THE DAVIDIC COVENANT -- HOUSE, THRONE, KINGDOM FOREVER
    # =========================================================================
    {
        "id": "covenant-davidic-promise",
        "ref": "2 Samuel 7",
        "chapter_num": 5,
        "title": "The Davidic Covenant \u2014 House, Throne, Kingdom Forever",
        "era": "covenant_arc_national",
        "type": "chapter",

        "synopsis": (
            "In 2 Samuel 7, YHWH makes a covenant with David that reshapes "
            "the entire trajectory of redemptive history. David wants to build "
            "God a house (bayit -- a temple). God responds with a stunning "
            "reversal: 'I will build YOU a house' -- not a building but a "
            "dynasty. Three promises emerge: a house (dynasty), a throne "
            "(kingship), and a kingdom (realm) -- and all three are FOREVER "
            "(ad olam). Like the Abrahamic covenant and unlike the Mosaic, "
            "the Davidic covenant is unilateral. God binds himself. 'When he "
            "commits iniquity, I will discipline him with the rod of men... "
            "but my steadfast love (chesed) will not depart from him' "
            "(7:14-15). Discipline, yes. Revocation, never. The Davidic son "
            "will be called 'son of God' (7:14) -- a phrase quoted directly "
            "in Hebrews 1:5 for Jesus. Psalm 89 celebrates this covenant. "
            "Psalm 132 reaffirms it. But the exile poses a devastating "
            "question: Jehoiachin is cursed (Jer 22:30), the dynasty appears "
            "to end. How does Jesus solve this? Through two genealogies -- "
            "one biological (Luke 3, through Mary), one legal (Matthew 1, "
            "through Joseph) -- bypassing the curse while maintaining both "
            "Davidic claims."
        ),

        "key_verse": {
            "ref": "2 Samuel 7:16",
            "text": (
                "And your house and your kingdom shall be made sure forever "
                "before me. Your throne shall be established forever."
            ),
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05d7\u05b6\u05e1\u05b6\u05d3 (chesed)",
                "meaning": (
                    "'Steadfast love,' 'covenant loyalty,' 'lovingkindness' "
                    "-- one of the richest words in biblical Hebrew, with no "
                    "single English equivalent. Chesed is loyal love that "
                    "persists because of covenant commitment, not because the "
                    "recipient deserves it. It is YHWH's defining covenant "
                    "attribute (Ex 34:6-7). In the Davidic covenant, chesed "
                    "is what guarantees the promise survives human failure: "
                    "'My chesed will not depart from him' (2 Sam 7:15). [B] "
                    "Chesed is not mere sentiment -- it is covenantal "
                    "obligation rooted in divine character."
                )
            },
            {
                "term": "\u05d1\u05b7\u05bc\u05d9\u05b4\u05ea (bayit)",
                "meaning": (
                    "'House' -- the wordplay in 2 Samuel 7 is built on this "
                    "single word. David wants to build God a bayit (temple). "
                    "God responds that he will build David a bayit (dynasty). "
                    "The entire chapter turns on this double meaning. David "
                    "thinks in terms of architecture; God thinks in terms of "
                    "lineage. The physical temple David's son Solomon will "
                    "build is temporary. The dynastic house God establishes "
                    "is forever."
                )
            },
            {
                "term": "\u05e2\u05b7\u05d3 \u05e2\u05d5\u05b9\u05dc\u05b8\u05dd (ad olam)",
                "meaning": (
                    "'Forever,' 'to eternity,' 'for the age' -- ad means "
                    "'until' or 'as far as,' olam means 'a long duration,' "
                    "'perpetuity,' 'eternity.' When applied to the Davidic "
                    "covenant, ad olam appears three times in 2 Sam 7:13,16 "
                    "-- house, throne, kingdom are all established ad olam. "
                    "This is not hyperbole. The NT treats it as a literal, "
                    "unbreakable divine commitment fulfilled in Jesus, whose "
                    "'kingdom will have no end' (Luke 1:33)."
                )
            },
            {
                "term": "\u05de\u05b8\u05e9\u05b4\u05c1\u05d9\u05d7\u05b7 (mashiach)",
                "meaning": (
                    "'Anointed one' -- from mashach, 'to smear, to anoint.' "
                    "Kings, priests, and occasionally prophets were anointed "
                    "with oil as a sign of divine selection. David is called "
                    "YHWH's mashiach (2 Sam 22:51, Ps 2:2, Ps 18:50). The "
                    "term eventually narrowed to mean THE Anointed One -- the "
                    "ultimate Davidic king who would fulfill all the covenant "
                    "promises. In Greek: christos. Jesus of Nazareth = Yeshua "
                    "ha-Mashiach, the Anointed Son of David."
                )
            }
        ],

        "ane_backdrop": (
            "Royal grant covenants in the ANE were gifts from a sovereign "
            "to a faithful servant -- unconditional and irrevocable. The "
            "Davidic covenant matches this pattern. Like the Abrahamic "
            "covenant, it is a divine grant, not a bilateral treaty. [C] "
            "Moshe Weinfeld demonstrated that the Davidic covenant parallels "
            "Hittite and Akkadian royal grant texts, where a king rewards a "
            "loyal vassal with a permanent land grant or dynasty. The grant "
            "could not be revoked even if future generations proved unworthy "
            "-- only the current offender would be punished, while the grant "
            "itself endured. This is precisely the logic of 2 Sam 7:14-15: "
            "individual sons will be disciplined, but the dynasty will never "
            "be removed. [C] The 'son of God' language in 7:14 also reflects "
            "ANE royal ideology, where the king was considered the adopted "
            "son of the deity. In Egypt, the pharaoh was 'son of Ra.' In "
            "Israel, the Davidic king is 'son of YHWH' -- not by nature "
            "(as in pagan mythology) but by covenant adoption. Psalm 2:7 "
            "makes this explicit: 'You are my Son; today I have begotten "
            "you' -- a coronation formula declaring the king's adopted "
            "sonship. Jesus transforms this adopted sonship into something "
            "far greater: he is the Son not by adoption but by nature "
            "(John 1:1-3, Col 1:15-17), making the Davidic promise "
            "infinitely more than any ANE king could have imagined."
        ),

        "second_temple": [
            {
                "source": "Psalms of Solomon 17:21-32 (1st c. BC)",
                "summary": (
                    "This Jewish text from the late Second Temple period "
                    "prays for the coming 'son of David' to purge Jerusalem "
                    "of Gentile rulers, destroy the unrighteous, and gather "
                    "a holy people. It reflects the widespread expectation "
                    "of a military-political Messiah who would restore the "
                    "Davidic kingdom in visible, earthly terms."
                ),
                "relevance": (
                    "[C] This text shows what most Jews expected the Davidic "
                    "covenant to produce: a warrior king who would overthrow "
                    "Rome and establish Israel's political sovereignty. "
                    "Jesus' fulfillment of the Davidic covenant defied these "
                    "expectations entirely -- a crucified king whose kingdom "
                    "is 'not of this world' (John 18:36). The Davidic "
                    "covenant is fulfilled, but not in the way anyone "
                    "anticipated."
                )
            },
            {
                "source": "Dead Sea Scrolls -- 4Q174 (Florilegium)",
                "summary": (
                    "This Qumran text interprets 2 Samuel 7:10-14 as a "
                    "prophecy of the eschatological temple and the messianic "
                    "'Branch of David' who will arise in the last days. The "
                    "community read the Davidic covenant as pointing to a "
                    "future fulfillment beyond the historical dynasty."
                ),
                "relevance": (
                    "[C] The Qumran community's interpretation confirms that "
                    "Second Temple Jews read the Davidic covenant as "
                    "eschatological -- pointing beyond Solomon and the "
                    "historical kings to an ultimate Davidic figure. This "
                    "messianic reading is precisely what the NT claims Jesus "
                    "fulfills."
                )
            }
        ],

        "cross_refs": [
            {
                "ref": "2 Samuel 7:12-16",
                "note": (
                    "[A] The core Davidic promise: offspring, house, throne, "
                    "kingdom -- all established forever. 'I will be to him a "
                    "father, and he shall be to me a son' (7:14)."
                ),
                "type": "ot"
            },
            {
                "ref": "Psalm 89:3-4, 19-37",
                "note": (
                    "[A] The covenant hymn celebrating YHWH's oath to David: "
                    "'I have made a covenant with my chosen one... I will "
                    "establish your offspring forever and build your throne "
                    "for all generations.' But Ps 89:38-51 then laments the "
                    "apparent failure of this covenant in exile."
                ),
                "type": "ot"
            },
            {
                "ref": "Psalm 132:11-12",
                "note": (
                    "[A] 'YHWH swore to David a sure oath from which he will "
                    "not turn back: One of the sons of your body I will set "
                    "on your throne.' An oath, not a contract. YHWH has bound "
                    "himself."
                ),
                "type": "ot"
            },
            {
                "ref": "Jeremiah 22:28-30",
                "note": (
                    "[A] The Jehoiachin curse: 'Write this man down as "
                    "childless... for none of his offspring shall succeed in "
                    "sitting on the throne of David.' This creates the "
                    "genealogical crisis that the dual genealogies of Jesus "
                    "resolve."
                ),
                "type": "ot"
            },
            {
                "ref": "Hebrews 1:5",
                "note": (
                    "[A] Direct quotation of 2 Sam 7:14: 'I will be to him "
                    "a father, and he shall be to me a son' -- applied to "
                    "Jesus as the ultimate Davidic heir, superior to angels."
                ),
                "type": "nt"
            },
            {
                "ref": "Luke 1:32-33",
                "note": (
                    "[A] Gabriel to Mary: 'The Lord God will give to him the "
                    "throne of his father David, and he will reign over the "
                    "house of Jacob forever, and of his kingdom there will "
                    "be no end.' Direct Davidic covenant language."
                ),
                "type": "nt"
            },
            {
                "ref": "Matthew 1:1-17 / Luke 3:23-38",
                "note": (
                    "[B] The two genealogies solve the Jehoiachin problem. "
                    "Matthew traces Joseph's legal line through Solomon and "
                    "Jehoiachin -- giving Jesus legal right to the throne. "
                    "Luke traces Mary's biological line through Nathan (another "
                    "son of David) -- bypassing the Jehoiachin curse entirely. "
                    "Legal claim through Joseph, biological descent through "
                    "Mary. The virgin birth is not just a miracle -- it is a "
                    "genealogical necessity."
                ),
                "type": "nt"
            }
        ],

        "divine_council_note": (
            "The Davidic covenant places the human king within YHWH's cosmic "
            "administration. Psalm 2 -- the royal coronation psalm -- presents "
            "the Davidic king as YHWH's installed ruler over the nations: "
            "'I have set my King on Zion, my holy hill... Ask of me, and I "
            "will make the nations your heritage' (Ps 2:6,8). [B] This is a "
            "direct reversal of the Deuteronomy 32:8-9 arrangement, where "
            "the nations were allotted to the sons of God while YHWH kept "
            "Israel. Now YHWH's Davidic king is promised authority OVER those "
            "same nations -- reclaiming what was given away at Babel. The "
            "'son of God' title in 2 Sam 7:14 and Ps 2:7 positions the "
            "Davidic king as YHWH's vice-regent within the divine council "
            "hierarchy. [B] Psalm 110:1 takes this further: 'YHWH says to "
            "my lord: Sit at my right hand, until I make your enemies your "
            "footstool.' The Davidic king is invited to sit at YHWH's right "
            "hand -- the position of supreme authority in the divine council. "
            "Jesus claims exactly this position (Mark 14:62), which is why "
            "the high priest tears his robes: not because Jesus claims to be "
            "Messiah (a human title), but because he claims the divine "
            "prerogative of sitting at YHWH's right hand and coming on the "
            "clouds -- the cloud-rider, an exclusively divine attribute "
            "(Dan 7:13). The Davidic covenant set up this cosmic claim. "
            "Jesus fulfilled it in a way that exceeded all expectations."
        ),

        "sections": [
            {
                "heading": "The Bayit Wordplay -- Temple and Dynasty",
                "body": (
                    "[A] Second Samuel 7 opens with David troubled that he "
                    "lives in a house (bayit) of cedar while the ark of God "
                    "dwells in a tent. He tells Nathan the prophet: I should "
                    "build God a proper bayit. That night, YHWH speaks to "
                    "Nathan with one of the great reversals in Scripture: "
                    "'Would you build me a house to dwell in?... YHWH "
                    "declares to you that YHWH will make YOU a house' "
                    "(7:5,11). The entire oracle pivots on the word bayit. "
                    "David thinks architecturally -- a building of stone. "
                    "God thinks dynastically -- a lineage of kings. Solomon "
                    "will build the physical temple, and it will eventually "
                    "be destroyed. The dynastic bayit endures forever. [B] "
                    "This reversal establishes a principle that runs through "
                    "all of Scripture: God does not need what humans offer "
                    "him. He gives what humans could never produce for "
                    "themselves. David cannot build a dynasty by his own "
                    "power -- only God can establish a house that stands "
                    "forever."
                )
            },
            {
                "heading": "Unconditional but Not Without Discipline",
                "body": (
                    "[A] The critical distinction in the Davidic covenant is "
                    "between discipline and revocation. 'When he commits "
                    "iniquity, I will discipline him with the rod of men, "
                    "with the stripes of the sons of men, but my steadfast "
                    "love (chesed) will not depart from him, as I took it "
                    "from Saul' (7:14-15). The comparison with Saul is "
                    "deliberate. God's chesed DID depart from Saul -- his "
                    "dynasty ended after one generation. David's dynasty will "
                    "endure through failure. Individual kings will be "
                    "punished, sometimes severely (exile being the ultimate "
                    "discipline), but the line will never be permanently cut "
                    "off. [B] This is the genius of the unconditional "
                    "covenant: it accommodates human failure without being "
                    "nullified by it. The Mosaic covenant breaks under the "
                    "weight of Israel's sin. The Davidic covenant bends but "
                    "holds. The exile tests this promise to its limit -- and "
                    "the promise survives, vindicated in the resurrection of "
                    "a crucified Davidic king."
                )
            },
            {
                "heading": "Son of God -- From Coronation to Incarnation",
                "body": (
                    "[A] 'I will be to him a father, and he shall be to me "
                    "a son' (2 Sam 7:14). In its original context, this "
                    "establishes the Davidic king as YHWH's adopted son -- "
                    "a coronation formula mirrored in Psalm 2:7: 'You are "
                    "my Son; today I have begotten you.' Every Davidic king "
                    "bore this title by covenant adoption. [B] But the NT "
                    "takes this further. Hebrews 1:5 quotes both 2 Sam 7:14 "
                    "and Psalm 2:7 and applies them to Jesus -- not as "
                    "adoption language but as a declaration of his unique "
                    "divine sonship. The author of Hebrews argues that Jesus "
                    "is superior to the angels precisely because he bears "
                    "this title in a way no angel ever has. [B] The Davidic "
                    "covenant created a category -- 'son of God' as royal "
                    "title -- that Jesus fills with content far exceeding "
                    "its original scope. David's sons were adopted into "
                    "divine sonship. Jesus IS the divine Son who entered "
                    "the Davidic line. The arrow of adoption reverses: not "
                    "a man elevated to divine status, but God incarnate "
                    "entering a human dynasty."
                )
            },
            {
                "heading": "The Jehoiachin Curse and the Two Genealogies",
                "body": (
                    "[A] Jeremiah 22:28-30 pronounces a devastating curse on "
                    "Jehoiachin (Coniah), the last ruling Davidic king before "
                    "the exile: 'Write this man down as childless, a man who "
                    "shall not succeed in his days, for none of his offspring "
                    "shall succeed in sitting on the throne of David.' This "
                    "creates an apparent contradiction: the Davidic covenant "
                    "promises an eternal dynasty, but the last king in the "
                    "line is cursed. [B] The NT resolves this through the "
                    "two genealogies. Matthew 1 traces Joseph's line through "
                    "Solomon and Jehoiachin -- giving Jesus the LEGAL right "
                    "to David's throne through his adoptive father. Luke 3 "
                    "traces Mary's line through Nathan, another son of David "
                    "-- establishing Jesus' BIOLOGICAL Davidic descent while "
                    "completely bypassing the Jehoiachin curse. The virgin "
                    "birth is not merely a miracle but a genealogical "
                    "necessity: Jesus must be legally of Joseph's line "
                    "(for the throne claim) but not biologically of "
                    "Jehoiachin's line (to avoid the curse). The incarnation "
                    "is the only mechanism that satisfies both requirements "
                    "simultaneously."
                )
            },
            {
                "heading": "The Melchizedekian Complication",
                "body": (
                    "[A] The Davidic covenant creates a king from the tribe "
                    "of Judah. But the Mosaic covenant restricts priesthood "
                    "to the tribe of Levi. No Davidic king could ever be a "
                    "Levitical priest -- wrong tribe. Yet Psalm 110:4, a "
                    "Davidic psalm, declares: 'YHWH has sworn and will not "
                    "change his mind: You are a priest forever after the "
                    "order of Melchizedek.' The Davidic king is a priest -- "
                    "but not a Levitical one. He holds a priesthood that "
                    "predates Levi entirely, going back to Genesis 14 and "
                    "Melchizedek, king of Salem and priest of El Elyon. [A] "
                    "Hebrews 7:13-14 makes the point explicit: 'The one of "
                    "whom these things are spoken belonged to another tribe, "
                    "from which no one has ever served at the altar. For it "
                    "is evident that our Lord was descended from Judah, and "
                    "in connection with that tribe Moses said nothing about "
                    "priests.' [B] The Mosaic priesthood was tribal and "
                    "temporary. The Melchizedekian priesthood is personal "
                    "and eternal. Jesus holds both the Davidic throne and "
                    "the Melchizedekian priesthood -- king and priest in "
                    "one person, something the Mosaic system could never "
                    "produce. The Davidic covenant pointed to a figure who "
                    "would transcend the Mosaic categories entirely."
                )
            }
        ]
    },

    # =========================================================================
    # CHAPTER 6: THE BROKEN COVENANT -- EXILE AND THE RIV
    # =========================================================================
    {
        "id": "covenant-exile-riv",
        "ref": "Hosea 4:1, Micah 6:1-2",
        "chapter_num": 6,
        "title": "The Broken Covenant \u2014 Exile and the Riv",
        "era": "covenant_arc_national",
        "type": "chapter",

        "synopsis": (
            "Israel broke the Mosaic covenant systematically and persistently. "
            "The prophets -- far from being inspirational speakers or social "
            "commentators -- functioned as covenant prosecutors. The Hebrew "
            "word riv means 'lawsuit,' 'legal dispute,' 'case at law.' When "
            "Hosea says 'YHWH has a riv against the inhabitants of the land' "
            "(4:1), he is not expressing disappointment -- he is serving "
            "legal notice. When Micah calls the mountains to 'hear YHWH's "
            "riv' (6:1-2), he is summoning witnesses for a cosmic courtroom "
            "proceeding. The prophets were royal messengers dispatched from "
            "YHWH's divine council (the heavenly courtroom) to deliver the "
            "verdict to the covenant-breaking vassal. The curses of "
            "Deuteronomy 28 activated in full: famine, plague, siege, exile, "
            "and horror. In 722 BC, the northern kingdom of Israel fell to "
            "Assyria. In 586 BC, Judah fell to Babylon. The Temple -- YHWH's "
            "dwelling place -- was destroyed. The covenant APPEARED to have "
            "failed. But it had not -- because the Abrahamic and Davidic "
            "covenants are unconditional. Only the Mosaic covenant was "
            "bilateral, and only the bilateral covenant was broken. The exile "
            "proved the Mosaic covenant's limitations and set the stage for "
            "the New Covenant promised in Jeremiah 31."
        ),

        "key_verse": {
            "ref": "Hosea 4:1",
            "text": (
                "Hear the word of the LORD, O children of Israel, for "
                "the LORD has a controversy with the inhabitants of the "
                "land. There is no faithfulness or steadfast love, and "
                "no knowledge of God in the land."
            ),
            "translation": "ESV"
        },

        "hebrew_terms": [
            {
                "term": "\u05e8\u05b4\u05d9\u05d1 (riv)",
                "meaning": (
                    "'Lawsuit,' 'legal dispute,' 'controversy,' 'case at "
                    "law' -- the technical term for YHWH's covenant lawsuit "
                    "against Israel. The prophetic riv follows a recognizable "
                    "legal pattern: summons of witnesses (often cosmic -- "
                    "heaven, earth, mountains), statement of the charges, "
                    "recital of past benefits (what YHWH has done), "
                    "accusation of breach, and pronouncement of sentence. "
                    "The prophets were not merely inspired poets -- they were "
                    "covenant prosecutors delivering YHWH's legal case "
                    "against a treaty-breaking vassal nation."
                )
            },
            {
                "term": "\u05d2\u05b8\u05bc\u05dc\u05d5\u05bc\u05ea (galut)",
                "meaning": (
                    "'Exile,' 'deportation,' 'diaspora' -- from galah, 'to "
                    "uncover, to reveal, to go into exile.' The wordplay is "
                    "theologically rich: Israel's sin is 'uncovered' (galah) "
                    "and the punishment is to be 'uncovered' from the land "
                    "-- stripped of homeland, temple, and visible divine "
                    "presence. Exile was not random disaster but the specific "
                    "covenant curse of Deuteronomy 28:36,64 activating."
                )
            },
            {
                "term": "\u05d1\u05b0\u05bc\u05e8\u05b4\u05d9\u05ea \u05e2\u05d5\u05b9\u05dc\u05b8\u05dd (berit olam)",
                "meaning": (
                    "'Everlasting covenant' -- the term applied to the "
                    "Abrahamic (Gen 17:7,13,19) and Davidic (2 Sam 23:5, "
                    "Isa 55:3) covenants but NOT to the Mosaic. The Mosaic "
                    "covenant is a berit but never a berit olam. [B] This "
                    "distinction is crucial in the exile: the berit olam "
                    "covenants survive Israel's failure precisely because "
                    "they do not depend on Israel's obedience. The Mosaic "
                    "covenant breaks because it was bilateral. The "
                    "everlasting covenants endure because God alone bears "
                    "the obligation."
                )
            },
            {
                "term": "\u05e0\u05b8\u05d1\u05b4\u05d9\u05d0 (navi)",
                "meaning": (
                    "'Prophet' -- one called to speak for another. The navi "
                    "is not primarily a predictor of the future but a "
                    "spokesman for YHWH -- a messenger from the divine "
                    "council dispatched with a specific word. [B] The "
                    "prophetic call narratives (Isa 6, Jer 1, Ezek 1-3) "
                    "all depict the prophet in the divine council receiving "
                    "a commission. They are not independent commentators "
                    "but authorized emissaries. Their riv oracles carry the "
                    "weight of the divine court's verdict."
                )
            }
        ],

        "ane_backdrop": (
            "The prophetic riv follows ANE treaty-lawsuit conventions with "
            "remarkable precision. When a suzerain's vassal violated the "
            "treaty, the sovereign would dispatch messengers to (1) recite "
            "past benefits, (2) enumerate violations, (3) summon witnesses, "
            "and (4) announce consequences. [C] The Hittite treaties include "
            "examples of such covenant lawsuits, where the great king "
            "addresses the vassal through messengers before military action. "
            "Israel's prophets function exactly as these treaty messengers "
            "-- they are royal envoys from YHWH the suzerain, delivering "
            "formal notice of covenant violation before the 'military' "
            "response (Assyria, Babylon) arrives. The cosmic witnesses "
            "summoned in Micah 6:1-2 ('Hear, O mountains, YHWH's riv') "
            "parallel the ANE practice of invoking mountains, rivers, and "
            "heaven as treaty witnesses. In pagan treaties, these were "
            "deified forces. In Israel's covenant, they are creation itself "
            "-- the natural order testifying to the breakdown of the "
            "covenant order. [C] The exile itself follows ANE patterns of "
            "vassal deportation. Both Assyria and Babylon practiced mass "
            "deportation as imperial policy -- removing populations from "
            "their homeland to break national identity. What is unique "
            "about Israel's exile is its theological interpretation: this "
            "was not merely imperial conquest but covenant curse fulfillment."
        ),

        "second_temple": [
            {
                "source": "2 Baruch 1:1-5 (late 1st c. AD)",
                "summary": (
                    "This apocalyptic text addresses the destruction of the "
                    "Second Temple (70 AD) through the lens of the first "
                    "destruction. It portrays God as having withdrawn from "
                    "the temple BEFORE the Babylonians arrived: 'Do you "
                    "think that this is the city of which I said: On the "
                    "palms of my hands I have carved you? This building "
                    "that is now built in your midst is not that which is "
                    "revealed with me.' The real temple is in heaven."
                ),
                "relevance": (
                    "[C] Second Baruch reflects the theological struggle "
                    "to understand exile: Did God fail? No -- God withdrew "
                    "his presence as covenant discipline. The earthly temple "
                    "was never the ultimate reality. This reasoning directly "
                    "parallels Ezekiel's vision of God's glory departing the "
                    "temple (Ezek 10-11) before the Babylonian destruction."
                )
            },
            {
                "source": "Dead Sea Scrolls -- 4QMMT (Halakhic Letter)",
                "summary": (
                    "This Qumran text functions as a covenant lawsuit in "
                    "miniature. The community accuses the Jerusalem temple "
                    "establishment of violating the covenant through "
                    "improper halakhic practice and appeals to the 'blessings "
                    "and curses' framework of Deuteronomy as evidence that "
                    "covenant violation is occurring."
                ),
                "relevance": (
                    "[C] 4QMMT demonstrates that the riv framework was not "
                    "just an ancient prophetic genre but a living legal "
                    "tradition in Second Temple Judaism. The Qumran community "
                    "saw themselves as prosecuting the same kind of covenant "
                    "case that Hosea and Micah had brought centuries earlier."
                )
            }
        ],

        "cross_refs": [
            {
                "ref": "Hosea 4:1-3",
                "note": (
                    "[A] The classic riv opening: 'YHWH has a riv with the "
                    "inhabitants of the land.' The charges: no faithfulness "
                    "(emet), no chesed, no knowledge of God (da'at elohim). "
                    "The consequence extends to creation itself -- 'the land "
                    "mourns, and all who dwell in it languish.'"
                ),
                "type": "ot"
            },
            {
                "ref": "Micah 6:1-8",
                "note": (
                    "[A] The most complete riv passage in Scripture. YHWH "
                    "summons the mountains as witnesses (6:1-2), recites "
                    "past benefits (6:3-5), and the accused asks what "
                    "offering could atone (6:6-7). The answer bypasses "
                    "ritual entirely: 'Do justice, love chesed, walk humbly "
                    "with your God' (6:8)."
                ),
                "type": "ot"
            },
            {
                "ref": "Deuteronomy 28:15-68",
                "note": (
                    "[A] The covenant curses in devastating detail: disease, "
                    "drought, defeat, siege, cannibalism, and exile. 'YHWH "
                    "will scatter you among all peoples, from one end of the "
                    "earth to the other' (28:64). The exile was not a "
                    "surprise -- it was spelled out in advance."
                ),
                "type": "ot"
            },
            {
                "ref": "Deuteronomy 30:19",
                "note": (
                    "[A] 'I call heaven and earth to witness against you "
                    "today' -- the treaty witness clause. Heaven and earth "
                    "are summoned as witnesses to the covenant, and they will "
                    "testify against Israel when the covenant is broken."
                ),
                "type": "ot"
            },
            {
                "ref": "Isaiah 6:1-13",
                "note": (
                    "[A] Isaiah's throne-room vision -- the prophet is "
                    "commissioned in the divine council. He sees YHWH on "
                    "his throne, hears the deliberation ('Whom shall I "
                    "send?'), and is dispatched with a message of judgment. "
                    "The prophet is a divine council messenger."
                ),
                "type": "ot"
            },
            {
                "ref": "Jeremiah 25:11-12",
                "note": (
                    "[A] The seventy-year exile prophesied: 'This whole land "
                    "shall become a ruin and a waste, and these nations shall "
                    "serve the king of Babylon seventy years.' Covenant curse "
                    "with a built-in time limit -- because the unconditional "
                    "covenants guarantee restoration."
                ),
                "type": "ot"
            },
            {
                "ref": "Jeremiah 31:31-34",
                "note": (
                    "[A] The New Covenant promise that emerges from the "
                    "ashes of the broken Mosaic covenant: 'I will put my "
                    "law within them, and I will write it on their hearts.' "
                    "Not a new set of rules -- the same Torah internalized "
                    "by the Spirit. The Mosaic covenant failed because it "
                    "was external. The New Covenant succeeds because it is "
                    "internal."
                ),
                "type": "ot"
            },
            {
                "ref": "Ezekiel 10-11",
                "note": (
                    "[A] The glory (kavod) of YHWH departs the temple in "
                    "stages -- from the inner sanctuary to the threshold "
                    "(10:4), to the east gate (10:19), to the Mount of "
                    "Olives (11:23). God leaves before Babylon arrives. The "
                    "temple is destroyed because God has already departed."
                ),
                "type": "ot"
            },
            {
                "ref": "Romans 9:4-5",
                "note": (
                    "[A] Paul affirms that the covenants (plural) belong to "
                    "Israel -- and have not been revoked. The exile did not "
                    "annul God's promises. 'The gifts and the calling of God "
                    "are irrevocable' (Rom 11:29)."
                ),
                "type": "nt"
            }
        ],

        "divine_council_note": (
            "The prophets are divine council messengers. This is not "
            "metaphor -- the prophetic call narratives explicitly depict the "
            "prophet standing in YHWH's council and receiving a commission. "
            "Isaiah 6: the prophet sees YHWH enthroned with seraphim, hears "
            "the council deliberation ('Whom shall I send?'), and volunteers "
            "as messenger. 1 Kings 22:19-23: Micaiah sees YHWH on his throne "
            "with the host of heaven (tseva ha-shamayim) standing beside him, "
            "deliberating how to judge Ahab. Jeremiah 23:18,22: 'Who among "
            "them has stood in the council (sod) of YHWH to see and to hear "
            "his word?... If they had stood in my council, they would have "
            "proclaimed my words to my people.' [B] The false prophets' crime "
            "is that they speak WITHOUT standing in the divine council. They "
            "invent their own message. The true prophet has been in the "
            "throne room, has heard the verdict, and delivers it faithfully. "
            "The riv is therefore not a human critique of society but a "
            "divine verdict delivered by authorized messengers from the "
            "highest court in the cosmos. When Hosea says 'YHWH has a riv,' "
            "he is not editorializing -- he is reading the court's ruling. "
            "[B] The exile itself is the divine council's sentence being "
            "executed. Assyria and Babylon are instruments of YHWH's "
            "judgment (Isa 10:5 -- 'Assyria, the rod of my anger'). The "
            "cosmic court has rendered its verdict, and earthly empires "
            "carry it out without knowing they serve a higher purpose."
        ),

        "sections": [
            {
                "heading": "The Riv: Covenant Lawsuit from the Divine Council",
                "body": (
                    "[A] The riv pattern appears across the prophetic "
                    "literature with consistent legal structure. Hosea 4:1: "
                    "'YHWH has a riv with the inhabitants of the land.' "
                    "Micah 6:1-2: 'Hear what YHWH says: Arise, plead (riv) "
                    "your case before the mountains, and let the hills hear "
                    "your voice. Hear, you mountains, the riv of YHWH.' "
                    "Isaiah 1:2-3: 'Hear, O heavens, and give ear, O earth; "
                    "for YHWH has spoken: Children have I reared and brought "
                    "up, but they have rebelled against me.' [B] This is "
                    "not prophetic emotion -- it is legal procedure. The "
                    "pattern matches ANE covenant-lawsuit conventions: (1) "
                    "summons of witnesses (mountains, heavens, earth), (2) "
                    "recital of past benefits ('I brought you out of Egypt'), "
                    "(3) enumeration of violations (idolatry, injustice, "
                    "covenant breaking), (4) pronouncement of sentence "
                    "(exile, destruction). The prophets are covenant "
                    "prosecutors, not inspired commentators. They speak with "
                    "the authority of the divine court because they have "
                    "BEEN in the divine court."
                )
            },
            {
                "heading": "The Charges: How Israel Broke the Covenant",
                "body": (
                    "[A] The prophetic indictment is comprehensive. Hosea "
                    "4:1-2 lists the charges: 'There is no faithfulness "
                    "(emet), no steadfast love (chesed), and no knowledge "
                    "of God (da'at elohim) in the land; there is swearing, "
                    "lying, murder, stealing, and committing adultery.' Note "
                    "the structure: three covenant virtues absent (emet, "
                    "chesed, da'at), five covenant violations present "
                    "(directly echoing the Decalogue). Isaiah adds: "
                    "injustice toward the poor (1:17,23), meaningless "
                    "ritual without heart change (1:11-15), and alliance "
                    "with foreign powers instead of trust in YHWH (30:1-2). "
                    "Jeremiah adds: worship of Baal and other gods in the "
                    "very temple of YHWH (7:9-11). Ezekiel adds: the "
                    "abominations practiced in the temple's inner chambers "
                    "(ch. 8). [B] The pattern is always the same: idolatry "
                    "and injustice together. Vertical covenant failure "
                    "(worshiping other gods) always produces horizontal "
                    "covenant failure (exploiting other people). The two are "
                    "inseparable in prophetic theology."
                )
            },
            {
                "heading": "The Curses Activate: 722 and 586 BC",
                "body": (
                    "[A] Deuteronomy 28 spelled out the covenant curses in "
                    "advance with horrifying specificity. Siege (28:49-52): "
                    "'A nation whose language you do not understand' will "
                    "besiege your cities -- Assyria, then Babylon. "
                    "Cannibalism during siege (28:53-57): fulfilled in 2 "
                    "Kings 6:28-29 and Lamentations 4:10. Exile and "
                    "dispersion (28:64): 'YHWH will scatter you among all "
                    "peoples.' In 722 BC, Assyria conquered the northern "
                    "kingdom and deported its population. The ten tribes "
                    "were scattered and never reconstituted as a political "
                    "entity. In 586 BC, Babylon conquered Judah, destroyed "
                    "Jerusalem, burned the temple, and deported the "
                    "surviving population to Babylon. [B] The exile was "
                    "not divine cruelty -- it was covenant consequence. "
                    "Every curse had been specified in advance, agreed to "
                    "by the people at Sinai ('All that YHWH has spoken we "
                    "will do,' Ex 24:7), and warned about by prophet after "
                    "prophet for centuries. The bilateral covenant had "
                    "bilateral consequences."
                )
            },
            {
                "heading": "The Glory Departs: Ezekiel's Devastating Vision",
                "body": (
                    "[A] Ezekiel 10-11 records the most theologically "
                    "devastating event in the OT: the kavod (glory, "
                    "weighty presence) of YHWH leaving the temple. The "
                    "departure happens in stages, as if God is reluctant "
                    "to leave: from the inner sanctuary to the threshold "
                    "(10:4), from the threshold to the east gate (10:19), "
                    "from the east gate to the Mount of Olives (11:23). "
                    "Each stage moves further from the center of Israel's "
                    "worship, further from the holy of holies where YHWH's "
                    "presence dwelt above the cherubim. [B] The temple's "
                    "destruction by Babylon was not the cause of God's "
                    "departure -- it was the consequence. God left FIRST. "
                    "The building was already an empty shell when Babylon "
                    "burned it. The loss was not architectural but "
                    "relational: YHWH's dwelling among his people -- the "
                    "whole point of the tabernacle and temple -- was "
                    "withdrawn. [B] Note the departure route: the kavod "
                    "stops at the Mount of Olives. Centuries later, Jesus "
                    "will ascend from the Mount of Olives (Acts 1:12) and "
                    "return in the same way (Acts 1:11). The glory that "
                    "departed from the east returns from the east."
                )
            },
            {
                "heading": "What Did NOT Fail: The Unconditional Covenants Endure",
                "body": (
                    "[B] The exile exposed a critical distinction that runs "
                    "through the entire covenant arc. The Mosaic covenant "
                    "was bilateral -- and it broke. But the Abrahamic "
                    "covenant was unilateral: God alone passed through the "
                    "animal pieces (Gen 15). The Davidic covenant was "
                    "unilateral: 'My chesed will not depart' (2 Sam 7:15). "
                    "These covenants do not depend on Israel's obedience "
                    "and therefore cannot be nullified by Israel's failure. "
                    "[A] This is why Jeremiah, in the very midst of "
                    "pronouncing judgment, also proclaims: 'Behold, the "
                    "days are coming, declares YHWH, when I will make a "
                    "new covenant with the house of Israel... I will put "
                    "my torah within them, and I will write it on their "
                    "hearts' (31:31-33). The New Covenant is announced "
                    "during the exile because the exile proves the Mosaic "
                    "covenant's limitations. What external law could not "
                    "accomplish -- because human nature cannot sustain "
                    "perfect obedience -- an internal covenant will achieve "
                    "through the Spirit. [B] The exile was not the end of "
                    "the story. It was the pivot point. The failure of the "
                    "bilateral covenant created the space for the "
                    "announcement of the final, eternal, unilateral covenant "
                    "that would write torah not on stone but on the human "
                    "heart."
                )
            }
        ]
    }
]
