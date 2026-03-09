"""
CORE BELIEFS — The Governance Architecture of Scripture

This is NOT systematic theology. This is the GOVERNANCE ARCHITECTURE — how God
administers His creation through council, covenant, and delegated authority.

Systematic theology asks: "What does the Bible teach about X?"
Governance architecture asks: "How does X function in God's administration?"

The difference matters. Theology catalogs truths. Governance reveals how those
truths OPERATE — who has authority, how it was delegated, when it was corrupted,
how it is being restored, and where it resolves.

Framework:
  - Literal Genesis, young-earth (~6,000 years) timeline
  - Scripture is primary authority
  - Michael Heiser's divine council framework as interpretive lens
  - Confidence: A = text-explicit, B = biblical inference, C = theological reasoning

Categories (10):
  ONTOLOGY           — God, Divine Council, the nature of reality
  COSMOLOGY          — Seen + unseen structure, cosmic geography, time
  ANTHROPOLOGY       — Imago Dei, body/soul/spirit, human purpose in the council
  COSMIC_REBELLION   — Eden, Watchers, Babel — the triad of rebellions
  COVENANT           — Noahic, Abrahamic, Mosaic, Davidic, New — the backbone
  MESSIAH_ATONEMENT  — Christology, the cross, substitution + Christus Victor
  SPIRIT             — Pneumatology, gifts, filling, indwelling
  CHURCH_COUNCIL     — Church as reconstituted council (Eph 3:10, 1 Cor 6:2-3)
  KINGDOM            — Authority, spiritual warfare, believer's role
  RESTORATION        — Second coming, judgment, new creation, final governance transfer
"""

# ══════════════════════════════════════════════════════════════
# BELIEF CATEGORIES
# ══════════════════════════════════════════════════════════════

BELIEF_CATEGORIES = [
    {"id": "ONTOLOGY", "name": "Ontology — The Nature of Reality", "color": "#c9a84c", "order": 1},
    {"id": "COSMOLOGY", "name": "Cosmology — Seen & Unseen Structure", "color": "#5b8dbf", "order": 2},
    {"id": "ANTHROPOLOGY", "name": "Anthropology — Humanity in the Council", "color": "#7ab648", "order": 3},
    {"id": "COSMIC_REBELLION", "name": "Cosmic Rebellion — The Three Rebellions", "color": "#d94f4f", "order": 4},
    {"id": "COVENANT", "name": "Covenant — The Governance Backbone", "color": "#e8a838", "order": 5},
    {"id": "MESSIAH_ATONEMENT", "name": "Messiah & Atonement — The Divine Rescue", "color": "#b84cc9", "order": 6},
    {"id": "SPIRIT", "name": "Spirit — The Empowering Presence", "color": "#4cc9c0", "order": 7},
    {"id": "CHURCH_COUNCIL", "name": "Church as Council — The Cosmic Announcement", "color": "#c97a4c", "order": 8},
    {"id": "KINGDOM", "name": "Kingdom — Authority & Warfare", "color": "#4c6ec9", "order": 9},
    {"id": "RESTORATION", "name": "Restoration — Final Governance Transfer", "color": "#c9c94c", "order": 10},
]

# ══════════════════════════════════════════════════════════════
# CORE BELIEFS
# ══════════════════════════════════════════════════════════════

