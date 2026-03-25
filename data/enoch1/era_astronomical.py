"""
era_astronomical.py — The Astronomical Book (1 Enoch 72-82)

The Astronomical Book (also called the Book of the Luminaries or the Book
of the Heavenly Luminaries) is among the OLDEST sections of the Enochic
corpus. Aramaic fragments from Qumran (4Q208-211, designated 4QEn-astr-a
through 4QEn-astr-d) date to the late 3rd or early 2nd century BC, making
this possibly the oldest Jewish apocalyptic text in existence. The Qumran
Aramaic version is considerably longer than the Ethiopic redaction, which
suggests the Ethiopic represents an abridgment of a much fuller original.

The Astronomical Book describes the divinely ordained system of the cosmos:
  72    — The solar calendar: 364 days, 12 months, 4 seasons
  73-74 — The lunar cycle: phases, relationship to the solar year
  75-76 — The gates of heaven: 6 solar gates, 12 wind portals
  77-79 — Geographic regions and the tablets of heaven
  80-81 — The eschatological disruption of cosmic order
  82    — The four intercalary days and conclusion

The 364-day solar calendar is the critical issue. It directly opposes the
354-day lunar calendar used in the Jerusalem Temple by the 2nd century BC.
The Qumran community adopted the 364-day calendar as a defining marker
of their identity, considering the Temple establishment's lunar calendar
a corruption. This calendrical controversy lies behind much of the Qumran
sectarian literature and may illuminate NT references to festival disputes.

Translation references: R.H. Charles (1912), O. Neugebauer (appendix to
Black, 1985), G.W.E. Nickelsburg & J.C. VanderKam (Hermeneia, 2012).
"""

