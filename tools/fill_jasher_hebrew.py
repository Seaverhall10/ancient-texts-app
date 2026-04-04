"""
fill_jasher_hebrew.py — Fill empty hebrew_terms in all Jasher era files.
One-time utility script. Safe to delete after use.
"""
import re
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All hebrew_terms replacements keyed by chapter ID
TERMS = {
    # === PRIMEVAL ===
    "jasher-intro": [
        {"term": "yashar", "transliteration": "yashar", "meaning": "Upright, straight, just -- the root of the book's title Sefer HaYashar ('Book of the Upright'); connotes moral rectitude and straightforward truth (Deut 6:18)"},
        {"term": "sefer", "transliteration": "sefer", "meaning": "Book, scroll, written document -- from the root s-f-r (to count, recount, write); indicates an authoritative written record, the same word used for Torah scrolls"},
        {"term": "midrash", "transliteration": "midrash", "meaning": "Inquiry, investigation, exposition -- from darash (to seek, inquire); the genre of rabbinic biblical interpretation that Jasher draws upon and compiles into narrative form"},
        {"term": "aggadah", "transliteration": "aggadah", "meaning": "Narrative, legend, homiletical teaching -- the non-legal storytelling tradition in rabbinic literature; Jasher is essentially an aggadic retelling of Genesis through Joshua"},
    ],
    "jasher-1-2": [
        {"term": "nachash", "transliteration": "nachash", "meaning": "Serpent, shining one -- the being who deceives Eve in Eden; from a root meaning to hiss or to shine, suggesting a luminous divine being rather than a mere animal (cf. Ezek 28:13-15)"},
        {"term": "kotnot or", "transliteration": "kotnot or", "meaning": "Garments of skin (Gen 3:21) -- in Jasher these become a major artifact passed from Adam to Noah to Nimrod, conferring dominion over the animal kingdom"},
        {"term": "hevel", "transliteration": "hevel", "meaning": "Abel; literally 'breath, vapor, vanity' -- a name foreshadowing his brief life; his righteous offering establishes the pattern of faithful worship"},
        {"term": "qayin", "transliteration": "qayin", "meaning": "Cain; possibly from qanah (to acquire/possess) -- Eve says 'I have acquired a man with the LORD' (Gen 4:1); his line represents escalating rebellion"},
    ],
    "jasher-3-4": [
        {"term": "chanokh", "transliteration": "chanokh", "meaning": "Enoch; from chanak (to dedicate, train up) -- the righteous sage-king who 'walked with God' (Gen 5:22) and was translated to heaven without dying"},
        {"term": "halakh", "transliteration": "halakh", "meaning": "To walk -- 'Enoch walked with God' (Gen 5:22); the Hebrew implies continuous, habitual communion, not a single event; same root as halakhah (the way one walks/lives)"},
        {"term": "laqach", "transliteration": "laqach", "meaning": "To take, receive -- 'God took him' (Gen 5:24); used for Enoch's translation to heaven; same verb used for Elijah's departure (2 Kings 2:3)"},
        {"term": "melekh", "transliteration": "melekh", "meaning": "King -- Jasher uniquely portrays Enoch as a king who rules over all the sons of men, a pre-flood sage-king paralleling Mesopotamian traditions of Enmeduranki"},
    ],
    "jasher-5-6": [
        {"term": "noach", "transliteration": "noach", "meaning": "Noah; from nacham (to comfort/rest) -- 'this one will comfort us' (Gen 5:29); the righteous remnant who finds grace (chen) in the eyes of the LORD"},
        {"term": "mabbul", "transliteration": "mabbul", "meaning": "Flood, deluge -- a word used exclusively for Noah's flood in the Hebrew Bible; implies a cosmic, heavenly catastrophe (from the waters above the firmament)"},
        {"term": "tevah", "transliteration": "tevah", "meaning": "Ark, chest -- used only for Noah's ark and Moses' basket (Exod 2:3); NOT the same word as the Ark of the Covenant (aron); implies a vessel of divine rescue"},
        {"term": "chen", "transliteration": "chen", "meaning": "Grace, favor -- 'Noah found grace in the eyes of the LORD' (Gen 6:8); the first occurrence of grace in the Bible, given to the one righteous man amid total corruption"},
        {"term": "tsaddiq", "transliteration": "tsaddiq", "meaning": "Righteous one -- Noah described as 'a righteous man, blameless in his generation' (Gen 6:9); the standard of covenant faithfulness"},
    ],
    "jasher-7": [
        {"term": "nimrod", "transliteration": "nimrod", "meaning": "Nimrod; possibly from marad (to rebel) -- 'a mighty hunter before the LORD' (Gen 10:8-9); Jasher presents him as the archetypal tyrant who usurps divine authority"},
        {"term": "gibbor", "transliteration": "gibbor", "meaning": "Mighty one, warrior, hero -- applied to Nimrod (Gen 10:8); the same word describes the Nephilim (Gen 6:4); implies superhuman power or dominance"},
        {"term": "tsayid", "transliteration": "tsayid", "meaning": "Hunter, hunting -- Nimrod was 'a mighty hunter before the LORD'; Jasher explains this through the garments of Adam that gave him power over animals"},
        {"term": "mamshelet", "transliteration": "mamshelet", "meaning": "Dominion, rule, authority -- the garments of Adam conferred dominion over the animal kingdom; Nimrod's possession of them is the source of his tyrannical power in Jasher"},
    ],
    "jasher-9-10": [
        {"term": "migdal", "transliteration": "migdal", "meaning": "Tower -- the Tower of Babel (migdal Bavel); from gadal (to be great); the builders' attempt to 'make a name' and reach heaven represents rebellion against divine order"},
        {"term": "balal", "transliteration": "balal", "meaning": "To confuse, confound, mix -- the root behind 'Babel' (Gen 11:9); God confused (balal) their language; a wordplay on Babylon (Bab-ili, 'gate of god')"},
        {"term": "saphah", "transliteration": "saphah", "meaning": "Language, lip, speech -- 'the whole earth had one language (saphah) and the same words' (Gen 11:1); the division of languages is the mechanism of the Babel judgment"},
        {"term": "puts", "transliteration": "puts", "meaning": "To scatter, disperse -- 'the LORD scattered them abroad over the face of all the earth' (Gen 11:8); the scattering at Babel is reversed at Pentecost (Acts 2)"},
    ],
    "jasher-11-13": [
        {"term": "avodah zarah", "transliteration": "avodah zarah", "meaning": "Strange worship, idolatry -- the worship of false gods that dominates the post-Babel world in Jasher; the backdrop against which Abram's monotheism emerges"},
        {"term": "teraphim", "transliteration": "teraphim", "meaning": "Household idols, divine images -- the idols Terah makes and sells; associated with divination and false worship throughout the Hebrew Bible (Gen 31:19, Judg 17:5)"},
        {"term": "Avram", "transliteration": "Avram", "meaning": "Exalted father -- Abram's birth name before the covenant renaming to Abraham (av hamon, 'father of a multitude', Gen 17:5); born into an idolatrous household"},
        {"term": "Terach", "transliteration": "Terach", "meaning": "Terah; Abram's father, an idol-maker in Ur of the Chaldeans; Jasher expands his role as both craftsman of idols and reluctant father who reports his son to Nimrod"},
    ],

    # === ABRAHAM ===
    "jasher-14-15": [
        {"term": "pesel", "transliteration": "pesel", "meaning": "Idol, graven image -- from pasal (to hew, carve); Abram smashes his father's idols in one of the most celebrated traditions in Jewish literature, a scene absent from Genesis"},
        {"term": "elil", "transliteration": "elil", "meaning": "Worthless thing, idol -- a contemptuous term for false gods, possibly a diminutive of el (god); the prophets use it to mock idols as 'nothings' (Isa 2:8, Hab 2:18)"},
        {"term": "emunah", "transliteration": "emunah", "meaning": "Faithfulness, steadfastness, belief -- Abram's refusal to worship idols demonstrates emunah in the one true God; the same root appears in 'Abraham believed (he'emin) the LORD' (Gen 15:6)"},
        {"term": "Ur Kasdim", "transliteration": "Ur Kasdim", "meaning": "Ur of the Chaldeans -- Abraham's birthplace (Gen 11:31); in rabbinic tradition, 'Ur' is also connected to or (fire), linking it to the furnace of Nimrod narrative in Jasher"},
    ],
    "jasher-15-16": [
        {"term": "kivshan ha-esh", "transliteration": "kivshan ha-esh", "meaning": "Furnace of fire -- the fiery furnace into which Nimrod casts Abram for refusing idolatry; parallels Daniel 3 (Nebuchadnezzar's furnace); connected to 'Ur' (fire) of the Chaldeans"},
        {"term": "esh", "transliteration": "esh", "meaning": "Fire -- central to the furnace narrative; Nimrod demands Abram worship fire; Abram argues that water extinguishes fire, exposing the absurdity of worshipping created elements"},
        {"term": "hatzalah", "transliteration": "hatzalah", "meaning": "Deliverance, rescue -- God delivers Abram from the furnace, establishing the pattern of divine rescue for the faithful; same root as in the Exodus deliverance"},
        {"term": "Haran", "transliteration": "Haran", "meaning": "Abram's brother who dies in the furnace according to Jasher; his death (for hesitating between God and Nimrod) contrasts with Abram's faithful survival"},
    ],
    "jasher-17-19": [
        {"term": "berit", "transliteration": "berit", "meaning": "Covenant -- the foundational relationship structure between God and Abraham (Gen 15, 17); a binding agreement involving promises, obligations, and covenant signs"},
        {"term": "eretz", "transliteration": "eretz", "meaning": "Land, earth -- the promised land of Canaan; 'To your offspring I will give this land' (Gen 12:7); the territorial dimension of the Abrahamic covenant"},
        {"term": "milchamah", "transliteration": "milchamah", "meaning": "War, battle -- the War of the Kings (Gen 14) where Abram defeats the coalition that captured Lot; demonstrates Abram as both man of faith and capable warrior"},
        {"term": "Malki-Tsedeq", "transliteration": "Malki-Tsedeq", "meaning": "Melchizedek, 'my king is righteousness' -- the priest-king of Salem who blesses Abram (Gen 14:18-20); a Melchizedekian priesthood that precedes and supersedes the Levitical order (Heb 7)"},
    ],
    "jasher-19-20": [
        {"term": "Sedom", "transliteration": "Sedom", "meaning": "Sodom -- the city destroyed for its extreme wickedness; Jasher expands the specific sins far beyond Genesis, detailing cruelty to strangers, perversion of justice, and systemic oppression"},
        {"term": "tseaqah", "transliteration": "tseaqah", "meaning": "Outcry, cry of distress -- 'the outcry against Sodom and Gomorrah is great' (Gen 18:20-21); the cry of the oppressed that reaches God and triggers judgment"},
        {"term": "mishpat", "transliteration": "mishpat", "meaning": "Justice, judgment -- 'Shall not the Judge of all the earth do justice?' (Gen 18:25); Abraham's intercession for Sodom raises the question of divine justice and mercy"},
        {"term": "haphakhah", "transliteration": "haphakhah", "meaning": "Overthrow, overturning -- the specific term for Sodom's destruction (Gen 19:29); not mere burning but a total cosmic inversion of the created order"},
    ],
    "jasher-22-23": [
        {"term": "Aqedah", "transliteration": "Aqedah", "meaning": "The Binding -- from aqad (to bind); the binding of Isaac (Gen 22) is the supreme test of Abraham's faith and a foundational event in Jewish theology; Jasher expands the dialogue and emotional weight"},
        {"term": "olah", "transliteration": "olah", "meaning": "Burnt offering, ascending offering -- from alah (to go up); the type of sacrifice God commands for Isaac; the smoke ascends entirely to God, symbolizing total dedication"},
        {"term": "yirah", "transliteration": "yirah", "meaning": "Fear, awe, reverence -- 'Now I know that you fear (yare) God' (Gen 22:12); the Aqedah demonstrates the highest form of yirat Hashem (fear of the Lord)"},
        {"term": "Moriyyah", "transliteration": "Moriyyah", "meaning": "Mount Moriah -- the site of Isaac's binding (Gen 22:2); later identified with the Temple Mount in Jerusalem (2 Chr 3:1); from ra'ah (to see) -- 'the LORD will provide/see'"},
        {"term": "ayil", "transliteration": "ayil", "meaning": "Ram -- the ram caught in the thicket that becomes the substitute sacrifice (Gen 22:13); a type of the substitutionary atonement that culminates in Christ"},
    ],
    "jasher-24-26": [
        {"term": "shiddukhin", "transliteration": "shiddukhin", "meaning": "Marriage arrangement -- the search for Isaac's wife (Gen 24); the servant's mission to find Rebekah establishes the pattern of divinely guided marriage in the patriarchal narratives"},
        {"term": "chesed", "transliteration": "chesed", "meaning": "Loyal love, covenant faithfulness, lovingkindness -- the servant prays for God's chesed in guiding him to the right woman (Gen 24:12); the relational glue of covenant"},
        {"term": "Qeturah", "transliteration": "Qeturah", "meaning": "Keturah; from qetoret (incense) -- Abraham's wife after Sarah's death (Gen 25:1); her sons become the ancestors of Arabian peoples, extending Abraham's influence beyond the covenant line"},
        {"term": "qevurah", "transliteration": "qevurah", "meaning": "Burial -- Abraham's burial at Machpelah (Gen 25:9-10); the purchase of the cave (Gen 23) establishes the first legal land claim in Canaan, a down payment on the promise"},
    ],

    # === JACOB/JOSEPH ===
    "jasher-27-30": [
        {"term": "bekhorah", "transliteration": "bekhorah", "meaning": "Birthright, firstborn status -- the rights Esau sells to Jacob for stew (Gen 25:31-34); carries both material inheritance (double portion) and spiritual leadership of the family"},
        {"term": "berakhah", "transliteration": "berakhah", "meaning": "Blessing -- Isaac's blessing stolen by Jacob (Gen 27); in the ancient world a spoken blessing carried binding, prophetic force and could not be revoked"},
        {"term": "Esav", "transliteration": "Esav", "meaning": "Esau; meaning uncertain, possibly 'hairy' (se'ar) -- the elder twin who despises his birthright; his descendants (Edom) become perpetual adversaries of Israel"},
        {"term": "Ya'aqov", "transliteration": "Ya'aqov", "meaning": "Jacob; from aqev (heel) -- 'he grasps the heel' (Gen 25:26); also implies 'supplanter'; later renamed Israel (yisra'el, 'he struggles with God')"},
    ],
    "jasher-31-36": [
        {"term": "Peniel", "transliteration": "Peniel", "meaning": "Face of God -- 'I have seen God face to face (panim el panim) and my life is preserved' (Gen 32:30); the site of Jacob's wrestling match and transformation into Israel"},
        {"term": "Yisrael", "transliteration": "Yisrael", "meaning": "Israel; 'he struggles/strives with God' or 'God strives' -- the new name given to Jacob after wrestling the divine being at Peniel (Gen 32:28); the name of the covenant nation"},
        {"term": "milchamah", "transliteration": "milchamah", "meaning": "War, battle -- Jasher significantly expands the military exploits of Jacob's sons, depicting them as formidable warriors who conquer cities, far beyond what Genesis records"},
        {"term": "shalom", "transliteration": "shalom", "meaning": "Peace, wholeness, completeness -- Jacob and Esau's reconciliation (Gen 33) is a restoration of shalom; Jacob arrives 'shalem' (whole/at peace) at Shechem (Gen 33:18)"},
    ],
    "jasher-37-39": [
        {"term": "Edom", "transliteration": "Edom", "meaning": "Esau's territory and nation; from adom (red) -- referring to the red stew (Gen 25:30); Jasher develops the Edomite genealogy and the Zepho narrative far beyond Genesis 36"},
        {"term": "toledot", "transliteration": "toledot", "meaning": "Generations, genealogy, account -- the structuring formula of Genesis ('these are the generations of...'); Jasher follows the Edomite toledot into territories and kingdoms not covered in the Bible"},
        {"term": "Tsepho", "transliteration": "Tsepho", "meaning": "Zepho; Esau's grandson (Gen 36:11, 1 Chr 1:36) -- Jasher develops him into a major character with military campaigns across Africa and into Italy, a tradition unique to Jasher"},
        {"term": "goy", "transliteration": "goy", "meaning": "Nation, people -- the Edomite and related nations that descend from Esau; Jasher traces the spread of these nations to explain the geopolitics of the biblical world"},
    ],
    "jasher-40-44": [
        {"term": "chalom", "transliteration": "chalom", "meaning": "Dream -- Joseph's prophetic dreams (Gen 37:5-10) drive the narrative; dreams as a mode of divine revelation are central to both Genesis and Jasher's Joseph cycle"},
        {"term": "bor", "transliteration": "bor", "meaning": "Pit, cistern -- the brothers cast Joseph into a pit (Gen 37:24); in Jasher the pit contains serpents and scorpions, heightening the drama and Joseph's miraculous survival"},
        {"term": "eved", "transliteration": "eved", "meaning": "Servant, slave -- Joseph is sold as a slave (Gen 37:28); his descent from beloved son to slave to prisoner to vizier is the archetypal pattern of divine reversal"},
        {"term": "Potiphar", "transliteration": "Potiphar", "meaning": "Potiphar; an Egyptian name meaning 'he whom Ra gave' -- the captain of Pharaoh's guard who purchases Joseph (Gen 39:1); Jasher expands the household dynamics and the wife's accusation"},
        {"term": "mashbir", "transliteration": "mashbir", "meaning": "Provider of grain, sustainer -- Joseph's role in Egypt distributing grain during famine; from shavar (to buy grain); Joseph becomes the sustainer of both Egypt and his own family"},
    ],
    "jasher-45-50": [
        {"term": "achim", "transliteration": "achim", "meaning": "Brothers -- the central relational term in the Joseph narrative; the brothers who betrayed Joseph must face him in Egypt; reconciliation restores the broken brotherhood"},
        {"term": "teshuvah", "transliteration": "teshuvah", "meaning": "Repentance, return -- the brothers' transformation from jealous conspirators to men willing to sacrifice for Benjamin demonstrates genuine teshuvah; Judah's speech (Gen 44:18-34) is its climax"},
        {"term": "ra'av", "transliteration": "ra'av", "meaning": "Famine -- the severe famine that drives Jacob's sons to Egypt (Gen 42:1-2); the divine mechanism by which Joseph's dreams are fulfilled and the family reunited"},
        {"term": "Goshen", "transliteration": "Goshen", "meaning": "The fertile region of Egypt where Jacob's family settles (Gen 46:28-34); Jasher describes the settlement in detail, setting the stage for Israel's growth into a nation"},
    ],
    "jasher-51-57": [
        {"term": "avdut", "transliteration": "avdut", "meaning": "Slavery, bondage, servitude -- the Israelites' condition in Egypt after Joseph's death; from eved (servant/slave); the primary condition from which the Exodus delivers"},
        {"term": "perikhat", "transliteration": "perikhat", "meaning": "Fruitfulness, multiplication -- 'the Israelites were fruitful and multiplied greatly' (Exod 1:7); their explosive growth fulfills the Abrahamic promise but triggers Egyptian fear"},
        {"term": "sivlot", "transliteration": "sivlot", "meaning": "Burdens, forced labor -- the heavy burdens imposed on Israel (Exod 1:11); from saval (to bear a load); the oppression that precedes the cry to God"},
        {"term": "melekh chadash", "transliteration": "melekh chadash", "meaning": "New king -- 'a new king arose over Egypt who did not know Joseph' (Exod 1:8); the political shift that transforms Israel's status from honored guests to enslaved population"},
    ],

    # === EGYPT ===
    "jasher-48-50": [
        {"term": "hakkarah", "transliteration": "hakkarah", "meaning": "Recognition -- from nakhar (to recognize); the key moment when Joseph reveals himself to his brothers (Gen 45:1-3); Jasher expands the emotional weight of this recognition scene"},
        {"term": "mechilah", "transliteration": "mechilah", "meaning": "Forgiveness, pardon -- Joseph's forgiveness of his brothers (Gen 50:19-21); a model of grace that anticipates divine forgiveness; 'You meant it for evil, but God meant it for good'"},
        {"term": "shever", "transliteration": "shever", "meaning": "Grain (for purchase) -- from the same root as 'breaking' (shavar); the brothers come to Egypt to buy grain (shever), creating the context for reunion; a wordplay on brokenness and provision"},
        {"term": "Binyamin", "transliteration": "Binyamin", "meaning": "Benjamin, 'son of the right hand' -- the youngest brother whose presence Joseph demands; the test of whether the brothers have changed from the men who sold Joseph"},
    ],
    "jasher-51-56": [
        {"term": "berakhot", "transliteration": "berakhot", "meaning": "Blessings (plural) -- Jacob's deathbed blessings over the twelve sons (Gen 49); prophetic declarations that shape each tribe's destiny; Jasher adds detail to each blessing's context"},
        {"term": "Makhpelah", "transliteration": "Makhpelah", "meaning": "The Cave of Machpelah -- the burial site Abraham purchased (Gen 23); Jacob's burial procession to Machpelah becomes a military event in Jasher, with Esau's descendants contesting the burial"},
        {"term": "neshiyah", "transliteration": "neshiyah", "meaning": "Forgetfulness -- Joseph's brothers fear he will forget his promise to forgive after Jacob's death (Gen 50:15); Jasher expands their anxiety and Joseph's reassurance"},
        {"term": "shivtei Yisrael", "transliteration": "shivtei Yisrael", "meaning": "Tribes of Israel -- the twelve sons whose blessings define the tribal structure of the nation; Jacob's deathbed scene is the founding charter of Israel as a twelve-tribe confederation"},
    ],
    "jasher-59-64": [
        {"term": "shikhchah", "transliteration": "shikhchah", "meaning": "Forgetting -- 'a new king arose who did not know Joseph' (Exod 1:8); the erasure of Joseph's memory from Egyptian consciousness triggers the shift to oppression"},
        {"term": "avodat perekh", "transliteration": "avodat perekh", "meaning": "Harsh labor, crushing work -- the brutal forced labor imposed on Israel (Exod 1:13-14); perekh implies work designed to break the spirit, not merely extract labor"},
        {"term": "miskenot", "transliteration": "miskenot", "meaning": "Storage cities -- Pithom and Raamses, built by Israelite slave labor (Exod 1:11); Jasher describes the construction in detail, emphasizing the cruelty of the taskmasters"},
        {"term": "go'el", "transliteration": "go'el", "meaning": "Redeemer, kinsman-redeemer -- the role God will fill for Israel; from ga'al (to redeem, buy back); the Exodus is fundamentally an act of redemption from slavery"},
    ],
    "jasher-65-71": [
        {"term": "Mosheh", "transliteration": "Mosheh", "meaning": "Moses; from mashah (to draw out) -- 'I drew him out of the water' (Exod 2:10); the deliverer whose name encodes his origin story and foreshadows his role in the Red Sea crossing"},
        {"term": "tevah", "transliteration": "tevah", "meaning": "Basket/ark -- the same word used for Noah's ark (Gen 6:14); Moses' basket on the Nile connects him typologically to Noah: both are vessels of divine rescue through water"},
        {"term": "sar", "transliteration": "sar", "meaning": "Prince, official -- Moses raised as an Egyptian prince in Pharaoh's court; Jasher expands his years as a military and political figure before his flight from Egypt"},
        {"term": "nakhar", "transliteration": "nakhar", "meaning": "To recognize, acknowledge -- Moses sees (ra'ah) the affliction of his brothers and recognizes them as his people; the moment of identity that drives him to act (Exod 2:11)"},
    ],
    "jasher-72-76": [
        {"term": "Kush", "transliteration": "Kush", "meaning": "Ethiopia/Cush -- the African kingdom where Moses becomes king and general according to Jasher; this tradition may explain the 'Cushite wife' of Numbers 12:1"},
        {"term": "ishah kushit", "transliteration": "ishah kushit", "meaning": "Cushite woman -- the wife Moses took in Ethiopia (Num 12:1); Jasher provides the narrative backstory: a queen given to Moses as king of Cush, distinct from Zipporah"},
        {"term": "gibbor chayil", "transliteration": "gibbor chayil", "meaning": "Mighty warrior, valiant man -- Moses as military commander in Jasher; leading the Cushite army to victory before becoming their king; a dimension of Moses absent from Exodus"},
        {"term": "mamlakhah", "transliteration": "mamlakhah", "meaning": "Kingdom -- Moses rules a kingdom for forty years before departing for Midian; Jasher presents three phases of Moses' life: Egypt (prince), Cush (king), Midian (shepherd)"},
    ],
    "jasher-77-78": [
        {"term": "seneh", "transliteration": "seneh", "meaning": "Burning bush, thornbush -- the site of God's self-revelation to Moses (Exod 3:2); a lowly desert bush that burns without being consumed, symbolizing divine presence in the humble and afflicted"},
        {"term": "ehyeh asher ehyeh", "transliteration": "ehyeh asher ehyeh", "meaning": "'I AM WHO I AM' or 'I WILL BE WHAT I WILL BE' (Exod 3:14) -- the divine name revealed at the bush; the self-existent, self-defining God who needs no external reference point"},
        {"term": "shalach", "transliteration": "shalach", "meaning": "To send -- 'Come, I will send you to Pharaoh' (Exod 3:10); Moses' prophetic commissioning; the same verb used for all of God's sent messengers"},
        {"term": "Midyan", "transliteration": "Midyan", "meaning": "Midian -- the wilderness region where Moses shepherds Jethro's flocks for forty years (Exod 2:15-22); the place of preparation between royal courts and divine mission"},
    ],
    "jasher-79-80": [
        {"term": "makkot", "transliteration": "makkot", "meaning": "Plagues, strikes, blows -- the ten plagues upon Egypt (Exod 7-12); from nakah (to strike); each plague systematically dismantles an Egyptian deity and Pharaoh's claim to divine authority"},
        {"term": "ot u-mofet", "transliteration": "ot u-mofet", "meaning": "Sign and wonder -- the paired terms for God's miraculous acts in Egypt (Exod 7:3); 'ot' signifies meaning, 'mofet' signifies power; together they reveal God's character through action"},
        {"term": "chazaq lev", "transliteration": "chazaq lev", "meaning": "Hardened heart -- Pharaoh's heart is hardened/strengthened (Exod 7:13); the Hebrew uses three different roots (chazaq, kaved, qashah), suggesting a progressive judicial hardening"},
        {"term": "Pesach", "transliteration": "Pesach", "meaning": "Passover -- from pasach (to pass over, skip); the final plague where the destroyer passes over houses marked with lamb's blood (Exod 12); the foundational redemptive event of Israel"},
    ],
    "jasher-81-82": [
        {"term": "yam suph", "transliteration": "yam suph", "meaning": "Sea of Reeds (Red Sea) -- the body of water God divides for Israel's crossing (Exod 13:18, 15:4); suph means 'reeds/rushes'; the crossing is the definitive act of divine deliverance"},
        {"term": "geulah", "transliteration": "geulah", "meaning": "Redemption -- the Exodus is the paradigmatic act of redemption in the Hebrew Bible; God as go'el (redeemer) buys Israel out of slavery with 'an outstretched arm and mighty hand'"},
        {"term": "shirah", "transliteration": "shirah", "meaning": "Song -- the Song of the Sea (Exod 15:1-18); Israel's response to deliverance; 'I will sing to the LORD, for He has triumphed gloriously; horse and rider He has thrown into the sea'"},
        {"term": "yad chazaqah", "transliteration": "yad chazaqah", "meaning": "Mighty hand -- 'the LORD brought us out of Egypt with a mighty hand' (Exod 13:14); the signature phrase for God's power displayed in the Exodus; paired with 'outstretched arm' (zeroa netuyah)"},
    ],

    # === MOSES ===
    "jasher-58-60": [
        {"term": "yeled", "transliteration": "yeled", "meaning": "Child, boy -- Moses as an infant drawn from the Nile (Exod 2:6); Jasher adds the tradition of the child Moses taking Pharaoh's crown, which triggers a test of his intelligence"},
        {"term": "bat Par'oh", "transliteration": "bat Par'oh", "meaning": "Daughter of Pharaoh -- the princess who adopts Moses (Exod 2:5-10); Jasher names her and expands her role, giving her political maneuvering to protect the Hebrew child"},
        {"term": "chokmah", "transliteration": "chokmah", "meaning": "Wisdom -- Moses educated in all the wisdom (chokmah) of Egypt (Acts 7:22); Jasher describes his training in Egyptian learning as preparation for his future role as lawgiver"},
        {"term": "nezer", "transliteration": "nezer", "meaning": "Crown, diadem -- the tradition (found in Jasher and earlier midrash) of infant Moses seizing Pharaoh's crown; the advisors test whether the child acts with intent or innocence"},
    ],
    "jasher-61-63": [
        {"term": "melekh Kush", "transliteration": "melekh Kush", "meaning": "King of Cush -- Moses' forty-year reign over Ethiopia according to Jasher; the most dramatic expansion of Moses' biography in the entire book"},
        {"term": "tsava", "transliteration": "tsava", "meaning": "Army, host, military force -- Moses leads the Cushite army as their general before becoming king; demonstrating military leadership that prefigures his leading Israel through the wilderness"},
        {"term": "gevurah", "transliteration": "gevurah", "meaning": "Strength, might, heroic power -- Moses' military prowess in Ethiopia; Jasher presents a warrior-Moses phase that complements the prophet-Moses of Exodus"},
        {"term": "galut", "transliteration": "galut", "meaning": "Exile -- Moses' departure from Cush and journey to Midian; each phase of his life involves exile and displacement before his ultimate calling at the burning bush"},
    ],
    "jasher-64-67": [
        {"term": "YHWH", "transliteration": "YHWH", "meaning": "The divine name (Tetragrammaton) -- revealed to Moses at the burning bush (Exod 3:14-15); 'I AM WHO I AM'; the personal, covenant name of the God of Abraham, Isaac, and Jacob"},
        {"term": "shaliach", "transliteration": "shaliach", "meaning": "Sent one, messenger, agent -- Moses as God's commissioned agent to Pharaoh; the shaliach carries the full authority of the one who sends; Moses speaks and acts with divine authority"},
        {"term": "matteh", "transliteration": "matteh", "meaning": "Staff, rod -- Moses' staff that becomes a serpent and performs signs (Exod 4:2-4); the instrument of God's power in the plagues; later the rod that parts the sea and strikes the rock"},
        {"term": "dam", "transliteration": "dam", "meaning": "Blood -- the first plague turns the Nile to blood (Exod 7:20); attacks Hapi, the Nile god; blood as the symbol of both judgment (plagues) and redemption (Passover lamb)"},
    ],
    "jasher-68-71": [
        {"term": "baqa", "transliteration": "baqa", "meaning": "To split, divide, cleave -- the verb for splitting the sea (Exod 14:16, 21); God divides the waters as at creation (Gen 1:6-7); the sea crossing is a new creation act"},
        {"term": "Sinai", "transliteration": "Sinai", "meaning": "Mount Sinai (also called Horeb) -- the mountain of God where the Torah is given (Exod 19-20); the site of divine theophany with fire, smoke, thunder, and the voice of God"},
        {"term": "Torah", "transliteration": "Torah", "meaning": "Instruction, teaching, law -- from yarah (to throw, direct, teach); the covenant instructions given at Sinai; not merely 'law' but comprehensive divine instruction for covenant life"},
        {"term": "midbar", "transliteration": "midbar", "meaning": "Wilderness, desert -- the setting for Israel's forty-year journey; from davar (to speak) -- the wilderness is where God speaks; a place of testing, provision, and intimate divine encounter"},
    ],
    "jasher-72-81": [
        {"term": "meraglim", "transliteration": "meraglim", "meaning": "Spies, scouts -- the twelve spies sent to Canaan (Num 13); from ragal (to walk about, spy out); ten return with a faithless report, two (Joshua, Caleb) with faith"},
        {"term": "am qesheh oref", "transliteration": "am qesheh oref", "meaning": "Stiff-necked people -- God's repeated description of Israel's stubbornness (Exod 32:9, 33:3, 34:9); the image of an ox that refuses to turn when directed"},
        {"term": "nachash nechoshet", "transliteration": "nachash nechoshet", "meaning": "Bronze serpent -- the serpent Moses lifts on a pole to heal snakebites (Num 21:8-9); Jesus identifies this as a type of his crucifixion (John 3:14-15)"},
        {"term": "nachalah", "transliteration": "nachalah", "meaning": "Inheritance, allotted portion -- the promised land as Israel's inheritance (Num 26:53); each tribe receives its nachalah; the land is God's gift, not a human conquest"},
    ],

    # === CONQUEST ===
    "jasher-83-84": [
        {"term": "luchot", "transliteration": "luchot", "meaning": "Tablets -- the two stone tablets inscribed by God's finger (Exod 31:18, 32:15-16); smashed by Moses at the golden calf; rewritten as an act of covenant renewal"},
        {"term": "egel", "transliteration": "egel", "meaning": "Calf -- the golden calf fashioned by Aaron (Exod 32:4); an Egyptian/Canaanite fertility symbol; Israel's first great apostasy after receiving the covenant"},
        {"term": "aseret ha-dibrot", "transliteration": "aseret ha-dibrot", "meaning": "Ten Words/Commandments -- literally 'ten utterances' (Exod 34:28); the summary of covenant obligation; the foundation of Israel's legal and moral order"},
        {"term": "kavod", "transliteration": "kavod", "meaning": "Glory, weight, honor -- the glory of the LORD that descends on Sinai (Exod 24:16-17) and fills the Tabernacle (Exod 40:34); the visible manifestation of God's presence"},
    ],
    "jasher-85-86": [
        {"term": "meraglim", "transliteration": "meraglim", "meaning": "Spies -- the twelve spies sent to Canaan (Num 13:2); their faithless report leads to forty years of wilderness wandering; only Joshua and Caleb enter the promised land"},
        {"term": "meri", "transliteration": "meri", "meaning": "Rebellion, bitterness -- Israel's repeated rebellion against God in the wilderness (Num 14:9, 20:10); from marah (to be bitter, rebellious); the defining sin of the wilderness generation"},
        {"term": "Miryam", "transliteration": "Miryam", "meaning": "Miriam -- Moses' sister, a prophetess (Exod 15:20); her death at Kadesh (Num 20:1) marks the end of the first generation; tradition connects her to the miraculous well that sustained Israel"},
        {"term": "Aharon", "transliteration": "Aharon", "meaning": "Aaron -- Moses' brother, the first high priest; his death on Mount Hor (Num 20:22-29) transfers the priesthood to Eleazar; Jasher describes the mourning period"},
    ],
    "jasher-87": [
        {"term": "Bil'am", "transliteration": "Bil'am", "meaning": "Balaam -- the pagan diviner hired by Balak to curse Israel (Num 22-24); instead blesses them by divine compulsion; a complex figure who knows YHWH but serves other interests"},
        {"term": "cherem", "transliteration": "cherem", "meaning": "Devoted to destruction, ban -- the total destruction commanded for Sihon and Og's kingdoms (Num 21:2-3, Deut 2:34); devoted entirely to God as an act of holy war"},
        {"term": "Og", "transliteration": "Og", "meaning": "Og king of Bashan -- a giant whose iron bed measured 9 by 4 cubits (Deut 3:11); one of the last of the Rephaim (remnant giant clans); his defeat opens the Transjordan for settlement"},
        {"term": "mot Mosheh", "transliteration": "mot Mosheh", "meaning": "Death of Moses -- Moses dies on Mount Nebo overlooking the promised land (Deut 34:1-5); 'the LORD buried him' (Deut 34:6); Jasher describes the transition of leadership to Joshua"},
    ],
    "jasher-89-91": [
        {"term": "nachalah", "transliteration": "nachalah", "meaning": "Inheritance, allotted portion -- the tribal territories distributed by Joshua (Josh 13-21); each tribe receives its allotted land as fulfillment of the Abrahamic promise"},
        {"term": "kibbush", "transliteration": "kibbush", "meaning": "Conquest -- from kavash (to subdue, conquer); the military campaign to take Canaan; Jasher summarizes the northern and southern campaigns and the settlement process"},
        {"term": "shofetim", "transliteration": "shofetim", "meaning": "Judges -- the leaders who arise after Joshua's death (Judg 2:16-18); Jasher's final chapters bridge the conquest into the Judges period, a time of cyclical apostasy and deliverance"},
        {"term": "Yehoshua", "transliteration": "Yehoshua", "meaning": "Joshua; 'YHWH saves' or 'YHWH is salvation' -- Moses' successor who leads the conquest of Canaan; his name is the Hebrew form of 'Jesus' (Greek Iesous), connecting the two deliverers"},
    ],
}


