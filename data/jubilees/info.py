"""
info.py — Book of Jubilees: Scholarly Text Introduction

Honest scholarly introduction to the "Little Genesis" — a Second Temple retelling
of Genesis-Exodus that was enormously popular at Qumran and preserves important
developments in the Watchers tradition.
"""

TEXT_INFO = {
    "text_id": "jubilees",
    "display_name": "Book of Jubilees (Little Genesis)",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "non-canonical",
        "label": "Non-Canonical — Pseudepigrapha (Ethiopian Orthodox exception)",
        "detail": "The Book of Jubilees is NOT part of the Protestant, Catholic, or Eastern "
                  "Orthodox canon. As with 1 Enoch, the Ethiopian Orthodox Tewahedo Church is "
                  "the sole exception, including Jubilees in its broader canon. In Western "
                  "scholarship, Jubilees is classified as Old Testament Pseudepigrapha. However, "
                  "its importance for understanding Second Temple Judaism is immense. With 15 or "
                  "more manuscript fragments recovered from Qumran (4Q216-227 and others), "
                  "Jubilees was one of the most frequently copied texts at the Dead Sea — more "
                  "copies than most canonical books received there. The Damascus Document (CD XVI.3-4) "
                  "explicitly cites the 'Book of the Divisions of the Times into their Jubilees and "
                  "Weeks' as authoritative. This means the Qumran community treated Jubilees as "
                  "something close to scripture, even if later Jewish and Christian tradition did not."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "The text presents itself as a direct divine revelation given to Moses by "
                       "the Angel of the Presence (malak ha-panim) on Mount Sinai during the "
                       "forty days described in Exodus 24:18. The opening reads: 'This is the "
                       "history of the division of the days of the law and of the testimony, of "
                       "the events of the years, of their year weeks, of their jubilees throughout "
                       "all the years of the world, as the Lord spoke to Moses on Mount Sinai.' "
                       "The entire book is framed as the Angel of the Presence dictating to Moses "
                       "from the 'heavenly tablets' — a pre-existing divine record of all history.",

        "scholarly_debate": "Jubilees is universally recognized by scholars as a pseudepigraphic "
                           "composition — it was not written by Moses or dictated by an angel, but "
                           "was composed by an anonymous Jewish author who attributed it to Moses "
                           "to give it maximum authority. This was a well-established literary "
                           "convention in the Second Temple period. The author was clearly a learned "
                           "scribe with deep knowledge of the Torah, likely associated with priestly "
                           "circles concerned about calendar observance, Gentile contamination, and "
                           "halakhic (legal) precision.\n\n"
                           "The single-author hypothesis is widely accepted: unlike 1 Enoch, which "
                           "is a composite of five distinct works, Jubilees shows consistent style, "
                           "vocabulary, and theological perspective throughout, pointing to a single "
                           "author working from Genesis 1 through Exodus 19. James VanderKam, the "
                           "leading Jubilees scholar, dates the composition to ~160-150 BC based on "
                           "internal evidence (awareness of the Maccabean crisis but writing after "
                           "the rededication of the Temple in 164 BC).",

        "bottom_line": "Jubilees was written by an anonymous Jewish priest-scribe around 160-150 BC "
                       "who recast the Genesis-Exodus narrative to address urgent concerns of his "
                       "day: calendar reform, Gentile influence, and the need for strict Torah "
                       "observance. The Mosaic attribution is a literary device, not a historical "
                       "claim. The author's theological agenda is real and should be recognized — "
                       "he is not simply retelling Genesis but reshaping it to serve his community's "
                       "convictions."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "The text claims to record revelation given during the Sinai theophany "
                       "(~1446 BC by traditional chronology, during the events of Exodus 24).",
        "critical_range": "Composed ~160-150 BC during the Maccabean period. The text shows "
                         "awareness of the crisis under Antiochus IV Epiphanes (167-164 BC) and "
                         "the Maccabean response, but the author writes from a position of relative "
                         "stability after the Temple's rededication. The intense concern about "
                         "Hellenistic cultural influence and intermarriage with Gentiles reflects "
                         "the social pressures of the mid-2nd century BC.",
        "evidence": "The strongest dating evidence is threefold: (1) The Qumran fragments — the "
                    "oldest manuscript (4Q216) is paleographically dated to ~125-100 BC, meaning "
                    "the text was already composed and in circulation by then, pushing composition "
                    "earlier. (2) The Animal Apocalypse of 1 Enoch (chs. 85-90, ~165-160 BC) and "
                    "Jubilees share traditions and concerns, suggesting roughly contemporary "
                    "composition. (3) Jubilees' polemic against Hellenistic practices (gymnasium "
                    "nudity, abandoning circumcision, calendar reform) fits precisely the Maccabean "
                    "era. The Damascus Document's citation of Jubilees as authoritative confirms "
                    "the text had achieved significant status by the 1st century BC at latest."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Conservative priestly-scribal circles in Palestine who were deeply "
                            "concerned about Hellenistic influence on Judaism. The audience valued "
                            "strict Torah observance, the 364-day solar calendar, separation from "
                            "Gentiles, and precise halakhic practice. The Qumran community clearly "
                            "embraced this text, though Jubilees may have been composed for a broader "
                            "priestly audience before the Qumran sect fully separated from Jerusalem.",

        "purpose": "Jubilees has a clear and ambitious agenda: to demonstrate that the Torah's laws "
                   "were not innovations given at Sinai but were eternal truths inscribed on the "
                   "'heavenly tablets' from creation and observed by the patriarchs long before "
                   "Moses. Abraham kept the Feast of Tabernacles. Noah observed the laws of "
                   "sacrifice. The 364-day solar calendar was ordained at creation. By pushing "
                   "Torah observance back to the patriarchal period, the author argues that these "
                   "practices are woven into the fabric of creation itself — making any deviation "
                   "(especially Hellenistic innovation) a cosmic offense, not merely a cultural "
                   "preference.",

        "theological_intent": "Jubilees is fighting a two-front war. Externally, it combats "
                             "Hellenistic assimilation — the pressure on Jews to adopt Greek customs, "
                             "abandon circumcision, eat with Gentiles, and follow the Seleucid calendar. "
                             "Internally, it promotes a specific form of Judaism: solar calendar "
                             "observance, radical separation from Gentiles, and a particular reading "
                             "of Torah law. The anti-Gentile polemic is intense — Jubilees portrays "
                             "intermarriage with non-Jews as an abomination worthy of death (Jubilees "
                             "30:7-17) and frames Gentile nations as inherently under demonic influence. "
                             "This is theology under siege — a community fighting for survival by "
                             "hardening its boundaries."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Hebrew. Unlike 1 Enoch (which was composed in Aramaic), Jubilees was written "
                    "in Hebrew — confirmed by the Qumran fragments (4Q216-227), which are all "
                    "in Hebrew.",
        "script": "Late Second Temple Hebrew script (Qumran fragments). The text was subsequently "
                  "translated into Greek (now mostly lost), and from Greek into Latin (fragmentary) "
                  "and Ge'ez (Ethiopic) — the only language preserving the complete text.",
        "linguistic_notes": "The Hebrew of the Qumran fragments matches the style of late biblical "
                           "Hebrew with influences from the emerging Mishnaic register. The author "
                           "deliberately imitates the language and style of the Pentateuch — this is "
                           "not surprising given that the text presents itself as Mosaic revelation. "
                           "The Hebrew composition is significant: it suggests the author intended "
                           "Jubilees to be read as a companion to the Torah itself, written in the "
                           "sacred language rather than the Aramaic vernacular.",
        "grammar_match": "The Hebrew of Jubilees is consistent with other late Second Temple Hebrew "
                        "compositions (Ben Sira, some Qumran sectarian texts). It is literary Hebrew "
                        "with biblical archaizing — the author knew the Torah intimately and modeled "
                        "his language on it. The Qumran fragments confirm authentic Second Temple "
                        "period composition; this is not a later forgery."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "Jubilees closely follows the canonical Genesis-Exodus narrative but adds "
                   "substantial theological content not found in — and sometimes in tension with — "
                   "the canonical text. It is a rewritten Bible, not an independent revelation.",

        "where_it_aligns": [
            "The basic narrative arc faithfully follows Genesis 1 through Exodus 19 — creation, "
            "patriarchs, Egypt, exodus. The author knows the Torah thoroughly and respects its "
            "narrative structure.",
            "The Watchers tradition (Jubilees 5) retells Genesis 6:1-4 in a way consistent with "
            "1 Enoch's reading and the interpretation reflected in Jude 6 and 2 Peter 2:4.",
            "The emphasis on covenant faithfulness and obedience to God's commands is entirely "
            "consistent with the Torah's own emphases (Deuteronomy 6-8, 28-30).",
            "The patriarchal narratives add detail but do not fundamentally contradict the "
            "canonical accounts of Abraham, Isaac, Jacob, and Joseph.",
            "The portrayal of angelic beings participating in God's governance of creation is "
            "consistent with the biblical divine council framework (Psalm 82, 89:5-7, "
            "Deuteronomy 32:8-9)."
        ],

        "where_it_diverges": [
            "The 364-day solar calendar directly conflicts with the lunisolar calendar embedded "
            "in the Torah's festival legislation (Leviticus 23). If the festivals fall on "
            "different days, one calendar must be wrong — and the canonical Torah's calendar is "
            "tied to lunar observation.",
            "The intense anti-Gentile polemic goes well beyond anything in Genesis. The canonical "
            "text includes Melchizedek (a non-Israelite priest blessed by God), Abimelech (a "
            "Philistine who feared God), and the Abrahamic promise that 'all families of the "
            "earth shall be blessed' (Genesis 12:3). Jubilees' blanket hostility toward Gentiles "
            "is in tension with this universal vision.",
            "The claim that Torah laws were observed by the patriarchs and inscribed on heavenly "
            "tablets from creation is a theological assertion, not something found in Genesis "
            "itself. Genesis shows the patriarchs practicing customs that sometimes differ from "
            "later Torah law (e.g., Jacob marrying two sisters, which Leviticus 18:18 prohibits).",
            "The Mastema figure (prince of demons retained to test humanity) adds a systematic "
            "demonology not present in the canonical text. While the concept of spiritual "
            "opposition exists in scripture (Job 1-2, 1 Chronicles 21:1), Jubilees' framework "
            "is more developed than anything canonical.",
            "Some narrative additions (Abraham's war against ravens at age 14, detailed accounts "
            "of patriarchal testaments) are pious fiction — edifying stories without canonical basis."
        ],

        "reader_guidance": "Jubilees is best read as an ancient Jewish commentary on Genesis — one "
                          "that retells the story with theological expansions reflecting the author's "
                          "community and concerns. Where it faithfully follows the canonical narrative, "
                          "it provides helpful Second Temple perspective. Where it adds laws, calendar "
                          "requirements, or anti-Gentile polemic, recognize these as the author's "
                          "interpretive additions, not divine revelation. The Watchers material and "
                          "Mastema tradition are valuable for understanding how the demonic realm was "
                          "understood in the period between the Testaments — but canonical scripture "
                          "remains the final authority."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "Hebrew fragments from Qumran Caves 1, 2, 3, 4, and 11 — at least 15 "
                    "manuscripts (4Q216-227, 1Q17-18, 2Q19-20, 3Q5, 11Q12). The oldest fragment "
                    "(4Q216) dates to approximately 125-100 BC. The sheer number of copies rivals "
                    "Deuteronomy, Psalms, and Isaiah at Qumran, demonstrating that this text held "
                    "extraordinary authority for that community.",
        "major_witnesses": [
            {"name": "Dead Sea Scrolls (4Q216-227, 1Q17-18, etc.)", "date": "~125 BC - 68 AD",
             "note": "15+ Hebrew manuscripts — fragmentary but covering substantial portions of the "
                     "text. These are the earliest witnesses and confirm Hebrew as the original language. "
                     "The quantity of copies is remarkable and rivals the most popular canonical books at Qumran."},
            {"name": "Ethiopic manuscripts", "date": "14th-18th century AD (copies of much older tradition)",
             "note": "Approximately 25-30 Ge'ez manuscripts preserve the COMPLETE text. As with "
                     "1 Enoch, Ethiopic is the only language in which the full text survives. The "
                     "Ge'ez translation was made from Greek, likely in the 5th-6th century AD."},
            {"name": "Latin fragments", "date": "5th-6th century AD",
             "note": "Partial Latin translation preserving roughly one-quarter of the text. Translated "
                     "from Greek. Provides an independent check on the Ethiopic version for the "
                     "portions it covers."},
            {"name": "Syriac fragments", "date": "Medieval",
             "note": "Very small Syriac fragments exist, quoted in chronicles. Limited value for "
                     "textual criticism but confirm wider awareness of the text."},
            {"name": "Greek (lost, but quoted)", "date": "2nd century BC - 5th century AD",
             "note": "The Greek translation is almost entirely lost but is quoted by several church "
                     "fathers (Epiphanius, Syncellus) and underlies both the Latin and Ethiopic versions. "
                     "Some Greek fragments survive in catena manuscripts."}
        ],
        "reliability": "The textual situation is better than one might expect. Where the Qumran "
                       "Hebrew fragments overlap with the Ethiopic version (via Greek intermediary), "
                       "the transmission is generally faithful — the Ethiopic translators preserved "
                       "the content accurately despite the double translation (Hebrew -> Greek -> "
                       "Ge'ez). The Latin fragments provide a useful third witness for the portions "
                       "they cover. The main uncertainty is in the sections where only the Ethiopic "
                       "survives without Hebrew or Latin corroboration."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "Jubilees retells history from creation to Sinai, but the text itself was "
                   "composed in the cauldron of the Maccabean crisis (~160-150 BC). Antiochus IV "
                   "Epiphanes had desecrated the Jerusalem Temple (167 BC), banned Torah observance, "
                   "and forced Hellenistic practices on the Jewish population. The Maccabean revolt "
                   "(167-164 BC) restored the Temple, but the cultural war continued — many Jews "
                   "were voluntarily adopting Greek customs, intermarrying with Gentiles, and "
                   "abandoning distinctive Jewish practices. Jubilees was written in this context "
                   "of existential threat to Jewish identity.",

        "geography": "The narrative follows the Genesis-Exodus geography: Eden, the land of Canaan "
                     "(the patriarchal journeys), Haran, Egypt, and Mount Sinai. The author's own "
                     "geographical context is Palestine — likely Judea, possibly Jerusalem or its "
                     "environs. The text shows detailed knowledge of Palestinian geography and of "
                     "the Jerusalem Temple establishment (even while critiquing its calendar). The "
                     "Qumran community that most enthusiastically preserved Jubilees lived at Khirbet "
                     "Qumran near the northwestern shore of the Dead Sea.",

        "historical_connections": "Jubilees connects to several major currents of Second Temple "
                                 "Judaism: (1) The calendar controversy — the 364-day solar calendar "
                                 "vs. the lunisolar calendar used at the Jerusalem Temple was one of "
                                 "the defining disputes of the period, and may have been a factor in "
                                 "the Qumran community's separation from mainstream Judaism. (2) The "
                                 "Enochic tradition — Jubilees knows and incorporates material from "
                                 "1 Enoch (especially the Watchers tradition), showing these texts "
                                 "circulated in overlapping communities. (3) The emergence of halakhah "
                                 "— Jubilees represents one of the earliest attempts to systematize "
                                 "Torah interpretation into detailed legal rulings, a process that would "
                                 "eventually produce the Mishnah and Talmud. (4) The Hasidim movement "
                                 "— the 'pious ones' who resisted Hellenization and may have been "
                                 "precursors to both the Pharisees and the Essenes."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "high",
        "summary": "Jubilees makes three major contributions to the divine council worldview that "
                   "Heiser traces through the biblical text:\n\n"
                   "(1) THE WATCHERS RETOLD (Jubilees 5): Jubilees retells the Watchers story from "
                   "1 Enoch / Genesis 6:1-4 with a critical addition — after God's judgment on the "
                   "Watchers and the Flood's destruction of the Nephilim, the spirits of the dead "
                   "giants (demons) continue to plague humanity. Noah prays for deliverance (Jubilees "
                   "10:1-6), and God commands that ALL the demons be bound. But Mastema, the prince "
                   "of the spirits, negotiates: he asks that one-tenth be left to him to test and "
                   "tempt humanity. God permits it. This is an extraordinary theological move — it "
                   "explains why evil persists after the Flood and provides an origin story for "
                   "ongoing demonic activity.\n\n"
                   "(2) MASTEMA AS SATAN FIGURE: Mastema (from the Hebrew root stm, 'to be hostile') "
                   "functions as the prince of evil spirits — a direct development of the Watchers "
                   "tradition into a systematic understanding of cosmic evil. He is behind the "
                   "testing of Abraham (Jubilees 17:16, paralleling the satan in Job 1-2), the "
                   "opposition during the Exodus (Jubilees 48:2-4, 9-12), and ongoing temptation "
                   "of humanity. This shows how Second Temple Judaism developed its understanding "
                   "of 'the satan' from a legal accuser (Job, Zechariah 3) into a prince of demons "
                   "— the framework that the New Testament inherits.\n\n"
                   "(3) ANGELIC GOVERNANCE: Jubilees 15:31-32 states that God appointed spirits "
                   "(angels) over all nations to lead them astray, but over Israel he appointed no "
                   "angel — God rules Israel directly. This is the Deuteronomy 32:8-9 worldview in "
                   "narrative form: the nations are allotted to lesser elohim, Israel belongs to "
                   "YHWH. This is a cornerstone of Heiser's 'Deuteronomy 32 worldview.'",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 12 (the Watchers and their aftermath)",
            "Reversing Hermon, chapter 3 (Jubilees and the persistence of evil after the Flood)",
            "Demons (2020), chapters on the origin of demons from Nephilim spirits — Jubilees 10 "
            "is a primary source for this tradition",
            "Supernatural, chapter 7 (the Deuteronomy 32 worldview — Jubilees 15:31-32 parallel)",
            "The Naked Bible Podcast, episodes on the divine council and territorial spirits"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "authority",
            "title": "Extremely Popular at Qumran — But Still Not Scripture",
            "body": "The sheer number of Jubilees manuscripts at Qumran (15+ copies) is striking — "
                    "it rivals Deuteronomy and Isaiah. The Damascus Document cites it by name as "
                    "authoritative. This tells us that at least one major Jewish community in the "
                    "time of Jesus treated Jubilees as something very close to scripture. But "
                    "popularity does not equal inspiration. The broader Jewish community did not "
                    "include Jubilees in the canon, and neither did the Christian church (outside "
                    "Ethiopia). Read it as a deeply valued Second Temple text that reveals how "
                    "devout Jews understood and applied the Torah — but do not elevate it to "
                    "canonical status."
        },
        {
            "type": "context",
            "title": "The Calendar War",
            "body": "One of Jubilees' central concerns is the 364-day solar calendar, which it "
                    "presents as the original calendar ordained by God at creation. This is not "
                    "a minor technical detail — it was a defining issue that likely contributed to "
                    "the Qumran community's break with the Jerusalem Temple. If the Temple was "
                    "celebrating Passover on the wrong day (by their reckoning), then the entire "
                    "sacrificial system was invalid. The canonical Torah ties its festivals to "
                    "lunar observation ('when you see the new moon'), which means the 364-day "
                    "solar calendar of Jubilees conflicts with the canonical system. Modern readers "
                    "should understand this as a heated intra-Jewish debate, not as settled "
                    "revelation about which calendar is correct."
        },
        {
            "type": "interpretation",
            "title": "Anti-Gentile Polemic — Handle with Care",
            "body": "Jubilees contains some of the harshest anti-Gentile rhetoric in Second Temple "
                    "literature. It demands absolute separation, condemns intermarriage in extreme "
                    "terms, and portrays the Gentile nations as inherently under demonic governance. "
                    "This must be understood in context: the author's community was facing forced "
                    "Hellenization and cultural extinction. The polemic is a survival response. But "
                    "it is in genuine tension with the canonical vision of God's plan for the nations "
                    "— from 'all families of the earth shall be blessed' (Genesis 12:3) to 'a light "
                    "for the nations' (Isaiah 49:6) to the Great Commission (Matthew 28:19). Paul "
                    "explicitly dismantled the Jew-Gentile wall in Ephesians 2:14. Jubilees' "
                    "separationism reflects one Second Temple perspective, not the fullness of "
                    "biblical revelation."
        },
        {
            "type": "warning",
            "title": "Rewritten Bible Is Still Rewritten",
            "body": "Jubilees' great strength is also its great danger for the reader: because it "
                    "retells Genesis so closely, it is easy to absorb its additions as if they were "
                    "part of the original. The patriarchs observing specific Torah laws, Abraham "
                    "fighting ravens as a boy, the detailed testaments of the patriarchs, the "
                    "Mastema negotiations — none of these are in Genesis. They are the author's "
                    "interpretive and creative additions. When studying Jubilees, always keep a copy "
                    "of Genesis open beside it so you can distinguish what the canonical text "
                    "actually says from what Jubilees adds."
        }
    ]
}
