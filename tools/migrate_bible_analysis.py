"""
Migrate NT + Non-Canonical sections of bible_analysis.py to structured fields.
Adds key_claim, contested_words, hidden_connections, what_it_doesnt_say,
unusual_characters, patterns, mistranslations to each non-stub entry.
"""

import re
import sys

FILE_PATH = r"C:\Users\User\Desktop\ANCIENT_TEXTS Study App\data\bible_analysis.py"

# ── Structured fields for each book (keyed by id) ────────────────────────

STRUCTURED = {}

# ═══════════════════════════════════════════════════
#  NEW TESTAMENT
# ═══════════════════════════════════════════════════

STRUCTURED['matthew'] = {
    "key_claim": "Matthew presents Jesus as the legitimate Davidic King whose Great Commission ('all authority in heaven and on earth') reverses the Deut 32:8 allotment — reclaiming the nations from the corrupt bene elohim.",
    "contested_words": [
        {"word": "ekklesia", "greek": "\u1f10\u03ba\u03ba\u03bb\u03b7\u03c3\u03af\u03b1", "issue": "'Church' hides the political meaning — governing assembly with judicial authority, declared at Caesarea Philippi (base of Hermon, Watcher descent site).", "severity": "CRITICAL"},
        {"word": "basileia ton ouranon", "greek": "\u03b2\u03b1\u03c3\u03b9\u03bb\u03b5\u03af\u03b1 \u03c4\u1ff6\u03bd \u03bf\u1f50\u03c1\u03b1\u03bd\u1ff6\u03bd", "issue": "'Kingdom of heaven' — uniquely Matthean circumlocution. Not 'going to heaven' but heaven's government invading earth.", "severity": "CRITICAL"},
        {"word": "pleroo", "greek": "\u03c0\u03bb\u03b7\u03c1\u03cc\u03c9", "issue": "'Fulfill' — appears 16 times. Does it mean predict-and-complete, or fill-up-the-meaning? Shapes how we read all OT quotations.", "severity": "MAJOR"},
        {"word": "proskyneo", "greek": "\u03c0\u03c1\u03bf\u03c3\u03ba\u03c5\u03bd\u03ad\u03c9", "issue": "'Worship' — magi worship the infant Jesus (2:11). Same word used for God alone. Matthew presents Jesus receiving divine honors from birth.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "deuteronomy", "why": "Jesus quotes Deuteronomy three times to defeat Satan (4:4, 7, 10 from Deut 6-8); Great Commission reverses Deut 32:8 allotment"},
        {"target": "genesis", "why": "Genealogy (1:1-17) traces the seed line from Abraham through David to Christ — Gen 3:15 fulfilled"},
        {"target": "daniel", "why": "Son of Man coming on clouds (24:30, 26:64) draws directly from Dan 7:13 — divine cloud-rider claim"},
        {"target": "1enoch", "why": "Caesarea Philippi declaration (16:13-20) is at the base of Mount Hermon — the Watcher descent site of 1 Enoch 6"},
        {"target": "revelation", "why": "Great Commission's 'all authority' claim finds culmination in Rev 11:15 — 'The kingdom of the world has become the kingdom of our Lord'"},
        {"target": "psalms", "why": "Ps 2:6-7 (the divine Son enthroned) and Ps 110:1 (sit at my right hand) underpin Matthew's royal Christology"},
    ],
    "what_it_doesnt_say": [
        "Never explains WHY Jesus chose 12 apostles — the number parallels the 12 tribes but Matthew never makes the connection explicit",
        "The magi's identity and origin are never specified — tradition says three kings, but the text gives no number or rank",
        "No account of Jesus between ages 12 and 30 — nearly two decades of silence",
        "Never names the 'star' the magi followed or explains its nature — astronomical, angelic, or supernatural?",
    ],
    "unusual_characters": [
        {"name": "The Magi", "ref": "2:1", "detail": "Pagan astrologers who recognize Israel's king before Israel does — Gentile worship before Jewish recognition.", "connections": ["numbers", "isaiah"]},
        {"name": "Pilate's wife", "ref": "27:19", "detail": "Only in Matthew — receives a dream warning about Jesus. A pagan woman gets divine revelation while Jewish leaders reject it.", "connections": []},
        {"name": "The centurion at the cross", "ref": "27:54", "detail": "'Truly this was the Son of God' — a Roman soldier makes the confession Israel's leaders refuse.", "connections": ["mark"]},
    ],
    "patterns": [
        "Five major discourse blocks (chs. 5-7, 10, 13, 18, 23-25) mirror the five books of Torah — Jesus as the new Moses giving new Torah",
        "Fulfillment formula: 'This was to fulfill what was spoken by the prophet' appears 12+ times — Matthew reads the entire OT as pointing to Christ",
        "Genealogy structure: 3 sets of 14 generations (1:17) — 14 = numerical value of David (dalet-vav-dalet = 4+6+4)",
        "Mountain theology: Temptation mount, Sermon mount, Transfiguration mount, Olivet Discourse, Great Commission mount — Jesus acts on mountains like Moses",
    ],
    "mistranslations": [
        {"english": "church", "original": "ekklesia", "issue": "Injects centuries of institutional religion into a term meaning 'governing assembly' with judicial and cosmic authority"},
        {"english": "kingdom of heaven", "original": "basileia ton ouranon", "issue": "Sounds like a destination ('going to heaven') when it means heaven's reign breaking into earth"},
        {"english": "fulfilled", "original": "pleroo", "issue": "Implies mere prediction-fulfillment when the Greek can mean 'filled up the meaning of' — a richer hermeneutic"},
    ],
}

STRUCTURED['mark'] = {
    "key_claim": "Mark 14:62 is the christological climax of the Gospel — Jesus claims to be the divine cloud-rider of Daniel 7:13 seated at God's right hand (Ps 110:1), and the high priest tears his robes because he understands the DIVINE claim, not merely a messianic one.",
    "contested_words": [
        {"word": "euangelion", "greek": "\u03b5\u1f50\u03b1\u03b3\u03b3\u03ad\u03bb\u03b9\u03bf\u03bd", "issue": "'Gospel' — in Roman usage, an imperial proclamation of victory or a new emperor's accession. Mark co-opts Caesar's word for Jesus.", "severity": "CRITICAL"},
        {"word": "huios tou theou", "greek": "\u03c5\u1f31\u1f78\u03c2 \u03c4\u03bf\u1fe6 \u03b8\u03b5\u03bf\u1fe6", "issue": "'Son of God' — Roman emperors claimed this title (divi filius). Mark's opening line is a direct counter-claim to Caesar.", "severity": "CRITICAL"},
        {"word": "euthys", "greek": "\u03b5\u1f50\u03b8\u03cd\u03c2", "issue": "'Immediately' — appears ~40 times. Mark's urgency is theological: the kingdom is breaking in NOW, not gradually.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "daniel", "why": "Mark 14:62 combines Dan 7:13 (cloud-rider) with Ps 110:1 (enthroned at right hand) — the two most explosive OT texts fused into one claim"},
        {"target": "isaiah", "why": "Mark 1:2-3 opens with Isaiah's 'prepare the way of the LORD' — the way being prepared is for YHWH himself, and Jesus walks it"},
        {"target": "psalms", "why": "Ps 110:1 quoted at 12:36 and alluded at 14:62 — the Lord who sits at YHWH's right hand is the interpretive key to Mark's Christology"},
        {"target": "1peter", "why": "Mark traditionally understood as Peter's memoir; 1 Peter's theology of suffering mirrors Mark's suffering-Messiah theme"},
        {"target": "exodus", "why": "The feeding of 5,000 (6:30-44) and 4,000 (8:1-10) echo Moses' manna provision — Jesus as the new Moses in the wilderness"},
    ],
    "what_it_doesnt_say": [
        "No birth narrative — Mark begins with Jesus as an adult at baptism, skipping 30 years entirely",
        "The original ending (16:8) stops at the empty tomb with the women fleeing in fear — no resurrection appearances",
        "No genealogy — unlike Matthew and Luke, Mark provides no family lineage for Jesus",
        "Never records the Sermon on the Mount — Mark focuses on actions over extended teaching",
    ],
    "unusual_characters": [
        {"name": "The Gerasene demoniac", "ref": "5:1-20", "detail": "'My name is Legion, for we are many' — a Roman military term for 6,000 soldiers. The demons beg not to be sent 'out of the region' — territorial assignment.", "connections": ["luke"]},
        {"name": "The young man who fled naked", "ref": "14:51-52", "detail": "Only in Mark — flees naked at Jesus' arrest. Possibly Mark himself. Echoes Gen 39 (Joseph fleeing) and Amos 2:16.", "connections": []},
        {"name": "Bartimaeus", "ref": "10:46", "detail": "The only healed blind man named — calls Jesus 'Son of David' publicly. Sees what the disciples cannot.", "connections": []},
    ],
    "patterns": [
        "Messianic Secret: Jesus repeatedly commands silence about his identity (1:34, 1:44, 3:12, 5:43, 8:30) — revelation must come through the cross, not miracles",
        "Sandwich structure (intercalation): Mark inserts one story inside another to create interpretive tension (e.g., 5:21-43, 11:12-25, 14:1-11)",
        "Two-stage healing of the blind man (8:22-26) mirrors the disciples' two-stage understanding: partial sight at Caesarea Philippi, full sight after resurrection",
        "Three passion predictions (8:31, 9:31, 10:33-34) followed by misunderstanding followed by teaching on discipleship — a repeating pedagogical cycle",
    ],
    "mistranslations": [
        {"english": "gospel", "original": "euangelion", "issue": "Loses the imperial-proclamation context — this was Caesar's word for announcing military victories and enthronements"},
        {"english": "immediately", "original": "euthys", "issue": "Often softened to 'then' or 'just then' in translations, hiding Mark's theological urgency about the inbreaking kingdom"},
        {"english": "Son of God", "original": "huios tou theou", "issue": "Modern readers hear theological title; first-century readers heard a direct challenge to the emperor's claim to divine sonship"},
    ],
}

STRUCTURED['luke'] = {
    "key_claim": "Luke presents the gospel as cosmic warfare through the Spirit — Jesus sees Satan fall like lightning (10:18) and Satan 'demands' to sift Peter (22:31), revealing the same divine council dynamic as Job 1-2 operating behind the scenes of Jesus' ministry.",
    "contested_words": [
        {"word": "dynamis", "greek": "\u03b4\u03cd\u03bd\u03b1\u03bc\u03b9\u03c2", "issue": "'Power' — used for the Holy Spirit's empowerment. Luke-Acts is the Spirit narrative: conceived by Spirit, anointed by Spirit, empowered by Spirit, filled with Spirit at Pentecost.", "severity": "CRITICAL"},
        {"word": "sozo", "greek": "\u03c3\u1f7d\u03b6\u03c9", "issue": "'Save/heal' — same Greek word. Luke uses it for physical healing AND spiritual salvation interchangeably, refusing to separate body and soul.", "severity": "MAJOR"},
        {"word": "exaiteomai", "greek": "\u1f10\u03be\u03b1\u03b9\u03c4\u03ad\u03bf\u03bc\u03b1\u03b9", "issue": "Satan 'demanded' (22:31) — legal term for requesting custody. Same dynamic as Job 1-2: Satan petitions the divine council for permission.", "severity": "CRITICAL"},
    ],
    "hidden_connections": [
        {"target": "job", "why": "Satan 'demands to sift you like wheat' (22:31) mirrors Job 1-2 — the adversary petitions the divine council for permission to test the righteous"},
        {"target": "leviticus", "why": "Jesus' inaugural sermon (4:18-19) quotes Isa 61 declaring Jubilee fulfilled — Lev 25's economic reset realized in the kingdom"},
        {"target": "acts", "why": "Luke-Acts is a unified two-volume work: Luke = Jesus' ministry by the Spirit, Acts = the ekklesia's ministry by the same Spirit"},
        {"target": "1samuel", "why": "Mary's Magnificat (1:46-55) directly echoes Hannah's prayer (1 Sam 2:1-10) — barren woman bearing the deliverer"},
        {"target": "genesis", "why": "Luke's genealogy (3:23-38) goes back to 'Adam, son of God' — Jesus as the new Adam, reclaiming what the first Adam lost"},
    ],
    "what_it_doesnt_say": [
        "Never explains how Satan 'fell like lightning from heaven' (10:18) — is this a past event or a present vision?",
        "The 70/72 sent out parallel the 70 nations of Gen 10 but Luke never makes the connection explicit",
        "Unique parables (Good Samaritan, Prodigal Son, Rich Man and Lazarus) have no parallels — why only Luke?",
        "Jesus' prayer life is emphasized (11 references to prayer) but what he prays is rarely disclosed",
    ],
    "unusual_characters": [
        {"name": "Zechariah", "ref": "1:5-25", "detail": "Struck mute for doubting Gabriel — a priest silenced in the temple. His speech returns when he writes 'His name is John.'", "connections": ["malachi"]},
        {"name": "Simeon", "ref": "2:25-35", "detail": "Told he would not die before seeing the Messiah. Calls Jesus 'a light for revelation to the Gentiles' — the nations theme from birth.", "connections": ["isaiah"]},
        {"name": "The thief on the cross", "ref": "23:40-43", "detail": "'Today you will be with me in Paradise' — only in Luke. Salvation at the last moment, no works, no baptism, just faith.", "connections": []},
    ],
    "patterns": [
        "Travel narrative (9:51-19:27): the entire central section is structured as a journey to Jerusalem — Jesus 'sets his face' toward the cross",
        "Reversal theme: the rich sent away empty, the poor filled; the first last, the last first; outsiders in, insiders out",
        "Prayer bookends: Jesus prays at every major transition — baptism, choosing apostles, transfiguration, Gethsemane, the cross",
        "Spirit-power sequence: conceived by Spirit (1:35), anointed by Spirit (3:22), led by Spirit into wilderness (4:1), returns in power of Spirit (4:14) — programmatic for Acts",
    ],
    "mistranslations": [
        {"english": "saved", "original": "sozo", "issue": "Splitting 'save' (spiritual) from 'heal' (physical) creates a false divide — Luke uses one word for both because wholeness is the point"},
        {"english": "demanded to have you", "original": "exaiteomai", "issue": "Often softened — the Greek is a legal demand, a petition before a court. Satan operates within a judicial framework, not chaos"},
        {"english": "power", "original": "dynamis", "issue": "Generic English hides the specific Spirit-empowerment theology that drives Luke-Acts"},
    ],
}

STRUCTURED['john'] = {
    "key_claim": "John's Prologue ('In the beginning was the Word, and the Word was with God, and the Word was God') establishes Jesus as a pre-existent divine person present at creation — two persons, both called God, one distinct from the other.",
    "contested_words": [
        {"word": "logos", "greek": "\u03bb\u03cc\u03b3\u03bf\u03c2", "issue": "'Word' — Greek philosophy (divine reason), Hebrew background (davar YHWH = God's active creative speech), Aramaic memra (divine intermediary). John bridges all three.", "severity": "CRITICAL"},
        {"word": "ego eimi", "greek": "\u1f10\u03b3\u03ce \u03b5\u1f30\u03bc\u03b9", "issue": "'I AM' — Jesus' seven absolute 'I AM' statements echo God's self-revelation at the burning bush (Ex 3:14). The Jews try to stone him for it (8:58-59).", "severity": "CRITICAL"},
        {"word": "monogenes", "greek": "\u03bc\u03bf\u03bd\u03bf\u03b3\u03b5\u03bd\u03ae\u03c2", "issue": "'Only begotten' or 'one and only/unique'? Mono-genes = unique-kind, not mono-gennao (only-born). Shapes whether the Son is 'begotten' or 'unique.'", "severity": "CRITICAL"},
        {"word": "parakletos", "greek": "\u03c0\u03b1\u03c1\u03ac\u03ba\u03bb\u03b7\u03c4\u03bf\u03c2", "issue": "'Comforter/Helper/Advocate' — legal term for a defense attorney. The Spirit is a divine advocate continuing Jesus' work in the divine council's earthly court.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "'In the beginning' (1:1) deliberately echoes Gen 1:1 — the Word who creates in Genesis is now identified as the incarnate Son"},
        {"target": "psalms", "why": "Jesus quotes Ps 82:6 ('you are gods') in John 10:34 — directly affirming the divine council and using it to defend his own deity claim"},
        {"target": "exodus", "why": "Seven 'I AM' statements echo Ex 3:14; Jesus replaces every Jewish institution: temple (2:19-21), manna (6:35), light (8:12), Passover lamb (1:29)"},
        {"target": "1enoch", "why": "The 'Son of Man' title in John draws from Dan 7:13 and the Parables of Enoch (1 En 37-71) where the Son of Man is pre-existent and enthroned"},
        {"target": "revelation", "why": "John 1:1-3 (the Word creating all things) finds its culmination in Rev 19:13 — the returning warrior 'whose name is called The Word of God'"},
        {"target": "isaiah", "why": "John 12:41 says Isaiah 'saw his glory and spoke of him' — identifying the figure on the throne in Isa 6 as the pre-incarnate Christ"},
    ],
    "what_it_doesnt_say": [
        "No birth narrative — John goes further back than Bethlehem to 'before the world existed' (17:5)",
        "No Synoptic parables, no Sermon on the Mount, no exorcisms — John's Jesus teaches through signs and extended discourses",
        "No account of the institution of the Lord's Supper — replaced by the foot-washing (ch. 13)",
        "The 'beloved disciple' is never named — tradition says John, but the text deliberately withholds the identity",
    ],
    "unusual_characters": [
        {"name": "Nicodemus", "ref": "3:1", "detail": "Pharisee who comes at NIGHT — moves from darkness to light across the Gospel (3:1, 7:50, 19:39). A secret disciple's slow emergence.", "connections": []},
        {"name": "The Samaritan woman", "ref": "4:7", "detail": "Longest one-on-one conversation in the Gospels. Jesus crosses every boundary: gender, ethnic, religious, moral. She becomes an evangelist.", "connections": []},
        {"name": "Lazarus", "ref": "11:1", "detail": "Raised after four days — specifically to counter the Jewish belief that the soul lingered three days. This is unmistakable resurrection.", "connections": []},
        {"name": "Thomas", "ref": "20:24-29", "detail": "'My Lord and my God' — the highest Christological confession in any Gospel, from the biggest doubter. John's theological climax.", "connections": []},
    ],
    "patterns": [
        "Seven signs (water to wine, healing official's son, pool of Bethesda, feeding 5000, walking on water, blind man healed, Lazarus raised) — each reveals a dimension of Jesus' divine identity",
        "Seven 'I AM' statements with predicates (bread, light, door, shepherd, resurrection, way, vine) plus the absolute 'I AM' (8:58) — eight total, echoing creation's eighth day (resurrection)",
        "Light vs. darkness motif runs from Prologue (1:5) through Nicodemus at night (3:2) to Judas going out 'and it was night' (13:30) to Easter morning dawn (20:1)",
        "Replacement theology: Jesus replaces every Jewish institution — temple, manna, water ceremony, light ceremony, Passover — as the reality behind the shadows",
    ],
    "mistranslations": [
        {"english": "only begotten", "original": "monogenes", "issue": "Implies biological generation; the Greek means 'one of a kind/unique' — not about origin but about uniqueness"},
        {"english": "Comforter", "original": "parakletos", "issue": "Sounds passive and emotional; the Greek is a legal advocate — a defense attorney in the divine court"},
        {"english": "Word", "original": "logos", "issue": "English 'word' sounds like mere speech; logos carries the weight of divine reason, creative agency, and personal intermediary"},
    ],
}

STRUCTURED['acts'] = {
    "key_claim": "Pentecost is the reversal of Babel and the Deut 32:8 allotment — the Spirit falls, every nation hears in their own language, and the nations assigned to lesser elohim are reclaimed for YHWH through the ekklesia.",
    "contested_words": [
        {"word": "glossa", "greek": "\u03b3\u03bb\u1ff6\u03c3\u03c3\u03b1", "issue": "'Tongues' — at Pentecost, known languages (2:6-11). At Corinth, unknown speech needing interpretation (1 Cor 14). Same word, different phenomena.", "severity": "CRITICAL"},
        {"word": "ethnos", "greek": "\u1f14\u03b8\u03bd\u03bf\u03c2", "issue": "'Nations/Gentiles' — Paul's mission is to reclaim the ethne allotted to corrupt elohim at Deut 32:8. Every conversion is cosmic territory recaptured.", "severity": "CRITICAL"},
        {"word": "horothesia", "greek": "\u1f41\u03c1\u03bf\u03b8\u03b5\u03c3\u03af\u03b1", "issue": "'Boundaries' (17:26) — God 'determined allotted periods and boundaries of their dwelling.' Paul at the Areopagus reveals the PURPOSE behind the Deut 32:8 allotment.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "deuteronomy", "why": "Pentecost reverses Deut 32:8 — the nations divided among lesser elohim are reunited under YHWH through the Spirit"},
        {"target": "genesis", "why": "Babel scattered languages (Gen 11); Pentecost reunites them. The table of nations (Gen 10) becomes the mission field of Acts"},
        {"target": "luke", "why": "Acts is volume 2 of Luke-Acts — the Spirit who empowered Jesus in Luke now empowers the ekklesia in Acts"},
        {"target": "joel", "why": "Peter's Pentecost sermon quotes Joel 2:28-32 — 'I will pour out my Spirit on ALL flesh.' The Spirit is no longer restricted to prophets, priests, and kings"},
        {"target": "daniel", "why": "The territorial prince concept (Dan 10) explains why Paul encounters spiritual resistance in specific regions — each territory has a ruling power"},
    ],
    "what_it_doesnt_say": [
        "Never records the deaths of Paul or Peter — Acts ends abruptly with Paul under house arrest in Rome",
        "No mention of what happened to most of the Twelve after Pentecost — only Peter and John get narrative attention",
        "Never explains why the Spirit falls differently each time — sometimes with tongues, sometimes without, sometimes with laying on of hands",
        "The Jerusalem Council (ch. 15) never addresses the divine council theology behind the Gentile mission — the cosmic framework is assumed, not stated",
    ],
    "unusual_characters": [
        {"name": "Stephen", "ref": "7:55-56", "detail": "Sees 'the Son of Man STANDING at the right hand of God' — the only time Jesus is described standing, not sitting. Rising to receive the first martyr.", "connections": ["daniel"]},
        {"name": "The Ethiopian eunuch", "ref": "8:27", "detail": "A Gentile, a eunuch (excluded from the assembly in Deut 23:1), reading Isaiah 53 — every barrier broken by the gospel.", "connections": ["isaiah"]},
        {"name": "Cornelius", "ref": "10:1", "detail": "Roman centurion — the Gentile Pentecost. The Spirit falls on uncircumcised pagans before baptism, shattering every category.", "connections": ["romans"]},
    ],
    "patterns": [
        "Geographical expansion fulfills 1:8 exactly: Jerusalem (chs. 1-7), Judea and Samaria (chs. 8-12), ends of the earth (chs. 13-28)",
        "Three conversion accounts of Paul (chs. 9, 22, 26) — each retelling emphasizes different theological aspects for different audiences",
        "The Spirit drives every major advance: Pentecost, Samaritan mission, Cornelius, Antioch sending, Macedonian call — human planning follows divine initiative",
        "Trial scenes parallel Jesus' trials: Stephen before the Sanhedrin, Paul before Jewish courts, Roman governors, and kings — the pattern of witness through suffering",
    ],
    "mistranslations": [
        {"english": "church", "original": "ekklesia", "issue": "Every occurrence in Acts should read 'assembly' or 'governing body' — the early movement was a counter-imperial governing structure, not a religious institution"},
        {"english": "Gentiles", "original": "ethne", "issue": "Hides the cosmic dimension — these are the 'nations' allotted to corrupt elohim at Babel, now being reclaimed"},
        {"english": "tongues", "original": "glossa", "issue": "Makes Pentecost sound like ecstatic gibberish when Acts 2 specifies known languages — every nation hearing in their own tongue"},
    ],
}

STRUCTURED['romans'] = {
    "key_claim": "Romans reveals the cosmic scope of the gospel: God 'gave them over' (1:24, 26, 28) echoes the Deut 32:8 allotment, creation itself groans under bondage (8:20-22), and the ekklesia will crush Satan underfoot (16:20) — fulfilling Gen 3:15 through Christ's body.",
    "contested_words": [
        {"word": "hilasterion", "greek": "\u1f31\u03bb\u03b1\u03c3\u03c4\u03ae\u03c1\u03b9\u03bf\u03bd", "issue": "'Propitiation/mercy seat' (3:25) — the kapporet, the lid of the Ark where blood was sprinkled on Yom Kippur. Christ IS the mercy seat. Connects to Lev 16 and kaphar.", "severity": "CRITICAL"},
        {"word": "paredoken", "greek": "\u03c0\u03b1\u03c1\u03ad\u03b4\u03c9\u03ba\u03b5\u03bd", "issue": "'Gave over' (1:24, 26, 28) — three-fold giving over of the nations. This IS the Deut 32:8 allotment described from Paul's perspective.", "severity": "CRITICAL"},
        {"word": "stoicheia", "greek": "\u03c3\u03c4\u03bf\u03b9\u03c7\u03b5\u1fd6\u03b1", "issue": "'Elementary principles' or 'elemental spirits'? These are the spiritual powers behind the cosmos — the allotted rulers of the Deut 32 framework.", "severity": "MAJOR"},
        {"word": "hyper", "greek": "\u1f51\u03c0\u03ad\u03c1", "issue": "Rom 8:31 'God is FOR us' — hyper means more than support; it means 'on behalf of' in a legal/covenantal sense. Divine council advocacy.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "Adam-Christ typology (5:12-21) is the most systematic treatment of Gen 3:15 — one man's trespass, one man's obedience. Rom 16:20 ('crush Satan under your feet') directly echoes Gen 3:15"},
        {"target": "deuteronomy", "why": "The three-fold 'gave them over' (1:24, 26, 28) echoes the Deut 32:8 allotment — God handed the nations to corrupt spiritual powers"},
        {"target": "leviticus", "why": "hilasterion (3:25) = the mercy seat of Lev 16 — Christ IS the kapporet where atonement blood is sprinkled"},
        {"target": "psalms", "why": "Rom 3:10-18 strings together Ps 14, 5, 140, 10, 36, Isa 59 — a divine prosecution case using Scripture as evidence"},
        {"target": "habakkuk", "why": "'The righteous shall live by faith' (1:17) quotes Hab 2:4 — the thesis statement of the entire letter"},
        {"target": "galatians", "why": "Abraham's faith-righteousness (Rom 4, Gen 15:6) parallels Galatians 3 — justification by faith precedes the Law by 430 years"},
    ],
    "what_it_doesnt_say": [
        "Never uses the word 'Trinity' — yet Rom 8 has Father, Son, and Spirit all working distinctly in the same passage",
        "The 'powers and principalities' of 8:38 are listed without explanation — Paul assumes his audience knows the spiritual hierarchy",
        "Chapters 9-11 (Israel's future) never resolve cleanly — 'all Israel will be saved' (11:26) remains one of the most debated verses in Scripture",
        "Rom 16:20 ('crush Satan under YOUR feet') transfers Gen 3:15 to the ekklesia without explaining the mechanism",
    ],
    "unusual_characters": [
        {"name": "Phoebe", "ref": "16:1", "detail": "Called diakonos (deacon/minister — same word used for Paul) and prostatis (patron/benefactor). She likely carried and read the letter to the Roman assemblies.", "connections": []},
        {"name": "Junia", "ref": "16:7", "detail": "'Outstanding among the apostles' — a woman apostle. Later manuscripts changed the name to masculine 'Junias' but no male name 'Junias' exists in ancient sources.", "connections": []},
        {"name": "Adam", "ref": "5:14", "detail": "Called 'a type of the one to come' — the first explicit typological framework. Adam's failure is the template Christ reverses.", "connections": ["genesis", "1corinthians"]},
    ],
    "patterns": [
        "Courtroom structure: indictment (1:18-3:20), verdict of grace (3:21-5:21), new life (6-8), Israel's case (9-11), life in the Spirit (12-16)",
        "Three-fold 'gave them over' (1:24, 26, 28) — escalating divine judgment that mirrors the Deut 32:8 allotment",
        "The 'therefore' chain: 3:20, 5:1, 8:1, 12:1 — each 'therefore' introduces the next phase of the argument. 'Therefore' in 12:1 pivots from theology to practice",
        "Rom 8 forms an inclusio with Gen 3: creation subjected to futility (8:20) will be liberated (8:21) — the cosmic curse reversed",
    ],
    "mistranslations": [
        {"english": "propitiation", "original": "hilasterion", "issue": "Abstract theological term hides the concrete image — the mercy seat where blood was sprinkled. Christ IS the furniture of the Holy of Holies"},
        {"english": "gave them up", "original": "paredoken", "issue": "Sounds like abandonment; the Greek is a judicial handing-over — a divine council act of consigning nations to their chosen gods"},
        {"english": "elementary principles", "original": "stoicheia", "issue": "Makes it sound like ABCs when Paul may mean the spiritual powers governing the cosmos — personal beings, not abstract concepts"},
    ],
}

STRUCTURED['1corinthians'] = {
    "key_claim": "The 'rulers of this age' who crucified Christ (2:8) are spiritual powers — archontes — who failed to understand the hidden wisdom of God, and the ekklesia is destined to judge angels (6:3), exercising authority over the very beings that rule the nations.",
    "contested_words": [
        {"word": "archontes", "greek": "\u1f04\u03c1\u03c7\u03bf\u03bd\u03c4\u03b5\u03c2", "issue": "'Rulers of this age' (2:8) — human rulers or spiritual powers? The context ('none of them understood' the hidden wisdom) points to cosmic powers who orchestrated the cross without grasping its meaning.", "severity": "CRITICAL"},
        {"word": "teleios", "greek": "\u03c4\u03ad\u03bb\u03b5\u03b9\u03bf\u03c2", "issue": "'Perfect/complete' (13:10) — 'when the perfect comes.' Cessationists say = completed canon. But teleios means 'mature/complete' and 1 Cor 13:12 explains it as seeing 'face to face' = Christ's return.", "severity": "CRITICAL"},
        {"word": "soma", "greek": "\u03c3\u1ff6\u03bc\u03b1", "issue": "'Body' — Paul's body metaphor for the ekklesia (ch. 12) is not a mere illustration but an ontological claim about corporate identity in Christ.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "exodus", "why": "'Christ our Passover lamb has been sacrificed' (5:7) — direct identification of Jesus with the Exodus 12 lamb. Passover typology fulfilled"},
        {"target": "genesis", "why": "Adam-Christ contrast continues: 'the first Adam became a living being; the last Adam became a life-giving spirit' (15:45) — Gen 2:7 reinterpreted"},
        {"target": "daniel", "why": "The resurrection body discussion (ch. 15) connects to Dan 12:2-3 — those raised 'shall shine like the stars,' a divine council image"},
        {"target": "psalms", "why": "'He must reign until he has put all enemies under his feet' (15:25) quotes Ps 110:1 — the enthroned Son subduing all powers"},
        {"target": "numbers", "why": "Israel's wilderness failures are 'examples for us' (10:6, 11) — Paul reads Numbers typologically"},
    ],
    "what_it_doesnt_say": [
        "Never defines who the 'rulers of this age' are — spiritual or political? Paul leaves the ambiguity as a test of worldview",
        "'We shall judge angels' (6:3) is stated without any explanation of how, when, or which angels",
        "The nature of 'tongues of angels' (13:1) is never explained — are these actual angelic languages?",
        "No timeline given for 'when the perfect comes' (13:10) — the debate between Christ's return and the completed canon remains unresolved in the text itself",
    ],
    "unusual_characters": [
        {"name": "The man delivered to Satan", "ref": "5:5", "detail": "'Deliver this man to Satan for the destruction of the flesh, that his spirit may be saved.' Paul uses divine council authority to hand someone to the adversary — same framework as Job 1-2.", "connections": ["job", "1timothy"]},
        {"name": "Chloe's people", "ref": "1:11", "detail": "A woman's household reports the church divisions — a woman is Paul's intelligence network in Corinth.", "connections": []},
    ],
    "patterns": [
        "Already/not yet tension: 'you were washed, sanctified, justified' (6:11) past tense, yet 'we shall be changed' (15:52) future — inaugurated eschatology",
        "Wisdom reversal: God chose the foolish to shame the wise (1:27) — the cross inverts every human power hierarchy",
        "Body metaphor: individual body (ch. 6, sexual ethics), corporate body (ch. 12, spiritual gifts), resurrection body (ch. 15) — three dimensions of soma",
        "Each problem Paul addresses traces back to a worldview failure — Corinth's issues are theological, not merely behavioral",
    ],
    "mistranslations": [
        {"english": "rulers", "original": "archontes", "issue": "Could mean human rulers or spiritual powers — most translations default to 'rulers' without flagging the spiritual dimension"},
        {"english": "perfect", "original": "teleios", "issue": "'Perfect' in English implies flawless; the Greek means 'mature/complete/arrived at telos' — the cessationism debate hangs on this one word"},
        {"english": "charity", "original": "agape", "issue": "KJV's 'charity' reduces divine self-giving love to human generosity — agape is covenant faithfulness in action"},
    ],
}

STRUCTURED['2corinthians'] = {
    "key_claim": "Paul identifies Satan as 'the god of this age' (4:4) who blinds minds — a direct reference to the Deut 32:8 territorial deity framework — and Paul himself has been caught up to 'the third heaven' (12:2), gaining divine council access.",
    "contested_words": [
        {"word": "ho theos tou aionos", "greek": "\u1f41 \u03b8\u03b5\u1f78\u03c2 \u03c4\u03bf\u1fe6 \u03b1\u1f30\u1ff6\u03bd\u03bf\u03c2", "issue": "'The god of this age' (4:4) — Satan called 'god' (theos). This is Deut 32:8 language: a spiritual being ruling over territory with divine authority.", "severity": "CRITICAL"},
        {"word": "tritos ouranos", "greek": "\u03c4\u03c1\u03af\u03c4\u03bf\u03c2 \u03bf\u1f50\u03c1\u03b1\u03bd\u03cc\u03c2", "issue": "'Third heaven' (12:2) — cosmological layers: atmosphere, stars, God's throne. Paul claims divine council access — he has been to the throne room.", "severity": "CRITICAL"},
        {"word": "metamorphoo", "greek": "\u03bc\u03b5\u03c4\u03b1\u03bc\u03bf\u03c1\u03c6\u03cc\u03c9", "issue": "'Transformed' (3:18) — same word used for the Transfiguration. Believers are being metamorphosed into the image of Christ progressively.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "deuteronomy", "why": "'The god of this age' (4:4) is a Deut 32:8 territorial deity — Satan as one of the allotted elohim who corrupted his assignment"},
        {"target": "job", "why": "Paul's 'thorn in the flesh, a messenger of Satan' (12:7) mirrors Job's framework — satanic affliction permitted by God for divine purposes"},
        {"target": "exodus", "why": "Moses' veiled face (3:13-16) reinterpreted — the veil hides the fading glory of the old covenant. Christ removes it"},
        {"target": "genesis", "why": "'God who said let light shine out of darkness' (4:6) — new creation language echoing Gen 1:3. The gospel is re-creation"},
        {"target": "isaiah", "why": "'Behold, now is the day of salvation' (6:2) quotes Isa 49:8 — the servant's mission becomes the present reality"},
    ],
    "what_it_doesnt_say": [
        "The 'third heaven' experience (12:2-4) — Paul heard 'things that cannot be told, which man may not utter.' What did he hear?",
        "The 'thorn in the flesh' (12:7) is never identified — physical ailment, spiritual opposition, or something else?",
        "Paul mentions 'super-apostles' (11:5) but never names them — who were his opponents in Corinth?",
        "The nature of the 'treasure in jars of clay' (4:7) is cosmic power in human weakness, but the mechanism is never explained",
    ],
    "unusual_characters": [
        {"name": "The god of this age", "ref": "4:4", "detail": "Satan given the title theos (god) — a divine being ruling a territorial domain, not merely a tempter. Deut 32:8 framework in Paul's own words.", "connections": ["deuteronomy", "ephesians"]},
        {"name": "Paul's thorn messenger", "ref": "12:7", "detail": "A 'messenger of Satan' (angelos satana) — a spirit being dispatched by the adversary, permitted by God to keep Paul humble.", "connections": ["job"]},
    ],
    "patterns": [
        "Weakness-power paradox: 'when I am weak, then I am strong' (12:10) — divine power operates through human vulnerability, not despite it",
        "New creation language: 'if anyone is in Christ, new creation' (5:17) — the gospel is not reformation but RE-creation, echoing Genesis 1",
        "Ministry of the Spirit vs. ministry of death (ch. 3): old covenant → glory that fades; new covenant → glory that increases. Progressive transformation",
        "Fool's speech (chs. 11-12): Paul inverts boasting — instead of achievements, he boasts of sufferings, weaknesses, and divine encounters",
    ],
    "mistranslations": [
        {"english": "god of this world", "original": "ho theos tou aionos", "issue": "'World' obscures 'age' (aion) — Satan rules a temporal domain, not just a geographical one. His authority has an expiration date"},
        {"english": "caught up", "original": "harpazo", "issue": "Sounds passive; the Greek implies violent seizure — Paul was snatched up to heaven, not gently transported"},
        {"english": "transformed", "original": "metamorphoo", "issue": "English 'transformed' is too vague — this is metamorphosis, the same word for Christ's transfiguration"},
    ],
}

STRUCTURED['galatians'] = {
    "key_claim": "Paul argues that the 'seed' (sperma) promised to Abraham is SINGULAR — 'referring to one, who is Christ' (3:16) — proving Gen 3:15's zera is fulfilled in one person, and before Christ humanity was enslaved to the stoicheia tou kosmou, the elemental spiritual powers governing the nations.",
    "contested_words": [
        {"word": "sperma", "greek": "\u03c3\u03c0\u03ad\u03c1\u03bc\u03b1", "issue": "'Seed' (3:16) — Paul makes the singular-vs-plural argument central. Gen 3:15's zera and Gen 12:7's seed are SINGULAR = Christ. The entire Bible narrows to one person.", "severity": "CRITICAL"},
        {"word": "stoicheia tou kosmou", "greek": "\u03c3\u03c4\u03bf\u03b9\u03c7\u03b5\u1fd6\u03b1 \u03c4\u03bf\u1fe6 \u03ba\u03cc\u03c3\u03bc\u03bf\u03c5", "issue": "'Elementary principles of the world' or 'elemental spirits of the cosmos'? (4:3, 9). Before Christ, humanity was enslaved to spiritual powers — the allotted elohim.", "severity": "CRITICAL"},
        {"word": "diatageis di angelon", "greek": "\u03b4\u03b9\u03b1\u03c4\u03b1\u03b3\u03b5\u1f76\u03c2 \u03b4\u03b9\u2019 \u1f00\u03b3\u03b3\u03ad\u03bb\u03c9\u03bd", "issue": "Law 'ordained through angels' (3:19) — the Torah was mediated by divine council beings. Confirmed by Acts 7:53 and Heb 2:2.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "The seed promise (Gen 3:15, 12:7) is Paul's central argument — sperma is singular, pointing to Christ alone"},
        {"target": "deuteronomy", "why": "The stoicheia enslavement parallels the Deut 32:8 allotment — before Christ, nations were under the authority of allotted spiritual powers"},
        {"target": "romans", "why": "Abraham's faith-righteousness (Gal 3:6, Gen 15:6) parallels Rom 4 — justification by faith precedes the Law by 430 years"},
        {"target": "colossians", "why": "stoicheia tou kosmou appears in both Gal 4:3 and Col 2:8, 20 — Paul's consistent framework of spiritual powers behind earthly systems"},
        {"target": "acts", "why": "Gal 2 records the Jerusalem Council from Paul's perspective — the Gentile mission's theological foundation"},
    ],
    "what_it_doesnt_say": [
        "Never explains WHO the stoicheia are — personal beings or impersonal forces? Paul's other letters suggest personal powers",
        "How angels 'ordained' the Law (3:19) is never detailed — what role did divine council beings play at Sinai?",
        "'Neither male nor female in Christ' (3:28) — Paul never works out the social implications in this letter",
        "The 'Jerusalem above is our mother' (4:26) is introduced without explanation of the heavenly Jerusalem concept",
    ],
    "unusual_characters": [
        {"name": "Abraham", "ref": "3:6-9", "detail": "Paul's primary example: justified by faith 430 years BEFORE the Law existed. If Abraham was righteous without Torah, Torah cannot be the path to righteousness.", "connections": ["genesis", "romans", "hebrews"]},
        {"name": "Hagar and Sarah", "ref": "4:21-31", "detail": "Allegorized as two covenants: Sinai (slavery) vs. promise (freedom). Bold reinterpretation of Gen 16-21.", "connections": ["genesis"]},
    ],
    "patterns": [
        "Before/after Christ structure: enslaved to stoicheia (4:3) → 'when the fullness of time came' (4:4) → adopted as sons (4:5). The turning point is incarnation",
        "Freedom-slavery binary: the entire letter oscillates between freedom in Christ and slavery to law/flesh/powers",
        "Autobiography as theology: Paul's conversion (chs. 1-2) is not memoir but evidence that the gospel comes from revelation, not human tradition",
        "Fruit vs. works contrast (5:19-23): 'works of the flesh' (human striving) vs. 'fruit of the Spirit' (divine production) — singular 'fruit,' one organic reality",
    ],
    "mistranslations": [
        {"english": "elementary principles", "original": "stoicheia tou kosmou", "issue": "Makes enslaving cosmic powers sound like ABCs — hides the spiritual warfare dimension of pre-Christian existence"},
        {"english": "seed", "original": "sperma", "issue": "Modern readers miss Paul's singular-plural argument — the English 'seed' can be either, but Paul's whole argument rests on the singular"},
        {"english": "ordained by angels", "original": "diatageis di angelon", "issue": "Often footnoted rather than translated — the angelic mediation of Torah is theologically explosive and usually suppressed"},
    ],
}

STRUCTURED['ephesians'] = {
    "key_claim": "Through the ekklesia, the manifold wisdom of God is made known to the rulers and authorities in heavenly places (3:10) — the governing assembly of believers TEACHES the divine council, and the battle is not against flesh and blood but against cosmic powers in the heavenlies (6:12).",
    "contested_words": [
        {"word": "ta epourania", "greek": "\u03c4\u1f70 \u1f10\u03c0\u03bf\u03c5\u03c1\u03ac\u03bd\u03b9\u03b1", "issue": "'Heavenly places' — appears 5 times in Ephesians (1:3, 20; 2:6; 3:10; 6:12). The spiritual realm where Christ is enthroned AND where hostile powers operate. Same space, contested territory.", "severity": "CRITICAL"},
        {"word": "kosmokratores", "greek": "\u03ba\u03bf\u03c3\u03bc\u03bf\u03ba\u03c1\u03ac\u03c4\u03bf\u03c1\u03b5\u03c2", "issue": "'Cosmic powers/world rulers' (6:12) — a term used in astrology for planetary deities ruling earthly affairs. Paul co-opts pagan language to describe real spiritual enemies.", "severity": "CRITICAL"},
        {"word": "mysterion", "greek": "\u03bc\u03c5\u03c3\u03c4\u03ae\u03c1\u03b9\u03bf\u03bd", "issue": "'Mystery' (3:3-6) — not a puzzle to solve but a hidden plan now revealed: Gentiles are co-heirs. The Deut 32:8 allotment is being reversed.", "severity": "MAJOR"},
        {"word": "panoplia", "greek": "\u03c0\u03b1\u03bd\u03bf\u03c0\u03bb\u03af\u03b1", "issue": "'Full armor' (6:11) — complete Roman military kit. Each piece maps to a spiritual reality. The battle is real and requires real equipment.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "deuteronomy", "why": "The Gentile inclusion (2:11-22) reverses the Deut 32:8 allotment — the dividing wall between Jew and Gentile is demolished because the cosmic partition is abolished"},
        {"target": "daniel", "why": "The 'rulers and authorities in heavenly places' (3:10, 6:12) are the territorial princes of Dan 10 — the ekklesia now confronts them with God's wisdom"},
        {"target": "genesis", "why": "'Predestined before the foundation of the world' (1:4) — God's plan precedes creation, precedes the Fall, precedes the allotment"},
        {"target": "colossians", "why": "Ephesians and Colossians are sister letters — Col 2:15 (disarming powers at the cross) is the victory; Eph 6:12 is the ongoing enforcement"},
        {"target": "isaiah", "why": "The armor of God (6:14-17) draws from Isa 59:17 where YHWH himself puts on armor — believers wear GOD's own battle gear"},
    ],
    "what_it_doesnt_say": [
        "HOW the ekklesia makes known God's wisdom to cosmic powers (3:10) is never explained — by its existence? Its worship? Its proclamation?",
        "The 'mystery of Christ' (3:4) was 'not made known to sons of men in other generations' — who ARE the 'sons of men' here? Humans or divine beings?",
        "'He descended into the lower regions of the earth' (4:9) — Sheol, the grave, or earth itself? The descent is never clarified",
        "The armor passage (6:10-20) assumes the battle is already happening but never says who initiates the attacks or how they manifest",
    ],
    "unusual_characters": [
        {"name": "The kosmokratores", "ref": "6:12", "detail": "'World rulers of this darkness' — astral powers governing earthly territories. The most explicit naming of the spiritual hierarchy in Paul's letters.", "connections": ["daniel", "deuteronomy", "colossians"]},
        {"name": "The 'one new man'", "ref": "2:15", "detail": "Jew and Gentile fused into a single new humanity in Christ — not Gentiles becoming Jewish or Jews becoming Gentile, but a third category entirely.", "connections": ["galatians"]},
    ],
    "patterns": [
        "Heavenly places (ta epourania) as contested space: believers seated there (2:6), Christ enthroned there (1:20), hostile powers there (3:10, 6:12) — one realm, multiple occupants",
        "Prayer → power → cosmic purpose: the prayer of 1:17-23 leads to resurrection power leads to cosmic authority. Paul's prayers are not personal comfort but cosmic commission",
        "The body metaphor matures: from individual gifts (1 Cor 12) to cosmic entity making God's wisdom known to spiritual powers (3:10) — the ekklesia has a supernatural audience",
        "Walk language: 'walk worthy' (4:1), 'no longer walk as Gentiles' (4:17), 'walk in love' (5:2), 'walk as children of light' (5:8), 'walk carefully' (5:15) — progressive transformation",
    ],
    "mistranslations": [
        {"english": "heavenly realms", "original": "ta epourania", "issue": "Sounds like a distant afterlife destination; Paul means the present spiritual dimension where cosmic powers operate and believers are already seated with Christ"},
        {"english": "rulers of darkness", "original": "kosmokratores tou skotous", "issue": "'World rulers' is too tame — kosmokratores implies governing authority over the entire cosmos, not just 'dark rulers'"},
        {"english": "struggle", "original": "pale", "issue": "'Struggle' softens what is literally hand-to-hand wrestling — the spiritual battle is close combat, not distant warfare"},
    ],
}

STRUCTURED['philippians'] = {
    "key_claim": "The Christ Hymn (2:5-11) declares that Jesus existed 'in the form of God' (morphe theou), emptied himself, and is now exalted so that every knee bows in three realms — heaven (the divine council), earth (humanity), and under the earth (imprisoned spirits).",
    "contested_words": [
        {"word": "morphe theou", "greek": "\u03bc\u03bf\u03c1\u03c6\u1f74 \u03b8\u03b5\u03bf\u1fe6", "issue": "'Form of God' (2:6) — morphe = essential nature, not mere appearance. Christ possessed the divine nature before incarnation. NOT a lesser being promoted.", "severity": "CRITICAL"},
        {"word": "kenoo", "greek": "\u03ba\u03b5\u03bd\u03cc\u03c9", "issue": "'Emptied himself' (2:7) — kenosis. What did he empty? Not divinity itself but the privileges and prerogatives of divine status. He did not cease to be God but ceased to live as God.", "severity": "CRITICAL"},
        {"word": "harpagmos", "greek": "\u1f01\u03c1\u03c0\u03b1\u03b3\u03bc\u03cc\u03c2", "issue": "'Something to be grasped' (2:6) — did not consider equality with God something to exploit/cling to. Contrasts with Adam who DID grasp at being 'like God' (Gen 3:5).", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "The Christ Hymn reverses Adam's grasping: Adam reached for equality with God (Gen 3:5); Christ, already possessing it, emptied himself — the anti-Adam"},
        {"target": "isaiah", "why": "'Every knee shall bow' (2:10) quotes Isa 45:23 — a passage about YHWH alone. Paul applies YHWH's exclusive prerogative to Jesus"},
        {"target": "1peter", "why": "Three realms bow: heaven, earth, under the earth — the imprisoned spirits of 1 Pet 3:19 are forced to acknowledge Christ's lordship"},
        {"target": "revelation", "why": "The universal acclamation 'Jesus Christ is Lord' (2:11) prefigures Rev 5:13 — every creature in every realm confessing"},
        {"target": "colossians", "why": "Col 1:15-20 (Christ hymn) parallels Phil 2:5-11 — both pre-existence, both cosmic scope, both exaltation after humiliation"},
    ],
    "what_it_doesnt_say": [
        "WHAT Jesus emptied himself of is never specified — divinity? Glory? Power? The text says morphe doulou (form of a servant) but not what was relinquished",
        "The three-realm acclamation (heaven, earth, under earth) never explains who 'under the earth' includes — imprisoned Watchers? Dead humans? Both?",
        "Why Philippi specifically receives this christological hymn — was there a specific heresy or situation prompting it?",
    ],
    "unusual_characters": [
        {"name": "Epaphroditus", "ref": "2:25-30", "detail": "Nearly died serving Paul. Called 'fellow soldier' (systratiotes) — military language for the spiritual battle.", "connections": []},
        {"name": "Euodia and Syntyche", "ref": "4:2-3", "detail": "Two women leaders 'who have labored side by side with me in the gospel' — Paul names women as co-workers in the cosmic mission.", "connections": []},
    ],
    "patterns": [
        "Kenosis pattern: divine status → voluntary humiliation → exaltation above all. The same pattern shapes Christian ethics: 'have this mind among yourselves' (2:5)",
        "Joy in suffering: Paul writes from prison yet 'joy/rejoice' appears 16 times — suffering and joy are not opposites but companions in the cosmic mission",
        "Three-realm cosmology: heaven, earth, under earth (2:10) — the entire created order, visible and invisible, acknowledges Christ. No territory exempt",
    ],
    "mistranslations": [
        {"english": "being in the form of God", "original": "en morphe theou hyparchon", "issue": "'Being' sounds static; the Greek participle hyparchon means 'existing as/continuously being' — Christ's divinity is ontological and ongoing, not a phase"},
        {"english": "made himself nothing", "original": "heauton ekenosen", "issue": "NIV's 'made himself nothing' goes too far — 'emptied himself' preserves the mystery of what was and wasn't relinquished"},
        {"english": "every knee should bow", "original": "pan gony kampse", "issue": "'Should' implies optional; the Greek is future indicative — every knee WILL bow, without exception"},
    ],
}

STRUCTURED['colossians'] = {
    "key_claim": "Christ created the entire spiritual hierarchy — thrones, dominions, rulers, authorities (1:16) — and then disarmed them at the cross, making a public spectacle of them in triumphal procession (2:15). The Creator defeated his own creation's rebellion.",
    "contested_words": [
        {"word": "thronoi, kyriotetes, archai, exousiai", "greek": "\u03b8\u03c1\u03cc\u03bd\u03bf\u03b9, \u03ba\u03c5\u03c1\u03b9\u03cc\u03c4\u03b7\u03c4\u03b5\u03c2, \u1f00\u03c1\u03c7\u03b1\u03af, \u1f10\u03be\u03bf\u03c5\u03c3\u03af\u03b1\u03b9", "issue": "Four ranks of spiritual powers (1:16) — the most detailed hierarchy in Paul. Created BY Christ, created FOR Christ. Their rebellion does not cancel their origin.", "severity": "CRITICAL"},
        {"word": "apekdysamenos", "greek": "\u1f00\u03c0\u03b5\u03ba\u03b4\u03c5\u03c3\u03ac\u03bc\u03b5\u03bd\u03bf\u03c2", "issue": "'Disarmed/stripped' (2:15) — middle voice: Christ himself stripped the powers. Like a victorious general stripping armor from defeated enemies in a Roman triumph.", "severity": "CRITICAL"},
        {"word": "stoicheia tou kosmou", "greek": "\u03c3\u03c4\u03bf\u03b9\u03c7\u03b5\u1fd6\u03b1 \u03c4\u03bf\u1fe6 \u03ba\u03cc\u03c3\u03bc\u03bf\u03c5", "issue": "'Elemental spirits of the world' (2:8, 20) — same as Gal 4:3. The spiritual powers behind human religion and philosophy. You died WITH Christ to their authority.", "severity": "CRITICAL"},
    ],
    "hidden_connections": [
        {"target": "ephesians", "why": "Sister letter: Col 2:15 (disarming powers at the cross) provides the VICTORY; Eph 6:12 describes the ongoing ENFORCEMENT of that victory"},
        {"target": "genesis", "why": "'Firstborn of all creation' (1:15) echoes Gen 1 — Christ is not the first creature but the one who holds primacy over all creation, as creator"},
        {"target": "philippians", "why": "Col 1:15-20 and Phil 2:5-11 are parallel Christ hymns: pre-existence, creative agency, cosmic supremacy, exaltation"},
        {"target": "galatians", "why": "stoicheia tou kosmou appears in both — the enslaving powers are the same whether addressed to Galatia or Colossae"},
        {"target": "hebrews", "why": "Christ as 'image of the invisible God' (1:15) connects to Heb 1:3 'exact imprint of his nature' — both establish divine Christology"},
    ],
    "what_it_doesnt_say": [
        "The four-tier hierarchy (thrones, dominions, rulers, authorities) is listed without explaining the differences between the ranks",
        "HOW Christ disarmed the powers at the cross is not explained — was it the act of dying? The resurrection? The descent?",
        "The 'Colossian heresy' Paul combats is never named — was it proto-Gnostic, Jewish mystical, or pagan? Scholars disagree",
        "'Worship of angels' (2:18) — were they worshipping angels or participating in angelic worship? The Greek is ambiguous",
    ],
    "unusual_characters": [
        {"name": "The cosmic Christ", "ref": "1:15-20", "detail": "Not merely a teacher or prophet but the creator and sustainer of all things visible and invisible — including the powers that oppose him.", "connections": ["john", "hebrews"]},
        {"name": "Onesimus", "ref": "4:9", "detail": "Called 'faithful and beloved brother, who is one of you' — the runaway slave of Philemon, now sent back as a brother in Christ.", "connections": ["philemon"]},
    ],
    "patterns": [
        "Christ hymn structure (1:15-20): two stanzas — Christ's role in creation (15-17) and Christ's role in redemption (18-20). Cosmic scope in both",
        "Died with / raised with: 'you died with Christ to the stoicheia' (2:20), 'you have been raised with Christ' (3:1) — the believer's position change is cosmic, not merely personal",
        "Put off / put on: old self (3:9) stripped off, new self (3:10) put on — the language of investiture, like a priest putting on garments for service",
    ],
    "mistranslations": [
        {"english": "powers and authorities", "original": "archai kai exousiai", "issue": "Generic English obscures the specific spiritual hierarchy — these are ranked beings with defined jurisdictions, not vague 'forces'"},
        {"english": "made a public spectacle", "original": "edeigmatisen en parrhesia", "issue": "The image is a Roman triumphal procession — conquered enemies paraded in chains. The cross is not defeat but a victory parade"},
        {"english": "basic principles", "original": "stoicheia tou kosmou", "issue": "Reduces enslaving cosmic spirits to 'elementary teachings' — hides the spiritual warfare dimension"},
    ],
}

STRUCTURED['1thessalonians'] = {
    "key_claim": "Christ's return involves the full apparatus of the divine council: 'the Lord himself will descend with a cry of command, with the voice of an archangel, and with the trumpet of God' (4:16) — and 'the man of lawlessness exalts himself against every so-called god' (2 Thess 2:4), an anti-council figure claiming supremacy over all spiritual powers.",
    "contested_words": [
        {"word": "parousia", "greek": "\u03c0\u03b1\u03c1\u03bf\u03c5\u03c3\u03af\u03b1", "issue": "'Coming' (4:15) — technical term for an emperor's official visit to a city. Citizens go OUT to meet him and escort him IN. Not 'rapture away' but 'welcoming the returning king.'", "severity": "CRITICAL"},
        {"word": "apantesis", "greek": "\u1f00\u03c0\u03ac\u03bd\u03c4\u03b7\u03c3\u03b9\u03c2", "issue": "'To meet' (4:17) — civic reception term: citizens going out to meet a dignitary and escorting him back to the city. Not departure but reception.", "severity": "CRITICAL"},
        {"word": "ho anomos", "greek": "\u1f41 \u1f04\u03bd\u03bf\u03bc\u03bf\u03c2", "issue": "'The lawless one' (2 Thess 2:3) — exalts himself above every 'so-called god or object of worship.' An anti-council figure claiming authority over all spiritual hierarchies.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "daniel", "why": "The 'man of lawlessness' exalting himself (2 Thess 2:4) echoes Dan 11:36 — the arrogant king who magnifies himself above every god"},
        {"target": "exodus", "why": "'The trumpet of God' (4:16) echoes the Sinai theophany (Ex 19:16) — Christ's return is a new Sinai, a new divine encounter"},
        {"target": "revelation", "why": "The parousia imagery (4:16-17) parallels Rev 19:11-16 — the returning King with heavenly armies"},
        {"target": "isaiah", "why": "'Peace and security, then sudden destruction' (5:3) echoes Isa 13:6-8 — the Day of the LORD as birth pains, sudden and inescapable"},
    ],
    "what_it_doesnt_say": [
        "Never uses the word 'rapture' — the concept of being 'caught up' (harpazo) is about meeting the returning King, not escaping earth",
        "The identity of 'the restrainer' (2 Thess 2:6-7) is never revealed — one of the biggest mysteries in the NT",
        "The timeline between the events of 4:16-17 is compressed — are these sequential moments or a single event?",
        "Paul never addresses what happens to those alive DURING the tribulation — only the dead and the living at the parousia",
    ],
    "unusual_characters": [
        {"name": "The archangel", "ref": "4:16", "detail": "An unnamed archangel whose voice accompanies the Lord's descent — divine council herald announcing the King's return.", "connections": ["daniel", "jude", "revelation"]},
        {"name": "The restrainer", "ref": "2 Thess 2:6-7", "detail": "'You know what restrains him now' — Paul's audience knew but we don't. The Holy Spirit? Rome? An angelic being? The mystery persists.", "connections": []},
    ],
    "patterns": [
        "Parousia as civic reception (apantesis): the imagery is citizens going OUT of the city to meet the returning emperor and escorting him IN — not escape but welcome",
        "Already/not yet: 'you turned from idols to serve the living God' (1:9) — past event; 'to wait for his Son from heaven' (1:10) — future hope. Both equally real",
        "Day vs. night imagery (5:1-11): believers are 'children of light/day,' not caught off guard — spiritual wakefulness as the posture of waiting",
    ],
    "mistranslations": [
        {"english": "caught up", "original": "harpazo", "issue": "Basis for 'rapture' theology — but the context is an apantesis (civic welcome), not an evacuation. Believers meet Christ to escort him to earth, not flee from it"},
        {"english": "coming", "original": "parousia", "issue": "Generic 'coming' hides the imperial-visit context — this is a king arriving to take possession of his territory"},
        {"english": "man of sin", "original": "ho anthropos tes anomias", "issue": "KJV 'man of sin' obscures 'man of lawlessness' — the figure is anti-Torah, anti-order, anti-council, not merely morally sinful"},
    ],
}

STRUCTURED['philemon'] = {
    "key_claim": "Philemon is the seed-line theme at its most personal — 'no longer as a slave but as a beloved brother' (v. 16) demonstrates that the gospel dismantles social hierarchies from the inside out, creating a new humanity where every distinction is abolished in Christ.",
    "contested_words": [
        {"word": "adelphos agapetos", "greek": "\u1f00\u03b4\u03b5\u03bb\u03c6\u1f78\u03c2 \u1f00\u03b3\u03b1\u03c0\u03b7\u03c4\u03cc\u03c2", "issue": "'Beloved brother' (v. 16) — Paul redefines Onesimus's social status using family language. Not reform of slavery but a new ontological category that makes slavery absurd.", "severity": "CRITICAL"},
        {"word": "oninemi", "greek": "\u1f40\u03bd\u03af\u03bd\u03b7\u03bc\u03b9", "issue": "'Benefit/refresh' (v. 20) — a wordplay on Onesimus's name (which means 'useful/beneficial'). Paul asks Philemon to live up to Onesimus's name by receiving him.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "galatians", "why": "'Neither slave nor free' (Gal 3:28) is enacted in concrete reality — Onesimus returns not as property but as family"},
        {"target": "colossians", "why": "Onesimus is mentioned in Col 4:9 as 'one of you' — sent with the Colossian letter. Philemon likely lived in Colossae"},
        {"target": "exodus", "why": "Deut 23:15-16 forbids returning a runaway slave — Paul's letter navigates between Roman law and Torah principle"},
    ],
    "what_it_doesnt_say": [
        "Never explicitly tells Philemon to free Onesimus — Paul hints, pressures, and shames, but never commands manumission",
        "What Onesimus did is never clarified — did he steal? Simply run away? The offense is unnamed",
        "Paul's 'charge it to me' (v. 18) — did Philemon actually collect? The outcome is never recorded",
    ],
    "unusual_characters": [
        {"name": "Onesimus", "ref": "v. 10", "detail": "A runaway slave whom Paul 'fathered' in prison. His name means 'useful' — Paul says he was formerly useless but now useful to both of them.", "connections": ["colossians"]},
        {"name": "Apphia", "ref": "v. 2", "detail": "Called 'our sister' — likely Philemon's wife. Named as a recipient of the letter, making the household decision communal, not just Philemon's.", "connections": []},
    ],
    "patterns": [
        "Persuasion structure: Paul moves from praise (vv. 4-7) to appeal (vv. 8-16) to offer (vv. 17-21) to pressure (v. 21 'knowing you will do even more') — masterful rhetoric",
        "Name theology: Onesimus ('useful') was 'useless' as a slave but 'useful' as a brother — identity is transformed by relationship to Christ, not social status",
        "The personal letter as theology: the shortest Pauline letter enacts the gospel in a single concrete situation — reconciliation, new identity, substitutionary payment",
    ],
    "mistranslations": [
        {"english": "slave", "original": "doulos", "issue": "Modern 'slave' carries chattel slavery connotations; Roman slavery was a complex spectrum. But Paul's point transcends the institution — brother abolishes the category"},
        {"english": "partner", "original": "koinonos", "issue": "Sounds like a business term; koinonos means 'one who shares in common' — Paul and Philemon share everything, including Onesimus's new identity"},
    ],
}

STRUCTURED['hebrews'] = {
    "key_claim": "Hebrews provides systematic proof that Christ is above every divine council member — quoting Ps 2:7, Deut 32:43 (DSS/LXX), Ps 45:6 ('Your throne, O God'), and Ps 8 — establishing a Melchizedekian priesthood older and superior to the Levitical order.",
    "contested_words": [
        {"word": "charakter tes hypostaseos", "greek": "\u03c7\u03b1\u03c1\u03b1\u03ba\u03c4\u1f74\u03c1 \u03c4\u1fc6\u03c2 \u1f51\u03c0\u03bf\u03c3\u03c4\u03ac\u03c3\u03b5\u03c9\u03c2", "issue": "'Exact imprint of his nature' (1:3) — charakter = stamp/die impression. The Son is not similar to God but the exact reproduction of the divine essence.", "severity": "CRITICAL"},
        {"word": "apaugasma", "greek": "\u1f00\u03c0\u03b1\u03cd\u03b3\u03b1\u03c3\u03bc\u03b1", "issue": "'Radiance' (1:3) — active radiance from a source, not reflected light. The Son actively shines forth God's glory, inseparable from the source.", "severity": "CRITICAL"},
        {"word": "kata ten taxin Melchisedek", "greek": "\u03ba\u03b1\u03c4\u1f70 \u03c4\u1f74\u03bd \u03c4\u03ac\u03be\u03b9\u03bd \u039c\u03b5\u03bb\u03c7\u03b9\u03c3\u03b5\u03b4\u03ad\u03ba", "issue": "'According to the order of Melchizedek' (5:6, 6:20, 7:17) — Jesus' priesthood is NOT Levitical. He is from Judah, not Levi (7:14). The Melchizedekian order is older, superior, eternal.", "severity": "CRITICAL"},
        {"word": "typos/skia", "greek": "\u03c4\u03cd\u03c0\u03bf\u03c2/\u03c3\u03ba\u03b9\u03ac", "issue": "'Copy and shadow' (8:5) — the earthly tabernacle is a replica of the heavenly original. Shadows are real but derivative. Christ ministers in the true tabernacle.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "Melchizedek (Gen 14:18) is the anchor: no genealogy, no beginning or end (Heb 7:3) — priest-king of Salem who prefigures Christ's eternal priesthood"},
        {"target": "psalms", "why": "Hebrews quotes Psalms more than any other OT book: Ps 2:7 (1:5), Ps 45:6 (1:8, 'Your throne, O God'), Ps 110:1, 4 (1:13, 5:6) — the divine council hymnbook as Christological proof"},
        {"target": "leviticus", "why": "The entire Day of Atonement (Lev 16) is reinterpreted: Christ enters the TRUE Holy of Holies with his own blood, once for all (9:11-12)"},
        {"target": "exodus", "why": "The tabernacle was built according to the heavenly 'pattern' (tavnit, Ex 25:40) — Heb 8:5 confirms it was a shadow of the real thing"},
        {"target": "deuteronomy", "why": "Heb 1:6 quotes Deut 32:43 (DSS/LXX): 'Let all God's angels worship him' — the divine council commanded to worship the Son"},
        {"target": "dss", "why": "11Q13 (Melchizedek Scroll) presents Melchizedek as a divine figure executing Ps 82 judgment — the Qumran community saw the same connection Hebrews makes"},
    ],
    "what_it_doesnt_say": [
        "The author is never named — Pauline authorship was debated even in antiquity. Origen: 'only God knows who wrote Hebrews'",
        "The audience is never explicitly identified — 'Hebrews' is a later title. Were they Jewish Christians tempted to revert to Judaism?",
        "HOW Melchizedek has 'no beginning of days or end of life' (7:3) — is this a literary argument from silence or an ontological claim?",
        "The 'great cloud of witnesses' (12:1) — are they observing us or simply testifying by their example? The text is ambiguous",
    ],
    "unusual_characters": [
        {"name": "Melchizedek", "ref": "7:1-3", "detail": "King of Salem, priest of God Most High. 'Without father, mother, genealogy, beginning of days, or end of life — resembling the Son of God.' The most mysterious figure in the Bible.", "connections": ["genesis", "psalms", "dss"]},
        {"name": "Moses", "ref": "3:1-6", "detail": "Faithful as a SERVANT in God's house; Christ faithful as a SON over God's house — both faithful, but vastly different rank.", "connections": ["exodus", "deuteronomy"]},
        {"name": "The Son", "ref": "1:1-4", "detail": "Named heir of all things, creator of the ages, radiance of glory, exact imprint of divine nature, sustainer of all things by his word — the highest Christology in the NT.", "connections": ["john", "colossians"]},
    ],
    "patterns": [
        "Better/superior comparisons: better covenant (7:22), better promises (8:6), better sacrifice (9:23), better country (11:16) — everything in the old order points to something superior in Christ",
        "Warning passages (2:1-4, 3:7-4:13, 5:11-6:12, 10:26-31, 12:25-29) — five escalating warnings against apostasy, each more severe than the last",
        "Shadow to reality: the entire old covenant system (tabernacle, priesthood, sacrifices) was the shadow; Christ is the substance that casts the shadow",
        "Faith hall of fame (ch. 11): Abel, Enoch, Noah, Abraham, Sarah, Moses — each exemplifies a different dimension of faith, building toward the 'pioneer and perfecter' (12:2)",
    ],
    "mistranslations": [
        {"english": "high priest", "original": "archiereus", "issue": "Familiar religious title obscures the radical claim — Jesus holds a priesthood that predates, outranks, and replaces the entire Levitical system"},
        {"english": "once for all", "original": "ephapax", "issue": "Often read as 'once upon a time' when it means 'once and for all time, never to be repeated' — the finality is absolute"},
        {"english": "copy and shadow", "original": "hypodeigma kai skia", "issue": "Sounds dismissive of the OT system; the point is that shadows are cast by REAL objects — the earthly tabernacle proves the heavenly one exists"},
    ],
}

STRUCTURED['james'] = {
    "key_claim": "James reveals that the demons possess orthodox theology — 'the demons believe and shudder' (2:19) — meaning intellectual assent to truth is not faith. Real faith produces works, and James points back to Job's endurance to reveal 'the purpose of the Lord' (5:11).",
    "contested_words": [
        {"word": "pistis", "greek": "\u03c0\u03af\u03c3\u03c4\u03b9\u03c2", "issue": "'Faith' (2:14-26) — James and Paul use the same word differently. Paul: faith vs. works of Torah. James: living faith vs. dead intellectual assent. No contradiction — different opponents.", "severity": "CRITICAL"},
        {"word": "phrissousin", "greek": "\u03c6\u03c1\u03af\u03c3\u03c3\u03bf\u03c5\u03c3\u03b9\u03bd", "issue": "'Shudder' (2:19) — physical trembling from terror. The demons' response to God's existence is not worship but horror. Right doctrine with wrong relationship.", "severity": "MAJOR"},
        {"word": "telos kyriou", "greek": "\u03c4\u03ad\u03bb\u03bf\u03c2 \u03ba\u03c5\u03c1\u03af\u03bf\u03c5", "issue": "'Purpose/outcome of the Lord' (5:11) — telos = end goal, purpose, completion. Job's suffering had a divine telos that was invisible during the trial.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "job", "why": "'You have heard of the steadfastness of Job and seen the telos of the Lord' (5:11) — James reads Job as evidence that God's purposes are compassionate even when hidden"},
        {"target": "genesis", "why": "Abraham 'offered up Isaac' (2:21) — faith completed by works. James reads Gen 22 as proof that Gen 15:6 faith produces Gen 22 obedience"},
        {"target": "matthew", "why": "James's ethical teaching closely parallels the Sermon on the Mount — oaths (5:12, Matt 5:34), prayer (5:13-18, Matt 6:5-15), mercy (2:13, Matt 5:7)"},
        {"target": "proverbs", "why": "James is NT wisdom literature — practical, proverbial, focused on speech, wealth, and community. The Hebrew wisdom tradition continued"},
    ],
    "what_it_doesnt_say": [
        "Never mentions the cross, resurrection, or atonement — the most 'Jewish' letter in the NT, focused on covenant faithfulness over theological system",
        "The 'faith vs. works' debate (2:14-26) never mentions Paul by name — is James responding to Paul or to a misunderstanding of Paul?",
        "The 'prayer of faith will save the sick' (5:15) is stated without qualification — what about unanswered prayers for healing?",
        "'The tongue is a fire, a world of unrighteousness' (3:6) — the most vivid speech ethics in the NT, but no system for controlling it is offered",
    ],
    "unusual_characters": [
        {"name": "James", "ref": "1:1", "detail": "Brother of Jesus who did not believe during Jesus' ministry (John 7:5) but became leader of the Jerusalem church. His conversion is one of the strongest resurrection evidences.", "connections": ["acts", "galatians"]},
        {"name": "Rahab", "ref": "2:25", "detail": "A Canaanite prostitute justified by works — paired with Abraham as proof that faith acts. Two extremes of society, same principle.", "connections": ["joshua", "hebrews"]},
    ],
    "patterns": [
        "Imperative density: James has more commands per verse than any NT book — practical, urgent, no room for passive religion",
        "Speech/tongue theme runs through the entire letter: quick to hear, slow to speak (1:19), the tongue as fire (3:1-12), do not grumble (5:9) — words are the index of the heart",
        "Rich/poor reversal: the rich will 'fade away' (1:11), the poor are 'heirs of the kingdom' (2:5), the rich are condemned (5:1-6) — radical economic inversion",
    ],
    "mistranslations": [
        {"english": "faith without works is dead", "original": "he pistis choris ergon nekra estin", "issue": "Often weaponized against Paul — but James defines 'works' as mercy and obedience, not Torah observance. Different word, different target"},
        {"english": "religion", "original": "threskeia", "issue": "'Religion' (1:27) is too institutional — threskeia means 'worship practice/devotion.' Pure devotion is caring for orphans and widows, not ritual"},
    ],
}

STRUCTURED['1peter'] = {
    "key_claim": "Christ 'proclaimed (ekerxen) to the spirits in prison' (3:19) — the Greek is kerysso (proclaim victory), NOT euangelizo (preach gospel). Christ announced his triumph to the imprisoned Watchers of Gen 6/1 Enoch, and all 'angels, authorities, and powers' are now subject to him (3:22).",
    "contested_words": [
        {"word": "ekerxen", "greek": "\u1f10\u03ba\u03ae\u03c1\u03c5\u03be\u03b5\u03bd", "issue": "'Proclaimed' (3:19) — kerysso = herald's announcement of victory, NOT euangelizo = preach the gospel. Christ did not offer salvation to imprisoned spirits; he announced their defeat.", "severity": "CRITICAL"},
        {"word": "pneumasin en phylake", "greek": "\u03c0\u03bd\u03b5\u03cd\u03bc\u03b1\u03c3\u03b9\u03bd \u1f10\u03bd \u03c6\u03c5\u03bb\u03b1\u03ba\u1fc7", "issue": "'Spirits in prison' (3:19) — these are the Watchers of Gen 6 / 1 Enoch 10 who 'did not obey in the days of Noah' (3:20). Not dead humans but imprisoned divine beings.", "severity": "CRITICAL"},
        {"word": "parepidemos", "greek": "\u03c0\u03b1\u03c1\u03b5\u03c0\u03af\u03b4\u03b7\u03bc\u03bf\u03c2", "issue": "'Sojourner/exile' (1:1, 2:11) — believers are resident aliens in a world governed by hostile spiritual powers. Their true citizenship is in the heavenly Jerusalem.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "1enoch", "why": "The 'spirits in prison who did not obey in the days of Noah' (3:19-20) are the imprisoned Watchers of 1 Enoch 10 — Peter assumes the Enochic framework"},
        {"target": "genesis", "why": "The disobedience 'in the days of Noah' (3:20) points to Gen 6:1-4 — the Watcher rebellion that provoked the Flood"},
        {"target": "2peter", "why": "2 Pet 2:4 expands: 'God did not spare angels when they sinned but cast them into Tartarus' — the same imprisoned spirits, named more explicitly"},
        {"target": "jude", "why": "Jude 6 parallels exactly: 'angels who did not stay within their position' kept in 'eternal chains' — the same tradition Peter draws from"},
        {"target": "exodus", "why": "'A royal priesthood, a holy nation' (2:9) quotes Ex 19:6 — Israel's vocation transferred to the ekklesia, including Gentiles"},
    ],
    "what_it_doesnt_say": [
        "WHEN Christ proclaimed to the imprisoned spirits — between death and resurrection? At the ascension? The timing is debated",
        "What the 'spirits in prison' heard — did they respond? Was it pure announcement or did it include judgment?",
        "How 'baptism now saves you' (3:21) works — Peter immediately qualifies: 'not removal of dirt but an appeal to God for a good conscience.' The mechanism is unclear",
        "The 'fiery trial' (4:12) is never specified — Nero's persecution? General tribulation? Eschatological suffering?",
    ],
    "unusual_characters": [
        {"name": "The spirits in prison", "ref": "3:19", "detail": "Imprisoned Watchers who rebelled in Noah's day. Christ visits them not to save but to announce victory — kerysso, not euangelizo.", "connections": ["1enoch", "genesis", "2peter", "jude"]},
        {"name": "Sarah", "ref": "3:6", "detail": "Example of holy women who 'hoped in God' — called Abraham 'lord.' Peter uses her as a model of strength, not submission.", "connections": ["genesis"]},
    ],
    "patterns": [
        "Suffering → glory pattern: Christ suffered then was glorified (1:11); believers suffer now and will be glorified later (4:13, 5:10). The sequence is fixed",
        "Stone imagery: Christ as living stone rejected by men, chosen by God (2:4-8). Believers as living stones built into a spiritual house — Ps 118:22 + Isa 28:16",
        "Exile language: 'elect exiles of the Dispersion' (1:1), 'sojourners and exiles' (2:11) — the ekklesia lives as aliens in hostile territory governed by spiritual powers",
    ],
    "mistranslations": [
        {"english": "preached", "original": "ekerxen (kerysso)", "issue": "CRITICAL: 'preached' implies gospel offer. The Greek is kerysso = announce/proclaim victory. Christ proclaimed triumph, not salvation, to the imprisoned Watchers"},
        {"english": "spirits in prison", "original": "pneumasin en phylake", "issue": "Often interpreted as dead humans; the context ('did not obey in days of Noah') and parallel texts (2 Pet 2:4, Jude 6) identify them as fallen divine beings"},
        {"english": "aliens and strangers", "original": "paroikoi kai parepidēmoi", "issue": "Sounds like mere metaphor; Peter means it ontologically — believers belong to a different polity and their current world is enemy territory"},
    ],
}

STRUCTURED['2peter'] = {
    "key_claim": "2 Peter provides the most explicit Greek confirmation of the Watcher framework: 'God did not spare angels when they sinned but cast them into Tartarus' (2:4) — using the Greek term for the prison of the Titans, confirming that the 1 Enoch/Watcher imprisonment is historical reality.",
    "contested_words": [
        {"word": "tartarosas", "greek": "\u03c4\u03b1\u03c1\u03c4\u03b1\u03c1\u03ce\u03c3\u03b1\u03c2", "issue": "'Cast into Tartarus' (2:4) — NOT Gehenna or Hades. Tartarus is the Greek mythological prison of the Titans. Peter deliberately uses pagan cosmological language to describe a real spiritual prison.", "severity": "CRITICAL"},
        {"word": "seirais zophou", "greek": "\u03c3\u03b5\u03b9\u03c1\u03b1\u1fd6\u03c2 \u03b6\u03cc\u03c6\u03bf\u03c5", "issue": "'Chains of gloomy darkness' (2:4) — some manuscripts read 'pits' (seirois). Either way, imprisoned in darkness awaiting judgment — matching 1 Enoch 10:4-6 exactly.", "severity": "CRITICAL"},
        {"word": "theian physin", "greek": "\u03b8\u03b5\u03af\u03b1\u03bd \u03c6\u03cd\u03c3\u03b9\u03bd", "issue": "'Divine nature' (1:4) — believers become 'partakers of the divine nature.' The only place in the NT that uses this phrase. Theosis/deification language.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "1enoch", "why": "Tartarus = the prison described in 1 Enoch 10:4-6 and 18:11-19:3 — Peter confirms the Watcher imprisonment using Greek cosmological terms"},
        {"target": "jude", "why": "2 Pet 2:4-17 closely parallels Jude 5-16 — both draw from the same Watcher tradition. The literary relationship is debated but the theology is identical"},
        {"target": "genesis", "why": "The angels who sinned (2:4) are the bene ha'elohim of Gen 6:1-4 — Peter treats Genesis 6 as recording a real angelic rebellion"},
        {"target": "1peter", "why": "The 'spirits in prison' of 1 Pet 3:19 are the same 'angels cast into Tartarus' of 2 Pet 2:4 — Peter's consistent cosmology across both letters"},
        {"target": "numbers", "why": "Balaam's 'way' (2:15) — the paradigm of the corrupt prophet who uses divine gifts for personal gain"},
    ],
    "what_it_doesnt_say": [
        "Why Peter uses TARTARUS instead of Gehenna or Sheol — is he contextualizing for a Greek audience or making a theological point about the nature of the prison?",
        "The relationship between 2 Peter and Jude is never addressed — did one copy the other? Did both use a common source?",
        "When 'the heavens will be set on fire and dissolved' (3:12) — is this literal cosmic destruction or transformation? The 'new heavens and new earth' (3:13) suggests renewal, not annihilation",
        "How believers 'become partakers of the divine nature' (1:4) — the mechanism of theosis is stated without explanation",
    ],
    "unusual_characters": [
        {"name": "The imprisoned angels", "ref": "2:4", "detail": "Cast into Tartarus — the Greek prison of the Titans. Peter confirms the Watcher framework using the most explicit pagan-cosmological language in the NT.", "connections": ["1enoch", "genesis", "jude"]},
        {"name": "Balaam", "ref": "2:15-16", "detail": "'The way of Balaam' — using prophetic gifts for profit. His donkey had more spiritual discernment than the prophet.", "connections": ["numbers", "jude", "revelation"]},
    ],
    "patterns": [
        "Three judgments in sequence (2:4-9): fallen angels → ancient world (Flood) → Sodom and Gomorrah. Each confirms God judges rebellious spiritual AND human agents",
        "Cosmic transformation: the present heavens and earth are 'stored up for fire' (3:7) but 'new heavens and new earth' will follow (3:13) — destruction is the prelude to renewal, not the end",
        "Eyewitness authority: 'we were eyewitnesses of his majesty' (1:16) at the Transfiguration — Peter grounds his teaching in direct divine encounter, not speculation",
    ],
    "mistranslations": [
        {"english": "hell", "original": "tartarosas", "issue": "CRITICAL: most translations render this as 'hell,' hiding the specific cosmological claim. Tartarus is NOT Gehenna — it is the specific prison for fallen divine beings"},
        {"english": "cast them down", "original": "tartarosas", "issue": "The verb form IS the name of the prison — 'tartarus-ed them.' The location is embedded in the action"},
        {"english": "partakers of the divine nature", "original": "theias koinonoi physeos", "issue": "Sounds like abstract theology; this is the most radical deification language in the NT — human beings sharing in God's own nature"},
    ],
}

STRUCTURED['1john'] = {
    "key_claim": "The purpose of the incarnation is cosmic warfare: 'the reason the Son of God appeared was to destroy the works of the devil' (3:8) — and believers must 'test the spirits' (4:1) because the spiritual realm produces both true and false revelation.",
    "contested_words": [
        {"word": "lyse", "greek": "\u03bb\u03cd\u03c3\u1fc3", "issue": "'Destroy' (3:8) — lyo means to loose, untie, dissolve. Christ did not merely defeat the devil's works but DISSOLVED them — undoing the damage at a structural level.", "severity": "CRITICAL"},
        {"word": "dokimazete ta pneumata", "greek": "\u03b4\u03bf\u03ba\u03b9\u03bc\u03ac\u03b6\u03b5\u03c4\u03b5 \u03c4\u1f70 \u03c0\u03bd\u03b5\u03cd\u03bc\u03b1\u03c4\u03b1", "issue": "'Test the spirits' (4:1) — dokimazo = assay, examine like testing metal. The spiritual realm produces real entities, not just ideas. Discernment is mandatory.", "severity": "CRITICAL"},
        {"word": "hilasmos", "greek": "\u1f31\u03bb\u03b1\u03c3\u03bc\u03cc\u03c2", "issue": "'Propitiation/atoning sacrifice' (2:2, 4:10) — same root as hilasterion (Rom 3:25). Christ IS the propitiation for our sins, 'and not for ours only but for the whole world.'", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "john", "why": "'In the beginning was the Word' (John 1:1) echoes 'what was from the beginning' (1 John 1:1) — both establish pre-existence and personal encounter with the divine"},
        {"target": "genesis", "why": "'Cain who was of the evil one and murdered his brother' (3:12) — the seed war of Gen 3:15 made personal. Cain = the serpent's seed, Abel = the righteous seed"},
        {"target": "revelation", "why": "The spirit of antichrist (2:18, 4:3) active now anticipates the final Antichrist of Revelation — the pattern is already at work"},
        {"target": "deuteronomy", "why": "Testing spirits (4:1) fulfills the Deut 13:1-5 mandate to test prophets — false revelation has been a threat since Sinai"},
    ],
    "what_it_doesnt_say": [
        "How to test the spirits (4:1-3) — the only criterion given is christological: 'every spirit that confesses Jesus Christ has come in the flesh.' Is that sufficient?",
        "'God is love' (4:8, 16) — the most quoted verse from 1 John, but the letter equally insists God is light (1:5) and truth. Love without light and truth is sentimentality",
        "The 'sin that leads to death' (5:16) is never identified — apostasy? Blasphemy against the Spirit? An unforgivable threshold?",
        "'No one born of God makes a practice of sinning' (3:9) — the tension with 1:8 ('if we say we have no sin, we deceive ourselves') is never fully resolved",
    ],
    "unusual_characters": [
        {"name": "The antichrist(s)", "ref": "2:18", "detail": "'Many antichrists have come' — plural, present, already active. The eschatological Antichrist is preceded by a pattern of anti-Christ spirits in every generation.", "connections": ["revelation", "2thessalonians"]},
        {"name": "Cain", "ref": "3:12", "detail": "'Of the evil one' — John identifies Cain's line as belonging to Satan's seed. The Gen 3:15 war personified in the first murder.", "connections": ["genesis"]},
    ],
    "patterns": [
        "Light/darkness dualism: God is light (1:5), walk in light (1:7), children of light vs. children of darkness — Qumran-like binary that is ultimately christological",
        "Love as theological test: 'whoever does not love does not know God' (4:8) — love is not sentiment but evidence of divine indwelling. The test is relational, not intellectual",
        "Abide/remain (meno): appears 27 times — the central command. Not activity but positioning: stay connected to the vine (John 15 language continued)",
        "Three witnesses: 'the Spirit and the water and the blood' (5:8) — three dimensions of testimony to Christ's reality",
    ],
    "mistranslations": [
        {"english": "propitiation", "original": "hilasmos", "issue": "Abstract theological term hides the concrete: Christ himself IS the atonement, not merely its agent — the offering and the altar merged"},
        {"english": "test the spirits", "original": "dokimazete ta pneumata", "issue": "'Test' sounds casual; dokimazo means metallurgical assay — rigorous, scientific examination of spiritual claims"},
        {"english": "destroy", "original": "lyse", "issue": "English 'destroy' implies violence; the Greek means 'dissolve, untie, undo' — Christ unravels the devil's work at the structural level"},
    ],
}

STRUCTURED['jude'] = {
    "key_claim": "Jude is the most explicit NT engagement with 1 Enoch — directly quoting 1 Enoch 1:9 as prophecy ('Enoch, the seventh from Adam, prophesied,' vv. 14-15) and treating the Watcher rebellion as historical fact (v. 6), confirming the imprisoned-angel framework that 1 Peter and 2 Peter also assume.",
    "contested_words": [
        {"word": "proephetyeusen", "greek": "\u03c0\u03c1\u03bf\u03b5\u03c6\u03ae\u03c4\u03b5\u03c5\u03c3\u03b5\u03bd", "issue": "'Prophesied' (v. 14) — Jude calls Enoch's words PROPHECY, not merely useful literature. This is the strongest canonical endorsement of 1 Enoch's authority.", "severity": "CRITICAL"},
        {"word": "oiketerion", "greek": "\u03bf\u1f30\u03ba\u03b7\u03c4\u03ae\u03c1\u03b9\u03bf\u03bd", "issue": "'Proper dwelling' (v. 6) — the angels 'left their proper dwelling.' oiketerion is used only here and 2 Cor 5:2 (of the resurrection body). The Watchers abandoned their heavenly body/domain.", "severity": "CRITICAL"},
        {"word": "desmois aidiois", "greek": "\u03b4\u03b5\u03c3\u03bc\u03bf\u1fd6\u03c2 \u1f00\u03ca\u03b4\u03af\u03bf\u03b9\u03c2", "issue": "'Eternal chains' (v. 6) — the imprisoned Watchers bound in everlasting bonds. Matches 1 Enoch 10:4-6 and 2 Pet 2:4 (Tartarus). Real prison, real chains, real judgment awaited.", "severity": "CRITICAL"},
    ],
    "hidden_connections": [
        {"target": "1enoch", "why": "Jude 14-15 directly quotes 1 Enoch 1:9. Jude 6 parallels 1 Enoch 10:4-6 (imprisoned Watchers). The most explicit canonical use of 1 Enoch"},
        {"target": "genesis", "why": "The angels 'who did not stay within their position' (v. 6) are the bene ha'elohim of Gen 6:1-4 who took human wives"},
        {"target": "2peter", "why": "Jude and 2 Peter share extensive material — both cite fallen angels, Balaam, and similar false teachers. The literary relationship confirms a shared Watcher tradition"},
        {"target": "1peter", "why": "The 'spirits in prison' (1 Pet 3:19) are the same 'angels kept in eternal chains' (Jude 6) — Peter and Jude share the same cosmology"},
        {"target": "numbers", "why": "Balaam (v. 11) and Korah's rebellion (v. 11) both from Numbers — Jude reads OT history as a pattern of spiritual rebellion"},
        {"target": "daniel", "why": "'Michael the archangel disputed with the devil about the body of Moses' (v. 9) — divine council conflict at the highest levels"},
    ],
    "what_it_doesnt_say": [
        "The source of the Michael-Satan dispute over Moses' body (v. 9) — Jude cites it as known but our source text (Assumption of Moses) is fragmentary",
        "WHY Jude treats 1 Enoch as authoritative prophecy — does quotation equal canonization? The letter never addresses the canon question",
        "The identity of the false teachers (v. 4) — they 'crept in unnoticed' but their specific heresy is described in imagery, not doctrine",
        "How the Watchers 'left their proper dwelling' (v. 6) — the mechanics of angelic embodiment are assumed, not explained",
    ],
    "unusual_characters": [
        {"name": "Michael the archangel", "ref": "v. 9", "detail": "Disputes with the devil over Moses' body — even the chief angel does not pronounce judgment independently but says 'The Lord rebuke you.' Divine council protocol.", "connections": ["daniel", "revelation"]},
        {"name": "Enoch", "ref": "v. 14", "detail": "'The seventh from Adam' — Jude specifies his genealogical position and calls his words PROPHECY. The strongest canonical endorsement of Enoch's authority.", "connections": ["genesis", "1enoch", "hebrews"]},
        {"name": "Cain, Balaam, Korah", "ref": "v. 11", "detail": "Three OT rebels as a pattern: Cain (murder from envy), Balaam (prophecy for profit), Korah (rebellion against authority). Three types of apostasy.", "connections": ["genesis", "numbers"]},
    ],
    "patterns": [
        "Triad of judgment examples: angels who fell (v. 6), Sodom and Gomorrah (v. 7), and the wilderness generation (v. 5) — spiritual, sexual, and national rebellion all judged",
        "Triad of apostasy types: 'way of Cain' (murder/envy), 'error of Balaam' (greed/corruption), 'rebellion of Korah' (authority rejection) — the three patterns recur in every generation",
        "Doxology framework: the letter ends with one of the most powerful doxologies in Scripture (vv. 24-25) — 'to the only God our Savior... before all time and now and forever'",
    ],
    "mistranslations": [
        {"english": "contend for the faith", "original": "epagonizomai", "issue": "Sounds intellectual; the Greek is athletic/military — agonize, struggle, fight for the faith. This is combat language, not debate language"},
        {"english": "kept in eternal chains", "original": "desmois aidiois hypo zophon tetereken", "issue": "Often spiritualized; Jude means actual imprisonment of actual beings in actual darkness — the Watcher tradition taken at face value"},
        {"english": "wandering stars", "original": "asteres planetai", "issue": "Poetic in English; in Jewish cosmology, wandering stars are fallen angels — beings that left their ordained orbit/position. Direct 1 Enoch imagery"},
    ],
}

STRUCTURED['revelation'] = {
    "key_claim": "Revelation is the divine council's final session — every thread converges as the Lamb opens the scroll, the nachash of Genesis 3 is identified by four names (serpent, devil, Satan, deceiver), and the Deut 32:8 allotment is FULLY reversed: 'You ransomed people from EVERY tribe and language and people and nation' (5:9).",
    "contested_words": [
        {"word": "ophis ho archaios", "greek": "\u1f44\u03c6\u03b9\u03c2 \u1f41 \u1f00\u03c1\u03c7\u03b1\u1fd6\u03bf\u03c2", "issue": "'That ancient serpent' (12:9) — four names: serpent (Gen 3), devil (diabolos), Satan (ha-satan), deceiver of the whole world. The entire story unified in one identification.", "severity": "CRITICAL"},
        {"word": "arnion", "greek": "\u1f00\u03c1\u03bd\u03af\u03bf\u03bd", "issue": "'Lamb' — appears 28 times in Revelation. NOT amnos (sacrificial lamb, John 1:29) but arnion (small lamb/lambkin). The most powerful being in the cosmos described by the weakest term.", "severity": "CRITICAL"},
        {"word": "nikao", "greek": "\u03bd\u03b9\u03ba\u03ac\u03c9", "issue": "'Conquer/overcome' — 17 times in Revelation. The seven letters each end with promises 'to the one who conquers.' Victory language permeates the entire book.", "severity": "MAJOR"},
        {"word": "martyria", "greek": "\u03bc\u03b1\u03c1\u03c4\u03c5\u03c1\u03af\u03b1", "issue": "'Testimony/witness' — same root as 'martyr.' In Revelation, bearing witness and dying for it are the same word. Testimony IS the mechanism of conquest.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "Eden bookend: the nachash of Gen 3 identified (12:9), the tree of life restored (22:2), the curse removed (22:3) — Rev 21-22 is Genesis 1-3 restored and surpassed"},
        {"target": "deuteronomy", "why": "'You ransomed people from every tribe, language, people, nation' (5:9) — the Deut 32:8 allotment FULLY reversed. Every nation reclaimed from the corrupt elohim"},
        {"target": "daniel", "why": "Rev 13 draws from Dan 7 (beasts from the sea), Rev 20 from Dan 12 (resurrection and judgment). Daniel's visions find their consummation in Revelation"},
        {"target": "ezekiel", "why": "The new Jerusalem (Rev 21) draws from Ezek 40-48 (new temple), the river of life from Ezek 47, the throne vision from Ezek 1. Revelation is Ezekiel fulfilled"},
        {"target": "exodus", "why": "The plagues of Revelation (trumpets, bowls) recapitulate the Exodus plagues on a cosmic scale — liberation from a spiritual Egypt"},
        {"target": "1enoch", "why": "The binding of Satan (20:1-3) parallels the binding of Azazel (1 Enoch 10:4-6) — both imprisoned in a pit, both released for a final period"},
        {"target": "psalms", "why": "Ps 2 ('the nations rage') underlies Rev 11:18, 19:15 — the divine decree against rebellious nations and their spiritual rulers"},
    ],
    "what_it_doesnt_say": [
        "The 'millennium' (20:1-6) — premillennial, postmillennial, or amillennial? The text describes 1,000 years without specifying whether the number is literal or symbolic",
        "The identity of the 144,000 (7:4, 14:1) — literal Israel or symbolic of the complete people of God? Twelve tribes times twelve thousand — the number is clearly structured",
        "The new Jerusalem descending 'from heaven' (21:2) — is this a city, a people, or both? The bride/city fusion is never resolved",
        "How the 'nations will walk by its light' (21:24) — if all evil is destroyed, who are these nations? The relationship between the new earth's inhabitants and the New Jerusalem is unclear",
    ],
    "unusual_characters": [
        {"name": "The Lamb (arnion)", "ref": "5:6", "detail": "Standing 'as though slain' with seven horns and seven eyes — the sacrificial victim IS the most powerful being in the cosmos. Weakness IS power.", "connections": ["john", "exodus", "isaiah"]},
        {"name": "The four living creatures", "ref": "4:6-8", "detail": "Lion, ox, eagle, human — echoing Ezekiel's chayyot. They never stop saying 'Holy, holy, holy' — the throne room of God in perpetual worship.", "connections": ["ezekiel", "isaiah"]},
        {"name": "The two witnesses", "ref": "11:3-12", "detail": "Power to shut heaven (Elijah) and turn water to blood (Moses) — the Law and Prophets testifying together in the end.", "connections": ["exodus", "1kings"]},
        {"name": "Michael", "ref": "12:7", "detail": "Leads the angelic army against the dragon — divine council warfare at its most explicit. Heaven itself becomes a battlefield.", "connections": ["daniel", "jude"]},
    ],
    "patterns": [
        "Sevenfold structure: 7 letters, 7 seals, 7 trumpets, 7 bowls — each cycle intensifies, but all cover the same period from different angles (recapitulation, not strict chronology)",
        "Worship scenes punctuate every judgment cycle — the throne room doxologies (4:8-11, 5:9-14, 7:9-12, 11:15-18, 15:3-4, 19:1-8) frame all destruction in the context of worship",
        "Babylon vs. New Jerusalem: the great prostitute (ch. 17) vs. the holy bride (ch. 21) — two cities, two systems, two destinies. Every human being lives in one or the other",
        "The conqueror promises (chs. 2-3) are all fulfilled in chs. 21-22: tree of life (2:7→22:2), no second death (2:11→21:8), hidden manna (2:17→22:2), authority over nations (2:26→22:5)",
        "Eden-to-Eden arc: Gen 1-3 (garden, tree, river, presence of God, no curse) → Rev 21-22 (city-garden, tree, river, presence of God, no more curse) — the Bible's narrative envelope",
    ],
    "mistranslations": [
        {"english": "Lamb", "original": "arnion", "issue": "English cannot capture that Revelation uses a DIMINUTIVE (little lamb/lambkin) for the most powerful being in existence — deliberate paradox of power through weakness"},
        {"english": "beast", "original": "therion", "issue": "English 'beast' sounds mythological; therion is a wild animal — the contrast is between the domesticated lamb and the wild, untamed power of empire"},
        {"english": "witness/testimony", "original": "martyria", "issue": "Modern 'witness' has lost its teeth — the Greek became 'martyr' because testimony in Revelation costs your life. Witness = death sentence"},
    ],
}

# ═══════════════════════════════════════════════════
#  NON-CANONICAL TEXTS
# ═══════════════════════════════════════════════════

STRUCTURED['enoch'] = {
    "key_claim": "According to 1 Enoch, the 200 Watchers who descended on Mount Hermon taught forbidden knowledge to humanity, their offspring (the Nephilim) became demons when killed (15:8-10), and the pre-existent Son of Man sits on the throne of glory to judge all — a framework that the NT authors (Jude, Peter, Jesus himself) treat as authoritative.",
    "contested_words": [
        {"word": "Watchers (Irin)", "hebrew": "עִירִין", "issue": "'Watchers' — divine beings who 'watch' over humanity. The term appears in Dan 4:13, 17, 23 (Aramaic). 1 Enoch expands their story: 200 descend on Hermon, take human wives, teach forbidden arts.", "severity": "CRITICAL"},
        {"word": "Azazel", "hebrew": "עֲזָאזֵל", "issue": "Leader of the Watchers who taught humanity warfare and cosmetics (1 En 8:1-2). The same being addressed in Lev 16 (Day of Atonement scapegoat) — sins sent BACK to their originator.", "severity": "CRITICAL"},
        {"word": "Nephilim", "hebrew": "נְפִילִים", "issue": "Offspring of Watchers and human women. 1 Enoch 15:8-10 explains that when they die, their disembodied spirits become DEMONS — the missing origin story for evil spirits.", "severity": "CRITICAL"},
        {"word": "Son of Man", "greek": "υἱὸς τοῦ ἀνθρώπου", "issue": "The Parables of Enoch (chs. 37-71) describe a pre-existent, enthroned Son of Man who judges. Jesus' self-designation draws from both Dan 7:13 AND the Enochic tradition.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "1 Enoch 6-16 is the expanded narrative of Gen 6:1-4 — what Genesis compresses into four verses, 1 Enoch unfolds into eleven chapters"},
        {"target": "jude", "why": "Jude 14-15 directly quotes 1 Enoch 1:9 as prophecy and treats the Watcher rebellion (Jude 6) as historical fact"},
        {"target": "leviticus", "why": "Azazel in Lev 16 is the same being named in 1 Enoch 10:4-6 — the Day of Atonement scapegoat ritual sends sins back to the Watcher leader"},
        {"target": "daniel", "why": "The 'Watchers' appear in Dan 4:13, 17, 23. The 'Son of Man' in Dan 7:13 is expanded in 1 Enoch's Parables (chs. 37-71)"},
        {"target": "2peter", "why": "'God did not spare angels when they sinned but cast them into Tartarus' (2 Pet 2:4) — Peter confirms the 1 Enoch imprisonment narrative"},
        {"target": "matthew", "why": "Jesus' demons seeking bodies (Matt 12:43-45) is explained by 1 Enoch 15:8-10 — disembodied Nephilim spirits seeking re-embodiment"},
    ],
    "what_it_doesnt_say": [
        "According to 1 Enoch, the Watchers' motivation beyond lust is never fully explored — why did 200 divine beings coordinate a rebellion?",
        "The relationship between the Parables (chs. 37-71) and the Book of Giants (found at Qumran instead) — why did different communities preserve different traditions?",
        "How Enoch traveled through the heavens — the cosmological journeys describe locations but not the mechanism of ascent",
        "According to 1 Enoch, the ultimate fate of the Watchers after final judgment is described but the duration of 'forever' is ambiguous in the original language",
    ],
    "unusual_characters": [
        {"name": "Semjaza (Shemihazah)", "ref": "6:3", "detail": "Leader of the 200 Watchers who organized the oath on Mount Hermon. According to 1 Enoch, he feared acting alone and required a mutual pact.", "connections": ["genesis"]},
        {"name": "Azazel", "ref": "8:1, 10:4-6", "detail": "According to 1 Enoch, the Watcher who taught warfare, metalwork, and cosmetics. Bound hand and foot, cast into darkness — the same being addressed in Lev 16.", "connections": ["leviticus"]},
        {"name": "The Son of Man (Parables)", "ref": "46:1-4", "detail": "According to 1 Enoch, a pre-existent figure with 'a head white as wool' who sits on the throne of glory. The imagery Jesus drew from for his self-designation.", "connections": ["daniel", "matthew", "revelation"]},
    ],
    "patterns": [
        "According to 1 Enoch, the Watcher narrative follows a rebellion-judgment-imprisonment arc that parallels the Eden rebellion and the Babel rebellion — three cosmic failures, three divine responses",
        "The heavenly journeys (chs. 17-36, 72-82) establish a cosmological framework: Sheol compartments, celestial mechanics, boundary geography — systematic supernatural cartography",
        "The demon-origin theory (15:8-10): Nephilim die → spirits have no body → seek embodiment → become demons. This explains the entire NT exorcism tradition",
        "The Son of Man in the Parables (37-71) grows from hidden to revealed to enthroned — the same revelation pattern as Jesus' ministry in the Gospels",
    ],
    "mistranslations": [
        {"english": "angels", "original": "Watchers (Irin)", "issue": "Calling them 'angels' conflates different categories — Watchers are a specific class of divine beings with a specific function and a specific rebellion"},
        {"english": "giants", "original": "Nephilim", "issue": "Reduces the theological category to physical size — the Nephilim are divine-human hybrids whose spiritual status (disembodied = demons) matters more than their height"},
        {"english": "Son of Man", "original": "Son of Man", "issue": "The Enochic Son of Man is pre-existent and enthroned — 'Son of Man' sounds humble in English but in this context it is the highest possible title"},
    ],
}

STRUCTURED['jubilees'] = {
    "key_claim": "According to Jubilees, the Angel of the Presence mediated Torah to Moses directly — a tradition confirmed by Acts 7:53 and Gal 3:19 — and the chief demon Mastema retained one-tenth of the demons after the Flood to test humanity, explaining why evil persists in a post-Flood world.",
    "contested_words": [
        {"word": "Angel of the Presence", "hebrew": "מַלְאַךְ הַפָּנִים", "issue": "According to Jubilees, Torah was dictated by the Angel of the Presence (malak ha-panim) — a specific divine being who stands before God. This is the mediating angel confirmed by Stephen (Acts 7:53) and Paul (Gal 3:19).", "severity": "CRITICAL"},
        {"word": "Mastema", "hebrew": "מַשְׂטֵמָה", "issue": "According to Jubilees, the chief of demons — derived from satan/accuse. After the Flood, God agrees to let Mastema retain 1/10 of the demons to test humanity. A negotiated arrangement, not uncontrolled evil.", "severity": "CRITICAL"},
        {"word": "364-day calendar", "hebrew": "", "issue": "According to Jubilees, the solar calendar of 364 days (52 weeks exactly) is the true calendar ordained at creation. This calendar controversy divided Second Temple Judaism and is central to the Dead Sea Scrolls community.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "acts", "why": "Stephen's speech: 'you who received the law as delivered by angels' (Acts 7:53) confirms Jubilees' tradition of angelic mediation of Torah"},
        {"target": "galatians", "why": "Paul: the law was 'ordained through angels' (Gal 3:19) — same tradition as Jubilees. The angelic mediation is canonical even if Jubilees is not"},
        {"target": "genesis", "why": "Jubilees retells Genesis with expanded detail — filling gaps, providing dates, and adding the angelic perspective on patriarchal history"},
        {"target": "exodus", "why": "Jubilees retells the Exodus with emphasis on the calendar and Passover dating — the liturgical framework behind the narrative"},
        {"target": "1enoch", "why": "Jubilees shares the Watcher tradition with 1 Enoch but adds the Mastema negotiation — a different emphasis on the demon problem"},
        {"target": "dss", "why": "Jubilees was one of the most popular texts at Qumran — the 364-day calendar was the community's liturgical backbone"},
    ],
    "what_it_doesnt_say": [
        "According to Jubilees, WHY God agreed to let Mastema keep 1/10 of the demons is never explained — a divine concession with enormous consequences",
        "The 364-day calendar creates a perpetual conflict with the 354-day lunar calendar — Jubilees never acknowledges the astronomical problem",
        "How the Angel of the Presence could mediate Torah when Exodus describes YHWH speaking directly to Moses — the mediation framework is added, not reconciled",
        "According to Jubilees, the relationship between Mastema and Satan/ha-satan is unclear — are they the same being or different?",
    ],
    "unusual_characters": [
        {"name": "Mastema", "ref": "10:8-11", "detail": "According to Jubilees, the prince of demons who petitioned God to retain 1/10 of the spirits. Same role as ha-satan in Job but with a different name and backstory.", "connections": ["job", "1enoch"]},
        {"name": "The Angel of the Presence", "ref": "1:27", "detail": "According to Jubilees, the specific angel who dictates the entire book to Moses. A divine being with face-to-face access to God — the mediator of Torah.", "connections": ["exodus", "acts", "galatians"]},
    ],
    "patterns": [
        "According to Jubilees, all history is organized into jubilee periods (49-year cycles) — time itself has a theological structure rooted in Lev 25",
        "The Mastema negotiation (10:8-11): Flood → spirits released → Mastema asks to retain some → God allows 1/10. Evil is permitted, bounded, and purposeful",
        "According to Jubilees, calendar polemics run throughout: the 364-day solar calendar ensures festivals always fall on the same weekday — liturgical order reflecting cosmic order",
    ],
    "mistranslations": [
        {"english": "Book of Jubilees", "original": "Sefer ha-Yovelim", "issue": "The title refers to jubilee-year dating system — the text organizes ALL of history into jubilee periods, making the calendar itself the theological framework"},
        {"english": "Mastema", "original": "Mastema", "issue": "Often left untranslated; the root means 'hostility/accusation' — functionally equivalent to ha-satan (the accuser) but with a specific post-Flood origin story"},
    ],
}

STRUCTURED['jasher'] = {
    "key_claim": "Jasher expands the patriarchal narratives with vivid detail — Abraham's childhood, Nimrod's tyranny, the tower of Babel — but this medieval compilation is NOT the original Book of Jashar referenced in Joshua 10:13 and 2 Samuel 1:18, which is lost.",
    "contested_words": [
        {"word": "Sefer HaYashar", "hebrew": "סֵפֶר הַיָּשָׁר", "issue": "'Book of the Upright/Righteous' — the original Jashar is cited in Josh 10:13 and 2 Sam 1:18 as a source the biblical authors used. This medieval text claims that title but cannot be verified as the original.", "severity": "CRITICAL"},
        {"word": "Nimrod", "hebrew": "נִמְרוֹד", "issue": "Genesis mentions Nimrod briefly (Gen 10:8-12); Jasher expands him into a major figure — tyrant, tower builder, hunter. The expansion is vivid but cannot be verified against the lost original.", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "genesis", "why": "Jasher fills narrative gaps in Genesis: Abraham's childhood, the tower of Babel details, Jacob and Esau's conflicts — whether historical or legendary, it shows how ancient readers imagined the missing stories"},
        {"target": "joshua", "why": "Josh 10:13 cites the ORIGINAL Book of Jashar for the sun standing still — this text claims that name but predates the original by over a millennium"},
        {"target": "2samuel", "why": "2 Sam 1:18 cites the original Book of Jashar for David's lament — another canonical reference to the lost source"},
        {"target": "1enoch", "why": "Jasher shares some patriarchal expansion traditions with 1 Enoch — particularly the pre-Flood period and the giants"},
    ],
    "what_it_doesnt_say": [
        "No claim to divine inspiration — unlike biblical texts, Jasher presents itself as historical narrative without prophetic authority",
        "The connection to the ORIGINAL Book of Jashar is never proven — the medieval text appeared in the 16th-18th century with no manuscript chain to antiquity",
        "The expanded Nimrod narrative has no parallel in other ancient sources — it may preserve genuine tradition or may be medieval invention",
        "How to distinguish historical memory from legendary expansion — Jasher mixes plausible detail with fantastic elements without differentiation",
    ],
    "unusual_characters": [
        {"name": "Nimrod", "ref": "ch. 7-12", "detail": "Expanded from Genesis's brief mention into a full-scale tyrant — receives the garments of Adam, becomes a mighty hunter, builds the tower. Historically unverifiable.", "connections": ["genesis"]},
        {"name": "Abraham (childhood)", "ref": "ch. 8-12", "detail": "Jasher provides a detailed childhood narrative — hiding in a cave, confronting idolatry, conflict with Nimrod. Fills Genesis's total silence about Abraham before age 75.", "connections": ["genesis"]},
    ],
    "patterns": [
        "Gap-filling pattern: wherever Genesis is silent (Abraham's childhood, Nimrod's story, the tower of Babel), Jasher provides detailed narrative — ancient midrashic tradition in action",
        "The patriarchal narratives follow Genesis's sequence but with expanded dialogue, motivation, and secondary characters — interpretive expansion, not contradiction",
        "The text preserves the seed-line emphasis: patriarchal genealogies and conflicts are always framed in terms of the righteous line vs. the rebellious",
    ],
    "mistranslations": [
        {"english": "Book of Jasher", "original": "Sefer HaYashar", "issue": "The title creates confusion with the biblical reference — readers must understand this is NOT the text Joshua and Samuel cite. That text is lost"},
        {"english": "Jasher", "original": "Yashar", "issue": "'Jasher' sounds like a person's name; yashar means 'upright/straight/righteous' — it is a TITLE ('Book of the Upright'), not an author's name"},
    ],
}

STRUCTURED['dss'] = {
    "key_claim": "The Dead Sea Scrolls preserve the original reading of Deut 32:8 ('sons of God' instead of 'sons of Israel') — the most important textual witness for the divine council framework — and 11Q13 presents Melchizedek as a divine figure executing the judgment of Psalm 82.",
    "contested_words": [
        {"word": "bene elohim (4QDeut-j)", "hebrew": "בְּנֵי אֱלֹהִים", "issue": "4QDeut-j preserves 'sons of God' at Deut 32:8 where the MT has 'sons of Israel' — the most consequential textual variant in the OT. The DSS reading is independently confirmed by the LXX.", "severity": "CRITICAL"},
        {"word": "Melchizedek (11Q13)", "hebrew": "מַלְכִּי־צֶדֶק", "issue": "11Q13 presents Melchizedek as an ELOHIM — a divine being who executes the judgment of Ps 82 against fallen gods. Not merely a human priest-king but a divine figure.", "severity": "CRITICAL"},
        {"word": "Sons of Light / Sons of Darkness", "hebrew": "בְּנֵי אוֹר / בְּנֵי חוֹשֶׁךְ", "issue": "The War Scroll (1QM) divides all reality into Sons of Light and Sons of Darkness — cosmic warfare between YHWH's camp and Belial's. The binary shapes NT language (John, Paul, 1 John).", "severity": "MAJOR"},
        {"word": "Belial", "hebrew": "בְּלִיַּעַל", "issue": "The DSS name for the chief adversary — distinct from ha-satan. Belial rules the Sons of Darkness. Paul uses the name once: 'What accord has Christ with Belial?' (2 Cor 6:15).", "severity": "MAJOR"},
    ],
    "hidden_connections": [
        {"target": "deuteronomy", "why": "4QDeut-j is THE textual witness: 'sons of God' at Deut 32:8 proves the MT 'sons of Israel' is a scribal alteration — the divine council allotment is original"},
        {"target": "psalms", "why": "11Q13 reads Ps 82 as Melchizedek judging the corrupt elohim — connecting Gen 14 → Ps 82 → Ps 110 into a continuous divine-figure narrative"},
        {"target": "hebrews", "why": "11Q13's divine Melchizedek illuminates Heb 7 — the Qumran community saw the same Melchizedek-as-divine-being connection that Hebrews develops christologically"},
        {"target": "genesis", "why": "The Genesis Apocryphon (1QapGen) retells patriarchal stories with expanded detail — parallel to Jubilees and Jasher in the gap-filling tradition"},
        {"target": "1enoch", "why": "Multiple copies of 1 Enoch found at Qumran (except the Parables) — the community treated it as authoritative. The Watcher tradition was mainstream, not fringe"},
        {"target": "isaiah", "why": "The Great Isaiah Scroll (1QIsa-a) is the oldest nearly complete OT manuscript — confirming the textual stability of Isaiah across 1,000 years"},
    ],
    "what_it_doesnt_say": [
        "The identity of the 'Teacher of Righteousness' — the community's founder is never named in any scroll",
        "Why the Qumran community separated from Jerusalem — the calendar dispute is clear but the triggering event is debated",
        "The scrolls never mention Jesus or early Christianity — the temporal overlap exists but direct connection is unproven",
        "How the community understood the relationship between Melchizedek (11Q13) and the Messiah(s) they expected — one figure or two?",
    ],
    "unusual_characters": [
        {"name": "Melchizedek (11Q13)", "ref": "11Q13", "detail": "Presented as a divine figure (elohim) who executes Ps 82 judgment, proclaims liberty in the final Jubilee, and atones for the Sons of Light. The Qumran community read Gen 14 as about a divine being.", "connections": ["genesis", "psalms", "hebrews"]},
        {"name": "Belial", "ref": "1QM, 1QS", "detail": "Prince of Darkness, ruler of the Sons of Darkness. The DSS chief adversary — distinct from ha-satan in the OT. Paul's only use: 'What accord has Christ with Belial?' (2 Cor 6:15).", "connections": ["2corinthians"]},
        {"name": "The Teacher of Righteousness", "ref": "CD, 1QpHab", "detail": "Unnamed founder of the community. Opposed by the 'Wicked Priest.' His identity is the biggest unsolved mystery of Dead Sea Scrolls scholarship.", "connections": []},
    ],
    "patterns": [
        "Cosmic dualism: every scroll assumes a warfare binary — Sons of Light vs. Sons of Darkness, Angel of Truth vs. Angel of Darkness, Michael vs. Belial. No neutrality exists",
        "Pesher interpretation: the scrolls read OT prophets as speaking about THEIR community and THEIR time — every prophecy has a present application. The NT does the same thing",
        "Calendar as theology: the 364-day solar calendar is not just practical but theological — the right calendar determines the right worship, which determines covenant faithfulness",
        "Textual preservation: the scrolls confirm both the stability of the biblical text (Isaiah scroll matches MT closely) and its variability (Deut 32:8 'sons of God' vs. MT 'sons of Israel')",
    ],
    "mistranslations": [
        {"english": "Dead Sea Scrolls", "original": "Various", "issue": "The collective label obscures the diversity — these are hundreds of distinct texts from multiple authors spanning 200+ years, not a single 'book'"},
        {"english": "sons of Israel", "original": "bene elohim", "issue": "The MT reading at Deut 32:8 is a scribal alteration — the DSS preserve the original 'sons of God' that the scribes changed to avoid divine council theology"},
    ],
}


# ── Injection logic ──────────────────────────────────────────────────────

def main():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    for book_id, fields in STRUCTURED.items():
        # Build the fields string
        lines = []
        for key in ["key_claim", "contested_words", "hidden_connections",
                     "what_it_doesnt_say", "unusual_characters", "patterns",
                     "mistranslations"]:
            if key not in fields:
                continue
            val = fields[key]
            lines.append(f'        "{key}": {repr(val)},')

        fields_block = "\n".join(lines)

        # Find the entry's body_html closing and inject after it
        # Pattern: body_html value ending with ''', followed by newline and "    },"
        # We need to find the specific entry by its id

        # Strategy: find "id": 'book_id' then find the next "}," that closes the dict
        id_pattern = f""""id": '{book_id}',"""
        id_pos = content.find(id_pattern)
        if id_pos == -1:
            # Try single quotes
            id_pattern = f""""id": '{book_id}',"""
            id_pos = content.find(id_pattern)
        if id_pos == -1:
            print(f"WARNING: Could not find entry for '{book_id}'")
            continue

        # Find the closing "}," for this entry
        # We need to find the next "}," that is at the proper indentation level
        # Look for "\n    }," after the id
        search_start = id_pos
        close_pattern = "\n    },"
        close_pos = content.find(close_pattern, search_start)
        if close_pos == -1:
            # Last entry might use "\n    }\n]"
            close_pattern = "\n    }\n]"
            close_pos = content.find(close_pattern, search_start)
            if close_pos == -1:
                print(f"WARNING: Could not find closing for '{book_id}'")
                continue

        # Check if this entry already has key_claim
        entry_text = content[id_pos:close_pos]
        if '"key_claim"' in entry_text:
            print(f"SKIP: '{book_id}' already has structured fields")
            continue

        # Insert the fields before the closing "},", i.e., right before close_pos
        # We want to insert after the last field line (body_html line)
        insert_pos = close_pos
        insertion = "\n" + fields_block
        content = content[:insert_pos] + insertion + content[insert_pos:]
        print(f"OK: Added structured fields to '{book_id}'")

    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\nDone. All structured fields injected.")

if __name__ == '__main__':
    main()