CHAPTERS = [
    # =========================================================================
    # THE SOLAR CALENDAR (1 Enoch 72)
    # =========================================================================
    {
        "id": "1en-72",
        "ref": "1 Enoch 72",
        "chapter_num": 72,
        "title": "The Solar Year — 364 Days and the Six Gates",
        "era": "astronomical",
        "type": "chapter",

        "synopsis": "Chapter 72 is the foundational text for the 364-day solar calendar "
                    "that would become a defining feature of sectarian Judaism at "
                    "Qumran. The angel Uriel shows Enoch the course of the sun through "
                    "six gates in the eastern and western heavens. The sun rises through "
                    "different gates depending on the season, completing a circuit of "
                    "twelve 30-day months plus four intercalary days (one at each "
                    "equinox and solstice), for a total of 364 days. The system is "
                    "mathematically elegant: 364 = 52 weeks exactly, meaning every "
                    "date falls on the same day of the week every year. This calendar "
                    "is divinely revealed — not a human calculation but a heavenly "
                    "truth — and departure from it constitutes cosmic rebellion.",

        "key_verse": {
            "ref": "1 Enoch 72:32-33",
            "text": "And the sun and the stars bring in all the years exactly, so "
                    "that they do not advance or delay their position by a single "
                    "day unto eternity; but complete the years with perfect justice "
                    "in 364 days.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "shamayim",
            "raqia",
            "malak_yhwh",
            "olam",
            "mishpat",
        ],

        "ane_backdrop": "Ancient calendrical systems varied widely. The Mesopotamian "
                        "calendar was lunisolar (354 days adjusted by intercalary "
                        "months). The Egyptian civil calendar was solar (365 days: "
                        "12 months of 30 days plus 5 epagomenal days). The 364-day "
                        "calendar of 1 Enoch is closest to a schematic solar calendar "
                        "that appears in some Mesopotamian astronomical texts (MUL.APIN "
                        "tradition), where the year is divided into 12 months of 30 "
                        "days with corrections. The six-gate system through which the "
                        "sun rises and sets may reflect observation of the sun's "
                        "seasonal movement along the horizon between the solstice "
                        "points, divided into six sectors.",

        "second_temple": [
            {
                "source": "Jubilees 6:32-38",
                "summary": "Jubilees mandates the 364-day solar calendar and condemns "
                           "those who use a lunar calendar: 'There will be those who "
                           "will assuredly make observations of the moon — how it "
                           "disturbs the seasons and comes in from year to year ten "
                           "days too soon. For this reason the years will come upon "
                           "them when they will disturb the order.'",
                "relevance": "Jubilees independently mandates the same 364-day calendar "
                             "as 1 Enoch 72, showing that this was a major theological "
                             "commitment shared across the Enochic-Jubilean tradition. "
                             "The attack on the lunar calendar implies a real dispute "
                             "with the Jerusalem Temple establishment.",
                "canon": False
            },
            {
                "source": "4Q317 (4QPhases of the Moon / Calendrical Document)",
                "summary": "A Qumran text that synchronizes the phases of the moon "
                           "with the 364-day solar calendar, attempting to harmonize "
                           "solar and lunar observations within the Enochic framework.",
                "relevance": "Shows the Qumran community actively working to reconcile "
                             "lunar observation with their solar calendar commitment, "
                             "demonstrating that the Astronomical Book's teachings were "
                             "not just theoretical but practically implemented.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Genesis 1:14-18", "note": "God made the luminaries to govern the day and night and to mark seasons, days, and years — the Astronomical Book claims to reveal the precise system God established at creation", "type": "ot"},
            {"ref": "Psalm 19:1-6", "note": "The heavens declare the glory of God; the sun runs its circuit from one end of heaven to the other — the cosmic order that 1 Enoch 72 maps in technical detail", "type": "ot"},
            {"ref": "Psalm 104:19", "note": "He made the moon to mark the seasons; the sun knows its time for setting — the OT basis for calendrical theology", "type": "ot"},
            {"ref": "4Q208-211 (4QEn-astr a-d)", "type": "dss", "note": "Aramaic fragments of the Astronomical Book from Qumran, dating to the late 3rd or early 2nd century BC. The Aramaic version is significantly longer than the Ethiopic, suggesting the latter is an abridgment. These are among the oldest DSS manuscripts."},
            {"ref": "4Q320-330 (Calendrical Documents)", "type": "dss", "note": "An extensive collection of Qumran calendrical texts that implement the 364-day solar calendar of 1 Enoch 72, including priestly rotation schedules and festival dates."},
            {"ref": "Daniel 7:25", "note": "The fourth beast's horn 'shall think to change the times and the law' — possibly reflecting the calendrical controversy: changing the sacred calendar is an act of cosmic rebellion", "type": "ot"},
            {"ref": "Sirach 43:1-12", "note": "Ben Sira's praise of the sun and moon as created wonders that follow God's commands — a more conventional treatment of celestial theology than 1 Enoch's technical detail", "type": "ot"}
        ],

        "divine_council_note": "The Astronomical Book presupposes that the cosmic "
                               "calendar is a divine council decree. The luminaries "
                               "follow their appointed courses because they obey "
                               "the commands of the Most High, mediated through the "
                               "angel Uriel. Deviation from the appointed calendar — "
                               "whether by celestial bodies or by human societies — "
                               "is rebellion against the council's order. This is why "
                               "the calendrical dispute was so heated: for the Enochic "
                               "tradition, using the wrong calendar was not a "
                               "mathematical error but a theological apostasy, a "
                               "refusal to align human worship with divine decree.",

        "sections": [
            {
                "heading": "The Solar Gates — Seasonal Mechanics (72:1-12)",
                "body": "Uriel, 'the leader of them all' (72:1), shows Enoch the "
                        "system by which the sun traverses the heavens. Six gates are "
                        "arranged in the east and six corresponding gates in the west. "
                        "The sun rises through the fourth gate at the vernal equinox, "
                        "progresses northward to the sixth gate at the summer solstice, "
                        "returns southward through gates five to one (reaching the "
                        "first gate at the winter solstice), then returns northward "
                        "again. Each month is 30 days; the additional 4 intercalary "
                        "days are added at the solstices and equinoxes (one per "
                        "season). This produces a year of exactly 364 days: (12 x 30) "
                        "+ 4 = 364. The mathematical elegance is deliberate: 364 = "
                        "7 x 52, meaning every date always falls on the same day of "
                        "the week. Passover is always on Wednesday; the Day of "
                        "Atonement is always on Friday. This fixed alignment between "
                        "festival dates and weekdays was theologically critical: the "
                        "Sabbath and the festivals would never conflict, and the "
                        "worship calendar would be permanently synchronized with the "
                        "creation week of Genesis 1."
            },
            {
                "heading": "The Daylight-Darkness Ratio (72:13-32)",
                "body": "The chapter tracks the changing ratio of daylight to darkness "
                        "through the year. At the equinoxes, day and night are equal "
                        "(12:12 in the text's division into 18 parts). At the summer "
                        "solstice, daylight reaches its maximum; at the winter "
                        "solstice, darkness predominates. The precise measurements are "
                        "given in 'parts' (a unit of time), with the longest day "
                        "having 12 parts of light and 6 of darkness. This scheme is "
                        "schematic rather than observational — it does not match any "
                        "specific latitude precisely but approximates conditions in "
                        "the Levant. The Aramaic fragments from Qumran (4Q208-211) "
                        "preserve a much more detailed version of these tables, with "
                        "day-by-day tracking of the sun's position, confirming that "
                        "the Ethiopic version is a summary of a longer original. "
                        "The theological point is that every variation in light and "
                        "darkness is divinely ordained: 'the sun and the stars bring "
                        "in all the years exactly, so that they do not advance or "
                        "delay their position by a single day' (72:33). The cosmos "
                        "runs on perfect divine clockwork."
            },
            {
                "heading": "The 364-Day Year — Theological Significance",
                "body": "The insistence on a 364-day year is not merely astronomical "
                        "but profoundly theological. The actual solar year is "
                        "approximately 365.25 days, meaning the 364-day calendar "
                        "would drift by roughly 1.25 days per year. The Astronomical "
                        "Book's authors were likely aware of this discrepancy but "
                        "maintained the 364-day count because of its mathematical "
                        "properties: perfect divisibility by 7 (ensuring fixed "
                        "weekdays for all dates), by 4 (matching four seasons of 91 "
                        "days each), and by 52 (exact weeks). The theological "
                        "commitment was to cosmic order over empirical precision. "
                        "A divinely created universe should operate on mathematically "
                        "perfect principles, and the 364-day calendar embodies that "
                        "perfection. The lunar calendar (354 days) was seen as even "
                        "worse: it required messy intercalation and produced festivals "
                        "that 'wandered' through the week. Jubilees 6:36-38 makes the "
                        "stakes explicit: those who follow the moon 'will assuredly "
                        "disturb the order' and 'mingle holy things with profane.' "
                        "Calendar was not a matter of convenience but of covenant "
                        "fidelity."
            }
        ]
    },

    # =========================================================================
    # THE LUNAR CYCLE (1 Enoch 73-75)
    # =========================================================================
    {
        "id": "1en-73-75",
        "ref": "1 Enoch 73-75",
        "chapter_num": 73,
        "title": "The Moon, the Winds, and the Gates of Heaven",
        "era": "astronomical",
        "type": "chapter",

        "synopsis": "Chapters 73-75 address the lunar cycle and the broader system of "
                    "heavenly gates. The moon passes through the same six gates as the "
                    "sun but on its own schedule, waxing and waning through 29.5-day "
                    "months. The text carefully tracks the moon's light as it increases "
                    "and decreases in fourteen-part increments. Chapter 75 describes "
                    "the twelve gates for the winds and their relationship to the "
                    "stellar gates. The section emphasizes that the lunar cycle is "
                    "subordinate to the solar: the moon's calendar is given for "
                    "observation but not for regulating festivals, which must follow "
                    "the solar 364-day count.",

        "key_verse": {
            "ref": "1 Enoch 74:12",
            "text": "And the sun and the stars bring in all the years exactly, so "
                    "that they do not advance or delay their position by a single "
                    "day unto eternity; but complete the years with perfect justice "
                    "in three hundred and sixty-four days.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "shamayim",
            "raqia",
            "ruach",
            "malak_yhwh",
            "olam",
        ],

        "ane_backdrop": "Lunar observation was the basis of most ANE calendrical "
                        "systems. The Mesopotamian calendar was fundamentally lunar, "
                        "with months beginning at the sighting of the new crescent "
                        "moon. The Egyptian calendar originally combined lunar and "
                        "solar elements before settling on a civil solar calendar. "
                        "The 1 Enoch Astronomical Book's treatment of the moon as "
                        "secondary to the sun may reflect polemical engagement with "
                        "Mesopotamian and/or contemporary Jewish practice. The "
                        "Babylonian MUL.APIN astronomical compendium (c. 1100 BC) "
                        "provides parallel gate-system descriptions for celestial "
                        "risings and settings.",

        "second_temple": [
            {
                "source": "4Q317 (4QPhases of the Moon)",
                "summary": "A Qumran document that meticulously tracks the moon's "
                           "illumination day by day, synchronized with the 364-day "
                           "solar calendar. It divides the moon's light into fourteen "
                           "parts, exactly as 1 Enoch 73 does.",
                "relevance": "Direct practical implementation of 1 Enoch 73's lunar "
                             "theory at Qumran. The community used this text alongside "
                             "the Astronomical Book to maintain their calendrical system.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Psalm 104:19", "note": "He made the moon to mark the seasons — the OT assigns the moon a calendrical function that the Astronomical Book subordinates to the solar cycle", "type": "ot"},
            {"ref": "Genesis 1:16", "note": "The greater light to rule the day and the lesser light to rule the night — the Astronomical Book's solar primacy over lunar reflects Genesis 1's hierarchy of luminaries", "type": "ot"},
            {"ref": "Sirach 43:6-8", "note": "The moon marks the times and is a sign for festivals — Ben Sira assumes the lunar calendar that 1 Enoch's tradition opposes, reflecting the mainstream position", "type": "ot"},
            {"ref": "4Q208-211 (4QEn-astr a-d)", "type": "dss", "note": "Aramaic fragments of the Astronomical Book preserving much more detailed lunar tables than the Ethiopic version, including a synchronistic calendar that tracks solar and lunar positions simultaneously"},
            {"ref": "4Q317 (4QPhases of the Moon)", "type": "dss", "note": "Qumran text implementing 1 Enoch 73's fourteen-part lunar illumination system within the framework of the 364-day calendar"},
            {"ref": "Colossians 2:16", "note": "Let no one pass judgment on you in questions of food and drink, or with regard to a festival or a new moon or a Sabbath — Paul's dismissal of calendrical disputes may echo the solar-lunar controversy that the Astronomical Book fueled", "type": "nt"}
        ],

        "divine_council_note": "The wind gates of chapter 75 reveal the cosmic "
                               "infrastructure maintained by the divine council. "
                               "Twelve gates at the four cardinal directions control "
                               "the winds, and each gate is supervised by angelic "
                               "administrators. The system extends the principle of "
                               "cosmic bureaucracy: nothing in the natural world — not "
                               "a breeze, not a raindrop — operates outside the "
                               "council's management. When weather disrupts or the "
                               "seasons fail (as described in the eschatological "
                               "sections, chapters 80-81), it signals a breakdown in "
                               "the council's order, not randomness.",

        "sections": [
            {
                "heading": "The Moon's Light — Waxing and Waning in Fourteen Parts (73:1-8)",
                "body": "Chapter 73 presents a systematic description of the lunar "
                        "cycle. The moon's illuminated surface is divided into fourteen "
                        "parts. During the first half of the month, one part is added "
                        "each day until the moon is full at day 14 (fourteen-fourteenths "
                        "illuminated). During the second half, one part is subtracted "
                        "each day until the moon is dark. The cycle runs approximately "
                        "29.5 days. The fourteen-part system is schematic — actual lunar "
                        "illumination is not perfectly linear — but it provides a "
                        "mathematical model that was practical for tracking. The Aramaic "
                        "fragments from Qumran (4Q208-211) show that the original "
                        "Astronomical Book contained much more detailed tables with "
                        "day-by-day positions, suggesting the Ethiopic version is a "
                        "radical abridgment. Neugebauer's analysis of 4Q208 shows that "
                        "the Aramaic text tracked the moon's position relative to the "
                        "sun in a system resembling Mesopotamian Goal-Year texts, "
                        "indicating sophisticated astronomical knowledge underlying "
                        "the schematic presentation."
            },
            {
                "heading": "Solar-Lunar Discrepancy (74:10-16)",
                "body": "Chapter 74 addresses the crucial discrepancy between the "
                        "solar and lunar years: 'In eight years it amounts to eighty "
                        "days, all the days which it falls behind in eight years are "
                        "eighty' (74:14, Charles — the text is corrupt in places). "
                        "The solar year of 364 days exceeds the lunar year of 354 "
                        "days by 10 days per year, accumulating to 80 days in eight "
                        "years. This discrepancy is precisely the problem that the "
                        "lunar calendar's intercalation must address. The Astronomical "
                        "Book does not propose intercalation; instead, it insists that "
                        "the solar count is correct and the lunar count is deficient. "
                        "The moon 'falls behind' — it is the moon that is wrong, not "
                        "the solar calendar that needs adjustment. This polemical "
                        "framing was central to the Qumran community's rejection "
                        "of the Temple establishment's lunar reckoning."
            },
            {
                "heading": "The Wind Gates and the Cosmic Infrastructure (75:1-9)",
                "body": "Chapter 75 describes twelve portals at the four cardinal "
                        "directions through which winds emerge. Three gates face east, "
                        "three west, three north, three south. From the eastern gates "
                        "come beneficial winds: 'the east wind, prosperity and dew, "
                        "rain and germination.' From the northern gates come harmful "
                        "cold. From the southern gates come drought and destruction. "
                        "From the western gates come dew, rain, locusts, and "
                        "desolation. The classification is moral as well as "
                        "meteorological: some winds are explicitly identified as "
                        "beneficial and others as harmful. This moral geography of "
                        "wind corresponds to the ethical geography of the Book of the "
                        "Watchers: the cosmos is structured so that physical direction "
                        "maps onto moral value. The 'storehouses of wind' referenced "
                        "here are the same otzarot mentioned in Job 38:22, Psalm "
                        "135:7, and Jeremiah 10:13 — places where God keeps atmospheric "
                        "phenomena under control and releases them according to his "
                        "purpose."
            }
        ]
    },

    # =========================================================================
    # THE COSMOLOGICAL GATES — STARS, WINDS, AND GEOGRAPHY (1 Enoch 76-77)
    # =========================================================================
    {
        "id": "1en-76-77",
        "ref": "1 Enoch 76-77",
        "chapter_num": 76,
        "title": "The Stellar Gates and the Geography of the World",
        "era": "astronomical",
        "type": "chapter",

        "synopsis": "Chapters 76-77 extend the gate system from the sun and moon to the "
                    "stars, winds, and geographic regions of the earth. The stars emerge "
                    "through the same six-gate system that governs the sun, each star "
                    "assigned a specific gate and a specific time of rising. The twelve "
                    "wind portals are described in detail: three at each cardinal direction, "
                    "each producing winds of different character (beneficial or harmful). "
                    "Chapter 77 maps the four quarters of the earth — seven great mountains, "
                    "seven rivers, seven islands — creating a schematic sacred geography "
                    "that places the cosmos under total angelic administration. Every "
                    "natural phenomenon — from a star\'s rising to a wind\'s direction — "
                    "operates on divine assignment.",

        "key_verse": {
            "ref": "1 Enoch 76:1-2",
            "text": "And the leaders of the heads of the thousands, who are placed "
                    "over the whole creation and over all the stars, have also to do "
                    "with the four intercalary days, being inseparable from their "
                    "office, according to the reckoning of the year; and these render "
                    "service on the four days which are not reckoned in the reckoning "
                    "of the year.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "shamayim",
            "raqia",
            "ruach",
            "malak_yhwh",
            "kavod",
        ],

        "ane_backdrop": "The systematic mapping of the world into four quarters with "
                        "numbered mountains and rivers reflects ANE geographic traditions. "
                        "The Babylonian Map of the World (c. 6th century BC) depicts the "
                        "earth as a disc surrounded by cosmic ocean with named regions and "
                        "mountains. The MUL.APIN astronomical compendium organizes stars "
                        "into three \'paths\' (Enlil, Anu, Ea) corresponding to northern, "
                        "equatorial, and southern bands of the sky, with each star assigned "
                        "a rising date. The Astronomical Book\'s gate system parallels this "
                        "Mesopotamian tradition of systematized stellar observation but "
                        "frames it theologically: the stars obey God, not fate or chance.",

        "second_temple": [
            {
                "source": "Jubilees 2:2",
                "summary": "On the first day God created the heavens and earth, the "
                           "waters, the spirits who serve before him: the angels of the "
                           "presence, the angels of sanctification, and the angels over "
                           "natural phenomena — winds, clouds, darkness, snow, hail, frost.",
                "relevance": "Jubilees confirms the Astronomical Book\'s framework: every "
                             "natural phenomenon is administered by an angel. The creation "
                             "of wind-angels on day one indicates that angelic governance "
                             "of nature is as old as creation itself.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Job 38:22-30", "note": "The storehouses of snow and hail, the channels for rain, the ice and frost of heaven — God challenges Job about the same cosmic infrastructure that the Astronomical Book maps systematically", "type": "ot"},
            {"ref": "Psalm 148:7-10", "note": "Fire and hail, snow and mist, stormy wind fulfilling his word — natural phenomena as obedient servants of divine command, the theology underlying the gate system", "type": "ot"},
            {"ref": "Jeremiah 10:13", "note": "He brings forth the wind from his storehouses — the otzarot (storehouses) of wind that 1 Enoch 76 maps as twelve gated portals", "type": "ot"},
            {"ref": "4Q208-211 (4QEn-astr a-d)", "type": "dss", "note": "The Aramaic Astronomical Book fragments, which preserve far more detailed stellar rising tables than the Ethiopic abridgment, indicating the original contained comprehensive star catalogs"},
            {"ref": "Revelation 7:1", "note": "Four angels standing at the four corners of the earth, holding back the four winds — the same cosmic geography of wind-controlling angels at cardinal directions", "type": "nt"},
            {"ref": "Ezekiel 37:9", "note": "Prophesy to the breath, come from the four winds — the four-directional wind system assumed in 1 Enoch 76 and throughout prophetic literature", "type": "ot"}
        ],

        "divine_council_note": "Chapters 76-77 reveal the depth of the divine council\'s "
                               "administrative structure. Every star has a \'leader\' (an "
                               "angelic chief), every wind gate has a supervisor, and the "
                               "four intercalary days have their own designated officers. "
                               "The cosmos is not governed by impersonal natural law but by "
                               "a vast angelic bureaucracy reporting to the Most High. This "
                               "is cosmic governance at its most granular: God rules through "
                               "an organized hierarchy of commissioned agents, each with "
                               "specific jurisdiction and accountability. When a star "
                               "deviates from its assigned gate (80:6), it is not a "
                               "malfunction but an act of rebellion — a council member "
                               "abandoning his post.",

        "sections": [
            {
                "heading": "The Stellar Gate System (76:1-5)",
                "body": "The stars, like the sun and moon, traverse the heavens through the "
                        "six-gate system. Each star rises through an appointed gate at an "
                        "appointed time and sets through its corresponding western gate. "
                        "\'Leaders of the heads of the thousands\' — angelic chiefs commanding "
                        "groups of a thousand stars — are responsible for maintaining the "
                        "stellar schedule. This military language (\'heads of thousands\') "
                        "echoes both the Watcher narrative (where twenty chiefs commanded "
                        "groups of ten, 1 Enoch 6:7) and Israelite military organization "
                        "(commanders of thousands, hundreds, fifties, and tens, Exod 18:21). "
                        "The heavenly host is literally an army, organized in ranked units "
                        "under a chain of command. The four intercalary days that bring the "
                        "year to 364 days are under the direct supervision of these stellar "
                        "leaders — they are not gaps in the calendar but specially governed "
                        "transitional days marking the solstices and equinoxes."
            },
            {
                "heading": "The Twelve Wind Gates — Moral Meteorology (76:6-14)",
                "body": "The twelve wind gates (three at each cardinal direction) produce "
                        "winds of different moral quality. From the eastern gates come "
                        "beneficial winds bringing prosperity, dew, and rain. From the "
                        "southeastern gates come dew, rain, and blessing. From the southern "
                        "gates come drought and desolation. From the southwestern and "
                        "western gates come dew, rain, but also locusts and destruction. "
                        "From the northern gates come cold, snow, frost, and hail. This "
                        "moral classification of wind reflects the Astronomical Book\'s "
                        "fundamental conviction that the physical and moral orders are "
                        "inseparable. A wind is not merely an atmospheric event but a "
                        "morally coded phenomenon: some winds express divine blessing, "
                        "others express divine judgment. The Deuteronomic covenant curses "
                        "(Deut 28:22-24) threaten scorching wind and drought as punishment "
                        "for disobedience — the same meteorological judgments that flow "
                        "from the southern and western gates in 1 Enoch 76."
            },
            {
                "heading": "The Sacred Geography of the Earth (77:1-8)",
                "body": "Chapter 77 maps the earth into four quadrants with specific "
                        "features: seven great mountains, seven great rivers, seven great "
                        "islands. The schematic numbering (four quarters, seven features in "
                        "each category) signals that this is sacred rather than empirical "
                        "geography — the world is organized according to divinely significant "
                        "numbers. The seven mountains likely include real identifiable peaks "
                        "known to the author (Hermon, Lebanon, Sinai, and others), but their "
                        "arrangement into a sevenfold system transforms cartography into "
                        "theology. The seven rivers may include the Nile, Euphrates, Tigris, "
                        "and Jordan, but again the sevenfold schema matters more than "
                        "identification. The four cardinal directions are morally coded: "
                        "east is associated with blessing (paradise lies in the east, Gen "
                        "2:8), north with judgment (Jeremiah 1:14, \'Out of the north evil "
                        "shall break forth\'). The geographic catalog places Jerusalem "
                        "implicitly at the center — the same cosmological claim made "
                        "explicitly in 1 Enoch 26:1 and Jubilees 8:19."
            }
        ]
    },

    # =========================================================================
    # ANGELIC GOVERNANCE OF NATURE (1 Enoch 78-79)
    # =========================================================================
    {
        "id": "1en-78-79",
        "ref": "1 Enoch 78-79",
        "chapter_num": 78,
        "title": "The Laws of the Luminaries and the Angelic Administration",
        "era": "astronomical",
        "type": "chapter",

        "synopsis": "Chapters 78-79 provide a systematic summary of the \'laws\' governing "
                    "the sun, moon, and stars — their appointed courses, seasonal "
                    "variations, and the precise relationship between solar and lunar "
                    "cycles. Chapter 78 returns to the moon\'s illumination patterns with "
                    "additional detail on how the moon receives its light from the sun "
                    "and how its phases correlate with its passage through the six gates. "
                    "Chapter 79 presents Uriel\'s summary charge to Enoch, emphasizing "
                    "that the complete \'law of the stars\' has been shown to him and "
                    "instructing him to record everything. The section functions as a "
                    "recapitulation and verification — Uriel confirms that Enoch has "
                    "received the full revelation and must now transmit it faithfully.",

        "key_verse": {
            "ref": "1 Enoch 79:1-2",
            "text": "And now, my son, I have shown thee everything, and the law of "
                    "all the stars of the heaven is completed. And he showed me all "
                    "the laws of these for every day, and for every season of bearing "
                    "rule, and for every year, and for its going forth, and for the "
                    "order prescribed to it every month and every week.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "malak_yhwh",
            "shamayim",
            "mishpat",
            "olam",
            "kavod",
        ],

        "ane_backdrop": "The concept that celestial bodies operate according to \'laws\' "
                        "(Akkadian: kishru, \'bond/regulation\') is attested in Mesopotamian "
                        "astronomical texts. The Enuma Elish describes Marduk assigning the "
                        "stations of the great gods as stars, fixing the year and its "
                        "divisions, and establishing the moon\'s phases. The crucial "
                        "difference in 1 Enoch is that these laws are mediated through a "
                        "named angel (Uriel) who serves as both cosmic administrator and "
                        "revelatory teacher. In Mesopotamian tradition, the astronomical "
                        "knowledge comes from the apkallu sages; in 1 Enoch, it comes "
                        "from a single archangel who reports to the divine council.",

        "second_temple": [
            {
                "source": "4Q318 (4QBrontologion / Zodiacal Calendar)",
                "summary": "A Qumran text that correlates zodiacal signs with weather "
                           "predictions and calendrical data, demonstrating that the "
                           "Qumran community engaged in practical astronomical observation "
                           "within their theological framework.",
                "relevance": "Shows that 1 Enoch 78-79\'s astronomical teachings were not "
                             "purely theoretical but connected to a living tradition of "
                             "celestial observation. 4Q318 applies Enochic astronomical "
                             "principles to weather prediction and agricultural planning.",
                "canon": False
            },
            {
                "source": "Sirach 43:1-12",
                "summary": "Ben Sira praises the sun (\'a marvelous instrument, the work "
                           "of the Most High\') and the moon (\'governing the times, an "
                           "everlasting sign\') as obedient servants of the Creator.",
                "relevance": "Ben Sira shares the Astronomical Book\'s conviction that the "
                             "luminaries obey divine commands, but lacks the technical "
                             "detail and the polemical edge about calendar disputes. This "
                             "represents the mainstream Wisdom tradition\'s engagement with "
                             "celestial theology.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Jeremiah 31:35-36", "note": "The LORD who gives the sun for light by day and the fixed order of the moon and stars for light by night — the \'fixed order\' (chuqqot) that the Astronomical Book maps in exhaustive detail", "type": "ot"},
            {"ref": "Jeremiah 33:25-26", "note": "If I have not established my covenant with day and night and the fixed order of heaven and earth — the cosmic covenant that the Astronomical Book claims to reveal", "type": "ot"},
            {"ref": "Job 38:31-33", "note": "Can you bind the chains of the Pleiades or loose the cords of Orion? Do you know the ordinances of the heavens? — God\'s challenge to Job about the very celestial laws Uriel reveals to Enoch", "type": "ot"},
            {"ref": "4Q208-211 (4QEn-astr a-d)", "type": "dss", "note": "The Aramaic Astronomical Book fragments from Qumran preserving far more detailed tables than the Ethiopic, with day-by-day solar-lunar synchronization data"},
            {"ref": "4Q318 (4QBrontologion)", "type": "dss", "note": "Qumran zodiacal calendar combining astronomical data with weather predictions, implementing the Astronomical Book\'s principles in practical form"},
            {"ref": "Psalm 136:7-9", "note": "He who made the great lights... the sun to rule over the day... the moon and stars to rule over the night — the governance language that the Astronomical Book develops into a full administrative system", "type": "ot"}
        ],

        "divine_council_note": "The \'law of the stars\' (1 Enoch 79:1) is council "
                               "legislation. Just as the Torah contains the laws governing "
                               "human conduct, the celestial torah contains the laws "
                               "governing cosmic conduct. Uriel, as the council member "
                               "responsible for the luminaries (cf. 1 Enoch 20:2), is both "
                               "the administrator who enforces these laws and the revealer "
                               "who discloses them to Enoch. The \'completion\' of the "
                               "revelation (79:1: \'the law of all the stars of the heaven "
                               "is completed\') indicates that Enoch has now received the "
                               "full cosmic legislation — he possesses the entire celestial "
                               "code, not just excerpts. This makes him the most informed "
                               "human being in history regarding the council\'s cosmic "
                               "governance.",

        "sections": [
            {
                "heading": "The Moon\'s Light Source and Phases (78:1-14)",
                "body": "Chapter 78 returns to the moon with additional precision. The "
                        "moon\'s light is not its own but borrowed from the sun: as the "
                        "moon rises, it receives light from the sun in increasing measure, "
                        "from one-fourteenth at the first visible crescent to fourteen-"
                        "fourteenths at full moon. The chapter tracks the moon\'s passage "
                        "through the six gates, noting that the moon\'s schedule does not "
                        "align with the sun\'s — this is precisely the basis for the "
                        "solar-lunar discrepancy. The moon completes its cycle in "
                        "approximately 29.5 days, meaning twelve lunar months total only "
                        "354 days, ten days short of the solar year. This accumulated "
                        "deficit is the technical reason why the Astronomical Book rejects "
                        "the lunar calendar: it \'falls behind\' the solar count and "
                        "requires periodic correction (intercalation) that the Enochic "
                        "tradition regards as human tampering with divinely fixed time. "
                        "The Aramaic fragments from 4Q208 preserve far more detailed "
                        "synchronistic tables tracking both sun and moon positions "
                        "simultaneously, indicating the original text was essentially "
                        "an astronomical reference work."
            },
            {
                "heading": "Uriel\'s Summary Charge to Enoch (79:1-6)",
                "body": "Chapter 79 presents Uriel\'s formal summary of the revelation. "
                        "\'The law of all the stars of the heaven is completed\' — the "
                        "revelation is comprehensive and final. Uriel has shown Enoch "
                        "\'all the laws of these for every day, and for every season of "
                        "bearing rule, and for every year, and for its going forth, and "
                        "for the order prescribed to it every month and every week\' "
                        "(79:2). The word \'law\' (Ge\'ez: heg; corresponding to Hebrew "
                        "choq or torah) is critical: these are not observations but "
                        "ordinances. The celestial bodies do not merely follow patterns; "
                        "they obey commands. The charge to Enoch is simultaneously a "
                        "charge to the reader: this knowledge exists, has been revealed, "
                        "and must be preserved and obeyed. The closing verses of chapter "
                        "79 note that Uriel showed Enoch \'every one of them\' — no star, "
                        "no gate, no wind has been omitted. The comprehensiveness of "
                        "the revelation validates the Enochic calendar against all "
                        "competitors: no alternative tradition can claim a more complete "
                        "angelic disclosure."
            },
            {
                "heading": "Calendar as Covenant Marker",
                "body": "The insistence on comprehensive cosmic legislation in chapters "
                        "78-79 reflects the Enochic tradition\'s understanding of "
                        "calendar as covenant identity. In the same way that circumcision "
                        "marked the Abrahamic covenant and Sabbath observance marked the "
                        "Sinai covenant, the 364-day solar calendar marked the Enochic "
                        "covenant community. To observe the correct calendar was to "
                        "declare allegiance to the revealed cosmic order; to observe the "
                        "wrong calendar was to stand outside the community of the "
                        "faithful. This explains the extraordinary detail of the "
                        "Astronomical Book: it is not academic astronomy but covenant "
                        "catechesis. Every table of stellar risings, every gate system, "
                        "every measurement of daylight and darkness serves to form the "
                        "reader into a person who \'reckons his days\' correctly (82:4). "
                        "The Qumran community implemented this catechetical function "
                        "through their extensive calendrical corpus (4Q320-330), which "
                        "applied the Astronomical Book\'s principles to the daily "
                        "practice of worship, priestly rotation, and festival "
                        "observance."
            }
        ]
    },

    # =========================================================================
    # HISTORICAL INSERT: THE JUBILEES AND QUMRAN CALENDAR CONNECTION
    # =========================================================================
    {
        "id": "insert-jubilees-qumran-calendar",
        "ref": "Historical Context",
        "chapter_num": None,
        "title": "From Enoch to Jubilees to Qumran — The 364-Day Calendar Tradition",
        "era": "astronomical",
        "type": "historical_insert",

        "synopsis": "The 364-day solar calendar of the Astronomical Book did not remain "
                    "a theoretical construct. It was adopted and further developed by the "
                    "Book of Jubilees (c. 160-150 BC), which wove the calendar into a "
                    "retelling of Genesis-Exodus as absolute divine law. The Qumran "
                    "community (c. 150 BC - 68 AD) then implemented the calendar in daily "
                    "practice, producing an extensive corpus of calendrical texts (4Q317-"
                    "330) that scheduled priestly rotations, festivals, and Sabbaths "
                    "according to the Enochic solar system. This section traces the "
                    "chain of transmission from the Astronomical Book through Jubilees "
                    "to the Dead Sea Scrolls, and considers its implications for "
                    "understanding Second Temple Judaism\'s deepest theological division.",

        "key_verse": None,
        "hebrew_terms": [
            "shamayim",
            "qodesh",
            "berit",
            "malak_yhwh",
            "mishpat",
        ],
        "ane_backdrop": None,
        "second_temple": [],

        "cross_refs": [
            {"ref": "Jubilees 6:32-38", "note": "The most explicit mandating of the 364-day calendar: those who follow the moon \'will disturb the order\' and \'mingle holy things with profane\'", "type": "pseudepigrapha"},
            {"ref": "Jubilees 6:17-22", "note": "God establishes the covenant with Noah with a heavenly sign, linking the post-Flood calendar to covenant theology — right calendar as covenant fidelity", "type": "pseudepigrapha"},
            {"ref": "4Q320 (4QCalendrical Document A)", "type": "dss", "note": "The foundational Qumran calendrical text synchronizing the 364-day year with the 24 priestly courses (mishmarot), establishing the practical implementation of the Enochic calendar for Temple service"},
            {"ref": "4Q321 (4QCalendrical Document Ba)", "type": "dss", "note": "Qumran text tracking lunar phases alongside the 364-day solar calendar, demonstrating the community\'s integration of lunar observation within the Enochic framework"},
            {"ref": "4Q394-399 (4QMMT)", "type": "dss", "note": "The Halakhic Letter opening with calendrical data — the calendar dispute as the primary reason for sectarian separation from the Temple establishment"},
            {"ref": "11Q13 (11QMelchizedek)", "type": "dss", "note": "Qumran eschatological text using Jubilee-period calculations derived from the 364-day calendar to predict the eschatological \'Jubilee of Jubilees\'"},
            {"ref": "Galatians 4:10", "note": "Paul\'s warning against observing \'days, months, seasons, and years\' may engage the very calendrical controversy that the Enochic-Jubilean-Qumran tradition fueled", "type": "nt"}
        ],

        "divine_council_note": "The chain of transmission — Uriel to Enoch to Methuselah "
                               "to \'the generations of the world\' (82:1) — is a divine "
                               "council communication protocol. The calendar is not human "
                               "discovery but angelic revelation: it passes from the council "
                               "through a single authorized channel (Uriel), to a single "
                               "authorized human recipient (Enoch), who transmits it through "
                               "the patriarchal line. Every link in the chain is divinely "
                               "authorized. The Jubilees expansion adds Moses as a second "
                               "channel (God reveals the calendar on Sinai, Jub 6:32-38), "
                               "and the Qumran community understood themselves as the end "
                               "of the chain — the remnant who faithfully preserved the "
                               "revealed calendar against the apostasy of the Temple "
                               "establishment.",

        "sections": [
            {
                "heading": "The Astronomical Book\'s Calendar — Original Foundation",
                "body": "The Astronomical Book (1 Enoch 72-82) establishes the 364-day "
                        "solar calendar as a divinely revealed cosmic law. The key "
                        "features are: (1) twelve months of 30 days each (360 days), "
                        "plus four intercalary days at the solstices and equinoxes (364 "
                        "total); (2) exactly 52 weeks, ensuring that every date falls on "
                        "the same weekday every year; (3) the calendar is mediated by "
                        "Uriel, the archangel over the luminaries, giving it the highest "
                        "possible angelic authority; (4) the lunar cycle is acknowledged "
                        "but declared subordinate — the moon\'s 354-day year \'falls "
                        "behind\' and is insufficient for regulating festivals. The "
                        "Astronomical Book does not address the practical problem of "
                        "drift (the actual solar year is ~365.25 days), focusing instead "
                        "on the theological perfection of the 364-day system. The Aramaic "
                        "fragments from Qumran (4Q208-211) show that the original text "
                        "was far more detailed than the surviving Ethiopic version, with "
                        "comprehensive day-by-day synchronistic tables that functioned as "
                        "a working astronomical reference."
            },
            {
                "heading": "Jubilees — Calendar as Absolute Law",
                "body": "The Book of Jubilees (c. 160-150 BC) takes the Astronomical "
                        "Book\'s calendar and elevates it from revealed knowledge to "
                        "absolute covenant law. In Jubilees 6:32-38, the 364-day calendar "
                        "is embedded in the Noah narrative: after the Flood, God establishes "
                        "the calendar as part of the renewed covenant. Those who follow the "
                        "moon \'will assuredly make observations of the moon — how it "
                        "disturbs the seasons and comes in from year to year ten days too "
                        "soon\' (6:36). The accusation is devastating: lunar-calendar users "
                        "\'will mingle holy things with profane\' (6:37) — they will "
                        "celebrate festivals on the wrong days, rendering the entire "
                        "sacrificial system invalid. Jubilees goes further than the "
                        "Astronomical Book by grounding the calendar in Mosaic revelation: "
                        "the Angel of the Presence dictates the entire book to Moses on "
                        "Sinai (Jub 1:27-29), meaning the calendar now has double "
                        "authority — both Enochic (through Uriel) and Mosaic (through the "
                        "Angel of the Presence). This dual legitimation was critical for "
                        "communities that accepted both Enochic and Mosaic authority."
            },
            {
                "heading": "Qumran — Implementation and Separation",
                "body": "The Qumran community transformed the theoretical calendar of "
                        "1 Enoch and the legal calendar of Jubilees into a working "
                        "liturgical system. The calendrical corpus from Cave 4 (4Q320-330) "
                        "includes: priestly rotation schedules assigning the 24 courses "
                        "(mishmarot) to specific weeks of the 364-day year; festival "
                        "calendars listing the dates of all major festivals on their "
                        "fixed weekdays; Sabbath calendars covering multiple years; and "
                        "synchronistic tables correlating solar dates, lunar phases, and "
                        "priestly duties. 4Q317 (Phases of the Moon) implements the "
                        "fourteen-part lunar illumination system of 1 Enoch 73, tracking "
                        "the moon day by day within the solar framework. 4Q318 "
                        "(Brontologion) correlates zodiacal signs with weather and "
                        "calendar. The practical implication was that the Qumran community "
                        "celebrated every festival on a different day than the Jerusalem "
                        "Temple. Their Passover, their Day of Atonement, their Feast of "
                        "Weeks — all fell on different dates. This calendrical disconnect "
                        "made participation in Temple worship impossible and was likely "
                        "the proximate cause of the community\'s physical separation "
                        "from Jerusalem."
            }
        ]
    },

    # =========================================================================
    # COSMIC DISRUPTION AND CONCLUSION (1 Enoch 80-82)
    # =========================================================================
    {
        "id": "1en-80-82",
        "ref": "1 Enoch 80-82",
        "chapter_num": 80,
        "title": "The Disruption of Order and the Heavenly Tablets",
        "era": "astronomical",
        "type": "chapter",

        "synopsis": "The final chapters of the Astronomical Book shift from cosmic "
                    "description to cosmic warning. Chapter 80 describes an "
                    "eschatological disruption of the natural order: the luminaries "
                    "will deviate from their courses, rain will fail, the earth will "
                    "withhold its fruit, and 'sinners shall not observe the seasons.' "
                    "Chapter 81 narrates Enoch reading the 'heavenly tablets' — the "
                    "divine record of all human deeds and all future events. Chapter "
                    "82 concludes with the four intercalary days and Enoch's charge "
                    "to his son Methuselah to preserve and transmit this celestial "
                    "knowledge to future generations.",

        "key_verse": {
            "ref": "1 Enoch 80:2-4",
            "text": "And in the days of the sinners the years shall be shortened, "
                    "and their seed shall be tardy on their lands and fields... and "
                    "many chiefs of the stars shall transgress the order prescribed... "
                    "and the entire law of the stars shall be closed to the sinners.",
            "translation": "Charles"
        },

        "hebrew_terms": [
            "shamayim",
            "mishpat",
            "cherem",
            "olam",
            "tsaddiq",
            "lukhot_shamayim",
        ],

        "ane_backdrop": "The concept of cosmic disruption as a sign of moral "
                        "degradation is widespread in the ANE. Mesopotamian omen "
                        "literature (the Enuma Anu Enlil series) treats celestial "
                        "anomalies — eclipses, unusual planetary positions — as "
                        "portents of earthly disaster. The Egyptian concept of Ma'at "
                        "(cosmic order) held that when the pharaoh failed to maintain "
                        "justice, the natural order itself collapsed. 1 Enoch 80's "
                        "vision of cosmic disruption draws on this shared conviction "
                        "that moral and natural order are interlinked: when one fails, "
                        "the other follows.",

        "second_temple": [
            {
                "source": "Jubilees 1:14",
                "summary": "God warns Moses that Israel will 'forget all of my laws "
                           "and all of my commandments... and they will err as to new "
                           "moons, sabbaths, festivals, jubilees, and ordinances.'",
                "relevance": "Jubilees shares the Astronomical Book's conviction that "
                             "calendrical error is a symptom of moral failure. The two "
                             "texts form a unified front in the calendrical controversy.",
                "canon": False
            },
            {
                "source": "4Q180 (Ages of Creation)",
                "summary": "A Qumran text that periodizes history using the 364-day "
                           "calendar framework, dividing all of time into "
                           "predetermined epochs recorded on heavenly tablets.",
                "relevance": "Demonstrates that the 'heavenly tablets' concept of "
                             "1 Enoch 81 was actively used at Qumran to structure their "
                             "understanding of history as divinely foreordained.",
                "canon": False
            }
        ],

        "cross_refs": [
            {"ref": "Isaiah 24:20-23", "note": "The earth staggers, the moon is confounded, the sun is ashamed — prophetic cosmic disruption language that 1 Enoch 80 develops into a systematic eschatological vision", "type": "ot"},
            {"ref": "Joel 2:10, 30-31", "note": "The sun and moon are darkened, the stars withdraw their shining — prophetic cosmic signs that become standard apocalyptic imagery", "type": "ot"},
            {"ref": "Matthew 24:29", "note": "The sun will be darkened, the moon will not give its light, the stars will fall from heaven — Jesus' Olivet Discourse draws on the same cosmic-disruption tradition as 1 Enoch 80", "type": "nt"},
            {"ref": "Revelation 6:12-14", "note": "The sun became black, the moon became like blood, the stars fell — the Apocalypse's cosmic disruption echoes both the prophets and 1 Enoch 80's vision of stellar disorder", "type": "nt"},
            {"ref": "Psalm 19:7", "note": "The law (torah) of the LORD is perfect — the Astronomical Book argues that the cosmic law written on heavenly tablets is similarly perfect, and human calendars must conform to it", "type": "ot"},
            {"ref": "Exodus 32:15-16", "note": "The tablets of stone, written by the finger of God — the 'heavenly tablets' of 1 Enoch 81 extend this concept: God's writing records not just the Law but all of history and destiny", "type": "ot"},
            {"ref": "4Q208-211 (4QEn-astr a-d)", "type": "dss", "note": "The Qumran Aramaic fragments of the Astronomical Book, including material much more detailed than the Ethiopic text, confirming the extreme antiquity of this section"},
            {"ref": "Revelation 20:12", "note": "Books were opened... the dead were judged by what was written in the books — the heavenly tablets of 1 Enoch 81 as forerunner to the Apocalypse's books of judgment", "type": "nt"}
        ],

        "divine_council_note": "The 'heavenly tablets' of 1 Enoch 81 are the divine "
                               "council's official records. They contain three types of "
                               "information: (1) the deeds of all humanity, written as "
                               "they occur — the basis for judgment; (2) the future "
                               "history of the world, already determined — the basis "
                               "for prophecy; (3) the cosmic laws that govern the "
                               "luminaries and the calendar — the basis for worship. "
                               "Access to the tablets is the ultimate expression of "
                               "council membership: to read them is to know what God "
                               "knows. Enoch is granted this access as a human admitted "
                               "to the council's innermost archives. The concept of "
                               "heavenly tablets recurs throughout Second Temple "
                               "literature (Jubilees passim, Daniel 10:21's 'book of "
                               "truth') and underlies Revelation's sealed scroll (Rev "
                               "5:1-5) that only the Lamb is worthy to open.",

        "sections": [
            {
                "heading": "The Disruption of the Luminaries (80:1-8)",
                "body": "Chapter 80 shifts from the present order to the eschatological "
                        "future when that order will be disrupted. 'In the days of the "
                        "sinners the years shall be shortened, and their seed shall be "
                        "tardy on their lands and fields, and all things on the earth "
                        "shall alter' (80:2). The luminaries will deviate: 'Many chiefs "
                        "of the stars shall transgress the order prescribed, and these "
                        "shall alter their orbits and tasks' (80:6). Stars are not mere "
                        "objects but agents — 'chiefs' (like the Watcher leaders of "
                        "chapters 6-7) who can obey or rebel. Their transgression is "
                        "part of the eschatological unraveling: as the end approaches, "
                        "even the cosmic infrastructure breaks down. 'Rain shall be "
                        "kept back and the heaven shall withhold it... the fruits of "
                        "the earth shall be backward, and shall not grow in their time, "
                        "and the fruits of the trees shall be withheld in their time' "
                        "(80:2-3). This agricultural collapse parallels the covenant "
                        "curses of Deuteronomy 28:23-24 ('your heavens shall be bronze "
                        "and your earth iron'). The cosmic disruption is not random "
                        "catastrophe but covenant judgment: creation responds to "
                        "humanity's sin by withdrawing its productivity."
            },
            {
                "heading": "The Heavenly Tablets — Enoch Reads the Record (81:1-6)",
                "body": "Chapter 81 narrates Enoch's encounter with the heavenly "
                        "tablets, the most sacred documents in the divine archive. 'And "
                        "I looked and saw therein written on heavenly tablets every "
                        "deed of every generation till the day of judgement' (81:2). "
                        "The tablets contain a comprehensive record of all human "
                        "history — past, present, and future — written by divine "
                        "decree. This concept of heavenly books is deeply rooted in "
                        "the OT: Exodus 32:32 refers to God's 'book' in which names "
                        "are written; Psalm 69:28 mentions the 'book of the living'; "
                        "Daniel 7:10 describes 'books opened' at the divine judgment; "
                        "and Daniel 10:21 references the 'book of truth.' The "
                        "Astronomical Book extends this concept: the heavenly tablets "
                        "are not merely records of judgment but blueprints of cosmic "
                        "order. They contain the calendar, the laws of the luminaries, "
                        "and the predetermined course of history. Enoch reads them all "
                        "and 'blessed the great Lord, the King of glory forever' "
                        "(81:3). The reading triggers worship — knowledge of the "
                        "divine plan leads to praise, not despair, because the plan "
                        "culminates in the triumph of righteousness."
            },
            {
                "heading": "Enoch's Charge to Methuselah — Preserving the Calendar (82:1-6)",
                "body": "The Astronomical Book concludes with Enoch transmitting his "
                        "celestial knowledge to his son Methuselah. 'And now, my son "
                        "Methuselah, all these things I am recounting to thee and "
                        "writing down for thee, and I have revealed to thee everything, "
                        "and given thee books concerning all these: so preserve, my "
                        "son Methuselah, the books from thy father's hand, and deliver "
                        "them to the generations of the world' (82:1). The charge "
                        "establishes a chain of prophetic transmission: Enoch received "
                        "from Uriel, Methuselah receives from Enoch, and he is to "
                        "deliver the knowledge 'to the generations of the world.' "
                        "This transmission chain legitimizes the text itself: the "
                        "Astronomical Book claims to be the very document that Enoch "
                        "gave to Methuselah, preserved across the millennia. The four "
                        "intercalary days are noted: they are 'not reckoned in the "
                        "reckoning of the year' in the sense that they are extra-monthly "
                        "days added at the quarter-turns (82:4-6). Leaders are "
                        "appointed over the four seasons — named angels who preside "
                        "over the quarterly divisions. The final emphasis is that "
                        "'blessed are all the righteous... who walk in the way of "
                        "righteousness and sin not as the sinners, in the reckoning "
                        "of all their days' (82:4). Right calendar = right worship = "
                        "righteousness. The equation is absolute."
            }
        ]
    },

    # =========================================================================
    # HISTORICAL INSERT: THE CALENDAR CONTROVERSY
    # =========================================================================
    {
        "id": "insert-calendar-controversy",
        "ref": "Historical Context",
        "chapter_num": None,
        "title": "The Solar Calendar Controversy — Enoch, Jubilees, and Qumran",
        "era": "astronomical",
        "type": "historical_insert",

        "synopsis": "The 364-day solar calendar advocated in the Astronomical Book "
                    "was not merely an academic preference but a central identity "
                    "marker for the Qumran community and their predecessors. The "
                    "Jerusalem Temple by the 2nd century BC had adopted a lunisolar "
                    "calendar (based on lunar months with intercalary adjustments). "
                    "The Enochic-Jubilean tradition considered this a catastrophic "
                    "apostasy: worshiping on the wrong days meant the festivals were "
                    "invalid and the Temple service was defiled. This calendrical "
                    "conflict may have been the proximate cause of the Qumran "
                    "community's separation from the Jerusalem establishment.",

        "key_verse": None,
        "hebrew_terms": [
            "shamayim",
            "qodesh",
            "berit",
            "mishpat",
            "avodah",
        ],
        "ane_backdrop": None,
        "second_temple": [],

        "cross_refs": [
            {"ref": "Jubilees 6:32-38", "note": "The most polemical text in the solar calendar controversy: those who follow the moon 'will disturb the order and mingle holy things with profane'", "type": "pseudepigrapha"},
            {"ref": "1 Enoch 75:2", "note": "The leaders of the stars who 'do not come forth in their time' — deviation from the calendar is equivalent to angelic rebellion", "type": "pseudepigrapha"},
            {"ref": "Daniel 7:25", "note": "The horn will 'think to change the times and the law' — changing the sacred calendar is associated with the ultimate enemy of God's people", "type": "ot"},
            {"ref": "4Q320-330 (Calendrical Documents)", "type": "dss", "note": "The Qumran calendrical corpus: priestly rotation schedules, festival calendars, and sabbath lists all based on the 364-day year, demonstrating practical implementation of the Enochic calendar"},
            {"ref": "4Q394-399 (4QMMT)", "type": "dss", "note": "The 'Halakhic Letter' that begins with a calendrical section, likely describing the festival differences between the Qumran community and the Temple establishment — possibly the founding document of the community's separation"},
            {"ref": "Galatians 4:10", "note": "Paul warns against observing 'days, months, seasons, and years' — possibly engaging the same calendrical controversy that divided Second Temple Judaism", "type": "nt"}
        ],

        "divine_council_note": "The calendrical controversy is fundamentally a "
                               "question about which calendar reflects the divine "
                               "council's decree. The Astronomical Book claims that "
                               "the 364-day solar calendar was revealed by Uriel, the "
                               "archangel charged with overseeing the luminaries — "
                               "direct council authority. The mainstream Temple "
                               "establishment, by contrast, followed a calendar based "
                               "on empirical observation of the moon. The dispute is "
                               "thus between revealed knowledge (the angelic disclosure "
                               "to Enoch) and observed knowledge (human calculation "
                               "from lunar sighting). For the Enochic tradition, "
                               "revelation always trumps observation.",

        "sections": [
            {
                "heading": "The Two Calendars — Solar vs. Lunisolar",
                "body": "The 364-day solar calendar of 1 Enoch and Jubilees divides "
                        "the year into four quarters of 91 days each (3 months of 30 "
                        "days + 1 intercalary day). Twelve months of 30 days = 360 "
                        "days + 4 intercalary days = 364 days = exactly 52 weeks. "
                        "The lunisolar calendar used by the mainstream Temple "
                        "establishment (and later standardized in the rabbinic "
                        "calendar) uses months of 29 or 30 days keyed to the lunar "
                        "cycle, producing a year of approximately 354 days, with an "
                        "intercalary month (Adar II) added roughly every three years "
                        "to realign with the solar year. The practical consequence "
                        "is that on the lunisolar calendar, festivals fall on "
                        "different days of the week each year. Passover might fall on "
                        "a Monday one year and a Thursday the next. On the 364-day "
                        "calendar, Passover is always on the same weekday. For the "
                        "Enochic tradition, this fixed alignment was non-negotiable: "
                        "God established both the Sabbath and the festivals, and they "
                        "must never conflict. A Passover that falls on the Sabbath "
                        "creates a halakhic problem; the 364-day calendar avoids it "
                        "entirely by design."
            },
            {
                "heading": "The Split with the Temple — 4QMMT and the Separation",
                "body": "The fragmentary text 4QMMT (Miqsat Ma'asei ha-Torah, 'Some "
                        "Works of the Law'), identified by Strugnell and Qimron as a "
                        "foundational sectarian document, opens with a calendrical "
                        "section that lists the dates of festivals according to the "
                        "364-day calendar. This has been interpreted as a letter from "
                        "the early Qumran leadership (possibly the Teacher of "
                        "Righteousness) to the Jerusalem establishment, explaining "
                        "the points of disagreement that necessitate separation. The "
                        "calendar is listed first — it is the primary issue. If the "
                        "Temple is keeping the wrong calendar, then every sacrifice, "
                        "every festival, every priestly rotation is invalid. The "
                        "Qumran community's withdrawal to the desert thus becomes "
                        "comprehensible: they could not participate in a Temple "
                        "service they considered temporally defiled. The War Scroll "
                        "(1QM) envisions a future when the sons of light will "
                        "reconquer Jerusalem and restore the correct calendar — "
                        "the Enochic solar calendar — to the Temple."
            },
            {
                "heading": "Implications for NT Studies",
                "body": "The calendrical controversy may illuminate several puzzles "
                        "in the NT. The discrepancy between the Synoptic Gospels and "
                        "John regarding the date of the Last Supper / crucifixion "
                        "(was the Last Supper a Passover meal or not?) has been "
                        "explained by some scholars (Jaubert, 1957) as a reflection "
                        "of different calendars: Jesus may have celebrated Passover "
                        "on the solar calendar (Tuesday evening), while the Temple "
                        "celebrated on the lunisolar calendar (Friday evening). This "
                        "would allow both accounts to be historically accurate. The "
                        "hypothesis is contested but demonstrates that the Enochic "
                        "calendrical tradition was not a dead issue by the 1st century "
                        "AD. Paul's warning in Galatians 4:10 against observing 'days, "
                        "months, seasons, and years' may also engage the calendrical "
                        "controversy, and Colossians 2:16's reference to 'festival, "
                        "new moon, or sabbath' may reflect tensions between solar and "
                        "lunar reckonings in early Christian communities that included "
                        "both mainstream and sectarian Jewish converts."
            }
        ]
    }
]
