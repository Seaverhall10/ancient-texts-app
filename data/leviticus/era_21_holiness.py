"""
era_21_holiness.py — The Holiness Code (Leviticus 18-22)

"Be holy (qedoshim tihyu), for I the LORD your God am holy (qadosh)" (19:2). The
Holiness Code (H, Leviticus 18-26) moves from ritual to ethics, from priestly
procedure to daily life. The Hebrew qadosh ('holy') means 'set apart, distinct,
other' — it describes God's fundamental nature and Israel's calling to reflect it.
Israel is called to be different from the nations — not because of arbitrary rules
but because Israel belongs to YHWH while the nations were allotted to lesser elohim
(divine council members, Deut 32:8-9) who corrupted them. Every prohibition is a
declaration of allegiance: 'I follow YHWH, not the gods of the nations.'
"""

CHAPTERS = [
    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 18 — SEXUAL BOUNDARIES
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-18",
        "ref": "Leviticus 18",
        "chapter_num": 18,
        "title": "Sexual Holiness — Boundaries the Nations Violated",
        "era": "holiness",
        "type": "chapter",
        "themes": ["HOLY", "LAW", "NATIONS", "LAND"],

        "synopsis": (
            "Leviticus 18 opens the Holiness Code with the most comprehensive list of "
            "prohibited sexual relationships in the Torah. The chapter is framed by an "
            "explicit contrast between Israel and the nations: 'You shall not do as they "
            "do in the land of Egypt, where you lived, and you shall not do as they do in "
            "the land of Canaan, to which I am bringing you' (18:3). Israel must not follow "
            "the practices of either Egypt (where they came from) or Canaan (where they are "
            "going). The prohibited relationships include: parent-child, step-parent, sibling, "
            "half-sibling, grandchild, aunt, uncle's wife, daughter-in-law, sister-in-law, "
            "a woman and her daughter or granddaughter, a woman's sister as a rival wife, "
            "intercourse during menstruation, adultery, child sacrifice to Molech, male "
            "same-sex intercourse, and bestiality. The chapter concludes with the warning "
            "that the land itself 'vomits out its inhabitants' when they practice these "
            "things (18:25, 28) — the land is personified as a moral agent that cannot "
            "tolerate certain practices. The nations being driven out are expelled not for "
            "ethnic reasons but for moral ones: 'For the people of the land, who were before "
            "you, did all of these abominations, so that the land became unclean' (18:27). "
            "The inclusion of Molech worship (child sacrifice) in the middle of a sexual "
            "ethics chapter is significant — it reveals that these prohibitions are not "
            "merely about human relationships but about worship. The nations' sexual practices "
            "were often tied to their religious systems — temple prostitution, fertility cults, "
            "and child sacrifice were interconnected. Sexual holiness and theological allegiance "
            "are inseparable in the Holiness Code."
        ),

        "key_verse": {
            "ref": "Leviticus 18:24-25",
            "text": "Do not make yourselves unclean by any of these things, for by all these the nations I am driving out before you have become unclean, and the land became unclean, so that I punished its iniquity, and the land vomited out its inhabitants.",
            "translation": "ESV"
        },

        "original_terms": [
            "toevah", "ervah", "gillui_arayot", "molech",
            "tebel", "zimah", "tame", "qia", "chukkat"
            # Key glosses: toevah = 'abomination/detestable thing' (in Leviticus,
            # typically associated with practices of the pagan nations); ervah =
            # 'nakedness/exposure' (euphemism for sexual relations — 'to uncover
            # the nakedness of'); gillui arayot = 'uncovering of nakedness'
            # (the category term for sexual violations); molech = a Canaanite/
            # Ammonite deity to whom children were sacrificed by fire (possibly
            # vocalized with the vowels of boshet, 'shame'); tebel = 'confusion/
            # perversion' (mixing of categories that violates created order);
            # zimah = 'depravity/lewdness'; qia = 'to vomit' (the land vomits
            # out inhabitants who practice these things)
        ],

        "ane_backdrop": (
            "The sexual prohibitions in Leviticus 18 address practices documented across the "
            "ANE. Incestuous relationships are addressed in Hittite law codes (Laws 189-195) "
            "and the Middle Assyrian Laws (MAL A 55). Egyptian royal practice permitted "
            "sibling marriage (particularly in the Ptolemaic period), which Leviticus "
            "categorically forbids. Child sacrifice to Molech is attested archaeologically "
            "at Carthaginian tophets and in biblical accounts (2 Kings 23:10, Jer 7:31). "
            "The Ugaritic texts describe ritual sexual activity in the cult of Baal and "
            "Asherah. Mesopotamian temple prostitution (involving both male and female "
            "participants) is documented in Herodotus and in cuneiform texts. The Levitical "
            "prohibitions are not addressing private behavior in isolation but a comprehensive "
            "religious-sexual system in which sexual acts were integrated with pagan worship. "
            "The phrase 'you shall not do as they do' places the entire chapter in the context "
            "of covenant separation from the nations' religious practices."
        ),

        "second_temple": [
            {
                "source": "Jubilees 33:10-20",
                "summary": "Jubilees expands on the sexual prohibitions, adding that "
                           "these laws were 'written and ordained on the heavenly tablets' — "
                           "they are not merely Sinaitic legislation but primordial cosmic law.",
                "relevance": "Elevates the sexual boundaries from national law to cosmic "
                             "law — they are inscribed in heaven, applicable to all humanity."
            },
            {
                "source": "4Q251 (Halakhah A)",
                "summary": "Qumran legal text interpreting and expanding the Leviticus 18 "
                           "sexual prohibitions, including additional degrees of kinship.",
                "relevance": "Shows that the Qumran community intensified the prohibited "
                             "relationships, reflecting their commitment to stricter purity."
            },
            {
                "source": "Wisdom of Solomon 14:12-27",
                "summary": "Describes the sexual depravity of Gentile nations as flowing "
                           "from idolatry — 'the making of idols was the beginning of "
                           "sexual immorality.'",
                "relevance": "Confirms the Leviticus 18 link between idolatrous worship "
                             "and sexual corruption — the nations' practices are a package."
            }
        ],

        "cross_refs": [
            {"ref": "Romans 1:18-32", "note": "Paul's description of Gentile moral decline echoes Leviticus 18's portrait of the nations — idolatry leads to sexual corruption", "type": "nt"},
            {"ref": "1 Corinthians 5:1", "note": "Paul confronts a case of sexual immorality 'not even tolerated among pagans' — a Leviticus 18 violation in the church", "type": "nt"},
            {"ref": "Deuteronomy 12:31", "note": "'They even burn their sons and daughters in the fire to their gods' — the Molech prohibition in Deuteronomic form", "type": "ot"},
            {"ref": "2 Kings 23:10", "note": "Josiah defiles the Topheth in the Valley of Ben-Hinnom — ending Molech worship", "type": "ot"},
            {"ref": "Ezekiel 16:20-21", "note": "Jerusalem accused of child sacrifice — 'you slaughtered my children and delivered them up as an offering'", "type": "ot"},
            {"ref": "Acts 15:20, 29", "note": "The Jerusalem Council requires Gentile believers to abstain from 'sexual immorality' (porneia) — the Leviticus 18 framework", "type": "nt"},
            {"ref": "Genesis 15:16", "note": "'The iniquity of the Amorites is not yet complete' — the land-vomiting principle in preview", "type": "ot"},
            {"ref": "Hebrews 12:16", "note": "'See to it that no one is sexually immoral or unholy like Esau' — the Leviticus 18 principle of sexual holiness carried into the new covenant", "type": "nt"},
            {"ref": "Hebrews 13:4", "note": "'Let marriage be held in honor among all, and let the marriage bed be undefiled, for God will judge the sexually immoral and adulterous' — the Leviticus 18 sexual boundaries restated as permanent moral law", "type": "nt"}
        ],

        "divine_council_note": (
            "The framework of Leviticus 18 is deeply connected to the Deuteronomy 32:8-9 "
            "allotment. The nations were placed under the governance of lesser elohim "
            "(bene elohim — 'sons of God,' divine council members assigned to govern the "
            "nations after the Babel dispersion) who corrupted them — leading to the very "
            "practices Leviticus 18 prohibits. "
            "The nations' sexual practices were not merely cultural preferences but the "
            "outworking of corrupt spiritual governance. Temple prostitution, child sacrifice, "
            "and fertility cult practices were worship directed at these corrupt elohim. "
            "When Israel is told 'you shall not do as they do,' the implicit reason is: "
            "you belong to YHWH, not to the gods who rule the nations. The sexual "
            "boundaries are covenant boundaries — they mark the difference between YHWH's "
            "kingdom and the kingdoms of the corrupted council members. The land itself "
            "responds to moral reality because YHWH governs the land of Israel directly."
        ),

        "sections": [
            {
                "title": "The Framework: Not Like Egypt, Not Like Canaan (18:1-5)",
                "content": (
                    "YHWH establishes the principle: 'You shall not do as they do in the "
                    "land of Egypt... and you shall not do as they do in the land of Canaan.' "
                    "Israel is defined by contrast — not the old life, not the surrounding "
                    "culture. 'You shall follow my rules and keep my statutes... I am the "
                    "LORD your God' (18:4). The repeated refrain 'I am the LORD' (ani YHWH) "
                    "appears as the motivational clause — obedience is grounded not in "
                    "abstract morality but in relationship. The person who keeps these "
                    "statutes 'shall live by them' (chai bahem) — a phrase Paul quotes in "
                    "Galatians 3:12 and Romans 10:5, pivotal to his argument about law and faith."
                )
            },
            {
                "title": "Prohibited Kinship Relationships (18:6-18)",
                "content": (
                    "The formula 'you shall not uncover the nakedness (ervah) of...' governs "
                    "the section. Ervah literally means 'nakedness/exposure' and is a euphemism "
                    "for sexual relations. The prohibited degrees cover: mother, father's wife "
                    "(stepmother), sister, half-sister, granddaughter, father's wife's daughter, "
                    "paternal aunt, maternal aunt, uncle's wife, daughter-in-law, brother's wife, "
                    "a woman and her daughter/granddaughter, and a woman's sister as a rival "
                    "wife during the first wife's lifetime. The list is remarkably comprehensive "
                    "and addresses relationships that could be exploited in polygamous family "
                    "structures. The prohibition protects vulnerable family members and maintains "
                    "the integrity of family bonds. Several patriarchs (Abraham married his "
                    "half-sister, Jacob married two sisters) practiced what Leviticus now "
                    "prohibits — the Sinai legislation represents a new standard."
                )
            },
            {
                "title": "Menstrual Impurity, Adultery, and Molech (18:19-21)",
                "content": (
                    "Three prohibitions are grouped: sexual intercourse during menstruation "
                    "(extending the Lev 15:24 impurity to moral prohibition), adultery with "
                    "a neighbor's wife, and the giving of children 'to pass through to Molech.' "
                    "The Molech prohibition sits between sexual and religious laws, revealing "
                    "the intersection: child sacrifice was a religious act tied to Canaanite "
                    "and Ammonite worship. 'Molech' (melek, 'king') may be a deliberate "
                    "distortion of 'melek' using the vowels of boshet ('shame'). The practice "
                    "involved burning children — either as direct sacrifice or passing them "
                    "through fire as a dedication ritual. Either way, it represents the most "
                    "extreme violation: destroying the image-bearers God created in pursuit "
                    "of favor from hostile spiritual beings."
                )
            },
            {
                "title": "Same-Sex Relations and Bestiality (18:22-23)",
                "content": (
                    "Male same-sex intercourse is called toevah ('abomination/detestable thing'). "
                    "Bestiality is called tebel ('confusion/perversion') — a mixing of categories "
                    "that violates the created order's boundaries. Both prohibitions are stated "
                    "briefly and without elaboration. The term toevah in Leviticus typically "
                    "refers to practices associated with pagan worship (cf. Deut 7:25-26; "
                    "18:9-12 where child sacrifice, divination, and sorcery are called toevah). "
                    "This contextual usage suggests the prohibitions address cultic practices "
                    "— acts performed in the context of the nations' worship systems — though "
                    "the text itself does not explicitly limit them to cultic contexts."
                )
            },
            {
                "title": "The Land Vomits Its Inhabitants (18:24-30)",
                "content": (
                    "The chapter closes with the extraordinary claim that the land itself "
                    "responds to moral reality: 'The land became unclean, so that I punished "
                    "its iniquity, and the land vomited out its inhabitants' (18:25). The "
                    "Canaanites are being expelled because the land cannot tolerate their "
                    "practices. Israel is warned: 'lest the land vomit you out also' — the "
                    "same fate awaits Israel if they adopt the nations' ways. This personification "
                    "of the land is deeply theological: the land of Israel is YHWH's land, "
                    "directly governed, morally responsive. What pollutes it is not merely "
                    "ritual impurity but moral corruption. The warning is prophetic: Israel "
                    "will indeed be 'vomited out' in the exile (2 Kings 17, Jer 7:15). "
                    "The Hebrew verb qia ('to vomit') is visceral — the land's revulsion "
                    "at moral corruption is depicted in the most physical terms possible."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 19 — THE HEART OF THE HOLINESS CODE
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-19",
        "ref": "Leviticus 19",
        "chapter_num": 19,
        "title": "Be Holy — The Ethical Heart of the Torah",
        "era": "holiness",
        "type": "chapter",
        "themes": ["HOLY", "LAW", "LOVE", "NAME"],

        "synopsis": (
            "Leviticus 19 is the ethical masterpiece of the Torah — a comprehensive vision "
            "of holy community life that ranges from the sublime ('Love your neighbor as "
            "yourself,' 19:18) to the specific ('Do not wear cloth of mixed fibers,' 19:19). "
            "The chapter opens with the foundational command: 'You shall be holy, for I the "
            "LORD your God am holy' (19:2) — the only place in the Pentateuch where this "
            "command is addressed to the entire congregation of Israel, not just the priests. "
            "Holiness is democratized: every Israelite, not just the priesthood, is called "
            "to embody God's character. The chapter covers an astonishing range of topics: "
            "reverence for parents (19:3), Sabbath observance (19:3), rejection of idols "
            "(19:4), peace offering procedures (19:5-8), provision for the poor through "
            "gleaning rights (19:9-10), theft and lying (19:11), false oaths (19:12), "
            "oppression of workers (19:13), protection of the disabled (19:14), judicial "
            "fairness (19:15), slander (19:16), the prohibition of hatred and the command "
            "to rebuke (19:17), and the climactic command to love the neighbor (19:18). "
            "The second half addresses mixed breeding/planting/fabrics (19:19), a case law "
            "about sexual violation (19:20-22), waiting to eat from fruit trees (19:23-25), "
            "blood consumption (19:26), divination and sorcery (19:26), specific grooming "
            "prohibitions (19:27-28), prostitution (19:29), Sabbath and sanctuary reverence "
            "(19:30), mediums and necromancers (19:31), respect for the elderly (19:32), "
            "justice for the resident alien (19:33-34 — 'love the alien as yourself'), "
            "honest weights and measures (19:35-36), and the closing refrain: 'I am the "
            "LORD' (19:37). The chapter echoes the Decalogue repeatedly but in expanded, "
            "applied form. Jesus identifies 19:18 as the second greatest commandment "
            "(Matt 22:39). Paul calls it the summation of the law (Gal 5:14, Rom 13:9)."
        ),

        "key_verse": {
            "ref": "Leviticus 19:18",
            "text": "You shall not take vengeance or bear a grudge against the sons of your own people, but you shall love your neighbor as yourself: I am the LORD.",
            "translation": "ESV"
        },

        "original_terms": [
            "qadosh", "ahavah", "rea", "ger", "leket",
            "peah", "mishpat", "toevah", "ov", "yidoni", "ani_YHWH"
            # Key glosses: qadosh = 'holy/set apart' (God's essential nature,
            # which Israel is called to reflect); ahavah = 'love' (not merely
            # emotion but covenantal commitment expressed in action); rea =
            # 'neighbor/fellow' (the one you are obligated to love); ger =
            # 'resident alien/sojourner' (a non-Israelite living in Israel's
            # community — also protected by the love command, 19:34); leket =
            # 'gleanings' (fallen grain left for the poor); pe'ah = 'corner/
            # edge' (of the field, left unharvested for the poor); mishpat =
            # 'justice/judgment' (right ruling); ov = 'medium/spiritist' (one
            # who channels the dead — forbidden because it accesses the
            # supernatural through unauthorized channels, cf. the Watcher
            # tradition); yidoni = 'necromancer/familiar spirit' (divination
            # through the dead); ani YHWH = 'I am the LORD' (the covenant
            # identity formula — appears 16 times in this chapter, grounding
            # every command in God's character)
        ],

        "ane_backdrop": (
            "The ethical vision of Leviticus 19 finds parallels in ANE wisdom traditions but "
            "surpasses them in scope and theological grounding. The Egyptian Instruction of "
            "Amenemope provides ethical guidelines including honest weights, care for the poor, "
            "and just speech — but grounds them in ma'at (cosmic order) rather than divine "
            "command. The Code of Hammurabi prescribes justice but only for specific classes — "
            "the penalties differ by social rank. Leviticus 19 demands equal justice: 'You "
            "shall not be partial to the poor or defer to the great' (19:15). The provision "
            "for gleaning (pe'ah and leket) has no precise ANE parallel — it is a systematic "
            "welfare mechanism embedded in agricultural law. The command to love the alien "
            "(ger) as oneself (19:34) is revolutionary in its context — no other ANE law code "
            "extends the full obligation of neighbor-love to non-citizens. The mixing "
            "prohibitions (19:19) have distant parallels in Egyptian purity regulations that "
            "prohibit certain mixtures, reflecting a concern for categorical boundaries."
        ),

        "second_temple": [
            {
                "source": "Hillel (Babylonian Talmud, Shabbat 31a)",
                "summary": "When asked to teach the whole Torah standing on one foot, Hillel "
                           "replied: 'What is hateful to you, do not do to your neighbor. "
                           "This is the whole Torah; the rest is commentary.'",
                "relevance": "Shows that by the first century BC, Leviticus 19:18 was "
                             "recognized as the ethical center of the Torah."
            },
            {
                "source": "Testament of Issachar 5:2",
                "summary": "'Love the LORD and your neighbor; have compassion on the poor "
                           "and the weak' — combining Deuteronomy 6:5 and Leviticus 19:18.",
                "relevance": "Pre-dates Jesus' combination of the two great commandments "
                             "(Mark 12:28-31), showing this pairing was already present in "
                             "Second Temple Judaism."
            },
            {
                "source": "CD (Damascus Document) 6:20-7:1",
                "summary": "The Qumran community applied Leviticus 19's neighbor-love "
                           "within their own community while restricting it from outsiders, "
                           "whom they considered 'sons of darkness.'",
                "relevance": "Illustrates the interpretive question Jesus addresses in "
                             "the parable of the Good Samaritan: 'Who is my neighbor?'"
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 22:39", "note": "Jesus identifies Lev 19:18 as 'the second greatest commandment' — second only to loving God (Deut 6:5)", "type": "nt"},
            {"ref": "Galatians 5:14", "note": "'The whole law is fulfilled in one word: You shall love your neighbor as yourself' — Paul's summary of Leviticus 19:18", "type": "nt"},
            {"ref": "Romans 13:8-10", "note": "'Love does no wrong to a neighbor; therefore love is the fulfilling of the law' — the ethical logic of Lev 19 in Pauline theology", "type": "nt"},
            {"ref": "James 2:8", "note": "'If you really fulfill the royal law according to the Scripture, You shall love your neighbor as yourself, you are doing well' — James quotes Lev 19:18", "type": "nt"},
            {"ref": "Luke 10:25-37", "note": "The parable of the Good Samaritan — Jesus' answer to 'Who is my neighbor?' expands Lev 19:18 beyond ethnic boundaries", "type": "nt"},
            {"ref": "Ruth 2:2-16", "note": "Ruth gleans in Boaz's field — the Leviticus 19:9-10 gleaning laws in narrative application", "type": "ot"},
            {"ref": "Deuteronomy 25:13-16", "note": "Honest weights and measures — the Leviticus 19:35-36 principle restated", "type": "ot"},
            {"ref": "1 Peter 1:15-16", "note": "'As he who called you is holy, be holy yourselves' — quoting Leviticus 19:2", "type": "nt"},
            {"ref": "Hebrews 12:14", "note": "'Strive for peace with everyone, and for the holiness without which no one will see the Lord' — the Lev 19:2 holiness command restated as the prerequisite for encountering God", "type": "nt"},
            {"ref": "Hebrews 13:1-3", "note": "'Let brotherly love continue. Do not neglect to show hospitality to strangers' — the Lev 19:18 and 19:33-34 neighbor-love and alien-love commands in the new covenant", "type": "nt"}
        ],

        "divine_council_note": (
            "Leviticus 19 democratizes holiness — extending the priestly calling to all "
            "Israel. In the divine council framework, Israel was chosen as YHWH's portion "
            "(nachalah, Deut 32:9) while the nations were allotted to lesser elohim. The "
            "ethical commands of Leviticus 19 are the practical outworking of that election: "
            "YHWH's people must reflect YHWH's character because they belong to YHWH, not "
            "to the corrupted gods. The command to love the alien (ger) is particularly "
            "significant — even those from the allotted nations who join Israel's community "
            "receive the full protection of covenant ethics, anticipating the day when all "
            "nations are reclaimed from the rebel elohim (Ps 82:8). The prohibition of "
            "divination, mediums, and necromancy (19:26, 31) directly opposes the spiritual "
            "technologies the fallen Watchers taught humanity. 1 Enoch 8:3 explicitly "
            "identifies sorcery, enchantments, and root-cutting (herbalism for magical "
            "purposes) among the forbidden arts Azazel and the other Watchers introduced. "
            "When Leviticus 19 forbids these practices, it is reversing the Watcher "
            "corruption — cutting Israel off from the illicit knowledge the rebellious "
            "council members disseminated. True knowledge comes through YHWH's authorized "
            "channels: the Torah, the prophets, the Urim and Thummim — not through the "
            "spiritual black market the fallen ones established."
        ),

        "sections": [
            {
                "title": "The Foundational Command: Be Holy (19:1-4)",
                "content": (
                    "YHWH speaks to the entire congregation of Israel — not just the priests, "
                    "not just the elders, but everyone: 'You shall be holy (qedoshim tihyu), "
                    "for I the LORD your God am holy.' Holiness is not optional and not "
                    "restricted to the religious elite. It begins with the most basic social "
                    "obligations: revere your parents (echoing the Fifth Commandment), keep "
                    "the Sabbath (Fourth Commandment), reject idols (First and Second "
                    "Commandments). The order is significant: family, time, worship — the "
                    "three foundational structures of Israelite life. The chapter will "
                    "proceed to apply holiness to every conceivable domain: economics, "
                    "justice, agriculture, sexuality, speech, and inter-ethnic relations. "
                    "Holiness is comprehensive — it covers all of life because God's "
                    "character encompasses all of reality."
                )
            },
            {
                "title": "Social Justice: The Poor, Workers, and Disabled (19:9-14)",
                "content": (
                    "The gleaning laws (pe'ah and leket) require farmers to leave the edges "
                    "of their fields unharvested and not to pick up fallen grain or stripped "
                    "grapevines — these belong 'to the poor and the sojourner.' This is "
                    "institutionalized provision: welfare embedded in the agricultural system. "
                    "Theft and lying are prohibited; false oaths profane God's name (19:12). "
                    "Workers' wages must be paid the same day — 'You shall not oppress your "
                    "neighbor or rob him. The wages of a hired worker shall not remain with "
                    "you all night until the morning' (19:13). The disabled are specifically "
                    "protected: 'You shall not curse the deaf or put a stumbling block before "
                    "the blind, but you shall fear your God' (19:14). The phrase 'fear your "
                    "God' appears when no human witness would detect the violation — God sees "
                    "what the deaf cannot hear and the blind cannot see."
                )
            },
            {
                "title": "Justice, Truth, and Neighbor-Love (19:15-18)",
                "content": (
                    "Judicial fairness: 'You shall not be partial to the poor or defer to "
                    "the great, but in righteousness shall you judge your neighbor' (19:15). "
                    "Both directions of bias are prohibited — not just favoritism toward "
                    "the wealthy but also toward the poor. Justice is blind. Slander and "
                    "endangering a neighbor's life are prohibited (19:16). Then the remarkable "
                    "inner-life commands: 'You shall not hate your brother in your heart' "
                    "(19:17a) — the first prohibition of interior attitude in the Torah. "
                    "'You shall surely rebuke your neighbor' (19:17b) — love requires honesty, "
                    "not passive tolerance of sin. 'You shall not take vengeance or bear a "
                    "grudge' (19:18a). And the climax: 've'ahavta lere'akha kamokha — you "
                    "shall love your neighbor as yourself. I am the LORD' (19:18b). This "
                    "command, which Jesus and Paul identify as the summation of the law, sits "
                    "embedded in a chapter of specific, concrete, practical commands — love "
                    "is not abstract sentiment but the animating principle behind every ethical "
                    "obligation."
                )
            },
            {
                "title": "The Mixing Prohibitions and Boundary Theology (19:19)",
                "content": (
                    "Three mixing prohibitions: do not breed two kinds of cattle together, "
                    "do not sow a field with two kinds of seed, do not wear a garment of "
                    "mixed cloth (sha'atnez — specifically wool and linen, Deut 22:11). "
                    "These regulations have generated extensive scholarly debate. The most "
                    "persuasive explanation: maintaining the distinctions God established in "
                    "creation. The creation account repeatedly emphasizes 'according to its "
                    "kind' (le-mino) — each creature has its category. The mixing prohibitions "
                    "train Israel to respect categorical boundaries at every level of daily "
                    "life. The wool-linen prohibition may also have a priestly dimension: "
                    "the high priest's garments combined wool and linen (Exod 28), making "
                    "this combination uniquely sacred — ordinary Israelites wear one or the "
                    "other, not both."
                )
            },
            {
                "title": "Sorcery, Mediums, and the Supernatural Prohibition (19:26-31)",
                "content": (
                    "A cluster of prohibitions addresses unauthorized access to the "
                    "supernatural: 'You shall not eat any flesh with blood. You shall not "
                    "interpret omens or tell fortunes' (19:26). 'You shall not make any "
                    "cuts on your body for the dead or tattoo yourselves' (19:28 — mourning "
                    "rituals associated with pagan worship). 'Do not turn to mediums (ovot) "
                    "or necromancers (yid'onim); do not seek them out, and so make yourselves "
                    "unclean by them' (19:31). These prohibitions form a coherent package: "
                    "Israel must not access the spiritual realm through any channel other "
                    "than YHWH's authorized means (prophets, priests, Urim and Thummim). "
                    "Divination, necromancy, and sorcery are the spiritual technologies "
                    "of the nations under their corrupt elohim — Israel must have no part "
                    "in them. The Watcher tradition (1 Enoch 8:3) specifically identifies "
                    "sorcery and divination as arts the fallen Watchers taught humanity."
                )
            },
            {
                "title": "Love the Alien as Yourself (19:33-37)",
                "content": (
                    "One of the most remarkable commands in the Torah: 'When a stranger "
                    "(ger) sojourns with you in your land, you shall not do him wrong. "
                    "You shall treat the stranger who sojourns with you as the native among "
                    "you, and you shall love him as yourself, for you were strangers in the "
                    "land of Egypt. I am the LORD your God' (19:33-34). The command to love "
                    "the neighbor (19:18) is explicitly extended to the non-Israelite resident. "
                    "The motivation is experiential: Israel knows what it feels like to be "
                    "an alien. The chapter closes with honest weights and measures (19:35-36) "
                    "and the comprehensive summary: 'You shall observe all my statutes and "
                    "all my rules, and do them. I am the LORD.' The refrain 'I am the LORD' "
                    "appears 16 times in this chapter — every command is grounded in YHWH's "
                    "identity and Israel's relationship to him."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 20 — PENALTIES FOR VIOLATIONS
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-20",
        "ref": "Leviticus 20",
        "chapter_num": 20,
        "title": "Penalties for Holiness Violations — The Severity of Boundaries",
        "era": "holiness",
        "type": "chapter",
        "themes": ["HOLY", "LAW", "SPIRIT", "NATIONS"],

        "synopsis": (
            "Leviticus 20 prescribes the penalties for violations enumerated in chapters 18-19, "
            "particularly the sexual prohibitions and the worship of Molech. Where chapter 18 "
            "stated what is prohibited, chapter 20 states what happens when the prohibitions "
            "are violated. The penalties range from death by stoning to 'bearing their sin' "
            "(dying childless). The chapter opens with the most severe case: child sacrifice "
            "to Molech (20:1-5). The offender is stoned by the community, and if the community "
            "fails to act, YHWH himself will 'set his face against' the person and their "
            "family and 'cut them off' (20:3-5). Turning to mediums and necromancers receives "
            "the same divine opposition: 'I will set my face against that person and will cut "
            "him off from among his people' (20:6). The holiness call is restated: 'Consecrate "
            "yourselves and be holy, for I am the LORD your God' (20:7). Cursing parents "
            "receives the death penalty (20:9). Then the sexual violations from chapter 18 "
            "receive specific penalties: adultery (death for both), father's wife (death for "
            "both), daughter-in-law (death), male same-sex intercourse (death), marrying a "
            "woman and her mother (burning), bestiality (death for person and animal), sister "
            "(public disgrace and childlessness), menstrual intercourse (both cut off), and "
            "aunt/uncle's wife (childlessness). The chapter concludes with the allotment "
            "framework: 'I have separated you from the peoples, that you should be mine' "
            "(20:26). Israel's holiness is grounded in divine election and enforced by "
            "severe sanctions because the stakes are cosmic — the presence of God among "
            "his people depends on maintaining the boundaries."
        ),

        "key_verse": {
            "ref": "Leviticus 20:26",
            "text": "You shall be holy to me, for I the LORD am holy and have separated you from the peoples, that you should be mine.",
            "translation": "ESV"
        },

        "original_terms": [
            "mot_yumat", "karet", "regem", "ervah",
            "ov", "yidoni", "molech", "qadosh", "badal"
            # Key glosses: mot yumat = 'he shall surely be put to death'
            # (emphatic death penalty formula); karet = 'cutting off' (divine
            # excommunication — either premature death or removal from the
            # covenant community); regem = 'stoning' (communal execution
            # method); badal = 'to separate/distinguish' (the divine act of
            # setting Israel apart — echoes the separations of Genesis 1,
            # light from darkness, waters from waters)
        ],

        "ane_backdrop": (
            "Capital punishment for sexual violations is attested in ANE law codes: the "
            "Code of Hammurabi prescribes death for adultery (drowning), incest with a "
            "daughter-in-law (the man is bound and thrown into water), and bestiality. "
            "The Middle Assyrian Laws prescribe death for adultery and various incest "
            "violations. Hittite laws are more lenient in some cases but equally severe "
            "in others. The Levitical system is distinctive in its theological grounding: "
            "the penalties are not primarily about social order (as in Hammurabi) but about "
            "holiness — maintaining the separation between Israel and the nations that "
            "YHWH's presence among them requires. The burning penalty for marrying a woman "
            "and her mother (20:14) has a parallel in Hammurabi 157 (burning for incest "
            "with one's mother after the father's death)."
        ),

        "second_temple": [
            {
                "source": "Mishnah Sanhedrin 7:1-4",
                "summary": "Rabbinic systematization of the death penalty categories: "
                           "stoning, burning, beheading, and strangulation, with specific "
                           "offenses assigned to each category.",
                "relevance": "Shows how the Leviticus 20 penalties were elaborated into "
                             "a formal judicial system with precise procedural requirements."
            },
            {
                "source": "Jubilees 30:7-17",
                "summary": "Jubilees prescribes the death penalty for intermarriage with "
                           "Gentiles, expanding the Leviticus 20 sexual boundaries into "
                           "ethnic boundaries.",
                "relevance": "Illustrates how Second Temple Judaism intensified the "
                             "separation theology of Leviticus 20."
            }
        ],

        "cross_refs": [
            {"ref": "John 8:3-11", "note": "The woman caught in adultery — Jesus does not abolish the Leviticus 20:10 principle but transforms its application: 'Let him who is without sin cast the first stone'", "type": "nt"},
            {"ref": "1 Corinthians 6:9-11", "note": "Paul lists Leviticus 18/20 violations as excluding from the kingdom — 'and such were some of you. But you were washed'", "type": "nt"},
            {"ref": "Deuteronomy 7:6", "note": "'The LORD your God has chosen you... to be a people for his treasured possession' — the election theology behind Lev 20:26", "type": "ot"},
            {"ref": "1 Peter 2:9", "note": "'A chosen race, a royal priesthood, a holy nation, a people for his own possession' — Leviticus 20:26 applied to the church", "type": "nt"},
            {"ref": "Deuteronomy 18:10-12", "note": "The prohibition against mediums and necromancers restated — 'because of these abominations the LORD is driving them out'", "type": "ot"},
            {"ref": "1 Samuel 28:3-19", "note": "Saul consults the medium at Endor — violating Leviticus 20:6 and bringing judgment on himself", "type": "ot"},
            {"ref": "Hebrews 10:26-31", "note": "'If we go on sinning deliberately after receiving the knowledge of truth, there no longer remains a sacrifice for sins, but a fearful expectation of judgment' — the severity of Lev 20 penalties carried forward: deliberate covenant violation meets divine judgment", "type": "nt"},
            {"ref": "Hebrews 12:28-29", "note": "'Let us offer to God acceptable worship, with reverence and awe, for our God is a consuming fire' — the Lev 20 death penalties teach the same lesson: holiness is not optional, and God's response to covenant violation is terrifyingly real", "type": "nt"}
        ],

        "divine_council_note": (
            "Leviticus 20:26 — 'I have separated you from the peoples, that you should "
            "be mine' — is the Holiness Code's expression of the Deuteronomy 32:8-9 "
            "allotment. YHWH separated Israel from the nations he allotted to lesser "
            "elohim. The severity of the penalties reflects the cosmic significance of "
            "the separation: if Israel adopts the nations' practices, they blur the "
            "distinction that their entire identity depends on. The mediums and necromancers "
            "(ov and yidoni) represent unauthorized access to the spiritual realm — "
            "communication with the dead and with spiritual beings through channels the "
            "corrupt elohim established. Israel's rejection of these practices is "
            "covenant loyalty to YHWH against the spiritual powers that govern the nations."
        ),

        "sections": [
            {
                "title": "Molech Worship: The Supreme Violation (20:1-5)",
                "content": (
                    "The chapter opens with the most severe case: anyone who gives their "
                    "children to Molech shall be put to death by stoning. The community is "
                    "responsible for executing the penalty. If the community looks the other "
                    "way ('hides their eyes'), YHWH himself will intervene — 'I will set "
                    "my face against that man and against his clan and will cut off from "
                    "among their people both him and all who follow him in whoring after "
                    "Molech.' The language of 'whoring after' (zanah acharei) casts Molech "
                    "worship as spiritual adultery. Child sacrifice is the most extreme "
                    "form of covenant violation because it destroys image-bearers in "
                    "service to hostile spiritual powers."
                )
            },
            {
                "title": "Mediums, Necromancers, and the Holiness Call (20:6-8)",
                "content": (
                    "Turning to ov (medium/spirit of a dead person) or yidoni (necromancer/ "
                    "familiar spirit) receives divine opposition: 'I will set my face against "
                    "that person.' The medium or necromancer themselves receive the death "
                    "penalty by stoning (20:27). Between these prohibitions sits the holiness "
                    "call: 'Consecrate yourselves therefore, and be holy, for I am the LORD "
                    "your God. Keep my statutes and do them; I am the LORD who sanctifies "
                    "you' (20:7-8). The structure is intentional: rejection of unauthorized "
                    "supernatural access is framed by the call to holiness. True holiness "
                    "means YHWH is the exclusive source of spiritual guidance."
                )
            },
            {
                "title": "Capital Offenses: Sexual Violations (20:9-16)",
                "content": (
                    "The penalties for sexual violations are specified: cursing father or "
                    "mother (death — 'his blood is upon him'), adultery (death for both), "
                    "relations with father's wife (death for both — 'they have uncovered "
                    "the father's nakedness'), daughter-in-law (death — tebel, 'confusion'), "
                    "male same-sex intercourse (death — toevah), marrying a woman and her "
                    "mother (burning — zimah, 'depravity'), bestiality (death for person and "
                    "animal). The repeated phrase 'their blood is upon them' (demeihem bam) "
                    "places the responsibility on the offenders, not the executioners. The "
                    "penalties protect the most vulnerable (children, wives) and maintain "
                    "the family structures on which Israelite society depends."
                )
            },
            {
                "title": "Lesser Penalties: Public Disgrace and Childlessness (20:17-21)",
                "content": (
                    "Some violations receive lesser penalties: sexual relations with a sister "
                    "results in public disgrace and 'cutting off.' Relations during "
                    "menstruation means both are 'cut off' — they have 'uncovered the source' "
                    "(maqor) of her blood flow. Relations with an aunt means 'bearing their "
                    "iniquity' — dying childless (ariri). Relations with an uncle's wife or "
                    "brother's wife similarly results in childlessness. The childlessness "
                    "penalty (ariri) is understood as divine punishment — God closes the "
                    "womb. In a culture where descendants were one's legacy and social "
                    "security, childlessness was a devastating consequence."
                )
            },
            {
                "title": "The Separation Theology: You Shall Be Mine (20:22-27)",
                "content": (
                    "The closing section provides the theological foundation: Israel must "
                    "keep the statutes 'lest the land vomit you out' (echoing 18:25-28). "
                    "'You shall not walk in the customs of the nation that I am driving "
                    "out before you, for they did all these things, and therefore I "
                    "detested them' (20:23). Then the climactic statement: 'I have separated "
                    "you from the peoples... you shall be holy to me, for I the LORD am "
                    "holy and have separated you from the peoples, that you should be mine' "
                    "(20:24-26). The verb badal ('to separate/distinguish') echoes Genesis 1 "
                    "where God 'separates' light from darkness, waters from waters, day "
                    "from night. Israel's separation is a creative act — God is forming a "
                    "distinct people the same way he formed a distinct cosmos. The clean/unclean "
                    "distinction in animals (20:25) serves this separating function. The "
                    "chapter ends with the death penalty for mediums and necromancers (20:27) "
                    "— bookending the chapter's opening Molech prohibition with its closing "
                    "sorcery prohibition."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 21-22 — PRIESTLY HOLINESS STANDARDS
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-21-22",
        "ref": "Leviticus 21-22",
        "chapter_num": 21,
        "title": "Priestly Holiness — Higher Standards for Those Who Approach",
        "era": "holiness",
        "type": "chapter",
        "themes": ["HOLY", "PRIEST", "LAW", "NAME"],

        "synopsis": (
            "Leviticus 21-22 establishes heightened holiness requirements for the priests — "
            "the men who serve at the altar and enter the sanctuary. If all Israel must be "
            "holy, the priests must be holier. If all Israelites must avoid certain forms "
            "of impurity, priests must avoid more. The standards are graduated: ordinary "
            "priests have one set of restrictions; the high priest has stricter ones. "
            "Leviticus 21 covers three areas: (1) Priestly mourning restrictions — ordinary "
            "priests may only defile themselves by contact with the dead for immediate "
            "family (mother, father, son, daughter, brother, virgin sister), never for "
            "distant relatives or non-kin. The high priest may not defile himself for ANY "
            "death — not even his father or mother — and must not leave the sanctuary or "
            "dishevel his hair or tear his garments (21:10-12). (2) Priestly marriage "
            "restrictions — priests may not marry a prostitute, a divorced woman, or a "
            "defiled woman. The high priest may only marry a virgin from his own people "
            "(21:13-15). (3) Physical blemish restrictions — no descendant of Aaron with a "
            "physical defect may approach the altar: blindness, lameness, mutilated face, "
            "limb too long, broken foot or hand, hunchback, dwarfism, eye defect, itching "
            "disease, crushed testicles (21:16-23). Such priests may eat the sacred food "
            "but may not offer sacrifice. Leviticus 22 continues with rules governing "
            "priestly access to holy food (unclean priests must refrain until purified), "
            "who may eat sacred food (priest's family, not outsiders), and the quality "
            "standards for sacrificial animals (tamim — without blemish, no blindness, "
            "broken limbs, sores, or discharge). The blemish requirements are NOT about "
            "the inherent worth of disabled people — they are about the symbolic wholeness "
            "required in what represents God's perfect, unblemished holiness. The altar is "
            "a theatrical representation of the divine realm, and its personnel and "
            "offerings must reflect the perfection of the God they serve."
        ),

        "key_verse": {
            "ref": "Leviticus 21:6",
            "text": "They shall be holy to their God and not profane the name of their God. For they offer the LORD's food offerings, the bread of their God; therefore they shall be holy.",
            "translation": "ESV"
        },

        "original_terms": [
            "kohen", "kohen_gadol", "tamei_nefesh", "mum",
            "tamim", "challal", "qadash", "lechem_elohim", "chillul_hashem"
            # Key glosses: kohen = 'priest' (a descendant of Aaron authorized
            # to serve at the altar and in the sanctuary); kohen gadol = 'high
            # priest' (the chief priest who alone enters the Most Holy Place on
            # Yom Kippur); tamei nefesh = 'impurity from a corpse' (the most
            # severe form of ritual contamination); mum = 'physical blemish/
            # defect' (disqualifies a priest from altar service, though not
            # from eating sacred food); tamim = 'without blemish/perfect/
            # whole' (required of both sacrificial animals and officiating
            # priests); challal = 'profaned/defiled' (a priest's daughter who
            # has been sexually compromised); lechem elohim = 'bread/food of
            # God' (the offerings presented at the altar — God's 'table');
            # chillul ha-shem = 'profanation of the Name' (the opposite of
            # sanctifying God's name — the supreme sin in Levitical theology)
        ],

        "ane_backdrop": (
            "Heightened priestly standards are universal in the ANE. Egyptian priests at "
            "Karnak and other major temples were required to shave their entire bodies, "
            "abstain from certain foods, maintain sexual purity during periods of temple "
            "service, and were prohibited from wearing wool (only linen allowed — parallel "
            "to the Levitical linen requirement). Mesopotamian priests (enu, mashmashu) "
            "underwent physical examinations for bodily defects; those with deformities "
            "were disqualified from certain temple functions. Hittite Instructions for "
            "Temple Officials require scrupulous purity of the priests who handle sacred "
            "food — any contamination of the offering is treated as a serious offense "
            "against the gods. The Levitical system fits this broader pattern while adding "
            "its distinctive theological framework: the priests are holy because they serve "
            "the holy God, and their standards reflect his character."
        ),

        "second_temple": [
            {
                "source": "11QTemple (Temple Scroll) 15-17",
                "summary": "The Temple Scroll provides expanded priestly purity regulations, "
                           "including additional physical blemish disqualifications and "
                           "stricter mourning limitations.",
                "relevance": "Shows the Qumran community's intensification of priestly "
                             "holiness standards — reflecting their critique of the Jerusalem "
                             "priesthood's perceived laxity."
            },
            {
                "source": "Mishnah Bekhorot 7:1-6",
                "summary": "Lists 142 specific physical blemishes that disqualify both "
                           "priests and sacrificial animals — a massive expansion of the "
                           "Leviticus 21-22 lists.",
                "relevance": "Demonstrates the rabbinic elaboration of the blemish system — "
                             "the brief biblical lists generated extensive halakhic analysis."
            },
            {
                "source": "Philo, De Specialibus Legibus I.80-97",
                "summary": "Philo explains the priestly restrictions allegorically: physical "
                           "wholeness represents moral wholeness, and the priest's body is a "
                           "visible symbol of the invisible perfection of God.",
                "relevance": "The Hellenistic interpretation: the bodily requirements point "
                             "to spiritual realities — the priests embody what all Israel "
                             "should aspire to."
            }
        ],

        "cross_refs": [
            {"ref": "Hebrews 7:26-28", "note": "Christ is the high priest who IS holy, innocent, unstained, separated from sinners — fulfilling the Leviticus 21 requirements perfectly", "type": "nt"},
            {"ref": "Hebrews 4:15", "note": "Christ is tempted in every way yet 'without sin' — the tamim (unblemished) requirement fulfilled morally, not just physically", "type": "nt"},
            {"ref": "1 Peter 1:18-19", "note": "Redeemed 'with the precious blood of Christ, like that of a lamb without blemish or spot' — the tamim animal requirement applied to Christ", "type": "nt"},
            {"ref": "Malachi 1:8, 14", "note": "Condemnation of offering blind and lame animals — violation of the Leviticus 22:17-25 blemish standards", "type": "ot"},
            {"ref": "Ezekiel 44:15-31", "note": "Ezekiel's eschatological temple has Zadokite priests with requirements paralleling and intensifying Leviticus 21", "type": "ot"},
            {"ref": "John 1:29", "note": "'The Lamb of God' — Christ as the ultimate tamim offering, without blemish", "type": "nt"}
        ],

        "divine_council_note": (
            "The priests serve as the earthly counterpart of the heavenly council attendants. "
            "As the seraphim in Isaiah 6 and the living creatures in Ezekiel 1 attend YHWH's "
            "heavenly throne with awe and purity, the priests attend YHWH's earthly throne "
            "(the ark between the cherubim) with corresponding holiness. The higher standards "
            "for the high priest mirror the closer proximity of the senior council members "
            "to YHWH's throne. The blemish restrictions ensure that what represents the "
            "divine realm is whole, complete, and unblemished — reflecting the perfection "
            "of the heavenly reality the tabernacle copies. The requirement that the high "
            "priest never leave the sanctuary during service (21:12) parallels the heavenly "
            "attendants who never leave the divine presence."
        ),

        "sections": [
            {
                "title": "Ordinary Priestly Restrictions (21:1-9)",
                "content": (
                    "Ordinary priests must not defile themselves by contact with the dead "
                    "except for closest kin: mother, father, son, daughter, brother, and "
                    "virgin sister. Contact with any other corpse transmits death-impurity "
                    "incompatible with altar service. They must not shave their heads, "
                    "trim their beards, or cut their bodies — mourning practices associated "
                    "with pagan worship (cf. 1 Kings 18:28). Marriage restrictions: no "
                    "prostitute (zonah), defiled woman, or divorced woman. The priest's "
                    "daughter who becomes a prostitute profanes her father's holiness and "
                    "is burned with fire. The priest's sanctity extends to his household — "
                    "the family participates in the elevated standard."
                )
            },
            {
                "title": "The High Priest's Elevated Standard (21:10-15)",
                "content": (
                    "The high priest (kohen ha-gadol) faces stricter restrictions: he must "
                    "not loosen his hair or tear his garments in mourning — EVER. He must "
                    "not go near ANY dead body — not even his father or mother. He must not "
                    "leave the sanctuary during his service period 'lest he profane the "
                    "sanctuary of his God' (21:12). He must marry only a virgin of his own "
                    "people — not a widow, divorcee, profaned woman, or prostitute. The "
                    "restrictions are cumulative: everything that applies to ordinary priests "
                    "applies to him with additional layers. His proximity to the Most Holy "
                    "Place demands proportionally greater holiness. The anointing oil is "
                    "upon his head; the consecration garments are upon him — he carries the "
                    "weight of the divine presence continuously."
                )
            },
            {
                "title": "Physical Blemish Restrictions (21:16-24)",
                "content": (
                    "No descendant of Aaron with a physical defect (mum) may approach the "
                    "altar to offer 'the bread of his God.' The list: blindness, lameness, "
                    "mutilated face, limb too long, broken foot, broken hand, hunchback, "
                    "dwarfism, eye defect, itching disease, scabs, crushed testicles. Such "
                    "priests may eat from the holy food (both 'most holy' and 'holy' portions) "
                    "but may not approach the veil or the altar. This is NOT a statement about "
                    "the inherent worth of disabled individuals — it is about representational "
                    "wholeness. The altar and its ministers are a theatrical representation of "
                    "the divine realm. Just as the animal offering must be tamim (without "
                    "blemish), the priest who presents it must also be whole — because both "
                    "represent the perfection of the God they serve."
                )
            },
            {
                "title": "Priestly Access to Sacred Food (22:1-16)",
                "content": (
                    "Priests who are in a state of impurity must 'separate themselves from "
                    "the holy things' until they are clean, 'lest they profane my holy name' "
                    "(22:2). Sources of impurity that restrict access: tsara'at, abnormal "
                    "discharge, contact with anything contaminated by a corpse, seminal "
                    "emission, contact with unclean swarming things, or contact with an "
                    "unclean person. After purification (bathing, waiting until evening), "
                    "the priest may again eat the sacred food 'because it is his bread' "
                    "(22:7). No outsider (zar — non-priest) may eat the holy food. The "
                    "priest's household (including slaves purchased with money) may eat, "
                    "but a priest's daughter married to a non-priest may not, unless she "
                    "returns widowed or divorced with no children. If someone eats holy "
                    "food inadvertently, they must repay it plus one-fifth — the asham "
                    "principle of Leviticus 5."
                )
            },
            {
                "title": "Blemish-Free Offerings (22:17-33)",
                "content": (
                    "Sacrificial animals must be tamim (without blemish). Specifically "
                    "disqualified: blind, broken, maimed, having a discharge, itching "
                    "disease, or scabs. An animal with a limb too long or too short may "
                    "be offered as a freewill offering but not for a vow (22:23 — a rare "
                    "exception). Castrated animals may not be offered. Animals must be at "
                    "least eight days old (22:27 — perhaps echoing the eight-day circumcision "
                    "and ordination patterns). A mother and her young may not be slaughtered "
                    "on the same day (22:28 — a compassion regulation). Thanksgiving offerings "
                    "must be eaten the same day (reiterating 7:15). The concluding verses "
                    "state the purpose: 'You shall not profane my holy name, that I may be "
                    "sanctified among the people of Israel. I am the LORD who sanctifies you' "
                    "(22:32). The quality of the offering reflects the worshiper's view of "
                    "the God being worshipped. Malachi 1:8 will later condemn Israel for "
                    "offering blind and lame animals — showing contempt for God under the "
                    "guise of worship."
                )
            }
        ]
    }
]