def fill_file(filepath, chapter_terms):
    """Replace empty hebrew_terms in a file based on chapter ID mapping."""
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # First pass: find ALL empty hebrew_terms positions and map them to line-level context
    # Strategy: find each "hebrew_terms": [] and look backwards to find the nearest "id" field
    empty_pattern = re.compile(r'"hebrew_terms":\s*\[\]')
    id_pattern = re.compile(r'"id":\s*"([^"]+)"')

    # Collect all matches with their positions
    replacements_to_make = []  # list of (start, end, new_text)

    for empty_match in empty_pattern.finditer(content):
        # Look backwards from this position for the nearest chapter id
        preceding = content[:empty_match.start()]
        id_matches = list(id_pattern.finditer(preceding))
        if not id_matches:
            continue
        nearest_id = id_matches[-1].group(1)

        if nearest_id in chapter_terms:
            terms = chapter_terms[nearest_id]
            term_strs = []
            for t in terms:
                term_strs.append(
                    '            {\n'
                    f'                "term": "{t["term"]}",\n'
                    f'                "transliteration": "{t["transliteration"]}",\n'
                    f'                "meaning": "{t["meaning"]}"\n'
                    '            }'
                )
            new_terms = '"hebrew_terms": [\n' + ",\n".join(term_strs) + "\n        ]"
            replacements_to_make.append((empty_match.start(), empty_match.end(), new_terms, nearest_id))

    # Apply replacements from bottom to top so positions don't shift
    count = 0
    for start, end, new_text, ch_id in reversed(replacements_to_make):
        content = content[:start] + new_text + content[end:]
        count += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return count


