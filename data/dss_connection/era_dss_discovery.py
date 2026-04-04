"""
era_dss_discovery.py -- Part I: Discovery and Textual Evidence (Chapters 1-3)

1947: a Bedouin shepherd throws a rock into a cave near the Dead Sea and
shatters a clay jar containing scrolls that had been hidden for nearly
two thousand years. Over the next decade, eleven caves yield approximately
900 manuscripts — the single greatest archaeological discovery for biblical
studies. The Great Isaiah Scroll (1QIsa-a) is complete, 1000 years older
than any previously known Hebrew Isaiah manuscript, and the text is
remarkably stable. But the scrolls do more than confirm preservation —
they expose scribal alterations. The Deut 32:8 reading in 4QDeut-j
("sons of God" rather than "sons of Israel") unlocks the entire divine
council worldview. Two independent witnesses (DSS + LXX) against one (MT).
This is not a footnote — it is the key that opens the door.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: THE DISCOVERY THAT CHANGED EVERYTHING
    # =========================================================================
    {
        "id": "dss-discovery-caves",
        "ref": "Isaiah 40:8; Psalm 12:6-7",
        "chapter_num": 1,
        "title": "The Discovery That Changed Everything",
        "era": "dss_discovery",
        "type": "chapter",
        "themes": ['DSS', 'TEXTUAL', 'PRESERVATION', 'ARCHAEOLOGY'],

        "synopsis": "In 1947, a Bedouin shepherd named Muhammad edh-Dhib threw a rock "
                    "into a cave near Khirbet Qumran on the northwest shore of the Dead "
                    "Sea. The rock shattered a clay jar containing leather scrolls that "
                    "had been sealed for nearly two millennia. Cave 1 yielded seven "
                    "major scrolls: the Great Isaiah Scroll (1QIsa-a), a second partial "
                    "Isaiah scroll (1QIsa-b), the Community Rule (1QS), the War Scroll "
                    "(1QM), the Thanksgiving Hymns (1QH), the Genesis Apocryphon "
                    "(1QapGen), and the Habakkuk Pesher (1QpHab). Between 1948 and "
                    "1956, ten more caves were discovered — Cave 4 alone contained "
                    "fragments of over 500 manuscripts. The total: approximately 900 "
                    "manuscripts spanning biblical texts, sectarian compositions, and "
                    "previously known pseudepigraphal works. The significance cannot "
                    "be overstated. Before 1947, the oldest substantial Hebrew Bible "
                    "manuscript was the Aleppo Codex, dating to roughly 930 AD. The "
                    "Great Isaiah Scroll dates to approximately 125 BC — pushing our "
                    "witness back by over a thousand years. And the text was remarkably "
                    "stable. Not identical in every letter, but the variants are minor "
                    "and well-documented. [A] The word of God endures — 'The grass "
                    "withers, the flower fades, but the word of our God will stand "
                    "forever' (Isa 40:8).",

        "key_verse": {
            "ref": "Isaiah 40:8",
            "text": "The grass withers, the flower fades, but the word of our God will stand forever.",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "מְגִלָּה (megillah)",
                "meaning": "[A] 'Scroll' — from galal, 'to roll.' The primary format for sacred "
                           "texts in antiquity. The Dead Sea Scrolls were written on leather "
                           "(animal skin) and papyrus, rolled and stored in clay jars — the "
                           "same preservation method described in Jeremiah 32:14: 'Put them in "
                           "an earthenware vessel, that they may last for a long time.' The Great "
                           "Isaiah Scroll is 7.34 meters (24 feet) long, written on 17 sheets of "
                           "leather sewn together, containing all 66 chapters of Isaiah."
            },
            {
                "term": "כָּתַב (katav)",
                "meaning": "[A] 'To write' — the fundamental act of textual transmission. The "
                           "scribes at Qumran were professional copyists operating within a "
                           "tradition of careful transmission. Their manuscripts show corrections, "
                           "marginal notes, and textual variants that illuminate how the Hebrew "
                           "Bible was transmitted. Some corrections are by the original scribe, "
                           "others by later hands — revealing a living scribal tradition that "
                           "valued accuracy while allowing for editorial refinement."
            },
            {
                "term": "סֵפֶר (sepher)",
                "meaning": "[A] 'Book, document, writing' — from saphar, 'to count, to recount.' "
                           "Sepher encompasses both the physical document and the authority it "
                           "carries. The 'Book of the Torah' (sepher ha-Torah) found in Josiah's "
                           "temple (2 Kings 22:8) triggered national reformation. The scrolls "
                           "found at Qumran similarly transformed our understanding — not by "
                           "revealing new theology, but by confirming how faithfully the old "
                           "theology had been preserved."
            }
        ],

        "ane_backdrop": "The Dead Sea region's extreme aridity (rainfall under 50mm per year, "
                       "temperatures exceeding 50C) created natural preservation conditions "
                       "unmatched anywhere in the ancient Near East. Clay jars sealed with "
                       "pitch kept the leather and papyrus scrolls intact for roughly two "
                       "thousand years. Qumran itself was an isolated settlement — likely "
                       "an Essene community, though this identification is debated — situated "
                       "between the Judean wilderness and the Dead Sea. The community "
                       "apparently hid their library during the Roman advance of 68 AD, "
                       "during the First Jewish Revolt. The Romans destroyed the settlement "
                       "but never found the caves. The scrolls waited in darkness until "
                       "that stone flew from a shepherd's hand in 1947.",

        "second_temple": [
            {
                "source": "1QIsa-a (Great Isaiah Scroll)",
                "summary": "The complete scroll of Isaiah, dating to approximately 125 BC. "
                           "Contains all 66 chapters on 17 leather sheets. When compared to "
                           "the Masoretic Text (standardized ~600-900 AD), the agreement is "
                           "remarkable — roughly 95% identical. The 5% variation consists "
                           "mostly of spelling differences, minor word order changes, and "
                           "occasional scribal errors.",
                "relevance": "[A] This is the single most important manuscript for demonstrating "
                            "the fidelity of biblical transmission. A thousand-year gap in the "
                            "manuscript record — and the text held. Not perfectly, not without "
                            "any variation, but with a stability that stunned scholars who "
                            "expected far greater divergence.",
                "canon": False
            },
            {
                "source": "Jeremiah 32:14",
                "summary": "Jeremiah instructs Baruch: 'Put them in an earthenware vessel, "
                           "that they may last for a long time.' The prophet prescribes the "
                           "exact storage method — sealed clay jars — that would preserve "
                           "the Dead Sea Scrolls for two millennia.",
                "relevance": "[A] The preservation method used at Qumran was ancient, deliberate, "
                            "and effective. The community stored their texts for the long term, "
                            "and the desert conditions plus sealed jars kept them intact."
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 40:8", "note": "[A] 'The grass withers, the flower fades, but the word of our God will stand forever' — the DSS confirm this promise physically. The text endured a thousand years of copying with remarkable fidelity", "type": "ot"},
            {"ref": "Psalm 12:6-7", "note": "[A] 'The words of the LORD are pure words, like silver refined in a furnace on the ground, purified seven times. You, O LORD, will keep them; you will guard us from this generation forever' — the preservation of God's words through faithful transmission", "type": "ot"},
            {"ref": "Jeremiah 32:14", "note": "[A] 'Put them in an earthenware vessel, that they may last for a long time' — the exact preservation method used at Qumran: scrolls sealed in clay jars", "type": "ot"},
            {"ref": "Deuteronomy 31:24-26", "note": "[A] Moses commands the Levites to place the Book of the Law beside the ark of the covenant — the principle of authoritative text storage as a sacred obligation", "type": "ot"},
            {"ref": "2 Kings 22:8-13", "note": "[A] Hilkiah finds 'the Book of the Law in the house of the LORD' — a lost scroll discovered, triggering reformation. The DSS are the greatest parallel: lost scrolls rediscovered, transforming understanding", "type": "ot"},
            {"ref": "Matthew 5:18", "note": "[A] 'Until heaven and earth pass away, not an iota, not a dot, will pass from the Law' — Jesus' confidence in textual preservation, confirmed by the DSS evidence of scribal fidelity", "type": "nt"},
            {"ref": "1QIsa-a (Great Isaiah Scroll)", "note": "[C] Complete Isaiah scroll, ~125 BC, 1000+ years older than the Masoretic Text. Roughly 95% identical — the textual evidence for faithful transmission", "type": "dss"}
        ],

        "divine_council_note": "The discovery of the Dead Sea Scrolls is not merely an "
                              "archaeological event — it is a theological event. The scrolls "
                              "confirmed that the divine council worldview was not a fringe "
                              "interpretation but the mainstream theology of Second Temple "
                              "Judaism. Texts like 1 Enoch, Jubilees, and the War Scroll — "
                              "found in multiple copies — show that the supernatural framework "
                              "of angelic rulers, fallen Watchers, and cosmic warfare was the "
                              "operating worldview of the community that preserved these texts. "
                              "The discovery forces modern readers to take this framework "
                              "seriously, not as mythology but as the theological context of "
                              "both the Old and New Testaments.",

        "sections": [
            {
                "heading": "The Shepherd's Stone — Cave 1 and the Seven Scrolls (1947)",
                "body": "The story begins with an accident. Muhammad edh-Dhib, a Bedouin "
                       "shepherd of the Ta'amireh tribe, was searching for a lost goat near "
                       "Khirbet Qumran when he threw a stone into a narrow cave opening. "
                       "The sound of shattering pottery drew him inside, where he found "
                       "clay jars containing leather scrolls wrapped in linen. Cave 1 "
                       "yielded seven major scrolls: the Great Isaiah Scroll (1QIsa-a) — "
                       "the complete text of all 66 chapters, 7.34 meters long, the best "
                       "preserved biblical manuscript from antiquity. A second, partial "
                       "Isaiah scroll (1QIsa-b). The Community Rule (1QS) — the governing "
                       "document of the Qumran community, including the Treatise on the "
                       "Two Spirits. The War Scroll (1QM) — an eschatological battle plan "
                       "for the final war between the sons of light and sons of darkness. "
                       "The Thanksgiving Hymns (1QH) — devotional poetry, possibly by the "
                       "Teacher of Righteousness himself. The Genesis Apocryphon (1QapGen) "
                       "— an Aramaic retelling of Genesis with expansions. The Habakkuk "
                       "Pesher (1QpHab) — a verse-by-verse commentary on Habakkuk 1-2, "
                       "applying the prophet's words to the community's own experience. "
                       "Four of the scrolls were purchased by the Syrian Orthodox archbishop "
                       "of Jerusalem; three by Eleazar Sukenik of Hebrew University. All "
                       "seven would eventually be reunited at the Shrine of the Book in "
                       "Jerusalem, where they remain today."
            },
            {
                "heading": "Eleven Caves, 900 Manuscripts — The Full Discovery (1948-1956)",
                "body": "The initial find triggered a decade of exploration. Professional "
                       "archaeologists and Bedouin treasure hunters competed to search the "
                       "cliffs along the Dead Sea. Cave 2 (1952) and Cave 3 (1952) yielded "
                       "fragments and the famous Copper Scroll — a list of hidden treasures "
                       "that remains unsolved. Cave 4 (1952) was the mother lode: fragments "
                       "of over 500 manuscripts crammed into a natural cave just meters from "
                       "the Qumran settlement. This single cave contained roughly 75% of all "
                       "scroll fragments. Caves 5-10 produced smaller finds. Cave 11 (1956) "
                       "yielded the last major discoveries: the Great Psalms Scroll "
                       "(11QPs-a), the Temple Scroll (11QT-a), and the Melchizedek scroll "
                       "(11Q13). The total collection: approximately 900 manuscripts. Every "
                       "book of the Hebrew Bible is represented except Esther. Biblical texts "
                       "make up roughly 25% of the collection. Another 25% are previously "
                       "known texts (1 Enoch, Jubilees, Tobit, Sirach). The remaining 50% "
                       "are sectarian compositions and previously unknown works. This is not "
                       "just a biblical library — it is a window into the entire intellectual "
                       "and spiritual world of Second Temple Judaism."
            },
            {
                "heading": "The Great Isaiah Scroll — A Thousand Years of Fidelity (1QIsa-a)",
                "body": "The Great Isaiah Scroll deserves special attention because it "
                       "answers a question that scholars had debated for centuries: how "
                       "faithfully was the Hebrew Bible transmitted? Before 1947, the oldest "
                       "substantial Hebrew Bible manuscript was the Aleppo Codex (~930 AD) "
                       "and the Leningrad Codex (~1008 AD). The Masoretic scribes who "
                       "produced these manuscripts claimed meticulous accuracy — they counted "
                       "every letter, marked the middle word of each book, and developed an "
                       "elaborate system of vowel pointing and cantillation marks. But did "
                       "the text they preserved actually match what was written a thousand "
                       "years earlier? The Great Isaiah Scroll answered: yes, remarkably so. "
                       "The agreement is roughly 95%. The 5% variation consists primarily of "
                       "spelling differences (plene versus defective writing — whether to "
                       "include vowel letters), minor word order changes, occasional "
                       "additions of conjunctions or pronouns, and a handful of substantive "
                       "variants that are theologically significant (such as Isaiah 53, "
                       "where some readings differ). The scribal tradition held. Not "
                       "perfectly — this is not a photocopy — but with a fidelity that "
                       "silenced the most aggressive textual critics."
            },
            {
                "heading": "What the Scrolls Revealed About Scribal Practice",
                "body": "Beyond confirming textual stability, the scrolls revealed how the "
                       "text was actually transmitted. Multiple manuscripts of the same book "
                       "show different textual families — the Masoretic tradition was not "
                       "the only one. Jeremiah at Qumran exists in both a longer form "
                       "(matching the MT) and a shorter form (matching the LXX), showing "
                       "that the book circulated in two editions. Samuel manuscripts from "
                       "Cave 4 (4QSam-a, 4QSam-b) sometimes agree with the LXX against "
                       "the MT, suggesting the LXX translators were working from a Hebrew "
                       "text different from the one that became the Masoretic standard. "
                       "Scribal corrections are visible: original scribes catching their "
                       "own errors, later hands adding marginal notes, dots placed above "
                       "letters to mark suspected errors. The Qumran scribes also used "
                       "distinctive practices: the 'Qumran scribal practice' of writing "
                       "the divine name YHWH in paleo-Hebrew script while the rest of the "
                       "text uses the standard Aramaic (square) script — visually "
                       "distinguishing God's name on the page. This is not just copying; "
                       "it is curating — careful, deliberate, reverent transmission of "
                       "sacred text."
            },
            {
                "heading": "Why 1947 — Providence and Timing",
                "body": "The timing of the discovery demands reflection. In 1947, the "
                       "United Nations voted to partition Palestine. In 1948, Israel "
                       "declared independence. The scrolls emerged at the exact moment when "
                       "the Jewish people were returning to the land after two thousand "
                       "years of exile — and the scrolls they found were hidden by Jews "
                       "fleeing the Roman destruction that began that exile. The Isaiah "
                       "scroll they found contains the very prophecy of return: 'Comfort, "
                       "comfort my people' (Isa 40:1). Cave 4 was discovered just meters "
                       "from the Qumran ruins, hidden in plain sight for nineteen centuries. "
                       "The Jordanian government controlled the caves until 1967, when "
                       "Israel captured the West Bank. The scroll fragments were transferred "
                       "to the Rockefeller Museum and eventually to the Israel Museum. The "
                       "publication process was agonizingly slow — monopolized by a small "
                       "team until public pressure and unauthorized publications broke the "
                       "logjam in the early 1990s. By the turn of the millennium, the full "
                       "corpus was accessible. The word of God endures — and it resurfaces "
                       "when the time is right."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: DEUT 32:8 AND THE DIVINE COUNCIL
    # =========================================================================
    {
        "id": "dss-deut32-divine-council",
        "ref": "Deuteronomy 32:8-9; Psalm 82:1-8",
        "chapter_num": 2,
        "title": "What the Scrolls Confirmed -- Deut 32:8 and the Divine Council",
        "era": "dss_discovery",
        "type": "chapter",
        "themes": ['DSS', 'DIVINE_COUNCIL', 'TEXTUAL', 'DEUT32'],

        "synopsis": "This is THE most important single finding from the Dead Sea Scrolls "
                    "for understanding the biblical worldview. 4QDeut-j reads 'sons of God' "
                    "(bene elohim) in Deuteronomy 32:8, where the Masoretic Text reads "
                    "'sons of Israel' (bene yisrael). The verse describes the Most High "
                    "dividing the nations and fixing their borders 'according to the number "
                    "of the sons of God.' The Septuagint (LXX), translated independently in "
                    "the 3rd century BC, reads 'angels of God' (angelon theou) — confirming "
                    "the same tradition. Two independent witnesses (DSS Hebrew + LXX Greek) "
                    "against one (MT). The scribal alteration is transparent: a later scribe "
                    "changed 'sons of God' to 'sons of Israel' — probably to avoid the "
                    "theological implication that God delegated authority over nations to "
                    "divine beings. But the original reading is clear, and it unlocks "
                    "everything: Psalm 82 (God judging the corrupt divine council), the "
                    "'prince of Persia' and 'prince of Greece' in Daniel 10, the "
                    "territorial assignment at Babel, and the Deuteronomy 32 worldview that "
                    "runs from Genesis 11 to Revelation 12. Without the DSS, we would have "
                    "no Hebrew witness to the original reading. This single textual variant "
                    "changes how you read the entire Bible.",

        "key_verse": {
            "ref": "Deuteronomy 32:8-9",
            "text": "When the Most High gave to the nations their inheritance, when he divided mankind, he fixed the borders of the peoples according to the number of the sons of God. But the LORD's portion is his people, Jacob his allotted heritage.",
            "translation": "ESV (with DSS/LXX reading)"
        },

        "original_terms": [
            {
                "term": "בְּנֵי אֱלֹהִים (b'nei 'elohim)",
                "meaning": "[A] 'Sons of God' — the reading preserved in 4QDeut-j (Dead Sea "
                           "Scrolls). This is the phrase used in Genesis 6:2 ('the sons of God "
                           "saw that the daughters of man were attractive'), Job 1:6 ('the sons "
                           "of God came to present themselves before YHWH'), and Job 38:7 ('when "
                           "the morning stars sang together and all the sons of God shouted for "
                           "joy'). The term refers to divine beings — members of God's heavenly "
                           "council. In Deut 32:8, it means that God divided the nations among "
                           "these divine beings, keeping Israel for himself (v. 9). The Masoretic "
                           "scribes changed this to 'sons of Israel' (b'nei yisrael), but the "
                           "DSS and LXX independently preserve the original reading."
            },
            {
                "term": "בְּנֵי יִשְׂרָאֵל (b'nei yisrael)",
                "meaning": "[A] 'Sons of Israel' — the Masoretic Text reading of Deuteronomy "
                           "32:8. This reading makes poor sense in context: how can God divide "
                           "the nations according to the number of Israel's sons when Israel "
                           "does not yet exist as a nation at the time the Song of Moses "
                           "describes? Some defenders attempt to read it as the 70 nations of "
                           "Genesis 10 corresponding to the 70 sons of Israel who went to Egypt "
                           "(Gen 46:27). But this requires importing a connection that the text "
                           "does not make. The simpler explanation: a scribe changed 'elohim' to "
                           "'yisrael' to remove the implication of a divine council, and two "
                           "independent witnesses (DSS + LXX) preserve the original."
            },
            {
                "term": "עֶלְיוֹן ('Elyon)",
                "meaning": "[A] 'Most High' — a divine title used in Deut 32:8 for God as the "
                           "supreme authority who distributes the nations. The title emphasizes "
                           "hierarchy: 'Elyon is above all the 'elohim (Ps 97:9). He presides "
                           "in the divine council (Ps 82:1, 'God has taken his place in the "
                           "divine council; in the midst of the gods he holds judgment'). The "
                           "use of 'Elyon in Deut 32:8 establishes that the God of Israel is "
                           "not one god among many but the supreme authority over ALL divine "
                           "beings — the one who assigns them their posts and holds them "
                           "accountable for their administration."
            },
            {
                "term": "נַחֲלָה (nachalah)",
                "meaning": "[A] 'Inheritance, allotted portion' — used in Deut 32:9 for Israel "
                           "as YHWH's own nachalah: 'But YHWH's portion (cheleq) is his people, "
                           "Jacob his allotted inheritance (nachalah).' When God divided the "
                           "nations among the sons of God, he kept one nation for himself. This "
                           "is not favoritism but election for purpose — Israel as YHWH's direct "
                           "inheritance while the other nations are under the administration of "
                           "divine beings who would become corrupt (Ps 82)."
            }
        ],

        "ane_backdrop": "The concept of a divine assembly where a supreme deity presides over "
                       "lesser gods is well attested across the ancient Near East. In Ugaritic "
                       "texts, El presides over the divine council (phr 'ilm) on his cosmic "
                       "mountain. In Mesopotamian tradition, the Anunnaki form the assembly of "
                       "great gods, with Anu, Enlil, and Ea at the top. The Deut 32:8 worldview "
                       "shares this structural framework — a supreme God distributing authority "
                       "among lesser divine beings — while making a radical claim: YHWH is not "
                       "merely first among equals. He is 'Elyon, the Most High, who assigned "
                       "the nations to the sons of God and can hold them accountable (Ps 82) "
                       "and strip them of their authority ('you shall die like men,' Ps 82:7). "
                       "The ANE parallel illuminates the structure; the biblical claim transforms it.",

        "second_temple": [
            {
                "source": "4QDeut-j",
                "summary": "A fragmentary Deuteronomy manuscript from Cave 4, dated to the "
                           "mid-2nd century BC. The fragment preserving Deut 32:8 reads 'sons "
                           "of God' (b'nei 'elohim) where the Masoretic Text has 'sons of "
                           "Israel.' This is the key textual witness — a Hebrew manuscript "
                           "confirming the reading that the LXX translated independently.",
                "relevance": "[A] This fragment is arguably the most theologically significant "
                            "single piece of evidence from the Dead Sea Scrolls. It provides "
                            "a Hebrew witness to the original reading of Deut 32:8, confirming "
                            "that the divine council theology was not a later innovation but "
                            "was embedded in the text itself.",
                "canon": False
            },
            {
                "source": "Septuagint (LXX) Deut 32:8",
                "summary": "The Greek translation reads 'angels of God' (angelon theou), "
                           "confirming the same theological tradition as the DSS 'sons of "
                           "God.' The LXX was translated in Alexandria in the 3rd century BC, "
                           "independently of the Qumran scribal tradition.",
                "relevance": "[A] Two independent witnesses — one Hebrew (DSS), one Greek "
                            "(LXX) — agree against the Masoretic Text. This is textual "
                            "criticism at its strongest: when independent witnesses converge, "
                            "the reading they share is almost certainly original."
            },
            {
                "source": "According to Jubilees 15:31-32",
                "summary": "Jubilees explicitly states that God 'set over all the peoples "
                           "and over all the nations spirits (angels) to lead them astray' "
                           "but kept Israel for himself — a direct interpretation of the "
                           "Deut 32:8 tradition.",
                "relevance": "[C] Jubilees demonstrates that Second Temple Jews read Deut "
                            "32:8 as describing the assignment of nations to divine beings — "
                            "exactly what the DSS reading says. This was the mainstream "
                            "interpretation, not a fringe view.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Deuteronomy 32:8-9", "note": "[A] 'When the Most High gave to the nations their inheritance... he fixed the borders of the peoples according to the number of the sons of God. But YHWH's portion is his people.' The foundational text — DSS/LXX reading restores the divine council framework", "type": "ot"},
            {"ref": "Psalm 82:1-8", "note": "[A] 'God (Elohim) has taken his place in the divine council; in the midst of the gods (elohim) he holds judgment.' The corrupt divine beings assigned to nations in Deut 32:8 are judged here — 'you shall die like men' (v. 7)", "type": "ot"},
            {"ref": "Psalm 89:5-7", "note": "[A] 'Who among the heavenly beings (b'nei elim) is like YHWH? God is greatly to be feared in the council of the holy ones' — YHWH's supremacy over the divine council", "type": "ot"},
            {"ref": "Daniel 10:13, 20-21", "note": "[A] 'The prince of the kingdom of Persia withstood me twenty-one days... the prince of Greece will come.' Territorial divine beings opposing God's messengers — the Deut 32:8 worldview in action", "type": "ot"},
            {"ref": "Genesis 11:1-9", "note": "[A] The Babel event — the scattering of nations that Deut 32:8 interprets as the moment God assigned nations to divine beings. Babel is the origin; Deut 32:8 is the interpretation", "type": "ot"},
            {"ref": "1 Corinthians 10:20", "note": "[A] 'What pagans sacrifice, they offer to demons, not to God' — Paul's reading of the Deut 32 worldview. The gods of the nations are real beings, now identified as hostile spiritual powers", "type": "nt"},
            {"ref": "Ephesians 6:12", "note": "[A] 'We do not wrestle against flesh and blood, but against the rulers, against the authorities, against the cosmic powers over this present darkness' — the territorial powers of Deut 32:8 as Paul understood them", "type": "nt"},
            {"ref": "Acts 17:26-27", "note": "[B] 'He made from one man every nation of mankind... having determined allotted periods and the boundaries of their dwelling place' — echoing Deut 32:8's language of boundaries and allotments", "type": "nt"},
            {"ref": "Jubilees 15:31-32", "note": "[C] According to Jubilees, God 'set over all the peoples and over all the nations spirits to lead them astray' but kept Israel — an explicit Second Temple reading of the Deut 32:8 tradition", "type": "pseudepigrapha"}
        ],

        "divine_council_note": "This chapter contains the single most important textual evidence "
                              "for the divine council framework in the entire Dead Sea Scrolls "
                              "corpus. The Deut 32:8 reading in 4QDeut-j — 'sons of God' instead "
                              "of 'sons of Israel' — is the linchpin. With this reading restored, "
                              "the entire biblical narrative from Babel to Revelation snaps into "
                              "focus: God divided the nations among divine beings (Deut 32:8), "
                              "those beings became corrupt (Ps 82), their territory includes "
                              "hostile spiritual powers (Dan 10), and Christ's work reclaims the "
                              "nations from these powers (Col 2:15, Eph 1:20-21). The Masoretic "
                              "alteration to 'sons of Israel' flattened this entire theology. "
                              "The Dead Sea Scrolls restored it.",

        "sections": [
            {
                "heading": "The Textual Evidence — 4QDeut-j and the LXX (Deut 32:8)",
                "body": "The case rests on three witnesses. Witness one: 4QDeut-j, a "
                       "fragmentary Deuteronomy manuscript from Qumran Cave 4, dated to the "
                       "mid-2nd century BC. The fragment preserving Deuteronomy 32:8 reads "
                       "b'nei 'elohim — 'sons of God.' Witness two: the Septuagint (LXX), "
                       "the Greek translation produced in Alexandria in the 3rd century BC, "
                       "which reads angelon theou — 'angels of God.' These are two independent "
                       "witnesses from different geographic locations (Judea and Egypt), in "
                       "different languages (Hebrew and Greek), separated by roughly a century. "
                       "Both preserve the same theological reading. Witness three: the "
                       "Masoretic Text (MT), standardized between the 6th and 10th centuries "
                       "AD, which reads b'nei yisrael — 'sons of Israel.' When two early, "
                       "independent witnesses agree against one later witness, the text-critical "
                       "verdict is clear: the earlier reading is original. A scribe changed "
                       "'elohim' to 'yisrael' — and the two-word alteration obscured the "
                       "divine council worldview for centuries."
            },
            {
                "heading": "Why a Scribe Changed It — Theological Discomfort",
                "body": "Why would a scribe alter the text of Scripture? The answer is "
                       "theological discomfort. The original reading — 'sons of God' — "
                       "implies that YHWH delegated authority over the nations to divine "
                       "beings. For later scribes operating in a context of strict monotheism "
                       "(particularly after the exile, when Jewish theology increasingly "
                       "emphasized God's sole sovereignty), this implication was troubling. "
                       "It sounded like polytheism. It sounded like God shared power. The "
                       "simplest solution: change 'sons of God' to 'sons of Israel' — making "
                       "the verse about the number of Jacob's descendants (70, per Gen 46:27) "
                       "rather than the number of divine beings. But the change created "
                       "problems. The verse's context is the division of ALL nations, not "
                       "Israel specifically. 'Israel' as a nation does not yet exist in the "
                       "Song of Moses' narrative frame. And the parallel with Psalm 82 — "
                       "where God judges the 'elohim' for their corrupt administration of "
                       "the nations — requires the 'sons of God' reading. The scribal "
                       "alteration solved one perceived problem (polytheism) while creating "
                       "a far larger one: it removed the interpretive key to the entire "
                       "divine council theology."
            },
            {
                "heading": "What Deut 32:8 Unlocks — The Entire Biblical Framework",
                "body": "Once you restore the 'sons of God' reading, the biblical narrative "
                       "from Babel onward takes on a completely different shape. At Babel "
                       "(Gen 11), God scatters the nations. Deut 32:8 interprets this event: "
                       "God divided the nations 'according to the number of the sons of God' "
                       "— assigning each nation to a divine being. Deut 32:9 adds the "
                       "punchline: 'But YHWH's portion is his people, Jacob his allotted "
                       "heritage.' God kept one nation for himself and delegated the rest. "
                       "Psalm 82 shows what happened next: the divine administrators became "
                       "corrupt — 'How long will you judge unjustly and show partiality to "
                       "the wicked?' (v. 2). God sentences them: 'You shall die like men, "
                       "and fall like any prince' (v. 7). Daniel 10 shows the system still "
                       "operating: the 'prince of Persia' and 'prince of Greece' are "
                       "territorial divine beings who resist God's messengers. Paul inherits "
                       "this framework: 'We do not wrestle against flesh and blood, but "
                       "against rulers, authorities, cosmic powers over this present darkness' "
                       "(Eph 6:12). Christ's triumph dismantles it: 'He disarmed the rulers "
                       "and authorities and put them to open shame' (Col 2:15). Pentecost "
                       "reverses Babel: tongues of fire, every nation hearing in their own "
                       "language (Acts 2) — God reclaiming the nations he distributed at "
                       "Babel. One textual variant. The entire biblical metanarrative."
            },
            {
                "heading": "The Integrity of the Discovery — Why This Is Not Controversial",
                "body": "Some readers worry that finding a variant reading undermines biblical "
                       "authority. The opposite is true. The DSS demonstrate that we can "
                       "identify scribal changes and recover the original reading. This is "
                       "textual criticism working exactly as it should — not destroying "
                       "Scripture but restoring it. The 'sons of God' reading is not a modern "
                       "scholarly invention. It is the OLDER reading, independently attested "
                       "in two different textual traditions (Hebrew and Greek). The 'sons of "
                       "Israel' reading is the later alteration. The DSS did not create a "
                       "new theology — they recovered an old one that had been obscured by "
                       "a well-intentioned but misguided scribal change. The textual evidence "
                       "is not the enemy of faith. It is the friend of truth. And the truth "
                       "is that the original text says exactly what the divine council "
                       "framework requires it to say."
            }
        ]
    },

    # =========================================================================
    # CHAPTER 3: THE SCROLLS THE BIBLE MENTIONS
    # =========================================================================
    {
        "id": "dss-biblical-manuscripts",
        "ref": "Daniel 7:9-14; Psalm 151; Isaiah 1-66",
        "chapter_num": 3,
        "title": "The Scrolls the Bible Mentions",
        "era": "dss_discovery",
        "type": "chapter",
        "themes": ['DSS', 'TEXTUAL', 'DANIEL', 'PSALMS', 'ISAIAH'],

        "synopsis": "The Dead Sea Scrolls include manuscripts of every Old Testament book "
                    "except Esther, many in multiple copies. Three collections deserve "
                    "special attention. Daniel: eight manuscripts from Cave 4 (4QDan-a "
                    "through 4QDan-e, plus fragments), with the earliest dating to "
                    "approximately 125 BC. This matters because critical scholars had dated "
                    "Daniel's composition to 165 BC — a Maccabean-era propaganda piece, "
                    "they claimed. But 4QDan-a dates within a generation of that supposed "
                    "composition — far too soon for a newly written text to achieve the "
                    "widespread authority and scribal distribution evidenced at Qumran. "
                    "The Psalms: the Great Psalms Scroll (11QPs-a) contains 41 canonical "
                    "psalms in a different ordering, plus seven non-canonical compositions "
                    "including Psalms 151, 154, and 155, and a prose section called 'David's "
                    "Compositions' attributing 4,050 songs to David. This shows the Psalter "
                    "was still being shaped in the Second Temple period. Isaiah: fragments "
                    "of every chapter found across multiple manuscripts, making Isaiah the "
                    "best-attested book at Qumran. The scribal evidence — corrections, "
                    "marginal notes, textual variants — shows these are not just copies "
                    "but windows into how the biblical text was transmitted, curated, and "
                    "revered.",

        "key_verse": {
            "ref": "Daniel 7:13-14",
            "text": "I saw in the night visions, and behold, with the clouds of heaven there came one like a son of man, and he came to the Ancient of Days and was presented before him. And to him was given dominion and glory and a kingdom, that all peoples, nations, and languages should serve him.",
            "translation": "ESV"
        },

        "original_terms": [
            {
                "term": "כְּבַר אֱנָשׁ (kebar enash)",
                "meaning": "[A] Aramaic: 'one like a son of man' — Daniel 7:13. The Qumran "
                           "Daniel manuscripts preserve this figure who comes 'with the clouds "
                           "of heaven' to the Ancient of Days. Cloud-riding is an exclusively "
                           "divine prerogative in the Hebrew Bible (Ps 68:4, Ps 104:3, Isa "
                           "19:1). This figure receives universal dominion — 'all peoples, "
                           "nations, and languages should serve him.' Jesus applied this title "
                           "to himself (Mark 14:62), and the high priest understood the divine "
                           "claim immediately — he tore his robes (Law #19)."
            },
            {
                "term": "עַתִּיק יוֹמִין ('Attiq Yomin)",
                "meaning": "[A] Aramaic: 'Ancient of Days' — Daniel 7:9, 13, 22. A unique "
                           "title for God emphasizing eternal existence. The Qumran Daniel "
                           "manuscripts preserve the throne vision: 'His clothing was white as "
                           "snow, and the hair of his head like pure wool; his throne was fiery "
                           "flames; its wheels were burning fire. A stream of fire issued and "
                           "came out from before him; a thousand thousands served him, and ten "
                           "thousand times ten thousand stood before him; the court sat in "
                           "judgment' (Dan 7:9-10). This is the divine council in session."
            },
            {
                "term": "מִזְמוֹר (mizmor)",
                "meaning": "[A] 'Psalm, song' — from zamar, 'to sing, to make music.' The "
                           "Great Psalms Scroll (11QPs-a) preserves 41 canonical psalms plus "
                           "additional compositions, showing that the Psalter collection was "
                           "still fluid in the Second Temple period. The 'David's Compositions' "
                           "prose section attributes 4,050 works to David — 3,600 psalms plus "
                           "450 songs — revealing the scope of the Davidic musical tradition "
                           "as understood at Qumran."
            }
        ],

        "ane_backdrop": "The preservation of Daniel at Qumran intersects with a critical "
                       "scholarly debate. The book of Daniel contains detailed descriptions "
                       "of events under Antiochus IV Epiphanes (~167-164 BC), leading many "
                       "critical scholars to date the book's final composition to ~165 BC — "
                       "treating the 'prophecies' as after-the-fact history. But the Qumran "
                       "evidence complicates this theory. 4QDan-a dates to roughly 125 BC, "
                       "only about 40 years after the supposed composition date. In the "
                       "ancient world, a text needed time to achieve the authority and "
                       "widespread distribution that Daniel clearly had at Qumran — multiple "
                       "manuscripts, pesher (commentary) treatment, and inclusion in the "
                       "community's apocalyptic framework. The DSS do not definitively "
                       "resolve the dating question, but they make the 165 BC composition "
                       "theory significantly more difficult to sustain.",

        "second_temple": [
            {
                "source": "11QPs-a (Great Psalms Scroll)",
                "summary": "The largest psalms manuscript from Qumran, containing 41 "
                           "canonical psalms in a non-Masoretic ordering, plus seven "
                           "non-canonical compositions. Psalm 151 (a first-person account "
                           "of David's anointing and victory over Goliath), Psalms 154 and "
                           "155 (previously known only from Syriac translations), and the "
                           "'David's Compositions' prose section.",
                "relevance": "[C] The different ordering and additional compositions show "
                            "that the Psalter was still being shaped in the 1st century BC. "
                            "The canonical collection we have was finalized later — the "
                            "Qumran community knew a broader Davidic tradition.",
                "canon": False
            },
            {
                "source": "4QDan-a through 4QDan-e",
                "summary": "Eight Daniel manuscripts from Cave 4, the earliest dating to "
                           "approximately 125 BC. They preserve portions of all twelve "
                           "chapters, including the critical language transition from Hebrew "
                           "to Aramaic at Daniel 2:4 and back to Hebrew at Daniel 8:1.",
                "relevance": "[A] Multiple early copies demonstrate Daniel's authority at "
                            "Qumran. The divine council throne vision (Dan 7:9-14), the "
                            "cloud-rider Son of Man, and the cosmic warfare of Daniel 10-12 "
                            "were central to the community's apocalyptic worldview.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Daniel 7:9-14", "note": "[A] The divine council in session — the Ancient of Days, fiery throne, ten thousand times ten thousand, and the cloud-riding Son of Man receiving universal dominion. Preserved in multiple Qumran manuscripts", "type": "ot"},
            {"ref": "Daniel 10:13, 20-21", "note": "[A] Territorial divine beings ('prince of Persia,' 'prince of Greece') and Michael as 'your prince' — the Deut 32:8 worldview in action, preserved at Qumran", "type": "ot"},
            {"ref": "Daniel 12:1-2", "note": "[A] 'At that time shall arise Michael, the great prince... and many of those who sleep in the dust of the earth shall awake' — resurrection hope preserved at Qumran, foundational for the War Scroll's eschatology", "type": "ot"},
            {"ref": "Psalm 82:1", "note": "[A] 'God has taken his place in the divine council; in the midst of the gods he holds judgment' — the divine council psalm, connecting directly to the Deut 32:8 framework the DSS confirmed", "type": "ot"},
            {"ref": "Isaiah 52:13-53:12", "note": "[A] The Suffering Servant — preserved in the Great Isaiah Scroll with minor variants. The Qumran community interpreted messianic expectation through Isaiah's servant passages", "type": "ot"},
            {"ref": "Mark 14:62-63", "note": "[A] Jesus claims to be the cloud-rider of Daniel 7:13 — the high priest tears his robes because he understood the divine claim, not merely a messianic one (Law #19)", "type": "nt"},
            {"ref": "11QPs-a (Great Psalms Scroll)", "note": "[C] 41 canonical psalms in non-standard order, plus Psalm 151 and other compositions — showing the Psalter was still being shaped in the Second Temple period", "type": "dss"},
            {"ref": "4QDan-a", "note": "[C] Earliest Daniel manuscript, ~125 BC — only a generation after the critical scholars' proposed composition date, challenging the late-dating theory", "type": "dss"}
        ],

        "divine_council_note": "The Daniel manuscripts at Qumran are crucial for the divine "
                              "council framework. Daniel 7 presents the fullest divine council "
                              "scene in the Hebrew Bible: the Ancient of Days takes his seat, "
                              "the court (divine council) sits in judgment, the books are opened, "
                              "and the Son of Man — a divine cloud-rider — receives universal "
                              "dominion. Daniel 10 reveals the territorial system: divine beings "
                              "('princes') assigned to nations (Persia, Greece), with Michael "
                              "assigned as Israel's prince. This is the Deut 32:8 framework in "
                              "narrative action. The Qumran community preserved, copied, and "
                              "studied these texts because they understood the world in exactly "
                              "these terms — a cosmic conflict between divine powers, with God's "
                              "people caught in the middle, awaiting the final intervention.",

        "sections": [
            {
                "heading": "Daniel at Qumran — Earlier Than Critics Claimed (4QDan-a through 4QDan-e)",
                "body": "Eight Daniel manuscripts were found at Qumran, spanning all twelve "
                       "chapters. The earliest, 4QDan-a, dates to approximately 125 BC — "
                       "and this date matters enormously. Critical scholarship had long "
                       "argued that Daniel was composed around 165 BC during the Maccabean "
                       "crisis, treating its 'prophecies' about Antiochus IV Epiphanes as "
                       "history written after the fact (vaticinium ex eventu). But a 125 BC "
                       "manuscript creates a problem for this theory: in the ancient world, "
                       "a text needed decades to achieve the kind of authority Daniel "
                       "clearly held at Qumran. Multiple copies, pesher commentary "
                       "treatment, integration into the community's apocalyptic framework — "
                       "this does not happen to a text that is only 40 years old. The "
                       "manuscripts also preserve the distinctive Hebrew-Aramaic-Hebrew "
                       "language transition (Hebrew in 1:1-2:4a, Aramaic in 2:4b-7:28, "
                       "Hebrew again in 8:1-12:13) — showing this feature was original to "
                       "the text, not a later editorial addition. Daniel was not a "
                       "Maccabean propaganda piece. It was ancient, authoritative, and "
                       "central to the community's hope."
            },
            {
                "heading": "The Great Psalms Scroll — A Living Psalter (11QPs-a)",
                "body": "The Great Psalms Scroll from Cave 11 is one of the largest and "
                       "best-preserved manuscripts from Qumran. It contains 41 canonical "
                       "psalms — but not in the order of the Masoretic Psalter. Psalm 118 "
                       "is followed by 104, then 147, then 105, and so on through a "
                       "sequence that matches no other known collection. Interspersed among "
                       "the canonical psalms are compositions not found in the standard "
                       "Psalter: Psalm 151 (a first-person account by David of his anointing "
                       "and his battle with Goliath — previously known only from the LXX), "
                       "Psalms 154 and 155 (previously known only from Syriac), and a prose "
                       "composition called 'David's Compositions' that attributes 4,050 "
                       "works to David: 3,600 psalms, 364 songs for daily offerings, 52 "
                       "songs for Sabbaths, 30 songs for festivals, and 4 songs for the "
                       "stricken. The numbers are keyed to the solar calendar — 364 days, "
                       "52 weeks. This scroll tells us that the Psalter was still a living, "
                       "growing collection in the 1st century BC. The 150-psalm canon we "
                       "know was finalized later."
            },
            {
                "heading": "Isaiah — Every Chapter, Multiple Witnesses",
                "body": "Isaiah is the best-attested biblical book at Qumran. The Great "
                       "Isaiah Scroll (1QIsa-a) preserves all 66 chapters. A second "
                       "partial scroll (1QIsa-b) covers portions of chapters 7-66 with "
                       "a text very close to the Masoretic standard. Fragments from Cave 4 "
                       "(4QIsa-a through 4QIsa-f) provide additional witnesses. Taken "
                       "together, every chapter of Isaiah has manuscript coverage from "
                       "Qumran. This wealth of evidence allows scholars to trace textual "
                       "transmission with unprecedented precision. Where 1QIsa-a and the "
                       "MT agree, the reading is virtually certain. Where they differ, the "
                       "variants illuminate scribal practice: most are spelling differences "
                       "(the Qumran scribes used fuller, more phonetic spelling), occasional "
                       "word additions or omissions, and rare substantive variants. Isaiah "
                       "53 — the Suffering Servant passage — shows some interesting variants "
                       "in 1QIsa-a, including a reading at 53:11 that adds 'light' ('he "
                       "shall see light and be satisfied') where the MT is shorter. The "
                       "LXX confirms the longer reading. Once again, the DSS and LXX "
                       "converge against a shorter MT — a pattern that strengthens "
                       "confidence in the longer readings."
            },
            {
                "heading": "Beyond the Big Three — Samuel, Jeremiah, and Textual Plurality",
                "body": "Samuel and Jeremiah from Qumran reveal something the Isaiah scrolls "
                       "do not: the Hebrew Bible circulated in more than one textual form. "
                       "4QSam-a, one of the oldest biblical manuscripts (mid-3rd century BC), "
                       "contains readings that agree with the LXX against the Masoretic Text "
                       "— suggesting the LXX translators worked from a Hebrew text different "
                       "from the one that became standard. Jeremiah is even more dramatic: "
                       "Qumran preserves both a longer text (matching the MT) and a shorter "
                       "text (matching the LXX, which is roughly 12% shorter). Both versions "
                       "circulated simultaneously. This does not undermine biblical authority "
                       "— it enriches it. The scribal tradition preserved the text with "
                       "extraordinary care, but different communities sometimes preserved "
                       "different editions. The DSS give us access to this textual plurality, "
                       "allowing scholars to weigh multiple witnesses rather than relying "
                       "on a single tradition. The Bible you hold in your hands is more "
                       "firmly grounded because of these discoveries, not less."
            },
            {
                "heading": "Scribal Corrections and Marginal Notes — Windows into Transmission",
                "body": "The Qumran manuscripts are not clean, sterile copies. They are "
                       "working documents that show the marks of human hands engaged in "
                       "sacred work. Scribal corrections appear throughout: letters written "
                       "and then scraped away, words inserted above the line with caret "
                       "marks, dots placed above letters to indicate suspected errors. The "
                       "Great Isaiah Scroll shows at least two different scribal hands — "
                       "the original copyist and a later corrector who brought readings "
                       "closer to the proto-Masoretic standard. Some manuscripts use the "
                       "paleo-Hebrew script for the divine name YHWH while writing the rest "
                       "in standard Aramaic (square) script — a visual distinction that "
                       "set God's name apart on the page. The Habakkuk Pesher (1QpHab) "
                       "shows another practice: the biblical text being quoted is written "
                       "in one format, and the community's interpretation follows in "
                       "another. These are not just old copies of the Bible. They are "
                       "evidence of communities who believed they were handling the words "
                       "of the living God — and treated them accordingly."
            }
        ]
    }
]
