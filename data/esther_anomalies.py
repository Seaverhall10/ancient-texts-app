"""
Esther Anomalies -- Why Esther is the Most Unusual Book of the Hebrew Bible.

Scholarly documentation of textual, canonical, and theological peculiarities.
The Book of Esther occupies a unique position in the biblical canon: it is the
only book of the Hebrew Bible absent from the Dead Sea Scrolls, one of only two
books that never explicitly names God, and the subject of more canonical dispute
than perhaps any other Old Testament book. Yet it remains one of the most beloved
texts in Judaism, read aloud every year at Purim.

This module documents the anomalies, the scholarly debates, and the theological
implications for the Ancient Texts Study App.
"""

ESTHER_ANOMALIES = {
    "title": "The Esther Enigma: Anomalies of a Canonical Outlier",
    "subtitle": "The Only Book Missing from Qumran, the Only Narrative Without God's Name",

    # ======================================================================
    # TIMELINE & BASIC DATA
    # ======================================================================
    "timeline": {
        "events": "~486-465 BCE (reign of Xerxes I / Ahasuerus); the narrative is set ~483-473 BCE",
        "composition": "~400-300 BCE (scholarly consensus for the Hebrew text); "
                       "some date it as late as the early 2nd century BCE",
        "greek_additions": "~2nd-1st century BCE (the six Greek additions were composed "
                          "at different times; the colophon of the LXX Esther dates the "
                          "Greek translation to ~114 BCE by Lysimachus of Jerusalem)",
        "note": "The events described fall in the Persian period, but the composition "
                "is centuries later. The author shows detailed knowledge of Persian "
                "court customs, palace architecture (confirmed by excavations at Susa), "
                "and administrative vocabulary -- suggesting access to genuine Persian-era "
                "sources or traditions, even if the final literary form is later."
    },

    # ======================================================================
    # CANONICAL STATUS ACROSS TRADITIONS
    # ======================================================================
    "canonical_status": {
        "jewish": {
            "status": "Canonical -- Ketuvim (Writings)",
            "detail": "Esther is one of the five Megillot (scrolls) and is read aloud "
                      "in its entirety at the festival of Purim (Adar 14-15). It is the "
                      "last of the Megillot in most arrangements. The Talmud (Megillah 7a) "
                      "records the tradition that Esther was composed 'with the Holy Spirit' "
                      "(be-ruach ha-qodesh). Despite its canonical status, the Talmud also "
                      "preserves debates about whether Esther 'defiles the hands' (i.e., is "
                      "sacred scripture) -- see Megillah 7a and Sanhedrin 100a."
        },
        "protestant": {
            "status": "Canonical (Old Testament)",
            "detail": "Included in the Protestant Old Testament as a historical book. "
                      "However, Esther has faced more skepticism from Protestant scholars "
                      "and reformers than almost any other OT book. Luther's objections "
                      "are the most famous (see canonical_disputes section)."
        },
        "catholic": {
            "status": "Canonical, with Greek Additions as deuterocanonical",
            "detail": "The Council of Trent (1546) affirmed both the Hebrew text and the "
                      "Greek Additions as canonical. Catholic Bibles include the six "
                      "additional sections (107 verses) interspersed within the narrative. "
                      "The Additions are designated deuterocanonical -- 'secondary canon' -- "
                      "meaning they are authoritative but acknowledged as later compositions."
        },
        "orthodox": {
            "status": "Canonical, with Greek Additions",
            "detail": "Eastern Orthodox churches accept Esther with the Greek Additions, "
                      "though the precise canonical weight of the Additions varies by "
                      "national church. The Greek Orthodox, Russian Orthodox, and other "
                      "Eastern traditions generally follow the Septuagint text."
        },
        "ethiopian": {
            "status": "Canonical",
            "detail": "The Ethiopian Orthodox Tewahedo Church includes Esther in its "
                      "broader canon of 81 books, using a Ge'ez translation."
        },
        "qumran": {
            "status": "ABSENT -- the only Old Testament book not found",
            "detail": "No fragment, no quotation, no allusion to Esther has been "
                      "identified among the approximately 900+ manuscripts recovered "
                      "from the 11 caves at Qumran. Every other book of the Hebrew "
                      "Bible is represented (some, like Psalms, Isaiah, and Deuteronomy, "
                      "in dozens of copies). This absence is the single most discussed "
                      "anomaly of the Dead Sea Scrolls corpus. See the dss_absence "
                      "section for full analysis."
        },
        "luther": {
            "status": "Wished it did not exist",
            "detail": "Martin Luther, Table Talk: 'I am so great an enemy to the second "
                      "book of the Maccabees, and to Esther, that I wish they had not "
                      "come to us at all, for they have too many heathen unnaturalities.' "
                      "He also called Esther 'less worthy of being held canonical' than "
                      "any other writing of the Old Testament. Luther's objection was "
                      "primarily theological: the book's nationalism, the absence of God, "
                      "and what he perceived as 'Judaizing' tendencies."
        }
    },

    # ======================================================================
    # MAIN SECTIONS -- DETAILED SCHOLARLY DOCUMENTATION
    # ======================================================================
    "sections": [
        # ------------------------------------------------------------------
        # 1. DEAD SEA SCROLLS ABSENCE
        # ------------------------------------------------------------------
        {
            "id": "dss_absence",
            "title": "Absent from the Dead Sea Scrolls",
            "content": (
                "Of the approximately 900+ manuscripts found in the 11 caves at Qumran "
                "(discovered 1947-1956), fragments of every book of the Hebrew Bible have "
                "been identified -- except Esther. This is not a minor statistical gap. "
                "Some biblical books are represented by 30+ copies (Psalms: 36 copies, "
                "Deuteronomy: 33, Isaiah: 22). Even small books like Obadiah and Nahum "
                "have fragments. Esther alone is completely absent.\n\n"
                "Moreover, Esther is not merely unpreserved -- it appears to be deliberately "
                "excluded. No other Qumran text quotes, alludes to, or references Esther. "
                "By contrast, non-canonical texts like 1 Enoch, Jubilees, and Tobit were "
                "preserved in multiple copies, demonstrating that the community valued texts "
                "beyond the strict Hebrew canon.\n\n"
                "HOWEVER: A nuance must be noted. The text 4Q550 (proto-Esther) is an Aramaic "
                "narrative set in the Persian court with plot elements reminiscent of Esther "
                "(a Jewish hero in a foreign court, court intrigue, danger and deliverance). "
                "Some scholars (notably J.T. Milik) have called this a 'proto-Esther' tradition. "
                "It is NOT the Book of Esther, but it suggests the community was familiar with "
                "the literary tradition behind it. Additionally, the phrase from Esther 3:7 "
                "appears echoed in 4Q267 (a Damascus Document copy), suggesting at least one "
                "scribe was acquainted with Esther's text even if the community did not preserve "
                "or venerate it.\n\n"
                "The absence remains the most significant textual anomaly in the Dead Sea "
                "Scrolls corpus."
            ),
            "theories": [
                {
                    "theory": "No mention of God",
                    "detail": "Esther never names YHWH, Elohim, El, Adonai, or any divine title. "
                              "For a community as theologically rigorous as the Yahad -- whose own "
                              "compositions (Community Rule, Hodayot, War Scroll) are saturated with "
                              "divine names and theological language -- a book that never mentions God "
                              "may have been viewed as theologically deficient or even secular.",
                    "strength": "Strong"
                },
                {
                    "theory": "No mention of prayer, Torah, Temple, or covenant",
                    "detail": "Esther contains no prayer (Esther 4:16 describes fasting but not "
                              "prayer explicitly), no reference to Torah or the commandments, no "
                              "mention of the Temple or Jerusalem, and no invocation of the covenant. "
                              "The Qumran community organized their entire existence around Torah "
                              "observance, prayer, and covenant renewal (see 1QS I-III). A book "
                              "lacking all of these would have seemed anomalous at best.",
                    "strength": "Strong"
                },
                {
                    "theory": "Purim rejected by the Qumran calendar",
                    "detail": "The Qumran community followed a strict 364-day solar calendar "
                              "(shared with Jubilees and 1 Enoch's Astronomical Book). Purim, the "
                              "festival instituted by Esther (9:20-32), is absent from every Qumran "
                              "calendar text. Since Purim is the entire raison d'etre of the book -- "
                              "Esther exists to explain and authorize Purim -- a community that rejected "
                              "the festival would have little use for the book that authorized it. "
                              "Notably, Purim is the only major Jewish festival not rooted in the Torah "
                              "(Pentateuch), which may have further delegitimized it for the Yahad.",
                    "strength": "Strong"
                },
                {
                    "theory": "Intermarriage with a Gentile king",
                    "detail": "Esther, a Jewish woman, marries the Persian king Ahasuerus (Xerxes I) -- "
                              "a Gentile. The Qumran community was intensely opposed to intermarriage "
                              "and contact with Gentiles. The Damascus Document and Temple Scroll both "
                              "contain strict prohibitions against foreign marriage. A narrative that "
                              "celebrates a Jewess becoming the queen of Persia through marriage to a "
                              "pagan king would have been deeply offensive to Essene sensibilities.",
                    "strength": "Moderate"
                },
                {
                    "theory": "Accidental non-preservation",
                    "detail": "The minimalist explanation: Esther is a short book (10 chapters). "
                              "Perhaps a copy existed at Qumran but simply was not preserved in the "
                              "caves, was destroyed by time, or has not yet been identified among "
                              "unclassified fragments. Absence of evidence is not necessarily evidence "
                              "of absence. However, this argument weakens when one considers that far "
                              "shorter books (Obadiah: 1 chapter, 21 verses) ARE represented, and "
                              "that no other Qumran text even quotes Esther.",
                    "strength": "Weak but not impossible"
                },
                {
                    "theory": "Secular/nationalistic tone",
                    "detail": "Esther is arguably the most 'secular' book in the Hebrew Bible. Its "
                              "concerns are political survival, court intrigue, ethnic identity, and "
                              "festive celebration. The Essenes, who withdrew from society to prepare "
                              "for the eschatological war between the Sons of Light and Sons of "
                              "Darkness, may have found Esther's this-worldly nationalism theologically "
                              "trivial or misguided.",
                    "strength": "Moderate"
                }
            ],
            "evidence_level": "A",
            "sources": [
                "Sidnie White Crawford, 'Has Esther Been Found at Qumran? 4QProto-Esther and the Esther Corpus,' Revue de Qumran 17 (1996): 307-325",
                "Martin Abegg Jr., Peter Flint, Eugene Ulrich, The Dead Sea Scrolls Bible (HarperOne, 1999)",
                "BYU Studies Quarterly, 'Why Is Esther Missing from the Qumran Scrolls?'",
                "Michael Kruger, 'The Dead Sea Scrolls, the Book of Esther, and the Argument from Silence'",
                "Emanuel Tov, Textual Criticism of the Hebrew Bible, 3rd ed. (Fortress, 2012)"
            ]
        },

        # ------------------------------------------------------------------
        # 2. ABSENCE OF GOD'S NAME
        # ------------------------------------------------------------------
        {
            "id": "divine_name_absence",
            "title": "The Book That Never Names God",
            "content": (
                "Esther is one of only two narrative books in the Hebrew Bible that never "
                "explicitly mentions God by any name or title. (Song of Songs is the other, "
                "though Song of Songs 8:6 contains the abbreviated form YAH in 'shalhebet-yah,' "
                "which some read as 'flame of the LORD' -- making Esther arguably the ONLY "
                "book with zero divine reference of any kind.)\n\n"
                "The absence is comprehensive:\n"
                "- No YHWH (the covenant name, used ~6,800 times in the OT)\n"
                "- No Elohim (generic 'God,' used ~2,600 times)\n"
                "- No El, Eloah, El Shaddai, El Elyon\n"
                "- No Adonai ('Lord')\n"
                "- No reference to prayer (fasting in 4:16, but no prayer)\n"
                "- No reference to Torah, commandments, or covenant\n"
                "- No reference to the Temple, Jerusalem, or the promised land\n"
                "- No reference to angels, prophets, or divine revelation\n"
                "- No reference to the patriarchs, Moses, or salvation history\n\n"
                "This silence is so total and so systematic that most scholars believe it is "
                "DELIBERATE -- not an oversight but a literary and theological strategy. The "
                "author appears to have consciously crafted a narrative in which God's activity "
                "is everywhere implied but nowhere stated. The 'coincidences' that drive the "
                "plot (Esther's elevation, Mordecai's discovery of the assassination plot, the "
                "king's insomnia at the critical moment, the reversal of Haman's gallows) are "
                "too perfectly orchestrated to be accidental -- yet the text never attributes "
                "them to divine action.\n\n"
                "This is the literary technique of the Deus absconditus -- the 'hidden God' "
                "(cf. Isaiah 45:15, 'Truly you are a God who hides himself'). The reader is "
                "invited to perceive providence where the characters cannot name it.\n\n"
                "Ecclesiastes is sometimes added to this list, but Ecclesiastes does mention "
                "'Elohim' (God) approximately 40 times. It lacks YHWH but not God. Esther "
                "alone among narrative books achieves total divine silence."
            ),
            "evidence_level": "A",
            "sources": [
                "Jon Levenson, Esther: A Commentary, Old Testament Library (Westminster John Knox, 1997)",
                "Michael V. Fox, Character and Ideology in the Book of Esther, 2nd ed. (Eerdmans, 2001)",
                "Chloe T. Sun, Conspicuous in His Absence: Studies in the Song of Songs and Esther (IVP Academic, 2021)",
                "Frederic Bush, Ruth, Esther, Word Biblical Commentary (Zondervan, 1996)"
            ]
        },

        # ------------------------------------------------------------------
        # 3. HIDDEN YHWH ACROSTICS
        # ------------------------------------------------------------------
        {
            "id": "hidden_acrostics",
            "title": "The Hidden Name: YHWH Acrostics in the Hebrew Text",
            "content": (
                "Despite -- or perhaps because of -- the absence of God's name on the surface, "
                "a remarkable phenomenon exists in the Hebrew text: the divine name YHWH appears "
                "to be encoded as acrostics in four passages, and the divine name EHYH ('I AM') "
                "in a fifth. In each case, the initial or final letters of four consecutive "
                "Hebrew words spell out the Tetragrammaton.\n\n"
                "This phenomenon was first documented by E.W. Bullinger in The Companion Bible "
                "(Appendix 60) and has been discussed by scholars ever since. At least three "
                "ancient Hebrew manuscripts are known in which the acrostic letters are written "
                "MAJUSCULAR -- that is, larger than the surrounding letters -- so that they "
                "stand out visibly. This scribal tradition suggests the acrostics were recognized "
                "and intentionally highlighted in antiquity, not merely discovered by modern "
                "readers looking for patterns.\n\n"
                "SCHOLARLY CAUTION: Not all scholars accept these acrostics as intentional. "
                "The paper 'Desperately Seeking YHWH: Finding God in Esther's Acrostics' "
                "(by Yoram Hazony and others) argues that statistical analysis of Hebrew text "
                "makes four-letter acrostics likely to occur by chance. The counter-argument "
                "is that (a) all four occur at dramatically significant moments in the narrative, "
                "(b) two are spoken by Jews and two by Gentiles, (c) two read forward and two "
                "backward, (d) two use initial letters and two use final letters -- a symmetrical "
                "pattern that chance alone cannot easily explain, and (e) the majuscular scribal "
                "tradition demonstrates ancient recognition.\n\n"
                "The structural pattern:\n"
                "- When a Jew speaks (Esther in 5:4, the narrator in 7:7): YHWH reads FORWARD\n"
                "- When a Gentile speaks or is quoted (Memucan in 1:20, Haman in 5:13): YHWH reads BACKWARD\n"
                "- The forward readings suggest God acting; the backward suggest God overruling\n"
                "- Initial letters = God initiating; Final letters = God completing/finishing\n\n"
                "Whether intentional or not, the acrostics have become an important part of "
                "the book's interpretive tradition and powerfully reinforce the theme of divine "
                "hiddenness -- God's name concealed within the text just as God's hand is "
                "concealed within the events."
            ),
            "evidence_level": "B",
            "evidence_note": "The acrostics themselves are objectively present in the Hebrew text. "
                            "Whether they are intentional authorial devices or coincidental is debated. "
                            "The majuscular scribal tradition favors intentionality.",
            "sources": [
                "E.W. Bullinger, The Companion Bible, Appendix 60: 'The Name of Jehovah in the Book of Esther'",
                "Chuck Missler, 'The Book of Esther,' Koinonia House (1997)",
                "Yoram Hazony, 'Desperately Seeking YHWH: Finding God in Esther's Acrostics'",
                "A. Boyd Luter and Barry C. Davis, 'Literary Analysis of Esther,' Bibliotheca Sacra 149 (1992)"
            ]
        },

        # ------------------------------------------------------------------
        # 4. GREEK ADDITIONS
        # ------------------------------------------------------------------
        {
            "id": "greek_additions",
            "title": "The Greek Additions: 107 Verses That 'Fix' the Problem",
            "content": (
                "The Septuagint (LXX) version of Esther contains 107 additional verses "
                "organized into six sections (designated Addition A through F) that are not "
                "found in the Hebrew Masoretic text. These additions transform the character "
                "of the book: whereas the Hebrew Esther never mentions God, the Greek Additions "
                "mention God over 50 times. Whereas the Hebrew has no prayers, the Greek adds "
                "two lengthy, theologically rich prayers (by Mordecai and Esther). Whereas the "
                "Hebrew offers no explanation for its theological silence, the Greek additions "
                "fill the void with explicit piety, apocalyptic dreams, and divine intervention.\n\n"
                "The theological intent is transparent: the Additions were composed to remedy "
                "the perceived deficiency of a sacred book that never mentions God. They retrofit "
                "conventional religious language onto a narrative that originally and deliberately "
                "lacked it. This makes them one of the clearest examples of 'theological editing' "
                "in the history of the biblical text.\n\n"
                "Jerome, when producing the Vulgate (late 4th century), recognized the Additions "
                "as non-original. He translated the Hebrew text for the body of Esther and moved "
                "all six Greek Additions to the end of the book (chapters 10:4-16:24 in the Vulgate), "
                "adding notes indicating they were not in the Hebrew. The Council of Trent (1546) "
                "nevertheless affirmed them as deuterocanonical.\n\n"
                "DATING AND AUTHORSHIP: The Additions were not all composed at the same time or "
                "by the same author. Additions A, C, D, and F show traces of a Semitic (Hebrew or "
                "Aramaic) original and may predate the Greek translation. Additions B and E (the "
                "royal letters) are composed in ornate Greek rhetorical style and were clearly "
                "written in Greek. The colophon at the end of Greek Esther states that the book "
                "was translated by 'Lysimachus son of Ptolemy, one of the residents of Jerusalem' "
                "and brought to Egypt in 'the fourth year of the reign of Ptolemy and Cleopatra' -- "
                "most likely 114 BCE (Ptolemy VIII) or 78/77 BCE (Ptolemy XII)."
            ),
            "evidence_level": "A",
            "sources": [
                "Carey Moore, Daniel, Esther, and Jeremiah: The Additions, Anchor Bible 44 (Doubleday, 1977)",
                "Karen Jobes, The Alpha-Text of Esther (SBL Dissertation Series, 1996)",
                "Kristin De Troyer, The End of the Alpha Text of Esther (SBL Septuagint and Cognate Studies, 2000)",
                "NRSV with Apocrypha, editorial notes on Additions to Esther"
            ]
        },

        # ------------------------------------------------------------------
        # 5. CANONICAL DISPUTES
        # ------------------------------------------------------------------
        {
            "id": "canonical_disputes",
            "title": "Two Millennia of Canonical Uncertainty",
            "content": (
                "No other book of the Hebrew Bible has provoked as much canonical debate as Esther. "
                "The disputes span Jewish, Christian, and modern scholarly traditions:\n\n"
                "JEWISH DEBATES:\n"
                "The Babylonian Talmud (Megillah 7a) records that 'Esther was composed with the "
                "Holy Spirit,' but the same tractate preserves the dissenting opinion of Rabbi "
                "Samuel that 'Esther does not defile the hands' -- the technical rabbinic term for "
                "a text that is NOT considered sacred scripture. The resolution was acceptance, "
                "but the very existence of the debate is telling. The Talmud also records that "
                "Esther sent a message to the Sages asking them to 'write me for the generations' "
                "(i.e., include me in the canon), and the Sages initially resisted (Megillah 7a).\n\n"
                "EARLY CHURCH DEBATES:\n"
                "Several major Church Fathers questioned or excluded Esther:\n"
                "- Athanasius of Alexandria (367 CE) listed Esther among the 'books not included "
                "  in the canon but approved for reading' in his 39th Festal Letter -- effectively "
                "  making it deuterocanonical, not fully canonical.\n"
                "- Gregory of Nazianzus (4th century) omitted Esther from his canonical list entirely.\n"
                "- Theodore of Mopsuestia (4th-5th century) excluded Esther from his canon.\n"
                "- Melito of Sardis (2nd century) compiled the earliest known Christian OT canonical "
                "  list (c. 170 CE) and did NOT include Esther.\n"
                "- Amphilochius of Iconium (4th century) noted that 'some say Esther should also "
                "  be added' to the canon -- implying it was not universally accepted.\n\n"
                "REFORMATION DEBATES:\n"
                "Martin Luther's hostility is the most famous: 'I am so great an enemy to the "
                "second book of the Maccabees, and to Esther, that I wish they had not come to "
                "us at all, for they have too many heathen unnaturalities' (Table Talk). He also "
                "wrote in De Servo Arbitrio (On the Bondage of the Will, 1525): 'I so much hate "
                "the book that I wish it did not exist at all, for it Judaizes too much and has "
                "much pagan naughtiness.' Luther's objection combined theological concerns (no "
                "mention of God) with anti-Jewish sentiment (the nationalistic celebration of "
                "Jewish triumph over Gentile enemies).\n\n"
                "MODERN SCHOLARLY ASSESSMENT:\n"
                "The consensus is that Esther's canonicity, while historically contested, is now "
                "firmly established in all major traditions (Jewish, Protestant, Catholic, Orthodox). "
                "However, the REASONS for its contested history illuminate important questions about "
                "what makes a text 'scripture' -- and whether the absence of explicit God-language "
                "disqualifies a text from divine authority."
            ),
            "evidence_level": "A",
            "sources": [
                "Babylonian Talmud, Megillah 7a-7b (canonical debate)",
                "Athanasius, 39th Festal Letter (367 CE)",
                "Melito of Sardis, Canonical List, preserved in Eusebius, Ecclesiastical History IV.26",
                "Martin Luther, Table Talk (Tischreden); De Servo Arbitrio (1525)",
                "Roger Beckwith, The Old Testament Canon of the New Testament Church (Eerdmans, 1985)",
                "Lee McDonald, The Biblical Canon: Its Origin, Transmission, and Authority (Hendrickson, 2007)"
            ]
        },

        # ------------------------------------------------------------------
        # 6. HISTORICAL QUESTIONS
        # ------------------------------------------------------------------
        {
            "id": "historical_questions",
            "title": "Historical Questions: Where Are Esther and Vashti in Persian Records?",
            "content": (
                "The historical setting of Esther is specific and verifiable in its broad strokes: "
                "Ahasuerus is almost universally identified with Xerxes I of Persia (486-465 BCE). "
                "The description of the palace at Susa (Shushan) matches archaeological findings "
                "remarkably well -- the 'court of the garden of the king's palace' (1:5), the "
                "'white and blue hangings' (1:6), and the general layout all correspond to the "
                "excavated remains of the Apadana at Susa. The Persian court customs, administrative "
                "terminology, and the structure of the postal system (8:10) all ring true.\n\n"
                "However, the central characters present problems:\n\n"
                "VASHTI: Greek historians (Herodotus, Histories VII.61, IX.108-113) identify "
                "Xerxes' queen as Amestris, daughter of Otanes. No 'Vashti' appears in any "
                "Persian or Greek record. Some scholars have attempted to identify Vashti with "
                "Amestris on linguistic grounds (the identification is phonetically plausible "
                "but not proven). Others suggest Vashti was a secondary wife or concubine not "
                "recorded in Greek sources.\n\n"
                "ESTHER: No Persian record mentions a Jewish queen. Herodotus indicates that "
                "Persian kings were required to marry within seven noble Persian families "
                "(Histories III.84) -- a Jewish wife would violate this custom. Some scholars "
                "have tried to identify Esther with Amestris (the phonetic similarity of "
                "'Esther' and 'Amestris' is noted), but the character profiles are very different: "
                "Amestris was notoriously cruel (Herodotus IX.112), while Esther is portrayed "
                "as courageous but compassionate.\n\n"
                "MORDECAI: The name is almost certainly derived from 'Marduk,' the chief god of "
                "Babylon (Akkadian: Marduku). The Babylonian form 'Mardukaya' appears in Persian-era "
                "administrative tablets from Persepolis and Borsippa, confirming that Jews in the "
                "Persian Empire did bear Babylonian theophoric names. An administrative text from "
                "the reign of Darius I or early Xerxes mentions a 'Marduka' who was a finance "
                "officer in Susa -- some scholars (Ungnad, 1940-43) have proposed this is the "
                "historical Mordecai, though the identification is speculative.\n\n"
                "ESTHER'S NAME: Hebrew 'Hadassah' (her Jewish name, 2:7) means 'myrtle.' "
                "'Esther' almost certainly derives from 'Ishtar,' the Mesopotamian goddess of "
                "love and war (Akkadian: Istar, also Astarte in Canaanite tradition). That both "
                "protagonists bear names derived from major Babylonian deities (Marduk and Ishtar) "
                "has led some scholars (notably Peter Jensen, 1892, and others) to propose that "
                "the Esther narrative is a historicized version of a Babylonian myth. This theory "
                "has been largely abandoned by modern scholarship as overly reductionist, but the "
                "onomastic connections remain significant.\n\n"
                "BOTTOM LINE: The historical setting is authentic; the central characters cannot "
                "be confirmed from external sources. This places Esther in the category of "
                "historical romance or novelistic history -- a genre common in the ancient Near "
                "East. The lack of external confirmation does not disprove historicity (absence "
                "of evidence is not evidence of absence), but it does mean the narrative cannot "
                "be independently verified."
            ),
            "evidence_level": "B",
            "evidence_note": "The setting is archaeologically confirmed (A-level); the characters "
                            "lack external confirmation (B-level). The Babylonian name etymologies "
                            "are well-established linguistically.",
            "sources": [
                "Herodotus, Histories III.84, VII.61, IX.108-113",
                "A. Ungnad, 'Keilinschriftliche Beitrage zum Buch Ezra und Esther,' ZAW 58-59 (1940-43): 240-244",
                "Edwin Yamauchi, Persia and the Bible (Baker Academic, 1990)",
                "Pierre Briant, From Cyrus to Alexander: A History of the Persian Empire (Eisenbrauns, 2002)",
                "Jon Levenson, Esther: A Commentary, Old Testament Library (Westminster John Knox, 1997)",
                "Bezalel Porten, 'Esther,' in The Anchor Bible Dictionary (Doubleday, 1992)"
            ]
        },

        # ------------------------------------------------------------------
        # 7. THEOLOGICAL IMPLICATIONS
        # ------------------------------------------------------------------
        {
            "id": "theological_implications",
            "title": "The Hidden God: Theology of Divine Absence",
            "content": (
                "The greatest anomaly of Esther is also its greatest theological contribution: "
                "it is a sustained meditation on how God works when God appears absent. This is "
                "the theology of the Deus absconditus -- the 'hidden God' of Isaiah 45:15 "
                "('Truly you are a God who hides himself, O God of Israel, the Savior').\n\n"
                "THE CASE FOR INTENTIONAL SILENCE:\n"
                "The author of Esther is not theologically naive. The silence is not accidental. "
                "Consider: the author describes a three-day fast (4:16) without mentioning prayer "
                "-- but every Jewish reader would know that fasting without prayer is meaningless. "
                "The author describes Mordecai's confidence that 'relief and deliverance will arise "
                "for the Jews from another place' (4:14) without identifying that 'other place' -- "
                "but every Jewish reader would hear 'from God.' The author records the king's "
                "insomnia at the precise moment when reading the chronicles would save Mordecai's "
                "life (6:1) -- but attributes it to nothing. The silence is not absence; it is "
                "eloquent restraint.\n\n"
                "THE 'OTHER PLACE' (MAKOM AHER):\n"
                "Mordecai's statement in 4:14 is the theological hinge of the entire book: "
                "'For if you remain silent at this time, relief and deliverance will arise for "
                "the Jews from another place (makom aher), but you and your father's house will "
                "perish.' The Hebrew 'makom' (place) is used in rabbinic literature as a name "
                "for God (HaMakom -- 'The Place,' i.e., the Omnipresent One). Whether the author "
                "intended this double meaning is debated, but the rabbinic tradition heard it "
                "clearly.\n\n"
                "PROVIDENCE THROUGH COINCIDENCE:\n"
                "The narrative is structured as a chain of 'coincidences' that are too precise "
                "to be random:\n"
                "- Esther happens to be chosen as queen (2:17)\n"
                "- Mordecai happens to overhear the assassination plot (2:21-23)\n"
                "- Haman happens to cast lots (purim) that delay the genocide by 11 months (3:7)\n"
                "- The king happens to have insomnia on the critical night (6:1)\n"
                "- The king happens to read the specific passage about Mordecai's loyalty (6:1-2)\n"
                "- Haman happens to enter the court at the exact wrong moment (6:4)\n"
                "- Haman falls on Esther's couch at the exact worst moment (7:8)\n"
                "- The gallows Haman built for Mordecai happen to be available for Haman (7:9-10)\n\n"
                "Each event is described in purely human terms. Together, they form an unmistakable "
                "pattern of divine orchestration. The theology is: God is not absent from history -- "
                "He is present precisely in the events we call 'coincidence.'\n\n"
                "CONNECTION TO THE APP'S BROADER THEMES:\n"
                "Esther demonstrates a mode of divine action that complements the more explicit "
                "interventions documented elsewhere in this app. In Genesis, God speaks directly. "
                "In Exodus, God acts with signs and wonders. In the prophets, God sends messengers. "
                "In Esther, God works through the ordinary mechanics of human decision, political "
                "maneuvering, and apparent chance. This is not a lesser mode of divine action -- it "
                "is the mode most people experience in their own lives. Esther validates the "
                "experience of the faithful who see no miracles but trust that God is at work.\n\n"
                "The Talmud captures this beautifully: 'Where is Esther indicated in the Torah? "
                "In the verse: And I will surely hide (haster astir) My face' (Deuteronomy 31:18). "
                "The wordplay on 'Esther' and 'haster' (to hide) makes the entire book a literary "
                "embodiment of the hidden face of God (hester panim)."
            ),
            "evidence_level": "B",
            "evidence_note": "The theological interpretation is widely shared among Jewish and "
                            "Christian scholars but is by nature interpretive, not factual. "
                            "The literary observations about coincidence-structure are objective.",
            "sources": [
                "Jon Levenson, Esther: A Commentary (Westminster John Knox, 1997), esp. Introduction",
                "Michael V. Fox, Character and Ideology in the Book of Esther (Eerdmans, 2001)",
                "Babylonian Talmud, Chullin 139b ('Where is Esther indicated in the Torah?')",
                "Abraham Joshua Heschel, God in Search of Man (Farrar, Straus and Giroux, 1955)",
                "Adele Berlin, JPS Bible Commentary: Esther (Jewish Publication Society, 2001)",
                "Sandra Berg, The Book of Esther: Motifs, Themes, and Structure (Scholars Press, 1979)"
            ]
        },

        # ------------------------------------------------------------------
        # 8. COMPARISON WITH SONG OF SONGS
        # ------------------------------------------------------------------
        {
            "id": "comparison_song_of_songs",
            "title": "Esther and Song of Songs: The Two Books Without God",
            "content": (
                "Esther and Song of Songs are often paired as the two biblical books that "
                "omit God's name. But the comparison reveals important differences:\n\n"
                "SONG OF SONGS:\n"
                "- Genre: Love poetry\n"
                "- God reference: Arguably contains 'YAH' in 8:6 (shalhebet-yah, 'flame of YAH')\n"
                "- Traditional reading: Allegory of God's love for Israel (Jewish) or Christ's "
                "  love for the Church (Christian)\n"
                "- Canonical challenge: Rabbi Akiva's defense -- 'The whole world is not worth "
                "  the day Song of Songs was given to Israel' (Mishnah Yadayim 3:5)\n"
                "- DSS status: FOUND at Qumran (4Q106-107, 6Q6)\n\n"
                "ESTHER:\n"
                "- Genre: Historical narrative / court tale\n"
                "- God reference: Zero (even the possible YAH in Song of Songs is absent)\n"
                "- Traditional reading: Providence of the hidden God\n"
                "- Canonical challenge: Multiple disputes (see canonical_disputes section)\n"
                "- DSS status: NOT FOUND at Qumran -- the only absence\n\n"
                "The contrast is revealing: Song of Songs, despite its erotic content and lack "
                "of overt theology, was preserved at Qumran and fiercely defended by the rabbis. "
                "Esther, despite its nationalistic narrative about Jewish survival, was not preserved "
                "at Qumran and has faced persistent canonical challenges. The difference may come "
                "down to allegorical potential: Song of Songs CAN be read as divine love; Esther "
                "resists allegorization. Its meaning is stubbornly historical and political, which "
                "makes it theologically uncomfortable for communities that prioritize the spiritual "
                "over the political.\n\n"
                "Chloe T. Sun's monograph 'Conspicuous in His Absence' (2021) argues that both "
                "books, despite their theological silence, are 'resistance literature' -- texts "
                "that insist God is present even when conventional God-language fails. Song of Songs "
                "resists the reduction of divine love to mere theology; Esther resists the reduction "
                "of divine action to mere miracle."
            ),
            "evidence_level": "B",
            "sources": [
                "Chloe T. Sun, Conspicuous in His Absence (IVP Academic, 2021)",
                "Mishnah Yadayim 3:5 (Rabbi Akiva on Song of Songs)",
                "Roland Murphy, The Song of Songs, Hermeneia (Fortress, 1990)",
                "Jon Levenson, Esther (Westminster John Knox, 1997)"
            ]
        }
    ],

    # ======================================================================
    # HIDDEN YHWH ACROSTICS -- DETAILED DATA
    # ======================================================================
    "hidden_yhwh_acrostics": [
        {
            "reference": "Esther 1:20",
            "verse_context": "Memucan (a Gentile advisor) counsels King Ahasuerus about Vashti's disobedience",
            "english": "...all the wives will give honor to their husbands...",
            "hebrew_phrase": "\u05d4\u05d9\u05d0 \u05d5\u05db\u05dc-\u05d4\u05e0\u05e9\u05c1\u05d9\u05dd \u05d9\u05ea\u05e0\u05d5",
            "transliteration": "Hi' Vekhol-haNashim Yittenu",
            "acrostic_letters": "\u05d4 \u05d5 \u05d4 \u05d9",
            "acrostic_type": "Initial letters, read RIGHT to LEFT (backward = HVHY)",
            "direction": "backward",
            "letter_position": "initial",
            "speaker": "Memucan (Gentile)",
            "theological_significance": (
                "A Gentile advisor unknowingly speaks words that encode God's name in reverse. "
                "The backward reading symbolizes God OVERRULING the counsel of the nations. "
                "The very decree that removes Vashti opens the path for Esther's elevation -- "
                "the Gentiles' own counsel becomes the instrument of divine providence."
            )
        },
        {
            "reference": "Esther 5:4",
            "verse_context": "Esther (a Jew) invites the king and Haman to a banquet",
            "english": "...let the king and Haman come today...",
            "hebrew_phrase": "\u05d9\u05d1\u05d5\u05d0 \u05d4\u05de\u05dc\u05da \u05d5\u05d4\u05de\u05df \u05d4\u05d9\u05d5\u05dd",
            "transliteration": "Yavo' HaMelekh VeHaman HaYom",
            "acrostic_letters": "\u05d9 \u05d4 \u05d5 \u05d4",
            "acrostic_type": "Initial letters, read LEFT to RIGHT (forward = YHVH)",
            "direction": "forward",
            "letter_position": "initial",
            "speaker": "Esther (Jew)",
            "theological_significance": (
                "Esther, a Jew, speaks -- and God's name reads forward, in its natural order. "
                "When God's people act in faith, God moves FORWARD with them. Esther's "
                "invitation is the beginning of the reversal that will save her people. "
                "The YHWH spelled by initial letters suggests God INITIATING the action."
            )
        },
        {
            "reference": "Esther 5:13",
            "verse_context": "Haman (a Gentile enemy) complains that Mordecai's defiance ruins his joy",
            "english": "...yet all this avails me nothing...",
            "hebrew_phrase": "\u05d6\u05d4 \u05d0\u05d9\u05e0\u05e0\u05d5 \u05e9\u05c1\u05d5\u05d4 \u05dc\u05d9",
            "transliteration": "ZeH 'EinennU ShoveH LI",
            "acrostic_letters": "\u05d4 \u05d5 \u05d4 \u05d9",
            "acrostic_type": "Final letters, read RIGHT to LEFT (backward = HVHY)",
            "direction": "backward",
            "letter_position": "final",
            "speaker": "Haman (Gentile enemy)",
            "theological_significance": (
                "Haman, the enemy of God's people, speaks words whose final letters encode "
                "YHWH in reverse. The backward reading of final letters doubly emphasizes "
                "REVERSAL and COMPLETION: God is overruling Haman's evil designs AND bringing "
                "them to their end. Haman's very complaint -- 'all this avails me nothing' -- "
                "unknowingly prophesies his own downfall. The hidden Name declares that Haman's "
                "satisfaction will indeed amount to nothing."
            )
        },
        {
            "reference": "Esther 7:7",
            "verse_context": "The narrator describes Haman's realization that his doom is sealed",
            "english": "...that evil was determined against him by the king...",
            "hebrew_phrase": "\u05db\u05d9-\u05db\u05dc\u05ea\u05d4 \u05d0\u05dc\u05d9\u05d5 \u05d4\u05e8\u05e2\u05d4",
            "transliteration": "Ki-khaletaH 'ElayV HaRa'aH",
            "acrostic_letters": "\u05d9 \u05d4 \u05d5 \u05d4",
            "acrostic_type": "Final letters, read LEFT to RIGHT (forward = YHVH)",
            "direction": "forward",
            "letter_position": "final",
            "speaker": "Narrator (describing divine judgment)",
            "theological_significance": (
                "At the climactic moment of judgment, the narrator's words encode YHWH forward "
                "in their final letters. Forward reading + final letters = God bringing His plan "
                "to COMPLETION in its natural, sovereign order. The evil determined against Haman "
                "is not mere royal anger -- it is divine justice. The Name hidden in the end-letters "
                "declares that God has the last word."
            )
        },
        {
            "reference": "Esther 7:5",
            "verse_context": "King Ahasuerus demands to know the identity of the one who threatens Esther's people",
            "english": "Who is he and where is he who dared to do this?",
            "hebrew_phrase": "\u05de\u05d9 \u05d4\u05d5\u05d0 \u05d6\u05d4 \u05d5\u05d0\u05d9-\u05d6\u05d4 \u05d4\u05d5\u05d0",
            "transliteration": "Mi hu' zeh ve-'ei-zeh hu'",
            "acrostic_letters": "\u05d0 \u05d4 \u05d9 \u05d4",
            "acrostic_type": "Initial letters spelling EHYH ('I AM')",
            "direction": "forward",
            "letter_position": "initial",
            "speaker": "King Ahasuerus",
            "theological_significance": (
                "This fifth acrostic is the most theologically stunning. The king asks 'Who is he?' "
                "and the hidden acrostic answers: EHYH -- 'I AM' -- the very name God revealed to "
                "Moses at the burning bush (Exodus 3:14, 'ehyeh asher ehyeh'). The pagan king, "
                "demanding to know the identity of the threat, unknowingly encodes the divine "
                "self-revelation. The answer to 'Who is behind all this?' is hidden in his own "
                "question: I AM. The God who hides Himself in Esther reveals His identity precisely "
                "at the moment of judgment. Like the burning bush, the revelation comes embedded "
                "in a question about identity."
            ),
            "note": "This acrostic is counted separately from the four YHWH acrostics by most "
                    "scholars because it encodes a different divine name (EHYH vs. YHWH). "
                    "Bullinger's Companion Bible Appendix 60 documents all five."
        }
    ],

    # ======================================================================
    # GREEK ADDITIONS -- DETAILED DATA
    # ======================================================================
    "greek_additions": [
        {
            "section": "Addition A (= LXX 11:2-12:6)",
            "location": "Before Hebrew 1:1",
            "content_summary": (
                "Mordecai's prophetic dream: two great dragons prepare for battle while the "
                "nations gather against the righteous. A small spring becomes a mighty river "
                "(representing Esther). God remembers His people and vindicates the righteous. "
                "Also narrates Mordecai's discovery of the assassination plot by the eunuchs "
                "Gabatha and Tharra (= Bigthan and Teresh)."
            ),
            "verses_added": 17,
            "theological_purpose": (
                "Frames the entire narrative in explicitly apocalyptic terms. The dream introduces "
                "God as an active agent before the story even begins, transforming a court tale "
                "into a story of cosmic conflict between good and evil. This addition is the most "
                "radical departure from the Hebrew Esther's theological silence."
            ),
            "original_language": "Probably Semitic (Hebrew or Aramaic) -- traces of Semitic syntax"
        },
        {
            "section": "Addition B (= LXX 13:1-7)",
            "location": "After Hebrew 3:13",
            "content_summary": (
                "The full text of King Artaxerxes' (Ahasuerus') edict ordering the destruction "
                "of the Jews. Composed in elaborate Greek rhetorical style with formal decree "
                "language. Accuses the Jews of following 'alien laws,' being 'ill-disposed to "
                "our government,' and threatening the stability of the empire."
            ),
            "verses_added": 7,
            "theological_purpose": (
                "Provides the actual legal document authorizing genocide -- making the threat "
                "concrete and legalistic. The anti-Jewish rhetoric anticipates later Hellenistic "
                "and Roman anti-Jewish polemics. Historically significant as one of the earliest "
                "literary depictions of state-sponsored antisemitism as a formal policy."
            ),
            "original_language": "Greek -- ornate rhetorical style, no Semitic source"
        },
        {
            "section": "Addition C (= LXX 13:8-14:19)",
            "location": "After Hebrew 4:17",
            "content_summary": (
                "The prayers of Mordecai and Esther. Mordecai prays to God, confessing that he "
                "refused to bow to Haman not out of pride but to avoid giving to a mortal the "
                "honor due to God alone. Esther prays in ashes and sackcloth, asking God for "
                "courage, declaring that she hates the 'bed of the uncircumcised' (her marriage "
                "to the pagan king), keeps kosher ('your servant has not eaten at Haman's table'), "
                "and has not found joy since her elevation except in God."
            ),
            "verses_added": 30,
            "theological_purpose": (
                "This is the theological heart of the Additions. It directly addresses the two "
                "most troubling absences in Hebrew Esther: (1) no prayer and (2) no God. Mordecai "
                "and Esther pray passionately and explicitly to the God of Abraham. Esther's "
                "prayer also addresses the intermarriage problem by having her declare hatred for "
                "her Gentile marriage -- an apologetic move that would have satisfied communities "
                "like Qumran that found the intermarriage offensive."
            ),
            "original_language": "Probably Semitic -- strong Semitic syntax and vocabulary"
        },
        {
            "section": "Addition D (= LXX 15:1-16)",
            "location": "Replaces / expands Hebrew 5:1-2",
            "content_summary": (
                "An expanded account of Esther's approach to the king. She faints from fear; "
                "God changes the king's heart from anger to tenderness; the king catches her "
                "as she collapses and reassures her. The scene is far more dramatic and emotionally "
                "intense than the terse Hebrew account."
            ),
            "verses_added": 16,
            "theological_purpose": (
                "Explicitly attributes the king's favorable response to divine intervention: "
                "'God changed the spirit of the king to gentleness' (15:8 LXX). The Hebrew "
                "text simply says the king extended the scepter -- no reason given, no God "
                "mentioned. The Addition fills the gap with direct divine causation, "
                "transforming a human political moment into a theophanic event."
            ),
            "original_language": "Probably Semitic -- Semitic syntax visible"
        },
        {
            "section": "Addition E (= LXX 16:1-24)",
            "location": "After Hebrew 8:12",
            "content_summary": (
                "The full text of the king's second edict, reversing the first. Denounces Haman "
                "as a Macedonian (not Persian) conspirator who plotted to transfer the empire "
                "from Persia to Macedonia. Praises the Jews as 'governed by most righteous laws' "
                "and as 'children of the living God.' Orders the Jews to defend themselves and "
                "declares Purim a memorial day."
            ),
            "verses_added": 24,
            "theological_purpose": (
                "Puts explicit theology in the mouth of a pagan king: the Jews are 'children "
                "of the living God, most high, most mighty, who has directed the kingdom for us "
                "and for our ancestors in the most excellent order' (16:16 LXX). This transforms "
                "the Persian king into a confessor of YHWH -- a move parallel to Nebuchadnezzar's "
                "confessions in Daniel 3-4. Also adds anti-Macedonian polemic (Haman as Macedonian), "
                "which may reflect the Ptolemaic-era context of the Greek translation."
            ),
            "original_language": "Greek -- the most ornate and rhetorical of all the Additions"
        },
        {
            "section": "Addition F (= LXX 10:4-11:1)",
            "location": "After Hebrew 10:3",
            "content_summary": (
                "Mordecai interprets his dream from Addition A: the two dragons were himself and "
                "Haman; the spring that became a river was Esther; the nations were those who "
                "sought to destroy the Jews; God remembered His people and vindicated His "
                "inheritance. Concludes with the colophon identifying the translator as "
                "Lysimachus son of Ptolemy."
            ),
            "verses_added": 11,
            "theological_purpose": (
                "Provides an inclusio (literary bookend) with Addition A, framing the entire "
                "narrative as the fulfillment of a divinely-sent prophetic dream. The "
                "interpretation explicitly credits God with the deliverance: 'The Lord has "
                "saved his people; the Lord has rescued us from all these evils; God has done "
                "great signs and wonders' (10:9 LXX). This final addition ensures that the last "
                "word of Greek Esther is an explicit doxology -- the opposite of the Hebrew "
                "Esther's theological silence."
            ),
            "original_language": "Probably Semitic for the dream interpretation; colophon in Greek"
        }
    ],

    # ======================================================================
    # SUMMARY STATISTICS ON GREEK ADDITIONS
    # ======================================================================
    "additions_summary": {
        "total_added_verses": 107,
        "god_mentions_in_additions": "50+ (vs. 0 in the Hebrew text)",
        "prayers_added": 2,
        "dreams_added": 1,
        "dream_interpretations_added": 1,
        "royal_decrees_added": 2,
        "theological_transformation": (
            "The Additions transform Esther from the most theologically silent book in the "
            "Hebrew Bible into a conventional story of divine deliverance with explicit prayer, "
            "divine intervention, prophetic dreams, and doxological praise. The theological "
            "gap that made Esther unique is filled -- which means the Additions, however "
            "well-intentioned, actually destroy the very literary and theological distinctiveness "
            "that makes Hebrew Esther remarkable."
        )
    },

    # ======================================================================
    # NAME ETYMOLOGIES
    # ======================================================================
    "name_etymologies": {
        "esther": {
            "hebrew_name": "Hadassah (\u05d4\u05b2\u05d3\u05b7\u05e1\u05bc\u05b8\u05d4)",
            "meaning": "Myrtle (a fragrant plant; symbolizes righteousness in Jewish tradition)",
            "persian_name": "Esther (\u05d0\u05b6\u05e1\u05b0\u05ea\u05bc\u05b5\u05e8)",
            "etymology": "Almost certainly from Akkadian 'Istar' (Ishtar), the Mesopotamian "
                         "goddess of love, fertility, and war. Some scholars propose Old Persian "
                         "'stara' (star) as an alternative, but the Ishtar connection is more "
                         "widely accepted. The form 'Esther' may also be connected to the West "
                         "Semitic 'Astarte' (Ashtoreth in Hebrew).",
            "significance": "A Jewish woman bearing the name of the chief Babylonian goddess -- "
                           "likely a 'throne name' or court name adopted in the diaspora setting, "
                           "while her Hebrew name Hadassah preserved her Jewish identity."
        },
        "mordecai": {
            "hebrew_form": "Mordekhai (\u05de\u05b8\u05e8\u05b0\u05d3\u05b3\u05db\u05b7\u05d9)",
            "etymology": "From Akkadian 'Marduk' (or 'Marduku'), the supreme god of Babylon. "
                         "The name means 'follower/worshipper of Marduk' or may be a hypocorism "
                         "of 'Marduk-bel-shunu' ('Marduk is their lord'). Babylonian administrative "
                         "texts from the Persian period attest the name 'Mardukaya' for officials "
                         "at Susa and Persepolis.",
            "significance": "That the Jewish hero of this most Jewish of stories bears the name of "
                           "Babylon's chief god is one of the book's many ironies. It reflects the "
                           "reality of diaspora life: Jews adopted local theophoric names while "
                           "maintaining their covenantal identity. The same phenomenon appears with "
                           "Daniel (Belteshazzar = 'Bel, protect his life') and others."
        },
        "vashti": {
            "hebrew_form": "Vashti (\u05d5\u05b7\u05e9\u05c1\u05b0\u05ea\u05bc\u05b4\u05d9)",
            "etymology": "Possibly from Old Persian 'vahista' meaning 'best' or 'most excellent.' "
                         "Some scholars connect it to the Elamite 'mashti.' The identification with "
                         "Herodotus's 'Amestris' is phonetically possible (Vashti ~ Amestris via "
                         "Elamite intermediary) but remains unproven.",
            "significance": "If Vashti = Amestris, the biblical and Greek historical traditions can "
                           "be partially reconciled. But Amestris remained powerful throughout Xerxes' "
                           "reign (and into her son Artaxerxes I's), which is difficult to square "
                           "with Vashti's deposition in Esther 1."
        },
        "haman": {
            "hebrew_form": "Haman (\u05d4\u05b8\u05de\u05b8\u05df)",
            "designation": "Haman the Agagite (ha-'Agagi)",
            "etymology": "The designation 'Agagite' connects Haman to Agag, king of the Amalekites "
                         "(1 Samuel 15). This is likely a literary/theological designation rather "
                         "than literal genealogy: Haman is an 'Amalekite' in the sense that he is "
                         "the archetypal enemy of Israel, continuing the eternal enmity between "
                         "Israel and Amalek (Exodus 17:16, Deuteronomy 25:17-19). The conflict "
                         "Mordecai-vs-Haman thus reenacts Saul-vs-Agag and Israel-vs-Amalek.",
            "significance": "The 'Agagite' label transforms the Esther narrative from mere court "
                           "intrigue into a chapter in the cosmic conflict between Israel and its "
                           "archetypal enemy. Saul failed to destroy Agag (1 Samuel 15); Mordecai "
                           "and Esther succeed where Saul failed."
        }
    },

    # ======================================================================
    # LITERARY STRUCTURE AND REVERSALS
    # ======================================================================
    "literary_reversals": {
        "description": (
            "Esther is structured around a stunning series of reversals (Hebrew: nahafokh hu, "
            "'it was turned upside down,' 9:1) that are the narrative engine of the book and "
            "the primary vehicle for expressing providence without naming God."
        ),
        "reversals": [
            {"setup": "Vashti is queen", "reversal": "Esther becomes queen"},
            {"setup": "Haman is honored, Mordecai refuses to bow", "reversal": "Mordecai is honored, Haman must lead his horse"},
            {"setup": "Haman builds gallows for Mordecai", "reversal": "Haman is hanged on his own gallows"},
            {"setup": "A decree orders the destruction of the Jews", "reversal": "A decree authorizes the Jews to defend themselves"},
            {"setup": "The date chosen by lot (pur) for destruction", "reversal": "That date becomes the festival of Purim (celebration)"},
            {"setup": "Haman's sons are to inherit his power", "reversal": "Haman's sons are hanged on gallows"},
            {"setup": "Sorrow and mourning (4:3)", "reversal": "'Light and gladness and joy and honor' (8:16)"},
            {"setup": "The enemies expected to overpower the Jews (9:1a)", "reversal": "Nahafokh hu -- 'it was reversed' -- the Jews overpowered their enemies (9:1b)"}
        ],
        "theological_note": (
            "The reversal structure IS the theology. Where other biblical books state 'God did X,' "
            "Esther shows reversal after reversal and lets the reader draw the conclusion. The "
            "Hebrew phrase 'nahafokh hu' (9:1) -- 'it was turned upside down' -- is the thematic "
            "key to the entire book. Who turns things upside down? The text never says. The reader "
            "is meant to know."
        )
    },

    # ======================================================================
    # READER NOTES AND STUDY GUIDANCE
    # ======================================================================
    "reader_notes": [
        {
            "type": "hermeneutic",
            "title": "How to Read Esther's Silence",
            "body": (
                "The temptation is to 'fix' Esther -- to read God into the text where the "
                "author deliberately left God out. The Greek Additions do exactly this, and "
                "in doing so they miss the point. The Hebrew Esther is not broken. Its silence "
                "is not a deficiency but a theological statement: God's providence does not "
                "require God's name. The book invites a mature faith that perceives divine "
                "action in ordinary events without requiring miraculous proof. Read Esther on "
                "its own terms before supplementing it with the Additions."
            )
        },
        {
            "type": "warning",
            "title": "The Acrostics: Signal or Noise?",
            "body": (
                "The YHWH acrostics are fascinating and may well be intentional -- the majuscular "
                "scribal tradition and the symmetrical patterns (2 forward/2 backward, 2 initial/"
                "2 final, 2 by Jews/2 by Gentiles) argue strongly for design. However, they should "
                "not be used as proof-texts to claim Esther 'really does' mention God. Even if "
                "intentional, the acrostics reinforce the HIDDENNESS of God, not His overt presence. "
                "The Name is encoded, not proclaimed. That is the entire point."
            )
        },
        {
            "type": "context",
            "title": "Why the Dead Sea Scrolls Absence Matters",
            "body": (
                "The Qumran absence does NOT prove Esther is non-canonical. It proves that one "
                "specific Jewish community -- the Yahad/Essenes -- either rejected or ignored it. "
                "Given what we know about the Essenes (strict purity, solar calendar, separatism, "
                "intense theocentrism), their rejection of Esther is entirely predictable. It tells "
                "us about them, not about Esther. Mainstream Judaism has read Esther at Purim for "
                "over two millennia. The Essenes disappeared in 68 CE."
            )
        },
        {
            "type": "connection",
            "title": "Esther and the Divine Council Framework",
            "body": (
                "Esther operates in a different register from the divine council texts documented "
                "elsewhere in this app. The Watchers, the Sons of God, the heavenly court -- all "
                "of these involve explicit supernatural activity. Esther shows the OTHER mode of "
                "divine governance: not through angels and cosmic battles but through human "
                "decisions, political systems, and apparent coincidence. Both modes are biblical. "
                "The God who commands heavenly armies in the War Scroll is the same God who keeps "
                "a king awake at night in Esther 6:1. The 'hidden God' of Esther is not a lesser "
                "God -- He is the same God operating through a different means."
            )
        },
        {
            "type": "scholarship",
            "title": "The Genre Question",
            "body": (
                "Scholars debate Esther's genre: is it historical narrative, historical novella, "
                "diaspora tale, wisdom narrative, or festive legend? The answer matters because "
                "genre determines how we evaluate historical claims. If Esther is strict history, "
                "the absence from Persian records is a problem. If it is a historically-grounded "
                "novella (like Judith or Tobit), the absence is expected. Most modern scholars "
                "classify it as a 'historicized wisdom tale' or 'diaspora novella' with a genuine "
                "Persian-period setting but a literary rather than strictly historiographic purpose. "
                "The book's primary goal is not to record events but to explain and authorize the "
                "festival of Purim and to model faithful Jewish life under foreign rule."
            )
        }
    ],

    # ======================================================================
    # KEY SCHOLARLY REFERENCES
    # ======================================================================
    "bibliography": [
        "Jon D. Levenson, Esther: A Commentary, Old Testament Library (Westminster John Knox, 1997)",
        "Michael V. Fox, Character and Ideology in the Book of Esther, 2nd ed. (Eerdmans, 2001)",
        "Adele Berlin, JPS Bible Commentary: Esther (Jewish Publication Society, 2001)",
        "Frederic Bush, Ruth, Esther, Word Biblical Commentary (Zondervan, 1996)",
        "Carey Moore, Esther, Anchor Bible (Doubleday, 1971)",
        "Carey Moore, Daniel, Esther, and Jeremiah: The Additions, Anchor Bible 44 (Doubleday, 1977)",
        "Karen Jobes, The Alpha-Text of Esther (SBL, 1996)",
        "Chloe T. Sun, Conspicuous in His Absence (IVP Academic, 2021)",
        "Sandra Berg, The Book of Esther: Motifs, Themes, and Structure (Scholars Press, 1979)",
        "Edwin Yamauchi, Persia and the Bible (Baker Academic, 1990)",
        "E.W. Bullinger, The Companion Bible, Appendix 60 (1922)",
        "Martin Abegg Jr., Peter Flint, Eugene Ulrich, The Dead Sea Scrolls Bible (HarperOne, 1999)",
        "Emanuel Tov, Textual Criticism of the Hebrew Bible, 3rd ed. (Fortress, 2012)",
        "Lee McDonald, The Biblical Canon: Its Origin, Transmission, and Authority (Hendrickson, 2007)",
        "Roger Beckwith, The Old Testament Canon of the New Testament Church (Eerdmans, 1985)"
    ]
}
