"""
era_44_judges_samson.py -- Samson: Spirit-Empowered Nazirite (Judges 13-16)

The Samson cycle is the most complex judge narrative -- a man empowered by the
Spirit of YHWH from the womb yet driven by personal appetites, a Nazirite
consecrated to God who repeatedly violates his vow, a deliverer who never
rallies Israel for battle but wages a one-man guerrilla war against the
Philistines. The cycle opens with the most detailed Angel of YHWH theophany
in Judges (chapter 13), where the Angel declares his name is 'Wonderful'
(peli) -- the same word used for the messianic child in Isaiah 9:6. Samson's
story is framed by two divine council themes: the Angel of YHWH who
commissions his birth and the territorial deity Dagon whose temple he
destroys in his death. Between these bookends, the Spirit of YHWH rushes
upon Samson repeatedly, enabling feats of supernatural strength -- but
Samson treats the divine gift as a personal weapon rather than a covenantal
trust. The theological lesson is that Spirit-empowerment and moral
faithfulness are tragically separable.
"""

CHAPTERS = [
    {
        "id": "judg-13",
        "ref": "Judges 13",
        "chapter_num": 13,
        "title": "The Angel of YHWH and the Birth of Samson",
        "era": "judges_samson",
        "type": "chapter",
        "themes": ["DC", "SPIRIT", "HOLY", "WOMEN"],

        "synopsis": "Israel does evil again, and YHWH gives them into the hand of the Philistines "
                    "for forty years -- the longest oppression in the book. The Angel of YHWH appears "
                    "to the wife of Manoah (unnamed in the text) of the tribe of Dan and announces "
                    "that she, though barren, will conceive a son. The child is to be a Nazirite from "
                    "the womb: 'no razor shall come upon his head' (13:5), and he 'shall begin to "
                    "save Israel from the hand of the Philistines' (13:5) -- the word 'begin' (yachel) "
                    "is significant: Samson will start the deliverance but not complete it. Manoah's "
                    "wife reports the encounter to her husband, describing the visitor as 'a man of "
                    "God' whose appearance was 'like the appearance of the Angel of God, very awesome' "
                    "(13:6). Manoah prays for the visitor to return, and the Angel appears again to "
                    "the woman. Manoah asks the Angel's name; the response is: 'Why do you ask my "
                    "name, seeing it is wonderful (peli)?' (13:18). Manoah offers a sacrifice, and "
                    "'when the flame went up toward heaven from the altar, the Angel of YHWH went up "
                    "in the flame of the altar' (13:20). Manoah is terrified: 'We shall surely die, "
                    "for we have seen God (elohim)!' (13:22). His wife's response is a model of "
                    "theological reasoning: 'If YHWH had meant to kill us, he would not have accepted "
                    "a burnt offering and a grain offering at our hands' (13:23). The boy is born and "
                    "named Samson (Shimshon, from shemesh, 'sun'). 'The Spirit of YHWH began to stir "
                    "him in Mahaneh-dan' (13:25).",

        "key_verse": {
            "ref": "Judges 13:18",
            "text": "And the angel of the LORD said to him, 'Why do you ask my name, seeing it is wonderful?'",
            "translation": "ESV"
        },

        "original_terms": [
            "peli (wonderful/incomprehensible -- the Angel's self-designation, connecting to the messianic title in Isaiah 9:6)",
            "nazir (Nazirite -- from nazar, 'to separate'; one consecrated to God by a special vow involving three prohibitions: no wine or grape products, no contact with dead bodies, and no cutting of hair (Numbers 6:1-21). Samson's case is unique: he is a Nazirite from the womb by divine decree, not personal choice, making his repeated violations all the more tragic)",
            "Shimshon (Samson -- from shemesh, 'sun'; a name with solar associations in a region bordering Philistine Dagon/sun worship)",
            "aqarah (barren -- Manoah's wife, placing Samson's birth in the barren-woman motif: Sarah, Rebekah, Rachel, Hannah, Elizabeth)",
            "mal'akh YHWH (Angel of YHWH -- the visible YHWH who announces Samson's birth and ascends in altar fire)",
            "elohim (God -- what Manoah calls the Angel in 13:22, identifying the figure as divine)",
            "yachel lehoshia (shall begin to save -- the partial nature of Samson's deliverance mandate)"
        ],

        "ane_backdrop": "The Nazirite vow (Numbers 6:1-21) is a uniquely Israelite institution with no "
                        "direct ANE parallel. It represents voluntary consecration to YHWH through "
                        "abstinence -- a form of living sacrifice. The uncut hair was the visible sign "
                        "of the vow, marking the Nazirite as YHWH's property. Samson's case is unique: "
                        "he is a Nazirite from the womb, not by personal choice -- his consecration is "
                        "a divine decree, not a human decision. The Philistines (Pelishtim) were part "
                        "of the Sea Peoples who settled on the southern Levantine coast after ~1175 BC. "
                        "Archaeological evidence from Ekron, Ashkelon, Ashdod, Gath, and Gaza reveals "
                        "Aegean-origin material culture: Mycenaean-style pottery, architectural forms, "
                        "and dietary practices (including pig consumption, notably absent from Israelite "
                        "sites). Their primary deity Dagon was a grain/fertility god whose temples at "
                        "Gaza and Ashdod are attested both textually and archaeologically. The forty-year "
                        "Philistine oppression corresponds to the archaeological picture of Philistine "
                        "expansion in the early 11th century BC.",

        "second_temple": [
            {
                "source": "Targum Jonathan on Judges 13:18",
                "summary": "The Targum renders peli ('wonderful') as 'hidden' or 'secret,' emphasizing "
                           "the inscrutability of the divine name rather than the christological "
                           "connection.",
                "relevance": "The Targumic translation reveals a theological strategy: by rendering peli "
                             "as 'hidden' rather than 'wonderful,' the Targum distances the passage from "
                             "christological readings while preserving the mystery of the Angel's identity."
            },
            {
                "source": "Origen, Homilies on Judges 7.2",
                "summary": "Origen identifies the Angel whose name is 'Wonderful' as the pre-incarnate "
                           "Christ, connecting Judges 13:18 directly to Isaiah 9:6 ('His name shall be "
                           "called Wonderful').",
                "relevance": "The patristic tradition saw the peli/pele connection as decisive: the "
                             "Angel of YHWH who announces Samson's birth is the same 'Wonderful "
                             "Counselor' of the messianic prophecy."
            },
            {
                "source": "Pseudo-Philo, Biblical Antiquities 42",
                "summary": "Pseudo-Philo recounts Samson's birth narrative with additional emphasis on "
                           "the divine promise and the barren-woman motif, connecting it to the Sarah "
                           "and Hannah traditions.",
                "relevance": "The Second Temple tradition recognized Samson's birth as part of the "
                             "pattern of miraculous births through barren women -- each birth advancing "
                             "God's redemptive plan."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 9:6", "note": "'His name shall be called Wonderful (pele), Counselor, Mighty God' -- the same root as the Angel's self-designation in 13:18", "type": "ot"},
            {"ref": "Numbers 6:1-21", "note": "The Nazirite vow legislation -- the framework for Samson's lifelong consecration", "type": "ot"},
            {"ref": "Genesis 18:14", "note": "'Is anything too wonderful (yippale) for YHWH?' -- the same root pele applied to YHWH's power over barrenness", "type": "ot"},
            {"ref": "Luke 1:11-20", "note": "The angel Gabriel announces John the Baptist to Zechariah -- the same pattern: angelic announcement, barren woman, Nazirite child", "type": "nt"},
            {"ref": "Judges 6:21-22", "note": "The Angel of YHWH consumes Gideon's offering with fire and disappears -- the same theophanic pattern as 13:19-20", "type": "ot"},
            {"ref": "Exodus 33:20", "note": "'No one shall see me and live' -- the basis of Manoah's terror in 13:22", "type": "ot"},
            {"ref": "Genesis 32:29", "note": "Jacob asks the Angel's name and is refused -- the same pattern of divine name-mystery as 13:18", "type": "ot"},
            {"ref": "Hebrews 11:32", "note": "Samson listed among the faith heroes despite his moral failures", "type": "nt"},
            {"ref": "1 Samuel 1:11", "note": "Hannah's vow dedicating Samuel as a Nazirite from the womb -- the closest parallel to Samson's prenatal consecration, but with opposite outcomes", "type": "ot"},
            {"ref": "Amos 2:11-12", "note": "'I raised up some of your sons for prophets, and some of your young men for Nazirites... but you made the Nazirites drink wine' -- Israel corrupts the very institution Samson embodies", "type": "ot"},
            {"ref": "Psalm 139:13-16", "note": "'You formed my inward parts; you knitted me together in my mother's womb' -- the divine sovereignty over prenatal life that governs Samson's Nazirite commission", "type": "ot"},
            {"ref": "Jeremiah 1:5", "note": "'Before I formed you in the womb I knew you' -- the same prenatal calling tradition as Samson, applied to the prophet Jeremiah", "type": "ot"}
        ],

        "divine_council_note": "Judges 13 contains the most theologically rich Angel of YHWH appearance "
                               "in the book. Three features are decisive for divine council theology: "
                               "(1) The Angel's name is peli ('wonderful') -- 13:18. This is not a personal "
                               "name but a category designation: the Angel's identity is beyond human "
                               "comprehension. The word peli shares the root pele with the messianic title "
                               "in Isaiah 9:6 (pele yo'ets, 'Wonderful Counselor'). The early church "
                               "fathers (Origen, Eusebius, Theodoret) consistently identified this Angel "
                               "as the pre-incarnate Christ on the basis of this connection. In the divine "
                               "council framework, the Angel is the second power in heaven -- the visible "
                               "YHWH whose name participates in the divine nature and therefore cannot be "
                               "fully disclosed to mortals. (2) The Angel ascends in the altar flame -- "
                               "13:20. When Manoah offers the burnt offering, the Angel 'went up in the "
                               "flame of the altar.' He does not merely vanish; he ascends through the "
                               "fire -- the same element that manifests YHWH's presence at Sinai, in the "
                               "burning bush, and in the pillar of fire. The Angel's departure through "
                               "sacrificial fire identifies him with the divine presence that receives "
                               "the sacrifice. (3) Manoah identifies the Angel as elohim -- 13:22. 'We "
                               "shall surely die, for we have seen God (elohim).' Manoah's wife corrects "
                               "his panic but not his identification: the figure they saw IS God. The text "
                               "does not say Manoah was wrong to call the Angel elohim -- only that seeing "
                               "God does not necessarily mean death when God has chosen to appear graciously.",

        "sections": [
            {
                "heading": "The Angel Appears to Manoah's Wife (13:1-7)",
                "body": "The Philistine oppression begins: 'YHWH gave them into the hand of the "
                        "Philistines for forty years' (13:1) -- the longest oppression in Judges, "
                        "and notably, there is no record of Israel crying out. The silence may indicate "
                        "that Israel had accommodated to Philistine rule -- a spiritual numbness worse "
                        "than active rebellion. YHWH acts anyway, initiating deliverance without being "
                        "asked. The Angel of YHWH appears to the wife of Manoah, a Danite from Zorah. "
                        "She is barren (aqarah) -- placing her in the theological lineage of barren "
                        "mothers whose supernatural conception advances the divine plan: Sarah (Gen "
                        "18:10-14), Rebekah (Gen 25:21), Rachel (Gen 30:22-24), and later Hannah (1 "
                        "Sam 1:19-20) and Elizabeth (Luke 1:7, 13). The Angel announces: 'You shall "
                        "conceive and bear a son. No razor shall come upon his head, for the child "
                        "shall be a Nazirite to God from the womb, and he shall begin to save Israel "
                        "from the hand of the Philistines' (13:5). The word 'begin' (yachel) is "
                        "theologically precise: Samson's work is initiatory, not final. The complete "
                        "deliverance from the Philistines will require Samuel, Saul, and David. The "
                        "woman reports to Manoah: 'A man of God came to me, and his appearance was like "
                        "the appearance of the Angel of God, very awesome. I did not ask him where he "
                        "was from, and he did not tell me his name' (13:6)."
            },
            {
                "heading": "The Angel Returns: Name, Sacrifice, and Ascension (13:8-23)",
                "body": "Manoah prays for the visitor to return: 'O Lord, please let the man of God "
                        "whom you sent come again to us and teach us what we are to do with the child "
                        "who will be born' (13:8). God hears, and the Angel appears again -- to the "
                        "woman, not to Manoah, who must be summoned. Manoah asks: 'What is to be the "
                        "child's manner of life, and what is his mission?' (13:12). The Angel repeats "
                        "the Nazirite instructions. Manoah offers hospitality: 'Please let us detain "
                        "you and prepare a young goat for you' (13:15). The Angel declines food but "
                        "invites a burnt offering: 'If you prepare a burnt offering, then offer it to "
                        "YHWH' (13:16) -- subtly redirecting worship from himself to YHWH, while "
                        "simultaneously identifying himself with YHWH's presence. Manoah asks the "
                        "Angel's name 'so that, when your words come true, we may honor you' (13:17). "
                        "The answer is luminous: 'Why do you ask my name, seeing it is wonderful "
                        "(peli)?' (13:18). The word peli is from the root pala -- to be extraordinary, "
                        "beyond comprehension. The Angel's identity is not hidden out of capriciousness "
                        "but because it transcends human categories. Manoah offers the sacrifice, 'and "
                        "the Angel did a wonderful thing (maphli la'asot) as Manoah and his wife looked "
                        "on. When the flame went up toward heaven from the altar, the Angel of YHWH "
                        "went up in the flame of the altar' (13:19-20). The Angel ascends through the "
                        "sacrificial fire -- identifying himself with the divine presence that receives "
                        "burnt offerings. Manoah and his wife fall on their faces. Manoah says: 'We "
                        "shall surely die, for we have seen God (elohim)' (13:22). His wife's response "
                        "is a masterpiece of pastoral theology: if YHWH intended to kill them, he would "
                        "not have accepted their sacrifice or shown them such things (13:23)."
            },
            {
                "heading": "Samson's Birth and the Spirit's Stirring (13:24-25)",
                "body": "The woman bears a son and names him Shimshon (Samson). The name derives from "
                        "shemesh ('sun') and may include a diminutive suffix: 'little sun' or 'sun-man.' "
                        "The solar association is notable because the Danite territory bordered the "
                        "Philistine region where solar cult practices were attested. The name may also "
                        "function as a polemic: the 'sun-man' of Israel will defeat the worshipers of "
                        "foreign astral deities. 'The child grew, and YHWH blessed him. And the Spirit "
                        "of YHWH began to stir him (lepha'amo) in Mahaneh-dan, between Zorah and "
                        "Eshtaol' (13:24-25). The verb pa'am means 'to impel, to agitate, to stir' -- "
                        "it suggests a restless, powerful impulse. The Spirit does not fully possess "
                        "Samson yet but begins to move him -- the same word used for Jacob's spirit "
                        "being 'stirred' by the news about Joseph (Gen 45:26 LXX). Mahaneh-dan means "
                        "'Camp of Dan,' the last encampment of the Danites before their migration north "
                        "(chapter 18). Samson is the last great Danite; the tribe is already losing "
                        "its territory to the Philistines and the Amorites. The Spirit's stirring marks "
                        "the beginning of YHWH's initiative to push back against Philistine encroachment."
            }
        ]
    },

    {
        "id": "judg-14",
        "ref": "Judges 14",
        "chapter_num": 14,
        "title": "The Timnah Marriage and the Riddle -- Spirit and Appetite",
        "era": "judges_samson",
        "type": "chapter",
        "themes": ["SPIRIT", "NATIONS"],

        "synopsis": "Samson goes to Timnah and desires a Philistine woman: 'Get her for me, for she "
                    "is right in my eyes' (14:3) -- language that foreshadows the book's refrain about "
                    "everyone doing what is 'right in his own eyes.' His parents protest the violation "
                    "of the intermarriage prohibition (Deut 7:3), but the narrator adds a critical "
                    "theological note: 'His father and mother did not know that it was from YHWH, for "
                    "he was seeking an opportunity against the Philistines' (14:4). YHWH uses Samson's "
                    "flawed desires to accomplish his purposes. On the way to Timnah, the Spirit of "
                    "YHWH 'rushes upon' Samson (14:6), and he tears a young lion apart with his bare "
                    "hands. Later he finds a swarm of bees and honey in the lion's carcass -- "
                    "touching a dead body, the first Nazirite violation. At his wedding feast "
                    "(mishteh, a drinking party -- possibly the second violation), Samson poses a "
                    "riddle: 'Out of the eater came something to eat. Out of the strong came "
                    "something sweet' (14:14). When the Philistines cannot solve it, they pressure "
                    "his bride to extract the answer. She weeps for seven days; he relents. The "
                    "Philistines answer the riddle, and Samson, furious, declares: 'If you had not "
                    "plowed with my heifer, you would not have found out my riddle' (14:18). The "
                    "Spirit rushes on him again (14:19), and he kills thirty Philistines at Ashkelon "
                    "to pay the wager. His wife is given to his best man.",

        "key_verse": {
            "ref": "Judges 14:4",
            "text": "His father and mother did not know that it was from the LORD, for he was seeking an opportunity against the Philistines. At that time the Philistines ruled over Israel.",
            "translation": "ESV"
        },

        "original_terms": [
            "vatitslach alav ruakh YHWH (the Spirit of YHWH rushed upon him -- the violent, sudden empowerment for supernatural strength)",
            "chidah (riddle -- a wisdom-contest form; Samson's riddle is based on a private experience no one can know)",
            "mishteh (feast/drinking party -- from shatah, 'to drink'; likely involving wine, potentially violating the Nazirite vow)",
            "to'anah (occasion/opportunity -- what YHWH seeks against the Philistines through Samson's desires)",
            "kephir arayot (young lion -- the animal Samson tears apart, an image of Spirit-empowered strength)",
            "yashar be'einav (right in his eyes -- the phrase connecting Samson's desire to the book's theological verdict)"
        ],

        "ane_backdrop": "The Timnah marriage follows ANE marriage patterns where the groom goes to the "
                        "bride's family -- a 'visiting marriage' (called sadiqa in Mesopotamian texts) "
                        "where the wife remains in her father's household and the husband visits. This "
                        "explains why Samson's wife remains among the Philistines after the wedding "
                        "feast. Riddle contests at wedding feasts are attested in various cultures and "
                        "served as entertainment and social competition. The lion-and-honey episode "
                        "connects to two ANE motifs: the hero who kills a lion bare-handed (attested "
                        "for Gilgamesh and depicted in Assyrian royal art) and the phenomenon of bee "
                        "swarms colonizing animal carcasses (biologically plausible once the flesh has "
                        "desiccated). Timnah (Tel Batash) has been excavated and shows Philistine "
                        "occupation in the Iron Age I period, with evidence of both Philistine and "
                        "Israelite material culture -- a border town where the two populations interacted.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities V.8.5-8",
                "summary": "Josephus recounts the Timnah narrative, emphasizing Samson's supernatural "
                           "strength and his parents' reluctance, while noting that God's providence "
                           "worked through Samson's desire.",
                "relevance": "Josephus preserves the divine providence reading (14:4) while presenting "
                             "the events as historical narrative."
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 7:3", "note": "'You shall not intermarry with them' -- the prohibition Samson violates by desiring a Philistine wife", "type": "ot"},
            {"ref": "Judges 17:6; 21:25", "note": "'Everyone did what was right in his own eyes' -- Samson's 'right in my eyes' (14:3) anticipates the refrain", "type": "ot"},
            {"ref": "Genesis 50:20", "note": "'You meant it for evil, but God meant it for good' -- the same providence theology as 14:4", "type": "ot"},
            {"ref": "Romans 8:28", "note": "'All things work together for good' -- the NT expression of God's sovereign use of flawed human choices", "type": "nt"},
            {"ref": "1 Peter 5:8", "note": "'Your adversary the devil prowls around like a roaring lion' -- the lion as a symbol of the spiritual enemy Samson defeats physically", "type": "nt"},
            {"ref": "Numbers 6:6-7", "note": "The Nazirite prohibition against corpse contact -- violated when Samson touches the lion carcass", "type": "ot"},
            {"ref": "Numbers 6:3-4", "note": "The Nazirite prohibition against wine and grape products -- potentially violated at the mishteh (drinking feast) in 14:10", "type": "ot"},
            {"ref": "Proverbs 5:3-6", "note": "'The lips of a forbidden woman drip honey... her feet go down to death' -- the wisdom tradition's warning against the exact pattern Samson follows", "type": "ot"},
            {"ref": "James 1:13-15", "note": "'Each person is tempted when he is lured and enticed by his own desire... sin when it is fully grown brings forth death' -- the NT analysis of Samson's trajectory", "type": "nt"}
        ],

        "divine_council_note": "Judges 14:4 is a key text for understanding divine sovereignty and human "
                               "agency: 'It was from YHWH, for he was seeking an opportunity (to'anah) "
                               "against the Philistines.' YHWH does not cause Samson's lust, but he "
                               "incorporates Samson's flawed desires into his cosmic plan. The divine "
                               "council has decreed the beginning of Philistine deliverance, and YHWH's "
                               "sovereignty is comprehensive enough to work through a compromised human "
                               "agent. The Spirit of YHWH 'rushing upon' (tsalach al) Samson is the "
                               "most violent expression of divine council empowerment in the book -- the "
                               "verb tsalach implies an overwhelming, sudden surge of divine power that "
                               "takes over the human agent. Unlike Othniel (where the Spirit 'came upon' "
                               "him, hayetah alav -- a more measured bestowal), Samson is seized by the "
                               "Spirit for specific acts of superhuman strength. This empowerment is "
                               "task-specific and does not sanctify: the Spirit gives power, not holiness.",

        "sections": [
            {
                "heading": "The Timnah Desire and the Lion (14:1-9)",
                "body": "Samson sees a Philistine woman at Timnah and demands that his parents arrange "
                        "the marriage: 'Get her for me, for she is right in my eyes' (14:3). The phrase "
                        "yashar be'einav ('right in his eyes') deliberately echoes the book's verdict "
                        "formula (17:6; 21:25). Samson is the judges period in miniature: empowered by "
                        "God's Spirit yet following personal appetite. His parents object on religious "
                        "grounds: 'Is there not a woman among the daughters of your relatives, or among "
                        "all our people, that you must go to take a wife from the uncircumcised "
                        "Philistines?' (14:3). The narrator intervenes: 'His father and mother did not "
                        "know that it was from YHWH' (14:4). On the journey to Timnah, a young lion "
                        "attacks Samson, 'and the Spirit of YHWH rushed upon him, and he tore the lion "
                        "in pieces as one tears a young goat, and he had nothing in his hand' (14:6). "
                        "The weaponless killing emphasizes that the strength is not Samson's but the "
                        "Spirit's. He tells no one. Later, returning to Timnah, he finds bees and honey "
                        "in the lion carcass. He scoops out the honey and eats it -- touching a dead "
                        "body, violating the Nazirite vow (Num 6:6). He gives honey to his parents "
                        "'but he did not tell them that he had scraped the honey from the carcass of "
                        "the lion' (14:9). Secrecy covers the violation."
            },
            {
                "heading": "The Riddle Contest and the Spirit's Vengeance (14:10-20)",
                "body": "Samson's father goes to the woman, 'and Samson prepared a feast (mishteh) "
                        "there, for so the young men used to do' (14:10). The mishteh is a drinking "
                        "party -- if Samson participates in the wine drinking, this is a second Nazirite "
                        "violation (Num 6:3-4). He poses the riddle to thirty Philistine companions: "
                        "'Out of the eater came something to eat. Out of the strong came something "
                        "sweet' (14:14). The riddle is unsolvable because it is based on a private "
                        "experience. After three days of failure, the Philistines threaten Samson's "
                        "bride: 'Entice your husband... or we will burn you and your father's house "
                        "with fire' (14:15). She weeps on Samson for the remaining four days of the "
                        "feast: 'You only hate me; you do not love me. You have put a riddle to my "
                        "people, and you have not told me what it is' (14:16). Samson relents. The "
                        "Philistines give the answer before sunset on the seventh day: 'What is sweeter "
                        "than honey? What is stronger than a lion?' Samson knows immediately: 'If you "
                        "had not plowed with my heifer, you would not have found out my riddle' (14:18). "
                        "The Spirit of YHWH rushes upon him again, and he goes to Ashkelon, strikes "
                        "down thirty men, takes their garments to pay the wager, and returns in burning "
                        "anger. His wife is given to his companion. The marriage-sabotage creates the "
                        "'occasion' YHWH was seeking against the Philistines."
            }
        ]
    },

    {
        "id": "judg-15",
        "ref": "Judges 15",
        "chapter_num": 15,
        "title": "Foxes, Jawbones, and Living Water -- Escalation",
        "era": "judges_samson",
        "type": "chapter",
        "themes": ["SPIRIT", "REVERSAL"],

        "synopsis": "Samson returns to Timnah to visit his wife, only to discover that her father has "
                    "given her to another man. In retaliation, Samson catches 300 foxes (or jackals), "
                    "ties them tail-to-tail with torches between them, and releases them into the "
                    "Philistine grain fields, vineyards, and olive orchards -- an act of agricultural "
                    "devastation. The Philistines respond by burning Samson's wife and father-in-law "
                    "alive. Samson retaliates with a 'great blow' (15:8). The Philistines advance "
                    "into Judah demanding Samson's surrender. Three thousand men of Judah bind Samson "
                    "with new ropes and deliver him to the Philistines -- his own people hand him "
                    "over. 'The Spirit of YHWH rushed upon him, and the ropes that were on his arms "
                    "became as flax that has caught fire, and his bonds melted off his hands' (15:14). "
                    "He seizes the fresh jawbone of a donkey and kills a thousand Philistines. Samson "
                    "composes a victory poem: 'With the jawbone of a donkey, heaps upon heaps, with "
                    "the jawbone of a donkey have I struck down a thousand men' (15:16). Exhausted "
                    "and dying of thirst, he cries to YHWH -- his first recorded prayer -- and God "
                    "splits open a hollow place in Lehi, and water flows out. 'He judged Israel in "
                    "the days of the Philistines twenty years' (15:20).",

        "key_verse": {
            "ref": "Judges 15:14",
            "text": "When he came to Lehi, the Philistines came shouting to meet him. Then the Spirit of the LORD rushed upon him, and the ropes that were on his arms became as flax that has caught fire, and his bonds melted off his hands.",
            "translation": "ESV"
        },

        "original_terms": [
            "lechi chamor (jawbone of a donkey -- the improvised weapon of the Spirit-empowered warrior)",
            "shu'alim (foxes/jackals -- the 300 animals used as incendiary weapons against the grain harvest)",
            "lappidim (torches -- tied between the foxes' tails, an unconventional weapon of agricultural destruction)",
            "Ramat Lechi (Jawbone Hill -- the site named for Samson's victory, with an etiological water-spring)",
            "En haQore (Spring of the Caller -- the spring God opened for Samson, named for his prayer)",
            "vatitslach alav ruakh YHWH (the Spirit of YHWH rushed upon him -- the now-familiar violent empowerment)"
        ],

        "ane_backdrop": "The burning-fox stratagem has been compared to Roman agricultural sabotage "
                        "tactics: Ovid (Fasti IV.681-712) describes a Roman festival involving foxes "
                        "with burning torches tied to their tails, connected to the destruction of grain "
                        "fields. Whether this represents a shared Mediterranean tradition or independent "
                        "development is debated. The Philistine retaliation by burning (15:6) reflects "
                        "the severity of agricultural crimes in ANE law: destruction of a community's "
                        "food supply was tantamount to genocide. Judah's willingness to hand Samson over "
                        "to the Philistines (15:11-13) reveals the depth of accommodation: the tribe "
                        "of Judah would rather surrender a Spirit-empowered deliverer than risk "
                        "Philistine reprisal. The jawbone weapon echoes the broader Judges theme of "
                        "improvised weapons (Shamgar's oxgoad, Jael's tent peg, the Thebez woman's "
                        "millstone) -- YHWH's warriors use whatever is at hand because the power comes "
                        "from the Spirit, not the weapon.",

        "second_temple": [
            {
                "source": "Josephus, Antiquities V.8.8-9",
                "summary": "Josephus describes Samson's feats in detail, including the jawbone battle, "
                           "and emphasizes the miraculous water-spring as evidence of divine favor.",
                "relevance": "Josephus treats the water miracle as confirming that despite Samson's "
                             "personal flaws, YHWH's power operated through him."
            }
        ],

        "cross_refs": [
            {"ref": "Exodus 17:1-7", "note": "Water from the rock at Horeb -- God providing water for his thirsting servant in the wilderness", "type": "ot"},
            {"ref": "Judges 3:31", "note": "Shamgar killing 600 with an oxgoad -- the same theme of improvised weapons empowered by YHWH", "type": "ot"},
            {"ref": "1 Corinthians 1:27", "note": "'God chose what is foolish in the world to shame the wise' -- a donkey jawbone defeating a thousand warriors", "type": "nt"},
            {"ref": "Psalm 3:7", "note": "'Strike all my enemies on the jaw' -- the jawbone as an instrument of divine justice", "type": "ot"},
            {"ref": "2 Timothy 4:17", "note": "'The Lord stood by me and strengthened me... I was rescued from the lion's mouth' -- the Samson pattern of Spirit-rescue", "type": "nt"},
            {"ref": "Isaiah 50:6-7", "note": "'I gave my back to those who strike... I have set my face like a flint' -- the Suffering Servant bound and delivered by his own people, as Judah binds Samson", "type": "ot"},
            {"ref": "Psalm 18:32-40", "note": "'He trains my hands for war... you made my enemies turn their backs to me' -- the divine warrior language behind Samson's superhuman feats", "type": "ot"},
            {"ref": "Numbers 20:2-13", "note": "Water from the rock at Meribah -- the wilderness water miracle paralleled at Lehi when God splits the rock for Samson", "type": "ot"}
        ],

        "divine_council_note": "Samson's first prayer (15:18) is theologically significant: 'You have "
                               "granted this great salvation by the hand of your servant, and shall I "
                               "now die of thirst and fall into the hands of the uncircumcised?' For the "
                               "first time, Samson acknowledges YHWH as the source of deliverance and "
                               "himself as YHWH's 'servant' (eved). The water miracle that follows -- God "
                               "splitting open the rock at Lehi -- echoes the wilderness water miracles "
                               "(Exod 17:1-7; Num 20:2-13), connecting Samson's experience to Israel's "
                               "covenant history. YHWH provides for his flawed servant as he provided "
                               "for his flawed people. The binding and betrayal by Judah (15:11-13) is a "
                               "haunting preview: Israel's own people deliver their deliverer to the "
                               "enemy -- a pattern that will reach its ultimate expression in the betrayal "
                               "of the Messiah by his own people. The Spirit's empowerment to break bonds "
                               "(15:14) demonstrates that no human restraint can contain what the divine "
                               "council has empowered. Samson's story functions as a parable of Israel "
                               "itself: chosen from the womb, empowered by YHWH's Spirit, given superhuman "
                               "gifts for a divine purpose, yet repeatedly squandering those gifts on "
                               "personal appetites. Israel was chosen, gifted, empowered -- and like Samson, "
                               "Israel is unfaithful, enslaved by the nations it was supposed to overcome, "
                               "yet ultimately victorious through self-sacrifice (a pattern that reaches its "
                               "fullest expression in the Messiah).",

        "sections": [
            {
                "heading": "The Foxes and the Escalation (15:1-8)",
                "body": "Samson returns to Timnah to visit his wife but learns she has been given to "
                        "his companion. Her father offers the younger sister instead. Samson declares: "
                        "'This time I shall be innocent in regard to the Philistines, when I do them "
                        "harm' (15:3). He catches 300 foxes (shu'alim -- possibly jackals, which are "
                        "more common and easier to capture in the region), ties them tail-to-tail with "
                        "torches between each pair, and releases them into the standing grain, the "
                        "stacked sheaves, the vineyards, and the olive orchards. The devastation is "
                        "comprehensive -- the entire agricultural cycle is destroyed. The Philistines' "
                        "retaliation is savage: they burn Samson's wife and father-in-law alive (15:6) "
                        "-- the very fate the Philistines had threatened if she did not extract the "
                        "riddle (14:15). Samson responds with a 'great blow' (makkah gedolah) and then "
                        "withdraws to the cleft of the rock at Etam."
            },
            {
                "heading": "Judah's Betrayal, the Spirit's Power, and the Prayer for Water (15:9-20)",
                "body": "The Philistines raid Judah demanding Samson's surrender. Three thousand men of "
                        "Judah -- Samson's own countrymen -- descend to arrest him: 'Do you not know "
                        "that the Philistines are rulers over us? What then is this that you have done "
                        "to us?' (15:11). Israel has accepted Philistine sovereignty as normal. Samson "
                        "allows himself to be bound, asking only that Judah not attack him themselves. "
                        "They bind him with two new ropes and bring him to the Philistines, who come "
                        "shouting in triumph. Then 'the Spirit of YHWH rushed upon him' (15:14). The "
                        "ropes disintegrate like burning flax. He seizes a fresh jawbone -- moist, "
                        "therefore heavier and more durable than a dry one -- and kills a thousand men. "
                        "His victory poem uses a wordplay: chamor ('donkey') and chomer ('heap') create "
                        "an alliterative pun. After the battle, he is desperately thirsty. His prayer "
                        "is raw: 'You have granted this great salvation (teshuah) by the hand of your "
                        "servant (eved), and shall I now die of thirst?' (15:18). God splits open the "
                        "maktesh ('mortar,' a hollow basin) in Lehi, and water flows. Samson drinks, "
                        "'his spirit returned (vatashav rucho), and he revived' (15:19). The spring is "
                        "named En haQore ('Spring of the One Who Called') -- YHWH responds to the "
                        "prayer of his flawed servant."
            }
        ]
    },

    {
        "id": "judg-16",
        "ref": "Judges 16",
        "chapter_num": 16,
        "title": "Delilah and Dagon's Temple -- The Spirit Departs, the Temple Falls",
        "era": "judges_samson",
        "type": "chapter",
        "themes": ["SPIRIT", "DC", "REVERSAL"],

        "synopsis": "Samson visits a prostitute in Gaza, then falls in love with Delilah in the "
                    "Valley of Sorek. The Philistine lords (seranim) offer Delilah 1,100 pieces of "
                    "silver each to discover the source of his strength. Three times Samson gives "
                    "false answers; three times she tests them while Philistines wait in ambush. The "
                    "fourth time, she presses him 'day after day... until his soul was vexed to death' "
                    "(16:16). He tells her everything: 'A razor has never come upon my head, for I "
                    "have been a Nazirite to God from my mother's womb. If my head is shaved, then "
                    "my strength will leave me' (16:17). Delilah lulls him to sleep on her lap, calls "
                    "a man to shave his seven locks, and 'his strength left him' (16:19). The most "
                    "devastating verse in the Samson cycle follows: 'He awoke from his sleep and said, "
                    "I will go out as at other times and shake myself free. But he did not know that "
                    "YHWH had departed from him' (16:20). The Philistines seize him, gouge out his "
                    "eyes, bind him with bronze shackles, and put him to grinding grain in the Gaza "
                    "prison. But 'the hair of his head began to grow again' (16:22). At a great feast "
                    "to Dagon, the Philistines bring out the blinded Samson for entertainment. He is "
                    "positioned between the two central pillars of the temple. His final prayer: 'O "
                    "Lord YHWH, please remember me and please strengthen me only this once, O God, "
                    "that I may be avenged on the Philistines for my two eyes' (16:28). He pushes "
                    "the pillars; the temple collapses. 'So the dead whom he killed at his death were "
                    "more than those whom he had killed during his life' (16:30). The temple of Dagon "
                    "falls to YHWH's power, manifested through a blind, broken, repentant Nazirite.",

        "key_verse": {
            "ref": "Judges 16:20",
            "text": "And she said, 'The Philistines are upon you, Samson!' And he awoke from his sleep and said, 'I will go out as at other times and shake myself free.' But he did not know that the LORD had departed from him.",
            "translation": "ESV"
        },

        "original_terms": [
            "Delilah (possibly from dalal, 'to weaken/impoverish' or laylah, 'night' -- the woman who drains Samson's power)",
            "seranim (lords/rulers -- the Philistine pentapolis (five-city) governors who ruled Gaza, Ashkelon, Ashdod, Ekron, and Gath; from a non-Semitic word possibly related to Greek tyrannos, reflecting the Philistines' Aegean/Sea Peoples origin)",
            "machleqot rosho (the locks of his head -- the seven Nazirite locks whose cutting represents the breaking of the vow)",
            "Dagon (the Philistine grain/fertility deity -- from dagan, 'grain'; an ancient Semitic deity worshiped from at least the 3rd millennium BC in Mesopotamia and at Ugarit as the father of Baal; adopted by the Philistines upon settling in Canaan; his temple becomes the arena for YHWH's final victory through Samson)",
            "YHWH sar me'alav (YHWH had departed from him -- the most terrifying statement in the Samson narrative)",
            "naqam (vengeance/avenging -- Samson's final prayer is for personal vengeance, not national deliverance)"
        ],

        "ane_backdrop": "Philistine temples with two central load-bearing pillars have been archaeologically "
                        "confirmed. Excavations at Tell Qasile (a Philistine settlement near modern Tel "
                        "Aviv) uncovered a temple from the Iron Age I period with two central wooden "
                        "pillars set on stone bases, close enough together for a single person to reach "
                        "both simultaneously. A similar architecture has been found at Ekron. The collapse "
                        "of such a building by dislodging its central supports is architecturally plausible. "
                        "Dagon was an ancient grain deity (from dagan, 'grain') worshiped throughout the "
                        "Levant and Mesopotamia from at least the 3rd millennium BC. He appears in the "
                        "Mari texts and at Ugarit as the father of Baal. The Philistines adopted Dagon "
                        "as their primary deity upon settling in Canaan. The seranim ('lords') who "
                        "gathered for the Dagon festival represented the five cities of the Philistine "
                        "pentapolis: Gaza, Ashkelon, Ashdod, Ekron, and Gath. The 1,100 pieces of silver "
                        "each (5,500 total from five lords) represents an extraordinary sum -- indicating "
                        "the Philistine elite's desperation to neutralize Samson.",

        "second_temple": [
            {
                "source": "Hebrews 11:32-34",
                "summary": "Samson is listed among those who 'through faith... out of weakness were "
                           "made strong' -- a reference to his final act of faith in the Dagon temple.",
                "relevance": "The NT commends Samson's faith at the end, not his moral failings. His "
                             "final prayer is the act that Hebrews celebrates: out of weakness (blind, "
                             "bound, broken) he was made strong by faith."
            },
            {
                "source": "Josephus, Antiquities V.8.12",
                "summary": "Josephus recounts the Dagon temple destruction, estimating 3,000 casualties "
                           "and noting that Samson's family retrieved his body for burial.",
                "relevance": "Josephus treats the temple collapse as a historically significant event that "
                             "dealt a major blow to Philistine religious confidence."
            },
            {
                "source": "Augustine, City of God 18.15",
                "summary": "Augustine identifies Samson as a type of Christ: betrayed by those close to "
                           "him, bound and humiliated, yet achieving his greatest victory in death.",
                "relevance": "The typological reading of Samson's death as prefiguring Christ's death -- "
                             "destroying the enemy's stronghold through self-sacrificial death -- was "
                             "standard in patristic exegesis."
            },
            {
                "source": "Pseudo-Philo, Biblical Antiquities 43:4-8",
                "summary": "Pseudo-Philo records a divine speech to Samson in prison, declaring that "
                           "despite his failures, God will grant him one final act of strength 'so that "
                           "the Philistines may know that the power belongs to me.'",
                "relevance": "The Second Temple tradition understood Samson's final act as divinely "
                             "purposed: YHWH restored power not because Samson deserved it but because "
                             "Dagon's claim to victory ('Our god has given Samson our enemy into our "
                             "hand') could not be allowed to stand unchallenged."
            },
            {
                "source": "4 Maccabees 16:20-21",
                "summary": "The author invokes the examples of biblical heroes who endured suffering for "
                           "God, including an implicit reference to Samson's willingness to die rather "
                           "than let the enemy's god triumph.",
                "relevance": "The Maccabean martyr tradition drew on the Samson precedent: death in the "
                             "service of YHWH's honor against pagan powers was the supreme act of faith."
            }
        ],

        "cross_refs": [
            {"ref": "1 Samuel 5:1-7", "note": "Dagon's statue falls before the ark of YHWH at Ashdod -- YHWH's continued victory over the Philistine deity", "type": "ot"},
            {"ref": "Judges 13:25; 14:6, 19; 15:14", "note": "The progressive Spirit-empowerment episodes -- contrasted with the Spirit's departure in 16:20", "type": "ot"},
            {"ref": "1 Samuel 16:14", "note": "'The Spirit of YHWH departed from Saul' -- the same divine withdrawal that befalls Samson", "type": "ot"},
            {"ref": "Colossians 2:15", "note": "Christ 'disarmed the rulers and authorities and put them to open shame' -- the Dagon temple as a foreshadowing", "type": "nt"},
            {"ref": "Numbers 6:5", "note": "'No razor shall come upon his head... he shall let the locks of hair of his head grow long' -- the Nazirite vow Samson finally forfeits", "type": "ot"},
            {"ref": "Philippians 4:13", "note": "'I can do all things through him who strengthens me' -- the positive expression of the Samson truth: strength comes from God's presence, not human ability", "type": "nt"},
            {"ref": "Psalm 9:15-16", "note": "'The nations have sunk in the pit that they made; in the net that they hid, their own foot has been caught' -- the Dagon temple trap that catches the trappers", "type": "ot"},
            {"ref": "Isaiah 53:3-5", "note": "'He was despised and rejected... wounded for our transgressions' -- Samson as a type of the Suffering Servant: humiliated, blinded, mocked, yet achieving his greatest victory in death", "type": "ot"},
            {"ref": "John 12:24", "note": "'Unless a grain of wheat falls into the earth and dies, it remains alone; but if it dies, it bears much fruit' -- the seed-death principle embodied in Samson's self-sacrificial final act", "type": "nt"},
            {"ref": "Hebrews 2:14-15", "note": "'Through death he might destroy the one who has the power of death' -- Christ accomplishing through death what Samson foreshadows: destroying the enemy's power by dying", "type": "nt"},
            {"ref": "Genesis 16:13", "note": "'You are a God of seeing' -- the irony of Samson's blindness: he who once saw the Philistine woman and declared her 'right in my eyes' now physically blind, finally sees spiritually in his last prayer", "type": "ot"},
            {"ref": "Lamentations 3:22-23", "note": "'The steadfast love of YHWH never ceases; his mercies never come to an end' -- YHWH restores power to the broken Samson one final time, grace after catastrophic failure", "type": "ot"}
        ],

        "divine_council_note": "Judges 16:20 -- 'he did not know that YHWH had departed from him' -- is "
                               "the most theologically devastating sentence in the judges period. The "
                               "Spirit of YHWH, the divine council's empowerment that had rushed upon "
                               "Samson repeatedly, has withdrawn. The departure is not arbitrary but "
                               "covenantal: the final Nazirite violation (the shaving of his hair) breaks "
                               "the visible sign of his consecration to YHWH. The hair was never the "
                               "source of Samson's power -- YHWH was. The hair was the covenant sign, "
                               "and its removal signified the broken covenant. The temple of Dagon becomes "
                               "the arena for the cosmic conflict between YHWH and the territorial deity "
                               "of the Philistines. Dagon's temple is his power center -- the physical "
                               "location where his worship concentrates and his spiritual authority is "
                               "exercised. When Samson destroys it, YHWH is striking at the infrastructure "
                               "of the rival deity's power. The Philistine lords gathered to 'offer a "
                               "great sacrifice to Dagon their god' and to celebrate: 'Our god has given "
                               "Samson our enemy into our hand' (16:23-24). They attribute the victory to "
                               "Dagon -- a direct challenge to YHWH's sovereignty. YHWH's response, "
                               "through the blinded Samson, is to collapse Dagon's house on Dagon's "
                               "worshipers. The final act is a divine council declaration: Dagon cannot "
                               "protect his own temple, his own priests, or his own lords from YHWH's "
                               "power. Samson's death in Dagon's temple is simultaneously his greatest "
                               "failure (self-destruction) and his greatest victory (destroying the "
                               "territorial deity's stronghold).",

        "sections": [
            {
                "heading": "Gaza, Delilah, and the Secret Revealed (16:1-20)",
                "body": "Samson visits a prostitute in Gaza (16:1) -- another episode of appetite-driven "
                        "behavior. The Gazites surround the house, planning to kill him at dawn, but "
                        "Samson rises at midnight, tears out the city gate (doors, posts, and bar), and "
                        "carries them to a hill facing Hebron -- a distance of approximately 38 miles, "
                        "an act of superhuman strength and public humiliation of the Philistines. Then "
                        "he falls in love with Delilah in the Valley of Sorek. The five Philistine "
                        "lords each offer her 1,100 pieces of silver to discover 'where his great "
                        "strength lies and how we may overpower him' (16:5). Three times Delilah asks; "
                        "three times Samson gives false answers: fresh bowstrings, new ropes, weaving "
                        "his hair into the loom. Each time she tests the method; each time he escapes. "
                        "The fourth time, she presses relentlessly: 'How can you say, I love you, when "
                        "your heart is not with me?' (16:15). She nags 'day after day... until his "
                        "soul was vexed to death' (16:16). He reveals everything: 'I have been a "
                        "Nazirite to God from my mother's womb. If my head is shaved, then my strength "
                        "will leave me' (16:17). Delilah recognizes the truth ('he had told her all "
                        "his heart,' 16:18), summons the lords, and lulls Samson to sleep on her lap. "
                        "A man shaves his seven locks. She torments him; he awakens: 'I will go out as "
                        "at other times and shake myself free. But he did not know that YHWH had "
                        "departed from him' (16:20). The ignorance is the tragedy: Samson does not even "
                        "perceive the absence of God."
            },
            {
                "heading": "Blindness, Dagon's Feast, and the Final Victory (16:21-31)",
                "body": "The Philistines seize Samson, gouge out his eyes, bind him with bronze "
                        "shackles, and force him to grind grain in the Gaza prison -- the mighty "
                        "warrior reduced to the work of a donkey or a slave-woman. 'But the hair of "
                        "his head began to grow again after it had been shaved' (16:22). This verse "
                        "is a seed of hope: the Nazirite sign is being restored. At a great festival "
                        "to Dagon, the lords and 3,000 spectators celebrate: 'Our god has given "
                        "Samson our enemy into our hand' (16:24). They attribute their victory to "
                        "Dagon -- a direct theological challenge to YHWH. When their hearts are merry, "
                        "they bring Samson out for sport. He is placed between the two central pillars "
                        "of the temple. Samson prays -- his longest and most theologically significant "
                        "prayer: 'O Lord YHWH, please remember me (zachreni na) and please strengthen "
                        "me (chazzqeni na) only this once, O God (elohim), that I may be avenged on "
                        "the Philistines for my two eyes' (16:28). The prayer addresses God by three "
                        "names -- Adonai YHWH, YHWH, and Elohim -- and uses the covenant language of "
                        "remembrance (zachar). He grasps the two middle pillars, 'one with his right "
                        "hand and one with his left, and leaned his weight against them' (16:29). 'Let "
                        "me die with the Philistines' (16:30). He pushes; the temple collapses. 'So "
                        "the dead whom he killed at his death were more than those whom he had killed "
                        "during his life' (16:30). His brothers retrieve his body and bury him between "
                        "Zorah and Eshtaol, in the tomb of his father Manoah (16:31)."
            }
        ]
    }
]
