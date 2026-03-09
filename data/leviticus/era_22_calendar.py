"""
era_22_calendar.py — The Sacred Calendar and Covenant (Leviticus 23-27)

The festival calendar is Israel's prophetic timeline — each feast (mo'ed, 'appointed
time/meeting,' the same word as in 'Tent of Meeting') encodes both historical
memory and eschatological anticipation. The Sabbatical (shemittah, 'release') and
Jubilee (yovel, 'ram's horn/liberty') years extend the Sabbath principle to the
land itself. The covenant blessings and curses of Leviticus 26 are the hinge on
which Israel's entire future swings.
"""

CHAPTERS = [
    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 23 — THE APPOINTED FEASTS (MO'ADIM)
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-23",
        "ref": "Leviticus 23",
        "chapter_num": 23,
        "title": "The Appointed Times — God's Prophetic Calendar",
        "era": "calendar",
        "type": "chapter",

        "synopsis": (
            "Leviticus 23 presents the complete festival calendar of Israel — seven appointed "
            "times (mo'adim) that structure the entire worship year. The Hebrew word mo'ed "
            "(plural mo'adim) means 'appointed time/meeting' — the same word used for the "
            "Tent of Meeting (ohel mo'ed). These are not arbitrary holidays but divine "
            "appointments — times when heaven and earth intersect with particular intensity. "
            "The seven feasts fall into two clusters separated by a gap: the Spring Feasts "
            "(Passover/Pesach, Unleavened Bread/Matzot, Firstfruits/Bikkurim, and "
            "Pentecost/Shavuot) and the Fall Feasts (Trumpets/Yom Teruah, Day of "
            "Atonement/Yom Kippur, and Tabernacles/Sukkot). The Sabbath is listed first "
            "as the foundational pattern: every seventh day, Israel ceases work and rests, "
            "re-enacting creation's seventh day. The Spring Feasts commemorate the Exodus "
            "(Passover = deliverance from Egypt, Unleavened Bread = the hasty departure, "
            "Firstfruits = the first harvest in the promised land, Pentecost = the giving "
            "of the Torah at Sinai). The Fall Feasts anticipate the consummation (Trumpets = "
            "the announcement of the coming king, Atonement = the final judgment and "
            "purification, Tabernacles = the eternal dwelling of God with his people). "
            "Christian theology reads the festivals as a prophetic timeline: Passover = "
            "the Cross (1 Cor 5:7), Firstfruits = the Resurrection (1 Cor 15:20), Pentecost "
            "= the coming of the Spirit (Acts 2), Trumpets = the return of Christ (1 Thess "
            "4:16), Atonement = the final judgment (Heb 9:27-28), Tabernacles = the "
            "eternal kingdom (Rev 21:3). The Spring Feasts were fulfilled at Christ's "
            "first coming, precisely on their calendar dates. The Fall Feasts await "
            "fulfillment at his second coming. The four-month gap between the Spring and "
            "Fall festivals corresponds to the present age — the church era between the "
            "Cross and the return."
        ),

        "key_verse": {
            "ref": "Leviticus 23:2",
            "text": "Speak to the people of Israel and say to them, These are the appointed feasts of the LORD that you shall proclaim as holy convocations; they are my appointed feasts.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "moed", "miqra_qodesh", "pesach", "matzot", "bikkurim",
            "shavuot", "teruah", "kippur", "sukkot", "lulav", "shabbat"
            # Key glosses: mo'ed = 'appointed time/meeting' (divine appointment
            # — same word as 'Tent of Meeting,' ohel mo'ed); miqra qodesh =
            # 'holy convocation/sacred assembly'; pesach = 'Passover' (from
            # pasach, 'to pass over/spare' — commemorating the Exodus); matzot =
            # 'unleavened bread' (7-day feast following Passover); bikkurim =
            # 'firstfruits' (the first sheaf of the harvest, waved before YHWH);
            # shavuot = 'Weeks/Pentecost' (50 days after Firstfruits — harvest
            # celebration, later associated with Torah-giving at Sinai); teruah =
            # 'trumpet blast/shout' (Yom Teruah, the Feast of Trumpets — later
            # Rosh Hashanah); kippur = 'atonement/purgation' (Yom Kippur);
            # sukkot = 'booths/tabernacles' (the 7-day feast of dwelling in
            # temporary shelters — joy and eschatological anticipation);
            # lulav = 'palm branch' (one of the four species waved at Sukkot);
            # shabbat = 'Sabbath/cessation' (the foundational weekly mo'ed)
        ],

        "ane_backdrop": (
            "Festival calendars are foundational to ANE religion. The Babylonian Akitu "
            "(New Year) festival was a multi-day celebration involving the recitation of "
            "Enuma Elish, a ritual humiliation and reinvestiture of the king, and the "
            "determination of destinies by the gods. The Ugaritic seasonal festivals "
            "correspond to agricultural cycles and include autumnal harvest celebrations "
            "parallel to Sukkot. Egyptian calendars mark festivals of Osiris, Horus, and "
            "other deities tied to the Nile's inundation cycle. The Israelite calendar is "
            "distinctive in several ways: (1) It commemorates historical events (Exodus), "
            "not mythological cycles. (2) It is centered on YHWH alone — no other deity "
            "receives a festival. (3) The Sabbath is uniquely Israelite — no other ANE "
            "culture observed a weekly day of rest with religious significance. (4) The "
            "festivals have eschatological orientation — they point forward, not merely "
            "backward. The Qumran community followed a 364-day solar calendar (1 Enoch, "
            "Jubilees) rather than the lunisolar calendar of mainstream Judaism, causing "
            "the festivals to fall on different dates — a major source of sectarian conflict."
        ),

        "second_temple": [
            {
                "source": "Jubilees 6:17-38",
                "summary": "Jubilees insists on a 364-day solar calendar and condemns "
                           "the lunar calendar as a corruption: 'They will observe the "
                           "festivals at the wrong time.'",
                "relevance": "The calendar was a defining sectarian issue in Second Temple "
                             "Judaism — Qumran, the Jubilees tradition, and mainstream "
                             "Judaism celebrated the feasts on different dates."
            },
            {
                "source": "Mishnah Mo'ed (entire order)",
                "summary": "An entire division of the Mishnah devoted to the festival "
                           "calendar — Shabbat, Pesachim, Sukkah, Yoma, Rosh Hashanah, "
                           "and more.",
                "relevance": "Shows the centrality of the festival calendar to rabbinic "
                             "Judaism — it generated more halakhic discussion than almost "
                             "any other topic."
            },
            {
                "source": "11QTemple 17-29",
                "summary": "The Temple Scroll provides an expanded festival calendar "
                           "including additional festivals not found in the Torah: a "
                           "Festival of New Wine and a Festival of New Oil.",
                "relevance": "Demonstrates that Qumran expanded the Leviticus 23 calendar "
                             "with additional appointed times, reflecting their solar "
                             "calendar framework."
            }
        ],

        "cross_refs": [
            {"ref": "1 Corinthians 5:7", "note": "'Christ, our Passover lamb, has been sacrificed' — Passover fulfilled at the Cross", "type": "nt"},
            {"ref": "1 Corinthians 15:20, 23", "note": "'Christ has been raised from the dead, the firstfruits of those who have fallen asleep' — Firstfruits fulfilled in the Resurrection", "type": "nt"},
            {"ref": "Acts 2:1-4", "note": "The Spirit descends on the day of Pentecost (Shavuot) — the feast of harvest/Torah-giving fulfilled by the Spirit", "type": "nt"},
            {"ref": "1 Thessalonians 4:16", "note": "'The Lord himself will descend from heaven with a cry of command, with the voice of an archangel, and with the sound of the trumpet of God' — Yom Teruah", "type": "nt"},
            {"ref": "Hebrews 9:27-28", "note": "'Christ, having been offered once to bear the sins of many, will appear a second time, not to deal with sin but to save' — Yom Kippur's fulfillment", "type": "nt"},
            {"ref": "Revelation 21:3", "note": "'Behold, the dwelling place of God is with man. He will dwell (tabernacle) with them' — Sukkot's ultimate fulfillment", "type": "nt"},
            {"ref": "John 7:37-39", "note": "On the last day of Sukkot, Jesus cries 'If anyone thirsts, let him come to me and drink' — the water ceremony of Tabernacles", "type": "nt"},
            {"ref": "Colossians 2:16-17", "note": "Paul: the festivals are 'a shadow of the things to come, but the substance belongs to Christ'", "type": "nt"},
            {"ref": "Zechariah 14:16-19", "note": "In the messianic age, all nations will come to Jerusalem to celebrate Sukkot — the festival universalized", "type": "ot"}
        ],

        "divine_council_note": (
            "The mo'adim ('appointed times') are meetings between heaven and earth — the "
            "very word mo'ed is the same as 'tent of meeting' (ohel mo'ed). These are "
            "scheduled intersections of the divine and human realms — cosmic appointments "
            "when heaven's calendar and earth's calendar align. In the divine council "
            "framework, the festivals mark the moments when YHWH's governance of Israel "
            "is most visibly enacted. The Spring Feasts trace the story of redemption "
            "from bondage (the nations under corrupt elohim) to covenant community "
            "(Israel gathered at Sinai, YHWH's own portion). The Fall Feasts — Trumpets, "
            "Atonement, Tabernacles — anticipate the final act of the cosmic drama: the "
            "trumpet announces the divine King's return to reclaim ALL nations from the "
            "corrupt council members (Ps 82:8, Rev 11:15), the Day of Atonement becomes "
            "the final judgment where all sin is dealt with permanently (including the "
            "Azazel dimension — the scapegoat's final journey, Rev 20:1-3), and Tabernacles "
            "becomes God's permanent dwelling with his people — heaven and earth fully "
            "reunited, the tabernacle vision made eternal (Rev 21:3). The prophetic "
            "calendar encodes the entire plan of redemption from the Exodus to the "
            "eschaton, from the council's corruption to its resolution."
        ),

        "sections": [
            {
                "title": "The Sabbath — The Foundation (23:1-3)",
                "content": (
                    "Before listing the annual feasts, YHWH establishes the Sabbath as the "
                    "foundational pattern: 'Six days shall work be done, but on the seventh "
                    "day is a Sabbath of solemn rest (shabbat shabbaton), a holy convocation "
                    "(miqra qodesh). You shall do no work.' The Sabbath is the first mo'ed, "
                    "the weekly rehearsal of the creation rest and the eschatological rest. "
                    "Every seven days, Israel practices what the eternal state will be: "
                    "cessation from labor, communion with God, trust that YHWH provides. "
                    "The Sabbath is listed separately and before the annual feasts because "
                    "it is the pattern that underlies all the others — the seven-day rhythm "
                    "generating the seven-feast structure."
                )
            },
            {
                "title": "The Spring Feasts: Passover, Unleavened Bread, Firstfruits (23:4-14)",
                "content": (
                    "Passover (Pesach): On the fourteenth day of the first month (Nisan/Aviv), "
                    "at twilight — the LORD's Passover. A lamb is slaughtered and its blood "
                    "commemorates deliverance from Egypt (Exodus 12). Unleavened Bread (Matzot): "
                    "beginning on the fifteenth of Nisan, seven days of eating matzot. The first "
                    "and seventh days are holy convocations with no regular work. Leaven "
                    "represents the old life in Egypt — removing it symbolizes the break with "
                    "slavery. Firstfruits (Bikkurim): on 'the day after the Sabbath' (debated "
                    "whether this means the day after the weekly Sabbath during Unleavened Bread "
                    "or the day after the festival sabbath), a sheaf of the first grain is waved "
                    "before the LORD. Until this offering, no new grain may be eaten. Christ "
                    "was crucified on Passover (Nisan 14), buried during Unleavened Bread, and "
                    "raised on Firstfruits — 'the firstfruits of those who have fallen asleep' "
                    "(1 Cor 15:20). The Spring Feasts were fulfilled precisely on their "
                    "appointed dates."
                )
            },
            {
                "title": "Pentecost / Feast of Weeks (23:15-22)",
                "content": (
                    "From the day of the Firstfruits wave offering, count seven complete weeks "
                    "(49 days) — the fiftieth day (pentecoste in Greek, hence 'Pentecost') is "
                    "the Feast of Weeks (Shavuot). Two loaves of bread made WITH leaven are "
                    "waved before the LORD — unique among the offerings, which normally exclude "
                    "leaven. This is accompanied by seven lambs, one bull, and two rams as "
                    "burnt offerings, a male goat as sin offering, and two male lambs as peace "
                    "offerings. Jewish tradition connects Shavuot to the giving of the Torah "
                    "at Sinai (Exodus 19:1 places Israel at Sinai in the third month, aligning "
                    "with Shavuot). The leavened loaves may represent the inclusion of Gentiles "
                    "(who, unlike Israel, carry 'leaven') in the harvest. The gleaning provision "
                    "for the poor is reiterated (23:22) — even in celebration, provision for "
                    "the vulnerable is mandatory. Acts 2: the Spirit descends on Shavuot, "
                    "the Torah is written on hearts (Jer 31:33), and the first harvest of "
                    "believers is gathered."
                )
            },
            {
                "title": "The Fall Feasts: Trumpets, Atonement, Tabernacles (23:23-43)",
                "content": (
                    "Trumpets (Yom Teruah): the first day of the seventh month (Tishri 1) — "
                    "a holy convocation with trumpet blasts (teruah). No regular work. The "
                    "nature of the teruah is debated: shofar blasts, alarm signals, or shouts "
                    "of acclamation. Later tradition calls this Rosh Hashanah (New Year). In "
                    "prophetic typology, the trumpet announces the King's coming (1 Thess 4:16, "
                    "Rev 11:15). Day of Atonement (Yom Kippur): Tishri 10 — already detailed "
                    "in chapter 16. Here the emphasis is on self-denial (innui nefesh — fasting) "
                    "and absolute rest. Anyone who works or does not afflict themselves is 'cut "
                    "off' or 'destroyed.' Tabernacles (Sukkot): beginning Tishri 15, seven days "
                    "of living in booths (sukkot) made of branches, commemorating the wilderness "
                    "wandering. The first day is a holy convocation; the eighth day (Shemini "
                    "Atzeret) is a solemn assembly. The four species are taken: fruit of "
                    "'splendid trees' (etrog/citron), palm branches (lulav), leafy branches "
                    "(myrtle), and willows (aravot). Sukkot is the feast of pure joy — 'you "
                    "shall rejoice before the LORD your God seven days' (23:40). In Zechariah "
                    "14:16-19, all nations will celebrate Sukkot in the messianic age — the "
                    "feast universalized. Revelation 21:3: God 'will tabernacle (skenoo) "
                    "with them' — the eternal Sukkot."
                )
            },
            {
                "title": "The Prophetic Structure: Already and Not Yet",
                "content": (
                    "The seven feasts form a complete prophetic narrative. The Spring Feasts "
                    "(Passover, Unleavened Bread, Firstfruits, Pentecost) were fulfilled at "
                    "Christ's first coming — and fulfilled precisely on their respective "
                    "calendar dates. Jesus was crucified on Passover (1 Cor 5:7), buried "
                    "during Unleavened Bread, raised on Firstfruits (1 Cor 15:20), and sent "
                    "the Spirit on Pentecost (Acts 2). The Fall Feasts (Trumpets, Atonement, "
                    "Tabernacles) await fulfillment at his second coming. Trumpets anticipates "
                    "the trumpet of God announcing Christ's return (1 Thess 4:16). Atonement "
                    "anticipates the final judgment when sin is dealt with completely. "
                    "Tabernacles anticipates the eternal dwelling of God with humanity — no "
                    "more temporary booths but a permanent abode. The four-month gap between "
                    "Spring and Fall feasts corresponds to the present 'church age' — the "
                    "already-fulfilled promises and the not-yet-fulfilled promises with the "
                    "current era stretching between them."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 24 — THE LAMPSTAND, THE BREAD, AND THE BLASPHEMER
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-24",
        "ref": "Leviticus 24",
        "chapter_num": 24,
        "title": "Light, Bread, and Blasphemy — Sacred Order and Its Violation",
        "era": "calendar",
        "type": "chapter",

        "synopsis": (
            "Leviticus 24 contains two sections that seem unrelated but are theologically "
            "connected: (1) instructions for the perpetual lampstand and the bread of the "
            "Presence (24:1-9), and (2) the case of the blasphemer and the lex talionis "
            "(24:10-23). The first section commands the Israelites to bring pure beaten "
            "olive oil for the lampstand (menorah), which Aaron must keep burning 'from "
            "evening to morning before the LORD regularly' — a perpetual statute. Then the "
            "twelve loaves of the bread of the Presence (lechem ha-panim, literally 'bread "
            "of the face/presence') are arranged in two rows of six on the pure gold table "
            "before the LORD. Fresh loaves are set out every Sabbath; the old loaves belong "
            "to Aaron and his sons, eaten in a holy place. The second section narrates the "
            "only legal case in Leviticus: a man of mixed parentage (Israelite mother, "
            "Egyptian father) blasphemes the Name (ha-Shem) and curses. He is brought to "
            "Moses, who inquires of YHWH. The verdict: the congregation must take him outside "
            "the camp; the witnesses lay their hands on his head; the entire congregation "
            "stones him. This leads to the articulation of the lex talionis: 'Whoever takes "
            "a human life shall surely be put to death... fracture for fracture, eye for eye, "
            "tooth for tooth' (24:17-20). The same standard applies to the native and the "
            "sojourner. The connection between the sections: the lampstand and showbread "
            "represent the perpetual maintenance of God's sacred order; the blasphemy case "
            "represents its violation. The perpetual light and bread sustain the divine-human "
            "relationship; blasphemy tears it apart."
        ),

        "key_verse": {
            "ref": "Leviticus 24:16",
            "text": "Whoever blasphemes the name of the LORD shall surely be put to death. All the congregation shall stone him. The sojourner as well as the native, when he blasphemes the Name, shall be put to death.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "menorah", "lechem_hapanim", "shemen_zayit",
            "ha_Shem", "naqav", "qalal", "ayin_tachat_ayin", "ger"
            # Key glosses: menorah = 'lampstand' (7-branched golden candelabrum
            # — symbolizing creation's completeness, the light of God's presence);
            # lechem ha-panim = 'bread of the Presence/Face' (lit. 'bread of the
            # face' — 12 loaves representing the 12 tribes continuously before
            # YHWH); shemen zayit = 'olive oil' (pure beaten oil for the lamp);
            # ha-Shem = 'the Name' (YHWH — the sacred divine name that must not
            # be blasphemed); naqav = 'to pierce/blaspheme' (to profane the
            # Name); qalal = 'to curse/make light of'; ayin tachat ayin = 'eye
            # for eye' (lex talionis — proportional justice, limiting rather than
            # encouraging retaliation)
        ],

        "ane_backdrop": (
            "Sacred lamps and offering tables are universal in ANE temples. Egyptian temples "
            "maintained perpetual lamps fueled by oil — the lamp before Amun at Karnak was "
            "never allowed to go out. Mesopotamian temples placed tables of offering bread "
            "before the divine image daily. The Ugaritic texts describe a 'table of offering' "
            "(tlhn) before the gods. The Levitical menorah and showbread serve parallel "
            "functions but without a cult image — YHWH has no image, so the light and bread "
            "are set 'before the LORD' in the empty space above the kapporet where YHWH's "
            "presence manifests. The lex talionis (eye for eye) is famously paralleled in "
            "the Code of Hammurabi (Laws 196-197), the Eshnunna Laws (Laws 42-47), and "
            "Middle Assyrian Laws. In all these codes, the principle is proportional justice: "
            "the punishment must match the crime, no more and no less."
        ),

        "second_temple": [
            {
                "source": "Josephus, Antiquities III.6.7",
                "summary": "Josephus describes the menorah and showbread table in the "
                           "Second Temple, noting that the lamp burned day and night and "
                           "the bread was changed every Sabbath.",
                "relevance": "Eyewitness account of the perpetual lamp and bread practice "
                             "as maintained in the Herodian temple."
            },
            {
                "source": "Mishnah Menachot 11:1-9",
                "summary": "Detailed description of the showbread preparation: the baking, "
                           "the arrangement, the replacement protocol, and the priestly "
                           "consumption.",
                "relevance": "Preserves the operational details of how the showbread was "
                             "actually handled in the Second Temple — information Leviticus "
                             "leaves unspecified."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 5:38-39", "note": "Jesus quotes the lex talionis and transforms it: 'Do not resist the one who is evil. But if anyone slaps you on the right cheek, turn to him the other also'", "type": "nt"},
            {"ref": "John 8:12", "note": "'I am the light of the world' — Jesus fulfills the perpetual lampstand", "type": "nt"},
            {"ref": "John 6:35", "note": "'I am the bread of life' — Jesus fulfills the bread of the Presence", "type": "nt"},
            {"ref": "1 Samuel 21:6", "note": "David eats the holy bread of the Presence — Jesus cites this in Mark 2:25-26 to establish mercy over rigid ceremony", "type": "ot"},
            {"ref": "Revelation 1:12-13, 20", "note": "The seven golden lampstands = the seven churches — the menorah imagery in the Apocalypse", "type": "nt"},
            {"ref": "Exodus 25:23-30, 31-40", "note": "The original instructions for the table and menorah — Leviticus 24 provides the perpetual maintenance protocol", "type": "ot"},
            {"ref": "Hebrews 9:1-5", "note": "Lists the furnishings of the earthly sanctuary — 'the lampstand and the table and the bread of the Presence' — which are copies of heavenly realities", "type": "nt"}
        ],

        "divine_council_note": (
            "The menorah and showbread represent the continuous maintenance of the "
            "divine-human interface. The light burns perpetually before YHWH — the earthly "
            "counterpart of the light that surrounds the heavenly throne (Ezek 1:27-28, "
            "Rev 4:5). The bread 'before the face' (panim) of YHWH symbolizes the ongoing "
            "covenant relationship between God and the twelve tribes. The blasphemy of the "
            "Name is the polar opposite — the deliberate profanation of the covenant "
            "foundation. In the divine council framework, the Name (ha-Shem) carries the "
            "power of the divine identity; cursing the Name is an assault on YHWH's "
            "authority in his own domain."
        ),

        "sections": [
            {
                "title": "The Perpetual Lampstand (24:1-4)",
                "content": (
                    "The Israelites are commanded to bring pure beaten olive oil (shemen "
                    "zayit zakh katit) for the light, to keep the lamp burning 'from "
                    "evening to morning before the LORD regularly' — a perpetual statute "
                    "(chuqqat olam). Aaron tends it in the Tent of Meeting, 'outside the "
                    "veil' — in the Holy Place, not the Most Holy Place. The menorah's "
                    "seven branches represent completeness and creation. The light before "
                    "YHWH maintains the visible presence of life and order in the sanctuary. "
                    "As the altar fire must never go out (6:13), the lamp must never go dark. "
                    "Both represent the perpetual connection between God and his people — "
                    "fire ascending (altar) and light shining (lampstand), the two directions "
                    "of the divine-human relationship."
                )
            },
            {
                "title": "The Bread of the Presence (24:5-9)",
                "content": (
                    "Twelve cakes of fine flour are baked — two-tenths of an ephah each. "
                    "They are set in two rows of six on the pure gold table. Frankincense "
                    "is placed on each row as a memorial portion (azkarah) — burned on the "
                    "altar when the bread is replaced. Every Sabbath, fresh bread replaces "
                    "the old, which becomes food for Aaron and his sons, eaten in a holy "
                    "place as 'most holy.' The twelve loaves represent the twelve tribes — "
                    "all Israel is continuously 'before the face' (panim) of YHWH. The "
                    "Sabbath replacement creates a weekly rhythm of renewal. The bread of "
                    "the Presence is the covenant table set for God and his people — a "
                    "permanent invitation to fellowship."
                )
            },
            {
                "title": "The Blasphemer's Case (24:10-16)",
                "content": (
                    "A man born of an Israelite mother and an Egyptian father gets into a "
                    "fight in the camp. During the altercation, he 'blasphemes the Name' "
                    "(vayyiqqov et ha-Shem) and 'curses' (vayeqallel). He is brought to "
                    "Moses; Moses inquires of YHWH. The verdict: bring him outside the camp; "
                    "all who heard lay their hands on his head (transferring the curse back "
                    "to him); the entire congregation stones him. The law is then generalized: "
                    "'Whoever curses (yeqallel) his God shall bear his sin. Whoever blasphemes "
                    "(noqev) the name of the LORD shall surely be put to death.' This applies "
                    "equally to native and sojourner. The hand-laying by witnesses is a "
                    "ritual transfer — the community divests itself of the pollution the "
                    "blasphemy created. Execution outside the camp removes the contamination "
                    "from the community's sacred space."
                )
            },
            {
                "title": "The Lex Talionis: Proportional Justice (24:17-23)",
                "content": (
                    "From the blasphemy case, the text derives the broader principle of "
                    "proportional justice: 'Whoever takes a human life shall surely be put "
                    "to death. Whoever takes an animal's life shall make it good, life for "
                    "life. If anyone injures his neighbor... fracture for fracture, eye for "
                    "eye, tooth for tooth' (24:17-20). The same standard applies to the "
                    "sojourner and the native — equal justice regardless of ethnic origin. "
                    "The lex talionis is not a mandate for personal revenge but a judicial "
                    "principle: the punishment must fit the crime. It limits retaliation — "
                    "you may not take a life for an eye or destroy a family for a tooth. "
                    "Jesus (Matt 5:38-39) does not contradict this judicial principle but "
                    "addresses personal relationships: the individual may choose mercy "
                    "even when justice permits retaliation."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 25 — SABBATICAL YEAR AND JUBILEE
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-25",
        "ref": "Leviticus 25",
        "chapter_num": 25,
        "title": "Sabbath for the Land — The Jubilee Vision",
        "era": "calendar",
        "type": "chapter",

        "synopsis": (
            "Leviticus 25 extends the Sabbath principle from the weekly rhythm (one day in "
            "seven) to the agricultural cycle (one year in seven) and then to the grand "
            "Jubilee cycle (the fiftieth year after seven sevens). The Sabbatical Year "
            "(shemittah) requires that every seventh year the land lies fallow: no sowing, "
            "no pruning, no harvesting what grows of itself as a private crop. Whatever the "
            "land produces voluntarily is common property — for the landowner, servants, "
            "hired workers, sojourners, livestock, and wild animals alike. The Jubilee Year "
            "(yovel) occurs after seven Sabbatical cycles — the fiftieth year. It is "
            "announced on the Day of Atonement (Tishri 10) with the blast of the trumpet "
            "(shofar/yovel). Three provisions define the Jubilee: (1) All agricultural land "
            "reverts to its original tribal/family owners — land cannot be permanently sold "
            "because 'the land is mine; for you are strangers and sojourners with me' (25:23). "
            "(2) All Israelite debt-slaves are released and return to their families and "
            "ancestral properties. (3) All debts are released. The Jubilee vision is "
            "revolutionary — a systematic economic reset that prevents permanent inequality, "
            "landlessness, and debt bondage. It is the most radical socioeconomic legislation "
            "in the ancient world. Land prices are calculated based on the number of crop "
            "years remaining until the next Jubilee — you are not buying the land but the "
            "number of harvests. The chapter includes detailed provisions for redeeming "
            "property (kinsman-redeemer, go'el), houses in walled cities (redeemable for "
            "one year only), Levitical property (always redeemable), lending without interest "
            "to fellow Israelites, and the treatment of Israelite versus non-Israelite "
            "servants. The theological foundation is stated twice: 'The land is mine' (25:23) "
            "and 'They are my servants, whom I brought out of Egypt; they shall not be sold "
            "as slaves' (25:42). Both land and people belong to YHWH — Israel is a tenant on "
            "God's land and a servant of God alone."
        ),

        "key_verse": {
            "ref": "Leviticus 25:10",
            "text": "And you shall consecrate the fiftieth year, and proclaim liberty throughout the land to all its inhabitants. It shall be a jubilee for you, when each of you shall return to his property and each of you shall return to his clan.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "shemittah", "yovel", "deror", "goel",
            "geullah", "shofar", "neshekh", "achuzzah", "eved"
            # Key glosses: shemittah = 'release/remission' (the sabbatical year
            # — every 7th year the land lies fallow); yovel = 'jubilee/ram's
            # horn' (the 50th year — proclaimed by shofar blast, all land reverts,
            # all Israelite slaves freed); deror = 'liberty/release' (proclaimed
            # at Jubilee — the word inscribed on the Liberty Bell); go'el =
            # 'kinsman-redeemer' (the family member who buys back lost property
            # or frees an enslaved relative — YHWH is Israel's ultimate go'el,
            # Isa 41:14); ge'ullah = 'redemption/right of redemption'; shofar =
            # 'ram's horn trumpet' (announces the Jubilee on Yom Kippur);
            # neshekh = 'interest/usury' (lit. 'bite' — forbidden on loans to
            # fellow Israelites); achuzzah = 'hereditary property/possession';
            # eved = 'servant/slave' (an Israelite eved is technically a bonded
            # laborer, not a chattel slave — freed at Jubilee)
        ],

        "ane_backdrop": (
            "Periodic royal debt releases (andurarum/misharum) are attested in Mesopotamia "
            "from the Old Babylonian period onward. Ammisaduqa's Edict (c. 1646 BC) is a "
            "royal debt release that cancels certain debts and frees certain categories of "
            "debt-slaves — the closest ANE parallel to the Jubilee. However, these are "
            "one-time royal acts of grace, not institutionalized cycles. The Levitical "
            "system makes the reset automatic and calendrical — it occurs whether the king "
            "wills it or not, because YHWH commands it. The fallow year concept has parallels "
            "in Roman agriculture (the ager compascuus) and in Greek practice, but the "
            "combination of fallow year + debt release + slave emancipation + land return is "
            "unparalleled. The kinsman-redeemer (go'el) institution has Mesopotamian parallels "
            "in family redemption rights but is given broader theological significance in "
            "Leviticus — YHWH himself is Israel's ultimate go'el (Isa 41:14, 44:6)."
        ),

        "second_temple": [
            {
                "source": "Isaiah 61:1-2",
                "summary": "The anointed one proclaims 'liberty (deror) to the captives' "
                           "and 'the year of the LORD's favor' — Jubilee language applied "
                           "to the messianic mission.",
                "relevance": "Jesus reads this passage in Luke 4:18-21 and declares 'Today "
                             "this Scripture has been fulfilled' — he IS the Jubilee."
            },
            {
                "source": "11Q13 (Melchizedek Scroll)",
                "summary": "A Qumran text that interprets the Jubilee eschatologically: "
                           "Melchizedek will execute the final Jubilee, releasing captives "
                           "from Belial's dominion and executing judgment on the wicked.",
                "relevance": "Shows that the Qumran community read the Jubilee as an "
                             "eschatological event — the ultimate release from bondage "
                             "and the final judgment, administered by a heavenly priest-figure."
            },
            {
                "source": "Josephus, Antiquities III.12.3",
                "summary": "Josephus describes the Jubilee as a time when 'every debtor "
                           "shall be released from their debts and every slave set free.'",
                "relevance": "Confirms first-century understanding of the Jubilee as both "
                             "an economic and a liberatory institution."
            }
        ],

        "cross_refs": [
            {"ref": "Luke 4:18-21", "note": "Jesus reads Isaiah 61 in the Nazareth synagogue and declares the Jubilee fulfilled — 'Today this Scripture has been fulfilled in your hearing'", "type": "nt"},
            {"ref": "Isaiah 61:1-2", "note": "'The Spirit of the Lord GOD is upon me... to proclaim liberty to the captives and the year of the LORD's favor' — the messianic Jubilee", "type": "ot"},
            {"ref": "Ruth 4:1-12", "note": "Boaz as the kinsman-redeemer (go'el) — the Leviticus 25 redemption principle in narrative application", "type": "ot"},
            {"ref": "Galatians 5:1", "note": "'For freedom Christ has set us free' — the spiritual Jubilee accomplished in Christ", "type": "nt"},
            {"ref": "Jeremiah 34:8-22", "note": "Zedekiah proclaims a Jubilee-like release but the owners reclaim their slaves — judgment follows for covenant violation", "type": "ot"},
            {"ref": "2 Chronicles 36:21", "note": "The exile lasts 70 years 'to fulfill the word of the LORD by Jeremiah, until the land had enjoyed its Sabbaths' — the land finally rests", "type": "ot"},
            {"ref": "Nehemiah 5:1-13", "note": "Nehemiah enforces the prohibition of interest-lending among Israelites — applying Leviticus 25:36-37", "type": "ot"},
            {"ref": "Hebrews 11:13-16", "note": "'They acknowledged that they were strangers and exiles on the earth... they desire a better country, that is, a heavenly one' — the Lev 25:23 principle ('you are strangers and sojourners with me') applied to the entire life of faith", "type": "nt"}
        ],

        "divine_council_note": (
            "The Jubilee vision is the socioeconomic expression of YHWH's sole sovereignty. "
            "The land belongs to YHWH (25:23) — Israel is a tenant. The people belong to "
            "YHWH (25:42) — no Israelite can permanently enslave another Israelite because "
            "they are all YHWH's servants. In the divine council framework, this is the "
            "contrast with the nations: under the corrupt elohim, the nations developed "
            "systems of permanent exploitation. Under YHWH, systemic exploitation is "
            "periodically reset. The 11Q13 Melchizedek Scroll explicitly connects the "
            "Jubilee to eschatological deliverance from Belial — the final Jubilee is "
            "cosmic liberation from the powers of darkness."
        ),

        "sections": [
            {
                "title": "The Sabbatical Year (25:1-7)",
                "content": (
                    "Every seventh year, the land observes a 'Sabbath to the LORD' (shabbat "
                    "la-YHWH). No sowing, no pruning, no organized harvesting. What grows "
                    "voluntarily is common food — for the owner, servants, hired workers, "
                    "sojourners, livestock, and wild animals. The land itself rests. This "
                    "requires radical trust: Israel must depend on YHWH's provision rather "
                    "than their own labor. God promises to provide a triple harvest in the "
                    "sixth year (25:21). The Sabbatical year teaches that the land's productivity "
                    "is God's gift, not human achievement. 2 Chronicles 36:21 says the exile "
                    "lasted seventy years so the land could 'enjoy its Sabbaths' — Israel's "
                    "failure to observe the Sabbatical years resulted in the land enforcing "
                    "its own rest."
                )
            },
            {
                "title": "The Year of Jubilee (25:8-17)",
                "content": (
                    "After seven Sabbatical cycles (49 years), the fiftieth year is the Jubilee "
                    "(yovel — from the ram's horn used to announce it). On the Day of Atonement "
                    "(Tishri 10), the trumpet sounds throughout the land. 'Proclaim liberty "
                    "(deror) throughout the land to all its inhabitants' (25:10) — this verse "
                    "is inscribed on the Liberty Bell in Philadelphia. Three provisions: "
                    "land returns to its original family, debt-slaves are freed, debts are "
                    "canceled. Land prices are calculated by the number of harvests remaining "
                    "until Jubilee — the buyer purchases crops, not the land itself. 'You "
                    "shall not wrong one another, but you shall fear your God' (25:17). The "
                    "Jubilee announces that YHWH's economy is fundamentally different from "
                    "the exploitative systems of the nations."
                )
            },
            {
                "title": "The Land Belongs to God (25:18-28)",
                "content": (
                    "God promises abundance in the sixth year to cover the Sabbatical and "
                    "Jubilee years. The foundational principle: 'The land shall not be sold "
                    "in perpetuity, for the land is mine. For you are strangers and sojourners "
                    "with me' (25:23). Israel does not own the land — they are guests on "
                    "YHWH's property. Land may be 'sold' (actually leased) but a kinsman-redeemer "
                    "(go'el) has the right to buy it back at any time, and in the Jubilee "
                    "it returns automatically. The go'el institution protects family "
                    "inheritance and prevents permanent landlessness. YHWH himself is "
                    "Israel's ultimate go'el — he redeems what was lost."
                )
            },
            {
                "title": "Houses, Levites, and Lending (25:29-38)",
                "content": (
                    "Houses in walled cities have different rules: the seller has one year "
                    "to redeem; after that, the house belongs permanently to the buyer and "
                    "does not revert at Jubilee. Village houses (no wall) follow the land "
                    "rules — they revert at Jubilee. Levitical houses in Levitical cities "
                    "are always redeemable and always revert — the Levites' permanent "
                    "inheritance must be protected because they have no agricultural land. "
                    "Lending to fellow Israelites must be interest-free (no neshekh — 'bite' "
                    "— usury, no tarbit — 'increase'). The motivation: 'I am the LORD your "
                    "God, who brought you out of the land of Egypt... to be your God' — "
                    "economic ethics are grounded in redemption theology."
                )
            },
            {
                "title": "Servitude and YHWH's Ownership of Israel (25:39-55)",
                "content": (
                    "An Israelite who falls into debt may serve as a laborer but must not "
                    "be treated as a slave (eved) — 'he shall be with you as a hired worker' "
                    "(25:40). At the Jubilee, they and their children go free, returning to "
                    "their family property. The theological reasoning is explicit: 'For they "
                    "are my servants, whom I brought out of the land of Egypt; they shall "
                    "not be sold as slaves' (25:42). No Israelite can permanently own "
                    "another Israelite because YHWH already owns them all. Non-Israelite "
                    "slaves receive different treatment (25:44-46) — they may be permanent "
                    "property, a distinction modern readers find troubling but which reflects "
                    "the ancient framework of covenant-insider/outsider categories. Even so, "
                    "Israelite slave-owners must not rule with harshness (25:43, 46). The "
                    "chapter closes with the possibility of a go'el redeeming an Israelite "
                    "from foreign servitude — the kinsman-redeemer rescues the enslaved "
                    "family member."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 26 — COVENANT BLESSINGS AND CURSES
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-26",
        "ref": "Leviticus 26",
        "chapter_num": 26,
        "title": "The Covenant Climax — Blessings, Curses, and Restoration",
        "era": "calendar",
        "type": "chapter",

        "synopsis": (
            "Leviticus 26 is the climactic conclusion of the Holiness Code and, arguably, "
            "of the entire book. It presents the covenant in its starkest form: obey and "
            "be blessed (26:1-13), or disobey and be cursed (26:14-39). The blessings are "
            "glorious: rain in season, abundant harvests, peace in the land, victory over "
            "enemies, God's presence ('I will walk among you and will be your God, and you "
            "shall be my people,' 26:12), and multiplication. The curses escalate in five "
            "stages, each introduced by 'if despite this you will not listen to me' — terror, "
            "disease, crop failure, wild beasts, sword, plague, famine so severe that parents "
            "eat their children, destruction of cities and high places, desolation of the "
            "land, scattering among the nations, and perpetual fear in exile. The five-fold "
            "escalation structure (26:14-17, 18-20, 21-22, 23-26, 27-39) is a systematic "
            "intensification — each stage is triggered by continued refusal to repent after "
            "the previous stage. The curses are not arbitrary punishments but the organic "
            "consequences of rejecting the covenant: without YHWH's blessing, the land fails; "
            "without YHWH's protection, enemies prevail; without YHWH's presence, existence "
            "itself becomes fearful. Yet the chapter does not end with curses. In one of the "
            "most beautiful passages in the Torah, YHWH promises restoration: 'If they confess "
            "their iniquity... then I will remember my covenant with Jacob, and I will remember "
            "my covenant with Isaac, and I will remember my covenant with Abraham, and I will "
            "remember the land' (26:40-42). Even in exile, God will not reject or abhor them "
            "or break his covenant. The patriarchal covenant is the bedrock — it cannot be "
            "annulled by Israel's failure. Leviticus 26 is the theological lens through which "
            "the prophets interpret Israel's history: every judgment and every hope of "
            "restoration flows from this chapter."
        ),

        "key_verse": {
            "ref": "Leviticus 26:11-12",
            "text": "I will make my dwelling among you, and my soul shall not abhor you. And I will walk among you and will be your God, and you shall be my people.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "berakhah", "qelalah", "berit", "shalom", "galut",
            "vidui", "zakar", "orlah_lev", "shammah", "qeri"
            # Key glosses: berakhah = 'blessing' (divine favor flowing from
            # covenant faithfulness); qelalah = 'curse' (the consequences of
            # covenant violation — not divine spite but the organic result of
            # rejecting YHWH's protection); berit = 'covenant' (the binding
            # agreement between YHWH and Israel); shalom = 'peace/wholeness/
            # completeness' (not merely absence of war but the presence of
            # harmony); galut = 'exile/captivity' (removal from the land —
            # the ultimate curse); vidui = 'confession' (verbal acknowledgment
            # of sin — required for restoration, 26:40); zakar = 'to remember'
            # (God 'remembers' the patriarchal covenant — not that he forgot,
            # but that he acts on it); orlat lev = 'uncircumcised heart'
            # (a heart not yet surrendered to God — must be 'humbled' for
            # restoration); qeri = 'contrary/hostile' (walking in opposition
            # to God — triggers escalating judgment)
        ],

        "ane_backdrop": (
            "Covenant blessings and curses are a standard feature of ANE treaty documents. "
            "Hittite suzerainty treaties (14th-13th century BC) conclude with blessings for "
            "loyalty and curses for violation. The Vassal Treaties of Esarhaddon (672 BC) "
            "contain an extensive curse section strikingly similar to Leviticus 26 and "
            "Deuteronomy 28: disease, famine, enemies, exile, cannibalism. The five-fold "
            "escalation pattern in Leviticus 26 has a parallel in the Atrahasis Epic where "
            "the gods send increasingly severe punishments (plague, drought, famine, flood) "
            "in response to human disobedience. The uniquely Israelite element is the "
            "restoration clause: ANE treaties typically end with curses — no provision for "
            "repentance and renewal. Leviticus 26:40-45 offers what no human suzerain would: "
            "unconditional restoration based on the earlier covenant with the patriarchs."
        ),

        "second_temple": [
            {
                "source": "Daniel 9:4-19",
                "summary": "Daniel's prayer of confession draws directly on Leviticus 26: "
                           "acknowledging the curses have come because of covenant violation "
                           "and appealing to God's mercy for restoration.",
                "relevance": "Demonstrates that Leviticus 26 was the interpretive framework "
                             "for understanding the exile — Daniel reads Israel's history "
                             "through this chapter."
            },
            {
                "source": "4Q390 (Pseudo-Moses)",
                "summary": "A Qumran text that reinterprets the Leviticus 26 cycle of sin, "
                           "punishment, and restoration as applying to the Second Temple "
                           "period — the community is still in the curse phase.",
                "relevance": "Shows that the Qumran community read itself as still living "
                             "under the Leviticus 26 curses, even after the return from Babylon."
            },
            {
                "source": "Nehemiah 9:5-38",
                "summary": "The great confession prayer of Nehemiah reviews Israel's history "
                           "as a cycle of blessing-disobedience-curse-restoration, following "
                           "the Leviticus 26 pattern exactly.",
                "relevance": "Post-exilic Israel interprets its entire history through the "
                             "Leviticus 26 lens."
            }
        ],

        "cross_refs": [
            {"ref": "2 Corinthians 6:16", "note": "Paul quotes Lev 26:12: 'I will walk among them, and I will be their God, and they shall be my people' — applied to the church", "type": "nt"},
            {"ref": "Revelation 21:3", "note": "'Behold, the dwelling place of God is with man. He will dwell with them, and they will be his people' — the ultimate fulfillment of Lev 26:11-12", "type": "nt"},
            {"ref": "Deuteronomy 28:1-68", "note": "The expanded parallel: Deuteronomy 28 provides an even longer blessings and curses section, building on Leviticus 26", "type": "ot"},
            {"ref": "2 Chronicles 7:14", "note": "'If my people... humble themselves and pray and seek my face and turn from their wicked ways, then I will hear from heaven and will forgive' — the restoration promise of Lev 26:40-42", "type": "ot"},
            {"ref": "Romans 11:1-2, 28-29", "note": "'God has not rejected his people... the gifts and the calling of God are irrevocable' — Paul affirming the Lev 26:44 principle", "type": "nt"},
            {"ref": "Jeremiah 31:31-34", "note": "'I will make a new covenant... I will put my law within them and write it on their hearts' — the ultimate restoration that Lev 26:40-45 anticipates", "type": "ot"},
            {"ref": "Lamentations 2:6-7", "note": "The destruction of Jerusalem described in the language of Leviticus 26 curses", "type": "ot"},
            {"ref": "Hebrews 8:6-13", "note": "The 'better covenant' with 'better promises' that Jeremiah 31 anticipated and Lev 26:40-45 foreshadowed — when the old covenant's curses are exhausted, the new covenant's restoration begins", "type": "nt"},
            {"ref": "Hebrews 10:16-17", "note": "'I will put my laws on their hearts and write them on their minds... I will remember their sins no more' — the ultimate fulfillment of the Lev 26:40-45 restoration promise through the new covenant", "type": "nt"},
            {"ref": "Hebrews 12:5-11", "note": "'The Lord disciplines the one he loves' — the five-stage discipline of Lev 26 reframed as fatherly correction, not punitive destruction", "type": "nt"}
        ],

        "divine_council_note": (
            "Leviticus 26 reveals the stakes of the divine-human covenant in the context "
            "of the divine council worldview. When Israel disobeys, God's presence withdraws "
            "— 'I will make your heavens like iron and your earth like bronze' (26:19). The "
            "blessings describe God's active presence: walking among them (26:12), the "
            "ultimate tabernacle experience — Eden restored, God dwelling with his people as "
            "he did in the garden (Gen 3:8). The curses describe progressive withdrawal of "
            "that presence, stage by stage, until the final curse: exile among the nations. "
            "In the Deuteronomy 32 framework, if Israel abandons YHWH, they become like "
            "the nations — effectively surrendered back to the corrupt elohim's dominion. "
            "The exile scatters Israel among those very nations, under those very gods. "
            "This is the ultimate humiliation: YHWH's chosen portion, living among the "
            "peoples allotted to the rebel council members. Yet the restoration promise "
            "(26:40-45) is anchored in the patriarchal covenant — the covenant that predates "
            "Sinai and does not depend on Israel's obedience. The Abrahamic covenant is "
            "unconditional; the Sinai covenant is conditional. When the conditional fails, "
            "the unconditional undergirds the restoration. This is the theological bedrock "
            "of Romans 11:28-29: 'the gifts and the calling of God are irrevocable.' YHWH "
            "will never permanently abandon his nachalah (inheritance/portion). The entire "
            "prophetic tradition — from Isaiah to Daniel to Revelation — builds on this "
            "promise: judgment is not the final word; restoration and the reclamation of "
            "all nations (Ps 82:8) is where the story ends."
        ),

        "sections": [
            {
                "title": "The Prologue: No Idols, Keep Sabbath (26:1-2)",
                "content": (
                    "Two prohibitions frame everything: 'You shall not make idols' and 'You "
                    "shall keep my Sabbaths and reverence my sanctuary.' These are the "
                    "foundational commitments: exclusive worship and temporal/spatial holiness. "
                    "Idolatry is the first step toward every curse; Sabbath-keeping is the "
                    "first sign of covenant faithfulness. The sanctuary (miqdash) represents "
                    "God's presence; reverencing it means honoring the divine-human interface. "
                    "Everything that follows — blessings and curses alike — flows from these "
                    "two principles."
                )
            },
            {
                "title": "The Covenant Blessings (26:3-13)",
                "content": (
                    "If Israel walks in YHWH's statutes: rain in season, abundant harvests "
                    "(threshing lasts until grape harvest, grape harvest until sowing — "
                    "uninterrupted abundance), bread to satisfaction, peace in the land "
                    "(no sword, no harmful beasts), victory over enemies (five chase a "
                    "hundred, a hundred chase ten thousand), multiplication ('I will turn "
                    "to you and make you fruitful'), establishment of the covenant, surplus "
                    "food (eating old stored grain while making room for the new). The climax: "
                    "'I will make my dwelling (mishkan) among you, and my soul shall not "
                    "abhor you. And I will walk among you and will be your God, and you shall "
                    "be my people' (26:11-12). This is Eden restored — God walking with his "
                    "people as he walked in the garden (Gen 3:8). The blessings are not "
                    "merely material but relational — God's presence IS the blessing."
                )
            },
            {
                "title": "The Five Escalating Curses (26:14-39)",
                "content": (
                    "Five cycles of judgment, each triggered by continued refusal to repent. "
                    "Stage 1 (26:14-17): sudden terror, wasting disease, fever, crop loss to "
                    "enemies, defeat in battle. Stage 2 (26:18-20): sevenfold punishment, "
                    "sky like iron, earth like bronze — drought and crop failure. Stage 3 "
                    "(26:21-22): wild beasts devouring children and livestock, roads deserted. "
                    "Stage 4 (26:23-26): sword executing covenant vengeance, plague within "
                    "cities, bread rationed so severely that ten women bake in one oven. "
                    "Stage 5 (26:27-39): cannibalism — parents eating their own children, "
                    "destruction of high places and incense altars, cities ruined, land "
                    "desolate, Israel scattered among the nations, perpetual fear in exile "
                    "— 'the sound of a driven leaf shall put them to flight' (26:36). The "
                    "escalation reveals YHWH's patience: each stage gives opportunity for "
                    "repentance before the next intensification. The curses are not divine "
                    "vindictiveness but the consequences of removing the covenant blessings."
                )
            },
            {
                "title": "The Restoration Promise (26:40-45)",
                "content": (
                    "Yet — even after the most extreme curses — YHWH offers restoration. "
                    "'If they confess their iniquity and the iniquity of their fathers in "
                    "their treachery... and also in walking contrary to me' (26:40). When "
                    "their 'uncircumcised heart' (orlat levavam) is humbled and they accept "
                    "the punishment of their iniquity, 'then I will remember my covenant "
                    "with Jacob, and I will remember my covenant with Isaac, and my covenant "
                    "with Abraham, and I will remember the land' (26:42). The covenants are "
                    "listed in reverse chronological order — Jacob, Isaac, Abraham — tracing "
                    "back to the most foundational promise. Even in the land of their enemies, "
                    "'I will not reject them or abhor them so as to destroy them utterly and "
                    "break my covenant with them, for I am the LORD their God' (26:44). This "
                    "is the bedrock of biblical hope: God's covenant faithfulness outlasts "
                    "human failure. The restoration is not earned by repentance alone but "
                    "guaranteed by God's unbreakable commitment."
                )
            },
            {
                "title": "The Colophon and the Prophetic Legacy (26:46)",
                "content": (
                    "'These are the statutes and rules and laws that the LORD made between "
                    "himself and the people of Israel through Moses on Mount Sinai.' This "
                    "verse closes the Holiness Code and, in many scholarly reconstructions, "
                    "the original conclusion of Leviticus (chapter 27 being an appendix). "
                    "The blessings and curses of Leviticus 26 became the interpretive "
                    "framework for all subsequent Israelite history. Every prophet who "
                    "announced judgment drew on this chapter. Every promise of restoration "
                    "echoed its language. Daniel 9, Nehemiah 9, and 2 Chronicles 7:14 all "
                    "apply Leviticus 26 to their historical situations. The chapter is not "
                    "merely legislation — it is prophecy. It tells Israel's story before "
                    "it happens."
                )
            }
        ]
    },

    # ══════════════════════════════════════════════════════════════════════
    # LEVITICUS 27 — VOWS, DEDICATIONS, AND VALUATIONS
    # ══════════════════════════════════════════════════════════════════════
    {
        "id": "lev-27",
        "ref": "Leviticus 27",
        "chapter_num": 27,
        "title": "Vows and Dedications — The Cost of Devotion",
        "era": "calendar",
        "type": "chapter",

        "synopsis": (
            "Leviticus 27, the final chapter of the book, addresses vows (nedarim) and "
            "dedications — voluntary acts of devotion in which a person, animal, house, or "
            "field is consecrated to YHWH. The chapter functions as an appendix to the main "
            "legislation, dealing with the practical question: what happens when someone "
            "makes a vow to dedicate something (or someone) to YHWH and then wants to "
            "redeem it? A system of monetary valuations is provided. Persons dedicated to "
            "YHWH are valued by age and sex: a male aged 20-60 at fifty silver shekels, a "
            "female at thirty, younger and older persons at progressively lower amounts, "
            "with special provision for those too poor to pay ('the priest shall value him "
            "according to what the vower can afford,' 27:8). Clean animals vowed to YHWH "
            "cannot be exchanged or substituted — if someone tries to switch a good animal "
            "for a bad one, BOTH become holy. Unclean animals can be redeemed with a "
            "one-fifth surcharge. Houses can be redeemed with one-fifth added. Land valuations "
            "are calculated based on the seed required to plant it (a homer of barley seed = "
            "fifty silver shekels for a full Jubilee cycle), adjusted for years remaining "
            "until Jubilee. Unredeemed dedicated fields become permanently priestly property "
            "at the Jubilee. The chapter distinguishes between voluntary dedications (which "
            "can be redeemed) and cherem — things irrevocably devoted to YHWH (which cannot "
            "be redeemed and, if a person, must be put to death). The tithe of the land — "
            "grain, fruit, livestock — is YHWH's and is holy. The livestock tithe is "
            "determined by counting: every tenth animal passing under the staff is YHWH's, "
            "regardless of quality. The book closes: 'These are the commandments that the "
            "LORD commanded Moses for the people of Israel on Mount Sinai' (27:34)."
        ),

        "key_verse": {
            "ref": "Leviticus 27:30",
            "text": "Every tithe of the land, whether of the seed of the land or of the fruit of the trees, is the LORD's; it is holy to the LORD.",
            "translation": "ESV"
        },

        "hebrew_terms": [
            "neder", "erekh", "cherem", "geullah",
            "maaser", "sheqel_haqqodesh", "chamishit", "qadosh", "haqdeish"
            # Key glosses: neder = 'vow' (a voluntary promise to God, binding
            # once spoken — Eccl 5:4-5); erekh = 'valuation/assessment' (the
            # monetary value assigned by the priest for redeeming a vowed
            # person or thing); cherem = 'devoted thing/ban' (irrevocably given
            # to God — cannot be redeemed or reclaimed; if a person, put to
            # death; the most extreme form of dedication); ge'ullah = 'right
            # of redemption' (the option to buy back what was vowed); ma'aser =
            # 'tithe/tenth' (one-tenth of all produce and livestock belongs to
            # YHWH as holy — obligatory, not voluntary); sheqel ha-qodesh =
            # 'sanctuary shekel' (the standard weight used for sacred
            # calculations — about 11.4 grams of silver); chamishit = 'one-
            # fifth/20%' (the surcharge for redeeming sacred things);
            # haqdeish = 'to consecrate/make holy' (to transfer from common
            # use to divine ownership)
        ],

        "ane_backdrop": (
            "Votive dedications and temple valuations are widely attested in the ANE. "
            "Mesopotamian temple records document detailed systems for dedicating persons, "
            "animals, and property to temple service, with corresponding monetary equivalents "
            "for redemption. Ugaritic texts record vows to Baal and other deities, including "
            "the dedication of children to temple service. The Levitical valuation system "
            "provides standardized rates rather than leaving them to priestly discretion, "
            "which is distinctive — it prevents exploitation of worshipers in a vulnerable "
            "emotional state. The cherem ('devoted thing') concept has parallels in the "
            "Moabite Mesha Stele, where the king 'devotes' captured cities and populations "
            "to his god Chemosh — total, irrevocable dedication to the deity, often involving "
            "destruction. The tithe (maaser — one-tenth) has parallels in Mesopotamian "
            "temple taxes and Neo-Babylonian tithe documents."
        ),

        "second_temple": [
            {
                "source": "Mishnah Arakhin 1-6",
                "summary": "An entire Mishnaic tractate devoted to the Leviticus 27 "
                           "valuation system — personal valuations, animal dedications, "
                           "field calculations, and redemption procedures.",
                "relevance": "Shows that the vow and valuation system remained a live "
                             "legal and theological topic in rabbinic Judaism."
            },
            {
                "source": "Numbers 30:1-16",
                "summary": "Provides additional legislation on vows, particularly "
                           "regarding women's vows and the authority of fathers and "
                           "husbands to annul them.",
                "relevance": "Expands the Leviticus 27 framework with gender-specific "
                             "provisions — the vow system was complex and carefully "
                             "regulated."
            },
            {
                "source": "Malachi 3:8-10",
                "summary": "'Will man rob God? Yet you are robbing me. In your tithes "
                           "and contributions... Bring the full tithe into the storehouse.'",
                "relevance": "The prophetic enforcement of the Leviticus 27:30-33 tithe "
                             "obligation — failure to tithe is covenant theft."
            }
        ],

        "cross_refs": [
            {"ref": "Matthew 23:23", "note": "Jesus criticizes Pharisees who tithe mint, dill, and cumin but neglect 'justice, mercy, and faithfulness' — affirming the tithe while prioritizing the weightier matters", "type": "nt"},
            {"ref": "Acts 5:1-11", "note": "Ananias and Sapphira dedicate property to God then withhold the price — violating the Leviticus 27 principle that what is vowed must be given", "type": "nt"},
            {"ref": "Judges 11:29-40", "note": "Jephthah's rash vow — the tragic narrative that illustrates why vow legislation is necessary", "type": "ot"},
            {"ref": "Ecclesiastes 5:4-5", "note": "'When you vow a vow to God, do not delay paying it... better that you should not vow than that you should vow and not pay'", "type": "ot"},
            {"ref": "1 Samuel 1:11, 24-28", "note": "Hannah's vow dedicating Samuel to YHWH — a person-dedication fulfilled without monetary redemption", "type": "ot"},
            {"ref": "Matthew 15:5-6", "note": "Jesus condemns using 'Corban' (dedicated to God) as an excuse to avoid caring for parents — abusing the vow system", "type": "nt"}
        ],

        "divine_council_note": (
            "The cherem ('devoted thing') concept connects to the divine council framework "
            "in its most severe form. Cherem represents total, irrevocable dedication to "
            "YHWH — nothing devoted under cherem can be redeemed. In the conquest narratives "
            "(Joshua 6-7), entire cities are placed under cherem — devoted to YHWH for "
            "destruction. Achan's violation of the cherem at Jericho brings disaster on all "
            "Israel. The principle: what belongs to YHWH is withdrawn from human use "
            "absolutely. In the cosmic framework, cherem represents the ultimate assertion "
            "of YHWH's sovereignty — certain things are so thoroughly God's that no human "
            "claim can touch them. The tithe operates on the same principle in milder form: "
            "one-tenth is YHWH's, permanently and non-negotiably."
        ),

        "sections": [
            {
                "title": "Valuation of Persons (27:1-8)",
                "content": (
                    "When someone makes a 'special vow' (yaphli neder) dedicating a person "
                    "to YHWH, the monetary valuation (erekh) is set by age and sex: male 20-60: "
                    "50 shekels; female 20-60: 30 shekels; male 5-20: 20 shekels; female 5-20: "
                    "10 shekels; male 1 month-5 years: 5 shekels; female 1 month-5 years: "
                    "3 shekels; male 60+: 15 shekels; female 60+: 10 shekels. These are "
                    "calculated by the sanctuary shekel standard. The differential valuations "
                    "likely reflect economic productivity rather than inherent worth — a "
                    "working-age male generates the most agricultural labor. The crucial "
                    "provision: 'if the person is too poor to pay the valuation, then he "
                    "shall be placed before the priest, and the priest shall value him "
                    "according to what the vower can afford' (27:8). No one's devotion is "
                    "priced out of reach."
                )
            },
            {
                "title": "Animals, Houses, and Fields (27:9-25)",
                "content": (
                    "Clean animals vowed to YHWH become holy and cannot be exchanged — any "
                    "attempt to substitute makes both animals holy. Unclean animals (not "
                    "suitable for sacrifice) are valued by the priest and can be redeemed "
                    "with a 20% surcharge. Houses follow the same pattern: priestly "
                    "valuation, redeemable with 20% added. Fields are valued by their "
                    "agricultural capacity — specifically by the seed needed to sow them. "
                    "If dedicated from the Jubilee year, the full value applies; if later, "
                    "the value is prorated by remaining years until Jubilee. If not redeemed "
                    "by the Jubilee, the field becomes permanent priestly property — it "
                    "never returns to the original family. A field that has already been "
                    "sold to another cannot be dedicated by the original owner — you cannot "
                    "dedicate what you do not possess. The 20% surcharge on redemption "
                    "ensures that the act of vowing carries real weight — getting out "
                    "costs more than getting in."
                )
            },
            {
                "title": "The Cherem — Irrevocable Devotion (27:28-29)",
                "content": (
                    "The cherem is the most extreme form of dedication: 'No devoted thing "
                    "(cherem) that a man devotes to the LORD, of anything that he has, "
                    "whether man or beast or of his inherited field, shall be sold or "
                    "redeemed; every devoted thing is most holy to the LORD' (27:28). Unlike "
                    "ordinary dedications (which can be redeemed), cherem is permanent and "
                    "total. 'No person devoted (cherem), who is to be devoted for destruction "
                    "from mankind, shall be ransomed; he shall surely be put to death' (27:29). "
                    "This verse is the legal foundation for the conquest cherem (Joshua 6-7) — "
                    "populations placed under the ban are irrevocably given to YHWH. The "
                    "severity is absolute: what enters the cherem category cannot return to "
                    "human use by any means. This represents the outer boundary of the "
                    "dedication spectrum — from the tithe (partial, regular) to the cherem "
                    "(total, irreversible)."
                )
            },
            {
                "title": "The Tithe (27:30-33)",
                "content": (
                    "Every tithe (maaser) of the land — grain and fruit — is YHWH's and "
                    "is holy. It may be redeemed with a 20% surcharge. The livestock tithe "
                    "follows a different procedure: the animals pass under a rod, and every "
                    "tenth animal is YHWH's — regardless of whether it is good or bad. If "
                    "the owner tries to substitute a different animal, both become holy. "
                    "The counting method prevents manipulation — you cannot cherry-pick the "
                    "runts for the tithe. The tenth belongs to God by right, not by human "
                    "choice. This is the foundational principle of the entire chapter: "
                    "everything belongs to YHWH, and the tithe is the minimum acknowledgment "
                    "of that truth. The vow and dedication system builds on this base — "
                    "the tithe is obligatory; additional dedications are voluntary acts of "
                    "devotion above the baseline."
                )
            },
            {
                "title": "The Final Colophon (27:34)",
                "content": (
                    "'These are the commandments that the LORD commanded Moses for the people "
                    "of Israel on Mount Sinai.' This closing verse frames the entire book as "
                    "Sinai revelation — divine legislation, not human invention. Leviticus "
                    "began with YHWH calling to Moses from the Tent of Meeting (1:1) and ends "
                    "with Moses transmitting YHWH's commands at Sinai (27:34). The book is "
                    "bracketed by divine speech — from first verse to last, this is God "
                    "telling Israel how to live in his presence. The Sinai reference connects "
                    "Leviticus to the broader Exodus-Numbers narrative: these instructions "
                    "were given during the year at the mountain, between the covenant "
                    "ratification (Exodus 24) and the departure for the promised land "
                    "(Numbers 10). They are the operating manual for a people who have "
                    "committed to dwelling with a holy God."
                )
            }
        ]
    }
]
