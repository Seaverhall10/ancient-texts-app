"""
info.py — Church History: Pentecost to Reformation: Scholarly Text Introduction

From the Upper Room to the 95 Theses — how the apostolic faith was preserved,
distorted, and recovered. An honest examination of church history through the
lens of Scripture, with particular attention to where traditions diverged from
biblical teaching.
"""

TEXT_INFO = {
    "text_id": "church_history",
    "display_name": "Church History: Pentecost to Reformation",

    # ── CANONICAL STATUS ──────────────────────────────────────────────
    "canonical_status": {
        "status": "thematic_study",
        "label": "Thematic Study — Church History",
        "detail": "This is not a primary text but a study resource examining the history "
                  "of the Christian church from Pentecost (c. AD 30) through the "
                  "Reformation (16th century). It evaluates historical developments "
                  "against the standard of Scripture, using the Berean approach (Acts "
                  "17:11) — examining every claim, tradition, and practice against what "
                  "the Bible actually teaches. All Scripture quotations use the ESV "
                  "unless otherwise noted."
    },

    # ── AUTHORSHIP ────────────────────────────────────────────────────
    "authorship": {
        "traditional": "This study text was compiled from multiple historical and "
                       "theological sources, synthesizing primary documents, church "
                       "father writings, conciliar records, and modern scholarship.",

        "scholarly_debate": "Church history scholarship spans an enormous range of perspectives. "
                           "Key sources include Eusebius of Caesarea (Church History, c. AD 324), "
                           "Philip Schaff (History of the Christian Church, 8 vols.), Justo "
                           "Gonzalez (The Story of Christianity), and Alister McGrath (Christianity's "
                           "Dangerous Idea). Catholic and Protestant historians often interpret the "
                           "same events differently — particularly regarding papal authority, the "
                           "role of tradition, and the Reformation. This study evaluates all claims "
                           "against Scripture as the final standard.",

        "bottom_line": "Church history is not a neutral subject — every historian brings "
                       "theological commitments. This study is transparent about its "
                       "commitment: Scripture is the ultimate authority (sola Scriptura), "
                       "and traditions, councils, and popes are evaluated by that standard, "
                       "not the reverse."
    },

    # ── DATE ──────────────────────────────────────────────────────────
    "date": {
        "traditional": "Covers roughly AD 30 (Pentecost) through the 16th century "
                       "(Protestant Reformation and Catholic Counter-Reformation).",
        "critical_range": "Apostolic era: AD 30-100. Patristic era: AD 100-451. "
                         "Early Medieval: AD 451-1054. High Medieval: AD 1054-1517. "
                         "Reformation: AD 1517-1563.",
        "evidence": "Primary sources include the New Testament (Acts, Pauline epistles), "
                    "apostolic fathers (Clement of Rome, Ignatius, Polycarp), church "
                    "father writings (Irenaeus, Tertullian, Origen, Augustine, Chrysostom), "
                    "conciliar records (Nicaea, Chalcedon, Trent), papal documents, and "
                    "the reformers' writings (Luther, Calvin, Zwingli)."
    },

    # ── AUDIENCE & PURPOSE ────────────────────────────────────────────
    "audience": {
        "original_audience": "Students and believers seeking to understand how the church "
                            "developed from the apostolic period to the Reformation. Designed "
                            "especially for those wrestling with Catholic claims about papal "
                            "authority, apostolic succession, and the role of tradition.",

        "purpose": "To provide an honest, Scripture-grounded survey of church history that "
                   "neither whitewashes Protestant failings nor unfairly caricatures Catholic "
                   "positions. The goal is truth, not tribalism. Where Rome departed from "
                   "Scripture, we say so clearly. Where the Reformers recovered biblical "
                   "truth, we celebrate it. Where all sides failed, we acknowledge it.",

        "theological_intent": "The church belongs to Christ, not to any institution, pope, or "
                             "tradition. The history of the church is the history of God "
                             "preserving His people through deeply flawed human structures. "
                             "Understanding that history equips believers to hold fast to what "
                             "Scripture teaches while learning from both the triumphs and "
                             "failures of those who came before."
    },

    # ── ORIGINAL LANGUAGE ─────────────────────────────────────────────
    "language": {
        "original": "Primary sources span multiple languages: Koine Greek (NT, early "
                    "fathers), Latin (Western church fathers, papal documents, conciliar "
                    "records), Syriac (Eastern church traditions), and various vernacular "
                    "languages (Reformation writings).",
        "script": "Greek uncial/minuscule, Latin script, with occasional Syriac and "
                  "Coptic sources.",
        "linguistic_notes": "Key theological terms cross language boundaries: ekklesia "
                           "(Greek, 'assembly/church'), papa/pontifex (Latin, 'father/ "
                           "bridge-builder'), petros/petra (Greek, the 'rock' debate in "
                           "Matthew 16:18), sola Scriptura/sola fide/sola gratia (Latin, "
                           "the Reformation slogans). Understanding the original language "
                           "of key terms often resolves what appear to be intractable "
                           "theological debates.",
        "grammar_match": "The linguistic evidence in key passages (especially Matthew 16:18 "
                        "and the petros/petra distinction) supports the Protestant reading "
                        "that 'the rock' is Peter's confession, not Peter himself."
    },

    # ── SCRIPTURE ALIGNMENT ───────────────────────────────────────────
    "scripture_alignment": {
        "verdict": "This study evaluates every historical development against Scripture "
                   "as the final standard. Where church history aligns with Scripture, "
                   "it is celebrated. Where it diverges, the divergence is clearly noted.",

        "where_it_aligns": [
            "Acts 2 — The church was born at Pentecost through the Holy Spirit, not "
            "through institutional decree",
            "Acts 17:11 — The Berean model of testing all teaching against Scripture "
            "is the method used throughout this study",
            "1 Peter 5:1-3 — Peter calls himself a 'fellow elder,' not a supreme "
            "pontiff, which informs the evaluation of papal claims",
            "Galatians 2:11-14 — Paul publicly corrected Peter, showing no doctrine "
            "of papal infallibility in the apostolic church",
            "Revelation 2-3 — Jesus evaluates churches directly, showing that the "
            "Head of the church is Christ, not any human representative"
        ],

        "where_it_diverges": [],

        "reader_guidance": "This study takes a firm but fair approach. When evaluating "
                          "Roman Catholic claims about papal authority, Marian doctrines, "
                          "purgatory, or transubstantiation, the standard is always 'What "
                          "does Scripture say?' — not 'What does tradition say about what "
                          "Scripture says.' Tradition is valuable as a witness but is never "
                          "equal to or above Scripture."
    },

    # ── MANUSCRIPT TRADITION ──────────────────────────────────────────
    "manuscripts": {
        "earliest": "The primary sources for church history begin with the New Testament "
                    "itself (c. AD 49-95) and continue through the apostolic fathers "
                    "(late 1st-early 2nd century).",
        "major_witnesses": [
            {"name": "Didache (Teaching of the Twelve)", "date": "c. AD 50-120",
             "note": "One of the earliest non-canonical Christian documents. Shows "
                     "early church liturgical practices and church order."},
            {"name": "1 Clement", "date": "c. AD 96",
             "note": "Letter from the church at Rome to Corinth. Often cited in papal "
                     "debates — notably, Clement writes on behalf of the church, not as "
                     "a papal authority."},
            {"name": "Letters of Ignatius", "date": "c. AD 110",
             "note": "Seven letters showing early episcopal structure but no evidence "
                     "of Roman primacy in the later papal sense."},
            {"name": "Eusebius, Church History", "date": "c. AD 324",
             "note": "The first comprehensive church history. Essential primary source "
                     "but reflects Eusebius's pro-Constantine perspective."}
        ],
        "reliability": "Church history relies on a rich but often partisan primary source "
                       "tradition. Both Catholic and Protestant sources must be read "
                       "critically. The Scripture against which all traditions are measured "
                       "is the best-attested document collection in antiquity."
    },

    # ── HISTORICAL CONTEXT ────────────────────────────────────────────
    "historical_context": {
        "setting": "The church emerged in the Roman Empire and was shaped by Jewish "
                   "theological categories, Greek philosophical language, and Roman "
                   "political structures. All three influences left permanent marks "
                   "on Christian theology and practice.",

        "geography": "Jerusalem (origin), Antioch (first Gentile church), Rome (Western "
                     "center), Constantinople (Eastern center), Alexandria and Carthage "
                     "(North African theology), Wittenberg and Geneva (Reformation).",

        "historical_connections": "Key turning points include: the destruction of the Temple "
                                 "(AD 70), the Edict of Milan (AD 313), the Council of Nicaea "
                                 "(AD 325), the fall of Rome (AD 476), the Great Schism "
                                 "(AD 1054), the Crusades (1096-1291), the Western Schism "
                                 "(1378-1417), and the Reformation (1517+). Each event "
                                 "reshaped the institutional church in ways that must be "
                                 "evaluated against the apostolic standard."
    },

    # ── DIVINE COUNCIL / HEISER FRAMEWORK ─────────────────────────────
    "divine_council": {
        "relevance": "moderate",
        "summary": "The divine council worldview of the biblical authors was gradually "
                   "eclipsed during the patristic period as Greek philosophical categories "
                   "(Neoplatonism, Aristotelian metaphysics) replaced the Hebrew "
                   "supernatural worldview. The early fathers still engaged with the "
                   "Watchers tradition and supernatural beings (Irenaeus, Justin Martyr, "
                   "Tertullian all discuss Genesis 6:1-4 as involving divine beings). But "
                   "by the medieval period, the divine council framework was largely "
                   "replaced by a Thomistic/Aristotelian angelology that domesticated the "
                   "biblical supernatural world. The Reformation recovered sola Scriptura "
                   "but did not fully recover the divine council worldview — that recovery "
                   "had to wait for modern scholarship informed by the Dead Sea Scrolls.",

        "key_heiser_refs": [
            "The Unseen Realm, chapter 1 (the supernatural worldview the church lost)",
            "Supernatural, introduction (why the biblical worldview matters)",
            "Reversing Hermon, chapter 1 (the Second Temple context the church forgot)"
        ]
    },

    # ── WARNINGS / READER NOTES ───────────────────────────────────────
    "reader_notes": [
        {
            "type": "context",
            "title": "Firm but Fair — Not Anti-Catholic",
            "body": "This study takes strong positions against certain Roman Catholic "
                    "doctrines (papal infallibility, purgatory, transubstantiation, Marian "
                    "dogmas) because the evidence — both biblical and historical — does "
                    "not support them. But this is not anti-Catholic prejudice. It is the "
                    "Berean method applied consistently. Where Catholic scholars have made "
                    "genuine contributions to biblical understanding (textual criticism, "
                    "patristic scholarship, liturgical tradition), we acknowledge them. "
                    "The target is never Catholic people — it is claims that cannot "
                    "withstand biblical scrutiny."
        },
        {
            "type": "theology",
            "title": "The Petros/Petra Distinction",
            "body": "Matthew 16:18 is perhaps the most contested verse in church history "
                    "debates. Jesus says to Peter: 'You are Petros (masculine, 'a stone') "
                    "and on this petra (feminine, 'bedrock/cliff') I will build my church.' "
                    "The Catholic reading identifies Peter as the rock. The Protestant "
                    "reading identifies the rock as Peter's confession ('You are the "
                    "Christ, the Son of the living God'). The linguistic evidence (different "
                    "Greek words), the immediate context (v. 23 — Jesus calls Peter 'Satan' "
                    "moments later), and the early patristic evidence (Chrysostom and "
                    "Augustine both read 'rock' as the confession) all favor the Protestant "
                    "reading. Peter himself, in 1 Peter 2:4-8, identifies Christ as the "
                    "cornerstone — never claiming that title for himself."
        },
        {
            "type": "warning",
            "title": "History Is Written by the Powerful",
            "body": "Much of what we know about early Christianity comes from the winners "
                    "of theological debates. Eusebius, the 'father of church history,' was "
                    "a political ally of Constantine. Medieval church history was recorded "
                    "almost exclusively by monks and clerics loyal to the papacy. The "
                    "Reformation is told differently by Lutherans, Calvinists, Anglicans, "
                    "and Catholics. Every source must be read critically, and every claim "
                    "must be tested against Scripture."
        }
    ]
}
