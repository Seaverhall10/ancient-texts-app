"""
era_54_solomon_glory.py -- Solomon's Glory and Apostasy (1 Kings 1-11)

David's son Solomon is anointed king, receives unparalleled wisdom from YHWH,
constructs and dedicates the Temple as the cosmic dwelling place of the divine
Name, hosts the Queen of Sheba, and ultimately falls into apostasy by building
high places for the territorial deities of his foreign wives. The Temple
dedication prayer (1 Kings 8) is the theological apex of the Deuteronomistic
History: YHWH's Name dwells in the house, the heavens cannot contain him, and
the nations are invited to pray toward this place. Solomon's apostasy is the
hinge on which the kingdom breaks.
"""

CHAPTERS = [
    {
        "id": "1kgs-1",
        "ref": "1 Kings 1",
        "chapter_num": 1,
        "title": "Adonijah's Bid and Solomon's Anointing",
        "era": "solomon_glory",
        "type": "chapter",
        "themes": ["KING", "SEED", "COV"],

        "synopsis": "David is old and feeble. His son Adonijah, the eldest surviving prince, "
                    "attempts to seize the throne by hosting a sacrificial feast at En-rogel, "
                    "enlisting Joab the general and Abiathar the priest. But Nathan the prophet "
                    "and Bathsheba intervene, reminding David of his oath that Solomon would "
                    "succeed him. David commands Zadok the priest, Nathan the prophet, and "
                    "Benaiah the warrior to anoint Solomon at the Gihon spring. Solomon rides "
                    "David's royal mule -- a public declaration of succession. The trumpet "
                    "sounds, the people shout 'Long live King Solomon!' and the earth splits "
                    "with the noise (1:40). Adonijah's feast collapses in panic. The chapter "
                    "establishes that Solomon's kingship is not by military coup but by "
                    "prophetic designation and royal decree -- YHWH's chosen king installed "
                    "through the institutional triad of priest, prophet, and warrior.",

        "key_verse": {
            "ref": "1 Kings 1:39",
            "text": "There Zadok the priest took the horn of oil from the tent and anointed Solomon. Then they blew the trumpet, and all the people said, 'Long live King Solomon!'",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "mashach (to anoint -- the act that designates YHWH's chosen king; root of mashiach, 'anointed one,' which becomes 'Messiah' in English via Greek Christos. Every Israelite king was a mashiach, but the term eventually pointed to THE ultimate Anointed One)",
            "shofar (ram's horn trumpet -- the instrument of royal proclamation and divine theophany; its blast marks coronations, holy days, and the coming day of YHWH)",
            "gichon (Gihon spring -- Jerusalem's primary water source; the name echoes the river of Eden, Gen 2:13, connecting the anointing site to paradise geography)",
            "pirdah (mule -- the royal mount; riding the king's mule was a public claim to the throne, an ANE succession convention)",
            "kohen (priest -- Zadok, the faithful priest who anoints Solomon; Abiathar, who backed Adonijah, descends from Eli's condemned line)",
            "navi (prophet -- Nathan the navi orchestrates the succession; the prophet's role in king-making is uniquely Israelite -- no Mesopotamian king required prophetic authorization)"
        ],

        "ane_backdrop": "Royal succession in the ancient Near East was rarely smooth. Egyptian, "
                        "Hittite, and Mesopotamian records attest to frequent succession crises, "
                        "palace coups, and fratricidal wars. The Hittite 'Edict of Telepinu' "
                        "(~1525 BC) attempted to regulate succession to prevent civil war. In "
                        "Egypt, co-regency was used to secure transitions. What scholars call "
                        "the 'Succession Narrative' (the connected narrative running from 2 Samuel "
                        "9 through 1 Kings 2 that traces who will succeed David on the throne) is "
                        "one of the earliest examples of sustained prose history in world literature. "
                        "Adonijah's feast at En-rogel follows the ANE pattern of a pretender "
                        "rallying supporters with a sacrificial banquet -- a quasi-religious "
                        "coronation. Solomon's anointing at the Gihon spring is the counter-ceremony: "
                        "legitimate, prophetically authorized, and conducted at a site associated "
                        "with Jerusalem's sacred geography. ANE royal ideology (the belief that the "
                        "king was the deity's earthly representative, ruling on the god's behalf) "
                        "shaped Israel's monarchy, but with a critical difference: the Israelite "
                        "king was never divine himself -- he was YHWH's vice-regent, accountable to "
                        "Torah, and subject to prophetic correction. No Mesopotamian king required "
                        "prophetic authorization for his throne.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities VII.14.4-10",
                "summary": "Josephus expands the succession narrative with dramatic detail, "
                           "portraying Nathan as a shrewd political operator who outmaneuvers "
                           "Adonijah's faction.",
                "relevance": "Josephus understood the succession crisis as both political and "
                             "theological: Solomon's anointing was YHWH's will enacted through "
                             "human agency."
            }
        ],

        "cross_refs": [
            {"ref": "2 Samuel 7:12-13", "note": "YHWH's promise to David: 'I will raise up your offspring... he shall build a house for my name'", "type": "ot"},
            {"ref": "1 Chronicles 22:9-10", "note": "David told explicitly that Solomon (shelomoh, 'peace') would build the Temple", "type": "ot"},
            {"ref": "Psalm 2:6-7", "note": "'I have set my King on Zion, my holy hill' -- the anointed king installed by divine decree", "type": "ot"},
            {"ref": "Psalm 72:1", "note": "'Give the king your justice, O God, and your righteousness to the royal son' -- a Solomon psalm", "type": "ot"}
        ],

        "divine_council_note": "Solomon's anointing at the Gihon spring carries cosmic geography "
                               "overtones. The name Gihon is one of the four rivers of Eden (Gen "
                               "2:13), and the spring feeds the Kidron Valley below the Temple Mount. "
                               "The anointing of YHWH's chosen king at a site named after an Eden "
                               "river, adjacent to the mountain where the Temple will be built, "
                               "connects the monarchy to the Eden-temple-divine presence complex. "
                               "Solomon is being installed as YHWH's vice-regent on the cosmic "
                               "mountain -- the earthly king who rules on behalf of the heavenly King.",

        "sections": [
            {
                "heading": "Adonijah's Presumption (1:1-10)",
                "body": "David is old and unable to keep warm; Abishag the Shunammite is brought "
                        "to attend him. Adonijah ('my lord is YHWH'), the son of Haggith and now "
                        "the eldest surviving prince after Amnon and Absalom, 'exalted himself, "
                        "saying, I will be king' (1:5). The narrator notes that David 'had never at "
                        "any time displeased him by asking, Why have you done thus and so?' (1:6) -- "
                        "a pattern of parental indulgence that echoes Eli with his sons (1 Sam 2-3). "
                        "Adonijah recruits Joab, David's battle-hardened general, and Abiathar the "
                        "priest -- both men with long service to David but now backing the pretender. "
                        "Significantly, Zadok the priest, Benaiah the warrior, Nathan the prophet, "
                        "and the gibborim (David's elite warriors) do not join Adonijah. The faction "
                        "lines are drawn: the old guard (Joab, Abiathar) versus the loyalists "
                        "(Zadok, Nathan, Benaiah). Adonijah holds a sacrificial feast at the Stone "
                        "of Zoheleth beside En-rogel, inviting all his brothers and the royal "
                        "officials of Judah -- but pointedly excluding Solomon, Nathan, and "
                        "Benaiah. The exclusion reveals his intent: this is a coronation banquet "
                        "designed to present the court with a fait accompli."
            },
            {
                "heading": "Nathan and Bathsheba's Intervention (1:11-27)",
                "body": "Nathan the prophet acts with urgency. He approaches Bathsheba: 'Have you "
                        "not heard that Adonijah the son of Haggith has become king and David our "
                        "lord does not know it?' (1:11). Nathan instructs Bathsheba to go to David "
                        "and remind him of his oath that Solomon would reign, then promises to "
                        "follow her in and confirm the report. The strategy is deliberate: "
                        "Bathsheba presents the personal appeal (the mother and wife invoking a "
                        "royal oath), Nathan provides the prophetic authority (the mouthpiece of "
                        "YHWH confirming the succession). Bathsheba enters David's chamber and "
                        "recounts the crisis: 'My lord, you swore to your servant by the LORD your "
                        "God, saying, Solomon your son shall reign after me' (1:17). She warns that "
                        "if Adonijah succeeds, she and Solomon will be counted as offenders -- "
                        "a euphemism for execution. Nathan enters and confirms everything. The "
                        "double witness (Deut 19:15) compels David to act."
            },
            {
                "heading": "Solomon Anointed at the Gihon (1:28-40)",
                "body": "David responds with an oath: 'As the LORD lives, who has redeemed my "
                        "soul out of every adversity, as I swore to you by the LORD, the God of "
                        "Israel, saying, Solomon your son shall reign after me... I will do it "
                        "this day' (1:29-30). The command is precise: Zadok, Nathan, and Benaiah "
                        "shall take Solomon on the king's mule to the Gihon spring, anoint him "
                        "with oil from the horn in the tent (the sacred oil of royal anointing), "
                        "and blow the trumpet. Solomon descends to the Gihon, Zadok anoints him, "
                        "and the people erupt: 'Long live King Solomon!' The celebration is so "
                        "exuberant that 'the earth was split by their noise' (1:40) -- hyperbolic "
                        "language that links the human acclamation to cosmic response, as if "
                        "creation itself acknowledges YHWH's chosen king. The Gihon spring as "
                        "the site of anointing is theologically significant: it is Jerusalem's "
                        "primary water source, located in the Kidron Valley beneath the future "
                        "Temple Mount. Water, kingship, and sacred mountain converge at one point."
            },
            {
                "heading": "Adonijah's Feast Dissolves (1:41-53)",
                "body": "The sound of celebration reaches En-rogel. Joab hears the trumpet; Jonathan "
                        "son of Abiathar arrives with the news: 'King David has made Solomon king' "
                        "(1:43). The guests scatter in terror. Adonijah flees to the altar and "
                        "grasps its horns -- the traditional claim of sanctuary (Exod 21:13-14). "
                        "He refuses to come down until Solomon swears not to kill him. Solomon's "
                        "response is measured but conditional: 'If he will show himself a worthy "
                        "man, not one of his hairs shall fall to the earth, but if wickedness is "
                        "found in him, he shall die' (1:52). Adonijah bows before Solomon. The "
                        "conditional mercy foreshadows the political executions of chapter 2: "
                        "Solomon's kingdom will be established not by grace alone but by decisive "
                        "elimination of threats. The chapter establishes the pattern that runs "
                        "through 1 Kings: YHWH's purposes advance through human political maneuvering, "
                        "prophetic intervention, and royal decree working in concert."
            }
        ]
    },

    {
        "id": "1kgs-3",
        "ref": "1 Kings 3",
        "chapter_num": 3,
        "title": "Solomon's Wisdom -- The Gift of a Listening Heart",
        "era": "solomon_glory",
        "type": "chapter",
        "themes": ["KING", "SPIRIT", "LAW"],

        "synopsis": "Solomon goes to Gibeon, the 'great high place' where the tabernacle of "
                    "meeting still stands, and offers a thousand burnt offerings. That night YHWH "
                    "appears to Solomon in a dream: 'Ask what I shall give you' (3:5). Solomon's "
                    "request is remarkable -- not wealth, long life, or military victory, but "
                    "'a listening heart' (lev shomea) to judge YHWH's people and to discern between "
                    "good and evil (3:9). YHWH is pleased: because Solomon asked for wisdom rather "
                    "than self-serving gifts, God grants him both wisdom and the things he did not "
                    "ask for -- riches and honor beyond any king of his age. The famous judgment "
                    "of the two mothers and the disputed baby (3:16-28) demonstrates Solomon's "
                    "God-given discernment. All Israel hears the verdict and fears the king, 'for "
                    "they perceived that the wisdom of God (chokhmat elohim) was in him to do "
                    "justice' (3:28). Solomon's wisdom is not mere cleverness but divine council "
                    "wisdom -- the ability to see truth as God sees it.",

        "key_verse": {
            "ref": "1 Kings 3:9",
            "text": "Give your servant therefore an understanding mind to govern your people, that I may discern between good and evil, for who is able to govern this your great people?",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "lev shomea (a listening/understanding heart -- lit. a heart that hears; the organ of discernment)",
            "chokhmat elohim (wisdom of God -- divine wisdom dwelling in a human king)",
            "biyn (to discern/understand -- the ability to distinguish between good and evil)",
            "mishpat (justice/judgment -- the king's primary function: rendering verdicts)",
            "chalom (dream -- the medium of YHWH's revelation to Solomon at Gibeon)",
            "bamah (high place -- Gibeon as the 'great high place' where the tabernacle stood)"
        ],

        "ane_backdrop": "Dream theophanies at sacred sites are well attested in ANE literature. "
                        "Egyptian pharaohs received divine messages in dreams at temples -- the "
                        "Dream Stela of Thutmose IV at the Great Sphinx records the god Harmachis "
                        "promising Thutmose the kingship if he clears the sand from the Sphinx. "
                        "The Gudea Cylinders of Lagash (~2100 BC) describe King Gudea receiving "
                        "temple-building instructions from the god Ningirsu in a dream. Solomon's "
                        "dream at Gibeon follows this pattern precisely: the king incubates at a "
                        "sacred site, the deity appears, and royal-temple instructions follow. The "
                        "request for wisdom rather than military power is distinctive: Mesopotamian "
                        "kings typically asked for victory and long reign. Solomon's request echoes "
                        "the 'wisdom of the scribe' tradition in Egyptian Instruction Literature "
                        "(e.g., the Instruction of Amenemope), but transcends it: this is not human "
                        "sagacity but a divine endowment.",

        "second_temple": [
            {
                "source": "Wisdom of Solomon 7:7-14",
                "summary": "'I prayed, and understanding was given me; I called on God, and the "
                           "spirit of wisdom came to me. I preferred her to scepters and thrones.' "
                           "The author writes in Solomon's voice, expanding the 1 Kings 3 prayer.",
                "relevance": "The Wisdom of Solomon personalizes chokmah as a divine figure who "
                             "dwells with God and is given to those who seek her -- amplifying "
                             "the divine council wisdom theme."
            },
            {
                "source": "Josephus, Antiquities VIII.2.1",
                "summary": "Josephus recounts the Gibeon dream and emphasizes that Solomon's wisdom "
                           "surpassed 'the understanding of the ancients and even the Egyptians.'",
                "relevance": "Josephus positions Solomon as the apex of ANE wisdom, surpassing "
                             "even Egypt's famed sages -- a claim with geopolitical implications."
            }
        ],

        "cross_refs": [
            {"ref": "Proverbs 1:7", "note": "'The fear of the LORD is the beginning of knowledge' -- the Solomonic wisdom tradition grounded in 1 Kings 3", "type": "ot"},
            {"ref": "Proverbs 8:15-16", "note": "'By me kings reign, and rulers decree what is just' -- personified Wisdom as the source of royal judgment", "type": "ot"},
            {"ref": "James 1:5", "note": "'If any of you lacks wisdom, let him ask God, who gives generously' -- echoing Solomon's request", "type": "nt"},
            {"ref": "Matthew 12:42", "note": "'Something greater than Solomon is here' -- Jesus claims to surpass Solomonic wisdom", "type": "nt"},
            {"ref": "Deuteronomy 17:14-20", "note": "The Torah's law of the king: he must copy the law and read it daily -- the foundation Solomon received", "type": "ot"}
        ],

        "divine_council_note": "Solomon's wisdom is described as chokhmat elohim (3:28) -- 'the "
                               "wisdom of God.' This is not human intelligence amplified but divine "
                               "council wisdom implanted in a human mind. In the wisdom tradition "
                               "(Proverbs 8; Job 28), wisdom (chokmah) is a divine attribute that "
                               "was present at creation, accessible only to God and those to whom he "
                               "reveals it. Solomon's 'listening heart' (lev shomea) is the organ that "
                               "receives divine council deliberation -- the ability to hear what God "
                               "hears, to see cases as the divine judge sees them. The two-mothers "
                               "judgment is the proof: Solomon perceives the truth that no human "
                               "investigation could uncover, because he operates with the discernment "
                               "of the heavenly court. This is why 'all Israel feared the king' (3:28) "
                               "-- they recognized something more than human at work in his judgments.",

        "sections": [
            {
                "heading": "The Dream at Gibeon (3:1-15)",
                "body": "Solomon makes a marriage alliance with Pharaoh of Egypt -- the first ominous "
                        "note in an otherwise glorious beginning. The narrator comments that 'the people "
                        "were sacrificing at the high places, because no house had yet been built for "
                        "the name of the LORD' (3:2) -- the high places are tolerated provisionally "
                        "because the Temple does not yet exist. Solomon goes to Gibeon, 'the great high "
                        "place' (bamah gedolah), where the tabernacle of meeting stood (2 Chr 1:3). He "
                        "offers a thousand burnt offerings -- a staggering number that signals both wealth "
                        "and devotion. That night YHWH appears in a dream with the extraordinary offer: "
                        "'Ask what I shall give you' (3:5). Solomon's response is a model of covenant "
                        "theology: he acknowledges YHWH's chesed (loyal love) to David, confesses his own "
                        "inadequacy ('I am but a little child; I do not know how to go out or come in,' "
                        "3:7), and makes the request: 'Give your servant a lev shomea to govern your "
                        "people, that I may discern between good and evil' (3:9). The phrase lev shomea "
                        "is literally 'a hearing heart' -- the Hebrew lev (heart) is the seat of "
                        "intellect and will, not merely emotion. Solomon asks for a heart attuned to "
                        "divine wisdom. YHWH's response is lavish: because Solomon did not ask for "
                        "long life, riches, or the death of enemies, God grants all of these along "
                        "with 'a wise and discerning heart, so that none like you has been before "
                        "you and none like you shall arise after you' (3:12)."
            },
            {
                "heading": "The Judgment of the Two Mothers (3:16-28)",
                "body": "The practical demonstration of divine wisdom follows immediately. Two "
                        "prostitutes come before the king with a dispute: both gave birth; one child "
                        "died in the night; each claims the living child. There are no witnesses, "
                        "no evidence, and no way to resolve the case by conventional means. Solomon "
                        "commands: 'Bring me a sword... Divide the living child in two, and give "
                        "half to the one and half to the other' (3:24-25). The true mother's "
                        "compassion (rachamim, from rechem, 'womb') erupts: 'Oh, my lord, give "
                        "her the living child, and by no means put him to death' (3:26). The false "
                        "mother consents to the division: 'It shall be neither mine nor yours; "
                        "divide it' (3:26). Solomon identifies the true mother. The judgment reveals "
                        "the nature of chokhmat elohim: it is not jurisprudential technique but "
                        "penetrating discernment of human hearts. Solomon creates a scenario that "
                        "forces the truth to reveal itself. 'All Israel heard of the judgment that "
                        "the king had rendered, and they stood in awe of the king, because they "
                        "perceived that the wisdom of God was in him to do justice' (3:28). The "
                        "people recognize the divine origin of the wisdom: this is not Solomon's "
                        "cleverness but God's wisdom operating through the king."
            }
        ]
    },

    {
        "id": "1kgs-6-8",
        "ref": "1 Kings 6-8",
        "chapter_num": 6,
        "title": "The Temple -- Cosmic Mountain, Eden Restored, YHWH's Name Enthroned",
        "era": "solomon_glory",
        "type": "chapter",
        "themes": ["HOLY", "PRIEST", "DC", "TYPE", "COV", "NAME", "NATIONS"],

        "synopsis": "Solomon builds the Temple in seven years (6:38), a number that echoes the "
                    "seven days of creation. The interior is cedar, gold, and cherubim -- Eden "
                    "imagery saturating every surface. The Holy of Holies houses two massive "
                    "cherubim whose wings span the entire room, sheltering the ark of the covenant "
                    "beneath them (6:23-28). The Temple is brought to completion, the ark is placed "
                    "in the inner sanctuary, and 'the cloud filled the house of the LORD, so that "
                    "the priests could not stand to minister because of the cloud, for the glory of "
                    "the LORD (kevod YHWH) filled the house of the LORD' (8:10-11). Solomon then "
                    "delivers the dedication prayer -- the theological summit of the entire "
                    "Deuteronomistic History. He declares that YHWH has chosen to 'put his name' "
                    "(shemo) in this house (8:29), yet acknowledges: 'Behold, heaven and the "
                    "highest heaven cannot contain you; how much less this house that I have "
                    "built!' (8:27). The prayer covers seven petitions for seven situations, each "
                    "ending with the plea that YHWH hear from heaven and act. Fire falls from "
                    "heaven (2 Chr 7:1), consuming the sacrifice. The Temple is YHWH's earthly "
                    "throne room -- the intersection of heaven and earth, the new Eden, the cosmic "
                    "mountain where the divine council's decisions are executed.",

        "key_verse": {
            "ref": "1 Kings 8:27",
            "text": "But will God indeed dwell on the earth? Behold, heaven and the highest heaven cannot contain you; how much less this house that I have built!",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "bayit YHWH (house of YHWH -- the Temple; in Hebrew bayit means both 'house' and 'palace.' The Temple is simultaneously YHWH's dwelling, his throne room, and his royal palace. ANE temples were always understood as the deity's house -- the place where the god 'lived' and received visitors, offerings, and petitions)",
            "devir (inner sanctuary / Holy of Holies -- the innermost room of the Temple, a perfect 20-cubit cube, where the ark and the cherubim stood. Only the high priest could enter, once per year on the Day of Atonement. This was YHWH's throne room -- the earthly counterpart of the heavenly council chamber)",
            "keruvim (cherubim -- composite winged beings who guard the divine throne; NOT the chubby baby angels of Renaissance art. In ANE iconography, the cherubim are powerful hybrid creatures -- human-faced, winged, often with lion or bull bodies -- who serve as throne guardians. They guarded Eden's entrance (Gen 3:24), formed the mercy seat on the ark (Exod 25:18-22), and in Ezekiel's visions carry YHWH's mobile throne (Ezek 1, 10))",
            "kavod YHWH (glory of YHWH -- Hebrew kavod literally means 'weight, heaviness,' translated 'glory.' It refers to YHWH's visible, radiant, weighty presence -- the luminous cloud-fire manifestation that appeared at Sinai, filled the tabernacle (Exod 40:34), and now fills the Temple. NOTE: Later Jewish tradition developed the term Shekinah (from shakan, 'to dwell') to describe God's indwelling presence. Shekinah does not appear in the Bible itself but became standard rabbinic vocabulary for what 1 Kings 8 describes as the kavod filling the Temple. The kavod and the Shekinah refer to the same reality: God's manifest, localized presence among his people)",
            "anan (cloud -- the theophanic cloud that fills the Temple; the same cloud that appeared at Sinai (Exod 19:16-18) and filled the tabernacle (Exod 40:34-35). In ANE religion, clouds were associated with divine presence and mystery)",
            "shem (name -- YHWH's name 'dwelling' in the Temple; Deuteronomy's Name theology is carefully nuanced: YHWH himself transcends the cosmos, but his Name -- his accessible, revealed identity -- is localized in the Temple. This prevents both the error of thinking God is confined to a building and the error of thinking God is distant and unreachable)",
            "shamayim hashamayim (heaven of heavens / highest heaven -- YHWH's true dwelling; Solomon affirms that even the cosmos cannot contain YHWH, let alone a building)",
            "tephillah (prayer -- the seven-fold dedication prayer; seven petitions for seven situations, the number of creation-completeness)"
        ],

        "ane_backdrop": "Temple construction in the ANE followed established patterns. The Gudea "
                        "Cylinders of Lagash (~2100 BC) describe divine instructions for temple "
                        "building, the king's role as builder, and a dedication ceremony with "
                        "divine approval. Egyptian temples at Karnak and Luxor were conceived as "
                        "microcosms -- the inner sanctuary represented the primeval mound of creation. "
                        "The Mesopotamian temple-as-cosmic-mountain (ziggurat) tradition is directly "
                        "relevant: the temple was the point where heaven met earth. Solomon's Temple "
                        "shares these patterns: it is built on a mountain (Moriah/Zion), its interior "
                        "is a garden paradise (cedar, gold, flowers, palm trees, cherubim), and its "
                        "innermost room is the dwelling of the deity. The seven-year construction "
                        "period (6:38) echoes the seven days of creation, establishing the Temple as "
                        "a new creation act. Crucially, Solomon builds the Temple and his own palace "
                        "as an integrated palace-temple complex (the connected architectural ensemble "
                        "in which the king's palace and the god's temple share walls, courtyards, and "
                        "administrative space, expressing the idea that the king governs as the god's "
                        "earthly representative). This is standard ANE practice: at Ugarit, the "
                        "palace of the king adjoined the temple of Baal; in Egypt, the pharaoh's "
                        "mortuary temple was the interface between royal and divine authority. "
                        "Solomon's palace takes thirteen years to build (7:1) while the Temple takes "
                        "seven -- the narrator subtly notes the disproportion. The cherubim in the "
                        "Holy of Holies parallel the lamassu (winged guardian figures) at the "
                        "entrances of Assyrian palaces and the sphinx-throne traditions of Phoenician "
                        "and Syrian kings. The cloud theophany at dedication (8:10-11) parallels ANE "
                        "accounts of the deity 'entering' the temple at its inauguration.",

        "second_temple": [
            {
                "source": "2 Chronicles 7:1-3",
                "summary": "The Chronicler adds that 'fire came down from heaven and consumed the "
                           "burnt offering and the sacrifices, and the glory of the LORD filled the "
                           "temple' -- a detail not in 1 Kings 8 but consistent with the theophanic "
                           "tradition.",
                "relevance": "The heavenly fire confirms divine acceptance: YHWH has taken up "
                             "residence in his house. The fire from heaven is a divine council act -- "
                             "the heavenly court responding to the earthly dedication."
            },
            {
                "source": "Josephus, Antiquities VIII.4.1",
                "summary": "Josephus provides extensive detail on the Temple dimensions, materials, "
                           "and furnishings, comparing Solomon's achievement to the wonders of the "
                           "ancient world.",
                "relevance": "Josephus wrote after the Second Temple's destruction and used Solomon's "
                             "Temple to demonstrate the glory of Israelite civilization to his "
                             "Greco-Roman audience."
            },
            {
                "source": "Sirach 47:13",
                "summary": "'Solomon reigned in an age of peace, and God gave him rest on every "
                           "side, that he might build a house in his name and prepare a sanctuary "
                           "to stand forever.'",
                "relevance": "Ben Sira praises the Temple as Solomon's defining achievement and "
                             "connects rest (menuchah) to temple building -- the theology of "
                             "Deuteronomy 12 and Psalm 132."
            }
        ],

        "cross_refs": [
            {"ref": "2 Samuel 7:5-13", "note": "The Davidic covenant: 'He shall build a house for my name' -- Solomon fulfills this promise", "type": "ot"},
            {"ref": "Exodus 40:34-35", "note": "The glory-cloud fills the tabernacle at its inauguration -- the same event repeated at the Temple", "type": "ot"},
            {"ref": "Genesis 2:8-14", "note": "Eden as the first temple-garden: cherubim, gold, trees, rivers -- all echoed in Temple design", "type": "ot"},
            {"ref": "Isaiah 6:1-4", "note": "Isaiah sees YHWH enthroned in the Temple, the seraphim calling 'Holy, holy, holy' -- the Temple as divine council throne room", "type": "ot"},
            {"ref": "Psalm 132:13-14", "note": "'The LORD has chosen Zion; he has desired it for his dwelling place: This is my resting place forever'", "type": "ot"},
            {"ref": "John 2:19-21", "note": "'Destroy this temple, and in three days I will raise it up' -- Jesus as the true temple", "type": "nt"},
            {"ref": "Revelation 21:22", "note": "'I saw no temple in the city, for its temple is the Lord God the Almighty and the Lamb'", "type": "nt"},
            {"ref": "Ephesians 2:19-22", "note": "Believers as 'a holy temple in the Lord... a dwelling place for God by the Spirit'", "type": "nt"}
        ],

        "divine_council_note": "The Temple is the earthly counterpart of the heavenly throne room. "
                               "When the glory-cloud (kevod YHWH) fills the house (8:10-11), heaven "
                               "and earth overlap. The cherubim in the Holy of Holies are divine "
                               "council figures -- the throne guardians who attend YHWH's presence "
                               "(cf. Gen 3:24; Ezek 1, 10; Isa 6). The Temple's Eden imagery (carved "
                               "palm trees, open flowers, gold overlaying everything) signals that "
                               "this is Eden restored -- the place where God dwells with humanity, "
                               "where the boundary between heaven and earth becomes permeable. "
                               "Solomon's prayer employs 'Name theology' (shem): YHWH's Name dwells "
                               "in the Temple while YHWH himself transcends heaven and earth (8:27). "
                               "This is not a limitation but a distinction between YHWH's essential "
                               "being (in the heavenly council) and his accessible presence (in the "
                               "earthly Temple). The seven petitions of the dedication prayer (8:31-53) "
                               "address every conceivable human crisis and direct the remedy toward "
                               "the Temple: pray 'toward this place' and YHWH will hear 'in heaven, "
                               "your dwelling place.' The Temple is the portal -- the place where "
                               "human prayer ascends to the divine council and divine response "
                               "descends to the human realm.",

        "sections": [
            {
                "heading": "The Temple as New Creation (1 Kings 6)",
                "body": "Construction begins in Solomon's fourth year, 480 years after the exodus "
                        "(6:1) -- a number that is 12 generations of 40 years, linking the Temple "
                        "to the exodus as the fulfillment of the entire wilderness-conquest sequence. "
                        "The Temple dimensions are modest by ANE standards (60 cubits long, 20 wide, "
                        "30 high -- roughly 90 x 30 x 45 feet) but the interior is extraordinary. "
                        "The walls are lined with cedar from Lebanon, carved with gourds and open "
                        "flowers (6:18) -- garden imagery. The floor is cypress. The inner sanctuary "
                        "(devir) is a perfect cube of 20 cubits (6:20), overlaid with pure gold -- "
                        "a geometry of perfection echoed in the New Jerusalem (Rev 21:16). Two "
                        "cherubim of olivewood, each 10 cubits tall with 10-cubit wingspans, stand "
                        "in the Holy of Holies. Their wings stretch from wall to wall, touching in "
                        "the center (6:27). They are the throne guardians -- the same beings who "
                        "guarded Eden's entrance (Gen 3:24) now guard the space where YHWH's "
                        "presence dwells. The entire interior is carved with cherubim, palm trees, "
                        "and open flowers (6:29), then overlaid with gold. The Temple is a golden "
                        "garden with angelic guardians -- Eden rebuilt in cedar and gold. The seven-"
                        "year construction period (6:38) deliberately parallels the seven days of "
                        "creation: the Temple is a microcosm, a new creation act."
            },
            {
                "heading": "The Glory Fills the House (1 Kings 8:1-13)",
                "body": "Solomon assembles all Israel for the dedication. The ark of the covenant "
                        "is brought from the City of David and placed in the inner sanctuary beneath "
                        "the cherubim's wings (8:6). When the priests withdraw, 'the cloud filled "
                        "the house of the LORD, so that the priests could not stand to minister "
                        "because of the cloud, for the glory of the LORD (kevod YHWH) filled the "
                        "house of the LORD' (8:10-11). This is the same cloud that descended on "
                        "Sinai (Exod 19:16-18), filled the tabernacle (Exod 40:34-35), and led "
                        "Israel through the wilderness. YHWH has moved in. His glory -- the "
                        "weighty, luminous manifestation of his presence -- now fills this house as "
                        "it filled the tabernacle. Solomon responds: 'The LORD has said that he "
                        "would dwell in thick darkness (araphel)' (8:12). The araphel is the same "
                        "word used for the divine darkness at Sinai (Deut 4:11; 5:22) -- the "
                        "impenetrable darkness that surrounds YHWH's presence, making him both "
                        "present and inaccessible. The Temple is the localization of Sinai: the "
                        "mountain of God compressed into a building, where the cloud and the "
                        "darkness and the glory permanently reside."
            },
            {
                "heading": "Solomon's Dedication Prayer (1 Kings 8:22-53)",
                "body": "Solomon's prayer is the theological masterpiece of the Deuteronomistic "
                        "History. He begins by affirming YHWH's incomparability: 'There is no God "
                        "like you, in heaven above or on earth beneath, keeping covenant and "
                        "showing steadfast love (chesed) to your servants who walk before you with "
                        "all their heart' (8:23). Then the stunning question: 'But will God indeed "
                        "dwell on the earth? Behold, heaven and the highest heaven (shamayim "
                        "hashamayim) cannot contain you; how much less this house that I have built!' "
                        "(8:27). Solomon affirms two truths simultaneously: YHWH genuinely dwells "
                        "in the Temple (his Name is there), and YHWH transcends the Temple (the "
                        "cosmos cannot contain him). The prayer then presents seven petitions "
                        "covering oath disputes (8:31-32), military defeat (8:33-34), drought "
                        "(8:35-36), famine and plague (8:37-40), the foreigner who prays toward "
                        "the Temple (8:41-43), battle (8:44-45), and exile (8:46-53). Each petition "
                        "follows the pattern: the crisis occurs, the people pray toward the Temple, "
                        "and YHWH hears 'in heaven your dwelling place' and acts. The petition for "
                        "the foreigner is remarkable: 'that all the peoples of the earth may know "
                        "your name and fear you' (8:43) -- the Temple is not merely Israel's "
                        "sanctuary but a house of prayer for all nations (cf. Isa 56:7). The final "
                        "petition envisions exile and return -- prophetically anticipating the "
                        "Babylonian captivity and the prayer orientation toward Jerusalem that "
                        "defined Jewish worship thereafter (Dan 6:10)."
            }
        ]
    },

    {
        "id": "1kgs-10-11",
        "ref": "1 Kings 10-11",
        "chapter_num": 10,
        "title": "Queen of Sheba, Solomon's Splendor, and the Apostasy That Breaks a Kingdom",
        "era": "solomon_glory",
        "type": "chapter",
        "themes": ["NATIONS", "KING", "REBEL", "DC", "WOMEN", "RIV"],

        "synopsis": "The Queen of Sheba visits Solomon, drawn by his fame, and is overwhelmed: "
                    "'The half was not told me. Your wisdom and prosperity surpass the report that "
                    "I heard' (10:7). She blesses YHWH and recognizes that Solomon's throne exists "
                    "'because the LORD loved Israel forever' (10:9). Solomon's wealth reaches "
                    "legendary proportions: 666 talents of gold annually (10:14), a great ivory "
                    "throne overlaid with gold (10:18-20), all his drinking vessels of gold (10:21), "
                    "and 'silver was not considered as anything in the days of Solomon' (10:21). "
                    "But chapter 11 reverses everything. Solomon 'loved many foreign women' (11:1) "
                    "-- from the nations YHWH had explicitly prohibited (Moab, Ammon, Edom, Sidon, "
                    "the Hittites). He had 700 wives and 300 concubines, 'and his wives turned "
                    "away his heart after other gods' (11:4). He built high places for Ashtoreth "
                    "of the Sidonians, Chemosh of Moab, and Milcom of Ammon -- the territorial "
                    "deities of the surrounding nations. YHWH is angry and pronounces judgment: "
                    "the kingdom will be torn from Solomon's son, with only one tribe preserved "
                    "for David's sake and for the sake of Jerusalem.",

        "key_verse": {
            "ref": "1 Kings 11:4",
            "text": "For when Solomon was old his wives turned away his heart after other gods, and his heart was not wholly true to the LORD his God, as was the heart of David his father.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "ashtoreth (Ashtoreth/Astarte -- the Sidonian goddess of fertility and war; the West Semitic form of Mesopotamian Ishtar. In the divine council framework, she is one of the elohim allotted to govern Sidon under the Deuteronomy 32:8-9 dispensation)",
            "kemosh (Chemosh -- the national deity of Moab; attested on the Mesha Stele where King Mesha credits Chemosh with military victories. Chemosh received human sacrifice, including Israelite captives dedicated as herem, 'devoted destruction')",
            "milkom (Milcom/Molech -- the Ammonite deity; associated with child sacrifice through fire. The name may derive from melek, 'king,' with the vowels of boshet, 'shame,' substituted by scribes to express revulsion)",
            "shiqquts (detestable thing / abomination -- the strongest Deuteronomic term for foreign gods; literally something that makes one shudder with disgust)",
            "bamah (high place -- an elevated outdoor worship site, usually on a hilltop, with an altar, a sacred tree or pole, and a standing stone. Solomon builds these for foreign gods on the hills east of Jerusalem -- the Mount of Olives, directly across from the Temple)",
            "satan (adversary -- YHWH raises adversaries (satans) against Solomon: Hadad, Rezon, Jeroboam. The Hebrew word satan means 'adversary, accuser' -- here it refers to human political opponents raised by divine decree, the same term later used for the heavenly accuser in Job 1-2)",
            "natah (to turn aside -- Solomon's heart 'turned' after other gods; the same verb of apostasy that Deuteronomy warns against)",
            "davaq (to cling/cleave -- Solomon 'clung' to his foreign wives; this is the same verb used for a man clinging to his wife in Gen 2:24 and for Israel clinging to YHWH in Deut 10:20. Solomon's covenantal devotion is misdirected)"
        ],

        "ane_backdrop": "Royal marriage alliances were standard ANE diplomacy: pharaohs, Hittite "
                        "kings, and Mesopotamian rulers cemented treaties through marriage. The "
                        "foreign wife typically brought her gods, her priests, and her cult practices "
                        "into the royal court. Ramesses II married a Hittite princess and accommodated "
                        "Hittite religious practice at Pi-Ramesses. Solomon's 700 wives and 300 "
                        "concubines represent an extensive network of international alliances -- each "
                        "wife a treaty partner, each treaty requiring at minimum tolerance of the "
                        "partner's deity. Chemosh of Moab is well attested in the Mesha Stele (~840 "
                        "BC), where King Mesha describes Chemosh commanding him in warfare and "
                        "receiving Israelite captives as herem (devoted to destruction). Ashtoreth "
                        "is the West Semitic form of Ishtar, the Mesopotamian goddess of love and "
                        "war. Milcom/Molech of Ammon was associated with child sacrifice (tophet "
                        "rituals), attested archaeologically at Carthage and likely practiced in "
                        "the Hinnom Valley outside Jerusalem.",

        "second_temple": [
            {
                "source": "Nehemiah 13:26",
                "summary": "'Did not Solomon king of Israel sin on account of such women? Among "
                           "the many nations there was no king like him... nevertheless foreign "
                           "women made even him to sin.'",
                "relevance": "Nehemiah invokes Solomon as the paradigmatic warning against foreign "
                             "wives and their gods -- even the wisest king fell."
            },
            {
                "source": "Testament of Solomon (1st-3rd c. AD)",
                "summary": "A pseudepigraphal text in which Solomon uses a divine ring to command "
                           "demons, but ultimately falls through the seduction of a Jebusite woman "
                           "who demands he sacrifice to her gods.",
                "relevance": "The Testament expands the apostasy narrative with demonological detail: "
                             "Solomon's fall is not merely religious unfaithfulness but submission to "
                             "demonic territorial powers."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 17:16-17", "note": "The law of the king: 'He shall not acquire many wives for himself, lest his heart turn away' -- Solomon violates every clause", "type": "ot"},
            {"ref": "Deuteronomy 7:1-4", "note": "'You shall not intermarry with them... for they would turn away your sons from following me, to serve other gods'", "type": "ot"},
            {"ref": "Deuteronomy 32:8-9", "note": "The nations allotted to the sons of God; Israel is YHWH's portion -- Solomon worships the gods of other nations' allotments", "type": "ot"},
            {"ref": "Matthew 6:29", "note": "'Even Solomon in all his glory was not arrayed like one of these' -- Jesus relativizes Solomon's splendor", "type": "nt"},
            {"ref": "Matthew 12:42", "note": "The Queen of the South will rise at the judgment -- she sought Solomon's wisdom; greater wisdom is present in Jesus", "type": "nt"},
            {"ref": "Revelation 18:12-13", "note": "Babylon's luxury goods echo Solomon's imports -- wealth as idolatrous seduction", "type": "nt"}
        ],

        "divine_council_note": "Solomon's apostasy is a divine council crisis. He builds high places "
                               "for Ashtoreth, Chemosh, and Milcom -- the territorial deities of Sidon, "
                               "Moab, and Ammon respectively. In the Deuteronomy 32:8-9 framework, "
                               "these are the elohim (sons of God) allotted to govern those nations. "
                               "Solomon, the king of YHWH's own nachalah (inheritance), is now "
                               "worshipping the divine beings assigned to other nations' territories. "
                               "This is not merely syncretism -- it is a direct inversion of the "
                               "divine council order. The king who built YHWH's earthly throne room "
                               "now builds rival throne rooms for subordinate elohim on the hills "
                               "surrounding Jerusalem. YHWH's response is to raise 'adversaries' "
                               "(satan, 11:14, 23, 25) -- the same term used for the heavenly "
                               "adversary in Job 1-2 and Zechariah 3. The earthly adversaries "
                               "(Hadad the Edomite, Rezon of Damascus, Jeroboam of Ephraim) are "
                               "instruments of divine council judgment. The number 666 for Solomon's "
                               "annual gold (10:14) is noted but not explained in the text; later "
                               "tradition (Rev 13:18) associates it with beastly counterfeit of "
                               "divine order.",

        "sections": [
            {
                "heading": "The Queen of Sheba: A Foreigner Praises YHWH (10:1-13)",
                "body": "The Queen of Sheba (likely modern Yemen or Ethiopia) comes with 'a very "
                        "great retinue, with camels bearing spices and very much gold and precious "
                        "stones' (10:2) to test Solomon with 'hard questions' (chidot -- riddles, "
                        "enigmas). Solomon answers all her questions; 'there was nothing hidden from "
                        "the king that he could not explain to her' (10:3). She is overwhelmed by his "
                        "wisdom, his palace, the food of his table, the seating of his officials, the "
                        "attendance of his servants, their clothing, his cupbearers, and 'his burnt "
                        "offerings that he offered at the house of the LORD' (10:5). Her confession "
                        "is remarkable: 'Blessed be the LORD your God, who has delighted in you and "
                        "set you on the throne of Israel! Because the LORD loved Israel forever, he "
                        "has made you king, that you may execute justice and righteousness' (10:9). "
                        "A pagan queen recognizes that Solomon's throne exists because of YHWH's "
                        "love -- the Temple-prayer petition for the foreigner (8:41-43) is being "
                        "fulfilled. She gives Solomon 120 talents of gold, spices in abundance, and "
                        "precious stones. The exchange symbolizes the nations bringing tribute to "
                        "YHWH's king on YHWH's mountain -- a foretaste of the eschatological "
                        "pilgrimage (Isa 60:1-7; Ps 72:10-11)."
            },
            {
                "heading": "Solomon's Apostasy (11:1-8)",
                "body": "The reversal is devastating in its simplicity: 'King Solomon loved many "
                        "foreign women, along with the daughter of Pharaoh: Moabite, Ammonite, "
                        "Edomite, Sidonian, and Hittite women, from the nations concerning which "
                        "the LORD had said to the people of Israel, You shall not enter into "
                        "marriage with them, neither shall they with you, for surely they will "
                        "turn away your heart after their gods' (11:1-2). The narrator adds: "
                        "'Solomon clung to these in love' (11:2) -- using the verb davaq, the same "
                        "word used for a man 'clinging' to his wife in Genesis 2:24 and for Israel "
                        "'clinging' to YHWH in Deuteronomy 10:20. Solomon's covenantal devotion, "
                        "which should have been directed to YHWH, is redirected to foreign women "
                        "and their gods. The result: 'When Solomon was old his wives turned away "
                        "his heart after other gods, and his heart was not wholly true (shalem) to "
                        "the LORD' (11:4). The adjective shalem (whole, complete, perfect) is a "
                        "wordplay on Solomon's own name (shelomoh, from shalom). The man of peace "
                        "is no longer at peace with God. He builds a high place for Chemosh, the "
                        "'abomination of Moab' (shiqquts Mo'av), and for Milcom, the 'abomination "
                        "of the Ammonites,' on the hills east of Jerusalem (11:7). The Mount of "
                        "Olives -- the hills across the Kidron from the Temple -- becomes the site "
                        "of rival worship. The very mountain where Ezekiel will see the glory of "
                        "YHWH depart (Ezek 11:23) now hosts the shrines of territorial deities."
            },
            {
                "heading": "YHWH's Judgment: The Kingdom Torn (11:9-43)",
                "body": "YHWH is angry: 'Since this has been your practice and you have not kept "
                        "my covenant and my statutes that I have commanded you, I will surely tear "
                        "the kingdom from you and will give it to your servant' (11:11). The verb "
                        "'tear' (qara) is physical -- a ripping apart, a violent sundering. But "
                        "there is mercy within the judgment: 'I will not do it in your days, for "
                        "the sake of David your father; I will tear it out of the hand of your son. "
                        "However, I will not tear away all the kingdom, but I will give one tribe "
                        "to your son, for the sake of David my servant and for the sake of Jerusalem "
                        "that I have chosen' (11:12-13). The Davidic covenant (2 Sam 7) prevents "
                        "total destruction; the lamp of David will not be extinguished. YHWH raises "
                        "three adversaries (satan): Hadad the Edomite, Rezon son of Eliada in "
                        "Damascus, and Jeroboam son of Nebat from Ephraim. Ahijah the prophet meets "
                        "Jeroboam, tears his new garment into twelve pieces, and gives ten to "
                        "Jeroboam: 'Take for yourself ten pieces, for thus says the LORD, the God "
                        "of Israel, Behold, I am about to tear the kingdom from the hand of Solomon "
                        "and will give you ten tribes' (11:31). The prophetic sign-act (tearing a "
                        "garment) physically enacts the divine decree. Solomon dies after a forty-year "
                        "reign, and the stage is set for catastrophe."
            }
        ]
    }
]