CORE_BELIEFS = [

    # ══════════════════════════════════════════════════════════════
    # ONTOLOGY — GOD, DIVINE COUNCIL, THE NATURE OF REALITY
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B01',
        'category': 'ONTOLOGY',
        'title': 'The One True God — Yahweh as Incomparable',
        'subtitle': 'Yahweh is unique among all elohim — not alone, but without peer.',
        'key_texts': ['Isaiah 44:6-8', 'Deuteronomy 6:4', 'Psalm 82:1', 'Deuteronomy 32:8-9', 'Psalm 89:6-7'],
        'council_relevance': 'Yahweh presides over the divine council as its unchallenged sovereign. The other elohim exist, but none compare to Him. Psalm 89:6 asks "Who among the bene elim is like Yahweh?" — presupposing real beings who are categorically inferior. Biblical monotheism is not denial of other spiritual beings but the declaration that Yahweh alone is the species-unique, uncreated Creator.',
        'covenant_link': 'All covenants — Yahweh is the sole suzerain of every covenant. His incomparability is the foundation on which covenant authority rests.',
        'eschatological_trajectory': 'Every knee bows (Phil 2:10-11). The corrupt elohim are judged (Ps 82:6-7). At the eschaton, Yahweh\'s incomparability is publicly vindicated before all beings, seen and unseen.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'There is one God, Yahweh, who is the Creator of all things, including the spiritual beings (elohim) of His council. He is not "alone" in the sense that no other spiritual beings exist — Scripture is clear they do (Ps 82, 89, Job 1-2, 1 Kings 22). He is alone in the sense that none can compare to Him. This is the Heiser distinction: Yahweh is an elohim, but no other elohim is Yahweh.',
        'historical_figures': [
            {'name': 'Athanasius of Alexandria', 'position': 'Defended the unique, uncreated nature of God against Arianism — the Son shares the Father\'s essence, not a created being.', 'orthodox': True},
            {'name': 'Michael Heiser', 'position': 'Recovered the divine council framework: biblical monotheism means Yahweh is species-unique among the elohim, not that no other elohim exist.', 'orthodox': True},
            {'name': 'Marcion of Sinope', 'position': 'Rejected the OT God as a lesser deity distinct from the NT God — a fundamental misreading of the biblical text.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'elohim (אֱלֹהִים) — not "God" exclusively but "spiritual being, divine one." Yahweh is an elohim; the council members are elohim. The Shema: echad (אֶחָד) = "one" in Deut 6:4. mi kamokha ba\'elim YHWH (מִי כָמֹכָה בָּאֵלִם יהוה) — "Who is like you among the gods, O Yahweh?" (Exod 15:11).',
        'summary': 'Yahweh is the incomparable God who presides over a real council of subordinate spiritual beings (elohim). Biblical monotheism does not deny the existence of other spiritual beings but declares that Yahweh alone is the uncreated, sovereign Creator — the God above all gods. This is the foundation of all governance: every authority in heaven and earth derives from Him.',
    },
    {
        'id': 'B02',
        'category': 'ONTOLOGY',
        'title': 'The Divine Council — Sod YHWH',
        'subtitle': 'God governs through a council of spiritual beings — this is His chosen administrative structure.',
        'key_texts': ['Psalm 82:1', 'Psalm 89:5-7', '1 Kings 22:19-22', 'Job 1:6-12', 'Jeremiah 23:18'],
        'council_relevance': 'This IS the council. Psalm 82:1 — "God stands in the divine assembly (adat-el); He judges among the elohim." 1 Kings 22 shows it in session: Yahweh on His throne, the host around Him, a deliberation, a decision, a commissioned agent. Job 1-2 shows the bene ha\'elohim presenting themselves before Yahweh with the satan among them. Jeremiah 23:18 treats standing in the sod YHWH as the credential of a true prophet.',
        'covenant_link': 'The covenant is the council\'s instrument for governing humanity. The prophets who stand in the sod deliver the riv (covenant lawsuit). The council is the legislature; the covenant is the legislation.',
        'eschatological_trajectory': 'The corrupt council members are judged (Ps 82:6-7), the faithful ones remain (the holy ones of Dan 7:18), and redeemed humans join the council (1 Cor 6:2-3, Rev 3:21). The council is restored and expanded, not abolished.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'God governs His creation through a council of spiritual beings. This is not mythology imported into the Bible — it is the Bible\'s own framework, visible in Psalms, Job, 1 Kings, Isaiah 6, Daniel 7, and Jeremiah. The council is Yahweh\'s chosen administrative structure: real beings with real delegated authority, accountable to Him.',
        'historical_figures': [
            {'name': 'Michael Heiser', 'position': 'Recovered the divine council as the interpretive context for the entire biblical narrative — from creation through eschatology.', 'orthodox': True},
            {'name': 'Frank Moore Cross', 'position': 'Identified the divine council motif as central to Israelite religion, rooted in the Canaanite antecedents but uniquely Yahwistic.', 'orthodox': True},
            {'name': 'Rudolf Bultmann', 'position': 'Demythologized spiritual beings as pre-scientific worldview artifacts — a position that requires ignoring the biblical text\'s own claims.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'sod YHWH (סוֹד יהוה) — the council/assembly of Yahweh (Jer 23:18). adat-el (עֲדַת אֵל) — the assembly of God (Ps 82:1). bene elohim (בְּנֵי הָאֱלֹהִים) — sons of God, council members (Job 1:6, 2:1). qadoshim (קְדֹשִׁים) — holy ones, the loyal council (Ps 89:5, Dan 7:18).',
        'summary': 'The divine council is God\'s administrative body — spiritual beings who serve, deliberate, and execute His will. This is not an optional interpretive lens; it is the framework the biblical authors assumed. Understanding it unlocks the logic of spiritual warfare, the prophetic office, the cosmic rebellions, and the eschatological restoration.',
    },
    {
        'id': 'B03',
        'category': 'ONTOLOGY',
        'title': 'The Trinity — Plurality Within Unity',
        'subtitle': 'God is echad (unified one), not yachid (solitary one) — plurality within the Godhead is an OT reality.',
        'key_texts': ['Genesis 1:26', 'Deuteronomy 6:4', 'Isaiah 48:16', 'Psalm 110:1', 'Daniel 7:13-14'],
        'council_relevance': 'The Trinity is the inner council of God Himself. The "let us make" of Gen 1:26 is not addressed to angels (who do not create) but reflects plurality within the Godhead. The "two Yahwehs" motif (Gen 19:24 — "Yahweh rained fire from Yahweh") and the "two powers in heaven" tradition recognized by early Judaism point to a second divine person distinguishable from yet identical to the Father. Daniel 7:13-14 shows two enthroned divine figures — the Ancient of Days and the Son of Man — sharing sovereign authority.',
        'covenant_link': 'Each person of the Trinity has a covenant role: the Father initiates, the Son mediates, the Spirit applies. The New Covenant explicitly involves all three (Jer 31:31-34 / Heb 8-10, the Son\'s blood, the Spirit\'s indwelling).',
        'eschatological_trajectory': 'The Son delivers the kingdom to the Father (1 Cor 15:24-28). The Spirit completes the transformation of believers. The Trinity is not diminished but fully revealed in the eschaton.',
        'governance_tag': 'creation_order',
        'confidence': 'B',
        'orthodox_position': 'God is one Being (echad) who exists eternally as three Persons — Father, Son, and Holy Spirit. This is not a NT invention imposed on the OT. The OT contains the "two powers in heaven" motif (two Yahwehs in Gen 19:24, the Angel of Yahweh who IS Yahweh in Exod 3, two enthroned figures in Dan 7:13-14, two Lords in Ps 110:1). The NT makes explicit what the OT embedded.',
        'historical_figures': [
            {'name': 'Athanasius of Alexandria', 'position': 'Defended homoousios (same substance) at Nicaea — the Son is of the same essence as the Father, not a created being.', 'orthodox': True},
            {'name': 'The Cappadocian Fathers', 'position': 'Basil, Gregory of Nazianzus, Gregory of Nyssa — clarified one ousia (essence), three hypostaseis (persons).', 'orthodox': True},
            {'name': 'Arius', 'position': 'Taught the Son was the first created being — "there was a time when the Son was not." Denied the co-eternity and co-equality of the Son.', 'orthodox': False},
            {'name': 'Sabellius', 'position': 'Taught modalism — one God who manifests in three sequential modes, not three co-eternal persons. Denies the interpersonal relationships within the Godhead.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'echad (אֶחָד) — "one" (compound unity, as in "one flesh" Gen 2:24), used in the Shema. yachid (יָחִיד) — "only, solitary" — notably NOT used in the Shema. homoousios (ὁμοούσιος) — "same substance/essence," the Nicene term. hypostasis (ὑπόστασις) — "person/subsistence." The "two powers" tradition: shenei rashuyyot (שְׁנֵי רְשֻׁיּוֹת).',
        'summary': 'The Trinity is the inner governance structure of God Himself — three Persons in one essence, operating in perfect unity and distinct roles. The OT seeds this with the "two powers" motif, and the NT harvests it. This is not philosophical speculation but the revealed architecture of deity, with direct implications for how authority is delegated and exercised in creation.',
    },
    {
        'id': 'B04',
        'category': 'ONTOLOGY',
        'title': 'God\'s Attributes Through Governance',
        'subtitle': 'Sovereignty is expressed through delegation, not micromanagement — God rules through agents.',
        'key_texts': ['Psalm 115:16', 'Genesis 1:28', 'Deuteronomy 32:8-9', 'Daniel 4:17', 'Matthew 28:18'],
        'council_relevance': 'This is the operating principle of the entire council framework. God is sovereign over all, but He has chosen to exercise that sovereignty through delegated authority — to spiritual beings (the council), to humans (the dominion mandate), and ultimately to Christ (Matt 28:18). Psalm 115:16 states the principle: "The heavens are the LORD\'s heavens, but the earth He has given to the children of man." Delegation is not weakness; it is the chosen mode of divine governance.',
        'covenant_link': 'Every covenant is an act of delegation: Noahic (stewardship of creation), Abrahamic (blessing the nations), Mosaic (priestly kingdom), Davidic (throne authority), New (Spirit-empowered participation).',
        'eschatological_trajectory': 'The final governance transfer — the Son delivers the kingdom to the Father (1 Cor 15:24-28), and redeemed humanity reigns forever (Rev 22:5). Delegation is not a temporary measure but the eternal pattern.',
        'governance_tag': 'creation_order',
        'confidence': 'B',
        'orthodox_position': 'God is omnipotent, omniscient, and omnipresent — and He has chosen to govern through real delegation to real agents with real authority and real accountability. He gives the earth to humans (Ps 115:16), assigns nations to elohim (Deut 32:8), entrusts the kingdom to the Son (Dan 7:14), and empowers the church through the Spirit. This delegation is genuine, not theatrical.',
        'historical_figures': [
            {'name': 'John Calvin', 'position': 'Emphasized God\'s absolute sovereignty, sometimes at the expense of genuine creaturely agency. Correct on sovereignty, incomplete on delegation.', 'orthodox': True},
            {'name': 'Greg Boyd', 'position': 'Emphasizes genuine creaturely freedom and spiritual warfare, but his open theism overreacts by limiting God\'s foreknowledge. Right on delegation, wrong on omniscience.', 'orthodox': False},
            {'name': 'Thomas Aquinas', 'position': 'Articulated primary and secondary causation — God as the primary cause working through secondary causes (agents). A helpful philosophical framework for delegation.', 'orthodox': True},
        ],
        'key_hebrew_greek': 'radah (רָדָה) — "to rule, have dominion" (Gen 1:28). mashal (מָשַׁל) — "to govern, reign." natan (נָתַן) — "to give, entrust" (Ps 115:16, the earth "given" to humanity). exousia (ἐξουσία) — "authority" (Matt 28:18, delegated from Father to Son to church).',
        'summary': 'God\'s sovereignty is expressed through delegation, not totalitarian micromanagement. He created a council, delegated authority to spiritual beings and humans, and governs through covenant relationship. When agents rebel, He does not abolish delegation — He judges the rebels and raises up faithful replacements. This pattern runs from Genesis to Revelation.',
    },

    # ══════════════════════════════════════════════════════════════
    # COSMOLOGY — SEEN & UNSEEN STRUCTURE
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B05',
        'category': 'COSMOLOGY',
        'title': 'Creation Ex Nihilo — Six Days, Young Earth',
        'subtitle': 'God created the heavens and earth in six literal days from nothing — no gap, no ages.',
        'key_texts': ['Genesis 1:1-2:3', 'Exodus 20:11', 'Psalm 33:6-9', 'Hebrews 11:3', 'Colossians 1:16'],
        'council_relevance': 'Creation is the first act of governance — God establishing His domain and populating it with agents. The six-day structure is itself administrative: days 1-3 form the realms (light/dark, sky/sea, land), days 4-6 fill them with rulers (luminaries, birds/fish, animals/humans). The pattern is kingdom-building: create territory, install rulers. Job 38:4-7 places the bene elohim (sons of God) as witnesses at creation — the council was present.',
        'covenant_link': 'Creation is the pre-covenant foundation. The Sabbath rest of Day 7 becomes the covenant sign of the Mosaic covenant (Exod 31:13-17). Creation order establishes the categories that covenants govern.',
        'eschatological_trajectory': 'New creation (Rev 21:1) — "Behold, I make all things new." The trajectory is not escape from the material world but its restoration and perfection. Creation is not abandoned; it is redeemed.',
        'governance_tag': 'creation_order',
        'confidence': 'A',
        'orthodox_position': 'God created the heavens and the earth in six literal, consecutive, 24-hour days approximately 6,000 years ago. The Hebrew yom with ordinal number and evening/morning formula demands literal days. Exodus 20:11 confirms it: "in six days the LORD made heaven and earth." Ex nihilo — from nothing (Heb 11:3). No gap theory, no day-age, no framework hypothesis. The text means what it says.',
        'historical_figures': [
            {'name': 'Basil of Caesarea', 'position': 'His Hexaemeron (homilies on the six days) insisted on the literal, historical reading of Genesis 1. Rejected allegorization.', 'orthodox': True},
            {'name': 'Martin Luther', 'position': 'Insisted on six literal days: "The days of creation were ordinary days in length. We must understand that these days were actual days, contrary to the opinion of the holy fathers."', 'orthodox': True},
            {'name': 'Charles Darwin', 'position': 'Proposed natural selection over deep time as the mechanism of biological diversity — a framework incompatible with the biblical account of special creation.', 'orthodox': False},
            {'name': 'Hugh Ross', 'position': 'Day-age creationism — each "day" is a long epoch. Attempts to harmonize Genesis with mainstream cosmology but does violence to the Hebrew text.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'bara (בָּרָא) — "to create" (used only of God, implies creation from nothing). yom (יוֹם) — "day" (with ordinal number = literal day in every other OT usage). erev va-voker (עֶרֶב וָבֹקֶר) — "evening and morning" — temporal markers defining literal days. tohu va-vohu (תֹהוּ וָבֹהוּ) — "formless and void" — the initial state before God\'s ordering work.',
        'summary': 'Creation in six literal days is the foundational governance act — God building His kingdom, forming territories, and installing rulers. The young-earth timeline is not a secondary issue; it anchors the entire biblical chronology from Adam to Christ. Creation ex nihilo establishes God\'s absolute ownership of everything that exists.',
    },
    {
        'id': 'B06',
        'category': 'COSMOLOGY',
        'title': 'Cosmic Geography — Three-Tiered Reality',
        'subtitle': 'The biblical cosmos has three tiers: heavens (shamayim), earth (erets), and underworld (sheol) — all real.',
        'key_texts': ['Exodus 20:4', 'Philippians 2:10', 'Revelation 5:3', '2 Kings 6:17', 'Ephesians 4:9-10'],
        'council_relevance': 'The three tiers are governance zones. The heavens are God\'s throne room and council chamber (1 Kings 22:19, Isa 6). The earth is the delegated domain of humanity (Ps 115:16). The underworld is the prison for rebellious spirits (2 Pet 2:4, Jude 6) and the abode of the dead. Christ\'s victory spans all three: He descended to the lower parts (Eph 4:9), walked the earth, and ascended far above all heavens (Eph 4:10). Philippians 2:10 — every knee bows "in heaven, on earth, and under the earth."',
        'covenant_link': 'The Mosaic covenant\'s second commandment references all three tiers (Exod 20:4). The tabernacle/temple architecture mirrors cosmic geography: Holy of Holies = heaven, Holy Place = visible creation, outer court = the world.',
        'eschatological_trajectory': 'New heaven and new earth (Rev 21:1) — the three tiers are unified under God\'s direct presence. The sea (chaos/abyss) is "no more." The underworld gives up its dead (Rev 20:13). The separation between seen and unseen is healed.',
        'governance_tag': 'creation_order',
        'confidence': 'B',
        'orthodox_position': 'The biblical cosmos is structured in three tiers: the heavens (God\'s throne, the council chamber, the dwelling of spiritual beings), the earth (humanity\'s delegated domain), and the underworld (sheol/hades, the realm of the dead and imprisoned spirits). These are real places, not metaphors. The "unseen realm" is as real as the visible world — Elisha\'s prayer in 2 Kings 6:17 reveals the chariots of fire that were always there.',
        'historical_figures': [
            {'name': 'Michael Heiser', 'position': 'Articulated the three-tiered cosmic geography as the assumed framework of the biblical authors, not borrowed mythology.', 'orthodox': True},
            {'name': 'N.T. Wright', 'position': 'Emphasizes that "heaven" in biblical thought is not a distant place but a dimension of reality that overlaps with earth — especially in the temple.', 'orthodox': True},
            {'name': 'Rudolf Bultmann', 'position': 'Dismissed the three-tiered cosmos as primitive mythology requiring demythologization for modern audiences.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'shamayim (שָׁמַיִם) — "heavens" (plural, multiple levels — Paul references "third heaven" in 2 Cor 12:2). erets (אֶרֶץ) — "earth, land." sheol (שְׁאוֹל) — the underworld, realm of the dead. tehom (תְּהוֹם) — "the deep, abyss" — the primordial waters, associated with chaos. tartaroo (ταρταρόω) — "cast into Tartarus" (2 Pet 2:4), the prison of the Watchers.',
        'summary': 'The biblical cosmos is a three-tiered governance structure: heavens (God\'s throne and council chamber), earth (humanity\'s delegated domain), and underworld (prison and abode of the dead). This is not primitive cosmology — it is the administrative map of reality. Christ\'s work spans all three tiers, and the eschaton reunifies them under God\'s direct presence.',
    },
    {
        'id': 'B07',
        'category': 'COSMOLOGY',
        'title': 'The Unseen Realm — Spiritual Reality',
        'subtitle': 'The spiritual world is as real as the physical — not metaphor, not mythology, not pre-scientific ignorance.',
        'key_texts': ['2 Kings 6:15-17', 'Ephesians 6:12', 'Colossians 1:16', 'Daniel 10:12-13', 'Hebrews 1:14'],
        'council_relevance': 'The unseen realm IS the council\'s operating theater. Daniel 10 shows a spiritual being delayed 21 days by the "prince of Persia" (a territorial spirit) until Michael intervened. This reveals that the council\'s operations are ongoing, contested, and directly affect earthly events. Colossians 1:16 catalogues the hierarchy: thrones, dominions, rulers, authorities — all created by and for Christ.',
        'covenant_link': 'The unseen realm is where covenant enforcement happens. The satan functions as a prosecuting attorney in the divine council (Job 1-2, Zech 3:1). The "accuser of the brethren" (Rev 12:10) brings covenant-lawsuit charges. Christ\'s blood silences the accusation.',
        'eschatological_trajectory': 'The veil between seen and unseen is removed. Believers see face to face (1 Cor 13:12). The nations of the unseen realm (angels, redeemed humanity) worship together before the throne (Rev 5:11-14).',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'The spiritual realm is objectively real. Angels, demons, territorial spirits, and the divine council are not metaphors, cultural accommodations, or mythological borrowings. They are real beings operating in a real dimension of reality that overlaps with and influences the physical world. Denying the unseen realm is not sophistication — it is blindness (2 Cor 4:4).',
        'historical_figures': [
            {'name': 'C.S. Lewis', 'position': 'In The Screwtape Letters and elsewhere, insisted on the reality of the spiritual world against modern materialist dismissal.', 'orthodox': True},
            {'name': 'Walter Wink', 'position': 'Reinterpreted "principalities and powers" as sociopolitical structures rather than personal spiritual beings — a demythologizing move that contradicts the text.', 'orthodox': False},
            {'name': 'Gregory of Nyssa', 'position': 'Affirmed the reality and hierarchy of angelic beings as part of God\'s created order.', 'orthodox': True},
        ],
        'key_hebrew_greek': 'mal\'ak (מַלְאָךְ) — "messenger, angel." saraph (שָׂרָף) — "burning one" (Isa 6, the seraphim). keruv (כְּרוּב) — "cherub" (Gen 3:24, Ezek 1). sar (שַׂר) — "prince, ruler" (Dan 10:13, the territorial prince of Persia). kosmokratoras (κοσμοκράτορας) — "world rulers" of darkness (Eph 6:12). pneumatika tes ponerias (πνευματικὰ τῆς πονηρίας) — "spiritual forces of evil" in heavenly places.',
        'summary': 'The unseen realm is the operational theater of divine governance. It is populated with real beings in a real hierarchy, engaged in real conflict that shapes earthly events. The biblical worldview demands we take this realm as seriously as the physical world — not more, not less, but equally. Daniel 10 is the paradigm: prayer moves in the seen realm; warfare responds in the unseen.',
    },
    {
        'id': 'B08',
        'category': 'COSMOLOGY',
        'title': 'Time and Prophetic Pattern',
        'subtitle': 'God operates through typology, already/not-yet, and prophetic telescoping — history rhymes by design.',
        'key_texts': ['Ecclesiastes 1:9', '1 Corinthians 10:6,11', 'Hebrews 8:5', 'Romans 5:14', 'Isaiah 46:10'],
        'council_relevance': 'The council operates across time in patterned ways. God "declares the end from the beginning" (Isa 46:10) — not because history is random but because He authors it with intentional patterns. Typology is not human pattern-recognition imposed on the text; it is God\'s deliberate design: Adam is a typos of Christ (Rom 5:14), the tabernacle is a typos of heavenly reality (Heb 8:5), and OT events "happened as examples for us" (1 Cor 10:6).',
        'covenant_link': 'Each covenant recapitulates and advances the previous ones. The Passover foreshadows the cross. The Sinai theophany foreshadows Pentecost. The Davidic throne foreshadows Christ\'s reign. Typology is the mechanism by which covenants connect across time.',
        'eschatological_trajectory': 'The already/not-yet framework: the kingdom is inaugurated (already) but not consummated (not yet). D-Day has happened (the cross); V-Day is coming (the parousia). Prophetic telescoping compresses near and far fulfillments into single oracles (Isa 61:1-2, where Jesus stops reading mid-sentence in Luke 4:18-19).',
        'governance_tag': 'eschatological',
        'confidence': 'B',
        'orthodox_position': 'Biblical time is linear (not cyclical) but patterned. God embeds types, shadows, and prophetic patterns into history that find their fulfillment in Christ and the eschaton. The already/not-yet framework is essential: the kingdom is present but not yet fully realized. Prophetic telescoping means a single prophecy can have near and far fulfillments. These are features of divine authorship, not coincidences.',
        'historical_figures': [
            {'name': 'Oscar Cullmann', 'position': 'Articulated the D-Day/V-Day analogy for already/not-yet eschatology — the decisive battle is won, but the war continues until final victory.', 'orthodox': True},
            {'name': 'George Eldon Ladd', 'position': 'Developed inaugurated eschatology: the kingdom is "already" present in Christ but "not yet" consummated. Central to understanding the NT.', 'orthodox': True},
            {'name': 'C.I. Scofield', 'position': 'Rigid dispensationalism that over-separates Israel and the church and misses typological continuity. Correct on futurism, problematic on discontinuity.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'typos (τύπος) — "type, pattern, example" (Rom 5:14, 1 Cor 10:6). skia (σκιά) — "shadow" (Col 2:17, Heb 8:5) — OT realities are shadows of the heavenly substance. parousia (παρουσία) — "coming, arrival, presence" — the technical term for Christ\'s return. kairos (καιρός) — "appointed time, season" — God\'s strategic moments in history.',
        'summary': 'God governs history through deliberate patterns — types, shadows, and prophetic telescoping that connect events across millennia. The already/not-yet framework is the master key: the decisive victory is accomplished at the cross, but the full manifestation awaits the parousia. This is not coincidence but authorial intent — God writes history the way an author writes a novel, with foreshadowing that only makes sense in retrospect.',
    },

    # ══════════════════════════════════════════════════════════════
    # ANTHROPOLOGY — HUMANITY IN THE COUNCIL
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B09',
        'category': 'ANTHROPOLOGY',
        'title': 'Imago Dei — The Image of God',
        'subtitle': 'Humans bear God\'s image as His representatives — tselem means idol/statue, the king\'s image in his territory.',
        'key_texts': ['Genesis 1:26-28', 'Genesis 5:1-3', 'Psalm 8:4-6', '2 Corinthians 3:18', 'Colossians 3:10'],
        'council_relevance': 'Imago Dei is a governance concept, not primarily an ontological one. In the ancient Near East, a king placed his tselem (image/statue) in conquered territory to represent his authority. Humans are God\'s tselem — His authorized representatives on earth. Psalm 8:5 says humans were made "a little lower than the elohim" — placed in the council hierarchy just below the spiritual beings, with dominion over the earth. The image is functional: we are God\'s vice-regents.',
        'covenant_link': 'The dominion mandate of Gen 1:28 is the first covenant-like commission. Every subsequent covenant refines and restores what the image was meant to do: rule, steward, bless, and represent God.',
        'eschatological_trajectory': 'The image is being renewed in Christ (Col 3:10, 2 Cor 3:18). Full restoration at the resurrection when we bear the image of the heavenly man (1 Cor 15:49). Redeemed humanity rules in the new creation (Rev 22:5).',
        'governance_tag': 'creation_order',
        'confidence': 'A',
        'orthodox_position': 'Every human being bears the image of God. This is not a quality humans possess (like rationality or morality) but a status they hold — God\'s authorized representatives on earth. The image was marred by the fall but not destroyed (Gen 9:6 still applies post-fall). It is being restored in Christ and will be perfected at the resurrection.',
        'historical_figures': [
            {'name': 'Michael Heiser', 'position': 'Recovered the ANE background of tselem as a functional/representational concept — humans as God\'s "idol" (image-statue) in His cosmic temple.', 'orthodox': True},
            {'name': 'John Walton', 'position': 'Emphasized the functional rather than structural interpretation of the image — what humans DO (represent God) rather than what they ARE.', 'orthodox': True},
            {'name': 'Irenaeus of Lyon', 'position': 'Distinguished between image (tselem) and likeness (demut), seeing likeness as the spiritual dimension lost at the fall and restored in Christ.', 'orthodox': True},
        ],
        'key_hebrew_greek': 'tselem (צֶלֶם) — "image, statue, idol" — the same word used for pagan idols. God\'s "idol" is not made of stone but of flesh. demut (דְּמוּת) — "likeness, resemblance." radah (רָדָה) — "to rule, have dominion" — the function of the image. eikon (εἰκών) — Greek "image" (Col 1:15, Christ is THE image of God; 2 Cor 3:18, we are being transformed into the same image).',
        'summary': 'The imago Dei is the governance mandate of humanity — we are God\'s living statues placed in His cosmic temple (the earth) to represent His authority and extend His rule. This is not about intelligence or morality; it is about vocation. The fall corrupted the image, Christ perfectly embodies it, and the Spirit is restoring it in believers who will rule in the new creation.',
    },
    {
        'id': 'B10',
        'category': 'ANTHROPOLOGY',
        'title': 'Body, Soul, Spirit — The Human Constitution',
        'subtitle': 'Humans are embodied beings with immaterial dimensions — nephesh, ruach, basar — made for resurrection.',
        'key_texts': ['Genesis 2:7', '1 Thessalonians 5:23', 'Hebrews 4:12', 'Ecclesiastes 12:7', '2 Corinthians 5:1-8'],
        'council_relevance': 'The human constitution is designed for council participation. The body (basar) operates in the physical realm. The spirit (ruach) interfaces with the spiritual realm. The soul (nephesh) is the living self — the whole person animated by God\'s breath. Humans are the only beings designed to operate in BOTH realms simultaneously — unlike angels (spirit only) or animals (body only). This dual-realm nature is why humans can serve as God\'s representatives on earth while participating in heavenly realities.',
        'covenant_link': 'The body is the covenant\'s arena — circumcision marks the flesh (Abrahamic), the law governs bodily behavior (Mosaic), the Spirit indwells the body (New). Embodiment is not incidental to covenant life but central to it.',
        'eschatological_trajectory': 'Bodily resurrection — not escape from the body but its glorification (1 Cor 15:42-44). The intermediate state (2 Cor 5:8, absent from the body, present with the Lord) is temporary. The final state is embodied, glorified, and eternal.',
        'governance_tag': 'creation_order',
        'confidence': 'B',
        'orthodox_position': 'Humans are created as body-soul/spirit unities. Whether bipartite (body + soul/spirit) or tripartite (body + soul + spirit), the key truth is that embodiment is essential to human nature — not a prison to escape. The soul/spirit survives death (the intermediate state) but the final destiny is bodily resurrection. Gnostic body-hatred is heresy; biblical anthropology affirms the goodness of the body.',
        'historical_figures': [
            {'name': 'Thomas Aquinas', 'position': 'The soul is the "form" of the body — hylomorphic unity. Body and soul are not two substances but one being with material and immaterial aspects.', 'orthodox': True},
            {'name': 'Tertullian', 'position': 'Defended bodily resurrection against gnostic spiritualizers: "The flesh is the hinge of salvation."', 'orthodox': True},
            {'name': 'Apollinaris of Laodicea', 'position': 'Denied Christ had a human soul/mind (the Logos replaced it) — condemned at Constantinople 381 because it implies Christ was not fully human.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'nephesh (נֶפֶשׁ) — "soul, life, self, being" (Gen 2:7 — Adam became a "living nephesh"). ruach (רוּחַ) — "spirit, breath, wind" (Eccl 12:7 — the spirit returns to God). basar (בָּשָׂר) — "flesh, body." neshama (נְשָׁמָה) — "breath" (Gen 2:7 — God breathed the neshama of life). soma (σῶμα) — "body" (1 Cor 15:44, the "spiritual body" of the resurrection).',
        'summary': 'Humans are uniquely constituted for dual-realm operation — body in the physical world, spirit interfacing with the spiritual. This is why we can represent God on earth while participating in heavenly realities. The body is not a prison but a temple (1 Cor 6:19), and the final destiny is not disembodiment but glorified resurrection. Every gnostic impulse to denigrate the body must be resisted.',
    },
    {
        'id': 'B11',
        'category': 'ANTHROPOLOGY',
        'title': 'Human Purpose in the Council',
        'subtitle': 'Humans were made to rule — "a little lower than the elohim" with dominion over the works of God\'s hands.',
        'key_texts': ['Psalm 8:4-6', 'Genesis 1:28', 'Hebrews 2:5-9', '1 Corinthians 6:2-3', 'Revelation 22:5'],
        'council_relevance': 'Psalm 8:5 places humans in the council hierarchy: "You have made him a little lower than the elohim and crowned him with glory and honor." Hebrews 2:5-9 applies this to Christ and, through Christ, to redeemed humanity. The astonishing claim of 1 Cor 6:2-3 is that believers will judge angels — humans, once ranked below the elohim, will exercise judicial authority OVER them. This is the great reversal: the junior members of the council become its judges.',
        'covenant_link': 'The dominion mandate (Gen 1:28) is the original commission. Each covenant advances the restoration of this purpose: Abraham\'s seed blesses nations, the Mosaic priesthood mediates God\'s presence, the Davidic king rules, and the New Covenant Spirit empowers believers for the ultimate role — judging the cosmos.',
        'eschatological_trajectory': 'Redeemed humans reign forever (Rev 22:5). They judge angels (1 Cor 6:2-3). The purpose that was frustrated by the fall is not merely restored but elevated — humanity\'s eschatological destiny exceeds its Edenic beginning.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'Humans were created to participate in God\'s governance of creation. We are members of the divine council — the junior members at present, but destined for a role that surpasses even the angels (Heb 2:5 — "it was not to angels that God subjected the world to come"). Psalm 8 is the charter: crowned with glory, given dominion, set over the works of God\'s hands.',
        'historical_figures': [
            {'name': 'Irenaeus of Lyon', 'position': 'Taught that humanity was created immature and destined to grow into its full destiny — the incarnation was always God\'s plan, not merely a response to the fall.', 'orthodox': True},
            {'name': 'Michael Heiser', 'position': 'Identified Psalm 8 as the key to human purpose within the divine council framework — humans ranked just below the elohim, destined to rule with God.', 'orthodox': True},
            {'name': 'Pelagius', 'position': 'Overemphasized human ability apart from grace — correct that humans have a high calling, wrong that they can achieve it by natural effort alone.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'me\'at (מְעַט) — "a little" (Ps 8:5, "a little lower than the elohim"). kavod ve-hadar (כָּבוֹד וְהָדָר) — "glory and honor/majesty" — royal language applied to humanity. radah (רָדָה) — "rule, have dominion." krinousin (κρινοῦσιν) — "will judge" (1 Cor 6:2, future tense — believers WILL judge the world and angels).',
        'summary': 'Humanity\'s purpose is governance — we were made to rule as God\'s representatives, ranked just below the spiritual beings in the council hierarchy. The fall interrupted this purpose; redemption restores and elevates it. The staggering claim of Scripture is that redeemed humans will judge angels and reign forever — the junior members of the council inherit the highest administrative role.',
    },
    {
        'id': 'B12',
        'category': 'ANTHROPOLOGY',
        'title': 'Male and Female — Complementary Image-Bearing',
        'subtitle': 'God created humanity as male and female — both bearing the image, with complementary roles in the dominion mandate.',
        'key_texts': ['Genesis 1:27', 'Genesis 2:18-24', '1 Corinthians 11:3,7-12', 'Ephesians 5:22-33', 'Galatians 3:28'],
        'council_relevance': 'The male-female distinction is embedded in the image-bearing mandate. Genesis 1:27 is emphatic: "male and female He created them" — the image is fully expressed only in the complementary pair. The dominion mandate (Gen 1:28) is given to BOTH together: "Be fruitful and multiply and fill the earth and subdue it." Neither bears the image alone; neither exercises dominion alone. The marriage relationship itself images the covenant relationship between God and His people (Eph 5:32).',
        'covenant_link': 'Marriage is the first covenant-like institution (Gen 2:24). The husband-wife relationship is the primary metaphor for God-Israel (Hosea) and Christ-church (Eph 5). The covenant is not gender-neutral — the roles are complementary and meaningful.',
        'eschatological_trajectory': 'In the resurrection, "they neither marry nor are given in marriage" (Matt 22:30) — the temporary institution gives way to the eternal reality it pointed to (the marriage supper of the Lamb, Rev 19:7-9).',
        'governance_tag': 'creation_order',
        'confidence': 'A',
        'orthodox_position': 'God created humanity as male and female — two sexes, complementary in nature and role, both fully bearing the image of God. Male headship in the family and church is a creation-order principle (1 Cor 11:3, 1 Tim 2:12-13), not a product of the fall. Equality of essence coexists with distinction of role — as in the Trinity itself (the Son submits to the Father without being less divine).',
        'historical_figures': [
            {'name': 'John Chrysostom', 'position': 'Affirmed complementary roles while insisting on the equal dignity of women — the head-body metaphor implies mutual dependence, not superiority.', 'orthodox': True},
            {'name': 'Wayne Grudem', 'position': 'Defended complementarianism from the text: male headship is pre-fall (1 Tim 2:13 grounds it in creation order, not cultural convention).', 'orthodox': True},
            {'name': 'Egalitarians (various)', 'position': 'Argue that all role distinctions are products of the fall and are abolished in Christ (Gal 3:28). This misreads Gal 3:28, which addresses salvific status, not role differentiation.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'zakar (זָכָר) — "male." neqevah (נְקֵבָה) — "female." ezer kenegdo (עֵזֶר כְּנֶגְדּוֹ) — "helper corresponding to him" (Gen 2:18) — ezer is used of God Himself (Ps 33:20), not a subordinate term. echad basar (אֶחָד בָּשָׂר) — "one flesh" (Gen 2:24). kephale (κεφαλή) — "head" (1 Cor 11:3, Eph 5:23) — debated meaning, but contextually denotes authority/source.',
        'summary': 'Male and female together constitute the full image of God, with complementary roles in the dominion mandate. This is creation-order design, not cultural artifact. The marriage relationship images the covenant between God and His people, making it a governance institution as much as a personal one. Equality of dignity coexists with distinction of function — the same pattern seen in the Trinity.',
    },

    # ══════════════════════════════════════════════════════════════
    # COSMIC REBELLION — THE THREE REBELLIONS
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B13',
        'category': 'COSMIC_REBELLION',
        'title': 'The Edenic Rebellion — The Nachash',
        'subtitle': 'The serpent of Eden was a divine being, not a talking snake — a member of the council who led the first cosmic rebellion.',
        'key_texts': ['Genesis 3:1-15', 'Ezekiel 28:12-17', 'Isaiah 14:12-15', 'Revelation 12:9', '2 Corinthians 11:3'],
        'council_relevance': 'The nachash (serpent) of Genesis 3 is identified in Ezekiel 28 as a divine being — "the anointed cherub who covers" (keruv mimshach ha-sokek), who was "in Eden, the garden of God," adorned with precious stones, "blameless from the day you were created until unrighteousness was found in you." This is a council member. Isaiah 14:13 reveals the motive: "I will ascend to heaven; I will raise my throne above the stars of God; I will sit on the mount of assembly" (har mo\'ed — the council mountain). The first rebellion was a coup attempt within the council itself.',
        'covenant_link': 'The protoevangelium (Gen 3:15) is the first covenant promise — the Seed of the Woman will crush the serpent\'s head. Every subsequent covenant advances this promise toward its fulfillment in Christ.',
        'eschatological_trajectory': 'The ancient serpent is identified as Satan in Rev 12:9. He is bound for 1,000 years (Rev 20:2), then cast into the lake of fire forever (Rev 20:10). The Genesis 3:15 head-crushing is accomplished at the cross and consummated at the eschaton.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'The serpent of Eden was not a mere animal but a divine being — the nachash, a shining/brilliant creature of the council who rebelled against Yahweh and seduced humanity into rebellion. Ezekiel 28 and Isaiah 14 provide the backstory. The Hebrew nachash can mean "serpent" but also "shining one" (from the verbal root meaning "to shine, to practice divination"). This was the first of three great cosmic rebellions that fractured God\'s governance order.',
        'historical_figures': [
            {'name': 'Michael Heiser', 'position': 'Demonstrated that nachash in Gen 3 is best understood as a divine throne-room guardian (cf. Ezek 28) who initiated the first cosmic rebellion within the council.', 'orthodox': True},
            {'name': 'Origen of Alexandria', 'position': 'Connected Isaiah 14 and Ezekiel 28 to the fall of Satan, establishing the traditional Christian reading of these passages as describing a pre-fall angelic rebellion.', 'orthodox': True},
            {'name': 'Modern critical scholars', 'position': 'Deny any connection between Gen 3, Isa 14, and Ezek 28 — treating each as isolated, non-supernatural texts. This atomistic reading ignores the canonical intertextuality that Revelation 12:9 makes explicit.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'nachash (נָחָשׁ) — "serpent" but also related to "shining one" (nachash as adjective = bronze/bright). keruv mimshach ha-sokek (כְּרוּב מִמְשַׁח הַסּוֹכֵךְ) — "anointed guardian cherub" (Ezek 28:14). helel ben-shachar (הֵילֵל בֶּן שָׁחַר) — "shining one, son of dawn" (Isa 14:12). ophis ho archaios (ὁ ὄφις ὁ ἀρχαῖος) — "the ancient serpent" (Rev 12:9).',
        'summary': 'The Edenic rebellion was not a conversation between a woman and a talking animal. It was the first cosmic insurrection — a divine council member seducing God\'s image-bearers into treason. The nachash was a shining guardian cherub who attempted to overthrow the governance order from within. This rebellion fractured the human-divine relationship and set in motion the entire redemptive narrative.',
    },
    {
        'id': 'B14',
        'category': 'COSMIC_REBELLION',
        'title': 'The Watcher Rebellion — Bene Ha\'Elohim of Genesis 6',
        'subtitle': 'Divine beings ("sons of God") abandoned their proper domain, took human wives, and produced the Nephilim.',
        'key_texts': ['Genesis 6:1-4', 'Jude 6-7', '2 Peter 2:4-5', '1 Enoch 6-16', 'Job 1:6'],
        'council_relevance': 'The bene ha\'elohim of Genesis 6:1-4 are divine council members — the same phrase used in Job 1:6, 2:1, and 38:7 for supernatural beings in Yahweh\'s presence. These beings "left their proper dwelling" (Jude 6) and transgressed the boundary between the spiritual and physical realms by taking human wives. The result was the Nephilim — hybrid offspring that violated the creation-order boundaries God established. This is the SECOND great rebellion: not a coup attempt (like Eden) but a boundary violation — council members abandoning their assigned domain.',
        'covenant_link': 'The Flood (Noahic covenant context) was God\'s response to the Watcher corruption. The Noahic covenant restarts creation after the contamination. The imprisoned Watchers (2 Pet 2:4, Jude 6) await final judgment.',
        'eschatological_trajectory': 'The Watchers are imprisoned in Tartarus (2 Pet 2:4) until the great day of judgment (Jude 6). Their final sentence is part of the cosmic reckoning when all rebellious spiritual powers are judged.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'The "sons of God" in Genesis 6:1-4 are divine beings (angels/Watchers), not the "godly line of Seth." This is the unanimous view of pre-Christian Judaism (1 Enoch, Jubilees, the Dead Sea Scrolls), the view of Jude and Peter (who treat it as historical fact), and the only reading that makes sense of the Hebrew phrase bene ha\'elohim as used throughout the OT. The Sethite interpretation is a post-Augustinian invention with no support in Second Temple Judaism or the NT authors.',
        'historical_figures': [
            {'name': 'Justin Martyr', 'position': 'Affirmed the angelic interpretation of Gen 6:1-4, following the universal early church reading.', 'orthodox': True},
            {'name': 'Augustine of Hippo', 'position': 'Proposed the Sethite interpretation (sons of God = godly line of Seth) largely to counter pagan mockery. This reading became dominant in the West but has no Second Temple support.', 'orthodox': False},
            {'name': 'Michael Heiser', 'position': 'Demonstrated that the supernatural reading is the only one consistent with the Hebrew phrase bene ha\'elohim and the Second Temple context of Jude and 2 Peter.', 'orthodox': True},
        ],
        'key_hebrew_greek': 'bene ha\'elohim (בְּנֵי הָאֱלֹהִים) — "sons of God" — divine council members (Job 1:6, 2:1, 38:7). Nephilim (נְפִילִים) — "fallen ones" or "giants" — the offspring of the illicit union. Watchers (עִירִין, irin) — the Aramaic term in Daniel 4:13,17 for divine beings; in 1 Enoch, the specific group that fell. tartaroo (ταρταρόω) — "cast into Tartarus" (2 Pet 2:4) — a prison beneath the underworld for the worst offenders.',
        'summary': 'The Watcher rebellion is the second great cosmic insurrection — divine council members who violated the creator-creature boundary by entering the human realm sexually, producing the Nephilim. This was not the "godly line of Seth" marrying unbelievers; it was a supernatural transgression that corrupted humanity so severely that God responded with the Flood. Jude 6 and 2 Peter 2:4 confirm the supernatural reading as the apostolic position.',
    },
    {
        'id': 'B15',
        'category': 'COSMIC_REBELLION',
        'title': 'The Babel Rebellion — Deuteronomy 32 Worldview',
        'subtitle': 'At Babel, God disinherited the nations and allotted them to lesser elohim — keeping only Israel for Himself.',
        'key_texts': ['Genesis 11:1-9', 'Deuteronomy 32:8-9', 'Deuteronomy 4:19-20', 'Psalm 82:1-8', 'Acts 17:26-27'],
        'council_relevance': 'This is the THIRD and most governance-altering rebellion. At Babel, humanity united in rebellion (Gen 11). God\'s response was not merely linguistic confusion but a cosmic restructuring: He allotted the nations to the "sons of God" (bene elohim, Deut 32:8 DSS/LXX) and kept Israel as His own inheritance (Deut 32:9). The allotted elohim then became corrupt (Ps 82) — they were supposed to govern justly but instead accepted worship and led the nations astray (Deut 4:19-20). Psalm 82 is the covenant lawsuit against these corrupt administrators: "I said, \'You are gods,\' but you will die like men."',
        'covenant_link': 'The Abrahamic covenant (Gen 12, immediately after Babel in Gen 11) is God\'s direct response: through Abraham\'s seed, He will reclaim ALL nations. The Babel disinheritance is reversed at Pentecost (Acts 2) when the nations hear the gospel in their own tongues — Babel undone.',
        'eschatological_trajectory': 'Psalm 82:8 — "Rise up, O God, judge the earth, for you shall inherit all the nations." The disinheritance is temporary. At the eschaton, God reclaims every nation, and the corrupt elohim are judged. Revelation 7:9 — every nation, tribe, tongue gathered before the throne.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'At Babel, God divided the nations and allotted them to subordinate divine beings (Deut 32:8 in the Dead Sea Scrolls and LXX reads "sons of God," not "sons of Israel" as in the Masoretic Text). These elohim were given administrative authority over the nations but became corrupt — accepting worship, perverting justice, and leading the nations into idolatry. Psalm 82 is their indictment. The Abrahamic covenant is God\'s plan to reclaim what was lost at Babel.',
        'historical_figures': [
            {'name': 'Michael Heiser', 'position': 'Made the Deuteronomy 32 worldview accessible: the Babel event was a cosmic disinheritance, and the Abrahamic covenant is the response. This is the backbone of biblical theology.', 'orthodox': True},
            {'name': 'Paul the Apostle', 'position': 'In Acts 17:26-27, references the Babel allotment: God "made from one man every nation... having determined allotted periods and the boundaries of their dwelling place, that they should seek God."', 'orthodox': True},
            {'name': 'Liberal critical scholars', 'position': 'Treat Deut 32:8-9 as evidence of Israelite henotheism (worship of one god while acknowledging others) evolving toward monotheism. This misreads the text: Yahweh is not one god among equals; He is the Most High who ASSIGNS the other gods their jurisdictions.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'bene elohim (בְּנֵי אֱלֹהִים) — "sons of God" (Deut 32:8, DSS 4QDeut-j). nachalah (נַחֲלָה) — "inheritance, allotment" (Deut 32:9, Israel is Yahweh\'s nachalah). Elyon (עֶלְיוֹן) — "Most High" (Deut 32:8, the God who distributes). gevulot ammim (גְּבֻלֹת עַמִּים) — "borders/boundaries of the peoples" — set according to the number of the divine beings.',
        'summary': 'The Babel event was not just a language miracle — it was a cosmic governance restructuring. God disinherited the rebellious nations and assigned them to subordinate elohim who subsequently became corrupt. He then chose one man, Abraham, through whose seed He would reclaim all nations. This is the Deuteronomy 32 worldview — the backbone of the entire biblical storyline from Genesis 11 to Revelation 7.',
    },
    {
        'id': 'B16',
        'category': 'COSMIC_REBELLION',
        'title': 'The Origin of Demons — Disembodied Nephilim',
        'subtitle': 'Demons are the disembodied spirits of the dead Nephilim — not fallen angels, not mere metaphors.',
        'key_texts': ['1 Enoch 15:8-12', 'Genesis 6:1-4', 'Mark 5:1-13', 'Luke 11:24-26', 'Matthew 12:43-45'],
        'council_relevance': 'The divine council framework distinguishes between categories of spiritual beings that systematic theology often conflates. Fallen angels (the Watchers) are imprisoned (2 Pet 2:4, Jude 6). The satan/nachash operates as a distinct entity (the original rebel). Demons (daimonia) are a THIRD category — the disembodied spirits of the Nephilim, who were the hybrid offspring of the Watcher-human unions. 1 Enoch 15:8-12 explains: because the Nephilim were born of flesh but fathered by spirits, their spirits — upon physical death — became "evil spirits on the earth," roaming, seeking embodiment. This explains why demons seek bodies (Mark 5, Luke 11) while angels do not.',
        'covenant_link': 'The Flood destroyed the Nephilim\'s bodies, releasing their spirits as demons. The Noahic covenant re-established order, but the demonic infestation persists until the eschaton. Christ\'s exorcisms are kingdom-of-God demonstrations (Matt 12:28).',
        'eschatological_trajectory': 'Demons are subject to Christ\'s authority (Luke 10:17-20) and will be finally dealt with at the judgment. The lake of fire is prepared "for the devil and his angels" (Matt 25:41). The complete cleansing of creation removes all demonic presence.',
        'governance_tag': 'council',
        'confidence': 'C',
        'orthodox_position': 'Demons are best understood as the disembodied spirits of the dead Nephilim — a view held universally in Second Temple Judaism (1 Enoch 15:8-12, Jubilees 10:1-9) and consistent with NT data. This explains key observations: why demons are distinct from fallen angels (who are imprisoned), why demons desperately seek embodiment (they once had bodies), and why exorcism is a kingdom act (reclaiming territory from illegitimate occupants). The confidence is C because the NT never explicitly states this origin, but the Second Temple background the NT authors assumed makes it the best available explanation.',
        'historical_figures': [
            {'name': 'The author of 1 Enoch', 'position': 'Explicitly identifies demons as the spirits of the dead giants/Nephilim (15:8-12), providing the dominant Second Temple explanation for demonic activity.', 'orthodox': True},
            {'name': 'Justin Martyr', 'position': 'Followed the Enochic tradition: demons are the offspring of the fallen angels, explaining their restless, body-seeking behavior.', 'orthodox': True},
            {'name': 'Modern systematic theologians', 'position': 'Typically equate demons with fallen angels — a conflation that ignores the Second Temple distinctions the NT authors assumed and creates exegetical problems (e.g., why are fallen angels imprisoned while demons roam free?).', 'orthodox': False},
        ],
        'key_hebrew_greek': 'daimonion (δαιμόνιον) — "demon" (NT). pneuma akatharton (πνεῦμα ἀκάθαρτον) — "unclean spirit" (Mark 5:2). shedim (שֵׁדִים) — "demons" (Deut 32:17, Ps 106:37) — associated with the nations\' false worship. Rephaim (רְפָאִים) — "shades, dead ones" — sometimes connected to the Nephilim (Gen 14:5, Isa 26:14). The Nephilim-demon connection: 1 Enoch 15:9 — "the spirits of the giants afflict, oppress, destroy, attack, do battle, and work destruction on the earth."',
        'summary': 'Demons are not fallen angels (who are imprisoned) or metaphors for psychological illness. They are the disembodied spirits of the Nephilim — beings born of flesh and spirit who, when their bodies perished in the Flood, became restless spirits seeking embodiment. This Second Temple understanding was the assumed background of the NT authors and explains the distinctive behavior of demons throughout the Gospels.',
    },

    # ══════════════════════════════════════════════════════════════
    # COVENANT — THE GOVERNANCE BACKBONE
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B17',
        'category': 'COVENANT',
        'title': 'The Noahic Covenant — Cosmic Stability',
        'subtitle': 'God binds Himself to never again destroy the earth by flood — the platform of cosmic stability for all that follows.',
        'key_texts': ['Genesis 8:20-9:17', 'Isaiah 54:9-10', 'Jeremiah 33:20-21', '2 Peter 3:5-7'],
        'council_relevance': 'The Noahic covenant is God re-establishing governance after the Watcher catastrophe. The Flood was a de-creation event (the waters of the deep returning, Gen 7:11), and the Noahic covenant is a re-creation charter. God promises cosmic stability — the seasons, seedtime and harvest, day and night will continue (Gen 8:22). This is not merely about weather; it is about the reliable framework within which all subsequent covenants and governance will operate. The rainbow (qeshet — also a war-bow) is God\'s sign that He has hung up His weapon.',
        'covenant_link': 'Foundation covenant — without cosmic stability, no other covenant can function. The Noahic covenant is universal (all creation), unconditional, and everlasting. It is the platform on which Abrahamic, Mosaic, Davidic, and New covenants are built.',
        'eschatological_trajectory': 'The Noahic promise holds until the final judgment by fire (2 Pet 3:7). Isaiah 54:9-10 links the Noahic stability to the New Covenant: "As I swore that the waters of Noah should no more go over the earth, so I have sworn that I will not be angry with you."',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'The Noahic covenant is a real, historical, unconditional covenant between God and all creation (humans, animals, and the earth itself). It guarantees cosmic stability until the final eschatological judgment. The Flood was a global, catastrophic event — not a regional flood or myth. The covenant sign (rainbow) is God\'s perpetual reminder of His commitment to the platform on which all redemptive history unfolds.',
        'historical_figures': [
            {'name': 'Noah', 'position': 'The covenant recipient — "a righteous man, blameless in his generation" (Gen 6:9) — who obeyed God in building the ark and received the post-Flood covenant.', 'orthodox': True},
            {'name': 'Peter the Apostle', 'position': 'Treats the Flood as historical fact and typological foreshadowing of final judgment (2 Pet 3:5-7) and baptism (1 Pet 3:20-21).', 'orthodox': True},
            {'name': 'Modern flood-deniers', 'position': 'Treat the Flood narrative as myth or local event — contradicting both the Genesis text and the NT authors\' explicit affirmation of its historicity.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'berit (בְּרִית) — "covenant" — first used in the Bible here (Gen 6:18, pre-Flood promise; Gen 9:9-17, formal establishment). qeshet (קֶשֶׁת) — "bow" (rainbow) — the same word used for a war-bow. God hangs up His weapon of judgment. ot (אוֹת) — "sign" — the rainbow as covenant sign. olam (עוֹלָם) — "everlasting" — the Noahic covenant has no expiration.',
        'summary': 'The Noahic covenant is the governance platform — God\'s guarantee of cosmic stability after the Flood\'s de-creation. Without this foundation, no subsequent covenant could operate. It is universal (all creation), unconditional (no human obligations), and everlasting (until the final fire). The rainbow is God\'s war-bow hung up in the sky — a permanent sign that He will not again unmake what He has made.',
    },
    {
        'id': 'B18',
        'category': 'COVENANT',
        'title': 'The Abrahamic Covenant — Land, Seed, Blessing',
        'subtitle': 'God\'s response to Babel — through one man\'s seed, all disinherited nations will be reclaimed.',
        'key_texts': ['Genesis 12:1-3', 'Genesis 15:1-21', 'Genesis 17:1-14', 'Galatians 3:8,16', 'Romans 4:13-17'],
        'council_relevance': 'The Abrahamic covenant is God\'s strategic countermove to the Babel disinheritance. After allotting the nations to corrupt elohim (Deut 32:8), God calls one man from Ur and promises: through your seed, all nations (the disinherited families of the earth) will be blessed (Gen 12:3). This is a reconquest plan — reclaiming the nations from the corrupt elohim through covenant, not through force. The three promises (land, seed, blessing) address the three dimensions of the Babel loss: territory, people, and relationship with God.',
        'covenant_link': 'Backbone covenant — the Mosaic, Davidic, and New covenants all build on Abrahamic foundations. The land promise is fulfilled initially in Joshua, ultimately in the new creation. The seed promise culminates in Christ (Gal 3:16). The blessing promise is universal and ongoing.',
        'eschatological_trajectory': 'The land promise is not exhausted by the conquest of Canaan — it extends to the whole earth (Rom 4:13 — Abraham as "heir of the world"). The seed is Christ. The blessing reaches every nation (Rev 7:9). The Abrahamic covenant is fully realized only in the new creation.',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'The Abrahamic covenant is unconditional (God alone passes between the pieces in Gen 15), historical (Abraham was a real person), and ongoing (the promises are not yet fully fulfilled). The seed promise is singular — Christ (Gal 3:16). The land promise extends to the whole earth through the Messiah. The blessing promise is being fulfilled as the gospel goes to all nations. This covenant is the hinge of redemptive history — God\'s answer to Babel.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Identified the singular "seed" as Christ (Gal 3:16) and the Abrahamic blessing as the gospel preached in advance (Gal 3:8).', 'orthodox': True},
            {'name': 'Abraham', 'position': 'The covenant recipient — "believed God and it was counted to him as righteousness" (Gen 15:6). The paradigm of faith.', 'orthodox': True},
            {'name': 'Dispensationalist extremes', 'position': 'Some hyper-dispensational readings so rigidly separate Israel and the church that they miss the Abrahamic covenant\'s universal scope — "all families of the earth" includes Gentile believers.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'berit ben ha-betarim (בְּרִית בֵּין הַבְּתָרִים) — "covenant between the pieces" (Gen 15) — God alone walks through, making it unconditional. zera (זֶרַע) — "seed" (singular in Gal 3:16 = Christ). berakah (בְּרָכָה) — "blessing." goy gadol (גּוֹי גָּדוֹל) — "great nation." The Abrahamic triad: erets (land), zera (seed), berakah (blessing).',
        'summary': 'The Abrahamic covenant is God\'s answer to Babel. After disinheriting the nations and allotting them to elohim who became corrupt, God launches a reconquest through covenant: one man, one family, one nation — and through that line, a Seed who will bless ALL nations. This is not one covenant among many; it is THE covenant that drives the entire biblical narrative from Genesis 12 to Revelation 22.',
    },
    {
        'id': 'B19',
        'category': 'COVENANT',
        'title': 'The Mosaic/Sinai Covenant — Theocratic Constitution',
        'subtitle': 'Israel\'s covenant at Sinai follows the ANE suzerainty treaty format — God as Great King, Israel as vassal nation.',
        'key_texts': ['Exodus 19:3-6', 'Exodus 20:1-17', 'Deuteronomy 28-30', 'Jeremiah 31:31-32', 'Galatians 3:19-25'],
        'council_relevance': 'The Sinai covenant constitutes Israel as a "kingdom of priests and a holy nation" (Exod 19:6) — a nation designed to function as God\'s council representatives on earth. The covenant follows the ANE suzerainty treaty format: preamble (Exod 20:2a — "I am Yahweh your God"), historical prologue (20:2b — "who brought you out of Egypt"), stipulations (the laws), blessings and curses (Deut 28), and witnesses (heaven and earth, Deut 30:19). The prophetic riv (covenant lawsuit) is a council prosecution: the prophet stands in the sod YHWH (Jer 23:18) and delivers the charges to the covenant-breaking nation.',
        'covenant_link': 'Built on the Abrahamic foundation (Exod 2:24 — "God remembered His covenant with Abraham"). The Mosaic covenant is conditional (blessings for obedience, curses for disobedience) while the Abrahamic remains unconditional. The Mosaic covenant reveals sin (Rom 3:20, Gal 3:19) and points to the need for a New Covenant (Jer 31:31-34).',
        'eschatological_trajectory': 'The Mosaic covenant is fulfilled in Christ (Matt 5:17) and superseded by the New Covenant (Heb 8:13). The law served as a guardian/tutor (paidagogos) until Christ came (Gal 3:24-25). The priestly-kingdom vocation of Exod 19:6 is taken up by the church (1 Pet 2:9) and fully realized in the new creation (Rev 5:10).',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'The Sinai covenant is a real, historical covenant given at a real mountain, in a real suzerainty treaty format. It constituted Israel as God\'s theocratic nation — a kingdom of priests mediating His presence to the world. The law is good, holy, and righteous (Rom 7:12), but it cannot save — it reveals sin and points to Christ. The covenant curses (Deut 28) were fulfilled in the exile, and the ultimate curse-bearing was accomplished by Christ on the cross (Gal 3:13).',
        'historical_figures': [
            {'name': 'Moses', 'position': 'The covenant mediator — stood between God and Israel at Sinai, received the Torah, interceded for the people after the golden calf.', 'orthodox': True},
            {'name': 'George Mendenhall', 'position': 'Demonstrated the structural parallels between the Sinai covenant and Hittite suzerainty treaties — confirming the covenant\'s ANE legal background.', 'orthodox': True},
            {'name': 'Marcion of Sinope', 'position': 'Rejected the Mosaic law and the OT God entirely — a heresy that severs the NT from its covenantal roots.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'torah (תּוֹרָה) — "instruction, law" — not mere legislation but divine instruction for covenant life. berit (בְּרִית) — "covenant." riv (רִיב) — "covenant lawsuit" — the prophetic prosecution of covenant violations. mamlekhet kohanim (מַמְלֶכֶת כֹּהֲנִים) — "kingdom of priests" (Exod 19:6). paidagogos (παιδαγωγός) — "guardian, tutor" (Gal 3:24) — the law\'s role until Christ came.',
        'summary': 'The Sinai covenant is Israel\'s theocratic constitution — a suzerainty treaty between the Great King (Yahweh) and His vassal nation (Israel). It established the priestly-kingdom mandate, the sacrificial system, and the prophetic office. The covenant is good but unable to save — it diagnoses the disease (sin) and points to the cure (Christ). The prophetic riv lawsuit and the covenant curses are council enforcement mechanisms.',
    },
    {
        'id': 'B20',
        'category': 'COVENANT',
        'title': 'The Davidic Covenant — Eternal Throne',
        'subtitle': 'God promises David an eternal dynasty and throne — the Son who will reign forever and be called God\'s Son.',
        'key_texts': ['2 Samuel 7:12-16', 'Psalm 2:6-7', 'Psalm 89:3-4', 'Psalm 110:1', 'Luke 1:32-33'],
        'council_relevance': 'The Davidic covenant installs a human king on Yahweh\'s throne — the most explicit merging of human and divine governance. Psalm 2 places the Davidic king in council language: "I have set My King on Zion, My holy hill" (v.6), "You are My Son" (v.7 — divine council sonship language), "Ask of Me, and I will give you the nations as Your inheritance" (v.8 — reversing the Babel disinheritance). Psalm 110 places two Lords together: "Yahweh said to my lord, \'Sit at My right hand\'" — a human king sharing the divine throne. Jesus identified this as the key Christological text (Matt 22:41-46).',
        'covenant_link': 'Advances the Abrahamic "seed" promise — the line narrows to David\'s house. The Davidic king is the covenant administrator who will bless the nations. The "Son of God" language (2 Sam 7:14, Ps 2:7) is adopted into the New Covenant\'s Christology.',
        'eschatological_trajectory': 'Christ is the ultimate Davidic king — currently reigning at the Father\'s right hand (Acts 2:30-36), to be fully manifest at the parousia (Rev 19:11-16). "He will reign over the house of Jacob forever, and of His kingdom there will be no end" (Luke 1:33).',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'The Davidic covenant is unconditional (2 Sam 7:15 — "My steadfast love will not depart from him") and eternal (the throne endures forever). Jesus is the Son of David who fulfills every promise: the eternal king, the Son of God, the one who inherits the nations. His reign began at the ascension (Acts 2:30-36) and will be consummated at His return.',
        'historical_figures': [
            {'name': 'David', 'position': 'The covenant recipient — "a man after God\'s own heart" (1 Sam 13:14), whose throne is established forever by divine promise.', 'orthodox': True},
            {'name': 'Peter the Apostle', 'position': 'At Pentecost, declared that the Davidic covenant was fulfilled in Christ\'s resurrection and enthronement (Acts 2:30-36).', 'orthodox': True},
            {'name': 'Jewish messianic expectation', 'position': 'Expected a political Davidic king who would overthrow Rome — correct on the Davidic identity, incomplete on the two-stage fulfillment (first coming = suffering, second = reign).', 'orthodox': False},
        ],
        'key_hebrew_greek': 'bayit (בַּיִת) — "house/dynasty." kissei (כִּסֵּא) — "throne." ben (בֵּן) — "son" (2 Sam 7:14 — "I will be his Father, and he will be My son"). mashiach (מָשִׁיחַ) — "anointed one" — the Davidic king is the anointed. Christos (Χριστός) — the Greek equivalent. ne\'um YHWH la\'adoni (נְאֻם יהוה לַאדֹנִי) — "Yahweh says to my Lord" (Ps 110:1).',
        'summary': 'The Davidic covenant places a human king on God\'s throne — the ultimate expression of delegated governance. Psalm 2 and Psalm 110 frame the Davidic king in divine council language: sonship, enthronement, inheritance of the nations. Jesus is the fulfillment — David\'s son who is also David\'s Lord, currently reigning and awaiting the full consummation of His kingdom.',
    },
    {
        'id': 'B21',
        'category': 'COVENANT',
        'title': 'The New Covenant — Internalized Law, Spirit Indwelling, Babel Reversal',
        'subtitle': 'The covenant Jeremiah promised: law on the heart, direct knowledge of God, total forgiveness, and the Spirit poured out.',
        'key_texts': ['Jeremiah 31:31-34', 'Ezekiel 36:26-27', 'Hebrews 8:8-13', 'Acts 2:1-21', '2 Corinthians 3:6'],
        'council_relevance': 'The New Covenant reconstitutes the human side of the divine council. Where the Mosaic covenant relied on external law and mediated access (through priests), the New Covenant internalizes the law (Jer 31:33 — "I will write it on their hearts") and gives direct access (Jer 31:34 — "they shall all know Me"). The Spirit indwelling (Ezek 36:27) makes every believer a "temple" — a point of heaven-earth intersection. Pentecost (Acts 2) is the Babel reversal: where God scattered nations and confused languages, now the Spirit unifies nations and enables communication. The divine council is being repopulated with Spirit-empowered human agents.',
        'covenant_link': 'Fulfills the Abrahamic promise of blessing to all nations. Supersedes the Mosaic covenant (Heb 8:13) while fulfilling its intent. Establishes the Davidic king (Christ) as mediator. Rests on the Noahic platform of cosmic stability.',
        'eschatological_trajectory': 'The New Covenant is inaugurated but not yet consummated. The Spirit is the "guarantee" (arrabon, Eph 1:14) of the full inheritance. Complete fulfillment comes when "they shall all know Me" is universal (Hab 2:14) and the law is perfectly internalized in resurrection bodies.',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'The New Covenant is the definitive covenant — mediated by Christ\'s blood (Luke 22:20), prophesied by Jeremiah and Ezekiel, inaugurated at the cross and Pentecost. It provides what the Mosaic covenant could not: internal transformation (new heart), direct knowledge of God (without priestly mediation), complete forgiveness (not annual atonement), and the indwelling Spirit (God\'s presence in every believer). It is better in every way (Heb 8:6) because it is mediated by a better priest (Christ) with a better sacrifice (His own blood).',
        'historical_figures': [
            {'name': 'Jeremiah', 'position': 'Prophesied the New Covenant (31:31-34) during the darkest hour of the Mosaic covenant\'s failure — the Babylonian destruction.', 'orthodox': True},
            {'name': 'Jesus of Nazareth', 'position': 'Inaugurated the New Covenant at the Last Supper: "This cup is the new covenant in My blood" (Luke 22:20).', 'orthodox': True},
            {'name': 'Dispensationalist extremes', 'position': 'Some argue the New Covenant is exclusively for ethnic Israel and the church participates only by analogy. This ignores Hebrews 8-10, which explicitly applies Jeremiah 31 to the church.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'berit chadashah (בְּרִית חֲדָשָׁה) — "new covenant" (Jer 31:31). lev chadash (לֵב חָדָשׁ) — "new heart" (Ezek 36:26). ruach chadashah (רוּחַ חֲדָשָׁה) — "new spirit" (Ezek 36:26). arrabon (ἀρραβών) — "guarantee, down payment" (Eph 1:14, 2 Cor 1:22) — the Spirit as the first installment of the full inheritance. diatheke (διαθήκη) — "covenant" (Heb 8:8, rendered from the LXX of Jer 31:31).',
        'summary': 'The New Covenant is the culmination of all God\'s covenant administration — internalizing the law, pouring out the Spirit, providing complete forgiveness, and reversing Babel at Pentecost. It reconstitutes the human side of the divine council: every believer is a temple, every believer has direct access to God, and every believer is empowered by the Spirit for the council mandate. This is governance perfected — not external compliance but internal transformation.',
    },

    # ══════════════════════════════════════════════════════════════
    # MESSIAH & ATONEMENT — THE DIVINE RESCUE
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B22',
        'category': 'MESSIAH_ATONEMENT',
        'title': 'The Deity of Christ — The Son of Man Is Divine',
        'subtitle': 'Jesus is not a promoted human or a created angel — He is Yahweh incarnate, the second power in heaven.',
        'key_texts': ['John 1:1-14', 'Colossians 1:15-20', 'Daniel 7:13-14', 'Philippians 2:5-11', 'Hebrews 1:1-4'],
        'council_relevance': 'Daniel 7:13-14 is the key divine council Christology text. The "Son of Man" comes on the clouds (a divine prerogative in the OT — only Yahweh rides clouds, cf. Ps 104:3, Deut 33:26) and approaches the "Ancient of Days" — two enthroned divine figures. He receives "dominion, glory, and a kingdom, that all peoples, nations, and languages should serve Him." The Aramaic pelach ("serve/worship") is used elsewhere in Daniel only of service to God. This is the "two powers in heaven" motif: a second divine figure who shares Yahweh\'s throne, authority, and worship. John 1:1 confirms it: the Word was with God and was God. Colossians 1:16 — all things, including the council itself (thrones, dominions, rulers, authorities), were created by Him and for Him.',
        'covenant_link': 'Christ is the mediator of the New Covenant (Heb 9:15) and the fulfillment of the Abrahamic seed promise (Gal 3:16), the Davidic throne promise (Luke 1:32-33), and the prophesied "prophet like Moses" (Acts 3:22).',
        'eschatological_trajectory': 'Every knee bows to Jesus — in heaven, on earth, and under the earth (Phil 2:10-11). He is the Alpha and Omega, the First and the Last (Rev 1:17, 22:13) — titles belonging to Yahweh (Isa 44:6). The divine identity of Christ is the final revelation.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'Jesus Christ is fully God — co-eternal, co-equal with the Father, the second Person of the Trinity. He is not a created being (contra Arius), not an angel (contra JWs), not a mere human elevated to divinity (contra adoptionism). The OT prepares for this through the "two powers" motif: the Angel of Yahweh who IS Yahweh (Exod 3), the Son of Man who shares God\'s throne (Dan 7), the "Lord" of Psalm 110:1 whom David calls "my Lord." The NT declares it explicitly: "The Word was God" (John 1:1).',
        'historical_figures': [
            {'name': 'Athanasius of Alexandria', 'position': 'Champion of Nicaea — "the Son is of the same substance (homoousios) as the Father." The hill he was willing to die on, and right to be.', 'orthodox': True},
            {'name': 'Alan Segal', 'position': 'Demonstrated the "two powers in heaven" tradition in early Judaism — showing that the binitarian reading of the OT preceded Christianity (Two Powers in Heaven, 1977).', 'orthodox': True},
            {'name': 'Arius', 'position': 'Taught the Son was the first and greatest creature — "there was a time when the Son was not." Condemned at Nicaea (325 AD). The most dangerous Christological heresy in church history.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'bar enash (בַּר אֱנָשׁ) — "Son of Man" (Dan 7:13, Aramaic) — Jesus\' preferred self-designation. memra (מֵימְרָא) — "Word" (Aramaic Targums\' way of describing the second divine power). logos (λόγος) — "Word" (John 1:1). morphe theou (μορφῇ θεοῦ) — "form of God" (Phil 2:6) — Christ existing in the very nature/form of God. eikon tou theou tou aoratou (εἰκὼν τοῦ θεοῦ τοῦ ἀοράτου) — "image of the invisible God" (Col 1:15).',
        'summary': 'Christ\'s deity is not a later church invention — it is rooted in the OT "two powers in heaven" tradition and the divine council framework. Daniel 7\'s Son of Man receives universal worship alongside the Ancient of Days. Psalm 110\'s "Lord" sits at Yahweh\'s right hand. The NT authors identify Jesus as this second divine figure who created and sustains all things, including the council itself.',
    },
    {
        'id': 'B23',
        'category': 'MESSIAH_ATONEMENT',
        'title': 'The Humanity of Christ — The Seed of the Woman',
        'subtitle': 'Jesus is fully human — true incarnation, genuine temptation, real suffering — the last Adam who succeeds where the first failed.',
        'key_texts': ['Galatians 4:4', 'Hebrews 2:14-18', 'Hebrews 4:15', 'Romans 5:12-21', '1 Timothy 2:5'],
        'council_relevance': 'The incarnation is the supreme governance act — the Most High takes on the nature of His junior council members (humanity) to accomplish what they could not. Hebrews 2:14-18 makes the council logic explicit: "Since the children share in flesh and blood, He Himself likewise partook of the same things, that through death He might destroy the one who has the power of death." He had to become human to: (1) serve as the kinsman-redeemer (go\'el), (2) bear the covenant curse as a human representative, (3) recapitulate and reverse Adam\'s failure (Rom 5:12-21), and (4) serve as the eternal mediator between God and humanity (1 Tim 2:5).',
        'covenant_link': 'Christ is the "Seed of the Woman" (Gen 3:15), the Seed of Abraham (Gal 3:16), the Son of David (Matt 1:1). Every covenant line converges in His humanity. The incarnation is not incidental to the covenant plan — it is the covenant plan.',
        'eschatological_trajectory': 'The risen Christ remains incarnate forever — He ascended bodily (Acts 1:9-11) and will return bodily (Acts 1:11). Humanity is permanently joined to deity in the person of Christ. The incarnation is not temporary but eternal.',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'Jesus Christ is fully human — body, soul, and spirit. He was born of a woman (Gal 4:4), grew in wisdom (Luke 2:52), experienced hunger, thirst, fatigue, and sorrow. He was tempted in every way as we are, yet without sin (Heb 4:15). His humanity is not a disguise or a temporary costume — it is a genuine, permanent assumption of human nature. The incarnation means God has forever joined Himself to humanity.',
        'historical_figures': [
            {'name': 'Irenaeus of Lyon', 'position': 'Developed the "recapitulation" theory — Christ relives and reverses every stage of human failure, from infancy to death. The last Adam undoes the first.', 'orthodox': True},
            {'name': 'Cyril of Alexandria', 'position': 'Championed the hypostatic union at Ephesus (431) — one Person (the divine Son) with two complete natures (divine and human), without confusion or separation.', 'orthodox': True},
            {'name': 'Docetists', 'position': 'Taught that Christ only appeared to be human — His body was an illusion. This destroys the atonement: if He did not truly suffer, He did not truly bear our sins.', 'orthodox': False},
            {'name': 'Apollinaris', 'position': 'Denied Christ had a human mind/soul — the divine Logos replaced it. Condemned because "what is not assumed is not healed" (Gregory of Nazianzus).', 'orthodox': False},
        ],
        'key_hebrew_greek': 'zera ha\'ishah (זֶרַע הָאִשָּׁה) — "seed of the woman" (Gen 3:15) — the first Messianic promise, emphasizing human descent. go\'el (גֹּאֵל) — "kinsman-redeemer" — must be a blood relative to redeem (Ruth 3-4, applied to Christ). sarx (σάρξ) — "flesh" (John 1:14 — "the Word became flesh"). kenosis (κένωσις) — "emptying" (Phil 2:7 — He "emptied Himself, taking the form of a servant").',
        'summary': 'The incarnation is the supreme governance act — the Most High becoming the lowest to rescue from within. Christ is the last Adam who succeeds where the first failed, the kinsman-redeemer who must share our nature to redeem it, and the eternal mediator who joins God and humanity permanently. His humanity is not a temporary measure but a permanent reality — God is forever human in the person of Christ.',
    },
    {
        'id': 'B24',
        'category': 'MESSIAH_ATONEMENT',
        'title': 'Substitutionary Atonement — The Cross as Cosmic Victory',
        'subtitle': 'The cross is BOTH penal substitution AND Christus Victor — Christ bears the curse AND defeats the powers.',
        'key_texts': ['Isaiah 53:4-6', 'Romans 3:24-26', 'Colossians 2:13-15', '2 Corinthians 5:21', 'Hebrews 9:22-28'],
        'council_relevance': 'The cross is a dual-front victory: toward God (propitiation, satisfying justice) and toward the powers (Christus Victor, defeating the cosmic enemies). Colossians 2:13-15 is the cosmic-warfare text: Christ canceled the "record of debt" (cheirographon — the legal accusation the powers held against humanity), nailed it to the cross, and then "disarmed the rulers and authorities and put them to open shame, triumphing over them in it." The Greek thriambeusas is a Roman triumph — a military victory parade. The cosmic powers orchestrated the crucifixion (1 Cor 2:6-8) not realizing it was God\'s trap: the cross destroyed their legal basis for holding humanity captive.',
        'covenant_link': 'The cross is the ultimate covenant act: Christ bears the Mosaic covenant curse (Gal 3:13 — "cursed is everyone who hangs on a tree"), inaugurates the New Covenant in His blood (Luke 22:20), fulfills the Abrahamic blessing promise, and takes the Davidic throne through resurrection.',
        'eschatological_trajectory': 'The decisive battle is won (Col 2:15), but the war continues (Eph 6:12) until the consummation (Rev 20:10). Already/not yet: the powers are legally defeated but not yet fully removed. The cross is D-Day; the parousia is V-Day.',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'The atonement is multifaceted: penal substitution (Christ bore the penalty we deserved — Isa 53:5-6, Rom 3:25, 2 Cor 5:21), propitiation (satisfying God\'s righteous wrath — hilasterion, Rom 3:25), Christus Victor (defeating the cosmic powers — Col 2:15), and redemption (buying back the enslaved — apolutrosis, Rom 3:24). These are not competing theories but complementary facets of one event. The cross simultaneously settles the legal problem (guilt), the relational problem (enmity), and the cosmic problem (enslaving powers).',
        'historical_figures': [
            {'name': 'Anselm of Canterbury', 'position': 'Cur Deus Homo — articulated the satisfaction theory: sin is an infinite offense requiring infinite satisfaction, which only the God-man can provide.', 'orthodox': True},
            {'name': 'Gustaf Aulen', 'position': 'Recovered the Christus Victor motif in his 1931 book — the cross as cosmic military victory, the dominant patristic view.', 'orthodox': True},
            {'name': 'Faustus Socinus', 'position': 'Denied penal substitution entirely — God simply forgives without satisfaction. This makes the cross unnecessary and guts the gospel.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'kaphar (כָּפַר) — "to cover, atone, make propitiation." asham (אָשָׁם) — "guilt offering" (Isa 53:10). hilasterion (ἱλαστήριον) — "propitiation, mercy seat" (Rom 3:25 — Christ IS the mercy seat). cheirographon (χειρόγραφον) — "record of debt, certificate of indebtedness" (Col 2:14). thriambeusas (θριαμβεύσας) — "triumphing, leading in triumphal procession" (Col 2:15). apekdysamenos (ἀπεκδυσάμενος) — "having disarmed/stripped off" (Col 2:15, middle voice — stripping the powers off Himself).',
        'summary': 'The cross is the single most governance-dense event in history. It simultaneously satisfies divine justice (penal substitution), defeats the cosmic powers (Christus Victor), inaugurates the New Covenant, bears the Mosaic curse, fulfills the Abrahamic promise, and enthrones the Davidic king. The powers orchestrated the crucifixion not realizing it was their own destruction — God\'s "hidden wisdom" (1 Cor 2:7) that turned the enemy\'s weapon into the instrument of his defeat.',
    },
    {
        'id': 'B25',
        'category': 'MESSIAH_ATONEMENT',
        'title': 'Bodily Resurrection — Vindication and Firstfruits',
        'subtitle': 'Christ rose bodily from the dead — not metaphorically, not spiritually, but physically — and this changes everything.',
        'key_texts': ['1 Corinthians 15:1-8,20-23', 'Romans 1:4', 'Acts 2:24-32', 'Luke 24:36-43', 'Philippians 3:20-21'],
        'council_relevance': 'The resurrection is the divine council\'s vindication of the Messianic claim. Romans 1:4 — Christ was "declared to be the Son of God in power according to the Spirit of holiness by His resurrection from the dead." In council terms: the challenge brought by the nachash (Gen 3), the Watchers (Gen 6), and the corrupt elohim (Ps 82) is definitively answered. Death — the weapon of the cosmic powers — is defeated. Acts 2:24 — "God raised Him up, loosing the pangs of death, because it was not possible for Him to be held by it." The resurrection is the proof that the cross worked.',
        'covenant_link': 'The resurrection validates every covenant promise: the Seed lives (Gen 3:15, Gal 3:16), the throne endures (2 Sam 7:13, Acts 2:30-36), the New Covenant is ratified by a living mediator (Heb 7:25), and the blessing flows to all nations (Acts 2-28).',
        'eschatological_trajectory': 'Christ is the "firstfruits" (aparche) of the resurrection harvest (1 Cor 15:20-23). His resurrection guarantees ours. The final enemy, death, is destroyed (1 Cor 15:26). The resurrection body is the prototype of the new creation body — physical, glorified, imperishable.',
        'governance_tag': 'eschatological',
        'confidence': 'A',
        'orthodox_position': 'Jesus Christ rose bodily from the dead on the third day. The tomb was empty. He appeared physically to hundreds of witnesses (1 Cor 15:5-8). He ate fish (Luke 24:42-43), was touched (John 20:27), and was not a ghost (Luke 24:39). The resurrection is the foundation of Christianity — "if Christ has not been raised, your faith is futile" (1 Cor 15:17). It is not metaphor, spiritual experience, or group hallucination. It is a historical event that vindicates every claim Jesus made.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Staked everything on the resurrection (1 Cor 15:14-17) and listed eyewitnesses, including 500 at once, most of whom were still alive when he wrote.', 'orthodox': True},
            {'name': 'N.T. Wright', 'position': 'In The Resurrection of the Son of God, made the historical case: the empty tomb + the appearances + the origin of the church are best explained by actual resurrection.', 'orthodox': True},
            {'name': 'Rudolf Bultmann', 'position': 'Denied the bodily resurrection, claiming "a corpse cannot come back to life." Reduced the resurrection to the disciples\' subjective faith experience.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'anastasis (ἀνάστασις) — "resurrection, rising up" — a physical, bodily event. aparche (ἀπαρχή) — "firstfruits" (1 Cor 15:20) — the first sheaf of the harvest, guaranteeing the rest. egeiro (ἐγείρω) — "to raise up" (Rom 6:4, 1 Cor 15:4) — God the Father raised the Son. soma pneumatikon (σῶμα πνευματικόν) — "spiritual body" (1 Cor 15:44) — not immaterial, but a physical body animated and empowered by the Spirit.',
        'summary': 'The bodily resurrection of Christ is the divine council\'s vindication of the Messianic claim, the defeat of death (the cosmic powers\' ultimate weapon), and the firstfruits of the new creation. It is the proof that the cross accomplished what it was meant to accomplish and the guarantee that believers will share in the same resurrection. Without the resurrection, there is no Christianity, no hope, and no new creation.',
    },

    # ══════════════════════════════════════════════════════════════
    # SPIRIT — THE EMPOWERING PRESENCE
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B26',
        'category': 'SPIRIT',
        'title': 'The Person and Deity of the Holy Spirit',
        'subtitle': 'The Spirit is not an impersonal force but a divine Person — the ruach YHWH, the third Person of the Trinity.',
        'key_texts': ['Genesis 1:2', 'Isaiah 63:10', 'Acts 5:3-4', 'John 14:16-17,26', '1 Corinthians 2:10-11'],
        'council_relevance': 'The Spirit is the divine Person who operates most directly within the council\'s earthly operations. In the OT, the ruach YHWH empowers judges (Judg 3:10), prophets (Ezek 2:2), and kings (1 Sam 16:13) for their council roles. The Spirit gives access to God\'s own mind (1 Cor 2:10-11 — "the Spirit searches everything, even the depths of God"). He is the one who enables humans to participate in the divine council: revelation (prophetic insight), empowerment (gifts), and transformation (sanctification). He can be grieved (Eph 4:30), lied to (Acts 5:3), and resisted (Acts 7:51) — attributes of a person, not a force.',
        'covenant_link': 'The Spirit is the agent of the New Covenant\'s internalization (Ezek 36:27 — "I will put My Spirit within you"). He writes the law on hearts (Jer 31:33 via 2 Cor 3:3). He is the arrabon (guarantee/down payment) of the full covenant inheritance (Eph 1:14).',
        'eschatological_trajectory': 'The Spirit\'s current indwelling is the "firstfruits" (Rom 8:23) of the full redemption to come. At the resurrection, the Spirit who raised Christ will give life to our mortal bodies (Rom 8:11). The Spirit and the Bride say "Come!" (Rev 22:17).',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'The Holy Spirit is the third Person of the Trinity — fully God, co-eternal and co-equal with the Father and the Son. He is a Person (with intellect, will, and emotions), not an impersonal force or energy (contra Jehovah\'s Witnesses, Unitarians). Acts 5:3-4 equates lying to the Spirit with lying to God. He proceeds from the Father (John 15:26) and is sent by the Son (John 16:7). He is the executive agent of the Godhead — the one who implements the Father\'s will and applies the Son\'s work.',
        'historical_figures': [
            {'name': 'Basil of Caesarea', 'position': 'Wrote On the Holy Spirit (375 AD), defending the Spirit\'s full deity and personhood against the Pneumatomachians ("Spirit-fighters") who denied it.', 'orthodox': True},
            {'name': 'Gregory of Nazianzus', 'position': 'Called the Spirit "God" explicitly in Oration 31, completing the Trinitarian theology: Father, Son, and Spirit are equally God.', 'orthodox': True},
            {'name': 'Macedonius I', 'position': 'Led the Pneumatomachians who accepted the Son\'s deity but denied the Spirit\'s — condemned at Constantinople (381 AD).', 'orthodox': False},
        ],
        'key_hebrew_greek': 'ruach YHWH (רוּחַ יהוה) — "Spirit of Yahweh." ruach ha-qodesh (רוּחַ הַקֹּדֶשׁ) — "Spirit of Holiness / Holy Spirit." parakletos (παράκλητος) — "Helper, Advocate, Counselor" (John 14:16). pneuma tes aletheias (πνεῦμα τῆς ἀληθείας) — "Spirit of truth" (John 14:17). arrabon (ἀρραβών) — "guarantee, pledge" (Eph 1:14).',
        'summary': 'The Holy Spirit is the divine Person who makes the council accessible to humans. He empowers for service, illuminates truth, convicts of sin, and transforms believers into the image of Christ. He is not an impersonal force but a Person who can be grieved, lied to, and resisted. As the executive agent of the Godhead, He implements the Father\'s plan and applies the Son\'s accomplished work to believers.',
    },
    {
        'id': 'B27',
        'category': 'SPIRIT',
        'title': 'Spiritual Gifts — Empowerment for the Council Mandate',
        'subtitle': 'The charismata are not for personal edification alone but for equipping the church to fulfill its cosmic mandate.',
        'key_texts': ['1 Corinthians 12:4-11', '1 Corinthians 14:1-5', 'Ephesians 4:11-13', 'Romans 12:6-8', '1 Peter 4:10-11'],
        'council_relevance': 'Spiritual gifts are the Spirit\'s distribution of council-function capabilities to the church. In the OT, only specific individuals received the Spirit for specific tasks (prophets, kings, craftsmen). In the New Covenant, EVERY believer is gifted (1 Cor 12:7 — "to each is given the manifestation of the Spirit"). This is the democratization of council participation. The gift list in Eph 4:11 (apostles, prophets, evangelists, pastors, teachers) mirrors council roles: revelation (prophets), governance (pastors/elders), proclamation (evangelists), instruction (teachers). The purpose: "to equip the saints for the work of ministry" (Eph 4:12) — building the body to maturity for its cosmic role.',
        'covenant_link': 'Spiritual gifts are a New Covenant phenomenon — the outpouring of the Spirit that Joel prophesied (Joel 2:28-29, Acts 2:17-18). The Mosaic covenant concentrated gifting in offices; the New Covenant distributes it to all believers.',
        'eschatological_trajectory': 'Gifts are partial and temporary: "when the perfect comes, the partial will pass away" (1 Cor 13:10). They serve the church during the already/not-yet period. At the consummation, direct knowledge replaces prophetic glimpses, and the gifts give way to the full reality they pointed to.',
        'governance_tag': 'council',
        'confidence': 'B',
        'orthodox_position': 'Spiritual gifts are real, active, and given to every believer by the Holy Spirit. They are not limited to the apostolic era (cessationism overreaches the textual evidence) nor are they signs of superior spirituality (the Corinthian error). They are functional empowerments for the church\'s mission — building the body and advancing the kingdom. The gift of prophecy is to be especially desired (1 Cor 14:1) because it brings direct revelation for the community.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Provided the definitive teaching on gifts: distributed by the Spirit (1 Cor 12), governed by love (1 Cor 13), ordered for edification (1 Cor 14).', 'orthodox': True},
            {'name': 'John Chrysostom', 'position': 'While acknowledging the gifts, observed their apparent decline in the post-apostolic era — an early voice in the cessationist trajectory.', 'orthodox': True},
            {'name': 'B.B. Warfield', 'position': 'Argued for cessationism — miraculous gifts ceased with the apostles. This position lacks explicit biblical support and contradicts 1 Cor 13:8-10\'s eschatological timeframe.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'charismata (χαρίσματα) — "grace-gifts" (1 Cor 12:4). pneumatika (πνευματικά) — "spiritual things/gifts" (1 Cor 12:1). phanerosis tou pneumatos (φανέρωσις τοῦ πνεύματος) — "manifestation of the Spirit" (1 Cor 12:7). propheteuo (προφητεύω) — "to prophesy" (1 Cor 14:1) — the gift Paul singles out as most desirable. oikodomeo (οἰκοδομέω) — "to build up, edify" — the purpose of all gifts.',
        'summary': 'Spiritual gifts are the Spirit\'s distribution of council capabilities to every believer — the democratization of what was formerly reserved for select individuals. They are not for personal display but for building the body toward maturity and equipping it for its cosmic mandate. The church that neglects or suppresses the gifts is a council operating at reduced capacity.',
    },
    {
        'id': 'B28',
        'category': 'SPIRIT',
        'title': 'Indwelling and Filling — The Believer as Temple',
        'subtitle': 'Every believer is a temple of the Holy Spirit — a point of heaven-earth intersection, a portable Eden.',
        'key_texts': ['1 Corinthians 6:19-20', '1 Corinthians 3:16', 'Ephesians 5:18', 'Acts 2:1-4', 'John 7:37-39'],
        'council_relevance': 'The indwelling of the Spirit makes every believer a point of heaven-earth intersection — what the tabernacle and temple were for Israel. In the OT, God\'s presence was localized (Eden, the tabernacle, the temple). In the New Covenant, God\'s presence is distributed to every believer through the Spirit. This is the reconstitution of the council\'s earthly operations: instead of one temple in one city, there are millions of temples (believers) spread across every nation. Pentecost (Acts 2) is the Babel reversal: where God scattered and confused, now the Spirit gathers and unifies. The tongues of fire are the visible sign that each believer is a "burning bush" — a place where God\'s presence dwells.',
        'covenant_link': 'The Spirit\'s indwelling IS the New Covenant promise fulfilled: "I will put My Spirit within you" (Ezek 36:27). The arrabon (guarantee/down payment) of Eph 1:14 means the Spirit\'s current presence is the first installment of the full inheritance.',
        'eschatological_trajectory': 'The Spirit\'s indwelling is the firstfruits (Rom 8:23) — a foretaste of the full redemption when God\'s presence fills all creation (Rev 21:3 — "the dwelling place of God is with man"). The temple becomes cosmic.',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'Every genuine believer is indwelt by the Holy Spirit from the moment of faith (Rom 8:9 — "if anyone does not have the Spirit of Christ, he does not belong to Him"). Indwelling is permanent and universal for believers. Filling (Eph 5:18) is the experiential, ongoing, and variable reality — believers can grieve the Spirit (Eph 4:30) and quench the Spirit (1 Thess 5:19), which diminishes the filling without removing the indwelling. The filling is the empowerment; the indwelling is the permanent residence.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Established the body-as-temple theology (1 Cor 6:19) and distinguished between indwelling (permanent, all believers) and filling (commanded, ongoing — Eph 5:18).', 'orthodox': True},
            {'name': 'John Owen', 'position': 'Wrote extensively on the Spirit\'s indwelling and communion with believers — the Puritan gold standard for pneumatology.', 'orthodox': True},
            {'name': 'Watchman Nee', 'position': 'Overemphasized the tripartite nature (body/soul/spirit) to the point of suggesting the soul is inherently opposed to the spirit — a near-gnostic tendency.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'naos (ναός) — "temple, sanctuary" (1 Cor 6:19) — the inner sanctuary where God dwells, not the outer structure (hieron). pleroo (πληρόω) — "to fill" (Eph 5:18 — "be filled with the Spirit"). oikeo (οἰκέω) — "to dwell, inhabit" (Rom 8:9,11 — the Spirit "dwells in you"). arrabon (ἀρραβών) — "guarantee, pledge, down payment" (Eph 1:14, 2 Cor 1:22).',
        'summary': 'The Spirit\'s indwelling makes every believer a temple — a point of heaven-earth intersection. This is the cosmic upgrade from the Old Covenant (one temple, one city) to the New (millions of temples, every nation). Pentecost reversed Babel: where God scattered and confused, the Spirit now gathers and empowers. The believer\'s body is not a prison but a sanctuary — the most sacred space in the cosmos after the heavenly throne room.',
    },

    # ══════════════════════════════════════════════════════════════
    # CHURCH AS COUNCIL — THE COSMIC ANNOUNCEMENT
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B29',
        'category': 'CHURCH_COUNCIL',
        'title': 'The Church as Cosmic Announcement',
        'subtitle': 'The church exists to display God\'s wisdom to the cosmic powers — Ephesians 3:10 is the church\'s mission statement.',
        'key_texts': ['Ephesians 3:10-11', 'Ephesians 1:20-23', '1 Peter 2:9', 'Matthew 16:18', 'Colossians 1:18'],
        'council_relevance': 'Ephesians 3:10 is the most council-dense ecclesiology verse in the NT: "so that through the church the manifold wisdom of God might now be made known to the rulers and authorities in the heavenly places." The church\'s PRIMARY audience is not the world — it is the cosmic powers. The church is God\'s demonstration project: a redeemed humanity, drawn from every nation (reversing Babel), filled with the Spirit (reversing the Watcher transgression), and united under Christ the head (reversing the Edenic rebellion). The very existence of the church is an announcement to the powers that their rebellion has failed.',
        'covenant_link': 'The church is the New Covenant community — the "kingdom of priests" that Israel was called to be (Exod 19:6, 1 Pet 2:9). The church inherits and universalizes Israel\'s covenant vocation.',
        'eschatological_trajectory': 'The church is the eschatological community — the already/not-yet people of God. She is the Bride being prepared for the marriage supper of the Lamb (Rev 19:7-9). Her final destiny is to reign with Christ in the new creation (Rev 22:5).',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'The church is not a human institution or social club — it is the cosmic body of Christ, chosen before the foundation of the world (Eph 1:4), purchased with His blood (Acts 20:28), and tasked with making God\'s wisdom known to the spiritual powers. The gates of hell will not prevail against it (Matt 16:18). It is composed of all genuine believers from every nation, tribe, and tongue — the Babel reversal in progress.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Revealed the "mystery" of the church: Jew and Gentile united in one body, displaying God\'s wisdom to the cosmic powers (Eph 3:1-12).', 'orthodox': True},
            {'name': 'Dietrich Bonhoeffer', 'position': 'Insisted the church is "Christ existing as community" — not an organization but the living presence of Christ in the world.', 'orthodox': True},
            {'name': 'Liberal ecclesiology', 'position': 'Reduces the church to a social justice organization or moral community, stripping it of its cosmic dimension and supernatural mandate.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'ekklesia (ἐκκλησία) — "assembly, called-out ones" — in the LXX, used for Israel\'s assembly (qahal). The church IS the new assembly of God\'s people. soma Christou (σῶμα Χριστοῦ) — "body of Christ" (Eph 1:23, Col 1:18). polupoikilos sophia (πολυποίκιλος σοφία) — "manifold/multi-faceted wisdom" (Eph 3:10) — the church displays the full spectrum of God\'s wisdom. archai kai exousiai (ἀρχαὶ καὶ ἐξουσίαι) — "rulers and authorities" (Eph 3:10) — the cosmic powers who are the audience.',
        'summary': 'The church\'s primary mission is cosmic — displaying God\'s manifold wisdom to the spiritual powers. Every time Jew and Gentile worship together, every time the redeemed gather in Christ\'s name, it is an announcement to the principalities that their rebellion has failed. The church is the reconstituted council — humanity restored to its intended role as God\'s representatives, now empowered by the Spirit and united under Christ.',
    },
    {
        'id': 'B30',
        'category': 'CHURCH_COUNCIL',
        'title': 'Believers Judge Angels — The Great Reversal',
        'subtitle': 'Redeemed humans will judge the very beings who once governed the nations — the divine council inversion.',
        'key_texts': ['1 Corinthians 6:2-3', 'Psalm 82:1-8', 'Revelation 3:21', 'Daniel 7:18,27', 'Matthew 19:28'],
        'council_relevance': 'This is the climax of the governance narrative. 1 Corinthians 6:2-3 — "Do you not know that the saints will judge the world? Do you not know that we will judge angels?" This is the Psalm 82 reversal: the elohim who were appointed to govern the nations but became corrupt (Ps 82:2-5) are sentenced to "die like men" (Ps 82:7), and their judicial role is transferred to redeemed humanity. Daniel 7:18,27 — "the saints of the Most High shall receive the kingdom and possess the kingdom forever." Revelation 3:21 — "The one who conquers, I will grant to sit with Me on My throne." Humans, once the junior members of the council, become its judges.',
        'covenant_link': 'This is the ultimate fulfillment of the dominion mandate (Gen 1:28), the priestly-kingdom vocation (Exod 19:6), and the Davidic throne promise (ruling with Christ). Every covenant was building toward this moment.',
        'eschatological_trajectory': 'This is the eschatological endpoint of human purpose — redeemed humanity judging angels and reigning with Christ forever. The "already" is the church\'s current spiritual authority (Eph 2:6, seated with Christ in heavenly places). The "not yet" is the full judicial authority at the final judgment.',
        'governance_tag': 'eschatological',
        'confidence': 'A',
        'orthodox_position': 'Redeemed humanity will exercise judicial authority over angels. This is not metaphor — Paul states it as established fact and uses it as the basis for a practical argument (if you will judge angels, you should be able to settle disputes among yourselves). The saints receive the kingdom (Dan 7:18,27), sit on Christ\'s throne (Rev 3:21), and judge both the world and angels (1 Cor 6:2-3). This is the great reversal: beings once ranked below the elohim now judge them.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Stated the fact casually — "Do you not know?" — implying this was common Christian teaching, not a new revelation.', 'orthodox': True},
            {'name': 'Michael Heiser', 'position': 'Connected 1 Cor 6:2-3 to the Psalm 82 divine council framework: the corrupt elohim lose their roles, and redeemed humans inherit them.', 'orthodox': True},
            {'name': 'Amillennialists who spiritualize', 'position': 'Some reduce this to metaphorical "participation in Christ\'s authority" without actual judicial function. The text resists this — Paul\'s argument requires a literal judicial role.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'krinousin (κρινοῦσιν) — "will judge" (1 Cor 6:2, future indicative — a statement of fact, not a possibility). qadishei elyon (קַדִּישֵׁי עֶלְיוֹנִין) — "saints of the Most High" (Dan 7:18,27, Aramaic) — the ones who receive the everlasting kingdom. nikao (νικάω) — "to conquer, overcome" (Rev 3:21) — the condition for sharing Christ\'s throne. thronos (θρόνος) — "throne" (Rev 3:21, Matt 19:28).',
        'summary': 'The divine council narrative reaches its climax in the great reversal: redeemed humans, once ranked below the elohim, will judge the very beings who governed (and corrupted) the nations. This is the Psalm 82 inversion — the corrupt administrators are removed, and the saints of the Most High inherit the kingdom forever. Every covenant, every act of redemption, every work of the Spirit was building toward this moment.',
    },
    {
        'id': 'B31',
        'category': 'CHURCH_COUNCIL',
        'title': 'The Lord\'s Supper and Baptism — Covenant Signs',
        'subtitle': 'Baptism and the Lord\'s Supper are not mere rituals but covenant participation acts with cosmic significance.',
        'key_texts': ['Luke 22:19-20', '1 Corinthians 11:23-26', 'Romans 6:3-5', 'Matthew 28:19', '1 Corinthians 10:16-21'],
        'council_relevance': 'Paul connects the Lord\'s Supper directly to the cosmic realm in 1 Corinthians 10:16-21: participation in the cup and bread is "participation" (koinonia) in Christ\'s blood and body — and this is contrasted with pagan sacrificial meals that are "fellowship with demons" (10:20). The table is a council meal: in the ANE, covenant meals ratified treaties and established loyalty. The Lord\'s Supper is the ongoing covenant meal of the new community — a repeated declaration of allegiance to the true King. Baptism in Christ\'s name (Matt 28:19) is public identification with the covenant community — the visible transfer of allegiance from the old order to the new.',
        'covenant_link': 'The Lord\'s Supper is explicitly covenantal: "This cup is the new covenant in My blood" (Luke 22:20). Baptism enacts the covenant transition: dying with Christ and rising to new life (Rom 6:3-5). Both are covenant signs, parallel to circumcision (Col 2:11-12) and the Passover meal.',
        'eschatological_trajectory': 'The Lord\'s Supper "proclaims the Lord\'s death until He comes" (1 Cor 11:26) — an already/not-yet act pointing to the marriage supper of the Lamb (Rev 19:9). Baptism anticipates the final resurrection. Both ordinances bridge the present age and the age to come.',
        'governance_tag': 'covenant',
        'confidence': 'A',
        'orthodox_position': 'Baptism and the Lord\'s Supper are ordained by Christ, commanded for all believers, and serve as covenant signs of the New Covenant community. They are not optional, not merely symbolic, and not magic. They are means of grace — real participation in Christ\'s death and resurrection (baptism) and real communion with Christ\'s body and blood (the Supper). The cosmic dimension is explicit in 1 Cor 10:16-21: the table declares loyalty in a cosmos where other tables (demonic) compete for allegiance.',
        'historical_figures': [
            {'name': 'Jesus of Nazareth', 'position': 'Instituted both: the Supper at the Last Passover (Luke 22:19-20), baptism in the Great Commission (Matt 28:19).', 'orthodox': True},
            {'name': 'John Calvin', 'position': 'Taught "spiritual real presence" — Christ is truly present in the Supper by the Spirit, neither merely symbolically (Zwingli) nor physically in the elements (Rome).', 'orthodox': True},
            {'name': 'Ulrich Zwingli', 'position': 'Reduced the Supper to a bare memorial — "do this in remembrance" means only remembering, with no real participation. This contradicts Paul\'s koinonia language in 1 Cor 10:16.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'koinonia (κοινωνία) — "participation, fellowship, communion" (1 Cor 10:16) — real participation in Christ, not mere symbol. anamnesis (ἀνάμνησις) — "remembrance" (Luke 22:19, 1 Cor 11:24) — in the OT sense, an active re-presentation, not just mental recall. baptizo (βαπτίζω) — "to immerse, baptize" — death and resurrection enacted (Rom 6:3-5). diatheke (διαθήκη) — "covenant" (Luke 22:20 — "this cup is the new diatheke in My blood").',
        'summary': 'Baptism and the Lord\'s Supper are not empty rituals but covenant participation acts with cosmic dimensions. The Supper is a covenant meal declaring allegiance to Christ in a cosmos where demonic tables compete for loyalty. Baptism is the public transfer of allegiance — dying to the old order and rising in the new. Both are means of grace that connect the present community to the accomplished work of Christ and the coming consummation.',
    },

    # ══════════════════════════════════════════════════════════════
    # KINGDOM — AUTHORITY & WARFARE
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B32',
        'category': 'KINGDOM',
        'title': 'The Already and the Not Yet',
        'subtitle': 'The kingdom is inaugurated at the cross but not yet consummated — D-Day has happened, V-Day is coming.',
        'key_texts': ['Mark 1:14-15', 'Luke 17:20-21', 'Matthew 13:24-30,36-43', 'Romans 8:18-25', '1 Corinthians 15:24-28'],
        'council_relevance': 'The already/not-yet framework is the governance situation of the current age. Christ has been enthroned (Eph 1:20-22 — "seated at His right hand in the heavenly places, far above all rule and authority and power and dominion"). The powers are legally defeated (Col 2:15). But they have not yet been fully removed — they still operate, resist, and oppress (Eph 6:12). This is the D-Day/V-Day analogy: the decisive battle has been won (the cross), but enemy forces still fight (the church age), and the final surrender is coming (the parousia). The church operates in this tension — possessing real authority but in a contested environment.',
        'covenant_link': 'The New Covenant is inaugurated (Heb 8:13) but not fully consummated (Heb 8:11 — "they shall all know Me" is not yet universal). The Abrahamic "all nations blessed" is in progress. The Davidic reign is real but not fully manifest.',
        'eschatological_trajectory': 'The end comes when Christ "delivers the kingdom to God the Father after destroying every rule and every authority and power" (1 Cor 15:24). The last enemy is death (1 Cor 15:26). Then the Son Himself is subjected to the Father "that God may be all in all" (1 Cor 15:28).',
        'governance_tag': 'eschatological',
        'confidence': 'A',
        'orthodox_position': 'The kingdom of God is present and future. Jesus inaugurated it at His first coming (Mark 1:15 — "The kingdom of God is at hand"). It is growing like a mustard seed (Matt 13:31-32), operating like leaven (Matt 13:33), and coexisting with evil until the harvest (Matt 13:24-30). The error of over-realized eschatology (everything is accomplished now) is as dangerous as the error of pure futurism (nothing has happened yet). The already/not-yet framework holds both truths together.',
        'historical_figures': [
            {'name': 'Oscar Cullmann', 'position': 'Coined the D-Day/V-Day analogy: the decisive battle is won, but the war continues until final victory. The best illustration of already/not-yet eschatology.', 'orthodox': True},
            {'name': 'George Eldon Ladd', 'position': 'Developed inaugurated eschatology as the framework for understanding the Gospels: the kingdom is present in Christ\'s ministry but not yet fully realized.', 'orthodox': True},
            {'name': 'Hyper-preterists', 'position': 'Claim all prophecy was fulfilled by 70 AD — including the second coming, resurrection, and final judgment. This destroys the "not yet" and contradicts the creeds.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'basileia tou theou (βασιλεία τοῦ θεοῦ) — "kingdom of God" — not primarily a territory but God\'s reign/rule. engiken (ἤγγικεν) — "has come near, is at hand" (Mark 1:15). entos humon (ἐντὸς ὑμῶν) — "in your midst / within you" (Luke 17:21). parousia (παρουσία) — "coming, arrival" — the future consummation. telos (τέλος) — "end, goal" (1 Cor 15:24) — the eschatological endpoint.',
        'summary': 'The kingdom of God is the central governance reality of the current age — present but not complete, inaugurated but not consummated. Christ reigns now from the Father\'s right hand with all authority, but the defeated powers still operate in this contested period. The church lives in the tension between D-Day (accomplished) and V-Day (coming), exercising real authority in a real war that has a guaranteed outcome.',
    },
    {
        'id': 'B33',
        'category': 'KINGDOM',
        'title': 'Spiritual Warfare — Enforcing Accomplished Victory',
        'subtitle': 'The war is real, the enemy is defeated but active, and believers enforce what Christ has already won.',
        'key_texts': ['Ephesians 6:10-18', 'Daniel 10:12-13,20-21', '2 Corinthians 10:3-5', 'James 4:7', 'Revelation 12:11'],
        'council_relevance': 'Spiritual warfare is the operational reality of the already/not-yet kingdom. Ephesians 6:12 names the opponents: "rulers, authorities, cosmic powers of this present darkness, spiritual forces of evil in the heavenly places." These are council categories — the same archai kai exousiai of Colossians 1:16 and Ephesians 3:10. Daniel 10 provides the operational model: Daniel prays, a heavenly messenger is dispatched, the "prince of Persia" (a territorial spirit governing that region since Deut 32) resists for 21 days, and Michael intervenes. This reveals the mechanism: prayer engages the council, and the unseen war directly affects earthly events.',
        'covenant_link': 'Spiritual warfare is covenant enforcement. The armor of God (Eph 6:14-17) is covenant language: truth, righteousness, the gospel, faith, salvation, the word of God. The "sword of the Spirit" is the rhema of God — the covenant word deployed in spiritual combat (as Jesus used it against the satan in Matt 4).',
        'eschatological_trajectory': 'The war ends at the parousia. Revelation 19:11-21 describes the final battle. Revelation 20:10 records the final disposition. Until then, the church fights from victory (Christ\'s), not toward it.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'Spiritual warfare is real, not metaphorical. Believers face genuine opposition from organized supernatural powers who are legally defeated (Col 2:15) but operationally active (1 Pet 5:8). The believer\'s stance is defensive (Eph 6:11,13 — "stand," not "attack") and truth-based (the armor is truth, righteousness, gospel, faith, salvation, the Word). We do not fight FOR victory but FROM victory — enforcing what Christ has already accomplished. The Daniel 10 model shows that prayer is the primary mechanism of engagement.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Provided the definitive spiritual warfare teaching in Eph 6:10-18, naming the enemy categories and prescribing the covenant armor.', 'orthodox': True},
            {'name': 'Clinton Arnold', 'position': 'In Ephesians: Power and Magic, demonstrated that Paul\'s spiritual warfare language addressed real spiritual power structures in the Ephesian context — not mere metaphor.', 'orthodox': True},
            {'name': 'Walter Wink', 'position': 'Reinterpreted principalities and powers as sociopolitical systems — evacuating the text of its supernatural content.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'panoplia tou theou (πανοπλία τοῦ θεοῦ) — "full armor of God" (Eph 6:11). pale (πάλη) — "wrestling, struggle" (Eph 6:12) — hand-to-hand combat language. kosmokratoras (κοσμοκράτορας) — "world rulers" of this darkness (Eph 6:12). machaira tou pneumatos (μάχαιρα τοῦ πνεύματος) — "sword of the Spirit" (Eph 6:17) — the only offensive weapon in the armor. rhema theou (ῥῆμα θεοῦ) — "word of God" (Eph 6:17) — the specific, spoken word deployed in combat.',
        'summary': 'Spiritual warfare is the church\'s operational reality in the already/not-yet period. The enemy is identified (organized supernatural powers), the mechanism is revealed (prayer engages the council, as Daniel 10 shows), and the stance is defined (stand in Christ\'s accomplished victory, wearing the covenant armor). This is not metaphor for psychological struggle — it is real conflict with real beings in the real unseen realm, with real consequences for the visible world.',
    },
    {
        'id': 'B34',
        'category': 'KINGDOM',
        'title': 'The Authority of Believers — Delegated, Not Inherent',
        'subtitle': 'Believers have real authority in the spiritual realm — but it is Christ\'s authority delegated, not human power generated.',
        'key_texts': ['Luke 10:19', 'Matthew 28:18-20', 'Mark 16:17-18', 'Ephesians 2:6', 'Acts 3:6,16'],
        'council_relevance': 'The authority of believers is the current-age expression of the Psalm 8 destiny. Jesus delegates His own authority: "All authority in heaven and on earth has been given to Me. Go therefore..." (Matt 28:18-19). The "therefore" is critical — the Great Commission is grounded in Christ\'s total authority. Luke 10:19 — "I have given you authority to tread on serpents and scorpions and over all the power of the enemy." This is Genesis 3:15 language applied to disciples. Ephesians 2:6 places believers "seated with Christ in heavenly places" — a council position. The authority is real but derivative: "In the name of Jesus Christ" (Acts 3:6) — always in His name, never in our own.',
        'covenant_link': 'Delegated authority is the operating principle of every covenant (B04). The Great Commission extends the Abrahamic mandate ("all nations") through the New Covenant community, empowered by the Spirit (Acts 1:8).',
        'eschatological_trajectory': 'The current delegated authority is a foretaste of the full reign (Rev 22:5). The "seated with Christ" position (Eph 2:6) is the already; the "they will reign forever" (Rev 22:5) is the not yet.',
        'governance_tag': 'council',
        'confidence': 'A',
        'orthodox_position': 'Believers have genuine, delegated authority in the spiritual realm — authority to pray, to resist the devil (James 4:7), to proclaim the gospel, to make disciples, and to exercise spiritual gifts. This authority is always derivative (from Christ), always exercised in His name, and always subject to His will. It is not magic, not human willpower, and not a blank check. The abuses (name-it-and-claim-it theology, prosperity gospel) come from treating delegated authority as inherent power.',
        'historical_figures': [
            {'name': 'Jesus of Nazareth', 'position': 'The source of all delegated authority: "All authority has been given to Me" (Matt 28:18). He delegates what He possesses.', 'orthodox': True},
            {'name': 'Peter and John', 'position': 'Exercised delegated authority: "In the name of Jesus Christ of Nazareth, rise up and walk" (Acts 3:6). Always in His name, never their own.', 'orthodox': True},
            {'name': 'Word of Faith movement', 'position': 'Teaches believers have inherent creative power through their words — "little gods" theology. This confuses delegated authority with inherent divinity and approaches the nachash\'s original lie ("you will be like God").', 'orthodox': False},
        ],
        'key_hebrew_greek': 'exousia (ἐξουσία) — "authority, right, power" (Luke 10:19, Matt 28:18) — legitimate, delegated authority, not raw power (dunamis). en to onomati (ἐν τῷ ὀνόματι) — "in the name of" (Acts 3:6, 16) — acting as Christ\'s authorized representative. dunamis (δύναμις) — "power, ability" (Acts 1:8) — the Spirit\'s enabling power that makes the exercise of exousia effective.',
        'summary': 'Believers have real authority in the spiritual realm, but it is always delegated from Christ, exercised in His name, and subject to His will. The Great Commission grounds the church\'s mission in Christ\'s total authority — "all authority... therefore go." This is council delegation: the king sends agents who act in his name and with his authority. The abuses come when people mistake the ambassador\'s credentials for personal sovereignty.',
    },
    {
        'id': 'B35',
        'category': 'KINGDOM',
        'title': 'Prayer as Council Participation',
        'subtitle': 'Prayer is not talking to the ceiling — it is real-time participation in the divine council\'s operations.',
        'key_texts': ['Daniel 10:12-14', 'Revelation 5:8; 8:3-5', 'Matthew 6:9-13', 'James 5:16-18', 'Ephesians 6:18-20'],
        'council_relevance': 'Daniel 10 is the paradigm for prayer in the council framework. Daniel prays (10:2-3). God dispatches a messenger immediately (10:12 — "from the first day... your words were heard, and I have come because of your words"). The messenger is delayed 21 days by the "prince of Persia" — a territorial spirit — until Michael intervenes (10:13). The revelation is then delivered to Daniel (10:14ff). This reveals the mechanism: human prayer activates council operations. It is not wishful thinking — it moves beings, engages conflicts, and changes outcomes in the unseen realm. Revelation 5:8 and 8:3-5 show the prayers of the saints presented before the throne as incense, directly triggering angelic action on earth.',
        'covenant_link': 'The Lord\'s Prayer (Matt 6:9-13) is covenant prayer: "Our Father" (covenant relationship), "Your kingdom come" (covenant rule), "Your will be done on earth as in heaven" (council alignment), "forgive us our debts" (covenant faithfulness), "deliver us from evil/the evil one" (spiritual warfare).',
        'eschatological_trajectory': 'Prayer is the present-age mechanism by which believers participate in the council\'s work. In the new creation, when God dwells directly with His people (Rev 21:3), prayer as petition may be transcended by direct communion — the model becoming the reality.',
        'governance_tag': 'council',
        'confidence': 'B',
        'orthodox_position': 'Prayer is real participation in the operations of the divine council. It is not psychological self-talk, not empty ritual, and not merely "aligning our will with God\'s" (though it includes that). Daniel 10 demonstrates that prayer engages the unseen realm in real time with real consequences. Revelation 8:3-5 shows the prayers of the saints directly triggering theophanic action on earth. James 5:16 — "The effective prayer of a righteous person can accomplish much." Prayer is the primary means by which believers exercise their council role in the current age.',
        'historical_figures': [
            {'name': 'Daniel the Prophet', 'position': 'The paradigm of prayer as council participation — his 21-day prayer vigil engaged heavenly conflict and resulted in divine revelation.', 'orthodox': True},
            {'name': 'E.M. Bounds', 'position': 'Wrote extensively on prayer as real spiritual power: "God shapes the world by prayer. The more praying there is in the world, the better the world will be."', 'orthodox': True},
            {'name': 'Friedrich Schleiermacher', 'position': 'Reduced prayer to a subjective feeling of dependence — denying any objective, causal effect on the spiritual realm. This contradicts the entire biblical testimony.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'palal (פָּלַל) — "to pray, intercede" (hitpael form = reflexive, "to intercede on behalf of"). tephillah (תְּפִלָּה) — "prayer." proseuche (προσευχή) — "prayer" (Eph 6:18). thymiama (θυμίαμα) — "incense" (Rev 5:8, 8:3) — the prayers of the saints presented as incense before the throne. deesis (δέησις) — "petition, supplication" (Eph 6:18). enischuo (ἐνισχύω) — "to strengthen, empower" — the effective (energoumene) prayer of James 5:16.',
        'summary': 'Prayer is the mechanism by which believers participate in the divine council\'s operations during the already/not-yet period. Daniel 10 reveals the model: prayer activates heavenly response, engages spiritual conflict, and results in revelation and intervention. The Lord\'s Prayer is structured as a covenant prayer that aligns the believer with the council\'s priorities. Prayer is not optional for the church — it is the primary instrument of council participation.',
    },

    # ══════════════════════════════════════════════════════════════
    # RESTORATION — FINAL GOVERNANCE TRANSFER
    # ══════════════════════════════════════════════════════════════
    {
        'id': 'B36',
        'category': 'RESTORATION',
        'title': 'The Second Coming — Visible, Physical, Triumphant',
        'subtitle': 'Christ will return bodily, visibly, and in power — the same Jesus who ascended will return in the same way.',
        'key_texts': ['Acts 1:9-11', 'Matthew 24:30', 'Revelation 19:11-16', '1 Thessalonians 4:16-17', 'Zechariah 14:4'],
        'council_relevance': 'The parousia is the moment when the invisible reign becomes visible. Christ currently reigns from the Father\'s right hand (Eph 1:20-22), unseen by the world. At the second coming, the curtain between the seen and unseen realms is pulled back. Revelation 19:11-16 describes the divine warrior — riding a white horse, eyes like flame, a sharp sword from His mouth, on His robe the title "King of kings and Lord of lords." This is the final council session made public: the King who has been governing from the unseen realm steps into the visible world to consummate His victory.',
        'covenant_link': 'The parousia fulfills every covenant\'s eschatological promise: the Abrahamic land promise (the whole renewed earth), the Davidic throne (visible, universal reign), and the New Covenant\'s "all shall know Me" (Hab 2:14).',
        'eschatological_trajectory': 'THIS IS the eschatological event — the hinge between the already and the fully realized. Every unfulfilled promise, every "not yet," resolves at the parousia. The dead are raised, the living are transformed, the powers are judged, and the kingdom is consummated.',
        'governance_tag': 'eschatological',
        'confidence': 'A',
        'orthodox_position': 'Jesus Christ will return bodily, visibly, and personally. "This Jesus, who was taken up from you into heaven, will come in the same way as you saw Him go into heaven" (Acts 1:11). The second coming is not metaphorical, not gradual, and not a spiritual experience — it is an event. Every eye will see Him (Rev 1:7). He comes in glory with His angels (Matt 25:31). This is the non-negotiable hope of the church, affirmed in every historic creed.',
        'historical_figures': [
            {'name': 'The Apostolic Church', 'position': 'Maranatha ("Our Lord, come!") was the earliest Christian prayer (1 Cor 16:22) — the church was born expecting the imminent return.', 'orthodox': True},
            {'name': 'The Nicene Creed', 'position': '"He will come again in glory to judge the living and the dead, and His kingdom will have no end." The universal Christian confession.', 'orthodox': True},
            {'name': 'Full preterists', 'position': 'Claim the second coming already occurred in 70 AD (the destruction of Jerusalem). This denies the bodily, visible return and contradicts Acts 1:11 and the creeds.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'parousia (παρουσία) — "coming, arrival, presence" — the technical term for the second coming. apokalypsis (ἀποκάλυψις) — "revelation, unveiling" (1 Pet 1:7) — Christ revealed in glory. epiphaneia (ἐπιφάνεια) — "appearing, manifestation" (2 Tim 4:8). maranatha (μαράνα θά) — Aramaic, "Our Lord, come!" (1 Cor 16:22). erchomenos meta ton nephelon (ἐρχόμενος μετὰ τῶν νεφελῶν) — "coming with the clouds" (Rev 1:7, Dan 7:13) — divine prerogative language.',
        'summary': 'The second coming is the moment when the invisible governance becomes visible. Christ, who has been reigning from the Father\'s right hand since the ascension, will step into the visible world to consummate His kingdom. This is not metaphor, not gradual progress, and not a past event. It is the future, bodily, visible, triumphant return of the same Jesus who ascended — the event that resolves every "not yet" in one decisive moment.',
    },
    {
        'id': 'B37',
        'category': 'RESTORATION',
        'title': 'Bodily Resurrection of All — Not Soul Sleep, Not Annihilation',
        'subtitle': 'Every human who has ever lived will be raised bodily — some to eternal life, some to eternal judgment.',
        'key_texts': ['Daniel 12:2', 'John 5:28-29', '1 Corinthians 15:42-49', 'Revelation 20:11-15', 'Acts 24:15'],
        'council_relevance': 'The bodily resurrection of all is the final reassembly of the council\'s human constituency. Every person who has ever borne the image of God (B09) will stand before the throne. Daniel 12:2 states it plainly: "Many of those who sleep in the dust of the earth shall awake, some to everlasting life, and some to shame and everlasting contempt." John 5:28-29 universalizes it: "an hour is coming when all who are in the tombs will hear His voice and come out." The resurrection is the precondition for the final judgment and the final governance assignment.',
        'covenant_link': 'The resurrection is the ultimate covenant fulfillment: the body given in creation (Gen 2:7), marred by the fall (Gen 3:19 — "to dust you shall return"), redeemed by Christ\'s resurrection (1 Cor 15:20-23), and glorified at the final day.',
        'eschatological_trajectory': 'This IS the eschatological completion of God\'s work in the body. The intermediate state (soul in God\'s presence, awaiting the body) gives way to the final state (glorified soul IN a glorified body). 1 Corinthians 15:42-44 describes the transformation: sown perishable, raised imperishable; sown in dishonor, raised in glory; sown in weakness, raised in power; sown a natural body, raised a spiritual body.',
        'governance_tag': 'eschatological',
        'confidence': 'A',
        'orthodox_position': 'All the dead will be raised bodily — believers to eternal life, unbelievers to eternal judgment. The resurrection is physical, not metaphorical. Soul sleep (the dead are unconscious until the resurrection) contradicts Jesus\' words to the thief (Luke 23:43) and Paul\'s desire to "depart and be with Christ" (Phil 1:23). Annihilationism (the wicked are destroyed, not punished eternally) contradicts "everlasting contempt" (Dan 12:2) and "eternal punishment" (Matt 25:46). The intermediate state is real but temporary; the final state is embodied.',
        'historical_figures': [
            {'name': 'Paul the Apostle', 'position': 'Wrote the definitive resurrection chapter (1 Cor 15), defending bodily resurrection against both deniers and spiritualizers.', 'orthodox': True},
            {'name': 'Tertullian', 'position': 'Championed bodily resurrection against Gnostic spiritualizers: "The flesh is the hinge of salvation" (De Resurrectione Carnis).', 'orthodox': True},
            {'name': 'Seventh-Day Adventism', 'position': 'Teaches soul sleep — the dead are unconscious until the resurrection. While affirming bodily resurrection, this contradicts Paul\'s expectation of immediate conscious presence with Christ (2 Cor 5:8, Phil 1:23).', 'orthodox': False},
        ],
        'key_hebrew_greek': 'yaqitsu (יָקִיצוּ) — "shall awake" (Dan 12:2) — physical awakening from the "sleep" of death. anastasis (ἀνάστασις) — "resurrection" (John 5:29, Acts 24:15). soma pneumatikon (σῶμα πνευματικόν) — "spiritual body" (1 Cor 15:44) — not immaterial, but a body fully animated by the Spirit. aphtharsia (ἀφθαρσία) — "imperishability" (1 Cor 15:42) — the resurrection body does not decay.',
        'summary': 'The bodily resurrection of all humanity is the final governance act concerning the body: every image-bearer reassembled, every person standing before the throne. The righteous receive glorified, imperishable bodies fit for the new creation. The unrighteous are raised to face judgment. The intermediate state (disembodied) is temporary; the final state is embodied forever. God is not done with the body — He created it, redeemed it, and will glorify it.',
    },
    {
        'id': 'B38',
        'category': 'RESTORATION',
        'title': 'Final Judgment and Hell — The Last Riv',
        'subtitle': 'The final judgment is the last covenant lawsuit (riv) of the cosmos — and hell is real, eternal, and just.',
        'key_texts': ['Matthew 25:31-46', 'Revelation 20:11-15', '2 Thessalonians 1:6-10', 'Daniel 7:9-10', 'Hebrews 9:27'],
        'council_relevance': 'The final judgment is the last session of the divine council — the riv to end all riv proceedings. Daniel 7:9-10 depicts it: "thrones were placed, and the Ancient of Days took His seat... the court sat in judgment, and the books were opened." Revelation 20:11-15 expands it: the great white throne, the books opened (including the Book of Life), and every person judged. This is the final council prosecution: every being — human and spiritual — gives account. The lake of fire is "prepared for the devil and his angels" (Matt 25:41) — the ultimate prison for the cosmic rebels, but also for humans who aligned with them.',
        'covenant_link': 'Judgment is always covenant-based. The "books" contain the record of covenant fidelity (or infidelity). The Book of Life is the covenant membership roll. The sentence is just because it is based on revealed covenant terms, not arbitrary decree.',
        'eschatological_trajectory': 'This IS the terminal eschatological event for evil. After the final judgment, there is no more rebellion, no more accusation, no more corruption. The cosmos is cleansed and ready for the new creation.',
        'governance_tag': 'eschatological',
        'confidence': 'A',
        'orthodox_position': 'The final judgment is real, universal, and just. Every person faces judgment (Heb 9:27). Believers are judged for rewards (2 Cor 5:10) but not for condemnation (Rom 8:1). Unbelievers face the great white throne (Rev 20:11-15) and eternal punishment. Hell (the lake of fire) is real, conscious, and eternal — "eternal punishment" (Matt 25:46, using the same word "eternal" applied to "eternal life" — if one is temporary, so is the other). Annihilationism and universalism both fail the text.',
        'historical_figures': [
            {'name': 'Jesus of Nazareth', 'position': 'Spoke more about hell than anyone else in Scripture. The sheep-and-goats judgment (Matt 25:31-46) is His own teaching: "Depart from Me, you cursed, into the eternal fire."', 'orthodox': True},
            {'name': 'Augustine of Hippo', 'position': 'Defended the eternity of hell against Origen\'s universalism: the punishment is as eternal as the life — both use aionios.', 'orthodox': True},
            {'name': 'Origen of Alexandria', 'position': 'Taught apokatastasis — the eventual restoration of all beings, including the devil. Condemned at the Fifth Ecumenical Council (553 AD). Contradicts Jesus\' explicit teaching on eternal punishment.', 'orthodox': False},
            {'name': 'Rob Bell', 'position': 'In Love Wins, promoted modern universalism — everyone is eventually saved, hell is not eternal. A compassionate-sounding position that contradicts Christ\'s clear words.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'riv (רִיב) — "covenant lawsuit" — the prophetic prosecution format applied to the final judgment. din (דִּין) — "judgment" (Dan 7:10 — dina yetiv, "the court sat in judgment"). thronos megas leukos (θρόνος μέγας λευκός) — "great white throne" (Rev 20:11). limne tou pyros (λίμνη τοῦ πυρός) — "lake of fire" (Rev 20:15). aionios (αἰώνιος) — "eternal, age-lasting" (Matt 25:46) — applied equally to punishment and life. kolasis aionios (κόλασις αἰώνιος) — "eternal punishment" (Matt 25:46).',
        'summary': 'The final judgment is the last riv — the covenant lawsuit of the cosmos. Every being stands before the throne, every account is settled, and every rebel — spiritual and human — receives just sentence. Hell is real, conscious, and eternal, because sin against an infinite God demands infinite justice. This is not vindictiveness but righteousness — the same God who offers grace through the cross also upholds justice through the judgment. Both are expressions of His character.',
    },
    {
        'id': 'B39',
        'category': 'RESTORATION',
        'title': 'New Creation and Governance Transfer — Eden Restored, Council Reunified',
        'subtitle': 'The final state is not escape from creation but its restoration — Eden expanded, the council reunified, humans reigning forever.',
        'key_texts': ['Revelation 21:1-5', 'Revelation 22:1-5', '1 Corinthians 15:24-28', 'Isaiah 65:17-25', 'Romans 8:19-22'],
        'council_relevance': 'Revelation 21-22 is the resolution of the entire divine council narrative. Eden is restored and expanded to cosmic scale: the tree of life is back (Rev 22:2), the river of life flows from the throne (Rev 22:1), and the curse is removed (Rev 22:3). The council is reunified: God dwells directly with His people (Rev 21:3 — "the dwelling place of God is with man"), the separation between heaven and earth is healed ("no more sea" — the chaos barrier is gone), and redeemed humans "will reign forever and ever" (Rev 22:5). The governance transfer is complete: 1 Corinthians 15:24-28 — Christ delivers the kingdom to the Father after destroying every hostile power, "that God may be all in all." The corrupt elohim are judged (Ps 82), the faithful remain, and humanity — the once-junior council members — reigns alongside God for eternity.',
        'covenant_link': 'Every covenant promise finds its ultimate fulfillment: Noahic stability (new heavens and earth), Abrahamic blessing (all nations gathered, Rev 7:9), Mosaic holiness (all inhabitants are holy), Davidic throne (Christ reigns), New Covenant intimacy ("they shall be His people, and God Himself will be with them," Rev 21:3).',
        'eschatological_trajectory': 'This IS the eschatological terminus — the eternal state. There is no further development, no further rebellion, no further restoration needed. God is all in all. The story that began in a garden ends in a garden-city, and the governance that began with delegation ends with reunion — not the abolition of delegation but its perfection.',
        'governance_tag': 'eschatological',
        'confidence': 'A',
        'orthodox_position': 'The final state is new creation, not disembodied heaven. God makes "all things new" (Rev 21:5) — not all new things. The material world is redeemed, not discarded. The new Jerusalem descends FROM heaven TO earth (Rev 21:2) — God comes to dwell with humanity, not the other way around. Redeemed humans reign forever (Rev 22:5) in glorified bodies on a renewed earth. This is the defeat of every gnostic impulse to escape the material world. Creation is good, and God\'s final word over it is restoration, not annihilation.',
        'historical_figures': [
            {'name': 'N.T. Wright', 'position': 'Championed new creation eschatology against "going to heaven when you die" reductionism. The final hope is resurrection and renewed creation, not escape from the world.', 'orthodox': True},
            {'name': 'Irenaeus of Lyon', 'position': 'Taught that God\'s original creation purpose will be fulfilled, not abandoned. Recapitulation ends in consummation — everything God intended from the beginning is realized in the end.', 'orthodox': True},
            {'name': 'Gnostic eschatology', 'position': 'Teaches the material world is evil and the goal is escape to a purely spiritual realm. This is the exact opposite of biblical eschatology, which promises physical resurrection in a renewed physical creation.', 'orthodox': False},
        ],
        'key_hebrew_greek': 'shamayim chadashim ve-erets chadashah (שָׁמַיִם חֲדָשִׁים וְאֶרֶץ חֲדָשָׁה) — "new heavens and new earth" (Isa 65:17). kainos (καινός) — "new" (Rev 21:5) — renewed/transformed, not brand new (neos). skene tou theou meta ton anthropon (σκηνὴ τοῦ θεοῦ μετὰ τῶν ἀνθρώπων) — "the dwelling/tabernacle of God is with mankind" (Rev 21:3). basileuousin eis tous aionas ton aionon (βασιλεύσουσιν εἰς τοὺς αἰῶνας τῶν αἰώνων) — "they will reign forever and ever" (Rev 22:5). ta panta en pasin (τὰ πάντα ἐν πᾶσιν) — "all in all" (1 Cor 15:28).',
        'summary': 'The new creation is the resolution of everything — Eden restored, the council reunified, humanity reigning, every covenant fulfilled, every rebellion judged, and God dwelling directly with His people. This is not escape from the material world but its perfection. The governance architecture that began with delegation (God ruling through council, covenant, and human agents) is not abolished but consummated — God is all in all, and His redeemed humanity reigns forever in a creation made permanently, gloriously new.',
    },
]

# ══════════════════════════════════════════════════════════════
# SUMMARY STATISTICS
# ══════════════════════════════════════════════════════════════

TOTAL_BELIEFS = len(CORE_BELIEFS)

# Count by category
CATEGORIES_COUNT = {}
for b in CORE_BELIEFS:
    cat = b['category']
    CATEGORIES_COUNT[cat] = CATEGORIES_COUNT.get(cat, 0) + 1

# Count by confidence level
CONFIDENCE_COUNT = {}
for b in CORE_BELIEFS:
    conf = b['confidence']
    CONFIDENCE_COUNT[conf] = CONFIDENCE_COUNT.get(conf, 0) + 1

# Count by governance tag
GOVERNANCE_TAGS = {}
for b in CORE_BELIEFS:
    tag = b['governance_tag']
    GOVERNANCE_TAGS[tag] = GOVERNANCE_TAGS.get(tag, 0) + 1