# Group terms by file
file_chapters = {
    'data/jasher/era_jasher_primeval.py': {k: v for k, v in TERMS.items() if k in [
        'jasher-intro', 'jasher-1-2', 'jasher-3-4', 'jasher-5-6', 'jasher-7', 'jasher-9-10', 'jasher-11-13'
    ]},
    'data/jasher/era_jasher_abraham.py': {k: v for k, v in TERMS.items() if k in [
        'jasher-14-15', 'jasher-15-16', 'jasher-17-19', 'jasher-19-20', 'jasher-22-23', 'jasher-24-26'
    ]},
    'data/jasher/era_jasher_jacob_joseph.py': {k: v for k, v in TERMS.items() if k in [
        'jasher-27-30', 'jasher-31-36', 'jasher-37-39', 'jasher-40-44', 'jasher-45-50', 'jasher-51-57'
    ]},
    'data/jasher/era_jasher_egypt.py': {k: v for k, v in TERMS.items() if k in [
        'jasher-48-50', 'jasher-51-56', 'jasher-59-64', 'jasher-65-71', 'jasher-72-76', 'jasher-77-78', 'jasher-79-80', 'jasher-81-82'
    ]},
    'data/jasher/era_jasher_moses.py': {k: v for k, v in TERMS.items() if k in [
        'jasher-58-60', 'jasher-61-63', 'jasher-64-67', 'jasher-68-71', 'jasher-72-81'
    ]},
    'data/jasher/era_jasher_conquest.py': {k: v for k, v in TERMS.items() if k in [
        'jasher-83-84', 'jasher-85-86', 'jasher-87', 'jasher-89-91'
    ]},
}

total = 0
for filepath, chapters in file_chapters.items():
    full_path = os.path.join(BASE, filepath)
    n = fill_file(full_path, chapters)
    print(f"{filepath}: {n} chapters filled")
    total += n

print(f"\nTotal chapters filled: {total}")
